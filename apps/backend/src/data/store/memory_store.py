"""
Phase 8.3 — Memory Store
Rolling window in-memory storage for normalized events.
Max 5,000 events per type.
"""

from collections import deque
from typing import List, Dict, Any, Optional
from threading import Lock

from ..normalized.tasks_normalizer import NormalizedTaskEvent
from ..normalized.session_normalizer import NormalizedStudyflowSession
from ..normalized.activity_normalizer import NormalizedUserActivity


# Configuration
MAX_EVENTS_PER_TYPE = 5000

# Thread-safe storage using deques with maxlen for automatic eviction
_task_events: deque = deque(maxlen=MAX_EVENTS_PER_TYPE)
_session_events: deque = deque(maxlen=MAX_EVENTS_PER_TYPE)
_activity_events: deque = deque(maxlen=MAX_EVENTS_PER_TYPE)

# Lock for thread safety
_store_lock = Lock()


def store_task_event(event: NormalizedTaskEvent) -> None:
    """
    Store a normalized task event.
    Automatically evicts oldest when at capacity.
    
    Args:
        event: Normalized task event to store
    """
    with _store_lock:
        _task_events.append(event)


def store_session_event(event: NormalizedStudyflowSession) -> None:
    """
    Store a normalized session event.
    Automatically evicts oldest when at capacity.
    
    Args:
        event: Normalized session event to store
    """
    with _store_lock:
        _session_events.append(event)


def store_activity_event(event: NormalizedUserActivity) -> None:
    """
    Store a normalized activity event.
    Automatically evicts oldest when at capacity.
    
    Args:
        event: Normalized activity event to store
    """
    with _store_lock:
        _activity_events.append(event)


def get_task_events(
    user_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[NormalizedTaskEvent]:
    """
    Get task events, optionally filtered by user.
    Returns sorted by timestamp (newest first) for determinism.
    
    Args:
        user_id: Optional user ID filter
        limit: Optional max number of events
        
    Returns:
        List of normalized task events, sorted newest first
    """
    with _store_lock:
        events = list(_task_events)
    
    if user_id:
        events = [e for e in events if e.user_id == user_id]
    
    # Sort by timestamp descending for determinism
    events = sorted(events, key=lambda e: e.timestamp_iso, reverse=True)
    
    if limit:
        events = events[:limit]
    
    return events


def get_session_events(
    user_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[NormalizedStudyflowSession]:
    """
    Get session events, optionally filtered by user.
    Returns sorted by timestamp (newest first) for determinism.
    
    Args:
        user_id: Optional user ID filter
        limit: Optional max number of events
        
    Returns:
        List of normalized session events, sorted newest first
    """
    with _store_lock:
        events = list(_session_events)
    
    if user_id:
        events = [e for e in events if e.user_id == user_id]
    
    # Sort by timestamp descending for determinism
    events = sorted(events, key=lambda e: e.timestamp_iso, reverse=True)
    
    if limit:
        events = events[:limit]
    
    return events


def get_activity_events(
    user_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[NormalizedUserActivity]:
    """
    Get activity events, optionally filtered by user.
    Returns sorted by timestamp (newest first) for determinism.
    
    Args:
        user_id: Optional user ID filter
        limit: Optional max number of events
        
    Returns:
        List of normalized activity events, sorted newest first
    """
    with _store_lock:
        events = list(_activity_events)
    
    if user_id:
        events = [e for e in events if e.user_id == user_id]
    
    # Sort by timestamp descending for determinism
    events = sorted(events, key=lambda e: e.timestamp_iso, reverse=True)
    
    if limit:
        events = events[:limit]
    
    return events


def get_store_stats() -> Dict[str, Any]:
    """
    Get current store statistics.
    
    Returns:
        Dict with counts and capacity info
    """
    with _store_lock:
        return {
            "task_events_count": len(_task_events),
            "session_events_count": len(_session_events),
            "activity_events_count": len(_activity_events),
            "max_per_type": MAX_EVENTS_PER_TYPE,
            "task_capacity_pct": round(len(_task_events) / MAX_EVENTS_PER_TYPE * 100, 2),
            "session_capacity_pct": round(len(_session_events) / MAX_EVENTS_PER_TYPE * 100, 2),
            "activity_capacity_pct": round(len(_activity_events) / MAX_EVENTS_PER_TYPE * 100, 2),
        }


def clear_store() -> Dict[str, int]:
    """
    Clear all events from store.
    Returns counts of cleared events.
    Used for testing.
    
    Returns:
        Dict with counts of cleared events per type
    """
    with _store_lock:
        counts = {
            "task_events_cleared": len(_task_events),
            "session_events_cleared": len(_session_events),
            "activity_events_cleared": len(_activity_events),
        }
        _task_events.clear()
        _session_events.clear()
        _activity_events.clear()
        return counts
