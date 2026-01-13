"""
Multi-Cloud Architecture - Design Across AWS, Azure, and GCP
=============================================================

Master multi-cloud strategies to design resilient systems across cloud providers.
Learn when to use each cloud, avoid vendor lock-in, and maximize leverage.

Career Impact: Senior/Architect roles require multi-cloud. +35-50% salary.
"""

MULTICLOUD_STRATEGIES = {
    "title": "Multi-Cloud Architecture & Strategy",
    "slug": "multicloud-strategies",
    "description": "Design applications that span AWS, Azure, and GCP. Master cloud-agnostic patterns, avoid vendor lock-in, and maximize each cloud's strengths.",
    "difficulty": "advanced",
    "estimated_minutes": 150,
    "xp_reward": 300,
    "order_index": 1,
    "content": r"""# Multi-Cloud Architecture & Strategy

## 🎯 TL;DR (30 seconds)

Multi-cloud means using 2+ cloud providers strategically (not just for redundancy). **84% of enterprises use multi-cloud** to avoid vendor lock-in, leverage best-in-class services, and meet regulatory requirements.

**Why this matters:** Senior+ roles require multi-cloud thinking. **Multi-cloud architects earn 35-50% more** than single-cloud engineers.

---

## 🚀 Why Multi-Cloud Matters for Your Career

### The Enterprise Reality (2026)

**Multi-Cloud Adoption:**
- 84% of enterprises use 2+ clouds
- 62% actively design for multi-cloud (not just accidental usage)
- 38% use all three: AWS + Azure + GCP

**Why Companies Go Multi-Cloud:**
1. **Avoid vendor lock-in** - No single point of failure
2. **Best-of-breed** - Use AWS for breadth, Azure for Windows, GCP for data
3. **Cost optimization** - Competition between providers
4. **Regulatory compliance** - Data sovereignty requirements
5. **Acquisitions** - Merging companies on different clouds
6. **Geographic coverage** - Use closest regions

**Job Market Reality:**
- 78% of Cloud Architect roles require multi-cloud experience
- 65% of Senior DevOps roles prefer multi-cloud
- Only 15% of companies are "cloud-agnostic" (can switch easily)

### Salary Impact (Sweden 2026)

| Role | Single Cloud | Multi-Cloud | Difference |
|------|--------------|-------------|------------|
| DevOps Engineer | 55,000 SEK | 72,000 SEK | **+31%** |
| Cloud Architect | 70,000 SEK | 98,000 SEK | **+40%** |
| Platform Engineer | 65,000 SEK | 88,000 SEK | **+35%** |
| VP Engineering | 120,000 SEK | 170,000 SEK | **+42%** |

**Multi-cloud expertise = +25,000 SEK/month = +300,000 SEK/year** 💰

---

## 📖 THEORY: Multi-Cloud Strategies

### Strategy 1: Best-of-Breed (Most Common)

Use each cloud for what it does best.

```
┌─────────────────────────────────────────────┐
│            Your Application                 │
├─────────────────────────────────────────────┤
│                                             │
│  AWS:                                       │
│  ├─ EC2 for compute (cheapest at scale)   │
│  ├─ S3 for object storage (most mature)   │
│  └─ Lambda for serverless (largest ecosystem)
│                                             │
│  Azure:                                     │
│  ├─ Azure AD for enterprise SSO           │
│  ├─ Azure SQL for Windows apps            │
│  └─ Azure DevOps for CI/CD                │
│                                             │
│  GCP:                                       │
│  ├─ BigQuery for data analytics           │
│  ├─ GKE for Kubernetes (best K8s)         │
│  └─ Vertex AI for machine learning        │
└─────────────────────────────────────────────┘
```

**Example: Spotify**
- GCP: BigQuery for analytics (billions of events)
- AWS: S3 for audio storage (petabytes)
- On-prem: PostgreSQL for user data (legacy)

**When to use:** Mature companies optimizing costs and features.

---

### Strategy 2: Geographic Redundancy

Primary cloud + failover cloud in different regions.

```
┌──────────────────────────────────────┐
│         PRIMARY (AWS US-East)        │
│  - 90% of traffic                    │
│  - Full application stack            │
└──────────────────────────────────────┘
              ↓ (replication)
┌──────────────────────────────────────┐
│       FAILOVER (Azure EU-West)       │
│  - 0% traffic (standby)              │
│  - Can handle 100% if AWS fails      │
└──────────────────────────────────────┘
```

**Example: Netflix** (AWS + Zuul router for multi-region)

**When to use:** Mission-critical apps (banking, healthcare).

---

### Strategy 3: Data Residency / Compliance

Keep data in specific regions due to regulations (GDPR, etc.).

```
┌──────────────────────────────────────┐
│      EU Customers (Azure EU)         │
│  - GDPR requires data in EU          │
│  - Azure has most EU regions         │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│      US Customers (AWS US)           │
│  - AWS cheapest in US                │
│  - More regions available            │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│    China Customers (Alibaba Cloud)   │
│  - Chinese law requires local cloud  │
│  - AWS/Azure restricted              │
└──────────────────────────────────────┘
```

**When to use:** Global SaaS with regulatory requirements.

---

### Strategy 4: Workload Segregation

Different teams/products on different clouds.

```
Team A (DevOps) → AWS (expertise, tooling)
Team B (Data Science) → GCP (BigQuery, Vertex AI)
Team C (Enterprise IT) → Azure (Active Directory integration)
```

**When to use:** Large enterprises with autonomous teams.

---

## 🏗️ Cloud-Agnostic Architecture Patterns

### Pattern 1: Abstract the Cloud with Terraform

**Problem:** Different APIs for each cloud.

**Solution:** Use Terraform as abstraction layer.

```hcl
# Define cloud-agnostic module
module "vm" {
  source = "./modules/vm"

  cloud_provider = "aws"  # or "azure" or "gcp"
  vm_size = "medium"
  region = "us-east"
}

# modules/vm/main.tf
resource "aws_instance" "this" {
  count = var.cloud_provider == "aws" ? 1 : 0
  instance_type = local.vm_sizes["aws"]["medium"]  # t3.medium
  # ...
}

resource "azurerm_virtual_machine" "this" {
  count = var.cloud_provider == "azure" ? 1 : 0
  vm_size = local.vm_sizes["azure"]["medium"]  # Standard_B2s
  # ...
}

resource "google_compute_instance" "this" {
  count = var.cloud_provider == "gcp" ? 1 : 0
  machine_type = local.vm_sizes["gcp"]["medium"]  # e2-medium
  # ...
}
```

**Benefit:** Change clouds by changing one variable.

---

### Pattern 2: Use Kubernetes for Portability

**Kubernetes runs the same way on any cloud!**

```yaml
# This YAML works on EKS, AKS, GKE identically
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: myapp:v1.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: webapp
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
```

**Cloud-specific only:**
- Load balancer implementation (cloud LB created)
- Storage classes (EBS vs Azure Disk vs GCP PD)
- Node pools (EC2 vs Azure VMs vs GCE)

**90% of your K8s config is portable!**

---

### Pattern 3: Object Storage Abstraction

**Problem:** S3, Blob Storage, Cloud Storage have different APIs.

**Solution:** Use S3-compatible API (most clouds support it).

```python
import boto3

# Works with AWS S3, Azure Blob (with compatibility), MinIO, etc.
s3 = boto3.client('s3',
    endpoint_url=os.environ['S3_ENDPOINT'],  # Different per cloud
    aws_access_key_id=os.environ['ACCESS_KEY'],
    aws_secret_access_key=os.environ['SECRET_KEY']
)

# Same code for all clouds!
s3.upload_file('file.txt', 'my-bucket', 'file.txt')
s3.download_file('my-bucket', 'file.txt', 'downloaded.txt')
```

**Cloud-specific endpoints:**
- AWS: `s3.amazonaws.com`
- GCP: Cloud Storage has S3-compatible API
- Azure: Use MinIO gateway or Azure SDK
- On-prem: MinIO

---

### Pattern 4: Message Queue Abstraction

**Problem:** SQS, Service Bus, Pub/Sub are different.

**Solution:** Use abstraction library or standard protocols.

```python
# Option 1: Use Celery (supports multiple brokers)
from celery import Celery

app = Celery('tasks', broker=os.environ['BROKER_URL'])
# broker_url can be:
# - AWS SQS: 'sqs://...'
# - Azure Service Bus: 'azureservicebus://...'
# - GCP Pub/Sub: 'gcppubsub://...'
# - RabbitMQ: 'amqp://...'

@app.task
def process_order(order_id):
    # Business logic is cloud-agnostic
    print(f"Processing {order_id}")

# Option 2: Use NATS (cloud-agnostic message system)
import nats

nc = await nats.connect(os.environ['NATS_URL'])
await nc.publish("orders", b'{"order_id": 123}')
```

---

### Pattern 5: Database Abstraction

**Problem:** Cloud-managed databases have different APIs.

**Solution:** Use standard protocols (PostgreSQL wire protocol, etc.).

```python
import psycopg2

# Works with:
# - AWS RDS PostgreSQL
# - Azure Database for PostgreSQL
# - GCP Cloud SQL PostgreSQL
# - Self-hosted PostgreSQL

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD']
)

# Same code for all clouds!
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
```

**Cloud-specific features to avoid for portability:**
- AWS Aurora Serverless v2 (pause/resume)
- Azure SQL Hyperscale (hot/cold tiers)
- GCP Spanner (global transactions)

Use these ONLY if portability isn't a requirement.

---

## 💻 HANDS-ON: Deploy to 3 Clouds with Terraform

### Step 1: Project Structure

```bash
mkdir multi-cloud-demo && cd multi-cloud-demo

# Create structure
mkdir -p {aws,azure,gcp,modules/vm}

# Create main Terraform files
touch {main.tf,variables.tf,outputs.tf}
touch modules/vm/{main.tf,variables.tf,outputs.tf}
```

---

### Step 2: Create Cloud-Agnostic VM Module

```hcl
# modules/vm/variables.tf
variable "cloud_provider" {
  type = string
  validation {
    condition = contains(["aws", "azure", "gcp"], var.cloud_provider)
    error_message = "Must be aws, azure, or gcp"
  }
}

variable "vm_name" { type = string }
variable "vm_size" { type = string default = "small" }
variable "region" { type = string }

# modules/vm/main.tf
locals {
  # Map generic sizes to cloud-specific sizes
  vm_sizes = {
    aws = {
      small  = "t3.micro"
      medium = "t3.medium"
      large  = "t3.large"
    }
    azure = {
      small  = "Standard_B1s"
      medium = "Standard_B2s"
      large  = "Standard_B4ms"
    }
    gcp = {
      small  = "e2-micro"
      medium = "e2-medium"
      large  = "e2-standard-4"
    }
  }
}

# AWS VM
resource "aws_instance" "vm" {
  count         = var.cloud_provider == "aws" ? 1 : 0
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu
  instance_type = local.vm_sizes["aws"][var.vm_size]

  tags = {
    Name = var.vm_name
  }
}

# Azure VM
resource "azurerm_linux_virtual_machine" "vm" {
  count               = var.cloud_provider == "azure" ? 1 : 0
  name                = var.vm_name
  resource_group_name = azurerm_resource_group.rg[0].name
  location            = var.region
  size                = local.vm_sizes["azure"][var.vm_size]

  admin_username = "azureuser"
  admin_ssh_key {
    username   = "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

resource "azurerm_resource_group" "rg" {
  count    = var.cloud_provider == "azure" ? 1 : 0
  name     = "${var.vm_name}-rg"
  location = var.region
}

# GCP VM
resource "google_compute_instance" "vm" {
  count        = var.cloud_provider == "gcp" ? 1 : 0
  name         = var.vm_name
  machine_type = local.vm_sizes["gcp"][var.vm_size]
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}  # Ephemeral public IP
  }
}

# modules/vm/outputs.tf
output "public_ip" {
  value = (
    var.cloud_provider == "aws" ? aws_instance.vm[0].public_ip :
    var.cloud_provider == "azure" ? azurerm_linux_virtual_machine.vm[0].public_ip_address :
    var.cloud_provider == "gcp" ? google_compute_instance.vm[0].network_interface[0].access_config[0].nat_ip :
    null
  )
}
```

---

### Step 3: Main Configuration

```hcl
# main.tf
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
    azurerm = { source = "hashicorp/azurerm", version = "~> 3.0" }
    google = { source = "hashicorp/google", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "azurerm" {
  features {}
}

provider "google" {
  project = var.gcp_project_id
  region  = "us-central1"
}

# Deploy to AWS
module "vm_aws" {
  source = "./modules/vm"

  cloud_provider = "aws"
  vm_name        = "demo-aws"
  vm_size        = "small"
  region         = "us-east-1"
}

# Deploy to Azure
module "vm_azure" {
  source = "./modules/vm"

  cloud_provider = "azure"
  vm_name        = "demo-azure"
  vm_size        = "small"
  region         = "eastus"
}

# Deploy to GCP
module "vm_gcp" {
  source = "./modules/vm"

  cloud_provider = "gcp"
  vm_name        = "demo-gcp"
  vm_size        = "small"
  region         = "us-central1"
}

# outputs.tf
output "aws_ip" { value = module.vm_aws.public_ip }
output "azure_ip" { value = module.vm_azure.public_ip }
output "gcp_ip" { value = module.vm_gcp.public_ip }
```

---

### Step 4: Deploy to All Clouds

```bash
# Initialize Terraform
terraform init

# Plan (see what will be created)
terraform plan

# Apply (create resources in all 3 clouds!)
terraform apply -auto-approve

# Output shows IPs:
# aws_ip = "54.123.45.67"
# azure_ip = "20.123.45.67"
# gcp_ip = "34.123.45.67"

# Clean up
terraform destroy -auto-approve
```

🎉 **You just deployed to 3 clouds with one command!**

---

## 💼 Interview Preparation

### Question 1: When Multi-Cloud?

**Interviewer:** "When would you recommend multi-cloud vs single cloud?"

✅ **Strong Answer:**
> "Multi-cloud makes sense for: 1) Large enterprises avoiding vendor lock-in and negotiating better pricing. 2) Best-of-breed strategy - using GCP for BigQuery, AWS for breadth, Azure for Windows. 3) Regulatory requirements - GDPR data residency. 4) Disaster recovery across providers (rare, most use multi-region in one cloud). I'd avoid multi-cloud for: 1) Startups - adds complexity without benefit. 2) Small teams - operational burden is high. 3) When cloud-native services are used (Lambda, DynamoDB) - hard to abstract. Multi-cloud works best with Kubernetes and standard protocols."

**Why this impresses:** Balanced view with trade-offs.

---

### Question 2: Avoiding Vendor Lock-in

**Interviewer:** "How do you design for minimal vendor lock-in?"

✅ **Strong Answer:**
> "Use abstraction layers: 1) Kubernetes for compute - runs anywhere. 2) Standard protocols - PostgreSQL wire protocol, S3 API, AMQP. 3) Terraform for infrastructure - multi-cloud by design. 4) Avoid cloud-specific services or isolate them behind interfaces. For example, if using DynamoDB, create a repository interface so you can swap for Cosmos DB or MongoDB. Document cloud-specific dependencies explicitly. That said, sometimes lock-in is worth it - AWS Lambda ecosystem is so rich that avoiding it for 'portability' may not make business sense. It's about conscious trade-offs."

**Why this impresses:** Practical approach.

---

### Question 3: Cost Management

**Interviewer:** "How do you manage costs across multiple clouds?"

✅ **Strong Answer:**
> "Centralized tooling: 1) Use CloudHealth or Cloudability for unified cost dashboard. 2) Tag everything with project/cost-center across all clouds. 3) Set budget alerts per cloud. 4) Use FinOps practices - regular cost reviews, chargeback to teams. 5) Reserved Instances/Committed Use where predictable. 6) Auto-scaling to match demand. 7) Multi-cloud can increase costs (data egress between clouds is expensive), so architect to minimize cross-cloud traffic. Keep data and compute in same cloud when possible."

**Why this impresses:** Cost-aware architecture.

---

### Question 4: Multi-Cloud Security

**Interviewer:** "What are security challenges with multi-cloud?"

✅ **Strong Answer:**
> "Challenges: 1) Inconsistent security policies - each cloud has different IAM models. 2) More attack surface - 3x the accounts to secure. 3) Visibility gaps - logs in different systems. Solutions: 1) Use SAML/SSO federation (Okta, Azure AD) for consistent identity. 2) Infrastructure as Code with policy checks (OPA, Sentinel). 3) Unified logging (Datadog, Splunk). 4) CSPM tools (Prisma Cloud, Wiz) for security posture across clouds. 5) Assume breach mindset - zero trust networking. 6) Centralized secrets (HashiCorp Vault works across clouds)."

**Why this impresses:** Security-first thinking.

---

## 📚 Tools for Multi-Cloud

### Infrastructure as Code
- **Terraform** - De facto standard for multi-cloud
- **Pulumi** - Terraform alternative with real programming languages
- **Crossplane** - K8s-native infrastructure

### Kubernetes Management
- **Rancher** - Manage K8s clusters across clouds
- **ArgoCD** - GitOps deployments to any K8s
- **Flux** - Alternative GitOps tool

### Monitoring & Logging
- **Datadog** - Unified monitoring across clouds
- **New Relic** - Alternative to Datadog
- **Grafana + Prometheus** - Open-source, cloud-agnostic
- **ELK Stack** - Elasticsearch, Logstash, Kibana

### Cost Management
- **CloudHealth (VMware)** - Multi-cloud cost optimization
- **Cloudability (Apptio)** - FinOps platform
- **Kubecost** - Kubernetes cost allocation

### Security
- **Prisma Cloud (Palo Alto)** - CSPM across clouds
- **Wiz** - Cloud security platform
- **HashiCorp Vault** - Secrets management anywhere

---

## 🎯 Decision Matrix: Which Cloud for What?

| Use Case | Best Cloud | Why |
|----------|-----------|-----|
| **Startup MVP** | AWS | Largest ecosystem, most integrations |
| **Enterprise Windows** | Azure | Active Directory integration |
| **Data Analytics** | GCP | BigQuery is unmatched |
| **Kubernetes** | GCP | GKE is gold standard |
| **Machine Learning** | GCP | Vertex AI, TPUs |
| **Breadth of Services** | AWS | 200+ services |
| **Cost Optimization** | GCP | Auto discounts |
| **Regulatory Compliance** | Azure | Most certifications |
| **Global Reach** | AWS | Most regions (33) |
| **Developer Experience** | GCP | Simplest APIs |

---

## 🏆 Portfolio Project: Multi-Cloud Terraform

**Build this for your GitHub:**

```
multi-cloud-terraform/
├── README.md (architecture diagram)
├── aws/
│   ├── main.tf
│   ├── vpc.tf
│   └── eks.tf
├── azure/
│   ├── main.tf
│   ├── vnet.tf
│   └── aks.tf
├── gcp/
│   ├── main.tf
│   ├── vpc.tf
│   └── gke.tf
├── modules/
│   ├── vm/
│   ├── storage/
│   └── database/
└── Makefile (deploy to any cloud)
```

**Features:**
- Deploy same app to AWS, Azure, or GCP
- Unified Terraform modules
- CI/CD with GitHub Actions
- Cost estimation
- Security scanning (tfsec)

**Why this impresses:**
- ✅ Real multi-cloud expertise
- ✅ Infrastructure as Code mastery
- ✅ Demonstrates abstraction skills
- ✅ Production-ready patterns

---

## ⚠️ Anti-Patterns (Avoid These!)

### ❌ Anti-Pattern 1: Multi-Cloud for "Redundancy"

```
Primary: AWS
Failover: Azure (standby)
```

**Problem:** 2x cost, 2x complexity, rarely tested, likely won't work in disaster.

**Better:** Multi-region in ONE cloud (simpler, cheaper, actually works).

---

### ❌ Anti-Pattern 2: Over-Abstraction

```python
# DON'T: Abstract everything
class CloudStorage:
    def upload(self, file): ...
    def download(self, file): ...
    # 100 methods to abstract all S3/Blob/GCS features
```

**Problem:** Abstractions leak. You end up with worst of all worlds.

**Better:** Use cloud-specific SDKs, accept some duplication.

---

### ❌ Anti-Pattern 3: Cross-Cloud Data Transfer

```
User → AWS EC2 → Azure SQL Database
```

**Problem:** Egress costs are HUGE ($0.08-0.12/GB). Latency is terrible.

**Better:** Keep data and compute in same cloud.

---

## 🌟 Module Summary

✅ **Strategic thinking** - When to use multi-cloud
✅ **Hands-on Terraform** - Deployed to 3 clouds
✅ **Abstraction patterns** - Cloud-agnostic design
✅ **Tools knowledge** - Datadog, Vault, Terraform
✅ **Cost awareness** - Egress costs, optimization
✅ **Security** - Multi-cloud challenges
✅ **Interview ready** - Can discuss trade-offs

**Job market impact:** Opens senior/architect roles
**Salary boost:** +35-50% over single-cloud engineers
**Time to complete:** 2.5 hours

---

**Module completed!** 🎉

**You're now a multi-cloud expert! This puts you in the top 15% of DevOps engineers.** 🏆
"""
}

MODULE = {
    "id": "cloud-multicloud-architecture",
    "slug": "cloud-multicloud-architecture",
    "title": "Multi-Cloud Architecture",
    "description": "Design across AWS, Azure, GCP. 84% of enterprises use multi-cloud. Opens senior/architect roles. +35-50% salary boost.",
    "icon": "☁️",
    "category": "cloud",
    "difficulty": "advanced",
    "estimated_hours": 10,
    "tasks": [MULTICLOUD_STRATEGIES],
}
