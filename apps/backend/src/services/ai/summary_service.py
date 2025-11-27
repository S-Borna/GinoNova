"""
Summary Service
Phase 7.7: AI service layer with DB integration and caching
Phase 7.13: Added AI event logging for telemetry diagnostics
Phase 7.14: Added debug frames for error isolation
Phase 7.15: Added traceability and execution mapping

Generates AI-powered daily and weekly summaries using real data
from repositories and the deterministic rule engine.
Includes in-memory caching with TTL.
"""
import logging
from datetime import datetime, timedelta
from typing import Any, Optional
from uuid import UUID, uuid4

from shared.ai import (
    DailySummaryResponse,
    SummaryHighlight,
    # Engine imports
    compute_daily_highlights,
    UserContext,
    ProgressData,
)

from ...db import user_repository, module_repository, task_repository, progress_repository
from ...db.memory import USERS
from ...schemas.user import UserInDB
from ...schemas.progress import ProgressInDB
from ...ai_logs.logger import log_ai_event
from ...ai_diagnostics.debug_frames import build_debug_frame, log_debug_frame
from ...ai_trace.provenance import build_provenance_frame
from ...ai_trace.execution_map import record_execution

logger = logging.getLogger(__name__)

# Cache TTL constant (5 minutes)
CACHE_TTL_SECONDS = 300


