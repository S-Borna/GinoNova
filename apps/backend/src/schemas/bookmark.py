"""
Bookmark schemas - Pydantic models for task bookmarking
PROMPT 4: Sidebar Bookmark System
"""
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class BookmarkCreate(BaseModel):
    """Schema for creating a bookmark"""
    task_id: UUID


class BookmarkResponse(BaseModel):
    """Schema for bookmark response with task info"""
    id: UUID
    user_id: UUID
    task_id: UUID
    created_at: datetime
    
    # Include task info for display
    task_title: str
    module_slug: str
    module_name: str

    class Config:
        from_attributes = True


class BookmarkList(BaseModel):
    """Schema for list of bookmarks"""
    bookmarks: list[BookmarkResponse]
    total: int


class BookmarkCheck(BaseModel):
    """Schema for checking bookmark status"""
    is_bookmarked: bool
