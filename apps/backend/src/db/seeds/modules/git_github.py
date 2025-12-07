"""
Git & GitHub Mastery - Linux-mallen
=====================================

20 tasks som följer Linux-mallen:
- Varför behöver du kunna detta?
- Så fungerar det
- Bash-kommentarer på VARJE rad
- Key Takeaways
- Inga emojis i headers
- Inga tabeller
"""

MODULE = {
    "name": "Git & GitHub Mastery",
    "slug": "git-github-mastery",
    "description": "Behärska versionskontroll med Git och samarbete via GitHub",
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

## Varför behöver du kunna detta?

Git är fundamentet för all modern mjukvaruutveckling. Utan förståelse för hur Git fungerar internt kommer du att:

- Förlora kod vid merge-konflikter
- Inte kunna återställa misstag
- Skapa kaotiska commit-historiker
- Bromsa hela teamets arbetsflöde

Varje DevOps-ingenjör arbetar med Git dagligen. Förståelse för arkitekturen gör skillnaden mellan att gissa och att veta exakt vad som händer.

---

## Så fungerar det

Git är ett distribuerat versionskontrollsystem. Till skillnad från centraliserade system (SVN, CVS) har varje utvecklare en komplett kopia av hela repositoryt, inklusive all historik.

**Gits tre områden:**

1. **Working Directory** - Dina faktiska filer på disk
2. **Staging Area (Index)** - Förberedelser för nästa commit
3. **Repository (.git)** - Databasen med alla commits

**Gits objekt:**

- **Blob** - Filinnehåll (ingen metadata)
- **Tree** - Katalogstruktur, pekar på blobs och andra trees
- **Commit** - Snapshot med metadata, pekar på ett tree
- **Tag** - Namngiven pekare till en commit

Allt i Git identifieras med SHA-1 hashar (40 tecken). Samma innehåll = samma hash, vilket ger integritet och deduplicering.

---

## Grundläggande Git-kommandon

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
git log                              # Fullständig logg
git log --oneline                    # Kompakt vy, en rad per commit
git log --graph                      # Visar branch-graf
git log --oneline --graph --all      # Kompakt graf för alla branches

# Visa specifik commit
git show abc123                      # Visar commit-detaljer och diff
git show HEAD                        # Visar senaste commit
git show HEAD~1                      # Visar näst senaste commit (1 steg bakåt)
git show HEAD~3                      # 3 commits bakåt

# Visa ändringar för en fil
git log -p hello.txt                 # Logg med patches för filen
git log --follow hello.txt           # Följer filhistorik även vid rename
```

---

## Key Takeaways

1. Git är distribuerat - varje klon är ett komplett repository
2. Tre områden: Working Directory → Staging Area → Repository
3. Allt identifieras med SHA-1 hashar för integritet
4. `git add` flyttar ändringar till staging, `git commit` sparar dem
5. `.git/` innehåller hela repositoryts data och historik
""",
        },
        {
            "title": "Branching & Merging",
            "slug": "branching-merging",
            "difficulty": "beginner",
            "content": """
# Branching & Merging

## Varför behöver du kunna detta?

Branching är det som gör Git överlägset. Det låter dig:

- Arbeta på features isolerat utan att störa main
- Experimentera utan risk
- Ha flera versioner parallellt (development, staging, production)
- Samarbeta effektivt i team

Utan branching-strategi blir kodbasen kaotisk. Merge-konflikter blir mardrömmar. Releases blir riskfyllda.

---

## Så fungerar det

En branch i Git är bara en pekare till en commit. Det kostar nästan ingenting att skapa en branch - det är bara en 41-byte fil med en commit-hash.

**HEAD** är en speciell pekare som visar vilken branch du är på.

**Merge** kombinerar två branches. Git väljer automatiskt rätt strategi:

- **Fast-forward** - Om målet inte har divergerat, flyttas bara pekaren
- **Three-way merge** - Om båda branches har commits, skapas en merge-commit

---

## Skapa och hantera branches

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

---

## Key Takeaways

1. Branches är billiga - bara pekare till commits
2. `git switch` är det moderna sättet att byta branch
3. Fast-forward sker när målet inte har divergerat
4. Konflikter löses manuellt, sedan `git add` och `git commit`
5. Ta bort mergade branches för att hålla ordning
""",
        },
        {
            "title": "Remote Repositories & GitHub",
            "slug": "remote-repositories-github",
            "difficulty": "beginner",
            "content": """
# Remote Repositories & GitHub

## Varför behöver du kunna detta?

Lokalt Git är bra, men värdet kommer från samarbete. Remote repositories låter dig:

- Dela kod med teamet
- Ha backup av all kod
- Deploya automatiskt via CI/CD
- Spåra issues och pull requests

GitHub är den dominerande plattformen. Att förstå remote-hantering är kritiskt för DevOps-arbete.

---

## Så fungerar det

Ett remote repository är en kopia av ditt repo på en server (GitHub, GitLab, etc.).

**Remote tracking branches** är lokala kopior av remote branches. De heter `origin/main`, `origin/feature-x`, etc.

**Fetch** hämtar ändringar från remote men applicerar dem inte.
**Pull** = fetch + merge.
**Push** skickar dina commits till remote.

---

## Konfigurera remotes

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
git push origin main                 # Uppdaterar din fork på GitHub
```

---

## Key Takeaways

1. Remote är en kopia på en server - `origin` är standardnamnet
2. SSH-nycklar är säkrare och smidigare än HTTPS + lösenord
3. `fetch` hämtar data, `pull` hämtar och mergar
4. `-u` sätter tracking så du slipper ange remote varje gång
5. `--prune` städar bort refs till borttagna remote branches
""",
        },
        {
            "title": "Git Workflow Strategies",
            "slug": "git-workflow-strategies",
            "difficulty": "intermediate",
            "content": """
# Git Workflow Strategies

## Varför behöver du kunna detta?

Utan en definierad workflow blir Git-historiken kaotisk. Team behöver:

- Tydliga regler för när och hur man mergar
- Skydd för produktionskod
- Effektiv code review-process
- Förutsägbara releaser

Rätt workflow minskar konflikter, förbättrar kodkvalitet och snabbar upp leverans.

---

## Så fungerar det

Det finns flera etablerade workflows. Varje organisation väljer baserat på teamstorlek, release-frekvens och komplexitet.

**Git Flow** - Komplex, för schemalagda releaser
**GitHub Flow** - Enkel, för kontinuerlig deployment
**GitLab Flow** - Mellanväg med environment-branches
**Trunk-Based** - Minimal branching, för mogna team

---

## GitHub Flow (Rekommenderat för de flesta)

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

---

## Key Takeaways

1. GitHub Flow är enklast - en branch, PR, merge till main
2. Git Flow passar större projekt med schemalagda releaser
3. Trunk-Based kräver mogen CI/CD men ger snabbast leverans
4. Conventional Commits gör historiken läsbar och automatiserbar
5. Konsekvent namngivning hjälper hela teamet
""",
        },
        {
            "title": "Rebasing & Interactive Rebase",
            "slug": "rebasing-interactive-rebase",
            "difficulty": "intermediate",
            "content": """
# Rebasing & Interactive Rebase

## Varför behöver du kunna detta?

Merge skapar "merge commits" som gör historiken svårläst. Rebase ger en linjär, ren historik.

Dessutom låter interactive rebase dig:

- Slå ihop flera commits till en
- Redigera commit-meddelanden
- Ta bort oönskade commits
- Ordna om commits

Professionella utvecklare förväntas kunna hålla en ren Git-historik.

---

## Så fungerar det

**Rebase** flyttar commits till en ny bas. Istället för att skapa en merge-commit "spelas" dina commits upp på toppen av target-branchen.

**Interactive rebase** (`-i`) låter dig välja vad som ska hända med varje commit:
- **pick** - Behåll commit som den är
- **reword** - Ändra commit-meddelande
- **squash** - Slå ihop med föregående commit
- **fixup** - Som squash men behåll inte meddelandet
- **drop** - Ta bort commit

---

## Grundläggande rebase

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
git reset --hard HEAD@{2}            # Återställ till tidigare tillstånd
```

---

## Key Takeaways

1. Rebase ger linjär historik - renare än merge
2. Interactive rebase (`-i`) ger full kontroll över commits
3. Squash WIP-commits före PR för professionell historik
4. `--fixup` och `--autosquash` automatiserar cleanup
5. **ALDRIG rebasa publika commits** - använd `--force-with-lease` om nödvändigt
""",
        },
        {
            "title": "Undoing Changes & Recovery",
            "slug": "undoing-changes-recovery",
            "difficulty": "intermediate",
            "content": """
# Undoing Changes & Recovery

## Varför behöver du kunna detta?

Misstag händer. Du kommer att:

- Commita fel saker
- Pusha till fel branch
- Ta bort kod av misstag
- Förstöra historiken med dålig rebase

Förmågan att återställa är skillnaden mellan panik och lugn problemlösning.

---

## Så fungerar det

Git har flera sätt att ångra, beroende på var ändringen är:

1. **Working directory** - Ändringar inte stagade
2. **Staging area** - Stagade men inte committade
3. **Committed** - Lokala commits
4. **Pushed** - Commits på remote

Varje steg kräver olika kommandon.

---

## Ångra ändringar i working directory

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
git cherry-pick abc1234              # Applicera commit här
```

---

## Key Takeaways

1. `restore` för working directory, `restore --staged` för staging area
2. `reset --soft` behåller ändringar, `--hard` kastar allt
3. `revert` för publika commits - skapar ny commit som ångrar
4. `reflog` är din backup - loggar allt även "borttaget"
5. Känslig data kräver omedelbar action OCH ny credential
""",
        },
        {
            "title": "Pull Requests & Code Review",
            "slug": "pull-requests-code-review",
            "difficulty": "intermediate",
            "content": """
# Pull Requests & Code Review

## Varför behöver du kunna detta?

Pull Requests (PRs) är hjärtat i modern mjukvaruutveckling. De ger:

- Code review före merge
- Dokumentation av ändringar
- CI/CD-integration
- Diskussion och feedback

Bra PR-praxis höjer kodkvaliteten och sprider kunskap i teamet.

---

## Så fungerar det

En Pull Request är en förfrågan om att merga en branch in i en annan. GitHub visar:

- Alla commits i branchen
- Diff av alla ändringar
- CI/CD-status (tester, linting)
- Review-kommentarer och godkännanden

PRs kan konfigureras med regler: kräv reviews, passerade tester, etc.

---

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

---

## Key Takeaways

1. Rebasa och städa commits innan PR för enklare review
2. Bra PR-beskrivning sparar reviewers tid
3. Kategorisera feedback: nitpick, suggestion, blocking
4. Branch protection rules förhindrar misstag
5. CODEOWNERS automatiserar reviewer-tilldelning
""",
        },
        {
            "title": "GitHub Actions Basics",
            "slug": "github-actions-basics",
            "difficulty": "intermediate",
            "content": """
# GitHub Actions Basics

## Varför behöver du kunna detta?

GitHub Actions är GitHubs inbyggda CI/CD-plattform. Fördelarna:

- Ingen extern tjänst behövs
- Gratis för public repos
- Djup GitHub-integration
- Tusentals community actions

Automatiserad testning och deployment är standard i professionell utveckling.

---

## Så fungerar det

GitHub Actions kör **workflows** definierade i YAML-filer under `.github/workflows/`.

**Komponenter:**
- **Workflow** - En automatiserad process
- **Event** - Trigger som startar workflow (push, PR, schedule)
- **Job** - Grupp av steg som körs på samma runner
- **Step** - Enskild uppgift (kör script eller action)
- **Action** - Återanvändbar enhet (community eller egen)
- **Runner** - Maskin som kör jobbet (GitHub-hosted eller self-hosted)

---

## Första workflow

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

## Varför behöver du kunna detta?

Du arbetar på en feature när något akut dyker upp. Du behöver byta branch men har uncommittade ändringar. Vad gör du?

**Stash** låter dig temporärt spara ändringar utan att commita.
**Worktrees** låter dig ha flera branches utcheckade samtidigt.

Båda är kritiska för effektivt arbete.

---

## Så fungerar det

**Stash** fungerar som en stack. Du pushar ändringar till stacken, byter branch, och poppar tillbaka dem senare.

**Worktrees** skapar separata working directories som delar samma `.git`-mapp. Du kan ha `main` i en katalog och `feature-x` i en annan - samtidigt.

---

## Git Stash grunderna

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

---

## Key Takeaways

1. `git stash` sparar ändringar temporärt utan commit
2. `stash -u` inkluderar untracked files
3. Worktrees låter dig ha flera branches utcheckade samtidigt
4. Worktrees delar `.git` - ändringar synkas automatiskt
5. Använd beskrivande stash-meddelanden (`-m`) för att hålla ordning
""",
        },
        {
            "title": "Git Tags & Releases",
            "slug": "git-tags-releases",
            "difficulty": "intermediate",
            "content": """
# Git Tags & Releases

## Varför behöver du kunna detta?

Tags markerar viktiga punkter i historiken - vanligtvis releaser. De ger:

- Tydlig versionshantering (v1.0.0, v2.0.0)
- Snabb navigering till specifika releases
- Underlag för GitHub Releases
- Deployment-triggers i CI/CD

Utan taggar är det svårt att spåra vad som är deployat var.

---

## Så fungerar det

Git har två typer av taggar:

**Lightweight tags** - Bara en pekare till en commit
**Annotated tags** - Fullt Git-objekt med metadata (rekommenderas)

Annotated tags innehåller:
- Taggare (namn + email)
- Datum
- Meddelande
- Valfri GPG-signatur

---

## Skapa taggar

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

---

## Key Takeaways

1. Använd annotated tags (`-a`) för releases
2. Semantic versioning: MAJOR.MINOR.PATCH
3. `--follow-tags` pushar bara annoterade taggar
4. GitHub Releases bygger på Git tags + extra metadata
5. Taggar är perfekta triggers för CI/CD releases
""",
        },
        {
            "title": "Git Hooks",
            "slug": "git-hooks",
            "difficulty": "intermediate",
            "content": """
# Git Hooks

## Varför behöver du kunna detta?

Git hooks automatiserar kvalitetskontroller. De kan:

- Köra linting före commit
- Validera commit-meddelanden
- Köra tester före push
- Formatera kod automatiskt

Hooks förhindrar att dålig kod ens hamnar i repositoryt.

---

## Så fungerar det

Hooks är scripts som Git kör vid specifika events. De ligger i `.git/hooks/`.

**Client-side hooks:**
- `pre-commit` - Före commit skapas
- `prepare-commit-msg` - Redigera default commit-meddelande
- `commit-msg` - Validera commit-meddelande
- `pre-push` - Före push till remote

**Server-side hooks:**
- `pre-receive` - Före commits accepteras
- `post-receive` - Efter commits accepterats

---

## Grundläggande hooks

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

---

## Key Takeaways

1. Hooks är scripts som körs vid Git-events
2. `pre-commit` för linting, `commit-msg` för meddelandevalidering
3. `.git/hooks/` versionshanteras INTE - använd Husky
4. lint-staged kör checks bara på staged files
5. Hooks förhindrar dålig kod från att committas
""",
        },
        {
            "title": "Git Configuration & Aliases",
            "slug": "git-configuration-aliases",
            "difficulty": "beginner",
            "content": """
# Git Configuration & Aliases

## Varför behöver du kunna detta?

Git är konfigurerbart. Rätt inställningar sparar tid och förhindrar misstag.

Aliases låter dig skapa genvägar för vanliga kommandon. Istället för att skriva `git log --oneline --graph --all` kan du skriva `git lg`.

Professionella utvecklare har sina egna optimerade Git-konfigurationer.

---

## Så fungerar det

Git-konfiguration lagras på tre nivåer:

1. **System** (`/etc/gitconfig`) - Alla användare
2. **Global** (`~/.gitconfig`) - Din användare
3. **Local** (`.git/config`) - Specifikt repo

Local överskrider Global som överskrider System.

---

## Grundläggande konfiguration

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

---

## Key Takeaways

1. Tre nivåer: system → global → local (local vinner)
2. `--global` för personliga inställningar, local för projekt
3. Aliases sparar tid: `git lg` istället för lång log-kommando
4. `pull.rebase = true` ger renare historik
5. Global gitignore för OS- och editor-filer
""",
        },
        {
            "title": "Submodules & Monorepos",
            "slug": "submodules-monorepos",
            "difficulty": "advanced",
            "content": """
# Submodules & Monorepos

## Varför behöver du kunna detta?

Större projekt behöver hantera kod på olika sätt:

**Submodules** - Inkludera externa repos i ditt projekt
**Monorepos** - Flera projekt i samma repository

Båda har för- och nackdelar. Rätt val beror på teamstorlek, beroenden och release-cykler.

---

## Så fungerar det

**Submodules** skapar en referens till en specifik commit i ett annat repo. De är som dependencies men med full Git-historik.

**Monorepos** samlar all kod i ett repo. Kräver verktyg som Nx, Turborepo eller Lerna för att skala.

---

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

# Kombinera med sparse checkout för stora repos
```

---

## Key Takeaways

1. Submodules inkluderar externa repos vid specifik commit
2. `--recurse-submodules` vid clone för att få all kod
3. Monorepos samlar allt i ett repo - kräver verktyg som Turborepo
4. Sparse checkout för att bara klona delar av stora repos
5. Worktrees ger parallellt arbete i monorepos
""",
        },
        {
            "title": "Git Bisect & Debugging",
            "slug": "git-bisect-debugging",
            "difficulty": "advanced",
            "content": """
# Git Bisect & Debugging

## Varför behöver du kunna detta?

En bugg har introducerats någonstans i historiken. Du vet att det fungerade förra veckan. Hur hittar du exakt vilken commit som introducerade buggen?

`git bisect` gör binärsökning genom commit-historiken. Istället för att testa 100 commits testar du ~7.

---

## Så fungerar det

Git bisect delar upp historiken i hälfter. Du testar mitten och säger "bra" eller "dålig". Git väljer nästa halva automatiskt.

**Binärsökning:** 1000 commits → ~10 tester
**Linjär sökning:** 1000 commits → ~500 tester i snitt

---

## Grundläggande bisect

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
# Skapa fix baserad på vad du hittat
```

---

## Key Takeaways

1. `git bisect` gör binärsökning - ~7 tester för 100 commits
2. `git bisect run` automatiserar med test-script
3. `git blame` visar vem som ändrade varje rad
4. `-S` i log hittar commits som ändrade en sträng
5. Kombinera bisect + blame + log för effektiv debugging
""",
        },
        {
            "title": "Git LFS & Large Files",
            "slug": "git-lfs-large-files",
            "difficulty": "advanced",
            "content": """
# Git LFS & Large Files

## Varför behöver du kunna detta?

Git är optimerat för textfiler. Stora binärfiler (bilder, videos, modeller) gör repos:

- Långsamma att klona
- Stora på disk
- Svåra att hantera

Git LFS (Large File Storage) löser detta genom att lagra stora filer separat.

---

## Så fungerar det

Git LFS ersätter stora filer med pekare. Själva filerna lagras på en separat server.

**Vanlig Git:**
- Varje commit lagrar hela filen
- Historiken växer snabbt

**Git LFS:**
- Commits innehåller bara pekare (~130 bytes)
- Filer laddas ned vid checkout
- Bara den version du behöver

---

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

---

## Key Takeaways

1. Git LFS lagrar stora filer separat - snabbare kloning
2. `git lfs track` före du lägger till stora filer
3. `.gitattributes` måste committas och pushas
4. `migrate import` skriver om historiken - kräver force push
5. Sätt upp LFS tidigt i projektet för bäst resultat
""",
        },
        {
            "title": "GitHub Features & Settings",
            "slug": "github-features-settings",
            "difficulty": "beginner",
            "content": """
# GitHub Features & Settings

## Varför behöver du kunna detta?

GitHub är mer än Git-hosting. Det är en komplett utvecklingsplattform med:

- Issues och projekt för planering
- Discussions för community
- Wiki för dokumentation
- Security features för säkerhet

Att utnyttja dessa features förbättrar team-samarbetet dramatiskt.

---

## Så fungerar det

GitHub bygger på Git men lägger till ett lager av samarbetsverktyg. Dessa är GitHub-specifika och finns inte i "ren" Git.

---

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

---

## Key Takeaways

1. GitHub är mer än Git - Issues, Projects, Discussions
2. Issue templates standardiserar buggrapporter
3. Projects ger Kanban-boards för planering
4. Dependabot håller dependencies uppdaterade
5. Template repos sparar tid vid nya projekt
""",
        },
        {
            "title": "GitHub Security & Access Control",
            "slug": "github-security-access-control",
            "difficulty": "intermediate",
            "content": """
# GitHub Security & Access Control

## Varför behöver du kunna detta?

Säkerhet i repositories är kritiskt. En läckt API-nyckel eller för breda behörigheter kan leda till:

- Datastöld
- Infrastruktur-kompromiss
- Ekonomiska förluster
- Rykteskador

GitHub har kraftfulla verktyg för att skydda kod och credentials.

---

## Så fungerar det

GitHub erbjuder flera säkerhetslager:

1. **Autentisering** - SSH-nycklar, tokens, 2FA
2. **Auktorisering** - Repo-åtkomst, branch protection
3. **Scanning** - Secrets, vulnerabilities, code
4. **Audit** - Loggar vem som gjorde vad

---

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

---

## Key Takeaways

1. Fine-grained PATs är säkrare än classic tokens
2. Deploy keys för CI/CD, begränsade till ett repo
3. Branch protection förhindrar direkta pushes till main
4. Secret scanning blockerar läckta credentials
5. Dependabot håller dependencies säkra automatiskt
""",
        },
        {
            "title": "Advanced Git Internals",
            "slug": "advanced-git-internals",
            "difficulty": "advanced",
            "content": """
# Advanced Git Internals

## Varför behöver du kunna detta?

Förståelse för Gits internals gör dig till en Git-mästare. Du kan:

- Återställa "förlorad" data
- Förstå varför kommandon beter sig som de gör
- Optimera stora repositories
- Felsöka komplexa problem

---

## Så fungerar det

Git är fundamentalt en content-addressable filesystem. Allt lagras som objekt identifierade av SHA-1 hashar.

**Fyra objekttyper:**
- blob - Filinnehåll
- tree - Katalogstruktur
- commit - Snapshot med metadata
- tag - Namngiven pekare (annotated)

---

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

---

## Key Takeaways

1. Git är en content-addressable database med fyra objekttyper
2. Refs är pekare till commits - branches och tags
3. Index (staging area) är mellansteget före commit
4. Packfiles komprimerar objekt för effektivitet
5. `git fsck` för att verifiera och hitta problem
""",
        },
        {
            "title": "Git for DevOps & Automation",
            "slug": "git-for-devops-automation",
            "difficulty": "advanced",
            "content": """
# Git for DevOps & Automation

## Varför behöver du kunna detta?

DevOps handlar om automation. Git-kunskap är kritisk för:

- GitOps-workflows (Kubernetes, ArgoCD)
- Infrastructure as Code (Terraform, Ansible)
- CI/CD-pipelines
- Automatisk dokumentation

Git är fundamentet för modern DevOps.

---

## Så fungerar det

DevOps använder Git som:
- Single source of truth för infrastruktur
- Trigger för automation
- Audit trail för ändringar
- Kollaborationsverktyg för ops och dev

---

## GitOps-mönster

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

---

## Key Takeaways

1. GitOps: Git är source of truth för infrastruktur
2. Remote state för Terraform, aldrig i Git
3. Environment branches för deployment-stages
4. git-crypt eller SOPS för krypterade secrets
5. Conventional Commits möjliggör automatisk changelog
""",
        },
        {
            "title": "Git Troubleshooting & Common Issues",
            "slug": "git-troubleshooting-common-issues",
            "difficulty": "intermediate",
            "content": """
# Git Troubleshooting & Common Issues

## Varför behöver du kunna detta?

Alla stöter på Git-problem. De vanligaste:

- Merge-konflikter
- Detached HEAD
- Push rejected
- Förlorade commits
- Korrupt repository

Att snabbt lösa dessa sparar timmar av frustration.

---

## Så fungerar det

De flesta Git-problem har enkla lösningar - när du vet vad du letar efter. Denna guide täcker de vanligaste scenarierna.

---

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

---

## Key Takeaways

1. `git reflog` är din livräddare för "förlorade" commits
2. `--force-with-lease` är säkrare än `--force`
3. `git fsck` för att hitta repository-problem
4. SSH-problem? Kontrollera ssh-agent och config
5. Performance: `git gc` och stora filer kan vara boven
""",
        },
    ],
}
