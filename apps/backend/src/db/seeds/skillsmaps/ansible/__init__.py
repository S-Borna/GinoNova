# =============================================================================
# ANSIBLE SKILLSMAP - 20 NODER
# Configuration Management & Automation
# =============================================================================

from .block_1_fundamentals import ANSIBLE_BLOCK_1
from .block_2_playbooks import ANSIBLE_BLOCK_2
from .block_3_advanced import ANSIBLE_BLOCK_3
from .block_4_modules import ANSIBLE_BLOCK_4
from .block_5_production import ANSIBLE_BLOCK_5

ANSIBLE_SKILLSMAP_INFO = {
    "name": "Ansible Mastery",
    "slug": "ansible-mastery",
    "description": "Behärska Configuration Management och Automation med Ansible",
    "total_nodes": 20,
    "estimated_hours": 25,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals", "bash-scripting"],
    "skills": ["Ansible", "Configuration Management", "Automation", "YAML", "Jinja2", "Idempotency"],
}

# Combine all blocks
_ANSIBLE_RAW_NODES = (
    ANSIBLE_BLOCK_1 +
    ANSIBLE_BLOCK_2 +
    ANSIBLE_BLOCK_3 +
    ANSIBLE_BLOCK_4 +
    ANSIBLE_BLOCK_5
)

# Ensure all nodes have 'id' field (generate from slug or node_id if missing)
def _ensure_node_id(node, index):
    """Add 'id' field if missing, based on slug or index."""
    if "id" not in node or node.get("id") is None:
        slug = node.get("slug", f"ansible-node-{index + 1}")
        node["id"] = f"ansible_{slug.replace('-', '_')}"
    return node

ANSIBLE_SKILLSMAP_ALL_NODES = [
    _ensure_node_id(dict(node), i) for i, node in enumerate(_ANSIBLE_RAW_NODES)
]

# Validation
assert len(ANSIBLE_SKILLSMAP_ALL_NODES) == 20, f"Expected 20 nodes, got {len(ANSIBLE_SKILLSMAP_ALL_NODES)}"

print(f"✅ Ansible SkillsMap COMPLETE: {len(ANSIBLE_SKILLSMAP_ALL_NODES)} nodes loaded")
