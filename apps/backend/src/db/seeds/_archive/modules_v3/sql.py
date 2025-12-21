"""
SQL Mastery - V3 Premium Module
===========================================
Database Querying & Management for DevOps

20 Premium tasks with V3 pedagogical structure
"""

# Import from skillsmaps
from ..skillsmaps.sql import SQL_SKILLSMAP_ALL_NODES, SQL_SKILLSMAP_INFO


def convert_sql_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"sql-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": f"Lär dig {node['title'].lower()} för SQL och databaser",
        "xp_reward": node.get("xp_reward", 100),
        "estimated_minutes": node.get("estimated_minutes", 45),
        "order_index": idx + 1,
        "prerequisites": [f"sql-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium"
    }


# Convert all nodes to V3 tasks
SQL_V3_TASKS = [
    convert_sql_node_to_v3_task(node, idx)
    for idx, node in enumerate(SQL_SKILLSMAP_ALL_NODES)
]


MODULE_SQL_MASTERY = {
    "track_slug": "backend-foundations",
    "order_index": 3,
    "name": "SQL Mastery",
    "slug": "sql-mastery",
    "title": "SQL Mastery",
    "description": "Behärska SQL för databaser och DevOps. Från grundläggande queries till avancerad optimering och produktionsdatabashantering.",
    "icon": "🗄️",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "total_xp": sum(t.get("xp_reward", 100) for t in SQL_V3_TASKS),
    "prerequisites": [],
    "skills": SQL_SKILLSMAP_INFO.get("skills", ["SQL", "PostgreSQL", "MySQL", "Database Design", "Query Optimization"]),
    "tasks": SQL_V3_TASKS,
    "labs": [
        {
            "id": "sql-lab-1",
            "title": "Designa DevOps-databas",
            "description": "Skapa en komplett databasschema för deployment-tracking",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 200
        },
        {
            "id": "sql-lab-2",
            "title": "Query Optimization Challenge",
            "description": "Optimera långsamma queries med index och EXPLAIN ANALYZE",
            "difficulty": "advanced",
            "estimated_minutes": 75,
            "xp_reward": 250
        }
    ]
}


# Validation
assert len(MODULE_SQL_MASTERY["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_SQL_MASTERY['tasks'])}"
print(f"✅ SQL Mastery V3: {len(MODULE_SQL_MASTERY['tasks'])} Premium tasks loaded")
