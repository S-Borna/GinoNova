"""
Cleanup Mock Data Script
========================
Removes ALL fake/seed progress data from the database.

- Deletes ALL TaskBlockProgress records
- Deletes ALL Progress records
- Deletes ALL StudyflowSession records
- Resets ALL users: total_xp=0, current_streak=0, longest_streak=0
- KEEPS user accounts intact
- KEEPS modules and tasks intact

Usage: python scripts/cleanup_mock_data.py
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from db import progress_repository, studyflow_repository, user_repository
from db.task_block_progress_repository import TASK_PROGRESS


def cleanup_mock_data():
    """Remove all mock/seed progress data."""
    print("🧹 Cleaning up mock data...")
    print("=" * 50)

    # 1. Clear TaskBlockProgress records
    task_block_count = len(TASK_PROGRESS)
    TASK_PROGRESS.clear()
    print(f"✅ Deleted {task_block_count} TaskBlockProgress records")

    # 2. Clear Progress records
    progress_count = len(progress_repository._progress_db)
    progress_repository.clear_progress()
    print(f"✅ Deleted {progress_count} Progress records")

    # 3. Clear StudyflowSession records
    studyflow_count = len(studyflow_repository._studyflows_db)
    studyflow_repository.clear_studyflows()
    print(f"✅ Deleted {studyflow_count} Studyflow records")

    # 4. Reset user stats
    users_reset = 0
    for user_id in list(user_repository._users_db.keys()):
        user = user_repository._users_db[user_id]
        # Reset XP and streaks but keep account
        user_data = user.model_dump()
        user_data['total_xp'] = 0
        user_data['current_streak'] = 0
        user_data['longest_streak'] = 0
        user_data['last_activity_at'] = None

        from schemas.user import UserInDB
        user_repository._users_db[user_id] = UserInDB(**user_data)
        users_reset += 1
        print(f"  ↳ Reset user: {user.email}")

    print(f"✅ Reset {users_reset} user stats to 0 XP, Level 1")

    print("=" * 50)
    print("🎉 Cleanup complete!")
    print("\nAll accounts should now show:")
    print("  - 0 XP")
    print("  - Level 1")
    print("  - 0 tasks completed")
    print("  - No recent sessions")


if __name__ == "__main__":
    cleanup_mock_data()
