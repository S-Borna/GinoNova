"""
NOD 3.4: Git Basics
===================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 3: DEVOPS
SISTA NODEN I MODUL 3 - DEVOPS KOMPLETT!
"""

GIT_BASICS_NODE = {
    "title": "Git Basics",
    "slug": "git-basics",
    "description": "Versionshantering med Git - grundläggande kommandon, branching och samarbete.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "order_index": 4,
    "content": r"""# Git Basics

> **TL;DR:** `git add .` → `git commit -m "msg"` → `git push`. Branch för features, merge via Pull Request!

---

## 📖 TEORI: Vad är Git?

**Git** = Distribuerat versionshanteringssystem
- Spårar ändringar i filer över tid
- Möjliggör samarbete mellan utvecklare
- **Distribuerat** = full historik lokalt
- Standard i ALL modern utveckling

### Varför Git?

| Egenskap | Fördel |
|----------|--------|
| Distribuerat | Full historik lokalt, funkar offline |
| Snabbt | De flesta operationer lokala |
| Branching | Billigt och enkelt att skapa branches |
| Säkert | SHA-1 checksums på allt |

---

## 📖 Grundläggande koncept

### Viktiga begrepp

| Begrepp | Beskrivning |
|---------|-------------|
| Repository (repo) | Projektmapp med .git-katalog |
| Commit | Sparad ögonblicksbild av ändringar |
| Branch | Parallell utvecklingslinje |
| Remote | Fjärrserver (GitHub, GitLab) |
| Clone | Kopiera repo från remote |
| Push | Skicka commits till remote |
| Pull | Hämta commits från remote |
| Merge | Sammanfoga branches |

### De tre tillstånden (KRITISKT!)

```
┌──────────────────┐    git add    ┌─────────────────┐   git commit   ┌──────────────┐
│ Working Directory│ ────────────► │  Staging Area   │ ─────────────► │  Repository  │
│   (ändringar)    │               │  (förberett)    │                │  (.git)      │
└──────────────────┘               └─────────────────┘                └──────────────┘
        │                                   │                                │
   Otrackade/                          Staged                          Committad
   Modifierade                        (redo för                        (permanent
      filer                            commit)                          historik)
```

---

## 📖 Konfigurera Git (första gången)

```bash
# Sätt namn och email (MÅSTE göras)
git config --global user.name "Said"
git config --global user.email "said@example.com"

# Sätt default branch till main
git config --global init.defaultBranch main

# Visa konfiguration
git config --list
```

---

## 📖 Skapa och klona repo

### Skapa nytt repo

```bash
# I befintlig katalog
cd mitt-projekt
git init

# Skapa ny katalog med repo
git init mitt-projekt
```

### Klona befintligt repo

```bash
# HTTPS (kräver username/password)
git clone https://git.chas-lab.dev/user/repo.git

# SSH (kräver SSH-nyckel)
git clone git@git.chas-lab.dev:user/repo.git

# Klona till specifik katalog
git clone https://... min-katalog
```

---

## 📖 Dagligt arbetsflöde

### Status - vad har ändrats?

```bash
# Visa status (ANVÄND OFTA!)
git status

# Kortversion
git status -s
```

### Add - lägg till i staging

```bash
# Lägg till specifik fil
git add filnamn.txt

# Lägg till alla filer i katalog
git add .

# Lägg till alla (inkl borttagna)
git add -A

# Interaktiv add
git add -p
```

### Commit - spara ändringar

```bash
# Commit med meddelande
git commit -m "Add login functionality"

# Kombinera add + commit (ENDAST spårade filer!)
git commit -am "Fix bug in login"

# Ändra senaste commit-meddelande
git commit --amend -m "Nytt meddelande"
```

### Visa historik

```bash
# Full historik
git log

# Kompakt (en rad per commit)
git log --oneline

# Med branch-graf
git log --oneline --graph --all

# Senaste N commits
git log -5
```

---

## 📖 Synka med remote

### Hantera remotes

```bash
# Lägg till remote
git remote add origin https://git.chas-lab.dev/user/repo.git

# Visa remotes
git remote -v

# Ta bort remote
git remote remove origin
```

### Push - skicka till remote

```bash
# Pusha till remote
git push origin main

# Första gången - sätt upstream
git push -u origin main

# Efter -u räcker:
git push
```

### Pull - hämta från remote

```bash
# Hämta och merga (vanligast)
git pull

# Bara hämta (ingen merge)
git fetch

# Pull med rebase (renare historik)
git pull --rebase
```

---

## 📖 Branching (VIKTIGT FÖR GRUPPROJEKT!)

### Skapa och byta branch

```bash
# Skapa branch
git branch feature-login

# Byta branch
git checkout feature-login
git switch feature-login        # Nyare syntax

# Skapa OCH byta i ett steg
git checkout -b feature-login
git switch -c feature-login     # Nyare syntax
```

### Lista och ta bort branches

```bash
# Lista lokala branches
git branch

# Lista alla (inkl remote)
git branch -a

# Ta bort branch (säker)
git branch -d feature-login

# Tvinga bort (även om ej merged)
git branch -D feature-login
```

### Merge - sammanfoga branches

```bash
# Stå på main, merga in feature
git checkout main
git merge feature-login

# Efter merge, ta bort feature-branch
git branch -d feature-login
```

### Merge-konflikter

```bash
# Vid konflikt visar Git:
<<<<<<< HEAD
din kod
=======
andras kod
>>>>>>> feature-login

# Lös konflikten:
# 1. Redigera filen, ta bort konfliktmarkörer
# 2. git add filnamn
# 3. git commit
```

---

## 📖 Pull/Merge Requests (GitLab/GitHub)

> "Pull requests are used to review changes before merging into the main branch"

### Workflow

```
1. Skapa feature-branch
   git checkout -b feature/user-setup

2. Gör ändringar, committa
   git add .
   git commit -m "Add user setup"

3. Pusha branch till remote
   git push -u origin feature/user-setup

4. Skapa Pull/Merge Request i GitLab
   - Välj source branch (feature/user-setup)
   - Välj target branch (main)
   - Skriv beskrivning
   - Tilldela reviewers

5. Kodgranskning
   - Reviewers kommenterar
   - Du gör eventuella ändringar
   - Push nya commits

6. Merge till main (i GitLab)
   - "Merge" knappen

7. Uppdatera lokal main
   git checkout main
   git pull
```

---

## 📖 .gitignore

### Filer som INTE ska spåras

```bash
# .gitignore

# Loggfiler
*.log

# Dependencies
node_modules/
__pycache__/
.venv/

# Secrets!
.env
*.pem
*.key

# OS-filer
.DS_Store
Thumbs.db

# Build-output
/dist/
/build/
*.pyc

# IDE
.idea/
.vscode/
```

### Tips

```bash
# Visa ignorerade filer
git status --ignored

# Sluta spåra fil (men behåll lokalt)
git rm --cached filnamn
```

---

## 📖 Ångra ändringar

### Working directory

```bash
# Ångra ändringar i fil (före add)
git checkout -- filnamn
git restore filnamn           # Nyare syntax

# Ångra ALLA ändringar
git checkout -- .
git restore .
```

### Staging area

```bash
# Ta bort från staging (behåll ändring)
git reset HEAD filnamn
git restore --staged filnamn  # Nyare syntax
```

### Commits

```bash
# Ångra senaste commit (behåll ändringar som staged)
git reset --soft HEAD~1

# Ångra senaste commit (behåll ändringar som unstaged)
git reset HEAD~1

# Ångra senaste commit (KASTA ändringar!)
git reset --hard HEAD~1
```

---

## 📖 Se skillnader

```bash
# Working vs staged
git diff

# Staged vs senaste commit
git diff --staged
git diff --cached

# Mellan commits
git diff abc123 def456

# Mellan branches
git diff main feature-login

# Specifik fil
git diff filnamn
```

---

## 📖 SSH-nycklar för Git

### Generera nyckel

```bash
# Ed25519 (rekommenderat)
ssh-keygen -t ed25519 -C "said@example.com"

# RSA (äldre alternativ)
ssh-keygen -t rsa -b 4096 -C "said@example.com"
```

### Lägg till i GitLab/GitHub

```bash
# Visa publik nyckel
cat ~/.ssh/id_ed25519.pub

# Kopiera och lägg till i:
# GitLab: Settings → SSH Keys
# GitHub: Settings → SSH and GPG keys
```

### Testa anslutning

```bash
ssh -T git@git.chas-lab.dev
ssh -T git@github.com
ssh -T git@gitlab.com
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Nytt projekt från scratch

```bash
# 1. Skapa projektmapp
mkdir mitt-projekt
cd mitt-projekt

# 2. Initiera Git
git init

# 3. Skapa filer
echo "# Mitt Projekt" > README.md
echo "node_modules/" > .gitignore

# 4. Första commit
git add .
git commit -m "Initial commit"

# 5. Lägg till remote
git remote add origin https://git.chas-lab.dev/user/mitt-projekt.git

# 6. Pusha
git push -u origin main
```

### Exempel 2: Klona och arbeta med grupprojekt

```bash
# 1. Klona
git clone https://git.chas-lab.dev/grupp3/linux-projekt.git
cd linux-projekt

# 2. Skapa feature-branch
git checkout -b feature/user-setup

# 3. Gör ändringar
nano setup-users.sh
git add setup-users.sh
git commit -m "Add user setup script"

# 4. Pusha till remote
git push -u origin feature/user-setup

# 5. [Skapa Merge Request i GitLab]

# 6. Efter merge - uppdatera lokal main
git checkout main
git pull

# 7. Ta bort lokal feature-branch
git branch -d feature/user-setup
```

### Exempel 3: Hantera merge-konflikt

```bash
# 1. Försök merga
git checkout main
git merge feature-login

# 2. KONFLIKT! Git säger:
# CONFLICT (content): Merge conflict in app.py
# Automatic merge failed

# 3. Öppna filen, fixa konflikten
nano app.py
# Ta bort <<<<<<< ======= >>>>>>>
# Behåll rätt kod

# 4. Markera som löst
git add app.py

# 5. Slutför merge
git commit -m "Merge feature-login, resolve conflict"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | git add . gör? | Lägger till alla filer i staging |
| 2 | git commit -m gör? | Sparar staging till repository |
| 3 | git push gör? | Skickar commits till remote |
| 4 | git pull gör? | Hämtar och mergar från remote |
| 5 | git checkout -b feature gör? | Skapar och byter till ny branch |
| 6 | git status visar? | Vilka filer som ändrats/staged |
| 7 | git log --oneline visar? | Kompakt commit-historik |
| 8 | git diff visar? | Skillnader mot staged/commit |
| 9 | git reset --soft HEAD~1 gör? | Ångrar commit, behåller ändringar |
| 10 | .gitignore används för? | Filer som EJ ska spåras |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är Git?**
- A) En texeditor
- B) Distribuerat versionshanteringssystem ✅
- C) Ett programmeringsspråk
- D) En webbserver

**2. Vilka är de tre tillstånden?**
- A) Add, Commit, Push
- B) Working Directory, Staging Area, Repository ✅
- C) Local, Remote, Cloud
- D) Branch, Merge, Pull

**3. Vilket kommando lägger till filer i staging?**
- A) git commit
- B) git add ✅
- C) git push
- D) git stage

**4. Hur skapar OCH byter du till ny branch?**
- A) git branch -c
- B) git checkout -b ✅
- C) git new branch
- D) git switch

**5. Vad gör git pull?**
- A) Bara hämtar
- B) Bara mergar
- C) Hämtar OCH mergar ✅
- D) Pushar

**6. Var ska .env-filer finnas?**
- A) I alla commits
- B) I .gitignore ✅
- C) I remote
- D) I staging

**7. Hur ångrar du senaste commit (behåll ändringar)?**
- A) git undo
- B) git reset --soft HEAD~1 ✅
- C) git revert
- D) git rollback

**8. Vad betyder -u i git push -u origin main?**
- A) Update
- B) Sätter upstream (tracking) ✅
- C) User
- D) Undo

**9. Hur visar du alla branches (inkl remote)?**
- A) git branch
- B) git branch -a ✅
- C) git branch -r
- D) git branches

**10. Vad är en Pull/Merge Request?**
- A) Automatisk merge
- B) Begäran om kodgranskning före merge ✅
- C) Hämta från remote
- D) Skapa branch

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande workflow
```bash
# 1. Skapa testmapp
mkdir /tmp/git-test && cd /tmp/git-test
git init

# 2. Konfigurera (om ej gjort)
git config user.name "Test"
git config user.email "test@test.com"

# 3. Skapa fil
echo "Hello Git" > hello.txt

# 4. Kolla status
git status

# 5. Lägg till och committa
git add hello.txt
git commit -m "Add hello.txt"

# 6. Visa historik
git log --oneline

# 7. Städa
cd && rm -rf /tmp/git-test
```

### Övning 2: Branching
```bash
# 1. Skapa repo
mkdir /tmp/branch-test && cd /tmp/branch-test
git init
echo "main content" > file.txt
git add . && git commit -m "Initial"

# 2. Skapa feature-branch
git checkout -b feature-x

# 3. Gör ändring på branch
echo "feature content" >> file.txt
git add . && git commit -m "Add feature"

# 4. Tillbaka till main
git checkout main
cat file.txt  # Bara "main content"

# 5. Merga
git merge feature-x
cat file.txt  # Nu finns båda

# 6. Ta bort branch
git branch -d feature-x

# 7. Städa
cd && rm -rf /tmp/branch-test
```

### Övning 3: Diff och ångra
```bash
# 1. Skapa repo
mkdir /tmp/diff-test && cd /tmp/diff-test
git init
echo "original" > test.txt
git add . && git commit -m "Initial"

# 2. Gör ändring
echo "ändring" >> test.txt

# 3. Se diff
git diff

# 4. Ångra (restore)
git restore test.txt
cat test.txt  # Bara "original"

# 5. Ny ändring + stage
echo "ny rad" >> test.txt
git add test.txt

# 6. Se staged diff
git diff --staged

# 7. Unstage
git restore --staged test.txt
git status

# 8. Städa
cd && rm -rf /tmp/diff-test
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Committa .env | Läcker secrets | Lägg i .gitignore FÖRST |
| Push till main direkt | Ingen review | Använd branches + MR |
| git reset --hard | Förlorar ändringar | Använd --soft |
| Glömma pull före push | Rejected push | git pull först |

---

## 📝 SAMMANFATTNING

```bash
# KONFIGURERA
git config --global user.name "Namn"
git config --global user.email "email@example.com"

# SKAPA/KLONA
git init                          # Nytt repo
git clone URL                     # Klona

# DAGLIGT ARBETE
git status                        # Vad har ändrats?
git add .                         # Stage alla
git commit -m "meddelande"        # Committa
git push                          # Skicka till remote
git pull                          # Hämta från remote

# BRANCHING
git checkout -b feature-x         # Skapa + byt
git checkout main                 # Byt till main
git merge feature-x               # Merga in
git branch -d feature-x           # Ta bort

# HISTORIK
git log --oneline                 # Kompakt historik
git diff                          # Visa ändringar

# ÅNGRA
git restore filnamn               # Ångra working dir
git restore --staged filnamn      # Unstage
git reset --soft HEAD~1           # Ångra commit

# WORKFLOW FÖR GRUPPROJEKT
1. git checkout -b feature/namn
2. Koda, git add, git commit
3. git push -u origin feature/namn
4. Skapa Merge Request i GitLab
5. Kodgranskning
6. Merge
7. git checkout main && git pull
```

"""
}

