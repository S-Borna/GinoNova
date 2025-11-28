"""
User Profile Router - Phase 9
API endpoints for user profile management
"""
from datetime import datetime
from uuid import UUID
from typing import Optional

from fastapi import APIRouter, Response, HTTPException, Query

from ..schemas.profile import (
    UserProfilePublic,
    UserProfileUpdate,
    UserStatsPublic,
    UserActivityResponse,
    UserActivityItem,
    LeaderboardResponse,
    LeaderboardEntry,
)
from ..core.deps import CurrentUser
from ..db.database import is_db_configured

profile_router = APIRouter()

# Phase version header
PHASE_VERSION = "9.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# LEVEL CALCULATIONS
# ==============================================================================

LEVEL_THRESHOLDS = [
    0, 100, 250, 500, 800, 1200, 1700, 2300, 3000, 3800,
    4700, 5700, 6800, 8000, 9500, 11000, 12800, 14800, 17000, 20000
]


def calculate_level(total_xp: int) -> int:
    """Calculate level from total XP"""
    for i in range(len(LEVEL_THRESHOLDS) - 1, -1, -1):
        if total_xp >= LEVEL_THRESHOLDS[i]:
            return i + 1
    return 1


def get_xp_for_level(level: int) -> int:
    """Get XP required for a level"""
    if level <= 1:
        return 0
    if level <= len(LEVEL_THRESHOLDS):
        return LEVEL_THRESHOLDS[level - 1]
    return LEVEL_THRESHOLDS[-1] + (level - len(LEVEL_THRESHOLDS)) * 3500


def calculate_level_progress(total_xp: int) -> tuple[int, int]:
    """Calculate XP to next level and progress percentage"""
    level = calculate_level(total_xp)
    current_threshold = get_xp_for_level(level)
    next_threshold = get_xp_for_level(level + 1)

    xp_to_next = next_threshold - total_xp
    level_range = next_threshold - current_threshold
    xp_into_level = total_xp - current_threshold
    progress = int((xp_into_level / level_range) * 100) if level_range > 0 else 100

    return xp_to_next, min(max(progress, 0), 100)


# ==============================================================================
# STATUS ENDPOINT
# ==============================================================================

@profile_router.get("/status")
def profile_status(response: Response):
    """Check profile module status"""
    add_phase_header(response)
    return {
        "profile": "configured",
        "phase": PHASE_VERSION,
        "database": "postgres" if is_db_configured() else "memory",
        "endpoints": ["get_profile", "update_profile", "get_stats", "get_activity", "get_leaderboard"]
    }


# ==============================================================================
# PROFILE ENDPOINTS
# ==============================================================================

@profile_router.get("/me", response_model=UserProfilePublic)
def get_my_profile(
    response: Response,
    current_user: CurrentUser
):
    """
    Get current user's profile with stats.
    """
    add_phase_header(response)

    # Calculate level - UserPublic doesn't have total_xp yet, default to 0
    total_xp = getattr(current_user, 'total_xp', 0)
    level = calculate_level(total_xp)

    # Get progress stats (simplified for now)
    tasks_completed = 0
    modules_completed = 0
    total_study_time = 0

    if is_db_configured():
        from ..db.hybrid_repository import progress_repo
        progress = progress_repo.get_by_user(current_user.id)
        tasks_completed = sum(1 for p in progress if p.task_id and p.status == "completed")

    return UserProfilePublic(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        avatar_url=getattr(current_user, 'avatar_url', None),
        bio=getattr(current_user, 'bio', None),
        github_username=getattr(current_user, 'github_username', None),
        linkedin_url=getattr(current_user, 'linkedin_url', None),
        website_url=getattr(current_user, 'website_url', None),
        timezone=getattr(current_user, 'timezone', 'UTC'),
        is_active=current_user.is_active,
        is_verified=getattr(current_user, 'is_verified', False),
        total_xp=total_xp,
        current_streak=getattr(current_user, 'current_streak', 0),
        longest_streak=getattr(current_user, 'longest_streak', 0),
        level=level,
        tasks_completed=tasks_completed,
        modules_completed=modules_completed,
        total_study_time=total_study_time,
        created_at=current_user.created_at,
        last_activity_at=getattr(current_user, 'last_activity_at', None),
    )


