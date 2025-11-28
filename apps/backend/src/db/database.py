"""
Database Configuration - PostgreSQL with SQLAlchemy
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Handle Railway's postgres:// vs postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Async URL for asyncpg
ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1) if DATABASE_URL else ""

# SQLAlchemy Base
Base = declarative_base()

# Sync engine (for migrations and admin tasks)
engine = create_engine(DATABASE_URL, echo=False) if DATABASE_URL else None

# Async engine (for API requests)
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=False) if ASYNC_DATABASE_URL else None

# Session factories
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) if engine else None
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
) if async_engine else None


def get_db():
    """Dependency for sync database sessions"""
    if not SessionLocal:
        raise RuntimeError("Database not configured. Set DATABASE_URL environment variable.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_db():
    """Dependency for async database sessions"""
    if not AsyncSessionLocal:
        raise RuntimeError("Database not configured. Set DATABASE_URL environment variable.")
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@contextmanager
def get_db_context():
    """Context manager for database sessions outside of FastAPI"""
    if not SessionLocal:
        raise RuntimeError("Database not configured. Set DATABASE_URL environment variable.")
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def is_db_configured() -> bool:
    """Check if database is configured"""
    return bool(DATABASE_URL)


def init_db():
    """Initialize database tables"""
    if engine:
        # Import models to register them with Base.metadata
        # This is required before create_all() so SQLAlchemy knows about all tables
        from . import models  # noqa: F401
        Base.metadata.create_all(bind=engine)
