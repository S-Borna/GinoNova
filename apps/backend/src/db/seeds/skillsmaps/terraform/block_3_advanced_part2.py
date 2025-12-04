# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 3: ADVANCED PATTERNS (Part 2)
# =============================================================================
# Nodes 11-12: Workspaces, Provisioners & Null Resources
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_11 = {
    "id": "terraform_node_11",
    "slug": "terraform-workspaces-environments",
    "title": "Workspaces & Environment Management",
    "description": "Master workspace patterns for multi-environment deployments",
    "node_id": 11,
    "content": r'''
# Workspaces & Environment Management

## Workspace Fundamentals

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKSPACES                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Workspaces = Separate state files for same configuration              │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              SAME TERRAFORM CODE                                 │   │
│  │              (main.tf, variables.tf, etc.)                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                              │                                          │
│           ┌──────────────────┼──────────────────┐                      │
│           │                  │                  │                      │
│           ▼                  ▼                  ▼                      │
│   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐             │
│   │   WORKSPACE   │  │   WORKSPACE   │  │   WORKSPACE   │             │
│   │     "dev"     │  │   "staging"   │  │    "prod"     │             │
│   ├───────────────┤  ├───────────────┤  ├───────────────┤             │
│   │  State: dev   │  │State: staging │  │ State: prod   │             │
│   │  Resources:   │  │  Resources:   │  │  Resources:   │             │
│   │  - 1 instance │  │  - 2 instances│  │  - 5 instances│             │
│   │  - t3.micro   │  │  - t3.small   │  │  - t3.large   │             │
│   └───────────────┘  └───────────────┘  └───────────────┘             │
│                                                                         │
│  USE CASES:                                                            │
│  • Multiple environments (dev/staging/prod)                            │
│  • Feature branches                                                    │
│  • Blue/Green deployments                                              │
│  • Multi-tenant infrastructure                                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Workspace Commands

```bash
# List workspaces (* indicates current)
terraform workspace list
# * default
#   dev
#   staging
#   prod

# Show current workspace
terraform workspace show
# default

# Create new workspace
terraform workspace new dev
# Created and switched to workspace "dev"!

terraform workspace new staging
terraform workspace new prod

# Switch workspace
terraform workspace select prod
# Switched to workspace "prod".

# Delete workspace (must switch away first)
terraform workspace select default
terraform workspace delete dev
# Deleted workspace "dev"!
```

---

## Workspace-Based Configuration

### Using terraform.workspace

```hcl
# Access current workspace name
locals {
  environment = terraform.workspace
}

# Environment-specific instance count
resource "aws_instance" "web" {
  count         = terraform.workspace == "prod" ? 3 : 1
  ami           = data.aws_ami.latest.id
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Name        = "web-${terraform.workspace}-${count.index + 1}"
    Environment = terraform.workspace
  }
}

# Conditional resources
resource "aws_autoscaling_group" "web" {
  count = terraform.workspace == "prod" ? 1 : 0
  # ... ASG only in production
}
```

### Workspace Configuration Map

```hcl
locals {
  workspace_config = {
    default = {
      instance_type  = "t3.micro"
      instance_count = 1
      enable_ha      = false
      enable_cdn     = false
    }
    dev = {
      instance_type  = "t3.micro"
      instance_count = 1
      enable_ha      = false
      enable_cdn     = false
    }
    staging = {
      instance_type  = "t3.small"
      instance_count = 2
      enable_ha      = true
      enable_cdn     = false
    }
    prod = {
      instance_type  = "t3.large"
      instance_count = 3
      enable_ha      = true
      enable_cdn     = true
    }
  }

  config = local.workspace_config[terraform.workspace]
}

resource "aws_instance" "web" {
  count         = local.config.instance_count
  instance_type = local.config.instance_type

  tags = {
    Name        = "web-${terraform.workspace}"
    Environment = terraform.workspace
  }
}

resource "aws_cloudfront_distribution" "cdn" {
  count = local.config.enable_cdn ? 1 : 0
  # ...
}
```

---

## Workspace State Organization

### Local Backend

```
terraform.tfstate.d/
├── dev/
│   └── terraform.tfstate
├── staging/
│   └── terraform.tfstate
└── prod/
    └── terraform.tfstate
```

### S3 Backend with Workspaces

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket               = "my-terraform-state"
    key                  = "infrastructure/terraform.tfstate"
    region               = "eu-north-1"
    dynamodb_table       = "terraform-locks"
    workspace_key_prefix = "workspaces"
  }
}

# Results in S3 paths:
# s3://my-terraform-state/workspaces/dev/infrastructure/terraform.tfstate
# s3://my-terraform-state/workspaces/staging/infrastructure/terraform.tfstate
# s3://my-terraform-state/workspaces/prod/infrastructure/terraform.tfstate
```

### Terraform Cloud Workspaces

```hcl
# Terraform Cloud uses workspace names directly
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      # Single workspace
      name = "my-app-prod"

      # Or workspace prefix
      # tags = ["app:my-app"]
    }
  }
}
```

---

## Workspaces vs Directory Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│           WORKSPACES vs DIRECTORY STRUCTURE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  WORKSPACES                           DIRECTORIES                       │
│  ──────────                           ───────────                       │
│                                                                         │
│  project/                             infrastructure/                   │
│  ├── main.tf                          ├── modules/                      │
│  ├── variables.tf                     │   └── vpc/                      │
│  └── (workspaces: dev,staging,prod)   ├── environments/                 │
│                                        │   ├── dev/                      │
│                                        │   │   └── main.tf              │
│                                        │   ├── staging/                  │
│                                        │   │   └── main.tf              │
│                                        │   └── prod/                     │
│                                        │       └── main.tf              │
│                                                                         │
│  PROS:                                PROS:                             │
│  ✓ Same code for all envs            ✓ Full isolation                  │
│  ✓ Easy to switch                    ✓ Different configs possible      │
│  ✓ Less duplication                  ✓ Independent deployments         │
│                                                                         │
│  CONS:                                CONS:                             │
│  ✗ Easy to apply to wrong env        ✗ Code duplication               │
│  ✗ Must use conditionals             ✗ Harder to keep in sync          │
│  ✗ Less isolation                    ✗ More files to maintain          │
│                                                                         │
│  USE WHEN:                            USE WHEN:                         │
│  • Same code, different sizes        • Very different configs          │
│  • Feature branches                   • Production vs non-prod split    │
│  • Quick environment switching       • Compliance requirements          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Environment Variables per Workspace

```hcl
# terraform.tfvars - Base values
project_name = "myapp"
region       = "eu-north-1"

# dev.tfvars
instance_type  = "t3.micro"
instance_count = 1

# staging.tfvars
instance_type  = "t3.small"
instance_count = 2

# prod.tfvars
instance_type  = "t3.large"
instance_count = 3

# Usage
terraform workspace select dev
terraform apply -var-file="${terraform.workspace}.tfvars"
```

### Auto-loading Based on Workspace

```hcl
# variables.tf
variable "instance_type" {
  type    = string
  default = null
}

# locals.tf
locals {
  default_instance_types = {
    dev     = "t3.micro"
    staging = "t3.small"
    prod    = "t3.large"
  }

  # Use provided value or workspace default
  instance_type = coalesce(
    var.instance_type,
    lookup(local.default_instance_types, terraform.workspace, "t3.micro")
  )
}
```

---

## CI/CD with Workspaces

### GitHub Actions Example

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  TF_VERSION: "1.6.4"
  AWS_REGION: "eu-north-1"

jobs:
  terraform:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        workspace: [dev, staging]
        include:
          - workspace: dev
            branch: develop
          - workspace: staging
            branch: develop

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Terraform Init
        run: terraform init

      - name: Select Workspace
        run: terraform workspace select ${{ matrix.workspace }} || terraform workspace new ${{ matrix.workspace }}

      - name: Terraform Plan
        run: terraform plan -var-file="${{ matrix.workspace }}.tfvars" -out=tfplan

      - name: Terraform Apply
        if: github.ref == 'refs/heads/${{ matrix.branch }}' && github.event_name == 'push'
        run: terraform apply -auto-approve tfplan

  production:
    runs-on: ubuntu-latest
    needs: terraform
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Init
        run: terraform init

      - name: Select Production
        run: terraform workspace select prod

      - name: Terraform Apply
        run: terraform apply -var-file="prod.tfvars" -auto-approve
```

---

## Workspace Safety

### Prevent Accidental Production Changes

```hcl
# preconditions.tf
resource "null_resource" "workspace_check" {
  lifecycle {
    precondition {
      condition     = terraform.workspace != "prod" || var.confirm_production == true
      error_message = "Set confirm_production=true to apply to production."
    }
  }
}

# Run with:
# terraform apply -var="confirm_production=true" -var-file="prod.tfvars"
```

### Workspace Naming Validation

```hcl
locals {
  allowed_workspaces = ["dev", "staging", "prod"]

  validate_workspace = (
    contains(local.allowed_workspaces, terraform.workspace)
    ? true
    : tobool("Invalid workspace '${terraform.workspace}'. Allowed: ${join(", ", local.allowed_workspaces)}")
  )
}
```

---

## Praktiska Övningar

### Övning 1: Workspace Setup
```bash
# 1. Skapa tre workspaces: dev, staging, prod
# 2. Konfigurera workspace-baserade variabler
# 3. Deploya till varje environment
```

### Övning 2: CI/CD Pipeline
```yaml
# Implementera GitHub Actions workflow som:
# 1. Kör plan på PR
# 2. Applicerar dev på merge till develop
# 3. Applicerar prod på merge till main
```

---

**Nästa Node:** Provisioners & Null Resources →
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["terraform_node_10"],
    "learning_outcomes": [
        "Hantera workspaces för multi-environment",
        "Konfigurera workspace-baserade resurser",
        "Implementera workspace-säkerhet",
        "Integrera workspaces med CI/CD",
        "Välja mellan workspaces och directories"
    ]
}

NODE_12 = {
    "id": "terraform_node_12",
    "slug": "terraform-provisioners-null",
    "title": "Provisioners & Null Resources - Extending Terraform",
    "description": "Use provisioners and null resources for complex workflows",
    "node_id": 12,
    "content": r'''
# Provisioners & Null Resources - Extending Terraform

## Provisioner Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM PROVISIONERS                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ⚠️  PROVISIONERS ARE A LAST RESORT!                                   │
│                                                                         │
│  Better alternatives:                                                  │
│  • cloud-init / user_data for EC2                                      │
│  • Packer for immutable images                                         │
│  • Configuration management (Ansible, Chef, Puppet)                    │
│  • Container orchestration (Kubernetes)                                │
│                                                                         │
│  USE PROVISIONERS WHEN:                                                │
│  • No other option exists                                              │
│  • Quick bootstrap needed                                              │
│  • Running local scripts on apply/destroy                              │
│                                                                         │
│  PROVISIONER TYPES                                                     │
│  ─────────────────                                                     │
│                                                                         │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│  │   local-exec    │  │   remote-exec   │  │      file       │        │
│  │   ───────────   │  │   ────────────  │  │   ────────      │        │
│  │ Runs on machine │  │ Runs on remote  │  │ Copy files to   │        │
│  │ where Terraform │  │ resource (SSH/  │  │ remote machine  │        │
│  │ is executed     │  │ WinRM)          │  │                 │        │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## local-exec Provisioner

Kör kommandon lokalt (på maskinen som kör Terraform).

### Basic Usage

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }
}
```

### Advanced Options

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    # Command to run
    command = "ansible-playbook -i ${self.private_ip}, playbook.yml"

    # Working directory
    working_dir = "${path.module}/ansible"

    # Environment variables
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
      AWS_REGION                = var.region
    }

    # Interpreter (default: shell)
    interpreter = ["/bin/bash", "-c"]

    # When to run
    when = create  # create (default) or destroy

    # Continue on failure
    on_failure = continue  # continue or fail (default)
  }
}
```

