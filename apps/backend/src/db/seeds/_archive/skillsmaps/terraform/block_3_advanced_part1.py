# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 3: ADVANCED PATTERNS (Part 1)
# =============================================================================
# Nodes 9-10: Variables Deep Dive, Outputs & Expressions
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_9 = {
    "id": "terraform_node_9",
    "slug": "terraform-variables-deep-dive",
    "title": "Variables Deep Dive - Dynamic Configurations",
    "description": "Master variable types, validation, and dynamic patterns",
    "node_id": 9,
    "content": r'''
# Variables Deep Dive - Dynamic Configurations

## Variable Architecture

```
+-------------------------------------------------------------------------+
|                    TERRAFORM VARIABLE FLOW                              |
+-------------------------------------------------------------------------+
|                                                                         |
|  INPUT SOURCES (Priority order - highest first)                        |
|  ---------------------------------------------                         |
|                                                                         |
|  1. Command line (-var, -var-file)                                     |
|     terraform apply -var="region=eu-west-1"                            |
|                                                                         |
|  2. *.auto.tfvars files (alphabetical order)                           |
|     prod.auto.tfvars, staging.auto.tfvars                              |
|                                                                         |
|  3. terraform.tfvars file                                              |
|     terraform.tfvars                                                   |
|                                                                         |
|  4. Environment variables (TF_VAR_*)                                   |
|     export TF_VAR_region="eu-north-1"                                  |
|                                                                         |
|  5. Default values in variable block                                   |
|     variable "region" { default = "us-east-1" }                        |
|                                                                         |
|  6. Interactive prompt (if no default)                                 |
|     var.region: _____                                                  |
|                                                                         |
|                                                                         |
|  +-------------+    +-------------+    +-------------+                |
|  |  Variables  |---▶|  Terraform  |---▶|  Resources  |                |
|  |   .tfvars   |    |   Config    |    |   Created   |                |
|  +-------------+    +-------------+    +-------------+                |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Variable Types Deep Dive

### Primitive Types

```hcl
# STRING
variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

# NUMBER
variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 1
}

# BOOL
variable "enable_monitoring" {
  description = "Enable CloudWatch monitoring"
  type        = bool
  default     = true
}

# Usage
resource "aws_instance" "web" {
  count      = var.instance_count
  monitoring = var.enable_monitoring

  tags = {
    Environment = var.environment
  }
}
```

### Collection Types

```hcl
# LIST - Ordered collection
variable "availability_zones" {
  description = "List of AZs"
  type        = list(string)
  default     = ["eu-north-1a", "eu-north-1b", "eu-north-1c"]
}

# Access by index
locals {
  first_az = var.availability_zones[0]
  all_azs  = join(", ", var.availability_zones)
}

# SET - Unique values, unordered
variable "allowed_ips" {
  description = "Set of allowed IP addresses"
  type        = set(string)
  default     = []
}

# Convert list to set (removes duplicates)
locals {
  unique_ips = toset(var.ip_list)
}

# MAP - Key-value pairs
variable "instance_types" {
  description = "Instance types per environment"
  type        = map(string)
  default = {
    dev     = "t3.micro"
    staging = "t3.small"
    prod    = "t3.large"
  }
}

# Access by key
locals {
  selected_type = var.instance_types[var.environment]
}
```

### Structural Types

```hcl
# OBJECT - Fixed structure with named attributes
variable "database_config" {
  description = "Database configuration"
  type = object({
    engine           = string
    engine_version   = string
    instance_class   = string
    allocated_storage = number
    multi_az         = bool
    backup_retention = optional(number, 7)  # Optional with default
  })

  default = {
    engine           = "postgres"
    engine_version   = "15.4"
    instance_class   = "db.t3.micro"
    allocated_storage = 20
    multi_az         = false
  }
}

# Usage
resource "aws_db_instance" "main" {
  engine               = var.database_config.engine
  engine_version       = var.database_config.engine_version
  instance_class       = var.database_config.instance_class
  allocated_storage    = var.database_config.allocated_storage
  multi_az             = var.database_config.multi_az
  backup_retention_period = var.database_config.backup_retention
}

# TUPLE - Fixed-length sequence with specific types
variable "subnet_config" {
  description = "Tuple of [cidr, az, public]"
  type        = tuple([string, string, bool])
  default     = ["10.0.1.0/24", "eu-north-1a", true]
}

# Access by index
locals {
  subnet_cidr = var.subnet_config[0]
  subnet_az   = var.subnet_config[1]
  is_public   = var.subnet_config[2]
}
```

### Complex Nested Types

```hcl
# List of objects
variable "subnets" {
  description = "Subnet configurations"
  type = list(object({
    cidr_block        = string
    availability_zone = string
    public            = bool
    tags              = optional(map(string), {})
  }))

  default = [
    {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "eu-north-1a"
      public            = true
    },
    {
      cidr_block        = "10.0.2.0/24"
      availability_zone = "eu-north-1b"
      public            = true
    },
    {
      cidr_block        = "10.0.11.0/24"
      availability_zone = "eu-north-1a"
      public            = false
    }
  ]
}

# Usage with for_each
resource "aws_subnet" "this" {
  for_each = { for idx, subnet in var.subnets : "${subnet.availability_zone}-${subnet.public}" => subnet }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr_block
  availability_zone       = each.value.availability_zone
  map_public_ip_on_launch = each.value.public

  tags = merge(each.value.tags, {
    Name = "${var.name}-${each.value.public ? "public" : "private"}-${each.value.availability_zone}"
  })
}

# Map of objects
variable "services" {
  description = "Service configurations"
  type = map(object({
    port           = number
    protocol       = string
    health_check   = object({
      path     = string
      interval = number
      timeout  = number
    })
    scaling        = optional(object({
      min_capacity = number
      max_capacity = number
    }))
  }))

  default = {
    api = {
      port     = 8080
      protocol = "HTTP"
      health_check = {
        path     = "/health"
        interval = 30
        timeout  = 5
      }
      scaling = {
        min_capacity = 2
        max_capacity = 10
      }
    }
    web = {
      port     = 80
      protocol = "HTTP"
      health_check = {
        path     = "/"
        interval = 60
        timeout  = 10
      }
    }
  }
}
```

---

## Variable Validation

### Basic Validation

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_count" {
  type = number

  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 100
    error_message = "Instance count must be between 1 and 100."
  }
}
```

### Regex Validation

```hcl
variable "bucket_name" {
  type = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$", var.bucket_name))
    error_message = "Bucket name must be 3-63 characters, lowercase, and start/end with letter or number."
  }
}

variable "email" {
  type = string

  validation {
    condition     = can(regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", var.email))
    error_message = "Must be a valid email address."
  }
}

variable "instance_type" {
  type = string

  validation {
    condition     = can(regex("^(t3|t3a|m5|c5)\\.(micro|small|medium|large|xlarge)$", var.instance_type))
    error_message = "Instance type must be t3, t3a, m5, or c5 family in allowed sizes."
  }
}
```

### Multiple Validations

```hcl
variable "cidr_block" {
  type = string

  validation {
    condition     = can(cidrnetmask(var.cidr_block))
    error_message = "Must be a valid CIDR notation."
  }

  validation {
    condition     = tonumber(split("/", var.cidr_block)[1]) >= 16
    error_message = "CIDR prefix must be /16 or larger (smaller network)."
  }

  validation {
    condition     = tonumber(split("/", var.cidr_block)[1]) <= 24
    error_message = "CIDR prefix must be /24 or smaller (larger network)."
  }
}

variable "password" {
  type      = string
  sensitive = true

  validation {
    condition     = length(var.password) >= 16
    error_message = "Password must be at least 16 characters."
  }

  validation {
    condition     = can(regex("[A-Z]", var.password))
    error_message = "Password must contain at least one uppercase letter."
  }

  validation {
    condition     = can(regex("[a-z]", var.password))
    error_message = "Password must contain at least one lowercase letter."
  }

  validation {
    condition     = can(regex("[0-9]", var.password))
    error_message = "Password must contain at least one number."
  }

  validation {
    condition     = can(regex("[!@#$%^&*]", var.password))
    error_message = "Password must contain at least one special character."
  }
}
```

### Cross-Variable Validation

```hcl
variable "min_instances" {
  type    = number
  default = 1
}

variable "max_instances" {
  type    = number
  default = 10

  validation {
    condition     = var.max_instances >= var.min_instances
    error_message = "max_instances must be greater than or equal to min_instances."
  }
}

# Alternative: Local validation
locals {
  validate_instances = (
    var.max_instances >= var.min_instances
    ? true
    : tobool("max_instances must be >= min_instances")
  )
}
```

---

## Sensitive Variables

```hcl
variable "database_password" {
  description = "Database master password"
  type        = string
  sensitive   = true

  validation {
    condition     = length(var.database_password) >= 16
    error_message = "Password must be at least 16 characters."
  }
}

variable "api_keys" {
  description = "API keys for external services"
  type        = map(string)
  sensitive   = true
}

# Usage - values hidden in plan/apply output
resource "aws_db_instance" "main" {
  password = var.database_password  # Shows as (sensitive value)
}

# Sensitive outputs
output "db_password" {
  value     = var.database_password
  sensitive = true
}
```

---

## Environment Variable Integration

```bash
# Set via environment
export TF_VAR_environment="prod"
export TF_VAR_instance_count=5
export TF_VAR_enable_monitoring=true

# Complex types via JSON
export TF_VAR_tags='{"Environment":"prod","Team":"platform"}'
export TF_VAR_availability_zones='["eu-north-1a","eu-north-1b"]'
```

---

## tfvars Files Organization

```
project/
+-- terraform.tfvars           # Default values (not in git if contains secrets)
+-- dev.tfvars                 # Development environment
+-- staging.tfvars             # Staging environment
+-- prod.tfvars                # Production environment
+-- secrets.auto.tfvars        # Auto-loaded secrets (in .gitignore!)
+-- common.auto.tfvars         # Auto-loaded common values
```

### terraform.tfvars

```hcl
# terraform.tfvars - Default values
project_name = "myapp"
region       = "eu-north-1"

common_tags = {
  ManagedBy = "Terraform"
  Project   = "myapp"
}
```

### Environment-specific tfvars

```hcl
# prod.tfvars
environment    = "prod"
instance_type  = "t3.large"
instance_count = 3
enable_ha      = true

database_config = {
  instance_class = "db.r5.large"
  multi_az       = true
  storage_gb     = 100
}
```

### Usage

```bash
# Apply with specific environment
terraform apply -var-file="prod.tfvars"

# Multiple var files
terraform apply \
  -var-file="common.tfvars" \
  -var-file="prod.tfvars" \
  -var-file="secrets.tfvars"
```

---

## Dynamic Variable Patterns

### Lookup Pattern

```hcl
variable "environment" {
  type = string
}

locals {
  environment_config = {
    dev = {
      instance_type = "t3.micro"
      min_size      = 1
      max_size      = 2
    }
    staging = {
      instance_type = "t3.small"
      min_size      = 2
      max_size      = 4
    }
    prod = {
      instance_type = "t3.large"
      min_size      = 3
      max_size      = 10
    }
  }

  config = local.environment_config[var.environment]
}

resource "aws_autoscaling_group" "web" {
  min_size = local.config.min_size
  max_size = local.config.max_size

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }
}
```

### Conditional Defaults

```hcl
variable "instance_type" {
  type    = string
  default = null  # No default
}

locals {
  # Use provided value or environment-based default
  instance_type = coalesce(
    var.instance_type,
    var.environment == "prod" ? "t3.large" : "t3.micro"
  )
}
```

---

## Praktiska Övningar

### Övning 1: Complex Type Definition
```hcl
# Definiera en variabel för service-konfiguration
variable "services" {
  type = map(object({
    replicas = number
    cpu      = number
    memory   = number
    env_vars = map(string)
  }))
}
```

### Övning 2: Validation Rules
```hcl
# Skapa validation för en S3 bucket-namn
variable "bucket_name" {
  type = string
  # Lägg till validations för:
  # - Längd 3-63 tecken
  # - Endast lowercase, siffror, bindestreck
  # - Börjar/slutar inte med bindestreck
}
```

---

**Nästa Node:** Outputs & Expressions ->
''',
    "xp_reward": 170,
    "estimated_minutes": 65,
    "prerequisites": ["terraform_node_8"],
    "learning_outcomes": [
        "Behärska alla variabeltyper",
        "Implementera komplex validering",
        "Organisera tfvars-filer",
        "Använda dynamiska patterns",
        "Hantera känslig data"
    ]
}

