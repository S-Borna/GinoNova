# -*- coding: utf-8 -*-
"""
CI/CD SkillsMap - 20 Consolidated Nodes
Version: 1.0
Date: 2025-12-02

Pedagogical Style: Akhilesh (Intro -> Concept -> Code -> Pro Tips -> Task)
Focus: Continuous Integration, Continuous Delivery, Pipelines, GitOps
"""

from typing import Literal, List, Dict, Any

DifficultyLevel = Literal["beginner", "intermediate", "advanced", "expert"]


# =============================================================================
# CI/CD SKILLSMAP METADATA
# =============================================================================

CICD_SKILLSMAP_INFO = {
    "name": "CI/CD Mastery",
    "slug": "cicd-mastery",
    "description": "Master continuous integration and delivery - from pipelines to GitOps",
    "total_nodes": 20,
    "estimated_hours": 40,
    "difficulty_range": "beginner to advanced",
    "focus": "GitHub Actions, GitLab CI, Jenkins, ArgoCD, GitOps",
}


# =============================================================================
# NODE 1: CI/CD FUNDAMENTALS
# =============================================================================

NODE_01_CICD_FUNDAMENTALS = {
    "node_id": 1,
    "title": "CI/CD Fundamentals",
    "slug": "cicd-fundamentals",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 60,
    "topics_covered": [
        "continuous integration", "continuous delivery", "continuous deployment",
        "pipeline concepts", "build automation", "test automation",
        "deployment strategies", "feedback loops"
    ],
    "content": r'''# CI/CD Fundamentals

## Varfor CI/CD ar Kritiskt

> "Without CI/CD, you're deploying with fear. With CI/CD, you're deploying with confidence."

Forestall dig: Det ar fredag eftermiddag. En kritisk buggfix maste ut i produktion.
Utan CI/CD: Manuell build, manuella tester, manuell deploy. Stress. Risk for fel.
Med CI/CD: `git push` → Automatisk pipeline → Deploy pa minuter. Lugnt och sakert.

## Vad du kommer lara dig

- Skillnaden mellan CI, CD och CD (ja, det finns tva CD:n)
- Pipeline-koncept och stages
- Varfor automation ar nyckeln
- Vanliga verktyg och deras anvandning

---

## Continuous Integration (CI)

### Koncept

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Developer │───▶│   Git Push  │───▶│   CI Server │
│   Commits   │    │   Trigger   │    │   Builds    │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                   ┌─────────────┐    ┌──────▼──────┐
                   │   Feedback  │◀───│  Run Tests  │
                   │   (Pass/Fail)│    │  (Auto)     │
                   └─────────────┘    └─────────────┘
```

**CI handlar om:**
- Merga kod ofta (minst dagligen)
- Automatisk build vid varje push
- Automatiska tester
- Snabb feedback till utvecklare

### Varfor CI?

```python
# UTAN CI - "Works on my machine" syndromet
developer_1_code = "fungerar lokalt"
developer_2_code = "fungerar lokalt"
merged_code = "KRASCHAR I PRODUKTION"  # Integration helvete

# MED CI - Tidig feedback
developer_1_code = "fungerar lokalt"
git_push()  # Trigger CI
ci_result = run_tests()  # Kraschar DIREKT
# Fixas innan det nar produktion!
```

---

## Continuous Delivery (CD)

### Koncept

```
CI Pipeline
    │
    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Build     │───▶│   Test      │───▶│   Stage     │
│   Artifact  │    │   Suite     │    │   Deploy    │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                   ┌─────────────┐    ┌──────▼──────┐
                   │  Production │◀───│   Manual    │
                   │   Deploy    │    │   Approval  │
                   └─────────────┘    └─────────────┘
```

**CD (Delivery) innebar:**
- Kod ar ALLTID redo att deployeras
- Automatisk deploy till staging/test
- Manuell godkannande for produktion
- Release nar affaren vill

---

## Continuous Deployment (CD)

### Koncept

```
CI Pipeline
    │
    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Build     │───▶│   Test      │───▶│  Production │
│   Artifact  │    │   Suite     │    │   Deploy    │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                      ┌──────▼──────┐
                                      │   LIVE!     │
                                      │   (Auto)    │
                                      └─────────────┘
```

**CD (Deployment) innebar:**
- VARJE lyckad commit gar till produktion
- Ingen manuell intervention
- Kraver extremt bra tester
- Netflix, Amazon, Google-stil

---

## Pipeline Stages

### Typisk Pipeline

```yaml
# Konceptuell pipeline
stages:
  - build      # Kompilera kod, skapa artifact
  - test       # Unit tests, integration tests
  - security   # SAST, dependency scanning
  - staging    # Deploy till test-miljo
  - approval   # Manuell godkannande (optional)
  - production # Deploy till prod
```

### Stage Breakdown

| Stage | Syfte | Typisk tid |
|-------|-------|------------|
| Build | Kompilera, paketera | 1-5 min |
| Unit Tests | Testa enskilda funktioner | 1-3 min |
| Integration Tests | Testa komponenter ihop | 5-15 min |
| Security Scan | Hitta sarbarheter | 2-10 min |
| Staging Deploy | Test i prod-lik miljo | 2-5 min |
| Production Deploy | Live! | 2-10 min |

---

## Vanliga CI/CD Verktyg

### Molnbaserade

| Verktyg | Bast for | Pris |
|---------|----------|------|
| GitHub Actions | GitHub-repos | Gratis (2000 min/manad) |
| GitLab CI | GitLab-repos | Gratis (400 min/manad) |
| CircleCI | Alla repos | Gratis tier finns |
| Travis CI | Open source | Gratis for OSS |

### Self-hosted

| Verktyg | Bast for | Komplexitet |
|---------|----------|-------------|
| Jenkins | Enterprise, flexibilitet | Hog |
| Drone | Container-native | Medium |
| Tekton | Kubernetes-native | Hog |
| Woodpecker | Enkel, latt | Lag |

### GitOps

| Verktyg | Bast for |
|---------|----------|
| ArgoCD | Kubernetes GitOps |
| Flux | Kubernetes GitOps |

---

## Pro Tips

> **Tip 1:** Borja enkelt. En basic pipeline som bygger och testar ar battre an ingen pipeline.

> **Tip 2:** "Fail fast" - Satt snabba tester forst i pipelinen. Ingen vill vanta 20 min for att fa veta att en syntax-fel finns.

> **Tip 3:** Testa lokalt forst! De flesta CI-verktyg har lokala runners (act for GitHub Actions, gitlab-runner for GitLab).

---

## Hands-on Task

### Uppgift: Forstå din nuvarande deployment-process

1. Dokumentera hur du deployar idag:
   - Hur manga manuella steg?
   - Hur lang tid tar det?
   - Vad kan ga fel?

2. Identifiera automation-mojligheter:
   - Vilka steg kan automatiseras?
   - Var behover du manuell godkannande?

3. Valj ett CI/CD-verktyg att lara dig (rekommendation: GitHub Actions for nyborjare)

---

## Sammanfattning

| Begrepp | Betydelse |
|---------|-----------|
| CI | Automatisk build + test vid varje commit |
| CD (Delivery) | Alltid redo att deploya, manuell trigger |
| CD (Deployment) | Automatisk deploy till produktion |
| Pipeline | Sekvens av steg fran kod till produktion |
| Stage | Ett steg i pipelinen (build, test, deploy) |

**Nasta steg:** Node 2 - GitHub Actions Grunderna
''',
}