### Common Patterns

```hcl
# Write to file
resource "aws_instance" "web" {
  count         = 3
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = <<-EOF
      echo "${self.tags.Name} ansible_host=${self.private_ip}" >> inventory.ini
    EOF
  }
}

# Call external API
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = <<-EOF
      curl -X POST https://api.example.com/instances \
        -H "Authorization: Bearer ${var.api_token}" \
        -d '{"instance_id": "${self.id}", "ip": "${self.private_ip}"}'
    EOF
  }
}

# Wait for instance
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = <<-EOF
      until nc -z ${self.public_ip} 22; do
        echo "Waiting for SSH..."
        sleep 5
      done
    EOF
  }
}

# Run Python script
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    interpreter = ["python3", "-c"]
    command     = <<-EOF
      import json
      data = {"id": "${self.id}", "ip": "${self.private_ip}"}
      with open("instance.json", "w") as f:
          json.dump(data, f)
    EOF
  }
}
```

---

## remote-exec Provisioner

Kör kommandon på den skapade resursen via SSH eller WinRM.

### SSH Connection

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.deployer.key_name

  # Connection configuration
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/deployer.pem")
    host        = self.public_ip

    # Optional
    timeout     = "5m"
    agent       = false
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd"
    ]
  }
}
```

### Script Execution

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.deployer.key_name

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file(var.private_key_path)
    host        = self.public_ip
  }

  # Run local script on remote
  provisioner "remote-exec" {
    script = "${path.module}/scripts/setup.sh"
  }

  # Run multiple scripts
  provisioner "remote-exec" {
    scripts = [
      "${path.module}/scripts/base.sh",
      "${path.module}/scripts/app.sh"
    ]
  }
}
```

