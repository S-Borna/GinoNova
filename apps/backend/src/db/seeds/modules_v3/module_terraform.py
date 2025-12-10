"""
Terraform Mastery - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: cloud-infrastructure
Tasks: 40
Estimated Hours: 25
"""

MODULE_TERRAFORM_MASTERY = {
    "track_slug": "cloud-infrastructure",
    "order_index": 100,
    "name": "Terraform Mastery",
    "slug": "terraform-mastery",
    "description": """Behärska Infrastructure as Code med Terraform""",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ['linux-fundamentals'],
    "tasks": [
            {
                "title": "Terraform Introduktion",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 100,
                "content": r"""
# Terraform Introduktion

Infrastructure as Code med HashiCorp Terraform.

## Varför Terraform?

| Funktion | Fördel |
|----------|--------|
| Deklarativ | Beskriv önskat tillstånd |
| Multi-cloud | AWS, Azure, GCP, etc |
| State | Spårar resurser |
| Plan | Förhandsgranska ändringar |
| Modular | Återanvändbar kod |

## Installation

```bash
# macOS
brew install terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Verifiera
terraform version
```

## Första Projektet

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}
```

## Grundläggande Workflow

```bash
terraform init      # Initiera, ladda providers
terraform plan      # Visa ändringar
terraform apply     # Applicera ändringar
terraform destroy   # Ta bort allt
```

**Nästa steg:** Node 2 - HCL Syntax

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "HCL Syntax",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 120,
                "content": r"""
# HCL Syntax

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


HashiCorp Configuration Language.

## Block Types

```hcl
# Resource block
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}

# Variable block
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

# Output block
output "instance_ip" {
  value = aws_instance.web.public_ip
}

# Locals block
locals {
  common_tags = {
    Environment = "production"
    Project     = "webapp"
  }
}
```

## Data Types

```hcl
# String
name = "myserver"

# Number
count = 3

# Bool
enabled = true

# List
subnets = ["10.0.1.0/24", "10.0.2.0/24"]

# Map
tags = {
  Name = "web"
  Env  = "prod"
}
```

## Referencing

```hcl
# Resurs-attribut
aws_instance.web.id
aws_instance.web.public_ip

# Variable
var.instance_type

# Local
local.common_tags

# Data source
data.aws_ami.ubuntu.id
```

| Koncept | Syntax |
|---------|--------|
| Resource | resource "type" "name" {} |
| Variable | var.name |
| Output | output "name" {} |
| Local | local.name |

**Nästa steg:** Node 3 - Variables & Outputs

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Variables & Outputs",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Variables & Outputs

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Parametrisera din Terraform-kod.

## Variable Declaration

```hcl
# variables.tf
variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 1
}

variable "enable_monitoring" {
  type    = bool
  default = true
}

variable "allowed_ports" {
  type    = list(number)
  default = [80, 443]
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "dev"
  }
}
```

## Variable Files

```hcl
# terraform.tfvars (auto-loaded)
region         = "eu-west-1"
instance_count = 3

# prod.tfvars
region         = "eu-west-1"
instance_count = 10
```

```bash
# Använd specifik fil
terraform apply -var-file="prod.tfvars"

# CLI variable
terraform apply -var="region=us-east-1"

# Environment variable
export TF_VAR_region="us-east-1"
```

## Outputs

```hcl
# outputs.tf
output "instance_ids" {
  description = "IDs of EC2 instances"
  value       = aws_instance.web[*].id
}

output "load_balancer_dns" {
  value     = aws_lb.main.dns_name
  sensitive = true
}
```

```bash
# Visa outputs
terraform output
terraform output instance_ids
```

**Nästa steg:** Node 4 - State Management

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "State Management",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# State Management

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Terraform state spårar infrastruktur.

## Lokal State

```bash
# Default: terraform.tfstate
ls -la terraform.tfstate
```

## Remote State (Rekommenderat)

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## State Commands

```bash
# Lista resurser i state
terraform state list

# Visa specifik resurs
terraform state show aws_instance.web

# Flytta resurs (rename)
terraform state mv aws_instance.web aws_instance.app

# Ta bort från state (inte infra)
terraform state rm aws_instance.old

# Importera befintlig resurs
terraform import aws_instance.web i-1234567890
```

## State Locking

```hcl
# DynamoDB för locking (AWS)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

| Backend | Locking |
|---------|---------|
| S3 + DynamoDB | Ja |
| Azure Blob | Ja |
| GCS | Ja |
| Terraform Cloud | Ja |

**Nästa steg:** Node 5 - Resources & Data Sources

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Resources & Data Sources",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# Resources & Data Sources

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Skapa och läs infrastruktur.

## Resources

```hcl
# Skapa resurs
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}
```

## Data Sources

```hcl
# Läs befintlig data
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

## Lifecycle

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [tags]
  }
}
```

## Provisioners (Undvik om möjligt)

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx"
    ]
  }
}
```

**Nästa steg:** Node 6 - Providers

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Providers",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Terraform Providers

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Providers kopplar till cloud APIs.

