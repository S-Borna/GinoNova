"""
User Profile Schemas - Phase 9
"""
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class UserProfileBase(BaseModel):
    """Base profile fields"""
    full_name: Optional[str] = Field(None, max_length=255)
    avatar_url: Optional[str] = Field(None, max_length=500)
    bio: Optional[str] = Field(None, max_length=1000)
    github_username: Optional[str] = Field(None, max_length=100)
    linkedin_url: Optional[str] = Field(None, max_length=255)
    website_url: Optional[str] = Field(None, max_length=255)
    timezone: Optional[str] = Field("UTC", max_length=50)


class UserProfileUpdate(UserProfileBase):
    """Schema for updating user profile"""
    pass


class UserProfilePublic(UserProfileBase):
    """Public profile response"""
    id: UUID
    email: str
    is_active: bool
    is_verified: bool

    # Stats
    total_xp: int = 0
    current_streak: int = 0
    longest_streak: int = 0
    level: int = 1

    # Computed
    tasks_completed: int = 0
    modules_completed: int = 0
    total_study_time: int = 0  # minutes

    created_at: datetime
    last_activity_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserStatsPublic(BaseModel):
    """User statistics response"""
    user_id: UUID

    # XP & Level
    total_xp: int = 0
    level: int = 1
    xp_to_next_level: int = 100
    level_progress_percent: int = 0

    # Streaks
    current_streak: int = 0
    longest_streak: int = 0
    streak_active: bool = False

    # Progress
    tasks_completed: int = 0
    tasks_total: int = 0
    modules_completed: int = 0
    modules_total: int = 0
    labs_completed: int = 0
    projects_completed: int = 0

    # Time
    total_study_time: int = 0  # minutes
    sessions_completed: int = 0
    avg_session_length: int = 0  # minutes

    # Activity
    last_activity_at: Optional[datetime] = None
    days_since_joined: int = 0

    class Config:
        from_attributes = True


class UserActivityItem(BaseModel):
    """Single activity item"""
    id: UUID
    type: str  # task_complete, module_complete, session_complete, level_up, streak
    title: str
    description: Optional[str] = None
    xp_earned: int = 0
    timestamp: datetime

    class Config:
        from_attributes = True


class UserActivityResponse(BaseModel):
    """User activity feed response"""
    user_id: UUID
    activities: list[UserActivityItem] = []
    total_count: int = 0
    has_more: bool = False


class LeaderboardEntry(BaseModel):
    """Leaderboard entry"""
    rank: int
    user_id: UUID
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    total_xp: int = 0
    level: int = 1
    current_streak: int = 0

    class Config:
        from_attributes = True


class LeaderboardResponse(BaseModel):
    """Leaderboard response"""
    type: str  # xp, streak, weekly
    entries: list[LeaderboardEntry] = []
    user_rank: Optional[int] = None
    total_users: int = 0
