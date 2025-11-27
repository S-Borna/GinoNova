"""
Recommendation Service
Phase 7.7: AI service layer with DB integration and caching
Phase 7.13: Added AI event logging for telemetry diagnostics
Phase 7.14: Added debug frames for error isolation
Phase 7.15: Added traceability and execution mapping
Phase 8.8: Added read-only data query engine integration

Provides personalized task, module, and studyflow recommendations
using real data from repositories and the deterministic rule engine.
Includes in-memory caching with TTL.
"""
import logging
import time
from datetime import datetime, timedelta
from typing import Any, Optional
from uuid import UUID, uuid4

from shared.ai import (
    TaskRecommendation,
    ModuleRecommendation,
    StudyflowRecommendation,
    Recommendations,
    RecommendationsResponse,
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
from ...schemas.progress import ProgressInDB
from ...ai_logs.logger import log_ai_event
from ...ai_diagnostics.debug_frames import build_debug_frame, log_debug_frame
from ...ai_trace.provenance import build_provenance_frame
from ...ai_trace.execution_map import record_execution
# Phase 8.8: Data query engine integration
from ...data.query.task_query import get_task_summary
from ...data.query.pattern_query import query_peak_hours

logger = logging.getLogger(__name__)

# Cache TTL constant (5 minutes)
CACHE_TTL_SECONDS = 300


class RecommendationService:
    """
    Service for generating personalized AI recommendations.

    Phase 7.7: Integrates with repositories for real user/module/task data.
    Uses compute_recommendation_scores from the rule engine.
    Includes in-memory caching with 5-minute TTL.
    """

    def __init__(self) -> None:
        """Initialize the recommendation service with cache."""
        self._cache: dict[str, dict[str, Any]] = {}
        logger.info("RecommendationService initialized (engine=active, db=integrated, cache=active)")

    def get_recommendations(
        self,
        user_id: Optional[UUID],
        limit: int = 5,
        include_reasoning: bool = False,
    ) -> RecommendationsResponse:
        """
        Generate personalized recommendations for a user.

        Uses real data from repositories combined with the deterministic
        rule engine to score and rank all available entities.

        Args:
            user_id: Optional user UUID for personalization
            limit: Maximum number of recommendations per category
            include_reasoning: Whether to include explanation text

        Returns:
            RecommendationsResponse with task, module, and studyflow suggestions
        """
        errors: list[str] = []
        context_dict: dict[str, Any] = {}
        output_dict: Optional[dict[str, Any]] = None

        try:
            logger.info(
                f"get_recommendations called: user_id={user_id}, "
                f"limit={limit}, include_reasoning={include_reasoning}"
            )

            # Build cache key
            cache_key = f"recommendations:{user_id}:{include_reasoning}"

            # Check cache
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                logger.debug(f"Cache hit for {cache_key}")
                return cached

            now = datetime.utcnow()

            # Resolve user (use provided or fallback to first user)
            user = self._resolve_user(user_id)
            resolved_user_id = user.id if user else None

            # Build user context from real data
            user_ctx: UserContext = self._build_user_context(user, resolved_user_id)
            context_dict = dict(user_ctx)  # Capture for debug frame

            # Load real data from repositories
            modules = self._load_modules(resolved_user_id)
            tasks = self._load_tasks(resolved_user_id)
            studyflows = self._get_studyflow_options()

            # Compute scores using rule engine
            scores = compute_recommendation_scores(user_ctx, modules, tasks, studyflows)

            logger.debug(
                f"Engine scores computed: "
                f"top_task={scores['top_task']['score'] if scores['top_task'] else 'N/A'}, "
                f"top_module={scores['top_module']['score'] if scores['top_module'] else 'N/A'}, "
                f"modules_count={len(modules)}, tasks_count={len(tasks)}"
            )

            # Build response from top scored items
            next_task: Optional[TaskRecommendation] = None
            next_module: Optional[ModuleRecommendation] = None
            studyflow: Optional[StudyflowRecommendation] = None

            if scores["top_task"]:
                top = scores["top_task"]
                task_data = top["task"]
                confidence = min(1.0, top["score"] / 100.0)
                reason = None
                if include_reasoning and top["triggered_rules"]:
                    reason = f"Selected based on: {', '.join(top['triggered_rules'][:3])}"

                next_task = TaskRecommendation(
                    task_id=task_data.get("id", "task-001"),
                    title=task_data.get("title", "Recommended Task"),
                    confidence=round(confidence, 2),
                    reason=reason,
                )

            if scores["top_module"]:
                top = scores["top_module"]
                module_data = top["module"]
                confidence = min(1.0, top["score"] / 100.0)
                reason = None
                if include_reasoning and top["triggered_rules"]:
                    reason = f"Selected based on: {', '.join(top['triggered_rules'][:3])}"

                next_module = ModuleRecommendation(
                    module_id=module_data.get("id", "module-001"),
                    name=module_data.get("name", "Recommended Module"),
                    confidence=round(confidence, 2),
                    reason=reason,
                )

            if scores["top_studyflow"]:
                top = scores["top_studyflow"]
                sf_data = top["studyflow"]
                studyflow = StudyflowRecommendation(
                    mode=sf_data.get("mode", "pomodoro"),
                    duration=sf_data.get("duration", 25),
                    intensity=sf_data.get("intensity", "medium"),
                )

            recommendations = Recommendations(
                next_task=next_task,
                next_module=next_module,
                studyflow=studyflow,
            )

            response = RecommendationsResponse(
                recommendations=recommendations,
                generated_at=now,
                expires_at=now + timedelta(minutes=10),
            )

            # Capture output for debug frame
            output_dict = {
                "has_task": next_task is not None,
                "has_module": next_module is not None,
                "has_studyflow": studyflow is not None,
            }

            # Store in cache
            self._store_in_cache(cache_key, response)

            # Phase 7.13: Log recommendation event for telemetry
            request_id = str(uuid4())
            log_ai_event(
                event_type="recommendation_generated",
                payload={
                    "type": "personalized" if user_id else "anonymous",
                    "limit": limit,
                    "include_reasoning": include_reasoning,
                    "has_task": response.recommendations.next_task is not None,
                    "has_module": response.recommendations.next_module is not None,
                    "has_studyflow": response.recommendations.studyflow is not None,
                },
                engine="recommendation_service",
                request_id=request_id,
                user_id=str(resolved_user_id) if resolved_user_id else None,
            )

            # Phase 7.15: Build provenance and record execution
            build_provenance_frame(
                engine_name="recommendation_service",
                context=context_dict,
                output=output_dict,
            )
            record_execution(
                engine_name="recommendation_service",
                input_keys=list(context_dict.keys()) if context_dict else [],
                output_keys=list(output_dict.keys()) if output_dict else [],
            )

            logger.debug(f"Returning recommendations: {response.model_dump_json()[:200]}...")
            return response

        except Exception as e:
            errors.append(f"RecommendationService error: {str(e)}")
            logger.error(f"RecommendationService exception: {e}")
            raise

        finally:
            # Phase 7.14: Always build and log debug frame
            frame = build_debug_frame(
                context=context_dict,
                engine="recommendation_service",
                output=output_dict,
                errors=errors,
            )
            log_debug_frame(frame)

    def _resolve_user(self, user_id: Optional[UUID]) -> Optional[UserInDB]:
        """
        Resolve user from ID or fallback to first available user.

        Args:
            user_id: Optional user UUID

        Returns:
            UserInDB if found, None otherwise
        """
        if user_id:
            user = user_repository.get_user_by_id(user_id)
            if user:
                return user

        # Fallback: get first user from in-memory store
        if USERS:
            return next(iter(USERS.values()))

        return None

    def _build_user_context(
        self,
        user: Optional[UserInDB],
        user_id: Optional[UUID],
    ) -> UserContext:
        """
        Build user context from real user data and progress.

        Args:
            user: User object if found
            user_id: User ID for progress lookup

        Returns:
            UserContext dict for engine scoring
        """
        hour = datetime.utcnow().hour
        if hour < 12:
            time_of_day = "morning"
        elif hour < 18:
            time_of_day = "afternoon"
        elif hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"

        # Default context
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

        # Phase 8.8: Enrich context with data query engine (read-only)
        try:
            task_summary = get_task_summary(str(user_id))
            if task_summary.get("has_data"):
                summary = task_summary.get("summary", {})
                # Enrich with historical data (does not change AI output structure)
                ctx["_data_enrichment"] = {
                    "total_events": task_summary.get("total_events", 0),
                    "preferred_difficulty": summary.get("preferred_difficulty", "medium"),
                    "peak_hour": summary.get("peak_hour"),
                }
            
            peak_hours_data = query_peak_hours(str(user_id))
            if peak_hours_data.get("has_data"):
                ctx["_peak_hours"] = peak_hours_data.get("peak_hours", [])
        except Exception as e:
            # Data enrichment is optional - log and continue
            logger.debug(f"Data enrichment skipped: {e}")

        # Load real progress data
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

        # Calculate XP (10 XP per completed task, 50 XP per completed module)
        ctx["xp"] = len(completed_tasks) * 10 + len(completed_modules) * 50

        # Estimate skill level based on completions
        total_completions = len(completed_tasks) + len(completed_modules)
        if total_completions >= 20:
            ctx["skill_level"] = "advanced"
        elif total_completions >= 5:
            ctx["skill_level"] = "intermediate"
        else:
            ctx["skill_level"] = "beginner"

        return ctx

    def _load_modules(self, user_id: Optional[UUID]) -> list[ModuleData]:
        """
        Load modules from repository and convert to engine format.

        Args:
            user_id: User ID for progress lookup

        Returns:
            List of ModuleData dicts for engine scoring
        """
        db_modules = module_repository.list_modules()

        if not db_modules:
            # Return sample data if no modules exist
            return self._get_sample_modules()

        # Get user progress for modules
        user_progress: dict[UUID, ProgressInDB] = {}
        if user_id:
            for p in progress_repository.list_progress_by_user(user_id):
                if p.module_id:
                    user_progress[p.module_id] = p

        modules: list[ModuleData] = []
        for m in db_modules:
            if not m.is_active:
                continue

            # Count tasks in module
            module_tasks = task_repository.list_tasks_by_module(m.id)
            total_tasks = len(module_tasks)

            # Get completed tasks count
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
                "difficulty": "medium",  # Default, can be extended later
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "prerequisites": [],
                "category": "general",
            })

        return modules if modules else self._get_sample_modules()

    def _load_tasks(self, user_id: Optional[UUID]) -> list[TaskData]:
        """
        Load tasks from repository and convert to engine format.

        Args:
            user_id: User ID for progress lookup

        Returns:
            List of TaskData dicts for engine scoring
        """
        db_tasks = task_repository.list_tasks()

        if not db_tasks:
            # Return sample data if no tasks exist
            return self._get_sample_tasks()

        now = datetime.utcnow()

        # Get user completed tasks
        completed_task_ids: set[UUID] = set()
        if user_id:
            for p in progress_repository.list_progress_by_user(user_id):
                if p.task_id and p.status == "completed":
                    completed_task_ids.add(p.task_id)

        tasks: list[TaskData] = []
        for t in db_tasks:
            if not t.is_active:
                continue
            if t.id in completed_task_ids:
                continue  # Skip completed tasks

            tasks.append({
                "id": str(t.id),
                "title": t.title,
                "difficulty": t.difficulty,
                "priority": "medium",  # Default priority
                "module_id": str(t.module_id),
                "due_date": (now + timedelta(days=7)).isoformat(),  # Default deadline
                "estimated_minutes": 25,  # Default estimate
                "prerequisites": [],
            })

        return tasks if tasks else self._get_sample_tasks()

    def _get_sample_modules(self) -> list[ModuleData]:
        """Return sample modules when DB is empty."""
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
            {
                "id": "sample-ci-cd-pipelines",
                "name": "CI/CD Pipeline Fundamentals",
                "difficulty": "medium",
                "total_tasks": 10,
                "completed_tasks": 0,
                "prerequisites": [],
                "category": "devops",
            },
        ]

    def _get_sample_tasks(self) -> list[TaskData]:
        """Return sample tasks when DB is empty."""
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
            {
                "id": "sample-task-cicd-001",
                "title": "Configure GitHub Actions workflow",
                "difficulty": "medium",
                "priority": "medium",
                "module_id": "sample-ci-cd-pipelines",
                "due_date": (now + timedelta(days=5)).isoformat(),
                "estimated_minutes": 35,
                "prerequisites": [],
            },
        ]

    def _get_studyflow_options(self) -> list[StudyflowData]:
        """Get available studyflow configurations."""
        return [
            {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
            {"mode": "taskrunner", "duration": 45, "intensity": "high"},
            {"mode": "sprint", "duration": 15, "intensity": "low"},
        ]

    # =========================================================================
    # ASYNC WORKER PATH (Phase 7.11)
    # =========================================================================

    def get_recommendations_async(
        self,
        user_id: Optional[UUID],
        limit: int = 5,
        include_reasoning: bool = False,
        include_trace: bool = False,
    ) -> dict[str, Any]:
        """
        Generate recommendations via async worker path.

        Phase 7.11: Includes trace_id and performance metrics support.
        Builds payload and delegates to RecommendWorker stub.
        Includes strict result validation and error handling.
        Currently synchronous - async scheduling will be added later.

        Args:
            user_id: Optional user UUID for personalization
            limit: Maximum number of recommendations per category
            include_reasoning: Whether to include explanation text
            include_trace: Whether to include trace metadata envelope

        Returns:
            WorkerResult dict with recommendations data
            If include_trace=True, returns {"data": {...}, "meta": {...}}

        Raises:
            HTTPException: If worker returns an error result
        """
        from fastapi import HTTPException

        from ...workers import RecommendWorker, RecommendPayload
        from ...workers.worker_protocol import validate_worker_result, ResultValidationError

        logger.info(
            f"get_recommendations_async called: user_id={user_id}, "
            f"limit={limit}, include_reasoning={include_reasoning}"
        )

        # Build payload
        payload: RecommendPayload = {
            "user_id": str(user_id) if user_id else None,
            "limit": limit,
            "include_reasoning": include_reasoning,
        }

        # Invoke worker (direct call for now - no actual async)
        worker = RecommendWorker()
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
        Invalidate cached recommendations for a user or all users.

        Args:
            user_id: User UUID whose cache should be invalidated.
                     If None, invalidates all recommendation caches.

        Returns:
            Number of cache entries invalidated.
        """
        if user_id is None:
            count = len(self._cache)
            self._cache.clear()
            logger.info(f"invalidate_cache: cleared all {count} entries")
            return count

        prefix = f"recommendations:{user_id}:"
        keys_to_remove = [k for k in self._cache if k.startswith(prefix)]
        for key in keys_to_remove:
            del self._cache[key]
        logger.info(f"invalidate_cache: cleared {len(keys_to_remove)} entries for user_id={user_id}")
        return len(keys_to_remove)

    def _get_from_cache(self, key: str) -> Optional[RecommendationsResponse]:
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

    def _store_in_cache(self, key: str, value: RecommendationsResponse) -> None:
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
