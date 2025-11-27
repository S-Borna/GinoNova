"""
Shared AI Schemas Package
Phase 7.4: Cross-language schema module for AI Engine with rule engine

This package provides the shared Pydantic models for the AI Engine,
enabling consistent data contracts across the monorepo.

Subpackages:
- engine: Deterministic rule engine (scoring, rules, heuristics)
"""
from .schemas import (
    TaskRecommendation,
    ModuleRecommendation,
    StudyflowRecommendation,
    Recommendations,
    RecommendationsResponse,
    NextStepResponse,
    DifficultyEstimate,
    SummaryHighlight,
    DailySummaryResponse,
    AIStatusResponse,
)

# Engine exports (Phase 7.4)
from .engine import (
    # Scoring functions
    score_task_relevance,
    score_module_priority,
    score_studyflow_mode,
    # Rule sets
    TASK_PRIORITY_RULES,
    MODULE_SELECTION_RULES,
    STUDYFLOW_MODE_RULES,
    apply_rules,
    # Heuristics
    compute_recommendation_scores,
    compute_difficulty_adjustment,
    compute_daily_highlights,
)

__all__ = [
    # Recommendation schemas
    "TaskRecommendation",
    "ModuleRecommendation",
    "StudyflowRecommendation",
    "Recommendations",
    "RecommendationsResponse",
    # Next step schemas
    "NextStepResponse",
    # Difficulty schemas
    "DifficultyEstimate",
    # Summary schemas
    "SummaryHighlight",
    "DailySummaryResponse",
    # Status schemas
    "AIStatusResponse",
    # Scoring functions (Phase 7.4)
    "score_task_relevance",
    "score_module_priority",
    "score_studyflow_mode",
    # Rule sets (Phase 7.4)
    "TASK_PRIORITY_RULES",
    "MODULE_SELECTION_RULES",
    "STUDYFLOW_MODE_RULES",
    "apply_rules",
    # Heuristics (Phase 7.4)
    "compute_recommendation_scores",
    "compute_difficulty_adjustment",
    "compute_daily_highlights",
]
