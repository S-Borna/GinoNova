"""
Shared AI Schemas Package
Phase 7.3: Cross-language schema module for AI Engine

This package provides the shared Pydantic models for the AI Engine,
enabling consistent data contracts across the monorepo.
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
]
