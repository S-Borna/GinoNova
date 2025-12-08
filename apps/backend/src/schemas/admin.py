"""
Admin Schemas - Phase 10
Pydantic models for admin API responses
"""
from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


# ==============================================================================
# USER MANAGEMENT SCHEMAS
# ==============================================================================

class AdminUserSummary(BaseModel):
    """Compact user info for admin lists"""
    id: UUID
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime

    class Config:
        from_attributes = True


class AdminUserDetail(BaseModel):
    """Detailed user info for admin view"""
    id: UUID
    email: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

    # Status
    is_active: bool = True
    is_admin: bool = False
    is_verified: bool = False

    # Stats
    total_xp: int = 0
    level: int = 1
    current_streak: int = 0
    longest_streak: int = 0

    # Progress
    tasks_completed: int = 0
    modules_completed: int = 0
    labs_completed: int = 0
    projects_completed: int = 0
    total_study_time: int = 0

    # Timestamps
    created_at: datetime
    updated_at: datetime
    last_activity_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AdminUserUpdate(BaseModel):
    """Schema for admin to update user"""
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    is_verified: Optional[bool] = None
    total_xp: Optional[int] = None


class AdminUsersListResponse(BaseModel):
    """Paginated user list response"""
    users: List[AdminUserDetail]
    total: int
    page: int = 1
    per_page: int = 20
    total_pages: int = 1


# ==============================================================================
# SYSTEM STATS SCHEMAS
# ==============================================================================

class SystemStats(BaseModel):
    """System-wide statistics"""
    # Users
    total_users: int = 0
    active_users: int = 0
    admin_users: int = 0
    users_today: int = 0
    users_this_week: int = 0
    
    # Real-time activity
    online_now: int = 0  # Users active in last 30 min
    active_today: int = 0  # Users active today

    # Content
    total_tracks: int = 0
    total_modules: int = 0
    total_tasks: int = 0
    total_labs: int = 0
    total_projects: int = 0

    # Activity
    total_tasks_completed: int = 0
    total_xp_earned: int = 0
    total_study_minutes: int = 0
    active_sessions: int = 0

    # Averages
    avg_tasks_per_user: float = 0.0
    avg_xp_per_user: float = 0.0
    avg_session_minutes: float = 0.0

    # Health
    database_status: str = "unknown"
    cache_status: str = "unknown"
    api_version: str = "1.0.0"


class DailyStats(BaseModel):
    """Daily statistics snapshot"""
    date: datetime
    new_users: int = 0
    active_users: int = 0
    tasks_completed: int = 0
    xp_earned: int = 0
    study_minutes: int = 0
    sessions_completed: int = 0


class StatsResponse(BaseModel):
    """Full stats response"""
    current: SystemStats
    daily: List[DailyStats] = []


# ==============================================================================
# SYSTEM LOGS SCHEMAS
# ==============================================================================

class SystemLogEntry(BaseModel):
    """System log entry"""
    id: str
    timestamp: datetime
    level: str  # info, warning, error
    source: str  # api, auth, database, etc.
    message: str
    details: Optional[dict] = None
    user_id: Optional[UUID] = None


class SystemLogsResponse(BaseModel):
    """System logs response"""
    logs: List[SystemLogEntry]
    total: int
    page: int = 1
    per_page: int = 50
    has_more: bool = False


# ==============================================================================
# CONTENT MANAGEMENT SCHEMAS
# ==============================================================================

class ContentSummary(BaseModel):
    """Content summary for admin dashboard"""
    tracks: int = 0
    modules: int = 0
    tasks: int = 0
    labs: int = 0
    projects: int = 0
    total_hours: float = 0.0

    # Status
    is_seeded: bool = False
    last_seed_at: Optional[datetime] = None


class ContentHealthCheck(BaseModel):
    """Content health check"""
    status: str  # healthy, warning, error
    tracks_ok: bool = True
    modules_ok: bool = True
    orphaned_tasks: int = 0
    orphaned_labs: int = 0
    missing_content: List[str] = []


# ==============================================================================
# ADMIN ACTIVITY SCHEMAS
# ==============================================================================

class AdminAction(BaseModel):
    """Admin action log entry"""
    id: str
    admin_id: UUID
    admin_email: str
    action: str  # user_update, content_seed, data_clear, etc.
    target_type: Optional[str] = None  # user, module, task, etc.
    target_id: Optional[UUID] = None
    details: Optional[dict] = None
    timestamp: datetime


class AdminActionsResponse(BaseModel):
    """Admin actions log response"""
    actions: List[AdminAction]
    total: int
    page: int = 1
    per_page: int = 50
