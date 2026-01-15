"""
Rate Limit Middleware - Phase 29 + Security Hardening
Protects API from abuse using Redis-based rate limiting with in-memory fallback.
"""
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging
import time
from collections import defaultdict

logger = logging.getLogger(__name__)

# In-memory fallback rate limiter (when Redis is unavailable)
class InMemoryRateLimiter:
    """Simple in-memory rate limiter using sliding window"""
    def __init__(self):
        self.requests = defaultdict(list)  # identifier -> list of request timestamps

    def check_rate_limit(self, identifier: str, max_requests: int, window_seconds: int) -> tuple[bool, int]:
        """Check if request is within rate limit. Returns (allowed, remaining)"""
        now = time.time()
        window_start = now - window_seconds

        # Clean old requests
        self.requests[identifier] = [
            ts for ts in self.requests[identifier]
            if ts > window_start
        ]

        current_count = len(self.requests[identifier])

        if current_count >= max_requests:
            return False, 0

        # Allow request
        self.requests[identifier].append(now)
        remaining = max_requests - current_count - 1
        return True, remaining

    def cleanup(self):
        """Periodically cleanup old entries to prevent memory bloat"""
        now = time.time()
        cutoff = now - 300  # Keep last 5 minutes
        for identifier in list(self.requests.keys()):
            self.requests[identifier] = [ts for ts in self.requests[identifier] if ts > cutoff]
            if not self.requests[identifier]:
                del self.requests[identifier]

# Global in-memory limiter instance
_memory_limiter = InMemoryRateLimiter()


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Rate limiting middleware using Redis with in-memory fallback.
    Stricter limits for auth endpoints to prevent brute force attacks.
    """

    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.rpm = requests_per_minute
        # Only health checks are truly exempt
        self.exempt_paths = {
            "/health",
            "/.well-known/health",
            "/api/health",
        }
        # Stricter limits for auth endpoints (to prevent brute force)
        self.auth_paths = {
            "/api/auth/login",
            "/api/auth/register",
        }
        self.auth_rpm = 5  # Only 5 login/register attempts per minute

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip rate limiting for health checks only
        if request.url.path in self.exempt_paths:
            return await call_next(request)

        # Get client identifier (IP address)
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            client_ip = forwarded_for.split(",")[0].strip()
        else:
            client_ip = request.client.host if request.client else "unknown"

        identifier = f"ip:{client_ip}"

        # Determine rate limit based on path
        is_auth_endpoint = request.url.path in self.auth_paths
        max_rpm = self.auth_rpm if is_auth_endpoint else self.rpm

        # Try Redis first, fallback to in-memory
        try:
            from ...db.redis_client import check_rate_limit, is_redis_configured

            if is_redis_configured():
                # Use Redis rate limiting
                allowed, remaining = check_rate_limit(identifier, max_rpm, 60)
            else:
                # Fallback to in-memory rate limiting
                logger.warning("Redis unavailable, using in-memory rate limiter")
                allowed, remaining = _memory_limiter.check_rate_limit(identifier, max_rpm, 60)
        except Exception as e:
            # If Redis fails, use in-memory fallback
            logger.error(f"Rate limit check failed: {e}, using in-memory fallback")
            allowed, remaining = _memory_limiter.check_rate_limit(identifier, max_rpm, 60)

        if not allowed:
            endpoint_type = "auth" if is_auth_endpoint else "api"
            logger.warning(f"Rate limit exceeded for {identifier} on {endpoint_type} endpoint: {request.url.path}")
            # Return Response directly instead of raising HTTPException
            return Response(
                content='{"detail":"Rate limit exceeded. Please wait before making more requests."}',
                status_code=429,
                media_type="application/json",
                headers={
                    "X-RateLimit-Limit": str(max_rpm),
                    "X-RateLimit-Remaining": "0",
                    "Retry-After": "60"
                }
            )

        # Continue with request
        response = await call_next(request)

        # Add rate limit headers
        response.headers["X-RateLimit-Limit"] = str(max_rpm)
        response.headers["X-RateLimit-Remaining"] = str(remaining)

        return response
