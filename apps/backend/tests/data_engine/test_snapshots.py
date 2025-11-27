"""
Phase 8.11 — Test Snapshots
Tests for the snapshot builder.
"""

import pytest
from datetime import datetime
from uuid import uuid4

from src.data.raw.raw_task_events import RawTaskEvent
from src.data.raw.raw_studyflow_sessions import RawStudyflowSession
from src.data.raw.raw_user_activity import RawUserActivity
from src.data.dispatcher.dispatcher import dispatch_event
from src.data.store.memory_store import clear_store
from src.data.store.snapshot_builder import (
    build_daily_snapshot,
    get_snapshot,
    get_all_snapshots,
)


class TestSnapshotBuilder:
    """Tests for snapshot builder."""

    def setup_method(self):
        """Clear store and add test data."""
        clear_store()
        self.user_id = uuid4()
        self.date_key = "2025-11-27"
        
        # Add task events
        for i in range(3):
            event = RawTaskEvent(
                event_id=f"evt_snap_{i}",
                event_type="task_completed" if i < 2 else "task_failed",
                user_id=self.user_id,
                task_id=uuid4(),
                timestamp=datetime(2025, 11, 27, 10 + i, 0, 0),
                difficulty=4 + i,
                xp_awarded=25 if i < 2 else 0,
            )
            dispatch_event(event, "task")
        
        # Add session events
        session = RawStudyflowSession(
            session_id="sess_snap_001",
            event_type="session_ended",
            user_id=self.user_id,
            timestamp=datetime(2025, 11, 27, 14, 0, 0),
            duration_minutes=45,
            focus_score=0.8,
        )
        dispatch_event(session, "session")
        
        # Add activity events
        activity = RawUserActivity(
            activity_id="act_snap_001",
            activity_type="xp_gained",
            user_id=self.user_id,
            timestamp=datetime(2025, 11, 27, 15, 0, 0),
            value_change=50,
        )
        dispatch_event(activity, "activity")

    def test_build_daily_snapshot(self):
        """Test building a daily snapshot."""
        snapshot = build_daily_snapshot(str(self.user_id), self.date_key)
        
        assert snapshot["user_id"] == str(self.user_id)
        assert snapshot["date_key"] == self.date_key
        assert "task_stats" in snapshot
        assert "difficulty_stats" in snapshot
        assert "studyflow_patterns" in snapshot
        assert "xp_deltas" in snapshot

    def test_snapshot_task_stats(self):
        """Test task stats in snapshot."""
        snapshot = build_daily_snapshot(str(self.user_id), self.date_key)
        
        task_stats = snapshot["task_stats"]
        assert task_stats["total_events"] == 3
        assert task_stats["completions"] == 2
        assert task_stats["failures"] == 1
        assert task_stats["total_xp"] == 50  # 25 + 25

    def test_snapshot_difficulty_stats(self):
        """Test difficulty stats in snapshot."""
        snapshot = build_daily_snapshot(str(self.user_id), self.date_key)
        
        diff_stats = snapshot["difficulty_stats"]
        assert "distribution" in diff_stats
        assert "completion_by_difficulty" in diff_stats

    def test_snapshot_studyflow_patterns(self):
        """Test studyflow patterns in snapshot."""
        snapshot = build_daily_snapshot(str(self.user_id), self.date_key)
        
        patterns = snapshot["studyflow_patterns"]
        assert patterns["total_sessions"] == 1
        assert patterns["total_duration_minutes"] == 45

    def test_snapshot_xp_deltas(self):
        """Test XP deltas in snapshot."""
        snapshot = build_daily_snapshot(str(self.user_id), self.date_key)
        
        xp = snapshot["xp_deltas"]
        assert xp["task_xp"] == 50
        assert xp["activity_xp"] == 50
        assert xp["total_xp"] == 100

    def test_get_snapshot(self):
        """Test retrieving a stored snapshot."""
        build_daily_snapshot(str(self.user_id), self.date_key)
        
        retrieved = get_snapshot(str(self.user_id), self.date_key)
        
        assert retrieved is not None
        assert retrieved["user_id"] == str(self.user_id)
        assert retrieved["date_key"] == self.date_key

    def test_get_snapshot_not_found(self):
        """Test retrieving non-existent snapshot."""
        result = get_snapshot(str(uuid4()), "2025-01-01")
        
        assert result is None

    def test_get_all_snapshots(self):
        """Test getting all snapshots."""
        build_daily_snapshot(str(self.user_id), "2025-11-27")
        build_daily_snapshot(str(self.user_id), "2025-11-26")
        
        snapshots = get_all_snapshots(user_id=str(self.user_id))
        
        assert len(snapshots) == 2
        # Should be sorted newest first
        assert snapshots[0]["date_key"] == "2025-11-27"
        assert snapshots[1]["date_key"] == "2025-11-26"

    def test_snapshot_empty_data(self):
        """Test snapshot with no matching data."""
        clear_store()
        
        snapshot = build_daily_snapshot(str(uuid4()), "2025-01-01")
        
        assert snapshot["task_stats"]["total_events"] == 0
        assert snapshot["studyflow_patterns"]["total_sessions"] == 0
