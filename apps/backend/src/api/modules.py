"""
Modules Router - API endpoints for module management
Phase 2.0: Modules Foundation
"""
from uuid import UUID

from fastapi import APIRouter, Response, status

from ..schemas.module import ModuleCreate, ModuleUpdate, ModulePublic
from ..services.module_service import module_service

modules_router = APIRouter()

# Phase version header
PHASE_VERSION = "2.0"


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
        "endpoints": ["list", "get", "create", "update", "delete"]
    }


@modules_router.get("/", response_model=list[ModulePublic])
def list_modules(response: Response):
    """
    List all modules.

    Returns list of all modules in the system.
    """
    add_phase_header(response)
    return module_service.list_modules()


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
