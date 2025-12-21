# =============================================================================
# TERRAFORM SKILLSMAP V3 - BLOCK 4: CI/CD & TESTING (Part 1)
# =============================================================================
# Nodes 13-14: CI/CD Pipelines, Testing
# Ultra-premium bootcamp-quality content (~12,000+ chars per node)
# =============================================================================

NODE_13 = {
    "id": "terraform_node_13",
    "slug": "terraform-cicd-pipelines",
    "title": "Terraform CI/CD Pipelines - Automated Infrastructure",
    "description": "Implement CI/CD pipelines for Terraform deployments",
    "node_id": 13,
    "content": r'''
# Terraform CI/CD Pipelines - Automated Infrastructure

## CI/CD Architecture

```
+-------------------------------------------------------------------------+
|                    TERRAFORM CI/CD PIPELINE                             |
+-------------------------------------------------------------------------+
|                                                                         |
|  +---------+    +-------------------------------------------------+    |
|  | Develop |---▶|              PULL REQUEST                       |    |
|  |  Code   |    |  +--------+  +--------+  +--------+  +-------+ |    |
|  +---------+    |  |  Lint  |-▶|Validate|-▶|  Plan  |-▶|Comment| |    |
|                 |  +--------+  +--------+  +--------+  +-------+ |    |
|                 +-------------------------------------------------+    |
|                                    |                                    |
|                                    | Approved & Merged                  |
|                                    ▼                                    |
|  +-----------------------------------------------------------------+   |
|  |                         MAIN BRANCH                              |   |
|  |  +--------+  +--------+  +--------+  +--------+  +-----------+ |   |
|  |  |  Init  |-▶|  Plan  |-▶| Approve|-▶| Apply  |-▶| Notify    | |   |
|  |  +--------+  +--------+  +--------+  +--------+  +-----------+ |   |
|  +-----------------------------------------------------------------+   |
|                                                                         |
|  STAGES:                                                               |
|  1. Lint & Format - terraform fmt, tflint                             |
|  2. Validate - terraform validate                                     |
|  3. Security - tfsec, checkov                                         |
|  4. Plan - terraform plan                                             |
|  5. Manual Approval (prod)                                            |
|  6. Apply - terraform apply                                           |
|  7. Tests - Integration tests                                         |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## GitHub Actions Pipeline

### Complete Workflow

```yaml
# .github/workflows/terraform.yml
name: Terraform CI/CD

on:
  push:
    branches: [main]
    paths:
      - 'infrastructure/**'
  pull_request:
    branches: [main]
    paths:
      - 'infrastructure/**'

env:
  TF_VERSION: "1.6.4"
  TF_WORKING_DIR: "infrastructure"
  AWS_REGION: "eu-north-1"

permissions:
  id-token: write
  contents: read
  pull-requests: write

jobs:
  # ===========================================
  # Lint and Format Check
  # ===========================================
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Format Check
        id: fmt
        run: terraform fmt -check -recursive
        working-directory: ${{ env.TF_WORKING_DIR }}
        continue-on-error: true

      - name: Setup TFLint
        uses: terraform-linters/setup-tflint@v4

      - name: Run TFLint
        run: tflint --recursive
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Comment on PR (Format Issues)
        if: steps.fmt.outcome == 'failure' && github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '⚠️ Terraform formatting issues detected. Run `terraform fmt -recursive` to fix.'
            })

  # ===========================================
  # Security Scanning
  # ===========================================
  security:
    name: Security Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          working_directory: ${{ env.TF_WORKING_DIR }}
          soft_fail: true

      - name: Run Checkov
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: ${{ env.TF_WORKING_DIR }}
          soft_fail: true
          output_format: sarif
          output_file_path: results.sarif

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: results.sarif

  # ===========================================
  # Terraform Plan
  # ===========================================
  plan:
    name: Terraform Plan
    runs-on: ubuntu-latest
    needs: [lint, security]
    strategy:
      matrix:
        environment: [dev, staging, prod]

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Terraform Init
        run: terraform init
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Select Workspace
        run: |
          terraform workspace select ${{ matrix.environment }} || \
          terraform workspace new ${{ matrix.environment }}
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Plan
        id: plan
        run: |
          terraform plan \
            -var-file="environments/${{ matrix.environment }}.tfvars" \
            -out=tfplan-${{ matrix.environment }} \
            -no-color 2>&1 | tee plan-output.txt
        working-directory: ${{ env.TF_WORKING_DIR }}
        continue-on-error: true

      - name: Upload Plan
        uses: actions/upload-artifact@v4
        with:
          name: tfplan-${{ matrix.environment }}
          path: ${{ env.TF_WORKING_DIR }}/tfplan-${{ matrix.environment }}

      - name: Comment Plan on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const plan = fs.readFileSync('${{ env.TF_WORKING_DIR }}/plan-output.txt', 'utf8');
            const truncated = plan.length > 65000 ? plan.substring(0, 65000) + '\n... (truncated)' : plan;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Terraform Plan - ${{ matrix.environment }}

              <details>
              <summary>Show Plan</summary>

              \`\`\`hcl
              ${truncated}
              \`\`\`
              </details>`
            })

  # ===========================================
  # Terraform Apply (Non-Prod)
  # ===========================================
  apply-nonprod:
    name: Apply Non-Prod
    runs-on: ubuntu-latest
    needs: plan
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    strategy:
      matrix:
        environment: [dev, staging]

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Download Plan
        uses: actions/download-artifact@v4
        with:
          name: tfplan-${{ matrix.environment }}
          path: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Init
        run: terraform init
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Select Workspace
        run: terraform workspace select ${{ matrix.environment }}
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Apply
        run: terraform apply -auto-approve tfplan-${{ matrix.environment }}
        working-directory: ${{ env.TF_WORKING_DIR }}

  # ===========================================
  # Terraform Apply (Production)
  # ===========================================
  apply-prod:
    name: Apply Production
    runs-on: ubuntu-latest
    needs: apply-nonprod
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    environment: production  # Requires manual approval

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_PROD_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Download Plan
        uses: actions/download-artifact@v4
        with:
          name: tfplan-prod
          path: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Init
        run: terraform init
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Select Workspace
        run: terraform workspace select prod
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Terraform Apply
        run: terraform apply -auto-approve tfplan-prod
        working-directory: ${{ env.TF_WORKING_DIR }}

      - name: Slack Notification
        if: always()
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
              "text": "Terraform Production Deployment: ${{ job.status }}",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Terraform Production Deployment*\nStatus: ${{ job.status }}\nCommit: ${{ github.sha }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

---

## GitLab CI Pipeline

```yaml
# .gitlab-ci.yml
image: hashicorp/terraform:1.6.4

stages:
  - validate
  - plan
  - apply

variables:
  TF_ROOT: "infrastructure"
  TF_STATE_NAME: "${CI_PROJECT_NAME}"

cache:
  key: "${TF_ROOT}"
  paths:
    - ${TF_ROOT}/.terraform

before_script:
  - cd ${TF_ROOT}
  - terraform init -backend-config="address=${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/terraform/state/${TF_STATE_NAME}"

# Validate
validate:
  stage: validate
  script:
    - terraform fmt -check -recursive
    - terraform validate
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# Plan for each environment
.plan_template: &plan_definition
  stage: plan
  script:
    - terraform workspace select ${ENVIRONMENT} || terraform workspace new ${ENVIRONMENT}
    - terraform plan -var-file="environments/${ENVIRONMENT}.tfvars" -out=plan.tfplan
  artifacts:
    paths:
      - ${TF_ROOT}/plan.tfplan
    expire_in: 1 week

plan:dev:
  <<: *plan_definition
  variables:
    ENVIRONMENT: dev
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

plan:staging:
  <<: *plan_definition
  variables:
    ENVIRONMENT: staging
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

plan:prod:
  <<: *plan_definition
  variables:
    ENVIRONMENT: prod
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# Apply
.apply_template: &apply_definition
  stage: apply
  script:
    - terraform workspace select ${ENVIRONMENT}
    - terraform apply -auto-approve plan.tfplan

apply:dev:
  <<: *apply_definition
  variables:
    ENVIRONMENT: dev
  needs: ["plan:dev"]
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

apply:staging:
  <<: *apply_definition
  variables:
    ENVIRONMENT: staging
  needs: ["plan:staging"]
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

apply:prod:
  <<: *apply_definition
  variables:
    ENVIRONMENT: prod
  needs: ["plan:prod"]
  when: manual  # Requires manual trigger
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

---

## Terraform Cloud Integration

```hcl
# terraform.tf
terraform {
  cloud {
    organization = "my-organization"

    workspaces {
      tags = ["app:myapp"]
    }
  }
}
```

### GitHub Actions with Terraform Cloud

```yaml
name: Terraform Cloud

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    env:
      TF_CLOUD_ORGANIZATION: "my-organization"
      TF_API_TOKEN: ${{ secrets.TF_API_TOKEN }}
      TF_WORKSPACE: "my-workspace"

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          cli_config_credentials_token: ${{ secrets.TF_API_TOKEN }}

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve
```

---

## Security Best Practices

```
+-------------------------------------------------------------------------+
|                    CI/CD SECURITY BEST PRACTICES                        |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. USE OIDC FOR CLOUD AUTH                                            |
|     • No long-lived credentials                                        |
|     • AWS: role-to-assume                                              |
|     • GCP: workload_identity_provider                                  |
|                                                                         |
|  2. SEPARATE ROLES PER ENVIRONMENT                                     |
|     • dev: Limited permissions                                         |
|     • prod: Stricter controls                                          |
|                                                                         |
|  3. REQUIRE APPROVAL FOR PRODUCTION                                    |
|     • GitHub Environments                                              |
|     • Manual gates                                                     |
|                                                                         |
|  4. SCAN FOR SECRETS                                                   |
|     • gitleaks, truffleHog                                            |
|     • Block commits with secrets                                       |
|                                                                         |
|  5. SECURITY SCANNING                                                  |
|     • tfsec for Terraform                                              |
|     • Checkov for compliance                                           |
|                                                                         |
|  6. LEAST PRIVILEGE                                                    |
|     • Minimal IAM permissions                                          |
|     • Time-limited credentials                                         |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Praktiska Övningar

### Övning 1: Setup GitHub Actions
```yaml
# Implementera en pipeline med:
# 1. Format check
# 2. Validate
# 3. Plan (kommentera på PR)
# 4. Apply (på main branch)
```

### Övning 2: Add Security Scanning
```yaml
# Lägg till:
# 1. tfsec
# 2. checkov
# 3. Cost estimation (infracost)
```

---

**Nästa Node:** Terraform Testing ->
''',
    "xp_reward": 180,
    "estimated_minutes": 70,
    "prerequisites": ["terraform_node_12"],
    "learning_outcomes": [
        "Designa Terraform CI/CD pipelines",
        "Implementera GitHub Actions workflows",
        "Konfigurera GitLab CI för Terraform",
        "Integrera Terraform Cloud",
        "Tillämpa CI/CD säkerhetspraxis"
    ]
}

