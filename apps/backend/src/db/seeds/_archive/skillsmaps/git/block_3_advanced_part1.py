# =============================================================================
# BLOCK 3: ADVANCED GIT PART 1 (Noder 9-10)
# =============================================================================

NODE_09_GITHUB_PLATFORM = {
    "node_id": 9,
    "title": "GitHub Platform Deep Dive",
    "slug": "github-platform-deep-dive",
    "estimated_minutes": 70,
    "xp_reward": 175,
    "prerequisites": ["git-large-files-performance"],
    "content": '''
# GitHub Platform Deep Dive

## Varför detta är kritiskt

> "GitHub är inte bara Git-hosting. Det är ett komplett utvecklingsekosystem med CI/CD, projekt-management, säkerhet och collaboration. Att ignorera GitHub's fulla potential är att kasta bort 80% av dess värde."

**Verkligheten:**
- 100+ miljoner repos
- 90% av open source lever på GitHub
- GitHub Actions har revolutionerat CI/CD
- Copilot förändrar hur kod skrivs

---

## GitHub Architecture

```
+-----------------------------------------------------------------------------+
|                       GITHUB PLATFORM ECOSYSTEM                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|   +---------------------------------------------------------------------+  |
|   |                        CODE HOSTING                                 |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   |  |Repositories | |  Branches   | |    Tags     | |  Releases   |   |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   +---------------------------------------------------------------------+  |
|                                    |                                        |
|   +--------------------------------+------------------------------------+  |
|   |                          COLLABORATION                              |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   |  |Pull Requests| |   Issues    | |Discussions  | |    Wiki     |   |  |
|   |  |  Review     | |  Tracking   | |  Community  | |Documentation|   |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   +---------------------------------------------------------------------+  |
|                                    |                                        |
|   +--------------------------------+------------------------------------+  |
|   |                           AUTOMATION                                |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   |  |   Actions   | |   Webhooks  | |   GitHub    | |   Pages     |   |  |
|   |  |   CI/CD     | |  Integrations| |    API     | |   Hosting   |   |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   +---------------------------------------------------------------------+  |
|                                    |                                        |
|   +--------------------------------+------------------------------------+  |
|   |                            SECURITY                                 |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   |  | Dependabot  | | Code Scan   | |  Secrets    | |   GHAS      |   |  |
|   |  |  Alerts     | |  CodeQL     | |  Scanning   | |  Advanced   |   |  |
|   |  +-------------+ +-------------+ +-------------+ +-------------+   |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
+-----------------------------------------------------------------------------+
```

---

## Pull Request Excellence

### Creating the Perfect PR

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Fixes #123
Related to #456

## How Has This Been Tested?
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Screenshots (if applicable)
<details>
<summary>Before</summary>
<img src="before.png" width="400">
</details>
<details>
<summary>After</summary>
<img src="after.png" width="400">
</details>

## Checklist
- [ ] My code follows the project style guidelines
- [ ] I have performed a self-review
- [ ] I have commented hard-to-understand areas
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests
- [ ] New and existing tests pass locally
```

### PR Best Practices

```bash
# Before creating PR
git fetch origin main
git rebase origin/main

# Clean up commits
git rebase -i origin/main
# Squash WIP commits, write clear messages

# Push with force if rebased
git push --force-with-lease

# Create PR from command line (GitHub CLI)
gh pr create --title "feat: add user authentication" \
  --body "Implements JWT-based auth" \
  --reviewer user1,user2 \
  --label "enhancement"
```

### Code Review Best Practices

```markdown
# As a Reviewer:

## Good Comments:
- ✅ "Consider using `const` here since this value isn't reassigned"
- ✅ "This could cause a race condition if called concurrently. Consider adding a mutex."
- ✅ "Nice refactor! This is much cleaner."

## Poor Comments:
- ❌ "This is wrong" (no explanation)
- ❌ "I would have done it differently" (no alternative)
- ❌ "Why?" (too vague)

## Comment Types:
- 🔴 **Blocking**: Must be fixed before merge
- 🟡 **Non-blocking**: Suggestion, can be addressed later
- 🟢 **Praise**: Good work recognition
- ❓ **Question**: Seeking understanding
```

---

## GitHub Issues & Projects

### Issue Templates

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: File a bug report
title: "[Bug]: "
labels: ["bug", "triage"]
assignees:
  - octocat
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: input
    id: version
    attributes:
      label: Version
      description: What version are you running?
      placeholder: ex. 1.0.0
    validations:
      required: true
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
    validations:
      required: true
  - type: textarea
    id: reproduce
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this issue?
      value: |
        1. Go to '...'
        2. Click on '....'
        3. Scroll down to '....'
        4. See error
    validations:
      required: true
  - type: dropdown
    id: browsers
    attributes:
      label: What browsers are you seeing the problem on?
      multiple: true
      options:
        - Firefox
        - Chrome
        - Safari
        - Microsoft Edge
  - type: textarea
    id: logs
    attributes:
      label: Relevant log output
      render: shell
```

### GitHub Projects (Beta)

```
+-----------------------------------------------------------------------------+
|                         PROJECT VIEWS                                       |
+-----------------------------------------------------------------------------+
|                                                                             |
|   TABLE VIEW:                                                               |
|   +---------------------------------------------------------------------+  |
|   | Title      | Status    | Priority | Assignee | Sprint   | Points   |  |
|   |------------+-----------+----------+----------+----------+----------|  |
|   | Add login  | In Review | High     | @alice   | Sprint 1 | 5        |  |
|   | Fix bug    | In Dev    | Critical | @bob     | Sprint 1 | 3        |  |
|   | Update docs| Backlog   | Low      | -        | -        | 2        |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
|   BOARD VIEW:                                                               |
|   +--------------+--------------+--------------+--------------+            |
|   |   Backlog    |   In Dev     |  In Review   |    Done      |            |
|   |--------------|--------------|--------------|--------------|            |
|   | +----------+ | +----------+ | +----------+ | +----------+ |            |
|   | |Update    | | |Fix bug   | | |Add login | | |Setup CI  | |            |
|   | |docs      | | |#234      | | |#123      | | |#100      | |            |
|   | +----------+ | +----------+ | +----------+ | +----------+ |            |
|   |              |              |              |              |            |
|   +--------------+--------------+--------------+--------------+            |
|                                                                             |
|   ROADMAP VIEW:                                                             |
|   +---------------------------------------------------------------------+  |
|   | Q1 2024          | Q2 2024          | Q3 2024          |            |  |
|   |------------------|------------------|------------------|            |  |
|   | ##### v1.0       | ########## v2.0  | #### v2.1        |            |  |
|   | Auth, Core API   | Dashboard, API v2| Mobile support   |            |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
+-----------------------------------------------------------------------------+
```

---

## GitHub CLI (gh)

```bash
# Install
brew install gh

# Authenticate
gh auth login

# Repository operations
gh repo create my-app --public --clone
gh repo clone owner/repo
gh repo fork owner/repo --clone
gh repo view owner/repo --web

# Pull request operations
gh pr create --title "Feature" --body "Description"
gh pr list --state open
gh pr view 123
gh pr checkout 123
gh pr merge 123 --squash
gh pr review 123 --approve
gh pr diff 123

# Issue operations
gh issue create --title "Bug" --body "Description"
gh issue list --label bug
gh issue view 123
gh issue close 123

# Workflow operations
gh run list
gh run view 123
gh run rerun 123
gh workflow run deploy.yml

# Release operations
gh release create v1.0.0 --title "Release 1.0.0" --notes "Release notes"
gh release download v1.0.0

# Search
gh search repos "language:python stars:>1000"
gh search issues "is:open is:issue label:bug"
gh search prs "author:octocat is:merged"
```

---

## Repository Settings & Security

### Branch Protection Rules

```yaml
# Via API or Settings UI
branch_protection:
  main:
    required_status_checks:
      strict: true  # Require branch to be up to date
      contexts:
        - "ci/tests"
        - "ci/lint"
        - "ci/build"
    required_pull_request_reviews:
      dismiss_stale_reviews: true
      require_code_owner_reviews: true
      required_approving_review_count: 2
      require_last_push_approval: true
    restrictions:
      users: []
      teams: ["maintainers"]
    enforce_admins: true
    required_linear_history: false
    allow_force_pushes: false
    allow_deletions: false
    required_conversation_resolution: true
    require_signed_commits: true
```

### CODEOWNERS

```
# .github/CODEOWNERS

# Default owners for everything
* @org/core-team

# Frontend team owns frontend code
/src/frontend/ @org/frontend-team
*.tsx @org/frontend-team
*.css @org/frontend-team

# Backend team owns backend code
/src/backend/ @org/backend-team
*.py @org/backend-team

# DevOps owns infrastructure
/infrastructure/ @org/devops-team
Dockerfile @org/devops-team
*.yml @org/devops-team

# Security team reviews sensitive files
/src/auth/ @org/security-team
**/security/** @org/security-team

# Documentation
/docs/ @org/docs-team
*.md @org/docs-team
```

### Dependabot Configuration

```yaml
# .github/dependabot.yml
version: 2
updates:
  # Python dependencies
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "python"
    commit-message:
      prefix: "deps"
    reviewers:
      - "backend-team"
    groups:
      development-dependencies:
        patterns:
          - "pytest*"
          - "black"
          - "mypy"
    ignore:
      - dependency-name: "django"
        versions: ["4.x"]  # Stay on 3.x

  # npm dependencies
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
    groups:
      react:
        patterns:
          - "react*"
          - "@types/react*"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
```

---

## GitHub API & Automation

```python
# Using PyGithub
from github import Github

# Authenticate
g = Github("your_access_token")

# Get repository
repo = g.get_repo("owner/repo")

# Create issue
issue = repo.create_issue(
    title="Bug: Login fails",
    body="Steps to reproduce...",
    labels=["bug", "priority:high"],
    assignees=["username"]
)

# Create PR
# First, create branch and push changes
pr = repo.create_pull(
    title="feat: Add feature X",
    body="Description of changes",
    head="feature-branch",
    base="main"
)

# Add reviewers
pr.create_review_request(reviewers=["reviewer1", "reviewer2"])

# Merge PR
pr.merge(
    commit_title="feat: Add feature X (#123)",
    merge_method="squash"
)

# List workflows
for workflow in repo.get_workflows():
    print(f"{workflow.name}: {workflow.state}")

# Trigger workflow
workflow = repo.get_workflow("deploy.yml")
workflow.create_dispatch(ref="main", inputs={"environment": "production"})
```

---

## Sammanfattning

| Feature | Use Case | Key Commands |
|---------|----------|--------------|
| Pull Requests | Code review | `gh pr create` |
| Issues | Task tracking | `gh issue create` |
| Projects | Sprint planning | UI-based |
| CODEOWNERS | Review routing | `.github/CODEOWNERS` |
| Dependabot | Dependency updates | `.github/dependabot.yml` |
| GitHub CLI | Automation | `gh` commands |

---

## Nästa Steg

GitHub platform mastered. Nästa: **GitHub Actions Mastery** — CI/CD pipelines och automation.
''',
}

