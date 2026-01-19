"""
Custom exceptions and error helpers
Phase 1.4: Standardized API error responses
"""
from fastapi import HTTPException, status


def raise_conflict(msg: str = "Resource already exists") -> None:
    """Raise 409 Conflict error"""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=msg
    )


def raise_unauthorized(msg: str = "Incorrect email or password") -> None:
    """Raise 401 Unauthorized error"""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"}
    )


def raise_forbidden(msg: str = "Access denied") -> None:
    """Raise 403 Forbidden error"""
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=msg
    )


def raise_not_found(msg: str = "Resource not found") -> None:
    """Raise 404 Not Found error"""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=msg
    )


def raise_bad_request(msg: str = "Invalid request") -> None:
    """Raise 400 Bad Request error"""
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=msg
    )


class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists"""
    pass


class InvalidCredentialsError(Exception):
    """Raised when authentication fails"""
    pass


class UserNotActiveError(Exception):
    """Raised when user account is deactivated"""
    pass


class AccountBannedError(Exception):
    """Raised when user account is banned/suspended"""
    pass
