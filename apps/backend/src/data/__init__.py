# Phase 8 — Data Engineering Layer
# Exports for data layer modules

from .raw import RawTaskEvent, RawStudyflowSession, RawUserActivity
from .normalized import (
    normalize_task_event,
    normalize_studyflow_session,
    normalize_user_activity,
)
from .store import memory_store, snapshot_builder, indexes
from .dispatcher import dispatch_event
from .query import task_query, pattern_query, difficulty_query

__all__ = [
    # Raw models
    "RawTaskEvent",
    "RawStudyflowSession",
    "RawUserActivity",
    # Normalizers
    "normalize_task_event",
    "normalize_studyflow_session",
    "normalize_user_activity",
    # Store
    "memory_store",
    "snapshot_builder",
    "indexes",
    # Dispatcher
    "dispatch_event",
    # Query
    "task_query",
    "pattern_query",
    "difficulty_query",
]
