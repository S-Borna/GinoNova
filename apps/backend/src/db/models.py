"""
SQLAlchemy Models - All database tables
"""
import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Boolean, Integer, Float, DateTime, Text, 
    ForeignKey, JSON, Enum, Index
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    """User account model"""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    
    # Profile fields (Phase 9)
    avatar_url = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    github_username = Column(String(100), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    website_url = Column(String(255), nullable=True)
    timezone = Column(String(50), default="UTC")
    
    # Status
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    
    # Stats
    total_xp = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_activity_at = Column(DateTime, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    studyflow_sessions = relationship("StudyflowSession", back_populates="user", cascade="all, delete-orphan")


class Track(Base):
    """Learning track model"""
    __tablename__ = "tracks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)
    color = Column(String(7), default="#6366f1")  # Hex color
    icon = Column(String(10), default="📚")  # Emoji
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    modules = relationship("Module", back_populates="track", cascade="all, delete-orphan")


class Module(Base):
    """Learning module model"""
    __tablename__ = "modules"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    track_id = Column(UUID(as_uuid=True), ForeignKey("tracks.id"), nullable=True)
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)
    difficulty = Column(String(20), default="intermediate")
    estimated_hours = Column(Float, default=10.0)
    prerequisites = Column(JSON, default=list)  # List of module slugs
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    track = relationship("Track", back_populates="modules")
    tasks = relationship("Task", back_populates="module", cascade="all, delete-orphan")
    labs = relationship("Lab", back_populates="module", cascade="all, delete-orphan")
    project = relationship("Project", back_populates="module", uselist=False, cascade="all, delete-orphan")

    __table_args__ = (
        Index('ix_modules_track_order', 'track_id', 'order_index'),
    )


class Task(Base):
    """Task/Lesson model"""
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    module_id = Column(UUID(as_uuid=True), ForeignKey("modules.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)  # Markdown content
    order_index = Column(Integer, default=1)
    difficulty = Column(String(20), default="medium")
    estimated_minutes = Column(Integer, default=15)
    xp_reward = Column(Integer, default=25)
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="tasks")

    __table_args__ = (
        Index('ix_tasks_module_order', 'module_id', 'order_index'),
    )


class Lab(Base):
    """Hands-on lab model"""
    __tablename__ = "labs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    module_id = Column(UUID(as_uuid=True), ForeignKey("modules.id"), nullable=False)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    instructions = Column(Text, nullable=True)  # Markdown
    order_index = Column(Integer, default=1)
    difficulty = Column(String(20), default="medium")
    estimated_hours = Column(Float, default=2.0)
    xp_reward = Column(Integer, default=100)
    expected_outcomes = Column(JSON, default=list)
    hints = Column(JSON, default=list)
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="labs")

    __table_args__ = (
        Index('ix_labs_module_order', 'module_id', 'order_index'),
    )


class Project(Base):
    """Module capstone project"""
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    module_id = Column(UUID(as_uuid=True), ForeignKey("modules.id"), nullable=False, unique=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True)  # Markdown
    deliverables = Column(JSON, default=list)
    estimated_hours = Column(Float, default=5.0)
    xp_reward = Column(Integer, default=500)
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="project")


class Progress(Base):
    """User progress tracking"""
    __tablename__ = "progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # What is being tracked (one of these should be set)
    module_id = Column(UUID(as_uuid=True), ForeignKey("modules.id"), nullable=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), nullable=True)
    lab_id = Column(UUID(as_uuid=True), ForeignKey("labs.id"), nullable=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    
    status = Column(String(20), default="not_started")  # not_started, in_progress, completed
    progress_percent = Column(Integer, default=0)
    xp_earned = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="progress")

    __table_args__ = (
        Index('ix_progress_user_module', 'user_id', 'module_id'),
        Index('ix_progress_user_task', 'user_id', 'task_id'),
    )


class StudyflowSession(Base):
    """Study session tracking"""
    __tablename__ = "studyflow_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    session_type = Column(String(20), default="pomodoro")  # pomodoro, deep_focus, custom
    duration_minutes = Column(Integer, default=25)
    actual_duration = Column(Integer, nullable=True)  # Actual time spent
    
    tasks_completed = Column(Integer, default=0)
    xp_earned = Column(Integer, default=0)
    
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    status = Column(String(20), default="active")  # active, completed, cancelled
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="studyflow_sessions")

    __table_args__ = (
        Index('ix_studyflow_user_date', 'user_id', 'started_at'),
    )
