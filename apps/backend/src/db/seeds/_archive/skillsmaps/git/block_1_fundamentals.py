# =============================================================================
# BLOCK 1: GIT FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_GIT_INTRODUCTION = {
    "node_id": 1,
    "title": "Git Introduction",
    "slug": "git-introduction",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [],
    "content": r'''
# Git Introduction

## Varför detta är kritiskt

> "Utan Git finns ingen modern mjukvaruutveckling. Varje kodbas, varje team, varje deploy förlitar sig på versionshantering. Git är inte ett verktyg — det är fundamentet."

**Verkligheten:**
- 95%+ av alla utvecklingsprojekt använder Git
- GitHub har 100+ miljoner repositories
- Varje CI/CD pipeline börjar med `git`
- "Git history" är ditt projekt's minne

---

## Git Arkitektur

```
+-------------------------------------------------------------------------+
|                         GIT ARCHITECTURE                                |
+-------------------------------------------------------------------------+
|                                                                         |
|   WORKING DIRECTORY          STAGING AREA           REPOSITORY          |
|   (Your files)               (Index)                (.git folder)       |
|   +-------------+           +-------------+        +-----------------+  |
|   | file1.py    |           |             |        | Commit History  |  |
|   | file2.js    |  git add  | file1.py    | commit |                 |  |
|   | README.md   | --------► | file2.js    | -----► |  +---+   +---+  |  |
|   | (modified)  |           | (staged)    |        |  | A |◄--| B |  |  |
|   +-------------+           +-------------+        |  +---+   +---+  |  |
|         |                         |                |     ▲          |  |
|         |        git checkout     |                |     |          |  |
|         |◄------------------------+----------------|     +-- HEAD   |  |
|                                                    +-----------------+  |
|                                                                         |
|   STATE TRANSITIONS:                                                    |
|   ----------------------------------------------------------------      |
|   Untracked  -► Staged  -► Committed  -► (repeat)                       |
|       |            |           |                                        |
|       +-- git add -+           |                                        |
|                    +-- git commit -+                                    |
|                                                                         |
|   OBJECT TYPES:                                                         |
|   +-- blob    = file content (compressed)                               |
|   +-- tree    = directory structure                                     |
|   +-- commit  = snapshot + metadata + parent pointer                    |
|   +-- tag     = named pointer to commit                                 |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Installation

### macOS

```bash
# Homebrew (rekommenderat)
brew install git

# Eller via Xcode Command Line Tools
xcode-select --install
```

### Ubuntu/Debian

```bash
# Stable version
sudo apt update
sudo apt install git

# Latest version via PPA
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
```

### Windows

```powershell
# Via winget
winget install Git.Git

# Eller ladda ner från git-scm.com
# Installera med "Git Bash" för Unix-liknande miljö
```

### Verifiera Installation

```bash
git --version
# git version 2.43.0

which git
# /usr/bin/git (eller /opt/homebrew/bin/git)
```

---

## Initial Configuration

### Identity Setup

```bash
# KRITISKT: Varje commit taggas med denna info
git config --global user.name "Said Mrebadi"
git config --global user.email "said@devopshub.se"

# Verifiera
git config --global --list
```

### Editor Configuration

```bash
# VS Code (rekommenderat för nybörjare)
git config --global core.editor "code --wait"

# Vim (för terminalmästare)
git config --global core.editor "vim"

# Nano (enklare)
git config --global core.editor "nano"
```

### Essential Settings

```bash
# Default branch name (main istället för master)
git config --global init.defaultBranch main

# Push only current branch
git config --global push.default current

# Auto-correct typos (after 3 seconds)
git config --global help.autocorrect 30

# Better diff output
git config --global diff.colorMoved default

# Prettier log format
git config --global format.pretty oneline

# Credential helper (caching)
# macOS
git config --global credential.helper osxkeychain

# Linux (cache for 1 hour)
git config --global credential.helper 'cache --timeout=3600'
```

### Alias Configuration

```bash
# Time-saving aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# Advanced aliases
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.amend 'commit --amend --no-edit'
git config --global alias.undo 'reset --soft HEAD~1'
```

---

## Skapa Repository

### Nytt Projekt

```bash
# Skapa och initiera
mkdir my-project
cd my-project
git init

# Verifiering
ls -la
# Visar .git mappen

# Status
git status
# On branch main
# No commits yet
```

### .git Mappstruktur

```
.git/
+-- HEAD              # Pointer till current branch
+-- config            # Repository-specific config
+-- description       # GitWeb description
+-- hooks/            # Pre/post commit scripts
|   +-- pre-commit.sample
|   +-- pre-push.sample
+-- info/
|   +-- exclude       # Local .gitignore
+-- objects/          # All content (blobs, trees, commits)
|   +-- info/
|   +-- pack/
+-- refs/
    +-- heads/        # Branch pointers
    +-- tags/         # Tag pointers
```

### Klona Befintligt Repository

```bash
# HTTPS (enklare)
git clone https://github.com/username/repository.git

# SSH (säkrare, kräver SSH key setup)
git clone git@github.com:username/repository.git

# Med annat mappnamn
git clone https://github.com/user/repo.git my-local-name

# Shallow clone (bara senaste commit)
git clone --depth 1 https://github.com/huge/repo.git

# Specifik branch
git clone -b develop https://github.com/user/repo.git
```

---

## Grundläggande Workflow

### Add -> Commit -> Push

```bash
# 1. Kolla status
git status

# 2. Lägg till ändringar
git add file.txt           # Specifik fil
git add .                  # Alla ändringar
git add -A                 # Alla (inkl. borttagna)
git add -p                 # Interaktiv (välj hunks)

# 3. Verifiera staging
git diff --staged

# 4. Commit
git commit -m "Add feature X"

# 5. Push (till remote)
git push origin main
```

### Commit Messages Best Practices

```bash
# Format:
# <type>(<scope>): <subject>
#
# <body>
#
# <footer>

# Exempel:
git commit -m "feat(auth): add OAuth2 login support

- Implement Google OAuth provider
- Add session management
- Update user model with provider field

Closes #123"

# Typer:
# feat     - ny feature
# fix      - bugfix
# docs     - dokumentation
# style    - formatting, semicolons
# refactor - omstrukturering utan ny feature
# test     - tester
# chore    - maintenance, dependencies
```

---

## File States Deep Dive

### Understanding States

```
+--------------------------------------------------------------------+
|                      FILE LIFECYCLE IN GIT                         |
+--------------------------------------------------------------------+
|                                                                    |
|   UNTRACKED                                                        |
|   ----------                                                       |
|   • Ny fil som Git inte känner till                               |
|   • Visas i `git status` under "Untracked files"                  |
|   • Övergång: git add -> STAGED                                    |
|                                                                    |
|   UNMODIFIED                                                       |
|   ----------                                                       |
|   • Tracked fil utan ändringar                                    |
|   • Samma som senaste commit                                      |
|   • Visas INTE i `git status` (clean)                             |
|                                                                    |
|   MODIFIED                                                         |
|   ----------                                                       |
|   • Tracked fil med ändringar                                     |
|   • Visas under "Changes not staged for commit"                   |
|   • Övergång: git add -> STAGED                                    |
|                                                                    |
|   STAGED                                                           |
|   ----------                                                       |
|   • Redo för commit                                               |
|   • Visas under "Changes to be committed"                         |
|   • Övergång: git commit -> UNMODIFIED (committed)                 |
|                                                                    |
+--------------------------------------------------------------------+
```

### Praktiska Kommandon

```bash
# Se exakt vad som är ändrat (working dir vs staging)
git diff

# Se vad som ska committas (staging vs last commit)
git diff --staged
git diff --cached  # samma sak

# Se alla ändringar (working dir vs last commit)
git diff HEAD

# Se ändringar för specifik fil
git diff -- path/to/file.py

# Kompakt status
git status -s
# M  modified_staged.py     # staged
#  M modified_unstaged.py   # modified
# A  new_staged.py          # added (staged)
# ?? untracked.py           # untracked
# MM both_staged_and_modified.py
```

---

## Viewing History

### Git Log

```bash
# Basic log
git log

# One line per commit
git log --oneline

# With graph
git log --oneline --graph --all

# Last N commits
git log -5

# Filter by author
git log --author="Said"

# Filter by date
git log --since="2024-01-01" --until="2024-06-01"

# Filter by message
git log --grep="bug fix"

# Filter by file
git log -- path/to/file.py

# Show changes in each commit
git log -p

# Stats
git log --stat
```

### Git Show

```bash
# Show specific commit
git show abc123

# Show file at commit
git show abc123:path/to/file.py

# Show tag
git show v1.0.0
```

---

## Undo Operations

### Unstage Files

```bash
# Unstage specific file
git restore --staged file.py

# Unstage all
git restore --staged .

# Old syntax (still works)
git reset HEAD file.py
```

### Discard Changes

```bash
# Discard changes in working directory
git restore file.py

# Discard all changes
git restore .

# DANGEROUS: Discard all including untracked
git clean -fd
```

### Amend Last Commit

```bash
# Change message
git commit --amend -m "New message"

# Add forgotten file
git add forgotten-file.py
git commit --amend --no-edit
```

---

## .gitignore

### Syntax

```gitignore
# Kommentarer med #

# Ignorera specifik fil
secret.key
config/database.yml

# Ignorera alla filer med extension
*.log
*.tmp
*.pyc

# Ignorera mapp
node_modules/
__pycache__/
.venv/
dist/
build/

# Negation (inkludera trots tidigare regel)
!important.log

# Glob patterns
**/logs          # logs i alla subfolders
*.py[cod]        # .pyc, .pyo, .pyd

# Ignorera i root endast
/TODO.md         # ignorera endast root TODO.md

# Ignorera bara filer, inte mappar
*.txt
!*/              # inkludera alla mappar
```

### Global Gitignore

```bash
# Skapa global ignore
git config --global core.excludesfile ~/.gitignore_global

# Innehåll i ~/.gitignore_global
.DS_Store
Thumbs.db
*.swp
.idea/
.vscode/
```

---

## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| `not a git repository` | Inte i git repo | `git init` eller `cd` rätt |
| `nothing to commit` | Inga staged ändringar | `git add .` först |
| `permission denied` | SSH key issue | Kolla SSH agent |
| `divergent branches` | Pull behövs | `git pull --rebase` |
| `detached HEAD` | Checkout commit | `git checkout main` |

---

## Praktisk Övning

```bash
# 1. Skapa projekt
mkdir git-mastery-practice && cd git-mastery-practice
git init

# 2. Konfigurera
git config user.name "Your Name"
git config user.email "you@example.com"

# 3. Skapa filer
echo "# Git Mastery" > README.md
echo "*.log" > .gitignore
echo "print('Hello Git')" > app.py

# 4. Första commit
git add .
git commit -m "feat: initial project setup"

# 5. Modifiera och commit igen
echo "print('Second feature')" >> app.py
git add app.py
git commit -m "feat: add second feature"

# 6. Kolla historik
git log --oneline

# BONUS: Skapa alias
git config alias.lg "log --oneline --graph --all"
git lg
```

---

## Sammanfattning

| Koncept | Kommando | Beskrivning |
|---------|----------|-------------|
| Init | `git init` | Skapa nytt repo |
| Clone | `git clone URL` | Kopiera repo |
| Status | `git status` | Se tillstånd |
| Add | `git add .` | Stage ändringar |
| Commit | `git commit -m ""` | Spara snapshot |
| Log | `git log --oneline` | Visa historik |
| Diff | `git diff` | Visa ändringar |
| Restore | `git restore file` | Ångra ändringar |

---

## Nästa Steg

Git basics behärskade! Nästa: **Git Core Operations** — commits, diff, reset, och stash.
''',
}

