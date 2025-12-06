"""
Data Structures & Algorithms SkillsMap
======================================
Master the foundations of computer science and technical interviews.

Slug: dsa-mastery
Total Nodes: 20
Blocks: 5 (4 nodes each)
"""

# SkillsMap Metadata
SKILLSMAP_METADATA = {
    "slug": "dsa-mastery",
    "name": "DSA Mastery",
    "title": "Data Structures & Algorithms Mastery",
    "description": "Bemästra datastrukturer och algoritmer för tekniska intervjuer och effektiv kod",
    "icon": "🧮",
    "color": "#10B981",  # Emerald green
    "track_slug": "programming",
    "difficulty": "intermediate",
    "estimated_hours": 35,
    "tags": ["DSA", "Algorithms", "Data Structures", "Interviews", "Problem Solving"],
}

# Import nodes from blocks
from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_linear import BLOCK_2_NODES
from .block_3_trees_graphs import BLOCK_3_NODES
from .block_4_advanced import BLOCK_4_NODES
from .block_5_patterns import BLOCK_5_NODES

# Combine all nodes
ALL_NODES = BLOCK_1_NODES + BLOCK_2_NODES + BLOCK_3_NODES + BLOCK_4_NODES + BLOCK_5_NODES

# Verify node count
assert len(ALL_NODES) == 20, f"Expected 20 nodes, got {len(ALL_NODES)}"

print(f"✅ DSA SkillsMap COMPLETE: {len(ALL_NODES)} nodes loaded")
