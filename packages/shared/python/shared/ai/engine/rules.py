"""
AI Rule Definitions
Phase 7.4: Static deterministic rule sets for AI decisions

All rules are pure, static, and deterministic.
Each rule is a tuple of (description, condition_function, score_modifier).
"""
from typing import Callable, TypedDict

from .scoring import UserContext, TaskData, ModuleData, StudyflowData


# ============================================================================
# RULE TYPE DEFINITIONS
# ============================================================================

class Rule(TypedDict):
    """A single rule definition."""
    name: str
    description: str
    condition: Callable[..., bool]
    score_modifier: float


# ============================================================================
# TASK PRIORITY RULES
# ============================================================================

def _task_is_next_in_sequence(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if task is the next one in module sequence."""
    order = task.get("order_in_module", 0)
    module_id = task.get("module_id", "")
    completed = user_ctx.get("completed_task_ids", [])
    # Simple heuristic: count completed tasks in same module
    completed_in_module = sum(1 for t in completed if module_id in t)
    return order == completed_in_module + 1


def _task_prerequisites_met(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if all task prerequisites are completed."""
    prerequisites = task.get("prerequisites", [])
    completed = user_ctx.get("completed_task_ids", [])
    return all(p in completed for p in prerequisites)


def _task_difficulty_matches_skill(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if task difficulty matches user skill level."""
    skill_map = {"beginner": 1, "intermediate": 2, "advanced": 3}
    diff_map = {"easy": 1, "medium": 2, "hard": 3}
    skill = skill_map.get(user_ctx.get("skill_level", "beginner"), 1)
    difficulty = diff_map.get(task.get("difficulty", "medium"), 2)
    return abs(skill - difficulty) <= 1


def _task_in_current_module(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if task is in user's current module."""
    current = user_ctx.get("current_module_id")
    task_module = task.get("module_id")
    return current is not None and current == task_module


def _task_is_short(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if task is quick to complete (under 15 minutes)."""
    return task.get("estimated_minutes", 30) <= 15


def _task_gives_good_xp(user_ctx: UserContext, task: TaskData) -> bool:
    """Check if task has above-average XP reward."""
    return task.get("xp_reward", 0) >= 50


TASK_PRIORITY_RULES: list[Rule] = [
    {
        "name": "next_in_sequence",
        "description": "Task is the next logical step in the module",
        "condition": _task_is_next_in_sequence,
        "score_modifier": 25.0,
    },
    {
        "name": "prerequisites_met",
        "description": "All prerequisites have been completed",
        "condition": _task_prerequisites_met,
        "score_modifier": 20.0,
    },
    {
        "name": "difficulty_match",
        "description": "Task difficulty matches user skill level",
        "condition": _task_difficulty_matches_skill,
        "score_modifier": 15.0,
    },
    {
        "name": "current_module",
        "description": "Task is in user's current active module",
        "condition": _task_in_current_module,
        "score_modifier": 20.0,
    },
    {
        "name": "quick_win",
        "description": "Task is quick to complete (under 15 min)",
        "condition": _task_is_short,
        "score_modifier": 10.0,
    },
    {
        "name": "high_xp",
        "description": "Task has good XP reward",
        "condition": _task_gives_good_xp,
        "score_modifier": 5.0,
    },
]


# ============================================================================
# MODULE SELECTION RULES
# ============================================================================

def _module_is_current(user_ctx: UserContext, module: ModuleData) -> bool:
    """Check if this is the user's current module."""
    return user_ctx.get("current_module_id") == module.get("module_id")


def _module_in_progress(user_ctx: UserContext, module: ModuleData) -> bool:
    """Check if module is started but not completed."""
    completed = module.get("completed_tasks", 0)
    total = module.get("total_tasks", 1)
    return 0 < completed < total


def _module_prerequisites_met(user_ctx: UserContext, module: ModuleData) -> bool:
    """Check if all module prerequisites are completed."""
    prerequisites = module.get("prerequisites", [])
    completed = user_ctx.get("completed_module_ids", [])
    return all(p in completed for p in prerequisites)


def _module_difficulty_appropriate(user_ctx: UserContext, module: ModuleData) -> bool:
    """Check if module difficulty is appropriate for user."""
    skill_map = {"beginner": 1, "intermediate": 2, "advanced": 3}
    diff_map = {"easy": 1, "medium": 2, "hard": 3}
    skill = skill_map.get(user_ctx.get("skill_level", "beginner"), 1)
    difficulty = diff_map.get(module.get("difficulty", "medium"), 2)
    return difficulty <= skill + 1


def _module_nearly_complete(user_ctx: UserContext, module: ModuleData) -> bool:
    """Check if module is nearly complete (>75%)."""
    completed = module.get("completed_tasks", 0)
    total = module.get("total_tasks", 1)
    return total > 0 and (completed / total) >= 0.75


MODULE_SELECTION_RULES: list[Rule] = [
    {
        "name": "is_current",
        "description": "Module is user's current active module",
        "condition": _module_is_current,
        "score_modifier": 30.0,
    },
    {
        "name": "in_progress",
        "description": "Module has been started but not completed",
        "condition": _module_in_progress,
        "score_modifier": 20.0,
    },
    {
        "name": "prerequisites_met",
        "description": "All prerequisite modules completed",
        "condition": _module_prerequisites_met,
        "score_modifier": 25.0,
    },
    {
        "name": "difficulty_appropriate",
        "description": "Module difficulty is appropriate for skill level",
        "condition": _module_difficulty_appropriate,
        "score_modifier": 15.0,
    },
    {
        "name": "nearly_complete",
        "description": "Module is >75% complete",
        "condition": _module_nearly_complete,
        "score_modifier": 15.0,
    },
]


# ============================================================================
# STUDYFLOW MODE RULES
# ============================================================================

def _studyflow_matches_time(user_ctx: UserContext, studyflow: StudyflowData) -> bool:
    """Check if studyflow mode suits time of day."""
    time = user_ctx.get("time_of_day", "afternoon")
    intensity = studyflow.get("intensity", "medium")

    if time in ("morning", "afternoon"):
        return True  # Most modes work during day
    else:  # evening/night
        return intensity != "high"


def _studyflow_matches_energy(user_ctx: UserContext, studyflow: StudyflowData) -> bool:
    """Check if studyflow intensity matches user energy."""
    study_today = user_ctx.get("study_minutes_today", 0)
    intensity = studyflow.get("intensity", "medium")

    if study_today < 30:
        return True  # Fresh, any intensity OK
    elif study_today < 90:
        return intensity in ("low", "medium")
    else:
        return intensity == "low"


def _studyflow_duration_appropriate(user_ctx: UserContext, studyflow: StudyflowData) -> bool:
    """Check if duration matches user preference."""
    preferred = user_ctx.get("preferred_session_duration", 25)
    duration = studyflow.get("duration", 25)
    return abs(duration - preferred) <= 10


def _studyflow_helps_streak(user_ctx: UserContext, studyflow: StudyflowData) -> bool:
    """Check if this studyflow would help maintain streak."""
    streak = user_ctx.get("streak_days", 0)
    study_today = user_ctx.get("study_minutes_today", 0)
    return streak > 0 and study_today == 0


def _studyflow_pomodoro_default(user_ctx: UserContext, studyflow: StudyflowData) -> bool:
    """Pomodoro is a safe default for most users."""
    return studyflow.get("mode") == "pomodoro"


STUDYFLOW_MODE_RULES: list[Rule] = [
    {
        "name": "matches_time",
        "description": "Studyflow mode suits time of day",
        "condition": _studyflow_matches_time,
        "score_modifier": 20.0,
    },
    {
        "name": "matches_energy",
        "description": "Intensity matches user's current energy level",
        "condition": _studyflow_matches_energy,
        "score_modifier": 25.0,
    },
    {
        "name": "duration_appropriate",
        "description": "Duration matches user preference",
        "condition": _studyflow_duration_appropriate,
        "score_modifier": 20.0,
    },
    {
        "name": "helps_streak",
        "description": "Would help maintain learning streak",
        "condition": _studyflow_helps_streak,
        "score_modifier": 15.0,
    },
    {
        "name": "pomodoro_default",
        "description": "Pomodoro is a reliable default choice",
        "condition": _studyflow_pomodoro_default,
        "score_modifier": 10.0,
    },
]


# ============================================================================
# RULE APPLICATION
# ============================================================================

def apply_rules(
    rules: list[Rule],
    user_ctx: UserContext,
    item: TaskData | ModuleData | StudyflowData,
) -> tuple[float, list[str]]:
    """
    Apply a set of rules to an item and return total score modifier.

    Args:
        rules: List of rules to apply
        user_ctx: User context
        item: The item being evaluated (task, module, or studyflow)

    Returns:
        Tuple of (total_score_modifier, list_of_triggered_rule_names)
    """
    total_modifier = 0.0
    triggered_rules: list[str] = []

    for rule in rules:
        try:
            if rule["condition"](user_ctx, item):
                total_modifier += rule["score_modifier"]
                triggered_rules.append(rule["name"])
        except (KeyError, TypeError):
            # Skip rules that fail due to missing data
            continue

    return total_modifier, triggered_rules
