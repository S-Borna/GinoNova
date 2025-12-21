# =============================================================================
# BLOCK 5: ENTERPRISE GIT PART 2 (Noder 19-20)
# =============================================================================

NODE_19_ENTERPRISE_WORKFLOWS = {
    "node_id": 19,
    "title": "Enterprise Git Workflows",
    "slug": "enterprise-workflows",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": ["disaster-recovery-migrations"],
    "content": r'''
# Enterprise Git Workflows

## Varför detta är kritiskt

> "I enterprise-miljöer handlar Git inte bara om kod. Det handlar om compliance, audit trails, governance, och att koordinera hundratals utvecklare över tidszoner."

---

## Enterprise Branch Strategy

```
+-------------------------------------------------------------------------+
|                    ENTERPRISE BRANCH MODEL                              |
+-------------------------------------------------------------------------+
|                                                                         |
|   PERMANENT BRANCHES:                                                   |
|   ------------------                                                    |
|                                                                         |
|   production ----●----●----●----●----●----●----● (protected)           |
|                  |         |         |         |                        |
|   staging   -----●---------●---------●---------● (protected)           |
|                  |         |         |         |                        |
|   develop   -----●----●----●----●----●----●----● (protected)           |
|                       |              |                                  |
|   TEMPORARY BRANCHES:                                                   |
|   ------------------                                                    |
|                                                                         |
|   feature/JIRA-123-user-auth --●--●--●-+                               |
|                                        | PR                             |
|   bugfix/JIRA-456-login-fix --●--●-----+-+                             |
|                                        | | PR                           |
|   hotfix/JIRA-789-security ------------+-+--●--● (-> production)        |
|                                        | |                              |
|   release/v2.0 ------------------------●-●--●--- (-> production)        |
|                                                                         |
|   NAMING CONVENTION:                                                    |
|   +-- feature/TICKET-ID-short-description                               |
|   +-- bugfix/TICKET-ID-short-description                                |
|   +-- hotfix/TICKET-ID-short-description                                |
|   +-- release/vMAJOR.MINOR                                              |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Branch Protection Rules

### GitHub Enterprise Settings

```yaml
# Branch protection for main/production
branches:
  - name: main
    protection:
      # Require PRs
      required_pull_request_reviews:
        required_approving_review_count: 2
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
        require_last_push_approval: true

      # Require status checks
      required_status_checks:
        strict: true
        contexts:
          - "ci/build"
          - "ci/test"
          - "ci/lint"
          - "security/scan"
          - "compliance/check"

      # Enforce admins
      enforce_admins: true

      # Require signed commits
      required_signatures: true

      # Require linear history
      required_linear_history: true

      # Restrict who can push
      restrictions:
        users: []
        teams:
          - release-managers
```

### CODEOWNERS for Enterprise

```
# .github/CODEOWNERS

# Default owners for everything
* @company/engineering-leads

# Architecture decisions
/docs/architecture/ @company/architects
/docs/adr/ @company/architects

# Security-sensitive files
/security/ @company/security-team
*.pem @company/security-team
*.key @company/security-team

# Infrastructure
/terraform/ @company/platform-team
/kubernetes/ @company/platform-team
/.github/workflows/ @company/devops-team

# Compliance
/compliance/ @company/compliance-team
/audit/ @company/compliance-team

# API contracts
/api/openapi.yaml @company/api-team @company/architects
/proto/ @company/api-team

# Database migrations
/migrations/ @company/dba-team @company/backend-leads

# Frontend
/apps/web/ @company/frontend-team
/packages/ui/ @company/design-system-team

# Backend
/apps/api/ @company/backend-team
```

---

## Compliance & Audit

### Audit Logging

```bash
# GitHub Enterprise audit log queries
# Via API
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.github.com/enterprises/ENTERPRISE/audit-log" \
  -d 'phrase=action:repo.create'

# Common audit queries
action:repo.create           # Repository created
action:repo.destroy          # Repository deleted
action:protected_branch.*    # Branch protection changes
action:org.add_member        # New org member
action:team.*                # Team changes
actor:username               # Actions by user
created:>=2024-01-01         # Date filter
```

### Compliance Automation

```yaml
# .github/workflows/compliance.yml
name: Compliance Checks

on:
  pull_request:
    branches: [main, production]

jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check licenses
        uses: licensebat/licensebat-action@v1
        with:
          config-file: .licensebat.toml

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'HIGH,CRITICAL'

  secrets-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Gitleaks
        uses: gitleaks/gitleaks-action@v2

  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          format: spdx-json
          output-file: sbom.spdx.json
```

---

## Release Management

### Semantic Versioning Automation

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Semantic Release
        uses: cycjimmy/semantic-release-action@v4
        with:
          semantic_version: 21
          extra_plugins: |
            @semantic-release/changelog
            @semantic-release/git
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Release Notes Generation

```yaml
# .github/release.yml
changelog:
  exclude:
    labels:
      - skip-changelog
    authors:
      - dependabot

  categories:
    - title: Breaking Changes
      labels:
        - breaking-change

    - title: New Features
      labels:
        - enhancement
        - feature

    - title: Bug Fixes
      labels:
        - bug
        - bugfix

    - title: Documentation
      labels:
        - documentation

    - title: Dependencies
      labels:
        - dependencies
```

---

## Team Coordination

### Inner Source Model

```
+-------------------------------------------------------------------------+
|                    INNER SOURCE MODEL                                   |
+-------------------------------------------------------------------------+
|                                                                         |
|   SHARED REPOSITORIES:                                                  |
|   +-----------------------------------------------------------------+   |
|   |                                                                 |   |
|   |   Platform Team (Owners)                                        |   |
|   |   +-- packages/shared-ui/                                       |   |
|   |   +-- packages/common-utils/                                    |   |
|   |   +-- packages/api-client/                                      |   |
|   |                                                                 |   |
|   |   Contributors (Other Teams):                                   |   |
|   |   +-- Team A -> Fork -> PR -> Review -> Merge                       |   |
|   |   +-- Team B -> Fork -> PR -> Review -> Merge                       |   |
|   |   +-- Team C -> Fork -> PR -> Review -> Merge                       |   |
|   |                                                                 |   |
|   +-----------------------------------------------------------------+   |
|                                                                         |
|   GUIDELINES:                                                           |
|   • CONTRIBUTING.md required                                            |
|   • Response SLA for PRs (48h)                                          |
|   • Office hours for contributors                                       |
|   • Regular sync meetings                                               |
|                                                                         |
+-------------------------------------------------------------------------+
```

### PR Review SLAs

```yaml
# .github/workflows/pr-sla.yml
name: PR SLA Check

on:
  schedule:
    - cron: '0 9 * * 1-5'  # Weekdays 9 AM

jobs:
  check-sla:
    runs-on: ubuntu-latest
    steps:
      - name: Check stale PRs
        uses: actions/github-script@v7
        with:
          script: |
            const { data: prs } = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open'
            });

            const now = new Date();
            const slaHours = 48;

            for (const pr of prs) {
              const created = new Date(pr.created_at);
              const hoursSinceCreation = (now - created) / (1000 * 60 * 60);

              if (hoursSinceCreation > slaHours && pr.requested_reviewers.length > 0) {
                // Send Slack notification
                console.log(`PR #${pr.number} exceeds SLA: ${hoursSinceCreation.toFixed(1)}h`);
              }
            }
```

---

## Multi-Region Setup

```
+-------------------------------------------------------------------------+
|                    MULTI-REGION GIT ARCHITECTURE                        |
+-------------------------------------------------------------------------+
|                                                                         |
|   PRIMARY (US)                    MIRRORS                               |
|   ------------                    -------                               |
|                                                                         |
|   +--------------+               +--------------+                      |
|   |   GitHub     |    sync       |   GitLab     |                      |
|   |   (Primary)  | -----------►  |   EU Mirror  |                      |
|   |              |    real-time  |              |                      |
|   +--------------+               +--------------+                      |
|          |                              |                               |
|          |                              |                               |
|          ▼                              ▼                               |
|   US Developers                  EU Developers                          |
|   (push/pull here)               (read from mirror)                     |
|                                  (push to primary)                      |
|                                                                         |
|   BENEFITS:                                                             |
|   • Faster clones for remote teams                                      |
|   • Disaster recovery                                                   |
|   • Compliance (data residency)                                         |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Sammanfattning

| Area | Practice | Benefit |
|------|----------|---------|
| Branches | Protected + CODEOWNERS | Quality gate |
| Compliance | Automated checks | Audit readiness |
| Releases | Semantic versioning | Predictable |
| Teams | Inner source | Collaboration |
| Global | Mirrors | Performance |

---

## Nästa Steg

Enterprise Workflows behärskad. Nästa: **Git Mastery Certification** — final project och certifiering.
''',
}

