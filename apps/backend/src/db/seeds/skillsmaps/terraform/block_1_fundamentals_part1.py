# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 1: FUNDAMENTALS (Part 1)
# =============================================================================
# Nodes 1-2: Terraform Introduction, HCL Syntax
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_1 = {
    "id": "terraform_node_1",
    "slug": "terraform-introduction",
    "title": "Terraform Introduction - Infrastructure as Code Revolution",
    "description": "Master the fundamentals of Terraform and Infrastructure as Code (IaC)",
    "node_id": 1,
    "content": '''
# Terraform Introduction - Infrastructure as Code Revolution

## Välkommen till Modern Infrastructure Management

Infrastructure as Code (IaC) har revolutionerat hur vi hanterar infrastruktur. Terraform från HashiCorp är ledande inom detta område och används av tusentals organisationer världen över.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM ECOSYSTEM OVERVIEW                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐         │
│    │    CODE      │────▶│   TERRAFORM  │────▶│   CLOUD      │         │
│    │   (.tf)      │     │   ENGINE     │     │  PROVIDERS   │         │
│    └──────────────┘     └──────────────┘     └──────────────┘         │
│           │                    │                    │                   │
│           │                    ▼                    │                   │
│           │            ┌──────────────┐            │                   │
│           │            │    STATE     │            │                   │
│           │            │  (.tfstate)  │            │                   │
│           │            └──────────────┘            │                   │
│           │                    │                    │                   │
│           ▼                    ▼                    ▼                   │
│    ┌─────────────────────────────────────────────────────────────┐    │
│    │                     INFRASTRUCTURE                          │    │
│    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │    │
│    │  │   AWS   │  │  AZURE  │  │   GCP   │  │  K8S    │       │    │
│    │  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │    │
│    └─────────────────────────────────────────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Varför Infrastructure as Code?

### Traditionell vs Modern Infrastructure Management

```
┌─────────────────────────────────────────────────────────────────────────┐
│           TRADITIONELL APPROACH                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Developer  ──▶  Ticket  ──▶  Ops Team  ──▶  Manual Config            │
│       │              │            │               │                     │
│       │    Dagar     │   Veckor   │    Timmar     │                     │
│       ▼              ▼            ▼               ▼                     │
│   ┌───────────────────────────────────────────────────────┐            │
│   │  • Inkonsistent konfiguration                         │            │
│   │  • Svårt att reproducera                              │            │
│   │  • Dokumentation blir outdated                        │            │
│   │  • Mänskliga misstag                                  │            │
│   │  • Svårt att audita                                   │            │
│   └───────────────────────────────────────────────────────┘            │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│           IAC APPROACH (TERRAFORM)                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Developer  ──▶  Code  ──▶  PR Review  ──▶  CI/CD  ──▶  Apply        │
│       │            │           │              │            │            │
│       │   Minuter  │  Timmar   │   Minuter    │  Sekunder  │            │
│       ▼            ▼           ▼              ▼            ▼            │
│   ┌───────────────────────────────────────────────────────┐            │
│   │  ✓ Versionskontrollerad                               │            │
│   │  ✓ Reproducerbar                                      │            │
│   │  ✓ Självdokumenterande                                │            │
│   │  ✓ Testbar                                            │            │
│   │  ✓ Auditbar                                           │            │
│   └───────────────────────────────────────────────────────┘            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Terraform vs Alternativen

### IaC Tools Comparison

| Feature | Terraform | CloudFormation | Pulumi | Ansible |
|---------|-----------|----------------|--------|---------|
| **Multi-cloud** | ✅ Ja | ❌ Endast AWS | ✅ Ja | ✅ Ja |
| **Språk** | HCL | JSON/YAML | Python/Go/etc | YAML |
| **State** | Explicit | Managed | Explicit | Implicit |
| **Deklarativ** | ✅ Ja | ✅ Ja | ✅/❌ | ⚠️ Delvis |
| **Plan/Preview** | ✅ Ja | ✅ Change Sets | ✅ Ja | ⚠️ Check mode |
| **Maturitet** | Hög | Hög | Medium | Hög |
| **Community** | Enormt | AWS-fokuserat | Växande | Enormt |

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM SWEET SPOT                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Configuration                                                         │
│   Management ────────┐                                                  │
│   (Ansible)          │                                                  │
│                      │     ┌─────────────────┐                         │
│                      ├────▶│   TERRAFORM     │◀────┐                   │
│   Infrastructure     │     │  Multi-Cloud    │     │                   │
│   Provisioning ──────┘     │  Orchestration  │     │                   │
│                            └─────────────────┘     │                   │
│                                   ▲                │                   │
│   Application        ─────────────┘                │                   │
│   Deployment                                       │                   │
│   (Kubernetes)  ───────────────────────────────────┘                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Installation - Alla Plattformar

### macOS Installation

```bash
# Via Homebrew (rekommenderat)
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# Verifiera installation
terraform version
# terraform v1.6.x

# Uppdatera
brew upgrade hashicorp/tap/terraform
```

### Linux Installation

```bash
# Ubuntu/Debian
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# RHEL/CentOS/Fedora
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum install terraform

# Manuell installation (alla distros)
TERRAFORM_VERSION="1.6.4"
wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform version
```

### Windows Installation

```powershell
# Via Chocolatey
choco install terraform

# Via Scoop
scoop install terraform

# Manuell: Ladda ner från terraform.io och lägg till i PATH
```

### tfenv - Version Manager (Rekommenderat)

```bash
# Installera tfenv
git clone https://github.com/tfutils/tfenv.git ~/.tfenv
echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Installera specifik version
tfenv install 1.6.4
tfenv use 1.6.4

# Lista installerade versioner
tfenv list

# Installera senaste
tfenv install latest

# Projekt-specifik version via .terraform-version fil
echo "1.6.4" > .terraform-version
```

---

## Första Terraform-Projektet

### Projektstruktur

```
my-first-terraform/
├── main.tf          # Huvudkonfiguration
├── variables.tf     # Variabeldeklarationer
├── outputs.tf       # Output-värden
├── providers.tf     # Provider-konfiguration
└── terraform.tfvars # Variabelvärden (känsligt!)
```

### providers.tf - Provider Setup

```hcl
# providers.tf
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = var.project_name
    }
  }
}
```

### variables.tf - Variabeldeklarationer

```hcl
# variables.tf
variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-north-1"
}

variable "environment" {
  description = "Environment name (dev/staging/prod)"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}
```

### main.tf - Resurser

```hcl
# main.tf
# Data source för senaste Amazon Linux AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Security Group
resource "aws_security_group" "web" {
  name        = "${var.project_name}-web-sg"
  description = "Security group for web server"

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]  # Endast internt
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-web-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from Terraform!</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "${var.project_name}-web-server"
  }
}
```

### outputs.tf - Outputs

```hcl
# outputs.tf
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.web.public_dns
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.web.id
}
```

---

## Terraform Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM CORE WORKFLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   1. INIT                    2. PLAN                   3. APPLY        │
│   ────────────────           ────────────────          ────────────    │
│                                                                         │
│   ┌─────────────┐           ┌─────────────┐          ┌─────────────┐  │
│   │  Download   │    ──▶    │   Generate  │   ──▶    │   Execute   │  │
│   │  Providers  │           │   Plan      │          │   Changes   │  │
│   │  & Modules  │           │   (Diff)    │          │             │  │
│   └─────────────┘           └─────────────┘          └─────────────┘  │
│         │                         │                        │           │
│         ▼                         ▼                        ▼           │
│   ┌─────────────┐           ┌─────────────┐          ┌─────────────┐  │
│   │   .terraform/│           │  Execution │          │   State     │  │
│   │   directory  │           │    Plan    │          │   Updated   │  │
│   └─────────────┘           └─────────────┘          └─────────────┘  │
│                                                                         │
│   4. (Optional) DESTROY                                                │
│   ─────────────────────                                                │
│   ┌─────────────────────────────────────────┐                         │
│   │  Remove all resources managed by state  │                         │
│   └─────────────────────────────────────────┘                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Detaljerade Kommandon

```bash
# 1. INIT - Initiera projektet
terraform init

# Output:
# Initializing the backend...
# Initializing provider plugins...
# - Finding hashicorp/aws versions matching "~> 5.0"...
# - Installing hashicorp/aws v5.31.0...
# Terraform has been successfully initialized!

# 2. VALIDATE - Validera syntax
terraform validate
# Success! The configuration is valid.

# 3. FMT - Formatera kod
terraform fmt -recursive
# main.tf
# variables.tf

# 4. PLAN - Visa ändringar
terraform plan -var="environment=dev" -var="project_name=demo"

# Output visar:
# + create
# ~ update in-place
# - destroy
# -/+ destroy and re-create

# 5. APPLY - Applicera ändringar
terraform apply -var="environment=dev" -var="project_name=demo"
# Terraform will perform the following actions:
# ...
# Do you want to perform these actions? yes

# 6. SHOW - Visa current state
terraform show

# 7. OUTPUT - Visa outputs
terraform output
terraform output instance_public_ip

# 8. DESTROY - Ta bort allt
terraform destroy
```

---

## Best Practices från Start

### 1. Använd Backend för State

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "project/terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

### 2. Använd Workspaces för Miljöer

```bash
# Lista workspaces
terraform workspace list

# Skapa workspace
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

# Byt workspace
terraform workspace select dev

# Använd i kod
resource "aws_instance" "web" {
  count = terraform.workspace == "prod" ? 3 : 1
  # ...
}
```

### 3. Sensitive Outputs

```hcl
output "db_password" {
  description = "Database password"
  value       = random_password.db.result
  sensitive   = true
}
```

---

## Praktiska Övningar

### Övning 1: Installera och Verifiera
```bash
# 1. Installera Terraform
# 2. Verifiera version
terraform version

# 3. Installera tfenv för version management
# 4. Skapa .terraform-version fil
```

### Övning 2: Första Projektet
```bash
# 1. Skapa projektstruktur
mkdir terraform-demo && cd terraform-demo

# 2. Skapa main.tf med local provider
cat > main.tf << 'EOF'
resource "local_file" "hello" {
  content  = "Hello, Terraform!"
  filename = "${path.module}/hello.txt"
}
EOF

# 3. Kör workflow
terraform init
terraform plan
terraform apply -auto-approve

# 4. Verifiera
cat hello.txt

# 5. Cleanup
terraform destroy -auto-approve
```

### Övning 3: Utforska State
```bash
# Visa state
terraform show

# Lista resurser i state
terraform state list

# Visa specifik resurs
terraform state show local_file.hello
```

---

**Nästa Node:** HCL Syntax Deep Dive →
''',
    "xp_reward": 150,
    "estimated_minutes": 60,
    "prerequisites": [],
    "learning_outcomes": [
        "Förstå Infrastructure as Code konceptet",
        "Installera och konfigurera Terraform",
        "Skapa första Terraform-projektet",
        "Behärska grundläggande workflow",
        "Implementera best practices från start"
    ]
}