### Bastion/Jump Host

```hcl
resource "aws_instance" "private" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.private.id

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file(var.private_key_path)
    host        = self.private_ip

    # Jump through bastion
    bastion_host        = aws_instance.bastion.public_ip
    bastion_user        = "ec2-user"
    bastion_private_key = file(var.private_key_path)
  }

  provisioner "remote-exec" {
    inline = ["echo 'Connected through bastion!'"]
  }
}
```

---

## file Provisioner

Kopiera filer till remote resource.

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.deployer.key_name

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file(var.private_key_path)
    host        = self.public_ip
  }

  # Copy single file
  provisioner "file" {
    source      = "${path.module}/configs/nginx.conf"
    destination = "/tmp/nginx.conf"
  }

  # Copy directory
  provisioner "file" {
    source      = "${path.module}/configs/"
    destination = "/tmp/configs"
  }

  # Copy content directly
  provisioner "file" {
    content     = templatefile("${path.module}/templates/app.conf.tpl", {
      db_host = aws_db_instance.main.endpoint
      db_name = var.db_name
    })
    destination = "/tmp/app.conf"
  }

  # Then run remote-exec to move files
  provisioner "remote-exec" {
    inline = [
      "sudo mv /tmp/nginx.conf /etc/nginx/nginx.conf",
      "sudo systemctl restart nginx"
    ]
  }
}
```

---

## Null Resource

Resurs som inte skapar något i cloud, men kan ha provisioners och triggers.

### Basic Null Resource

```hcl
resource "null_resource" "example" {
  # Re-run when input changes
  triggers = {
    instance_id = aws_instance.web.id
  }

  provisioner "local-exec" {
    command = "echo 'Instance ${aws_instance.web.id} was created'"
  }
}
```

### Trigger Patterns

```hcl
# Trigger on any change
resource "null_resource" "always_run" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "echo 'Running at ${timestamp()}'"
  }
}

