"""
DevSecOps - Security in DevOps Practices
=========================================

Master DevSecOps: security scanning, vulnerability management, secrets management,
compliance automation, and security-first CI/CD. Shift left on security.
"""

DEVSECOPS_FUNDAMENTALS = {
    "title": "DevSecOps - Security Automation & Best Practices",
    "slug": "devsecops-practices",
    "description": "Master DevSecOps for production: security scanning, SAST/DAST, secrets management, compliance automation, and security-first CI/CD pipelines. Shift security left.",
    "difficulty": "advanced",
    "estimated_minutes": 130,
    "xp_reward": 220,
    "order_index": 1,
    "content": r"""# DevSecOps - Security Automation & Best Practices

## 🎯 TL;DR (30 seconds)

DevSecOps integrates security into every stage of development: code scanning, container scanning, infrastructure scanning,
secrets management, and compliance automation. Catch vulnerabilities before production. Required in 70% of enterprise DevOps roles.

**Why this matters:** Security breaches cost millions. DevSecOps catches vulnerabilities early when they're cheap to fix.
Manual security reviews are too slow - automate it.

---

## 🚀 Why DevSecOps for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 70% of Enterprise DevOps roles require security skills
- 85% of FinTech/Healthcare DevOps require DevSecOps
- 60% of Senior DevOps mention security automation

**Salary Impact (Sweden):**
| Role | Without Security | With DevSecOps | Difference |
|------|-----------------|----------------|------------|
| DevOps Engineer | 45,000 SEK | 55,000 SEK | **+22%** |
| Security Engineer | 52,000 SEK | 65,000 SEK | **+25%** |
| Senior SRE | 60,000 SEK | 75,000 SEK | **+25%** |

**Reality:** Security is no longer optional. Companies face regulations (GDPR, SOC2, ISO27001).

---

## 📖 THEORY: What is DevSecOps?

### Traditional Security vs DevSecOps

**Traditional (Security at end):**
```
Dev → Test → QA → Security Review (2 weeks) → Deploy
                       ↑
                  Find critical vuln
                  Send back to Dev
                  Delay release by 3 weeks
```

**DevSecOps (Security throughout):**
```
Dev → Commit → [Auto Scan] → Build → [Container Scan] → Deploy
                    ↓                        ↓
              Block if critical        Block if high risk
              Fix immediately           Security gates pass
```

**Result:** Find issues early = cheaper, faster fixes.

---

### DevSecOps Pillars

1. **SAST** (Static Analysis) - Scan code for vulnerabilities
2. **DAST** (Dynamic Analysis) - Test running application
3. **SCA** (Software Composition Analysis) - Scan dependencies
4. **Container Scanning** - Scan Docker images
5. **IaC Scanning** - Scan Terraform/Kubernetes configs
6. **Secrets Management** - Never commit passwords/keys
7. **Compliance Automation** - Automated audits

---

## 🛠️ HANDS-ON: SAST with SonarQube

### Step 1: Run SonarQube

```bash
docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  sonarqube:community

# Access: http://localhost:9000
# Default login: admin/admin
```

---

### Step 2: Scan Python Project

**Install scanner:**
```bash
# Download sonar-scanner
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1-linux.zip
unzip sonar-scanner-cli-5.0.1-linux.zip
export PATH=$PATH:$PWD/sonar-scanner-5.0.1-linux/bin
```

**Create `sonar-project.properties`:**
```properties
sonar.projectKey=myapp
sonar.projectName=My Application
sonar.projectVersion=1.0
sonar.sources=src
sonar.python.version=3.10
sonar.host.url=http://localhost:9000
sonar.login=your_token_here
```

**Run scan:**
```bash
sonar-scanner
```

**View results:** http://localhost:9000/dashboard?id=myapp

**Findings:**
- Code smells
- Bugs
- Security vulnerabilities
- Code coverage

---

## 🎓 Dependency Scanning (SCA)

### Scan Python Dependencies

**Install Safety:**
```bash
pip install safety
```

**Scan for known vulnerabilities:**
```bash
# Generate requirements
pip freeze > requirements.txt

# Scan
safety check -r requirements.txt

# Output:
# +==============================================================================+
# |                                                                              |
# |                               /$$$$$$  /$$$$$$                               |
# |                              /$$__  $$|_  $$_/                               |
# |           /$$$$$$$  /$$$$$$ | $$  \__/  | $$                                |
# |          /$$_____/ |____  $$| $$$$$$    | $$                                |
# |         |  $$$$$$   /$$$$$$$| $$__  $$  | $$                                |
# |          \____  $$ /$$__  $$| $$  \ $$  | $$                                |
# |          /$$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$                              |
# |         |_______/  \_______/|__/  |__/|______/                              |
# |                                                                              |
# |  REPORT                                                                      |
# |                                                                              |
# |  ❌ 3 vulnerabilities found                                                 |
# |                                                                              |
# |  📦 requests v2.25.0                                                         |
# |  🔴 CVE-2023-32681: CRITICAL                                                |
# |  Upgrade to requests>=2.31.0                                                |
# +==============================================================================+
```

---

### Scan Node.js Dependencies

```bash
# Audit dependencies
npm audit

# Fix automatically
npm audit fix

# Force fix (may break things)
npm audit fix --force
```

---

## 🎓 Container Image Scanning

### Scan with Trivy

**Install Trivy:**
```bash
# Ubuntu/Debian
wget https://github.com/aquasecurity/trivy/releases/download/v0.48.0/trivy_0.48.0_Linux-64bit.deb
sudo dpkg -i trivy_0.48.0_Linux-64bit.deb

# Or Docker
alias trivy="docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy"
```

**Scan Docker image:**
```bash
trivy image nginx:latest

# Output:
# nginx:latest (alpine 3.18.4)
# ============================
# Total: 2 (HIGH: 1, CRITICAL: 1)
#
# ┌───────────────┬──────────────────┬──────────┬───────────────────┬─────────────────┐
# │   Library     │  Vulnerability   │ Severity │ Installed Version │  Fixed Version  │
# ├───────────────┼──────────────────┼──────────┼───────────────────┼─────────────────┤
# │ openssl       │ CVE-2023-5678    │ CRITICAL │ 3.1.1             │ 3.1.4           │
# │ curl          │ CVE-2023-1234    │ HIGH     │ 8.1.0             │ 8.1.2           │
# └───────────────┴──────────────────┴──────────┴───────────────────┴─────────────────┘
```

**Scan and block if critical:**
```bash
# Exit code 1 if CRITICAL found
trivy image --exit-code 1 --severity CRITICAL myapp:latest

# Use in CI/CD to block builds
```

---

## 🔐 Secrets Management

### Problem: Hardcoded Secrets

**❌ NEVER DO THIS:**
```python
# BAD: Secrets in code
DATABASE_URL = "postgresql://admin:SuperSecret123@db.example.com:5432/prod"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
API_KEY = "sk_live_51H1234567890abcdef"

# This WILL leak to GitHub!
```

---

### Solution 1: Environment Variables

```python
# GOOD: Use environment variables
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
API_KEY = os.environ.get('API_KEY')
```

**Set in Kubernetes:**
```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    env:
    - name: DATABASE_URL
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: url
```

---

### Solution 2: Vault (Next Module)

```python
# Use HashiCorp Vault
import hvac

client = hvac.Client(url='http://vault:8200')
secret = client.secrets.kv.v2.read_secret_version(path='myapp/database')
DATABASE_URL = secret['data']['data']['url']
```

---

### Scan for Leaked Secrets

**Install Gitleaks:**
```bash
docker pull zricethezav/gitleaks:latest
```

**Scan repository:**
```bash
# Scan current repo
docker run -v $(pwd):/path zricethezav/gitleaks:latest detect --source="/path" -v

# Output:
# ○
# │╲
# │ ○
# ○ ░
# ░    gitleaks
#
# Finding:     AWS Access Key
# Secret:      AKIAIOSFODNN7EXAMPLE
# RuleID:      aws-access-key
# Entropy:     3.854272
# File:        config/settings.py
# Line:        42
# Commit:      a1b2c3d4
# Date:        2026-01-10
# Fingerprint: a1b2c3d4:config/settings.py:aws-access-key:42
```

**Pre-commit hook (prevent commits with secrets):**
```bash
# .git/hooks/pre-commit
#!/bin/bash
gitleaks protect --staged --verbose --exit-code 1
```

---

## 🎓 Infrastructure as Code (IaC) Scanning

### Scan Terraform with tfsec

**Install tfsec:**
```bash
curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash
```

**Scan Terraform code:**
```bash
tfsec .

# Output:
# Result #1 CRITICAL S3 bucket does not have encryption enabled
# ──────────────────────────────────────────────────────────────────
#   main.tf:10-15
#   ──────────────────────────────────────────────────────────────
#    10   resource "aws_s3_bucket" "data" {
#    11     bucket = "my-data-bucket"
#    12     # Missing: server_side_encryption_configuration
#    13   }
#   ──────────────────────────────────────────────────────────────
#   Impact:     Data is not encrypted at rest
#   Resolution: Enable bucket encryption
```

**Fix:**
```hcl
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
```

---

### Scan Kubernetes with kubesec

```bash
# Install
docker pull kubesec/kubesec:v2

# Scan
docker run -i kubesec/kubesec:v2 scan /dev/stdin < deployment.yaml

# Output:
# [
#   {
#     "score": -30,
#     "critical": [
#       {
#         "selector": "containers[] .securityContext .privileged == true",
#         "reason": "Privileged containers can access all devices"
#       }
#     ],
#     "advise": [
#       {
#         "selector": ".spec .securityContext .runAsNonRoot",
#         "reason": "Force the running image to run as a non-root user"
#       }
#     ]
#   }
# ]
```

---

## 🎓 CI/CD Security Pipeline

### GitHub Actions Security Pipeline

**`.github/workflows/security.yml`:**
```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  secrets-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for Gitleaks

      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/secrets

  dependency-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Safety (Python)
        run: |
          pip install safety
          safety check -r requirements.txt

      - name: Run npm audit (Node)
        run: npm audit --audit-level=moderate

  container-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Scan with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myapp:${{ github.sha }}'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'  # Fail build if critical found

      - name: Upload results to GitHub
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  iac-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Scan Terraform
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          soft_fail: false  # Fail on issues
```

---

## 🎤 Interview Questions & Answers

### Question 1: Shift Left

**Interviewer:** "What does 'shift left' mean in DevSecOps?"

❌ **Weak Answer:**
> "Move security earlier."

✅ **Strong Answer:**
> "Shift left means integrating security into early development stages rather than at the end. Implement: 1) SAST scans in IDE/pre-commit hooks. 2) Dependency scanning in CI/CD. 3) Security training for developers. 4) Threat modeling during design. Benefits: Cheaper to fix (10x cheaper than production), faster releases (no late-stage blocks), better quality. Challenge: Need automation - can't slow down dev velocity. Use tools like Semgrep, Trivy, pre-commit hooks."

**Why this impresses:** Shows understanding of philosophy and implementation.

---

### Question 2: Vulnerability Triage

**Interviewer:** "Scanner found 500 vulnerabilities. How do you prioritize?"

❌ **Weak Answer:**
> "Fix critical first."

✅ **Strong Answer:**
> "Triage by: 1) Severity - CRITICAL > HIGH > MEDIUM > LOW. 2) Exploitability - is there public exploit? 3) Exposure - is vulnerable component internet-facing? 4) Business impact - does it affect core functionality? Focus on: High-severity + easily exploitable + exposed = fix immediately. Low-severity + no exploit + internal = schedule for later. Use CVSS scores but don't blindly trust - add business context. Set SLAs: Critical = 24h, High = 7 days, Medium = 30 days."

**Why this impresses:** Demonstrates practical risk management.

---

## 📚 Flashcards

**Q: What is SAST?**
A: Static Application Security Testing - scan source code for vulnerabilities.

**Q: What is DAST?**
A: Dynamic Application Security Testing - test running application.

**Q: What is SCA?**
A: Software Composition Analysis - scan third-party dependencies.

**Q: What is CVE?**
A: Common Vulnerabilities and Exposures - standardized vulnerability ID.

**Q: What is CVSS?**
A: Common Vulnerability Scoring System - severity rating 0-10.

**Q: What is shift left?**
A: Move security testing earlier in development cycle.

---

## 🎓 Quiz

### Question 1

**Which tool scans Docker images for vulnerabilities?**

A) Gitleaks
B) Trivy ✅
C) Safety
D) SonarQube

**Answer:** B ✅

**Explanation:** Trivy scans container images, Gitleaks scans for secrets, Safety scans Python deps.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **DevSecOps expertise** - Required in 70% of enterprise roles
✅ **Security automation** - Shift security left with confidence
✅ **Compliance knowledge** - Meet regulatory requirements
✅ **Tool mastery** - SAST, DAST, SCA, container scanning
✅ **Interview confidence** - Answer security questions expertly

**Time to complete:** 2.5 hours
**Job market impact:** Required in 70% of enterprise DevOps
**Salary boost:** +22-25% average
**Career protection:** Security is non-negotiable now

---

**Module completed!** 🎉

**Next recommended:** HashiCorp Vault - Secrets management mastery
"""
}

# Export as MODULE dict
MODULE = {
    "id": "security-devsecops",
    "slug": "security-devsecops",
    "title": "DevSecOps Practices",
    "description": "Master DevSecOps for production: security scanning, SAST/DAST, secrets management, compliance automation, and security-first CI/CD. Shift security left.",
    "icon": "🔒",
    "category": "security",
    "difficulty": "advanced",
    "estimated_hours": 12,
    "tasks": [DEVSECOPS_FUNDAMENTALS],
}
