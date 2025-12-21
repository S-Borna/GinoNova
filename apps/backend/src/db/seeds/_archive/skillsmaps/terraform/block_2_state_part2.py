# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 2: STATE & MODULES (Part 2)
# =============================================================================
# Nodes 7-8: Modules Basics, Advanced Modules
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_7 = {
    "id": "terraform_node_7",
    "slug": "terraform-modules-basics",
    "title": "Terraform Modules - Reusable Infrastructure",
    "description": "Create and use modules for reusable infrastructure code",
    "node_id": 7,
    "content": r'''
# Terraform Modules - Reusable Infrastructure

## Vad är Modules?

Modules är containers för flera resurser som används tillsammans. De är Terraforms sätt att organisera och återanvända kod.

```
+-------------------------------------------------------------------------+
|                    TERRAFORM MODULE CONCEPT                             |
+-------------------------------------------------------------------------+
|                                                                         |
|  WITHOUT MODULES                        WITH MODULES                   |
|  ---------------                        ------------                   |
|                                                                         |
|  project/                               project/                        |
|  +-- main.tf (500 lines)               +-- main.tf (50 lines)          |
|  +-- variables.tf                       +-- modules/                    |
|  +-- outputs.tf                         |   +-- vpc/                    |
|                                         |   |   +-- main.tf             |
|  • Svårt att underhålla                |   |   +-- variables.tf        |
|  • Ingen återanvändning                |   |   +-- outputs.tf          |
|  • Svårt att testa                     |   +-- ec2/                    |
|                                         |   |   +-- ...                 |
|                                         |   +-- rds/                    |
|                                         |       +-- ...                 |
|                                         |                               |
|                                         • Organiserad kod              |
|                                         • Återanvändbar                |
|                                         • Testbar                      |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Module Types

```
+-------------------------------------------------------------------------+
|                    MODULE HIERARCHY                                     |
+-------------------------------------------------------------------------+
|                                                                         |
|  ROOT MODULE                                                           |
|  -----------                                                           |
|  • Ditt projekt's huvudkatalog                                        |
|  • Varje Terraform-konfiguration har minst en root module             |
|  • Kallar child modules                                               |
|                                                                         |
|  +------------------------------------------------------+             |
|  |  ROOT MODULE (./main.tf)                             |             |
|  |                                                       |             |
|  |  module "vpc" {                                       |             |
|  |    source = "./modules/vpc"                          |             |
|  |  }                                                   |             |
|  |                                                       |             |
|  |  module "eks" {                                       |             |
|  |    source = "./modules/eks"                          |             |
|  |  }                                                   |             |
|  +------------------------------------------------------+             |
|       |                    |                                           |
|       ▼                    ▼                                           |
|  +-------------+     +-------------+                                  |
|  | CHILD MODULE|     | CHILD MODULE|                                  |
|  |   (VPC)     |     |   (EKS)     |                                  |
|  +-------------+     +-------------+                                  |
|                                                                         |
|  MODULE SOURCES                                                        |
|  --------------                                                        |
|  • Local: "./modules/vpc"                                             |
|  • Registry: "hashicorp/vpc/aws"                                      |
|  • GitHub: "github.com/org/module"                                    |
|  • S3: "s3::https://bucket.s3.region.amazonaws.com/module.zip"       |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Creating Your First Module

### Module Structure

```
modules/vpc/
+-- main.tf          # Resources
+-- variables.tf     # Input variables
+-- outputs.tf       # Output values
+-- versions.tf      # Provider requirements
+-- README.md        # Documentation
+-- examples/        # Usage examples
    +-- basic/
        +-- main.tf
```

### modules/vpc/variables.tf

```hcl
variable "name" {
  description = "Name prefix for all resources"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = []
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = []
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
  description = "Additional tags for all resources"
  type        = map(string)
  default     = {}
}
```

### modules/vpc/main.tf

```hcl
# VPC
resource "aws_vpc" "this" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(var.tags, {
    Name = "${var.name}-vpc"
  })
}

# Internet Gateway
resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = merge(var.tags, {
    Name = "${var.name}-igw"
  })
}

# Public Subnets
resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)

  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true

  tags = merge(var.tags, {
    Name = "${var.name}-public-${var.availability_zones[count.index]}"
    Tier = "public"
  })
}

# Private Subnets
resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidrs)

  vpc_id            = aws_vpc.this.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = merge(var.tags, {
    Name = "${var.name}-private-${var.availability_zones[count.index]}"
    Tier = "private"
  })
}

# Elastic IPs for NAT
resource "aws_eip" "nat" {
  count  = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.public_subnet_cidrs)) : 0
  domain = "vpc"

  tags = merge(var.tags, {
    Name = "${var.name}-nat-eip-${count.index + 1}"
  })

  depends_on = [aws_internet_gateway.this]
}

# NAT Gateways
resource "aws_nat_gateway" "this" {
  count = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.public_subnet_cidrs)) : 0

  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = merge(var.tags, {
    Name = "${var.name}-nat-${count.index + 1}"
  })

  depends_on = [aws_internet_gateway.this]
}

# Public Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.this.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.this.id
  }

  tags = merge(var.tags, {
    Name = "${var.name}-public-rt"
  })
}

# Private Route Tables
resource "aws_route_table" "private" {
  count  = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.private_subnet_cidrs)) : length(var.private_subnet_cidrs)
  vpc_id = aws_vpc.this.id

  dynamic "route" {
    for_each = var.enable_nat_gateway ? [1] : []
    content {
      cidr_block     = "0.0.0.0/0"
      nat_gateway_id = aws_nat_gateway.this[var.single_nat_gateway ? 0 : count.index].id
    }
  }

  tags = merge(var.tags, {
    Name = "${var.name}-private-rt-${count.index + 1}"
  })
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  count          = length(var.public_subnet_cidrs)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(var.private_subnet_cidrs)
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[var.single_nat_gateway ? 0 : count.index].id
}
```

### modules/vpc/outputs.tf

```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.this.id
}

output "vpc_cidr_block" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.this.cidr_block
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "nat_gateway_ids" {
  description = "IDs of NAT Gateways"
  value       = aws_nat_gateway.this[*].id
}

output "public_route_table_id" {
  description = "ID of public route table"
  value       = aws_route_table.public.id
}

output "private_route_table_ids" {
  description = "IDs of private route tables"
  value       = aws_route_table.private[*].id
}
```

---

## Using Modules

### Basic Usage

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"

  name               = "production"
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["eu-north-1a", "eu-north-1b", "eu-north-1c"]

  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = false

  tags = {
    Environment = "production"
    Project     = "myapp"
  }
}

# Reference module outputs
resource "aws_instance" "app" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  subnet_id     = module.vpc.private_subnet_ids[0]
}
```

### Multiple Module Instances

```hcl
# Create VPCs for multiple environments
locals {
  environments = {
    dev = {
      cidr_block           = "10.0.0.0/16"
      enable_nat_gateway   = false
      single_nat_gateway   = true
    }
    staging = {
      cidr_block           = "10.1.0.0/16"
      enable_nat_gateway   = true
      single_nat_gateway   = true
    }
    prod = {
      cidr_block           = "10.2.0.0/16"
      enable_nat_gateway   = true
      single_nat_gateway   = false
    }
  }
}

module "vpc" {
  source   = "./modules/vpc"
  for_each = local.environments

  name               = each.key
  cidr_block         = each.value.cidr_block
  availability_zones = data.aws_availability_zones.available.names

  public_subnet_cidrs  = [for i in range(3) : cidrsubnet(each.value.cidr_block, 8, i)]
  private_subnet_cidrs = [for i in range(3) : cidrsubnet(each.value.cidr_block, 8, i + 10)]

  enable_nat_gateway = each.value.enable_nat_gateway
  single_nat_gateway = each.value.single_nat_gateway

  tags = {
    Environment = each.key
  }
}

# Access specific environment VPC
output "prod_vpc_id" {
  value = module.vpc["prod"].vpc_id
}
```

---

## Module Sources

### Local Modules

```hcl
# Relative path
module "vpc" {
  source = "./modules/vpc"
}

# Absolute path (not recommended)
module "vpc" {
  source = "/home/user/terraform/modules/vpc"
}
```

### Terraform Registry

```hcl
# Public registry
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.4.0"

  name = "production-vpc"
  cidr = "10.0.0.0/16"
  # ...
}

# Private registry (Terraform Cloud)
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = "1.0.0"
}
```

### Git Repositories

```hcl
# HTTPS
module "vpc" {
  source = "git::https://github.com/myorg/terraform-modules.git//vpc?ref=v1.0.0"
}

# SSH
module "vpc" {
  source = "git::ssh://git@github.com/myorg/terraform-modules.git//vpc?ref=v1.0.0"
}

# GitHub shorthand
module "vpc" {
  source = "github.com/myorg/terraform-modules//vpc?ref=v1.0.0"
}

# Specific branch
module "vpc" {
  source = "git::https://github.com/myorg/terraform-modules.git//vpc?ref=feature/new-feature"
}
```

### S3 Bucket

```hcl
module "vpc" {
  source = "s3::https://my-terraform-modules.s3.eu-north-1.amazonaws.com/vpc/v1.0.0.zip"
}
```

---

## Module Versioning

```
+-------------------------------------------------------------------------+
|                    MODULE VERSIONING STRATEGY                           |
+-------------------------------------------------------------------------+
|                                                                         |
|  SEMANTIC VERSIONING                                                   |
|  -------------------                                                   |
|                                                                         |
|     v1.2.3                                                             |
|     | | +-- Patch: Bug fixes (backwards compatible)                   |
|     | +---- Minor: New features (backwards compatible)                |
|     +------ Major: Breaking changes                                   |
|                                                                         |
|  VERSION CONSTRAINTS                                                   |
|  -------------------                                                   |
|                                                                         |
|  version = "5.0.0"        # Exact version                             |
|  version = ">= 5.0.0"     # Minimum version                           |
|  version = "~> 5.0"       # >= 5.0.0, < 6.0.0 (recommended)          |
|  version = ">= 5.0, < 6"  # Range                                     |
|                                                                         |
|  BEST PRACTICE                                                         |
|  -------------                                                         |
|  • Production: Pin to specific version or pessimistic (~>)            |
|  • Development: Can use >= for latest features                        |
|  • Test new versions in staging first                                 |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Praktiska Övningar

### Övning 1: Skapa EC2 Module
```hcl
# modules/ec2/main.tf
resource "aws_instance" "this" {
  count         = var.instance_count
  ami           = var.ami_id
  instance_type = var.instance_type
  # ...
}

# Använd modulen
module "web_servers" {
  source         = "./modules/ec2"
  instance_count = 3
  instance_type  = "t3.micro"
  ami_id         = data.aws_ami.latest.id
}
```

### Övning 2: Använd Registry Module
```hcl
# Använd terraform-aws-modules/vpc/aws
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.4.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-north-1a", "eu-north-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
}
```

---

**Nästa Node:** Advanced Modules ->
''',
    "xp_reward": 180,
    "estimated_minutes": 70,
    "prerequisites": ["terraform_node_6"],
    "learning_outcomes": [
        "Förstå module-konceptet",
        "Skapa egna modules",
        "Använda modules från olika källor",
        "Hantera module versioning",
        "Organisera kod med modules"
    ]
}

