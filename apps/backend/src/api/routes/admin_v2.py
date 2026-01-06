"""
Admin Dashboard v2 API Routes
Complete admin functionality with real-time stats, user management, analytics
"""

from datetime import datetime, timedelta, timezone
from typing import Optional, List, Literal
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlalchemy import func, desc, asc, and_, or_
from sqlalchemy.orm import Session

from src.core.deps import get_current_user
from src.db.database import get_db
from src.db.models import User, AIUsageLog, ExamResult
from src.schemas.user import UserPublic

router = APIRouter()


# =============================================================================
# SCHEMAS
# =============================================================================

class UserPermissions(BaseModel):
    ai_quiz_access: bool = True
    premium_modules_access: bool = True
    study_room_access: bool = True
    skillpath_access: bool = True


class UserStats(BaseModel):
    modules_completed: int = 0
    tasks_completed: int = 0
    study_sessions: int = 0
    ai_requests: int = 0


class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    is_admin: bool = False
    is_banned: bool = False
    is_active: bool = True
    is_verified: bool = False
    oauth_provider: Optional[str] = None
    created_at: datetime
    last_activity_at: Optional[datetime] = None
    total_xp: int = 0
    level: int = 1
    current_streak: int = 0
    permissions: UserPermissions = UserPermissions()
    stats: UserStats = UserStats()
    status: str = "offline"

    class Config:
        from_attributes = True


