"""
Heuristics Function Tests
Phase 7.8: Validate AI heuristic computation

Tests:
- compute_recommendation_scores produces valid outputs
- compute_difficulty_adjustment returns appropriate adjustments
- compute_daily_highlights selects correct highlights
"""
from shared.ai.engine.scoring import UserContext, TaskData, ModuleData, StudyflowData, ProgressData
from shared.ai.engine.heuristics import (
    compute_recommendation_scores,
    compute_difficulty_adjustment,
    compute_daily_highlights,
    RecommendationScores,
    DifficultyAdjustment,
    DailyHighlight,
)


# ============================================================================
# STATIC SAMPLE DATA
# ============================================================================

SAMPLE_USER_BEGINNER: UserContext = {
    "user_id": "user-beginner",
    "skill_level": "beginner",
    "current_module_id": "module-docker-101",
    "completed_task_ids": [],
    "completed_module_ids": [],
    "streak_days": 0,
    "study_minutes_today": 0,
    "preferred_session_duration": 25,
    "time_of_day": "morning",
}

SAMPLE_USER_INTERMEDIATE: UserContext = {
    "user_id": "user-intermediate",
    "skill_level": "intermediate",
    "current_module_id": "module-k8s-101",
    "completed_task_ids": ["task-001", "task-002", "task-003"],
    "completed_module_ids": ["module-docker-101"],
    "streak_days": 7,
    "study_minutes_today": 45,
    "preferred_session_duration": 30,
    "time_of_day": "afternoon",
}

SAMPLE_USER_ADVANCED: UserContext = {
    "user_id": "user-advanced",
    "skill_level": "advanced",
    "current_module_id": "module-terraform-pro",
    "completed_task_ids": ["task-001", "task-002", "task-003", "task-004", "task-005"],
    "completed_module_ids": ["module-docker-101", "module-k8s-101", "module-k8s-201"],
    "streak_days": 30,
    "study_minutes_today": 90,
    "preferred_session_duration": 45,
    "time_of_day": "evening",
}

SAMPLE_TASKS: list[TaskData] = [
    {
        "task_id": "task-easy-1",
        "module_id": "module-docker-101",
        "difficulty": "easy",
        "estimated_minutes": 10,
        "xp_reward": 25,
        "prerequisites": [],
        "order_in_module": 1,
    },
    {
        "task_id": "task-medium-1",
        "module_id": "module-k8s-101",
        "difficulty": "medium",
        "estimated_minutes": 20,
        "xp_reward": 50,
        "prerequisites": ["task-easy-1"],
        "order_in_module": 2,
    },
    {
        "task_id": "task-hard-1",
        "module_id": "module-terraform-pro",
        "difficulty": "hard",
        "estimated_minutes": 45,
        "xp_reward": 100,
        "prerequisites": ["task-medium-1"],
        "order_in_module": 3,
    },
]

SAMPLE_MODULES: list[ModuleData] = [
    {
        "module_id": "module-docker-101",
        "difficulty": "easy",
        "total_tasks": 10,
        "completed_tasks": 0,
        "prerequisites": [],
    },
    {
        "module_id": "module-k8s-101",
        "difficulty": "medium",
        "total_tasks": 15,
        "completed_tasks": 8,
        "prerequisites": ["module-docker-101"],
    },
    {
        "module_id": "module-terraform-pro",
        "difficulty": "hard",
        "total_tasks": 20,
        "completed_tasks": 18,
        "prerequisites": ["module-k8s-101"],
    },
]

SAMPLE_STUDYFLOWS: list[StudyflowData] = [
    {"mode": "pomodoro", "duration": 25, "intensity": "medium"},
    {"mode": "sprint", "duration": 15, "intensity": "high"},
    {"mode": "deep_focus", "duration": 60, "intensity": "high"},
    {"mode": "taskrunner", "duration": 10, "intensity": "low"},
]

SAMPLE_PROGRESS: ProgressData = {
    "total_xp": 1500,
    "level": 5,
    "tasks_completed_today": 3,
    "modules_in_progress": 2,
    "current_streak": 7,
    "weekly_study_minutes": 180,
    "recent_activity": ["task-001", "task-002", "task-003"],
}


# ============================================================================
# RECOMMENDATION SCORES TESTS
# ============================================================================

