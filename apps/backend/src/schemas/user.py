"""
User schemas - Pydantic models for API validation
"""
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for user registration"""
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """Schema for public user data (no password)"""
    id: UUID
    email: str
    role: str
    onboarding_complete: bool
    baseline_skills: dict
    preferences: dict
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserInDB(UserPublic):
    """Schema for user data stored in database (includes hashed password)"""
    hashed_password: str


class TokenResponse(BaseModel):
    """Schema for token response"""
    access_token: str
    token_type: str = "bearer"


class AuthResponse(BaseModel):
    """Schema for auth response with user data"""
    user: UserPublic
    message: str
