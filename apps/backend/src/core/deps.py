"""
Dependencies - FastAPI dependency injection for auth
Phase 1.4: Enhanced error messages and is_active check
Phase 10.1: Auto-update last_activity_at on every authenticated request
"""
from typing import Annotated, Optional
from uuid import UUID
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..core.jwt import decode_access_token
from ..services.user_service import user_service
from ..schemas.user import UserPublic
from ..db import user_repository

# HTTP Bearer token security scheme (auto_error=False for explicit error handling)
security = HTTPBearer(auto_error=False)

# Throttle activity updates - only update if more than 5 minutes since last update
ACTIVITY_UPDATE_THROTTLE_MINUTES = 5


async def get_current_user(
    credentials: Annotated[Optional[HTTPAuthorizationCredentials], Depends(security)]
) -> UserPublic:
    """
    Dependency to get the current authenticated user from JWT token.

    Args:
        credentials: Bearer token from Authorization header

    Returns:
        UserPublic schema of the authenticated user

    Raises:
        HTTPException: 401 if token is missing, invalid, or user not found
        HTTPException: 403 if user account is deactivated
    """
    # Check if credentials are provided
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    user_id_str = payload.get("sub")
    if user_id_str is None:
        raise credentials_exception

    try:
        user_id = UUID(user_id_str)
    except ValueError:
        raise credentials_exception

    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise credentials_exception

    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is deactivated"
        )

    # Auto-update last_activity_at (throttled to avoid excessive DB writes)
    # Only update if more than ACTIVITY_UPDATE_THROTTLE_MINUTES since last update
    now = datetime.utcnow()
    should_update_activity = False
    
    if user.last_activity_at is None:
        should_update_activity = True
    else:
        time_since_last = now - user.last_activity_at
        if time_since_last > timedelta(minutes=ACTIVITY_UPDATE_THROTTLE_MINUTES):
            should_update_activity = True
    
    if should_update_activity:
        try:
            user_repository.update_user(user.id, last_activity_at=now)
        except Exception:
            # Don't fail the request if activity update fails
            pass

    return UserPublic(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active,
        is_admin=user.is_admin,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


async def get_current_admin_user(
    current_user: Annotated[UserPublic, Depends(get_current_user)]
) -> UserPublic:
    """
    Dependency to verify the current user is an admin.

    Args:
        current_user: The authenticated user from get_current_user

    Returns:
        UserPublic schema if user is admin

    Raises:
        HTTPException: 403 if user is not an admin
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


async def get_current_active_user(
    current_user: Annotated[UserPublic, Depends(get_current_user)]
) -> UserPublic:
    """
    Dependency to verify the current user is active.

    Note: get_current_user already checks is_active, but this can be used
    for explicit documentation purposes.

    Args:
        current_user: The authenticated user from get_current_user

    Returns:
        UserPublic schema if user is active

    Raises:
        HTTPException: 403 if user is not active
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is deactivated"
        )
    return current_user


# Type aliases for cleaner dependency injection
CurrentUser = Annotated[UserPublic, Depends(get_current_user)]
AdminUser = Annotated[UserPublic, Depends(get_current_admin_user)]
ActiveUser = Annotated[UserPublic, Depends(get_current_active_user)]