class SummaryService:
    """
    Service for generating AI-powered learning summaries.

    Phase 7.7: Integrates with repositories for real progress data.
    Uses compute_daily_highlights from the rule engine.
    Includes in-memory caching with 5-minute TTL.
    """

    def __init__(self) -> None:
        """Initialize the summary service with cache."""
        self._cache: dict[str, dict[str, Any]] = {}
        logger.info("SummaryService initialized (engine=active, db=integrated, cache=active)")

    def get_daily_summary(
        self,
        user_id: Optional[UUID],
    ) -> DailySummaryResponse:
        """
        Generate a daily learning summary for a user.

        Uses real progress data from repository combined with rule engine
        to compute highlights and metrics.

        Args:
            user_id: Optional user UUID for personalized summary

        Returns:
            DailySummaryResponse with full daily summary
        """
        errors: list[str] = []
        context_dict: dict[str, Any] = {}
        output_dict: Optional[dict[str, Any]] = None

        try:
            logger.info(f"get_daily_summary called: user_id={user_id}")

            now = datetime.utcnow()
            today = now.strftime("%Y-%m-%d")

            # Build cache key
            cache_key = f"summary:{user_id}:{today}"

            # Check cache
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                logger.debug(f"Cache hit for {cache_key}")
                return cached

            # Resolve user
            user = self._resolve_user(user_id)
            resolved_user_id = user.id if user else None

            # Build context and progress data from real DB
            user_ctx = self._build_user_context(user, resolved_user_id)
            progress = self._build_progress_data(resolved_user_id)
            context_dict = dict(user_ctx)  # Capture for debug frame

            # Compute highlights using rule engine
            raw_highlights = compute_daily_highlights(user_ctx, progress)

            logger.debug(f"Computed {len(raw_highlights)} highlights from DB data")

            # Convert engine highlights to schema highlights
            highlights = [
                SummaryHighlight(
                    type=h["type"],
                    title=h["title"],
                    description=h["description"],
                    metric=h.get("metric"),
                )
                for h in raw_highlights
            ]

            # Generate greeting based on time and progress
            greeting = self._generate_greeting(user_ctx, progress)

            # Generate motivation message
            motivation = self._generate_motivation(user_ctx, progress)

            response = DailySummaryResponse(
                date=today,
                greeting=greeting,
                highlights=highlights,
                tasks_completed=progress.get("tasks_completed_today", 0),
                xp_earned=progress.get("xp_earned_today", 0),
                study_minutes=progress.get("study_minutes_today", 0),
                streak_days=progress.get("streak_days", 0),
                motivation_message=motivation,
                generated_at=now,
            )

            # Capture output for debug frame
            output_dict = {
                "date": today,
                "highlights_count": len(highlights),
                "tasks_completed": response.tasks_completed,
                "xp_earned": response.xp_earned,
            }

            # Store in cache
            self._store_in_cache(cache_key, response)

            # Phase 7.13: Log summary event for telemetry
            request_id = str(uuid4())
            log_ai_event(
                event_type="summary_generated",
                payload={
                    "date": today,
                    "highlights_count": len(highlights),
                    "tasks_completed": response.tasks_completed,
                    "xp_earned": response.xp_earned,
                    "streak_days": response.streak_days,
                },
                engine="summary_service",
                request_id=request_id,
                user_id=str(resolved_user_id) if resolved_user_id else None,
            )

            # Phase 7.15: Build provenance and record execution
            build_provenance_frame(
                engine_name="summary_service",
                context=context_dict,
                output=output_dict,
            )
            record_execution(
                engine_name="summary_service",
                input_keys=list(context_dict.keys()) if context_dict else [],
                output_keys=list(output_dict.keys()) if output_dict else [],
            )

            logger.debug(
                f"Returning daily summary: date={response.date}, "
                f"tasks={response.tasks_completed}, xp={response.xp_earned}"
            )
            return response

        except Exception as e:
            errors.append(f"SummaryService error: {str(e)}")
            logger.error(f"SummaryService exception: {e}")
            raise

        finally:
            # Phase 7.14: Always build and log debug frame
            frame = build_debug_frame(
                context=context_dict,
                engine="summary_service",
                output=output_dict,
                errors=errors,
            )
            log_debug_frame(frame)
        return response

    def get_weekly_summary(
        self,
        user_id: UUID,
    ) -> dict:
        """
        Generate a weekly learning summary for a user.

        Args:
            user_id: User UUID for personalized summary

        Returns:
            Dictionary with weekly summary data
        """
        logger.info(f"get_weekly_summary called: user_id={user_id}")

        now = datetime.utcnow()
        progress = self._build_weekly_progress_data(user_id)

        total_tasks = progress.get("tasks_completed_week", 0)
        total_xp = progress.get("xp_earned_week", 0)
        total_minutes = progress.get("study_minutes_week", 0)
        streak = progress.get("streak_days", 0)

        if total_tasks >= 15 and total_minutes >= 300:
            quality = "exceptional"
            message = "Outstanding week! You're making incredible progress."
        elif total_tasks >= 10 or total_minutes >= 180:
            quality = "great"
            message = "Great week! Keep building on this momentum."
        elif total_tasks >= 5 or total_minutes >= 60:
            quality = "good"
            message = "Solid progress this week. Every step counts!"
        else:
            quality = "needs_improvement"
            message = "Room to grow! Try setting smaller daily goals next week."

        # Calculate week start/end
        week_start = (now - timedelta(days=now.weekday())).strftime("%Y-%m-%d")
        week_end = (now + timedelta(days=6 - now.weekday())).strftime("%Y-%m-%d")

        return {
            "week_start": week_start,
            "week_end": week_end,
            "status": "computed",
            "quality": quality,
            "tasks_completed": total_tasks,
            "xp_earned": total_xp,
            "study_minutes": total_minutes,
            "streak_days": streak,
            "message": message,
            "generated_at": now.isoformat(),
        }

    def generate_motivation_message(
        self,
        user_id: UUID,
        context: str = "general",
    ) -> str:
        """
        Generate a contextual motivation message.

        Args:
            user_id: User UUID for personalization
            context: Context for the message

        Returns:
            Motivational message string
        """
        logger.info(
            f"generate_motivation_message called: "
            f"user_id={user_id}, context={context}"
        )

        user = self._resolve_user(user_id)
        user_ctx = self._build_user_context(user, user_id)
        streak = user_ctx.get("streak_days", 0)
        xp = user_ctx.get("xp", 0)

        messages = {
            "general": self._general_motivation(streak, xp),
            "streak": self._streak_motivation(streak),
            "achievement": "Congratulations on your achievement! You're crushing it!",
            "comeback": "Welcome back! Ready to continue your learning journey?",
            "milestone": "You've reached a milestone! Time to celebrate your progress.",
            "morning": "Fresh start to the day! Great time for focused learning.",
            "evening": "Wind down with some light review. Consistency beats intensity.",
        }

        return messages.get(context, messages["general"])

    def _resolve_user(self, user_id: Optional[UUID]) -> Optional[UserInDB]:
        """Resolve user from ID or fallback to first available user."""
        if user_id:
            user = user_repository.get_user_by_id(user_id)
            if user:
                return user

        if USERS:
            return next(iter(USERS.values()))

        return None

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

        return ctx

    def _build_progress_data(self, user_id: Optional[UUID]) -> ProgressData:
        """
        Build progress data from real DB records.

        Args:
            user_id: User ID to load progress for

        Returns:
            ProgressData dict for engine computation
        """
        if not user_id:
            # Return minimal data for anonymous users
            return {
                "tasks_completed_today": 0,
                "xp_earned_today": 0,
                "study_minutes_today": 0,
                "streak_days": 0,
                "modules_in_progress": [],
                "recent_achievements": [],
            }

        # Get all progress records for user
        progress_records = progress_repository.list_progress_by_user(user_id)
        now = datetime.utcnow()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        # Count today's completions
        tasks_completed_today = 0
        for p in progress_records:
            if p.task_id and p.status == "completed":
                if p.updated_at >= today_start:
                    tasks_completed_today += 1

        # Calculate XP (10 per task completed today)
        xp_earned_today = tasks_completed_today * 10

        # Build modules in progress
        modules_in_progress = []
        db_modules = module_repository.list_modules()

        for m in db_modules:
            if not m.is_active:
                continue

            module_tasks = task_repository.list_tasks_by_module(m.id)
            total_tasks = len(module_tasks)
            completed_tasks = 0

            for t in module_tasks:
                task_progress = progress_repository.get_progress_by_user_and_target(
                    user_id=user_id, task_id=t.id
                )
                if task_progress and task_progress.status == "completed":
                    completed_tasks += 1

            if 0 < completed_tasks < total_tasks:
                modules_in_progress.append({
                    "id": str(m.id),
                    "name": m.name,
                    "total_tasks": total_tasks,
                    "completed_tasks": completed_tasks,
                })

        # Count completed modules for achievements
        completed_modules = []
        for m in db_modules:
            module_tasks = task_repository.list_tasks_by_module(m.id)
            if not module_tasks:
                continue

            all_completed = True
            for t in module_tasks:
                task_prog = progress_repository.get_progress_by_user_and_target(
                    user_id=user_id, task_id=t.id
                )
                if not task_prog or task_prog.status != "completed":
                    all_completed = False
                    break

            if all_completed:
                completed_modules.append(f"Completed {m.name} module")

        # Calculate streak (simplified - days with activity)
        streak_days = self._calculate_streak(progress_records)

        return {
            "tasks_completed_today": tasks_completed_today,
            "xp_earned_today": xp_earned_today,
            "study_minutes_today": tasks_completed_today * 15,  # Estimate 15 min per task
            "streak_days": streak_days,
            "modules_in_progress": modules_in_progress,
            "recent_achievements": completed_modules[:3],
        }

    def _build_weekly_progress_data(self, user_id: UUID) -> dict:
        """Build weekly aggregated progress data."""
        progress_records = progress_repository.list_progress_by_user(user_id)
        now = datetime.utcnow()
        week_start = now - timedelta(days=now.weekday())
        week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)

        tasks_completed_week = 0
        for p in progress_records:
            if p.task_id and p.status == "completed":
                if p.updated_at >= week_start:
                    tasks_completed_week += 1

        xp_earned_week = tasks_completed_week * 10
        study_minutes_week = tasks_completed_week * 15
        streak_days = self._calculate_streak(progress_records)

        return {
            "tasks_completed_week": tasks_completed_week,
            "xp_earned_week": xp_earned_week,
            "study_minutes_week": study_minutes_week,
            "streak_days": streak_days,
        }

    def _calculate_streak(self, progress_records: list[ProgressInDB]) -> int:
        """
        Calculate current streak from progress records.

        Simple algorithm: count consecutive days with completed tasks
        going backwards from today.
        """
        if not progress_records:
            return 0

        # Get all completion dates
        completion_dates: set[str] = set()
        for p in progress_records:
            if p.status == "completed" and p.task_id:
                completion_dates.add(p.updated_at.strftime("%Y-%m-%d"))

        if not completion_dates:
            return 0

        # Count consecutive days
        streak = 0
        current_date = datetime.utcnow().date()

        while True:
            date_str = current_date.strftime("%Y-%m-%d")
            if date_str in completion_dates:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break

        return streak

    def _generate_greeting(
        self,
        user_ctx: UserContext,
        progress: ProgressData,
    ) -> str:
        """Generate personalized greeting based on context."""
        time_of_day = user_ctx.get("time_of_day", "afternoon")
        tasks = progress.get("tasks_completed_today", 0)

        greetings = {
            "morning": "Good morning! Ready to learn something new?",
            "afternoon": "Good afternoon! Here's your progress update.",
            "evening": "Good evening! Let's review your day.",
            "night": "Working late? Here's what you've accomplished.",
        }

        base_greeting = greetings.get(time_of_day, "Hello!")

        if tasks >= 5:
            return f"{base_greeting} Incredible productivity today!"
        elif tasks >= 3:
            return f"{base_greeting} Great progress so far!"
        elif tasks > 0:
            return f"{base_greeting} You're making progress!"
        else:
            return base_greeting

    def _generate_motivation(
        self,
        user_ctx: UserContext,
        progress: ProgressData,
    ) -> str:
        """Generate motivation message based on progress."""
        streak = progress.get("streak_days", 0)
        tasks = progress.get("tasks_completed_today", 0)
        xp = progress.get("xp_earned_today", 0)

        if streak >= 7 and tasks >= 3:
            return "You're on fire! Your consistency is paying off. Keep this momentum going!"
        elif streak >= 7:
            return f"Amazing {streak}-day streak! Consistency is the key to mastery."
        elif tasks >= 5:
            return "Productivity champion! You've crushed it today."
        elif xp >= 200:
            return "Great XP gains! You're leveling up fast."
        elif tasks >= 1:
            return "Every task completed is a step forward. Keep it up!"
        else:
            return "Ready to start? Even 15 minutes of focused learning makes a difference."

    def _general_motivation(self, streak: int, xp: int) -> str:
        """Generate general motivation based on stats."""
        if streak >= 14:
            return f"Two weeks strong! Your {streak}-day streak shows true dedication."
        elif streak >= 7:
            return "A full week of learning! You're building great habits."
        elif xp >= 5000:
            return "Over 5000 XP! You're becoming a DevOps expert."
        elif xp >= 1000:
            return "Solid progress! Keep building your knowledge base."
        else:
            return "Keep up the great work! Every step forward counts."

    def _streak_motivation(self, streak: int) -> str:
        """Generate streak-specific motivation."""
        if streak >= 30:
            return f"Legendary {streak}-day streak! You're in the top tier of learners."
        elif streak >= 14:
            return f"Two weeks and counting! {streak} days of dedication."
        elif streak >= 7:
            return f"One week milestone! {streak} days of consistent learning."
        elif streak >= 3:
            return f"{streak} days in a row! Building momentum."
        elif streak > 0:
            return "Streak started! Come back tomorrow to keep it going."
        else:
            return "Start a new streak today! Consistency beats intensity."

    # =========================================================================
    # ASYNC WORKER PATH (Phase 7.11)
    # =========================================================================

    def get_daily_summary_async(
        self,
        user_id: Optional[UUID],
        include_trace: bool = False,
    ) -> dict[str, Any]:
        """
        Generate daily summary via async worker path.

        Phase 7.11: Includes trace_id and performance metrics support.
        Builds payload and delegates to SummaryWorker stub.
        Includes strict result validation and error handling.
        Currently synchronous - async scheduling will be added later.

        Args:
            user_id: Optional user UUID for personalized summary
            include_trace: Whether to include trace metadata envelope

        Returns:
            WorkerResult dict with summary data
            If include_trace=True, returns {"data": {...}, "meta": {...}}

        Raises:
            HTTPException: If worker returns an error result
        """
        from fastapi import HTTPException

        from ...workers import SummaryWorker, SummaryPayload
        from ...workers.worker_protocol import validate_worker_result, ResultValidationError

        logger.info(f"get_daily_summary_async called: user_id={user_id}")

        # Build payload
        payload: SummaryPayload = {
            "user_id": str(user_id) if user_id else None,
        }

        # Invoke worker (direct call for now - no actual async)
        worker = SummaryWorker()
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
        Invalidate cached summaries for a user or all users.

        Args:
            user_id: User UUID whose cache should be invalidated.
                     If None, invalidates all summary caches.

        Returns:
            Number of cache entries invalidated.
        """
        if user_id is None:
            count = len(self._cache)
            self._cache.clear()
            logger.info(f"invalidate_cache: cleared all {count} entries")
            return count

        prefix = f"summary:{user_id}:"
        keys_to_remove = [k for k in self._cache if k.startswith(prefix)]
        for key in keys_to_remove:
            del self._cache[key]
        logger.info(f"invalidate_cache: cleared {len(keys_to_remove)} entries for user_id={user_id}")
        return len(keys_to_remove)

    def _get_from_cache(self, key: str) -> Optional[DailySummaryResponse]:
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

    def _store_in_cache(self, key: str, value: DailySummaryResponse) -> None:
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
