"""
Auth Router - Authentication endpoints
Phase 1.4: Register, Login with JWT, standardized errors, rate-limit placeholders
Phase OAuth: Google, GitHub, Discord OAuth support
"""
import os
from fastapi import APIRouter, HTTPException, status, Request
from uuid import uuid4
from datetime import datetime, timezone

from ..schemas.user import UserCreate, UserLogin, UserPublic, TokenResponse, OAuthRequest, OAuthTokenResponse
from ..services.user_service import user_service
from ..core.jwt import create_access_token
from ..core.deps import CurrentUser
from ..core.exceptions import (
    raise_conflict,
    raise_unauthorized,
    raise_forbidden,
    UserAlreadyExistsError,
    InvalidCredentialsError,
    AccountBannedError,
)
from ..db import user_repository

auth_router = APIRouter()


def get_client_ip(request: Request) -> str:
    """Get client IP from request, handling proxies/load balancers."""
    # Check common proxy headers
    forwarded_for = request.headers.get("X-Forwarded-For")
    if forwarded_for:
        # X-Forwarded-For can be comma-separated list, first is original client
        return forwarded_for.split(",")[0].strip()

    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip.strip()

    # Fallback to direct client IP
    if request.client:
        return request.client.host

    return None

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
def register(user_data: UserCreate, request: Request):
    """
    Register a new user.

    - **email**: Valid email address (will be normalized to lowercase)
    - **password**: Minimum 8 characters
    - **full_name**: Optional full name (max 100 chars)

    Returns JWT access token on successful registration.
    User must verify email before full access is granted.

    Raises:
        409 Conflict: If email already exists
        422 Validation Error: If password/email invalid
        503 Service Unavailable: If lockdown mode is enabled
    """
    # Check lockdown mode - block new registrations except allowed emails
    check_lockdown(user_data.email)

    # Get client IP for tracking
    client_ip = get_client_ip(request)

    # TODO: Add rate limit - limiter.limit("5/minute")
    try:
        user = user_service.create_user(user_data)

        # Save registration IP
        if client_ip:
            user_repository.update_user(user.id, registration_ip=client_ip, last_login_ip=client_ip)

        # Generate and send verification code
        try:
            from src.services.email_service import generate_verification_code, get_code_expiry, send_verification_email
            from src.db.database import SessionLocal
            from src.db.models import User as UserModel

            code = generate_verification_code()
            expires_at = get_code_expiry()

            # Update user with verification code
            db = SessionLocal()
            try:
                db_user = db.query(UserModel).filter(UserModel.id == user.id).first()
                if db_user:
                    db_user.verification_code = code
                    db_user.verification_code_expires_at = expires_at
                    db_user.is_verified = False
                    db.commit()

                    # Send verification email
                    send_verification_email(user.email, code, user.full_name)
                    print(f"[Register] Verification code sent to {user.email}")
            finally:
                db.close()
        except Exception as e:
            print(f"[Register] Failed to send verification email: {e}")
            # Continue anyway - user can request new code

        # Log registration activity for admin dashboard
        try:
            from .routes.admin_v2 import add_activity_log
            add_activity_log(
                activity_type="registration",
                user_id=str(user.id),
                user_email=user.email,
                user_name=user.full_name,
                details=f"New user via email/password registration (IP: {client_ip or 'unknown'}) - awaiting verification"
            )
        except Exception as e:
            print(f"[ActivityLog] Failed to log registration: {e}")

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
def login(login_data: UserLogin, request: Request):
    """
    Login with email and password.

    Returns JWT access token on successful authentication.

    Raises:
        401 Unauthorized: If email/password is incorrect
        403 Forbidden: If user account is banned/suspended
        503 Service Unavailable: If lockdown mode is enabled
    """
    # Check lockdown mode - block logins except allowed emails
    check_lockdown(login_data.email)

    # Get client IP
    client_ip = get_client_ip(request)

    # TODO: Add rate limit - limiter.limit("10/minute")
    try:
        user = user_service.authenticate_user(login_data)
    except InvalidCredentialsError:
        raise_unauthorized("Incorrect email or password")
    except AccountBannedError:
        raise_forbidden("Your account has been suspended. Contact support for assistance.")

    if not user:
        raise_unauthorized("Incorrect email or password")

    # Update last_activity_at, last_login_at, and last_login_ip
    from ..db import user_repository
    now = datetime.now(timezone.utc)
    update_data = {"last_activity_at": now, "last_login_at": now}
    if client_ip:
        update_data["last_login_ip"] = client_ip
    user_repository.update_user(user.id, **update_data)

    # Log login activity for admin dashboard
    try:
        from .routes.admin_v2 import add_activity_log
        add_activity_log(
            activity_type="login",
            user_id=str(user.id),
            user_email=user.email,
            user_name=user.full_name,
            details=f"Email/password login (IP: {client_ip or 'unknown'})"
        )
    except Exception as e:
        print(f"[ActivityLog] Failed to log login: {e}")

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


