"""
Terraform Part 1 - HCL Basics & Core Concepts
Premium V3 Content with Full Pedagogical Structure
"""

TASKS_PART1 = [
    {
        "title": "HCL Syntax & Configuration Basics",
        "slug": "hcl-syntax-basics",
        "description": "Master HashiCorp Configuration Language fundamentals",
        "difficulty": "beginner",
        "xp_reward": 150,
        "estimated_minutes": 45,
        "content": """# HCL Syntax & Configuration Basics

## Varför HCL är Kritiskt att Behärska

> **"Infrastructure as Code börjar med att kunna SKRIVA den koden."**

HCL (HashiCorp Configuration Language) är inte bara ännu ett konfigurationsformat – det är grunden för hela Terraform-ekosystemet och nyckeln till att hantera infrastruktur på ett modernt sätt.

```
+-----------------------------------------------------------------------------+
|                    INFRASTRUKTUR-EVOLUTION                                   |
+-----------------------------------------------------------------------------+
|                                                                              |
|   Manuellt              Skript                  Infrastructure as Code       |
|   +-----+              +-----+                 +---------------------+       |
|   |Click|    ->         |Bash |      ->          |   HCL / Terraform    |       |
|   |Click|              |AWS  |                 |   Declarative        |       |
|   |Click|              |CLI  |                 |   Version Control    |       |
|   +-----+              +-----+                 |   State Management   |       |
|                                                 +---------------------+       |
|   ❌ Repetitivt        ⚠️ Imperative           ✅ Deklarativt               |
|   ❌ Error-prone       ⚠️ Hard to maintain     ✅ Reproducerbart            |
|   ❌ No history        ⚠️ No state tracking    ✅ State-aware               |
|                                                                              |
+-----------------------------------------------------------------------------+
```

### Vad du kommer lära dig

Efter denna uppgift kommer du kunna:
- ✅ Skriva syntaktiskt korrekt HCL från scratch
- ✅ Förstå alla datatyper och strukturer
- ✅ Använda interpolation och expressions
- ✅ Organisera Terraform-filer professionellt

---

## Understanding HCL

HashiCorp Configuration Language (HCL) is designed to be both human-readable and machine-friendly.

## Basic Structure

```hcl
# Block type with labels
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name        = "WebServer"
    Environment = "Production"
  }
}
```

## Data Types

```hcl
# Strings
name = "my-resource"

# Numbers
count = 3
price = 10.50

# Booleans
enabled = true

# Lists
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Maps
tags = {
  Name = "MyResource"
  Env  = "prod"
}

# Objects
server_config = {
  cpu    = 4
  memory = 8192
  disk   = 100
}
```

## String Interpolation

```hcl
# Variable interpolation
resource "aws_instance" "example" {
  tags = {
    Name = "${var.project_name}-${var.environment}-server"
  }
}

# Heredoc for multi-line strings
user_data = <<-EOF
  #!/bin/bash
  echo "Hello, World!"
  apt-get update
  apt-get install -y nginx
EOF
```

## Comments

```hcl
# Single-line comment

// Also single-line comment

/*
  Multi-line
  comment block
*/
```

## Expressions

```hcl
# Conditional expression
instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

# For expressions
upper_names = [for name in var.names : upper(name)]

# Splat expressions
instance_ids = aws_instance.web[*].id
```

## Practical Exercise

Create a configuration file:

```hcl
# main.tf
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

locals {
  common_tags = {
    Project     = "TerraformLearning"
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Providers & Resource Configuration",
        "slug": "providers-resources",
        "description": "Configure providers and define infrastructure resources",
        "difficulty": "beginner",
        "xp_reward": 175,
        "estimated_minutes": 50,
        "content": """# Providers & Resource Configuration

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    TERRAFORM WORKFLOW                                |
+---------------------------------------------------------------------+
|   +--------+     +--------+     +--------+     +--------+          |
|   |  Write |----▶|  Plan  |----▶| Review |----▶| Apply  |          |
|   |   HCL  |     |        |     |        |     |        |          |
|   +--------+     +--------+     +--------+     +--------+          |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Provider Basics

```hcl
terraform {
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

# AWS Provider
provider "aws" {
  region = "us-east-1"

  default_tags {
    tags = {
      ManagedBy = "Terraform"
    }
  }
}

# Multiple provider configurations
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}
```

## Resource Syntax

```hcl
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  # Configuration arguments
  argument1 = value1
  argument2 = value2

  # Nested blocks
  nested_block {
    nested_argument = value
  }
}
```

## AWS Resources Example

```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "main-vpc"
  }
}

# Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

# Security Group
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }

  tags = {
    Name = "web-server"
  }
}
```

## Resource References

```hcl
# Reference another resource
resource "aws_eip" "web" {
  instance = aws_instance.web.id
  domain   = "vpc"
}

# Reference attributes
output "public_ip" {
  value = aws_instance.web.public_ip
}
```

## Meta-Arguments

```hcl
# count
resource "aws_instance" "server" {
  count         = 3
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "server-${count.index}"
  }
}

# for_each
resource "aws_instance" "servers" {
  for_each = {
    web = "t3.micro"
    api = "t3.small"
    db  = "t3.medium"
  }

  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}

# depends_on
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  depends_on = [aws_db_instance.main]
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    },
    {
        "title": "Variables & Outputs",
        "slug": "variables-outputs",
        "description": "Define inputs, outputs, and local values",
        "difficulty": "beginner",
        "xp_reward": 150,
        "estimated_minutes": 40,
        "content": """# Variables & Outputs

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    TERRAFORM WORKFLOW                                |
+---------------------------------------------------------------------+
|   +--------+     +--------+     +--------+     +--------+          |
|   |  Write |----▶|  Plan  |----▶| Review |----▶| Apply  |          |
|   |   HCL  |     |        |     |        |     |        |          |
|   +--------+     +--------+     +--------+     +--------+          |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Input Variables

```hcl
# variables.tf

# Simple variable
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

# Variable with validation
variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Must be dev, staging, or prod."
  }
}