## Provider Configuration

```hcl
# AWS
provider "aws" {
  region  = "eu-north-1"
  profile = "production"
}

# Azure
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

# Google Cloud
provider "google" {
  project = "my-project"
  region  = "europe-north1"
}
```

## Multiple Providers

```hcl
provider "aws" {
  region = "eu-north-1"
  alias  = "stockholm"
}

provider "aws" {
  region = "us-east-1"
  alias  = "virginia"
}

resource "aws_instance" "eu" {
  provider = aws.stockholm
  # ...
}

resource "aws_instance" "us" {
  provider = aws.virginia
  # ...
}
```

## Version Constraints

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0, < 3.0"
    }
  }
}
```

| Constraint | Betydelse |
|------------|-----------|
| = 1.0.0 | Exakt version |
| >= 1.0 | Minst 1.0 |
| ~> 5.0 | >= 5.0, < 6.0 |
| >= 2.0, < 3.0 | Range |

**Nästa steg:** Node 7 - Count & For_each

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Count & For_each",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Count & For_each

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Skapa flera resurser.

## Count

```hcl
resource "aws_instance" "web" {
  count = 3

  ami           = "ami-12345"
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}

# Referera
aws_instance.web[0].id
aws_instance.web[*].id  # Alla
```

## Conditional Count

```hcl
variable "create_instance" {
  type    = bool
  default = true
}

resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
  # ...
}
```

## For_each med Map

```hcl
variable "instances" {
  default = {
    web    = "t3.micro"
    api    = "t3.small"
    worker = "t3.medium"
  }
}

resource "aws_instance" "servers" {
  for_each = var.instances

  ami           = "ami-12345"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}

# Referera
aws_instance.servers["web"].id
```

## For_each med Set

```hcl
resource "aws_iam_user" "users" {
  for_each = toset(["alice", "bob", "charlie"])
  name     = each.value
}
```

| Meta-arg | Bäst för |
|----------|---------|
| count | Antal resurser |
| for_each | Map/Set av resurser |

**Nästa steg:** Node 8 - Expressions

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Expressions & Functions",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Expressions & Functions

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Dynamisk HCL.

## Conditional

```hcl
instance_type = var.env == "prod" ? "t3.large" : "t3.micro"
```

## For Expressions

```hcl
# List transformation
instance_ids = [for i in aws_instance.web : i.id]

# Map transformation
instance_ips = {for i in aws_instance.web : i.tags.Name => i.public_ip}

# Filtering
large_instances = [for i in aws_instance.web : i.id if i.instance_type == "t3.large"]
```

## String Functions

```hcl
upper("hello")           # "HELLO"
lower("HELLO")           # "hello"
title("hello world")     # "Hello World"
format("Hello, %s!", var.name)
join(", ", ["a", "b"])   # "a, b"
split(",", "a,b,c")      # ["a", "b", "c"]
```

## Collection Functions

```hcl
length(["a", "b", "c"])   # 3
concat([1, 2], [3, 4])    # [1, 2, 3, 4]
merge({a = 1}, {b = 2})   # {a = 1, b = 2}
lookup({a = 1}, "a", 0)   # 1
contains(["a", "b"], "a") # true
```

## Filesystem

```hcl
file("script.sh")         # Läs fil
templatefile("user_data.tftpl", {
  name = var.name
})
```

## Dynamic Blocks

```hcl
resource "aws_security_group" "web" {
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidrs
    }
  }
}
```

**Nästa steg:** Node 9 - Modules Basics

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Modules Basics",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Terraform Modules

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Återanvändbar infrastrukturkod.

## Module Structure

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    README.md
```

## Skapa Module

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block = var.cidr_block

  tags = {
    Name = var.name
  }
}

resource "aws_subnet" "public" {
  count  = length(var.public_subnets)
  vpc_id = aws_vpc.this.id
  cidr_block = var.public_subnets[count.index]
}

# modules/vpc/variables.tf
variable "cidr_block" {
  type = string
}

variable "name" {
  type = string
}

variable "public_subnets" {
  type = list(string)
}

# modules/vpc/outputs.tf
output "vpc_id" {
  value = aws_vpc.this.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}
```

## Använda Module

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"

  name           = "production"
  cidr_block     = "10.0.0.0/16"
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
}

# Referera output
resource "aws_instance" "web" {
  subnet_id = module.vpc.public_subnet_ids[0]
}
```

**Nästa steg:** Node 10 - Module Sources

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Module Sources",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Module Sources

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hämta modules från olika källor.

## Local Path

```hcl
module "vpc" {
  source = "./modules/vpc"
}

module "shared" {
  source = "../shared-modules/vpc"
}
```

## Terraform Registry

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}
```

## Git

```hcl
# HTTPS
module "vpc" {
  source = "git::https://github.com/org/terraform-modules.git//vpc?ref=v1.0.0"
}

