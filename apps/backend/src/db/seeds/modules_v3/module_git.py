"""
Git & GitHub Mastery - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: foundation
Tasks: 30
Estimated Hours: 15
"""

MODULE_GIT_GITHUB_MASTERY = {
    "track_slug": "foundation",
    "order_index": 100,
    "name": "Git & GitHub Mastery",
    "slug": "git-github-mastery",
    "description": """Behärska versionshantering och samarbete""",
    "difficulty": "beginner",
    "estimated_hours": 15,
    "prerequisites": [],
    "tasks": [
            {
                "title": "Git Introduktion",
                "difficulty": "easy",
                "estimated_minutes": 40,
                "xp_reward": 100,
                "content": r"""
# Git Introduktion

Git är industristandard för versionshantering.

## Installation

```bash
# macOS
brew install git

# Ubuntu
sudo apt install git

# Verifiera
git --version
```

## Konfiguration

```bash
# Identitet
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.com"

# Default branch
git config --global init.defaultBranch main

# Editor
git config --global core.editor "code --wait"

# Se config
git config --list
```

## Grundläggande Workflow

```bash
# Skapa repo
git init

# Klona befintligt
git clone https://github.com/user/repo.git

# Status
git status

# Lägg till filer
git add file.txt
git add .

# Commit
git commit -m "Initial commit"
```

## Git Areas

```
Working Dir → Staging Area → Repository
     git add      git commit
```

**Nästa steg:** Node 2 - Git Basics
"""
            },
            {
                "title": "Git Basics",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 110,
                "content": r"""
# Git Basics

Dagliga Git-operationer.

## Status & Diff

```bash
# Status
git status
git status -s  # Short format

# Diff
git diff              # Working vs staging
git diff --staged     # Staging vs last commit
git diff HEAD~1       # Working vs previous commit
```

## Commit

```bash
# Commit med meddelande
git commit -m "Add feature"

# Commit alla ändringar
git commit -am "Update files"

# Ändra senaste commit
git commit --amend -m "Better message"
```

## Log

```bash
# Commit history
git log
git log --oneline
git log --oneline --graph
git log -5  # Senaste 5

# Sök i commits
git log --grep="fix"
git log --author="name"
```

## Undo

```bash
# Unstage fil
git restore --staged file.txt

# Discard changes
git restore file.txt

# Reset till commit
git reset HEAD~1         # Soft
git reset --hard HEAD~1  # Hard (farligt!)
```

| Kommando | Effekt |
|----------|--------|
| restore | Ångra working changes |
| reset --soft | Flytta HEAD, behåll staged |
| reset --hard | Radera allt |
| revert | Ny commit som ångrar |

**Nästa steg:** Node 3 - Branching
"""
            },
            {
                "title": "Branching",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Git Branching

Isolera arbete i branches.

## Branch-operationer

```bash
# Lista branches
git branch
git branch -a  # Alla inkl remote

# Skapa branch
git branch feature/login

# Byt branch
git checkout feature/login
git switch feature/login  # Nyare syntax

# Skapa och byt
git checkout -b feature/signup
git switch -c feature/signup

# Ta bort branch
git branch -d feature/done
git branch -D feature/force  # Force delete
```

## Merge

```bash
# Merge branch till main
git checkout main
git merge feature/login

# Fast-forward merge (linear)
# Sker automatiskt om möjligt

# Merge commit (3-way)
# Skapas vid divergerande historia
```

## Merge Conflicts

```bash
# Vid konflikt
<<<<<<< HEAD
din kod
=======
deras kod
>>>>>>> feature/login

# Efter fix
git add conflicted_file.txt
git commit -m "Resolve merge conflict"
```

## Branch Strategies

| Strategy | Användning |
|----------|-----------|
| Feature branches | En branch per feature |
| Git Flow | main, develop, feature, release |
| Trunk-based | Korta branches, frekventa merges |

**Nästa steg:** Node 4 - Remote Repositories
"""
            },
            {
                "title": "Remote Repositories",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 120,
                "content": r"""
# Remote Repositories

Samarbeta via remotes.

## Remote-operationer

```bash
# Lista remotes
git remote -v

# Lägg till remote
git remote add origin https://github.com/user/repo.git

# Ta bort remote
git remote remove origin

# Ändra URL
git remote set-url origin git@github.com:user/repo.git
```

## Push & Pull

```bash
# Push
git push origin main
git push -u origin main  # Set upstream

# Pull (fetch + merge)
git pull origin main

# Fetch (hämta utan merge)
git fetch origin
git fetch --all
```

## Tracking Branches

```bash
# Se tracking
git branch -vv

# Set upstream
git branch --set-upstream-to=origin/main

# Push med tracking
git push -u origin feature/login
```

## Pull med Rebase

```bash
# Pull med rebase istället för merge
git pull --rebase origin main

# Konfigurera default
git config --global pull.rebase true
```

| Kommando | Effekt |
|----------|--------|
| fetch | Hämta remote changes |
| pull | fetch + merge |
| push | Skicka till remote |

**Nästa steg:** Node 5 - GitHub Basics
"""
            },
            {
                "title": "GitHub Basics",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 120,
                "content": r"""
# GitHub Basics

GitHub för hosting och samarbete.

## SSH Setup

```bash
# Generera SSH-nyckel
ssh-keygen -t ed25519 -C "your@email.com"

# Starta agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Kopiera public key
cat ~/.ssh/id_ed25519.pub
# Lägg till i GitHub Settings > SSH Keys

# Testa
ssh -T git@github.com
```

## Repository Setup

```bash
# Klona med SSH
git clone git@github.com:user/repo.git

# Eller HTTPS
git clone https://github.com/user/repo.git
```

## GitHub CLI

```bash
# Installera
brew install gh

# Autentisera
gh auth login

# Skapa repo
gh repo create myproject --public

# Klona
gh repo clone user/repo
```

## README & License

```markdown
# Project Name

## Description
Brief description

## Installation
```bash
npm install
```

## Usage
How to use

## License
MIT
```

**Nästa steg:** Node 6 - Pull Requests
"""
            },
            {
                "title": "Pull Requests",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Pull Requests

Code review och merge workflow.

## PR Workflow

```bash
# 1. Skapa feature branch
git checkout -b feature/add-login

# 2. Gör ändringar och commit
git add .
git commit -m "Add login feature"

# 3. Push till GitHub
git push -u origin feature/add-login

# 4. Skapa PR på GitHub eller via CLI
gh pr create --title "Add login" --body "Description"
```

## GitHub CLI för PRs

```bash
# Lista PRs
gh pr list

# Se PR
gh pr view 123

# Checkout PR lokalt
gh pr checkout 123

# Merge PR
gh pr merge 123 --squash

# Review
gh pr review 123 --approve
```

## PR Template

```markdown
<!-- .github/pull_request_template.md -->
## Description
What does this PR do?

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change

## Checklist
- [ ] Tests added
- [ ] Documentation updated
- [ ] Linted
```

## Review Best Practices

| Tip | Beskrivning |
|-----|-------------|
| Små PRs | Lättare att reviewra |
| Beskrivning | Förklara varför |
| Screenshots | För UI-ändringar |
| Tests | Visa att det fungerar |

**Nästa steg:** Node 7 - Issues & Projects
"""
            },
            {
                "title": "Issues & Projects",
                "difficulty": "easy",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""
# Issues & Projects

Projekthantering på GitHub.

## Issues

```bash
# Skapa issue via CLI
gh issue create --title "Bug: Login fails" --body "Details..."

# Lista issues
gh issue list
gh issue list --assignee @me

# Stäng issue
gh issue close 123
```

## Issue Template

```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Bug Report
about: Report a bug
---

## Description
Clear description

## Steps to Reproduce
1. Go to...
2. Click...

## Expected Behavior
What should happen

## Actual Behavior
What happens

## Environment
- OS:
- Version:
```

## Labels

| Label | Användning |
|-------|-----------|
| bug | Fel |
| enhancement | Ny feature |
| documentation | Docs |
| good first issue | Nybörjarvänlig |
| help wanted | Behöver hjälp |

## GitHub Projects

```bash
# Skapa projekt
gh project create --title "Sprint 1"

# Lägg till issue
gh project item-add 1 --issue 123
```

## Automatisering

```yaml
# Close issue via commit
git commit -m "Fix login bug

Fixes #123"
```

**Nästa steg:** Node 8 - GitHub Actions Intro
"""
            },
            {
                "title": "GitHub Actions Intro",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# GitHub Actions Intro

CI/CD direkt i GitHub.

## Basic Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
```

## Triggers

```yaml
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:  # Manual trigger
```

## Secrets

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: ./deploy.sh
```

## Vanliga Actions

| Action | Användning |
|--------|-----------|
| actions/checkout | Klona repo |
| actions/setup-node | Node.js |
| actions/setup-python | Python |
| actions/cache | Cacha dependencies |

**Nästa steg:** Node 9 - Advanced Git
"""
            },
            {
                "title": "Advanced Git",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Advanced Git

Avancerade Git-tekniker.

## Rebase

```bash
# Rebase på main
git checkout feature
git rebase main

# Interaktiv rebase
git rebase -i HEAD~3
# pick, squash, edit, drop
```

## Cherry-pick

```bash
# Plocka specifik commit
git cherry-pick abc1234

# Flera commits
git cherry-pick abc1234 def5678
```

## Stash

```bash
# Spara temporärt
git stash
git stash push -m "WIP: feature"

# Lista stashes
git stash list

# Återställ
git stash pop       # Ta bort från stash
git stash apply     # Behåll i stash

# Drop
git stash drop stash@{0}
```

## Bisect

```bash
# Hitta buggig commit
git bisect start
git bisect bad           # Current is bad
git bisect good abc1234  # This was good

# Git testar commits
git bisect good  # or bad
# ... repeat until found

git bisect reset
```

## Worktrees

```bash
# Flera working directories
git worktree add ../hotfix hotfix-branch
git worktree list
git worktree remove ../hotfix
```

**Nästa steg:** Node 10 - Git Hooks
"""
            },
            {
                "title": "Git Hooks",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Git Hooks

Automatisering vid Git-events.

## Lokala Hooks

```bash
# .git/hooks/pre-commit
#!/bin/sh
npm run lint
npm test

# Gör körbar
chmod +x .git/hooks/pre-commit
```

## Vanliga Hooks

| Hook | När |
|------|-----|
| pre-commit | Före commit |
| commit-msg | Validera meddelande |
| pre-push | Före push |
| post-merge | Efter merge |

## Husky (Node.js)

```bash
# Installera
npm install husky --save-dev
npx husky init

# Lägg till hook
echo "npm test" > .husky/pre-commit
```

## Commit Message Hook

```bash
# .husky/commit-msg
#!/bin/sh
npx commitlint --edit $1
```

## Conventional Commits

```bash
# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

# Format
# type(scope): description
# feat(auth): add login endpoint
# fix(ui): correct button color
```

| Type | Användning |
|------|-----------|
| feat | Ny feature |
| fix | Buggfix |
| docs | Dokumentation |
| chore | Underhåll |

**Nästa steg:** Node 11 - Git Strategies
"""
            },
            {
                "title": "Git Strategies",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Git Branching Strategies

Välj rätt workflow.

## Git Flow

```
main ─────────●─────────────●───────
              │             │
release ──────┼─────●───────┤
              │     │       │
develop ──●───┼─────●───●───┼───●───
          │   │         │   │   │
feature ──●───┘         └───┘   │
                                │
hotfix ─────────────────────────●───
```

```bash
# Feature branch
git checkout -b feature/login develop
git checkout develop
git merge feature/login

# Release
git checkout -b release/1.0 develop
git checkout main
git merge release/1.0
git tag -a v1.0.0
```

## GitHub Flow

```bash
# Enklare: main + feature branches
git checkout -b feature/new-thing
# ... arbeta ...
git push origin feature/new-thing
# Skapa PR, review, merge to main
```

## Trunk-Based

```bash
# Korta branches, ofta merge
git checkout -b short-feature
# Max 1-2 dagar
git checkout main
git merge short-feature
```

## Val av Strategy

| Strategy | Team Size | Release |
|----------|-----------|---------|
| Git Flow | Stora | Scheduled |
| GitHub Flow | Medium | Continuous |
| Trunk-Based | Small | Continuous |

**Nästa steg:** Node 12 - Monorepo
"""
            },
            {
                "title": "Monorepo",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Monorepo Management

Flera projekt i ett repo.

## Struktur

```
monorepo/
├── packages/
│   ├── frontend/
│   ├── backend/
│   └── shared/
├── apps/
│   ├── web/
│   └── mobile/
├── package.json
└── turbo.json
```

## Turborepo

```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"]
    }
  }
}
```

```bash
# Kör i alla packages
turbo run build
turbo run test

# Affected only
turbo run build --filter=...[origin/main]
```

## Workspace

```json
// package.json
{
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

## Sparse Checkout

```bash
# Endast en del av repo
git sparse-checkout init
git sparse-checkout set packages/frontend
```

| Tool | Fokus |
|------|-------|
| Turborepo | JS/TS monorepos |
| Nx | Full-featured |
| Lerna | Package publishing |
| Bazel | Multi-language |

**Nästa steg:** Node 13 - Git Security
"""
            },
            {
                "title": "Git Security",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 135,
                "content": r"""
# Git Security

Säkerhet i versionshantering.

## Signed Commits

```bash
# Generera GPG-nyckel
gpg --full-generate-key

# Lista nycklar
gpg --list-secret-keys --keyid-format=long

# Konfigurera Git
git config --global user.signingkey ABC123
git config --global commit.gpgsign true

# Signera commit
git commit -S -m "Signed commit"

# Verifiera
git verify-commit HEAD
```

## .gitignore Secrets

```gitignore
# .gitignore
.env
.env.local
*.pem
*.key
secrets/
config/production.json
```

## Pre-commit Secret Scan

```bash
# Installera
pip install detect-secrets

# Scan
detect-secrets scan > .secrets.baseline

# Pre-commit hook
detect-secrets-hook --baseline .secrets.baseline
```

## Ta bort Secrets från History

```bash
# BFG Repo-Cleaner
bfg --delete-files secrets.txt
bfg --replace-text passwords.txt

# Git filter-branch (långsam)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.txt"
```

| Risk | Lösning |
|------|---------|
| Secrets i kod | .gitignore + scanning |
| Osignerade commits | GPG signing |
| Läckt secret | Rotera + BFG |

**Nästa steg:** Node 14 - Git Recovery
"""
            },
            {
                "title": "Git Recovery",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Git Recovery

Återställ förlorat arbete.

## Reflog

```bash
# Se alla HEAD-ändringar
git reflog

# Återställ till tidigare state
git reset --hard HEAD@{5}

# Återställ raderad branch
git checkout -b recovered HEAD@{10}
```

## Återställ Commits

```bash
# Ångra reset
git reflog
git reset --hard abc1234

# Återskapa commit
git cherry-pick abc1234
```

## Återställ Filer

```bash
# Från specifik commit
git checkout abc1234 -- file.txt

# Från stash
git stash show -p stash@{0} | git apply

# Från index
git checkout --cached file.txt
```

## Fsck

```bash
# Hitta dangling objects
git fsck --lost-found

# Återställ dangling commit
git show abc1234
git branch recovered abc1234
```

## Backup Strategier

```bash
# Klona som backup
git clone --mirror repo.git repo-backup.git

# Bundle
git bundle create backup.bundle --all
git clone backup.bundle restored-repo
```

| Scenario | Kommando |
|----------|----------|
| Ångra reset | reflog + reset |
| Raderad branch | reflog + checkout |
| Förlorad commit | fsck + cherry-pick |

**Nästa steg:** Node 15 - Git Best Practices
"""
            },
            {
                "title": "Git Best Practices",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 150,
                "content": r"""
# Git Best Practices

Professionell Git-användning.

## Commit Messages

```bash
# Format
<type>(<scope>): <subject>

<body>

<footer>

# Exempel
feat(auth): add OAuth2 login

Implement GitHub OAuth2 authentication
with token refresh support.

Closes #123
```

## Small Commits

```bash
# Atomic commits
git add -p file.txt  # Interaktiv staging

# Partial commits
git add --patch
```

## Branch Naming

```
feature/add-login
bugfix/fix-header
hotfix/security-patch
release/v1.2.0
docs/update-readme
```

## Repo Hygiene

```bash
# Cleanup
git gc
git prune

# Remove merged branches
git branch --merged | grep -v main | xargs git branch -d
```

## Checklist

| Practice | Varför |
|----------|--------|
| Små commits | Lättare review/revert |
| Bra meddelanden | Dokumentation |
| Branch per feature | Isolering |
| Rebase före merge | Clean history |
| Signera commits | Verifiering |
| Aldrig force push main | Skydda delad historia |
| Review all PRs | Kvalitet |

**🎉 Grattis! Du har slutfört Git & GitHub Mastery SkillsMap!**
"""
            },
            {
                "title": "Git Introduktion",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 100,
                "content": r"""
# Git Introduktion

Git är industristandard för versionshantering.

## Installation

```bash
# macOS
brew install git

# Ubuntu
sudo apt install git

# Verifiera
git --version
```

## Konfiguration

```bash
# Identitet
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.com"

# Default branch
git config --global init.defaultBranch main

# Editor
git config --global core.editor "code --wait"

# Se config
git config --list
```

## Grundläggande Workflow

```bash
# Skapa repo
git init

# Klona befintligt
git clone https://github.com/user/repo.git

# Status
git status

# Lägg till filer
git add file.txt
git add .

# Commit
git commit -m "Initial commit"
```

## Git Areas

```
Working Dir → Staging Area → Repository
     git add      git commit
```

**Nästa steg:** Node 2 - Git Basics
"""
            },
            {
                "title": "Git Basics",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 110,
                "content": r"""
# Git Basics

Dagliga Git-operationer.

## Status & Diff

```bash
# Status
git status
git status -s  # Short format

# Diff
git diff              # Working vs staging
git diff --staged     # Staging vs last commit
git diff HEAD~1       # Working vs previous commit
```

## Commit

```bash
# Commit med meddelande
git commit -m "Add feature"

# Commit alla ändringar
git commit -am "Update files"

# Ändra senaste commit
git commit --amend -m "Better message"
```

## Log

```bash
# Commit history
git log
git log --oneline
git log --oneline --graph
git log -5  # Senaste 5

# Sök i commits
git log --grep="fix"
git log --author="name"
```

## Undo

```bash
# Unstage fil
git restore --staged file.txt

# Discard changes
git restore file.txt

# Reset till commit
git reset HEAD~1         # Soft
git reset --hard HEAD~1  # Hard (farligt!)
```

| Kommando | Effekt |
|----------|--------|
| restore | Ångra working changes |
| reset --soft | Flytta HEAD, behåll staged |
| reset --hard | Radera allt |
| revert | Ny commit som ångrar |

**Nästa steg:** Node 3 - Branching
"""
            },
            {
                "title": "Branching",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Git Branching

Isolera arbete i branches.

## Branch-operationer

```bash
# Lista branches
git branch
git branch -a  # Alla inkl remote

# Skapa branch
git branch feature/login

# Byt branch
git checkout feature/login
git switch feature/login  # Nyare syntax

# Skapa och byt
git checkout -b feature/signup
git switch -c feature/signup

# Ta bort branch
git branch -d feature/done
git branch -D feature/force  # Force delete
```

## Merge

```bash
# Merge branch till main
git checkout main
git merge feature/login

# Fast-forward merge (linear)
# Sker automatiskt om möjligt

# Merge commit (3-way)
# Skapas vid divergerande historia
```

## Merge Conflicts

```bash
# Vid konflikt
<<<<<<< HEAD
din kod
=======
deras kod
>>>>>>> feature/login

# Efter fix
git add conflicted_file.txt
git commit -m "Resolve merge conflict"
```

## Branch Strategies

| Strategy | Användning |
|----------|-----------|
| Feature branches | En branch per feature |
| Git Flow | main, develop, feature, release |
| Trunk-based | Korta branches, frekventa merges |

**Nästa steg:** Node 4 - Remote Repositories
"""
            },
            {
                "title": "Remote Repositories",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 120,
                "content": r"""
# Remote Repositories

Samarbeta via remotes.

## Remote-operationer

```bash
# Lista remotes
git remote -v

# Lägg till remote
git remote add origin https://github.com/user/repo.git

# Ta bort remote
git remote remove origin

# Ändra URL
git remote set-url origin git@github.com:user/repo.git
```

## Push & Pull

```bash
# Push
git push origin main
git push -u origin main  # Set upstream

# Pull (fetch + merge)
git pull origin main

# Fetch (hämta utan merge)
git fetch origin
git fetch --all
```

## Tracking Branches

```bash
# Se tracking
git branch -vv

# Set upstream
git branch --set-upstream-to=origin/main

# Push med tracking
git push -u origin feature/login
```

## Pull med Rebase

```bash
# Pull med rebase istället för merge
git pull --rebase origin main

# Konfigurera default
git config --global pull.rebase true
```

| Kommando | Effekt |
|----------|--------|
| fetch | Hämta remote changes |
| pull | fetch + merge |
| push | Skicka till remote |

**Nästa steg:** Node 5 - GitHub Basics
"""
            },
            {
                "title": "GitHub Basics",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 120,
                "content": r"""
# GitHub Basics

GitHub för hosting och samarbete.

## SSH Setup

```bash
# Generera SSH-nyckel
ssh-keygen -t ed25519 -C "your@email.com"

# Starta agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Kopiera public key
cat ~/.ssh/id_ed25519.pub
# Lägg till i GitHub Settings > SSH Keys

# Testa
ssh -T git@github.com
```

## Repository Setup

```bash
# Klona med SSH
git clone git@github.com:user/repo.git

# Eller HTTPS
git clone https://github.com/user/repo.git
```

## GitHub CLI

```bash
# Installera
brew install gh

# Autentisera
gh auth login

# Skapa repo
gh repo create myproject --public

# Klona
gh repo clone user/repo
```

## README & License

```markdown
# Project Name

## Description
Brief description

## Installation
```bash
npm install
```

## Usage
How to use

## License
MIT
```

**Nästa steg:** Node 6 - Pull Requests
"""
            },
            {
                "title": "Pull Requests",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Pull Requests

Code review och merge workflow.

## PR Workflow

```bash
# 1. Skapa feature branch
git checkout -b feature/add-login

# 2. Gör ändringar och commit
git add .
git commit -m "Add login feature"

# 3. Push till GitHub
git push -u origin feature/add-login

# 4. Skapa PR på GitHub eller via CLI
gh pr create --title "Add login" --body "Description"
```

## GitHub CLI för PRs

```bash
# Lista PRs
gh pr list

# Se PR
gh pr view 123

# Checkout PR lokalt
gh pr checkout 123

# Merge PR
gh pr merge 123 --squash

# Review
gh pr review 123 --approve
```

## PR Template

```markdown
<!-- .github/pull_request_template.md -->
## Description
What does this PR do?

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change

## Checklist
- [ ] Tests added
- [ ] Documentation updated
- [ ] Linted
```

## Review Best Practices

| Tip | Beskrivning |
|-----|-------------|
| Små PRs | Lättare att reviewra |
| Beskrivning | Förklara varför |
| Screenshots | För UI-ändringar |
| Tests | Visa att det fungerar |

**Nästa steg:** Node 7 - Issues & Projects
"""
            },
            {
                "title": "Issues & Projects",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""
# Issues & Projects

Projekthantering på GitHub.

## Issues

```bash
# Skapa issue via CLI
gh issue create --title "Bug: Login fails" --body "Details..."

# Lista issues
gh issue list
gh issue list --assignee @me

# Stäng issue
gh issue close 123
```

## Issue Template

```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Bug Report
about: Report a bug
---

## Description
Clear description

## Steps to Reproduce
1. Go to...
2. Click...

## Expected Behavior
What should happen

## Actual Behavior
What happens

## Environment
- OS:
- Version:
```

## Labels

| Label | Användning |
|-------|-----------|
| bug | Fel |
| enhancement | Ny feature |
| documentation | Docs |
| good first issue | Nybörjarvänlig |
| help wanted | Behöver hjälp |

## GitHub Projects

```bash
# Skapa projekt
gh project create --title "Sprint 1"

# Lägg till issue
gh project item-add 1 --issue 123
```

## Automatisering

```yaml
# Close issue via commit
git commit -m "Fix login bug

Fixes #123"
```

**Nästa steg:** Node 8 - GitHub Actions Intro
"""
            },
            {
                "title": "GitHub Actions Intro",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# GitHub Actions Intro

CI/CD direkt i GitHub.

## Basic Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
```

## Triggers

```yaml
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:  # Manual trigger
```

## Secrets

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: ./deploy.sh
```

## Vanliga Actions

| Action | Användning |
|--------|-----------|
| actions/checkout | Klona repo |
| actions/setup-node | Node.js |
| actions/setup-python | Python |
| actions/cache | Cacha dependencies |

**Nästa steg:** Node 9 - Advanced Git
"""
            },
            {
                "title": "Advanced Git",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Advanced Git

Avancerade Git-tekniker.

## Rebase

```bash
# Rebase på main
git checkout feature
git rebase main

# Interaktiv rebase
git rebase -i HEAD~3
# pick, squash, edit, drop
```

## Cherry-pick

```bash
# Plocka specifik commit
git cherry-pick abc1234

# Flera commits
git cherry-pick abc1234 def5678
```

## Stash

```bash
# Spara temporärt
git stash
git stash push -m "WIP: feature"

# Lista stashes
git stash list

# Återställ
git stash pop       # Ta bort från stash
git stash apply     # Behåll i stash

# Drop
git stash drop stash@{0}
```

## Bisect

```bash
# Hitta buggig commit
git bisect start
git bisect bad           # Current is bad
git bisect good abc1234  # This was good

# Git testar commits
git bisect good  # or bad
# ... repeat until found

git bisect reset
```

## Worktrees

```bash
# Flera working directories
git worktree add ../hotfix hotfix-branch
git worktree list
git worktree remove ../hotfix
```

**Nästa steg:** Node 10 - Git Hooks
"""
            },
            {
                "title": "Git Hooks",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Git Hooks

Automatisering vid Git-events.

## Lokala Hooks

```bash
# .git/hooks/pre-commit
#!/bin/sh
npm run lint
npm test

# Gör körbar
chmod +x .git/hooks/pre-commit
```

## Vanliga Hooks

| Hook | När |
|------|-----|
| pre-commit | Före commit |
| commit-msg | Validera meddelande |
| pre-push | Före push |
| post-merge | Efter merge |

## Husky (Node.js)

```bash
# Installera
npm install husky --save-dev
npx husky init

# Lägg till hook
echo "npm test" > .husky/pre-commit
```

## Commit Message Hook

```bash
# .husky/commit-msg
#!/bin/sh
npx commitlint --edit $1
```

## Conventional Commits

```bash
# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

# Format
# type(scope): description
# feat(auth): add login endpoint
# fix(ui): correct button color
```

| Type | Användning |
|------|-----------|
| feat | Ny feature |
| fix | Buggfix |
| docs | Dokumentation |
| chore | Underhåll |

**Nästa steg:** Node 11 - Git Strategies
"""
            },
            {
                "title": "Git Strategies",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Git Branching Strategies

Välj rätt workflow.

## Git Flow

```
main ─────────●─────────────●───────
              │             │
release ──────┼─────●───────┤
              │     │       │
develop ──●───┼─────●───●───┼───●───
          │   │         │   │   │
feature ──●───┘         └───┘   │
                                │
hotfix ─────────────────────────●───
```

```bash
# Feature branch
git checkout -b feature/login develop
git checkout develop
git merge feature/login

# Release
git checkout -b release/1.0 develop
git checkout main
git merge release/1.0
git tag -a v1.0.0
```

## GitHub Flow

```bash
# Enklare: main + feature branches
git checkout -b feature/new-thing
# ... arbeta ...
git push origin feature/new-thing
# Skapa PR, review, merge to main
```

## Trunk-Based

```bash
# Korta branches, ofta merge
git checkout -b short-feature
# Max 1-2 dagar
git checkout main
git merge short-feature
```

## Val av Strategy

| Strategy | Team Size | Release |
|----------|-----------|---------|
| Git Flow | Stora | Scheduled |
| GitHub Flow | Medium | Continuous |
| Trunk-Based | Small | Continuous |

**Nästa steg:** Node 12 - Monorepo
"""
            },
            {
                "title": "Monorepo",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Monorepo Management

Flera projekt i ett repo.

## Struktur

```
monorepo/
├── packages/
│   ├── frontend/
│   ├── backend/
│   └── shared/
├── apps/
│   ├── web/
│   └── mobile/
├── package.json
└── turbo.json
```

## Turborepo

```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"]
    }
  }
}
```

```bash
# Kör i alla packages
turbo run build
turbo run test

# Affected only
turbo run build --filter=...[origin/main]
```

## Workspace

```json
// package.json
{
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

## Sparse Checkout

```bash
# Endast en del av repo
git sparse-checkout init
git sparse-checkout set packages/frontend
```

| Tool | Fokus |
|------|-------|
| Turborepo | JS/TS monorepos |
| Nx | Full-featured |
| Lerna | Package publishing |
| Bazel | Multi-language |

**Nästa steg:** Node 13 - Git Security
"""
            },
            {
                "title": "Git Security",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 135,
                "content": r"""
# Git Security

Säkerhet i versionshantering.

## Signed Commits

```bash
# Generera GPG-nyckel
gpg --full-generate-key

# Lista nycklar
gpg --list-secret-keys --keyid-format=long

# Konfigurera Git
git config --global user.signingkey ABC123
git config --global commit.gpgsign true

# Signera commit
git commit -S -m "Signed commit"

# Verifiera
git verify-commit HEAD
```

## .gitignore Secrets

```gitignore
# .gitignore
.env
.env.local
*.pem
*.key
secrets/
config/production.json
```

## Pre-commit Secret Scan

```bash
# Installera
pip install detect-secrets

# Scan
detect-secrets scan > .secrets.baseline

# Pre-commit hook
detect-secrets-hook --baseline .secrets.baseline
```

## Ta bort Secrets från History

```bash
# BFG Repo-Cleaner
bfg --delete-files secrets.txt
bfg --replace-text passwords.txt

# Git filter-branch (långsam)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.txt"
```

| Risk | Lösning |
|------|---------|
| Secrets i kod | .gitignore + scanning |
| Osignerade commits | GPG signing |
| Läckt secret | Rotera + BFG |

**Nästa steg:** Node 14 - Git Recovery
"""
            },
            {
                "title": "Git Recovery",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Git Recovery

Återställ förlorat arbete.

## Reflog

```bash
# Se alla HEAD-ändringar
git reflog

# Återställ till tidigare state
git reset --hard HEAD@{5}

# Återställ raderad branch
git checkout -b recovered HEAD@{10}
```

## Återställ Commits

```bash
# Ångra reset
git reflog
git reset --hard abc1234

# Återskapa commit
git cherry-pick abc1234
```

## Återställ Filer

```bash
# Från specifik commit
git checkout abc1234 -- file.txt

# Från stash
git stash show -p stash@{0} | git apply

# Från index
git checkout --cached file.txt
```

## Fsck

```bash
# Hitta dangling objects
git fsck --lost-found

# Återställ dangling commit
git show abc1234
git branch recovered abc1234
```

## Backup Strategier

```bash
# Klona som backup
git clone --mirror repo.git repo-backup.git

# Bundle
git bundle create backup.bundle --all
git clone backup.bundle restored-repo
```

| Scenario | Kommando |
|----------|----------|
| Ångra reset | reflog + reset |
| Raderad branch | reflog + checkout |
| Förlorad commit | fsck + cherry-pick |

**Nästa steg:** Node 15 - Git Best Practices
"""
            },
            {
                "title": "Git Best Practices",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 150,
                "content": r"""
# Git Best Practices

Professionell Git-användning.

## Commit Messages

```bash
# Format
<type>(<scope>): <subject>

<body>

<footer>

# Exempel
feat(auth): add OAuth2 login

Implement GitHub OAuth2 authentication
with token refresh support.

Closes #123
```

## Small Commits

```bash
# Atomic commits
git add -p file.txt  # Interaktiv staging

# Partial commits
git add --patch
```

## Branch Naming

```
feature/add-login
bugfix/fix-header
hotfix/security-patch
release/v1.2.0
docs/update-readme
```

## Repo Hygiene

```bash
# Cleanup
git gc
git prune

# Remove merged branches
git branch --merged | grep -v main | xargs git branch -d
```

## Checklist

| Practice | Varför |
|----------|--------|
| Små commits | Lättare review/revert |
| Bra meddelanden | Dokumentation |
| Branch per feature | Isolering |
| Rebase före merge | Clean history |
| Signera commits | Verifiering |
| Aldrig force push main | Skydda delad historia |
| Review all PRs | Kvalitet |

**🎉 Grattis! Du har slutfört Git & GitHub Mastery SkillsMap!**
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_GIT_GITHUB_MASTERY


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_GIT_GITHUB_MASTERY["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
