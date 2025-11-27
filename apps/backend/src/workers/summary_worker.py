"""
Summary Worker
Phase 7.10: Stubbed worker for async daily summary generation

Uses deterministic rule engine calls only.
No DB writes, no async scheduling, no queues.
Includes strict error handling and metadata.
"""
from datetime import datetime, timezone
from typing import Any

from .base import BaseWorker
from .worker_protocol import WorkerTask

# Import rule engine for deterministic computations
from shared.ai.engine.scoring import UserContext, TaskData, ModuleData
from shared.ai.engine.heuristics import (
    compute_daily_highlights,
    ProgressData,
)


# ============================================================================
# SAMPLE DATA (Deterministic fallback)
# ============================================================================

FALLBACK_USER_CONTEXT: UserContext = {
    "user_id": "worker-fallback",
    "skill_level": "intermediate",
    "current_module_id": "module-default",
    "completed_task_ids": ["task-001"],
    "completed_module_ids": [],
    "streak_days": 5,
    "study_minutes_today": 45,
    "preferred_session_duration": 25,
    "time_of_day": "afternoon",
}

FALLBACK_TASKS: list[TaskData] = [
    {
        "task_id": "task-001",
        "module_id": "module-default",
        "difficulty": "easy",
        "estimated_minutes": 15,
        "xp_reward": 30,
        "prerequisites": [],
        "order_in_module": 1,
    },
    {
        "task_id": "task-002",
        "module_id": "module-default",
        "difficulty": "medium",
        "estimated_minutes": 25,
        "xp_reward": 50,
        "prerequisites": ["task-001"],
        "order_in_module": 2,
    },
]

FALLBACK_MODULES: list[ModuleData] = [
    {
        "module_id": "module-default",
        "difficulty": "easy",
        "total_tasks": 10,
        "completed_tasks": 1,
        "prerequisites": [],
    },
]

FALLBACK_PROGRESS: ProgressData = {
    "total_xp": 530,
    "level": 3,
    "tasks_completed_today": 1,
    "modules_in_progress": 1,
    "current_streak": 5,
    "weekly_study_minutes": 135,
    "recent_activity": ["task-001"],
}


# ============================================================================
# GREETING TEMPLATES
# ============================================================================

GREETINGS = {
    "morning": "Good morning! Ready to learn something new?",
    "afternoon": "Good afternoon! Keep up the great work!",
    "evening": "Good evening! Perfect time for a focused session.",
    "night": "Burning the midnight oil? Let's make it count!",
}


# ============================================================================
# SUMMARY WORKER
# ============================================================================

class SummaryWorker(BaseWorker):
    """
    Worker for generating daily AI summary.

    Computes highlights, progress stats, and motivational messaging
    based on user context and activity.
    """

    required_payload_keys: list[str] = []

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.SUMMARY

    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Generate daily summary using rule engine heuristics.

        Args:
            payload: SummaryPayload with user_id

        Returns:
            Dict with greeting, highlights, progress, motivational_message

        Raises:
            Exception: On rule engine failure (handled by BaseWorker)
        """
        user_id = payload.get("user_id")

        # Use fallback context
        user_ctx = FALLBACK_USER_CONTEXT.copy()
        if user_id:
            user_ctx["user_id"] = user_id

        # Get time-appropriate greeting
        time_of_day = user_ctx.get("time_of_day", "afternoon")
        greeting = GREETINGS.get(time_of_day, GREETINGS["afternoon"])

        # Compute daily highlights using heuristics with error handling
        try:
            highlights = compute_daily_highlights(
                user_ctx,
                FALLBACK_TASKS,
                FALLBACK_MODULES,
                FALLBACK_PROGRESS,
            )
        except Exception as e:
            raise RuntimeError(f"Daily highlights heuristics engine failed: {e}") from e

        # Format highlights for response
        formatted_highlights = [
            {
                "type": h["type"],
                "title": h["title"],
                "description": h["description"],
                "priority": h["priority"],
            }
            for h in highlights
        ]

        # Build progress summary
        progress = {
            "tasks_completed_today": FALLBACK_PROGRESS["tasks_completed_today"],
            "xp_earned_today": 30,  # From task-001
            "study_minutes_today": user_ctx["study_minutes_today"],
            "current_streak": FALLBACK_PROGRESS["current_streak"],
            "level": FALLBACK_PROGRESS["level"],
            "total_xp": FALLBACK_PROGRESS["total_xp"],
        }

        # Generate motivational message
        streak = user_ctx.get("streak_days", 0)
        if streak >= 7:
            motivational = f"🔥 Amazing! {streak} day streak! You're unstoppable!"
        elif streak >= 3:
            motivational = f"💪 Great momentum! {streak} days and counting!"
        elif streak > 0:
            motivational = "🌟 Keep it up! Every day counts!"
        else:
            motivational = "🚀 Today is a great day to start learning!"

        return {
            "greeting": greeting,
            "highlights": formatted_highlights,
            "progress": progress,
            "motivational_message": motivational,
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "user_id": user_id,
            "_metadata": {
                "heuristics_used": ["compute_daily_highlights"],
                "highlight_count": len(formatted_highlights),
            },
        }
