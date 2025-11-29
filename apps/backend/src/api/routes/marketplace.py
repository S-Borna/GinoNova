"""
Marketplace API Routes
Phase 13 - Marketplace & Extensions System

Endpoints for:
- Browsing marketplace items
- Creator management
- Installing/uninstalling packs
- Reviews and ratings
"""
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Response, HTTPException, status
from pydantic import BaseModel

from ...schemas.marketplace import (
    # Creator
    CreatorPublic, CreatorInDB,
    # Items
    MarketplaceItemPublic, MarketplaceItemInDB,
    ItemType,
    # Installations
    InstallationCreate, InstallationPublic, InstallationInDB,
    # Reviews
    UserReviewCreate, UserReviewPublic, UserReviewInDB,
)


router = APIRouter(prefix="/marketplace", tags=["marketplace"])

PHASE_VERSION = "13.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# IN-MEMORY STORAGE (Will be PostgreSQL in production)
# ==============================================================================

_creators_db: dict[UUID, CreatorInDB] = {}
_items_db: dict[UUID, MarketplaceItemInDB] = {}
_installations_db: dict[UUID, InstallationInDB] = {}
_user_reviews_db: dict[UUID, UserReviewInDB] = {}


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def _get_creator_by_user(user_id: UUID) -> Optional[CreatorInDB]:
    """Get creator profile by user ID"""
    for creator in _creators_db.values():
        if creator.user_id == user_id:
            return creator
    return None


def _seed_sample_items():
    """Seed sample marketplace items for demo"""
    if _items_db:
        return  # Already seeded

    # Create a sample creator
    sample_creator_id = uuid4()
    sample_creator = CreatorInDB(
        id=sample_creator_id,
        user_id=uuid4(),
        display_name="DevOpsHub Official",
        bio="Official DevOpsHub content packs",
        rating=4.8,
        total_items=3,
        is_verified=True,
    )
    _creators_db[sample_creator_id] = sample_creator

    # Sample items
    sample_items = [
        {
            "title": "Kubernetes Mastery Pack",
            "short_description": "Complete K8s training from pods to production",
            "description": "Master Kubernetes with this comprehensive pack covering pods, deployments, services, ingress, helm, and production best practices.",
            "type": "module_pack",
            "price_cents": 4999,
            "is_free": False,
            "tags": ["kubernetes", "k8s", "containers", "orchestration"],
            "difficulty": "advanced",
            "estimated_hours": 40,
            "modules_count": 8,
            "tasks_count": 45,
            "status": "published",
        },
        {
            "title": "CI/CD Pipeline Fundamentals",
            "short_description": "Build automated pipelines with GitHub Actions & GitLab CI",
            "description": "Learn to build robust CI/CD pipelines from scratch. Covers GitHub Actions, GitLab CI, Jenkins basics, and deployment strategies.",
            "type": "module_pack",
            "price_cents": 0,
            "is_free": True,
            "tags": ["cicd", "github-actions", "gitlab-ci", "automation"],
            "difficulty": "intermediate",
            "estimated_hours": 20,
            "modules_count": 5,
            "tasks_count": 28,
            "status": "published",
        },
        {
            "title": "Cloud Security Essentials",
            "short_description": "Secure your cloud infrastructure",
            "description": "Essential security practices for AWS, GCP, and Azure. Covers IAM, network security, secrets management, and compliance.",
            "type": "module_pack",
            "price_cents": 2999,
            "is_free": False,
            "tags": ["security", "cloud", "aws", "compliance"],
            "difficulty": "intermediate",
            "estimated_hours": 25,
            "modules_count": 6,
            "tasks_count": 32,
            "status": "published",
        },
    ]

    for item_data in sample_items:
        item_id = uuid4()
        item = MarketplaceItemInDB(
            id=item_id,
            creator_id=sample_creator_id,
            creator_name=sample_creator.display_name,
            installs_count=50 + hash(item_data["title"]) % 200,
            rating=4.0 + (hash(item_data["title"]) % 10) / 10,
            reviews_count=10 + hash(item_data["title"]) % 30,
            published_at=datetime.utcnow(),
            **item_data,
        )
        _items_db[item_id] = item


# ==============================================================================
# RESPONSE SCHEMAS
# ==============================================================================

class MarketplaceStatusResponse(BaseModel):
    """Marketplace status response"""
    status: str = "operational"
    phase: str = PHASE_VERSION
    total_items: int = 0
    total_creators: int = 0
    features: List[str]


