"""
Lab Model - Data model for hands-on labs
Phase C.1: Seed Bootcamp v3.0 Content (Redo)

Labs are practical exercises within modules.
Each module has 4-6 labs with estimated hours and expected outcomes.
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID


class Lab:
    """
    Lab entity representing a hands-on lab within a module.

    Attributes:
        id: Unique identifier (UUID)
        module_id: UUID of the parent module
        title: Lab title (e.g., "Lab 1.1: Terminal Power User Setup")
        slug: URL-friendly identifier
        description: Brief description of the lab
        estimated_hours: Expected time to complete (e.g., 2.0)
        instructions: Markdown content with lab instructions
        expected_outcomes: List of outcomes to check off
        hints: List of optional hints
        difficulty: One of: easy, medium, hard
        order_index: Display order within module
        xp_reward: XP earned on completion
        is_active: Whether lab is active (default True)
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
        estimated_hours: float = 2.0,
        instructions: Optional[str] = None,
        expected_outcomes: Optional[list[str]] = None,
        hints: Optional[list[str]] = None,
        difficulty: Literal["easy", "medium", "hard"] = "medium",
        order_index: int = 0,
        xp_reward: int = 100,
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.module_id = module_id
        self.title = title
        self.slug = slug
        self.description = description
        self.estimated_hours = estimated_hours
        self.instructions = instructions
        self.expected_outcomes = expected_outcomes or []
        self.hints = hints or []
        self.difficulty = difficulty
        self.order_index = order_index
        self.xp_reward = xp_reward
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Lab(id={self.id}, title={self.title}, module_id={self.module_id})"
