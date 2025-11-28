"""
Bootcamp Seed Data - 10 Modules with comprehensive DevOps curriculum
Phase C.1: Seed Bootcamp Content

Each module contains 5-15 tasks covering the core competencies
for a complete DevOps Engineer bootcamp.
"""
from typing import Literal

DifficultyLevel = Literal["easy", "medium", "hard"]


# =============================================================================
# MODULE DEFINITIONS
# =============================================================================

BOOTCAMP_MODULES: list[dict] = [
    # -------------------------------------------------------------------------
    # Module 01: Onboarding
    # -------------------------------------------------------------------------
    {
        "name": "Module 01 · Onboarding",
        "description": "Welcome to the DevOps Bootcamp! Get set up and ready to learn.",
        "tasks": [
            {
                "title": "Complete your profile setup",
                "description": "Fill out your profile with bio, goals, and avatar to personalize your learning journey.",
                "difficulty": "easy",
            },
            {
                "title": "Take the pre-assessment quiz",
                "description": "Assess your current knowledge level to customize your learning path.",
                "difficulty": "easy",
            },
            {
                "title": "Join the community Discord",
                "description": "Connect with fellow learners and get access to support channels.",
                "difficulty": "easy",
            },
            {
                "title": "Set up your local dev environment",
                "description": "Install VS Code, Git, and essential extensions for the course.",
                "difficulty": "easy",
            },
            {
                "title": "Create your first GitHub account",
                "description": "Sign up for GitHub and configure your profile and SSH keys.",
                "difficulty": "easy",
            },
            {
                "title": "Read the bootcamp roadmap",
                "description": "Familiarize yourself with the curriculum structure and milestones.",
                "difficulty": "easy",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 02: Foundations
    # -------------------------------------------------------------------------
    {
        "name": "Module 02 · Foundations",
        "description": "Core concepts of DevOps culture, principles, and practices.",
        "tasks": [
            {
                "title": "What is DevOps?",
                "description": "Learn the history, philosophy, and goals of the DevOps movement.",
                "difficulty": "easy",
            },
            {
                "title": "The DevOps lifecycle explained",
                "description": "Understand the 8 phases: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor.",
                "difficulty": "easy",
            },
            {
                "title": "CI/CD fundamentals",
                "description": "Introduction to Continuous Integration and Continuous Delivery concepts.",
                "difficulty": "medium",
            },
            {
                "title": "Infrastructure as Code overview",
                "description": "Learn why IaC is critical for modern infrastructure management.",
                "difficulty": "medium",
            },
            {
                "title": "Configuration management basics",
                "description": "Understand declarative vs imperative approaches to system configuration.",
                "difficulty": "medium",
            },
            {
                "title": "DevOps metrics and KPIs",
                "description": "Learn about DORA metrics: deployment frequency, lead time, MTTR, change failure rate.",
                "difficulty": "medium",
            },
            {
                "title": "The Three Ways of DevOps",
                "description": "Deep dive into Flow, Feedback, and Continuous Learning principles.",
                "difficulty": "medium",
            },
            {
                "title": "Quiz: DevOps Foundations",
                "description": "Test your understanding of core DevOps concepts and principles.",
                "difficulty": "easy",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 03: Linux Basics
    # -------------------------------------------------------------------------
    {
        "name": "Module 03 · Linux Basics",
        "description": "Essential Linux skills every DevOps engineer must master.",
        "tasks": [
            {
                "title": "Linux distributions overview",
                "description": "Compare Ubuntu, CentOS, Alpine, and other popular distros.",
                "difficulty": "easy",
            },
            {
                "title": "File system navigation",
                "description": "Master cd, ls, pwd, find, and locate commands.",
                "difficulty": "easy",
            },
            {
                "title": "File permissions and ownership",
                "description": "Understand chmod, chown, and the Unix permission model.",
                "difficulty": "medium",
            },
            {
                "title": "Process management",
                "description": "Learn ps, top, htop, kill, and systemctl for process control.",
                "difficulty": "medium",
            },
            {
                "title": "Package management",
                "description": "Master apt, yum, and apk package managers.",
                "difficulty": "medium",
            },
            {
                "title": "User and group management",
                "description": "Create users, groups, and manage sudo permissions.",
                "difficulty": "medium",
            },
            {
                "title": "Text processing tools",
                "description": "Use grep, sed, awk, and cut for log analysis.",
                "difficulty": "hard",
            },
            {
                "title": "Disk and storage management",
                "description": "Learn df, du, mount, fdisk, and LVM basics.",
                "difficulty": "hard",
            },
            {
                "title": "System logs and journalctl",
                "description": "Navigate /var/log and use journalctl for systemd logging.",
                "difficulty": "medium",
            },
            {
                "title": "Lab: Set up a Linux VM",
                "description": "Create an Ubuntu VM using VirtualBox or Multipass.",
                "difficulty": "medium",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 04: Shell Scripting
    # -------------------------------------------------------------------------
    {
        "name": "Module 04 · Shell Scripting",
        "description": "Automate tasks with Bash scripts and command-line mastery.",
        "tasks": [
            {
                "title": "Bash basics and syntax",
                "description": "Learn shebang, variables, quoting, and basic script structure.",
                "difficulty": "easy",
            },
            {
                "title": "Control structures",
                "description": "Master if/else, case statements, and conditional expressions.",
                "difficulty": "medium",
            },
            {
                "title": "Loops and iteration",
                "description": "Use for, while, and until loops for repetitive tasks.",
                "difficulty": "medium",
            },
            {
                "title": "Functions in Bash",
                "description": "Create reusable functions with arguments and return values.",
                "difficulty": "medium",
            },
            {
                "title": "Input/output and redirection",
                "description": "Master stdin, stdout, stderr, pipes, and here documents.",
                "difficulty": "medium",
            },
            {
                "title": "Command substitution and expansion",
                "description": "Use $(), ${}, and arithmetic expansion effectively.",
                "difficulty": "hard",
            },
            {
                "title": "Error handling and debugging",
                "description": "Implement set -e, trap, and debug with set -x.",
                "difficulty": "hard",
            },
            {
                "title": "Working with arrays",
                "description": "Create and manipulate indexed and associative arrays.",
                "difficulty": "hard",
            },
            {
                "title": "Lab: Backup automation script",
                "description": "Write a script to backup files with rotation and logging.",
                "difficulty": "hard",
            },
            {
                "title": "Lab: System health check script",
                "description": "Create a script that monitors CPU, memory, and disk usage.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 05: Git & GitHub
    # -------------------------------------------------------------------------
    {
        "name": "Module 05 · Git & GitHub",
        "description": "Version control mastery with Git and GitHub collaboration.",
        "tasks": [
            {
                "title": "Git basics: init, add, commit",
                "description": "Learn the fundamental Git workflow for tracking changes.",
                "difficulty": "easy",
            },
            {
                "title": "Branching and merging",
                "description": "Create branches, merge changes, and resolve conflicts.",
                "difficulty": "medium",
            },
            {
                "title": "Remote repositories",
                "description": "Push, pull, fetch, and work with GitHub remotes.",
                "difficulty": "medium",
            },
            {
                "title": "Git rebase vs merge",
                "description": "Understand when to use rebase and interactive rebasing.",
                "difficulty": "hard",
            },
            {
                "title": "Pull requests and code review",
                "description": "Create PRs, review code, and use GitHub review features.",
                "difficulty": "medium",
            },
            {
                "title": "GitHub Actions basics",
                "description": "Create your first CI workflow with GitHub Actions.",
                "difficulty": "medium",
            },
            {
                "title": "Branch protection rules",
                "description": "Configure required reviews, status checks, and restrictions.",
                "difficulty": "medium",
            },
            {
                "title": "Git hooks",
                "description": "Set up pre-commit, pre-push, and other client-side hooks.",
                "difficulty": "hard",
            },
            {
                "title": "Git stash and cherry-pick",
                "description": "Use stash for WIP changes and cherry-pick for selective commits.",
                "difficulty": "medium",
            },
            {
                "title": "Gitflow workflow",
                "description": "Learn the Gitflow branching model for release management.",
                "difficulty": "hard",
            },
            {
                "title": "Lab: Open source contribution",
                "description": "Fork a project, create a branch, and submit a real PR.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 06: Networking
    # -------------------------------------------------------------------------
    {
        "name": "Module 06 · Networking",
        "description": "TCP/IP, DNS, HTTP, and network troubleshooting fundamentals.",
        "tasks": [
            {
                "title": "OSI and TCP/IP models",
                "description": "Understand the 7-layer OSI model and practical TCP/IP stack.",
                "difficulty": "medium",
            },
            {
                "title": "IP addressing and subnetting",
                "description": "Learn IPv4/IPv6, CIDR notation, and subnet calculation.",
                "difficulty": "hard",
            },
            {
                "title": "DNS fundamentals",
                "description": "Understand A, AAAA, CNAME, MX records and DNS resolution.",
                "difficulty": "medium",
            },
            {
                "title": "HTTP/HTTPS deep dive",
                "description": "Learn request/response cycle, methods, headers, and status codes.",
                "difficulty": "medium",
            },
            {
                "title": "TLS/SSL certificates",
                "description": "Understand certificate chains, Let's Encrypt, and HTTPS setup.",
                "difficulty": "hard",
            },
            {
                "title": "Network troubleshooting tools",
                "description": "Master ping, traceroute, netstat, ss, and tcpdump.",
                "difficulty": "medium",
            },
            {
                "title": "Load balancing concepts",
                "description": "Learn L4 vs L7 load balancing, algorithms, and health checks.",
                "difficulty": "hard",
            },
            {
                "title": "Firewalls and iptables",
                "description": "Configure Linux firewall rules with iptables and ufw.",
                "difficulty": "hard",
            },
            {
                "title": "VPNs and tunneling",
                "description": "Understand VPN types, WireGuard, and SSH tunneling.",
                "difficulty": "hard",
            },
            {
                "title": "Lab: Set up nginx reverse proxy",
                "description": "Configure nginx as a reverse proxy with SSL termination.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 07: Cloud & AWS
    # -------------------------------------------------------------------------
    {
        "name": "Module 07 · Cloud & AWS",
        "description": "AWS fundamentals and cloud computing essentials.",
        "tasks": [
            {
                "title": "Cloud computing models",
                "description": "Understand IaaS, PaaS, SaaS, and shared responsibility.",
                "difficulty": "easy",
            },
            {
                "title": "AWS account setup",
                "description": "Create an AWS account, set up IAM, and enable MFA.",
                "difficulty": "easy",
            },
            {
                "title": "EC2 fundamentals",
                "description": "Launch instances, choose AMIs, and manage key pairs.",
                "difficulty": "medium",
            },
            {
                "title": "S3 storage basics",
                "description": "Create buckets, upload objects, and configure permissions.",
                "difficulty": "medium",
            },
            {
                "title": "VPC networking",
                "description": "Design VPCs with subnets, route tables, and security groups.",
                "difficulty": "hard",
            },
            {
                "title": "IAM deep dive",
                "description": "Create users, roles, policies, and understand least privilege.",
                "difficulty": "hard",
            },
            {
                "title": "RDS and managed databases",
                "description": "Deploy PostgreSQL on RDS with backups and multi-AZ.",
                "difficulty": "medium",
            },
            {
                "title": "AWS CLI essentials",
                "description": "Configure AWS CLI and manage resources from command line.",
                "difficulty": "medium",
            },
            {
                "title": "CloudWatch monitoring",
                "description": "Set up metrics, alarms, and log groups for observability.",
                "difficulty": "medium",
            },
            {
                "title": "Cost management",
                "description": "Use Cost Explorer, set budgets, and optimize spending.",
                "difficulty": "medium",
            },
            {
                "title": "Lab: Deploy a 3-tier app",
                "description": "Build VPC, EC2, RDS stack for a web application.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 08: Infrastructure as Code
    # -------------------------------------------------------------------------
    {
        "name": "Module 08 · Infrastructure as Code",
        "description": "Terraform, CloudFormation, and IaC best practices.",
        "tasks": [
            {
                "title": "IaC principles and benefits",
                "description": "Learn idempotency, declarative syntax, and version control for infra.",
                "difficulty": "easy",
            },
            {
                "title": "Terraform basics",
                "description": "Install Terraform, write your first configuration, apply changes.",
                "difficulty": "medium",
            },
            {
                "title": "Terraform state management",
                "description": "Understand local vs remote state, S3 backend, and state locking.",
                "difficulty": "hard",
            },
            {
                "title": "Terraform modules",
                "description": "Create reusable modules and use the Terraform Registry.",
                "difficulty": "hard",
            },
            {
                "title": "Terraform workspaces",
                "description": "Manage multiple environments with workspaces.",
                "difficulty": "medium",
            },
            {
                "title": "Variables and outputs",
                "description": "Use input variables, locals, and output values effectively.",
                "difficulty": "medium",
            },
            {
                "title": "Terraform import and data sources",
                "description": "Import existing resources and use data sources.",
                "difficulty": "hard",
            },
            {
                "title": "AWS CloudFormation basics",
                "description": "Write YAML templates and deploy stacks.",
                "difficulty": "medium",
            },
            {
                "title": "Ansible fundamentals",
                "description": "Install Ansible, write playbooks, and manage inventory.",
                "difficulty": "medium",
            },
            {
                "title": "Lab: Full Terraform project",
                "description": "Build a complete AWS infrastructure with modules and remote state.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 09: Containers
    # -------------------------------------------------------------------------
    {
        "name": "Module 09 · Containers",
        "description": "Docker containerization from basics to production patterns.",
        "tasks": [
            {
                "title": "Container fundamentals",
                "description": "Understand containers vs VMs, namespaces, and cgroups.",
                "difficulty": "easy",
            },
            {
                "title": "Docker installation and basics",
                "description": "Install Docker, run your first container, explore commands.",
                "difficulty": "easy",
            },
            {
                "title": "Docker images and Dockerfile",
                "description": "Build custom images with Dockerfile best practices.",
                "difficulty": "medium",
            },
            {
                "title": "Multi-stage builds",
                "description": "Optimize image size with multi-stage Dockerfile patterns.",
                "difficulty": "hard",
            },
            {
                "title": "Docker volumes and networking",
                "description": "Persist data with volumes and configure container networks.",
                "difficulty": "medium",
            },
            {
                "title": "Docker Compose",
                "description": "Define multi-container apps with docker-compose.yml.",
                "difficulty": "medium",
            },
            {
                "title": "Container registries",
                "description": "Push images to Docker Hub, ECR, and private registries.",
                "difficulty": "medium",
            },
            {
                "title": "Container security",
                "description": "Scan for vulnerabilities, use non-root users, secrets management.",
                "difficulty": "hard",
            },
            {
                "title": "Docker health checks",
                "description": "Implement HEALTHCHECK instruction for container monitoring.",
                "difficulty": "medium",
            },
            {
                "title": "Lab: Containerize a full-stack app",
                "description": "Create Dockerfiles for frontend, backend, and database.",
                "difficulty": "hard",
            },
        ],
    },
    # -------------------------------------------------------------------------
    # Module 10: Kubernetes
    # -------------------------------------------------------------------------
    {
        "name": "Module 10 · Kubernetes",
        "description": "Container orchestration with Kubernetes for production workloads.",
        "tasks": [
            {
                "title": "Kubernetes architecture",
                "description": "Understand control plane, nodes, and core components.",
                "difficulty": "medium",
            },
            {
                "title": "Setting up a local cluster",
                "description": "Install minikube or kind for local Kubernetes development.",
                "difficulty": "easy",
            },
            {
                "title": "Pods and ReplicaSets",
                "description": "Create pods, understand lifecycle, and use ReplicaSets.",
                "difficulty": "medium",
            },
            {
                "title": "Deployments and rollouts",
                "description": "Deploy apps, perform rolling updates, and rollbacks.",
                "difficulty": "medium",
            },
            {
                "title": "Services and networking",
                "description": "Expose apps with ClusterIP, NodePort, and LoadBalancer.",
                "difficulty": "medium",
            },
            {
                "title": "ConfigMaps and Secrets",
                "description": "Manage configuration and sensitive data securely.",
                "difficulty": "medium",
            },
            {
                "title": "Persistent Volumes",
                "description": "Configure storage with PV, PVC, and StorageClasses.",
                "difficulty": "hard",
            },
            {
                "title": "Ingress controllers",
                "description": "Route external traffic with nginx-ingress and cert-manager.",
                "difficulty": "hard",
            },
            {
                "title": "Helm package manager",
                "description": "Use Helm charts to deploy and manage applications.",
                "difficulty": "hard",
            },
            {
                "title": "Resource limits and autoscaling",
                "description": "Set requests/limits and configure HPA for auto-scaling.",
                "difficulty": "hard",
            },
            {
                "title": "RBAC and security",
                "description": "Configure ServiceAccounts, Roles, and NetworkPolicies.",
                "difficulty": "hard",
            },
            {
                "title": "Lab: Deploy microservices",
                "description": "Deploy a complete microservices app with Helm and Ingress.",
                "difficulty": "hard",
            },
        ],
    },
]


def get_bootcamp_seed_data() -> list[dict]:
    """
    Returns the complete bootcamp seed data.
    Each module dict contains:
      - name: str
      - description: str
      - tasks: list[dict] with title, description, difficulty
    """
    return BOOTCAMP_MODULES


def get_module_count() -> int:
    """Returns the total number of modules in the bootcamp."""
    return len(BOOTCAMP_MODULES)


def get_task_count() -> int:
    """Returns the total number of tasks across all modules."""
    return sum(len(module["tasks"]) for module in BOOTCAMP_MODULES)
