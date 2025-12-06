"""
React & Next.js - V3 Premium Module
===========================================
Master modern frontend development with React and Next.js

20 Premium tasks with V3 pedagogical structure
From React fundamentals to production-ready Next.js apps
"""

# Import from skillsmaps
from ..skillsmaps.react import ALL_NODES, SKILLSMAP_METADATA


def convert_react_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"react-nextjs-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": node.get("description", f"Lär dig {node['title'].lower()}"),
        "xp_reward": node.get("xp_reward", 100),
        "estimated_minutes": node.get("estimated_minutes", 60),
        "order_index": idx + 1,
        "prerequisites": [f"react-nextjs-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium",
        "topics_covered": node.get("topics_covered", [])
    }


# Convert all nodes to V3 tasks
REACT_NEXTJS_V3_TASKS = [
    convert_react_node_to_v3_task(node, idx)
    for idx, node in enumerate(ALL_NODES)
]


MODULE_REACT_NEXTJS = {
    "track_slug": "frontend",
    "order_index": 1,  # Primary frontend module
    "name": "React & Next.js",
    "slug": "react-nextjs",
    "title": "React & Next.js Mastery",
    "description": SKILLSMAP_METADATA["description"],
    "icon": SKILLSMAP_METADATA["icon"],
    "difficulty": SKILLSMAP_METADATA["difficulty"],
    "estimated_hours": SKILLSMAP_METADATA["estimated_hours"],
    "total_xp": sum(t.get("xp_reward", 100) for t in REACT_NEXTJS_V3_TASKS),
    "prerequisites": SKILLSMAP_METADATA["prerequisites"],
    "skills": SKILLSMAP_METADATA["tags"] + ["Hooks", "Server Components", "App Router", "TailwindCSS"],
    "tasks": REACT_NEXTJS_V3_TASKS,
    "labs": [
        {
            "id": "react-nextjs-lab-1",
            "title": "Todo App med Local Storage",
            "description": "Bygg en komplett todo-app med React hooks och persistent storage",
            "difficulty": "beginner",
            "estimated_minutes": 60,
            "xp_reward": 150
        },
        {
            "id": "react-nextjs-lab-2",
            "title": "E-commerce Product Page",
            "description": "Skapa en produktsida med dynamic routing och server components",
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 250
        },
        {
            "id": "react-nextjs-lab-3",
            "title": "Dashboard med Auth",
            "description": "Bygg en dashboard med authentication, charts och real-time data",
            "difficulty": "advanced",
            "estimated_minutes": 120,
            "xp_reward": 350
        }
    ]
}


# Validation
assert len(MODULE_REACT_NEXTJS["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_REACT_NEXTJS['tasks'])}"
print(f"✅ React & Next.js V3: {len(MODULE_REACT_NEXTJS['tasks'])} Premium tasks loaded")
