# =============================================================================
# SQL SKILLSMAP - 20 NODER
# Database Querying & Management for DevOps
# =============================================================================

from .block_1_fundamentals import SQL_BLOCK_1
from .block_2_queries import SQL_BLOCK_2
from .block_3_advanced import SQL_BLOCK_3
from .block_4_optimization import SQL_BLOCK_4
from .block_5_production import SQL_BLOCK_5

SQL_SKILLSMAP_INFO = {
    "name": "SQL Mastery",
    "slug": "sql-mastery",
    "description": "Behärska SQL för databaser och DevOps",
    "total_nodes": 20,
    "estimated_hours": 25,
    "difficulty": "intermediate",
    "prerequisites": [],
    "skills": ["SQL", "PostgreSQL", "MySQL", "Database Design", "Query Optimization", "Indexing"],
}

SQL_SKILLSMAP_ALL_NODES = (
    SQL_BLOCK_1 +
    SQL_BLOCK_2 +
    SQL_BLOCK_3 +
    SQL_BLOCK_4 +
    SQL_BLOCK_5
)

# Validation
assert len(SQL_SKILLSMAP_ALL_NODES) == 20, f"Expected 20 nodes, got {len(SQL_SKILLSMAP_ALL_NODES)}"

print(f"✅ SQL SkillsMap COMPLETE: {len(SQL_SKILLSMAP_ALL_NODES)} nodes loaded")
