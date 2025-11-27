"""
Phase 8.7 — Data Debug Endpoints
Read-only endpoints for inspecting data layer state.
"""

from fastapi import APIRouter, Query
from typing import Optional, Dict, Any

from ..data.store.memory_store import (
    get_task_events,
    get_session_events,
    get_activity_events,
    get_store_stats,
)
from ..data.store.snapshot_builder import get_all_snapshots, get_snapshot
from ..data.normalized.tasks_normalizer import NormalizedTaskEvent
from ..data.normalized.session_normalizer import NormalizedStudyflowSession
from ..data.normalized.activity_normalizer import NormalizedUserActivity


data_router = APIRouter(prefix="/data", tags=["data"])


@data_router.get("/raw")
def get_raw_data(
    event_type: str = Query("task", description="Event type: task, session, activity"),
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    limit: int = Query(50, ge=1, le=500, description="Max events to return"),
) -> Dict[str, Any]:
    """
    Get raw event data from the store.
    Read-only endpoint for debugging.
    
    Note: Returns normalized events (raw events are transformed on ingest).
    """
    if event_type == "task":
        events = get_task_events(user_id=user_id, limit=limit)
        return {
            "event_type": "task",
            "count": len(events),
            "events": [e.model_dump() for e in events],
        }
    elif event_type == "session":
        events = get_session_events(user_id=user_id, limit=limit)
        return {
            "event_type": "session",
            "count": len(events),
            "events": [e.model_dump() for e in events],
        }
    elif event_type == "activity":
        events = get_activity_events(user_id=user_id, limit=limit)
        return {
            "event_type": "activity",
            "count": len(events),
            "events": [e.model_dump() for e in events],
        }
    else:
        return {
            "error": f"Unknown event type: {event_type}",
            "valid_types": ["task", "session", "activity"],
        }


@data_router.get("/normalized")
def get_normalized_data(
    event_type: str = Query("task", description="Event type: task, session, activity"),
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    limit: int = Query(50, ge=1, le=500, description="Max events to return"),
) -> Dict[str, Any]:
    """
    Get normalized event data from the store.
    Read-only endpoint for debugging.
    """
    # Normalized data is what we store, so same as /raw in current implementation
    return get_raw_data(event_type=event_type, user_id=user_id, limit=limit)


@data_router.get("/store")
def get_store_status() -> Dict[str, Any]:
    """
    Get store statistics and capacity info.
    Read-only endpoint for debugging.
    """
    stats = get_store_stats()
    return {
        "status": "healthy",
        "stats": stats,
    }


@data_router.get("/snapshots")
def get_snapshots_data(
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    date_key: Optional[str] = Query(None, description="Specific date YYYY-MM-DD"),
) -> Dict[str, Any]:
    """
    Get daily snapshots.
    Read-only endpoint for debugging.
    """
    if date_key and user_id:
        # Get specific snapshot
        snapshot = get_snapshot(user_id=user_id, date_key=date_key)
        if snapshot:
            return {
                "count": 1,
                "snapshots": [snapshot],
            }
        else:
            return {
                "count": 0,
                "snapshots": [],
                "message": f"No snapshot found for user {user_id} on {date_key}",
            }
    else:
        # Get all snapshots
        snapshots = get_all_snapshots(user_id=user_id)
        return {
            "count": len(snapshots),
            "snapshots": snapshots,
        }
