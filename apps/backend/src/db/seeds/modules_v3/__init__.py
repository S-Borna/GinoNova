"""
DevOps Learning Modules
============================================================================

CAMP DEVOPS: Core DevOps curriculum (YH-level)
SKILLSMAPS: Additional programming & specialized skills

Total: 13 Camp DevOps + 11 SkillsMaps = 24 modules
"""

# =============================================================================
# CAMP DEVOPS - Core DevOps Curriculum (13 modules)
# =============================================================================

# Core Infrastructure
from .module_linux import MODULE_LINUX_MASTERY
from .module_bash import MODULE_BASH

# Version Control
from .git import MODULE_GIT_GITHUB_MASTERY

# Containers & Orchestration
from .docker import MODULE_DOCKER_MASTERY
from .kubernetes import MODULE_KUBERNETES_MASTERY

# CI/CD & IaC
from .module_cicd import MODULE_CICD_MASTERY
from .terraform import MODULE_TERRAFORM_MASTERY
from .ansible import MODULE_ANSIBLE_MASTERY

# Cloud Platforms
from .module_aws import MODULE_AWS_DEVOPS
from .azure import SKILLSMAP_METADATA as MODULE_AZURE_INFO, ALL_NODES as AZURE_NODES
MODULE_AZURE_MASTERY = {
    **MODULE_AZURE_INFO,
    "tasks": AZURE_NODES,
}

# Scripting & Automation
from .module_python import MODULE_PYTHON_DEVOPS

# Architecture & Data
from .system_design import MODULE_SYSTEM_DESIGN
from .sql import MODULE_SQL_MASTERY

# V2 MODULES (with content_blocks for ILE)
from .module_linux_v2 import MODULE_LINUX_MASTERY_V2
from .module_azure_v2 import MODULE_AZURE_MASTERY_V2


# =============================================================================
# SKILLSMAPS - Additional Programming & Specialized Skills (11 modules)
# =============================================================================

# Programming Languages
from .module_javascript import MODULE_JAVASCRIPT
from .module_typescript import MODULE_TYPESCRIPT
from .module_nodejs import MODULE_NODEJS
from .go import MODULE_GO_MASTERY
from .dotnet import MODULE_INFO as MODULE_DOTNET_MASTERY

# Frontend
from .react_nextjs import MODULE_REACT_NEXTJS

# Specialized/Emerging
from .module_mlops import MODULE_MLOPS
from .prompt_engineering import MODULE_PROMPT_ENGINEERING
from .ai_agents import MODULE_AI_AGENTS


# =============================================================================
# MODULE LISTS
# =============================================================================

# Camp DevOps - Core YH DevOps curriculum
CAMP_DEVOPS_MODULES = [
    MODULE_LINUX_MASTERY_V2,  # V2 replaces V1
    MODULE_BASH,
    MODULE_GIT_GITHUB_MASTERY,
    MODULE_DOCKER_MASTERY,
    MODULE_KUBERNETES_MASTERY,
    MODULE_CICD_MASTERY,
    MODULE_TERRAFORM_MASTERY,
    MODULE_ANSIBLE_MASTERY,
    MODULE_AWS_DEVOPS,
    MODULE_AZURE_MASTERY_V2,  # V2 replaces V1
    MODULE_PYTHON_DEVOPS,
    MODULE_SYSTEM_DESIGN,
    MODULE_SQL_MASTERY,
]

# SkillsMaps - Additional programming & specialized skills
SKILLSMAPS_MODULES = [
    MODULE_JAVASCRIPT,
    MODULE_TYPESCRIPT,
    MODULE_NODEJS,
    MODULE_GO_MASTERY,
    MODULE_DOTNET_MASTERY,
    MODULE_REACT_NEXTJS,
    MODULE_MLOPS,
    MODULE_PROMPT_ENGINEERING,
    MODULE_AI_AGENTS,
]

# All modules combined (for backwards compatibility)
ALL_V3_MODULES = CAMP_DEVOPS_MODULES + SKILLSMAPS_MODULES


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_all_modules():
    """Returns all modules."""
    return ALL_V3_MODULES


def get_camp_devops_modules():
    """Returns Camp DevOps modules (core YH curriculum)."""
    return CAMP_DEVOPS_MODULES


def get_skillsmaps_modules():
    """Returns SkillsMaps modules (additional skills)."""
    return SKILLSMAPS_MODULES


def get_module_count():
    """Returns the number of modules."""
    return len(ALL_V3_MODULES)


def get_total_tasks():
    """Returns total task count across all modules."""
    return sum(len(m['tasks']) for m in ALL_V3_MODULES)


def get_module_by_slug(slug: str):
    """Returns a module by its slug."""
    for m in ALL_V3_MODULES:
        if m['slug'] == slug:
            return m
    return None


def get_modules_by_track(track_slug: str):
    """Returns all modules for a specific track."""
    return [m for m in ALL_V3_MODULES if m.get('track_slug') == track_slug]
