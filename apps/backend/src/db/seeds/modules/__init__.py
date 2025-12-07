"""
DevOps Learning Modules - Clean Architecture
=============================================

EN fil per modul. Ingen V1/V2/V3. Bara senaste versionen.

Struktur:
- modules/linux.py      → Linux Mastery
- modules/docker.py     → Docker Mastery
- modules/kubernetes.py → Kubernetes Mastery
- modules/git_github.py → Git & GitHub Mastery
- modules/bash.py       → Bash Mastery
- modules/terraform.py  → Terraform Mastery
- modules/ansible.py    → Ansible Mastery
- modules/cicd.py       → CI/CD Mastery
- etc.

Alla moduler exporteras via ALL_MODULES listan.
"""

# Refaktorerade moduler (nya rena filer)
from .linux import MODULE as LINUX_MODULE
from .docker import MODULE as DOCKER_MODULE
from .kubernetes import MODULE as KUBERNETES_MODULE
from .git_github import MODULE as GIT_GITHUB_MODULE
from .bash import MODULE as BASH_MODULE
from .terraform import MODULE as TERRAFORM_MODULE
from .ansible import MODULE as ANSIBLE_MODULE
from .cicd import MODULE as CICD_MODULE
from .aws import MODULE as AWS_MODULE

# Legacy-moduler som ännu inte refaktorerats
# Importeras från gamla strukturen tills de flyttas hit
from ..modules_v3 import (
    # MODULE_BASH, - Ersatt av bash.py
    # MODULE_GIT_GITHUB_MASTERY, - Ersatt av git_github.py
    # MODULE_DOCKER_MASTERY, - Ersatt av docker.py
    # MODULE_KUBERNETES_MASTERY, - Ersatt av kubernetes.py
    # MODULE_TERRAFORM_MASTERY, - Ersatt av terraform.py
    # MODULE_ANSIBLE_MASTERY, - Ersatt av ansible.py
    # MODULE_CICD_MASTERY, - Ersatt av cicd.py
    # MODULE_AWS_DEVOPS, - Ersatt av aws.py
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
    KUBERNETES_MODULE,
    GIT_GITHUB_MODULE,
    BASH_MODULE,
    TERRAFORM_MODULE,
    ANSIBLE_MODULE,
    CICD_MODULE,
    AWS_MODULE,
]

LEGACY_MODULES = [
    # MODULE_BASH, - Ersatt av bash.py
    # MODULE_GIT_GITHUB_MASTERY, - Ersatt av git_github.py
    # MODULE_DOCKER_MASTERY, - Ersatt av docker.py
    # MODULE_KUBERNETES_MASTERY, - Ersatt av kubernetes.py
    # MODULE_TERRAFORM_MASTERY, - Ersatt av terraform.py
    # MODULE_ANSIBLE_MASTERY, - Ersatt av ansible.py
    # MODULE_CICD_MASTERY, - Ersatt av cicd.py
    # MODULE_AWS_DEVOPS, - Ersatt av aws.py
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
