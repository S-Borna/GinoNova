"""
Studyflow Module Registry
Samlar alla moduler för Studyflow
"""

from .linux import LINUX_MODULE
from .bash import BASH_MODULE
from .docker import DOCKER_MODULE
from .kubernetes import KUBERNETES_MODULE
from .git import GIT_MODULE

# Registry över alla studyflow-moduler
STUDYFLOW_MODULES = {
    "linux": LINUX_MODULE,
    "bash": BASH_MODULE,
    "docker": DOCKER_MODULE,
    "kubernetes": KUBERNETES_MODULE,
    "git": GIT_MODULE,
}

def get_all_modules():
    """Returnerar lista med alla moduler"""
    return list(STUDYFLOW_MODULES.values())

def get_module(slug: str):
    """Hämtar en specifik modul"""
    return STUDYFLOW_MODULES.get(slug)

def get_module_topics(slug: str):
    """Hämtar topics för en modul"""
    module = get_module(slug)
    if module:
        return module.get("topics", [])
    return []
