"""
Error Handler Middleware - Phase 29
Global exception handling with structured error responses.
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging
import traceback
import uuid

logger = logging.getLogger(__name__)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """
    Global error handler that catches unhandled exceptions.
    Logs full traceback but returns safe error to client.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException:
            # Re-raise HTTPExceptions so FastAPI handles them properly
            # This includes 401, 403, 404, 429, etc.
            raise
        except Exception as e:
            # Generate unique request ID for tracking
            request_id = str(uuid.uuid4())[:8]

            # Log full error with traceback
            logger.error(
                f"Unhandled error [{request_id}] on {request.method} {request.url.path}: "
                f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
            )

            # Return safe error to client
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "An internal error occurred. Please try again.",
                    "request_id": request_id,
                    "type": "internal_error"
                }
            )
