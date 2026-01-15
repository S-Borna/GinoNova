"""
Admin Core - Phase 10
Admin authentication and authorization utilities
"""
from functools import wraps
from typing import Callable, List, Optional
from fastapi import HTTPException, status

from ..schemas.user import UserPublic


# Admin emails - in production, use database roles
ADMIN_EMAILS = [
    "said.ebadi@hotmail.com",
    "admin@ginonova.se",
]


def is_admin(user: UserPublic) -> bool:
    """
    Check if a user is an admin.

    Args:
        user: UserPublic object

    Returns:
        True if user is admin, False otherwise
    """
    # Check by email
    if user.email.lower() in [e.lower() for e in ADMIN_EMAILS]:
        return True

    # Check by is_admin flag (if exists)
    if getattr(user, 'is_admin', False):
        return True

    return False


def require_admin(user: UserPublic) -> None:
    """
    Require admin access. Raises HTTPException if not admin.

    Args:
        user: UserPublic object

    Raises:
        HTTPException: 403 if not admin
    """
    if not is_admin(user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )


def admin_only(func: Callable) -> Callable:
    """
    Decorator to require admin access for an endpoint.

    Usage:
        @admin_only
        def my_admin_endpoint(current_user: CurrentUser):
            ...
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Find current_user in kwargs
        current_user = kwargs.get('current_user')
        if current_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required"
            )
        require_admin(current_user)
        return await func(*args, **kwargs)
    return wrapper


class AdminPermission:
    """
    Admin permission levels.
    For future role-based access control.
    """
    VIEW_USERS = "view_users"
    EDIT_USERS = "edit_users"
    DELETE_USERS = "delete_users"

    VIEW_CONTENT = "view_content"
    EDIT_CONTENT = "edit_content"
    DELETE_CONTENT = "delete_content"

    VIEW_LOGS = "view_logs"

    SEED_DATA = "seed_data"
    CLEAR_DATA = "clear_data"

    ALL = "*"


# Permission sets by role (for future use)
ADMIN_PERMISSIONS = {
    "super_admin": [AdminPermission.ALL],
    "content_admin": [
        AdminPermission.VIEW_USERS,
        AdminPermission.VIEW_CONTENT,
        AdminPermission.EDIT_CONTENT,
        AdminPermission.VIEW_LOGS,
    ],
    "viewer": [
        AdminPermission.VIEW_USERS,
        AdminPermission.VIEW_CONTENT,
        AdminPermission.VIEW_LOGS,
    ],
}
