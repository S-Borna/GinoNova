"""
Git Advanced - Tasks 9-16
Premium Bootcamp-Quality Content
"""

TASKS_ADVANCED = [
    {
        "title": "Git Rebase",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 150,
        "content": r"""
# 🔄 Git Rebase

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
- Förstå skillnaden mellan merge och rebase
- Utföra basic rebase
- Använda interaktiv rebase
- Veta när man INTE ska rebasa

---

## 📖 Rebase vs Merge

### Visualisering

```
FÖRE:
main:    A -> B -> C
              ↘
feature:       D -> E

EFTER MERGE:
main:    A -> B -> C -----> M (merge commit)
              ↘       ↗
feature:       D -> E

EFTER REBASE:
main:    A -> B -> C -> D' -> E' (linjär historik)
```

### Fördelar med Rebase

| Merge | Rebase |
|-------|--------|
| Bevarar all historik | Renare, linjär historik |
| Merge commits | Inga extra commits |
| Visar när merge skedde | Ser ut som sekventiellt |
| Säkrare för delade branches | Bra för lokala branches |

---

## 🛠️ Basic Rebase

### Standard rebase workflow

```bash
# 1. Du jobbar på feature branch
git switch feature/login

# 2. Main har uppdaterats
git fetch origin

# 3. Rebasa din branch på main
git rebase main

# Vad händer:
# - Dina commits "flyttas" till efter main
# - Commit-hashes ändras (D -> D', E -> E')

# 4. Vid konflikter
git add .
git rebase --continue

# 5. Avbryt vid problem
git rebase --abort
```

### Rebase remote tracking

```bash
# Istället för pull + merge
git pull --rebase origin main

# Konfigurera som default
git config --global pull.rebase true
```

---

## ✏️ Interaktiv Rebase

### Kraftfullt verktyg för att redigera historik

```bash
# Rebasa senaste 3 commits
git rebase -i HEAD~3

# Editor öppnas:
pick abc123 First commit
pick def456 Second commit
pick ghi789 Third commit

# Kommandon:
# p, pick   = behåll commit
# r, reword = ändra meddelande
# e, edit   = pausa för ändringar
# s, squash = slå ihop med föregående
# f, fixup  = squash utan meddelande
# d, drop   = ta bort commit
```

### Vanliga användningsfall

```bash
# Squash: Slå ihop commits
pick abc123 Add feature
squash def456 Fix typo
squash ghi789 More fixes
# Resultat: En commit med kombinerat meddelande

# Reword: Ändra commit-meddelande
reword abc123 Better commit message

# Reorder: Ändra ordning
pick ghi789 Third (nu först)
pick abc123 First (nu andra)
```

---

## ⚠️ Rebase Golden Rule

```
+-----------------------------------------------------------------+
|                    REBASE GOLDEN RULE                           |
+-----------------------------------------------------------------+
|                                                                 |
|   ALDRIG rebasa commits som är pushade och delade!             |
|                                                                 |
|   ✅ OK: Rebasa lokala commits                                 |
|   ✅ OK: Rebasa din egna feature branch (före PR merge)        |
|   ❌ NEJ: Rebasa main/develop                                  |
|   ❌ NEJ: Rebasa efter någon annan börjat jobba på branchen    |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🏋️ Övningar

### Övning 1: Basic rebase
```bash
mkdir rebase-test && cd rebase-test && git init
echo "a" > file && git add . && git commit -m "A"
echo "b" >> file && git commit -am "B"

git switch -c feature
echo "d" >> file && git commit -am "D"

git switch main
echo "c" >> file && git commit -am "C"

git switch feature
git rebase main
git log --oneline --graph --all
```

### Övning 2: Interaktiv rebase
```bash
# Squash tre commits till en
git rebase -i HEAD~3
# Ändra till: pick, squash, squash
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git rebase main | Rebasa på main |
| git rebase -i HEAD~n | Interaktiv rebase |
| git rebase --continue | Fortsätt efter konflikt |
| git rebase --abort | Avbryt rebase |

**Nästa steg:** Git Cherry-Pick & Bisect

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Git Cherry-Pick & Bisect",
        "difficulty": "medium",
        "estimated_minutes": 45,
        "xp_reward": 135,
        "content": r"""
# 🍒 Git Cherry-Pick & Bisect

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
- Plocka specifika commits med cherry-pick
- Hitta bugg-introducerande commit med bisect
- Förstå när dessa verktyg är användbara

---

## 🍒 Git Cherry-Pick

### Vad är cherry-pick?

Kopiera en specifik commit till din nuvarande branch.

```
FÖRE:
main:    A -> B -> C
              ↘
feature:       D -> E -> F (du vill ha E)

EFTER cherry-pick E:
main:    A -> B -> C -> E'
              ↘
feature:       D -> E -> F
```

### Användning

```bash
# Cherry-pick en commit
git cherry-pick abc123

# Cherry-pick flera commits
git cherry-pick abc123 def456 ghi789

# Cherry-pick range
git cherry-pick abc123..def456

# Utan commit (bara apply changes)
git cherry-pick --no-commit abc123

# Vid konflikt
git cherry-pick --continue
git cherry-pick --abort
```

### Användningsfall

```bash
# Hotfix: Ta buggfix från develop till main
git switch main
git cherry-pick <bugfix-commit>

# Backport: Applicera feature på äldre version
git switch release/1.0
git cherry-pick <feature-commit>
```

---

## 🔍 Git Bisect

### Binärsökning för buggar

```bash
# Scenario: Något fungerade i v1.0, trasigt nu
# Bisect hittar exakt vilken commit som bröt det

# 1. Starta bisect
git bisect start

# 2. Markera nuvarande som dålig
git bisect bad

# 3. Markera känd bra commit
git bisect good v1.0

# 4. Git checkar ut mitt-commit
# Testa om buggen finns
git bisect good  # eller bad

# 5. Upprepa tills Git hittar skyldig commit
# Bisecting: 0 revisions left to test
# abc123 is the first bad commit

# 6. Avsluta
git bisect reset
```

### Automatiserad bisect

```bash
# Kör test-script automatiskt
git bisect start HEAD v1.0
git bisect run ./test-script.sh

# test-script.sh ska returnera:
# 0 = good
# 1-127 (utom 125) = bad
# 125 = skip
```

### Visualisering

```
                              ✓ good
v1.0: A -> B -> C -> D -> E -> F -> G -> H (bad)
              ↑
          Bisect startar här (mitt)

Om D är good -> sök E-H
Om D är bad -> sök A-C
```

---

## 🏋️ Övningar

### Övning 1: Cherry-pick
```bash
git switch -c feature
echo "feature1" > feature.txt && git add . && git commit -m "Feature 1"
echo "feature2" >> feature.txt && git commit -am "Feature 2"

git switch main
# Plocka bara Feature 2
git cherry-pick <commit-hash-for-feature2>
```

### Övning 2: Bisect
```bash
# Skapa historik med en "bugg"
for i in {1..10}; do
  echo "commit $i" >> file.txt
  git add . && git commit -m "Commit $i"
done

# Anta commit 5 introducerade bugg
git bisect start HEAD HEAD~10
# Testa och markera good/bad
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git cherry-pick | Kopiera commit |
| git bisect start | Starta bugg-sökning |
| git bisect good/bad | Markera commit |
| git bisect reset | Avsluta bisect |

**Nästa steg:** Git Stash

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Git Stash",
        "difficulty": "medium",
        "estimated_minutes": 40,
        "xp_reward": 125,
        "content": r"""
# 📦 Git Stash

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
- Spara temporärt arbete med stash
- Hantera flera stashes
- Återställa och applicera stashes

---

## 📖 Vad är Stash?

Temporär förvaring av uncommitted changes.

```
+-----------------------------------------------------------------+
|                        GIT STASH                                |
+-----------------------------------------------------------------+
|                                                                 |
|   Scenario: Du jobbar på feature, måste fixa urgent bug        |
|                                                                 |
|   Working Directory --stash--> Stash Stack                     |
|   (ändringar)                  [0] WIP on feature              |
|                                [1] Previous stash              |
|                                                                 |
|   ... fixa bug ...                                             |
|                                                                 |
|   Stash Stack --stash pop--> Working Directory                 |
|   (tom)                       (ändringar tillbaka)             |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🛠️ Stash Operationer

### Spara

```bash
# Basic stash
git stash

# Med meddelande
git stash push -m "WIP: login feature"

# Inkludera untracked files
git stash -u
git stash --include-untracked

# Inkludera ignorerade files
git stash -a
git stash --all

# Stash specifika filer
git stash push -m "Only these" file1.txt file2.txt

# Interaktiv stash (välj vad)
git stash -p
```

### Lista och visa

```bash
# Lista stashes
git stash list
# stash@{0}: WIP on feature: abc123 Add login
# stash@{1}: On main: def456 Fix bug

# Visa innehåll
git stash show
git stash show -p  # Full diff
git stash show stash@{1}
```

### Återställa

```bash
# Pop: Applicera och ta bort
git stash pop

# Apply: Applicera och behåll
git stash apply

# Specifik stash
git stash pop stash@{2}
git stash apply stash@{1}
```

### Ta bort

```bash
# Ta bort en stash
git stash drop stash@{0}

# Rensa alla stashes
git stash clear
```

---

## 🔀 Avancerade Stash

### Skapa branch från stash

```bash
# Skapa ny branch med stashed changes
git stash branch new-feature-branch stash@{0}
# Skapar branch, checkar ut, applicerar stash
```

### Stash till specifik commit

```bash
# Se stash som commit
git stash show stash@{0} -p

# Cherry-pick stash (om du behöver)
git stash show -p stash@{0} | git apply
```

---

## 🏋️ Övningar

### Övning 1: Basic stash workflow
```bash
# Jobba på något
echo "work in progress" > wip.txt
git add wip.txt

# Måste byta branch
git stash push -m "WIP: feature"
git switch main
# ... gör urgent fix ...
git switch feature
git stash pop
```

### Övning 2: Hantera flera stashes
```bash
git stash push -m "First"
git stash push -m "Second"
git stash list
git stash apply stash@{1}  # Första
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| git stash | Spara changes |
| git stash push -m | Med meddelande |
| git stash list | Lista alla |
| git stash pop | Applicera + ta bort |
| git stash apply | Applicera + behåll |
| git stash drop | Ta bort stash |

**Nästa steg:** Git Hooks

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Git Hooks",
        "difficulty": "medium",
        "estimated_minutes": 50,
        "xp_reward": 140,
        "content": r"""
# 🪝 Git Hooks

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
- Förstå vad Git hooks är
- Implementera pre-commit och commit-msg hooks
- Använda Husky för team-hooks
- Automatisera kvalitetskontroller

---

## 📖 Vad är Hooks?

Scripts som körs automatiskt vid Git-events.

```
+-----------------------------------------------------------------+
|                      GIT HOOKS                                  |
+-----------------------------------------------------------------+
|                                                                 |
|   git commit --------------------------------------------->    |
|        |                                                        |
|        +-- pre-commit    (lint, test, format)                  |
|        +-- prepare-commit-msg                                  |
|        +-- commit-msg    (validera meddelande)                 |
|        +-- post-commit   (notifieringar)                       |
|                                                                 |
|   git push ----------------------------------------------->    |
|        |                                                        |
|        +-- pre-push      (tester före push)                    |
|                                                                 |
+-----------------------------------------------------------------+
```

### Vanliga Hooks

| Hook | När | Användning |
|------|-----|-----------|
| pre-commit | Före commit | Lint, format, test |
| commit-msg | Efter meddelande | Validera format |
| pre-push | Före push | Köra tester |
| post-merge | Efter merge | Installera deps |
| pre-rebase | Före rebase | Varningar |

---

## 🛠️ Manuella Hooks

### Skapa hook

```bash
# Hooks finns i .git/hooks/
ls .git/hooks/
# pre-commit.sample
# commit-msg.sample

# Aktivera genom att ta bort .sample
cp .git/hooks/pre-commit.sample .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Pre-commit exempel

```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "Running pre-commit hooks..."

# Lint
npm run lint
if [ $? -ne 0 ]; then
    echo "❌ Linting failed"
    exit 1
fi

# Tests
npm test
if [ $? -ne 0 ]; then
    echo "❌ Tests failed"
    exit 1
fi

echo "✅ Pre-commit passed"
exit 0
```

### Commit-msg exempel

```bash
#!/bin/sh
# .git/hooks/commit-msg

commit_msg=$(cat "$1")

# Kräv conventional commit format
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"; then
    echo "❌ Commit message must follow Conventional Commits"
    echo "   Example: feat(auth): add login feature"
    exit 1
fi

echo "✅ Commit message valid"
exit 0
```

---

## 🐕 Husky (Rekommenderat)

### Installation

```bash
# Installera Husky
npm install husky --save-dev

# Initiera
npx husky init

# Skapar .husky/ mapp och konfigurerar package.json
```

### Konfigurera hooks

```bash
# Pre-commit hook
echo "npm run lint && npm test" > .husky/pre-commit

# Commit-msg hook
echo "npx commitlint --edit \$1" > .husky/commit-msg
```

### Med lint-staged

```bash
# Kör lint endast på staged files (snabbare)
npm install lint-staged --save-dev
```

```json
// package.json
{
  "lint-staged": {
    "*.{js,ts}": ["eslint --fix", "prettier --write"],
    "*.{css,scss}": ["prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

```bash
# .husky/pre-commit
npx lint-staged
```

---

## 🔧 Commitlint

```bash
# Installera
npm install @commitlint/cli @commitlint/config-conventional --save-dev

# Konfigurera
echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js

# Hook
echo "npx commitlint --edit \$1" > .husky/commit-msg
```

### Conventional Commits

```bash
# Format: type(scope): description

feat(auth): add OAuth2 login
fix(api): handle null response
docs(readme): update installation
refactor(db): optimize queries
test(unit): add user tests
chore(deps): update packages
```

---

## 🏋️ Övningar

### Övning 1: Manuell hook
```bash
# Skapa pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "Pre-commit running..."
# Kolla att inga TODO finns
if git diff --cached | grep -i "TODO"; then
    echo "Found TODO in staged changes!"
    exit 1
fi
exit 0
EOF
chmod +x .git/hooks/pre-commit
```

### Övning 2: Husky setup
```bash
npm init -y
npm install husky lint-staged --save-dev
npx husky init
echo "npx lint-staged" > .husky/pre-commit
```

---

## 📚 Sammanfattning

| Hook | Syfte |
|------|-------|
| pre-commit | Kvalitetskontroll |
| commit-msg | Meddelandeformat |
| pre-push | Tester |
| Husky | Team-delning av hooks |
| lint-staged | Lint endast ändrade filer |

**Nästa steg:** Git Security

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Git Security",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 150,
        "content": r"""
# 🔒 Git Security

## Lärande mål
- Signera commits med GPG
- Undvika att committa secrets
- Ta bort känslig data från historik
- Security best practices

---

## 🔐 Signerade Commits

### Varför signera?

- Verifiera att commit verkligen kommer från dig
- Skydd mot impersonation
- Krav i vissa organisationer

### GPG Setup

```bash
# 1. Generera GPG-nyckel
gpg --full-generate-key
# Välj: RSA and RSA, 4096 bits, 0 (never expires)
# Ange namn och email (samma som Git config)

# 2. Lista nycklar
gpg --list-secret-keys --keyid-format=long
# sec   rsa4096/ABC123DEF456 2025-01-01
# uid   Your Name <email@example.com>

# 3. Konfigurera Git
git config --global user.signingkey ABC123DEF456
git config --global commit.gpgsign true

# 4. Exportera public key för GitHub
gpg --armor --export ABC123DEF456
# Kopiera och lägg till på GitHub > Settings > GPG keys
```

### Signera commits

```bash
# Signera enskild commit
git commit -S -m "Signed commit"

# Verifiera
git log --show-signature -1
git verify-commit HEAD
```

---

## 🚫 Undvik Secrets

### .gitignore för secrets

```bash
# .gitignore
.env
.env.*
*.pem
*.key
*.crt
secrets/
config/local.json
credentials.json
```

### Pre-commit scanning

```bash
# Installera detect-secrets
pip install detect-secrets

# Skapa baseline
detect-secrets scan > .secrets.baseline

# Pre-commit hook
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

### git-secrets

```bash
# AWS-specifik secret scanning
brew install git-secrets

# Konfigurera
git secrets --install
git secrets --register-aws

# Kör manuellt
git secrets --scan
```

---

## 🧹 Ta Bort Secrets från Historik

### BFG Repo-Cleaner (Rekommenderat)

```bash
# Installera
brew install bfg

# Ta bort fil från all historik
bfg --delete-files secrets.txt

# Ersätt text
echo "PASSWORD=****" > replacements.txt
bfg --replace-text replacements.txt

# Cleanup
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### git filter-branch (Långsammare)

```bash
# Ta bort fil
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.txt" \
  --prune-empty --tag-name-filter cat -- --all

# Cleanup
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push (kräver coordination med team!)
git push origin --force --all
```

### ⚠️ Varning

```
EFTER ATT DU TAR BORT FRÅN HISTORIK:
1. Rotera alla läckta secrets omedelbart
2. Koordinera med team - alla måste re-clone
3. Force push krävs
4. GitHub kan ha cacheade kopior
```

---

## 🛡️ Security Best Practices

### Repository

```bash
# Branch protection
# GitHub: Settings > Branches > Branch protection rules
# - Require PR reviews
# - Require status checks
# - Require signed commits

# CODEOWNERS
# .github/CODEOWNERS
* @security-team
/config/ @devops-team
```

### Development

```bash
# Använd environment variables
export API_KEY="secret"  # Inte i kod!

# Använd secret managers
# AWS Secrets Manager, HashiCorp Vault, etc.

# Git config för signing
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

---

## 🏋️ Övningar

### Övning 1: GPG signing
```bash
gpg --full-generate-key
git config --global commit.gpgsign true
git commit --allow-empty -m "Signed test"
git verify-commit HEAD
```

### Övning 2: Secret scanning
```bash
pip install detect-secrets
detect-secrets scan
# Kolla output för eventuella secrets
```

---

## 📚 Sammanfattning

| Åtgärd | Verktyg |
|--------|---------|
| Signera commits | GPG |
| Förhindra secrets | .gitignore, detect-secrets |
| Ta bort från historik | BFG |
| Branch protection | GitHub settings |

**Nästa steg:** Git Strategies

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Git Branching Strategies",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 📊 Git Branching Strategies

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
- Förstå Git Flow, GitHub Flow, Trunk-Based
- Välja rätt strategi för ditt team
- Implementera release management

---

## 🌊 Git Flow

### Struktur

```
+-----------------------------------------------------------------+
|                        GIT FLOW                                 |
+-----------------------------------------------------------------+
|                                                                 |
|  main ----●-----------------------------●-------●---------->   |
|           |                             ↑       |               |
|           |                             |       |               |
|  hotfix   +-------------●---------------+       |               |
|                         |                       |               |
|  release ---------------+-------●---------------+               |
|                         |       ↑                               |
|  develop ●------●-------+-------+---●---●---●--------------->  |
|          |      |       |       |   |   |   |                   |
|  feature +------+       +-------+   +---+   +-------------->   |
|                                                                 |
+-----------------------------------------------------------------+
```

### Branches

| Branch | Syfte | Livstid |
|--------|-------|---------|
| main | Produktion | Permanent |
| develop | Integration | Permanent |
| feature/* | Ny funktionalitet | Tillfällig |
| release/* | Förbered release | Tillfällig |
| hotfix/* | Akuta buggar | Tillfällig |

### Workflow

```bash
# Feature
git checkout develop
git checkout -b feature/login
# ... arbeta ...
git checkout develop
git merge --no-ff feature/login
git branch -d feature/login

# Release
git checkout develop
git checkout -b release/1.2.0
# ... testa, fixa ...
git checkout main
git merge --no-ff release/1.2.0
git tag -a v1.2.0
git checkout develop
git merge --no-ff release/1.2.0

# Hotfix
git checkout main
git checkout -b hotfix/1.2.1
# ... fixa ...
git checkout main
git merge --no-ff hotfix/1.2.1
git tag -a v1.2.1
git checkout develop
git merge --no-ff hotfix/1.2.1
```

---

## 🐙 GitHub Flow

### Enklare modell

```
main ----●---●---●---●---●---●---●---●---------------------->
         |       |       |       |
         |       |       |       +-- feature-4 (PR merge)
         |       |       +---------- feature-3 (PR merge)
         |       +------------------ feature-2 (PR merge)
         +-------------------------- feature-1 (PR merge)
```

### Regler

1. `main` är alltid deploybar
2. Skapa branch från main
3. Commit ofta, push ofta
4. Öppna PR för diskussion
5. Merge efter review
6. Deploy omedelbart efter merge

### Workflow

```bash
# 1. Skapa branch
git checkout main
git pull
git checkout -b feature/user-profile

# 2. Arbeta och pusha
git add . && git commit -m "Add profile page"
git push -u origin feature/user-profile

# 3. Skapa PR på GitHub

# 4. Review och merge

# 5. Deploy (automatiskt via CI/CD)
```

---

## 🌳 Trunk-Based Development

### Minimal branching

```
main/trunk ----●---●---●---●---●---●---●---●---●---●------>
                   |       |
                   |       +-- short-lived branch (max 1-2 dagar)
                   +---------- another short branch
```

### Principer

- Alla commitar till main (trunk)
- Korta branches (timmar, max dagar)
- Feature flags för ofärdig kod
- Continuous Integration är kritiskt

### Feature Flags

```javascript
// Kod bakom feature flag
if (featureFlags.newCheckout) {
  return <NewCheckoutFlow />;
} else {
  return <OldCheckoutFlow />;
}
```

### Workflow

```bash
# Direkt på main (små ändringar)
git checkout main
git pull
# ... liten ändring ...
git commit -m "Fix typo"
git push

# Kort branch (större ändringar)
git checkout -b quick-feature
# ... max 1-2 dagar arbete ...
git checkout main
git merge quick-feature
git push
```

---

## 🎯 Välj Rätt Strategi

| Faktor | Git Flow | GitHub Flow | Trunk-Based |
|--------|----------|-------------|-------------|
| Team-storlek | Stora | Medium | Alla |
| Release-cykel | Scheduled | Continuous | Continuous |
| Komplexitet | Hög | Låg | Låg |
| CI/CD-mognad | Valfritt | Viktigt | Kritiskt |
| Parallella versioner | Ja | Nej | Nej |

### Rekommendationer

```
Startup/litet team -> GitHub Flow eller Trunk-Based
Enterprise med scheduled releases -> Git Flow
Hög deployment-frekvens -> Trunk-Based
Open source -> GitHub Flow
```

---

## 🏋️ Övningar

### Övning: Implementera GitHub Flow
```bash
# Simluera komplett workflow
git checkout main
git checkout -b feature/new-thing
echo "feature" > feature.txt
git add . && git commit -m "feat: add new thing"
git push -u origin feature/new-thing
# Skapa PR på GitHub
# Merge via GitHub
git checkout main
git pull
```

---

## 📚 Sammanfattning

| Strategi | Bäst för |
|----------|----------|
| Git Flow | Scheduled releases, stora team |
| GitHub Flow | Continuous deployment |
| Trunk-Based | Snabb iteration, mogen CI/CD |

**Nästa steg:** Git Monorepo

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Git Monorepo & Large Files",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 145,
        "content": r"""
# 📦 Git Monorepo & Large Files

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
- Förstå monorepo vs polyrepo
- Hantera stora repositories
- Använda Git LFS för stora filer
- Sparse checkout och partial clone

---

## 🏢 Monorepo vs Polyrepo

### Monorepo

```
company-monorepo/
+-- apps/
|   +-- web/
|   +-- mobile/
|   +-- api/
+-- packages/
|   +-- ui/
|   +-- utils/
|   +-- shared/
+-- tools/
|   +-- scripts/
+-- package.json
```

### Fördelar Monorepo

| Fördel | Beskrivning |
|--------|-------------|
| Atomic changes | Ändra flera paket i en commit |
| Code sharing | Enkel delning av kod |
| Tooling | Ett build-system |
| Refactoring | Enklare stora ändringar |

### Nackdelar

| Nackdel | Lösning |
|---------|---------|
| Stort repo | Sparse checkout, LFS |
| CI/CD komplexitet | Affected/changed detection |
| Permissions | CODEOWNERS, branch rules |

---

## 🔧 Monorepo Verktyg

### Turborepo

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
    },
    "lint": {}
  }
}
```

```bash
# Kör på alla packages
turbo run build

# Endast affected
turbo run build --filter=...[origin/main]

# Specifikt package
turbo run build --filter=@company/web
```

### Nx

```bash
# Installera
npx create-nx-workspace

# Affected commands
nx affected:build
nx affected:test
nx affected:lint

# Dependency graph
nx graph
```

---

## 📁 Git LFS

### För stora filer

```bash
# Installera
brew install git-lfs
git lfs install

# Tracka filtyper
git lfs track "*.psd"
git lfs track "*.mp4"
git lfs track "*.zip"

# Se vad som trackas
cat .gitattributes
# *.psd filter=lfs diff=lfs merge=lfs -text

# Commit som vanligt
git add large-file.psd
git commit -m "Add design file"
git push
```

### LFS Kommandon

```bash
# Lista LFS filer
git lfs ls-files

# Pull LFS content
git lfs pull

# Status
git lfs status

# Migrate existerande filer
git lfs migrate import --include="*.psd"
```

---

## ✂️ Sparse Checkout

### Checka ut endast del av repo

```bash
# Initiera sparse checkout
git clone --filter=blob:none --sparse <url>
cd repo

# Lägg till mappar
git sparse-checkout set apps/web packages/shared

# Visa vad som är checkout:at
git sparse-checkout list

# Lägg till fler
git sparse-checkout add apps/mobile

# Inaktivera
git sparse-checkout disable
```

---

## 🚀 Partial Clone

### Clone utan alla blobs

```bash
# Blobless clone (hämtar blobs on-demand)
git clone --filter=blob:none <url>

# Treeless clone (hämtar trees on-demand)
git clone --filter=tree:0 <url>

# Shallow clone (begränsad historik)
git clone --depth=1 <url>
git clone --shallow-since="2025-01-01" <url>
```

---

## 🏋️ Övningar

### Övning 1: Git LFS
```bash
git lfs install
git lfs track "*.zip"
echo "large content" > test.zip
git add .gitattributes test.zip
git commit -m "Add large file with LFS"
git lfs ls-files
```

### Övning 2: Sparse checkout
```bash
git clone --filter=blob:none --sparse https://github.com/vercel/next.js
cd next.js
git sparse-checkout set packages/next
ls packages/
```

---

## 📚 Sammanfattning

| Verktyg | Användning |
|---------|-----------|
| Turborepo/Nx | Monorepo management |
| Git LFS | Stora binärfiler |
| Sparse checkout | Checka ut delar av repo |
| Partial clone | Clone utan all data |

**Nästa steg:** Git Troubleshooting

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Git Troubleshooting & Recovery",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🔧 Git Troubleshooting & Recovery

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
- Återställa förlorat arbete med reflog
- Felsöka vanliga Git-problem
- Använda git fsck
- Recovery-strategier

---

## 🆘 Git Reflog - Din Livlina

### Vad är reflog?

Reflog sparar ALLA HEAD-ändringar, även de som "försvinner".

```bash
# Se reflog
git reflog
# abc123 HEAD@{0}: commit: Latest commit
# def456 HEAD@{1}: reset: moving to HEAD~1
# ghi789 HEAD@{2}: commit: Accidentally deleted commit

# Detaljerad
git reflog show --all
```

### Återställ förlorad commit

```bash
# Scenario: git reset --hard tog bort commits
git reflog
# Hitta commit före reset

# Återställ
git reset --hard HEAD@{2}
# eller skapa branch
git branch recovered HEAD@{2}
```

### Återställ raderad branch

```bash
# Scenario: git branch -D raderade viktigt arbete
git reflog
# Hitta senaste commit på branchen

git checkout -b restored-branch HEAD@{5}
```

---

## 🔍 Git Fsck

### Hitta dangling objects

```bash
# Sök efter orefrerade objects
git fsck --lost-found

# Output:
# dangling commit abc123
# dangling blob def456

# Återställ dangling commit
git show abc123
git branch recovered abc123
```

---

## ⚠️ Vanliga Problem

### "Detached HEAD"

```bash
# Problem: HEAD pekar på commit, inte branch
# Lösning: Skapa branch
git branch my-work
git checkout my-work

# Eller om du vill tillbaka
git checkout main
```

### Merge conflicts vid pull

```bash
# Problem: Konflikter vid git pull
# Lösning 1: Lös konflikter
git status  # Se conflicted files
# Redigera filer
git add .
git commit

# Lösning 2: Abort och rebase istället
git merge --abort
git pull --rebase
```

### "Your branch has diverged"

```bash
# Problem: Lokal och remote har divergerat
# Lösning 1: Merge (standard)
git pull

# Lösning 2: Rebase (renare historik)
git pull --rebase

# Lösning 3: Force push (om ensam på branch)
git push --force-with-lease
```

### Ångra push

```bash
# Scenario: Pushade fel commit
# Lösning 1: Revert (säkert)
git revert HEAD
git push

# Lösning 2: Reset + force push (om ensam)
git reset --hard HEAD~1
git push --force-with-lease
```

### Commit på fel branch

```bash
# Scenario: Commitade på main istället för feature
# Lösning:
git branch feature  # Skapa branch med commit
git reset --hard HEAD~1  # Ta bort från main
git checkout feature  # Fortsätt på rätt branch
```

### Stora filer av misstag

```bash
# Problem: Commitade stor fil
# Lösning före push:
git reset --soft HEAD~1
git restore --staged large-file.zip
echo "large-file.zip" >> .gitignore
git commit -m "Original commit without large file"

# Lösning efter push:
# Använd BFG (se Git Security lektionen)
```

---

## 🧹 Cleanup & Maintenance

### Garbage collection

```bash
# Automatic cleanup
git gc

# Aggressive cleanup
git gc --aggressive --prune=now

# Prune unreachable objects
git prune
```

### Repo-storlek

```bash
# Se storlek
git count-objects -v

# Hitta stora filer i historik
git rev-list --objects --all | \
git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
awk '/^blob/ {print $3, $4}' | \
sort -rn | head -10
```

---

## 🏋️ Övningar

### Övning 1: Reflog recovery
```bash
# Skapa commits
mkdir reflog-test && cd reflog-test && git init
echo "a" > f && git add . && git commit -m "A"
echo "b" >> f && git commit -am "B"
echo "c" >> f && git commit -am "C"

# "Förlora" commits
git reset --hard HEAD~2

# Återställ
git reflog
git reset --hard HEAD@{1}
git log --oneline
```

### Övning 2: Fixa detached HEAD
```bash
git checkout HEAD~2  # Detached!
echo "work" > new.txt && git add . && git commit -m "New work"
git branch save-work  # Spara!
git checkout main
git merge save-work
```

---

## 📚 Sammanfattning

| Problem | Lösning |
|---------|---------|
| Förlorad commit | git reflog + reset |
| Raderad branch | git reflog + checkout -b |
| Detached HEAD | git branch + checkout |
| Merge conflicts | Lösa eller abort + rebase |
| Fel commit pushad | revert eller reset + force |
| Stor fil | BFG eller filter-branch |

**Grattis! Du har slutfört Git & GitHub Mastery!** 🎉

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
]
