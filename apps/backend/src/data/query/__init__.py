# Phase 8.5 — Data Query Engine
# Safe, deterministic read-only queries for AI engines

from .task_query import (
    query_user_tasks,
    query_task_completions,
    query_task_by_module,
    get_task_summary,
)
from .pattern_query import (
    query_study_patterns,
    query_peak_hours,
    query_productivity_trends,
)
from .difficulty_query import (
    query_difficulty_distribution,
    query_difficulty_performance,
    query_recommended_difficulty,
)

__all__ = [
    # Task queries
    "query_user_tasks",
    "query_task_completions",
    "query_task_by_module",
    "get_task_summary",
    # Pattern queries
    "query_study_patterns",
    "query_peak_hours",
    "query_productivity_trends",
    # Difficulty queries
    "query_difficulty_distribution",
    "query_difficulty_performance",
    "query_recommended_difficulty",
]
