"""
AI Rule Engine
Phase 7.11: Deterministic rule engine with metrics and tracing

This package provides the core AI engine components:
- scoring: Pure scoring functions (0-100 range)
- rules: Static rule definitions
- heuristics: High-level recommendation logic
- metrics: Performance instrumentation (histograms, counters)

No ML. No randomness. Pure deterministic logic.
"""
from .scoring import (
    score_task_relevance,
    score_module_priority,
    score_studyflow_mode,
    # TypedDicts
    UserContext,
    TaskData,
    ModuleData,
    StudyflowData,
)
from .rules import (
    TASK_PRIORITY_RULES,
    MODULE_SELECTION_RULES,
    STUDYFLOW_MODE_RULES,
    apply_rules,
)
from .heuristics import (
    compute_recommendation_scores,
    compute_difficulty_adjustment,
    compute_daily_highlights,
    # TypedDicts
    ProgressData,
)
from .metrics import (
    Histogram,
    Counter,
    MetricRegistry,
    WORKER_METRICS,
    get_worker_latency,
    get_worker_errors,
    record_worker_latency,
    record_worker_error,
    get_all_metrics,
    reset_all_metrics,
)

__all__ = [
    # Scoring functions
    "score_task_relevance",
    "score_module_priority",
    "score_studyflow_mode",
    # TypedDicts (scoring)
    "UserContext",
    "TaskData",
    "ModuleData",
    "StudyflowData",
    # Rule sets
    "TASK_PRIORITY_RULES",
    "MODULE_SELECTION_RULES",
    "STUDYFLOW_MODE_RULES",
    "apply_rules",
    # Heuristics
    "compute_recommendation_scores",
    "compute_difficulty_adjustment",
    "compute_daily_highlights",
    # TypedDicts (heuristics)
    "ProgressData",
    # Metrics
    "Histogram",
    "Counter",
    "MetricRegistry",
    "WORKER_METRICS",
    "get_worker_latency",
    "get_worker_errors",
    "record_worker_latency",
    "record_worker_error",
    "get_all_metrics",
    "reset_all_metrics",
]