# =============================================================================
# NODE 2: GITHUB ACTIONS BASICS
# =============================================================================

NODE_02_GITHUB_ACTIONS_BASICS = {
    "node_id": 2,
    "title": "GitHub Actions Grunderna",
    "slug": "github-actions-basics",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 70,
    "topics_covered": [
        "workflows", "jobs", "steps", "runners",
        "triggers", "events", "yaml syntax", "first workflow"
    ],
    "content": r'''# GitHub Actions Grunderna

## Varfor GitHub Actions?

> "GitHub Actions ar det enklaste sattet att komma igang med CI/CD - det ar redan dar du har din kod."

GitHub Actions ar:
- Integrerat i GitHub (ingen extern setup)
- Gratis for publika repos
- 2000 gratis minuter/manad for privata repos
- Enorm marketplace med fardiga actions

---

## Workflow Struktur

### Fil-placering

```
your-repo/
├── .github/
│   └── workflows/
│       ├── ci.yml           # CI pipeline
│       ├── deploy.yml       # Deploy pipeline
│       └── scheduled.yml    # Scheduled jobs
├── src/
└── README.md
```

### Grundlaggande Struktur

```yaml
# .github/workflows/ci.yml

name: CI Pipeline              # Workflow-namn (visas i GitHub UI)

on:                            # TRIGGERS - nar ska workflow koras?
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:                          # JOBS - vad ska goras?
  build:
    runs-on: ubuntu-latest     # RUNNER - var kors det?

    steps:                     # STEPS - steg-for-steg
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run tests
        run: npm test
```

---

## Triggers (on:)

### Push Trigger

```yaml
on:
  push:
    branches:
      - main
      - 'feature/**'    # Alla feature-branches
    paths:
      - 'src/**'        # Bara om src/ andras
      - '!**.md'        # Ignorera markdown-filer
```

### Pull Request Trigger

```yaml
on:
  pull_request:
    branches: [main]
    types:
      - opened
      - synchronize
      - reopened
```

### Scheduled Trigger (Cron)

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Varje natt kl 02:00 UTC
    # ┬ ┬ ┬ ┬ ┬
    # │ │ │ │ └── Veckodag (0-7, 0=sondag)
    # │ │ │ └──── Manad (1-12)
    # │ │ └────── Dag (1-31)
    # │ └──────── Timme (0-23)
    # └────────── Minut (0-59)
```

### Manual Trigger

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

---

## Jobs och Steps

### Multipla Jobs

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  build:
    runs-on: ubuntu-latest
    needs: test              # Kors EFTER test-jobbet
    steps:
      - uses: actions/checkout@v4
      - run: npm run build

  deploy:
    runs-on: ubuntu-latest
    needs: [test, build]     # Kors efter BADA
    steps:
      - run: echo "Deploying..."
```

### Job Dependencies

```
┌──────┐    ┌──────┐    ┌──────┐
│ test │───▶│build │───▶│deploy│
└──────┘    └──────┘    └──────┘
   │                        ▲
   └────────────────────────┘
        (parallel ocksa ok)
```

---

## Runners

### GitHub-hosted Runners

```yaml
jobs:
  linux:
    runs-on: ubuntu-latest      # eller ubuntu-22.04, ubuntu-20.04

  macos:
    runs-on: macos-latest       # eller macos-13, macos-12

  windows:
    runs-on: windows-latest     # eller windows-2022, windows-2019
```

### Self-hosted Runners

```yaml
jobs:
  internal:
    runs-on: self-hosted        # Din egen server
    # eller
    runs-on: [self-hosted, linux, x64]  # Med labels
```

---

## Ditt Forsta Workflow

### Steg 1: Skapa workflow-fil

```bash
mkdir -p .github/workflows
touch .github/workflows/ci.yml
```

### Steg 2: Skriv workflow

```yaml
# .github/workflows/ci.yml
name: My First CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  hello:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Hello World
        run: echo "Hello from GitHub Actions!"

      - name: Show repository info
        run: |
          echo "Repository: ${{ github.repository }}"
          echo "Branch: ${{ github.ref_name }}"
          echo "Commit: ${{ github.sha }}"

      - name: List files
        run: ls -la
```

### Steg 3: Pusha och se magin

```bash
git add .github/
git commit -m "Add first GitHub Actions workflow"
git push
```

Ga till: `https://github.com/<user>/<repo>/actions`

---

## Pro Tips

> **Tip 1:** Anvand `@v4` (version tags) istallet for `@main` for actions. Mer stabilt.

> **Tip 2:** Anvand `actions/checkout@v4` ALLTID forst - annars finns inte din kod!

> **Tip 3:** Testa workflows med [act](https://github.com/nektos/act) lokalt:
> ```bash
> brew install act
> act push
> ```

---

## Hands-on Task

### Uppgift: Skapa ditt forsta workflow

1. Skapa `.github/workflows/ci.yml` i ett repo
2. Lagg till basic triggers (push + PR)
3. Lagg till steps som:
   - Checkar ut koden
   - Visar repository-info
   - Listar filer
4. Pusha och verifiera att det kors

**Bonus:** Lagg till ett misslyckat steg (`exit 1`) och se hur det ser ut i UI.

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| Workflow | Hel automation-fil (.yml) |
| Job | Grupp av steps som kors pa samma runner |
| Step | Enskilt kommando eller action |
| Runner | Maskin som kor jobbet |
| Trigger (on:) | Vad som startar workflow |
| Action | Ateranvandbar komponent (uses:) |

**Nasta steg:** Node 3 - GitHub Actions: Environment & Secrets
''',
}


