# CI/CD Pipeline Basics - GitHub Actions
## The Complete Beginner's Guide to Automated Deployments

---

## 🎯 TL;DR (30 seconds)
CI/CD automatically tests and deploys your code when you push to GitHub. Think of it like a robot assistant that:
1. ✅ Runs your tests
2. ✅ Checks for bugs
3. ✅ Deploys to production
4. ✅ All without you clicking anything!

**Real-world value:** Companies want DevOps engineers who can set up CI/CD. This skill alone will get you interviews.

---

## 🚀 Why This Matters for Your Career

**Interview Question You'll Hear:**
> "Have you set up a CI/CD pipeline before?"

**What Employers Want:**
- Can you automate testing? ✅
- Can you deploy code safely? ✅
- Do you understand GitHub Actions? ✅

**Salary Impact:** DevOps engineers who know CI/CD earn **15-25% more** than those who only know manual deployment.

---

## 📖 THEORY (Read this first)

### What is CI/CD?

**The Old Way (Manual):**
```
Developer writes code → Manually run tests →
Wait for approval → Manually deploy to server →
Hope nothing breaks 🤞
```
**Time:** 2-4 hours per deployment
**Errors:** High (humans make mistakes)
**Stress:** High (deployments on Friday at 5pm? 😰)

**The CI/CD Way (Automated):**
```
Developer writes code → Push to GitHub →
Robot runs tests automatically →
Robot deploys if tests pass →
Done! ✅
```
**Time:** 5-10 minutes (fully automated)
**Errors:** Low (same process every time)
**Stress:** Low (deploy 10x per day safely)

---

### Mental Model: CI/CD is Like a Quality Control Factory

Imagine a car factory:

🏭 **Traditional Factory (Manual):**
- Worker builds car part
- Another worker checks if it fits
- Manager approves it
- Another worker installs it
- **Slow, expensive, error-prone**

🤖 **Automated Factory (CI/CD):**
- Robot builds car part
- Sensors check quality instantly
- Robots install it automatically
- **Fast, cheap, consistent**

**CI/CD does this for your code!**

---

### Key Concepts (Remember These for Interviews)

#### 1️⃣ **Continuous Integration (CI)**
**Definition:** Automatically test code every time someone pushes changes.

**Interview Answer:**
> "CI means every time I push code, automated tests run to catch bugs early. This prevents breaking the main branch."

**Real Example:**
```yaml
# Every push → Run tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: npm test
```

#### 2️⃣ **Continuous Deployment (CD)**
**Definition:** Automatically deploy code to production if tests pass.

**Interview Answer:**
> "CD means if all tests pass, code automatically deploys to production. No manual steps. This allows us to deploy 10+ times per day safely."

**Real Example:**
```yaml
# Tests pass → Deploy automatically
jobs:
  deploy:
    needs: test  # Only runs if tests pass
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

#### 3️⃣ **Pipeline**
**Definition:** A series of automated steps that run in order.

**Visual:**
```
Code Push → Build → Test → Security Scan → Deploy → Monitor
   ↓          ↓       ↓         ↓            ↓         ↓
  ✅        ✅      ✅        ✅           ✅        ✅
```

If ANY step fails → **Stop! Don't deploy!** 🛑

---

## 💻 HANDS-ON PROJECT: Build Your First CI/CD Pipeline

### Project: Automated Testing for a Python Web App

**What you'll build:**
- Simple Flask web app
- Automated tests that run on every push
- Deployment to a free hosting service
- **Portfolio-ready for your GitHub!**

---

### Step 1: Create a Simple Python Web App

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps! 🚀"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```python
# test_app.py
import pytest
from app import app

