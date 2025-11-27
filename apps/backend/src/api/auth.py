"""
Auth Router - Authentication endpoints
Phase 1.1: Register, Login with JWT, /me, and protected routes
"""
from fastapi import APIRouter, HTTPException, status

from ..schemas.user import UserCreate, UserLogin, UserPublic, TokenResponse
from ..services.user_service import user_service
from ..core.jwt import create_access_token
from ..core.deps import CurrentUser

auth_router = APIRouter()


@auth_router.get("/status")
def auth_status():
    """Check auth module status"""
    return {"auth": "configured", "phase": "1.1", "jwt": True}


@auth_router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate):
    """
    Register a new user.

    - **email**: Valid email address (will be normalized to lowercase)
    - **password**: Minimum 6 characters

    Returns JWT access token on successful registration.
    """
    try:
        user = user_service.create_user(user_data)

        # Generate JWT token
        access_token = create_access_token(
            user_id=user.id,
            email=user.email,
            role=user.role.value
        )

        return TokenResponse(
            access_token=access_token,
            token_type="bearer"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@auth_router.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin):
    """
    Login with email and password.

    Returns JWT access token on successful authentication.
    """
    user = user_service.authenticate_user(login_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate JWT token
    access_token = create_access_token(
        user_id=user.id,
        email=user.email,
        role=user.role.value
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )


@auth_router.get("/me", response_model=UserPublic)
def get_current_user_info(current_user: CurrentUser):
    """
    Get the current authenticated user's information.

    Requires valid JWT token in Authorization header.
    """
    return current_user


@auth_router.get("/test-protected")
def test_protected_route(current_user: CurrentUser):
    """
    Test protected route - requires authentication.

    Returns success message with user email if token is valid.
    """
    return {
        "ok": True,
        "message": f"Hello {current_user.email}! You are authenticated.",
        "user_id": str(current_user.id)
    }