@profile_router.put("/me", response_model=UserProfilePublic)
def update_my_profile(
    data: UserProfileUpdate,
    response: Response,
    current_user: CurrentUser
):
    """
    Update current user's profile.
    """
    add_phase_header(response)

    update_data = data.model_dump(exclude_unset=True)

    updated_user = current_user

    if is_db_configured():
        from ..db.hybrid_repository import user_repo
        result = user_repo.update(current_user.id, update_data)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        updated_user = result
    else:
        # In-memory update - uses **kwargs
        from ..db.user_repository import update_user
        result = update_user(current_user.id, **update_data)
        if result:
            updated_user = result

    level = calculate_level(getattr(updated_user, 'total_xp', 0))

    return UserProfilePublic(
        id=updated_user.id,
        email=updated_user.email,
        full_name=getattr(updated_user, 'full_name', None),
        avatar_url=getattr(updated_user, 'avatar_url', None),
        bio=getattr(updated_user, 'bio', None),
        github_username=getattr(updated_user, 'github_username', None),
        linkedin_url=getattr(updated_user, 'linkedin_url', None),
        website_url=getattr(updated_user, 'website_url', None),
        timezone=getattr(updated_user, 'timezone', 'UTC'),
        is_active=updated_user.is_active,
        is_verified=getattr(updated_user, 'is_verified', False),
        total_xp=getattr(updated_user, 'total_xp', 0),
        current_streak=getattr(updated_user, 'current_streak', 0),
        longest_streak=getattr(updated_user, 'longest_streak', 0),
        level=level,
        tasks_completed=0,
        modules_completed=0,
        total_study_time=0,
        created_at=updated_user.created_at,
        last_activity_at=getattr(updated_user, 'last_activity_at', None),
    )


# ==============================================================================
# STATS ENDPOINT
# ==============================================================================

@profile_router.get("/me/stats", response_model=UserStatsPublic)
def get_my_stats(
    response: Response,
    current_user: CurrentUser
):
    """
    Get detailed statistics for current user.
    """
    add_phase_header(response)

    total_xp = getattr(current_user, 'total_xp', 0)
    level = calculate_level(total_xp)
    xp_to_next, level_progress = calculate_level_progress(total_xp)

    # Get progress counts
    tasks_completed = 0
    modules_completed = 0
    labs_completed = 0
    projects_completed = 0
    tasks_total = 0
    modules_total = 0

    if is_db_configured():
        from ..db.hybrid_repository import progress_repo, module_repo, task_repo

        progress = progress_repo.get_by_user(current_user.id)
        tasks_completed = sum(1 for p in progress if p.task_id and p.status == "completed")
        modules_completed = sum(1 for p in progress if p.module_id and p.status == "completed")
        labs_completed = sum(1 for p in progress if p.lab_id and p.status == "completed")
        projects_completed = sum(1 for p in progress if p.project_id and p.status == "completed")

        tasks_total = len(task_repo.get_all())
        modules_total = len(module_repo.get_all())
    else:
        from ..db.task_repository import list_tasks
        from ..db.module_repository import list_modules
        tasks_total = len(list_tasks())
        modules_total = len(list_modules())

    # Calculate streak status
    current_streak = getattr(current_user, 'current_streak', 0)
    last_activity = getattr(current_user, 'last_activity_at', None)
    streak_active = False
    if last_activity:
        days_since = (datetime.utcnow() - last_activity).days
        streak_active = days_since <= 1

    # Days since joined
    days_since_joined = (datetime.utcnow() - current_user.created_at).days

    return UserStatsPublic(
        user_id=current_user.id,
        total_xp=total_xp,
        level=level,
        xp_to_next_level=xp_to_next,
        level_progress_percent=level_progress,
        current_streak=current_streak,
        longest_streak=getattr(current_user, 'longest_streak', 0),
        streak_active=streak_active,
        tasks_completed=tasks_completed,
        tasks_total=tasks_total,
        modules_completed=modules_completed,
        modules_total=modules_total,
        labs_completed=labs_completed,
        projects_completed=projects_completed,
        total_study_time=0,  # TODO: Calculate from studyflow sessions
        sessions_completed=0,
        avg_session_length=0,
        last_activity_at=last_activity,
        days_since_joined=days_since_joined,
    )


# ==============================================================================
# ACTIVITY FEED
# ==============================================================================

