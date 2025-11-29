"""
Community Schemas
Phase 16 - Community & Social Layer

Pydantic models for:
- Discussion threads
- Comments
- Reactions
- Activity feeds
"""
from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==============================================================================
# ENUMS
# ==============================================================================

ThreadStatus = Literal["open", "solved", "locked", "closed"]
ReactionType = Literal["upvote", "fire", "question", "solved", "helpful"]
ActivityType = Literal[
    "thread_created",
    "comment_created",
    "thread_solved",
    "admin_announcement",
    "reaction_added",
]


# ==============================================================================
# THREAD
# ==============================================================================

class ThreadBase(BaseModel):
    """Base thread model"""
    title: str = Field(..., min_length=5, max_length=200)
    body_markdown: str = Field(..., min_length=10, max_length=10000)

    # Context (optional)
    module_slug: Optional[str] = None
    task_id: Optional[UUID] = None

    # Tags
    tags: List[str] = []


class ThreadCreate(ThreadBase):
    """Schema for creating a thread"""
    pass


class ThreadUpdate(BaseModel):
    """Schema for updating a thread"""
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    body_markdown: Optional[str] = Field(None, min_length=10, max_length=10000)
    tags: Optional[List[str]] = None
    status: Optional[ThreadStatus] = None


class ThreadPublic(ThreadBase):
    """Public thread view"""
    id: UUID
    user_id: UUID
    author_name: str = ""
    author_avatar: Optional[str] = None

    # Status
    status: ThreadStatus = "open"

    # Stats
    comments_count: int = 0
    upvotes_count: int = 0
    views_count: int = 0

    # Dates
    created_at: datetime
    updated_at: datetime
    solved_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ThreadInDB(ThreadBase):
    """Internal thread model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    author_name: str = ""
    author_avatar: Optional[str] = None

    # Status
    status: ThreadStatus = "open"

    # Stats
    comments_count: int = 0
    upvotes_count: int = 0
    views_count: int = 0

    # Flags
    is_pinned: bool = False
    is_active: bool = True

    # Dates
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    solved_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==============================================================================
# COMMENT
# ==============================================================================

class CommentBase(BaseModel):
    """Base comment model"""
    body_markdown: str = Field(..., min_length=1, max_length=5000)


class CommentCreate(CommentBase):
    """Schema for creating a comment"""
    thread_id: UUID
    parent_id: Optional[UUID] = None  # For replies


class CommentUpdate(BaseModel):
    """Schema for updating a comment"""
    body_markdown: Optional[str] = Field(None, min_length=1, max_length=5000)


class CommentPublic(CommentBase):
    """Public comment view"""
    id: UUID
    thread_id: UUID
    user_id: UUID
    parent_id: Optional[UUID] = None

    # Author info
    author_name: str = ""
    author_avatar: Optional[str] = None

    # Stats
    upvotes_count: int = 0
    is_solution: bool = False

    # Dates
    created_at: datetime
    updated_at: datetime

    # Nested replies (optional)
    replies: List["CommentPublic"] = []

    class Config:
        from_attributes = True


class CommentInDB(CommentBase):
    """Internal comment model"""
    id: UUID = Field(default_factory=uuid4)
    thread_id: UUID
    user_id: UUID
    parent_id: Optional[UUID] = None

    # Author info
    author_name: str = ""
    author_avatar: Optional[str] = None

    # Stats
    upvotes_count: int = 0
    is_solution: bool = False

    # Flags
    is_active: bool = True

    # Dates
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# REACTION
# ==============================================================================

class ReactionCreate(BaseModel):
    """Schema for creating a reaction"""
    target_type: Literal["thread", "comment"]
    target_id: UUID
    reaction: ReactionType


class ReactionPublic(BaseModel):
    """Public reaction view"""
    id: UUID
    target_type: str
    target_id: UUID
    user_id: UUID
    reaction: ReactionType
    created_at: datetime

    class Config:
        from_attributes = True


class ReactionInDB(BaseModel):
    """Internal reaction model"""
    id: UUID = Field(default_factory=uuid4)
    target_type: str
    target_id: UUID
    user_id: UUID
    reaction: ReactionType
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# ACTIVITY FEED
# ==============================================================================

class ActivityPublic(BaseModel):
    """Public activity feed item"""
    id: UUID
    type: ActivityType
    user_id: Optional[UUID] = None

    # Context
    thread_id: Optional[UUID] = None
    thread_title: Optional[str] = None
    comment_id: Optional[UUID] = None

    # Display
    message: str = ""

    # Dates
    created_at: datetime

    class Config:
        from_attributes = True


class ActivityInDB(BaseModel):
    """Internal activity model"""
    id: UUID = Field(default_factory=uuid4)
    type: ActivityType
    user_id: Optional[UUID] = None

    # Context
    thread_id: Optional[UUID] = None
    thread_title: Optional[str] = None
    comment_id: Optional[UUID] = None

    # Payload
    payload: Optional[dict] = None
    message: str = ""

    # Dates
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# Update forward refs for nested comments
CommentPublic.model_rebuild()