# SSH
module "vpc" {
  source = "git@github.com:org/terraform-modules.git//vpc?ref=main"
}
```

## S3

```hcl
module "vpc" {
  source = "s3::https://s3-eu-north-1.amazonaws.com/bucket/vpc.zip"
}
```

## Version Constraints

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"  # >= 5.0.0, < 6.0.0
}
```

| Source | Användning |
|--------|-----------|
| Local | Utveckling |
| Registry | Officiella modules |
| Git | Privata modules |
| S3/GCS | Enterprise |

**Nästa steg:** Node 11 - Module Patterns

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Module Patterns",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Module Design Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Best practices för modules.

## Composition Pattern

```hcl
# Root module sammansätter child modules
module "network" {
  source = "./modules/network"
}

module "compute" {
  source = "./modules/compute"
  vpc_id = module.network.vpc_id
}

module "database" {
  source     = "./modules/database"
  subnet_ids = module.network.private_subnet_ids
}
```

## Wrapper Module

```hcl
# Wrap och förenkla community module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  # Sätt defaults för din org
  name = var.name
  cidr = var.cidr

  azs             = ["eu-north-1a", "eu-north-1b"]
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  enable_nat_gateway = true
  single_nat_gateway = var.environment != "prod"

  tags = local.common_tags
}
```

## Validation

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

## Sensitive Outputs

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

| Pattern | Användning |
|---------|-----------|
| Composition | Kombinera modules |
| Wrapper | Standardisera |
| Facade | Förenkla interface |

**Nästa steg:** Node 12 - Workspaces

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Workspaces",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Terraform Workspaces

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hantera flera miljöer.

## Workspace Commands

```bash
# Lista workspaces
terraform workspace list

# Skapa workspace
terraform workspace new staging
terraform workspace new production

# Byt workspace
terraform workspace select staging

# Visa aktiv
terraform workspace show

# Ta bort
terraform workspace delete staging
```

## Använd i Config

```hcl
# Conditional baserat på workspace
locals {
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"
  instance_count = terraform.workspace == "prod" ? 3 : 1
}

resource "aws_instance" "web" {
  count         = local.instance_count
  instance_type = local.instance_type

  tags = {
    Environment = terraform.workspace
  }
}
```

## Workspace vs Directories

```
# Workspace approach
terraform workspace select staging
terraform apply

# Directory approach (ofta bättre)
environments/
  dev/
    main.tf
    terraform.tfvars
  staging/
    main.tf
    terraform.tfvars
  prod/
    main.tf
    terraform.tfvars
```

| Approach | Pros | Cons |
|----------|------|------|
| Workspace | Enkel setup | Delad state-fil |
| Directory | Isolerad state | Mer boilerplate |

**Nästa steg:** Node 13 - AWS Resources

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "AWS Resources",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# AWS med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Vanliga AWS-resurser.

## VPC & Networking

```hcl
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "eu-north-1a"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}
```

## EC2

```hcl
resource "aws_instance" "web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = file("userdata.sh")
}

resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
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
```

## RDS

```hcl
resource "aws_db_instance" "postgres" {
  identifier        = "mydb"
  engine            = "postgres"
  engine_version    = "15"
  instance_class    = "db.t3.micro"
  allocated_storage = 20

  db_name  = "myapp"
  username = "admin"
  password = var.db_password

  skip_final_snapshot = true
}
```

**Nästa steg:** Node 14 - EKS & Containers

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "EKS & Containers",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# EKS med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Kubernetes på AWS.

## EKS Cluster

```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.0"

  cluster_name    = "my-cluster"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 3
      desired_size = 2

      instance_types = ["t3.medium"]
    }
  }
}
```

## ECR

```hcl
resource "aws_ecr_repository" "app" {
  name                 = "my-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
```

## ECS

```hcl
resource "aws_ecs_cluster" "main" {
  name = "my-cluster"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512

  container_definitions = jsonencode([
    {
      name  = "app"
      image = "${aws_ecr_repository.app.repository_url}:latest"
      portMappings = [
        {
          containerPort = 8080
        }
      ]
    }
  ])
}
```

| Service | Användning |
|---------|-----------|
| EKS | Managed Kubernetes |
| ECS | Container orchestration |
| ECR | Container registry |
| Fargate | Serverless containers |

**Nästa steg:** Node 15 - S3 & IAM

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "S3 & IAM",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# S3 & IAM med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Storage och access management.

## S3 Bucket

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "my-unique-bucket-name"
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

## IAM Role

```hcl
resource "aws_iam_role" "lambda" {
  name = "lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
```

## IAM Policy

```hcl
resource "aws_iam_policy" "s3_read" {
  name = "s3-read-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.data.arn,
          "${aws_s3_bucket.data.arn}/*"
        ]
      }
    ]
  })
}
```

