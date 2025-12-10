# =============================================================================
# BASH SKILLSMAP V3 - ULTRA-PREMIUM BOOTCAMP-QUALITY CONTENT
# =============================================================================
# 20 noder med fullständigt pedagogiskt innehåll (~10,000-15,000 chars/nod)
# Strukturen: Intro -> Koncept -> ASCII-diagram -> Praktik -> Övningar
# =============================================================================

# Block 1: Bash Fundamentals (Nodes 1-4)
from .block_1_fundamentals_part1 import BLOCK_1_PART_1_NODES
from .block_1_fundamentals_part2 import BLOCK_1_PART_2_NODES

# Block 2: Variables & Control Flow (Nodes 5-8)
from .block_2_variables_part1 import BLOCK_2_PART_1_NODES
from .block_2_variables_part2 import BLOCK_2_PART_2_NODES

# Block 3: Functions & Advanced (Nodes 9-12)
from .block_3_functions_part1 import BLOCK_3_PART_1_NODES
from .block_3_functions_part2 import BLOCK_3_PART_2_NODES

# Block 4: Text Processing & Automation (Nodes 13-16)
from .block_4_textprocessing_part1 import BLOCK_4_PART_1_NODES
from .block_4_textprocessing_part2 import BLOCK_4_PART_2_NODES

# Block 5: DevOps & Production (Nodes 17-20)
from .block_5_devops_part1 import BLOCK_5_PART_1_NODES
from .block_5_devops_part2 import BLOCK_5_PART_2_NODES

SKILLSMAP_METADATA = {
    "name": "Bash Mastery V3",
    "slug": "bash-mastery",
    "description": "Behärska Bash-skriptning från grunden till avancerad automation. Premium bootcamp-kvalitet med djupgående teori, ASCII-diagram, praktiska övningar och DevOps-patterns.",
    "icon": "💻",
    "color": "#4EAA25",
    "track_id": "skillsmaps",
    "total_nodes": 20,
    "estimated_hours": 35,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals"],
    "skills": [
        "Bash", "Shell Scripting", "Variables", "Arrays", "Control Flow",
        "Functions", "Text Processing", "sed", "awk", "grep",
        "Process Management", "Automation", "DevOps Scripts", "Error Handling",
        "Debugging", "Best Practices", "Security", "Performance"
    ],
    "certification_available": True,
    "version": "3.0",
    "quality_standard": "linux-mastery-equivalent",
    "avg_chars_per_node": 12000,
}

# Combine all nodes in correct order
ALL_NODES = (
    BLOCK_1_PART_1_NODES +   # Nodes 1-2
    BLOCK_1_PART_2_NODES +   # Nodes 3-4
    BLOCK_2_PART_1_NODES +   # Nodes 5-6
    BLOCK_2_PART_2_NODES +   # Nodes 7-8
    BLOCK_3_PART_1_NODES +   # Nodes 9-10
    BLOCK_3_PART_2_NODES +   # Nodes 11-12
    BLOCK_4_PART_1_NODES +   # Nodes 13-14
    BLOCK_4_PART_2_NODES +   # Nodes 15-16
    BLOCK_5_PART_1_NODES +   # Nodes 17-18
    BLOCK_5_PART_2_NODES     # Nodes 19-20
)

__all__ = [
    "ALL_NODES",
    "SKILLSMAP_METADATA",
    "get_all_nodes",
    "get_node_count",
    "get_total_xp",
    "get_node_by_id",
    "get_node_by_slug",
    "validate_module",
]

def get_all_nodes():
    """Return all nodes in the Bash skillsmap."""
    return ALL_NODES

def get_node_count():
    """Return total number of nodes."""
    return len(ALL_NODES)

def get_total_xp():
    """Calculate total XP available in this skillsmap."""
    return sum(node.get("xp_reward", 100) for node in ALL_NODES)

def get_node_by_id(node_id: str):
    """Find a specific node by its ID."""
    for node in ALL_NODES:
        if node.get("id") == node_id:
            return node
    return None

def get_node_by_slug(slug: str):
    """Find a specific node by its slug."""
    for node in ALL_NODES:
        if node.get("slug") == slug:
            return node
    return None

def validate_module():
    """Validate the module structure."""
    errors = []
    if len(ALL_NODES) != 20:
        errors.append(f"Expected 20 nodes, got {len(ALL_NODES)}")
    for i, node in enumerate(ALL_NODES):
        if not node.get("content"):
            errors.append(f"Node {i+1} missing content")
        if len(node.get("content", "")) < 5000:
            errors.append(f"Node {i+1} content too short ({len(node.get('content', ''))} chars)")
    return errors if errors else None