NODE_8 = {
    "id": "terraform_node_8",
    "slug": "advanced-terraform-modules",
    "title": "Advanced Modules - Composition & Testing",
    "description": "Master advanced module patterns, composition and testing",
    "node_id": 8,
    "content": r'''
# Advanced Modules - Composition & Testing

## Module Composition Patterns

```
+-------------------------------------------------------------------------+
|                    MODULE COMPOSITION PATTERNS                          |
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN 1: LAYERED MODULES                                            |
|  --------------------------                                            |
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |  Application Layer                                               |   |
|  |  module "app" { source = "./modules/app" }                      |   |
|  +---------------------------+-------------------------------------+   |
|                              |                                          |
|  +---------------------------▼-------------------------------------+   |
|  |  Compute Layer                                                   |   |
|  |  module "eks" { source = "./modules/eks" }                      |   |
|  +---------------------------+-------------------------------------+   |
|                              |                                          |
|  +---------------------------▼-------------------------------------+   |
|  |  Network Layer                                                   |   |
|  |  module "vpc" { source = "./modules/vpc" }                      |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
|  PATTERN 2: COMPOSITE MODULES                                          |
|  ---------------------------                                           |
|                                                                         |
|  +-----------------------------------------------------------------+   |
|  |  module "platform" {                                             |   |
|  |    source = "./modules/platform"                                 |   |
|  |    # Internally creates:                                         |   |
|  |    # - VPC                                                       |   |
|  |    # - EKS                                                       |   |
|  |    # - RDS                                                       |   |
|  |    # - Monitoring                                                |   |
|  |  }                                                               |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Module Input Validation

### Complex Validation Rules

```hcl
variable "environment" {
  description = "Environment name"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string

  validation {
    condition     = can(regex("^t3\\.", var.instance_type)) || can(regex("^t3a\\.", var.instance_type))
    error_message = "Instance type must be t3.* or t3a.* for cost optimization."
  }
}

variable "cidr_block" {
  description = "VPC CIDR block"
  type        = string

  validation {
    condition     = can(cidrnetmask(var.cidr_block))
    error_message = "CIDR block must be a valid IPv4 CIDR notation."
  }

  validation {
    condition     = tonumber(split("/", var.cidr_block)[1]) >= 16 && tonumber(split("/", var.cidr_block)[1]) <= 24
    error_message = "CIDR block must have a prefix between /16 and /24."
  }
}

variable "database_config" {
  type = object({
    engine         = string
    engine_version = string
    instance_class = string
    storage_gb     = number
    multi_az       = bool
  })

  validation {
    condition     = contains(["postgres", "mysql", "mariadb"], var.database_config.engine)
    error_message = "Database engine must be postgres, mysql, or mariadb."
  }

  validation {
    condition     = var.database_config.storage_gb >= 20 && var.database_config.storage_gb <= 65536
    error_message = "Storage must be between 20 and 65536 GB."
  }
}
```

### Validation with Preconditions

```hcl
resource "aws_instance" "this" {
  ami           = var.ami_id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture."
    }

    precondition {
      condition     = data.aws_ami.selected.root_device_type == "ebs"
      error_message = "AMI must use EBS root device."
    }

    postcondition {
      condition     = self.public_ip != null || !var.assign_public_ip
      error_message = "Instance should have public IP when assign_public_ip is true."
    }
  }
}
```

---

## Module Outputs - Advanced Patterns

### Conditional Outputs

```hcl
output "load_balancer_dns" {
  description = "DNS name of load balancer (if created)"
  value       = var.create_lb ? aws_lb.this[0].dns_name : null
}

output "database_endpoint" {
  description = "Database endpoint"
  value       = var.create_database ? aws_db_instance.this[0].endpoint : null
  sensitive   = true
}
```

### Complex Output Structures

```hcl
output "vpc_config" {
  description = "Complete VPC configuration"
  value = {
    vpc_id              = aws_vpc.this.id
    vpc_cidr            = aws_vpc.this.cidr_block
    public_subnets = {
      ids   = aws_subnet.public[*].id
      cidrs = aws_subnet.public[*].cidr_block
    }
    private_subnets = {
      ids   = aws_subnet.private[*].id
      cidrs = aws_subnet.private[*].cidr_block
    }
    nat_gateway_ids     = aws_nat_gateway.this[*].id
    availability_zones  = var.availability_zones
  }
}

output "security_groups" {
  description = "Map of security group configurations"
  value = {
    for sg_name, sg in aws_security_group.this : sg_name => {
      id   = sg.id
      arn  = sg.arn
      name = sg.name
    }
  }
}
```

---

## Module Dependencies

### Implicit Dependencies

```hcl
# Module B depends on Module A through reference
module "vpc" {
  source = "./modules/vpc"
  # ...
}

module "eks" {
  source = "./modules/eks"

  vpc_id     = module.vpc.vpc_id        # Implicit dependency
  subnet_ids = module.vpc.private_subnet_ids
}
```

### Explicit Dependencies

```hcl
module "app" {
  source = "./modules/app"

  # Explicit dependency without direct reference
  depends_on = [
    module.database,
    module.secrets
  ]
}
```

### Provider Passing

```hcl
# Root module
provider "aws" {
  region = "eu-north-1"
  alias  = "primary"
}

provider "aws" {
  region = "eu-west-1"
  alias  = "dr"
}

module "primary_vpc" {
  source = "./modules/vpc"

  providers = {
    aws = aws.primary
  }

  # ...
}

module "dr_vpc" {
  source = "./modules/vpc"

  providers = {
    aws = aws.dr
  }

  # ...
}

# In module - providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

---

## Testing Modules

### Terraform Test Framework (1.6+)

```hcl
# tests/vpc_test.tftest.hcl
run "vpc_creates_correctly" {
  command = plan

  variables {
    name               = "test-vpc"
    cidr_block         = "10.0.0.0/16"
    availability_zones = ["eu-north-1a", "eu-north-1b"]
    public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
    private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24"]
  }

  assert {
    condition     = aws_vpc.this.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block is incorrect"
  }

  assert {
    condition     = length(aws_subnet.public) == 2
    error_message = "Should create 2 public subnets"
  }

  assert {
    condition     = length(aws_subnet.private) == 2
    error_message = "Should create 2 private subnets"
  }
}

run "vpc_applies_successfully" {
  command = apply

  variables {
    name               = "test-vpc"
    cidr_block         = "10.0.0.0/16"
    availability_zones = ["eu-north-1a", "eu-north-1b"]
    public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
    private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24"]
  }

  assert {
    condition     = output.vpc_id != null
    error_message = "VPC ID should be set"
  }
}
```

### Running Tests

```bash
# Run all tests
terraform test

# Run specific test file
terraform test -filter=tests/vpc_test.tftest.hcl

# Verbose output
terraform test -verbose
```

### Integration Testing with Terratest

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

    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        Vars: map[string]interface{}{
            "name":               "terratest-vpc",
            "cidr_block":         "10.0.0.0/16",
            "availability_zones": []string{"eu-north-1a", "eu-north-1b"},
            "public_subnet_cidrs":  []string{"10.0.1.0/24", "10.0.2.0/24"},
            "private_subnet_cidrs": []string{"10.0.11.0/24", "10.0.12.0/24"},
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcId)

    publicSubnetIds := terraform.OutputList(t, terraformOptions, "public_subnet_ids")
    assert.Equal(t, 2, len(publicSubnetIds))
}
```

---

## Module Documentation

### README.md Structure

```markdown
# AWS VPC Module

Terraform module for creating AWS VPC with public and private subnets.

## Features

- Multi-AZ deployment
- NAT Gateway support
- Customizable CIDR blocks
- VPC Flow Logs (optional)

## Usage

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.4.0"

  name = "production-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-north-1a", "eu-north-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
}
```

## Requirements

| Name | Version |
|------|---------|
| terraform | >= 1.6.0 |
| aws | >= 5.0 |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| name | VPC name | `string` | n/a | yes |
| cidr_block | VPC CIDR | `string` | `"10.0.0.0/16"` | no |

## Outputs

| Name | Description |
|------|-------------|
| vpc_id | The ID of the VPC |
| public_subnet_ids | List of public subnet IDs |
```

### Auto-generate Documentation

```bash
# Install terraform-docs
brew install terraform-docs

# Generate README
terraform-docs markdown table . > README.md

# Or specific format
terraform-docs markdown document --output-file README.md .
```

---

## Module Publishing

### Terraform Registry Requirements

```
my-module/
+-- README.md           # Required
+-- main.tf             # Required
+-- variables.tf        # Required (can be empty)
+-- outputs.tf          # Required (can be empty)
+-- versions.tf         # Recommended
+-- LICENSE             # Recommended
+-- CHANGELOG.md        # Recommended
+-- examples/
    +-- basic/
        +-- main.tf
```

### Repository Naming Convention

```
terraform-<PROVIDER>-<NAME>
# Examples:
terraform-aws-vpc
terraform-azurerm-virtual-network
terraform-google-network
```

### Versioning with Git Tags

```bash
# Tag a release
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# List tags
git tag -l "v*"
```

---

## Praktiska Övningar

### Övning 1: Composite Module
```hcl
# Skapa module som kombinerar VPC + EKS + RDS
module "platform" {
  source = "./modules/platform"

  name        = "myapp"
  environment = "prod"

  vpc_cidr     = "10.0.0.0/16"
  eks_version  = "1.28"
  db_engine    = "postgres"
}
```

### Övning 2: Module Testing
```hcl
# Skapa test för din VPC module
# tests/vpc_test.tftest.hcl
run "vpc_validation" {
  command = plan

  assert {
    condition     = length(aws_subnet.private) >= 2
    error_message = "Must have at least 2 private subnets for HA"
  }
}
```

### Övning 3: Module Documentation
```bash
# Installera terraform-docs
# Generera dokumentation för din module
terraform-docs markdown table ./modules/vpc > ./modules/vpc/README.md
```

---

**Nästa Node:** Variables & Outputs Deep Dive ->
''',
    "xp_reward": 190,
    "estimated_minutes": 75,
    "prerequisites": ["terraform_node_7"],
    "learning_outcomes": [
        "Tillämpa avancerade module patterns",
        "Validera module inputs",
        "Hantera module dependencies",
        "Testa modules effektivt",
        "Dokumentera och publicera modules"
    ]
}

# Block 2 Part 2 exports
BLOCK_2_PART_2_NODES = [NODE_7, NODE_8]

__all__ = ["NODE_7", "NODE_8", "BLOCK_2_PART_2_NODES"]
