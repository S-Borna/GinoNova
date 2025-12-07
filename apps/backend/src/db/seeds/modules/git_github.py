"""
Git & GitHub Mastery - Docker-style V3
========================================

20 noder med Docker-style formatering:
- Unicode-separatorer
- Tabeller for struktur
- ASCII-diagram
- Key Takeaways som tabell
- Kom ihag som bullet-lista
- Svenska utan emojis
"""

MODULE = {
    "name": "Git & GitHub Mastery",
    "slug": "git-github-mastery",
    "description": "Beharska versionskontroll med Git och samarbete via GitHub",
    "icon": "git-branch",
    "difficulty": "beginner",
    "estimated_hours": 25,
    "tasks": [
        {
            "title": "Git Fundamentals & Architecture",
            "slug": "git-fundamentals-architecture",
            "difficulty": "beginner",
            "content": """
# Git Fundamentals & Architecture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan Git-forstaelse           | Med Git-forstaelse            |
|---------------------------|-------------------------------|-------------------------------|
| Merge-konflikt            | Forlorar kod, gamlingar       | Loser snabbt, bevarar allt    |
| Misstag i kod             | Manuell rollback, kaos        | git revert pa sekunder        |
| Team-samarbete            | Overskrivna filer             | Clean branch-workflow         |
| Deployment                | "Vilken version ar live?"     | Tags och releases             |

Git ar fundamentet for ALL modern DevOps - CI/CD, GitOps, Infrastructure as Code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Gits Arkitektur

Git ar ett DISTRIBUERAT versionskontrollsystem - varje klon ar ett komplett repo.

```
┌─────────────────────────────────────────────────────────────────┐
│                         GIT WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    git add    ┌──────────────┐   git commit   │
│  │   Working    │ ────────────► │   Staging    │ ────────────►  │
│  │  Directory   │               │    Area      │                │
│  │              │               │   (Index)    │                │
│  │  Dina filer  │               │ Forberedelse │   ┌─────────┐  │
│  │  pa disk     │               │              │   │  .git/  │  │
│  └──────────────┘               └──────────────┘   │  Repo   │  │
│         ▲                                          └─────────┘  │
│         │                  git checkout/restore                 │
│         └───────────────────────────────────────────────────────│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Gits fyra objekttyper:**

| Objekttyp | Beskrivning                    | Exempel                        |
|-----------|--------------------------------|--------------------------------|
| blob      | Filinnehall (ingen metadata)   | Innehallet i app.js            |
| tree      | Katalogstruktur                | Pekar pa blobs och andra trees |
| commit    | Snapshot med metadata          | Author, datum, meddelande      |
| tag       | Namngiven pekare               | v1.0.0 pekar pa en commit      |

Allt identifieras med SHA-1 hashar (40 tecken). Samma innehall = samma hash.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Git-kommandon

```bash
# Installera Git (Ubuntu/Debian)
sudo apt update                      # Uppdaterar paketlistor
sudo apt install git -y              # Installerar Git

# Verifiera installation
git --version                        # Visar installerad version (t.ex. git version 2.43.0)

# Konfigurera användaridentitet (obligatoriskt för commits)
git config --global user.name "Ditt Namn"    # Sätter namn globalt
git config --global user.email "din@email.se"  # Sätter email globalt

# Visa all konfiguration
git config --list                    # Listar alla inställningar
git config --global --list           # Endast globala inställningar

# Skapa nytt repository
mkdir mitt-projekt                   # Skapar projektkatalog
cd mitt-projekt                      # Går in i katalogen
git init                             # Initierar tomt Git-repo, skapar .git/

# Klona befintligt repository
git clone https://github.com/user/repo.git  # Klonar remote repo lokalt
git clone git@github.com:user/repo.git      # Klonar via SSH (rekommenderat)
```

---

## Förstå .git-katalogen

```bash
# Utforska .git-strukturen
ls -la .git/                         # Visar innehållet i .git

# Viktiga filer och kataloger:
# .git/config      - Repo-specifik konfiguration
# .git/HEAD        - Pekare till aktuell branch
# .git/objects/    - Alla Git-objekt (blobs, trees, commits)
# .git/refs/       - Branch- och tag-pekare
# .git/index       - Staging area

# Se vad HEAD pekar på
cat .git/HEAD                        # Visar: ref: refs/heads/main

# Se vilken commit main pekar på
cat .git/refs/heads/main             # Visar commit-hash (40 tecken)

# Inspektera ett Git-objekt
git cat-file -t abc123               # Visar objekttyp (blob/tree/commit)
git cat-file -p abc123               # Visar objektinnehåll
```

---

## Staging och Commits

```bash
# Skapa en testfil
echo "Hello Git" > hello.txt         # Skapar fil med innehåll

# Kontrollera status
git status                           # Visar untracked files (röd)

# Lägg till i staging area
git add hello.txt                    # Stagar specifik fil
git add .                            # Stagar alla ändringar i aktuell katalog
git add -A                           # Stagar ALLT (även borttagna filer)

# Kontrollera status igen
git status                           # Visar staged files (grön)

# Se vad som är stagat
git diff --staged                    # Visar diff mellan staging och senaste commit

# Skapa commit
git commit -m "Add hello.txt"        # Skapar commit med meddelande

# Genväg: stage + commit i ett steg (endast trackade filer)
git commit -am "Update hello.txt"    # -a stagar alla modifierade trackade filer
```

---

## Visa historik

```bash
# Visa commit-logg
git log                              # Fullstandig logg
git log --oneline                    # Kompakt vy, en rad per commit
git log --graph                      # Visar branch-graf
git log --oneline --graph --all      # Kompakt graf for alla branches

# Visa specifik commit
git show abc123                      # Visar commit-detaljer och diff
git show HEAD                        # Visar senaste commit
git show HEAD~1                      # Visar nast senaste commit (1 steg bakat)
git show HEAD~3                      # 3 commits bakat

# Visa andringar for en fil
git log -p hello.txt                 # Logg med patches for filen
git log --follow hello.txt           # Foljer filhistorik aven vid rename
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## .git-katalogen

```
┌─────────────────────────────────────────────────────────────────┐
│                      .git/ STRUKTUR                             │
├─────────────────────────────────────────────────────────────────┤
│  .git/                                                          │
│  ├── config         Repo-specifik konfiguration                 │
│  ├── HEAD           Pekare till aktuell branch                  │
│  ├── index          Staging area (binarfil)                     │
│  ├── objects/       Alla Git-objekt (blobs, trees, commits)     │
│  │   ├── ab/        Objekt med hash som borjar "ab"             │
│  │   └── pack/      Packade objekt (optimering)                 │
│  └── refs/          Branch- och tag-pekare                      │
│      ├── heads/     Lokala branches                             │
│      ├── remotes/   Remote tracking branches                    │
│      └── tags/      Taggar                                      │
└─────────────────────────────────────────────────────────────────┘
```

```bash
# Inspektera .git
cat .git/HEAD                        # Visar: ref: refs/heads/main
cat .git/refs/heads/main             # Visar commit-hash (40 tecken)
git cat-file -t abc123               # Visar objekttyp (blob/tree/commit)
git cat-file -p abc123               # Visar objektinnehall
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Distribuerat              | Varje klon ar ett komplett repository               |
| Tre omraden               | Working Directory - Staging Area - Repository       |
| SHA-1 hashar              | 40 tecken, identifierar allt, ger integritet        |
| git add                   | Flyttar andringar till staging                      |
| git commit                | Sparar staging till repository                      |
| .git/                     | Innehaller HELA repositoryts data och historik      |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Git ar distribuerat - du har ALLTID full historik lokalt
- Staging area lat dig valja exakt vad som ska committas
- Commit ofta, push regelbundet, pull innan du borjar arbeta
- Forsta .git-strukturen = forsta hur Git fungerar
- Samma innehall = samma hash (deduplicering)
""",
        },
        {
            "title": "Branching & Merging",
            "slug": "branching-merging",
            "difficulty": "beginner",
            "content": """
# Branching & Merging

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan branching              | Med branching                 |
|---------------------------|------------------------------|-------------------------------|
| Ny feature                | Jobbar pa main, blockar alla | Isolerad branch, parallellt   |
| Buggfix akut              | Maste vanta pa features      | Hotfix-branch direkt          |
| Experiment                | Risk att forstora main       | Branch, testa, kasta om fel   |
| Code review               | Ingen struktur               | PR fran branch, review, merge |

Branching ar det som gor Git overlaget. Det kostar INGENTING att skapa en branch.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hur Branching Fungerar

```
┌─────────────────────────────────────────────────────────────────┐
│                      BRANCH = PEKARE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  En branch ar BARA en 41-byte fil med en commit-hash!           │
│                                                                 │
│      ┌────────┐                                                 │
│      │  HEAD  │ ◄── Vilken branch du ar pa                      │
│      └───┬────┘                                                 │
│          │                                                      │
│          ▼                                                      │
│      ┌────────┐        ┌────────┐        ┌────────┐            │
│      │  main  │───────►│ commit │◄───────│feature │            │
│      └────────┘        │  C3    │        └────────┘            │
│                        └───┬────┘                               │
│                            │                                    │
│                        ┌───▼────┐        ┌────────┐            │
│                        │ commit │◄───────│ commit │            │
│                        │  C2    │        │  C4    │            │
│                        └───┬────┘        └────────┘            │
│                            │               (feature)            │
│                        ┌───▼────┐                               │
│                        │ commit │                               │
│                        │  C1    │                               │
│                        └────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Merge-strategier:**

| Strategi        | Nar                           | Resultat                      |
|-----------------|-------------------------------|-------------------------------|
| Fast-forward    | Malet har inte divergerat     | Flyttar bara pekaren          |
| Three-way merge | Bada branches har commits     | Skapar merge-commit           |
| Squash merge    | Vill ha clean historik        | En commit med alla andringar  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa och Hantera Branches

```bash
# Lista branches
git branch                           # Visar lokala branches, * markerar aktiv
git branch -a                        # Visar även remote branches
git branch -v                        # Visar senaste commit för varje branch

# Skapa ny branch
git branch feature-login             # Skapar branch från HEAD
git branch feature-api abc123        # Skapar branch från specifik commit

# Byta branch
git checkout feature-login           # Byter till branch (gammalt sätt)
git switch feature-login             # Byter till branch (nytt, rekommenderat)

# Skapa och byt i ett steg
git checkout -b feature-signup       # Skapar och byter (gammalt)
git switch -c feature-signup         # Skapar och byter (nytt)

# Byta namn på branch
git branch -m old-name new-name      # Byter namn på branch
git branch -m new-name               # Byter namn på aktiv branch

# Ta bort branch
git branch -d feature-done           # Tar bort (endast om merged)
git branch -D feature-abandoned      # Tvingar borttagning
```

---

## Merging

```bash
# Förberedelse: gå till målbranch
git switch main                      # Byt till main

# Merge feature-branch in i main
git merge feature-login              # Mergar feature-login in i main

# Om fast-forward är möjligt sker det automatiskt
# Om inte skapas en merge-commit

# Tvinga merge-commit (även vid fast-forward)
git merge --no-ff feature-login      # Skapar alltid merge-commit

# Avbryt pågående merge (vid konflikter)
git merge --abort                    # Återställer till före merge

# Se vilka branches som är mergade
git branch --merged                  # Branches som är mergade i HEAD
git branch --no-merged               # Branches som INTE är mergade
```

---

## Hantera merge-konflikter

```bash
# Vid konflikt visar git status vilka filer som är i konflikt
git status                           # Visar "both modified: filnamn"

# Öppna filen och leta efter konfliktmarkörer:
# <<<<<<< HEAD
# Din kod (current branch)
# =======
# Inkommande kod (branch som mergas)
# >>>>>>> feature-branch

# Redigera filen och ta bort markörer
# Behåll den kod du vill ha

# Markera som löst
git add konflikt-fil.txt             # Stagar den lösta filen

# Slutför merge
git commit                           # Skapar merge-commit (meddelande genereras)

# Eller med eget meddelande
git commit -m "Merge feature-login, resolved auth conflict"
```

---

## Praktiskt exempel

```bash
# Scenario: utveckla login-feature

# 1. Skapa feature-branch från main
git switch main                      # Säkerställ att du är på main
git pull origin main                 # Hämta senaste ändringar
git switch -c feature-login          # Skapa och byt till feature-branch

# 2. Gör ändringar
echo "login code" > login.js         # Skapa fil
git add login.js                     # Staga
git commit -m "Add login form"       # Commita

# 3. Fortsätt utveckla
echo "validation" >> login.js        # Lägg till mer kod
git commit -am "Add input validation" # Staga + commita

# 4. Merge tillbaka till main
git switch main                      # Byt till main
git merge feature-login              # Merga in feature

# 5. Städa upp
git branch -d feature-login          # Ta bort feature-branch
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Branch = pekare           | Bara 41 bytes, kostar ingenting att skapa           |
| git switch                | Moderna sattet att byta branch (istallet for checkout) |
| Fast-forward              | Nar malet inte har divergerat                       |
| --no-ff                   | Tvingar merge-commit aven vid fast-forward          |
| Stada upp                 | Ta bort mergade branches for ordning                |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Branches ar billiga - skapa en for varje feature
- Anvand git switch istallet for git checkout
- Konfliktmarkorar: <<<<<<< HEAD, =======, >>>>>>> branch
- Merga till main ofta for att undvika stora konflikter
- Ta bort branches efter merge for att halla ordning
""",
        },
        {
            "title": "Remote Repositories & GitHub",
            "slug": "remote-repositories-github",
            "difficulty": "beginner",
            "content": """
# Remote Repositories & GitHub

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan remote                   | Med remote (GitHub)           |
|---------------------------|-------------------------------|-------------------------------|
| Backup                    | Forlorar allt vid diskcrash   | Kod sakert i molnet           |
| Team-samarbete            | USB-sticka, email?            | Clone, push, pull             |
| CI/CD                     | Manuell deployment            | Push triggar pipeline         |
| Code review               | Visa skarmen?                 | Pull Requests                 |

GitHub ar den dominerande plattformen. Remote-hantering ar kritiskt for DevOps.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Remote Arkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    LOCAL vs REMOTE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────┐              ┌─────────────────┐          │
│   │   LOCAL REPO    │              │  REMOTE (origin)│          │
│   │                 │    git push  │                 │          │
│   │  main ─────────────────────────► main           │          │
│   │                 │              │                 │          │
│   │  origin/main◄───────────────────                │          │
│   │  (tracking)     │   git fetch  │                 │          │
│   │                 │              │                 │          │
│   │  feature ──────────────────────► feature        │          │
│   │                 │              │                 │          │
│   └─────────────────┘              └─────────────────┘          │
│                                                                 │
│   origin/main = LOKAL kopia av remote branch                    │
│   Uppdateras vid fetch/pull, inte automatiskt                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Kommandon:**

| Kommando       | Vad det gor                                          |
|----------------|------------------------------------------------------|
| git fetch      | Hamtar data fran remote, applicerar INTE             |
| git pull       | fetch + merge (eller rebase med --rebase)            |
| git push       | Skickar dina commits till remote                     |
| git clone      | Skapar lokal kopia av remote repo                    |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SSH-nycklar for GitHub

```bash
# Se befintliga remotes
git remote                           # Listar remote-namn
git remote -v                        # Visar URL:er (fetch och push)

# Lägg till remote (efter git init)
git remote add origin https://github.com/user/repo.git  # HTTPS
git remote add origin git@github.com:user/repo.git      # SSH (rekommenderat)

# Byt remote URL
git remote set-url origin git@github.com:user/repo.git  # Byt till SSH

# Ta bort remote
git remote remove origin             # Tar bort remote-referens

# Byt namn på remote
git remote rename origin upstream    # Byter namn origin → upstream
```

---

## SSH-nycklar för GitHub

```bash
# Generera SSH-nyckel
ssh-keygen -t ed25519 -C "din@email.se"  # Modernaste algoritmen
# Tryck Enter för default-sökväg (~/.ssh/id_ed25519)
# Ange lösenord (valfritt men rekommenderat)

# Starta SSH-agent
eval "$(ssh-agent -s)"               # Startar agenten i bakgrunden

# Lägg till nyckel till agenten
ssh-add ~/.ssh/id_ed25519            # Laddar privata nyckeln

# Kopiera publika nyckeln
cat ~/.ssh/id_ed25519.pub            # Visa publika nyckeln
# Kopiera output

# Lägg till på GitHub:
# 1. Settings → SSH and GPG keys → New SSH key
# 2. Klistra in publika nyckeln
# 3. Spara

# Testa anslutning
ssh -T git@github.com                # Ska säga "Hi username!"
```

---

## Push och Pull

```bash
# Första push till ny remote
git push -u origin main              # -u sätter upstream tracking

# Efter första push räcker:
git push                             # Pushar till tracking-branch
git push origin main                 # Explicit branch

# Hämta ändringar
git fetch                            # Hämtar ALLA remotes
git fetch origin                     # Hämtar från origin
git fetch origin main                # Hämtar bara main

# Se vad som hämtades
git log origin/main --oneline        # Visar remote-historik
git diff main origin/main            # Jämför lokal med remote

# Pull = fetch + merge
git pull                             # Hämtar och mergar tracking-branch
git pull origin main                 # Explicit

# Pull med rebase istället för merge
git pull --rebase                    # Håller historiken linjär
```

---

## Arbeta med remote branches

```bash
# Lista remote branches
git branch -r                        # Visar remote tracking branches

# Checka ut remote branch
git switch feature-x                 # Git skapar lokal branch automatiskt
# Om det finns origin/feature-x sätts tracking upp

# Manuellt skapa lokal branch från remote
git switch -c feature-x origin/feature-x  # Explicit

# Push ny lokal branch till remote
git push -u origin feature-new       # Skapar remote branch + sätter tracking

# Ta bort remote branch
git push origin --delete feature-done  # Tar bort på remote

# Städa bort lokala refs till borttagna remote branches
git fetch --prune                    # Tar bort stale tracking branches
```

---

## Synkronisera fork

```bash
# Scenario: du har forkat ett projekt och vill hålla din fork uppdaterad

# Lägg till original-repo som upstream
git remote add upstream https://github.com/original/repo.git

# Verifiera
git remote -v                        # Visar origin (din fork) och upstream

# Hämta från upstream
git fetch upstream                   # Hämtar original-projektets ändringar

# Merga upstream in i din main
git switch main                      # Byt till main
git merge upstream/main              # Merga upstream's main

# Pusha till din fork
git push origin main                 # Uppdaterar din fork pa GitHub
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Remote = origin           | Standardnamn for remote repository                  |
| SSH vs HTTPS              | SSH ar sakrare och smidigare an losenord            |
| fetch vs pull             | fetch hamtar data, pull hamtar OCH mergar           |
| -u (upstream)             | Satter tracking sa du slipper ange remote varje gang|
| --prune                   | Stadar bort refs till borttagna remote branches     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Konfigurera SSH-nycklar FORST - slipper losenord varje gang
- git pull --rebase ger renare historik an vanlig pull
- origin/main ar lokal kopia - uppdateras vid fetch
- For forks: upstream = original, origin = din fork
- Fetch forst, kolla diff, sedan merge/pull
""",
        },
        {
            "title": "Git Workflow Strategies",
            "slug": "git-workflow-strategies",
            "difficulty": "intermediate",
            "content": """
# Git Workflow Strategies

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan workflow                 | Med workflow                  |
|---------------------------|-------------------------------|-------------------------------|
| Release                   | "Vilken commit ar stabil?"    | Taggar, release branches      |
| Hotfix                    | Panik, pushes direkt till main| Strukturerad hotfix-process   |
| Code review               | Ingen standardisering         | PR-templates, approvals       |
| CI/CD                     | Buildar ibland, kraschar ofta | Automatiserat, forutsagbart   |

Ratt workflow minskar konflikter, forbattrar kodkvalitet och snabbar upp leverans.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Workflow-jamforelse

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKFLOW COMPARISON                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GITHUB FLOW (Enkel - Rekommenderas)                           │
│  ──────────────────────────────────────                         │
│  main ─────●─────●─────●─────●─────●                           │
│             \\         /                                         │
│              ●───────●  feature                                 │
│                 PR                                              │
│                                                                 │
│  GIT FLOW (Komplex - Schemalagda releaser)                     │
│  ──────────────────────────────────────────                     │
│  main    ─────●─────────────────●─────●                        │
│               │                 │     │                         │
│  release      │     ●───────────●     │                        │
│               │    /            │     │                         │
│  develop ─────●───●─────●───────●─────●                        │
│                    \\   /                                        │
│  feature            ●─●                                         │
│                                                                 │
│  TRUNK-BASED (Snabbast - Mogna team)                           │
│  ────────────────────────────────────                           │
│  main ─────●─────●─────●─────●─────●                           │
│             \\   /   \\   /   \\   /                              │
│              ●       ●       ●   (kort-livade branches)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Workflow     | Komplexitet | Release-frekvens   | Bast for               |
|--------------|-------------|--------------------|-----------------------|
| GitHub Flow  | Lag         | Kontinuerlig       | De flesta team        |
| Git Flow     | Hog         | Schemalagd         | Stora projekt, apps   |
| Trunk-Based  | Lag         | Kontinuerlig       | Mogna team, micro     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitHub Flow (Rekommenderat)

```bash
# GitHub Flow: Enkel och effektiv

# 1. Main är alltid deploybar
# Allt på main kan gå till produktion

# 2. Skapa feature-branch
git switch main                      # Börja från main
git pull origin main                 # Säkerställ senaste version
git switch -c feature/user-auth      # Beskrivande branch-namn

# 3. Gör commits regelbundet
git add .                            # Staga ändringar
git commit -m "Add user model"       # Beskrivande meddelanden
git commit -m "Add auth middleware"  # Små, fokuserade commits
git commit -m "Add login endpoint"   # Lätt att reviewa

# 4. Pusha och skapa Pull Request
git push -u origin feature/user-auth # Pusha till remote

# 5. Code review sker i PR på GitHub
# Diskutera, få feedback, gör ändringar

# 6. Merge via GitHub när approved
# Använd "Squash and merge" för clean history

# 7. Ta bort branch
git switch main                      # Tillbaka till main
git pull                             # Hämta mergad kod
git branch -d feature/user-auth      # Städa lokal branch
```

---

## Git Flow (För större projekt)

```bash
# Git Flow: Mer struktur, fler branches

# Permanenta branches:
# - main (produktion)
# - develop (integration)

# Temporära branches:
# - feature/* (nya features)
# - release/* (förberedelse för release)
# - hotfix/* (kritiska bugfixar)

# Feature development
git switch develop                   # Börja från develop
git switch -c feature/payment        # Skapa feature-branch

# ... utveckla ...

git switch develop                   # Tillbaka till develop
git merge --no-ff feature/payment    # Merge med commit

# Release
git switch develop                   # Från develop
git switch -c release/v1.2.0         # Skapa release-branch

# ... testa, fixa buggar ...

git switch main                      # Merga till main
git merge --no-ff release/v1.2.0     # Release är redo
git tag v1.2.0                       # Tagga versionen

git switch develop                   # Merga tillbaka till develop
git merge --no-ff release/v1.2.0     # Inkludera release-fixar

# Hotfix (kritisk bugg i produktion)
git switch main                      # Från main
git switch -c hotfix/security-patch  # Skapa hotfix-branch

# ... fixa ...

git switch main                      # Merga till main
git merge --no-ff hotfix/security-patch
git tag v1.2.1                       # Ny version

git switch develop                   # Merga till develop också
git merge --no-ff hotfix/security-patch
```

---

## Trunk-Based Development

```bash
# Trunk-Based: Minimal branching, snabba merges

# Principer:
# 1. Alla arbetar mot main (trunk)
# 2. Feature branches lever max 1-2 dagar
# 3. Feature flags för ofärdig kod
# 4. Kräver robust CI/CD

# Kort feature-branch
git switch main                      # Alltid börja från main
git pull                             # Senaste version
git switch -c feat/button-color      # Liten, fokuserad ändring

# Snabb utveckling (samma dag)
git add .                            # Staga
git commit -m "Update button color"  # Commita
git push -u origin feat/button-color # Pusha

# Merge samma dag (efter CI passerar)
# PR → Review → Merge

# Feature flags för större features
# if (featureFlags.newCheckout) { ... }
# Koden kan mergas till main utan att vara aktiv
```

---

## Commit-meddelanden

```bash
# Conventional Commits format:
# <type>(<scope>): <description>

# Types:
# feat:     Ny funktionalitet
# fix:      Buggfix
# docs:     Dokumentation
# style:    Formatering (ingen kodändring)
# refactor: Omstrukturering (ingen ny funktion/bugg)
# test:     Tester
# chore:    Underhåll (dependencies, config)

# Exempel på bra commits:
git commit -m "feat(auth): add JWT token refresh"
git commit -m "fix(api): handle null user in response"
git commit -m "docs(readme): update installation steps"
git commit -m "refactor(db): extract connection pooling"
git commit -m "test(user): add unit tests for validation"

# Multiline commit message
git commit                           # Öppnar editor
# Rad 1: Kort sammanfattning (max 50 tecken)
# Rad 2: Tom
# Rad 3+: Detaljerad beskrivning
```

---

## Branch-namngivning

```bash
# Konventioner för branch-namn:

# Feature branches
feature/user-authentication
feature/payment-integration
feat/add-dark-mode

# Bug fixes
fix/login-redirect
bugfix/null-pointer-exception

# Hotfixes (produktion)
hotfix/security-vulnerability
hotfix/critical-crash

# Releases
release/v1.2.0
release/2024-q1

# Med issue-nummer
feature/JIRA-123-user-auth
fix/GH-456-login-bug
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| GitHub Flow               | Enklast - en branch, PR, merge till main            |
| Git Flow                  | For storre projekt med schemalagda releaser         |
| Trunk-Based               | Kraver mogen CI/CD men ger snabbast leverans        |
| Conventional Commits      | Gor historiken lasbar och automatiserbar            |
| Konsekvent namngivning    | feature/, fix/, hotfix/ - hjalper hela teamet       |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Borja med GitHub Flow - enklast och fungerar for de flesta
- Commit-meddelanden ar dokumentation - skriv tydligt
- feat: ny funktion, fix: buggfix, docs: dokumentation
- Sma commits ar batttre an stora - lattare att reviewa
- Branch-namn ska vara beskrivande: feature/user-auth
""",
        },
        {
            "title": "Rebasing & Interactive Rebase",
            "slug": "rebasing-interactive-rebase",
            "difficulty": "intermediate",
            "content": """
# Rebasing & Interactive Rebase

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan rebase                   | Med rebase                    |
|---------------------------|-------------------------------|-------------------------------|
| Feature branch            | Massa merge-commits           | Linjar, ren historik          |
| WIP commits               | "WIP", "fix", "oops" synliga  | Squashade till en fin commit  |
| Code review               | Svart att folja               | Tydlig, logisk historik       |
| git bisect                | Hoppar runt i merge-spaghetti | Linjar sokning                |

Professionella utvecklare forvantas kunna halla en ren Git-historik.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Merge vs Rebase

```
┌─────────────────────────────────────────────────────────────────┐
│                    MERGE vs REBASE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FORE:                                                          │
│        A───B───C feature                                        │
│       /                                                         │
│  D───E───F───G main                                             │
│                                                                 │
│  EFTER MERGE:                                                   │
│        A───B───C                                                │
│       /         \\                                               │
│  D───E───F───G───M main  (M = merge commit)                    │
│                                                                 │
│  EFTER REBASE:                                                  │
│                  A'──B'──C' feature                            │
│                 /                                               │
│  D───E───F───G main                                             │
│                                                                 │
│  Rebase "flyttar" commits till ny bas (nya hashar A', B', C')  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Aspekt          | Merge                         | Rebase                        |
|-----------------|-------------------------------|-------------------------------|
| Historik        | Bevarar allt, merge-commits   | Linjar, omskrivna commits     |
| Saker           | Aldrig problem                | Farligt for publika commits   |
| Anvandning      | Publika branches, PRs         | Lokala branches, cleanup      |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Rebase

```bash
# Scenario: feature-branch har divergerat från main

# Visuellt före rebase:
#       A---B---C feature
#      /
# D---E---F---G main

# Efter rebase:
#               A'--B'--C' feature
#              /
# D---E---F---G main

# Utför rebase
git switch feature                   # Gå till din branch
git rebase main                      # Flytta commits till toppen av main

# Om konflikter uppstår:
# 1. Lösa konflikten i filen
# 2. git add <fil>
# 3. git rebase --continue

# Avbryt rebase om det blir för komplicerat
git rebase --abort                   # Återställ till före rebase

# Efter lyckad rebase, uppdatera remote (force push krävs!)
git push --force-with-lease          # Säkrare än --force
```

---

## Interactive rebase

```bash
# Redigera de senaste 3 commits
git rebase -i HEAD~3                 # Öppnar editor

# Editor visar:
# pick abc1234 Add user model
# pick def5678 Fix typo in user model
# pick ghi9012 Add user validation

# Ändra "pick" till önskad action:
# pick abc1234 Add user model
# squash def5678 Fix typo in user model    # Slå ihop med föregående
# reword ghi9012 Add user validation       # Ändra meddelande

# Spara och stäng - Git guidar dig genom ändringarna

# Vanliga användningsfall:

# Slå ihop alla till en commit
# squash, squash, squash (behåll första som pick)

# Ändra commit-meddelande
# reword

# Ta bort en commit
# drop (eller radera raden)

# Byt ordning
# Flytta raderna
```

---

## Squash commits före merge

```bash
# Scenario: Du har 5 "work in progress" commits
# och vill göra en clean PR

# Se dina commits
git log --oneline main..HEAD         # Commits sedan main

# Räkna antal commits att squasha
git rev-list --count main..HEAD      # T.ex. 5

# Interactive rebase mot main
git rebase -i main                   # Öppnar editor med alla commits sedan main

# Behåll första som pick, resten som squash:
# pick abc1234 WIP: start user feature
# squash def5678 WIP: more progress
# squash ghi9012 WIP: almost done
# squash jkl3456 Fix tests
# squash mno7890 Final cleanup

# Spara - Git ber dig skriva nytt kombinerat meddelande
# Skriv ett bra, beskrivande meddelande:
# "feat(user): Add complete user registration flow"
```

---

## Fixup commits

```bash
# Scenario: Du upptäcker ett fel i en tidigare commit
# och vill fixa det utan att skapa ny commit

# Gör din fix
echo "fixed code" >> file.py         # Fixa felet

# Skapa fixup commit
git commit -a --fixup=abc1234        # abc1234 är committen du fixar
# Skapar commit med meddelande "fixup! Original commit message"

# Autosquash vid rebase
git rebase -i --autosquash main      # Fixup-commits placeras automatiskt rätt

# Editorn visar:
# pick abc1234 Original commit
# fixup xyz9999 fixup! Original commit     # Automatiskt efter rätt commit
# pick def5678 Next commit

# Spara - fixup mergas in automatiskt
```

---

## Amend senaste commit

```bash
# Glömde lägga till en fil?
git add forgotten-file.js            # Staga den glömda filen
git commit --amend --no-edit         # Lägg till i senaste commit

# Vill ändra commit-meddelandet?
git commit --amend -m "Better message"  # Nytt meddelande

# Öppna editor för att redigera meddelande
git commit --amend                   # Öppnar editor

# OBS: Amend ändrar commit-hash!
# Om redan pushad krävs force push
git push --force-with-lease          # Uppdatera remote
```

---

## Säkerhetsregler för rebase

```bash
# GYLLENE REGELN: Rebasa ALDRIG publika commits!
# Om någon annan har baserat arbete på dina commits, förstör rebase deras historik.

# OK att rebasa:
# - Lokala commits som inte pushats
# - Din egen feature-branch som ingen annan arbetar på
# - Pull --rebase för att hålla clean history

# INTE OK att rebasa:
# - main/develop som andra arbetar mot
# - Commits som andra har pullade
# - Delade branches

# Säker force push
git push --force-with-lease          # Misslyckas om remote har nya commits
# Bättre än --force som skriver över allt

# Om olyckan är framme
git reflog                           # Visar alla HEAD-ändringar
git reset --hard HEAD@{2}            # Aterstall till tidigare tillstand
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Interactive Rebase Actions

| Action   | Vad det gor                                          |
|----------|------------------------------------------------------|
| pick     | Behall commit som den ar                             |
| reword   | Andra commit-meddelande                              |
| squash   | Sla ihop med foregaende, behall bada meddelanden     |
| fixup    | Sla ihop, behall BARA foregaendes meddelande         |
| drop     | Ta bort commit helt                                  |
| edit     | Pausa for att andra commit                           |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Rebase                    | Ger linjar historik - renare an merge               |
| Interactive rebase (-i)   | Full kontroll over commits                          |
| Squash                    | Sla ihop WIP-commits fore PR                        |
| --fixup + --autosquash    | Automatiserar cleanup                               |
| ALDRIG rebasa publikt     | Anvand --force-with-lease om nodvandigt             |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Rebase LOKALA branches - aldrig publika
- Squash WIP-commits fore PR for professionell historik
- --force-with-lease ar sakrare an --force
- Vid problem: git rebase --abort for att avbryta
- Reflog ar din raddning om det gar fel
""",
        },
        {
            "title": "Undoing Changes & Recovery",
            "slug": "undoing-changes-recovery",
            "difficulty": "intermediate",
            "content": """
# Undoing Changes & Recovery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan recovery-kunskap         | Med recovery-kunskap          |
|---------------------------|-------------------------------|-------------------------------|
| Fel commit                | Panik, manuell fix            | git revert pa sekunder        |
| Push till fel branch      | Kaos i teamet                 | Reset + correct branch        |
| Kaslig data pushad        | "Vad gor vi nu?!"             | Filter-branch + force push    |
| Forlorade commits         | Forlorade for evigt           | Reflog raddar dagen           |

Formagan att aterstalla ar skillnaden mellan panik och lugn problemlosning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Undo Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                      UNDO DECISION TREE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Var ar andringen?                                              │
│  │                                                              │
│  ├─► Working Directory (ej stagad)                              │
│  │   └─► git restore <file>                                     │
│  │                                                              │
│  ├─► Staging Area (stagad, ej committad)                        │
│  │   └─► git restore --staged <file>                            │
│  │                                                              │
│  ├─► Committad (lokalt)                                         │
│  │   ├─► Angra + behall andringar: git reset --soft HEAD~1      │
│  │   ├─► Angra + unstage: git reset HEAD~1                      │
│  │   └─► Angra + kasta allt: git reset --hard HEAD~1            │
│  │                                                              │
│  └─► Pushad (remote)                                            │
│      └─► git revert HEAD (skapar NY commit som angrar)          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Situation            | Kommando                          | Effekt                        |
|----------------------|-----------------------------------|-------------------------------|
| Unstage fil          | git restore --staged file         | Tar bort fran staging         |
| Kasta lokal andring  | git restore file                  | Atergar till HEAD             |
| Angra senaste commit | git reset --soft HEAD~1           | Behaller andringar i staging  |
| Revert pushad commit | git revert HEAD                   | Ny commit som angrar          |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Angra i Working Directory

```bash
# Kasta bort ändringar i en fil (återställ till senaste commit)
git checkout -- filename.txt         # Gammalt sätt
git restore filename.txt             # Nytt, tydligare (Git 2.23+)

# Kasta bort ALLA ändringar
git checkout -- .                    # Gammalt
git restore .                        # Nytt

# Kasta bort untracked files
git clean -f                         # Ta bort untracked files
git clean -fd                        # Inkludera directories
git clean -fxd                       # Inkludera ignored files (försiktig!)

# Dry run först
git clean -n                         # Visar vad som skulle tas bort
git clean -nd                        # Med directories
```

---

## Ångra staging (unstage)

```bash
# Unstage en fil (behåll ändringar i working directory)
git reset HEAD filename.txt          # Gammalt sätt
git restore --staged filename.txt    # Nytt, tydligare

# Unstage allt
git reset HEAD                       # Gammalt
git restore --staged .               # Nytt

# Skillnaden:
# reset/restore --staged tar bort från staging
# Men filen har fortfarande ändringarna
```

---

## Ångra commits

```bash
# Ångra senaste commit men behåll ändringar i staging
git reset --soft HEAD~1              # Flyttar HEAD, ändringar kvar staged

# Ångra senaste commit, behåll ändringar i working directory
git reset --mixed HEAD~1             # Default, ändringar kvar unstaged
git reset HEAD~1                     # Samma sak

# Ångra senaste commit OCH kasta bort ändringar
git reset --hard HEAD~1              # FARLIGT - ändringar försvinner!

# Ångra flera commits
git reset --soft HEAD~3              # Ångra 3 commits

# Ångra till specifik commit
git reset --hard abc1234             # Återställ till commit abc1234
```

---

## Revert (säkert sätt för pushade commits)

```bash
# Revert skapar en NY commit som ångrar en tidigare commit
# Säkert för publika/pushade commits - förstör inte historik

# Revertera senaste commit
git revert HEAD                      # Skapar commit som ångrar HEAD

# Revertera specifik commit
git revert abc1234                   # Ångrar commit abc1234

# Revertera utan att commita direkt
git revert --no-commit abc1234       # Ändringarna hamnar i staging

# Revertera en merge-commit (kräver -m)
git revert -m 1 abc1234              # -m 1 = behåll första parent (main)

# Revertera flera commits
git revert HEAD~3..HEAD              # Revertera de 3 senaste
```

---

## Reflog - Din säkerhetsbackup

```bash
# Reflog loggar ALLA ändringar av HEAD - även "borttagna" commits
# Livräddare vid misslyckad rebase/reset

# Visa reflog
git reflog                           # Visar alla HEAD-ändringar
git reflog show main                 # För specifik branch

# Output exempel:
# abc1234 HEAD@{0}: commit: Add feature
# def5678 HEAD@{1}: rebase: finish
# ghi9012 HEAD@{2}: rebase: start
# jkl3456 HEAD@{3}: commit: WIP
# mno7890 HEAD@{4}: checkout: moving from main to feature

# Återställ till tidigare tillstånd
git reset --hard HEAD@{3}            # Gå tillbaka till tillstånd 3

# Hitta "förlorad" commit
git reflog | grep "important"        # Sök i reflog
git cherry-pick abc1234              # Plocka tillbaka commit
```

---

## Återställa borttagna branches

```bash
# Tog du bort en branch av misstag?

# Hitta senaste commit i reflog
git reflog | grep feature-x          # Leta efter branch-namn

# Eller hitta via grep
git reflog | grep "checkout: moving"  # Se branch-byten

# Återskapa branch från commit
git branch feature-x abc1234         # Skapa branch vid commit

# Snabbare: Git visar commit vid delete
# git branch -D feature-x
# Deleted branch feature-x (was abc1234).
# Använd abc1234 för att återskapa
```

---

## Återställa fil från tidigare commit

```bash
# Hämta fil från specifik commit
git checkout abc1234 -- filename.txt # Hämtar filen, stagar automatiskt
git restore --source=abc1234 filename.txt  # Nyare syntax

# Hämta fil från 3 commits sedan
git checkout HEAD~3 -- filename.txt  # Relativ referens

# Hämta fil från annan branch
git checkout other-branch -- filename.txt  # Från annan branch

# Se filens innehåll utan att checka ut
git show abc1234:filename.txt        # Visa innehåll
git show HEAD~3:src/app.js           # Med sökväg
```

---

## Nödläges-checklista

```bash
# "Jag förstörde allt med hard reset!"
git reflog                           # Hitta commit före reset
git reset --hard HEAD@{1}            # Återställ

# "Jag pushade känslig data!"
# 1. Ändra credentials OMEDELBART
# 2. Force push fixad version
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.txt" \
  --prune-empty --tag-name-filter cat -- --all
git push --force --all

# "Jag mergade fel branch till main!"
git reset --hard HEAD~1              # Om inte pushad
git revert -m 1 HEAD                 # Om pushad

# "Jag commitade till fel branch!"
git log --oneline -1                 # Notera commit-hash
git reset --hard HEAD~1              # Ta bort från fel branch
git switch correct-branch            # Byt till rätt branch
git cherry-pick abc1234              # Applicera commit har
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| git restore               | For working directory och staging area              |
| git reset --soft          | Angra commit, behall andringar staged               |
| git reset --hard          | Angra commit OCH kasta andringar (farligt!)         |
| git revert                | For publika commits - skapar ny commit som angrar   |
| git reflog                | Din backup - loggar allt aven "borttaget"           |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Reflog ar din livlina - commits ar aldrig helt forlorade
- Revert for publika commits, reset for lokala
- --force-with-lease ar sakrare an --force
- Kanslig data kraver OMEDELBAR credential-rotation
- Skriv ner commit-hashar innan du gor farliga operationer
""",
        },
        {
            "title": "Pull Requests & Code Review",
            "slug": "pull-requests-code-review",
            "difficulty": "intermediate",
            "content": """
# Pull Requests & Code Review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan PR-process               | Med PR-process                |
|---------------------------|-------------------------------|-------------------------------|
| Kodkvalitet               | Buggar gar rakt till prod     | Review fangar problem         |
| Kunskapsspridning         | Bara en vet hur X fungerar    | Teamet laser varandras kod    |
| Dokumentation             | "Varfor andrade vi detta?"    | PR-beskrivning forklarar      |
| CI/CD                     | Manuella tester               | Automatiska checks i PR       |

PRs ar hjartat i modern mjukvaruutveckling. Bra PR-praxis hojer kodkvaliteten.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PR Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                      PR LIFECYCLE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. SKAPA BRANCH                                                │
│     git switch -c feature/user-auth                             │
│              │                                                  │
│              ▼                                                  │
│  2. UTVECKLA + COMMITA                                          │
│     git commit -m "feat(auth): add login"                       │
│              │                                                  │
│              ▼                                                  │
│  3. PUSH + SKAPA PR                                             │
│     git push -u origin feature/user-auth                        │
│     → GitHub: "Compare & pull request"                          │
│              │                                                  │
│              ▼                                                  │
│  4. CI KORS AUTOMATISKT                                         │
│     Tests, linting, build                                       │
│              │                                                  │
│              ▼                                                  │
│  5. CODE REVIEW                                                 │
│     Kommentarer, feedback, diskussion                           │
│              │                                                  │
│              ▼                                                  │
│  6. APPROVED + MERGE                                            │
│     Squash and merge till main                                  │
│              │                                                  │
│              ▼                                                  │
│  7. DELETE BRANCH                                               │
│     Automatiskt eller manuellt                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa en bra Pull Request

```bash
# 1. Säkerställ clean branch
git switch main                      # Uppdatera main
git pull origin main                 # Hämta senaste
git switch feature-branch            # Tillbaka till feature
git rebase main                      # Rebasa på senaste main

# 2. Squash om nödvändigt
git rebase -i main                   # Rensa upp commits

# 3. Push
git push -u origin feature-branch    # Force push om rebasad
git push --force-with-lease          # Säkrare force push

# 4. Skapa PR på GitHub
# - Gå till repo på GitHub
# - Klicka "Compare & pull request"
# - Eller: Pull requests → New pull request
```

---

## PR-beskrivning template

```markdown
## Beskrivning
Kort sammanfattning av vad PR:en gör.

## Typ av ändring
- [ ] Buggfix
- [ ] Ny feature
- [ ] Breaking change
- [ ] Dokumentation

## Hur har detta testats?
Beskriv testerna du kört.

## Checklist
- [ ] Koden följer projektets stilguide
- [ ] Jag har lagt till tester
- [ ] Dokumentationen är uppdaterad
- [ ] CI passerar

## Screenshots (om UI-ändring)
Före/efter bilder.

## Relaterade issues
Closes #123
Relates to #456
```

---

## Ge bra code review

```bash
# Som reviewer, tänk på:

# 1. Kör koden lokalt
git fetch origin                     # Hämta senaste
git switch pr-branch                 # Checka ut PR-branchen
# Testa att det fungerar!

# 2. Läs igenom diffen noggrant
# - Förstå kontexten
# - Tänk på edge cases
# - Kolla efter säkerhetsproblem
# - Verifiera testning

# 3. Kommentera konstruktivt
# Dåligt: "Det här är fel"
# Bra: "Överväg att använda X här för att hantera edge case Y"

# 4. Kategorisera feedback
# [nitpick] - Mindre förslag, ok att ignorera
# [suggestion] - Bra idé, diskuterbart
# [blocking] - Måste fixas före merge
```

---

## GitHub CLI för PRs

```bash
# Installera GitHub CLI
brew install gh                      # macOS
sudo apt install gh                  # Ubuntu

# Autentisera
gh auth login                        # Följ instruktioner

# Skapa PR från terminalen
gh pr create                         # Interaktiv
gh pr create --title "Add feature" --body "Description"

# Lista PRs
gh pr list                           # Öppna PRs
gh pr list --state all               # Alla PRs

# Visa specifik PR
gh pr view 123                       # PR nummer 123
gh pr view --web                     # Öppna i browser

# Checka ut PR lokalt
gh pr checkout 123                   # Checkar ut PR #123

# Merge PR
gh pr merge 123                      # Interaktiv merge
gh pr merge 123 --squash             # Squash merge
gh pr merge 123 --rebase             # Rebase merge

# Godkänn PR
gh pr review 123 --approve           # Godkänn
gh pr review 123 --comment -b "LGTM" # Kommentera
gh pr review 123 --request-changes   # Be om ändringar
```

---

## Branch Protection Rules

```yaml
# På GitHub: Settings → Branches → Add rule

# Branch name pattern: main

# Rekommenderade inställningar:

# ✅ Require a pull request before merging
#    - Require approvals: 1-2
#    - Dismiss stale reviews
#    - Require review from code owners

# ✅ Require status checks to pass
#    - Require branches to be up to date
#    - Välj checks: CI, tests, lint

# ✅ Require conversation resolution

# ✅ Require signed commits (valfritt)

# ✅ Include administrators
#    - Även admins måste följa reglerna

# ❌ Allow force pushes
#    - Aldrig på main!
```

---

## CODEOWNERS

```bash
# Fil: .github/CODEOWNERS
# Automatisk tilldelning av reviewers baserat på filändringar

# Syntax: pattern owner(s)

# Default owner för allt
*       @default-reviewer

# Frontend
*.js    @frontend-team
*.tsx   @frontend-team
/src/components/  @frontend-lead

# Backend
*.py    @backend-team
/api/   @backend-lead

# DevOps
Dockerfile      @devops-team
*.yaml          @devops-team
.github/        @devops-team

# Docs
*.md    @docs-team

# Kritiska filer - kräver senior review
/src/auth/      @security-team @senior-dev
package.json    @tech-lead
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Review Feedback Kategorier

| Prefix      | Betydelse                          | Action                        |
|-------------|-----------------------------------|-------------------------------|
| [nitpick]   | Mindre forslag, ok att ignorera   | Valfritt att fixa             |
| [suggestion]| Bra ide, diskuterbart             | Diskutera, besluta            |
| [blocking]  | Maste fixas fore merge            | Obligatorisk fix              |
| [question]  | Behover forklaring                | Svara pa fragan               |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Rebasa fore PR            | Ger enklare review, clean historik                  |
| PR-beskrivning            | Sparar reviewers tid - forklara VARFOR              |
| Kategorisera feedback     | nitpick, suggestion, blocking                       |
| Branch protection         | Forhindrar misstag, kraver reviews                  |
| CODEOWNERS                | Automatiserar reviewer-tilldelning                  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Sma PRs ar batttre an stora - lattare att reviewa
- Svara pa ALLA kommentarer, aven om du inte andrar
- gh CLI ar kraftfullt - gh pr create, gh pr checkout
- Squash and merge for clean historik
- Delete branch efter merge - automatisera detta
""",
        },
        {
            "title": "GitHub Actions Basics",
            "slug": "github-actions-basics",
            "difficulty": "intermediate",
            "content": """
# GitHub Actions Basics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan GitHub Actions           | Med GitHub Actions            |
|---------------------------|-------------------------------|-------------------------------|
| Tester                    | Manuellt, glomms bort         | Automatiskt vid varje push    |
| Deployment               | SSH + manuella steg           | git push = deploy             |
| Code quality              | "Jag testar lokalt"           | CI blockerar trasig kod       |
| Kostnad                   | Jenkins-server, underhall     | Gratis for public repos       |

GitHub Actions ar standard for CI/CD i modern utveckling.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitHub Actions Arkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                  GITHUB ACTIONS STRUCTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  WORKFLOW (.github/workflows/ci.yml)                           │
│  │                                                              │
│  ├─► EVENT (trigger)                                            │
│  │   push, pull_request, schedule, workflow_dispatch            │
│  │                                                              │
│  └─► JOBS (parallella som standard)                             │
│      │                                                          │
│      ├─► job: build                                             │
│      │   runs-on: ubuntu-latest                                 │
│      │   steps:                                                 │
│      │     - uses: actions/checkout@v4                          │
│      │     - run: npm install                                   │
│      │     - run: npm test                                      │
│      │                                                          │
│      └─► job: deploy (needs: build)                             │
│          runs-on: ubuntu-latest                                 │
│          steps: ...                                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Komponent   | Beskrivning                                          |
|-------------|------------------------------------------------------|
| Workflow    | YAML-fil som definierar automation                   |
| Event       | Trigger (push, PR, cron, manuell)                    |
| Job         | Grupp av steg pa samma runner                        |
| Step        | Enskild uppgift (action eller script)                |
| Action      | Ateranvandbar enhet fran marketplace                 |
| Runner      | Maskin som kor jobbet                                |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Forsta Workflow

```yaml
# .github/workflows/ci.yml

name: CI                             # Workflow-namn (visas i GitHub)

on:                                  # Triggers
  push:                              # Vid push
    branches: [main]                 # Till main
  pull_request:                      # Vid PR
    branches: [main]                 # Mot main

jobs:                                # Jobs att köra
  build:                             # Job-namn
    runs-on: ubuntu-latest           # Runner (GitHub-hosted)

    steps:                           # Steg i jobbet
      - name: Checkout code          # Steg-namn
        uses: actions/checkout@v4    # Använd checkout action

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:                        # Action inputs
          node-version: '20'
          cache: 'npm'               # Cacha npm dependencies

      - name: Install dependencies
        run: npm ci                  # Kör shell-kommando

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build
```

---

## Workflow triggers

```yaml
# Push och PR (vanligast)
on:
  push:
    branches: [main, develop]
    paths:                           # Kör bara vid ändringar i dessa sökvägar
      - 'src/**'
      - 'package.json'
  pull_request:
    branches: [main]
    types: [opened, synchronize]     # Specifika PR-events

# Schemalagd körning
on:
  schedule:
    - cron: '0 2 * * *'              # Varje natt kl 02:00 UTC

# Manuell trigger
on:
  workflow_dispatch:                 # Knapp i GitHub UI
    inputs:
      environment:
        description: 'Deploy environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

# Vid release
on:
  release:
    types: [published]

# Vid tagg
on:
  push:
    tags:
      - 'v*'                         # v1.0.0, v2.0.0, etc.
```

---

## Jobs och dependencies

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test

  build:
    needs: [lint, test]              # Väntar på lint OCH test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build

  deploy:
    needs: build                     # Väntar på build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'  # Bara på main
    steps:
      - run: echo "Deploying..."
```

---

## Secrets och variabler

```yaml
# Använd secrets (aldrig hårdkoda credentials!)
# Lägg till i: Settings → Secrets → Actions

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server
        env:
          SSH_KEY: ${{ secrets.SSH_PRIVATE_KEY }}  # Secret
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          echo "$SSH_KEY" > key.pem
          chmod 600 key.pem
          # Använd key för SSH...

      - name: Use variable
        env:
          NODE_ENV: ${{ vars.NODE_ENV }}  # Variabel (inte hemlig)
        run: echo "Environment: $NODE_ENV"

# Inbyggda variabler
# ${{ github.sha }}           - Commit SHA
# ${{ github.ref }}           - Branch/tag ref
# ${{ github.actor }}         - Användare som triggade
# ${{ github.repository }}    - owner/repo
# ${{ github.event_name }}    - push, pull_request, etc.
```

---

## Matrix builds

```yaml
# Testa på flera versioner/plattformar parallellt
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [18, 20, 22]
      fail-fast: false               # Fortsätt även om en failar

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm ci
      - run: npm test
```

---

## Artifacts och caching

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Cache dependencies
      - uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('**/package-lock.json') }}
          restore-keys: npm-

      - run: npm ci
      - run: npm run build

      # Spara build-output som artifact
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/
          retention-days: 7

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      # Hämta artifact från build-job
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/

      - run: ls -la dist/
```

---

## Key Takeaways

1. Workflows definieras i `.github/workflows/*.yml`
2. `on:` bestämmer triggers (push, PR, schedule, dispatch)
3. `needs:` skapar dependencies mellan jobs
4. Secrets för credentials, aldrig i kod
5. Matrix för parallell testning på flera versioner
""",
        },
        {
            "title": "Git Stash & Worktrees",
            "slug": "git-stash-worktrees",
            "difficulty": "intermediate",
            "content": """
# Git Stash & Worktrees

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan stash/worktrees          | Med stash/worktrees           |
|---------------------------|-------------------------------|-------------------------------|
| Akut buggfix              | Commita halvfardigt, kladd    | Stash, fixa, pop              |
| Testa annan branch        | Forlora andringar             | Worktree = parallellt         |
| Code review               | Byt branch, tappa context     | Worktree for review           |
| Experiment                | Risk att blanda               | Isolerade worktrees           |

Stash och worktrees ar kritiska for effektivt arbete i team.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stash Visualisering

```
┌─────────────────────────────────────────────────────────────────┐
│                      STASH STACK                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  WORKING DIRECTORY                                              │
│  (med andringar)                                                │
│        │                                                        │
│        │ git stash                                              │
│        ▼                                                        │
│  ┌─────────────┐                                                │
│  │ stash@{0}   │ ◄── Senaste stash                              │
│  │ "WIP auth"  │                                                │
│  ├─────────────┤                                                │
│  │ stash@{1}   │                                                │
│  │ "Fix bug"   │                                                │
│  ├─────────────┤                                                │
│  │ stash@{2}   │                                                │
│  │ "Refactor"  │                                                │
│  └─────────────┘                                                │
│        │                                                        │
│        │ git stash pop                                          │
│        ▼                                                        │
│  WORKING DIRECTORY                                              │
│  (andringar tillbaka)                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Git Stash Grunderna

```bash
# Spara aktuella ändringar i stash
git stash                            # Stashar tracked, modified files
git stash -u                         # Inkluderar untracked files
git stash -a                         # Inkluderar ignored files (sällsynt)

# Med beskrivning
git stash push -m "WIP: user auth"   # Stash med meddelande

# Stasha specifika filer
git stash push -m "partial" file1.js file2.js  # Bara dessa filer

# Interaktiv stash (välj hunks)
git stash -p                         # Välj vilka ändringar att stasha

# Lista stashes
git stash list                       # Visar alla stashes
# stash@{0}: WIP on main: abc1234 Latest commit message
# stash@{1}: On feature: def5678 Another message
```

---

## Återställa från stash

```bash
# Applicera senaste stash (behåll i stash)
git stash apply                      # Applicerar stash@{0}

# Applicera och ta bort från stash
git stash pop                        # Apply + drop

# Applicera specifik stash
git stash apply stash@{2}            # Tredje stashen
git stash pop stash@{1}              # Andra stashen

# Visa stash-innehåll
git stash show                       # Sammanfattning
git stash show -p                    # Full diff
git stash show stash@{1}             # Specifik stash

# Ta bort stash
git stash drop                       # Ta bort senaste
git stash drop stash@{2}             # Specifik
git stash clear                      # TA BORT ALLA (försiktig!)
```

---

## Avancerad stash-användning

```bash
# Skapa branch från stash
git stash branch new-feature         # Skapar branch, applicerar stash, droppar

# Stash endast staged changes
git stash --staged                   # Bara det som är stagat

# Stash allt utom staged
git stash --keep-index               # Behåller staging area

# Typiskt scenario:
# 1. Stage det du vill commita
# 2. git stash --keep-index
# 3. Testa att staged changes fungerar isolerat
# 4. git stash pop för att få tillbaka resten
```

---

## Git Worktrees

```bash
# Varför worktrees?
# - Byta branch utan stash
# - Jämföra kod från olika branches sida vid sida
# - Köra tester på en branch medan du utvecklar på en annan
# - Ha main deploybar medan du arbetar på features

# Lista befintliga worktrees
git worktree list                    # Visar alla worktrees
# /home/user/project        abc1234 [main]

# Skapa ny worktree för befintlig branch
git worktree add ../project-feature feature-x
# Skapar ../project-feature med feature-x utcheckad

# Skapa ny worktree med NY branch
git worktree add -b hotfix-123 ../project-hotfix main
# Skapar hotfix-123 branch från main, checkar ut i ../project-hotfix

# Nu kan du:
cd ../project-feature                # Arbeta på feature
cd ../project                        # Tillbaka till main
# Båda finns samtidigt!
```

---

## Hantera worktrees

```bash
# Worktree-struktur (typisk)
~/projects/
├── myapp/                           # Huvudrepo (main)
│   └── .git/                        # Git-databasen
├── myapp-feature/                   # Worktree (feature-x)
│   └── .git                         # Fil som pekar till huvudrepo
└── myapp-hotfix/                    # Worktree (hotfix)
    └── .git                         # Fil som pekar till huvudrepo

# Ta bort worktree
git worktree remove ../project-feature  # Tar bort katalog och registrering

# Om katalogen redan är borta
git worktree prune                   # Städar upp stale worktree-refs

# Lås worktree (förhindra borttagning)
git worktree lock ../project-feature # Låser
git worktree unlock ../project-feature  # Låser upp

# Flytta worktree
git worktree move ../old-path ../new-path  # Flytta katalog
```

---

## Praktiska scenarios

```bash
# Scenario 1: Akut buggfix mitt i feature-arbete

# Du är på feature-branch med ändringar
git stash -m "WIP: halfway through feature"  # Spara arbete
git switch main                      # Byt till main
git pull                             # Uppdatera
git switch -c hotfix-critical        # Skapa hotfix-branch
# ... fixa buggen ...
git commit -am "Fix critical bug"
git switch main && git merge hotfix-critical
git push
git switch feature-branch            # Tillbaka
git stash pop                        # Återställ arbete

# Scenario 2: Använda worktrees för parallel utveckling

# Huvudprojekt på main
cd ~/projects/app                    # main branch

# Skapa worktree för feature
git worktree add ~/projects/app-auth feature/auth

# Nu kan du ha VSCode öppet i båda
# Terminal 1: cd ~/projects/app && npm run dev
# Terminal 2: cd ~/projects/app-auth && npm run dev

# Scenario 3: Code review med worktree
git worktree add ~/projects/app-pr-review pr-branch
cd ~/projects/app-pr-review
npm install && npm test              # Testa PR lokalt
# ... review ...
git worktree remove ~/projects/app-pr-review
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| git stash                 | Sparar andringar temporart utan commit              |
| stash -u                  | Inkluderar untracked files                          |
| stash -m                  | Beskrivande meddelande for ordning                  |
| Worktrees                 | Flera branches utcheckade samtidigt                 |
| Delar .git                | Worktrees synkar automatiskt                        |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Stash ar en stack - LIFO (Last In, First Out)
- git stash pop = apply + drop i ett steg
- Worktrees ar perfekta for code review
- Varje worktree maste ha unik branch
- Stada upp worktrees med git worktree remove
""",
        },
        {
            "title": "Git Tags & Releases",
            "slug": "git-tags-releases",
            "difficulty": "intermediate",
            "content": """
# Git Tags & Releases

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan taggar                   | Med taggar                    |
|---------------------------|-------------------------------|-------------------------------|
| Release                   | "Vilken commit ar v1.2.0?"    | git checkout v1.2.0           |
| Rollback                  | Leta i logg, gissa            | git checkout v1.1.0           |
| CI/CD deploy              | Manuell trigger               | Push tag = auto deploy        |
| Changelog                 | Manuell dokumentation         | Auto-genererat fran tags      |

Tags ar fundamentet for versionshantering och release-automatisering.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tag-typer

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIGHTWEIGHT vs ANNOTATED                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LIGHTWEIGHT TAG                 ANNOTATED TAG                  │
│  ────────────────                ──────────────                 │
│  Bara en pekare                  Fullt Git-objekt               │
│                                                                 │
│  ┌────────┐                      ┌────────────────┐             │
│  │ v1.0.0 │────► commit          │ v1.0.0 (tag)   │             │
│  └────────┘                      │ Author: Said   │             │
│                                  │ Date: 2024-01  │             │
│                                  │ Msg: Release   │             │
│                                  └───────┬────────┘             │
│                                          │                      │
│                                          ▼                      │
│                                       commit                    │
│                                                                 │
│  Anvandning: Temporart           Anvandning: Releases           │
│                                  (rekommenderas)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Typ         | Skapas med         | Innehall                     | Anvandning     |
|-------------|--------------------|-----------------------------|----------------|
| Lightweight | git tag v1.0.0     | Bara pekare                 | Temporara tags |
| Annotated   | git tag -a v1.0.0  | Metadata, meddelande, datum | Releases       |
| Signed      | git tag -s v1.0.0  | + GPG-signatur              | Sakra releases |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Taggar

```bash
# Lightweight tag (bara pekare)
git tag v1.0.0                       # Taggar HEAD
git tag v1.0.0 abc1234               # Taggar specifik commit

# Annotated tag (rekommenderat)
git tag -a v1.0.0 -m "Release version 1.0.0"  # Med meddelande
git tag -a v1.0.0                    # Öppnar editor för meddelande

# Signerad tag (kräver GPG-setup)
git tag -s v1.0.0 -m "Signed release" # Signerad med GPG

# Tagga tidigare commit
git tag -a v0.9.0 abc1234 -m "Beta release"  # Retroaktiv tagg
```

---

## Hantera taggar

```bash
# Lista taggar
git tag                              # Alla taggar
git tag -l "v1.*"                    # Filtrera med pattern
git tag -l --sort=-v:refname         # Sortera i versionsordning

# Visa tagg-info
git show v1.0.0                      # Visar tagg + commit

# Ta bort tagg
git tag -d v1.0.0                    # Ta bort lokalt
git push origin --delete v1.0.0      # Ta bort på remote
git push origin :refs/tags/v1.0.0    # Alternativ syntax

# Byt namn på tagg (skapa ny, ta bort gammal)
git tag new-tag old-tag              # Kopiera
git tag -d old-tag                   # Ta bort gammal
git push origin new-tag :old-tag     # Uppdatera remote
```

---

## Push taggar till remote

```bash
# Push specifik tagg
git push origin v1.0.0               # Pushar en tagg

# Push ALLA taggar
git push origin --tags               # Pushar alla taggar

# Push endast annotated tags
git push origin --follow-tags        # Bara annoterade

# Rekommendation: Använd --follow-tags
# Lägg till som default:
git config --global push.followTags true
```

---

## Semantic Versioning

```bash
# Format: MAJOR.MINOR.PATCH
# v1.0.0 → v1.0.1 → v1.1.0 → v2.0.0

# MAJOR (1.x.x)
# Inkompatibla API-ändringar
# Breaking changes
git tag -a v2.0.0 -m "Breaking: New API structure"

# MINOR (x.1.x)
# Ny funktionalitet, bakåtkompatibel
git tag -a v1.1.0 -m "Add: User authentication feature"

# PATCH (x.x.1)
# Buggfixar, bakåtkompatibla
git tag -a v1.0.1 -m "Fix: Login redirect issue"

# Pre-release versioner
git tag -a v2.0.0-alpha.1 -m "Alpha release"
git tag -a v2.0.0-beta.2 -m "Beta release"
git tag -a v2.0.0-rc.1 -m "Release candidate"
```

---

## GitHub Releases

```bash
# GitHub Releases bygger på Git tags
# Lägg till: release notes, binärer, assets

# Med GitHub CLI
gh release create v1.0.0             # Interaktiv
gh release create v1.0.0 --title "Version 1.0" --notes "Release notes"

# Med filer
gh release create v1.0.0 ./dist/*.zip  # Ladda upp assets

# Från specifik branch/commit
gh release create v1.0.0 --target main

# Draft release (inte publicerad än)
gh release create v1.0.0 --draft

# Pre-release
gh release create v2.0.0-beta.1 --prerelease

# Lista releases
gh release list

# Visa specifik release
gh release view v1.0.0

# Ta bort release
gh release delete v1.0.0 --yes

# Auto-generera release notes
gh release create v1.0.0 --generate-notes
```

---

## Checkout tag

```bash
# Checka ut tagg (detached HEAD state)
git checkout v1.0.0                  # Varning: detached HEAD

# Se vilken version du är på
git describe                         # Visar närmaste tagg
git describe --tags                  # Inkluderar lightweight

# Output: v1.0.0-3-gabc1234
# = 3 commits efter v1.0.0, commit abc1234

# Skapa branch från tagg
git checkout -b hotfix-v1 v1.0.0     # Skapa branch vid tagg
git switch -c hotfix-v1 v1.0.0       # Nyare syntax
```

---

## CI/CD med taggar

```yaml
# GitHub Actions: Trigger på tag
name: Release

on:
  push:
    tags:
      - 'v*'                         # v1.0.0, v2.0.0, etc.

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Get version from tag
        run: echo "VERSION=${GITHUB_REF#refs/tags/}" >> $GITHUB_ENV

      - name: Build with version
        run: |
          echo "Building version $VERSION"
          npm version $VERSION --no-git-tag-version
          npm run build

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
          generate_release_notes: true
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Semantic Versioning

| Version       | Nar                                    | Exempel                       |
|---------------|----------------------------------------|-------------------------------|
| MAJOR (X.0.0) | Breaking changes, inkompatibelt        | v1.0.0 → v2.0.0               |
| MINOR (0.X.0) | Ny funktionalitet, bakatkompat         | v1.0.0 → v1.1.0               |
| PATCH (0.0.X) | Buggfixar, bakatkompat                 | v1.0.0 → v1.0.1               |
| Pre-release   | Alpha, beta, RC                        | v2.0.0-beta.1                 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Annotated tags (-a)       | Anvand for releases - har metadata                  |
| Semantic versioning       | MAJOR.MINOR.PATCH                                   |
| --follow-tags             | Pushar bara annoterade taggar                       |
| GitHub Releases           | Bygger pa Git tags + release notes                  |
| CI/CD trigger             | Push tag = automatisk deployment                    |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- ALLTID annotated tags for releases: git tag -a v1.0.0
- Push tags explicit: git push origin v1.0.0
- gh release create for GitHub Releases fran CLI
- Tags ar permanenta - ta bort kraver --delete
- Semantic versioning ar standard - folj det
""",
        },
        {
            "title": "Git Hooks",
            "slug": "git-hooks",
            "difficulty": "intermediate",
            "content": """
# Git Hooks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan hooks                    | Med hooks                     |
|---------------------------|-------------------------------|-------------------------------|
| Lint-fel                  | Upptacks i CI, forsenar       | Blockeras vid commit          |
| Daliga commit-msg         | Oläsbar historik              | Valideras automatiskt         |
| Trasig kod pushad         | Bryter prod, rollback         | Pre-push tester stoppar       |
| Formatering               | Inkonsekvent kod              | Auto-formatering vid commit   |

Hooks forhindrar att dalig kod ens hamnar i repositoryt.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hook-typer

```
┌─────────────────────────────────────────────────────────────────┐
│                      GIT HOOKS LIFECYCLE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLIENT-SIDE HOOKS                                              │
│  ─────────────────                                              │
│                                                                 │
│  git commit                                                     │
│       │                                                         │
│       ├──► pre-commit         Lint, formatera, tester           │
│       │                                                         │
│       ├──► prepare-commit-msg Redigera default-meddelande       │
│       │                                                         │
│       └──► commit-msg         Validera commit-meddelande        │
│                                                                 │
│  git push                                                       │
│       │                                                         │
│       └──► pre-push           Full test suite, build            │
│                                                                 │
│  SERVER-SIDE HOOKS                                              │
│  ─────────────────                                              │
│                                                                 │
│  pre-receive    Validera fore accept                            │
│  post-receive   Trigger deployment, notifieringar               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Hook             | Nar                    | Anvandning                    |
|------------------|------------------------|-------------------------------|
| pre-commit       | Fore commit skapas     | Lint, format, unit tests      |
| commit-msg       | Efter meddelande       | Validera Conventional Commits |
| pre-push         | Fore push till remote  | Full test suite, build        |
| post-receive     | Efter server tar emot  | Deploy, notifiera             |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Hooks

```bash
# Hooks ligger i .git/hooks/
ls .git/hooks/                       # Visar sample-hooks

# Samples har .sample extension - ta bort för att aktivera
cd .git/hooks
cp pre-commit.sample pre-commit      # Kopiera sample
chmod +x pre-commit                  # Gör körbar

# Eller skapa egen:
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "Running pre-commit hook..."

# Kör linting
npm run lint
if [ $? -ne 0 ]; then
    echo "Lint failed! Fix errors before committing."
    exit 1
fi

echo "Pre-commit passed!"
exit 0
EOF
chmod +x .git/hooks/pre-commit
```

---

## Pre-commit hook exempel

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Färger för output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
NC='\\033[0m' # No Color

echo "🔍 Running pre-commit checks..."

# 1. Kolla efter debug-statements
if git diff --cached --name-only | xargs grep -l "console.log\\|debugger\\|print(" 2>/dev/null; then
    echo -e "${RED}❌ Found debug statements! Remove before committing.${NC}"
    exit 1
fi

# 2. Kör linting på staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.(js|ts|tsx)$')
if [ -n "$STAGED_FILES" ]; then
    echo "Running ESLint on staged files..."
    echo "$STAGED_FILES" | xargs npx eslint
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ ESLint failed!${NC}"
        exit 1
    fi
fi

# 3. Kör TypeScript check
if [ -f "tsconfig.json" ]; then
    echo "Running TypeScript check..."
    npx tsc --noEmit
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ TypeScript errors!${NC}"
        exit 1
    fi
fi

# 4. Kör tester (snabba unit tests)
echo "Running tests..."
npm test -- --passWithNoTests
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Tests failed!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All checks passed!${NC}"
exit 0
```

---

## Commit-msg hook

```bash
#!/bin/bash
# .git/hooks/commit-msg
# Validerar att commit-meddelanden följer Conventional Commits

commit_msg_file=$1
commit_msg=$(cat "$commit_msg_file")

# Regex för Conventional Commits
pattern="^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)(\\(.+\\))?: .{1,50}"

if ! echo "$commit_msg" | grep -qE "$pattern"; then
    echo "❌ Invalid commit message format!"
    echo ""
    echo "Expected format: type(scope): description"
    echo ""
    echo "Types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert"
    echo ""
    echo "Examples:"
    echo "  feat(auth): add JWT token refresh"
    echo "  fix(api): handle null user response"
    echo "  docs(readme): update installation steps"
    exit 1
fi

echo "✅ Commit message valid"
exit 0
```

---

## Pre-push hook

```bash
#!/bin/bash
# .git/hooks/pre-push

echo "🚀 Running pre-push checks..."

# Förhindra push till main/master utan PR
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\\(.*\\),\\1,')
if [ "$current_branch" = "main" ] || [ "$current_branch" = "master" ]; then
    echo "❌ Direct push to $current_branch is not allowed!"
    echo "Please create a pull request instead."
    exit 1
fi

# Kör full test suite
echo "Running full test suite..."
npm test
if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Fix before pushing."
    exit 1
fi

# Bygg för att säkerställa att det kompilerar
echo "Running build..."
npm run build
if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

echo "✅ Pre-push checks passed!"
exit 0
```

---

## Husky (rekommenderat)

```bash
# Husky hanterar hooks och gör dem versionshanterade
# Hooks i .git/hooks/ versionshanteras INTE

# Installera Husky
npm install husky --save-dev

# Initiera Husky
npx husky init                       # Skapar .husky/ directory

# Skapa pre-commit hook
echo "npm run lint" > .husky/pre-commit

# Skapa commit-msg hook
echo 'npx commitlint --edit "$1"' > .husky/commit-msg

# Nu är hooks versionshanterade i .husky/
# Teamet får dem automatiskt vid npm install
```

---

## lint-staged

```bash
# Kör linting bara på staged files (snabbare)
npm install lint-staged --save-dev

# package.json
{
  "lint-staged": {
    "*.{js,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,md}": [
      "prettier --write"
    ]
  }
}

# .husky/pre-commit
npx lint-staged
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Hooks                     | Scripts som kors vid Git-events                     |
| pre-commit                | For linting, formatering, snabba tester             |
| commit-msg                | Validera commit-meddelanden                         |
| Husky                     | Versionshanterar hooks, teamet far automatiskt      |
| lint-staged               | Kor checks BARA pa staged files (snabbt)            |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- .git/hooks/ versionshanteras INTE - anvand Husky
- Hooks maste vara executable: chmod +x
- Exit 0 = OK, Exit non-zero = blockera
- lint-staged ar mycket snabbare an att kora pa alla filer
- Conventional Commits + commitlint = automatisk changelog
""",
        },
        {
            "title": "Git Configuration & Aliases",
            "slug": "git-configuration-aliases",
            "difficulty": "beginner",
            "content": """
# Git Configuration & Aliases

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan config/aliases           | Med config/aliases            |
|---------------------------|-------------------------------|-------------------------------|
| Vanliga kommandon         | git log --oneline --graph...  | git lg                        |
| Pull-strategi             | Merge commits overallt        | Rebase som default            |
| Credentials               | Ange varje gang               | Cached/keychain               |
| Misstag                   | Push till main direkt         | Branch protection hints       |

Professionella utvecklare har optimerade Git-konfigurationer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Konfigurationsnivaer

```
┌─────────────────────────────────────────────────────────────────┐
│                  GIT CONFIG HIERARCHY                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PRIORITET (hogst forst):                                       │
│                                                                 │
│  ┌─────────────────┐                                            │
│  │  LOCAL          │  .git/config      Repo-specifik            │
│  │  --local        │  Overskriver allt                          │
│  └────────┬────────┘                                            │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                            │
│  │  GLOBAL         │  ~/.gitconfig     Din anvandare            │
│  │  --global       │  Rekommenderat for personliga settings     │
│  └────────┬────────┘                                            │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                            │
│  │  SYSTEM         │  /etc/gitconfig   Alla anvandare           │
│  │  --system       │  Sallan anvand                             │
│  └─────────────────┘                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Konfiguration

```bash
# Obligatoriskt: identitet
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.se"

# Visa konfiguration
git config --list                    # All config
git config --list --show-origin      # Med källa
git config user.name                 # Specifik inställning

# Default branch
git config --global init.defaultBranch main  # main istället för master

# Default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim
git config --global core.editor "nano"         # Nano

# Radändningar (viktigt för cross-platform)
git config --global core.autocrlf input  # Mac/Linux
git config --global core.autocrlf true   # Windows
```

---

## Avancerad konfiguration

```bash
# Pull-strategi (undvik merge commits)
git config --global pull.rebase true    # Rebase vid pull
git config --global pull.ff only        # Bara fast-forward

# Push-beteende
git config --global push.default current  # Pusha till samma branch-namn
git config --global push.autoSetupRemote true  # Auto-setup remote tracking
git config --global push.followTags true  # Pusha annoterade taggar

# Diff och merge
git config --global merge.conflictstyle diff3  # Visa gemensam ancestor
git config --global diff.colorMoved zebra      # Färga flyttade rader

# Credential caching
git config --global credential.helper cache    # Cache i minnet (15 min)
git config --global credential.helper 'cache --timeout=3600'  # 1 timme
git config --global credential.helper store    # Spara permanent (osäkert)
git config --global credential.helper osxkeychain  # macOS Keychain
```

---

## Git aliases

```bash
# Skapa aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.sw switch

# Använd:
git st                               # = git status
git co main                          # = git checkout main
git br                               # = git branch

# Mer avancerade aliases
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "reset HEAD --"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.amend "commit --amend --no-edit"

# Använd:
git lg                               # Fin commit-graf
git last                             # Senaste commit
git unstage file.txt                 # Ta bort från staging
git undo                             # Ångra senaste commit
git amend                            # Lägg till i senaste commit
```

---

## Produktiv .gitconfig

```ini
# ~/.gitconfig

[user]
    name = Ditt Namn
    email = din@email.se

[init]
    defaultBranch = main

[core]
    editor = code --wait
    autocrlf = input
    excludesFile = ~/.gitignore_global
    pager = less -FRX

[pull]
    rebase = true
    ff = only

[push]
    default = current
    autoSetupRemote = true
    followTags = true

[merge]
    conflictstyle = diff3

[diff]
    colorMoved = zebra

[alias]
    # Basics
    st = status
    co = checkout
    sw = switch
    br = branch
    ci = commit

    # Logging
    lg = log --oneline --graph --all --decorate
    ll = log --oneline -20
    last = log -1 HEAD --stat

    # Undo
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
    discard = checkout --

    # Shortcuts
    amend = commit --amend --no-edit
    fixup = commit --fixup
    please = push --force-with-lease

    # Info
    aliases = config --get-regexp alias
    branches = branch -a
    tags = tag -l
    remotes = remote -v

    # Workflow
    save = !git add -A && git commit -m 'SAVEPOINT'
    wip = !git add -u && git commit -m 'WIP'
    wipe = !git add -A && git commit -qm 'WIPE SAVEPOINT' && git reset HEAD~1 --hard

[color]
    ui = auto
    branch = auto
    diff = auto
    status = auto

[color "branch"]
    current = yellow reverse
    local = yellow
    remote = green

[color "status"]
    added = green
    changed = yellow
    untracked = red
```

---

## Global gitignore

```bash
# Skapa global gitignore
touch ~/.gitignore_global
git config --global core.excludesFile ~/.gitignore_global

# ~/.gitignore_global innehåll:
cat > ~/.gitignore_global << 'EOF'
# OS-filer
.DS_Store
.DS_Store?
._*
Thumbs.db
ehthumbs.db

# Editor-filer
*.swp
*.swo
*~
.idea/
.vscode/
*.sublime-*

# Debug
*.log
npm-debug.log*

# Env-filer (backup)
.env.local
.env.*.local
EOF
```

---

## Redigera config direkt

```bash
# Öppna global config i editor
git config --global --edit           # ~/.gitconfig

# Öppna local config
git config --edit                    # .git/config

# Ta bort inställning
git config --global --unset alias.st

# Ta bort en sektion
git config --global --remove-section alias
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Tre nivaer                | system - global - local (local vinner)              |
| --global                  | For personliga installningar                        |
| Aliases                   | Sparar tid: git lg istallet for lang logg           |
| pull.rebase = true        | Ger renare historik som default                     |
| Global gitignore          | For OS- och editor-filer (.DS_Store, .idea/)        |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Satt upp din identitet FORST: user.name och user.email
- Aliases ar personliga - skapa for kommandon du anvander ofta
- git config --global --edit for att redigera direkt
- Dela bra aliases med teamet via dokumentation
- Global gitignore forhindrar att .DS_Store hamnar i commits
""",
        },
        {
            "title": "Submodules & Monorepos",
            "slug": "submodules-monorepos",
            "difficulty": "advanced",
            "content": """
# Submodules & Monorepos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan strategi                 | Med submodules/monorepo       |
|---------------------------|-------------------------------|-------------------------------|
| Delad kod                 | Copy-paste, divergerar        | En kalla, synkad              |
| Beroenden                 | npm install fran npm          | Lokal utveckling, snabbare    |
| Microservices             | 20 separata repos             | Monorepo, atomara commits     |
| Libraries                 | Publicera till npm            | Submodule, pinnad version     |

Storre projekt kraver strukturerad kodhantering.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Submodules vs Monorepo

```
┌─────────────────────────────────────────────────────────────────┐
│                SUBMODULES vs MONOREPO                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SUBMODULES                      MONOREPO                       │
│  ──────────                      ────────                       │
│                                                                 │
│  repo-main/                      company/                       │
│  ├── src/                        ├── apps/                      │
│  ├── libs/                       │   ├── web/                   │
│  │   └── shared/ ──► repo        │   ├── api/                   │
│  └── .gitmodules                 │   └── mobile/                │
│                                  ├── packages/                  │
│  Separata repos                  │   ├── ui/                    │
│  Pinnades till commit            │   └── utils/                 │
│  Explicit version                └── turbo.json                 │
│                                                                 │
│                                  Allt i ett repo                │
│                                  Atomara commits                │
│                                  Enklare refactoring            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Aspekt           | Submodules                   | Monorepo                      |
|------------------|------------------------------|-------------------------------|
| Versionshantering| Pinnades till commit         | Alltid senaste                |
| Atomara commits  | Nej, separata repos          | Ja, en commit for alla        |
| CI/CD            | Per-repo pipelines           | Intelligent caching           |
| Bast for         | Externa beroenden            | Intern kod, team-projekt      |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Git Submodules

```bash
# Lägg till submodule
git submodule add https://github.com/user/library.git libs/library
# Skapar .gitmodules fil och clonar repo

# .gitmodules innehåll:
# [submodule "libs/library"]
#     path = libs/library
#     url = https://github.com/user/library.git

# Commita submodule-tillägget
git add .gitmodules libs/library
git commit -m "Add library submodule"

# Klona repo med submodules
git clone --recurse-submodules https://github.com/user/project.git

# Eller efter vanlig clone:
git submodule init                   # Registrera submodules
git submodule update                 # Klona innehåll

# Kombination:
git submodule update --init --recursive  # Init + update + nested submodules
```

---

## Uppdatera submodules

```bash
# Gå in i submodule
cd libs/library                      # Det är ett vanligt Git-repo

# Uppdatera till senaste
git fetch                            # Hämta senaste
git checkout main                    # Byt till main
git pull                             # Dra ner ändringar

# Gå tillbaka och commita
cd ../..                             # Tillbaka till parent
git add libs/library                 # Stage ny commit-referens
git commit -m "Update library to latest"

# Eller uppdatera alla submodules
git submodule update --remote        # Uppdaterar alla till remote HEAD

# Uppdatera en specifik
git submodule update --remote libs/library
```

---

## Arbeta med submodules

```bash
# Status för submodules
git submodule status                 # Visar commit och path

# Kör kommando i alla submodules
git submodule foreach 'git status'
git submodule foreach 'git checkout main && git pull'

# Ta bort submodule (flera steg)
git submodule deinit libs/library    # Ta bort från config
git rm libs/library                  # Ta bort från index
rm -rf .git/modules/libs/library     # Ta bort cached data
git commit -m "Remove library submodule"

# Byt URL för submodule
git config --file=.gitmodules submodule.libs/library.url NEW_URL
git submodule sync                   # Synka till .git/config
git submodule update --init --remote
```

---

## Monorepo-struktur

```bash
# Typisk monorepo-struktur
mycompany/
├── apps/
│   ├── web/                         # Frontend app
│   │   ├── src/
│   │   └── package.json
│   ├── api/                         # Backend API
│   │   ├── src/
│   │   └── package.json
│   └── mobile/                      # Mobile app
│       ├── src/
│       └── package.json
├── packages/
│   ├── ui/                          # Shared UI components
│   │   ├── src/
│   │   └── package.json
│   ├── utils/                       # Shared utilities
│   │   └── package.json
│   └── config/                      # Shared configs
│       └── package.json
├── package.json                     # Root package.json
├── turbo.json                       # Turborepo config
└── pnpm-workspace.yaml              # Workspace definition
```

---

## Turborepo setup

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
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

```bash
# Kör kommandon i monorepo
turbo run build                      # Bygger allt med caching
turbo run build --filter=web         # Bara web-appen
turbo run test --filter=./packages/* # Bara packages
turbo run dev --parallel             # Kör dev parallellt
```

---

## Sparse checkout (för stora monorepos)

```bash
# Klona bara en del av ett stort repo

# Ny feature (Git 2.25+)
git clone --filter=blob:none --sparse https://github.com/big/monorepo.git
cd monorepo

# Välj vad du vill ha
git sparse-checkout init --cone
git sparse-checkout set apps/web packages/ui

# Nu har du bara dessa kataloger
ls                                   # apps/ packages/
ls apps/                             # web/
ls packages/                         # ui/

# Lägg till fler senare
git sparse-checkout add apps/api

# Visa vad som är inkluderat
git sparse-checkout list

# Tillbaka till full checkout
git sparse-checkout disable
```

---

## Git worktrees för monorepo

```bash
# Arbeta på flera delar av monorepo samtidigt

# Skapa worktree för specifik app
git worktree add ../web-feature apps/web
cd ../web-feature
# Arbeta bara på web-appen

# Skapa worktree för hotfix
git worktree add -b hotfix-api ../api-hotfix main
cd ../api-hotfix
# Fixa något i API:et

# Kombinera med sparse checkout for stora repos
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Submodules                | Inkluderar externa repos vid specifik commit        |
| --recurse-submodules      | Vid clone for att fa all kod                        |
| Monorepo                  | Allt i ett repo, kraver Turborepo/Nx                |
| Sparse checkout           | Klona bara delar av stora repos                     |
| Worktrees                 | Parallellt arbete i monorepos                       |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Submodules ar komplexa - dokumentera for teamet
- git submodule update --init --recursive vid clone
- Monorepo kraver verktyg: Turborepo, Nx, eller Lerna
- Sparse checkout for att spara tid vid clone
- Submodules for externa beroenden, monorepo for intern kod
""",
        },
        {
            "title": "Git Bisect & Debugging",
            "slug": "git-bisect-debugging",
            "difficulty": "advanced",
            "content": """
# Git Bisect & Debugging

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan bisect                   | Med bisect                    |
|---------------------------|-------------------------------|-------------------------------|
| Bugg i prod               | Manuellt leta, timmar         | Binarsokning, minuter         |
| 100 commits sedan OK      | Testa 50 i snitt              | Testa ~7                      |
| Regression                | "Nagon maste ha andrat..."    | Exakt commit identifierad     |
| Accountability            | Gissning                      | git blame visar vem           |

git bisect ar kraftfullt for att hitta exakt vilken commit som introducerade en bugg.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bisect Visualisering

```
┌─────────────────────────────────────────────────────────────────┐
│                    BINARY SEARCH                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1000 commits att soka igenom?                                  │
│                                                                 │
│  LINJAR SOKNING:    ~500 tester i snitt                        │
│  BINARSOKNING:      ~10 tester (log2 1000)                     │
│                                                                 │
│  [GOOD]────────────────[?]────────────────[BAD]                │
│    │                    │                    │                  │
│    v1.0.0               │                  HEAD                 │
│                         │                                       │
│                    testa mitten                                 │
│                         │                                       │
│                   ┌─────┴─────┐                                 │
│                   │           │                                 │
│                  BAD?       GOOD?                               │
│                   │           │                                 │
│              soka har     soka har                              │
│                                                                 │
│  Varje test halverar sokomradet!                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Bisect

```bash
# Starta bisect
git bisect start

# Markera aktuell commit som dålig (har buggen)
git bisect bad                       # HEAD är bad

# Markera en känd bra commit
git bisect good v1.0.0               # v1.0.0 var ok
# Eller med commit-hash:
git bisect good abc123

# Git checkar ut mitten-commit
# Bisecting: 50 revisions left to test after this

# Testa om buggen finns
npm test                             # Eller manuell test

# Markera resultatet
git bisect good                      # Ingen bugg här
# eller
git bisect bad                       # Buggen finns

# Git checkar ut nästa commit att testa
# Fortsätt tills Git hittar första bad commit

# När klar:
# abc123 is the first bad commit

# Avsluta bisect
git bisect reset                     # Återgå till original HEAD
```

---

## Automatisk bisect

```bash
# Automatisera med ett test-script
git bisect start
git bisect bad HEAD
git bisect good v1.0.0

# Kör script automatiskt
# Exit code 0 = good, non-zero = bad
git bisect run npm test

# Eller med custom script
git bisect run ./test-bug.sh

# Script-exempel:
cat > test-bug.sh << 'EOF'
#!/bin/bash
# Testa om buggen finns

# Bygg först
npm ci || exit 125                   # 125 = skip denna commit (kan ej bygga)

# Kör specifikt test
npm test -- --grep "user login"
exit $?                              # 0 = pass = good, annat = fail = bad
EOF
chmod +x test-bug.sh

git bisect run ./test-bug.sh
# Git kör automatiskt och hittar första bad commit
```

---

## Bisect med skip

```bash
# Ibland kan en commit inte testas (bygger ej, etc.)
git bisect skip                      # Hoppa över aktuell commit

# Hoppa över range
git bisect skip abc123..def456

# Vid automatisk körning, exit 125 = skip
# Användbart för commits som inte kompilerar
```

---

## Git blame

```bash
# Vem ändrade den här raden senast?
git blame filename.js                # Visar varje rad med commit-info

# Output:
# abc123 (Anna 2024-01-15 10:30:45 +0100  1) function login() {
# def456 (Bob  2024-01-20 14:22:33 +0100  2)   validateInput();
# abc123 (Anna 2024-01-15 10:30:45 +0100  3)   authenticate();

# Visa specifika rader
git blame -L 10,20 filename.js       # Bara rad 10-20
git blame -L 10,+5 filename.js       # Rad 10 + 5 rader

# Ignorera whitespace-ändringar
git blame -w filename.js

# Visa commit-meddelanden
git blame -c filename.js             # Mer detaljer

# Följ genom renames
git blame -M filename.js             # Detektera flytt inom fil
git blame -C filename.js             # Detektera kopiering mellan filer
git blame -C -C filename.js          # Ännu aggressivare

# Se äldre blame (före en commit)
git blame abc123^ -- filename.js     # Blame vid parent till abc123
```

---

## Git log för debugging

```bash
# Hitta commits som rörde en specifik fil
git log --oneline -- filename.js

# Sök i commit-meddelanden
git log --grep="fix login"           # Commits med "fix login"
git log --grep="bug" --grep="auth" --all-match  # Båda orden

# Sök i kod-ändringar
git log -S "functionName"            # Commits som la till/tog bort strängen
git log -G "regex.*pattern"          # Regex-sökning

# Visa vad som ändrades
git log -p -- filename.js            # Patches för filen
git log -p -S "functionName"         # Patches där strängen ändrades

# Begränsa tidsperiod
git log --since="2024-01-01" --until="2024-01-31"
git log --since="2 weeks ago"
```

---

## Git show för inspektion

```bash
# Visa en commit i detalj
git show abc123                      # Commit + diff

# Visa specifik fil vid commit
git show abc123:filename.js          # Filens innehåll vid den commit

# Visa bara filnamn som ändrades
git show --stat abc123
git show --name-only abc123

# Visa diff för specifik fil
git show abc123 -- filename.js

# Jämför fil mellan commits
git diff abc123 def456 -- filename.js
```

---

## Avancerad debugging

```bash
# Hitta vem som introducerade en bugg i en funktion
git log -L :functionName:filename.js
# Visar historik för funktionen

# Pickaxe: hitta när en sträng la till/togs bort
git log -S "buggy_code" --source --all

# Hitta merge som introducerade ändring
git log --ancestry-path abc123..HEAD

# Kolla vilka branches som innehåller en commit
git branch --contains abc123
git branch -r --contains abc123      # Remote branches

# Hitta gemensam ancestor
git merge-base main feature          # Senaste gemensamma commit
```

---

## Debugging checklista

```bash
# 1. Identifiera senast kända bra version
git log --oneline                    # Hitta commit/tag

# 2. Verifiera att buggen finns nu
npm test                             # Eller manuell test

# 3. Starta bisect
git bisect start
git bisect bad HEAD
git bisect good v1.0.0

# 4. Automatisera om möjligt
git bisect run npm test

# 5. När commit hittats, analysera
git show <bad-commit>                # Se ändringarna
git blame -L :function:file.js       # Kontext

# 6. Avsluta och fixa
git bisect reset
# Skapa fix baserad pa vad du hittat
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| git bisect                | Binarsokning - ~7 tester for 100 commits            |
| git bisect run            | Automatisera med test-script                        |
| git blame                 | Visar vem som andrade varje rad                     |
| git log -S                | Hittar commits som andrade en strang                |
| Kombinera                 | bisect + blame + log for effektiv debugging         |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- git bisect ar MAKALOST for att hitta regressioner
- Automatisera med git bisect run nar mojligt
- Exit 125 = skip (commit kan ej testas)
- git blame -w ignorerar whitespace-andringar
- Avsluta ALLTID med git bisect reset
""",
        },
        {
            "title": "Git LFS & Large Files",
            "slug": "git-lfs-large-files",
            "difficulty": "advanced",
            "content": """
# Git LFS & Large Files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Utan LFS                      | Med LFS                       |
|---------------------------|-------------------------------|-------------------------------|
| Clone-tid                 | 10+ minuter                   | Sekunder                      |
| Repo-storlek              | 5 GB                          | 50 MB + on-demand             |
| CI/CD                     | Timeout vid clone             | Snabba pipelines              |
| Historik                  | Varje version av bild sparas  | Bara pekare i historik        |

Git ar optimerat for text. Stora binarfiler (bilder, videos, ML-modeller) kraver LFS.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LFS Arkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIT LFS WORKFLOW                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  UTAN LFS:                                                      │
│  ─────────                                                      │
│  .git/objects/                                                  │
│  ├── commit1 ──► image.psd (50 MB)                             │
│  ├── commit2 ──► image.psd (50 MB)  Varje version sparas!      │
│  └── commit3 ──► image.psd (50 MB)  = 150 MB for en fil        │
│                                                                 │
│  MED LFS:                                                       │
│  ────────                                                       │
│  .git/objects/                     LFS Server                   │
│  ├── commit1 ──► pekare (130 B)    ├── abc123.psd (50 MB)      │
│  ├── commit2 ──► pekare (130 B)    ├── def456.psd (50 MB)      │
│  └── commit3 ──► pekare (130 B)    └── ghi789.psd (50 MB)      │
│                                                                 │
│  Pekare i repo, faktiska filer pa LFS-server                   │
│  Laddas ned on-demand vid checkout                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installera Git LFS

```bash
# macOS
brew install git-lfs

# Ubuntu
sudo apt install git-lfs

# Windows
# Ladda ner från git-lfs.github.com

# Initiera LFS globalt (en gång)
git lfs install                      # Sätter upp hooks

# Verifiera installation
git lfs version
```

---

## Konfigurera LFS för repo

```bash
# Initiera i repo
cd myrepo
git lfs install                      # Lokalt för detta repo

# Spåra filtyper
git lfs track "*.psd"                # Photoshop-filer
git lfs track "*.zip"                # Zip-arkiv
git lfs track "*.pdf"                # PDF-dokument
git lfs track "*.mp4"                # Videos
git lfs track "*.png"                # Bilder

# Flera på en gång
git lfs track "*.jpg" "*.jpeg" "*.gif" "*.png"

# Spåra specifik fil
git lfs track "path/to/large-file.bin"

# Skapar/uppdaterar .gitattributes
cat .gitattributes
# *.psd filter=lfs diff=lfs merge=lfs -text
# *.zip filter=lfs diff=lfs merge=lfs -text

# VIKTIGT: Commita .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS for large files"
```

---

## Arbeta med LFS-filer

```bash
# Lägg till stor fil
git add large-video.mp4              # Normalt add
git commit -m "Add video"            # Normalt commit

# LFS hanterar automatiskt baserat på .gitattributes

# Verifiera att filen är LFS-tracked
git lfs ls-files                     # Lista LFS-filer
git lfs status                       # Status för LFS-filer

# Se vilka filer som spåras
cat .gitattributes

# Lista tracking patterns
git lfs track                        # Visar konfigurerade patterns
```

---

## Klona repo med LFS

```bash
# Normal clone hämtar LFS-filer automatiskt
git clone https://github.com/user/repo.git

# Clone utan LFS-filer (snabbare)
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/user/repo.git

# Hämta LFS-filer senare
git lfs pull                         # Hämtar alla LFS-filer

# Hämta selektivt
git lfs pull --include="*.png"       # Bara PNG
git lfs pull --exclude="*.mp4"       # Allt utom video
```

---

## LFS-kommandon

```bash
# Lista LFS-filer
git lfs ls-files                     # Alla LFS-filer i repo
git lfs ls-files --size              # Med storlek

# Status
git lfs status                       # Visa pending uploads

# Fetch/pull
git lfs fetch                        # Hämta till cache, checkout ej
git lfs pull                         # Hämta och checka ut
git lfs fetch --all                  # Hämta alla versioner (hela historiken)

# Push
git lfs push origin main             # Pusha LFS-objekt explicit
git lfs push --all origin            # Pusha alla LFS-objekt

# Prune gammal data
git lfs prune                        # Ta bort gamla lokala LFS-objekt
git lfs prune --dry-run              # Visa vad som skulle tas bort

# Migrera befintliga filer till LFS
git lfs migrate import --include="*.psd" --include-ref=main
# OBS: Skriver om historiken!
```

---

## Migrera befintligt repo till LFS

```bash
# VARNING: Migrera KRÄVER force push och påverkar alla som klonat!

# Analysera repo för stora filer
git lfs migrate info                 # Visa kandidater för LFS

# Output:
# migrate: Fetching remote refs: ..., done.
# migrate: Sorting commits: ..., done.
# migrate: Examining commits: 100% (500/500), done.
# *.zip    500 MB   20 files
# *.psd    350 MB   15 files
# *.mp4    1.2 GB    5 files

# Migrera specifika filtyper
git lfs migrate import --include="*.zip,*.psd,*.mp4"

# Migrera allt över viss storlek
git lfs migrate import --above=10mb

# Begränsa till specifik branch
git lfs migrate import --include="*.psd" --include-ref=main

# Force push (alla branches)
git push --force --all origin

# Alla i teamet måste:
# 1. Backa upp lokala ändringar
# 2. rm -rf repo && git clone ...
```

---

## Best practices

```bash
# 1. Konfigurera LFS INNAN du lägger till stora filer
git lfs track "*.psd"
git add .gitattributes
git commit -m "Configure LFS"
# SEN lägg till filer

# 2. Sätt upp i .gitattributes direkt
cat >> .gitattributes << 'EOF'
# Images
*.png filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text

# Videos
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs merge=lfs -text

# Archives
*.zip filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text

# ML Models
*.h5 filter=lfs diff=lfs merge=lfs -text
*.pkl filter=lfs diff=lfs merge=lfs -text
*.model filter=lfs diff=lfs merge=lfs -text
EOF

# 3. Undvik att committa secrets/credentials i LFS
# De går INTE att ta bort från LFS-historik enkelt

# 4. Sätt upp LFS-kvota på GitHub/GitLab
# Gratis tier har begränsningar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Git LFS                   | Lagrar stora filer separat - snabbare kloning       |
| git lfs track             | Kor FORE du lagger till stora filer                 |
| .gitattributes            | Maste committas och pushas                          |
| migrate import            | Skriver om historiken - kraver force push           |
| Timing                    | Satt upp LFS tidigt i projektet                     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- LFS = pekare i repo, filer pa separat server
- Gor git lfs track INNAN du lagger till filer
- .gitattributes maste vara med i forsta commit
- git lfs migrate skriver om HELA historiken
- Gratis tier har bandbreddsbegransningar
""",
        },
        {
            "title": "GitHub Features & Settings",
            "slug": "github-features-settings",
            "difficulty": "beginner",
            "content": """
# GitHub Features & Settings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Feature                   | DevOps-anvandning                                   |
|---------------------------|-----------------------------------------------------|
| Issues                    | Buggtracking, feature requests                      |
| Projects                  | Sprint-planering, Kanban                            |
| Discussions               | Team-kommunikation, RFC                             |
| Wiki                      | Dokumentation, runbooks                             |
| Templates                 | Standardiserade PRs och issues                      |

GitHub ar mer an Git-hosting - det ar en hel utvecklingsplattform.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitHub Platform Oversikt

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITHUB PLATFORM                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   ISSUES    │  │  PROJECTS   │  │ DISCUSSIONS │             │
│  │  Bug track  │  │   Kanban    │  │  Community  │             │
│  │  Features   │  │  Roadmap    │  │    Q&A      │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │    WIKI     │  │  ACTIONS    │  │  SECURITY   │             │
│  │    Docs     │  │   CI/CD     │  │  Scanning   │             │
│  │  Runbooks   │  │ Automation  │  │ Dependabot  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  PACKAGES   │  │  RELEASES   │  │   PAGES     │             │
│  │   Docker    │  │  Versions   │  │   Static    │             │
│  │    npm      │  │ Changelogs  │  │   Sites     │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Repository Settings

```yaml
# Settings → General

# Repository name
# Byt namn: Settings → General → Repository name
# OBS: Bryter länkar och clones!

# Default branch
# Settings → General → Default branch
# Ändra från master till main om nödvändigt

# Features (aktivera/avaktivera)
# ✅ Wikis - Dokumentation
# ✅ Issues - Buggrapporter och features
# ✅ Discussions - Community-forum
# ✅ Projects - Kanban/projekt
# ✅ Preserve this repository - Arkivering

# Merge button
# ✅ Allow merge commits
# ✅ Allow squash merging (rekommenderat)
# ✅ Allow rebase merging
# ✅ Always suggest updating PR branches
# ✅ Automatically delete head branches
```

---

## GitHub Issues

```markdown
# Issues för buggrapporter och features

# Skapa issue via GitHub UI
1. Gå till repo → Issues → New issue
2. Välj template (om det finns)
3. Fyll i titel och beskrivning
4. Lägg till labels, assignees, project

# Issue templates (.github/ISSUE_TEMPLATE/)

# bug_report.md
---
name: Bug Report
about: Report a bug
title: "[BUG] "
labels: bug
assignees: ''
---

## Describe the bug
A clear description of the bug.

## Steps to reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected behavior
What should happen.

## Screenshots
If applicable.

## Environment
- OS: [e.g. macOS 14]
- Browser: [e.g. Chrome 120]
- Version: [e.g. v1.2.0]

# feature_request.md
---
name: Feature Request
about: Suggest a new feature
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## Problem
What problem does this solve?

## Solution
Describe the solution you'd like.

## Alternatives
Alternative solutions considered.
```

---

## GitHub Projects

```yaml
# Projects för projekthantering (Kanban/roadmap)

# Skapa projekt
1. Repo → Projects → New project
2. Välj template: Board, Table, Roadmap
3. Namnge projektet

# Board columns (typisk setup):
# - 📥 Backlog
# - 🔜 Ready
# - 🏃 In Progress
# - 👀 In Review
# - ✅ Done

# Lägg till issues i projekt
# 1. Öppna issue → Projects → Välj projekt
# 2. Dra issue till rätt column

# Automatisering (built-in)
# - Auto-add issues with label
# - Auto-move when PR merged
# - Auto-close when moved to Done

# Custom fields
# - Priority (High, Medium, Low)
# - Estimate (1, 2, 3, 5, 8 points)
# - Sprint (Sprint 1, Sprint 2...)
```

---

## Labels

```bash
# Standardlabels att ha:

# Type
bug           # 🔴 Fel i koden
enhancement   # 🟢 Ny feature
documentation # 📘 Dokumentation
question      # 🟣 Fråga

# Priority
priority: high    # 🔴 Akut
priority: medium  # 🟡 Normal
priority: low     # 🟢 Kan vänta

# Status
wontfix       # ⚪ Kommer ej fixas
duplicate     # ⚪ Duplicat
help wanted   # 🟡 Hjälp behövs
good first issue  # 🟢 Bra för nybörjare

# Area
frontend      # 🔵 Frontend-kod
backend       # 🟤 Backend-kod
devops        # 🟠 Infrastructure
testing       # 🟣 Tester
```

---

## GitHub Discussions

```markdown
# Discussions för community-interaktion

# Kategorier att sätta upp:
📣 Announcements  - Nyheter (bara maintainers)
💬 General        - Allmän diskussion
💡 Ideas          - Förslag
🙏 Q&A            - Frågor och svar
🙌 Show and tell  - Visa upp projekt

# Aktivera:
Settings → Features → ✅ Discussions

# Moderering:
- Pin viktiga diskussioner
- Lock avslutade diskussioner
- Mark answers i Q&A
```

---

## GitHub Wiki

```markdown
# Wiki för dokumentation

# Aktivera:
Settings → Features → ✅ Wikis

# Struktur:
Home              # Startsida
Getting-Started   # Kom igång
Installation      # Installation
Configuration     # Konfiguration
API-Reference     # API-docs
FAQ               # Vanliga frågor

# Klona wiki lokalt
git clone https://github.com/user/repo.wiki.git

# Nu kan du redigera wiki med Git!
cd repo.wiki
echo "# FAQ" > FAQ.md
git add FAQ.md
git commit -m "Add FAQ page"
git push
```

---

## Security Features

```yaml
# Settings → Security

# Dependabot
# Automatiska säkerhetsuppdateringar av dependencies

# Security advisories
# Privat rapportera sårbarheter

# Code scanning
# Automatisk analys med CodeQL

# Secret scanning
# Detekterar läckta API-nycklar etc.

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

---

## Repository Templates

```bash
# Skapa template-repo
Settings → ✅ Template repository

# Användning:
# "Use this template" → Skapar nytt repo från template

# Template bör innehålla:
.github/
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
├── PULL_REQUEST_TEMPLATE.md
├── workflows/
│   └── ci.yml
└── dependabot.yml
README.md
LICENSE
.gitignore
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| GitHub                    | Mer an Git - Issues, Projects, Discussions          |
| Issue templates           | Standardiserar buggrapporter och feature requests   |
| Projects                  | Kanban-boards for planering och sprinthantering     |
| Dependabot                | Haller dependencies uppdaterade automatiskt         |
| Template repos            | Sparar tid vid nya projekt                          |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Aktivera Issue templates for konsekvent rapportering
- Projects kan automatisera issue-hantering
- Dependabot.yml kravs for automatiska uppdateringar
- Wiki kan klonas och redigeras som vanligt Git-repo
- Template repos sparar setup-tid for nya projekt
""",
        },
        {
            "title": "GitHub Security & Access Control",
            "slug": "github-security-access-control",
            "difficulty": "intermediate",
            "content": """
# GitHub Security & Access Control

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Risk                      | Konsekvens                     | Prevention                    |
|---------------------------|--------------------------------|-------------------------------|
| Lackt API-nyckel          | Infrastruktur-kompromiss       | Secret scanning               |
| For breda behorigheter    | Obehorig access                | Fine-grained PATs             |
| Direkt push till main     | Trasig produktion              | Branch protection             |
| Sarbara dependencies      | Sakerhetshall                  | Dependabot                    |

Sakerhet i repositories ar kritiskt - en lackt credential kan kosta miljoner.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitHub Sakerhetslager

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITHUB SECURITY LAYERS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  AUTENTISERING              AUKTORISERING                       │
│  ──────────────             ──────────────                      │
│  - SSH-nycklar              - Repo permissions                  │
│  - PATs (tokens)            - Branch protection                 │
│  - 2FA / SAML SSO           - Team access                       │
│  - Deploy keys              - CODEOWNERS                        │
│                                                                 │
│  SCANNING                   AUDIT                               │
│  ────────                   ─────                               │
│  - Secret scanning          - Audit logs                        │
│  - Dependabot               - Security advisories               │
│  - CodeQL                   - Compliance reports                │
│  - Push protection          - API activity                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Personal Access Tokens (PAT)

```bash
# PAT ersätter lösenord för Git-operationer

# Skapa token:
# Settings → Developer settings → Personal access tokens
# → Tokens (classic) eller Fine-grained tokens

# Classic token scopes:
# repo         - Full kontroll över privata repos
# workflow     - Uppdatera GitHub Actions
# write:packages - Pusha packages
# read:org     - Läsa org-info

# Fine-grained tokens (rekommenderat)
# - Begränsa till specifika repos
# - Granular permissions
# - Utgångsdatum

# Använd token:
git clone https://github.com/user/private-repo.git
# Username: your-username
# Password: ghp_xxxxxxxxxxxx (token, inte lösenord)

# Eller sätt som credential:
git config --global credential.helper store
# Första gången du anger token sparas det
```

---

## Deploy Keys

```bash
# Deploy keys = SSH-nycklar för ett specifikt repo
# Bättre än PAT för CI/CD

# Generera nyckel
ssh-keygen -t ed25519 -C "deploy-key-production"
# Spara som deploy_key (inget lösenord för automation)

# Lägg till i repo:
# Settings → Deploy keys → Add deploy key
# Klistra in publika nyckeln (.pub)
# ✅ Allow write access (om du behöver pusha)

# Använd i CI/CD:
# 1. Spara privata nyckeln som secret
# 2. Konfigurera SSH i workflow

# GitHub Actions exempel:
- uses: webfactory/ssh-agent@v0.8.0
  with:
    ssh-private-key: ${{ secrets.DEPLOY_KEY }}

- run: git clone git@github.com:user/repo.git
```

---

## Branch Protection

```yaml
# Settings → Branches → Add branch protection rule

# Branch name pattern: main

# Protect matching branches:

# ✅ Require a pull request before merging
    # Require approvals: 2
    # Dismiss stale reviews when new commits pushed
    # Require review from code owners
    # Restrict who can dismiss reviews

# ✅ Require status checks to pass before merging
    # Require branches to be up to date
    # Status checks: ci, test, lint

# ✅ Require conversation resolution before merging

# ✅ Require signed commits

# ✅ Require linear history (no merge commits)

# ✅ Restrict who can push to matching branches
    # Endast specifika team/personer

# ✅ Rules applied to everyone including admins

# ❌ Allow force pushes
# ❌ Allow deletions
```

---

## Secret Scanning

```yaml
# GitHub skannar automatiskt efter läckta secrets

# Detekterar:
# - API keys (AWS, Azure, GCP)
# - OAuth tokens
# - SSH private keys
# - Database credentials
# - Payment credentials

# Settings → Security → Secret scanning
# ✅ Enable

# Push protection (blockerar push med secrets)
# Settings → Code security → Secret scanning → Push protection

# Custom patterns:
# Settings → Security → Secret scanning → Custom patterns
# Lägg till egna regex för interna credentials
```

---

## Dependabot

```yaml
# .github/dependabot.yml

version: 2
updates:
  # JavaScript/npm
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
      timezone: "Europe/Stockholm"
    open-pull-requests-limit: 10
    reviewers:
      - "security-team"
    labels:
      - "dependencies"
      - "security"
    groups:
      dev-dependencies:
        patterns:
          - "*"
        exclude-patterns:
          - "react*"
          - "next*"
        update-types:
          - "minor"
          - "patch"

  # Docker
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"

  # Python
  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "daily"
```

---

## Code Scanning (CodeQL)

```yaml
# .github/workflows/codeql.yml

name: "CodeQL"

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Varje söndag

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      actions: read
      contents: read

    strategy:
      matrix:
        language: ['javascript', 'python']

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform Analysis
        uses: github/codeql-action/analyze@v3
```

---

## Team & Organization Access

```yaml
# Organization-nivå säkerhet

# Teams:
# - developers (write)
# - maintainers (maintain)
# - admins (admin)

# Repository access:
# Settings → Collaborators and teams

# Base permissions:
# Organization Settings → Member privileges
# Base permission: None/Read/Write

# SAML SSO:
# Organization Settings → Security → SAML SSO
# Kräver företags-login

# 2FA requirement:
# Organization Settings → Security
# ✅ Require 2FA for everyone
```

---

## Audit Log

```bash
# Organization Settings → Audit log

# Filtrera:
# action:repo.create          # Repo skapade
# action:repo.destroy         # Repo borttagna
# actor:username              # Av specifik person
# repo:org/repo               # I specifikt repo
# created:>2024-01-01         # Efter datum

# Exportera:
# Audit log → Export → JSON/CSV

# API:
curl -H "Authorization: token $TOKEN" \\
  "https://api.github.com/orgs/myorg/audit-log?phrase=action:repo.create"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Fine-grained PATs         | Sakrare an classic tokens - granular permissions    |
| Deploy keys               | For CI/CD - begransade till ETT repo                |
| Branch protection         | Forhindrar direkta pushes till main                 |
| Secret scanning           | Blockerar lackta credentials automatiskt            |
| Dependabot                | Haller dependencies sakra med auto-PRs              |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Fine-grained PATs med utgangsdatum och repo-begransning
- Deploy keys kan inte atervandas mellan repos
- Branch protection rules galler ALLA inklusive admins
- Secret scanning push protection ar on by default
- CodeQL hittar sarbarheter i koden sjalv
""",
        },
        {
            "title": "Advanced Git Internals",
            "slug": "advanced-git-internals",
            "difficulty": "advanced",
            "content": """
# Advanced Git Internals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario                  | Krav pa Git-kunskap                                 |
|---------------------------|-----------------------------------------------------|
| Aterstalla forlorad kod   | Forsta objektmodellen och reflog                    |
| Felsoka konstiga beteenden| Veta hur refs och index fungerar                    |
| Optimera stora repos      | Forsta packfiles och gc                             |
| Skripta Git-operationer   | Anvanda plumbing-kommandon                          |

Forstaelse for Gits internals gor dig till en Git-mastare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Git Object Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIT OBJECT DATABASE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FYRA OBJEKTTYPER:                                              │
│                                                                 │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐                │
│  │   BLOB   │     │   TREE   │     │  COMMIT  │                │
│  │          │     │          │     │          │                │
│  │ Fildata  │◄────│ Katalog  │◄────│ Snapshot │                │
│  │ (binart) │     │ struktur │     │ +metadata│                │
│  └──────────┘     └──────────┘     └──────────┘                │
│                                          │                      │
│                                          ▼                      │
│                                    ┌──────────┐                │
│                                    │   TAG    │                │
│                                    │          │                │
│                                    │ Namngiven│                │
│                                    │  pekare  │                │
│                                    └──────────┘                │
│                                                                 │
│  SHA-1 hash: abc123def456...                                    │
│  Lagringsplats: .git/objects/ab/c123def456...                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Git Objects

```bash
# Inspektera objekt
git cat-file -t abc123               # Typ: blob/tree/commit/tag
git cat-file -p abc123               # Print innehåll
git cat-file -s abc123               # Storlek i bytes

# Hitta en blob (filinnehåll)
echo "Hello" | git hash-object --stdin  # Beräknar hash utan att spara
echo "Hello" | git hash-object -w --stdin  # Sparar objekt

# Skapa tree manuellt (avancerat)
git mktree                           # Läser tree-format från stdin

# Objekt-databasen
ls .git/objects/                     # Loose objects + packfiles
ls .git/objects/ab/                  # Objekt med hash som börjar "ab"
# abc123... → .git/objects/ab/c123...
```

---

## References (Refs)

```bash
# Refs är pekare till commits

# Branches
cat .git/refs/heads/main             # Commit-hash som main pekar på
git update-ref refs/heads/new-branch abc123  # Skapa branch manuellt

# Tags
cat .git/refs/tags/v1.0.0            # Commit/tag-objekt hash

# Remote tracking
cat .git/refs/remotes/origin/main    # Remote branch ref

# HEAD
cat .git/HEAD                        # ref: refs/heads/main (symbolic)
# Eller direkt hash vid detached HEAD

# Packed refs (optimering)
cat .git/packed-refs                 # Många refs i en fil

# Symbolic refs
git symbolic-ref HEAD                # Visar refs/heads/main
git symbolic-ref HEAD refs/heads/feature  # Byt branch utan checkout
```

---

## The Index (Staging Area)

```bash
# Index = .git/index (binärfil)

# Visa index-innehåll
git ls-files                         # Filer i index
git ls-files -s                      # Med mode, hash, stage number
git ls-files --debug                 # Detaljerad info

# Output:
# 100644 abc123 0 src/file.js
# mode   hash   stage filename
# stage: 0=normal, 1-3=merge conflict

# Manuell index-manipulation
git update-index --add --cacheinfo 100644,abc123,file.txt

# Visa diff mot index
git diff --cached                    # Staged changes
git diff-index HEAD                  # Index vs HEAD
```

---

## Packfiles

```bash
# Git packar objekt för effektivitet

# Skapa packfile manuellt
git gc                               # Garbage collection, skapar packfiles

# Lista packfiles
ls .git/objects/pack/
# pack-abc123.pack - Komprimerad data
# pack-abc123.idx  - Index för snabb lookup

# Inspektera packfile
git verify-pack -v .git/objects/pack/pack-*.idx

# Unpacka (för debugging)
git unpack-objects < .git/objects/pack/pack-*.pack

# Repack för optimering
git repack -a -d -f                  # Ompacka allt
```

---

## Garbage Collection

```bash
# Git lagrar allt - även "borttagna" objekt
# GC rensar unreachable objects

# Kör GC
git gc                               # Standard GC
git gc --aggressive                  # Grundligare (långsammare)
git gc --auto                        # Kör bara om nödvändigt

# Prune unreachable objects
git prune                            # Ta bort unreachable
git prune --dry-run                  # Visa vad som skulle tas bort
git prune --expire now               # Ta bort allt unreachable

# GC-inställningar
git config gc.auto 256               # Auto-GC vid 256 loose objects
git config gc.pruneExpire "2 weeks ago"  # Behåll 2 veckor

# Hitta dangling objects
git fsck                             # Filesystem check
git fsck --unreachable               # Lista unreachable
git fsck --dangling                  # Lista dangling (ej ref:ad)
```

---

## Plumbing Commands

```bash
# Porcelain = user-friendly (git add, commit)
# Plumbing = low-level (git hash-object, update-index)

# Skapa commit manuellt med plumbing

# 1. Skapa blob
echo "file content" | git hash-object -w --stdin
# → abc123

# 2. Skapa tree
git mktree << EOF
100644 blob abc123    filename.txt
EOF
# → def456

# 3. Skapa commit
git commit-tree def456 -m "Manual commit" -p HEAD
# → ghi789

# 4. Uppdatera branch
git update-ref refs/heads/main ghi789

# Andra plumbing:
git rev-parse HEAD                   # Resolve ref till hash
git rev-list HEAD                    # Lista commits
git diff-tree -r abc123 def456       # Diff mellan trees
git for-each-ref                     # Lista alla refs
```

---

## Debugging Repository Issues

```bash
# Verifiera integritet
git fsck                             # Check all objects
git fsck --full                      # Grundligare check
git fsck --strict                    # Strikt mode

# Reparera skadad repo
# Om .git/index är korrupt:
rm .git/index
git reset                            # Återskapar index

# Om objekt saknas:
git fetch origin                     # Hämta från remote
# eller klona på nytt

# Hitta stora objekt
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  awk '/^blob/ {print $3, $4}' |
  sort -rn |
  head -20

# Visa repo-statistik
git count-objects -v                 # Objektstatistik
git rev-list --all --count           # Antal commits
```

---

## Performance Optimization

```bash
# För stora repos

# Shallow clone
git clone --depth 1 https://github.com/big/repo.git
git fetch --unshallow                # Hämta full historik senare

# Partial clone (Git 2.22+)
git clone --filter=blob:none https://github.com/big/repo.git
# Blobs hämtas on-demand

# Sparse checkout
git sparse-checkout init --cone
git sparse-checkout set src/

# Commit graph (snabbare log)
git commit-graph write --reachable
git config core.commitGraph true

# Multi-pack index
git multi-pack-index write
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Objekttyper               | blob, tree, commit, tag - allt ar SHA-1 hashat      |
| Refs                      | Pekare till commits - branches och tags             |
| Index                     | Staging area - mellansteget fore commit             |
| Packfiles                 | Komprimerar objekt for effektivitet                 |
| git fsck                  | Verifiera och hitta problem i repo                  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- Git ar en content-addressable databas
- Allt identifieras med SHA-1 hash
- Refs ar bara textfiler med commit-hashar
- Packfiles skapas av git gc
- Dangling objects ar inte forlorade - bara unreferenced
""",
        },
        {
            "title": "Git for DevOps & Automation",
            "slug": "git-for-devops-automation",
            "difficulty": "advanced",
            "content": """
# Git for DevOps & Automation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Koncept                   | DevOps-anvandning                                   |
|---------------------------|-----------------------------------------------------|
| GitOps                    | Git som source of truth for infrastruktur           |
| IaC                       | Terraform/Ansible i versionskontroll                |
| CI/CD triggers            | Push/PR triggar deployment pipelines                |
| Audit trail               | Git log = compliance och spaarbarhet                |

Git ar fundamentet for modern DevOps och automation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitOps Arkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITOPS WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  DEVELOPER              GIT REPO                CLUSTER         │
│  ─────────              ────────                ───────         │
│                                                                 │
│  ┌─────────┐           ┌─────────┐           ┌─────────┐       │
│  │  Code   │──push────►│  main   │◄──sync────│  ArgoCD │       │
│  │ Change  │           │ branch  │           │  /Flux  │       │
│  └─────────┘           └─────────┘           └─────────┘       │
│       │                     │                     │             │
│       ▼                     ▼                     ▼             │
│  ┌─────────┐           ┌─────────┐           ┌─────────┐       │
│  │   PR    │──review──►│  merge  │──trigger─►│ deploy  │       │
│  │ Review  │           │         │           │         │       │
│  └─────────┘           └─────────┘           └─────────┘       │
│                                                                 │
│  Principer:                                                     │
│  1. Deklarativ  - Beskriv onskat tillstand                     │
│  2. Versioned   - Allt i Git                                    │
│  3. Automated   - PR = Deploy                                   │
│  4. Observed    - Kontinuerlig sync                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitOps-monster

```yaml
# GitOps: Git som source of truth för infrastruktur

# Principer:
# 1. Deklarativ - Beskriv önskat tillstånd
# 2. Versionshanterad - Allt i Git
# 3. Automatiserad - PR = Deploy
# 4. Observerad - Kontinuerlig sync

# Repo-struktur för GitOps:
infrastructure/
├── base/                            # Bas-konfiguration
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
├── overlays/
│   ├── development/
│   │   └── kustomization.yaml
│   ├── staging/
│   │   └── kustomization.yaml
│   └── production/
│       └── kustomization.yaml
└── apps/
    ├── frontend/
    └── backend/

# Workflow:
# 1. Utvecklare skapar PR med infrastrukturändringar
# 2. CI validerar (terraform plan, kubectl dry-run)
# 3. Review och godkännande
# 4. Merge till main
# 5. ArgoCD/Flux detekterar ändring och synkar
```

---

## Terraform med Git

```bash
# .gitignore för Terraform
cat > .gitignore << 'EOF'
# Local .terraform directories
**/.terraform/*

# Terraform state (känsligt!)
*.tfstate
*.tfstate.*

# Crash logs
crash.log
crash.*.log

# Sensitive variable files
*.tfvars
!example.tfvars

# Override files
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# CLI config
.terraformrc
terraform.rc
EOF

# Backend config för remote state
cat > backend.tf << 'EOF'
terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
EOF

# Git workflow för Terraform
# 1. Skapa feature branch
git checkout -b infra/add-rds

# 2. Gör ändringar
# terraform plan för att verifiera

# 3. Skapa PR
# CI kör: terraform fmt -check, terraform validate, terraform plan

# 4. Merge
# CD kör: terraform apply -auto-approve
```

---

## Ansible med Git

```yaml
# Struktur för Ansible repo
ansible/
├── inventories/
│   ├── development/
│   │   └── hosts.yml
│   ├── staging/
│   │   └── hosts.yml
│   └── production/
│       └── hosts.yml
├── playbooks/
│   ├── deploy.yml
│   └── rollback.yml
├── roles/
│   └── webserver/
├── group_vars/
│   └── all.yml
└── ansible.cfg

# ansible.cfg
[defaults]
inventory = inventories/development/hosts.yml
roles_path = roles
host_key_checking = False

# Git workflow
# 1. Ändra playbook/role
# 2. Test lokalt: ansible-playbook --check
# 3. PR med CI som kör ansible-lint
# 4. Merge triggar deploy
```

---

## Automation med Git Hooks

```bash
# Automatisera med server-side hooks

# post-receive hook (på Git-server)
#!/bin/bash
while read oldrev newrev ref; do
    if [[ $ref == "refs/heads/main" ]]; then
        echo "Deploying to production..."
        git --work-tree=/var/www/app checkout -f
        cd /var/www/app
        npm install
        pm2 restart app
    fi
done

# post-merge hook (lokalt, för docs)
#!/bin/bash
if git diff-tree -r --name-only --no-commit-id HEAD | grep -q "docs/"; then
    echo "Regenerating documentation..."
    npm run docs:build
fi
```

---

## Git i CI/CD-pipelines

```yaml
# .github/workflows/cd.yml

name: CD Pipeline

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0               # Full historik för versioning

      - name: Get version from tag
        if: startsWith(github.ref, 'refs/tags/')
        run: |
          VERSION=${GITHUB_REF#refs/tags/}
          echo "VERSION=$VERSION" >> $GITHUB_ENV

      - name: Get version from commit
        if: github.ref == 'refs/heads/main'
        run: |
          VERSION=$(git describe --tags --always)
          echo "VERSION=$VERSION" >> $GITHUB_ENV

      - name: Get changed files
        run: |
          # Filer ändrade sedan senaste tag
          CHANGED=$(git diff --name-only $(git describe --tags --abbrev=0)..HEAD)
          echo "Changed files: $CHANGED"

      - name: Deploy
        run: |
          echo "Deploying version $VERSION"
          # ... deploy logic
```

---

## Changelog-generering

```bash
# Automatisk changelog från commits

# Conventional Commits format krävs:
# feat(api): add user endpoint
# fix(auth): resolve token expiry
# docs(readme): update installation

# Med git-cliff
cargo install git-cliff

# cliff.toml
[changelog]
header = "# Changelog"
body = '''
{%% for group, commits in commits | group_by(attribute="group") %%}
## {{ group }}
{%% for commit in commits %%}
- {{ commit.message }} ([{{ commit.id | truncate(length=7) }}](link))
{%% endfor %%}
{%% endfor %%}
'''
trim = true

[git]
conventional_commits = true

# Generera changelog
git cliff -o CHANGELOG.md
git cliff --tag v1.0.0 -o CHANGELOG.md

# I CI:
git cliff --unreleased --tag $NEW_VERSION >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "docs: update changelog"
```

---

## Branch-strategier för Ops

```bash
# Environment branches för deployment

# Struktur:
# main         → Production
# staging      → Staging environment
# develop      → Development environment

# Promotion workflow:
# 1. PR till develop → Auto-deploy till dev
# 2. PR develop → staging → Auto-deploy till staging
# 3. PR staging → main → Auto-deploy till production (med approval)

# Med environment protection:
# GitHub: Settings → Environments → Production
# - Required reviewers
# - Wait timer
# - Deployment branches: main only
```

---

## Secrets Management

```bash
# ALDRIG commita secrets!

# Använd environment variables
export DATABASE_URL="postgres://..."

# Eller secrets manager
# AWS Secrets Manager, HashiCorp Vault, etc.

# Git-crypt för krypterade filer
git crypt init
git crypt add-gpg-user john@example.com

# .gitattributes
secrets/** filter=git-crypt diff=git-crypt
*.secret filter=git-crypt diff=git-crypt

# Filer krypteras automatiskt vid push
# Dekrypteras automatiskt för användare med nyckel

# SOPS (Secrets OPerationS)
sops secrets.yaml                    # Krypterar YAML-filer
# Stöder AWS KMS, GCP KMS, Azure Key Vault, PGP
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| GitOps                    | Git ar source of truth for infrastruktur            |
| Terraform state           | Remote state, ALDRIG i Git                          |
| Environment branches      | main/staging/develop for deployment-stages          |
| Secrets                   | git-crypt eller SOPS for krypterade filer           |
| Conventional Commits      | Mojliggor automatisk changelog-generering           |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- GitOps: Git = single source of truth
- Terraform state i S3/GCS med locking
- ALDRIG commita secrets - anvand environment variables
- Environment protection for production-deploys
- Conventional Commits for automatisk changelog
""",
        },
        {
            "title": "Git Troubleshooting & Common Issues",
            "slug": "git-troubleshooting-common-issues",
            "difficulty": "intermediate",
            "content": """
# Git Troubleshooting & Common Issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Problem                   | Tidsforlust utan losning                            |
|---------------------------|-----------------------------------------------------|
| Merge conflicts           | Timmar av frustration                               |
| Detached HEAD             | Forlorade commits                                   |
| Push rejected             | Blockerad deployment                                |
| Korrupt repo              | Potentiell dataforlust                              |

Alla stoter pa Git-problem. Snabb losning sparar timmar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanligaste Git-problemen

```
┌─────────────────────────────────────────────────────────────────┐
│                    GIT TROUBLESHOOTING                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PROBLEM              SYMPTOM                LOSNING            │
│  ───────              ───────                ───────            │
│                                                                 │
│  Merge conflict       <<<< ==== >>>>         Redigera, add,     │
│                       markorer i fil         commit             │
│                                                                 │
│  Detached HEAD        "detached HEAD"        git switch -c      │
│                       varning                new-branch         │
│                                                                 │
│  Push rejected        fetch first            git pull --rebase  │
│                       meddelande             sen push           │
│                                                                 │
│  Forlorade commits    Commits "forsvann"     git reflog         │
│                       efter reset            git reset --hard   │
│                                                                 │
│  Korrupt index        index file error       rm .git/index      │
│                                              git reset          │
│                                                                 │
│  SSH permission       Permission denied      ssh-add, config    │
│                       (publickey)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Merge Conflicts

```bash
# Problem: Merge conflict!
# CONFLICT (content): Merge conflict in file.js

# 1. Se vilka filer som är i konflikt
git status
# Both modified: file.js

# 2. Öppna filen, leta efter markörer:
# <<<<<<< HEAD
# din kod
# =======
# inkommande kod
# >>>>>>> feature-branch

# 3. Redigera - behåll rätt kod, ta bort markörer

# 4. Markera som löst
git add file.js

# 5. Fortsätt merge
git commit                           # Eller git merge --continue

# Vill du avbryta?
git merge --abort                    # Återställ till före merge

# Verktyg för konfliktlösning
git mergetool                        # Öppnar konfigurerat verktyg
# Konfigurera:
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

---

## Detached HEAD

```bash
# Problem: Du checkade ut en commit, inte en branch
# You are in 'detached HEAD' state...

# Du kan fortfarande arbeta, men commits "försvinner"

# Lösning 1: Skapa branch här
git switch -c new-branch             # Skapar branch vid HEAD

# Lösning 2: Gå tillbaka till en branch
git switch main                      # Byt till main

# Om du har commits du vill behålla:
git log --oneline                    # Notera commit-hashar
git switch main
git cherry-pick abc123               # Plocka commits

# Vad orsakade det?
git checkout abc123                  # Checkout av commit
git checkout v1.0.0                  # Checkout av tag
# Använd git switch istället!
```

---

## Push Rejected

```bash
# Problem: Push rejected - remote has work you don't have
# ! [rejected] main -> main (fetch first)

# Orsak: Någon annan har pushat

# Lösning 1: Pull och merge
git pull                             # fetch + merge
git push                             # Nu funkar det

# Lösning 2: Pull med rebase (renare historik)
git pull --rebase                    # Rebase dina commits
git push

# Problem: Push rejected - force push required
# ! [rejected] feature -> feature (non-fast-forward)

# Orsak: Du har rebasat/amend:at pushade commits

# Lösning (om du är SÄKER):
git push --force-with-lease          # Säkrare force push

# VARNING: Force push skriver över remote!
# Gör bara på din egna feature-branch
```

---

## Förlorade Commits

```bash
# Problem: "Förlorade" commits efter reset/rebase

# Lösning: Reflog!
git reflog                           # Visar alla HEAD-ändringar

# Output:
# abc123 HEAD@{0}: reset: moving to HEAD~3
# def456 HEAD@{1}: commit: Important work  <- HÄR!
# ...

# Återställ:
git reset --hard def456              # Gå tillbaka
# eller
git cherry-pick def456               # Plocka commit

# Tidsgräns: ~90 dagar (gc.reflogExpire)
```

---

## Ångra Vanliga Misstag

```bash
# "Jag commitade till fel branch!"
git log --oneline -1                 # Notera commit
git reset --hard HEAD~1              # Ta bort från fel branch
git switch correct-branch
git cherry-pick abc123               # Lägg till på rätt

# "Jag glömde lägga till en fil i commit!"
git add forgotten-file.js
git commit --amend --no-edit

# "Jag skrev fel commit-meddelande!"
git commit --amend -m "Correct message"

# "Jag vill ta bort senaste commit men behålla ändringarna!"
git reset --soft HEAD~1              # Ändringarna stannar staged

# "Jag vill kasta allt och börja om från remote!"
git fetch origin
git reset --hard origin/main

# "Jag pushade känslig data!"
# 1. Byt credentials OMEDELBART
# 2. Ta bort från historik:
git filter-branch --force --index-filter \\
  "git rm --cached --ignore-unmatch path/to/secret" \\
  --prune-empty --tag-name-filter cat -- --all
git push --force --all
# 3. Kontakta GitHub support för att rensa caches
```

---

## Repository Problem

```bash
# Problem: Korrupt index
# fatal: index file smaller than expected

git rm --cached -r .                 # Rensa index
git reset                            # Återskapa från HEAD

# Problem: Korrupt objekt
# error: object file is empty

# Ta bort korrupt objekt och hämta från remote:
rm .git/objects/ab/c123...
git fetch --all

# Problem: Locked index
# fatal: Unable to create '.git/index.lock': File exists

rm .git/index.lock                   # Ta bort lock-fil

# Problem: Repo är långsamt
git gc                               # Garbage collection
git repack -a -d -f                  # Ompackning

# Verifiering
git fsck                             # Kontrollera integritet
```

---

## SSH/Authentication Problem

```bash
# Problem: Permission denied (publickey)

# 1. Kontrollera att SSH-agent kör
eval "$(ssh-agent -s)"

# 2. Lägg till nyckel
ssh-add ~/.ssh/id_ed25519

# 3. Verifiera
ssh -T git@github.com                # Ska säga "Hi username!"

# Problem: Wrong key used
# 4. Kontrollera vilken nyckel som används
ssh -vT git@github.com               # Verbose output

# 5. Konfigurera specifik nyckel för GitHub
# ~/.ssh/config
Host github.com
  IdentityFile ~/.ssh/github_key
  IdentitiesOnly yes

# Problem: HTTPS credentials fungerar inte
git config --global credential.helper cache  # Temporär cache
git config --global credential.helper store  # Permanent (osäkert)
```

---

## Submodule Problem

```bash
# Problem: Submodule inte initierad
# fatal: no submodule mapping found

git submodule init
git submodule update

# Eller vid clone:
git clone --recurse-submodules URL

# Problem: Submodule pekar på fel commit
cd submodule-path
git checkout main
git pull
cd ..
git add submodule-path
git commit -m "Update submodule"

# Problem: Ta bort submodule helt
git submodule deinit path/to/sub
git rm path/to/sub
rm -rf .git/modules/path/to/sub
git commit -m "Remove submodule"
```

---

## Performance Problem

```bash
# Problem: Git är långsamt

# 1. Kör garbage collection
git gc --aggressive

# 2. Kontrollera repo-storlek
du -sh .git                          # Storlek på .git
git count-objects -v                 # Objektstatistik

# 3. Hitta stora filer
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  awk '/^blob/ {print $3, $4}' |
  sort -rn | head -10

# 4. För stora repos
git config core.preloadIndex true
git config core.fscache true
git config gc.auto 256

# 5. Överväg partial/shallow clone för CI
git clone --depth 1 URL
git clone --filter=blob:none URL
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| git reflog                | Din livräddare for forlorade commits                |
| --force-with-lease        | Sakrare an --force for push                         |
| git fsck                  | Hitta och diagnostisera repo-problem                |
| SSH-problem               | Kontrollera ssh-agent och ~/.ssh/config             |
| Performance               | git gc och stora filer kan vara boven               |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kom ihag

- git reflog visar ALLA HEAD-andringar (90 dagar)
- ALDRIG --force pa delade branches - anvand --force-with-lease
- Merge conflict? git merge --abort for att backa
- Detached HEAD? git switch -c new-branch
- Korrupt repo? rm .git/index && git reset
""",
        },
    ],
}
