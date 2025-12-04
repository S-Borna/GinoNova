"""
Terraform Part 4 - Production & Best Practices
"""

TASKS_PART4 = [
    {
        "title": "Testing Terraform Code",
        "slug": "terraform-testing",
        "description": "Test infrastructure code with Terratest and native testing",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 55,
        "content": """# Testing Terraform Code

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│   ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐          │
│   │  Write │────▶│  Plan  │────▶│ Review │────▶│ Apply  │          │
│   │   HCL  │     │        │     │        │     │        │          │
│   └────────┘     └────────┘     └────────┘     └────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt  
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Native Terraform Testing (1.6+)

```hcl
# tests/vpc_test.tftest.hcl
provider "aws" {
  region = "us-east-1"
}

variables {
  vpc_cidr    = "10.0.0.0/16"
  environment = "test"
}

run "create_vpc" {
  command = apply

  assert {
    condition     = aws_vpc.main.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block did not match expected"
  }

  assert {
    condition     = aws_vpc.main.enable_dns_hostnames == true
    error_message = "DNS hostnames should be enabled"
  }
}

run "validate_subnets" {
  command = apply

  assert {
    condition     = length(aws_subnet.private) == 3
    error_message = "Expected 3 private subnets"
  }

  assert {
    condition     = length(aws_subnet.public) == 3
    error_message = "Expected 3 public subnets"
  }
}
```

```bash
# Run tests
terraform test

# Run specific test file
terraform test -filter=tests/vpc_test.tftest.hcl

# Verbose output
terraform test -verbose
```

## Terratest (Go)

```go
// test/vpc_test.go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/gruntwork-io/terratest/modules/aws"
    "github.com/stretchr/testify/assert"
)

func TestVpcModule(t *testing.T) {
    t.Parallel()

    awsRegion := "us-east-1"

    terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
        TerraformDir: "../modules/vpc",

        Vars: map[string]interface{}{
            "vpc_cidr":    "10.0.0.0/16",
            "environment": "test",
            "availability_zones": []string{
                "us-east-1a",
                "us-east-1b",
            },
        },

        EnvVars: map[string]string{
            "AWS_DEFAULT_REGION": awsRegion,
        },
    })

    // Clean up after test
    defer terraform.Destroy(t, terraformOptions)

    // Deploy infrastructure
    terraform.InitAndApply(t, terraformOptions)

    // Get outputs
    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    publicSubnetIds := terraform.OutputList(t, terraformOptions, "public_subnet_ids")
    privateSubnetIds := terraform.OutputList(t, terraformOptions, "private_subnet_ids")

    // Assertions
    assert.NotEmpty(t, vpcId)
    assert.Len(t, publicSubnetIds, 2)
    assert.Len(t, privateSubnetIds, 2)

    // Verify VPC exists
    vpc := aws.GetVpcById(t, vpcId, awsRegion)
    assert.Equal(t, "10.0.0.0/16", *vpc.CidrBlock)

    // Verify subnets
    for _, subnetId := range publicSubnetIds {
        subnet := aws.GetSubnetById(t, subnetId, awsRegion)
        assert.True(t, *subnet.MapPublicIpOnLaunch)
    }
}

func TestEc2Instance(t *testing.T) {
    t.Parallel()

    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/ec2",
        Vars: map[string]interface{}{
            "instance_type": "t3.micro",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    instanceId := terraform.Output(t, terraformOptions, "instance_id")
    publicIp := terraform.Output(t, terraformOptions, "public_ip")

    // Test HTTP endpoint
    url := fmt.Sprintf("http://%s:80", publicIp)
    http_helper.HttpGetWithRetry(t, url, nil, 200, "OK", 30, 5*time.Second)
}
```

## Unit Testing with Mocks

```hcl
# tests/unit/mock_providers.tf
mock_provider "aws" {
  mock_resource "aws_vpc" {
    defaults = {
      id         = "vpc-mock123"
      cidr_block = "10.0.0.0/16"
    }
  }

  mock_resource "aws_subnet" {
    defaults = {
      id                = "subnet-mock123"
      availability_zone = "us-east-1a"
    }
  }
}

# tests/unit/main_test.tftest.hcl
run "unit_test_vpc_naming" {
  command = plan

  providers = {
    aws = mock_provider.aws
  }

  assert {
    condition     = aws_vpc.main.tags["Name"] == "test-vpc"
    error_message = "VPC name tag incorrect"
  }
}
```

## Contract Testing

```hcl
# tests/contract/outputs_test.tftest.hcl
run "verify_output_contract" {
  command = plan

  # Verify required outputs exist and have correct types
  assert {
    condition     = can(output.vpc_id)
    error_message = "vpc_id output must be defined"
  }

  assert {
    condition     = can(output.private_subnet_ids[0])
    error_message = "private_subnet_ids must be a list"
  }

  assert {
    condition     = can(tonumber(output.nat_gateway_count))
    error_message = "nat_gateway_count must be a number"
  }
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Security Best Practices",
        "slug": "security-practices",
        "description": "Secure Terraform configurations and secrets management",
        "difficulty": "advanced",
        "xp_reward": 250,
        "estimated_minutes": 60,
        "content": """# Security Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│   ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐          │
│   │  Write │────▶│  Plan  │────▶│ Review │────▶│ Apply  │          │
│   │   HCL  │     │        │     │        │     │        │          │
│   └────────┘     └────────┘     └────────┘     └────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt  
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Secrets Management

```hcl
# DON'T: Hardcode secrets
resource "aws_db_instance" "bad" {
  password = "hardcoded-password"  # NEVER DO THIS
}

# DO: Use variables with sensitive flag
variable "db_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "good" {
  password = var.db_password
}
```

## AWS Secrets Manager Integration

```hcl
# Create secret
resource "aws_secretsmanager_secret" "db" {
  name = "${var.environment}/database/credentials"

  tags = {
    Environment = var.environment
  }
}

resource "aws_secretsmanager_secret_version" "db" {
  secret_id = aws_secretsmanager_secret.db.id

  secret_string = jsonencode({
    username = var.db_username
    password = random_password.db.result
    host     = aws_db_instance.main.endpoint
    port     = 5432
    database = var.db_name
  })
}

# Read secret
data "aws_secretsmanager_secret_version" "db" {
  secret_id = aws_secretsmanager_secret.db.id
}

locals {
  db_creds = jsondecode(data.aws_secretsmanager_secret_version.db.secret_string)
}

resource "aws_db_instance" "main" {
  username = local.db_creds.username
  password = local.db_creds.password
}
```

## HashiCorp Vault Integration

```hcl
provider "vault" {
  address = "https://vault.example.com"
}

# Read from Vault
data "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "database/credentials"
}

resource "aws_db_instance" "main" {
  username = data.vault_kv_secret_v2.db.data["username"]
  password = data.vault_kv_secret_v2.db.data["password"]
}

# Dynamic database credentials
data "vault_database_secret" "app" {
  backend = "database"
  role    = "app-role"
}

resource "kubernetes_secret" "db" {
  metadata {
    name = "db-credentials"
  }

  data = {
    username = data.vault_database_secret.app.username
    password = data.vault_database_secret.app.password
  }
}
```

## State Security

```hcl
# Encrypted S3 backend
terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "alias/terraform-state"
    dynamodb_table = "terraform-locks"

    # Restrict access
    acl = "private"
  }
}

# S3 bucket policy
resource "aws_s3_bucket_policy" "state" {
  bucket = aws_s3_bucket.state.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "EnforceTLS"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource = [
          aws_s3_bucket.state.arn,
          "${aws_s3_bucket.state.arn}/*"
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      },
      {
        Sid       = "RestrictToTerraformRole"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource = [
          aws_s3_bucket.state.arn,
          "${aws_s3_bucket.state.arn}/*"
        ]
        Condition = {
          StringNotEquals = {
            "aws:PrincipalArn" = var.terraform_role_arn
          }
        }
      }
    ]
  })
}
```

## IAM Least Privilege

```hcl
# Terraform execution role
data "aws_iam_policy_document" "terraform" {
  # Only allow specific actions
  statement {
    sid    = "EC2Management"
    effect = "Allow"

    actions = [
      "ec2:Describe*",
      "ec2:CreateVpc",
      "ec2:DeleteVpc",
      "ec2:CreateSubnet",
      "ec2:DeleteSubnet",
      "ec2:CreateSecurityGroup",
      "ec2:DeleteSecurityGroup",
    ]

    resources = ["*"]

    condition {
      test     = "StringEquals"
      variable = "aws:RequestedRegion"
      values   = ["us-east-1", "us-west-2"]
    }
  }

  # Require MFA for destructive actions
  statement {
    sid    = "RequireMFAForDestructive"
    effect = "Deny"

    actions = [
      "ec2:DeleteVpc",
      "rds:DeleteDBInstance",
      "s3:DeleteBucket",
    ]

    resources = ["*"]

    condition {
      test     = "BoolIfExists"
      variable = "aws:MultiFactorAuthPresent"
      values   = ["false"]
    }
  }
}
```

## Security Scanning

```bash
# tfsec - static analysis
tfsec .

# checkov - policy checking
checkov -d .

# terrascan - compliance
terrascan scan -i terraform

# trivy - vulnerability scanning
trivy config .
```

```yaml
# .github/workflows/security.yml
security-scan:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: tfsec
      uses: aquasecurity/tfsec-action@v1.0.0
      with:
        soft_fail: false

    - name: Checkov
      uses: bridgecrewio/checkov-action@master
      with:
        directory: terraform/
        framework: terraform
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Performance & Scalability",
        "slug": "performance-scalability",
        "description": "Optimize Terraform for large-scale infrastructure",
        "difficulty": "advanced",
        "xp_reward": 200,
        "estimated_minutes": 50,
        "content": """# Performance & Scalability

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│   ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐          │
│   │  Write │────▶│  Plan  │────▶│ Review │────▶│ Apply  │          │
│   │   HCL  │     │        │     │        │     │        │          │
│   └────────┘     └────────┘     └────────┘     └────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt  
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## State Splitting

```
infrastructure/
├── networking/        # VPC, subnets, routes
│   ├── main.tf
│   └── backend.tf     # networking/terraform.tfstate
├── compute/           # EC2, ASG, LB
│   ├── main.tf
│   └── backend.tf     # compute/terraform.tfstate
├── database/          # RDS, ElastiCache
│   ├── main.tf
│   └── backend.tf     # database/terraform.tfstate
└── applications/      # ECS, Lambda
    ├── main.tf
    └── backend.tf     # applications/terraform.tfstate
```

```hcl
# networking/backend.tf
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "networking/terraform.tfstate"
    region = "us-east-1"
  }
}

