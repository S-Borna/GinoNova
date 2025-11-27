"""
Scoring Function Tests
Phase 7.8: Validate AI scoring functions

Tests:
- Output ranges (0-100)
- Monotonic behavior (hard task > easy task for beginners)
- Mode scoring differences
- Difficulty matching
"""
import pytest

from shared.ai.engine.scoring import (
    UserContext,
    TaskData,
    ModuleData,
    StudyflowData,
    score_task_relevance,
    score_module_priority,
    score_studyflow_mode,
    SKILL_LEVEL_MAP,
    DIFFICULTY_MAP,
)


# ============================================================================
# STATIC SAMPLE DATA
# ============================================================================

SAMPLE_USER_BEGINNER: UserContext = {
    "user_id": "user-001",
    "skill_level": "beginner",
    "current_module_id": "module-k8s-101",
    "completed_task_ids": ["task-001", "task-002"],
    "completed_module_ids": [],
    "streak_days": 3,
    "total_xp": 150,
    "study_minutes_today": 30,
    "last_activity_minutes_ago": 15,
    "preferred_session_duration": 25,
    "time_of_day": "morning",
    "day_of_week": 1,
}

SAMPLE_USER_ADVANCED: UserContext = {
    "user_id": "user-002",
    "skill_level": "advanced",
    "current_module_id": "module-terraform-adv",
    "completed_task_ids": ["task-001", "task-002", "task-003", "task-004", "task-005"],
    "completed_module_ids": ["module-k8s-101", "module-docker-101"],
    "streak_days": 14,
    "total_xp": 5000,
    "study_minutes_today": 60,
    "last_activity_minutes_ago": 5,
    "preferred_session_duration": 45,
    "time_of_day": "afternoon",
    "day_of_week": 3,
}

SAMPLE_TASK_EASY: TaskData = {
    "task_id": "task-easy-001",
    "title": "Introduction to Pods",
    "module_id": "module-k8s-101",
    "difficulty": "easy",
    "xp_reward": 25,
    "estimated_minutes": 10,
    "prerequisites": [],
    "tags": ["kubernetes", "basics"],
    "order_in_module": 1,
}

SAMPLE_TASK_MEDIUM: TaskData = {
    "task_id": "task-medium-001",
    "title": "Deploy a ReplicaSet",
    "module_id": "module-k8s-101",
    "difficulty": "medium",
    "xp_reward": 50,
    "estimated_minutes": 25,
    "prerequisites": ["task-easy-001"],
    "tags": ["kubernetes", "deployments"],
    "order_in_module": 3,
}

SAMPLE_TASK_HARD: TaskData = {
    "task_id": "task-hard-001",
    "title": "Configure Helm Charts",
    "module_id": "module-k8s-101",
    "difficulty": "hard",
    "xp_reward": 100,
    "estimated_minutes": 45,
    "prerequisites": ["task-medium-001"],
    "tags": ["kubernetes", "helm", "advanced"],
    "order_in_module": 5,
}

SAMPLE_MODULE_PROGRESS: ModuleData = {
    "module_id": "module-k8s-101",
    "name": "Kubernetes 101",
    "difficulty": "medium",
    "total_tasks": 10,
    "completed_tasks": 3,
    "category": "containers",
    "prerequisites": [],
    "order_in_path": 1,
}

SAMPLE_MODULE_NEW: ModuleData = {
    "module_id": "module-terraform-basics",
    "name": "Terraform Basics",
    "difficulty": "easy",
    "total_tasks": 8,
    "completed_tasks": 0,
    "category": "infrastructure",
    "prerequisites": [],
    "order_in_path": 2,
}

SAMPLE_STUDYFLOW_POMODORO: StudyflowData = {
    "mode": "pomodoro",
    "duration": 25,
    "intensity": "medium",
}

SAMPLE_STUDYFLOW_SPRINT: StudyflowData = {
    "mode": "sprint",
    "duration": 15,
    "intensity": "high",
}

