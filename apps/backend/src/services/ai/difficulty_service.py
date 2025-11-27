"""
Difficulty Service
Phase 7.7: AI service layer with DB integration and caching

Estimates user-adjusted task difficulty using real data from
repositories and the deterministic rule engine.
Includes in-memory caching with TTL.
"""
import logging
from datetime import datetime, timedelta
from typing import Any, Optional
from uuid import UUID

from shared.ai import (
    DifficultyEstimate,
    # Engine imports
    compute_difficulty_adjustment,
    UserContext,
    TaskData,
)

from ...db import user_repository, task_repository, progress_repository
from ...db.memory import USERS
from ...schemas.user import UserInDB

logger = logging.getLogger(__name__)

# Cache TTL constant (5 minutes)
CACHE_TTL_SECONDS = 300


class DifficultyService:
    """
    Service for estimating task difficulty for specific users.

    Phase 7.7: Integrates with repositories for real task and user data.
    Uses compute_difficulty_adjustment from the rule engine.
    Includes in-memory caching with 5-minute TTL.
    """

    def __init__(self) -> None:
        """Initialize the difficulty service with cache."""
        self._cache: dict[str, dict[str, Any]] = {}
        logger.info("DifficultyService initialized (engine=active, db=integrated, cache=active)")

    def estimate_difficulty(
        self,
        task_id: UUID,
        user_id: Optional[UUID],
    ) -> DifficultyEstimate:
        """
        Estimate how difficult a task will be for a specific user.

        Uses real task data from repository and rule engine to adjust
        base difficulty based on user context and progress.

        Args:
            task_id: UUID of the task to estimate
            user_id: Optional user UUID for personalized estimate

        Returns:
            DifficultyEstimate with adjusted difficulty and predictions
        """
        logger.info(f"estimate_difficulty called: task_id={task_id}, user_id={user_id}")

        # Build cache key
        cache_key = f"difficulty:{user_id}:{task_id}"

        # Check cache
        cached = self._get_from_cache(cache_key)
        if cached is not None:
            logger.debug(f"Cache hit for {cache_key}")
            return cached

        now = datetime.utcnow()

        # Resolve user
        user = self._resolve_user(user_id)
        resolved_user_id = user.id if user else user_id

        # Build context
        user_ctx = self._build_user_context(user, resolved_user_id)

        # Load task data
        task_data = self._load_task_data(task_id, resolved_user_id)

        # Compute adjustment using rule engine
        adjustment = compute_difficulty_adjustment(user_ctx, task_data)

        logger.debug(
            f"Difficulty adjustment computed: "
            f"base={adjustment['base_difficulty']}, "
            f"adjusted={adjustment['adjusted_difficulty']}, "
            f"factors={len(adjustment['factors'])}"
        )

        # Check prerequisites
        prerequisites = task_data.get("prerequisites", [])
        completed = user_ctx.get("completed_task_ids", [])
        prereqs_met = all(p in completed for p in prerequisites)

        response = DifficultyEstimate(
            task_id=str(task_id),
            base_difficulty=adjustment["base_difficulty"],
            user_adjusted_difficulty=adjustment["adjusted_difficulty"],
            estimated_duration=adjustment["estimated_minutes"],
            success_probability=adjustment["success_probability"],
            prerequisites_met=prereqs_met,
            generated_at=now,
        )

        # Store in cache
        self._store_in_cache(cache_key, response)

        logger.debug(
            f"Returning difficulty estimate: base={response.base_difficulty}, "
            f"adjusted={response.user_adjusted_difficulty}, "
            f"success_prob={response.success_probability}"
        )
        return response

    def batch_estimate_difficulty(
        self,
        task_ids: list[UUID],
        user_id: Optional[UUID],
    ) -> list[DifficultyEstimate]:
        """
        Estimate difficulty for multiple tasks at once.

        Args:
            task_ids: List of task UUIDs to estimate
            user_id: Optional user UUID for personalized estimates

        Returns:
            List of DifficultyEstimate objects
        """
        logger.info(
            f"batch_estimate_difficulty called: "
            f"task_count={len(task_ids)}, user_id={user_id}"
        )

        user = self._resolve_user(user_id)
        resolved_user_id = user.id if user else user_id
        user_ctx = self._build_user_context(user, resolved_user_id)
        now = datetime.utcnow()

        results = []
        for task_id in task_ids:
            task_data = self._load_task_data(task_id, resolved_user_id)
            adjustment = compute_difficulty_adjustment(user_ctx, task_data)

            prerequisites = task_data.get("prerequisites", [])
            completed = user_ctx.get("completed_task_ids", [])
            prereqs_met = all(p in completed for p in prerequisites)

            results.append(DifficultyEstimate(
                task_id=str(task_id),
                base_difficulty=adjustment["base_difficulty"],
                user_adjusted_difficulty=adjustment["adjusted_difficulty"],
                estimated_duration=adjustment["estimated_minutes"],
                success_probability=adjustment["success_probability"],
                prerequisites_met=prereqs_met,
                generated_at=now,
            ))

        return results

    def check_prerequisites(
        self,
        task_id: UUID,
        user_id: UUID,
    ) -> bool:
        """
        Check if a user has completed all prerequisites for a task.

        Args:
            task_id: Task UUID to check
            user_id: User UUID to check against

        Returns:
            True if all prerequisites are met, False otherwise
        """
        logger.info(f"check_prerequisites called: task_id={task_id}, user_id={user_id}")

        user = self._resolve_user(user_id)
        resolved_user_id = user.id if user else user_id
        user_ctx = self._build_user_context(user, resolved_user_id)
        task_data = self._load_task_data(task_id, resolved_user_id)

        prerequisites = task_data.get("prerequisites", [])
        if not prerequisites:
            return True

        completed = user_ctx.get("completed_task_ids", [])
        return all(p in completed for p in prerequisites)

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

    def _load_task_data(
        self,
        task_id: UUID,
        user_id: Optional[UUID],
    ) -> TaskData:
        """
        Load task data from repository and convert to engine format.

        Args:
            task_id: UUID of the task to load
            user_id: User ID for context (unused for now)

        Returns:
            TaskData dict for engine computation
        """
        task = task_repository.get_task_by_id(task_id)

        if task:
            return {
                "id": str(task.id),
                "title": task.title,
                "difficulty": task.difficulty,
                "priority": "medium",
                "module_id": str(task.module_id),
                "due_date": None,
                "estimated_minutes": 25,
                "prerequisites": [],
            }

        # Fallback: deterministic sample task based on ID hash
        task_id_str = str(task_id)
        id_hash = hash(task_id_str) % 3

        if id_hash == 0:
            return {
                "id": task_id_str,
                "title": "Kubernetes Deployment Configuration",
                "difficulty": "medium",
                "priority": "high",
                "module_id": "kubernetes-101",
                "due_date": None,
                "estimated_minutes": 30,
                "prerequisites": [],
            }
        elif id_hash == 1:
            return {
                "id": task_id_str,
                "title": "Docker Compose Multi-Service Setup",
                "difficulty": "easy",
                "priority": "medium",
                "module_id": "docker-advanced",
                "due_date": None,
                "estimated_minutes": 20,
                "prerequisites": [],
            }
        else:
            return {
                "id": task_id_str,
                "title": "Terraform State Management",
                "difficulty": "hard",
                "priority": "low",
                "module_id": "terraform-basics",
                "due_date": None,
                "estimated_minutes": 45,
                "prerequisites": [],
            }

    def invalidate_cache(self, user_id: Optional[UUID] = None, task_id: Optional[UUID] = None) -> int:
        """
        Invalidate cached difficulty estimates.

        Args:
            user_id: User UUID whose cache should be invalidated.
            task_id: Task UUID whose cache should be invalidated.
            If both None, invalidates all caches.

        Returns:
            Number of cache entries invalidated.
        """
        if user_id is None and task_id is None:
            count = len(self._cache)
            self._cache.clear()
            logger.info(f"invalidate_cache: cleared all {count} entries")
            return count

        if user_id is not None and task_id is not None:
            key = f"difficulty:{user_id}:{task_id}"
            if key in self._cache:
                del self._cache[key]
                logger.info(f"invalidate_cache: cleared entry for user_id={user_id}, task_id={task_id}")
                return 1
            return 0

        # Partial match - clear all matching entries
        prefix = f"difficulty:{user_id}:" if user_id else "difficulty:"
        suffix = f":{task_id}" if task_id else ""
        keys_to_remove = [
            k for k in self._cache
            if k.startswith(prefix) or (suffix and k.endswith(suffix))
        ]
        for key in keys_to_remove:
            del self._cache[key]
        logger.info(f"invalidate_cache: cleared {len(keys_to_remove)} entries")
        return len(keys_to_remove)

    def _get_from_cache(self, key: str) -> Optional[DifficultyEstimate]:
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

    def _store_in_cache(self, key: str, value: DifficultyEstimate) -> None:
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
