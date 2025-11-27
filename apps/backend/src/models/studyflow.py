"""
Studyflow Model - Data model for learning studyflows
Phase 4.0: Studyflow Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID


class Studyflow:
    """
    Studyflow entity representing a learning path step within a module.

    Attributes:
        id: Unique identifier (UUID)
        module_id: UUID of the parent module
        title: Studyflow title (3-100 chars)
        description: Optional description (max 500 chars)
        order: Position in the module (positive int, unique per module)
        is_active: Whether studyflow is active (default True)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    def __init__(
        self,
        id: UUID,
        module_id: UUID,
        title: str,
        description: Optional[str] = None,
        order: int = 1,
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.module_id = module_id
        self.title = title
        self.description = description
        self.order = order
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Studyflow(id={self.id}, title={self.title}, module_id={self.module_id}, order={self.order})"
