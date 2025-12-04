"""
Terraform V3 SkillsMap - Block 5 Part 1: Production & Security
Nodes 17-18: Security hardening and multi-cloud strategies.
Target: ~10,000+ chars per node with ASCII diagrams, tables, and practical exercises.
"""

# =============================================================================
# NODE 17: TERRAFORM SECURITY HARDENING
# =============================================================================

NODE_17_SECURITY = {
    "id": "terraform-security-hardening",
    "slug": "terraform-security-hardening",
    "title": "Terraform Security Hardening: Enterprise-Grade Protection",
    "xp_reward": 200,
    "estimated_minutes": 90,
    "type": "advanced",
    "duration": "90 minutes",
    "prerequisites": ["terraform-state-management", "terraform-modules"],
    "objectives": [
        "Implement secrets management best practices",
        "Secure state file storage and access",
        "Apply policy-as-code with Sentinel/OPA",
        "Design secure CI/CD pipelines for Terraform"
    ],
    "content": """
# TERRAFORM SECURITY HARDENING: ENTERPRISE-GRADE PROTECTION

## 🔐 SECURITY ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 TERRAFORM SECURITY LAYERS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 1: SECRETS MANAGEMENT                                         │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐            │   │
│  │  │  HashiCorp    │  │  AWS Secrets  │  │  Azure Key    │            │   │
│  │  │  Vault        │  │  Manager      │  │  Vault        │            │   │
│  │  └───────────────┘  └───────────────┘  └───────────────┘            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 2: STATE FILE PROTECTION                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  • Encryption at rest (KMS/HSM)                               │  │   │
│  │  │  • Encryption in transit (TLS 1.3)                            │  │   │
│  │  │  • Access control (IAM policies)                              │  │   │
│  │  │  • State locking (DynamoDB/Consul)                            │  │   │
│  │  │  • Audit logging (CloudTrail/Activity Log)                    │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 3: POLICY ENFORCEMENT                                         │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐            │   │
│  │  │  Sentinel     │  │  OPA/Conftest │  │  Checkov      │            │   │
│  │  │  (Enterprise) │  │  (Open Source)│  │  (Security)   │            │   │
│  │  └───────────────┘  └───────────────┘  └───────────────┘            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 4: CI/CD SECURITY                                             │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  • Least privilege service accounts                           │  │   │
│  │  │  • Ephemeral credentials (OIDC)                               │  │   │
│  │  │  • Plan/Apply separation                                      │  │   │
│  │  │  • Manual approval gates                                      │  │   │
│  │  │  • Artifact signing                                           │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔑 SECRETS MANAGEMENT

### Anti-Pattern: Hardcoded Secrets

```hcl
# ❌ NEVER DO THIS - Secrets in code
resource "aws_db_instance" "main" {
  identifier = "production-db"
  engine     = "postgres"

  # DANGEROUS: Hardcoded credentials
  username = "admin"
  password = "SuperSecret123!"  # This will be in state AND version control!
}

# ❌ NEVER DO THIS - Secrets in variables with defaults
variable "db_password" {
  default = "SuperSecret123!"  # Still exposed
}
```

### Pattern 1: Environment Variables

```hcl
# ✅ Use environment variables
# Set in shell: export TF_VAR_db_password="secure-password-from-vault"

variable "db_password" {
  description = "Database password - set via TF_VAR_db_password"
  type        = string
  sensitive   = true  # Mark as sensitive

  # No default - must be provided
  validation {
    condition     = length(var.db_password) >= 16
    error_message = "Database password must be at least 16 characters."
  }
}

resource "aws_db_instance" "main" {
  identifier = "production-db"
  engine     = "postgres"
  username   = "admin"
  password   = var.db_password  # From environment variable
}
```

### Pattern 2: HashiCorp Vault Integration

```hcl
# Using Vault for secrets management
provider "vault" {
  address = "https://vault.company.com:8200"

  # Use token from environment or other auth method
  # Auth methods: token, approle, aws, kubernetes, etc.
}

# Read secrets from Vault
data "vault_kv_secret_v2" "database" {
  mount = "secret"
  name  = "production/database"
}

data "vault_kv_secret_v2" "api_keys" {
  mount = "secret"
  name  = "production/api-keys"
}

# Use secrets in resources
resource "aws_db_instance" "main" {
  identifier = "production-db"
  engine     = "postgres"

  username = data.vault_kv_secret_v2.database.data["username"]
  password = data.vault_kv_secret_v2.database.data["password"]
}

resource "aws_secretsmanager_secret_version" "api_key" {
  secret_id = aws_secretsmanager_secret.api_key.id
  secret_string = jsonencode({
    api_key    = data.vault_kv_secret_v2.api_keys.data["api_key"]
    api_secret = data.vault_kv_secret_v2.api_keys.data["api_secret"]
  })
}

# Dynamic database credentials (recommended for production)
data "vault_database_secret" "creds" {
  backend = "database"
  name    = "readonly-role"  # Vault database role
}

# These credentials automatically rotate!
locals {
  db_username = data.vault_database_secret.creds.username
  db_password = data.vault_database_secret.creds.password
}
```

### Pattern 3: AWS Secrets Manager

```hcl
# Using AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db_credentials" {
  secret_id = "production/database/credentials"
}

locals {
  db_creds = jsondecode(data.aws_secretsmanager_secret_version.db_credentials.secret_string)
}

resource "aws_db_instance" "main" {
  identifier = "production-db"
  engine     = "postgres"

  username = local.db_creds["username"]
  password = local.db_creds["password"]

  # Enable automatic rotation
  manage_master_user_password   = true
  master_user_secret_kms_key_id = aws_kms_key.db_secrets.arn
}

# Create secret with rotation
resource "aws_secretsmanager_secret" "db_credentials" {
  name        = "production/database/credentials"
  description = "Database credentials for production"

  kms_key_id = aws_kms_key.secrets.arn

  # Rotation configuration
  rotation_rules {
    automatically_after_days = 30
  }
}

resource "aws_secretsmanager_secret_rotation" "db_credentials" {
  secret_id           = aws_secretsmanager_secret.db_credentials.id
  rotation_lambda_arn = aws_lambda_function.secret_rotation.arn

  rotation_rules {
    automatically_after_days = 30
  }
}
```

---

## 🔒 STATE FILE SECURITY

### Secure Backend Configuration

```hcl
# Secure S3 backend with all protections enabled
terraform {
  backend "s3" {
    bucket = "company-terraform-state"
    key    = "production/infrastructure.tfstate"
    region = "us-east-1"

    # Encryption
    encrypt        = true
    kms_key_id     = "alias/terraform-state-key"

    # Locking
    dynamodb_table = "terraform-locks"

    # Access Control
    acl = "private"

    # Additional security
    skip_metadata_api_check = true  # Don't use IMDS for credentials
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# S3 bucket for state (created separately, typically by a bootstrap module)
resource "aws_s3_bucket" "terraform_state" {
  bucket = "company-terraform-state"

  tags = {
    Name        = "Terraform State"
    Environment = "Management"
    ManagedBy   = "Terraform"
  }
}

# Block all public access
resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Enable versioning for state history
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Server-side encryption with KMS
resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.terraform_state.arn
    }
    bucket_key_enabled = true
  }
}

# KMS key for state encryption
resource "aws_kms_key" "terraform_state" {
  description             = "KMS key for Terraform state encryption"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      },
      {
        Sid    = "Allow Terraform Role"
        Effect = "Allow"
        Principal = {
          AWS = aws_iam_role.terraform.arn
        }
        Action = [
          "kms:Encrypt",
          "kms:Decrypt",
          "kms:GenerateDataKey*",
          "kms:DescribeKey"
        ]
        Resource = "*"
      }
    ]
  })

  tags = {
    Name      = "terraform-state-key"
    ManagedBy = "Terraform"
  }
}

# DynamoDB table for state locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  # Enable point-in-time recovery
  point_in_time_recovery {
    enabled = true
  }

  # Enable encryption
  server_side_encryption {
    enabled     = true
    kms_key_arn = aws_kms_key.terraform_state.arn
  }

  tags = {
    Name      = "Terraform Locks"
    ManagedBy = "Terraform"
  }
}

# Enable CloudTrail for state access auditing
resource "aws_cloudtrail" "terraform_audit" {
  name                          = "terraform-state-audit"
  s3_bucket_name                = aws_s3_bucket.audit_logs.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true

  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["${aws_s3_bucket.terraform_state.arn}/"]
    }
  }

  tags = {
    Name      = "Terraform State Audit Trail"
    ManagedBy = "Terraform"
  }
}
```

---

## 📜 POLICY AS CODE

### OPA/Conftest Policies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POLICY-AS-CODE ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     TERRAFORM PLAN                                    │   │
│  │  terraform plan -out=tfplan                                           │   │
│  │  terraform show -json tfplan > plan.json                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     POLICY ENGINE                                     │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  • Conftest (OPA)    - Open source                            │  │   │
│  │  │  • Sentinel          - HashiCorp Enterprise                   │  │   │
│  │  │  • Checkov           - Security scanning                      │  │   │
│  │  │  • tfsec             - Security analysis                      │  │   │
│  │  │  • Regula            - Compliance checking                    │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     POLICY DECISION                                   │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │   │
│  │  │  ✅ ALLOW   │  │  ⚠️ WARN    │  │  ❌ DENY    │                  │   │
│  │  │  Continue   │  │  Log/Alert  │  │  Block      │                  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Conftest/OPA Policies

```rego
# policy/terraform/security.rego
package terraform.security

import input as tfplan

# Deny public S3 buckets
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_s3_bucket"
    resource.change.after.acl == "public-read"

    msg := sprintf(
        "S3 bucket '%s' has public-read ACL. Public buckets are not allowed.",
        [resource.address]
    )
}

deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_s3_bucket"
    resource.change.after.acl == "public-read-write"

    msg := sprintf(
        "S3 bucket '%s' has public-read-write ACL. This is extremely dangerous!",
        [resource.address]
    )
}

# Require encryption on RDS instances
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_db_instance"
    not resource.change.after.storage_encrypted

    msg := sprintf(
        "RDS instance '%s' does not have storage encryption enabled.",
        [resource.address]
    )
}

# Require encryption on EBS volumes
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_ebs_volume"
    not resource.change.after.encrypted

    msg := sprintf(
        "EBS volume '%s' is not encrypted. All volumes must be encrypted.",
        [resource.address]
    )
}

# Deny overly permissive security groups
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_security_group_rule"
    resource.change.after.type == "ingress"
    resource.change.after.cidr_blocks[_] == "0.0.0.0/0"
    resource.change.after.from_port == 22

    msg := sprintf(
        "Security group rule '%s' allows SSH from 0.0.0.0/0. Use VPN or bastion.",
        [resource.address]
    )
}

deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_security_group_rule"
    resource.change.after.type == "ingress"
    resource.change.after.cidr_blocks[_] == "0.0.0.0/0"
    resource.change.after.from_port == 3389

    msg := sprintf(
        "Security group rule '%s' allows RDP from 0.0.0.0/0. Use VPN or bastion.",
        [resource.address]
    )
}

# Require specific tags
required_tags := {"Environment", "Owner", "Project", "CostCenter"}

deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_instance"
    tags := {tag | resource.change.after.tags[tag]}
    missing := required_tags - tags
    count(missing) > 0

    msg := sprintf(
        "EC2 instance '%s' is missing required tags: %v",
        [resource.address, missing]
    )
}

# Deny large instance types without approval
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_instance"
    instance_type := resource.change.after.instance_type
    startswith(instance_type, "x1")

    msg := sprintf(
        "Instance '%s' uses expensive x1 instance type. Requires cost approval.",
        [resource.address]
    )
}

# Warn on instance type changes (potential downtime)
warn[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_instance"
    resource.change.actions[_] == "update"
    resource.change.before.instance_type != resource.change.after.instance_type

    msg := sprintf(
        "Instance '%s' instance type changing from %s to %s. May cause downtime.",
        [resource.address, resource.change.before.instance_type, resource.change.after.instance_type]
    )
}
```

### Running Conftest

```bash
#!/bin/bash
# run-policy-check.sh

set -euo pipefail

echo "╔═══════════════════════════════════════════════════╗"
echo "║     TERRAFORM POLICY VALIDATION                   ║"
echo "╚═══════════════════════════════════════════════════╝"

# Generate plan JSON
echo "📋 Generating Terraform plan..."
terraform plan -out=tfplan -no-color
terraform show -json tfplan > plan.json

# Run Conftest
echo ""
echo "🔍 Running policy checks..."
conftest test plan.json \\
  --policy policy/ \\
  --output table \\
  --all-namespaces

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All policy checks passed!"
else
    echo ""
    echo "❌ Policy violations detected. Fix before applying."
    exit 1
fi

# Additional security scanning with Checkov
echo ""
echo "🔒 Running security scan with Checkov..."
checkov -f plan.json \\
  --framework terraform_plan \\
  --output cli \\
  --soft-fail
```

---

## 🛡️ CI/CD SECURITY

### Secure GitHub Actions Workflow

```yaml
# .github/workflows/terraform.yml
name: Terraform Security Pipeline

on:
  pull_request:
    branches: [main]
    paths:
      - 'terraform/**'
      - '.github/workflows/terraform.yml'
  push:
    branches: [main]
    paths:
      - 'terraform/**'

permissions:
  id-token: write  # Required for OIDC
  contents: read
  pull-requests: write

env:
  TF_VERSION: "1.6.0"
  AWS_REGION: "us-east-1"

jobs:
  security-scan:
    name: Security Scanning
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform/
          framework: terraform
          output_format: sarif
          output_file_path: reports/checkov.sarif
          soft_fail: false

      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          working_directory: terraform/
          soft_fail: false

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: reports/

  terraform-plan:
    name: Terraform Plan
    runs-on: ubuntu-latest
    needs: security-scan
    environment: production-plan  # Requires approval

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          role-session-name: terraform-plan
          aws-region: ${{ env.AWS_REGION }}

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Init
        working-directory: terraform/
        run: terraform init -backend-config=backends/production.hcl

      - name: Terraform Validate
        working-directory: terraform/
        run: terraform validate

      - name: Terraform Plan
        working-directory: terraform/
        run: |
          terraform plan \\
            -var-file=environments/production.tfvars \\
            -out=tfplan \\
            -no-color

      - name: Policy Check (Conftest)
        working-directory: terraform/
        run: |
          terraform show -json tfplan > plan.json
          conftest test plan.json --policy ../policy/

      - name: Upload Plan Artifact
        uses: actions/upload-artifact@v4
        with:
          name: terraform-plan
          path: terraform/tfplan
          retention-days: 5

  terraform-apply:
    name: Terraform Apply
    runs-on: ubuntu-latest
    needs: terraform-plan
    if: github.ref == 'refs/heads/main'
    environment: production-apply  # Requires manual approval

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download Plan Artifact
        uses: actions/download-artifact@v4
        with:
          name: terraform-plan
          path: terraform/

      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          role-session-name: terraform-apply
          aws-region: ${{ env.AWS_REGION }}

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Init
        working-directory: terraform/
        run: terraform init -backend-config=backends/production.hcl

      - name: Terraform Apply
        working-directory: terraform/
        run: terraform apply -auto-approve tfplan
```

### OIDC IAM Role for GitHub Actions

```hcl
# GitHub OIDC provider
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = ["sts.amazonaws.com"]

  thumbprint_list = [
    "6938fd4d98bab03faadb97b34396831e3780aea1",
    "1c58a3a8518e8759bf075b76b750d4f2df264fcd"
  ]
}

# IAM role for GitHub Actions
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
            "token.actions.githubusercontent.com:sub" = "repo:your-org/your-repo:*"
          }
        }
      }
    ]
  })

  tags = {
    Name      = "GitHub Actions Role"
    ManagedBy = "Terraform"
  }
}

# Attach necessary permissions
resource "aws_iam_role_policy_attachment" "github_actions" {
  role       = aws_iam_role.github_actions.name
  policy_arn = aws_iam_policy.terraform_permissions.arn
}

resource "aws_iam_policy" "terraform_permissions" {
  name        = "TerraformPermissions"
  description = "Permissions for Terraform to manage infrastructure"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ec2:*",
          "s3:*",
          "rds:*",
          "elasticloadbalancing:*",
          "ecs:*",
          "ecr:*",
          "logs:*",
          "cloudwatch:*"
        ]
        Resource = "*"
        Condition = {
          StringEquals = {
            "aws:RequestedRegion" = ["us-east-1", "us-west-2"]
          }
        }
      },
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = "arn:aws:s3:::company-terraform-state/*"
      },
      {
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:DeleteItem"
        ]
        Resource = "arn:aws:dynamodb:*:*:table/terraform-locks"
      }
    ]
  })
}
```

---

## 🧪 HANDS-ON EXERCISE

### Exercise: Implement Security Hardening

```hcl
# Complete this security-hardened configuration

# TODO 1: Configure secure S3 backend
terraform {
  backend "s3" {
    # Your secure configuration here
  }
}

# TODO 2: Implement Vault integration for secrets
data "vault_kv_secret_v2" "db_creds" {
  # Your configuration here
}

# TODO 3: Create security group with least privilege
resource "aws_security_group" "app" {
  # Your secure configuration here
}

# TODO 4: Create KMS key with proper policy
resource "aws_kms_key" "data" {
  # Your configuration here
}
```

### Validation Commands

```bash
# Run security validation
checkov -d . --framework terraform
tfsec .
conftest test . --policy policy/

# All commands should pass with no high-severity findings
```
""",
    "practice_tasks": [
        "Configure Vault integration for secrets",
        "Set up encrypted state backend with audit logging",
        "Write OPA policies for security compliance",
        "Implement OIDC authentication for CI/CD",
        "Create security scanning pipeline"
    ],
    "assessment": {
        "type": "hands-on",
        "passing_score": 90,
        "time_limit": "60 minutes"
    }
}

