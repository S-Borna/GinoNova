"""
Prompt Engineering - V3 Premium Module
===========================================
Master the Art of AI Communication

20 Premium tasks with V3 pedagogical structure
"""

# Import from skillsmaps
from ..skillsmaps.prompt_engineering import PROMPT_ENGINEERING_NODES, PROMPT_ENGINEERING_METADATA


def convert_prompt_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"prompt-eng-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": f"Lär dig {node['title'].lower()} för prompt engineering",
        "xp_reward": node.get("xp_reward", 100),
        "estimated_minutes": node.get("estimated_minutes", 45),
        "order_index": idx + 1,
        "prerequisites": [f"prompt-eng-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium"
    }


# Convert all nodes to V3 tasks
PROMPT_ENGINEERING_V3_TASKS = [
    convert_prompt_node_to_v3_task(node, idx)
    for idx, node in enumerate(PROMPT_ENGINEERING_NODES)
]


MODULE_PROMPT_ENGINEERING = {
    "track_slug": "ai-mlops",
    "order_index": 1,
    "name": "Prompt Engineering",
    "slug": "prompt-engineering",
    "title": "Prompt Engineering",
    "description": "Bemästra konsten att kommunicera med AI-modeller effektivt. Från grundläggande prompt-tekniker till avancerade strategier för GPT-4, Claude och andra LLMs.",
    "icon": "🧠",
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "total_xp": sum(t.get("xp_reward", 100) for t in PROMPT_ENGINEERING_V3_TASKS),
    "prerequisites": [],
    "skills": ["Prompt Engineering", "LLMs", "GPT-4", "Claude", "AI Agents", "RAG", "Fine-tuning"],
    "tasks": PROMPT_ENGINEERING_V3_TASKS,
    "labs": [
        {
            "id": "prompt-eng-lab-1",
            "title": "Bygg en AI-assistant",
            "description": "Skapa en specialiserad AI-assistant med system prompts och few-shot examples",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 200
        },
        {
            "id": "prompt-eng-lab-2",
            "title": "Chain-of-Thought Prompting",
            "description": "Implementera avancerade reasoning-tekniker för komplexa problem",
            "difficulty": "advanced",
            "estimated_minutes": 75,
            "xp_reward": 250
        }
    ]
}


# Validation
assert len(MODULE_PROMPT_ENGINEERING["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_PROMPT_ENGINEERING['tasks'])}"
print(f"✅ Prompt Engineering V3: {len(MODULE_PROMPT_ENGINEERING['tasks'])} Premium tasks loaded")
