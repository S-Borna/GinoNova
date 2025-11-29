"""
Badges API Routes - Phase 21
Badge awarding and tracking endpoints.
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/badges", tags=["badges"])


# Badge definitions with criteria
BADGE_DEFINITIONS = {
    # Skill badges
    "linux_beginner": {
        "name": "Linux Beginner",
        "category": "skill",
        "description": "Started learning Linux fundamentals",
        "max_level": 5,
        "criteria": {
            1: {"tasks_completed": 5, "module": "linux"},
            2: {"tasks_completed": 15, "module": "linux"},
            3: {"tasks_completed": 30, "module": "linux"},
            4: {"tasks_completed": 50, "module": "linux"},
            5: {"module_completed": True},
        },
        "xp_per_level": 50,
    },
    "git_master": {
        "name": "Git Master",
        "category": "skill",
        "description": "Mastering version control with Git",
        "max_level": 5,
        "criteria": {
            1: {"tasks_completed": 5, "module": "git"},
            2: {"tasks_completed": 15, "module": "git"},
            3: {"tasks_completed": 30, "module": "git"},
            4: {"tasks_completed": 50, "module": "git"},
            5: {"module_completed": True},
        },
        "xp_per_level": 50,
    },
    "docker_pro": {
        "name": "Docker Pro",
        "category": "skill",
        "description": "Containerization expert",
        "max_level": 5,
        "criteria": {
            1: {"tasks_completed": 5, "module": "docker"},
            2: {"tasks_completed": 15, "module": "docker"},
            3: {"tasks_completed": 30, "module": "docker"},
            4: {"tasks_completed": 50, "module": "docker"},
            5: {"module_completed": True},
        },
        "xp_per_level": 50,
    },
    "k8s_ninja": {
        "name": "Kubernetes Ninja",
        "category": "skill",
        "description": "Orchestration mastery",
        "max_level": 5,
        "criteria": {
            1: {"tasks_completed": 5, "module": "kubernetes"},
            2: {"tasks_completed": 15, "module": "kubernetes"},
            3: {"tasks_completed": 30, "module": "kubernetes"},
            4: {"tasks_completed": 50, "module": "kubernetes"},
            5: {"module_completed": True},
        },
        "xp_per_level": 75,
    },
    "cloud_architect": {
        "name": "Cloud Architect",
        "category": "skill",
        "description": "AWS/Cloud infrastructure expert",
        "max_level": 5,
        "criteria": {
            1: {"tasks_completed": 5, "module": "aws"},
            2: {"tasks_completed": 15, "module": "aws"},
            3: {"tasks_completed": 30, "module": "aws"},
            4: {"tasks_completed": 50, "module": "aws"},
            5: {"module_completed": True},
        },
        "xp_per_level": 75,
    },
    
    # Streak badges
    "streak_warrior": {
        "name": "Streak Warrior",
        "category": "streak",
        "description": "Consistent daily learning",
        "max_level": 5,
        "criteria": {
            1: {"streak_days": 7},
            2: {"streak_days": 14},
            3: {"streak_days": 30},
            4: {"streak_days": 60},
            5: {"streak_days": 100},
        },
        "xp_per_level": 100,
    },
    "early_bird": {
        "name": "Early Bird",
        "category": "streak",
        "description": "Study before 8 AM",
        "max_level": 3,
        "criteria": {
            1: {"early_sessions": 5},
            2: {"early_sessions": 20},
            3: {"early_sessions": 50},
        },
        "xp_per_level": 30,
    },
    "night_owl": {
        "name": "Night Owl",
        "category": "streak",
        "description": "Study after 10 PM",
        "max_level": 3,
        "criteria": {
            1: {"late_sessions": 5},
            2: {"late_sessions": 20},
            3: {"late_sessions": 50},
        },
        "xp_per_level": 30,
    },
    
    # Achievement badges
    "first_task": {
        "name": "First Steps",
        "category": "achievement",
        "description": "Completed your first task",
        "max_level": 1,
        "criteria": {1: {"tasks_completed": 1}},
        "xp_per_level": 25,
    },
    "module_master": {
        "name": "Module Master",
        "category": "achievement",
        "description": "Completed modules",
        "max_level": 5,
        "criteria": {
            1: {"modules_completed": 1},
            2: {"modules_completed": 3},
            3: {"modules_completed": 5},
            4: {"modules_completed": 10},
            5: {"modules_completed": 15},
        },
        "xp_per_level": 150,
    },
    "xp_collector": {
        "name": "XP Collector",
        "category": "achievement",
        "description": "Accumulated XP",
        "max_level": 5,
        "criteria": {
            1: {"total_xp": 500},
            2: {"total_xp": 2000},
            3: {"total_xp": 5000},
            4: {"total_xp": 10000},
            5: {"total_xp": 25000},
        },
        "xp_per_level": 100,
    },
}


# Response models
class BadgeResponse(BaseModel):
    slug: str
    name: str
    category: str
    level: int
    max_level: int
    awarded_at: Optional[datetime] = None


class BadgeDefinitionResponse(BaseModel):
    slug: str
    name: str
    category: str
    description: str
    max_level: int
    criteria: dict


@router.get("/")
async def get_my_badges(
    user_id: Optional[UUID] = Query(None, description="User ID")
):
    """
    Get all badges earned by a user.
    """
    # TODO: Implement actual database lookup
    return {
        "badges": [],
        "total_badges": 0,
        "total_xp_from_badges": 0
    }


@router.get("/available")
async def get_available_badges():
    """
    Get all available badge definitions.
    """
    return {
        "badges": [
            {
                "slug": slug,
                "name": data["name"],
                "category": data["category"],
                "description": data["description"],
                "max_level": data["max_level"],
            }
            for slug, data in BADGE_DEFINITIONS.items()
        ],
        "total": len(BADGE_DEFINITIONS)
    }


@router.get("/{badge_slug}")
async def get_badge_details(badge_slug: str):
    """
    Get details for a specific badge.
    """
    if badge_slug not in BADGE_DEFINITIONS:
        raise HTTPException(status_code=404, detail="Badge not found")
    
    data = BADGE_DEFINITIONS[badge_slug]
    return {
        "slug": badge_slug,
        "name": data["name"],
        "category": data["category"],
        "description": data["description"],
        "max_level": data["max_level"],
        "criteria": data["criteria"],
        "xp_per_level": data["xp_per_level"],
    }


@router.post("/check")
async def check_and_award_badges(
    user_id: Optional[UUID] = Query(None, description="User ID")
):
    """
    Check user's progress and award any earned badges.
    Should be called after completing tasks, modules, or other activities.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # TODO: Implement actual badge checking logic
    # 1. Get user's current badges
    # 2. Get user's progress/stats
    # 3. Check each badge criteria
    # 4. Award new badges if criteria met
    # 5. Return newly awarded badges
    
    new_badges = []
    
    logger.info(f"Badge check for user {user_id}: {len(new_badges)} new badges")
    
    return {
        "new_badges": new_badges,
        "total_checked": len(BADGE_DEFINITIONS),
        "message": "Badge check completed"
    }


@router.get("/leaderboard")
async def get_badge_leaderboard(limit: int = Query(10, le=100)):
    """
    Get leaderboard of users with most badges.
    """
    # TODO: Implement actual leaderboard
    return {
        "leaderboard": [],
        "limit": limit
    }
