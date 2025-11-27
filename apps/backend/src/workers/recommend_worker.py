"""
Recommendation Worker
Phase 7.10: Stubbed worker for async recommendation generation

Uses deterministic rule engine calls only.
No DB writes, no async scheduling, no queues.
Includes strict error handling and metadata.
"""
from typing import Any

from .base import BaseWorker
from .worker_protocol import WorkerTask

# Import rule engine for deterministic computations
from shared.ai.engine.scoring import (
    score_task_relevance,
    score_module_priority,
    score_studyflow_mode,
    UserContext,
    TaskData,
    ModuleData,
    StudyflowData,
)
from shared.ai.engine.rules import (
    TASK_PRIORITY_RULES,
    MODULE_SELECTION_RULES,
    STUDYFLOW_MODE_RULES,
    apply_rules,
)


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
        "completed_tasks": 0,
        "prerequisites": [],
    },
]

FALLBACK_STUDYFLOWS: list[StudyflowData] = [
    {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
    {"mode": "sprint", "duration": 15, "intensity": "high"},
]


# ============================================================================
# RECOMMEND WORKER
# ============================================================================

class RecommendWorker(BaseWorker):
    """
    Worker for generating AI recommendations.

    Uses rule engine to score tasks, modules, and studyflows
    for a given user context.
    """

    required_payload_keys = ["limit", "include_reasoning"]

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.RECOMMEND

    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Generate recommendations using rule engine.

        Args:
            payload: RecommendPayload with user_id, limit, include_reasoning

        Returns:
            Dict with task_recommendations, module_recommendations, studyflow_recommendations

        Raises:
            Exception: On rule engine failure (handled by BaseWorker)
        """
        user_id = payload.get("user_id")
        limit = payload.get("limit", 5)
        include_reasoning = payload.get("include_reasoning", False)

        # Use fallback context (in production, would fetch from DB)
        user_ctx = FALLBACK_USER_CONTEXT.copy()
        if user_id:
            user_ctx["user_id"] = user_id

        all_triggered_rules: list[str] = []

        # Score tasks with error handling
        task_recommendations = []
        try:
            for task in FALLBACK_TASKS[:limit]:
                base_score = score_task_relevance(user_ctx, task)
                modifier, triggered_rules = apply_rules(TASK_PRIORITY_RULES, user_ctx, task)
                all_triggered_rules.extend(triggered_rules)
                final_score = min(100, max(0, base_score + modifier))

                rec = {
                    "task_id": task["task_id"],
                    "score": final_score,
                    "difficulty": task["difficulty"],
                    "estimated_minutes": task["estimated_minutes"],
                }
                if include_reasoning:
                    rec["reasoning"] = f"Base: {base_score}, Rules: {triggered_rules}"
                task_recommendations.append(rec)

            # Sort by score
            task_recommendations.sort(key=lambda x: x["score"], reverse=True)
        except Exception as e:
            raise RuntimeError(f"Task scoring engine failed: {e}") from e

        # Score modules with error handling
        module_recommendations = []
        try:
            for module in FALLBACK_MODULES[:limit]:
                base_score = score_module_priority(user_ctx, module)
                modifier, triggered_rules = apply_rules(MODULE_SELECTION_RULES, user_ctx, module)
                all_triggered_rules.extend(triggered_rules)
                final_score = min(100, max(0, base_score + modifier))

                rec = {
                    "module_id": module["module_id"],
                    "score": final_score,
                    "difficulty": module["difficulty"],
                    "progress": module["completed_tasks"] / module["total_tasks"] * 100,
                }
                if include_reasoning:
                    rec["reasoning"] = f"Base: {base_score}, Rules: {triggered_rules}"
                module_recommendations.append(rec)

            module_recommendations.sort(key=lambda x: x["score"], reverse=True)
        except Exception as e:
            raise RuntimeError(f"Module scoring engine failed: {e}") from e

        # Score studyflows with error handling
        studyflow_recommendations = []
        try:
            for sf in FALLBACK_STUDYFLOWS[:limit]:
                base_score = score_studyflow_mode(user_ctx, sf)
                modifier, triggered_rules = apply_rules(STUDYFLOW_MODE_RULES, user_ctx, sf)
                all_triggered_rules.extend(triggered_rules)
                final_score = min(100, max(0, base_score + modifier))

                rec = {
                    "mode": sf["mode"],
                    "score": final_score,
                    "duration": sf["duration"],
                    "intensity": sf["intensity"],
                }
                if include_reasoning:
                    rec["reasoning"] = f"Base: {base_score}, Rules: {triggered_rules}"
                studyflow_recommendations.append(rec)

            studyflow_recommendations.sort(key=lambda x: x["score"], reverse=True)
        except Exception as e:
            raise RuntimeError(f"Studyflow scoring engine failed: {e}") from e

        # Store triggered rules for metadata (accessed via extra_metadata in run())
        self._triggered_rules = list(set(all_triggered_rules))

        return {
            "task_recommendations": task_recommendations,
            "module_recommendations": module_recommendations,
            "studyflow_recommendations": studyflow_recommendations,
            "user_id": user_id,
            "_metadata": {
                "triggered_rules": self._triggered_rules,
            },
        }