NODE_20_GIT_MASTERY = {
    "node_id": 20,
    "title": "Git Mastery Certification",
    "slug": "git-mastery-certification",
    "estimated_minutes": 90,
    "xp_reward": 250,
    "prerequisites": ["enterprise-workflows"],
    "content": r'''
# Git Mastery Certification

## Grattis!

> "Du har nått slutet av Git Mastery-modulen. Denna sista nod sammanfattar allt du lärt dig och presenterar ett capstone-projekt för att demonstrera dina kunskaper."

---

## Kunskapsöversikt

```
+-------------------------------------------------------------------------+
|                       GIT MASTERY PROGRESSION                           |
+-------------------------------------------------------------------------+
|                                                                         |
|   FUNDAMENTALS (Nodes 1-4)                                              |
|   ------------------------                                              |
|   ✓ Git internals (objects, refs, packfiles)                           |
|   ✓ Repository structure                                                |
|   ✓ Staging and committing                                              |
|   ✓ History navigation                                                  |
|                                                                         |
|   BRANCHING (Nodes 5-8)                                                 |
|   --------------------                                                  |
|   ✓ Branch strategies (GitFlow, Trunk-based)                           |
|   ✓ Merging and rebasing                                                |
|   ✓ Conflict resolution                                                 |
|   ✓ Cherry-pick and selective merging                                   |
|                                                                         |
|   ADVANCED (Nodes 9-12)                                                 |
|   ---------------------                                                 |
|   ✓ Interactive rebase                                                  |
|   ✓ Git bisect for debugging                                            |
|   ✓ Worktrees                                                           |
|   ✓ Submodules and subtrees                                             |
|   ✓ Security and compliance                                             |
|   ✓ Monorepo strategies                                                 |
|                                                                         |
|   GITHUB (Nodes 13-16)                                                  |
|   --------------------                                                  |
|   ✓ GitHub platform features                                            |
|   ✓ Pull request workflows                                              |
|   ✓ Issues and Projects                                                 |
|   ✓ GitHub Actions CI/CD                                                |
|                                                                         |
|   ENTERPRISE (Nodes 17-20)                                              |
|   ------------------------                                              |
|   ✓ GitOps principles                                                   |
|   ✓ Disaster recovery                                                   |
|   ✓ Enterprise workflows                                                |
|   ✓ Certification project                                               |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Capstone Project

### Scenario

Du ska sätta upp ett komplett Git-ekosystem för ett företag med följande krav:

```
+-------------------------------------------------------------------------+
|                    CAPSTONE PROJECT REQUIREMENTS                        |
+-------------------------------------------------------------------------+
|                                                                         |
|   COMPANY: TechCorp                                                     |
|   TEAMS: 3 development teams, 15 developers                             |
|   PRODUCTS: Monorepo with 2 applications + shared packages              |
|                                                                         |
|   DELIVERABLES:                                                         |
|                                                                         |
|   1. REPOSITORY SETUP                                                   |
|      □ Monorepo structure with Turborepo/Nx                             |
|      □ Branch protection rules                                          |
|      □ CODEOWNERS file                                                  |
|      □ PR and issue templates                                           |
|                                                                         |
|   2. CI/CD PIPELINE                                                     |
|      □ Build and test workflow                                          |
|      □ Affected-based builds                                            |
|      □ Security scanning (Gitleaks, Trivy)                              |
|      □ Automated releases                                               |
|                                                                         |
|   3. GITOPS SETUP                                                       |
|      □ Kubernetes manifests with Kustomize                              |
|      □ ArgoCD or Flux configuration                                     |
|      □ Multi-environment setup (dev/staging/prod)                       |
|                                                                         |
|   4. DOCUMENTATION                                                      |
|      □ CONTRIBUTING.md                                                  |
|      □ Development workflow guide                                       |
|      □ Disaster recovery runbook                                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Project Implementation

### Step 1: Monorepo Structure

```bash
# Initialize monorepo
npx create-turbo@latest techcorp-platform

# Structure
techcorp-platform/
+-- apps/
|   +-- web/                 # Next.js frontend
|   +-- api/                 # Node.js backend
+-- packages/
|   +-- ui/                  # Shared UI components
|   +-- config/              # Shared configs
|   +-- utils/               # Shared utilities
+-- manifests/               # Kubernetes manifests
|   +-- base/
|   +-- environments/
+-- .github/
|   +-- CODEOWNERS
|   +-- PULL_REQUEST_TEMPLATE.md
|   +-- ISSUE_TEMPLATE/
|   +-- workflows/
+-- turbo.json
+-- package.json
```

### Step 2: Branch Protection

```yaml
# Configure via GitHub API or UI
branches:
  main:
    protection:
      required_approving_review_count: 2
      require_code_owner_reviews: true
      required_status_checks:
        - "CI / Build"
        - "CI / Test"
        - "Security / Scan"
      enforce_admins: true
      required_linear_history: true
```

### Step 3: CODEOWNERS

```
# .github/CODEOWNERS
* @techcorp/engineering-leads

/apps/web/ @techcorp/frontend-team
/apps/api/ @techcorp/backend-team
/packages/ui/ @techcorp/design-system
/manifests/ @techcorp/platform-team
/.github/ @techcorp/devops-team
```

### Step 4: CI/CD Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      web: ${{ steps.filter.outputs.web }}
      api: ${{ steps.filter.outputs.api }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v2
        id: filter
        with:
          filters: |
            web:
              - 'apps/web/**'
              - 'packages/**'
            api:
              - 'apps/api/**'
              - 'packages/**'

  build-web:
    needs: detect-changes
    if: needs.detect-changes.outputs.web == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'
      - run: pnpm install
      - run: pnpm turbo run build --filter=web

  build-api:
    needs: detect-changes
    if: needs.detect-changes.outputs.api == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'
      - run: pnpm install
      - run: pnpm turbo run build --filter=api

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
      - uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'HIGH,CRITICAL'
```

### Step 5: GitOps Manifests

```yaml
# manifests/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: techcorp-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: techcorp-api
  template:
    metadata:
      labels:
        app: techcorp-api
    spec:
      containers:
        - name: api
          image: ghcr.io/techcorp/api:latest
          ports:
            - containerPort: 3000
---
# manifests/environments/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: production
resources:
  - ../../base
patches:
  - path: replicas-patch.yaml
```

### Step 6: ArgoCD Application

```yaml
# argocd/applications/techcorp.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: techcorp-production
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/techcorp/platform.git
    targetRevision: main
    path: manifests/environments/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

## Certification Checklist

```
+-------------------------------------------------------------------------+
|                    CERTIFICATION CHECKLIST                              |
+-------------------------------------------------------------------------+
|                                                                         |
|   FUNDAMENTALS:                                                         |
|   □ Explain Git object model (blob, tree, commit, tag)                  |
|   □ Navigate history with git log, show, diff                           |
|   □ Understand refs, HEAD, and reflog                                   |
|                                                                         |
|   BRANCHING:                                                            |
|   □ Implement GitFlow or Trunk-based development                        |
|   □ Perform merge and rebase operations                                 |
|   □ Resolve complex merge conflicts                                     |
|   □ Use cherry-pick effectively                                         |
|                                                                         |
|   ADVANCED:                                                             |
|   □ Use interactive rebase for history cleanup                          |
|   □ Debug with git bisect                                               |
|   □ Manage multiple worktrees                                           |
|   □ Configure and use submodules/subtrees                               |
|                                                                         |
|   GITHUB:                                                               |
|   □ Set up repository with protection rules                             |
|   □ Create effective PR workflows                                       |
|   □ Build CI/CD with GitHub Actions                                     |
|   □ Manage projects with Issues and Projects                            |
|                                                                         |
|   ENTERPRISE:                                                           |
|   □ Implement GitOps with ArgoCD/Flux                                   |
|   □ Design disaster recovery strategy                                   |
|   □ Set up enterprise branch strategy                                   |
|   □ Configure compliance automation                                     |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Command Reference

```bash
# Fundamentals
git init / git clone
git add / git commit
git log / git show / git diff
git status / git branch

# Branching
git checkout -b / git switch -c
git merge / git rebase
git cherry-pick
git stash

# Advanced
git rebase -i
git bisect start/good/bad
git worktree add
git submodule add

# Remote
git remote add/remove
git fetch / git pull / git push
git push --force-with-lease

# History
git reflog
git reset --hard/soft/mixed
git revert

# GitHub CLI
gh repo create/clone/fork
gh pr create/list/merge
gh issue create/list/close
gh run list/view/watch
```

---

## Nästa Steg

**Grattis till Git Mastery!**

Du har nu kunskaperna att:
- Hantera komplexa Git-historiker
- Designa branching-strategier för stora team
- Implementera GitOps för Kubernetes
- Sätta upp enterprise-grade CI/CD
- Hantera disaster recovery

**Rekommenderade fortsatta studier:**
- Kubernetes Mastery
- CI/CD Pipeline Design
- Platform Engineering
- DevSecOps
''',
}

BLOCK_5_PART_2_NODES = [NODE_19_ENTERPRISE_WORKFLOWS, NODE_20_GIT_MASTERY]
