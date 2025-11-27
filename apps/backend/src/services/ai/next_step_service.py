"""
Next Step Service
Phase 7.7: AI service layer with DB integration and caching
Phase 7.13: Added AI event logging for telemetry diagnostics
Phase 7.14: Added debug frames for error isolation
Phase 7.15: Added traceability and execution mapping
Phase 8.8: Added read-only data query engine integration

Provides the single most optimal next action recommendation
using real data from repositories and the deterministic rule engine.
Includes in-memory caching with TTL.
"""
import logging
from datetime import datetime, timedelta
from typing import Any, Optional
from uuid import UUID, uuid4

from shared.ai import (
    NextStepResponse,
    # Engine imports
    compute_recommendation_scores,
    UserContext,
    TaskData,
    ModuleData,
    StudyflowData,
)

from ...db import user_repository, module_repository, task_repository, progress_repository
from ...db.memory import USERS
from ...schemas.user import UserInDB
from ...ai_logs.logger import log_ai_event
from ...ai_diagnostics.debug_frames import build_debug_frame, log_debug_frame
from ...ai_trace.provenance import build_provenance_frame
from ...ai_trace.execution_map import record_execution
# Phase 8.8: Data query engine integration
from ...data.query.task_query import query_task_completions
from ...data.query.pattern_query import query_study_patterns

logger = logging.getLogger(__name__)

# Cache TTL constant (5 minutes)
CACHE_TTL_SECONDS = 300


