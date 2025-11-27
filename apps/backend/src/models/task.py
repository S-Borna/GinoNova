"""
Task Model - Data model for learning tasks
Phase 3.0: Tasks Foundation
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID


class Task:
    """
    Task entity representing a learning task within a module.

    Attributes:
        id: Unique identifier (UUID)
        module_id: UUID of the parent module
        title: Task title (3-100 chars, unique per module)
        description: Optional description (max 500 chars)
        difficulty: One of: easy, medium, hard
        is_active: Whether task is active (default True)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    def __init__(
        self,
        id: UUID,
        module_id: UUID,
        title: str,
        description: Optional[str] = None,
        difficulty: Literal["easy", "medium", "hard"] = "medium",
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.module_id = module_id
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title={self.title}, module_id={self.module_id}, difficulty={self.difficulty})"
