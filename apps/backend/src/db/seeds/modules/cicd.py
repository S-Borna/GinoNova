"""
CI/CD Mastery Module
====================

Komplett kurs i Continuous Integration & Continuous Deployment.
Följer Linux-mallen: Svenska, pedagogiskt, kommentarer på varje rad.

20 noder från grundläggande till avancerat.
"""

MODULE = {
    "slug": "cicd-mastery",
    "title": "CI/CD Mastery",
    "description": "Automatisera bygg, test och deployment med moderna CI/CD-pipelines",
    "icon": "git-pull-request",
    "category": "devops",
    "order": 9,
    "tasks": [
        {
            "title": "Introduction to CI/CD",
            "slug": "introduction-to-cicd",
            "difficulty": "beginner",
            "content": '''
# Introduction to CI/CD

## Varför behöver du kunna detta?

Utan CI/CD:

- Manuella deployments som tar timmar
- "Det funkar på min maskin" problem
- Buggar upptäcks sent
- Rädsla för att deploya

Med CI/CD:

- Automatiserade, reproducerbara deployments
- Snabb feedback på kodkvalitet
- Kontinuerligt värde till användare

---

## Så fungerar det

CI/CD är en pipeline:

1. **Continuous Integration (CI)** - automatisk bygg och test vid varje commit
2. **Continuous Delivery (CD)** - kod alltid redo för produktion
3. **Continuous Deployment** - automatisk deploy till produktion

---

## CI/CD Pipeline stages

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Code   │───▶│  Build  │───▶│  Test   │───▶│ Deploy  │───▶│ Monitor │
│ Commit  │    │         │    │         │    │         │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  Git push     Compile        Unit tests    Staging      Alerts
  PR/MR        Lint           Integration   Production   Metrics
               Dependencies   E2E tests     Canary       Logs
```

---

## Populära CI/CD-verktyg

```bash
# Cloud-baserade
GitHub Actions         # Integrerat i GitHub
GitLab CI              # Integrerat i GitLab
CircleCI               # Populärt för open source
Azure DevOps           # Microsoft-ekosystem
AWS CodePipeline       # AWS-native

# Self-hosted
Jenkins                # Mest flexibelt, äldst
TeamCity               # JetBrains
Drone CI               # Container-native
Argo CD                # Kubernetes-native GitOps
```

---

## Första pipelinen (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI Pipeline                      # Pipeline-namn

on:                                    # Triggers
  push:
    branches: [main, develop]          # Vid push till dessa branches
  pull_request:
    branches: [main]                   # Vid PR mot main

jobs:
  build:                               # Job-namn
    runs-on: ubuntu-latest             # Runner OS

    steps:
      - name: Checkout code            # Hämta kod
        uses: actions/checkout@v4

      - name: Setup Node.js            # Installera Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies     # Installera dependencies
        run: npm ci

      - name: Run linter               # Lint-kontroll
        run: npm run lint

      - name: Run tests                # Kör tester
        run: npm test

      - name: Build                    # Bygg applikation
        run: npm run build
```

---

## CI/CD Best Practices

```yaml
# 1. Snabb feedback - kör snabba tester först
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint             # Sekunder, inte minuter

  unit-test:
    needs: lint                        # Kör efter lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  integration-test:
    needs: unit-test                   # Kör efter unit tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run test:integration
```

```bash
# 2. Reproducerbarhet
# Använd lock-filer
npm ci                                 # Inte npm install
pip install -r requirements.txt        # Pinnade versioner
```

---

## Key Takeaways

1. CI/CD automatiserar hela vägen från kod till produktion
2. CI = bygg och test vid varje commit
3. CD = automatisk deployment (delivery eller deployment)
4. Snabb feedback är kritiskt
5. Reproducerbarhet genom lock-filer och pinnade versioner
''',
        },
        {
            "title": "GitHub Actions Fundamentals",
            "slug": "github-actions-fundamentals",
            "difficulty": "beginner",
            "content": '''
# GitHub Actions Fundamentals

## Varför behöver du kunna detta?

GitHub Actions är industristandard:

- Integrerat direkt i GitHub
- Gratis för public repos
- Stort marketplace med färdiga actions
- Matrix builds för multi-platform

---

## Så fungerar det

GitHub Actions komponenter:

1. **Workflow** - YAML-fil som definierar automation
2. **Job** - en uppsättning steg som körs på samma runner
3. **Step** - individuell task (action eller command)
4. **Action** - återanvändbar komponent
5. **Runner** - maskin som kör jobs

---

## Workflow syntax

```yaml
# .github/workflows/main.yml
name: Main Workflow                    # Visas i GitHub UI

on:                                    # Triggers
  push:
    branches:
      - main
      - 'release/*'                    # Wildcard pattern
    paths:
      - 'src/**'                       # Bara om src ändras
      - '!src/**/*.md'                 # Utom markdown

  pull_request:
    types: [opened, synchronize, reopened]

  schedule:
    - cron: '0 0 * * *'                # Dagligen vid midnatt

  workflow_dispatch:                   # Manuell trigger
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

env:                                   # Globala env vars
  NODE_ENV: production
  CI: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

---

## Jobs och dependencies

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    needs: lint                        # Vänta på lint
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  build:
    runs-on: ubuntu-latest
    needs: [lint, test]                # Vänta på båda
    steps:
      - uses: actions/checkout@v4
      - run: npm run build

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'  # Bara på main
    steps:
      - run: echo "Deploying..."
```

---

## Matrix builds

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [18, 20, 22]
        exclude:
          - os: windows-latest
            node: 18
        include:
          - os: ubuntu-latest
            node: 20
            experimental: true

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}

      - run: npm ci
      - run: npm test
        continue-on-error: ${{ matrix.experimental || false }}
```

---

## Secrets och variabler

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production            # GitHub Environment

    steps:
      - name: Deploy to server
        env:
          SSH_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          echo "$SSH_KEY" > key.pem
          chmod 600 key.pem
          ssh -i key.pem user@server "deploy.sh"

      # Repository variable
      - name: Use variable
        run: echo "Deploying to ${{ vars.DEPLOY_URL }}"
```

---

## Caching

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Cache npm dependencies
      - name: Cache npm
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('package-lock.json') }}
          restore-keys: |
            npm-

      # Eller använd setup-node med cache
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'                 # Automatisk cache

      - run: npm ci
      - run: npm run build

      # Cache build output
      - name: Cache build
        uses: actions/cache@v4
        with:
          path: dist
          key: build-${{ github.sha }}
```

---

## Artifacts

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build

      # Ladda upp build-output
      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/
          retention-days: 5

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      # Ladda ner artifact
      - name: Download build artifact
        uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/

      - name: Deploy
        run: |
          ls -la dist/
          # Deploy files...
```

---

## Reusable workflows

```yaml
# .github/workflows/deploy-reusable.yml
name: Reusable Deploy

on:
  workflow_call:                       # Gör workflow anropbar
    inputs:
      environment:
        required: true
        type: string
    secrets:
      deploy_key:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - run: echo "Deploying to ${{ inputs.environment }}"
```

```yaml
# .github/workflows/main.yml - Anropa reusable
jobs:
  deploy-staging:
    uses: ./.github/workflows/deploy-reusable.yml
    with:
      environment: staging
    secrets:
      deploy_key: ${{ secrets.STAGING_KEY }}

  deploy-production:
    needs: deploy-staging
    uses: ./.github/workflows/deploy-reusable.yml
    with:
      environment: production
    secrets:
      deploy_key: ${{ secrets.PRODUCTION_KEY }}
```

---

## Key Takeaways

1. Workflows triggas av events (push, PR, schedule)
2. Jobs körs parallellt om inte `needs` specificeras
3. Matrix builds för multi-platform/version testing
4. Caching sparar tid på dependencies
5. Artifacts delar data mellan jobs
''',
        },
        {
            "title": "GitLab CI/CD",
            "slug": "gitlab-cicd",
            "difficulty": "beginner",
            "content": '''
# GitLab CI/CD

## Varför behöver du kunna detta?

GitLab CI/CD är kraftfullt:

- Integrerat DevSecOps
- Auto DevOps för snabbstart
- Container Registry inbyggt
- Kubernetes integration

Populärt i enterprise-miljöer.

---

## Så fungerar det

GitLab CI/CD components:

1. `.gitlab-ci.yml` i repo-root
2. **Pipeline** - alla jobs för en commit
3. **Stages** - grupperar jobs
4. **Jobs** - individuella tasks
5. **Runners** - kör jobs

---

## Grundläggande pipeline

```yaml
# .gitlab-ci.yml
stages:                                # Definiera stages
  - build
  - test
  - deploy

variables:                             # Globala variabler
  NODE_VERSION: "20"

build:                                 # Job-namn
  stage: build                         # Tillhör build-stage
  image: node:${NODE_VERSION}          # Docker image
  script:
    - npm ci                           # Installera dependencies
    - npm run build                    # Bygg
  artifacts:
    paths:
      - dist/                          # Spara build output
    expire_in: 1 hour

test:
  stage: test
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm test
  coverage: '/Coverage: (\d+\.\d+)%/'  # Parse coverage från output

deploy:
  stage: deploy
  script:
    - echo "Deploying application..."
  only:
    - main                             # Bara på main branch
  environment:
    name: production
    url: https://example.com
```

---

## Jobs och dependencies

```yaml
stages:
  - build
  - test
  - deploy

build-frontend:
  stage: build
  script:
    - cd frontend && npm ci && npm run build
  artifacts:
    paths:
      - frontend/dist/

build-backend:
  stage: build
  script:
    - cd backend && pip install -r requirements.txt

unit-tests:
  stage: test
  needs: []                            # Kör direkt, vänta inte på build
  script:
    - npm test

integration-tests:
  stage: test
  needs:
    - build-frontend
    - build-backend
  script:
    - npm run test:integration

deploy-staging:
  stage: deploy
  needs:
    - integration-tests
  script:
    - deploy_to_staging.sh
  environment:
    name: staging
```

---

## Cache och artifacts

```yaml
# Cache för snabbare builds
build:
  stage: build
  image: node:20
  cache:
    key:
      files:
        - package-lock.json            # Cache key baserat på lockfile
    paths:
      - node_modules/                  # Cacha dependencies
    policy: pull-push                  # Hämta och uppdatera

  script:
    - npm ci
    - npm run build

  artifacts:
    paths:
      - dist/
    expire_in: 1 week
    when: on_success                   # Bara vid success

# Separata cache per branch
test:
  cache:
    key: "$CI_COMMIT_REF_SLUG"         # Branch-namn som key
    paths:
      - node_modules/
    policy: pull                       # Bara hämta, uppdatera inte
```

---

## Environments och deployment

```yaml
deploy-staging:
  stage: deploy
  script:
    - ./deploy.sh staging
  environment:
    name: staging
    url: https://staging.example.com
    on_stop: stop-staging              # Job att köra vid stop

stop-staging:
  stage: deploy
  script:
    - ./teardown.sh staging
  when: manual
  environment:
    name: staging
    action: stop

deploy-production:
  stage: deploy
  script:
    - ./deploy.sh production
  environment:
    name: production
    url: https://example.com
  when: manual                         # Manuell trigger
  only:
    - main
```

---

## Rules och conditions

```yaml
# Moderna rules (ersätter only/except)
build:
  script:
    - npm run build
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: always
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: always
    - if: '$CI_COMMIT_TAG'
      when: always
    - when: never                      # Default: kör inte

test:
  script:
    - npm test
  rules:
    - changes:
        - src/**/*                     # Kör om src ändras
        - tests/**/*
    - if: '$CI_COMMIT_MESSAGE =~ /\[skip tests\]/'
      when: never

deploy:
  script:
    - ./deploy.sh
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
      allow_failure: false
```

---

## Includes och templates

```yaml
# .gitlab-ci.yml
include:
  # Lokal fil
  - local: '/templates/test.yml'

  # Från annat projekt
  - project: 'company/ci-templates'
    ref: main
    file: '/templates/deploy.yml'

  # Remote URL
  - remote: 'https://example.com/ci-template.yml'

# Använd template med extends
.node-template:                        # Template (börjar med .)
  image: node:20
  before_script:
    - npm ci

build:
  extends: .node-template              # Ärv från template
  script:
    - npm run build

test:
  extends: .node-template
  script:
    - npm test
```

---

## Services (sidecars)

```yaml
# Test med database
test:
  stage: test
  image: python:3.11
  services:
    - name: postgres:15
      alias: db                        # Hostname i job
    - name: redis:7
      alias: cache
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: "postgresql://test:test@db:5432/test_db"
    REDIS_URL: "redis://cache:6379"
  script:
    - pip install -r requirements.txt
    - pytest
```

---

## Key Takeaways

1. `.gitlab-ci.yml` i repo-root
2. Stages grupperar jobs
3. `needs` för DAG-baserade dependencies
4. `rules` ersätter only/except
5. `include` för återanvändbara templates
''',
        },
        {
            "title": "Jenkins Pipelines",
            "slug": "jenkins-pipelines",
            "difficulty": "intermediate",
            "content": '''
# Jenkins Pipelines

## Varför behöver du kunna detta?

Jenkins är fortfarande enormt populärt:

- Mest flexibla CI/CD-verktyget
- Tusentals plugins
- Self-hosted kontroll
- Legacy-system integration

Många företag har Jenkins-infrastruktur.

---

## Så fungerar det

Jenkins Pipeline typer:

1. **Declarative Pipeline** - strukturerad YAML-liknande syntax
2. **Scripted Pipeline** - full Groovy-kontroll
3. **Multibranch Pipeline** - automatisk per branch

---

## Declarative Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any                          // Kör på valfri agent

    environment {                      // Environment variables
        NODE_ENV = 'production'
        DEPLOY_ENV = "${params.ENVIRONMENT}"
    }

    parameters {                       // Input-parametrar
        choice(
            name: 'ENVIRONMENT',
            choices: ['staging', 'production'],
            description: 'Deploy target'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: 'Skip test stage'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm           // Hämta kod från SCM
            }
        }

        stage('Build') {
            steps {
                sh 'npm ci'            // Shell-kommando
                sh 'npm run build'
            }
        }

        stage('Test') {
            when {
                expression { !params.SKIP_TESTS }
            }
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results/*.xml'  // Publicera test results
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh './deploy.sh ${DEPLOY_ENV}'
            }
        }
    }

    post {                             // Körs efter alla stages
        success {
            echo 'Pipeline succeeded!'
            slackSend channel: '#deployments', message: 'Deploy OK'
        }
        failure {
            echo 'Pipeline failed!'
            slackSend channel: '#alerts', message: 'Deploy FAILED'
        }
        always {
            cleanWs()                  // Rensa workspace
        }
    }
}
```

---

## Agent options

```groovy
pipeline {
    // Kör på specifik agent
    agent {
        label 'linux && docker'        // Agent med labels
    }

    stages {
        stage('Docker Build') {
            agent {
                docker {
                    image 'node:20'    // Kör i Docker container
                    args '-v /tmp:/tmp'
                }
            }
            steps {
                sh 'npm ci && npm run build'
            }
        }

        stage('Kubernetes') {
            agent {
                kubernetes {
                    yaml \'\'\'
                    apiVersion: v1
                    kind: Pod
                    spec:
                      containers:
                      - name: node
                        image: node:20
                        command: ['sleep', 'infinity']
                    \'\'\'
                }
            }
            steps {
                container('node') {
                    sh 'npm test'
                }
            }
        }
    }
}
```

---

## Parallel execution

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Test') {
            parallel {                 // Kör parallellt
                stage('Unit Tests') {
                    steps {
                        sh 'npm run test:unit'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'npm run test:integration'
                    }
                }
                stage('E2E Tests') {
                    agent {
                        docker { image 'cypress/included:latest' }
                    }
                    steps {
                        sh 'npm run test:e2e'
                    }
                }
            }
        }
    }
}
```

---

## Credentials

```groovy
pipeline {
    agent any

    environment {
        // Hämta credentials
        AWS_CREDS = credentials('aws-credentials')  // username/password
        SSH_KEY = credentials('deploy-ssh-key')     // SSH key
        API_TOKEN = credentials('api-token')        // Secret text
    }

    stages {
        stage('Deploy') {
            steps {
                // AWS credentials sätts som AWS_CREDS_USR och AWS_CREDS_PSW
                sh \'\'\'
                    export AWS_ACCESS_KEY_ID=$AWS_CREDS_USR
                    export AWS_SECRET_ACCESS_KEY=$AWS_CREDS_PSW
                    aws s3 sync dist/ s3://my-bucket/
                \'\'\'

                // SSH key
                sshagent(['deploy-ssh-key']) {
                    sh 'ssh user@server "deploy.sh"'
                }

                // API token
                withCredentials([string(credentialsId: 'api-token', variable: 'TOKEN')]) {
                    sh 'curl -H "Authorization: Bearer $TOKEN" https://api.example.com'
                }
            }
        }
    }
}
```

---

## Shared Libraries

```groovy
// vars/deployApp.groovy (i shared library repo)
def call(Map config = [:]) {
    def environment = config.environment ?: 'staging'
    def version = config.version ?: 'latest'

    echo "Deploying version ${version} to ${environment}"

    sh """
        kubectl set image deployment/app app=${version} -n ${environment}
        kubectl rollout status deployment/app -n ${environment}
    """
}

// vars/notifySlack.groovy
def call(String status, String channel = '#deployments') {
    def color = status == 'SUCCESS' ? 'good' : 'danger'
    slackSend(
        channel: channel,
        color: color,
        message: "${env.JOB_NAME} - ${status}"
    )
}
```

```groovy
// Jenkinsfile - använd shared library
@Library('my-shared-library') _

pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                deployApp(
                    environment: 'production',
                    version: "${env.BUILD_NUMBER}"
                )
            }
        }
    }

    post {
        success { notifySlack('SUCCESS') }
        failure { notifySlack('FAILURE', '#alerts') }
    }
}
```

---

## Multibranch Pipeline

```groovy
// Jenkinsfile - automatiskt för alla branches
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm ci && npm run build'
            }
        }

        stage('Deploy to Dev') {
            when {
                branch 'develop'
            }
            steps {
                sh './deploy.sh dev'
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'release/*'
            }
            steps {
                sh './deploy.sh staging'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?'
                sh './deploy.sh production'
            }
        }
    }
}
```

---

## Key Takeaways

1. Declarative Pipeline för strukturerad syntax
2. `agent` bestämmer var pipeline körs
3. `parallel` för concurrent execution
4. `credentials()` för säker secrets-hantering
5. Shared Libraries för återanvändbar kod
''',
        },
        {
            "title": "Testing in Pipelines",
            "slug": "testing-in-pipelines",
            "difficulty": "intermediate",
            "content": '''
# Testing in Pipelines

## Varför behöver du kunna detta?

Tester är CI/CD:s ryggrad:

- Fånga buggar innan produktion
- Dokumentera förväntad funktion
- Möjliggöra säkra refaktorer
- Bygga förtroende för deployment

Automatiserade tester = trygg kontinuerlig deployment.

---

## Så fungerar det

Test-pyramid:

```
          /\\
         /  \\
        / E2E\\           Få, långsamma, högt värde
       /──────\\
      /Integr- \\         Mellan
     /  ation   \\
    /────────────\\
   /   Unit       \\      Många, snabba, grundläggande
  /________________\\
```

---

## Unit Tests

```yaml
# GitHub Actions - Unit tests
jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Run unit tests
        run: npm test -- --coverage
        env:
          CI: true

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage/lcov.info
          fail_ci_if_error: true

      - name: Check coverage threshold
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "Coverage ${COVERAGE}% is below 80%"
            exit 1
          fi
```

---

## Integration Tests

```yaml
# Integration tests med services
jobs:
  integration-tests:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      redis:
        image: redis:7
        ports:
          - 6379:6379

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - run: npm ci

      - name: Run migrations
        run: npm run db:migrate
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db

      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
```

---

## E2E Tests

```yaml
# E2E med Playwright
jobs:
  e2e-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - run: npm ci

      - name: Install Playwright
        run: npx playwright install --with-deps

      - name: Build application
        run: npm run build

      - name: Run E2E tests
        run: npx playwright test
        env:
          BASE_URL: http://localhost:3000

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30
```

```yaml
# E2E med Cypress
jobs:
  cypress:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Cypress run
        uses: cypress-io/github-action@v6
        with:
          build: npm run build
          start: npm start
          wait-on: 'http://localhost:3000'
          browser: chrome
          record: true
        env:
          CYPRESS_RECORD_KEY: ${{ secrets.CYPRESS_RECORD_KEY }}
```

---

## Test Reports

```yaml
# JUnit test reports
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - run: npm ci

      - name: Run tests with JUnit reporter
        run: npm test -- --reporter=jest-junit
        continue-on-error: true

      - name: Publish Test Report
        uses: mikepenz/action-junit-report@v4
        if: always()
        with:
          report_paths: '**/junit.xml'
          fail_on_failure: true
          require_tests: true

      - name: Test Summary
        uses: test-summary/action@v2
        if: always()
        with:
          paths: '**/junit.xml'
```

---

## Parallel Testing

```yaml
# Parallella tester för snabbhet
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shard: [1, 2, 3, 4]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - run: npm ci

      - name: Run tests (shard ${{ matrix.shard }}/4)
        run: npm test -- --shard=${{ matrix.shard }}/4

  merge-coverage:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Download all coverage
        uses: actions/download-artifact@v4
        with:
          pattern: coverage-*
          merge-multiple: true

      - name: Merge coverage
        run: npx nyc merge coverage/ merged-coverage.json
```

---

## Security Testing

```yaml
# Security scans i pipeline
jobs:
  security:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      # Dependency scanning
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      # Static analysis
      - name: Run CodeQL
        uses: github/codeql-action/analyze@v3

      # Secret scanning
      - name: Scan for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
          head: HEAD

      # Container scanning
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Scan container
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          severity: 'CRITICAL,HIGH'
          exit-code: '1'
```

---

## Flaky Test Handling

```yaml
# Hantera flaky tests
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - run: npm ci

      - name: Run tests with retry
        uses: nick-fields/retry@v3
        with:
          timeout_minutes: 10
          max_attempts: 3
          command: npm test

      # Eller i Jest
      - name: Run tests
        run: npm test -- --bail --retries=2
```

---

## Key Takeaways

1. Unit tests = snabba, många, körs alltid
2. Integration tests behöver services (DB, cache)
3. E2E tests validerar hela flöden
4. Parallella tester med sharding
5. Security scans i varje pipeline
''',
        },
        {
            "title": "Build & Release Strategies",
            "slug": "build-release-strategies",
            "difficulty": "intermediate",
            "content": '''
# Build & Release Strategies

## Varför behöver du kunna detta?

Rätt release-strategi:

- Minimerar downtime
- Möjliggör snabb rollback
- Reducerar risk
- Skalar med teamet

En strategi passar inte alla situationer.

---

## Så fungerar det

Release-strategier:

1. **Big Bang** - allt på en gång
2. **Rolling** - gradvis ersättning
3. **Blue/Green** - parallella miljöer
4. **Canary** - testa på liten grupp
5. **Feature Flags** - runtime-kontroll

---

## Rolling Deployment

```yaml
# Kubernetes rolling update
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1                      # Max extra pods
      maxUnavailable: 0                # Ingen nedtid
  template:
    spec:
      containers:
        - name: app
          image: myapp:v2
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

```yaml
# GitHub Actions - Rolling deploy
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Rolling deploy
        run: |
          kubectl set image deployment/myapp \
            app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp \
            --timeout=300s
```

---

## Blue/Green Deployment

```yaml
# Blue/Green med Kubernetes services
# blue-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
        - name: app
          image: myapp:v1
---
# green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
        - name: app
          image: myapp:v2
---
# service.yaml - Switch mellan blue/green
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    version: green                     # Ändra för att switcha
  ports:
    - port: 80
```

```yaml
# GitHub Actions - Blue/Green
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to inactive environment
        run: |
          # Avgör vilken som är aktiv
          ACTIVE=$(kubectl get svc myapp -o jsonpath='{.spec.selector.version}')
          if [ "$ACTIVE" = "blue" ]; then
            DEPLOY_TO="green"
          else
            DEPLOY_TO="blue"
          fi

          # Deploy nya versionen till inaktiv
          kubectl set image deployment/myapp-$DEPLOY_TO \
            app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp-$DEPLOY_TO

      - name: Run smoke tests
        run: |
          # Testa mot nya deployen direkt
          DEPLOY_TO_IP=$(kubectl get deployment myapp-$DEPLOY_TO -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
          curl -f http://$DEPLOY_TO_IP/health

      - name: Switch traffic
        run: |
          kubectl patch svc myapp -p '{"spec":{"selector":{"version":"'$DEPLOY_TO'"}}}'
```

---

## Canary Deployment

```yaml
# Canary med Argo Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    canary:
      canaryService: myapp-canary
      stableService: myapp-stable
      trafficRouting:
        nginx:
          stableIngress: myapp-ingress
      steps:
        - setWeight: 5                 # 5% till canary
        - pause: { duration: 5m }      # Vänta och observera
        - setWeight: 20                # 20% om OK
        - pause: { duration: 10m }
        - setWeight: 50
        - pause: { duration: 10m }
        - setWeight: 100               # Full rollout
      analysis:
        templates:
          - templateName: success-rate
        startingStep: 1
```

```yaml
# GitHub Actions - Simple canary
jobs:
  canary:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy canary (10%)
        run: |
          kubectl set image deployment/myapp-canary \
            app=myapp:${{ github.sha }}
          kubectl scale deployment/myapp-canary --replicas=1
          kubectl scale deployment/myapp-stable --replicas=9

      - name: Monitor metrics
        run: |
          sleep 300  # 5 minuter
          # Kolla error rate
          ERROR_RATE=$(curl -s prometheus/query?query=error_rate | jq '.data.result[0].value[1]')
          if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
            echo "Error rate too high, rolling back"
            kubectl scale deployment/myapp-canary --replicas=0
            exit 1
          fi

      - name: Full rollout
        run: |
          kubectl set image deployment/myapp-stable \
            app=myapp:${{ github.sha }}
          kubectl scale deployment/myapp-stable --replicas=10
          kubectl scale deployment/myapp-canary --replicas=0
```

---

## Feature Flags

```yaml
# Deploy med feature flags
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy new feature (disabled)
        run: |
          # Deploya kod med feature flag OFF
          curl -X PATCH https://launchdarkly.com/api/v2/flags/new-feature \
            -H "Authorization: ${{ secrets.LD_API_KEY }}" \
            -d '{"environments":{"production":{"on":false}}}'

          # Deploya applikationen
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}

      - name: Enable for internal users
        run: |
          curl -X PATCH https://launchdarkly.com/api/v2/flags/new-feature \
            -H "Authorization: ${{ secrets.LD_API_KEY }}" \
            -d '{"environments":{"production":{"rules":[{"clauses":[{"attribute":"email","op":"endsWith","values":["@company.com"]}]}]}}}'
```

```typescript
// I applikationskoden
import { init } from '@launchdarkly/node-server-sdk';

const client = init(process.env.LD_SDK_KEY);

async function handleRequest(user: User) {
    const showNewFeature = await client.variation(
        'new-feature',
        { key: user.id, email: user.email },
        false  // default
    );

    if (showNewFeature) {
        return newFeatureHandler();
    } else {
        return legacyHandler();
    }
}
```

---

## Semantic Versioning

```yaml
# Automatisk versioning
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get next version
        id: version
        uses: paulhatch/semantic-version@v5
        with:
          tag_prefix: "v"
          major_pattern: "(MAJOR)"
          minor_pattern: "(MINOR)"
          version_format: "${major}.${minor}.${patch}"

      - name: Create release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: v${{ steps.version.outputs.version }}
          generate_release_notes: true

      - name: Build and push
        run: |
          docker build -t myapp:${{ steps.version.outputs.version }} .
          docker push myapp:${{ steps.version.outputs.version }}
```

---

## Key Takeaways

1. Rolling = gradvis, ingen extra infrastruktur
2. Blue/Green = snabb switch, full rollback
3. Canary = testa på liten grupp först
4. Feature flags = runtime-kontroll
5. Välj strategi efter risktolerans
''',
        },
        {
            "title": "GitLab CI Deep Dive",
            "slug": "gitlab-ci-deep-dive",
            "difficulty": "intermediate",
            "content": '''
# GitLab CI Deep Dive

## Varför behöver du kunna detta?

GitLab CI är integrerat:

- All-in-one DevOps-plattform
- Inbyggd container registry
- Kubernetes-integration
- Enterprise-ready

Många organisationer väljer GitLab för simplicitet.

---

## Så fungerar det

GitLab CI-koncept:

1. **Pipeline** - hela CI/CD-flödet
2. **Stage** - grupp av jobs
3. **Job** - enskild uppgift
4. **Runner** - server som kör jobs

---

## Grundläggande Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - build                                # Stadie 1
  - test                                 # Stadie 2
  - deploy                               # Stadie 3

# Globala variabler
variables:
  NODE_VERSION: "20"
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

# Cache för snabbare builds
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# Default för alla jobs
default:
  image: node:${NODE_VERSION}
  before_script:
    - npm ci --cache .npm

# Build job
build:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

# Test job
test:
  stage: test
  script:
    - npm test -- --coverage
  coverage: '/Lines\s*:\s*(\d+\.?\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
      junit: junit.xml

# Deploy job
deploy:
  stage: deploy
  script:
    - npm run deploy
  only:
    - main
  environment:
    name: production
    url: https://myapp.com
```

---

## Services och Databaser

```yaml
# Integration tests med services
integration-test:
  stage: test
  image: node:20
  services:
    - name: postgres:15
      alias: db
      variables:
        POSTGRES_DB: test
        POSTGRES_USER: test
        POSTGRES_PASSWORD: test
    - name: redis:7
      alias: cache
  variables:
    DATABASE_URL: postgresql://test:test@db:5432/test
    REDIS_URL: redis://cache:6379
  script:
    - npm ci
    - npm run db:migrate
    - npm run test:integration
```

---

## Docker Build

```yaml
# Bygg och pusha till GitLab Registry
docker-build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind                     # Docker-in-Docker
  variables:
    DOCKER_TLS_CERTDIR: "/certs"
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE
    # Tagga latest för main
    - |
      if [ "$CI_COMMIT_BRANCH" = "main" ]; then
        docker tag $DOCKER_IMAGE $CI_REGISTRY_IMAGE:latest
        docker push $CI_REGISTRY_IMAGE:latest
      fi

# Alternativ med Kaniko (säkrare, ingen privileged)
docker-build-kaniko:
  stage: build
  image:
    name: gcr.io/kaniko-project/executor:v1.9.0-debug
    entrypoint: [""]
  script:
    - /kaniko/executor
      --context "${CI_PROJECT_DIR}"
      --dockerfile "${CI_PROJECT_DIR}/Dockerfile"
      --destination "${DOCKER_IMAGE}"
      --cache=true
```

---

## Parallel och Matrix

```yaml
# Parallella tester
test:
  stage: test
  parallel: 4                            # 4 parallella jobs
  script:
    - npm test -- --shard=$CI_NODE_INDEX/$CI_NODE_TOTAL

# Matrix builds
test-matrix:
  stage: test
  parallel:
    matrix:
      - NODE: ['18', '20', '21']
        OS: ['alpine', 'slim']
  image: node:${NODE}-${OS}
  script:
    - npm ci
    - npm test
```

---

## Environment och Deploy

```yaml
# Multi-environment deploys
.deploy_template: &deploy_template
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context $KUBE_CONTEXT
    - kubectl set image deployment/myapp app=$DOCKER_IMAGE
    - kubectl rollout status deployment/myapp

deploy-staging:
  <<: *deploy_template
  stage: deploy
  variables:
    KUBE_CONTEXT: staging-cluster
  environment:
    name: staging
    url: https://staging.myapp.com
  only:
    - develop

deploy-production:
  <<: *deploy_template
  stage: deploy
  variables:
    KUBE_CONTEXT: production-cluster
  environment:
    name: production
    url: https://myapp.com
  only:
    - main
  when: manual                           # Manuell trigger
  allow_failure: false

# Rollback
rollback-production:
  stage: deploy
  script:
    - kubectl rollout undo deployment/myapp
  environment:
    name: production
    action: stop
  when: manual
  only:
    - main
```

---

## Review Apps

```yaml
# Dynamiska preview-miljöer
deploy-review:
  stage: deploy
  script:
    - helm upgrade --install myapp-$CI_COMMIT_REF_SLUG ./chart
      --set image.tag=$CI_COMMIT_SHA
      --set ingress.host=$CI_COMMIT_REF_SLUG.review.myapp.com
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    url: https://$CI_COMMIT_REF_SLUG.review.myapp.com
    on_stop: stop-review
    auto_stop_in: 1 week
  only:
    - merge_requests

stop-review:
  stage: deploy
  script:
    - helm uninstall myapp-$CI_COMMIT_REF_SLUG
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    action: stop
  when: manual
  only:
    - merge_requests
```

---

## Rules och Workflow

```yaml
# Avancerade regler
workflow:
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_MERGE_REQUEST_ID
    - if: $CI_COMMIT_TAG

build:
  stage: build
  rules:
    # Kör på main och MRs
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_MERGE_REQUEST_ID
    # Kör om specifika filer ändras
    - changes:
        - src/**/*
        - package.json
    # Kör inte på draft MRs
    - if: $CI_MERGE_REQUEST_TITLE =~ /^Draft:/
      when: never

security-scan:
  stage: test
  rules:
    # Kör alltid på main
    - if: $CI_COMMIT_BRANCH == "main"
    # Kör manuellt på andra branches
    - when: manual
      allow_failure: true
```

---

## Key Takeaways

1. Stages grupperar jobs, körs sekventiellt
2. Services ger databaser och cache
3. Registry integrerat - använd $CI_REGISTRY
4. Review Apps för PR-previews
5. Rules ersätter only/except
''',
        },
        {
            "title": "Azure DevOps Pipelines",
            "slug": "azure-devops-pipelines",
            "difficulty": "intermediate",
            "content": '''
# Azure DevOps Pipelines

## Varför behöver du kunna detta?

Azure DevOps för enterprise:

- Djup Azure-integration
- Komplett DevOps-svit
- Enterprise compliance
- Microsoft support

Dominant i Microsoft-miljöer.

---

## Så fungerar det

Azure Pipelines struktur:

1. **Pipeline** - YAML-fil
2. **Stage** - logisk grupp
3. **Job** - körs på en agent
4. **Step** - enskild task

---

## Grundläggande Pipeline

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
      - develop
  paths:
    include:
      - src/*

pr:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  - name: nodeVersion
    value: '20'
  - group: production-secrets          # Variable group

stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: $(nodeVersion)
            displayName: 'Install Node.js'

          - script: npm ci
            displayName: 'Install dependencies'

          - script: npm run build
            displayName: 'Build application'

          - publish: $(System.DefaultWorkingDirectory)/dist
            artifact: drop
            displayName: 'Publish artifact'

  - stage: Test
    dependsOn: Build
    jobs:
      - job: TestJob
        steps:
          - download: current
            artifact: drop

          - script: npm test
            displayName: 'Run tests'

          - task: PublishTestResults@2
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: '**/junit.xml'
```

---

## Templates och Återanvändning

```yaml
# templates/build-template.yml
parameters:
  - name: projectPath
    type: string
    default: '.'
  - name: nodeVersion
    type: string
    default: '20'

steps:
  - task: NodeTool@0
    inputs:
      versionSpec: ${{ parameters.nodeVersion }}

  - script: |
      cd ${{ parameters.projectPath }}
      npm ci
      npm run build
    displayName: 'Build ${{ parameters.projectPath }}'
```

```yaml
# azure-pipelines.yml - använd template
stages:
  - stage: Build
    jobs:
      - job: BuildFrontend
        steps:
          - template: templates/build-template.yml
            parameters:
              projectPath: 'apps/frontend'
              nodeVersion: '20'

      - job: BuildBackend
        steps:
          - template: templates/build-template.yml
            parameters:
              projectPath: 'apps/backend'
              nodeVersion: '18'
```

---

## Container Jobs

```yaml
# Kör i container
jobs:
  - job: ContainerJob
    pool:
      vmImage: 'ubuntu-latest'
    container: node:20-alpine
    steps:
      - script: node --version
        displayName: 'Check Node version'

  # Flera containers
  - job: IntegrationTest
    pool:
      vmImage: 'ubuntu-latest'
    services:
      postgres:
        image: postgres:15
        ports:
          - 5432:5432
        env:
          POSTGRES_DB: test
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
    steps:
      - script: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
```

---

## Multi-Stage Deploy

```yaml
# Deploy till flera miljöer
stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - script: npm run build
          - publish: dist
            artifact: app

  - stage: DeployDev
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/develop'))
    jobs:
      - deployment: DeployDev
        environment: 'Development'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: app
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'Azure-Connection'
                    appName: 'myapp-dev'
                    package: '$(Pipeline.Workspace)/app'

  - stage: DeployProd
    dependsOn: DeployDev
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProd
        environment: 'Production'
        strategy:
          runOnce:
            preDeploy:
              steps:
                - script: echo "Pre-deploy checks"
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'Azure-Connection'
                    appName: 'myapp-prod'
                    deploymentMethod: 'zipDeploy'
            routeTraffic:
              steps:
                - script: echo "Shifting traffic"
            postRouteTraffic:
              steps:
                - script: npm run smoke-test
            on:
              failure:
                steps:
                  - script: echo "Deployment failed, initiating rollback"
              success:
                steps:
                  - script: echo "Deployment successful"
```

---

## Approvals och Gates

```yaml
# Manuella approvals i YAML
stages:
  - stage: DeployProd
    jobs:
      - deployment: Production
        environment: 'Production'        # Konfigurerat med approvals
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploying to prod"
```

```yaml
# Environment konfiguration (portal)
# Settings -> Pipelines -> Environments -> Production
# Add check:
# - Approvals (require approval from team leads)
# - Business hours (deploy only Mon-Fri 9-17)
# - Exclusive lock (one deployment at a time)
```

---

## Variables och Secrets

```yaml
# Variable groups och Key Vault
variables:
  - group: 'production-variables'        # From Library
  - name: localVar
    value: 'local value'

# Key Vault integration
variables:
  - group: 'keyvault-secrets'            # Linked to Azure Key Vault

steps:
  - script: |
      echo "Using secret: $(DatabasePassword)"
    displayName: 'Use secret'
    env:
      DATABASE_PASSWORD: $(DatabasePassword)

# Runtime secrets
steps:
  - task: AzureKeyVault@2
    inputs:
      azureSubscription: 'Azure-Connection'
      KeyVaultName: 'my-keyvault'
      SecretsFilter: '*'
      RunAsPreJob: true
```

---

## Matrix och Parallel

```yaml
# Matrix builds
jobs:
  - job: Test
    strategy:
      matrix:
        Node18-Ubuntu:
          nodeVersion: '18'
          vmImage: 'ubuntu-latest'
        Node20-Ubuntu:
          nodeVersion: '20'
          vmImage: 'ubuntu-latest'
        Node20-Windows:
          nodeVersion: '20'
          vmImage: 'windows-latest'
      maxParallel: 3
    pool:
      vmImage: $(vmImage)
    steps:
      - task: NodeTool@0
        inputs:
          versionSpec: $(nodeVersion)
      - script: npm test
```

---

## Key Takeaways

1. Stages → Jobs → Steps hierarki
2. Templates för återanvändning
3. Environments för deployment-kontroll
4. Variable groups för secrets
5. Matrix för multi-platform testing
''',
        },
        {
            "title": "Container-based CI/CD",
            "slug": "container-based-cicd",
            "difficulty": "intermediate",
            "content": '''
# Container-based CI/CD

## Varför behöver du kunna detta?

Containers i CI/CD:

- Konsistenta build-miljöer
- Snabbare pipeline-starts
- Reproducerbarhet
- Isolering mellan jobs

"Works on my machine" försvinner.

---

## Så fungerar det

Container-CI flow:

1. **Build** - skapa container image
2. **Test** - testa i container
3. **Scan** - säkerhetsskanning
4. **Push** - till registry
5. **Deploy** - till runtime

---

## Multi-Stage Dockerfile

```dockerfile
# Dockerfile - optimerad för CI/CD
# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && \
    cp -R node_modules prod_modules && \
    npm ci

# Stage 2: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Stage 3: Test
FROM builder AS tester
RUN npm test

# Stage 4: Production
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001
COPY --from=deps /app/prod_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./
USER nextjs
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

---

## Build och Push

```yaml
# GitHub Actions - Container workflow
name: Container CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=sha,prefix=
            type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64
```

---

## Security Scanning

```yaml
# Container security scanning
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build image for scanning
        run: docker build -t myapp:scan .

      # Trivy vulnerability scanner
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:scan
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'

      # Grype scanner
      - name: Scan with Grype
        uses: anchore/scan-action@v3
        with:
          image: myapp:scan
          fail-build: true
          severity-cutoff: high

      # Snyk container scan
      - name: Run Snyk container scan
        uses: snyk/actions/docker@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          image: myapp:scan
          args: --severity-threshold=high
```

---

## Container Testing

```yaml
# Testa containers
jobs:
  test-container:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build test image
        run: docker build --target tester -t myapp:test .

      - name: Run unit tests in container
        run: |
          docker run --rm myapp:test npm test

      - name: Structure test
        uses: docker://ghcr.io/goss-org/goss:latest
        with:
          args: validate --goss-file goss.yaml

      # Container structure test
      - name: Container structure test
        run: |
          docker run --rm \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v $(pwd):/workspace \
            gcr.io/gcp-runtimes/container-structure-test:latest \
            test --image myapp:test --config /workspace/container-structure-test.yaml
```

```yaml
# container-structure-test.yaml
schemaVersion: '2.0.0'
commandTests:
  - name: "node version"
    command: "node"
    args: ["--version"]
    expectedOutput: ["v20.*"]

fileExistenceTests:
  - name: 'App directory'
    path: '/app'
    shouldExist: true
  - name: 'No root files'
    path: '/root/.bash_history'
    shouldExist: false

metadataTest:
  user: 'nextjs'
  exposedPorts: ['3000']
  workdir: '/app'
  entrypoint: []
```

---

## Registry Management

```yaml
# Multi-registry push
jobs:
  push-multiple-registries:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      # Login till alla registries
      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Login to AWS ECR
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push to all registries
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.sha }}
            docker.io/myorg/myapp:${{ github.sha }}
            ${{ secrets.AWS_ACCOUNT }}.dkr.ecr.eu-west-1.amazonaws.com/myapp:${{ github.sha }}
```

---

## Layer Caching

```yaml
# Optimerad caching
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      # GitHub Actions cache
      - name: Build with GHA cache
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      # Registry cache (snabbare för stora teams)
      - name: Build with registry cache
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: myapp:${{ github.sha }}
          cache-from: type=registry,ref=myapp:buildcache
          cache-to: type=registry,ref=myapp:buildcache,mode=max
```

---

## Key Takeaways

1. Multi-stage builds för mindre images
2. Skanna images innan push
3. Container structure tests validerar
4. Cacha layers för snabbare builds
5. Multi-registry för redundans
''',
        },
        {
            "title": "GitOps with ArgoCD",
            "slug": "gitops-argocd",
            "difficulty": "advanced",
            "content": '''
# GitOps with ArgoCD

## Varför behöver du kunna detta?

GitOps-fördelar:

- Git som single source of truth
- Deklarativ infrastruktur
- Automatisk drift-detection
- Audit trail inbyggt

Modern Kubernetes-deployment standard.

---

## Så fungerar det

GitOps-principer:

1. **Declarative** - önskad state i Git
2. **Versioned** - all ändring committas
3. **Automated** - agent synkar till cluster
4. **Auditable** - Git history = audit log

---

## ArgoCD Installation

```bash
# Installera ArgoCD i Kubernetes
kubectl create namespace argocd

# Installera med kubectl
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Eller med Helm
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd \
  --namespace argocd \
  --create-namespace \
  --set server.service.type=LoadBalancer

# Hämta initial admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# Port forward för lokal access
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

---

## Application Definition

```yaml
# argocd/applications/myapp.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default

  source:
    repoURL: https://github.com/myorg/myapp-manifests.git
    targetRevision: main
    path: overlays/production

  destination:
    server: https://kubernetes.default.svc
    namespace: myapp

  syncPolicy:
    automated:
      prune: true                        # Ta bort borttagna resurser
      selfHeal: true                     # Återställ vid drift
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - PruneLast=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

---

## App of Apps Pattern

```yaml
# argocd/root-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    targetRevision: main
    path: argocd/applications
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

```yaml
# argocd/applications/frontend.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: frontend
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/frontend.git
    targetRevision: main
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: frontend
---
# argocd/applications/backend.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: backend
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/backend.git
    targetRevision: main
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: backend
```

---

## Kustomize Integration

```yaml
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: app
          image: myapp:latest
          resources:
            requests:
              memory: "64Mi"
              cpu: "100m"
```

```yaml
# overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
  - ../../base

replicas:
  - name: myapp
    count: 5

images:
  - name: myapp
    newTag: v1.2.3

patches:
  - patch: |-
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/memory
        value: "256Mi"
    target:
      kind: Deployment
      name: myapp
```

```yaml
# ArgoCD Application med Kustomize
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-prod
spec:
  source:
    repoURL: https://github.com/myorg/myapp.git
    path: overlays/production
    # ArgoCD detekterar kustomization.yaml automatiskt
  destination:
    server: https://kubernetes.default.svc
    namespace: production
```

---

## Helm Integration

```yaml
# ArgoCD med Helm chart
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-helm
spec:
  source:
    repoURL: https://charts.myorg.com
    chart: myapp
    targetRevision: 1.2.3
    helm:
      releaseName: myapp
      valueFiles:
        - values-production.yaml
      values: |
        replicaCount: 5
        image:
          tag: v1.2.3
        ingress:
          enabled: true
          hosts:
            - myapp.example.com
      parameters:
        - name: service.type
          value: LoadBalancer
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
```

---

## Image Updater

```yaml
# ArgoCD Image Updater - automatisk image update
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  annotations:
    # Aktivera image updater
    argocd-image-updater.argoproj.io/image-list: myapp=ghcr.io/myorg/myapp
    argocd-image-updater.argoproj.io/myapp.update-strategy: semver
    argocd-image-updater.argoproj.io/myapp.allow-tags: regexp:^v[0-9]+\.[0-9]+\.[0-9]+$
    argocd-image-updater.argoproj.io/write-back-method: git
spec:
  source:
    repoURL: https://github.com/myorg/myapp-config.git
    path: k8s
    targetRevision: main
```

```yaml
# Installation av Image Updater
# argocd-image-updater.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-image-updater-config
  namespace: argocd
data:
  registries.conf: |
    registries:
      - name: GitHub Container Registry
        api_url: https://ghcr.io
        prefix: ghcr.io
        credentials: pullsecret:argocd/ghcr-creds
```

---

## Progressive Delivery

```yaml
# Argo Rollouts integration
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10
        - pause: { duration: 5m }
        - analysis:
            templates:
              - templateName: success-rate
        - setWeight: 50
        - pause: { duration: 10m }
        - analysis:
            templates:
              - templateName: success-rate
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: app
          image: myapp:v2
---
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  metrics:
    - name: success-rate
      interval: 1m
      successCondition: result[0] >= 0.95
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{status=~"2.."}[5m])) /
            sum(rate(http_requests_total[5m]))
```

---

## Key Takeaways

1. Git = single source of truth
2. App of Apps för skalbarhet
3. Kustomize/Helm för miljö-variationer
4. Image Updater automatiserar
5. Rollouts för canary/blue-green
''',
        },
        {
            "title": "Secrets Management",
            "slug": "secrets-management",
            "difficulty": "advanced",
            "content": '''
# Secrets Management

## Varför behöver du kunna detta?

Secrets-läckage är dyrt:

- API-nycklar på GitHub kostar miljoner
- Databasen exponeras
- Kunddata komprometteras
- Compliance-brott

Secrets ska ALDRIG finnas i kod.

---

## Så fungerar det

Secrets-strategier:

1. **Environment Variables** - runtime injection
2. **Secret Managers** - centraliserad lagring
3. **Sealed Secrets** - krypterade i Git
4. **SOPS** - encrypted files

---

## GitHub Actions Secrets

```yaml
# Använda GitHub secrets
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Repository secrets
      - name: Deploy
        run: ./deploy.sh
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}

      # Environment secrets (mer kontroll)
      - name: Deploy to production
        run: ./deploy-prod.sh
        environment: production
        env:
          API_KEY: ${{ secrets.PROD_API_KEY }}
```

```yaml
# OIDC för molnleverantörer (bäst)
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write                    # OIDC token
      contents: read

    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: eu-west-1
          # Ingen hemlig nyckel - OIDC!

      - name: Deploy to AWS
        run: aws s3 sync dist/ s3://my-bucket/
```

---

## HashiCorp Vault

```yaml
# GitHub Actions med Vault
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Import secrets from Vault
        uses: hashicorp/vault-action@v2
        with:
          url: https://vault.mycompany.com
          method: jwt
          role: github-actions
          secrets: |
            secret/data/production/database url | DATABASE_URL ;
            secret/data/production/api key | API_KEY ;
            secret/data/production/aws access_key | AWS_ACCESS_KEY_ID ;
            secret/data/production/aws secret_key | AWS_SECRET_ACCESS_KEY

      - name: Use secrets
        run: |
          echo "Connecting to database..."
          ./deploy.sh
        env:
          DATABASE_URL: ${{ env.DATABASE_URL }}
          API_KEY: ${{ env.API_KEY }}
```

```hcl
# Vault policy för GitHub Actions
path "secret/data/production/*" {
  capabilities = ["read"]
}

path "aws/creds/github-actions" {
  capabilities = ["read"]
}

# JWT auth konfiguration
resource "vault_jwt_auth_backend" "github" {
  path               = "jwt"
  oidc_discovery_url = "https://token.actions.githubusercontent.com"
  bound_issuer       = "https://token.actions.githubusercontent.com"
}

resource "vault_jwt_auth_backend_role" "github_actions" {
  backend        = vault_jwt_auth_backend.github.path
  role_name      = "github-actions"
  token_policies = ["github-actions"]

  bound_claims = {
    repository = "myorg/myrepo"
  }

  user_claim = "actor"
  role_type  = "jwt"
}
```

---

## AWS Secrets Manager

```yaml
# Hämta secrets från AWS
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read

    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: eu-west-1

      - name: Get secrets from AWS Secrets Manager
        uses: aws-actions/aws-secretsmanager-get-secrets@v2
        with:
          secret-ids: |
            PROD_DB,prod/database/credentials
            PROD_API,prod/api/keys
          parse-json-secrets: true

      - name: Use secrets
        run: |
          # Secrets finns nu som env vars
          # PROD_DB_USERNAME, PROD_DB_PASSWORD etc
          ./deploy.sh
```

```yaml
# I Kubernetes med External Secrets
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: database-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: SecretStore
    name: aws-secrets-manager
  target:
    name: database-credentials
  data:
    - secretKey: username
      remoteRef:
        key: prod/database/credentials
        property: username
    - secretKey: password
      remoteRef:
        key: prod/database/credentials
        property: password
```

---

## Sealed Secrets

```bash
# Installera Sealed Secrets controller
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm install sealed-secrets sealed-secrets/sealed-secrets \
  --namespace kube-system

# Installera kubeseal CLI
brew install kubeseal
```

```yaml
# Skapa vanlig secret först
apiVersion: v1
kind: Secret
metadata:
  name: database-credentials
  namespace: myapp
type: Opaque
stringData:
  username: admin
  password: supersecret123
```

```bash
# Kryptera med kubeseal
kubeseal --format yaml < secret.yaml > sealed-secret.yaml

# Resultatet kan committas till Git!
```

```yaml
# sealed-secret.yaml - säker att committa
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: database-credentials
  namespace: myapp
spec:
  encryptedData:
    username: AgBj8h3kf9D...base64...
    password: AgCk9j4lg0E...base64...
  template:
    metadata:
      name: database-credentials
      namespace: myapp
    type: Opaque
```

---

## SOPS

```bash
# Installera SOPS
brew install sops

# Konfigurera med age (enkel)
age-keygen -o key.txt

# Eller med AWS KMS
export SOPS_KMS_ARN="arn:aws:kms:eu-west-1:123456789:key/abc-123"
```

```yaml
# .sops.yaml - konfiguration
creation_rules:
  - path_regex: .*secrets.*\.yaml$
    kms: arn:aws:kms:eu-west-1:123456789:key/abc-123
  - path_regex: .*\.enc\.yaml$
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
```

```yaml
# secrets.yaml - före kryptering
database:
  username: admin
  password: supersecret123
api_key: sk-abc123456
```

```bash
# Kryptera
sops -e secrets.yaml > secrets.enc.yaml

# Dekryptera
sops -d secrets.enc.yaml > secrets.yaml
```

```yaml
# I GitHub Actions
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: eu-west-1

      - name: Install SOPS
        run: |
          curl -LO https://github.com/getsops/sops/releases/download/v3.8.1/sops-v3.8.1.linux.amd64
          sudo mv sops-v3.8.1.linux.amd64 /usr/local/bin/sops
          sudo chmod +x /usr/local/bin/sops

      - name: Decrypt secrets
        run: sops -d secrets.enc.yaml > secrets.yaml

      - name: Deploy with secrets
        run: ./deploy.sh
```

---

## Key Takeaways

1. ALDRIG secrets i kod eller Git
2. OIDC > statiska credentials
3. Vault för enterprise-scale
4. Sealed Secrets för GitOps
5. SOPS för encrypted config files
''',
        },
        {
            "title": "Pipeline Optimization",
            "slug": "pipeline-optimization",
            "difficulty": "advanced",
            "content": '''
# Pipeline Optimization

## Varför behöver du kunna detta?

Långsamma pipelines kostar:

- Utvecklartid i väntan
- Försenade releaser
- Frustration och context-switch
- Högre infrastrukturkostnad

30 min → 5 min = enorm produktivitetsökning.

---

## Så fungerar det

Optimeringsområden:

1. **Parallellism** - kör saker samtidigt
2. **Caching** - återanvänd resultat
3. **Inkrementella builds** - bara ändrat
4. **Rätt runners** - resurser efter behov

---

## Parallel Execution

```yaml
# GitHub Actions - Maximalt parallellt
jobs:
  # Dessa körs parallellt
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint

  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run typecheck

  test-unit:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shard: [1, 2, 3, 4]              # 4 parallella test-runners
    steps:
      - uses: actions/checkout@v4
      - run: npm test -- --shard=${{ matrix.shard }}/4

  test-e2e:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
    steps:
      - uses: actions/checkout@v4
      - run: npx playwright test --project=${{ matrix.browser }}

  # Väntar på alla ovan
  deploy:
    needs: [lint, typecheck, test-unit, test-e2e]
    runs-on: ubuntu-latest
    steps:
      - run: echo "All checks passed, deploying..."
```

---

## Advanced Caching

```yaml
# Multi-layer caching
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Cache node_modules
      - uses: actions/cache@v4
        id: npm-cache
        with:
          path: |
            node_modules
            ~/.npm
          key: npm-${{ hashFiles('package-lock.json') }}
          restore-keys: |
            npm-

      # Cache Next.js build
      - uses: actions/cache@v4
        with:
          path: |
            .next/cache
          key: nextjs-${{ hashFiles('package-lock.json') }}-${{ hashFiles('**/*.ts', '**/*.tsx') }}
          restore-keys: |
            nextjs-${{ hashFiles('package-lock.json') }}-
            nextjs-

      # Cache Turbo
      - uses: actions/cache@v4
        with:
          path: .turbo
          key: turbo-${{ github.sha }}
          restore-keys: |
            turbo-

      - run: npm ci
        if: steps.npm-cache.outputs.cache-hit != 'true'

      - run: npm run build
```

```yaml
# Docker layer caching
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3

      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## Incremental Builds

```yaml
# Bygg bara det som ändrats
jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      frontend: ${{ steps.changes.outputs.frontend }}
      backend: ${{ steps.changes.outputs.backend }}
      infra: ${{ steps.changes.outputs.infra }}
    steps:
      - uses: actions/checkout@v4

      - uses: dorny/paths-filter@v3
        id: changes
        with:
          filters: |
            frontend:
              - 'apps/frontend/**'
              - 'packages/ui/**'
            backend:
              - 'apps/backend/**'
              - 'packages/shared/**'
            infra:
              - 'infra/**'
              - 'terraform/**'

  build-frontend:
    needs: detect-changes
    if: needs.detect-changes.outputs.frontend == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: npm run build:frontend

  build-backend:
    needs: detect-changes
    if: needs.detect-changes.outputs.backend == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: npm run build:backend

  deploy-infra:
    needs: detect-changes
    if: needs.detect-changes.outputs.infra == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: terraform apply -auto-approve
```

---

## Turbo/Nx for Monorepos

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
      "outputs": ["coverage/**"]
    },
    "lint": {
      "outputs": []
    }
  }
}
```

```yaml
# GitHub Actions med Turbo
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0                 # Behövs för att detektera ändringar

      - uses: actions/cache@v4
        with:
          path: .turbo
          key: turbo-${{ github.sha }}
          restore-keys: turbo-

      - run: npm ci

      # Turbo kör bara det som ändrats
      - run: npx turbo run build test lint --filter=[HEAD^1]

      # Eller med remote caching
      - run: npx turbo run build test lint
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: myteam
```

---

## Larger Runners

```yaml
# Större runners för snabbare builds
jobs:
  build:
    runs-on: ubuntu-latest-16-cores     # 16 cores
    # Eller custom: runs-on: [self-hosted, linux, x64, high-memory]

    steps:
      - uses: actions/checkout@v4

      # Utnyttja fler cores
      - run: npm ci --maxsockets=16
      - run: npm run build -- --max-workers=16
      - run: npm test -- --maxWorkers=16
```

```yaml
# Self-hosted runners för specialbehov
jobs:
  build:
    runs-on: [self-hosted, linux, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: nvidia-smi                  # GPU tillgänglig
      - run: python train_model.py
```

---

## Pipeline Metrics

```yaml
# Mät pipeline-performance
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Start timer
        id: timer
        run: echo "start=$(date +%s)" >> $GITHUB_OUTPUT

      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build
      - run: npm test

      - name: Report metrics
        if: always()
        run: |
          END=$(date +%s)
          DURATION=$((END - ${{ steps.timer.outputs.start }}))
          echo "Pipeline duration: ${DURATION}s"

          # Skicka till monitoring
          curl -X POST https://metrics.mycompany.com/pipeline \
            -d "duration=${DURATION}&repo=${{ github.repository }}&workflow=${{ github.workflow }}"
```

---

## Key Takeaways

1. Parallellism = största vinsten
2. Cacha allt som går (node_modules, builds)
3. Inkrementella builds i monorepos
4. Större runners för krävande jobs
5. Mät och iterera
''',
        },
        {
            "title": "Multi-Environment Deployments",
            "slug": "multi-environment-deployments",
            "difficulty": "advanced",
            "content": '''
# Multi-Environment Deployments

## Varför behöver du kunna detta?

Flera miljöer ger:

- Säker testning före produktion
- Isolering av features
- Compliance-krav
- Gradvis utrullning

Dev → Staging → Prod är standard.

---

## Så fungerar det

Miljö-hierarki:

1. **Development** - utvecklartestning
2. **Staging** - prod-like testning
3. **Production** - live-trafik

Varje miljö = egen konfiguration.

---

## GitHub Environments

```yaml
# Multi-environment deploy
name: Deploy

on:
  push:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}
    steps:
      - uses: actions/checkout@v4

      - name: Get version
        id: version
        run: echo "version=${{ github.sha }}" >> $GITHUB_OUTPUT

      - run: npm ci
      - run: npm run build

      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  deploy-dev:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment:
      name: development
      url: https://dev.myapp.com
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build
          path: dist/

      - name: Deploy to dev
        run: ./deploy.sh dev
        env:
          API_URL: ${{ vars.API_URL }}
          API_KEY: ${{ secrets.API_KEY }}

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build

      - name: Deploy to staging
        run: ./deploy.sh staging
        env:
          API_URL: ${{ vars.API_URL }}
          API_KEY: ${{ secrets.API_KEY }}

      - name: Run smoke tests
        run: npm run test:smoke
        env:
          TEST_URL: https://staging.myapp.com

  deploy-production:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build

      - name: Deploy to production
        run: ./deploy.sh production
        env:
          API_URL: ${{ vars.API_URL }}
          API_KEY: ${{ secrets.API_KEY }}
```

---

## Kubernetes Environments

```yaml
# Kustomize per miljö
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: app
          image: myapp:latest
          envFrom:
            - configMapRef:
                name: myapp-config
            - secretRef:
                name: myapp-secrets
```

```yaml
# overlays/development/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: development
resources:
  - ../../base
replicas:
  - name: myapp
    count: 1
configMapGenerator:
  - name: myapp-config
    literals:
      - LOG_LEVEL=debug
      - ENV=development
```

```yaml
# overlays/staging/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: staging
resources:
  - ../../base
replicas:
  - name: myapp
    count: 2
configMapGenerator:
  - name: myapp-config
    literals:
      - LOG_LEVEL=info
      - ENV=staging
```

```yaml
# overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: production
resources:
  - ../../base
replicas:
  - name: myapp
    count: 5
configMapGenerator:
  - name: myapp-config
    literals:
      - LOG_LEVEL=warn
      - ENV=production
patches:
  - patch: |-
      - op: add
        path: /spec/template/spec/containers/0/resources
        value:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
    target:
      kind: Deployment
```

---

## Terraform Workspaces

```hcl
# main.tf
variable "environment" {
  description = "Environment name"
  type        = string
}

locals {
  env_config = {
    development = {
      instance_type = "t3.small"
      min_size      = 1
      max_size      = 2
    }
    staging = {
      instance_type = "t3.medium"
      min_size      = 2
      max_size      = 4
    }
    production = {
      instance_type = "t3.large"
      min_size      = 3
      max_size      = 10
    }
  }

  config = local.env_config[var.environment]
}

resource "aws_instance" "app" {
  instance_type = local.config.instance_type

  tags = {
    Name        = "myapp-${var.environment}"
    Environment = var.environment
  }
}
```

```yaml
# GitHub Actions med Terraform workspaces
jobs:
  deploy:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [development, staging, production]
      max-parallel: 1                    # En i taget
    environment: ${{ matrix.environment }}
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init

      - name: Select workspace
        run: terraform workspace select ${{ matrix.environment }} || terraform workspace new ${{ matrix.environment }}

      - name: Terraform Apply
        run: terraform apply -auto-approve -var="environment=${{ matrix.environment }}"
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

---

## Environment Promotion

```yaml
# Promote mellan miljöer
name: Promote Release

on:
  workflow_dispatch:
    inputs:
      source_env:
        description: 'Source environment'
        required: true
        type: choice
        options:
          - development
          - staging
      target_env:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      version:
        description: 'Version to promote'
        required: true

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate promotion path
        run: |
          if [ "${{ inputs.source_env }}" = "development" ] && [ "${{ inputs.target_env }}" = "production" ]; then
            echo "Cannot promote directly from dev to prod!"
            exit 1
          fi

  promote:
    needs: validate
    runs-on: ubuntu-latest
    environment: ${{ inputs.target_env }}
    steps:
      - uses: actions/checkout@v4

      - name: Get image from source registry
        run: |
          docker pull myregistry.com/${{ inputs.source_env }}/myapp:${{ inputs.version }}
          docker tag myregistry.com/${{ inputs.source_env }}/myapp:${{ inputs.version }} \
                     myregistry.com/${{ inputs.target_env }}/myapp:${{ inputs.version }}
          docker push myregistry.com/${{ inputs.target_env }}/myapp:${{ inputs.version }}

      - name: Deploy to ${{ inputs.target_env }}
        run: |
          kubectl --context=${{ inputs.target_env }} set image deployment/myapp \
            app=myregistry.com/${{ inputs.target_env }}/myapp:${{ inputs.version }}
```

---

## Environment Variables

```yaml
# Centraliserad env-hantering
# .github/workflows/deploy.yml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
    steps:
      - uses: actions/checkout@v4

      # Environment-specifika vars från GitHub
      - name: Setup environment
        run: |
          echo "Deploying to: ${{ vars.ENVIRONMENT_NAME }}"
          echo "API URL: ${{ vars.API_URL }}"
          echo "Region: ${{ vars.AWS_REGION }}"

      - name: Deploy
        run: ./deploy.sh
        env:
          # Vars (ej hemliga)
          ENV: ${{ vars.ENVIRONMENT_NAME }}
          API_URL: ${{ vars.API_URL }}
          AWS_REGION: ${{ vars.AWS_REGION }}
          # Secrets (hemliga)
          API_KEY: ${{ secrets.API_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

---

## Key Takeaways

1. Dev → Staging → Prod = standard flow
2. GitHub Environments för approvals
3. Kustomize för K8s per-miljö config
4. Terraform workspaces för infra
5. Promotion workflows för kontrollerade releaser
''',
        },
        {
            "title": "Monitoring CI/CD Pipelines",
            "slug": "monitoring-cicd-pipelines",
            "difficulty": "advanced",
            "content": '''
# Monitoring CI/CD Pipelines

## Varför behöver du kunna detta?

Pipeline-övervakning visar:

- Build success rate
- Deploy frequency
- Lead time för changes
- Mean time to recovery

DORA-metrics mäter engineering excellence.

---

## Så fungerar det

Vad att mäta:

1. **Deployment Frequency** - hur ofta
2. **Lead Time** - commit → prod
3. **Change Failure Rate** - misslyckade deploys
4. **MTTR** - tid att återställa

---

## DORA Metrics

```yaml
# GitHub Actions - DORA metrics
name: DORA Metrics

on:
  workflow_run:
    workflows: ["Deploy"]
    types: [completed]

jobs:
  collect-metrics:
    runs-on: ubuntu-latest
    steps:
      - name: Calculate Lead Time
        id: lead-time
        run: |
          # Hämta commit timestamp
          COMMIT_TIME=$(git log -1 --format=%ct ${{ github.sha }})
          DEPLOY_TIME=$(date +%s)
          LEAD_TIME=$((DEPLOY_TIME - COMMIT_TIME))
          echo "lead_time=${LEAD_TIME}" >> $GITHUB_OUTPUT

      - name: Determine Success
        id: success
        run: |
          if [ "${{ github.event.workflow_run.conclusion }}" = "success" ]; then
            echo "success=1" >> $GITHUB_OUTPUT
          else
            echo "success=0" >> $GITHUB_OUTPUT
          fi

      - name: Send to Datadog
        run: |
          curl -X POST "https://api.datadoghq.com/api/v1/series" \
            -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "series": [
                {
                  "metric": "cicd.deployment.lead_time",
                  "points": [['"$(date +%s)"', '"${{ steps.lead-time.outputs.lead_time }}"']],
                  "tags": ["repo:${{ github.repository }}", "env:production"]
                },
                {
                  "metric": "cicd.deployment.success",
                  "points": [['"$(date +%s)"', '"${{ steps.success.outputs.success }}"']],
                  "tags": ["repo:${{ github.repository }}", "env:production"]
                }
              ]
            }'
```

---

## Build Notifications

```yaml
# Slack notifications
jobs:
  notify:
    runs-on: ubuntu-latest
    if: always()
    needs: [build, test, deploy]
    steps:
      - name: Slack Notification
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          fields: repo,message,commit,author,action,eventName,ref,workflow
          mention: 'here'
          if_mention: failure
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}

      # Eller med custom message
      - name: Custom Slack message
        if: failure()
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H 'Content-Type: application/json' \
            -d '{
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "🚨 Pipeline Failed"
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {"type": "mrkdwn", "text": "*Repository:*\n${{ github.repository }}"},
                    {"type": "mrkdwn", "text": "*Branch:*\n${{ github.ref_name }}"},
                    {"type": "mrkdwn", "text": "*Author:*\n${{ github.actor }}"},
                    {"type": "mrkdwn", "text": "*Commit:*\n${{ github.sha }}"}
                  ]
                },
                {
                  "type": "actions",
                  "elements": [
                    {
                      "type": "button",
                      "text": {"type": "plain_text", "text": "View Run"},
                      "url": "${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"
                    }
                  ]
                }
              ]
            }'
```

---

## Pipeline Dashboards

```yaml
# Prometheus metrics endpoint
jobs:
  export-metrics:
    runs-on: ubuntu-latest
    steps:
      - name: Push metrics to Prometheus Pushgateway
        run: |
          cat <<EOF | curl --data-binary @- http://pushgateway.monitoring:9091/metrics/job/github_actions/instance/${{ github.repository }}
          # HELP github_actions_workflow_duration_seconds Duration of workflow runs
          # TYPE github_actions_workflow_duration_seconds gauge
          github_actions_workflow_duration_seconds{workflow="${{ github.workflow }}"} ${{ github.event.workflow_run.run_duration }}

          # HELP github_actions_workflow_success Success status of workflow
          # TYPE github_actions_workflow_success gauge
          github_actions_workflow_success{workflow="${{ github.workflow }}"} ${{ github.event.workflow_run.conclusion == 'success' && '1' || '0' }}
          EOF
```

```yaml
# Grafana dashboard query examples
# PromQL för DORA metrics:

# Deployment Frequency (per dag)
sum(increase(github_actions_workflow_success{workflow="Deploy"}[24h]))

# Change Failure Rate
1 - (
  sum(github_actions_workflow_success{workflow="Deploy"}) /
  sum(count_over_time(github_actions_workflow_success{workflow="Deploy"}[30d]))
)

# Lead Time (genomsnitt senaste veckan)
avg_over_time(cicd_deployment_lead_time[7d])
```

---

## Alerting

```yaml
# PagerDuty integration
jobs:
  alert:
    runs-on: ubuntu-latest
    if: failure()
    steps:
      - name: Alert PagerDuty
        run: |
          curl -X POST https://events.pagerduty.com/v2/enqueue \
            -H 'Content-Type: application/json' \
            -d '{
              "routing_key": "${{ secrets.PAGERDUTY_KEY }}",
              "event_action": "trigger",
              "dedup_key": "github-${{ github.repository }}-${{ github.run_id }}",
              "payload": {
                "summary": "Pipeline failed: ${{ github.workflow }}",
                "source": "${{ github.repository }}",
                "severity": "error",
                "custom_details": {
                  "run_url": "${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}",
                  "commit": "${{ github.sha }}",
                  "author": "${{ github.actor }}"
                }
              }
            }'
```

```yaml
# Auto-resolve vid success
jobs:
  resolve-alert:
    runs-on: ubuntu-latest
    if: success()
    steps:
      - name: Resolve PagerDuty
        run: |
          curl -X POST https://events.pagerduty.com/v2/enqueue \
            -H 'Content-Type: application/json' \
            -d '{
              "routing_key": "${{ secrets.PAGERDUTY_KEY }}",
              "event_action": "resolve",
              "dedup_key": "github-${{ github.repository }}-${{ github.run_id }}"
            }'
```

---

## GitHub Actions Insights

```yaml
# Spara workflow metrics
jobs:
  save-metrics:
    runs-on: ubuntu-latest
    steps:
      - name: Get workflow timing
        id: timing
        uses: actions/github-script@v7
        with:
          script: |
            const run = await github.rest.actions.getWorkflowRun({
              owner: context.repo.owner,
              repo: context.repo.repo,
              run_id: context.runId
            });

            const jobs = await github.rest.actions.listJobsForWorkflowRun({
              owner: context.repo.owner,
              repo: context.repo.repo,
              run_id: context.runId
            });

            const metrics = {
              total_duration: run.data.run_duration,
              jobs: jobs.data.jobs.map(j => ({
                name: j.name,
                duration: (new Date(j.completed_at) - new Date(j.started_at)) / 1000,
                conclusion: j.conclusion
              }))
            };

            console.log(JSON.stringify(metrics, null, 2));
            return metrics;

      - name: Store in database
        run: |
          curl -X POST https://api.mycompany.com/metrics/pipeline \
            -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" \
            -d '${{ steps.timing.outputs.result }}'
```

---

## Key Takeaways

1. DORA metrics = engineering excellence KPIs
2. Slack/Teams för realtids-notifieringar
3. Prometheus/Grafana för dashboards
4. PagerDuty för on-call alerting
5. Spara historik för trend-analys
''',
        },
        {
            "title": "Compliance and Audit",
            "slug": "compliance-audit",
            "difficulty": "advanced",
            "content": '''
# Compliance and Audit

## Varför behöver du kunna detta?

Compliance-krav:

- SOC 2, ISO 27001
- PCI DSS för betalningar
- HIPAA för healthcare
- GDPR för EU-data

Audit trail = bevis på processer.

---

## Så fungerar det

Compliance i CI/CD:

1. **Access Control** - vem får deploya
2. **Audit Trail** - vad hände när
3. **Approvals** - manuella godkännanden
4. **Scanning** - säkerhet och licenser

---

## Branch Protection

```yaml
# GitHub branch protection via API
# Automatisera setup med Terraform
resource "github_branch_protection" "main" {
  repository_id = github_repository.myrepo.node_id
  pattern       = "main"

  # Kräv PR reviews
  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 2
    require_last_push_approval      = true
  }

  # Kräv status checks
  required_status_checks {
    strict = true
    contexts = [
      "build",
      "test",
      "security-scan",
      "compliance-check"
    ]
  }

  # Förhindra force push
  allows_force_pushes = false
  allows_deletions    = false

  # Kräv signerade commits
  require_signed_commits = true

  # Admins följer också reglerna
  enforce_admins = true
}
```

---

## Approval Workflows

```yaml
# Multi-level approvals
name: Production Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build

  security-review:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: security-review              # Kräver security team approval
    steps:
      - name: Security scan results
        run: echo "Security scan passed"

  compliance-review:
    needs: security-review
    runs-on: ubuntu-latest
    environment:
      name: compliance-review            # Kräver compliance team approval
    steps:
      - name: Compliance check
        run: echo "Compliance requirements met"

  deploy:
    needs: compliance-review
    runs-on: ubuntu-latest
    environment:
      name: production                   # Kräver final approval
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

---

## Audit Logging

```yaml
# Logga alla deployment-händelser
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Create audit record - START
        id: audit-start
        run: |
          AUDIT_ID=$(uuidgen)
          echo "audit_id=${AUDIT_ID}" >> $GITHUB_OUTPUT

          curl -X POST https://audit.mycompany.com/events \
            -H "Authorization: Bearer ${{ secrets.AUDIT_TOKEN }}" \
            -d '{
              "id": "'${AUDIT_ID}'",
              "event": "deployment.started",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "actor": "${{ github.actor }}",
              "repository": "${{ github.repository }}",
              "commit": "${{ github.sha }}",
              "workflow": "${{ github.workflow }}",
              "run_id": "${{ github.run_id }}",
              "environment": "production",
              "approvers": "${{ github.event.inputs.approvers }}"
            }'

      - name: Deploy
        id: deploy
        run: ./deploy.sh

      - name: Create audit record - COMPLETE
        if: always()
        run: |
          curl -X POST https://audit.mycompany.com/events \
            -H "Authorization: Bearer ${{ secrets.AUDIT_TOKEN }}" \
            -d '{
              "id": "'${{ steps.audit-start.outputs.audit_id }}'",
              "event": "deployment.completed",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "status": "${{ steps.deploy.outcome }}",
              "duration_seconds": "${{ github.event.workflow_run.run_duration }}"
            }'
```

---

## License Compliance

```yaml
# Scanna dependencies för licenser
jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install license checker
        run: npm install -g license-checker

      - name: Check licenses
        run: |
          license-checker --production --json > licenses.json

          # Kolla efter förbjudna licenser
          FORBIDDEN=$(jq -r 'to_entries[] | select(.value.licenses | test("GPL|AGPL|SSPL")) | .key' licenses.json)

          if [ -n "$FORBIDDEN" ]; then
            echo "❌ Forbidden licenses found:"
            echo "$FORBIDDEN"
            exit 1
          fi

      - name: FOSSA scan
        uses: fossas/fossa-action@main
        with:
          api-key: ${{ secrets.FOSSA_API_KEY }}

      - name: Upload SBOM
        run: |
          npm sbom --sbom-format cyclonedx > sbom.json
          curl -X POST https://sbom.mycompany.com/upload \
            -F "file=@sbom.json" \
            -F "repo=${{ github.repository }}" \
            -F "version=${{ github.sha }}"
```

---

## Change Management

```yaml
# Koppla till change management system
jobs:
  create-change-request:
    runs-on: ubuntu-latest
    outputs:
      change_id: ${{ steps.create.outputs.change_id }}
    steps:
      - name: Create ServiceNow change request
        id: create
        run: |
          RESPONSE=$(curl -X POST https://mycompany.service-now.com/api/now/table/change_request \
            -u "${{ secrets.SNOW_USER }}:${{ secrets.SNOW_PASS }}" \
            -H "Content-Type: application/json" \
            -d '{
              "short_description": "Deploy ${{ github.repository }} to production",
              "description": "Automated deployment from GitHub Actions\nCommit: ${{ github.sha }}\nAuthor: ${{ github.actor }}",
              "type": "standard",
              "risk": "low",
              "impact": "3"
            }')

          CHANGE_ID=$(echo $RESPONSE | jq -r '.result.number')
          echo "change_id=${CHANGE_ID}" >> $GITHUB_OUTPUT

  deploy:
    needs: create-change-request
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy with change ID
        run: |
          echo "Deploying with change request: ${{ needs.create-change-request.outputs.change_id }}"
          ./deploy.sh

  close-change-request:
    needs: [create-change-request, deploy]
    if: always()
    runs-on: ubuntu-latest
    steps:
      - name: Update change request
        run: |
          STATUS=${{ needs.deploy.result == 'success' && 'successful' || 'unsuccessful' }}

          curl -X PATCH "https://mycompany.service-now.com/api/now/table/change_request/${{ needs.create-change-request.outputs.change_id }}" \
            -u "${{ secrets.SNOW_USER }}:${{ secrets.SNOW_PASS }}" \
            -H "Content-Type: application/json" \
            -d '{
              "state": "closed",
              "close_code": "'${STATUS}'",
              "close_notes": "Deployment completed via GitHub Actions"
            }'
```

---

## Evidence Collection

```yaml
# Samla bevis för audit
jobs:
  collect-evidence:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate evidence package
        run: |
          mkdir -p evidence

          # Git info
          git log --oneline -20 > evidence/recent_commits.txt
          git show --stat > evidence/change_details.txt

          # Test results
          npm test -- --json > evidence/test_results.json || true

          # Security scans
          npm audit --json > evidence/npm_audit.json || true

          # Build info
          cat <<EOF > evidence/build_info.json
          {
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "commit": "${{ github.sha }}",
            "branch": "${{ github.ref_name }}",
            "actor": "${{ github.actor }}",
            "run_id": "${{ github.run_id }}",
            "workflow": "${{ github.workflow }}"
          }
          EOF

      - name: Sign evidence
        run: |
          # Skapa hash av all evidence
          find evidence -type f -exec sha256sum {} \; > evidence/checksums.txt

          # Signera med GPG (om konfigurerat)
          # gpg --sign evidence/checksums.txt

      - name: Upload evidence
        uses: actions/upload-artifact@v4
        with:
          name: audit-evidence-${{ github.sha }}
          path: evidence/
          retention-days: 2555              # 7 år för compliance
```

---

## Key Takeaways

1. Branch protection = första försvarslinjen
2. Multi-level approvals för känsliga deploys
3. Audit logging för alla händelser
4. License scanning för compliance
5. Evidence collection för audits
''',
        },
        {
            "title": "Disaster Recovery",
            "slug": "disaster-recovery",
            "difficulty": "advanced",
            "content": '''
# Disaster Recovery

## Varför behöver du kunna detta?

Disaster recovery för CI/CD:

- Pipeline-infrastruktur kan gå ner
- Secrets kan komprometteras
- Deploys kan misslyckas kritiskt
- Snabb recovery = mindre påverkan

RTO och RPO styr strategin.

---

## Så fungerar det

DR-koncept:

1. **RTO** - Recovery Time Objective
2. **RPO** - Recovery Point Objective
3. **Backup** - säkerhetskopiering
4. **Rollback** - återställ tidigare version

---

## Rollback Strategies

```yaml
# Kubernetes rollback
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy new version
        id: deploy
        run: |
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp --timeout=300s

      - name: Rollback on failure
        if: failure() && steps.deploy.outcome == 'failure'
        run: |
          echo "Deployment failed, rolling back..."
          kubectl rollout undo deployment/myapp
          kubectl rollout status deployment/myapp

          # Notifiera
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"⚠️ Deployment rolled back for myapp"}'
```

```yaml
# Database migration rollback
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Backup database
        id: backup
        run: |
          BACKUP_NAME="pre-deploy-$(date +%Y%m%d-%H%M%S)"
          pg_dump $DATABASE_URL > backup/${BACKUP_NAME}.sql
          echo "backup_name=${BACKUP_NAME}" >> $GITHUB_OUTPUT
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}

      - name: Run migrations
        id: migrate
        run: npm run db:migrate

      - name: Deploy application
        id: deploy
        run: ./deploy.sh

      - name: Rollback on failure
        if: failure()
        run: |
          # Rollback migrations
          npm run db:migrate:rollback

          # Om det inte fungerar, återställ från backup
          if [ $? -ne 0 ]; then
            psql $DATABASE_URL < backup/${{ steps.backup.outputs.backup_name }}.sql
          fi

          # Rollback app
          kubectl rollout undo deployment/myapp
```

---

## Blue/Green DR

```yaml
# Blue/Green med snabb failover
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Get current active
        id: current
        run: |
          ACTIVE=$(kubectl get svc myapp -o jsonpath='{.spec.selector.version}')
          echo "active=${ACTIVE}" >> $GITHUB_OUTPUT
          echo "target=$([ $ACTIVE = 'blue' ] && echo 'green' || echo 'blue')" >> $GITHUB_OUTPUT

      - name: Deploy to inactive
        run: |
          kubectl set image deployment/myapp-${{ steps.current.outputs.target }} \
            app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp-${{ steps.current.outputs.target }}

      - name: Health check new deployment
        id: health
        run: |
          TARGET_IP=$(kubectl get deployment myapp-${{ steps.current.outputs.target }} -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

          for i in {1..10}; do
            if curl -sf http://${TARGET_IP}/health; then
              echo "Health check passed"
              exit 0
            fi
            sleep 5
          done
          exit 1

      - name: Switch traffic
        if: success()
        run: |
          kubectl patch svc myapp -p '{"spec":{"selector":{"version":"${{ steps.current.outputs.target }}"}}}'
          echo "Traffic switched to ${{ steps.current.outputs.target }}"

      - name: Keep old version ready
        run: |
          echo "Old version (${{ steps.current.outputs.active }}) kept running for fast rollback"
          echo "To rollback: kubectl patch svc myapp -p '{\"spec\":{\"selector\":{\"version\":\"${{ steps.current.outputs.active }}\"}}}'
```

---

## Backup CI/CD Configuration

```yaml
# Backup GitHub Actions workflows och secrets
name: Backup CI/CD Config

on:
  schedule:
    - cron: '0 0 * * *'                  # Dagligen

jobs:
  backup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Backup workflows
        run: |
          mkdir -p backup/workflows
          cp -r .github/workflows backup/workflows/

          # Metadata
          cat <<EOF > backup/metadata.json
          {
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "repository": "${{ github.repository }}",
            "commit": "${{ github.sha }}"
          }
          EOF

      - name: Backup environment config
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');

            // Lista environments
            const envs = await github.rest.repos.getAllEnvironments({
              owner: context.repo.owner,
              repo: context.repo.repo
            });

            fs.writeFileSync('backup/environments.json', JSON.stringify(envs.data, null, 2));

      - name: Upload to S3
        run: |
          aws s3 cp backup/ s3://cicd-backups/${{ github.repository }}/$(date +%Y-%m-%d)/ --recursive
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.BACKUP_AWS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.BACKUP_AWS_SECRET }}
```

---

## Multi-Region Deployment

```yaml
# Deploy till flera regioner för redundans
jobs:
  deploy:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        region: [eu-west-1, us-east-1, ap-southeast-1]
      fail-fast: false                   # Fortsätt även om en region misslyckas
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS region
        run: |
          aws configure set region ${{ matrix.region }}

      - name: Deploy to ${{ matrix.region }}
        run: |
          # Kubernetes context per region
          kubectl config use-context ${{ matrix.region }}
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp

      - name: Update Route53 health check
        run: |
          aws route53 update-health-check \
            --health-check-id ${{ secrets[format('HEALTH_CHECK_{0}', matrix.region)] }} \
            --resource-path "/health"
```

---

## Incident Response

```yaml
# Automatisk incident response
name: Incident Response

on:
  workflow_dispatch:
    inputs:
      action:
        description: 'Emergency action'
        required: true
        type: choice
        options:
          - rollback-last
          - rollback-version
          - scale-down
          - enable-maintenance
      version:
        description: 'Version to rollback to (if rollback-version)'
        required: false

jobs:
  emergency-action:
    runs-on: ubuntu-latest
    environment: emergency               # Snabb approval
    steps:
      - name: Log incident start
        run: |
          curl -X POST https://incidents.mycompany.com/api/incidents \
            -H "Authorization: Bearer ${{ secrets.INCIDENT_TOKEN }}" \
            -d '{
              "action": "${{ inputs.action }}",
              "triggered_by": "${{ github.actor }}",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
            }'

      - name: Rollback to last version
        if: inputs.action == 'rollback-last'
        run: kubectl rollout undo deployment/myapp

      - name: Rollback to specific version
        if: inputs.action == 'rollback-version'
        run: |
          kubectl set image deployment/myapp app=myapp:${{ inputs.version }}

      - name: Scale down
        if: inputs.action == 'scale-down'
        run: kubectl scale deployment/myapp --replicas=0

      - name: Enable maintenance mode
        if: inputs.action == 'enable-maintenance'
        run: |
          kubectl apply -f k8s/maintenance-page.yaml
          kubectl patch ingress myapp -p '{"spec":{"rules":[{"host":"myapp.com","http":{"paths":[{"path":"/","pathType":"Prefix","backend":{"service":{"name":"maintenance","port":{"number":80}}}}]}}]}}'

      - name: Notify team
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{
              "text":"🚨 Emergency action executed: ${{ inputs.action }} by ${{ github.actor }}"
            }'
```

---

## Key Takeaways

1. Alltid ha rollback-strategi
2. Blue/Green för snabb failover
3. Backup CI/CD config regelbundet
4. Multi-region för hög tillgänglighet
5. Incident response workflows förbereds
''',
        },
        {
            "title": "CircleCI and Other Platforms",
            "slug": "circleci-other-platforms",
            "difficulty": "intermediate",
            "content": '''
# CircleCI and Other Platforms

## Varför behöver du kunna detta?

Olika plattformar för olika behov:

- CircleCI = snabbhet och Docker-fokus
- Travis CI = open source-vänlig
- Bitbucket Pipelines = Atlassian-ekosystem
- Buildkite = self-hosted power

Kunskap överförs mellan plattformar.

---

## Så fungerar det

Gemensamma koncept:

1. **Pipeline Definition** - YAML-fil
2. **Jobs** - körbar enhet
3. **Workflows** - orkestrering
4. **Artifacts** - output-filer

---

## CircleCI Basics

```yaml
# .circleci/config.yml
version: 2.1

orbs:
  node: circleci/node@5.2
  aws-cli: circleci/aws-cli@4.1

executors:
  node-executor:
    docker:
      - image: cimg/node:20.10
    working_directory: ~/project

jobs:
  build:
    executor: node-executor
    steps:
      - checkout
      - node/install-packages:
          pkg-manager: npm
      - run:
          name: Build application
          command: npm run build
      - persist_to_workspace:
          root: .
          paths:
            - dist
            - node_modules

  test:
    executor: node-executor
    parallelism: 4                       # 4 parallella containers
    steps:
      - checkout
      - attach_workspace:
          at: .
      - run:
          name: Run tests
          command: |
            TESTS=$(circleci tests glob "**/*.test.ts" | circleci tests split)
            npm test -- $TESTS
      - store_test_results:
          path: test-results

  deploy:
    executor: node-executor
    steps:
      - checkout
      - attach_workspace:
          at: .
      - aws-cli/setup
      - run:
          name: Deploy to AWS
          command: |
            aws s3 sync dist/ s3://my-bucket/
            aws cloudfront create-invalidation --distribution-id $CF_DIST_ID --paths "/*"

workflows:
  build-test-deploy:
    jobs:
      - build
      - test:
          requires:
            - build
      - deploy:
          requires:
            - test
          filters:
            branches:
              only: main
```

---

## CircleCI Advanced

```yaml
# Avancerad CircleCI config
version: 2.1

orbs:
  docker: circleci/docker@2.4

commands:
  setup-env:
    description: "Setup environment"
    steps:
      - checkout
      - restore_cache:
          keys:
            - deps-{{ checksum "package-lock.json" }}
      - run: npm ci
      - save_cache:
          key: deps-{{ checksum "package-lock.json" }}
          paths:
            - node_modules

jobs:
  build-docker:
    machine:
      image: ubuntu-2204:current
    steps:
      - checkout
      - docker/build:
          image: myapp
          tag: $CIRCLE_SHA1
      - docker/push:
          image: myapp
          tag: $CIRCLE_SHA1
          registry: $DOCKER_REGISTRY

  deploy-staging:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: Deploy to staging
          command: ./deploy.sh staging

  deploy-production:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: Deploy to production
          command: ./deploy.sh production

workflows:
  main:
    jobs:
      - build-docker:
          context: docker-credentials
      - deploy-staging:
          requires:
            - build-docker
          filters:
            branches:
              only: develop
      - hold-for-approval:
          type: approval
          requires:
            - build-docker
          filters:
            branches:
              only: main
      - deploy-production:
          requires:
            - hold-for-approval
          context: production-credentials
```

---

## Travis CI

```yaml
# .travis.yml
language: node_js
node_js:
  - "20"
  - "18"

cache:
  npm: true
  directories:
    - node_modules

branches:
  only:
    - main
    - develop

stages:
  - name: test
  - name: build
  - name: deploy
    if: branch = main

jobs:
  include:
    - stage: test
      name: "Unit Tests"
      script: npm test

    - stage: test
      name: "Lint"
      script: npm run lint

    - stage: build
      name: "Build"
      script: npm run build
      deploy:
        provider: s3
        access_key_id: $AWS_ACCESS_KEY_ID
        secret_access_key: $AWS_SECRET_ACCESS_KEY
        bucket: my-bucket
        local_dir: dist
        skip_cleanup: true
        on:
          branch: main

    - stage: deploy
      name: "Deploy to Production"
      script: skip
      deploy:
        provider: script
        script: ./deploy-prod.sh
        on:
          branch: main

notifications:
  slack:
    rooms:
      - secure: "encrypted-webhook-url"
    on_success: change
    on_failure: always
```

---

## Bitbucket Pipelines

```yaml
# bitbucket-pipelines.yml
image: node:20

definitions:
  caches:
    npm: ~/.npm
  services:
    postgres:
      image: postgres:15
      variables:
        POSTGRES_DB: test
        POSTGRES_USER: test
        POSTGRES_PASSWORD: test
  steps:
    - step: &build
        name: Build
        caches:
          - npm
        script:
          - npm ci
          - npm run build
        artifacts:
          - dist/**
    - step: &test
        name: Test
        caches:
          - npm
        script:
          - npm ci
          - npm test
    - step: &deploy-staging
        name: Deploy to Staging
        deployment: staging
        script:
          - pipe: atlassian/aws-s3-deploy:1.1.0
            variables:
              AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
              AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
              AWS_DEFAULT_REGION: eu-west-1
              S3_BUCKET: staging-bucket
              LOCAL_PATH: dist

pipelines:
  default:
    - step: *build
    - step: *test

  branches:
    main:
      - step: *build
      - step: *test
      - step:
          <<: *deploy-staging
          name: Deploy to Production
          deployment: production
          trigger: manual

  pull-requests:
    '**':
      - step: *build
      - step: *test
```

---

## Buildkite

```yaml
# .buildkite/pipeline.yml
steps:
  - label: ":npm: Install"
    command: npm ci
    key: install
    plugins:
      - docker#v5.10.0:
          image: node:20

  - label: ":jest: Test"
    command: npm test
    depends_on: install
    parallelism: 4
    plugins:
      - docker#v5.10.0:
          image: node:20
      - test-collector#v1.10.0:
          files: "junit.xml"

  - label: ":docker: Build"
    command: docker build -t myapp:$BUILDKITE_COMMIT .
    depends_on: install
    plugins:
      - docker-login#v2.1.0:
          username: $DOCKER_USER
          password-env: DOCKER_PASSWORD

  - wait

  - label: ":rocket: Deploy Staging"
    command: ./deploy.sh staging
    branches: develop

  - block: "Deploy to Production?"
    branches: main

  - label: ":rocket: Deploy Production"
    command: ./deploy.sh production
    branches: main
```

```yaml
# Buildkite med agents
steps:
  - label: "Build on Linux"
    command: make build
    agents:
      queue: linux

  - label: "Build on macOS"
    command: make build
    agents:
      queue: macos

  - label: "Build on Windows"
    command: make build
    agents:
      queue: windows
```

---

## Platform Comparison

```yaml
# Samma pipeline på olika plattformar

# GitHub Actions
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build

# GitLab CI
build:
  stage: build
  image: node:20
  script:
    - npm ci
    - npm run build

# CircleCI
jobs:
  build:
    docker:
      - image: cimg/node:20
    steps:
      - checkout
      - run: npm ci
      - run: npm run build

# Azure Pipelines
jobs:
  - job: Build
    pool:
      vmImage: ubuntu-latest
    steps:
      - task: NodeTool@0
        inputs:
          versionSpec: '20'
      - script: npm ci
      - script: npm run build
```

---

## Key Takeaways

1. CircleCI = snabb, Docker-native
2. Travis CI = enkel, bra för OSS
3. Bitbucket Pipelines = Atlassian-integration
4. Buildkite = flexibel, self-hosted
5. Koncept överförs mellan alla plattformar
''',
        },
        {
            "title": "Self-Hosted Runners",
            "slug": "self-hosted-runners",
            "difficulty": "advanced",
            "content": '''
# Self-Hosted Runners

## Varför behöver du kunna detta?

Self-hosted runners för:

- Specialhårdvara (GPU, ARM)
- Striktare säkerhet/compliance
- Kostnadsoptimering
- Tillgång till interna resurser

Cloud runners räcker inte alltid.

---

## Så fungerar det

Self-hosted setup:

1. **Provision** - skapa server
2. **Install** - runner-agent
3. **Register** - koppla till repo/org
4. **Label** - för targeting

---

## GitHub Actions Runner

```bash
# Installera GitHub Actions runner
# 1. Ladda ner
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# 2. Konfigurera
./config.sh --url https://github.com/myorg/myrepo --token ABCDEF123456

# 3. Starta som service
sudo ./svc.sh install
sudo ./svc.sh start
```

```yaml
# Använd self-hosted runner
jobs:
  build:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - run: npm run build

  # Med labels
  gpu-training:
    runs-on: [self-hosted, linux, gpu, cuda-12]
    steps:
      - run: nvidia-smi
      - run: python train_model.py
```

---

## Kubernetes Runner

```yaml
# Actions Runner Controller (ARC)
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: github-runners
spec:
  replicas: 3
  template:
    spec:
      repository: myorg/myrepo
      labels:
        - kubernetes
        - linux
      env:
        - name: DOCKER_HOST
          value: tcp://localhost:2375
      dockerdWithinRunnerContainer: true
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"
        requests:
          cpu: "500m"
          memory: "1Gi"
---
# Autoscaling
apiVersion: actions.summerwind.dev/v1alpha1
kind: HorizontalRunnerAutoscaler
metadata:
  name: github-runners-autoscaler
spec:
  scaleTargetRef:
    name: github-runners
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: TotalNumberOfQueuedAndInProgressWorkflowRuns
      repositoryNames:
        - myorg/myrepo
```

```bash
# Installera ARC med Helm
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm install actions-runner-controller actions-runner-controller/actions-runner-controller \
  --namespace actions-runner-system \
  --create-namespace \
  --set authSecret.create=true \
  --set authSecret.github_token=$GITHUB_PAT
```

---

## GitLab Runner

```bash
# Installera GitLab Runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt-get install gitlab-runner

# Registrera
sudo gitlab-runner register \
  --url https://gitlab.com/ \
  --registration-token $REGISTRATION_TOKEN \
  --executor docker \
  --docker-image node:20 \
  --description "Docker Runner" \
  --tag-list "docker,linux"
```

```toml
# /etc/gitlab-runner/config.toml
concurrent = 10
check_interval = 0

[[runners]]
  name = "Docker Runner"
  url = "https://gitlab.com/"
  token = "TOKEN"
  executor = "docker"
  [runners.docker]
    image = "node:20"
    privileged = true
    volumes = ["/cache", "/var/run/docker.sock:/var/run/docker.sock"]
    allowed_images = ["node:*", "python:*", "docker:*"]
    pull_policy = "if-not-present"
  [runners.cache]
    Type = "s3"
    [runners.cache.s3]
      ServerAddress = "s3.amazonaws.com"
      BucketName = "gitlab-runner-cache"
      AccessKey = "ACCESS_KEY"
      SecretKey = "SECRET_KEY"
```

---

## Docker-in-Docker Setup

```yaml
# GitHub Actions med DinD
jobs:
  build:
    runs-on: self-hosted
    container:
      image: docker:24-dind
      options: --privileged
    steps:
      - uses: actions/checkout@v4
      - run: |
          docker build -t myapp:${{ github.sha }} .
          docker push myapp:${{ github.sha }}
```

```yaml
# GitLab med DinD service
build:
  image: docker:24
  services:
    - docker:24-dind
  variables:
    DOCKER_HOST: tcp://docker:2376
    DOCKER_TLS_CERTDIR: "/certs"
  script:
    - docker build -t myapp .
```

---

## Security Hardening

```yaml
# Säker runner-konfiguration
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: secure-runners
spec:
  template:
    spec:
      # Begränsa resurser
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"

      # Kör som non-root
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000

      # Network policy
      serviceAccountName: runner-sa

      # Ephemeral runner (ny för varje job)
      ephemeral: true
```

```yaml
# Network policy för runners
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: runner-network-policy
spec:
  podSelector:
    matchLabels:
      app: github-runner
  policyTypes:
    - Egress
    - Ingress
  egress:
    - to:
        - ipBlock:
            cidr: 10.0.0.0/8            # Internt nätverk
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              app: docker-registry
  ingress: []                            # Ingen inkommande trafik
```

---

## Monitoring Runners

```yaml
# Prometheus metrics för runners
apiVersion: v1
kind: Service
metadata:
  name: runner-metrics
  labels:
    app: github-runner
spec:
  ports:
    - name: metrics
      port: 9090
  selector:
    app: github-runner
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: runner-monitor
spec:
  selector:
    matchLabels:
      app: github-runner
  endpoints:
    - port: metrics
      interval: 30s
```

```yaml
# Alerting för runner-status
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: runner-alerts
spec:
  groups:
    - name: runners
      rules:
        - alert: RunnerDown
          expr: up{job="github-runner"} == 0
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "GitHub Runner is down"

        - alert: RunnerQueueBacklog
          expr: github_runner_job_queue_length > 10
          for: 10m
          labels:
            severity: warning
          annotations:
            summary: "Runner queue backlog growing"
```

---

## Key Takeaways

1. Self-hosted för special-behov
2. Kubernetes ARC för skalbarhet
3. Ephemeral runners för säkerhet
4. DinD för container builds
5. Monitoring och alerting viktigt
''',
        },
        {
            "title": "Monorepo CI/CD Patterns",
            "slug": "monorepo-cicd-patterns",
            "difficulty": "advanced",
            "content": '''
# Monorepo CI/CD Patterns

## Varför behöver du kunna detta?

Monorepos kräver smart CI/CD:

- Bygg inte allt vid varje commit
- Dela cache mellan projekt
- Versionera koordinerat
- Hantera beroenden

Turbo, Nx, Bazel löser detta.

---

## Så fungerar det

Monorepo CI-utmaningar:

1. **Change Detection** - vad ändrades
2. **Dependency Graph** - vad påverkas
3. **Selective Execution** - kör bara det
4. **Caching** - spara tid

---

## Turborepo Setup

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "inputs": ["src/**/*.tsx", "src/**/*.ts", "test/**/*.ts"]
    },
    "lint": {
      "outputs": []
    },
    "deploy": {
      "dependsOn": ["build", "test"],
      "outputs": []
    }
  }
}
```

```yaml
# GitHub Actions med Turborepo
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0                 # Full history för change detection

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install

      # Turbo remote caching
      - name: Setup Turbo cache
        uses: actions/cache@v4
        with:
          path: .turbo
          key: turbo-${{ github.sha }}
          restore-keys: |
            turbo-

      # Kör bara det som ändrats
      - name: Build affected packages
        run: pnpm turbo run build --filter=[HEAD^1]
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: ${{ vars.TURBO_TEAM }}

      - name: Test affected packages
        run: pnpm turbo run test --filter=[HEAD^1]
```

---

## Nx Monorepo

```json
// nx.json
{
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "lint", "test", "e2e"]
      }
    }
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"]
    },
    "test": {
      "inputs": ["default", "^production"]
    }
  }
}
```

```yaml
# GitHub Actions med Nx
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  main:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: nrwl/nx-set-shas@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci

      # Kör affected commands
      - run: npx nx affected -t lint --parallel=3
      - run: npx nx affected -t test --parallel=3 --ci --code-coverage
      - run: npx nx affected -t build --parallel=3

      # Deploy affected apps
      - name: Deploy affected apps
        if: github.ref == 'refs/heads/main'
        run: |
          AFFECTED=$(npx nx show projects --affected --type=app)
          for app in $AFFECTED; do
            echo "Deploying $app..."
            npx nx run $app:deploy
          done
```

---

## Change Detection

```yaml
# Manuell change detection
jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      frontend: ${{ steps.filter.outputs.frontend }}
      backend: ${{ steps.filter.outputs.backend }}
      shared: ${{ steps.filter.outputs.shared }}
    steps:
      - uses: actions/checkout@v4

      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            frontend:
              - 'apps/frontend/**'
              - 'packages/ui/**'
              - 'packages/shared/**'
            backend:
              - 'apps/backend/**'
              - 'packages/shared/**'
              - 'packages/db/**'
            shared:
              - 'packages/shared/**'

  build-frontend:
    needs: detect-changes
    if: needs.detect-changes.outputs.frontend == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build:frontend

  build-backend:
    needs: detect-changes
    if: needs.detect-changes.outputs.backend == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build:backend
```

---

## Versioning Strategy

```yaml
# Changesets för koordinerad versioning
# .changeset/config.json
{
  "$schema": "https://unpkg.com/@changesets/config@3.0.0/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [
    ["@myorg/frontend", "@myorg/backend", "@myorg/shared"]
  ],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch"
}
```

```yaml
# GitHub Actions för release
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install

      - name: Create Release PR or Publish
        uses: changesets/action@v1
        with:
          publish: pnpm release
          version: pnpm changeset version
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

---

## Deploy Coordination

```yaml
# Koordinerad deploy
jobs:
  detect:
    runs-on: ubuntu-latest
    outputs:
      apps: ${{ steps.affected.outputs.apps }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - id: affected
        run: |
          APPS=$(npx nx show projects --affected --type=app | jq -R -s -c 'split("\n")[:-1]')
          echo "apps=${APPS}" >> $GITHUB_OUTPUT

  deploy:
    needs: detect
    if: needs.detect.outputs.apps != '[]'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        app: ${{ fromJson(needs.detect.outputs.apps) }}
      max-parallel: 1                    # En app i taget
    steps:
      - uses: actions/checkout@v4

      - name: Deploy ${{ matrix.app }}
        run: |
          echo "Deploying ${{ matrix.app }}..."

          case "${{ matrix.app }}" in
            frontend)
              netlify deploy --prod
              ;;
            backend)
              railway up
              ;;
            api-gateway)
              kubectl apply -f k8s/${{ matrix.app }}/
              ;;
          esac

  verify:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - name: Run E2E tests
        run: npx playwright test
```

---

## Shared Dependencies

```yaml
# Hantera shared packages
jobs:
  shared-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for shared package changes
        id: shared
        run: |
          if git diff --name-only HEAD^1 | grep -q "packages/shared"; then
            echo "changed=true" >> $GITHUB_OUTPUT
          fi

      - name: Rebuild all dependents
        if: steps.shared.outputs.changed == 'true'
        run: |
          # Om shared ändrades, bygg allt som beror på det
          pnpm turbo run build --filter="...@myorg/shared"

      - name: Test all dependents
        if: steps.shared.outputs.changed == 'true'
        run: |
          pnpm turbo run test --filter="...@myorg/shared"
```

---

## Key Takeaways

1. Turbo/Nx för smart change detection
2. Remote caching sparar enormt med tid
3. Affected commands = bygg bara det ändrade
4. Changesets för koordinerad versioning
5. Deploy i rätt ordning för dependencies
''',
        },
        {
            "title": "Enterprise CI/CD Patterns",
            "slug": "enterprise-cicd-patterns",
            "difficulty": "expert",
            "content": '''
# Enterprise CI/CD Patterns

## Varför behöver du kunna detta?

Enterprise-skala kräver:

- Standardisering över team
- Centraliserad governance
- Cost management
- Compliance automation

Patterns som skalar till 100+ team.

---

## Så fungerar det

Enterprise CI/CD principer:

1. **Platform Team** - bygger verktygen
2. **Product Teams** - använder verktygen
3. **Golden Paths** - rekommenderad väg
4. **Guardrails** - automatiska begränsningar

---

## Template Libraries

```yaml
# Centralt template repo
# .github/workflows/templates/node-service.yml
name: Node Service Template

on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: '20'
      deploy-target:
        type: string
        required: true
    secrets:
      DEPLOY_TOKEN:
        required: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'

      - run: npm ci
      - run: npm run build
      - run: npm test

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  deploy:
    needs: [build, security]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to ${{ inputs.deploy-target }}
        run: ./deploy.sh ${{ inputs.deploy-target }}
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

```yaml
# Användning i produkt-repo
name: CI/CD

on:
  push:
    branches: [main]

jobs:
  pipeline:
    uses: myorg/platform-templates/.github/workflows/node-service.yml@v2
    with:
      node-version: '20'
      deploy-target: 'production'
    secrets:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

---

## Policy Enforcement

```yaml
# OPA/Conftest för policy
name: Policy Check

on:
  pull_request:

jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Conftest
        run: |
          wget https://github.com/open-policy-agent/conftest/releases/download/v0.48.0/conftest_0.48.0_Linux_x86_64.tar.gz
          tar xzf conftest_0.48.0_Linux_x86_64.tar.gz
          sudo mv conftest /usr/local/bin/

      - name: Test Kubernetes manifests
        run: conftest test k8s/ -p policies/

      - name: Test Terraform
        run: conftest test terraform/ -p policies/

      - name: Test Dockerfile
        run: conftest test Dockerfile -p policies/
```

```rego
# policies/kubernetes.rego
package kubernetes

deny[msg] {
  input.kind == "Deployment"
  not input.spec.template.spec.securityContext.runAsNonRoot
  msg = "Deployments must run as non-root"
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.resources.limits
  msg = sprintf("Container %s must have resource limits", [container.name])
}

deny[msg] {
  input.kind == "Deployment"
  not input.metadata.labels["app.kubernetes.io/version"]
  msg = "Deployments must have version label"
}
```

---

## Cost Management

```yaml
# Resource quotas och cost tracking
jobs:
  cost-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Estimate infrastructure cost
        id: infracost
        uses: infracost/actions/setup@v2
        with:
          api-key: ${{ secrets.INFRACOST_API_KEY }}

      - name: Generate cost diff
        run: |
          infracost diff --path=terraform/ \
            --format=json \
            --out-file=/tmp/infracost.json

      - name: Check cost threshold
        run: |
          MONTHLY_COST=$(jq '.diffTotalMonthlyCost' /tmp/infracost.json)
          if (( $(echo "$MONTHLY_COST > 1000" | bc -l) )); then
            echo "❌ Cost increase exceeds $1000/month threshold"
            echo "Requires approval from @platform-team"
            exit 1
          fi

      - name: Post cost comment
        uses: infracost/actions/comment@v1
        with:
          path: /tmp/infracost.json
          behavior: update
```

---

## Centralized Logging

```yaml
# Logga alla pipeline-events
jobs:
  any-job:
    runs-on: ubuntu-latest
    steps:
      - name: Initialize logging
        run: |
          # Skapa strukturerad log
          cat <<EOF > pipeline-log.json
          {
            "pipeline_id": "${{ github.run_id }}",
            "repository": "${{ github.repository }}",
            "branch": "${{ github.ref_name }}",
            "commit": "${{ github.sha }}",
            "actor": "${{ github.actor }}",
            "started_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "event": "started"
          }
          EOF

          curl -X POST https://logs.mycompany.com/pipelines \
            -H "Authorization: Bearer ${{ secrets.LOG_TOKEN }}" \
            -d @pipeline-log.json

      - name: Run steps...
        run: echo "Doing work..."

      - name: Finalize logging
        if: always()
        run: |
          cat <<EOF > pipeline-log.json
          {
            "pipeline_id": "${{ github.run_id }}",
            "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "event": "completed",
            "status": "${{ job.status }}",
            "duration_seconds": "${{ github.event.workflow_run.run_duration }}"
          }
          EOF

          curl -X POST https://logs.mycompany.com/pipelines \
            -H "Authorization: Bearer ${{ secrets.LOG_TOKEN }}" \
            -d @pipeline-log.json
```

---

## Multi-Tenant Platform

```yaml
# Platform för flera teams
# platform/team-onboarding.yml
name: Onboard New Team

on:
  workflow_dispatch:
    inputs:
      team_name:
        required: true
      repository:
        required: true
      environments:
        required: true
        type: choice
        options:
          - dev
          - dev,staging
          - dev,staging,prod

jobs:
  onboard:
    runs-on: ubuntu-latest
    steps:
      - name: Create team resources
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_TOKEN }}
          script: |
            const teamName = '${{ inputs.team_name }}';
            const repo = '${{ inputs.repository }}';
            const envs = '${{ inputs.environments }}'.split(',');

            // Skapa environments
            for (const env of envs) {
              await github.rest.repos.createOrUpdateEnvironment({
                owner: context.repo.owner,
                repo: repo,
                environment_name: env,
                deployment_branch_policy: {
                  protected_branches: env === 'prod',
                  custom_branch_policies: env !== 'prod'
                }
              });
            }

            // Sätt upp branch protection
            await github.rest.repos.updateBranchProtection({
              owner: context.repo.owner,
              repo: repo,
              branch: 'main',
              required_status_checks: {
                strict: true,
                contexts: ['build', 'test', 'security-scan']
              },
              required_pull_request_reviews: {
                required_approving_review_count: 2
              },
              enforce_admins: true
            });

      - name: Setup standard workflows
        run: |
          git clone https://github.com/myorg/${{ inputs.repository }}
          cd ${{ inputs.repository }}

          # Kopiera standard workflows
          mkdir -p .github/workflows
          cp ../platform/templates/*.yml .github/workflows/

          git add .github/
          git commit -m "chore: Add standard CI/CD workflows"
          git push
```

---

## Metrics Dashboard

```yaml
# Enterprise metrics collection
jobs:
  collect-metrics:
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Send metrics to DataDog
        run: |
          # DORA metrics
          curl -X POST "https://api.datadoghq.com/api/v1/series" \
            -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
            -d '{
              "series": [{
                "metric": "cicd.deployment_frequency",
                "type": "count",
                "points": [['"$(date +%s)"', 1]],
                "tags": [
                  "team:${{ github.repository_owner }}",
                  "repo:${{ github.repository }}",
                  "env:${{ github.event.deployment.environment }}"
                ]
              }, {
                "metric": "cicd.lead_time_seconds",
                "type": "gauge",
                "points": [['"$(date +%s)"', '"${{ github.event.workflow_run.run_duration }}"']],
                "tags": [
                  "team:${{ github.repository_owner }}",
                  "repo:${{ github.repository }}"
                ]
              }]
            }'
```

---

## Key Takeaways

1. Templates standardiserar över teams
2. Policy-as-Code för governance
3. Cost management förhindrar överraskningar
4. Centraliserad logging för visibility
5. Self-service med guardrails
''',
        },
    ],
}