# Complex types
variable "instance_config" {
  description = "EC2 instance configuration"
  type = object({
    instance_type = string
    ami_id        = string
    volume_size   = number
    tags          = map(string)
  })

  default = {
    instance_type = "t3.micro"
    ami_id        = "ami-0c55b159cbfafe1f0"
    volume_size   = 20
    tags          = {}
  }
}

# List variable
variable "availability_zones" {
  description = "List of AZs"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

# Sensitive variable
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
```

## Setting Variable Values

```hcl
# terraform.tfvars
region      = "us-west-2"
environment = "prod"

instance_config = {
  instance_type = "t3.large"
  ami_id        = "ami-0123456789"
  volume_size   = 50
  tags = {
    Team = "Platform"
  }
}
```

```bash
# Command line
terraform apply -var="environment=prod"

# Environment variables
export TF_VAR_region="us-west-2"
export TF_VAR_db_password="secret123"

# Variable file
terraform apply -var-file="prod.tfvars"
```

## Local Values

```hcl
locals {
  # Simple local
  project_name = "myapp"

  # Computed local
  name_prefix = "${var.project}-${var.environment}"

  # Common tags
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = var.team
  }

  # Conditional local
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

  # Complex computed value
  subnet_cidrs = {
    for idx, az in var.availability_zones :
    az => cidrsubnet(var.vpc_cidr, 8, idx)
  }
}

# Using locals
resource "aws_instance" "web" {
  instance_type = local.instance_type

  tags = merge(local.common_tags, {
    Name = "${local.name_prefix}-web"
  })
}
```

## Output Values

```hcl
# outputs.tf

# Simple output
output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
}

# Sensitive output
output "db_connection_string" {
  description = "Database connection string"
  value       = "postgresql://${aws_db_instance.main.endpoint}/${var.db_name}"
  sensitive   = true
}

# Complex output
output "instance_details" {
  description = "Instance details"
  value = {
    id         = aws_instance.web.id
    public_ip  = aws_instance.web.public_ip
    private_ip = aws_instance.web.private_ip
    az         = aws_instance.web.availability_zone
  }
}

# List output
output "subnet_ids" {
  description = "All subnet IDs"
  value       = aws_subnet.private[*].id
}

