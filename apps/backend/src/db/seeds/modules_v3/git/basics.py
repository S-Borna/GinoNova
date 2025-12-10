"""
Git Basics - Tasks 1-8
Premium Bootcamp-Quality Content
"""

TASKS_BASICS = [
    {
        "title": "Git Introduktion & Installation",
        "difficulty": "easy",
        "estimated_minutes": 45,
        "xp_reward": 100,
        "content": r"""
# 🎯 Git Introduktion & Installation

## Lärande mål
Efter denna lektion kommer du kunna:
- Förstå vad Git är och varför det används
- Installera Git på ditt operativsystem
- Konfigurera Git med din identitet
- Verifiera att allt fungerar

---

## 📖 Vad är Git?

Git är ett **distribuerat versionshanteringssystem** skapat av Linus Torvalds 2005.

### Varför Git?

```
+-----------------------------------------------------------------+
|                    UTAN VERSIONSHANTERING                       |
+-----------------------------------------------------------------+
|                                                                 |
|   projekt_v1.zip                                                |
|   projekt_v2_final.zip                                          |
|   projekt_v2_final_FINAL.zip                                    |
|   projekt_v2_final_FINAL_fixed.zip        <- Kaos!              |
|   projekt_backup_jan15.zip                                      |
|                                                                 |
+-----------------------------------------------------------------+

+-----------------------------------------------------------------+
|                      MED GIT                                    |
+-----------------------------------------------------------------+
|                                                                 |
|   .git/                                                         |
|   +-- Full historik                                             |
|   +-- Alla versioner                   <- Ordning!              |
|   +-- Vem ändrade vad                                          |
|   +-- Enkelt samarbete                                          |
|                                                                 |
+-----------------------------------------------------------------+
```

### Git vs Andra System

| Feature | Git | SVN | Dropbox |
|---------|-----|-----|---------|
| Distribuerat | ✅ | ❌ | ❌ |
| Branching | ✅ Snabbt | ⚠️ Långsamt | ❌ |
| Offline | ✅ | ❌ | ⚠️ |
| Merge | ✅ Smart | ⚠️ Basic | ❌ |
| Industri standard | ✅ | ❌ | ❌ |

---

## 🛠️ Installation

### macOS

```bash
# Alternativ 1: Xcode Command Line Tools (inkluderar Git)
xcode-select --install

# Alternativ 2: Homebrew (rekommenderat)
brew install git

# Verifiera
git --version
# git version 2.43.0
```

### Ubuntu/Debian

```bash
# Uppdatera paketlista
sudo apt update

# Installera Git
sudo apt install git -y

# Verifiera
git --version
# git version 2.43.0
```

### Windows

```powershell
# Alternativ 1: Git for Windows
# Ladda ner från https://git-scm.com/download/win

# Alternativ 2: winget
winget install Git.Git

# Alternativ 3: Chocolatey
choco install git

# Verifiera (i Git Bash eller PowerShell)
git --version
```

---

## ⚙️ Grundkonfiguration

### Obligatorisk konfiguration

```bash
# Din identitet (används i varje commit)
git config --global user.name "Ditt Namn"
git config --global user.email "din.email@example.com"

# Verifiera
git config --global --list
```

### Rekommenderad konfiguration

```bash
# Default branch namn (main istället för master)
git config --global init.defaultBranch main

# Standard editor (välj din favorit)
git config --global core.editor "code --wait"    # VS Code
git config --global core.editor "vim"            # Vim
git config --global core.editor "nano"           # Nano

# Färger i terminalen
git config --global color.ui auto

# Hjälpsamma alias
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
```

### Konfigurationsfiler

```bash
# Tre nivåer av config
~/.gitconfig           # --global (användare)
.git/config            # --local (repo, default)
/etc/gitconfig         # --system (alla användare)

# Se var config kommer från
git config --list --show-origin
```

---

## 🧪 Verifiera Installation

```bash
# Test 1: Git version
git --version

# Test 2: Config
git config user.name
git config user.email

# Test 3: Skapa test-repo
mkdir git-test && cd git-test
git init
echo "Hello Git" > README.md
git add .
git commit -m "Initial commit"
git log --oneline

# Cleanup
cd .. && rm -rf git-test
```

---

## 🏋️ Övningar

### Övning 1: Installera och konfigurera
1. Installera Git på ditt system
2. Konfigurera namn och email
3. Sätt default branch till `main`
4. Konfigurera din favorit-editor

### Övning 2: Skapa alias
```bash
# Skapa dessa alias och testa dem
git config --global alias.s "status -sb"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "reset HEAD --"
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Git | Distribuerat versionshanteringssystem |
| Config levels | system < global < local |
| user.name | Din identitet i commits |
| user.email | Email kopplad till commits |

**Nästa steg:** Git Grundläggande Workflow

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Git Grundläggande Workflow",
        "difficulty": "easy",
        "estimated_minutes": 50,
        "xp_reward": 120,
        "content": r"""
# 🔄 Git Grundläggande Workflow

## Lärande mål
- Förstå Git's tre områden (working, staging, repository)
- Skapa repositories med `git init` och `git clone`
- Använda `git add`, `git commit`, `git status`
- Förstå .gitignore

---

## 📖 Git's Tre Områden

```
+-----------------------------------------------------------------+
|                       GIT WORKFLOW                              |
+-----------------------------------------------------------------+
|                                                                 |
|  +--------------+    +--------------+    +--------------+      |
|  |   Working    |--->|   Staging    |--->|  Repository  |      |
|  |  Directory   |    |    Area      |    |   (.git)     |      |
|  +--------------+    +--------------+    +--------------+      |
|         |                   |                   |               |
|    Dina filer         git add           git commit              |
|    (ändringar)       (välj vad)        (spara snapshot)        |
|                                                                 |
+-----------------------------------------------------------------+
```

### Varför Staging Area?

```bash
# Scenario: Du har ändrat 5 filer men vill bara commita 2

# Utan staging - allt eller inget
# Med staging - välj exakt vad som ska ingå

git add file1.py file2.py    # Bara dessa två
git commit -m "Add feature"  # Commit endast valda
```

---

## 🏗️ Skapa Repository

### Nytt projekt

```bash
# Skapa mapp och initiera
mkdir my-project
cd my-project
git init

# Resultat
Initialized empty Git repository in /path/my-project/.git/

# Verifiera
ls -la
# .git/  <- Git's databas
```

### Klona befintligt

```bash
# HTTPS
git clone https://github.com/user/repo.git

# SSH (rekommenderat)
git clone git@github.com:user/repo.git

# Med annat namn
git clone https://github.com/user/repo.git my-folder

# Shallow clone (bara senaste)
git clone --depth 1 https://github.com/user/repo.git
```

---

## 📝 Status & Diff

### git status

```bash
# Full status
git status

# Kort format
git status -s
# M  modified.txt      # Modified, staged
#  M unstaged.txt      # Modified, not staged
# ?? new-file.txt      # Untracked
# A  added.txt         # New file, staged
# D  deleted.txt       # Deleted

# Branch info också
git status -sb
# ## main...origin/main
```

### git diff

```bash
# Working vs Staging
git diff

# Staging vs Last Commit
git diff --staged
git diff --cached  # samma sak

# Working vs Specific Commit
git diff HEAD~2

# Mellan två commits
git diff abc123 def456

# Endast filnamn
git diff --name-only
```

---

## ➕ Lägga till filer

### git add

```bash
# En fil
git add README.md

# Flera filer
git add file1.txt file2.txt

# Alla filer i mapp
git add src/

# Alla ändringar
git add .
git add -A  # samma sak

# Interaktiv (välj hunks)
git add -p
# y = stage this hunk
# n = skip
# s = split into smaller
# q = quit
```

### Interaktiv add (git add -p)

```bash
# Perfekt när du vill dela upp ändringar
git add -p

# Exempel output:
# @@ -1,3 +1,5 @@
#  line 1
# +new line
#  line 2
# Stage this hunk [y,n,q,a,d,s,e,?]?
```

---

## 💾 Commit

### Grundläggande commit

```bash
# Med meddelande
git commit -m "Add login feature"

# Öppna editor för längre meddelande
git commit

# Add + Commit (endast tracked files)
git commit -am "Quick update"
```

### Bra commit-meddelanden

```bash
# ❌ Dåligt
git commit -m "fix"
git commit -m "update"
git commit -m "changes"

# ✅ Bra
git commit -m "Fix login button not responding on mobile"
git commit -m "Add user authentication with JWT tokens"
git commit -m "Refactor database connection pooling"

# Format: Conventional Commits
# <type>(<scope>): <description>
git commit -m "feat(auth): add OAuth2 Google login"
git commit -m "fix(ui): correct button alignment on Safari"
git commit -m "docs(readme): update installation steps"
```

### Commit Types

| Type | Användning |
|------|-----------|
| feat | Ny feature |
| fix | Buggfix |
| docs | Dokumentation |
| style | Formattering (ingen kodändring) |
| refactor | Refaktorering |
| test | Tester |
| chore | Underhåll |

---

## 🚫 .gitignore

### Skapa .gitignore

```bash
# .gitignore - filer som Git ska ignorera

# Operativsystem
.DS_Store
Thumbs.db

# Dependencies
node_modules/
vendor/
__pycache__/
*.pyc

# Build output
dist/
build/
*.o
*.exe

# Environment & Secrets
.env
.env.local
*.pem
secrets/

# IDE
.vscode/
.idea/
*.swp

# Logs
*.log
logs/

# Temporary
tmp/
*.tmp
```

### Patterns

```bash
# Ignorera alla .log filer
*.log

# Men inte important.log
!important.log

# Ignorera build/ i root
/build/

# Ignorera build/ överallt
build/

# Ignorera filer i specifik mapp
docs/*.txt
```

### Globala ignores

```bash
# Skapa global gitignore
git config --global core.excludesfile ~/.gitignore_global

# Lägg till OS-specifika filer
echo ".DS_Store" >> ~/.gitignore_global
echo "Thumbs.db" >> ~/.gitignore_global
```

---

## 🏋️ Övningar

### Övning 1: Komplett workflow
```bash
mkdir git-practice && cd git-practice
git init
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"
echo "console.log('hello')" > app.js
git status
git add app.js
git commit -m "feat: add main application file"
git log --oneline
```

### Övning 2: Partial staging
```bash
# Ändra flera saker i en fil
# Använd git add -p för att välja vad som ska stageas
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git init | Skapa nytt repo |
| git clone | Kopiera befintligt repo |
| git status | Visa status |
| git diff | Visa ändringar |
| git add | Stagea ändringar |
| git commit | Spara snapshot |

**Nästa steg:** Git Log & Historik

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Git Log & Historik",
        "difficulty": "easy",
        "estimated_minutes": 45,
        "xp_reward": 110,
        "content": r"""
# 📜 Git Log & Historik

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Navigera commit-historik med `git log`
- Förstå commit-hash och referenser
- Använda `git show` för detaljer
- Söka i historik

---

## 📖 Git Log Basics

### Grundläggande log

```bash
# Full log
git log

# Output:
# commit abc123def456... (HEAD -> main)
# Author: Your Name <email@example.com>
# Date:   Mon Dec 4 10:30:00 2025 +0100
#
#     Add new feature

# Kompakt format
git log --oneline
# abc123d Add new feature
# def456a Fix bug
# ghi789b Initial commit
```

### Log med graf

```bash
# Visa branch-struktur
git log --oneline --graph

# Med alla branches
git log --oneline --graph --all

# Dekorationer (branch/tag labels)
git log --oneline --graph --all --decorate

# Mitt favorit-alias
git config --global alias.lg "log --oneline --graph --all --decorate"
git lg
```

### Exempel på graf-output

```
* abc123d (HEAD -> feature) Add new feature
* def456a Update tests
| * ghi789b (main) Hotfix
|/
* jkl012c Common ancestor
* mno345d Initial commit
```

---

## 🔢 Commit Referenser

### Hash

```bash
# Full hash (40 tecken)
abc123def456789012345678901234567890abcd

# Short hash (7+ tecken, unika)
abc123d

# Använd i kommandon
git show abc123d
git diff abc123d def456a
```

### Relativa referenser

```bash
# HEAD = nuvarande position
git show HEAD

# En commit bakåt
git show HEAD~1
git show HEAD^

# Tre commits bakåt
git show HEAD~3

# Parent av merge (första parent)
git show HEAD^1

# Parent av merge (andra parent)
git show HEAD^2
```

### Diagram: Referenser

```
HEAD~3   HEAD~2   HEAD~1   HEAD
   |        |        |       |
   ▼        ▼        ▼       ▼
+-----+  +-----+  +-----+  +-----+
| A   |--| B   |--| C   |--| D   |
+-----+  +-----+  +-----+  +-----+
```

---

## 🔍 Filtrera Log

### Begränsa antal

```bash
# Senaste 5 commits
git log -5

# Senaste 10
git log -n 10
```

### Filtrera på författare

```bash
# Specifik författare
git log --author="John"
git log --author="john@email.com"

# Flera författare (regex)
git log --author="John\|Jane"
```

### Filtrera på datum

```bash
# Efter datum
git log --after="2025-01-01"
git log --since="2 weeks ago"

# Före datum
git log --before="2025-12-01"
git log --until="yesterday"

# Intervall
git log --after="2025-01-01" --before="2025-06-01"
```

### Filtrera på innehåll

```bash
# Sök i commit-meddelanden
git log --grep="fix"
git log --grep="bug" --grep="error" --all-match

# Sök efter kod-ändringar
git log -S "function_name"  # Pickaxe
git log -G "regex_pattern"  # Regex

# Ändringar i specifik fil
git log -- path/to/file.js
git log --follow -- renamed-file.js  # Följer rename
```

---

## 📊 Log Formattering

### Inbyggda format

```bash
# Oneline
git log --oneline

# Short
git log --format=short

# Full
git log --format=full

# Fuller
git log --format=fuller
```

### Custom format

```bash
# Custom format
git log --pretty=format:"%h - %an, %ar : %s"
# abc123d - John Doe, 2 hours ago : Add feature

# Med färger
git log --pretty=format:"%C(yellow)%h%C(reset) %C(blue)%an%C(reset) %s"

# Användbara placeholders
# %H  - Full hash
# %h  - Short hash
# %an - Author name
# %ae - Author email
# %ar - Author date, relative
# %ad - Author date
# %s  - Subject (commit message)
# %b  - Body
```

### Statistik

```bash
# Ändrade filer
git log --stat

# Kort statistik
git log --shortstat

# Endast filnamn
git log --name-only

# Med status (A/M/D)
git log --name-status
```

---

## 🔎 Git Show

```bash
# Visa commit detaljer
git show abc123d

# Visa endast meddelande
git show abc123d --quiet

# Visa specifik fil i commit
git show abc123d:path/to/file.js

# Visa fil från annan branch
git show main:src/app.js
```

---

## 🏋️ Övningar

### Övning 1: Utforska historik
```bash
# I ett repo med historik
git log --oneline -20
git log --graph --all --oneline
git log --author="$(git config user.name)" --oneline
```

### Övning 2: Sök i historik
```bash
# Hitta commits som nämner "bug"
git log --grep="bug" --oneline

# Hitta när en funktion introducerades
git log -S "myFunction" --oneline
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git log | Visa historik |
| git log --oneline | Kompakt vy |
| git log --graph | Med branch-graf |
| git log -n | Begränsa antal |
| git log --author | Filtrera på författare |
| git log --grep | Sök i meddelanden |
| git log -S | Sök efter kodändringar |
| git show | Visa commit-detaljer |

**Nästa steg:** Ångra & Ändra i Git

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Ångra & Ändra i Git",
        "difficulty": "easy",
        "estimated_minutes": 55,
        "xp_reward": 130,
        "content": r"""
# ↩️ Ångra & Ändra i Git

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Ångra ändringar i working directory
- Unstage filer från staging area
- Ändra commits med amend
- Använda reset och revert

---

## 📖 Ångra i Working Directory

### git restore (Git 2.23+)

```bash
# Ångra ändringar i en fil
git restore file.txt

# Ångra alla ändringar
git restore .

# Ångra specifik fil till specifik commit
git restore --source=HEAD~2 file.txt
```

### Äldre syntax (fortfarande fungerar)

```bash
# Ångra ändringar
git checkout -- file.txt
git checkout -- .
```

---

## 📤 Unstage Filer

### git restore --staged

```bash
# Unstage en fil
git restore --staged file.txt

# Unstage alla
git restore --staged .
```

### git reset (alternativ)

```bash
# Unstage en fil
git reset HEAD file.txt

# Unstage alla
git reset HEAD
```

### Diagram: Ångra operationer

```
+-----------------------------------------------------------------+
|                     ÅNGRA OPERATIONER                           |
+-----------------------------------------------------------------+
|                                                                 |
|  Repository --------------------------------------------------  |
|       |                                                         |
|       | git reset --soft HEAD~1 (behåll staging)               |
|       | git reset HEAD~1 (unstage, behåll working)             |
|       | git reset --hard HEAD~1 (radera allt) ⚠️               |
|       ▼                                                         |
|  Staging ----------------------------------------------------   |
|       |                                                         |
|       | git restore --staged file.txt                          |
|       ▼                                                         |
|  Working ----------------------------------------------------   |
|       |                                                         |
|       | git restore file.txt                                   |
|       ▼                                                         |
|  (Ändringar borta)                                             |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## ✏️ Ändra Senaste Commit

### git commit --amend

```bash
# Ändra commit-meddelande
git commit --amend -m "Bättre meddelande"

# Lägg till glömd fil
git add forgotten-file.txt
git commit --amend --no-edit

# Ändra både meddelande och filer
git add more-changes.txt
git commit --amend -m "Updated commit"
```

### ⚠️ Varning om amend

```bash
# Amend skapar NY commit med ny hash
# Aldrig amend commits som är pushade!

# Före amend
abc123 Original commit

# Efter amend
def456 Amended commit  <- Ny hash!
```

---

## 🔄 Git Reset

### Tre lägen

```bash
# Soft: Flytta HEAD, behåll staging och working
git reset --soft HEAD~1

# Mixed (default): Flytta HEAD, unstage, behåll working
git reset HEAD~1
git reset --mixed HEAD~1

# Hard: Flytta HEAD, radera staging och working ⚠️
git reset --hard HEAD~1
```

### Praktiska exempel

```bash
# "Oj, jag commitade för tidigt"
git reset --soft HEAD~1
# Nu kan du fortsätta jobba och commita igen

# "Jag vill börja om med staging"
git reset HEAD~1
# Ändringar finns kvar, men unstaged

# "Radera allt och börja om" ⚠️
git reset --hard HEAD~1
# VARNING: Ändringar försvinner permanent!
```

### Reset vs Checkout

| Kommando | Påverkar HEAD | Påverkar Branch | Påverkar Working |
|----------|---------------|-----------------|------------------|
| reset --soft | ✅ | ✅ | ❌ |
| reset --mixed | ✅ | ✅ | ❌ |
| reset --hard | ✅ | ✅ | ✅ |
| checkout | ✅ | ❌ | ✅ |

---

## ⏪ Git Revert

### Säkert sätt att ångra

```bash
# Revert skapar NY commit som ångrar en gammal
git revert abc123

# Revert senaste commit
git revert HEAD

# Revert utan att öppna editor
git revert HEAD --no-edit

# Revert flera commits
git revert HEAD~3..HEAD --no-commit
git commit -m "Revert last 3 commits"
```

### Reset vs Revert

```bash
# Reset - ändrar historik (farligt för delade branches)
git reset --hard HEAD~1
# Historik: A -> B -> C -> D  blir  A -> B -> C

# Revert - lägger till ny commit (säkert)
git revert HEAD
# Historik: A -> B -> C -> D  blir  A -> B -> C -> D -> D'
# D' ångrar D
```

---

## 🆘 Återställ Förlorat Arbete

### Git Reflog

```bash
# Se alla HEAD-ändringar (livlina!)
git reflog

# Output:
# abc123d HEAD@{0}: commit: Add feature
# def456a HEAD@{1}: reset: moving to HEAD~1
# ghi789b HEAD@{2}: commit: Deleted commit (kan återställas!)

# Återställ
git reset --hard HEAD@{2}
# eller
git checkout -b recovered HEAD@{2}
```

---

## 🏋️ Övningar

### Övning 1: Ångra workflow
```bash
# Skapa test-miljö
mkdir undo-test && cd undo-test && git init
echo "Version 1" > file.txt && git add . && git commit -m "v1"
echo "Version 2" > file.txt && git add . && git commit -m "v2"
echo "Version 3" > file.txt && git add . && git commit -m "v3"

# Testa reset
git reset --soft HEAD~1
git status  # v3 ändringar staged

git reset HEAD~1
git status  # v2 ändringar i working

git reset --hard HEAD~1
git log --oneline  # Tillbaka till v1
```

### Övning 2: Rädda med reflog
```bash
# Efter hård reset - hitta förlorad commit
git reflog
git reset --hard HEAD@{1}  # Återställ
```

---

## 📚 Sammanfattning

| Scenario | Kommando |
|----------|----------|
| Ångra working changes | `git restore file.txt` |
| Unstage fil | `git restore --staged file.txt` |
| Ändra senaste commit | `git commit --amend` |
| Ångra commit (privat) | `git reset HEAD~1` |
| Ångra commit (delad) | `git revert HEAD` |
| Rädda förlorat | `git reflog` |

**Nästa steg:** Git Branching Basics

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Git Branching Basics",
        "difficulty": "easy",
        "estimated_minutes": 50,
        "xp_reward": 130,
        "content": r"""
# 🌿 Git Branching Basics

## Lärande mål
- Förstå vad branches är och varför de används
- Skapa, byta och ta bort branches
- Visualisera branch-struktur
- Förstå HEAD och branch-pekare

---

## 📖 Vad är en Branch?

En branch är en **pekare till en commit**. Det är allt!

```
+-----------------------------------------------------------------+
|                      BRANCHES                                   |
+-----------------------------------------------------------------+
|                                                                 |
|                          feature --+                            |
|                                    ▼                            |
|    +-----+    +-----+    +-----+    +-----+                    |
|    | A   |--->| B   |--->| C   |--->| D   |                    |
|    +-----+    +-----+    +-----+    +-----+                    |
|                            ▲          ▲                         |
|                            |          +-- HEAD                  |
|                          main                                   |
|                                                                 |
+-----------------------------------------------------------------+
```

### Varför Branches?

| Utan branches | Med branches |
|---------------|--------------|
| Alla jobbar på samma kod | Isolerade ändringar |
| Konflikter hela tiden | Merge när klart |
| Svårt att experimentera | Riskfri testning |
| En version i taget | Parallell utveckling |

---

## 🛠️ Hantera Branches

### Lista branches

```bash
# Lokala branches
git branch

# Alla branches (inkl. remote)
git branch -a

# Med senaste commit
git branch -v

# Merged/not merged
git branch --merged
git branch --no-merged
```

### Skapa branch

```bash
# Skapa branch (stannar på nuvarande)
git branch feature/login

# Skapa och byt till ny branch
git checkout -b feature/signup

# Nyare syntax (Git 2.23+)
git switch -c feature/payment

# Skapa från specifik commit
git branch bugfix/issue-42 abc123
```

### Byta branch

```bash
# Klassisk syntax
git checkout main

# Nyare syntax (rekommenderat)
git switch main

# Byt till föregående branch
git switch -
git checkout -
```

### Ta bort branch

```bash
# Ta bort merged branch
git branch -d feature/done

# Force delete (oavsett merge-status)
git branch -D feature/abandoned

# Ta bort remote branch
git push origin --delete feature/old
```

---

## 🧭 HEAD Förklarat

HEAD är en pekare till "var du är nu".

```bash
# Se vad HEAD pekar på
cat .git/HEAD
# ref: refs/heads/main

# Detached HEAD (pekar direkt på commit)
git checkout abc123
# HEAD pekar nu på commit, inte branch
```

### Detached HEAD State

```
+-----------------------------------------------------------------+
|                    DETACHED HEAD                                |
+-----------------------------------------------------------------+
|                                                                 |
|  Normal:         HEAD -> main -> commit C                        |
|                                                                 |
|  Detached:       HEAD -> commit B (direkt)                      |
|                  main -> commit C                                |
|                                                                 |
|    +-----+    +-----+    +-----+                               |
|    | A   |--->| B   |--->| C   |                               |
|    +-----+    +-----+    +-----+                               |
|                 ▲          ▲                                    |
|                HEAD       main                                  |
|                                                                 |
+-----------------------------------------------------------------+

# Fixa detached HEAD - skapa branch
git switch -c save-my-work
```

---

## 📊 Visualisera Branches

### git log --graph

```bash
# Enkel graf
git log --oneline --graph

# Alla branches
git log --oneline --graph --all

# Med branch-namn
git log --oneline --graph --all --decorate

# Alias
git config --global alias.tree "log --oneline --graph --all --decorate"
git tree
```

### Exempel output

```
* 2d3f4a5 (HEAD -> feature) Add tests
* 1b2c3d4 Add feature
| * 8e9f0a1 (main) Update README
|/
* 7c8d9e0 Initial commit
```

---

## 🔀 Branch Workflow

### Feature Branch Workflow

```bash
# 1. Börja från main
git switch main
git pull

# 2. Skapa feature branch
git switch -c feature/user-profile

# 3. Jobba och commita
git add .
git commit -m "Add user profile page"

# 4. Pusha till remote
git push -u origin feature/user-profile

# 5. Skapa PR / Merge (nästa lektion)
```

### Branch Naming Conventions

```bash
# Feature
feature/add-login
feature/user-dashboard

# Bugfix
bugfix/fix-header
bugfix/issue-123

# Hotfix
hotfix/security-patch

# Release
release/v1.2.0

# Experiment
experiment/new-algorithm
```

---

## 🏋️ Övningar

### Övning 1: Branch hantering
```bash
# Skapa repo
mkdir branch-test && cd branch-test && git init
echo "main" > file.txt && git add . && git commit -m "Initial"

# Skapa branches
git branch feature-a
git branch feature-b
git branch -v  # Lista alla

# Byt och commita
git switch feature-a
echo "feature a" >> file.txt && git commit -am "Add feature A"

git switch feature-b
echo "feature b" >> file.txt && git commit -am "Add feature B"

# Visualisera
git log --oneline --graph --all
```

### Övning 2: Rensa branches
```bash
# Hitta och ta bort merged branches
git branch --merged main | grep -v "main" | xargs git branch -d
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git branch | Lista branches |
| git branch name | Skapa branch |
| git switch name | Byt branch |
| git switch -c name | Skapa + byt |
| git branch -d name | Ta bort branch |
| git log --graph | Visualisera |

**Nästa steg:** Merging Branches

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Merging Branches",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 140,
        "content": r"""
# 🔀 Merging Branches

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå skillnaden mellan fast-forward och 3-way merge
- Utföra merges med `git merge`
- Lösa merge-konflikter
- Välja rätt merge-strategi

---

## 📖 Merge Typer

### Fast-Forward Merge

När target branch inte har nya commits:

```
FÖRE:
    main: A -> B -> C
                   ↘
    feature:        D -> E

EFTER git merge feature:
    main: A -> B -> C -> D -> E <- (fast-forward, inga merge commits)
```

```bash
# Fast-forward sker automatiskt om möjligt
git switch main
git merge feature/simple
# Fast-forward
```

### 3-Way Merge

När båda branches har unika commits:

```
FÖRE:
    main: A -> B -> C -> F
                   ↘
    feature:        D -> E

EFTER git merge feature:
    main: A -> B -> C -> F -> M (merge commit)
                   ↘   ↗
    feature:        D -> E
```

```bash
git switch main
git merge feature/complex
# Skapar merge commit
```

---

## 🛠️ Utföra Merge

### Grundläggande merge

```bash
# 1. Byt till target branch
git switch main

# 2. Merge source branch
git merge feature/login

# 3. Om konflikter - lös dem (nästa sektion)

# 4. Push
git push
```

### Merge options

```bash
# Tvinga merge commit (ingen fast-forward)
git merge --no-ff feature/login

# Squash alla commits till en
git merge --squash feature/login
git commit -m "Add login feature"

# Avbryt pågående merge
git merge --abort
```

### När använda --no-ff

```bash
# Fast-forward (svårt att se var feature började/slutade)
A -> B -> C -> D -> E -> F

# --no-ff (tydlig feature-historik)
A -> B -> C ---------> M
         ↘       ↗
          D -> E -> F
```

---

## ⚔️ Lösa Merge-Konflikter

### När uppstår konflikter?

```bash
# Samma rad ändrad i båda branches
# main: "Hello World"
# feature: "Hello Git"
```

### Konflikt-markers

```
<<<<<<< HEAD
Hello World
=======
Hello Git
>>>>>>> feature/greeting

# Förklaring:
# <<<<<<< HEAD     = Din nuvarande branch
# =======          = Separator
# >>>>>>> feature  = Inkommande branch
```

### Lösa konflikter

```bash
# 1. Se vilka filer som har konflikter
git status
# Both modified: greeting.txt

# 2. Öppna filen och redigera
# Ta bort markers, behåll rätt kod

# 3. Markera som löst
git add greeting.txt

# 4. Slutför merge
git commit -m "Merge feature/greeting, resolve conflicts"
```

### Verktyg för konfliktlösning

```bash
# Använd merge tool
git mergetool

# Konfigurera tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# VS Code har inbyggt stöd:
# "Accept Current" | "Accept Incoming" | "Accept Both"
```

---

## 📊 Merge vs Rebase

```bash
# Merge - bevarar historik
git merge feature/login
# Skapar merge commit, branch-historik intakt

# Rebase - linjär historik
git rebase main
# "Flyttar" commits, renare historik men ändrar commits
```

### Visualisering

```
MERGE:
main:    A -> B -> C ---------> M
              ↘           ↗
feature:       D -> E -> F

REBASE:
main:    A -> B -> C -> D' -> E' -> F'
              ↑
         (feature rebased)
```

---

## 🏋️ Övningar

### Övning 1: Fast-forward vs 3-way
```bash
mkdir merge-test && cd merge-test && git init
echo "initial" > file.txt && git add . && git commit -m "Initial"

# Fast-forward scenario
git switch -c feature-ff
echo "feature" >> file.txt && git commit -am "Add feature"
git switch main
git merge feature-ff  # Fast-forward!

# 3-way scenario
git switch -c feature-3way
echo "3way feature" >> file.txt && git commit -am "3way"
git switch main
echo "main change" >> other.txt && git add . && git commit -m "Main"
git merge feature-3way  # 3-way merge!
```

### Övning 2: Lösa konflikt
```bash
git switch -c conflict-a
echo "A version" > shared.txt && git commit -am "Version A"
git switch main
echo "Main version" > shared.txt && git commit -am "Main version"
git merge conflict-a  # Konflikt!
# Lös manuellt, git add, git commit
```

---

## 📚 Sammanfattning

| Typ | När | Resultat |
|-----|-----|----------|
| Fast-forward | Rak linje | Ingen merge commit |
| 3-way | Divergerade | Merge commit |
| --no-ff | Vill ha merge commit | Explicit merge |
| --squash | Rena upp | En commit |

**Nästa steg:** Remote Repositories

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Remote Repositories",
        "difficulty": "medium",
        "estimated_minutes": 50,
        "xp_reward": 135,
        "content": r"""
# 🌐 Remote Repositories

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå lokalt vs remote repository
- Hantera remotes med `git remote`
- Push och pull ändringar
- Tracking branches

---

## 📖 Lokalt vs Remote

```
+-----------------------------------------------------------------+
|                  LOCAL vs REMOTE                                |
+-----------------------------------------------------------------+
|                                                                 |
|   Din dator                          GitHub/GitLab              |
|  +------------------+              +------------------+        |
|  |  Local Repo      |    push -->  |  Remote Repo     |        |
|  |  .git/           |    <-- pull  |  origin          |        |
|  |                  |              |                  |        |
|  |  main            |              |  main            |        |
|  |  feature/login   |              |  feature/login   |        |
|  +------------------+              +------------------+        |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🔗 Hantera Remotes

### Lista remotes

```bash
# Enkel lista
git remote
# origin

# Med URL
git remote -v
# origin  git@github.com:user/repo.git (fetch)
# origin  git@github.com:user/repo.git (push)

# Detaljerad info
git remote show origin
```

### Lägga till remote

```bash
# Lägg till origin
git remote add origin git@github.com:user/repo.git

# Lägg till upstream (för forks)
git remote add upstream git@github.com:original/repo.git

# Flera remotes är vanligt
git remote -v
# origin    git@github.com:myuser/repo.git
# upstream  git@github.com:original/repo.git
```

### Ändra remote

```bash
# Ändra URL
git remote set-url origin git@github.com:newuser/repo.git

# Byt namn
git remote rename origin github

# Ta bort
git remote remove upstream
```

---

## ⬆️ Git Push

### Grundläggande push

```bash
# Push current branch
git push origin main

# Push med upstream tracking
git push -u origin main
# Nu räcker det med: git push

# Push alla branches
git push --all origin

# Push tags
git push --tags
```

### Push options

```bash
# Force push (⚠️ farligt!)
git push --force
git push -f

# Säkrare force push
git push --force-with-lease
# Misslyckas om någon annan pushat

# Delete remote branch
git push origin --delete feature/old
```

### Push workflow

```bash
# Typiskt workflow
git switch -c feature/new-thing
# ... jobba ...
git add . && git commit -m "Add thing"
git push -u origin feature/new-thing
# Skapa PR på GitHub
```

---

## ⬇️ Git Pull & Fetch

### git fetch

```bash
# Hämta ändringar utan merge
git fetch origin

# Hämta alla remotes
git fetch --all

# Se vad som hämtades
git log origin/main --oneline
```

### git pull

```bash
# Fetch + merge
git pull origin main

# Pull med rebase
git pull --rebase origin main

# Konfigurera default
git config --global pull.rebase true
```

### Fetch vs Pull

```
FETCH:
Local:  A -> B -> C (main)
Remote: A -> B -> C -> D -> E (origin/main)
Efter fetch: origin/main uppdaterad, main oförändrad

PULL:
Local:  A -> B -> C -> D -> E (main, mergad)
```

---

## 🔗 Tracking Branches

### Vad är tracking?

```bash
# Tracking = koppling mellan lokal och remote branch
git branch -vv
# * main    abc123 [origin/main] Latest commit
#   feature def456 [origin/feature: ahead 2] Local changes
```

### Sätta tracking

```bash
# Vid push
git push -u origin feature/new

# Manuellt
git branch --set-upstream-to=origin/main main

# Kortare
git branch -u origin/main
```

### Tracking status

```bash
# Se status
git status
# Your branch is ahead of 'origin/main' by 2 commits.

# Detaljerad
git branch -vv
# ahead 2, behind 3 = du har 2 lokala, remote har 3 du saknar
```

---

## 🔄 Synkronisera

### Typiskt sync-workflow

```bash
# 1. Hämta senaste
git fetch origin

# 2. Se status
git status
# Your branch is behind 'origin/main' by 3 commits

# 3. Merge eller rebase
git pull --rebase  # Rekommenderat för feature branches
# eller
git merge origin/main

# 4. Push dina ändringar
git push
```

### Hantera "behind"

```bash
# Du är bakom remote
git pull --rebase origin main
# Dina lokala commits "flyttas" ovanpå remote

# Vid konflikter under rebase
git add .
git rebase --continue
# eller
git rebase --abort
```

---

## 🏋️ Övningar

### Övning 1: Remote setup
```bash
# Skapa repo på GitHub först
# Sedan lokalt:
mkdir my-project && cd my-project
git init
echo "# My Project" > README.md
git add . && git commit -m "Initial commit"
git remote add origin git@github.com:user/my-project.git
git push -u origin main
```

### Övning 2: Sync workflow
```bash
# Simulera team-arbete
# Gör ändringar på GitHub (Edit on GitHub)
# Lokalt:
git fetch origin
git status  # Behind by 1
git pull
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git remote -v | Lista remotes |
| git remote add | Lägg till remote |
| git push | Skicka till remote |
| git push -u | Push + set tracking |
| git fetch | Hämta utan merge |
| git pull | Fetch + merge |
| git pull --rebase | Fetch + rebase |

**Nästa steg:** GitHub Workflow

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "GitHub Workflow",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 145,
        "content": r"""
# 🐙 GitHub Workflow

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Konfigurera SSH för GitHub
- Förstå Fork & Clone workflow
- Skapa och hantera Pull Requests
- Använda GitHub CLI

---

## 🔐 SSH Setup

### Generera SSH-nyckel

```bash
# Skapa nyckel (Ed25519 rekommenderas)
ssh-keygen -t ed25519 -C "din.email@example.com"

# Eller RSA för äldre system
ssh-keygen -t rsa -b 4096 -C "din.email@example.com"

# Acceptera default location (~/.ssh/id_ed25519)
# Välj passphrase (rekommenderat)
```

### Lägga till i ssh-agent

```bash
# Starta ssh-agent
eval "$(ssh-agent -s)"

# Lägg till nyckel
ssh-add ~/.ssh/id_ed25519

# macOS: Lägg till i Keychain
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

### Lägg till på GitHub

```bash
# Kopiera public key
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip   # Linux

# Eller visa och kopiera manuellt
cat ~/.ssh/id_ed25519.pub
```

1. Gå till GitHub -> Settings -> SSH and GPG keys
2. Klicka "New SSH key"
3. Klistra in public key
4. Testa: `ssh -T git@github.com`

---

## 🍴 Fork Workflow

### När använda Fork?

- Bidra till open source
- Ingen write access till original repo
- Experimentera utan att påverka original

### Fork workflow

```bash
# 1. Fork på GitHub (klicka Fork-knappen)

# 2. Clone din fork
git clone git@github.com:YOUR-USERNAME/repo.git
cd repo

# 3. Lägg till upstream
git remote add upstream git@github.com:ORIGINAL/repo.git

# 4. Håll synkad
git fetch upstream
git switch main
git merge upstream/main

# 5. Jobba på feature branch
git switch -c my-feature
# ... ändringar ...
git push origin my-feature

# 6. Skapa PR från din fork till original
```

---

## 📝 Pull Requests

### Skapa PR via webben

1. Push din branch till GitHub
2. Gå till repo på GitHub
3. Klicka "Compare & pull request"
4. Fyll i:
   - Titel (tydlig beskrivning)
   - Beskrivning (vad/varför/hur)
   - Reviewers
   - Labels

### PR Best Practices

```markdown
## Description
Brief description of what this PR does.

## Changes
- Added user authentication
- Updated login UI
- Fixed password validation bug

## Testing
- [ ] Unit tests pass
- [ ] Manual testing done
- [ ] No regressions

## Screenshots (if UI changes)
Before | After
-------|------
img    | img

## Related Issues
Closes #123
Fixes #456
```

### Hantera PR Feedback

```bash
# Efter review comments - gör ändringar
git add .
git commit -m "Address review feedback"
git push

# Squash commits före merge (optional)
git rebase -i main
# Ändra 'pick' till 'squash' för commits du vill slå ihop
git push --force-with-lease
```

---

## 💻 GitHub CLI (gh)

### Installation

```bash
# macOS
brew install gh

# Ubuntu
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh

# Auth
gh auth login
```

### Repo operations

```bash
# Skapa repo
gh repo create my-project --public --source=. --push

# Clone
gh repo clone owner/repo

# Fork + clone
gh repo fork owner/repo --clone

# View
gh repo view
gh repo view --web  # Öppna i browser
```

### PR operations

```bash
# Skapa PR
gh pr create --title "Add feature" --body "Description"

# Skapa interaktivt
gh pr create

# Lista PRs
gh pr list
gh pr list --state=all

# View/checkout PR
gh pr view 123
gh pr checkout 123

# Review
gh pr review 123 --approve
gh pr review 123 --comment -b "Looks good!"
gh pr review 123 --request-changes -b "Please fix X"

# Merge
gh pr merge 123 --squash
gh pr merge 123 --merge
gh pr merge 123 --rebase
```

### Issue operations

```bash
# Skapa issue
gh issue create --title "Bug" --body "Description"

# Lista
gh issue list
gh issue list --label="bug"

# Close
gh issue close 123
```

---

## 🏋️ Övningar

### Övning 1: SSH Setup
```bash
# Generera nyckel
ssh-keygen -t ed25519 -C "email"
# Lägg till på GitHub
# Testa
ssh -T git@github.com
```

### Övning 2: PR Workflow
```bash
# Fork ett test-repo
gh repo fork octocat/Spoon-Knife --clone
cd Spoon-Knife
git switch -c my-change
echo "My contribution" >> README.md
git commit -am "Add contribution"
git push origin my-change
gh pr create
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| ssh-keygen | Skapa SSH-nyckel |
| gh repo create | Skapa repo |
| gh pr create | Skapa PR |
| gh pr checkout | Checkout PR lokalt |
| gh pr merge | Merge PR |
| gh issue create | Skapa issue |

**Nästa steg:** Advanced Git

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
]
