"""
JWT Token handling - Creation and validation
"""
import os
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from jose import JWTError, jwt

# JWT Configuration
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

# CRITICAL: Secret key MUST be read from environment in production
# Support both JWT_SECRET_KEY and JWT_SECRET for backwards compatibility
SECRET_KEY = os.getenv("JWT_SECRET_KEY") or os.getenv("JWT_SECRET", "devops-hub-secret-key-change-in-production-abc123xyz789")

# Log warning if using default key
if SECRET_KEY == "devops-hub-secret-key-change-in-production-abc123xyz789":
    import logging
    logging.warning("⚠️  JWT using default SECRET_KEY - set JWT_SECRET_KEY or JWT_SECRET in production!")


def create_access_token(
    user_id: UUID,
    email: str,
    role: str = "user",
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a JWT access token.

    Args:
        user_id: User's UUID
        email: User's email
        role: User's role (user/admin)
        expires_delta: Optional custom expiration time

    Returns:
        Encoded JWT token string
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)

    to_encode = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": expire,
        "version": "1.0",
    }

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Decode and validate a JWT access token.

    Args:
        token: JWT token string

    Returns:
        Decoded token payload if valid, None if invalid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def get_token_user_id(token: str) -> Optional[UUID]:
    """
    Extract user ID from a JWT token.

    Args:
        token: JWT token string

    Returns:
        User UUID if valid token, None otherwise
    """
    payload = decode_access_token(token)
    if payload is None:
        return None

    user_id_str = payload.get("sub")
    if user_id_str is None:
        return None

    try:
        return UUID(user_id_str)
    except ValueError:
        return None