NODE_2 = {
    "id": "terraform_node_2",
    "slug": "hcl-syntax-mastery",
    "title": "HCL Syntax Mastery - HashiCorp Configuration Language",
    "description": "Deep dive into HCL syntax, expressions, and language features",
    "node_id": 2,
    "content": '''
# HCL Syntax Mastery - HashiCorp Configuration Language

## Introduktion till HCL

HashiCorp Configuration Language (HCL) är designat för att vara både människo-läsbart och maskin-vänligt. Det kombinerar det bästa från JSON (strukturerad data) med programmeringsspråksfunktioner.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         HCL LANGUAGE OVERVIEW                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────────────┐                                                  │
│   │   BLOCKS        │  ← Grundläggande byggstenar                      │
│   │   ─────────     │     resource, variable, output, module           │
│   │   type "label" {│                                                  │
│   │     attribute   │                                                  │
│   │   }             │                                                  │
│   └─────────────────┘                                                  │
│           │                                                             │
│           ▼                                                             │
│   ┌─────────────────┐                                                  │
│   │   ATTRIBUTES    │  ← Nyckel-värde par                              │
│   │   ──────────    │     name = "value"                               │
│   │   key = value   │     count = 5                                    │
│   └─────────────────┘                                                  │
│           │                                                             │
│           ▼                                                             │
│   ┌─────────────────┐                                                  │
│   │   EXPRESSIONS   │  ← Dynamiska värden                              │
│   │   ───────────   │     var.name, local.value                        │
│   │   references,   │     functions, conditionals                      │
│   │   functions     │                                                  │
│   └─────────────────┘                                                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Block Types

### 1. Resource Blocks

```hcl
# Syntax: resource "<TYPE>" "<LOCAL_NAME>" { ... }
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  # Nested block
  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }

  # Dynamic nested blocks
  dynamic "ebs_block_device" {
    for_each = var.additional_volumes
    content {
      device_name = ebs_block_device.value.device_name
      volume_size = ebs_block_device.value.size
    }
  }

  tags = {
    Name        = "web-server"
    Environment = var.environment
  }
}
```

### 2. Variable Blocks

```hcl
# String variable
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# Number variable
variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 1

  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 10
    error_message = "Instance count must be between 1 and 10."
  }
}

# Boolean variable
variable "enable_monitoring" {
  description = "Enable detailed monitoring"
  type        = bool
  default     = false
}

# List variable
variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["eu-north-1a", "eu-north-1b"]
}

# Map variable
variable "instance_tags" {
  description = "Additional tags for instances"
  type        = map(string)
  default     = {}
}

# Object variable
variable "database_config" {
  description = "Database configuration"
  type = object({
    engine         = string
    engine_version = string
    instance_class = string
    storage_gb     = number
    multi_az       = bool
  })
  default = {
    engine         = "postgres"
    engine_version = "15.4"
    instance_class = "db.t3.micro"
    storage_gb     = 20
    multi_az       = false
  }
}

# Complex nested type
variable "vpc_config" {
  type = object({
    cidr_block = string
    subnets = list(object({
      cidr_block        = string
      availability_zone = string
      public            = bool
    }))
  })
}
```

### 3. Output Blocks

```hcl
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web_server.id
}

output "instance_details" {
  description = "Detailed instance information"
  value = {
    id         = aws_instance.web_server.id
    public_ip  = aws_instance.web_server.public_ip
    private_ip = aws_instance.web_server.private_ip
    arn        = aws_instance.web_server.arn
  }
}

output "database_password" {
  description = "Database password"
  value       = random_password.db.result
  sensitive   = true  # Dölj i output
}

# Conditional output
output "load_balancer_dns" {
  description = "Load balancer DNS name"
  value       = var.create_lb ? aws_lb.main[0].dns_name : null
}
```

### 4. Local Values

```hcl
locals {
  # Simple value
  project_name = "myproject"

  # Computed value
  full_name = "${local.project_name}-${var.environment}"

  # Complex computation
  common_tags = {
    Project     = local.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
    CreatedAt   = timestamp()
  }

  # Conditional logic
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

  # Map transformation
  subnet_ids = { for k, v in aws_subnet.main : k => v.id }

  # List filtering
  public_subnets = [for s in var.subnets : s if s.public]
}

# Usage
resource "aws_instance" "web" {
  instance_type = local.instance_type
  tags          = merge(local.common_tags, { Name = local.full_name })
}
```

---

## Data Types

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         HCL DATA TYPES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PRIMITIVE TYPES                                                        │
│  ───────────────                                                        │
│  ┌──────────┬─────────────────────────────────────────────┐            │
│  │ string   │ "hello", "world-${var.env}"                │            │
│  │ number   │ 42, 3.14159                                 │            │
│  │ bool     │ true, false                                 │            │
│  └──────────┴─────────────────────────────────────────────┘            │
│                                                                         │
│  COLLECTION TYPES                                                       │
│  ────────────────                                                       │
│  ┌──────────┬─────────────────────────────────────────────┐            │
│  │ list     │ ["a", "b", "c"]  - Ordered, same type      │            │
│  │ set      │ toset(["a", "b"]) - Unique, unordered      │            │
│  │ map      │ { key = "value" } - Key-value pairs        │            │
│  └──────────┴─────────────────────────────────────────────┘            │
│                                                                         │
│  STRUCTURAL TYPES                                                       │
│  ────────────────                                                       │
│  ┌──────────┬─────────────────────────────────────────────┐            │
│  │ object   │ object({ name = string, port = number })   │            │
│  │ tuple    │ tuple([string, number, bool])               │            │
│  └──────────┴─────────────────────────────────────────────┘            │
│                                                                         │
│  SPECIAL TYPES                                                          │
│  ─────────────                                                          │
│  ┌──────────┬─────────────────────────────────────────────┐            │
│  │ any      │ Accepts any type (use sparingly)            │            │
│  │ null     │ Represents absence of value                 │            │
│  └──────────┴─────────────────────────────────────────────┘            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Type Constraints i Praktiken

```hcl
# list(string) - Lista av strängar
variable "security_groups" {
  type    = list(string)
  default = ["sg-123", "sg-456"]
}

# map(number) - Map med numeriska värden
variable "port_mapping" {
  type = map(number)
  default = {
    http  = 80
    https = 443
    ssh   = 22
  }
}

# set(string) - Unika värden
variable "allowed_ips" {
  type    = set(string)
  default = ["10.0.0.1", "10.0.0.2"]
}

# Complex nested types
variable "services" {
  type = list(object({
    name     = string
    port     = number
    protocol = string
    health_check = object({
      path     = string
      interval = number
    })
  }))
  default = []
}
```

---

## Expressions och References

### Resource References

```hcl
# Referera till annat resource
resource "aws_instance" "web" {
  ami                    = data.aws_ami.latest.id
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.web.id]
  subnet_id              = aws_subnet.public[0].id
}

# Referera till module output
module "vpc" {
  source = "./modules/vpc"
}

resource "aws_instance" "web" {
  subnet_id = module.vpc.public_subnet_ids[0]
}

# Self-reference (inom provisioner/lifecycle)
resource "aws_instance" "web" {
  # ...
  provisioner "local-exec" {
    command = "echo ${self.private_ip}"
  }
}
```

### String Interpolation

```hcl
# Basic interpolation
name = "server-${var.environment}"

# Escape interpolation
description = "Use $${variable} for literal"

# Complex expressions
tags = {
  Name = "${var.project}-${var.environment}-${count.index + 1}"
}

# Heredoc syntax
user_data = <<-EOF
  #!/bin/bash
  echo "Environment: ${var.environment}"
  echo "Instance: ${count.index}"
  apt-get update
  apt-get install -y nginx
EOF

# Strip trailing whitespace
config = <<-EOT
  line 1
  line 2
  EOT
```

### Conditional Expressions

```hcl
# Ternary operator
instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

# Null coalescing (via coalesce)
region = coalesce(var.region, "eu-north-1")

# Complex conditionals
tags = var.enable_tagging ? {
  Name        = var.name
  Environment = var.environment
} : {}

# Conditional resources
resource "aws_eip" "web" {
  count    = var.create_eip ? 1 : 0
  instance = aws_instance.web.id
}
```

### For Expressions

```hcl
# Transform list
upper_names = [for name in var.names : upper(name)]

# Filter list
prod_servers = [for s in var.servers : s if s.environment == "prod"]

# Transform to map
instance_ips = { for i in aws_instance.web : i.tags.Name => i.private_ip }

# Nested for
all_cidrs = flatten([
  for vpc in var.vpcs : [
    for subnet in vpc.subnets : subnet.cidr_block
  ]
])

# Map with conditional
enabled_features = {
  for k, v in var.features : k => v
  if v.enabled
}

# Grouping with ...
by_environment = {
  for s in var.servers : s.environment => s.name...
}
# Result: { "prod" = ["server1", "server2"], "dev" = ["server3"] }
```

### Splat Expressions

```hcl
# Legacy splat (for lists)
instance_ids = aws_instance.web.*.id

# Full splat (recommended)
instance_ids = aws_instance.web[*].id

# Nested attribute
all_public_ips = aws_instance.web[*].network_interface[0].public_ip

# With null handling
ips = try(aws_instance.web[*].public_ip, [])
```

---

## Functions Reference

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TERRAFORM BUILT-IN FUNCTIONS                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  STRING FUNCTIONS                                                       │
│  ────────────────                                                       │
│  format("Hello, %s!", "World")        → "Hello, World!"                │
│  join(", ", ["a", "b", "c"])          → "a, b, c"                      │
│  split(",", "a,b,c")                  → ["a", "b", "c"]                │
│  replace("hello", "l", "L")           → "heLLo"                        │
│  lower("HELLO")                       → "hello"                        │
│  upper("hello")                       → "HELLO"                        │
│  trim("  hello  ")                    → "hello"                        │
│  substr("hello", 0, 3)                → "hel"                          │
│                                                                         │
│  COLLECTION FUNCTIONS                                                   │
│  ────────────────────                                                   │
│  length(["a", "b", "c"])              → 3                              │
│  element(["a", "b", "c"], 1)          → "b"                            │
│  concat([1, 2], [3, 4])               → [1, 2, 3, 4]                   │
│  flatten([[1, 2], [3, 4]])            → [1, 2, 3, 4]                   │
│  distinct([1, 2, 1, 3])               → [1, 2, 3]                      │
│  sort(["b", "a", "c"])                → ["a", "b", "c"]                │
│  reverse([1, 2, 3])                   → [3, 2, 1]                      │
│  contains(["a", "b"], "a")            → true                           │
│  lookup({a="1"}, "a", "default")      → "1"                            │
│  merge({a=1}, {b=2})                  → {a=1, b=2}                     │
│  keys({a=1, b=2})                     → ["a", "b"]                     │
│  values({a=1, b=2})                   → [1, 2]                         │
│  zipmap(["a","b"], [1, 2])            → {a=1, b=2}                     │
│                                                                         │
│  NUMERIC FUNCTIONS                                                      │
│  ─────────────────                                                      │
│  min(1, 2, 3)                         → 1                              │
│  max(1, 2, 3)                         → 3                              │
│  abs(-5)                              → 5                              │
│  ceil(4.1)                            → 5                              │
│  floor(4.9)                           → 4                              │
│                                                                         │
│  TYPE CONVERSION                                                        │
│  ───────────────                                                        │
│  tostring(123)                        → "123"                          │
│  tonumber("123")                      → 123                            │
│  tobool("true")                       → true                           │
│  tolist(toset([1, 2]))               → [1, 2]                         │
│  toset([1, 1, 2])                     → [1, 2]                         │
│  tomap({a = "b"})                     → {a = "b"}                      │
│                                                                         │
│  ENCODING FUNCTIONS                                                     │
│  ──────────────────                                                     │
│  jsonencode({a = 1})                  → '{"a":1}'                      │
│  jsondecode('{"a":1}')                → {a = 1}                        │
│  yamlencode({a = 1})                  → "a: 1\\n"                      │
│  yamldecode("a: 1")                   → {a = 1}                        │
│  base64encode("hello")                → "aGVsbG8="                     │
│  base64decode("aGVsbG8=")             → "hello"                        │
│                                                                         │
│  FILESYSTEM FUNCTIONS                                                   │
│  ────────────────────                                                   │
│  file("./file.txt")                   → file contents                  │
│  fileexists("./file.txt")             → true/false                     │
│  templatefile("./tpl.txt", {v=1})    → rendered template              │
│  abspath("./relative")                → "/absolute/path"               │
│  dirname("/path/to/file.txt")         → "/path/to"                     │
│  basename("/path/to/file.txt")        → "file.txt"                     │
│                                                                         │
│  HASH & CRYPTO FUNCTIONS                                                │
│  ───────────────────────                                                │
│  md5("hello")                         → "5d41402abc4b2a76..."          │
│  sha256("hello")                      → "2cf24dba5fb0a30e..."          │
│  uuid()                               → random UUID                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Praktiska Funktionsexempel

```hcl
# String formatting
locals {
  formatted_name = format("%s-%s-%03d", var.project, var.env, count.index)
  # Result: "myproject-prod-001"
}

# List manipulation
locals {
  sorted_zones   = sort(var.availability_zones)
  unique_tags    = distinct(concat(var.default_tags, var.custom_tags))
  first_zone     = element(var.availability_zones, 0)
}

# Map operations
locals {
  merged_tags = merge(
    var.default_tags,
    var.custom_tags,
    { ManagedBy = "Terraform" }
  )
  tag_keys = keys(local.merged_tags)
}

# Conditional with coalesce
locals {
  region     = coalesce(var.region, data.aws_region.current.name)
  account_id = coalesce(var.account_id, data.aws_caller_identity.current.account_id)
}

# Template rendering
resource "aws_instance" "web" {
  user_data = templatefile("${path.module}/userdata.tftpl", {
    hostname    = var.hostname
    environment = var.environment
    packages    = var.packages
  })
}

# File reading with validation
locals {
  config = fileexists("${path.module}/config.json") ? jsondecode(file("${path.module}/config.json")) : {}
}

# try() for safe access
locals {
  bucket_name = try(aws_s3_bucket.main[0].bucket, null)
  port        = try(var.config.network.port, 8080)
}

# can() for validation
variable "json_data" {
  type = string
  validation {
    condition     = can(jsondecode(var.json_data))
    error_message = "Must be valid JSON."
  }
}
```

---

## Praktiska Övningar

### Övning 1: Typ-experimentering
```hcl
# Skapa variables.tf med olika typer
variable "example_list" {
  type    = list(string)
  default = ["a", "b", "c"]
}

variable "example_map" {
  type = map(object({
    enabled = bool
    port    = number
  }))
  default = {
    web = { enabled = true, port = 80 }
    api = { enabled = true, port = 8080 }
  }
}

# Använd terraform console för att experimentera
# $ terraform console
# > var.example_list[0]
# > var.example_map.web.port
```

### Övning 2: For Expressions
```hcl
locals {
  servers = [
    { name = "web1", env = "prod" },
    { name = "web2", env = "prod" },
    { name = "dev1", env = "dev" }
  ]

  # 1. Extrahera alla namn
  server_names = [for s in local.servers : s.name]

  # 2. Filtrera prod-servrar
  prod_servers = [for s in local.servers : s.name if s.env == "prod"]

  # 3. Skapa map
  server_map = { for s in local.servers : s.name => s.env }
}
```

### Övning 3: Dynamiska Block
```hcl
variable "ingress_rules" {
  default = [
    { port = 80, cidr = "0.0.0.0/0" },
    { port = 443, cidr = "0.0.0.0/0" },
    { port = 22, cidr = "10.0.0.0/8" }
  ]
}

resource "aws_security_group" "example" {
  name = "example"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = [ingress.value.cidr]
    }
  }
}
```

---

**Nästa Node:** Providers Deep Dive →
''',
    "xp_reward": 160,
    "estimated_minutes": 65,
    "prerequisites": ["terraform_node_1"],
    "learning_outcomes": [
        "Behärska HCL syntax och block types",
        "Förstå alla datatyper",
        "Använda expressions och references",
        "Tillämpa funktioner effektivt",
        "Skapa dynamiska konfigurationer"
    ]
}

# Block 1 Part 1 exports
BLOCK_1_PART_1_NODES = [NODE_1, NODE_2]

__all__ = ["NODE_1", "NODE_2", "BLOCK_1_PART_1_NODES"]
