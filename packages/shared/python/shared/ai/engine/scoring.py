"""
AI Scoring Functions
Phase 7.4: Pure deterministic scoring for AI recommendations

All functions return scores in the 0-100 range.
No ML. No randomness. Rule-based only.
"""
from typing import TypedDict


# ============================================================================
# TYPE DEFINITIONS
# ============================================================================

class UserContext(TypedDict, total=False):
    """User context for scoring decisions."""
    user_id: str
    skill_level: str  # "beginner", "intermediate", "advanced"
    current_module_id: str | None
    completed_task_ids: list[str]
    completed_module_ids: list[str]
    streak_days: int
    total_xp: int
    study_minutes_today: int
    last_activity_minutes_ago: int | None
    preferred_session_duration: int  # minutes
    time_of_day: str  # "morning", "afternoon", "evening", "night"
    day_of_week: int  # 0=Monday, 6=Sunday


class TaskData(TypedDict, total=False):
    """Task data for scoring."""
    task_id: str
    title: str
    module_id: str
    difficulty: str  # "easy", "medium", "hard"
    xp_reward: int
    estimated_minutes: int
    prerequisites: list[str]
    tags: list[str]
    order_in_module: int


class ModuleData(TypedDict, total=False):
    """Module data for scoring."""
    module_id: str
    name: str
    difficulty: str
    total_tasks: int
    completed_tasks: int
    category: str
    prerequisites: list[str]
    order_in_path: int


class StudyflowData(TypedDict, total=False):
    """Studyflow session data for scoring."""
    mode: str  # "pomodoro", "taskrunner", "sprint"
    duration: int  # minutes
    intensity: str  # "low", "medium", "high"


# ============================================================================
# SCORING CONSTANTS
# ============================================================================

SKILL_LEVEL_MAP = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
}

DIFFICULTY_MAP = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

TIME_OF_DAY_FOCUS = {
    "morning": 0.9,
    "afternoon": 1.0,
    "evening": 0.8,
    "night": 0.6,
}


# ============================================================================
# TASK SCORING
# ============================================================================

def score_task_relevance(user_ctx: UserContext, task: TaskData) -> float:
    """
    Score how relevant a task is for a user.

    Factors:
    - Is the task in the user's current module? (+30)
    - Is the task's difficulty appropriate for skill level? (+25)
    - Are prerequisites met? (+20 if yes, 0 if no)
    - Is the task the next logical step? (+15)
    - Bonus for maintaining streak (+10)

    Args:
        user_ctx: User context dictionary
        task: Task data dictionary

    Returns:
        Score from 0-100
    """
    score = 0.0

    # Current module bonus
    current_module = user_ctx.get("current_module_id")
    task_module = task.get("module_id")
    if current_module and task_module == current_module:
        score += 30.0

    # Difficulty match scoring
    user_skill = SKILL_LEVEL_MAP.get(user_ctx.get("skill_level", "beginner"), 1)
    task_difficulty = DIFFICULTY_MAP.get(task.get("difficulty", "medium"), 2)

    difficulty_diff = abs(user_skill - task_difficulty)
    if difficulty_diff == 0:
        score += 25.0  # Perfect match
    elif difficulty_diff == 1:
        score += 15.0  # Close match
    else:
        score += 5.0   # Mismatch

    # Prerequisites check
    prerequisites = task.get("prerequisites", [])
    completed_tasks = user_ctx.get("completed_task_ids", [])
    if not prerequisites or all(p in completed_tasks for p in prerequisites):
        score += 20.0

    # Next logical step (order-based)
    order = task.get("order_in_module", 0)
    completed_in_module = len([
        t for t in completed_tasks
        if t.startswith(task_module or "")
    ]) if task_module else 0

    if order == completed_in_module + 1:
        score += 15.0  # This is the next task
    elif order <= completed_in_module:
        score -= 10.0  # Already completed or passed

    # Streak bonus
    streak = user_ctx.get("streak_days", 0)
    if streak > 0:
        score += min(10.0, streak * 2.0)  # Up to +10 for streak

    return max(0.0, min(100.0, score))


# ============================================================================
# MODULE SCORING
# ============================================================================

