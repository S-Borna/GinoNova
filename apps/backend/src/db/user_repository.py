"""
User Repository - Data access layer for user operations
Phase 1.2: In-memory storage (fallback)
Phase 1.5: PostgreSQL with SQLAlchemy (primary)
"""
from typing import Optional
from uuid import UUID
from datetime import datetime

from .memory import USERS
from .database import is_db_configured, get_db_context
from ..schemas.user import UserInDB


def _get_user_model():
    """Lazy import of UserModel to avoid circular imports"""
    from .models import User as UserModel
    return UserModel


def _model_to_schema(user) -> UserInDB:
    """Convert SQLAlchemy model to Pydantic schema"""
    return UserInDB(
        id=user.id,
        email=user.email,
        password_hash=user.hashed_password,
        full_name=user.full_name,
        is_active=user.is_active,
        is_admin=user.is_admin,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


def list_users() -> list[UserInDB]:
    """
    Get all users from the database.

    Returns:
        List of all UserInDB objects
    """
    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            users = db.query(UserModel).all()
            return [_model_to_schema(u) for u in users]

    return list(USERS.values())


def get_user_by_email(email: str) -> Optional[UserInDB]:
    """
    Get user by email address.

    Args:
        email: User's email (will be normalized)

    Returns:
        UserInDB if found, None otherwise
    """
    normalized_email = email.lower().strip()

    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            user = db.query(UserModel).filter(UserModel.email == normalized_email).first()
            return _model_to_schema(user) if user else None

    return USERS.get(normalized_email)


def get_user_by_id(user_id: UUID) -> Optional[UserInDB]:
    """
    Get user by UUID.

    Args:
        user_id: User's UUID

    Returns:
        UserInDB if found, None otherwise
    """
    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            user = db.query(UserModel).filter(UserModel.id == user_id).first()
            return _model_to_schema(user) if user else None

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

    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            # Check if email already exists
            existing = db.query(UserModel).filter(UserModel.email == normalized_email).first()
            if existing:
                raise ValueError(f"User with email {normalized_email} already exists")

            # Create new user
            db_user = UserModel(
                id=user.id,
                email=normalized_email,
                hashed_password=user.password_hash,
                full_name=user.full_name,
                is_active=user.is_active,
                is_admin=user.is_admin,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            db.add(db_user)
            # Commit handled by context manager
            db.flush()
            db.refresh(db_user)
            return _model_to_schema(db_user)

    # Fallback to in-memory
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
    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            user = db.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return None

            # Update allowed fields
            allowed_fields = ['full_name', 'is_active', 'is_admin', 'avatar_url', 'bio',
                            'github_username', 'linkedin_url', 'website_url', 'timezone',
                            'total_xp', 'current_streak', 'longest_streak', 'last_activity_at']

            for key, value in kwargs.items():
                if key in allowed_fields:
                    setattr(user, key, value)

            user.updated_at = datetime.utcnow()
            db.flush()
            db.refresh(user)
            return _model_to_schema(user)

    # Fallback to in-memory
    user = get_user_by_id(user_id)
    if not user:
        return None

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
    if is_db_configured():
        UserModel = _get_user_model()
        with get_db_context() as db:
            user = db.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return False

            db.delete(user)
            # Commit handled by context manager
            return True

    # Fallback to in-memory
    user = get_user_by_id(user_id)
    if not user:
        return False

    del USERS[user.email.lower().strip()]
    return True
