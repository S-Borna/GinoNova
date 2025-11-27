"""
Service Integration Tests
Phase 7.8: Validate AI services produce valid schema outputs

Tests:
- Services return valid Pydantic schema outputs
- Correct top picks are selected
- Services handle edge cases gracefully
"""
from unittest.mock import MagicMock, AsyncMock, patch
import pytest

from services.ai.recommendation_service import RecommendationService
from services.ai.next_step_service import NextStepService
from services.ai.difficulty_service import DifficultyService
from services.ai.summary_service import SummaryService

from schemas.ai import (
    RecommendationResponse,
    NextStepResponse,
    DifficultyResponse,
    SummaryResponse,
)


# ============================================================================
# STATIC MOCK DATA
# ============================================================================

MOCK_USER_ID = "user-test-001"

MOCK_TASKS = [
    {
        "id": "task-001",
        "module_id": "module-docker-101",
        "title": "Docker Basics",
        "difficulty": "easy",
        "estimated_minutes": 15,
        "xp_reward": 30,
        "prerequisites": [],
        "order_in_module": 1,
        "status": "pending",
    },
    {
        "id": "task-002",
        "module_id": "module-docker-101",
        "title": "Docker Compose",
        "difficulty": "medium",
        "estimated_minutes": 25,
        "xp_reward": 50,
        "prerequisites": ["task-001"],
        "order_in_module": 2,
        "status": "pending",
    },
    {
        "id": "task-003",
        "module_id": "module-k8s-101",
        "title": "Kubernetes Intro",
        "difficulty": "medium",
        "estimated_minutes": 30,
        "xp_reward": 60,
        "prerequisites": ["task-002"],
        "order_in_module": 1,
        "status": "pending",
    },
]

MOCK_MODULES = [
    {
        "id": "module-docker-101",
        "title": "Docker Fundamentals",
        "difficulty": "easy",
        "total_tasks": 10,
        "completed_tasks": 2,
        "prerequisites": [],
    },
    {
        "id": "module-k8s-101",
        "title": "Kubernetes Basics",
        "difficulty": "medium",
        "total_tasks": 15,
        "completed_tasks": 0,
        "prerequisites": ["module-docker-101"],
    },
]