NODE_02_GIT_CORE_OPERATIONS = {
    "node_id": 2,
    "title": "Git Core Operations",
    "slug": "git-core-operations",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [1],
    "content": r'''
# Git Core Operations

## Varför detta är kritiskt

> "Git är inte bara add-commit-push. De verkliga superkrafterna ligger i att förstå commits, navigera historik, och återställa tillstånd. Dessa operationer räddar projekt."

**Verktyg du måste bemästra:**
- **Commits** — Förstå vad de verkligen är
- **Diff** — Se exakt vad som ändrats
- **Reset** — Ångra och återställ
- **Stash** — Tillfällig lagring

---

## Commit Architecture

```
+-------------------------------------------------------------------------+
|                         COMMIT ANATOMY                                  |
+-------------------------------------------------------------------------+
|                                                                         |
|   commit 7a8b9c2d4e5f6a1b2c3d4e5f6a7b8c9d0e1f2a3b                       |
|   +-- tree    d4e5f6a7b8c9...  -+                                       |
|   |                             | Pointer to project snapshot           |
|   |   +-------------------------+                                       |
|   |   |   tree d4e5f6a7...                                              |
|   |   |   +-- blob abc123  README.md                                    |
|   |   |   +-- blob def456  app.py                                       |
|   |   |   +-- tree 789abc  src/                                         |
|   |   |       +-- blob 111aaa  main.py                                  |
|   |   |       +-- blob 222bbb  utils.py                                 |
|   |                                                                     |
|   +-- parent  1a2b3c4d5e6f...  <- Previous commit (chain)                |
|   |                                                                     |
|   +-- author    Said <said@dev.se>  Mon Dec 4 10:00:00 2024             |
|   +-- committer Said <said@dev.se>  Mon Dec 4 10:00:00 2024             |
|   |                                                                     |
|   +-- message                                                           |
|       feat: implement user authentication                               |
|                                                                         |
|   SHA-1 HASH:                                                           |
|   • Calculated from: tree + parent + author + message                   |
|   • Unique identifier (collision impossible)                            |
|   • If ANY byte changes, hash changes completely                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Commit Deep Dive

### Anatomy of a Good Commit

```bash
# View commit details
git show HEAD
git show abc123

# View specific parts
git show --stat HEAD           # Files changed
git show --name-only HEAD      # Only filenames
git show --name-status HEAD    # Filenames with status (M/A/D)
git show HEAD~2                # Two commits back
git show HEAD^                 # Parent commit
git show main@{yesterday}      # Yesterday's state
```

### Commit Ranges

```bash
# Commits in feature not in main
git log main..feature

# All commits affecting file
git log --follow -- file.py

# Commits between two points
git log abc123..def456

# Commits in either but not both
git log main...feature

# Last N commits
git log -n 5
```

### Interactive Commit

```bash
# Add changes interactively (choose hunks)
git add -p

# Then for each hunk:
# y - stage this hunk
# n - skip this hunk
# s - split into smaller hunks
# e - manually edit hunk
# q - quit (don't stage rest)
```

---

## Git Diff Mastery

### Diff Types

```
+--------------------------------------------------------------------+
|                         DIFF COMPARISONS                           |
+--------------------------------------------------------------------+
|                                                                    |
|   Working Directory    Staging (Index)    Last Commit (HEAD)       |
|   -----------------    --------------     -----------------        |
|                                                                    |
|         |                    |                    |                |
|         |   git diff         |  git diff --staged |                |
|         |◄------------------►|◄------------------►|                |
|         |                    |                    |                |
|         |            git diff HEAD                |                |
|         |◄-----------------------------------------►                |
|                                                                    |
|   git diff             = Working vs Staged                         |
|   git diff --staged    = Staged vs Last Commit                     |
|   git diff HEAD        = Working vs Last Commit                    |
|   git diff abc..def    = Between two commits                       |
|   git diff branch1 branch2 = Between branches                      |
|                                                                    |
+--------------------------------------------------------------------+
```

### Practical Diff Commands

```bash
# Basic diff (working vs staged)
git diff

# Staged changes (what will be committed)
git diff --staged
git diff --cached  # Same thing

# Compare with specific commit
git diff HEAD~3

# Compare two branches
git diff main feature

# Compare specific file
git diff -- path/to/file.py

# Diff with context lines
git diff -U5  # 5 lines of context

# Word diff (more readable)
git diff --word-diff

# Stat only (no content)
git diff --stat

# Name only
git diff --name-only

# Summary (insertions/deletions)
git diff --shortstat
```

### Diff Output Explained

```diff
diff --git a/file.py b/file.py
index abc123..def456 100644
--- a/file.py                  <- Old version
+++ b/file.py                  <- New version
@@ -10,7 +10,8 @@ def function():   <- Hunk header (line numbers)
     existing line              <- Context (unchanged)
-    removed line               <- Deletion (red)
+    added line                 <- Addition (green)
+    another new line           <- Addition
     more context               <- Context
```

---

## Git Reset

### Reset Modes

```
+-------------------------------------------------------------------------+
|                         RESET MODES                                     |
+-------------------------------------------------------------------------+
|                                                                         |
|   --soft            --mixed (default)        --hard                     |
|   ------            -----------------        ------                     |
|                                                                         |
|   HEAD: ✓ Moves     HEAD: ✓ Moves            HEAD: ✓ Moves              |
|   Index: ✗ Keeps    Index: ✓ Resets          Index: ✓ Resets            |
|   Working: ✗ Keeps  Working: ✗ Keeps         Working: ✓ DELETES         |
|                                                                         |
|   Use case:         Use case:                Use case:                  |
|   Redo commit       Unstage changes          Complete undo              |
|   Squash commits    Start fresh staging      ⚠️ DESTRUCTIVE             |
|                                                                         |
|   Example:                                                              |
|   ---------                                                             |
|   Before: A - B - C - D (HEAD)                                          |
|                                                                         |
|   git reset --soft B                                                    |
|   Result: A - B (HEAD)                                                  |
|           C and D changes staged                                        |
|                                                                         |
|   git reset --mixed B                                                   |
|   Result: A - B (HEAD)                                                  |
|           C and D changes in working dir                                |
|                                                                         |
|   git reset --hard B                                                    |
|   Result: A - B (HEAD)                                                  |
|           C and D changes GONE                                          |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Reset Commands

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1
git reset --mixed HEAD~1  # Same

# Undo last commit, DISCARD changes
git reset --hard HEAD~1  # ⚠️ DANGEROUS

# Reset specific file
git reset HEAD -- file.py

# Reset to specific commit
git reset --hard abc123

# Reset to remote state
git reset --hard origin/main
```

### Recovery After Reset

```bash
# View recent HEAD positions (lifesaver!)
git reflog

# Output:
# abc123 HEAD@{0}: reset: moving to HEAD~1
# def456 HEAD@{1}: commit: feature X
# 789abc HEAD@{2}: commit: feature Y

# Recover "lost" commit
git reset --hard def456

# Or create branch from it
git branch recovered-feature def456
```

---

## Git Stash

### Stash Workflow

```
+--------------------------------------------------------------------+
|                      STASH WORKFLOW                                |
+--------------------------------------------------------------------+
|                                                                    |
|   Working Directory                    Stash Stack                 |
|   (with changes)                       -------------               |
|   +-------------+                      +-------------+             |
|   | modified    |     git stash        | stash@{0}   |             |
|   | files       | ------------------►  | stash@{1}   |             |
|   +-------------+                      | stash@{2}   |             |
|         |                              +-------------+             |
|         |                                    |                     |
|         |◄-----------------------------------+                     |
|              git stash pop                                         |
|                                                                    |
|   OPERATIONS:                                                      |
|   git stash              = Save and clean working dir              |
|   git stash pop          = Restore and remove from stack           |
|   git stash apply        = Restore but keep in stack               |
|   git stash list         = Show all stashes                        |
|   git stash drop         = Remove top stash                        |
|   git stash clear        = Remove ALL stashes                      |
|                                                                    |
+--------------------------------------------------------------------+
```

### Stash Commands

```bash
# Basic stash (tracked files only)
git stash

# With message
git stash push -m "Work in progress on feature X"

# Include untracked files
git stash -u
git stash --include-untracked

# Include ignored files too
git stash -a
git stash --all

# Stash specific files
git stash push -m "partial work" -- file1.py file2.py

# Interactive stash (choose hunks)
git stash -p
```

### Working with Stash

```bash
# List stashes
git stash list
# stash@{0}: On main: WIP on feature X
# stash@{1}: On develop: debug code
# stash@{2}: On main: broken implementation

# View stash contents
git stash show           # Summary
git stash show -p        # Full diff
git stash show stash@{2} # Specific stash

# Apply most recent (keep in stack)
git stash apply

# Apply specific stash
git stash apply stash@{2}

# Apply and remove (pop)
git stash pop

# Remove stash without applying
git stash drop stash@{1}

# Clear all stashes
git stash clear
```

### Stash Branch

```bash
# Create branch from stash
git stash branch new-feature stash@{0}
# Creates branch, checks it out, applies stash, drops stash
```

---

## Git Restore vs Reset

### Comparison

| Command | Affects | Use Case |
|---------|---------|----------|
| `git restore file` | Working Dir | Discard local changes |
| `git restore --staged file` | Index | Unstage file |
| `git reset --soft` | HEAD | Redo commit |
| `git reset --mixed` | HEAD + Index | Unstage all |
| `git reset --hard` | Everything | Complete undo |

```bash
# Modern commands (Git 2.23+)
git restore file.py                  # Discard changes
git restore --staged file.py         # Unstage
git restore --source=HEAD~2 file.py  # Restore from commit

# Legacy commands (still work)
git checkout -- file.py              # Discard changes
git reset HEAD file.py               # Unstage
```

---

## Practical Scenarios

### Scenario 1: Oops, Committed to Wrong Branch

```bash
# You're on main, should have been on feature
git log --oneline -1  # Note the commit hash

# Undo commit (keep changes)
git reset --soft HEAD~1

# Switch and commit there
git checkout feature
git commit -m "Same message"
```

### Scenario 2: Need to Switch Branch with Uncommitted Changes

```bash
# Stash your work
git stash -m "WIP feature X"

# Switch and work
git checkout other-branch
# ... do work ...

# Return and restore
git checkout original-branch
git stash pop
```

### Scenario 3: Accidentally Staged Wrong File

```bash
# Unstage it
git restore --staged secret-file.env

# Or for all files
git restore --staged .
```

---

## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| Lost commits after reset | Used --hard | `git reflog` + `git reset --hard <hash>` |
| Stash conflicts on pop | Changes conflict | Resolve manually, then `git stash drop` |
| Can't stash | No tracked changes | Use `git stash -u` for untracked |
| Wrong file staged | Accidental `git add` | `git restore --staged file` |

---

## Sammanfattning

| Operation | Command | Effect |
|-----------|---------|--------|
| View diff | `git diff` | See changes |
| Soft reset | `git reset --soft HEAD~1` | Undo commit, keep staged |
| Mixed reset | `git reset HEAD~1` | Undo commit, unstaged |
| Hard reset | `git reset --hard HEAD~1` | ⚠️ Undo everything |
| Stash | `git stash` | Save work temporarily |
| Pop stash | `git stash pop` | Restore work |
| Recovery | `git reflog` | Find lost commits |

---

## Nästa Steg

Core operations bemästrade. Nästa: **Branching & Merging** — parallell utveckling.
''',
}

