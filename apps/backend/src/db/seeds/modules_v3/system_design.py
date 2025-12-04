"""
System Design - V3 Premium Module
===========================================
Design Scalable, Robust & High-Performance Systems

20 Premium tasks with V3 pedagogical structure
"""

# Import from skillsmaps
from ..skillsmaps.system_design import SYSTEM_DESIGN_NODES, SYSTEM_DESIGN_METADATA


def convert_system_design_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"system-design-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": f"Lär dig {node['title'].lower()} för system design",
        "xp_reward": node.get("xp_reward", 100),
        "estimated_minutes": node.get("estimated_minutes", 45),
        "order_index": idx + 1,
        "prerequisites": [f"system-design-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium"
    }


# Convert all nodes to V3 tasks
SYSTEM_DESIGN_V3_TASKS = [
    convert_system_design_node_to_v3_task(node, idx)
    for idx, node in enumerate(SYSTEM_DESIGN_NODES)
]


MODULE_SYSTEM_DESIGN = {
    "track_slug": "platform-engineering",
    "order_index": 10,
    "name": "System Design",
    "slug": "system-design",
    "title": "System Design",
    "description": "Designa skalbara, robusta och högpresterande system. Från grundläggande koncept som CAP-teoremet till avancerade arkitekturmönster för miljontals användare.",
    "icon": "🏗️",
    "difficulty": "advanced",
    "estimated_hours": 35,
    "total_xp": sum(t.get("xp_reward", 100) for t in SYSTEM_DESIGN_V3_TASKS),
    "prerequisites": ["sql-mastery", "linux-mastery"],
    "skills": ["System Design", "Scalability", "Distributed Systems", "CAP Theorem", "Load Balancing", "Caching", "Database Sharding"],
    "tasks": SYSTEM_DESIGN_V3_TASKS,
    "labs": [
        {
            "id": "system-design-lab-1",
            "title": "Design URL Shortener",
            "description": "Designa en skalbar URL-förkortare som bit.ly",
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 300
        },
        {
            "id": "system-design-lab-2",
            "title": "Design Twitter Feed",
            "description": "Designa en skalbar social media feed med miljontals användare",
            "difficulty": "advanced",
            "estimated_minutes": 120,
            "xp_reward": 400
        }
    ]
}


# Validation
assert len(MODULE_SYSTEM_DESIGN["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_SYSTEM_DESIGN['tasks'])}"
print(f"✅ System Design V3: {len(MODULE_SYSTEM_DESIGN['tasks'])} Premium tasks loaded")
