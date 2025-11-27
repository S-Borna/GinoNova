"""
Dependencies - FastAPI dependency injection for auth
Phase 1.2: Updated for new user models
"""
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..core.jwt import decode_access_token
from ..services.user_service import user_service
from ..schemas.user import UserPublic

# HTTP Bearer token security scheme
security = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> UserPublic:
    """
    Dependency to get the current authenticated user from JWT token.

    Args:
        credentials: Bearer token from Authorization header

    Returns:
        UserPublic schema of the authenticated user

    Raises:
        HTTPException: 401 if token is invalid or user not found
    """
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
