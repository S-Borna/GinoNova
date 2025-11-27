"""
Phase 8.3 — Secondary Indexes
Indexes for efficient queries: by module, by date, by difficulty.
"""

from typing import List, Dict, Optional
from threading import Lock

from .memory_store import get_task_events, get_session_events
from ..normalized.tasks_normalizer import NormalizedTaskEvent
from ..normalized.session_normalizer import NormalizedStudyflowSession


# Index storage
_module_index: Dict[str, List[str]] = {}  # module_id -> list of event_ids
_date_index: Dict[str, List[str]] = {}  # date_key -> list of event_ids
_difficulty_index: Dict[str, List[str]] = {}  # difficulty_bucket -> list of event_ids
_index_lock = Lock()


def rebuild_indexes() -> Dict[str, int]:
    """
    Rebuild all secondary indexes from current store.
    Called after bulk operations or periodically.
    
    Returns:
        Dict with counts of indexed items per index type
    """
    task_events = get_task_events()
    session_events = get_session_events()
    
    with _index_lock:
        # Clear existing indexes
        _module_index.clear()
        _date_index.clear()
        _difficulty_index.clear()
        
        # Index task events
        for event in task_events:
            # Module index
            if event.module_id:
                if event.module_id not in _module_index:
                    _module_index[event.module_id] = []
                _module_index[event.module_id].append(event.event_id)
            
            # Date index
            if event.date_key not in _date_index:
                _date_index[event.date_key] = []
            _date_index[event.date_key].append(event.event_id)
            
            # Difficulty index
            if event.difficulty_bucket not in _difficulty_index:
                _difficulty_index[event.difficulty_bucket] = []
            _difficulty_index[event.difficulty_bucket].append(event.event_id)
        
        # Index session events by date (and module if present)
        for event in session_events:
            # Module index for sessions
            if event.module_id:
                if event.module_id not in _module_index:
                    _module_index[event.module_id] = []
                _module_index[event.module_id].append(event.session_id)
            
            # Date index for sessions
            if event.date_key not in _date_index:
                _date_index[event.date_key] = []
            _date_index[event.date_key].append(event.session_id)
        
        return {
            "modules_indexed": len(_module_index),
            "dates_indexed": len(_date_index),
            "difficulties_indexed": len(_difficulty_index),
            "total_task_events": len(task_events),
            "total_session_events": len(session_events),
        }


def get_events_by_module(
    module_id: str,
    user_id: Optional[str] = None,
) -> Dict[str, List]:
    """
    Get all events for a specific module.
    Returns both task and session events.
    
    Args:
        module_id: Module ID to filter by
        user_id: Optional user ID filter
        
    Returns:
        Dict with task_events and session_events lists
    """
    task_events = get_task_events(user_id=user_id)
    session_events = get_session_events(user_id=user_id)
    
    # Filter by module
    task_events = [e for e in task_events if e.module_id == module_id]
    session_events = [e for e in session_events if e.module_id == module_id]
    
    # Sort for determinism
    task_events = sorted(task_events, key=lambda e: (e.timestamp_iso, e.event_id), reverse=True)
    session_events = sorted(session_events, key=lambda e: (e.timestamp_iso, e.session_id), reverse=True)
    
    return {
        "task_events": task_events,
        "session_events": session_events,
    }


def get_events_by_date(
    date_key: str,
    user_id: Optional[str] = None,
) -> Dict[str, List]:
    """
    Get all events for a specific date.
    Returns task, session, and activity events.
    
    Args:
        date_key: Date in YYYY-MM-DD format
        user_id: Optional user ID filter
        
    Returns:
        Dict with task_events, session_events lists
    """
    from .memory_store import get_activity_events
    
    task_events = get_task_events(user_id=user_id)
    session_events = get_session_events(user_id=user_id)
    activity_events = get_activity_events(user_id=user_id)
    
    # Filter by date
    task_events = [e for e in task_events if e.date_key == date_key]
    session_events = [e for e in session_events if e.date_key == date_key]
    activity_events = [e for e in activity_events if e.date_key == date_key]
    
    # Sort for determinism
    task_events = sorted(task_events, key=lambda e: (e.timestamp_iso, e.event_id), reverse=True)
    session_events = sorted(session_events, key=lambda e: (e.timestamp_iso, e.session_id), reverse=True)
    activity_events = sorted(activity_events, key=lambda e: (e.timestamp_iso, e.activity_id), reverse=True)
    
    return {
        "task_events": task_events,
        "session_events": session_events,
        "activity_events": activity_events,
    }


def get_events_by_difficulty(
    difficulty_bucket: str,
    user_id: Optional[str] = None,
) -> List[NormalizedTaskEvent]:
    """
    Get task events for a specific difficulty bucket.
    
    Args:
        difficulty_bucket: One of "easy", "medium", "hard", "extreme"
        user_id: Optional user ID filter
        
    Returns:
        List of normalized task events
    """
    task_events = get_task_events(user_id=user_id)
    
    # Filter by difficulty
    task_events = [e for e in task_events if e.difficulty_bucket == difficulty_bucket]
    
    # Sort for determinism
    task_events = sorted(task_events, key=lambda e: (e.timestamp_iso, e.event_id), reverse=True)
    
    return task_events
