"""
AI Engine API Controller
Phase 7.12: AI Controller with worker load simulator and stress harness
Phase 7.14: Added debug frames endpoint for error isolation diagnostics

This module provides the API surface for the DevOpsHub AI Engine.
Endpoints delegate to service classes for business logic.
Async endpoints delegate to workers with strict contract validation.
Tracing support with optional include_trace parameter for metrics visibility.
Load simulator available for deterministic stress testing.
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
from ..ai_logs.diagnostics import get_daily_diagnostics
from ..ai_diagnostics.debug_frames import get_recent_debug_frames


# ============================================================================
# ROUTER
# ============================================================================

ai_router = APIRouter()


# ============================================================================
# DIAGNOSTICS ENDPOINT (Phase 7.13)
# ============================================================================

@ai_router.get("/diagnostics")
def ai_diagnostics() -> dict:
    """
    Phase 7.13: AI Logs + Telemetry Diagnostics.

    Returns daily diagnostic summary from AI logs including:
    - AI calls today
    - Average latency
    - Error counts
    - Recommendation type breakdown
    - Next step usage counts

    This endpoint has zero performance impact on AI operations.
    Pure log-based summarization with no model usage.
    """
    return get_daily_diagnostics()


# ============================================================================
# DEBUG FRAMES ENDPOINT (Phase 7.14)
# ============================================================================

@ai_router.get("/debug-frames")
def ai_debug_frames(
    limit: int = Query(25, ge=1, le=100, description="Maximum number of frames to return"),
) -> list[dict[str, Any]]:
    """
    Phase 7.14: AI Debug Frames for Error Isolation.

    Returns the most recent debug frames from AI engine operations.
    Frames include:
    - Engine identification
    - Context validation status
    - Output validation status
    - Error messages
    - Schema/key introspection
    - Timestamps

    Frames are returned newest-first for debugging.
    This endpoint has zero performance impact on AI operations.
    """
    return get_recent_debug_frames(limit=limit)


# ============================================================================
# STATUS ENDPOINT
# ============================================================================

@ai_router.get("/status", response_model=AIStatusResponse)
def ai_status() -> AIStatusResponse:
    """
    Phase 7.12 AI Engine status check.

    Returns the current status of all AI engine components.
    """
    return AIStatusResponse(
        phase="7.12",
        feature="Worker Load Simulator",
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
            "workers": "validated",
            "metrics": "active (histogram, counters)",
            "tracing": "enabled",
            "load_simulator": "ready",
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
# ASYNC WORKER ENDPOINTS (Phase 7.11)
# ============================================================================

@ai_router.get("/recommendations/async")
def get_recommendations_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendations"),
    limit: int = Query(5, ge=1, le=20, description="Maximum number of recommendations"),
    include_reasoning: bool = Query(False, description="Include reasoning explanations"),
    include_trace: bool = Query(False, description="Include trace metadata envelope"),
) -> dict[str, Any]:
    """
    Get personalized AI recommendations via async worker path.

    Phase 7.11: Delegates to RecommendWorker with contract validation and tracing.
    Returns validated WorkerResult with strict type safety.
    If include_trace=True, returns {"data": {...}, "meta": {...}} with trace_id.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return recommendation_service.get_recommendations_async(
        user_id=user_id,
        limit=limit,
        include_reasoning=include_reasoning,
        include_trace=include_trace,
    )


@ai_router.get("/next_step/async")
def get_next_step_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized recommendation"),
    include_trace: bool = Query(False, description="Include trace metadata envelope"),
) -> dict[str, Any]:
    """
    Get the single most optimal next action via async worker path.

    Phase 7.11: Delegates to NextStepWorker with contract validation and tracing.
    Returns validated WorkerResult with strict type safety.
    If include_trace=True, returns {"data": {...}, "meta": {...}} with trace_id.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return next_step_service.get_next_step_async(
        user_id=user_id,
        include_trace=include_trace,
    )


@ai_router.get("/difficulty/{task_id}/async")
def get_difficulty_estimate_async(
    task_id: UUID,
    user_id: Optional[UUID] = Query(None, description="User ID for personalized estimate"),
    include_trace: bool = Query(False, description="Include trace metadata envelope"),
) -> dict[str, Any]:
    """
    Get user-adjusted difficulty estimate via async worker path.

    Phase 7.11: Delegates to DifficultyWorker with contract validation and tracing.
    Returns validated WorkerResult with strict type safety.
    If include_trace=True, returns {"data": {...}, "meta": {...}} with trace_id.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return difficulty_service.estimate_difficulty_async(
        task_id=task_id,
        user_id=user_id,
        include_trace=include_trace,
    )


@ai_router.get("/summary/today/async")
def get_daily_summary_async(
    user_id: Optional[UUID] = Query(None, description="User ID for personalized summary"),
    include_trace: bool = Query(False, description="Include trace metadata envelope"),
) -> dict[str, Any]:
    """
    Get AI-generated daily summary via async worker path.

    Phase 7.11: Delegates to SummaryWorker with contract validation and tracing.
    Returns validated WorkerResult with strict type safety.
    If include_trace=True, returns {"data": {...}, "meta": {...}} with trace_id.

    **Note:** Currently synchronous - async scheduling will be added later.
    """
    return summary_service.get_daily_summary_async(
        user_id=user_id,
        include_trace=include_trace,
    )