**Nästa steg:** Node 16 - Multi-Cloud

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Multi-Cloud",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 150,
                "content": r"""
# Multi-Cloud Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hantera flera clouds.

## Azure Resources

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "my-rg"
  location = "North Europe"
}

resource "azurerm_virtual_network" "main" {
  name                = "my-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}
```

## GCP Resources

```hcl
provider "google" {
  project = "my-project"
  region  = "europe-north1"
}

resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_instance" "vm" {
  name         = "my-vm"
  machine_type = "e2-micro"
  zone         = "europe-north1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = google_compute_network.vpc.id
  }
}
```

## Multi-Cloud Architecture

```hcl
# AWS primary
module "aws_infra" {
  source = "./modules/aws"
  providers = {
    aws = aws.primary
  }
}

# GCP for ML workloads
module "gcp_ml" {
  source = "./modules/gcp"
  providers = {
    google = google.ml
  }
}
```

| Cloud | Provider |
|-------|----------|
| AWS | hashicorp/aws |
| Azure | hashicorp/azurerm |
| GCP | hashicorp/google |
| K8s | hashicorp/kubernetes |

**Nästa steg:** Node 17 - Testing

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Terraform Testing",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Terraform Testing

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Testa din infrastrukturkod.

## Terraform Validate

```bash
terraform validate
```

## Terraform Plan

```bash
# Dry-run
terraform plan

# Spara plan
terraform plan -out=tfplan
terraform apply tfplan
```

## Terratest (Go)

```go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
)

func TestVPC(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        Vars: map[string]interface{}{
            "cidr_block": "10.0.0.0/16",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcId)
}
```

## Terraform Test (Native)

```hcl
# tests/vpc.tftest.hcl
run "vpc_creation" {
  command = apply

  variables {
    cidr_block = "10.0.0.0/16"
  }

  assert {
    condition     = aws_vpc.main.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block is incorrect"
  }
}
```

```bash
terraform test
```

**Nästa steg:** Node 18 - CI/CD Integration

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "CI/CD Integration",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Terraform CI/CD

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisera Terraform.

## GitHub Actions

```yaml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Format
        run: terraform fmt -check

      - name: Terraform Plan
        run: terraform plan -no-color
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve
```

## Atlantis

```yaml
# atlantis.yaml
version: 3
projects:
  - name: production
    dir: environments/prod
    autoplan:
      when_modified: ["*.tf"]
```

## GitLab CI

```yaml
stages:
  - validate
  - plan
  - apply

plan:
  stage: plan
  script:
    - terraform init
    - terraform plan -out=tfplan
  artifacts:
    paths:
      - tfplan

apply:
  stage: apply
  script:
    - terraform apply tfplan
  when: manual
  only:
    - main
```

| Tool | Approach |
|------|----------|
| GitHub Actions | Push-based |
| Atlantis | PR comments |
| Terraform Cloud | Managed |

**Nästa steg:** Node 19 - Security

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Terraform Security",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 150,
                "content": r"""
# Terraform Security

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Säker infrastrukturkod.

## Secrets Management

```hcl
# Aldrig hårdkoda secrets!

# Använd variables
variable "db_password" {
  type      = string
  sensitive = true
}

# Eller data sources
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}
```

## tfsec Scanning

```bash
# Installera
brew install tfsec

# Scan
tfsec .

# Ignore specific check
#tfsec:ignore:aws-s3-enable-bucket-logging
resource "aws_s3_bucket" "logs" {
  # ...
}
```

## Checkov

```bash
# Installera
pip install checkov

# Scan
checkov -d .

# Som GitHub Action
- uses: bridgecrewio/checkov-action@master
  with:
    directory: .
```

## Drift Detection

```bash
# Detektera drift
terraform plan -detailed-exitcode

# Exit codes:
# 0 = No changes
# 1 = Error
# 2 = Changes detected
```

## State Security

```hcl
# Krypterad state
terraform {
  backend "s3" {
    encrypt = true
    kms_key_id = "alias/terraform-state"
  }
}
```

| Tool | Funktion |
|------|----------|
| tfsec | Security scanning |
| checkov | Policy-as-code |
| Sentinel | Enterprise policies |

**Nästa steg:** Node 20 - Best Practices

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Terraform Best Practices",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 175,
                "content": r"""
# Terraform Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Produktion-redo Terraform.

## File Structure

```
project/
  modules/
    vpc/
    compute/
    database/
  environments/
    dev/
      main.tf
      backend.tf
      variables.tf
      terraform.tfvars
    prod/
      main.tf
      backend.tf
      variables.tf
      terraform.tfvars
```

## Naming Conventions

```hcl
# Resource naming
resource "aws_instance" "web_server" {}  # snake_case
resource "aws_s3_bucket" "app_data" {}

# Variable naming
variable "instance_type" {}
variable "enable_monitoring" {}
```

## Tagging Strategy

```hcl
locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
    Owner       = var.owner
  }
}

resource "aws_instance" "web" {
  tags = merge(local.common_tags, {
    Name = "web-server"
  })
}
```

## Locking

```bash
# Alltid använda state locking
terraform apply -lock=true

# Lock timeout
terraform apply -lock-timeout=5m
```

## Checklist

| Practice | Implementation |
|----------|----------------|
| Remote state | S3/GCS/Azure Blob |
| State locking | DynamoDB/etc |
| Encrypt state | Enable encryption |
| Pin versions | required_version |
| Use modules | DRY kod |
| Validate | CI/CD pipeline |
| Scan security | tfsec/checkov |
| Tag resources | common_tags |
| Document | README per module |

**Grattis! Du har slutfört Terraform Mastery SkillsMap!**

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Terraform Introduktion",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 100,
                "content": r"""
