# =============================================================================
# BLOCK 2: BRANCHING PART 2 (Noder 7-8)
# =============================================================================

NODE_07_ADVANCED_WORKFLOWS = {
    "node_id": 7,
    "title": "Advanced Git Workflows",
    "slug": "advanced-git-workflows",
    "estimated_minutes": 65,
    "xp_reward": 165,
    "prerequisites": ["merge-rebase-mastery"],
    "content": '''
# Advanced Git Workflows

## Varför detta är kritiskt

> "Git's avancerade verktyg är skillnaden mellan timmar av manuellt arbete och sekunder av automatiserad elegans. Stash, worktrees och bisect är power user's hemliga vapen."

**Verkligheten:**
- Stash sparar arbete vid oväntade kontextbyten
- Worktrees möjliggör parallellt arbete utan overhead
- Bisect hittar buggar på minuter istället för timmar
- Submodules hanterar komplexa projektberoenden

---

## Git Stash Mastery

```
+-----------------------------------------------------------------------------+
|                            GIT STASH                                        |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Stash temporarily saves uncommitted changes                               |
|                                                                             |
|   STASH STACK:                                                              |
|   +---------------------------------------------------------------------+  |
|   |  stash@{0}  -►  Latest stash (most recent)                          |  |
|   |       |                                                             |  |
|   |  stash@{1}  -►  Previous stash                                      |  |
|   |       |                                                             |  |
|   |  stash@{2}  -►  Older stash                                         |  |
|   |       |                                                             |  |
|   |     ...                                                             |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
|   WHAT GETS STASHED:                                                        |
|   +-- Modified tracked files ✅                                             |
|   +-- Staged changes ✅                                                     |
|   +-- Untracked files ❌ (unless -u)                                        |
|   +-- Ignored files ❌ (unless -a)                                          |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Stash Operations

```bash
# Basic stash
git stash
git stash push  # Same as above

# Stash with message
git stash push -m "WIP: feature X implementation"

# Stash including untracked files
git stash -u
git stash --include-untracked

# Stash everything (including ignored)
git stash -a
git stash --all

# Stash specific files
git stash push -m "stash login" src/login.py src/auth.py

# Stash interactively
git stash -p  # Choose hunks to stash
```

### Managing Stashes

```bash
# List stashes
git stash list
# stash@{0}: On main: WIP: feature X
# stash@{1}: On develop: Bug fix attempt

# Show stash contents
git stash show              # Summary
git stash show -p           # Full diff
git stash show stash@{1}    # Specific stash

# Apply stash
git stash apply             # Apply latest, keep in stack
git stash apply stash@{2}   # Apply specific stash

# Pop stash (apply and delete)
git stash pop               # Apply and remove latest
git stash pop stash@{1}     # Apply and remove specific

# Drop stash
git stash drop              # Delete latest
git stash drop stash@{2}    # Delete specific

# Clear all stashes
git stash clear
```

### Advanced Stash Patterns

```bash
# Create branch from stash
git stash branch new-feature stash@{0}
# Creates branch, checks it out, applies stash

# Stash only staged changes
git stash --staged
git stash --keep-index  # Stash unstaged, keep staged

# Recover dropped stash
git fsck --unreachable | grep commit
git show <hash>  # Find your stash
git stash apply <hash>

# Stash with partial commit
git add -p                    # Stage some changes
git stash --keep-index        # Stash the rest
git commit -m "partial work"  # Commit staged
git stash pop                 # Get rest back
```

---

## Git Worktrees

```
+-----------------------------------------------------------------------------+
|                           GIT WORKTREES                                     |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Worktrees allow multiple working directories for ONE repository           |
|                                                                             |
|   TRADITIONAL:                       WITH WORKTREES:                        |
|   +-----------------+               +-----------------+                    |
|   |   myproject/    |               |   myproject/    | (main)             |
|   |   +-- .git/     |               |   +-- .git/     |                    |
|   |   +-- ...       |               |   +-- ...       |                    |
|   +-----------------+               |                 |                    |
|                                     |   ../myproject-feat/  | (feature)    |
|   Switch branches = lose context    |   +-- ...       |                    |
|                                     |                 |                    |
|                                     |   ../myproject-fix/   | (hotfix)     |
|                                     |   +-- ...       |                    |
|                                     +-----------------+                    |
|                                                                             |
|   BENEFITS:                                                                 |
|   +-- Work on multiple branches simultaneously                              |
|   +-- No stashing required                                                  |
|   +-- Keep long builds running                                              |
|   +-- Review PRs while working                                              |
|   +-- Shared .git saves disk space                                          |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Worktree Operations

```bash
# List existing worktrees
git worktree list
# /path/to/repo          abc1234 [main]
# /path/to/repo-feature  def5678 [feature]

# Add new worktree for existing branch
git worktree add ../my-project-develop develop

# Add worktree with new branch
git worktree add -b feature/auth ../my-project-auth main

# Add worktree in detached HEAD
git worktree add --detach ../my-project-test abc1234

# Remove worktree
cd /path/to/repo
git worktree remove ../my-project-feature

# Prune stale worktrees
git worktree prune
```

### Worktree Workflow

```bash
# Scenario: Working on feature, need to fix bug in main

# Current state: In feature branch
pwd  # /home/user/myproject (on feature/login)

# Create worktree for hotfix
git worktree add ../myproject-hotfix main
cd ../myproject-hotfix

# Fix the bug
git checkout -b hotfix/critical-bug
# ... make fixes ...
git commit -m "fix: critical bug"
git push -u origin hotfix/critical-bug

# Switch back to feature work
cd ../myproject
# Continue feature work, no stashing needed!

# After hotfix is merged, clean up
cd ../myproject
git worktree remove ../myproject-hotfix
```

### IDE Integration

```bash
# Open different worktree in new VS Code window
code ../myproject-feature

# Each worktree can have:
# - Own VS Code workspace settings
# - Own terminal sessions
# - Own debugger configurations

# .gitignore worktree-specific files
# In .git/info/exclude:
# .vscode/
# *.local
```

---

## Git Bisect

```
+-----------------------------------------------------------------------------+
|                            GIT BISECT                                       |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Binary search through history to find bug-introducing commit              |
|                                                                             |
|   CONCEPT:                                                                  |
|   +---------------------------------------------------------------------+  |
|   |                                                                     |  |
|   |   A---B---C---D---E---F---G---H---I---J                             |  |
|   |   ▲                               ▲                                 |  |
|   |   good                            bad                               |  |
|   |   (works)                         (broken)                          |  |
|   |                                                                     |  |
|   |   Step 1: Test E (middle)                                           |  |
|   |           Result: good                                              |  |
|   |                                                                     |  |
|   |   A---B---C---D---E---F---G---H---I---J                             |  |
|   |               ▲       ▲       ▲                                     |  |
|   |               good    test    bad                                   |  |
|   |                                                                     |  |
|   |   Step 2: Test G (middle of E-J)                                    |  |
|   |           Result: bad                                               |  |
|   |                                                                     |  |
|   |   Step 3: Test F (middle of E-G)                                    |  |
|   |           Result: good                                              |  |
|   |                                                                     |  |
|   |   FOUND: G is the first bad commit!                                 |  |
|   |                                                                     |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
|   With 1000 commits: ~10 tests needed (log₂ 1000 ≈ 10)                     |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Manual Bisect

```bash
# Start bisect session
git bisect start

# Mark current as bad
git bisect bad

# Mark known good commit
git bisect good v1.0.0  # or commit hash

# Git checks out middle commit
# Test your code manually, then:
git bisect good  # if working
git bisect bad   # if broken

# Repeat until found
# "abc1234 is the first bad commit"

# View bisect log
git bisect log

# Reset when done
git bisect reset
```

### Automated Bisect

```bash
# Create test script
cat > test.sh << 'EOF'
#!/bin/bash
npm test
# Exit 0 = good, Exit 1+ = bad
EOF
chmod +x test.sh

# Run automated bisect
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
git bisect run ./test.sh

# Script can be any command
git bisect run make test
git bisect run python -c "import mymodule; mymodule.test()"
git bisect run grep -q "expected_string" output.txt
```

### Bisect with Skip

```bash
# If a commit can't be tested (won't compile)
git bisect skip

# Skip range of commits
git bisect skip abc123..def456

# Bisect will work around skipped commits
```

---

## Submodules

```
+-----------------------------------------------------------------------------+
|                          GIT SUBMODULES                                     |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Include other Git repositories as subdirectories                          |
|                                                                             |
|   STRUCTURE:                                                                |
|   +---------------------------------------------------------------------+  |
|   |  main-project/                                                      |  |
|   |  +-- .git/                                                          |  |
|   |  +-- .gitmodules              # Submodule configuration             |  |
|   |  +-- src/                                                           |  |
|   |  +-- libs/                                                          |  |
|   |      +-- shared-utils/        # Submodule (another repo)            |  |
|   |      |   +-- (tracked at specific commit)                           |  |
|   |      +-- ui-components/       # Another submodule                   |  |
|   |          +-- (tracked at specific commit)                           |  |
|   +---------------------------------------------------------------------+  |
|                                                                             |
|   PROS:                              CONS:                                  |
|   +-- Share code between repos      +-- Complex workflow                   |
|   +-- Pin dependency versions       +-- Extra commands needed              |
|   +-- Separate access control       +-- Confusing for beginners            |
|   +-- Independent histories         +-- CI/CD complexity                   |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Submodule Operations

```bash
# Add submodule
git submodule add https://github.com/user/repo libs/shared

# Clone repo with submodules
git clone --recurse-submodules https://github.com/user/main-project

# Or after cloning:
git submodule init
git submodule update

# One command:
git submodule update --init --recursive

# Update submodule to latest
cd libs/shared
git checkout main
git pull
cd ..
git add libs/shared
git commit -m "Update shared lib"

# Update all submodules
git submodule update --remote

# Status
git submodule status
git submodule foreach git status
```

### .gitmodules File

```ini
# .gitmodules
[submodule "libs/shared"]
    path = libs/shared
    url = https://github.com/company/shared-utils
    branch = main

[submodule "libs/ui"]
    path = libs/ui
    url = git@github.com:company/ui-components.git
    branch = develop
```

---

## Git Hooks

```
+-----------------------------------------------------------------------------+
|                            GIT HOOKS                                        |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Hooks are scripts that run at specific Git events                         |
|                                                                             |
|   LOCATION: .git/hooks/ (local) or managed via tools                        |
|                                                                             |
|   CLIENT-SIDE HOOKS:                                                        |
|   +-- pre-commit       -> Before commit (lint, format)                       |
|   +-- prepare-commit-msg -> Edit commit message                              |
|   +-- commit-msg       -> Validate commit message                            |
|   +-- post-commit      -> After commit (notify)                              |
|   +-- pre-push         -> Before push (test)                                 |
|   +-- post-checkout    -> After checkout (dependencies)                      |
|                                                                             |
|   SERVER-SIDE HOOKS:                                                        |
|   +-- pre-receive      -> Before accepting push                              |
|   +-- update           -> Per-branch validation                              |
|   +-- post-receive     -> After accepting (deploy, notify)                   |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Pre-commit Hook Example

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run linter
echo "Running linter..."
npm run lint
if [ $? -ne 0 ]; then
    echo "Lint failed. Commit aborted."
    exit 1
fi

# Run tests
echo "Running tests..."
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi

# Check for secrets
if grep -r "API_KEY\|SECRET\|PASSWORD" --include="*.py" --include="*.js" .; then
    echo "Potential secret found. Commit aborted."
    exit 1
fi

echo "All checks passed!"
exit 0
```

### Using Husky (Node.js)

```bash
# Install husky
npm install husky --save-dev
npx husky install

# Add pre-commit hook
npx husky add .husky/pre-commit "npm run lint-staged"

# .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npm run lint-staged
```

### Using pre-commit (Python)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.280
    hooks:
      - id: ruff
```

```bash
# Install
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

---

## Sammanfattning

| Tool | Use Case | Key Command |
|------|----------|-------------|
| Stash | Temporary save | `git stash` |
| Worktrees | Parallel branches | `git worktree add` |
| Bisect | Find bugs | `git bisect start` |
| Submodules | Shared repos | `git submodule add` |
| Hooks | Automation | `.git/hooks/` |

---

## Nästa Steg

Advanced workflows mastered. Nästa: **Git Large Files & Performance** — LFS, shallow clones, och repo optimization.
''',
}

