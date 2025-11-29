"""
DevOpsHub Backend - Main Application
Phase FAS 4.3 - PostgreSQL + Redis integration

FastAPI application with:
- PostgreSQL database (with SQLite fallback)
- Redis caching and sessions
- CORS configuration
- Health endpoints
- Lifespan management
"""

import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ==============================================================================
# LIFESPAN MANAGEMENT
# ==============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan handler.
    Initializes and cleans up resources.
    """
    # -------------------------------------------------------------------------
    # STARTUP
    # -------------------------------------------------------------------------
    logger.info("🚀 Starting DevOpsHub Backend...")
    
    # Initialize PostgreSQL
    try:
        from .db.database import init_db, is_postgresql, check_db_health
        
        init_db()
        
        health = check_db_health()
        if health["connected"]:
            db_type = "PostgreSQL" if is_postgresql() else "SQLite"
            logger.info(f"🗄️ {db_type} connected: {health.get('version', 'unknown')}")
        else:
            logger.warning(f"⚠️ Database connection issue: {health.get('error', 'unknown')}")
            
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
    
    # Initialize Redis
    try:
        from .db.redis_client import get_redis_client, is_redis_configured, redis_health_check
        
        if is_redis_configured():
            client = get_redis_client()
            if client:
                health = redis_health_check()
                logger.info(f"🔴 Redis connected: v{health.get('version', 'unknown')}")
            else:
                logger.warning("⚠️ Redis configured but connection failed")
        else:
            logger.info("📝 Redis not configured - using in-memory fallback")
            
    except Exception as e:
        logger.warning(f"⚠️ Redis initialization skipped: {e}")
    
    # Seed data if needed
    try:
        from .db.seeds import seed_bootcamp_data
        seed_bootcamp_data()
        logger.info("📚 Bootcamp data seeded")
    except Exception as e:
        logger.warning(f"⚠️ Seed data skipped: {e}")
    
    logger.info("✅ DevOpsHub Backend ready!")
    
    yield
    
    # -------------------------------------------------------------------------
    # SHUTDOWN
    # -------------------------------------------------------------------------
    logger.info("🛑 Shutting down DevOpsHub Backend...")
    
    # Close Redis
    try:
        from .db.redis_client import close_redis
        close_redis()
        logger.info("Redis connection closed")
    except:
        pass
    
    # Dispose database
    try:
        from .db.database import dispose_db
        dispose_db()
        logger.info("Database connections disposed")
    except:
        pass
    
    logger.info("👋 Goodbye!")


# ==============================================================================
# APPLICATION FACTORY
# ==============================================================================

def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    
    app = FastAPI(
        title="DevOpsHub API",
        description="Backend API for DevOpsHub Learning Platform",
        version="2.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )
    
    # -------------------------------------------------------------------------
    # CORS
    # -------------------------------------------------------------------------
    
    # Get allowed origins from environment
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    allowed_origins = [
        frontend_url,
        "http://localhost:3000",
        "http://localhost:3001",
        "https://saasprojekt.netlify.app",
        "https://*.netlify.app",
    ]
    
    # Add any additional origins from environment
    extra_origins = os.getenv("CORS_ORIGINS", "")
    if extra_origins:
        allowed_origins.extend(extra_origins.split(","))
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Total-Count", "X-Phase"],
    )
    
    # -------------------------------------------------------------------------
    # ROUTES
    # -------------------------------------------------------------------------
    
    # Import and register routers
    from .api.routes import (
        auth,
        modules,
        tasks,
        labs,
        progress,
        studyflow,
        dashboard,
        search,
        users,
        admin,
    )
    
    # API v1 routes
    app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
    app.include_router(modules.router, prefix="/api/modules", tags=["Modules"])
    app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
    app.include_router(labs.router, prefix="/api/labs", tags=["Labs"])
    app.include_router(progress.router, prefix="/api/progress", tags=["Progress"])
    app.include_router(studyflow.router, prefix="/api/studyflow", tags=["Studyflow"])
    app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
    app.include_router(search.router, prefix="/api/search", tags=["Search"])
    app.include_router(users.router, prefix="/api/users", tags=["Users"])
    app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
    
    # -------------------------------------------------------------------------
    # HEALTH ENDPOINTS
    # -------------------------------------------------------------------------
    
    @app.get("/", tags=["Health"])
    async def root():
        """Root endpoint - basic health check."""
        return {
            "status": "ok",
            "service": "DevOpsHub API",
            "version": "2.0.0"
        }
    
    @app.get("/health", tags=["Health"])
    async def health_check():
        """Comprehensive health check."""
        from .db.database import check_db_health
        from .db.redis_client import redis_health_check, is_redis_configured
        
        db_health = check_db_health()
        redis_health = redis_health_check() if is_redis_configured() else {"status": "not_configured"}
        
        overall_status = "healthy"
        if db_health.get("status") != "healthy":
            overall_status = "degraded"
        
        return {
            "status": overall_status,
            "service": "DevOpsHub API",
            "version": "2.0.0",
            "components": {
                "database": db_health,
                "redis": redis_health,
            }
        }
    
    @app.get("/api/health", tags=["Health"])
    async def api_health():
        """API health check."""
        return {"status": "ok", "api": "v1"}
    
    # -------------------------------------------------------------------------
    # ERROR HANDLERS
    # -------------------------------------------------------------------------
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """Global exception handler."""
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal server error",
                "detail": str(exc) if os.getenv("DEBUG", "false").lower() == "true" else None
            }
        )
    
    return app


# ==============================================================================
# APPLICATION INSTANCE
# ==============================================================================

app = create_app()


# ==============================================================================
# DEVELOPMENT SERVER
# ==============================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "false").lower() == "true",
        log_level="info",
    )
