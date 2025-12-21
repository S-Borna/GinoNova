# =============================================================================
# GIT SKILLSMAP - 20 NODER
# Version Control Mastery
# =============================================================================

from .block_1_fundamentals import GIT_BLOCK_1
from .block_2_branching_part1 import BLOCK_2_PART_1_NODES
from .block_2_branching_part2 import BLOCK_2_PART_2_NODES
from .block_3_advanced_part1 import BLOCK_3_PART_1_NODES
from .block_3_advanced_part2 import BLOCK_3_PART_2_NODES
from .block_4_github_part1 import BLOCK_4_PART_1_NODES
from .block_4_github_part2 import BLOCK_4_PART_2_NODES
from .block_5_enterprise_part1 import BLOCK_5_PART_1_NODES
from .block_5_enterprise_part2 import BLOCK_5_PART_2_NODES

GIT_SKILLSMAP_INFO = {
    "name": "Git Mastery",
    "slug": "git-mastery",
    "description": "Behärska versionskontroll med Git från grunderna till enterprise-nivå",
    "total_nodes": 20,
    "estimated_hours": 30,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals"],
    "skills": ["Git", "GitHub", "Version Control", "CI/CD", "GitOps", "Branching Strategies"],
}

# Combine all blocks
_GIT_RAW_NODES = (
    GIT_BLOCK_1 +
    BLOCK_2_PART_1_NODES +
    BLOCK_2_PART_2_NODES +
    BLOCK_3_PART_1_NODES +
    BLOCK_3_PART_2_NODES +
    BLOCK_4_PART_1_NODES +
    BLOCK_4_PART_2_NODES +
    BLOCK_5_PART_1_NODES +
    BLOCK_5_PART_2_NODES
)

# Ensure all nodes have 'id' field (generate from slug or node_id if missing)
def _ensure_node_id(node, index):
    """Add 'id' field if missing, based on slug or index."""
    if "id" not in node or node.get("id") is None:
        slug = node.get("slug", f"git-node-{index + 1}")
        node["id"] = f"git_{slug.replace('-', '_')}"
    return node

GIT_SKILLSMAP_ALL_NODES = [
    _ensure_node_id(dict(node), i) for i, node in enumerate(_GIT_RAW_NODES)
]

# Validation
assert len(GIT_SKILLSMAP_ALL_NODES) == 20, f"Expected 20 nodes, got {len(GIT_SKILLSMAP_ALL_NODES)}"

print(f"✅ Git SkillsMap COMPLETE: {len(GIT_SKILLSMAP_ALL_NODES)} nodes loaded")
