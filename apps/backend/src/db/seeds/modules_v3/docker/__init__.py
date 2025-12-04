"""
Docker Mastery - Premium Module
Complete Container Platform for DevOps
"""

from .fundamentals import TASKS_FUNDAMENTALS
from .advanced import TASKS_ADVANCED

MODULE_DOCKER_MASTERY = {
    "track_slug": "containers-orchestration",
    "order_index": 10,
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "title": "Docker Mastery",
    "description": "Master containerization from fundamentals to production-ready deployments",
    "icon": "🐳",
    "category": "Containerization",
    "difficulty": "intermediate",
    "estimated_hours": 22,
    "prerequisites": [],
    "tasks": TASKS_FUNDAMENTALS + TASKS_ADVANCED,
    "labs": []
}