# =============================================================================
# NODE 3: GITHUB ACTIONS ENVIRONMENT & SECRETS
# =============================================================================

NODE_03_GITHUB_ACTIONS_ENV_SECRETS = {
    "node_id": 3,
    "title": "GitHub Actions: Environment & Secrets",
    "slug": "github-actions-env-secrets",
    "difficulty": "beginner",
    "estimated_minutes": 50,
    "xp_reward": 65,
    "topics_covered": [
        "environment variables", "secrets", "contexts",
        "environment protection", "GITHUB_TOKEN", "encrypted secrets"
    ],
    "content": r'''# GitHub Actions: Environment & Secrets

## Varfor Secrets?

> "Never, EVER, commit credentials to git. GitHub Actions secrets ar din vän."

Credentials i kod = sarbarhetsrisk
Secrets i GitHub = krypterat, savert, auditat

---

## Environment Variables

### Workflow-level

```yaml
name: CI

env:                           # Tillganglig i ALLA jobs
  NODE_ENV: production
  APP_NAME: my-app

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "App: $APP_NAME, Env: $NODE_ENV"
```

### Job-level

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:                       # Bara i DETTA job
      DATABASE_URL: postgresql://localhost/test

    steps:
      - run: echo $DATABASE_URL
```

### Step-level

```yaml
steps:
  - name: Deploy
    env:                       # Bara i DETTA step
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
    run: ./deploy.sh
```

---

## GitHub Secrets

### Skapa Secrets (UI)

```
Repository → Settings → Secrets and variables → Actions
    └── New repository secret
        Name: AWS_ACCESS_KEY_ID
        Value: AKIA...
```

### Anvanda Secrets

```yaml
steps:
  - name: Configure AWS
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    run: aws s3 ls

  - name: Docker login
    run: |
      echo "${{ secrets.DOCKER_PASSWORD }}" | \
        docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
```

### Secret Scopes

| Scope | Tillganglighet |
|-------|----------------|
| Repository secrets | Bara detta repo |
| Environment secrets | Bara specifik environment |
| Organization secrets | Alla/valda repos i org |

---

## GITHUB_TOKEN

### Automatisk Token

```yaml
# GitHub skapar automatiskt GITHUB_TOKEN for varje workflow
steps:
  - name: Create Release
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: gh release create v1.0.0

  - name: Push to repo
    run: |
      git config user.name github-actions
      git config user.email github-actions@github.com
      git push
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### GITHUB_TOKEN Permissions

```yaml
# Default: read for PR, write for push
# Anpassa permissions:
permissions:
  contents: write        # Pusha commits
  pull-requests: write   # Kommentera PR
  issues: write         # Skapa issues
  packages: write       # Pusha paket
```

---

## Contexts

### GitHub Context

```yaml
steps:
  - run: |
      echo "Repository: ${{ github.repository }}"
      echo "Owner: ${{ github.repository_owner }}"
      echo "SHA: ${{ github.sha }}"
      echo "Ref: ${{ github.ref }}"
      echo "Branch: ${{ github.ref_name }}"
      echo "Event: ${{ github.event_name }}"
      echo "Actor: ${{ github.actor }}"
      echo "Run ID: ${{ github.run_id }}"
      echo "Run Number: ${{ github.run_number }}"
```

### Env Context

```yaml
env:
  MY_VAR: hello

steps:
  - run: echo "${{ env.MY_VAR }}"  # "hello"
```

### Secrets Context

```yaml
steps:
  - run: echo "${{ secrets.API_KEY }}"  # Maskeras i loggar
```

---

## Environments

### Skapa Environment (UI)

```
Repository → Settings → Environments → New environment
    Name: production
    Protection rules:
      ✓ Required reviewers (lagg till approvers)
      ✓ Wait timer (ex: 5 minuter)
      ✓ Deployment branches (bara main)
```

### Anvanda Environment

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging         # Anvander staging secrets
    steps:
      - run: ./deploy.sh

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-staging
    environment:
      name: production
      url: https://myapp.com     # Visas i GitHub UI
    steps:
      - run: ./deploy.sh
```

### Environment-specifika Secrets

```yaml
# staging environment har:
#   API_URL = https://api.staging.example.com
# production environment har:
#   API_URL = https://api.example.com

jobs:
  deploy:
    environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
    steps:
      - run: curl ${{ secrets.API_URL }}  # Ratt URL baserat pa environment
```

---

## Pro Tips

> **Tip 1:** Secrets maskeras automatiskt i loggar. Men var forsiktig med `base64` eller liknande som kan avsloja dem!

> **Tip 2:** Rotera secrets regelbundet. Anvand GitHub CLI:
> ```bash
> gh secret set API_KEY --body "new-value"
> ```

> **Tip 3:** Anvand environments for prod-deploys med required reviewers - ingen kan accidentellt deploya till prod!

---

## Hands-on Task

### Uppgift: Satt upp secrets och environments

1. Skapa ett repository secret: `TEST_SECRET`

2. Skapa tva environments: `staging` och `production`

3. Lagg till environment-specifika secrets i varje

4. Skapa workflow som anvander ratt environment:

```yaml
name: Deploy

on:
  push:
    branches: [main, develop]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}

    steps:
      - name: Show environment
        run: |
          echo "Deploying to: ${{ github.ref_name }}"
          echo "API URL: ${{ secrets.API_URL }}"
```

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| `env:` | Vanliga environment variables |
| `secrets.X` | Krypterade hemligheter |
| `GITHUB_TOKEN` | Automatisk token for repo-operationer |
| Environment | Isolerad deploy-miljo med egna secrets |
| Context | Tillgang till metadata (`github.`, `env.`, etc) |

**Nasta steg:** Node 4 - GitHub Actions: Build & Test
''',
}