NODE_10 = {
    "id": "terraform_node_10",
    "slug": "terraform-outputs-expressions",
    "title": "Outputs & Expressions - Data Transformation",
    "description": "Master outputs, expressions and data manipulation",
    "node_id": 10,
    "content": r'''
# Outputs & Expressions - Data Transformation

## Output Fundamentals

```
+-------------------------------------------------------------------------+
|                    TERRAFORM OUTPUTS PURPOSE                            |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. EXPOSE VALUES                                                      |
|     +- Show important info after apply                                 |
|        terraform output instance_ip                                    |
|                                                                         |
|  2. CROSS-MODULE COMMUNICATION                                         |
|     +- Pass data between modules                                       |
|        module.vpc.vpc_id                                               |
|                                                                         |
|  3. REMOTE STATE DATA                                                  |
|     +- Share data with other configurations                            |
|        data.terraform_remote_state.networking.outputs.vpc_id           |
|                                                                         |
|  4. INTEGRATION                                                        |
|     +- Output for scripts/CI/CD                                        |
|        terraform output -json | jq .instance_ip.value                  |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Output Types

### Basic Outputs

```hcl
# Simple value
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

# Computed value
output "vpc_cidr" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

# List output
output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}

# Map output
output "subnet_cidrs" {
  description = "Map of subnet names to CIDRs"
  value       = { for s in aws_subnet.public : s.tags.Name => s.cidr_block }
}
```

### Conditional Outputs

```hcl
output "load_balancer_dns" {
  description = "DNS name of load balancer"
  value       = var.create_lb ? aws_lb.main[0].dns_name : null
}

output "database_endpoint" {
  description = "Database endpoint (null if not created)"
  value       = var.create_database ? aws_db_instance.main[0].endpoint : "No database created"
}

# One-liner conditional
output "nat_gateway_ips" {
  value = var.enable_nat_gateway ? aws_eip.nat[*].public_ip : []
}
```

### Sensitive Outputs

```hcl
output "database_password" {
  description = "Database master password"
  value       = random_password.db.result
  sensitive   = true
}

output "api_key" {
  description = "Generated API key"
  value       = aws_api_gateway_api_key.main.value
  sensitive   = true
}

# Access sensitive output
# terraform output -raw database_password
```

### Complex Structured Outputs

```hcl
output "vpc_config" {
  description = "Complete VPC configuration"
  value = {
    id         = aws_vpc.main.id
    cidr_block = aws_vpc.main.cidr_block

    subnets = {
      public = [for s in aws_subnet.public : {
        id                = s.id
        cidr_block        = s.cidr_block
        availability_zone = s.availability_zone
      }]
      private = [for s in aws_subnet.private : {
        id                = s.id
        cidr_block        = s.cidr_block
        availability_zone = s.availability_zone
      }]
    }

    nat_gateways = var.enable_nat_gateway ? aws_nat_gateway.main[*].id : []

    route_tables = {
      public  = aws_route_table.public.id
      private = aws_route_table.private[*].id
    }
  }
}

output "instances" {
  description = "EC2 instance details"
  value = {
    for instance in aws_instance.web :
    instance.tags.Name => {
      id         = instance.id
      public_ip  = instance.public_ip
      private_ip = instance.private_ip
      az         = instance.availability_zone
    }
  }
}
```

---

## Expressions Deep Dive

### For Expressions

```hcl
# Transform list
locals {
  # Input: ["alice", "bob", "carol"]
  upper_names = [for name in var.names : upper(name)]
  # Output: ["ALICE", "BOB", "CAROL"]
}

# Filter list
locals {
  # Input: [{name="web1", env="prod"}, {name="web2", env="dev"}]
  prod_servers = [for s in var.servers : s.name if s.env == "prod"]
  # Output: ["web1"]
}

# List to map
locals {
  # Input: [{name="web1", ip="10.0.0.1"}, {name="web2", ip="10.0.0.2"}]
  server_ips = { for s in var.servers : s.name => s.ip }
  # Output: {web1 = "10.0.0.1", web2 = "10.0.0.2"}
}

# Map transformation
locals {
  # Input: {web = {port = 80}, api = {port = 8080}}
  ports = { for name, config in var.services : name => config.port }
  # Output: {web = 80, api = 8080}
}

# Nested for
locals {
  all_cidrs = flatten([
    for vpc in var.vpcs : [
      for subnet in vpc.subnets : subnet.cidr_block
    ]
  ])
}

# Grouping with ...
locals {
  # Input: [{name="s1", env="prod"}, {name="s2", env="prod"}, {name="s3", env="dev"}]
  servers_by_env = {
    for s in var.servers : s.env => s.name...
  }
  # Output: {prod = ["s1", "s2"], dev = ["s3"]}
}
```

### Splat Expressions

```hcl
# List splat
locals {
  instance_ids = aws_instance.web[*].id
  public_ips   = aws_instance.web[*].public_ip
}

# Nested splat
locals {
  all_enis = aws_instance.web[*].network_interface[*].network_interface_id
}

# Safe access with try
locals {
  first_ip = try(aws_instance.web[0].public_ip, "no-instances")
}
```

### Conditional Expressions

```hcl
# Ternary
locals {
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
}

# Nested conditionals (use sparingly)
locals {
  instance_type = (
    var.environment == "prod" ? "t3.large" :
    var.environment == "staging" ? "t3.medium" :
    "t3.micro"
  )
}

# Conditional resources
resource "aws_eip" "web" {
  count    = var.assign_eip ? 1 : 0
  instance = aws_instance.web.id
}

# Conditional blocks
resource "aws_autoscaling_group" "web" {
  # ...

  dynamic "tag" {
    for_each = var.enable_asg_tags ? var.asg_tags : {}
    content {
      key                 = tag.key
      value               = tag.value
      propagate_at_launch = true
    }
  }
}
```

---

## String Functions & Templates

### String Manipulation

```hcl
locals {
  # Join
  az_string = join(", ", var.availability_zones)
  # "eu-north-1a, eu-north-1b"

  # Split
  parts = split("-", "web-server-01")
  # ["web", "server", "01"]

  # Format
  name = format("%s-%s-%03d", var.project, var.env, var.index)
  # "myapp-prod-001"

  # Replace
  sanitized = replace(var.name, " ", "-")

  # Regex replace
  cleaned = replace(var.input, "/[^a-z0-9]/", "")

  # Upper/Lower
  upper_env = upper(var.environment)
  lower_env = lower(var.environment)

  # Trim
  trimmed = trim(var.input, " ")

  # Substring
  short_id = substr(aws_instance.web.id, 0, 8)
}
```

### Template Functions

```hcl
# templatefile function
resource "aws_instance" "web" {
  user_data = templatefile("${path.module}/userdata.tftpl", {
    hostname    = var.hostname
    environment = var.environment
    packages    = var.packages
    config      = jsonencode(var.app_config)
  })
}

# userdata.tftpl
#!/bin/bash
hostnamectl set-hostname ${hostname}
echo "ENVIRONMENT=${environment}" >> /etc/environment

%{ for pkg in packages ~}
apt-get install -y ${pkg}
%{ endfor ~}

cat > /etc/app/config.json << 'EOF'
${config}
EOF

%{ if environment == "prod" ~}
systemctl enable monitoring-agent
%{ endif ~}
```

### Heredoc Syntax

```hcl
# Standard heredoc
resource "local_file" "config" {
  content = <<EOF
server {
  listen 80;
  server_name ${var.domain};
}
EOF
  filename = "${path.module}/nginx.conf"
}

# Indented heredoc (strips leading whitespace)
resource "local_file" "config" {
  content = <<-EOF
    server {
      listen 80;
      server_name ${var.domain};
    }
  EOF
  filename = "${path.module}/nginx.conf"
}
```

---

## Collection Functions

### List Functions

```hcl
locals {
  # Length
  count = length(var.servers)

  # Element (with wrap-around)
  first = element(var.azs, 0)

  # Concat
  all_subnets = concat(var.public_subnets, var.private_subnets)

  # Flatten
  all_cidrs = flatten([var.vpc1_cidrs, var.vpc2_cidrs])

  # Distinct
  unique = distinct(var.tags)

  # Sort
  sorted = sort(var.names)

  # Reverse
  reversed = reverse(var.names)

  # Contains
  has_prod = contains(var.environments, "prod")

  # Index
  idx = index(var.azs, "eu-north-1a")

  # Slice
  first_two = slice(var.azs, 0, 2)

  # Compact (remove empty strings)
  non_empty = compact(var.strings)

  # Coalesce list (first non-empty)
  primary = coalescelist(var.primary_list, var.fallback_list)
}
```

### Map Functions

```hcl
locals {
  # Keys/Values
  tag_keys   = keys(var.tags)
  tag_values = values(var.tags)

  # Lookup (with default)
  region = lookup(var.region_map, var.environment, "eu-north-1")

  # Merge
  all_tags = merge(var.default_tags, var.custom_tags, {
    ManagedBy = "Terraform"
  })

  # Zipmap
  tag_map = zipmap(var.tag_keys, var.tag_values)
}
```

---

## Type Conversion

```hcl
locals {
  # To string
  str_num = tostring(42)  # "42"

  # To number
  num = tonumber("42")  # 42

  # To bool
  flag = tobool("true")  # true

  # To list
  list_from_set = tolist(toset(["a", "b", "c"]))

  # To set (removes duplicates)
  unique_set = toset(["a", "a", "b"])  # ["a", "b"]

  # To map
  map_val = tomap({
    key1 = "value1"
    key2 = "value2"
  })

  # JSON encode/decode
  json_str = jsonencode(var.config)
  config   = jsondecode(var.json_input)

  # YAML encode/decode
  yaml_str = yamlencode(var.config)
  config   = yamldecode(var.yaml_input)

  # Base64
  encoded = base64encode("hello")
  decoded = base64decode("aGVsbG8=")
}
```

---

## Advanced Patterns

### Null Handling

```hcl
locals {
  # Coalesce - first non-null
  region = coalesce(var.region, var.default_region, "eu-north-1")

  # try - safe access
  port = try(var.config.network.port, 8080)

  # can - check if expression is valid
  is_valid_json = can(jsondecode(var.input))
}

# Conditional with null
resource "aws_security_group_rule" "custom" {
  count = var.custom_port != null ? 1 : 0

  type              = "ingress"
  from_port         = var.custom_port
  to_port           = var.custom_port
  protocol          = "tcp"
  security_group_id = aws_security_group.main.id
  cidr_blocks       = ["0.0.0.0/0"]
}
```

### Dynamic Blocks

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

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

  dynamic "egress" {
    for_each = var.egress_rules
    iterator = rule  # Custom iterator name
    content {
      from_port   = rule.value.port
      to_port     = rule.value.port
      protocol    = rule.value.protocol
      cidr_blocks = rule.value.cidr_blocks
    }
  }
}
```

---

## Praktiska Övningar

### Övning 1: Complex Output
```hcl
# Skapa en strukturerad output för hela infrastrukturen
output "infrastructure" {
  value = {
    vpc        = { ... }
    subnets    = { ... }
    instances  = { ... }
  }
}
```

### Övning 2: For Expression Mastery
```hcl
# Transformera en lista av servers till olika format
variable "servers" {
  default = [
    { name = "web1", env = "prod", ip = "10.0.0.1" },
    { name = "web2", env = "prod", ip = "10.0.0.2" },
    { name = "dev1", env = "dev", ip = "10.0.1.1" }
  ]
}

# 1. Extrahera alla IPs
# 2. Filtrera prod-servrar
# 3. Skapa map: name => ip
# 4. Gruppera per environment
```

---

**Nästa Node:** Workspaces & Environment Management ->
''',
    "xp_reward": 170,
    "estimated_minutes": 65,
    "prerequisites": ["terraform_node_9"],
    "learning_outcomes": [
        "Behärska output-typer och patterns",
        "Använda for expressions effektivt",
        "Tillämpa string och collection functions",
        "Implementera dynamiska blocks",
        "Hantera null och conditional logic"
    ]
}

# Block 3 Part 1 exports
BLOCK_3_PART_1_NODES = [NODE_9, NODE_10]

__all__ = ["NODE_9", "NODE_10", "BLOCK_3_PART_1_NODES"]
