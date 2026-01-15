"""
Content Delivery System (CDS) API Routes
Phase 14 - Content Delivery
Phase SECURITY: Added authentication to prevent content scraping

Provides clean, content-focused endpoints for:
- Module content by slug
- Task content by ID
- Raw markdown/content fetching

All endpoints require authentication to prevent unauthorized content scraping.
"""
from typing import Optional, List, Any
from uuid import UUID

from fastapi import APIRouter, Response, HTTPException, status
from pydantic import BaseModel

from ...db import module_repository, task_repository
from ...core.deps import CurrentUser


router = APIRouter(prefix="/content", tags=["content"])

PHASE_VERSION = "14.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# RESPONSE SCHEMAS
# ==============================================================================

class TaskSummary(BaseModel):
    """Minimal task info for module listing"""
    id: str
    title: str
    order_index: int
    difficulty: str
    estimated_minutes: int
    xp_reward: int
    has_content_blocks: bool = False


class ModuleContentResponse(BaseModel):
    """Full module content response for CDS"""
    id: str
    slug: str
    name: str
    title: str  # Alias for name
    description: Optional[str] = None

    # Structure
    track_id: Optional[str] = None
    order_index: int = 1

    # Metadata
    difficulty: str = "intermediate"
    estimated_hours: float = 10.0
    prerequisites: List[str] = []
    tags: List[str] = []

    # Content
    content: Optional[str] = None  # Raw markdown if exists

    # Tasks
    tasks: List[TaskSummary] = []
    total_tasks: int = 0

    # Status
    is_active: bool = True


class TaskContentResponse(BaseModel):
    """Full task content response for CDS"""
    id: str
    module_id: str
    title: str
    description: Optional[str] = None

    # Order
    order_index: int = 1

    # Content
    content: Optional[str] = None  # Markdown content
    content_blocks: Optional[List[Any]] = None  # Interactive blocks
    requirements: Optional[List[Any]] = None  # Completion requirements

    # Metadata
    difficulty: str = "medium"
    estimated_minutes: int = 15
    xp_reward: int = 25

    # Examples (future)
    examples: List[Any] = []

    # Attachments (future)
    attachments: List[Any] = []

    # Status
    is_active: bool = True

    # Navigation context
    module_slug: Optional[str] = None
    prev_task_id: Optional[str] = None
    next_task_id: Optional[str] = None


class ContentStatusResponse(BaseModel):
    """CDS status response"""
    status: str = "operational"
    phase: str = PHASE_VERSION
    endpoints: List[str]
    features: List[str]


# ==============================================================================
# ENDPOINTS
# ==============================================================================

@router.get("/status", response_model=ContentStatusResponse)
def content_status(response: Response, current_user: CurrentUser):
    """
    Get Content Delivery System status.
    
    **Authentication required**: Must be logged in to access content system.

    Args:
        current_user: Authenticated user (injected)

    Returns:
        CDS status and available features
        
    Raises:
        401: If not authenticated
    """
    add_phase_header(response)
    return ContentStatusResponse(
        status="operational",
        phase=PHASE_VERSION,
        endpoints=[
            "GET /content/module/{slug}",
            "GET /content/task/{id}",
            "GET /content/raw/{path}",
        ],
        features=[
            "markdown_rendering",
            "code_highlighting",
            "interactive_content_blocks",
            "task_navigation",
            "module_overview",
        ]
    )


@router.get("/module/{slug}", response_model=ModuleContentResponse)
def get_module_content(slug: str, response: Response, current_user: CurrentUser):
    """
    Get module content by slug.

    This endpoint returns full module content including:
    - Module metadata
    - Task list with summaries
    - Raw markdown content if available

    **Authentication required**: Must be logged in to access module content.

    Args:
        slug: Module slug (e.g., "linux-basics", "docker-fundamentals")
        current_user: Authenticated user (injected)

    Returns:
        ModuleContentResponse with full module data

    Raises:
        401: If not authenticated
        404: If module not found
    """
    add_phase_header(response)

    # Find module by slug
    module = module_repository.get_module_by_slug(slug)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module with slug '{slug}' not found"
        )

    # Get tasks for this module
    tasks = task_repository.list_tasks_by_module(module.id)

    # Build task summaries
    task_summaries = [
        TaskSummary(
            id=str(task.id),
            title=task.title,
            order_index=task.order_index,
            difficulty=task.difficulty,
            estimated_minutes=task.estimated_minutes,
            xp_reward=task.xp_reward,
            has_content_blocks=bool(task.content_blocks),
        )
        for task in sorted(tasks, key=lambda t: t.order_index)
    ]

    # Generate tags from module name and difficulty
    tags = [
        module.difficulty,
        module.name.lower().replace(" ", "-"),
    ]
    if module.track_id:
        tags.append("track")

    return ModuleContentResponse(
        id=str(module.id),
        slug=module.slug,
        name=module.name,
        title=module.name,  # Alias
        description=module.description,
        track_id=str(module.track_id) if module.track_id else None,
        order_index=module.order_index,
        difficulty=module.difficulty,
        estimated_hours=module.estimated_hours,
        prerequisites=module.prerequisites or [],
        tags=tags,
        content=None,  # TODO: Load from markdown file if exists
        tasks=task_summaries,
        total_tasks=len(task_summaries),
        is_active=module.is_active,
    )


