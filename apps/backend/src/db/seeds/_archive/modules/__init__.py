"""
DevOps Learning Modules - Clean Architecture
=============================================

EN fil per modul. Ingen V1/V2/V3. Bara senaste versionen.

22 moduler totalt:
- 13 i Camp DevOps (DevOps-fokuserade)
- 22 i SkillsMaps (alla moduler)

Camp DevOps är ett subset av SkillsMaps.
"""

# =============================================================================
# REFAKTORERADE MODULER (nya rena filer med 20 tasks var)
# =============================================================================
from .linux import MODULE as LINUX_MODULE
from .docker import MODULE as DOCKER_MODULE
from .kubernetes import MODULE as KUBERNETES_MODULE
from .git_github import MODULE as GIT_GITHUB_MODULE
from .bash import MODULE as BASH_MODULE
from .terraform import MODULE as TERRAFORM_MODULE
from .ansible import MODULE as ANSIBLE_MODULE
from .cicd import MODULE as CICD_MODULE
from .aws import MODULE as AWS_MODULE
from .azure import MODULE as AZURE_MODULE

# =============================================================================
# LEGACY-MODULER (väntar på omskrivning till Linux-mallen)
# =============================================================================
from ..modules_v3 import (
    MODULE_PYTHON_DEVOPS,
    MODULE_SYSTEM_DESIGN,
    MODULE_SQL_MASTERY,
    MODULE_JAVASCRIPT,
    MODULE_TYPESCRIPT,
    MODULE_NODEJS,
    MODULE_GO_MASTERY,
    MODULE_DOTNET_MASTERY,
    MODULE_REACT_NEXTJS,
    MODULE_MLOPS,
    MODULE_PROMPT_ENGINEERING,
    MODULE_AI_AGENTS,
)

# =============================================================================
# ALLA MODULER (22 st) - används av SkillsMaps
# =============================================================================
ALL_MODULES = [
    # Refaktorerade (10 st)
    LINUX_MODULE,
    DOCKER_MODULE,
    KUBERNETES_MODULE,
    GIT_GITHUB_MODULE,
    BASH_MODULE,
    TERRAFORM_MODULE,
    ANSIBLE_MODULE,
    CICD_MODULE,
    AWS_MODULE,
    AZURE_MODULE,
    # Legacy (12 st)
    MODULE_PYTHON_DEVOPS,
    MODULE_SYSTEM_DESIGN,
    MODULE_SQL_MASTERY,
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

# =============================================================================
# CAMP DEVOPS (13 st) - DevOps-fokuserade moduler
# =============================================================================
CAMP_DEVOPS_SLUGS = [
    "linux-mastery",
    "bash-mastery",
    "git-github-mastery",
    "docker-mastery",
    "kubernetes-mastery",
    "cicd-mastery",
    "terraform-mastery",
    "ansible-mastery",
    "aws-mastery",
    "azure-mastery-v2",
    "python-devops",         # Legacy - väntar på omskrivning
    "system-design",         # Legacy - väntar på omskrivning
    "sql-mastery",           # Legacy - väntar på omskrivning
]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_all_modules():
    """Returnerar alla 22 moduler (SkillsMaps)."""
    return ALL_MODULES


def get_camp_devops_modules():
    """Returnerar Camp DevOps moduler (13 st DevOps-fokuserade)."""
    return [m for m in ALL_MODULES if m.get("slug") in CAMP_DEVOPS_SLUGS]


def get_skillsmaps_modules():
    """Returnerar alla moduler (samma som get_all_modules)."""
    return ALL_MODULES


def get_module_by_slug(slug: str):
    """Hämta en modul via slug."""
    for m in ALL_MODULES:
        if m.get("slug") == slug:
            return m
    return None


def get_module_count():
    """Antal moduler totalt."""
    return len(ALL_MODULES)


def get_total_tasks():
    """Totalt antal tasks."""
    return sum(len(m.get("tasks", [])) for m in ALL_MODULES)
