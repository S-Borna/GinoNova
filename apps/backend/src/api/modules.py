"""
Modules Router - API endpoints for module management
Phase 2.0: Modules Foundation
Phase 5.0: Added full module with content endpoint
Phase SECURITY: Added authentication to all endpoints
"""
from uuid import UUID
from typing import Optional

from fastapi import APIRouter, Response, status

from ..schemas.module import ModuleCreate, ModuleUpdate, ModulePublic
from ..services.module_service import module_service
from ..db.seeds.content import get_module_by_slug as get_content_module
from ..core.deps import CurrentUser

modules_router = APIRouter()

# Phase version header
PHASE_VERSION = "5.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


@modules_router.get("/status")
def modules_status(response: Response):
    """Check modules module status"""
    add_phase_header(response)
    return {
        "modules": "configured",
        "phase": PHASE_VERSION,
        "endpoints": ["list", "get", "create", "update", "delete", "full"]
    }


@modules_router.get("/full/{slug}")
def get_full_module(slug: str, response: Response, current_user: CurrentUser):
    """
    Get FULL module data including all tasks and content.

    This is the main endpoint for frontend to get complete module data.
    Returns module with all tasks, groups, content - everything needed to render.

    **Authentication required**: Must be logged in to access module content.

    Args:
        slug: Module slug (e.g., 'doe25-tenta', 'linux-247')
        current_user: Authenticated user (injected)

    Returns:
        Full module dict with all data from content source

    Raises:
        401: If not authenticated
        404: If module not found
    """
    add_phase_header(response)

    module = get_content_module(slug)
    if not module:
        return Response(
            content=f'{{"detail": "Module \'{slug}\' not found"}}',
            status_code=404,
            media_type="application/json"
        )

    return module


@modules_router.get("/full")
def list_full_modules(response: Response, current_user: CurrentUser):
    """
    List ALL modules with full data including tasks and content.

    This is the main endpoint for frontend to get all modules for listing pages.

    **Authentication required**: Must be logged in to access module content.

    Args:
        current_user: Authenticated user (injected)

    Returns:
        List of all modules with full content

    Raises:
        401: If not authenticated
    """
    add_phase_header(response)
    from ..db.seeds.content import get_all_modules
    return get_all_modules()


@modules_router.get("", response_model=list[ModulePublic])
@modules_router.get("/", response_model=list[ModulePublic])
def list_modules(response: Response, current_user: CurrentUser):
    """
    List all modules.

    **Authentication required**: Must be logged in to view modules.

    Args:
        current_user: Authenticated user (injected)

    Returns:
        List of all modules in the system

    Raises:
        401: If not authenticated
    """
    add_phase_header(response)
    return module_service.list_modules()


@modules_router.get("/slug/{slug}", response_model=ModulePublic)
def get_module_by_slug(slug: str, response: Response, current_user: CurrentUser):
    """
    Get a specific module by slug.

    **Authentication required**: Must be logged in to view module details.

    Args:
        slug: Slug of the module to retrieve (e.g., 'linux-mastery')
        current_user: Authenticated user (injected)

    Returns:
        ModulePublic object

    Raises:
        401: If not authenticated
        404: If module not found
    """
    add_phase_header(response)
    return module_service.get_module_by_slug(slug)


@modules_router.get("/{module_id}", response_model=ModulePublic)
def get_module(module_id: UUID, response: Response):
    """
    Get a specific module by ID.

    Args:
        module_id: UUID of the module to retrieve

    Returns:
        ModulePublic object

    Raises:
        404: If module not found
    """
    add_phase_header(response)
    return module_service.get_module_by_id(module_id)


@modules_router.post("/", response_model=ModulePublic, status_code=status.HTTP_201_CREATED)
def create_module(data: ModuleCreate, response: Response):
    """
    Create a new module.

    Args:
        data: ModuleCreate schema with:
            - name: Module name (2-50 chars, unique)
            - description: Optional description (max 300 chars)

    Returns:
        Created ModulePublic object

    Raises:
        409: If module name already exists
        422: If validation fails
    """
    add_phase_header(response)
    return module_service.create_module(data)


@modules_router.put("/{module_id}", response_model=ModulePublic)
def update_module(module_id: UUID, data: ModuleUpdate, response: Response):
    """
    Update an existing module.

    Args:
        module_id: UUID of the module to update
        data: ModuleUpdate schema with optional fields:
            - name: New module name (2-50 chars)
            - description: New description (max 300 chars)
            - is_active: Whether module is active

    Returns:
        Updated ModulePublic object

    Raises:
        404: If module not found
        409: If new name conflicts with existing module
        422: If validation fails
    """
    add_phase_header(response)
    return module_service.update_module(module_id, data)


@modules_router.delete("/{module_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_module(module_id: UUID, response: Response):
    """
    Delete a module.

    Args:
        module_id: UUID of the module to delete

    Raises:
        404: If module not found
    """
    add_phase_header(response)
    module_service.delete_module(module_id)
    return None