class TestComputeRecommendationScores:
    """Test compute_recommendation_scores function."""

    def test_returns_recommendation_scores_type(self) -> None:
        """Should return RecommendationScores TypedDict."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        assert "task_scores" in result
        assert "module_scores" in result
        assert "studyflow_scores" in result

    def test_task_scores_list_length(self) -> None:
        """task_scores should have same length as input tasks."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        assert len(result["task_scores"]) == len(SAMPLE_TASKS)

    def test_module_scores_list_length(self) -> None:
        """module_scores should have same length as input modules."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        assert len(result["module_scores"]) == len(SAMPLE_MODULES)

    def test_studyflow_scores_list_length(self) -> None:
        """studyflow_scores should have same length as input studyflows."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        assert len(result["studyflow_scores"]) == len(SAMPLE_STUDYFLOWS)

    def test_task_scores_in_valid_range(self) -> None:
        """All task scores should be in 0-100 range."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        for scored_task in result["task_scores"]:
            assert 0 <= scored_task["score"] <= 100, f"Score out of range: {scored_task}"

    def test_module_scores_in_valid_range(self) -> None:
        """All module scores should be in 0-100 range."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        for scored_module in result["module_scores"]:
            assert 0 <= scored_module["score"] <= 100, f"Score out of range: {scored_module}"

    def test_studyflow_scores_in_valid_range(self) -> None:
        """All studyflow scores should be in 0-100 range."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        for scored_sf in result["studyflow_scores"]:
            assert 0 <= scored_sf["score"] <= 100, f"Score out of range: {scored_sf}"

    def test_scores_sorted_by_score_descending(self) -> None:
        """Scores should be sorted by score in descending order."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        task_scores = [t["score"] for t in result["task_scores"]]
        assert task_scores == sorted(task_scores, reverse=True), "Tasks not sorted by score"

    def test_beginner_prefers_easy_tasks(self) -> None:
        """Beginner user should score easy tasks higher."""
        result = compute_recommendation_scores(
            SAMPLE_USER_BEGINNER, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        easy_task_score = next(
            t["score"] for t in result["task_scores"] if t["task_id"] == "task-easy-1"
        )
        hard_task_score = next(
            t["score"] for t in result["task_scores"] if t["task_id"] == "task-hard-1"
        )
        assert easy_task_score > hard_task_score, "Beginner should prefer easy tasks"

    def test_advanced_can_handle_hard_tasks(self) -> None:
        """Advanced user should score hard tasks reasonably high."""
        result = compute_recommendation_scores(
            SAMPLE_USER_ADVANCED, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        hard_task_score = next(
            t["score"] for t in result["task_scores"] if t["task_id"] == "task-hard-1"
        )
        assert hard_task_score >= 50, "Advanced user should handle hard tasks"

    def test_handles_empty_lists(self) -> None:
        """Should handle empty task/module/studyflow lists."""
        result = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, [], [], []
        )
        assert result["task_scores"] == []
        assert result["module_scores"] == []
        assert result["studyflow_scores"] == []


# ============================================================================
# DIFFICULTY ADJUSTMENT TESTS
# ============================================================================

class TestComputeDifficultyAdjustment:
    """Test compute_difficulty_adjustment function."""

    def test_returns_difficulty_adjustment_type(self) -> None:
        """Should return DifficultyAdjustment TypedDict."""
        result = compute_difficulty_adjustment(SAMPLE_USER_INTERMEDIATE, SAMPLE_PROGRESS)
        assert "adjustment_factor" in result
        assert "reason" in result
        assert "recommended_difficulty" in result

    def test_adjustment_factor_in_range(self) -> None:
        """Adjustment factor should be in reasonable range (e.g., 0.5 to 1.5)."""
        result = compute_difficulty_adjustment(SAMPLE_USER_INTERMEDIATE, SAMPLE_PROGRESS)
        assert 0.5 <= result["adjustment_factor"] <= 1.5, f"Adjustment out of range: {result}"

    def test_beginner_gets_lower_difficulty(self) -> None:
        """Beginner should get lower recommended difficulty."""
        result = compute_difficulty_adjustment(SAMPLE_USER_BEGINNER, SAMPLE_PROGRESS)
        assert result["recommended_difficulty"] in ["easy", "medium"]

    def test_advanced_can_handle_harder(self) -> None:
        """Advanced user should get higher recommended difficulty."""
        result = compute_difficulty_adjustment(SAMPLE_USER_ADVANCED, SAMPLE_PROGRESS)
        assert result["recommended_difficulty"] in ["medium", "hard"]

    def test_tired_user_gets_lower_adjustment(self) -> None:
        """User with high study minutes should get lower adjustment."""
        tired_user: UserContext = {**SAMPLE_USER_INTERMEDIATE, "study_minutes_today": 180}
        result = compute_difficulty_adjustment(tired_user, SAMPLE_PROGRESS)
        assert result["adjustment_factor"] <= 1.0, "Tired user should get easier content"

    def test_fresh_user_gets_normal_or_higher(self) -> None:
        """User with low study minutes should get normal or higher adjustment."""
        fresh_user: UserContext = {**SAMPLE_USER_INTERMEDIATE, "study_minutes_today": 0}
        result = compute_difficulty_adjustment(fresh_user, SAMPLE_PROGRESS)
        assert result["adjustment_factor"] >= 0.9, "Fresh user should handle normal difficulty"

    def test_reason_is_non_empty_string(self) -> None:
        """Reason should be a non-empty string."""
        result = compute_difficulty_adjustment(SAMPLE_USER_INTERMEDIATE, SAMPLE_PROGRESS)
        assert isinstance(result["reason"], str)
        assert len(result["reason"]) > 0

    def test_handles_minimal_progress(self) -> None:
        """Should handle progress with minimal data."""
        minimal_progress: ProgressData = {
            "total_xp": 0,
            "level": 1,
            "tasks_completed_today": 0,
            "modules_in_progress": 0,
            "current_streak": 0,
            "weekly_study_minutes": 0,
            "recent_activity": [],
        }
        result = compute_difficulty_adjustment(SAMPLE_USER_BEGINNER, minimal_progress)
        assert "adjustment_factor" in result


# ============================================================================
# DAILY HIGHLIGHTS TESTS
# ============================================================================

class TestComputeDailyHighlights:
    """Test compute_daily_highlights function."""

    def test_returns_list_of_highlights(self) -> None:
        """Should return list of DailyHighlight TypedDicts."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        assert isinstance(result, list)

    def test_highlights_have_required_fields(self) -> None:
        """Each highlight should have type, title, description, priority."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        for highlight in result:
            assert "type" in highlight, f"Highlight missing 'type': {highlight}"
            assert "title" in highlight, f"Highlight missing 'title': {highlight}"
            assert "description" in highlight, f"Highlight missing 'description': {highlight}"
            assert "priority" in highlight, f"Highlight missing 'priority': {highlight}"

    def test_highlights_limited_count(self) -> None:
        """Should return limited number of highlights (e.g., max 5)."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        assert len(result) <= 5, "Too many highlights returned"

    def test_highlights_priority_in_range(self) -> None:
        """Highlight priority should be in valid range (1-5 or similar)."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        for highlight in result:
            assert 1 <= highlight["priority"] <= 5, f"Priority out of range: {highlight}"

    def test_streak_highlight_when_streak_at_risk(self) -> None:
        """Should include streak highlight when user has streak but hasn't studied."""
        at_risk_user: UserContext = {
            **SAMPLE_USER_INTERMEDIATE,
            "streak_days": 10,
            "study_minutes_today": 0,
        }
        result = compute_daily_highlights(
            at_risk_user, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        streak_highlight = next(
            (h for h in result if h["type"] == "streak"), None
        )
        assert streak_highlight is not None, "Should have streak highlight"

    def test_nearly_complete_module_highlight(self) -> None:
        """Should include highlight for module at 90%+ completion."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        # module-terraform-pro is at 90% (18/20)
        module_highlight = next(
            (h for h in result if h["type"] == "module_completion"), None
        )
        assert module_highlight is not None, "Should have module completion highlight"

    def test_handles_empty_data(self) -> None:
        """Should handle empty task and module lists."""
        result = compute_daily_highlights(
            SAMPLE_USER_BEGINNER, [], [], SAMPLE_PROGRESS
        )
        assert isinstance(result, list)

    def test_highlights_sorted_by_priority(self) -> None:
        """Highlights should be sorted by priority (highest first)."""
        result = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        if len(result) > 1:
            priorities = [h["priority"] for h in result]
            assert priorities == sorted(priorities, reverse=True), "Not sorted by priority"


# ============================================================================
# DETERMINISM TESTS
# ============================================================================

class TestHeuristicDeterminism:
    """Verify heuristics produce deterministic results."""

    def test_recommendation_scores_deterministic(self) -> None:
        """Same inputs should produce identical recommendation scores."""
        result1 = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        result2 = compute_recommendation_scores(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_STUDYFLOWS
        )
        assert result1 == result2, "Recommendation scores not deterministic"

    def test_difficulty_adjustment_deterministic(self) -> None:
        """Same inputs should produce identical difficulty adjustment."""
        result1 = compute_difficulty_adjustment(SAMPLE_USER_INTERMEDIATE, SAMPLE_PROGRESS)
        result2 = compute_difficulty_adjustment(SAMPLE_USER_INTERMEDIATE, SAMPLE_PROGRESS)
        assert result1 == result2, "Difficulty adjustment not deterministic"

    def test_daily_highlights_deterministic(self) -> None:
        """Same inputs should produce identical daily highlights."""
        result1 = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        result2 = compute_daily_highlights(
            SAMPLE_USER_INTERMEDIATE, SAMPLE_TASKS, SAMPLE_MODULES, SAMPLE_PROGRESS
        )
        assert result1 == result2, "Daily highlights not deterministic"