# Terraform Introduktion

Infrastructure as Code med HashiCorp Terraform.

## Varför Terraform?

| Funktion | Fördel |
|----------|--------|
| Deklarativ | Beskriv önskat tillstånd |
| Multi-cloud | AWS, Azure, GCP, etc |
| State | Spårar resurser |
| Plan | Förhandsgranska ändringar |
| Modular | Återanvändbar kod |

## Installation

```bash
# macOS
brew install terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Verifiera
terraform version
```

## Första Projektet

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}
```

## Grundläggande Workflow

```bash
terraform init      # Initiera, ladda providers
terraform plan      # Visa ändringar
terraform apply     # Applicera ändringar
terraform destroy   # Ta bort allt
```

**Nästa steg:** Node 2 - HCL Syntax

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "HCL Syntax",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 120,
                "content": r"""
# HCL Syntax

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


HashiCorp Configuration Language.

## Block Types

```hcl
# Resource block
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}

# Variable block
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

# Output block
output "instance_ip" {
  value = aws_instance.web.public_ip
}

# Locals block
locals {
  common_tags = {
    Environment = "production"
    Project     = "webapp"
  }
}
```

## Data Types

```hcl
# String
name = "myserver"

# Number
count = 3

# Bool
enabled = true

# List
subnets = ["10.0.1.0/24", "10.0.2.0/24"]

# Map
tags = {
  Name = "web"
  Env  = "prod"
}
```

## Referencing

```hcl
# Resurs-attribut
aws_instance.web.id
aws_instance.web.public_ip

# Variable
var.instance_type

# Local
local.common_tags

# Data source
data.aws_ami.ubuntu.id
```

| Koncept | Syntax |
|---------|--------|
| Resource | resource "type" "name" {} |
| Variable | var.name |
| Output | output "name" {} |
| Local | local.name |

**Nästa steg:** Node 3 - Variables & Outputs

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Variables & Outputs",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Variables & Outputs

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Parametrisera din Terraform-kod.

## Variable Declaration

```hcl
# variables.tf
variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 1
}

variable "enable_monitoring" {
  type    = bool
  default = true
}

variable "allowed_ports" {
  type    = list(number)
  default = [80, 443]
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "dev"
  }
}
```

## Variable Files

```hcl
# terraform.tfvars (auto-loaded)
region         = "eu-west-1"
instance_count = 3

# prod.tfvars
region         = "eu-west-1"
instance_count = 10
```

```bash
# Använd specifik fil
terraform apply -var-file="prod.tfvars"

# CLI variable
terraform apply -var="region=us-east-1"

# Environment variable
export TF_VAR_region="us-east-1"
```

## Outputs

```hcl
# outputs.tf
output "instance_ids" {
  description = "IDs of EC2 instances"
  value       = aws_instance.web[*].id
}

output "load_balancer_dns" {
  value     = aws_lb.main.dns_name
  sensitive = true
}
```

```bash
# Visa outputs
terraform output
terraform output instance_ids
```

**Nästa steg:** Node 4 - State Management

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "State Management",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# State Management

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Terraform state spårar infrastruktur.

## Lokal State

```bash
# Default: terraform.tfstate
ls -la terraform.tfstate
```

## Remote State (Rekommenderat)

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## State Commands

```bash
# Lista resurser i state
terraform state list

# Visa specifik resurs
terraform state show aws_instance.web

# Flytta resurs (rename)
terraform state mv aws_instance.web aws_instance.app

# Ta bort från state (inte infra)
terraform state rm aws_instance.old

# Importera befintlig resurs
terraform import aws_instance.web i-1234567890
```

## State Locking

```hcl
# DynamoDB för locking (AWS)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

| Backend | Locking |
|---------|---------|
| S3 + DynamoDB | Ja |
| Azure Blob | Ja |
| GCS | Ja |
| Terraform Cloud | Ja |

**Nästa steg:** Node 5 - Resources & Data Sources

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Resources & Data Sources",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# Resources & Data Sources

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Skapa och läs infrastruktur.

## Resources

```hcl
# Skapa resurs
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}
```

## Data Sources

```hcl
# Läs befintlig data
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

## Lifecycle

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [tags]
  }
}
```

## Provisioners (Undvik om möjligt)

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx"
    ]
  }
}
```

**Nästa steg:** Node 6 - Providers

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Providers",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Terraform Providers

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Providers kopplar till cloud APIs.

## Provider Configuration

```hcl
# AWS
provider "aws" {
  region  = "eu-north-1"
  profile = "production"
}

# Azure
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

# Google Cloud
provider "google" {
  project = "my-project"
  region  = "europe-north1"
}
```

## Multiple Providers

```hcl
provider "aws" {
  region = "eu-north-1"
  alias  = "stockholm"
}

