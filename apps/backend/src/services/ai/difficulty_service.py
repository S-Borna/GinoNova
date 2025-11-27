"""
Difficulty Service
Phase 7.5: AI service layer with rule engine integration

Estimates user-adjusted task difficulty using the deterministic
rule engine's compute_difficulty_adjustment function.
"""
import logging
from datetime import datetime
from typing import Optional
from uuid import UUID

from shared.ai import (
    DifficultyEstimate,
    # Engine imports
    compute_difficulty_adjustment,
    UserContext,
    TaskData,
)

logger = logging.getLogger(__name__)


class DifficultyService:
    """
    Service for estimating task difficulty for specific users.

    Phase 7.5: Uses compute_difficulty_adjustment from the rule engine
    to provide personalized difficulty estimates.
    """

    def __init__(self) -> None:
        """Initialize the difficulty service."""
        logger.info("DifficultyService initialized (engine=active)")

    def estimate_difficulty(
        self,
        task_id: UUID,
        user_id: Optional[UUID],
    ) -> DifficultyEstimate:
        """
        Estimate how difficult a task will be for a specific user.

        Uses the rule engine to adjust base difficulty based on:
        - User's skill level vs task difficulty
        - Prerequisite completion status
        - Learning momentum (streak, XP)
        - Time of day factors

        Args:
            task_id: UUID of the task to estimate
            user_id: Optional user UUID for personalized estimate

        Returns:
            DifficultyEstimate with adjusted difficulty and predictions
        """
        logger.info(f"estimate_difficulty called: task_id={task_id}, user_id={user_id}")

        now = datetime.utcnow()

        # Build context
        user_ctx = self._build_user_context(user_id)
        task_data = self._get_task_data(task_id)

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

        # Build context once for all tasks
        user_ctx = self._build_user_context(user_id)
        now = datetime.utcnow()

        results = []
        for task_id in task_ids:
            task_data = self._get_task_data(task_id)
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

        user_ctx = self._build_user_context(user_id)
        task_data = self._get_task_data(task_id)

        prerequisites = task_data.get("prerequisites", [])
        if not prerequisites:
            return True

        completed = user_ctx.get("completed_task_ids", [])
        return all(p in completed for p in prerequisites)

    def _build_user_context(self, user_id: Optional[UUID]) -> UserContext:
        """
        Build user context for difficulty calculation.

        Phase 7.5: Returns deterministic sample context.
        Phase 7.6+: Will query actual user data from DB.
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

        return {
            "user_id": str(user_id) if user_id else "anonymous",
            "skill_level": "intermediate",
            "streak_days": 5,
            "xp": 1500,
            "completed_module_ids": ["docker-basics", "linux-fundamentals"],
            "completed_task_ids": ["task-001", "task-002", "task-003"],
            "focus_energy": "high" if hour < 16 else "medium",
            "time_of_day": time_of_day,
            "available_minutes": 45,
        }

    def _get_task_data(self, task_id: UUID) -> TaskData:
        """
        Get task data by ID.

        Phase 7.5: Returns deterministic sample task based on ID pattern.
        Phase 7.6+: Will query from DB.
        """
        task_id_str = str(task_id)

        # Return different task data based on ID hash (deterministic)
        # This simulates different tasks in the system
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
                "prerequisites": ["task-001"],
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
                "prerequisites": ["task-002", "task-003"],
            }
