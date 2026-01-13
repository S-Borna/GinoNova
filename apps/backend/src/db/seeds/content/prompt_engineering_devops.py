"""
Prompt Engineering for DevOps - Master AI-Powered Workflows
===========================================================

Learn to 10x your productivity using ChatGPT, GitHub Copilot, and AI tools for DevOps tasks.
This is the most valuable emerging skill - gives you a massive competitive advantage.

MODULES:
1. Prompt Engineering Fundamentals
2. AI for Infrastructure as Code (Terraform/CloudFormation)
3. AI for Kubernetes YAML Generation
4. AI-Powered Bash Scripting
5. Debugging with AI Assistants
6. AI for Documentation & Runbooks
7. Advanced: Custom GPT for Your Infrastructure

Outcome: 10x faster at writing code, debugging issues, and solving problems.
"""

# =============================================================================
# MODULE 1: PROMPT ENGINEERING FUNDAMENTALS
# =============================================================================

PROMPT_FUNDAMENTALS = {
    "title": "Prompt Engineering Fundamentals for DevOps",
    "slug": "prompt-engineering-basics",
    "description": "Master the art of communicating with AI to 10x your DevOps productivity. Learn proven patterns that get you perfect code, configs, and solutions on the first try.",
    "difficulty": "beginner",
    "estimated_minutes": 75,
    "xp_reward": 150,
    "order_index": 1,
    "content": r"""# Prompt Engineering Fundamentals for DevOps

## 🎯 TL;DR (30 seconds)

Prompt engineering is the skill of asking AI tools the right questions to get perfect results. Instead of spending 2 hours writing Terraform code, you can get AI to generate 90% of it in 30 seconds - then you review and adjust.

**Reality:** DevOps engineers who master prompt engineering are **10x more productive** and can tackle problems they couldn't before.

---

## 🚀 Why This Skill is a Game-Changer

### The Productivity Revolution

**Traditional DevOps Work:**
```
Task: Write Terraform for AWS VPC with 2 subnets, NAT gateway, route tables
Time: 2-3 hours (research docs, write code, debug)
Stress: High (easy to make mistakes)
```

**With Prompt Engineering:**
```
Prompt: "Generate Terraform code for AWS VPC with 2 public subnets,
2 private subnets, NAT gateway, and route tables. Use best practices."

Time: 30 seconds for AI + 10 minutes review/adjust
Stress: Low (AI handles boilerplate, you focus on business logic)
```

**Time saved:** 2+ hours per task → Compound that over a career 🚀

---

### Career Impact

**Without Prompt Engineering:**
- Write every line of code manually
- Spend hours debugging errors
- Limited by your memory of syntax
- Competitive with 1,000s of DevOps engineers

**With Prompt Engineering:**
- Generate code 10x faster
- Debug issues in minutes
- Access infinite knowledge through AI
- Competitive advantage over 95% of engineers (most don't know this yet!)

**Salary Impact:**
- Junior DevOps with prompt skills > Senior without
- Can work on complex problems others avoid
- Get more done in less time = promotions/raises
- Emerging skill = bonus points in interviews

---

## 📖 THEORY: What Makes a Good Prompt?

### The 6 Elements of Perfect Prompts

Most people ask AI: "Make me a Terraform file"
**Result:** Generic, unusable code 😞

**The TRIPOD Framework for DevOps Prompts:**

1. **Task** - What you want
2. **Role** - Who the AI should be
3. **Instructions** - Specific requirements
4. **Parameters** - Technical details
5. **Output** - Desired format
6. **Danger** - What to avoid

Let's break it down:

---

### Element 1: Task (What You Want)

❌ **Vague:**
> "Help with Kubernetes"

✅ **Clear:**
> "Generate a Kubernetes Deployment YAML for a Python FastAPI app"

**Why it matters:** AI needs to know the specific deliverable.

---

### Element 2: Role (Who AI Should Be)

❌ **No role:**
> "Generate Terraform code"

✅ **With role:**
> "You are a senior DevOps engineer with 10 years of AWS experience. Generate Terraform code..."

**Why it matters:** AI adjusts complexity and best practices based on role.

**Useful roles for DevOps:**
- "Senior DevOps Engineer with AWS expertise"
- "Site Reliability Engineer (SRE) focused on production systems"
- "Security-focused DevOps engineer"
- "Platform engineer building internal tools"

---

### Element 3: Instructions (Specific Requirements)

❌ **No instructions:**
> "Make a Docker file"

✅ **With instructions:**
> "Create a multi-stage Dockerfile for a Node.js app. Use Alpine for small size. Run as non-root user. Include health check."

**Why it matters:** AI doesn't know your requirements unless you specify.

---

### Element 4: Parameters (Technical Details)

❌ **Missing parameters:**
> "Create an AWS EC2 instance"

✅ **With parameters:**
> "Create an AWS EC2 instance:
> - Instance type: t3.medium
> - OS: Ubuntu 22.04
> - Region: eu-north-1
> - Security group: Allow SSH (22) and HTTPS (443)
> - Storage: 50GB GP3"

**Why it matters:** Prevents back-and-forth iterations.

---

### Element 5: Output (Desired Format)

❌ **No format:**
> "Explain Kubernetes services"

✅ **With format:**
> "Explain Kubernetes services in 3 bullet points with code examples. Format as markdown."

**Why it matters:** Gets you exactly what you need.

**Common outputs for DevOps:**
- "YAML format with comments"
- "Terraform with variables separated into variables.tf"
- "Bash script with error handling"
- "Markdown documentation with examples"
- "Table comparing options"

---

### Element 6: Danger (What to Avoid)

❌ **No guardrails:**
> "Generate Kubernetes YAML"
> *AI uses 'latest' tags and runs as root* 😱

✅ **With guardrails:**
> "Generate Kubernetes YAML.
> DO NOT use 'latest' tags - use specific versions.
> DO NOT run as root user - use securityContext.
> DO include resource limits."

**Why it matters:** Prevents AI from making rookie mistakes.

---

## 💻 HANDS-ON: Before & After Examples

### Example 1: Creating a Dockerfile

#### ❌ Bad Prompt
```
Make a Dockerfile for Python
```

**AI Output:**
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

**Problems:**
- Uses old Python version
- No security (runs as root)
- Large image size (not using slim/alpine)
- No health check
- Copies everything (including .git, cache)

---

#### ✅ Good Prompt (Using TRIPOD)
```
You are a senior DevOps engineer focused on container security and optimization.

Task: Create a production-ready Dockerfile for a Python FastAPI application.

Instructions:
- Use multi-stage build to reduce size
- Run as non-root user
- Include health check endpoint
- Use .dockerignore to exclude unnecessary files

Parameters:
- Python version: 3.11
- Base image: python:3.11-slim
- App listens on port 8000
- Health check endpoint: /health

Output: Dockerfile with inline comments explaining each step

Danger:
- DO NOT use 'latest' tags
- DO NOT run as root
- DO NOT copy .git or __pycache__
```

**AI Output:**
```dockerfile
# Multi-stage build for smaller final image
FROM python:3.11-slim as builder

# Install dependencies in separate stage
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage - only runtime dependencies
FROM python:3.11-slim

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Copy installed packages from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

WORKDIR /app

# Copy only necessary files (use .dockerignore)
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Result:** Production-ready, secure, optimized Dockerfile on first try! 🎉

---

### Example 2: Terraform AWS Infrastructure

#### ❌ Bad Prompt
```
Create Terraform for AWS
```

**AI Output:** Generic, incomplete code that won't work.

---

#### ✅ Good Prompt
```
You are a senior DevOps engineer specializing in AWS infrastructure.

Task: Generate Terraform code for a production-ready web application infrastructure on AWS.

Instructions:
- Use modules for reusability
- Follow AWS Well-Architected Framework
- Include high availability across 2 AZs
- Use remote state in S3

Parameters:
- Region: eu-north-1
- VPC CIDR: 10.0.0.0/16
- 2 public subnets (for load balancer)
- 2 private subnets (for EC2 instances)
- Application Load Balancer
- 2 EC2 instances (t3.medium, Ubuntu 22.04)
- RDS PostgreSQL (db.t3.micro)
- Security groups with least privilege

Output: Separate files - main.tf, variables.tf, outputs.tf. Include comments.

Danger:
- DO NOT hardcode secrets
- DO NOT allow 0.0.0.0/0 for SSH
- DO NOT use default VPC
- DO include encryption for RDS
```

**AI Output:** Complete, production-ready Terraform with:
- ✅ Proper structure
- ✅ Security best practices
- ✅ High availability
- ✅ Commented and organized
- ✅ Ready to use with minimal adjustments

---

## 🎯 Advanced Prompting Techniques

### Technique 1: Chain of Thought (CoT)

Instead of asking for final answer, ask AI to explain reasoning.

❌ **Direct:**
> "Why is my pod crashing?"

✅ **Chain of Thought:**
> "I have a Kubernetes pod stuck in CrashLoopBackOff. Walk me through your debugging process step-by-step:
> 1. What would you check first?
> 2. What commands would you run?
> 3. What are the most common causes?
> 4. How would you fix each?"

**Result:** Get a learning experience, not just an answer.

---

### Technique 2: Few-Shot Learning

Give AI examples of what you want.

**Prompt:**
```
I need Kubernetes service definitions. Here are two examples of my style:

Example 1:
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
  labels:
    app: frontend
    team: web
spec:
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP

Example 2:
---
apiVersion: v1
kind: Service
metadata:
  name: backend
  labels:
    app: backend
    team: api
spec:
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP

Now create a service for a database following the same style:
- Name: postgres
- Team label: data
- Port: 5432
- Type: ClusterIP
```

**Result:** AI matches your exact style and conventions.

---

### Technique 3: Iterative Refinement

Start broad, then narrow down.

**Prompt 1:**
> "I need to deploy a Python web app to Kubernetes. What architecture would you recommend?"

**AI Response:** Suggests deployment, service, ingress, configmap, secret.

**Prompt 2:**
> "Great. Now generate the Deployment YAML with:
> - 3 replicas
> - Resource limits: 512Mi memory, 500m CPU
> - Environment variables from ConfigMap 'app-config'
> - Secrets from 'app-secrets'
> - Health checks on /health endpoint"

**Result:** Precise output because you refined requirements.

---

## 🧠 Real-World DevOps Prompting Patterns

### Pattern 1: The "Expert Reviewer"

**Use case:** Check your code for mistakes

**Prompt:**
```
You are a senior DevOps engineer reviewing this Terraform code for a junior engineer.

[paste your code]

Review for:
1. Security vulnerabilities
2. Missing best practices
3. Potential cost optimizations
4. Scalability issues

Format: List issues with severity (Critical/High/Medium/Low) and suggested fixes.
```

---

### Pattern 2: The "Migration Assistant"

**Use case:** Convert between formats

**Prompt:**
```
You are an expert in both Docker Compose and Kubernetes.

Task: Convert this docker-compose.yml to Kubernetes manifests (Deployment, Service, ConfigMap).

[paste docker-compose.yml]

Output: Separate YAML files for each resource with comments explaining the conversion.
```

---

### Pattern 3: The "Troubleshooter"

**Use case:** Debug production issues

**Prompt:**
```
You are a Site Reliability Engineer debugging a production issue.

Symptoms:
- API response time increased from 200ms to 5000ms
- CPU usage normal (30%)
- Memory usage high (85%)
- No error logs

Context:
- Node.js API on Kubernetes
- PostgreSQL database (RDS)
- Redis cache
- 10 pods running

Walk me through:
1. What would you check first and why?
2. What commands/queries would you run?
3. What are the most likely causes?
4. How would you fix each?

Format: Step-by-step debugging guide.
```

---

### Pattern 4: The "Documentation Generator"

**Use case:** Create runbooks and docs

**Prompt:**
```
You are a technical writer for DevOps teams.

Task: Create a runbook for deploying our Python API to Kubernetes.

Context:
- Git repo: github.com/company/api
- Docker registry: registry.company.com
- K8s cluster: production (eu-north-1)
- Namespace: api-production

Include:
1. Prerequisites (tools, access)
2. Pre-deployment checklist
3. Deployment steps (with commands)
4. Verification steps
5. Rollback procedure
6. Troubleshooting common issues

Output: Markdown format with code blocks and clear sections.
```

---

## 💼 Interview Advantage

### Why Prompt Engineering Gets You Hired

**Interviewer:** "How would you approach learning a new tool like Terraform?"

❌ **Without prompt engineering:**
> "I'd read the documentation and do tutorials."

✅ **With prompt engineering:**
> "I'd start with official docs, but I'd also use AI to accelerate learning. For example, I'd prompt:
>
> 'You are a Terraform expert. I'm experienced with CloudFormation. Explain Terraform concepts by comparing them to CloudFormation equivalents. Then generate example Terraform code for [specific use case].'
>
> This lets me map new concepts to what I know, then immediately practice with relevant examples. I can learn a new tool in days instead of weeks."

**Why this impresses:** Shows you're a fast learner who uses modern tools.

---

### Demonstrating Prompt Skills in Interviews

**Live Coding Exercise:**
> "Write Terraform for an AWS VPC"

**Without AI:** Struggle for 30 minutes, make syntax errors.

**With AI (if allowed):**
1. Open ChatGPT/GitHub Copilot
2. Use your perfect prompt (30 seconds)
3. Review AI output (2 minutes)
4. Explain the code confidently (3 minutes)
5. Modify for specific requirements (5 minutes)

**Total:** 10 minutes vs 30 minutes + You look like an expert!

**Note:** Always check if AI tools are allowed in interview. Some companies love it (shows modern skills), others don't allow it. When in doubt, ask!

---

## 📚 Prompt Library for DevOps

### Save These Templates

#### 1. Docker Optimization
```
You are a container optimization expert.

Task: Review this Dockerfile and suggest optimizations for:
- Smaller image size
- Faster build times
- Better security
- Best practices

[paste Dockerfile]

Output: Optimized Dockerfile with comments explaining each improvement.
```

#### 2. Kubernetes Debugging
```
You are a Kubernetes troubleshooting expert.

Issue: [describe problem]

Logs: [paste logs]

Describe output: [paste kubectl describe]

Provide:
1. Most likely root cause
2. Step-by-step debugging commands
3. Fix with explanation
4. Prevention for future
```

#### 3. Bash Script Generation
```
You are an expert in Bash scripting and Linux automation.

Task: Create a Bash script that [describe task]

Requirements:
- Include error handling (set -euo pipefail)
- Add logging to /var/log/[script-name].log
- Validate prerequisites before running
- Add help text (--help flag)
- Include dry-run mode (--dry-run flag)

Output: Production-ready script with comments.
```

#### 4. CI/CD Pipeline
```
You are a CI/CD architect.

Task: Design a GitHub Actions workflow for [application type]

Requirements:
- Run tests on every PR
- Security scanning (dependencies, container)
- Deploy to staging on merge to main
- Deploy to production on git tag
- Automatic rollback if health checks fail

Output: Complete .github/workflows/ci-cd.yml with comments.
```

#### 5. Documentation
```
You are a technical writer for DevOps teams.

Task: Create comprehensive documentation for [system/tool]

Audience: Junior DevOps engineers

Include:
- Overview (what it does, why it matters)
- Architecture diagram (ASCII or description)
- Quick start guide
- Common operations with examples
- Troubleshooting section
- Best practices

Output: Markdown with clear sections and code examples.
```

---

## 🎯 Practice Exercises

### Exercise 1: Perfect Prompts

Improve these bad prompts:

**Bad:** "Make a Docker file"
**Your improved version:** _______

**Bad:** "Help with Terraform"
**Your improved version:** _______

**Bad:** "Kubernetes not working"
**Your improved version:** _______

<details>
<summary>💡 Example Answers</summary>

**Docker:**
> "You are a container security expert. Create a production-ready multi-stage Dockerfile for a Go 1.21 web application. Requirements: Alpine base, non-root user, health check on /healthz, optimized layers. Output: Dockerfile with security annotations."

**Terraform:**
> "You are a senior DevOps engineer. Generate Terraform code for AWS VPC with 2 public and 2 private subnets, NAT gateway, route tables. Use eu-north-1 region. Include variables.tf and outputs.tf. Follow AWS best practices."

**Kubernetes:**
> "You are an SRE expert. My Kubernetes pod is in CrashLoopBackOff state. Here are the logs: [logs]. And describe output: [describe]. Provide step-by-step debugging approach with kubectl commands and likely root causes."

</details>

---

### Exercise 2: Build Your Prompt Library

Create perfect prompts for your daily tasks:

1. Your most common Docker task
2. Your most common Kubernetes task
3. Your most common troubleshooting scenario
4. Your most common documentation need

**Save these!** You'll use them hundreds of times.

---

## 🧠 Advanced: Training AI on Your Infrastructure

### Technique: Custom GPT for Your Company

If using ChatGPT Plus, you can create a custom GPT trained on your infrastructure:

**Setup:**
```
Name: "[Company] DevOps Assistant"

Instructions:
"You are a senior DevOps engineer at [Company]. You have expert knowledge of our infrastructure:

Infrastructure:
- Cloud: AWS (us-east-1, eu-west-1)
- Container orchestration: Kubernetes (EKS)
- IaC: Terraform
- CI/CD: GitHub Actions
- Monitoring: Prometheus + Grafana
- Logging: CloudWatch

Conventions:
- All resources tagged with: Environment, Team, CostCenter
- Terraform modules in terraform-modules repo
- Kubernetes manifests use Kustomize
- Secrets in AWS Secrets Manager
- Use eu-west-1 as default region

When generating code:
- Follow company conventions
- Include proper tags
- Use existing modules when possible
- Add comments referencing runbooks
"

Knowledge: [upload your runbooks, architecture docs]

Conversation starters:
- "Generate Terraform for new microservice"
- "Troubleshoot EKS pod issue"
- "Create GitHub Actions workflow"
- "Write runbook for deployment"
```

**Result:** AI that knows your specific infrastructure! 🎉

---

## 📊 Productivity Metrics

### Measure Your Improvement

**Track these before and after learning prompt engineering:**

| Task | Before (hours) | After (hours) | Savings |
|------|----------------|---------------|---------|
| Write Terraform module | 3 | 0.5 | 83% |
| Create K8s deployment | 1 | 0.25 | 75% |
| Debug production issue | 2 | 0.5 | 75% |
| Write documentation | 2 | 0.5 | 75% |
| Create bash script | 1 | 0.25 | 75% |

**Average time savings:** 75-85%
**Productivity increase:** 4-6x

---

## 💡 Pro Tips

### Tip 1: Iterate in Public

Bad: Ask AI for perfect answer in one shot
Good: Show AI your problem-solving process

**Example:**
```
"I'm debugging a Kubernetes issue. Here's what I've tried:
1. Checked logs - nothing obvious
2. Described pod - see ImagePullBackOff
3. Checked image name - looks correct

What should I check next?"
```

AI gives better help when it sees your thought process.

---

### Tip 2: Use AI for Learning, Not Just Solutions

Bad: "Give me the answer"
Good: "Teach me how to solve this"

**Example:**
```
"I need to understand Kubernetes networking. Don't just give me commands - explain:
1. How does pod-to-pod communication work?
2. What are the different service types and when to use each?
3. How does DNS work in Kubernetes?
4. Give me hands-on exercises to practice

Format: Teach like I'm explaining it in an interview."
```

---

### Tip 3: Fact-Check Everything

**AI can hallucinate!** Always verify:
- Command syntax (test in non-prod)
- Security recommendations (check docs)
- Best practices (compare with official sources)

**Good habit:**
```
"Is this command correct: kubectl get pod -o yaml
Also, what are alternative ways to achieve the same result?"
```

AI will catch its own mistakes when asked to double-check.

---

## ⚠️ Common Mistakes

### ❌ Mistake 1: Being Too Vague

**Bad:** "Help with Docker"
**Why it's bad:** AI doesn't know what you need
**Fix:** Use TRIPOD framework - specify task, role, instructions, parameters, output, danger

---

### ❌ Mistake 2: Accepting First Response

**Bad:** Take AI output as-is without review
**Why it's bad:** AI makes mistakes, especially security
**Fix:** Always review, test, and iterate

---

### ❌ Mistake 3: Not Providing Context

**Bad:** "Why is this broken? [paste error]"
**Why it's bad:** AI needs full picture
**Fix:** Include context: what you're trying to do, what you've tried, full error, environment details

---

## 🎯 Next Steps

After mastering prompt fundamentals:

1. **Module 2:** AI for Infrastructure as Code (generate Terraform/CloudFormation)
2. **Module 3:** AI for Kubernetes YAML generation
3. **Module 4:** AI-powered Bash scripting
4. **Module 5:** Debugging with AI (production issues)
5. **Module 6:** AI for documentation automation
6. **Module 7:** Custom GPT for your infrastructure

---

## 📚 Flashcards

**Q: What is prompt engineering?**
A: The skill of asking AI the right questions to get perfect results. Uses structure (task, role, instructions, parameters, output, danger).

**Q: What is the TRIPOD framework?**
A: Task, Role, Instructions, Parameters, Output, Danger - six elements of perfect prompts.

**Q: Why specify AI's role?**
A: AI adjusts complexity and best practices based on role (e.g., "senior DevOps engineer" vs "beginner").

**Q: What is Chain of Thought (CoT)?**
A: Asking AI to explain reasoning step-by-step instead of just giving final answer.

**Q: What is Few-Shot Learning?**
A: Giving AI examples of what you want before asking it to generate similar output.

**Q: Why is "latest" tag dangerous?**
A: Not reproducible - "latest" changes over time, breaking deployments. Always use specific versions.

**Q: How much faster does prompt engineering make you?**
A: 4-6x productivity increase (75-85% time savings on coding tasks).

**Q: Should you trust AI output blindly?**
A: No! Always review, test, and fact-check. AI can hallucinate and make security mistakes.

---

## 🎓 Quiz

### Question 1: Improve This Prompt

**Bad prompt:** "Make me a Terraform file for AWS"

**What's missing?**
A) Task specification
B) Technical parameters
C) Output format
D) All of the above ✅

**Better prompt:**
> "You are a senior DevOps engineer. Generate Terraform code for AWS VPC with 2 public and 2 private subnets in eu-north-1. Include variables.tf and outputs.tf with comments. DO NOT hardcode values."

---

### Question 2: Which is Better?

**Prompt A:** "Fix this Kubernetes YAML [paste]"

**Prompt B:** "You are a Kubernetes expert. Review this deployment YAML for security issues, missing resource limits, and best practices. [paste]. Output: List of issues with severity and fixes."

**Answer:** B ✅

**Why:** Specifies role, what to look for, and desired output format.

---

### Question 3: Scenario

You're debugging a production issue. Which prompt is better?

**A)** "My pod is crashing help"

**B)** "You are an SRE expert. My production pod is CrashLoopBackOff. Logs: [paste]. Describe: [paste]. Walk me through debugging: 1) What to check first? 2) Common causes? 3) How to fix?"

**Answer:** B ✅

**Why:** Provides context, logs, and asks for structured debugging approach.

---

## 🌟 Why This Module is Revolutionary

✅ **10x productivity** - Tasks that took hours now take minutes
✅ **Learn faster** - Master new tools in days instead of weeks
✅ **Competitive advantage** - 95% of DevOps engineers don't know this yet
✅ **Interview ready** - Demonstrates modern skills and fast learning
✅ **Future-proof** - AI is only getting better, early adopters win

**Time to complete:** 1-1.5 hours
**ROI:** Save 10-20 hours per week for the rest of your career
**Career impact:** Priceless

---

**Module completed!** 🎉

**Next:** Module 2 - AI for Infrastructure as Code (Terraform/CloudFormation)

**Practice:** Use TRIPOD framework for your next DevOps task today!
"""
}

# Export all modules
PROMPT_ENGINEERING_MODULES = [
    PROMPT_FUNDAMENTALS,
    # More modules will be added...
]

# MODULE export för kompatibilitet med systemet
MODULE = {
    "name": "Prompt Engineering for DevOps",
    "slug": "prompt-engineering-devops",
    "description": "Master AI-assisted DevOps with the TRIPOD framework. 10x your productivity with ChatGPT, Claude, and Copilot. The emerging skill that gives you a competitive edge.",
    "icon": "🤖",
    "order_index": 13,
    "category": "devops",
    "difficulty": "beginner",
    "estimated_hours": 4,
    "tasks": PROMPT_ENGINEERING_MODULES
}
