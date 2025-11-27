"""
User model - Phase 1.2
Note: This module is kept for backwards compatibility.
The main user models are now in schemas/user.py (Pydantic models)
and will be replaced by SQLAlchemy models in Phase 2.
"""
from enum import Enum


class UserRole(str, Enum):
    """User roles enum - kept for backwards compatibility"""
    USER = "user"
    ADMIN = "admin"


# The User class is deprecated in Phase 1.2
# Use schemas.user.UserInDB and schemas.user.UserPublic instead
# This will be replaced by SQLAlchemy models in Phase 2
