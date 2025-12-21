"""
Terraform V3 SkillsMap Module
============================

20 Premium Nodes (~10,000+ chars/node) organized into 10 block files.

Block Structure:
- Block 1: Fundamentals (Nodes 1-4) - IaC Core, HCL Mastery
- Block 2: State Management (Nodes 5-8) - Remote State, Locking, Workspaces
- Block 3: Advanced Patterns (Nodes 9-12) - Modules, Testing, CI/CD
- Block 4: CI/CD Integration (Nodes 13-16) - Pipelines, GitOps, Policy
- Block 5: Production (Nodes 17-20) - Scaling, Multi-Cloud, Security
"""

# Block 1: Fundamentals
from .block_1_fundamentals_part1 import BLOCK_1_PART_1_NODES
from .block_1_fundamentals_part2 import BLOCK_1_PART_2_NODES

# Block 2: State Management
from .block_2_state_part1 import BLOCK_2_PART_1_NODES
from .block_2_state_part2 import BLOCK_2_PART_2_NODES

# Block 3: Advanced Patterns
from .block_3_advanced_part1 import BLOCK_3_PART_1_NODES
from .block_3_advanced_part2 import BLOCK_3_PART_2_NODES

# Block 4: CI/CD Integration
from .block_4_cicd_part1 import BLOCK_4_PART_1_NODES
from .block_4_cicd_part2 import BLOCK_4_PART_2_NODES

# Block 5: Production
from .block_5_production_part1 import BLOCK_5_PART_1_NODES
from .block_5_production_part2 import BLOCK_5_PART_2_NODES

# Combine all nodes in order
TERRAFORM_NODES = (
    BLOCK_1_PART_1_NODES +  # Nodes 1-2
    BLOCK_1_PART_2_NODES +  # Nodes 3-4
    BLOCK_2_PART_1_NODES +  # Nodes 5-6
    BLOCK_2_PART_2_NODES +  # Nodes 7-8
    BLOCK_3_PART_1_NODES +  # Nodes 9-10
    BLOCK_3_PART_2_NODES +  # Nodes 11-12
    BLOCK_4_PART_1_NODES +  # Nodes 13-14
    BLOCK_4_PART_2_NODES +  # Nodes 15-16
    BLOCK_5_PART_1_NODES +  # Nodes 17-18
    BLOCK_5_PART_2_NODES    # Nodes 19-20
)

# Export for external use
__all__ = [
    'TERRAFORM_NODES',
    'BLOCK_1_PART_1_NODES',
    'BLOCK_1_PART_2_NODES',
    'BLOCK_2_PART_1_NODES',
    'BLOCK_2_PART_2_NODES',
    'BLOCK_3_PART_1_NODES',
    'BLOCK_3_PART_2_NODES',
    'BLOCK_4_PART_1_NODES',
    'BLOCK_4_PART_2_NODES',
    'BLOCK_5_PART_1_NODES',
    'BLOCK_5_PART_2_NODES',
]
