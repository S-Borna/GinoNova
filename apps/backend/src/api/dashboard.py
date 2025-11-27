"""
Dashboard API - Aggregated summary endpoint
Phase 6.0: Dashboard Foundation
"""
from fastapi import APIRouter
from uuid import UUID

from ..core.settings import settings
from ..services.module_service import module_service
from ..services.task_service import task_service
from ..services.studyflow_service import studyflow_service
from ..services.progress_service import progress_service
from ..db import user_repository

dashboard_router = APIRouter()


@dashboard_router.get("/status")
def dashboard_status():
    """Phase 6.0 status check"""
    return {
        "phase": "6.0",
        "feature": "Dashboard Foundation",
        "status": "operational"
    }


@dashboard_router.get("/summary")
def dashboard_summary(user_id: UUID | None = None):
    """
    Aggregated dashboard summary.

    Combines data from:
    - user (if user_id provided)
    - modules
    - tasks
    - studyflow
    - progress (if user_id provided)
    - system info
    - version info

    Args:
        user_id: Optional UUID to fetch user-specific data

    Returns:
        Aggregated JSON object with all dashboard data
    """
    # User data (if user_id provided)
    user_data = None
    progress_data = []
    if user_id:
        user = user_repository.get_user_by_id(user_id)
        if user:
            user_data = {
                "id": str(user.id),
                "email": user.email,
                "full_name": user.full_name,
                "is_active": user.is_active,
                "is_admin": user.is_admin,
                "created_at": user.created_at.isoformat() if user.created_at else None,
            }
        # Progress records for user
        progress_records = progress_service.list_progress_for_user(user_id)
        progress_data = [
            {
                "id": str(p.id),
                "user_id": str(p.user_id),
                "module_id": str(p.module_id) if p.module_id else None,
                "task_id": str(p.task_id) if p.task_id else None,
                "studyflow_id": str(p.studyflow_id) if p.studyflow_id else None,
                "status": p.status,
                "progress": p.progress,
            }
            for p in progress_records
        ]

    # Modules list
    modules = module_service.list_modules()
    modules_data = [
        {
            "id": str(m.id),
            "name": m.name,
            "description": m.description,
            "is_active": m.is_active,
        }
        for m in modules
    ]

    # Tasks list
    tasks = task_service.list_tasks()
    tasks_data = [
        {
            "id": str(t.id),
            "module_id": str(t.module_id),
            "title": t.title,
            "difficulty": t.difficulty,
            "is_active": t.is_active,
        }
        for t in tasks
    ]

    # Studyflows list
    studyflows = studyflow_service.list_studyflows()
    studyflow_data = [
        {
            "id": str(sf.id),
            "module_id": str(sf.module_id),
            "title": sf.title,
            "order": sf.order,
            "is_active": sf.is_active,
        }
        for sf in studyflows
    ]

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
        "active_modules": sum(1 for m in modules_data if m["is_active"]),
        "active_tasks": sum(1 for t in tasks_data if t["is_active"]),
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
