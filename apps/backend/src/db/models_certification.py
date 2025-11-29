"""
Certification & Badge Models - Phase 21
Certificates and badges to validate competence.
"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON, Enum, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from .database import Base


class CertificateType(str, enum.Enum):
    """Types of certificates that can be earned."""
    MODULE = "module"      # Completed a single module
    TRACK = "track"        # Completed an entire track
    BOOTCAMP = "bootcamp"  # Completed the full bootcamp
    MASTER = "master"      # Achieved mastery level


class Certificate(Base):
    """
    Certificate issued to user upon completion.
    Each certificate has a unique verification code for public validation.
    """
    __tablename__ = "certificates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    certificate_type = Column(Enum(CertificateType), nullable=False)
    reference_id = Column(String(100), nullable=False)  # module_id, track_id, etc.
    reference_name = Column(String(255), nullable=False)  # "Linux Fundamentals", etc.
    pdf_url = Column(String(500), nullable=True)  # URL to generated PDF
    verification_code = Column(String(50), unique=True, nullable=False)
    score = Column(Integer, nullable=True)  # Optional completion score (0-100)
    issued_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)  # Most don't expire
    metadata = Column(JSON, default=dict)  # Additional data (skills, duration, etc.)

    # Relationships
    user = relationship("User")


class BadgeCategory(str, enum.Enum):
    """Categories of badges."""
    SKILL = "skill"        # Technical skill badges
    ACHIEVEMENT = "achievement"  # Milestones
    STREAK = "streak"      # Consistency badges
    SOCIAL = "social"      # Community engagement
    SPECIAL = "special"    # Limited edition / events


class Badge(Base):
    """
    Badge awarded to user for achievements.
    Badges can have multiple levels (bronze, silver, gold, etc.)
    """
    __tablename__ = "badges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    badge_slug = Column(String(100), nullable=False)  # Unique identifier like "linux_master"
    badge_name = Column(String(255), nullable=False)  # Display name
    badge_category = Column(Enum(BadgeCategory), default=BadgeCategory.SKILL)
    level = Column(Integer, default=1)  # 1-5 typically
    description = Column(Text, nullable=True)
    icon_url = Column(String(500), nullable=True)
    awarded_at = Column(DateTime, default=datetime.utcnow)
    criteria_met = Column(JSON, default=dict)  # What triggered the badge

    # Relationships
    user = relationship("User")


class BadgeDefinition(Base):
    """
    Badge definitions - what badges exist and their criteria.
    """
    __tablename__ = "badge_definitions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(Enum(BadgeCategory), default=BadgeCategory.SKILL)
    icon_url = Column(String(500), nullable=True)
    max_level = Column(Integer, default=5)
    criteria = Column(JSON, default=dict)  # Criteria for each level
    xp_reward = Column(Integer, default=50)  # XP awarded per level
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
