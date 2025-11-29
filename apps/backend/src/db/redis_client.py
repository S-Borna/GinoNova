"""
Redis Client - Phase 22
Provides caching and rate limiting via Redis.
"""
import os
import json
import logging
from typing import Optional, Any, Tuple

logger = logging.getLogger(__name__)
REDIS_URL = os.getenv("REDIS_URL", "")
_redis_client = None


def get_redis_client():
    """Get or create Redis client singleton."""
    global _redis_client
    if _redis_client is not None:
        return _redis_client
    if not REDIS_URL:
        logger.warning("REDIS_URL not set - Redis features disabled")
        return None
    try:
        import redis
        _redis_client = redis.from_url(REDIS_URL, decode_responses=True, socket_timeout=5)
        _redis_client.ping()
        logger.info("✅ Redis connected")
        return _redis_client
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
        return None


def is_redis_configured() -> bool:
    """Check if Redis is available."""
    return get_redis_client() is not None


def cache_get(key: str) -> Optional[Any]:
    """Get value from cache."""
    client = get_redis_client()
    if not client:
        return None
    try:
        value = client.get(key)
        return json.loads(value) if value else None
    except Exception as e:
        logger.debug(f"Cache get failed for {key}: {e}")
        return None


def cache_set(key: str, value: Any, ttl: int = 300) -> bool:
    """Set value in cache with TTL (default 5 minutes)."""
    client = get_redis_client()
    if not client:
        return False
    try:
        client.setex(key, ttl, json.dumps(value, default=str))
        return True
    except Exception as e:
        logger.debug(f"Cache set failed for {key}: {e}")
        return False


def cache_delete(key: str) -> bool:
    """Delete key from cache."""
    client = get_redis_client()
    if not client:
        return False
    try:
        client.delete(key)
        return True
    except Exception as e:
        logger.debug(f"Cache delete failed for {key}: {e}")
        return False


def check_rate_limit(identifier: str, max_requests: int, window_seconds: int) -> Tuple[bool, int]:
    """
    Check rate limit for identifier.
    Returns (allowed, remaining_requests).
    """
    client = get_redis_client()
    if not client:
        return True, max_requests  # Allow if Redis unavailable

    key = f"rate_limit:{identifier}"
    try:
        current = client.get(key)
        if current is None:
            client.setex(key, window_seconds, 1)
            return True, max_requests - 1

        current_count = int(current)
        if current_count >= max_requests:
            return False, 0

        client.incr(key)
        return True, max_requests - current_count - 1
    except Exception as e:
        logger.debug(f"Rate limit check failed: {e}")
        return True, max_requests
