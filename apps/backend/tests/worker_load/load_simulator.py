"""
Worker Load Simulator
Phase 7.12: Deterministic load simulation for worker stress testing

This module provides simulate_worker_load() which runs a worker multiple times
and collects performance metrics. All simulations are deterministic - no async,
no concurrency, no randomness.
"""
from collections import Counter
from typing import Any, Protocol, TypedDict
import sys
from pathlib import Path

# Add paths for imports
root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(root / "packages/shared/python"))
sys.path.insert(0, str(root / "apps/backend/src"))


# ============================================================================
# TYPE DEFINITIONS
# ============================================================================

class LatencyStats(TypedDict):
    """Latency statistics from load simulation."""
    min: float
    max: float
    avg: float
    p95: float
    p99: float


class LoadSimulationResult(TypedDict):
    """Result of a load simulation run."""
    runs: int
    success: int
    errors: int
    latency: LatencyStats
    rules_triggered: dict[str, int]
    metadata_examples: list[dict[str, Any]]


class WorkerProtocol(Protocol):
    """Protocol for workers that can be load tested."""
    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Execute the worker with given payload."""
        ...


# ============================================================================
# PERCENTILE CALCULATION
# ============================================================================

def calculate_percentile(sorted_values: list[float], percentile: float) -> float:
    """
    Calculate the percentile value from a sorted list.

    Args:
        sorted_values: Pre-sorted list of float values
        percentile: Percentile to calculate (0-100)

    Returns:
        The value at the given percentile
    """
    if not sorted_values:
        return 0.0

    n = len(sorted_values)
    if n == 1:
        return sorted_values[0]

    # Calculate index using linear interpolation
    k = (n - 1) * (percentile / 100.0)
    f = int(k)
    c = f + 1 if f + 1 < n else f

    # Linear interpolation between floor and ceiling
    if f == c:
        return sorted_values[f]

    d = k - f
    return sorted_values[f] * (1 - d) + sorted_values[c] * d


# ============================================================================
# LOAD SIMULATOR
# ============================================================================

def simulate_worker_load(
    worker: WorkerProtocol,
    payload: dict[str, Any],
    runs: int,
) -> LoadSimulationResult:
    """
    Simulate worker load by running it multiple times.

    Executes the worker in a deterministic loop (no concurrency) and collects:
    - Success/error counts
    - Latency statistics (min, max, avg, p95, p99)
    - Rules triggered (from metadata)
    - Sample metadata for inspection

    Args:
        worker: The worker instance to test
        payload: The payload to pass to each run
        runs: Number of times to run the worker

    Returns:
        LoadSimulationResult with all collected metrics
    """
    if runs < 1:
        raise ValueError("runs must be at least 1")

    # Collectors
    latencies: list[float] = []
    success_count = 0
    error_count = 0
    rules_triggered: Counter[str] = Counter()
    metadata_examples: list[dict[str, Any]] = []

    # Deterministic loop - no concurrency
    for i in range(runs):
        result = worker.run(payload)

        # Track success/error
        if result.get("success", False):
            success_count += 1
        else:
            error_count += 1

        # Collect latency from metadata
        metadata = result.get("metadata", {})
        duration_ms = metadata.get("duration_ms", 0.0)
        latencies.append(duration_ms)

        # Collect triggered rules from result data
        data = result.get("data", {})
        if data:
            # Check for _metadata.triggered_rules in result data
            inner_metadata = data.get("_metadata", {})
            triggered = inner_metadata.get("triggered_rules", [])
            for rule in triggered:
                rules_triggered[rule] += 1

            # Also check for triggered_rules in other locations
            if "triggered_rules" in data:
                for rule in data["triggered_rules"]:
                    rules_triggered[rule] += 1

        # Collect a few metadata examples (first 3)
        if len(metadata_examples) < 3:
            metadata_examples.append({
                "run": i + 1,
                "success": result.get("success", False),
                "duration_ms": duration_ms,
                "worker": metadata.get("worker", "unknown"),
                "task_type": metadata.get("task_type", "unknown"),
                "trace_id": metadata.get("trace_id", ""),
            })

    # Calculate latency statistics
    sorted_latencies = sorted(latencies)
    latency_stats = LatencyStats(
        min=min(latencies) if latencies else 0.0,
        max=max(latencies) if latencies else 0.0,
        avg=sum(latencies) / len(latencies) if latencies else 0.0,
        p95=calculate_percentile(sorted_latencies, 95),
        p99=calculate_percentile(sorted_latencies, 99),
    )

    return LoadSimulationResult(
        runs=runs,
        success=success_count,
        errors=error_count,
        latency=latency_stats,
        rules_triggered=dict(rules_triggered),
        metadata_examples=metadata_examples,
    )


# ============================================================================
# STRESS TEST HELPERS
# ============================================================================

def assert_load_result_valid(result: LoadSimulationResult) -> None:
    """
    Assert that a load simulation result meets minimum requirements.

    Raises:
        AssertionError: If any validation fails
    """
    assert result["runs"] > 0, "Must have at least 1 run"
    assert result["success"] > 0, "Must have at least 1 successful run"
    assert result["latency"]["min"] > 0, "Min latency must be positive"
    assert result["latency"]["avg"] < 50, "Avg latency should be under 50ms for static engine"
    assert result["latency"]["min"] <= result["latency"]["avg"], "Min should be <= avg"
    assert result["latency"]["avg"] <= result["latency"]["max"], "Avg should be <= max"
    assert result["latency"]["p95"] <= result["latency"]["p99"], "p95 should be <= p99"


def assert_deterministic(results: list[LoadSimulationResult]) -> None:
    """
    Assert that multiple load simulation results are deterministic.

    Compares success/error counts across multiple runs to ensure
    the worker behaves consistently.

    Args:
        results: List of LoadSimulationResult from multiple simulations

    Raises:
        AssertionError: If results show nondeterministic behavior
    """
    if len(results) < 2:
        return

    first = results[0]
    for i, result in enumerate(results[1:], start=2):
        assert result["success"] == first["success"], \
            f"Success count differs: run 1 had {first['success']}, run {i} had {result['success']}"
        assert result["errors"] == first["errors"], \
            f"Error count differs: run 1 had {first['errors']}, run {i} had {result['errors']}"
