# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 1: FUNDAMENTALS (Part 2)
# =============================================================================
# Nodes 3-4: Providers, Resources & Data Sources
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_3 = {
    "id": "terraform_node_3",
    "slug": "terraform-providers",
    "title": "Terraform Providers - Cloud Integration Mastery",
    "description": "Master provider configuration for AWS, Azure, GCP and more",
    "node_id": 3,
    "content": '''
# Terraform Providers - Cloud Integration Mastery

## Vad är Providers?

Providers är plugins som gör det möjligt för Terraform att interagera med cloud providers, SaaS-tjänster och andra APIer. De ansvarar för att förstå API-interaktioner och exponera resurser.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM PROVIDER ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                      ┌──────────────────────┐                          │
│                      │    TERRAFORM CORE    │                          │
│                      │   (Configuration     │                          │
│                      │    Processing)       │                          │
│                      └──────────┬───────────┘                          │
│                                 │                                       │
│           ┌─────────────────────┼─────────────────────┐                │
│           │                     │                     │                │
│           ▼                     ▼                     ▼                │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐         │
│   │ AWS Provider  │    │ Azure Provider│    │ GCP Provider  │         │
│   │   (hashicorp/ │    │   (hashicorp/ │    │   (hashicorp/ │         │
│   │    aws)       │    │    azurerm)   │    │    google)    │         │
│   └───────┬───────┘    └───────┬───────┘    └───────┬───────┘         │
│           │                     │                     │                │
│           ▼                     ▼                     ▼                │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐         │
│   │    AWS API    │    │   Azure API   │    │   GCP API     │         │
│   │               │    │               │    │               │         │
│   │  EC2, S3,     │    │  VMs, Storage │    │  GCE, GCS,    │         │
│   │  RDS, etc     │    │  SQL, etc     │    │  BigQuery     │         │
│   └───────────────┘    └───────────────┘    └───────────────┘         │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     OTHER PROVIDERS                              │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐       │   │
│  │  │Kuberne-│ │Docker  │ │GitHub  │ │DataDog │ │PagerDuty       │   │
│  │  │tes     │ │        │ │        │ │        │ │        │       │   │
│  │  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Provider Registry

Terraform Registry är den officiella källan för providers:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROVIDER TIERS                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  OFFICIAL (HashiCorp)                                                   │
│  ────────────────────                                                   │
│  • hashicorp/aws        AWS Cloud Platform                             │
│  • hashicorp/azurerm    Microsoft Azure                                │
│  • hashicorp/google     Google Cloud Platform                          │
│  • hashicorp/kubernetes Kubernetes                                     │
│  • hashicorp/vault      HashiCorp Vault                                │
│  • hashicorp/consul     HashiCorp Consul                               │
│                                                                         │
│  VERIFIED (Partner-maintained, HashiCorp-verified)                     │
│  ────────────────────────────────────────────────────────────────────  │
│  • datadog/datadog      Monitoring & APM                               │
│  • cloudflare/cloudflare CDN & DNS                                     │
│  • newrelic/newrelic    Observability                                  │
│  • pagerduty/pagerduty  Incident Management                            │
│                                                                         │
│  COMMUNITY (Third-party maintained)                                     │
│  ─────────────────────────────────                                      │
│  • Tusentals tillgängliga                                              │
│  • Varierande kvalitet                                                 │
│  • Granska före användning                                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Provider Configuration

### Basic Provider Setup

```hcl
# terraform.tf - Provider requirements
terraform {
  required_version = ">= 1.6.0"

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
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.24"
    }
  }
}
```

### Version Constraints

```hcl
# Version constraint syntax
version = "5.0.0"      # Exact version
version = ">= 5.0.0"   # Minimum version
version = "~> 5.0"     # >= 5.0, < 6.0 (Pessimistic)
version = ">= 5.0, < 6.0"  # Range
version = "!= 5.1.0"   # Exclude version

# Best practice: Pessimistic constraint
required_providers {
  aws = {
    source  = "hashicorp/aws"
    version = "~> 5.31"  # >= 5.31.0, < 6.0.0
  }
}
```

---

## AWS Provider Deep Dive

### Basic Configuration

```hcl
provider "aws" {
  region = "eu-north-1"

  # Authentication (flera metoder)
  # 1. Environment variables (recommended)
  # AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

  # 2. Shared credentials file
  shared_config_files      = ["~/.aws/config"]
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "production"

  # 3. IAM Role (för EC2/ECS)
  # Automatic med instance metadata

  # 4. Explicit credentials (UNDVIK!)
  # access_key = "AKIAXXXXXXXX"
  # secret_key = "xxxxxxxx"
}
```

### Advanced AWS Configuration

```hcl
provider "aws" {
  region = var.aws_region

  # Assume Role (cross-account)
  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/TerraformRole"
    session_name = "TerraformSession"
    external_id  = var.external_id
  }

  # Default tags för alla resurser
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
      Team        = var.team
    }
  }

  # Retry configuration
  retry_mode  = "standard"
  max_retries = 3

  # Custom endpoints (localstack, mocking)
  endpoints {
    s3       = var.s3_endpoint
    dynamodb = var.dynamodb_endpoint
  }

  # Skip validation (för testing)
  skip_credentials_validation = var.skip_validation
  skip_metadata_api_check     = var.skip_validation
  skip_region_validation      = var.skip_validation
}
```

### Multiple AWS Regions

```hcl
# Default provider
provider "aws" {
  region = "eu-north-1"
  alias  = "stockholm"
}

# Additional region
provider "aws" {
  region = "eu-west-1"
  alias  = "ireland"
}

provider "aws" {
  region = "us-east-1"
  alias  = "virginia"
}

# Resource med specifik provider
resource "aws_s3_bucket" "eu_bucket" {
  provider = aws.stockholm
  bucket   = "my-eu-bucket"
}

resource "aws_s3_bucket" "us_bucket" {
  provider = aws.virginia
  bucket   = "my-us-bucket"
}

# S3 replication mellan regioner
resource "aws_s3_bucket_replication_configuration" "replication" {
  provider = aws.stockholm
  bucket   = aws_s3_bucket.eu_bucket.id
  role     = aws_iam_role.replication.arn

  rule {
    destination {
      bucket = aws_s3_bucket.us_bucket.arn
    }
    status = "Enabled"
  }
}
```

### Cross-Account Setup

```hcl
# Account A - Source account
provider "aws" {
  region = "eu-north-1"
  alias  = "source"
}

# Account B - Target account (assume role)
provider "aws" {
  region = "eu-north-1"
  alias  = "target"

  assume_role {
    role_arn = "arn:aws:iam::${var.target_account_id}:role/TerraformCrossAccountRole"
  }
}

# Create VPC in source account
resource "aws_vpc" "source_vpc" {
  provider   = aws.source
  cidr_block = "10.0.0.0/16"
}

# Create VPC in target account
resource "aws_vpc" "target_vpc" {
  provider   = aws.target
  cidr_block = "10.1.0.0/16"
}

# VPC Peering across accounts
resource "aws_vpc_peering_connection" "peer" {
  provider      = aws.source
  vpc_id        = aws_vpc.source_vpc.id
  peer_vpc_id   = aws_vpc.target_vpc.id
  peer_owner_id = var.target_account_id
  auto_accept   = false
}

resource "aws_vpc_peering_connection_accepter" "peer" {
  provider                  = aws.target
  vpc_peering_connection_id = aws_vpc_peering_connection.peer.id
  auto_accept               = true
}
```

---

## Azure Provider Configuration

```hcl
# Azure Provider
provider "azurerm" {
  features {
    # Key Vault behavior
    key_vault {
      purge_soft_delete_on_destroy    = false
      recover_soft_deleted_key_vaults = true
    }

    # Resource Group behavior
    resource_group {
      prevent_deletion_if_contains_resources = true
    }

    # Virtual Machine behavior
    virtual_machine {
      delete_os_disk_on_deletion     = true
      graceful_shutdown              = true
      skip_shutdown_and_force_delete = false
    }
  }

  # Authentication
  subscription_id = var.azure_subscription_id
  tenant_id       = var.azure_tenant_id

  # Service Principal (CI/CD)
  client_id       = var.azure_client_id
  client_secret   = var.azure_client_secret

  # Or use Managed Identity
  use_msi = true
}

# Multiple subscriptions
provider "azurerm" {
  alias           = "production"
  subscription_id = var.prod_subscription_id
  features {}
}

provider "azurerm" {
  alias           = "development"
  subscription_id = var.dev_subscription_id
  features {}
}
```

---

## Google Cloud Provider

```hcl
# GCP Provider
provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
  zone    = var.gcp_zone

  # Authentication
  # 1. Application Default Credentials
  # gcloud auth application-default login

  # 2. Service Account Key
  credentials = file(var.gcp_credentials_file)

  # 3. Workload Identity (recommended för GKE)
  # Automatic

  # Batching (performance optimization)
  batching {
    enable_batching = true
  }
}

# Google Beta Provider (för nya features)
provider "google-beta" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# Multiple projects
provider "google" {
  alias   = "networking"
  project = var.networking_project_id
  region  = var.gcp_region
}

# Resurser i shared VPC
resource "google_compute_network" "shared_vpc" {
  provider = google.networking
  name     = "shared-vpc"
}
```

---

## Kubernetes Provider

```hcl
# Kubernetes Provider - EKS
provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority[0].data)

  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", var.cluster_name]
  }
}

# Kubernetes Provider - GKE
provider "kubernetes" {
  host                   = "https://${google_container_cluster.primary.endpoint}"
  cluster_ca_certificate = base64decode(google_container_cluster.primary.master_auth[0].cluster_ca_certificate)
  token                  = data.google_client_config.default.access_token
}

# Kubernetes Provider - Local kubeconfig
provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "my-cluster"
}

# Helm Provider (för charts)
provider "helm" {
  kubernetes {
    host                   = data.aws_eks_cluster.cluster.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority[0].data)

    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      command     = "aws"
      args        = ["eks", "get-token", "--cluster-name", var.cluster_name]
    }
  }
}
```

---

## Provider Dependency Management

```hcl
# providers.tf med dependency chain
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.24"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.12"
    }
  }
}

# AWS provider först
provider "aws" {
  region = var.region
}

# EKS cluster data (beroende på AWS)
data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_name
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_name
}

# Kubernetes provider (beroende på EKS)
provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority[0].data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}

# Helm provider (beroende på Kubernetes)
provider "helm" {
  kubernetes {
    host                   = data.aws_eks_cluster.cluster.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority[0].data)
    token                  = data.aws_eks_cluster_auth.cluster.token
  }
}
```

---

## Provider Debugging

```bash
# Enable debug logging
export TF_LOG=DEBUG
export TF_LOG_PATH="terraform.log"

# Provider-specific logging
export TF_LOG_PROVIDER=DEBUG

# AWS specific
export AWS_DEBUG=true

# Show provider versions
terraform providers

# Lock provider versions
terraform providers lock \\
  -platform=linux_amd64 \\
  -platform=darwin_amd64 \\
  -platform=darwin_arm64

# Mirror providers (air-gapped environments)
terraform providers mirror /path/to/mirror
```

---

## Praktiska Övningar

### Övning 1: Multi-Provider Setup
```hcl
# Konfigurera AWS + Cloudflare
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

# AWS ALB + Cloudflare DNS
resource "aws_lb" "main" {
  name               = "main-lb"
  load_balancer_type = "application"
  subnets            = var.subnet_ids
}

resource "cloudflare_record" "app" {
  zone_id = var.cloudflare_zone_id
  name    = "app"
  value   = aws_lb.main.dns_name
  type    = "CNAME"
  proxied = true
}
```

### Övning 2: Cross-Region DR
```hcl
# Primary region
provider "aws" {
  region = "eu-north-1"
  alias  = "primary"
}

# DR region
provider "aws" {
  region = "eu-west-1"
  alias  = "dr"
}

# RDS med read replica
resource "aws_db_instance" "primary" {
  provider             = aws.primary
  identifier           = "mydb-primary"
  # ...
}

resource "aws_db_instance" "replica" {
  provider             = aws.dr
  identifier           = "mydb-replica"
  replicate_source_db  = aws_db_instance.primary.arn
}
```

---

**Nästa Node:** Resources & Data Sources →
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["terraform_node_2"],
    "learning_outcomes": [
        "Förstå provider-arkitekturen",
        "Konfigurera AWS, Azure och GCP providers",
        "Hantera multi-region och cross-account setups",
        "Implementera provider dependencies",
        "Debugga provider-problem"
    ]
}

NODE_4 = {
    "id": "terraform_node_4",
    "slug": "resources-data-sources",
    "title": "Resources & Data Sources - Infrastructure Building Blocks",
    "description": "Master resource lifecycle and data source usage patterns",
    "node_id": 4,
    "content": '''
# Resources & Data Sources - Infrastructure Building Blocks

## Resources vs Data Sources

```
┌─────────────────────────────────────────────────────────────────────────┐
│              RESOURCES vs DATA SOURCES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  RESOURCES                              DATA SOURCES                    │
│  ─────────                              ────────────                    │
│                                                                         │
│  ┌─────────────────────┐               ┌─────────────────────┐         │
│  │  CREATE / UPDATE    │               │    READ ONLY        │         │
│  │  / DELETE           │               │                     │         │
│  └─────────────────────┘               └─────────────────────┘         │
│                                                                         │
│  resource "aws_instance"               data "aws_ami" "latest"         │
│  {                                      {                               │
│    ami = "ami-xxx"                       most_recent = true            │
│    instance_type = "t3"                  filter {...}                  │
│  }                                      }                               │
│                                                                         │
│  • Managed by Terraform                • Query existing resources      │
│  • Stored in state                     • Read at plan time             │
│  • Full lifecycle control              • No state tracking             │
│  • Changes applied                     • Reference external data       │
│                                                                         │
│  Use cases:                            Use cases:                       │
│  • Create new infrastructure           • Lookup AMI IDs                │
│  • Modify existing resources           • Get VPC/Subnet IDs            │
│  • Destroy when removed                • Read secrets                  │
│                                         • Query account info           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Resource Fundamentals

### Basic Resource Syntax

```hcl
# resource "<PROVIDER>_<TYPE>" "<LOCAL_NAME>" { ... }
resource "aws_instance" "web_server" {
  # Required arguments
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  # Optional arguments
  key_name               = "my-key"
  vpc_security_group_ids = [aws_security_group.web.id]
  subnet_id              = aws_subnet.public.id

  # Nested blocks
  root_block_device {
    volume_size           = 20
    volume_type           = "gp3"
    encrypted             = true
    delete_on_termination = true
  }

  # Metadata
  tags = {
    Name        = "web-server"
    Environment = var.environment
  }
}
```

### Resource Attributes

```hcl
# Referera till resource attributes
# Format: <TYPE>.<NAME>.<ATTRIBUTE>

# Computed attributes (efter creation)
output "instance_id" {
  value = aws_instance.web_server.id
}

output "public_ip" {
  value = aws_instance.web_server.public_ip
}

output "arn" {
  value = aws_instance.web_server.arn
}

# Nested attributes
output "root_volume_id" {
  value = aws_instance.web_server.root_block_device[0].volume_id
}
```

---

## Resource Meta-Arguments

### count - Multiple Identical Resources

```hcl
# Skapa 3 identiska instanser
resource "aws_instance" "web" {
  count         = 3
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  tags = {
    Name = "web-server-${count.index + 1}"
  }
}

# Referera till count resources
output "instance_ids" {
  value = aws_instance.web[*].id  # Alla IDs
}

output "first_instance" {
  value = aws_instance.web[0].id  # Första
}

# Conditional med count
resource "aws_eip" "web" {
  count    = var.create_eip ? length(aws_instance.web) : 0
  instance = aws_instance.web[count.index].id
}
```

### for_each - Resources from Collection

```hcl
# for_each med map
variable "instances" {
  default = {
    web     = { type = "t3.micro", az = "eu-north-1a" }
    api     = { type = "t3.small", az = "eu-north-1b" }
    worker  = { type = "t3.medium", az = "eu-north-1c" }
  }
}

resource "aws_instance" "servers" {
  for_each = var.instances

  ami               = data.aws_ami.latest.id
  instance_type     = each.value.type
  availability_zone = each.value.az

  tags = {
    Name = each.key
    Type = each.value.type
  }
}

# Referera till for_each resources
output "web_instance_id" {
  value = aws_instance.servers["web"].id
}

output "all_ips" {
  value = { for k, v in aws_instance.servers : k => v.public_ip }
}

# for_each med set
resource "aws_iam_user" "devs" {
  for_each = toset(["alice", "bob", "carol"])
  name     = each.key
}
```

### depends_on - Explicit Dependencies

```hcl
# Implicit dependency (genom reference)
resource "aws_instance" "web" {
  subnet_id = aws_subnet.public.id  # Implicit depends on subnet
}

# Explicit dependency (utan reference)
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  # Explicit dependency
  depends_on = [
    aws_internet_gateway.main,  # Vänta på IGW
    aws_route_table.public,     # Vänta på routes
  ]
}

