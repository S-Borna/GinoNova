"""
Terraform Mastery Module
========================

Komplett kurs i Infrastructure as Code med Terraform.
Följer Linux-mallen: Svenska, pedagogiskt, bash-kommentarer på varje rad.

20 noder från grundläggande till avancerat.
"""

MODULE = {
    "name": "Terraform Mastery",
    "slug": "terraform-mastery",
    "description": "Bygg skalbar infrastruktur som kod med Terraform",
    "track_slug": "infrastructure",
    "order_index": 7,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "🏗️",
    "color": "#7B42BC",
    "tasks": [
        {
            "title": "Introduction to Terraform",
            "slug": "introduction-to-terraform",
            "difficulty": "beginner",
            "content": """
# Introduction to Terraform

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan IaC | Konsekvens |
|-----------------|------------|
| Manuell infrastruktur | Timmar att satta upp, felbelagt |
| Ingen versionshantering | Vet inte vad som andrades eller nar |
| Svar att replikera | Staging ≠ Production = buggar |
| Dokumentation ur synk | README sager en sak, verkligheten en annan |

Terraform loser allt detta genom Infrastructure as Code. Du beskriver onskat tillstand i kod, Terraform gor verkligheten. Deklarativt, versionshanterat, replikerbart.

+-------------+     +-------------+     +-------------+
|   .tf fil   |----▶|   terraform |----▶|    Cloud    |
|   (onskat)  |     |   plan/apply|     |   (verklig) |
+-------------+     +-------------+     +-------------+
       |                   |                   |
       ▼                   ▼                   ▼
+-------------+     +-------------+     +-------------+
| Git version |     | State file  |     | EC2, S3,    |
| control     |     | (mapping)   |     | VPC, RDS... |
+-------------+     +-------------+     +-------------+

------------------------------------------------------------

---

## Installation

```bash
# macOS med Homebrew
brew tap hashicorp/tap             # Lägg till HashiCorp repo
brew install hashicorp/tap/terraform  # Installera Terraform

# Linux (Ubuntu/Debian)
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# Verifiera installation
terraform version                    # Visa version
terraform -help                      # Visa hjälp
```

---

## Första konfigurationen

```hcl
# main.tf - Minimal Terraform config

# Terraform settings block
terraform {
  required_version = ">= 1.0.0"      # Kräv minst denna version

  required_providers {
    aws = {
      source  = "hashicorp/aws"       # Provider source
      version = "~> 5.0"              # Version constraint
    }
  }
}

# Provider configuration
provider "aws" {
  region = "eu-north-1"              # Stockholm region
}

# Första resursen - en S3 bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-bucket-name-12345"  # Måste vara globalt unikt

  tags = {
    Name        = "Example Bucket"
    Environment = "dev"
  }
}
```

---

## Grundläggande workflow

```bash
# Steg 1: Initiera projekt
terraform init                       # Ladda ner providers, sätt upp backend

# Steg 2: Formatera kod
terraform fmt                        # Autoformatera .tf-filer
terraform fmt -check                 # Kontrollera formatering

# Steg 3: Validera konfiguration
terraform validate                   # Syntaxkontroll

# Steg 4: Planera ändringar
terraform plan                       # Visa vad som kommer ändras
terraform plan -out=tfplan           # Spara plan till fil

# Steg 5: Applicera ändringar
terraform apply                      # Applicera med bekräftelse
terraform apply tfplan               # Applicera sparad plan
terraform apply -auto-approve        # Utan bekräftelse (CI/CD)

# Steg 6: Visa state
terraform show                       # Visa aktuellt state
terraform state list                 # Lista resurser

# Steg 7: Ta bort resurser
terraform destroy                    # Ta bort ALLT
terraform destroy -target=aws_s3_bucket.example  # Specifik resurs
```

---

## Terraform vs alternativ

```
Terraform           | CloudFormation      | Pulumi
--------------------|---------------------|-------------------
Multi-cloud         | Endast AWS          | Multi-cloud
HCL syntax          | YAML/JSON           | Python/TS/Go
Declarative         | Declarative         | Imperative möjligt
State file          | Stack state         | State file
Drift detection     | Drift detection     | Drift detection
Providers ecosystem | Limited             | SDKs
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Deklarativt | Beskriv onskat tillstand, Terraform gor resten |
| Workflow | init -> plan -> apply ar standard |
| State-fil | Kritisk - mappar config till verklig infrastruktur |
| HCL | HashiCorp Configuration Language for infra |
| Providers | Plugins for AWS, Azure, GCP, Kubernetes mm |

## Kom ihag

- terraform init laddar providers och satter upp backend
- terraform plan visar EXAKT vad som kommer andras
- ALDRIG editera state-filen manuellt
- terraform destroy tar bort ALLT - var forsiktig
- Version-locka providers for reproducerbarhet
""",
        },
        {
            "title": "HCL Syntax & Basics",
            "slug": "hcl-syntax-basics",
            "difficulty": "beginner",
            "content": """
# HCL Syntax & Basics

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan HCL-kunskap | Konsekvens |
|-------------------------|------------|
| Gissar pa syntax | Standig trial-and-error debugging |
| Fel variabeltyper | Runtime-fel vid terraform apply |
| Hardkodade varden | Samma config funkar inte i staging vs prod |
| Ingen kod-atervanvandning | Copy-paste helvete |

HCL ar Terraforms sprak - designat for infrastruktur, lasbart for manniskor och maskiner. Forsta syntax = skriv effektiv, underhallbar Terraform-kod.

+---------------------------------------------------------+
|                    HCL BUILDING BLOCKS                   |
+---------------------------------------------------------+
|  terraform { }    - Global konfiguration                |
|  provider "x" { } - Plugin-konfiguration                |
|  resource "x" { } - Skapar infrastruktur                |
|  variable "x" { } - Input-varden                        |
|  output "x" { }   - Exporterar varden                   |
|  locals { }       - Lokala varden                       |
|  data "x" { }     - Laser extern data                   |
|  module "x" { }   - Ateranvander kod                    |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Block-typer

```hcl
# Terraform block - global konfiguration
terraform {
  required_version = ">= 1.0"
  backend "s3" {
    bucket = "my-tf-state"
  }
}

# Provider block - konfigurerar provider
provider "aws" {
  region = "eu-north-1"
}

# Resource block - skapar infrastruktur
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
}

# Variable block - input-värden
variable "environment" {
  type        = string
  default     = "dev"
  description = "The deployment environment"
}

# Output block - exponera värden
output "instance_ip" {
  value       = aws_instance.web.public_ip
  description = "Public IP of the web server"
}

# Locals block - lokala värden
locals {
  common_tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# Data block - läs extern data
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical
}

# Module block - återanvänd konfiguration
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
}
```

---

## Datatyper

```hcl
# String
name = "my-server"
name = "Hello, ${var.name}!"         # Interpolation

# Number
count = 3
ratio = 1.5

# Bool
enabled = true
disabled = false

# List (tuple)
availability_zones = ["eu-north-1a", "eu-north-1b", "eu-north-1c"]
first_az = var.availability_zones[0]  # Index access

# Map (object)
tags = {
  Name        = "web-server"
  Environment = "production"
}
env_value = var.tags["Environment"]  # Key access

# Set (unique values)
unique_ports = toset([80, 443, 8080])

# Null
optional_value = null                 # Inte satt
```

---

## Variabeltyper

```hcl
# variables.tf

# String
variable "region" {
  type        = string
  default     = "eu-north-1"
  description = "AWS region"
}

# Number
variable "instance_count" {
  type        = number
  default     = 2
  description = "Number of instances"
}

# Bool
variable "enable_monitoring" {
  type        = bool
  default     = true
  description = "Enable CloudWatch monitoring"
}

# List
variable "allowed_cidrs" {
  type        = list(string)
  default     = ["10.0.0.0/8", "172.16.0.0/12"]
  description = "Allowed CIDR blocks"
}

# Map
variable "instance_types" {
  type = map(string)
  default = {
    dev  = "t3.micro"
    prod = "t3.large"
  }
  description = "Instance types per environment"
}

# Object (complex type)
variable "server_config" {
  type = object({
    name          = string
    instance_type = string
    disk_size     = number
    tags          = map(string)
  })
  default = {
    name          = "web"
    instance_type = "t3.micro"
    disk_size     = 20
    tags          = {}
  }
}

# Sensitive
variable "db_password" {
  type        = string
  sensitive   = true                  # Döljs i output
  description = "Database password"
}
```

---

## Expressions och operatorer

```hcl
# Aritmetik
locals {
  total     = 10 + 5                  # 15
  remaining = 10 - 3                  # 7
  doubled   = 4 * 2                   # 8
  half      = 10 / 2                  # 5
  modulo    = 10 % 3                  # 1
}

# Jämförelser
locals {
  is_prod     = var.environment == "production"
  is_not_dev  = var.environment != "dev"
  is_large    = var.instance_count > 5
  is_valid    = var.count >= 1 && var.count <= 100
}

# Logiska operatorer
locals {
  should_scale = var.enable_scaling && var.instance_count > 1
  needs_alert  = var.cpu_high || var.memory_high
  is_disabled  = !var.enabled
}

# Conditional (ternary)
locals {
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
  db_size       = var.enable_ha ? 100 : 50
}

# String interpolation
locals {
  bucket_name = "app-${var.environment}-${var.region}"
  full_name   = "${var.first_name} ${var.last_name}"
}
```

---

## Referera till resurser

```hcl
# Skapa resurser
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id        # Referens till VPC
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id  # Referens till data source
  instance_type = var.instance_type       # Referens till variabel
  subnet_id     = aws_subnet.public.id    # Referens till subnet

  tags = local.common_tags                # Referens till locals
}

# Output med referens
output "vpc_id" {
  value = aws_vpc.main.id
}

output "instance_dns" {
  value = aws_instance.web.public_dns
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Blocks | Grundenheten: type "label" { ... } |
| Datatyper | string, number, bool, list, map, object |
| Interpolation | ${} for att blanda variabler i strangar |
| Conditional | condition ? true_val : false_val |
| Referenser | resource_type.name.attribute |

## Kom ihag

- variable "x" {} definierar input, var.x anvander det
- locals {} for beraknade varden som ateranvands
- output {} exponerar varden efter apply
- sensitive = true doljer varden i terminal output
- object() for komplexa typer med flera falt
""",
        },
        {
            "title": "Providers & Resources",
            "slug": "providers-and-resources",
            "difficulty": "beginner",
            "content": """
# Providers & Resources

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan provider-kunskap | Konsekvens |
|------------------------------|------------|
| Fel provider-version | Breaking changes, inkompabilitet |
| Hardkodade credentials | Sakerhetsrisk, fungerar inte i CI/CD |
| En provider per projekt | Multi-cloud, multi-region omojligt |
| Ingen version-locking | "Worked yesterday" syndrom |

Providers ar Terraforms plugins - de oversatter HCL till API-anrop. AWS, Azure, GCP, Kubernetes, GitHub - allt via providers. Resources ar objekten du skapar via providers.

+-------------+     +-------------+     +-------------+
|   .tf fil   |----▶|  Provider   |----▶|  Cloud API  |
|  resource   |     |  (plugin)   |     |  (AWS etc)  |
+-------------+     +-------------+     +-------------+
       |                   |                   |
       ▼                   ▼                   ▼
+-------------+     +-------------+     +-------------+
| aws_instance|     | hashicorp/  |     |  EC2 API    |
| aws_s3...   |     |   aws       |     |  S3 API     |
+-------------+     +-------------+     +-------------+

------------------------------------------------------------

---

## Provider-konfiguration

```hcl
# versions.tf - Provider requirements
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"              # >= 5.0.0, < 6.0.0
    }

    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.0, < 4.0"       # Range
    }

    google = {
      source  = "hashicorp/google"
      version = "5.10.0"              # Exakt version
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.25"
    }
  }
}

# providers.tf - Provider configuration
provider "aws" {
  region = "eu-north-1"

  # Credentials från environment eller AWS config
  # AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

  default_tags {
    tags = {
      ManagedBy = "Terraform"
      Project   = "MyApp"
    }
  }
}

provider "azurerm" {
  features {}                         # Krävs för Azure
  subscription_id = var.azure_subscription_id
}

provider "google" {
  project = var.gcp_project
  region  = "europe-north1"
}
```

---

## Multipla providers

```hcl
# Alias för multipla regioner
provider "aws" {
  region = "eu-north-1"
  alias  = "stockholm"
}

provider "aws" {
  region = "eu-west-1"
  alias  = "ireland"
}

# Använd specifik provider
resource "aws_instance" "stockholm_server" {
  provider = aws.stockholm

  ami           = "ami-12345678"
  instance_type = "t3.micro"
}

resource "aws_instance" "ireland_server" {
  provider = aws.ireland

  ami           = "ami-87654321"      # Olika AMI per region
  instance_type = "t3.micro"
}

# Multipla AWS-konton
provider "aws" {
  alias   = "production"
  region  = "eu-north-1"
  profile = "prod"                    # AWS CLI profile
}

provider "aws" {
  alias   = "development"
  region  = "eu-north-1"
  profile = "dev"
}
```

---

## Resource syntax

```hcl
# Syntax: resource "TYPE" "NAME" { ... }

# TYPE = provider_resource (aws_instance, google_compute_instance)
# NAME = lokal identifierare (används för referens)

resource "aws_instance" "web_server" {
  # Required arguments
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  # Optional arguments
  subnet_id                   = aws_subnet.main.id
  vpc_security_group_ids      = [aws_security_group.web.id]
  associate_public_ip_address = true

  # Nested blocks
  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }

  # Tags
  tags = {
    Name = "WebServer"
  }
}

# Referera till resursen
output "instance_id" {
  value = aws_instance.web_server.id
}

output "public_ip" {
  value = aws_instance.web_server.public_ip
}
```

---

## Vanliga AWS-resurser

```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = { Name = "main-vpc" }
}

# Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "eu-north-1a"
  map_public_ip_on_launch = true

  tags = { Name = "public-subnet" }
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

# S3 Bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-unique-bucket-name"
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

# RDS Database
resource "aws_db_instance" "postgres" {
  identifier        = "myapp-db"
  engine            = "postgres"
  engine_version    = "15.4"
  instance_class    = "db.t3.micro"
  allocated_storage = 20

  db_name  = "myapp"
  username = "admin"
  password = var.db_password          # Sensitive variable

  skip_final_snapshot = true          # Dev only
}
```

---

## Data sources

```hcl
# Läs existerande resurser
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]      # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Använd data sources
resource "aws_instance" "web" {
  ami               = data.aws_ami.ubuntu.id
  instance_type     = "t3.micro"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Account = data.aws_caller_identity.current.account_id
    Region  = data.aws_region.current.name
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Provider | Definierar plattform - AWS, Azure, GCP, K8s |
| Resource | Skapar faktisk infrastruktur via provider |
| Alias | Multipla providers av samma typ (regioner, konton) |
| Data source | Laser existerande resurser utan att skapa |
| terraform init | Laddar ner providers fran registry |

## Kom ihag

- version = "~> 5.0" betyder >= 5.0.0, < 6.0.0
- Credentials via environment variabler, aldrig i kod
- default_tags appliceras pa alla resurser automatiskt
- Data sources ger read-only access till existerande resurser
- Terraform Registry har 3000+ providers
""",
        },
        {
            "title": "State Management",
            "slug": "state-management",
            "difficulty": "beginner",
            "content": """
# State Management

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan state-forstaelse | Konsekvens |
|------------------------------|------------|
| Local state i team | Konflikter, dataforlust, inkonsistent infra |
| Ingen state locking | Parallella apply = korrupt state |
| State i Git | Secrets i klartext, versionskaos |
| Forlorad state-fil | Terraform kan inte hantera existerande resurser |

State ar Terraforms hjarna - den mappar din kod till verklig infrastruktur. Utan state vet Terraform inte vad som finns. Remote state med locking ar obligatoriskt for team.

+-------------+     +-------------+     +-------------+
|   .tf kod   |----▶|  State fil  |◀---▶|   Verklig   |
|  (onskat)   |     |  (mapping)  |     |   infra     |
+-------------+     +-------------+     +-------------+
                          |
                          ▼
              +-----------------------+
              |  terraform.tfstate    |
              |  - resource IDs       |
              |  - attributes         |
              |  - dependencies       |
              |  - metadata           |
              +-----------------------+

------------------------------------------------------------

---

## Local state

```bash
# Default: terraform.tfstate i aktuell katalog
ls -la terraform.tfstate             # JSON-fil

# Visa state
terraform show                       # Formaterad output
terraform state list                 # Lista resurser
terraform state show aws_instance.web  # Visa specifik resurs

# State-filen innehåller:
# - Terraform version
# - Resource mappings
# - Metadata
# - Outputs

# VARNING: terraform.tfstate innehåller secrets!
# Lägg ALLTID till i .gitignore:
echo "*.tfstate" >> .gitignore
echo "*.tfstate.*" >> .gitignore
```

---

## Remote state med S3

```hcl
# backend.tf - S3 backend konfiguration
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/networking/terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"  # Locking
  }
}

# Skapa S3 bucket och DynamoDB manuellt först:
# aws s3 mb s3://my-terraform-state --region eu-north-1
# aws dynamodb create-table \
#   --table-name terraform-locks \
#   --attribute-definitions AttributeName=LockID,AttributeType=S \
#   --key-schema AttributeName=LockID,KeyType=HASH \
#   --billing-mode PAY_PER_REQUEST
```

```bash
# Migrera från local till remote
terraform init -migrate-state        # Flytta state till S3
```

---

## Remote state med Azure

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "tfstateaccount"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}
```

---

## State locking

```hcl
# S3 + DynamoDB för locking
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"  # Krävs för locking
  }
}

# Locking förhindrar:
# - Parallella ändringar
# - State corruption
# - Race conditions
```

```bash
# Forcera unlock (använd försiktigt!)
terraform force-unlock LOCK_ID

# Visa lock info
terraform plan                       # Visar om låst
```

---

## State-kommandon

```bash
# Lista resurser i state
terraform state list
# aws_instance.web
# aws_security_group.web
# aws_vpc.main

# Visa specifik resurs
terraform state show aws_instance.web

# Flytta resurs (rename)
terraform state mv aws_instance.web aws_instance.webserver
# Uppdatera också i .tf-filen!

# Ta bort från state (inte från cloud!)
terraform state rm aws_instance.legacy
# Resursen finns kvar i AWS men Terraform "glömmer" den

# Importera existerande resurs
terraform import aws_instance.imported i-1234567890abcdef0
# Skapar state-entry för existerande resurs

# Pull state (för debugging)
terraform state pull > state.json

# Push state (farligt!)
terraform state push state.json

# Refresh state (synka med verklighet)
terraform refresh                    # Deprecated
terraform apply -refresh-only        # Rekommenderas
```

---

## State i CI/CD

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan -out=tfplan

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve tfplan
```

---

## Workspaces

```bash
# Workspaces = separata state-filer
terraform workspace list             # Lista workspaces
terraform workspace new staging      # Skapa workspace
terraform workspace select staging   # Byt workspace
terraform workspace show             # Visa aktuellt
terraform workspace delete staging   # Ta bort

# Använd i konfiguration
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Environment = terraform.workspace
  }
}

# State-path blir:
# s3://bucket/env:/staging/terraform.tfstate
# s3://bucket/env:/prod/terraform.tfstate
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| State-fil | Mappar config till verkliga resurser via ID |
| Remote state | S3, Azure Blob, GCS - obligatoriskt for team |
| State locking | DynamoDB forhindrar parallella apply |
| terraform state | mv, rm, import for state-manipulation |
| Workspaces | Separata state-filer for miljoseparation |

## Kom ihag

- ALDRIG editera terraform.tfstate manuellt
- Remote backend med locking fran dag 1 i team
- terraform state list visar alla hanterade resurser
- terraform import tar in existerande resurser i state
- Backup av state ar kritiskt - aktivera versioning pa S3
""",
        },
        {
            "title": "Variables & Outputs",
            "slug": "variables-and-outputs",
            "difficulty": "beginner",
            "content": """
# Variables & Outputs

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan variabler | Konsekvens |
|-----------------------|------------|
| Hardkodade varden | Copy-paste for varje miljo |
| Secrets i kod | Sakerhetskatastrof vid Git push |
| Ingen flexibilitet | Samma config funkar inte overallt |
| Ingen output | Manuellt kopiera IPs, ARNs etc. |

Variables ar input, outputs ar export. Med dem blir samma Terraform-kod anvandbar i dev, staging och prod. Secrets hanteras sakert via sensitive-flaggan.

+-------------+     +-------------+     +-------------+
|  Variables  |----▶|  Terraform  |----▶|   Outputs   |
|   (input)   |     |    kod      |     |  (export)   |
+-------------+     +-------------+     +-------------+
       |                                       |
       ▼                                       ▼
+-------------+                         +-------------+
| -var        |                         | terraform   |
| -var-file   |                         | output      |
| TF_VAR_     |                         | (query)     |
| terraform.  |                         |             |
|   tfvars    |                         |             |
+-------------+                         +-------------+

------------------------------------------------------------

---

## Input variables

```hcl
# variables.tf

# Grundläggande variabel
variable "region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "eu-north-1"
}

# Utan default (required)
variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  # Ingen default = måste anges
}

# Med validering
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"

  validation {
    condition     = can(regex("^t3\\.", var.instance_type))
    error_message = "Instance type must be t3 family."
  }
}

# Sensitive
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

# Complex type
variable "server_config" {
  description = "Server configuration"
  type = object({
    instance_type = string
    disk_size     = number
    enable_backup = bool
  })
  default = {
    instance_type = "t3.micro"
    disk_size     = 20
    enable_backup = false
  }
}
```

---

## Sätta variabelvärden

```bash
# 1. CLI-flag
terraform apply -var="environment=prod"
terraform apply -var="instance_type=t3.large" -var="region=eu-west-1"

# 2. Variabelfil
# terraform.tfvars (laddas automatiskt)
environment   = "prod"
instance_type = "t3.large"
region        = "eu-north-1"

# custom.tfvars (måste anges)
terraform apply -var-file="prod.tfvars"

# 3. Environment variables
export TF_VAR_environment="prod"
export TF_VAR_db_password="secret123"
terraform apply

# 4. Interaktivt (om saknas)
# Terraform frågar efter värden

# Prioritet (högst vinner):
# 1. -var och -var-file (sist vinner)
# 2. *.auto.tfvars (alfabetisk ordning)
# 3. terraform.tfvars
# 4. TF_VAR_ environment variables
# 5. Default i variable block
```

---

## Locals

```hcl
# locals.tf

locals {
  # Beräknade värden
  name_prefix = "${var.project}-${var.environment}"

  # Common tags för alla resurser
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = var.owner
  }

  # Conditional
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

  # Derived från andra locals
  full_name = "${local.name_prefix}-server"

  # Merged maps
  all_tags = merge(
    local.common_tags,
    var.extra_tags
  )
}

# Användning
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.instance_type

  tags = merge(local.all_tags, {
    Name = local.full_name
  })
}
```

---

## Outputs

```hcl
# outputs.tf

# Basic output
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP address"
  value       = aws_instance.web.public_ip
}

# Sensitive output
output "db_password" {
  description = "Database password"
  value       = random_password.db.result
  sensitive   = true
}

# Complex output
output "instance_info" {
  description = "Instance information"
  value = {
    id         = aws_instance.web.id
    public_ip  = aws_instance.web.public_ip
    private_ip = aws_instance.web.private_ip
    az         = aws_instance.web.availability_zone
  }
}

# Conditional output
output "load_balancer_dns" {
  description = "Load balancer DNS name"
  value       = var.enable_lb ? aws_lb.main[0].dns_name : null
}

# Lista av värden
output "instance_ips" {
  description = "IPs of all instances"
  value       = aws_instance.web[*].public_ip
}
```

---

## Använda outputs

```bash
# Visa outputs
terraform output                     # Alla outputs
terraform output instance_id         # Specifik output
terraform output -json               # JSON format
terraform output -raw public_ip      # Utan quotes

# I script
IP=$(terraform output -raw public_ip)
ssh ubuntu@$IP

# Sensitive outputs
terraform output db_password         # Visar: <sensitive>
terraform output -json db_password   # Visar värdet (JSON)
```

---

## Remote state data source

```hcl
# Läs outputs från annan Terraform-konfiguration

# networking/outputs.tf (i annat projekt)
output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnets" {
  value = aws_subnet.private[*].id
}

# application/main.tf (detta projekt)
data "terraform_remote_state" "network" {
  backend = "s3"

  config = {
    bucket = "my-terraform-state"
    key    = "networking/terraform.tfstate"
    region = "eu-north-1"
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  # Använd output från networking
  subnet_id = data.terraform_remote_state.network.outputs.private_subnets[0]
  vpc_security_group_ids = [
    data.terraform_remote_state.network.outputs.app_security_group_id
  ]
}
```

---

## Variable files per miljö

```bash
# Projektstruktur
+-- main.tf
+-- variables.tf
+-- outputs.tf
+-- terraform.tfvars          # Gemensamma defaults
+-- dev.tfvars                # Dev-miljö
+-- staging.tfvars            # Staging-miljö
+-- prod.tfvars               # Prod-miljö

# Kör för specifik miljö
terraform plan -var-file="prod.tfvars"
terraform apply -var-file="prod.tfvars"

# Eller använd workspaces + auto.tfvars
+-- terraform.tfvars
+-- dev.auto.tfvars           # Laddas i dev workspace
+-- prod.auto.tfvars          # Laddas i prod workspace
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Variables | Input med type, default, validation, sensitive |
| Locals | Beraknade varden som ateranvands i config |
| Outputs | Exporterade varden efter apply |
| .tfvars | Variabelvarden per miljo (dev.tfvars, prod.tfvars) |
| Remote state | Data source for cross-project referens |

## Kom ihag

- sensitive = true doljer varden i logs OCH plan output
- TF_VAR_namn satter variabel via environment
- validation block validerar input innan apply
- terraform output -json for att hamta sensitive varden
- Separata .tfvars per miljo ar best practice
""",
        },
        {
            "title": "Resource Dependencies",
            "slug": "resource-dependencies",
            "difficulty": "intermediate",
            "content": """
# Resource Dependencies

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan beroendeforstaelse | Konsekvens |
|--------------------------------|------------|
| Fel skapningsordning | EC2 fore subnet = krasch |
| Osynliga beroenden | Uppdateringar gar sonder |
| Cykler i dependencies | Terraform kan inte planera |
| Race conditions | Timing-fel vid parallel skapning |

Infrastruktur har beroenden - EC2 behover VPC, Lambda behover IAM Role. Terraform bygger automatiskt en dependency graph och skapar i ratt ordning. Men ibland behover du explicit kontroll.

+-------------+
|     VPC     |
+------+------+
       |
       ▼
+-------------+
|   Subnet    |
+------+------+
       |
       ▼
+-------------+     +-------------+
|  Instance   |----▶| Sec Group   |
+-------------+     +-------------+

------------------------------------------------------------

Terraform analyserar beroenden:

1. **Implicit** - Via referens (automatiskt)
2. **Explicit** - Via `depends_on`

Resurser skapas parallellt när möjligt.

---

## Implicita beroenden

```hcl
# Terraform förstår ordningen automatiskt

# 1. VPC skapas först (ingen referens till annat)
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# 2. Subnet skapas efter VPC (refererar aws_vpc.main.id)
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id       # Implicit dependency
  cidr_block = "10.0.1.0/24"
}

# 3. Security Group efter VPC
resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id           # Implicit dependency
  name   = "web-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 4. Instance efter Subnet och SG
resource "aws_instance" "web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id    # Implicit
  vpc_security_group_ids = [aws_security_group.web.id]  # Implicit
}

# Terraform-plan visar ordningen:
# aws_vpc.main
# aws_subnet.public (depends on aws_vpc.main)
# aws_security_group.web (depends on aws_vpc.main)
# aws_instance.web (depends on aws_subnet.public, aws_security_group.web)
```

---

## Explicita beroenden med depends_on

```hcl
# När implicita beroenden inte räcker

# S3 bucket
resource "aws_s3_bucket" "logs" {
  bucket = "my-app-logs"
}

# IAM policy som ger tillgång till bucket
resource "aws_iam_policy" "s3_access" {
  name = "s3-logs-access"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:*"]
        Resource = "${aws_s3_bucket.logs.arn}/*"
      }
    ]
  })
}

# Application - behöver bucket och policy först
# Men refererar inte till dem direkt
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  # Ingen direkt referens till S3 eller policy
  # Men vi VET att appen behöver dem

  depends_on = [
    aws_s3_bucket.logs,
    aws_iam_policy.s3_access
  ]

  user_data = <<-EOF
    #!/bin/bash
    # App konfigureras med bucket-namn via annan metod
    aws s3 ls s3://my-app-logs/
  EOF
}

# Vanliga fall för depends_on:
# - IAM policies måste finnas innan resurser som använder dem
# - Null resources som kör scripts
# - Cross-module dependencies
```

---

## Lifecycle och create_before_destroy

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    # Skapa ny innan gammal tas bort (zero downtime)
    create_before_destroy = true

    # Ignorera ändringar i specifika attribut
    ignore_changes = [
      tags["LastUpdated"],
      user_data
    ]

    # Förhindra förstörelse
    prevent_destroy = true

    # Ersätt vid ändring av dessa
    replace_triggered_by = [
      aws_security_group.web.id
    ]
  }
}
```

---

## Grafera beroenden

```bash
# Generera dependency graph
terraform graph | dot -Tpng > graph.png

# Eller i SVG
terraform graph | dot -Tsvg > graph.svg

# Visa i terminal (för enkla cases)
terraform graph

# Installera graphviz om det saknas
brew install graphviz                # macOS
apt install graphviz                 # Ubuntu
```

---

## Circular dependencies

```hcl
# FELAKTIGT - Circular dependency
resource "aws_security_group" "a" {
  name = "sg-a"

  ingress {
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [aws_security_group.b.id]  # Refererar till B
  }
}

resource "aws_security_group" "b" {
  name = "sg-b"

  ingress {
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    security_groups = [aws_security_group.a.id]  # Refererar till A
  }
}
# Error: Cycle detected

# LÖSNING - Separata regler
resource "aws_security_group" "a" {
  name = "sg-a"
}

resource "aws_security_group" "b" {
  name = "sg-b"
}

resource "aws_security_group_rule" "a_from_b" {
  type                     = "ingress"
  from_port                = 80
  to_port                  = 80
  protocol                 = "tcp"
  security_group_id        = aws_security_group.a.id
  source_security_group_id = aws_security_group.b.id
}

resource "aws_security_group_rule" "b_from_a" {
  type                     = "ingress"
  from_port                = 443
  to_port                  = 443
  protocol                 = "tcp"
  security_group_id        = aws_security_group.b.id
  source_security_group_id = aws_security_group.a.id
}
```

---

## Timing och timeouts

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  timeouts {
    create = "30m"                   # Max tid för create
    update = "20m"                   # Max tid för update
    delete = "15m"                   # Max tid för delete
  }
}

resource "aws_db_instance" "main" {
  identifier     = "mydb"
  engine         = "postgres"
  instance_class = "db.t3.micro"

  timeouts {
    create = "60m"                   # RDS tar lång tid
    delete = "30m"
  }
}
```

---

## Provisioners och beroenden

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  # Provisioner körs efter resursen skapats
  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }

  # Provisioner vid destroy
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance ${self.id} destroyed' >> destroyed.log"
  }

  # Fortsätt även om provisioner misslyckas
  provisioner "local-exec" {
    command    = "echo 'might fail'"
    on_failure = continue
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Implicita beroenden | Via referenser - Terraform bygger graph automatiskt |
| depends_on | Explicit beroende nar ingen referens finns |
| lifecycle | Kontrollerar create_before_destroy, prevent_destroy |
| Cirkulara beroenden | Undvik med separata resurser (ex: security_group_rule) |
| Timeouts | create, update, delete for langsamma operationer |

## Kom ihag

- Terraform bygger dependency graph automatiskt fran referenser
- depends_on ar sallan nodvandigt - anvand bara vid dolda beroenden
- create_before_destroy for zero-downtime updates
- prevent_destroy skyddar kritiska resurser fran oavsiktlig radering
- terraform graph visualiserar dependencies (output till Graphviz)
""",
        },
        {
            "title": "Modules",
            "slug": "terraform-modules",
            "difficulty": "intermediate",
            "content": """
# Terraform Modules

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan modules | Konsekvens |
|---------------------|------------|
| Duplicerad kod | Copy-paste for varje miljo och projekt |
| Inkonsistens | Staging ser inte ut som production |
| Svart att uppdatera | Andra pa 10 stallen istallet for 1 |
| Ingen standardisering | Varje team gor olika |

Modules ar Terraforms funktion for kod-atervanvandning. Skapa en VPC-modul en gang, anvand den i alla projekt. Community modules sparar hundratals timmar.

+---------------------------------------------------------+
|                  MODULE ECOSYSTEM                        |
+---------------------------------------------------------+
|  Root Module          Child Modules         Registry    |
|  +----------+         +----------+         +---------+ |
|  | main.tf  | ------▶ | modules/ | ------▶ | Public  | |
|  | (caller) |         |  vpc/    |         | modules | |
|  +----------+         |  ec2/    |         +---------+ |
|                       |  rds/    |                      |
|                       +----------+                      |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Module-struktur

```bash
# Standard module-layout
modules/
+-- vpc/
    +-- main.tf              # Resurser
    +-- variables.tf         # Input variables
    +-- outputs.tf           # Output values
    +-- versions.tf          # Provider requirements
    +-- README.md            # Dokumentation

# Användning
.
+-- main.tf                  # Anropar modules
+-- variables.tf
+-- outputs.tf
+-- modules/
    +-- vpc/
    +-- ec2/
    +-- rds/
```

---

## Skapa en module

```hcl
# modules/vpc/variables.tf
variable "name" {
  description = "Name prefix for resources"
  type        = string
}

variable "cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "azs" {
  description = "Availability zones"
  type        = list(string)
}

variable "public_subnets" {
  description = "Public subnet CIDRs"
  type        = list(string)
  default     = []
}

variable "private_subnets" {
  description = "Private subnet CIDRs"
  type        = list(string)
  default     = []
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
```

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block           = var.cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(var.tags, {
    Name = "${var.name}-vpc"
  })
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = merge(var.tags, {
    Name = "${var.name}-igw"
  })
}

resource "aws_subnet" "public" {
  count = length(var.public_subnets)

  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnets[count.index]
  availability_zone       = var.azs[count.index]
  map_public_ip_on_launch = true

  tags = merge(var.tags, {
    Name = "${var.name}-public-${count.index + 1}"
    Type = "public"
  })
}

resource "aws_subnet" "private" {
  count = length(var.private_subnets)

  vpc_id            = aws_vpc.this.id
  cidr_block        = var.private_subnets[count.index]
  availability_zone = var.azs[count.index]

  tags = merge(var.tags, {
    Name = "${var.name}-private-${count.index + 1}"
    Type = "private"
  })
}
```

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.this.id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.this.cidr_block
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "igw_id" {
  description = "Internet Gateway ID"
  value       = aws_internet_gateway.this.id
}
```

---

## Använda modules

```hcl
# main.tf - Root module
module "vpc" {
  source = "./modules/vpc"          # Lokal path

  name = "myapp"
  cidr = "10.0.0.0/16"
  azs  = ["eu-north-1a", "eu-north-1b", "eu-north-1c"]

  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnets = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]

  tags = {
    Environment = "prod"
    Project     = "myapp"
  }
}

# Referera module outputs
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = module.vpc.public_subnet_ids[0]
}

output "vpc_id" {
  value = module.vpc.vpc_id
}
```

---

## Module sources

```hcl
# Lokal path
module "vpc" {
  source = "./modules/vpc"
}

# Terraform Registry
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  # Module-specifika inputs
  name = "my-vpc"
  cidr = "10.0.0.0/16"
}

# GitHub
module "vpc" {
  source = "github.com/terraform-aws-modules/terraform-aws-vpc"
}

# GitHub med tag
module "vpc" {
  source = "github.com/terraform-aws-modules/terraform-aws-vpc?ref=v5.0.0"
}

# S3
module "vpc" {
  source = "s3::https://s3-eu-north-1.amazonaws.com/bucket/modules/vpc.zip"
}

# Private registry
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = "1.0.0"
}
```

---

## Module versioning

```hcl
# Rekommenderat för published modules
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"                  # Exakt version
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"                 # >= 5.0.0, < 6.0.0
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = ">= 5.0, < 6.0"          # Range
}
```

```bash
# Uppgradera modules
terraform init -upgrade              # Uppdatera till nyaste inom constraint
```

---

## Populära registry modules

```hcl
# AWS VPC
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-north-1a", "eu-north-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true
}

# AWS EKS
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.0.0"

  cluster_name    = "my-cluster"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.medium"]
      min_size       = 1
      max_size       = 3
      desired_size   = 2
    }
  }
}

# AWS RDS
module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = "6.0.0"

  identifier = "mydb"
  engine     = "postgres"

  instance_class    = "db.t3.micro"
  allocated_storage = 20

  db_name  = "myapp"
  username = "admin"
  password = var.db_password

  vpc_security_group_ids = [module.vpc.default_security_group_id]
  subnet_ids             = module.vpc.database_subnets
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Module | Ateranvandbar Terraform-komponent med input/output |
| Standard-struktur | main.tf, variables.tf, outputs.tf, versions.tf |
| Source | Lokal path, GitHub, Registry, S3 - alla fungerar |
| Versioning | ALLTID version-locka published modules |
| Registry | 3000+ fardiga modules sparar hundratals timmar |

## Kom ihag

- terraform init laddar ner modules fran source
- module.namn.output_namn refererar till module outputs
- Lokala modules: source = "./modules/vpc"
- GitHub modules: source = "github.com/org/repo?ref=v1.0"
- terraform init -upgrade uppdaterar modules
""",
        },
        {
            "title": "Count & For Each",
            "slug": "count-and-for-each",
            "difficulty": "intermediate",
            "content": """
# Count & For Each

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan iteration | Konsekvens |
|-----------------------|------------|
| Manuell duplicering | Copy-paste for varje instans |
| Hardkodade antal | Maste andra kod for att skala |
| Svart att underhalla | 20 likadana resurser att updatera |
| Ingen dynamik | Kan inte anpassa per item |

count och for_each skapar multipla resurser dynamiskt. Istallet for 10 resource-blocks, ett block med count = 10. for_each ar generellt battre - stabilare vid andringar.

+---------------------------------------------------------+
|              COUNT vs FOR_EACH                           |
+---------------------------------------------------------+
|  count = 3                    for_each = toset([...])   |
|  +-------------------+        +-------------------+     |
|  | resource[0]       |        | resource["a"]     |     |
|  | resource[1]       |        | resource["b"]     |     |
|  | resource[2]       |        | resource["c"]     |     |
|  +-------------------+        +-------------------+     |
|  Index-baserat (fragilt)      Nyckel-baserat (stabilt)  |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Count basics

```hcl
# Skapa 3 identiska instanser
resource "aws_instance" "web" {
  count = 3

  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"      # web-0, web-1, web-2
  }
}

# Referera till specifik instans
output "first_instance_id" {
  value = aws_instance.web[0].id
}

# Referera till alla
output "all_instance_ids" {
  value = aws_instance.web[*].id     # Splat syntax
}
```

---

## Count med variabler

```hcl
variable "instance_count" {
  type    = number
  default = 3
}

variable "availability_zones" {
  type    = list(string)
  default = ["eu-north-1a", "eu-north-1b", "eu-north-1c"]
}

resource "aws_instance" "web" {
  count = var.instance_count

  ami               = data.aws_ami.ubuntu.id
  instance_type     = "t3.micro"
  availability_zone = var.availability_zones[count.index % length(var.availability_zones)]

  tags = {
    Name = "web-${count.index}"
  }
}
```

---

## Conditional med count

```hcl
variable "create_bastion" {
  type    = bool
  default = false
}

# Skapa bara om variabeln är true
resource "aws_instance" "bastion" {
  count = var.create_bastion ? 1 : 0

  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = { Name = "bastion" }
}

# Referera conditional resource
output "bastion_ip" {
  value = var.create_bastion ? aws_instance.bastion[0].public_ip : null
}

# Eller med try()
output "bastion_ip_safe" {
  value = try(aws_instance.bastion[0].public_ip, null)
}
```

---

## For_each med set

```hcl
variable "instance_names" {
  type    = set(string)
  default = ["web", "api", "worker"]
}

resource "aws_instance" "server" {
  for_each = var.instance_names

  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = each.key                  # "web", "api", "worker"
    # each.value = same as each.key for sets
  }
}

# Referera
output "web_instance_id" {
  value = aws_instance.server["web"].id
}

output "all_instance_ids" {
  value = { for k, v in aws_instance.server : k => v.id }
}
```

---

## For_each med map

```hcl
variable "instances" {
  type = map(object({
    instance_type = string
    disk_size     = number
  }))
  default = {
    web = {
      instance_type = "t3.micro"
      disk_size     = 20
    }
    api = {
      instance_type = "t3.small"
      disk_size     = 50
    }
    worker = {
      instance_type = "t3.medium"
      disk_size     = 100
    }
  }
}

resource "aws_instance" "server" {
  for_each = var.instances

  ami           = data.aws_ami.ubuntu.id
  instance_type = each.value.instance_type

  root_block_device {
    volume_size = each.value.disk_size
  }

  tags = {
    Name = each.key
  }
}
```

---

## For expressions

```hcl
# Transform lista
locals {
  # Lista av strings till uppercase
  names = ["alice", "bob", "charlie"]
  upper_names = [for name in local.names : upper(name)]
  # ["ALICE", "BOB", "CHARLIE"]

  # Filtrera
  short_names = [for name in local.names : name if length(name) < 5]
  # ["bob"]

  # Till map
  name_map = { for name in local.names : name => upper(name) }
  # {alice = "ALICE", bob = "BOB", charlie = "CHARLIE"}
}

# Med resurser
output "instance_ips" {
  value = { for k, instance in aws_instance.server : k => instance.public_ip }
  # {web = "1.2.3.4", api = "5.6.7.8", worker = "9.10.11.12"}
}

# Nested for
locals {
  users = ["alice", "bob"]
  roles = ["admin", "user"]

  user_roles = [
    for user in local.users : [
      for role in local.roles : {
        user = user
        role = role
      }
    ]
  ]
  # Flatten
  user_roles_flat = flatten(local.user_roles)
}
```

---

## Count vs for_each

```hcl
# COUNT: Problem vid borttagning
resource "aws_instance" "web" {
  count = 3
  # ...
}
# Resurser: [0], [1], [2]
# Om du tar bort [1] -> [2] blir [1] -> onödig re-create

# FOR_EACH: Stabilt vid ändringar
resource "aws_instance" "web" {
  for_each = toset(["web1", "web2", "web3"])
  # ...
}
# Resurser: ["web1"], ["web2"], ["web3"]
# Ta bort "web2" -> bara den tas bort

# REKOMMENDATION:
# - count: För identiska resurser, conditional create
# - for_each: För unika resurser, stabila identifierare
```

---

## Dynamic blocks

```hcl
variable "ingress_rules" {
  type = list(object({
    port        = number
    cidr_blocks = list(string)
  }))
  default = [
    { port = 80, cidr_blocks = ["0.0.0.0/0"] },
    { port = 443, cidr_blocks = ["0.0.0.0/0"] },
    { port = 22, cidr_blocks = ["10.0.0.0/8"] }
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| count | For antal kopior - index-baserat (fragilt) |
| for_each | For unika resurser - nyckel-baserat (stabilt) |
| each.key/value | Accessor i for_each iteration |
| dynamic blocks | For nested iteration i resource blocks |
| for expressions | List/map transformation i locals |

## Kom ihag

- for_each ar nastan alltid battre an count - stabilare
- count = 0 for conditional resource creation
- toset() konverterar lista till set for for_each
- flatten() for att platta ut nested lists
- dynamic blocks for variabelt antal ingress/egress rules
""",
        },
        {
            "title": "Data Sources",
            "slug": "data-sources",
            "difficulty": "intermediate",
            "content": """
# Data Sources

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan data sources | Konsekvens |
|--------------------------|------------|
| Hardkodade AMI IDs | Gammal AMI, sakerhetsproblem |
| Manuell lookup | Kolla console, kopiera, klistra |
| Ingen dynamik | Availability zones, account ID |
| Isolerade projekt | Kan inte lasa fran annat state |

Data sources laser existerande infrastruktur och extern data. Du hardkodar inte AMI IDs - du laser senaste Ubuntu automatiskt. Du hardkodar inte AZs - du laser tillgangliga dynamiskt.

+---------------------------------------------------------+
|                   DATA SOURCES                           |
+---------------------------------------------------------+
|  data "aws_ami" { }       -> Senaste Ubuntu AMI         |
|  data "aws_vpc" { }       -> Existerande VPC            |
|  data "aws_caller_id" { } -> Account ID, ARN            |
|  data "aws_region" { }    -> Current region             |
|  data "terraform_remote_state" { } -> Annat projekt     |
+---------------------------------------------------------+

------------------------------------------------------------
- Account information

Data sources läser utan att skapa.

---

## Så fungerar det

Data sources:

1. Frågar provider's API
2. Returnerar attribut
3. Används i andra resurser

Läser vid plan och apply.

---

## Grundläggande data sources

```hcl
# Hitta senaste Ubuntu AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]     # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Använd AMI
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}

# Available AZs
data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_subnet" "public" {
  count             = length(data.aws_availability_zones.available.names)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}
```

---

## Account och region info

```hcl
# Aktuellt AWS-konto
data "aws_caller_identity" "current" {}

# Aktuell region
data "aws_region" "current" {}

# Partition (aws, aws-cn, aws-us-gov)
data "aws_partition" "current" {}

# Använd för ARN-konstruktion
locals {
  bucket_arn = "arn:${data.aws_partition.current.partition}:s3:::my-bucket"
  account_id = data.aws_caller_identity.current.account_id
  region     = data.aws_region.current.name
}

output "account_info" {
  value = {
    account_id = data.aws_caller_identity.current.account_id
    arn        = data.aws_caller_identity.current.arn
    user_id    = data.aws_caller_identity.current.user_id
  }
}
```

---

## Existerande resurser

```hcl
# Hitta VPC by tag
data "aws_vpc" "main" {
  filter {
    name   = "tag:Name"
    values = ["production-vpc"]
  }
}

# Hitta VPC by ID
data "aws_vpc" "specific" {
  id = "vpc-12345678"
}

# Hitta subnets i VPC
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.main.id]
  }

  filter {
    name   = "tag:Type"
    values = ["private"]
  }
}

# Hitta security group
data "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = data.aws_vpc.main.id
}

# Använd existerande resurser
resource "aws_instance" "app" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = data.aws_subnets.private.ids[0]
  vpc_security_group_ids = [data.aws_security_group.web.id]
}
```

---

## IAM data sources

```hcl
# Policy document (bättre än JSON-strängar)
data "aws_iam_policy_document" "s3_access" {
  statement {
    sid    = "AllowS3Access"
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject"
    ]

    resources = [
      "${aws_s3_bucket.data.arn}/*"
    ]
  }

  statement {
    sid    = "AllowBucketListing"
    effect = "Allow"

    actions = [
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.data.arn
    ]
  }
}

# Skapa policy med dokumentet
resource "aws_iam_policy" "s3_access" {
  name   = "s3-access-policy"
  policy = data.aws_iam_policy_document.s3_access.json
}

# Assume role policy
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

---

## Template files

```hcl
# user-data.sh.tpl
#!/bin/bash
echo "Hello from ${instance_name}"
echo "Environment: ${environment}"
echo "Region: ${region}"

apt update && apt install -y nginx

# Läs template
data "template_file" "user_data" {
  template = file("${path.module}/user-data.sh.tpl")

  vars = {
    instance_name = "web-server"
    environment   = var.environment
    region        = data.aws_region.current.name
  }
}

# Använd
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  user_data     = data.template_file.user_data.rendered
}

# MODERN ALTERNATIV: templatefile()
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  user_data = templatefile("${path.module}/user-data.sh.tpl", {
    instance_name = "web-server"
    environment   = var.environment
    region        = data.aws_region.current.name
  })
}
```

---

## Remote state data source

```hcl
# Läs outputs från annan Terraform-konfiguration
data "terraform_remote_state" "network" {
  backend = "s3"

  config = {
    bucket = "my-terraform-state"
    key    = "network/terraform.tfstate"
    region = "eu-north-1"
  }
}

# Använd outputs
resource "aws_instance" "app" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = data.terraform_remote_state.network.outputs.private_subnet_ids[0]
  vpc_security_group_ids = [data.terraform_remote_state.network.outputs.app_sg_id]
}
```

---

## External data source

```hcl
# Kör script och läs JSON-output
data "external" "git_info" {
  program = ["bash", "${path.module}/scripts/git-info.sh"]
}

# scripts/git-info.sh
#!/bin/bash
cat <<EOF
{
  "commit": "$(git rev-parse HEAD)",
  "branch": "$(git rev-parse --abbrev-ref HEAD)",
  "author": "$(git log -1 --format='%an')"
}
EOF

# Använd
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    GitCommit = data.external.git_info.result.commit
    GitBranch = data.external.git_info.result.branch
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Data sources | Laser utan att skapa - read-only |
| aws_ami | Hitta senaste image med filter dynamiskt |
| aws_iam_policy_document | Battre an JSON-strangar for policies |
| templatefile() | Dynamiska scripts med variabler |
| terraform_remote_state | Lasa outputs fran annat Terraform-projekt |

## Kom ihag

- most_recent = true for att fa senaste matchande AMI
- data "aws_caller_identity" {} ger account ID utan hardkodning
- data "aws_region" {} ger current region dynamiskt
- external data source kor scripts och laser JSON output
- Data sources uppdateras vid varje plan/apply
""",
        },
        {
            "title": "Functions & Expressions",
            "slug": "functions-and-expressions",
            "difficulty": "intermediate",
            "content": """
# Functions & Expressions

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan funktioner | Konsekvens |
|------------------------|------------|
| Manuella transformationer | Rakna ut subnet CIDR manuellt |
| Ingen dynamik | Hardkodade strangar overallt |
| Svart att lasa | Komplicerad logik i resources |
| Duplicerad logik | Samma berakning pa flera stallen |

Terraform har 100+ inbyggda funktioner for strangar, listor, maps, filer, natverk. Istallet for att hardkoda cidrsubnet(vpc_cidr, 8, 1), berakna den dynamiskt.

+---------------------------------------------------------+
|                  FUNCTION CATEGORIES                     |
+---------------------------------------------------------+
|  String   | upper, lower, format, split, join, regex   |
|  Numeric  | min, max, ceil, floor, abs, parseint       |
|  List     | length, element, concat, flatten, sort     |
|  Map      | lookup, keys, values, merge, zipmap        |
|  File     | file, templatefile, filebase64             |
|  Network  | cidrsubnet, cidrhost, cidrnetmask          |
|  Encoding | base64encode, jsonencode, yamlencode       |
|  Hash     | md5, sha256, uuid                          |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Strängfunktioner

```hcl
locals {
  # Case
  upper_name = upper("hello")          # "HELLO"
  lower_name = lower("HELLO")          # "hello"
  title_name = title("hello world")    # "Hello World"

  # Trim
  trimmed = trim("  hello  ", " ")     # "hello"
  trimprefix = trimprefix("helloworld", "hello")  # "world"
  trimsuffix = trimsuffix("helloworld", "world")  # "hello"

  # Replace
  replaced = replace("hello-world", "-", "_")  # "hello_world"

  # Split & Join
  parts = split(",", "a,b,c")          # ["a", "b", "c"]
  joined = join("-", ["a", "b", "c"])  # "a-b-c"

  # Substring
  sub = substr("hello", 0, 3)          # "hel"

  # Format
  formatted = format("Hello, %s!", "World")  # "Hello, World!"
  padded = format("%05d", 42)          # "00042"

  # Regex
  matched = regex("[a-z]+", "hello123")  # "hello"
  all_matches = regexall("[0-9]+", "a1b2c3")  # ["1", "2", "3"]

  # Contains
  has_dev = strcontains("dev-server", "dev")  # true
}
```

---

## Numeriska funktioner

```hcl
locals {
  # Avrundning
  ceil_val = ceil(1.5)                 # 2
  floor_val = floor(1.5)               # 1
  round_val = round(1.5)               # 2

  # Min/Max
  minimum = min(1, 2, 3)               # 1
  maximum = max(1, 2, 3)               # 3

  # Absolute
  absolute = abs(-5)                   # 5

  # Power & Log
  power = pow(2, 3)                    # 8
  log_val = log(100, 10)               # 2

  # Signum
  sign = signum(-5)                    # -1

  # Parse nummer från sträng
  number = parseint("42", 10)          # 42
}
```

---

## Collection-funktioner

```hcl
locals {
  list = ["a", "b", "c"]
  map = { a = 1, b = 2, c = 3 }

  # Length
  list_len = length(local.list)        # 3
  map_len = length(local.map)          # 3

  # Element access
  first = element(local.list, 0)       # "a"
  last = element(local.list, -1)       # "c" (wrap-around)

  # Lookup med default
  value = lookup(local.map, "d", 0)    # 0 (default)

  # Contains
  has_a = contains(local.list, "a")    # true

  # Index
  idx = index(local.list, "b")         # 1

  # Keys & Values
  keys = keys(local.map)               # ["a", "b", "c"]
  values = values(local.map)           # [1, 2, 3]

  # Merge
  merged = merge(
    { a = 1 },
    { b = 2 },
    { a = 3 }                          # Överskriver a
  )  # { a = 3, b = 2 }

  # Concat
  combined = concat(
    ["a", "b"],
    ["c", "d"]
  )  # ["a", "b", "c", "d"]

  # Flatten
  nested = [["a", "b"], ["c", "d"]]
  flat = flatten(local.nested)         # ["a", "b", "c", "d"]

  # Distinct
  unique = distinct(["a", "b", "a"])   # ["a", "b"]

  # Sort
  sorted = sort(["c", "a", "b"])       # ["a", "b", "c"]

  # Reverse
  reversed = reverse(["a", "b", "c"])  # ["c", "b", "a"]

  # Slice
  sliced = slice(["a", "b", "c", "d"], 1, 3)  # ["b", "c"]

  # Coalesce (första non-null)
  first_valid = coalesce(null, "", "hello")  # ""

  # Compact (ta bort tomma strängar)
  compacted = compact(["a", "", "b", ""])  # ["a", "b"]

  # Zipmap
  zipped = zipmap(
    ["a", "b", "c"],
    [1, 2, 3]
  )  # { a = 1, b = 2, c = 3 }
}
```

---

## Type-funktioner

```hcl
locals {
  # Konvertera typer
  to_string = tostring(123)            # "123"
  to_number = tonumber("42")           # 42
  to_bool = tobool("true")             # true

  # Collection-typer
  to_list = tolist(toset(["a", "b", "a"]))  # ["a", "b"]
  to_set = toset(["a", "b", "a"])      # Set med "a", "b"
  to_map = tomap({ a = 1 })            # Map

  # Try (undvik fel)
  safe_value = try(var.config.nested.value, "default")

  # Can (kontrollera om uttryck är giltigt)
  is_valid = can(regex("^[a-z]+$", var.name))

  # Type check
  type_of = type(123)                  # number
}
```

---

## Fil-funktioner

```hcl
locals {
  # Läs fil
  content = file("${path.module}/config.txt")

  # Läs JSON
  config = jsondecode(file("${path.module}/config.json"))

  # Läs YAML (Terraform 0.12+)
  yaml_config = yamldecode(file("${path.module}/config.yaml"))

  # Base64
  encoded = base64encode("hello")      # "aGVsbG8="
  decoded = base64decode("aGVsbG8=")   # "hello"

  # Gzip
  compressed = base64gzip("hello")

  # Template
  rendered = templatefile("${path.module}/template.tpl", {
    name = "world"
  })

  # File exists
  exists = fileexists("${path.module}/optional.txt")

  # Fileset (glob)
  configs = fileset(path.module, "configs/*.json")
}

# Läs alla config-filer
locals {
  all_configs = {
    for f in local.configs :
    trimsuffix(basename(f), ".json") => jsondecode(file("${path.module}/${f}"))
  }
}
```

---

## IP-funktioner

```hcl
locals {
  # CIDR subnät
  subnets = cidrsubnets("10.0.0.0/16", 8, 8, 8)
  # ["10.0.0.0/24", "10.0.1.0/24", "10.0.2.0/24"]

  # Specifikt subnät
  subnet_1 = cidrsubnet("10.0.0.0/16", 8, 0)   # "10.0.0.0/24"
  subnet_2 = cidrsubnet("10.0.0.0/16", 8, 1)   # "10.0.1.0/24"

  # CIDR host
  host = cidrhost("10.0.0.0/24", 5)    # "10.0.0.5"

  # Netmask
  mask = cidrnetmask("10.0.0.0/16")    # "255.255.0.0"
}

# Dynamiska subnets
variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "az_count" {
  default = 3
}

locals {
  public_cidrs = [
    for i in range(var.az_count) :
    cidrsubnet(var.vpc_cidr, 8, i)
  ]

  private_cidrs = [
    for i in range(var.az_count) :
    cidrsubnet(var.vpc_cidr, 8, i + 100)
  ]
}
```

---

## Praktiska exempel

```hcl
# Generera unika namn
locals {
  unique_name = "${var.project}-${var.environment}-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}

# Tagga alla resurser konsekvent
locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
    CreatedAt   = timestamp()
  }
}

# Conditional resource creation
locals {
  create_nat = var.environment == "prod" ? true : false
  nat_count  = local.create_nat ? length(var.availability_zones) : 0
}

# Lookup instance type per environment
variable "instance_types" {
  type = map(string)
  default = {
    dev     = "t3.micro"
    staging = "t3.small"
    prod    = "t3.large"
  }
}

locals {
  instance_type = lookup(var.instance_types, var.environment, "t3.micro")
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| terraform console | REPL for att testa funktioner interaktivt |
| merge() | Kombinera maps, senare varden overskriver |
| try() | Saker access till nested values utan fel |
| cidrsubnet() | Dynamiska IP-berakningar fran VPC CIDR |
| templatefile() | Dynamiska konfigurationsfiler med variabler |

## Kom ihag

- lookup(map, key, default) for saker map-access
- coalesce() returnerar forsta icke-null varde
- flatten() plattar ut nested lists
- jsonencode()/yamlencode() for strukturerad output
- regex() matchar monster, regexall() ger alla matchningar
""",
        },
        {
            "title": "Terraform Workspaces",
            "slug": "terraform-workspaces",
            "difficulty": "intermediate",
            "content": """
# Terraform Workspaces

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan miljoseparation | Konsekvens |
|-----------------------------|------------|
| Samma state for alla miljor | Dev-andringar paverkar prod |
| Manuell kopiering | Copy-paste mellan miljoer |
| Ingen isolering | En miss tar ner allt |
| Svar att testa | Kan inte testa infra-andringar sakert |

Workspaces ger separata state-filer for samma kod. Dev, staging, prod - samma Terraform, olika infrastruktur. Alternativet ar katalogstruktur med separata mappar.

+---------------------------------------------------------+
|              WORKSPACE vs DIRECTORY                      |
+---------------------------------------------------------+
|  Workspaces:              Directory Structure:          |
|  +--------------+         +--------------+             |
|  | Same .tf     |         | environments/|             |
|  | files        |         |   dev/       |             |
|  |              |         |   staging/   |             |
|  | Different    |         |   prod/      |             |
|  | state files  |         | modules/     |             |
|  +--------------+         +--------------+             |
|  Enkelt, samma kod        Explicit, full kontroll      |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Workspace-kommandon

```bash
# Lista workspaces
terraform workspace list
# * default
#   staging
#   production

# Skapa ny workspace
terraform workspace new staging
# Created and switched to workspace "staging"!

# Byt workspace
terraform workspace select production
# Switched to workspace "production".

# Visa aktiv workspace
terraform workspace show
# production

# Ta bort workspace (måste vara tom)
terraform workspace delete staging
```

---

## Använda workspace i kod

```hcl
# Referera till aktuell workspace
locals {
  environment = terraform.workspace

  # Olika config per workspace
  instance_type = {
    default    = "t3.micro"
    staging    = "t3.small"
    production = "t3.large"
  }

  instance_count = {
    default    = 1
    staging    = 2
    production = 3
  }
}

resource "aws_instance" "web" {
  count = local.instance_count[terraform.workspace]

  ami           = data.aws_ami.ubuntu.id
  instance_type = local.instance_type[terraform.workspace]

  tags = {
    Name        = "web-${terraform.workspace}-${count.index}"
    Environment = terraform.workspace
  }
}
```

---

## Workspace state

```hcl
# S3 backend med workspaces
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "app/terraform.tfstate"
    region = "eu-north-1"
  }
}

# State-filer blir:
# s3://my-terraform-state/env:/default/app/terraform.tfstate
# s3://my-terraform-state/env:/staging/app/terraform.tfstate
# s3://my-terraform-state/env:/production/app/terraform.tfstate
```

---

## Directory structure alternativ

```bash
# Rekommenderas för större projekt
.
+-- modules/                    # Återanvändbara modules
|   +-- vpc/
|   +-- ec2/
|   +-- rds/
|
+-- environments/
|   +-- dev/
|   |   +-- main.tf
|   |   +-- variables.tf
|   |   +-- terraform.tfvars
|   |   +-- backend.tf
|   |
|   +-- staging/
|   |   +-- main.tf
|   |   +-- variables.tf
|   |   +-- terraform.tfvars
|   |   +-- backend.tf
|   |
|   +-- prod/
|       +-- main.tf
|       +-- variables.tf
|       +-- terraform.tfvars
|       +-- backend.tf
```

```hcl
# environments/prod/main.tf
module "vpc" {
  source = "../../modules/vpc"

  name = "prod"
  cidr = "10.0.0.0/16"
}

# environments/prod/backend.tf
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"  # Unik key per miljö
    region = "eu-north-1"
  }
}

# environments/prod/terraform.tfvars
environment    = "prod"
instance_type  = "t3.large"
instance_count = 3
```

---

## Workspace vs Directory

```
Workspaces                      | Directory Structure
--------------------------------|--------------------------------
En kodbas                       | Kod per miljö (eller shared)
Snabbt att byta                 | Explicit separation
Risk för fel workspace          | Tydligare
Samma backend config            | Olika backend per miljö
Bra för liknande miljöer        | Bra för olika miljöer
Svårare code review             | Enklare code review
```

---

## Workspace best practices

```hcl
# Validera workspace
locals {
  valid_workspaces = ["default", "dev", "staging", "prod"]
}

resource "null_resource" "validate_workspace" {
  count = contains(local.valid_workspaces, terraform.workspace) ? 0 : 1

  provisioner "local-exec" {
    command = "echo 'Invalid workspace: ${terraform.workspace}' && exit 1"
  }
}

# Skydda prod
resource "aws_instance" "web" {
  # Förhindra destroy i prod
  lifecycle {
    prevent_destroy = terraform.workspace == "prod"
  }
}

# Olika providers per workspace
provider "aws" {
  region = terraform.workspace == "prod" ? "eu-north-1" : "eu-west-1"

  assume_role {
    role_arn = "arn:aws:iam::${local.account_ids[terraform.workspace]}:role/TerraformRole"
  }
}

locals {
  account_ids = {
    default = "111111111111"
    staging = "222222222222"
    prod    = "333333333333"
  }
}
```

---

## CI/CD med workspaces

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  push:
    branches: [main, staging]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        workspace: [staging, prod]

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init

      - name: Select Workspace
        run: terraform workspace select ${{ matrix.workspace }} || terraform workspace new ${{ matrix.workspace }}

      - name: Terraform Plan
        run: terraform plan -out=tfplan

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && matrix.workspace == 'prod'
        run: terraform apply -auto-approve tfplan
```

---

## Terragrunt för multi-environment

```hcl
# terragrunt.hcl (i environment-katalog)
# Terragrunt = wrapper som förenklar multi-environment

include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "../../modules/app"
}

inputs = {
  environment    = "prod"
  instance_type  = "t3.large"
  instance_count = 3
}

# root terragrunt.hcl
remote_state {
  backend = "s3"
  config = {
    bucket = "my-terraform-state"
    key    = "${path_relative_to_include()}/terraform.tfstate"
    region = "eu-north-1"
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Workspaces | Samma kod, olika state-filer |
| Directory structure | Separata mappar per miljo - explicit |
| terraform.workspace | Inbyggd variabel for aktuell workspace |
| Workspaces bast for | Liknande miljoer (dev, staging) |
| Directory bast for | Prod vs non-prod med olika config |

## Kom ihag

- terraform workspace select NAMN byter aktivt workspace
- terraform workspace new NAMN skapar nytt workspace
- terraform.workspace ger aktuellt workspace-namn i kod
- Workspaces andrar state path automatiskt
- Terragrunt forenklar multi-environment ytterligare
""",
        },
        {
            "title": "Import & Migration",
            "slug": "import-and-migration",
            "difficulty": "intermediate",
            "content": """
# Import & Migration

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan import/migration | Konsekvens |
|------------------------------|------------|
| Existerande infra utan IaC | Terraform ser inte manuellt skapad infra |
| Refaktorering | Rename = destroy + create = downtime |
| State korruption | Manuell recovery utan state manipulation |
| Modul-uppdelning | Kan inte flytta resurser mellan states |

Import tar in existerande infrastruktur i Terraform state. State manipulation (mv, rm) mojliggor refaktorering utan att destroya resurser. Kritiskt for migrering till IaC.

+---------------------------------------------------------+
|                   IMPORT WORKFLOW                        |
+---------------------------------------------------------+
|  1. Skriv resource block i .tf          (tom kropp)    |
|  2. terraform import <address> <id>     (populerar)    |
|  3. terraform plan                      (diff)         |
|  4. Justera .tf for att matcha          (no changes)   |
|  5. terraform apply                     (verify)       |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Importera resurser

```bash
# Syntax: terraform import <address> <id>

# EC2 instance
terraform import aws_instance.web i-1234567890abcdef0

# S3 bucket
terraform import aws_s3_bucket.data my-bucket-name

# Security Group
terraform import aws_security_group.web sg-12345678

# IAM Role
terraform import aws_iam_role.app my-role-name

# RDS
terraform import aws_db_instance.main my-db-identifier

# VPC
terraform import aws_vpc.main vpc-12345678

# Subnet
terraform import aws_subnet.public subnet-12345678
```

---

## Import workflow

```hcl
# Steg 1: Skapa tom resurs-definition
resource "aws_instance" "web" {
  # Kommer fyllas i
}
```

```bash
# Steg 2: Importera
terraform import aws_instance.web i-1234567890abcdef0

# Steg 3: Visa importerad state
terraform state show aws_instance.web
```

```hcl
# Steg 4: Fyll i konfigurationen
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
  subnet_id     = "subnet-12345678"

  vpc_security_group_ids = [
    "sg-12345678"
  ]

  tags = {
    Name = "web-server"
  }
}
```

```bash
# Steg 5: Verifiera (ingen ändring)
terraform plan
# No changes. Infrastructure is up-to-date.
```

---

## Import block (Terraform 1.5+)

```hcl
# Nyare syntax - deklarativ import
import {
  to = aws_instance.web
  id = "i-1234567890abcdef0"
}

resource "aws_instance" "web" {
  # Konfiguration
}

# Kör import
terraform plan -generate-config-out=generated.tf
# Genererar konfiguration automatiskt!

terraform apply
# Importerar resurserna
```

---

## Generera config från import

```bash
# Terraform 1.5+ kan generera config

# Steg 1: Definiera import blocks
cat > imports.tf << 'EOF'
import {
  to = aws_instance.web
  id = "i-1234567890abcdef0"
}

import {
  to = aws_security_group.web
  id = "sg-12345678"
}
EOF

# Steg 2: Generera config
terraform plan -generate-config-out=generated.tf

# Steg 3: Granska generated.tf och flytta till main.tf

# Steg 4: Applicera
terraform apply
```

---

## State-manipulation

```bash
# Lista resurser
terraform state list
# aws_instance.web
# aws_security_group.web
# aws_vpc.main

# Visa resurs
terraform state show aws_instance.web

# Flytta/rename resurs
terraform state mv aws_instance.web aws_instance.webserver
# OBS: Uppdatera .tf-filen också!

# Flytta till module
terraform state mv aws_instance.web module.compute.aws_instance.web

# Ta bort från state (resursen finns kvar i AWS)
terraform state rm aws_instance.legacy
# Användbart när resurs ska hanteras utanför Terraform

# Pull state (för backup/debugging)
terraform state pull > state_backup.json

# Push state (FARLIGT!)
terraform state push state_backup.json
```

---

## Migrera mellan states

```bash
# Scenario: Flytta resurs mellan projekt

# Projekt A: Ta bort från state
cd project-a
terraform state rm aws_s3_bucket.shared

# Projekt B: Importera
cd ../project-b
terraform import aws_s3_bucket.shared my-bucket-name
```

---

## Refaktorera utan downtime

```hcl
# FÖRE: En stor fil
resource "aws_instance" "web" {
  # ...
}

# EFTER: Flytta till module
module "web" {
  source = "./modules/web"
}
```

```bash
# Steg 1: Skapa module med samma konfiguration

# Steg 2: Flytta state
terraform state mv aws_instance.web module.web.aws_instance.this

# Steg 3: Plan (bör visa inga ändringar)
terraform plan

# Steg 4: Ta bort gamla resursen från root (redan i module)
```

---

## Migrera backend

```bash
# Från local till S3

# 1. Lägg till backend config
cat >> backend.tf << 'EOF'
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "app/terraform.tfstate"
    region = "eu-north-1"
  }
}
EOF

# 2. Initiera med migration
terraform init -migrate-state
# Kopierar local state till S3

# 3. Verifiera
terraform state list
```

---

## Disaster recovery

```bash
# Backup state regelbundet
terraform state pull > backups/state_$(date +%Y%m%d).json

# Återställ från backup
terraform state push backups/state_20240115.json

# Eller: Recreate från scratch
# Ta bort state och importera allt
rm terraform.tfstate
terraform import aws_instance.web i-12345...
terraform import aws_vpc.main vpc-12345...
# etc.
```

---

## Moved blocks (Terraform 1.1+)

```hcl
# Refaktorera utan state-kommandon

# Rename resurs
moved {
  from = aws_instance.web
  to   = aws_instance.webserver
}

resource "aws_instance" "webserver" {
  # ... (samma config)
}

# Flytta till module
moved {
  from = aws_instance.app
  to   = module.compute.aws_instance.app
}

# Kör plan - Terraform förstår flytten
terraform plan
# aws_instance.web has moved to aws_instance.webserver
# No changes.

# Apply för att uppdatera state
terraform apply
```

---

## Import best practices

```bash
# 1. Tagga resurser innan import
aws ec2 create-tags --resources i-12345 --tags Key=ManagedBy,Value=Terraform

# 2. Importera i små batches
# Inte 100 resurser på en gång

# 3. Verifiera efter varje import
terraform plan  # Bör visa inga ändringar

# 4. Dokumentera importerade resurser
# Kommentera i kod var de kom från

# 5. Kör i test-miljö först
terraform workspace new import-test
terraform import ...
terraform workspace delete import-test
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| terraform import | Tar in existerande resurs i state |
| Import blocks (1.5+) | Deklarativ import direkt i .tf-filer |
| -generate-config-out | Genererar .tf-filer fran importerad resurs |
| moved blocks | Refaktorering utan state-kommandon |
| State backup | KRITISKT - alltid backup fore migration |

## Kom ihag

- terraform import kraver att resource block finns i .tf forst
- terraform plan efter import ska visa "No changes"
- terraform state mv for rename utan destroy/create
- terraform state rm tar bort fran state, INTE fran cloud
- moved {} i kod ar battre an terraform state mv
""",
        },
        {
            "title": "Terraform in CI/CD",
            "slug": "terraform-in-cicd",
            "difficulty": "advanced",
            "content": """
# Terraform in CI/CD

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan CI/CD | Konsekvens |
|-------------------|------------|
| Manuell korning | Vem korde vad? Nar? Varfor? |
| Ingen granskning | Misstag gar direkt till prod |
| Inkonsistent process | Olika personer gor olika |
| Ingen audit trail | Compliance-problem |

CI/CD for Terraform ger kontroll, sparbarhet och automation. Plan i PR, Apply efter merge. Allt loggas, allt granskas, allt ar repeterbart.

+---------------------------------------------------------+
|               TERRAFORM CI/CD PIPELINE                   |
+---------------------------------------------------------+
|  PR Created -▶ fmt -▶ validate -▶ plan -▶ Comment      |
|                                            |            |
|  PR Merged -▶ plan -▶ apply -▶ notify                  |
|                         |                               |
|                    Protected by                         |
|                    approval gates                       |
+---------------------------------------------------------+

------------------------------------------------------------

---

## GitHub Actions

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read
  pull-requests: write

env:
  TF_VERSION: "1.6.0"
  AWS_REGION: "eu-north-1"

jobs:
  terraform:
    name: Terraform
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: ./terraform

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Terraform Format
        id: fmt
        run: terraform fmt -check -recursive
        continue-on-error: true

      - name: Terraform Init
        id: init
        run: terraform init

      - name: Terraform Validate
        id: validate
        run: terraform validate -no-color

      - name: Terraform Plan
        id: plan
        if: github.event_name == 'pull_request'
        run: terraform plan -no-color -out=tfplan
        continue-on-error: true

      - name: Update PR Comment
        uses: actions/github-script@v7
        if: github.event_name == 'pull_request'
        with:
          script: |
            const output = `#### Terraform Format 🖌 \`${{ steps.fmt.outcome }}\`
            #### Terraform Init ⚙️ \`${{ steps.init.outcome }}\`
            #### Terraform Validate 🤖 \`${{ steps.validate.outcome }}\`
            #### Terraform Plan 📖 \`${{ steps.plan.outcome }}\`

            <details><summary>Show Plan</summary>

            \`\`\`terraform
            ${{ steps.plan.outputs.stdout }}
            \`\`\`

            </details>`;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: output
            })

      - name: Terraform Plan Status
        if: steps.plan.outcome == 'failure'
        run: exit 1

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve tfplan
```

---

## GitLab CI

```yaml
# .gitlab-ci.yml
image: hashicorp/terraform:1.6.0

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform
  TF_STATE_NAME: production

cache:
  paths:
    - ${TF_ROOT}/.terraform

before_script:
  - cd ${TF_ROOT}
  - terraform init

stages:
  - validate
  - plan
  - apply

validate:
  stage: validate
  script:
    - terraform fmt -check -recursive
    - terraform validate
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

plan:
  stage: plan
  script:
    - terraform plan -out=tfplan
  artifacts:
    paths:
      - ${TF_ROOT}/tfplan
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

apply:
  stage: apply
  script:
    - terraform apply -auto-approve tfplan
  dependencies:
    - plan
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      when: manual
  environment:
    name: production
```

---

## OIDC för AWS (ingen secrets)

```yaml
# GitHub Actions med OIDC
name: Terraform with OIDC

on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  terraform:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: eu-north-1

      # Ingen AWS_ACCESS_KEY_ID eller AWS_SECRET_ACCESS_KEY!
```

```hcl
# Skapa OIDC provider i AWS
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = ["sts.amazonaws.com"]

  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

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
            "token.actions.githubusercontent.com:sub" = "repo:my-org/my-repo:*"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "github_actions" {
  role       = aws_iam_role.github_actions.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"  # Begränsa i prod!
}
```

---

## Plan artifacts

```yaml
# Spara plan som artifact
- name: Terraform Plan
  run: terraform plan -out=tfplan

- name: Upload Plan
  uses: actions/upload-artifact@v4
  with:
    name: tfplan
    path: terraform/tfplan
    retention-days: 5

# I apply-job
- name: Download Plan
  uses: actions/download-artifact@v4
  with:
    name: tfplan
    path: terraform

- name: Terraform Apply
  run: terraform apply tfplan
```

---

## Drift detection

```yaml
# Schemalagd drift check
name: Drift Detection

on:
  schedule:
    - cron: '0 6 * * *'  # 06:00 varje dag

jobs:
  drift-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init

      - name: Check for Drift
        id: plan
        run: |
          terraform plan -detailed-exitcode -out=tfplan
        continue-on-error: true

      - name: Report Drift
        if: steps.plan.outcome == 'failure'
        run: |
          echo "Drift detected!"
          # Skicka Slack/Teams/PagerDuty alert
```

---

## Terraform Cloud/Enterprise

```hcl
# Använd Terraform Cloud som backend
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      name = "production"
    }
  }
}

# Eller med tags
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      tags = ["app:myapp", "env:prod"]
    }
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| CI/CD | Ger sparbarhet, granskning och automation |
| Plan i PR | Visa andringar innan merge - review |
| Apply vid merge | Endast efter godkand PR till main |
| OIDC | Eliminerar statiska credentials i CI/CD |
| Drift detection | Schemalagd kontroll av config vs verklighet |

## Kom ihag

- terraform fmt -check i CI for konsistent formatering
- terraform validate fangar syntax-fel tidigt
- Spara plan som artifact for exakt reproducerbarhet
- ALDRIG terraform apply -auto-approve i PR-pipeline
- Terraform Cloud ger gratis remote state och collaboration
""",
        },
        {
            "title": "Security Best Practices",
            "slug": "security-best-practices",
            "difficulty": "advanced",
            "content": """
# Security Best Practices

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Sakerhetsproblem | Konsekvens |
|------------------|------------|
| Secrets i state | State-fil laser = alla secrets exponerade |
| Over-privileged IAM | Komprometterad pipeline = full AWS access |
| Okrypterad state | Data breach vid S3 misconfiguration |
| Ingen policy validation | Osaker infra deployeras direkt |

Terraform hanterar kritisk infrastruktur - IAM, natverk, databaser. Sakerhet maste byggas in fran start, inte laggas till efterat. Defense in depth med kryptering, least privilege och policy as code.

+---------------------------------------------------------+
|               SECURITY LAYERS                            |
+---------------------------------------------------------+
|  1. State Security    | Krypterat, begransad access    |
|  2. Secrets Mgmt      | Aldrig i kod, externa stores   |
|  3. Least Privilege   | Minimal IAM for varje resurs   |
|  4. Policy as Code    | Sentinel, OPA, tfsec           |
|  5. Audit Logging     | CloudTrail, state versioning   |
+---------------------------------------------------------+

------------------------------------------------------------

---

## State security

```hcl
# S3 backend med kryptering
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "eu-north-1"

    # Kryptering
    encrypt        = true
    kms_key_id     = "arn:aws:kms:eu-north-1:123456789012:key/..."

    # Locking
    dynamodb_table = "terraform-locks"

    # Versioning (aktivera på bucket)
  }
}

# S3 bucket för state
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state"
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.terraform.arn
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

---

## Secrets management

```hcl
# ALDRIG hårdkoda secrets!

# Dåligt ❌
resource "aws_db_instance" "main" {
  password = "mysecretpassword"
}

# Bra ✅ - Variabel (från CI/CD)
variable "db_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "main" {
  password = var.db_password
}

# Bättre ✅ - AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}

resource "aws_db_instance" "main" {
  password = data.aws_secretsmanager_secret_version.db.secret_string
}

# Eller generera och lagra
resource "random_password" "db" {
  length  = 32
  special = true
}

resource "aws_secretsmanager_secret" "db" {
  name = "prod/db/password"
}

resource "aws_secretsmanager_secret_version" "db" {
  secret_id     = aws_secretsmanager_secret.db.id
  secret_string = random_password.db.result
}
```

---

## Least privilege IAM

```hcl
# Specifika permissions, inte AdministratorAccess

data "aws_iam_policy_document" "terraform" {
  # Endast nödvändiga actions
  statement {
    sid    = "EC2Management"
    effect = "Allow"

    actions = [
      "ec2:Describe*",
      "ec2:CreateTags",
      "ec2:RunInstances",
      "ec2:TerminateInstances"
    ]

    resources = ["*"]

    condition {
      test     = "StringEquals"
      variable = "aws:RequestedRegion"
      values   = ["eu-north-1"]
    }
  }

  # Begränsa till specifika resurser
  statement {
    sid    = "S3Access"
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:PutObject"
    ]

    resources = [
      "arn:aws:s3:::my-bucket/*"
    ]
  }
}

# Kräv MFA för känsliga operationer
data "aws_iam_policy_document" "require_mfa" {
  statement {
    sid    = "RequireMFA"
    effect = "Deny"

    actions = ["*"]

    resources = ["*"]

    condition {
      test     = "BoolIfExists"
      variable = "aws:MultiFactorAuthPresent"
      values   = ["false"]
    }
  }
}
```

---

## Sensitive outputs

```hcl
# Markera känsliga outputs
output "db_password" {
  value     = random_password.db.result
  sensitive = true  # Döljs i terminal
}

# Sensitive variabler
variable "api_key" {
  type      = string
  sensitive = true
}

# State innehåller fortfarande värdet!
# Kryptera state och begränsa access
```

---

## Policy as Code med Sentinel/OPA

```hcl
# Sentinel policy (Terraform Cloud/Enterprise)
# cost-estimation.sentinel

import "tfplan/v2" as tfplan

# Beräkna kostnad
monthly_cost = 0
for tfplan.resource_changes as _, rc {
  if rc.type == "aws_instance" and rc.change.actions contains "create" {
    instance_type = rc.change.after.instance_type
    if instance_type == "t3.large" {
      monthly_cost += 50
    }
  }
}

# Policy: Begränsa kostnad per apply
main = rule {
  monthly_cost < 500
}
```

```yaml
# OPA policy för Terraform
# policy/terraform.rego

package terraform

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_s3_bucket"
  not resource.change.after.server_side_encryption_configuration

  msg := sprintf("S3 bucket %s must have encryption enabled", [resource.name])
}

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_security_group_rule"
  resource.change.after.cidr_blocks[_] == "0.0.0.0/0"
  resource.change.after.from_port == 22

  msg := "SSH (port 22) should not be open to the world"
}
```

---

## Kryptering av resurser

```hcl
# EBS encryption by default
resource "aws_ebs_encryption_by_default" "enabled" {
  enabled = true
}

# KMS key för kryptering
resource "aws_kms_key" "main" {
  description             = "Main encryption key"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  policy = data.aws_iam_policy_document.kms.json
}

# RDS med kryptering
resource "aws_db_instance" "main" {
  identifier     = "mydb"
  engine         = "postgres"
  instance_class = "db.t3.micro"

  storage_encrypted = true
  kms_key_id        = aws_kms_key.main.arn
}

# S3 med kryptering
resource "aws_s3_bucket_server_side_encryption_configuration" "main" {
  bucket = aws_s3_bucket.main.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.main.arn
    }
  }
}
```

---

## Nätverkssäkerhet

```hcl
# Private subnets för databaser
resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.100.0/24"
  map_public_ip_on_launch = false  # Ingen public IP
}

# Strikt security group
resource "aws_security_group" "db" {
  name        = "db-sg"
  vpc_id      = aws_vpc.main.id

  # Endast från app-tier
  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]
  }

  # Ingen egress (eller specifika endpoints)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = []  # Ingen utgående trafik
  }
}

# VPC Flow Logs
resource "aws_flow_log" "main" {
  vpc_id          = aws_vpc.main.id
  traffic_type    = "ALL"
  iam_role_arn    = aws_iam_role.flow_log.arn
  log_destination = aws_cloudwatch_log_group.flow_log.arn
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| State encryption | KMS-kryptering for state i S3 |
| Secrets Manager | Secrets i extern store, aldrig i kod |
| Least privilege | Minimal IAM for varje resurs och pipeline |
| sensitive = true | Doljer varden i plan och output |
| Policy as Code | Sentinel, OPA, tfsec for automatisk validering |

## Kom ihag

- S3 bucket for state: versioning + encryption + access logging
- aws_iam_policy_document ar sakrare an hardkodad JSON
- Checkov och tfsec skannar for sakerhetsproblem i CI
- ALDRIG commit tfvars med secrets - anvand environment variabler
- VPC Flow Logs for natverksovervakning
""",
        },
        {
            "title": "Testing Terraform",
            "slug": "testing-terraform",
            "difficulty": "advanced",
            "content": """
# Testing Terraform

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan testning | Konsekvens |
|----------------------|------------|
| Otestade andringar | Bryter produktion vid apply |
| Ingen linting | Inkonsistent kod, dolda fel |
| Ingen security scanning | Sarbarheter deployeras |
| Saknar integration tests | Modules fungerar inte ihop |

Tester fangar problem innan deploy. Static analysis ar gratis och snabbt. Integration tests verifierar mot verklig infrastruktur. Policy tests sakerstraller compliance.

+---------------------------------------------------------+
|               TERRAFORM TEST PYRAMID                     |
+---------------------------------------------------------+
|                    +-----------+                        |
|                    | E2E Tests |  Langsammast           |
|                   ++-----------++                       |
|                   |Integration  |  Verkliga resurser    |
|                  ++-------------++                      |
|                  |  Unit Tests   |  Module-logik        |
|                 ++---------------++                     |
|                 |  Static Analysis |  Snabbast          |
|                 +-----------------+                     |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Static analysis

```bash
# Format check
terraform fmt -check -recursive -diff

# Validering
terraform validate

# TFLint - Linter för Terraform
brew install tflint                  # macOS
tflint --init
tflint

# tflint.hcl
plugin "aws" {
  enabled = true
  version = "0.27.0"
  source  = "github.com/terraform-linters/tflint-ruleset-aws"
}

rule "terraform_naming_convention" {
  enabled = true
}

rule "terraform_documented_variables" {
  enabled = true
}

# Checkov - Security scanning
pip install checkov
checkov -d .

# tfsec - Security scanner
brew install tfsec
tfsec .
```

---

## Terratest

```go
// test/vpc_test.go
package test

import (
    "testing"

    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVpcModule(t *testing.T) {
    t.Parallel()

    terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
        TerraformDir: "../modules/vpc",

        Vars: map[string]interface{}{
            "name":            "test-vpc",
            "cidr":            "10.0.0.0/16",
            "azs":             []string{"eu-north-1a", "eu-north-1b"},
            "private_subnets": []string{"10.0.1.0/24", "10.0.2.0/24"},
            "public_subnets":  []string{"10.0.101.0/24", "10.0.102.0/24"},
        },
    })

    // Cleanup
    defer terraform.Destroy(t, terraformOptions)

    // Deploy
    terraform.InitAndApply(t, terraformOptions)

    // Validate outputs
    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcId)

    privateSubnets := terraform.OutputList(t, terraformOptions, "private_subnet_ids")
    assert.Equal(t, 2, len(privateSubnets))
}
```

```bash
# Kör Terratest
cd test
go test -v -timeout 30m
```

---

## Terraform test (native, 1.6+)

```hcl
# tests/vpc.tftest.hcl
provider "aws" {
  region = "eu-north-1"
}

variables {
  name = "test-vpc"
  cidr = "10.0.0.0/16"
}

run "create_vpc" {
  command = apply

  assert {
    condition     = aws_vpc.main.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block mismatch"
  }

  assert {
    condition     = aws_vpc.main.enable_dns_hostnames == true
    error_message = "DNS hostnames should be enabled"
  }
}

run "verify_subnets" {
  command = apply

  assert {
    condition     = length(aws_subnet.public) == 2
    error_message = "Expected 2 public subnets"
  }
}
```

```bash
# Kör native tests
terraform test
```

---

## Mocking i tests

```hcl
# tests/mock.tftest.hcl

# Mock provider - ingen riktig AWS-kommunikation
mock_provider "aws" {}

run "unit_test" {
  command = plan  # Bara plan, ingen apply

  assert {
    condition     = aws_instance.web.instance_type == "t3.micro"
    error_message = "Wrong instance type"
  }
}

# Override specifika resurser
override_resource {
  target = aws_ami.ubuntu
  values = {
    id = "ami-mock12345"
  }
}
```

---

## Integration test workflow

```yaml
# .github/workflows/terraform-test.yml
name: Terraform Tests

on:
  pull_request:
    branches: [main]

jobs:
  static-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Terraform Format
        run: terraform fmt -check -recursive

      - name: Terraform Validate
        run: |
          terraform init -backend=false
          terraform validate

      - name: TFLint
        uses: terraform-linters/setup-tflint@v4
        with:
          tflint_version: latest

      - run: tflint --init && tflint

      - name: Checkov
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: .
          soft_fail: true

  integration-test:
    needs: static-analysis
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Test
        run: terraform test
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

---

## Cost estimation

```bash
# Infracost - Kostnadsprediction
brew install infracost

# Generera kostnad
infracost breakdown --path .

# I CI/CD
infracost diff --path . --compare-to infracost-base.json

# GitHub PR comment
infracost comment github \
  --path /tmp/infracost.json \
  --repo $GITHUB_REPOSITORY \
  --github-token $GITHUB_TOKEN \
  --pull-request $PR_NUMBER
```

---

## Contract testing

```hcl
# Validera module-kontrakt

# Module output måste ha specifikt format
variable "subnets" {
  type = list(object({
    id         = string
    cidr_block = string
    az         = string
  }))

  validation {
    condition = alltrue([
      for s in var.subnets : can(regex("^subnet-", s.id))
    ])
    error_message = "All subnet IDs must start with 'subnet-'"
  }
}

# Test
run "contract_validation" {
  command = plan

  variables {
    subnets = [
      { id = "subnet-123", cidr_block = "10.0.1.0/24", az = "eu-north-1a" },
      { id = "subnet-456", cidr_block = "10.0.2.0/24", az = "eu-north-1b" }
    ]
  }

  # Ingen assert behövs - validering sker automatiskt
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| terraform fmt/validate | Gratis statisk analys i varje pipeline |
| TFLint | Linter for best practices och provider-regler |
| Checkov/tfsec | Security scanning for sarbarheter |
| Terratest | Go-baserade integrationstester mot verklig infra |
| terraform test (1.6+) | Native HCL-baserade tester |

## Kom ihag

- Statisk analys ar snabb och ska koras vid varje commit
- Integrationstester skapar verkliga resurser - dyrt men vardefullt
- Infracost visar kostnadspaverkan innan apply
- terraform test kraver tests/ katalog med .tftest.hcl filer
- Contract testing validerar module input/output kontrakt
""",
        },
        {
            "title": "Remote State & Backends",
            "slug": "remote-state-backends",
            "difficulty": "intermediate",
            "content": '''
# Remote State & Backends

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem med lokal state | Konsekvens |
|------------------------|------------|
| Inte delbar | Team kan inte samarbeta |
| Ingen backup | Forlorad state = forlorad kontroll |
| Ingen locking | Parallella apply = korrupt state |
| Ingen encryption | Secrets i klartext pa disk |

Remote backends (S3, GCS, Azure Blob) loser alla dessa problem. State sparas centralt, krypterat, med locking och versioning. Obligatoriskt for team och CI/CD.

+---------------------------------------------------------+
|              REMOTE STATE ARCHITECTURE                   |
+---------------------------------------------------------+
|                                                          |
|  Developer A --+                                        |
|                |      +----------+      +-----------+  |
|  Developer B --+----▶ | S3 State | ----▶| DynamoDB  |  |
|                |      | (central)|      |  (lock)   |  |
|  CI/CD --------+      +----------+      +-----------+  |
|                              |                          |
|                              ▼                          |
|                       +----------+                      |
|                       |   KMS    |                      |
|                       |(encrypt) |                      |
|                       +----------+                      |
+---------------------------------------------------------+

------------------------------------------------------------

---

## S3 Backend (AWS)

```hcl
# backend.tf - S3 backend med DynamoDB locking

terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"    # S3 bucket namn
    key            = "prod/network/terraform.tfstate"  # Path i bucket
    region         = "eu-north-1"                   # AWS region

    # State locking med DynamoDB
    dynamodb_table = "terraform-state-lock"         # Lock table

    # Encryption
    encrypt        = true                           # SSE-S3 encryption

    # Access
    role_arn       = "arn:aws:iam::123456789:role/TerraformRole"  # Optional
  }
}
```

```bash
# Skapa S3 bucket och DynamoDB för state
aws s3 mb s3://my-terraform-state-bucket --region eu-north-1

# Aktivera versioning
aws s3api put-bucket-versioning \
  --bucket my-terraform-state-bucket \
  --versioning-configuration Status=Enabled

# Skapa DynamoDB lock table
aws dynamodb create-table \
  --table-name terraform-state-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region eu-north-1
```

---

## Azure Blob Backend

```hcl
# backend.tf - Azure Blob Storage

terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"             # Resource group
    storage_account_name = "tfstateaccount"         # Storage account
    container_name       = "tfstate"                # Container
    key                  = "prod.terraform.tfstate" # Blob name

    # Encryption och locking är inbyggt i Azure
    use_azuread_auth     = true                     # AAD auth istället för access key
  }
}
```

```bash
# Skapa Azure storage med AZ CLI
az group create --name tfstate-rg --location northeurope

az storage account create \
  --name tfstateaccount \
  --resource-group tfstate-rg \
  --location northeurope \
  --sku Standard_LRS \
  --encryption-services blob

az storage container create \
  --name tfstate \
  --account-name tfstateaccount
```

---

## GCS Backend (Google Cloud)

```hcl
# backend.tf - Google Cloud Storage

terraform {
  backend "gcs" {
    bucket  = "my-terraform-state"                  # GCS bucket
    prefix  = "prod/network"                        # Path prefix

    # Locking är inbyggt i GCS backend
  }
}
```

```bash
# Skapa GCS bucket
gsutil mb -l europe-north1 gs://my-terraform-state

# Aktivera versioning
gsutil versioning set on gs://my-terraform-state
```

---

## Backend migration

```bash
# Migrera från lokal till S3
# 1. Lägg till backend config
# 2. Kör init

terraform init                      # Frågar om migration

# Output:
# Initializing the backend...
# Do you want to copy existing state to the new backend?
# Enter "yes" to copy and "no" to start with empty state.

# Migrera mellan backends
terraform init -migrate-state       # Explicit migration

# Rekonfigurera backend
terraform init -reconfigure         # Kassera gammal state
```

---

## State environments med prefix

```hcl
# Separera miljöer i samma bucket

# dev
terraform {
  backend "s3" {
    bucket = "company-terraform-state"
    key    = "dev/app/terraform.tfstate"      # dev prefix
    region = "eu-north-1"
  }
}

# prod
terraform {
  backend "s3" {
    bucket = "company-terraform-state"
    key    = "prod/app/terraform.tfstate"     # prod prefix
    region = "eu-north-1"
  }
}
```

```bash
# Eller använd workspaces
terraform workspace new dev
terraform workspace new prod
terraform workspace select prod

# State sparas som:
# s3://bucket/env:/prod/terraform.tfstate
```

---

## Partial backend configuration

```hcl
# main.tf - Backend utan känsliga värden
terraform {
  backend "s3" {
    key    = "app/terraform.tfstate"
  }
}
```

```bash
# Övriga värden vid init
terraform init \
  -backend-config="bucket=my-state-bucket" \
  -backend-config="region=eu-north-1" \
  -backend-config="dynamodb_table=tf-lock"

# Eller från fil
terraform init -backend-config=backend.hcl
```

```hcl
# backend.hcl - Separata backend-värden
bucket         = "my-state-bucket"
region         = "eu-north-1"
dynamodb_table = "tf-lock"
encrypt        = true
```

---

## Remote state data source

```hcl
# Läs state från annat projekt

data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "prod/network/terraform.tfstate"
    region = "eu-north-1"
  }
}

# Använd outputs från remote state
resource "aws_instance" "app" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  # Referera till network-projektets VPC
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_ids[0]

  vpc_security_group_ids = [
    data.terraform_remote_state.network.outputs.app_security_group_id
  ]
}
```

---

## State locking

```bash
# Vid concurrency-problem
terraform force-unlock LOCK_ID      # FARLIGT - endast vid stuck lock

# Visa lock-status
aws dynamodb get-item \
  --table-name terraform-state-lock \
  --key '{"LockID":{"S":"my-state-bucket/prod/app/terraform.tfstate-md5"}}'
```

```hcl
# Lock info i state
# terraform.tfstate innehåller:
{
  "lineage": "unique-id",
  "serial": 42,
  "terraform_version": "1.7.0"
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Remote backend | Krav for team - S3, GCS, Azure Blob |
| State locking | DynamoDB/GCS forhindrar parallella andringar |
| Partial config | -backend-config haller secrets utanfor kod |
| State migration | terraform init -migrate-state flyttar state |
| Remote state data | Cross-project references via data source |

## Kom ihag

- S3 bucket: aktivera versioning, encryption, access logging
- DynamoDB table behovs for locking - skapa fore init
- terraform force-unlock ENDAST vid stuck lock
- backend.hcl for miljospecifika backend-varden
- terraform state pull > backup.json for manuell backup
''',
        },
        {
            "title": "Terraform Cloud & Enterprise",
            "slug": "terraform-cloud-enterprise",
            "difficulty": "advanced",
            "content": '''
# Terraform Cloud & Enterprise

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem TFC loser | Fordel |
|-------------------|--------|
| DIY state management | Managed state med UI och versioning |
| Egen CI/CD for TF | Remote execution med runs i TFC |
| Team access control | RBAC och SSO integration |
| Compliance | Policy as Code med Sentinel |
| Module discovery | Private registry for interna modules |

Terraform Cloud ar HashiCorps managed platform - gratis for sma team. Remote state, execution, VCS integration och policy enforcement i en tjanst. Enterprise lagger till SSO, audit logging och mer.

+---------------------------------------------------------+
|              TERRAFORM CLOUD FEATURES                    |
+---------------------------------------------------------+
|  Free Tier          | Plus/Enterprise                  |
|  -----------------  | --------------------------------  |
|  Remote state       | SSO/SAML                         |
|  Remote runs        | Audit logging                    |
|  VCS integration    | Private networking               |
|  5 users            | Unlimited users                  |
|  State versioning   | Custom agents                    |
|  Cost estimation    | Sentinel policies                |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Grundläggande setup

```hcl
# main.tf - Terraform Cloud backend

terraform {
  cloud {
    organization = "my-company"             # TFC organization

    workspaces {
      name = "production"                   # Specifik workspace
      # ELLER
      # tags = ["app:web", "env:prod"]      # Tag-baserad
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

```bash
# Login till Terraform Cloud
terraform login                              # Öppnar browser för auth

# Initiera med cloud backend
terraform init

# Plan och apply körs remote
terraform plan                               # Remote execution
terraform apply
```

---

## Workspace configuration

```bash
# CLI-driven workflow - lokala plans, remote apply
terraform plan                               # Körs remote
terraform apply                              # Körs remote

# VCS-driven workflow - triggras av git push
# Konfigurera i TFC UI:
# 1. Connect VCS provider
# 2. Map repo till workspace
# 3. Push triggers plan
# 4. Merge triggers apply
```

```hcl
# Variabler i Terraform Cloud
# Sätts i UI eller via API

# terraform.auto.tfvars - Lokal override
environment = "staging"
instance_type = "t3.small"

# Sensitive variables sätts i TFC UI
# AWS_ACCESS_KEY_ID (sensitive, env var)
# AWS_SECRET_ACCESS_KEY (sensitive, env var)
```

---

## Sentinel policies

```python
# policies/cost-estimation.sentinel
# Policy: Blockera om kostnaden överstiger threshold

import "tfrun"
import "decimal"

# Max kostnad per månad
max_monthly_cost = decimal.new(500)

# Hämta estimerad kostnad
monthly_cost = decimal.new(tfrun.cost_estimation.proposed_monthly_cost)

main = rule {
    monthly_cost.less_than_or_equals(max_monthly_cost)
}
```

```python
# policies/required-tags.sentinel
# Policy: Alla resurser måste ha tags

import "tfplan/v2" as tfplan

required_tags = ["Environment", "Owner", "Project"]

# Hitta alla resurser som stöder tags
taggable_resources = filter tfplan.resource_changes as _, rc {
    rc.mode is "managed" and
    rc.type in ["aws_instance", "aws_s3_bucket", "aws_vpc"]
}

# Kontrollera att alla required tags finns
main = rule {
    all taggable_resources as _, resource {
        all required_tags as tag {
            resource.change.after.tags contains tag
        }
    }
}
```

```bash
# Policy set struktur
policies/
+-- sentinel.hcl            # Policy set config
+-- cost-estimation.sentinel
+-- required-tags.sentinel
+-- test/
    +-- required-tags/
        +-- pass.hcl
        +-- fail.hcl
```

---

## Run triggers

```hcl
# Workspace dependency - production beror på staging

# I Terraform Cloud UI:
# Workspace: production
# Run Triggers: Add staging workspace

# När staging workspace apply:ar
# -> production workspace triggas automatiskt
```

```bash
# API-driven runs
curl \
  --header "Authorization: Bearer $TFC_TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request POST \
  --data @payload.json \
  https://app.terraform.io/api/v2/runs
```

---

## Private module registry

```bash
# Publicera module till privat registry
# Module repo måste följa naming: terraform-PROVIDER-NAME

# Via VCS:
# 1. Connect GitHub/GitLab
# 2. Add module från repo
# 3. Tag releases (v1.0.0)

# Använd privat module
module "vpc" {
  source  = "app.terraform.io/my-company/vpc/aws"
  version = "1.0.0"

  cidr = "10.0.0.0/16"
}
```

```hcl
# terraform.tf - Registry credentials
credentials "app.terraform.io" {
  token = "your-token-here"
}
```

---

## Agent pools (Enterprise)

```hcl
# Självhostad agent för privat nätverk

# 1. Skapa agent pool i TFC
# 2. Hämta agent token
# 3. Kör agent i privat nätverk

# docker-compose.yml för agent
services:
  tfc-agent:
    image: hashicorp/tfc-agent:latest
    environment:
      TFC_AGENT_TOKEN: "your-agent-token"
      TFC_AGENT_NAME: "prod-agent-1"
    restart: unless-stopped
```

```bash
# Installera agent direkt
curl -o tfc-agent.zip https://releases.hashicorp.com/tfc-agent/1.7.0/tfc-agent_1.7.0_linux_amd64.zip
unzip tfc-agent.zip
./tfc-agent
```

---

## Team access och RBAC

```bash
# Team permissions i TFC:
# - Read: Se state och runs
# - Plan: Köra plans
# - Write: Apply changes
# - Admin: Hantera workspace settings

# Organization-level permissions:
# - Manage Policies
# - Manage Workspaces
# - Manage VCS Settings
# - Manage Teams
```

```hcl
# Terraform provider för TFC
terraform {
  required_providers {
    tfe = {
      source  = "hashicorp/tfe"
      version = "~> 0.51"
    }
  }
}

provider "tfe" {
  organization = "my-company"
}

# Skapa workspace med kod
resource "tfe_workspace" "production" {
  name              = "production"
  organization      = "my-company"
  terraform_version = "1.7.0"

  vcs_repo {
    identifier     = "my-org/infrastructure"
    branch         = "main"
    oauth_token_id = var.oauth_token_id
  }
}

# Team access
resource "tfe_team_access" "dev_team" {
  access       = "write"
  team_id      = tfe_team.developers.id
  workspace_id = tfe_workspace.production.id
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Terraform Cloud | Gratis managed state, runs och VCS-integration |
| VCS-driven workflow | Git push triggar plan, merge triggar apply |
| Sentinel | Policy as Code for compliance enforcement |
| Private registry | Interna modules med versioning |
| Agent pools | Kor Terraform i privat natverk |

## Kom ihag

- terraform login authenticerar mot TFC
- cloud {} block ersatter backend {} for TFC
- Workspace settings: auto-apply, terraform version, VCS repo
- Variable sets delar variabler mellan workspaces
- Run triggers kopplar ihop beroende workspaces
''',
        },
        {
            "title": "Advanced Module Patterns",
            "slug": "advanced-module-patterns",
            "difficulty": "advanced",
            "content": '''
# Advanced Module Patterns

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan patterns | Konsekvens |
|----------------------|------------|
| Monolitiska moduler | Svara att underhalla och testa |
| Ingen standardisering | Varje team gor egna losningar |
| Hardkodad konfiguration | Moduler funkar bara i ett use case |
| Ingen composition | Copy-paste istallet for kombination |

Avancerade module patterns tar atervanvandning till nasta niva. Composition kombinerar sma moduler. Factory pattern skapar manga resurser. Wrapper patterns forenklar komplexa interfaces.

+---------------------------------------------------------+
|              ADVANCED MODULE PATTERNS                    |
+---------------------------------------------------------+
|  Composition    | Sma moduler som kombineras            |
|  Factory        | for_each skapar manga instanser       |
|  Wrapper        | Forenklar komplex modul-interface     |
|  Opinionated    | Defaults for common use cases         |
|  Configuration  | Flexibel via complex types            |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Module composition

```hcl
# modules/network/main.tf
# Liten, fokuserad modul

resource "aws_vpc" "main" {
  cidr_block           = var.cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(var.tags, {
    Name = var.name
  })
}

output "vpc_id" {
  value = aws_vpc.main.id
}
```

```hcl
# modules/eks-cluster/main.tf
# Komponerar andra moduler

module "vpc" {
  source = "../network"

  name = "${var.cluster_name}-vpc"
  cidr = var.vpc_cidr
  tags = var.tags
}

module "subnets" {
  source = "../subnets"

  vpc_id            = module.vpc.vpc_id
  availability_zones = var.availability_zones
  public_cidrs      = var.public_subnet_cidrs
  private_cidrs     = var.private_subnet_cidrs
  tags              = var.tags
}

module "eks" {
  source = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = var.cluster_name
  cluster_version = var.kubernetes_version

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.subnets.private_subnet_ids
}
```

---

## Factory pattern

```hcl
# modules/s3-buckets/main.tf
# Skapa många likadana resurser

variable "buckets" {
  type = map(object({
    versioning = optional(bool, true)
    encryption = optional(string, "AES256")
    lifecycle_rules = optional(list(object({
      id      = string
      enabled = bool
      prefix  = optional(string, "")
      expiration_days = optional(number)
    })), [])
  }))
}

resource "aws_s3_bucket" "buckets" {
  for_each = var.buckets

  bucket = each.key

  tags = {
    ManagedBy = "terraform"
  }
}

resource "aws_s3_bucket_versioning" "buckets" {
  for_each = { for k, v in var.buckets : k => v if v.versioning }

  bucket = aws_s3_bucket.buckets[each.key].id

  versioning_configuration {
    status = "Enabled"
  }
}

# Användning
module "data_buckets" {
  source = "./modules/s3-buckets"

  buckets = {
    "company-data-lake"     = { versioning = true }
    "company-logs"          = { versioning = false, lifecycle_rules = [...] }
    "company-backups"       = { versioning = true, encryption = "aws:kms" }
  }
}
```

---

## Wrapper modules

```hcl
# modules/simple-lambda/main.tf
# Förenkla komplex upstream-modul

# Komplex upstream-modul med 50+ variabler
module "lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 6.0"

  # Fasta värden enligt company standards
  runtime       = "python3.11"
  architectures = ["arm64"]
  memory_size   = 256
  timeout       = 30

  # Exponera endast det som behövs
  function_name = var.name
  description   = var.description
  handler       = var.handler
  source_path   = var.source_path

  # Security defaults
  tracing_mode = "Active"

  environment_variables = merge({
    LOG_LEVEL   = "INFO"
    ENVIRONMENT = var.environment
  }, var.environment_variables)

  tags = var.tags
}
```

```hcl
# root/main.tf
# Enkel användning

module "order_processor" {
  source = "./modules/simple-lambda"

  name        = "order-processor"
  description = "Process incoming orders"
  handler     = "main.handler"
  source_path = "./src/order_processor"

  environment_variables = {
    QUEUE_URL = aws_sqs_queue.orders.url
  }
}
```

---

## Optional features pattern

```hcl
# modules/rds/variables.tf

variable "create_replica" {
  description = "Create read replica"
  type        = bool
  default     = false
}

variable "enable_monitoring" {
  description = "Enable enhanced monitoring"
  type        = bool
  default     = true
}

variable "backup_retention_days" {
  description = "Days to retain backups"
  type        = number
  default     = 7
}
```

```hcl
# modules/rds/main.tf

resource "aws_db_instance" "main" {
  identifier     = var.name
  engine         = "postgres"
  engine_version = var.engine_version
  instance_class = var.instance_class

  # Conditional monitoring
  monitoring_interval = var.enable_monitoring ? 60 : 0
  monitoring_role_arn = var.enable_monitoring ? aws_iam_role.monitoring[0].arn : null

  backup_retention_period = var.backup_retention_days
}

# Conditional read replica
resource "aws_db_instance" "replica" {
  count = var.create_replica ? 1 : 0

  identifier          = "${var.name}-replica"
  replicate_source_db = aws_db_instance.main.identifier
  instance_class      = var.replica_instance_class
}

# Conditional IAM role
resource "aws_iam_role" "monitoring" {
  count = var.enable_monitoring ? 1 : 0

  name = "${var.name}-monitoring"
  assume_role_policy = data.aws_iam_policy_document.monitoring_assume.json
}
```

---

## Configuration objects pattern

```hcl
# variables.tf - Strukturerad konfiguration

variable "config" {
  type = object({
    name        = string
    environment = string

    network = object({
      vpc_cidr = string
      azs      = list(string)
    })

    compute = optional(object({
      instance_type = optional(string, "t3.micro")
      min_size      = optional(number, 1)
      max_size      = optional(number, 3)
    }), {})

    database = optional(object({
      engine         = optional(string, "postgres")
      instance_class = optional(string, "db.t3.micro")
      multi_az       = optional(bool, false)
    }))

    features = optional(object({
      enable_monitoring = optional(bool, true)
      enable_backups    = optional(bool, true)
      enable_cdn        = optional(bool, false)
    }), {})
  })
}
```

```hcl
# main.tf - Användning

module "app" {
  source = "./modules/full-stack"

  config = {
    name        = "myapp"
    environment = "production"

    network = {
      vpc_cidr = "10.0.0.0/16"
      azs      = ["eu-north-1a", "eu-north-1b"]
    }

    compute = {
      instance_type = "t3.small"
      max_size      = 5
    }

    database = {
      multi_az = true
    }

    features = {
      enable_cdn = true
    }
  }
}
```

---

## Validation patterns

```hcl
# variables.tf med validering

variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  type = string

  validation {
    condition     = can(regex("^t3\\.(micro|small|medium|large)$", var.instance_type))
    error_message = "Only t3 instances allowed."
  }
}

variable "cidr" {
  type = string

  validation {
    condition     = can(cidrhost(var.cidr, 0))
    error_message = "Must be valid CIDR notation."
  }
}

# Komplex cross-variable validation
variable "config" {
  type = object({
    environment   = string
    instance_type = string
  })

  validation {
    condition = !(
      var.config.environment == "prod" &&
      contains(["t3.micro", "t3.small"], var.config.instance_type)
    )
    error_message = "Production requires at least t3.medium."
  }
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Composition | Sma moduler kombineras till storre |
| Factory pattern | for_each skapar manga liknande resurser |
| Wrapper modules | Forenklar komplexa upstream-moduler |
| Optional features | count = var.enabled ? 1 : 0 |
| Configuration objects | Strukturerad input med defaults |

## Kom ihag

- optional() i variable types for defaults (Terraform 1.3+)
- Validering fangar fel tidigt med tydliga meddelanden
- Sma fokuserade moduler ar lättare att testa
- Outputs ska vara vad konsumenten behover, inte allt
- README.md i varje modul ar obligatoriskt
''',
        },
        {
            "title": "Multi-Cloud & Provider Patterns",
            "slug": "multi-cloud-provider-patterns",
            "difficulty": "advanced",
            "content": '''
# Multi-Cloud & Provider Patterns

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Driver for multi-cloud | Verklighetsbild |
|-----------------------|-----------------|
| Vendor lock-in | Undvik beroende av en leverantor |
| Best-of-breed | AWS for compute, GCP for ML, Azure for .NET |
| Redundans | DR i annan cloud |
| Compliance | Data residency krav per region/land |

Terraform hanterar alla clouds med samma workflow. En state-fil kan innehalla resurser fran AWS, Azure och GCP. Samma HCL-syntax, samma plan/apply process.

+---------------------------------------------------------+
|              MULTI-CLOUD ARCHITECTURE                    |
+---------------------------------------------------------+
|                                                          |
|  +-------------------------------------------------+    |
|  |               Terraform                          |    |
|  +----------+----------+----------+---------------+    |
|             |          |          |                     |
|             ▼          ▼          ▼                     |
|       +---------+ +---------+ +---------+              |
|       |   AWS   | |  Azure  | |   GCP   |              |
|       |provider | |provider | |provider |              |
|       +---------+ +---------+ +---------+              |
|                                                          |
+---------------------------------------------------------+

------------------------------------------------------------

---

## Multi-provider setup

```hcl
# providers.tf - Flera cloud providers

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
  region = "eu-north-1"

  default_tags {
    tags = {
      ManagedBy = "terraform"
      Project   = var.project_name
    }
  }
}

# Azure Provider
provider "azurerm" {
  features {}

  subscription_id = var.azure_subscription_id
}

# Google Cloud Provider
provider "google" {
  project = var.gcp_project_id
  region  = "europe-north1"
}
```

---

## Provider aliases

```hcl
# Multi-region med aliases

provider "aws" {
  alias  = "stockholm"
  region = "eu-north-1"
}

provider "aws" {
  alias  = "ireland"
  region = "eu-west-1"
}

provider "aws" {
  alias  = "virginia"
  region = "us-east-1"
}

# Resurser med specifik provider
resource "aws_s3_bucket" "primary" {
  provider = aws.stockholm
  bucket   = "my-bucket-primary"
}

resource "aws_s3_bucket" "replica" {
  provider = aws.ireland
  bucket   = "my-bucket-replica"
}

# CloudFront kräver us-east-1 för certificates
resource "aws_acm_certificate" "cdn" {
  provider          = aws.virginia
  domain_name       = "cdn.example.com"
  validation_method = "DNS"
}
```

---

## Cross-cloud disaster recovery

```hcl
# Primary på AWS, DR på Azure

# Primary database på AWS
resource "aws_rds_cluster" "primary" {
  provider = aws.stockholm

  cluster_identifier = "primary-db"
  engine             = "aurora-postgresql"

  master_username = var.db_username
  master_password = var.db_password
}

# DR database på Azure
resource "azurerm_postgresql_flexible_server" "dr" {
  name                = "dr-db"
  location            = azurerm_resource_group.dr.location
  resource_group_name = azurerm_resource_group.dr.name

  administrator_login    = var.db_username
  administrator_password = var.db_password

  sku_name = "GP_Standard_D2s_v3"
  version  = "14"

  # Geo-redundant backup
  geo_redundant_backup_enabled = true
}

# DNS failover
resource "aws_route53_health_check" "primary" {
  fqdn              = aws_rds_cluster.primary.endpoint
  port              = 5432
  type              = "TCP"
  failure_threshold = "3"
}

resource "aws_route53_record" "db" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "db.example.com"
  type    = "CNAME"

  set_identifier = "primary"

  failover_routing_policy {
    type = "PRIMARY"
  }

  health_check_id = aws_route53_health_check.primary.id
  records         = [aws_rds_cluster.primary.endpoint]
  ttl             = 60
}
```

---

## Abstract resource pattern

```hcl
# modules/object-storage/main.tf
# Abstrahera cloud-specifik implementation

variable "provider_type" {
  type = string
  validation {
    condition     = contains(["aws", "azure", "gcp"], var.provider_type)
    error_message = "Must be aws, azure, or gcp."
  }
}

# AWS S3
resource "aws_s3_bucket" "bucket" {
  count  = var.provider_type == "aws" ? 1 : 0
  bucket = var.bucket_name
}

# Azure Blob
resource "azurerm_storage_container" "container" {
  count                 = var.provider_type == "azure" ? 1 : 0
  name                  = var.bucket_name
  storage_account_name  = var.storage_account
  container_access_type = "private"
}

# GCP Cloud Storage
resource "google_storage_bucket" "bucket" {
  count    = var.provider_type == "gcp" ? 1 : 0
  name     = var.bucket_name
  location = var.region
}

# Unified output
output "bucket_id" {
  value = coalesce(
    try(aws_s3_bucket.bucket[0].id, null),
    try(azurerm_storage_container.container[0].id, null),
    try(google_storage_bucket.bucket[0].id, null)
  )
}
```

---

## Provider configuration modules

```hcl
# modules/aws-provider/main.tf

variable "region" {
  type = string
}

variable "assume_role_arn" {
  type    = string
  default = null
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
      configuration_aliases = [aws]
    }
  }
}

# Dynamisk provider konfiguration
provider "aws" {
  region = var.region

  dynamic "assume_role" {
    for_each = var.assume_role_arn != null ? [1] : []
    content {
      role_arn = var.assume_role_arn
    }
  }

  default_tags {
    tags = {
      ManagedBy = "terraform"
      Region    = var.region
    }
  }
}
```

---

## Cross-account AWS

```hcl
# Multi-account med assume role

provider "aws" {
  alias  = "management"
  region = "eu-north-1"
  # Default credentials för management account
}

provider "aws" {
  alias  = "production"
  region = "eu-north-1"

  assume_role {
    role_arn     = "arn:aws:iam::PROD_ACCOUNT_ID:role/TerraformRole"
    session_name = "terraform"
  }
}

provider "aws" {
  alias  = "staging"
  region = "eu-north-1"

  assume_role {
    role_arn     = "arn:aws:iam::STAGING_ACCOUNT_ID:role/TerraformRole"
    session_name = "terraform"
  }
}

# Resurser i olika accounts
module "prod_network" {
  source = "./modules/network"

  providers = {
    aws = aws.production
  }

  cidr = "10.0.0.0/16"
}

module "staging_network" {
  source = "./modules/network"

  providers = {
    aws = aws.staging
  }

  cidr = "10.1.0.0/16"
}
```

---

## Provider passthrough

```hcl
# modules/vpc/main.tf

terraform {
  required_providers {
    aws = {
      source                = "hashicorp/aws"
      version               = "~> 5.0"
      configuration_aliases = [aws]  # Kräv explicit provider
    }
  }
}

# Modul använder injektad provider
resource "aws_vpc" "main" {
  cidr_block = var.cidr
}
```

```hcl
# root/main.tf

provider "aws" {
  alias  = "eu"
  region = "eu-north-1"
}

provider "aws" {
  alias  = "us"
  region = "us-east-1"
}

# Passera provider till modul
module "eu_vpc" {
  source = "./modules/vpc"

  providers = {
    aws = aws.eu
  }

  cidr = "10.0.0.0/16"
}

module "us_vpc" {
  source = "./modules/vpc"

  providers = {
    aws = aws.us
  }

  cidr = "10.1.0.0/16"
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Samma workflow | Terraform hanterar alla clouds med identiskt arbetsflode |
| Provider aliases | for multi-region och multi-account deployments |
| Abstrakta moduler | Doljer cloud-specifik implementation bakom enhetligt interface |
| Cross-account | Anvand assume_role for access mellan AWS-konton |
| Provider passthrough | Gör moduler flexibla med explicit providers-block |

## Kom ihag
- Varje cloud har sin provider med egen konfiguration
- Alias-pattern: `aws.eu`, `aws.us` for samma provider olika regioner
- Abstraktionslager gor det enkelt att byta cloud senare
- terraform_remote_state for cross-workspace data sharing
- Version-låsa providers for reproducerbarhet
''',
        },
        {
            "title": "Drift Detection & Reconciliation",
            "slug": "drift-detection-reconciliation",
            "difficulty": "advanced",
            "content": '''
# Drift Detection & Reconciliation

------------------------------
## Varfor viktigt for DevOps?

| Problem utan drift detection | Konsekvens |
|------------------------------|------------|
| Manuella konsolandringar upptacks inte | Konfiguration i kod stammer inte med verkligheten |
| Ingen insyn i infrastrukturandringar | Sakerhetsproblem gar oupptackta |
| State ur synk med verkligheten | Apply kan ge oforutsagbara resultat |
| Ingen audit trail for andringar | Omojligt att spara vem/vad/nar |

```
+-----------------------------------------------------------------+
|                    DRIFT LIVSCYKEL                              |
+-----------------------------------------------------------------+
|                                                                 |
|   +---------+    +---------+    +---------+    +---------+     |
|   |  Kod    |--->|  State  |--->|  Cloud  |--->|  Drift  |     |
|   | (.tf)   |    | (.state)|    |(resurser)|   |(avvikelse)|   |
|   +---------+    +---------+    +---------+    +---------+     |
|        |                                             |          |
|        +------------ terraform plan -----------------+          |
|                           |                                     |
|                     +-----+-----+                               |
|                     |  Drift?   |                               |
|                     +-----+-----+                               |
|               +-----------+-----------+                         |
|               v           v           v                         |
|          +--------+  +--------+  +--------+                     |
|          | Accept |  | Reject |  | Import |                     |
|          |(refresh)| |(apply) |  |(import)|                     |
|          +--------+  +--------+  +--------+                     |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## Så fungerar det

Terraform hanterar drift genom:

1. `terraform plan` visar drift
2. `terraform apply` reconcilierar
3. `terraform refresh` uppdaterar state
4. Automation detekterar drift kontinuerligt

---

## Detektera drift

```bash
# Plan visar drift
terraform plan                        # Visar alla ändringar

# Exempel output vid drift:
# aws_security_group.main will be updated in-place
#   ~ ingress {
#       ~ from_port = 22 -> 443    # Någon ändrade manuellt
#     }

# Refresh only - uppdatera state utan ändringar
terraform apply -refresh-only         # Bekräftelse krävs

# Detaljerad diff
terraform show -json | jq '.values.root_module.resources'
```

---

## Automated drift detection

```yaml
# .github/workflows/drift-detection.yml
name: Drift Detection

on:
  schedule:
    - cron: '0 */6 * * *'            # Var 6:e timme
  workflow_dispatch:                  # Manual trigger

jobs:
  detect-drift:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init

      - name: Detect Drift
        id: drift
        run: |
          terraform plan -detailed-exitcode -out=tfplan 2>&1 | tee plan.txt
          EXIT_CODE=$?
          if [ $EXIT_CODE -eq 2 ]; then
            echo "drift=true" >> $GITHUB_OUTPUT
            echo "## Drift Detected! :warning:" >> $GITHUB_STEP_SUMMARY
            cat plan.txt >> $GITHUB_STEP_SUMMARY
          fi
        continue-on-error: true

      - name: Notify on Drift
        if: steps.drift.outputs.drift == 'true'
        run: |
          curl -X POST "${{ secrets.SLACK_WEBHOOK }}" \
            -H 'Content-type: application/json' \
            -d '{"text": "Terraform drift detected in production!"}'
```

---

## Reconciliation strategies

```hcl
# Strategy 1: Accept drift - uppdatera state
# Använd när: Manuell ändring var korrekt

# Refresh state till verkligheten
terraform apply -refresh-only

# Strategy 2: Reject drift - återställ infrastruktur
# Använd när: Manuell ändring var fel

terraform apply                       # Återställ till kod
```

```bash
# Strategy 3: Import drift - inkorporera i kod
# Använd när: Manuell resurs ska hanteras av Terraform

# Hitta resurs-ID
aws ec2 describe-instances --filters "Name=tag:Name,Values=manual-instance"

# Import till state
terraform import aws_instance.manual i-0123456789abcdef

# Generera HCL (Terraform 1.5+)
terraform plan -generate-config-out=generated.tf
```

---

## Lifecycle ignore_changes

```hcl
# Ignorera specifika attribut som ändras utanför Terraform

resource "aws_instance" "app" {
  ami           = var.ami_id
  instance_type = var.instance_type

  lifecycle {
    # Ignorera tags som ändras av andra processer
    ignore_changes = [
      tags["LastModified"],
      tags["UpdatedBy"],
    ]

    # Ignorera user_data ändringar (kräver recreate)
    # ignore_changes = [user_data]
  }
}

resource "aws_autoscaling_group" "app" {
  name             = "app-asg"
  min_size         = 2
  max_size         = 10
  desired_capacity = 2

  lifecycle {
    # Ignorera desired_capacity - hanteras av autoscaling
    ignore_changes = [desired_capacity]
  }
}

resource "aws_ecs_service" "app" {
  name            = "app"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 2

  lifecycle {
    # Ignorera task_definition - uppdateras av CI/CD
    ignore_changes = [task_definition]
  }
}
```

---

## State manipulation

```bash
# Ta bort resurs från state (men behåll i cloud)
terraform state rm aws_instance.legacy
# Nu kan resursen hanteras manuellt

# Flytta resurs i state
terraform state mv aws_instance.old aws_instance.new
# Vid refactoring av kod

# Lista resurser i state
terraform state list

# Visa specifik resurs
terraform state show aws_instance.app

# Pull/push remote state
terraform state pull > backup.tfstate
terraform state push backup.tfstate
```

---

## Prevent destroy

```hcl
# Skydda kritiska resurser från oavsiktlig borttagning

resource "aws_rds_cluster" "production" {
  cluster_identifier = "production-db"
  engine             = "aurora-postgresql"

  deletion_protection = true           # Cloud-nivå skydd

  lifecycle {
    prevent_destroy = true             # Terraform-nivå skydd
  }
}

resource "aws_s3_bucket" "data_lake" {
  bucket = "company-data-lake"

  lifecycle {
    prevent_destroy = true
  }
}

# Försök att destroya ger:
# Error: Instance cannot be destroyed
# Resource aws_rds_cluster.production has lifecycle.prevent_destroy set
```

---

## Drift remediation workflow

```bash
# Komplett workflow för drift-hantering

# Steg 1: Detektera
terraform plan -detailed-exitcode
# Exit code 2 = drift detected

# Steg 2: Analysera
terraform show -json tfplan | jq '.resource_changes[] | select(.change.actions != ["no-op"])'

# Steg 3: Beslut
# - Är driften avsiktlig?
# - Ska vi behålla eller återställa?

# Steg 4a: Behåll drift (uppdatera state)
terraform apply -refresh-only -auto-approve

# Steg 4b: Återställ drift (uppdatera infra)
terraform apply -auto-approve

# Steg 4c: Import och uppdatera kod
terraform import aws_resource.new RESOURCE_ID
# Uppdatera .tf-filer manuellt
terraform plan   # Verifiera ingen drift
```

---

## Monitoring och alerting

```hcl
# CloudWatch alarm för oväntade ändringar

resource "aws_cloudwatch_event_rule" "config_changes" {
  name        = "detect-config-changes"
  description = "Detect changes to critical resources"

  event_pattern = jsonencode({
    source      = ["aws.config"]
    detail-type = ["Config Rules Compliance Change"]
    detail = {
      messageType = ["ComplianceChangeNotification"]
      newEvaluationResult = {
        complianceType = ["NON_COMPLIANT"]
      }
    }
  })
}

resource "aws_cloudwatch_event_target" "sns" {
  rule      = aws_cloudwatch_event_rule.config_changes.name
  target_id = "SendToSNS"
  arn       = aws_sns_topic.alerts.arn
}
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Drift-detektor | `terraform plan` visar avvikelser mellan kod och verklighet |
| Automatisering | Schemalagd drift-detection i CI/CD var 6:e timme |
| ignore_changes | Lifecycle-block for legitim extern hantering |
| prevent_destroy | Skydda kritiska resurser fran oavsiktlig borttagning |
| Reconciliation | Tre strategier: accept (refresh), reject (apply), import |

## Kom ihag
- Exit code 2 fran `terraform plan -detailed-exitcode` = drift detected
- `terraform apply -refresh-only` accepterar drift och uppdaterar state
- `ignore_changes` for attribut som andras av autoscaling/CI-CD
- `prevent_destroy = true` ger error vid forsok att ta bort resurs
- Kombinera deletion_protection (cloud) med prevent_destroy (Terraform)
''',
        },
    ],
}
