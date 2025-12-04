"""
Go Programming Mastery - Premium Module
DevOps-Ready Go Development
"""

from .basics import TASKS_BASICS
from .advanced import TASKS_ADVANCED

ALL_TASKS = TASKS_BASICS + TASKS_ADVANCED

MODULE_GO_MASTERY = {
    "track_slug": "programming",
    "order_index": 107,
    "name": "Go Programming Mastery",
    "slug": "go-mastery",
    "title": "Go Programming Mastery",
    "description": "Master Go programming for cloud-native development and DevOps tooling",
    "icon": "🐹",
    "category": "Programming Languages",
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "prerequisites": ["git-github-mastery"],
    "tasks": ALL_TASKS,
    "labs": []
}
