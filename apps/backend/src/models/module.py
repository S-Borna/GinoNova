"""
Module Model - Data model for learning modules
Phase 2.0: Modules Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID


class Module:
    """
    Module entity representing a learning module in the system.

    Attributes:
        id: Unique identifier (UUID)
        name: Module name (2-50 chars, unique)
        description: Optional description (max 300 chars)
        is_active: Whether module is active (default True)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    def __init__(
        self,
        id: UUID,
        name: str,
        description: Optional[str] = None,
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Module(id={self.id}, name={self.name}, is_active={self.is_active})"
