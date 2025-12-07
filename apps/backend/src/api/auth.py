"""
Auth Router - Authentication endpoints
Phase 1.4: Register, Login with JWT, standardized errors, rate-limit placeholders
Phase OAuth: Google, GitHub, Discord OAuth support
"""
import os
from fastapi import APIRouter, HTTPException, status
from uuid import uuid4
from datetime import datetime

from ..schemas.user import UserCreate, UserLogin, UserPublic, TokenResponse, OAuthRequest, OAuthTokenResponse
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

# === LOCKDOWN MODE ===
# Set LOCKDOWN_MODE=true to block all auth except allowed emails
LOCKDOWN_MODE = os.getenv("LOCKDOWN_MODE", "false").lower() == "true"
ALLOWED_EMAILS = [
    email.strip().lower()
    for email in os.getenv("ALLOWED_EMAILS", "").split(",")
    if email.strip()
]

def check_lockdown(email: str):
    """Block access if lockdown mode is enabled and email is not allowed."""
    if LOCKDOWN_MODE and email.lower() not in ALLOWED_EMAILS:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Systemet är tillfälligt stängt för underhåll. Försök igen senare."
        )


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
        503 Service Unavailable: If lockdown mode is enabled
    """
    # Check lockdown mode - block new registrations except allowed emails
    check_lockdown(user_data.email)

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
    except Exception as e:
        # Log unexpected errors for debugging
        import traceback
        print(f"Registration error: {type(e).__name__}: {e}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Registration failed: {type(e).__name__}: {str(e)}"
        )


@auth_router.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin):
    """
    Login with email and password.

    Returns JWT access token on successful authentication.

    Raises:
        401 Unauthorized: If email/password is incorrect
        503 Service Unavailable: If lockdown mode is enabled
    """
    # Check lockdown mode - block logins except allowed emails
    check_lockdown(login_data.email)

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


# Temporary dev endpoint for password reset (remove in production)
from pydantic import BaseModel

class DevPasswordReset(BaseModel):
    email: str
    new_password: str
    secret: str

@auth_router.post("/dev-reset-password")
def dev_reset_password(data: DevPasswordReset):
    """
    DEV ONLY: Reset password without authentication.
    Requires knowing the email and a secret key.
    """
    import os
    DEV_SECRET = os.getenv("DEV_SECRET", "devops-hub-2024")

    if data.secret != DEV_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    from ..db import user_repository
    from ..core.security import hash_password

    user = user_repository.get_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed = hash_password(data.new_password)
    updated = user_repository.update_user(user.id, hashed_password=hashed)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update password")

    return {"success": True, "message": f"Password reset for {data.email}"}


# === OAUTH ENDPOINTS ===

@auth_router.post("/oauth", response_model=OAuthTokenResponse)
def oauth_login(oauth_data: OAuthRequest):
    """
    OAuth login/register endpoint.

    Called by NextAuth.js after successful OAuth authentication.
    Creates a new user if email doesn't exist, or logs in existing user.

    - **email**: User's email from OAuth provider
    - **name**: User's name from OAuth provider
    - **provider**: OAuth provider (google, github, discord)
    - **provider_id**: Unique ID from OAuth provider
    - **avatar**: Optional avatar URL

    Returns JWT access token and user data.

    Raises:
        503 Service Unavailable: If lockdown mode is enabled
    """
    # Check lockdown mode - block OAuth logins except allowed emails
    check_lockdown(oauth_data.email)

    from ..db import user_repository
    from ..db.database import is_db_configured, get_db_context
    from ..schemas.user import UserInDB

    try:
        # Check if user already exists
        existing_user = user_repository.get_user_by_email(oauth_data.email)

        if existing_user:
            # User exists - update OAuth info if needed and return token
            if is_db_configured():
                from ..db.models import User as UserModel
                with get_db_context() as db:
                    user = db.query(UserModel).filter(UserModel.email == oauth_data.email.lower().strip()).first()
                    if user:
                        # Update OAuth provider info if not set
                        if not user.oauth_provider:
                            user.oauth_provider = oauth_data.provider
                            user.oauth_provider_id = oauth_data.provider_id
                        # Update avatar if provided and not already set
                        if oauth_data.avatar and not user.avatar_url:
                            user.avatar_url = oauth_data.avatar
                        db.flush()
                        db.refresh(user)

            access_token = create_access_token(
                user_id=existing_user.id,
                email=existing_user.email,
                role="admin" if existing_user.is_admin else "user"
            )

            return OAuthTokenResponse(
                access_token=access_token,
                token_type="bearer",
                user=UserPublic(
                    id=existing_user.id,
                    email=existing_user.email,
                    full_name=existing_user.full_name,
                    is_active=existing_user.is_active,
                    is_admin=existing_user.is_admin,
                    created_at=existing_user.created_at,
                    updated_at=existing_user.updated_at,
                )
            )

        # Create new OAuth user
        now = datetime.utcnow()
        new_user_id = uuid4()

        if is_db_configured():
            from ..db.models import User as UserModel
            with get_db_context() as db:
                db_user = UserModel(
                    id=new_user_id,
                    email=oauth_data.email.lower().strip(),
                    hashed_password=None,  # No password for OAuth users
                    full_name=oauth_data.name,
                    oauth_provider=oauth_data.provider,
                    oauth_provider_id=oauth_data.provider_id,
                    avatar_url=oauth_data.avatar,
                    is_active=True,
                    is_admin=False,
                    created_at=now,
                    updated_at=now,
                )
                db.add(db_user)
                db.flush()
                db.refresh(db_user)

                access_token = create_access_token(
                    user_id=db_user.id,
                    email=db_user.email,
                    role="user"
                )

                return OAuthTokenResponse(
                    access_token=access_token,
                    token_type="bearer",
                    user=UserPublic(
                        id=db_user.id,
                        email=db_user.email,
                        full_name=db_user.full_name,
                        is_active=db_user.is_active,
                        is_admin=db_user.is_admin,
                        created_at=db_user.created_at,
                        updated_at=db_user.updated_at,
                    )
                )
        else:
            # Fallback for in-memory storage
            new_user = UserInDB(
                id=new_user_id,
                email=oauth_data.email.lower().strip(),
                password_hash="",  # Empty for OAuth users
                full_name=oauth_data.name,
                is_active=True,
                is_admin=False,
                created_at=now,
                updated_at=now,
            )

            # Store in memory
            from ..db.memory import USERS
            USERS[new_user.email] = new_user

            access_token = create_access_token(
                user_id=new_user.id,
                email=new_user.email,
                role="user"
            )

            return OAuthTokenResponse(
                access_token=access_token,
                token_type="bearer",
                user=UserPublic(
                    id=new_user.id,
                    email=new_user.email,
                    full_name=new_user.full_name,
                    is_active=new_user.is_active,
                    is_admin=new_user.is_admin,
                    created_at=new_user.created_at,
                    updated_at=new_user.updated_at,
                )
            )

    except Exception as e:
        import traceback
        print(f"OAuth error: {type(e).__name__}: {e}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"OAuth authentication failed: {str(e)}"
        )
