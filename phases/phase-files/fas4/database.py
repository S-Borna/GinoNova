"""
Database Configuration - PostgreSQL + SQLite Fallback
Phase FAS 4.2 - PostgreSQL persistence

Features:
- Automatic PostgreSQL detection from DATABASE_URL
- SQLite fallback for local development
- Connection pooling
- Health check endpoint
- Migration support ready
"""

import os
import logging
from typing import Optional
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool, StaticPool

logger = logging.getLogger(__name__)

# ==============================================================================
# DATABASE URL DETECTION
# ==============================================================================

def get_database_url() -> str:
    """
    Get database URL from environment or use SQLite fallback.
    Handles Railway's postgres:// vs postgresql:// URL format.
    """
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        # Railway uses postgres:// but SQLAlchemy needs postgresql://
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        
        logger.info("🗄️ PostgreSQL database detected")
        return database_url
    
    # Fallback to SQLite for local development
    sqlite_path = os.getenv("SQLITE_PATH", "./devopshub.db")
    logger.info(f"📁 Using SQLite fallback: {sqlite_path}")
    return f"sqlite:///{sqlite_path}"


def is_postgresql() -> bool:
    """Check if using PostgreSQL."""
    url = get_database_url()
    return url.startswith("postgresql://")


# ==============================================================================
# ENGINE CONFIGURATION
# ==============================================================================

def create_db_engine():
    """
    Create SQLAlchemy engine with appropriate settings.
    """
    database_url = get_database_url()
    
    if is_postgresql():
        # PostgreSQL configuration
        engine = create_engine(
            database_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800,  # Recycle connections after 30 min
            pool_pre_ping=True,  # Verify connections before use
            echo=os.getenv("SQL_ECHO", "false").lower() == "true",
        )
    else:
        # SQLite configuration
        engine = create_engine(
            database_url,
            poolclass=StaticPool,  # Single connection for SQLite
            connect_args={"check_same_thread": False},
            echo=os.getenv("SQL_ECHO", "false").lower() == "true",
        )
    
    return engine


# Global engine and session factory
_engine = None
_SessionLocal = None


def get_engine():
    """Get or create database engine."""
    global _engine
    if _engine is None:
        _engine = create_db_engine()
    return _engine


def get_session_factory():
    """Get or create session factory."""
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=get_engine()
        )
    return _SessionLocal


# ==============================================================================
# SESSION MANAGEMENT
# ==============================================================================

def get_db() -> Session:
    """
    Get database session.
    Use as dependency in FastAPI routes.
    """
    SessionLocal = get_session_factory()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """
    Context manager for database sessions.
    Use in background tasks or scripts.
    """
    SessionLocal = get_session_factory()
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


# ==============================================================================
# INITIALIZATION
# ==============================================================================

def init_db():
    """
    Initialize database - create tables if needed.
    Call this on application startup.
    """
    from .models import Base  # Import your models
    
    engine = get_engine()
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    logger.info("✅ Database tables initialized")
    
    return engine


def dispose_db():
    """
    Dispose database connections.
    Call this on application shutdown.
    """
    global _engine, _SessionLocal
    
    if _engine:
        _engine.dispose()
        _engine = None
        _SessionLocal = None
        logger.info("Database connections disposed")


# ==============================================================================
# HEALTH CHECK
# ==============================================================================

def check_db_health() -> dict:
    """
    Check database health status.
    """
    try:
        engine = get_engine()
        
        with engine.connect() as conn:
            # Simple query to check connection
            if is_postgresql():
                result = conn.execute(text("SELECT version()"))
                version = result.scalar()
            else:
                result = conn.execute(text("SELECT sqlite_version()"))
                version = f"SQLite {result.scalar()}"
        
        return {
            "status": "healthy",
            "database": "postgresql" if is_postgresql() else "sqlite",
            "version": version,
            "connected": True
        }
        
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return {
            "status": "unhealthy",
            "database": "postgresql" if is_postgresql() else "sqlite",
            "connected": False,
            "error": str(e)
        }


# ==============================================================================
# MIGRATION HELPERS
# ==============================================================================

def run_migrations():
    """
    Run database migrations.
    Placeholder for Alembic integration.
    """
    # TODO: Integrate with Alembic
    # from alembic.config import Config
    # from alembic import command
    # 
    # alembic_cfg = Config("alembic.ini")
    # command.upgrade(alembic_cfg, "head")
    
    logger.info("Migrations placeholder - implement with Alembic")


def create_migration(message: str):
    """
    Create new migration.
    Placeholder for Alembic integration.
    """
    # TODO: Integrate with Alembic
    # from alembic.config import Config
    # from alembic import command
    # 
    # alembic_cfg = Config("alembic.ini")
    # command.revision(alembic_cfg, message=message, autogenerate=True)
    
    logger.info(f"Migration creation placeholder: {message}")