# Module dependency
module "app" {
  source = "./modules/app"

  depends_on = [module.networking]
}
```

### lifecycle - Control Resource Behavior

```hcl
resource "aws_instance" "critical" {
  ami           = data.aws_ami.latest.id
  instance_type = var.instance_type

  lifecycle {
    # Prevent accidental destruction
    prevent_destroy = true

    # Create new before destroying old
    create_before_destroy = true

    # Ignore external changes
    ignore_changes = [
      ami,            # Ignore AMI updates
      tags["LastModified"],
      user_data,
    ]

    # Replace when specific conditions
    replace_triggered_by = [
      aws_launch_template.main.latest_version,
    ]

    # Preconditions (Terraform 1.2+)
    precondition {
      condition     = var.instance_type != "t2.micro"
      error_message = "t2.micro is not allowed in production."
    }

    # Postconditions
    postcondition {
      condition     = self.public_ip != null
      error_message = "Instance must have a public IP."
    }
  }
}
```

### provisioners - Last Resort

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  # Local-exec - körs på maskinen som kör Terraform
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> inventory.txt"
  }

  # Remote-exec - körs på resursen
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx",
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }

  # File provisioner
  provisioner "file" {
    source      = "config/nginx.conf"
    destination = "/tmp/nginx.conf"

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }

  # On-destroy provisioner
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Destroying ${self.id}' >> destroy.log"
  }
}
```