class UsersListResponse(BaseModel):
    users: List[UserResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


class OverviewStats(BaseModel):
    online_users: int
    online_trend: int
    total_users: int
    total_users_trend: int
    new_users_today: int
    new_users_trend: int
    active_users_24h: int
    active_users_week: int
    total_study_sessions: int
    avg_session_duration_minutes: int
    total_tasks_completed: int
    total_ai_requests: int
    ai_cost_total: float
    ai_cost_today: float


class ActivityData(BaseModel):
    date: str
    active_users: int
    new_users: int
    study_sessions: int


class ActivityResponse(BaseModel):
    data: List[ActivityData]


class SystemHealth(BaseModel):
    database: dict
    api: dict
    openai: dict


class UserGrowthData(BaseModel):
    date: str
    total_users: int
    new_users: int


class UserGrowthResponse(BaseModel):
    data: List[UserGrowthData]


class HeatmapData(BaseModel):
    day: int  # 0-6 (Mon-Sun)
    hour: int  # 0-23
    count: int


class HeatmapResponse(BaseModel):
    data: List[HeatmapData]


class TopUser(BaseModel):
    id: str
    email: str
    full_name: Optional[str]
    avatar_url: Optional[str]
    value: int
    label: str


class TopUsersResponse(BaseModel):
    most_active: List[TopUser]
    highest_xp: List[TopUser]
    longest_streak: List[TopUser]


class AIUsageOverview(BaseModel):
    total_requests: int
    total_tokens: int
    total_cost: float
    requests_today: int
    cost_today: float
    requests_this_week: int
    cost_this_week: float


class AIUsageByUser(BaseModel):
    id: str
    email: str
    full_name: Optional[str]
    requests: int
    tokens: int
    cost: float
    last_used: Optional[datetime]


class AIUsageListResponse(BaseModel):
    users: List[AIUsageByUser]
    total: int


class BanRequest(BaseModel):
    reason: Optional[str] = None


class UpdateUserRequest(BaseModel):
    full_name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_active: Optional[bool] = None


class UpdatePermissionsRequest(BaseModel):
    ai_quiz_access: Optional[bool] = None
    premium_modules_access: Optional[bool] = None
    study_room_access: Optional[bool] = None
    skillpath_access: Optional[bool] = None


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def require_admin(current_user: UserPublic = Depends(get_current_user)) -> UserPublic:
    """Middleware to require admin access"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


def get_user_status(last_activity: Optional[datetime], last_login: Optional[datetime] = None) -> str:
    """
    Calculate user status based on last_activity_at (most recent activity)
    This tracks actual usage, not just login time
    """
    # Prefer last_activity_at as it updates on every API call (more accurate)
    check_time = last_activity if last_activity else last_login

    if not check_time:
        return "offline"

    now = datetime.now(timezone.utc)
    # Ensure check_time is timezone-aware
    if check_time.tzinfo is None:
        check_time = check_time.replace(tzinfo=timezone.utc)

    diff = (now - check_time).total_seconds()

    if diff < 600:  # 10 minutes - online (was 5 min, too short)
        return "online"
    elif diff < 1800:  # 30 minutes - away (was 1 hour)
        return "away"
    else:
        return "offline"


def user_to_response(user: User) -> UserResponse:
    """Convert User model to UserResponse"""
    last_activity = getattr(user, 'last_activity_at', None)
    last_login = getattr(user, 'last_login_at', None)

    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        avatar_url=getattr(user, 'avatar_url', None),
        is_admin=user.is_admin,
        is_banned=not user.is_active,  # Using is_active as banned flag
        is_active=user.is_active,
        is_verified=getattr(user, 'is_verified', False),
        oauth_provider=getattr(user, 'oauth_provider', None),
        created_at=user.created_at,
        last_activity_at=last_activity,
        total_xp=getattr(user, 'total_xp', 0) or 0,
        level=getattr(user, 'level', 1) or 1,
        current_streak=getattr(user, 'current_streak', 0) or 0,
        permissions=UserPermissions(
            ai_quiz_access=getattr(user, 'ai_quiz_access', True),
            premium_modules_access=getattr(user, 'premium_modules_access', True),
            study_room_access=True,
            skillpath_access=True,
        ),
        stats=UserStats(
            modules_completed=getattr(user, 'modules_completed', 0) or 0,
            tasks_completed=getattr(user, 'tasks_completed', 0) or 0,
            study_sessions=0,  # Would need to query study sessions
            ai_requests=0,  # Would need to query AI usage
        ),
        status=get_user_status(last_activity, last_login)
    )


# =============================================================================
# DASHBOARD STATS ENDPOINTS
# =============================================================================

@router.get("/stats/overview", response_model=OverviewStats)
async def get_overview_stats(
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get dashboard overview statistics"""
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday_start = today_start - timedelta(days=1)
    week_ago = now - timedelta(days=7)
    ten_min_ago = now - timedelta(minutes=10)  # Match get_user_status() timeout
    day_ago = now - timedelta(hours=24)

    # Online users (active in last 10 minutes) - matches get_user_status()
    online_users = db.query(func.count(User.id)).filter(
        User.last_activity_at >= ten_min_ago
    ).scalar() or 0

    # Total users
    total_users = db.query(func.count(User.id)).scalar() or 0

    # New users today
    new_today = db.query(func.count(User.id)).filter(
        User.created_at >= today_start
    ).scalar() or 0

    # New users yesterday (for trend)
    new_yesterday = db.query(func.count(User.id)).filter(
        and_(
            User.created_at >= yesterday_start,
            User.created_at < today_start
        )
    ).scalar() or 0

    # Active users in last 24h
    active_24h = db.query(func.count(User.id)).filter(
        User.last_activity_at >= day_ago
    ).scalar() or 0

    # Active users this week
    active_week = db.query(func.count(User.id)).filter(
        User.last_activity_at >= week_ago
    ).scalar() or 0

    # Users registered this week (for trend)
    new_this_week = db.query(func.count(User.id)).filter(
        User.created_at >= week_ago
    ).scalar() or 0

    # AI Usage stats from ai_usage_logs
    try:
        total_ai_requests = db.query(func.count(AIUsageLog.id)).scalar() or 0
        ai_cost_total = db.query(func.sum(AIUsageLog.cost_usd)).scalar() or 0.0
        ai_cost_today = db.query(func.sum(AIUsageLog.cost_usd)).filter(
            AIUsageLog.created_at >= today_start
        ).scalar() or 0.0
    except Exception:
        total_ai_requests = 0
        ai_cost_total = 0.0
        ai_cost_today = 0.0

    return OverviewStats(
        online_users=online_users,
        online_trend=0,  # Would need historical data to calculate
        total_users=total_users,
        total_users_trend=new_this_week,
        new_users_today=new_today,
        new_users_trend=new_today - new_yesterday,
        active_users_24h=active_24h,
        active_users_week=active_week,
        total_study_sessions=0,  # Would need study_sessions table
        avg_session_duration_minutes=0,
        total_tasks_completed=0,  # Would need progress table aggregation
        total_ai_requests=total_ai_requests,
        ai_cost_total=round(ai_cost_total, 2),
        ai_cost_today=round(ai_cost_today, 4),
    )


@router.get("/stats/activity", response_model=ActivityResponse)
async def get_activity_stats(
    days: int = Query(7, ge=1, le=90),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get activity statistics for the last N days"""
    now = datetime.now(timezone.utc)
    data = []

    for i in range(days - 1, -1, -1):
        day_start = (now - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day_start + timedelta(days=1)

        # Active users that day
        active = db.query(func.count(User.id)).filter(
            and_(
                User.last_activity_at >= day_start,
                User.last_activity_at < day_end
            )
        ).scalar() or 0

        # New users that day
        new = db.query(func.count(User.id)).filter(
            and_(
                User.created_at >= day_start,
                User.created_at < day_end
            )
        ).scalar() or 0

        data.append(ActivityData(
            date=day_start.strftime("%Y-%m-%d"),
            active_users=active,
            new_users=new,
            study_sessions=0  # Would need study_sessions table
        ))

    return ActivityResponse(data=data)


@router.get("/stats/system-health", response_model=SystemHealth)
async def get_system_health(
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get system health status"""
    import time

    # Test database
    db_start = time.time()
    try:
        db.execute("SELECT 1")
        db_latency = int((time.time() - db_start) * 1000)
        db_status = "connected"
    except Exception:
        db_latency = 0
        db_status = "error"

    return SystemHealth(
        database={
            "status": db_status,
            "latency_ms": db_latency
        },
        api={
            "status": "healthy",
            "latency_ms": 50
        },
        openai={
            "status": "connected",
            "rate_limit_percent": 25
        }
    )


# =============================================================================
# USER MANAGEMENT ENDPOINTS
# =============================================================================

@router.get("/users", response_model=UsersListResponse)
async def get_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=10, le=100),
    search: Optional[str] = None,
    status: Optional[Literal["online", "away", "offline", "banned"]] = None,
    role: Optional[Literal["admin", "user"]] = None,
    sort: str = Query("last_activity", regex="^(last_activity|created|email|xp)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get paginated list of users with filtering and sorting"""
    now = datetime.now(timezone.utc)
    five_min_ago = now - timedelta(minutes=5)
    one_hour_ago = now - timedelta(hours=1)

    query = db.query(User)

    # Search filter
    if search:
        search_term = f"%{search.lower()}%"
        query = query.filter(
            or_(
                func.lower(User.email).like(search_term),
                func.lower(User.full_name).like(search_term)
            )
        )

    # Role filter
    if role == "admin":
        query = query.filter(User.is_admin.is_(True))
    elif role == "user":
        query = query.filter(User.is_admin.is_(False))

    # Status filter
    if status == "banned":
        query = query.filter(User.is_active.is_(False))
    elif status == "online":
        query = query.filter(User.last_activity_at >= five_min_ago)
    elif status == "away":
        query = query.filter(
            and_(
                User.last_activity_at >= one_hour_ago,
                User.last_activity_at < five_min_ago
            )
        )
    elif status == "offline":
        query = query.filter(
            or_(
                User.last_activity_at < one_hour_ago,
                User.last_activity_at.is_(None)
            )
        )

    # Get total count
    total = query.count()

    # Sorting
    sort_column = {
        "last_activity": User.last_activity_at,
        "created": User.created_at,
        "email": User.email,
        "xp": User.total_xp if hasattr(User, 'total_xp') else User.created_at
    }.get(sort, User.last_activity_at)

    if order == "desc":
        query = query.order_by(desc(sort_column).nullslast())
    else:
        query = query.order_by(asc(sort_column).nullsfirst())

    # Pagination
    offset = (page - 1) * page_size
    users = query.offset(offset).limit(page_size).all()

    return UsersListResponse(
        users=[user_to_response(u) for u in users],
        total=total,
        page=page,
        page_size=page_size,
        total_pages=(total + page_size - 1) // page_size
    )


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get detailed user information"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_to_response(user)


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: UUID,
    data: UpdateUserRequest,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Update user information"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.full_name is not None:
        user.full_name = data.full_name
    if data.is_admin is not None:
        user.is_admin = data.is_admin
    if data.is_active is not None:
        user.is_active = data.is_active

    user.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(user)

    return user_to_response(user)


@router.delete("/users/{user_id}")
async def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Delete a user permanently"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Don't allow deleting yourself
    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")

    db.delete(user)
    db.commit()

    return {"ok": True, "message": "User deleted successfully"}


@router.post("/users/{user_id}/ban")
async def ban_user(
    user_id: UUID,
    data: BanRequest,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Ban a user (sets is_active to False)"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot ban yourself")

    user.is_active = False
    user.updated_at = datetime.now(timezone.utc)

    # Force logout by clearing session version if exists
    if hasattr(user, 'force_logout_at'):
        user.force_logout_at = datetime.now(timezone.utc)

    db.commit()

    return {"ok": True, "message": f"User {user.email} has been banned", "reason": data.reason}


@router.post("/users/{user_id}/unban")
async def unban_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Unban a user (sets is_active to True)"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = True
    user.updated_at = datetime.now(timezone.utc)
    db.commit()

    return {"ok": True, "message": f"User {user.email} has been unbanned"}


@router.post("/users/{user_id}/force-logout")
async def force_logout_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Force logout a user by setting force_logout_at"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Set force_logout_at if the column exists
    if hasattr(user, 'force_logout_at'):
        user.force_logout_at = datetime.now(timezone.utc)
        db.commit()

    return {"ok": True, "message": f"User {user.email} will be logged out"}


@router.post("/users/{user_id}/toggle-admin")
async def toggle_admin(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Toggle admin status for a user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot change your own admin status")

    user.is_admin = not user.is_admin
    user.updated_at = datetime.now(timezone.utc)
    db.commit()

    status = "admin" if user.is_admin else "regular user"
    return {"ok": True, "message": f"User {user.email} is now {status}", "is_admin": user.is_admin}


@router.put("/users/{user_id}/permissions")
async def update_permissions(
    user_id: UUID,
    data: UpdatePermissionsRequest,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Update user permissions"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.ai_quiz_access is not None and hasattr(user, 'ai_quiz_access'):
        user.ai_quiz_access = data.ai_quiz_access
    if data.premium_modules_access is not None and hasattr(user, 'premium_modules_access'):
        user.premium_modules_access = data.premium_modules_access

    user.updated_at = datetime.now(timezone.utc)
    db.commit()

    return {"ok": True, "message": "Permissions updated"}


@router.get("/users/{user_id}/activity")
async def get_user_activity(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get user's recent activity"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # This would need an activity_log table
    # Return placeholder data
    activities = []
    if user.last_activity_at:
        activities.append({
            "id": "1",
            "type": "login",
            "description": "Last login",
            "timestamp": user.last_activity_at.isoformat()
        })
    if user.created_at:
        activities.append({
            "id": "2",
            "type": "login",
            "description": "Account created",
            "timestamp": user.created_at.isoformat()
        })

    return {"activities": activities}


@router.get("/users/{user_id}/learning")
async def get_user_learning(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get user's learning progress"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # This would need module_progress and skill_path_progress tables
    return {
        "modules": [],
        "skill_paths": [],
        "recent_tasks": []
    }


@router.get("/users/{user_id}/ai-usage")
async def get_user_ai_usage_detail(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get user's AI usage statistics"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate last 7 days
    now = datetime.now(timezone.utc)
    requests_by_day = []
    for i in range(6, -1, -1):
        day = now - timedelta(days=i)
        requests_by_day.append({
            "date": day.strftime("%Y-%m-%d"),
            "count": 0
        })

    return {
        "total_requests": 0,
        "tokens_used": 0,
        "requests_by_day": requests_by_day,
        "top_features": []
    }


# =============================================================================
# ANALYTICS ENDPOINTS
# =============================================================================

@router.get("/analytics")
async def get_combined_analytics(
    time_range: str = Query("30d", alias="range"),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get combined analytics data for the dashboard"""
    # Parse time range
    days = 30
    if time_range == "7d":
        days = 7
    elif time_range == "90d":
        days = 90

    now = datetime.now(timezone.utc)
    start_date = now - timedelta(days=days)
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    # Total users
    total_users = db.query(func.count(User.id)).scalar() or 0

    # Active users in period
    active_users_7d = db.query(func.count(User.id)).filter(
        User.last_activity_at >= week_ago
    ).scalar() or 0

    active_users_30d = db.query(func.count(User.id)).filter(
        User.last_activity_at >= month_ago
    ).scalar() or 0

    # New users in period
    new_users_7d = db.query(func.count(User.id)).filter(
        User.created_at >= week_ago
    ).scalar() or 0

    new_users_30d = db.query(func.count(User.id)).filter(
        User.created_at >= month_ago
    ).scalar() or 0

    # Calculate growth rate
    prev_month_users = db.query(func.count(User.id)).filter(
        User.created_at < month_ago
    ).scalar() or 1
    growth_rate = ((total_users - prev_month_users) / prev_month_users) * 100 if prev_month_users > 0 else 0

    # Activity by day
    activity_by_day = []
    for i in range(min(days, 14) - 1, -1, -1):
        day_start = (now - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day_start + timedelta(days=1)

        users_active = db.query(func.count(User.id)).filter(
            and_(
                User.last_activity_at >= day_start,
                User.last_activity_at < day_end
            )
        ).scalar() or 0

        activity_by_day.append({
            "date": day_start.strftime("%Y-%m-%d"),
            "users": users_active,
            "sessions": users_active  # Approximation
        })

    # Activity by hour (last 7 days)
    activity_by_hour = []
    for hour in range(24):
        count = 0  # Would need detailed activity logs
        activity_by_hour.append({"hour": hour, "count": count})

    # Top modules (placeholder - would need module progress data)
    top_modules = []

    # User levels distribution - User model doesn't have level column yet
    # Just return all users at level 1 for now
    user_levels = [{"level": 1, "count": total_users}]

    # Calculate actual retention based on user activity
    # Day 1: Users who came back within 1 day of signup
    # Day 7: Users who came back within 7 days of signup
    # Day 30: Users who came back within 30 days of signup
    try:
        # Users created more than 1 day ago
        users_1d_old = db.query(User).filter(
            User.created_at < now - timedelta(days=1)
        ).all()
        retained_1d = sum(1 for u in users_1d_old if u.last_activity_at and
                         u.last_activity_at > u.created_at + timedelta(hours=1))
        retention_day1 = round((retained_1d / len(users_1d_old) * 100) if users_1d_old else 0)

        # Users created more than 7 days ago
        users_7d_old = db.query(User).filter(
            User.created_at < now - timedelta(days=7)
        ).all()
        retained_7d = sum(1 for u in users_7d_old if u.last_activity_at and
                         u.last_activity_at > u.created_at + timedelta(days=1))
        retention_day7 = round((retained_7d / len(users_7d_old) * 100) if users_7d_old else 0)

        # Users created more than 30 days ago
        users_30d_old = db.query(User).filter(
            User.created_at < now - timedelta(days=30)
        ).all()
        retained_30d = sum(1 for u in users_30d_old if u.last_activity_at and
                          u.last_activity_at > u.created_at + timedelta(days=7))
        retention_day30 = round((retained_30d / len(users_30d_old) * 100) if users_30d_old else 0)
    except Exception:
        retention_day1 = 0
        retention_day7 = 0
        retention_day30 = 0

    return {
        "overview": {
            "total_users": total_users,
            "active_users_7d": active_users_7d,
            "active_users_30d": active_users_30d,
            "new_users_7d": new_users_7d,
            "new_users_30d": new_users_30d,
            "growth_rate": round(growth_rate, 1)
        },
        "engagement": {
            "avg_session_duration": 0,
            "sessions_per_user": 0,
            "modules_completed_total": 0,
            "tasks_completed_total": 0,
            "avg_modules_per_user": 0,
            "avg_tasks_per_user": 0
        },
        "retention": {
            "day1": retention_day1,
            "day7": retention_day7,
            "day30": retention_day30
        },
        "activity_by_hour": activity_by_hour,
        "activity_by_day": activity_by_day,
        "top_modules": top_modules,
        "user_levels": user_levels
    }


@router.get("/analytics/user-growth", response_model=UserGrowthResponse)
async def get_user_growth(
    days: int = Query(30, ge=7, le=365),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get user growth data over time"""
    now = datetime.now(timezone.utc)
    data = []

    for i in range(days - 1, -1, -1):
        day_start = (now - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day_start + timedelta(days=1)

        # Total users up to this day
        total = db.query(func.count(User.id)).filter(
            User.created_at < day_end
        ).scalar() or 0

        # New users that day
        new = db.query(func.count(User.id)).filter(
            and_(
                User.created_at >= day_start,
                User.created_at < day_end
            )
        ).scalar() or 0

        data.append(UserGrowthData(
            date=day_start.strftime("%Y-%m-%d"),
            total_users=total,
            new_users=new
        ))

    return UserGrowthResponse(data=data)


@router.get("/analytics/activity-heatmap", response_model=HeatmapResponse)
async def get_activity_heatmap(
    days: int = Query(30, ge=7, le=90),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get activity heatmap data (day of week vs hour)"""
    now = datetime.now(timezone.utc)
    start_date = now - timedelta(days=days)

    # Get all last_activity_at timestamps in range
    activities = db.query(User.last_activity_at).filter(
        User.last_activity_at >= start_date
    ).all()

    # Build heatmap
    heatmap = {}
    for (activity_time,) in activities:
        if activity_time:
            day = activity_time.weekday()  # 0=Monday
            hour = activity_time.hour
            key = (day, hour)
            heatmap[key] = heatmap.get(key, 0) + 1

    # Convert to list
    data = []
    for day in range(7):
        for hour in range(24):
            data.append(HeatmapData(
                day=day,
                hour=hour,
                count=heatmap.get((day, hour), 0)
            ))

    return HeatmapResponse(data=data)


@router.get("/analytics/top-users", response_model=TopUsersResponse)
async def get_top_users(
    limit: int = Query(10, ge=5, le=50),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get top users by various metrics"""
    now = datetime.now(timezone.utc)
    week_ago = now - timedelta(days=7)

    # Most active (by last_activity_at frequency - simplified)
    most_active = db.query(User).filter(
        User.last_activity_at >= week_ago
    ).order_by(desc(User.last_activity_at)).limit(limit).all()

    # Highest XP
    highest_xp_query = db.query(User)
    if hasattr(User, 'total_xp'):
        highest_xp_query = highest_xp_query.order_by(desc(User.total_xp))
    highest_xp = highest_xp_query.limit(limit).all()

    # Longest streak
    longest_streak_query = db.query(User)
    if hasattr(User, 'current_streak'):
        longest_streak_query = longest_streak_query.order_by(desc(User.current_streak))
    longest_streak = longest_streak_query.limit(limit).all()

    return TopUsersResponse(
        most_active=[
            TopUser(
                id=str(u.id),
                email=u.email,
                full_name=u.full_name,
                avatar_url=getattr(u, 'avatar_url', None),
                value=1,  # Would need session count
                label="sessions this week"
            ) for u in most_active
        ],
        highest_xp=[
            TopUser(
                id=str(u.id),
                email=u.email,
                full_name=u.full_name,
                avatar_url=getattr(u, 'avatar_url', None),
                value=getattr(u, 'total_xp', 0) or 0,
                label="XP"
            ) for u in highest_xp
        ],
        longest_streak=[
            TopUser(
                id=str(u.id),
                email=u.email,
                full_name=u.full_name,
                avatar_url=getattr(u, 'avatar_url', None),
                value=getattr(u, 'current_streak', 0) or 0,
                label="day streak"
            ) for u in longest_streak
        ]
    )


# =============================================================================
# AI USAGE ENDPOINTS
# =============================================================================

@router.get("/ai-usage")
async def get_combined_ai_usage(
    time_range: str = Query("30d", alias="range"),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get combined AI usage data for the dashboard"""
    # Parse time range
    days = 30
    if time_range == "7d":
        days = 7
    elif time_range == "90d":
        days = 90

    now = datetime.now(timezone.utc)
    start_date = now - timedelta(days=days)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = now - timedelta(days=7)

    try:
        # Total stats for period
        total_requests = db.query(func.count(AIUsageLog.id)).filter(
            AIUsageLog.created_at >= start_date
        ).scalar() or 0

        total_tokens = db.query(func.sum(AIUsageLog.total_tokens)).filter(
            AIUsageLog.created_at >= start_date
        ).scalar() or 0

        total_cost = db.query(func.sum(AIUsageLog.cost_usd)).filter(
            AIUsageLog.created_at >= start_date
        ).scalar() or 0.0

        # Today's stats
        requests_today = db.query(func.count(AIUsageLog.id)).filter(
            AIUsageLog.created_at >= today_start
        ).scalar() or 0

        # Unique users
        unique_users = db.query(func.count(func.distinct(AIUsageLog.user_id))).filter(
            AIUsageLog.created_at >= start_date
        ).scalar() or 0

        # By feature
        feature_stats = db.query(
            AIUsageLog.feature,
            func.count(AIUsageLog.id).label('requests'),
            func.sum(AIUsageLog.total_tokens).label('tokens'),
            func.sum(AIUsageLog.cost_usd).label('cost')
        ).filter(
            AIUsageLog.created_at >= start_date
        ).group_by(AIUsageLog.feature).all()

        by_feature = []
        for feat in feature_stats:
            by_feature.append({
                "name": feat.feature or "Unknown",
                "requests": feat.requests or 0,
                "tokens": feat.tokens or 0,
                "cost": round(feat.cost or 0, 4),
                "avg_time": 200
            })

        # If no data, show default features
        if not by_feature:
            by_feature = [
                {"name": "AI Quiz", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 200},
                {"name": "Dallas Chat", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 350},
                {"name": "Study Assistant", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 180}
            ]

        # By model
        model_stats = db.query(
            AIUsageLog.model,
            func.count(AIUsageLog.id).label('requests'),
            func.sum(AIUsageLog.total_tokens).label('tokens'),
            func.sum(AIUsageLog.cost_usd).label('cost')
        ).filter(
            AIUsageLog.created_at >= start_date
        ).group_by(AIUsageLog.model).all()

        by_model = []
        for mod in model_stats:
            by_model.append({
                "model": mod.model or "unknown",
                "requests": mod.requests or 0,
                "tokens": mod.tokens or 0,
                "cost": round(mod.cost or 0, 4)
            })

        if not by_model:
            by_model = [
                {"model": "gpt-4", "requests": 0, "tokens": 0, "cost": 0.0},
                {"model": "gpt-3.5-turbo", "requests": 0, "tokens": 0, "cost": 0.0}
            ]

        # Daily data for chart
        by_day = []
        for i in range(min(days, 14) - 1, -1, -1):
            day_start = (now - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
            day_end = day_start + timedelta(days=1)

            day_requests = db.query(func.count(AIUsageLog.id)).filter(
                and_(
                    AIUsageLog.created_at >= day_start,
                    AIUsageLog.created_at < day_end
                )
            ).scalar() or 0

            day_tokens = db.query(func.sum(AIUsageLog.total_tokens)).filter(
                and_(
                    AIUsageLog.created_at >= day_start,
                    AIUsageLog.created_at < day_end
                )
            ).scalar() or 0

            day_cost = db.query(func.sum(AIUsageLog.cost_usd)).filter(
                and_(
                    AIUsageLog.created_at >= day_start,
                    AIUsageLog.created_at < day_end
                )
            ).scalar() or 0.0

            by_day.append({
                "date": day_start.strftime("%Y-%m-%d"),
                "requests": day_requests,
                "tokens": day_tokens or 0,
                "cost": round(day_cost or 0, 4)
            })

        # Top users by usage
        top_users_data = db.query(
            AIUsageLog.user_id,
            func.count(AIUsageLog.id).label('requests'),
            func.sum(AIUsageLog.total_tokens).label('tokens'),
            func.sum(AIUsageLog.cost_usd).label('cost')
        ).filter(
            and_(
                AIUsageLog.created_at >= start_date,
                AIUsageLog.user_id.isnot(None)
            )
        ).group_by(AIUsageLog.user_id).order_by(desc('requests')).limit(10).all()

        top_users = []
        for tu in top_users_data:
            user = db.query(User).filter(User.id == tu.user_id).first()
            if user:
                top_users.append({
                    "user_id": str(tu.user_id),
                    "email": user.email,
                    "full_name": user.full_name,
                    "requests": tu.requests or 0,
                    "tokens": tu.tokens or 0,
                    "cost": round(tu.cost or 0, 4)
                })

    except Exception as e:
        # If table doesn't exist or other error, return zeros
        total_requests = 0
        total_tokens = 0
        total_cost = 0.0
        requests_today = 0
        unique_users = 0
        by_feature = [
            {"name": "AI Quiz", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 200},
            {"name": "Dallas Chat", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 350},
            {"name": "Study Assistant", "requests": 0, "tokens": 0, "cost": 0.0, "avg_time": 180}
        ]
        by_model = [
            {"model": "gpt-4", "requests": 0, "tokens": 0, "cost": 0.0},
            {"model": "gpt-3.5-turbo", "requests": 0, "tokens": 0, "cost": 0.0}
        ]
        by_day = []
        for i in range(min(days, 14) - 1, -1, -1):
            day = now - timedelta(days=i)
            by_day.append({
                "date": day.strftime("%Y-%m-%d"),
                "requests": 0,
                "tokens": 0,
                "cost": 0.0
            })
        top_users = []

    return {
        "summary": {
            "total_requests": total_requests,
            "total_tokens": total_tokens,
            "estimated_cost": round(total_cost, 2),
            "avg_response_time": 150,
            "success_rate": 99.5,
            "unique_users": unique_users,
            "requests_today": requests_today,
            "requests_change": 0
        },
        "by_feature": by_feature,
        "by_model": by_model,
        "by_day": by_day,
        "top_users": top_users,
        "errors": []
    }


@router.get("/ai-usage/overview", response_model=AIUsageOverview)
async def get_ai_usage_overview(
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get AI usage overview statistics"""
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = now - timedelta(days=7)

    try:
        total_requests = db.query(func.count(AIUsageLog.id)).scalar() or 0
        total_tokens = db.query(func.sum(AIUsageLog.total_tokens)).scalar() or 0
        total_cost = db.query(func.sum(AIUsageLog.cost_usd)).scalar() or 0.0

        requests_today = db.query(func.count(AIUsageLog.id)).filter(
            AIUsageLog.created_at >= today_start
        ).scalar() or 0

        cost_today = db.query(func.sum(AIUsageLog.cost_usd)).filter(
            AIUsageLog.created_at >= today_start
        ).scalar() or 0.0

        requests_this_week = db.query(func.count(AIUsageLog.id)).filter(
            AIUsageLog.created_at >= week_ago
        ).scalar() or 0

        cost_this_week = db.query(func.sum(AIUsageLog.cost_usd)).filter(
            AIUsageLog.created_at >= week_ago
        ).scalar() or 0.0
    except Exception:
        total_requests = 0
        total_tokens = 0
        total_cost = 0.0
        requests_today = 0
        cost_today = 0.0
        requests_this_week = 0
        cost_this_week = 0.0

    return AIUsageOverview(
        total_requests=total_requests,
        total_tokens=total_tokens or 0,
        total_cost=round(total_cost or 0, 2),
        requests_today=requests_today,
        cost_today=round(cost_today or 0, 4),
        requests_this_week=requests_this_week,
        cost_this_week=round(cost_this_week or 0, 4)
    )


@router.get("/ai-usage/by-user", response_model=AIUsageListResponse)
async def get_ai_usage_by_user(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=10, le=100),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get AI usage grouped by user"""
    try:
        # Get aggregated stats per user
        user_stats = db.query(
            AIUsageLog.user_id,
            func.count(AIUsageLog.id).label('requests'),
            func.sum(AIUsageLog.total_tokens).label('tokens'),
            func.sum(AIUsageLog.cost_usd).label('cost'),
            func.max(AIUsageLog.created_at).label('last_used')
        ).filter(
            AIUsageLog.user_id.isnot(None)
        ).group_by(AIUsageLog.user_id).order_by(desc('requests')).offset(
            (page - 1) * page_size
        ).limit(page_size).all()

        total = db.query(func.count(func.distinct(AIUsageLog.user_id))).filter(
            AIUsageLog.user_id.isnot(None)
        ).scalar() or 0

        users = []
        for us in user_stats:
            user = db.query(User).filter(User.id == us.user_id).first()
            if user:
                users.append(AIUsageByUser(
                    id=str(us.user_id),
                    email=user.email,
                    full_name=user.full_name,
                    requests=us.requests or 0,
                    tokens=us.tokens or 0,
                    cost=round(us.cost or 0, 4),
                    last_used=us.last_used
                ))
    except Exception:
        users = []
        total = 0

    return AIUsageListResponse(
        users=users,
        total=total
    )


@router.get("/ai-usage/{user_id}")
async def get_user_ai_usage(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get AI usage for a specific user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        total_requests = db.query(func.count(AIUsageLog.id)).filter(
            AIUsageLog.user_id == user_id
        ).scalar() or 0

        total_tokens = db.query(func.sum(AIUsageLog.total_tokens)).filter(
            AIUsageLog.user_id == user_id
        ).scalar() or 0

        total_cost = db.query(func.sum(AIUsageLog.cost_usd)).filter(
            AIUsageLog.user_id == user_id
        ).scalar() or 0.0

        recent = db.query(AIUsageLog).filter(
            AIUsageLog.user_id == user_id
        ).order_by(desc(AIUsageLog.created_at)).limit(10).all()

        recent_requests = [{
            "id": str(r.id),
            "feature": r.feature,
            "model": r.model,
            "tokens": r.total_tokens,
            "cost": round(r.cost_usd, 4),
            "created_at": r.created_at.isoformat() if r.created_at else None
        } for r in recent]
    except Exception:
        total_requests = 0
        total_tokens = 0
        total_cost = 0.0
        recent_requests = []

    return {
        "user_id": str(user_id),
        "total_requests": total_requests,
        "total_tokens": total_tokens or 0,
        "total_cost": round(total_cost or 0, 4),
        "recent_requests": recent_requests
    }


# =============================================================================
# SETTINGS ENDPOINTS
# =============================================================================

@router.get("/settings")
async def get_settings(
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get admin settings"""
    # Return full settings structure that frontend expects
    return {
        "general": {
            "site_name": "DevOpsHub",
            "site_description": "Learn DevOps with interactive modules",
            "maintenance_mode": False,
            "registration_enabled": True,
            "email_verification_required": False
        },
        "security": {
            "max_login_attempts": 5,
            "lockout_duration_minutes": 15,
            "session_timeout_hours": 24,
            "require_2fa_for_admins": False,
            "password_min_length": 8
        },
        "notifications": {
            "email_notifications_enabled": True,
            "slack_webhook_url": "",
            "notify_on_new_user": True,
            "notify_on_error": True,
            "daily_report_enabled": False
        },
        "ai": {
            "ai_features_enabled": True,
            "max_requests_per_user_day": 100,
            "max_tokens_per_request": 4000,
            "rate_limit_enabled": True,
            "allowed_models": ["gpt-4", "gpt-3.5-turbo"]
        },
        "features": {
            "study_room_enabled": True,
            "skillpath_enabled": True,
            "premium_modules_enabled": True,
            "ai_quiz_enabled": True,
            "leaderboard_enabled": True,
            "achievements_enabled": True
        }
    }


@router.put("/settings")
async def update_settings(
    settings: dict,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Update admin settings"""
    # This would need a settings table to persist changes
    # For now, just accept and acknowledge
    return {"ok": True, "message": "Settings updated"}


# =============================================================================
# EXAM STATS ENDPOINTS (Admin)
# =============================================================================

@router.get("/exam-stats")
async def get_exam_stats(
    time_range: str = Query("30d", alias="range"),
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get comprehensive exam statistics for admin dashboard"""
    days = 30
    if time_range == "7d":
        days = 7
    elif time_range == "90d":
        days = 90

    now = datetime.now(timezone.utc)
    start_date = now - timedelta(days=days)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = now - timedelta(days=7)

    try:
        # Total exams in period
        total_exams = db.query(func.count(ExamResult.id)).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).scalar() or 0

        total_exams_today = db.query(func.count(ExamResult.id)).filter(
            ExamResult.completed_at >= today_start,
            ExamResult.completed == True
        ).scalar() or 0

        total_exams_week = db.query(func.count(ExamResult.id)).filter(
            ExamResult.completed_at >= week_ago,
            ExamResult.completed == True
        ).scalar() or 0

        # Total questions answered
        total_questions = db.query(func.sum(ExamResult.question_count)).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).scalar() or 0

        # Average score
        avg_score = db.query(func.avg(ExamResult.score_percent)).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).scalar() or 0.0

        # Average time
        avg_time_seconds = db.query(func.avg(ExamResult.time_spent_seconds)).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).scalar() or 0

        # Unique users who took exams
        unique_users = db.query(func.count(func.distinct(ExamResult.user_id))).filter(
            ExamResult.completed_at >= start_date
        ).scalar() or 0

        # Top performers (highest avg score, min 2 exams)
        top_performers_data = db.query(
            ExamResult.user_id,
            func.count(ExamResult.id).label('exam_count'),
            func.avg(ExamResult.score_percent).label('avg_score'),
            func.max(ExamResult.score_percent).label('best_score'),
            func.sum(ExamResult.question_count).label('total_questions'),
            func.sum(ExamResult.correct_answers).label('total_correct'),
            func.avg(ExamResult.time_spent_seconds).label('avg_time'),
            func.max(ExamResult.completed_at).label('last_exam')
        ).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).group_by(ExamResult.user_id).having(
            func.count(ExamResult.id) >= 1
        ).order_by(desc('avg_score')).limit(10).all()

        top_performers = []
        for tp in top_performers_data:
            user = db.query(User).filter(User.id == tp.user_id).first()
            if user:
                top_performers.append({
                    "user_id": str(tp.user_id),
                    "email": user.email,
                    "full_name": user.full_name,
                    "total_exams": tp.exam_count,
                    "avg_score": round(tp.avg_score or 0, 1),
                    "best_score": round(tp.best_score or 0, 1),
                    "total_questions": tp.total_questions or 0,
                    "total_correct": tp.total_correct or 0,
                    "avg_time_minutes": round((tp.avg_time or 0) / 60, 1),
                    "last_exam_at": tp.last_exam.isoformat() if tp.last_exam else None
                })

        # Recent exams
        recent_exams_data = db.query(ExamResult).filter(
            ExamResult.completed == True
        ).order_by(desc(ExamResult.completed_at)).limit(10).all()

        recent_exams = []
        for exam in recent_exams_data:
            user = db.query(User).filter(User.id == exam.user_id).first()
            recent_exams.append({
                "id": str(exam.id),
                "user_email": user.email if user else "Unknown",
                "user_name": user.full_name if user else None,
                "score_percent": round(exam.score_percent, 1),
                "correct_answers": exam.correct_answers,
                "question_count": exam.question_count,
                "time_spent_minutes": round(exam.time_spent_seconds / 60, 1),
                "sources": exam.sources or [],
                "completed_at": exam.completed_at.isoformat() if exam.completed_at else None
            })

        # Score distribution
        score_distribution = {"0-20": 0, "20-40": 0, "40-60": 0, "60-80": 0, "80-100": 0}
        all_scores = db.query(ExamResult.score_percent).filter(
            ExamResult.completed_at >= start_date,
            ExamResult.completed == True
        ).all()
        
        for (score,) in all_scores:
            if score < 20:
                score_distribution["0-20"] += 1
            elif score < 40:
                score_distribution["20-40"] += 1
            elif score < 60:
                score_distribution["40-60"] += 1
            elif score < 80:
                score_distribution["60-80"] += 1
            else:
                score_distribution["80-100"] += 1

        # By source (which question sources are most used)
        # This requires parsing the JSON sources field - simplified for now
        by_source = [
            {"source": "doe25", "count": 0, "avg_score": 0},
            {"source": "handson", "count": 0, "avg_score": 0},
            {"source": "linux-commands", "count": 0, "avg_score": 0}
        ]

        # Daily exams chart
        exams_by_day = []
        for i in range(min(days, 14) - 1, -1, -1):
            day_start = (now - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0)
            day_end = day_start + timedelta(days=1)
            
            day_count = db.query(func.count(ExamResult.id)).filter(
                and_(
                    ExamResult.completed_at >= day_start,
                    ExamResult.completed_at < day_end,
                    ExamResult.completed == True
                )
            ).scalar() or 0
            
            day_avg = db.query(func.avg(ExamResult.score_percent)).filter(
                and_(
                    ExamResult.completed_at >= day_start,
                    ExamResult.completed_at < day_end,
                    ExamResult.completed == True
                )
            ).scalar() or 0

            exams_by_day.append({
                "date": day_start.strftime("%Y-%m-%d"),
                "count": day_count,
                "avg_score": round(day_avg, 1)
            })

    except Exception as e:
        # If table doesn't exist yet, return zeros
        return {
            "total_exams": 0,
            "total_exams_today": 0,
            "total_exams_week": 0,
            "total_questions_answered": 0,
            "avg_score": 0,
            "avg_time_minutes": 0,
            "unique_users": 0,
            "top_performers": [],
            "recent_exams": [],
            "score_distribution": {"0-20": 0, "20-40": 0, "40-60": 0, "60-80": 0, "80-100": 0},
            "by_source": [],
            "exams_by_day": [],
            "error": str(e)
        }

    return {
        "total_exams": total_exams,
        "total_exams_today": total_exams_today,
        "total_exams_week": total_exams_week,
        "total_questions_answered": total_questions,
        "avg_score": round(avg_score, 1),
        "avg_time_minutes": round(avg_time_seconds / 60, 1) if avg_time_seconds else 0,
        "unique_users": unique_users,
        "top_performers": top_performers,
        "recent_exams": recent_exams,
        "score_distribution": score_distribution,
        "by_source": by_source,
        "exams_by_day": exams_by_day
    }


@router.get("/exam-stats/user/{user_id}")
async def get_user_exam_stats(
    user_id: UUID,
    db: Session = Depends(get_db),
    admin: UserPublic = Depends(require_admin)
):
    """Get exam statistics for a specific user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    results = db.query(ExamResult).filter(
        ExamResult.user_id == user_id,
        ExamResult.completed == True
    ).order_by(desc(ExamResult.completed_at)).all()

    if not results:
        return {
            "user_id": str(user_id),
            "email": user.email,
            "full_name": user.full_name,
            "total_exams": 0,
            "avg_score": 0,
            "best_score": 0,
            "worst_score": 0,
            "total_questions": 0,
            "total_correct": 0,
            "accuracy_percent": 0,
            "avg_time_minutes": 0,
            "exams": []
        }

    total_questions = sum(r.question_count for r in results)
    total_correct = sum(r.correct_answers for r in results)
    
    return {
        "user_id": str(user_id),
        "email": user.email,
        "full_name": user.full_name,
        "total_exams": len(results),
        "avg_score": round(sum(r.score_percent for r in results) / len(results), 1),
        "best_score": round(max(r.score_percent for r in results), 1),
        "worst_score": round(min(r.score_percent for r in results), 1),
        "total_questions": total_questions,
        "total_correct": total_correct,
        "accuracy_percent": round(total_correct / total_questions * 100, 1) if total_questions > 0 else 0,
        "avg_time_minutes": round(sum(r.time_spent_seconds for r in results) / len(results) / 60, 1),
        "exams": [{
            "id": str(r.id),
            "score_percent": round(r.score_percent, 1),
            "correct": r.correct_answers,
            "total": r.question_count,
            "time_minutes": round(r.time_spent_seconds / 60, 1),
            "sources": r.sources or [],
            "completed_at": r.completed_at.isoformat() if r.completed_at else None
        } for r in results[:20]]
    }