# =============================================================================
# NODE 4: GITHUB ACTIONS BUILD & TEST
# =============================================================================

NODE_04_GITHUB_ACTIONS_BUILD_TEST = {
    "node_id": 4,
    "title": "GitHub Actions: Build & Test",
    "slug": "github-actions-build-test",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 75,
    "topics_covered": [
        "build workflows", "test automation", "matrix builds",
        "caching", "artifacts", "test reporting"
    ],
    "content": r'''# GitHub Actions: Build & Test

## CI Pipeline i Praktiken

> "En bra CI-pipeline ar snabb, palitlig och ger tydlig feedback."

Build + Test ar hjartat av CI. Lat oss bygga en riktig pipeline.

---

## Node.js Projekt

### Komplett CI Pipeline

```yaml
name: Node.js CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'           # Automatisk npm cache!

      - name: Install dependencies
        run: npm ci              # ci ar snabbare an install

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build
```

---

## Python Projekt

### Komplett CI Pipeline

```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8

      - name: Lint with flake8
        run: flake8 src/ --max-line-length=100

      - name: Run tests with coverage
        run: pytest --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
```

---

## Matrix Builds

### Testa mot flera versioner

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]
        # Skapar 3 parallella jobs!

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm test
```

### Multi-dimensional Matrix

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    python-version: ['3.10', '3.11', '3.12']
    # Skapar 3 x 3 = 9 parallella jobs!

runs-on: ${{ matrix.os }}
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: ${{ matrix.python-version }}
```

### Exclude och Include

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20]
    exclude:
      - os: windows-latest
        node: 18            # Skippa Windows + Node 18
    include:
      - os: ubuntu-latest
        node: 22
        experimental: true  # Lagg till extra kombination
```

---

## Caching

### Automatisk Cache (Setup Actions)

```yaml
# Dessa actions har inbyggd cache:
- uses: actions/setup-node@v4
  with:
    cache: 'npm'           # Cachar ~/.npm

- uses: actions/setup-python@v5
  with:
    cache: 'pip'           # Cachar pip

- uses: actions/setup-go@v5
  with:
    cache: true            # Cachar go modules
```

### Manuell Cache

```yaml
- name: Cache node_modules
  uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

### Cache Strategi

```
┌─────────────┐
│  Forsta run │
│  Cache MISS │─────▶ Installera → Spara cache
└─────────────┘

┌─────────────┐
│  Andra run  │
│  Cache HIT  │─────▶ Ladda cache → Skippa install
└─────────────┘
                      (10x snabbare!)
```

---

## Artifacts

### Spara Build Output

```yaml
- name: Build
  run: npm run build

- name: Upload build artifact
  uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 5
```

### Anvand Artifact i Annat Job

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: dist
          path: dist/
      - run: ls dist/  # Build-filerna finns har!
```

---

## Test Reporting

### Jest med Coverage

```yaml
- name: Run tests
  run: npm test -- --coverage --reporters=jest-junit
  env:
    JEST_JUNIT_OUTPUT_DIR: ./reports

- name: Upload test results
  uses: actions/upload-artifact@v4
  if: always()  # Aven om tester failar!
  with:
    name: test-results
    path: reports/
```

### Pytest med JUnit

```yaml
- name: Run tests
  run: pytest --junitxml=reports/junit.xml

- name: Publish test results
  uses: mikepenz/action-junit-report@v4
  if: always()
  with:
    report_paths: 'reports/*.xml'
```

---

## Pro Tips

> **Tip 1:** Anvand `npm ci` istallet for `npm install` - det ar snabbare och mer deterministiskt.

> **Tip 2:** Satt `if: always()` pa artifact uploads sa du far dem aven nar tester failar.

> **Tip 3:** Matrix builds ar gratis parallellism - anvand dem for att testa mot flera versioner!

---

## Hands-on Task

### Uppgift: Bygg en komplett CI-pipeline

Skapa en pipeline som:

1. Kor pa push till main och PR
2. Anvander matrix for Node 18 + 20
3. Cachar dependencies
4. Kor lint + tests + build
5. Sparar build artifacts

```yaml
name: Complete CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [18, 20]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'

      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build

      - uses: actions/upload-artifact@v4
        if: matrix.node == 20  # Bara fran en version
        with:
          name: build-${{ github.sha }}
          path: dist/
```

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| Matrix | Parallella builds med olika konfigurationer |
| Cache | Spara dependencies mellan runs |
| Artifacts | Spara output-filer (build, reports) |
| `npm ci` | Snabbare, reproducerbar install |
| `if: always()` | Kor step aven vid failure |

**Nasta steg:** Node 5 - GitHub Actions: Deployment
''',
}


