"""
Terraform Part 3 - Multi-Cloud & Advanced Providers
"""

TASKS_PART3 = [
    {
        "title": "Multi-Cloud Infrastructure",
        "slug": "multi-cloud",
        "description": "Deploy infrastructure across AWS, Azure, and GCP",
        "difficulty": "advanced",
        "xp_reward": 250,
        "estimated_minutes": 65,
        "content": """# Multi-Cloud Infrastructure

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



## Multi-Provider Configuration

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
}

# Azure Provider
provider "azurerm" {
  features {}
  subscription_id = var.azure_subscription_id
}

# GCP Provider
provider "google" {
  project = var.gcp_project_id
  region  = "us-central1"
}
```

## Cross-Cloud VPC/VNet/Network

```hcl
# AWS VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "multi-cloud-aws"
  }
}

# Azure Virtual Network
resource "azurerm_resource_group" "main" {
  name     = "multi-cloud-rg"
  location = "East US"
}

resource "azurerm_virtual_network" "main" {
  name                = "multi-cloud-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

# GCP VPC
resource "google_compute_network" "main" {
  name                    = "multi-cloud-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "main" {
  name          = "multi-cloud-subnet"
  ip_cidr_range = "10.2.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.main.id
}
```

## Cross-Cloud Connectivity

```hcl
# AWS VPN Gateway
resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "multi-cloud-vpn-gw"
  }
}

# Azure VPN Gateway
resource "azurerm_virtual_network_gateway" "main" {
  name                = "multi-cloud-vpn-gw"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  type     = "Vpn"
  vpn_type = "RouteBased"

  active_active = false
  enable_bgp    = false
  sku           = "VpnGw1"

  ip_configuration {
    name                          = "vnetGatewayConfig"
    public_ip_address_id          = azurerm_public_ip.vpn.id
    private_ip_address_allocation = "Dynamic"
    subnet_id                     = azurerm_subnet.gateway.id
  }
}
```

## Abstracted Multi-Cloud Module

```hcl
# modules/compute/main.tf
variable "cloud_provider" {
  type = string
  validation {
    condition     = contains(["aws", "azure", "gcp"], var.cloud_provider)
    error_message = "Must be aws, azure, or gcp."
  }
}

# AWS
resource "aws_instance" "main" {
  count = var.cloud_provider == "aws" ? 1 : 0

  ami           = var.aws_ami
  instance_type = var.instance_size

  tags = var.tags
}

# Azure
resource "azurerm_linux_virtual_machine" "main" {
  count = var.cloud_provider == "azure" ? 1 : 0

  name                = var.name
  resource_group_name = var.azure_resource_group
  location            = var.azure_location
  size                = var.instance_size

  admin_username = "adminuser"

  admin_ssh_key {
    username   = "adminuser"
    public_key = var.ssh_public_key
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

# GCP
resource "google_compute_instance" "main" {
  count = var.cloud_provider == "gcp" ? 1 : 0

  name         = var.name
  machine_type = var.instance_size
  zone         = var.gcp_zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = var.gcp_network

    access_config {}
  }
}

output "instance_id" {
  value = coalesce(
    try(aws_instance.main[0].id, null),
    try(azurerm_linux_virtual_machine.main[0].id, null),
    try(google_compute_instance.main[0].id, null)
  )
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    },
    {
        "title": "Kubernetes Provider & Resources",
        "slug": "kubernetes-provider",
        "description": "Manage Kubernetes resources with Terraform",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 55,
        "content": """# Kubernetes Provider & Resources

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



## Provider Configuration

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.11"
    }
  }
}

# Using kubeconfig
provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "my-cluster"
}

# Using EKS
provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority[0].data)

  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", var.cluster_name]
  }
}
```

## Kubernetes Resources

```hcl
# Namespace
resource "kubernetes_namespace" "app" {
  metadata {
    name = "my-app"

    labels = {
      environment = var.environment
    }
  }
}