# compute/main.tf - Reference networking state
data "terraform_remote_state" "networking" {
  backend = "s3"

  config = {
    bucket = "terraform-state"
    key    = "networking/terraform.tfstate"
    region = "us-east-1"
  }
}

resource "aws_instance" "web" {
  subnet_id = data.terraform_remote_state.networking.outputs.private_subnet_ids[0]
}
```

## Parallelism & Concurrency

```bash
# Increase parallelism (default: 10)
terraform apply -parallelism=20

# Reduce for API rate limits
terraform apply -parallelism=5
```

## Targeted Operations

```bash
# Target specific resources
terraform plan -target=aws_instance.web
terraform apply -target=module.vpc

# Target multiple resources
terraform apply -target=aws_instance.web -target=aws_eip.web

# Refresh specific resources
terraform refresh -target=aws_instance.web
```

## Resource Dependencies

```hcl
# Implicit dependency (preferred)
resource "aws_instance" "web" {
  subnet_id = aws_subnet.public.id  # Implicit dependency
}

# Explicit dependency
resource "aws_instance" "app" {
  ami           = "ami-123"
  instance_type = "t3.micro"

  depends_on = [aws_db_instance.main]  # Wait for DB
}

# Lifecycle management
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  lifecycle {
    create_before_destroy = true  # Zero-downtime updates
    prevent_destroy       = true  # Prevent accidental deletion
    ignore_changes        = [ami] # Ignore AMI updates

    # Replace when expression changes
    replace_triggered_by = [
      aws_security_group.web.id
    ]
  }
}
```

## Data Source Optimization

```hcl
# Cache expensive lookups
locals {
  ami_id = var.ami_id != "" ? var.ami_id : data.aws_ami.amazon_linux.id
}

