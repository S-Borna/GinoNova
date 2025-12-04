"""
Bootcamp v3 Modules - Auto-converted from Skillsmaps
============================================================================

Contains all DevOps learning modules in bootcamp_v3 format.
Each module has tasks with full pedagogical content.

Total: 18 modules, 360+ tasks (ALL PREMIUM V3)
"""

# Import all converted modules
from .module_aws import MODULE_AWS_DEVOPS
from .module_bash import MODULE_BASH
from .module_cicd import MODULE_CICD_MASTERY
from .docker import MODULE_DOCKER_MASTERY  # Premium upgraded version
from .git import MODULE_GIT_GITHUB_MASTERY  # Premium upgraded version
from .go import MODULE_GO_MASTERY  # Premium upgraded version
from .module_javascript import MODULE_JAVASCRIPT
from .kubernetes import MODULE_KUBERNETES_MASTERY  # Premium upgraded version
from .module_linux import MODULE_LINUX_MASTERY
from .module_mlops import MODULE_MLOPS
from .module_nodejs import MODULE_NODEJS
from .module_python import MODULE_PYTHON_DEVOPS
from .terraform import MODULE_TERRAFORM_MASTERY  # Premium upgraded version
from .module_typescript import MODULE_TYPESCRIPT

# NEW V3 PREMIUM MODULES
from .ansible import MODULE_ANSIBLE_MASTERY
from .sql import MODULE_SQL_MASTERY
from .system_design import MODULE_SYSTEM_DESIGN
from .prompt_engineering import MODULE_PROMPT_ENGINEERING


# All modules list (18 TOTAL)
ALL_V3_MODULES = [
    MODULE_AWS_DEVOPS,
    MODULE_ANSIBLE_MASTERY,  # NEW
    MODULE_BASH,
    MODULE_CICD_MASTERY,
    MODULE_DOCKER_MASTERY,
    MODULE_GIT_GITHUB_MASTERY,
    MODULE_GO_MASTERY,
    MODULE_JAVASCRIPT,
    MODULE_KUBERNETES_MASTERY,
    MODULE_LINUX_MASTERY,
    MODULE_MLOPS,
    MODULE_NODEJS,
    MODULE_PROMPT_ENGINEERING,  # NEW
    MODULE_PYTHON_DEVOPS,
    MODULE_SQL_MASTERY,  # NEW
    MODULE_SYSTEM_DESIGN,  # NEW
    MODULE_TERRAFORM_MASTERY,
    MODULE_TYPESCRIPT,
]


def get_all_modules():
    """Returns all v3 modules."""
    return ALL_V3_MODULES


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
    return [m for m in ALL_V3_MODULES if m['track_slug'] == track_slug]
