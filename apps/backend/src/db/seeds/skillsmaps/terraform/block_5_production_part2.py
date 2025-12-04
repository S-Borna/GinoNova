# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 5: PRODUCTION (Part 2)
# =============================================================================
# Nodes 19-20: Enterprise Patterns, Advanced State Operations
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_19 = {
    "id": "terraform_node_19",
    "slug": "terraform-enterprise-patterns",
    "title": "Enterprise Terraform - Scalable Infrastructure Patterns",
    "description": "Design enterprise-scale Terraform architectures and workflows",
    "xp_reward": 200,
    "estimated_minutes": 90,
    "node_id": 19,
    "content": '''
# Enterprise Terraform - Scalable Infrastructure Patterns

## Enterprise Architecture Overview

```
+-----------------------------------------------------------------------------+
|                 ENTERPRISE TERRAFORM ARCHITECTURE                            |
+-----------------------------------------------------------------------------+
|                                                                              |
|  +-----------------------------------------------------------------------+  |
|  |  LAYER 1: PLATFORM TEAM (Central)                                     |  |
|  |  +-------------------------------------------------------------------+|  |
|  |  |  * Module Registry (Private)                                      ||  |
|  |  |  * Policy Library (Sentinel/OPA)                                  ||  |
|  |  |  * Shared Services (VPC, IAM, DNS)                                ||  |
|  |  |  * Bootstrap and State Backend                                    ||  |
|  |  +-------------------------------------------------------------------+|  |
|  +-----------------------------------------------------------------------+  |
|                                    |                                         |
|                                    v                                         |
|  +-----------------------------------------------------------------------+  |
|  |  LAYER 2: SHARED INFRASTRUCTURE                                       |  |
|  |  +-----------+  +-----------+  +-----------+  +----------+            |  |
|  |  | Networking|  | Security  |  | Monitoring|  | Identity |            |  |
|  |  | (VPC/DNS) |  | (WAF/KMS) |  | (Observ)  |  | (IAM/SSO)|            |  |
|  |  +-----------+  +-----------+  +-----------+  +----------+            |  |
|  +-----------------------------------------------------------------------+  |
|                                    |                                         |
|                                    v                                         |
|  +-----------------------------------------------------------------------+  |
|  |  LAYER 3: PRODUCT TEAMS (Self-Service)                                |  |
|  |  +-------------+  +-------------+  +-------------+                    |  |
|  |  |  Team Alpha |  |  Team Beta  |  |  Team Gamma |                    |  |
|  |  |  +---------+|  |  +---------+|  |  +---------+|                    |  |
|  |  |  | App A   ||  |  | App B   ||  |  | App C   ||                    |  |
|  |  |  | App D   ||  |  | App E   ||  |  | App F   ||                    |  |
|  |  |  +---------+|  |  +---------+|  |  +---------+|                    |  |
|  |  +-------------+  +-------------+  +-------------+                    |  |
|  +-----------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------+
```

---

## Repository Structure Patterns

### Pattern 1: Monorepo Structure

```
terraform-infrastructure/
|-- .github/
|   +-- workflows/
|       |-- terraform-ci.yml
|       +-- terraform-cd.yml
|-- modules/                        # Reusable modules
|   |-- compute/
|   |-- networking/
|   |-- database/
|   +-- security/
|-- policies/                       # OPA/Sentinel policies
|   |-- security/
|   |-- cost/
|   +-- compliance/
|-- environments/                   # Environment configs
|   |-- development/
|   |-- staging/
|   +-- production/
|-- stacks/                         # Deployable stacks
|   |-- platform/
|   |   |-- networking/
|   |   |-- identity/
|   |   +-- monitoring/
|   +-- applications/
|       |-- team-alpha/
|       |-- team-beta/
|       +-- team-gamma/
+-- scripts/
```

### Pattern 2: Multi-Repo with Module Registry

```
Organization Repositories:

terraform-modules (Central)
|-- Versioned module releases
|-- Published to private registry
+-- Owned by Platform Team
    |
    v
+-----------------------------------------------------------------------+
|  Private Module Registry (Terraform Cloud/Enterprise)                  |
|  |-- networking/vpc v2.3.0                                             |
|  |-- compute/ecs v1.5.0                                                |
|  |-- database/rds v3.1.0                                               |
|  +-- security/iam v2.0.0                                               |
+-----------------------------------------------------------------------+
                                    |
      +-----------------------------+-----------------------------+
      |                             |                             |
      v                             v                             v
team-alpha-infra            team-beta-infra            team-gamma-infra
```

---

## Private Module Registry

### Module Publishing Workflow

```hcl
# modules/networking/vpc/versions.tf
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

# modules/networking/vpc/variables.tf
variable "name" {
  description = "Name prefix for VPC resources"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string

  validation {
    condition     = can(cidrnetmask(var.cidr_block))
    error_message = "Must be a valid CIDR block."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = []
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}

variable "enable_nat_gateway" {
  description = "Enable NAT Gateway for private subnets"
  type        = bool
  default     = true
}

variable "single_nat_gateway" {
  description = "Use single NAT Gateway (cost saving)"
  type        = bool
  default     = false
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {}
}
```

### Using Private Registry Modules

```hcl
# Consumer: team-alpha application
module "vpc" {
  source  = "app.terraform.io/company/vpc/aws"
  version = "~> 2.3"

  name       = "team-alpha-${var.environment}"
  cidr_block = "10.0.0.0/16"

  private_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnet_cidrs  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  single_nat_gateway = var.environment != "production"

  tags = local.common_tags
}

module "ecs_cluster" {
  source  = "app.terraform.io/company/ecs/aws"
  version = "~> 1.5"

  name               = "team-alpha-${var.environment}"
  vpc_id             = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids

  tags = local.common_tags
}

module "rds" {
  source  = "app.terraform.io/company/rds/aws"
  version = "~> 3.1"

  identifier = "team-alpha-${var.environment}"

  engine         = "postgres"
  engine_version = "15.4"
  instance_class = var.db_instance_class

  vpc_id              = module.vpc.vpc_id
  subnet_ids          = module.vpc.private_subnet_ids
  allowed_cidr_blocks = [module.vpc.vpc_cidr_block]

  tags = local.common_tags
}
```

---

## GitOps Workflow with Atlantis

### Atlantis Configuration

```yaml
# atlantis.yaml
version: 3
automerge: false
parallel_plan: true
parallel_apply: false

projects:
  - name: platform-networking
    dir: stacks/platform/networking
    workspace: production
    autoplan:
      when_modified:
        - "*.tf"
        - "../../modules/networking/**"
      enabled: true
    apply_requirements:
      - approved
      - mergeable
    workflow: platform-workflow

  - name: team-alpha-prod
    dir: stacks/applications/team-alpha
    workspace: production
    autoplan:
      when_modified:
        - "*.tf"
        - "../../modules/**"
      enabled: true
    apply_requirements:
      - approved
    workflow: team-workflow

workflows:
  platform-workflow:
    plan:
      steps:
        - init
        - run: conftest test $(terraform show -json $PLANFILE) --policy ../../../policies/
        - plan:
            extra_args: ["-var-file", "environments/production.tfvars"]
    apply:
      steps:
        - apply

  team-workflow:
    plan:
      steps:
        - init
        - run: checkov -f $(terraform show -json $PLANFILE) --framework terraform_plan
        - plan
    apply:
      steps:
        - apply
```

---

## Self-Service Platform Integration

### Backstage Template

```hcl
# templates/new-application/main.tf

variable "app_name" {
  description = "Application name (from Backstage template)"
  type        = string
}

variable "team" {
  description = "Owning team (from Backstage)"
  type        = string
}

variable "environment" {
  description = "Target environment"
  type        = string
}

variable "app_config" {
  description = "Application configuration from Backstage"
  type = object({
    container_port    = number
    cpu               = number
    memory            = number
    desired_count     = number
    health_check_path = string
    domain            = string
  })
}

# Lookup shared infrastructure
data "terraform_remote_state" "platform" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "platform/networking/terraform.tfstate"
    region = "us-east-1"
  }
}

data "terraform_remote_state" "shared" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "platform/shared/terraform.tfstate"
    region = "us-east-1"
  }
}

# Create application resources using company modules
module "ecs_service" {
  source  = "app.terraform.io/company/ecs-service/aws"
  version = "~> 2.0"

  name        = var.app_name
  environment = var.environment

  cluster_arn = data.terraform_remote_state.shared.outputs.ecs_cluster_arn
  vpc_id      = data.terraform_remote_state.platform.outputs.vpc_id
  subnet_ids  = data.terraform_remote_state.platform.outputs.private_subnet_ids

  container_port    = var.app_config.container_port
  cpu               = var.app_config.cpu
  memory            = var.app_config.memory
  desired_count     = var.app_config.desired_count
  health_check_path = var.app_config.health_check_path

  alb_listener_arn = data.terraform_remote_state.shared.outputs.alb_listener_arn
  domain           = var.app_config.domain

  tags = {
    Application = var.app_name
    Team        = var.team
    Environment = var.environment
    ManagedBy   = "Terraform"
    CreatedBy   = "Backstage"
  }
}

output "service_url" {
  value = "https://${var.app_config.domain}"
}

output "ecs_service_name" {
  value = module.ecs_service.service_name
}
```

---

## Enterprise Metrics Dashboard

```
+-----------------------------------------------------------------------------+
|                    ENTERPRISE TERRAFORM METRICS                              |
+-----------------------------------------------------------------------------+
|                                                                              |
|  OPERATIONAL METRICS:                                                        |
|  +----------------------------------------------------------------------+   |
|  |  Metric                        | Target        | Current             |   |
|  |  ------------------------------+---------------+-------------------  |   |
|  |  Plan Success Rate             | > 99%         | 99.7%               |   |
|  |  Apply Success Rate            | > 99.5%       | 99.8%               |   |
|  |  Mean Time to Deploy           | < 15 min      | 8 min               |   |
|  |  Drift Detection Rate          | < 1%          | 0.3%                |   |
|  |  Policy Compliance             | 100%          | 100%                |   |
|  |  Module Reuse Rate             | > 80%         | 87%                 |   |
|  +----------------------------------------------------------------------+   |
|                                                                              |
|  RESOURCE METRICS:                                                           |
|  +----------------------------------------------------------------------+   |
|  |  Category           | Production  | Staging     | Development        |   |
|  |  -------------------+-------------+-------------+------------------  |   |
|  |  Total Resources    | 2,450       | 1,200       | 650                |   |
|  |  State Files        | 45          | 45          | 30                 |   |
|  |  Active Workspaces  | 45          | 45          | 60                 |   |
|  |  Monthly Cost       | $125,000    | $35,000     | $15,000            |   |
|  +----------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
```

---

## Hands-On Exercise

### Exercise: Enterprise Module Structure

```hcl
# Create an enterprise-ready module with:
# 1. Version constraints
# 2. Input validation
# 3. Default tags
# 4. Comprehensive outputs
# 5. README documentation

# TODO: Complete the module structure
```
''',
    "practice_tasks": [
        "Design enterprise repository structure",
        "Implement private module registry",
        "Configure Atlantis GitOps workflow",
        "Create self-service platform integration",
        "Build enterprise metrics dashboard"
    ],
    "assessment": {
        "type": "hands-on",
        "passing_score": 85,
        "time_limit": "90 minutes"
    }
}

