"""
Bootcamp v3 Modules - Auto-converted from Skillsmaps
============================================================================

Contains all DevOps learning modules in bootcamp_v3 format.
Each module has tasks with full pedagogical content.

Total: 14 modules, 280+ tasks
"""

# Import all converted modules
from .module_aws import MODULE_AWS_DEVOPS
from .module_bash import MODULE_BASH
from .module_cicd import MODULE_CICD_MASTERY
from .module_docker import MODULE_DOCKER_MASTERY
from .module_git import MODULE_GIT_GITHUB_MASTERY
from .module_go import MODULE_GO
from .module_javascript import MODULE_JAVASCRIPT
from .module_kubernetes import MODULE_KUBERNETES_MASTERY
from .module_linux import MODULE_LINUX_MASTERY
from .module_mlops import MODULE_MLOPS
from .module_nodejs import MODULE_NODEJS
from .module_python import MODULE_PYTHON_DEVOPS
from .module_terraform import MODULE_TERRAFORM_MASTERY
from .module_typescript import MODULE_TYPESCRIPT


# All modules list
ALL_V3_MODULES = [
    MODULE_AWS_DEVOPS,
    MODULE_BASH,
    MODULE_CICD_MASTERY,
    MODULE_DOCKER_MASTERY,
    MODULE_GIT_GITHUB_MASTERY,
    MODULE_GO,
    MODULE_JAVASCRIPT,
    MODULE_KUBERNETES_MASTERY,
    MODULE_LINUX_MASTERY,
    MODULE_MLOPS,
    MODULE_NODEJS,
    MODULE_PYTHON_DEVOPS,
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