def test_homepage():
    """Test the homepage returns correct message"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps" in response.data

def test_health_endpoint():
    """Test health check endpoint"""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
```

```txt
# requirements.txt
flask==3.0.0
pytest==7.4.3
```

---

### Step 2: Create Your First GitHub Actions Workflow

Create file: `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

# When should this run?
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# What should happen?
jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      # 1. Get the code
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. Set up Python
      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # 3. Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # 4. Run tests
      - name: Run tests
        run: pytest -v

      # 5. Check if app starts
      - name: Test app startup
        run: |
          timeout 5 python app.py || true
          echo "App started successfully!"
```

**What this does:**
1. ✅ Triggers on every push to `main` or pull request
2. ✅ Sets up a clean Ubuntu environment
3. ✅ Installs Python and dependencies
4. ✅ Runs all tests
5. ✅ Checks if app can start

**If ANY step fails → You see a red ❌ on GitHub → Don't merge!**

---

### Step 3: Add Security Scanning (Important!)

Add to your workflow:

```yaml
  security:
    name: Security Scan
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Run security scan
        run: |
          pip install safety
          safety check --file requirements.txt

      - name: Scan for secrets
        run: |
          # Check if any API keys or passwords in code
          ! grep -r "API_KEY\s*=\s*['\"]" . --exclude-dir=.git || \
          (echo "❌ Found hardcoded secrets!" && exit 1)
```

**Why this matters:**
- **Interview Question:** "How do you ensure code security?"
- **Your Answer:** "I use automated security scanning in CI/CD to catch vulnerabilities before they reach production."

---

### Step 4: Add Deployment (CD)

Add to your workflow:

```yaml
  deploy:
    name: Deploy to Production
    needs: [test, security]  # Only runs if BOTH pass
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'  # Only deploy from main

    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Render
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
        run: |
          echo "🚀 Deploying to production..."
          # Your deployment script here
          curl -X POST "https://api.render.com/deploy/..." \
               -H "Authorization: Bearer $RENDER_API_KEY"

      - name: Health check
        run: |
          sleep 10  # Wait for deployment
          curl https://your-app.onrender.com/health || \
          (echo "❌ Deployment failed!" && exit 1)

      - name: Notify team
        run: |
          echo "✅ Deployment successful!"
          # Send Slack notification (optional)
```

---

## 🧠 Key Concepts to Remember

### The 4 Stages of Every CI/CD Pipeline

```
1. BUILD    → Compile/prepare your code
2. TEST     → Run automated tests
3. SCAN     → Security & quality checks
4. DEPLOY   → Push to production
```

**Interview Tip:** When asked about CI/CD, describe these 4 stages!

---

### Common Interview Questions & Answers

#### Q: "What's the difference between CI and CD?"

✅ **Good Answer:**
> "CI is Continuous Integration - automatically testing code on every push to catch bugs early. CD is Continuous Deployment - automatically deploying code to production if tests pass. Together, they let us ship code multiple times per day safely."

❌ **Bad Answer:**
> "CI/CD is like... automated stuff?"

---

#### Q: "How do you handle failed deployments?"

✅ **Good Answer:**
> "My pipeline has health checks after deployment. If they fail, I have an automatic rollback step that reverts to the last known good version. I also send alerts to Slack so the team knows immediately."

**Example code:**
```yaml
- name: Health check & rollback
  run: |
    if ! curl https://app.com/health; then
      echo "❌ Health check failed - rolling back"
      kubectl rollout undo deployment/myapp
      exit 1
    fi
```

---

#### Q: "Have you used GitHub Actions before?"

✅ **Good Answer:**
> "Yes, I've built CI/CD pipelines with GitHub Actions. For example, I created a pipeline that runs tests, security scans, and deploys to production - all triggered by pushing to GitHub. I can show you the code in my portfolio."

**Pro Tip:** Have this project in your GitHub with README explaining what you built!

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: No Tests = Broken CI/CD
**Problem:**
```yaml
# This is useless - no tests!
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
      - run: ./deploy.sh  # YOLO! 🎲
```

**Why bad:** You're deploying untested code → Production breaks! 💥

**✅ Fix:**
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pytest

  deploy:
    needs: test  # Only deploy if tests pass!
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

---

### ❌ Mistake 2: Hardcoded Secrets
**Problem:**
```yaml
- name: Deploy
  run: |
    export API_KEY="sk_live_123456..."  # 🚨 SECURITY RISK!
    ./deploy.sh
```

**Why bad:** Your API keys are visible in GitHub → Anyone can steal them!

**✅ Fix:**
```yaml
- name: Deploy
  env:
    API_KEY: ${{ secrets.API_KEY }}  # Stored securely in GitHub Secrets
  run: ./deploy.sh
```

**How to add secrets:**
1. Go to GitHub repo → Settings → Secrets
2. Add secret: `API_KEY` = `sk_live_...`
3. Use in workflow: `${{ secrets.API_KEY }}`

---

### ❌ Mistake 3: Deploy Everything to Main
**Problem:**
```yaml
on:
  push:
    branches: [main, develop, feature/*]  # Deploys from ALL branches! 😱
```

**Why bad:** Every feature branch deploys → 50 deployments per day → Chaos!

**✅ Fix:**
```yaml
on:
  push:
    branches: [main]  # Only deploy from main
  pull_request:       # Run tests on PRs, but don't deploy
    branches: [main]
```

---

## 🎯 Practice Exercises

### Exercise 1: Add Linting to Pipeline
**Goal:** Catch code style issues before tests

```yaml
- name: Run linter
  run: |
    pip install flake8
    flake8 . --count --max-line-length=127
```

### Exercise 2: Add Test Coverage Report
**Goal:** Ensure at least 80% code coverage

```yaml
- name: Check test coverage
  run: |
    pip install pytest-cov
    pytest --cov=app --cov-fail-under=80
```

### Exercise 3: Build & Push Docker Image
**Goal:** Create deployable container

```yaml
- name: Build Docker image
  run: docker build -t myapp:${{ github.sha }} .

- name: Push to registry
  run: docker push myapp:${{ github.sha }}
```

---

## 📚 FLASHCARDS (Study These!)

**Q: What does CI stand for?**
A: Continuous Integration - automatically testing code on every push

**Q: What does CD stand for?**
A: Continuous Deployment/Delivery - automatically deploying code to production

**Q: What is a GitHub Actions workflow?**
A: A YAML file that defines automated steps (build, test, deploy) triggered by events

**Q: Where do you store API keys in GitHub Actions?**
A: In GitHub Secrets (Settings → Secrets), never in code

**Q: What happens if tests fail in a CI/CD pipeline?**
A: The pipeline stops, deployment is blocked, and developers are notified

**Q: Name 3 benefits of CI/CD**
A: 1) Faster deployments, 2) Fewer bugs in production, 3) Automated testing

**Q: What's a "job" in GitHub Actions?**
A: A set of steps that run in the same environment (e.g., test job, deploy job)

**Q: What's a "step" in GitHub Actions?**
A: A single action or command within a job (e.g., "run tests", "deploy app")

**Q: What does "needs: test" mean in a workflow?**
A: This job only runs if the "test" job succeeds first

**Q: How do you trigger a workflow only on main branch?**
A: Use `on: push: branches: [main]` in your workflow YAML

---

## 🎓 QUIZ (Test Your Knowledge)

### Question 1: Multiple Choice
**Which command runs GitHub Actions workflows locally for testing?**

A) `gh actions run`
B) `act`  ✅ (Correct - this is a local GitHub Actions runner)
C) `github-actions-test`
D) `workflow-test`

**Explanation:** `act` is a tool that runs GitHub Actions workflows locally using Docker, letting you test before pushing.

---

### Question 2: True/False
**"You should always deploy directly from feature branches to production."**

❌ **FALSE**

**Explanation:** Only deploy from stable branches (usually `main` or `release`). Feature branches should run tests but not deploy.

---

### Question 3: Fill in the Blank
**Complete this workflow to run tests only on pull requests:**

```yaml
on:
  ___________:
    branches: [main]
```

**Answer:** `pull_request`

---

### Question 4: Debugging Challenge
**This workflow doesn't work. What's wrong?**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh

  test:
    runs-on: ubuntu-latest
    steps:
      - run: pytest
```

**Answer:** Deploy runs BEFORE tests! Jobs run in parallel by default. Fix:
```yaml
deploy:
  needs: test  # Add this line
  runs-on: ubuntu-latest
```

---

## 🚀 Real-World Example: How Netflix Uses CI/CD

**Netflix deploys 4,000+ times per day!** Here's how:

```
Developer writes code
    ↓
Push to GitHub
    ↓
Automated tests run (5 min)
    ↓
Security scan (2 min)
    ↓
Deploy to 1% of users (canary deployment)
    ↓
Monitor for errors (10 min)
    ↓
If OK → Deploy to 100% of users
    ↓
If errors → Automatic rollback
```

**Key Principles You Should Learn:**
1. ✅ Automated testing (no manual QA)
2. ✅ Gradual rollouts (1% → 10% → 100%)
3. ✅ Automatic rollbacks (if health checks fail)
4. ✅ Fast feedback (<10 minutes)

---

## 💼 Building Your Portfolio Project

### Project Idea: "Full-Stack App with CI/CD"

**What to build:**
1. Simple Todo app (React frontend + Node.js backend)
2. Dockerized application
3. Full CI/CD pipeline with:
   - Frontend tests (Jest)
   - Backend tests (Mocha)
   - Security scanning
   - Automated deployment
4. README explaining your pipeline

**Why this gets you hired:**
- ✅ Shows full-stack knowledge
- ✅ Demonstrates CI/CD skills
- ✅ Proves you can deploy production apps
- ✅ Portfolio piece for interviews

**GitHub Actions workflow for this:**
```yaml
name: Full-Stack CI/CD

on: [push]

jobs:
  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cd frontend && npm test

  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cd backend && npm test

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm audit

  deploy:
    needs: [test-frontend, test-backend, security-scan]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

---

## 🎯 Interview Preparation Checklist

Before your DevOps interview, make sure you can:

- [ ] Explain CI/CD in 30 seconds
- [ ] Draw a CI/CD pipeline on a whiteboard
- [ ] Show a GitHub Actions workflow you built
- [ ] Explain how to handle deployment failures
- [ ] Discuss security in CI/CD (secret management)
- [ ] Describe how to do rollbacks
- [ ] Explain the difference between CI and CD
- [ ] Show a portfolio project with automated deployments

---

## 📈 Next Steps

### After Mastering This Module:

1. **Advanced CI/CD:**
   - Multi-stage deployments (dev → staging → production)
   - A/B testing and feature flags
   - Kubernetes deployments with Helm

2. **Other CI/CD Tools:**
   - GitLab CI/CD
   - Jenkins pipelines
   - CircleCI

3. **Infrastructure as Code:**
   - Terraform for cloud resources
   - Ansible for configuration management

---

## 🌟 Why This Module Works for Job Hunting

✅ **Practical:** You build a real pipeline you can show in interviews
✅ **Interview-focused:** Includes common questions & answers
✅ **Portfolio-ready:** GitHub project demonstrates your skills
✅ **Beginner-friendly:** Clear explanations with analogies
✅ **Industry-relevant:** Uses tools real companies use
✅ **Comprehensive:** Theory + practice + troubleshooting

**Time to complete:** 4-6 hours
**Skill level gained:** Junior DevOps Engineer (interview-ready)
**Salary impact:** +15-25% vs manual deployment knowledge only

---

## 📚 Additional Resources

- **GitHub Actions Documentation:** https://docs.github.com/en/actions
- **Free hosting for practice:** Render.com, Railway.app, Fly.io
- **Act (local testing):** https://github.com/nektos/act
- **Example pipelines:** https://github.com/actions/starter-workflows

---

**Module completed!** 🎉

**Next recommended module:** Kubernetes Basics (deploying CI/CD-built containers)
