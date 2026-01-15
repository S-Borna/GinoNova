"""
Dashboard API - Aggregated summary endpoint
Phase 6.0: Dashboard Foundation
Phase SECURITY: Added authentication and fixed IDOR vulnerabilities
"""
from fastapi import APIRouter, HTTPException
from uuid import UUID
import logging

from ..core.settings import settings
from ..services.module_service import module_service
from ..services.task_service import task_service
from ..services.studyflow_service import studyflow_service
from ..services.progress_service import progress_service
from ..db import user_repository
from ..core.deps import CurrentUser

dashboard_router = APIRouter()
logger = logging.getLogger(__name__)


@dashboard_router.get("/status")
def dashboard_status(current_user: CurrentUser):
    """
    Phase 6.0 status check.
    
    **Authentication required**: Must be logged in.
    
    Args:
        current_user: Authenticated user (injected)
        
    Returns:
        Dashboard status information
    """
    return {
        "phase": "6.0",
        "feature": "Dashboard Foundation",
        "status": "operational"
    }


@dashboard_router.get("/summary")
def dashboard_summary(current_user: CurrentUser):
    """
    Aggregated dashboard summary for the authenticated user.

    Combines data from:
    - user (authenticated user)
    - modules
    - tasks
    - studyflow
    - progress (for authenticated user)
    - system info
    - version info

    **Authentication required**: Must be logged in.
    **Authorization**: Users can only access their own dashboard data.

    Args:
        current_user: Authenticated user (injected)

    Returns:
        Aggregated JSON object with all dashboard data for the authenticated user
        
    Raises:
        401: If not authenticated
    """
    try:
        # User data for authenticated user
        user_data = None
        progress_data = []
        user_id = current_user.id
        if user_id:
            try:
                user = user_repository.get_user_by_id(user_id)
                if user:
                    user_data = {
                        "id": str(user.id),
                        "email": getattr(user, 'email', ''),
                        "full_name": getattr(user, 'full_name', None),
                        "is_active": getattr(user, 'is_active', True),
                        "is_admin": getattr(user, 'is_admin', False),
                        "created_at": user.created_at.isoformat() if getattr(user, 'created_at', None) else None,
                    }
                # Progress records for user
                progress_records = progress_service.list_progress_for_user(user_id)
                progress_data = [
                    {
                        "id": str(p.id),
                        "user_id": str(p.user_id),
                        "module_id": str(p.module_id) if getattr(p, 'module_id', None) else None,
                        "task_id": str(p.task_id) if getattr(p, 'task_id', None) else None,
                        "studyflow_id": str(p.studyflow_id) if getattr(p, 'studyflow_id', None) else None,
                        "status": getattr(p, 'status', 'unknown'),
                        "progress": getattr(p, 'progress', 0),
                    }
                    for p in progress_records
                ]
            except Exception as e:
                logger.error(f"Error fetching user data: {e}")
                # Continue without user data

        # Modules list
        modules_data = []
        try:
            modules = module_service.list_modules()
            modules_data = [
                {
                    "id": str(m.id),
                    "name": getattr(m, 'name', 'Unknown'),
                    "description": getattr(m, 'description', None),
                    "is_active": getattr(m, 'is_active', True),
                }
                for m in modules
            ]
        except Exception as e:
            logger.error(f"Error fetching modules: {e}")

        # Tasks list
        tasks_data = []
        try:
            tasks = task_service.list_tasks()
            tasks_data = [
                {
                    "id": str(t.id),
                    "module_id": str(t.module_id) if getattr(t, 'module_id', None) else None,
                    "title": getattr(t, 'title', 'Unknown'),
                    "difficulty": getattr(t, 'difficulty', 'medium'),
                    "is_active": getattr(t, 'is_active', True),
                }
                for t in tasks
            ]
        except Exception as e:
            logger.error(f"Error fetching tasks: {e}")

        # Studyflows list
        studyflow_data = []
        try:
            studyflows = studyflow_service.list_studyflows()
            studyflow_data = [
                {
                    "id": str(sf.id),
                    "module_id": str(sf.module_id) if getattr(sf, 'module_id', None) else None,
                    "title": getattr(sf, 'title', 'Unknown'),
                    "order": getattr(sf, 'order', 0),
                    "is_active": getattr(sf, 'is_active', True),
                }
                for sf in studyflows
            ]
        except Exception as e:
            logger.error(f"Error fetching studyflows: {e}")

        # System info
        system_data = {
            "service": "saas-backend",
            "version": settings.PROJECT_VERSION,
            "environment": settings.RAILWAY_ENV or "development",
        }

        # Version info
        version_data = {
            "api_version": settings.PROJECT_VERSION,
            "phase": "6.0",
        }

        # Aggregated stats
        stats = {
            "total_modules": len(modules_data),
            "total_tasks": len(tasks_data),
            "total_studyflows": len(studyflow_data),
            "total_progress_records": len(progress_data),
            "active_modules": sum(1 for m in modules_data if m.get("is_active", False)),
            "active_tasks": sum(1 for t in tasks_data if t.get("is_active", False)),
        }

        return {
            "user": user_data,
            "modules": modules_data,
            "tasks": tasks_data,
            "studyflow": studyflow_data,
            "progress": progress_data,
            "system": system_data,
            "version": version_data,
            "stats": stats,
        }
    except Exception as e:
        logger.error(f"Dashboard summary error: {e}")
        raise HTTPException(status_code=500, detail=f"Dashboard error: {str(e)}")
