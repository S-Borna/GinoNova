# =============================================================================
# BLOCK 4: GITHUB COLLABORATION PART 1 (Noder 13-14)
# =============================================================================

NODE_13_GITHUB_PLATFORM = {
    "node_id": 13,
    "title": "GitHub Platform Deep Dive",
    "slug": "github-platform-deep-dive",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": ["monorepo-scale"],
    "content": r'''
# GitHub Platform Deep Dive

## Varför detta är kritiskt

> "GitHub är inte bara Git hosting. Det är hela ekosystemet för modern mjukvaruutveckling — collaboration, CI/CD, project management, security scanning, och community."

---

## GitHub Architecture

```
+-------------------------------------------------------------------------+
|                       GITHUB ECOSYSTEM                                  |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------------------------------------------------+   |
|   |                    REPOSITORY                                   |   |
|   +-----------------------------------------------------------------+   |
|   |                                                                 |   |
|   |  CODE              ISSUES           PULL REQUESTS               |   |
|   |  ----              ------           -------------               |   |
|   |  • Branches        • Bug reports    • Code review               |   |
|   |  • Commits         • Features       • Discussion                |   |
|   |  • Tags/Releases   • Tasks          • CI checks                 |   |
|   |  • File browser    • Labels         • Merge options             |   |
|   |                                                                 |   |
|   |  ACTIONS           PROJECTS         WIKI/DOCS                   |   |
|   |  -------           --------         ---------                   |   |
|   |  • CI/CD           • Kanban         • Documentation             |   |
|   |  • Automation      • Roadmap        • Guides                    |   |
|   |  • Workflows       • Sprints        • API docs                  |   |
|   |                                                                 |   |
|   |  SECURITY          INSIGHTS         SETTINGS                    |   |
|   |  --------          --------         --------                    |   |
|   |  • Dependabot      • Contributors   • Branch rules              |   |
|   |  • Code scanning   • Traffic        • Webhooks                  |   |
|   |  • Secret scanning • Commits        • Integrations              |   |
|   |                                                                 |   |
|   +-----------------------------------------------------------------+   |
|                                                                         |
|   ORGANIZATION FEATURES:                                                |
|   • Teams & permissions                                                 |
|   • Enterprise security                                                 |
|   • Audit logs                                                          |
|   • SAML/SSO                                                            |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Repository Setup

### Creating Repository

```bash
# Via GitHub CLI (gh):
gh repo create my-project --public --description "My awesome project"

# Create and clone in one step
gh repo create my-project --public --clone

# Create from template
gh repo create my-project --template owner/template-repo

# Create private repo
gh repo create my-project --private
```

### Initial Setup

```bash
# Local project -> GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

### Repository Settings

```
+-------------------------------------------------------------------------+
|                    REPOSITORY SETTINGS                                  |
+-------------------------------------------------------------------------+
|                                                                         |
|   GENERAL:                                                              |
|   +-- Default branch: main                                              |
|   +-- Features: Issues ✓, Projects ✓, Wiki ✓                            |
|   +-- Pull Requests:                                                    |
|       +-- Allow merge commits ✓                                         |
|       +-- Allow squash merging ✓                                        |
|       +-- Allow rebase merging ✓                                        |
|                                                                         |
|   BRANCH PROTECTION (Settings -> Branches):                              |
|   +-- Require PR before merging                                         |
|   +-- Require status checks                                             |
|   +-- Require review (1-2 approvals)                                    |
|   +-- Dismiss stale reviews                                             |
|   +-- Require linear history (optional)                                 |
|                                                                         |
|   COLLABORATORS:                                                        |
|   +-- Settings -> Collaborators                                          |
|   +-- Add by username or email                                          |
|   +-- Permission levels:                                                |
|       +-- Read      - Clone, pull                                       |
|       +-- Triage    - Manage issues                                     |
|       +-- Write     - Push, merge                                       |
|       +-- Maintain  - Manage repo (no delete)                           |
|       +-- Admin     - Full access                                       |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## SSH Key Setup

### Generate SSH Key

```bash
# Generate Ed25519 key (recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Or RSA (legacy compatibility)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# macOS: Add to keychain
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

### Add to GitHub

```bash
# Copy public key
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip   # Linux

# Go to: GitHub -> Settings -> SSH and GPG keys -> New SSH key
# Paste the key

# Test connection
ssh -T git@github.com
# Hi username! You've successfully authenticated...
```

### Configure Git for SSH

```bash
# Use SSH for all GitHub repos
git config --global url."git@github.com:".insteadOf "https://github.com/"

# Or per-repo
cd my-repo
git remote set-url origin git@github.com:user/repo.git
```

---

## GitHub CLI (gh)

### Installation

```bash
# macOS
brew install gh

# Ubuntu
sudo apt install gh

# Windows
winget install GitHub.cli
```

### Authentication

```bash
# Login
gh auth login
# Choose: GitHub.com
# Choose: HTTPS or SSH
# Authenticate via browser

# Status
gh auth status

# Logout
gh auth logout
```

### Common Commands

```bash
# Repository operations
gh repo create
gh repo clone owner/repo
gh repo fork owner/repo
gh repo view
gh repo list

# Issues
gh issue list
gh issue create
gh issue view 123
gh issue close 123
gh issue comment 123 --body "Comment"

# Pull Requests
gh pr list
gh pr create
gh pr checkout 123
gh pr merge 123
gh pr review 123 --approve

# Actions
gh run list
gh run view
gh run watch
gh run rerun 123

# Gists
gh gist create file.py
gh gist list
gh gist view
```

---

## README Best Practices

### Structure

```markdown
# Project Name

Short description of what the project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

‍‍‍bash
npm install project-name
‍‍‍

## Usage

‍‍‍javascript
const project = require('project-name');
project.doSomething();
‍‍‍

## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| port   | 3000    | Server port |
| debug  | false   | Enable debug |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT © Your Name
```

### Badges

```markdown
![Build Status](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)
![npm version](https://img.shields.io/npm/v/package-name)
![License](https://img.shields.io/github/license/user/repo)
![Downloads](https://img.shields.io/npm/dm/package-name)
```

---

## GitHub Features

### GitHub Pages

```yaml
# Enable in Settings -> Pages
# Source: Branch (main) / Folder (/docs or /)

# Jekyll config (_config.yml)
theme: jekyll-theme-minimal
title: My Project
description: Project description
```

### Releases

```bash
# Create release via CLI
gh release create v1.0.0 --title "Version 1.0.0" --notes "Release notes"

# Upload assets
gh release create v1.0.0 ./dist/*.zip

# Create from tag
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
gh release create v1.0.0 --generate-notes
```

### GitHub Packages

```json
{
  "name": "@owner/package-name",
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  }
}
```

---

## Repository Templates

### Creating Template

```
1. Create repository with common structure
2. Add template files:
   - README.md (with placeholders)
   - .github/ISSUE_TEMPLATE/
   - .github/PULL_REQUEST_TEMPLATE.md
   - .github/workflows/
   - Standard config files

3. Settings -> ✓ Template repository
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

## Security Features

### Dependabot

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### Secret Scanning

```
Automatically enabled for public repos
Enable in Settings -> Security -> Secret scanning

GitHub scans for:
- API keys
- OAuth tokens
- SSH keys
- Database credentials
- Cloud provider keys
```

---

## Sammanfattning

| Feature | Purpose | Access |
|---------|---------|--------|
| Repository | Code hosting | github.com |
| Issues | Bug tracking | Repo -> Issues |
| Actions | CI/CD | Repo -> Actions |
| Pages | Static hosting | Settings -> Pages |
| Packages | Package registry | Packages tab |
| Security | Vulnerability alerts | Security tab |

---

## Nästa Steg

GitHub platform behärskad. Nästa: **Pull Requests Mastery** — code review och collaboration.
''',
}