# =============================================================================
# NODE 5: GITHUB ACTIONS DEPLOYMENT
# =============================================================================

NODE_05_GITHUB_ACTIONS_DEPLOYMENT = {
    "node_id": 5,
    "title": "GitHub Actions: Deployment",
    "slug": "github-actions-deployment",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 80,
    "topics_covered": [
        "deployment workflows", "environments", "cloud deploys",
        "Docker builds", "Kubernetes deploys", "rollback strategies"
    ],
    "content": r'''# GitHub Actions: Deployment

## Deployment Automation

> "The best deployment is the one you don't have to think about."

Fran git push till live produktion - automatiskt.

---

## Deploy till Cloud Providers

### AWS (S3 + CloudFront)

```yaml
name: Deploy to AWS

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Build
        run: npm run build

      - name: Deploy to S3
        run: aws s3 sync dist/ s3://${{ secrets.S3_BUCKET }} --delete

      - name: Invalidate CloudFront
        run: |
          aws cloudfront create-invalidation \
            --distribution-id ${{ secrets.CF_DISTRIBUTION_ID }} \
            --paths "/*"
```

### Vercel

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```

### Netlify

```yaml
name: Deploy to Netlify

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build

      - name: Deploy to Netlify
        uses: nwtgck/actions-netlify@v2
        with:
          publish-dir: './dist'
          production-deploy: true
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
```

---

## Docker Build & Push

### Build och Pusha till Docker Hub

```yaml
name: Docker Build

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myuser/myapp:latest
            myuser/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Multi-platform Build

```yaml
- name: Build multi-platform
  uses: docker/build-push-action@v5
  with:
    context: .
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myuser/myapp:latest
```

---

## Kubernetes Deployment

### Deploy med kubectl

```yaml
name: Deploy to K8s

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl
        uses: azure/k8s-set-context@v3
        with:
          kubeconfig: ${{ secrets.KUBE_CONFIG }}

      - name: Update image tag
        run: |
          sed -i "s|IMAGE_TAG|${{ github.sha }}|g" k8s/deployment.yaml

      - name: Deploy
        run: kubectl apply -f k8s/

      - name: Wait for rollout
        run: kubectl rollout status deployment/myapp -n production
```

### Deploy med Helm

```yaml
- name: Deploy with Helm
  run: |
    helm upgrade --install myapp ./charts/myapp \
      --namespace production \
      --set image.tag=${{ github.sha }} \
      --wait
```

---

## Deployment Strategies

### Blue-Green

```yaml
jobs:
  deploy:
    steps:
      - name: Deploy to green
        run: kubectl apply -f k8s/green/

      - name: Health check
        run: |
          for i in {1..30}; do
            if curl -s http://green.internal/health | grep -q "ok"; then
              echo "Green is healthy!"
              break
            fi
            sleep 2
          done

      - name: Switch traffic
        run: |
          kubectl patch service myapp \
            -p '{"spec":{"selector":{"version":"green"}}}'
```

### Canary

```yaml
- name: Deploy canary (10%)
  run: |
    kubectl apply -f k8s/canary/
    kubectl scale deployment myapp-canary --replicas=1
    kubectl scale deployment myapp-stable --replicas=9

- name: Monitor metrics
  run: |
    # Vanta och analysera error rates
    sleep 300

- name: Promote or rollback
  run: |
    if [ "$ERROR_RATE" -lt "1" ]; then
      kubectl scale deployment myapp-canary --replicas=10
      kubectl delete deployment myapp-stable
    else
      kubectl delete deployment myapp-canary
      echo "Rollback - keeping stable"
    fi
```

---

## Rollback

### Automatisk Rollback

```yaml
- name: Deploy
  run: kubectl apply -f k8s/

- name: Wait for rollout
  id: rollout
  run: kubectl rollout status deployment/myapp --timeout=5m
  continue-on-error: true

- name: Rollback on failure
  if: steps.rollout.outcome == 'failure'
  run: |
    kubectl rollout undo deployment/myapp
    echo "::error::Deployment failed, rolled back!"
    exit 1
```

---

## Pro Tips

> **Tip 1:** Anvand `environment: production` med required reviewers for prod-deploys.

> **Tip 2:** Tagga Docker images med git SHA (`${{ github.sha }}`) for full spårbarhet.

> **Tip 3:** Implementera health checks och automatisk rollback - det raddar liv!

---

## Hands-on Task

### Uppgift: Bygg en deploy-pipeline

1. Valj din deployment target (Vercel, Netlify, eller Docker Hub)

2. Satt upp secrets i GitHub

3. Skapa deploy workflow:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build

      # Lagg till din deployment step har
```

4. Testa genom att pusha till main!

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| Environment | Isolerad deploy-miljo (staging, production) |
| Docker Build | Bygg och pusha container images |
| K8s Deploy | Deploya till Kubernetes |
| Blue-Green | Tva identiska miljoer, switch trafik |
| Canary | Gradvis utrullning, monitorera |
| Rollback | Aterstall till tidigare version |

**Nasta steg:** Node 6 - GitHub Actions: Reusable Workflows
''',
}