@profile_router.get("/me/activity", response_model=UserActivityResponse)
def get_my_activity(
    response: Response,
    current_user: CurrentUser,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Get activity feed for current user.
    """
    add_phase_header(response)

    # TODO: Implement activity tracking table
    # For now, return empty activity feed
    activities: list[UserActivityItem] = []

    return UserActivityResponse(
        user_id=current_user.id,
        activities=activities,
        total_count=0,
        has_more=False,
    )


# ==============================================================================
# LEADERBOARD
# ==============================================================================

@profile_router.get("/leaderboard", response_model=LeaderboardResponse)
def get_leaderboard(
    response: Response,
    current_user: CurrentUser,
    leaderboard_type: str = Query("xp", pattern="^(xp|streak|weekly)$"),
    limit: int = Query(10, ge=1, le=100),
):
    """
    Get leaderboard rankings.

    Types:
    - xp: All-time XP leaderboard
    - streak: Current streak leaderboard
    - weekly: Weekly XP leaderboard
    """
    add_phase_header(response)

    entries: list[LeaderboardEntry] = []
    user_rank: Optional[int] = None
    total_users = 0

    if is_db_configured():
        from ..db.hybrid_repository import user_repo
        users = user_repo.list_all()
        total_users = len(users)

        # Sort by leaderboard type
        if leaderboard_type == "xp":
            sorted_users = sorted(users, key=lambda u: getattr(u, 'total_xp', 0), reverse=True)
        elif leaderboard_type == "streak":
            sorted_users = sorted(users, key=lambda u: getattr(u, 'current_streak', 0), reverse=True)
        else:  # weekly
            sorted_users = sorted(users, key=lambda u: getattr(u, 'total_xp', 0), reverse=True)

        # Build entries
        for rank, user in enumerate(sorted_users[:limit], 1):
            entries.append(LeaderboardEntry(
                rank=rank,
                user_id=user.id,
                full_name=getattr(user, 'full_name', None),
                avatar_url=getattr(user, 'avatar_url', None),
                total_xp=getattr(user, 'total_xp', 0),
                level=calculate_level(getattr(user, 'total_xp', 0)),
                current_streak=getattr(user, 'current_streak', 0),
            ))

            if user.id == current_user.id:
                user_rank = rank
    else:
        # In-memory fallback
        from ..db.user_repository import list_users
        users = list_users()
        total_users = len(users)

        sorted_users = sorted(users, key=lambda u: getattr(u, 'total_xp', 0), reverse=True)

        for rank, user in enumerate(sorted_users[:limit], 1):
            entries.append(LeaderboardEntry(
                rank=rank,
                user_id=user.id,
                full_name=getattr(user, 'full_name', None),
                avatar_url=getattr(user, 'avatar_url', None),
                total_xp=0,
                level=1,
                current_streak=0,
            ))

            if user.id == current_user.id:
                user_rank = rank

    return LeaderboardResponse(
        type=leaderboard_type,
        entries=entries,
        user_rank=user_rank,
        total_users=total_users,
    )


# ==============================================================================
# PUBLIC PROFILE (by ID)
# ==============================================================================

@profile_router.get("/{user_id}", response_model=UserProfilePublic)
def get_user_profile(
    user_id: UUID,
    response: Response,
):
    """
    Get public profile for a user by ID.
    """
    add_phase_header(response)

    user = None

    if is_db_configured():
        from ..db.hybrid_repository import user_repo
        user = user_repo.get_by_id(user_id)
    else:
        from ..db.user_repository import get_user_by_id
        user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    level = calculate_level(getattr(user, 'total_xp', 0))

    return UserProfilePublic(
        id=user.id,
        email=user.email,
        full_name=getattr(user, 'full_name', None),
        avatar_url=getattr(user, 'avatar_url', None),
        bio=getattr(user, 'bio', None),
        github_username=getattr(user, 'github_username', None),
        linkedin_url=getattr(user, 'linkedin_url', None),
        website_url=getattr(user, 'website_url', None),
        timezone=getattr(user, 'timezone', 'UTC'),
        is_active=user.is_active,
        is_verified=getattr(user, 'is_verified', False),
        total_xp=getattr(user, 'total_xp', 0),
        current_streak=getattr(user, 'current_streak', 0),
        longest_streak=getattr(user, 'longest_streak', 0),
        level=level,
        tasks_completed=0,
        modules_completed=0,
        total_study_time=0,
        created_at=user.created_at,
        last_activity_at=getattr(user, 'last_activity_at', None),
    )