data "aws_ami" "amazon_linux" {
  count = var.ami_id == "" ? 1 : 0  # Only query if needed

  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_instance" "web" {
  ami = local.ami_id
}
```

## Module Caching

```bash
# Use plugin cache
export TF_PLUGIN_CACHE_DIR="$HOME/.terraform.d/plugin-cache"

# Pre-download providers
terraform providers mirror ./terraform-plugins

# Use local mirror
terraform init -plugin-dir=./terraform-plugins
```

## Large State Management

```bash
# List state resources
terraform state list | wc -l

# Remove old resources
terraform state rm module.deprecated

# Move resources between states
terraform state mv -state-out=new.tfstate aws_instance.web aws_instance.web

# Refresh only specific resources
terraform apply -refresh-only -target=aws_instance.web
```


> 💡 **Pro Tip:** Kör `terraform validate` efter varje ändring – det fångar syntaxfel utan API-anrop.
"""
    },
    {
        "title": "Disaster Recovery & Rollback",
        "slug": "disaster-recovery",
        "description": "Implement disaster recovery and rollback strategies",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 55,
        "content": """# Disaster Recovery & Rollback

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│   ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐          │
│   │  Write │────▶│  Plan  │────▶│ Review │────▶│ Apply  │          │
│   │   HCL  │     │        │     │        │     │        │          │
│   └────────┘     └────────┘     └────────┘     └────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt  
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## State Backup Strategy

```hcl
# S3 versioning for state
resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Lifecycle rules for version retention
resource "aws_s3_bucket_lifecycle_configuration" "state" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    id     = "state-versions"
    status = "Enabled"

    noncurrent_version_transition {
      noncurrent_days = 30
      storage_class   = "GLACIER"
    }

    noncurrent_version_expiration {
      noncurrent_days = 365
    }
  }
}
```

## State Recovery

```bash
# List state versions (S3)
aws s3api list-object-versions \\
  --bucket terraform-state \\
  --prefix prod/terraform.tfstate

