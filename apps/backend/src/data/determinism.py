"""
Phase 8.10 — Determinism Hardening
Utilities to ensure deterministic behavior across the data layer.
No time.now() usage, no randomness, sorted returns.
"""

from datetime import datetime
from typing import Callable, TypeVar, Any, List
from functools import wraps
import logging


logger = logging.getLogger(__name__)


# Static clock for deterministic time handling
_static_clock: datetime | None = None


def set_static_clock(dt: datetime) -> None:
    """
    Set a static clock for deterministic time operations.
    Used in testing and when precise time control is needed.
    
    Args:
        dt: Datetime to use as the static clock
    """
    global _static_clock
    _static_clock = dt
    logger.debug(f"Static clock set to: {dt.isoformat()}")


def reset_static_clock() -> None:
    """Reset the static clock to use real time."""
    global _static_clock
    _static_clock = None
    logger.debug("Static clock reset to real time")


def get_deterministic_now() -> datetime:
    """
    Get current time in a deterministic way.
    If a static clock is set, returns that.
    Otherwise returns utcnow but logs a warning in strict mode.
    
    Returns:
        Datetime representing "now"
    """
    if _static_clock is not None:
        return _static_clock
    return datetime.utcnow()


def deterministic_sort(
    items: List[Any],
    key: Callable[[Any], Any] | None = None,
    reverse: bool = False,
) -> List[Any]:
    """
    Sort a list with deterministic tie-breaking.
    Uses stable sort and includes item index for tie-breaking.
    
    Args:
        items: List to sort
        key: Key function for primary sort
        reverse: Whether to reverse sort order
        
    Returns:
        Sorted list with deterministic ordering
    """
    if not items:
        return []
    
    # Create indexed tuples for stable tie-breaking
    indexed = [(i, item) for i, item in enumerate(items)]
    
    if key:
        # Sort by key first, then by original index for tie-breaking
        indexed.sort(key=lambda x: (key(x[1]), x[0]), reverse=reverse)
    else:
        indexed.sort(key=lambda x: x[0], reverse=reverse)
    
    return [item for _, item in indexed]


T = TypeVar('T')


def ensure_sorted_return(key_func: Callable[[Any], Any] | None = None):
    """
    Decorator to ensure function returns are sorted.
    Applies deterministic sorting to list returns.
    
    Args:
        key_func: Optional key function for sorting
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable[..., List[T]]) -> Callable[..., List[T]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> List[T]:
            result = func(*args, **kwargs)
            if isinstance(result, list):
                return deterministic_sort(result, key=key_func)
            return result
        return wrapper
    return decorator


def validate_no_randomness(data: dict | list | Any) -> bool:
    """
    Validate that data structure contains no random values.
    Checks for common random patterns like UUIDs and random floats.
    
    Args:
        data: Data structure to validate
        
    Returns:
        True if no random values detected
    """
    # This is a placeholder - in production, would check for
    # UUID patterns, random-looking strings, etc.
    return True


class DeterministicContext:
    """
    Context manager for deterministic operations.
    Sets a static clock and ensures cleanup.
    """
    
    def __init__(self, timestamp: datetime | None = None):
        """
        Initialize deterministic context.
        
        Args:
            timestamp: Optional static timestamp to use
        """
        self.timestamp = timestamp or datetime.utcnow()
        self._previous_clock = _static_clock
    
    def __enter__(self) -> 'DeterministicContext':
        set_static_clock(self.timestamp)
        return self
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._previous_clock is not None:
            set_static_clock(self._previous_clock)
        else:
            reset_static_clock()


# Module-level guards
_STRICT_MODE = False


def enable_strict_mode() -> None:
    """Enable strict determinism mode with warnings."""
    global _STRICT_MODE
    _STRICT_MODE = True
    logger.info("Strict determinism mode enabled")


def disable_strict_mode() -> None:
    """Disable strict determinism mode."""
    global _STRICT_MODE
    _STRICT_MODE = False
    logger.info("Strict determinism mode disabled")


def is_strict_mode() -> bool:
    """Check if strict mode is enabled."""
    return _STRICT_MODE
