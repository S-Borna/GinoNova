"""
Kubernetes Mastery - Premium Module
Complete Container Orchestration for Production
"""

from .fundamentals import TASKS_FUNDAMENTALS
from .advanced import TASKS_ADVANCED

MODULE_KUBERNETES_MASTERY = {
    "track_slug": "containers-orchestration",
    "order_index": 12,
    "name": "Kubernetes Mastery",
    "slug": "kubernetes-mastery",
    "title": "Kubernetes Mastery",
    "description": "Master container orchestration from fundamentals to production-grade deployments",
    "icon": "☸️",
    "category": "Container Orchestration",
    "difficulty": "advanced",
    "estimated_hours": 25,
    "prerequisites": ["docker-mastery"],
    "tasks": TASKS_FUNDAMENTALS + TASKS_ADVANCED,
    "labs": []
}
