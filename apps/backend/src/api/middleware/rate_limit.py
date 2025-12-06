"""
Rate Limit Middleware - Phase 29
Protects API from abuse using Redis-based rate limiting.
"""
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging

logger = logging.getLogger(__name__)


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Rate limiting middleware using Redis.
    Falls back to allowing requests if Redis is unavailable.
    """

    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.rpm = requests_per_minute
        self.exempt_paths = {
            "/health",
            "/.well-known/health",
            "/api/health",
            "/api/auth/login",
            "/api/auth/register",
            "/api/auth/refresh",
            "/api/auth/me",
            "/api/auth/status",
            "/api/auth/google",
            "/api/auth/github",
            "/api/auth/discord",
        }

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip rate limiting for health checks
        if request.url.path in self.exempt_paths:
            return await call_next(request)

        # Import here to avoid circular imports
        from ...db.redis_client import check_rate_limit, is_redis_configured

        # If Redis not configured, allow all requests
        if not is_redis_configured():
            return await call_next(request)

        # Get client identifier (IP or user)
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            client_ip = forwarded_for.split(",")[0].strip()
        else:
            client_ip = request.client.host if request.client else "unknown"

        identifier = f"ip:{client_ip}"

        # Check rate limit
        allowed, remaining = check_rate_limit(identifier, self.rpm, 60)

        if not allowed:
            logger.warning(f"Rate limit exceeded for {identifier}")
            # Return Response directly instead of raising HTTPException
            # BaseHTTPMiddleware has issues with exception propagation
            return Response(
                content='{"detail":"Rate limit exceeded. Please wait before making more requests."}',
                status_code=429,
                media_type="application/json",
                headers={
                    "X-RateLimit-Limit": str(self.rpm),
                    "X-RateLimit-Remaining": "0",
                    "Retry-After": "60"
                }
            )

        # Continue with request
        response = await call_next(request)

        # Add rate limit headers
        response.headers["X-RateLimit-Limit"] = str(self.rpm)
        response.headers["X-RateLimit-Remaining"] = str(remaining)

        return response