---

## Data Sources

### Common Data Source Patterns

```hcl
# AWS AMI Lookup
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

# AWS Availability Zones
data "aws_availability_zones" "available" {
  state = "available"

  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

# AWS Caller Identity
data "aws_caller_identity" "current" {}

# AWS Region
data "aws_region" "current" {}

# Usage
resource "aws_instance" "web" {
  ami               = data.aws_ami.amazon_linux.id
  instance_type     = "t3.micro"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    AccountId = data.aws_caller_identity.current.account_id
    Region    = data.aws_region.current.name
  }
}
```

### VPC and Subnet Lookups

```hcl
# Lookup existing VPC
data "aws_vpc" "main" {
  filter {
    name   = "tag:Name"
    values = ["production-vpc"]
  }
}

# Alternative: by ID
data "aws_vpc" "by_id" {
  id = "vpc-12345678"
}

# Lookup subnets
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.main.id]
  }

  tags = {
    Tier = "private"
  }
}

# Get subnet details
data "aws_subnet" "private" {
  for_each = toset(data.aws_subnets.private.ids)
  id       = each.value
}

# Usage med Auto Scaling
resource "aws_autoscaling_group" "web" {
  vpc_zone_identifier = data.aws_subnets.private.ids
  # ...
}
```

### Secrets and Parameters