NODE_20 = {
    "id": "terraform_node_20",
    "slug": "terraform-advanced-state",
    "title": "Advanced State Operations - Expert-Level State Management",
    "description": "Master state surgery, migration, and recovery procedures",
    "xp_reward": 200,
    "estimated_minutes": 90,
    "node_id": 20,
    "content": '''
# Advanced State Operations - Expert-Level State Management

## State Internals

```
+-----------------------------------------------------------------------------+
|                    TERRAFORM STATE STRUCTURE                                 |
+-----------------------------------------------------------------------------+
|                                                                              |
|  {                                                                           |
|    "version": 4,                    // State format version                  |
|    "terraform_version": "1.6.0",    // TF version that wrote state          |
|    "serial": 42,                    // Incremented on each write             |
|    "lineage": "abc123...",          // Unique ID for state lineage           |
|    "outputs": {                     // Output values                         |
|      "vpc_id": {                                                             |
|        "value": "vpc-123",                                                   |
|        "type": "string"                                                      |
|      }                                                                       |
|    },                                                                        |
|    "resources": [                   // Managed resources                     |
|      {                                                                       |
|        "mode": "managed",           // managed or data                       |
|        "type": "aws_vpc",           // Resource type                         |
|        "name": "main",              // Resource name                         |
|        "provider": "provider[registry.terraform.io/hashicorp/aws]",          |
|        "instances": [...]                                                    |
|      }                                                                       |
|    ]                                                                         |
|  }                                                                           |
+-----------------------------------------------------------------------------+
```

---

## State Commands Reference

```
+-----------------------------------------------------------------------------+
|                    TERRAFORM STATE COMMANDS                                  |
+-----------------------------------------------------------------------------+
|                                                                              |
|  COMMAND                     | PURPOSE                                       |
|  ----------------------------+---------------------------------------------- |
|  terraform state list        | List resources in state                       |
|  terraform state show        | Show details of a resource                    |
|  terraform state mv          | Move/rename resource in state                 |
|  terraform state rm          | Remove resource from state                    |
|  terraform state pull        | Download remote state to stdout               |
|  terraform state push        | Upload local state to remote                  |
|  terraform state replace-provider | Replace provider in state              |
|  terraform force-unlock      | Manually unlock state                         |
|                                                                              |
|  ADVANCED OPERATIONS:                                                        |
|  ----------------------------+---------------------------------------------- |
|  terraform refresh           | Update state from real infrastructure         |
|  -replace flag               | Modern replacement for taint                  |
+-----------------------------------------------------------------------------+
```

---

## State Migration: Splitting Monolith

```bash
#!/bin/bash
# split-state.sh - Split monolith into separate state files

set -euo pipefail

echo "STATE SPLITTING OPERATION"

# Step 1: Backup current state
terraform state pull > state-backup-$(date +%Y%m%d-%H%M%S).json

# Step 2: List all resources
terraform state list

# Step 3: Define resources to move
NETWORKING_RESOURCES=(
    "aws_vpc.main"
    "aws_subnet.public[0]"
    "aws_subnet.public[1]"
    "aws_subnet.private[0]"
    "aws_subnet.private[1]"
    "aws_internet_gateway.main"
    "aws_nat_gateway.main"
)

# Step 4: Move resources to new state
cd ../networking

for resource in "${NETWORKING_RESOURCES[@]}"; do
    echo "Moving: $resource"
    terraform state mv \
        -state=../monolith/terraform.tfstate \
        -state-out=terraform.tfstate \
        "$resource" "$resource"
done

# Step 5: Verify both states
echo "Verification:"
cd ../monolith && terraform state list | wc -l
cd ../networking && terraform state list | wc -l

echo "State split complete!"
```

---

## State Recovery Procedures

```bash
#!/bin/bash
# recover-state.sh - State recovery procedures

set -euo pipefail

echo "STATE RECOVERY PROCEDURES"

# Method 1: Restore from S3 versioning
aws s3api list-object-versions \
    --bucket company-terraform-state \
    --prefix "production/terraform.tfstate" \
    --query 'Versions[].{VersionId:VersionId,LastModified:LastModified}' \
    --output table

# Restore specific version
read -p "Enter VersionId to restore: " VERSION_ID
aws s3api get-object \
    --bucket company-terraform-state \
    --key "production/terraform.tfstate" \
    --version-id "$VERSION_ID" \
    restored-state.json

# Method 2: Reconstruct with import blocks
cat > reconstruct.tf << 'EOF'
import {
  to = aws_vpc.main
  id = "vpc-12345678"
}

import {
  to = aws_subnet.public[0]
  id = "subnet-public-1"
}
EOF

# Method 3: jq manipulation
jq 'del(.resources[] | select(.name == "corrupted"))' \
    current-state.json > fixed-state.json
```

---

## Force Unlock Stuck State

```bash
#!/bin/bash
# force-unlock.sh

echo "WARNING: Force unlock should be used carefully!"

# Get lock info
terraform plan 2>&1 | grep -A5 "Lock Info" || echo "No lock found"

# Force unlock
read -p "Enter Lock ID to force unlock: " LOCK_ID

if [ -n "$LOCK_ID" ]; then
    terraform force-unlock -force "$LOCK_ID"
    echo "Lock released"
fi
```

---

## State Analysis with Python

```python
#!/usr/bin/env python3
"""state-analyzer.py - Analyze Terraform state"""

import json
import sys
from collections import defaultdict

def analyze_state(state_file: str):
    with open(state_file, 'r') as f:
        state = json.load(f)

    print("TERRAFORM STATE ANALYSIS")
    print(f"Version: {state.get('version')}")
    print(f"Terraform: {state.get('terraform_version')}")
    print(f"Serial: {state.get('serial')}")

    resources = state.get('resources', [])
    print(f"Resources: {len(resources)} total")

    # Group by type
    by_type = defaultdict(list)
    for resource in resources:
        by_type[resource.get('type', 'unknown')].append(resource)

    print("By Type:")
    for rtype, items in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"  * {rtype}: {len(items)}")

if __name__ == "__main__":
    analyze_state(sys.argv[1])
```

---

## Cross-State References

```hcl
# Using terraform_remote_state
data "terraform_remote_state" "networking" {
  backend = "s3"

  config = {
    bucket = "company-terraform-state"
    key    = "networking/terraform.tfstate"
    region = "us-east-1"
  }
}

# Reference resources from other state
resource "aws_instance" "app" {
  ami           = var.ami_id
  instance_type = "t3.medium"

  subnet_id              = data.terraform_remote_state.networking.outputs.private_subnet_ids[0]
  vpc_security_group_ids = [data.terraform_remote_state.networking.outputs.app_security_group_id]
}
```

---

## State Operations Safety Checklist

```
+-----------------------------------------------------------------------------+
|                    STATE OPERATIONS SAFETY CHECKLIST                         |
+-----------------------------------------------------------------------------+
|                                                                              |
|  BEFORE ANY STATE OPERATION:                                                 |
|  +----------------------------------------------------------------------+   |
|  | [ ] Create state backup: terraform state pull > backup.json          |   |
|  | [ ] Verify S3 versioning is enabled                                  |   |
|  | [ ] Document current state: terraform state list > resources.txt     |   |
|  | [ ] Notify team of planned maintenance                               |   |
|  | [ ] Ensure no other operations are running                           |   |
|  | [ ] Test operation in non-production first                           |   |
|  +----------------------------------------------------------------------+   |
|                                                                              |
|  AFTER STATE OPERATION:                                                      |
|  +----------------------------------------------------------------------+   |
|  | [ ] Run terraform plan - should show expected changes only           |   |
|  | [ ] Verify resource counts match expectations                        |   |
|  | [ ] Test infrastructure functionality                                |   |
|  | [ ] Update documentation                                             |   |
|  +----------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------+
```

---

## Hands-On Exercise

### Exercise: State Surgery

```bash
# Scenario: Split monolith state into domain-specific states

# Current structure (monolith):
# - VPC, Subnets, IGW, NAT
# - ECS Cluster, Services
# - RDS Databases
# - S3 Buckets
# - IAM Roles

# Target structure:
# - networking/ (VPC, Subnets, IGW, NAT)
# - compute/ (ECS Cluster, Services)
# - data/ (RDS, S3)
# - security/ (IAM Roles)

# TODO 1: Backup current state
# TODO 2: Create directory structure
# TODO 3: Move resources to appropriate states
# TODO 4: Update configurations to use remote state references
# TODO 5: Verify all states with terraform plan
```

### Expected Results

```
+-----------------------------------------------------------------------------+
|                    STATE SURGERY RESULTS                                     |
+-----------------------------------------------------------------------------+
|                                                                              |
|  Original State: 45 resources                                                |
|                                                                              |
|  After Split:                                                                |
|  |-- networking/: 12 resources                                               |
|  |-- compute/: 15 resources                                                  |
|  |-- data/: 10 resources                                                     |
|  +-- security/: 8 resources                                                  |
|                                                                              |
|  Verification:                                                               |
|  |-- All terraform plan commands show "No changes"                           |
|  |-- Cross-state references working                                          |
|  +-- Infrastructure unchanged                                                |
+-----------------------------------------------------------------------------+
```
''',
    "practice_tasks": [
        "Analyze state structure with Python/jq",
        "Split monolith state into domains",
        "Recover from corrupted state",
        "Migrate between providers",
        "Implement cross-state references"
    ],
    "assessment": {
        "type": "practical",
        "passing_score": 90,
        "time_limit": "90 minutes"
    }
}

# Export for __init__.py
BLOCK_5_PART_2_NODES = [NODE_19, NODE_20]
