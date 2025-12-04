# =============================================================================
# BLOCK 2: BRANCHING STRATEGIES (Noder 5-6)
# =============================================================================

NODE_05_BRANCHING_STRATEGIES = {
    "node_id": 5,
    "title": "Branching Strategies",
    "slug": "branching-strategies",
    "estimated_minutes": 65,
    "xp_reward": 160,
    "prerequisites": ["git-internals-objects"],
    "content": '''
# Branching Strategies

## Varför detta är kritiskt

> "Din branching-strategi är er utvecklingsprocess i kodform. Fel strategi saboterar produktivitet, release-cykler och teamsamarbete. Rätt strategi accelererar leverans och kvalitet."

**Verkligheten:**
- 90% av team failures i Git beror på dålig branching-strategi
- Rätt strategi kan halvera tid-till-produktion
- Enterprise teams kräver dokumenterad workflow
- CI/CD integration kräver förutsägbar branching

---

## Branching Strategy Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BRANCHING STRATEGY COMPARISON                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  GITFLOW                                                            │  │
│   │  ─────────────────────────────────────────────────────────────────  │  │
│   │  • Best for: Scheduled releases, versioned products                 │  │
│   │  • Branches: main, develop, feature/*, release/*, hotfix/*          │  │
│   │  • Complexity: High                                                 │  │
│   │  • Release frequency: Weekly to monthly                             │  │
│   │                                                                     │  │
│   │  main      ●───────────●────────────●──────────────●               │  │
│   │             \\         /│\\          /               /               │  │
│   │  hotfix/*    \\       / │ \\        /               /                │  │
│   │               \\     /  │  \\      /               /                 │  │
│   │  release/*    ●───●    │   ●────●               /                  │  │
│   │              /         │        \\             /                    │  │
│   │  develop   ●───●───●───●────●────●───●───●───●                     │  │
│   │           / \\       \\      /       \\    /                         │  │
│   │  feature/*  ●───●    ●────●         ●──●                           │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  TRUNK-BASED DEVELOPMENT                                            │  │
│   │  ─────────────────────────────────────────────────────────────────  │  │
│   │  • Best for: Continuous deployment, mature CI/CD                    │  │
│   │  • Branches: main, short-lived feature branches                     │  │
│   │  • Complexity: Low                                                  │  │
│   │  • Release frequency: Multiple per day                              │  │
│   │                                                                     │  │
│   │  main     ●───●───●───●───●───●───●───●───●───●                     │  │
│   │          /│\\  │  / \\ /│\\  │                                        │  │
│   │  feature  ●   ● ●   ● ● ●  ●                                        │  │
│   │        (< 2 days old)                                               │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  GITHUB FLOW                                                        │  │
│   │  ─────────────────────────────────────────────────────────────────  │  │
│   │  • Best for: Web apps, continuous delivery                          │  │
│   │  • Branches: main, feature/*                                        │  │
│   │  • Complexity: Very low                                             │  │
│   │  • Release frequency: On every merge                                │  │
│   │                                                                     │  │
│   │  main     ●───●───────●───────●───────●───────●                     │  │
│   │          / \\       / \\     / \\     / \\                             │  │
│   │  feature  ●───●───●   ●───●   ●───●   ●───●                         │  │
│   │           PR review   Deploy  Deploy  Deploy                        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  GITLAB FLOW                                                        │  │
│   │  ─────────────────────────────────────────────────────────────────  │  │
│   │  • Best for: Multiple environments, staged releases                 │  │
│   │  • Branches: main, environment branches, feature/*                  │  │
│   │  • Complexity: Medium                                               │  │
│   │  • Release frequency: Daily to weekly                               │  │
│   │                                                                     │  │
│   │  production   ●─────────────●─────────────●                         │  │
│   │              ↑              ↑              ↑                         │  │
│   │  staging     ●───────●─────●───────●─────●                         │  │
│   │             ↑        ↑            ↑                                 │  │
│   │  main      ●───●───●───●───●───●───●───●                           │  │
│   │           / \\    / \\      / \\                                       │  │
│   │  feature   ●───●   ●───●    ●───●                                   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## GitFlow Implementation

### Setup

```bash
# Install git-flow CLI (optional but helpful)
# macOS
brew install git-flow

# Ubuntu
apt install git-flow

# Initialize git-flow
git flow init

# Branch naming convention:
# Production releases: main
# Development: develop
# Features: feature/*
# Releases: release/*
# Hotfixes: hotfix/*
```

### Feature Development

```bash
# Start a feature
git flow feature start user-authentication
# Creates: feature/user-authentication from develop

# Work on feature
git add .
git commit -m "feat: add login form"
git commit -m "feat: add authentication logic"

# Finish feature (merges to develop)
git flow feature finish user-authentication

# Without git-flow:
git checkout develop
git checkout -b feature/user-authentication
# ... work ...
git checkout develop
git merge --no-ff feature/user-authentication
git branch -d feature/user-authentication
```

### Release Process

```bash
# Start release
git flow release start 1.0.0
# Creates: release/1.0.0 from develop

# Bump version, update changelog
echo "1.0.0" > VERSION
git add VERSION
git commit -m "chore: bump version to 1.0.0"

# Finish release
git flow release finish 1.0.0
# Merges to main AND develop
# Creates tag v1.0.0

# Without git-flow:
git checkout develop
git checkout -b release/1.0.0
# ... prepare release ...
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"
git checkout develop
git merge --no-ff release/1.0.0
git branch -d release/1.0.0
```

### Hotfix Process

```bash
# Emergency fix from production
git flow hotfix start 1.0.1
# Creates: hotfix/1.0.1 from main

# Fix the bug
git add .
git commit -m "fix: critical security vulnerability"

# Finish hotfix
git flow hotfix finish 1.0.1
# Merges to main AND develop
# Creates tag v1.0.1
```

---

## Trunk-Based Development

### Core Principles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TRUNK-BASED DEVELOPMENT RULES                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. SMALL COMMITS                                                          │
│      • Each commit should be deployable                                     │
│      • Max 200 lines changed                                                │
│      • Atomic, focused changes                                              │
│                                                                             │
│   2. SHORT-LIVED BRANCHES                                                   │
│      • Maximum 2 days                                                       │
│      • Ideally < 1 day                                                      │
│      • Merge frequently                                                     │
│                                                                             │
│   3. FEATURE FLAGS                                                          │
│      • Deploy incomplete features                                           │
│      • Toggle visibility                                                    │
│      • Gradual rollout                                                      │
│                                                                             │
│   4. CONTINUOUS INTEGRATION                                                 │
│      • Run tests on every commit                                            │
│      • Block broken builds                                                  │
│      • Fast feedback (< 10 min)                                             │
│                                                                             │
│   5. MAIN IS ALWAYS DEPLOYABLE                                              │
│      • Protected branch                                                     │
│      • Required CI checks                                                   │
│      • No direct commits                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Trunk-Based Workflow

```bash
# 1. Start from latest main
git checkout main
git pull --rebase

# 2. Create short-lived branch
git checkout -b add-user-api

# 3. Make small, focused changes
git add .
git commit -m "feat: add User model"
# Commit should be deployable!

# 4. Sync with main frequently
git fetch origin main
git rebase origin/main

# 5. Push and create PR
git push -u origin add-user-api

# 6. Quick review and merge (same day)
# After approval:
git checkout main
git pull
git merge add-user-api
git push
git branch -d add-user-api
```

### Feature Flags Pattern

```python
# Python example with feature flags
from feature_flags import get_flag

def get_user_profile(user_id):
    user = User.get(user_id)

    # New feature behind flag
    if get_flag("new_profile_layout"):
        return render_new_profile(user)

    # Existing behavior
    return render_profile(user)


# Feature flag configuration (environment-based)
FEATURE_FLAGS = {
    "new_profile_layout": {
        "enabled": True,
        "rollout_percentage": 25,  # 25% of users
        "allowed_users": ["beta_testers"],
    }
}
```

```javascript
// React component with feature flag
import { useFeatureFlag } from './feature-flags';

function Dashboard() {
  const showNewDashboard = useFeatureFlag('new_dashboard');

  if (showNewDashboard) {
    return <NewDashboard />;
  }

  return <LegacyDashboard />;
}
```

---

## GitHub Flow Implementation

### The Simplest Production Workflow

```bash
# 1. Create branch from main
git checkout main
git pull
git checkout -b feature/add-search

# 2. Develop and commit
git add .
git commit -m "feat: add search endpoint"
git commit -m "feat: add search UI"
git commit -m "test: add search tests"

# 3. Push branch
git push -u origin feature/add-search

# 4. Open Pull Request on GitHub
# - Description with screenshots
# - Request reviewers
# - Link to issue

# 5. Discuss and review
# - Address feedback
# - Push additional commits

# 6. Deploy to production (from branch!)
# - Verify in production

# 7. Merge to main
# - Squash or merge commit
# - Delete branch
```

### Branch Protection Rules

```yaml
# GitHub branch protection (via API or UI)
protection_rules:
  main:
    required_status_checks:
      strict: true  # Branch must be up to date
      contexts:
        - "ci/tests"
        - "ci/lint"
        - "ci/build"
    required_pull_request_reviews:
      dismiss_stale_reviews: true
      require_code_owner_reviews: true
      required_approving_review_count: 2
    restrictions:
      users: []
      teams: ["core-team"]
    enforce_admins: true
    required_linear_history: false
    allow_force_pushes: false
    allow_deletions: false
```

---

## Release Management

### Semantic Versioning

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      SEMANTIC VERSIONING (SemVer)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   VERSION FORMAT: MAJOR.MINOR.PATCH                                         │
│                                                                             │
│   2.1.3                                                                     │
│   │ │ └── PATCH: Bug fixes, security patches                               │
│   │ │            Backward compatible                                        │
│   │ │                                                                       │
│   │ └──── MINOR: New features                                               │
│   │              Backward compatible                                        │
│   │                                                                         │
│   └────── MAJOR: Breaking changes                                           │
│                  May require migration                                      │
│                                                                             │
│   EXAMPLES:                                                                 │
│   1.0.0 → 1.0.1  Bug fix                                                    │
│   1.0.1 → 1.1.0  New feature added                                          │
│   1.1.0 → 2.0.0  Breaking API change                                        │
│                                                                             │
│   PRE-RELEASE VERSIONS:                                                     │
│   1.0.0-alpha.1   → Early testing                                           │
│   1.0.0-beta.1    → Feature complete                                        │
│   1.0.0-rc.1      → Release candidate                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Automated Versioning

```bash
# Using standard-version
npm install -g standard-version

# Automatic version bump based on commits
standard-version
# Reads commit messages, bumps version, generates CHANGELOG

# Commit message format (Conventional Commits)
# feat: new feature → MINOR
# fix: bug fix → PATCH
# BREAKING CHANGE: → MAJOR

# Example commits:
git commit -m "feat: add user search API"
git commit -m "fix: handle null user case"
git commit -m "feat!: change auth flow"  # Breaking change
```

### Changelog Generation

```bash
# Auto-generate CHANGELOG.md
standard-version --release-as minor

# Output in CHANGELOG.md:
# ## [1.1.0] - 2024-01-15
# ### Features
# * add user search API (abc1234)
#
# ### Bug Fixes
# * handle null user case (def5678)
```

---

## Strategy Selection Guide

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHOOSE YOUR BRANCHING STRATEGY                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ASK YOURSELF:                                                             │
│                                                                             │
│   1. How often do you deploy?                                               │
│      □ Multiple times per day → Trunk-Based                                 │
│      □ Weekly/Monthly → GitFlow                                             │
│      □ On every merge → GitHub Flow                                         │
│                                                                             │
│   2. Do you support multiple versions?                                      │
│      □ Yes (v1.x, v2.x in parallel) → GitFlow                               │
│      □ No (always latest) → GitHub/Trunk                                    │
│                                                                             │
│   3. Team maturity with CI/CD?                                              │
│      □ High (comprehensive tests) → Trunk-Based                             │
│      □ Medium → GitHub Flow                                                 │
│      □ Low → GitFlow (more gates)                                           │
│                                                                             │
│   4. Release approval process?                                              │
│      □ None (auto-deploy) → Trunk-Based                                     │
│      □ Light (PR approval) → GitHub Flow                                    │
│      □ Heavy (release committee) → GitFlow                                  │
│                                                                             │
│   RECOMMENDATIONS BY PRODUCT TYPE:                                          │
│   ├── Web SaaS → GitHub Flow or Trunk-Based                                 │
│   ├── Mobile App (App Store) → GitFlow                                      │
│   ├── Open Source Library → GitFlow                                         │
│   ├── Internal Tools → GitHub Flow                                          │
│   └── Microservices → Trunk-Based per service                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Sammanfattning

| Strategy | Best For | Complexity | Release Speed |
|----------|----------|------------|---------------|
| GitFlow | Versioned products | High | Slow |
| Trunk-Based | CD/CD mature teams | Low | Fast |
| GitHub Flow | Web apps | Very Low | Medium |
| GitLab Flow | Multi-environment | Medium | Medium |

---

## Nästa Steg

Branching strategies mastered. Nästa: **Merge & Rebase Mastery** — konflikthantering och historik-manipulation.
''',
}

