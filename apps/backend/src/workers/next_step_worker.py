"""
Next Step Worker
Phase 7.9: Stubbed worker for async next step recommendation

Uses deterministic rule engine calls only.
No DB writes, no async scheduling, no queues.
"""
from typing import Any

from .base import BaseWorker
from .worker_protocol import WorkerTask, NextStepPayload

# Import rule engine for deterministic computations
from shared.ai.engine.scoring import (
    score_task_relevance,
    UserContext,
    TaskData,
)
from shared.ai.engine.rules import TASK_PRIORITY_RULES, apply_rules


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

FALLBACK_TASKS: list[TaskData] = [
    {
        "task_id": "task-001",
        "module_id": "module-default",
        "title": "Introduction to Docker",
        "difficulty": "easy",
        "estimated_minutes": 15,
        "xp_reward": 30,
        "prerequisites": [],
        "order_in_module": 1,
    },
    {
        "task_id": "task-002",
        "module_id": "module-default",
        "title": "Docker Compose Basics",
        "difficulty": "medium",
        "estimated_minutes": 25,
        "xp_reward": 50,
        "prerequisites": ["task-001"],
        "order_in_module": 2,
    },
    {
        "task_id": "task-003",
        "module_id": "module-default",
        "title": "Multi-Container Applications",
        "difficulty": "medium",
        "estimated_minutes": 30,
        "xp_reward": 60,
        "prerequisites": ["task-002"],
        "order_in_module": 3,
    },
]


# ============================================================================
# NEXT STEP WORKER
# ============================================================================

class NextStepWorker(BaseWorker):
    """
    Worker for determining the optimal next step.

    Scores all available tasks and returns the single best option
    with reasoning.
    """

    required_payload_keys: list[str] = []

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.NEXT_STEP

    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Determine optimal next step using rule engine.

        Args:
            payload: NextStepPayload with user_id

        Returns:
            Dict with next_task, score, reason
        """
        user_id = payload.get("user_id")

        # Use fallback context
        user_ctx = FALLBACK_USER_CONTEXT.copy()
        if user_id:
            user_ctx["user_id"] = user_id

        # Score all tasks
        scored_tasks = []
        for task in FALLBACK_TASKS:
            # Check prerequisites
            prereqs = task.get("prerequisites", [])
            prereqs_met = all(
                p in user_ctx.get("completed_task_ids", [])
                for p in prereqs
            )

            if not prereqs_met:
                continue

            # Already completed?
            if task["task_id"] in user_ctx.get("completed_task_ids", []):
                continue

            base_score = score_task_relevance(user_ctx, task)
            modifier, triggered_rules = apply_rules(TASK_PRIORITY_RULES, user_ctx, task)
            final_score = min(100, max(0, base_score + modifier))

            scored_tasks.append({
                "task": task,
                "score": final_score,
                "triggered_rules": triggered_rules,
            })

        # Sort by score and get best
        scored_tasks.sort(key=lambda x: x["score"], reverse=True)

        if not scored_tasks:
            return {
                "next_task": None,
                "score": 0,
                "reason": "No available tasks - all completed or prerequisites not met",
                "user_id": user_id,
            }

        best = scored_tasks[0]
        task = best["task"]

        # Build reason
        reasons = []
        if best["triggered_rules"]:
            reasons.append(f"Matched rules: {', '.join(best['triggered_rules'])}")
        reasons.append(f"Difficulty: {task['difficulty']}")
        reasons.append(f"Est. time: {task['estimated_minutes']}min")

        return {
            "next_task": {
                "task_id": task["task_id"],
                "title": task.get("title", task["task_id"]),
                "difficulty": task["difficulty"],
                "estimated_minutes": task["estimated_minutes"],
                "xp_reward": task["xp_reward"],
            },
            "score": best["score"],
            "reason": " | ".join(reasons),
            "user_id": user_id,
        }
