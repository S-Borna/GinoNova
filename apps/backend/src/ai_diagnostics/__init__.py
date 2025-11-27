"""
PHASE 7.14 — AI Error Isolation + Debug Frames

This module provides debug frame building and error isolation
for AI engine diagnostics. Pure observability layer with no
business logic changes.
"""

from .debug_frames import build_debug_frame, get_recent_debug_frames

__all__ = ["build_debug_frame", "get_recent_debug_frames"]
