"""
Difficulty Worker
Phase 7.10: Stubbed worker for async difficulty estimation

Uses deterministic rule engine calls only.
No DB writes, no async scheduling, no queues.
Includes strict error handling and metadata.
"""
from typing import Any

from .base import BaseWorker
from .worker_protocol import WorkerTask

# Import rule engine for deterministic computations
from shared.ai.engine.scoring import UserContext
from shared.ai.engine.heuristics import compute_difficulty_adjustment, ProgressData


# ============================================================================
# SAMPLE DATA (Deterministic fallback)
# ============================================================================

FALLBACK_USER_CONTEXT: UserContext = {
    "user_id": "worker-fallback",
    "skill_level": "intermediate",
    "current_module_id": "module-default",
    "completed_task_ids": [],
    "completed_module_ids": [],
    "streak_days": 0,
    "study_minutes_today": 0,
    "preferred_session_duration": 25,
    "time_of_day": "afternoon",
}

FALLBACK_PROGRESS: ProgressData = {
    "total_xp": 500,
    "level": 3,
    "tasks_completed_today": 1,
    "modules_in_progress": 1,
    "current_streak": 3,
    "weekly_study_minutes": 90,
    "recent_activity": [],
}

FALLBACK_TASKS = {
    "task-001": {"difficulty": "easy", "title": "Introduction to Docker"},
    "task-002": {"difficulty": "medium", "title": "Docker Compose Basics"},
    "task-003": {"difficulty": "hard", "title": "Container Orchestration"},
}

# Difficulty numeric values for adjustment calculation
DIFFICULTY_VALUES = {"easy": 1, "medium": 2, "hard": 3}


# ============================================================================
# DIFFICULTY WORKER
# ============================================================================

class DifficultyWorker(BaseWorker):
    """
    Worker for estimating user-adjusted difficulty.

    Combines task's base difficulty with user context
    to provide personalized difficulty estimate.
    """

    required_payload_keys = ["task_id"]

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.DIFFICULTY

    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Estimate difficulty using rule engine heuristics.

        Args:
            payload: DifficultyPayload with user_id, task_id

        Returns:
            Dict with task_id, base_difficulty, adjusted_difficulty,
            adjustment_factor, reason

        Raises:
            Exception: On rule engine failure (handled by BaseWorker)
        """
        user_id = payload.get("user_id")
        task_id = payload.get("task_id")

        # Use fallback context
        user_ctx = FALLBACK_USER_CONTEXT.copy()
        if user_id:
            user_ctx["user_id"] = user_id

        # Get task info
        task_id_str = str(task_id) if task_id else "unknown"
        task_info = FALLBACK_TASKS.get(task_id_str, {
            "difficulty": "medium",
            "title": f"Task {task_id_str}",
        })
        base_difficulty = task_info["difficulty"]
        base_value = DIFFICULTY_VALUES.get(base_difficulty, 2)

        # Compute adjustment using heuristics with error handling
        try:
            adjustment = compute_difficulty_adjustment(user_ctx, FALLBACK_PROGRESS)
        except Exception as e:
            raise RuntimeError(f"Difficulty heuristics engine failed: {e}") from e

        # Apply adjustment to base difficulty
        adjusted_value = base_value * adjustment["adjustment_factor"]

        # Map back to difficulty level
        if adjusted_value <= 1.3:
            adjusted_difficulty = "easy"
        elif adjusted_value <= 2.3:
            adjusted_difficulty = "medium"
        else:
            adjusted_difficulty = "hard"

        # Build reason
        reasons = [adjustment["reason"]]
        if user_ctx["skill_level"] == "beginner" and base_difficulty == "hard":
            reasons.append("Task may be challenging for current skill level")
        elif user_ctx["skill_level"] == "advanced" and base_difficulty == "easy":
            reasons.append("Task should be straightforward at your level")

        return {
            "task_id": task_id,
            "task_title": task_info["title"],
            "base_difficulty": base_difficulty,
            "adjusted_difficulty": adjusted_difficulty,
            "adjustment_factor": adjustment["adjustment_factor"],
            "recommended_difficulty": adjustment["recommended_difficulty"],
            "reason": " | ".join(reasons),
            "user_id": user_id,
            "_metadata": {
                "heuristics_used": ["compute_difficulty_adjustment"],
            },
        }
