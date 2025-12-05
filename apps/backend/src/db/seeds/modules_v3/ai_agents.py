"""
AI Agents - V3 Premium Module
===========================================
Design, Build and Ship AI Agents

20 Premium tasks with V3 pedagogical structure
Based on roadmap.sh/ai-agents
"""

# Import from skillsmaps
from ..skillsmaps.ai_agents import ALL_NODES, SKILLSMAP_METADATA


def convert_ai_agents_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"ai-agents-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": f"Lär dig {node['title'].lower()} för AI-agenter",
        "xp_reward": node.get("xp_reward", 120),
        "estimated_minutes": node.get("estimated_minutes", 90),
        "order_index": idx + 1,
        "prerequisites": [f"ai-agents-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium"
    }


# Convert all nodes to V3 tasks
AI_AGENTS_V3_TASKS = [
    convert_ai_agents_node_to_v3_task(node, idx)
    for idx, node in enumerate(ALL_NODES)
]


MODULE_AI_AGENTS = {
    "track_slug": "ai-mlops",
    "order_index": 2,  # After prompt-engineering
    "name": "AI Agents",
    "slug": "ai-agents",
    "title": "AI Agents",
    "description": SKILLSMAP_METADATA["description"],
    "icon": SKILLSMAP_METADATA["icon"],
    "difficulty": SKILLSMAP_METADATA["difficulty"],
    "estimated_hours": SKILLSMAP_METADATA["estimated_hours"],
    "total_xp": sum(t.get("xp_reward", 120) for t in AI_AGENTS_V3_TASKS),
    "prerequisites": SKILLSMAP_METADATA["prerequisites"],
    "skills": SKILLSMAP_METADATA["tags"] + ["Multi-Agent Systems", "Autonomous Agents", "Tool Use"],
    "tasks": AI_AGENTS_V3_TASKS,
    "labs": [
        {
            "id": "ai-agents-lab-1",
            "title": "Bygg en ReAct Agent",
            "description": "Skapa en agent som resonerar och agerar med verktyg",
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 250
        },
        {
            "id": "ai-agents-lab-2",
            "title": "Multi-Agent Workflow",
            "description": "Implementera ett multi-agent system med specialiserade agenter",
            "difficulty": "advanced",
            "estimated_minutes": 120,
            "xp_reward": 350
        },
        {
            "id": "ai-agents-lab-3",
            "title": "Production Agent med Monitoring",
            "description": "Deploya en agent med full observability och guardrails",
            "difficulty": "advanced",
            "estimated_minutes": 90,
            "xp_reward": 300
        }
    ]
}


# Validation
assert len(MODULE_AI_AGENTS["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_AI_AGENTS['tasks'])}"
print(f"✅ AI Agents V3: {len(MODULE_AI_AGENTS['tasks'])} Premium tasks loaded")
