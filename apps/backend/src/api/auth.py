"""
Auth Router - Authentication endpoints
Phase 1: Register and Login (no JWT yet)
"""
from fastapi import APIRouter, HTTPException, status

from ..schemas.user import UserCreate, UserLogin, UserPublic, AuthResponse
from ..services.user_service import user_service

auth_router = APIRouter()


@auth_router.get("/status")
def auth_status():
    """Check auth module status"""
    return {"auth": "configured", "phase": "1.0"}


@auth_router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate):
    """
    Register a new user.
    
    - **email**: Valid email address (will be normalized to lowercase)
    - **password**: Minimum 6 characters
    """
    try:
        user = user_service.create_user(user_data)
        return AuthResponse(
            user=UserPublic(
                id=user.id,
                email=user.email,
                role=user.role.value,
                onboarding_complete=user.onboarding_complete,
                baseline_skills=user.baseline_skills,
                preferences=user.preferences,
                created_at=user.created_at,
                updated_at=user.updated_at,
            ),
            message="User registered successfully"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@auth_router.post("/login", response_model=AuthResponse)
def login(login_data: UserLogin):
    """
    Login with email and password.
    
    Phase 1: Returns user data
    Phase 1.1: Will return JWT access token
    """
    user = user_service.authenticate_user(login_data)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    return AuthResponse(
        user=UserPublic(
            id=user.id,
            email=user.email,
            role=user.role.value,
            onboarding_complete=user.onboarding_complete,
            baseline_skills=user.baseline_skills,
            preferences=user.preferences,
            created_at=user.created_at,
            updated_at=user.updated_at,
        ),
        message="Login successful"
    )
