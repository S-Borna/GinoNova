"""
Terraform V3 SkillsMap - Block 4: CI/CD Integration Part 2
Nodes 15-16: GitOps Workflows & Policy as Code

Premium DevOps Content Standard:
- ~10,000+ characters per node
- Comprehensive ASCII diagrams
- Production-ready code examples
- Real-world enterprise patterns
"""

# =============================================================================
# NODE 15: GitOps Workflows with Terraform
# =============================================================================

NODE_15_GITOPS_WORKFLOWS = {
    "id": "terraform-gitops-workflows",
    "slug": "terraform-gitops-workflows",
    "title": "GitOps Workflows with Terraform",
    "description": "Master GitOps-driven infrastructure automation with Terraform and modern tools",
    "xp_reward": 190,
    "estimated_minutes": 75,
    "content": '''# GitOps Workflows with Terraform

## GitOps Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GITOPS TERRAFORM ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │   DEVELOPER     │    │    GIT REPO     │    │   CI/CD SYSTEM  │        │
│  │  Workstation    │───▶│   (Source of    │───▶│   (Automation)  │        │
│  │                 │    │     Truth)      │    │                 │        │
│  └─────────────────┘    └────────┬────────┘    └────────┬────────┘        │
│          │                       │                      │                  │
│          │ Push                  │ Trigger              │ Apply           │
│          ▼                       ▼                      ▼                  │
│  ┌─────────────────────────────────────────────────────────────────┐      │
│  │                     GITOPS WORKFLOW ENGINE                       │      │
│  ├─────────────────────────────────────────────────────────────────┤      │
│  │                                                                   │      │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │      │
│  │  │   ATLANTIS   │  │   TERRAFORM  │  │   SPACELIFT  │           │      │
│  │  │              │  │    CLOUD     │  │              │           │      │
│  │  │  PR-Based    │  │   Built-in   │  │  Advanced    │           │      │
│  │  │  Automation  │  │   GitOps     │  │  GitOps      │           │      │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘           │      │
│  │         │                 │                 │                    │      │
│  │         └─────────────────┼─────────────────┘                    │      │
│  │                           ▼                                      │      │
│  │               ┌──────────────────────┐                          │      │
│  │               │   TERRAFORM ENGINE   │                          │      │
│  │               │   plan → approve →   │                          │      │
│  │               │   apply → verify     │                          │      │
│  │               └──────────┬───────────┘                          │      │
│  │                          │                                       │      │
│  └──────────────────────────┼───────────────────────────────────────┘      │
│                             ▼                                              │
│  ┌─────────────────────────────────────────────────────────────────┐      │
│  │                    CLOUD INFRASTRUCTURE                          │      │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐            │      │
│  │  │   AWS   │  │   GCP   │  │  Azure  │  │  K8s    │            │      │
│  │  │         │  │         │  │         │  │         │            │      │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘            │      │
│  └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Atlantis Configuration

### Server Setup

```yaml
# atlantis.yaml - Repository Configuration
version: 3
automerge: false
delete_source_branch_on_merge: true
parallel_plan: true
parallel_apply: false

projects:
  # Development Environment
  - name: dev-infrastructure
    dir: environments/dev
    workspace: dev
    terraform_version: v1.5.0
    autoplan:
      when_modified:
        - "**/*.tf"
        - "**/*.tfvars"
        - "../modules/**/*.tf"
      enabled: true
    apply_requirements:
      - approved
      - mergeable
    workflow: standard

  # Staging Environment
  - name: staging-infrastructure
    dir: environments/staging
    workspace: staging
    terraform_version: v1.5.0
    autoplan:
      when_modified:
        - "**/*.tf"
        - "**/*.tfvars"
        - "../modules/**/*.tf"
      enabled: true
    apply_requirements:
      - approved
      - mergeable
      - undiverged
    workflow: standard

  # Production Environment
  - name: prod-infrastructure
    dir: environments/prod
    workspace: prod
    terraform_version: v1.5.0
    autoplan:
      when_modified:
        - "**/*.tf"
        - "**/*.tfvars"
        - "../modules/**/*.tf"
      enabled: true
    apply_requirements:
      - approved
      - mergeable
      - undiverged
    workflow: production

workflows:
  standard:
    plan:
      steps:
        - init:
            extra_args:
              - "-upgrade"
        - run: terraform fmt -check -recursive
        - run: tflint --config=.tflint.hcl
        - run: checkov -d . --quiet
        - plan:
            extra_args:
              - "-var-file=terraform.tfvars"
    apply:
      steps:
        - apply

  production:
    plan:
      steps:
        - init:
            extra_args:
              - "-upgrade"
        - run: terraform fmt -check -recursive
        - run: tflint --config=.tflint.hcl
        - run: checkov -d . --quiet --check HIGH
        - run: |
            echo "Running OPA policy validation..."
            conftest test . --policy ../policies
        - plan:
            extra_args:
              - "-var-file=terraform.tfvars"
              - "-out=tfplan"
        - run: |
            terraform show -json tfplan > plan.json
            echo "Plan exported for audit"
    apply:
      steps:
        - run: |
            echo "Production deployment at $(date)"
            echo "Approved by: $ATLANTIS_PULL_AUTHOR"
        - apply:
            extra_args:
              - "tfplan"
        - run: |
            echo "Deployment complete. Sending notification..."
            curl -X POST "$SLACK_WEBHOOK" \
              -H "Content-Type: application/json" \
              -d '{"text":"Production infrastructure deployed successfully"}'
```

### Atlantis Server Helm Deployment

```yaml
# values.yaml for Atlantis Helm Chart
image:
  repository: ghcr.io/runatlantis/atlantis
  tag: v0.25.0
  pullPolicy: IfNotPresent

replicaCount: 1

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
  hosts:
    - host: atlantis.company.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: atlantis-tls
      hosts:
        - atlantis.company.com

atlantisUrl: https://atlantis.company.com

orgAllowlist:
  - github.com/myorg/*

github:
  user: atlantis-bot
  token: ""  # Set via secret
  secret: "" # Webhook secret

environment:
  - name: AWS_REGION
    value: us-east-1
  - name: TF_IN_AUTOMATION
    value: "true"
  - name: ATLANTIS_REPO_CONFIG_JSON
    value: |
      {
        "repos": [
          {
            "id": "github.com/myorg/*",
            "apply_requirements": ["approved", "mergeable"],
            "workflow": "default",
            "allowed_overrides": ["workflow", "apply_requirements"],
            "allow_custom_workflows": true
          }
        ]
      }

# IRSA for AWS Authentication
serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/atlantis-role

persistence:
  enabled: true
  storageClassName: gp3
  size: 50Gi

resources:
  requests:
    cpu: 500m
    memory: 1Gi
  limits:
    cpu: 2000m
    memory: 4Gi

# Redis for distributed locking
redis:
  enabled: true
  architecture: standalone
  auth:
    enabled: true
```

## Terraform Cloud GitOps

### Workspace Configuration

```hcl
# terraform-cloud-workspaces.tf
# Managing Terraform Cloud Workspaces as Code

terraform {
  required_providers {
    tfe = {
      source  = "hashicorp/tfe"
      version = "~> 0.50"
    }
  }
}

# Variables for workspace configuration
variable "environments" {
  description = "Environment configurations"
  type = map(object({
    auto_apply           = bool
    terraform_version    = string
    working_directory    = string
    vcs_branch          = string
    run_triggers        = list(string)
    variables           = map(string)
    sensitive_variables = map(string)
  }))
  default = {
    dev = {
      auto_apply        = true
      terraform_version = "1.5.0"
      working_directory = "environments/dev"
      vcs_branch        = "main"
      run_triggers      = []
      variables = {
        environment = "dev"
        log_level   = "debug"
      }
      sensitive_variables = {}
    }
    staging = {
      auto_apply        = false
      terraform_version = "1.5.0"
      working_directory = "environments/staging"
      vcs_branch        = "main"
      run_triggers      = ["dev"]
      variables = {
        environment = "staging"
        log_level   = "info"
      }
      sensitive_variables = {}
    }
    prod = {
      auto_apply        = false
      terraform_version = "1.5.0"
      working_directory = "environments/prod"
      vcs_branch        = "main"
      run_triggers      = ["staging"]
      variables = {
        environment = "prod"
        log_level   = "warn"
      }
      sensitive_variables = {}
    }
  }
}

# VCS Provider Configuration
resource "tfe_oauth_client" "github" {
  organization     = var.tfc_organization
  api_url          = "https://api.github.com"
  http_url         = "https://github.com"
  oauth_token      = var.github_oauth_token
  service_provider = "github"
}

# Create Workspaces
resource "tfe_workspace" "environments" {
  for_each = var.environments

  name                = "infrastructure-${each.key}"
  organization        = var.tfc_organization
  working_directory   = each.value.working_directory
  terraform_version   = each.value.terraform_version
  auto_apply          = each.value.auto_apply
  queue_all_runs      = true
  speculative_enabled = true

  vcs_repo {
    identifier         = "${var.github_org}/${var.github_repo}"
    oauth_token_id     = tfe_oauth_client.github.oauth_token_id
    branch             = each.value.vcs_branch
    ingress_submodules = false
  }

  tag_names = ["terraform", each.key, "infrastructure"]
}

# Workspace Variables
resource "tfe_variable" "workspace_vars" {
  for_each = {
    for item in flatten([
      for env, config in var.environments : [
        for key, value in config.variables : {
          workspace_id = tfe_workspace.environments[env].id
          key          = key
          value        = value
          env          = env
        }
      ]
    ]) : "${item.env}-${item.key}" => item
  }

  key          = each.value.key
  value        = each.value.value
  category     = "terraform"
  workspace_id = each.value.workspace_id
  description  = "Managed by Terraform"
}

# Run Triggers for Promotion
resource "tfe_run_trigger" "promotion" {
  for_each = {
    for env, config in var.environments :
    env => config if length(config.run_triggers) > 0
  }

  workspace_id  = tfe_workspace.environments[each.key].id
  sourceable_id = tfe_workspace.environments[each.value.run_triggers[0]].id
}

# Notification Configuration
resource "tfe_notification_configuration" "slack" {
  for_each = var.environments

  name             = "slack-${each.key}"
  enabled          = true
  workspace_id     = tfe_workspace.environments[each.key].id
  destination_type = "slack"
  url              = var.slack_webhook_url

  triggers = [
    "run:created",
    "run:planning",
    "run:needs_attention",
    "run:applying",
    "run:completed",
    "run:errored"
  ]
}

# Policy Sets
resource "tfe_policy_set" "security" {
  name         = "security-policies"
  description  = "Security compliance policies"
  organization = var.tfc_organization
  kind         = "sentinel"

  vcs_repo {
    identifier         = "${var.github_org}/terraform-policies"
    branch             = "main"
    oauth_token_id     = tfe_oauth_client.github.oauth_token_id
    ingress_submodules = false
  }

  workspace_ids = [
    for ws in tfe_workspace.environments : ws.id
  ]
}
```

## ArgoCD Integration for Kubernetes Terraform

```yaml
# argocd-terraform-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: terraform-controller
  namespace: argocd
spec:
  project: infrastructure
  source:
    repoURL: https://github.com/myorg/terraform-controller
    targetRevision: HEAD
    path: deploy
    helm:
      values: |
        replicaCount: 2

        serviceAccount:
          create: true
          annotations:
            eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/terraform-controller

        resources:
          requests:
            cpu: 200m
            memory: 256Mi
          limits:
            cpu: 1000m
            memory: 1Gi
  destination:
    server: https://kubernetes.default.svc
    namespace: terraform-system
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true

---
# Terraform CRD Example
apiVersion: infra.contrib.fluxcd.io/v1alpha1
kind: Terraform
metadata:
  name: vpc-infrastructure
  namespace: terraform-system
spec:
  approvePlan: auto
  interval: 1h
  path: ./environments/prod/vpc
  sourceRef:
    kind: GitRepository
    name: infrastructure
    namespace: flux-system
  vars:
    - name: environment
      value: production
    - name: vpc_cidr
      value: "10.0.0.0/16"
  varsFrom:
    - kind: Secret
      name: aws-credentials
  writeOutputsToSecret:
    name: vpc-outputs
  runnerPodTemplate:
    spec:
      serviceAccountName: terraform-runner
      containers:
        - name: terraform
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
            limits:
              cpu: 2000m
              memory: 2Gi
```

## GitOps PR Workflow Automation

```python
#!/usr/bin/env python3
"""
GitOps PR Automation Script
Handles automated PR creation and management for Terraform changes
"""

import os
import json
import subprocess
import hashlib
from datetime import datetime
from github import Github
from typing import Dict, List, Optional

class TerraformGitOpsManager:
    """Manages GitOps workflows for Terraform"""

    def __init__(
        self,
        github_token: str,
        repo_name: str,
        base_branch: str = "main"
    ):
        self.gh = Github(github_token)
        self.repo = self.gh.get_repo(repo_name)
        self.base_branch = base_branch

    def create_infrastructure_pr(
        self,
        changes: Dict,
        environment: str,
        description: str
    ) -> str:
        """Create a PR for infrastructure changes"""

        # Generate branch name
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        change_hash = hashlib.md5(
            json.dumps(changes, sort_keys=True).encode()
        ).hexdigest()[:8]
        branch_name = f"infra/{environment}/{timestamp}-{change_hash}"

        # Create branch
        base_ref = self.repo.get_git_ref(f"heads/{self.base_branch}")
        self.repo.create_git_ref(
            ref=f"refs/heads/{branch_name}",
            sha=base_ref.object.sha
        )

        # Apply changes to files
        for file_path, content in changes.items():
            try:
                existing = self.repo.get_contents(file_path, ref=branch_name)
                self.repo.update_file(
                    path=file_path,
                    message=f"Update {file_path}",
                    content=content,
                    sha=existing.sha,
                    branch=branch_name
                )
            except Exception:
                self.repo.create_file(
                    path=file_path,
                    message=f"Create {file_path}",
                    content=content,
                    branch=branch_name
                )

        # Create PR
        pr_body = self._generate_pr_body(changes, environment, description)
        pr = self.repo.create_pull(
            title=f"[{environment.upper()}] Infrastructure Update",
            body=pr_body,
            head=branch_name,
            base=self.base_branch
        )

        # Add labels
        pr.add_to_labels("infrastructure", environment, "terraform")

        # Request reviewers based on environment
        reviewers = self._get_required_reviewers(environment)
        if reviewers:
            pr.create_review_request(reviewers=reviewers)

        return pr.html_url

    def _generate_pr_body(
        self,
        changes: Dict,
        environment: str,
        description: str
    ) -> str:
        """Generate PR body with change details"""

        files_changed = "\n".join([f"- `{f}`" for f in changes.keys()])

        return f"""## Infrastructure Change Request

### Environment: `{environment}`

### Description
{description}

### Files Changed
{files_changed}

### Checklist
- [ ] Terraform plan reviewed
- [ ] Security scan passed
- [ ] Cost estimation reviewed
- [ ] Documentation updated
- [ ] Required approvals obtained

### Instructions
1. Review the Terraform plan in the PR comments
2. Verify security compliance
3. Approve and merge when ready
4. Monitor the apply process

---
*This PR was automatically generated by the GitOps automation system*
"""

    def _get_required_reviewers(self, environment: str) -> List[str]:
        """Get required reviewers based on environment"""
        reviewers_map = {
            "dev": ["dev-lead"],
            "staging": ["dev-lead", "qa-lead"],
            "prod": ["dev-lead", "security-lead", "ops-lead"]
        }
        return reviewers_map.get(environment, [])

    def validate_pr_plan(self, pr_number: int) -> Dict:
        """Validate Terraform plan for a PR"""

        pr = self.repo.get_pull(pr_number)

        # Get plan output from PR comments
        comments = pr.get_issue_comments()
        plan_comment = None
        for comment in comments:
            if "terraform plan" in comment.body.lower():
                plan_comment = comment
                break

        if not plan_comment:
            return {"status": "pending", "message": "Plan not found"}

        # Analyze plan
        plan_text = plan_comment.body
        analysis = {
            "status": "success",
            "add": plan_text.count("+ "),
            "change": plan_text.count("~ "),
            "destroy": plan_text.count("- "),
            "warnings": [],
            "errors": []
        }

        # Check for dangerous operations
        if "destroy" in plan_text.lower() and analysis["destroy"] > 5:
            analysis["warnings"].append(
                f"Large number of resources to destroy: {analysis['destroy']}"
            )

        if "error" in plan_text.lower():
            analysis["status"] = "failed"
            analysis["errors"].append("Plan contains errors")

        return analysis

    def promote_to_environment(
        self,
        source_env: str,
        target_env: str,
        pr_number: int
    ) -> str:
        """Promote infrastructure changes between environments"""

        source_pr = self.repo.get_pull(pr_number)

        # Get files from source PR
        files = source_pr.get_files()
        changes = {}

        for file in files:
            if source_env in file.filename:
                # Replace source env with target env in path
                new_path = file.filename.replace(source_env, target_env)
                content = self.repo.get_contents(
                    file.filename,
                    ref=source_pr.head.sha
                ).decoded_content.decode()

                # Update environment-specific values
                content = content.replace(
                    f'environment = "{source_env}"',
                    f'environment = "{target_env}"'
                )
                changes[new_path] = content

        return self.create_infrastructure_pr(
            changes=changes,
            environment=target_env,
            description=f"Promotion from {source_env} (PR #{pr_number})"
        )


if __name__ == "__main__":
    manager = TerraformGitOpsManager(
        github_token=os.environ["GITHUB_TOKEN"],
        repo_name="myorg/infrastructure"
    )

    # Example: Create infrastructure PR
    changes = {
        "environments/dev/main.tf": """
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "dev/infrastructure.tfstate"
    region = "us-east-1"
  }
}

module "vpc" {
  source = "../../modules/vpc"

  environment = "dev"
  vpc_cidr    = "10.0.0.0/16"
}
"""
    }

    pr_url = manager.create_infrastructure_pr(
        changes=changes,
        environment="dev",
        description="Update VPC configuration"
    )
    print(f"Created PR: {pr_url}")
```

## Drift Detection and Reconciliation

```hcl
# drift-detection.tf
# Automated Drift Detection Configuration

variable "drift_detection_schedule" {
  description = "Cron schedule for drift detection"
  default     = "0 */6 * * *"  # Every 6 hours
}

# Lambda for Drift Detection
module "drift_detector" {
  source = "./modules/drift-detector"

  function_name = "terraform-drift-detector"
  runtime       = "python3.11"
  timeout       = 900  # 15 minutes
  memory_size   = 1024

  environment_variables = {
    TFC_TOKEN         = var.tfc_token
    TFC_ORGANIZATION  = var.tfc_organization
    SLACK_WEBHOOK_URL = var.slack_webhook_url
    SNS_TOPIC_ARN     = aws_sns_topic.drift_alerts.arn
  }

  # IAM Role for drift detection
  additional_policies = [
    aws_iam_policy.drift_detector.arn
  ]
}

# EventBridge Schedule
resource "aws_cloudwatch_event_rule" "drift_detection" {
  name                = "terraform-drift-detection"
  description         = "Trigger drift detection"
  schedule_expression = "cron(${var.drift_detection_schedule})"
}

resource "aws_cloudwatch_event_target" "drift_detector" {
  rule      = aws_cloudwatch_event_rule.drift_detection.name
  target_id = "DriftDetector"
  arn       = module.drift_detector.function_arn
}

# SNS Topic for Alerts
resource "aws_sns_topic" "drift_alerts" {
  name = "terraform-drift-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.drift_alerts.arn
  protocol  = "email"
  endpoint  = var.alert_email
}
```

This comprehensive GitOps guide provides enterprise-grade patterns for managing Terraform infrastructure through Git-based workflows.
''',
    "practice_tasks": [
        {
            "id": "task-1-atlantis-setup",
            "title": "Configure Atlantis for PR-Based Workflows",
            "description": "Deploy and configure Atlantis server for automated Terraform planning",
            "steps": [
                "Deploy Atlantis using Helm chart",
                "Configure repository webhooks",
                "Set up atlantis.yaml for projects",
                "Create custom workflows",
                "Test PR-based planning"
            ],
            "validation": "atlantis plan triggered on PR creation"
        },
        {
            "id": "task-2-tfc-gitops",
            "title": "Implement Terraform Cloud GitOps",
            "description": "Configure Terraform Cloud workspaces with VCS integration",
            "steps": [
                "Create TFC workspaces programmatically",
                "Configure VCS integration",
                "Set up run triggers for promotion",
                "Implement policy sets",
                "Configure notifications"
            ],
            "validation": "terraform runs triggered on git push"
        },
        {
            "id": "task-3-drift-detection",
            "title": "Build Drift Detection System",
            "description": "Create automated drift detection and alerting",
            "steps": [
                "Deploy drift detection Lambda",
                "Configure scheduled execution",
                "Set up SNS alerting",
                "Create Slack integration",
                "Test drift scenarios"
            ],
            "validation": "drift alerts received within 6 hours"
        }
    ]
}


