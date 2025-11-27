"""
Worker Performance Metrics
Phase 7.11: In-repo instrumentation for worker performance tracking

Provides:
- Histogram class for latency distribution
- Counter class for error counting
- Global registries for worker metrics

No external monitoring systems. Deterministic, in-memory only.
"""
from threading import Lock
from typing import Any


# ============================================================================
# HISTOGRAM CLASS
# ============================================================================

class Histogram:
    """
    Simple histogram for latency distribution tracking.

    Buckets: 0-5ms, 5-20ms, 20-50ms, 50-100ms, 100-250ms, 250-500ms, 500+ms
    Thread-safe with Lock.
    """

    # Bucket boundaries in milliseconds
    BUCKET_BOUNDS = [5, 20, 50, 100, 250, 500]
    BUCKET_LABELS = ["0-5ms", "5-20ms", "20-50ms", "50-100ms", "100-250ms", "250-500ms", "500+ms"]

    def __init__(self, name: str) -> None:
        """
        Initialize histogram with name.

        Args:
            name: Identifier for this histogram (e.g., task_type)
        """
        self.name = name
        self._lock = Lock()
        self._buckets = [0] * len(self.BUCKET_LABELS)
        self._count = 0
        self._sum = 0.0
        self._min: float | None = None
        self._max: float | None = None

    def record(self, value_ms: float) -> None:
        """
        Record a latency value in milliseconds.

        Args:
            value_ms: Latency value in milliseconds
        """
        with self._lock:
            self._count += 1
            self._sum += value_ms

            # Update min/max
            if self._min is None or value_ms < self._min:
                self._min = value_ms
            if self._max is None or value_ms > self._max:
                self._max = value_ms

            # Find bucket index
            bucket_idx = len(self.BUCKET_BOUNDS)  # Default to last bucket (500+)
            for i, bound in enumerate(self.BUCKET_BOUNDS):
                if value_ms < bound:
                    bucket_idx = i
                    break

            self._buckets[bucket_idx] += 1

    def to_dict(self) -> dict[str, Any]:
        """
        Export histogram data as dictionary.

        Returns:
            Dict with buckets, count, sum, min, max, avg
        """
        with self._lock:
            buckets = dict(zip(self.BUCKET_LABELS, self._buckets))
            avg = self._sum / self._count if self._count > 0 else 0.0

            return {
                "name": self.name,
                "count": self._count,
                "sum_ms": round(self._sum, 2),
                "min_ms": round(self._min, 2) if self._min is not None else None,
                "max_ms": round(self._max, 2) if self._max is not None else None,
                "avg_ms": round(avg, 2),
                "buckets": buckets,
            }

    def reset(self) -> None:
        """Reset histogram to initial state."""
        with self._lock:
            self._buckets = [0] * len(self.BUCKET_LABELS)
            self._count = 0
            self._sum = 0.0
            self._min = None
            self._max = None


# ============================================================================
# COUNTER CLASS
# ============================================================================

class Counter:
    """
    Simple counter for error counting.

    Thread-safe with Lock.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize counter with name.

        Args:
            name: Identifier for this counter (e.g., task_type)
        """
        self.name = name
        self._lock = Lock()
        self._value = 0

    def inc(self, amount: int = 1) -> None:
        """
        Increment counter.

        Args:
            amount: Amount to increment (default: 1)
        """
        with self._lock:
            self._value += amount

    def value(self) -> int:
        """Get current counter value."""
        with self._lock:
            return self._value

    def to_dict(self) -> dict[str, Any]:
        """
        Export counter data as dictionary.

        Returns:
            Dict with name and value
        """
        with self._lock:
            return {
                "name": self.name,
                "value": self._value,
            }

    def reset(self) -> None:
        """Reset counter to zero."""
        with self._lock:
            self._value = 0


# ============================================================================
# METRIC REGISTRY
# ============================================================================

class MetricRegistry:
    """
    Registry for managing metrics by task type.

    Provides lazy initialization of histograms and counters.
    """

    def __init__(self) -> None:
        """Initialize empty registry."""
        self._lock = Lock()
        self._histograms: dict[str, Histogram] = {}
        self._counters: dict[str, Counter] = {}

    def get_histogram(self, task_type: str) -> Histogram:
        """
        Get or create histogram for task type.

        Args:
            task_type: Worker task type identifier

        Returns:
            Histogram instance
        """
        with self._lock:
            if task_type not in self._histograms:
                self._histograms[task_type] = Histogram(f"worker_latency_{task_type}")
            return self._histograms[task_type]

    def get_counter(self, task_type: str) -> Counter:
        """
        Get or create counter for task type.

        Args:
            task_type: Worker task type identifier

        Returns:
            Counter instance
        """
        with self._lock:
            if task_type not in self._counters:
                self._counters[task_type] = Counter(f"worker_errors_{task_type}")
            return self._counters[task_type]

    def all_histograms(self) -> dict[str, dict[str, Any]]:
        """Get all histograms as dict."""
        with self._lock:
            return {k: v.to_dict() for k, v in self._histograms.items()}

    def all_counters(self) -> dict[str, dict[str, Any]]:
        """Get all counters as dict."""
        with self._lock:
            return {k: v.to_dict() for k, v in self._counters.items()}

    def to_dict(self) -> dict[str, Any]:
        """Export all metrics as dictionary."""
        return {
            "latency": self.all_histograms(),
            "errors": self.all_counters(),
        }

    def reset_all(self) -> None:
        """Reset all metrics."""
        with self._lock:
            for h in self._histograms.values():
                h.reset()
            for c in self._counters.values():
                c.reset()


# ============================================================================
# GLOBAL REGISTRIES
# ============================================================================

# Global metric registry instance
WORKER_METRICS = MetricRegistry()

# Convenience accessors
WORKER_LATENCY: dict[str, Histogram] = {}  # Populated lazily via registry
WORKER_ERRORS: dict[str, Counter] = {}  # Populated lazily via registry


def get_worker_latency(task_type: str) -> Histogram:
    """
    Get latency histogram for task type.

    Args:
        task_type: Worker task type (e.g., "recommend", "next_step")

    Returns:
        Histogram instance for recording latencies
    """
    return WORKER_METRICS.get_histogram(task_type)


def get_worker_errors(task_type: str) -> Counter:
    """
    Get error counter for task type.

    Args:
        task_type: Worker task type (e.g., "recommend", "next_step")

    Returns:
        Counter instance for counting errors
    """
    return WORKER_METRICS.get_counter(task_type)


def record_worker_latency(task_type: str, duration_ms: float) -> None:
    """
    Record worker latency.

    Args:
        task_type: Worker task type
        duration_ms: Execution duration in milliseconds
    """
    get_worker_latency(task_type).record(duration_ms)


def record_worker_error(task_type: str) -> None:
    """
    Increment worker error counter.

    Args:
        task_type: Worker task type
    """
    get_worker_errors(task_type).inc()


def get_all_metrics() -> dict[str, Any]:
    """
    Get all worker metrics.

    Returns:
        Dict with latency histograms and error counters
    """
    return WORKER_METRICS.to_dict()


def reset_all_metrics() -> None:
    """Reset all metrics to initial state."""
    WORKER_METRICS.reset_all()
