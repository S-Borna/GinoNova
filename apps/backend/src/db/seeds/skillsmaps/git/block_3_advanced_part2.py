# =============================================================================
# BLOCK 3: ADVANCED GIT PART 2 (Noder 11-12)
# =============================================================================

NODE_11_SECURITY_COMPLIANCE = {
    "node_id": 11,
    "title": "Git Security & Compliance",
    "slug": "git-security-compliance",
    "estimated_minutes": 65,
    "xp_reward": 165,
    "prerequisites": ["github-actions-mastery"],
    "content": '''
# Git Security & Compliance

## Varför detta är kritiskt

> "En enda läckt API-nyckel kan kosta miljoner. En osäker pipeline kan öppna hela infrastrukturen för attack. Git-säkerhet är inte valfritt — det är överlevnad."

**Verkligheten:**
- 40%+ av dataläckor involverar credentials i kod
- Secret scanning hittar tusentals exponerade nycklar dagligen
- Compliance-krav (SOC2, PCI, HIPAA) kräver audit trails
- Supply chain attacks ökar exponentiellt

---

## Security Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      GIT SECURITY LAYERS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   LAYER 1: AUTHENTICATION & ACCESS                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ SSH Keys    │ │ PAT Tokens  │ │    SSO     │ │    2FA      │   │  │
│   │  │ Ed25519     │ │ Fine-grained│ │   SAML     │ │   TOTP      │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   LAYER 2: CODE SECURITY                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ Secret Scan │ │  CodeQL     │ │ Dependabot  │ │ SAST/DAST   │   │  │
│   │  │ Pre-commit  │ │  Analysis   │ │  Alerts     │ │  Scanning   │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   LAYER 3: COMMIT INTEGRITY                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ GPG Signing │ │  Verified   │ │  Branch     │ │  Required   │   │  │
│   │  │   Commits   │ │  Commits    │ │ Protection  │ │  Reviews    │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   LAYER 4: AUDIT & COMPLIANCE                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ Audit Logs  │ │ Compliance  │ │  Security   │ │  Access     │   │  │
│   │  │  History    │ │  Reports    │ │  Alerts     │ │  Reviews    │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## GPG Commit Signing

### Setup GPG Key

```bash
# Install GPG
# macOS
brew install gnupg

# Generate key
gpg --full-generate-key
# Choose: RSA and RSA, 4096 bits, no expiration
# Enter name and email (must match Git config)

# List keys
gpg --list-secret-keys --keyid-format=long

# Output:
# sec   rsa4096/3AA5C34371567BD2 2023-01-01 [SC]
#       1234567890ABCDEF1234567890ABCDEF12345678
# uid                 [ultimate] Your Name <your.email@example.com>
# ssb   rsa4096/42B317FD4BA89E7A 2023-01-01 [E]

# Export public key
gpg --armor --export 3AA5C34371567BD2

# Add to GitHub: Settings → SSH and GPG keys → New GPG key
```

### Configure Git

```bash
# Tell Git to use GPG key
git config --global user.signingkey 3AA5C34371567BD2

# Sign all commits by default
git config --global commit.gpgsign true

# Sign all tags by default
git config --global tag.gpgsign true

# Set GPG program (macOS)
git config --global gpg.program gpg

# For macOS, add to ~/.zshrc:
export GPG_TTY=$(tty)
```

### Signing Commits

```bash
# Sign a commit (if not default)
git commit -S -m "Signed commit"

# Verify commit signature
git log --show-signature
git verify-commit HEAD

# Sign a tag
git tag -s v1.0.0 -m "Signed release"

# Verify tag
git verify-tag v1.0.0
```

---

## Secret Scanning & Prevention

### Pre-commit Secret Detection

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: package-lock.json

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

### Gitleaks Configuration

```toml
# .gitleaks.toml
title = "Gitleaks Configuration"

[allowlist]
description = "Allowlisted files and patterns"
paths = [
    "go\\.sum$",
    "package-lock\\.json$",
    ".secrets.baseline$",
]

[[rules]]
id = "aws-access-key"
description = "AWS Access Key"
regex = "AKIA[0-9A-Z]{16}"
tags = ["key", "AWS"]

[[rules]]
id = "aws-secret-key"
description = "AWS Secret Key"
regex = "(?i)aws(.{0,20})?(?-i)['\"][0-9a-zA-Z\\/+]{40}['\"]"
tags = ["key", "AWS"]

[[rules]]
id = "github-pat"
description = "GitHub Personal Access Token"
regex = "ghp_[0-9a-zA-Z]{36}"
tags = ["key", "GitHub"]

[[rules]]
id = "generic-api-key"
description = "Generic API Key"
regex = "(?i)(api[_-]?key|apikey|api_secret)[\\s]*[=:]\\s*['\"][0-9a-zA-Z]{32,}['\"]"
tags = ["key", "API"]
```

### GitHub Secret Scanning

```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 * * *'

jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  codeql:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: javascript, python

      - name: Autobuild
        uses: github/codeql-action/autobuild@v2

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2

  dependency-review:
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v3
        with:
          fail-on-severity: high
          deny-licenses: GPL-3.0, AGPL-3.0
```

---

## Access Control & Permissions

### SSH Key Security

```bash
# Generate secure SSH key (Ed25519)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Or RSA 4096 for compatibility
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# SSH config for multiple accounts
# ~/.ssh/config
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes

# Clone using specific identity
git clone git@github.com-work:company/repo.git
```

### Fine-grained Personal Access Tokens

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FINE-GRAINED PAT CONFIGURATION                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Token Name: ci-deployment-token                                           │
│   Expiration: 90 days                                                       │
│                                                                             │
│   REPOSITORY ACCESS:                                                        │
│   ├── ○ All repositories                                                   │
│   └── ● Selected repositories                                              │
│       └── myorg/myrepo                                                      │
│                                                                             │
│   PERMISSIONS:                                                              │
│   ├── Repository:                                                           │
│   │   ├── Contents: Read and write                                          │
│   │   ├── Metadata: Read-only (mandatory)                                   │
│   │   ├── Pull requests: Read and write                                     │
│   │   └── Workflows: Read and write                                         │
│   │                                                                         │
│   └── Account:                                                              │
│       └── (none selected)                                                   │
│                                                                             │
│   BEST PRACTICES:                                                           │
│   • Minimal permissions needed                                              │
│   • Short expiration (30-90 days)                                           │
│   • Rotate regularly                                                        │
│   • Use specific repos, not all                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Removing Secrets from History

```bash
# STOP! First, revoke the exposed credential

# Option 1: BFG Repo Cleaner (fastest)
java -jar bfg.jar --replace-text passwords.txt repo.git
# passwords.txt format:
# literal:my_actual_password==>REMOVED
# regex:sk_live_[a-zA-Z0-9]{24}==>STRIPE_KEY_REMOVED

# Clean up
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Option 2: git-filter-repo (recommended)
pip install git-filter-repo

# Create replacement file
cat > replacements.txt << EOF
literal:AKIAIOSFODNN7EXAMPLE==>AWS_KEY_REMOVED
regex:sk_live_[a-zA-Z0-9]{24}==>STRIPE_KEY_REMOVED
EOF

git filter-repo --replace-text replacements.txt

# Force push (coordinate with team!)
git push --force --all
git push --force --tags

# All collaborators must:
git fetch origin
git reset --hard origin/main
# Or re-clone the repository
```

---

## Audit & Compliance

### GitHub Audit Log

```bash
# Enterprise audit log API
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.github.com/enterprises/ENTERPRISE/audit-log?phrase=action:repo.create"

# Organization audit log
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.github.com/orgs/ORG/audit-log?phrase=actor:username"

# Filter by action
# repo.create, repo.destroy, member.add, team.add_member
# org.oauth_app_access_approved, protected_branch.create
```

### Compliance Configuration

```yaml
# .github/settings.yml (GitHub Settings App)
repository:
  name: myrepo
  description: Production repository
  private: true
  has_issues: true
  has_wiki: false
  default_branch: main
  allow_squash_merge: true
  allow_merge_commit: false
  allow_rebase_merge: false
  delete_branch_on_merge: true

branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 2
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
      required_status_checks:
        strict: true
        contexts:
          - "ci/tests"
          - "security/scan"
      enforce_admins: true
      required_linear_history: true
      restrictions:
        users: []
        teams:
          - maintainers
```

---

## Supply Chain Security

### Dependency Management

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    groups:
      production-dependencies:
        dependency-type: "production"
      development-dependencies:
        dependency-type: "development"
    labels:
      - "dependencies"
    commit-message:
      prefix: "deps"
    reviewers:
      - "security-team"
    # Security updates only
    allow:
      - dependency-type: "direct"
    ignore:
      - dependency-name: "*"
        update-types: ["version-update:semver-patch"]
```

### SBOM Generation

```yaml
# .github/workflows/sbom.yml
name: Generate SBOM

on:
  release:
    types: [published]

jobs:
  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.spdx.json

      - name: Attach to Release
        uses: softprops/action-gh-release@v1
        with:
          files: sbom.spdx.json
```

---

## Sammanfattning

| Security Layer | Tools | Purpose |
|----------------|-------|---------|
| Authentication | SSH, PAT, SSO | Access control |
| Commit Integrity | GPG signing | Verification |
| Secret Detection | Gitleaks, detect-secrets | Prevent leaks |
| Code Scanning | CodeQL, SAST | Vulnerability detection |
| Dependencies | Dependabot, SBOM | Supply chain |
| Audit | Audit logs | Compliance |

---

## Nästa Steg

Security & Compliance mastered. Nästa: **Monorepo & Scale** — hantering av stora kodbasar och team.
''',
}

