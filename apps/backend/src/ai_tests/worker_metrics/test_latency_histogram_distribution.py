"""
Latency Histogram Distribution Tests
Phase 7.11: Tests for histogram bucket distribution

Tests:
- Histogram records values in correct buckets
- Bucket distribution matches expected bounds
- Histogram aggregates multiple samples correctly
- Registry creates histograms per task type
- Global WORKER_METRICS registry functions correctly
"""
import pytest
import sys
from pathlib import Path

# Add packages to path
root = Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(root / "packages/shared/python"))

from shared.ai.engine.metrics import (
    Histogram,
    MetricRegistry,
    WORKER_METRICS,
    record_worker_latency,
    get_all_metrics,
    reset_all_metrics,
    get_worker_latency,
)


# ============================================================================
# HISTOGRAM BUCKET TESTS
# ============================================================================

class TestHistogramBuckets:
    """Test histogram bucket distribution."""

    def test_bucket_bounds(self) -> None:
        """Verify histogram bucket bounds are correct."""
        assert Histogram.BUCKET_BOUNDS == [5, 20, 50, 100, 250, 500]
        assert Histogram.BUCKET_LABELS == [
            "0-5ms", "5-20ms", "20-50ms", "50-100ms", "100-250ms", "250-500ms", "500+ms"
        ]

    def test_record_in_first_bucket(self) -> None:
        """Test recording value in 0-5ms bucket."""
        h = Histogram("test_first_bucket")
        h.record(3.0)
        
        data = h.to_dict()
        assert data["buckets"]["0-5ms"] == 1
        assert data["count"] == 1
        assert data["sum_ms"] == 3.0

    def test_record_in_middle_bucket(self) -> None:
        """Test recording value in 50-100ms bucket."""
        h = Histogram("test_middle_bucket")
        h.record(75.0)
        
        data = h.to_dict()
        assert data["buckets"]["50-100ms"] == 1
        assert data["count"] == 1
        assert data["sum_ms"] == 75.0

    def test_record_in_last_bucket(self) -> None:
        """Test recording value in 500+ms bucket."""
        h = Histogram("test_last_bucket")
        h.record(750.0)
        
        data = h.to_dict()
        assert data["buckets"]["500+ms"] == 1
        assert data["count"] == 1
        assert data["sum_ms"] == 750.0

    def test_boundary_values(self) -> None:
        """Test values exactly at bucket boundaries."""
        h = Histogram("test_boundaries")
        
        # Exactly 5ms should go to 0-5ms bucket (<=)
        h.record(5.0)
        # Exactly 20ms should go to 5-20ms bucket (<=)
        h.record(20.0)
        # Exactly 500ms should go to 250-500ms bucket (<=)
        h.record(500.0)
        
        data = h.to_dict()
        assert data["buckets"]["0-5ms"] == 1
        assert data["buckets"]["5-20ms"] == 1
        assert data["buckets"]["250-500ms"] == 1
        assert data["count"] == 3

    def test_multiple_records_same_bucket(self) -> None:
        """Test multiple records in the same bucket."""
        h = Histogram("test_multiple_same")
        h.record(10.0)
        h.record(12.0)
        h.record(15.0)
        
        data = h.to_dict()
        assert data["buckets"]["5-20ms"] == 3
        assert data["count"] == 3
        assert data["sum_ms"] == 37.0

    def test_multiple_records_different_buckets(self) -> None:
        """Test records across different buckets."""
        h = Histogram("test_multiple_different")
        h.record(2.0)   # 0-5ms
        h.record(30.0)  # 20-50ms
        h.record(150.0) # 100-250ms
        h.record(600.0) # 500+ms
        
        data = h.to_dict()
        assert data["buckets"]["0-5ms"] == 1
        assert data["buckets"]["20-50ms"] == 1
        assert data["buckets"]["100-250ms"] == 1
        assert data["buckets"]["500+ms"] == 1
        assert data["count"] == 4
        assert data["sum_ms"] == 782.0

    def test_min_max_tracking(self) -> None:
        """Test min/max value tracking."""
        h = Histogram("test_minmax")
        h.record(50.0)
        h.record(10.0)
        h.record(100.0)
        
        data = h.to_dict()
        assert data["min_ms"] == 10.0
        assert data["max_ms"] == 100.0

    def test_average_calculation(self) -> None:
        """Test average calculation."""
        h = Histogram("test_average")
        h.record(10.0)
        h.record(20.0)
        h.record(30.0)
        
        data = h.to_dict()
        assert data["avg_ms"] == 20.0

    def test_empty_histogram(self) -> None:
        """Test empty histogram returns zeroes."""
        h = Histogram("test_empty")
        
        data = h.to_dict()
        assert data["count"] == 0
        assert data["sum_ms"] == 0.0
        assert data["min_ms"] == 0.0
        assert data["max_ms"] == 0.0
        assert data["avg_ms"] == 0.0