provider "aws" {
  region = "us-east-1"
  alias  = "virginia"
}

resource "aws_instance" "eu" {
  provider = aws.stockholm
  # ...
}

resource "aws_instance" "us" {
  provider = aws.virginia
  # ...
}
```

## Version Constraints

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0, < 3.0"
    }
  }
}
```

| Constraint | Betydelse |
|------------|-----------|
| = 1.0.0 | Exakt version |
| >= 1.0 | Minst 1.0 |
| ~> 5.0 | >= 5.0, < 6.0 |
| >= 2.0, < 3.0 | Range |

**Nästa steg:** Node 7 - Count & For_each

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Count & For_each",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Count & For_each

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Skapa flera resurser.

## Count

```hcl
resource "aws_instance" "web" {
  count = 3

  ami           = "ami-12345"
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}

# Referera
aws_instance.web[0].id
aws_instance.web[*].id  # Alla
```

## Conditional Count

```hcl
variable "create_instance" {
  type    = bool
  default = true
}

resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
  # ...
}
```

## For_each med Map

```hcl
variable "instances" {
  default = {
    web    = "t3.micro"
    api    = "t3.small"
    worker = "t3.medium"
  }
}

resource "aws_instance" "servers" {
  for_each = var.instances

  ami           = "ami-12345"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}

# Referera
aws_instance.servers["web"].id
```

## For_each med Set

```hcl
resource "aws_iam_user" "users" {
  for_each = toset(["alice", "bob", "charlie"])
  name     = each.value
}
```

| Meta-arg | Bäst för |
|----------|---------|
| count | Antal resurser |
| for_each | Map/Set av resurser |

**Nästa steg:** Node 8 - Expressions

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Expressions & Functions",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Expressions & Functions

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Dynamisk HCL.

## Conditional

```hcl
instance_type = var.env == "prod" ? "t3.large" : "t3.micro"
```

## For Expressions

```hcl
# List transformation
instance_ids = [for i in aws_instance.web : i.id]

# Map transformation
instance_ips = {for i in aws_instance.web : i.tags.Name => i.public_ip}

# Filtering
large_instances = [for i in aws_instance.web : i.id if i.instance_type == "t3.large"]
```

## String Functions

```hcl
upper("hello")           # "HELLO"
lower("HELLO")           # "hello"
title("hello world")     # "Hello World"
format("Hello, %s!", var.name)
join(", ", ["a", "b"])   # "a, b"
split(",", "a,b,c")      # ["a", "b", "c"]
```

## Collection Functions

```hcl
length(["a", "b", "c"])   # 3
concat([1, 2], [3, 4])    # [1, 2, 3, 4]
merge({a = 1}, {b = 2})   # {a = 1, b = 2}
lookup({a = 1}, "a", 0)   # 1
contains(["a", "b"], "a") # true
```

## Filesystem

```hcl
file("script.sh")         # Läs fil
templatefile("user_data.tftpl", {
  name = var.name
})
```

## Dynamic Blocks

```hcl
resource "aws_security_group" "web" {
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidrs
    }
  }
}
```

**Nästa steg:** Node 9 - Modules Basics

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Modules Basics",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Terraform Modules

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Återanvändbar infrastrukturkod.

## Module Structure

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    README.md
```

## Skapa Module

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block = var.cidr_block

  tags = {
    Name = var.name
  }
}

resource "aws_subnet" "public" {
  count  = length(var.public_subnets)
  vpc_id = aws_vpc.this.id
  cidr_block = var.public_subnets[count.index]
}

# modules/vpc/variables.tf
variable "cidr_block" {
  type = string
}

variable "name" {
  type = string
}

variable "public_subnets" {
  type = list(string)
}

# modules/vpc/outputs.tf
output "vpc_id" {
  value = aws_vpc.this.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}
```

## Använda Module

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"

  name           = "production"
  cidr_block     = "10.0.0.0/16"
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
}

# Referera output
resource "aws_instance" "web" {
  subnet_id = module.vpc.public_subnet_ids[0]
}
```

**Nästa steg:** Node 10 - Module Sources

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Module Sources",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Module Sources

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hämta modules från olika källor.

## Local Path

```hcl
module "vpc" {
  source = "./modules/vpc"
}

module "shared" {
  source = "../shared-modules/vpc"
}
```

## Terraform Registry

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}
```

## Git

```hcl
# HTTPS
module "vpc" {
  source = "git::https://github.com/org/terraform-modules.git//vpc?ref=v1.0.0"
}

# SSH
module "vpc" {
  source = "git@github.com:org/terraform-modules.git//vpc?ref=main"
}
```

## S3

```hcl
module "vpc" {
  source = "s3::https://s3-eu-north-1.amazonaws.com/bucket/vpc.zip"
}
```

## Version Constraints

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"  # >= 5.0.0, < 6.0.0
}
```

| Source | Användning |
|--------|-----------|
| Local | Utveckling |
| Registry | Officiella modules |
| Git | Privata modules |
| S3/GCS | Enterprise |

**Nästa steg:** Node 11 - Module Patterns

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Module Patterns",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Module Design Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Best practices för modules.

## Composition Pattern

```hcl
# Root module sammansätter child modules
module "network" {
  source = "./modules/network"
}