SAMPLE_STUDYFLOW_TASKRUNNER: StudyflowData = {
    "mode": "taskrunner",
    "duration": 45,
    "intensity": "low",
}


# ============================================================================
# OUTPUT RANGE TESTS
# ============================================================================

class TestScoringOutputRanges:
    """Verify all scoring functions return values in 0-100 range."""

    def test_task_relevance_range(self) -> None:
        """score_task_relevance should return 0-100."""
        score = score_task_relevance(SAMPLE_USER_BEGINNER, SAMPLE_TASK_EASY)
        assert 0 <= score <= 100, f"Score {score} out of range"

    def test_task_relevance_range_all_difficulties(self) -> None:
        """All task difficulties should produce valid scores."""
        for task in [SAMPLE_TASK_EASY, SAMPLE_TASK_MEDIUM, SAMPLE_TASK_HARD]:
            score = score_task_relevance(SAMPLE_USER_BEGINNER, task)
            assert 0 <= score <= 100, f"Score {score} out of range for {task['difficulty']}"

    def test_module_priority_range(self) -> None:
        """score_module_priority should return 0-100."""
        score = score_module_priority(SAMPLE_USER_BEGINNER, SAMPLE_MODULE_PROGRESS)
        assert 0 <= score <= 100, f"Score {score} out of range"

    def test_module_priority_range_all_states(self) -> None:
        """All module states should produce valid scores."""
        for module in [SAMPLE_MODULE_PROGRESS, SAMPLE_MODULE_NEW]:
            score = score_module_priority(SAMPLE_USER_BEGINNER, module)
            assert 0 <= score <= 100, f"Score {score} out of range for {module['name']}"

    def test_studyflow_mode_range(self) -> None:
        """score_studyflow_mode should return 0-100."""
        score = score_studyflow_mode(SAMPLE_USER_BEGINNER, SAMPLE_STUDYFLOW_POMODORO)
        assert 0 <= score <= 100, f"Score {score} out of range"

    def test_studyflow_mode_range_all_modes(self) -> None:
        """All studyflow modes should produce valid scores."""
        for sf in [SAMPLE_STUDYFLOW_POMODORO, SAMPLE_STUDYFLOW_SPRINT, SAMPLE_STUDYFLOW_TASKRUNNER]:
            score = score_studyflow_mode(SAMPLE_USER_BEGINNER, sf)
            assert 0 <= score <= 100, f"Score {score} out of range for {sf['mode']}"


# ============================================================================
# MONOTONIC BEHAVIOR TESTS
# ============================================================================

