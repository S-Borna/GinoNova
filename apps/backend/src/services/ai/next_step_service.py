"""
Next Step Service
Phase 7.5: AI service layer with rule engine integration

Provides the single most optimal next action recommendation
using the deterministic rule engine.
"""
import logging
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from shared.ai import (
    NextStepResponse,
    # Engine imports
    compute_recommendation_scores,
    UserContext,
    TaskData,
    ModuleData,
    StudyflowData,
)

logger = logging.getLogger(__name__)


class NextStepService:
    """
    Service for determining the single best next action for a user.

    Phase 7.5: Uses compute_recommendation_scores to select the
    highest-scoring action across tasks, modules, and studyflow.
    """

    def __init__(self) -> None:
        """Initialize the next step service."""
        logger.info("NextStepService initialized (engine=active)")

    def get_next_step(
        self,
        user_id: Optional[UUID],
    ) -> NextStepResponse:
        """
        Determine the single most optimal next action for a user.

        Compares top-scored task, module, and studyflow to select
        the best overall recommendation.

        Args:
            user_id: Optional user UUID for personalization

        Returns:
            NextStepResponse with the recommended action
        """
        logger.info(f"get_next_step called: user_id={user_id}")

        now = datetime.utcnow()

        # Build context and get items
        user_ctx = self._build_user_context(user_id)
        modules = self._get_available_modules()
        tasks = self._get_available_tasks()
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

        return response

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
                "score": top["score"] * 0.9,  # Slight discount for modules
                "confidence": min(1.0, top["score"] / 100.0),
                "estimated_duration": 30,
            })

        # Add studyflow if user energy is low (suggests break/refocus)
        if scores["top_studyflow"]:
            top = scores["top_studyflow"]
            sf = top["studyflow"]
            # Studyflow is recommended when energy is low or time is short
            sf_weight = 0.7
            if user_ctx.get("focus_energy") == "low":
                sf_weight = 1.1  # Prioritize if tired
            if user_ctx.get("available_minutes", 60) < 20:
                sf_weight = 1.0  # Good for short time slots

            candidates.append({
                "action_type": "studyflow",
                "action_id": None,
                "title": f"Start: {sf.get('mode', 'pomodoro').capitalize()} Session",
                "description": self._build_studyflow_description(sf),
                "score": top["score"] * sf_weight,
                "confidence": min(1.0, top["score"] / 100.0),
                "estimated_duration": sf.get("duration", 25),
            })

        # Select highest scoring
        if not candidates:
            # Fallback if no candidates
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

        Uses deterministic rules based on time and context.

        Args:
            user_id: User UUID to check

        Returns:
            NextStepResponse with break recommendation
        """
        logger.info(f"get_break_recommendation called: user_id={user_id}")

        now = datetime.utcnow()
        user_ctx = self._build_user_context(user_id)

        # Determine break duration based on energy/time
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

    def _build_user_context(self, user_id: Optional[UUID]) -> UserContext:
        """Build user context for scoring."""
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

    def _get_available_modules(self) -> list[ModuleData]:
        """Get available modules."""
        return [
            {
                "id": "kubernetes-101",
                "name": "Introduction to Kubernetes",
                "difficulty": "medium",
                "total_tasks": 12,
                "completed_tasks": 0,
                "prerequisites": ["docker-basics"],
                "category": "containers",
            },
            {
                "id": "ci-cd-pipelines",
                "name": "CI/CD Pipeline Fundamentals",
                "difficulty": "medium",
                "total_tasks": 10,
                "completed_tasks": 2,
                "prerequisites": [],
                "category": "devops",
            },
        ]

    def _get_available_tasks(self) -> list[TaskData]:
        """Get available tasks."""
        now = datetime.utcnow()
        return [
            {
                "id": "task-k8s-001",
                "title": "Deploy your first Pod",
                "difficulty": "easy",
                "priority": "high",
                "module_id": "kubernetes-101",
                "due_date": (now + timedelta(days=2)).isoformat(),
                "estimated_minutes": 20,
                "prerequisites": [],
            },
            {
                "id": "task-cicd-001",
                "title": "Configure GitHub Actions workflow",
                "difficulty": "medium",
                "priority": "medium",
                "module_id": "ci-cd-pipelines",
                "due_date": (now + timedelta(days=5)).isoformat(),
                "estimated_minutes": 35,
                "prerequisites": [],
            },
        ]

    def _get_studyflow_options(self) -> list[StudyflowData]:
        """Get studyflow options."""
        return [
            {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
            {"mode": "taskrunner", "duration": 45, "intensity": "high"},
            {"mode": "sprint", "duration": 15, "intensity": "low"},
        ]
