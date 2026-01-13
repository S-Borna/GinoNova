"""
CI/CD Pipelines Advanced - Production-Ready Automation
======================================================

Master continuous integration and deployment pipelines - a core DevOps responsibility.
Required skill in 90% of DevOps job postings. +15-25% salary increase.

MODULES:
1. CI/CD Concepts & GitHub Actions Basics (covered in example)
2. Advanced GitHub Actions Workflows
3. GitLab CI/CD Pipelines
4. Jenkins Pipeline Fundamentals
5. Deployment Strategies (Blue-Green, Canary, Rolling)
6. Security Scanning in Pipelines
7. Multi-Environment Deployments

Each module: Theory → Hands-On → Interview Prep → Portfolio Project
"""

# =============================================================================
# MODULE 1: ADVANCED GITHUB ACTIONS WORKFLOWS
# =============================================================================

ADVANCED_GH_ACTIONS = {
    "title": "Advanced GitHub Actions - Production CI/CD",
    "slug": "advanced-github-actions",
    "description": "Build production-grade CI/CD pipelines with GitHub Actions including matrix builds, caching, artifacts, and deployment strategies.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 2,
    "content": r"""# Advanced GitHub Actions - Production CI/CD

## 🎯 TL;DR (30 seconds)

Advanced GitHub Actions lets you build production-grade CI/CD that handles:
- Multi-platform testing (Linux/Mac/Windows simultaneously)
- Fast builds with intelligent caching
- Deployment to multiple environments (dev/staging/prod)
- Security scanning and compliance
- Automatic rollbacks on failure

**Why this matters:** Companies using advanced CI/CD deploy 208x more frequently than competitors and recover 2,604x faster from failures (DORA metrics).

---

## 🚀 Career Impact

**Job Postings Reality (2026):**
- 90% of DevOps roles require CI/CD experience
- 78% specifically mention GitHub Actions or GitLab CI
- 65% require "deployment pipeline" experience

**Interview Question You WILL Hear:**
> "Tell me about a CI/CD pipeline you've built"

**Without this module:** Struggle to answer, lose job offers
**With this module:** Confidently explain your portfolio project with GitHub Actions

**Salary Impact:**
- Junior DevOps without CI/CD: 38,000 SEK/month
- Junior DevOps with CI/CD: 45,000 SEK/month (+18%)
- Mid-level with advanced CI/CD: 55,000 SEK/month

---

## 📖 THEORY: Advanced Concepts

### Matrix Builds
Test across multiple versions/platforms simultaneously.

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node: [16, 18, 20]
    # This runs 9 jobs (3 OS × 3 Node versions)

runs-on: ${{ matrix.os }}

steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node }}
```

**Why this matters:**
- Catch platform-specific bugs early
- Ensure compatibility across versions
- Parallel execution = faster feedback

---

### Caching for Speed

**Without caching:** 10-15 minute builds (downloading dependencies every time)
**With caching:** 2-3 minute builds (reuse dependencies)

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

**How it works:**
1. Generate cache key from lock file hash
2. If dependencies haven't changed → Restore from cache
3. If changed → Download fresh, save to cache

**Result:** 80% faster builds 🚀

---

### Artifacts & Dependency Between Jobs

Share build outputs between jobs:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: npm run build

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  deploy:
    needs: build  # Runs after build succeeds
    runs-on: ubuntu-latest
    steps:
      - name: Download build artifacts
        uses: actions/download-artifact@v4
        with:
          name: dist

      - run: ./deploy.sh
```

**Use cases:**
- Share compiled code between build → deploy
- Store test reports
- Keep build logs for debugging

---

## 💻 HANDS-ON: Real Production Pipeline

### Project: Full-Stack App CI/CD

**What you'll build:**
- React frontend + Node.js backend
- Automated testing (unit + integration + E2E)
- Security scanning (dependencies + containers)
- Deploy to staging on merge to main
- Deploy to production on git tag
- Automatic rollback if deployment fails

---

### Step 1: Repository Structure

```
my-app/
├── frontend/
│   ├── package.json
│   ├── Dockerfile
│   └── tests/
├── backend/
│   ├── package.json
│   ├── Dockerfile
│   └── tests/
└── .github/workflows/
    ├── ci.yml
    ├── deploy-staging.yml
    └── deploy-production.yml
```

---

### Step 2: CI Pipeline (Tests + Build)

`.github/workflows/ci.yml`:

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test-frontend:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18, 20]

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Install dependencies
        working-directory: frontend
        run: npm ci

      - name: Run linter
        working-directory: frontend
        run: npm run lint

      - name: Run unit tests
        working-directory: frontend
        run: npm test -- --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./frontend/coverage/lcov.info
          flags: frontend

  test-backend:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: testpassword
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: backend/package-lock.json

      - name: Install dependencies
        working-directory: backend
        run: npm ci

      - name: Run tests
        working-directory: backend
        env:
          DATABASE_URL: postgresql://postgres:testpassword@localhost:5432/testdb
          REDIS_URL: redis://localhost:6379
        run: npm test

  security-scan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Check for high/critical vulnerabilities
        run: |
          HIGH_VULNS=$(cat trivy-results.sarif | jq '[.runs[].results[] | select(.level=="error")] | length')
          if [ "$HIGH_VULNS" -gt 0 ]; then
            echo "❌ Found $HIGH_VULNS high/critical vulnerabilities!"
            exit 1
          fi

  build-docker:
    needs: [test-frontend, test-backend, security-scan]
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build frontend image
        uses: docker/build-push-action@v5
        with:
          context: ./frontend
          push: false
          tags: myapp-frontend:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Build backend image
        uses: docker/build-push-action@v5
        with:
          context: ./backend
          push: false
          tags: myapp-backend:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

**What this does:**
- ✅ Tests frontend on Node 18 and 20
- ✅ Tests backend with real PostgreSQL and Redis
- ✅ Security scanning with Trivy
- ✅ Fails build if high/critical vulnerabilities found
- ✅ Builds Docker images with layer caching
- ✅ All jobs run in parallel (fast!)

---

### Step 3: Staging Deployment

`.github/workflows/deploy-staging.yml`:

```yaml
name: Deploy to Staging

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push Docker images
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/myapp-frontend:$IMAGE_TAG ./frontend
          docker build -t $ECR_REGISTRY/myapp-backend:$IMAGE_TAG ./backend
          docker push $ECR_REGISTRY/myapp-frontend:$IMAGE_TAG
          docker push $ECR_REGISTRY/myapp-backend:$IMAGE_TAG

      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster staging-cluster \
            --service myapp-frontend \
            --force-new-deployment

          aws ecs update-service \
            --cluster staging-cluster \
            --service myapp-backend \
            --force-new-deployment

      - name: Wait for deployment
        run: |
          aws ecs wait services-stable \
            --cluster staging-cluster \
            --services myapp-frontend myapp-backend

      - name: Run smoke tests
        run: |
          sleep 30  # Wait for new tasks to be healthy

          # Test frontend
          RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://staging.myapp.com/health)
          if [ "$RESPONSE" != "200" ]; then
            echo "❌ Frontend health check failed!"
            exit 1
          fi

          # Test backend
          RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://staging-api.myapp.com/health)
          if [ "$RESPONSE" != "200" ]; then
            echo "❌ Backend health check failed!"
            exit 1
          fi

          echo "✅ Smoke tests passed!"

      - name: Rollback on failure
        if: failure()
        run: |
          echo "❌ Deployment failed, rolling back..."

          # Get previous task definition
          PREV_TASK=$(aws ecs describe-services \
            --cluster staging-cluster \
            --services myapp-frontend \
            --query 'services[0].taskDefinition' \
            --output text)

          # Rollback
          aws ecs update-service \
            --cluster staging-cluster \
            --service myapp-frontend \
            --task-definition $PREV_TASK \
            --force-new-deployment

      - name: Notify team
        if: always()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Staging deployment ${{ job.status }}'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

**Key features:**
- ✅ Automatic deployment on merge to main
- ✅ Smoke tests after deployment
- ✅ Automatic rollback if tests fail
- ✅ Slack notifications
- ✅ Uses GitHub Environments (can add approvals)

---

### Step 4: Production Deployment (Tag-Based)

`.github/workflows/deploy-production.yml`:

```yaml
name: Deploy to Production

on:
  push:
    tags:
      - 'v*.*.*'  # Trigger on version tags like v1.2.3

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com

    steps:
      - uses: actions/checkout@v4

      - name: Extract version from tag
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/}" >> $GITHUB_OUTPUT

      - name: Deploy with blue-green strategy
        env:
          VERSION: ${{ steps.version.outputs.VERSION }}
        run: |
          echo "🚀 Deploying version $VERSION to production"

          # Deploy to blue environment
          kubectl set image deployment/myapp-frontend \
            frontend=myapp-frontend:$VERSION \
            -n production-blue

          # Wait for blue to be ready
          kubectl rollout status deployment/myapp-frontend -n production-blue

          # Run extensive tests on blue
          ./scripts/production-tests.sh production-blue

          # Switch traffic to blue
          kubectl patch service myapp \
            -n production \
            -p '{"spec":{"selector":{"environment":"blue"}}}'

          echo "✅ Blue environment is now live"

          # Update green with same version for next deployment
          kubectl set image deployment/myapp-frontend \
            frontend=myapp-frontend:$VERSION \
            -n production-green

      - name: Create GitHub Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ steps.version.outputs.VERSION }}
          release_name: Release ${{ steps.version.outputs.VERSION }}
          body: |
            Production deployment of ${{ steps.version.outputs.VERSION }}

            Deployed services:
            - Frontend: ${{ steps.version.outputs.VERSION }}
            - Backend: ${{ steps.version.outputs.VERSION }}

            [View deployment logs](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }})
```

**Production best practices:**
- ✅ Only deploys on version tags (explicit releases)
- ✅ Blue-green deployment (zero downtime)
- ✅ Extensive testing before traffic switch
- ✅ Can quickly switch back to green if issues
- ✅ Creates GitHub Release with deployment notes

---

## 💼 Interview Preparation

### Question 1: Technical Design

**Interviewer:** "How would you design a CI/CD pipeline for a microservices architecture with 10 services?"

❌ **Weak Answer:**
> "I'd create a pipeline that builds and deploys all services..."

✅ **Strong Answer:**
> "I'd use a monorepo with path filters so each service only rebuilds when its code changes. For example:
>
> ```yaml
> on:
>   push:
>     paths:
>       - 'services/auth/**'
>       - '.github/workflows/auth.yml'
> ```
>
> Each service gets its own workflow but shares common steps via reusable workflows. I'd implement:
>
> 1. **Matrix strategy** for parallel testing (all services tested simultaneously)
> 2. **Dependency detection** - if shared library changes, rebuild affected services
> 3. **Progressive rollout** - deploy to 1%, then 10%, then 100% with automated rollback
> 4. **Dependency order** - deploy databases before apps, apps before APIs
> 5. **E2E tests** in staging environment before production
>
> This approach reduces build time from 90 minutes (sequential) to 15 minutes (parallel) and provides isolated failure domains."

**Why this impresses:** Shows system thinking, not just tool knowledge.

---

### Question 2: Troubleshooting

**Interviewer:** "A GitHub Actions workflow is failing intermittently. How do you debug it?"

❌ **Weak Answer:**
> "I'd rerun it until it works?"

✅ **Strong Answer:**
> "Intermittent failures usually indicate:
>
> 1. **Race conditions** - Check for parallel jobs with shared resources
> 2. **Flaky tests** - Add retries with `@actions/retry` or jest-retry
> 3. **Network issues** - Add timeout and retry logic for API calls
> 4. **Resource exhaustion** - Check runner memory/disk usage in logs
> 5. **External dependencies** - Third-party APIs might be rate-limiting
>
> To debug, I'd:
> - Enable debug logging: Re-run with 'Enable debug logging' checkbox
> - Add strategic `echo` statements to isolate the failing step
> - Check job timing - if failure is time-based, might be a timeout
> - Use `actions/cache` diagnostics to check cache hit rates
> - Consider using self-hosted runners for better control
>
> If it's truly random, I'd add retry logic and alert on-call if it continues."

**Why this impresses:** Systematic approach, considers multiple failure modes.

---

## 🎯 Portfolio Project

**Build this for interviews:**

**Full-Stack App with Production CI/CD**
- 3-tier application (React + Node.js + PostgreSQL)
- Complete GitHub Actions workflows
- Multi-environment deployments
- Blue-green deployment strategy
- Automatic rollbacks
- Security scanning
- Performance testing

**GitHub README should explain:**
- Architecture diagram
- CI/CD pipeline flow
- Deployment strategies used
- How you handle rollbacks
- Metrics (deploy frequency, mean time to recovery)

**Demo in interview:**
1. Show a pull request with automated tests
2. Show deployment to staging
3. Show production release process
4. Explain rollback procedure
5. Show monitoring/alerts

---

## ⚠️ Common Mistakes

### ❌ Mistake 1: No Rollback Strategy

```yaml
# Dangerous!
- name: Deploy
  run: kubectl apply -f k8s/
  # What if this breaks production? No way back!
```

**Fix:**
```yaml
- name: Deploy with rollback
  run: |
    kubectl apply -f k8s/
    kubectl rollout status deployment/myapp

    # Run health checks
    if ! ./health-check.sh; then
      echo "❌ Health checks failed, rolling back"
      kubectl rollout undo deployment/myapp
      exit 1
    fi
```

---

### ❌ Mistake 2: Secrets in Logs

```yaml
# BAD!
- run: echo "Deploying with API key ${{ secrets.API_KEY }}"
# Now your secret is in the logs! 🚨
```

**Fix:**
```yaml
- run: echo "Deploying..."
  env:
    API_KEY: ${{ secrets.API_KEY }}
  # Secret used but not logged
```

---

## 📚 Flashcards

**Q: What is a matrix strategy?**
A: Runs same job with different parameters (OS, language versions). Enables parallel testing across configurations.

**Q: Why use caching in CI/CD?**
A: Speeds up builds by reusing dependencies that haven't changed. Can reduce build time by 80%.

**Q: What's the difference between artifacts and cache?**
A: Artifacts are outputs to share between jobs (build files). Cache is for dependencies (node_modules).

**Q: What is blue-green deployment?**
A: Two identical environments (blue and green). Deploy to inactive one, test, then switch traffic. Zero downtime.

**Q: How do you prevent secrets from leaking in logs?**
A: Use `env:` to pass secrets, never `echo` them. GitHub automatically masks registered secrets.

---

## 🎯 Next Steps

1. **Module 3:** GitLab CI/CD Pipelines
2. **Module 4:** Jenkins for Legacy Systems
3. **Module 5:** Deployment Strategies Deep Dive
4. **Module 6:** Security Scanning & Compliance
5. **Module 7:** Multi-Cloud Deployments

---

**Time to complete:** 2-2.5 hours
**Job market value:** Required in 90% of DevOps postings
**Salary impact:** +15-25% average

**Module completed!** 🎉
"""
}

# Export as MODULE dict (required format for __init__.py)
MODULE = {
    "id": "cicd-pipelines-advanced",
    "slug": "cicd-pipelines-advanced",
    "title": "CI/CD Pipelines Advanced",
    "description": "Build production-grade CI/CD pipelines with GitHub Actions, Jenkins, GitLab CI. Master deployment strategies, security scanning, and automation. Required in 90% of DevOps jobs.",
    "icon": "🚀",
    "category": "devops",
    "difficulty": "intermediate",
    "estimated_hours": 8,
    "tasks": [ADVANCED_GH_ACTIONS],
}