NODE_10_GITHUB_ACTIONS = {
    "node_id": 10,
    "title": "GitHub Actions Mastery",
    "slug": "github-actions-mastery",
    "estimated_minutes": 80,
    "xp_reward": 200,
    "prerequisites": ["github-platform-deep-dive"],
    "content": '''
# GitHub Actions Mastery

## Varför detta är kritiskt

> "GitHub Actions har demokratiserat CI/CD. Från enkel linting till komplex multi-cloud deployment — allt i din repo. Att inte utnyttja Actions är att utveckla med händerna bakbundna."

**Verkligheten:**
- 98% av GitHub repos kan använda Actions gratis
- Ersätter Jenkins, CircleCI, Travis för de flesta team
- Marketplace har 10,000+ färdiga actions
- Integration med hela GitHub-ekosystemet

---

## GitHub Actions Architecture

```
+-----------------------------------------------------------------------------+
|                      GITHUB ACTIONS ARCHITECTURE                            |
+-----------------------------------------------------------------------------+
|                                                                             |
|   WORKFLOW FILE (.github/workflows/*.yml)                                   |
|   +---------------------------------------------------------------------+  |
|   |                                                                     |  |
|   |  on: [push, pull_request]        <- TRIGGER                          |  |
|   |                                                                     |  |
|   |  jobs:                                                              |  |
|   |    build:                        <- JOB                              |  |
|   |      runs-on: ubuntu-latest      <- RUNNER                           |  |
|   |      steps:                                                         |  |
|   |        - uses: actions/checkout  <- ACTION                           |  |
|   |        - run: npm test           <- COMMAND                          |  |
|   |                                                                     |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
|   EXECUTION FLOW:                                                           |
|   +---------+    +---------+    +---------+    +---------+               |
|   | Trigger | -► |  Queue  | -► | Runner  | -► | Execute |               |
|   | Event   |    | Jobs    |    | Starts  |    | Steps   |               |
|   +---------+    +---------+    +---------+    +---------+               |
|                                                                             |
|   RUNNERS:                                                                  |
|   +-- GitHub-hosted (ubuntu, windows, macos)                               |
|   +-- Self-hosted (your own servers)                                       |
|                                                                             |
+-----------------------------------------------------------------------------+
```

---

## Basic Workflow Structure

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

# Triggers
on:
  push:
    branches: [main, develop]
    paths:
      - 'src/**'
      - 'tests/**'
      - '.github/workflows/**'
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:  # Manual trigger
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

# Environment variables (workflow-level)
env:
  NODE_VERSION: '20'
  PYTHON_VERSION: '3.11'

# Jobs
jobs:
  lint:
    name: Lint Code
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - run: npm ci
      - run: npm run lint

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: lint  # Run after lint
    strategy:
      matrix:
        node-version: [18, 20, 21]
        os: [ubuntu-latest, macos-latest]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - run: npm ci
      - run: npm test

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  build:
    name: Build
    runs-on: ubuntu-latest
    needs: test
    outputs:
      version: ${{ steps.version.outputs.version }}
    steps:
      - uses: actions/checkout@v4

      - name: Get version
        id: version
        run: echo "version=$(node -p 'require(\"./package.json\").version')" >> $GITHUB_OUTPUT

      - run: npm ci
      - run: npm run build

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ github.sha }}
          path: dist/
          retention-days: 7

  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://myapp.com
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: build-${{ github.sha }}

      - name: Deploy to production
        run: |
          echo "Deploying version ${{ needs.build.outputs.version }}"
          # Deploy commands here
```

---

## Advanced Workflow Patterns

### Reusable Workflows

```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy Workflow

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      version:
        required: true
        type: string
    secrets:
      AWS_ACCESS_KEY_ID:
        required: true
      AWS_SECRET_ACCESS_KEY:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Deploy
        run: |
          echo "Deploying ${{ inputs.version }} to ${{ inputs.environment }}"
```

```yaml
# .github/workflows/main.yml
name: Main Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}
    steps:
      - uses: actions/checkout@v4
      - id: version
        run: echo "version=1.0.${{ github.run_number }}" >> $GITHUB_OUTPUT

  deploy-staging:
    needs: build
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
      version: ${{ needs.build.outputs.version }}
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

  deploy-production:
    needs: deploy-staging
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: production
      version: ${{ needs.build.outputs.version }}
    secrets:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

### Composite Actions

```yaml
# .github/actions/setup-project/action.yml
name: 'Setup Project'
description: 'Setup Node.js and install dependencies'
inputs:
  node-version:
    description: 'Node.js version'
    required: false
    default: '20'
  working-directory:
    description: 'Working directory'
    required: false
    default: '.'

runs:
  using: 'composite'
  steps:
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
        cache: 'npm'
        cache-dependency-path: ${{ inputs.working-directory }}/package-lock.json

    - name: Install dependencies
      shell: bash
      working-directory: ${{ inputs.working-directory }}
      run: npm ci

    - name: Cache build
      uses: actions/cache@v4
      with:
        path: ${{ inputs.working-directory }}/.next/cache
        key: nextjs-${{ hashFiles('**/package-lock.json') }}
```

```yaml
# Using the composite action
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/setup-project
        with:
          node-version: '20'
      - run: npm run build
```

---

## Matrix Strategies

```yaml
jobs:
  test:
    strategy:
      fail-fast: false  # Continue other jobs if one fails
      max-parallel: 4   # Limit concurrent jobs
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20]
        include:
          # Additional combinations
          - os: ubuntu-latest
            node: 21
            experimental: true
        exclude:
          # Skip specific combinations
          - os: windows-latest
            node: 18

    runs-on: ${{ matrix.os }}
    continue-on-error: ${{ matrix.experimental == true }}

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

---

## Caching Strategies

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # npm cache (built into setup-node)
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      # Custom cache
      - name: Cache custom directory
        uses: actions/cache@v4
        with:
          path: |
            ~/.custom-cache
            .build-cache
          key: custom-${{ runner.os }}-${{ hashFiles('**/config.json') }}
          restore-keys: |
            custom-${{ runner.os }}-
            custom-

      # Docker layer caching
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Cache Docker layers
        uses: actions/cache@v4
        with:
          path: /tmp/.buildx-cache
          key: docker-${{ runner.os }}-${{ github.sha }}
          restore-keys: |
            docker-${{ runner.os }}-

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          cache-from: type=local,src=/tmp/.buildx-cache
          cache-to: type=local,dest=/tmp/.buildx-cache-new,mode=max

      # Rotate cache to prevent unbounded growth
      - name: Move cache
        run: |
          rm -rf /tmp/.buildx-cache
          mv /tmp/.buildx-cache-new /tmp/.buildx-cache
```

---

## Secrets and Environments

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com

    steps:
      - name: Access secrets
        env:
          # Repository secrets
          API_KEY: ${{ secrets.API_KEY }}
          # Environment secrets (override repo secrets)
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
        run: |
          echo "Deploying with secrets..."
          # Secrets are masked in logs

      - name: Access variables
        env:
          # Repository variables
          LOG_LEVEL: ${{ vars.LOG_LEVEL }}
          # Environment variables
          API_URL: ${{ vars.API_URL }}
        run: |
          echo "API_URL: $API_URL"

      # Using GITHUB_TOKEN (automatic)
      - name: Create release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## Docker Workflows

```yaml
name: Docker Build & Push

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## Self-Hosted Runners

```yaml
# Using self-hosted runner
jobs:
  build:
    runs-on: [self-hosted, linux, x64]
    steps:
      - uses: actions/checkout@v4
      - run: ./build.sh

# Runner labels for routing
jobs:
  gpu-job:
    runs-on: [self-hosted, gpu]
    steps:
      - run: python train_model.py

  deploy:
    runs-on: [self-hosted, production, aws]
    steps:
      - run: ./deploy.sh
```

### Runner Setup Script

```bash
#!/bin/bash
# Setup self-hosted runner on Ubuntu

# Create runner user
sudo useradd -m github-runner
sudo usermod -aG docker github-runner

# Download runner
cd /home/github-runner
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf actions-runner-linux-x64.tar.gz

# Configure
./config.sh --url https://github.com/org/repo --token TOKEN

# Install as service
sudo ./svc.sh install
sudo ./svc.sh start
```

---

## Sammanfattning

| Concept | Description | Use Case |
|---------|-------------|----------|
| Workflow | YAML file defining automation | CI/CD pipeline |
| Job | Set of steps running on same runner | Build, Test, Deploy |
| Step | Individual task | Run command, use action |
| Action | Reusable automation unit | Setup tools, deploy |
| Matrix | Test multiple configurations | Cross-platform testing |
| Secrets | Encrypted variables | API keys, credentials |
| Environment | Deployment target | staging, production |

---

## Nästa Steg

GitHub Actions mastered. Nästa: **Security & Compliance** — kod-scanning, secrets management, och compliance.
''',
}

BLOCK_3_PART_1_NODES = [NODE_09_GITHUB_PLATFORM, NODE_10_GITHUB_ACTIONS]