# ConfigMap
resource "kubernetes_config_map" "app" {
  metadata {
    name      = "app-config"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  data = {
    "app.properties" = <<-EOF
      database.host=${var.db_host}
      database.port=5432
      log.level=info
    EOF
  }
}

# Secret
resource "kubernetes_secret" "app" {
  metadata {
    name      = "app-secrets"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  data = {
    "db-password" = var.db_password
    "api-key"     = var.api_key
  }

  type = "Opaque"
}

# Deployment
resource "kubernetes_deployment" "app" {
  metadata {
    name      = "my-app"
    namespace = kubernetes_namespace.app.metadata[0].name

    labels = {
      app = "my-app"
    }
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        app = "my-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }

      spec {
        container {
          name  = "app"
          image = "${var.image_repository}:${var.image_tag}"

          port {
            container_port = 8080
          }

          env_from {
            config_map_ref {
              name = kubernetes_config_map.app.metadata[0].name
            }
          }

          env {
            name = "DB_PASSWORD"
            value_from {
              secret_key_ref {
                name = kubernetes_secret.app.metadata[0].name
                key  = "db-password"
              }
            }
          }

          resources {
            limits = {
              cpu    = "500m"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "256Mi"
            }
          }

          liveness_probe {
            http_get {
              path = "/health"
              port = 8080
            }
            initial_delay_seconds = 30
            period_seconds        = 10
          }
        }
      }
    }
  }
}

# Service
resource "kubernetes_service" "app" {
  metadata {
    name      = "my-app"
    namespace = kubernetes_namespace.app.metadata[0].name
  }

  spec {
    selector = {
      app = "my-app"
    }

    port {
      port        = 80
      target_port = 8080
    }

    type = "ClusterIP"
  }
}

# Ingress
resource "kubernetes_ingress_v1" "app" {
  metadata {
    name      = "my-app"
    namespace = kubernetes_namespace.app.metadata[0].name

    annotations = {
      "kubernetes.io/ingress.class"    = "nginx"
      "cert-manager.io/cluster-issuer" = "letsencrypt-prod"
    }
  }

  spec {
    tls {
      hosts       = ["app.example.com"]
      secret_name = "app-tls"
    }

    rule {
      host = "app.example.com"

      http {
        path {
          path      = "/"
          path_type = "Prefix"

          backend {
            service {
              name = kubernetes_service.app.metadata[0].name
              port {
                number = 80
              }
            }
          }
        }
      }
    }
  }
}
```

## Helm Provider

```hcl
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

# Install Helm chart
resource "helm_release" "nginx_ingress" {
  name       = "nginx-ingress"
  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"
  namespace  = "ingress-nginx"
  version    = "4.7.1"

  create_namespace = true

  set {
    name  = "controller.replicaCount"
    value = "2"
  }

  set {
    name  = "controller.service.type"
    value = "LoadBalancer"
  }

  values = [
    file("${path.module}/values/nginx-ingress.yaml")
  ]
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    },
    {
        "title": "Database & Storage Providers",
        "slug": "database-storage",
        "description": "Provision and configure databases and storage",
        "difficulty": "intermediate",
        "xp_reward": 200,
        "estimated_minutes": 50,
        "content": """# Database & Storage Providers

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



## RDS PostgreSQL

```hcl
resource "aws_db_subnet_group" "main" {
  name       = "${var.environment}-db-subnet"
  subnet_ids = var.private_subnet_ids

  tags = {
    Name = "${var.environment}-db-subnet-group"
  }
}

resource "aws_db_instance" "postgres" {
  identifier = "${var.environment}-postgres"

  engine         = "postgres"
  engine_version = "15.4"
  instance_class = var.db_instance_class

  allocated_storage     = 100
  max_allocated_storage = 500
  storage_type          = "gp3"
  storage_encrypted     = true

  db_name  = var.db_name
  username = var.db_username
  password = var.db_password
  port     = 5432

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.db.id]

  multi_az               = var.environment == "prod"
  publicly_accessible    = false
  deletion_protection    = var.environment == "prod"
  skip_final_snapshot    = var.environment != "prod"
  final_snapshot_identifier = var.environment == "prod" ? "${var.environment}-final-snapshot" : null

  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "Mon:04:00-Mon:05:00"

  performance_insights_enabled = true

  tags = {
    Environment = var.environment
  }
}

# Read replica
resource "aws_db_instance" "replica" {
  count = var.create_replica ? 1 : 0

  identifier = "${var.environment}-postgres-replica"

  replicate_source_db = aws_db_instance.postgres.identifier
  instance_class      = var.db_instance_class

  publicly_accessible  = false
  skip_final_snapshot  = true

  tags = {
    Environment = var.environment
    Role        = "replica"
  }
}
```

## Aurora Cluster

```hcl
resource "aws_rds_cluster" "aurora" {
  cluster_identifier = "${var.environment}-aurora"

  engine         = "aurora-postgresql"
  engine_version = "15.4"

  database_name   = var.db_name
  master_username = var.db_username
  master_password = var.db_password

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.db.id]

  storage_encrypted = true

  backup_retention_period = 7
  preferred_backup_window = "03:00-04:00"

  skip_final_snapshot = var.environment != "prod"

  serverlessv2_scaling_configuration {
    min_capacity = 0.5
    max_capacity = 16
  }
}

resource "aws_rds_cluster_instance" "aurora" {
  count = var.aurora_instance_count

  identifier         = "${var.environment}-aurora-${count.index}"
  cluster_identifier = aws_rds_cluster.aurora.id

  instance_class = "db.serverless"
  engine         = aws_rds_cluster.aurora.engine
  engine_version = aws_rds_cluster.aurora.engine_version
}
```

## S3 with Lifecycle

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "${var.environment}-data-${data.aws_caller_identity.current.account_id}"

  tags = {
    Environment = var.environment
  }
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
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.s3.arn
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "data" {
  bucket = aws_s3_bucket.data.id

  rule {
    id     = "archive-old-objects"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }

    noncurrent_version_transition {
      noncurrent_days = 30
      storage_class   = "GLACIER"
    }

    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}
```

## ElastiCache Redis

```hcl
resource "aws_elasticache_subnet_group" "main" {
  name       = "${var.environment}-cache-subnet"
  subnet_ids = var.private_subnet_ids
}

resource "aws_elasticache_replication_group" "redis" {
  replication_group_id = "${var.environment}-redis"
  description          = "Redis cluster for ${var.environment}"

  node_type            = var.redis_node_type
  num_cache_clusters   = var.redis_num_nodes
  port                 = 6379

  engine               = "redis"
  engine_version       = "7.0"
  parameter_group_name = "default.redis7"

  subnet_group_name  = aws_elasticache_subnet_group.main.name
  security_group_ids = [aws_security_group.redis.id]

  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  auth_token                 = var.redis_auth_token

  automatic_failover_enabled = var.environment == "prod"
  multi_az_enabled          = var.environment == "prod"

  snapshot_retention_limit = 7
  snapshot_window         = "03:00-05:00"

  tags = {
    Environment = var.environment
  }
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    },
    {
        "title": "CI/CD Integration",
        "slug": "cicd-integration",
        "description": "Integrate Terraform with CI/CD pipelines",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 55,
        "content": """# CI/CD Integration

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



## GitHub Actions

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  push:
    branches: [main]
    paths:
      - 'terraform/**'
  pull_request:
    branches: [main]
    paths:
      - 'terraform/**'

env:
  TF_VERSION: '1.6.0'
  TF_WORKING_DIR: './terraform'

jobs:
  terraform:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      pull-requests: write
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Format
        id: fmt
        run: terraform fmt -check
        working-directory: ${{ env.TF_WORKING_DIR }}
        continue-on-error: true

      - name: Terraform Init
        id: init
        run: terraform init
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Validate
        id: validate
        run: terraform validate -no-color
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Plan
        id: plan
        if: github.event_name == 'pull_request'
        run: terraform plan -no-color -out=tfplan
        working-directory: ${{ env.TF_WORKING_DIR }}
        continue-on-error: true

      - name: Update PR
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

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve tfplan
        working-directory: ${{ env.TF_WORKING_DIR }}
```

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - plan
  - apply

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform

image:
  name: hashicorp/terraform:1.6
  entrypoint: [""]

.terraform-init: &terraform-init
  - cd ${TF_ROOT}
  - terraform init -backend-config="address=${TF_STATE_ADDRESS}"

validate:
  stage: validate
  script:
    - *terraform-init
    - terraform validate
    - terraform fmt -check
  rules:
    - changes:
        - terraform/**/*

plan:
  stage: plan
  script:
    - *terraform-init
    - terraform plan -out=plan.tfplan
  artifacts:
    paths:
      - ${TF_ROOT}/plan.tfplan
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - terraform/**/*

apply:
  stage: apply
  script:
    - *terraform-init
    - terraform apply -auto-approve plan.tfplan
  dependencies:
    - plan
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      changes:
        - terraform/**/*
      when: manual
  environment:
    name: production
```

## Atlantis

```yaml
# atlantis.yaml
version: 3
projects:
  - name: infrastructure
    dir: terraform/infrastructure
    workspace: default
    terraform_version: v1.6.0
    autoplan:
      when_modified: ["*.tf", "*.tfvars"]
      enabled: true
    apply_requirements: [approved, mergeable]

  - name: applications
    dir: terraform/applications
    workspace: default
    terraform_version: v1.6.0
    autoplan:
      when_modified: ["*.tf"]
      enabled: true

workflows:
  default:
    plan:
      steps:
        - init
        - plan:
            extra_args: ["-var-file", "prod.tfvars"]
    apply:
      steps:
        - apply
```

## AWS CodePipeline

```hcl
resource "aws_codepipeline" "terraform" {
  name     = "terraform-pipeline"
  role_arn = aws_iam_role.codepipeline.arn

  artifact_store {
    type     = "S3"
    location = aws_s3_bucket.artifacts.bucket
  }

  stage {
    name = "Source"

    action {
      name             = "Source"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["source_output"]

      configuration = {
        ConnectionArn    = aws_codestarconnections_connection.github.arn
        FullRepositoryId = "org/terraform-repo"
        BranchName       = "main"
      }
    }
  }

  stage {
    name = "Plan"

    action {
      name            = "TerraformPlan"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      input_artifacts = ["source_output"]
      version         = "1"

      configuration = {
        ProjectName = aws_codebuild_project.terraform_plan.name
      }
    }
  }

  stage {
    name = "Approve"

    action {
      name     = "ManualApproval"
      category = "Approval"
      owner    = "AWS"
      provider = "Manual"
      version  = "1"
    }
  }

  stage {
    name = "Apply"

    action {
      name            = "TerraformApply"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      input_artifacts = ["source_output"]
      version         = "1"

      configuration = {
        ProjectName = aws_codebuild_project.terraform_apply.name
      }
    }
  }
}
```


> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.
"""
    },
    {
        "title": "Policy as Code with Sentinel",
        "slug": "policy-sentinel",
        "description": "Implement governance with Sentinel policies",
        "difficulty": "advanced",
        "xp_reward": 225,
        "estimated_minutes": 55,
        "content": """# Policy as Code with Sentinel

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



## Sentinel Basics

```sentinel
# policies/require-tags.sentinel
import "tfplan/v2" as tfplan

# Required tags
required_tags = ["Environment", "Owner", "Project"]

# Get all resources with tags
all_resources_with_tags = filter tfplan.resource_changes as _, rc {
    rc.mode is "managed" and
    rc.change.after.tags is not null
}

# Check for required tags
deny_missing_tags = rule {
    all all_resources_with_tags as _, resource {
        all required_tags as tag {
            resource.change.after.tags contains tag
        }
    }
}

main = rule {
    deny_missing_tags
}
```

## Cost Control Policy

```sentinel
# policies/cost-control.sentinel
import "tfplan/v2" as tfplan
import "decimal"

# Maximum monthly cost in dollars
max_monthly_cost = 1000

# Instance type costs (simplified)
instance_costs = {
    "t3.micro":  7.30,
    "t3.small":  14.60,
    "t3.medium": 29.20,
    "t3.large":  58.40,
    "t3.xlarge": 116.80,
}

# Calculate EC2 costs
ec2_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_instance" and
    rc.mode is "managed" and
    rc.change.actions contains "create"
}

total_cost = 0
for ec2_instances as _, instance {
    instance_type = instance.change.after.instance_type
    if instance_costs contains instance_type {
        total_cost = total_cost + instance_costs[instance_type]
    }
}

# Cost limit rule
cost_under_limit = rule {
    total_cost < max_monthly_cost
}

main = rule {
    cost_under_limit
}
```

## Security Policy

```sentinel
# policies/security.sentinel
import "tfplan/v2" as tfplan

# Deny public S3 buckets
s3_buckets = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket" and
    rc.mode is "managed"
}

deny_public_buckets = rule {
    all s3_buckets as _, bucket {
        bucket.change.after.acl is not "public-read" and
        bucket.change.after.acl is not "public-read-write"
    }
}

# Require encryption on RDS
rds_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_db_instance" and
    rc.mode is "managed" and
    rc.change.actions contains "create"
}

require_rds_encryption = rule {
    all rds_instances as _, rds {
        rds.change.after.storage_encrypted is true
    }
}

# Deny open security groups
security_groups = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_security_group" and
    rc.mode is "managed"
}

deny_open_ingress = rule {
    all security_groups as _, sg {
        all sg.change.after.ingress as _, ingress {
            ingress.cidr_blocks not contains "0.0.0.0/0" or
            ingress.from_port is 443 or
            ingress.from_port is 80
        }
    }
}

main = rule {
    deny_public_buckets and
    require_rds_encryption and
    deny_open_ingress
}
```

## OPA/Conftest Alternative

```rego
# policy/terraform.rego
package terraform

# Deny unencrypted S3 buckets
deny[msg] {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"
    resource.change.after.server_side_encryption_configuration == null

    msg := sprintf("S3 bucket '%s' must have encryption enabled", [resource.name])
}

# Require tags
required_tags := {"Environment", "Owner", "Project"}

deny[msg] {
    resource := input.resource_changes[_]
    resource.change.after.tags != null
    missing := required_tags - {tag | resource.change.after.tags[tag]}
    count(missing) > 0

    msg := sprintf("Resource '%s' is missing required tags: %v", [resource.name, missing])
}

# Instance size limits
allowed_instance_types := {"t3.micro", "t3.small", "t3.medium"}

deny[msg] {
    resource := input.resource_changes[_]
    resource.type == "aws_instance"
    not allowed_instance_types[resource.change.after.instance_type]

    msg := sprintf("Instance '%s' uses disallowed type: %s", [
        resource.name,
        resource.change.after.instance_type
    ])
}
```

```bash
# Run Conftest
terraform plan -out=tfplan
terraform show -json tfplan > tfplan.json
conftest test tfplan.json -p policy/
```

## Policy Testing

```sentinel
# policies/test/require-tags/pass.hcl
mock "tfplan/v2" {
    module {
        source = "mock-tfplan-pass.sentinel"
    }
}

test {
    rules = {
        main = true
    }
}

# policies/test/require-tags/fail.hcl
mock "tfplan/v2" {
    module {
        source = "mock-tfplan-fail.sentinel"
    }
}

test {
    rules = {
        main = false
    }
}
```


> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.
"""
    }
]
