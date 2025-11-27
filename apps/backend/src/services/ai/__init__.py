"""
AI Services Package
Phase 7.2: AI service layer with structured stub implementations

This package contains the AI engine service classes that provide
the business logic layer between API controllers and future AI/ML models.
"""
from .recommendation_service import RecommendationService
from .next_step_service import NextStepService
from .difficulty_service import DifficultyService
from .summary_service import SummaryService

# Service singletons
recommendation_service = RecommendationService()
next_step_service = NextStepService()
difficulty_service = DifficultyService()
summary_service = SummaryService()

__all__ = [
    "RecommendationService",
    "NextStepService",
    "DifficultyService",
    "SummaryService",
    "recommendation_service",
    "next_step_service",
    "difficulty_service",
    "summary_service",
]