# Map output
output "instances" {
  description = "Map of instance names to IPs"
  value = {
    for k, v in aws_instance.servers :
    k => v.public_ip
  }
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Data Sources & Lookups",
        "slug": "data-sources-lookups",
        "description": "Query existing resources and external data",
        "difficulty": "intermediate",
        "xp_reward": 175,
        "estimated_minutes": 45,
        "content": """# Data Sources & Lookups

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    TERRAFORM WORKFLOW                                |
+---------------------------------------------------------------------+
|   +--------+     +--------+     +--------+     +--------+          |
|   |  Write |----▶|  Plan  |----▶| Review |----▶| Apply  |          |
|   |   HCL  |     |        |     |        |     |        |          |
|   +--------+     +--------+     +--------+     +--------+          |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Data Source Basics

```hcl
# Query existing AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Use the data source
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

## Common AWS Data Sources

```hcl
# Current AWS account
data "aws_caller_identity" "current" {}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}

# Current region
data "aws_region" "current" {}

# Availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Existing VPC
data "aws_vpc" "existing" {
  tags = {
    Name = "production-vpc"
  }
}

# Existing subnets
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.existing.id]
  }

  tags = {
    Tier = "private"
  }
}

# IAM policy document
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "ec2" {
  name               = "ec2-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
```

## External Data Sources

```hcl
# HTTP data source
data "http" "myip" {
  url = "https://ipv4.icanhazip.com"
}

resource "aws_security_group_rule" "ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["${chomp(data.http.myip.response_body)}/32"]
  security_group_id = aws_security_group.main.id
}

# External program
data "external" "git_info" {
  program = ["bash", "-c", <<-EOF
    echo '{"commit": "'$(git rev-parse HEAD)'", "branch": "'$(git branch --show-current)'"}'
  EOF
  ]
}

locals {
  git_commit = data.external.git_info.result.commit
}

# Template file
data "template_file" "user_data" {
  template = file("${path.module}/templates/user_data.sh.tpl")

  vars = {
    environment = var.environment
    app_name    = var.app_name
  }
}
```

## Remote State Data

```hcl
# Reference another Terraform state
data "terraform_remote_state" "vpc" {
  backend = "s3"

  config = {
    bucket = "my-terraform-state"
    key    = "vpc/terraform.tfstate"
    region = "us-east-1"
  }
}

# Use outputs from remote state
resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.vpc.outputs.private_subnet_ids[0]

  vpc_security_group_ids = [
    data.terraform_remote_state.vpc.outputs.app_security_group_id
  ]
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "State Management Fundamentals",
        "slug": "state-management",
        "description": "Understand and manage Terraform state",
        "difficulty": "intermediate",
        "xp_reward": 200,
        "estimated_minutes": 55,
        "content": """# State Management Fundamentals

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    TERRAFORM WORKFLOW                                |
+---------------------------------------------------------------------+
|   +--------+     +--------+     +--------+     +--------+          |
|   |  Write |----▶|  Plan  |----▶| Review |----▶| Apply  |          |
|   |   HCL  |     |        |     |        |     |        |          |
|   +--------+     +--------+     +--------+     +--------+          |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Understanding State

Terraform state maps your configuration to real-world resources.

```bash
# State file structure (simplified)
{
  "version": 4,
  "terraform_version": "1.6.0",
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "instances": [
        {
          "attributes": {
            "id": "i-1234567890abcdef0",
            "ami": "ami-0c55b159cbfafe1f0",
            "instance_type": "t3.micro"
          }
        }
      ]
    }
  ]
}
```

## Remote State Backends

```hcl
# S3 Backend (AWS)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

# Azure Blob Storage
terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "tfstate"
    container_name       = "state"
    key                  = "prod.terraform.tfstate"
  }
}

# GCS Backend
terraform {
  backend "gcs" {
    bucket = "my-terraform-state"
    prefix = "prod/infrastructure"
  }
}

# Terraform Cloud
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      name = "my-workspace"
    }
  }
}
```

## State Commands

```bash
# List resources in state
terraform state list

# Show specific resource
terraform state show aws_instance.web

# Move resource in state
terraform state mv aws_instance.old aws_instance.new

# Remove from state (doesn't destroy)
terraform state rm aws_instance.web

# Pull remote state locally
terraform state pull > state.json

# Push local state to remote
terraform state push state.json

# Replace provider in state
terraform state replace-provider \\
  hashicorp/aws \\
  registry.terraform.io/hashicorp/aws
```

## State Locking

```hcl
# DynamoDB table for state locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
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
```

```bash
# Force unlock (use carefully!)
terraform force-unlock LOCK_ID
```

## Import Existing Resources

```bash
# Import command
terraform import aws_instance.web i-1234567890abcdef0

# Import into module
terraform import module.vpc.aws_vpc.main vpc-12345678
```

```hcl
# Import block (Terraform 1.5+)
import {
  to = aws_instance.web
  id = "i-1234567890abcdef0"
}

# Generate configuration
terraform plan -generate-config-out=generated.tf
```

## Workspaces

```bash
# Create workspace
terraform workspace new production

# List workspaces
terraform workspace list

# Select workspace
terraform workspace select production

# Show current workspace
terraform workspace show
```

```hcl
# Use workspace in configuration
resource "aws_instance" "web" {
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Environment = terraform.workspace
  }
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    }
]