```hcl
# AWS Secrets Manager
data "aws_secretsmanager_secret" "db_creds" {
  name = "production/database/credentials"
}

data "aws_secretsmanager_secret_version" "db_creds" {
  secret_id = data.aws_secretsmanager_secret.db_creds.id
}

locals {
  db_credentials = jsondecode(data.aws_secretsmanager_secret_version.db_creds.secret_string)
}

# AWS SSM Parameter Store
data "aws_ssm_parameter" "api_key" {
  name            = "/production/api/key"
  with_decryption = true
}

# Usage
resource "aws_db_instance" "main" {
  username = local.db_credentials.username
  password = local.db_credentials.password
}
```

### External Data Source

```hcl
# Call external program
data "external" "git_info" {
  program = ["bash", "-c", <<-EOF
    echo '{"commit": "'$(git rev-parse HEAD)'", "branch": "'$(git branch --show-current)'"}'
  EOF
  ]
}

# Usage
resource "aws_instance" "web" {
  tags = {
    GitCommit = data.external.git_info.result.commit
    GitBranch = data.external.git_info.result.branch
  }
}

# HTTP Data Source
data "http" "my_ip" {
  url = "https://api.ipify.org?format=json"
}

locals {
  my_ip = jsondecode(data.http.my_ip.response_body).ip
}
```

