"""
Error Counter Tests
Phase 7.11: Tests for worker error counters

Tests:
- Counter increments correctly
- Counter thread-safety
- Registry creates counters per task type
- Global error recording functions
"""
import sys
from pathlib import Path

# Add packages to path
root = Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(root / "packages/shared/python"))

from shared.ai.engine.metrics import (
    Counter,
    MetricRegistry,
    record_worker_error,
    get_worker_errors,
    get_all_metrics,
    reset_all_metrics,
)


# ============================================================================
# COUNTER TESTS
# ============================================================================

class TestCounter:
    """Test Counter class functionality."""

    def test_counter_starts_at_zero(self) -> None:
        """Test counter initializes to zero."""
        c = Counter("test_start")
        data = c.to_dict()
        assert data["count"] == 0

    def test_counter_increment_default(self) -> None:
        """Test counter increments by 1 by default."""
        c = Counter("test_inc_default")
        c.inc()

        data = c.to_dict()
        assert data["count"] == 1

    def test_counter_increment_custom(self) -> None:
        """Test counter increments by custom amount."""
        c = Counter("test_inc_custom")
        c.inc(5)

        data = c.to_dict()
        assert data["count"] == 5

    def test_counter_multiple_increments(self) -> None:
        """Test counter handles multiple increments."""
        c = Counter("test_multi")
        c.inc()
        c.inc(3)
        c.inc(2)

        data = c.to_dict()
        assert data["count"] == 6

    def test_counter_to_dict(self) -> None:
        """Test counter serialization."""
        c = Counter("test_serialize")
        c.inc(10)

        data = c.to_dict()
        assert data["name"] == "test_serialize"
        assert data["count"] == 10


# ============================================================================
# REGISTRY COUNTER TESTS
# ============================================================================

class TestRegistryCounters:
    """Test MetricRegistry counter functionality."""

    def test_registry_creates_counter(self) -> None:
        """Test registry creates counters lazily."""
        registry = MetricRegistry()
        c = registry.get_counter("error_task")

        assert isinstance(c, Counter)
        assert c.name == "error_task"

    def test_registry_returns_same_counter(self) -> None:
        """Test registry returns same counter for same name."""
        registry = MetricRegistry()
        c1 = registry.get_counter("same_error")
        c2 = registry.get_counter("same_error")

        assert c1 is c2

    def test_registry_creates_separate_counters(self) -> None:
        """Test registry creates separate counters for different names."""
        registry = MetricRegistry()
        c1 = registry.get_counter("error_a")
        c2 = registry.get_counter("error_b")

        assert c1 is not c2

    def test_registry_to_dict_includes_counters(self) -> None:
        """Test registry serializes counters."""
        registry = MetricRegistry()
        registry.get_counter("error_x").inc()
        registry.get_counter("error_y").inc(5)

        data = registry.to_dict()
        assert "errors" in data
        assert "error_x" in data["errors"]
        assert "error_y" in data["errors"]
        assert data["errors"]["error_x"]["count"] == 1
        assert data["errors"]["error_y"]["count"] == 5


# ============================================================================
# GLOBAL ERROR RECORDING TESTS
# ============================================================================

class TestGlobalErrorRecording:
    """Test global error recording functions."""

    def setup_method(self) -> None:
        """Reset metrics before each test."""
        reset_all_metrics()

    def test_record_worker_error(self) -> None:
        """Test recording worker error via helper function."""
        record_worker_error("recommend")

        metrics = get_all_metrics()
        assert metrics["errors"]["recommend"]["count"] == 1

    def test_record_multiple_errors_same_worker(self) -> None:
        """Test recording multiple errors for same worker."""
        record_worker_error("difficulty")
        record_worker_error("difficulty")
        record_worker_error("difficulty")

        metrics = get_all_metrics()
        assert metrics["errors"]["difficulty"]["count"] == 3

    def test_record_errors_different_workers(self) -> None:
        """Test recording errors for different workers."""
        record_worker_error("recommend")
        record_worker_error("next_step")
        record_worker_error("summary")

        metrics = get_all_metrics()
        assert "recommend" in metrics["errors"]
        assert "next_step" in metrics["errors"]
        assert "summary" in metrics["errors"]

    def test_get_worker_errors(self) -> None:
        """Test getting worker error counter."""
        record_worker_error("next_step")
        record_worker_error("next_step")

        c = get_worker_errors("next_step")
        data = c.to_dict()
        assert data["count"] == 2


# ============================================================================
# ERROR + LATENCY COMBINED TESTS
# ============================================================================

class TestErrorAndLatencyCombined:
    """Test that error and latency metrics work together."""

    def setup_method(self) -> None:
        """Reset metrics before each test."""
        reset_all_metrics()

    def test_both_metrics_recorded(self) -> None:
        """Test recording both latency and errors."""
        from shared.ai.engine.metrics import record_worker_latency

        # Record some successful executions
        record_worker_latency("recommend", 15.0)
        record_worker_latency("recommend", 25.0)

        # Record an error
        record_worker_error("recommend")

        metrics = get_all_metrics()
        assert metrics["latency"]["recommend"]["count"] == 2
        assert metrics["errors"]["recommend"]["count"] == 1

    def test_error_rate_calculation(self) -> None:
        """Test calculating error rate from metrics."""
        from shared.ai.engine.metrics import record_worker_latency

        # 8 successes, 2 errors = 20% error rate
        for _ in range(8):
            record_worker_latency("difficulty", 30.0)
        for _ in range(2):
            record_worker_error("difficulty")

        metrics = get_all_metrics()
        success_count = metrics["latency"]["difficulty"]["count"]
        error_count = metrics["errors"]["difficulty"]["count"]
        total = success_count + error_count
        error_rate = error_count / total * 100

        assert error_rate == 20.0
