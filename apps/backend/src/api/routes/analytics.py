"""
Analytics API Routes - Phase 13
Phase SECURITY: Added authentication and fixed IDOR vulnerabilities

Event tracking and insights endpoints.
All endpoints require authentication and enforce authorization.
Users can only access their own analytics data unless they are admins.
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
from src.core.deps import CurrentUser, AdminUser

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
    current_user: CurrentUser,
    db: Session = Depends(get_db)
):
    """
    Track an analytics event for the authenticated user.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Users can only track events for themselves.

    Args:
        request: Event data to track
        current_user: Authenticated user (injected)
        db: Database session

    Returns:
        Event tracking confirmation
        
    Raises:
        401: If not authenticated
    """
    user_id = current_user.id

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
    current_user: CurrentUser,
    db: Session = Depends(get_db)
):
    """
    Get analytics summary for a user.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Users can only view their own analytics unless they are admins.

    Args:
        user_id: User ID to get analytics for
        current_user: Authenticated user (injected)
        db: Database session

    Returns:
        User analytics summary
        
    Raises:
        401: If not authenticated
        403: If user tries to access another user's analytics without admin privileges
        404: If user not found
    """
    # Authorization check: users can only view their own analytics unless admin
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own analytics"
        )

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
    current_user: CurrentUser,
    days: int = Query(30, le=365),
    db: Session = Depends(get_db)
):
    """
    Get daily statistics for a user.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Users can only view their own daily stats unless they are admins.

    Args:
        user_id: User ID to get daily stats for
        current_user: Authenticated user (injected)
        days: Number of days to fetch
        db: Database session

    Returns:
        Daily statistics for the specified period
        
    Raises:
        401: If not authenticated
        403: If user tries to access another user's stats without admin privileges
    """
    # Authorization check: users can only view their own stats unless admin
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own daily statistics"
        )
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
    current_user: CurrentUser
):
    """
    Get computed insights for a user.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Users can only view their own insights unless they are admins.

    Args:
        user_id: User ID to get insights for
        current_user: Authenticated user (injected)

    Returns:
        User insights and recommendations
        
    Raises:
        401: If not authenticated
        403: If user tries to access another user's insights without admin privileges
    """
    # Authorization check: users can only view their own insights unless admin
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own insights"
        )
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
    current_user: CurrentUser,
    weeks: int = Query(12, le=52),
    db: Session = Depends(get_db)
):
    """
    Get activity heatmap data (like GitHub contribution graph).
    
    **Authentication required**: Must be logged in.
    **Authorization**: Users can only view their own heatmap unless they are admins.

    Args:
        user_id: User ID to get heatmap for
        current_user: Authenticated user (injected)
        weeks: Number of weeks to include
        db: Database session

    Returns:
        Activity heatmap data
        
    Raises:
        401: If not authenticated
        403: If user tries to access another user's heatmap without admin privileges
    """
    # Authorization check: users can only view their own heatmap unless admin
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own activity heatmap"
        )
    analytics_service = AnalyticsService(db)
    heatmap_data = analytics_service.get_activity_heatmap(user_id, weeks)

    return {
        "user_id": str(user_id),
        "weeks": weeks,
        "data": heatmap_data,
    }


@router.get("/leaderboard")
async def get_leaderboard(
    current_user: CurrentUser,
    period: str = Query("week", regex="^(day|week|month|all)$"),
    metric: str = Query("xp", regex="^(xp|tasks|streak|hours)$"),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    """
    Get leaderboard based on various metrics.
    
    **Authentication required**: Must be logged in to view leaderboard.

    Args:
        current_user: Authenticated user (injected)
        period: Time period (day, week, month, all)
        metric: Metric to rank by (xp, tasks, streak, hours)
        limit: Max entries to return
        db: Database session

    Returns:
        Leaderboard rankings
        
    Raises:
        401: If not authenticated
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
    admin_user: AdminUser,
    db: Session = Depends(get_db)
):
    """
    Get platform-wide analytics overview.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Admin access required.

    Args:
        admin_user: Authenticated admin user (injected)
        db: Database session

    Returns:
        Platform-wide analytics overview
        
    Raises:
        401: If not authenticated
        403: If user is not an admin
    """
    analytics_service = AnalyticsService(db)
    overview_data = analytics_service.get_platform_overview()

    return overview_data


@router.get("/admin/modules")
async def get_module_analytics(
    admin_user: AdminUser
):
    """
    Get analytics for all modules.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Admin access required.

    Args:
        admin_user: Authenticated admin user (injected)

    Returns:
        Analytics for all modules
        
    Raises:
        401: If not authenticated
        403: If user is not an admin
    """
    # TODO: Fetch from module_analytics table
    return {
        "modules": [],
    }


@router.get("/admin/retention")
async def get_retention_analytics(
    admin_user: AdminUser,
    cohort_type: str = Query("week", regex="^(day|week|month)$")
):
    """
    Get user retention cohort analysis.
    
    **Authentication required**: Must be logged in.
    **Authorization**: Admin access required.

    Args:
        admin_user: Authenticated admin user (injected)
        cohort_type: Cohort grouping type (day, week, month)

    Returns:
        User retention cohort analysis
        
    Raises:
        401: If not authenticated
        403: If user is not an admin
    """
    return {
        "cohort_type": cohort_type,
        "cohorts": [],
    }