MOCK_STUDYFLOWS = [
    {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
    {"mode": "sprint", "duration": 15, "intensity": "high"},
    {"mode": "deep_focus", "duration": 60, "intensity": "high"},
]

MOCK_PROGRESS = {
    "total_xp": 500,
    "level": 3,
    "tasks_completed_today": 1,
    "modules_in_progress": 1,
    "current_streak": 5,
    "weekly_study_minutes": 120,
    "recent_activity": ["task-001"],
}

MOCK_USER_CONTEXT = {
    "user_id": MOCK_USER_ID,
    "skill_level": "intermediate",
    "current_module_id": "module-docker-101",
    "completed_task_ids": ["task-001"],
    "completed_module_ids": [],
    "streak_days": 5,
    "study_minutes_today": 30,
    "preferred_session_duration": 25,
    "time_of_day": "afternoon",
}


# ============================================================================
# MOCK REPOSITORY FACTORY
# ============================================================================

def create_mock_task_repository() -> MagicMock:
    """Create mock task repository with deterministic data."""
    mock = MagicMock()
    mock.get_pending_tasks = AsyncMock(return_value=MOCK_TASKS)
    mock.get_task_by_id = AsyncMock(side_effect=lambda id: next(
        (t for t in MOCK_TASKS if t["id"] == id), None
    ))
    return mock


def create_mock_module_repository() -> MagicMock:
    """Create mock module repository with deterministic data."""
    mock = MagicMock()
    mock.get_available_modules = AsyncMock(return_value=MOCK_MODULES)
    mock.get_module_by_id = AsyncMock(side_effect=lambda id: next(
        (m for m in MOCK_MODULES if m["id"] == id), None
    ))
    return mock


def create_mock_studyflow_repository() -> MagicMock:
    """Create mock studyflow repository with deterministic data."""
    mock = MagicMock()
    mock.get_studyflows = AsyncMock(return_value=MOCK_STUDYFLOWS)
    return mock


def create_mock_progress_repository() -> MagicMock:
    """Create mock progress repository with deterministic data."""
    mock = MagicMock()
    mock.get_user_progress = AsyncMock(return_value=MOCK_PROGRESS)
    return mock


def create_mock_user_repository() -> MagicMock:
    """Create mock user repository with deterministic context."""
    mock = MagicMock()
    mock.get_user_context = AsyncMock(return_value=MOCK_USER_CONTEXT)
    return mock


# ============================================================================
# RECOMMENDATION SERVICE TESTS
# ============================================================================

class TestRecommendationService:
    """Test RecommendationService integration."""

    @pytest.fixture
    def service(self) -> RecommendationService:
        """Create service with mock repositories."""
        return RecommendationService(
            task_repo=create_mock_task_repository(),
            module_repo=create_mock_module_repository(),
            studyflow_repo=create_mock_studyflow_repository(),
            user_repo=create_mock_user_repository(),
        )

    @pytest.mark.asyncio
    async def test_get_recommendations_returns_valid_response(self, service: RecommendationService) -> None:
        """Should return valid RecommendationResponse."""
        response = await service.get_recommendations(MOCK_USER_ID)
        assert isinstance(response, RecommendationResponse)

    @pytest.mark.asyncio
    async def test_response_has_tasks(self, service: RecommendationService) -> None:
        """Response should include recommended tasks."""
        response = await service.get_recommendations(MOCK_USER_ID)
        assert hasattr(response, "tasks")
        assert isinstance(response.tasks, list)

    @pytest.mark.asyncio
    async def test_response_has_modules(self, service: RecommendationService) -> None:
        """Response should include recommended modules."""
        response = await service.get_recommendations(MOCK_USER_ID)
        assert hasattr(response, "modules")
        assert isinstance(response.modules, list)

    @pytest.mark.asyncio
    async def test_response_has_studyflows(self, service: RecommendationService) -> None:
        """Response should include recommended studyflows."""
        response = await service.get_recommendations(MOCK_USER_ID)
        assert hasattr(response, "studyflows")
        assert isinstance(response.studyflows, list)

    @pytest.mark.asyncio
    async def test_top_picks_limited(self, service: RecommendationService) -> None:
        """Top picks should be limited to reasonable count."""
        response = await service.get_recommendations(MOCK_USER_ID)
        assert len(response.tasks) <= 5, "Too many task recommendations"
        assert len(response.modules) <= 3, "Too many module recommendations"
        assert len(response.studyflows) <= 3, "Too many studyflow recommendations"

    @pytest.mark.asyncio
    async def test_tasks_have_scores(self, service: RecommendationService) -> None:
        """Recommended tasks should include scores."""
        response = await service.get_recommendations(MOCK_USER_ID)
        for task in response.tasks:
            assert hasattr(task, "score")
            assert 0 <= task.score <= 100

    @pytest.mark.asyncio
    async def test_deterministic_results(self, service: RecommendationService) -> None:
        """Same user should get same recommendations."""
        response1 = await service.get_recommendations(MOCK_USER_ID)
        response2 = await service.get_recommendations(MOCK_USER_ID)
        assert response1.tasks == response2.tasks


# ============================================================================
# NEXT STEP SERVICE TESTS
# ============================================================================

class TestNextStepService:
    """Test NextStepService integration."""

    @pytest.fixture
    def service(self) -> NextStepService:
        """Create service with mock repositories."""
        return NextStepService(
            task_repo=create_mock_task_repository(),
            module_repo=create_mock_module_repository(),
            user_repo=create_mock_user_repository(),
        )

    @pytest.mark.asyncio
    async def test_get_next_step_returns_valid_response(self, service: NextStepService) -> None:
        """Should return valid NextStepResponse."""
        response = await service.get_next_step(MOCK_USER_ID)
        assert isinstance(response, NextStepResponse)

    @pytest.mark.asyncio
    async def test_response_has_task(self, service: NextStepService) -> None:
        """Response should include recommended next task."""
        response = await service.get_next_step(MOCK_USER_ID)
        assert hasattr(response, "task")

    @pytest.mark.asyncio
    async def test_response_has_reason(self, service: NextStepService) -> None:
        """Response should include reason for recommendation."""
        response = await service.get_next_step(MOCK_USER_ID)
        assert hasattr(response, "reason")
        assert isinstance(response.reason, str)
        assert len(response.reason) > 0

    @pytest.mark.asyncio
    async def test_next_task_has_prerequisites_met(self, service: NextStepService) -> None:
        """Recommended task should have prerequisites met."""
        response = await service.get_next_step(MOCK_USER_ID)
        if response.task:
            task = response.task
            # task-001 is complete, so task-002 is valid
            if task.prerequisites:
                for prereq in task.prerequisites:
                    assert prereq in MOCK_USER_CONTEXT["completed_task_ids"], \
                        f"Prerequisite {prereq} not met"

    @pytest.mark.asyncio
    async def test_deterministic_next_step(self, service: NextStepService) -> None:
        """Same user should get same next step."""
        response1 = await service.get_next_step(MOCK_USER_ID)
        response2 = await service.get_next_step(MOCK_USER_ID)
        assert response1.task == response2.task


# ============================================================================
# DIFFICULTY SERVICE TESTS
# ============================================================================

class TestDifficultyService:
    """Test DifficultyService integration."""

    @pytest.fixture
    def service(self) -> DifficultyService:
        """Create service with mock repositories."""
        return DifficultyService(
            progress_repo=create_mock_progress_repository(),
            user_repo=create_mock_user_repository(),
        )

    @pytest.mark.asyncio
    async def test_get_difficulty_returns_valid_response(self, service: DifficultyService) -> None:
        """Should return valid DifficultyResponse."""
        response = await service.get_difficulty_assessment(MOCK_USER_ID)
        assert isinstance(response, DifficultyResponse)

    @pytest.mark.asyncio
    async def test_response_has_adjustment_factor(self, service: DifficultyService) -> None:
        """Response should include adjustment factor."""
        response = await service.get_difficulty_assessment(MOCK_USER_ID)
        assert hasattr(response, "adjustment_factor")
        assert 0.5 <= response.adjustment_factor <= 1.5

    @pytest.mark.asyncio
    async def test_response_has_recommended_difficulty(self, service: DifficultyService) -> None:
        """Response should include recommended difficulty."""
        response = await service.get_difficulty_assessment(MOCK_USER_ID)
        assert hasattr(response, "recommended_difficulty")
        assert response.recommended_difficulty in ["easy", "medium", "hard"]

    @pytest.mark.asyncio
    async def test_response_has_reason(self, service: DifficultyService) -> None:
        """Response should include reason."""
        response = await service.get_difficulty_assessment(MOCK_USER_ID)
        assert hasattr(response, "reason")
        assert isinstance(response.reason, str)

    @pytest.mark.asyncio
    async def test_deterministic_difficulty(self, service: DifficultyService) -> None:
        """Same user should get same difficulty assessment."""
        response1 = await service.get_difficulty_assessment(MOCK_USER_ID)
        response2 = await service.get_difficulty_assessment(MOCK_USER_ID)
        assert response1.adjustment_factor == response2.adjustment_factor


# ============================================================================
# SUMMARY SERVICE TESTS
# ============================================================================

class TestSummaryService:
    """Test SummaryService integration."""

    @pytest.fixture
    def service(self) -> SummaryService:
        """Create service with mock repositories."""
        return SummaryService(
            task_repo=create_mock_task_repository(),
            module_repo=create_mock_module_repository(),
            progress_repo=create_mock_progress_repository(),
            user_repo=create_mock_user_repository(),
        )

    @pytest.mark.asyncio
    async def test_get_summary_returns_valid_response(self, service: SummaryService) -> None:
        """Should return valid SummaryResponse."""
        response = await service.get_daily_summary(MOCK_USER_ID)
        assert isinstance(response, SummaryResponse)

    @pytest.mark.asyncio
    async def test_response_has_highlights(self, service: SummaryService) -> None:
        """Response should include daily highlights."""
        response = await service.get_daily_summary(MOCK_USER_ID)
        assert hasattr(response, "highlights")
        assert isinstance(response.highlights, list)

    @pytest.mark.asyncio
    async def test_response_has_progress_summary(self, service: SummaryService) -> None:
        """Response should include progress summary."""
        response = await service.get_daily_summary(MOCK_USER_ID)
        assert hasattr(response, "progress")

    @pytest.mark.asyncio
    async def test_highlights_have_required_fields(self, service: SummaryService) -> None:
        """Each highlight should have type, title, description, priority."""
        response = await service.get_daily_summary(MOCK_USER_ID)
        for highlight in response.highlights:
            assert hasattr(highlight, "type")
            assert hasattr(highlight, "title")
            assert hasattr(highlight, "description")
            assert hasattr(highlight, "priority")

    @pytest.mark.asyncio
    async def test_highlights_limited_count(self, service: SummaryService) -> None:
        """Highlights should be limited to reasonable count."""
        response = await service.get_daily_summary(MOCK_USER_ID)
        assert len(response.highlights) <= 5

    @pytest.mark.asyncio
    async def test_deterministic_summary(self, service: SummaryService) -> None:
        """Same user should get same summary."""
        response1 = await service.get_daily_summary(MOCK_USER_ID)
        response2 = await service.get_daily_summary(MOCK_USER_ID)
        assert response1.highlights == response2.highlights


# ============================================================================
# EDGE CASE TESTS
# ============================================================================

class TestServiceEdgeCases:
    """Test services handle edge cases gracefully."""

    @pytest.mark.asyncio
    async def test_recommendation_with_empty_tasks(self) -> None:
        """RecommendationService should handle empty task list."""
        service = RecommendationService(
            task_repo=MagicMock(get_pending_tasks=AsyncMock(return_value=[])),
            module_repo=create_mock_module_repository(),
            studyflow_repo=create_mock_studyflow_repository(),
            user_repo=create_mock_user_repository(),
        )
        response = await service.get_recommendations(MOCK_USER_ID)
        assert response.tasks == []

    @pytest.mark.asyncio
    async def test_next_step_with_all_completed(self) -> None:
        """NextStepService should handle all tasks completed."""
        service = NextStepService(
            task_repo=MagicMock(get_pending_tasks=AsyncMock(return_value=[])),
            module_repo=create_mock_module_repository(),
            user_repo=create_mock_user_repository(),
        )
        response = await service.get_next_step(MOCK_USER_ID)
        # Should return None or a "no more tasks" indication
        assert response.task is None or response.reason != ""

    @pytest.mark.asyncio
    async def test_difficulty_with_new_user(self) -> None:
        """DifficultyService should handle brand new user."""
        new_user_repo = MagicMock(get_user_context=AsyncMock(return_value={
            "user_id": "new-user",
            "skill_level": "beginner",
            "current_module_id": None,
            "completed_task_ids": [],
            "completed_module_ids": [],
            "streak_days": 0,
            "study_minutes_today": 0,
            "preferred_session_duration": 25,
            "time_of_day": "morning",
        }))
        new_progress_repo = MagicMock(get_user_progress=AsyncMock(return_value={
            "total_xp": 0,
            "level": 1,
            "tasks_completed_today": 0,
            "modules_in_progress": 0,
            "current_streak": 0,
            "weekly_study_minutes": 0,
            "recent_activity": [],
        }))
        service = DifficultyService(
            progress_repo=new_progress_repo,
            user_repo=new_user_repo,
        )
        response = await service.get_difficulty_assessment("new-user")
        assert response.recommended_difficulty == "easy"
