"""
User model - Phase 1 placeholder (no database yet)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class User:
    """
    User model placeholder.
    In Phase 2, this will be a SQLAlchemy model with actual database persistence.
    """
    
    def __init__(
        self,
        email: str,
        hashed_password: str,
        id: Optional[UUID] = None,
        role: UserRole = UserRole.USER,
        onboarding_complete: bool = False,
        baseline_skills: Optional[dict] = None,
        preferences: Optional[dict] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id or uuid4()
        self.email = email.lower().strip()
        self.hashed_password = hashed_password
        self.role = role
        self.onboarding_complete = onboarding_complete
        self.baseline_skills = baseline_skills or {}
        self.preferences = preferences or {}
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Convert user to dictionary (excluding password)"""
        return {
            "id": str(self.id),
            "email": self.email,
            "role": self.role.value,
            "onboarding_complete": self.onboarding_complete,
            "baseline_skills": self.baseline_skills,
            "preferences": self.preferences,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