class MarketplaceListResponse(BaseModel):
    """Paginated marketplace items response"""
    items: List[MarketplaceItemPublic]
    total: int
    page: int
    per_page: int
    has_more: bool


class InstallationResponse(BaseModel):
    """Installation response"""
    success: bool
    message: str
    installation: Optional[InstallationPublic] = None


# ==============================================================================
# MARKETPLACE ENDPOINTS
# ==============================================================================

@router.get("/status", response_model=MarketplaceStatusResponse)
def marketplace_status(response: Response):
    """
    Get marketplace system status.
    """
    add_phase_header(response)
    _seed_sample_items()  # Ensure sample data exists

    return MarketplaceStatusResponse(
        status="operational",
        phase=PHASE_VERSION,
        total_items=len(_items_db),
        total_creators=len(_creators_db),
        features=[
            "browse_items",
            "search_items",
            "view_item_details",
            "install_items",
            "user_reviews",
            "creator_profiles",
        ]
    )


@router.get("", response_model=MarketplaceListResponse)
@router.get("/", response_model=MarketplaceListResponse)
def list_marketplace_items(
    page: int = 1,
    per_page: int = 20,
    type: Optional[ItemType] = None,
    is_free: Optional[bool] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
    sort_by: str = "popular",  # popular, newest, rating
    response: Response = None
):
    """
    List marketplace items with filtering and pagination.

    Args:
        page: Page number (1-indexed)
        per_page: Items per page (max 50)
        type: Filter by item type
        is_free: Filter free/paid items
        difficulty: Filter by difficulty
        search: Search in title/description
        sort_by: Sort order (popular, newest, rating)
    """
    if response:
        add_phase_header(response)

    _seed_sample_items()

    # Filter items
    items = list(_items_db.values())

    # Only show published items
    items = [i for i in items if i.status == "published" and i.is_active]

    if type:
        items = [i for i in items if i.type == type]

    if is_free is not None:
        items = [i for i in items if i.is_free == is_free]

    if difficulty:
        items = [i for i in items if i.difficulty == difficulty]

    if search:
        search_lower = search.lower()
        items = [
            i for i in items
            if search_lower in i.title.lower()
            or (i.description and search_lower in i.description.lower())
            or any(search_lower in tag.lower() for tag in i.tags)
        ]

    # Sort
    if sort_by == "newest":
        items.sort(key=lambda x: x.created_at, reverse=True)
    elif sort_by == "rating":
        items.sort(key=lambda x: x.rating, reverse=True)
    else:  # popular
        items.sort(key=lambda x: x.installs_count, reverse=True)

    # Paginate
    total = len(items)
    per_page = min(per_page, 50)
    start = (page - 1) * per_page
    end = start + per_page
    page_items = items[start:end]

    return MarketplaceListResponse(
        items=[MarketplaceItemPublic(**i.model_dump()) for i in page_items],
        total=total,
        page=page,
        per_page=per_page,
        has_more=end < total,
    )


@router.get("/featured", response_model=List[MarketplaceItemPublic])
def get_featured_items(response: Response, limit: int = 6):
    """
    Get featured marketplace items.
    """
    add_phase_header(response)
    _seed_sample_items()

    # Get published items sorted by rating/installs
    items = [
        i for i in _items_db.values()
        if i.status == "published" and i.is_active
    ]
    items.sort(key=lambda x: (x.rating * x.installs_count), reverse=True)

    return [MarketplaceItemPublic(**i.model_dump()) for i in items[:limit]]


@router.get("/item/{item_id}", response_model=MarketplaceItemPublic)
def get_marketplace_item(item_id: UUID, response: Response):
    """
    Get marketplace item details by ID.
    """
    add_phase_header(response)
    _seed_sample_items()

    item = _items_db.get(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Marketplace item {item_id} not found"
        )

    return MarketplaceItemPublic(**item.model_dump())


# ==============================================================================
# INSTALLATION ENDPOINTS
# ==============================================================================

