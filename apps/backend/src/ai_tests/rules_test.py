"""
Rule Application Tests
Phase 7.8: Validate AI rule sets and application

Tests:
- Each RULESET is applied correctly
- Selector functions return expected rule matches
- Rule conditions trigger appropriately
"""
from shared.ai.engine.scoring import UserContext, TaskData, ModuleData, StudyflowData
from shared.ai.engine.rules import (
    TASK_PRIORITY_RULES,
    MODULE_SELECTION_RULES,
    STUDYFLOW_MODE_RULES,
    apply_rules,
    # Individual condition functions for direct testing
    _task_is_next_in_sequence,
    _task_prerequisites_met,
    _task_difficulty_matches_skill,
    _task_in_current_module,
    _task_is_short,
    _task_gives_good_xp,
    _module_is_current,
    _module_in_progress,
    _module_prerequisites_met,
    _module_difficulty_appropriate,
    _module_nearly_complete,
    _studyflow_matches_time,
    _studyflow_matches_energy,
    _studyflow_duration_appropriate,
    _studyflow_helps_streak,
    _studyflow_pomodoro_default,
)


# ============================================================================
# STATIC SAMPLE DATA
# ============================================================================

SAMPLE_USER: UserContext = {
    "user_id": "user-001",
    "skill_level": "intermediate",
    "current_module_id": "module-k8s-101",
    "completed_task_ids": ["task-001", "task-002"],
    "completed_module_ids": ["module-docker-101"],
    "streak_days": 5,
    "study_minutes_today": 30,
    "preferred_session_duration": 25,
    "time_of_day": "afternoon",
}

SAMPLE_TASK_NEXT: TaskData = {
    "task_id": "task-003",
    "module_id": "module-k8s-101",
    "difficulty": "medium",
    "estimated_minutes": 10,
    "xp_reward": 60,
    "prerequisites": ["task-002"],
    "order_in_module": 3,
}

SAMPLE_TASK_OTHER: TaskData = {
    "task_id": "task-100",
    "module_id": "module-other",
    "difficulty": "hard",
    "estimated_minutes": 45,
    "xp_reward": 30,
    "prerequisites": ["task-099"],
    "order_in_module": 5,
}

SAMPLE_MODULE_CURRENT: ModuleData = {
    "module_id": "module-k8s-101",
    "difficulty": "medium",
    "total_tasks": 10,
    "completed_tasks": 8,
    "prerequisites": ["module-docker-101"],
}

