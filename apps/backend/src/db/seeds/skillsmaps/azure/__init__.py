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

# Import V2 nodes
from .block_1_v2 import AZURE_NODE_1_INTRO_V2
from .block_1_node2_v2 import AZURE_NODE_2_V2
from .block_1_node3_v2 import AZURE_NODE_3_V2
from .block_1_node4_v2 import AZURE_NODE_4_V2
from .block_2_node5_v2 import AZURE_NODE_5_V2
from .block_2_node6_v2 import AZURE_NODE_6_V2
from .block_2_node7_v2 import AZURE_NODE_7_V2
from .block_2_node8_v2 import AZURE_NODE_8_V2
from .block_3_node9_v2 import AZURE_NODE_9_V2
from .block_3_node10_v2 import AZURE_NODE_10_SQL_V2
from .block_3_node11_v2 import AZURE_NODE_11_COSMOS_V2
from .block_3_node12_v2 import AZURE_NODE_12_REDIS_V2
from .block_4_node13_v2 import AZURE_NODE_13_DEVOPS_V2
from .block_4_node14_v2 import AZURE_NODE_14_ACR_V2
from .block_4_node15_v2 import AZURE_NODE_15_BICEP_V2
from .block_4_node16_v2 import AZURE_NODE_16_PIPELINES_V2
from .block_5_node17_v2 import AZURE_NODE_17_ENTRA_V2
from .block_5_node18_v2 import AZURE_NODE_18_KEYVAULT_V2
from .block_5_node19_v2 import AZURE_NODE_19_DEFENDER_V2
from .block_5_node20_v2 import AZURE_NODE_20_GOVERNANCE_V2

# V2 nodes list
ALL_AZURE_V2_NODES = [
    AZURE_NODE_1_INTRO_V2,
    AZURE_NODE_2_V2,
    AZURE_NODE_3_V2,
    AZURE_NODE_4_V2,
    AZURE_NODE_5_V2,
    AZURE_NODE_6_V2,
    AZURE_NODE_7_V2,
    AZURE_NODE_8_V2,
    AZURE_NODE_9_V2,
    AZURE_NODE_10_SQL_V2,
    AZURE_NODE_11_COSMOS_V2,
    AZURE_NODE_12_REDIS_V2,
    AZURE_NODE_13_DEVOPS_V2,
    AZURE_NODE_14_ACR_V2,
    AZURE_NODE_15_BICEP_V2,
    AZURE_NODE_16_PIPELINES_V2,
    AZURE_NODE_17_ENTRA_V2,
    AZURE_NODE_18_KEYVAULT_V2,
    AZURE_NODE_19_DEFENDER_V2,
    AZURE_NODE_20_GOVERNANCE_V2,
]

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