# Restore specific version
aws s3api get-object \\
  --bucket terraform-state \\
  --key prod/terraform.tfstate \\
  --version-id "abc123" \\
  restored-state.tfstate

# Apply restored state
terraform state push restored-state.tfstate
```

## Blue-Green Deployments

```hcl
variable "active_environment" {
  type    = string
  default = "blue"

  validation {
    condition     = contains(["blue", "green"], var.active_environment)
    error_message = "Must be blue or green."
  }
}

# Blue environment
module "blue" {
  source = "./modules/environment"

  name    = "blue"
  enabled = true

  instance_count = var.active_environment == "blue" ? var.desired_count : 0
}

# Green environment
module "green" {
  source = "./modules/environment"

  name    = "green"
  enabled = true

  instance_count = var.active_environment == "green" ? var.desired_count : 0
}

# Load balancer points to active
resource "aws_lb_listener_rule" "app" {
  listener_arn = aws_lb_listener.app.arn
  priority     = 100

  action {
    type             = "forward"
    target_group_arn = var.active_environment == "blue" ? module.blue.target_group_arn : module.green.target_group_arn
  }

  condition {
    path_pattern {
      values = ["/*"]
    }
  }
}
```

## Canary Deployments

```hcl
resource "aws_lb_listener_rule" "canary" {
  listener_arn = aws_lb_listener.app.arn
  priority     = 50

  action {
    type = "forward"

    forward {
      target_group {
        arn    = module.stable.target_group_arn
        weight = 90
      }

      target_group {
        arn    = module.canary.target_group_arn
        weight = 10
      }

      stickiness {
        enabled  = true
        duration = 600
      }
    }
  }

  condition {
    path_pattern {
      values = ["/*"]
    }
  }
}

# Gradually shift traffic
variable "canary_weight" {
  type    = number
  default = 10

  validation {
    condition     = var.canary_weight >= 0 && var.canary_weight <= 100
    error_message = "Must be between 0 and 100."
  }
}
```

## Rollback Procedures

```bash
#!/bin/bash
# scripts/rollback.sh

set -e

# Get previous state version
PREVIOUS_VERSION=$(aws s3api list-object-versions \\
  --bucket terraform-state \\
  --prefix prod/terraform.tfstate \\
  --query 'Versions[1].VersionId' \\
  --output text)

echo "Rolling back to version: $PREVIOUS_VERSION"

