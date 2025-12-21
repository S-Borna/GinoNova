"""
Study Data - Flashcards & Quiz för Studyroom
=============================================

Endast färdiga moduler med:
- 90 flashcards per modul (30 per svårighetsgrad: easy, medium, hard)
- 60 quiz-frågor per modul (20 per svårighetsgrad: easy, medium, hard)

Moduler inkluderade (9 st färdiga):
1. Linux Mastery
2. Docker Mastery
3. Kubernetes Mastery
4. Git & GitHub Mastery
5. Bash Mastery
6. Terraform Mastery
7. Ansible Mastery
8. CI/CD Mastery
9. AWS Mastery
"""

from .linux_study import LINUX_STUDY_DATA
from .docker_study import DOCKER_STUDY_DATA
from .kubernetes_study import KUBERNETES_STUDY_DATA
from .git_study import GIT_STUDY_DATA
from .bash_study import BASH_STUDY_DATA
from .terraform_study import TERRAFORM_STUDY_DATA
from .ansible_study import ANSIBLE_STUDY_DATA
from .cicd_study import CICD_STUDY_DATA
from .aws_study import AWS_STUDY_DATA

# Registry av alla studydata - använder module_slug från varje modul
STUDY_DATA_REGISTRY = {
    LINUX_STUDY_DATA["module_slug"]: LINUX_STUDY_DATA,
    DOCKER_STUDY_DATA["module_slug"]: DOCKER_STUDY_DATA,
    KUBERNETES_STUDY_DATA["module_slug"]: KUBERNETES_STUDY_DATA,
    GIT_STUDY_DATA["module_slug"]: GIT_STUDY_DATA,
    BASH_STUDY_DATA["module_slug"]: BASH_STUDY_DATA,
    TERRAFORM_STUDY_DATA["module_slug"]: TERRAFORM_STUDY_DATA,
    ANSIBLE_STUDY_DATA["module_slug"]: ANSIBLE_STUDY_DATA,
    CICD_STUDY_DATA["module_slug"]: CICD_STUDY_DATA,
    AWS_STUDY_DATA["module_slug"]: AWS_STUDY_DATA,
}

def get_study_data(module_slug: str):
    """Hämta studydata för en modul"""
    return STUDY_DATA_REGISTRY.get(module_slug)

def get_all_study_modules():
    """Returnerar alla moduler med studydata"""
    return list(STUDY_DATA_REGISTRY.keys())
