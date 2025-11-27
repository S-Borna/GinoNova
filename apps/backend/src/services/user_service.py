"""
User Service - Business logic for user operations
Phase 1.4: Uses repository layer with custom exceptions
"""
from typing import Optional
from uuid import UUID

from ..schemas.user import UserCreate, UserLogin, UserPublic, UserInDB, create_user_in_db
from ..core.security import hash_password, verify_password
from ..core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from ..db import user_repository


class UserService:
    """
    User service handles all user-related business logic.

    Phase 1.4: Uses repository layer with custom exceptions
    Phase 2: Repository will use SQLAlchemy + PostgreSQL
    """

    def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        """Get user by email address (normalized to lowercase)"""
        normalized_email = email.lower().strip()
        return user_repository.get_user_by_email(normalized_email)

    def get_user_by_id(self, user_id: UUID) -> Optional[UserInDB]:
        """Get user by UUID"""
        return user_repository.get_user_by_id(user_id)

    def create_user(self, user_data: UserCreate) -> UserPublic:
        """
        Create a new user.

        Args:
            user_data: UserCreate schema with email, password, and optional full_name

        Returns:
            UserPublic object (without password_hash)

        Raises:
            UserAlreadyExistsError: If email already exists
        """
        # Normalize email before checking (schema also normalizes, but be safe)
        normalized_email = user_data.email.lower().strip()

        # Check if user already exists
        existing = user_repository.get_user_by_email(normalized_email)
        if existing:
            raise UserAlreadyExistsError(f"User with email {normalized_email} already exists")

        # Hash password with bcrypt
        hashed = hash_password(user_data.password)

        # Create UserInDB using factory function
        user_in_db = create_user_in_db(
            email=normalized_email,
            password_hash=hashed,
            full_name=user_data.full_name,
        )

        # Store in repository
        user_repository.create_user(user_in_db)

        # Return public user data
        return UserPublic(
            id=user_in_db.id,
            email=user_in_db.email,
            full_name=user_in_db.full_name,
            is_active=user_in_db.is_active,
            is_admin=user_in_db.is_admin,
            created_at=user_in_db.created_at,
            updated_at=user_in_db.updated_at,
        )

    def authenticate_user(self, login_data: UserLogin) -> Optional[UserInDB]:
        """
        Authenticate user with email and password.

        Args:
            login_data: UserLogin schema with email and password

        Returns:
            UserInDB object if authentication successful

        Raises:
            InvalidCredentialsError: If credentials are invalid
        """
        # Normalize email before lookup (schema also normalizes, but be safe)
        normalized_email = login_data.email.lower().strip()
        user = user_repository.get_user_by_email(normalized_email)

        if not user:
            raise InvalidCredentialsError("Invalid email or password")

        if not verify_password(login_data.password, user.password_hash):
            raise InvalidCredentialsError("Invalid email or password")

        return user

    def update_user(self, user_id: UUID, **kwargs) -> Optional[UserPublic]:
        """
        Update user fields.

        Args:
            user_id: UUID of user to update
            **kwargs: Fields to update

        Returns:
            Updated UserPublic or None if not found
        """
        updated = user_repository.update_user(user_id, **kwargs)
        if not updated:
            return None

        return UserPublic(
            id=updated.id,
            email=updated.email,
            full_name=updated.full_name,
            is_active=updated.is_active,
            is_admin=updated.is_admin,
            created_at=updated.created_at,
            updated_at=updated.updated_at,
        )


# Singleton instance
user_service = UserService()
