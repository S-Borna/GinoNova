# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 2: STATE & MODULES (Part 1)
# =============================================================================
# Nodes 5-6: State Management, Remote State
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_5 = {
    "id": "terraform_node_5",
    "slug": "terraform-state-management",
    "title": "Terraform State Management - The Source of Truth",
    "description": "Master Terraform state file management and best practices",
    "node_id": 5,
    "content": '''
# Terraform State Management - The Source of Truth

## Vad är Terraform State?

State är hjärtat i Terraform. Det är en JSON-fil som mappar dina konfigurationer till verkliga resurser i cloud providers.

```
+-------------------------------------------------------------------------+
|                    TERRAFORM STATE OVERVIEW                             |
+-------------------------------------------------------------------------+
|                                                                         |
|  +------------------+                                                  |
|  |  Configuration   |     .tf files                                    |
|  |    (Desired)     |     "I want 3 EC2 instances"                     |
|  +--------+---------+                                                  |
|           |                                                             |
|           ▼                                                             |
|  +------------------+                                                  |
|  |  Terraform State |     .tfstate file                                |
|  |    (Mapping)     |     "These are the 3 instances I manage"         |
|  |                  |     - ID: i-abc123 -> aws_instance.web[0]         |
|  |                  |     - ID: i-def456 -> aws_instance.web[1]         |
|  |                  |     - ID: i-ghi789 -> aws_instance.web[2]         |
|  +--------+---------+                                                  |
|           |                                                             |
|           ▼                                                             |
|  +------------------+                                                  |
|  |  Real Resources  |     AWS/Azure/GCP                                |
|  |    (Actual)      |     "The actual infrastructure"                  |
|  +------------------+                                                  |
|                                                                         |
|  STATE PURPOSES:                                                        |
|  ---------------                                                        |
|  1. Mapping: Config address -> Resource ID                              |
|  2. Metadata: Dependencies, outputs, provider config                   |
|  3. Performance: Cache for plan operations                             |
|  4. Syncing: Team collaboration                                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## State File Anatomy

```json
{
  "version": 4,
  "terraform_version": "1.6.4",
  "serial": 42,
  "lineage": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "outputs": {
    "instance_ip": {
      "value": "54.123.45.67",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\\"registry.terraform.io/hashicorp/aws\\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "id": "i-0abc123def456789",
            "ami": "ami-0c55b159cbfafe1f0",
            "instance_type": "t3.micro",
            "private_ip": "10.0.1.100",
            "public_ip": "54.123.45.67",
            "tags": {
              "Name": "web-server"
            }
          },
          "sensitive_attributes": [],
          "private": "base64encodeddata..."
        }
      ]
    }
  ]
}
```

```
+-------------------------------------------------------------------------+
|                    STATE FILE COMPONENTS                                |
+-------------------------------------------------------------------------+
|                                                                         |
|  version          Schema version för state format                      |
|  terraform_version Terraform version som skapade staten               |
|  serial           Inkrementellt nummer, ökar vid varje ändring        |
|  lineage          Unikt ID för state history                          |
|  outputs          Alla output values                                   |
|  resources        Lista av managed resources                           |
|    +- mode        managed (resource) eller data (data source)         |
|    +- type        Resource type (aws_instance)                        |
|    +- name        Local name (web)                                    |
|    +- provider    Full provider address                               |
|    +- instances   List of resource instances                          |
|        +- attributes  All resource attributes                         |
|        +- sensitive_attributes  Sensitive data markers               |
|        +- private     Provider-specific data                          |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## State Commands

### Inspecting State

```bash
# Lista alla resurser i state
terraform state list
# aws_instance.web
# aws_security_group.web
# aws_vpc.main

# Visa detaljer för specifik resurs
terraform state show aws_instance.web
# resource "aws_instance" "web" {
#     ami                         = "ami-0c55b159cbfafe1f0"
#     instance_type               = "t3.micro"
#     ...
# }

# Visa full state (JSON)
terraform show -json | jq .

# Pull remote state lokalt
terraform state pull > local.tfstate
```

### Modifying State

```bash
# Flytta resurs till ny adress
terraform state mv aws_instance.web aws_instance.web_server
# Moved aws_instance.web to aws_instance.web_server

# Flytta till modul
terraform state mv aws_instance.web module.compute.aws_instance.web

# Ta bort från state (resurs finns kvar i cloud!)
terraform state rm aws_instance.web
# Removed aws_instance.web

# Importera befintlig resurs
terraform import aws_instance.web i-0abc123def456789
# aws_instance.web: Importing...
# aws_instance.web: Import complete!

# Markera för recreation
terraform taint aws_instance.web  # Deprecated
terraform apply -replace="aws_instance.web"  # Modern
```

### State Operations Workflow

```
+-------------------------------------------------------------------------+
|                    STATE MODIFICATION WORKFLOW                          |
+-------------------------------------------------------------------------+
|                                                                         |
|  SCENARIO: Rename resource without destroying                          |
|                                                                         |
|  1. BEFORE                                                             |
|     +-----------------------------------------+                       |
|     | resource "aws_instance" "old_name" {...}|                       |
|     +-----------------------------------------+                       |
|                                                                         |
|  2. STATE MOVE                                                         |
|     $ terraform state mv aws_instance.old_name aws_instance.new_name  |
|                                                                         |
|  3. UPDATE CONFIG                                                      |
|     +-----------------------------------------+                       |
|     | resource "aws_instance" "new_name" {...}|                       |
|     +-----------------------------------------+                       |
|                                                                         |
|  4. VERIFY                                                             |
|     $ terraform plan                                                   |
|     # No changes. Your infrastructure matches the configuration.      |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Local State

```hcl
# Default: Local state (terraform.tfstate)
# Skapas automatiskt i working directory

# Projektstruktur
my-terraform-project/
+-- main.tf
+-- variables.tf
+-- outputs.tf
+-- terraform.tfstate         # State file (KÄNSLIGT!)
+-- terraform.tfstate.backup  # Backup av föregående state
```

### Local State Risks

```
+-------------------------------------------------------------------------+
|                    LOCAL STATE PROBLEMS                                 |
+-------------------------------------------------------------------------+
|                                                                         |
|  ⚠️  RISK 1: Team Collaboration                                        |
|      ------------------------                                          |
|      Developer A: terraform apply (modifies state)                     |
|      Developer B: terraform apply (overwrites A's changes!)            |
|      -> State conflict, potential resource destruction                  |
|                                                                         |
|  ⚠️  RISK 2: Single Point of Failure                                   |
|      -----------------------------                                      |
|      - State file på laptop -> Laptop kraschar -> State borta            |
|      - Ingen backup -> Terraform vet inte om befintliga resurser        |
|      - Manual recovery krävs                                           |
|                                                                         |
|  ⚠️  RISK 3: Security                                                  |
|      ----------------                                                   |
|      - State innehåller secrets (databas-lösenord, API-nycklar)        |
|      - Plain text JSON                                                 |
|      - Risk att committa till Git                                      |
|                                                                         |
|  ⚠️  RISK 4: Locking                                                   |
|      ----------------                                                   |
|      - Ingen locking för local state                                   |
|      - Concurrent applies kan korruptera state                         |
|                                                                         |
+-------------------------------------------------------------------------+
```

### .gitignore for Terraform

```gitignore
# .gitignore

# Local .terraform directories
**/.terraform/*

# State files
*.tfstate
*.tfstate.*
*.tfstate.backup

# Crash log files
crash.log
crash.*.log

# Exclude override files
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Exclude CLI configuration files
.terraformrc
terraform.rc

# Sensitive variable files
*.tfvars
!example.tfvars

# Lock file (include i Git för reproducibility)
# .terraform.lock.hcl  # KEEP THIS IN GIT
```

---

## State Locking

```
+-------------------------------------------------------------------------+
|                    STATE LOCKING MECHANISM                              |
+-------------------------------------------------------------------------+
|                                                                         |
|  WITHOUT LOCKING                          WITH LOCKING                 |
|  ---------------                          ------------                 |
|                                                                         |
|  User A                User B             User A                User B |
|    |                     |                  |                     |    |
|    +- Read state         |                  +- Acquire lock       |    |
|    |                     |                  |  ✓ Lock acquired    |    |
|    |                     +- Read state      |                     |    |
|    |                     |                  |                     +- Try lock |
|    +- Modify state       |                  |                     |  ✗ Locked! |
|    |                     |                  +- Modify state       |    |
|    |                     +- Modify state    |                     | (wait...) |
|    |                     |                  +- Release lock       |    |
|    ▼                     ▼                  |                     |    |
|  +-------------------------+              |                     +- Acquire |
|  |    CORRUPTED STATE!    |              |                     |  ✓ OK    |
|  |    Data loss possible   |              ▼                     ▼    |
|  +-------------------------+              +-------------------------+ |
|                                           |    SAFE STATE          | |
|                                           |    Consistent data      | |
|                                           +-------------------------+ |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Force Unlock

```bash
# Om en process kraschade med aktivt lås
terraform force-unlock LOCK_ID

# Exempel
# Error: Error acquiring the state lock
# Lock Info:
#   ID:        a1b2c3d4-5678-90ab-cdef-1234567890ab
#   Path:      terraform-state/prod/terraform.tfstate
#   Operation: OperationTypeApply

terraform force-unlock a1b2c3d4-5678-90ab-cdef-1234567890ab
```

---

## State Workspaces

Workspaces låter dig ha flera state files för samma konfiguration.

```bash
# Lista workspaces
terraform workspace list
# * default
#   dev
#   staging
#   prod

# Skapa workspace
terraform workspace new dev
# Created and switched to workspace "dev"!

# Byt workspace
terraform workspace select prod
# Switched to workspace "prod"

# Visa current workspace
terraform workspace show
# prod

# Ta bort workspace
terraform workspace delete dev
# Deleted workspace "dev"!
```

### Workspace i Kod

```hcl
# Använd workspace i konfiguration
resource "aws_instance" "web" {
  count         = terraform.workspace == "prod" ? 3 : 1
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Name        = "web-${terraform.workspace}"
    Environment = terraform.workspace
  }
}

# Conditional backend key
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "env/${terraform.workspace}/terraform.tfstate"
    region = "eu-north-1"
  }
}

# Workspace-specific variables
locals {
  environment_config = {
    dev = {
      instance_count = 1
      instance_type  = "t3.micro"
    }
    staging = {
      instance_count = 2
      instance_type  = "t3.small"
    }
    prod = {
      instance_count = 3
      instance_type  = "t3.large"
    }
  }

  config = local.environment_config[terraform.workspace]
}

resource "aws_instance" "web" {
  count         = local.config.instance_count
  instance_type = local.config.instance_type
}
```

---

## Import Existing Resources

```
+-------------------------------------------------------------------------+
|                    TERRAFORM IMPORT WORKFLOW                            |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. EXISTING RESOURCE (created manually)                               |
|     +---------------------------------------------+                   |
|     |  AWS Console: EC2 Instance i-0abc123       |                   |
|     |  (Exists but not in Terraform state)        |                   |
|     +---------------------------------------------+                   |
|                                                                         |
|  2. CREATE PLACEHOLDER CONFIG                                          |
|     ```hcl                                                             |
|     resource "aws_instance" "imported" {                               |
|       # Will be populated after import                                 |
|     }                                                                  |
|     ```                                                                |
|                                                                         |
|  3. RUN IMPORT                                                         |
|     $ terraform import aws_instance.imported i-0abc123                |
|                                                                         |
|  4. GENERATE CONFIG                                                    |
|     $ terraform show -no-color > imported.tf                          |
|     # Or use `terraform plan` to see required attributes              |
|                                                                         |
|  5. COMPLETE CONFIG                                                    |
|     ```hcl                                                             |
|     resource "aws_instance" "imported" {                               |
|       ami           = "ami-0c55b159cbfafe1f0"                         |
|       instance_type = "t3.micro"                                       |
|       # ... all required attributes                                    |
|     }                                                                  |
|     ```                                                                |
|                                                                         |
|  6. VERIFY                                                             |
|     $ terraform plan                                                   |
|     # No changes required.                                             |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Import Block (Terraform 1.5+)

```hcl
# Modern import syntax
import {
  to = aws_instance.web
  id = "i-0abc123def456789"
}

# Generera konfiguration
# terraform plan -generate-config-out=generated.tf

# Import med for_each
import {
  for_each = var.existing_instances
  to       = aws_instance.imported[each.key]
  id       = each.value
}
```

---

## Praktiska Övningar

### Övning 1: State Inspection
```bash
# 1. Skapa enkel infrastruktur
# 2. Inspektera state
terraform state list
terraform state show aws_instance.web

# 3. Exportera state
terraform show -json > state.json
cat state.json | jq '.values.root_module.resources'
```

### Övning 2: State Migration
```bash
# Scenario: Refactoring - flytta till modul

# 1. Backup state
cp terraform.tfstate terraform.tfstate.backup

# 2. Flytta resources till modul
terraform state mv aws_instance.web module.compute.aws_instance.web
terraform state mv aws_security_group.web module.compute.aws_security_group.web

# 3. Uppdatera konfiguration
# 4. Verify
terraform plan
```

### Övning 3: Import Workflow
```bash
# 1. Identifiera resurs-ID i AWS Console
# 2. Skapa placeholder config
# 3. Import
terraform import aws_s3_bucket.existing my-existing-bucket

# 4. Generate full config
terraform show -no-color aws_s3_bucket.existing

# 5. Verify no changes
terraform plan
```

---

**Nästa Node:** Remote State & Backends ->
''',
    "xp_reward": 180,
    "estimated_minutes": 70,
    "prerequisites": ["terraform_node_4"],
    "learning_outcomes": [
        "Förstå state-filens struktur och syfte",
        "Behärska state commands",
        "Hantera state locking",
        "Använda workspaces effektivt",
        "Importera befintliga resurser"
    ]
}

