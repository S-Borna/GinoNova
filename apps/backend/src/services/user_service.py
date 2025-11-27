"""
User Service - Business logic for user operations
Phase 1: In-memory storage placeholder (no database yet)
"""
from typing import Optional
from uuid import UUID

from ..models.user import User, UserRole
from ..schemas.user import UserCreate, UserLogin


class UserService:
    """
    User service handles all user-related business logic.
    
    Phase 1: Uses in-memory storage (dict)
    Phase 2: Will use SQLAlchemy + PostgreSQL
    """
    
    def __init__(self):
        # In-memory user storage (placeholder for Phase 1)
        self._users: dict[str, User] = {}
    
    def _hash_password(self, password: str) -> str:
        """
        Placeholder password hashing.
        Phase 1.1: Will use bcrypt with passlib
        """
        # TODO: Replace with bcrypt in Phase 1.1
        return f"hashed_{password}"
    
    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Placeholder password verification.
        Phase 1.1: Will use bcrypt with passlib
        """
        # TODO: Replace with bcrypt verification in Phase 1.1
        return hashed_password == f"hashed_{plain_password}"
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email address"""
        normalized_email = email.lower().strip()
        return self._users.get(normalized_email)
    
    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """Get user by UUID"""
        for user in self._users.values():
            if user.id == user_id:
                return user
        return None
    
    def create_user(self, user_data: UserCreate) -> User:
        """
        Create a new user.
        
        Args:
            user_data: UserCreate schema with email and password
            
        Returns:
            Created User object
            
        Raises:
            ValueError: If email already exists
        """
        normalized_email = user_data.email.lower().strip()
        
        # Check if user already exists
        if normalized_email in self._users:
            raise ValueError(f"User with email {normalized_email} already exists")
        
        # Hash password and create user
        hashed_password = self._hash_password(user_data.password)
        user = User(
            email=normalized_email,
            hashed_password=hashed_password,
            role=UserRole.USER,
        )
        
        # Store user
        self._users[normalized_email] = user
        
        return user
    
    def authenticate_user(self, login_data: UserLogin) -> Optional[User]:
        """
        Authenticate user with email and password.
        
        Args:
            login_data: UserLogin schema with email and password
            
        Returns:
            User object if authentication successful, None otherwise
        """
        user = self.get_user_by_email(login_data.email)
        
        if not user:
            return None
        
        if not self._verify_password(login_data.password, user.hashed_password):
            return None
        
        return user
    
    def update_user(self, user_id: UUID, **kwargs) -> Optional[User]:
        """
        Update user fields.
        
        Args:
            user_id: UUID of user to update
            **kwargs: Fields to update
            
        Returns:
            Updated User object or None if not found
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key) and key not in ["id", "email", "hashed_password"]:
                setattr(user, key, value)
        
        return user


# Singleton instance for Phase 1 (in-memory storage)
user_service = UserService()