NODE_03_BRANCHING_MERGING = {
    "node_id": 3,
    "title": "Branching & Merging",
    "slug": "branching-merging",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [2],
    "content": r'''
# Branching & Merging

## Varför detta är kritiskt

> "Branching är Git's superkraft. Det låter team arbeta parallellt utan att trampa på varandra. Merge och rebase är verktygen som sammanfogar arbete. Förstå dem = bli en Git-mästare."

**Verkliga scenarier:**
- Utveckla features isolerat
- Fixa buggar utan att störa pågående arbete
- Experimentera säkert
- Code review via Pull Requests

---

## Branch Architecture

```
+-------------------------------------------------------------------------+
|                       BRANCH CONCEPTUAL MODEL                           |
+-------------------------------------------------------------------------+
|                                                                         |
|                                                                         |
|   main:        A --- B --- C --------------- G --- H                    |
|                           |                 ▲                           |
|                           |                 | merge                     |
|   feature:                +--- D --- E --- F                            |
|                                                                         |
|                                                                         |
|   WHAT IS A BRANCH?                                                     |
|   ------------------                                                    |
|   • Just a pointer (40-byte file!) to a commit                          |
|   • .git/refs/heads/main contains: abc123...                            |
|   • Creating branch = creating new pointer                              |
|   • Super fast (no file copying)                                        |
|                                                                         |
|   HEAD:                                                                 |
|   ------                                                                |
|   • Pointer to current branch (or commit in detached state)             |
|   • .git/HEAD contains: ref: refs/heads/main                            |
|   • Moves when you commit or checkout                                   |
|                                                                         |
|   BRANCH NAMING:                                                        |
|   --------------                                                        |
|   feature/     -> new features (feature/user-auth)                       |
|   bugfix/      -> bug fixes (bugfix/login-crash)                         |
|   hotfix/      -> production fixes (hotfix/security-patch)               |
|   release/     -> release prep (release/v2.0)                            |
|   experiment/  -> experiments (experiment/new-algorithm)                 |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Branch Operations

### Create and Switch

```bash
# List branches
git branch              # Local only
git branch -a           # All (including remote)
git branch -v           # With last commit
git branch -vv          # With tracking info

# Create branch
git branch feature-x

# Switch to branch (modern)
git switch feature-x

# Switch to branch (legacy)
git checkout feature-x

# Create AND switch (modern)
git switch -c feature-y

# Create AND switch (legacy)
git checkout -b feature-y

# Create from specific commit
git switch -c hotfix abc123

# Create tracking branch
git switch -c feature origin/feature
```

### Delete Branches

```bash
# Delete merged branch
git branch -d feature-done

# Force delete (even if unmerged)
git branch -D abandoned-feature

# Delete remote branch
git push origin --delete feature-done

# Prune deleted remote branches locally
git fetch --prune
```

### Rename Branches

```bash
# Rename current branch
git branch -m new-name

# Rename specific branch
git branch -m old-name new-name

# After renaming, update remote
git push origin -u new-name
git push origin --delete old-name
```

---

## Merge Strategies

### Fast-Forward Merge

```
+--------------------------------------------------------------------+
|                    FAST-FORWARD MERGE                              |
+--------------------------------------------------------------------+
|                                                                    |
|   BEFORE:                                                          |
|   main:     A --- B --- C                                          |
|                         |                                          |
|   feature:              +--- D --- E                               |
|                                   HEAD                              |
|                                                                    |
|   AFTER git merge feature (on main):                               |
|   main:     A --- B --- C --- D --- E                              |
|                                   HEAD                              |
|                                                                    |
|   • No new commit created                                          |
|   • main pointer just moves forward                                |
|   • Linear history preserved                                       |
|   • Happens when no commits on main since branch                   |
|                                                                    |
+--------------------------------------------------------------------+
```

```bash
# On main
git merge feature-x
# Fast-forward merge if possible

# Force merge commit even if FF possible
git merge --no-ff feature-x
```

### Three-Way Merge

```
+--------------------------------------------------------------------+
|                    THREE-WAY MERGE                                 |
+--------------------------------------------------------------------+
|                                                                    |
|   BEFORE:                                                          |
|   main:     A --- B --- C --- F                                    |
|                         |     HEAD                                  |
|   feature:              +--- D --- E                               |
|                                                                    |
|   AFTER git merge feature (on main):                               |
|   main:     A --- B --- C --- F --- G (merge commit)               |
|                         |           |                              |
|   feature:              +--- D --- E+                              |
|                                                                    |
|   • Creates new merge commit (G)                                   |
|   • G has TWO parents (F and E)                                    |
|   • Uses "common ancestor" (C) to resolve                          |
|   • Non-linear but shows true history                              |
|                                                                    |
+--------------------------------------------------------------------+
```

```bash
# Three-way merge with message
git merge feature-x -m "Merge feature-x: user authentication"

# Abort if conflicts
git merge --abort

# View merge commits
git log --merges
```

---

## Handling Merge Conflicts

### Conflict Anatomy

```
+--------------------------------------------------------------------+
|                    MERGE CONFLICT                                  |
+--------------------------------------------------------------------+
|                                                                    |
|   File content during conflict:                                    |
|   ------------------------------                                   |
|                                                                    |
|   Some code that's fine                                            |
|   <<<<<<< HEAD                                                     |
|   This is from current branch (main)                               |
|   =======                                                          |
|   This is from incoming branch (feature)                           |
|   >>>>>>> feature-x                                                |
|   More code that's fine                                            |
|                                                                    |
|   RESOLUTION:                                                      |
|   1. Edit file - remove markers, keep desired code                 |
|   2. git add file                                                  |
|   3. git commit (merge commit message pre-filled)                  |
|                                                                    |
+--------------------------------------------------------------------+
```

### Resolving Conflicts

```bash
# Start merge
git merge feature-x
# CONFLICT (content): Merge conflict in file.py

# See conflicted files
git status
# both modified:   file.py

# Edit file manually OR use merge tool
git mergetool

# After fixing
git add file.py
git commit
# Uses pre-filled merge message

# OR abort everything
git merge --abort
```

### Merge Tool Setup

```bash
# Configure VS Code as merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Or use vimdiff
git config --global merge.tool vimdiff

# Run merge tool
git mergetool
```

---

## Git Rebase

### Rebase Concept

```
+-------------------------------------------------------------------------+
|                       REBASE VISUALIZATION                              |
+-------------------------------------------------------------------------+
|                                                                         |
|   BEFORE REBASE:                                                        |
|   main:     A --- B --- C --- F                                         |
|                         |                                               |
|   feature:              +--- D --- E                                    |
|                                   HEAD                                  |
|                                                                         |
|   git rebase main (while on feature):                                   |
|   -------------------------------------                                 |
|                                                                         |
|   AFTER REBASE:                                                         |
|   main:     A --- B --- C --- F                                         |
|                               |                                         |
|   feature:                    +--- D' --- E'                            |
|                                          HEAD                           |
|                                                                         |
|   • D and E are REPLAYED on top of F                                    |
|   • Creates NEW commits (D', E') with different hashes                  |
|   • Original D and E still exist but unreferenced                       |
|   • Results in LINEAR history                                           |
|                                                                         |
|   ⚠️ GOLDEN RULE:                                                       |
|   Never rebase commits that have been pushed to shared branches!        |
|   (Rewrites history = confuses collaborators)                           |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Rebase Commands

```bash
# Simple rebase
git checkout feature
git rebase main

# Interactive rebase (edit history)
git rebase -i HEAD~5

# Rebase onto specific commit
git rebase --onto main feature~3 feature

# Continue after resolving conflicts
git rebase --continue

# Skip problematic commit
git rebase --skip

# Abort rebase
git rebase --abort
```

### Interactive Rebase

```bash
# Edit last 5 commits
git rebase -i HEAD~5

# Editor opens:
pick abc123 First commit
pick def456 Second commit
pick 789abc Third commit

# Options:
# pick   = use commit as-is
# reword = change commit message
# edit   = stop for amending
# squash = meld into previous commit
# fixup  = like squash but discard message
# drop   = remove commit
# reorder = just reorder lines

# Example: Squash last 3 into 1
pick abc123 First commit
squash def456 Second commit
squash 789abc Third commit
```

---

## Merge vs Rebase

| Aspect | Merge | Rebase |
|--------|-------|--------|
| History | Non-linear (true) | Linear (clean) |
| Creates | Merge commit | New commits |
| Safety | Safe always | ⚠️ Don't rebase pushed |
| Conflicts | Resolve once | May resolve multiple |
| Use case | Shared branches | Local cleanup |

```bash
# Recommended workflow:
# 1. Work on feature branch
# 2. Rebase locally before merge
git checkout feature
git rebase main
# 3. Merge (will be fast-forward)
git checkout main
git merge feature
```

---

## Cherry-Pick

### Single Commit

```bash
# Apply specific commit to current branch
git cherry-pick abc123

# Without auto-commit (for editing)
git cherry-pick -n abc123

# Cherry-pick range
git cherry-pick abc123..def456

# Cherry-pick merge commit (specify parent)
git cherry-pick -m 1 merge-commit-hash
```

### Use Cases

```bash
# Hotfix: Apply bug fix from develop to main
git checkout main
git cherry-pick bugfix-commit-hash

# Partial feature: Take only one commit
git checkout release
git cherry-pick specific-feature-commit
```

---

## Branch Strategies

### Git Flow

```
+--------------------------------------------------------------------+
|                      GIT FLOW                                      |
+--------------------------------------------------------------------+
|                                                                    |
|   main     ----●-------------------●---------------●--             |
|               |                   ▲               ▲                |
|               |                   | hotfix        |                |
|   hotfix      |                ---●---            |                |
|               |                                   |                |
|   release     |           ----●----●--------------+                |
|               |          ▲                                         |
|               |          |                                         |
|   develop  ---●------●---●--------------●----------                |
|               |      ▲              ▲                              |
|               |      |              |                              |
|   feature     +--●---+     ●----●---+                              |
|                                                                    |
|   Branches:                                                        |
|   main     = production code only                                  |
|   develop  = integration branch                                    |
|   feature/ = new features                                          |
|   release/ = release preparation                                   |
|   hotfix/  = emergency production fixes                            |
|                                                                    |
+--------------------------------------------------------------------+
```

### Trunk-Based Development

```
+--------------------------------------------------------------------+
|                  TRUNK-BASED DEVELOPMENT                           |
+--------------------------------------------------------------------+
|                                                                    |
|   main     ----●----●----●----●----●----●----●----                 |
|               |    |    |    |                                     |
|   feature     +●---+    +●---+                                     |
|               (short-lived)                                        |
|                                                                    |
|   Principles:                                                      |
|   • Very short-lived feature branches (1-2 days)                   |
|   • Merge to main frequently                                       |
|   • Feature flags for incomplete features                          |
|   • Requires good CI/CD                                            |
|                                                                    |
+--------------------------------------------------------------------+
```

---

## Praktisk Övning

```bash
# 1. Setup
git init branch-practice && cd branch-practice
echo "# Branch Practice" > README.md
git add . && git commit -m "Initial commit"

# 2. Create feature branch
git switch -c feature/add-login
echo "Login code" > login.py
git add . && git commit -m "feat: add login"

# 3. Simulate main progressing
git switch main
echo "Other work" > other.py
git add . && git commit -m "feat: other work"

# 4. Rebase feature onto main
git switch feature/add-login
git rebase main

# 5. Merge back
git switch main
git merge feature/add-login

# 6. Check history
git log --oneline --graph --all
```

---

## Sammanfattning

| Operation | Command | Result |
|-----------|---------|--------|
| Create branch | `git switch -c name` | New branch |
| Merge | `git merge branch` | Combine histories |
| Rebase | `git rebase main` | Linear history |
| Cherry-pick | `git cherry-pick hash` | Copy single commit |
| Delete branch | `git branch -d name` | Remove branch |

---

## Nästa Steg

Branching och merging behärskade. Nästa: **Remote Repositories** — samarbete och GitHub.
''',
}