# Trigger on specific resource changes
resource "null_resource" "configure" {
  triggers = {
    instance_ids = join(",", aws_instance.web[*].id)
    config_hash  = md5(file("${path.module}/config.yml"))
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i inventory configure.yml"
  }

  depends_on = [aws_instance.web]
}

# Trigger on file change
resource "null_resource" "deploy" {
  triggers = {
    source_hash = filemd5("${path.module}/app/main.py")
  }

  provisioner "local-exec" {
    command = "deploy.sh"
  }
}
```

### Destroy-time Provisioner

```hcl
resource "null_resource" "cleanup" {
  triggers = {
    cluster_name = var.cluster_name
    region       = var.region
  }

  # Run on destroy
  provisioner "local-exec" {
    when    = destroy
    command = "aws eks update-kubeconfig --name ${self.triggers.cluster_name} --region ${self.triggers.region} && kubectl delete ns app"

    on_failure = continue
  }
}
```

---

## terraform_data Resource (Modern Alternative)

Terraform 1.4+ introducerade `terraform_data` som ersättning för `null_resource`.

```hcl
resource "terraform_data" "bootstrap" {
  # Input values
  input = {
    instance_ip = aws_instance.web.public_ip
    config_hash = md5(file("config.yml"))
  }

  # Triggers replacement (like null_resource triggers)
  triggers_replace = [
    aws_instance.web.id,
    filemd5("config.yml")
  ]

  provisioner "local-exec" {
    command = "ansible-playbook -i ${self.input.instance_ip}, playbook.yml"
  }
}

