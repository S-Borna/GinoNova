"""
Summary Worker Stress Tests
Phase 7.12: Deterministic stress testing for SummaryWorker

Tests run 100-300 iterations to verify:
- Consistent success/error counts (deterministic)
- Latency within acceptable bounds
- Rules triggered as expected
- No nondeterministic behavior
"""
import sys
from pathlib import Path

# Add paths for imports
root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(root / "packages/shared/python"))
sys.path.insert(0, str(root / "apps/backend/src"))

from workers import SummaryWorker
from .load_simulator import (
    simulate_worker_load,
    assert_load_result_valid,
    assert_deterministic,
)


# ============================================================================
# STATIC TEST FIXTURES (No randomness)
# ============================================================================

SUMMARY_PAYLOAD_BASIC = {
    "user_id": None,
}

SUMMARY_PAYLOAD_WITH_USER = {
    "user_id": "test-user-001",
}


# ============================================================================
# STRESS TESTS
# ============================================================================

class TestSummaryWorkerStress:
    """Stress tests for SummaryWorker."""

    def test_basic_load_100_runs(self) -> None:
        """Test 100 runs with basic payload."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=100)

        assert_load_result_valid(result)
        assert result["runs"] == 100
        assert result["success"] == 100, "All runs should succeed"
        assert result["errors"] == 0, "No errors expected"

    def test_with_user_150_runs(self) -> None:
        """Test 150 runs with user ID."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_WITH_USER, runs=150)

        assert_load_result_valid(result)
        assert result["runs"] == 150
        assert result["success"] == 150, "All runs should succeed"
        assert result["errors"] == 0, "No errors expected"

    def test_deterministic_behavior(self) -> None:
        """Verify worker produces deterministic results."""
        worker = SummaryWorker()

        # Run simulation 3 times
        results = [
            simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=50)
            for _ in range(3)
        ]

        # All runs should have same success/error counts
        assert_deterministic(results)

    def test_latency_bounds(self) -> None:
        """Verify latency stays within expected bounds."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=100)

        # Static engine should be fast
        assert result["latency"]["min"] > 0, "Min latency must be positive"
        assert result["latency"]["avg"] < 50, "Avg latency should be under 50ms"
        assert result["latency"]["p95"] < 100, "p95 should be under 100ms"
        assert result["latency"]["p99"] < 200, "p99 should be under 200ms"

    def test_rules_triggered(self) -> None:
        """Verify rules are triggered during execution."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_WITH_USER, runs=100)

        # Should have at least some rules triggered
        assert len(result["rules_triggered"]) >= 1, "Should trigger at least 1 rule"

    def test_metadata_examples_collected(self) -> None:
        """Verify metadata examples are collected."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=10)

        assert len(result["metadata_examples"]) == 3, "Should collect 3 examples"
        for example in result["metadata_examples"]:
            assert "run" in example
            assert "success" in example
            assert "duration_ms" in example
            assert "worker" in example
            assert "task_type" in example
            assert "trace_id" in example
            assert example["worker"] == "SummaryWorker"
            assert example["task_type"] == "summary"
            assert len(example["trace_id"]) == 32, "trace_id should be 32-char hex"

    def test_high_load_300_runs(self) -> None:
        """Test 300 runs for high load scenario."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=300)

        assert_load_result_valid(result)
        assert result["runs"] == 300
        assert result["success"] == 300, "All runs should succeed"
        assert result["errors"] == 0, "No errors expected"
        # Even at high load, avg latency should be reasonable
        assert result["latency"]["avg"] < 50, "Avg latency should stay under 50ms"

    def test_consistent_response_structure(self) -> None:
        """Verify response structure is consistent across runs."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=50)

        # All metadata examples should have same structure
        for example in result["metadata_examples"]:
            assert isinstance(example["run"], int)
            assert isinstance(example["success"], bool)
            assert isinstance(example["duration_ms"], float)
            assert isinstance(example["worker"], str)
            assert isinstance(example["task_type"], str)
            assert isinstance(example["trace_id"], str)

    def test_total_execution_reasonable(self) -> None:
        """Verify total execution time is reasonable."""
        worker = SummaryWorker()
        result = simulate_worker_load(worker, SUMMARY_PAYLOAD_BASIC, runs=100)

        # Total time should be sum * count roughly
        total_time = result["latency"]["avg"] * result["runs"]
        # 100 runs at avg < 50ms should be < 5000ms total
        assert total_time < 5000, "Total execution time should be under 5 seconds"