# =============================================================================
# NODE 18: MULTI-CLOUD TERRAFORM
# =============================================================================

NODE_18_MULTI_CLOUD = {
    "id": "terraform-multi-cloud",
    "slug": "terraform-multi-cloud",
    "title": "Multi-Cloud Terraform: Cross-Platform Infrastructure",
    "xp_reward": 200,
    "estimated_minutes": 90,
    "type": "advanced",
    "duration": "90 minutes",
    "prerequisites": ["terraform-providers", "terraform-modules"],
    "objectives": [
        "Design multi-cloud architectures with Terraform",
        "Implement provider aliases for multi-region/account",
        "Create cloud-agnostic modules",
        "Handle cross-cloud networking and services"
    ],
    "content": """
# MULTI-CLOUD TERRAFORM: CROSS-PLATFORM INFRASTRUCTURE

## 🌐 MULTI-CLOUD ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTI-CLOUD TERRAFORM ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     TERRAFORM CONFIGURATION                          │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  providers.tf  │  variables.tf  │  modules/  │  environments/ │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│           ┌────────────────────────┼────────────────────────┐               │
│           │                        │                        │               │
│           ▼                        ▼                        ▼               │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐           │
│  │      AWS        │   │     AZURE       │   │      GCP        │           │
│  │   Provider      │   │   Provider      │   │   Provider      │           │
│  ├─────────────────┤   ├─────────────────┤   ├─────────────────┤           │
│  │ • EC2/ECS       │   │ • VMs/AKS       │   │ • GCE/GKE       │           │
│  │ • RDS/Aurora    │   │ • SQL/CosmosDB  │   │ • Cloud SQL     │           │
│  │ • S3/CloudFront │   │ • Blob/CDN      │   │ • GCS/CDN       │           │
│  │ • VPC/Direct    │   │ • VNet/Express  │   │ • VPC/Interconn │           │
│  │   Connect       │   │   Route         │   │                 │           │
│  └─────────────────┘   └─────────────────┘   └─────────────────┘           │
│           │                        │                        │               │
│           └────────────────────────┼────────────────────────┘               │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     UNIFIED STATE MANAGEMENT                          │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  Remote State Backend (S3/GCS/Azure Blob)                     │  │   │
│  │  │  • Cross-cloud resource references                            │  │   │
│  │  │  • Unified outputs and data sharing                           │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 MULTI-PROVIDER CONFIGURATION

### Basic Multi-Cloud Setup

```hcl
# versions.tf - Multi-cloud provider requirements
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

# providers.tf - Multi-cloud provider configuration
provider "aws" {
  region = "us-east-1"

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      Cloud       = "AWS"
      ManagedBy   = "Terraform"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = var.azure_subscription_id
  tenant_id       = var.azure_tenant_id
}

provider "google" {
  project = var.gcp_project_id
  region  = "us-central1"
}

# Provider aliases for multi-region
provider "aws" {
  alias  = "us_west"
  region = "us-west-2"

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      Cloud       = "AWS"
      Region      = "us-west-2"
      ManagedBy   = "Terraform"
    }
  }
}

provider "aws" {
  alias  = "eu_west"
  region = "eu-west-1"

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      Cloud       = "AWS"
      Region      = "eu-west-1"
      ManagedBy   = "Terraform"
    }
  }
}
```

---

## 🏗️ CLOUD-AGNOSTIC MODULE PATTERNS

### Pattern 1: Abstraction Layer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CLOUD-AGNOSTIC MODULE ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     ABSTRACTION LAYER                                 │   │
│  │                     (Generic Interface)                               │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  module "compute" {                                            │  │   │
│  │  │    source       = "./modules/compute"                          │  │   │
│  │  │    cloud        = "aws"  # or "azure" or "gcp"                │  │   │
│  │  │    instance_size = "medium"                                    │  │   │
│  │  │    count        = 3                                            │  │   │
│  │  │  }                                                             │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     CLOUD-SPECIFIC IMPLEMENTATIONS                    │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │   │
│  │  │     AWS     │  │    AZURE    │  │     GCP     │                  │   │
│  │  │ aws_instance│  │ azurerm_vm  │  │google_compute│                 │   │
│  │  │ t3.medium   │  │Standard_D2s │  │ n1-standard-2│                 │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Abstract Compute Module

```hcl
# modules/compute/variables.tf
variable "cloud" {
  description = "Target cloud provider"
  type        = string

  validation {
    condition     = contains(["aws", "azure", "gcp"], var.cloud)
    error_message = "Cloud must be one of: aws, azure, gcp."
  }
}

variable "instance_size" {
  description = "Abstract instance size (small, medium, large, xlarge)"
  type        = string
  default     = "medium"

  validation {
    condition     = contains(["small", "medium", "large", "xlarge"], var.instance_size)
    error_message = "Instance size must be one of: small, medium, large, xlarge."
  }
}

variable "instance_count" {
  description = "Number of instances to create"
  type        = number
  default     = 1
}

variable "name" {
  description = "Name prefix for resources"
  type        = string
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {}
}

# modules/compute/locals.tf
locals {
  # Instance type mapping across clouds
  instance_type_map = {
    aws = {
      small  = "t3.small"
      medium = "t3.medium"
      large  = "t3.large"
      xlarge = "t3.xlarge"
    }
    azure = {
      small  = "Standard_B1s"
      medium = "Standard_D2s_v3"
      large  = "Standard_D4s_v3"
      xlarge = "Standard_D8s_v3"
    }
    gcp = {
      small  = "e2-small"
      medium = "e2-medium"
      large  = "e2-standard-4"
      xlarge = "e2-standard-8"
    }
  }

  instance_type = local.instance_type_map[var.cloud][var.instance_size]

  common_tags = merge(var.tags, {
    Module    = "compute"
    Cloud     = var.cloud
    ManagedBy = "Terraform"
  })
}

# modules/compute/main.tf
# AWS Implementation
resource "aws_instance" "this" {
  count = var.cloud == "aws" ? var.instance_count : 0

  ami           = data.aws_ami.ubuntu[0].id
  instance_type = local.instance_type

  tags = merge(local.common_tags, {
    Name = "${var.name}-${count.index + 1}"
  })
}

data "aws_ami" "ubuntu" {
  count       = var.cloud == "aws" ? 1 : 0
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# Azure Implementation
resource "azurerm_linux_virtual_machine" "this" {
  count = var.cloud == "azure" ? var.instance_count : 0

  name                = "${var.name}-${count.index + 1}"
  resource_group_name = var.azure_resource_group
  location            = var.azure_location
  size                = local.instance_type

  admin_username = "adminuser"
  admin_ssh_key {
    username   = "adminuser"
    public_key = var.ssh_public_key
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  tags = local.common_tags
}

# GCP Implementation
resource "google_compute_instance" "this" {
  count = var.cloud == "gcp" ? var.instance_count : 0

  name         = "${var.name}-${count.index + 1}"
  machine_type = local.instance_type
  zone         = var.gcp_zone

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  labels = local.common_tags
}

# modules/compute/outputs.tf
output "instance_ids" {
  description = "IDs of created instances"
  value = coalesce(
    var.cloud == "aws" ? aws_instance.this[*].id : null,
    var.cloud == "azure" ? azurerm_linux_virtual_machine.this[*].id : null,
    var.cloud == "gcp" ? google_compute_instance.this[*].instance_id : null,
    []
  )
}

output "private_ips" {
  description = "Private IP addresses of instances"
  value = coalesce(
    var.cloud == "aws" ? aws_instance.this[*].private_ip : null,
    var.cloud == "azure" ? azurerm_linux_virtual_machine.this[*].private_ip_address : null,
    var.cloud == "gcp" ? google_compute_instance.this[*].network_interface[0].network_ip : null,
    []
  )
}
```

---

## 🌉 CROSS-CLOUD NETWORKING

### VPN/Interconnect Between Clouds

```hcl
# Cross-cloud VPN between AWS and GCP

# AWS Side - Customer Gateway and VPN
resource "aws_customer_gateway" "gcp" {
  bgp_asn    = 65000
  ip_address = google_compute_address.vpn.address
  type       = "ipsec.1"

  tags = {
    Name = "gcp-customer-gateway"
  }
}

resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "aws-vpn-gateway"
  }
}

resource "aws_vpn_connection" "gcp" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.gcp.id
  type                = "ipsec.1"
  static_routes_only  = true

  tags = {
    Name = "aws-to-gcp-vpn"
  }
}

resource "aws_vpn_connection_route" "gcp" {
  destination_cidr_block = var.gcp_vpc_cidr
  vpn_connection_id      = aws_vpn_connection.gcp.id
}

# GCP Side - VPN Gateway and Tunnel
resource "google_compute_address" "vpn" {
  name   = "vpn-static-ip"
  region = var.gcp_region
}

resource "google_compute_vpn_gateway" "main" {
  name    = "gcp-vpn-gateway"
  network = google_compute_network.main.id
  region  = var.gcp_region
}

resource "google_compute_forwarding_rule" "esp" {
  name        = "vpn-esp"
  ip_protocol = "ESP"
  ip_address  = google_compute_address.vpn.address
  target      = google_compute_vpn_gateway.main.self_link
  region      = var.gcp_region
}

resource "google_compute_forwarding_rule" "udp500" {
  name        = "vpn-udp500"
  ip_protocol = "UDP"
  port_range  = "500"
  ip_address  = google_compute_address.vpn.address
  target      = google_compute_vpn_gateway.main.self_link
  region      = var.gcp_region
}

resource "google_compute_forwarding_rule" "udp4500" {
  name        = "vpn-udp4500"
  ip_protocol = "UDP"
  port_range  = "4500"
  ip_address  = google_compute_address.vpn.address
  target      = google_compute_vpn_gateway.main.self_link
  region      = var.gcp_region
}

resource "google_compute_vpn_tunnel" "aws" {
  name          = "gcp-to-aws-tunnel"
  peer_ip       = aws_vpn_connection.gcp.tunnel1_address
  shared_secret = aws_vpn_connection.gcp.tunnel1_preshared_key

  target_vpn_gateway = google_compute_vpn_gateway.main.self_link

  local_traffic_selector  = [var.gcp_vpc_cidr]
  remote_traffic_selector = [var.aws_vpc_cidr]

  depends_on = [
    google_compute_forwarding_rule.esp,
    google_compute_forwarding_rule.udp500,
    google_compute_forwarding_rule.udp4500
  ]
}

# Route from GCP to AWS
resource "google_compute_route" "to_aws" {
  name                = "route-to-aws"
  network             = google_compute_network.main.name
  dest_range          = var.aws_vpc_cidr
  priority            = 1000
  next_hop_vpn_tunnel = google_compute_vpn_tunnel.aws.self_link
}
```

---

## 📊 MULTI-CLOUD DECISION MATRIX

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTI-CLOUD SERVICE MAPPING                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SERVICE TYPE    │ AWS               │ AZURE             │ GCP              │
│  ────────────────┼───────────────────┼───────────────────┼──────────────    │
│  Compute         │ EC2, ECS, Lambda  │ VMs, ACI, Func    │ GCE, Run, Func   │
│  Kubernetes      │ EKS               │ AKS               │ GKE              │
│  Database        │ RDS, DynamoDB     │ SQL, CosmosDB     │ Cloud SQL, Spanner│
│  Object Storage  │ S3                │ Blob Storage      │ Cloud Storage    │
│  CDN             │ CloudFront        │ Azure CDN         │ Cloud CDN        │
│  DNS             │ Route 53          │ Azure DNS         │ Cloud DNS        │
│  Load Balancer   │ ALB/NLB           │ Load Balancer     │ Cloud LB         │
│  VPN             │ Site-to-Site VPN  │ VPN Gateway       │ Cloud VPN        │
│  IAM             │ IAM               │ Azure AD          │ Cloud IAM        │
│  Secrets         │ Secrets Manager   │ Key Vault         │ Secret Manager   │
│  Monitoring      │ CloudWatch        │ Azure Monitor     │ Cloud Monitoring │
│                                                                              │
│  TERRAFORM RESOURCES:                                                        │
│  ────────────────┼───────────────────┼───────────────────┼──────────────    │
│  Compute         │ aws_instance      │ azurerm_linux_vm  │ google_compute   │
│  K8s Cluster     │ aws_eks_cluster   │ azurerm_aks_clust │ google_container │
│  RDS             │ aws_db_instance   │ azurerm_mssql_db  │ google_sql_db    │
│  Storage         │ aws_s3_bucket     │ azurerm_storage   │ google_storage   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 MULTI-REGION FAILOVER

```hcl
# Multi-region active-passive failover configuration

# Primary Region (AWS us-east-1)
module "primary_region" {
  source = "./modules/app-stack"

  providers = {
    aws = aws.primary
  }

  region       = "us-east-1"
  is_primary   = true
  db_replica   = false

  vpc_cidr     = "10.0.0.0/16"
  environment  = var.environment
}

# Secondary Region (AWS us-west-2)
module "secondary_region" {
  source = "./modules/app-stack"

  providers = {
    aws = aws.secondary
  }

  region       = "us-west-2"
  is_primary   = false
  db_replica   = true

  vpc_cidr     = "10.1.0.0/16"
  environment  = var.environment

  # Read replica from primary
  primary_db_arn = module.primary_region.db_arn
}

# Global Accelerator for failover
resource "aws_globalaccelerator_accelerator" "app" {
  name            = "${var.project_name}-global"
  ip_address_type = "IPV4"
  enabled         = true

  attributes {
    flow_logs_enabled   = true
    flow_logs_s3_bucket = aws_s3_bucket.logs.id
    flow_logs_s3_prefix = "global-accelerator/"
  }
}

resource "aws_globalaccelerator_listener" "app" {
  accelerator_arn = aws_globalaccelerator_accelerator.app.id
  protocol        = "TCP"

  port_range {
    from_port = 443
    to_port   = 443
  }
}

resource "aws_globalaccelerator_endpoint_group" "primary" {
  listener_arn = aws_globalaccelerator_listener.app.id

  endpoint_group_region         = "us-east-1"
  health_check_interval_seconds = 10
  health_check_path             = "/health"
  health_check_port             = 443
  health_check_protocol         = "HTTPS"
  threshold_count               = 3
  traffic_dial_percentage       = 100

  endpoint_configuration {
    endpoint_id                    = module.primary_region.alb_arn
    weight                         = 100
    client_ip_preservation_enabled = true
  }
}

resource "aws_globalaccelerator_endpoint_group" "secondary" {
  listener_arn = aws_globalaccelerator_listener.app.id

  endpoint_group_region         = "us-west-2"
  health_check_interval_seconds = 10
  health_check_path             = "/health"
  health_check_port             = 443
  health_check_protocol         = "HTTPS"
  threshold_count               = 3
  traffic_dial_percentage       = 0  # Standby - activate during failover

  endpoint_configuration {
    endpoint_id                    = module.secondary_region.alb_arn
    weight                         = 100
    client_ip_preservation_enabled = true
  }
}

# Route53 health check for primary
resource "aws_route53_health_check" "primary" {
  fqdn              = module.primary_region.alb_dns_name
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = 3
  request_interval  = 10

  tags = {
    Name = "primary-health-check"
  }
}

# DNS failover
resource "aws_route53_record" "app" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "app.${var.domain}"
  type    = "A"

  alias {
    name                   = aws_globalaccelerator_accelerator.app.dns_name
    zone_id                = aws_globalaccelerator_accelerator.app.hosted_zone_id
    evaluate_target_health = true
  }
}
```

---

## 🧪 HANDS-ON EXERCISE

### Exercise: Multi-Cloud Deployment

```hcl
# Deploy the same application to AWS and GCP

# TODO 1: Configure providers for both clouds
# Your code here

# TODO 2: Create cloud-agnostic compute module
module "aws_compute" {
  source = "./modules/compute"
  cloud  = "aws"
  # Your configuration here
}

module "gcp_compute" {
  source = "./modules/compute"
  cloud  = "gcp"
  # Your configuration here
}

# TODO 3: Set up cross-cloud DNS
# Your code here

# TODO 4: Configure cross-cloud VPN
# Your code here
```

### Expected Result

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTI-CLOUD DEPLOYMENT RESULT                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AWS (us-east-1):                                                            │
│  ├── EC2 Instances: 3x t3.medium                                             │
│  ├── ALB: app-alb-123.elb.amazonaws.com                                      │
│  └── VPC: 10.0.0.0/16                                                        │
│                                                                              │
│  GCP (us-central1):                                                          │
│  ├── GCE Instances: 3x e2-medium                                             │
│  ├── Load Balancer: 34.102.xxx.xxx                                           │
│  └── VPC: 10.1.0.0/16                                                        │
│                                                                              │
│  Cross-Cloud:                                                                │
│  ├── VPN Tunnel: Active (IKEv2)                                              │
│  ├── DNS: app.example.com → Global Load Balancer                             │
│  └── Latency: <50ms between clouds                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```
""",
    "practice_tasks": [
        "Configure multi-provider Terraform project",
        "Create cloud-agnostic compute module",
        "Set up cross-cloud VPN tunnel",
        "Implement multi-region failover",
        "Design disaster recovery architecture"
    ],
    "assessment": {
        "type": "hands-on",
        "passing_score": 85,
        "time_limit": "90 minutes"
    }
}

# =============================================================================
# BLOCK 5 PART 1 EXPORT
# =============================================================================

BLOCK_5_PART_1_NODES = [NODE_17_SECURITY, NODE_18_MULTI_CLOUD]