### Template File Data Source

```hcl
# userdata.tftpl template
# #!/bin/bash
# hostname ${hostname}
# echo "Environment: ${environment}" >> /etc/environment
# %{ for pkg in packages ~}
# apt-get install -y ${pkg}
# %{ endfor ~}

data "template_file" "userdata" {
  template = file("${path.module}/userdata.tftpl")

  vars = {
    hostname    = var.hostname
    environment = var.environment
    packages    = join(" ", var.packages)
  }
}

# Modern approach: templatefile function
resource "aws_instance" "web" {
  user_data = templatefile("${path.module}/userdata.tftpl", {
    hostname    = var.hostname
    environment = var.environment
    packages    = var.packages
  })
}
```

---

## Resource Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DEPENDENCY GRAPH EXAMPLE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                      ┌────────────────┐                                │
│                      │     VPC        │                                │
│                      │ aws_vpc.main   │                                │
│                      └───────┬────────┘                                │
│                              │                                          │
│            ┌─────────────────┼─────────────────┐                       │
│            │                 │                 │                       │
│            ▼                 ▼                 ▼                       │
│   ┌────────────────┐ ┌────────────────┐ ┌────────────────┐            │
│   │    Subnet A    │ │    Subnet B    │ │ Internet GW    │            │
│   │ aws_subnet.a   │ │ aws_subnet.b   │ │ aws_igw.main   │            │
│   └───────┬────────┘ └───────┬────────┘ └───────┬────────┘            │
│           │                  │                  │                      │
│           │                  │                  │                      │
│           └──────────┬───────┴──────────────────┘                      │
│                      │                                                  │
│                      ▼                                                  │
│            ┌─────────────────────┐                                     │
│            │    Route Table      │                                     │
│            │ aws_route_table.pub │                                     │
│            └──────────┬──────────┘                                     │
│                       │                                                 │
│                       ▼                                                 │
│            ┌─────────────────────┐                                     │
│            │   Security Group    │                                     │
│            │ aws_security_group  │                                     │
│            └──────────┬──────────┘                                     │
│                       │                                                 │
│                       ▼                                                 │
│            ┌─────────────────────┐                                     │
│            │    EC2 Instance     │                                     │
│            │ aws_instance.web    │                                     │
│            └─────────────────────┘                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