@auth_router.post("/logout")
def logout_user(current_user: CurrentUser, request: Request):
    """
    Logout - logs user activity before token is cleared on client.
    Returns success message.
    """
    # Get client IP
    client_ip = get_client_ip(request)

    # Log logout activity for admin dashboard
    try:
        from .routes.admin_v2 import add_activity_log
        add_activity_log(
            activity_type="logout",
            user_id=str(current_user.id),
            user_email=current_user.email,
            user_name=current_user.full_name,
            details=f"User logged out (IP: {client_ip or 'unknown'})"
        )
    except Exception as e:
        print(f"[ActivityLog] Failed to log logout: {e}")

    return {"ok": True, "message": "Logged out successfully"}


@auth_router.get("/me", response_model=UserPublic)
def get_current_user_info(current_user: CurrentUser):
    """
    Get the current authenticated user's information.

    Requires valid JWT token in Authorization header.
    Returns UserPublic schema.
    Also updates last_activity_at for online status tracking.
    """
    # Update last_activity_at for online status tracking
    user_repository.update_user(current_user.id, last_activity_at=datetime.now(timezone.utc))
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


# ==============================================================================
# SECURITY: DEV ENDPOINT REMOVED
# ==============================================================================
# The /dev-reset-password endpoint has been removed for security reasons.
# It allowed password resets without proper authentication, which is a critical
# security vulnerability in production environments.
#
# For password resets, use the proper /forgot-password and /reset-password endpoints
# that require email verification tokens.
#
# If you need to reset a password in development, use the database directly or
# create a proper admin endpoint with full authentication and authorization.
# ==============================================================================


# === OAUTH ENDPOINTS ===

@auth_router.post("/oauth", response_model=OAuthTokenResponse)
def oauth_login(oauth_data: OAuthRequest, request: Request):
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

    # Get client IP
    client_ip = get_client_ip(request)

    from ..db import user_repository
    from ..db.database import is_db_configured, get_db_context
    from ..schemas.user import UserInDB

    try:
        # Check if user already exists
        existing_user = user_repository.get_user_by_email(oauth_data.email)

        if existing_user:
            # Check if user is banned/deactivated
            if not existing_user.is_active:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Your account has been suspended. Contact support for assistance."
                )

            # User exists - update OAuth info and last_activity_at
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
                        # Update last_activity_at, last_login_at, and last_login_ip
                        now = datetime.now(timezone.utc)
                        user.last_activity_at = now
                        user.last_login_at = now
                        if client_ip:
                            user.last_login_ip = client_ip
                        user.updated_at = now
                        db.flush()
                        db.refresh(user)

            # Log OAuth login activity for admin dashboard
            try:
                from .routes.admin_v2 import add_activity_log
                add_activity_log(
                    activity_type="login",
                    user_id=str(existing_user.id),
                    user_email=existing_user.email,
                    user_name=existing_user.full_name,
                    details=f"{oauth_data.provider.capitalize()} OAuth login (IP: {client_ip or 'unknown'})",
                    oauth_provider=oauth_data.provider
                )
            except Exception as e:
                print(f"[ActivityLog] Failed to log OAuth login: {e}")

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
        now = datetime.now(timezone.utc)
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
                    registration_ip=client_ip,
                    last_login_ip=client_ip,
                    is_active=True,
                    is_admin=False,
                    created_at=now,
                    updated_at=now,
                    last_activity_at=now,
                )
                db.add(db_user)
                db.flush()
                db.refresh(db_user)

                # Log new OAuth registration for admin dashboard
                try:
                    from .routes.admin_v2 import add_activity_log
                    add_activity_log(
                        activity_type="registration",
                        user_id=str(db_user.id),
                        user_email=db_user.email,
                        user_name=db_user.full_name,
                        details=f"New user via {oauth_data.provider.capitalize()} OAuth (IP: {client_ip or 'unknown'})",
                        oauth_provider=oauth_data.provider
                    )
                except Exception as e:
                    print(f"[ActivityLog] Failed to log OAuth registration: {e}")

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