# Store and retrieve data
resource "terraform_data" "store" {
  input = {
    created_at = timestamp()
    version    = var.app_version
  }
}

output "stored_data" {
  value = terraform_data.store.output
}
```

---

## Provisioner Alternatives

### cloud-init (Preferred for EC2)

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
  EOF

  user_data_replace_on_change = true
}

# Or use templatefile
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"

  user_data = templatefile("${path.module}/userdata.sh", {
    environment = var.environment
    db_host     = aws_db_instance.main.endpoint
  })
}
```

### Packer (Immutable Images)

```json
// packer/ami.pkr.hcl
source "amazon-ebs" "web" {
  ami_name      = "web-server-{{timestamp}}"
  instance_type = "t3.micro"
  region        = "eu-north-1"
  source_ami_filter {
    filters = {
      name                = "amzn2-ami-hvm-*-x86_64-gp2"
      virtualization-type = "hvm"
    }
    owners      = ["amazon"]
    most_recent = true
  }
  ssh_username = "ec2-user"
}

build {
  sources = ["source.amazon-ebs.web"]

  provisioner "shell" {
    script = "scripts/setup.sh"
  }
}
```

```hcl
# Terraform uses Packer-built AMI
data "aws_ami" "web" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "name"
    values = ["web-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.web.id
  instance_type = "t3.micro"
  # No provisioners needed!
}
```

---

## Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROVISIONER BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1. USE PROVISIONERS AS LAST RESORT                                    │
│     • Prefer cloud-init, Packer, Ansible                               │
│     • Provisioners break the declarative model                         │
│                                                                         │
│  2. MAKE PROVISIONERS IDEMPOTENT                                       │
│     • Running twice should produce same result                         │
│     • Use checksums and conditions                                     │
│                                                                         │
│  3. HANDLE FAILURES GRACEFULLY                                         │
│     • Use on_failure = continue when appropriate                       │
│     • Log errors for debugging                                         │
│                                                                         │
│  4. AVOID REMOTE-EXEC WHEN POSSIBLE                                    │
│     • Requires network connectivity                                    │
│     • SSH key management complexity                                    │
│     • Prefer local-exec with Ansible                                   │
│                                                                         │
│  5. USE NULL_RESOURCE FOR ORCHESTRATION                                │
│     • Trigger external workflows                                       │
│     • Chain dependencies                                               │
│     • Run cleanup on destroy                                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Praktiska Övningar

### Övning 1: Inventory Generation
```hcl
# Skapa Ansible inventory från EC2 instances
resource "null_resource" "inventory" {
  triggers = {
    instances = join(",", aws_instance.web[*].id)
  }

  provisioner "local-exec" {
    command = <<-EOF
      echo "[web]" > inventory.ini
      %{ for instance in aws_instance.web ~}
      echo "${instance.tags.Name} ansible_host=${instance.private_ip}" >> inventory.ini
      %{ endfor ~}
    EOF
  }
}
```

### Övning 2: Post-Deploy Verification
```hcl
# Verifiera deployment efter apply
resource "null_resource" "verify" {
  triggers = {
    lb_dns = aws_lb.main.dns_name
  }

  provisioner "local-exec" {
    command = <<-EOF
      for i in {1..30}; do
        if curl -s http://${aws_lb.main.dns_name}/health | grep -q "ok"; then
          echo "Health check passed!"
          exit 0
        fi
        echo "Waiting for health check... ($i/30)"
        sleep 10
      done
      echo "Health check failed!"
      exit 1
    EOF
  }
}
```

---

**Nästa Node:** Terraform CI/CD Pipeline →
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["terraform_node_11"],
    "learning_outcomes": [
        "Förstå när provisioners är lämpliga",
        "Använda local-exec och remote-exec",
        "Implementera null_resource patterns",
        "Hantera destroy-time provisioners",
        "Välja rätt alternativ till provisioners"
    ]
}

# Block 3 Part 2 exports
BLOCK_3_PART_2_NODES = [NODE_11, NODE_12]

__all__ = ["NODE_11", "NODE_12", "BLOCK_3_PART_2_NODES"]
