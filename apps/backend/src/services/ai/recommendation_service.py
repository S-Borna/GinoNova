"""
Recommendation Service
Phase 7.6: AI service layer with DB integration

Provides personalized task, module, and studyflow recommendations
using real data from repositories and the deterministic rule engine.
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

from ...db import user_repository, module_repository, task_repository, progress_repository
from ...db.memory import USERS
from ...schemas.user import UserInDB
from ...schemas.progress import ProgressInDB

logger = logging.getLogger(__name__)


class RecommendationService:
    """
    Service for generating personalized AI recommendations.

    Phase 7.6: Integrates with repositories for real user/module/task data.
    Uses compute_recommendation_scores from the rule engine.
    """

    def __init__(self) -> None:
        """Initialize the recommendation service."""
        logger.info("RecommendationService initialized (engine=active, db=integrated)")

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
        logger.info(
            f"get_recommendations called: user_id={user_id}, "
            f"limit={limit}, include_reasoning={include_reasoning}"
        )

        now = datetime.utcnow()

        # Resolve user (use provided or fallback to first user)
        user = self._resolve_user(user_id)
        resolved_user_id = user.id if user else None

        # Build user context from real data
        user_ctx: UserContext = self._build_user_context(user, resolved_user_id)

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

        logger.debug(f"Returning recommendations: {response.model_dump_json()[:200]}...")
        return response

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

    def invalidate_cache(self, user_id: UUID) -> None:
        """
        Invalidate cached recommendations for a user.

        Args:
            user_id: User UUID whose cache should be invalidated

        Note:
            Phase 7.6: No-op (no cache implemented yet).
            Future: Will clear Redis cache for user.
        """
        logger.info(f"invalidate_cache called for user_id={user_id} (no-op, cache not implemented)")