```bash
# Visualize dependency graph
terraform graph | dot -Tpng > graph.png

# Show in terminal
terraform graph
```

---

## Praktiska Övningar

### Övning 1: count vs for_each
```hcl
# Scenario: Skapa IAM users

# Med count (problem: index-baserad)
resource "aws_iam_user" "count_users" {
  count = length(var.usernames)
  name  = var.usernames[count.index]
}

# Med for_each (bättre: key-baserad)
resource "aws_iam_user" "foreach_users" {
  for_each = toset(var.usernames)
  name     = each.key
}

# Varför for_each är bättre:
# - Om "bob" tas bort från mitten av listan
#   count: Alla efter "bob" får nya index, destruktiva ändringar
#   for_each: Endast "bob" påverkas
```

### Övning 2: Data Source Pipeline
```hcl
# Hämta senaste golden AMI baserat på tags
data "aws_ami" "golden" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "tag:Environment"
    values = [var.environment]
  }

  filter {
    name   = "tag:Validated"
    values = ["true"]
  }
}

# Hämta secrets
data "aws_secretsmanager_secret_version" "app" {
  secret_id = "${var.environment}/app/config"
}

# Deploy med data
resource "aws_instance" "app" {
  ami = data.aws_ami.golden.id

  user_data = base64encode(jsonencode({
    config = jsondecode(data.aws_secretsmanager_secret_version.app.secret_string)
  }))
}
```

### Övning 3: Lifecycle Management
```hcl
# Blue-green deployment pattern
resource "aws_launch_template" "app" {
  name_prefix   = "app-"
  image_id      = var.ami_id
  instance_type = var.instance_type

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "app" {
  name = "${var.app_name}-${aws_launch_template.app.latest_version}"

  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }

  lifecycle {
    create_before_destroy = true
  }
}
```

---

**Nästa Node:** State Management →
''',
    "xp_reward": 170,
    "estimated_minutes": 65,
    "prerequisites": ["terraform_node_3"],
    "learning_outcomes": [
        "Förstå skillnaden mellan resources och data sources",
        "Behärska meta-arguments (count, for_each, lifecycle)",
        "Använda data sources effektivt",
        "Hantera resource dependencies",
        "Implementera avancerade patterns"
    ]
}

# Block 1 Part 2 exports
BLOCK_1_PART_2_NODES = [NODE_3, NODE_4]

__all__ = ["NODE_3", "NODE_4", "BLOCK_1_PART_2_NODES"]
