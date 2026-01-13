"""
Analytics API Routes - Phase 13
Event tracking and insights endpoints.
"""
from fastapi import APIRouter, HTTPException, Query, Request, Depends
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import logging

from src.db.database import get_db
from src.services.analytics_service import AnalyticsService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/analytics", tags=["analytics"])


# Event types for tracking
EVENT_TYPES = [
    "page_view",
    "task_start",
    "task_complete",
    "task_hint_used",
    "module_start",
    "module_complete",
    "session_start",
    "session_end",
    "ai_chat",
    "certificate_earned",
    "badge_earned",
    "streak_continued",
]


# Request/Response models
class TrackEventRequest(BaseModel):
    event_type: str
    event_data: dict = {}
    session_id: Optional[str] = None


class DailyStatsResponse(BaseModel):
    date: str
    study_minutes: int
    tasks_completed: int
    xp_earned: int


class UserAnalyticsResponse(BaseModel):
    total_study_hours: float
    tasks_completed: int
    current_streak: int
    longest_streak: int
    favorite_time: Optional[str]
    weekly_activity: List[int]


@router.post("/event")
async def track_event(
    request: TrackEventRequest,
    req: Request,
    user_id: Optional[UUID] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Track an analytics event.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    if request.event_type not in EVENT_TYPES:
        logger.warning(f"Unknown event type: {request.event_type}")
        # Still track it, just log warning

    # Store event in database
    analytics_service = AnalyticsService(db)
    event = analytics_service.track_event(
        user_id=user_id,
        event_type=request.event_type,
        event_data=request.event_data,
        session_id=request.session_id,
        ip_address=req.client.host if req.client else None,
        user_agent=req.headers.get("user-agent")
    )

    logger.debug(f"Event tracked: {request.event_type} for user {user_id}")

    return {"tracked": True, "event_type": request.event_type, "event_id": str(event.id)}


@router.get("/user/{user_id}", response_model=UserAnalyticsResponse)
async def get_user_analytics(
    user_id: UUID,
    requesting_user: Optional[UUID] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Get analytics summary for a user.
    """
    # TODO: Check if requesting_user can view user_id's analytics
    # For now, users can view their own analytics

    analytics_service = AnalyticsService(db)
    data = analytics_service.get_user_analytics_summary(user_id)

    if not data:
        raise HTTPException(status_code=404, detail="User not found")

    return UserAnalyticsResponse(
        total_study_hours=data.get("total_study_hours", 0),
        tasks_completed=data.get("tasks_completed", 0),
        current_streak=data.get("current_streak", 0),
        longest_streak=data.get("longest_streak", 0),
        favorite_time=data.get("favorite_time", "evening"),
        weekly_activity=data.get("weekly_activity", [0] * 7)
    )


@router.get("/user/{user_id}/daily")
async def get_daily_stats(
    user_id: UUID,
    days: int = Query(30, le=365),
    requesting_user: Optional[UUID] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Get daily statistics for a user.
    """
    # Generate date range
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days)

    # Fetch from database
    analytics_service = AnalyticsService(db)
    stats = analytics_service.get_daily_stats(user_id, days)

    daily_stats = []
    for stat in stats:
        daily_stats.append({
            "date": stat.date.isoformat(),
            "study_minutes": stat.study_minutes,
            "tasks_completed": stat.tasks_completed,
            "xp_earned": stat.xp_earned,
            "sessions_count": stat.sessions_count,
            "ai_calls": stat.ai_calls
        })

    return {
        "user_id": str(user_id),
        "start_date": str(start_date),
        "end_date": str(end_date),
        "daily_stats": daily_stats,
    }


@router.get("/user/{user_id}/insights")
async def get_user_insights(
    user_id: UUID,
    requesting_user: Optional[UUID] = Query(None)
):
    """
    Get computed insights for a user.
    """
    # TODO: Fetch from user_insights table
    return {
        "user_id": str(user_id),
        "insights": {
            "strongest_skill": None,
            "weakest_skill": None,
            "recommended_focus": None,
            "estimated_completion": None,
            "study_pattern": "Ingen data ännu",
        }
    }


@router.get("/user/{user_id}/activity-heatmap")
async def get_activity_heatmap(
    user_id: UUID,
    weeks: int = Query(12, le=52),
    requesting_user: Optional[UUID] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Get activity heatmap data (like GitHub contribution graph).
    """
    analytics_service = AnalyticsService(db)
    heatmap_data = analytics_service.get_activity_heatmap(user_id, weeks)

    return {
        "user_id": str(user_id),
        "weeks": weeks,
        "data": heatmap_data,
    }


@router.get("/leaderboard")
async def get_leaderboard(
    period: str = Query("week", regex="^(day|week|month|all)$"),
    metric: str = Query("xp", regex="^(xp|tasks|streak|hours)$"),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    """
    Get leaderboard based on various metrics.
    """
    analytics_service = AnalyticsService(db)
    leaderboard_data = analytics_service.get_leaderboard(period, metric, limit)

    return {
        "period": period,
        "metric": metric,
        "leaderboard": leaderboard_data,
    }


# Admin endpoints
@router.get("/admin/overview")
async def get_admin_analytics(
    admin_user: Optional[UUID] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Get platform-wide analytics overview.
    Admin only.
    """
    # TODO: Check admin permissions

    analytics_service = AnalyticsService(db)
    overview_data = analytics_service.get_platform_overview()

    return overview_data


@router.get("/admin/modules")
async def get_module_analytics(
    admin_user: Optional[UUID] = Query(None)
):
    """
    Get analytics for all modules.
    Admin only.
    """
    # TODO: Fetch from module_analytics table
    return {
        "modules": [],
    }


@router.get("/admin/retention")
async def get_retention_analytics(
    admin_user: Optional[UUID] = Query(None),
    cohort_type: str = Query("week", regex="^(day|week|month)$")
):
    """
    Get user retention cohort analysis.
    Admin only.
    """
    return {
        "cohort_type": cohort_type,
        "cohorts": [],
    }