NODE_06_MERGE_REBASE = {
    "node_id": 6,
    "title": "Merge & Rebase Mastery",
    "slug": "merge-rebase-mastery",
    "estimated_minutes": 70,
    "xp_reward": 175,
    "prerequisites": ["branching-strategies"],
    "content": '''
# Merge & Rebase Mastery

## Varför detta är kritiskt

> "Merge och Rebase är Git's mest missförstådda kommandon. Felaktig användning skapar röriga historiker, förlorade commits och frustrerade team. Rätt användning ger kristallklar historik."

**Verkligheten:**
- Merge vs Rebase-debatten har delat teams i årtionden
- Fel val kan bryta CI/CD pipelines
- `--force` pushes har förstört produktionsbrancher
- Conflict resolution är en kritisk DevOps-skill

---

## Merge vs Rebase Fundamentals

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MERGE vs REBASE                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   INITIAL STATE:                                                            │
│                                                                             │
│   main:    A───B───C                                                        │
│                 \\                                                            │
│   feature:      D───E                                                       │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────    │
│                                                                             │
│   AFTER MERGE:                              AFTER REBASE:                   │
│                                                                             │
│   main:    A───B───C───M                    main:    A───B───C              │
│                 \\     /                                      \\              │
│   feature:      D───E                       feature:          D'──E'        │
│                                                                             │
│   • Creates merge commit (M)                • Rewrites history              │
│   • Preserves branch history                • Creates new commits (D', E')  │
│   • Non-destructive                         • Linear history                │
│   • Shows when work diverged                • Cleaner, but alters history   │
│                                                                             │
│   USE MERGE WHEN:                           USE REBASE WHEN:                │
│   ├── Public/shared branches                ├── Local/private branches      │
│   ├── Want to preserve history              ├── Want clean linear history   │
│   ├── Working with others' code             ├── Before pushing feature      │
│   └── Release branches                      └── Updating feature from main  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Merge Strategies Deep Dive

### Fast-Forward Merge

```bash
# Scenario: main hasn't changed since feature branched
# main:    A───B
#               \\
# feature:      C───D

git checkout main
git merge feature
# Result: A───B───C───D (no merge commit)

# Force merge commit anyway
git merge --no-ff feature
# Result: A───B───────M
#               \\     /
#                C───D
```

### Three-Way Merge

```bash
# Scenario: main has diverged
# main:    A───B───E
#               \\
# feature:      C───D

git checkout main
git merge feature

# Automatic 3-way merge
# Result: A───B───E───M
#               \\     /
#                C───D

# M contains changes from both branches
```

### Merge Strategies

```bash
# Default: recursive (best for most cases)
git merge feature

# Ours strategy (keep our version on conflicts)
git merge -s ours feature

# Resolve strategy (older, simpler)
git merge -s resolve feature

# Octopus (merge multiple branches)
git merge feature1 feature2 feature3

# Subtree (for subprojects)
git merge -s subtree feature
```

### Merge Options

```bash
# Don't auto-commit (review before committing)
git merge --no-commit feature

# Squash all commits into one
git merge --squash feature
git commit -m "feat: add feature X"
# No merge commit, just one new commit

# Abort in-progress merge
git merge --abort

# Continue after resolving conflicts
git merge --continue
```

---

## Rebase Fundamentals

### Basic Rebase

```bash
# Update feature branch with main changes
git checkout feature
git rebase main

# What happens:
# 1. Saves feature commits temporarily
# 2. Resets feature to main
# 3. Replays feature commits on top

# Before:
# main:    A───B───C
#               \\
# feature:      D───E

# After:
# main:    A───B───C
#                   \\
# feature:          D'──E'
```

### Interactive Rebase (The Power Tool)

```bash
# Rebase last 5 commits interactively
git rebase -i HEAD~5

# Or from a base commit
git rebase -i main

# Editor opens with:
pick abc1234 First commit message
pick def5678 Second commit message
pick 789abcd Third commit message
pick bcdef01 Fourth commit message
pick cdef012 Fifth commit message

# Commands:
# p, pick = use commit
# r, reword = use commit, but edit message
# e, edit = use commit, but stop for amending
# s, squash = meld into previous commit
# f, fixup = like squash, but discard message
# d, drop = remove commit
# x, exec = run command
```

### Interactive Rebase Examples

```bash
# Squash multiple commits
git rebase -i HEAD~4

# Change to:
pick abc1234 feat: start user feature
squash def5678 WIP: more work
squash 789abcd fix typo
squash bcdef01 cleanup

# Result: One clean commit with combined changes

# Reorder commits
git rebase -i HEAD~3
# Rearrange lines in editor

# Split a commit
git rebase -i HEAD~2
# Change 'pick' to 'edit'
# When stopped:
git reset HEAD~
git add file1.py
git commit -m "Part 1"
git add file2.py
git commit -m "Part 2"
git rebase --continue
```

---

## Conflict Resolution

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CONFLICT RESOLUTION WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. IDENTIFY CONFLICTS                                                     │
│      git status                                                             │
│      # both modified: src/app.py                                            │
│                                                                             │
│   2. UNDERSTAND THE CONFLICT                                                │
│      <<<<<<< HEAD                                                           │
│      current_value = "from main"                                            │
│      =======                                                                │
│      current_value = "from feature"                                         │
│      >>>>>>> feature                                                        │
│                                                                             │
│   3. RESOLVE OPTIONS                                                        │
│      a) Manual edit (most common)                                           │
│      b) Accept ours:   git checkout --ours file.py                          │
│      c) Accept theirs: git checkout --theirs file.py                        │
│      d) Use merge tool: git mergetool                                       │
│                                                                             │
│   4. MARK RESOLVED                                                          │
│      git add src/app.py                                                     │
│                                                                             │
│   5. CONTINUE                                                               │
│      git merge --continue   # or                                            │
│      git rebase --continue                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Conflict Resolution Tools

```bash
# Configure merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd \
  'code --wait --merge $REMOTE $LOCAL $BASE $MERGED'

# Launch merge tool
git mergetool

# For complex conflicts, use 3-way diff
git config --global merge.conflictstyle diff3

# Conflict now shows:
<<<<<<< HEAD
current code
||||||| common ancestor
original code
=======
incoming code
>>>>>>> feature

# Abort if overwhelmed
git merge --abort
git rebase --abort
```

### Rerere (Reuse Recorded Resolution)

```bash
# Enable rerere
git config --global rerere.enabled true

# How it works:
# 1. First conflict: Resolve manually
# 2. Git records the resolution
# 3. Same conflict later: Auto-resolves!

# View recorded resolutions
ls .git/rr-cache/

# Forget a resolution
git rerere forget <file>

# Train rerere from history
git rerere-train.sh main feature
```

---

## Advanced Rebase Techniques

### Autosquash

```bash
# Create fixup commits
git commit --fixup abc1234  # Creates: fixup! Original message
git commit --squash def5678 # Creates: squash! Original message

# Autosquash during rebase
git rebase -i --autosquash main

# Enable by default
git config --global rebase.autoSquash true
```

### Rebase Onto

```bash
# Scenario: Move feature to different base
# Before:
# main:      A───B───C───D
#                 \\
# old-base:       X───Y
#                      \\
# feature:              E───F

# Move feature from old-base to main
git rebase --onto main old-base feature

# After:
# main:      A───B───C───D
#                         \\
# feature:                 E'──F'
```

### Preserving Merge Commits

```bash
# Rebase with merge commits
git rebase --rebase-merges main

# Recreates merge commits in rebased history
# Useful for complex branch structures
```

---

## Cherry-Pick

```bash
# Apply specific commits to current branch
git cherry-pick abc1234

# Cherry-pick range
git cherry-pick abc1234..def5678

# Cherry-pick without committing
git cherry-pick -n abc1234

# Continue after conflict
git cherry-pick --continue

# Abort
git cherry-pick --abort

# Common use cases:
# 1. Backport fixes to release branch
# 2. Extract single commit from feature
# 3. Rescue commits from abandoned branch
```

---

## The Golden Rules

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GOLDEN RULES OF REBASE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ⚠️  NEVER REBASE PUBLIC/SHARED BRANCHES                                   │
│                                                                             │
│   ✅ SAFE:                                                                   │
│   git checkout my-feature                                                   │
│   git rebase main                      # Rebase MY branch onto main         │
│   git push --force-with-lease          # Force push MY branch               │
│                                                                             │
│   ❌ DANGEROUS:                                                              │
│   git checkout main                                                         │
│   git rebase feature                   # DON'T rebase shared branches!      │
│   git push --force                     # This breaks everyone's repo        │
│                                                                             │
│   RECOVERY FROM BAD REBASE:                                                 │
│   git reflog                           # Find pre-rebase state              │
│   git reset --hard HEAD@{n}            # Reset to that state                │
│                                                                             │
│   SAFE FORCE PUSH:                                                          │
│   git push --force-with-lease          # Fails if remote changed            │
│   git push --force-with-lease=origin/my-feature                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Team Workflow Recommendations

```bash
# Recommended workflow:
# 1. Create feature branch
git checkout -b feature/xyz main

# 2. Work on feature
git commit -m "feat: add X"
git commit -m "feat: add Y"

# 3. Before PR: clean up history
git fetch origin main
git rebase -i origin/main
# Squash WIP commits, fix messages

# 4. Rebase onto latest main
git rebase origin/main

# 5. Push (force if rebased)
git push --force-with-lease

# 6. PR review → Merge to main
# Use squash merge or merge commit (team decision)
```

---

## Sammanfattning

| Operation | Use When | Caution |
|-----------|----------|---------|
| Merge | Combining public branches | Creates merge commits |
| Fast-forward | Simple updates | May hide branch history |
| Rebase | Cleaning feature branch | Never on shared branches |
| Interactive Rebase | Editing local history | Rewrites commits |
| Cherry-pick | Extracting specific commits | May create duplicates |

---

## Nästa Steg

Merge & Rebase mastered. Nästa: **Advanced Git Workflows** — stash, worktrees, och bisect.
''',
}

BLOCK_2_PART_1_NODES = [NODE_05_BRANCHING_STRATEGIES, NODE_06_MERGE_REBASE]