# =============================================================================
# NODE 6: GITHUB ACTIONS REUSABLE WORKFLOWS
# =============================================================================

NODE_06_GITHUB_ACTIONS_REUSABLE = {
    "node_id": 6,
    "title": "GitHub Actions: Reusable Workflows",
    "slug": "github-actions-reusable",
    "difficulty": "intermediate",
    "estimated_minutes": 50,
    "xp_reward": 70,
    "topics_covered": [
        "reusable workflows", "composite actions", "workflow_call",
        "inputs", "outputs", "organization workflows"
    ],
    "content": r'''# GitHub Actions: Reusable Workflows

## DRY Principle i CI/CD

> "Copy-paste ar teknisk skuld. Reusable workflows ar investering."

Istallet for att kopiera samma workflow till 50 repos - skapa en gang, anvand overallt.

---

## Reusable Workflow

### Skapa Reusable Workflow

```yaml
# .github/workflows/reusable-build.yml
name: Reusable Build

on:
  workflow_call:             # Gor den anropbar!
    inputs:
      node-version:
        description: 'Node.js version'
        required: false
        default: '20'
        type: string
      working-directory:
        description: 'Working directory'
        required: false
        default: '.'
        type: string
    secrets:
      npm-token:
        description: 'NPM auth token'
        required: false

jobs:
  build:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ${{ inputs.working-directory }}

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'

      - run: npm ci
        env:
          NPM_TOKEN: ${{ secrets.npm-token }}

      - run: npm test
      - run: npm run build
```

### Anropa Reusable Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]

jobs:
  build:
    uses: ./.github/workflows/reusable-build.yml
    with:
      node-version: '20'
      working-directory: './frontend'
    secrets:
      npm-token: ${{ secrets.NPM_TOKEN }}
```

---

## Outputs fran Reusable Workflows

### Definiera Outputs

```yaml
# reusable-build.yml
on:
  workflow_call:
    outputs:
      artifact-name:
        description: 'Name of the build artifact'
        value: ${{ jobs.build.outputs.artifact }}

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      artifact: ${{ steps.upload.outputs.artifact-name }}

    steps:
      - run: npm run build

      - id: upload
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ github.sha }}
          path: dist/
```

### Anvand Outputs

```yaml
jobs:
  build:
    uses: ./.github/workflows/reusable-build.yml

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: ${{ needs.build.outputs.artifact-name }}
```

---

## Composite Actions

### Skapa Composite Action

```yaml
# .github/actions/setup-project/action.yml
name: 'Setup Project'
description: 'Setup Node.js and install dependencies'

inputs:
  node-version:
    description: 'Node.js version'
    required: false
    default: '20'

runs:
  using: 'composite'
  steps:
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
        cache: 'npm'

    - name: Install dependencies
      run: npm ci
      shell: bash

    - name: Verify installation
      run: npm list --depth=0
      shell: bash
```

### Anvand Composite Action

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup project
        uses: ./.github/actions/setup-project
        with:
          node-version: '20'

      - run: npm test
```

---

## Organisation Workflows

### Central Workflow Repository

```
org-workflows/
├── .github/
│   └── workflows/
│       ├── node-ci.yml
│       ├── docker-build.yml
│       ├── security-scan.yml
│       └── deploy-k8s.yml
```

### Anvand fran Annat Repo

```yaml
# I any-repo/.github/workflows/ci.yml
jobs:
  build:
    uses: my-org/org-workflows/.github/workflows/node-ci.yml@main
    with:
      node-version: '20'
    secrets: inherit  # Arv alla secrets
```

---

## Workflow Patterns

### Matrix + Reusable

```yaml
jobs:
  test:
    strategy:
      matrix:
        environment: [staging, production]
    uses: ./.github/workflows/test-env.yml
    with:
      environment: ${{ matrix.environment }}
```

### Conditional Workflows

```yaml
jobs:
  check:
    runs-on: ubuntu-latest
    outputs:
      should-deploy: ${{ steps.check.outputs.deploy }}
    steps:
      - id: check
        run: echo "deploy=${{ github.ref == 'refs/heads/main' }}" >> $GITHUB_OUTPUT

  deploy:
    needs: check
    if: needs.check.outputs.should-deploy == 'true'
    uses: ./.github/workflows/deploy.yml
```

---

## Pro Tips

> **Tip 1:** Anvand `secrets: inherit` nar du vill skicka alla secrets till reusable workflow.

> **Tip 2:** Versionstagga dina reusable workflows (`@v1`, `@v2`) for stabilitet.

> **Tip 3:** Composite actions ar battre for sma, ateranvandbara steg. Reusable workflows for hela pipelines.

---

## Hands-on Task

### Uppgift: Skapa en reusable workflow

1. Skapa `.github/workflows/reusable-ci.yml`:

```yaml
name: Reusable CI

on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: '20'

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

2. Anropa den fran huvudworkflow:

```yaml
name: CI
on: [push, pull_request]

jobs:
  ci:
    uses: ./.github/workflows/reusable-ci.yml
    with:
      node-version: '20'
```

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| Reusable Workflow | Hel workflow som kan anropas |
| Composite Action | Ateranvandbar grupp av steps |
| `workflow_call` | Trigger for reusable workflows |
| `secrets: inherit` | Arv alla secrets automatiskt |
| Organisation Workflows | Central repo for org-gemensamma workflows |

**Nasta steg:** Node 7 - GitHub Actions: Advanced Patterns
''',
}


# =============================================================================
# NODE 7: GITHUB ACTIONS ADVANCED PATTERNS
# =============================================================================

