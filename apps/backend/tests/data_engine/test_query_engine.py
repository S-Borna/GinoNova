"""
Phase 8.11 — Test Query Engine
Tests for the data query engine.
"""

import pytest
from datetime import datetime
from uuid import uuid4

from src.data.raw.raw_task_events import RawTaskEvent
from src.data.raw.raw_studyflow_sessions import RawStudyflowSession
from src.data.dispatcher.dispatcher import dispatch_event
from src.data.store.memory_store import clear_store
from src.data.query.task_query import (
    query_user_tasks,
    query_task_completions,
    get_task_summary,
)
from src.data.query.pattern_query import (
    query_study_patterns,
    query_peak_hours,
    query_productivity_trends,
)
from src.data.query.difficulty_query import (
    query_difficulty_distribution,
    query_difficulty_performance,
    query_recommended_difficulty,
)


class TestTaskQuery:
    """Tests for task query engine."""

    def setup_method(self):
        """Clear store and add test data."""
        clear_store()
        self.user_id = uuid4()

        # Add test events
        for i in range(5):
            event = RawTaskEvent(
                event_id=f"evt_query_{i}",
                event_type="task_completed" if i % 2 == 0 else "task_failed",
                user_id=self.user_id,
                task_id=uuid4(),
                timestamp=datetime(2025, 11, 27, 10 + i, 0, 0),
                difficulty=3 + i,
                xp_awarded=10 * i if i % 2 == 0 else 0,
            )
            dispatch_event(event, "task")

    def test_query_user_tasks(self):
        """Test querying tasks for a user."""
        result = query_user_tasks(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert result["total_events"] == 5
        assert len(result["events"]) == 5

    def test_query_user_tasks_with_limit(self):
        """Test querying with limit."""
        result = query_user_tasks(str(self.user_id), limit=3)

        assert len(result["events"]) == 3

    def test_query_task_completions(self):
        """Test querying task completions."""
        result = query_task_completions(str(self.user_id), days=7)

        assert result["user_id"] == str(self.user_id)
        assert "totals" in result
        assert result["totals"]["completions"] == 3  # i=0,2,4
        assert result["totals"]["failures"] == 2  # i=1,3

    def test_get_task_summary(self):
        """Test getting task summary."""
        result = get_task_summary(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert result["has_data"] is True
        assert result["total_events"] == 5
        assert "summary" in result
        assert "completion_rate" in result["summary"]

    def test_get_task_summary_no_data(self):
        """Test task summary with no data."""
        result = get_task_summary(str(uuid4()))

        assert result["has_data"] is False
        assert result["total_events"] == 0


class TestPatternQuery:
    """Tests for pattern query engine."""

    def setup_method(self):
        """Clear store and add test session data."""
        clear_store()
        self.user_id = uuid4()

        # Add test sessions
        for i in range(3):
            session = RawStudyflowSession(
                session_id=f"sess_query_{i}",
                event_type="session_ended",
                user_id=self.user_id,
                timestamp=datetime(2025, 11, 27, 10 + i * 2, 0, 0),
                duration_minutes=30 + i * 10,
                focus_score=0.6 + i * 0.1,
                interruptions=i,
            )
            dispatch_event(session, "session")

    def test_query_study_patterns(self):
        """Test querying study patterns."""
        result = query_study_patterns(str(self.user_id), days=7)

        assert result["user_id"] == str(self.user_id)
        assert result["has_data"] is True
        assert "patterns" in result

    def test_query_peak_hours(self):
        """Test querying peak hours."""
        result = query_peak_hours(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert result["has_data"] is True
        assert "peak_hours" in result
        assert isinstance(result["peak_hours"], list)

    def test_query_productivity_trends(self):
        """Test querying productivity trends."""
        result = query_productivity_trends(str(self.user_id), days=14)

        assert result["user_id"] == str(self.user_id)
        assert "trend" in result

    def test_query_patterns_no_data(self):
        """Test patterns with no data."""
        result = query_study_patterns(str(uuid4()))

        assert result["has_data"] is False


class TestDifficultyQuery:
    """Tests for difficulty query engine."""

    def setup_method(self):
        """Clear store and add varied difficulty data."""
        clear_store()
        self.user_id = uuid4()

        # Add events with different difficulties
        difficulties = [2, 3, 5, 5, 6, 7, 8, 9]  # easy, easy, medium, medium, hard, hard, extreme, extreme
        event_types = ["task_completed", "task_completed", "task_completed", "task_failed",
                       "task_completed", "task_failed", "task_failed", "task_completed"]

        for i, (diff, etype) in enumerate(zip(difficulties, event_types)):
            event = RawTaskEvent(
                event_id=f"evt_diff_{i}",
                event_type=etype,
                user_id=self.user_id,
                task_id=uuid4(),
                timestamp=datetime(2025, 11, 27, 10, i, 0),
                difficulty=diff,
                xp_awarded=diff * 5 if etype == "task_completed" else 0,
            )
            dispatch_event(event, "task")

    def test_query_difficulty_distribution(self):
        """Test querying difficulty distribution."""
        result = query_difficulty_distribution(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert result["has_data"] is True
        assert "distribution" in result
        assert result["distribution"]["easy"] == 2
        assert result["distribution"]["medium"] == 2
        assert result["distribution"]["hard"] == 2
        assert result["distribution"]["extreme"] == 2

    def test_query_difficulty_performance(self):
        """Test querying difficulty performance."""
        result = query_difficulty_performance(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert result["has_data"] is True
        assert "performance" in result
        assert "easy" in result["performance"]
        assert "completion_rate" in result["performance"]["easy"]

    def test_query_recommended_difficulty(self):
        """Test getting recommended difficulty."""
        result = query_recommended_difficulty(str(self.user_id))

        assert result["user_id"] == str(self.user_id)
        assert "recommended" in result
        assert result["recommended"] in ["easy", "medium", "hard", "extreme"]

    def test_difficulty_no_data(self):
        """Test difficulty queries with no data."""
        result = query_difficulty_distribution(str(uuid4()))

        assert result["has_data"] is False
