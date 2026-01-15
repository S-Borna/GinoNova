"""
Progress Router - API endpoints for progress tracking
Phase 5.0: Progress Engine Foundation
Phase SECURITY: Added authentication and authorization checks
"""
from uuid import UUID

from fastapi import APIRouter, Response, status, HTTPException

from ..schemas.progress import ProgressCreate, ProgressUpdate, ProgressPublic
from ..services.progress_service import progress_service
from ..core.deps import CurrentUser

progress_router = APIRouter()

# Phase version header
PHASE_VERSION = "5.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


@progress_router.get("/status")
def progress_status(response: Response):
    """Check progress module status"""
    add_phase_header(response)
    return {
        "progress": "configured",
        "phase": PHASE_VERSION,
        "endpoints": ["list_by_user", "get", "create", "update"]
    }


@progress_router.get("/user/{user_id}", response_model=list[ProgressPublic])
def list_progress_by_user(user_id: UUID, response: Response, current_user: CurrentUser):
    """
    List all progress records for a specific user.

    **Authentication required**: Must be logged in.
    **Authorization**: Users can only access their own progress unless they're admin.

    Args:
        user_id: UUID of the user
        current_user: Authenticated user (injected)

    Returns:
        List of ProgressPublic objects belonging to the user

    Raises:
        401: If not authenticated
        403: If trying to access another user's progress without admin rights
    """
    # Authorization check: users can only access their own progress unless admin
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own progress"
        )

    add_phase_header(response)
    return progress_service.list_progress_for_user(user_id)


@progress_router.get("/{progress_id}", response_model=ProgressPublic)
def get_progress(progress_id: UUID, response: Response, current_user: CurrentUser):
    """
    Get a specific progress record by ID.

    **Authentication required**: Must be logged in.
    **Authorization**: Users can only access their own progress unless they're admin.

    Args:
        progress_id: UUID of the progress record to retrieve
        current_user: Authenticated user (injected)

    Returns:
        ProgressPublic object

    Raises:
        401: If not authenticated
        403: If trying to access another user's progress
        404: If progress record not found
    """
    add_phase_header(response)
    progress = progress_service.get_progress_by_id(progress_id)

    # Authorization check: verify the progress belongs to current user or user is admin
    if progress.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own progress"
        )

    return progress


@progress_router.post("/", response_model=ProgressPublic, status_code=status.HTTP_201_CREATED)
def create_progress(data: ProgressCreate, response: Response, current_user: CurrentUser):
    """
    Create a new progress record.

    **Authentication required**: Must be logged in.
    **Authorization**: Users can only create progress for themselves unless they're admin.

    Args:
        data: ProgressCreate schema with:
            - user_id: UUID of the user
            - module_id OR task_id OR studyflow_id: UUID of target (exactly one)
            - progress: Percentage (0-100, default 0)
        current_user: Authenticated user (injected)

    Returns:
        Created ProgressPublic object

    Raises:
        401: If not authenticated
        403: If trying to create progress for another user
        404: If target not found
        409: If progress already exists for user + target
        422: If validation fails (e.g., more than one target set)
    """
    # Authorization check: users can only create progress for themselves unless admin
    if data.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create progress for yourself"
        )

    add_phase_header(response)
    return progress_service.create_progress(data)


@progress_router.put("/{progress_id}", response_model=ProgressPublic)
def update_progress(progress_id: UUID, data: ProgressUpdate, response: Response):
    """
    Update an existing progress record.

    Args:
        progress_id: UUID of the progress record to update
        data: ProgressUpdate schema with optional fields:
            - progress: New percentage (0-100)

    Returns:
        Updated ProgressPublic object

    Notes:
        - Status is automatically synced based on progress value
        - progress=0 => not_started
        - progress 1-99 => in_progress
        - progress=100 => completed

    Raises:
        404: If progress record not found
        422: If validation fails
    """
    add_phase_header(response)
    return progress_service.update_progress(progress_id, data)
