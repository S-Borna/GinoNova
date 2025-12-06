"""
React & Next.js SkillsMap — Modern Frontend Development
========================================================

20 nodes covering React from fundamentals to production-ready Next.js apps.
Akhilesh-style pedagogy: Hook → Concept → Code → Pro Tips → Hands-on Task

Block 1 (Nodes 1-4): React Fundamentals
Block 2 (Nodes 5-8): State & Effects
Block 3 (Nodes 9-12): Advanced Patterns
Block 4 (Nodes 13-16): Next.js Framework
Block 5 (Nodes 17-20): Production & Testing

Total: 20 nodes, ~30 hours, 2000 XP
"""

from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_state_effects import BLOCK_2_NODES
from .block_3_advanced import BLOCK_3_NODES
from .block_4_nextjs import BLOCK_4_NODES
from .block_5_production import BLOCK_5_NODES

SKILLSMAP_METADATA = {
    "id": "react-nextjs-mastery",
    "slug": "react-nextjs-mastery",
    "title": "React & Next.js Mastery",
    "description": "Bygg moderna webbapplikationer med React och Next.js - från komponenter till produktion",
    "icon": "⚛️",
    "color": "#61DAFB",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "total_xp": 2000,
    "prerequisites": ["javascript", "typescript"],
    "tags": ["React", "Next.js", "Frontend", "Fullstack", "TypeScript", "SSR", "RSC"],
}

# Combine all nodes
ALL_NODES = BLOCK_1_NODES + BLOCK_2_NODES + BLOCK_3_NODES + BLOCK_4_NODES + BLOCK_5_NODES

def get_node_count():
    return len(ALL_NODES)

def get_total_xp():
    return sum(node.get("xp_reward", 100) for node in ALL_NODES)
