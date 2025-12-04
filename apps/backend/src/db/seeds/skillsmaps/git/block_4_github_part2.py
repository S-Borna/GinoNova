# =============================================================================
# BLOCK 4: GITHUB COLLABORATION PART 2 (Noder 15-16)
# =============================================================================

NODE_15_ISSUES_PROJECTS = {
    "node_id": 15,
    "title": "Issues & Projects",
    "slug": "issues-projects",
    "estimated_minutes": 50,
    "xp_reward": 135,
    "prerequisites": ["pull-requests-mastery"],
    "content": r'''
# Issues & Projects

## Varför detta är kritiskt

> "Issues är mer än bug tracking. De är kommunikationsnavet för ditt projekt — feature requests, discussions, documentation tasks. GitHub Projects tar det vidare med visualisering och workflow automation."

---

## Issues Deep Dive

### Issue Anatomy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ISSUE STRUCTURE                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   #123 - Login button not working on mobile                             │
│   ───────────────────────────────────────────                           │
│                                                                         │
│   Status: Open                Labels: bug, mobile, high-priority        │
│   Assignees: @developer       Milestone: v2.1                           │
│   Project: Sprint 12          Linked PR: #125                           │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ DESCRIPTION                                                     │   │
│   │                                                                 │   │
│   │ ## Bug Description                                              │   │
│   │ The login button doesn't respond to taps on iOS Safari.        │   │
│   │                                                                 │   │
│   │ ## Steps to Reproduce                                           │   │
│   │ 1. Open site on iPhone                                          │   │
│   │ 2. Go to /login                                                 │   │
│   │ 3. Tap "Sign In" button                                         │   │
│   │ 4. Nothing happens                                              │   │
│   │                                                                 │   │
│   │ ## Expected Behavior                                            │   │
│   │ Login form should submit                                        │   │
│   │                                                                 │   │
│   │ ## Environment                                                  │   │
│   │ - Device: iPhone 14                                             │   │
│   │ - OS: iOS 17.1                                                  │   │
│   │ - Browser: Safari                                               │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   TIMELINE:                                                             │
│   @user opened this issue 2 hours ago                                   │
│   @developer was assigned 1 hour ago                                    │
│   @developer linked PR #125                                             │
│   @tester commented: "Confirmed on my device"                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Creating Issues

### Via CLI

```bash
# Simple issue
gh issue create --title "Bug: Login fails on mobile" \
  --body "The login button doesn't work on iOS Safari"

# With labels and assignee
gh issue create \
  --title "Feature: Dark mode support" \
  --body "Add dark mode theme option" \
  --label "enhancement,ui" \
  --assignee "@me" \
  --milestone "v2.0"

# From template
gh issue create --template bug_report.md

# Interactive mode
gh issue create
```

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
    id: contact
    attributes:
      label: Contact Details
      description: How can we reach you?
      placeholder: ex. email@example.com
    validations:
      required: false

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
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

  - type: checkboxes
    id: terms
    attributes:
      label: Code of Conduct
      options:
        - label: I agree to follow this project's Code of Conduct
          required: true
```

---

## Managing Issues

### Searching & Filtering

```bash
# List open issues
gh issue list

# Filter by label
gh issue list --label "bug"

# Filter by assignee
gh issue list --assignee "@me"

# Filter by milestone
gh issue list --milestone "v2.0"

# Search
gh issue list --search "login"

# Complex search (on GitHub.com)
# is:issue is:open label:bug assignee:username
# is:issue is:closed author:username
```

### Issue Operations

```bash
# View issue
gh issue view 123

# View in browser
gh issue view 123 --web

# Close issue
gh issue close 123

# Reopen issue
gh issue reopen 123

# Add comment
gh issue comment 123 --body "Working on this now"

# Edit issue
gh issue edit 123 --add-label "in-progress"
gh issue edit 123 --add-assignee "@me"

# Pin issue
gh issue pin 123

# Transfer issue to another repo
gh issue transfer 123 owner/other-repo
```

---

## Labels

### Standard Labels

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      LABEL SYSTEM                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   TYPE:                                                                 │
│   ├── bug           🔴 red      - Something isn't working               │
│   ├── enhancement   🔵 blue     - New feature request                   │
│   ├── documentation 🟢 green    - Documentation changes                 │
│   └── question      🟣 purple   - Further information requested         │
│                                                                         │
│   PRIORITY:                                                             │
│   ├── critical      🔴 red      - Must fix immediately                  │
│   ├── high          🟠 orange   - Important, fix soon                   │
│   ├── medium        🟡 yellow   - Normal priority                       │
│   └── low           🟢 green    - Nice to have                          │
│                                                                         │
│   STATUS:                                                               │
│   ├── triage        ⚪ gray     - Needs assessment                      │
│   ├── in-progress   🔵 blue     - Being worked on                       │
│   ├── blocked       🔴 red      - Cannot proceed                        │
│   └── needs-review  🟣 purple   - Needs code review                     │
│                                                                         │
│   COMPONENT:                                                            │
│   ├── frontend      🔵 teal     - UI/UX related                         │
│   ├── backend       🔵 navy     - Server/API related                    │
│   ├── database      🟤 brown    - Database related                      │
│   └── infra         ⚪ gray     - Infrastructure                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Creating Labels via CLI

```bash
# Create label
gh label create "critical" --color "B60205" --description "Must fix immediately"

# List labels
gh label list

# Edit label
gh label edit "bug" --color "FF0000"

# Delete label
gh label delete "wontfix"
```

---

## GitHub Projects

### Project Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GITHUB PROJECT BOARD                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─ Sprint 12 ─────────────────────────────────────────────────────┐   │
│   │                                                                 │   │
│   │  📋 Backlog    🏃 In Progress    👀 Review    ✅ Done           │   │
│   │  ──────────    ─────────────    ────────    ──────             │   │
│   │                                                                 │   │
│   │  ┌─────────┐   ┌─────────┐      ┌─────────┐ ┌─────────┐        │   │
│   │  │ #134    │   │ #128    │      │ #125    │ │ #120    │        │   │
│   │  │ Feature │   │ Bug fix │      │ PR #126 │ │ Done!   │        │   │
│   │  │ ────────│   │ ────────│      │ ────────│ │ ────────│        │   │
│   │  │ @dev1   │   │ @dev2   │      │ @dev1   │ │ @dev2   │        │   │
│   │  └─────────┘   └─────────┘      └─────────┘ └─────────┘        │   │
│   │                                                                 │   │
│   │  ┌─────────┐                                 ┌─────────┐        │   │
│   │  │ #135    │                                 │ #119    │        │   │
│   │  │ Docs    │                                 │ Shipped │        │   │
│   │  └─────────┘                                 └─────────┘        │   │
│   │                                                                 │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   VIEWS:                                                                │
│   • Board (Kanban)                                                      │
│   • Table (Spreadsheet)                                                 │
│   • Roadmap (Timeline)                                                  │
│                                                                         │
│   CUSTOM FIELDS:                                                        │
│   • Status (Single select)                                              │
│   • Priority (Single select)                                            │
│   • Sprint (Iteration)                                                  │
│   • Estimate (Number)                                                   │
│   • Due date (Date)                                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Project Automation

### Built-in Automation

```yaml
# When issue is opened:
- Add to project
- Set status to "Triage"

# When PR is opened:
- Add to project
- Set status to "In Progress"

# When PR is merged:
- Set status to "Done"
- Archive item

# When issue is closed:
- Set status to "Done"
```

### Workflow Automation

```yaml
# .github/workflows/project-automation.yml
name: Project Automation
on:
  issues:
    types: [opened, closed]
  pull_request:
    types: [opened, closed]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.5.0
        with:
          project-url: https://github.com/users/username/projects/1
          github-token: ${{ secrets.PROJECT_TOKEN }}
```

---

## Milestones

### Creating Milestones

```bash
# Via GitHub UI:
# Repository → Issues → Milestones → New milestone

# Milestone structure:
# - Title: v2.0.0
# - Due date: 2024-03-01
# - Description: Major release with new auth system
```

### Using Milestones

```bash
# Assign issue to milestone
gh issue edit 123 --milestone "v2.0.0"

# View milestone progress
# Shows % complete based on closed issues

# Filter by milestone
gh issue list --milestone "v2.0.0"
```

---

## Linking Issues and PRs

### Reference Syntax

```markdown
# In commit messages or PR descriptions:

Fixes #123           # Closes issue when PR merges
Closes #123          # Same as Fixes
Resolves #123        # Same as Fixes

Related to #123      # Links but doesn't close
See #123             # Links but doesn't close
Part of #123         # Links but doesn't close

# Cross-repository references
Fixes owner/repo#123

# Multiple issues
Fixes #123, fixes #124, fixes #125
```

### Tracking Relationships

```
Issue #100 (Epic)
├── Issue #101 (Task) - Linked via description
├── Issue #102 (Task) - Linked via description
└── PR #103 - "Closes #101"
    └── Commits referencing #100
```

---

## Sammanfattning

| Concept | Command | Purpose |
|---------|---------|---------|
| Create issue | `gh issue create` | Report bugs/features |
| Labels | `gh label create` | Categorize issues |
| Milestones | GitHub UI | Track releases |
| Projects | GitHub UI | Kanban/roadmap |
| Link | `Closes #123` | Connect PR to issue |

---

## Nästa Steg

Issues och Projects behärskade. Nästa: **GitHub Actions** — CI/CD automation.
''',
}