NODE_12_MONOREPO_SCALE = {
    "node_id": 12,
    "title": "Monorepo & Scale",
    "slug": "monorepo-scale",
    "estimated_minutes": 70,
    "xp_reward": 175,
    "prerequisites": ["git-security-compliance"],
    "content": '''
# Monorepo & Scale

## Varför detta är kritiskt

> "När din kodbas växer förbi några hundra tusen rader, blir vanliga Git-workflows till flaskhalsar. Monorepo-strategier och skalningsoptimering är skillnaden mellan produktivitet och kaos."

**Verkligheten:**
- Google har 86TB i ett monorepo
- Meta hanterar 100+ miljoner commits
- Många företag migrerar till monorepos
- Tooling är kritiskt för att lyckas

---

## Monorepo Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MONOREPO vs POLYREPO                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   POLYREPO (Multiple Repositories):                                         │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                       │
│   │ frontend-app │ │ backend-api  │ │shared-utils  │                       │
│   │    .git      │ │    .git      │ │    .git      │                       │
│   │   package/   │ │   package/   │ │   package/   │                       │
│   └──────────────┘ └──────────────┘ └──────────────┘                       │
│   + Independent versioning         - Dependency management complex          │
│   + Clear ownership                - Cross-repo changes hard                │
│   - Duplicated config              - Inconsistent tooling                   │
│                                                                             │
│   MONOREPO (Single Repository):                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         company-platform                            │  │
│   │                              .git                                   │  │
│   │  ┌──────────────┬──────────────┬──────────────┬──────────────┐     │  │
│   │  │    apps/     │  packages/   │   tools/     │    docs/     │     │  │
│   │  ├──────────────┼──────────────┼──────────────┼──────────────┤     │  │
│   │  │ frontend/    │ ui/          │ cli/         │ api-docs/    │     │  │
│   │  │ backend/     │ utils/       │ scripts/     │ guides/      │     │  │
│   │  │ mobile/      │ config/      │ generators/  │              │     │  │
│   │  └──────────────┴──────────────┴──────────────┴──────────────┘     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│   + Atomic cross-package changes   - Larger clone size                      │
│   + Shared tooling                 - Complex CI/CD                          │
│   + Consistent dependencies        - Permission management                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Monorepo Tooling

### Turborepo Setup

```bash
# Initialize Turborepo
npx create-turbo@latest

# Directory structure
company-platform/
├── apps/
│   ├── web/           # Next.js app
│   ├── mobile/        # React Native
│   └── api/           # Node.js backend
├── packages/
│   ├── ui/            # Shared React components
│   ├── config/        # Shared configs (ESLint, TS)
│   └── utils/         # Shared utilities
├── package.json       # Root package.json
├── turbo.json         # Turborepo config
└── pnpm-workspace.yaml
```

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**"]
    },
    "lint": {},
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "deploy": {
      "dependsOn": ["build", "test", "lint"]
    }
  }
}
```

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

### Nx Setup

```bash
# Create Nx workspace
npx create-nx-workspace@latest company-platform --preset=ts

# Add plugins
nx add @nx/react
nx add @nx/node
nx add @nx/jest

# Generate new app
nx generate @nx/react:app frontend

# Generate new library
nx generate @nx/js:library utils
```

```json
// nx.json
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "cache": true
    },
    "test": {
      "cache": true
    }
  },
  "affected": {
    "defaultBase": "main"
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/**/?(*.)+(spec|test).[jt]s?(x)?(.snap)",
      "!{projectRoot}/tsconfig.spec.json"
    ],
    "sharedGlobals": ["{workspaceRoot}/babel.config.json"]
  }
}
```

---

## Affected-Based CI/CD

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      affected: ${{ steps.affected.outputs.affected }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for comparison

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'

      - run: pnpm install

      - name: Get affected projects
        id: affected
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            BASE="origin/${{ github.base_ref }}"
          else
            BASE="HEAD~1"
          fi
          AFFECTED=$(pnpm turbo run build --dry-run=json --filter="...[${BASE}]" | jq -c '.tasks | map(.taskId)')
          echo "affected=$AFFECTED" >> $GITHUB_OUTPUT

  build:
    needs: detect-changes
    if: needs.detect-changes.outputs.affected != '[]'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        project: ${{ fromJson(needs.detect-changes.outputs.affected) }}
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'

      - run: pnpm install

      - name: Build ${{ matrix.project }}
        run: pnpm turbo run build --filter=${{ matrix.project }}

      - name: Test ${{ matrix.project }}
        run: pnpm turbo run test --filter=${{ matrix.project }}
```

---

## Remote Caching

### Turborepo Remote Cache

```bash
# Login to Vercel (Turborepo remote cache)
npx turbo login

# Link to remote cache
npx turbo link

# Environment variables for CI
export TURBO_TOKEN=${{ secrets.TURBO_TOKEN }}
export TURBO_TEAM=my-team

# Cache hit example
pnpm turbo run build
# cache hit, replaying output...
# Tasks:    1 successful, 1 total
# Cached:   1 cached, 1 total
# Time:     2.1s
```

### Self-hosted Cache

```typescript
// turbo-remote-cache server (example)
import { createServer } from '@turbo-remote-cache/server';

const server = createServer({
  storage: {
    driver: 's3',
    options: {
      bucket: 'turbo-cache',
      region: 'us-east-1',
    },
  },
  auth: {
    type: 'bearer',
    validate: async (token) => {
      return token === process.env.TURBO_TOKEN;
    },
  },
});

server.listen(3000);
```

---

## Code Ownership at Scale

### CODEOWNERS for Monorepo

```
# .github/CODEOWNERS

# Default owners
* @company/engineering

# App-specific ownership
/apps/web/ @company/frontend-team
/apps/api/ @company/backend-team
/apps/mobile/ @company/mobile-team

# Package ownership
/packages/ui/ @company/design-system-team
/packages/config/ @company/platform-team
/packages/utils/ @company/platform-team

# Infrastructure
/.github/ @company/devops-team
/infrastructure/ @company/devops-team
turbo.json @company/platform-team
nx.json @company/platform-team

# Documentation
/docs/ @company/docs-team
*.md @company/docs-team
```

### Team-based Access

```yaml
# GitHub organization teams structure
teams:
  engineering:
    members: [all-engineers]
    repos:
      company-platform: write

  frontend-team:
    members: [alice, bob]
    repos:
      company-platform: write
    paths:
      - apps/web/**
      - packages/ui/**

  backend-team:
    members: [charlie, dave]
    repos:
      company-platform: write
    paths:
      - apps/api/**
      - packages/utils/**

  platform-team:
    members: [eve, frank]
    repos:
      company-platform: admin
```

---

## Git Performance at Scale

### Sparse Checkout Strategy

```bash
# Clone with sparse checkout
git clone --filter=blob:none --sparse https://github.com/company/platform
cd platform

# Configure sparse checkout
git sparse-checkout init --cone

# Check out specific packages
git sparse-checkout set apps/web packages/ui packages/config

# Add more later
git sparse-checkout add apps/api

# List current sparse config
git sparse-checkout list
```

### Git Configuration for Large Repos

```ini
# .gitconfig for monorepo
[core]
    fsmonitor = true
    untrackedCache = true
    preloadIndex = true
    commitGraph = true

[gc]
    auto = 256
    writeCommitGraph = true

[fetch]
    parallel = 8
    writeCommitGraph = true

[pack]
    threads = 0
    windowMemory = 512m
    deltaCacheSize = 512m

[index]
    version = 4
    threads = true

[feature]
    manyFiles = true

[maintenance]
    auto = true
    strategy = incremental
```

### Scheduled Maintenance

```yaml
# .github/workflows/maintenance.yml
name: Repository Maintenance

on:
  schedule:
    - cron: '0 2 * * 0'  # Weekly Sunday 2 AM

jobs:
  maintenance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run git maintenance
        run: |
          git maintenance run --task=gc
          git maintenance run --task=commit-graph
          git maintenance run --task=prefetch
          git maintenance run --task=loose-objects
          git maintenance run --task=incremental-repack
```

---

## Handling Large Binary Files

```yaml
# .gitattributes for monorepo
# Track large files with LFS
*.psd filter=lfs diff=lfs merge=lfs -text
*.ai filter=lfs diff=lfs merge=lfs -text
*.sketch filter=lfs diff=lfs merge=lfs -text

# App-specific assets
apps/web/public/videos/** filter=lfs diff=lfs merge=lfs -text
apps/mobile/assets/images/** filter=lfs diff=lfs merge=lfs -text

# Generated files (don't track changes)
**/dist/** binary
**/build/** binary
**/.next/** binary

# Lock files (merge strategy)
**/pnpm-lock.yaml merge=ours
**/package-lock.json merge=ours
```

---

## Migration to Monorepo

```bash
#!/bin/bash
# migrate-to-monorepo.sh

MONOREPO="company-platform"
REPOS=("frontend" "backend" "shared-utils")

# Create monorepo
mkdir $MONOREPO
cd $MONOREPO
git init

# Migrate each repo preserving history
for REPO in "${REPOS[@]}"; do
    # Add remote
    git remote add $REPO https://github.com/company/$REPO.git
    git fetch $REPO --tags

    # Rewrite paths
    git read-tree --prefix=apps/$REPO/ -u $REPO/main

    # Or use git-filter-repo for full history
    # git filter-repo --to-subdirectory-filter apps/$REPO
done

# Create unified commits
git add .
git commit -m "chore: migrate to monorepo structure"

# Setup tooling
npx create-turbo@latest --skip-transform
npm init -w apps/frontend -y
npm init -w apps/backend -y
npm init -w packages/utils -y
```

---

## Sammanfattning

| Challenge | Solution | Tool |
|-----------|----------|------|
| Build coordination | Task pipelines | Turborepo, Nx |
| Code ownership | CODEOWNERS | GitHub |
| CI efficiency | Affected detection | turbo/nx --affected |
| Build caching | Remote cache | Vercel, S3 |
| Clone speed | Sparse checkout | git sparse-checkout |
| Large files | LFS | git-lfs |

---

## Nästa Steg

Monorepo & Scale mastered. Nästa: **Enterprise Git Operations** — GitOps, disaster recovery, och enterprise workflows.
''',
}

BLOCK_3_PART_2_NODES = [NODE_11_SECURITY_COMPLIANCE, NODE_12_MONOREPO_SCALE]