NODE_08_LARGE_FILES_PERFORMANCE = {
    "node_id": 8,
    "title": "Git Large Files & Performance",
    "slug": "git-large-files-performance",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": ["advanced-git-workflows"],
    "content": '''
# Git Large Files & Performance

## Varför detta är kritiskt

> "Git skapades för källkod, inte för gigabyte av binärfiler. Utan rätt strategi för stora filer blir repos omöjliga att klona, pushes tar timmar, och team-produktivitet kollapsar."

**Verkligheten:**
- 100MB+ repo tar minuter att klona
- Binärfiler multiplicerar repo-storlek vid varje ändring
- CI/CD väntetider ökar exponentiellt
- Enterprise repos kan nå 100GB+ utan optimering

---

## Repository Size Analysis

```
+-----------------------------------------------------------------------------+
|                     REPOSITORY SIZE BREAKDOWN                               |
+-----------------------------------------------------------------------------+
|                                                                             |
|   HEALTHY REPO:                    BLOATED REPO:                            |
|   +---------------------+         +---------------------+                  |
|   |  .git/  50 MB       |         |  .git/  5 GB        | <- Problem!       |
|   |  +-- objects 45 MB  |         |  +-- objects 4.8 GB |                  |
|   |  +-- refs 5 MB      |         |  +-- pack 4.7 GB    |                  |
|   |  src/   10 MB       |         |  src/   100 MB      |                  |
|   |  Total: 60 MB       |         |  assets/ 2 GB       | <- Binary files   |
|   |                     |         |  Total: 7.1 GB      |                  |
|   +---------------------+         +---------------------+                  |
|                                                                             |
|   COMMON BLOAT CAUSES:                                                      |
|   +-- Large binary files committed                                          |
|   +-- Secrets/credentials in history                                        |
|   +-- Generated files (node_modules, build/)                                |
|   +-- Large media assets (images, videos)                                   |
|   +-- Database dumps                                                        |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Analyzing Repository Size

```bash
# Total repo size
du -sh .

# .git directory size
du -sh .git

# Detailed .git breakdown
du -sh .git/*

# Count objects
git count-objects -v

# Find large files in history
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  sed -n 's/^blob //p' | \
  sort -rnk2 | \
  head -20

# Alternative: git-sizer tool
brew install git-sizer
git-sizer --verbose
```

### Find Large Files Script

```bash
#!/bin/bash
# find-large-files.sh

echo "Top 20 largest files in repo history:"
echo "======================================"

git rev-list --objects --all | \
while read sha path; do
    if [ -n "$path" ]; then
        echo "$sha $path"
    fi
done | \
while read sha path; do
    size=$(git cat-file -s "$sha" 2>/dev/null)
    if [ -n "$size" ]; then
        echo "$size $sha $path"
    fi
done | \
sort -rn | \
head -20 | \
while read size sha path; do
    # Convert to MB
    mb=$(echo "scale=2; $size/1024/1024" | bc)
    printf "%8.2f MB %s %s\n" "$mb" "$sha" "$path"
done
```

---

## Git LFS (Large File Storage)

```
+-----------------------------------------------------------------------------+
|                            GIT LFS                                          |
+-----------------------------------------------------------------------------+
|                                                                             |
|   LFS stores large files on a separate server                               |
|                                                                             |
|   WITHOUT LFS:                          WITH LFS:                           |
|   +-------------------+               +-------------------+                |
|   |  Git Repository   |               |  Git Repository   |                |
|   |  +-------------+  |               |  +-------------+  |                |
|   |  | logo.png    |  |               |  | pointer.txt |  | (200 bytes)    |
|   |  | (5 MB)      |  |               |  | -> LFS ref   |  |                |
|   |  +-------------+  |               |  +-------------+  |                |
|   |  +-------------+  |               +---------+---------+                |
|   |  | logo-v2.png |  |                         |                          |
|   |  | (5 MB)      |  |                         ▼                          |
|   |  +-------------+  |               +-------------------+                |
|   |  Total: 10 MB     |               |    LFS Server     |                |
|   +-------------------+               |  +-------------+  |                |
|                                       |  | logo.png    |  |                |
|   Each version stored                 |  | (5 MB)      |  |                |
|   in .git/objects                     |  +-------------+  |                |
|                                       |  Only latest      |                |
|                                       |  downloaded       |                |
|                                       +-------------------+                |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Setting Up LFS

```bash
# Install Git LFS
# macOS
brew install git-lfs

# Ubuntu
apt install git-lfs

# Windows (included with Git for Windows)

# Initialize LFS in repo
git lfs install

# Track file types
git lfs track "*.psd"
git lfs track "*.zip"
git lfs track "*.mp4"
git lfs track "assets/**"

# This creates/updates .gitattributes
cat .gitattributes
# *.psd filter=lfs diff=lfs merge=lfs -text
# *.zip filter=lfs diff=lfs merge=lfs -text

# Add .gitattributes to repo
git add .gitattributes
git commit -m "Configure Git LFS"

# Now add large files normally
git add assets/video.mp4
git commit -m "Add video"
git push
```

### LFS Operations

```bash
# Check LFS status
git lfs status

# List tracked files
git lfs ls-files

# List tracked patterns
git lfs track

# Untrack a pattern
git lfs untrack "*.mp4"

# Pull LFS files
git lfs pull

# Fetch specific files
git lfs fetch --include="*.psd"

# Prune old LFS files
git lfs prune

# Migrate existing files to LFS
git lfs migrate import --include="*.psd" --everything
```

### LFS in CI/CD

```yaml
# GitHub Actions with LFS
name: Build
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true  # Enable LFS

      # Or fetch only needed files
      - uses: actions/checkout@v4
        with:
          lfs: false
      - run: |
          git lfs fetch --include="required-assets/*"
          git lfs checkout
```

---

## Shallow Clones and Partial Clones

### Shallow Clone

```bash
# Clone with limited history
git clone --depth 1 https://github.com/user/repo
# Only latest commit, no history

# Clone with last N commits
git clone --depth 100 https://github.com/user/repo

# Shallow since date
git clone --shallow-since="2023-01-01" https://github.com/user/repo

# Deepen shallow clone later
git fetch --deepen=50
git fetch --unshallow  # Get full history

# Shallow clone single branch
git clone --depth 1 --branch main --single-branch https://github.com/user/repo
```

### Partial Clone (Git 2.22+)

```bash
# Blobless clone (best for CI)
git clone --filter=blob:none https://github.com/user/repo
# Clones commits and trees, fetches blobs on demand

# Treeless clone (smallest initial)
git clone --filter=tree:0 https://github.com/user/repo
# Only commits initially, trees and blobs on demand

# Size limit filter
git clone --filter=blob:limit=1m https://github.com/user/repo
# Exclude blobs larger than 1MB

# Sparse checkout with partial clone
git clone --filter=blob:none --sparse https://github.com/user/repo
cd repo
git sparse-checkout set src/frontend
```

### Sparse Checkout

```bash
# Enable sparse checkout
git sparse-checkout init --cone

# Check out only specific directories
git sparse-checkout set src/backend docs

# Add more directories
git sparse-checkout add tests

# View current sparse config
git sparse-checkout list

# Disable (checkout everything)
git sparse-checkout disable
```

---

## Repository Cleanup

### Remove Large Files from History

```bash
# Using git-filter-repo (recommended)
pip install git-filter-repo

# Remove specific file from all history
git filter-repo --path large-file.zip --invert-paths

# Remove files by size
git filter-repo --strip-blobs-bigger-than 10M

# Remove directory from history
git filter-repo --path build/ --invert-paths

# Remove sensitive data
git filter-repo --replace-text expressions.txt
# expressions.txt: literal:password123==>REMOVED
```

### BFG Repo Cleaner (Alternative)

```bash
# Download BFG
# https://rtyley.github.io/bfg-repo-cleaner/

# Remove files bigger than 100M
java -jar bfg.jar --strip-blobs-bigger-than 100M repo.git

# Remove specific files
java -jar bfg.jar --delete-files *.mp4 repo.git

# Remove passwords
java -jar bfg.jar --replace-text passwords.txt repo.git

# Clean up
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### Garbage Collection

```bash
# Standard GC
git gc

# Aggressive GC (slower, better compression)
git gc --aggressive

# Auto GC (runs if needed)
git gc --auto

# Manual cleanup
git reflog expire --expire=now --all
git gc --prune=now

# Verify integrity after cleanup
git fsck
```

---

## Performance Optimization

```
+-----------------------------------------------------------------------------+
|                     PERFORMANCE OPTIMIZATION                                |
+-----------------------------------------------------------------------------+
|                                                                             |
|   Configuration for large repos:                                            |
|                                                                             |
|   # .gitconfig                                                              |
|   [core]                                                                    |
|       fsmonitor = true          # Filesystem monitor (huge speedup)         |
|       untrackedCache = true     # Cache untracked files                     |
|       preloadIndex = true       # Parallel index loading                    |
|       commitGraph = true        # Commit graph for faster logs              |
|                                                                             |
|   [gc]                                                                      |
|       auto = 256                # Trigger GC less often                     |
|       writeCommitGraph = true   # Maintain commit graph                     |
|                                                                             |
|   [pack]                                                                    |
|       threads = 0               # Use all CPUs                              |
|       windowMemory = 256m       # More memory for delta                     |
|                                                                             |
|   [fetch]                                                                   |
|       writeCommitGraph = true   # Update graph on fetch                     |
|       parallel = 4              # Parallel fetches                          |
|                                                                             |
|   [index]                                                                   |
|       version = 4               # Newer index format                        |
|                                                                             |
+-----------------------------------------------------------------------------+
```

### Commit Graph

```bash
# Generate commit graph
git commit-graph write --reachable

# Verify commit graph
git commit-graph verify

# Write on fetch (recommended)
git config --global fetch.writeCommitGraph true

# Benefits:
# - Faster git log
# - Faster git merge-base
# - Faster reachability queries
```

### Filesystem Monitor

```bash
# Enable fsmonitor (requires watchman)
brew install watchman
git config core.fsmonitor true

# Or use built-in fsmonitor (Git 2.36+)
git config core.fsmonitor true
git config core.untrackedCache true

# Test impact
time git status  # Before
git config core.fsmonitor true
time git status  # After (should be faster)
```

---

## Best Practices Summary

| Strategy | When to Use | Impact |
|----------|-------------|--------|
| Git LFS | Binary files > 1MB | Repo size, clone time |
| Shallow clone | CI/CD, quick checkouts | Clone time |
| Partial clone | Monorepos, large repos | Clone time, disk space |
| Sparse checkout | Only need subset | Disk space |
| git-filter-repo | Remove history bloat | Repo size |
| fsmonitor | Large working directories | git status speed |
| Commit graph | Repos with long history | Log/merge speed |

---

## Sammanfattning

| Problem | Solution | Command |
|---------|----------|---------|
| Large binaries | Git LFS | `git lfs track` |
| Slow clone | Shallow clone | `git clone --depth 1` |
| Huge history | Partial clone | `--filter=blob:none` |
| Bloated .git | filter-repo | `git filter-repo` |
| Slow git status | fsmonitor | `core.fsmonitor = true` |

---

## Nästa Steg

Large files & performance mastered. Nästa: **GitHub Platform Deep Dive** — PRs, Actions, och advanced collaboration.
''',
}

BLOCK_2_PART_2_NODES = [NODE_07_ADVANCED_WORKFLOWS, NODE_08_LARGE_FILES_PERFORMANCE]