NODE_14 = {
    "id": "terraform_node_14",
    "slug": "terraform-testing",
    "title": "Terraform Testing - Quality Assurance",
    "description": "Implement testing strategies for Terraform configurations",
    "node_id": 14,
    "content": r'''
# Terraform Testing - Quality Assurance

## Testing Pyramid for IaC

```
+-------------------------------------------------------------------------+
|                    IAC TESTING PYRAMID                                  |
+-------------------------------------------------------------------------+
|                                                                         |
|                          +--------------+                              |
|                         /|  End-to-End  |\                             |
|                        / |    Tests     | \                            |
|                       /  |  (Terratest) |  \                           |
|                      /   +--------------+   \                          |
|                     /                        \                          |
|                    /  +--------------------+  \                        |
|                   /   |  Integration Tests |   \                       |
|                  /    | (terraform test)   |    \                      |
|                 /     +--------------------+     \                     |
|                /                                  \                     |
|               /    +--------------------------+    \                   |
|              /     |      Unit Tests          |     \                  |
|             /      |  (validate, tflint)      |      \                 |
|            /       +--------------------------+       \                |
|           /                                            \               |
|          /   +----------------------------------------+ \              |
|         /    |           Static Analysis              |  \             |
|        /     |    (fmt, tfsec, checkov, sentinel)     |   \            |
|       /      +----------------------------------------+    \           |
|      +------------------------------------------------------+          |
|                                                                         |
|  SPEED  ◀-----------------------------------------------▶  CONFIDENCE |
|  FAST                                                        SLOW     |
|  CHEAP                                                       EXPENSIVE|
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Static Analysis

### terraform fmt

```bash
# Check formatting
terraform fmt -check -recursive -diff

# Auto-fix formatting
terraform fmt -recursive
```

### terraform validate

```bash
# Validate configuration
terraform validate

# JSON output for CI
terraform validate -json | jq .
```

### TFLint

```bash
# Install
brew install tflint

# Run
tflint --recursive

# With config
tflint --config .tflint.hcl
```

```hcl
# .tflint.hcl
config {
  module = true
}

plugin "aws" {
  enabled = true
  version = "0.27.0"
  source  = "github.com/terraform-linters/tflint-ruleset-aws"
}

rule "terraform_naming_convention" {
  enabled = true
  format  = "snake_case"
}

rule "terraform_typed_variables" {
  enabled = true
}

rule "terraform_required_version" {
  enabled = true
}
```

### tfsec

```bash
# Install
brew install tfsec

# Run
tfsec .

# JSON output
tfsec . --format json

# With custom checks
tfsec . --custom-check-dir ./checks
```

### Checkov

```bash
# Install
pip install checkov

# Run
checkov -d .

# Skip specific checks
checkov -d . --skip-check CKV_AWS_18,CKV_AWS_21
```

---

## Terraform Test Framework (1.6+)

### Test File Structure

```
project/
+-- main.tf
+-- variables.tf
+-- outputs.tf
+-- tests/
    +-- setup/
    |   +-- main.tf        # Shared test fixtures
    +-- unit/
    |   +-- variables.tftest.hcl
    +-- integration/
        +-- vpc.tftest.hcl
```

### Basic Test

```hcl
# tests/unit/variables.tftest.hcl

# Test that default values are valid
run "test_default_values" {
  command = plan

  assert {
    condition     = var.environment == "dev"
    error_message = "Default environment should be dev"
  }

  assert {
    condition     = var.instance_count >= 1
    error_message = "Instance count must be at least 1"
  }
}

# Test input validation
run "test_invalid_environment" {
  command = plan

  variables {
    environment = "invalid"
  }

  expect_failures = [
    var.environment
  ]
}
```

### Integration Test

```hcl
# tests/integration/vpc.tftest.hcl

# Setup provider for tests
provider "aws" {
  region = "eu-north-1"
}

# Test VPC creation
run "vpc_creates_with_correct_cidr" {
  command = plan

  variables {
    vpc_cidr = "10.0.0.0/16"
    environment = "test"
  }

  assert {
    condition     = aws_vpc.main.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR should be 10.0.0.0/16"
  }
}

# Test subnet creation
run "creates_correct_number_of_subnets" {
  command = plan

  variables {
    vpc_cidr = "10.0.0.0/16"
    availability_zones = ["eu-north-1a", "eu-north-1b"]
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

# Apply test (creates real resources)
run "vpc_applies_successfully" {
  command = apply

  variables {
    vpc_cidr = "10.99.0.0/16"
    environment = "tftest"
  }

  assert {
    condition     = output.vpc_id != null
    error_message = "VPC ID should be set after apply"
  }

  assert {
    condition     = can(regex("^vpc-", output.vpc_id))
    error_message = "VPC ID should start with vpc-"
  }
}
```

### Running Tests

```bash
# Run all tests
terraform test

# Run specific test file
terraform test -filter=tests/unit/variables.tftest.hcl

# Verbose output
terraform test -verbose

# JSON output
terraform test -json
```

---

## Terratest (Go-based Testing)

### Setup

```go
// test/vpc_test.go
package test

import (
    "testing"
    "fmt"

    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/gruntwork-io/terratest/modules/aws"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/require"
)

func TestVpcModule(t *testing.T) {
    t.Parallel()

    awsRegion := "eu-north-1"

    terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
        TerraformDir: "../modules/vpc",

        Vars: map[string]interface{}{
            "name":               fmt.Sprintf("test-vpc-%s", random.UniqueId()),
            "cidr_block":         "10.99.0.0/16",
            "availability_zones": []string{"eu-north-1a", "eu-north-1b"},
            "environment":        "test",
        },

        EnvVars: map[string]string{
            "AWS_DEFAULT_REGION": awsRegion,
        },
    })

    // Clean up resources when test completes
    defer terraform.Destroy(t, terraformOptions)

    // Run terraform init and apply
    terraform.InitAndApply(t, terraformOptions)

    // Get outputs
    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    publicSubnetIds := terraform.OutputList(t, terraformOptions, "public_subnet_ids")
    privateSubnetIds := terraform.OutputList(t, terraformOptions, "private_subnet_ids")

    // Assertions
    assert.NotEmpty(t, vpcId)
    assert.Equal(t, 2, len(publicSubnetIds))
    assert.Equal(t, 2, len(privateSubnetIds))

    // Verify VPC exists in AWS
    vpc := aws.GetVpcById(t, vpcId, awsRegion)
    assert.Equal(t, "10.99.0.0/16", *vpc.CidrBlock)
}
```

### HTTP Testing

```go
func TestWebServerResponds(t *testing.T) {
    t.Parallel()

    terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
        TerraformDir: "../",
        Vars: map[string]interface{}{
            "environment": "test",
        },
    })

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    // Get the URL of the web server
    url := terraform.Output(t, terraformOptions, "web_url")

    // Verify the web server returns 200 OK
    http_helper.HttpGetWithRetry(
        t,
        url,
        nil,
        200,
        "Hello, World!",
        30,
        5*time.Second,
    )
}
```

### Running Terratest

```bash
# Install dependencies
go mod init test
go mod tidy

# Run tests
go test -v -timeout 30m

# Run specific test
go test -v -run TestVpcModule

# Parallel tests
go test -v -parallel 4
```

---

## Policy as Code

### Sentinel (Terraform Cloud/Enterprise)

```python
# policies/require-tags.sentinel
import "tfplan/v2" as tfplan

mandatory_tags = ["Environment", "Owner", "Project"]

allResources = filter tfplan.resource_changes as _, rc {
    rc.mode is "managed" and
    (rc.change.actions contains "create" or rc.change.actions contains "update")
}

taggedResources = filter allResources as _, rc {
    rc.change.after.tags is not null
}

main = rule {
    all taggedResources as _, resource {
        all mandatory_tags as tag {
            resource.change.after.tags contains tag
        }
    }
}
```

### OPA (Open Policy Agent)

```rego
# policy/required_tags.rego
package terraform.analysis

required_tags := {"Environment", "Owner", "Project"}

deny[msg] {
    resource := input.resource_changes[_]
    resource.mode == "managed"
    resource.type == "aws_instance"

    provided_tags := {key | resource.change.after.tags[key]}
    missing_tags := required_tags - provided_tags
    count(missing_tags) > 0

    msg := sprintf("Instance %v is missing required tags: %v", [resource.address, missing_tags])
}
```

```bash
# Run OPA evaluation
terraform plan -out=tfplan
terraform show -json tfplan > tfplan.json
opa eval -i tfplan.json -d policy/ "data.terraform.analysis.deny"
```

---

## Test Automation

### Makefile

```makefile
# Makefile
.PHONY: fmt validate lint security test test-unit test-integration

fmt:
	terraform fmt -recursive

validate:
	terraform validate

lint:
	tflint --recursive

security:
	tfsec .
	checkov -d .

test-unit:
	terraform test -filter=tests/unit/

test-integration:
	terraform test -filter=tests/integration/

test: test-unit test-integration

ci: fmt validate lint security test

clean:
	rm -rf .terraform
	rm -f terraform.tfstate*
	rm -f *.tfplan
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.86.0
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tflint
      - id: terraform_tfsec
      - id: terraform_docs
        args:
          - --hook-config=--path-to-file=README.md
          - --hook-config=--add-to-existing-file=true
          - --hook-config=--create-file-if-not-exist=true

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-merge-conflict
      - id: end-of-file-fixer
      - id: trailing-whitespace
```

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run -a
```

---

## Praktiska Övningar

### Övning 1: Setup Test Suite
```bash
# 1. Skapa test directory
mkdir -p tests/{unit,integration}

# 2. Skapa basic validation test
# 3. Kör terraform test
```

### Övning 2: Write Terratest
```go
// Skriv test som:
// 1. Skapar EC2 instance
// 2. Verifierar SSH connectivity
// 3. Kör cleanup
```

### Övning 3: Add Pre-commit
```yaml
# Konfigurera pre-commit med:
# 1. terraform_fmt
# 2. terraform_validate
# 3. tflint
# 4. tfsec
```

---

**Nästa Node:** Terraform Security ->
''',
    "xp_reward": 180,
    "estimated_minutes": 70,
    "prerequisites": ["terraform_node_13"],
    "learning_outcomes": [
        "Implementera Terraform testing pyramid",
        "Använda terraform test framework",
        "Skriva Terratest-tester",
        "Konfigurera policy as code",
        "Automatisera tester med pre-commit"
    ]
}

# Block 4 Part 1 exports
BLOCK_4_PART_1_NODES = [NODE_13, NODE_14]

__all__ = ["NODE_13", "NODE_14", "BLOCK_4_PART_1_NODES"]
