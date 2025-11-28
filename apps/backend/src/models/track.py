"""
Track Model - Data model for bootcamp tracks
Phase C.1: Seed Bootcamp v3.0 Content (Redo)

Bootcamp v3.0 has 4 tracks:
- Track 1: Foundation (Modules 01-05)
- Track 2: Cloud & Infrastructure (Modules 06-09)
- Track 3: Containers & Orchestration (Modules 10-12)
- Track 4: Platform Engineering (Modules 13-15)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID


class Track:
    """
    Track entity representing a learning track in Bootcamp v3.0.

    Attributes:
        id: Unique identifier (UUID)
        name: Track name (e.g., "Foundation")
        slug: URL-friendly identifier (e.g., "foundation")
        description: Track description
        color: Hex color code for UI (e.g., "#6366f1")
        icon: Emoji or icon identifier
        order_index: Display order (1-4)
        is_active: Whether track is active (default True)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
    """

    def __init__(
        self,
        id: UUID,
        name: str,
        slug: str,
        description: str,
        color: str,
        icon: str,
        order_index: int,
        is_active: bool = True,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.slug = slug
        self.description = description
        self.color = color
        self.icon = icon
        self.order_index = order_index
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        return f"Track(id={self.id}, name={self.name}, order_index={self.order_index})"