@router.get("/task/{task_id}", response_model=TaskContentResponse)
def get_task_content(task_id: UUID, response: Response, current_user: CurrentUser):
    """
    Get task content by ID.

    This endpoint returns full task content including:
    - Task metadata
    - Markdown content OR interactive content blocks
    - Navigation context (prev/next tasks)
    - Examples and attachments

    **Authentication required**: Must be logged in to access task content.

    Args:
        task_id: Task UUID
        current_user: Authenticated user (injected)

    Returns:
        TaskContentResponse with full task data

    Raises:
        401: If not authenticated
        404: If task not found
    """
    add_phase_header(response)

    # Find task
    task = task_repository.get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id '{task_id}' not found"
        )

    # Get module for slug
    module = module_repository.get_module_by_id(task.module_id) if task.module_id else None
    module_slug = module.slug if module else None

    # Get sibling tasks for navigation
    prev_task_id = None
    next_task_id = None

    if task.module_id:
        sibling_tasks = task_repository.list_tasks_by_module(task.module_id)
        sorted_siblings = sorted(sibling_tasks, key=lambda t: t.order_index)

        current_idx = next(
            (i for i, t in enumerate(sorted_siblings) if t.id == task.id),
            -1
        )

        if current_idx > 0:
            prev_task_id = str(sorted_siblings[current_idx - 1].id)
        if current_idx >= 0 and current_idx < len(sorted_siblings) - 1:
            next_task_id = str(sorted_siblings[current_idx + 1].id)

    return TaskContentResponse(
        id=str(task.id),
        module_id=str(task.module_id) if task.module_id else "",
        title=task.title,
        description=task.description,
        order_index=task.order_index,
        content=task.content,
        content_blocks=task.content_blocks,
        requirements=task.requirements,
        difficulty=task.difficulty,
        estimated_minutes=task.estimated_minutes,
        xp_reward=task.xp_reward,
        examples=[],  # TODO: Extract from content or separate field
        attachments=[],  # TODO: Future feature
        is_active=task.is_active,
        module_slug=module_slug,
        prev_task_id=prev_task_id,
        next_task_id=next_task_id,
    )


@router.get("/raw/{path:path}")
def get_raw_content(path: str, response: Response, current_user: CurrentUser):
    """
    Get raw markdown content by path.

    This endpoint returns raw markdown content for:
    - Module README files
    - Task content files
    - Documentation

    **Authentication required**: Must be logged in to access raw content.

    Args:
        path: Content path (e.g., "modules/linux/README.md")
        current_user: Authenticated user (injected)

    Returns:
        Raw markdown content

    Raises:
        401: If not authenticated
        404: If content not found
        501: Feature not yet implemented
    """
    add_phase_header(response)

    # TODO: Implement file-based content loading
    # For now, return not implemented
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Raw content fetching not yet implemented. Content is stored in database."
    )


# ==============================================================================
# SEARCH & DISCOVERY
# ==============================================================================

class ContentSearchResult(BaseModel):
    """Search result item"""
    type: str  # "module" or "task"
    id: str
    title: str
    description: Optional[str] = None
    slug: Optional[str] = None
    module_slug: Optional[str] = None
    relevance: float = 1.0


class ContentSearchResponse(BaseModel):
    """Search results response"""
    query: str
    total: int
    results: List[ContentSearchResult]


@router.get("/search", response_model=ContentSearchResponse)
def search_content(
    q: str,
    current_user: CurrentUser,
    type: Optional[str] = None,  # "module", "task", or None for all
    limit: int = 20,
    response: Response = None
):
    """
    Search content by query.

    Simple text search across modules and tasks.

    **Authentication required**: Must be logged in to search content.

    Args:
        q: Search query
        current_user: Authenticated user (injected)
        type: Filter by content type ("module" or "task")
        limit: Max results to return

    Returns:
        ContentSearchResponse with matching content
        
    Raises:
        401: If not authenticated
    """
    if response:
        add_phase_header(response)

    results: List[ContentSearchResult] = []
    query_lower = q.lower()

    # Search modules
    if type is None or type == "module":
        for module in module_repository.list_modules():
            # Simple relevance scoring
            relevance = 0.0
            if query_lower in module.name.lower():
                relevance += 1.0
            if module.description and query_lower in module.description.lower():
                relevance += 0.5
            if query_lower in module.slug.lower():
                relevance += 0.3

            if relevance > 0:
                results.append(ContentSearchResult(
                    type="module",
                    id=str(module.id),
                    title=module.name,
                    description=module.description,
                    slug=module.slug,
                    relevance=relevance,
                ))

    # Search tasks
    if type is None or type == "task":
        for task in task_repository.list_tasks():
            # Simple relevance scoring
            relevance = 0.0
            if query_lower in task.title.lower():
                relevance += 1.0
            if task.description and query_lower in task.description.lower():
                relevance += 0.5
            if task.content and query_lower in task.content.lower():
                relevance += 0.3

            if relevance > 0:
                # Get module for slug
                module = None
                if task.module_id:
                    module = module_repository.get_module_by_id(task.module_id)

                results.append(ContentSearchResult(
                    type="task",
                    id=str(task.id),
                    title=task.title,
                    description=task.description,
                    module_slug=module.slug if module else None,
                    relevance=relevance,
                ))

    # Sort by relevance and limit
    results.sort(key=lambda r: r.relevance, reverse=True)
    results = results[:limit]

    return ContentSearchResponse(
        query=q,
        total=len(results),
        results=results,
    )