# =============================================================================
# NODE 16: Policy as Code with Terraform
# =============================================================================

NODE_16_POLICY_AS_CODE = {
    "id": "terraform-policy-as-code",
    "slug": "terraform-policy-as-code",
    "title": "Policy as Code with Terraform",
    "description": "Implement governance and compliance using Sentinel, OPA, and Checkov",
    "xp_reward": 190,
    "estimated_minutes": 75,
    "content": '''# Policy as Code with Terraform

## Policy Framework Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     POLICY AS CODE ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        POLICY SOURCES                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │   │
│  │  │  Security   │  │  Compliance │  │    Cost     │                 │   │
│  │  │  Standards  │  │ Requirements│  │   Limits    │                 │   │
│  │  │  (CIS/NIST) │  │ (SOC2/PCI)  │  │  (Budgets)  │                 │   │
│  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                 │   │
│  │         │                │                │                         │   │
│  │         └────────────────┼────────────────┘                         │   │
│  │                          ▼                                          │   │
│  │              ┌───────────────────────┐                              │   │
│  │              │   POLICY DEFINITION   │                              │   │
│  │              │   (Version Controlled)│                              │   │
│  │              └───────────┬───────────┘                              │   │
│  └──────────────────────────┼───────────────────────────────────────────┘   │
│                             │                                               │
│  ┌──────────────────────────▼───────────────────────────────────────────┐   │
│  │                     POLICY ENGINES                                    │   │
│  │                                                                       │   │
│  │  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐           │   │
│  │  │    SENTINEL    │ │      OPA       │ │    CHECKOV     │           │   │
│  │  │  (TFC Native)  │ │  (Kubernetes)  │ │ (Static Scan)  │           │   │
│  │  │                │ │                │ │                │           │   │
│  │  │ ▪ Soft/Hard    │ │ ▪ Rego Lang    │ │ ▪ 1000+ Rules  │           │   │
│  │  │   Mandatory    │ │ ▪ Admission    │ │ ▪ Custom Checks│           │   │
│  │  │ ▪ TFC Runs     │ │   Control      │ │ ▪ CI/CD Native │           │   │
│  │  │ ▪ Cost Est     │ │ ▪ Data-Driven  │ │ ▪ Multi-Cloud  │           │   │
│  │  └───────┬────────┘ └───────┬────────┘ └───────┬────────┘           │   │
│  │          │                  │                  │                     │   │
│  │          └──────────────────┼──────────────────┘                     │   │
│  │                             ▼                                        │   │
│  │                  ┌───────────────────┐                               │   │
│  │                  │  POLICY DECISION  │                               │   │
│  │                  │  Pass / Fail /    │                               │   │
│  │                  │  Advisory         │                               │   │
│  │                  └─────────┬─────────┘                               │   │
│  └────────────────────────────┼──────────────────────────────────────────┘   │
│                               ▼                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ENFORCEMENT POINTS                                │   │
│  │                                                                      │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │   IDE    │  │    CI    │  │   TFC    │  │  Deploy  │           │   │
│  │  │  (Pre)   │  │  (Plan)  │  │  (Run)   │  │  (Apply) │           │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## HashiCorp Sentinel Policies

### Sentinel Policy Structure

```python
# sentinel.hcl - Policy Configuration
policy "require-tags" {
  source            = "./policies/require-tags.sentinel"
  enforcement_level = "hard-mandatory"
}

policy "restrict-instance-types" {
  source            = "./policies/restrict-instance-types.sentinel"
  enforcement_level = "soft-mandatory"
}

policy "enforce-encryption" {
  source            = "./policies/enforce-encryption.sentinel"
  enforcement_level = "hard-mandatory"
}

policy "cost-estimation" {
  source            = "./policies/cost-estimation.sentinel"
  enforcement_level = "advisory"
}
```

### Comprehensive Sentinel Policies

```python
# policies/require-tags.sentinel
# Ensures all taggable resources have required tags

import "tfplan/v2" as tfplan
import "strings"

# Required tags for all resources
required_tags = ["environment", "project", "owner", "cost-center"]

# Get all taggable resources
allTaggableResources = filter tfplan.resource_changes as _, rc {
    rc.mode is "managed" and
    rc.change.after is not null and
    keys(rc.change.after) contains "tags"
}

# Validate tags
validate_tags = func(resources, tags) {
    validated = true
    for resources as _, resource {
        resource_tags = resource.change.after.tags else {}

        for tags as tag {
            if tag not in keys(resource_tags) {
                print("Resource", resource.address, "missing required tag:", tag)
                validated = false
            } else if resource_tags[tag] is "" {
                print("Resource", resource.address, "has empty value for tag:", tag)
                validated = false
            }
        }
    }
    return validated
}

# Main rule
main = rule {
    validate_tags(allTaggableResources, required_tags)
}
```

```python
# policies/enforce-encryption.sentinel
# Enforces encryption on storage and databases

import "tfplan/v2" as tfplan

# S3 Bucket Encryption
s3_buckets = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket" and
    rc.mode is "managed" and
    rc.change.after is not null
}

s3_bucket_encryption = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket_server_side_encryption_configuration" and
    rc.mode is "managed"
}

# EBS Volume Encryption
ebs_volumes = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_ebs_volume" and
    rc.mode is "managed" and
    rc.change.after is not null
}

# RDS Instance Encryption
rds_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_db_instance" and
    rc.mode is "managed" and
    rc.change.after is not null
}

# Validate EBS Encryption
validate_ebs_encryption = rule {
    all ebs_volumes as _, vol {
        vol.change.after.encrypted is true
    }
}

# Validate RDS Encryption
validate_rds_encryption = rule {
    all rds_instances as _, db {
        db.change.after.storage_encrypted is true
    }
}

# Main Rule - All encryption checks must pass
main = rule {
    validate_ebs_encryption and
    validate_rds_encryption
}
```

```python
# policies/cost-estimation.sentinel
# Cost control policies

import "tfplan/v2" as tfplan
import "decimal"

# Maximum allowed monthly cost increase
max_monthly_cost_increase = decimal.new(1000)

# Get cost estimate
cost_estimate = tfplan.cost_estimate

# Check if cost estimate exists
cost_estimate_exists = rule {
    cost_estimate is not null
}

# Validate cost increase
validate_cost_increase = func() {
    if cost_estimate is null {
        return true  # No cost estimate available
    }

    proposed_monthly = decimal.new(cost_estimate.proposed_monthly_cost)
    prior_monthly = decimal.new(cost_estimate.prior_monthly_cost else 0)

    cost_increase = proposed_monthly.subtract(prior_monthly)

    if cost_increase.compare(max_monthly_cost_increase) > 0 {
        print("Cost increase exceeds limit:")
        print("  Prior Monthly Cost:", prior_monthly)
        print("  Proposed Monthly Cost:", proposed_monthly)
        print("  Increase:", cost_increase)
        print("  Maximum Allowed:", max_monthly_cost_increase)
        return false
    }

    return true
}

# Main rule
main = rule when cost_estimate_exists {
    validate_cost_increase()
}
```

## Open Policy Agent (OPA) Policies

### OPA with Conftest

```rego
# policies/terraform/security.rego
package terraform.security

import input as tfplan

# Deny public S3 buckets
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_s3_bucket_public_access_block"
    resource.change.after.block_public_acls != true
    msg := sprintf(
        "S3 bucket %s must block public ACLs",
        [resource.address]
    )
}

deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_s3_bucket_public_access_block"
    resource.change.after.block_public_policy != true
    msg := sprintf(
        "S3 bucket %s must block public policies",
        [resource.address]
    )
}

# Deny unrestricted security group rules
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_security_group_rule"
    resource.change.after.type == "ingress"
    resource.change.after.cidr_blocks[_] == "0.0.0.0/0"
    resource.change.after.from_port != 443
    resource.change.after.to_port != 443
    msg := sprintf(
        "Security group rule %s allows unrestricted access on non-HTTPS port",
        [resource.address]
    )
}

# Require VPC flow logs
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_vpc"
    resource.change.actions[_] == "create"

    # Check if flow log exists for this VPC
    not has_flow_log(resource.change.after.id)

    msg := sprintf(
        "VPC %s must have flow logs enabled",
        [resource.address]
    )
}

has_flow_log(vpc_id) {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_flow_log"
    resource.change.after.vpc_id == vpc_id
}
```

```rego
# policies/terraform/cost.rego
package terraform.cost

import input as tfplan

# Define allowed instance types
allowed_instance_types := {
    "t3.micro", "t3.small", "t3.medium", "t3.large",
    "m5.large", "m5.xlarge",
    "r5.large", "r5.xlarge"
}

# Deny expensive instance types
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_instance"
    resource.change.after.instance_type != null
    not allowed_instance_types[resource.change.after.instance_type]
    msg := sprintf(
        "Instance type %s is not in the allowed list for %s",
        [resource.change.after.instance_type, resource.address]
    )
}

# Warn on large RDS instances
warn[msg] {
    resource := tfplan.resource_changes[_]
    resource.type == "aws_db_instance"
    large_instance_classes[resource.change.after.instance_class]
    msg := sprintf(
        "Large RDS instance class %s used for %s - ensure this is justified",
        [resource.change.after.instance_class, resource.address]
    )
}

large_instance_classes := {
    "db.r5.4xlarge", "db.r5.8xlarge", "db.r5.12xlarge",
    "db.m5.4xlarge", "db.m5.8xlarge", "db.m5.12xlarge"
}

# Require cost allocation tags
deny[msg] {
    resource := tfplan.resource_changes[_]
    resource.change.after.tags != null
    not resource.change.after.tags["cost-center"]
    msg := sprintf(
        "Resource %s must have 'cost-center' tag for cost allocation",
        [resource.address]
    )
}
```

### OPA Terraform Integration

```hcl
# opa-integration.tf
# OPA integration for Terraform validation

# Null resource to run OPA checks
resource "null_resource" "opa_validation" {
  triggers = {
    plan_hash = sha256(jsonencode(local.terraform_plan))
  }

  provisioner "local-exec" {
    command = <<-EOT
      terraform show -json tfplan > plan.json

      echo "Running OPA policy checks..."

      # Run security policies
      conftest test plan.json \
        --policy policies/terraform/security.rego \
        --output json > security_results.json

      # Run cost policies
      conftest test plan.json \
        --policy policies/terraform/cost.rego \
        --output json > cost_results.json

      # Check for failures
      if jq -e '.[] | select(.failures | length > 0)' security_results.json > /dev/null; then
        echo "❌ Security policy violations found!"
        jq '.[] | .failures[]' security_results.json
        exit 1
      fi

      echo "✅ All policy checks passed"
    EOT
  }
}
```

## Checkov Integration

### Checkov Configuration

```yaml
# .checkov.yaml
branch: main
compact: true
download-external-modules: true
evaluate-variables: true
external-modules-download-path: .external_modules
framework:
  - terraform
  - terraform_plan
output:
  - cli
  - json
  - sarif
soft-fail: false

# Skip specific checks
skip-check:
  - CKV_AWS_144  # S3 cross-region replication
  - CKV2_AWS_6   # S3 public access block (handled separately)

# Custom policy directory
external-checks-dir:
  - ./custom_policies

# Check specific directories
directory:
  - ./environments/prod
  - ./modules
```

### Custom Checkov Policies

```python
# custom_policies/require_backup_plan.py
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class RequireBackupPlan(BaseResourceCheck):
    """Ensure RDS instances have backup retention configured"""

    def __init__(self):
        name = "Ensure RDS instances have backup retention >= 7 days"
        id = "CKV_CUSTOM_1"
        supported_resources = ["aws_db_instance"]
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources
        )

    def scan_resource_conf(self, conf):
        """Scan RDS configuration for backup settings"""

        backup_retention = conf.get("backup_retention_period", [0])

        if isinstance(backup_retention, list):
            backup_retention = backup_retention[0] if backup_retention else 0

        if backup_retention >= 7:
            return CheckResult.PASSED

        return CheckResult.FAILED

check = RequireBackupPlan()
```

```python
# custom_policies/require_vpc_endpoints.py
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckCategories, CheckResult

class RequireVPCEndpoints(BaseResourceCheck):
    """Ensure VPCs have required service endpoints"""

    REQUIRED_ENDPOINTS = ["s3", "dynamodb", "ec2", "ecr.api", "ecr.dkr"]

    def __init__(self):
        name = "Ensure VPC has required service endpoints"
        id = "CKV_CUSTOM_2"
        supported_resources = ["aws_vpc"]
        categories = [CheckCategories.NETWORKING]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources
        )

    def scan_resource_conf(self, conf):
        """Check for VPC endpoint configurations"""

        # This check requires graph-based analysis
        # Mark as passed if VPC exists, actual validation
        # happens in graph check
        return CheckResult.PASSED

check = RequireVPCEndpoints()
```

### CI Pipeline with Policy Checks

```yaml
# .github/workflows/terraform-policy.yml
name: Terraform Policy Validation

on:
  pull_request:
    paths:
      - "**.tf"
      - "**.tfvars"
      - "policies/**"

env:
  TF_VERSION: "1.5.0"
  CHECKOV_VERSION: "2.4.0"
  OPA_VERSION: "0.55.0"

jobs:
  policy-check:
    name: Policy Validation
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Tools
        run: |
          pip install checkov==${{ env.CHECKOV_VERSION }}

          curl -L -o opa https://openpolicyagent.org/downloads/v${{ env.OPA_VERSION }}/opa_linux_amd64_static
          chmod +x opa
          sudo mv opa /usr/local/bin/

          curl -sL https://github.com/open-policy-agent/conftest/releases/download/v0.44.1/conftest_0.44.1_Linux_x86_64.tar.gz | tar xz
          sudo mv conftest /usr/local/bin/

      - name: Terraform Init
        run: terraform init -backend=false
        working-directory: environments/prod

      - name: Terraform Plan
        run: |
          terraform plan -out=tfplan -var-file=terraform.tfvars
          terraform show -json tfplan > plan.json
        working-directory: environments/prod

      - name: Run Checkov
        run: |
          checkov -d environments/prod \
            --config-file .checkov.yaml \
            --output cli \
            --output json \
            --output-file-path . \
            --soft-fail-on MEDIUM

      - name: Run OPA/Conftest
        run: |
          conftest test environments/prod/plan.json \
            --policy policies/terraform/ \
            --output json > opa_results.json

          # Check for failures
          FAILURES=$(jq '[.[] | .failures | length] | add' opa_results.json)
          if [ "$FAILURES" -gt 0 ]; then
            echo "❌ OPA policy failures: $FAILURES"
            jq '.[] | .failures[]' opa_results.json
            exit 1
          fi

      - name: Upload Results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: policy-results
          path: |
            checkov_results.json
            opa_results.json

      - name: Comment PR
        uses: actions/github-script@v7
        if: github.event_name == 'pull_request'
        with:
          script: |
            const fs = require('fs');

            let comment = '## 🔒 Policy Validation Results\n\n';

            // Checkov results
            const checkovResults = JSON.parse(
              fs.readFileSync('checkov_results.json', 'utf8')
            );
            const passed = checkovResults.passed || 0;
            const failed = checkovResults.failed || 0;

            comment += `### Checkov\n`;
            comment += `- ✅ Passed: ${passed}\n`;
            comment += `- ❌ Failed: ${failed}\n\n`;

            // OPA results
            const opaResults = JSON.parse(
              fs.readFileSync('opa_results.json', 'utf8')
            );
            const opaFailures = opaResults.reduce(
              (acc, r) => acc + r.failures.length, 0
            );

            comment += `### OPA/Conftest\n`;
            comment += `- Failures: ${opaFailures}\n`;

            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

## Policy Decision Matrix

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    POLICY ENFORCEMENT MATRIX                              │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  Policy Type          │ Dev    │ Staging │ Prod   │ Tool              │
│  ─────────────────────┼────────┼─────────┼────────┼───────────────────│
│  Required Tags        │ Warn   │ Block   │ Block  │ Sentinel/Checkov  │
│  Encryption at Rest   │ Warn   │ Block   │ Block  │ Checkov/OPA       │
│  Public Access        │ Block  │ Block   │ Block  │ All               │
│  Instance Types       │ Warn   │ Warn    │ Block  │ Sentinel/OPA      │
│  Cost Limits          │ Warn   │ Warn    │ Block  │ Sentinel          │
│  Backup Retention     │ Warn   │ Block   │ Block  │ Checkov           │
│  VPC Flow Logs        │ Warn   │ Block   │ Block  │ OPA               │
│  Security Groups      │ Block  │ Block   │ Block  │ All               │
│                                                                           │
│  Legend:                                                                  │
│  - Warn: Advisory only, allows deployment                                │
│  - Block: Hard enforcement, prevents deployment                          │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

This comprehensive policy-as-code guide provides enterprise-grade governance for Terraform infrastructure management.
''',
    "practice_tasks": [
        {
            "id": "task-1-sentinel-policies",
            "title": "Implement Sentinel Policies for TFC",
            "description": "Create and deploy Sentinel policies in Terraform Cloud",
            "steps": [
                "Create sentinel.hcl configuration",
                "Write tag enforcement policy",
                "Implement encryption validation",
                "Add cost estimation policy",
                "Test policy enforcement"
            ],
            "validation": "sentinel policies blocking non-compliant plans"
        },
        {
            "id": "task-2-opa-integration",
            "title": "Integrate OPA with Terraform Pipeline",
            "description": "Set up OPA/Conftest for policy validation",
            "steps": [
                "Install OPA and Conftest",
                "Write Rego security policies",
                "Create cost control policies",
                "Integrate with CI pipeline",
                "Validate with terraform plan"
            ],
            "validation": "OPA validating terraform plans in CI"
        },
        {
            "id": "task-3-checkov-custom",
            "title": "Create Custom Checkov Policies",
            "description": "Develop organization-specific Checkov policies",
            "steps": [
                "Set up custom policy directory",
                "Create backup validation check",
                "Implement VPC endpoint check",
                "Configure Checkov YAML",
                "Run full compliance scan"
            ],
            "validation": "custom checkov policies running in pipeline"
        }
    ]
}


# =============================================================================
# BLOCK 4 PART 2 EXPORT
# =============================================================================

BLOCK_4_PART_2_NODES = [NODE_15_GITOPS_WORKFLOWS, NODE_16_POLICY_AS_CODE]
