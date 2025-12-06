"""
Azure Cloud Mastery SkillsMap - Module Wrapper
Provides access to all Azure blocks and metadata.
"""

from ..skillsmaps.azure import SKILLSMAP_METADATA
from ..skillsmaps.azure.block_1_fundamentals import BLOCK_1_NODES
from ..skillsmaps.azure.block_2_compute import BLOCK_2_NODES
from ..skillsmaps.azure.block_3_storage import BLOCK_3_NODES
from ..skillsmaps.azure.block_4_devops import BLOCK_4_NODES
from ..skillsmaps.azure.block_5_security import BLOCK_5_NODES

# Combine all nodes
ALL_NODES = BLOCK_1_NODES + BLOCK_2_NODES + BLOCK_3_NODES + BLOCK_4_NODES + BLOCK_5_NODES

# Module exports
__all__ = [
    "SKILLSMAP_METADATA",
    "BLOCK_1_NODES",
    "BLOCK_2_NODES",
    "BLOCK_3_NODES",
    "BLOCK_4_NODES",
    "BLOCK_5_NODES",
    "ALL_NODES",
]