module "compute" {
  source = "./modules/compute"
  vpc_id = module.network.vpc_id
}

module "database" {
  source     = "./modules/database"
  subnet_ids = module.network.private_subnet_ids
}
```

## Wrapper Module

```hcl
# Wrap och förenkla community module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  # Sätt defaults för din org
  name = var.name
  cidr = var.cidr

  azs             = ["eu-north-1a", "eu-north-1b"]
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  enable_nat_gateway = true
  single_nat_gateway = var.environment != "prod"

  tags = local.common_tags
}
```

## Validation

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

## Sensitive Outputs

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

| Pattern | Användning |
|---------|-----------|
| Composition | Kombinera modules |
| Wrapper | Standardisera |
| Facade | Förenkla interface |

**Nästa steg:** Node 12 - Workspaces

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Workspaces",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Terraform Workspaces

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hantera flera miljöer.

## Workspace Commands

```bash
# Lista workspaces
terraform workspace list

# Skapa workspace
terraform workspace new staging
terraform workspace new production

# Byt workspace
terraform workspace select staging

# Visa aktiv
terraform workspace show

# Ta bort
terraform workspace delete staging
```

## Använd i Config

```hcl
# Conditional baserat på workspace
locals {
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"
  instance_count = terraform.workspace == "prod" ? 3 : 1
}

resource "aws_instance" "web" {
  count         = local.instance_count
  instance_type = local.instance_type

  tags = {
    Environment = terraform.workspace
  }
}
```

## Workspace vs Directories

```
# Workspace approach
terraform workspace select staging
terraform apply

# Directory approach (ofta bättre)
environments/
  dev/
    main.tf
    terraform.tfvars
  staging/
    main.tf
    terraform.tfvars
  prod/
    main.tf
    terraform.tfvars
```

| Approach | Pros | Cons |
|----------|------|------|
| Workspace | Enkel setup | Delad state-fil |
| Directory | Isolerad state | Mer boilerplate |

**Nästa steg:** Node 13 - AWS Resources

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "AWS Resources",
                "difficulty": "expert",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# AWS med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Vanliga AWS-resurser.

## VPC & Networking

```hcl
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "eu-north-1a"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}
```

## EC2

```hcl
resource "aws_instance" "web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = file("userdata.sh")
}

resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
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
```

## RDS

```hcl
resource "aws_db_instance" "postgres" {
  identifier        = "mydb"
  engine            = "postgres"
  engine_version    = "15"
  instance_class    = "db.t3.micro"
  allocated_storage = 20

  db_name  = "myapp"
  username = "admin"
  password = var.db_password

  skip_final_snapshot = true
}
```

**Nästa steg:** Node 14 - EKS & Containers

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "EKS & Containers",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# EKS med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Kubernetes på AWS.

## EKS Cluster

```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.0"

  cluster_name    = "my-cluster"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 3
      desired_size = 2

      instance_types = ["t3.medium"]
    }
  }
}
```

## ECR

```hcl
resource "aws_ecr_repository" "app" {
  name                 = "my-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
```

## ECS

```hcl
resource "aws_ecs_cluster" "main" {
  name = "my-cluster"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512

  container_definitions = jsonencode([
    {
      name  = "app"
      image = "${aws_ecr_repository.app.repository_url}:latest"
      portMappings = [
        {
          containerPort = 8080
        }
      ]
    }
  ])
}
```

| Service | Användning |
|---------|-----------|
| EKS | Managed Kubernetes |
| ECS | Container orchestration |
| ECR | Container registry |
| Fargate | Serverless containers |

**Nästa steg:** Node 15 - S3 & IAM

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "S3 & IAM",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# S3 & IAM med Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Storage och access management.

## S3 Bucket

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "my-unique-bucket-name"
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

## IAM Role

```hcl
resource "aws_iam_role" "lambda" {
  name = "lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
```

## IAM Policy

```hcl
resource "aws_iam_policy" "s3_read" {
  name = "s3-read-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.data.arn,
          "${aws_s3_bucket.data.arn}/*"
        ]
      }
    ]
  })
}
```

**Nästa steg:** Node 16 - Multi-Cloud

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Multi-Cloud",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 150,
                "content": r"""
# Multi-Cloud Terraform

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Hantera flera clouds.

## Azure Resources

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "my-rg"
  location = "North Europe"
}

resource "azurerm_virtual_network" "main" {
  name                = "my-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}
```

## GCP Resources

```hcl
provider "google" {
  project = "my-project"
  region  = "europe-north1"
}

resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_instance" "vm" {
  name         = "my-vm"
  machine_type = "e2-micro"
  zone         = "europe-north1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = google_compute_network.vpc.id
  }
}
```

## Multi-Cloud Architecture

