"""
User schemas - Pydantic models for API validation
Phase 1.2: Full user models with repository layer
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema with common fields"""
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False


class UserCreate(BaseModel):
    """Schema for user registration"""
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str


class UserPublic(UserBase):
    """Schema for public user data (no password)"""
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserInDB(UserPublic):
    """Schema for user data stored in database (includes hashed password)"""
    password_hash: str


def create_user_in_db(
    email: str,
    password_hash: str,
    full_name: Optional[str] = None,
    is_active: bool = True,
    is_admin: bool = False,
) -> UserInDB:
    """Factory function to create a new UserInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    return UserInDB(
        id=uuid4(),
        email=email.lower().strip(),
        password_hash=password_hash,
        full_name=full_name,
        is_active=is_active,
        is_admin=is_admin,
        created_at=now,
        updated_at=now,
    )


class TokenResponse(BaseModel):
    """Schema for token response"""
    access_token: str
    token_type: str = "bearer"


class AuthResponse(BaseModel):
    """Schema for auth response with user data"""
    user: UserPublic
    message: str
