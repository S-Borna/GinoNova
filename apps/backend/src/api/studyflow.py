"""
Studyflow Router - API endpoints for studyflow management
Phase 4.0: Studyflow Foundation
"""
from uuid import UUID

from fastapi import APIRouter, Response, status

from ..schemas.studyflow import StudyflowCreate, StudyflowUpdate, StudyflowPublic
from ..services.studyflow_service import studyflow_service

studyflow_router = APIRouter()

# Phase version header
PHASE_VERSION = "4.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


@studyflow_router.get("/status")
def studyflow_status(response: Response):
    """Check studyflow module status"""
    add_phase_header(response)
    return {
        "studyflow": "configured",
        "phase": PHASE_VERSION,
        "endpoints": ["list", "list_by_module", "get", "create", "update", "delete"]
    }


@studyflow_router.get("/", response_model=list[StudyflowPublic])
def list_studyflows(response: Response):
    """
    List all studyflows.

    Returns list of all studyflows in the system.
    """
    add_phase_header(response)
    return studyflow_service.list_studyflows()


@studyflow_router.get("/module/{module_id}", response_model=list[StudyflowPublic])
def list_studyflows_by_module(module_id: UUID, response: Response):
    """
    List all studyflows for a specific module, sorted by order.

    Args:
        module_id: UUID of the module

    Returns:
        List of StudyflowPublic objects belonging to the module

    Raises:
        404: If module not found
    """
    add_phase_header(response)
    return studyflow_service.list_studyflows_for_module(module_id)


@studyflow_router.get("/{studyflow_id}", response_model=StudyflowPublic)
def get_studyflow(studyflow_id: UUID, response: Response):
    """
    Get a specific studyflow by ID.

    Args:
        studyflow_id: UUID of the studyflow to retrieve

    Returns:
        StudyflowPublic object

    Raises:
        404: If studyflow not found
    """
    add_phase_header(response)
    return studyflow_service.get_studyflow_by_id(studyflow_id)


@studyflow_router.post("/", response_model=StudyflowPublic, status_code=status.HTTP_201_CREATED)
def create_studyflow(data: StudyflowCreate, response: Response):
    """
    Create a new studyflow.

    Args:
        data: StudyflowCreate schema with:
            - module_id: UUID of the parent module
            - title: Studyflow title (3-100 chars)
            - description: Optional description (max 500 chars)
            - order: Position in module (> 0, unique per module)

    Returns:
        Created StudyflowPublic object

    Raises:
        404: If module not found
        409: If (module_id, order) already exists
        422: If validation fails
    """
    add_phase_header(response)
    return studyflow_service.create_studyflow(data)


@studyflow_router.put("/{studyflow_id}", response_model=StudyflowPublic)
def update_studyflow(studyflow_id: UUID, data: StudyflowUpdate, response: Response):
    """
    Update an existing studyflow.

    Args:
        studyflow_id: UUID of the studyflow to update
        data: StudyflowUpdate schema with optional fields:
            - title: New studyflow title (3-100 chars)
            - description: New description (max 500 chars)
            - order: New position (> 0)
            - is_active: Whether studyflow is active

    Returns:
        Updated StudyflowPublic object

    Raises:
        404: If studyflow not found
        409: If new order conflicts with existing studyflow in same module
        422: If validation fails
    """
    add_phase_header(response)
    return studyflow_service.update_studyflow(studyflow_id, data)


@studyflow_router.delete("/{studyflow_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_studyflow(studyflow_id: UUID, response: Response):
    """
    Delete a studyflow.

    Args:
        studyflow_id: UUID of the studyflow to delete

    Raises:
        404: If studyflow not found
    """
    add_phase_header(response)
    studyflow_service.delete_studyflow(studyflow_id)
    return None
