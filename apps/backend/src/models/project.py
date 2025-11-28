"""
Project Model - Data model for module projects
Phase C.1: Seed Bootcamp v3.0 Content (Redo)

Each module has one capstone project with deliverables.
Projects are practical implementations that demonstrate mastery.
"""
from datetime import datetime
from typing import Optional
from uuid import UUID


class Project:
    """
    Project entity representing a capstone project within a module.

    Attributes:
        id: Unique identifier (UUID)
        module_id: UUID of the parent module
        title: Project title (e.g., "Development Environment as Code")
        slug: URL-friendly identifier
        description: Project overview
        requirements: Markdown content with detailed requirements
        deliverables: List of deliverables to submit
        xp_reward: XP earned on completion (projects give more XP)
        estimated_hours: Expected time to complete
        is_active: Whether project is active (default True)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    def __init__(
        self,
        id: UUID,
        module_id: UUID,
        title: str,
        slug: str,
        description: Optional[str] = None,
        requirements: Optional[str] = None,
        deliverables: Optional[list[str]] = None,
        xp_reward: int = 500,
        estimated_hours: float = 5.0,
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.module_id = module_id
        self.title = title
        self.slug = slug
        self.description = description
        self.requirements = requirements
        self.deliverables = deliverables or []
        self.xp_reward = xp_reward
        self.estimated_hours = estimated_hours
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Project(id={self.id}, title={self.title}, module_id={self.module_id})"
