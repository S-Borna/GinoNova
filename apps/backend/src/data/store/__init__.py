# Phase 8.3 — Storage Layer
# In-memory store with rolling windows and indexes

from .memory_store import (
    store_task_event,
    store_session_event,
    store_activity_event,
    get_task_events,
    get_session_events,
    get_activity_events,
    get_store_stats,
    clear_store,
)
from .snapshot_builder import (
    build_daily_snapshot,
    get_snapshot,
    get_all_snapshots,
)
from .indexes import (
    get_events_by_module,
    get_events_by_date,
    get_events_by_difficulty,
    rebuild_indexes,
)

__all__ = [
    # Memory store
    "store_task_event",
    "store_session_event",
    "store_activity_event",
    "get_task_events",
    "get_session_events",
    "get_activity_events",
    "get_store_stats",
    "clear_store",
    # Snapshot builder
    "build_daily_snapshot",
    "get_snapshot",
    "get_all_snapshots",
    # Indexes
    "get_events_by_module",
    "get_events_by_date",
    "get_events_by_difficulty",
    "rebuild_indexes",
]
