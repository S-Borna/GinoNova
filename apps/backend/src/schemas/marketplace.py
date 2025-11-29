"""
Marketplace Schemas
Phase 13 - Marketplace & Extensions System

Pydantic models for:
- Creator profiles
- Marketplace items
- Installations
- Reviews
"""
from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==============================================================================
# ENUMS
# ==============================================================================

ItemType = Literal["module_pack", "task_pack", "bootcamp", "addon"]
ItemStatus = Literal["draft", "review", "published", "retired"]
ReviewStatus = Literal["pending", "approved", "rejected"]


# ==============================================================================
# CREATOR
# ==============================================================================

class CreatorBase(BaseModel):
    """Base creator model"""
    bio: Optional[str] = None
    website: Optional[str] = None
    github_url: Optional[str] = None
    specialties: List[str] = []


class CreatorCreate(CreatorBase):
    """Schema for creating a creator profile"""
    user_id: UUID


class CreatorPublic(CreatorBase):
    """Public creator profile"""
    id: UUID
    user_id: UUID
    display_name: str = ""
    avatar_url: Optional[str] = None
    rating: float = 0.0
    total_items: int = 0
    total_installs: int = 0
    is_verified: bool = False
    created_at: datetime

    class Config:
        from_attributes = True


class CreatorInDB(CreatorBase):
    """Internal creator model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    display_name: str = ""
    avatar_url: Optional[str] = None
    rating: float = 0.0
    total_items: int = 0
    total_installs: int = 0
    is_verified: bool = False
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# MARKETPLACE ITEM
# ==============================================================================

class MarketplaceItemBase(BaseModel):
    """Base marketplace item"""
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=2000)
    short_description: Optional[str] = Field(None, max_length=200)
    type: ItemType = "module_pack"

    # Pricing
    price_cents: int = Field(default=0, ge=0)  # 0 = free
    is_free: bool = True

    # Metadata
    tags: List[str] = []
    difficulty: str = "intermediate"
    estimated_hours: float = 10.0

    # Content counts
    modules_count: int = 0
    tasks_count: int = 0

    # Preview
    thumbnail_url: Optional[str] = None
    preview_video_url: Optional[str] = None


class MarketplaceItemCreate(MarketplaceItemBase):
    """Schema for creating a marketplace item"""
    content_manifest: Optional[dict] = None  # JSON manifest of included content


class MarketplaceItemUpdate(BaseModel):
    """Schema for updating a marketplace item"""
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=2000)
    short_description: Optional[str] = Field(None, max_length=200)
    price_cents: Optional[int] = Field(None, ge=0)
    is_free: Optional[bool] = None
    tags: Optional[List[str]] = None
    difficulty: Optional[str] = None
    estimated_hours: Optional[float] = None
    thumbnail_url: Optional[str] = None
    preview_video_url: Optional[str] = None
    content_manifest: Optional[dict] = None


class MarketplaceItemPublic(MarketplaceItemBase):
    """Public marketplace item view"""
    id: UUID
    creator_id: UUID
    creator_name: str = ""

    # Versioning
    version: str = "1.0.0"

    # Status
    status: ItemStatus = "draft"

    # Stats
    installs_count: int = 0
    rating: float = 0.0
    reviews_count: int = 0

    # Dates
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MarketplaceItemInDB(MarketplaceItemBase):
    """Internal marketplace item model"""
    id: UUID = Field(default_factory=uuid4)
    creator_id: UUID
    creator_name: str = ""

    # Versioning
    version: str = "1.0.0"

    # Status
    status: ItemStatus = "draft"

    # Stats
    installs_count: int = 0
    rating: float = 0.0
    reviews_count: int = 0

    # Content
    content_manifest: Optional[dict] = None

    # Flags
    is_featured: bool = False
    is_active: bool = True

    # Dates
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    published_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==============================================================================
# INSTALLATION
# ==============================================================================

class InstallationBase(BaseModel):
    """Base installation model"""
    item_id: UUID
    version: str = "1.0.0"


class InstallationCreate(InstallationBase):
    """Schema for creating an installation"""
    tenant_id: Optional[UUID] = None  # For org installations


class InstallationPublic(InstallationBase):
    """Public installation view"""
    id: UUID
    user_id: UUID
    tenant_id: Optional[UUID] = None

    # Item info
    item_title: str = ""
    item_type: ItemType = "module_pack"

    # Status
    is_active: bool = True

    # Dates
    installed_at: datetime
    updated_at: Optional[datetime] = None
    uninstalled_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class InstallationInDB(InstallationBase):
    """Internal installation model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    tenant_id: Optional[UUID] = None

    # Item info
    item_title: str = ""
    item_type: ItemType = "module_pack"

    # Status
    is_active: bool = True

    # Dates
    installed_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    uninstalled_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==============================================================================
# REVIEW (Admin review of items)
# ==============================================================================

class ItemReviewBase(BaseModel):
    """Base item review model"""
    notes: Optional[str] = Field(None, max_length=1000)


class ItemReviewCreate(ItemReviewBase):
    """Schema for creating an item review"""
    item_id: UUID
    status: ReviewStatus = "pending"


class ItemReviewPublic(ItemReviewBase):
    """Public item review view"""
    id: UUID
    item_id: UUID
    admin_id: UUID
    status: ReviewStatus
    reviewed_at: datetime

    class Config:
        from_attributes = True


class ItemReviewInDB(ItemReviewBase):
    """Internal item review model"""
    id: UUID = Field(default_factory=uuid4)
    item_id: UUID
    admin_id: UUID
    status: ReviewStatus = "pending"
    reviewed_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# USER REVIEWS (User ratings of items)
# ==============================================================================

class UserReviewBase(BaseModel):
    """Base user review model"""
    rating: int = Field(..., ge=1, le=5)
    title: Optional[str] = Field(None, max_length=100)
    comment: Optional[str] = Field(None, max_length=1000)


class UserReviewCreate(UserReviewBase):
    """Schema for creating a user review"""
    item_id: UUID


class UserReviewPublic(UserReviewBase):
    """Public user review view"""
    id: UUID
    item_id: UUID
    user_id: UUID
    user_display_name: str = ""
    created_at: datetime
    is_verified_purchase: bool = False

    class Config:
        from_attributes = True


class UserReviewInDB(UserReviewBase):
    """Internal user review model"""
    id: UUID = Field(default_factory=uuid4)
    item_id: UUID
    user_id: UUID
    user_display_name: str = ""
    is_verified_purchase: bool = False
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