SAMPLE_MODULE_NEW: ModuleData = {
    "module_id": "module-terraform",
    "difficulty": "easy",
    "total_tasks": 8,
    "completed_tasks": 0,
    "prerequisites": [],
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


# ============================================================================
# TASK RULE CONDITION TESTS
# ============================================================================

class TestTaskRuleConditions:
    """Test individual task rule conditions."""

    def test_task_is_next_in_sequence_true(self) -> None:
        """Task with correct order should be detected as next."""
        user: UserContext = {
            "user_id": "test",
            "completed_task_ids": ["module-k8s-101-task1", "module-k8s-101-task2"],
        }
        task: TaskData = {
            "task_id": "task-003",
            "module_id": "module-k8s-101",
            "order_in_module": 3,
        }
        assert _task_is_next_in_sequence(user, task) is True

    def test_task_is_next_in_sequence_false(self) -> None:
        """Task with wrong order should not be detected as next."""
        user: UserContext = {
            "user_id": "test",
            "completed_task_ids": ["module-k8s-101-task1"],
        }
        task: TaskData = {
            "task_id": "task-005",
            "module_id": "module-k8s-101",
            "order_in_module": 5,
        }
        assert _task_is_next_in_sequence(user, task) is False

    def test_task_prerequisites_met_true(self) -> None:
        """Task with all prerequisites completed should return True."""
        user: UserContext = {
            "user_id": "test",
            "completed_task_ids": ["prereq-1", "prereq-2"],
        }
        task: TaskData = {
            "task_id": "task-003",
            "prerequisites": ["prereq-1", "prereq-2"],
        }
        assert _task_prerequisites_met(user, task) is True

    def test_task_prerequisites_met_false(self) -> None:
        """Task with missing prerequisites should return False."""
        user: UserContext = {
            "user_id": "test",
            "completed_task_ids": ["prereq-1"],
        }
        task: TaskData = {
            "task_id": "task-003",
            "prerequisites": ["prereq-1", "prereq-2"],
        }
        assert _task_prerequisites_met(user, task) is False

    def test_task_prerequisites_met_empty(self) -> None:
        """Task with no prerequisites should return True."""
        user: UserContext = {"user_id": "test", "completed_task_ids": []}
        task: TaskData = {"task_id": "task-001", "prerequisites": []}
        assert _task_prerequisites_met(user, task) is True

    def test_task_difficulty_matches_skill_beginner_easy(self) -> None:
        """Beginner + easy task should match."""
        user: UserContext = {"user_id": "test", "skill_level": "beginner"}
        task: TaskData = {"task_id": "task-001", "difficulty": "easy"}
        assert _task_difficulty_matches_skill(user, task) is True

    def test_task_difficulty_matches_skill_beginner_hard(self) -> None:
        """Beginner + hard task should not match (diff > 1)."""
        user: UserContext = {"user_id": "test", "skill_level": "beginner"}
        task: TaskData = {"task_id": "task-001", "difficulty": "hard"}
        assert _task_difficulty_matches_skill(user, task) is False

    def test_task_difficulty_matches_skill_intermediate_hard(self) -> None:
        """Intermediate + hard task should match (diff = 1)."""
        user: UserContext = {"user_id": "test", "skill_level": "intermediate"}
        task: TaskData = {"task_id": "task-001", "difficulty": "hard"}
        assert _task_difficulty_matches_skill(user, task) is True

    def test_task_in_current_module_true(self) -> None:
        """Task in current module should return True."""
        user: UserContext = {"user_id": "test", "current_module_id": "module-k8s"}
        task: TaskData = {"task_id": "task-001", "module_id": "module-k8s"}
        assert _task_in_current_module(user, task) is True

    def test_task_in_current_module_false(self) -> None:
        """Task in different module should return False."""
        user: UserContext = {"user_id": "test", "current_module_id": "module-k8s"}
        task: TaskData = {"task_id": "task-001", "module_id": "module-docker"}
        assert _task_in_current_module(user, task) is False

    def test_task_is_short_true(self) -> None:
        """Task under 15 minutes should be short."""
        task: TaskData = {"task_id": "task-001", "estimated_minutes": 10}
        assert _task_is_short({}, task) is True

    def test_task_is_short_false(self) -> None:
        """Task over 15 minutes should not be short."""
        task: TaskData = {"task_id": "task-001", "estimated_minutes": 30}
        assert _task_is_short({}, task) is False

    def test_task_gives_good_xp_true(self) -> None:
        """Task with 50+ XP should be good XP."""
        task: TaskData = {"task_id": "task-001", "xp_reward": 75}
        assert _task_gives_good_xp({}, task) is True

    def test_task_gives_good_xp_false(self) -> None:
        """Task with < 50 XP should not be good XP."""
        task: TaskData = {"task_id": "task-001", "xp_reward": 25}
        assert _task_gives_good_xp({}, task) is False


# ============================================================================
# MODULE RULE CONDITION TESTS
# ============================================================================

class TestModuleRuleConditions:
    """Test individual module rule conditions."""

    def test_module_is_current_true(self) -> None:
        """Current module should return True."""
        user: UserContext = {"user_id": "test", "current_module_id": "module-k8s"}
        module: ModuleData = {"module_id": "module-k8s"}
        assert _module_is_current(user, module) is True

    def test_module_is_current_false(self) -> None:
        """Non-current module should return False."""
        user: UserContext = {"user_id": "test", "current_module_id": "module-k8s"}
        module: ModuleData = {"module_id": "module-docker"}
        assert _module_is_current(user, module) is False

    def test_module_in_progress_true(self) -> None:
        """Module with partial completion should be in progress."""
        module: ModuleData = {"module_id": "m1", "total_tasks": 10, "completed_tasks": 5}
        assert _module_in_progress({}, module) is True

    def test_module_in_progress_false_not_started(self) -> None:
        """Module with 0 completion should not be in progress."""
        module: ModuleData = {"module_id": "m1", "total_tasks": 10, "completed_tasks": 0}
        assert _module_in_progress({}, module) is False

    def test_module_in_progress_false_completed(self) -> None:
        """Module with 100% completion should not be in progress."""
        module: ModuleData = {"module_id": "m1", "total_tasks": 10, "completed_tasks": 10}
        assert _module_in_progress({}, module) is False

    def test_module_prerequisites_met_true(self) -> None:
        """Module with all prerequisites completed should return True."""
        user: UserContext = {
            "user_id": "test",
            "completed_module_ids": ["prereq-1", "prereq-2"],
        }
        module: ModuleData = {"module_id": "m1", "prerequisites": ["prereq-1", "prereq-2"]}
        assert _module_prerequisites_met(user, module) is True

    def test_module_prerequisites_met_false(self) -> None:
        """Module with missing prerequisites should return False."""
        user: UserContext = {"user_id": "test", "completed_module_ids": ["prereq-1"]}
        module: ModuleData = {"module_id": "m1", "prerequisites": ["prereq-1", "prereq-2"]}
        assert _module_prerequisites_met(user, module) is False

    def test_module_difficulty_appropriate_true(self) -> None:
        """Module with appropriate difficulty should return True."""
        user: UserContext = {"user_id": "test", "skill_level": "intermediate"}
        module: ModuleData = {"module_id": "m1", "difficulty": "medium"}
        assert _module_difficulty_appropriate(user, module) is True

    def test_module_difficulty_appropriate_false(self) -> None:
        """Module too difficult should return False."""
        user: UserContext = {"user_id": "test", "skill_level": "beginner"}
        module: ModuleData = {"module_id": "m1", "difficulty": "hard"}
        assert _module_difficulty_appropriate(user, module) is False

    def test_module_nearly_complete_true(self) -> None:
        """Module at 80% should be nearly complete."""
        module: ModuleData = {"module_id": "m1", "total_tasks": 10, "completed_tasks": 8}
        assert _module_nearly_complete({}, module) is True

    def test_module_nearly_complete_false(self) -> None:
        """Module at 50% should not be nearly complete."""
        module: ModuleData = {"module_id": "m1", "total_tasks": 10, "completed_tasks": 5}
        assert _module_nearly_complete({}, module) is False


# ============================================================================
# STUDYFLOW RULE CONDITION TESTS
# ============================================================================

class TestStudyflowRuleConditions:
    """Test individual studyflow rule conditions."""

    def test_studyflow_matches_time_day_high(self) -> None:
        """High intensity during day should match."""
        user: UserContext = {"user_id": "test", "time_of_day": "morning"}
        sf: StudyflowData = {"mode": "sprint", "intensity": "high"}
        assert _studyflow_matches_time(user, sf) is True

    def test_studyflow_matches_time_night_high(self) -> None:
        """High intensity at night should not match."""
        user: UserContext = {"user_id": "test", "time_of_day": "night"}
        sf: StudyflowData = {"mode": "sprint", "intensity": "high"}
        assert _studyflow_matches_time(user, sf) is False

    def test_studyflow_matches_time_night_low(self) -> None:
        """Low intensity at night should match."""
        user: UserContext = {"user_id": "test", "time_of_day": "night"}
        sf: StudyflowData = {"mode": "pomodoro", "intensity": "low"}
        assert _studyflow_matches_time(user, sf) is True

    def test_studyflow_matches_energy_fresh_high(self) -> None:
        """Fresh user (low study time) should match any intensity."""
        user: UserContext = {"user_id": "test", "study_minutes_today": 15}
        sf: StudyflowData = {"mode": "sprint", "intensity": "high"}
        assert _studyflow_matches_energy(user, sf) is True

    def test_studyflow_matches_energy_tired_high(self) -> None:
        """Tired user (high study time) should not match high intensity."""
        user: UserContext = {"user_id": "test", "study_minutes_today": 120}
        sf: StudyflowData = {"mode": "sprint", "intensity": "high"}
        assert _studyflow_matches_energy(user, sf) is False

    def test_studyflow_matches_energy_tired_low(self) -> None:
        """Tired user should match low intensity."""
        user: UserContext = {"user_id": "test", "study_minutes_today": 120}
        sf: StudyflowData = {"mode": "taskrunner", "intensity": "low"}
        assert _studyflow_matches_energy(user, sf) is True

    def test_studyflow_duration_appropriate_close(self) -> None:
        """Duration within 10 minutes of preference should be appropriate."""
        user: UserContext = {"user_id": "test", "preferred_session_duration": 25}
        sf: StudyflowData = {"mode": "pomodoro", "duration": 30}
        assert _studyflow_duration_appropriate(user, sf) is True

    def test_studyflow_duration_appropriate_far(self) -> None:
        """Duration far from preference should not be appropriate."""
        user: UserContext = {"user_id": "test", "preferred_session_duration": 25}
        sf: StudyflowData = {"mode": "taskrunner", "duration": 60}
        assert _studyflow_duration_appropriate(user, sf) is False

    def test_studyflow_helps_streak_true(self) -> None:
        """User with streak but no study today needs to maintain streak."""
        user: UserContext = {"user_id": "test", "streak_days": 5, "study_minutes_today": 0}
        assert _studyflow_helps_streak(user, {}) is True

    def test_studyflow_helps_streak_false_no_streak(self) -> None:
        """User without streak doesn't need to maintain."""
        user: UserContext = {"user_id": "test", "streak_days": 0, "study_minutes_today": 0}
        assert _studyflow_helps_streak(user, {}) is False

    def test_studyflow_helps_streak_false_already_studied(self) -> None:
        """User who already studied today doesn't need streak help."""
        user: UserContext = {"user_id": "test", "streak_days": 5, "study_minutes_today": 30}
        assert _studyflow_helps_streak(user, {}) is False

    def test_studyflow_pomodoro_default_true(self) -> None:
        """Pomodoro mode should return True."""
        sf: StudyflowData = {"mode": "pomodoro"}
        assert _studyflow_pomodoro_default({}, sf) is True

    def test_studyflow_pomodoro_default_false(self) -> None:
        """Non-pomodoro mode should return False."""
        sf: StudyflowData = {"mode": "sprint"}
        assert _studyflow_pomodoro_default({}, sf) is False


# ============================================================================
# APPLY_RULES TESTS
# ============================================================================

class TestApplyRules:
    """Test the apply_rules function."""

    def test_apply_task_rules_returns_modifier_and_list(self) -> None:
        """apply_rules should return score modifier and triggered rule names."""
        modifier, triggered = apply_rules(TASK_PRIORITY_RULES, SAMPLE_USER, SAMPLE_TASK_NEXT)
        assert isinstance(modifier, float)
        assert isinstance(triggered, list)
        assert all(isinstance(r, str) for r in triggered)

    def test_apply_task_rules_positive_modifier(self) -> None:
        """Matching task should get positive modifier."""
        modifier, triggered = apply_rules(TASK_PRIORITY_RULES, SAMPLE_USER, SAMPLE_TASK_NEXT)
        assert modifier > 0, "Good task should get positive modifier"
        assert len(triggered) > 0, "Should have triggered rules"

    def test_apply_task_rules_includes_expected_rules(self) -> None:
        """Task in current module should trigger 'current_module' rule."""
        modifier, triggered = apply_rules(TASK_PRIORITY_RULES, SAMPLE_USER, SAMPLE_TASK_NEXT)
        assert "current_module" in triggered, f"Expected 'current_module' in {triggered}"

    def test_apply_module_rules_current_module(self) -> None:
        """Current module should trigger 'is_current' rule."""
        modifier, triggered = apply_rules(MODULE_SELECTION_RULES, SAMPLE_USER, SAMPLE_MODULE_CURRENT)
        assert "is_current" in triggered, f"Expected 'is_current' in {triggered}"

    def test_apply_module_rules_nearly_complete(self) -> None:
        """Module at 80% should trigger 'nearly_complete' rule."""
        modifier, triggered = apply_rules(MODULE_SELECTION_RULES, SAMPLE_USER, SAMPLE_MODULE_CURRENT)
        assert "nearly_complete" in triggered, f"Expected 'nearly_complete' in {triggered}"

    def test_apply_studyflow_rules_pomodoro_default(self) -> None:
        """Pomodoro should trigger 'pomodoro_default' rule."""
        modifier, triggered = apply_rules(STUDYFLOW_MODE_RULES, SAMPLE_USER, SAMPLE_STUDYFLOW_POMODORO)
        assert "pomodoro_default" in triggered, f"Expected 'pomodoro_default' in {triggered}"

    def test_apply_rules_handles_empty_data(self) -> None:
        """apply_rules should handle empty/minimal data gracefully."""
        modifier, triggered = apply_rules(TASK_PRIORITY_RULES, {}, {})
        assert isinstance(modifier, float)
        assert isinstance(triggered, list)


# ============================================================================
# RULESET COMPLETENESS TESTS
# ============================================================================

class TestRulesetCompleteness:
    """Verify rulesets are complete and well-formed."""

    def test_task_rules_have_required_fields(self) -> None:
        """All task rules should have name, description, condition, score_modifier."""
        for rule in TASK_PRIORITY_RULES:
            assert "name" in rule, f"Rule missing 'name': {rule}"
            assert "description" in rule, f"Rule missing 'description': {rule}"
            assert "condition" in rule, f"Rule missing 'condition': {rule}"
            assert "score_modifier" in rule, f"Rule missing 'score_modifier': {rule}"
            assert callable(rule["condition"]), f"Rule condition not callable: {rule['name']}"
            assert isinstance(rule["score_modifier"], (int, float)), f"Invalid modifier: {rule['name']}"

    def test_module_rules_have_required_fields(self) -> None:
        """All module rules should have required fields."""
        for rule in MODULE_SELECTION_RULES:
            assert "name" in rule
            assert "description" in rule
            assert "condition" in rule
            assert "score_modifier" in rule
            assert callable(rule["condition"])

    def test_studyflow_rules_have_required_fields(self) -> None:
        """All studyflow rules should have required fields."""
        for rule in STUDYFLOW_MODE_RULES:
            assert "name" in rule
            assert "description" in rule
            assert "condition" in rule
            assert "score_modifier" in rule
            assert callable(rule["condition"])

    def test_task_rules_count(self) -> None:
        """Should have expected number of task rules."""
        assert len(TASK_PRIORITY_RULES) >= 5, "Expected at least 5 task rules"

    def test_module_rules_count(self) -> None:
        """Should have expected number of module rules."""
        assert len(MODULE_SELECTION_RULES) >= 4, "Expected at least 4 module rules"

    def test_studyflow_rules_count(self) -> None:
        """Should have expected number of studyflow rules."""
        assert len(STUDYFLOW_MODE_RULES) >= 4, "Expected at least 4 studyflow rules"