NODE_6 = {
    "id": "terraform_node_6",
    "slug": "remote-state-backends",
    "title": "Remote State & Backends - Team Collaboration",
    "description": "Configure remote state backends for team collaboration and security",
    "node_id": 6,
    "content": '''
# Remote State & Backends - Team Collaboration

## Varför Remote State?

```
+-------------------------------------------------------------------------+
|                    REMOTE STATE BENEFITS                                |
+-------------------------------------------------------------------------+
|                                                                         |
|  LOCAL STATE                           REMOTE STATE                    |
|  -----------                           ------------                    |
|                                                                         |
|  ❌ Single developer only              ✅ Team collaboration           |
|  ❌ No locking                         ✅ State locking                 |
|  ❌ On local machine                   ✅ Centralized storage          |
|  ❌ Easy to lose                       ✅ Durable & backed up          |
|  ❌ Plain text secrets                 ✅ Encryption at rest           |
|  ❌ No audit trail                     ✅ Versioning & history         |
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |                     REMOTE STATE ARCHITECTURE                    |   |
|  |                                                                   |   |
|  |   Developer A     Developer B      CI/CD Pipeline                |   |
|  |       |               |                 |                        |   |
|  |       +---------------+-----------------+                        |   |
|  |                       |                                          |   |
|  |                       ▼                                          |   |
|  |              +----------------+                                  |   |
|  |              |  State Lock    |  (DynamoDB/Consul/etc)          |   |
|  |              +-------+--------+                                  |   |
|  |                      |                                           |   |
|  |                      ▼                                           |   |
|  |              +----------------+                                  |   |
|  |              |  Remote State  |  (S3/GCS/Azure Blob/etc)        |   |
|  |              |   (encrypted)  |                                  |   |
|  |              +----------------+                                  |   |
|  |                                                                   |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## AWS S3 Backend (Most Common)

### Backend Infrastructure

```hcl
# bootstrap/main.tf - Skapa backend-resurser först

# S3 Bucket för state
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-company-terraform-state"

  lifecycle {
    prevent_destroy = true
  }
}

# Versioning
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Encryption
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

# Block public access
resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# DynamoDB för locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-state-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name = "Terraform State Lock Table"
  }
}

# KMS Key för encryption
resource "aws_kms_key" "terraform_state" {
  description             = "KMS key for Terraform state encryption"
  deletion_window_in_days = 30
  enable_key_rotation     = true
}

resource "aws_kms_alias" "terraform_state" {
  name          = "alias/terraform-state"
  target_key_id = aws_kms_key.terraform_state.key_id
}
```

### Backend Configuration

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-company-terraform-state"
    key            = "production/networking/terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
    kms_key_id     = "alias/terraform-state"
    dynamodb_table = "terraform-state-locks"

    # Optional: Assume role
    role_arn       = "arn:aws:iam::123456789012:role/TerraformStateRole"

    # Optional: Workspace prefix
    workspace_key_prefix = "workspaces"
  }
}
```

### State Path Structure

```
+-------------------------------------------------------------------------+
|                    S3 STATE ORGANIZATION                                |
+-------------------------------------------------------------------------+
|                                                                         |
|  my-company-terraform-state/                                           |
|  |                                                                      |
|  +-- production/                                                       |
|  |   +-- networking/                                                   |
|  |   |   +-- terraform.tfstate      VPC, Subnets, etc.               |
|  |   +-- eks/                                                          |
|  |   |   +-- terraform.tfstate      EKS Cluster                       |
|  |   +-- rds/                                                          |
|  |   |   +-- terraform.tfstate      Databases                         |
|  |   +-- applications/                                                 |
|  |       +-- terraform.tfstate      Application resources             |
|  |                                                                      |
|  +-- staging/                                                          |
|  |   +-- networking/                                                   |
|  |   |   +-- terraform.tfstate                                        |
|  |   +-- applications/                                                 |
|  |       +-- terraform.tfstate                                        |
|  |                                                                      |
|  +-- shared/                                                           |
|      +-- iam/                                                          |
|      |   +-- terraform.tfstate      IAM Roles, Policies               |
|      +-- dns/                                                          |
|          +-- terraform.tfstate      Route53 Zones                     |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Azure Blob Backend

```hcl
# Bootstrap: Create storage account
resource "azurerm_resource_group" "tfstate" {
  name     = "tfstate-rg"
  location = "North Europe"
}

resource "azurerm_storage_account" "tfstate" {
  name                     = "mycompanytfstate"
  resource_group_name      = azurerm_resource_group.tfstate.name
  location                 = azurerm_resource_group.tfstate.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  blob_properties {
    versioning_enabled = true
  }

  network_rules {
    default_action = "Deny"
    ip_rules       = var.allowed_ips
  }
}

resource "azurerm_storage_container" "tfstate" {
  name                  = "tfstate"
  storage_account_name  = azurerm_storage_account.tfstate.name
  container_access_type = "private"
}

# Backend configuration
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "mycompanytfstate"
    container_name       = "tfstate"
    key                  = "production/terraform.tfstate"

    # Use Azure AD auth (recommended)
    use_azuread_auth     = true
  }
}
```

---

## Google Cloud Storage Backend

```hcl
# Bootstrap: Create bucket
resource "google_storage_bucket" "tfstate" {
  name     = "mycompany-terraform-state"
  location = "EU"

  versioning {
    enabled = true
  }

  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      num_newer_versions = 5
    }
    action {
      type = "Delete"
    }
  }
}

# Backend configuration
terraform {
  backend "gcs" {
    bucket = "mycompany-terraform-state"
    prefix = "production/networking"
  }
}
```

---

## Terraform Cloud Backend

```hcl
# Terraform Cloud configuration
terraform {
  cloud {
    organization = "my-organization"

    workspaces {
      name = "production-networking"
      # Or use prefix for multiple workspaces
      # tags = ["networking", "production"]
    }
  }
}

# Alternative: Remote backend (legacy)
terraform {
  backend "remote" {
    organization = "my-organization"

    workspaces {
      name = "production-networking"
    }
  }
}
```

```
+-------------------------------------------------------------------------+
|                    TERRAFORM CLOUD FEATURES                             |
+-------------------------------------------------------------------------+
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |  FREE TIER                                                       |   |
|  |  • Remote state management                                       |   |
|  |  • State locking                                                 |   |
|  |  • Remote operations                                             |   |
|  |  • Up to 5 users                                                 |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |  TEAM TIER                                                       |   |
|  |  • Team management                                               |   |
|  |  • SSO                                                           |   |
|  |  • Sentinel policies                                             |   |
|  |  • Run triggers                                                  |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |  BUSINESS TIER                                                   |   |
|  |  • Self-hosted agents                                            |   |
|  |  • Audit logging                                                 |   |
|  |  • Custom concurrency                                            |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Remote State Data Source

Läs state från andra Terraform-konfigurationer:

```hcl
# networking project outputs VPC info
# Production networking state

# Application project reads VPC info
data "terraform_remote_state" "networking" {
  backend = "s3"

  config = {
    bucket = "my-company-terraform-state"
    key    = "production/networking/terraform.tfstate"
    region = "eu-north-1"
  }
}

# Use networking outputs
resource "aws_instance" "app" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  subnet_id              = data.terraform_remote_state.networking.outputs.private_subnet_ids[0]
  vpc_security_group_ids = [data.terraform_remote_state.networking.outputs.app_security_group_id]
}

# networking/outputs.tf - Must expose these outputs
output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "app_security_group_id" {
  value = aws_security_group.app.id
}
```

### Cross-Account Remote State

```hcl
# Read state from different AWS account
data "terraform_remote_state" "shared_services" {
  backend = "s3"

  config = {
    bucket   = "shared-services-terraform-state"
    key      = "global/dns/terraform.tfstate"
    region   = "eu-north-1"
    role_arn = "arn:aws:iam::111111111111:role/TerraformReadState"
  }
}
```

---

## Backend Migration

```bash
# Migrera från local till S3

# 1. Lägg till backend config
# backend.tf
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "project/terraform.tfstate"
    region = "eu-north-1"
  }
}

# 2. Reinitialize
terraform init -migrate-state

# Terraform will detect the new backend configuration and ask:
# Do you want to copy existing state to the new backend? yes

# 3. Verify
terraform state list
```

### Migrera mellan backends

```bash
# Migrera från S3 till Terraform Cloud

# 1. Pull current state
terraform state pull > terraform.tfstate.backup

# 2. Uppdatera backend config till TFC
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "my-workspace"
    }
  }
}

# 3. Initialize and migrate
terraform init -migrate-state

# 4. Push state om nödvändigt
terraform state push terraform.tfstate.backup
```

---

## Backend Best Practices

```
+-------------------------------------------------------------------------+
|                    BACKEND BEST PRACTICES                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. ALWAYS USE REMOTE STATE IN TEAMS                                   |
|     • Minimum: S3 + DynamoDB                                           |
|     • Preferred: Terraform Cloud                                       |
|                                                                         |
|  2. ENABLE VERSIONING                                                  |
|     • S3 bucket versioning                                             |
|     • Möjliggör rollback                                               |
|                                                                         |
|  3. ENCRYPT STATE                                                      |
|     • KMS encryption för S3                                            |
|     • State innehåller secrets                                         |
|                                                                         |
|  4. RESTRICT ACCESS                                                    |
|     • IAM policies                                                     |
|     • Bucket policies                                                  |
|     • Network restrictions                                             |
|                                                                         |
|  5. USE SEPARATE STATE FILES                                           |
|     • Per environment (dev/staging/prod)                               |
|     • Per component (networking/compute/storage)                       |
|     • Minimera blast radius                                            |
|                                                                         |
|  6. BACKUP REGULARLY                                                   |
|     • Cross-region replication                                         |
|     • Lifecycle policies                                               |
|                                                                         |
|  7. AUDIT ACCESS                                                       |
|     • CloudTrail för S3                                                |
|     • Audit logs för TFC                                               |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Praktiska Övningar

### Övning 1: Setup S3 Backend
```bash
# 1. Skapa S3 bucket och DynamoDB table (bootstrap)
# 2. Configure backend
# 3. Migrate state
# 4. Verify locking works
```

### Övning 2: Cross-Stack Communication
```hcl
# Stack 1: Networking
# - Output VPC ID, subnet IDs
# Stack 2: Application
# - Use remote state data source
# - Deploy into networking
```

### Övning 3: Multi-Environment Setup
```bash
# 1. Create workspace per environment
# 2. Configure workspace-specific state paths
# 3. Deploy same config to multiple environments
```

---

**Nästa Node:** Modules - Reusable Infrastructure ->
''',
    "xp_reward": 180,
    "estimated_minutes": 70,
    "prerequisites": ["terraform_node_5"],
    "learning_outcomes": [
        "Konfigurera S3/GCS/Azure backends",
        "Implementera state locking",
        "Använda remote state data sources",
        "Migrera mellan backends",
        "Tillämpa backend best practices"
    ]
}

# Block 2 Part 1 exports
BLOCK_2_PART_1_NODES = [NODE_5, NODE_6]

__all__ = ["NODE_5", "NODE_6", "BLOCK_2_PART_1_NODES"]
