"""
Recommendation Service
Phase 7.5: AI service layer with rule engine integration

Provides personalized task, module, and studyflow recommendations
using the deterministic rule engine (scoring + rules + heuristics).
"""
import logging
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

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

logger = logging.getLogger(__name__)


class RecommendationService:
    """
    Service for generating personalized AI recommendations.

    Phase 7.5: Uses compute_recommendation_scores from the rule engine
    to provide deterministic, explainable recommendations.
    """

    def __init__(self) -> None:
        """Initialize the recommendation service."""
        logger.info("RecommendationService initialized (engine=active)")

    def get_recommendations(
        self,
        user_id: Optional[UUID],
        limit: int = 5,
        include_reasoning: bool = False,
    ) -> RecommendationsResponse:
        """
        Generate personalized recommendations for a user.

        Uses the deterministic rule engine to score and rank all available
        modules, tasks, and studyflow configurations.

        Args:
            user_id: Optional user UUID for personalization
            limit: Maximum number of recommendations per category
            include_reasoning: Whether to include explanation text

        Returns:
            RecommendationsResponse with task, module, and studyflow suggestions
        """
        logger.info(
            f"get_recommendations called: user_id={user_id}, "
            f"limit={limit}, include_reasoning={include_reasoning}"
        )

        now = datetime.utcnow()

        # Build user context
        # Phase 7.5: Static context - real DB integration in Phase 7.6+
        user_ctx: UserContext = self._build_user_context(user_id)

        # Get available items
        # Phase 7.5: Static data - real DB queries in Phase 7.6+
        modules = self._get_available_modules()
        tasks = self._get_available_tasks()
        studyflows = self._get_studyflow_options()

        # Compute scores using rule engine
        scores = compute_recommendation_scores(user_ctx, modules, tasks, studyflows)

        logger.debug(
            f"Engine scores computed: "
            f"top_task={scores['top_task']['score'] if scores['top_task'] else 'N/A'}, "
            f"top_module={scores['top_module']['score'] if scores['top_module'] else 'N/A'}"
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

        logger.debug(f"Returning recommendations: {response.model_dump_json()[:200]}...")
        return response

    def _build_user_context(self, user_id: Optional[UUID]) -> UserContext:
        """
        Build user context for scoring.

        Phase 7.5: Returns deterministic sample context.
        Phase 7.6+: Will query actual user data from DB.
        """
        # Deterministic context based on user_id presence
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
        """
        Get available modules for recommendation.

        Phase 7.5: Returns deterministic sample modules.
        Phase 7.6+: Will query from DB.
        """
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
            {
                "id": "terraform-basics",
                "name": "Infrastructure as Code with Terraform",
                "difficulty": "hard",
                "total_tasks": 15,
                "completed_tasks": 0,
                "prerequisites": ["linux-fundamentals"],
                "category": "iac",
            },
        ]

    def _get_available_tasks(self) -> list[TaskData]:
        """
        Get available tasks for recommendation.

        Phase 7.5: Returns deterministic sample tasks.
        Phase 7.6+: Will query from DB.
        """
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
            {
                "id": "task-tf-001",
                "title": "Write your first Terraform module",
                "difficulty": "hard",
                "priority": "low",
                "module_id": "terraform-basics",
                "due_date": (now + timedelta(days=7)).isoformat(),
                "estimated_minutes": 45,
                "prerequisites": ["task-001"],
            },
        ]

    def _get_studyflow_options(self) -> list[StudyflowData]:
        """
        Get available studyflow configurations.

        Phase 7.5: Returns deterministic options.
        """
        return [
            {
                "mode": "pomodoro",
                "duration": 25,
                "intensity": "medium",
            },
            {
                "mode": "taskrunner",
                "duration": 45,
                "intensity": "high",
            },
            {
                "mode": "sprint",
                "duration": 15,
                "intensity": "low",
            },
        ]

    def invalidate_cache(self, user_id: UUID) -> None:
        """
        Invalidate cached recommendations for a user.

        Args:
            user_id: User UUID whose cache should be invalidated

        Note:
            Phase 7.5: No-op (no cache implemented yet).
            Phase 7.6+: Will clear Redis cache for user.
        """
        logger.info(f"invalidate_cache called for user_id={user_id} (no-op, cache not implemented)")