NODE_04_REMOTE_REPOSITORIES = {
    "node_id": 4,
    "title": "Remote Repositories",
    "slug": "remote-repositories",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [3],
    "content": r'''
# Remote Repositories

## Varför detta är kritiskt

> "Git utan remotes är som en bil utan vägar. Remotes möjliggör samarbete, backup, deployment. GitHub, GitLab, Bitbucket — förstå hur de fungerar med Git."

**Remote operations:**
- Push/Pull code
- Sync med team
- Backup till molnet
- CI/CD triggers

---

## Remote Architecture

```
+-------------------------------------------------------------------------+
|                       REMOTE ARCHITECTURE                               |
+-------------------------------------------------------------------------+
|                                                                         |
|   LOCAL MACHINE                      REMOTE SERVER                      |
|   -------------                      -------------                      |
|                                                                         |
|   Working Dir                                                           |
|   +---------+      git push         +----------------------+            |
|   | files   | -------------------►  | origin/main          |            |
|   +---------+                       | origin/develop       |            |
|       |                             | origin/feature-x     |            |
|   +---------+      git fetch        +----------------------+            |
|   | .git    | ◄-------------------           |                          |
|   | local   |                                | github.com               |
|   | refs    |                                | gitlab.com               |
|   +---------+                                | bitbucket.org            |
|       |                                                                 |
|   LOCAL BRANCHES:        REMOTE-TRACKING BRANCHES:                      |
|   main                   origin/main                                    |
|   develop               origin/develop                                  |
|   feature-x              origin/feature-x                               |
|                                                                         |
|   MULTIPLE REMOTES:                                                     |
|   origin   -> Your fork (read/write)                                     |
|   upstream -> Original repo (usually read-only)                          |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Managing Remotes

### View Remotes

```bash
# List remotes
git remote
# origin

# List with URLs
git remote -v
# origin  https://github.com/user/repo.git (fetch)
# origin  https://github.com/user/repo.git (push)

# Show detailed info
git remote show origin
# * remote origin
#   Fetch URL: https://github.com/user/repo.git
#   Push  URL: https://github.com/user/repo.git
#   HEAD branch: main
#   Remote branches:
#     develop tracked
#     main    tracked
```

### Add/Remove Remotes

```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# Add upstream (for forks)
git remote add upstream https://github.com/original/repo.git

# Remove remote
git remote remove upstream

# Rename remote
git remote rename origin github

# Change URL
git remote set-url origin git@github.com:user/repo.git
```

---

## Fetch, Pull, Push

### Git Fetch

```
+--------------------------------------------------------------------+
|                        GIT FETCH                                   |
+--------------------------------------------------------------------+
|                                                                    |
|   BEFORE:                                                          |
|   Local:   main --- A --- B                                        |
|   origin/main --- A --- B                                          |
|                                                                    |
|   Remote (has new commits):                                        |
|   origin: main --- A --- B --- C --- D                             |
|                                                                    |
|   AFTER git fetch:                                                 |
|   Local:   main --- A --- B                                        |
|   origin/main --- A --- B --- C --- D                              |
|                                                                    |
|   • Downloads commits but doesn't merge                            |
|   • Updates remote-tracking branches                               |
|   • Safe operation (no changes to working dir)                     |
|                                                                    |
+--------------------------------------------------------------------+
```

```bash
# Fetch from default remote
git fetch

# Fetch from specific remote
git fetch upstream

# Fetch specific branch
git fetch origin main

# Fetch all remotes
git fetch --all

# Fetch and prune deleted branches
git fetch --prune
```

### Git Pull

```bash
# Pull = Fetch + Merge
git pull

# Pull with rebase (cleaner history)
git pull --rebase

# Pull specific branch
git pull origin develop

# Configure pull to always rebase
git config --global pull.rebase true
```

### Git Push

```bash
# Push current branch
git push

# Push to specific remote/branch
git push origin main

# Push and set upstream (first time)
git push -u origin feature-x
git push --set-upstream origin feature-x

# Push all branches
git push --all

# Push tags
git push --tags

# Force push (DANGEROUS - rewrites remote history)
git push --force

# Force push with safety (fails if remote has new commits)
git push --force-with-lease
```

---

## Remote-Tracking Branches

### Understanding Remote Tracking

```bash
# Local branch tracking remote
git branch -vv
# * main         abc123 [origin/main] Latest commit
#   feature      def456 [origin/feature: ahead 2] Two new commits
#   develop      789abc [origin/develop: behind 3] Three commits behind

# Set tracking
git branch -u origin/feature
git branch --set-upstream-to=origin/feature

# Create branch tracking remote
git checkout -b feature origin/feature

# See what would be pushed/pulled
git log origin/main..HEAD    # Commits to push
git log HEAD..origin/main    # Commits to pull
```

### Comparing Local and Remote

```bash
# Commits on remote not in local
git log HEAD..origin/main

# Commits in local not on remote
git log origin/main..HEAD

# Show divergence
git log --left-right main...origin/main
```

---

## Cloning Deep Dive

### Clone Options

```bash
# Standard clone
git clone https://github.com/user/repo.git

# Clone to specific folder
git clone https://github.com/user/repo.git my-folder

# Shallow clone (latest only)
git clone --depth 1 https://github.com/user/repo.git

# Clone specific branch
git clone -b develop https://github.com/user/repo.git

# Clone with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Mirror clone (exact copy, for backup)
git clone --mirror https://github.com/user/repo.git
```

### SSH vs HTTPS

```bash
# HTTPS (easier setup, requires token for push)
git clone https://github.com/user/repo.git

# SSH (requires key setup, more secure)
git clone git@github.com:user/repo.git

# Convert HTTPS to SSH
git remote set-url origin git@github.com:user/repo.git
```

---

## Syncing Forks

### Fork Workflow

```
+--------------------------------------------------------------------+
|                       FORK WORKFLOW                                |
+--------------------------------------------------------------------+
|                                                                    |
|   ORIGINAL REPO (upstream)                                         |
|   github.com/company/project                                       |
|        |                 ▲                                         |
|        | fork            | Pull Request                            |
|        ▼                 |                                         |
|   YOUR FORK (origin)                                               |
|   github.com/you/project                                           |
|        |                 ▲                                         |
|        | clone           | push                                    |
|        ▼                 |                                         |
|   LOCAL REPOSITORY                                                 |
|   ~/code/project                                                   |
|                                                                    |
|   WORKFLOW:                                                        |
|   1. Fork on GitHub                                                |
|   2. Clone your fork                                               |
|   3. Add upstream remote                                           |
|   4. Create feature branch                                         |
|   5. Make changes, push to origin                                  |
|   6. Create Pull Request to upstream                               |
|                                                                    |
+--------------------------------------------------------------------+
```

### Sync Commands

```bash
# Add upstream (once)
git remote add upstream https://github.com/original/repo.git

# Sync with upstream
git fetch upstream

# Update main with upstream
git checkout main
git merge upstream/main

# Or rebase
git checkout main
git rebase upstream/main

# Push updated main to your fork
git push origin main
```

---

## Tags

### Creating Tags

```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag specific commit
git tag -a v0.9.0 abc123 -m "Beta release"

# List tags
git tag
git tag -l "v1.*"
```

### Pushing Tags

```bash
# Push specific tag
git push origin v1.0.0

# Push all tags
git push --tags

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## Submodules

### Adding Submodules

```bash
# Add submodule
git submodule add https://github.com/lib/library.git libs/library

# Clone with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Initialize submodules in existing clone
git submodule update --init --recursive
```

### Updating Submodules

```bash
# Update all submodules
git submodule update --remote

# Update specific submodule
git submodule update --remote libs/library

# Pull with submodule updates
git pull --recurse-submodules
```

---

## Practical Scenarios

### Scenario 1: Diverged Branches

```bash
# Your push is rejected because remote has new commits
# error: failed to push some refs

# Solution 1: Pull and merge
git pull
# Resolve any conflicts
git push

# Solution 2: Pull with rebase (cleaner)
git pull --rebase
git push
```

### Scenario 2: Reset to Remote State

```bash
# Discard all local changes, match remote
git fetch origin
git reset --hard origin/main
```

### Scenario 3: Working with Multiple Remotes

```bash
# Setup
git remote add github git@github.com:user/repo.git
git remote add gitlab git@gitlab.com:user/repo.git

# Push to both
git push github main
git push gitlab main
```

---

## Felsökning

| Problem | Orsak | Lösning |
|---------|-------|---------|
| `rejected - non-fast-forward` | Remote has new commits | `git pull --rebase` then push |
| `Permission denied (publickey)` | SSH key issue | Check `ssh-add -l`, add key |
| `Repository not found` | Wrong URL or no access | Verify URL and permissions |
| `Could not read from remote` | Network or auth issue | Check network, re-auth |

---

## Sammanfattning

| Command | Operation | Note |
|---------|-----------|------|
| `git remote -v` | List remotes | URLs shown |
| `git fetch` | Download changes | Safe, no merge |
| `git pull` | Download + merge | Or `--rebase` |
| `git push` | Upload changes | `-u` first time |
| `git clone` | Copy repository | `--depth 1` for shallow |

---

## Nästa Steg

Remote repositories behärskade. Nästa: **GitHub Collaboration** — Pull Requests, Issues, Actions.
''',
}

GIT_BLOCK_1 = [
    NODE_01_GIT_INTRODUCTION,
    NODE_02_GIT_CORE_OPERATIONS,
    NODE_03_BRANCHING_MERGING,
    NODE_04_REMOTE_REPOSITORIES,
]
