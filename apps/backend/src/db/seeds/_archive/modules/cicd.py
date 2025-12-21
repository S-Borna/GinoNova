"""
CI/CD Mastery Module
====================

Komplett kurs i Continuous Integration & Continuous Deployment.
Följer Linux-mallen: Svenska, pedagogiskt, kommentarer på varje rad.

20 noder från grundläggande till avancerat.
"""

MODULE = {
    "name": "CI/CD Mastery",
    "slug": "cicd-mastery",
    "description": "Automatisera bygg, test och deployment med moderna CI/CD-pipelines",
    "track_slug": "devops",
    "order_index": 9,
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "prerequisites": ["git-github-mastery"],
    "icon": "🔄",
    "color": "#2088FF",
    "tasks": [
        {
            "order_index": 1,
            "title": "Introduction to CI/CD",
            "slug": "introduction-to-cicd",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 50,
            "content": """# Introduction to CI/CD

------------------------------------------------------------

## Introduktion

Föreställ dig att varje gång en utvecklare pushar kod så tar det tre dagar innan någon testar den, och när buggar hittas har alla redan gått vidare till andra uppgifter. Detta är verkligheten för team utan CI/CD - en värld av manuella processer, sena upptäckter och rädsla för att deploya på fredagar. Continuous Integration och Continuous Delivery/Deployment är DevOps-revolutionen som förvandlar denna kaotiska process till ett väloljat maskineri där kod testas automatiskt inom minuter, buggar fångas innan de når produktion, och deployments blir så rutinmässiga att de kan göras när som helst utan stress.

------------------------------------------------------------

## Teori

CI/CD representerar en fundamental förändring i hur mjukvara byggs och levereras. Continuous Integration handlar om att integrera kod från flera utvecklare till en delad huvudbranch flera gånger om dagen, där varje integration verifieras av automatiserade byggen och tester. Detta bryter den traditionella modellen där utvecklare arbetade isolerat i veckor innan de slog ihop sin kod, vilket ofta resulterade i smärtsamma merge-konflikter och svårhittade buggar. CI kräver att teamet committar ofta, att byggen är snabba, och att trasiga byggen fixas omedelbart - det är ett kulturellt skifte lika mycket som ett tekniskt.

Continuous Delivery och Continuous Deployment är två relaterade men distinkta koncept. Continuous Delivery innebär att kod alltid är i ett deploybart tillstånd och kan releasas till produktion med ett knapptryck, medan Continuous Deployment tar det ett steg längre genom att automatiskt deploya varje ändring som passerar alla tester direkt till produktion utan manuell intervention. De flesta organisationer börjar med Continuous Delivery och går mot Continuous Deployment när deras testsvit och processer mognar.

```
CI/CD EVOLUTION
------------------------------------------------------------

    TRADITIONELL           CONTINUOUS            CONTINUOUS
    DEVELOPMENT           INTEGRATION            DEPLOYMENT
         |                     |                      |
         v                     v                      v
    +--------+            +--------+             +--------+
    | Veckor |            | Timmar |             | Minuter|
    | mellan |    --->    | mellan |    --->     | till   |
    | merges |            | merges |             | prod   |
    +--------+            +--------+             +--------+
         |                     |                      |
    Stora                  Små                   Automatisk
    konflikter             ändringar             deployment

    RISK: HÖG              RISK: MEDIUM          RISK: LÅG
    FEEDBACK: LÅNGSAM      FEEDBACK: SNABB       FEEDBACK: OMEDELBAR
```

En CI/CD-pipeline är sekvensen av steg som kod går igenom från commit till produktion. Den typiska pipelinen börjar med kodhantering där utvecklaren pushar till ett repository som Git. Byggsteget kompilerar koden, installerar dependencies och skapar artefakter. Teststeget kör unit-tester, integrationstester och eventuellt end-to-end-tester. Deployment-steget skickar koden till olika miljöer som staging och produktion. Varje steg fungerar som en kvalitetsport - om något misslyckas stoppas pipelinen och teamet meddelas.

DORA-metriker (DevOps Research and Assessment) är branschstandarden för att mäta CI/CD-effektivitet. Deployment Frequency mäter hur ofta kod når produktion - elite teams deployer flera gånger per dag. Lead Time for Changes mäter tiden från commit till produktion - elite teams har under en timme. Change Failure Rate mäter hur ofta deployments orsakar problem - elite teams har under 15%. Mean Time to Recovery mäter hur snabbt team återhämtar sig från fel - elite teams har under en timme. Dessa metriker ger objektiv data för att driva förbättringar.

------------------------------------------------------------

## Steg-för-steg Guide

Implementera grundläggande CI/CD från grunden:

```bash
# Steg 1: Skapa projektstruktur
mkdir my-cicd-project && cd my-cicd-project
git init
npm init -y

# Steg 2: Lägg till testramverk
npm install --save-dev jest
echo '{"scripts":{"test":"jest","lint":"eslint ."}}' > package.json

# Steg 3: Skapa enkel testkod
mkdir src tests
cat > src/calculator.js << 'EOF'
function add(a, b) {
  return a + b;
}
module.exports = { add };
EOF

cat > tests/calculator.test.js << 'EOF'
const { add } = require('../src/calculator');
test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(3);
});
EOF

# Steg 4: Skapa GitHub Actions workflow
mkdir -p .github/workflows
cat > .github/workflows/ci.yml << 'EOF'
name: CI Pipeline

on:
  push:
    branches: [main]
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
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build --if-present
EOF

# Steg 5: Pusha och verifiera
git add .
git commit -m "feat: add CI pipeline"
git push origin main

# Gå till GitHub -> Actions för att se pipelinen köra
```

------------------------------------------------------------

## Praktiska Exempel

Exempel 1 - Multi-stage pipeline med gates:
```yaml
# .github/workflows/complete-pipeline.yml
name: Complete CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # Stage 1: Snabb kvalitetskontroll
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint

  # Stage 2: Unit tester (parallellt med lint)
  unit-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3

  # Stage 3: Bygg (efter lint och test)
  build:
    needs: [lint, unit-test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/

  # Stage 4: Deploy till staging
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
      - run: echo "Deploying to staging..."

  # Stage 5: Deploy till produktion (endast main)
  deploy-production:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
      - run: echo "Deploying to production..."
```

Exempel 2 - Fail-fast med snabb feedback:
```yaml
# Optimerad för snabbast möjliga feedback
jobs:
  # Kör på sekunder - hittar 80% av problemen
  quick-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint        # 10 sekunder
      - run: npm run typecheck   # 15 sekunder
      - run: npm run test:unit   # 30 sekunder

  # Kör på minuter - hittar integrationsproblem
  integration:
    needs: quick-checks
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:integration
```

Exempel 3 - Branch-baserad deployment:
```yaml
on:
  push:
    branches:
      - main
      - develop
      - 'release/*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to environment
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "Deploying to PRODUCTION"
            ENVIRONMENT=production
          elif [[ "${{ github.ref }}" == "refs/heads/develop" ]]; then
            echo "Deploying to STAGING"
            ENVIRONMENT=staging
          elif [[ "${{ github.ref }}" == refs/heads/release/* ]]; then
            echo "Deploying to UAT"
            ENVIRONMENT=uat
          fi
          ./deploy.sh $ENVIRONMENT
```

------------------------------------------------------------

## Bästa Praxis

1. Commit ofta och i små steg - Små ändringar är lättare att granska, testa och rulla tillbaka än stora batchar med kod som ändrats under veckor
2. Fixa trasiga byggen omedelbart - En trasig build blockerar hela teamet och underminerar förtroendet för CI-systemet
3. Kör snabba tester först - Ordna pipelinen så lint och unit-tester kör innan långsammare integrationstester för snabbast feedback
4. Använd lock-filer för reproducerbarhet - package-lock.json och liknande garanterar att samma dependencies installeras varje gång
5. Automatisera allt som kan automatiseras - Manuella steg är felkällor och flaskhalsar
6. Implementera quality gates - Blockera deployment om tester misslyckas eller coverage sjunker under threshold
7. Övervaka DORA-metriker - Mät deployment frequency, lead time, change failure rate och MTTR för kontinuerlig förbättring
8. Behandla infrastruktur som kod - Pipelines ska vara versionshanterade och granskningsbara

------------------------------------------------------------

## Vanliga Fallgropar

1. För långa pipelines - Pipelines som tar 30+ minuter dödar developer-produktiviteten och uppmuntrar till att skippa CI
2. Flaky tests - Tester som ibland misslyckas utan kodändring förstör förtroendet och leder till "bara kör om"-kultur
3. Manuella deployment-steg - Varje manuellt steg är en risk för fel och en flaskhals för leverans
4. Ignorera trasiga byggen - "Den där är alltid trasig" är ett varningstecken på att CI-kulturen är bruten
5. Otillräcklig testning - En grön pipeline utan meningsfulla tester ger falskt förtroende
6. Secrets i kod - API-nycklar och lösenord ska aldrig committas, använd secrets management
7. Ingen rollback-plan - Varje deployment måste ha en snabb väg tillbaka vid problem
8. Silos mellan team - CI/CD kräver samarbete mellan utvecklare, ops och QA

------------------------------------------------------------

## Övningar

### Övning 1: Din första pipeline
Skapa ett nytt GitHub-repository med en enkel Node.js-applikation och implementera en CI-pipeline som kör linting och tester vid varje push.

<details>
<summary>Visa lösning</summary>

```bash
# Skapa nytt repo på GitHub, klona och konfigurera
git clone https://github.com/username/cicd-ovning.git
cd cicd-ovning

# Initiera projekt
npm init -y
npm install --save-dev jest eslint

# package.json scripts
cat > package.json << 'EOF'
{
  "name": "cicd-ovning",
  "scripts": {
    "test": "jest",
    "lint": "eslint src/"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "eslint": "^8.0.0"
  }
}
EOF

# Skapa kod och test
mkdir src
echo 'module.exports.greet = (name) => `Hello, ${name}!`;' > src/index.js
mkdir __tests__
echo "const {greet} = require('../src'); test('greets', () => expect(greet('World')).toBe('Hello, World!'));" > __tests__/index.test.js

# Skapa workflow
mkdir -p .github/workflows
cat > .github/workflows/ci.yml << 'EOF'
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint
      - run: npm test
EOF

git add . && git commit -m "Add CI pipeline" && git push
```

</details>

### Övning 2: Pipeline med quality gates
Utöka pipelinen med code coverage-krav där deployment blockeras om coverage är under 80%.

<details>
<summary>Visa lösning</summary>

```yaml
# .github/workflows/ci.yml
name: CI with Quality Gates

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci

      - name: Run tests with coverage
        run: npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          fail_ci_if_error: true

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Coverage passed, deploying..."
```

```javascript
// jest.config.js
module.exports = {
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

</details>

### Övning 3: Multi-environment deployment
Implementera en pipeline som deployer till staging vid push till develop-branch och till produktion vid push till main med manuellt godkännande.

<details>
<summary>Visa lösning</summary>

```yaml
# .github/workflows/deploy.yml
name: Multi-Environment Deploy

on:
  push:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build
      - run: |
          echo "Deploying to staging..."
          # ./deploy.sh staging

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build
      - run: |
          echo "Deploying to production..."
          # ./deploy.sh production
```

Konfigurera environment protection rules i GitHub:
1. Settings -> Environments -> production
2. Required reviewers: Lägg till godkännare
3. Wait timer: 5 minuter (valfritt)

</details>

------------------------------------------------------------

## Kopplingar

- GitHub Actions Fundamentals - Fördjupning i GitHub Actions som CI/CD-plattform
- GitLab CI/CD - Alternativ CI/CD-plattform med liknande koncept
- Testing in Pipelines - Hur man strukturerar tester för CI/CD
- Build and Release Strategies - Deployment-strategier som blue-green och canary
- Docker Mastery - Container-baserade pipelines för reproducerbarhet

------------------------------------------------------------

## Sammanfattning

CI/CD automatiserar hela processen från kod till produktion genom kontinuerlig integration, testning och deployment. Continuous Integration kräver frekventa commits, automatiserade byggen och omedelbar fix av trasiga builds. Continuous Delivery håller koden alltid deploybar medan Continuous Deployment automatiserar hela vägen till produktion. Pipelines struktureras i stages (build, test, deploy) med quality gates som blockerar vid fel. DORA-metriker (deployment frequency, lead time, change failure rate, MTTR) mäter CI/CD-effektivitet. Nyckeln är snabb feedback, reproducerbarhet genom lock-filer, och en kultur där trasiga byggen fixas omedelbart.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `git push origin main` | Triggar CI pipeline |
| `npm ci` | Installerar exakta versioner från lock-fil |
| `npm test -- --coverage` | Kör tester med coverage-rapport |
| `npm run lint` | Kör linting för kodkvalitet |
| `gh run list` | Lista GitHub Actions-körningar |
| `gh run view` | Visa detaljer för en körning |
| `gh run watch` | Följ pipeline i realtid |
| `gh workflow run` | Trigga workflow manuellt |

------------------------------------------------------------

## Referenser

- GitHub Actions Documentation - docs.github.com/actions
- DORA Metrics - dora.dev för DevOps Research and Assessment
- Continuous Delivery (Humble & Farley) - Klassisk bok om CD
- Accelerate (Forsgren, Humble, Kim) - Forskning bakom DORA
- The DevOps Handbook - Praktisk guide till DevOps-implementation
""",
        },
        {
            "order_index": 2,
            "title": "GitHub Actions Fundamentals",
            "slug": "github-actions-fundamentals",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 50,
            "content": """# GitHub Actions Fundamentals

------------------------------------------------------------

## Introduktion

GitHub Actions har revolutionerat CI/CD genom att erbjuda kraftfull automation direkt integrerad i världens största kodplattform. Istället för att konfigurera separata CI-servrar, hantera Jenkins-installationer eller betala för externa tjänster får du med GitHub Actions en komplett automationsplattform som aktiveras med en enda YAML-fil i ditt repository. Över 15,000 färdiga actions i marketplace, generös gratisnivå för public repos, och djup integration med GitHub-ekosystemet gör detta till det naturliga valet för de flesta projekt.

------------------------------------------------------------

## Teori

GitHub Actions bygger på en hierarkisk struktur där workflows är toppnivån. En workflow är en automatiserad process definierad i en YAML-fil under .github/workflows/ och kan innehålla ett eller flera jobs. Varje job kör på en runner - en virtuell maskin som GitHub tillhandahåller eller som du hostar själv. Jobs innehåller steps som antingen använder färdiga actions från marketplace eller kör shell-kommandon direkt. Denna modulära arkitektur gör det möjligt att bygga komplexa automationspipelines från återanvändbara komponenter.

Events triggar workflows och GitHub erbjuder ett rikt utbud av triggers. Push-events aktiverar workflows vid commits till specificerade branches. Pull_request-events kör vid PR-aktivitet som öppning, uppdatering eller merging. Schedule använder cron-syntax för tidbaserad körning. Workflow_dispatch tillåter manuell triggning från GitHub UI med valfria inputparametrar. Repository_dispatch möjliggör extern triggning via API. Kombinationen av dessa events ger full kontroll över när automation ska köra.

```
GITHUB ACTIONS ARKITEKTUR
------------------------------------------------------------

    REPOSITORY
         |
         v
    .github/workflows/
         |
         +-- ci.yml (Workflow 1)
         |      |
         |      +-- Job: lint
         |      |      +-- Step: checkout
         |      |      +-- Step: run eslint
         |      |
         |      +-- Job: test
         |             +-- Step: checkout
         |             +-- Step: setup-node
         |             +-- Step: npm test
         |
         +-- deploy.yml (Workflow 2)
                |
                +-- Job: build
                +-- Job: deploy-staging
                +-- Job: deploy-prod

    RUNNERS (executors)
    +------------------+------------------+------------------+
    | ubuntu-latest    | windows-latest   | macos-latest     |
    | (Linux)          | (Windows)        | (macOS)          |
    +------------------+------------------+------------------+
    | Self-hosted runners för specialiserad hårdvara/säkerhet |
    +--------------------------------------------------------+
```

Matrix builds är en kraftfull funktion som automatiskt skapar flera jobb från en enda definition. Genom att specificera arrayer av värden för olika parametrar som operativsystem, språkversioner eller miljökonfigurationer genererar GitHub Actions alla kombinationer. Detta är ovärderligt för bibliotek som måste fungera över flera plattformar eller Node-versioner. Exclude-direktivet filtrerar bort specifika kombinationer och include lägger till extra konfigurationer.

Secrets och environment variables hanterar känslig data säkert. Repository secrets krypteras och är endast tillgängliga för workflows. Environment secrets kopplas till specifika deployment-miljöer som staging eller production. Variables är för icke-känslig konfiguration. GitHub maskar automatiskt secrets i loggar för att förhindra ofrivillig exponering. Organization secrets kan delas mellan repositories för centraliserad hantering.

------------------------------------------------------------

## Steg-för-steg Guide

Bygg en komplett CI/CD workflow från grunden:

```yaml
# .github/workflows/ci.yml
# Steg 1: Definiera namn och triggers
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
    paths-ignore:
      - '**.md'
      - 'docs/**'
  pull_request:
    branches: [main]
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

# Steg 2: Globala environment variables
env:
  NODE_VERSION: '20'
  CI: true

# Steg 3: Definiera jobs
jobs:
  # Job 1: Snabba kvalitetskontroller
  lint:
    name: Lint Code
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Run Prettier check
        run: npm run format:check

  # Job 2: Tester med coverage
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - run: npm ci

      - name: Run tests with coverage
        run: npm test -- --coverage --coverageReporters=lcov

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: true

  # Job 3: Bygg applikation
  build:
    name: Build Application
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - run: npm ci
      - run: npm run build

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ github.sha }}
          path: dist/
          retention-days: 7

  # Job 4: Deploy (endast main branch)
  deploy:
    name: Deploy to ${{ github.event.inputs.environment || 'staging' }}
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main' || github.event_name == 'workflow_dispatch'
    environment:
      name: ${{ github.event.inputs.environment || 'staging' }}
      url: ${{ steps.deploy.outputs.url }}
    steps:
      - name: Download build artifact
        uses: actions/download-artifact@v4
        with:
          name: build-${{ github.sha }}
          path: dist/

      - name: Deploy application
        id: deploy
        run: |
          echo "Deploying to ${{ github.event.inputs.environment || 'staging' }}..."
          echo "url=https://${{ github.event.inputs.environment || 'staging' }}.example.com" >> $GITHUB_OUTPUT
```

------------------------------------------------------------

## Praktiska Exempel

Exempel 1 - Matrix build för multi-platform testing:
```yaml
jobs:
  test-matrix:
    name: Test on ${{ matrix.os }} / Node ${{ matrix.node }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false  # Fortsätt alla jobb även om ett misslyckas
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [18, 20, 22]
        exclude:
          - os: windows-latest
            node: 18  # Skippa Windows + Node 18
        include:
          - os: ubuntu-latest
            node: 20
            experimental: true  # Extra flagga

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}

      - run: npm ci
      - run: npm test

      - name: Experimental tests
        if: matrix.experimental
        run: npm run test:experimental
```

Exempel 2 - Reusable workflow:
```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy Workflow

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      version:
        required: true
        type: string
    secrets:
      deploy_token:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ inputs.version }}

      - name: Deploy
        env:
          TOKEN: ${{ secrets.deploy_token }}
        run: ./deploy.sh ${{ inputs.environment }}

# Användning från annan workflow:
# jobs:
#   call-deploy:
#     uses: ./.github/workflows/reusable-deploy.yml
#     with:
#       environment: production
#       version: v1.2.3
#     secrets:
#       deploy_token: ${{ secrets.DEPLOY_TOKEN }}
```

Exempel 3 - Composite action:
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
      shell: bash
      run: npm ci

    - name: Verify installation
      shell: bash
      run: npm ls --depth=0

# Användning:
# steps:
#   - uses: actions/checkout@v4
#   - uses: ./.github/actions/setup-project
#     with:
#       node-version: '22'
```

------------------------------------------------------------

## Bästa Praxis

1. Pin action versions - Använd @v4 eller specifik SHA istället för @main för reproducerbarhet och säkerhet
2. Använd caching strategiskt - setup-node har inbyggd cache, använd actions/cache för andra dependencies
3. Parallelisera oberoende jobs - Jobs utan needs kör parallellt och sparar tid
4. Fail fast för snabb feedback - Kör lint och snabba tester först innan långsammare steg
5. Använd environments för deployment - Ger approval gates, secrets isolation och deployment history
6. Begränsa workflow permissions - Sätt permissions explicit istället för default write-all
7. Använd workflow_dispatch för manuella triggers - Ger flexibilitet för ad-hoc körningar
8. Organisera workflows logiskt - Separera CI och CD i olika filer för klarhet

------------------------------------------------------------

## Vanliga Fallgropar

1. Överdriven concurrency - För många parallella matrix-jobb kan sluka minuter snabbt på betalplaner
2. Saknad caching - Att installera dependencies varje gång slösar tid och resurser
3. Secrets i loggar - Även om GitHub maskar kan debug-output avslöja känslig data
4. Hårdkodade versioner - Att inte uppdatera actions regelbundet missar säkerhetspatchar
5. Ignorera fail-fast - En trasig matris-cell bör inte alltid stoppa alla andra tester
6. För stora artifacts - Upload av GB-stora artifacts slösar lagring och tid
7. Saknad timeout - Jobs som hänger kan köra i 6 timmar utan timeout-konfiguration
8. Branch protection utan CI - Required status checks kräver att workflows faktiskt kör

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande CI workflow
Skapa en workflow som kör linting och tester vid push och pull requests till main-branchen.

<details>
<summary>Visa lösning</summary>

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Lint
        run: npm run lint

      - name: Test
        run: npm test
```

</details>

### Övning 2: Matrix build
Implementera en matrix build som testar mot Node 18, 20 och 22 på Ubuntu och macOS.

<details>
<summary>Visa lösning</summary>

```yaml
name: Matrix CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
        node: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'

      - run: npm ci
      - run: npm test

      - name: Report
        run: echo "Tested on ${{ matrix.os }} with Node ${{ matrix.node }}"
```

</details>

### Övning 3: Reusable workflow med secrets
Skapa en reusable workflow för deployment som tar environment och version som input och använder secrets för authentication.

<details>
<summary>Visa lösning</summary>

```yaml
# .github/workflows/deploy-reusable.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      version:
        required: true
        type: string
    secrets:
      AWS_ACCESS_KEY_ID:
        required: true
      AWS_SECRET_ACCESS_KEY:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ inputs.version }}

      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Deploy to ${{ inputs.environment }}
        run: |
          echo "Deploying version ${{ inputs.version }} to ${{ inputs.environment }}"
          aws s3 sync ./dist s3://myapp-${{ inputs.environment }}/

# Anrop från main workflow:
# .github/workflows/release.yml
# jobs:
#   deploy-staging:
#     uses: ./.github/workflows/deploy-reusable.yml
#     with:
#       environment: staging
#       version: ${{ github.sha }}
#     secrets:
#       AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
#       AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

</details>

------------------------------------------------------------

## Kopplingar

- Introduction to CI/CD - Grundläggande CI/CD-koncept som denna nod bygger på
- GitLab CI/CD - Jämförbar CI/CD-plattform med liknande koncept
- Secrets Management in CI/CD - Fördjupning i secrets-hantering
- Container-based CI/CD - Docker builds med GitHub Actions
- Self-Hosted Runners - När GitHub-hosted runners inte räcker till

------------------------------------------------------------

## Sammanfattning

GitHub Actions erbjuder kraftfull CI/CD direkt integrerad i GitHub genom YAML-baserade workflows. Arkitekturen består av workflows som innehåller jobs, som i sin tur innehåller steps med actions eller kommandon. Events som push, pull_request och schedule triggar workflows. Matrix builds automatiserar multi-platform testning. Secrets och environments hanterar känslig data och deployment-miljöer säkert. Reusable workflows och composite actions möjliggör återanvändning över repositories. Best practices inkluderar version pinning, strategisk caching, parallellisering och explicit permissions.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `gh workflow list` | Lista alla workflows i repo |
| `gh workflow run NAME` | Trigga workflow manuellt |
| `gh run list` | Lista workflow-körningar |
| `gh run view RUN_ID` | Visa detaljer för körning |
| `gh run watch RUN_ID` | Följ körning i realtid |
| `gh run download RUN_ID` | Ladda ner artifacts |
| `gh secret set NAME` | Skapa/uppdatera secret |
| `gh variable set NAME` | Skapa/uppdatera variable |
| `act` | Kör workflows lokalt (tredjepartsverktyg) |
| `gh api` | Interagera med GitHub API |

------------------------------------------------------------

## Referenser

- GitHub Actions Documentation - docs.github.com/actions
- Actions Marketplace - github.com/marketplace?type=actions
- GitHub Actions Toolkit - github.com/actions/toolkit
- act - Local workflow runner - github.com/nektos/act
- GitHub Skills - skills.github.com för interaktiva kurser
""",
        },
        {
            "order_index": 3,
            "title": "GitLab CI/CD",
            "slug": "gitlab-cicd",
            "difficulty": "beginner",
            "content": """# GitLab CI/CD

------------------------------------------------------------

## Introduktion

Föreställ dig att du har ett GitLab-repo där varje push automatiskt bygger, testar och deployar din applikation - utan att du behöver konfigurera externa tjänster. GitLab CI/CD ger dig denna kraftfulla all-in-one-plattform direkt integrerad i din Git-hosting.

I denna modul lär du dig att behärska GitLab CI/CD - från grundläggande pipelines till avancerade funktioner som Auto DevOps, environments och review apps.

### Lärandemål

Efter denna modul kommer du att:

- Förstå GitLab CI/CD-arkitektur och hur den skiljer sig från andra CI/CD-verktyg
- Kunna skapa och konfigurera .gitlab-ci.yml för dina projekt
- Behärska stages, jobs, artifacts och cache
- Implementera multi-environment deployments med GitLab Environments
- Använda GitLab Runner för att köra dina pipelines

------------------------------------------------------------

## Teori

### Varför GitLab CI/CD?

GitLab CI/CD är GitLabs inbyggda CI/CD-plattform som erbjuder en komplett DevOps-lösning från planering till produktion.

**Viktiga fördelar:**

| Fördel | Beskrivning |
|--------|-------------|
| **All-in-one** | Git, CI/CD, Container Registry, och mer i samma plattform |
| **DevSecOps** | Integrerad säkerhetsskanning (SAST, DAST, dependency scanning) |
| **Auto DevOps** | Automatisk CI/CD utan konfiguration för standardprojekt |
| **Environments** | Inbyggd miljöhantering med review apps |
| **DAG Support** | Directed Acyclic Graph för komplexa pipeline-dependencies |

### Arkitektur

GitLab CI/CD består av flera sammankopplade komponenter:

```
+------------------------------------------------------------------+
|                    GITLAB CI/CD ARKITEKTUR                       |
+------------------------------------------------------------------+
|                                                                  |
|   [GitLab Server]                                                |
|        |                                                         |
|        v                                                         |
|   .gitlab-ci.yml (repo root)                                     |
|        |                                                         |
|        v                                                         |
|   +--PIPELINE--------------------------------------------+       |
|   |                                                      |       |
|   |   +--STAGE: build--+  +--STAGE: test--+             |       |
|   |   |                |  |               |             |       |
|   |   | [job: build]   |  | [job: unit]   |             |       |
|   |   | [job: compile] |  | [job: lint]   |             |       |
|   |   |                |  | [job: e2e]    |             |       |
|   |   +----------------+  +---------------+             |       |
|   |                                                      |       |
|   +------------------------------------------------------+       |
|        |                                                         |
|        v                                                         |
|   [GitLab Runners] (Shared / Specific / Group)                   |
|        |                                                         |
|        v                                                         |
|   [Executor: Docker / Shell / Kubernetes]                        |
|                                                                  |
+------------------------------------------------------------------+
```

### Nyckelkoncept

| Koncept | Beskrivning |
|---------|-------------|
| **Pipeline** | Komplett körning av alla stages och jobs för en commit |
| **Stage** | Grupp av jobs som körs parallellt (t.ex. build, test, deploy) |
| **Job** | Individuell uppgift med script som körs av en Runner |
| **Runner** | Agent som exekverar jobs (shared, group, eller project-specific) |
| **Artifacts** | Filer som sparas mellan jobs/stages |
| **Cache** | Filer som cachas mellan pipeline-körningar |

### GitLab vs GitHub Actions

| Aspekt | GitLab CI/CD | GitHub Actions |
|--------|--------------|----------------|
| Konfiguration | .gitlab-ci.yml | .github/workflows/*.yml |
| Parallel jobs | Implicit per stage | Explicit med matrix |
| Dependencies | needs: keyword | needs: keyword |
| Runners | Self-hosted eller Shared | Self-hosted eller GitHub-hosted |
| Environments | Native support | Environment protection rules |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Din första .gitlab-ci.yml

Skapa filen `.gitlab-ci.yml` i projektets rot:

```yaml
# .gitlab-ci.yml - Din första GitLab pipeline
stages:
  - build
  - test
  - deploy

variables:
  APP_NAME: "min-app"
  NODE_VERSION: "20"

# Build stage
build-job:
  stage: build
  image: node:${NODE_VERSION}
  script:
    - echo "Bygger $APP_NAME..."
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

# Test stage
test-job:
  stage: test
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm test
  coverage: '/Coverage: (\d+\.\d+)%/'

# Deploy stage
deploy-job:
  stage: deploy
  script:
    - echo "Deployar till produktion..."
  only:
    - main
  environment:
    name: production
    url: https://example.com
```

### Steg 2: Konfigurera artifacts och cache

```yaml
# Optimerad pipeline med cache och artifacts
stages:
  - install
  - build
  - test

# Global cache för alla jobs
cache:
  key:
    files:
      - package-lock.json
  paths:
    - node_modules/

install-dependencies:
  stage: install
  image: node:20
  script:
    - npm ci
  cache:
    key:
      files:
        - package-lock.json
    paths:
      - node_modules/
    policy: push              # Endast skriv till cache

build-app:
  stage: build
  image: node:20
  script:
    - npm run build
  cache:
    policy: pull              # Endast läs från cache
  artifacts:
    paths:
      - dist/
      - build/
    expire_in: 1 week
    when: on_success

test-unit:
  stage: test
  image: node:20
  script:
    - npm test
  cache:
    policy: pull
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

### Steg 3: Implementera needs (DAG)

```yaml
# Använd needs för att skapa dependency graph
stages:
  - build
  - test
  - deploy

build-frontend:
  stage: build
  script:
    - cd frontend && npm run build
  artifacts:
    paths:
      - frontend/dist/

build-backend:
  stage: build
  script:
    - cd backend && npm run build
  artifacts:
    paths:
      - backend/dist/

test-frontend:
  stage: test
  needs:
    - build-frontend          # Väntar endast på frontend build
  script:
    - cd frontend && npm test

test-backend:
  stage: test
  needs:
    - build-backend           # Väntar endast på backend build
  script:
    - cd backend && npm test

integration-test:
  stage: test
  needs:
    - build-frontend
    - build-backend           # Väntar på båda builds
  script:
    - npm run test:integration

deploy:
  stage: deploy
  needs:
    - test-frontend
    - test-backend
    - integration-test        # Väntar på alla tester
  script:
    - ./deploy.sh
```

### Steg 4: Rules och villkorlig körning

```yaml
# Modern syntax med rules (ersätter only/except)
build:
  script:
    - npm run build
  rules:
    # Kör för merge requests
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: always
    # Kör för main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: always
    # Kör för tags
    - if: '$CI_COMMIT_TAG'
      when: always
    # Annars kör inte
    - when: never

test:
  script:
    - npm test
  rules:
    # Kör endast om relevanta filer ändrats
    - changes:
        - src/**/*
        - tests/**/*
        - package.json

deploy-staging:
  script:
    - ./deploy.sh staging
  rules:
    - if: '$CI_COMMIT_BRANCH == "develop"'
      when: always

deploy-production:
  script:
    - ./deploy.sh production
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual            # Manuell godkännande
      allow_failure: false
```

### Steg 5: Environments och review apps

```yaml
# Multi-environment deployment
stages:
  - build
  - test
  - review
  - staging
  - production

# Review app för varje merge request
review:
  stage: review
  script:
    - ./deploy.sh review-$CI_MERGE_REQUEST_IID
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    url: https://review-$CI_MERGE_REQUEST_IID.example.com
    on_stop: stop-review
    auto_stop_in: 1 week
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'

stop-review:
  stage: review
  script:
    - ./teardown.sh review-$CI_MERGE_REQUEST_IID
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    action: stop
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: manual

deploy-staging:
  stage: staging
  script:
    - ./deploy.sh staging
  environment:
    name: staging
    url: https://staging.example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-production:
  stage: production
  script:
    - ./deploy.sh production
  environment:
    name: production
    url: https://example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
  needs:
    - deploy-staging
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Fullständig Node.js pipeline

```yaml
# Komplett CI/CD för Node.js-projekt
stages:
  - install
  - quality
  - build
  - test
  - deploy

variables:
  NODE_VERSION: "20"
  NPM_CONFIG_CACHE: "$CI_PROJECT_DIR/.npm"

# Global cache
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .npm/
    - node_modules/

# Templates
.node-base:
  image: node:${NODE_VERSION}
  before_script:
    - npm ci --cache .npm --prefer-offline

# Install
install:
  extends: .node-base
  stage: install
  script:
    - npm ci
  cache:
    policy: push

# Quality checks
lint:
  extends: .node-base
  stage: quality
  needs: []
  script:
    - npm run lint

type-check:
  extends: .node-base
  stage: quality
  needs: []
  script:
    - npm run type-check

security-audit:
  extends: .node-base
  stage: quality
  needs: []
  script:
    - npm audit --audit-level=high
  allow_failure: true

# Build
build:
  extends: .node-base
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 day

# Tests
test-unit:
  extends: .node-base
  stage: test
  needs:
    - build
  script:
    - npm run test:unit -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

test-e2e:
  extends: .node-base
  stage: test
  needs:
    - build
  services:
    - name: postgres:15
      alias: db
  variables:
    DATABASE_URL: "postgresql://postgres:postgres@db:5432/test"
  script:
    - npm run test:e2e

# Deploy
deploy-staging:
  stage: deploy
  needs:
    - test-unit
    - test-e2e
  script:
    - apt-get update && apt-get install -y rsync
    - rsync -avz dist/ user@staging:/var/www/app/
  environment:
    name: staging
    url: https://staging.example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-production:
  stage: deploy
  needs:
    - deploy-staging
  script:
    - rsync -avz dist/ user@production:/var/www/app/
  environment:
    name: production
    url: https://example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
```

### Exempel 2: Docker-baserad pipeline

```yaml
# Docker build och push pipeline
stages:
  - build
  - test
  - scan
  - push
  - deploy

variables:
  DOCKER_HOST: tcp://docker:2376
  DOCKER_TLS_CERTDIR: "/certs"
  DOCKER_TLS_VERIFY: 1
  DOCKER_CERT_PATH: "$DOCKER_TLS_CERTDIR/client"
  IMAGE_NAME: $CI_REGISTRY_IMAGE
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA

services:
  - docker:24.0.5-dind

build-image:
  stage: build
  image: docker:24.0.5
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
    - docker save $IMAGE_NAME:$IMAGE_TAG > image.tar
  artifacts:
    paths:
      - image.tar
    expire_in: 1 hour

test-image:
  stage: test
  image: docker:24.0.5
  script:
    - docker load < image.tar
    - docker run --rm $IMAGE_NAME:$IMAGE_TAG npm test

scan-image:
  stage: scan
  image: docker:24.0.5
  script:
    - docker load < image.tar
    - apk add --no-cache curl
    - curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $IMAGE_NAME:$IMAGE_TAG
  allow_failure: true

push-image:
  stage: push
  image: docker:24.0.5
  script:
    - docker load < image.tar
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker push $IMAGE_NAME:$IMAGE_TAG
    - docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
    - docker push $IMAGE_NAME:latest
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-k8s:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/app app=$IMAGE_NAME:$IMAGE_TAG
    - kubectl rollout status deployment/app
  environment:
    name: production
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
```

### Exempel 3: Monorepo med includes

```yaml
# Huvudfil: .gitlab-ci.yml
include:
  - local: '/apps/frontend/.gitlab-ci.yml'
  - local: '/apps/backend/.gitlab-ci.yml'
  - local: '/apps/api/.gitlab-ci.yml'
  - project: 'company/ci-templates'
    ref: main
    file: '/templates/security.yml'

stages:
  - install
  - build
  - test
  - deploy

variables:
  DOCKER_BUILDKIT: 1

# Global workflow rules
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH && $CI_OPEN_MERGE_REQUESTS'
      when: never
    - if: '$CI_COMMIT_BRANCH'

# Template som används av alla appar
.app-base:
  cache:
    key: ${CI_COMMIT_REF_SLUG}-${CI_PROJECT_DIR}
    paths:
      - node_modules/
```

```yaml
# apps/frontend/.gitlab-ci.yml
frontend-build:
  extends: .app-base
  stage: build
  script:
    - cd apps/frontend && npm run build
  artifacts:
    paths:
      - apps/frontend/dist/
  rules:
    - changes:
        - apps/frontend/**/*
        - packages/shared/**/*

frontend-test:
  extends: .app-base
  stage: test
  needs:
    - frontend-build
  script:
    - cd apps/frontend && npm test
  rules:
    - changes:
        - apps/frontend/**/*
        - packages/shared/**/*
```

------------------------------------------------------------

## Bästa Praxis

### Pipeline-design

```yaml
# BRA: Optimerad pipeline med DAG och parallella jobs
stages:
  - prepare
  - build
  - test
  - deploy

install:
  stage: prepare
  script:
    - npm ci
  cache:
    policy: push

lint:
  stage: build
  needs: []              # Kör direkt, vänta inte på prepare
  script:
    - npm run lint

build:
  stage: build
  needs:
    - install
  script:
    - npm run build
  artifacts:
    paths:
      - dist/

test-unit:
  stage: test
  needs:
    - install           # Behöver bara dependencies
  script:
    - npm run test:unit

test-integration:
  stage: test
  needs:
    - build             # Behöver build artifacts
  script:
    - npm run test:integration
```

### Cache-strategi

```yaml
# Optimal cache-konfiguration
variables:
  NPM_CONFIG_CACHE: "$CI_PROJECT_DIR/.npm"

cache:
  key:
    files:
      - package-lock.json    # Cache key baserat på lockfile
    prefix: ${CI_JOB_NAME}   # Unik per job-typ
  paths:
    - .npm/
    - node_modules/
  policy: pull-push

# Job som endast läser cache
test:
  cache:
    policy: pull            # Snabbare, skriver inte till cache
```

### Säkerhet

```yaml
# Säker hantering av secrets
variables:
  # Använd CI/CD Variables istället för hårdkodade värden
  DEPLOY_USER: $DEPLOY_USER
  # Masked variables visas inte i loggar

deploy:
  script:
    # Använd file-type variables för certifikat
    - echo "$DEPLOY_KEY" > /tmp/deploy.key
    - chmod 600 /tmp/deploy.key
    - ssh -i /tmp/deploy.key $DEPLOY_USER@server
  after_script:
    # Städa upp känsliga filer
    - rm -f /tmp/deploy.key
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Cache fungerar inte

```yaml
# FEL: Cache key är för generell
cache:
  key: "$CI_COMMIT_REF_SLUG"    # Ändras för varje branch
  paths:
    - node_modules/

# RÄTT: Cache key baserad på dependencies
cache:
  key:
    files:
      - package-lock.json       # Ändras endast när deps ändras
  paths:
    - node_modules/
```

### Problem 2: Jobs körs i fel ordning

```yaml
# FEL: Förlitar sig på stage-ordning
test:
  stage: test
  script:
    - npm test                  # Kraschar om build inte körts

# RÄTT: Explicit dependency med needs
test:
  stage: test
  needs:
    - build                     # Garanterar att build körs först
  script:
    - npm test
```

### Problem 3: Pipeline blockas av manuella jobs

```yaml
# FEL: Manuellt job blockar hela pipeline
deploy:
  when: manual
  script:
    - ./deploy.sh

# RÄTT: allow_failure för att inte blockera
deploy:
  when: manual
  allow_failure: true           # Pipeline markeras som lyckad
  script:
    - ./deploy.sh
```

### Problem 4: Artifacts försvinner

```yaml
# FEL: Artifacts går ut för snabbt
build:
  artifacts:
    paths:
      - dist/
    # Ingen expire_in = default 30 dagar

# RÄTT: Explicit expire_in
build:
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
    when: on_success            # Spara endast vid lyckad build
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande Pipeline

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en komplett CI/CD pipeline för ett Node.js-projekt.

**Uppgift:**

1. Skapa `.gitlab-ci.yml` med stages: install, lint, build, test
2. Implementera cache för node_modules
3. Lägg till artifacts för build output
4. Konfigurera code coverage reporting

**Förväntad lösning:**

```yaml
stages:
  - install
  - lint
  - build
  - test

variables:
  NODE_VERSION: "20"

cache:
  key:
    files:
      - package-lock.json
  paths:
    - node_modules/

install:
  stage: install
  image: node:${NODE_VERSION}
  script:
    - npm ci

lint:
  stage: lint
  image: node:${NODE_VERSION}
  needs:
    - install
  script:
    - npm run lint

build:
  stage: build
  image: node:${NODE_VERSION}
  needs:
    - install
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 day

test:
  stage: test
  image: node:${NODE_VERSION}
  needs:
    - install
  script:
    - npm test -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

</details>

### Övning 2: Multi-Environment Deployment

<details>
<summary>Visa övning</summary>

**Mål:** Implementera deployments till staging och production med environments.

**Uppgift:**

1. Skapa review apps för merge requests
2. Automatisk deploy till staging vid merge till main
3. Manuell deploy till production med approval
4. Konfigurera environment URLs och auto_stop

**Förväntad lösning:**

```yaml
stages:
  - build
  - test
  - review
  - staging
  - production

build:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  needs:
    - build
  script:
    - npm test

# Review app för MRs
review:
  stage: review
  script:
    - ./scripts/deploy.sh review-$CI_MERGE_REQUEST_IID
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    url: https://review-$CI_MERGE_REQUEST_IID.example.com
    on_stop: stop-review
    auto_stop_in: 3 days
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'

stop-review:
  stage: review
  script:
    - ./scripts/teardown.sh review-$CI_MERGE_REQUEST_IID
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    action: stop
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: manual

# Auto-deploy till staging
deploy-staging:
  stage: staging
  needs:
    - test
  script:
    - ./scripts/deploy.sh staging
  environment:
    name: staging
    url: https://staging.example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

# Manuell deploy till production
deploy-production:
  stage: production
  needs:
    - deploy-staging
  script:
    - ./scripts/deploy.sh production
  environment:
    name: production
    url: https://example.com
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
```

</details>

### Övning 3: Docker Pipeline med Security Scanning

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en Docker-pipeline med container scanning och säker image-hantering.

**Uppgift:**

1. Bygg Docker image med GitLab Container Registry
2. Kör container security scanning med Trivy
3. Push endast säkra images (inga CRITICAL vulnerabilities)
4. Tagga images med commit SHA och semantic version

**Förväntad lösning:**

```yaml
stages:
  - build
  - scan
  - push
  - deploy

variables:
  IMAGE_NAME: $CI_REGISTRY_IMAGE
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA

services:
  - docker:24.0.5-dind

build-image:
  stage: build
  image: docker:24.0.5
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
    - docker save $IMAGE_NAME:$IMAGE_TAG > image.tar
  artifacts:
    paths:
      - image.tar
    expire_in: 2 hours

scan-container:
  stage: scan
  image: docker:24.0.5
  needs:
    - build-image
  script:
    - docker load < image.tar
    - apk add --no-cache curl
    - curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
    - trivy image --exit-code 0 --severity LOW,MEDIUM $IMAGE_NAME:$IMAGE_TAG
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $IMAGE_NAME:$IMAGE_TAG
  artifacts:
    reports:
      container_scanning: gl-container-scanning-report.json

push-image:
  stage: push
  image: docker:24.0.5
  needs:
    - scan-container
  script:
    - docker load < image.tar
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker push $IMAGE_NAME:$IMAGE_TAG
    # Tagga med semantic version för tags
    - |
      if [ -n "$CI_COMMIT_TAG" ]; then
        docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:$CI_COMMIT_TAG
        docker push $IMAGE_NAME:$CI_COMMIT_TAG
      fi
    # Tagga latest för main branch
    - |
      if [ "$CI_COMMIT_BRANCH" == "main" ]; then
        docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
        docker push $IMAGE_NAME:latest
      fi
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_TAG'

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  needs:
    - push-image
  script:
    - kubectl set image deployment/app app=$IMAGE_NAME:$IMAGE_TAG
    - kubectl rollout status deployment/app --timeout=300s
  environment:
    name: production
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
```

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **GitHub Actions** | Jämförelse av syntax och funktioner |
| **Docker** | Container-baserade jobs och image building |
| **Kubernetes** | Deploy till K8s med GitLab Agent |
| **Testing** | Integrerade test reports och coverage |
| **Security** | SAST, DAST, och dependency scanning |

------------------------------------------------------------

## Sammanfattning

GitLab CI/CD erbjuder en kraftfull, integrerad CI/CD-plattform med unika fördelar:

**Styrkor:**
- All-in-one plattform - Git, CI/CD, Registry, Security
- DAG-baserade pipelines med needs keyword
- Native environment och review app support
- Auto DevOps för snabbstart

**Nyckelkoncept:**
- .gitlab-ci.yml definierar hela pipelinen
- Stages grupperar jobs, jobs körs parallellt inom stage
- needs skapar explicit DAG för beroenden
- rules ersätter gamla only/except syntax
- Environments ger deployment tracking och rollback

------------------------------------------------------------

## Nyckelkommandon

| Syntax | Beskrivning |
|--------|-------------|
| `stages:` | Definiera pipeline stages |
| `image:` | Docker image för job |
| `script:` | Kommandon att köra |
| `needs:` | Job dependencies (DAG) |
| `rules:` | Villkor för när job körs |
| `artifacts:` | Filer att spara |
| `cache:` | Dependencies att cacha |
| `environment:` | Deployment miljö |
| `extends:` | Ärv från template |
| `include:` | Inkludera externa filer |

------------------------------------------------------------

## Referenser

- GitLab CI/CD Documentation - docs.gitlab.com/ee/ci
- .gitlab-ci.yml Reference - docs.gitlab.com/ee/ci/yaml
- GitLab Runner - docs.gitlab.com/runner
- Predefined Variables - docs.gitlab.com/ee/ci/variables/predefined_variables.html
- Auto DevOps - docs.gitlab.com/ee/topics/autodevops
""",
        },
        {
            "order_index": 4,
            "title": "Jenkins Pipelines",
            "slug": "jenkins-pipelines",
            "difficulty": "intermediate",
            "content": """# Jenkins Pipelines

------------------------------------------------------------

## Introduktion

Föreställ dig att du arbetar på ett företag med hundratals projekt och behöver ett CI/CD-system som kan anpassas till varje unik situation. Jenkins har varit branschstandard i över ett decennium och erbjuder oöverträffad flexibilitet genom sin plugin-arkitektur och Groovy-baserade pipelines.

I denna modul lär du dig att behärska Jenkins Pipelines - från grundläggande Declarative Pipelines till avancerade Scripted Pipelines och Shared Libraries.

### Lärandemål

Efter denna modul kommer du att:

- Förstå skillnaden mellan Declarative och Scripted Pipelines
- Kunna skapa och konfigurera Jenkinsfile för dina projekt
- Behärska agents, stages, parallel execution och post-actions
- Implementera säker credential-hantering
- Använda Shared Libraries för återanvändbar pipeline-kod

------------------------------------------------------------

## Teori

### Varför Jenkins?

Jenkins är världens mest populära självhostade CI/CD-server med en enorm community och plugin-ekosystem.

**Viktiga fördelar:**

| Fördel | Beskrivning |
|--------|-------------|
| **Flexibilitet** | Mest anpassningsbara CI/CD-verktyget |
| **Plugin-ekosystem** | 1800+ plugins för integration med nästan allt |
| **Self-hosted** | Full kontroll över infrastruktur och data |
| **Enterprise-proven** | Används av Fortune 500-företag |
| **Groovy-power** | Programmatisk logik för komplexa workflows |

### Pipeline-typer

Jenkins erbjuder två huvudtyper av pipelines:

```
+------------------------------------------------------------------+
|                    JENKINS PIPELINE-TYPER                        |
+------------------------------------------------------------------+
|                                                                  |
|   DECLARATIVE PIPELINE (Rekommenderad)                           |
|   +----------------------------------------------------------+   |
|   | pipeline {                                               |   |
|   |     agent any                                            |   |
|   |     stages {                                             |   |
|   |         stage('Build') { steps { sh 'make' } }           |   |
|   |     }                                                    |   |
|   | }                                                        |   |
|   +----------------------------------------------------------+   |
|   - Strukturerad, läsbar syntax                                  |
|   - Enkel att komma igång med                                    |
|   - Validering av syntax innan körning                           |
|                                                                  |
|   SCRIPTED PIPELINE (Avancerad)                                  |
|   +----------------------------------------------------------+   |
|   | node {                                                   |   |
|   |     stage('Build') {                                     |   |
|   |         sh 'make'                                        |   |
|   |     }                                                    |   |
|   | }                                                        |   |
|   +----------------------------------------------------------+   |
|   - Full Groovy-programmering                                    |
|   - Maximum flexibilitet                                         |
|   - Bättre för komplexa logiska flöden                           |
|                                                                  |
+------------------------------------------------------------------+
```

### Arkitektur

| Komponent | Beskrivning |
|-----------|-------------|
| **Jenkins Controller** | Huvudserver som schemalägger och koordinerar |
| **Agents/Nodes** | Maskiner som exekverar jobs |
| **Executor** | Process-slot på en agent |
| **Workspace** | Arbetskatalog för build |
| **Jenkinsfile** | Pipeline-definition i kod |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Din första Declarative Pipeline

Skapa en fil `Jenkinsfile` i projektets rot:

```groovy
// Jenkinsfile - Din första Jenkins Pipeline
pipeline {
    agent any

    environment {
        APP_NAME = 'min-app'
        NODE_VERSION = '20'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Bygger ${APP_NAME}..."
            }
        }

        stage('Install') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results/**/*.xml'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deployar till produktion...'
                sh './scripts/deploy.sh'
            }
        }
    }

    post {
        success {
            echo 'Pipeline lyckades!'
        }
        failure {
            echo 'Pipeline misslyckades!'
        }
        always {
            cleanWs()
        }
    }
}
```

### Steg 2: Agent-konfiguration

```groovy
pipeline {
    // Global agent - används om stage inte definierar egen
    agent any

    stages {
        stage('Build med Docker') {
            // Stage-specifik agent med Docker
            agent {
                docker {
                    image 'node:20'
                    args '-v /tmp:/tmp -u root'
                }
            }
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }

        stage('Test med specifik nod') {
            // Agent med label
            agent {
                label 'linux && docker'
            }
            steps {
                sh 'npm test'
            }
        }

        stage('Deploy') {
            // Kör på master/controller
            agent {
                label 'master'
            }
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

### Steg 3: Parallell exekvering

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm ci && npm run build'
            }
        }

        stage('Test - Parallell') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'npm run test:unit'
                    }
                    post {
                        always {
                            junit 'test-results/unit/*.xml'
                        }
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'npm run test:integration'
                    }
                    post {
                        always {
                            junit 'test-results/integration/*.xml'
                        }
                    }
                }
                stage('E2E Tests') {
                    agent {
                        docker {
                            image 'cypress/browsers:latest'
                        }
                    }
                    steps {
                        sh 'npm run test:e2e'
                    }
                    post {
                        always {
                            archiveArtifacts artifacts: 'cypress/screenshots/**/*', allowEmptyArchive: true
                        }
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'npm audit --audit-level=high'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                allOf {
                    branch 'main'
                    expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
                }
            }
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

### Steg 4: Credential-hantering

```groovy
pipeline {
    agent any

    environment {
        // Username/Password credentials
        AWS_CREDENTIALS = credentials('aws-credentials-id')
        // Secret text
        API_TOKEN = credentials('api-token-id')
        // Secret file
        KUBECONFIG = credentials('kubeconfig-file')
    }

    stages {
        stage('Deploy till AWS') {
            steps {
                // AWS_CREDENTIALS_USR och AWS_CREDENTIALS_PSW sätts automatiskt
                sh '''
                    export AWS_ACCESS_KEY_ID=$AWS_CREDENTIALS_USR
                    export AWS_SECRET_ACCESS_KEY=$AWS_CREDENTIALS_PSW
                    aws s3 sync dist/ s3://my-bucket/
                '''
            }
        }

        stage('Deploy till K8s') {
            steps {
                // Använd secret file
                sh '''
                    export KUBECONFIG=$KUBECONFIG
                    kubectl apply -f k8s/
                '''
            }
        }

        stage('SSH Deploy') {
            steps {
                // SSH Agent plugin
                sshagent(['deploy-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@server "
                            cd /app &&
                            git pull &&
                            docker compose up -d
                        "
                    '''
                }
            }
        }

        stage('Med withCredentials') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push myimage:latest
                    '''
                }
            }
        }
    }
}
```

### Steg 5: Input och godkännanden

```groovy
pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['staging', 'production'],
            description: 'Välj deployment-miljö'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: 'Hoppa över tester'
        )
        string(
            name: 'VERSION',
            defaultValue: 'latest',
            description: 'Version att deploya'
        )
    }

    stages {
        stage('Test') {
            when {
                expression { params.SKIP_TESTS == false }
            }
            steps {
                sh 'npm test'
            }
        }

        stage('Deploy till Staging') {
            when {
                expression { params.ENVIRONMENT == 'staging' }
            }
            steps {
                sh "./deploy.sh staging ${params.VERSION}"
            }
        }

        stage('Godkänn Production') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                // Manuellt godkännande
                input message: 'Godkänn deploy till produktion?',
                      ok: 'Deploy!',
                      submitter: 'admin,release-team'
            }
        }

        stage('Deploy till Production') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                sh "./deploy.sh production ${params.VERSION}"
            }
        }
    }
}
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Fullständig CI/CD Pipeline

```groovy
// Komplett Jenkinsfile för Node.js-projekt
pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        DOCKER_REGISTRY = 'registry.example.com'
        IMAGE_NAME = "${DOCKER_REGISTRY}/myapp"
        IMAGE_TAG = "${env.BUILD_NUMBER}-${env.GIT_COMMIT?.take(7)}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    env.GIT_COMMIT = sh(
                        script: 'git rev-parse HEAD',
                        returnStdout: true
                    ).trim()
                }
            }
        }

        stage('Install & Build') {
            agent {
                docker {
                    image 'node:20'
                    reuseNode true
                }
            }
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }

        stage('Quality Gates') {
            parallel {
                stage('Lint') {
                    agent {
                        docker {
                            image 'node:20'
                            reuseNode true
                        }
                    }
                    steps {
                        sh 'npm run lint'
                    }
                }
                stage('Unit Tests') {
                    agent {
                        docker {
                            image 'node:20'
                            reuseNode true
                        }
                    }
                    steps {
                        sh 'npm run test:unit -- --coverage'
                    }
                    post {
                        always {
                            junit 'test-results/unit/*.xml'
                            publishHTML(target: [
                                reportDir: 'coverage',
                                reportFiles: 'index.html',
                                reportName: 'Coverage Report'
                            ])
                        }
                    }
                }
                stage('Security Audit') {
                    steps {
                        sh 'npm audit --audit-level=high || true'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push to Registry') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-registry',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo $DOCKER_PASS | docker login $DOCKER_REGISTRY -u $DOCKER_USER --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh "./scripts/deploy.sh staging ${IMAGE_TAG}"
            }
        }

        stage('Deploy Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy till produktion?', ok: 'Deploy!'
                sh "./scripts/deploy.sh production ${IMAGE_TAG}"
            }
        }
    }

    post {
        success {
            slackSend(
                color: 'good',
                message: "Build ${env.BUILD_NUMBER} lyckades: ${env.BUILD_URL}"
            )
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Build ${env.BUILD_NUMBER} misslyckades: ${env.BUILD_URL}"
            )
        }
        always {
            cleanWs()
        }
    }
}
```

### Exempel 2: Shared Library

```groovy
// vars/standardPipeline.groovy (i shared library repo)
def call(Map config = [:]) {
    def nodeVersion = config.nodeVersion ?: '20'
    def deployEnv = config.deployEnv ?: 'staging'

    pipeline {
        agent any

        stages {
            stage('Setup') {
                steps {
                    script {
                        echo "Använder Node ${nodeVersion}"
                    }
                }
            }

            stage('Build') {
                agent {
                    docker {
                        image "node:${nodeVersion}"
                        reuseNode true
                    }
                }
                steps {
                    sh 'npm ci'
                    sh 'npm run build'
                }
            }

            stage('Test') {
                agent {
                    docker {
                        image "node:${nodeVersion}"
                        reuseNode true
                    }
                }
                steps {
                    sh 'npm test'
                }
            }

            stage('Deploy') {
                when {
                    branch 'main'
                }
                steps {
                    script {
                        deploy(environment: deployEnv)
                    }
                }
            }
        }
    }
}

// vars/deploy.groovy
def call(Map config = [:]) {
    def env = config.environment

    withCredentials([
        usernamePassword(
            credentialsId: "${env}-deploy-creds",
            usernameVariable: 'DEPLOY_USER',
            passwordVariable: 'DEPLOY_PASS'
        )
    ]) {
        sh "./scripts/deploy.sh ${env}"
    }
}

// Jenkinsfile (i projekt som använder library)
@Library('my-shared-library') _

standardPipeline(
    nodeVersion: '20',
    deployEnv: 'production'
)
```

### Exempel 3: Multibranch med Feature Flags

```groovy
// Multibranch Pipeline Jenkinsfile
pipeline {
    agent any

    environment {
        BRANCH_TYPE = getBranchType(env.BRANCH_NAME)
    }

    stages {
        stage('Build') {
            steps {
                sh 'npm ci && npm run build'
            }
        }

        stage('Test') {
            parallel {
                stage('Unit') {
                    steps { sh 'npm run test:unit' }
                }
                stage('Integration') {
                    when {
                        expression { env.BRANCH_TYPE != 'feature' }
                    }
                    steps { sh 'npm run test:integration' }
                }
            }
        }

        stage('Deploy Dev') {
            when {
                expression { env.BRANCH_TYPE == 'feature' }
            }
            steps {
                sh "./deploy.sh dev-${env.BRANCH_NAME}"
            }
        }

        stage('Deploy Staging') {
            when {
                expression { env.BRANCH_TYPE == 'develop' }
            }
            steps {
                sh './deploy.sh staging'
            }
        }

        stage('Deploy Production') {
            when {
                expression { env.BRANCH_TYPE == 'main' }
            }
            steps {
                input 'Deploy till produktion?'
                sh './deploy.sh production'
            }
        }
    }
}

// Groovy funktion för branch-typ
def getBranchType(branchName) {
    if (branchName == 'main' || branchName == 'master') {
        return 'main'
    } else if (branchName == 'develop') {
        return 'develop'
    } else if (branchName.startsWith('feature/')) {
        return 'feature'
    } else if (branchName.startsWith('hotfix/')) {
        return 'hotfix'
    }
    return 'other'
}
```

------------------------------------------------------------

## Bästa Praxis

### Pipeline som kod

```groovy
// BRA: Allt i version control
// Jenkinsfile i repo-root
pipeline {
    agent any
    // ...
}

// BRA: Externalisera scripts
stage('Deploy') {
    steps {
        sh './scripts/deploy.sh'  // Script i repo
    }
}

// UNDVIK: Hårdkodad logik i pipeline
// Lägg komplex logik i externa scripts istället
```

### Timeouts och felhantering

```groovy
pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')      // Global timeout
        retry(2)                                  // Försök igen vid fel
    }

    stages {
        stage('Flaky Test') {
            options {
                timeout(time: 10, unit: 'MINUTES')  // Stage-specifik
                retry(3)
            }
            steps {
                sh 'npm run test:e2e'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    try {
                        sh './deploy.sh'
                    } catch (Exception e) {
                        echo "Deploy misslyckades: ${e.message}"
                        // Rollback
                        sh './rollback.sh'
                        throw e
                    }
                }
            }
        }
    }
}
```

### Workspace-hantering

```groovy
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)    // Manuell checkout
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()                // Rensa workspace först
                checkout scm
            }
        }
    }

    post {
        always {
            cleanWs(
                cleanWhenSuccess: true,
                cleanWhenFailure: false,  // Behåll vid fel för debug
                deleteDirs: true
            )
        }
    }
}
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Credentials läcker i loggar

```groovy
// FEL: Credentials kan visas i loggar
stage('Deploy') {
    steps {
        sh "curl -u ${API_TOKEN} https://api.example.com"
    }
}

// RÄTT: Använd mask och withCredentials
stage('Deploy') {
    steps {
        withCredentials([string(credentialsId: 'api-token', variable: 'TOKEN')]) {
            sh '''
                set +x
                curl -u $TOKEN https://api.example.com
            '''
        }
    }
}
```

### Problem 2: Pipeline hänger vid input

```groovy
// FEL: Input blockerar executor
stage('Approve') {
    steps {
        input 'Godkänn?'              // Blockerar agent
        sh './deploy.sh'
    }
}

// RÄTT: Input utanför agent-allokering
stage('Approve') {
    agent none                        // Ingen agent allokerad
    steps {
        input 'Godkänn?'
    }
}
stage('Deploy') {
    agent any                         // Agent allokeras efter input
    steps {
        sh './deploy.sh'
    }
}
```

### Problem 3: Groovy sandbox-begränsningar

```groovy
// FEL: Kan kräva admin-godkännande
stage('Process') {
    steps {
        script {
            new File('/etc/passwd').text  // Blocked av sandbox
        }
    }
}

// RÄTT: Använd Jenkins-steg
stage('Process') {
    steps {
        script {
            def content = readFile '/etc/passwd'
        }
    }
}
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande Pipeline

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en komplett Declarative Pipeline för ett Node.js-projekt.

**Uppgift:**

1. Skapa Jenkinsfile med stages: Install, Build, Test, Deploy
2. Använd Docker agent för Node.js
3. Lägg till parallella test-stages (unit, integration)
4. Implementera deploy endast för main branch

**Förväntad lösning:**

```groovy
pipeline {
    agent any

    stages {
        stage('Install') {
            agent {
                docker {
                    image 'node:20'
                    reuseNode true
                }
            }
            steps {
                sh 'npm ci'
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'node:20'
                    reuseNode true
                }
            }
            steps {
                sh 'npm run build'
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    agent {
                        docker {
                            image 'node:20'
                            reuseNode true
                        }
                    }
                    steps {
                        sh 'npm run test:unit'
                    }
                    post {
                        always {
                            junit 'test-results/unit/*.xml'
                        }
                    }
                }
                stage('Integration Tests') {
                    agent {
                        docker {
                            image 'node:20'
                            reuseNode true
                        }
                    }
                    steps {
                        sh 'npm run test:integration'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh './scripts/deploy.sh'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
```

</details>

### Övning 2: Credential-hantering

<details>
<summary>Visa övning</summary>

**Mål:** Implementera säker hantering av olika credential-typer.

**Uppgift:**

1. Konfigurera AWS credentials (username/password)
2. Konfigurera Docker registry credentials
3. Konfigurera SSH-nyckel för deploy
4. Säkerställ att credentials aldrig visas i loggar

**Förväntad lösning:**

```groovy
pipeline {
    agent any

    stages {
        stage('Push till ECR') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'aws-credentials',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    sh '''
                        set +x
                        aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
                        docker push $ECR_REGISTRY/myapp:latest
                    '''
                }
            }
        }

        stage('Push till Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        set +x
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push myorg/myapp:latest
                    '''
                }
            }
        }

        stage('Deploy via SSH') {
            steps {
                sshagent(['deploy-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no deploy@server "
                            cd /app &&
                            docker compose pull &&
                            docker compose up -d
                        "
                    '''
                }
            }
        }
    }
}
```

</details>

### Övning 3: Shared Library

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en Shared Library för återanvändbara pipeline-steg.

**Uppgift:**

1. Skapa en Shared Library med standardiserad build-pipeline
2. Inkludera konfigurerbara parametrar för Node version och deploy-miljö
3. Använd library i ett projekt-Jenkinsfile

**Förväntad lösning:**

```groovy
// vars/nodePipeline.groovy
def call(Map config = [:]) {
    def nodeVersion = config.nodeVersion ?: '20'
    def runTests = config.runTests != false
    def deployBranches = config.deployBranches ?: ['main']

    pipeline {
        agent any

        stages {
            stage('Build') {
                agent {
                    docker {
                        image "node:${nodeVersion}"
                        reuseNode true
                    }
                }
                steps {
                    sh 'npm ci'
                    sh 'npm run build'
                }
            }

            stage('Test') {
                when {
                    expression { runTests }
                }
                agent {
                    docker {
                        image "node:${nodeVersion}"
                        reuseNode true
                    }
                }
                steps {
                    sh 'npm test'
                }
            }

            stage('Deploy') {
                when {
                    expression {
                        deployBranches.contains(env.BRANCH_NAME)
                    }
                }
                steps {
                    script {
                        deployToEnvironment(
                            environment: config.deployEnv ?: 'staging'
                        )
                    }
                }
            }
        }
    }
}

// vars/deployToEnvironment.groovy
def call(Map config = [:]) {
    def env = config.environment

    withCredentials([
        usernamePassword(
            credentialsId: "${env}-deploy-creds",
            usernameVariable: 'DEPLOY_USER',
            passwordVariable: 'DEPLOY_PASS'
        )
    ]) {
        sh "./scripts/deploy.sh ${env}"
    }
}

// Jenkinsfile i projekt
@Library('my-company-library@main') _

nodePipeline(
    nodeVersion: '20',
    runTests: true,
    deployEnv: 'production',
    deployBranches: ['main', 'release/*']
)
```

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **GitHub Actions** | Modern alternativ - jämför syntax och koncept |
| **GitLab CI/CD** | Integrerad lösning vs separat CI-server |
| **Docker** | Container-baserade agents och builds |
| **Kubernetes** | Deploy till K8s-kluster |
| **Secrets Management** | Vault-integration för säkra credentials |

------------------------------------------------------------

## Sammanfattning

Jenkins Pipelines erbjuder oöverträffad flexibilitet för CI/CD:

**Styrkor:**
- Declarative Pipeline för strukturerad, läsbar syntax
- Scripted Pipeline för komplex programmatisk logik
- Enormt plugin-ekosystem
- Full kontroll med self-hosting

**Nyckelkoncept:**
- Jenkinsfile definierar pipeline som kod
- Agents bestämmer var stages körs
- parallel för concurrent execution
- credentials() för säker secret-hantering
- Shared Libraries för återanvändbar kod

------------------------------------------------------------

## Nyckelkommandon

| Syntax | Beskrivning |
|--------|-------------|
| `pipeline { }` | Declarative pipeline block |
| `agent any` | Kör på valfri tillgänglig agent |
| `agent { docker }` | Kör i Docker container |
| `stages { }` | Container för stages |
| `stage('Name') { }` | Definierar en stage |
| `steps { }` | Steg inom en stage |
| `parallel { }` | Parallella stages |
| `when { branch }` | Villkorlig körning |
| `post { always }` | Post-build actions |
| `credentials()` | Hämta credentials |

------------------------------------------------------------

## Referenser

- Jenkins Pipeline Documentation - jenkins.io/doc/book/pipeline
- Pipeline Syntax Reference - jenkins.io/doc/book/pipeline/syntax
- Shared Libraries - jenkins.io/doc/book/pipeline/shared-libraries
- Jenkins Plugins - plugins.jenkins.io
- Blue Ocean - jenkins.io/projects/blueocean
""",
        },
        {
            "order_index": 5,
            "title": "Testing in Pipelines",
            "slug": "testing-in-pipelines",
            "difficulty": "intermediate",
            "content": """# Testing in Pipelines

------------------------------------------------------------

## Introduktion

Föreställ dig att varje kodändring automatiskt valideras genom hundratals tester innan den når produktion. Automatiserade tester i CI/CD-pipelines är din första försvarslinje mot buggar och regressioner.

I denna modul lär du dig att implementera en komplett teststrategi i dina pipelines - från snabba unit-tester till omfattande end-to-end-tester.

### Lärandemål

Efter denna modul kommer du att:

- Förstå testpyramiden och hur den tillämpas i CI/CD
- Kunna implementera unit, integration och E2E-tester i pipelines
- Behärska parallella tester och sharding för snabbare körningar
- Konfigurera test-rapportering och code coverage
- Implementera säkerhetstester som en del av din pipeline

------------------------------------------------------------

## Teori

### Varför tester i CI/CD?

Automatiserade tester är fundamentet för kontinuerlig leverans med hög kvalitet.

**Viktiga fördelar:**

| Fördel | Beskrivning |
|--------|-------------|
| **Tidig upptäckt** | Fånga buggar innan de når produktion |
| **Dokumentation** | Tester beskriver förväntad funktionalitet |
| **Refaktorering** | Säkra ändringar med god testtäckning |
| **Förtroende** | Möjliggör kontinuerlig deployment |
| **Snabb feedback** | Automatiserad validering på minuter |

### Testpyramiden

Testpyramiden är en strategi för att balansera olika testtyper:

```
+------------------------------------------------------------------+
|                       TESTPYRAMIDEN                              |
+------------------------------------------------------------------+
|                                                                  |
|                          /\\                                      |
|                         /  \\                                     |
|                        / E2E\\          FÅ - Dyra, långsamma     |
|                       /      \\         Testar hela flödet        |
|                      /--------\\                                  |
|                     /          \\                                 |
|                    / Integration\\      MELLAN - Service-tester  |
|                   /              \\     API, databas, externa     |
|                  /----------------\\                              |
|                 /                  \\                             |
|                /    Unit Tests      \\  MÅNGA - Snabba, billiga  |
|               /                      \\ Testar enskilda funktioner|
|              /------------------------\\                          |
|                                                                  |
+------------------------------------------------------------------+

REKOMMENDERAD FÖRDELNING:
+------------------+--------+-----------+
| Typ              | Andel  | Körtid    |
+------------------+--------+-----------+
| Unit             | 70%    | Sekunder  |
| Integration      | 20%    | Minuter   |
| E2E              | 10%    | 5-15 min  |
+------------------+--------+-----------+
```

### Test-typer förklarade

| Test-typ | Vad testas | Exempel |
|----------|------------|---------|
| **Unit** | Enskilda funktioner/klasser | `calculateTotal()` returnerar rätt värde |
| **Integration** | Samverkan mellan komponenter | API + Databas fungerar tillsammans |
| **E2E** | Hela användarflödet | Användare kan logga in och köpa produkt |
| **Smoke** | Grundläggande funktionalitet | Applikationen startar och svarar |
| **Performance** | Hastighet och skalbarhet | Svarstid under 200ms vid 1000 req/s |
| **Security** | Sårbarheter | Inga kända CVEs i dependencies |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Unit-tester i pipeline

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout kod
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Installera dependencies
        run: npm ci

      - name: Kör unit-tester
        run: npm test -- --coverage --watchAll=false
        env:
          CI: true

      - name: Kontrollera coverage-tröskel
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          echo "Line coverage: $COVERAGE%"
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "::error::Coverage $COVERAGE% är under tröskeln 80%"
            exit 1
          fi

      - name: Ladda upp coverage till Codecov
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage/lcov.info
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}
```

### Steg 2: Integration-tester med services

```yaml
  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
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
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Kör databasmigrationer
        run: npm run db:migrate
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/testdb

      - name: Seed testdata
        run: npm run db:seed:test
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/testdb

      - name: Kör integration-tester
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/testdb
          REDIS_URL: redis://localhost:6379
          NODE_ENV: test
```

### Steg 3: E2E-tester med Playwright

```yaml
  e2e-tests:
    name: E2E Tests
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Installera dependencies
        run: npm ci

      - name: Installera Playwright browsers
        run: npx playwright install --with-deps chromium firefox

      - name: Bygg applikationen
        run: npm run build

      - name: Kör E2E-tester
        run: npx playwright test
        env:
          BASE_URL: http://localhost:3000
          CI: true

      - name: Ladda upp testartefakter
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: |
            playwright-report/
            test-results/
          retention-days: 7

      - name: Publicera testresultat
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-html-report
          path: playwright-report/
```

### Steg 4: Parallella tester med sharding

```yaml
  parallel-tests:
    name: Tests (Shard ${{ matrix.shard }})
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Kör tester (shard ${{ matrix.shard }}/4)
        run: npm test -- --shard=${{ matrix.shard }}/4 --coverage

      - name: Ladda upp coverage-data
        uses: actions/upload-artifact@v4
        with:
          name: coverage-${{ matrix.shard }}
          path: coverage/

  merge-coverage:
    name: Merge Coverage Reports
    needs: parallel-tests
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Ladda ner alla coverage-rapporter
        uses: actions/download-artifact@v4
        with:
          pattern: coverage-*
          path: coverage-reports/

      - name: Slå ihop coverage
        run: |
          npm install -g nyc
          npx nyc merge coverage-reports/ merged-coverage.json
          npx nyc report --reporter=lcov --reporter=text-summary

      - name: Ladda upp till Codecov
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage/lcov.info
```

### Steg 5: Säkerhetstester

```yaml
  security-tests:
    name: Security Scans
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      # Dependency scanning med npm audit
      - name: NPM Security Audit
        run: npm audit --audit-level=high
        continue-on-error: true

      # Snyk för djupare analys
      - name: Snyk Security Scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      # Secret scanning
      - name: Scan för hemligheter
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

      # SAST med CodeQL
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: javascript

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett test-workflow

```yaml
name: Complete Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  CI: true

jobs:
  # Snabba tester först för tidig feedback
  lint-and-typecheck:
    name: Lint & Type Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check

  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    needs: lint-and-typecheck
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    needs: lint-and-typecheck
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports: ['5432:5432']
        options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run db:migrate
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
      - run: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test

  e2e-tests:
    name: E2E Tests
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npx playwright install --with-deps chromium
      - run: npm run build
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/

  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: lint-and-typecheck
    steps:
      - uses: actions/checkout@v4
      - run: npm audit --audit-level=high
      - uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # Alla tester måste passera innan merge
  test-gate:
    name: Test Gate
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests, e2e-tests, security-scan]
    if: always()
    steps:
      - name: Kontrollera alla test-resultat
        run: |
          if [[ "${{ needs.unit-tests.result }}" != "success" ]] ||
             [[ "${{ needs.integration-tests.result }}" != "success" ]] ||
             [[ "${{ needs.e2e-tests.result }}" != "success" ]]; then
            echo "::error::En eller flera test-sviter misslyckades"
            exit 1
          fi
          echo "Alla tester passerade!"
```

### Exempel 2: Playwright E2E-konfiguration

```javascript
// playwright.config.js
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 4 : undefined,
  reporter: [
    ['html'],
    ['junit', { outputFile: 'test-results/junit.xml' }],
    process.env.CI ? ['github'] : ['list']
  ],

  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'mobile',
      use: { ...devices['iPhone 13'] },
    },
  ],

  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
  },
});
```

### Exempel 3: Jest med coverage-krav

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts', '**/*.test.ts'],

  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/index.ts',
  ],

  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
    // Striktare krav för kritiska moduler
    './src/services/payment/': {
      branches: 95,
      functions: 95,
      lines: 95,
    },
  },

  reporters: [
    'default',
    ['jest-junit', {
      outputDirectory: 'test-results',
      outputName: 'junit.xml',
    }],
  ],

  // Retry flaky tests
  retryTimes: process.env.CI ? 2 : 0,
};
```

------------------------------------------------------------

## Bästa Praxis

### Test-organisation

```
tests/
├── unit/                    # Snabba, isolerade tester
│   ├── services/
│   └── utils/
├── integration/             # Service-integration
│   ├── api/
│   └── database/
├── e2e/                     # End-to-end flöden
│   ├── auth.spec.ts
│   └── checkout.spec.ts
└── fixtures/                # Testdata
    └── users.json
```

### Testnamn och struktur

```typescript
// BRA: Beskrivande testnamn
describe('UserService', () => {
  describe('createUser', () => {
    it('should create a new user with valid data', async () => {
      // ...
    });

    it('should throw ValidationError when email is invalid', async () => {
      // ...
    });

    it('should hash password before saving', async () => {
      // ...
    });
  });
});

// UNDVIK: Vaga testnamn
it('works', () => { /* ... */ });
it('test 1', () => { /* ... */ });
```

### Isolerade tester

```typescript
// BRA: Varje test är oberoende
beforeEach(async () => {
  await db.truncate(['users', 'orders']);
});

afterEach(async () => {
  jest.clearAllMocks();
});

// BRA: Använd factories för testdata
const user = await UserFactory.create({ role: 'admin' });

// UNDVIK: Beroende mellan tester
let userId;  // Delad state - farligt!
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Flaky tests

```yaml
# FEL: Test misslyckas slumpmässigt
- run: npm test

# RÄTT: Implementera retry och timeout
- name: Kör tester med retry
  uses: nick-fields/retry@v3
  with:
    timeout_minutes: 10
    max_attempts: 3
    command: npm test
```

```typescript
// FEL: Race condition i test
it('should update user', async () => {
  updateUser(userId);  // Ingen await!
  const user = await getUser(userId);  // Kan få gamla data
});

// RÄTT: Vänta på alla operationer
it('should update user', async () => {
  await updateUser(userId);
  const user = await getUser(userId);
});
```

### Problem 2: Långsamma tester

```yaml
# FEL: Alla tester i sekvens
- run: npm test  # 20 minuter

# RÄTT: Parallella tester med sharding
strategy:
  matrix:
    shard: [1, 2, 3, 4]
steps:
  - run: npm test -- --shard=${{ matrix.shard }}/4
# Tar nu 5 minuter
```

### Problem 3: Hårdkodade testdata

```typescript
// FEL: Hårdkodad data som kan bli utdaterad
it('should parse date', () => {
  expect(parseDate('2024-01-15')).toBe('January 15, 2024');
});

// RÄTT: Dynamisk testdata
it('should parse date', () => {
  const today = new Date();
  const formatted = formatDate(today);
  expect(parseDate(formatted)).toEqual(today);
});
```

### Problem 4: Otillräcklig coverage

```yaml
# Lägg till coverage-gate
- name: Check coverage
  run: |
    npm test -- --coverage
    # Misslyckas om coverage < 80%
    npx nyc check-coverage --lines 80 --functions 80 --branches 80
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande testpipeline

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en CI-pipeline med unit-tester och coverage.

**Uppgift:**

1. Konfigurera Jest med coverage-rapportering
2. Skapa GitHub Actions workflow för tester
3. Lägg till coverage-tröskel på 80%
4. Integrera med Codecov

**Förväntad lösning:**

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Kör tester med coverage
        run: npm test -- --coverage --watchAll=false

      - name: Kontrollera coverage
        run: |
          npx nyc check-coverage --lines 80 --functions 80 --branches 80

      - name: Upload till Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: true
```

</details>

### Övning 2: Integration-tester med databas

<details>
<summary>Visa övning</summary>

**Mål:** Implementera integration-tester som använder PostgreSQL.

**Uppgift:**

1. Konfigurera PostgreSQL som service i workflow
2. Kör databasmigrationer innan tester
3. Isolera varje test med transaktioner
4. Generera testrapport

**Förväntad lösning:**

```yaml
name: Integration Tests

on: [push, pull_request]

jobs:
  integration:
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

    env:
      DATABASE_URL: postgresql://test:test@localhost:5432/test_db

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Kör migrationer
        run: npm run db:migrate

      - name: Kör integration-tester
        run: npm run test:integration -- --reporter=jest-junit

      - name: Publicera testrapport
        uses: mikepenz/action-junit-report@v4
        if: always()
        with:
          report_paths: '**/junit.xml'
```

</details>

### Övning 3: E2E med Playwright

<details>
<summary>Visa övning</summary>

**Mål:** Implementera E2E-tester med Playwright och parallell körning.

**Uppgift:**

1. Konfigurera Playwright för CI
2. Kör tester parallellt på flera browsers
3. Spara screenshots vid misslyckande
4. Generera HTML-rapport

**Förväntad lösning:**

```yaml
name: E2E Tests

on: [push, pull_request]

jobs:
  e2e:
    name: E2E (${{ matrix.browser }})
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        browser: [chromium, firefox]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci

      - name: Installera Playwright
        run: npx playwright install --with-deps ${{ matrix.browser }}

      - name: Bygg app
        run: npm run build

      - name: Kör E2E-tester
        run: npx playwright test --project=${{ matrix.browser }}

      - name: Ladda upp rapport
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report-${{ matrix.browser }}
          path: |
            playwright-report/
            test-results/
          retention-days: 7
```

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **GitHub Actions** | Workflow-syntax för test-jobs |
| **GitLab CI/CD** | Test-stages och reports |
| **Docker** | Container-baserade testmiljöer |
| **Security** | SAST/DAST i testpipeline |
| **Monitoring** | Test-metrics och dashboards |

------------------------------------------------------------

## Sammanfattning

Automatiserade tester i CI/CD är avgörande för kvalitet och leveranshastighet:

**Testpyramiden:**
- Unit tests (70%) - Snabba, många, billiga
- Integration tests (20%) - Testar samverkan
- E2E tests (10%) - Validerar hela flödet

**Nyckelkoncept:**
- Parallella tester med sharding för snabbhet
- Coverage-trösklar för kvalitetskontroll
- Flaky test-hantering med retries
- Säkerhetstester som en del av pipelinen

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `npm test -- --coverage` | Kör tester med coverage |
| `npm test -- --shard=1/4` | Kör första av 4 shards |
| `npx playwright test` | Kör Playwright E2E |
| `npx nyc check-coverage` | Validera coverage-tröskel |
| `npm audit` | Säkerhetsaudit av dependencies |

------------------------------------------------------------

## Referenser

- Jest Documentation - jestjs.io/docs
- Playwright Test - playwright.dev/docs/test-intro
- Codecov Documentation - docs.codecov.com
- GitHub Actions Test Reporting - docs.github.com/actions
- Testing Best Practices - martinfowler.com/testing
""",
        },
        {
            "order_index": 6,
            "title": "Build & Release Strategies",
            "slug": "build-release-strategies",
            "difficulty": "intermediate",
            "content": """# Build & Release Strategies

------------------------------------------------------------

## Introduktion

Föreställ dig att du ska uppgradera en applikation som används av tusentals användare - utan avbrott, utan buggar som når alla, och med möjlighet att snabbt återgå till föregående version om något går fel. Det är här release-strategier kommer in.

I denna modul lär du dig de viktigaste strategierna för att deploya ändringar säkert till produktion - från enkla rolling updates till avancerade canary deployments.

### Lärandemål

Efter denna modul kommer du att:

- Förstå skillnaderna mellan olika deployment-strategier
- Kunna implementera Rolling, Blue/Green och Canary deployments
- Behärska semantic versioning och automatiserad release
- Implementera feature flags för säkrare utrullningar
- Välja rätt strategi baserat på risktolerans och krav

------------------------------------------------------------

## Teori

### Varför release-strategier?

Rätt release-strategi minimerar risk och möjliggör snabba, säkra leveranser.

**Viktiga fördelar:**

| Fördel | Beskrivning |
|--------|-------------|
| **Tillgänglighet** | Minimerar eller eliminerar nedtid |
| **Säkerhet** | Snabb rollback möjlig vid problem |
| **Risk** | Reducerar påverkan av buggar |
| **Validering** | Testa på riktiga användare gradvis |
| **Flexibilitet** | Olika strategier för olika situationer |

### Översikt av strategier

```
+------------------------------------------------------------------+
|                    DEPLOYMENT STRATEGIES                         |
+------------------------------------------------------------------+
|                                                                  |
|   RECREATE (Big Bang)                                            |
|   [v1] [v1] [v1] ----> [X] [X] [X] ----> [v2] [v2] [v2]          |
|                    Nedtid!                                       |
|                                                                  |
|   ROLLING UPDATE                                                 |
|   [v1] [v1] [v1] [v1]                                            |
|   [v2] [v1] [v1] [v1]   <- En åt gången                          |
|   [v2] [v2] [v1] [v1]                                            |
|   [v2] [v2] [v2] [v1]                                            |
|   [v2] [v2] [v2] [v2]   <- Klart, ingen nedtid                   |
|                                                                  |
|   BLUE/GREEN                                                     |
|   [BLUE v1] <-- Traffic                                          |
|   [GREEN v2] idle                                                |
|        |                                                         |
|        v  Switch!                                                |
|   [BLUE v1] idle                                                 |
|   [GREEN v2] <-- Traffic                                         |
|                                                                  |
|   CANARY                                                         |
|   [v1] [v1] [v1] [v1] [v1] [v1] [v1] [v1] [v1] [v2]              |
|                                              ^                   |
|                                     5% canary traffic            |
|                                                                  |
+------------------------------------------------------------------+
```

### Jämförelse

| Strategi | Nedtid | Rollback | Resurser | Komplexitet |
|----------|--------|----------|----------|-------------|
| **Recreate** | Ja | Långsam | Låga | Låg |
| **Rolling** | Nej | Medium | Låga | Låg |
| **Blue/Green** | Nej | Snabb | Höga (2x) | Medium |
| **Canary** | Nej | Snabb | Medium | Hög |
| **Feature Flag** | Nej | Omedelbar | Låga | Medium |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Rolling Deployment

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1           # Max 1 extra pod under uppdatering
      maxUnavailable: 0     # Alltid minst 4 tillgängliga
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
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
```

```yaml
# .github/workflows/rolling-deploy.yml
name: Rolling Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup kubectl
        uses: azure/setup-kubectl@v3

      - name: Configure kubeconfig
        run: |
          echo "${{ secrets.KUBECONFIG }}" | base64 -d > kubeconfig
          export KUBECONFIG=kubeconfig

      - name: Deploy med rolling update
        run: |
          kubectl set image deployment/myapp \
            app=myapp:${{ github.sha }}

      - name: Vänta på rollout
        run: |
          kubectl rollout status deployment/myapp \
            --timeout=300s

      - name: Verifiera deployment
        run: |
          kubectl get pods -l app=myapp
          kubectl describe deployment myapp
```

### Steg 2: Blue/Green Deployment

```yaml
# kubernetes/blue-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
        - name: app
          image: myapp:v1
          ports:
            - containerPort: 8080
---
# kubernetes/green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
spec:
  replicas: 0  # Startar med 0 replicas
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
        - name: app
          image: myapp:v2
          ports:
            - containerPort: 8080
---
# kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    version: blue  # Pekar på aktiv deployment
  ports:
    - port: 80
      targetPort: 8080
```

```yaml
# .github/workflows/blue-green.yml
name: Blue/Green Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Bestäm aktiv/inaktiv miljö
        id: env
        run: |
          ACTIVE=$(kubectl get svc myapp -o jsonpath='{.spec.selector.version}')
          if [ "$ACTIVE" = "blue" ]; then
            echo "deploy_to=green" >> $GITHUB_OUTPUT
            echo "active=blue" >> $GITHUB_OUTPUT
          else
            echo "deploy_to=blue" >> $GITHUB_OUTPUT
            echo "active=green" >> $GITHUB_OUTPUT
          fi

      - name: Deploya till inaktiv miljö
        run: |
          # Uppdatera image
          kubectl set image deployment/myapp-${{ steps.env.outputs.deploy_to }} \
            app=myapp:${{ github.sha }}

          # Skala upp inaktiv miljö
          kubectl scale deployment/myapp-${{ steps.env.outputs.deploy_to }} \
            --replicas=3

          # Vänta på readiness
          kubectl rollout status deployment/myapp-${{ steps.env.outputs.deploy_to }} \
            --timeout=300s

      - name: Kör smoke tests
        run: |
          POD=$(kubectl get pod -l version=${{ steps.env.outputs.deploy_to }} -o jsonpath='{.items[0].metadata.name}')
          kubectl port-forward $POD 8080:8080 &
          sleep 5
          curl -f http://localhost:8080/health
          curl -f http://localhost:8080/api/status

      - name: Växla trafik
        run: |
          kubectl patch svc myapp -p \
            '{"spec":{"selector":{"version":"${{ steps.env.outputs.deploy_to }}"}}}'

      - name: Verifiera
        run: |
          sleep 10
          curl -f https://myapp.example.com/health

      - name: Skala ner gammal miljö
        run: |
          kubectl scale deployment/myapp-${{ steps.env.outputs.active }} \
            --replicas=0
```

### Steg 3: Canary Deployment

```yaml
# .github/workflows/canary.yml
name: Canary Deploy

on:
  push:
    branches: [main]

jobs:
  canary:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy canary (5%)
        run: |
          # Deploya ny version till canary deployment
          kubectl set image deployment/myapp-canary \
            app=myapp:${{ github.sha }}

          # Skala: 1 canary, 19 stable = 5%
          kubectl scale deployment/myapp-canary --replicas=1
          kubectl scale deployment/myapp-stable --replicas=19

          kubectl rollout status deployment/myapp-canary

      - name: Övervaka metrics (5 min)
        id: monitor_5
        run: |
          echo "Övervakar canary i 5 minuter..."
          sleep 300

          # Hämta error rate från Prometheus
          ERROR_RATE=$(curl -s "prometheus:9090/api/v1/query?query=rate(http_errors_total{version='canary'}[5m])" | jq -r '.data.result[0].value[1] // "0"')

          echo "Error rate: $ERROR_RATE"

          if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
            echo "error=true" >> $GITHUB_OUTPUT
          else
            echo "error=false" >> $GITHUB_OUTPUT
          fi

      - name: Rollback vid fel
        if: steps.monitor_5.outputs.error == 'true'
        run: |
          echo "::error::Canary visar för hög error rate, rullar tillbaka"
          kubectl scale deployment/myapp-canary --replicas=0
          kubectl scale deployment/myapp-stable --replicas=20
          exit 1

      - name: Öka till 25%
        run: |
          kubectl scale deployment/myapp-canary --replicas=5
          kubectl scale deployment/myapp-stable --replicas=15

      - name: Övervaka metrics (10 min)
        run: |
          echo "Övervakar 25% canary i 10 minuter..."
          sleep 600

          # Kontrollera metrics igen
          ERROR_RATE=$(curl -s "prometheus:9090/api/v1/query?query=rate(http_errors_total{version='canary'}[10m])" | jq -r '.data.result[0].value[1] // "0"')

          if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
            echo "::error::Fel upptäckt vid 25%"
            kubectl scale deployment/myapp-canary --replicas=0
            kubectl scale deployment/myapp-stable --replicas=20
            exit 1
          fi

      - name: Full utrullning (100%)
        run: |
          # Uppdatera stable till ny version
          kubectl set image deployment/myapp-stable \
            app=myapp:${{ github.sha }}

          kubectl scale deployment/myapp-stable --replicas=20
          kubectl scale deployment/myapp-canary --replicas=0

          kubectl rollout status deployment/myapp-stable

      - name: Cleanup
        if: always()
        run: |
          echo "Canary deployment slutförd"
```

### Steg 4: Feature Flags

```yaml
# .github/workflows/feature-flag-deploy.yml
name: Deploy with Feature Flags

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Säkerställ feature flag är AV
        run: |
          curl -X PATCH \
            -H "Authorization: ${{ secrets.LAUNCHDARKLY_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{"patch": [{"op": "replace", "path": "/environments/production/on", "value": false}]}' \
            "https://app.launchdarkly.com/api/v2/flags/my-project/new-checkout-flow"

      - name: Deploy applikation
        run: |
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp

      - name: Aktivera för interna användare
        run: |
          curl -X PATCH \
            -H "Authorization: ${{ secrets.LAUNCHDARKLY_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "patch": [
                {"op": "replace", "path": "/environments/production/on", "value": true},
                {"op": "replace", "path": "/environments/production/rules", "value": [
                  {
                    "variation": 0,
                    "clauses": [
                      {"attribute": "email", "op": "endsWith", "values": ["@company.com"]}
                    ]
                  }
                ]}
              ]
            }' \
            "https://app.launchdarkly.com/api/v2/flags/my-project/new-checkout-flow"
```

```typescript
// src/features/checkout.ts
import * as LaunchDarkly from '@launchdarkly/node-server-sdk';

const ldClient = LaunchDarkly.init(process.env.LD_SDK_KEY);

export async function getCheckoutHandler(user: User) {
  await ldClient.waitForInitialization();

  const useNewCheckout = await ldClient.variation(
    'new-checkout-flow',
    {
      key: user.id,
      email: user.email,
      custom: {
        plan: user.plan,
        country: user.country,
      }
    },
    false  // Default om flaggan inte finns
  );

  if (useNewCheckout) {
    return newCheckoutHandler;
  }

  return legacyCheckoutHandler;
}
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Automatiserad Semantic Versioning

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Beräkna version
        id: version
        uses: paulhatch/semantic-version@v5
        with:
          tag_prefix: "v"
          major_pattern: "(BREAKING CHANGE)"
          minor_pattern: "(feat)"
          version_format: "${{major}}.${{minor}}.${{patch}}"

      - name: Skapa Git tag
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git tag v${{ steps.version.outputs.version }}
          git push origin v${{ steps.version.outputs.version }}

      - name: Generera changelog
        id: changelog
        uses: mikepenz/release-changelog-builder-action@v4
        with:
          configuration: .github/changelog-config.json
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Skapa GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: v${{ steps.version.outputs.version }}
          name: Release v${{ steps.version.outputs.version }}
          body: ${{ steps.changelog.outputs.changelog }}
          draft: false
          prerelease: false

  build-and-push:
    needs: release
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: |
          docker build -t myapp:${{ needs.release.outputs.version }} .
          docker tag myapp:${{ needs.release.outputs.version }} myapp:latest

      - name: Push to registry
        run: |
          docker push myapp:${{ needs.release.outputs.version }}
          docker push myapp:latest
```

### Exempel 2: Argo Rollouts Canary

```yaml
# kubernetes/rollout.yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: myapp
spec:
  replicas: 10
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
          image: myapp:v1
          ports:
            - containerPort: 8080
  strategy:
    canary:
      canaryService: myapp-canary
      stableService: myapp-stable
      trafficRouting:
        nginx:
          stableIngress: myapp-ingress
      steps:
        - setWeight: 5
        - pause: {duration: 5m}
        - setWeight: 20
        - pause: {duration: 10m}
        - setWeight: 50
        - pause: {duration: 10m}
        - setWeight: 100
      analysis:
        templates:
          - templateName: success-rate
        startingStep: 1
        args:
          - name: service-name
            value: myapp-canary
---
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  args:
    - name: service-name
  metrics:
    - name: success-rate
      interval: 1m
      successCondition: result[0] >= 0.95
      failureLimit: 3
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{service="{{args.service-name}}",status=~"2.."}[5m])) /
            sum(rate(http_requests_total{service="{{args.service-name}}"}[5m]))
```

### Exempel 3: Progressive Delivery Pipeline

```yaml
# .github/workflows/progressive-delivery.yml
name: Progressive Delivery

on:
  push:
    branches: [main]

env:
  IMAGE: myapp

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image_tag: ${{ steps.build.outputs.tag }}
    steps:
      - uses: actions/checkout@v4

      - name: Build and push
        id: build
        run: |
          TAG=${{ github.sha }}
          docker build -t $IMAGE:$TAG .
          docker push $IMAGE:$TAG
          echo "tag=$TAG" >> $GITHUB_OUTPUT

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy till staging
        run: |
          kubectl --context staging set image deployment/myapp \
            app=$IMAGE:${{ needs.build.outputs.image_tag }}
          kubectl --context staging rollout status deployment/myapp

      - name: Kör E2E-tester
        run: |
          npm run test:e2e -- --base-url=https://staging.example.com

  deploy-canary:
    needs: [build, deploy-staging]
    runs-on: ubuntu-latest
    environment: production-canary
    steps:
      - name: Deploy canary (5%)
        run: |
          kubectl --context prod set image deployment/myapp-canary \
            app=$IMAGE:${{ needs.build.outputs.image_tag }}
          kubectl --context prod scale deployment/myapp-canary --replicas=1

      - name: Övervaka i 15 minuter
        run: |
          for i in {1..15}; do
            ERROR_RATE=$(curl -s prometheus/query | jq '.error_rate')
            if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
              echo "::error::Hög error rate, avbryter"
              kubectl --context prod scale deployment/myapp-canary --replicas=0
              exit 1
            fi
            echo "Minut $i: Error rate OK ($ERROR_RATE)"
            sleep 60
          done

  deploy-production:
    needs: [build, deploy-canary]
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Full utrullning
        run: |
          kubectl --context prod set image deployment/myapp-stable \
            app=$IMAGE:${{ needs.build.outputs.image_tag }}
          kubectl --context prod rollout status deployment/myapp-stable
          kubectl --context prod scale deployment/myapp-canary --replicas=0

      - name: Verifiera
        run: |
          curl -f https://myapp.example.com/health
```

------------------------------------------------------------

## Bästa Praxis

### Välj rätt strategi

```
+------------------------------------------------------------------+
|              NÄR SKA JAG ANVÄNDA VILKEN STRATEGI?                |
+------------------------------------------------------------------+
|                                                                  |
|   ROLLING UPDATE                                                 |
|   - Låg risk-ändringar                                           |
|   - Begränsade resurser                                          |
|   - Databas-kompatibla ändringar                                 |
|                                                                  |
|   BLUE/GREEN                                                     |
|   - Kräver snabb rollback                                        |
|   - Stora ändringar                                              |
|   - Behöver testa i prod-miljö före switch                       |
|                                                                  |
|   CANARY                                                         |
|   - Hög risk-ändringar                                           |
|   - Bra observability finns                                      |
|   - Vill validera med riktig trafik                              |
|                                                                  |
|   FEATURE FLAGS                                                  |
|   - Behöver kontroll per användare/segment                       |
|   - A/B-testning krävs                                           |
|   - Vill separera deploy från release                            |
|                                                                  |
+------------------------------------------------------------------+
```

### Rollback-plan

```yaml
# Inkludera alltid rollback-steg
- name: Deploy
  id: deploy
  run: kubectl set image deployment/myapp app=myapp:$NEW_VERSION

- name: Verify
  id: verify
  run: |
    sleep 30
    curl -f https://myapp.example.com/health || exit 1

- name: Rollback vid fel
  if: failure() && steps.deploy.outcome == 'success'
  run: |
    kubectl rollout undo deployment/myapp
    kubectl rollout status deployment/myapp
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Databas-migrationer bryter rollback

```yaml
# FEL: Breaking migration innan deploy
- run: npm run db:migrate  # DROP COLUMN age
- run: kubectl set image ...  # Ny kod utan age
# Rollback fungerar inte - gammal kod kräver age!

# RÄTT: Expand-contract pattern
# Steg 1: Lägg till ny kolumn, behåll gammal
- run: npm run db:migrate  # ADD COLUMN birth_date
- run: kubectl set image ... # Kod läser båda

# Steg 2: Migrera data
- run: npm run db:migrate  # UPDATE birth_date FROM age

# Steg 3: Ta bort gammal (efter några deploys)
- run: npm run db:migrate  # DROP COLUMN age
```

### Problem 2: Ingen health check

```yaml
# FEL: Ingen readiness probe
spec:
  containers:
    - name: app
      image: myapp:v2
      # Pod markeras ready direkt!

# RÄTT: Proper health checks
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
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 30
        periodSeconds: 10
```

------------------------------------------------------------

## Övningar

### Övning 1: Rolling Deployment

<details>
<summary>Visa övning</summary>

**Mål:** Implementera en rolling deployment med zero downtime.

**Uppgift:**

1. Skapa Kubernetes Deployment med RollingUpdate strategi
2. Konfigurera maxSurge och maxUnavailable
3. Lägg till readiness probe
4. Skapa GitHub Actions workflow för deploy

**Förväntad lösning:**

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    spec:
      containers:
        - name: app
          image: myapp:latest
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

```yaml
# .github/workflows/deploy.yml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: kubectl set image deployment/myapp app=myapp:${{ github.sha }}
      - run: kubectl rollout status deployment/myapp --timeout=300s
```

</details>

### Övning 2: Blue/Green med manuell switch

<details>
<summary>Visa övning</summary>

**Mål:** Implementera Blue/Green deployment med manuell trafikswitch.

**Uppgift:**

1. Skapa två deployments (blue och green)
2. Skapa service som pekar på aktiv deployment
3. Implementera workflow med manuellt godkännande för switch
4. Lägg till smoke tests innan switch

**Förväntad lösning:**

Se Steg 2 i Steg-för-steg Guide ovan.

</details>

### Övning 3: Feature Flag Integration

<details>
<summary>Visa övning</summary>

**Mål:** Implementera feature flag-baserad release.

**Uppgift:**

1. Integrera LaunchDarkly (eller liknande) i din app
2. Skapa deployment workflow som:
   - Stänger av flaggan
   - Deployar ny kod
   - Aktiverar för interna användare först
3. Lägg till manuellt steg för full aktivering

**Förväntad lösning:**

Se Steg 4 i Steg-för-steg Guide ovan.

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **Kubernetes** | Deployment strategies och rollouts |
| **GitOps** | ArgoCD Rollouts för canary |
| **Monitoring** | Metrics för canary-beslut |
| **Testing** | Smoke tests mellan steg |
| **Security** | Validering innan rollout |

------------------------------------------------------------

## Sammanfattning

Release-strategier är avgörande för säkra produktionsleveranser:

**Strategier:**
- Rolling Update - Enkel, gradvis, låg resursåtgång
- Blue/Green - Snabb switch, full rollback, kräver dubbla resurser
- Canary - Testar på riktig trafik, kräver bra observability
- Feature Flags - Runtime-kontroll, A/B-testning

**Nyckelprinciper:**
- Välj strategi baserat på risknivå
- Ha alltid en rollback-plan
- Använd health checks för automatisk återhämtning
- Separera deployment från release med feature flags

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `kubectl rollout status` | Följ deployment-progress |
| `kubectl rollout undo` | Rollback till föregående |
| `kubectl set image` | Uppdatera container image |
| `kubectl scale` | Ändra antal replicas |
| `kubectl patch svc` | Ändra service selector |

------------------------------------------------------------

## Referenser

- Kubernetes Deployment Strategies - kubernetes.io/docs/concepts/workloads/controllers/deployment
- Argo Rollouts - argoproj.github.io/argo-rollouts
- LaunchDarkly Feature Flags - launchdarkly.com/docs
- Flagger Progressive Delivery - flagger.app
- Martin Fowler - Feature Toggles - martinfowler.com/articles/feature-toggles.html
""",
        },
        {
            "order_index": 7,
            "title": "GitLab CI Deep Dive",
            "slug": "gitlab-ci-deep-dive",
            "difficulty": "intermediate",
            "content": """# GitLab CI Deep Dive

------------------------------------------------------------

## Introduktion

Du har redan lärt dig grunderna i GitLab CI/CD - nu är det dags att gå djupare. I denna modul utforskar vi avancerade funktioner som Parent-Child Pipelines, DAG-optimering, Dynamic Child Pipelines och Auto DevOps.

Denna modul bygger vidare på grundläggande GitLab CI/CD-kunskaper och fokuserar på enterprise-mönster och skalbar pipeline-design.

### Lärandemål

Efter denna modul kommer du att:

- Behärska Parent-Child och Multi-Project Pipelines
- Optimera pipelines med DAG och needs-keyword
- Implementera Dynamic Child Pipelines för monorepos
- Konfigurera och anpassa Auto DevOps
- Använda avancerad caching och artifacts-strategi

------------------------------------------------------------

## Teori

### Avancerad Pipeline-arkitektur

GitLab erbjuder kraftfulla funktioner för att bygga skalbara pipelines:

```
+------------------------------------------------------------------+
|                 AVANCERADE GITLAB PIPELINE-MÖNSTER               |
+------------------------------------------------------------------+
|                                                                  |
|   PARENT-CHILD PIPELINES                                         |
|   +------------------+                                           |
|   | Parent Pipeline  |                                           |
|   |    [trigger]-----+---> Child Pipeline A                      |
|   |    [trigger]-----+---> Child Pipeline B                      |
|   +------------------+                                           |
|                                                                  |
|   DAG (Directed Acyclic Graph)                                   |
|   [lint] ----+                                                   |
|              |---> [test] ----+                                  |
|   [build]----+                |---> [deploy]                     |
|                               |                                  |
|   [security]------------------+                                  |
|                                                                  |
|   MULTI-PROJECT PIPELINE                                         |
|   [Repo A: Build] ---trigger---> [Repo B: Deploy]                |
|                                                                  |
+------------------------------------------------------------------+
```

### Nyckelkoncept

| Koncept | Beskrivning |
|---------|-------------|
| **Parent-Child** | Delar upp pipeline i hanterbara delar |
| **DAG** | Optimerar beroenden mellan jobs |
| **Dynamic Pipelines** | Generera pipeline-config runtime |
| **Multi-Project** | Trigga pipelines i andra repos |
| **Auto DevOps** | Automatisk CI/CD utan konfiguration |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Parent-Child Pipelines

```yaml
# .gitlab-ci.yml (Parent)
stages:
  - triggers
  - deploy

variables:
  PARENT_VERSION: "1.0.0"

# Trigga child pipeline för frontend
frontend:
  stage: triggers
  trigger:
    include: frontend/.gitlab-ci.yml
    strategy: depend                    # Vänta på child
  rules:
    - changes:
        - frontend/**/*

# Trigga child pipeline för backend
backend:
  stage: triggers
  trigger:
    include: backend/.gitlab-ci.yml
    strategy: depend
  rules:
    - changes:
        - backend/**/*

# Deploy efter alla children
deploy:
  stage: deploy
  needs:
    - job: frontend
      optional: true
    - job: backend
      optional: true
  script:
    - echo "Alla komponenter byggda, deployar..."
```

```yaml
# frontend/.gitlab-ci.yml (Child)
stages:
  - build
  - test

variables:
  NODE_VERSION: "20"

build-frontend:
  stage: build
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

test-frontend:
  stage: test
  image: node:${NODE_VERSION}
  needs:
    - build-frontend
  script:
    - npm test
```

### Steg 2: DAG-optimering med needs

```yaml
# Optimerad pipeline med DAG
stages:
  - prepare
  - build
  - test
  - security
  - deploy

# Dessa kör parallellt
lint:
  stage: prepare
  script:
    - npm run lint

install:
  stage: prepare
  script:
    - npm ci
  artifacts:
    paths:
      - node_modules/
    expire_in: 1 hour

# Build väntar bara på install, inte lint
build:
  stage: build
  needs:
    - install                           # Explicit beroende
  script:
    - npm run build
  artifacts:
    paths:
      - dist/

# Tester kan köras parallellt
unit-tests:
  stage: test
  needs:
    - install                           # Behöver bara dependencies
  script:
    - npm test -- --coverage

integration-tests:
  stage: test
  needs:
    - build                             # Behöver build artifacts
    - install
  services:
    - postgres:15
  script:
    - npm run test:integration

e2e-tests:
  stage: test
  needs:
    - build
  script:
    - npm run test:e2e

# Security kan köra parallellt med tester
security-scan:
  stage: security
  needs:
    - install                           # Startar direkt efter install
  script:
    - npm audit --audit-level=high

dependency-scan:
  stage: security
  needs: []                             # Kör helt parallellt
  script:
    - trivy fs .

# Deploy väntar på allt kritiskt
deploy:
  stage: deploy
  needs:
    - unit-tests
    - integration-tests
    - security-scan
  script:
    - ./deploy.sh
```

### Steg 3: Dynamic Child Pipelines

```yaml
# .gitlab-ci.yml - Dynamisk pipeline för monorepo
stages:
  - generate
  - trigger

generate-pipeline:
  stage: generate
  image: python:3.11
  script:
    - |
      # Identifiera ändrade appar
      CHANGED_APPS=$(git diff --name-only $CI_MERGE_REQUEST_DIFF_BASE_SHA |
        grep -oE "^apps/[^/]+" | sort -u)

      # Generera pipeline YAML
      python scripts/generate-pipeline.py $CHANGED_APPS > generated-pipeline.yml

      cat generated-pipeline.yml
  artifacts:
    paths:
      - generated-pipeline.yml

trigger-dynamic:
  stage: trigger
  trigger:
    include:
      - artifact: generated-pipeline.yml
        job: generate-pipeline
    strategy: depend
```

```python
# scripts/generate-pipeline.py
import sys
import yaml

def generate_pipeline(apps):
    pipeline = {
        'stages': ['build', 'test', 'deploy'],
        'variables': {'CI': 'true'}
    }

    for app in apps:
        app_name = app.replace('apps/', '')

        # Build job
        pipeline[f'build-{app_name}'] = {
            'stage': 'build',
            'image': 'node:20',
            'script': [
                f'cd {app}',
                'npm ci',
                'npm run build'
            ],
            'artifacts': {
                'paths': [f'{app}/dist/'],
                'expire_in': '1 hour'
            }
        }

        # Test job
        pipeline[f'test-{app_name}'] = {
            'stage': 'test',
            'image': 'node:20',
            'needs': [f'build-{app_name}'],
            'script': [
                f'cd {app}',
                'npm test'
            ]
        }

    return pipeline

if __name__ == '__main__':
    apps = [arg for arg in sys.argv[1:] if arg.startswith('apps/')]
    if not apps:
        # Fallback - bygg alla
        apps = ['apps/frontend', 'apps/backend', 'apps/api']

    pipeline = generate_pipeline(apps)
    print(yaml.dump(pipeline, default_flow_style=False))
```

### Steg 4: Multi-Project Pipelines

```yaml
# repo-a/.gitlab-ci.yml
stages:
  - build
  - trigger-downstream

build:
  stage: build
  script:
    - docker build -t myimage:$CI_COMMIT_SHA .
    - docker push myimage:$CI_COMMIT_SHA

# Trigga deployment i annat repo
trigger-deploy:
  stage: trigger-downstream
  trigger:
    project: myorg/deployment-repo
    branch: main
    strategy: depend
  variables:
    UPSTREAM_IMAGE: myimage:$CI_COMMIT_SHA
    UPSTREAM_PIPELINE_ID: $CI_PIPELINE_ID
```

```yaml
# deployment-repo/.gitlab-ci.yml
stages:
  - deploy

deploy-from-upstream:
  stage: deploy
  rules:
    - if: $UPSTREAM_IMAGE                # Kör bara om triggad
  script:
    - echo "Deployar image: $UPSTREAM_IMAGE"
    - kubectl set image deployment/myapp app=$UPSTREAM_IMAGE
  environment:
    name: production
```

### Steg 5: Auto DevOps anpassning

```yaml
# .gitlab-ci.yml med Auto DevOps
include:
  - template: Auto-DevOps.gitlab-ci.yml

variables:
  # Konfigurera Auto DevOps
  AUTO_DEVOPS_PLATFORM_TARGET: EC2
  POSTGRES_ENABLED: "true"
  TEST_DISABLED: "false"
  CODE_QUALITY_DISABLED: "false"
  SAST_DISABLED: "false"
  DAST_DISABLED: "true"                 # Inaktivera DAST

  # Kubernetes-config
  KUBE_NAMESPACE: production
  HELM_UPGRADE_EXTRA_ARGS: >-
    --set image.pullPolicy=Always
    --set resources.limits.memory=512Mi

# Överskugga Auto DevOps jobs
build:
  extends: .auto-build
  before_script:
    - echo "Anpassad pre-build"
  after_script:
    - echo "Anpassad post-build"

# Lägg till egna jobs utöver Auto DevOps
custom-security-scan:
  stage: test
  image: aquasec/trivy:latest
  script:
    - trivy image $CI_APPLICATION_REPOSITORY:$CI_APPLICATION_TAG
  allow_failure: true
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Enterprise Monorepo Pipeline

```yaml
# .gitlab-ci.yml
include:
  - local: '/ci/templates/common.yml'
  - local: '/ci/templates/docker.yml'
  - local: '/ci/templates/deploy.yml'

stages:
  - prepare
  - build
  - test
  - security
  - package
  - deploy

workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"
    - if: $CI_COMMIT_TAG

variables:
  DOCKER_BUILDKIT: 1
  COMPOSE_DOCKER_CLI_BUILD: 1

# Detect changed apps
detect-changes:
  stage: prepare
  image: alpine:latest
  script:
    - |
      if [ "$CI_MERGE_REQUEST_IID" ]; then
        CHANGED=$(git diff --name-only origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME)
      else
        CHANGED=$(git diff --name-only HEAD~1)
      fi

      echo "FRONTEND_CHANGED=false" > changes.env
      echo "BACKEND_CHANGED=false" >> changes.env
      echo "API_CHANGED=false" >> changes.env

      echo "$CHANGED" | grep -q "^apps/frontend/" && echo "FRONTEND_CHANGED=true" >> changes.env || true
      echo "$CHANGED" | grep -q "^apps/backend/" && echo "BACKEND_CHANGED=true" >> changes.env || true
      echo "$CHANGED" | grep -q "^apps/api/" && echo "API_CHANGED=true" >> changes.env || true
      echo "$CHANGED" | grep -q "^packages/" && {
        echo "FRONTEND_CHANGED=true" >> changes.env
        echo "BACKEND_CHANGED=true" >> changes.env
        echo "API_CHANGED=true" >> changes.env
      } || true

      cat changes.env
  artifacts:
    reports:
      dotenv: changes.env

# Frontend jobs
build-frontend:
  stage: build
  needs:
    - detect-changes
  rules:
    - if: $FRONTEND_CHANGED == "true"
    - if: $CI_COMMIT_TAG
  trigger:
    include: apps/frontend/.gitlab-ci.yml
    strategy: depend

# Backend jobs
build-backend:
  stage: build
  needs:
    - detect-changes
  rules:
    - if: $BACKEND_CHANGED == "true"
    - if: $CI_COMMIT_TAG
  trigger:
    include: apps/backend/.gitlab-ci.yml
    strategy: depend

# API jobs
build-api:
  stage: build
  needs:
    - detect-changes
  rules:
    - if: $API_CHANGED == "true"
    - if: $CI_COMMIT_TAG
  trigger:
    include: apps/api/.gitlab-ci.yml
    strategy: depend

# Global security scan
security-scan:
  stage: security
  needs: []
  image: aquasec/trivy:latest
  script:
    - trivy fs --severity HIGH,CRITICAL .
  allow_failure: true

# Deploy
deploy-staging:
  stage: deploy
  needs:
    - job: build-frontend
      optional: true
    - job: build-backend
      optional: true
    - job: build-api
      optional: true
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - ./scripts/deploy.sh staging
```

### Exempel 2: Avancerad Cache-strategi

```yaml
# Optimerad caching
variables:
  NPM_CONFIG_CACHE: "$CI_PROJECT_DIR/.npm"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.pip"

# Global cache definition
cache: &global_cache
  key:
    files:
      - package-lock.json
      - requirements.txt
  paths:
    - .npm/
    - .pip/
    - node_modules/
    - venv/
  policy: pull-push

# Install job - skriver till cache
install:
  stage: prepare
  cache:
    <<: *global_cache
    policy: push                        # Endast skriv
  script:
    - npm ci --cache .npm --prefer-offline
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt

# Test jobs - läser från cache
test-frontend:
  stage: test
  cache:
    <<: *global_cache
    policy: pull                        # Endast läs (snabbare)
  needs:
    - install
  script:
    - npm test

test-backend:
  stage: test
  cache:
    <<: *global_cache
    policy: pull
  needs:
    - install
  script:
    - source venv/bin/activate
    - pytest

# Branch-specifik cache för artifacts
build:
  stage: build
  cache:
    key: build-$CI_COMMIT_REF_SLUG
    paths:
      - dist/
      - .next/cache/
    policy: pull-push
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 day
```

### Exempel 3: Review Apps med Kubernetes

```yaml
# Dynamiska preview-miljöer
.review_template:
  image: dtzar/helm-kubectl:3.12
  before_script:
    - kubectl config use-context $KUBE_CONTEXT

deploy-review:
  extends: .review_template
  stage: deploy
  script:
    - |
      # Skapa namespace om det inte finns
      kubectl create namespace review-$CI_MERGE_REQUEST_IID --dry-run=client -o yaml | kubectl apply -f -

      # Deploy med Helm
      helm upgrade --install review-$CI_MERGE_REQUEST_IID ./chart \
        --namespace review-$CI_MERGE_REQUEST_IID \
        --set image.tag=$CI_COMMIT_SHA \
        --set ingress.host=$CI_MERGE_REQUEST_IID.review.example.com \
        --set env.DATABASE_URL=$REVIEW_DATABASE_URL \
        --wait --timeout 5m
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    url: https://$CI_MERGE_REQUEST_IID.review.example.com
    on_stop: stop-review
    auto_stop_in: 3 days
  rules:
    - if: $CI_MERGE_REQUEST_ID

stop-review:
  extends: .review_template
  stage: deploy
  script:
    - helm uninstall review-$CI_MERGE_REQUEST_IID -n review-$CI_MERGE_REQUEST_IID || true
    - kubectl delete namespace review-$CI_MERGE_REQUEST_IID || true
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    action: stop
  rules:
    - if: $CI_MERGE_REQUEST_ID
      when: manual
```

------------------------------------------------------------

## Bästa Praxis

### Pipeline-design

```yaml
# BRA: Modulär design med includes
include:
  - local: '/ci/templates/base.yml'
  - local: '/ci/templates/test.yml'
  - local: '/ci/templates/deploy.yml'
  - project: 'company/ci-templates'
    ref: v2.0
    file: '/templates/security.yml'

# BRA: Använd extends för återanvändning
.node-base:
  image: node:20
  cache:
    key: node-modules
    paths:
      - node_modules/
  before_script:
    - npm ci

build:
  extends: .node-base
  script:
    - npm run build

test:
  extends: .node-base
  script:
    - npm test
```

### Optimering

```yaml
# BRA: Interruptible för att spara resurser
job:
  interruptible: true                   # Avbryt vid ny commit

# BRA: Resource groups för deployment
deploy-production:
  resource_group: production            # Endast en deploy åt gången
  script:
    - ./deploy.sh

# BRA: Timeout för att förhindra stuck jobs
job:
  timeout: 30 minutes
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Pipeline för komplex

```yaml
# FEL: Allt i en fil
# 1000+ rader .gitlab-ci.yml

# RÄTT: Dela upp med includes
include:
  - local: '/ci/jobs/build.yml'
  - local: '/ci/jobs/test.yml'
  - local: '/ci/jobs/deploy.yml'
```

### Problem 2: Cache inte effektiv

```yaml
# FEL: För bred cache key
cache:
  key: $CI_COMMIT_SHA                   # Ny cache varje commit!

# RÄTT: Key baserad på dependencies
cache:
  key:
    files:
      - package-lock.json               # Ändras bara vid dependency-update
```

------------------------------------------------------------

## Övningar

### Övning 1: Parent-Child Pipeline

<details>
<summary>Visa övning</summary>

**Mål:** Implementera en monorepo-pipeline med Parent-Child struktur.

**Uppgift:**

1. Skapa parent pipeline som detekterar ändringar
2. Trigga child pipelines för ändrade appar
3. Implementera DAG-optimering i child pipelines
4. Lägg till deploy som väntar på alla children

**Se Steg 1 och Exempel 1 för lösning.**

</details>

### Övning 2: Dynamic Pipeline

<details>
<summary>Visa övning</summary>

**Mål:** Generera pipeline-konfiguration dynamiskt.

**Uppgift:**

1. Identifiera ändrade mappar
2. Generera YAML-fil med jobs för ändrade appar
3. Trigga genererad pipeline som child

**Se Steg 3 för lösning.**

</details>

### Övning 3: Review Apps

<details>
<summary>Visa övning</summary>

**Mål:** Implementera automatiska preview-miljöer för MRs.

**Uppgift:**

1. Deploy unique miljö per MR
2. Automatisk cleanup efter 3 dagar
3. Manuell stop-action
4. Dynamisk DNS/Ingress

**Se Exempel 3 för lösning.**

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **GitLab CI/CD** | Grundläggande koncept |
| **Docker** | Container builds med Kaniko |
| **Kubernetes** | Review apps och deployment |
| **Monorepo** | Dynamic child pipelines |
| **Security** | SAST/DAST integration |

------------------------------------------------------------

## Sammanfattning

GitLab CI/CD erbjuder kraftfulla avancerade funktioner:

**Nyckelkoncept:**
- Parent-Child Pipelines för modularitet
- DAG med needs för optimering
- Dynamic Child Pipelines för monorepos
- Auto DevOps för snabbstart

**Optimering:**
- Effektiv caching med rätt keys
- Interruptible jobs
- Resource groups för deploys

------------------------------------------------------------

## Nyckelkommandon

| Syntax | Beskrivning |
|--------|-------------|
| `trigger: include:` | Trigga child pipeline |
| `needs:` | DAG dependencies |
| `strategy: depend` | Vänta på child pipeline |
| `resource_group:` | Begränsa concurrent jobs |
| `interruptible:` | Tillåt avbrott |
| `include: project:` | Inkludera från annat repo |

------------------------------------------------------------

## Referenser

- GitLab CI/CD Pipelines - docs.gitlab.com/ee/ci/pipelines
- Parent-Child Pipelines - docs.gitlab.com/ee/ci/pipelines/parent_child_pipelines.html
- DAG Dependencies - docs.gitlab.com/ee/ci/directed_acyclic_graph
- Auto DevOps - docs.gitlab.com/ee/topics/autodevops
- Review Apps - docs.gitlab.com/ee/ci/review_apps
""",
        },
        {
            "order_index": 8,
            "title": "Azure DevOps Pipelines",
            "slug": "azure-devops-pipelines",
            "difficulty": "intermediate",
            "content": """# Azure DevOps Pipelines

------------------------------------------------------------

## Introduktion

Föreställ dig att du arbetar i ett Microsoft-centrerat företag med Azure-infrastruktur, Windows-utvecklare och behov av enterprise compliance. Azure DevOps Pipelines är den naturliga lösningen - en komplett CI/CD-plattform djupt integrerad med Azure-ekosystemet.

I denna modul lär du dig att behärska Azure DevOps Pipelines - från YAML-konfiguration till avancerade multi-stage deployments med approvals och gates.

### Lärandemål

Efter denna modul kommer du att:

- Förstå Azure DevOps Pipeline-hierarkin (Stages, Jobs, Steps)
- Kunna skapa och konfigurera YAML-baserade pipelines
- Behärska templates för återanvändning och standardisering
- Implementera multi-stage deployments med environments
- Hantera secrets med Variable Groups och Azure Key Vault

------------------------------------------------------------

## Teori

### Varför Azure DevOps Pipelines?

Azure DevOps är Microsofts kompletta DevOps-plattform med djup Azure-integration.

**Viktiga fördelar:**

| Fördel | Beskrivning |
|--------|-------------|
| **Azure-integration** | Native integration med alla Azure-tjänster |
| **Hybrid-support** | Microsoft-hosted och self-hosted agents |
| **Compliance** | SOC, ISO, HIPAA-certifierad |
| **Marketplace** | 1000+ extensions |
| **Komplett** | Repos, Boards, Artifacts, Test Plans |

### Pipeline-hierarki

```
+------------------------------------------------------------------+
|                 AZURE PIPELINES HIERARKI                         |
+------------------------------------------------------------------+
|                                                                  |
|   PIPELINE (azure-pipelines.yml)                                 |
|   |                                                              |
|   +--STAGE: Build                                                |
|   |  |                                                           |
|   |  +--JOB: BuildApp                                            |
|   |     |                                                        |
|   |     +--STEP: Checkout                                        |
|   |     +--STEP: Install Node                                    |
|   |     +--STEP: npm install                                     |
|   |     +--STEP: npm build                                       |
|   |     +--STEP: Publish Artifact                                |
|   |                                                              |
|   +--STAGE: Test                                                 |
|   |  +--JOB: UnitTests                                           |
|   |  +--JOB: IntegrationTests (parallel)                         |
|   |                                                              |
|   +--STAGE: Deploy                                               |
|      +--DEPLOYMENT: Production                                   |
|         +--ENVIRONMENT: prod (approvals)                         |
|                                                                  |
+------------------------------------------------------------------+
```

### Nyckelkoncept

| Koncept | Beskrivning |
|---------|-------------|
| **Pipeline** | YAML-fil som definierar hela flödet |
| **Stage** | Logisk grupp - t.ex. Build, Test, Deploy |
| **Job** | Körs på en agent, kan vara parallella |
| **Step** | Enskild task eller script |
| **Environment** | Target för deployment med policies |
| **Template** | Återanvändbar pipeline-komponent |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Din första Azure Pipeline

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
      - develop
  paths:
    include:
      - src/**
      - package.json

pr:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  nodeVersion: '20'
  npm_config_cache: $(Pipeline.Workspace)/.npm

stages:
  - stage: Build
    displayName: 'Build Stage'
    jobs:
      - job: BuildJob
        displayName: 'Build Application'
        steps:
          - task: NodeTool@0
            displayName: 'Install Node.js'
            inputs:
              versionSpec: $(nodeVersion)

          - task: Cache@2
            displayName: 'Cache npm'
            inputs:
              key: 'npm | "$(Agent.OS)" | package-lock.json'
              path: $(npm_config_cache)
              restoreKeys: |
                npm | "$(Agent.OS)"

          - script: npm ci
            displayName: 'Install dependencies'

          - script: npm run build
            displayName: 'Build application'

          - script: npm test -- --coverage
            displayName: 'Run tests'

          - task: PublishTestResults@2
            displayName: 'Publish test results'
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: '**/junit.xml'

          - task: PublishCodeCoverageResults@1
            displayName: 'Publish coverage'
            inputs:
              codeCoverageTool: 'Cobertura'
              summaryFileLocation: '**/coverage/cobertura-coverage.xml'

          - publish: $(System.DefaultWorkingDirectory)/dist
            artifact: app
            displayName: 'Publish artifact'
```

### Steg 2: Multi-Stage Pipeline med Environments

```yaml
# azure-pipelines.yml
trigger:
  - main

variables:
  - group: 'app-settings'
  - name: dockerRegistry
    value: 'myregistry.azurecr.io'

stages:
  # Build Stage
  - stage: Build
    displayName: 'Build'
    jobs:
      - job: BuildAndTest
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: Docker@2
            displayName: 'Build Docker image'
            inputs:
              containerRegistry: 'AzureContainerRegistry'
              repository: 'myapp'
              command: 'build'
              Dockerfile: 'Dockerfile'
              tags: |
                $(Build.BuildId)
                latest

          - task: Docker@2
            displayName: 'Push Docker image'
            inputs:
              containerRegistry: 'AzureContainerRegistry'
              repository: 'myapp'
              command: 'push'
              tags: |
                $(Build.BuildId)
                latest

  # Deploy to Staging
  - stage: DeployStaging
    displayName: 'Deploy to Staging'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployStaging
        displayName: 'Deploy to Staging'
        environment: 'staging'
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebAppContainer@1
                  displayName: 'Deploy to App Service'
                  inputs:
                    azureSubscription: 'Azure-Connection'
                    appName: 'myapp-staging'
                    containers: '$(dockerRegistry)/myapp:$(Build.BuildId)'

                - script: |
                    curl -f https://myapp-staging.azurewebsites.net/health
                  displayName: 'Smoke test'

  # Deploy to Production
  - stage: DeployProduction
    displayName: 'Deploy to Production'
    dependsOn: DeployStaging
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProduction
        displayName: 'Deploy to Production'
        environment: 'production'  # Har approvals konfigurerade
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            preDeploy:
              steps:
                - script: echo "Förbereder deployment..."
                  displayName: 'Pre-deploy'
            deploy:
              steps:
                - task: AzureWebAppContainer@1
                  inputs:
                    azureSubscription: 'Azure-Connection'
                    appName: 'myapp-production'
                    containers: '$(dockerRegistry)/myapp:$(Build.BuildId)'
            postRouteTraffic:
              steps:
                - script: |
                    npm run test:smoke -- --url=https://myapp.azurewebsites.net
                  displayName: 'Post-deploy verification'
            on:
              failure:
                steps:
                  - script: echo "Deployment failed!"
                    displayName: 'Handle failure'
```

### Steg 3: Templates för återanvändning

```yaml
# templates/node-build.yml
parameters:
  - name: nodeVersion
    type: string
    default: '20'
  - name: workingDirectory
    type: string
    default: '.'
  - name: buildCommand
    type: string
    default: 'npm run build'

steps:
  - task: NodeTool@0
    displayName: 'Install Node.js ${{ parameters.nodeVersion }}'
    inputs:
      versionSpec: ${{ parameters.nodeVersion }}

  - task: Cache@2
    displayName: 'Cache npm'
    inputs:
      key: 'npm | "$(Agent.OS)" | ${{ parameters.workingDirectory }}/package-lock.json'
      path: $(npm_config_cache)

  - script: npm ci
    displayName: 'Install dependencies'
    workingDirectory: ${{ parameters.workingDirectory }}

  - script: ${{ parameters.buildCommand }}
    displayName: 'Build'
    workingDirectory: ${{ parameters.workingDirectory }}
```

```yaml
# templates/deploy-webapp.yml
parameters:
  - name: environment
    type: string
  - name: appName
    type: string
  - name: azureSubscription
    type: string

jobs:
  - deployment: Deploy${{ parameters.environment }}
    displayName: 'Deploy to ${{ parameters.environment }}'
    environment: ${{ parameters.environment }}
    pool:
      vmImage: 'ubuntu-latest'
    strategy:
      runOnce:
        deploy:
          steps:
            - download: current
              artifact: app

            - task: AzureWebApp@1
              displayName: 'Deploy to ${{ parameters.appName }}'
              inputs:
                azureSubscription: ${{ parameters.azureSubscription }}
                appName: ${{ parameters.appName }}
                package: '$(Pipeline.Workspace)/app'

            - script: |
                curl -f https://${{ parameters.appName }}.azurewebsites.net/health
              displayName: 'Health check'
```

```yaml
# azure-pipelines.yml - använder templates
trigger:
  - main

stages:
  - stage: Build
    jobs:
      - job: BuildFrontend
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - template: templates/node-build.yml
            parameters:
              nodeVersion: '20'
              workingDirectory: 'apps/frontend'

          - publish: apps/frontend/dist
            artifact: frontend

      - job: BuildBackend
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - template: templates/node-build.yml
            parameters:
              nodeVersion: '18'
              workingDirectory: 'apps/backend'

          - publish: apps/backend/dist
            artifact: backend

  - stage: DeployStaging
    dependsOn: Build
    jobs:
      - template: templates/deploy-webapp.yml
        parameters:
          environment: 'staging'
          appName: 'myapp-staging'
          azureSubscription: 'Azure-Connection'

  - stage: DeployProduction
    dependsOn: DeployStaging
    jobs:
      - template: templates/deploy-webapp.yml
        parameters:
          environment: 'production'
          appName: 'myapp-production'
          azureSubscription: 'Azure-Connection'
```

### Steg 4: Secrets med Key Vault

```yaml
# azure-pipelines.yml
variables:
  - group: 'app-config'                 # Variable Group från Library
  - name: keyVaultName
    value: 'myapp-keyvault'

stages:
  - stage: Deploy
    jobs:
      - job: DeployWithSecrets
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          # Hämta secrets från Key Vault
          - task: AzureKeyVault@2
            displayName: 'Fetch secrets from Key Vault'
            inputs:
              azureSubscription: 'Azure-Connection'
              KeyVaultName: $(keyVaultName)
              SecretsFilter: '*'
              RunAsPreJob: true

          # Använd secrets
          - script: |
              echo "Configuring application..."
              # Secrets finns nu som variabler
            displayName: 'Configure'
            env:
              DATABASE_URL: $(DatabaseConnectionString)
              API_KEY: $(ExternalApiKey)

          # Deploy med secrets
          - task: AzureWebApp@1
            inputs:
              azureSubscription: 'Azure-Connection'
              appName: 'myapp'
              appSettings: |
                -DATABASE_URL "$(DatabaseConnectionString)"
                -API_KEY "$(ExternalApiKey)"
```

### Steg 5: Container Jobs med Services

```yaml
# azure-pipelines.yml
stages:
  - stage: Test
    jobs:
      - job: IntegrationTests
        displayName: 'Integration Tests'
        pool:
          vmImage: 'ubuntu-latest'
        services:
          postgres:
            image: postgres:15
            ports:
              - 5432:5432
            env:
              POSTGRES_DB: testdb
              POSTGRES_USER: testuser
              POSTGRES_PASSWORD: testpass
          redis:
            image: redis:7
            ports:
              - 6379:6379
        container: node:20
        steps:
          - script: |
              npm ci
              npm run db:migrate
              npm run test:integration
            displayName: 'Run integration tests'
            env:
              DATABASE_URL: postgresql://testuser:testpass@postgres:5432/testdb
              REDIS_URL: redis://redis:6379
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett CI/CD för .NET

```yaml
# azure-pipelines.yml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'
  dotnetVersion: '8.0.x'

stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: Build
        steps:
          - task: UseDotNet@2
            displayName: 'Install .NET'
            inputs:
              version: $(dotnetVersion)

          - task: DotNetCoreCLI@2
            displayName: 'Restore'
            inputs:
              command: 'restore'
              projects: '**/*.csproj'

          - task: DotNetCoreCLI@2
            displayName: 'Build'
            inputs:
              command: 'build'
              projects: '**/*.csproj'
              arguments: '--configuration $(buildConfiguration) --no-restore'

          - task: DotNetCoreCLI@2
            displayName: 'Test'
            inputs:
              command: 'test'
              projects: '**/*Tests.csproj'
              arguments: '--configuration $(buildConfiguration) --collect:"XPlat Code Coverage"'

          - task: PublishCodeCoverageResults@2
            displayName: 'Publish coverage'
            inputs:
              summaryFileLocation: '$(Agent.TempDirectory)/**/coverage.cobertura.xml'

          - task: DotNetCoreCLI@2
            displayName: 'Publish'
            inputs:
              command: 'publish'
              publishWebProjects: true
              arguments: '--configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)'

          - publish: $(Build.ArtifactStagingDirectory)
            artifact: drop

  - stage: DeployDev
    displayName: 'Deploy to Dev'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/develop'))
    jobs:
      - deployment: DeployDev
        environment: 'development'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'Dev-Azure'
                    appName: 'myapp-dev'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'

  - stage: DeployProd
    displayName: 'Deploy to Production'
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProd
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'Prod-Azure'
                    appName: 'myapp-prod'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'
                    deploymentMethod: 'zipDeploy'
                    slotName: 'staging'

                - task: AzureAppServiceManage@0
                  displayName: 'Swap slots'
                  inputs:
                    azureSubscription: 'Prod-Azure'
                    appName: 'myapp-prod'
                    action: 'Swap Slots'
                    sourceSlot: 'staging'
                    targetSlot: 'production'
```

### Exempel 2: Matrix Testing

```yaml
# azure-pipelines.yml
trigger:
  - main

stages:
  - stage: Test
    jobs:
      - job: CrossPlatformTest
        displayName: 'Test on multiple platforms'
        strategy:
          matrix:
            Linux_Node18:
              vmImage: 'ubuntu-latest'
              nodeVersion: '18'
            Linux_Node20:
              vmImage: 'ubuntu-latest'
              nodeVersion: '20'
            Windows_Node20:
              vmImage: 'windows-latest'
              nodeVersion: '20'
            Mac_Node20:
              vmImage: 'macos-latest'
              nodeVersion: '20'
          maxParallel: 4
        pool:
          vmImage: $(vmImage)
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: $(nodeVersion)

          - script: npm ci
            displayName: 'Install'

          - script: npm test
            displayName: 'Test'

          - task: PublishTestResults@2
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: '**/junit.xml'
              testRunTitle: '$(vmImage) - Node $(nodeVersion)'
```

------------------------------------------------------------

## Bästa Praxis

### Pipeline-organisation

```yaml
# BRA: Använd stages för logiska grupperingar
stages:
  - stage: Build
  - stage: Test
  - stage: DeployDev
  - stage: DeployStaging
  - stage: DeployProd

# BRA: Använd templates för återanvändning
steps:
  - template: templates/common-steps.yml

# BRA: Centralisera variabler
variables:
  - group: 'shared-config'
  - template: variables/common.yml
```

### Säkerhet

```yaml
# BRA: Använd Service Connections med minsta möjliga behörighet
# BRA: Använd Key Vault för secrets
# BRA: Aktivera branch policies

# Kräv PR för main
trigger: none  # Trigga endast via PR

pr:
  branches:
    include:
      - main
  autoCancel: true
```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Artifact-hantering

```yaml
# FEL: Använder fel artifact-namn
- download: current
  artifact: wrong-name            # Finns inte!

# RÄTT: Matcha publish och download
- publish: dist
  artifact: app
# ...
- download: current
  artifact: app
```

### Problem 2: Condition-syntax

```yaml
# FEL: Fel condition syntax
condition: variables.Build.SourceBranch == 'refs/heads/main'

# RÄTT: Använd eq() funktion
condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
```

------------------------------------------------------------

## Övningar

### Övning 1: Multi-Stage Pipeline

<details>
<summary>Visa övning</summary>

**Mål:** Skapa en komplett pipeline med Build, Test, Deploy stages.

**Uppgift:**

1. Konfigurera triggers för main och PRs
2. Implementera Build stage med caching
3. Lägg till Test stage med code coverage
4. Implementera Deploy stages för staging och prod
5. Konfigurera environment approvals

**Se Steg 2 för lösning.**

</details>

### Övning 2: Template Library

<details>
<summary>Visa övning</summary>

**Mål:** Skapa återanvändbara templates.

**Uppgift:**

1. Skapa build template med parametrar
2. Skapa deploy template för Azure Web Apps
3. Använd templates i huvudpipeline

**Se Steg 3 för lösning.**

</details>

### Övning 3: Key Vault Integration

<details>
<summary>Visa övning</summary>

**Mål:** Implementera säker secret-hantering.

**Uppgift:**

1. Konfigurera Azure Key Vault
2. Länka till Variable Group
3. Använd secrets i pipeline
4. Konfigurera app settings från secrets

**Se Steg 4 för lösning.**

</details>

------------------------------------------------------------

## Kopplingar

| Modul | Koppling |
|-------|----------|
| **GitHub Actions** | Alternativ CI/CD-plattform |
| **Docker** | Container builds och registry |
| **Kubernetes** | AKS deployment |
| **Terraform** | Infrastructure as Code |
| **Azure** | Native integration |

------------------------------------------------------------

## Sammanfattning

Azure DevOps Pipelines erbjuder enterprise-ready CI/CD:

**Nyckelkoncept:**
- Hierarkisk struktur: Pipeline → Stage → Job → Step
- Templates för standardisering och återanvändning
- Environments med approvals och gates
- Deep Azure-integration

**Styrkor:**
- Hybrid agents (Microsoft-hosted och self-hosted)
- Compliance och enterprise-support
- Variable Groups och Key Vault integration

------------------------------------------------------------

## Nyckelkommandon

| Syntax | Beskrivning |
|--------|-------------|
| `trigger:` | Branch-triggers |
| `pr:` | Pull request-triggers |
| `pool:` | Agent-konfiguration |
| `stages:` | Pipeline stages |
| `jobs:` | Jobs inom stage |
| `steps:` | Steps inom job |
| `template:` | Referera template |
| `variables:` | Definiera variabler |
| `deployment:` | Deployment job |
| `environment:` | Target environment |

------------------------------------------------------------

## Referenser

- Azure Pipelines Documentation - docs.microsoft.com/azure/devops/pipelines
- YAML Schema Reference - docs.microsoft.com/azure/devops/pipelines/yaml-schema
- Environments - docs.microsoft.com/azure/devops/pipelines/process/environments
- Templates - docs.microsoft.com/azure/devops/pipelines/process/templates
- Key Vault Integration - docs.microsoft.com/azure/devops/pipelines/release/azure-key-vault
""",
        },
        {
            "order_index": 9,
            "title": "Container-based CI/CD",
            "slug": "container-based-cicd",
            "difficulty": "intermediate",
            "content": """# Container-based CI/CD

------------------------------------------------------------

## Introduktion

Efter denna modul mass du kunna:
- Bygga och optimera Docker images för CI/CD-pipelines
- Implementera multi-stage builds för minimala production images
- Säkerhetsscanna container images med Trivy, Grype och Snyk
- Konfigurera container registries och cache-strategier
- Köra tester i isolerade containermiljöer

------------------------------------------------------------

## Introduktion

Container-baserad CI/CD revolutionerar hur vi bygger, testar och deployar applikationer genom att garantera fullständig konsistens mellan utvecklingsmiljö och produktion. Genom att paketera applikationer med alla dependencies eliminerar containers det klassiska "works on my machine"-problemet och möjliggör snabbare, mer pålitliga pipelines med perfekt reproducerbarhet.

------------------------------------------------------------

## Teori

### Varför Container-baserad CI/CD?

Container-teknologi har fundamentalt förändrat CI/CD genom att erbjuda flera avgörande fördelar:

```
TRADITIONELL CI/CD VS CONTAINER-BASERAD CI/CD
============================================

TRADITIONELL:
+------------------+     +------------------+     +------------------+
|   Dev Machine    |     |   CI Server      |     |   Production     |
|------------------|     |------------------|     |------------------|
| Node 18          |     | Node 16          |     | Node 20          |
| npm 9.x          |     | npm 8.x          |     | npm 10.x         |
| Linux/Mac/Win    |     | Ubuntu 20.04     |     | Ubuntu 22.04     |
| Lokal config     |     | CI config        |     | Prod config      |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
   "Fungerar!"              "Fungerar?"              "Kraschar!"

CONTAINER-BASERAD:
+------------------+     +------------------+     +------------------+
|   Dev Machine    |     |   CI Server      |     |   Production     |
|------------------|     |------------------|     |------------------|
| Docker           |     | Docker           |     | Docker/K8s       |
|   +----------+   |     |   +----------+   |     |   +----------+   |
|   | Same     |   |     |   | Same     |   |     |   | Same     |   |
|   | Image    |   |     |   | Image    |   |     |   | Image    |   |
|   +----------+   |     |   +----------+   |     |   +----------+   |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
   "Fungerar!"               "Fungerar!"              "Fungerar!"
```

### Container CI/CD Flow

En modern container-baserad pipeline följer ett strukturerat flöde:

```
CONTAINER CI/CD PIPELINE FLÖDE
==============================

                    +-------------------+
                    |   Git Push        |
                    +-------------------+
                            |
                            v
+-----------------------------------------------------------+
|                     BUILD STAGE                            |
|-----------------------------------------------------------|
|  1. Checkout kod                                          |
|  2. Multi-stage Docker build                              |
|  3. Layer caching för snabbhet                            |
|  4. Generera build metadata                               |
+-----------------------------------------------------------+
                            |
                            v
+-----------------------------------------------------------+
|                     TEST STAGE                             |
|-----------------------------------------------------------|
|  1. Kör unit tests i container                            |
|  2. Container structure tests                              |
|  3. Integration tests med testcontainers                  |
+-----------------------------------------------------------+
                            |
                            v
+-----------------------------------------------------------+
|                     SCAN STAGE                             |
|-----------------------------------------------------------|
|  1. Vulnerability scanning (Trivy/Grype)                  |
|  2. License compliance                                     |
|  3. SBOM generation                                        |
|  4. Policy enforcement                                     |
+-----------------------------------------------------------+
                            |
                            v
+-----------------------------------------------------------+
|                     PUSH STAGE                             |
|-----------------------------------------------------------|
|  1. Tag image med SHA/version                             |
|  2. Push till container registry                          |
|  3. Sign image (cosign/notation)                          |
|  4. Update cache layers                                    |
+-----------------------------------------------------------+
                            |
                            v
+-----------------------------------------------------------+
|                    DEPLOY STAGE                            |
|-----------------------------------------------------------|
|  1. Pull från registry                                    |
|  2. Deploy till Kubernetes/ECS/Cloud Run                  |
|  3. Health checks                                          |
|  4. Rollback vid fel                                       |
+-----------------------------------------------------------+
```

### Multi-Stage Builds - Teorin

Multi-stage builds är nyckeln till små, säkra production images:

```
MULTI-STAGE BUILD STRATEGI
==========================

Stage 1: DEPENDENCIES (deps)
+---------------------------+
| Base: node:20-alpine      |
| - package.json            |
| - package-lock.json       |
| - npm ci                  |
| Storlek: ~500MB           |
+---------------------------+
            |
            v
Stage 2: BUILDER
+---------------------------+
| Base: node:20-alpine      |
| - Kopiera node_modules    |
| - Kopiera källkod         |
| - npm run build           |
| Storlek: ~800MB           |
+---------------------------+
            |
            v
Stage 3: TESTER
+---------------------------+
| Base: builder             |
| - Kör alla tester         |
| - Coverage rapport        |
| Kasseras efter CI         |
+---------------------------+
            |
            v
Stage 4: RUNNER (Production)
+---------------------------+
| Base: node:20-alpine      |
| - Endast prod deps        |
| - Endast dist/build       |
| - Non-root user           |
| Storlek: ~150MB           |
+---------------------------+

Resultat: 800MB --> 150MB (81% reduktion!)
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa Optimerad Multi-Stage Dockerfile

```dockerfile
# Dockerfile - Optimerad för CI/CD
# ================================

# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app

# Installera endast nödvändiga system-dependencies
RUN apk add --no-cache libc6-compat

# Kopiera package files först för bättre caching
COPY package.json package-lock.json ./

# Installera alla dependencies
RUN npm ci

# Skapa separat kopia av production dependencies
RUN cp -R node_modules prod_modules && \
    npm prune --production && \
    mv node_modules prod_only_modules && \
    mv prod_modules node_modules

# Stage 2: Builder
FROM node:20-alpine AS builder
WORKDIR /app

# Kopiera dependencies från deps stage
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Bygg applikationen
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build

# Stage 3: Tester (används i CI)
FROM builder AS tester
ENV NODE_ENV=test

# Kör tester
RUN npm run test:ci
RUN npm run lint

# Stage 4: Production Runner
FROM node:20-alpine AS runner
WORKDIR /app

# Säkerhetsinställningar
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Skapa non-root user
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 appuser

# Kopiera endast nödvändiga filer
COPY --from=deps --chown=appuser:nodejs /app/prod_only_modules ./node_modules
COPY --from=builder --chown=appuser:nodejs /app/dist ./dist
COPY --from=builder --chown=appuser:nodejs /app/package.json ./

# Byt till non-root user
USER appuser

# Exponera port
EXPOSE 3000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# Starta applikationen
CMD ["node", "dist/index.js"]
```

### Steg 2: Konfigurera GitHub Actions Container Workflow

```yaml
# .github/workflows/container-cicd.yml
name: Container CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # Job 1: Build och Test
  build-test:
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build test image
        uses: docker/build-push-action@v5
        with:
          context: .
          target: tester
          load: true
          tags: ${{ env.IMAGE_NAME }}:test
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=sha,prefix=
            type=semver,pattern={{version}}
            type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}

  # Job 2: Security Scanning
  security-scan:
    needs: build-test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build image for scanning
        run: |
          docker build -t scan-target:latest .

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'scan-target:latest'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
          vuln-type: 'os,library'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run Grype scanner
        uses: anchore/scan-action@v3
        with:
          image: 'scan-target:latest'
          fail-build: true
          severity-cutoff: high
          output-format: sarif

      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          image: 'scan-target:latest'
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.spdx.json

  # Job 3: Push till Registry
  push:
    needs: [build-test, security-scan]
    if: github.event_name != 'pull_request'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      id-token: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

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
            type=sha,prefix=
            type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          platforms: linux/amd64,linux/arm64

      - name: Sign container image
        uses: sigstore/cosign-installer@v3

      - name: Sign the image
        run: |
          cosign sign --yes ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}@${{ steps.build-push.outputs.digest }}
```

### Steg 3: Container Structure Tests

```yaml
# container-structure-test.yaml
schemaVersion: '2.0.0'

# Kommandotester
commandTests:
  - name: "Node version check"
    command: "node"
    args: ["--version"]
    expectedOutput: ["v20\\..*"]

  - name: "App user exists"
    command: "id"
    args: ["appuser"]
    expectedOutput: ["uid=1001"]

  - name: "No shell history"
    command: "cat"
    args: ["/home/appuser/.bash_history"]
    exitCode: 1

# Filexistenstester
fileExistenceTests:
  - name: 'Application directory exists'
    path: '/app'
    shouldExist: true
    permissions: 'drwxr-xr-x'

  - name: 'Package.json exists'
    path: '/app/package.json'
    shouldExist: true

  - name: 'No source code in production'
    path: '/app/src'
    shouldExist: false

  - name: 'No test files in production'
    path: '/app/__tests__'
    shouldExist: false

  - name: 'No dev dependencies'
    path: '/app/node_modules/.bin/jest'
    shouldExist: false

# Metadata tester
metadataTest:
  user: 'appuser'
  exposedPorts: ['3000']
  workdir: '/app'
  env:
    - key: 'NODE_ENV'
      value: 'production'

# Licenstester
licenseTests:
  - debian: false
  - files: ['/app/LICENSE']
```

### Steg 4: Kör Container Structure Tests i Pipeline

```yaml
# Lägg till i workflow
- name: Run container structure tests
  run: |
    # Installera container-structure-test
    curl -LO https://github.com/GoogleContainerTools/container-structure-test/releases/download/v1.16.0/container-structure-test-linux-amd64
    chmod +x container-structure-test-linux-amd64
    sudo mv container-structure-test-linux-amd64 /usr/local/bin/container-structure-test

    # Kör tester
    container-structure-test test \
      --image ${{ env.IMAGE_NAME }}:latest \
      --config container-structure-test.yaml
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Multi-Registry Push

```yaml
# Push till flera registries samtidigt
name: Multi-Registry Push

on:
  release:
    types: [published]

jobs:
  push-everywhere:
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

      - name: Login to Google Artifact Registry
        uses: docker/login-action@v3
        with:
          registry: europe-north1-docker.pkg.dev
          username: _json_key
          password: ${{ secrets.GCP_SA_KEY }}

      # Bygg och push till alla
      - name: Build and push to all registries
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          platforms: linux/amd64,linux/arm64
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.event.release.tag_name }}
            ghcr.io/${{ github.repository }}:latest
            docker.io/myorg/myapp:${{ github.event.release.tag_name }}
            docker.io/myorg/myapp:latest
            ${{ secrets.AWS_ACCOUNT }}.dkr.ecr.eu-north-1.amazonaws.com/myapp:${{ github.event.release.tag_name }}
            europe-north1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/myapp/api:${{ github.event.release.tag_name }}
```

### Exempel 2: Avancerad Caching

```yaml
# Optimerad caching för snabbare builds
- name: Build with advanced caching
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: ${{ steps.meta.outputs.tags }}
    cache-from: |
      type=gha
      type=registry,ref=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:buildcache
    cache-to: |
      type=gha,mode=max
      type=registry,ref=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:buildcache,mode=max
    build-args: |
      BUILDKIT_INLINE_CACHE=1
```

### Exempel 3: Kaniko Build (för Kubernetes runners)

```yaml
# kaniko-build.yaml - För Kubernetes-baserade runners
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: kaniko-build
spec:
  params:
    - name: IMAGE
      description: Name of the image to build
    - name: DOCKERFILE
      default: ./Dockerfile
    - name: CONTEXT
      default: ./
  workspaces:
    - name: source
  results:
    - name: IMAGE_DIGEST
  steps:
    - name: build-and-push
      image: gcr.io/kaniko-project/executor:latest
      args:
        - --dockerfile=$(params.DOCKERFILE)
        - --context=$(workspaces.source.path)/$(params.CONTEXT)
        - --destination=$(params.IMAGE)
        - --cache=true
        - --cache-ttl=24h
        - --snapshot-mode=redo
        - --use-new-run
      env:
        - name: DOCKER_CONFIG
          value: /kaniko/.docker
```

------------------------------------------------------------

## Bästa Praxis

### Image Optimization

```dockerfile
# Bästa praxis för minimala images

# 1. Använd specifika versioner, inte :latest
FROM node:20.10.0-alpine3.19 AS base

# 2. Minimera layers genom att kombinera RUN
RUN apk add --no-cache \
      curl \
      dumb-init \
    && rm -rf /var/cache/apk/*

# 3. Använd .dockerignore
# .dockerignore innehåll:
# node_modules
# .git
# *.md
# .env*
# coverage/
# .nyc_output/

# 4. Kopiera package files först för cache
COPY package*.json ./
RUN npm ci --only=production

# 5. Använd non-root user
USER node

# 6. Använd dumb-init för signalhantering
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/index.js"]
```

### Security Hardening

```dockerfile
# Säkerhetshärdad Dockerfile
FROM node:20-alpine AS production

# Uppdatera base image packages
RUN apk update && apk upgrade --no-cache

# Ta bort onödiga verktyg
RUN apk del --purge apk-tools

# Sätt säkra permissions
RUN chmod 755 /app && \
    chown -R node:node /app

# Förhindra privilege escalation
RUN chmod u-s /usr/bin/* && \
    chmod g-s /usr/bin/*

# Read-only filesystem där möjligt
USER node
WORKDIR /app

# Healthcheck utan curl (säkrare)
HEALTHCHECK --interval=30s --timeout=3s \
    CMD node -e "require('http').get('http://localhost:3000/health')"
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Stora Images

```dockerfile
# FEL: Alla dependencies i production image
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "index.js"]
# Resultat: ~1.2GB image

# RÄTT: Multi-stage med production deps endast
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production && npm cache clean --force
USER node
CMD ["node", "dist/index.js"]
# Resultat: ~150MB image
```

### Fallgrop 2: Root User

```dockerfile
# FEL: Kör som root
FROM node:20
WORKDIR /app
COPY . .
CMD ["node", "index.js"]

# RÄTT: Dedicated non-root user
FROM node:20-alpine
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup
WORKDIR /app
COPY --chown=appuser:appgroup . .
USER appuser
CMD ["node", "index.js"]
```

### Fallgrop 3: Ignorera Cache

```yaml
# FEL: Ingen caching
- name: Build image
  run: docker build -t myapp .

# RÄTT: Buildx med caching
- name: Build with cache
  uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

------------------------------------------------------------

## Övningar

### Övning 1: Optimera Dockerfile
<details>
<summary>Visa övning</summary>

**Mål:** Reducera image-storlek med 50%+

**Scenario:**
Du har en Node.js-applikation med följande Dockerfile som producerar en 1.1GB image:

```dockerfile
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["npm", "start"]
```

**Uppgifter:**
1. Konvertera till multi-stage build
2. Använd Alpine base image
3. Separera build och production dependencies
4. Lägg till non-root user
5. Implementera healthcheck

**Förväntat resultat:**
- Image under 200MB
- Non-root user
- Healthcheck fungerar
- Alla tester passerar

</details>

### Övning 2: Container Security Pipeline
<details>
<summary>Visa övning</summary>

**Mål:** Implementera fullständig säkerhetsscanning

**Scenario:**
Skapa en GitHub Actions workflow som:

1. Bygger container image
2. Kör Trivy vulnerability scan
3. Kör Grype scan
4. Genererar SBOM
5. Failar builden om CRITICAL eller HIGH vulnerabilities hittas
6. Laddar upp scan-resultat till GitHub Security

**Krav:**
- Använd matrix för att köra scanners parallellt
- Cache scan-databaser för snabbhet
- Generera SARIF-rapporter

</details>

### Övning 3: Multi-Registry Setup
<details>
<summary>Visa övning</summary>

**Mål:** Pusha till tre registries samtidigt

**Scenario:**
Konfigurera en pipeline som:

1. Bygger multi-platform images (amd64 + arm64)
2. Pushar till GitHub Container Registry
3. Pushar till Docker Hub
4. Pushar till AWS ECR
5. Taggar korrekt baserat på git ref

**Bonus:**
- Signera images med cosign
- Verifiera signatures innan deploy

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- Docker Mastery: Container-grunder
- Kubernetes Fundamentals: Container orchestration
- GitOps with ArgoCD: Deployment automation
- Pipeline Security: Säkerhetsintegration

### Förkunskaper:
- Docker basics (images, containers, Dockerfile)
- Git och version control
- CI/CD grundläggande koncept

### Bygger mot:
- Kubernetes deployment patterns
- Service mesh integration
- Multi-cloud strategies

------------------------------------------------------------

## Sammanfattning

Container-baserad CI/CD ger:

| Aspekt | Fördel |
|--------|--------|
| **Konsistens** | Samma miljö överallt |
| **Snabbhet** | Layer caching |
| **Säkerhet** | Image scanning |
| **Portabilitet** | Registry-agnostisk |

**Kom ihåg:**
1. Multi-stage builds för minimala images
2. Scanna alltid innan push
3. Använd non-root users
4. Cacha aggressivt för snabbhet
5. Signera production images

------------------------------------------------------------

## Nyckelkommandon

```bash
# Bygg med Buildx
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# Scanna med Trivy
trivy image --severity HIGH,CRITICAL myapp:latest

# Container structure test
container-structure-test test --image myapp:latest --config test.yaml

# Push till registry
docker push ghcr.io/org/myapp:latest

# Signera med cosign
cosign sign --key cosign.key ghcr.io/org/myapp:latest

# Verifiera signatur
cosign verify --key cosign.pub ghcr.io/org/myapp:latest

# Generera SBOM
syft myapp:latest -o spdx-json > sbom.json
```

------------------------------------------------------------

## Referenser

- Docker Documentation: https://docs.docker.com
- Buildx Documentation: https://docs.docker.com/buildx/
- Trivy: https://trivy.dev
- Cosign: https://docs.sigstore.dev/cosign/overview/
- Container Structure Tests: https://github.com/GoogleContainerTools/container-structure-test
- SBOM Best Practices: https://www.cisa.gov/sbom
""",
        },
        {
            "order_index": 10,
            "title": "GitOps with ArgoCD",
            "slug": "gitops-argocd",
            "difficulty": "advanced",
            "content": """# GitOps with ArgoCD

------------------------------------------------------------

## Introduktion

Efter denna modul måste du kunna:
- Förklara GitOps-principer och varför de förbättrar deployment-säkerhet
- Installera och konfigurera ArgoCD i ett Kubernetes-kluster
- Skapa och hantera ArgoCD Applications med sync policies
- Implementera App of Apps-mönstret för skalbara miljöer
- Integrera ArgoCD med Kustomize och Helm för miljövariationer

------------------------------------------------------------

## Introduktion

GitOps representerar en modern approach till infrastructure och application deployment där Git fungerar som den enda sanningskällan (single source of truth). ArgoCD är den ledande GitOps-operatorn för Kubernetes som kontinuerligt övervakar Git-repositories och automatiskt synkroniserar klusterstate med deklarativa konfigurationer. Denna approach ger oöverträffad audit trail, enkel rollback och förbättrad säkerhet genom att eliminera direkt klusteraccess.

------------------------------------------------------------

## Teori

### GitOps Fundamentala Principer

GitOps bygger på fyra kärnprinciper som tillsammans skapar en robust deployment-modell:

```
GITOPS PRINCIPER - ÖVERSIKT
===========================

+------------------------------------------------------------------+
|                    DEKLARATIV KONFIGURATION                       |
|------------------------------------------------------------------|
|  - All infrastruktur och applikationskonfiguration i YAML/JSON   |
|  - Beskriver ÖNSKAT state, inte HUR det ska uppnås               |
|  - Kubernetes-native med Custom Resources                         |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    VERSIONSHANTERAT I GIT                         |
|------------------------------------------------------------------|
|  - Varje ändring är en Git commit                                 |
|  - Pull requests för review och godkännande                       |
|  - Branch protection och merge policies                           |
|  - Komplett historik för alla ändringar                           |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    AUTOMATISK SYNKRONISERING                      |
|------------------------------------------------------------------|
|  - GitOps-operator (ArgoCD) övervakar Git repos                   |
|  - Detekterar drift mellan Git och kluster                        |
|  - Applicerar ändringar automatiskt eller via manuell sync        |
|  - Self-healing återställer oönskade ändringar                    |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    FULLSTÄNDIG AUDIT TRAIL                        |
|------------------------------------------------------------------|
|  - Git history = komplett ändringslogg                            |
|  - Vem, vad, när för varje deployment                             |
|  - Compliance och säkerhetsrapportering                           |
|  - Enkel rollback med git revert                                  |
+------------------------------------------------------------------+
```

### Push vs Pull Deployment

```
TRADITIONELL PUSH-MODELL VS GITOPS PULL-MODELL
==============================================

PUSH-MODELL (CI/CD-driven):

  Developer     CI/CD Server      Kubernetes
     |              |                 |
     |-- push ---->|                  |
     |              |-- kubectl ----->|
     |              |   apply         |
     |              |                 |

  Problem:
  - CI behöver kluster-credentials
  - Svårt att spåra ändringar
  - Ingen drift-detection
  - Manuell rollback

PULL-MODELL (GitOps):

  Developer     Git Repo       ArgoCD        Kubernetes
     |             |              |               |
     |-- push ---->|              |               |
     |             |<-- poll -----|               |
     |             |              |-- sync ------>|
     |             |              |               |
     |             |              |<-- monitor ---|
     |             |              |               |

  Fördelar:
  - Git är enda access point
  - Automatisk drift-detection
  - Self-healing
  - Audit trail i Git
  - Enkel rollback (git revert)
```

### ArgoCD Arkitektur

```
ARGOCD ARKITEKTUR
=================

+------------------------------------------------------------------+
|                        ARGOCD SERVER                              |
|------------------------------------------------------------------|
|                                                                   |
|   +------------------+    +------------------+                    |
|   |   API Server     |    |   Web UI         |                    |
|   |------------------|    |------------------|                    |
|   | - REST API       |    | - Dashboard      |                    |
|   | - gRPC           |    | - App status     |                    |
|   | - Auth           |    | - Sync actions   |                    |
|   +------------------+    +------------------+                    |
|                                                                   |
+------------------------------------------------------------------+
         |                           |
         v                           v
+------------------+    +------------------+    +------------------+
|   Repo Server    |    |   Application    |    |   Dex (SSO)      |
|------------------|    |   Controller     |    |------------------|
| - Clone repos    |    |------------------|    | - LDAP           |
| - Generate       |    | - Watches apps   |    | - OIDC           |
|   manifests      |    | - Compares state |    | - SAML           |
| - Kustomize/Helm |    | - Syncs changes  |    +------------------+
+------------------+    +------------------+
         |                      |
         v                      v
+------------------+    +------------------+
|   Git Repos      |    |   Kubernetes     |
|------------------|    |   Clusters       |
| - Config repos   |    |------------------|
| - App repos      |    | - Target clusters|
| - Helm charts    |    | - In-cluster     |
+------------------+    | - External       |
                        +------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Installera ArgoCD

```bash
# Skapa namespace för ArgoCD
kubectl create namespace argocd

# Installera ArgoCD (standard installation)
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Alternativ: Installation med Helm för mer kontroll
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

helm install argocd argo/argo-cd \
  --namespace argocd \
  --create-namespace \
  --set configs.params."server\\.insecure"=true \
  --set server.service.type=LoadBalancer \
  --set controller.replicas=2 \
  --set repoServer.replicas=2

# Vänta på att pods är redo
kubectl wait --for=condition=Ready pods --all -n argocd --timeout=300s

# Hämta initial admin-lösenord
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d && echo

# Exponera ArgoCD UI lokalt
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Logga in via CLI
argocd login localhost:8080 --username admin --password <lösenord>

# Ändra admin-lösenord
argocd account update-password
```

### Steg 2: Konfigurera Git Repository

```bash
# Lägg till Git repository
argocd repo add https://github.com/myorg/gitops-config.git \
  --username git \
  --password $GITHUB_TOKEN

# För SSH-autentisering
argocd repo add git@github.com:myorg/gitops-config.git \
  --ssh-private-key-path ~/.ssh/argocd_deploy_key

# Verifiera repository connection
argocd repo list
```

### Steg 3: Skapa Första Application

```yaml
# argocd/applications/demo-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: demo-app
  namespace: argocd
  # Finalizer förhindrar borttagning av resurser vid app-radering
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  # Projekt för RBAC och resursgruppering
  project: default

  # Källa - var konfigurationen finns
  source:
    repoURL: https://github.com/myorg/demo-app.git
    targetRevision: main  # Branch, tag eller commit SHA
    path: k8s/overlays/staging  # Path till manifests

  # Destination - vart det ska deployas
  destination:
    server: https://kubernetes.default.svc  # In-cluster
    namespace: demo-staging

  # Sync policy - hur synkronisering ska ske
  syncPolicy:
    automated:
      prune: true       # Ta bort resurser som inte finns i Git
      selfHeal: true    # Återställ manuella ändringar
      allowEmpty: false # Förhindra deploy av tom app
    syncOptions:
      - CreateNamespace=true
      - PruneLast=true
      - ServerSideApply=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

```bash
# Applicera Application
kubectl apply -f argocd/applications/demo-app.yaml

# Verifiera status
argocd app get demo-app

# Manuell sync om automated inte är aktiverat
argocd app sync demo-app
```

### Steg 4: Implementera App of Apps Pattern

```yaml
# argocd/root-app.yaml - Root Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    targetRevision: main
    path: argocd/applications  # Katalog med alla Applications
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

```yaml
# argocd/applications/platform/cert-manager.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: cert-manager
  namespace: argocd
spec:
  project: platform
  source:
    repoURL: https://charts.jetstack.io
    chart: cert-manager
    targetRevision: v1.14.0
    helm:
      values: |
        installCRDs: true
        prometheus:
          enabled: true
  destination:
    server: https://kubernetes.default.svc
    namespace: cert-manager
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true

---
# argocd/applications/apps/frontend.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: frontend
  namespace: argocd
spec:
  project: production
  source:
    repoURL: https://github.com/myorg/frontend.git
    targetRevision: main
    path: k8s/production
  destination:
    server: https://kubernetes.default.svc
    namespace: frontend
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### Steg 5: Kustomize Integration

```yaml
# k8s/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: ghcr.io/myorg/api:latest
          ports:
            - containerPort: 8080
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "500m"
```

```yaml
# k8s/base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
  - configmap.yaml
```

```yaml
# k8s/overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
  - ../../base

# Sätt replicas
replicas:
  - name: api
    count: 5

# Uppdatera image tag
images:
  - name: ghcr.io/myorg/api
    newTag: v1.5.2

# Environment-specifika patches
patches:
  - target:
      kind: Deployment
      name: api
    patch: |
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/memory
        value: "512Mi"
      - op: replace
        path: /spec/template/spec/containers/0/resources/limits/memory
        value: "1Gi"

# Lägg till labels
commonLabels:
  environment: production
  team: platform
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Multi-Cluster Deployment

```yaml
# Registrera externa kluster
# argocd/clusters/production-eu.yaml
apiVersion: v1
kind: Secret
metadata:
  name: production-eu-cluster
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: production-eu
  server: https://k8s-eu.example.com:6443
  config: |
    {
      "bearerToken": "<service-account-token>",
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64-encoded-ca-cert>"
      }
    }
```

```yaml
# Application för multi-cluster
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: api-multicluster
  namespace: argocd
spec:
  generators:
    - clusters:
        selector:
          matchLabels:
            environment: production
  template:
    metadata:
      name: 'api-{{name}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/myorg/api.git
        targetRevision: main
        path: 'k8s/overlays/{{metadata.labels.region}}'
      destination:
        server: '{{server}}'
        namespace: api
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

### Exempel 2: ArgoCD Image Updater

```yaml
# Installation av Image Updater
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-image-updater/stable/manifests/install.yaml

# Konfigurera Application med Image Updater
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: api
  namespace: argocd
  annotations:
    # Aktivera image updater
    argocd-image-updater.argoproj.io/image-list: api=ghcr.io/myorg/api
    # Uppdateringsstrategi (semver, latest, digest)
    argocd-image-updater.argoproj.io/api.update-strategy: semver
    # Filtrera tillåtna tags
    argocd-image-updater.argoproj.io/api.allow-tags: regexp:^v[0-9]+\\.[0-9]+\\.[0-9]+$
    # Skriv tillbaka till Git (inte bara live state)
    argocd-image-updater.argoproj.io/write-back-method: git
    argocd-image-updater.argoproj.io/git-branch: main
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    targetRevision: main
    path: apps/api
  destination:
    server: https://kubernetes.default.svc
    namespace: api
```

### Exempel 3: Notification Integration

```yaml
# argocd-notifications-cm ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
data:
  # Slack integration
  service.slack: |
    token: $slack-token

  template.app-deployed: |
    message: |
      :white_check_mark: Application {{.app.metadata.name}} deployed!
      Revision: {{.app.status.sync.revision}}
      Environment: {{.app.spec.destination.namespace}}

  template.app-health-degraded: |
    message: |
      :warning: Application {{.app.metadata.name}} health degraded!
      Status: {{.app.status.health.status}}

  trigger.on-deployed: |
    - when: app.status.sync.status == 'Synced'
      send: [app-deployed]

  trigger.on-health-degraded: |
    - when: app.status.health.status == 'Degraded'
      send: [app-health-degraded]

  # Teams integration
  service.teams: |
    recipientUrls:
      devops-channel: $teams-webhook-url
```

------------------------------------------------------------

## Bästa Praxis

### Repository Structure

```
gitops-config/
├── argocd/
│   ├── applications/          # Application definitions
│   │   ├── platform/          # Infrastructure apps
│   │   │   ├── cert-manager.yaml
│   │   │   ├── external-dns.yaml
│   │   │   └── ingress-nginx.yaml
│   │   └── apps/              # Business applications
│   │       ├── api.yaml
│   │       └── frontend.yaml
│   └── projects/              # ArgoCD Projects (RBAC)
│       ├── platform.yaml
│       └── production.yaml
├── clusters/
│   ├── production/
│   │   ├── base/
│   │   └── overlays/
│   └── staging/
│       ├── base/
│       └── overlays/
└── apps/
    ├── api/
    │   ├── base/
    │   └── overlays/
    │       ├── staging/
    │       └── production/
    └── frontend/
        ├── base/
        └── overlays/
```

### Security Best Practices

```yaml
# ArgoCD Project med RBAC
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: production
  namespace: argocd
spec:
  description: Production applications

  # Tillåtna källrepon
  sourceRepos:
    - 'https://github.com/myorg/*'

  # Tillåtna destinations
  destinations:
    - namespace: 'prod-*'
      server: https://kubernetes.default.svc

  # Förbjudna resurser
  namespaceResourceBlacklist:
    - group: ''
      kind: ResourceQuota
    - group: ''
      kind: LimitRange

  # Cluster-wide resources
  clusterResourceWhitelist:
    - group: ''
      kind: Namespace

  # Sync windows
  syncWindows:
    - kind: deny
      schedule: '* * * * 0'  # Ingen deploy på söndagar
      duration: 24h
      applications: ['*']
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Saknad Finalizer

```yaml
# FEL: Resurser tas inte bort vid app-delete
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
spec:
  # ... config

# RÄTT: Lägg till finalizer
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  # ... config
```

### Fallgrop 2: Drift genom manuella ändringar

```yaml
# FEL: Ingen selfHeal - drift upptäcks men fixas inte
syncPolicy:
  automated:
    prune: true

# RÄTT: Aktivera selfHeal
syncPolicy:
  automated:
    prune: true
    selfHeal: true  # Återställer manuella ändringar automatiskt
```

### Fallgrop 3: Credentials i Git

```yaml
# FEL: Secrets i vanlig YAML i Git
apiVersion: v1
kind: Secret
data:
  password: bXlwYXNzd29yZA==  # Base64 är INTE kryptering!

# RÄTT: Använd Sealed Secrets eller External Secrets
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
spec:
  encryptedData:
    password: AgBy3i4OJSWK...  # Krypterat med cluster-specifik nyckel
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande ArgoCD Setup
<details>
<summary>Visa övning</summary>

**Mål:** Installera ArgoCD och deploya en enkel applikation

**Uppgifter:**
1. Installera ArgoCD i ett Kubernetes-kluster (minikube/kind fungerar)
2. Exponera ArgoCD UI och logga in
3. Skapa ett GitHub-repository med en enkel Kubernetes Deployment
4. Skapa en ArgoCD Application som pekar på ditt repository
5. Verifiera att synkronisering fungerar

**Förväntat resultat:**
- ArgoCD UI visar applikationen som "Synced" och "Healthy"
- Ändringar i Git reflekteras automatiskt i klustret

</details>

### Övning 2: App of Apps Implementation
<details>
<summary>Visa övning</summary>

**Mål:** Implementera App of Apps-mönstret för flera applikationer

**Scenario:**
Skapa en GitOps-struktur som hanterar:
- En frontend-applikation
- En backend-applikation
- Gemensam infrastruktur (Ingress, ConfigMaps)

**Krav:**
1. En root Application som hanterar alla andra Applications
2. Separata namespaces för frontend och backend
3. Kustomize overlays för staging och production
4. Automated sync med prune och selfHeal

</details>

### Övning 3: Multi-Environment Pipeline
<details>
<summary>Visa övning</summary>

**Mål:** Skapa en GitOps-baserad promotion-pipeline

**Scenario:**
Implementera promotion från staging till production:

1. Image byggs och pushas av CI
2. Image Updater uppdaterar staging automatiskt
3. Efter manuell review, uppdatera production via PR
4. ArgoCD synkar production

**Leverabler:**
- CI workflow som bygger och pushar images
- Image Updater konfiguration för staging
- Branch protection och PR-flöde för production

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- Kubernetes Fundamentals: Bas för ArgoCD
- Container-based CI/CD: Image building
- Pipeline Security: Secrets management i GitOps
- Monitoring CI/CD: Observability för ArgoCD

### Förkunskaper:
- Kubernetes grundläggande koncept
- Git workflows och branching
- YAML-syntax

### Bygger mot:
- Multi-cluster GitOps
- Progressive Delivery med Argo Rollouts
- Policy as Code med OPA/Gatekeeper

------------------------------------------------------------

## Sammanfattning

GitOps med ArgoCD ger:

| Aspekt | Fördel |
|--------|--------|
| **Säkerhet** | Ingen direkt klusteraccess behövs |
| **Audit** | Komplett historik i Git |
| **Rollback** | git revert = instant rollback |
| **Skalbarhet** | App of Apps för många applikationer |

**Kom ihåg:**
1. Git är alltid single source of truth
2. Använd App of Apps för skalbarhet
3. Aktivera selfHeal och prune för automation
4. Separera config-repos från app-repos
5. Implementera RBAC med ArgoCD Projects

------------------------------------------------------------

## Nyckelkommandon

```bash
# ArgoCD CLI
argocd login <server>
argocd app list
argocd app get <app-name>
argocd app sync <app-name>
argocd app diff <app-name>
argocd app history <app-name>
argocd app rollback <app-name> <history-id>

# Kubectl för ArgoCD
kubectl get applications -n argocd
kubectl describe application <app-name> -n argocd

# Visa sync status
argocd app get <app-name> --output json | jq '.status.sync'

# Force refresh från Git
argocd app get <app-name> --refresh

# Hard refresh (clear cache)
argocd app get <app-name> --hard-refresh
```

------------------------------------------------------------

## Referenser

- ArgoCD Documentation: https://argo-cd.readthedocs.io
- GitOps Principles: https://opengitops.dev
- ArgoCD Best Practices: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
- Kustomize: https://kustomize.io
- Argo Rollouts: https://argoproj.github.io/rollouts/
- Sealed Secrets: https://sealed-secrets.netlify.app
""",
        },
        {
            "order_index": 11,
            "title": "Secrets Management",
            "slug": "secrets-management",
            "difficulty": "advanced",
            "content": """# Secrets Management i CI/CD

------------------------------------------------------------

## Introduktion

Efter denna modul måste du kunna:
- Förklara varför secrets aldrig ska finnas i kod eller Git
- Konfigurera GitHub Actions med repository och environment secrets
- Implementera OIDC-baserad autentisering mot molnleverantörer
- Använda HashiCorp Vault för centraliserad secrets management
- Implementera Sealed Secrets och SOPS för GitOps-workflows

------------------------------------------------------------

## Introduktion

Secrets management är en av de mest kritiska aspekterna av CI/CD-säkerhet. Exponerade API-nycklar, databasuppgifter eller molncredentials kan leda till katastrofala dataintrång som kostar miljoner i skadestånd och förlorat förtroende. Denna modul täcker moderna strategier för att hantera secrets säkert genom hela deployment-pipelinen, från utveckling till produktion.

------------------------------------------------------------

## Teori

### Varför Secrets Management är Kritiskt

```
KONSEKVENSER AV SECRETS-LÄCKAGE
================================

+------------------------------------------------------------------+
|                    SCENARIO: API-NYCKEL I GIT                     |
+------------------------------------------------------------------+
|                                                                   |
|   Utvecklare pushar kod med AWS credentials                       |
|                           |                                       |
|                           v                                       |
|   GitHub-bots scannar publika repos inom SEKUNDER                |
|                           |                                       |
|                           v                                       |
|   Angripare får tillgång till AWS-kontot                         |
|                           |                                       |
|                           v                                       |
|   +------------------+  +------------------+  +------------------+|
|   | Crypto Mining    |  | Data Exfiltration|  | Ransomware       ||
|   | $50,000/dag      |  | Kunddata läcker  |  | Hela infra låst  ||
|   +------------------+  +------------------+  +------------------+|
|                                                                   |
|   TOTAL KOSTNAD: $100,000 - $10,000,000+                         |
+------------------------------------------------------------------+

VERKLIGA EXEMPEL:
- Uber (2016): 57 miljoner användares data exponerad - $148M böter
- Capital One (2019): 100M kunduppgifter - $80M böter
- Codecov (2021): Supply chain attack via läckt credential
```

### Secrets Management Strategier

```
SECRETS MANAGEMENT PYRAMID
==========================

                    +----------------+
                    |    OIDC        |  <-- BÄST: Inga statiska secrets
                    |  Federation    |      Kortlivade tokens
                    +----------------+
                           |
              +------------------------+
              |    Secret Managers     |  <-- BRA: Centraliserat
              |  Vault, AWS SM, GCP SM |      Åtkomstkontroll
              +------------------------+      Audit logging
                           |
         +--------------------------------+
         |      Encrypted Secrets         |  <-- OK: Krypterat i Git
         |   Sealed Secrets, SOPS, git-crypt |    Fungerar med GitOps
         +--------------------------------+
                           |
    +----------------------------------------+
    |         Environment Variables           |  <-- MINIMUM: Inte i kod
    |      GitHub Secrets, GitLab Variables   |      Men synliga i logs
    +----------------------------------------+
                           |
+------------------------------------------------+
|              ALDRIG: Secrets i Kod              |  <-- FÖRBJUDET
|        Hardcoded passwords, API keys            |
+------------------------------------------------+
```

### OIDC - Identitetsfederation

```
OIDC AUTENTISERINGSFLÖDE
========================

GitHub Actions                  Cloud Provider (AWS/GCP/Azure)
      |                                    |
      |  1. Begär OIDC token               |
      |  från GitHub                       |
      |                                    |
      v                                    |
+-------------+                            |
| OIDC Token  |                            |
| - iss: github.com                        |
| - sub: repo:org/name:ref:main            |
| - aud: sts.amazonaws.com                 |
+-------------+                            |
      |                                    |
      |  2. Presentera token               |
      +----------------------------------->|
      |                                    |
      |  3. Verifiera token                |
      |     - Signatur OK?                 |
      |     - Issuer trusted?              |
      |     - Claims matchar policy?       |
      |                                    |
      |  4. Utfärda kortlivad credential   |
      |<-----------------------------------+
      |                                    |
      v                                    |
+-------------+                            |
| AWS Creds   |                            |
| - 1h TTL    |                            |
| - Begränsad |                            |
|   access    |                            |
+-------------+                            |

FÖRDELAR MED OIDC:
- Inga långlivade secrets att hantera
- Automatisk rotation (varje token är unikt)
- Granulär access control per repo/branch
- Fullständig audit trail
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera GitHub Repository Secrets

```bash
# Via GitHub CLI
gh secret set AWS_ACCESS_KEY_ID --body "AKIA..."
gh secret set AWS_SECRET_ACCESS_KEY --body "..."

# Lista secrets (visar bara namn, inte värden)
gh secret list

# Ta bort secret
gh secret delete AWS_ACCESS_KEY_ID
```

```yaml
# .github/workflows/deploy.yml - Använda secrets
name: Deploy Application

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy with secrets
        run: |
          echo "Deploying to production..."
          ./deploy.sh
        env:
          # Repository secrets
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          # Inbyggda secrets
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Steg 2: Konfigurera Environment Secrets

```yaml
# Environments ger extra kontroll
name: Production Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://app.example.com

    steps:
      - uses: actions/checkout@v4

      # Environment-specifika secrets
      - name: Deploy to production
        run: ./deploy-prod.sh
        env:
          # Dessa secrets är specifika för production environment
          API_KEY: ${{ secrets.PROD_API_KEY }}
          DATABASE_URL: ${{ secrets.PROD_DATABASE_URL }}

# Environment Settings i GitHub:
# - Required reviewers: Kräv godkännande innan deploy
# - Wait timer: Fördröjning mellan godkännande och deploy
# - Deployment branches: Begränsa vilka branches som kan deploya
```

### Steg 3: Implementera OIDC med AWS

```yaml
# .github/workflows/deploy-oidc.yml
name: Deploy with OIDC

on:
  push:
    branches: [main]

permissions:
  id-token: write   # Krävs för OIDC
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials via OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: eu-north-1
          # Ingen secret key behövs!

      - name: Deploy to S3
        run: aws s3 sync ./dist s3://my-bucket/

      - name: Update ECS service
        run: |
          aws ecs update-service \
            --cluster production \
            --service api \
            --force-new-deployment
```

```hcl
# terraform/github-oidc.tf - Konfigurera AWS för OIDC
# OIDC Provider
resource "aws_iam_openid_connect_provider" "github" {
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

# IAM Role för GitHub Actions
resource "aws_iam_role" "github_actions" {
  name = "GitHubActionsRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = aws_iam_openid_connect_provider.github.arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
          }
          StringLike = {
            # Begränsa till specifikt repo och branch
            "token.actions.githubusercontent.com:sub" = "repo:myorg/myrepo:ref:refs/heads/main"
          }
        }
      }
    ]
  })
}

# Permissions för rollen
resource "aws_iam_role_policy_attachment" "github_actions_s3" {
  role       = aws_iam_role.github_actions.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}
```

### Steg 4: HashiCorp Vault Integration

```yaml
# .github/workflows/vault-secrets.yml
name: Deploy with Vault

on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Import secrets from Vault
        uses: hashicorp/vault-action@v2
        with:
          url: https://vault.mycompany.com
          method: jwt
          role: github-actions
          secrets: |
            secret/data/production/database url | DATABASE_URL ;
            secret/data/production/database username | DB_USERNAME ;
            secret/data/production/database password | DB_PASSWORD ;
            secret/data/production/api key | API_KEY

      - name: Use secrets
        run: |
          echo "Connecting to database..."
          ./deploy.sh
        env:
          DATABASE_URL: ${{ env.DATABASE_URL }}
          DB_USERNAME: ${{ env.DB_USERNAME }}
          DB_PASSWORD: ${{ env.DB_PASSWORD }}
          API_KEY: ${{ env.API_KEY }}
```

```hcl
# vault-config.hcl - Vault konfiguration
# JWT Auth Backend för GitHub Actions
resource "vault_jwt_auth_backend" "github" {
  path               = "jwt"
  oidc_discovery_url = "https://token.actions.githubusercontent.com"
  bound_issuer       = "https://token.actions.githubusercontent.com"
}

resource "vault_jwt_auth_backend_role" "github_actions" {
  backend        = vault_jwt_auth_backend.github.path
  role_name      = "github-actions"
  token_policies = ["github-actions-policy"]

  bound_claims = {
    repository = "myorg/myrepo"
  }

  user_claim = "actor"
  role_type  = "jwt"
  token_ttl  = 3600
}

# Policy för GitHub Actions
resource "vault_policy" "github_actions" {
  name = "github-actions-policy"

  policy = <<EOT
path "secret/data/production/*" {
  capabilities = ["read"]
}

path "aws/creds/deploy-role" {
  capabilities = ["read"]
}
EOT
}
```

### Steg 5: Sealed Secrets för GitOps

```bash
# Installera Sealed Secrets controller i Kubernetes
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm install sealed-secrets sealed-secrets/sealed-secrets \
  --namespace kube-system \
  --set-string fullnameOverride=sealed-secrets-controller

# Installera kubeseal CLI
brew install kubeseal  # macOS
# eller
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.24.0/kubeseal-0.24.0-linux-amd64.tar.gz
tar -xvf kubeseal-*.tar.gz
sudo install kubeseal /usr/local/bin/
```

```yaml
# 1. Skapa vanlig secret (ska INTE committas!)
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: database-credentials
  namespace: production
type: Opaque
stringData:
  username: admin
  password: SuperSecretPassword123!
  connection-string: postgresql://admin:SuperSecretPassword123!@db.example.com:5432/app
```

```bash
# 2. Kryptera med kubeseal
kubeseal --format yaml \
  --controller-namespace kube-system \
  --controller-name sealed-secrets-controller \
  < secret.yaml > sealed-secret.yaml

# Ta bort okrypterade filen!
rm secret.yaml
```

```yaml
# 3. sealed-secret.yaml - SÄKER att committa till Git!
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: database-credentials
  namespace: production
spec:
  encryptedData:
    username: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq...
    password: AgBjpKLMNO+xyz123abc456def789...
    connection-string: AgCkl9mNOPqr+stu098vwx765yza...
  template:
    metadata:
      name: database-credentials
      namespace: production
    type: Opaque
```

### Steg 6: SOPS för Krypterade Filer

```bash
# Installera SOPS
brew install sops  # macOS

# Generera age-nyckel (enkel och säker)
age-keygen -o ~/.config/sops/age/keys.txt
# Spara public key för .sops.yaml
```

```yaml
# .sops.yaml - Konfiguration för SOPS
creation_rules:
  # Production secrets - krypteras med AWS KMS
  - path_regex: environments/production/.*\.enc\.yaml$
    kms: arn:aws:kms:eu-north-1:123456789012:key/abc-123-def-456

  # Staging secrets - krypteras med age
  - path_regex: environments/staging/.*\.enc\.yaml$
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p

  # Development - lokal age-nyckel
  - path_regex: environments/dev/.*\.enc\.yaml$
    age: age1local...
```

```yaml
# environments/production/secrets.yaml - FÖRE kryptering
database:
  host: db.example.com
  port: 5432
  username: admin
  password: SuperSecretPassword123!

api:
  stripe_key: sk_live_abc123...
  sendgrid_key: SG.xyz789...

oauth:
  google_client_secret: GOCSPX-...
```

```bash
# Kryptera filen
sops -e environments/production/secrets.yaml > environments/production/secrets.enc.yaml

# Redigera krypterad fil direkt (dekrypterar i $EDITOR, krypterar vid save)
sops environments/production/secrets.enc.yaml

# Dekryptera till stdout
sops -d environments/production/secrets.enc.yaml

# Extrahera enskilt värde
sops -d --extract '["database"]["password"]' environments/production/secrets.enc.yaml
```

```yaml
# .github/workflows/deploy-with-sops.yml
name: Deploy with SOPS

on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: eu-north-1

      - name: Install SOPS
        run: |
          curl -LO https://github.com/getsops/sops/releases/download/v3.8.1/sops-v3.8.1.linux.amd64
          sudo mv sops-v3.8.1.linux.amd64 /usr/local/bin/sops
          sudo chmod +x /usr/local/bin/sops

      - name: Decrypt and deploy
        run: |
          # Dekryptera secrets
          sops -d environments/production/secrets.enc.yaml > /tmp/secrets.yaml

          # Exportera som environment variables
          export DATABASE_PASSWORD=$(yq '.database.password' /tmp/secrets.yaml)
          export API_KEY=$(yq '.api.stripe_key' /tmp/secrets.yaml)

          # Deploy
          ./deploy.sh

          # Rensa upp
          rm /tmp/secrets.yaml
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett Multi-Layer Secrets Setup

```yaml
# Kombinera flera strategier för defense in depth
name: Production Deploy

on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      # Layer 1: OIDC för cloud access
      - name: Configure AWS via OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: eu-north-1

      # Layer 2: Hämta secrets från Vault
      - name: Get secrets from Vault
        uses: hashicorp/vault-action@v2
        with:
          url: ${{ secrets.VAULT_URL }}
          method: jwt
          role: production-deploy
          secrets: |
            secret/data/production/app config | APP_CONFIG

      # Layer 3: Dekryptera SOPS-filer
      - name: Decrypt configuration
        run: |
          sops -d config/production.enc.yaml > /tmp/config.yaml

      # Layer 4: Environment secrets för känslig runtime config
      - name: Deploy
        run: ./deploy.sh
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
          APP_CONFIG: ${{ env.APP_CONFIG }}
```

### Exempel 2: External Secrets Operator

```yaml
# Kubernetes External Secrets med AWS Secrets Manager
# external-secrets-store.yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secrets-manager
  namespace: production
spec:
  provider:
    aws:
      service: SecretsManager
      region: eu-north-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa

---
# external-secret.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: database-credentials
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: SecretStore
    name: aws-secrets-manager
  target:
    name: database-credentials
    creationPolicy: Owner
  data:
    - secretKey: username
      remoteRef:
        key: production/database
        property: username
    - secretKey: password
      remoteRef:
        key: production/database
        property: password
    - secretKey: host
      remoteRef:
        key: production/database
        property: host
```

------------------------------------------------------------

## Bästa Praxis

### Secrets Hygiene

```yaml
# 1. Aldrig logga secrets
- name: Deploy (RÄTT)
  run: |
    # Använd --quiet eller redirect till /dev/null
    aws s3 cp . s3://bucket/ --quiet

- name: Deploy (FEL)
  run: |
    # Riskerar att logga credentials
    echo "Deploying with key: $API_KEY"  # ALDRIG!

# 2. Maskera secrets i logs
- name: Custom masking
  run: |
    # GitHub maskerar automatiskt kända secrets
    # Men för dynamiskt hämtade:
    echo "::add-mask::$DYNAMIC_SECRET"

# 3. Begränsa secret scope
jobs:
  build:
    # Ingen tillgång till secrets

  deploy:
    needs: build
    environment: production
    # Endast här finns production secrets
```

### Rotation och Audit

```bash
# Rotera secrets regelbundet
# AWS Secrets Manager med automatisk rotation
aws secretsmanager rotate-secret \
  --secret-id production/database \
  --rotation-lambda-arn arn:aws:lambda:eu-north-1:123456789012:function:RotateSecret

# Audit log för secrets access
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=GetSecretValue \
  --start-time 2024-01-01
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Secrets i Build Artifacts

```dockerfile
# FEL: Secret i Docker layer
FROM node:20
ARG DATABASE_URL
ENV DATABASE_URL=$DATABASE_URL
RUN npm run build

# RÄTT: Multi-stage utan secrets i final image
FROM node:20 AS builder
ARG DATABASE_URL
RUN npm run build

FROM node:20-alpine
COPY --from=builder /app/dist ./dist
# DATABASE_URL injiceras vid runtime, inte build
```

### Fallgrop 2: Secrets i Git History

```bash
# Om secret råkat committas:

# 1. Rotera secret OMEDELBART
# 2. Ta bort från historik med BFG eller git-filter-repo
bfg --replace-text passwords.txt repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 3. Force push (kräver att alla team members re-cloner)
git push --force --all
```

### Fallgrop 3: Över-privilegierade Secrets

```yaml
# FEL: En secret med full access
AWS_ACCESS_KEY_ID: AKIA... # Full AdministratorAccess

# RÄTT: Minimala permissions per use case
# deploy-secret: Endast S3 och ECS access
# monitoring-secret: Endast CloudWatch read
```

------------------------------------------------------------

## Övningar

### Övning 1: OIDC Implementation
<details>
<summary>Visa övning</summary>

**Mål:** Konfigurera OIDC mellan GitHub Actions och AWS

**Uppgifter:**
1. Skapa OIDC provider i AWS
2. Skapa IAM role med trust policy för ditt repo
3. Skapa GitHub Actions workflow som använder OIDC
4. Verifiera att ingen statisk credential behövs

**Verifiering:**
- Workflow kör framgångsrikt
- Inga AWS secrets i GitHub repository settings

</details>

### Övning 2: Vault Integration
<details>
<summary>Visa övning</summary>

**Mål:** Sätt upp HashiCorp Vault med GitHub Actions

**Uppgifter:**
1. Starta Vault i dev mode (eller använd HCP Vault)
2. Konfigurera JWT auth backend för GitHub
3. Skapa secrets och policy
4. Implementera workflow som hämtar secrets

**Krav:**
- JWT-baserad auth (ingen static token)
- Audit logging aktiverat
- Minimal policy (least privilege)

</details>

### Övning 3: GitOps Secrets med Sealed Secrets
<details>
<summary>Visa övning</summary>

**Mål:** Implementera GitOps-vänlig secrets management

**Scenario:**
Du har en Kubernetes-applikation som behöver:
- Database credentials
- API keys
- TLS certificates

**Uppgifter:**
1. Installera Sealed Secrets controller
2. Skapa och kryptera alla secrets
3. Commita SealedSecrets till Git
4. Verifiera att ArgoCD kan synka och dekryptera

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- Pipeline Security: Övergripande säkerhet
- GitOps with ArgoCD: Secrets i GitOps
- Kubernetes Security: Runtime secrets
- Compliance and Audit: Secrets audit

### Förkunskaper:
- CI/CD grundläggande koncept
- Kryptografi basics (symmetric/asymmetric)
- Cloud provider basics (IAM)

### Bygger mot:
- Zero Trust Architecture
- Secret-less deployments
- Hardware Security Modules (HSM)

------------------------------------------------------------

## Sammanfattning

Secrets Management är fundamentalt för CI/CD-säkerhet:

| Strategi | Användning | Säkerhetsnivå |
|----------|------------|---------------|
| **OIDC** | Cloud access | Högst |
| **Vault** | Enterprise | Hög |
| **Sealed Secrets** | GitOps | Medel-Hög |
| **GitHub Secrets** | Enkel setup | Medel |

**Kom ihåg:**
1. ALDRIG secrets i kod eller Git
2. OIDC > statiska credentials
3. Rotera secrets regelbundet
4. Audit all secrets access
5. Least privilege alltid

------------------------------------------------------------

## Nyckelkommandon

```bash
# GitHub CLI secrets
gh secret set SECRET_NAME
gh secret list
gh secret delete SECRET_NAME

# AWS Secrets Manager
aws secretsmanager create-secret --name my-secret --secret-string "value"
aws secretsmanager get-secret-value --secret-id my-secret

# Vault
vault kv put secret/myapp password=secret
vault kv get secret/myapp

# Sealed Secrets
kubeseal --format yaml < secret.yaml > sealed-secret.yaml
kubeseal --recovery-unseal --recovery-private-key key.pem < sealed-secret.yaml

# SOPS
sops -e secrets.yaml > secrets.enc.yaml
sops -d secrets.enc.yaml
sops --rotate secrets.enc.yaml
```

------------------------------------------------------------

## Referenser

- GitHub OIDC Documentation: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- HashiCorp Vault: https://www.vaultproject.io/docs
- AWS Secrets Manager: https://docs.aws.amazon.com/secretsmanager/
- Sealed Secrets: https://sealed-secrets.netlify.app
- SOPS: https://github.com/getsops/sops
- External Secrets Operator: https://external-secrets.io
""",
        },
        {
            "order_index": 12,
            "title": "Pipeline Optimization",
            "slug": "pipeline-optimization",
            "difficulty": "advanced",
            "content": """# Pipeline Optimization

------------------------------------------------------------

## Introduktion

Efter denna modul måste du kunna:
- Identifiera flaskhalsar i CI/CD-pipelines och mäta performance
- Implementera parallellisering för att maximera throughput
- Konfigurera effektiv caching för dependencies och builds
- Använda inkrementella builds i monorepo-miljöer
- Optimera runner-konfiguration för olika workloads

------------------------------------------------------------

## Introduktion

Pipeline-optimering är avgörande för developer experience och organisationens leveranskapacitet. En pipeline som tar 30 minuter istället för 5 minuter kostar inte bara i väntetid - den skapar context-switching, frustration och minskar frekvensen av deployments. Denna modul täcker beprövade tekniker för att dramatiskt snabba upp dina pipelines utan att kompromissa kvalitet.

------------------------------------------------------------

## Teori

### Varför Pipeline-hastighet Spelar Roll

```
KOSTNADEN AV LÅNGSAMMA PIPELINES
================================

Scenario: Team med 10 utvecklare, 20 PRs/dag

LÅNGSAM PIPELINE (30 min):
+------------------------------------------------------------------+
|  Utvecklare pushar kod                                            |
|      |                                                            |
|      v                                                            |
|  [========= 30 minuter väntan =========]                         |
|      |                                                            |
|  Context switch till annat arbete                                 |
|      |                                                            |
|  Pipeline klar - återgå till PR                                   |
|      |                                                            |
|  Ny context switch                                                |
|                                                                   |
|  Kostnad per PR: ~45 min (inkl context switch)                   |
|  Daglig kostnad: 20 PRs × 45 min = 15 timmar förlorat            |
|  Veckovis: 75 timmar = nästan 2 heltidsanställda!                |
+------------------------------------------------------------------+

SNABB PIPELINE (5 min):
+------------------------------------------------------------------+
|  Utvecklare pushar kod                                            |
|      |                                                            |
|      v                                                            |
|  [= 5 min =]  <- Kort nog att vänta                              |
|      |                                                            |
|  Direkt feedback, fortsätt arbeta                                |
|                                                                   |
|  Kostnad per PR: ~7 min                                          |
|  Daglig kostnad: 20 PRs × 7 min = 2.3 timmar                     |
|  Besparing: 12.7 timmar/dag = 63 timmar/vecka!                   |
+------------------------------------------------------------------+
```

### Optimeringsstrategier Översikt

```
PIPELINE OPTIMIZATION PYRAMID
=============================

                    +------------------+
                    |   ARKITEKTUR     |  Separera tjänster
                    |   Microservices  |  Mindre builds
                    +------------------+
                           |
              +------------------------+
              |    INKREMENTELLT       |  Bygg bara ändrat
              |    Turbo/Nx/Bazel      |  Smart caching
              +------------------------+
                           |
         +--------------------------------+
         |        PARALLELLISM            |  Matrix builds
         |     Sharding, Fan-out          |  Concurrent jobs
         +--------------------------------+
                           |
    +----------------------------------------+
    |             CACHING                     |  Dependencies
    |    Dependencies, Builds, Docker layers |  Build artifacts
    +----------------------------------------+
                           |
+------------------------------------------------+
|              SNABBARE RUNNERS                   |  Mer CPU/RAM
|        Larger runners, Self-hosted              |  Specialhårdvara
+------------------------------------------------+

TYPISK FÖRBÄTTRING:
- Snabbare runners: 10-20% snabbare
- Caching: 30-50% snabbare
- Parallellism: 50-70% snabbare
- Inkrementellt: 80-95% snabbare (monorepos)
```

### Flödesanalys för Optimering

```
IDENTIFIERA FLASKHALSAR
=======================

Pipeline Timeline (före optimering):
====================================

Job 1: Install      [========] 4 min
Job 2: Lint         [====] 2 min
Job 3: Type Check   [======] 3 min
Job 4: Unit Tests   [================] 8 min
Job 5: Build        [==========] 5 min
Job 6: E2E Tests    [====================] 10 min
Job 7: Deploy       [====] 2 min
                    |------------------------|
                    Total: 34 minuter (sekventiellt)

Pipeline Timeline (efter optimering):
=====================================

                    Parallellt:
Job 1: Install      [========] 4 min (cached: 30s)

Job 2: Lint         [=] 30s ─┐
Job 3: Type Check   [=] 30s ─┼── Parallellt
Job 4a: Tests 1/4   [===] 2m ┘
Job 4b: Tests 2/4   [===] 2m ─┐
Job 4c: Tests 3/4   [===] 2m ─┼── Parallellt sharding
Job 4d: Tests 4/4   [===] 2m ─┘

Job 5: Build        [==] 1 min (cached)
Job 6: E2E          [=====] 3 min (parallella browsers)
Job 7: Deploy       [=] 30s
                    |--------|
                    Total: ~8 minuter

FÖRBÄTTRING: 34 min → 8 min = 76% snabbare!
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Mät Nuvarande Performance

```yaml
# .github/workflows/ci.yml - Lägg till timing
name: CI Pipeline

on: [push, pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - name: Start timing
        id: start
        run: echo "time=$(date +%s)" >> $GITHUB_OUTPUT

      - uses: actions/checkout@v4

      - name: Get timing for each step
        run: |
          echo "Checkout done at: $(date +%s)"

      # ... resten av steps

      - name: Report total time
        if: always()
        env:
          START: ${{ steps.start.outputs.time }}
        run: |
          END=$(date +%s)
          DURATION=$((END - START))
          echo "::notice::Pipeline duration: ${DURATION} seconds"

          # Skicka till metrics system
          curl -s -X POST "${{ secrets.METRICS_URL }}/pipeline" \
            -H "Content-Type: application/json" \
            -d '{
              "repo": "${{ github.repository }}",
              "workflow": "${{ github.workflow }}",
              "duration_seconds": '"$DURATION"',
              "status": "${{ job.status }}",
              "sha": "${{ github.sha }}"
            }'
```

### Steg 2: Implementera Parallellism

```yaml
# Maximalt parallella jobs
name: Optimized CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  # Stage 1: Setup och cache (körs först)
  setup:
    runs-on: ubuntu-latest
    outputs:
      cache-key: ${{ steps.cache-key.outputs.key }}
    steps:
      - uses: actions/checkout@v4

      - name: Generate cache key
        id: cache-key
        run: echo "key=deps-${{ hashFiles('package-lock.json') }}" >> $GITHUB_OUTPUT

      - uses: actions/cache@v4
        id: cache
        with:
          path: node_modules
          key: ${{ steps.cache-key.outputs.key }}

      - name: Install dependencies
        if: steps.cache.outputs.cache-hit != 'true'
        run: npm ci

  # Stage 2: Parallella checks (kräver setup)
  lint:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ needs.setup.outputs.cache-key }}
      - run: npm run lint

  typecheck:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ needs.setup.outputs.cache-key }}
      - run: npm run typecheck

  # Stage 2: Parallella tester med sharding
  test:
    needs: setup
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ needs.setup.outputs.cache-key }}
      - name: Run tests (shard ${{ matrix.shard }}/4)
        run: npm test -- --shard=${{ matrix.shard }}/4

  # Stage 2: Parallella E2E-tester
  e2e:
    needs: setup
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        browser: [chromium, firefox, webkit]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ needs.setup.outputs.cache-key }}
      - name: Run E2E (${{ matrix.browser }})
        run: npx playwright test --project=${{ matrix.browser }}

  # Stage 3: Build (kan köras parallellt med tester)
  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ needs.setup.outputs.cache-key }}
      - uses: actions/cache@v4
        with:
          path: .next/cache
          key: nextjs-${{ hashFiles('package-lock.json') }}-${{ hashFiles('**/*.ts', '**/*.tsx') }}
          restore-keys: |
            nextjs-${{ hashFiles('package-lock.json') }}-
            nextjs-
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: dist/

  # Stage 4: Deploy (väntar på ALLA checks)
  deploy:
    needs: [lint, typecheck, test, e2e, build]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build
      - run: ./deploy.sh
```

### Steg 3: Avancerad Caching

```yaml
# Multi-layer caching strategi
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Layer 1: npm cache (globalt)
      - uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-global-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
          restore-keys: |
            npm-global-${{ runner.os }}-

      # Layer 2: node_modules (projekt-specifikt)
      - uses: actions/cache@v4
        id: node-modules
        with:
          path: node_modules
          key: node-modules-${{ hashFiles('package-lock.json') }}

      # Layer 3: Build cache (Next.js)
      - uses: actions/cache@v4
        with:
          path: |
            .next/cache
            dist/.cache
          key: build-${{ hashFiles('package-lock.json') }}-${{ hashFiles('src/**') }}
          restore-keys: |
            build-${{ hashFiles('package-lock.json') }}-
            build-

      # Layer 4: Turbo cache (monorepo)
      - uses: actions/cache@v4
        with:
          path: .turbo
          key: turbo-${{ runner.os }}-${{ github.sha }}
          restore-keys: |
            turbo-${{ runner.os }}-

      - name: Install
        if: steps.node-modules.outputs.cache-hit != 'true'
        run: npm ci

      - name: Build
        run: npm run build
```

### Steg 4: Inkrementella Builds för Monorepos

```yaml
# Använd Turborepo för smarta builds
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Behövs för att jämföra med tidigare commits

      - uses: actions/cache@v4
        with:
          path: .turbo
          key: turbo-${{ github.sha }}
          restore-keys: turbo-

      - run: npm ci

      # Kör bara det som ändrats sedan senaste main
      - name: Build changed packages
        run: npx turbo run build --filter='[origin/main]'
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: ${{ secrets.TURBO_TEAM }}

      # Eller med paths-filter för mer kontroll
      - uses: dorny/paths-filter@v3
        id: changes
        with:
          filters: |
            frontend:
              - 'apps/frontend/**'
              - 'packages/ui/**'
            backend:
              - 'apps/backend/**'
            docs:
              - 'docs/**'

      - name: Build frontend
        if: steps.changes.outputs.frontend == 'true'
        run: npx turbo run build --filter=frontend

      - name: Build backend
        if: steps.changes.outputs.backend == 'true'
        run: npx turbo run build --filter=backend
```

```json
// turbo.json - Turborepo konfiguration
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "build/**"],
      "cache": true
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "cache": true
    },
    "lint": {
      "outputs": [],
      "cache": true
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### Steg 5: Optimera Docker Builds

```yaml
# Snabba Docker builds
jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
          # Aktivera cache
          cache-from: type=gha
          cache-to: type=gha,mode=max
          # Parallella platforms
          platforms: linux/amd64,linux/arm64
          # Build arguments för cache-busting kontroll
          build-args: |
            BUILDKIT_INLINE_CACHE=1
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Before/After Optimization

```yaml
# FÖRE: 25 minuter total
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install          # 3 min
      - run: npm run lint         # 2 min
      - run: npm run typecheck    # 2 min
      - run: npm test             # 10 min
      - run: npm run build        # 5 min
      - run: npm run e2e          # 3 min

# EFTER: 6 minuter total
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: deps-${{ hashFiles('package-lock.json') }}
      - run: npm ci
        if: steps.cache.outputs.cache-hit != 'true'

  checks:
    needs: setup
    runs-on: ubuntu-latest
    strategy:
      matrix:
        check: [lint, typecheck]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: deps-${{ hashFiles('package-lock.json') }}
      - run: npm run ${{ matrix.check }}

  test:
    needs: setup
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shard: [1, 2, 3, 4, 5]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: node_modules
          key: deps-${{ hashFiles('package-lock.json') }}
      - run: npm test -- --shard=${{ matrix.shard }}/5

  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v4
        with:
          path: |
            node_modules
            .next/cache
          key: build-${{ hashFiles('package-lock.json', 'src/**') }}
      - run: npm run build

  e2e:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run e2e
```

------------------------------------------------------------

## Bästa Praxis

```yaml
# 1. Fail fast för snabb feedback
strategy:
  fail-fast: true  # Avbryt alla jobs om en failar

# 2. Använd rätt runner-storlek
runs-on: ubuntu-latest         # Standard
runs-on: ubuntu-latest-4-cores # Snabbare
runs-on: ubuntu-latest-16-cores # Mycket snabbare

# 3. Minimera checkout
- uses: actions/checkout@v4
  with:
    fetch-depth: 1  # Shallow clone (snabbare)
    sparse-checkout: |  # Endast nödvändiga filer
      src
      package.json
      package-lock.json

# 4. Använd composite actions för återanvändning
# .github/actions/setup/action.yml
name: 'Setup'
runs:
  using: 'composite'
  steps:
    - uses: actions/cache@v4
      with:
        path: node_modules
        key: deps-${{ hashFiles('package-lock.json') }}
    - run: npm ci
      if: steps.cache.outputs.cache-hit != 'true'
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Cache Invalidering

```yaml
# FEL: Cache uppdateras aldrig
- uses: actions/cache@v4
  with:
    path: node_modules
    key: node-modules  # Statisk nyckel!

# RÄTT: Inkludera hash av lock-fil
- uses: actions/cache@v4
  with:
    path: node_modules
    key: node-modules-${{ hashFiles('package-lock.json') }}
```

### Fallgrop 2: Onödig Sekventiell Körning

```yaml
# FEL: Lint väntar på test
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: npm test
  lint:
    needs: test  # Varför vänta?
    runs-on: ubuntu-latest
    steps:
      - run: npm run lint

# RÄTT: Parallellt
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: npm test
  lint:
    runs-on: ubuntu-latest  # Ingen needs!
    steps:
      - run: npm run lint
```

------------------------------------------------------------

## Övningar

### Övning 1: Parallellisera Pipeline
<details>
<summary>Visa övning</summary>

**Mål:** Reducera pipeline-tid med 50%+

**Scenario:**
Du har en pipeline som tar 20 minuter sekventiellt:
- Install: 3 min
- Lint: 2 min
- Test: 10 min
- Build: 5 min

**Uppgifter:**
1. Identifiera beroenden mellan stegen
2. Implementera parallella jobs
3. Lägg till test sharding
4. Mät förbättringen

</details>

### Övning 2: Monorepo Optimization
<details>
<summary>Visa övning</summary>

**Mål:** Bygg endast ändrade paket

**Scenario:**
Monorepo med 5 paket, full build tar 15 minuter.

**Uppgifter:**
1. Sätt upp Turborepo
2. Konfigurera remote caching
3. Implementera filter för ändrade paket
4. Mät tid för typisk PR (1 paket ändrat)

</details>

### Övning 3: Docker Build Optimization
<details>
<summary>Visa övning</summary>

**Mål:** Snabba upp Docker builds från 10 min till 2 min

**Uppgifter:**
1. Analysera Dockerfile layer-ordning
2. Implementera multi-stage build
3. Aktivera BuildKit caching
4. Konfigurera GitHub Actions cache

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- GitHub Actions: Workflow syntax
- Container-based CI/CD: Docker optimization
- Monorepo Patterns: Turborepo/Nx
- Self-Hosted Runners: Custom infrastructure

### Förkunskaper:
- CI/CD grundläggande koncept
- Caching-principer
- Parallell programmering basics

### Bygger mot:
- Enterprise CI/CD Patterns
- Platform Engineering
- Developer Experience optimization

------------------------------------------------------------

## Sammanfattning

Pipeline-optimering handlar om:

| Teknik | Typisk Förbättring |
|--------|-------------------|
| **Caching** | 30-50% |
| **Parallellism** | 50-70% |
| **Sharding** | 60-80% |
| **Inkrementellt** | 80-95% |

**Kom ihåg:**
1. Mät innan du optimerar
2. Parallellisera oberoende steg
3. Cacha allt som går
4. Inkrementella builds för monorepos
5. Iterera och mät igen

------------------------------------------------------------

## Nyckelkommandon

```bash
# Turbo commands
npx turbo run build --filter='[origin/main]'
npx turbo run build --dry-run
npx turbo run build --graph

# Jest sharding
npm test -- --shard=1/4
npm test -- --listTests

# Playwright sharding
npx playwright test --shard=1/4
npx playwright test --project=chromium

# GitHub Actions timing
gh run view <run-id> --json jobs | jq '.jobs[] | {name, duration: (.completedAt | fromdate) - (.startedAt | fromdate)}'
```

------------------------------------------------------------

## Referenser

- GitHub Actions Optimization: https://docs.github.com/en/actions/using-workflows/caching-dependencies
- Turborepo: https://turbo.build/repo/docs
- Nx: https://nx.dev
- Jest Sharding: https://jestjs.io/docs/cli#--shard
- Playwright Sharding: https://playwright.dev/docs/test-sharding
""",
        },
        {
            "order_index": 13,
            "title": "Multi-Environment Deployments",
            "slug": "multi-environment-deployments",
            "difficulty": "advanced",
            "content": """# Multi-Environment Deployments

------------------------------------------------------------

## Introduktion

Efter denna modul måste du kunna:
- Designa och implementera multi-environment deployment-strategier
- Konfigurera GitHub Environments med approvals och secrets
- Använda Kustomize för miljöspecifik Kubernetes-konfiguration
- Implementera Terraform workspaces för infrastructure per miljö
- Skapa kontrollerade promotion workflows mellan miljöer

------------------------------------------------------------

## Introduktion

Multi-environment deployments är fundamentalt för säker mjukvaruleverans. Genom att ha separata miljöer för utveckling, testning och produktion kan team validera ändringar stegvis innan de når användare. Denna approach minskar risken för produktionsincidenter och ger möjlighet att testa i produktionsliknande miljöer utan att påverka riktiga användare.

------------------------------------------------------------

## Teori

### Environment Hierarki

```
STANDARD ENVIRONMENT FLOW
=========================

+------------------------------------------------------------------+
|                    DEVELOPMENT ENVIRONMENT                        |
|------------------------------------------------------------------|
|  - Snabb iteration                                                |
|  - Utvecklarnas sandlåda                                          |
|  - Automatisk deploy vid varje push till develop                  |
|  - Lågkostnadsmiljö (mindre resurser)                            |
|  - Mock-tjänster och testdata                                     |
+------------------------------------------------------------------+
                              |
                              | Automatisk promotion
                              v
+------------------------------------------------------------------+
|                     STAGING ENVIRONMENT                           |
|------------------------------------------------------------------|
|  - Produktionslik konfiguration                                   |
|  - Integrationstester och E2E-tester                             |
|  - Performance testing                                            |
|  - QA-validering                                                  |
|  - Deploy vid merge till main                                     |
+------------------------------------------------------------------+
                              |
                              | Manuell approval + promotion
                              v
+------------------------------------------------------------------+
|                    PRODUCTION ENVIRONMENT                         |
|------------------------------------------------------------------|
|  - Riktig användartrafik                                          |
|  - Full skalning och redundans                                    |
|  - Strikt access control                                          |
|  - Rollback-möjlighet                                             |
|  - Monitoring och alerting                                        |
+------------------------------------------------------------------+

YTTERLIGARE MILJÖER (vid behov):
================================

+-------------------+    +-------------------+    +-------------------+
|    PREVIEW        |    |    CANARY         |    |    DISASTER       |
|-------------------|    |-------------------|    |    RECOVERY       |
| - Per-PR miljöer  |    | - Subset av       |    |-------------------|
| - Isolerad test   |    |   prod-trafik     |    | - Standby miljö   |
| - Auto-cleanup    |    | - Gradvis rollout |    | - Snabb failover  |
+-------------------+    +-------------------+    +-------------------+
```

### Konfigurationsstrategi

```
ENVIRONMENT CONFIGURATION MATRIX
================================

                    | Development | Staging    | Production
--------------------|-------------|------------|-------------
Replicas            | 1           | 2          | 5-10
CPU Request         | 100m        | 250m       | 500m
Memory Request      | 128Mi       | 256Mi      | 512Mi
Log Level           | debug       | info       | warn
Feature Flags       | All enabled | Beta       | Stable only
Database            | Local/Mock  | Shared     | Dedicated
SSL/TLS             | Optional    | Required   | Required
Monitoring          | Basic       | Full       | Full + Alerts
Access              | All devs    | Team leads | SRE + Approval
Auto-scaling        | Off         | Limited    | Full
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera GitHub Environments

```yaml
# .github/workflows/deploy.yml
name: Multi-Environment Deploy

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}
      image: ${{ steps.build.outputs.image }}
    steps:
      - uses: actions/checkout@v4

      - name: Generate version
        id: version
        run: |
          VERSION="${{ github.sha }}"
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      - name: Build application
        run: |
          npm ci
          npm run build

      - name: Build and push Docker image
        id: build
        run: |
          IMAGE="ghcr.io/${{ github.repository }}:${{ steps.version.outputs.version }}"
          docker build -t $IMAGE .
          docker push $IMAGE
          echo "image=$IMAGE" >> $GITHUB_OUTPUT

      - uses: actions/upload-artifact@v4
        with:
          name: build-${{ steps.version.outputs.version }}
          path: dist/

  # Deploy till Development
  deploy-dev:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment:
      name: development
      url: https://dev.myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to development
        run: |
          echo "Deploying ${{ needs.build.outputs.image }} to development"
          kubectl --context=dev set image deployment/myapp \
            app=${{ needs.build.outputs.image }}
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG }}

  # Deploy till Staging (auto vid main push)
  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to staging
        run: |
          kubectl --context=staging set image deployment/myapp \
            app=${{ needs.build.outputs.image }}
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG }}

      - name: Run smoke tests
        run: |
          npm run test:smoke -- --url=https://staging.myapp.com

      - name: Run E2E tests
        run: |
          npm run test:e2e -- --url=https://staging.myapp.com

  # Deploy till Production (kräver approval)
  deploy-production:
    needs: [build, deploy-staging]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to production
        run: |
          kubectl --context=production set image deployment/myapp \
            app=${{ needs.build.outputs.image }}
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG }}

      - name: Verify deployment
        run: |
          kubectl --context=production rollout status deployment/myapp --timeout=5m

      - name: Health check
        run: |
          for i in {1..10}; do
            if curl -sf https://myapp.com/health; then
              echo "Health check passed"
              exit 0
            fi
            sleep 10
          done
          echo "Health check failed"
          exit 1
```

### Steg 2: Kustomize för Kubernetes

```yaml
# k8s/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
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
          image: myapp:latest
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef:
                name: myapp-config
            - secretRef:
                name: myapp-secrets
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "200m"
          readinessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 15
            periodSeconds: 20
```

```yaml
# k8s/base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
  - ingress.yaml

commonLabels:
  app.kubernetes.io/name: myapp
```

```yaml
# k8s/overlays/development/kustomization.yaml
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
      - FEATURE_FLAGS=all

patches:
  - target:
      kind: Deployment
      name: myapp
    patch: |
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/memory
        value: "64Mi"
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/cpu
        value: "50m"
```

```yaml
# k8s/overlays/staging/kustomization.yaml
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
      - FEATURE_FLAGS=beta

images:
  - name: myapp
    newName: ghcr.io/myorg/myapp
```

```yaml
# k8s/overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
  - ../../base
  - hpa.yaml
  - pdb.yaml

replicas:
  - name: myapp
    count: 5

configMapGenerator:
  - name: myapp-config
    literals:
      - LOG_LEVEL=warn
      - ENV=production
      - FEATURE_FLAGS=stable

patches:
  - target:
      kind: Deployment
      name: myapp
    patch: |
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/memory
        value: "512Mi"
      - op: replace
        path: /spec/template/spec/containers/0/resources/requests/cpu
        value: "500m"
      - op: replace
        path: /spec/template/spec/containers/0/resources/limits/memory
        value: "1Gi"
      - op: replace
        path: /spec/template/spec/containers/0/resources/limits/cpu
        value: "1000m"

images:
  - name: myapp
    newName: ghcr.io/myorg/myapp
```

### Steg 3: Terraform Workspaces

```hcl
# terraform/main.tf
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
      db_class      = "db.t3.micro"
      domain        = "dev.myapp.com"
    }
    staging = {
      instance_type = "t3.medium"
      min_size      = 2
      max_size      = 4
      db_class      = "db.t3.small"
      domain        = "staging.myapp.com"
    }
    production = {
      instance_type = "t3.large"
      min_size      = 3
      max_size      = 20
      db_class      = "db.r6g.large"
      domain        = "myapp.com"
    }
  }

  config = local.env_config[var.environment]
}

# EKS Cluster
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "myapp-${var.environment}"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      instance_types = [local.config.instance_type]
      min_size       = local.config.min_size
      max_size       = local.config.max_size
      desired_size   = local.config.min_size
    }
  }

  tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# RDS Database
module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = "~> 6.0"

  identifier = "myapp-${var.environment}"

  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = local.config.db_class
  allocated_storage    = var.environment == "production" ? 100 : 20

  multi_az = var.environment == "production" ? true : false

  tags = {
    Environment = var.environment
  }
}
```

```yaml
# .github/workflows/terraform.yml
name: Terraform Deploy

on:
  push:
    branches: [main]
    paths:
      - 'terraform/**'
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        type: choice
        options:
          - development
          - staging
          - production

jobs:
  plan:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [development, staging, production]
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        working-directory: terraform
        run: terraform init

      - name: Select Workspace
        working-directory: terraform
        run: |
          terraform workspace select ${{ matrix.environment }} || \
          terraform workspace new ${{ matrix.environment }}

      - name: Terraform Plan
        working-directory: terraform
        run: terraform plan -var="environment=${{ matrix.environment }}" -out=tfplan

      - uses: actions/upload-artifact@v4
        with:
          name: tfplan-${{ matrix.environment }}
          path: terraform/tfplan

  apply:
    needs: plan
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [development, staging, production]
      max-parallel: 1
    environment: ${{ matrix.environment }}
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - uses: actions/download-artifact@v4
        with:
          name: tfplan-${{ matrix.environment }}
          path: terraform/

      - name: Terraform Apply
        working-directory: terraform
        run: |
          terraform workspace select ${{ matrix.environment }}
          terraform apply -auto-approve tfplan
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Preview Environments per PR

```yaml
# .github/workflows/preview.yml
name: Preview Environment

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  deploy-preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate preview URL
        id: preview
        run: |
          PREVIEW_ID="pr-${{ github.event.pull_request.number }}"
          echo "id=$PREVIEW_ID" >> $GITHUB_OUTPUT
          echo "url=https://$PREVIEW_ID.preview.myapp.com" >> $GITHUB_OUTPUT

      - name: Deploy preview
        run: |
          # Skapa namespace om det inte finns
          kubectl create namespace preview-${{ steps.preview.outputs.id }} --dry-run=client -o yaml | kubectl apply -f -

          # Deploy med unik subdomain
          helm upgrade --install ${{ steps.preview.outputs.id }} ./chart \
            --namespace preview-${{ steps.preview.outputs.id }} \
            --set image.tag=${{ github.sha }} \
            --set ingress.host=${{ steps.preview.outputs.id }}.preview.myapp.com

      - name: Comment PR with preview URL
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '## Preview Environment Ready!\n\nURL: ${{ steps.preview.outputs.url }}'
            })

  cleanup-preview:
    if: github.event.action == 'closed'
    runs-on: ubuntu-latest
    steps:
      - name: Delete preview environment
        run: |
          kubectl delete namespace preview-pr-${{ github.event.pull_request.number }}
```

### Exempel 2: Environment Promotion Workflow

```yaml
# .github/workflows/promote.yml
name: Promote Release

on:
  workflow_dispatch:
    inputs:
      source:
        description: 'Source environment'
        required: true
        type: choice
        options:
          - development
          - staging
      target:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      version:
        description: 'Version/tag to promote'
        required: true
        type: string

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate promotion path
        run: |
          # Förhindra direkta promotions till production från dev
          if [[ "${{ inputs.source }}" == "development" && "${{ inputs.target }}" == "production" ]]; then
            echo "ERROR: Cannot promote directly from development to production"
            echo "Please promote to staging first"
            exit 1
          fi

  promote:
    needs: validate
    runs-on: ubuntu-latest
    environment: ${{ inputs.target }}
    steps:
      - uses: actions/checkout@v4

      - name: Tag image for target environment
        run: |
          SOURCE_IMAGE="ghcr.io/${{ github.repository }}:${{ inputs.version }}"
          TARGET_IMAGE="ghcr.io/${{ github.repository }}:${{ inputs.target }}-${{ inputs.version }}"

          docker pull $SOURCE_IMAGE
          docker tag $SOURCE_IMAGE $TARGET_IMAGE
          docker push $TARGET_IMAGE

      - name: Deploy to ${{ inputs.target }}
        run: |
          kubectl --context=${{ inputs.target }} set image deployment/myapp \
            app=ghcr.io/${{ github.repository }}:${{ inputs.target }}-${{ inputs.version }}

      - name: Create release record
        run: |
          echo "{ \"version\": \"${{ inputs.version }}\", \"environment\": \"${{ inputs.target }}\", \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\", \"promoted_by\": \"${{ github.actor }}\" }" >> releases.json
```

------------------------------------------------------------

## Bästa Praxis

### Environment Isolation

```yaml
# Säkerställ isolering mellan miljöer
# 1. Separata namespaces/kluster
# 2. Separata secrets per miljö
# 3. Network policies

# k8s/base/network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
  ingress: []
  egress: []
```

### Configuration Management

```yaml
# Använd environment variables och secrets konsekvent
# GitHub Environment Variables (vars) för icke-hemlig config
# GitHub Environment Secrets för hemlig config

# I workflow:
env:
  # Från vars (synlig i logs)
  API_URL: ${{ vars.API_URL }}
  LOG_LEVEL: ${{ vars.LOG_LEVEL }}
  # Från secrets (maskerade i logs)
  API_KEY: ${{ secrets.API_KEY }}
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Delad State mellan Miljöer

```hcl
# FEL: Samma state för alla miljöer
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "myapp/terraform.tfstate"  # Samma för alla!
  }
}

# RÄTT: Separata state-filer
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "myapp/${terraform.workspace}/terraform.tfstate"
  }
}
```

### Fallgrop 2: Ingen Approval för Production

```yaml
# FEL: Automatisk deploy till production
deploy-production:
  needs: build
  runs-on: ubuntu-latest
  # Ingen environment!

# RÄTT: Kräv approval
deploy-production:
  needs: build
  runs-on: ubuntu-latest
  environment:
    name: production  # Konfigurerad med required reviewers
```

------------------------------------------------------------

## Övningar

### Övning 1: Multi-Environment Setup
<details>
<summary>Visa övning</summary>

**Mål:** Konfigurera komplett multi-environment pipeline

**Uppgifter:**
1. Skapa GitHub Environments (dev, staging, prod)
2. Konfigurera secrets per miljö
3. Implementera deploy workflow med environment promotion
4. Lägg till required reviewers för production

</details>

### Övning 2: Kustomize Overlays
<details>
<summary>Visa övning</summary>

**Mål:** Skapa Kubernetes config för tre miljöer

**Uppgifter:**
1. Skapa base configuration
2. Skapa overlays för dev, staging, prod
3. Variera replicas, resurser och config
4. Testa med `kustomize build`

</details>

### Övning 3: Preview Environments
<details>
<summary>Visa övning</summary>

**Mål:** Implementera ephemeral preview environments per PR

**Uppgifter:**
1. Skapa workflow som triggas på PR
2. Generera unik preview URL
3. Deploy till isolerat namespace
4. Implementera cleanup vid PR close

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- GitOps with ArgoCD: Multi-environment GitOps
- Secrets Management: Per-environment secrets
- Pipeline Optimization: Effektiv multi-env deploy
- Kubernetes Fundamentals: Namespace isolation

### Förkunskaper:
- CI/CD grundläggande koncept
- Kubernetes basics
- Git branching strategies

### Bygger mot:
- Blue/Green Deployments
- Canary Releases
- Feature Flags management

------------------------------------------------------------

## Sammanfattning

Multi-environment deployments är kritiska för säker leverans:

| Aspekt | Implementation |
|--------|----------------|
| **Hierarki** | Dev → Staging → Prod |
| **Config** | Kustomize/Helm overlays |
| **Secrets** | GitHub Environments |
| **Promotion** | Kontrollerad workflow |

**Kom ihåg:**
1. Separera miljöer tydligt
2. Använd environments för approvals
3. Kustomize för miljöspecifik config
4. Terraform workspaces för infra
5. Automatisera promotion workflows

------------------------------------------------------------

## Nyckelkommandon

```bash
# Kustomize
kustomize build overlays/production | kubectl apply -f -
kubectl apply -k overlays/staging

# Terraform workspaces
terraform workspace list
terraform workspace select production
terraform workspace new staging

# Kubectl context
kubectl config use-context production
kubectl --context=staging get pods

# ArgoCD environments
argocd app create myapp-prod --dest-namespace production
argocd app sync myapp-staging
```

------------------------------------------------------------

## Referenser

- GitHub Environments: https://docs.github.com/en/actions/deployment/targeting-different-environments
- Kustomize: https://kustomize.io
- Terraform Workspaces: https://developer.hashicorp.com/terraform/language/state/workspaces
- ArgoCD ApplicationSets: https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/
""",
        },
        {
            "order_index": 14,
            "title": "Monitoring CI/CD Pipelines",
            "slug": "monitoring-cicd-pipelines",
            "difficulty": "advanced",
            "content": """# Monitoring CI/CD Pipelines

------------------------------------------------------------

## Introduktion

Efter denna modul måste du kunna:
- Implementera och mäta DORA-metrics för engineering excellence
- Konfigurera real-time notifieringar till Slack, Teams och email
- Bygga dashboards med Prometheus och Grafana för pipeline-övervakning
- Sätta upp alerting med PagerDuty och OpsGenie
- Analysera trender och optimera baserat på historisk data

------------------------------------------------------------

## Introduktion

Monitoring av CI/CD-pipelines är fundamentalt för att säkerställa pålitlig mjukvaruleverans. Utan insyn i pipeline-hälsa, build-tider och failure rates är det omöjligt att förbättra. DORA-metrics (DevOps Research and Assessment) har blivit industristandard för att mäta och benchmarka engineering-team. Denna modul täcker hur du samlar in, visualiserar och agerar på pipeline-data.

------------------------------------------------------------

## Teori

### DORA Metrics Framework

```
DORA METRICS - DE FYRA NYCKELINDIKATORERNA
==========================================

+------------------------------------------------------------------+
|                    1. DEPLOYMENT FREQUENCY                        |
|------------------------------------------------------------------|
|  Hur ofta deployas kod till produktion?                          |
|                                                                   |
|  Elite:    Multiple gånger per dag                               |
|  High:     Mellan dagligen och veckovis                          |
|  Medium:   Mellan veckovis och månadsvis                         |
|  Low:      Mindre än en gång per månad                           |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    2. LEAD TIME FOR CHANGES                       |
|------------------------------------------------------------------|
|  Tid från commit till kod i produktion                           |
|                                                                   |
|  Elite:    Mindre än en timme                                    |
|  High:     Mellan en dag och en vecka                            |
|  Medium:   Mellan en vecka och en månad                          |
|  Low:      Mellan en månad och sex månader                       |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    3. CHANGE FAILURE RATE                         |
|------------------------------------------------------------------|
|  Procent av deployments som orsakar incident                     |
|                                                                   |
|  Elite:    0-15%                                                 |
|  High:     16-30%                                                |
|  Medium:   31-45%                                                |
|  Low:      > 45%                                                 |
+------------------------------------------------------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    4. MEAN TIME TO RECOVERY (MTTR)                |
|------------------------------------------------------------------|
|  Tid att återställa tjänsten vid incident                        |
|                                                                   |
|  Elite:    Mindre än en timme                                    |
|  High:     Mindre än en dag                                      |
|  Medium:   Mindre än en vecka                                    |
|  Low:      Mer än en vecka                                       |
+------------------------------------------------------------------+
```

### Pipeline Metrics Architecture

```
MONITORING ARKITEKTUR
=====================

+-------------------+     +-------------------+     +-------------------+
| GitHub Actions    |     | GitLab CI         |     | Jenkins           |
| Workflow Events   |     | Pipeline Events   |     | Build Events      |
+-------------------+     +-------------------+     +-------------------+
         |                        |                        |
         v                        v                        v
+------------------------------------------------------------------+
|                    METRICS COLLECTOR                              |
|------------------------------------------------------------------|
|  - Webhook receiver                                               |
|  - Event parser                                                   |
|  - Metric calculation                                             |
|  - Data enrichment                                                |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|                    TIME-SERIES DATABASE                           |
|------------------------------------------------------------------|
|  Prometheus / InfluxDB / TimescaleDB                             |
|  - Build duration                                                 |
|  - Success/failure counts                                         |
|  - Lead time measurements                                         |
+------------------------------------------------------------------+
         |
         +-----------------+-----------------+
         |                 |                 |
         v                 v                 v
+---------------+  +---------------+  +---------------+
| DASHBOARDS    |  | ALERTS        |  | REPORTS       |
|---------------|  |---------------|  |---------------|
| Grafana       |  | PagerDuty     |  | Weekly email  |
| Datadog       |  | OpsGenie      |  | DORA report   |
|               |  | Slack         |  | Trends        |
+---------------+  +---------------+  +---------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Samla DORA Metrics

```yaml
# .github/workflows/dora-metrics.yml
name: DORA Metrics Collection

on:
  workflow_run:
    workflows: ["CI/CD Pipeline", "Deploy"]
    types: [completed]

jobs:
  collect-metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Calculate Lead Time
        id: lead-time
        run: |
          # Hämta commit timestamp (Unix epoch)
          COMMIT_SHA="${{ github.event.workflow_run.head_sha }}"
          COMMIT_TIME=$(git log -1 --format=%ct $COMMIT_SHA)

          # Deploy-tidpunkt
          DEPLOY_TIME=$(date +%s)

          # Lead time i sekunder
          LEAD_TIME=$((DEPLOY_TIME - COMMIT_TIME))
          LEAD_TIME_HOURS=$(echo "scale=2; $LEAD_TIME / 3600" | bc)

          echo "lead_time_seconds=$LEAD_TIME" >> $GITHUB_OUTPUT
          echo "lead_time_hours=$LEAD_TIME_HOURS" >> $GITHUB_OUTPUT

      - name: Calculate Deployment Frequency
        id: deploy-freq
        uses: actions/github-script@v7
        with:
          script: |
            const { data: runs } = await github.rest.actions.listWorkflowRuns({
              owner: context.repo.owner,
              repo: context.repo.repo,
              workflow_id: 'deploy.yml',
              status: 'success',
              per_page: 100
            });

            // Räkna deployments senaste 24h
            const oneDayAgo = Date.now() - (24 * 60 * 60 * 1000);
            const recentDeploys = runs.workflow_runs.filter(
              run => new Date(run.created_at).getTime() > oneDayAgo
            ).length;

            // Räkna deployments senaste 7 dagar
            const oneWeekAgo = Date.now() - (7 * 24 * 60 * 60 * 1000);
            const weeklyDeploys = runs.workflow_runs.filter(
              run => new Date(run.created_at).getTime() > oneWeekAgo
            ).length;

            core.setOutput('daily_deploys', recentDeploys);
            core.setOutput('weekly_deploys', weeklyDeploys);
            core.setOutput('avg_daily', (weeklyDeploys / 7).toFixed(2));

      - name: Calculate Change Failure Rate
        id: failure-rate
        uses: actions/github-script@v7
        with:
          script: |
            const { data: runs } = await github.rest.actions.listWorkflowRuns({
              owner: context.repo.owner,
              repo: context.repo.repo,
              workflow_id: 'deploy.yml',
              per_page: 100
            });

            const thirtyDaysAgo = Date.now() - (30 * 24 * 60 * 60 * 1000);
            const recentRuns = runs.workflow_runs.filter(
              run => new Date(run.created_at).getTime() > thirtyDaysAgo
            );

            const total = recentRuns.length;
            const failures = recentRuns.filter(r => r.conclusion === 'failure').length;
            const failureRate = total > 0 ? ((failures / total) * 100).toFixed(2) : 0;

            core.setOutput('total_deploys', total);
            core.setOutput('failed_deploys', failures);
            core.setOutput('failure_rate', failureRate);

      - name: Send to Prometheus Pushgateway
        run: |
          cat << EOF | curl --data-binary @- http://pushgateway.monitoring:9091/metrics/job/cicd/repo/${{ github.repository }}
          # HELP cicd_lead_time_seconds Time from commit to production deployment
          # TYPE cicd_lead_time_seconds gauge
          cicd_lead_time_seconds{repo="${{ github.repository }}"} ${{ steps.lead-time.outputs.lead_time_seconds }}

          # HELP cicd_deployment_frequency Daily deployment count
          # TYPE cicd_deployment_frequency gauge
          cicd_deployment_frequency{repo="${{ github.repository }}"} ${{ steps.deploy-freq.outputs.daily_deploys }}

          # HELP cicd_change_failure_rate Percentage of failed deployments
          # TYPE cicd_change_failure_rate gauge
          cicd_change_failure_rate{repo="${{ github.repository }}"} ${{ steps.failure-rate.outputs.failure_rate }}

          # HELP cicd_deployment_success Success status of latest deployment
          # TYPE cicd_deployment_success gauge
          cicd_deployment_success{repo="${{ github.repository }}"} ${{ github.event.workflow_run.conclusion == 'success' && '1' || '0' }}
          EOF

      - name: Send to Datadog
        if: vars.DATADOG_ENABLED == 'true'
        run: |
          curl -X POST "https://api.datadoghq.eu/api/v1/series" \
            -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "series": [
                {
                  "metric": "cicd.dora.lead_time",
                  "type": "gauge",
                  "points": [['"$(date +%s)"', '"${{ steps.lead-time.outputs.lead_time_seconds }}"']],
                  "tags": ["repo:${{ github.repository }}", "env:production"]
                },
                {
                  "metric": "cicd.dora.deployment_frequency",
                  "type": "gauge",
                  "points": [['"$(date +%s)"', '"${{ steps.deploy-freq.outputs.daily_deploys }}"']],
                  "tags": ["repo:${{ github.repository }}"]
                },
                {
                  "metric": "cicd.dora.change_failure_rate",
                  "type": "gauge",
                  "points": [['"$(date +%s)"', '"${{ steps.failure-rate.outputs.failure_rate }}"']],
                  "tags": ["repo:${{ github.repository }}"]
                }
              ]
            }'
```

### Steg 2: Konfigurera Notifieringar

```yaml
# Slack notifications med rich formatting
name: Pipeline Notifications

on:
  workflow_run:
    workflows: ["CI/CD Pipeline"]
    types: [completed]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Slack Success Notification
        if: github.event.workflow_run.conclusion == 'success'
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "✅ Pipeline Successful"
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {
                      "type": "mrkdwn",
                      "text": "*Repository:*\n${{ github.repository }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Branch:*\n${{ github.event.workflow_run.head_branch }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Author:*\n${{ github.event.workflow_run.actor.login }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Duration:*\n${{ github.event.workflow_run.run_duration }}s"
                    }
                  ]
                },
                {
                  "type": "actions",
                  "elements": [
                    {
                      "type": "button",
                      "text": {"type": "plain_text", "text": "View Run"},
                      "url": "${{ github.event.workflow_run.html_url }}"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK

      - name: Slack Failure Notification
        if: github.event.workflow_run.conclusion == 'failure'
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
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
                  "text": {
                    "type": "mrkdwn",
                    "text": "Pipeline for *${{ github.repository }}* has failed on branch `${{ github.event.workflow_run.head_branch }}`"
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {
                      "type": "mrkdwn",
                      "text": "*Commit:*\n`${{ github.event.workflow_run.head_sha }}`"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Author:*\n${{ github.event.workflow_run.actor.login }}"
                    }
                  ]
                },
                {
                  "type": "actions",
                  "elements": [
                    {
                      "type": "button",
                      "text": {"type": "plain_text", "text": "🔍 Investigate"},
                      "style": "danger",
                      "url": "${{ github.event.workflow_run.html_url }}"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
```

### Steg 3: PagerDuty Integration

```yaml
# Alerting för kritiska pipeline-fel
- name: Trigger PagerDuty Alert
  if: |
    github.event.workflow_run.conclusion == 'failure' &&
    github.event.workflow_run.head_branch == 'main'
  run: |
    curl -X POST https://events.pagerduty.com/v2/enqueue \
      -H 'Content-Type: application/json' \
      -d '{
        "routing_key": "${{ secrets.PAGERDUTY_ROUTING_KEY }}",
        "event_action": "trigger",
        "dedup_key": "cicd-${{ github.repository }}-${{ github.event.workflow_run.id }}",
        "payload": {
          "summary": "Production deploy failed for ${{ github.repository }}",
          "source": "github-actions",
          "severity": "error",
          "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
          "custom_details": {
            "repository": "${{ github.repository }}",
            "branch": "${{ github.event.workflow_run.head_branch }}",
            "commit": "${{ github.event.workflow_run.head_sha }}",
            "author": "${{ github.event.workflow_run.actor.login }}",
            "run_url": "${{ github.event.workflow_run.html_url }}"
          }
        },
        "links": [
          {
            "href": "${{ github.event.workflow_run.html_url }}",
            "text": "View failed workflow run"
          }
        ]
      }'

- name: Auto-resolve on success
  if: github.event.workflow_run.conclusion == 'success'
  run: |
    curl -X POST https://events.pagerduty.com/v2/enqueue \
      -H 'Content-Type: application/json' \
      -d '{
        "routing_key": "${{ secrets.PAGERDUTY_ROUTING_KEY }}",
        "event_action": "resolve",
        "dedup_key": "cicd-${{ github.repository }}-${{ github.event.workflow_run.id }}"
      }'
```

### Steg 4: Grafana Dashboard

```yaml
# Grafana dashboard JSON (sparas som ConfigMap)
apiVersion: v1
kind: ConfigMap
metadata:
  name: cicd-dashboard
  labels:
    grafana_dashboard: "1"
data:
  cicd-dashboard.json: |
    {
      "dashboard": {
        "title": "CI/CD Pipeline Metrics",
        "panels": [
          {
            "title": "Deployment Frequency",
            "type": "stat",
            "targets": [
              {
                "expr": "sum(increase(cicd_deployment_success{repo=\"myorg/myapp\"}[24h]))",
                "legendFormat": "Daily Deploys"
              }
            ]
          },
          {
            "title": "Lead Time (hours)",
            "type": "gauge",
            "targets": [
              {
                "expr": "avg(cicd_lead_time_seconds{repo=\"myorg/myapp\"}) / 3600"
              }
            ],
            "fieldConfig": {
              "defaults": {
                "thresholds": {
                  "steps": [
                    {"value": 0, "color": "green"},
                    {"value": 24, "color": "yellow"},
                    {"value": 168, "color": "red"}
                  ]
                }
              }
            }
          },
          {
            "title": "Change Failure Rate",
            "type": "gauge",
            "targets": [
              {
                "expr": "cicd_change_failure_rate{repo=\"myorg/myapp\"}"
              }
            ],
            "fieldConfig": {
              "defaults": {
                "unit": "percent",
                "thresholds": {
                  "steps": [
                    {"value": 0, "color": "green"},
                    {"value": 15, "color": "yellow"},
                    {"value": 30, "color": "red"}
                  ]
                }
              }
            }
          },
          {
            "title": "Pipeline Duration Trend",
            "type": "timeseries",
            "targets": [
              {
                "expr": "avg_over_time(cicd_pipeline_duration_seconds[1h])",
                "legendFormat": "Avg Duration"
              }
            ]
          }
        ]
      }
    }
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Weekly DORA Report

```yaml
# Automatisk veckorapport
name: Weekly DORA Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Måndag 09:00

jobs:
  generate-report:
    runs-on: ubuntu-latest
    steps:
      - name: Generate DORA Report
        id: report
        uses: actions/github-script@v7
        with:
          script: |
            // Hämta data för senaste veckan
            const oneWeekAgo = new Date();
            oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);

            const { data: runs } = await github.rest.actions.listWorkflowRuns({
              owner: context.repo.owner,
              repo: context.repo.repo,
              workflow_id: 'deploy.yml',
              created: `>=${oneWeekAgo.toISOString()}`
            });

            const total = runs.workflow_runs.length;
            const successful = runs.workflow_runs.filter(r => r.conclusion === 'success').length;
            const failed = runs.workflow_runs.filter(r => r.conclusion === 'failure').length;

            const report = {
              period: `${oneWeekAgo.toDateString()} - ${new Date().toDateString()}`,
              deploymentFrequency: total,
              avgDailyDeploys: (total / 7).toFixed(2),
              successRate: ((successful / total) * 100).toFixed(1),
              failureRate: ((failed / total) * 100).toFixed(1)
            };

            return report;

      - name: Send Report to Slack
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H 'Content-Type: application/json' \
            -d '{
              "blocks": [
                {
                  "type": "header",
                  "text": {"type": "plain_text", "text": "📊 Weekly DORA Report"}
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*${{ fromJson(steps.report.outputs.result).period }}*"
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {"type": "mrkdwn", "text": "*Deployment Frequency:*\n${{ fromJson(steps.report.outputs.result).deploymentFrequency }} deploys"},
                    {"type": "mrkdwn", "text": "*Daily Average:*\n${{ fromJson(steps.report.outputs.result).avgDailyDeploys }} deploys/day"},
                    {"type": "mrkdwn", "text": "*Success Rate:*\n${{ fromJson(steps.report.outputs.result).successRate }}%"},
                    {"type": "mrkdwn", "text": "*Failure Rate:*\n${{ fromJson(steps.report.outputs.result).failureRate }}%"}
                  ]
                }
              ]
            }'
```

------------------------------------------------------------

## Bästa Praxis

```yaml
# 1. Strukturerade logs för enkel analys
- name: Structured logging
  run: |
    echo '{"event":"deploy_start","timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"${{ github.repository }}","sha":"${{ github.sha }}"}'

# 2. Konsekvent tagging för filtrering
# Använd alltid samma tags:
# - repo: repository name
# - env: environment (dev/staging/prod)
# - team: team ownership
# - service: service name

# 3. Separata channels för olika severity
# #cicd-alerts - Endast kritiska fel
# #cicd-deploys - Alla deploys
# #cicd-metrics - Dagliga/veckovisa rapporter
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Alert Fatigue

```yaml
# FEL: Notifiera på ALLT
on:
  workflow_run:
    types: [completed]

# RÄTT: Filtrera viktigt
on:
  workflow_run:
    workflows: ["Production Deploy"]  # Endast prod
    types: [completed]
    branches: [main]  # Endast main
```

### Fallgrop 2: Saknad Kontext

```yaml
# FEL: Minimal information
- name: Notify
  run: echo "Build failed"

# RÄTT: Rich context
- name: Notify with context
  run: |
    curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
      -d '{
        "text": "Build failed",
        "attachments": [{
          "fields": [
            {"title": "Repo", "value": "${{ github.repository }}"},
            {"title": "Commit", "value": "${{ github.sha }}"},
            {"title": "Author", "value": "${{ github.actor }}"},
            {"title": "Link", "value": "${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"}
          ]
        }]
      }'
```

------------------------------------------------------------

## Övningar

### Övning 1: DORA Metrics Dashboard
<details>
<summary>Visa övning</summary>

**Mål:** Skapa komplett DORA metrics collection och visualization

**Uppgifter:**
1. Implementera metrics collection workflow
2. Skicka data till Prometheus/Datadog
3. Skapa Grafana dashboard med alla 4 DORA metrics
4. Lägg till trender över tid

</details>

### Övning 2: Smart Alerting
<details>
<summary>Visa övning</summary>

**Mål:** Implementera intelligent alerting utan noise

**Uppgifter:**
1. Konfigurera Slack för success/failure
2. PagerDuty endast för production failures
3. Implementera deduplication
4. Auto-resolve vid recovery

</details>

### Övning 3: Weekly Report Automation
<details>
<summary>Visa övning</summary>

**Mål:** Automatisera veckovis DORA-rapport

**Uppgifter:**
1. Samla metrics från senaste veckan
2. Beräkna alla 4 DORA metrics
3. Jämför med föregående vecka
4. Skicka rapport till Slack/email

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade moduler:
- Pipeline Optimization: Mät förbättringar
- Multi-Environment: Environment-specifika metrics
- Enterprise CI/CD: Skalbar monitoring
- Compliance: Audit logging

### Förkunskaper:
- CI/CD grundläggande koncept
- Prometheus/Grafana basics
- Webhook integrations

### Bygger mot:
- SRE practices
- Platform Engineering
- DevOps maturity assessment

------------------------------------------------------------

## Sammanfattning

CI/CD Monitoring möjliggör kontinuerlig förbättring:

| Metric | Vad det mäter | Elite-nivå |
|--------|---------------|------------|
| **Deployment Frequency** | Leveranshastighet | Multiple/dag |
| **Lead Time** | Feedback loop | < 1 timme |
| **Change Failure Rate** | Kvalitet | < 15% |
| **MTTR** | Resiliens | < 1 timme |

**Kom ihåg:**
1. Mät kontinuerligt, inte manuellt
2. Visualisera trender, inte bara punktdata
3. Notifiera intelligent, undvik noise
4. Agera på insikter, inte bara samla data
5. Benchmarka mot DORA standards

------------------------------------------------------------

## Nyckelkommandon

```bash
# GitHub CLI för workflow stats
gh run list --workflow=deploy.yml --limit=100 --json conclusion,createdAt

# Prometheus queries
# Deployment frequency
sum(increase(cicd_deployment_success[24h]))

# Change failure rate
sum(cicd_deployment_success == 0) / sum(cicd_deployment_success)

# Lead time trend
avg_over_time(cicd_lead_time_seconds[7d])
```

------------------------------------------------------------

## Referenser

- DORA Metrics: https://dora.dev
- Four Keys Project: https://github.com/dora-team/fourkeys
- Prometheus: https://prometheus.io/docs
- Grafana: https://grafana.com/docs
- PagerDuty Events API: https://developer.pagerduty.com/docs/events-api-v2/overview/
""",
        },
        {
            "order_index": 15,
            "title": "Compliance and Audit",
            "slug": "compliance-audit",
            "difficulty": "hard",
            "estimated_minutes": 60,
            "xp_reward": 75,
            "content": """# Compliance and Audit

------------------------------------------------------------

## Introduktion

Föreställ dig att du arbetar på ett fintech-bolag som hanterar betalningar. En dag ringer revisorn och vill veta exakt vem som deployade vad till produktion de senaste sex månaderna, vilka säkerhetstester som kördes, och vilka godkännanden som fanns för varje release. Utan ordentlig compliance och audit trail står du där med tomma händer - och potentiellt utan PCI DSS-certifiering.

Compliance i CI/CD handlar inte bara om att följa regler för regelns skull. Det handlar om att bygga förtroende - förtroende från kunder som litar på att deras data är säker, förtroende från regulatorer som kräver spårbarhet, och förtroende inom organisationen att förändringar är kontrollerade och godkända. I en värld där en enda säkerhetsincident kan kosta miljoner och förstöra rykte är compliance en konkurrensfördel.

Som DevOps-ingenjör kommer du möta krav från SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR och branschspecifika regelverk. Denna nod ger dig verktygen att bygga pipelines som inte bara levererar kod snabbt utan också genererar den dokumentation och spårbarhet som krävs för att klara vilken revision som helst.

------------------------------------------------------------

## Teori

### Compliance-ramverk och deras CI/CD-krav

Olika regelverk ställer olika krav på mjukvaruleverans. Att förstå dessa krav är grunden för att bygga compliant pipelines.

```
+---------------------------------------------------------------+
|              COMPLIANCE-RAMVERK ÖVERSIKT                      |
+---------------------------------------------------------------+
|                                                               |
|   SOC 2 Type II                                               |
|   +----------------------------------------------------------+|
|   | - Change management procedures                           ||
|   | - Access controls och separation of duties               ||
|   | - Logging och monitoring av alla ändringar               ||
|   | - Incident response procedures                           ||
|   +----------------------------------------------------------+|
|                                                               |
|   PCI DSS (Payment Card Industry)                             |
|   +----------------------------------------------------------+|
|   | - Quarterly vulnerability scans                          ||
|   | - Code review för alla ändringar                         ||
|   | - Separation mellan dev och prod miljöer                 ||
|   | - Kryptering av känslig data                             ||
|   +----------------------------------------------------------+|
|                                                               |
|   HIPAA (Healthcare)                                          |
|   +----------------------------------------------------------+|
|   | - Audit trails för all PHI-åtkomst                       ||
|   | - Access controls baserat på role                        ||
|   | - Encryption at rest och in transit                      ||
|   | - Business Associate Agreements                          ||
|   +----------------------------------------------------------+|
|                                                               |
|   GDPR (EU Data Protection)                                   |
|   +----------------------------------------------------------+|
|   | - Data minimization                                      ||
|   | - Right to erasure (rätt att bli glömd)                  ||
|   | - Privacy by design                                      ||
|   | - 72-timmars breach notification                         ||
|   +----------------------------------------------------------+|
|                                                               |
+---------------------------------------------------------------+
```

| Ramverk | Fokusområde | CI/CD-implikation |
|---------|-------------|-------------------|
| **SOC 2** | Säkerhet, tillgänglighet, konfidentialitet | Change management, access control, logging |
| **ISO 27001** | Informationssäkerhet | Riskhantering, dokumentation, kontinuerlig förbättring |
| **PCI DSS** | Betalkortsdata | Vulnerability scanning, code review, miljöseparation |
| **HIPAA** | Hälsodata (USA) | Audit trails, encryption, access controls |
| **GDPR** | Persondata (EU) | Data protection, privacy by design |

### Separation of Duties

En grundprincip i compliance är att samma person inte ska kunna både skriva kod och deploya den till produktion utan granskning. Detta förhindrar både misstag och illvilliga ändringar.

```
+---------------------------------------------------------------+
|              SEPARATION OF DUTIES                             |
+---------------------------------------------------------------+
|                                                               |
|   UTVECKLARE          REVIEWER           DEPLOYER             |
|   +----------+        +----------+       +----------+         |
|   |  Skriver |  --->  | Granskar |  ---> | Godkänner|         |
|   |   kod    |        |   PR     |       |  deploy  |         |
|   +----------+        +----------+       +----------+         |
|        |                   |                  |               |
|        v                   v                  v               |
|   Får INTE            Får INTE           Får INTE             |
|   godkänna            skriva samma       ändra kod            |
|   egen kod            kod                efter review         |
|                                                               |
+---------------------------------------------------------------+
```

### Audit Trail - Vad som måste loggas

En komplett audit trail dokumenterar hela livscykeln för en kodändring:

```
+---------------------------------------------------------------+
|              AUDIT TRAIL KOMPONENTER                          |
+---------------------------------------------------------------+
|                                                               |
|   1. SOURCE CONTROL                                           |
|      - Commit hash, author, timestamp                         |
|      - Branch, PR number                                      |
|      - Reviewers och approvals                                |
|                                                               |
|   2. BUILD                                                    |
|      - Build ID, trigger                                      |
|      - Dependencies och versioner                             |
|      - Build artifacts och checksums                          |
|                                                               |
|   3. TEST                                                     |
|      - Test results, coverage                                 |
|      - Security scan results                                  |
|      - Compliance check results                               |
|                                                               |
|   4. DEPLOYMENT                                               |
|      - Deployment timestamp                                   |
|      - Target environment                                     |
|      - Approver(s)                                            |
|      - Rollback information                                   |
|                                                               |
|   5. RUNTIME                                                  |
|      - Application logs                                       |
|      - Access logs                                            |
|      - Error tracking                                         |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera Branch Protection

Branch protection är första försvarslinjen för att säkerställa att kod granskas innan den når main.

```bash
# Konfigurera via GitHub CLI
gh api repos/{owner}/{repo}/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["build","test","security-scan"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2,"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
  --field restrictions=null \
  --field allow_force_pushes=false \
  --field allow_deletions=false
```

```hcl
# Terraform för reproducerbar setup
# terraform/github-branch-protection.tf

resource "github_branch_protection" "main" {
  repository_id = github_repository.app.node_id
  pattern       = "main"

  # Kräv PR reviews
  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 2
    require_last_push_approval      = true

    # Specifika teams som måste godkänna
    pull_request_bypassers = [
      data.github_team.platform.node_id
    ]
  }

  # Kräv att alla status checks passerar
  required_status_checks {
    strict = true  # Branch måste vara uppdaterad med main
    contexts = [
      "build",
      "test",
      "security-scan",
      "license-check",
      "compliance-gate"
    ]
  }

  # Kräv signerade commits för extra säkerhet
  require_signed_commits = true

  # Admins måste också följa reglerna
  enforce_admins = true

  # Förhindra destruktiva operationer
  allows_force_pushes = false
  allows_deletions    = false

  # Lås branch för direkta pushes
  lock_branch = false

  # Kräv conversation resolution
  require_conversation_resolution = true
}

# CODEOWNERS för automatisk reviewer-tilldelning
resource "github_repository_file" "codeowners" {
  repository          = github_repository.app.name
  branch              = "main"
  file                = ".github/CODEOWNERS"
  content             = <<-EOT
    # Default owners
    *                   @myorg/platform-team

    # Security-sensitive files
    /terraform/         @myorg/security-team @myorg/platform-team
    /.github/workflows/ @myorg/platform-team
    /src/auth/          @myorg/security-team

    # Compliance-critical
    /src/payments/      @myorg/compliance-team @myorg/security-team
  EOT
  commit_message      = "Add CODEOWNERS for compliance"
  overwrite_on_create = true
}
```

### Steg 2: Implementera Multi-Level Approvals

```yaml
# .github/workflows/production-deploy.yml
name: Production Deployment with Approvals

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      skip_staging:
        description: 'Skip staging deployment'
        required: false
        type: boolean
        default: false

jobs:
  # Steg 1: Build och test
  build-and-test:
    runs-on: ubuntu-latest
    outputs:
      artifact_version: ${{ steps.version.outputs.version }}
    steps:
      - uses: actions/checkout@v4

      - name: Generate version
        id: version
        run: |
          VERSION="${{ github.sha }}-$(date +%Y%m%d%H%M%S)"
          echo "version=${VERSION}" >> $GITHUB_OUTPUT

      - name: Build
        run: npm ci && npm run build

      - name: Run tests
        run: npm test -- --coverage --ci

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ steps.version.outputs.version }}
          path: dist/
          retention-days: 90

  # Steg 2: Security scanning
  security-scan:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: SAST Scan
        uses: github/codeql-action/analyze@v3

      - name: Dependency Scan
        run: npm audit --audit-level=high

      - name: Container Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'

  # Steg 3: Security Team Approval
  security-approval:
    needs: security-scan
    runs-on: ubuntu-latest
    environment:
      name: security-review
      url: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
    steps:
      - name: Security team has approved
        run: |
          echo "Security review completed by: ${{ github.actor }}"
          echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

  # Steg 4: Deploy to Staging
  deploy-staging:
    needs: security-approval
    if: ${{ !inputs.skip_staging }}
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: build-${{ needs.build-and-test.outputs.artifact_version }}
          path: dist/

      - name: Deploy to staging
        run: ./scripts/deploy.sh staging

  # Steg 5: QA Verification
  qa-verification:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: qa-verification
    steps:
      - name: Run smoke tests
        run: |
          curl -f https://staging.myapp.com/health || exit 1

      - name: QA team verification complete
        run: echo "QA verified staging deployment"

  # Steg 6: Final Production Approval
  production-approval:
    needs: [security-approval, qa-verification]
    runs-on: ubuntu-latest
    environment:
      name: production-approval
    steps:
      - name: Production deployment approved
        run: |
          echo "Production approved by: ${{ github.actor }}"
          echo "This approval is logged for audit purposes"

  # Steg 7: Production Deployment
  deploy-production:
    needs: production-approval
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: build-${{ needs.build-and-test.outputs.artifact_version }}
          path: dist/

      - name: Create audit record
        run: |
          cat <<EOF > audit-record.json
          {
            "event": "production_deployment",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "version": "${{ needs.build-and-test.outputs.artifact_version }}",
            "commit": "${{ github.sha }}",
            "actor": "${{ github.actor }}",
            "workflow_run": "${{ github.run_id }}",
            "approvals": {
              "security": "security-review environment",
              "qa": "qa-verification environment",
              "production": "production-approval environment"
            }
          }
          EOF
          cat audit-record.json

      - name: Deploy to production
        run: ./scripts/deploy.sh production

      - name: Upload audit record
        uses: actions/upload-artifact@v4
        with:
          name: audit-${{ github.run_id }}
          path: audit-record.json
          retention-days: 2555  # 7 år
```

### Steg 3: Konfigurera Audit Logging

```yaml
# .github/workflows/audit-logger.yml
name: Centralized Audit Logger

on:
  workflow_run:
    workflows: ["*"]
    types: [completed]
  deployment:
  deployment_status:

jobs:
  log-event:
    runs-on: ubuntu-latest
    steps:
      - name: Construct audit event
        id: audit
        uses: actions/github-script@v7
        with:
          script: |
            const event = {
              timestamp: new Date().toISOString(),
              event_type: context.eventName,
              repository: context.repo.repo,
              organization: context.repo.owner,
              actor: context.actor,
              workflow: context.workflow,
              run_id: context.runId,
              run_number: context.runNumber,
              sha: context.sha,
              ref: context.ref,
              payload: context.payload
            };

            // Lägg till workflow-specifik info
            if (context.eventName === 'workflow_run') {
              event.workflow_run = {
                name: context.payload.workflow_run.name,
                conclusion: context.payload.workflow_run.conclusion,
                head_branch: context.payload.workflow_run.head_branch,
                head_sha: context.payload.workflow_run.head_sha
              };
            }

            core.setOutput('event', JSON.stringify(event));
            return event;

      - name: Send to audit system
        run: |
          curl -X POST "${{ secrets.AUDIT_API_URL }}/events" \
            -H "Authorization: Bearer ${{ secrets.AUDIT_API_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '${{ steps.audit.outputs.event }}'

      - name: Send to SIEM
        if: always()
        run: |
          # Skicka till Splunk/ELK/etc för långtidslagring
          curl -X POST "${{ secrets.SIEM_URL }}/services/collector/event" \
            -H "Authorization: Splunk ${{ secrets.SPLUNK_TOKEN }}" \
            -d '{
              "event": ${{ steps.audit.outputs.event }},
              "sourcetype": "github:audit",
              "index": "cicd_audit"
            }'
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: SOC 2 Compliant Pipeline

```yaml
# .github/workflows/soc2-compliant.yml
name: SOC 2 Compliant Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AUDIT_ENABLED: true

jobs:
  # Mandatory: Code review verification
  verify-review:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Verify PR was approved
        uses: actions/github-script@v7
        with:
          script: |
            // Hitta PR för denna commit
            const { data: prs } = await github.rest.repos.listPullRequestsAssociatedWithCommit({
              owner: context.repo.owner,
              repo: context.repo.repo,
              commit_sha: context.sha
            });

            if (prs.length === 0) {
              core.setFailed('No PR found for this commit. Direct pushes are not allowed.');
              return;
            }

            const pr = prs[0];

            // Verifiera reviews
            const { data: reviews } = await github.rest.pulls.listReviews({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: pr.number
            });

            const approvals = reviews.filter(r => r.state === 'APPROVED');

            if (approvals.length < 2) {
              core.setFailed(`PR #${pr.number} requires at least 2 approvals. Found: ${approvals.length}`);
              return;
            }

            // Verifiera att author inte godkände sin egen PR
            const authorApproval = approvals.find(a => a.user.login === pr.user.login);
            if (authorApproval) {
              core.setFailed('Self-approval is not allowed');
              return;
            }

            console.log(`PR #${pr.number} verified with ${approvals.length} approvals`);

  # Mandatory: Security scanning
  security-controls:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: SAST - Static Analysis
        uses: github/codeql-action/analyze@v3

      - name: SCA - Dependency Check
        run: |
          npm audit --json > npm-audit.json || true

          # Fail på kritiska sårbarheter
          CRITICAL=$(jq '.metadata.vulnerabilities.critical' npm-audit.json)
          if [ "$CRITICAL" -gt 0 ]; then
            echo "Critical vulnerabilities found: $CRITICAL"
            exit 1
          fi

      - name: Secrets Detection
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          extra_args: --only-verified

      - name: Upload security artifacts
        uses: actions/upload-artifact@v4
        with:
          name: security-scan-results
          path: |
            npm-audit.json
            codeql-results/
          retention-days: 2555

  # Mandatory: Change documentation
  document-change:
    runs-on: ubuntu-latest
    needs: [verify-review, security-controls]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate change documentation
        run: |
          mkdir -p compliance-docs

          # Git log för ändringar
          git log --oneline -20 > compliance-docs/recent_changes.txt

          # Commit detaljer
          git show --stat > compliance-docs/commit_details.txt

          # Generate SBOM
          npm sbom --sbom-format cyclonedx > compliance-docs/sbom.json

          # Timestamp och metadata
          cat <<EOF > compliance-docs/change_record.json
          {
            "change_id": "${{ github.run_id }}",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "commit_sha": "${{ github.sha }}",
            "author": "${{ github.actor }}",
            "change_type": "${{ github.event_name }}",
            "branch": "${{ github.ref_name }}",
            "repository": "${{ github.repository }}"
          }
          EOF

      - name: Upload compliance documentation
        uses: actions/upload-artifact@v4
        with:
          name: compliance-docs-${{ github.sha }}
          path: compliance-docs/
          retention-days: 2555  # 7 år retention
```

### Exempel 2: PCI DSS Deployment Pipeline

```yaml
# .github/workflows/pci-dss-deploy.yml
name: PCI DSS Compliant Deployment

on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      change_ticket:
        description: 'Change management ticket ID'
        required: true
        type: string

jobs:
  pre-deployment-checks:
    runs-on: ubuntu-latest
    steps:
      - name: Validate change ticket
        run: |
          # Verifiera att change ticket existerar och är godkänd
          TICKET_STATUS=$(curl -s "https://servicenow.mycompany.com/api/now/table/change_request/${{ inputs.change_ticket }}" \
            -H "Authorization: Bearer ${{ secrets.SNOW_TOKEN }}" | jq -r '.result.state')

          if [ "$TICKET_STATUS" != "approved" ]; then
            echo "Change ticket ${{ inputs.change_ticket }} is not approved. Status: $TICKET_STATUS"
            exit 1
          fi

          echo "Change ticket validated: ${{ inputs.change_ticket }}"

      - name: Verify deployment window
        run: |
          # PCI DSS kräver ofta change windows
          HOUR=$(date +%H)
          DAY=$(date +%u)

          # Exempel: Endast deploy 06-18 på vardagar
          if [ "${{ inputs.environment }}" == "production" ]; then
            if [ $DAY -gt 5 ] || [ $HOUR -lt 6 ] || [ $HOUR -gt 18 ]; then
              echo "Production deployments only allowed Mon-Fri 06:00-18:00"
              exit 1
            fi
          fi

      - uses: actions/checkout@v4

      - name: Quarterly vulnerability scan check
        run: |
          # Verifiera att quarterly scan är utförd (PCI DSS Requirement 11.2)
          LAST_SCAN=$(curl -s "https://security.mycompany.com/api/scans/latest" \
            -H "Authorization: Bearer ${{ secrets.SECURITY_TOKEN }}" | jq -r '.scan_date')

          SCAN_AGE=$(( ($(date +%s) - $(date -d "$LAST_SCAN" +%s)) / 86400 ))

          if [ $SCAN_AGE -gt 90 ]; then
            echo "Quarterly vulnerability scan is overdue. Last scan: $LAST_SCAN"
            exit 1
          fi

          echo "Quarterly scan verified. Last scan: $LAST_SCAN ($SCAN_AGE days ago)"

  cardholder-data-check:
    runs-on: ubuntu-latest
    needs: pre-deployment-checks
    steps:
      - uses: actions/checkout@v4

      - name: Scan for cardholder data patterns
        run: |
          # Sök efter potentiell PAN (Primary Account Number) data
          # Detta är en förenklad check - använd dedikerade verktyg i produktion

          PATTERNS="[0-9]{13,16}|[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}"

          if grep -rE "$PATTERNS" src/ --include="*.js" --include="*.ts" --include="*.json"; then
            echo "WARNING: Potential cardholder data patterns found in code"
            echo "Manual review required before deployment"
            exit 1
          fi

          echo "No cardholder data patterns detected"

      - name: Verify encryption configuration
        run: |
          # Verifiera att TLS är konfigurerat
          if ! grep -q "TLS_VERSION.*1.2\|1.3" config/security.yml; then
            echo "TLS 1.2 or higher must be configured"
            exit 1
          fi

          echo "Encryption configuration verified"

  deploy:
    needs: [pre-deployment-checks, cardholder-data-check]
    runs-on: ubuntu-latest
    environment:
      name: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4

      - name: Start deployment audit record
        id: audit_start
        run: |
          AUDIT_ID=$(uuidgen)
          echo "audit_id=$AUDIT_ID" >> $GITHUB_OUTPUT

          curl -X POST "https://audit.mycompany.com/pci/deployments" \
            -H "Authorization: Bearer ${{ secrets.AUDIT_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "audit_id": "'$AUDIT_ID'",
              "event": "deployment_started",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "environment": "${{ inputs.environment }}",
              "change_ticket": "${{ inputs.change_ticket }}",
              "initiated_by": "${{ github.actor }}",
              "commit_sha": "${{ github.sha }}",
              "workflow_run_id": "${{ github.run_id }}"
            }'

      - name: Deploy
        id: deploy
        run: ./scripts/deploy.sh ${{ inputs.environment }}

      - name: Complete deployment audit record
        if: always()
        run: |
          curl -X PATCH "https://audit.mycompany.com/pci/deployments/${{ steps.audit_start.outputs.audit_id }}" \
            -H "Authorization: Bearer ${{ secrets.AUDIT_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "event": "deployment_completed",
              "completed_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "status": "${{ steps.deploy.outcome }}",
              "duration_seconds": "${{ github.event.workflow_run.run_duration }}"
            }'
```

### Exempel 3: License Compliance Scanning

```yaml
# .github/workflows/license-compliance.yml
name: License Compliance Check

on:
  pull_request:
  push:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'  # Varje måndag 06:00

jobs:
  scan-licenses:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Scan NPM licenses
        run: |
          npx license-checker --production --json > licenses.json

          # Definiera godkända licenser
          ALLOWED_LICENSES="MIT|Apache-2.0|BSD-2-Clause|BSD-3-Clause|ISC|0BSD|CC0-1.0|Unlicense"

          # Hitta förbjudna licenser
          FORBIDDEN=$(jq -r '
            to_entries[] |
            select(.value.licenses | test("GPL|AGPL|LGPL|SSPL|CPAL|OSL|EUPL") ) |
            "\(.key): \(.value.licenses)"
          ' licenses.json)

          if [ -n "$FORBIDDEN" ]; then
            echo "::error::Forbidden licenses detected:"
            echo "$FORBIDDEN"
            exit 1
          fi

          echo "All licenses approved"

      - name: Generate SBOM
        run: |
          # CycloneDX SBOM
          npx @cyclonedx/cyclonedx-npm --output-file sbom-cyclonedx.json

          # SPDX SBOM
          npx spdx-sbom-generator -o sbom-spdx.json

      - name: Upload license artifacts
        uses: actions/upload-artifact@v4
        with:
          name: license-compliance-${{ github.sha }}
          path: |
            licenses.json
            sbom-cyclonedx.json
            sbom-spdx.json
          retention-days: 2555

      - name: Submit to FOSSA
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        uses: fossas/fossa-action@main
        with:
          api-key: ${{ secrets.FOSSA_API_KEY }}
```

------------------------------------------------------------

## Bästa Praxis

### 1. Implementera Immutable Audit Logs

```yaml
# Använd write-once storage för audit logs
- name: Store immutable audit log
  run: |
    # Skapa signerad audit record
    RECORD=$(cat <<EOF
    {
      "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
      "event": "deployment",
      "data": {
        "sha": "${{ github.sha }}",
        "actor": "${{ github.actor }}",
        "environment": "production"
      }
    }
    EOF
    )

    # Beräkna SHA256 hash
    HASH=$(echo "$RECORD" | sha256sum | cut -d' ' -f1)

    # Lagra i immutable storage (S3 Object Lock, Azure Immutable Blob, etc)
    aws s3 cp - "s3://audit-logs/$(date +%Y/%m/%d)/${HASH}.json" \
      --object-lock-mode COMPLIANCE \
      --object-lock-retain-until-date "$(date -d '+7 years' +%Y-%m-%dT%H:%M:%SZ)" \
      <<< "$RECORD"
```

### 2. Automatisera Compliance Reports

```yaml
# Veckovis compliance rapport
- name: Generate weekly compliance report
  run: |
    cat <<EOF > compliance-report.md
    # Weekly Compliance Report
    **Period:** $(date -d '7 days ago' +%Y-%m-%d) to $(date +%Y-%m-%d)
    **Generated:** $(date -u +%Y-%m-%dT%H:%M:%SZ)

    ## Deployment Summary
    - Total deployments: ${DEPLOY_COUNT}
    - Successful: ${SUCCESS_COUNT}
    - Failed: ${FAILED_COUNT}
    - Rollbacks: ${ROLLBACK_COUNT}

    ## Security Metrics
    - Vulnerabilities found: ${VULN_COUNT}
    - Critical/High resolved: ${RESOLVED_COUNT}
    - Average time to fix: ${AVG_FIX_TIME}

    ## Compliance Status
    - All deployments approved: ✅
    - Audit trail complete: ✅
    - Security scans passing: ✅
    EOF
```

### 3. Implementera Break-Glass Procedures

```yaml
# Emergency deployment med extra audit
- name: Emergency deployment
  if: inputs.emergency == true
  environment:
    name: emergency-production
  steps:
    - name: Log emergency deployment
      run: |
        # Extra logging för emergency deploys
        curl -X POST "https://audit.mycompany.com/emergency" \
          -d '{
            "type": "emergency_deployment",
            "justification": "${{ inputs.justification }}",
            "approved_by": "${{ github.actor }}",
            "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
          }'

        # Notifiera security team
        curl -X POST "${{ secrets.SLACK_SECURITY_WEBHOOK }}" \
          -d '{"text": "⚠️ Emergency deployment initiated by ${{ github.actor }}"}'
```

### 4. Version Control för Compliance Config

```yaml
# Alla compliance-regler i kod
# .github/compliance/rules.yml
compliance_rules:
  branch_protection:
    required_reviews: 2
    dismiss_stale_reviews: true
    require_codeowners: true

  security_scanning:
    sast: required
    dast: required_for_production
    dependency_check: required

  deployment_gates:
    staging_required: true
    security_approval: required
    change_ticket: required_for_production

  retention:
    audit_logs: 2555  # 7 years
    build_artifacts: 90
    test_results: 365
```

### 5. Continuous Compliance Monitoring

```yaml
# Daglig compliance check
name: Daily Compliance Check

on:
  schedule:
    - cron: '0 6 * * *'

jobs:
  compliance-audit:
    runs-on: ubuntu-latest
    steps:
      - name: Check branch protection
        uses: actions/github-script@v7
        with:
          script: |
            const { data: protection } = await github.rest.repos.getBranchProtection({
              owner: context.repo.owner,
              repo: context.repo.repo,
              branch: 'main'
            });

            const issues = [];

            if (!protection.required_pull_request_reviews) {
              issues.push('PR reviews not required');
            } else if (protection.required_pull_request_reviews.required_approving_review_count < 2) {
              issues.push('Less than 2 approvals required');
            }

            if (!protection.required_status_checks) {
              issues.push('Status checks not required');
            }

            if (protection.allow_force_pushes.enabled) {
              issues.push('Force pushes allowed');
            }

            if (issues.length > 0) {
              core.setFailed(`Compliance issues found:\n${issues.join('\n')}`);
            }
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Incomplete Audit Trail

```yaml
# FEL: Loggar inte misslyckade försök
- name: Deploy
  run: ./deploy.sh

# RÄTT: Logga ALLA händelser
- name: Deploy with complete audit
  id: deploy
  run: ./deploy.sh
  continue-on-error: true

- name: Log deployment result
  if: always()
  run: |
    curl -X POST "${{ secrets.AUDIT_URL }}" \
      -d '{
        "event": "deployment",
        "status": "${{ steps.deploy.outcome }}",
        "error": "${{ steps.deploy.outputs.error || 'none' }}"
      }'

- name: Fail if deployment failed
  if: steps.deploy.outcome == 'failure'
  run: exit 1
```

### Fallgrop 2: Bypass av Approval Gates

```yaml
# FEL: Admin kan bypassa
enforce_admins: false

# RÄTT: Ingen undantag
enforce_admins: true

# Om emergency bypass behövs, använd separat workflow med extra audit
```

### Fallgrop 3: Otillräcklig Retention

```yaml
# FEL: Default retention (90 dagar)
- uses: actions/upload-artifact@v4
  with:
    name: audit-log
    path: audit.json

# RÄTT: Compliance-krav retention (ofta 7 år)
- uses: actions/upload-artifact@v4
  with:
    name: audit-log
    path: audit.json
    retention-days: 2555  # 7 år

# Eller bättre: Extern långtidslagring
- name: Archive to long-term storage
  run: |
    aws s3 cp audit.json s3://compliance-archive/$(date +%Y/%m/%d)/ \
      --storage-class GLACIER_IR
```

### Fallgrop 4: Manuella Compliance Checks

```yaml
# FEL: Lita på manuell verifiering
- name: Manual security check
  run: echo "Please verify security manually"

# RÄTT: Automatisera alla kontroller
- name: Automated security gate
  run: |
    # SAST
    npm run security:sast || exit 1

    # Dependency check
    npm audit --audit-level=high || exit 1

    # License check
    npm run license:check || exit 1

    echo "All automated checks passed"
```

------------------------------------------------------------

## Övningar

### Övning 1: Implementera Basic Compliance Pipeline (25 XP)

**Mål:** Skapa en pipeline med grundläggande compliance-kontroller.

**Din uppgift:**
1. Konfigurera branch protection på main med 2 required reviews
2. Lägg till CODEOWNERS-fil
3. Implementera workflow med security scanning och audit logging
4. Verifiera att direkt push till main blockeras

<details>
<summary>Ledtråd</summary>

Börja med GitHub CLI för branch protection:
```bash
gh api repos/{owner}/{repo}/branches/main/protection --method PUT ...
```

Skapa sedan `.github/CODEOWNERS` och `workflows/compliance.yml`.

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Branch protection
gh api repos/myorg/myrepo/branches/main/protection \
  --method PUT \
  -f required_status_checks='{"strict":true,"contexts":["build","test"]}' \
  -f enforce_admins=true \
  -f required_pull_request_reviews='{"required_approving_review_count":2}' \
  -f allow_force_pushes=false

# 2. CODEOWNERS
cat > .github/CODEOWNERS << 'EOF'
* @myorg/platform-team
/src/security/ @myorg/security-team
/.github/ @myorg/platform-team
EOF

# 3. Workflow - se Praktiska Exempel 1 för komplett implementation
```

</details>

**Verifikation:** Försök pusha direkt till main - det ska blockeras.

---

### Övning 2: SOC 2 Evidence Collection (30 XP)

**Mål:** Implementera automatisk insamling av audit evidence.

**Din uppgift:**
1. Skapa workflow som genererar komplett change documentation
2. Inkludera git history, test results, security scans
3. Signera evidence med checksums
4. Lagra med 7 års retention

<details>
<summary>Ledtråd</summary>

Använd `actions/upload-artifact` med `retention-days: 2555` och generera SHA256 checksums för alla filer.

</details>

<details>
<summary>Lösning</summary>

```yaml
name: Evidence Collection

on:
  push:
    branches: [main]

jobs:
  collect-evidence:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate evidence
        run: |
          mkdir -p evidence

          # Change details
          git log --oneline -50 > evidence/git_history.txt
          git show --stat > evidence/commit_details.txt
          git diff HEAD~1 > evidence/changes.diff

          # Build info
          npm ci
          npm test -- --coverage --json > evidence/test_results.json
          npm audit --json > evidence/security_audit.json

          # Metadata
          cat <<EOF > evidence/metadata.json
          {
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "commit": "${{ github.sha }}",
            "actor": "${{ github.actor }}",
            "run_id": "${{ github.run_id }}"
          }
          EOF

          # Generate checksums
          find evidence -type f -exec sha256sum {} \; > evidence/checksums.txt

      - uses: actions/upload-artifact@v4
        with:
          name: soc2-evidence-${{ github.sha }}
          path: evidence/
          retention-days: 2555
```

</details>

---

### Övning 3: Multi-Level Approval System (35 XP)

**Mål:** Implementera production deployment med security, QA och management approvals.

**Din uppgift:**
1. Skapa tre GitHub Environments: security-review, qa-review, production
2. Konfigurera required reviewers för varje
3. Implementera deployment workflow som kräver alla tre godkännanden i sekvens
4. Lägg till audit logging för varje godkännande

<details>
<summary>Ledtråd</summary>

Använd `environment:` i jobs för att triggra approval gates. Varje environment kan ha olika required reviewers.

</details>

<details>
<summary>Lösning</summary>

```yaml
# Se Steg-för-steg Guide, Steg 2 för komplett implementation
# Nyckelkoncept:

jobs:
  security-approval:
    environment:
      name: security-review
    steps:
      - run: echo "Security approved by ${{ github.actor }}"

  qa-approval:
    needs: security-approval
    environment:
      name: qa-review
    steps:
      - run: echo "QA approved by ${{ github.actor }}"

  production-deploy:
    needs: qa-approval
    environment:
      name: production
    steps:
      - run: ./deploy.sh
```

Konfigurera environments i GitHub: Settings → Environments → Add required reviewers.

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **Secrets Management:** Säker hantering av credentials för audit systems
- **Monitoring CI/CD Pipelines:** Övervakning av compliance metrics
- **Enterprise CI/CD Patterns:** Skalbar compliance för stora organisationer
- **Disaster Recovery:** Compliance vid incident response

### Förkunskaper:
- GitHub Actions Fundamentals
- Multi-Environment Deployments
- Security scanning basics

### Bygger mot:
- SOC 2 certifiering
- PCI DSS compliance
- ISO 27001 implementation
- Enterprise security policies

------------------------------------------------------------

## Sammanfattning

- **Branch protection** är första försvarslinjen - kräv reviews, status checks och signerade commits
- **Separation of duties** förhindrar att samma person skriver och godkänner kod
- **Audit trails** måste vara kompletta och immutabla - logga ALLA händelser
- **Multi-level approvals** säkerställer att rätt personer granskar innan production
- **Evidence collection** automatiseras för att alltid ha dokumentation redo för revision
- **License compliance** scannas automatiskt för att undvika juridiska problem
- **Change management** integration kopplar deploys till godkända change tickets
- **Retention policies** måste uppfylla regulatoriska krav (ofta 7 år)
- **Continuous monitoring** upptäcker compliance-avvikelser innan de blir problem

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `gh api repos/.../protection` | Konfigurera branch protection | `gh api repos/org/repo/branches/main/protection --method PUT` |
| `npm audit` | Scanna npm dependencies | `npm audit --audit-level=high --json` |
| `npx license-checker` | Lista alla licenser | `npx license-checker --production --json` |
| `npm sbom` | Generera SBOM | `npm sbom --sbom-format cyclonedx` |
| `git log --oneline` | Commit history för audit | `git log --oneline -50 > history.txt` |
| `sha256sum` | Skapa checksums för integritet | `sha256sum file.json > checksum.txt` |

------------------------------------------------------------

## Referenser

- SOC 2 Compliance Guide: https://www.aicpa.org/soc2
- PCI DSS Requirements: https://www.pcisecuritystandards.org
- ISO 27001 Standard: https://www.iso.org/iso-27001-information-security.html
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- GitHub Branch Protection: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches
- CycloneDX SBOM: https://cyclonedx.org
- SPDX License List: https://spdx.org/licenses/
- FOSSA License Compliance: https://fossa.com
""",
        },
        {
            "order_index": 16,
            "title": "Disaster Recovery",
            "slug": "disaster-recovery",
            "difficulty": "advanced",
            "content": """# Disaster Recovery

Disaster Recovery (DR) för CI/CD är konsten att säkerställa kontinuitet i din utvecklingsprocess även när katastrofer inträffar. Detta omfattar allt från runner-failures och secrets-kompromittering till complete infrastructure outages. En väl förberedd DR-strategi är skillnaden mellan minuters nedtid och dagars kaos.

------------------------------------------------------------

## Introduktion

### Varför Disaster Recovery för CI/CD?

CI/CD-pipelines har blivit kritisk infrastruktur för moderna organisationer. När din pipeline går ner stannar all deployment, vilket kan kosta miljontals kronor per timme i förlorad produktivitet och missade releases. Disaster Recovery handlar om att minimera denna påverkan genom förberedelse, redundans och snabb återställning.

**Verkliga katastrofscenarier:**
- **GitHub outage 2023:** 4+ timmar nedtid påverkade miljontals utvecklare globalt
- **CircleCI secrets breach 2023:** Tvingade tusentals organisationer att rotera alla secrets
- **AWS us-east-1 outage 2021:** Många CI/CD-system otillgängliga i timmar
- **Docker Hub rate limiting 2020:** Bröt pipelines för otaliga projekt

### Vad du kommer lära dig

Efter denna modul kommer du kunna:
- Designa resilient CI/CD-arkitektur med redundans
- Implementera automatiska rollback-strategier
- Konfigurera multi-region deployment för hög tillgänglighet
- Skapa backup-rutiner för CI/CD-konfiguration och secrets
- Bygga incident response workflows för snabb åtgärd
- Definiera och uppnå RTO/RPO-mål för din pipeline

### Förkunskaper

- Solid förståelse för GitHub Actions eller annan CI/CD-plattform
- Erfarenhet av Kubernetes deployments
- Grundläggande förståelse för cloud infrastructure (AWS/GCP/Azure)
- Kännedom om secrets management

------------------------------------------------------------

## Teori

### RTO och RPO - Grundläggande DR-koncept

**Recovery Time Objective (RTO)** är den maximala tiden din CI/CD-pipeline får vara otillgänglig innan det orsakar oacceptabel affärspåverkan.

**Recovery Point Objective (RPO)** är den maximala mängden data/arbete du kan förlora vid en katastrof.

```
+------------------------------------------------------------------+
|                    RTO/RPO VISUALISERING                         |
+------------------------------------------------------------------+
|                                                                  |
|   Tidslinje:                                                     |
|                                                                  |
|   [Senaste backup] -------- [Katastrof] -------- [Återställd]    |
|          |                      |                     |          |
|          |<------ RPO --------->|                     |          |
|          |    (dataförlust)     |<------ RTO -------->|          |
|                                      (nedtid)                    |
|                                                                  |
+------------------------------------------------------------------+
|                                                                  |
|   Exempel RTO/RPO-mål:                                           |
|                                                                  |
|   Tier 1 (Kritisk):     RTO = 15 min,  RPO = 0 (zero data loss)  |
|   Tier 2 (Viktig):      RTO = 1 timme, RPO = 1 timme             |
|   Tier 3 (Standard):    RTO = 4 timmar, RPO = 24 timmar          |
|   Tier 4 (Låg prioritet): RTO = 24 timmar, RPO = 1 vecka         |
|                                                                  |
+------------------------------------------------------------------+
```

### DR-strategier för CI/CD

| Strategi | RTO | RPO | Kostnad | Komplexitet |
|----------|-----|-----|---------|-------------|
| **Backup & Restore** | Timmar | Timmar-dagar | Låg | Låg |
| **Pilot Light** | 10-30 min | Minuter | Medium | Medium |
| **Warm Standby** | Minuter | Sekunder | Hög | Hög |
| **Multi-Site Active** | Sekunder | Zero | Mycket hög | Mycket hög |

### Katastroftyper och Responses

```
+------------------------------------------------------------------+
|                  KATASTROFTYPER FÖR CI/CD                        |
+------------------------------------------------------------------+
|                                                                  |
|   1. INFRASTRUKTUR-FAILURE                                       |
|      - Runner-pool otillgänglig                                  |
|      - Cloud provider outage                                     |
|      - Network partition                                         |
|      Response: Failover till backup runners/region               |
|                                                                  |
|   2. SECURITY INCIDENT                                           |
|      - Secrets kompromitterade                                   |
|      - Supply chain attack                                       |
|      - Unauthorized access                                       |
|      Response: Rotation, isolation, forensics                    |
|                                                                  |
|   3. DATA CORRUPTION                                             |
|      - Korrupt artifact cache                                    |
|      - Felaktig configuration push                               |
|      - Database migration failure                                |
|      Response: Restore från backup, rollback                     |
|                                                                  |
|   4. DEPLOYMENT FAILURE                                          |
|      - Bad release till production                               |
|      - Breaking database migration                               |
|      - Infrastructure drift                                      |
|      Response: Automated rollback, canary analysis               |
|                                                                  |
+------------------------------------------------------------------+
```

### Rollback-strategier

| Strategi | Beskrivning | Hastighet | Risk |
|----------|-------------|-----------|------|
| **Kubernetes rollout undo** | Återställ till föregående ReplicaSet | Sekunder | Låg |
| **Blue/Green switch** | Byt trafik mellan environments | Sekunder | Mycket låg |
| **Canary rollback** | Stoppa gradvis utrullning | Sekunder | Låg |
| **Database restore** | Återställ databas från backup | Minuter-timmar | Medium |
| **Full infrastructure restore** | Återskapa hela stacken | Timmar | Hög |

### Multi-Region Arkitektur

```
+------------------------------------------------------------------+
|              MULTI-REGION CI/CD ARKITEKTUR                       |
+------------------------------------------------------------------+
|                                                                  |
|                      Global Load Balancer                        |
|                             |                                    |
|          +------------------+------------------+                  |
|          |                  |                  |                  |
|          v                  v                  v                  |
|   +-------------+    +-------------+    +-------------+          |
|   |  EU-WEST-1  |    |  US-EAST-1  |    | AP-SOUTH-1  |          |
|   |-------------|    |-------------|    |-------------|          |
|   | Runners: 10 |    | Runners: 15 |    | Runners: 8  |          |
|   | Cache: S3   |    | Cache: S3   |    | Cache: S3   |          |
|   | Secrets:Vault|   | Secrets:Vault|   | Secrets:Vault|         |
|   +-------------+    +-------------+    +-------------+          |
|          |                  |                  |                  |
|          +------------------+------------------+                  |
|                             |                                    |
|                    Cross-Region Replication                      |
|                                                                  |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Implementera Kubernetes Rollback

Automatisk rollback vid deployment-failure är grundläggande DR.

```yaml
# .github/workflows/deploy-with-rollback.yml
name: Deploy with Auto-Rollback

on:
  push:
    branches: [main]

env:
  DEPLOYMENT_NAME: myapp
  NAMESPACE: production
  ROLLOUT_TIMEOUT: 300s

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl
        uses: azure/k8s-set-context@v4
        with:
          kubeconfig: ${{ secrets.KUBECONFIG }}

      - name: Record pre-deployment state
        id: pre-deploy
        run: |
          # Spara nuvarande revision för potentiell rollback
          CURRENT_REVISION=$(kubectl rollout history deployment/$DEPLOYMENT_NAME \
            -n $NAMESPACE --revision=0 | tail -1 | awk '{print $1}')
          echo "revision=$CURRENT_REVISION" >> $GITHUB_OUTPUT

          # Spara nuvarande image
          CURRENT_IMAGE=$(kubectl get deployment/$DEPLOYMENT_NAME -n $NAMESPACE \
            -o jsonpath='{.spec.template.spec.containers[0].image}')
          echo "current_image=$CURRENT_IMAGE" >> $GITHUB_OUTPUT

          echo "📝 Current revision: $CURRENT_REVISION"
          echo "📝 Current image: $CURRENT_IMAGE"

      - name: Deploy new version
        id: deploy
        run: |
          echo "🚀 Deploying ${{ github.sha }}..."

          # Uppdatera image
          kubectl set image deployment/$DEPLOYMENT_NAME \
            app=myapp:${{ github.sha }} \
            -n $NAMESPACE

          # Annotera deployment
          kubectl annotate deployment/$DEPLOYMENT_NAME \
            -n $NAMESPACE \
            kubernetes.io/change-cause="Deploy ${{ github.sha }} by ${{ github.actor }}" \
            --overwrite

      - name: Wait for rollout
        id: rollout
        run: |
          echo "⏳ Waiting for rollout to complete..."

          if kubectl rollout status deployment/$DEPLOYMENT_NAME \
            -n $NAMESPACE \
            --timeout=$ROLLOUT_TIMEOUT; then
            echo "✅ Rollout completed successfully"
            echo "status=success" >> $GITHUB_OUTPUT
          else
            echo "❌ Rollout failed or timed out"
            echo "status=failure" >> $GITHUB_OUTPUT
            exit 1
          fi

      - name: Health check
        id: health
        if: steps.rollout.outputs.status == 'success'
        run: |
          echo "🏥 Running health checks..."

          # Vänta på att alla pods är ready
          kubectl wait --for=condition=ready pod \
            -l app=$DEPLOYMENT_NAME \
            -n $NAMESPACE \
            --timeout=120s

          # Kör application-level health check
          POD=$(kubectl get pod -l app=$DEPLOYMENT_NAME -n $NAMESPACE \
            -o jsonpath='{.items[0].metadata.name}')

          for i in {1..5}; do
            if kubectl exec $POD -n $NAMESPACE -- curl -sf http://localhost:8080/health; then
              echo "✅ Health check $i/5 passed"
            else
              echo "❌ Health check $i/5 failed"
              exit 1
            fi
            sleep 2
          done

          echo "status=healthy" >> $GITHUB_OUTPUT

      - name: Automatic rollback on failure
        if: failure()
        run: |
          echo "🔄 Initiating automatic rollback..."

          # Rollback till föregående version
          kubectl rollout undo deployment/$DEPLOYMENT_NAME -n $NAMESPACE

          # Vänta på rollback
          kubectl rollout status deployment/$DEPLOYMENT_NAME \
            -n $NAMESPACE \
            --timeout=$ROLLOUT_TIMEOUT

          echo "✅ Rollback completed"

          # Verifiera att vi är tillbaka på rätt version
          RESTORED_IMAGE=$(kubectl get deployment/$DEPLOYMENT_NAME -n $NAMESPACE \
            -o jsonpath='{.spec.template.spec.containers[0].image}')
          echo "📝 Restored to: $RESTORED_IMAGE"

      - name: Notify on rollback
        if: failure()
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H "Content-Type: application/json" \
            -d '{
              "blocks": [
                {
                  "type": "header",
                  "text": {"type": "plain_text", "text": "⚠️ Deployment Rolled Back"}
                },
                {
                  "type": "section",
                  "fields": [
                    {"type": "mrkdwn", "text": "*Service:*\n${{ env.DEPLOYMENT_NAME }}"},
                    {"type": "mrkdwn", "text": "*Environment:*\n${{ env.NAMESPACE }}"},
                    {"type": "mrkdwn", "text": "*Failed Commit:*\n${{ github.sha }}"},
                    {"type": "mrkdwn", "text": "*Triggered by:*\n${{ github.actor }}"}
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

### Steg 2: Blue/Green Deployment med Instant Rollback

```yaml
# .github/workflows/blue-green-deploy.yml
name: Blue/Green Deployment

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl
        uses: azure/k8s-set-context@v4
        with:
          kubeconfig: ${{ secrets.KUBECONFIG }}

      - name: Determine environments
        id: env
        run: |
          # Hitta vilken färg som är aktiv
          ACTIVE=$(kubectl get svc myapp-production -n production \
            -o jsonpath='{.spec.selector.color}' 2>/dev/null || echo "blue")

          if [ "$ACTIVE" = "blue" ]; then
            TARGET="green"
          else
            TARGET="blue"
          fi

          echo "active=$ACTIVE" >> $GITHUB_OUTPUT
          echo "target=$TARGET" >> $GITHUB_OUTPUT
          echo "📝 Active: $ACTIVE, Target: $TARGET"

      - name: Deploy to inactive environment
        run: |
          TARGET="${{ steps.env.outputs.target }}"
          echo "🚀 Deploying to $TARGET environment..."

          # Uppdatera target deployment
          kubectl set image deployment/myapp-$TARGET \
            app=myapp:${{ github.sha }} \
            -n production

          # Vänta på rollout
          kubectl rollout status deployment/myapp-$TARGET \
            -n production \
            --timeout=300s

      - name: Run smoke tests on target
        id: smoke
        run: |
          TARGET="${{ steps.env.outputs.target }}"

          # Hämta target service IP (intern service för testing)
          TARGET_URL=$(kubectl get svc myapp-$TARGET -n production \
            -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

          echo "🧪 Running smoke tests against $TARGET ($TARGET_URL)..."

          # Kör smoke tests
          for endpoint in "/health" "/api/status" "/api/ready"; do
            if curl -sf "http://$TARGET_URL:8080$endpoint" > /dev/null; then
              echo "✅ $endpoint OK"
            else
              echo "❌ $endpoint FAILED"
              exit 1
            fi
          done

          echo "status=passed" >> $GITHUB_OUTPUT

      - name: Switch traffic
        if: steps.smoke.outputs.status == 'passed'
        run: |
          TARGET="${{ steps.env.outputs.target }}"
          echo "🔀 Switching traffic to $TARGET..."

          # Atomic traffic switch
          kubectl patch svc myapp-production -n production \
            -p '{"spec":{"selector":{"color":"'$TARGET'"}}}'

          echo "✅ Traffic now routing to $TARGET"

      - name: Verify switch
        run: |
          TARGET="${{ steps.env.outputs.target }}"

          # Verifiera att trafiken går till rätt ställe
          sleep 5

          CURRENT=$(kubectl get svc myapp-production -n production \
            -o jsonpath='{.spec.selector.color}')

          if [ "$CURRENT" = "$TARGET" ]; then
            echo "✅ Traffic switch verified: $CURRENT"
          else
            echo "❌ Traffic switch failed! Expected $TARGET, got $CURRENT"
            exit 1
          fi

      - name: Keep old version warm
        run: |
          ACTIVE="${{ steps.env.outputs.active }}"
          echo "🔥 Keeping $ACTIVE warm for instant rollback"
          echo "To rollback, run: kubectl patch svc myapp-production -n production -p '{\"spec\":{\"selector\":{\"color\":\"$ACTIVE\"}}}'"

      # EMERGENCY ROLLBACK - can be triggered manually
      - name: Emergency rollback (manual trigger only)
        if: github.event_name == 'workflow_dispatch' && inputs.rollback == true
        run: |
          ACTIVE="${{ steps.env.outputs.active }}"
          echo "🚨 Emergency rollback to $ACTIVE..."

          kubectl patch svc myapp-production -n production \
            -p '{"spec":{"selector":{"color":"'$ACTIVE'"}}}'

          echo "✅ Rolled back to $ACTIVE"
```

### Steg 3: Database Migration Rollback

```yaml
# .github/workflows/deploy-with-db-migration.yml
name: Deploy with Database Migration

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      DATABASE_URL: ${{ secrets.DATABASE_URL }}

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Create database backup
        id: backup
        run: |
          BACKUP_NAME="pre-deploy-$(date +%Y%m%d-%H%M%S)-${{ github.sha }}"

          echo "📦 Creating backup: $BACKUP_NAME"

          # Skapa backup med pg_dump
          pg_dump "$DATABASE_URL" \
            --format=custom \
            --compress=9 \
            --file="backup/${BACKUP_NAME}.dump"

          # Ladda upp till S3
          aws s3 cp "backup/${BACKUP_NAME}.dump" \
            "s3://myapp-db-backups/${BACKUP_NAME}.dump" \
            --storage-class STANDARD_IA

          echo "backup_name=$BACKUP_NAME" >> $GITHUB_OUTPUT
          echo "✅ Backup uploaded to S3"

      - name: Run migrations
        id: migrate
        run: |
          echo "🔄 Running database migrations..."

          # Lista pending migrations
          npx prisma migrate status

          # Kör migrations
          if npx prisma migrate deploy; then
            echo "status=success" >> $GITHUB_OUTPUT
            echo "✅ Migrations completed"
          else
            echo "status=failure" >> $GITHUB_OUTPUT
            echo "❌ Migrations failed"
            exit 1
          fi

      - name: Deploy application
        id: deploy
        run: |
          echo "🚀 Deploying application..."

          kubectl set image deployment/myapp \
            app=myapp:${{ github.sha }} \
            -n production

          kubectl rollout status deployment/myapp \
            -n production \
            --timeout=300s

      - name: Health check
        id: health
        run: |
          echo "🏥 Running post-deployment health checks..."

          # Comprehensive health check
          npm run test:smoke:production

          echo "status=healthy" >> $GITHUB_OUTPUT

      - name: Rollback on failure
        if: failure()
        run: |
          echo "🔄 Initiating rollback..."

          # 1. Rollback application
          echo "Rolling back application..."
          kubectl rollout undo deployment/myapp -n production

          # 2. Rollback database
          echo "Rolling back database migrations..."

          # Försök först med migration rollback
          if npx prisma migrate reset --force --skip-seed 2>/dev/null; then
            echo "✅ Migration rollback successful"
          else
            # Om det misslyckas, restore från backup
            echo "⚠️ Migration rollback failed, restoring from backup..."

            BACKUP_NAME="${{ steps.backup.outputs.backup_name }}"

            # Ladda ner backup
            aws s3 cp "s3://myapp-db-backups/${BACKUP_NAME}.dump" \
              "/tmp/${BACKUP_NAME}.dump"

            # Restore
            pg_restore \
              --dbname="$DATABASE_URL" \
              --clean \
              --if-exists \
              "/tmp/${BACKUP_NAME}.dump"

            echo "✅ Database restored from backup"
          fi

      - name: Notify on rollback
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "🚨 Deployment with DB migration rolled back!",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Deployment Rollback*\nCommit: `${{ github.sha }}`\nBackup: `${{ steps.backup.outputs.backup_name }}`"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### Steg 4: Backup CI/CD Configuration

```yaml
# .github/workflows/backup-cicd-config.yml
name: Backup CI/CD Configuration

on:
  schedule:
    - cron: '0 2 * * *'  # Dagligen kl 02:00
  workflow_dispatch:

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
          cp -r .github/workflows/* backup/workflows/

          # Metadata
          cat > backup/metadata.json << EOF
          {
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "repository": "${{ github.repository }}",
            "commit": "${{ github.sha }}",
            "branch": "${{ github.ref_name }}",
            "backup_type": "scheduled"
          }
          EOF

      - name: Backup environments config
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');

            // Hämta environments
            const { data: envs } = await github.rest.repos.getAllEnvironments({
              owner: context.repo.owner,
              repo: context.repo.repo
            });

            // Hämta branch protection rules
            const { data: branches } = await github.rest.repos.listBranches({
              owner: context.repo.owner,
              repo: context.repo.repo,
              protected: true
            });

            const branchProtection = {};
            for (const branch of branches) {
              try {
                const { data: protection } = await github.rest.repos.getBranchProtection({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  branch: branch.name
                });
                branchProtection[branch.name] = protection;
              } catch (e) {
                console.log(`No protection for ${branch.name}`);
              }
            }

            fs.writeFileSync('backup/environments.json', JSON.stringify(envs, null, 2));
            fs.writeFileSync('backup/branch-protection.json', JSON.stringify(branchProtection, null, 2));

      - name: Backup secrets metadata
        run: |
          # OBS: Kan inte backup:a secrets-värden, bara metadata
          gh secret list --json name,updatedAt > backup/secrets-metadata.json
          gh variable list --json name,value > backup/variables.json
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Create backup archive
        run: |
          BACKUP_NAME="cicd-backup-$(date +%Y%m%d-%H%M%S)"
          tar -czf "${BACKUP_NAME}.tar.gz" backup/

          # Skapa checksum
          sha256sum "${BACKUP_NAME}.tar.gz" > "${BACKUP_NAME}.sha256"

          echo "backup_name=${BACKUP_NAME}" >> $GITHUB_ENV

      - name: Upload to S3
        run: |
          aws s3 cp "${backup_name}.tar.gz" \
            "s3://cicd-backups/${{ github.repository }}/${backup_name}.tar.gz"
          aws s3 cp "${backup_name}.sha256" \
            "s3://cicd-backups/${{ github.repository }}/${backup_name}.sha256"
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.BACKUP_AWS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.BACKUP_AWS_SECRET }}
          AWS_REGION: eu-west-1

      - name: Cleanup old backups
        run: |
          # Behåll senaste 30 dagarna
          aws s3 ls "s3://cicd-backups/${{ github.repository }}/" | \
            while read -r line; do
              DATE=$(echo $line | awk '{print $1}')
              FILE=$(echo $line | awk '{print $4}')
              if [[ $(date -d "$DATE" +%s) -lt $(date -d "-30 days" +%s) ]]; then
                aws s3 rm "s3://cicd-backups/${{ github.repository }}/$FILE"
              fi
            done
```

### Steg 5: Multi-Region Deployment

```yaml
# .github/workflows/multi-region-deploy.yml
name: Multi-Region Deployment

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image: ${{ steps.build.outputs.image }}
    steps:
      - uses: actions/checkout@v4

      - name: Build and push image
        id: build
        run: |
          IMAGE="myapp:${{ github.sha }}"
          docker build -t $IMAGE .

          # Push till alla regioners registries
          for region in eu-west-1 us-east-1 ap-southeast-1; do
            aws ecr get-login-password --region $region | \
              docker login --username AWS --password-stdin \
              ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${region}.amazonaws.com

            docker tag $IMAGE \
              ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${region}.amazonaws.com/$IMAGE
            docker push \
              ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${region}.amazonaws.com/$IMAGE
          done

          echo "image=$IMAGE" >> $GITHUB_OUTPUT

  deploy:
    needs: build
    runs-on: ubuntu-latest
    strategy:
      matrix:
        region: [eu-west-1, us-east-1, ap-southeast-1]
      fail-fast: false  # Fortsätt även om en region failar
      max-parallel: 1   # Deploy sekventiellt för säkerhet

    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl for ${{ matrix.region }}
        run: |
          aws eks update-kubeconfig \
            --region ${{ matrix.region }} \
            --name myapp-cluster-${{ matrix.region }}

      - name: Deploy to ${{ matrix.region }}
        run: |
          echo "🚀 Deploying to ${{ matrix.region }}..."

          kubectl set image deployment/myapp \
            app=${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ matrix.region }}.amazonaws.com/${{ needs.build.outputs.image }} \
            -n production

          kubectl rollout status deployment/myapp \
            -n production \
            --timeout=300s

      - name: Health check ${{ matrix.region }}
        run: |
          ENDPOINT=$(kubectl get svc myapp -n production \
            -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

          for i in {1..10}; do
            if curl -sf "https://$ENDPOINT/health"; then
              echo "✅ ${{ matrix.region }} healthy"
              exit 0
            fi
            sleep 10
          done
          echo "❌ Health check failed for ${{ matrix.region }}"
          exit 1

      - name: Update Route53 health check
        if: success()
        run: |
          aws route53 update-health-check \
            --health-check-id ${{ secrets[format('HEALTH_CHECK_{0}', matrix.region)] }} \
            --resource-path "/health" \
            --fully-qualified-domain-name "myapp-${{ matrix.region }}.example.com"

      - name: Rollback ${{ matrix.region }} on failure
        if: failure()
        run: |
          echo "🔄 Rolling back ${{ matrix.region }}..."
          kubectl rollout undo deployment/myapp -n production

  verify-global:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - name: Verify global deployment
        run: |
          echo "🌍 Verifying global deployment..."

          for region in eu-west-1 us-east-1 ap-southeast-1; do
            # Kolla Route53 health
            HEALTH=$(aws route53 get-health-check-status \
              --health-check-id ${{ secrets[format('HEALTH_CHECK_{0}', env.region)] }} \
              --query 'HealthCheckObservations[0].StatusReport.Status' \
              --output text)

            echo "Region $region: $HEALTH"
          done
```

### Steg 6: Emergency Response Workflow

```yaml
# .github/workflows/emergency-response.yml
name: Emergency Response

on:
  workflow_dispatch:
    inputs:
      action:
        description: 'Emergency action to take'
        required: true
        type: choice
        options:
          - rollback-last
          - rollback-version
          - scale-down
          - scale-up
          - maintenance-on
          - maintenance-off
          - rotate-secrets
      target:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - production
          - staging
          - all-regions
      version:
        description: 'Version to rollback to (if rollback-version)'
        required: false
      reason:
        description: 'Reason for emergency action'
        required: true

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Log incident
        run: |
          curl -X POST "${{ secrets.INCIDENT_API }}/incidents" \
            -H "Authorization: Bearer ${{ secrets.INCIDENT_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "action": "${{ inputs.action }}",
              "target": "${{ inputs.target }}",
              "reason": "${{ inputs.reason }}",
              "triggered_by": "${{ github.actor }}",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
              "run_id": "${{ github.run_id }}"
            }'

  execute:
    needs: validate
    runs-on: ubuntu-latest
    environment: emergency  # Kräver godkännande
    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl
        run: |
          if [ "${{ inputs.target }}" = "all-regions" ]; then
            for region in eu-west-1 us-east-1 ap-southeast-1; do
              aws eks update-kubeconfig --region $region --name myapp-cluster-$region
            done
          else
            aws eks update-kubeconfig --region eu-west-1 --name myapp-cluster
          fi

      - name: Execute - Rollback to last version
        if: inputs.action == 'rollback-last'
        run: |
          echo "🔄 Rolling back to previous version..."
          kubectl rollout undo deployment/myapp -n ${{ inputs.target }}
          kubectl rollout status deployment/myapp -n ${{ inputs.target }}

      - name: Execute - Rollback to specific version
        if: inputs.action == 'rollback-version' && inputs.version != ''
        run: |
          echo "🔄 Rolling back to version ${{ inputs.version }}..."
          kubectl set image deployment/myapp \
            app=myapp:${{ inputs.version }} \
            -n ${{ inputs.target }}
          kubectl rollout status deployment/myapp -n ${{ inputs.target }}

      - name: Execute - Scale down
        if: inputs.action == 'scale-down'
        run: |
          echo "⬇️ Scaling down..."
          kubectl scale deployment/myapp --replicas=0 -n ${{ inputs.target }}

      - name: Execute - Scale up
        if: inputs.action == 'scale-up'
        run: |
          echo "⬆️ Scaling up..."
          kubectl scale deployment/myapp --replicas=3 -n ${{ inputs.target }}
          kubectl rollout status deployment/myapp -n ${{ inputs.target }}

      - name: Execute - Maintenance mode ON
        if: inputs.action == 'maintenance-on'
        run: |
          echo "🔧 Enabling maintenance mode..."
          kubectl apply -f k8s/maintenance-page.yaml -n ${{ inputs.target }}
          kubectl patch ingress myapp -n ${{ inputs.target }} \
            -p '{"spec":{"rules":[{"host":"myapp.com","http":{"paths":[{"path":"/","pathType":"Prefix","backend":{"service":{"name":"maintenance","port":{"number":80}}}}]}}]}}'

      - name: Execute - Maintenance mode OFF
        if: inputs.action == 'maintenance-off'
        run: |
          echo "✅ Disabling maintenance mode..."
          kubectl delete -f k8s/maintenance-page.yaml -n ${{ inputs.target }} --ignore-not-found
          kubectl apply -f k8s/ingress.yaml -n ${{ inputs.target }}

      - name: Execute - Rotate secrets
        if: inputs.action == 'rotate-secrets'
        run: |
          echo "🔐 Rotating secrets..."
          ./scripts/rotate-secrets.sh ${{ inputs.target }}
          kubectl rollout restart deployment/myapp -n ${{ inputs.target }}

  notify:
    needs: [validate, execute]
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Notify team
        run: |
          STATUS="${{ needs.execute.result }}"

          if [ "$STATUS" = "success" ]; then
            EMOJI="✅"
            COLOR="good"
          else
            EMOJI="❌"
            COLOR="danger"
          fi

          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H "Content-Type: application/json" \
            -d '{
              "attachments": [{
                "color": "'$COLOR'",
                "blocks": [
                  {
                    "type": "header",
                    "text": {"type": "plain_text", "text": "'$EMOJI' Emergency Action '$STATUS'"}
                  },
                  {
                    "type": "section",
                    "fields": [
                      {"type": "mrkdwn", "text": "*Action:*\n${{ inputs.action }}"},
                      {"type": "mrkdwn", "text": "*Target:*\n${{ inputs.target }}"},
                      {"type": "mrkdwn", "text": "*Triggered by:*\n${{ github.actor }}"},
                      {"type": "mrkdwn", "text": "*Reason:*\n${{ inputs.reason }}"}
                    ]
                  }
                ]
              }]
            }'
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Complete DR Setup med Terraform

```hcl
# terraform/dr-infrastructure/main.tf

# Multi-region EKS clusters
module "eks_primary" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "myapp-primary"
  cluster_version = "1.28"

  vpc_id     = module.vpc_primary.vpc_id
  subnet_ids = module.vpc_primary.private_subnets

  eks_managed_node_groups = {
    main = {
      min_size     = 3
      max_size     = 10
      desired_size = 5

      instance_types = ["t3.large"]
    }
  }

  providers = {
    aws = aws.primary
  }
}

module "eks_dr" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "myapp-dr"
  cluster_version = "1.28"

  vpc_id     = module.vpc_dr.vpc_id
  subnet_ids = module.vpc_dr.private_subnets

  eks_managed_node_groups = {
    main = {
      min_size     = 1  # Minimal i standby
      max_size     = 10
      desired_size = 1

      instance_types = ["t3.large"]
    }
  }

  providers = {
    aws = aws.dr
  }
}

# Route53 Health Checks
resource "aws_route53_health_check" "primary" {
  fqdn              = "myapp-primary.example.com"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = "3"
  request_interval  = "30"

  tags = {
    Name = "myapp-primary-health"
  }
}

resource "aws_route53_health_check" "dr" {
  fqdn              = "myapp-dr.example.com"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = "3"
  request_interval  = "30"

  tags = {
    Name = "myapp-dr-health"
  }
}

# Failover routing
resource "aws_route53_record" "myapp" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "myapp.example.com"
  type    = "A"

  failover_routing_policy {
    type = "PRIMARY"
  }

  set_identifier  = "primary"
  health_check_id = aws_route53_health_check.primary.id

  alias {
    name                   = module.alb_primary.dns_name
    zone_id                = module.alb_primary.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "myapp_failover" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "myapp.example.com"
  type    = "A"

  failover_routing_policy {
    type = "SECONDARY"
  }

  set_identifier  = "dr"
  health_check_id = aws_route53_health_check.dr.id

  alias {
    name                   = module.alb_dr.dns_name
    zone_id                = module.alb_dr.zone_id
    evaluate_target_health = true
  }
}

# Database replication
resource "aws_rds_cluster" "primary" {
  cluster_identifier = "myapp-primary"
  engine             = "aurora-postgresql"
  engine_version     = "15.4"

  database_name   = "myapp"
  master_username = var.db_username
  master_password = var.db_password

  backup_retention_period = 35
  preferred_backup_window = "02:00-03:00"

  # Enable global database for cross-region replication
  global_cluster_identifier = aws_rds_global_cluster.myapp.id

  provider = aws.primary
}

resource "aws_rds_cluster" "dr" {
  cluster_identifier = "myapp-dr"
  engine             = "aurora-postgresql"
  engine_version     = "15.4"

  global_cluster_identifier = aws_rds_global_cluster.myapp.id

  # DR cluster is read-only until failover

  provider = aws.dr
}
```

### Exempel 2: Secrets Rotation Script

```bash
#!/bin/bash
# scripts/rotate-secrets.sh

set -euo pipefail

ENVIRONMENT=${1:-production}
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="/var/log/secret-rotation-${TIMESTAMP}.log"

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $1" | tee -a "$LOG_FILE"
}

rotate_database_password() {
  log "Rotating database password..."

  # Generera nytt lösenord
  NEW_PASSWORD=$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 32)

  # Uppdatera i AWS Secrets Manager
  aws secretsmanager update-secret \
    --secret-id "myapp/${ENVIRONMENT}/database" \
    --secret-string "{\"password\":\"${NEW_PASSWORD}\"}"

  # Uppdatera i Kubernetes
  kubectl create secret generic db-credentials \
    --from-literal=password="${NEW_PASSWORD}" \
    --namespace="${ENVIRONMENT}" \
    --dry-run=client -o yaml | kubectl apply -f -

  log "Database password rotated successfully"
}

rotate_api_keys() {
  log "Rotating API keys..."

  # Generera nya API keys
  NEW_KEY=$(openssl rand -hex 32)

  # Uppdatera i GitHub secrets
  gh secret set API_KEY --body "${NEW_KEY}" --repo "$GITHUB_REPOSITORY"

  # Uppdatera i Kubernetes
  kubectl create secret generic api-credentials \
    --from-literal=api-key="${NEW_KEY}" \
    --namespace="${ENVIRONMENT}" \
    --dry-run=client -o yaml | kubectl apply -f -

  log "API keys rotated successfully"
}

rotate_tls_certificates() {
  log "Rotating TLS certificates..."

  # Trigger cert-manager renewal
  kubectl delete secret myapp-tls --namespace="${ENVIRONMENT}" --ignore-not-found

  # Vänta på ny cert
  for i in {1..60}; do
    if kubectl get secret myapp-tls --namespace="${ENVIRONMENT}" 2>/dev/null; then
      log "New TLS certificate issued"
      return 0
    fi
    sleep 5
  done

  log "ERROR: TLS certificate not issued within timeout"
  return 1
}

main() {
  log "Starting secret rotation for ${ENVIRONMENT}"

  rotate_database_password
  rotate_api_keys
  rotate_tls_certificates

  log "Secret rotation completed"

  # Skicka audit event
  curl -X POST "${AUDIT_API}/events" \
    -H "Authorization: Bearer ${AUDIT_TOKEN}" \
    -d "{\"event\":\"secret_rotation\",\"environment\":\"${ENVIRONMENT}\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"
}

main "$@"
```

### Exempel 3: DR Runbook Automation

```yaml
# .github/workflows/dr-runbook.yml
name: DR Runbook - Failover to DR Region

on:
  workflow_dispatch:
    inputs:
      confirm:
        description: 'Type "FAILOVER" to confirm'
        required: true
      reason:
        description: 'Reason for failover'
        required: true

jobs:
  validate:
    runs-on: ubuntu-latest
    outputs:
      proceed: ${{ steps.check.outputs.proceed }}
    steps:
      - name: Validate confirmation
        id: check
        run: |
          if [ "${{ inputs.confirm }}" = "FAILOVER" ]; then
            echo "proceed=true" >> $GITHUB_OUTPUT
          else
            echo "❌ Invalid confirmation. Expected 'FAILOVER', got '${{ inputs.confirm }}'"
            echo "proceed=false" >> $GITHUB_OUTPUT
            exit 1
          fi

  pre-failover:
    needs: validate
    if: needs.validate.outputs.proceed == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Create incident ticket
        id: ticket
        run: |
          TICKET=$(curl -X POST "${{ secrets.JIRA_API }}/issue" \
            -H "Authorization: Basic ${{ secrets.JIRA_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "fields": {
                "project": {"key": "INC"},
                "summary": "DR Failover initiated",
                "description": "Reason: ${{ inputs.reason }}",
                "issuetype": {"name": "Incident"}
              }
            }' | jq -r '.key')
          echo "ticket=$TICKET" >> $GITHUB_OUTPUT

      - name: Verify DR region health
        run: |
          # Kolla att DR-regionen är redo
          aws eks update-kubeconfig --region us-west-2 --name myapp-dr

          if kubectl get nodes | grep -q "Ready"; then
            echo "✅ DR cluster is healthy"
          else
            echo "❌ DR cluster is not healthy!"
            exit 1
          fi

      - name: Scale up DR
        run: |
          echo "⬆️ Scaling up DR region..."

          # Scale node group
          aws eks update-nodegroup-config \
            --cluster-name myapp-dr \
            --nodegroup-name main \
            --scaling-config minSize=3,maxSize=10,desiredSize=5 \
            --region us-west-2

          # Vänta på nodes
          kubectl wait --for=condition=ready nodes --all --timeout=300s

  failover:
    needs: pre-failover
    runs-on: ubuntu-latest
    environment: dr-failover  # Kräver manuellt godkännande
    steps:
      - name: Promote DR database
        run: |
          echo "🗄️ Promoting DR database to primary..."

          aws rds failover-global-cluster \
            --global-cluster-identifier myapp-global \
            --target-db-cluster-identifier myapp-dr \
            --region us-west-2

      - name: Update DNS
        run: |
          echo "🌐 Updating DNS to point to DR..."

          # Disable primary health check temporarily
          aws route53 update-health-check \
            --health-check-id ${{ secrets.PRIMARY_HEALTH_CHECK }} \
            --disabled

          # Force traffic to DR
          aws route53 change-resource-record-sets \
            --hosted-zone-id ${{ secrets.HOSTED_ZONE_ID }} \
            --change-batch '{
              "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                  "Name": "myapp.example.com",
                  "Type": "A",
                  "AliasTarget": {
                    "HostedZoneId": "'${{ secrets.DR_ALB_ZONE }}'",
                    "DNSName": "'${{ secrets.DR_ALB_DNS }}'",
                    "EvaluateTargetHealth": true
                  }
                }
              }]
            }'

      - name: Verify failover
        run: |
          echo "🔍 Verifying failover..."

          # Vänta på DNS propagation
          sleep 60

          # Testa production endpoint
          for i in {1..10}; do
            if curl -sf "https://myapp.example.com/health"; then
              echo "✅ Failover successful - DR region serving traffic"
              exit 0
            fi
            sleep 10
          done

          echo "❌ Failover verification failed"
          exit 1

  post-failover:
    needs: failover
    runs-on: ubuntu-latest
    steps:
      - name: Update monitoring
        run: |
          # Uppdatera Datadog/Grafana dashboards
          curl -X POST "${{ secrets.DATADOG_API }}/dashboard" \
            -H "DD-API-KEY: ${{ secrets.DATADOG_API_KEY }}" \
            -d '{"active_region": "us-west-2"}'

      - name: Notify stakeholders
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{
              "text": "🚨 DR FAILOVER COMPLETE",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*DR Failover Complete*\n\n• Primary region: OFFLINE\n• DR region: ACTIVE\n• Reason: ${{ inputs.reason }}\n• Triggered by: ${{ github.actor }}"
                  }
                }
              ]
            }'

          # Skicka SMS till on-call
          curl -X POST "https://api.twilio.com/2010-04-01/Accounts/${{ secrets.TWILIO_ACCOUNT }}/Messages.json" \
            -u "${{ secrets.TWILIO_ACCOUNT }}:${{ secrets.TWILIO_TOKEN }}" \
            -d "To=${{ secrets.ONCALL_PHONE }}" \
            -d "From=${{ secrets.TWILIO_NUMBER }}" \
            -d "Body=DR FAILOVER COMPLETE - Check Slack for details"
```

------------------------------------------------------------

## Bästa Praxis

### 1. Definiera Tydliga RTO/RPO-mål

```yaml
# Dokumentera RTO/RPO i README eller runbook
# dr-config.yaml
disaster_recovery:
  rto_targets:
    tier1_critical:
      rto: "15 minutes"
      rpo: "0 (zero data loss)"
      services:
        - payment-service
        - auth-service
    tier2_important:
      rto: "1 hour"
      rpo: "1 hour"
      services:
        - api-gateway
        - notification-service
    tier3_standard:
      rto: "4 hours"
      rpo: "24 hours"
      services:
        - analytics-service
        - reporting-service
```

### 2. Implementera Immutable Infrastructure

```yaml
# Använd immutable deployments - aldrig modifiera running instances
jobs:
  deploy:
    steps:
      # ❌ DÅLIGT: Modifiera befintliga instanser
      # - run: ssh server "git pull && npm install && pm2 restart"

      # ✅ BRA: Bygg ny image och deploy
      - name: Build immutable image
        run: |
          docker build -t myapp:${{ github.sha }} .
          docker push myapp:${{ github.sha }}

      - name: Deploy new version
        run: |
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}
```

### 3. Testa DR-procedurer Regelbundet

```yaml
# Schemalägg DR-tester månadsvis
name: Monthly DR Test

on:
  schedule:
    - cron: '0 3 1 * *'  # Första dagen varje månad

jobs:
  dr-test:
    runs-on: ubuntu-latest
    environment: dr-test
    steps:
      - name: Simulate primary failure
        run: |
          # Scale down primary (i staging)
          kubectl scale deployment/myapp --replicas=0 -n staging

      - name: Verify failover
        run: |
          # Verifiera att traffic går till DR
          sleep 60
          curl -sf https://staging.myapp.com/health

      - name: Restore primary
        run: |
          kubectl scale deployment/myapp --replicas=3 -n staging

      - name: Document results
        run: |
          echo "DR test completed at $(date)" >> dr-test-results.log
```

### 4. Håll Backup och Recovery Scripts Uppdaterade

```bash
# Versionshantera alla DR-scripts
# scripts/dr/
# ├── backup-database.sh
# ├── restore-database.sh
# ├── failover-to-dr.sh
# ├── failback-to-primary.sh
# └── verify-failover.sh

# Testa scripts regelbundet
#!/bin/bash
# scripts/verify-dr-scripts.sh

set -e

echo "Verifying DR scripts..."

# Syntax check
for script in scripts/dr/*.sh; do
  bash -n "$script" && echo "✅ $script syntax OK"
done

# Dry run (om möjligt)
bash scripts/dr/backup-database.sh --dry-run
bash scripts/dr/failover-to-dr.sh --dry-run

echo "All DR scripts verified"
```

### 5. Dokumentera Runbooks

```markdown
# DR Runbook: Complete Failover

## Prerequisites
- [ ] Access to AWS console
- [ ] kubectl configured for both regions
- [ ] Slack/PagerDuty access for notifications

## Steps

### 1. Assess Situation (5 min)
- Verify primary region is actually down
- Check Route53 health checks
- Review CloudWatch metrics

### 2. Initiate Failover (10 min)
- Run: `gh workflow run dr-runbook.yml -f confirm=FAILOVER -f reason="Primary region outage"`
- Monitor workflow progress
- Verify DR region is serving traffic

### 3. Post-Failover (15 min)
- Update status page
- Notify stakeholders
- Create incident ticket

### 4. Investigate & Recover Primary (varies)
- Diagnose primary region issues
- Restore when ready
- Plan failback

## Rollback
If DR failover fails:
- Scale up backup instances in third region
- Contact AWS support
- Use manual DNS override
```

------------------------------------------------------------

## Vanliga Fallgropar

### ❌ Fallgrop 1: Aldrig Testa DR

```yaml
# Problem: DR-planen har aldrig testats
# När katastrofen väl inträffar fungerar ingenting

# ✅ Lösning: Regelbundna DR-tester
name: Quarterly DR Drill

on:
  schedule:
    - cron: '0 6 1 */3 *'  # Första dagen varje kvartal

jobs:
  full-dr-drill:
    runs-on: ubuntu-latest
    steps:
      - name: Execute full DR drill
        run: |
          echo "🚨 Starting quarterly DR drill..."

          # Dokumentera start
          START_TIME=$(date +%s)

          # Kör failover
          ./scripts/dr/failover-to-dr.sh

          # Verifiera
          ./scripts/dr/verify-failover.sh

          # Kör failback
          ./scripts/dr/failback-to-primary.sh

          # Beräkna tid
          END_TIME=$(date +%s)
          DURATION=$((END_TIME - START_TIME))

          echo "DR drill completed in ${DURATION} seconds"

          # Jämför med RTO
          if [ $DURATION -gt 900 ]; then  # 15 min
            echo "⚠️ WARNING: Exceeded 15 min RTO target"
          fi
```

### ❌ Fallgrop 2: Secrets Inte Synkade till DR

```yaml
# Problem: Secrets finns bara i primary region
# DR failover misslyckas pga saknade credentials

# ✅ Lösning: Synka secrets till alla regioner
name: Sync Secrets to DR

on:
  workflow_dispatch:
  repository_dispatch:
    types: [secrets-updated]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Sync to AWS Secrets Manager DR
        run: |
          # Lista alla secrets i primary
          SECRETS=$(aws secretsmanager list-secrets \
            --region eu-west-1 \
            --query 'SecretList[].Name' \
            --output text)

          for secret in $SECRETS; do
            # Hämta från primary
            VALUE=$(aws secretsmanager get-secret-value \
              --secret-id $secret \
              --region eu-west-1 \
              --query 'SecretString' \
              --output text)

            # Uppdatera i DR region
            aws secretsmanager put-secret-value \
              --secret-id $secret \
              --secret-string "$VALUE" \
              --region us-west-2

            echo "✅ Synced: $secret"
          done
```

### ❌ Fallgrop 3: Databas Lag vid Failover

```yaml
# Problem: Asynkron replikering orsakar dataförlust

# ✅ Lösning: Övervaka replication lag
name: Monitor Replication Lag

on:
  schedule:
    - cron: '*/5 * * * *'

jobs:
  check-lag:
    runs-on: ubuntu-latest
    steps:
      - name: Check replication lag
        run: |
          LAG=$(aws rds describe-db-clusters \
            --db-cluster-identifier myapp-dr \
            --query 'DBClusters[0].ReplicationLag' \
            --output text)

          # Alert om lag > 60 sekunder
          if [ "$LAG" -gt 60 ]; then
            curl -X POST ${{ secrets.PAGERDUTY_WEBHOOK }} \
              -d "{\"event_action\":\"trigger\",\"payload\":{\"summary\":\"DB replication lag: ${LAG}s\"}}"
          fi
```

### ❌ Fallgrop 4: Glömma External Dependencies

```yaml
# Problem: Applikationen beroende av services som inte har DR

# ✅ Lösning: Mappa och planera för alla beroenden
# dependencies.yaml
external_dependencies:
  - name: Stripe
    type: payment
    dr_strategy: "Multi-region by provider"
    failover: automatic

  - name: SendGrid
    type: email
    dr_strategy: "Fallback to AWS SES"
    failover: manual
    runbook: docs/sendgrid-failover.md

  - name: Redis Cloud
    type: cache
    dr_strategy: "Warm standby in DR region"
    failover: automatic
    rto: 5 minutes
```

### ❌ Fallgrop 5: Ingen Kommunikationsplan

```yaml
# Problem: Ingen vet vem som ska göra vad under incident

# ✅ Lösning: Automatisera kommunikation
name: DR Communication

on:
  workflow_call:
    inputs:
      phase:
        required: true
        type: string
      status:
        required: true
        type: string

jobs:
  communicate:
    runs-on: ubuntu-latest
    steps:
      - name: Update status page
        run: |
          curl -X POST "https://api.statuspage.io/v1/pages/$PAGE_ID/incidents" \
            -H "Authorization: OAuth ${{ secrets.STATUSPAGE_TOKEN }}" \
            -d '{
              "incident": {
                "name": "Infrastructure Failover in Progress",
                "status": "${{ inputs.status }}",
                "body": "We are executing DR procedures. Updates every 15 minutes."
              }
            }'

      - name: Notify internal teams
        run: |
          # Engineering
          curl -X POST ${{ secrets.SLACK_ENGINEERING }} \
            -d '{"text":"🚨 DR Phase: ${{ inputs.phase }} - Status: ${{ inputs.status }}"}'

          # Support
          curl -X POST ${{ secrets.SLACK_SUPPORT }} \
            -d '{"text":"📢 Customer impact: DR in progress. Check status page."}'

          # Leadership
          if [ "${{ inputs.phase }}" = "failover-complete" ]; then
            curl -X POST ${{ secrets.SLACK_LEADERSHIP }} \
              -d '{"text":"DR failover completed. Incident report will follow."}'
          fi
```

------------------------------------------------------------

## Övningar

### Övning 1: Implementera Basic Rollback (20 XP)

**Mål:** Skapa en deployment workflow med automatisk rollback vid failure.

**Din uppgift:**
1. Skapa `.github/workflows/deploy-with-rollback.yml`
2. Implementera deployment till Kubernetes
3. Lägg till health check efter deployment
4. Implementera automatisk rollback om health check misslyckas
5. Lägg till Slack-notifikation vid rollback

<details>
<summary>Ledtråd</summary>

Använd `kubectl rollout status` med timeout och `kubectl rollout undo` för rollback. Kontrollera `if: failure()` för att trigga rollback-steg.

</details>

<details>
<summary>Lösning</summary>

```yaml
name: Deploy with Rollback

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure kubectl
        run: |
          echo "${{ secrets.KUBECONFIG }}" | base64 -d > kubeconfig
          export KUBECONFIG=kubeconfig

      - name: Deploy
        id: deploy
        run: |
          kubectl set image deployment/myapp app=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp --timeout=300s

      - name: Health check
        id: health
        run: |
          for i in {1..5}; do
            if curl -sf http://myapp.example.com/health; then
              echo "✅ Health check passed"
              exit 0
            fi
            sleep 10
          done
          exit 1

      - name: Rollback on failure
        if: failure()
        run: |
          kubectl rollout undo deployment/myapp
          kubectl rollout status deployment/myapp

      - name: Notify rollback
        if: failure()
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"⚠️ Deployment rolled back for ${{ github.sha }}"}'
```

</details>

---

### Övning 2: Skapa DR Backup Workflow (25 XP)

**Mål:** Automatisera backup av CI/CD-konfiguration och kritiska data.

**Din uppgift:**
1. Skapa daglig backup av `.github/workflows/`
2. Exportera GitHub environments och branch protection rules
3. Backup secrets metadata (inte värden)
4. Ladda upp till S3 med versionering
5. Implementera retention policy (behåll 30 dagar)

<details>
<summary>Ledtråd</summary>

Använd `gh api` för att hämta environments och branch protection. `gh secret list` ger metadata utan värden.

</details>

<details>
<summary>Lösning</summary>

```yaml
name: Daily CI/CD Backup

on:
  schedule:
    - cron: '0 2 * * *'

jobs:
  backup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Backup workflows
        run: |
          mkdir -p backup
          cp -r .github/workflows backup/

          # Metadata
          echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","sha":"${{ github.sha }}"}' > backup/metadata.json

      - name: Export GitHub config
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Environments
          gh api repos/${{ github.repository }}/environments > backup/environments.json

          # Branch protection
          gh api repos/${{ github.repository }}/branches/main/protection > backup/branch-protection.json || true

          # Secrets metadata
          gh secret list --json name,updatedAt > backup/secrets.json
          gh variable list --json name,value > backup/variables.json

      - name: Upload to S3
        run: |
          BACKUP_NAME="backup-$(date +%Y%m%d)"
          tar -czf ${BACKUP_NAME}.tar.gz backup/

          aws s3 cp ${BACKUP_NAME}.tar.gz \
            s3://myapp-cicd-backups/${BACKUP_NAME}.tar.gz
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET }}

      - name: Cleanup old backups
        run: |
          # Ta bort backups äldre än 30 dagar
          aws s3 ls s3://myapp-cicd-backups/ | while read -r line; do
            DATE=$(echo $line | awk '{print $1}')
            FILE=$(echo $line | awk '{print $4}')
            if [[ $(date -d "$DATE" +%s) -lt $(date -d "-30 days" +%s) ]]; then
              aws s3 rm "s3://myapp-cicd-backups/$FILE"
            fi
          done
```

</details>

---

### Övning 3: Emergency Response Workflow (35 XP)

**Mål:** Bygg ett komplett emergency response system med flera åtgärdstyper.

**Din uppgift:**
1. Skapa `workflow_dispatch` med val för olika emergency actions
2. Implementera: rollback, scale-down, maintenance mode, rotate secrets
3. Kräv environment approval för emergency environment
4. Logga alla actions till incident management system
5. Skicka notifikationer till multiple kanaler (Slack, SMS)

<details>
<summary>Ledtråd</summary>

Använd `type: choice` i workflow_dispatch för att erbjuda flera alternativ. Separata jobs per action med `if: inputs.action == 'xxx'`.

</details>

<details>
<summary>Lösning</summary>

```yaml
name: Emergency Response

on:
  workflow_dispatch:
    inputs:
      action:
        type: choice
        required: true
        options:
          - rollback-last
          - scale-down
          - maintenance-on
          - maintenance-off
          - rotate-secrets
      reason:
        required: true
        description: 'Reason for emergency action'

jobs:
  log-incident:
    runs-on: ubuntu-latest
    steps:
      - name: Create incident record
        run: |
          curl -X POST "${{ secrets.INCIDENT_API }}" \
            -H "Authorization: Bearer ${{ secrets.INCIDENT_TOKEN }}" \
            -d '{
              "action": "${{ inputs.action }}",
              "reason": "${{ inputs.reason }}",
              "actor": "${{ github.actor }}",
              "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
            }'

  execute:
    needs: log-incident
    runs-on: ubuntu-latest
    environment: emergency
    steps:
      - uses: actions/checkout@v4

      - name: Rollback
        if: inputs.action == 'rollback-last'
        run: |
          kubectl rollout undo deployment/myapp -n production

      - name: Scale down
        if: inputs.action == 'scale-down'
        run: |
          kubectl scale deployment/myapp --replicas=0 -n production

      - name: Maintenance ON
        if: inputs.action == 'maintenance-on'
        run: |
          kubectl apply -f k8s/maintenance.yaml
          kubectl patch ingress myapp -p '{"spec":{"rules":[{"http":{"paths":[{"backend":{"service":{"name":"maintenance"}}}]}}]}}'

      - name: Maintenance OFF
        if: inputs.action == 'maintenance-off'
        run: |
          kubectl apply -f k8s/ingress.yaml

      - name: Rotate secrets
        if: inputs.action == 'rotate-secrets'
        run: |
          ./scripts/rotate-secrets.sh production

  notify:
    needs: execute
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Slack
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"🚨 Emergency: ${{ inputs.action }} - ${{ needs.execute.result }}"}'

      - name: SMS
        run: |
          curl -X POST "https://api.twilio.com/Messages.json" \
            -u "${{ secrets.TWILIO_SID }}:${{ secrets.TWILIO_TOKEN }}" \
            -d "To=${{ secrets.ONCALL_PHONE }}" \
            -d "From=${{ secrets.TWILIO_NUMBER }}" \
            -d "Body=Emergency action: ${{ inputs.action }}"
```

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **Blue/Green Deployments:** Grund för snabb failover utan nedtid
- **Canary Releases:** Gradvis utrullning med automatisk rollback
- **Multi-Environment Deployments:** Hantera staging/production environments
- **Secrets Management:** Kritiskt för DR - secrets måste vara tillgängliga i alla regioner
- **Monitoring CI/CD Pipelines:** Upptäck problem innan de kräver DR

### Förkunskaper:
- Kubernetes Deployments och Services
- Cloud infrastructure basics (AWS/GCP/Azure)
- Database backup och restore
- DNS och load balancing

### Bygger mot:
- Enterprise CI/CD Patterns
- Multi-region cloud architecture
- SRE practices
- Business Continuity Planning

------------------------------------------------------------

## Sammanfattning

- **RTO/RPO** definierar hur snabbt du måste återhämta dig och hur mycket data du kan förlora
- **Immutable infrastructure** gör rollback enklare och säkrare
- **Blue/Green deployment** ger instant failover genom att hålla två versioner körandes
- **Database DR** kräver replikering och övervakad replication lag
- **Backup CI/CD config** regelbundet - workflows, secrets metadata, environments
- **Multi-region** deployment ger geografisk redundans men ökar komplexitet
- **Emergency workflows** ska vara fördefinierade och testade
- **Kommunikationsplan** är lika viktig som teknisk plan
- **Testa DR regelbundet** - en plan som aldrig testats är ingen plan
- **Dokumentera runbooks** så att vem som helst kan utföra failover

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `kubectl rollout undo` | Rollback deployment | `kubectl rollout undo deployment/myapp` |
| `kubectl rollout status` | Vänta på rollout | `kubectl rollout status deployment/myapp --timeout=300s` |
| `kubectl rollout history` | Visa deployment history | `kubectl rollout history deployment/myapp` |
| `kubectl scale` | Skala deployment | `kubectl scale deployment/myapp --replicas=0` |
| `pg_dump` | Backup PostgreSQL | `pg_dump $DATABASE_URL > backup.sql` |
| `pg_restore` | Restore PostgreSQL | `pg_restore --dbname=$URL backup.dump` |
| `aws rds failover-global-cluster` | Failover Aurora | `aws rds failover-global-cluster --global-cluster-identifier myapp` |
| `aws route53 change-resource-record-sets` | Uppdatera DNS | `aws route53 change-resource-record-sets --hosted-zone-id X --change-batch file://changes.json` |
| `gh workflow run` | Trigga workflow manuellt | `gh workflow run dr-failover.yml -f confirm=FAILOVER` |

------------------------------------------------------------

## Referenser

- AWS Disaster Recovery Whitepaper: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/
- Kubernetes Rollout Documentation: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment
- Aurora Global Database: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html
- Route53 Health Checks: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html
- GitHub Actions workflow_dispatch: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch
- SRE Book - Disaster Recovery: https://sre.google/sre-book/managing-incidents/
- NIST Contingency Planning Guide: https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
- PagerDuty Incident Response: https://response.pagerduty.com/
""",
        },
        {
            "order_index": 17,
            "title": "CircleCI and Other Platforms",
            "slug": "circleci-other-platforms",
            "difficulty": "intermediate",
            "content": """# CircleCI and Other Platforms

Medan GitHub Actions dominerar marknaden finns det flera andra kraftfulla CI/CD-plattformar, var och en med sina styrkor. Att förstå CircleCI, Travis CI, GitLab CI, Bitbucket Pipelines och Buildkite ger dig flexibilitet att välja rätt verktyg för varje projekt och gör dig till en mer komplett DevOps-ingenjör.

------------------------------------------------------------

## Introduktion

### Varför Lära Sig Flera CI/CD-plattformar?

I en verklig DevOps-karriär kommer du att stöta på olika CI/CD-system beroende på organisationens val, legacy-system, eller specifika krav. Att kunna navigera mellan plattformar är en värdefull färdighet.

**När väljer man vilken plattform?**
- **CircleCI:** Snabbhet, Docker-native, avancerad parallelism
- **GitLab CI:** All-in-one DevOps, self-hosted möjlighet
- **Travis CI:** Open source-projekt, enkel konfiguration
- **Bitbucket Pipelines:** Atlassian-ekosystem (Jira, Confluence)
- **Buildkite:** Hybrid cloud/self-hosted, maximal kontroll
- **Azure DevOps:** Microsoft-ekosystem, enterprise-features

### Vad du kommer lära dig

Efter denna modul kommer du kunna:
- Konfigurera pipelines i CircleCI, GitLab CI, Travis CI, Bitbucket och Buildkite
- Migrera pipelines mellan olika plattformar
- Välja rätt plattform baserat på projektets krav
- Utnyttja varje plattforms unika styrkor
- Implementera cross-platform CI/CD-strategier

### Förkunskaper

- Solid förståelse för GitHub Actions
- Grundläggande YAML-kunskap
- Docker och containerisering
- Git och versionshantering

------------------------------------------------------------

## Teori

### CI/CD Platform Landscape

```
+------------------------------------------------------------------+
|                   CI/CD PLATFORM LANDSCAPE                       |
+------------------------------------------------------------------+
|                                                                  |
|   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              |
|   │   GitHub    │  │   GitLab    │  │  CircleCI   │              |
|   │   Actions   │  │     CI      │  │             │              |
|   │  ─────────  │  │  ─────────  │  │  ─────────  │              |
|   │ Cloud-first │  │  All-in-one │  │ Docker-first│              |
|   │ Marketplace │  │ Self-hosted │  │   Speed     │              |
|   │  Matrix     │  │ Auto DevOps │  │  Orbs       │              |
|   └─────────────┘  └─────────────┘  └─────────────┘              |
|                                                                  |
|   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              |
|   │  Bitbucket  │  │  Buildkite  │  │   Azure     │              |
|   │  Pipelines  │  │             │  │   DevOps    │              |
|   │  ─────────  │  │  ─────────  │  │  ─────────  │              |
|   │  Atlassian  │  │   Hybrid    │  │  Microsoft  │              |
|   │    Pipes    │  │   Agents    │  │  Pipelines  │              |
|   │    Jira     │  │  Plugins    │  │    Boards   │              |
|   └─────────────┘  └─────────────┘  └─────────────┘              |
|                                                                  |
+------------------------------------------------------------------+
```

### Platform Comparison

| Feature | GitHub Actions | CircleCI | GitLab CI | Bitbucket | Buildkite |
|---------|---------------|----------|-----------|-----------|-----------|
| **Hosting** | Cloud | Cloud/Server | Cloud/Self | Cloud | Hybrid |
| **Config** | YAML | YAML | YAML | YAML | YAML |
| **Parallelism** | Matrix | Native | Parallel | Limited | Native |
| **Caching** | actions/cache | Built-in | Built-in | Built-in | Plugin |
| **Secrets** | Encrypted | Contexts | Variables | Variables | Hooks |
| **Docker** | Good | Excellent | Good | Good | Excellent |
| **Pricing** | Minutes | Credits | Minutes | Minutes | Agents |

### Gemensamma Koncept

```
+------------------------------------------------------------------+
|              UNIVERSELLA CI/CD KONCEPT                           |
+------------------------------------------------------------------+
|                                                                  |
|   ┌─────────────────────────────────────────────────────────┐    |
|   │                    PIPELINE                              │    |
|   │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │    |
|   │  │   JOB    │→ │   JOB    │→ │   JOB    │→ │   JOB    │ │    |
|   │  │  Build   │  │   Test   │  │  Deploy  │  │ Notify   │ │    |
|   │  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │    |
|   └─────────────────────────────────────────────────────────┘    |
|                                                                  |
|   Varje plattform har:                                           |
|   • Pipeline definition (YAML-fil)                               |
|   • Jobs (körbara enheter)                                       |
|   • Steps/Commands (individuella kommandon)                      |
|   • Artifacts (output som delas mellan jobs)                     |
|   • Caching (snabba upp builds)                                  |
|   • Secrets (säker credential-hantering)                         |
|   • Triggers (när pipeline körs)                                 |
|                                                                  |
+------------------------------------------------------------------+
```

### Terminology Mapping

| Koncept | GitHub Actions | CircleCI | GitLab CI | Bitbucket |
|---------|---------------|----------|-----------|-----------|
| Pipeline file | workflow.yml | config.yml | .gitlab-ci.yml | pipelines.yml |
| Job collection | workflow | workflow | pipeline | pipeline |
| Executable unit | job | job | job | step |
| Command | step | step | script | script |
| Reusable code | action | orb | include | pipe |
| Secret group | environment | context | group | deployment |
| Parallel builds | matrix | parallelism | parallel | parallel |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: CircleCI Setup och Konfiguration

```yaml
# .circleci/config.yml
version: 2.1

# Orbs - återanvändbara paket (som GitHub Actions)
orbs:
  node: circleci/node@5.2
  aws-cli: circleci/aws-cli@4.1
  slack: circleci/slack@4.12

# Executors - definierar körmiljön
executors:
  node-executor:
    docker:
      - image: cimg/node:20.10
    working_directory: ~/project
    resource_class: medium
    environment:
      NODE_ENV: test

  node-with-db:
    docker:
      - image: cimg/node:20.10
      - image: cimg/postgres:15.0
        environment:
          POSTGRES_USER: test
          POSTGRES_DB: testdb
          POSTGRES_PASSWORD: test

# Commands - återanvändbara steg
commands:
  setup-dependencies:
    description: "Install and cache dependencies"
    steps:
      - checkout
      - restore_cache:
          keys:
            - deps-v1-{{ checksum "package-lock.json" }}
            - deps-v1-
      - run:
          name: Install dependencies
          command: npm ci
      - save_cache:
          key: deps-v1-{{ checksum "package-lock.json" }}
          paths:
            - node_modules

  notify-slack:
    description: "Send Slack notification"
    parameters:
      status:
        type: string
    steps:
      - slack/notify:
          event: << parameters.status >>
          template: basic_success_1

# Jobs
jobs:
  build:
    executor: node-executor
    steps:
      - setup-dependencies
      - run:
          name: Build application
          command: npm run build
      - persist_to_workspace:
          root: .
          paths:
            - dist
            - node_modules

  test:
    executor: node-with-db
    parallelism: 4  # Kör 4 parallella containers
    steps:
      - setup-dependencies
      - attach_workspace:
          at: .
      - run:
          name: Wait for database
          command: dockerize -wait tcp://localhost:5432 -timeout 60s
      - run:
          name: Run tests (split)
          command: |
            # Dela upp tester över parallella containers
            TESTS=$(circleci tests glob "**/*.test.ts" | circleci tests split --split-by=timings)
            npm test -- $TESTS
      - store_test_results:
          path: test-results
      - store_artifacts:
          path: coverage

  lint:
    executor: node-executor
    steps:
      - setup-dependencies
      - run:
          name: Run linting
          command: npm run lint -- --format junit -o lint-results.xml
      - store_test_results:
          path: lint-results.xml

  security-scan:
    executor: node-executor
    steps:
      - setup-dependencies
      - run:
          name: Security audit
          command: npm audit --audit-level=high

  deploy-staging:
    executor: node-executor
    steps:
      - attach_workspace:
          at: .
      - aws-cli/setup
      - run:
          name: Deploy to staging
          command: |
            aws s3 sync dist/ s3://staging-bucket/ --delete
            aws cloudfront create-invalidation \
              --distribution-id $STAGING_CF_ID \
              --paths "/*"
      - notify-slack:
          status: pass

  deploy-production:
    executor: node-executor
    steps:
      - attach_workspace:
          at: .
      - aws-cli/setup
      - run:
          name: Deploy to production
          command: |
            aws s3 sync dist/ s3://production-bucket/ --delete
            aws cloudfront create-invalidation \
              --distribution-id $PRODUCTION_CF_ID \
              --paths "/*"
      - notify-slack:
          status: pass

# Workflows - orkestrering
workflows:
  version: 2
  build-test-deploy:
    jobs:
      - build
      - lint:
          requires:
            - build
      - test:
          requires:
            - build
      - security-scan:
          requires:
            - build
      - deploy-staging:
          requires:
            - lint
            - test
            - security-scan
          filters:
            branches:
              only: develop
          context: staging-aws
      - hold-for-production:
          type: approval
          requires:
            - lint
            - test
            - security-scan
          filters:
            branches:
              only: main
      - deploy-production:
          requires:
            - hold-for-production
          context: production-aws

  # Nightly security scan
  nightly:
    triggers:
      - schedule:
          cron: "0 2 * * *"
          filters:
            branches:
              only: main
    jobs:
      - security-scan
```

### Steg 2: GitLab CI Konfiguration

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - security
  - deploy

# Global settings
default:
  image: node:20-alpine
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
      - .npm/

variables:
  npm_config_cache: "$CI_PROJECT_DIR/.npm"
  FF_USE_FASTZIP: "true"

# Templates
.node-setup:
  before_script:
    - npm ci --cache .npm --prefer-offline

.deploy-template:
  image: amazon/aws-cli:latest
  before_script:
    - aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
    - aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
    - aws configure set region eu-west-1

# Jobs
build:
  stage: build
  extends: .node-setup
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

lint:
  stage: test
  extends: .node-setup
  script:
    - npm run lint
  allow_failure: true

test:unit:
  stage: test
  extends: .node-setup
  services:
    - postgres:15
  variables:
    POSTGRES_DB: test
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: "postgresql://test:test@postgres:5432/test"
  script:
    - npm test -- --coverage
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

test:e2e:
  stage: test
  extends: .node-setup
  image: mcr.microsoft.com/playwright:latest
  script:
    - npm run test:e2e
  artifacts:
    when: always
    paths:
      - playwright-report/
    expire_in: 7 days
  parallel: 3  # Kör 3 parallella instanser

sast:
  stage: security
  # GitLab built-in SAST
  include:
    - template: Security/SAST.gitlab-ci.yml

dependency_scanning:
  stage: security
  extends: .node-setup
  script:
    - npm audit --audit-level=high
  allow_failure: true

deploy:staging:
  stage: deploy
  extends: .deploy-template
  script:
    - aws s3 sync dist/ s3://$STAGING_BUCKET/ --delete
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

deploy:production:
  stage: deploy
  extends: .deploy-template
  script:
    - aws s3 sync dist/ s3://$PRODUCTION_BUCKET/ --delete
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
  needs:
    - test:unit
    - test:e2e
    - sast
```

### Steg 3: Bitbucket Pipelines

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
    redis:
      image: redis:7-alpine

  steps:
    - step: &install
        name: Install Dependencies
        caches:
          - npm
        script:
          - npm ci
        artifacts:
          - node_modules/**

    - step: &build
        name: Build
        caches:
          - npm
        script:
          - npm run build
        artifacts:
          - dist/**

    - step: &test
        name: Run Tests
        caches:
          - npm
        services:
          - postgres
          - redis
        script:
          - npm test

    - step: &lint
        name: Lint
        caches:
          - npm
        script:
          - npm run lint

    - step: &security
        name: Security Scan
        script:
          - npm audit --audit-level=high

    - step: &deploy-staging
        name: Deploy to Staging
        deployment: staging
        script:
          - pipe: atlassian/aws-s3-deploy:1.1.0
            variables:
              AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
              AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
              AWS_DEFAULT_REGION: eu-west-1
              S3_BUCKET: $STAGING_BUCKET
              LOCAL_PATH: dist

    - step: &deploy-production
        name: Deploy to Production
        deployment: production
        trigger: manual
        script:
          - pipe: atlassian/aws-s3-deploy:1.1.0
            variables:
              AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
              AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
              AWS_DEFAULT_REGION: eu-west-1
              S3_BUCKET: $PRODUCTION_BUCKET
              LOCAL_PATH: dist

pipelines:
  default:
    - step: *install
    - parallel:
        - step: *build
        - step: *lint
        - step: *security
    - step: *test

  branches:
    develop:
      - step: *install
      - parallel:
          - step: *build
          - step: *test
      - step: *deploy-staging

    main:
      - step: *install
      - parallel:
          - step: *build
          - step: *test
          - step: *security
      - step: *deploy-staging
      - step: *deploy-production

  pull-requests:
    '**':
      - step: *install
      - parallel:
          - step: *lint
          - step: *test

  custom:
    security-audit:
      - step:
          name: Full Security Audit
          script:
            - npm ci
            - npm audit
            - npx snyk test
```

### Steg 4: Buildkite Pipeline

```yaml
# .buildkite/pipeline.yml
steps:
  # Build step
  - label: ":npm: Install & Build"
    command:
      - npm ci
      - npm run build
    key: build
    plugins:
      - docker#v5.10.0:
          image: node:20
          volumes:
            - "./:/app"
          workdir: /app
    artifact_paths:
      - "dist/**/*"

  # Parallel test steps
  - label: ":jest: Unit Tests"
    command: npm test
    key: test
    depends_on: build
    parallelism: 4
    plugins:
      - docker#v5.10.0:
          image: node:20
      - test-collector#v1.10.0:
          files: "junit.xml"

  - label: ":eslint: Lint"
    command: npm run lint
    key: lint
    depends_on: build
    plugins:
      - docker#v5.10.0:
          image: node:20

  - label: ":lock: Security Scan"
    command: npm audit --audit-level=high
    key: security
    depends_on: build
    plugins:
      - docker#v5.10.0:
          image: node:20
    soft_fail: true

  # Wait for all tests
  - wait: ~
    key: test-complete

  # Deploy staging
  - label: ":rocket: Deploy Staging"
    command: ./scripts/deploy.sh staging
    key: deploy-staging
    depends_on: test-complete
    branches: develop
    agents:
      queue: deploy
    plugins:
      - aws-assume-role-with-web-identity#v1.0.0:
          role-arn: arn:aws:iam::123456789:role/deploy-role

  # Production approval
  - block: ":hand: Approve Production Deploy"
    key: approve-production
    depends_on: test-complete
    branches: main
    fields:
      - text: "Deploy Reason"
        key: deploy-reason
        required: true

  # Deploy production
  - label: ":rocket: Deploy Production"
    command: ./scripts/deploy.sh production
    key: deploy-production
    depends_on: approve-production
    branches: main
    agents:
      queue: deploy
    concurrency: 1
    concurrency_group: production-deploy
    plugins:
      - aws-assume-role-with-web-identity#v1.0.0:
          role-arn: arn:aws:iam::123456789:role/deploy-role

  # Notify on completion
  - label: ":slack: Notify"
    command: ./scripts/notify-slack.sh
    depends_on:
      - deploy-staging
      - deploy-production
    allow_dependency_failure: true
    plugins:
      - slack-notify#v1.0.0:
          webhook_url: $SLACK_WEBHOOK
```

```yaml
# Buildkite med dynamisk pipeline
# .buildkite/pipeline.yml
steps:
  - label: ":pipeline: Generate Pipeline"
    command: .buildkite/generate-pipeline.sh | buildkite-agent pipeline upload
```

```bash
#!/bin/bash
# .buildkite/generate-pipeline.sh

cat <<YAML
steps:
YAML

# Generera test steps baserat på ändrade filer
CHANGED_FILES=$(git diff --name-only HEAD~1)

if echo "$CHANGED_FILES" | grep -q "^frontend/"; then
  cat <<YAML
  - label: ":react: Frontend Tests"
    command: cd frontend && npm test
YAML
fi

if echo "$CHANGED_FILES" | grep -q "^backend/"; then
  cat <<YAML
  - label: ":python: Backend Tests"
    command: cd backend && pytest
YAML
fi
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Migration från GitHub Actions till CircleCI

```yaml
# FÖRE: GitHub Actions
# .github/workflows/ci.yml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test
      - run: npm run build

# EFTER: CircleCI
# .circleci/config.yml
version: 2.1
orbs:
  node: circleci/node@5.2
jobs:
  build:
    docker:
      - image: cimg/node:20.10
    steps:
      - checkout
      - node/install-packages
      - run: npm test
      - run: npm run build
workflows:
  main:
    jobs:
      - build
```

### Exempel 2: Multi-Platform CI Matrix

```yaml
# GitLab CI med multi-platform matrix
# .gitlab-ci.yml
stages:
  - test

.test-template:
  stage: test
  script:
    - npm ci
    - npm test

test:node18:
  extends: .test-template
  image: node:18

test:node20:
  extends: .test-template
  image: node:20

test:node21:
  extends: .test-template
  image: node:21
  allow_failure: true  # Experimentell

# CircleCI motsvarande
# .circleci/config.yml
version: 2.1
jobs:
  test:
    parameters:
      node-version:
        type: string
    docker:
      - image: cimg/node:<< parameters.node-version >>
    steps:
      - checkout
      - run: npm ci
      - run: npm test

workflows:
  test-matrix:
    jobs:
      - test:
          matrix:
            parameters:
              node-version: ["18.19", "20.10", "21.5"]
```

### Exempel 3: Cross-Platform Pipeline Converter Script

```python
#!/usr/bin/env python3
# scripts/convert-pipeline.py
# Convert GitHub Actions to other CI platforms.

import yaml
import sys
from pathlib import Path

def github_to_circleci(github_config: dict) -> dict:
    # Convert GitHub Actions workflow to CircleCI config.
    circleci = {
        "version": 2.1,
        "jobs": {},
        "workflows": {"main": {"jobs": []}}
    }

    for job_name, job_config in github_config.get("jobs", {}).items():
        circleci_job = {
            "docker": [{"image": "cimg/base:stable"}],
            "steps": ["checkout"]
        }

        # Convert steps
        for step in job_config.get("steps", []):
            if isinstance(step, dict):
                if "run" in step:
                    circleci_job["steps"].append({
                        "run": {
                            "name": step.get("name", "Run command"),
                            "command": step["run"]
                        }
                    })
                elif "uses" in step:
                    # Map common actions
                    if "checkout" in step["uses"]:
                        continue  # Already added
                    elif "setup-node" in step["uses"]:
                        circleci_job["docker"] = [{"image": "cimg/node:20.10"}]
            elif isinstance(step, str):
                circleci_job["steps"].append({"run": step})

        circleci["jobs"][job_name] = circleci_job
        circleci["workflows"]["main"]["jobs"].append(job_name)

    return circleci

def github_to_gitlab(github_config: dict) -> dict:
    # Convert GitHub Actions workflow to GitLab CI config.
    gitlab = {
        "stages": [],
        "default": {"image": "node:20"}
    }

    for job_name, job_config in github_config.get("jobs", {}).items():
        stage = job_config.get("needs", ["build"])[0] if job_config.get("needs") else "build"
        if stage not in gitlab["stages"]:
            gitlab["stages"].append(stage)

        gitlab_job = {
            "stage": stage,
            "script": []
        }

        for step in job_config.get("steps", []):
            if isinstance(step, dict) and "run" in step:
                gitlab_job["script"].append(step["run"])

        gitlab[job_name] = gitlab_job

    return gitlab

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: convert-pipeline.py <github-workflow.yml> <target: circleci|gitlab>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        github = yaml.safe_load(f)

    target = sys.argv[2]
    if target == "circleci":
        result = github_to_circleci(github)
        output_path = ".circleci/config.yml"
    elif target == "gitlab":
        result = github_to_gitlab(github)
        output_path = ".gitlab-ci.yml"
    else:
        print(f"Unknown target: {target}")
        sys.exit(1)

    Path(output_path).parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        yaml.dump(result, f, default_flow_style=False)

    print(f"Converted to {output_path}")
```

------------------------------------------------------------

## Bästa Praxis

### 1. Använd Plattformsspecifika Features

```yaml
# CircleCI - Utnyttja Orbs för återanvändbarhet
version: 2.1
orbs:
  # Officiella orbs
  aws-cli: circleci/aws-cli@4.1
  kubernetes: circleci/kubernetes@1.3
  slack: circleci/slack@4.12

  # Custom orb (publicerad)
  mycompany: mycompany/common@1.0

jobs:
  deploy:
    executor: mycompany/node-executor
    steps:
      - mycompany/setup-credentials
      - kubernetes/install-kubectl
      - aws-cli/setup
      - run: kubectl apply -f k8s/
```

### 2. Strukturera Config för Läsbarhet

```yaml
# GitLab CI - Använd includes och extends
# .gitlab-ci.yml
include:
  - local: .gitlab/ci/test.yml
  - local: .gitlab/ci/deploy.yml
  - template: Security/SAST.gitlab-ci.yml

# .gitlab/ci/test.yml
.test-defaults:
  stage: test
  before_script:
    - npm ci
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

unit-tests:
  extends: .test-defaults
  script:
    - npm test

integration-tests:
  extends: .test-defaults
  services:
    - postgres:15
  script:
    - npm run test:integration
```

### 3. Hantera Secrets Konsekvent

```yaml
# CircleCI - Använd Contexts för miljöspecifika secrets
workflows:
  deploy:
    jobs:
      - deploy:
          context:
            - aws-credentials      # Org-wide
            - production-secrets   # Environment-specific

# Bitbucket - Använd deployment variables
pipelines:
  branches:
    main:
      - step:
          deployment: production   # Ger tillgång till production-specifika variabler
          script:
            - echo $PRODUCTION_API_KEY
```

### 4. Optimera Build Times

```yaml
# CircleCI - Parallelism och caching
jobs:
  test:
    parallelism: 4
    steps:
      - checkout
      - restore_cache:
          keys:
            - deps-{{ checksum "package-lock.json" }}
            - deps-
      - run: npm ci
      - save_cache:
          key: deps-{{ checksum "package-lock.json" }}
          paths:
            - node_modules
      - run: |
          TESTS=$(circleci tests glob "**/*.test.ts" | circleci tests split --split-by=timings)
          npm test -- $TESTS
      - store_test_results:
          path: test-results  # Används för timing-baserad split
```

------------------------------------------------------------

## Vanliga Fallgropar

### ❌ Fallgrop 1: Ignorera Plattformsskillnader

```yaml
# Problem: Samma YAML fungerar inte överallt
# GitHub Actions
- run: echo ${{ github.sha }}

# CircleCI - Använd CIRCLE_SHA1
- run: echo $CIRCLE_SHA1

# GitLab CI - Använd CI_COMMIT_SHA
script:
  - echo $CI_COMMIT_SHA

# Bitbucket - Använd BITBUCKET_COMMIT
script:
  - echo $BITBUCKET_COMMIT

# ✅ Lösning: Abstrahera med environment variables
# scripts/ci-env.sh
export COMMIT_SHA=${GITHUB_SHA:-${CIRCLE_SHA1:-${CI_COMMIT_SHA:-${BITBUCKET_COMMIT}}}}
export BRANCH=${GITHUB_REF_NAME:-${CIRCLE_BRANCH:-${CI_COMMIT_REF_NAME:-${BITBUCKET_BRANCH}}}}
```

### ❌ Fallgrop 2: Dålig Cache-strategi

```yaml
# Problem: Cache-nyckel för bred
# ❌ DÅLIGT
cache:
  key: deps-v1  # Invalideras aldrig automatiskt
  paths:
    - node_modules/

# ✅ BRA
cache:
  key: deps-{{ checksum "package-lock.json" }}
  paths:
    - node_modules/

# Ännu bättre - fallback keys
cache:
  keys:
    - deps-{{ .Branch }}-{{ checksum "package-lock.json" }}
    - deps-{{ .Branch }}-
    - deps-
```

### ❌ Fallgrop 3: Hårdkodade Timeout-värden

```yaml
# Problem: Timeout som fungerar på en plattform men inte en annan

# CircleCI - Längre default timeouts
jobs:
  long-test:
    docker:
      - image: cimg/node:20
    steps:
      - run:
          name: Long running test
          command: npm run test:e2e
          no_output_timeout: 30m  # CircleCI-specifik

# GitLab CI
long-test:
  timeout: 2 hours  # GitLab-specifik
  script:
    - npm run test:e2e

# ✅ Lösning: Dokumentera och justera för varje plattform
```

### ❌ Fallgrop 4: Ej Testa Pipeline-ändringar

```yaml
# Problem: Push:a pipeline-ändringar direkt till main

# ✅ Lösning: Testa i branch först
# CircleCI - setup workflow för config validation
setup: true
workflows:
  validate:
    jobs:
      - validate-config:
          filters:
            branches:
              only: /^feature\/.*/

# GitLab - Validera innan merge
validate-ci:
  stage: .pre
  script:
    - gitlab-ci-lint .gitlab-ci.yml
  only:
    changes:
      - .gitlab-ci.yml
```

------------------------------------------------------------

## Övningar

### Övning 1: Migrera GitHub Actions till CircleCI (20 XP)

**Mål:** Konvertera en GitHub Actions workflow till CircleCI-format.

**Din uppgift:**
1. Ta denna GitHub Actions workflow:
```yaml
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm test
```
2. Konvertera till CircleCI-format
3. Lägg till caching
4. Lägg till parallelism för tester

<details>
<summary>Ledtråd</summary>

CircleCI använder `docker` istället för `runs-on`, och `checkout` är ett inbyggt step. Orbs ersätter actions.

</details>

<details>
<summary>Lösning</summary>

```yaml
version: 2.1

orbs:
  node: circleci/node@5.2

jobs:
  test:
    docker:
      - image: cimg/node:20.10
    parallelism: 4
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
      - run:
          name: Run tests
          command: |
            TESTS=$(circleci tests glob "**/*.test.js" | circleci tests split)
            npm test -- $TESTS

workflows:
  main:
    jobs:
      - test
```

</details>

---

### Övning 2: Multi-Platform Build Matrix (25 XP)

**Mål:** Skapa en pipeline som bygger på flera plattformar samtidigt.

**Din uppgift:**
1. Skapa en GitLab CI pipeline
2. Bygg på Node 18, 20 och 21
3. Testa på både Linux och Alpine-baserade images
4. Samla coverage från alla varianter
5. Fail-fast om en kritisk variant misslyckas

<details>
<summary>Ledtråd</summary>

Använd GitLab CI:s `parallel:matrix` eller skapa separata jobs som extends en template.

</details>

<details>
<summary>Lösning</summary>

```yaml
stages:
  - test
  - report

.test-template:
  stage: test
  script:
    - npm ci
    - npm test -- --coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

test:
  extends: .test-template
  parallel:
    matrix:
      - NODE_VERSION: ["18", "20"]
        BASE_IMAGE: ["node", "node-alpine"]
  image: "${BASE_IMAGE}:${NODE_VERSION}"
  rules:
    - if: $NODE_VERSION == "20"
      allow_failure: false  # Kritisk version
    - allow_failure: true   # Övriga kan faila

test:node21:
  extends: .test-template
  image: node:21
  allow_failure: true  # Experimentell

coverage-report:
  stage: report
  image: node:20
  script:
    - npx nyc merge coverage/ .nyc_output/merged.json
    - npx nyc report --reporter=text
  needs:
    - test
```

</details>

---

### Övning 3: Cross-Platform Secret Sync (35 XP)

**Mål:** Implementera script som synkar secrets mellan CI-plattformar.

**Din uppgift:**
1. Skapa ett script som läser secrets från GitHub
2. Synka till CircleCI contexts
3. Synka till GitLab CI variables
4. Implementera dry-run mode
5. Lägg till audit logging

<details>
<summary>Ledtråd</summary>

Använd respektive plattforms API: GitHub REST API, CircleCI v2 API, GitLab REST API. Secrets kan inte läsas ut - synka baserat på secret names/metadata.

</details>

<details>
<summary>Lösning</summary>

```bash
#!/bin/bash
# scripts/sync-secrets.sh

set -euo pipefail

DRY_RUN=${DRY_RUN:-false}
LOG_FILE="secret-sync-$(date +%Y%m%d).log"

log() {
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $1" | tee -a "$LOG_FILE"
}

# Hämta GitHub secrets metadata (inte värden)
get_github_secrets() {
  gh api repos/$GITHUB_REPO/actions/secrets \
    --jq '.secrets[].name'
}

# Synka till CircleCI
sync_to_circleci() {
  local secret_name=$1
  local secret_value=$2

  if [ "$DRY_RUN" = "true" ]; then
    log "[DRY-RUN] Would sync $secret_name to CircleCI"
    return
  fi

  curl -s -X POST "https://circleci.com/api/v2/context/$CIRCLECI_CONTEXT_ID/environment-variable" \
    -H "Circle-Token: $CIRCLECI_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"$secret_name\",\"value\":\"$secret_value\"}"

  log "Synced $secret_name to CircleCI"
}

# Synka till GitLab
sync_to_gitlab() {
  local secret_name=$1
  local secret_value=$2

  if [ "$DRY_RUN" = "true" ]; then
    log "[DRY-RUN] Would sync $secret_name to GitLab"
    return
  fi

  curl -s -X POST "https://gitlab.com/api/v4/projects/$GITLAB_PROJECT_ID/variables" \
    -H "PRIVATE-TOKEN: $GITLAB_TOKEN" \
    -F "key=$secret_name" \
    -F "value=$secret_value" \
    -F "protected=true" \
    -F "masked=true" || \
  curl -s -X PUT "https://gitlab.com/api/v4/projects/$GITLAB_PROJECT_ID/variables/$secret_name" \
    -H "PRIVATE-TOKEN: $GITLAB_TOKEN" \
    -F "value=$secret_value"

  log "Synced $secret_name to GitLab"
}

# Main
log "Starting secret sync"
log "Dry run: $DRY_RUN"

# Läs från 1Password/Vault istället för GitHub
# (secrets kan inte läsas ut från GitHub)
for secret in $(cat .secrets-to-sync); do
  VALUE=$(op read "op://CI-CD/$secret")
  sync_to_circleci "$secret" "$VALUE"
  sync_to_gitlab "$secret" "$VALUE"
done

log "Secret sync completed"
```

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **GitHub Actions Fundamentals:** Grunderna som tillämpas på andra plattformar
- **Self-Hosted Runners:** Bygga egen CI-infrastruktur
- **Enterprise CI/CD Patterns:** Avancerade mönster för stora organisationer
- **Secrets Management:** Hantera credentials över plattformar

### Förkunskaper:
- GitHub Actions grunderna
- Docker och containers
- YAML-syntax
- Basic scripting (Bash)

### Bygger mot:
- Multi-platform CI/CD-strategi
- Platform-agnostic DevOps
- CI/CD konsultation och migrering
- Enterprise CI/CD arkitektur

------------------------------------------------------------

## Sammanfattning

- **CircleCI** excellerar i Docker-native builds och snabb parallelism
- **GitLab CI** erbjuder all-in-one DevOps med inbyggd security scanning
- **Bitbucket Pipelines** integrerar sömlöst med Jira och Confluence
- **Buildkite** ger maximal kontroll med hybrid self-hosted/cloud
- **Travis CI** är enkel att komma igång med för open source
- Alla plattformar delar samma grundläggande koncept: jobs, steps, artifacts, caching
- **Orbs** (CircleCI), **includes** (GitLab), **pipes** (Bitbucket) motsvarar GitHub Actions
- Välj plattform baserat på ekosystem, inte bara features
- Dokumentera plattformsskillnader vid migration
- Testa pipeline-ändringar i feature branches

------------------------------------------------------------

## Nyckelkommandon

| Plattform | Validate Config | Trigger Build | View Status |
|-----------|-----------------|---------------|-------------|
| CircleCI | `circleci config validate` | `circleci workflow rerun` | `circleci workflow list` |
| GitLab | `gitlab-ci-lint` | `gitlab-runner exec` | `glab ci status` |
| Bitbucket | N/A | `bb pipeline run` | `bb pipeline list` |
| Buildkite | `buildkite-agent pipeline upload --dry-run` | `bk build create` | `bk build list` |

| CircleCI CLI | Beskrivning |
|--------------|-------------|
| `circleci setup` | Konfigurera CLI med token |
| `circleci config validate` | Validera config.yml |
| `circleci local execute` | Kör job lokalt |
| `circleci tests split` | Dela tester för parallelism |

------------------------------------------------------------

## Referenser

- CircleCI Documentation: https://circleci.com/docs/
- CircleCI Orbs Registry: https://circleci.com/developer/orbs
- GitLab CI/CD Documentation: https://docs.gitlab.com/ee/ci/
- Bitbucket Pipelines: https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/
- Buildkite Documentation: https://buildkite.com/docs
- Travis CI Documentation: https://docs.travis-ci.com/
- Azure Pipelines: https://docs.microsoft.com/en-us/azure/devops/pipelines/
- CI/CD Platform Comparison: https://www.g2.com/categories/continuous-integration
""",
        },
        {
            "order_index": 18,
            "title": "Self-Hosted Runners",
            "slug": "self-hosted-runners",
            "difficulty": "advanced",
            "content": """# Self-Hosted Runners

Self-hosted runners ger dig full kontroll över din CI/CD-infrastruktur. De är essentiella när du behöver specialhårdvara som GPU:er, ARM-processorer, eller måste köra builds inom ditt privata nätverk för compliance-krav. Denna modul lär dig att designa, implementera och underhålla en robust self-hosted runner-infrastruktur.

------------------------------------------------------------

## Introduktion

### Varför Self-Hosted Runners?

Cloud-baserade runners från GitHub, GitLab och andra är bekväma men har begränsningar:

**När du behöver self-hosted:**
- **Specialhårdvara:** GPU:er för ML/AI-träning, ARM för embedded
- **Compliance:** Data måste stanna inom ditt nätverk (HIPAA, PCI-DSS)
- **Prestanda:** Dedikerade resurser för snabbare builds
- **Kostnad:** Hög volym gör egna runners billigare
- **Nätverksåtkomst:** Interna system, databaser, on-prem resurser

### Vad du kommer lära dig

Efter denna modul kommer du kunna:
- Sätta upp self-hosted runners för GitHub Actions, GitLab CI och andra plattformar
- Implementera autoskalning med Kubernetes och Actions Runner Controller (ARC)
- Konfigurera säkerhetshärdning för runners
- Bygga ephemeral runners för maximal säkerhet
- Övervaka och felsöka runner-infrastruktur

### Förkunskaper

- Grundläggande Linux-administration
- Docker och Kubernetes-kunskap
- Förståelse för CI/CD-koncept
- Grundläggande nätverkssäkerhet

------------------------------------------------------------

## Teori

### Runner-arkitektur

```
+------------------------------------------------------------------+
|                    SELF-HOSTED RUNNER ARKITEKTUR                 |
+------------------------------------------------------------------+
|                                                                  |
|    CI/CD Platform                                                |
|    (GitHub/GitLab)                                               |
|          │                                                       |
|          │ Jobs                                                  |
|          ▼                                                       |
|    ┌─────────────────────────────────────────────────────────┐   |
|    │                   RUNNER POOL                           │   |
|    │                                                         │   |
|    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │   |
|    │  │ Runner  │  │ Runner  │  │ Runner  │  │ Runner  │    │   |
|    │  │  (GPU)  │  │ (Linux) │  │ (macOS) │  │  (ARM)  │    │   |
|    │  │         │  │         │  │         │  │         │    │   |
|    │  │ Label:  │  │ Label:  │  │ Label:  │  │ Label:  │    │   |
|    │  │ gpu     │  │ linux   │  │ macos   │  │ arm64   │    │   |
|    │  │ cuda-12 │  │ x64     │  │ m1      │  │ linux   │    │   |
|    │  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │   |
|    │                                                         │   |
|    └─────────────────────────────────────────────────────────┘   |
|                                                                  |
+------------------------------------------------------------------+
```

### Runner-typer

| Typ | Beskrivning | Use Case | Säkerhet |
|-----|-------------|----------|----------|
| **Persistent** | Alltid igång, tar flera jobs | Dev/Test | Lägre |
| **Ephemeral** | Ny instans per job | Production | Högre |
| **Autoscaled** | Skalas baserat på behov | Varierande load | Flexibel |
| **Containerized** | Kör i Docker/K8s | Isolering | Hög |

### Säkerhetsmodell

```
+------------------------------------------------------------------+
|               RUNNER SÄKERHETSMODELL                             |
+------------------------------------------------------------------+
|                                                                  |
|   TRUST BOUNDARY                                                 |
|   │                                                              |
|   │  ┌──────────────────────────────────────────────────────┐    |
|   │  │                PUBLIC CODE                            │    |
|   │  │  (Pull requests, forks, public repos)                 │    |
|   │  │                                                       │    |
|   │  │  ⚠️ RISK: Kan köra godtycklig kod                     │    |
|   │  │  ✅ LÖSNING: Ephemeral runners, sandboxing            │    |
|   │  └──────────────────────────────────────────────────────┘    |
|   │                                                              |
|   │  ┌──────────────────────────────────────────────────────┐    |
|   │  │                PRIVATE CODE                           │    |
|   │  │  (Trusted maintainers, organization repos)            │    |
|   │  │                                                       │    |
|   │  │  ⚠️ RISK: Supply chain attacks                        │    |
|   │  │  ✅ LÖSNING: Pinned actions, dependency scanning      │    |
|   │  └──────────────────────────────────────────────────────┘    |
|   │                                                              |
+------------------------------------------------------------------+
```

### Skalningsstrategier

| Strategi | Trigger | Fördel | Nackdel |
|----------|---------|--------|---------|
| **Queue-based** | Antal väntande jobs | Responsiv | Kan överprovisiona |
| **Schedule-based** | Tid på dygnet | Förutsägbar | Kan missa toppar |
| **Metric-based** | CPU/Memory usage | Effektiv | Komplexare setup |
| **Hybrid** | Kombination | Optimal | Svårare att underhålla |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: GitHub Actions Self-Hosted Runner

```bash
#!/bin/bash
# scripts/setup-github-runner.sh

set -euo pipefail

# Variabler
RUNNER_VERSION="2.311.0"
RUNNER_USER="runner"
RUNNER_HOME="/home/${RUNNER_USER}/actions-runner"
GITHUB_URL="${GITHUB_URL:-https://github.com/myorg}"
RUNNER_TOKEN="${RUNNER_TOKEN}"
RUNNER_NAME="${RUNNER_NAME:-$(hostname)}"
RUNNER_LABELS="${RUNNER_LABELS:-self-hosted,linux,x64}"

# Skapa användare
sudo useradd -m -s /bin/bash ${RUNNER_USER} || true

# Installera beroenden
sudo apt-get update
sudo apt-get install -y curl jq docker.io
sudo usermod -aG docker ${RUNNER_USER}

# Ladda ner runner
sudo -u ${RUNNER_USER} mkdir -p ${RUNNER_HOME}
cd ${RUNNER_HOME}

sudo -u ${RUNNER_USER} curl -o actions-runner.tar.gz -L \
  "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz"
sudo -u ${RUNNER_USER} tar xzf actions-runner.tar.gz
rm actions-runner.tar.gz

# Konfigurera runner
sudo -u ${RUNNER_USER} ./config.sh \
  --url "${GITHUB_URL}" \
  --token "${RUNNER_TOKEN}" \
  --name "${RUNNER_NAME}" \
  --labels "${RUNNER_LABELS}" \
  --work "_work" \
  --unattended \
  --replace

# Installera som systemd service
sudo ./svc.sh install ${RUNNER_USER}
sudo ./svc.sh start

echo "✅ GitHub Actions runner installed and started"
```

```yaml
# Använd self-hosted runner i workflow
# .github/workflows/build.yml
name: Build on Self-Hosted

on: [push]

jobs:
  build:
    runs-on: [self-hosted, linux, x64]
    steps:
      - uses: actions/checkout@v4

      - name: Build application
        run: |
          npm ci
          npm run build

      - name: Run tests
        run: npm test

  # GPU-specifikt job
  train-model:
    runs-on: [self-hosted, linux, gpu, cuda-12]
    steps:
      - uses: actions/checkout@v4

      - name: Verify GPU
        run: nvidia-smi

      - name: Train model
        run: python train.py --epochs 100
```

### Steg 2: Kubernetes Actions Runner Controller (ARC)

```bash
#!/bin/bash
# scripts/install-arc.sh

# Installera cert-manager (krävs av ARC)
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml
kubectl wait --for=condition=ready pod -l app=cert-manager -n cert-manager --timeout=120s

# Installera ARC via Helm
helm repo add actions-runner-controller \
  https://actions-runner-controller.github.io/actions-runner-controller

helm install arc actions-runner-controller/actions-runner-controller \
  --namespace arc-system \
  --create-namespace \
  --set authSecret.create=true \
  --set authSecret.github_token="${GITHUB_PAT}" \
  --set image.actionsRunnerRepositoryAndTag=summerwind/actions-runner:latest \
  --wait

echo "✅ Actions Runner Controller installed"
```

```yaml
# kubernetes/runners/deployment.yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: github-runners
  namespace: arc-runners
spec:
  replicas: 3
  template:
    spec:
      repository: myorg/myrepo
      # Eller organisation-wide:
      # organization: myorg

      labels:
        - kubernetes
        - linux
        - x64

      # Runner konfiguration
      env:
        - name: DOCKER_HOST
          value: tcp://localhost:2376
        - name: DOCKER_TLS_CERTDIR
          value: /certs

      # Docker-in-Docker sidecar
      dockerdWithinRunnerContainer: true

      # Resursbegränsningar
      resources:
        limits:
          cpu: "4"
          memory: "8Gi"
        requests:
          cpu: "1"
          memory: "2Gi"

      # Säkerhet
      securityContext:
        fsGroup: 1000

      # Volumes för caching
      volumeMounts:
        - name: work
          mountPath: /runner/_work
      volumes:
        - name: work
          emptyDir: {}

---
# Autoscaling baserat på job queue
apiVersion: actions.summerwind.dev/v1alpha1
kind: HorizontalRunnerAutoscaler
metadata:
  name: github-runners-autoscaler
  namespace: arc-runners
spec:
  scaleTargetRef:
    kind: RunnerDeployment
    name: github-runners

  minReplicas: 1
  maxReplicas: 20

  scaleUpTriggers:
    - githubEvent:
        workflowJob: {}
      amount: 1
      duration: "5m"

  scaleDownDelaySecondsAfterScaleOut: 300

  metrics:
    - type: TotalNumberOfQueuedAndInProgressWorkflowRuns
      repositoryNames:
        - myorg/myrepo
```

### Steg 3: Ephemeral Runners för Säkerhet

```yaml
# kubernetes/runners/ephemeral.yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: ephemeral-runners
  namespace: arc-runners
spec:
  replicas: 0  # Autoscaler hanterar
  template:
    spec:
      organization: myorg

      # KRITISKT: Ephemeral mode
      ephemeral: true

      labels:
        - ephemeral
        - linux
        - secure

      # Minimal image
      image: summerwind/actions-runner:latest

      # Strikt säkerhet
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        readOnlyRootFilesystem: false  # Runner behöver skriva
        allowPrivilegeEscalation: false

      # Resursbegränsningar
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"
          ephemeral-storage: "10Gi"
        requests:
          cpu: "500m"
          memory: "1Gi"

      # Ingen persistent storage
      volumeMounts:
        - name: work
          mountPath: /runner/_work
      volumes:
        - name: work
          emptyDir:
            sizeLimit: "10Gi"

---
# Autoscaler för ephemeral runners
apiVersion: actions.summerwind.dev/v1alpha1
kind: HorizontalRunnerAutoscaler
metadata:
  name: ephemeral-autoscaler
  namespace: arc-runners
spec:
  scaleTargetRef:
    kind: RunnerDeployment
    name: ephemeral-runners

  minReplicas: 0   # Skala till noll när idle
  maxReplicas: 50  # Hantera spikes

  scaleUpTriggers:
    - githubEvent:
        workflowJob: {}
      amount: 1
      duration: "2m"  # Snabb nedtrappning

  scaleDownDelaySecondsAfterScaleOut: 60
```

### Steg 4: GitLab Runner med Kubernetes Executor

```bash
#!/bin/bash
# scripts/install-gitlab-runner.sh

# Installera GitLab Runner via Helm
helm repo add gitlab https://charts.gitlab.io

helm install gitlab-runner gitlab/gitlab-runner \
  --namespace gitlab-runners \
  --create-namespace \
  --set gitlabUrl=https://gitlab.com/ \
  --set runnerRegistrationToken="${GITLAB_REGISTRATION_TOKEN}" \
  --set rbac.create=true \
  --set runners.privileged=true \
  --set runners.config="
    [[runners]]
      [runners.kubernetes]
        namespace = \"gitlab-runners\"
        image = \"ubuntu:22.04\"
        privileged = true
        cpu_request = \"500m\"
        cpu_limit = \"2\"
        memory_request = \"1Gi\"
        memory_limit = \"4Gi\"
        service_cpu_request = \"100m\"
        service_cpu_limit = \"1\"
        helper_cpu_request = \"100m\"
        helper_cpu_limit = \"500m\"
        poll_timeout = 600
        [runners.kubernetes.volumes]
          [[runners.kubernetes.volumes.empty_dir]]
            name = \"docker-certs\"
            mount_path = \"/certs/client\"
            medium = \"Memory\"
  "
```

```toml
# config.toml för avancerad GitLab Runner
concurrent = 20
check_interval = 3

[[runners]]
  name = "kubernetes-runner"
  url = "https://gitlab.com/"
  token = "TOKEN"
  executor = "kubernetes"

  [runners.kubernetes]
    namespace = "gitlab-runners"
    image = "node:20"
    privileged = false

    # Säkerhet
    allow_privilege_escalation = false

    # Pod annotations
    [runners.kubernetes.pod_annotations]
      "prometheus.io/scrape" = "true"
      "prometheus.io/port" = "9252"

    # Node selector
    [runners.kubernetes.node_selector]
      "node-type" = "ci-runners"

    # Tolerations
    [[runners.kubernetes.node_tolerations]]
      key = "ci-runners"
      operator = "Equal"
      value = "true"
      effect = "NoSchedule"

    # Resource limits
    cpu_limit = "2"
    cpu_limit_overwrite_max_allowed = "4"
    memory_limit = "4Gi"
    memory_limit_overwrite_max_allowed = "8Gi"

    # Services
    [[runners.kubernetes.services]]
      name = "docker"
      alias = "docker"
      entrypoint = ["dockerd-entrypoint.sh"]
      command = ["--host=tcp://0.0.0.0:2376"]

    # Volumes
    [[runners.kubernetes.volumes.empty_dir]]
      name = "cache"
      mount_path = "/cache"

    [[runners.kubernetes.volumes.secret]]
      name = "docker-certs"
      mount_path = "/certs"
      read_only = true

  [runners.cache]
    Type = "s3"
    Shared = true
    [runners.cache.s3]
      ServerAddress = "minio.gitlab-runners.svc:9000"
      BucketName = "runner-cache"
      Insecure = true
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: GPU Runner för ML/AI

```yaml
# kubernetes/runners/gpu-runner.yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: gpu-runners
  namespace: arc-runners
spec:
  replicas: 2
  template:
    spec:
      organization: myorg
      labels:
        - gpu
        - cuda-12
        - linux

      # Custom image med CUDA
      image: myorg/actions-runner-cuda:12.2

      # GPU resources
      resources:
        limits:
          nvidia.com/gpu: 1
          cpu: "8"
          memory: "32Gi"
        requests:
          nvidia.com/gpu: 1
          cpu: "4"
          memory: "16Gi"

      # Node selector för GPU-noder
      nodeSelector:
        accelerator: nvidia-tesla-v100

      # Tolerations
      tolerations:
        - key: "nvidia.com/gpu"
          operator: "Exists"
          effect: "NoSchedule"
```

```dockerfile
# Dockerfile för GPU runner
FROM summerwind/actions-runner:latest

# Installera CUDA
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://nvidia.github.io/libnvidia-container/stable/deb/$(. /etc/os-release; echo $ID$VERSION_ID) /" | tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt-get update && \
    apt-get install -y nvidia-container-toolkit cuda-toolkit-12-2 && \
    rm -rf /var/lib/apt/lists/*

# Python för ML
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu122

USER runner
```

```yaml
# Workflow som använder GPU runner
name: ML Training

on:
  push:
    paths:
      - 'models/**'
      - 'training/**'

jobs:
  train:
    runs-on: [self-hosted, gpu, cuda-12]
    steps:
      - uses: actions/checkout@v4

      - name: Verify GPU
        run: |
          nvidia-smi
          python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

      - name: Train model
        run: |
          python3 training/train.py \
            --epochs 100 \
            --batch-size 64 \
            --learning-rate 0.001

      - name: Upload model
        uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: models/output/
```

### Exempel 2: Multi-Architecture Build

```yaml
# kubernetes/runners/arm-runner.yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: arm64-runners
  namespace: arc-runners
spec:
  replicas: 2
  template:
    spec:
      organization: myorg
      labels:
        - arm64
        - linux

      # ARM64 image
      image: summerwind/actions-runner:latest

      # Node selector för ARM-noder
      nodeSelector:
        kubernetes.io/arch: arm64

      resources:
        limits:
          cpu: "4"
          memory: "8Gi"
```

```yaml
# Multi-arch build workflow
name: Multi-Architecture Build

on:
  push:
    branches: [main]

jobs:
  build:
    strategy:
      matrix:
        include:
          - runner: [self-hosted, linux, x64]
            arch: amd64
          - runner: [self-hosted, linux, arm64]
            arch: arm64

    runs-on: ${{ matrix.runner }}

    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: |
          docker build -t myapp:${{ github.sha }}-${{ matrix.arch }} .
          docker push myapp:${{ github.sha }}-${{ matrix.arch }}

  manifest:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Create multi-arch manifest
        run: |
          docker manifest create myapp:${{ github.sha }} \
            myapp:${{ github.sha }}-amd64 \
            myapp:${{ github.sha }}-arm64
          docker manifest push myapp:${{ github.sha }}
```

### Exempel 3: Säkerhetshärdad Runner

```yaml
# kubernetes/runners/hardened-runner.yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: hardened-runners
  namespace: arc-runners
spec:
  replicas: 5
  template:
    spec:
      organization: myorg
      ephemeral: true

      labels:
        - hardened
        - linux
        - production

      # Minimal base image
      image: myorg/actions-runner-hardened:latest

      # Strikt säkerhet
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        runAsGroup: 1000
        fsGroup: 1000
        seccompProfile:
          type: RuntimeDefault

      containerSecurityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: false
        capabilities:
          drop:
            - ALL

      # Resursbegränsningar
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"
          ephemeral-storage: "10Gi"
        requests:
          cpu: "500m"
          memory: "1Gi"

      # Service account med minimal access
      serviceAccountName: hardened-runner-sa
      automountServiceAccountToken: false

      # No host networking
      hostNetwork: false
      hostPID: false
      hostIPC: false

---
# Network policy för isolation
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: hardened-runner-policy
  namespace: arc-runners
spec:
  podSelector:
    matchLabels:
      actions-runner: hardened-runners
  policyTypes:
    - Ingress
    - Egress

  # Ingen ingress
  ingress: []

  # Begränsad egress
  egress:
    # GitHub API
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
      ports:
        - protocol: TCP
          port: 443
    # DNS
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53

---
# Pod Security Policy (om aktiverat)
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: hardened-runner-psp
spec:
  privileged: false
  allowPrivilegeEscalation: false
  runAsUser:
    rule: MustRunAsNonRoot
  seLinux:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
    - emptyDir
    - secret
    - configMap
  hostNetwork: false
  hostIPC: false
  hostPID: false
```

------------------------------------------------------------

## Bästa Praxis

### 1. Använd Ephemeral Runners för Public Repos

```yaml
# Workflow med säker ephemeral runner
jobs:
  build:
    runs-on: [self-hosted, ephemeral, linux]
    steps:
      - uses: actions/checkout@v4
      # Runnern förstörs efter detta job
```

### 2. Implementera Runner Labels Strategiskt

```yaml
# Organisera runners med labels
# Environment-baserade
runs-on: [self-hosted, production]
runs-on: [self-hosted, staging]

# Kapacitetsbaserade
runs-on: [self-hosted, high-memory]
runs-on: [self-hosted, gpu, cuda-12]

# Team-baserade
runs-on: [self-hosted, team-backend]
runs-on: [self-hosted, team-ml]
```

### 3. Övervaka Runner Health

```yaml
# Prometheus metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: runner-metrics
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: actions-runner
  endpoints:
    - port: metrics
      interval: 30s
```

### 4. Regelbunden Uppdatering

```bash
#!/bin/bash
# scripts/update-runners.sh
# Kör månadsvis

# Uppdatera ARC
helm upgrade arc actions-runner-controller/actions-runner-controller \
  --namespace arc-system \
  --reuse-values

# Rulla ut nya runners
kubectl rollout restart deployment -n arc-runners
```

------------------------------------------------------------

## Vanliga Fallgropar

### ❌ Fallgrop 1: Persistent Runners för Public Repos

```yaml
# ❌ DÅLIGT: Persistent runner kan komprometteras
runs-on: [self-hosted, linux]

# ✅ BRA: Ephemeral runner för varje job
# RunnerDeployment med ephemeral: true
```

### ❌ Fallgrop 2: Överdriven Privileged Mode

```yaml
# ❌ DÅLIGT: Full privileged access
dockerdWithinRunnerContainer: true
securityContext:
  privileged: true

# ✅ BRA: Rootless Docker eller Kaniko
# Använd kaniko för container builds istället
```

### ❌ Fallgrop 3: Ingen Resursbegränsning

```yaml
# ❌ DÅLIGT: Obegränsade resurser
resources: {}

# ✅ BRA: Explicita limits
resources:
  limits:
    cpu: "4"
    memory: "8Gi"
  requests:
    cpu: "1"
    memory: "2Gi"
```

------------------------------------------------------------

## Övningar

### Övning 1: Sätt upp GitHub Actions Runner (20 XP)

**Mål:** Installera och konfigurera en self-hosted runner på en VM.

**Din uppgift:**
1. Skapa en Ubuntu VM (kan vara lokal VM eller cloud)
2. Installera GitHub Actions runner
3. Registrera mot ditt repository
4. Skapa en workflow som använder runnern
5. Verifiera att builds körs på din runner

<details>
<summary>Ledtråd</summary>

Hämta registration token från Settings → Actions → Runners. Använd `--unattended` för scriptat setup.

</details>

<details>
<summary>Lösning</summary>

Se Steg 1 i guiden för komplett setup-script. Workflow:

```yaml
name: Test Self-Hosted
on: [push]
jobs:
  test:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - run: echo "Running on $(hostname)"
```

</details>

---

### Övning 2: Kubernetes Runner med Autoscaling (25 XP)

**Mål:** Deploya ARC med autoskalning baserat på job queue.

**Din uppgift:**
1. Installera Actions Runner Controller i Kubernetes
2. Skapa en RunnerDeployment
3. Konfigurera HorizontalRunnerAutoscaler
4. Testa genom att trigga flera workflows samtidigt
5. Verifiera att runners skalas upp och ner

<details>
<summary>Ledtråd</summary>

Skapa GitHub App för bättre rate limits. Använd `TotalNumberOfQueuedAndInProgressWorkflowRuns` metric.

</details>

<details>
<summary>Lösning</summary>

Se Steg 2 för kompletta manifests. Testa med:

```bash
# Trigga 10 workflows samtidigt
for i in {1..10}; do
  gh workflow run test.yml &
done
wait

# Observera scaling
kubectl get pods -n arc-runners -w
```

</details>

---

### Övning 3: Säkerhetshärdad Ephemeral Runner (35 XP)

**Mål:** Bygg en produktionsklar säkerhetshärdad runner.

**Din uppgift:**
1. Skapa ephemeral RunnerDeployment
2. Implementera NetworkPolicy för isolation
3. Konfigurera securityContext med minimal privileges
4. Lägg till monitoring med Prometheus
5. Dokumentera säkerhetsåtgärder

<details>
<summary>Ledtråd</summary>

Kombinera `ephemeral: true`, `runAsNonRoot`, NetworkPolicy och resource limits.

</details>

<details>
<summary>Lösning</summary>

Se Exempel 3: Säkerhetshärdad Runner för komplett implementation.

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **GitHub Actions Fundamentals:** Grund för runner-användning
- **Enterprise CI/CD Patterns:** Runners i enterprise-miljöer
- **Secrets Management:** Säker hantering av credentials på runners
- **Container-based CI/CD:** Docker-builds på self-hosted runners

### Förkunskaper:
- Linux-administration
- Kubernetes basics
- Docker och containrar
- Nätverkssäkerhet

### Bygger mot:
- Enterprise-grade CI/CD-infrastruktur
- High-performance ML pipelines
- Compliant CI/CD för reglerade industrier
- Multi-cloud CI/CD-arkitektur

------------------------------------------------------------

## Sammanfattning

- **Self-hosted runners** krävs för specialhårdvara, compliance och interna resurser
- **Ephemeral runners** är säkrare och rekommenderas för production
- **Actions Runner Controller (ARC)** möjliggör Kubernetes-baserad autoskalning
- **Labels** organiserar runners för targeting i workflows
- **Säkerhetshärdning** inkluderar non-root, NetworkPolicy och resource limits
- **Monitoring** är kritiskt för att upptäcka problem tidigt
- **GitLab Runner** stödjer Kubernetes executor för liknande funktionalitet
- **GPU runners** möjliggör ML/AI-träning i CI/CD
- Uppdatera runners regelbundet för säkerhetspatchar

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `./config.sh --url X --token Y` | Konfigurera GitHub runner |
| `./svc.sh install && ./svc.sh start` | Starta som service |
| `gitlab-runner register` | Registrera GitLab runner |
| `helm install arc actions-runner-controller/actions-runner-controller` | Installera ARC |
| `kubectl get runnerdeployments` | Lista runner deployments |
| `kubectl get horizontalrunnerautoscalers` | Lista autoscalers |

------------------------------------------------------------

## Referenser

- GitHub Self-Hosted Runners: https://docs.github.com/en/actions/hosting-your-own-runners
- Actions Runner Controller: https://github.com/actions/actions-runner-controller
- GitLab Runner: https://docs.gitlab.com/runner/
- Kubernetes Executor: https://docs.gitlab.com/runner/executors/kubernetes.html
- Runner Security: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions
- NVIDIA GPU Operator: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/
""",
        },
        {
            "order_index": 19,
            "title": "Monorepo CI/CD Patterns",
            "slug": "monorepo-cicd-patterns",
            "difficulty": "advanced",
            "content": """# Monorepo CI/CD Patterns

------------------------------------------------------------

## Introduktion

Monorepo-arkitektur - där flera projekt, applikationer och paket lever i samma repository - har blivit standard för moderna organisationer. Google, Meta, Microsoft och Uber hanterar miljontals rader kod i monorepos. Men denna arkitektur skapar unika CI/CD-utmaningar: hur bygger du bara det som ändrats? Hur hanterar du beroenden mellan projekt? Hur skapar du koordinerade releases?

**Verkliga utmaningar:**
- **Build-tider som exploderar:** Utan smart change detection kan varje commit trigga builds för alla 50+ projekt
- **Cache-invalidering:** Ett ändrat shared-paket kan invalidera cachen för hela monorepon
- **Dependency hell:** Cirkulära beroenden och version-mismatches mellan projekt
- **Release koordination:** Hur releaser du frontend och backend tillsammans när de delar typer?
- **CI-kostnader:** GitHub Actions eller CircleCI-minuter som skenar när allt byggs varje gång

**Vad denna nod täcker:**
- Turborepo, Nx och Bazel för intelligent change detection
- Remote caching för dramatiskt snabbare builds
- Dependency graph-analys och affected-commands
- Changesets för koordinerad versioning och changelogs
- Multi-project deployment strategies
- Path-based filtering och workspace-native features

**Förkunskaper:**
- Node.js och npm/pnpm/yarn
- GitHub Actions eller annan CI/CD-plattform
- Grundläggande förståelse för package managers och workspaces
- Erfarenhet av JavaScript/TypeScript-projekt

**I slutet av denna nod kan du:**
- Konfigurera Turborepo eller Nx för effektiv monorepo-CI/CD
- Implementera remote caching som sparar timmar av build-tid
- Bygga endast affected projects baserat på ändringar
- Skapa koordinerade releases med changesets
- Optimera CI/CD-kostnader genom smart execution

------------------------------------------------------------

## Teori

### Monorepo vs Polyrepo Trade-offs

```
POLYREPO                              MONOREPO
+-------------+  +-------------+      +---------------------------+
| Frontend    |  | Backend     |      |         Monorepo          |
| Repo        |  | Repo        |      |                           |
|             |  |             |      |  +---------+ +---------+  |
| - Own CI/CD |  | - Own CI/CD |      |  |Frontend | |Backend  |  |
| - Own deps  |  | - Own deps  |      |  +---------+ +---------+  |
| - Isolated  |  | - Isolated  |      |                           |
+-------------+  +-------------+      |  +---------+ +---------+  |
                                      |  |Shared   | |Types    |  |
+-------------+                       |  +---------+ +---------+  |
| Shared      |                       |                           |
| Repo        |   = 3 repos           |  - Unified CI/CD          |
| - Published |   = 3 CI/CD           |  - Shared deps            |
+-------------+   = NPM deps          |  - Atomic changes         |
                                      +---------------------------+
                                        = 1 repo, 1 CI/CD
```

**Monorepo fördelar:**
| Fördel | Beskrivning | Exempel |
|--------|-------------|---------|
| **Atomic changes** | En PR kan ändra frontend + backend + types | Lägg till nytt API endpoint med typer |
| **Code sharing** | Direkt import utan publish | Import { User } from '@acme/types' |
| **Unified tooling** | En ESLint, en Prettier, en test-config | Konsistens över alla projekt |
| **Koordinerade releases** | Relaterade paket releasas tillsammans | v2.0.0 för hela systemet |
| **Enklare refactoring** | Hitta alla usages, ändra överallt | Byt API-response format |

**Monorepo utmaningar:**
| Utmaning | Konsekvens | Lösning |
|----------|------------|---------|
| **Build-tid** | Allt byggs varje gång | Change detection + caching |
| **Dependency graph** | Komplex beroendestruktur | Graph-verktyg (Nx, Turbo) |
| **Repository storlek** | Långsam clone | Shallow clone, sparse checkout |
| **Ägarskap** | Vem äger vad? | CODEOWNERS, team boundaries |
| **CI-kostnader** | Dyra builds | Remote caching, affected builds |

### Change Detection Principer

```
                     CHANGE DETECTION FLOW

   Commit: "Update Button component"
                    │
                    ▼
   ┌────────────────────────────────────┐
   │         DETECT CHANGES             │
   │                                    │
   │   git diff HEAD~1 --name-only      │
   │   Result: packages/ui/Button.tsx   │
   └────────────────────────────────────┘
                    │
                    ▼
   ┌────────────────────────────────────┐
   │      BUILD DEPENDENCY GRAPH        │
   │                                    │
   │   @acme/ui ◄── apps/web           │
   │             ◄── apps/docs          │
   │             ◄── packages/widgets   │
   └────────────────────────────────────┘
                    │
                    ▼
   ┌────────────────────────────────────┐
   │      CALCULATE AFFECTED            │
   │                                    │
   │   packages/ui (changed)            │
   │   packages/widgets (depends on ui) │
   │   apps/web (depends on ui)         │
   │   apps/docs (depends on ui)        │
   │                                    │
   │   NOT affected: apps/api           │
   └────────────────────────────────────┘
                    │
                    ▼
   ┌────────────────────────────────────┐
   │      RUN TASKS ON AFFECTED         │
   │                                    │
   │   turbo run build --filter=[HEAD~1]│
   │   > Build: @acme/ui               │
   │   > Build: @acme/widgets          │
   │   > Build: apps/web               │
   │   > Build: apps/docs              │
   │   > Skip: apps/api (no changes)   │
   └────────────────────────────────────┘
```

### Caching-strategier

```
                    CACHING HIERARKI

   ┌─────────────────────────────────────────┐
   │              REMOTE CACHE               │
   │        (Vercel, Nx Cloud, etc.)        │
   │                                         │
   │   cache-key: hash(inputs + deps + env) │
   │   Delas mellan: Alla CI runners + devs │
   │   Hit rate: 70-90%                     │
   └─────────────────────────────────────────┘
                       │
                       │ Miss? Försök nästa nivå
                       ▼
   ┌─────────────────────────────────────────┐
   │              LOCAL CACHE                │
   │         (.turbo/ eller .nx/)           │
   │                                         │
   │   Lagrad på: CI runner disk            │
   │   Livslängd: Runner session            │
   │   GitHub Cache Action kan persistera   │
   └─────────────────────────────────────────┘
                       │
                       │ Miss? Bygg
                       ▼
   ┌─────────────────────────────────────────┐
   │            ACTUAL BUILD                 │
   │                                         │
   │   npm run build                        │
   │   Output sparas i cache                │
   │   Pushas till remote                   │
   └─────────────────────────────────────────┘

   CACHE HIT = Sekunder (download output)
   CACHE MISS = Minuter (faktisk build)
```

### Task Orchestration

```
                    TASK ORCHESTRATION

   turbo run build test lint

   ┌─────────────────────────────────────────────────────┐
   │                  TOPOLOGICAL SORT                   │
   │                                                     │
   │   @acme/types ────┬───► @acme/utils ──────┐        │
   │                   │                        │        │
   │                   └───► @acme/ui ─────────┼───┐    │
   │                                           │   │    │
   │   @acme/config ──────────────────────────┼───┼──┐ │
   │                                           ▼   ▼  ▼ │
   │                                      apps/web      │
   │                                                     │
   │   Build order: types → utils, ui → web             │
   └─────────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────┐
   │                  PARALLEL EXECUTION                 │
   │                                                     │
   │   Time ────────────────────────────────────►       │
   │                                                     │
   │   CPU 1: [  types  ][  utils  ][     web     ]     │
   │   CPU 2: [  config ][   ui    ][             ]     │
   │   CPU 3: [      lint: types, config, ui     ]      │
   │   CPU 4: [      test: types, config         ]      │
   │                                                     │
   │   Turbo/Nx maximerar parallellism baserat på       │
   │   dependency graph och tillgängliga CPU-cores      │
   └─────────────────────────────────────────────────────┘
```

### Verktygslandskap

| Verktyg | Fokus | Språk | Företag |
|---------|-------|-------|---------|
| **Turborepo** | Enkelhet, caching | JS/TS | Vercel |
| **Nx** | Full-featured, plugins | Alla | Nrwl |
| **Bazel** | Hermetic builds, scale | Alla | Google |
| **Lerna** | Publishing (legacy) | JS/TS | Open source |
| **Rush** | Enterprise scale | JS/TS | Microsoft |
| **moon** | Modern, fast | Alla | moonrepo |
| **pants** | Python-fokus | Python, Go | Toolchain |

**Val-guide:**
```
Start här:
    │
    ├─ Bara JavaScript/TypeScript?
    │   │
    │   ├─ Enkelhet + Speed? → Turborepo
    │   │
    │   └─ Plugins + Generators? → Nx
    │
    ├─ Flera språk (JS + Python + Go)?
    │   │
    │   ├─ < 1M lines of code? → Nx (custom executors)
    │   │
    │   └─ Google-scale? → Bazel
    │
    └─ Python-fokus?
        │
        └─ pants eller poetry workspaces
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Grundläggande Monorepo-struktur

```bash
# Skapa monorepo med pnpm workspaces
mkdir acme-monorepo && cd acme-monorepo
pnpm init

# Konfigurera workspaces
cat > pnpm-workspace.yaml << 'EOF'
packages:
  - 'apps/*'
  - 'packages/*'
EOF

# Root package.json
cat > package.json << 'EOF'
{
  "name": "acme-monorepo",
  "private": true,
  "scripts": {
    "build": "turbo run build",
    "test": "turbo run test",
    "lint": "turbo run lint",
    "dev": "turbo run dev",
    "clean": "turbo run clean && rm -rf node_modules"
  },
  "devDependencies": {
    "turbo": "^2.0.0",
    "typescript": "^5.4.0"
  },
  "packageManager": "pnpm@9.0.0"
}
EOF

# Skapa mappstruktur
mkdir -p apps/{web,api,docs}
mkdir -p packages/{ui,types,config,utils}
```

```bash
# Shared TypeScript config
# packages/config/tsconfig/base.json
mkdir -p packages/config/tsconfig
cat > packages/config/tsconfig/base.json << 'EOF'
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "compilerOptions": {
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true
  }
}
EOF

# React library config
cat > packages/config/tsconfig/react-library.json << 'EOF'
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "extends": "./base.json",
  "compilerOptions": {
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "declaration": true,
    "declarationMap": true,
    "outDir": "dist"
  }
}
EOF

# Config package.json
cat > packages/config/package.json << 'EOF'
{
  "name": "@acme/config",
  "version": "0.0.0",
  "private": true,
  "exports": {
    "./tsconfig/*": "./tsconfig/*.json",
    "./eslint": "./eslint/index.js"
  }
}
EOF
```

### Steg 2: Konfigurera Turborepo

```json
// turbo.json - Full konfiguration
{
  "$schema": "https://turbo.build/schema.json",

  // Globala beroenden som påverkar all caching
  "globalDependencies": [
    ".env",
    ".env.local",
    "tsconfig.json"
  ],

  // Globala environment variables
  "globalEnv": [
    "NODE_ENV",
    "CI"
  ],

  // Task pipeline
  "tasks": {
    // Build task
    "build": {
      "dependsOn": ["^build"],  // Bygg dependencies först
      "outputs": [
        "dist/**",
        ".next/**",
        "!.next/cache/**"
      ],
      "inputs": [
        "src/**",
        "package.json",
        "tsconfig.json"
      ]
    },

    // Test task
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "inputs": [
        "src/**",
        "tests/**",
        "**/*.test.ts",
        "**/*.test.tsx"
      ]
    },

    // Lint task - ingen ordning behövs
    "lint": {
      "dependsOn": [],
      "outputs": [],
      "inputs": [
        "src/**",
        "*.config.js",
        ".eslintrc*"
      ]
    },

    // Type check
    "typecheck": {
      "dependsOn": ["^build"],
      "outputs": []
    },

    // Dev server - persistent task
    "dev": {
      "dependsOn": ["^build"],
      "persistent": true,
      "cache": false
    },

    // Clean task
    "clean": {
      "cache": false
    }
  }
}
```

```yaml
# .github/workflows/ci.yml - Turborepo CI
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
  TURBO_TEAM: ${{ vars.TURBO_TEAM }}

jobs:
  build:
    name: Build and Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history för change detection

      - name: Setup pnpm
        uses: pnpm/action-setup@v3
        with:
          version: 9

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      # Kör alla tasks på affected packages
      - name: Build affected packages
        run: pnpm turbo run build --filter='[HEAD^1]'

      - name: Lint affected packages
        run: pnpm turbo run lint --filter='[HEAD^1]'

      - name: Test affected packages
        run: pnpm turbo run test --filter='[HEAD^1]'

      - name: Typecheck affected packages
        run: pnpm turbo run typecheck --filter='[HEAD^1]'
```

### Steg 3: Konfigurera Nx (alternativ)

```bash
# Skapa Nx workspace
npx create-nx-workspace@latest acme --preset=ts
cd acme

# Lägg till plugins
npm install -D @nx/next @nx/react @nx/node @nx/eslint
```

```json
// nx.json - Full konfiguration
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "namedInputs": {
    // Produktionskod (exkluderar tester)
    "production": [
      "default",
      "!{projectRoot}/**/*.test.ts",
      "!{projectRoot}/**/*.spec.ts",
      "!{projectRoot}/jest.config.ts"
    ],
    // Alla filer
    "default": [
      "{projectRoot}/**/*",
      "sharedGlobals"
    ],
    // Globala filer som påverkar alla
    "sharedGlobals": [
      "{workspaceRoot}/tsconfig.base.json",
      "{workspaceRoot}/.eslintrc.json"
    ]
  },

  // Task runners
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "lint", "test", "typecheck"]
      }
    }
  },

  // Target defaults
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "outputs": ["{projectRoot}/dist"]
    },
    "test": {
      "inputs": ["default", "^production"],
      "outputs": ["{projectRoot}/coverage"]
    },
    "lint": {
      "inputs": ["default"],
      "outputs": []
    }
  },

  // Default project (för nx run commands)
  "defaultProject": "web"
}
```

```yaml
# .github/workflows/ci.yml - Nx CI
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

      # Sätt base och head SHAs för affected
      - uses: nrwl/nx-set-shas@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci

      # Kör affected commands
      - name: Lint affected
        run: npx nx affected -t lint --parallel=3

      - name: Test affected
        run: npx nx affected -t test --parallel=3 --ci --code-coverage

      - name: Build affected
        run: npx nx affected -t build --parallel=3

      # Visa affected projects
      - name: Show affected projects
        run: npx nx show projects --affected

  # Distributed task execution (DTE) för stora repos
  dte:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
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

      # Använd Nx Cloud för distributed execution
      - name: Run with Nx Cloud DTE
        run: npx nx-cloud start-ci-run --distribute-on="3 linux-medium-js"

      - name: Run all targets
        run: |
          npx nx affected -t lint test build --parallel=3
```

### Steg 4: Remote Caching

```bash
# Turborepo Remote Caching med Vercel
# 1. Länka till Vercel
npx turbo login
npx turbo link

# 2. Sätt secrets i GitHub
# TURBO_TOKEN: Från Vercel dashboard
# TURBO_TEAM: Ditt Vercel team name

# 3. Verifiera
npx turbo run build --dry
# Output: Remote caching enabled
```

```yaml
# Självhostad Turbo Remote Cache med Docker
# docker-compose.yml
version: '3.8'
services:
  turbo-cache:
    image: ducktors/turborepo-remote-cache
    ports:
      - "3000:3000"
    environment:
      TURBO_TOKEN: ${TURBO_TOKEN}
      STORAGE_PROVIDER: local
      STORAGE_PATH: /cache
    volumes:
      - turbo-cache:/cache

volumes:
  turbo-cache:
```

```yaml
# CI med självhostad cache
name: CI with Self-Hosted Cache

jobs:
  build:
    runs-on: self-hosted
    env:
      TURBO_API: http://turbo-cache:3000
      TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
      TURBO_TEAM: acme

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install

      # --remote-only tvingar remote cache användning
      - run: pnpm turbo run build --remote-only
```

### Steg 5: Path-based Filtering utan Build Tool

```yaml
# .github/workflows/ci.yml - Manuell change detection
name: CI with Path Filtering

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      frontend: ${{ steps.filter.outputs.frontend }}
      backend: ${{ steps.filter.outputs.backend }}
      shared: ${{ steps.filter.outputs.shared }}
      infra: ${{ steps.filter.outputs.infra }}

    steps:
      - uses: actions/checkout@v4

      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            frontend:
              - 'apps/web/**'
              - 'packages/ui/**'
              - 'packages/types/**'
            backend:
              - 'apps/api/**'
              - 'packages/types/**'
              - 'packages/db/**'
            shared:
              - 'packages/types/**'
              - 'packages/utils/**'
            infra:
              - 'terraform/**'
              - 'k8s/**'

  # Frontend job
  frontend:
    needs: detect-changes
    if: needs.detect-changes.outputs.frontend == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --filter="@acme/web..." --frozen-lockfile

      - name: Build frontend
        run: pnpm --filter="@acme/web" build

      - name: Test frontend
        run: pnpm --filter="@acme/web" test

  # Backend job
  backend:
    needs: detect-changes
    if: needs.detect-changes.outputs.backend == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --filter="@acme/api..." --frozen-lockfile

      - name: Build backend
        run: pnpm --filter="@acme/api" build

      - name: Test backend
        run: pnpm --filter="@acme/api" test

  # Infrastructure job
  infra:
    needs: detect-changes
    if: needs.detect-changes.outputs.infra == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Plan
        run: |
          cd terraform
          terraform init
          terraform plan

  # Alltid kör om shared ändras (påverkar alla)
  shared-changes:
    needs: detect-changes
    if: needs.detect-changes.outputs.shared == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Build and test all (shared changed)
        run: |
          pnpm turbo run build test
```

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

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Fullständig Turborepo-monorepo

```
acme-monorepo/
├── apps/
│   ├── web/              # Next.js frontend
│   │   ├── package.json
│   │   └── src/
│   ├── api/              # Node.js backend
│   │   ├── package.json
│   │   └── src/
│   └── docs/             # Dokumentationssajt
│       ├── package.json
│       └── src/
├── packages/
│   ├── ui/               # Shared React components
│   │   ├── package.json
│   │   └── src/
│   ├── types/            # Shared TypeScript types
│   │   ├── package.json
│   │   └── src/
│   ├── config/           # Shared configs
│   │   ├── eslint/
│   │   └── tsconfig/
│   └── utils/            # Shared utilities
│       ├── package.json
│       └── src/
├── turbo.json
├── package.json
└── pnpm-workspace.yaml
```

```json
// packages/ui/package.json
{
  "name": "@acme/ui",
  "version": "0.0.0",
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    },
    "./button": {
      "import": "./dist/button.mjs",
      "require": "./dist/button.js",
      "types": "./dist/button.d.ts"
    }
  },
  "scripts": {
    "build": "tsup src/index.ts --format cjs,esm --dts",
    "dev": "tsup src/index.ts --format cjs,esm --dts --watch",
    "lint": "eslint src/",
    "test": "vitest run",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^18.2.0"
  },
  "devDependencies": {
    "@acme/config": "workspace:*",
    "@types/react": "^18.2.0",
    "tsup": "^8.0.0",
    "typescript": "^5.4.0",
    "vitest": "^1.4.0"
  }
}
```

```yaml
# .github/workflows/ci.yml - Komplett CI
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
  TURBO_TEAM: ${{ vars.TURBO_TEAM }}

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      # Parallell execution
      - name: Run CI tasks
        run: |
          pnpm turbo run \
            build \
            lint \
            test \
            typecheck \
            --filter='[HEAD^1]' \
            --concurrency=4

      # Upload artifacts för deployment
      - name: Upload build artifacts
        if: github.ref == 'refs/heads/main'
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: |
            apps/web/.next/
            apps/api/dist/

  deploy-preview:
    needs: build
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      # Deploy till preview environment
      - name: Deploy Preview
        run: |
          pnpm turbo run deploy:preview --filter='[HEAD^1]'
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - uses: actions/download-artifact@v4
        with:
          name: build-output

      - name: Deploy to Production
        run: |
          # Deploy frontend
          npx vercel deploy --prod --prebuilt

          # Deploy backend
          railway up -s api
```

### Exempel 2: Changesets för Koordinerad Release

```json
// .changeset/config.json
{
  "$schema": "https://unpkg.com/@changesets/config@3.0.0/schema.json",
  "changelog": [
    "@changesets/changelog-github",
    { "repo": "acme/monorepo" }
  ],
  "commit": false,
  "fixed": [],
  "linked": [
    ["@acme/web", "@acme/api", "@acme/types"]
  ],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": ["@acme/docs"]
}
```

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches: [main]

concurrency: ${{ github.workflow }}-${{ github.ref }}

jobs:
  release:
    name: Release
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile
      - run: pnpm turbo run build

      - name: Create Release Pull Request or Publish
        id: changesets
        uses: changesets/action@v1
        with:
          version: pnpm changeset version
          publish: pnpm changeset publish
          title: 'chore: version packages'
          commit: 'chore: version packages'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

      - name: Deploy if published
        if: steps.changesets.outputs.published == 'true'
        run: |
          echo "Packages published, deploying..."
          pnpm turbo run deploy --filter='[main^1]'
```

```bash
# Workflow för utvecklare:

# 1. Gör ändringar
git checkout -b feature/new-button
# Ändra packages/ui/src/Button.tsx

# 2. Skapa changeset
pnpm changeset
# Välj: @acme/ui
# Typ: patch
# Beskrivning: "Add loading state to Button"

# 3. Commit och push
git add .
git commit -m "feat: add loading state to button"
git push origin feature/new-button

# 4. Efter merge till main:
# - changesets/action skapar en PR med version bumps
# - När den PRn mergas, publiceras paketen
```

### Exempel 3: Multi-Language Monorepo med Nx

```json
// nx.json för mixed repo (TypeScript + Python + Go)
{
  "namedInputs": {
    "default": ["{projectRoot}/**/*"],
    "production": [
      "default",
      "!{projectRoot}/**/*.test.*",
      "!{projectRoot}/**/*_test.*"
    ]
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "cache": true
    },
    "test": {
      "dependsOn": ["build"],
      "cache": true
    },
    "lint": {
      "cache": true
    }
  },
  "plugins": [
    "@nx/next",
    "@nx/node",
    {
      "plugin": "./tools/nx-python-plugin",
      "options": {
        "pythonCommand": "python3"
      }
    },
    {
      "plugin": "./tools/nx-go-plugin",
      "options": {
        "goCommand": "go"
      }
    }
  ]
}
```

```yaml
# .github/workflows/ci.yml - Multi-language
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  affected:
    runs-on: ubuntu-latest
    outputs:
      has-js: ${{ steps.affected.outputs.has-js }}
      has-python: ${{ steps.affected.outputs.has-python }}
      has-go: ${{ steps.affected.outputs.has-go }}

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: nrwl/nx-set-shas@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - run: npm ci

      - id: affected
        run: |
          # Kolla vilka språk som påverkas
          AFFECTED=$(npx nx show projects --affected --json)

          if echo "$AFFECTED" | jq -e '.[] | select(startswith("js-"))' > /dev/null; then
            echo "has-js=true" >> $GITHUB_OUTPUT
          fi

          if echo "$AFFECTED" | jq -e '.[] | select(startswith("py-"))' > /dev/null; then
            echo "has-python=true" >> $GITHUB_OUTPUT
          fi

          if echo "$AFFECTED" | jq -e '.[] | select(startswith("go-"))' > /dev/null; then
            echo "has-go=true" >> $GITHUB_OUTPUT
          fi

  js-build:
    needs: affected
    if: needs.affected.outputs.has-js == 'true'
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
      - run: npx nx affected -t build test lint --parallel=3

  python-build:
    needs: affected
    if: needs.affected.outputs.has-python == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: nrwl/nx-set-shas@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - run: npm ci
      - run: pip install poetry

      - run: npx nx affected -t build test lint --parallel=3

  go-build:
    needs: affected
    if: needs.affected.outputs.has-go == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: nrwl/nx-set-shas@v4

      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - run: npm ci
      - run: npx nx affected -t build test lint --parallel=3
```

### Exempel 4: Deployment Matrix för Monorepo

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  detect-deployables:
    runs-on: ubuntu-latest
    outputs:
      apps: ${{ steps.detect.outputs.apps }}

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - id: detect
        run: |
          # Hitta affected apps som är deployable
          APPS=$(pnpm turbo run build --filter='[HEAD^1]' --dry=json \
            | jq -r '.tasks[] | select(.task == "build") | .package' \
            | xargs -I {} sh -c 'test -f apps/{}/deploy.sh && echo {}' \
            | jq -R -s -c 'split("\n") | map(select(length > 0))')

          echo "apps=$APPS" >> $GITHUB_OUTPUT

  deploy:
    needs: detect-deployables
    if: needs.detect-deployables.outputs.apps != '[]'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        app: ${{ fromJson(needs.detect-deployables.outputs.apps) }}
      fail-fast: false
      max-parallel: 2

    environment: production-${{ matrix.app }}

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      # Build the specific app
      - name: Build ${{ matrix.app }}
        run: pnpm turbo run build --filter=${{ matrix.app }}
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: ${{ vars.TURBO_TEAM }}

      # Deploy using app-specific script
      - name: Deploy ${{ matrix.app }}
        run: ./apps/${{ matrix.app }}/deploy.sh
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
          ENVIRONMENT: production

  notify:
    needs: [detect-deployables, deploy]
    if: always() && needs.detect-deployables.outputs.apps != '[]'
    runs-on: ubuntu-latest

    steps:
      - name: Send Slack notification
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Deployment completed",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Monorepo Deployment*\\n${{ needs.deploy.result == 'success' && '✅ Success' || '❌ Failed' }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

------------------------------------------------------------

## Bästa Praxis

### 1. Strukturera Beroenden Korrekt

```
DEPENDENCY DIRECTION

                    ┌─────────────┐
                    │   apps/     │
                    │             │
                    │  web  api   │
                    └──────┬──────┘
                           │ imports
                           ▼
                    ┌─────────────┐
                    │  packages/  │
                    │             │
                    │  ui  utils  │
                    └──────┬──────┘
                           │ imports
                           ▼
                    ┌─────────────┐
                    │  packages/  │
                    │             │
                    │ types config│
                    └─────────────┘

Rules:
1. Apps → Packages (never Packages → Apps)
2. Higher level → Lower level
3. No circular dependencies
```

```json
// turbo.json - Boundary enforcement
{
  "tasks": {
    "lint:deps": {
      "dependsOn": [],
      "outputs": [],
      "inputs": ["package.json", "tsconfig.json"]
    }
  }
}

// .depcheckrc
{
  "rules": [
    {
      "rule": "no-circular",
      "scope": "all"
    },
    {
      "rule": "directory-hierarchy",
      "allow": [
        { "from": "apps/*", "to": "packages/*" },
        { "from": "packages/ui", "to": "packages/types" },
        { "from": "packages/utils", "to": "packages/types" }
      ]
    }
  ]
}
```

### 2. Optimera Cache Hit Rate

```yaml
# Maximera cache hits
# turbo.json
{
  "tasks": {
    "build": {
      "inputs": [
        # Endast source files
        "src/**/*.ts",
        "src/**/*.tsx",

        # Config som påverkar output
        "tsconfig.json",
        "package.json",

        # Exkludera test files
        "!**/*.test.ts",
        "!**/*.spec.ts",

        # Exkludera documentation
        "!**/*.md",
        "!docs/**"
      ],
      "outputs": [
        "dist/**"
      ]
    }
  },

  # Minimera globala invalidations
  "globalDependencies": [
    # Bara filer som VERKLIGEN påverkar alla
    "tsconfig.base.json"
    # INTE: package-lock.json, .env, etc
  ]
}
```

### 3. Parallellism och Concurrency

```yaml
# Optimal parallelism
# CI workflow
- name: Run tasks
  run: |
    # Sätt concurrency baserat på runner
    CPUS=$(nproc)
    pnpm turbo run build test lint \
      --concurrency=$CPUS \
      --log-order=grouped

# turbo.json
{
  "tasks": {
    # CPU-intensiva tasks: limit concurrency
    "build": {
      "dependsOn": ["^build"]
    },

    # I/O-bound tasks: hög parallelism OK
    "lint": {
      "dependsOn": []  # Kan köra parallellt med allt
    },

    # Tests: moderat parallellism
    "test": {
      "dependsOn": ["build"]
    }
  }
}
```

### 4. Workspace Dependencies

```json
// package.json - Workspace protocol
{
  "dependencies": {
    // ✅ Workspace protocol - alltid senaste
    "@acme/ui": "workspace:*",

    // ✅ Workspace med version constraint
    "@acme/types": "workspace:^1.0.0",

    // ❌ Undvik: Hårdkodad version
    // "@acme/ui": "1.2.3"
  }
}
```

------------------------------------------------------------

## Vanliga Fallgropar

### ❌ Fallgrop 1: Ingen Fetch Depth

```yaml
# ❌ DÅLIGT: Shallow clone
- uses: actions/checkout@v4
# fetch-depth: 1 (default)
# Change detection fungerar inte!

# ✅ BRA: Full history
- uses: actions/checkout@v4
  with:
    fetch-depth: 0  # Full history för change detection
```

### ❌ Fallgrop 2: Global Dependencies Explosionen

```json
// ❌ DÅLIGT: Allt är globalt
{
  "globalDependencies": [
    ".env",
    ".env.local",
    "package-lock.json",
    "tsconfig.json",
    "**/*.config.js"
  ]
}
// En ändring i package-lock invaliderar ALL cache

// ✅ BRA: Minimal globala deps
{
  "globalDependencies": [
    "tsconfig.base.json"
  ],
  "tasks": {
    "build": {
      "inputs": [
        "src/**",
        "tsconfig.json",
        "package.json"
      ]
    }
  }
}
```

### ❌ Fallgrop 3: Circular Dependencies

```typescript
// ❌ DÅLIGT: Cirkulärt beroende
// packages/ui/Button.tsx
import { formatDate } from '@acme/utils'

// packages/utils/date.ts
import { Button } from '@acme/ui'  // Circular!

// ✅ BRA: Extrahera till gemensam dependency
// packages/types/common.ts (bas)
// packages/utils/date.ts (importerar types)
// packages/ui/Button.tsx (importerar types och utils)
```

### ❌ Fallgrop 4: Missad Dependency Declaration

```json
// ❌ DÅLIGT: Implicit dependency
// packages/ui/package.json
{
  "dependencies": {
    // Använder @acme/types men deklarerar inte
  }
}
// Turbo vet inte om beroendet!

// ✅ BRA: Explicit dependency
{
  "dependencies": {
    "@acme/types": "workspace:*"
  }
}
```

### ❌ Fallgrop 5: Bygg Allt Alltid

```yaml
# ❌ DÅLIGT: Bygg allt varje gång
- run: pnpm turbo run build
# 30 minuter för varje PR...

# ✅ BRA: Bygg bara affected
- run: pnpm turbo run build --filter='[HEAD^1]'
# 2 minuter för typiska PRs
```

------------------------------------------------------------

## Övningar

### Övning 1: Sätt upp Turborepo Monorepo (20 XP)

**Mål:** Skapa en komplett monorepo med Turborepo.

**Din uppgift:**
1. Initiera pnpm workspace
2. Skapa två apps (web, api) och två packages (ui, types)
3. Konfigurera turbo.json med korrekt pipeline
4. Verifiera att `turbo run build` bygger i rätt ordning
5. Verifiera att `turbo run build --filter=@acme/web` bara bygger web och dess deps

<details>
<summary>Ledtråd</summary>

Använd `dependsOn: ["^build"]` för att säkerställa att dependencies byggs först.

</details>

<details>
<summary>Lösning</summary>

```bash
mkdir acme && cd acme
pnpm init

cat > pnpm-workspace.yaml << 'EOF'
packages:
  - 'apps/*'
  - 'packages/*'
EOF

mkdir -p apps/web apps/api packages/ui packages/types

# Skapa package.json för varje
# apps/web/package.json
{
  "name": "@acme/web",
  "dependencies": {
    "@acme/ui": "workspace:*",
    "@acme/types": "workspace:*"
  }
}

# turbo.json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    }
  }
}
```

</details>

---

### Övning 2: Implementera Remote Caching (25 XP)

**Mål:** Konfigurera Vercel Remote Cache för Turborepo.

**Din uppgift:**
1. Logga in på Vercel CLI
2. Länka projektet
3. Konfigurera GitHub Actions med TURBO_TOKEN
4. Mät cache hit rate före och efter
5. Dokumentera tidsbesparingen

<details>
<summary>Ledtråd</summary>

Använd `turbo run build --summarize` för att se cache statistics.

</details>

<details>
<summary>Lösning</summary>

```bash
# Lokalt
npx turbo login
npx turbo link

# GitHub Secrets
# TURBO_TOKEN: från Vercel
# TURBO_TEAM: team slug

# CI
- run: pnpm turbo run build --summarize
  env:
    TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
    TURBO_TEAM: ${{ vars.TURBO_TEAM }}

# Mät
# Första run: 0% cache hit, 5min
# Efterföljande: 95% cache hit, 30sec
```

</details>

---

### Övning 3: Changesets Release Pipeline (35 XP)

**Mål:** Implementera automatiserad release med Changesets.

**Din uppgift:**
1. Installera och konfigurera @changesets/cli
2. Skapa changeset workflow i GitHub Actions
3. Testa hela flödet: changeset → PR → merge → publish
4. Konfigurera linked packages för koordinerade releases
5. Generera changelog automatiskt

<details>
<summary>Ledtråd</summary>

Använd changesets/action för GitHub Actions. Konfigurera "linked" i config för att synka versioner.

</details>

<details>
<summary>Lösning</summary>

```bash
pnpm add -Dw @changesets/cli @changesets/changelog-github

# .changeset/config.json
{
  "changelog": ["@changesets/changelog-github", { "repo": "acme/monorepo" }],
  "linked": [["@acme/web", "@acme/api"]],
  "access": "restricted"
}

# Workflow
# 1. pnpm changeset (skapa changeset)
# 2. Push PR
# 3. Merge → changesets/action skapar version PR
# 4. Merge version PR → publicerar till npm
```

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **GitHub Actions Fundamentals:** Grund för CI/CD
- **Enterprise CI/CD Patterns:** Skalering av monorepo-CI
- **Container-based CI/CD:** Docker builds i monorepo
- **Self-Hosted Runners:** Custom runners för monorepo

### Förkunskaper:
- npm/pnpm workspaces
- Git branching och merging
- Package publishing (npm)
- TypeScript/JavaScript

### Bygger mot:
- Enterprise-scale monorepo management
- Automatiserad release engineering
- Platform engineering för monorepos
- Multi-team collaboration patterns

------------------------------------------------------------

## Sammanfattning

- **Monorepo CI/CD** kräver smart change detection och caching
- **Turborepo** erbjuder enkelhet och snabb setup med utmärkt caching
- **Nx** ger mer features som code generators och plugins
- **Remote caching** sparar dramatiskt med build-tid (70-90% cache hits)
- **Affected commands** bygger bara det som ändrats och dess beroenden
- **Dependency graph** måste struktureras korrekt (apps → packages)
- **Changesets** hanterar koordinerad versioning och changelogs
- **Path filtering** är ett enklare alternativ utan build tools
- Fetch depth 0 är kritiskt för change detection
- Minimera globalDependencies för bättre cache hit rate

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `turbo run build` | Bygg alla packages |
| `turbo run build --filter='[HEAD^1]'` | Bygg affected sedan förra commit |
| `turbo run build --filter=@acme/web...` | Bygg web och alla dependencies |
| `turbo run build --dry` | Visa vad som skulle köras |
| `npx nx affected -t build` | Nx affected build |
| `npx nx graph` | Visualisera dependency graph |
| `pnpm changeset` | Skapa ny changeset |
| `pnpm changeset version` | Bump versions från changesets |
| `pnpm changeset publish` | Publicera packages |

------------------------------------------------------------

## Referenser

- Turborepo Docs: https://turbo.build/repo/docs
- Nx Docs: https://nx.dev/getting-started/intro
- Changesets: https://github.com/changesets/changesets
- pnpm Workspaces: https://pnpm.io/workspaces
- Monorepo Tools: https://monorepo.tools/
- Vercel Remote Cache: https://vercel.com/docs/monorepos/remote-caching
""",
        },
        {
            "order_index": 20,
            "title": "Enterprise CI/CD Patterns",
            "slug": "enterprise-cicd-patterns",
            "difficulty": "expert",
            "content": """# Enterprise CI/CD Patterns

------------------------------------------------------------

## Introduktion

Enterprise CI/CD handlar om att skala CI/CD-praktiker från enstaka team till hundratals eller tusentals utvecklare. Det kräver standardisering, governance, self-service och automation på en helt annan nivå. Platform engineering-rörelsen har gjort enterprise CI/CD till en egen disciplin.

**Verkliga enterprise-utmaningar:**
- **Standardisering utan stagnation:** 200 team behöver konsistenta pipelines men också flexibilitet
- **Governance at scale:** Compliance-krav måste uppfyllas automatiskt, inte manuellt
- **Cost management:** CI/CD-kostnader kan skena - 6-siffriga månadsräkningar är vanliga
- **Self-service balans:** Teams ska kunna jobba självständigt inom guardrails
- **Multi-cloud/hybrid:** Olika applikationer deployas till olika miljöer
- **Audit och traceability:** Vem deployade vad, när, och varför?

**Vad denna nod täcker:**
- Platform Team-modellen och Internal Developer Platforms
- Reusable workflow templates och composite actions
- Policy-as-Code med OPA/Conftest
- Cost management och FinOps för CI/CD
- Centraliserad observability och metrics
- Multi-tenant CI/CD-plattformar
- DORA metrics och engineering intelligence
- Compliance automation och audit trails

**Förkunskaper:**
- Solid förståelse för CI/CD fundamentals
- Erfarenhet av GitHub Actions eller annan CI/CD-plattform
- Kubernetes basics (för advanced patterns)
- Förståelse för organisationsstrukturer

**I slutet av denna nod kan du:**
- Designa en Internal Developer Platform för CI/CD
- Implementera reusable workflow libraries
- Automatisera compliance och governance
- Sätta upp cost tracking och optimization
- Mäta och förbättra engineering effectiveness
- Bygga self-service CI/CD med guardrails

------------------------------------------------------------

## Teori

### Platform Engineering Model

```
                    PLATFORM ENGINEERING

   ┌─────────────────────────────────────────────────────┐
   │                  PRODUCT TEAMS                       │
   │                                                      │
   │   Team A      Team B      Team C      Team D        │
   │     ▼           ▼           ▼           ▼           │
   │   ┌────┐      ┌────┐      ┌────┐      ┌────┐       │
   │   │App │      │App │      │App │      │App │       │
   │   └────┘      └────┘      └────┘      └────┘       │
   │                                                      │
   │         Self-service, autonomi inom guardrails      │
   └──────────────────────────┬──────────────────────────┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────┐
   │              INTERNAL DEVELOPER PLATFORM            │
   │                                                      │
   │   ┌─────────────┬─────────────┬─────────────┐      │
   │   │  Templates  │   Policies  │  Self-Serve │      │
   │   │  Library    │   Engine    │  Portal     │      │
   │   └─────────────┴─────────────┴─────────────┘      │
   │                                                      │
   │   ┌─────────────┬─────────────┬─────────────┐      │
   │   │   Secrets   │   Runner    │  Monitoring │      │
   │   │   Manager   │   Pool      │  Dashboard  │      │
   │   └─────────────┴─────────────┴─────────────┘      │
   │                                                      │
   │         Maintained by Platform Team                 │
   └─────────────────────────────────────────────────────┘
```

### Golden Paths vs Guardrails

| Koncept | Definition | Implementation |
|---------|-----------|----------------|
| **Golden Path** | Rekommenderad, beprövad väg | Workflow templates, starter kits |
| **Guardrails** | Automatiska begränsningar | Policy-as-Code, required checks |
| **Paved Road** | Enkel väg med fart-bumps | Warnings, non-blocking checks |
| **Hard Boundary** | Absolut krav | Blocking policy, branch protection |

```
                    AUTONOMY SPECTRUM

   Full Autonomy ────────────────────────► Full Control

   ┌───────────┬───────────┬───────────┬───────────┐
   │           │           │           │           │
   │   Chaos   │  Paved    │  Golden   │  Locked   │
   │   Mode    │  Roads    │  Paths    │  Down     │
   │           │           │           │           │
   │ No rules  │ Warnings  │ Templates │ Required  │
   │ No help   │ Guidance  │ Defaults  │ Policies  │
   │           │           │           │           │
   └───────────┴───────────┴───────────┴───────────┘

   Optimal: Kombination av Golden Paths (enkelt)
            + Guardrails (säkert)
```

### DORA Metrics

```
                    DORA METRICS

   ┌─────────────────────────────────────────────────┐
   │                  THROUGHPUT                      │
   │                                                  │
   │   Deployment Frequency    Lead Time for Changes │
   │   ─────────────────────   ───────────────────── │
   │                                                  │
   │   How often we deploy     Time from commit      │
   │   to production           to production         │
   │                                                  │
   │   Elite: Multiple/day     Elite: < 1 hour      │
   │   High: 1/week-1/month    High: 1 day-1 week   │
   │   Medium: 1/month-6/month Medium: 1 week-1 mo  │
   │   Low: < 1/6 months       Low: 1 month-6 mo    │
   └─────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────┐
   │                   STABILITY                      │
   │                                                  │
   │   Change Failure Rate     MTTR                  │
   │   ─────────────────────   ───────────────────── │
   │                                                  │
   │   % of deployments        Mean Time to          │
   │   causing failures        Recovery              │
   │                                                  │
   │   Elite: 0-15%            Elite: < 1 hour      │
   │   High: 16-30%            High: < 1 day        │
   │   Medium: 31-45%          Medium: 1 day-1 week │
   │   Low: > 45%              Low: > 1 week        │
   └─────────────────────────────────────────────────┘
```

### Multi-Tenant Architecture

```
                 MULTI-TENANT CI/CD

   ┌─────────────────────────────────────────────────┐
   │                ORGANIZATION                      │
   │                                                  │
   │   ┌──────────┐  ┌──────────┐  ┌──────────┐     │
   │   │  Team A  │  │  Team B  │  │  Team C  │     │
   │   │          │  │          │  │          │     │
   │   │ ┌──────┐ │  │ ┌──────┐ │  │ ┌──────┐ │     │
   │   │ │Repo 1│ │  │ │Repo 3│ │  │ │Repo 5│ │     │
   │   │ │Repo 2│ │  │ │Repo 4│ │  │ │Repo 6│ │     │
   │   │ └──────┘ │  │ └──────┘ │  │ └──────┘ │     │
   │   │          │  │          │  │          │     │
   │   │ Budget:  │  │ Budget:  │  │ Budget:  │     │
   │   │ $1000/mo │  │ $2000/mo │  │ $500/mo  │     │
   │   └──────────┘  └──────────┘  └──────────┘     │
   │                                                  │
   │   Shared Resources:                             │
   │   - Self-hosted runners (pooled)                │
   │   - Remote cache                                │
   │   - Secrets vault                               │
   │   - Artifact storage                            │
   └─────────────────────────────────────────────────┘
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa Reusable Workflow Library

```yaml
# .github/workflows/templates/build-and-deploy.yml
# Centralt template-repo: myorg/platform-templates

name: Build and Deploy Template

on:
  workflow_call:
    inputs:
      # Application configuration
      app-name:
        description: 'Application name'
        required: true
        type: string
      language:
        description: 'Programming language'
        required: true
        type: string
        default: 'node'
      node-version:
        description: 'Node.js version'
        required: false
        type: string
        default: '20'
      python-version:
        description: 'Python version'
        required: false
        type: string
        default: '3.12'

      # Deployment configuration
      environment:
        description: 'Target environment'
        required: true
        type: string
      deploy-strategy:
        description: 'Deployment strategy'
        required: false
        type: string
        default: 'rolling'

      # Feature flags
      skip-tests:
        description: 'Skip tests'
        required: false
        type: boolean
        default: false
      security-scan:
        description: 'Run security scan'
        required: false
        type: boolean
        default: true

    secrets:
      DEPLOY_TOKEN:
        required: true
      SNYK_TOKEN:
        required: false
      SLACK_WEBHOOK:
        required: false

    outputs:
      deployment-url:
        description: 'URL of deployed application'
        value: ${{ jobs.deploy.outputs.url }}
      artifact-version:
        description: 'Version of deployed artifact'
        value: ${{ jobs.build.outputs.version }}

jobs:
  build:
    name: Build ${{ inputs.app-name }}
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Version calculation
      - name: Calculate version
        id: version
        run: |
          VERSION=$(git describe --tags --always)
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      # Language-specific setup
      - name: Setup Node.js
        if: inputs.language == 'node'
        uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'

      - name: Setup Python
        if: inputs.language == 'python'
        uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}

      # Build
      - name: Install and Build (Node)
        if: inputs.language == 'node'
        run: |
          npm ci
          npm run build

      - name: Install and Build (Python)
        if: inputs.language == 'python'
        run: |
          pip install poetry
          poetry install
          poetry build

      # Upload artifact
      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-${{ inputs.app-name }}-${{ steps.version.outputs.version }}
          path: |
            dist/
            build/
          retention-days: 7

  test:
    name: Test ${{ inputs.app-name }}
    needs: build
    if: ${{ !inputs.skip-tests }}
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup (Node)
        if: inputs.language == 'node'
        uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'

      - name: Run tests
        run: |
          npm ci
          npm test -- --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          flags: ${{ inputs.app-name }}

  security:
    name: Security Scan
    needs: build
    if: ${{ inputs.security-scan }}
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk
        uses: snyk/actions/node@master
        continue-on-error: true
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          severity: 'CRITICAL,HIGH'

  deploy:
    name: Deploy to ${{ inputs.environment }}
    needs: [build, test, security]
    if: always() && needs.build.result == 'success' && (needs.test.result == 'success' || needs.test.result == 'skipped')
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    outputs:
      url: ${{ steps.deploy.outputs.url }}

    steps:
      - uses: actions/checkout@v4

      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: build-${{ inputs.app-name }}-${{ needs.build.outputs.version }}

      - name: Deploy
        id: deploy
        run: |
          # Deploy logic based on strategy
          case "${{ inputs.deploy-strategy }}" in
            rolling)
              echo "Deploying with rolling update..."
              ;;
            blue-green)
              echo "Deploying with blue-green..."
              ;;
            canary)
              echo "Deploying with canary..."
              ;;
          esac

          echo "url=https://${{ inputs.app-name }}.${{ inputs.environment }}.example.com" >> $GITHUB_OUTPUT
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}

      - name: Notify Slack
        if: always() && secrets.SLACK_WEBHOOK != ''
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "${{ inputs.app-name }} deployed to ${{ inputs.environment }}: ${{ job.status }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

```yaml
# Användning i team-repo
# .github/workflows/ci.yml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:

jobs:
  deploy-staging:
    uses: myorg/platform-templates/.github/workflows/build-and-deploy.yml@v2
    with:
      app-name: my-service
      language: node
      environment: staging
      security-scan: true
    secrets:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  deploy-production:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    uses: myorg/platform-templates/.github/workflows/build-and-deploy.yml@v2
    with:
      app-name: my-service
      language: node
      environment: production
      deploy-strategy: canary
    secrets:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
```

### Steg 2: Implementera Policy-as-Code

```rego
# policies/cicd/required-checks.rego
package cicd.required_checks

default allow = false

# Alla repos måste ha required checks
allow {
  input.repository.branch_protection.required_status_checks.strict == true
  count(input.repository.branch_protection.required_status_checks.contexts) >= 3
}

required_checks := ["build", "test", "security-scan"]

violation[msg] {
  context := required_checks[_]
  not context_exists(context)
  msg := sprintf("Required check '%s' is not configured", [context])
}

context_exists(context) {
  input.repository.branch_protection.required_status_checks.contexts[_] == context
}
```

```rego
# policies/kubernetes/security.rego
package kubernetes.security

# Deny privileged containers
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("Container '%s' must not run in privileged mode", [container.name])
}

# Require resource limits
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.resources.limits.memory
  msg := sprintf("Container '%s' must specify memory limits", [container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.resources.limits.cpu
  msg := sprintf("Container '%s' must specify CPU limits", [container.name])
}

# Require non-root
deny[msg] {
  input.kind == "Deployment"
  not input.spec.template.spec.securityContext.runAsNonRoot == true
  msg := "Deployment must run as non-root user"
}

# Require read-only root filesystem
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.securityContext.readOnlyRootFilesystem == true
  msg := sprintf("Container '%s' should have read-only root filesystem", [container.name])
}
```

```yaml
# .github/workflows/policy-check.yml
name: Policy Check

on:
  pull_request:
    paths:
      - 'k8s/**'
      - 'terraform/**'
      - '.github/workflows/**'

jobs:
  policy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Conftest
        uses: instrumenta/conftest-action@master
        with:
          version: 0.48.0

      # Check Kubernetes manifests
      - name: Validate Kubernetes
        run: |
          conftest test k8s/ \
            --policy policies/kubernetes/ \
            --output json \
            > k8s-results.json

          if [ $(jq '.[] | select(.failures | length > 0)' k8s-results.json | wc -l) -gt 0 ]; then
            echo "❌ Kubernetes policy violations found"
            jq '.[] | select(.failures | length > 0)' k8s-results.json
            exit 1
          fi

      # Check Terraform
      - name: Validate Terraform
        run: |
          conftest test terraform/ \
            --policy policies/terraform/ \
            --all-namespaces

      # Check CI workflows
      - name: Validate Workflows
        run: |
          conftest test .github/workflows/ \
            --policy policies/cicd/ \
            --all-namespaces
```

### Steg 3: Cost Management och FinOps

```yaml
# .github/workflows/cost-tracking.yml
name: CI/CD Cost Tracking

on:
  workflow_run:
    workflows: ["*"]
    types: [completed]

jobs:
  track-cost:
    runs-on: ubuntu-latest

    steps:
      - name: Calculate job cost
        id: cost
        run: |
          # GitHub Actions pricing (example)
          # Linux: $0.008/min
          # macOS: $0.08/min
          # Windows: $0.016/min

          DURATION_MIN=${{ github.event.workflow_run.run_duration / 60 }}

          # Assuming Linux runner
          COST=$(echo "$DURATION_MIN * 0.008" | bc -l)

          echo "duration=$DURATION_MIN" >> $GITHUB_OUTPUT
          echo "cost=$COST" >> $GITHUB_OUTPUT

      - name: Store metrics
        run: |
          curl -X POST "${{ secrets.METRICS_ENDPOINT }}" \
            -H "Content-Type: application/json" \
            -d '{
              "metric": "cicd_cost",
              "value": ${{ steps.cost.outputs.cost }},
              "tags": {
                "repo": "${{ github.repository }}",
                "workflow": "${{ github.event.workflow_run.name }}",
                "team": "${{ github.repository_owner }}",
                "duration_min": ${{ steps.cost.outputs.duration }}
              }
            }'
```

```yaml
# .github/workflows/cost-report.yml
name: Weekly Cost Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Måndag 09:00

jobs:
  report:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_TOKEN }}
          script: |
            const org = context.repo.owner;

            // Get workflow usage for org
            const usage = await github.rest.billing.getGithubActionsOrganizationBilling({
              org: org
            });

            const report = `
            ## Weekly CI/CD Cost Report

            **Total minutes used:** ${usage.data.total_minutes_used}
            **Minutes included:** ${usage.data.included_minutes}
            **Paid minutes:** ${usage.data.total_paid_minutes_used}

            ### By Repository
            | Repository | Minutes | Est. Cost |
            |------------|---------|-----------|
            ${usage.data.minutes_used_breakdown ?
              Object.entries(usage.data.minutes_used_breakdown)
                .map(([repo, mins]) => `| ${repo} | ${mins} | $${(mins * 0.008).toFixed(2)} |`)
                .join('\n')
              : 'N/A'}

            ### Recommendations
            - Consider self-hosted runners for high-volume repos
            - Enable caching to reduce build times
            - Use path filters to skip unnecessary builds
            `;

            // Create issue with report
            await github.rest.issues.create({
              owner: org,
              repo: 'platform-reports',
              title: `Weekly CI/CD Cost Report - ${new Date().toISOString().split('T')[0]}`,
              body: report,
              labels: ['cost-report', 'automated']
            });
```

### Steg 4: DORA Metrics Collection

```yaml
# .github/workflows/dora-metrics.yml
name: DORA Metrics Collection

on:
  deployment:
  workflow_run:
    workflows: ["Deploy"]
    types: [completed]

jobs:
  collect:
    runs-on: ubuntu-latest

    steps:
      - name: Calculate DORA metrics
        id: dora
        uses: actions/github-script@v7
        with:
          script: |
            const owner = context.repo.owner;
            const repo = context.repo.repo;

            // Get deployments for last 30 days
            const thirtyDaysAgo = new Date();
            thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

            const deployments = await github.rest.repos.listDeployments({
              owner,
              repo,
              per_page: 100
            });

            const recentDeploys = deployments.data.filter(
              d => new Date(d.created_at) > thirtyDaysAgo
            );

            // Deployment Frequency
            const deployFrequency = recentDeploys.length / 30;

            // Lead Time (from commit to deploy)
            let totalLeadTime = 0;
            for (const deploy of recentDeploys) {
              const commit = await github.rest.repos.getCommit({
                owner,
                repo,
                ref: deploy.sha
              });

              const commitTime = new Date(commit.data.commit.committer.date);
              const deployTime = new Date(deploy.created_at);
              totalLeadTime += (deployTime - commitTime) / 1000 / 60 / 60; // hours
            }
            const avgLeadTime = recentDeploys.length > 0
              ? totalLeadTime / recentDeploys.length
              : 0;

            // Change Failure Rate (deploys that were rolled back)
            const failedDeploys = deployments.data.filter(d => {
              return d.statuses?.some(s => s.state === 'failure');
            }).length;
            const changeFailureRate = recentDeploys.length > 0
              ? (failedDeploys / recentDeploys.length) * 100
              : 0;

            return {
              deployFrequency: deployFrequency.toFixed(2),
              leadTimeHours: avgLeadTime.toFixed(1),
              changeFailureRate: changeFailureRate.toFixed(1)
            };

      - name: Send to metrics backend
        run: |
          curl -X POST "${{ secrets.METRICS_ENDPOINT }}" \
            -H "Content-Type: application/json" \
            -d '{
              "metrics": {
                "deployment_frequency": ${{ fromJson(steps.dora.outputs.result).deployFrequency }},
                "lead_time_hours": ${{ fromJson(steps.dora.outputs.result).leadTimeHours }},
                "change_failure_rate": ${{ fromJson(steps.dora.outputs.result).changeFailureRate }}
              },
              "repository": "${{ github.repository }}",
              "timestamp": "${{ github.event.created_at }}"
            }'

      - name: Update dashboard
        run: |
          # Update Grafana dashboard annotation
          curl -X POST "${{ secrets.GRAFANA_URL }}/api/annotations" \
            -H "Authorization: Bearer ${{ secrets.GRAFANA_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "dashboardId": 1,
              "time": '"$(date +%s)"'000,
              "text": "Deployment to production",
              "tags": ["deployment", "${{ github.repository }}"]
            }'
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Team Onboarding Automation

```yaml
# .github/workflows/onboard-team.yml
name: Onboard New Team

on:
  workflow_dispatch:
    inputs:
      team-name:
        description: 'Team name'
        required: true
        type: string
      team-lead-github:
        description: 'Team lead GitHub username'
        required: true
        type: string
      tech-stack:
        description: 'Technology stack'
        required: true
        type: choice
        options:
          - node-typescript
          - python
          - go
          - java
      environments:
        description: 'Environments needed'
        required: true
        type: choice
        options:
          - dev-only
          - dev-staging
          - dev-staging-prod

jobs:
  create-repo:
    runs-on: ubuntu-latest
    outputs:
      repo-name: ${{ steps.create.outputs.repo-name }}

    steps:
      - name: Create repository from template
        id: create
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_TOKEN }}
          script: |
            const teamName = '${{ inputs.team-name }}';
            const repoName = `${teamName}-service`;
            const techStack = '${{ inputs.tech-stack }}';

            // Template mapping
            const templates = {
              'node-typescript': 'myorg/template-node-ts',
              'python': 'myorg/template-python',
              'go': 'myorg/template-go',
              'java': 'myorg/template-java'
            };

            // Create repo from template
            const repo = await github.rest.repos.createUsingTemplate({
              template_owner: 'myorg',
              template_repo: templates[techStack].split('/')[1],
              owner: 'myorg',
              name: repoName,
              private: true,
              description: `Service for ${teamName} team`
            });

            core.setOutput('repo-name', repoName);
            return repoName;

  setup-environments:
    needs: create-repo
    runs-on: ubuntu-latest

    steps:
      - name: Configure environments
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_TOKEN }}
          script: |
            const repoName = '${{ needs.create-repo.outputs.repo-name }}';
            const envConfig = '${{ inputs.environments }}';

            const environments = {
              'dev-only': ['dev'],
              'dev-staging': ['dev', 'staging'],
              'dev-staging-prod': ['dev', 'staging', 'production']
            };

            for (const env of environments[envConfig]) {
              await github.rest.repos.createOrUpdateEnvironment({
                owner: 'myorg',
                repo: repoName,
                environment_name: env,
                deployment_branch_policy: {
                  protected_branches: env === 'production',
                  custom_branch_policies: env !== 'production'
                },
                reviewers: env === 'production' ? [
                  {
                    type: 'User',
                    id: (await github.rest.users.getByUsername({
                      username: '${{ inputs.team-lead-github }}'
                    })).data.id
                  }
                ] : []
              });

              // Add environment secrets
              // ... secret setup
            }

  setup-branch-protection:
    needs: create-repo
    runs-on: ubuntu-latest

    steps:
      - name: Configure branch protection
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ADMIN_TOKEN }}
          script: |
            const repoName = '${{ needs.create-repo.outputs.repo-name }}';

            await github.rest.repos.updateBranchProtection({
              owner: 'myorg',
              repo: repoName,
              branch: 'main',
              required_status_checks: {
                strict: true,
                contexts: ['build', 'test', 'security-scan', 'policy-check']
              },
              enforce_admins: false,
              required_pull_request_reviews: {
                dismiss_stale_reviews: true,
                require_code_owner_reviews: true,
                required_approving_review_count: 1
              },
              restrictions: null,
              required_linear_history: true,
              allow_force_pushes: false,
              allow_deletions: false
            });

  notify:
    needs: [create-repo, setup-environments, setup-branch-protection]
    runs-on: ubuntu-latest

    steps:
      - name: Send welcome notification
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "🎉 Welcome aboard, ${{ inputs.team-name }} team!",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*New Team Onboarded*\\n\\n• *Team:* ${{ inputs.team-name }}\\n• *Repository:* ${{ needs.create-repo.outputs.repo-name }}\\n• *Stack:* ${{ inputs.tech-stack }}\\n• *Environments:* ${{ inputs.environments }}\\n\\n<https://github.com/myorg/${{ needs.create-repo.outputs.repo-name }}|View Repository>"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### Exempel 2: Composite Action för Standard Build

```yaml
# .github/actions/standard-build/action.yml
name: 'Standard Build'
description: 'Organization-standard build process with all required steps'

inputs:
  language:
    description: 'Programming language'
    required: true
  version:
    description: 'Language version'
    required: false
    default: 'latest'
  cache-key:
    description: 'Custom cache key suffix'
    required: false
    default: ''

outputs:
  artifact-name:
    description: 'Name of the build artifact'
    value: ${{ steps.artifact.outputs.name }}
  build-time:
    description: 'Build duration in seconds'
    value: ${{ steps.timer.outputs.duration }}

runs:
  using: 'composite'
  steps:
    - name: Start timer
      id: start
      shell: bash
      run: echo "start=$(date +%s)" >> $GITHUB_OUTPUT

    # Node.js setup
    - name: Setup Node.js
      if: inputs.language == 'node'
      uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.version == 'latest' && '20' || inputs.version }}
        cache: 'npm'

    # Python setup
    - name: Setup Python
      if: inputs.language == 'python'
      uses: actions/setup-python@v5
      with:
        python-version: ${{ inputs.version == 'latest' && '3.12' || inputs.version }}

    - name: Cache Python dependencies
      if: inputs.language == 'python'
      uses: actions/cache@v4
      with:
        path: ~/.cache/pip
        key: pip-${{ runner.os }}-${{ inputs.version }}-${{ hashFiles('**/requirements*.txt', '**/pyproject.toml') }}-${{ inputs.cache-key }}

    # Go setup
    - name: Setup Go
      if: inputs.language == 'go'
      uses: actions/setup-go@v5
      with:
        go-version: ${{ inputs.version == 'latest' && '1.22' || inputs.version }}

    # Install dependencies
    - name: Install dependencies (Node)
      if: inputs.language == 'node'
      shell: bash
      run: npm ci

    - name: Install dependencies (Python)
      if: inputs.language == 'python'
      shell: bash
      run: |
        pip install --upgrade pip
        pip install poetry
        poetry install

    - name: Install dependencies (Go)
      if: inputs.language == 'go'
      shell: bash
      run: go mod download

    # Build
    - name: Build (Node)
      if: inputs.language == 'node'
      shell: bash
      run: npm run build

    - name: Build (Python)
      if: inputs.language == 'python'
      shell: bash
      run: poetry build

    - name: Build (Go)
      if: inputs.language == 'go'
      shell: bash
      run: go build -o dist/ ./...

    # Create artifact name
    - name: Set artifact name
      id: artifact
      shell: bash
      run: |
        NAME="build-${{ github.repository_owner }}-${{ github.event.repository.name }}-${{ github.sha }}"
        echo "name=$NAME" >> $GITHUB_OUTPUT

    # Calculate duration
    - name: Stop timer
      id: timer
      shell: bash
      run: |
        END=$(date +%s)
        DURATION=$((END - ${{ steps.start.outputs.start }}))
        echo "duration=$DURATION" >> $GITHUB_OUTPUT
```

### Exempel 3: Self-Service Environment Creation

```yaml
# .github/workflows/create-environment.yml
name: Create Environment

on:
  workflow_dispatch:
    inputs:
      environment-name:
        description: 'Environment name (e.g., feature-xyz, hotfix-123)'
        required: true
        type: string
      ttl-days:
        description: 'Time to live (days)'
        required: true
        type: choice
        options:
          - '1'
          - '3'
          - '7'
          - '14'
        default: '7'
      size:
        description: 'Environment size'
        required: true
        type: choice
        options:
          - small
          - medium
          - large

jobs:
  validate:
    runs-on: ubuntu-latest
    outputs:
      approved: ${{ steps.check.outputs.approved }}

    steps:
      - name: Check quotas
        id: check
        uses: actions/github-script@v7
        with:
          script: |
            // Check team's environment quota
            const team = '${{ github.actor }}';
            const maxEnvs = 3;

            // Get existing environments (from custom API or database)
            const existingEnvs = 1; // Example

            if (existingEnvs >= maxEnvs) {
              core.setFailed(`Team has reached maximum environments (${maxEnvs})`);
              core.setOutput('approved', 'false');
            } else {
              core.setOutput('approved', 'true');
            }

  provision:
    needs: validate
    if: needs.validate.outputs.approved == 'true'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3

      - name: Create environment
        run: |
          cd terraform/environments

          # Create environment-specific tfvars
          cat > ${{ inputs.environment-name }}.tfvars << EOF
          environment_name = "${{ inputs.environment-name }}"
          size             = "${{ inputs.size }}"
          ttl_days         = ${{ inputs.ttl-days }}
          created_by       = "${{ github.actor }}"
          created_at       = "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
          repository       = "${{ github.repository }}"
          EOF

          terraform init
          terraform workspace new ${{ inputs.environment-name }} || terraform workspace select ${{ inputs.environment-name }}
          terraform apply -var-file=${{ inputs.environment-name }}.tfvars -auto-approve

      - name: Schedule cleanup
        run: |
          # Create cleanup scheduled workflow
          cat > .github/workflows/cleanup-${{ inputs.environment-name }}.yml << 'EOF'
          name: Cleanup ${{ inputs.environment-name }}
          on:
            schedule:
              - cron: '0 0 * * *'  # Check daily
          jobs:
            cleanup:
              runs-on: ubuntu-latest
              steps:
                - name: Check TTL
                  run: |
                    CREATED="${{ github.event.created_at }}"
                    TTL_DAYS=${{ inputs.ttl-days }}
                    # ... cleanup logic
          EOF

      - name: Notify
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "🌍 Environment '${{ inputs.environment-name }}' created",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*New Environment Created*\\n• Name: ${{ inputs.environment-name }}\\n• Size: ${{ inputs.size }}\\n• TTL: ${{ inputs.ttl-days }} days\\n• Created by: ${{ github.actor }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

------------------------------------------------------------

## Bästa Praxis

### 1. Version Template Libraries

```yaml
# Använd semantic versioning för templates
# myorg/platform-templates repository

# Release workflow
name: Release Templates

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          body: |
            ## Changes in ${{ github.ref_name }}

            See [CHANGELOG.md](CHANGELOG.md) for details.
          generate_release_notes: true

# Usage i consumer repos:
# uses: myorg/platform-templates/.github/workflows/build.yml@v2
# uses: myorg/platform-templates/.github/workflows/build.yml@v2.1.0
```

### 2. Implement Progressive Rollout

```yaml
# Canary deployment med automatisk rollback
deploy-canary:
  runs-on: ubuntu-latest
  steps:
    - name: Deploy canary (10%)
      run: |
        kubectl set image deployment/${{ env.APP }} \
          app=${{ env.IMAGE }}:${{ github.sha }} \
          -n production

        kubectl patch deployment/${{ env.APP }} \
          -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge":"10%","maxUnavailable":"0"}}}}' \
          -n production

    - name: Monitor canary
      run: |
        # Vänta och observera metrics
        sleep 300

        ERROR_RATE=$(curl -s "$PROMETHEUS_URL/api/v1/query" \
          --data-urlencode 'query=rate(http_requests_total{status=~"5.."}[5m])' \
          | jq -r '.data.result[0].value[1]')

        if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
          echo "Error rate too high, rolling back"
          kubectl rollout undo deployment/${{ env.APP }} -n production
          exit 1
        fi

    - name: Full rollout
      run: |
        kubectl rollout status deployment/${{ env.APP }} -n production --timeout=10m
```

### 3. Centralize Secrets Management

```yaml
# HashiCorp Vault integration
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read

    steps:
      - name: Authenticate to Vault
        uses: hashicorp/vault-action@v2
        with:
          url: ${{ secrets.VAULT_URL }}
          method: jwt
          role: github-actions
          secrets: |
            secret/data/production/db DB_PASSWORD ;
            secret/data/production/api API_KEY ;

      - name: Deploy with secrets
        run: |
          # Secrets available as env vars
          deploy --db-password="$DB_PASSWORD" --api-key="$API_KEY"
```

### 4. Implement Audit Logging

```yaml
# Comprehensive audit logging
- name: Audit log
  if: always()
  run: |
    cat << EOF | curl -X POST "$AUDIT_ENDPOINT" -d @-
    {
      "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
      "event_type": "deployment",
      "actor": "${{ github.actor }}",
      "repository": "${{ github.repository }}",
      "workflow": "${{ github.workflow }}",
      "run_id": "${{ github.run_id }}",
      "environment": "${{ inputs.environment }}",
      "result": "${{ job.status }}",
      "commit": "${{ github.sha }}",
      "ref": "${{ github.ref }}",
      "approvers": "${{ toJson(github.event.review.user.login) }}",
      "metadata": {
        "duration_seconds": "${{ steps.timer.outputs.duration }}",
        "artifact_version": "${{ steps.build.outputs.version }}"
      }
    }
    EOF
```

------------------------------------------------------------

## Vanliga Fallgropar

### ❌ Fallgrop 1: One-Size-Fits-All Templates

```yaml
# ❌ DÅLIGT: Rigid template utan flexibilitet
jobs:
  build:
    uses: myorg/templates/.github/workflows/build.yml@v1
    # Ingen möjlighet till anpassning

# ✅ BRA: Flexibla inputs med sane defaults
jobs:
  build:
    uses: myorg/templates/.github/workflows/build.yml@v1
    with:
      node-version: '18'  # Override default
      skip-e2e: true      # Team-specific
      custom-script: './scripts/special-build.sh'
```

### ❌ Fallgrop 2: Ignoring Template Versioning

```yaml
# ❌ DÅLIGT: Pinnad till main (breaking changes)
uses: myorg/templates/.github/workflows/build.yml@main

# ❌ DÅLIGT: Ingen version alls
uses: myorg/templates/.github/workflows/build.yml

# ✅ BRA: Semantic version
uses: myorg/templates/.github/workflows/build.yml@v2
uses: myorg/templates/.github/workflows/build.yml@v2.1.0
```

### ❌ Fallgrop 3: Over-Engineering Policies

```rego
// ❌ DÅLIGT: För strikta policies som blockerar alla
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  container.image != regex.match(`^myorg-registry.com/.*:v[0-9]+\.[0-9]+\.[0-9]+$`, container.image)
  msg := "Container image must be from approved registry with semver tag"
}
// Blockerar dev/testing/debugging

// ✅ BRA: Environment-aware policies
deny[msg] {
  input.kind == "Deployment"
  input.metadata.labels.environment == "production"
  container := input.spec.template.spec.containers[_]
  not startswith(container.image, "myorg-registry.com/")
  msg := "Production containers must use approved registry"
}
// Strikt för prod, flexibelt för dev
```

### ❌ Fallgrop 4: Missing Escape Hatches

```yaml
# ❌ DÅLIGT: Ingen väg runt blockering
# All deployments måste passera ALLA checks

# ✅ BRA: Emergency override med audit
deploy-emergency:
  if: github.event.inputs.emergency == 'true'
  environment:
    name: production-emergency
    url: ${{ steps.deploy.outputs.url }}
  steps:
    - name: Require justification
      if: github.event.inputs.justification == ''
      run: |
        echo "Emergency deploys require justification"
        exit 1

    - name: Audit emergency deploy
      run: |
        curl -X POST "$AUDIT_ENDPOINT" -d '{
          "event": "emergency_deploy",
          "actor": "${{ github.actor }}",
          "justification": "${{ github.event.inputs.justification }}",
          "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
        }'

    - name: Deploy (bypassing normal gates)
      run: ./deploy.sh --force
```

------------------------------------------------------------

## Övningar

### Övning 1: Skapa Reusable Workflow Library (25 XP)

**Mål:** Bygg en central template för din organisation.

**Din uppgift:**
1. Skapa ett nytt repository `platform-templates`
2. Implementera en reusable workflow för Node.js-services
3. Inkludera: build, test, security scan, deploy
4. Lägg till inputs för språkversion och environment
5. Använd templaten i ett team-repo

<details>
<summary>Ledtråd</summary>

Använd `workflow_call` trigger och definiera inputs/outputs/secrets.

</details>

<details>
<summary>Lösning</summary>

Se Steg 1 i guiden för komplett implementation.

</details>

---

### Övning 2: Implementera Policy-as-Code (30 XP)

**Mål:** Automatisera governance med OPA/Conftest.

**Din uppgift:**
1. Installera Conftest
2. Skriv Rego-policies för Kubernetes
3. Integrera i PR-workflow
4. Blockera PRs som bryter policies
5. Lägg till undantag för dev-miljöer

<details>
<summary>Ledtråd</summary>

Använd Conftest med `--policy` flaggan. Policies kan kolla `input.metadata.labels.environment`.

</details>

<details>
<summary>Lösning</summary>

Se Steg 2 för kompletta policies och workflow integration.

</details>

---

### Övning 3: DORA Metrics Dashboard (35 XP)

**Mål:** Mät engineering effectiveness med DORA metrics.

**Din uppgift:**
1. Implementera deployment frequency tracking
2. Beräkna lead time for changes
3. Spåra change failure rate
4. Skapa en Grafana dashboard
5. Sätt upp alerting för regression

<details>
<summary>Ledtråd</summary>

Använd GitHub API för att hämta deployment och commit data. Push metrics till Prometheus/DataDog.

</details>

<details>
<summary>Lösning</summary>

Se Steg 4 för komplett DORA metrics collection workflow.

</details>

------------------------------------------------------------

## Kopplingar

### Relaterade noder i modulen:
- **Monorepo CI/CD:** Enterprise patterns för monorepos
- **Self-Hosted Runners:** Custom runners för enterprise
- **Secrets Management:** Enterprise secrets i scale
- **Compliance and Audit:** Regulatoriska krav

### Förkunskaper:
- CI/CD fundamentals
- Kubernetes basics
- Infrastructure as Code
- Policy concepts

### Bygger mot:
- Internal Developer Platform (IDP)
- Platform Engineering
- DevOps transformation
- Cloud-native enterprise

------------------------------------------------------------

## Sammanfattning

- **Platform Engineering** skapar self-service CI/CD med guardrails
- **Reusable Workflows** standardiserar pipelines över organisationen
- **Policy-as-Code** automatiserar governance och compliance
- **DORA Metrics** mäter engineering effectiveness
- **Cost Management** förhindrar CI/CD-kostnader från att skena
- **Multi-tenant** patterns skalar till hundratals team
- **Golden Paths** ger rekommenderad väg med flexibilitet
- **Audit Logging** säkerställer traceability
- Balansera autonomi med kontroll
- Templates måste versionshanteras

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `conftest test k8s/ -p policies/` | Kör policy-checks |
| `infracost diff --path=terraform/` | Estimera infra-kostnader |
| `gh api repos/{owner}/{repo}/environments` | Lista environments |
| `gh workflow run onboard.yml -f team=xxx` | Trigga onboarding |
| `kubectl rollout undo deployment/xxx` | Rollback deployment |

------------------------------------------------------------

## Referenser

- Platform Engineering: https://platformengineering.org/
- DORA Metrics: https://dora.dev/
- Open Policy Agent: https://www.openpolicyagent.org/
- Backstage IDP: https://backstage.io/
- GitHub Reusable Workflows: https://docs.github.com/en/actions/using-workflows/reusing-workflows
- Infracost: https://www.infracost.io/
- Team Topologies: https://teamtopologies.com/
""",
        },
    ],
}
