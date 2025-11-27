# Phase 8.4 — Event Dispatcher
# Deterministic event dispatch pipeline

from .dispatcher import dispatch_event, dispatch_batch

__all__ = [
    "dispatch_event",
    "dispatch_batch",
]
