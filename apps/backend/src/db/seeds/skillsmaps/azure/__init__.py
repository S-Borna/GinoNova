"""
Azure Cloud SkillsMap - Metadata & Index
========================================

Complete Azure cloud platform mastery from basics to advanced services.

Slug: azure-mastery
Icon: ☁️
Color: #0078D4 (Azure blue)
Nodes: 20 (5 blocks × 4 nodes)

Block Structure:
1. Azure Fundamentals (Nodes 1-4)
2. Compute & Networking (Nodes 5-8)
3. Storage & Databases (Nodes 9-12)
4. DevOps & Automation (Nodes 13-16)
5. Security & Monitoring (Nodes 17-20)
"""

from typing import Any

# Import all blocks
from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_compute import BLOCK_2_NODES
from .block_3_storage import BLOCK_3_NODES
from .block_4_devops import BLOCK_4_NODES
from .block_5_security import BLOCK_5_NODES

# SkillsMap metadata
SKILLSMAP_METADATA: dict[str, Any] = {
    "slug": "azure-mastery",
    "name": "Azure Cloud Mastery",
    "title": "Azure Cloud Mastery",
    "description": "Komplett guide till Microsoft Azure - från fundamentals till avancerade tjänster",
    "icon": "☁️",
    "color": "#0078D4",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "track_slug": "cloud",
    "tags": ["azure", "cloud", "microsoft", "iaas", "paas", "devops"],
}

# Combine all nodes
ALL_NODES = (
    BLOCK_1_NODES +
    BLOCK_2_NODES +
    BLOCK_3_NODES +
    BLOCK_4_NODES +
    BLOCK_5_NODES
)

# Verify node count
assert len(ALL_NODES) == 20, f"Expected 20 nodes, got {len(ALL_NODES)}"

print(f"✅ Azure SkillsMap COMPLETE: {len(ALL_NODES)} nodes loaded")