NODE_16_GITHUB_ACTIONS = {
    "node_id": 16,
    "title": "GitHub Actions Mastery",
    "slug": "github-actions-mastery",
    "estimated_minutes": 65,
    "xp_reward": 165,
    "prerequisites": ["issues-projects"],
    "content": r'''
# GitHub Actions Mastery

## Varför detta är kritiskt

> "GitHub Actions har revolutionerat CI/CD. Det är integrerat, kraftfullt, och har ett enormt marketplace. Ingen extern CI-tjänst behövs — allt finns i GitHub."

---

## Actions Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GITHUB ACTIONS ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   WORKFLOW (.github/workflows/ci.yml)                                   │
│   ──────────────────────────────────                                    │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ name: CI                                                        │   │
│   │                                                                 │   │
│   │ on: [push, pull_request]    ← TRIGGER                           │   │
│   │                                                                 │   │
│   │ jobs:                                                           │   │
│   │   ┌─────────────────────────────────────────────────────────┐   │   │
│   │   │ JOB: test                                               │   │   │
│   │   │ runs-on: ubuntu-latest  ← RUNNER                        │   │   │
│   │   │                                                         │   │   │
│   │   │ steps:                                                  │   │   │
│   │   │   ┌───────────────────────────────────────────────┐     │   │   │
│   │   │   │ STEP 1: actions/checkout@v4                   │     │   │   │
│   │   │   │ STEP 2: actions/setup-node@v4                 │     │   │   │
│   │   │   │ STEP 3: npm install                           │     │   │   │
│   │   │   │ STEP 4: npm test                              │     │   │   │
│   │   │   └───────────────────────────────────────────────┘     │   │   │
│   │   └─────────────────────────────────────────────────────────┘   │   │
│   │                                                                 │   │
│   │   ┌─────────────────────────────────────────────────────────┐   │   │
│   │   │ JOB: build                                              │   │   │
│   │   │ needs: test             ← DEPENDENCY                    │   │   │
│   │   │ ...                                                     │   │   │
│   │   └─────────────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   COMPONENTS:                                                           │
│   Workflow → Jobs → Steps → Actions                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Basic Workflow

### Minimal CI Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Run linter
        run: npm run lint
```

---

## Workflow Triggers

### Event Types

```yaml
on:
  # Push to branches
  push:
    branches:
      - main
      - 'release/**'
    paths:
      - 'src/**'
      - 'package.json'
    tags:
      - 'v*'

  # Pull requests
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]

  # Schedule (cron)
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

  # Manual trigger
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

  # Other workflows
  workflow_run:
    workflows: ["Build"]
    types: [completed]

  # Releases
  release:
    types: [published]
```

---

## Jobs and Steps

### Job Configuration

```yaml
jobs:
  build:
    name: Build Application
    runs-on: ubuntu-latest
    timeout-minutes: 15

    # Job-level environment variables
    env:
      NODE_ENV: production

    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: npm run build
        env:
          API_URL: ${{ secrets.API_URL }}

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: build  # Runs after build

    steps:
      - uses: actions/checkout@v4
      - run: npm test

  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    needs: [build, test]  # Runs after both
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4
      - run: ./deploy.sh
```

### Matrix Builds

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20, 22]
        exclude:
          - os: windows-latest
            node: 18
        include:
          - os: ubuntu-latest
            node: 20
            coverage: true

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}

      - run: npm test

      - if: matrix.coverage
        run: npm run coverage
```

---

## Common Actions

### Checkout and Setup

```yaml
# Checkout code
- uses: actions/checkout@v4
  with:
    fetch-depth: 0  # Full history for tags
    submodules: true

# Setup languages
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

- uses: actions/setup-python@v5
  with:
    python-version: '3.12'
    cache: 'pip'

- uses: actions/setup-go@v5
  with:
    go-version: '1.21'
```

### Caching

```yaml
# Cache dependencies
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

### Artifacts

```yaml
# Upload artifact
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7

# Download artifact
- uses: actions/download-artifact@v4
  with:
    name: build-output
    path: dist/
```

---

## Secrets and Variables

### Using Secrets

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        env:
          API_KEY: ${{ secrets.API_KEY }}
          AWS_ACCESS_KEY: ${{ secrets.AWS_ACCESS_KEY }}
        run: |
          echo "Deploying with API key"
          ./deploy.sh
```

### Environment Variables

```yaml
# Repository level
env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      NODE_ENV: production
    steps:
      - name: Build
        env:
          BUILD_ID: ${{ github.run_id }}
        run: npm run build
```

---

## Conditional Execution

### If Conditions

```yaml
jobs:
  deploy:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        if: github.event.inputs.environment == 'staging'
        run: ./deploy-staging.sh

      - name: Deploy to production
        if: github.event.inputs.environment == 'production'
        run: ./deploy-production.sh

      - name: Always run cleanup
        if: always()
        run: ./cleanup.sh

      - name: Run on failure
        if: failure()
        run: ./notify-failure.sh
```

---

## Reusable Workflows

### Create Reusable Workflow

```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      deploy_key:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        env:
          DEPLOY_KEY: ${{ secrets.deploy_key }}
        run: ./deploy.sh ${{ inputs.environment }}
```

### Use Reusable Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
    secrets:
      deploy_key: ${{ secrets.STAGING_DEPLOY_KEY }}

  deploy-production:
    needs: deploy-staging
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: production
    secrets:
      deploy_key: ${{ secrets.PROD_DEPLOY_KEY }}
```

---

## Complete CI/CD Example

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage/

  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: dist
          path: dist/
      - name: Deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
        run: ./scripts/deploy.sh
```

---

## Monitoring Workflows

### CLI Commands

```bash
# List workflow runs
gh run list

# View specific run
gh run view 12345

# Watch running workflow
gh run watch

# View logs
gh run view 12345 --log

# Re-run failed jobs
gh run rerun 12345 --failed
```

---

## Sammanfattning

| Component | Purpose | Example |
|-----------|---------|---------|
| Workflow | CI/CD definition | `.github/workflows/ci.yml` |
| Trigger | When to run | `on: [push, pull_request]` |
| Job | Unit of work | `jobs: test:` |
| Step | Single action | `- run: npm test` |
| Action | Reusable component | `actions/checkout@v4` |
| Secret | Sensitive data | `${{ secrets.API_KEY }}` |

---

## Nästa Steg

GitHub Actions behärskad. Nästa: **Enterprise Git Operations** — GitOps och enterprise workflows.
''',
}

BLOCK_4_PART_2_NODES = [NODE_15_ISSUES_PROJECTS, NODE_16_GITHUB_ACTIONS]