class TestScoringMonotonicBehavior:
    """Verify expected ordering in scoring results."""

    def test_current_module_task_scores_higher(self) -> None:
        """Task in current module should score higher than task in other module."""
        task_in_current = SAMPLE_TASK_EASY.copy()
        task_in_current["module_id"] = SAMPLE_USER_BEGINNER["current_module_id"]

        task_other = SAMPLE_TASK_EASY.copy()
        task_other["module_id"] = "other-module"

        score_current = score_task_relevance(SAMPLE_USER_BEGINNER, task_in_current)
        score_other = score_task_relevance(SAMPLE_USER_BEGINNER, task_other)

        assert score_current > score_other, (
            f"Current module task ({score_current}) should score higher than other ({score_other})"
        )

    def test_difficulty_match_scores_higher(self) -> None:
        """Task matching skill level should score higher than mismatch."""
        # Beginner user + easy task = good match
        # Beginner user + hard task = mismatch
        score_easy = score_task_relevance(SAMPLE_USER_BEGINNER, SAMPLE_TASK_EASY)
        score_hard = score_task_relevance(SAMPLE_USER_BEGINNER, SAMPLE_TASK_HARD)

        # Note: This depends on other factors too, but difficulty match should help
        # We test the isolated effect using a controlled scenario
        beginner_ctx: UserContext = {
            "user_id": "test",
            "skill_level": "beginner",
            "completed_task_ids": [],
            "completed_module_ids": [],
            "streak_days": 0,
            "time_of_day": "afternoon",
        }

        easy_task: TaskData = {"difficulty": "easy", "module_id": "m1", "prerequisites": []}
        hard_task: TaskData = {"difficulty": "hard", "module_id": "m1", "prerequisites": []}

        score_match = score_task_relevance(beginner_ctx, easy_task)
        score_mismatch = score_task_relevance(beginner_ctx, hard_task)

        assert score_match > score_mismatch, (
            f"Difficulty match ({score_match}) should score higher than mismatch ({score_mismatch})"
        )

    def test_current_module_has_higher_priority(self) -> None:
        """Current module should have higher priority than new module."""
        user_with_current = SAMPLE_USER_BEGINNER.copy()
        user_with_current["current_module_id"] = "module-k8s-101"

        score_current = score_module_priority(user_with_current, SAMPLE_MODULE_PROGRESS)
        score_new = score_module_priority(user_with_current, SAMPLE_MODULE_NEW)

        assert score_current > score_new, (
            f"Current module ({score_current}) should have higher priority than new ({score_new})"
        )

    def test_in_progress_module_higher_than_completed(self) -> None:
        """Module in progress should score higher than completed module."""
        in_progress: ModuleData = {
            "module_id": "m1",
            "total_tasks": 10,
            "completed_tasks": 5,
            "prerequisites": [],
        }
        completed: ModuleData = {
            "module_id": "m2",
            "total_tasks": 10,
            "completed_tasks": 10,
            "prerequisites": [],
        }

        user_ctx: UserContext = {
            "user_id": "test",
            "skill_level": "intermediate",
            "completed_module_ids": [],
        }

        score_progress = score_module_priority(user_ctx, in_progress)
        score_done = score_module_priority(user_ctx, completed)

        assert score_progress > score_done, (
            f"In-progress ({score_progress}) should score higher than completed ({score_done})"
        )


# ============================================================================
# MODE SCORING DIFFERENCES TESTS
# ============================================================================

class TestStudyflowModeDifferences:
    """Verify studyflow modes score differently based on context."""

    def test_morning_prefers_higher_intensity(self) -> None:
        """Morning sessions should favor higher intensity modes."""
        morning_user: UserContext = {
            "user_id": "test",
            "time_of_day": "morning",
            "study_minutes_today": 0,
            "preferred_session_duration": 25,
            "streak_days": 0,
        }

        high_intensity: StudyflowData = {"mode": "sprint", "duration": 25, "intensity": "high"}
        low_intensity: StudyflowData = {"mode": "taskrunner", "duration": 25, "intensity": "low"}

        score_high = score_studyflow_mode(morning_user, high_intensity)
        score_low = score_studyflow_mode(morning_user, low_intensity)

        # Morning + fresh should favor high intensity
        assert score_high >= score_low, (
            f"Morning should favor high intensity ({score_high}) over low ({score_low})"
        )

    def test_night_prefers_lower_intensity(self) -> None:
        """Night sessions should favor lower intensity modes."""
        night_user: UserContext = {
            "user_id": "test",
            "time_of_day": "night",
            "study_minutes_today": 0,
            "preferred_session_duration": 25,
            "streak_days": 0,
        }

        high_intensity: StudyflowData = {"mode": "sprint", "duration": 25, "intensity": "high"}
        low_intensity: StudyflowData = {"mode": "pomodoro", "duration": 25, "intensity": "low"}

        score_high = score_studyflow_mode(night_user, high_intensity)
        score_low = score_studyflow_mode(night_user, low_intensity)

        assert score_low > score_high, (
            f"Night should favor low intensity ({score_low}) over high ({score_high})"
        )

    def test_tired_user_prefers_low_intensity(self) -> None:
        """User with lots of study time today should prefer low intensity."""
        tired_user: UserContext = {
            "user_id": "test",
            "time_of_day": "afternoon",
            "study_minutes_today": 120,  # Lots of study time
            "preferred_session_duration": 25,
            "streak_days": 0,
        }

        high_intensity: StudyflowData = {"mode": "sprint", "duration": 25, "intensity": "high"}
        low_intensity: StudyflowData = {"mode": "taskrunner", "duration": 25, "intensity": "low"}

        score_high = score_studyflow_mode(tired_user, high_intensity)
        score_low = score_studyflow_mode(tired_user, low_intensity)

        assert score_low > score_high, (
            f"Tired user should prefer low intensity ({score_low}) over high ({score_high})"
        )

    def test_duration_preference_affects_score(self) -> None:
        """Duration closer to user preference should score higher."""
        user_prefers_25: UserContext = {
            "user_id": "test",
            "time_of_day": "afternoon",
            "study_minutes_today": 30,
            "preferred_session_duration": 25,
            "streak_days": 0,
        }

        sf_25_min: StudyflowData = {"mode": "pomodoro", "duration": 25, "intensity": "medium"}
        sf_45_min: StudyflowData = {"mode": "pomodoro", "duration": 45, "intensity": "medium"}

        score_match = score_studyflow_mode(user_prefers_25, sf_25_min)
        score_long = score_studyflow_mode(user_prefers_25, sf_45_min)

        assert score_match > score_long, (
            f"Duration match ({score_match}) should score higher than mismatch ({score_long})"
        )


