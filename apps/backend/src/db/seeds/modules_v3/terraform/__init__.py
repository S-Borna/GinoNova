"""
Terraform Mastery - Premium Module
Infrastructure as Code for Multi-Cloud
"""

from .part1_basics import TASKS_PART1
from .part2_modules import TASKS_PART2
from .part3_advanced import TASKS_PART3
from .part4_production import TASKS_PART4

MODULE_TERRAFORM_MASTERY = {
    "track_slug": "cloud-infrastructure",
    "order_index": 7,
    "name": "Terraform Mastery",
    "slug": "terraform-mastery",
    "title": "Terraform Mastery",
    "description": "Master Infrastructure as Code with Terraform for multi-cloud deployments",
    "icon": "🏗️",
    "category": "Infrastructure as Code",
    "difficulty": "advanced",
    "estimated_hours": 30,
    "prerequisites": ["aws-devops"],
    "tasks": TASKS_PART1 + TASKS_PART2 + TASKS_PART3 + TASKS_PART4,
    "labs": []
}