NODE_07_GITHUB_ACTIONS_ADVANCED = {
    "node_id": 7,
    "title": "GitHub Actions: Advanced Patterns",
    "slug": "github-actions-advanced",
    "difficulty": "advanced",
    "estimated_minutes": 70,
    "xp_reward": 90,
    "topics_covered": [
        "concurrency", "dynamic matrices", "self-hosted runners",
        "workflow optimization", "debugging", "security hardening"
    ],
    "content": r'''# GitHub Actions: Advanced Patterns

## Avancerade Tekniker

> "Mastering GitHub Actions means knowing when to use its power - and when not to."

---

## Concurrency Control

### Avbryt Tidigare Runs

```yaml
name: CI

on:
  push:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
  # Om ny push kommer medan CI kors - avbryt gamla!
```

### Koa for Deploys

```yaml
concurrency:
  group: production-deploy
  cancel-in-progress: false
  # Deploys koar - en i taget till produktion!
```

---

## Dynamic Matrix

### Generera Matrix fran Fil

```yaml
jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - uses: actions/checkout@v4
      - id: set-matrix
        run: |
          # Las fran JSON-fil eller generera dynamiskt
          echo "matrix=$(cat .github/matrix.json)" >> $GITHUB_OUTPUT

  build:
    needs: prepare
    strategy:
      matrix: ${{ fromJson(needs.prepare.outputs.matrix) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building ${{ matrix.service }}"
```

### Detect Changed Files

```yaml
jobs:
  changes:
    runs-on: ubuntu-latest
    outputs:
      services: ${{ steps.filter.outputs.changes }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v2
        id: filter
        with:
          filters: |
            frontend:
              - 'frontend/**'
            backend:
              - 'backend/**'
            shared:
              - 'shared/**'

  build:
    needs: changes
    if: ${{ needs.changes.outputs.services != '[]' }}
    strategy:
      matrix:
        service: ${{ fromJson(needs.changes.outputs.services) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building ${{ matrix.service }}"
```

---

## Self-Hosted Runners

### Setup Runner

```bash
# Pa din server:
mkdir actions-runner && cd actions-runner

# Ladda ner
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

tar xzf ./actions-runner-linux-x64.tar.gz

# Konfigurera
./config.sh --url https://github.com/your-org/your-repo \
  --token YOUR_RUNNER_TOKEN

# Starta som service
sudo ./svc.sh install
sudo ./svc.sh start
```

### Anvand Self-Hosted

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, x64]
    # Matchar runners med dessa labels
    steps:
      - uses: actions/checkout@v4
      - run: ./internal-build.sh
```

### Runner i Docker

```yaml
# docker-compose.yml for runner
services:
  runner:
    image: myorg/github-runner:latest
    environment:
      - GITHUB_TOKEN
      - RUNNER_REPOSITORY_URL=https://github.com/org/repo
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

---

## Workflow Optimization

### Parallel Jobs

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [...]

  test-unit:
    runs-on: ubuntu-latest
    steps: [...]

  test-integration:
    runs-on: ubuntu-latest
    steps: [...]

  # Alla kor parallellt!
  build:
    needs: [lint, test-unit, test-integration]
    runs-on: ubuntu-latest
    steps: [...]
```

### Fail Fast

```yaml
strategy:
  fail-fast: true  # Default - stoppa alla om en failar
  # fail-fast: false  # Lat alla fortsatta
```

### Timeout

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30  # Default ar 360 (6 timmar!)
    steps:
      - name: Long running task
        timeout-minutes: 10  # Per-step timeout
        run: ./slow-script.sh
```

---

## Debugging

### Debug Logging

```yaml
# Satt dessa secrets for verbose output:
# ACTIONS_RUNNER_DEBUG: true
# ACTIONS_STEP_DEBUG: true

steps:
  - name: Debug info
    run: |
      echo "Event: ${{ github.event_name }}"
      echo "Ref: ${{ github.ref }}"
      echo "SHA: ${{ github.sha }}"
      cat $GITHUB_EVENT_PATH | jq .
```

### SSH Debug Session

```yaml
- name: Setup tmate session
  if: failure()
  uses: mxschmitt/action-tmate@v3
  with:
    limit-access-to-actor: true
  # SSH in och debugga!
```

---

## Security Hardening

### Minimal Permissions

```yaml
permissions:
  contents: read   # Bara read
  # Alla andra permissions ar disabled
```

### Pin Actions to SHA

```yaml
# INTE:
- uses: actions/checkout@v4
# UTAN:
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
```

### Dependency Review

```yaml
- name: Dependency Review
  uses: actions/dependency-review-action@v3
  with:
    fail-on-severity: high
```

### CODEOWNERS for Workflows

```
# .github/CODEOWNERS
.github/workflows/ @security-team
```

---

## Pro Tips

> **Tip 1:** Anvand `timeout-minutes` pa alla jobs - undvik hangande pipelines.

> **Tip 2:** Pin actions till SHA for produktions-workflows (supply chain security).

> **Tip 3:** Anvand `concurrency` for att undvika race conditions i deploys.

---

## Hands-on Task

### Uppgift: Optimera en pipeline

1. Lagg till concurrency control:
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

2. Lagg till timeouts:
```yaml
timeout-minutes: 15
```

3. Minimal permissions:
```yaml
permissions:
  contents: read
```

4. Parallellisera oberoende jobs

---

## Sammanfattning

| Koncept | Forklaring |
|---------|------------|
| Concurrency | Kontrollera parallella runs |
| Dynamic Matrix | Generera matrix dynamiskt |
| Self-hosted | Egna runners for specialfall |
| Timeout | Begränsa körtid |
| Permission | Minimal access principle |
| Pin to SHA | Sakrare an version tags |

**Nasta steg:** Node 8 - GitLab CI Grunderna
''',
}


# =============================================================================
# EXPORT: BLOCK 1 NODES (1-7)
# =============================================================================

