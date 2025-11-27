"""
Trace ID Propagation Tests
Phase 7.11: Tests for trace_id validation and propagation

Tests:
- trace_id is 32-char hex string (uuid4.hex)
- trace_id validation function
- trace_id included in WorkerResult metadata
- trace_id propagation through worker execution
- duration_ms is positive after execution
"""
import re
import sys
from pathlib import Path

# Add packages to path
root = Path(__file__).parent.parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(root / "packages/shared/python"))
sys.path.insert(0, str(root / "apps/backend/src"))

from workers.worker_protocol import (
    validate_trace_id,
    TRACE_ID_PATTERN,
    ResultValidationError,
    validate_worker_result,
)


# ============================================================================
# TRACE ID FORMAT TESTS
# ============================================================================

class TestTraceIdFormat:
    """Test trace_id format requirements."""

    def test_trace_id_pattern_valid(self) -> None:
        """Test valid trace_id patterns."""
        valid_ids = [
            "a" * 32,
            "f" * 32,
            "0" * 32,
            "deadbeef" * 4,
            "0123456789abcdef" * 2,
        ]
        for trace_id in valid_ids:
            assert TRACE_ID_PATTERN.match(trace_id), f"Should match: {trace_id}"

    def test_trace_id_pattern_invalid(self) -> None:
        """Test invalid trace_id patterns are rejected."""
        invalid_ids = [
            "",
            "a" * 31,  # Too short
            "a" * 33,  # Too long
            "A" * 32,  # Uppercase not allowed
            "ghijklmn" * 4,  # Invalid hex chars
            "1234-5678-9abc-def0",  # Contains dashes
            "12345678 90abcdef 12345678 90abcdef",  # Contains spaces
        ]
        for trace_id in invalid_ids:
            assert not TRACE_ID_PATTERN.match(trace_id), f"Should not match: {trace_id}"

    def test_uuid4_hex_format(self) -> None:
        """Test that uuid4().hex produces valid trace_id."""
        from uuid import uuid4
        
        for _ in range(10):
            trace_id = uuid4().hex
            assert TRACE_ID_PATTERN.match(trace_id)
            assert len(trace_id) == 32


# ============================================================================
# TRACE ID VALIDATION FUNCTION TESTS
# ============================================================================

class TestValidateTraceId:
    """Test validate_trace_id function."""

    def test_valid_trace_id_passes(self) -> None:
        """Test valid trace_id passes validation."""
        valid_id = "a" * 32
        # Should not raise
        validate_trace_id(valid_id)

    def test_invalid_trace_id_raises(self) -> None:
        """Test invalid trace_id raises ResultValidationError."""
        invalid_id = "not-a-valid-trace-id"
        try:
            validate_trace_id(invalid_id)
            assert False, "Should have raised ResultValidationError"
        except ResultValidationError as e:
            assert "32-character lowercase hex" in str(e)

    def test_non_string_raises(self) -> None:
        """Test non-string trace_id raises error."""
        try:
            validate_trace_id(123)  # type: ignore
            assert False, "Should have raised ResultValidationError"
        except ResultValidationError as e:
            assert "must be a string" in str(e)

    def test_empty_string_raises(self) -> None:
        """Test empty string raises error."""
        try:
            validate_trace_id("")
            assert False, "Should have raised ResultValidationError"
        except ResultValidationError as e:
            assert "32-character lowercase hex" in str(e)


# ============================================================================
# WORKER RESULT METADATA TESTS
# ============================================================================

