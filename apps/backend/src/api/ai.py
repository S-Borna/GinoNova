"""
AI Engine API Controller
Phase 7.9: AI Controller with worker integration layer

This module provides the API surface for the DevOpsHub AI Engine.
Endpoints delegate to service classes for business logic.
Async endpoints delegate to stubbed workers for future async pipelines.
"""
from typing import Any, Optional
from uuid import UUID

from fastapi import APIRouter, Query

from shared.ai import (
    RecommendationsResponse,
    NextStepResponse,
    DifficultyEstimate,
    DailySummaryResponse,
    AIStatusResponse,
)
from ..services.ai import (
    recommendation_service,
    next_step_service,
    difficulty_service,
    summary_service,
)


# ============================================================================
# ROUTER
# ============================================================================

ai_router = APIRouter()


# ============================================================================
# STATUS ENDPOINT
# ============================================================================

@ai_router.get("/status", response_model=AIStatusResponse)
def ai_status() -> AIStatusResponse:
    """
    Phase 7.9 AI Engine status check.

    Returns the current status of all AI engine components.
    """
    return AIStatusResponse(
        phase="7.9",
        feature="Worker Integration Layer (Stubbed)",
        status="operational",
        engines={
            "recommendation": "active (db-integrated, cached)",
            "next_step": "active (db-integrated, cached)",
            "difficulty_estimator": "active (db-integrated, cached)",
            "summary": "active (db-integrated, cached)",
            "scoring": "active",
            "rules": "active",
            "heuristics": "active",
            "cache": "active (in-memory, TTL=300s)",
            "tests": "ready",
            "workers": "stubbed",
        },
        cache_enabled=True,
        fallback_mode="deterministic",
    )
# ============================================================================
# RECOMMENDATIONS ENDPOINT
# ============================================================================

@ai_router.get("/recommendations", response_model=RecommendationsResponse)
def get_recommendations(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendations"),
    limit: int = Query(5, ge=1, le=20, description="Maximum number of recommendations"),
    include_reasoning: bool = Query(False, description="Include reasoning explanations"),
) -> RecommendationsResponse:
    """
    Get personalized AI recommendations.

    Returns recommendations for:
    - Next task to complete
    - Next module to start/continue
    - Optimal studyflow session configuration

    **Phase 7.2:** Delegates to RecommendationService (stub mode).
    """
    return recommendation_service.get_recommendations(
        user_id=user_id,
        limit=limit,
        include_reasoning=include_reasoning,
    )
# ============================================================================
# NEXT STEP ENDPOINT
# ============================================================================

@ai_router.get("/next_step", response_model=NextStepResponse)
def get_next_step(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendation"),
) -> NextStepResponse:
    """
    Get the single most optimal next action.

    Returns a single recommendation for what the user should do next,
    considering their current progress, recent activity, and learning goals.

    **Phase 7.2:** Delegates to NextStepService (stub mode).
    """
    return next_step_service.get_next_step(user_id=user_id)
# ============================================================================
# DIFFICULTY ESTIMATE ENDPOINT
# ============================================================================

@ai_router.get("/difficulty/{task_id}", response_model=DifficultyEstimate)
def get_difficulty_estimate(
    task_id: UUID,
    user_id: Optional[UUID] = Query(None, description="User ID for personalized estimate"),
) -> DifficultyEstimate:
    """
    Get user-adjusted difficulty estimate for a task.

    Estimates how difficult a specific task will be for a given user,
    taking into account their skill level, past performance, and prerequisites.

    **Phase 7.2:** Delegates to DifficultyService (stub mode).

    Args:
        task_id: UUID of the task to estimate
        user_id: Optional user ID for personalized estimate
    """
    return difficulty_service.estimate_difficulty(
        task_id=task_id,
        user_id=user_id,
    )
# ============================================================================
# DAILY SUMMARY ENDPOINT
# ============================================================================

@ai_router.get("/summary/today", response_model=DailySummaryResponse)
def get_daily_summary(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized summary"),
) -> DailySummaryResponse:
    """
    Get AI-generated daily summary.

    Returns a personalized summary of the user's progress today,
    including achievements, highlights, and motivational messaging.

    **Phase 7.2:** Delegates to SummaryService (stub mode).
    """
    return summary_service.get_daily_summary(user_id=user_id)


# ============================================================================
# ASYNC WORKER ENDPOINTS (Phase 7.9)
# ============================================================================

@ai_router.get("/recommendations/async")
def get_recommendations_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendations"),
    limit: int = Query(5, ge=1, le=20, description="Maximum number of recommendations"),
    include_reasoning: bool = Query(False, description="Include reasoning explanations"),
) -> dict[str, Any]:
    """
    Get personalized AI recommendations via async worker path.

    Phase 7.9: Delegates to RecommendWorker stub.
    Returns raw WorkerResult - no schema transformation.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return recommendation_service.get_recommendations_async(
        user_id=user_id,
        limit=limit,
        include_reasoning=include_reasoning,
    )


@ai_router.get("/next_step/async")
def get_next_step_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendation"),
) -> dict[str, Any]:
    """
    Get the single most optimal next action via async worker path.

    Phase 7.9: Delegates to NextStepWorker stub.
    Returns raw WorkerResult - no schema transformation.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return next_step_service.get_next_step_async(user_id=user_id)


@ai_router.get("/difficulty/{task_id}/async")
def get_difficulty_estimate_async(
    task_id: UUID,
    user_id: Optional[UUID] = Query(None, description="User ID for personalized estimate"),
) -> dict[str, Any]:
    """
    Get user-adjusted difficulty estimate via async worker path.

    Phase 7.9: Delegates to DifficultyWorker stub.
    Returns raw WorkerResult - no schema transformation.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return difficulty_service.estimate_difficulty_async(
        task_id=task_id,
        user_id=user_id,
    )


@ai_router.get("/summary/today/async")
def get_daily_summary_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized summary"),
) -> dict[str, Any]:
    """
    Get AI-generated daily summary via async worker path.

    Phase 7.9: Delegates to SummaryWorker stub.
    Returns raw WorkerResult - no schema transformation.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return summary_service.get_daily_summary_async(user_id=user_id)