```hcl
# AWS primary
module "aws_infra" {
  source = "./modules/aws"
  providers = {
    aws = aws.primary
  }
}

# GCP for ML workloads
module "gcp_ml" {
  source = "./modules/gcp"
  providers = {
    google = google.ml
  }
}
```

| Cloud | Provider |
|-------|----------|
| AWS | hashicorp/aws |
| Azure | hashicorp/azurerm |
| GCP | hashicorp/google |
| K8s | hashicorp/kubernetes |

**Nästa steg:** Node 17 - Testing

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Terraform Testing",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Terraform Testing

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Testa din infrastrukturkod.

## Terraform Validate

```bash
terraform validate
```

## Terraform Plan

```bash
# Dry-run
terraform plan

# Spara plan
terraform plan -out=tfplan
terraform apply tfplan
```

## Terratest (Go)

```go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
)

func TestVPC(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        Vars: map[string]interface{}{
            "cidr_block": "10.0.0.0/16",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcId)
}
```

## Terraform Test (Native)

```hcl
# tests/vpc.tftest.hcl
run "vpc_creation" {
  command = apply

  variables {
    cidr_block = "10.0.0.0/16"
  }

  assert {
    condition     = aws_vpc.main.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block is incorrect"
  }
}
```

```bash
terraform test
```

**Nästa steg:** Node 18 - CI/CD Integration

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "CI/CD Integration",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Terraform CI/CD

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisera Terraform.

## GitHub Actions

```yaml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Format
        run: terraform fmt -check

      - name: Terraform Plan
        run: terraform plan -no-color
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve
```

## Atlantis

```yaml
# atlantis.yaml
version: 3
projects:
  - name: production
    dir: environments/prod
    autoplan:
      when_modified: ["*.tf"]
```

## GitLab CI

```yaml
stages:
  - validate
  - plan
  - apply

plan:
  stage: plan
  script:
    - terraform init
    - terraform plan -out=tfplan
  artifacts:
    paths:
      - tfplan

apply:
  stage: apply
  script:
    - terraform apply tfplan
  when: manual
  only:
    - main
```

| Tool | Approach |
|------|----------|
| GitHub Actions | Push-based |
| Atlantis | PR comments |
| Terraform Cloud | Managed |

**Nästa steg:** Node 19 - Security

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Terraform Security",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 150,
                "content": r"""
# Terraform Security

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Säker infrastrukturkod.

## Secrets Management

```hcl
# Aldrig hårdkoda secrets!

# Använd variables
variable "db_password" {
  type      = string
  sensitive = true
}

# Eller data sources
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}
```

## tfsec Scanning

```bash
# Installera
brew install tfsec

# Scan
tfsec .

# Ignore specific check
#tfsec:ignore:aws-s3-enable-bucket-logging
resource "aws_s3_bucket" "logs" {
  # ...
}
```

## Checkov

```bash
# Installera
pip install checkov

# Scan
checkov -d .

# Som GitHub Action
- uses: bridgecrewio/checkov-action@master
  with:
    directory: .
```

## Drift Detection

```bash
# Detektera drift
terraform plan -detailed-exitcode

# Exit codes:
# 0 = No changes
# 1 = Error
# 2 = Changes detected
```

## State Security

```hcl
# Krypterad state
terraform {
  backend "s3" {
    encrypt = true
    kms_key_id = "alias/terraform-state"
  }
}
```

| Tool | Funktion |
|------|----------|
| tfsec | Security scanning |
| checkov | Policy-as-code |
| Sentinel | Enterprise policies |

**Nästa steg:** Node 20 - Best Practices

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Terraform Best Practices",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 175,
                "content": r"""
# Terraform Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Produktion-redo Terraform.

## File Structure

```
project/
  modules/
    vpc/
    compute/
    database/
  environments/
    dev/
      main.tf
      backend.tf
      variables.tf
      terraform.tfvars
    prod/
      main.tf
      backend.tf
      variables.tf
      terraform.tfvars
```

## Naming Conventions

```hcl
# Resource naming
resource "aws_instance" "web_server" {}  # snake_case
resource "aws_s3_bucket" "app_data" {}

# Variable naming
variable "instance_type" {}
variable "enable_monitoring" {}
```

## Tagging Strategy

```hcl
locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
    Owner       = var.owner
  }
}

resource "aws_instance" "web" {
  tags = merge(local.common_tags, {
    Name = "web-server"
  })
}
```

## Locking

```bash
# Alltid använda state locking
terraform apply -lock=true

# Lock timeout
terraform apply -lock-timeout=5m
```

## Checklist

| Practice | Implementation |
|----------|----------------|
| Remote state | S3/GCS/Azure Blob |
| State locking | DynamoDB/etc |
| Encrypt state | Enable encryption |
| Pin versions | required_version |
| Use modules | DRY kod |
| Validate | CI/CD pipeline |
| Scan security | tfsec/checkov |
| Tag resources | common_tags |
| Document | README per module |

**Grattis! Du har slutfört Terraform Mastery SkillsMap!**

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_TERRAFORM_MASTERY


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_TERRAFORM_MASTERY["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