@router.post("/install", response_model=InstallationResponse)
def install_item(
    data: InstallationCreate,
    response: Response,
    # user: UserInDB = Depends(get_current_user)  # TODO: Add auth
):
    """
    Install a marketplace item.

    This will add the content to the user's (or tenant's) workspace.
    """
    add_phase_header(response)
    _seed_sample_items()

    # Check item exists
    item = _items_db.get(data.item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Marketplace item {data.item_id} not found"
        )

    if item.status != "published":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Item is not available for installation"
        )

    # TODO: Check payment for paid items
    # TODO: Get actual user from auth
    mock_user_id = uuid4()

    # Check if already installed
    for inst in _installations_db.values():
        if inst.item_id == data.item_id and inst.user_id == mock_user_id and inst.is_active:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Item already installed"
            )

    # Create installation
    installation = InstallationInDB(
        id=uuid4(),
        item_id=data.item_id,
        user_id=mock_user_id,
        tenant_id=data.tenant_id,
        version=data.version or item.version,
        item_title=item.title,
        item_type=item.type,
    )
    _installations_db[installation.id] = installation

    # Update install count
    item.installs_count += 1

    return InstallationResponse(
        success=True,
        message=f"Successfully installed '{item.title}'",
        installation=InstallationPublic(**installation.model_dump()),
    )


@router.delete("/install/{installation_id}", response_model=InstallationResponse)
def uninstall_item(installation_id: UUID, response: Response):
    """
    Uninstall a marketplace item.
    """
    add_phase_header(response)

    installation = _installations_db.get(installation_id)
    if not installation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Installation not found"
        )

    # Soft delete
    installation.is_active = False
    installation.uninstalled_at = datetime.utcnow()

    return InstallationResponse(
        success=True,
        message="Successfully uninstalled item",
    )


@router.get("/installations", response_model=List[InstallationPublic])
def list_installations(
    response: Response,
    # user: UserInDB = Depends(get_current_user)  # TODO: Add auth
):
    """
    List user's installed marketplace items.
    """
    add_phase_header(response)

    # TODO: Get actual user from auth
    # For now, return all active installations
    installations = [
        InstallationPublic(**i.model_dump())
        for i in _installations_db.values()
        if i.is_active
    ]

    return installations


# ==============================================================================
# CREATOR ENDPOINTS
# ==============================================================================

@router.get("/creator/{creator_id}", response_model=CreatorPublic)
def get_creator(creator_id: UUID, response: Response):
    """
    Get creator profile by ID.
    """
    add_phase_header(response)
    _seed_sample_items()

    creator = _creators_db.get(creator_id)
    if not creator:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Creator not found"
        )

    return CreatorPublic(**creator.model_dump())


@router.get("/creator/{creator_id}/items", response_model=List[MarketplaceItemPublic])
def get_creator_items(creator_id: UUID, response: Response):
    """
    Get all published items by a creator.
    """
    add_phase_header(response)
    _seed_sample_items()

    items = [
        MarketplaceItemPublic(**i.model_dump())
        for i in _items_db.values()
        if i.creator_id == creator_id and i.status == "published"
    ]

    return items


# ==============================================================================
# REVIEW ENDPOINTS
# ==============================================================================

@router.get("/item/{item_id}/reviews", response_model=List[UserReviewPublic])
def get_item_reviews(item_id: UUID, response: Response):
    """
    Get reviews for a marketplace item.
    """
    add_phase_header(response)

    reviews = [
        UserReviewPublic(**r.model_dump())
        for r in _user_reviews_db.values()
        if r.item_id == item_id and r.is_active
    ]

    return reviews


@router.post("/item/{item_id}/review", response_model=UserReviewPublic, status_code=status.HTTP_201_CREATED)
def create_review(
    item_id: UUID,
    data: UserReviewCreate,
    response: Response,
):
    """
    Create a review for a marketplace item.
    """
    add_phase_header(response)
    _seed_sample_items()

    # Check item exists
    item = _items_db.get(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    # TODO: Check user has installed item
    mock_user_id = uuid4()

    review = UserReviewInDB(
        id=uuid4(),
        item_id=item_id,
        user_id=mock_user_id,
        user_display_name="Anonymous User",  # TODO: Get from user profile
        rating=data.rating,
        title=data.title,
        comment=data.comment,
        is_verified_purchase=False,  # TODO: Check installation
    )
    _user_reviews_db[review.id] = review

    # Update item rating (simple average)
    item_reviews = [r for r in _user_reviews_db.values() if r.item_id == item_id and r.is_active]
    if item_reviews:
        item.rating = sum(r.rating for r in item_reviews) / len(item_reviews)
        item.reviews_count = len(item_reviews)

    return UserReviewPublic(**review.model_dump())
