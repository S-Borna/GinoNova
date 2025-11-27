"""
User Repository - Data access layer for user operations
Phase 1.2: In-memory storage
Phase 2: PostgreSQL with SQLAlchemy
"""
from typing import Optional
from uuid import UUID

from .memory import USERS
from ..schemas.user import UserInDB


def get_user_by_email(email: str) -> Optional[UserInDB]:
    """
    Get user by email address.

    Args:
        email: User's email (will be normalized)

    Returns:
        UserInDB if found, None otherwise
    """
    normalized_email = email.lower().strip()
    return USERS.get(normalized_email)


def get_user_by_id(user_id: UUID) -> Optional[UserInDB]:
    """
    Get user by UUID.

    Args:
        user_id: User's UUID

    Returns:
        UserInDB if found, None otherwise
    """
    for user in USERS.values():
        if user.id == user_id:
            return user
    return None


def create_user(user: UserInDB) -> UserInDB:
    """
    Store a new user in the database.

    Args:
        user: UserInDB object to store

    Returns:
        The stored UserInDB object

    Raises:
        ValueError: If email already exists
    """
    normalized_email = user.email.lower().strip()

    if normalized_email in USERS:
        raise ValueError(f"User with email {normalized_email} already exists")

    USERS[normalized_email] = user
    return user


def update_user(user_id: UUID, **kwargs) -> Optional[UserInDB]:
    """
    Update user fields.

    Args:
        user_id: UUID of user to update
        **kwargs: Fields to update

    Returns:
        Updated UserInDB or None if not found
    """
    user = get_user_by_id(user_id)
    if not user:
        return None

    # Create updated user with new values
    user_dict = user.model_dump()
    for key, value in kwargs.items():
        if key in user_dict and key not in ["id", "email", "password_hash"]:
            user_dict[key] = value

    updated_user = UserInDB(**user_dict)
    USERS[user.email.lower().strip()] = updated_user
    return updated_user


def delete_user(user_id: UUID) -> bool:
    """
    Delete a user by UUID.

    Args:
        user_id: UUID of user to delete

    Returns:
        True if deleted, False if not found
    """
    user = get_user_by_id(user_id)
    if not user:
        return False

    del USERS[user.email.lower().strip()]
    return True