def score_module_priority(user_ctx: UserContext, module: ModuleData) -> float:
    """
    Score module priority for a user.

    Factors:
    - Is this the current module? (+35)
    - Progress percentage in module (+20 max)
    - Difficulty appropriateness (+20)
    - Prerequisites met (+15)
    - Path order bonus (+10)

    Args:
        user_ctx: User context dictionary
        module: Module data dictionary

    Returns:
        Score from 0-100
    """
    score = 0.0

    module_id = module.get("module_id", "")

    # Current module gets high priority
    if user_ctx.get("current_module_id") == module_id:
        score += 35.0

    # Progress scoring - higher progress = higher priority to complete
    total_tasks = module.get("total_tasks", 1)
    completed_tasks = module.get("completed_tasks", 0)
    if total_tasks > 0:
        progress = completed_tasks / total_tasks
        if 0 < progress < 1:
            score += progress * 20.0  # Partial progress bonus
        elif progress >= 1:
            score -= 20.0  # Already completed, lower priority

    # Difficulty match
    user_skill = SKILL_LEVEL_MAP.get(user_ctx.get("skill_level", "beginner"), 1)
    module_difficulty = DIFFICULTY_MAP.get(module.get("difficulty", "medium"), 2)

    difficulty_diff = abs(user_skill - module_difficulty)
    if difficulty_diff == 0:
        score += 20.0
    elif difficulty_diff == 1:
        score += 10.0

    # Prerequisites
    prerequisites = module.get("prerequisites", [])
    completed_modules = user_ctx.get("completed_module_ids", [])
    if not prerequisites or all(p in completed_modules for p in prerequisites):
        score += 15.0
    else:
        score -= 15.0  # Can't start yet

    # Path order - earlier in path slightly preferred if not started
    order = module.get("order_in_path", 0)
    if completed_tasks == 0 and order > 0:
        score += max(0, 10 - order)  # Bonus decreases with order

    return max(0.0, min(100.0, score))


# ============================================================================
# STUDYFLOW SCORING
# ============================================================================

def score_studyflow_mode(user_ctx: UserContext, studyflow: StudyflowData) -> float:
    """
    Score how appropriate a studyflow configuration is for a user.

    Factors:
    - Time of day appropriateness (+25)
    - Session duration match with preference (+25)
    - Energy level consideration (+20)
    - Recent activity factor (+15)
    - Streak maintenance (+15)

    Args:
        user_ctx: User context dictionary
        studyflow: Studyflow configuration

    Returns:
        Score from 0-100
    """
    score = 0.0

    mode = studyflow.get("mode", "pomodoro")
    duration = studyflow.get("duration", 25)
    intensity = studyflow.get("intensity", "medium")

    # Time of day scoring
    time_of_day = user_ctx.get("time_of_day", "afternoon")
    time_factor = TIME_OF_DAY_FOCUS.get(time_of_day, 1.0)

    # Mode appropriateness by time
    if time_of_day in ("morning", "afternoon"):
        if mode == "sprint" and intensity == "high":
            score += 25.0 * time_factor
        elif mode == "pomodoro":
            score += 20.0 * time_factor
        else:
            score += 15.0 * time_factor
    else:  # evening/night
        if mode == "pomodoro" and intensity in ("low", "medium"):
            score += 25.0 * time_factor
        elif mode == "taskrunner":
            score += 20.0 * time_factor
        else:
            score += 10.0 * time_factor

    # Duration preference match
    preferred = user_ctx.get("preferred_session_duration", 25)
    duration_diff = abs(duration - preferred)
    if duration_diff <= 5:
        score += 25.0
    elif duration_diff <= 15:
        score += 15.0
    else:
        score += 5.0

    # Energy level (based on study time today)
    study_today = user_ctx.get("study_minutes_today", 0)
    if study_today < 30:
        # Fresh - can handle high intensity
        if intensity == "high":
            score += 20.0
        elif intensity == "medium":
            score += 15.0
        else:
            score += 10.0
    elif study_today < 90:
        # Some fatigue
        if intensity == "medium":
            score += 20.0
        elif intensity == "low":
            score += 15.0
        else:
            score += 5.0
    else:
        # Tired - prefer low intensity
        if intensity == "low":
            score += 20.0
        else:
            score += 5.0

    # Recent activity
    last_activity = user_ctx.get("last_activity_minutes_ago")
    if last_activity is not None:
        if last_activity < 30:
            score += 15.0  # Recently active, momentum
        elif last_activity < 120:
            score += 10.0
        else:
            score += 5.0  # Cold start

    # Streak maintenance
    streak = user_ctx.get("streak_days", 0)
    if streak > 0 and study_today == 0:
        # Need to study to maintain streak
        score += 15.0

    return max(0.0, min(100.0, score))
