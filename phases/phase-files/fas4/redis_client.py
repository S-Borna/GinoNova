"""
Redis Client - Caching and Session Management
Phase FAS 4.1 - PostgreSQL + Redis persistence

Features:
- Lazy initialization
- Connection pooling
- Cache get/set/delete
- Rate limiting
- Session storage
- Health check
"""

import os
import json
import logging
from typing import Optional, Any
from datetime import timedelta

logger = logging.getLogger(__name__)

# Global redis client
_redis_client = None


def is_redis_configured() -> bool:
    """Check if Redis is configured via environment variables."""
    redis_url = os.getenv("REDIS_URL") or os.getenv("REDIS_PRIVATE_URL")
    return bool(redis_url)


def get_redis_client():
    """
    Get or create Redis client with lazy initialization.
    Returns None if Redis is not configured.
    """
    global _redis_client
    
    if _redis_client is not None:
        return _redis_client
    
    redis_url = os.getenv("REDIS_URL") or os.getenv("REDIS_PRIVATE_URL")
    
    if not redis_url:
        logger.info("Redis not configured - using in-memory fallback")
        return None
    
    try:
        import redis
        
        _redis_client = redis.from_url(
            redis_url,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_timeout=5,
            retry_on_timeout=True,
            health_check_interval=30,
        )
        
        # Test connection
        _redis_client.ping()
        logger.info("🔴 Redis connected successfully!")
        
        return _redis_client
        
    except ImportError:
        logger.warning("redis package not installed")
        return None
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
        return None


def close_redis():
    """Close Redis connection."""
    global _redis_client
    if _redis_client:
        try:
            _redis_client.close()
        except:
            pass
        _redis_client = None


# ==============================================================================
# CACHE OPERATIONS
# ==============================================================================

def cache_get(key: str) -> Optional[Any]:
    """
    Get value from cache.
    Returns None if not found or Redis unavailable.
    """
    client = get_redis_client()
    if not client:
        return None
    
    try:
        value = client.get(f"cache:{key}")
        if value:
            return json.loads(value)
        return None
    except Exception as e:
        logger.warning(f"Cache get error for {key}: {e}")
        return None


def cache_set(
    key: str, 
    value: Any, 
    ttl_seconds: int = 3600
) -> bool:
    """
    Set value in cache with TTL.
    Returns True if successful.
    """
    client = get_redis_client()
    if not client:
        return False
    
    try:
        serialized = json.dumps(value)
        client.setex(
            f"cache:{key}",
            ttl_seconds,
            serialized
        )
        return True
    except Exception as e:
        logger.warning(f"Cache set error for {key}: {e}")
        return False


def cache_delete(key: str) -> bool:
    """Delete value from cache."""
    client = get_redis_client()
    if not client:
        return False
    
    try:
        client.delete(f"cache:{key}")
        return True
    except Exception as e:
        logger.warning(f"Cache delete error for {key}: {e}")
        return False


def cache_delete_pattern(pattern: str) -> int:
    """
    Delete all keys matching pattern.
    Returns number of keys deleted.
    """
    client = get_redis_client()
    if not client:
        return 0
    
    try:
        keys = client.keys(f"cache:{pattern}")
        if keys:
            return client.delete(*keys)
        return 0
    except Exception as e:
        logger.warning(f"Cache delete pattern error for {pattern}: {e}")
        return 0


# ==============================================================================
# RATE LIMITING
# ==============================================================================

def check_rate_limit(
    identifier: str,
    limit: int = 100,
    window_seconds: int = 60
) -> tuple[bool, int]:
    """
    Check if rate limit exceeded.
    Returns (is_allowed, remaining_requests).
    """
    client = get_redis_client()
    if not client:
        return True, limit  # Allow if Redis unavailable
    
    key = f"ratelimit:{identifier}"
    
    try:
        pipe = client.pipeline()
        pipe.incr(key)
        pipe.ttl(key)
        results = pipe.execute()
        
        current_count = results[0]
        ttl = results[1]
        
        # Set expiry on first request
        if ttl == -1:
            client.expire(key, window_seconds)
        
        remaining = max(0, limit - current_count)
        is_allowed = current_count <= limit
        
        return is_allowed, remaining
        
    except Exception as e:
        logger.warning(f"Rate limit check error: {e}")
        return True, limit