NODE_14_PULL_REQUESTS = {
    "node_id": 14,
    "title": "Pull Requests Mastery",
    "slug": "pull-requests-mastery",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": ["github-platform-deep-dive"],
    "content": r'''
# Pull Requests Mastery

## Varför detta är kritiskt

> "Pull Requests är hjärtat av code review, knowledge sharing, och kvalitetssäkring. En bra PR-kultur = ett bra team."

---

## Pull Request Anatomy

```
+-------------------------------------------------------------------------+
|                       PULL REQUEST STRUCTURE                            |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------------------------------------------------+   |
|   | Title: feat: implement user authentication                      |   |
|   +-----------------------------------------------------------------+   |
|   |                                                                 |   |
|   | DESCRIPTION                                                     |   |
|   | -----------                                                     |   |
|   | ## What                                                         |   |
|   | Adds OAuth2 login with Google provider                          |   |
|   |                                                                 |   |
|   | ## Why                                                          |   |
|   | Users requested social login (Issue #123)                       |   |
|   |                                                                 |   |
|   | ## How                                                          |   |
|   | - Added passport-google-oauth20                                 |   |
|   | - Created auth routes                                           |   |
|   | - Updated user model                                            |   |
|   |                                                                 |   |
|   | ## Testing                                                      |   |
|   | - [ ] Unit tests pass                                           |   |
|   | - [ ] Manual testing done                                       |   |
|   | - [ ] Tested logout flow                                        |   |
|   |                                                                 |   |
|   | Closes #123                                                     |   |
|   |                                                                 |   |
|   +-----------------------------------------------------------------+   |
|   | Reviewers: @teammate1, @teammate2                               |   |
|   | Labels: feature, auth, needs-review                             |   |
|   | Project: Sprint 12                                              |   |
|   | Milestone: v2.0                                                 |   |
|   +-----------------------------------------------------------------+   |
|                                                                         |
|   TABS:                                                                 |
|   [Conversation] [Commits] [Checks] [Files changed]                     |
|                                                                         |
|   STATUS CHECKS:                                                        |
|   ✓ Build passing                                                       |
|   ✓ Tests (142/142)                                                     |
|   ✓ Lint                                                                |
|   ✓ Security scan                                                       |
|   ⏳ Review required (0/2)                                              |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Creating Pull Requests

### From Command Line

```bash
# Create feature branch
git checkout -b feature/user-auth
# ... make changes ...
git add .
git commit -m "feat: implement OAuth login"
git push -u origin feature/user-auth

# Create PR via gh CLI
gh pr create --title "feat: implement user authentication" \
  --body "Adds OAuth2 login support. Closes #123" \
  --reviewer teammate1,teammate2 \
  --label "feature,auth"

# Create PR and open in browser
gh pr create --web

# Create draft PR
gh pr create --draft
```

### PR Template

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->

## Description
<!-- What does this PR do? -->

## Related Issues
<!-- Link issues: Closes #123 -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented hard-to-understand areas
- [ ] I have made corresponding documentation updates
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing unit tests pass locally

## Screenshots (if applicable)
<!-- Add screenshots for UI changes -->
```

---

## Code Review Best Practices

### As Author

```
+-------------------------------------------------------------------------+
|                    PR AUTHOR CHECKLIST                                  |
+-------------------------------------------------------------------------+
|                                                                         |
|   BEFORE REQUESTING REVIEW:                                             |
|   +-- ✓ Self-review your diff                                           |
|   +-- ✓ Ensure CI passes                                                |
|   +-- ✓ Write clear description                                         |
|   +-- ✓ Keep PR small (< 400 lines ideal)                               |
|   +-- ✓ Separate refactoring from features                              |
|   +-- ✓ Respond to feedback promptly                                    |
|                                                                         |
|   GOOD PR HYGIENE:                                                      |
|   +-- One feature per PR                                                |
|   +-- Descriptive commit messages                                       |
|   +-- No commented-out code                                             |
|   +-- No debug statements                                               |
|   +-- Tests included                                                    |
|                                                                         |
+-------------------------------------------------------------------------+
```

### As Reviewer

```
+-------------------------------------------------------------------------+
|                    REVIEWER CHECKLIST                                   |
+-------------------------------------------------------------------------+
|                                                                         |
|   CODE QUALITY:                                                         |
|   +-- [ ] Logic is correct                                              |
|   +-- [ ] No obvious bugs                                               |
|   +-- [ ] Error handling present                                        |
|   +-- [ ] Edge cases handled                                            |
|                                                                         |
|   DESIGN:                                                               |
|   +-- [ ] Follows project patterns                                      |
|   +-- [ ] No unnecessary complexity                                     |
|   +-- [ ] Good naming                                                   |
|   +-- [ ] Single responsibility                                         |
|                                                                         |
|   SECURITY:                                                             |
|   +-- [ ] No hardcoded secrets                                          |
|   +-- [ ] Input validation                                              |
|   +-- [ ] No SQL injection                                              |
|   +-- [ ] Auth/authz correct                                            |
|                                                                         |
|   PERFORMANCE:                                                          |
|   +-- [ ] No N+1 queries                                                |
|   +-- [ ] Reasonable time complexity                                    |
|   +-- [ ] No memory leaks                                               |
|                                                                         |
|   TESTING:                                                              |
|   +-- [ ] Tests exist                                                   |
|   +-- [ ] Tests are meaningful                                          |
|   +-- [ ] Edge cases tested                                             |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Review Comments

### Comment Types

```
BLOCKING (Request Changes):
❌ "This will cause a null pointer exception when user is undefined"
❌ "SQL injection vulnerability here"
❌ "This breaks the API contract"

SUGGESTIONS (Non-blocking):
💡 "Consider extracting this to a helper function"
💡 "You could use destructuring here"
💡 "Optional: this could be more efficient with a Map"

QUESTIONS:
❓ "Why did you choose this approach over X?"
❓ "How does this handle the case where...?"

PRAISE:
👍 "Great solution!"
👍 "Nice refactor, much cleaner"
```

### Suggesting Changes

```markdown
<!-- In GitHub review, use suggestion blocks -->

‍‍‍suggestion
const user = await getUserById(id);
if (!user) {
  throw new NotFoundError('User not found');
}
‍‍‍
```

---

## Merge Strategies

```
+--------------------------------------------------------------------+
|                       MERGE STRATEGIES                             |
+--------------------------------------------------------------------+
|                                                                    |
|   MERGE COMMIT (--no-ff)                                           |
|   ----------------------                                           |
|   main:     A --- B ----------- M                                  |
|                   |            /|                                  |
|   feature:        +--- C --- D-+                                   |
|                                                                    |
|   • Preserves complete history                                     |
|   • Clear when feature was merged                                  |
|   • Extra merge commits                                            |
|                                                                    |
|   SQUASH AND MERGE                                                 |
|   ----------------                                                 |
|   main:     A --- B --- S                                          |
|                                                                    |
|   feature:        +--- C --- D (discarded)                         |
|                                                                    |
|   • Single commit for entire PR                                    |
|   • Clean main history                                             |
|   • Lose individual commit history                                 |
|                                                                    |
|   REBASE AND MERGE                                                 |
|   ----------------                                                 |
|   main:     A --- B --- C' --- D'                                  |
|                                                                    |
|   • Linear history                                                 |
|   • Individual commits preserved                                   |
|   • No merge commits                                               |
|                                                                    |
+--------------------------------------------------------------------+
```

### Merge Commands

```bash
# Via gh CLI
gh pr merge 123 --merge     # Merge commit
gh pr merge 123 --squash    # Squash and merge
gh pr merge 123 --rebase    # Rebase and merge

# Auto-merge when checks pass
gh pr merge 123 --auto --squash

# Delete branch after merge
gh pr merge 123 --squash --delete-branch
```

---

## PR Workflow

### Feature Branch Flow

```bash
# 1. Create branch
git checkout main
git pull
git checkout -b feature/awesome-feature

# 2. Work on feature
# ... make changes ...
git add .
git commit -m "feat: add awesome feature"

# 3. Keep updated with main
git fetch origin main
git rebase origin/main  # or merge

# 4. Push and create PR
git push -u origin feature/awesome-feature
gh pr create

# 5. Address review feedback
# ... make changes ...
git add .
git commit -m "refactor: address review feedback"
git push

# 6. After approval, merge
gh pr merge --squash --delete-branch
```

### Handling Conflicts

```bash
# If PR has conflicts:

# 1. Update local main
git checkout main
git pull

# 2. Rebase feature branch
git checkout feature/awesome
git rebase main

# 3. Resolve conflicts
# Edit conflicted files
git add .
git rebase --continue

# 4. Force push (safe for feature branches)
git push --force-with-lease
```

---

## Advanced PR Features

### Draft PRs

```bash
# Create as draft
gh pr create --draft

# Convert to ready
gh pr ready 123

# Use cases:
# - Early feedback
# - CI/CD testing
# - Work in progress
```

### Auto-merge

```yaml
# Enable in repo settings
Settings -> General -> Allow auto-merge

# Set up via CLI
gh pr merge 123 --auto --squash

# Requirements:
# - Branch protection enabled
# - Required checks must pass
# - Required reviews must approve
```

### PR Automation

```yaml
# .github/workflows/pr-automation.yml
name: PR Automation
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}

  size-label:
    runs-on: ubuntu-latest
    steps:
      - uses: codelytv/pr-size-labeler@v1
        with:
          xs_max_size: 10
          s_max_size: 100
          m_max_size: 500
          l_max_size: 1000
```

---

## Multi-reviewer Flow

```
+--------------------------------------------------------------------+
|                    MULTI-REVIEWER FLOW                             |
+--------------------------------------------------------------------+
|                                                                    |
|   Author creates PR                                                |
|         |                                                          |
|         ▼                                                          |
|   +-------------+    +-------------+                               |
|   | Reviewer 1  |    | Reviewer 2  |                               |
|   | (Domain)    |    | (Security)  |                               |
|   +-------------+    +-------------+                               |
|         |                   |                                      |
|         ▼                   ▼                                      |
|   Request changes     Approve                                      |
|         |                                                          |
|         ▼                                                          |
|   Author fixes                                                     |
|         |                                                          |
|         ▼                                                          |
|   Re-review                                                        |
|         |                                                          |
|         ▼                                                          |
|   Both approve -> Merge                                             |
|                                                                    |
+--------------------------------------------------------------------+
```

---

## Sammanfattning

| Action | Command | Note |
|--------|---------|------|
| Create PR | `gh pr create` | Use `--draft` for WIP |
| List PRs | `gh pr list` | Filter with `--state` |
| Review | `gh pr review` | `--approve/--request-changes` |
| Merge | `gh pr merge` | `--squash/--merge/--rebase` |
| Checkout | `gh pr checkout 123` | Test locally |

---

## Nästa Steg

Pull Requests behärskade. Nästa: **Issues & Projects** — project management i GitHub.
''',
}

BLOCK_4_PART_1_NODES = [NODE_13_GITHUB_PLATFORM, NODE_14_PULL_REQUESTS]
