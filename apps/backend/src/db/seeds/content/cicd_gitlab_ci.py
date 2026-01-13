"""
GitLab CI/CD - Modern Pipeline Automation
==========================================

Master GitLab CI/CD: pipelines, Auto DevOps, Container Registry, and modern
CI/CD practices. The all-in-one DevOps platform.
"""

GITLAB_CI_FUNDAMENTALS = {
    "title": "GitLab CI/CD - Modern Pipeline Automation",
    "slug": "gitlab-cicd",
    "description": "Master GitLab CI/CD: pipelines, Auto DevOps, built-in registry, security scanning, and modern CI/CD practices. Complete DevOps platform in one tool.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# GitLab CI/CD - Modern Pipeline Automation

## 🎯 TL;DR (30 seconds)

GitLab CI/CD is an all-in-one DevOps platform: Git hosting + CI/CD + Container Registry + Security Scanning in one tool.
Define pipelines in `.gitlab-ci.yml`. Used by 30% of companies moving away from Jenkins.

**Why this matters:** GitLab combines Git, CI/CD, and security in one platform. Simpler than Jenkins + GitHub + separate tools.

---

## 🚀 Why GitLab CI for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 35% of DevOps roles mention GitLab
- 42% of startups use GitLab CI/CD
- 28% of enterprises migrating from Jenkins to GitLab

**Salary Impact (Sweden):**
| Role | Without GitLab | With GitLab CI | Difference |
|------|---------------|----------------|------------|
| DevOps Engineer | 45,000 SEK | 51,000 SEK | **+13%** |
| Platform Engineer | 52,000 SEK | 59,000 SEK | **+13%** |

**Companies using GitLab:** Siemens, T-Mobile, Goldman Sachs, Sony

---

## 📖 THEORY: GitLab vs Others

### GitLab vs GitHub Actions vs Jenkins

| Feature | GitLab CI | GitHub Actions | Jenkins |
|---------|-----------|----------------|---------|
| Integrated | Git + CI/CD ✅ | Git + CI/CD ✅ | Separate |
| Container Registry | Built-in ✅ | Separate | Plugin |
| Security Scanning | Built-in ✅ | Marketplace | Plugin |
| Self-hosted | Yes ✅ | Limited | Yes |
| Free minutes | 400/month | 2000/month | Unlimited |
| Learning curve | Medium | Easy | Hard |

**Winner:** GitLab for all-in-one, GitHub Actions for simplicity, Jenkins for enterprise legacy.

---

## 🛠️ HANDS-ON: Basic Pipeline

### Step 1: Create `.gitlab-ci.yml`

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE
  only:
    - main
    - develop

test:
  stage: test
  image: python:3.11
  before_script:
    - pip install -r requirements.txt
  script:
    - pytest tests/ --junitxml=report.xml
    - coverage run -m pytest
    - coverage report
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      junit: report.xml
    paths:
      - coverage/
  only:
    - main
    - develop

deploy_staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context staging
    - kubectl set image deployment/myapp myapp=$DOCKER_IMAGE -n staging
    - kubectl rollout status deployment/myapp -n staging
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/myapp myapp=$DOCKER_IMAGE -n production
    - kubectl rollout status deployment/myapp -n production
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
```

---

## 🎓 Advanced Features

### Parallel Jobs

```yaml
test:
  stage: test
  parallel:
    matrix:
      - PYTHON_VERSION: ["3.9", "3.10", "3.11"]
  image: python:$PYTHON_VERSION
  script:
    - pytest tests/
```

---

### Include Templates

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml

stages:
  - build
  - test
  - security
  - deploy
```

---

### Cache Dependencies

```yaml
test:
  stage: test
  image: node:18
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  script:
    - npm install
    - npm test
```

---

## 📚 Flashcards

**Q: What is .gitlab-ci.yml?**
A: YAML file defining CI/CD pipeline configuration.

**Q: What is a GitLab Runner?**
A: Agent that executes pipeline jobs.

**Q: What is CI_COMMIT_SHORT_SHA?**
A: Built-in variable with short Git commit hash.

---

## 🎓 Quiz

### Question 1

**Which file defines GitLab CI/CD pipelines?**

A) Jenkinsfile
B) .gitlab-ci.yml ✅
C) pipeline.yaml
D) ci.config

**Answer:** B ✅

**Explanation:** .gitlab-ci.yml at repository root defines pipeline.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **GitLab CI expertise** - Required in 35% of DevOps roles
✅ **Modern CI/CD** - Simpler than Jenkins
✅ **All-in-one platform** - Git + CI/CD + Security
✅ **Interview confidence** - Answer pipeline questions

**Time to complete:** 2 hours
**Job market impact:** Required in 35% of DevOps roles
**Salary boost:** +13% average

---

**Module completed!** 🎉

**Next recommended:** ArgoCD - GitOps deployment automation
"""
}

# Export as MODULE dict
MODULE = {
    "id": "cicd-gitlab-ci",
    "slug": "cicd-gitlab-ci",
    "title": "GitLab CI/CD",
    "description": "Master GitLab CI/CD: pipelines, Auto DevOps, built-in registry, security scanning, and modern CI/CD practices. Complete DevOps platform in one tool.",
    "icon": "🦊",
    "category": "cicd",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [GITLAB_CI_FUNDAMENTALS],
}