# ============================================================================
# CONSTANT MAPS TESTS
# ============================================================================

class TestScoringConstants:
    """Verify scoring constants are properly defined."""

    def test_skill_level_map_complete(self) -> None:
        """SKILL_LEVEL_MAP should have all expected levels."""
        expected = {"beginner", "intermediate", "advanced"}
        assert set(SKILL_LEVEL_MAP.keys()) == expected

    def test_difficulty_map_complete(self) -> None:
        """DIFFICULTY_MAP should have all expected difficulties."""
        expected = {"easy", "medium", "hard"}
        assert set(DIFFICULTY_MAP.keys()) == expected

    def test_skill_level_ordering(self) -> None:
        """Skill levels should be ordered beginner < intermediate < advanced."""
        assert SKILL_LEVEL_MAP["beginner"] < SKILL_LEVEL_MAP["intermediate"]
        assert SKILL_LEVEL_MAP["intermediate"] < SKILL_LEVEL_MAP["advanced"]

    def test_difficulty_ordering(self) -> None:
        """Difficulties should be ordered easy < medium < hard."""
        assert DIFFICULTY_MAP["easy"] < DIFFICULTY_MAP["medium"]
        assert DIFFICULTY_MAP["medium"] < DIFFICULTY_MAP["hard"]


# ============================================================================
# EDGE CASES
# ============================================================================

class TestScoringEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_user_context(self) -> None:
        """Scoring should handle minimal user context."""
        minimal_user: UserContext = {"user_id": "minimal"}
        score = score_task_relevance(minimal_user, SAMPLE_TASK_EASY)
        assert 0 <= score <= 100

    def test_empty_task_data(self) -> None:
        """Scoring should handle minimal task data."""
        minimal_task: TaskData = {"task_id": "minimal"}
        score = score_task_relevance(SAMPLE_USER_BEGINNER, minimal_task)
        assert 0 <= score <= 100

    def test_empty_module_data(self) -> None:
        """Scoring should handle minimal module data."""
        minimal_module: ModuleData = {"module_id": "minimal"}
        score = score_module_priority(SAMPLE_USER_BEGINNER, minimal_module)
        assert 0 <= score <= 100

    def test_empty_studyflow_data(self) -> None:
        """Scoring should handle minimal studyflow data."""
        minimal_sf: StudyflowData = {}
        score = score_studyflow_mode(SAMPLE_USER_BEGINNER, minimal_sf)
        assert 0 <= score <= 100

    def test_high_streak_bonus_capped(self) -> None:
        """Streak bonus should be capped to prevent excessive scores."""
        high_streak_user: UserContext = {
            "user_id": "test",
            "skill_level": "beginner",
            "streak_days": 100,  # Very high streak
            "completed_task_ids": [],
        }
        score = score_task_relevance(high_streak_user, SAMPLE_TASK_EASY)
        assert score <= 100, "Score should not exceed 100 even with high streak"
