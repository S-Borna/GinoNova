"""
Terraform Part 2 - Modules & Reusability
"""

TASKS_PART2 = [
    {
        "title": "Module Structure & Design",
        "slug": "module-structure",
        "description": "Create reusable Terraform modules",
        "difficulty": "intermediate",
        "xp_reward": 200,
        "estimated_minutes": 55,
        "content": """# Module Structure & Design

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



## Module Basics

```
modules/
+-- vpc/
|   +-- main.tf
|   +-- variables.tf
|   +-- outputs.tf
|   +-- README.md
+-- ec2/
|   +-- main.tf
|   +-- variables.tf
|   +-- outputs.tf
+-- rds/
    +-- main.tf
    +-- variables.tf
    +-- outputs.tf
```

## VPC Module Example

```hcl
# modules/vpc/variables.tf
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "enable_nat_gateway" {
  description = "Enable NAT Gateway"
  type        = bool
  default     = true
}
```

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.environment}-igw"
  }
}

resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = var.availability_zones[count.index]

  map_public_ip_on_launch = true

  tags = {
    Name = "${var.environment}-public-${count.index + 1}"
    Tier = "public"
  }
}

resource "aws_subnet" "private" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index + 10)
  availability_zone = var.availability_zones[count.index]

  tags = {
    Name = "${var.environment}-private-${count.index + 1}"
    Tier = "private"
  }
}

resource "aws_nat_gateway" "main" {
  count         = var.enable_nat_gateway ? 1 : 0
  allocation_id = aws_eip.nat[0].id
  subnet_id     = aws_subnet.public[0].id

  tags = {
    Name = "${var.environment}-nat"
  }
}

resource "aws_eip" "nat" {
  count  = var.enable_nat_gateway ? 1 : 0
  domain = "vpc"
}
```

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.main.cidr_block
}
```

## Using Modules

```hcl
# environments/prod/main.tf
module "vpc" {
  source = "../../modules/vpc"

  vpc_cidr           = "10.0.0.0/16"
  environment        = "production"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  enable_nat_gateway = true
}

module "web_servers" {
  source = "../../modules/ec2"

  instance_count = 3
  instance_type  = "t3.large"
  subnet_ids     = module.vpc.private_subnet_ids
  vpc_id         = module.vpc.vpc_id

  depends_on = [module.vpc]
}

output "vpc_id" {
  value = module.vpc.vpc_id
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    },
    {
        "title": "Module Sources & Versioning",
        "slug": "module-sources",
        "description": "Use modules from various sources with version control",
        "difficulty": "intermediate",
        "xp_reward": 175,
        "estimated_minutes": 45,
        "content": """# Module Sources & Versioning

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



## Local Modules

```hcl
module "vpc" {
  source = "./modules/vpc"
}

module "shared" {
  source = "../shared-modules/networking"
}
```

## Terraform Registry

```hcl
# Official AWS VPC module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Environment = "production"
  }
}

# EKS module
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "my-cluster"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 10
      desired_size = 3

      instance_types = ["t3.large"]
    }
  }
}
```

## Git Sources

```hcl
# HTTPS
module "vpc" {
  source = "git::https://github.com/org/terraform-modules.git//vpc?ref=v1.2.0"
}

# SSH
module "vpc" {
  source = "git::ssh://git@github.com/org/terraform-modules.git//vpc?ref=main"
}

# Specific tag
module "vpc" {
  source = "github.com/org/terraform-modules//vpc?ref=v2.0.0"
}

# Specific commit
module "vpc" {
  source = "github.com/org/terraform-modules//vpc?ref=abc123"
}
```

## S3 Source

```hcl
module "vpc" {
  source = "s3::https://s3-eu-west-1.amazonaws.com/mybucket/modules/vpc.zip"
}
```

## Version Constraints

```hcl
# Exact version
version = "1.2.3"

# Pessimistic constraint (allows 1.2.x)
version = "~> 1.2.0"

# Greater than or equal
version = ">= 1.0.0"

# Range
version = ">= 1.0.0, < 2.0.0"
```

## Private Registry

```hcl
# Terraform Cloud private registry
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = "1.0.0"
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Module Composition Patterns",
        "slug": "module-composition",
        "description": "Advanced patterns for composing modules",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 60,
        "content": """# Module Composition Patterns

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



## Nested Modules

```
infrastructure/
+-- main.tf
+-- modules/
|   +-- application/
|       +-- main.tf
|       +-- modules/
|       |   +-- compute/
|       |   +-- database/
|       |   +-- networking/
|       +-- outputs.tf
```

```hcl
# modules/application/main.tf
module "networking" {
  source = "./modules/networking"

  vpc_cidr    = var.vpc_cidr
  environment = var.environment
}

module "database" {
  source = "./modules/database"

  subnet_ids = module.networking.private_subnet_ids
  vpc_id     = module.networking.vpc_id
}

module "compute" {
  source = "./modules/compute"

  subnet_ids         = module.networking.private_subnet_ids
  db_endpoint        = module.database.endpoint
  security_group_ids = [module.networking.app_sg_id]
}
```

## Factory Pattern

```hcl
# modules/microservice/main.tf
variable "services" {
  type = map(object({
    container_port  = number
    cpu            = number
    memory         = number
    desired_count  = number
    health_check_path = string
  }))
}

resource "aws_ecs_service" "service" {
  for_each = var.services

  name            = each.key
  cluster         = var.cluster_id
  task_definition = aws_ecs_task_definition.task[each.key].arn
  desired_count   = each.value.desired_count

  load_balancer {
    target_group_arn = aws_lb_target_group.tg[each.key].arn
    container_name   = each.key
    container_port   = each.value.container_port
  }
}

# Usage
module "microservices" {
  source = "./modules/microservice"

  cluster_id = aws_ecs_cluster.main.id

  services = {
    api = {
      container_port    = 8080
      cpu              = 256
      memory           = 512
      desired_count    = 3
      health_check_path = "/health"
    }
    worker = {
      container_port    = 8081
      cpu              = 512
      memory           = 1024
      desired_count    = 2
      health_check_path = "/ready"
    }
  }
}
```

## Wrapper Modules

```hcl
# modules/secure-s3-bucket/main.tf
module "bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "3.14.0"

  bucket = var.bucket_name

  # Enforce security defaults
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  versioning = {
    enabled = true
  }

  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm = "aws:kms"
      }
    }
  }

  # Allow overrides
  tags = merge(local.default_tags, var.tags)
}