class NextStepService:
    """
    Service for determining the single best next action for a user.

    Phase 7.7: Integrates with repositories for real user/module/task data.
    Uses compute_recommendation_scores to select the highest-scoring action.
    Includes in-memory caching with 5-minute TTL.
    """

    def __init__(self) -> None:
        """Initialize the next step service with cache."""
        self._cache: dict[str, dict[str, Any]] = {}
        logger.info("NextStepService initialized (engine=active, db=integrated, cache=active)")

    def get_next_step(
        self,
        user_id: Optional[UUID],
    ) -> NextStepResponse:
        """
        Determine the single most optimal next action for a user.

        Compares top-scored task, module, and studyflow from real data
        to select the best overall recommendation.

        Args:
            user_id: Optional user UUID for personalization

        Returns:
            NextStepResponse with the recommended action
        """
        errors: list[str] = []
        context_dict: dict[str, Any] = {}
        output_dict: Optional[dict[str, Any]] = None

        try:
            logger.info(f"get_next_step called: user_id={user_id}")

            # Build cache key
            cache_key = f"next_step:{user_id}"

            # Check cache
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                logger.debug(f"Cache hit for {cache_key}")
                return cached

            now = datetime.utcnow()

            # Resolve user
            user = self._resolve_user(user_id)
            resolved_user_id = user.id if user else None

            # Build context and load data
            user_ctx = self._build_user_context(user, resolved_user_id)
            context_dict = dict(user_ctx)  # Capture for debug frame
            modules = self._load_modules(resolved_user_id)
            tasks = self._load_tasks(resolved_user_id)
            studyflows = self._get_studyflow_options()

            # Compute scores
            scores = compute_recommendation_scores(user_ctx, modules, tasks, studyflows)

            # Determine best action by comparing top scores
            best_action = self._select_best_action(scores, user_ctx)

            logger.debug(
                f"Selected next_step: action_type={best_action['action_type']}, "
                f"score={best_action['score']}"
            )

            response = NextStepResponse(
                action_type=best_action["action_type"],
                action_id=best_action["action_id"],
                title=best_action["title"],
                description=best_action["description"],
                confidence=best_action["confidence"],
                estimated_duration=best_action["estimated_duration"],
                generated_at=now,
            )

            # Capture output for debug frame
            output_dict = {
                "action_type": best_action["action_type"],
                "action_id": best_action["action_id"],
                "confidence": best_action["confidence"],
            }

            # Store in cache
            self._store_in_cache(cache_key, response)

            # Phase 7.13: Log next_step event for telemetry
            request_id = str(uuid4())
            log_ai_event(
                event_type="next_step_selected",
                payload={
                    "action_type": best_action["action_type"],
                    "action_id": best_action["action_id"],
                    "confidence": best_action["confidence"],
                    "estimated_duration": best_action["estimated_duration"],
                },
                engine="next_step_service",
                request_id=request_id,
                user_id=str(resolved_user_id) if resolved_user_id else None,
            )

            # Phase 7.15: Build provenance and record execution
            build_provenance_frame(
                engine_name="next_step_service",
                context=context_dict,
                output=output_dict,
            )
            record_execution(
                engine_name="next_step_service",
                input_keys=list(context_dict.keys()) if context_dict else [],
                output_keys=list(output_dict.keys()) if output_dict else [],
            )

            return response

        except Exception as e:
            errors.append(f"NextStepService error: {str(e)}")
            logger.error(f"NextStepService exception: {e}")
            raise

        finally:
            # Phase 7.14: Always build and log debug frame
            frame = build_debug_frame(
                context=context_dict,
                engine="next_step_service",
                output=output_dict,
                errors=errors,
            )
            log_debug_frame(frame)

    def _resolve_user(self, user_id: Optional[UUID]) -> Optional[UserInDB]:
        """Resolve user from ID or fallback to first available user."""
        if user_id:
            user = user_repository.get_user_by_id(user_id)
            if user:
                return user

        if USERS:
            return next(iter(USERS.values()))

        return None

    def _select_best_action(
        self,
        scores: dict,
        user_ctx: UserContext,
    ) -> dict:
        """
        Select the best action from scored items.

        Compares task, module, and studyflow scores with type-based
        weighting to select the optimal next action.
        """
        candidates = []

        # Add top task
        if scores["top_task"]:
            top = scores["top_task"]
            task = top["task"]
            candidates.append({
                "action_type": "task",
                "action_id": task.get("id"),
                "title": f"Complete: {task.get('title', 'Task')}",
                "description": self._build_task_description(task, top["triggered_rules"]),
                "score": top["score"],
                "confidence": min(1.0, top["score"] / 100.0),
                "estimated_duration": task.get("estimated_minutes", 25),
            })

        # Add top module (weighted slightly lower - tasks are more actionable)
        if scores["top_module"]:
            top = scores["top_module"]
            module = top["module"]
            candidates.append({
                "action_type": "module",
                "action_id": module.get("id"),
                "title": f"Continue: {module.get('name', 'Module')}",
                "description": self._build_module_description(module, top["triggered_rules"]),
                "score": top["score"] * 0.9,
                "confidence": min(1.0, top["score"] / 100.0),
                "estimated_duration": 30,
            })

        # Add studyflow if user energy is low
        if scores["top_studyflow"]:
            top = scores["top_studyflow"]
            sf = top["studyflow"]
            sf_weight = 0.7
            if user_ctx.get("focus_energy") == "low":
                sf_weight = 1.1
            if user_ctx.get("available_minutes", 60) < 20:
                sf_weight = 1.0

            candidates.append({
                "action_type": "studyflow",
                "action_id": None,
                "title": f"Start: {sf.get('mode', 'pomodoro').capitalize()} Session",
                "description": self._build_studyflow_description(sf),
                "score": top["score"] * sf_weight,
                "confidence": min(1.0, top["score"] / 100.0),
                "estimated_duration": sf.get("duration", 25),
            })

        if not candidates:
            return {
                "action_type": "task",
                "action_id": None,
                "title": "Explore Learning Paths",
                "description": "No specific recommendations available. Browse modules to get started.",
                "score": 50.0,
                "confidence": 0.5,
                "estimated_duration": 15,
            }

        candidates.sort(key=lambda x: x["score"], reverse=True)
        best = candidates[0]
        best["confidence"] = round(best["confidence"], 2)
        return best

    def _build_task_description(self, task: TaskData, rules: list[str]) -> str:
        """Build description for task recommendation."""
        parts = []

        if task.get("module_id"):
            parts.append("Part of your current learning path.")

        if "urgent_deadline" in str(rules).lower():
            parts.append("This task has an upcoming deadline.")
        elif "high_priority" in str(rules).lower():
            parts.append("Marked as high priority.")

        difficulty = task.get("difficulty", "medium")
        parts.append(f"Difficulty: {difficulty}.")

        return " ".join(parts) if parts else "Continue your learning progress with this task."

    def _build_module_description(self, module: ModuleData, rules: list[str]) -> str:
        """Build description for module recommendation."""
        total = module.get("total_tasks", 0)
        completed = module.get("completed_tasks", 0)
        progress = int((completed / total * 100)) if total > 0 else 0

        if progress > 0:
            return f"You're {progress}% through this module. Keep the momentum going!"
        else:
            return f"Start this module to expand your skills. {total} tasks to complete."

    def _build_studyflow_description(self, sf: StudyflowData) -> str:
        """Build description for studyflow recommendation."""
        mode = sf.get("mode", "pomodoro")
        duration = sf.get("duration", 25)
        intensity = sf.get("intensity", "medium")

        descriptions = {
            "pomodoro": f"A focused {duration}-minute session with {intensity} intensity. Great for deep work.",
            "taskrunner": f"Power through tasks in {duration} minutes. High productivity mode.",
            "sprint": f"Quick {duration}-minute burst. Perfect for short breaks or warm-ups.",
        }
        return descriptions.get(mode, f"{mode.capitalize()} session for {duration} minutes.")

    def get_break_recommendation(self, user_id: UUID) -> NextStepResponse:
        """
        Check if user should take a break and return break recommendation.

        Args:
            user_id: User UUID to check

        Returns:
            NextStepResponse with break recommendation
        """
        logger.info(f"get_break_recommendation called: user_id={user_id}")

        now = datetime.utcnow()
        user = self._resolve_user(user_id)
        user_ctx = self._build_user_context(user, user_id)

        energy = user_ctx.get("focus_energy", "medium")
        time_of_day = user_ctx.get("time_of_day", "afternoon")

        if energy == "low" or time_of_day == "night":
            duration = 15
            title = "Take a longer break"
            description = "You've been working hard. A 15-minute break will help you recharge."
        elif energy == "high":
            duration = 5
            title = "Quick stretch break"
            description = "A short 5-minute break keeps you sharp. Stretch and refocus."
        else:
            duration = 10
            title = "Take a 10-minute break"
            description = "Step away for a bit. A balanced break improves retention."

        return NextStepResponse(
            action_type="break",
            action_id=None,
            title=title,
            description=description,
            confidence=0.75,
            estimated_duration=duration,
            generated_at=now,
        )

    def _build_user_context(
        self,
        user: Optional[UserInDB],
        user_id: Optional[UUID],
    ) -> UserContext:
        """Build user context from real user data and progress."""
        hour = datetime.utcnow().hour
        if hour < 12:
            time_of_day = "morning"
        elif hour < 18:
            time_of_day = "afternoon"
        elif hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"

        ctx: UserContext = {
            "user_id": str(user_id) if user_id else "anonymous",
            "skill_level": "intermediate",
            "streak_days": 0,
            "xp": 0,
            "completed_module_ids": [],
            "completed_task_ids": [],
            "focus_energy": "high" if hour < 16 else "medium",
            "time_of_day": time_of_day,
            "available_minutes": 45,
        }

        if not user_id:
            return ctx

        progress_records = progress_repository.list_progress_by_user(user_id)

        completed_modules = []
        completed_tasks = []

        for p in progress_records:
            if p.status == "completed":
                if p.module_id:
                    completed_modules.append(str(p.module_id))
                if p.task_id:
                    completed_tasks.append(str(p.task_id))

        ctx["completed_module_ids"] = completed_modules
        ctx["completed_task_ids"] = completed_tasks
        ctx["xp"] = len(completed_tasks) * 10 + len(completed_modules) * 50

        total_completions = len(completed_tasks) + len(completed_modules)
        if total_completions >= 20:
            ctx["skill_level"] = "advanced"
        elif total_completions >= 5:
            ctx["skill_level"] = "intermediate"
        else:
            ctx["skill_level"] = "beginner"

        # Phase 8.8: Enrich context with data query engine (read-only)
        try:
            completion_data = query_task_completions(str(user_id), days=7)
            if completion_data.get("totals"):
                ctx["_completion_stats"] = completion_data.get("totals", {})

            pattern_data = query_study_patterns(str(user_id), days=7)
            if pattern_data.get("has_data"):
                ctx["_study_patterns"] = pattern_data.get("patterns", {}).get("aggregates", {})
        except Exception as e:
            # Data enrichment is optional - log and continue
            logger.debug(f"Data enrichment skipped: {e}")

        return ctx

    def _load_modules(self, user_id: Optional[UUID]) -> list[ModuleData]:
        """Load modules from repository and convert to engine format."""
        db_modules = module_repository.list_modules()

        if not db_modules:
            return [
                {
                    "id": "sample-kubernetes-101",
                    "name": "Introduction to Kubernetes",
                    "difficulty": "medium",
                    "total_tasks": 12,
                    "completed_tasks": 0,
                    "prerequisites": [],
                    "category": "containers",
                },
            ]

        modules: list[ModuleData] = []
        for m in db_modules:
            if not m.is_active:
                continue

            module_tasks = task_repository.list_tasks_by_module(m.id)
            total_tasks = len(module_tasks)

            completed_tasks = 0
            if user_id:
                for t in module_tasks:
                    task_progress = progress_repository.get_progress_by_user_and_target(
                        user_id=user_id, task_id=t.id
                    )
                    if task_progress and task_progress.status == "completed":
                        completed_tasks += 1

            modules.append({
                "id": str(m.id),
                "name": m.name,
                "difficulty": "medium",
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "prerequisites": [],
                "category": "general",
            })

        return modules if modules else self._load_modules(None)

    def _load_tasks(self, user_id: Optional[UUID]) -> list[TaskData]:
        """Load tasks from repository and convert to engine format."""
        db_tasks = task_repository.list_tasks()

        if not db_tasks:
            now = datetime.utcnow()
            return [
                {
                    "id": "sample-task-k8s-001",
                    "title": "Deploy your first Pod",
                    "difficulty": "easy",
                    "priority": "high",
                    "module_id": "sample-kubernetes-101",
                    "due_date": (now + timedelta(days=2)).isoformat(),
                    "estimated_minutes": 20,
                    "prerequisites": [],
                },
            ]

        now = datetime.utcnow()
        completed_task_ids: set[UUID] = set()
        if user_id:
            for p in progress_repository.list_progress_by_user(user_id):
                if p.task_id and p.status == "completed":
                    completed_task_ids.add(p.task_id)

        tasks: list[TaskData] = []
        for t in db_tasks:
            if not t.is_active or t.id in completed_task_ids:
                continue

            tasks.append({
                "id": str(t.id),
                "title": t.title,
                "difficulty": t.difficulty,
                "priority": "medium",
                "module_id": str(t.module_id),
                "due_date": (now + timedelta(days=7)).isoformat(),
                "estimated_minutes": 25,
                "prerequisites": [],
            })

        return tasks if tasks else self._load_tasks(None)

    def _get_studyflow_options(self) -> list[StudyflowData]:
        """Get studyflow options."""
        return [
            {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
            {"mode": "taskrunner", "duration": 45, "intensity": "high"},
            {"mode": "sprint", "duration": 15, "intensity": "low"},
        ]

    # =========================================================================
    # ASYNC WORKER PATH (Phase 7.11)
    # =========================================================================

    def get_next_step_async(
        self,
        user_id: Optional[UUID],
        include_trace: bool = False,
    ) -> dict[str, Any]:
        """
        Determine next step via async worker path.

        Phase 7.11: Includes trace_id and performance metrics support.
        Builds payload and delegates to NextStepWorker stub.
        Includes strict result validation and error handling.
        Currently synchronous - async scheduling will be added later.

        Args:
            user_id: Optional user UUID for personalization
            include_trace: Whether to include trace metadata envelope

        Returns:
            WorkerResult dict with next step data
            If include_trace=True, returns {"data": {...}, "meta": {...}}

        Raises:
            HTTPException: If worker returns an error result
        """
        from fastapi import HTTPException

        from ...workers import NextStepWorker, NextStepPayload
        from ...workers.worker_protocol import validate_worker_result, ResultValidationError

        logger.info(f"get_next_step_async called: user_id={user_id}")

        # Build payload
        payload: NextStepPayload = {
            "user_id": str(user_id) if user_id else None,
        }

        # Invoke worker (direct call for now - no actual async)
        worker = NextStepWorker()
        result = worker.run(payload)  # type: ignore

        # Validate result structure
        try:
            validate_worker_result(result)  # type: ignore
        except ResultValidationError as e:
            logger.error(f"Worker result validation failed: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Worker result validation failed: {e}",
            )

        # Check for worker-level errors
        if not result["success"]:
            error = result["error"]
            error_message = error["message"] if error else "Unknown worker error"
            logger.error(f"Worker returned error: {error_message}")
            raise HTTPException(
                status_code=500,
                detail=error_message,
            )

        logger.debug(
            f"Worker result: success={result['success']}, "
            f"worker={result['metadata'].get('worker')}, "
            f"trace_id={result['metadata'].get('trace_id')}"
        )

        # Return with trace envelope if requested
        if include_trace:
            return {
                "data": result["data"],
                "meta": {
                    "trace_id": result["metadata"]["trace_id"],
                    "worker": result["metadata"]["worker"],
                    "task_type": result["metadata"]["task_type"],
                    "duration_ms": result["metadata"]["duration_ms"],
                    "timestamp": result["metadata"]["timestamp"],
                },
            }

        return result  # type: ignore

    def invalidate_cache(self, user_id: Optional[UUID] = None) -> int:
        """
        Invalidate cached next_step results for a user or all users.

        Args:
            user_id: User UUID whose cache should be invalidated.
                     If None, invalidates all next_step caches.

        Returns:
            Number of cache entries invalidated.
        """
        if user_id is None:
            count = len(self._cache)
            self._cache.clear()
            logger.info(f"invalidate_cache: cleared all {count} entries")
            return count

        key = f"next_step:{user_id}"
        if key in self._cache:
            del self._cache[key]
            logger.info(f"invalidate_cache: cleared entry for user_id={user_id}")
            return 1
        return 0

    def _get_from_cache(self, key: str) -> Optional[NextStepResponse]:
        """
        Get value from cache if exists and not expired.

        Args:
            key: Cache key to look up

        Returns:
            Cached value if valid, None otherwise
        """
        entry = self._cache.get(key)
        if entry is None:
            return None

        if datetime.utcnow() > entry["expires_at"]:
            del self._cache[key]
            logger.debug(f"Cache expired for key={key}")
            return None

        return entry["value"]

    def _store_in_cache(self, key: str, value: NextStepResponse) -> None:
        """
        Store value in cache with TTL.

        Args:
            key: Cache key
            value: Value to cache
        """
        self._cache[key] = {
            "value": value,
            "expires_at": datetime.utcnow() + timedelta(seconds=CACHE_TTL_SECONDS),
        }
        logger.debug(f"Cached value for key={key}")
