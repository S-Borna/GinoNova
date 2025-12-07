"""
DevOps Learning Modules - Clean Architecture
=============================================

EN fil per modul. Ingen V1/V2/V3. Bara senaste versionen.

Struktur:
- modules/linux.py      → Linux Mastery
- modules/docker.py     → Docker Mastery
- modules/kubernetes.py → Kubernetes Mastery
- etc.

Alla moduler exporteras via ALL_MODULES listan.
"""

# Refaktorerade moduler (nya rena filer)
from .linux import MODULE as LINUX_MODULE
from .docker import MODULE as DOCKER_MODULE

# Legacy-moduler som ännu inte refaktorerats
# Importeras från gamla strukturen tills de flyttas hit
from ..modules_v3 import (
    MODULE_BASH,
    MODULE_GIT_GITHUB_MASTERY,
    # MODULE_DOCKER_MASTERY, - Ersatt av docker.py
    MODULE_KUBERNETES_MASTERY,
    MODULE_CICD_MASTERY,
    MODULE_TERRAFORM_MASTERY,
    MODULE_ANSIBLE_MASTERY,
    MODULE_AWS_DEVOPS,
    MODULE_AZURE_MASTERY_V2,
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

# Refaktorerade moduler har prioritet
ALL_MODULES = [
    LINUX_MODULE,
    DOCKER_MODULE,
]

LEGACY_MODULES = [
    MODULE_BASH,
    MODULE_GIT_GITHUB_MASTERY,
    # MODULE_DOCKER_MASTERY, - Ersatt av docker.py
    MODULE_KUBERNETES_MASTERY,
    MODULE_CICD_MASTERY,
    MODULE_TERRAFORM_MASTERY,
    MODULE_ANSIBLE_MASTERY,
    MODULE_AWS_DEVOPS,
    MODULE_AZURE_MASTERY_V2,
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


def get_all_modules():
    """Returnerar alla moduler - refaktorerade + legacy."""
    # Refaktorerade moduler har prioritet
    refactored_slugs = {m["slug"] for m in ALL_MODULES}

    # Lägg till legacy-moduler som inte refaktorerats än
    combined = list(ALL_MODULES)
    for legacy in LEGACY_MODULES:
        if legacy["slug"] not in refactored_slugs:
            combined.append(legacy)

    return combined


def get_module_by_slug(slug: str):
    """Hämta en modul via slug."""
    for m in get_all_modules():
        if m["slug"] == slug:
            return m
    return None


def get_module_count():
    """Antal moduler totalt."""
    return len(get_all_modules())


def get_total_tasks():
    """Totalt antal tasks."""
    return sum(len(m.get("tasks", [])) for m in get_all_modules())