# Usage - simpler interface
module "logs_bucket" {
  source = "./modules/secure-s3-bucket"

  bucket_name = "my-logs-bucket"
  tags = {
    Purpose = "Application Logs"
  }
}
```

## Module Testing

```hcl
# test/vpc_test.go (Terratest)
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVpcModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        Vars: map[string]interface{}{
            "vpc_cidr":    "10.0.0.0/16",
            "environment": "test",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcId)
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Dynamic Blocks & Expressions",
        "slug": "dynamic-blocks",
        "description": "Master dynamic configuration generation",
        "difficulty": "advanced",
        "xp_reward": 200,
        "estimated_minutes": 50,
        "content": """# Dynamic Blocks & Expressions

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



## Dynamic Blocks

```hcl
variable "ingress_rules" {
  type = list(object({
    port        = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))

  default = [
    {
      port        = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTP"
    },
    {
      port        = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTPS"
    }
  ]
}

resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
      description = ingress.value.description
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

## Nested Dynamic Blocks

```hcl
variable "load_balancer_config" {
  type = object({
    listeners = list(object({
      port     = number
      protocol = string
      actions = list(object({
        type             = string
        target_group_arn = string
      }))
    }))
  })
}

resource "aws_lb_listener" "main" {
  dynamic "default_action" {
    for_each = var.load_balancer_config.listeners[0].actions

    content {
      type             = default_action.value.type
      target_group_arn = default_action.value.target_group_arn
    }
  }
}
```

## For Expressions

```hcl
# Transform list
variable "names" {
  default = ["alice", "bob", "charlie"]
}

locals {
  upper_names = [for name in var.names : upper(name)]
  # Result: ["ALICE", "BOB", "CHARLIE"]

  # With condition
  short_names = [for name in var.names : name if length(name) < 5]
  # Result: ["bob"]
}

# Transform to map
locals {
  name_lengths = {
    for name in var.names : name => length(name)
  }
  # Result: {alice = 5, bob = 3, charlie = 7}
}

# Nested for
variable "users" {
  default = {
    admin = ["read", "write", "delete"]
    user  = ["read"]
  }
}

locals {
  user_permissions = flatten([
    for user, perms in var.users : [
      for perm in perms : {
        user       = user
        permission = perm
      }
    ]
  ])
  # Result: [{user="admin", permission="read"}, ...]
}
```

## Conditional Expressions

```hcl
# Simple ternary
locals {
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
}

# Conditional resource creation
resource "aws_nat_gateway" "main" {
  count = var.enable_nat ? 1 : 0

  allocation_id = aws_eip.nat[0].id
  subnet_id     = aws_subnet.public[0].id
}

# Conditional with for_each
resource "aws_route53_record" "main" {
  for_each = var.create_dns_records ? toset(var.dns_names) : []

  zone_id = var.zone_id
  name    = each.value
  type    = "A"

  alias {
    name    = aws_lb.main.dns_name
    zone_id = aws_lb.main.zone_id
  }
}

# Coalesce for defaults
locals {
  region = coalesce(var.region, "us-east-1")
}

# Try for safe access
locals {
  instance_type = try(var.config.instance_type, "t3.micro")
}
```


> 💡 **Pro Tip:** Kör `terraform validate` efter varje ändring – det fångar syntaxfel utan API-anrop.
"""
    },
    {
        "title": "Functions & Built-in Helpers",
        "slug": "functions-helpers",
        "description": "Master Terraform's built-in functions",
        "difficulty": "intermediate",
        "xp_reward": 175,
        "estimated_minutes": 45,
        "content": """# Functions & Built-in Helpers

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



## String Functions

```hcl
locals {
  # Format
  formatted = format("Hello, %s!", var.name)

  # Join/Split
  joined = join("-", ["foo", "bar", "baz"])  # "foo-bar-baz"
  parts  = split(",", "a,b,c")               # ["a", "b", "c"]

  # Case
  upper_name = upper(var.name)
  lower_name = lower(var.name)
  title_name = title(var.name)

  # Trim
  trimmed = trim("  hello  ", " ")
  prefix_trimmed = trimprefix("helloworld", "hello")
  suffix_trimmed = trimsuffix("helloworld", "world")

  # Replace
  replaced = replace("hello world", "world", "terraform")

  # Regex
  matched = regex("[a-z]+", "hello123")  # "hello"
  all_matches = regexall("[a-z]+", "hello123world")  # ["hello", "world"]

  # Substr
  substring = substr("hello", 0, 3)  # "hel"
}
```

## Collection Functions

```hcl
locals {
  # Length
  list_len = length(["a", "b", "c"])  # 3

  # Element access
  first = element(["a", "b", "c"], 0)  # "a"

  # Contains
  has_item = contains(["a", "b", "c"], "b")  # true

  # Concat
  combined = concat(["a", "b"], ["c", "d"])  # ["a", "b", "c", "d"]

  # Flatten
  flat = flatten([["a", "b"], ["c"]])  # ["a", "b", "c"]

  # Distinct
  unique = distinct(["a", "b", "a", "c"])  # ["a", "b", "c"]

  # Sort
  sorted = sort(["c", "a", "b"])  # ["a", "b", "c"]

  # Reverse
  reversed = reverse(["a", "b", "c"])  # ["c", "b", "a"]

  # Slice
  sliced = slice(["a", "b", "c", "d"], 1, 3)  # ["b", "c"]

  # Lookup
  value = lookup({a = "1", b = "2"}, "a", "default")  # "1"

  # Keys/Values
  map_keys = keys({a = 1, b = 2})  # ["a", "b"]
  map_values = values({a = 1, b = 2})  # [1, 2]

  # Merge
  merged = merge({a = 1}, {b = 2}, {c = 3})

  # Zipmap
  zipped = zipmap(["a", "b"], [1, 2])  # {a = 1, b = 2}
}
```

## Numeric Functions

```hcl
locals {
  # Math
  absolute = abs(-5)      # 5
  ceiling = ceil(4.3)     # 5
  floored = floor(4.7)    # 4
  maximum = max(1, 5, 3)  # 5
  minimum = min(1, 5, 3)  # 1

  # Parse
  parsed_int = parseint("100", 10)  # 100
}
```

## Encoding Functions

```hcl
locals {
  # JSON
  json_encoded = jsonencode({name = "test", count = 5})
  json_decoded = jsondecode("{\"name\":\"test\"}")

  # Base64
  b64_encoded = base64encode("hello")
  b64_decoded = base64decode("aGVsbG8=")

  # URL
  url_encoded = urlencode("hello world")

  # YAML
  yaml_encoded = yamlencode({name = "test"})
  yaml_decoded = yamldecode("name: test")
}
```

## Filesystem Functions

```hcl
locals {
  # Read files
  config = file("${path.module}/config.json")

  # Template
  rendered = templatefile("${path.module}/user_data.tpl", {
    hostname = var.hostname
    packages = var.packages
  })

  # Path
  current_module = path.module
  root_module    = path.root
  current_dir    = path.cwd

  # File exists check
  config_exists = fileexists("${path.module}/config.json")
}
```

## Type Conversion

```hcl
locals {
  # Conversions
  as_string = tostring(123)
  as_number = tonumber("123")
  as_bool   = tobool("true")
  as_list   = tolist(toset(["a", "b", "a"]))
  as_set    = toset(["a", "b", "a"])
  as_map    = tomap({a = 1, b = 2})

  # Try/Can
  safe_value = try(var.optional.nested.value, "default")
  is_valid   = can(regex("^[a-z]+$", var.input))
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    }
]