# Download previous state
aws s3api get-object \\
  --bucket terraform-state \\
  --key prod/terraform.tfstate \\
  --version-id "$PREVIOUS_VERSION" \\
  previous-state.tfstate

# Create backup of current state
terraform state pull > current-state-backup.tfstate

# Push previous state
terraform state push previous-state.tfstate

# Apply to restore infrastructure
terraform apply -auto-approve

echo "Rollback complete!"
```

## Import for Recovery

```hcl
# import.tf - Recover lost state
import {
  to = aws_instance.web
  id = "i-1234567890abcdef0"
}

import {
  to = aws_vpc.main
  id = "vpc-12345678"
}

import {
  to = aws_db_instance.main
  id = "my-database"
}
```

```bash
# Generate configuration from imports
terraform plan -generate-config-out=recovered.tf

# Review and apply
terraform apply
```

## Multi-Region DR

```hcl
# Primary region
provider "aws" {
  alias  = "primary"
  region = "us-east-1"
}

# DR region
provider "aws" {
  alias  = "dr"
  region = "us-west-2"
}

# Primary resources
module "primary" {
  source = "./modules/infrastructure"
  providers = {
    aws = aws.primary
  }

  environment = "prod"
  is_primary  = true
}

# DR resources (scaled down)
module "dr" {
  source = "./modules/infrastructure"
  providers = {
    aws = aws.dr
  }

  environment    = "prod-dr"
  is_primary     = false
  instance_count = var.dr_mode ? var.production_count : 1
}

# Route53 health check and failover
resource "aws_route53_health_check" "primary" {
  fqdn              = module.primary.lb_dns_name
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = 3
  request_interval  = 30
}

