"""
Azure Mastery V2 - Interactive Learning Engine Format
=====================================================

Uses V2 nodes with content_blocks for the ILE experience.

Track: cloud
Nodes: 20
Estimated Hours: 25
"""

from ..skillsmaps.v2_to_content_blocks import load_v2_azure_nodes

# Get all V2 tasks with content_blocks
_v2_tasks = load_v2_azure_nodes()

MODULE_AZURE_MASTERY_V2 = {
    "track_slug": "cloud",
    "order_index": 200,
    "name": "Azure Cloud Mastery",
    "slug": "azure-mastery-v2",  # New slug to avoid conflict
    "description": "Komplett guide till Microsoft Azure - från fundamentals till avancerade tjänster med interaktivt lärande",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "☁️",
    "color": "#0078D4",
    "tasks": _v2_tasks,
}