CICD_SKILLSMAP_BLOCK_1 = [
    NODE_01_CICD_FUNDAMENTALS,
    NODE_02_GITHUB_ACTIONS_BASICS,
    NODE_03_GITHUB_ACTIONS_ENV_SECRETS,
    NODE_04_GITHUB_ACTIONS_BUILD_TEST,
    NODE_05_GITHUB_ACTIONS_DEPLOYMENT,
    NODE_06_GITHUB_ACTIONS_REUSABLE,
    NODE_07_GITHUB_ACTIONS_ADVANCED,
]


# =============================================================================
# BLOCK 2: GITLAB CI (Noder 8-11)
# =============================================================================

NODE_08_GITLAB_CI_BASICS = {
    "node_id": 8,
    "title": "GitLab CI Grunderna",
    "slug": "gitlab-ci-basics",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [1],
    "content": '''
# GitLab CI Grunderna

GitLab CI/CD är inbyggt i GitLab och kräver ingen extern setup.

## .gitlab-ci.yml Struktur

```yaml
stages:
  - build
  - test
  - deploy

variables:
  NODE_ENV: production

build-job:
  stage: build
  image: node:18
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

test-job:
  stage: test
  script:
    - npm test
  coverage: '/Coverage: (\\d+)%/'

deploy-job:
  stage: deploy
  script:
    - ./deploy.sh
  only:
    - main
  environment:
    name: production
```

## Viktiga Koncept

| Koncept | Beskrivning |
|---------|-------------|
| stages | Ordning på pipeline-steg |
| image | Docker image för job |
| artifacts | Filer mellan stages |
| only/except | När job körs |
| environment | Deploy-miljö |

**Nästa steg:** Node 9 - GitLab CI Runners
''',
}

NODE_09_GITLAB_CI_RUNNERS = {
    "node_id": 9,
    "title": "GitLab CI Runners",
    "slug": "gitlab-ci-runners",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [8],
    "content": '''
# GitLab CI Runners

Runners exekverar dina CI/CD jobs.

## Runner-typer

```yaml
# Shared runners (GitLab.com)
job:
  tags: []  # Använder shared runners

# Specifik runner
job:
  tags:
    - docker
    - linux

# Self-hosted runner
job:
  tags:
    - self-hosted
    - gpu
```

## Runner Registration

```bash
# Installera runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt install gitlab-runner

# Registrera runner
sudo gitlab-runner register \\
  --url https://gitlab.com/ \\
  --registration-token $TOKEN \\
  --executor docker \\
  --docker-image alpine:latest
```

## Executor-typer

| Executor | Användning |
|----------|-----------|
| shell | Lokalt på runner |
| docker | Container per job |
| kubernetes | K8s pods |
| docker+machine | Auto-scaling |

**Nästa steg:** Node 10 - GitLab CI Advanced
''',
}

NODE_10_GITLAB_CI_ADVANCED = {
    "node_id": 10,
    "title": "GitLab CI Advanced",
    "slug": "gitlab-ci-advanced",
    "estimated_minutes": 65,
    "xp_reward": 160,
    "prerequisites": [9],
    "content": '''
# GitLab CI Advanced Features

## Parent-Child Pipelines

```yaml
# .gitlab-ci.yml
stages:
  - triggers

trigger-backend:
  stage: triggers
  trigger:
    include: backend/.gitlab-ci.yml
    strategy: depend

trigger-frontend:
  stage: triggers
  trigger:
    include: frontend/.gitlab-ci.yml
```

## Dynamic Child Pipelines

```yaml
generate-config:
  stage: build
  script:
    - python generate_pipeline.py > child.yml
  artifacts:
    paths:
      - child.yml

child-pipeline:
  stage: test
  trigger:
    include:
      - artifact: child.yml
        job: generate-config
```

## Rules (Ersätter only/except)

```yaml
job:
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: always
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      when: manual
    - when: never
```

## Cache & Artifacts

```yaml
build:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  artifacts:
    expire_in: 1 week
    paths:
      - dist/
```

**Nästa steg:** Node 11 - GitLab CI Security
''',
}

NODE_11_GITLAB_CI_SECURITY = {
    "node_id": 11,
    "title": "GitLab CI Security",
    "slug": "gitlab-ci-security",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [10],
    "content": '''
# GitLab CI Security Features

## Secret Management

```yaml
deploy:
  script:
    - echo $DB_PASSWORD  # Maskerad i logs
  variables:
    DB_PASSWORD: $DB_PASSWORD  # Från CI/CD Settings
```

## Protected Variables

```yaml
# Endast på protected branches
production-deploy:
  script:
    - deploy --key=$PROD_KEY
  only:
    - main
  variables:
    PROD_KEY: $PROD_KEY  # Protected variable
```

## Security Scanning

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml

sast:
  stage: test

dependency_scanning:
  stage: test
```

## Container Scanning

```yaml
include:
  - template: Security/Container-Scanning.gitlab-ci.yml

container_scanning:
  variables:
    CS_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

| Scan | Hittar |
|------|--------|
| SAST | Kodfel |
| DAST | Runtime-sårbarheter |
| Dependency | Paket-CVE:er |
| Container | Image-sårbarheter |

**Nästa steg:** Node 12 - Jenkins Fundamentals
''',
}

CICD_SKILLSMAP_BLOCK_2 = [
    NODE_08_GITLAB_CI_BASICS,
    NODE_09_GITLAB_CI_RUNNERS,
    NODE_10_GITLAB_CI_ADVANCED,
    NODE_11_GITLAB_CI_SECURITY,
]

# Block 3: Jenkins (Noder 12-15) - kommer härnäst
# Block 4: ArgoCD & GitOps (Noder 16-20) - kommer sist
