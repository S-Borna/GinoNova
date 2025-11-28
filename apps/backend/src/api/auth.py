"""
Auth Router - Authentication endpoints
Phase 1.4: Register, Login with JWT, standardized errors, rate-limit placeholders
"""
from fastapi import APIRouter, HTTPException, status

from ..schemas.user import UserCreate, UserLogin, UserPublic, TokenResponse
from ..services.user_service import user_service
from ..core.jwt import create_access_token
from ..core.deps import CurrentUser
from ..core.exceptions import (
    raise_conflict,
    raise_unauthorized,
    UserAlreadyExistsError,
    InvalidCredentialsError,
)

auth_router = APIRouter()


# === RATE LIMIT PLACEHOLDERS ===
# TODO Phase 2: Add rate limiting middleware (e.g., slowapi)
# from slowapi import Limiter
# limiter = Limiter(key_func=get_remote_address)
# @limiter.limit("5/minute")  # 5 requests per minute for auth endpoints


@auth_router.get("/status")
def auth_status():
    """Check auth module status"""
    return {"auth": "configured", "phase": "1.4", "jwt": True, "models": "UserBase/UserCreate/UserInDB/UserPublic"}


@auth_router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate):
    """
    Register a new user.

    - **email**: Valid email address (will be normalized to lowercase)
    - **password**: Minimum 8 characters
    - **full_name**: Optional full name (max 100 chars)

    Returns JWT access token on successful registration.

    Raises:
        409 Conflict: If email already exists
        422 Validation Error: If password/email invalid
    """
    # TODO: Add rate limit - limiter.limit("5/minute")
    try:
        user = user_service.create_user(user_data)

        # Generate JWT token
        access_token = create_access_token(
            user_id=user.id,
            email=user.email,
            role="admin" if user.is_admin else "user"
        )

        return TokenResponse(
            access_token=access_token,
            token_type="bearer"
        )
    except UserAlreadyExistsError:
        raise_conflict("A user with this email already exists")


@auth_router.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin):
    """
    Login with email and password.

    Returns JWT access token on successful authentication.

    Raises:
        401 Unauthorized: If email/password is incorrect
    """
    # TODO: Add rate limit - limiter.limit("10/minute")
    try:
        user = user_service.authenticate_user(login_data)
    except InvalidCredentialsError:
        raise_unauthorized("Incorrect email or password")

    if not user:
        raise_unauthorized("Incorrect email or password")

    # Generate JWT token
    access_token = create_access_token(
        user_id=user.id,
        email=user.email,
        role="admin" if user.is_admin else "user"
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
    Returns UserPublic schema.
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
        "user_id": str(current_user.id),
        "is_admin": current_user.is_admin
    }


@auth_router.post("/me/reset-progress")
def reset_user_progress(current_user: CurrentUser):
    """
    Reset all progress for the current user.

    This will:
    - Delete all progress records for the user
    - Keep account info (email, password, name)

    Returns:
        Success message with count of deleted records
    """
    from ..db import progress_repository

    # Get all progress records for this user
    user_progress = progress_repository.list_progress_by_user(current_user.id)
    deleted_count = len(user_progress)

    # Delete each progress record
    for progress in user_progress:
        progress_repository.delete_progress(progress.id)

    return {
        "ok": True,
        "message": f"Successfully reset all progress",
        "deleted_records": deleted_count
    }