class TestWorkerResultMetadata:
    """Test trace_id in WorkerResult metadata."""

    def test_valid_result_with_trace_id(self) -> None:
        """Test valid WorkerResult with trace_id passes validation."""
        from datetime import datetime, timezone
        from uuid import uuid4
        
        result = {
            "success": True,
            "data": {"key": "value"},
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 15.5,
                "trace_id": uuid4().hex,
            },
        }
        # Should not raise
        validate_worker_result(result)

    def test_missing_trace_id_raises(self) -> None:
        """Test missing trace_id raises error."""
        from datetime import datetime, timezone
        
        result = {
            "success": True,
            "data": {"key": "value"},
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 15.5,
                # Missing trace_id
            },
        }
        try:
            validate_worker_result(result)
            assert False, "Should have raised ResultValidationError"
        except ResultValidationError as e:
            assert "trace_id" in str(e)

    def test_invalid_trace_id_format_raises(self) -> None:
        """Test invalid trace_id format raises error."""
        from datetime import datetime, timezone
        
        result = {
            "success": True,
            "data": {"key": "value"},
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 15.5,
                "trace_id": "invalid-trace-id",
            },
        }
        try:
            validate_worker_result(result)
            assert False, "Should have raised ResultValidationError"
        except ResultValidationError as e:
            assert "32-character lowercase hex" in str(e)


# ============================================================================
# WORKER EXECUTION PROPAGATION TESTS
# ============================================================================

class TestWorkerExecutionPropagation:
    """Test trace_id propagation through worker execution."""

    def test_recommend_worker_includes_trace_id(self) -> None:
        """Test RecommendWorker includes trace_id in result."""
        from workers import RecommendWorker
        
        worker = RecommendWorker()
        result = worker.run({
            "user_id": None,
            "limit": 5,
            "include_reasoning": False,
        })
        
        assert "metadata" in result
        assert "trace_id" in result["metadata"]
        assert TRACE_ID_PATTERN.match(result["metadata"]["trace_id"])

    def test_next_step_worker_includes_trace_id(self) -> None:
        """Test NextStepWorker includes trace_id in result."""
        from workers import NextStepWorker
        
        worker = NextStepWorker()
        result = worker.run({
            "user_id": None,
        })
        
        assert "metadata" in result
        assert "trace_id" in result["metadata"]
        assert TRACE_ID_PATTERN.match(result["metadata"]["trace_id"])

    def test_difficulty_worker_includes_trace_id(self) -> None:
        """Test DifficultyWorker includes trace_id in result."""
        from workers import DifficultyWorker
        
        worker = DifficultyWorker()
        result = worker.run({
            "user_id": None,
            "task_id": "test-task-123",
        })
        
        assert "metadata" in result
        assert "trace_id" in result["metadata"]
        assert TRACE_ID_PATTERN.match(result["metadata"]["trace_id"])

    def test_summary_worker_includes_trace_id(self) -> None:
        """Test SummaryWorker includes trace_id in result."""
        from workers import SummaryWorker
        
        worker = SummaryWorker()
        result = worker.run({
            "user_id": None,
        })
        
        assert "metadata" in result
        assert "trace_id" in result["metadata"]
        assert TRACE_ID_PATTERN.match(result["metadata"]["trace_id"])


# ============================================================================
# DURATION VALIDATION TESTS
# ============================================================================

class TestDurationValidation:
    """Test duration_ms is correctly calculated."""

    def test_duration_is_positive(self) -> None:
        """Test duration_ms is positive after execution."""
        from workers import RecommendWorker
        
        worker = RecommendWorker()
        result = worker.run({
            "user_id": None,
            "limit": 5,
            "include_reasoning": False,
        })
        
        assert result["metadata"]["duration_ms"] > 0

    def test_duration_is_float(self) -> None:
        """Test duration_ms is a float."""
        from workers import NextStepWorker
        
        worker = NextStepWorker()
        result = worker.run({
            "user_id": None,
        })
        
        assert isinstance(result["metadata"]["duration_ms"], float)

    def test_different_executions_have_unique_trace_ids(self) -> None:
        """Test each execution gets a unique trace_id."""
        from workers import RecommendWorker
        
        worker = RecommendWorker()
        trace_ids = set()
        
        for _ in range(5):
            result = worker.run({
                "user_id": None,
                "limit": 5,
                "include_reasoning": False,
            })
            trace_ids.add(result["metadata"]["trace_id"])
        
        # All trace_ids should be unique
        assert len(trace_ids) == 5
