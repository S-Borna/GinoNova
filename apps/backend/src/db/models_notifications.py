"""
Notification Models - Phase 12
In-app and email notification system.
"""
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from .database import Base


class Notification(Base):
    """
    In-app notification for a user.
    """
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    type = Column(String(50), nullable=False)  # streak_reminder, achievement, etc.
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    data = Column(JSON, default=dict)  # Additional data (links, IDs, etc.)
    read = Column(Boolean, default=False, index=True)
    read_at = Column(DateTime, nullable=True)
    action_url = Column(String(500), nullable=True)  # Deep link
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    expires_at = Column(DateTime, nullable=True)  # Auto-dismiss after this


class NotificationPreference(Base):
    """
    User preferences for notifications.
    """
    __tablename__ = "notification_preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)

    # In-app notifications
    in_app_enabled = Column(Boolean, default=True)

    # Email preferences
    email_enabled = Column(Boolean, default=True)
    email_digest = Column(String(20), default="daily")  # none, instant, daily, weekly

    # Notification types
    streak_reminders = Column(Boolean, default=True)
    weekly_summary = Column(Boolean, default=True)
    achievement_alerts = Column(Boolean, default=True)
    new_content_alerts = Column(Boolean, default=True)
    marketing_emails = Column(Boolean, default=False)

    # Push notifications (future)
    push_enabled = Column(Boolean, default=False)

    # Quiet hours
    quiet_hours_start = Column(String(5), nullable=True)  # HH:MM
    quiet_hours_end = Column(String(5), nullable=True)
    timezone = Column(String(50), default="UTC")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class EmailLog(Base):
    """
    Log of sent emails for tracking and debugging.
    """
    __tablename__ = "email_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    email_type = Column(String(50), nullable=False)
    recipient = Column(String(255), nullable=False)
    subject = Column(String(500), nullable=False)
    status = Column(String(20), default="sent")  # sent, delivered, failed, bounced
    provider_id = Column(String(255), nullable=True)  # SendGrid/SES message ID
    error_message = Column(Text, nullable=True)
    sent_at = Column(DateTime, default=datetime.utcnow)
