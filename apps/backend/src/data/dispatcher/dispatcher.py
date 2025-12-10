"""
Phase 8.4 — Event Dispatcher
Deterministic dispatch pipeline: raw events -> normalizers -> store.
Integrates with Phase 7 telemetry.
"""

from typing import Union, List, Dict, Any
import logging

from ..raw.raw_task_events import RawTaskEvent
from ..raw.raw_studyflow_sessions import RawStudyflowSession
from ..raw.raw_user_activity import RawUserActivity
from ..normalized.tasks_normalizer import normalize_task_event
from ..normalized.session_normalizer import normalize_studyflow_session
from ..normalized.activity_normalizer import normalize_user_activity
from ..store.memory_store import (
    store_task_event,
    store_session_event,
    store_activity_event,
)

# Import Phase 7 telemetry
from ...ai_logs.logger import log_ai_event


logger = logging.getLogger(__name__)


# Event type mapping for deterministic dispatch
_EVENT_HANDLERS = {
    "task": {
        "raw_type": RawTaskEvent,
        "normalizer": normalize_task_event,
        "store": store_task_event,
    },
    "session": {
        "raw_type": RawStudyflowSession,
        "normalizer": normalize_studyflow_session,
        "store": store_session_event,
    },
    "activity": {
        "raw_type": RawUserActivity,
        "normalizer": normalize_user_activity,
        "store": store_activity_event,
    },
}


def dispatch_event(
    event: Union[RawTaskEvent, RawStudyflowSession, RawUserActivity],
    event_category: str,
) -> Dict[str, Any]:
    """
    Dispatch a single raw event through the pipeline.
    Deterministic order: validate -> normalize -> store -> log.
    No async operations.

    Args:
        event: Raw event to dispatch
        event_category: One of "task", "session", "activity"

    Returns:
        Dict with dispatch status and normalized event info
    """
    if event_category not in _EVENT_HANDLERS:
        raise ValueError(f"Unknown event category: {event_category}")

    handler = _EVENT_HANDLERS[event_category]

    # Step 1: Validate type (already done via Pydantic, but explicit check)
    if not isinstance(event, handler["raw_type"]):
        raise TypeError(
            f"Event type mismatch: expected {handler['raw_type'].__name__}, "
            f"got {type(event).__name__}"
        )

    # Step 2: Normalize (deterministic transformation)
    normalized = handler["normalizer"](event)

    # Step 3: Store in memory
    handler["store"](normalized)

    # Step 4: Log via Phase 7 telemetry
    _log_dispatch_event(event_category, normalized)

    logger.debug(
        f"Dispatched {event_category} event: {_get_event_id(event, event_category)}"
    )

    return {
        "status": "dispatched",
        "category": event_category,
        "event_id": _get_event_id(event, event_category),
        "normalized_keys": list(normalized.model_dump().keys()),
    }


def dispatch_batch(
    events: List[Union[RawTaskEvent, RawStudyflowSession, RawUserActivity]],
    event_category: str,
) -> Dict[str, Any]:
    """
    Dispatch a batch of raw events.
    Events are processed in deterministic order (as provided).

    Args:
        events: List of raw events to dispatch
        event_category: One of "task", "session", "activity"

    Returns:
        Dict with batch dispatch status
    """
    results = []
    errors = []

    for i, event in enumerate(events):
        try:
            result = dispatch_event(event, event_category)
            results.append(result)
        except Exception as e:
            errors.append({
                "index": i,
                "event_id": _get_event_id(event, event_category),
                "error": str(e),
            })
            logger.error(f"Batch dispatch error at index {i}: {e}")

    # Log batch telemetry
    log_ai_event(
        event_type="data_batch_dispatched",
        payload={
            "category": event_category,
            "total": len(events),
            "success": len(results),
            "errors": len(errors),
        },
        engine="data_dispatcher",
    )

    return {
        "status": "batch_complete",
        "category": event_category,
        "total": len(events),
        "success": len(results),
        "errors": errors,
    }


def _get_event_id(
    event: Union[RawTaskEvent, RawStudyflowSession, RawUserActivity],
    category: str,
) -> str:
    """Extract event ID based on category."""
    if category == "task" and isinstance(event, RawTaskEvent):
        return event.event_id
    elif category == "session" and isinstance(event, RawStudyflowSession):
        return event.session_id
    elif category == "activity" and isinstance(event, RawUserActivity):
        return event.activity_id
    return "unknown"


def _log_dispatch_event(category: str, normalized: Any) -> None:
    """Log dispatch event via Phase 7 telemetry."""
    payload_size = len(str(normalized.model_dump()))

    log_ai_event(
        event_type="data_event_dispatched",
        payload={
            "category": category,
            "layer": "data_engine",
            "payload_size": payload_size,
        },
        engine="data_dispatcher",
    )