# ============================================================================
# METRIC REGISTRY TESTS
# ============================================================================

class TestMetricRegistry:
    """Test MetricRegistry lazy initialization."""

    def test_registry_creates_histogram(self) -> None:
        """Test registry creates histograms lazily."""
        registry = MetricRegistry()
        h = registry.get_histogram("new_task")
        
        assert isinstance(h, Histogram)
        assert h.name == "new_task"

    def test_registry_returns_same_histogram(self) -> None:
        """Test registry returns same histogram for same name."""
        registry = MetricRegistry()
        h1 = registry.get_histogram("same_task")
        h2 = registry.get_histogram("same_task")
        
        assert h1 is h2

    def test_registry_creates_separate_histograms(self) -> None:
        """Test registry creates separate histograms for different names."""
        registry = MetricRegistry()
        h1 = registry.get_histogram("task_a")
        h2 = registry.get_histogram("task_b")
        
        assert h1 is not h2

    def test_registry_to_dict(self) -> None:
        """Test registry serializes all histograms."""
        registry = MetricRegistry()
        registry.get_histogram("task_x").record(10.0)
        registry.get_histogram("task_y").record(20.0)
        
        data = registry.to_dict()
        assert "latency" in data
        assert "task_x" in data["latency"]
        assert "task_y" in data["latency"]


# ============================================================================
# GLOBAL WORKER_METRICS TESTS
# ============================================================================

class TestGlobalWorkerMetrics:
    """Test global WORKER_METRICS registry."""

    def setup_method(self) -> None:
        """Reset metrics before each test."""
        reset_all_metrics()

    def test_record_worker_latency(self) -> None:
        """Test recording worker latency via helper function."""
        record_worker_latency("recommend", 15.0)
        
        metrics = get_all_metrics()
        assert metrics["latency"]["recommend"]["count"] == 1
        assert metrics["latency"]["recommend"]["sum_ms"] == 15.0

    def test_get_worker_latency(self) -> None:
        """Test getting worker latency histogram."""
        record_worker_latency("next_step", 25.0)
        
        h = get_worker_latency("next_step")
        data = h.to_dict()
        assert data["count"] == 1

    def test_multiple_workers(self) -> None:
        """Test metrics for multiple workers."""
        record_worker_latency("recommend", 10.0)
        record_worker_latency("difficulty", 30.0)
        record_worker_latency("summary", 50.0)
        record_worker_latency("next_step", 70.0)
        
        metrics = get_all_metrics()
        assert "recommend" in metrics["latency"]
        assert "difficulty" in metrics["latency"]
        assert "summary" in metrics["latency"]
        assert "next_step" in metrics["latency"]

    def test_reset_all_metrics(self) -> None:
        """Test resetting all metrics."""
        record_worker_latency("recommend", 10.0)
        reset_all_metrics()
        
        metrics = get_all_metrics()
        # After reset, latency dict should be empty
        assert metrics["latency"] == {}


# ============================================================================
# BUCKET DISTRIBUTION VERIFICATION
# ============================================================================

class TestBucketDistribution:
    """Verify bucket distribution across all bucket ranges."""

    def test_all_buckets_covered(self) -> None:
        """Test that all bucket ranges work correctly."""
        h = Histogram("test_all_buckets")
        
        # Record one value in each bucket
        test_values = [
            (1.0, "0-5ms"),
            (10.0, "5-20ms"),
            (35.0, "20-50ms"),
            (75.0, "50-100ms"),
            (175.0, "100-250ms"),
            (350.0, "250-500ms"),
            (750.0, "500+ms"),
        ]
        
        for value, expected_bucket in test_values:
            h.record(value)
        
        data = h.to_dict()
        for _, bucket_label in test_values:
            assert data["buckets"][bucket_label] >= 1, f"Bucket {bucket_label} should have at least 1 record"

    def test_bucket_percentages(self) -> None:
        """Test bucket percentage calculation."""
        h = Histogram("test_percentages")
        
        # 10 total records
        for _ in range(5):
            h.record(3.0)  # 0-5ms
        for _ in range(3):
            h.record(30.0)  # 20-50ms
        for _ in range(2):
            h.record(600.0)  # 500+ms
        
        data = h.to_dict()
        # 5/10 = 50%, 3/10 = 30%, 2/10 = 20%
        assert data["buckets"]["0-5ms"] == 5
        assert data["buckets"]["20-50ms"] == 3
        assert data["buckets"]["500+ms"] == 2
        assert data["count"] == 10
