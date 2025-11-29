"""
Analytics Models - Phase 13
Track user behavior, study time, and progress insights.
"""
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, JSON, Date, Index
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
import uuid

from .database import Base


class AnalyticsEvent(Base):
    """
    Generic analytics event for tracking user actions.
    """
    __tablename__ = "analytics_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    event_type = Column(String(100), nullable=False, index=True)
    event_data = Column(JSON, default=dict)
    session_id = Column(String(100), nullable=True)  # Browser session
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    __table_args__ = (
        Index('ix_analytics_user_type_date', 'user_id', 'event_type', 'created_at'),
    )


class DailyStats(Base):
    """
    Aggregated daily statistics per user.
    """
    __tablename__ = "daily_stats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    study_minutes = Column(Integer, default=0)
    tasks_completed = Column(Integer, default=0)
    tasks_attempted = Column(Integer, default=0)
    xp_earned = Column(Integer, default=0)
    sessions_count = Column(Integer, default=0)
    ai_calls = Column(Integer, default=0)
    hints_used = Column(Integer, default=0)
    modules_touched = Column(JSON, default=list)  # List of module IDs worked on
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        Index('ix_daily_stats_user_date', 'user_id', 'date', unique=True),
    )


class UserInsights(Base):
    """
    Computed insights about user's learning patterns.
    Updated periodically based on analytics events.
    """
    __tablename__ = "user_insights"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)

    # Study patterns
    total_study_hours = Column(Float, default=0)
    avg_session_length = Column(Integer, default=0)  # Minutes
    favorite_study_time = Column(String(20), nullable=True)  # morning, afternoon, evening, night
    most_active_day = Column(String(10), nullable=True)  # monday, tuesday, etc.

    # Performance
    strongest_skill = Column(String(100), nullable=True)  # Module with best performance
    weakest_skill = Column(String(100), nullable=True)  # Module needing improvement
    avg_task_completion_time = Column(Integer, nullable=True)  # Minutes
    accuracy_rate = Column(Float, nullable=True)  # 0-100%

    # Engagement
    longest_streak = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    streak_start_date = Column(Date, nullable=True)
    last_active_date = Column(Date, nullable=True)

    # Predictions
    estimated_completion_date = Column(Date, nullable=True)
    recommended_pace = Column(String(50), nullable=True)  # slow, normal, fast

    # Metadata
    calculated_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ModuleAnalytics(Base):
    """
    Analytics aggregated per module (for admin insights).
    """
    __tablename__ = "module_analytics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    module_id = Column(UUID(as_uuid=True), nullable=False, unique=True)
    module_slug = Column(String(100), nullable=False)

    # Engagement
    total_enrollments = Column(Integer, default=0)
    active_users = Column(Integer, default=0)
    completions = Column(Integer, default=0)
    completion_rate = Column(Float, default=0)  # 0-100%

    # Performance
    avg_completion_time = Column(Float, nullable=True)  # Hours
    avg_score = Column(Float, nullable=True)
    difficulty_rating = Column(Float, nullable=True)  # User-perceived difficulty

    # Feedback
    avg_rating = Column(Float, nullable=True)
    rating_count = Column(Integer, default=0)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
