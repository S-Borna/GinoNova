"""
AI Heuristics
Phase 7.4: High-level deterministic recommendation logic

Combines scoring functions and rules to produce final recommendations.
No ML. No external dependencies. Pure deterministic logic.
"""
from typing import TypedDict

from .scoring import (
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
from .rules import (
    TASK_PRIORITY_RULES,
    MODULE_SELECTION_RULES,
    STUDYFLOW_MODE_RULES,
    apply_rules,
)


# ============================================================================
# TYPE DEFINITIONS
# ============================================================================

class ScoredTask(TypedDict):
    """Task with computed score."""
    task: TaskData
    score: float
    triggered_rules: list[str]


class ScoredModule(TypedDict):
    """Module with computed score."""
    module: ModuleData
    score: float
    triggered_rules: list[str]


class ScoredStudyflow(TypedDict):
    """Studyflow config with computed score."""
    studyflow: StudyflowData
    score: float
    triggered_rules: list[str]


class RecommendationScores(TypedDict):
    """All recommendation scores."""
    tasks: list[ScoredTask]
    modules: list[ScoredModule]
    studyflows: list[ScoredStudyflow]
    top_task: ScoredTask | None
    top_module: ScoredModule | None
    top_studyflow: ScoredStudyflow | None


class DifficultyAdjustment(TypedDict):
    """Difficulty adjustment result."""
    base_difficulty: str
    adjusted_difficulty: float  # 1.0-5.0 scale
    estimated_minutes: int
    success_probability: float
    factors: list[str]


class DailyHighlight(TypedDict):
    """A highlight for the daily summary."""
    type: str  # "achievement", "progress", "streak", "recommendation"
    title: str
    description: str
    metric: str | None


class ProgressData(TypedDict, total=False):
    """User progress data for highlights."""
    tasks_completed_today: int
    xp_earned_today: int
    study_minutes_today: int
    streak_days: int
    modules_in_progress: list[ModuleData]
    recent_achievements: list[str]


# ============================================================================
# RECOMMENDATION SCORING
# ============================================================================

def compute_recommendation_scores(
    user_ctx: UserContext,
    modules: list[ModuleData],
    tasks: list[TaskData],
    studyflows: list[StudyflowData],
) -> RecommendationScores:
    """
    Compute recommendation scores for all items.

    Combines base scoring functions with rule-based modifiers
    to produce final ranked recommendations.

    Args:
        user_ctx: User context dictionary
        modules: List of available modules
        tasks: List of available tasks
        studyflows: List of studyflow configurations

    Returns:
        RecommendationScores with ranked items and top picks
    """
    # Score all tasks
    scored_tasks: list[ScoredTask] = []
    for task in tasks:
        base_score = score_task_relevance(user_ctx, task)
        rule_modifier, triggered = apply_rules(TASK_PRIORITY_RULES, user_ctx, task)
        final_score = min(100.0, base_score + rule_modifier)
        scored_tasks.append({
            "task": task,
            "score": final_score,
            "triggered_rules": triggered,
        })
    scored_tasks.sort(key=lambda x: x["score"], reverse=True)

    # Score all modules
    scored_modules: list[ScoredModule] = []
    for module in modules:
        base_score = score_module_priority(user_ctx, module)
        rule_modifier, triggered = apply_rules(MODULE_SELECTION_RULES, user_ctx, module)
        final_score = min(100.0, base_score + rule_modifier)
        scored_modules.append({
            "module": module,
            "score": final_score,
            "triggered_rules": triggered,
        })
    scored_modules.sort(key=lambda x: x["score"], reverse=True)

    # Score all studyflows
    scored_studyflows: list[ScoredStudyflow] = []
    for studyflow in studyflows:
        base_score = score_studyflow_mode(user_ctx, studyflow)
        rule_modifier, triggered = apply_rules(STUDYFLOW_MODE_RULES, user_ctx, studyflow)
        final_score = min(100.0, base_score + rule_modifier)
        scored_studyflows.append({
            "studyflow": studyflow,
            "score": final_score,
            "triggered_rules": triggered,
        })
    scored_studyflows.sort(key=lambda x: x["score"], reverse=True)

    return {
        "tasks": scored_tasks,
        "modules": scored_modules,
        "studyflows": scored_studyflows,
        "top_task": scored_tasks[0] if scored_tasks else None,
        "top_module": scored_modules[0] if scored_modules else None,
        "top_studyflow": scored_studyflows[0] if scored_studyflows else None,
    }


# ============================================================================
# DIFFICULTY ADJUSTMENT
# ============================================================================

def compute_difficulty_adjustment(
    user_ctx: UserContext,
    task: TaskData,
) -> DifficultyAdjustment:
    """
    Compute user-adjusted difficulty for a task.

    Adjusts base difficulty based on:
    - User skill level vs task difficulty
    - Prerequisite completion
    - Recent performance indicators (streak, XP)
    - Time factors

    Args:
        user_ctx: User context dictionary
        task: Task data dictionary

    Returns:
        DifficultyAdjustment with adjusted metrics
    """
    factors: list[str] = []

    # Base difficulty
    base_difficulty = task.get("difficulty", "medium")
    base_value = DIFFICULTY_MAP.get(base_difficulty, 2)

    # Start with base difficulty on 1-5 scale
    adjusted = float(base_value) + 1.0  # Convert 1-3 to 2-4

    # Skill level adjustment
    user_skill = SKILL_LEVEL_MAP.get(user_ctx.get("skill_level", "beginner"), 1)
    task_difficulty = DIFFICULTY_MAP.get(base_difficulty, 2)

    skill_diff = task_difficulty - user_skill
    if skill_diff > 0:
        adjusted += skill_diff * 0.5
        factors.append(f"Above skill level (+{skill_diff * 0.5:.1f})")
    elif skill_diff < 0:
        adjusted += skill_diff * 0.3
        factors.append(f"Below skill level ({skill_diff * 0.3:.1f})")

    # Prerequisites check
    prerequisites = task.get("prerequisites", [])
    completed = user_ctx.get("completed_task_ids", [])
    prereqs_met = all(p in completed for p in prerequisites)

    if not prereqs_met and prerequisites:
        adjusted += 1.0
        factors.append("Missing prerequisites (+1.0)")
    elif prereqs_met and prerequisites:
        adjusted -= 0.2
        factors.append("Prerequisites completed (-0.2)")

    # Streak bonus (momentum helps)
    streak = user_ctx.get("streak_days", 0)
    if streak >= 7:
        adjusted -= 0.3
        factors.append("Strong streak momentum (-0.3)")
    elif streak >= 3:
        adjusted -= 0.1
        factors.append("Good streak (-0.1)")

    # Time of day factor
    time_of_day = user_ctx.get("time_of_day", "afternoon")
    if time_of_day == "night":
        adjusted += 0.3
        factors.append("Late night (+0.3)")
    elif time_of_day == "morning":
        adjusted -= 0.1
        factors.append("Morning freshness (-0.1)")

    # Clamp to 1.0-5.0 range
    adjusted = max(1.0, min(5.0, adjusted))

    # Estimate duration
    base_minutes = task.get("estimated_minutes", 25)
    duration_factor = adjusted / 3.0  # Normalize around medium
    estimated_minutes = int(base_minutes * duration_factor)

    # Success probability
    # Higher adjusted difficulty = lower success probability
    success_prob = max(0.3, min(0.95, 1.0 - (adjusted - 1.0) / 5.0))

    return {
        "base_difficulty": base_difficulty,
        "adjusted_difficulty": round(adjusted, 2),
        "estimated_minutes": max(5, estimated_minutes),
        "success_probability": round(success_prob, 2),
        "factors": factors,
    }


# ============================================================================
# DAILY HIGHLIGHTS
# ============================================================================

def compute_daily_highlights(
    user_ctx: UserContext,
    progress: ProgressData,
) -> list[DailyHighlight]:
    """
    Compute highlights for daily summary.

    Generates personalized highlights based on user progress.

    Args:
        user_ctx: User context dictionary
        progress: Progress data for the day

    Returns:
        List of DailyHighlight objects
    """
    highlights: list[DailyHighlight] = []

    # Streak highlight
    streak = progress.get("streak_days", user_ctx.get("streak_days", 0))
    if streak > 0:
        if streak >= 30:
            title = "🔥 Monthly Streak Master!"
            desc = f"Incredible! You've maintained a {streak}-day learning streak."
        elif streak >= 7:
            title = "🔥 Week-long Streak!"
            desc = f"Amazing consistency! {streak} days of continuous learning."
        else:
            title = "🔥 Streak Active"
            desc = f"Keep it up! You're on a {streak}-day streak."

        highlights.append({
            "type": "streak",
            "title": title,
            "description": desc,
            "metric": f"{streak} days",
        })

    # Tasks completed highlight
    tasks_completed = progress.get("tasks_completed_today", 0)
    if tasks_completed > 0:
        if tasks_completed >= 5:
            title = "🎯 Productivity Champion!"
            desc = f"Outstanding! You completed {tasks_completed} tasks today."
        elif tasks_completed >= 3:
            title = "🎯 Great Progress!"
            desc = f"Solid work! {tasks_completed} tasks completed today."
        else:
            title = "🎯 Task Complete"
            desc = f"You completed {tasks_completed} task(s) today."

        highlights.append({
            "type": "achievement",
            "title": title,
            "description": desc,
            "metric": str(tasks_completed),
        })

    # XP highlight
    xp_earned = progress.get("xp_earned_today", 0)
    if xp_earned >= 100:
        highlights.append({
            "type": "achievement",
            "title": "⭐ XP Milestone",
            "description": f"You earned {xp_earned} XP today!",
            "metric": f"{xp_earned} XP",
        })

    # Study time highlight
    study_minutes = progress.get("study_minutes_today", 0)
    if study_minutes >= 60:
        hours = study_minutes // 60
        mins = study_minutes % 60
        time_str = f"{hours}h {mins}m" if mins else f"{hours}h"
        highlights.append({
            "type": "progress",
            "title": "📚 Deep Focus",
            "description": f"You've studied for {time_str} today!",
            "metric": time_str,
        })
    elif study_minutes >= 30:
        highlights.append({
            "type": "progress",
            "title": "📚 Good Session",
            "description": f"{study_minutes} minutes of focused learning.",
            "metric": f"{study_minutes} min",
        })

    # Module progress highlights
    modules_in_progress = progress.get("modules_in_progress", [])
    for module in modules_in_progress[:2]:  # Top 2 modules
        total = module.get("total_tasks", 1)
        completed = module.get("completed_tasks", 0)
        if total > 0:
            pct = int((completed / total) * 100)
            if pct >= 90:
                highlights.append({
                    "type": "progress",
                    "title": "🏁 Almost There!",
                    "description": f"{module.get('name', 'Module')} is {pct}% complete.",
                    "metric": f"{pct}%",
                })
            elif pct >= 50:
                highlights.append({
                    "type": "progress",
                    "title": "📈 Halfway Point",
                    "description": f"You're {pct}% through {module.get('name', 'the module')}.",
                    "metric": f"{pct}%",
                })

    # Recent achievements
    achievements = progress.get("recent_achievements", [])
    for achievement in achievements[:2]:  # Top 2 achievements
        highlights.append({
            "type": "achievement",
            "title": "🏆 Achievement Unlocked",
            "description": achievement,
            "metric": None,
        })

    # Recommendation if no activity
    if tasks_completed == 0 and study_minutes == 0:
        highlights.append({
            "type": "recommendation",
            "title": "💡 Ready to Start?",
            "description": "A quick 15-minute session can build momentum!",
            "metric": None,
        })

    return highlights
