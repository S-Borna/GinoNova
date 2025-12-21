"""
Linux Mastery V2 - Interactive Learning Engine Format
=====================================================

Uses V2 nodes with content_blocks for the ILE experience.

Track: foundation
Nodes: 20
Estimated Hours: 25
"""

from ..skillsmaps.v2_to_content_blocks import load_v2_linux_nodes

# Get all V2 tasks with content_blocks
_v2_tasks = load_v2_linux_nodes()

MODULE_LINUX_MASTERY_V2 = {
    "track_slug": "foundation",
    "order_index": 100,
    "name": "Linux Mastery",
    "slug": "linux-mastery-v2",  # New slug to avoid conflict
    "description": "Komplett Linux-administration - från processer till troubleshooting med interaktivt lärande",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": [],
    "icon": "🐧",
    "color": "#FCC624",
    "tasks": _v2_tasks,
}

# For backwards compatibility, also export with original name
# Uncomment below to replace old module:
# MODULE_LINUX_MASTERY = MODULE_LINUX_MASTERY_V2