resource "aws_route53_record" "app" {
  zone_id = var.zone_id
  name    = "app.example.com"
  type    = "A"

  failover_routing_policy {
    type = "PRIMARY"
  }

  set_identifier  = "primary"
  health_check_id = aws_route53_health_check.primary.id

  alias {
    name                   = module.primary.lb_dns_name
    zone_id                = module.primary.lb_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "app_dr" {
  zone_id = var.zone_id
  name    = "app.example.com"
  type    = "A"

  failover_routing_policy {
    type = "SECONDARY"
  }

  set_identifier = "secondary"

  alias {
    name                   = module.dr.lb_dns_name
    zone_id                = module.dr.lb_zone_id
    evaluate_target_health = true
  }
}
```


> 💡 **Pro Tip:** Kör `terraform validate` efter varje ändring – det fångar syntaxfel utan API-anrop.
"""
    },
    {
        "title": "Production Deployment Patterns",
        "slug": "production-patterns",
        "description": "Enterprise patterns for production Terraform deployments",
        "difficulty": "advanced",
        "xp_reward": 250,
        "estimated_minutes": 65,
        "content": """# Production Deployment Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│   ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐          │
│   │  Write │────▶│  Plan  │────▶│ Review │────▶│ Apply  │          │
│   │   HCL  │     │        │     │        │     │        │          │
│   └────────┘     └────────┘     └────────┘     └────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt  
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---



## Environment Hierarchy

```
terraform/
├── modules/           # Shared modules
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── monitoring/
├── environments/
│   ├── _shared/       # Shared configuration
│   │   ├── providers.tf
│   │   └── backend.tf.tpl
│   ├── dev/
│   │   ├── main.tf
│   │   ├── backend.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── main.tf
│   │   ├── backend.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── main.tf
│       ├── backend.tf
│       └── terraform.tfvars
└── global/            # Account-wide resources
    ├── iam/
    ├── route53/
    └── s3/
```

## Terragrunt for DRY

```hcl
# terragrunt.hcl (root)
remote_state {
  backend = "s3"

  config = {
    bucket         = "terraform-state-${get_aws_account_id()}"
    key            = "${path_relative_to_include()}/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite"

  contents = <<EOF
provider "aws" {
  region = "${local.region}"

  default_tags {
    tags = {
      Environment = "${local.environment}"
      ManagedBy   = "Terraform"
      Project     = "${local.project}"
    }
  }
}
EOF
}

# environments/prod/terragrunt.hcl
include "root" {
  path = find_in_parent_folders()
}

locals {
  environment = "prod"
  region      = "us-east-1"
  project     = "myapp"
}

terraform {
  source = "../../modules//vpc"
}

inputs = {
  vpc_cidr           = "10.0.0.0/16"
  enable_nat_gateway = true
  single_nat_gateway = false
}
```

## GitOps with Terraform

```yaml
# .github/workflows/gitops.yml
name: GitOps Terraform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      environments: ${{ steps.changes.outputs.environments }}
    steps:
      - uses: actions/checkout@v4
      - id: changes
        run: |
          ENVS=$(git diff --name-only HEAD~1 | grep '^terraform/environments/' | cut -d'/' -f3 | sort -u | jq -R -s -c 'split("\\n")[:-1]')
          echo "environments=$ENVS" >> $GITHUB_OUTPUT

  terraform:
    needs: detect-changes
    if: needs.detect-changes.outputs.environments != '[]'
    strategy:
      matrix:
        environment: ${{ fromJson(needs.detect-changes.outputs.environments) }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3

      - name: Terraform Plan
        working-directory: terraform/environments/${{ matrix.environment }}
        run: |
          terraform init
          terraform plan -out=tfplan

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        working-directory: terraform/environments/${{ matrix.environment }}
        run: terraform apply -auto-approve tfplan
```

## Drift Detection

```yaml
# .github/workflows/drift.yml
name: Drift Detection

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours

jobs:
  drift-check:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [dev, staging, prod]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3

      - name: Check for Drift
        id: drift
        working-directory: terraform/environments/${{ matrix.environment }}
        run: |
          terraform init
          terraform plan -detailed-exitcode -out=tfplan 2>&1 | tee plan.txt
          EXIT_CODE=$?
          if [ $EXIT_CODE -eq 2 ]; then
            echo "drift=true" >> $GITHUB_OUTPUT
          fi

      - name: Alert on Drift
        if: steps.drift.outputs.drift == 'true'
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "⚠️ Terraform drift detected in ${{ matrix.environment }}!",
              "attachments": [
                {
                  "color": "warning",
                  "text": "Run `terraform apply` to reconcile."
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Cost Estimation

```hcl
# Infracost integration
# .infracost.yml
version: 0.1

projects:
  - path: terraform/environments/prod
    terraform_var_files:
      - terraform.tfvars

  - path: terraform/environments/staging
    terraform_var_files:
      - terraform.tfvars
```

```yaml
# GitHub Action for cost estimation
- name: Infracost
  uses: infracost/actions/setup@v2

- name: Generate Cost Report
  run: |
    infracost breakdown --path terraform/ \\
      --format json --out-file infracost.json

    infracost comment github \\
      --path infracost.json \\
      --repo ${{ github.repository }} \\
      --pull-request ${{ github.event.pull_request.number }} \\
      --github-token ${{ secrets.GITHUB_TOKEN }}
```

## Change Management

```hcl
# Approval gates via outputs
output "changes_summary" {
  value = {
    resources_to_create = length([for r in local.plan.resource_changes : r if r.change.actions[0] == "create"])
    resources_to_update = length([for r in local.plan.resource_changes : r if r.change.actions[0] == "update"])
    resources_to_delete = length([for r in local.plan.resource_changes : r if r.change.actions[0] == "delete"])

    high_risk_changes = [
      for r in local.plan.resource_changes : r.address
      if contains(["aws_db_instance", "aws_rds_cluster", "aws_vpc"], r.type)
      && contains(r.change.actions, "delete")
    ]
  }
}
```

## Compliance & Audit

```hcl
# Audit logging
resource "aws_cloudtrail" "terraform" {
  name           = "terraform-audit"
  s3_bucket_name = aws_s3_bucket.audit.id

  event_selector {
    read_write_type           = "All"
    include_management_events = true
  }

  tags = {
    Purpose = "Terraform Audit Trail"
  }
}

# Resource tagging policy
variable "required_tags" {
  type = map(string)

  default = {
    Environment = "Must specify environment"
    Owner       = "Must specify owner team"
    Project     = "Must specify project name"
    CostCenter  = "Must specify cost center"
  }
}

locals {
  validated_tags = {
    for key, desc in var.required_tags :
    key => lookup(var.tags, key, null) != null ? var.tags[key] : error("Missing required tag: ${key} - ${desc}")
  }
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    }
]
