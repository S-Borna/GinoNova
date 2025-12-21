"""
Linux Mastery V3 - Naturlig Svensk Pedagogisk Stil
===================================================

Använder de omskrivna noderna från linux_skillsmap.py med:
- Naturliga svenska förklaringar med "Tänk på det som..." metaforer
- Bash-kodblock med kommentarer på VARJE rad
- Key Takeaways-sektioner
- INGA emojis i headers
- INGA tabeller
- INGA AI-Coach/Diagnostic/Playbook-sektioner

Track: foundation
Nodes: 20
Estimated Hours: 30
"""

from ..skillsmaps.linux_skillsmap import LINUX_SKILLSMAP_NODES, LINUX_SKILLSMAP_INFO


def _convert_node_to_task(node: dict) -> dict:
    """Convert a skillsmap node to a module task format."""
    # Map difficulty to standard values
    difficulty_map = {
        "beginner": "easy",
        "intermediate": "medium",
        "advanced": "hard",
        "expert": "hard"
    }

    return {
        "title": node.get("title", "Untitled"),
        "slug": node.get("slug", ""),
        "difficulty": difficulty_map.get(node.get("difficulty", "intermediate"), "medium"),
        "estimated_minutes": node.get("estimated_minutes", 45),
        "xp_reward": node.get("xp_reward", 75),
        "content": node.get("content", ""),
    }


# Convert all nodes to tasks
LINUX_V3_TASKS = [_convert_node_to_task(node) for node in LINUX_SKILLSMAP_NODES]


MODULE_LINUX_MASTERY_V3 = {
    "track_slug": "foundation",
    "order_index": 100,
    "name": "Linux Mastery",
    "slug": "linux-mastery",
    "description": LINUX_SKILLSMAP_INFO.get(
        "description",
        "Komplett Linux-administration - från filsystem till brandväggar med naturlig svensk pedagogik"
    ),
    "difficulty": "intermediate",
    "estimated_hours": LINUX_SKILLSMAP_INFO.get("estimated_hours", 30),
    "prerequisites": [],
    "icon": "🐧",
    "color": "#FCC624",
    "tasks": LINUX_V3_TASKS,
}


def get_linux_v3_module():
    """Return the Linux V3 module definition."""
    return MODULE_LINUX_MASTERY_V3


def get_linux_v3_tasks():
    """Return just the tasks for Linux V3."""
    return LINUX_V3_TASKS
