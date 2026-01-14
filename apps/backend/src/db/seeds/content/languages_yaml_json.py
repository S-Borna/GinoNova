"""
YAML & JSON Mastery - Configuration Management
===============================================

Master YAML and JSON for DevOps: Kubernetes manifests, CI/CD pipelines, configuration files,
and data serialization. Essential formats for every DevOps tool.
"""

YAML_JSON_FUNDAMENTALS = {
    "title": "YAML & JSON Mastery - Configuration Management",
    "slug": "yaml-json-mastery",
    "description": "Master YAML and JSON for DevOps: Kubernetes manifests, CI/CD pipelines, configuration management, and data serialization. Essential for all DevOps work.",
    "difficulty": "beginner",
    "estimated_minutes": 90,
    "xp_reward": 150,
    "order_index": 1,
    "content": r"""# YAML & JSON Mastery - Configuration Management

## 🎯 TL;DR (30 seconds)

YAML and JSON are the universal configuration formats in DevOps. Kubernetes uses YAML, APIs use JSON, CI/CD pipelines
use YAML. Master these formats = read and write any DevOps config. Required in 100% of DevOps roles.

**Why this matters:** Every DevOps tool uses YAML or JSON. Can't work with Docker Compose, Kubernetes, Terraform,
Ansible, or CI/CD without understanding these formats.

---

## 🚀 Why YAML/JSON for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 100% of DevOps roles require YAML knowledge
- 95% work with JSON daily
- Average DevOps role writes 1000+ lines of YAML/year

**Reality Check:**
- Can't write Kubernetes manifests without YAML
- Can't work with APIs without JSON
- Can't debug CI/CD pipelines without YAML
- **This is non-negotiable knowledge**

---

## 📖 THEORY: YAML vs JSON

### When to Use Each

**YAML (YAML Ain't Markup Language):**
- Human-readable
- Supports comments
- Less verbose
- Used for: Kubernetes, Docker Compose, Ansible, CI/CD

**JSON (JavaScript Object Notation):**
- Universal data exchange
- Strict syntax
- Faster parsing
- Used for: APIs, config files, data storage

---

## 🛠️ YAML Fundamentals

### Basic Syntax

```yaml
# Comments start with #

# Key-value pairs
name: John Doe
age: 30
active: true

# Nested objects
address:
  street: 123 Main St
  city: Stockholm
  country: Sweden

# Lists (arrays)
skills:
  - Docker
  - Kubernetes
  - Python
  - Terraform

# Inline list
colors: [red, green, blue]

# Multi-line strings
description: |
  This is a multi-line string.
  It preserves newlines.
  Great for scripts or long text.

# Folded string (single line)
summary: >
  This long text
  will be folded
  into a single line.

# Anchors & aliases (reuse)
default: &default_config
  timeout: 30
  retries: 3

production:
  <<: *default_config
  replicas: 5

staging:
  <<: *default_config
  replicas: 2
```

---

### Common YAML Pitfalls

**❌ Indentation errors:**
```yaml
# BAD: Inconsistent indentation
services:
  web:
    image: nginx
     ports:  # Wrong indent!
      - 80:80
```

**✅ Correct:**
```yaml
services:
  web:
    image: nginx
    ports:
      - 80:80
```

---

**❌ Unquoted special characters:**
```yaml
# BAD: Colon without quotes
message: Error: connection failed  # Interpreted as nested object!
```

**✅ Correct:**
```yaml
message: "Error: connection failed"
```

---

## 🎓 Real-World YAML: Kubernetes

### Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

**Key patterns:**
- `apiVersion` + `kind` = resource type
- `metadata` = names and labels
- `spec` = desired state
- Indentation = hierarchy

---

## 🛠️ JSON Fundamentals

### Basic Syntax

```json
{
  "name": "John Doe",
  "age": 30,
  "active": true,
  "address": {
    "street": "123 Main St",
    "city": "Stockholm",
    "country": "Sweden"
  },
  "skills": [
    "Docker",
    "Kubernetes",
    "Python",
    "Terraform"
  ],
  "metadata": null
}
```

**Rules:**
- Keys must be quoted
- No comments allowed
- No trailing commas
- Strict syntax (one mistake = invalid)

---

## 🎓 Working with JSON in CLI

### jq - JSON Processor

**Install jq:**
```bash
sudo apt install jq  # Ubuntu
brew install jq      # macOS
```

**Examples:**
```bash
# Pretty print
echo '{"name":"John","age":30}' | jq '.'

# Extract field
echo '{"name":"John","age":30}' | jq '.name'
# Output: "John"

# Filter array
echo '[{"name":"Alice","age":25},{"name":"Bob","age":30}]' | jq '.[] | select(.age > 25)'
# Output: {"name":"Bob","age":30}

# AWS CLI example
aws ec2 describe-instances | jq '.Reservations[].Instances[] | {id: .InstanceId, type: .InstanceType}'
```

---

## 🎓 YAML ↔ JSON Conversion

### Python Conversion

```python
import yaml
import json

# YAML to JSON
yaml_string = """
name: John Doe
age: 30
"""

data = yaml.safe_load(yaml_string)
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON to YAML
json_string = '{"name": "John Doe", "age": 30}'
data = json.loads(json_string)
yaml_string = yaml.dump(data)
print(yaml_string)
```

---

### yq - YAML Processor

```bash
# Install
sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
sudo chmod +x /usr/local/bin/yq

# Read value
yq '.metadata.name' deployment.yaml

# Update value
yq '.spec.replicas = 5' -i deployment.yaml

# Convert YAML to JSON
yq -o=json deployment.yaml
```

---

## 🎓 Validation & Linting

### YAML Linting

**Install yamllint:**
```bash
pip install yamllint
```

**Lint files:**
```bash
yamllint config.yaml

# Output:
# config.yaml
#   3:1       error    trailing spaces  (trailing-spaces)
#   5:81      error    line too long (82 > 80 characters)  (line-length)
```

**Fix common issues:**
- Remove trailing spaces
- Consistent indentation (2 or 4 spaces)
- Line length < 80 chars
- No duplicate keys

---

### JSON Validation

```bash
# Validate JSON
jq empty config.json

# If valid: no output
# If invalid: error message

# Example error:
# parse error: Expected separator between values at line 3, column 5
```

---

## 📚 Flashcards

**Q: What does YAML stand for?**
A: YAML Ain't Markup Language (recursive acronym).

**Q: What's the difference between | and > in YAML?**
A: | preserves newlines, > folds into single line.

**Q: Can JSON have comments?**
A: No. JSON doesn't support comments (YAML does with #).

**Q: What is jq?**
A: Command-line JSON processor for parsing and transforming JSON.

**Q: What is yq?**
A: Command-line YAML processor (like jq for YAML).

**Q: What indentation for YAML?**
A: 2 spaces is standard (never tabs).

---

## 🎓 Quiz

### Question 1

**Which format supports comments?**

A) JSON
B) YAML ✅
C) Both
D) Neither

**Answer:** B ✅

**Explanation:** YAML supports comments with #, JSON doesn't.

---

### Question 2

**What's wrong with this YAML?**
```yaml
name: John
age: 30
skills:
- Docker
 - Kubernetes  # Wrong indent!
```

A) Nothing
B) Inconsistent indentation ✅
C) Missing quotes
D) Invalid syntax

**Answer:** B ✅

**Explanation:** List items must have same indentation level.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Essential knowledge** - Required in 100% of DevOps roles
✅ **YAML fluency** - Read/write Kubernetes, CI/CD, IaC
✅ **JSON mastery** - Work with APIs and data
✅ **Debugging skills** - Fix configuration errors quickly
✅ **Interview confidence** - Explain YAML/JSON differences

**Time to complete:** 1.5 hours
**Job market impact:** Non-negotiable foundational skill
**Career foundation:** Everything else builds on this

---

**Module completed!** 🎉

**Congratulations!** You've mastered the configuration languages that power all DevOps tools.
"""
}

# Export as MODULE dict
MODULE = {
    "id": "languages-yaml-json",
    "slug": "languages-yaml-json",
    "title": "YAML & JSON Mastery",
    "description": "Master YAML and JSON for DevOps: Kubernetes manifests, CI/CD pipelines, configuration management, and data serialization. Essential formats for every DevOps tool.",
    "icon": "📄",
    "category": "languages",
    "difficulty": "beginner",
    "estimated_hours": 8,
    "tasks": [YAML_JSON_FUNDAMENTALS],
}