# ==============================================================================
# SESSION STORAGE
# ==============================================================================

def session_set(
    session_id: str,
    data: dict,
    ttl_seconds: int = 86400  # 24 hours
) -> bool:
    """Store session data."""
    client = get_redis_client()
    if not client:
        return False
    
    try:
        serialized = json.dumps(data)
        client.setex(
            f"session:{session_id}",
            ttl_seconds,
            serialized
        )
        return True
    except Exception as e:
        logger.warning(f"Session set error: {e}")
        return False


def session_get(session_id: str) -> Optional[dict]:
    """Get session data."""
    client = get_redis_client()
    if not client:
        return None
    
    try:
        value = client.get(f"session:{session_id}")
        if value:
            return json.loads(value)
        return None
    except Exception as e:
        logger.warning(f"Session get error: {e}")
        return None


def session_delete(session_id: str) -> bool:
    """Delete session."""
    client = get_redis_client()
    if not client:
        return False
    
    try:
        client.delete(f"session:{session_id}")
        return True
    except:
        return False


def session_extend(session_id: str, ttl_seconds: int = 86400) -> bool:
    """Extend session TTL."""
    client = get_redis_client()
    if not client:
        return False
    
    try:
        return bool(client.expire(f"session:{session_id}", ttl_seconds))
    except:
        return False


# ==============================================================================
# LEADERBOARD / SORTED SETS
# ==============================================================================

def leaderboard_add(
    board_name: str,
    user_id: str,
    score: float
) -> bool:
    """Add or update user score in leaderboard."""
    client = get_redis_client()
    if not client:
        return False
    
    try:
        client.zadd(f"leaderboard:{board_name}", {user_id: score})
        return True
    except Exception as e:
        logger.warning(f"Leaderboard add error: {e}")
        return False


def leaderboard_increment(
    board_name: str,
    user_id: str,
    increment: float
) -> Optional[float]:
    """Increment user score and return new score."""
    client = get_redis_client()
    if not client:
        return None
    
    try:
        return client.zincrby(f"leaderboard:{board_name}", increment, user_id)
    except Exception as e:
        logger.warning(f"Leaderboard increment error: {e}")
        return None


def leaderboard_get_top(
    board_name: str,
    count: int = 10
) -> list[tuple[str, float]]:
    """Get top N users from leaderboard."""
    client = get_redis_client()
    if not client:
        return []
    
    try:
        results = client.zrevrange(
            f"leaderboard:{board_name}",
            0,
            count - 1,
            withscores=True
        )
        return results
    except Exception as e:
        logger.warning(f"Leaderboard get top error: {e}")
        return []


def leaderboard_get_rank(
    board_name: str,
    user_id: str
) -> Optional[int]:
    """Get user rank (1-indexed)."""
    client = get_redis_client()
    if not client:
        return None
    
    try:
        rank = client.zrevrank(f"leaderboard:{board_name}", user_id)
        return rank + 1 if rank is not None else None
    except Exception as e:
        logger.warning(f"Leaderboard get rank error: {e}")
        return None


# ==============================================================================
# HEALTH CHECK
# ==============================================================================

def redis_health_check() -> dict:
    """
    Check Redis health status.
    Returns status dict with connection info.
    """
    client = get_redis_client()
    
    if not client:
        return {
            "status": "unavailable",
            "configured": is_redis_configured(),
            "connected": False,
            "message": "Redis not configured or unavailable"
        }
    
    try:
        info = client.info("server")
        memory = client.info("memory")
        
        return {
            "status": "healthy",
            "configured": True,
            "connected": True,
            "version": info.get("redis_version", "unknown"),
            "used_memory_human": memory.get("used_memory_human", "unknown"),
            "connected_clients": info.get("connected_clients", 0),
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "configured": True,
            "connected": False,
            "error": str(e)
        }
