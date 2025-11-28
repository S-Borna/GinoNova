# DevOpsHub Bootcamp v3.0

> **Enterprise-Grade DevOps Education Platform**
> From Zero to Production-Ready DevOps Engineer

---

## Vision

Denna bootcamp ska producera **anställningsbara DevOps Engineers** med praktisk erfarenhet motsvarande 2-3 års arbetslivserfarenhet. Varje modul innehåller:

- **Teori** — Koncept och arkitektur
- **Hands-on Labs** — Praktiska övningar
- **Projekt** — Verkliga implementationer
- **Assessment** — Kunskapskontroll
- **Portfolio Artifacts** — Bevisbara leverabler

---

## Bootcamp Structure

```
TOTAL: 15 Moduler | ~200 timmar | 12-16 veckor

TRACK 1: FOUNDATION (Vecka 1-4)
├── Module 01: Environment & Tooling Setup
├── Module 02: Linux Mastery
├── Module 03: Shell Scripting & Automation
├── Module 04: Git & Collaborative Workflows
└── Module 05: Python for DevOps

TRACK 2: CLOUD & INFRASTRUCTURE (Vecka 5-8)
├── Module 06: AWS Core Services
├── Module 07: Infrastructure as Code (Terraform)
├── Module 08: Serverless Architecture
└── Module 09: Networking & Security

TRACK 3: CONTAINERS & ORCHESTRATION (Vecka 9-11)
├── Module 10: Docker Fundamentals
├── Module 11: Docker Advanced & Production
└── Module 12: Kubernetes Core

TRACK 4: PLATFORM ENGINEERING (Vecka 12-15)
├── Module 13: Kubernetes Advanced & GitOps
├── Module 14: Observability & Monitoring
└── Module 15: SRE, DevSecOps & Capstone
```

---

# TRACK 1: FOUNDATION

## Module 01: Environment & Tooling Setup

**Duration:** 8-10 hours | **Difficulty:** ⭐ Beginner

### Overview
Etablera en professionell utvecklingsmiljö identisk med enterprise-standarder. Du bygger grunden som resten av bootcampen vilar på.

### Learning Objectives
- Konfigurera macOS/Linux utvecklingsmiljö med säkerhetsbaselines
- Installera och konfigurera essentiella DevOps-verktyg
- Förstå terminal, shell och CLI fundamentals
- Etablera Git credentials och SSH-nycklar
- Skapa reproducerbar miljö med dotfiles

### Topics

#### 1.1 Operating System Setup
- macOS vs Linux för DevOps-arbete
- Terminal emulators (iTerm2, Alacritty)
- Shell selection (zsh, bash) och konfiguration
- Package managers (Homebrew, apt, yum)

#### 1.2 Essential Tools Installation
- VS Code med DevOps-extensions
- Docker Desktop
- Git och GitHub CLI
- AWS CLI v2
- Terraform
- kubectl
- Python 3.11+

#### 1.3 Security Baseline
- SSH key generation och management
- GPG signing för commits
- Password managers integration
- MFA setup för alla tjänster

#### 1.4 Dotfiles & Reproducibility
- Skapa personligt dotfiles-repo
- Shell aliases och functions
- Environment variables management
- Backup och restore strategi

### Hands-on Labs
1. **Lab 1.1:** Terminal Power User Setup (2h)
2. **Lab 1.2:** Complete Tool Chain Installation (3h)
3. **Lab 1.3:** SSH & Security Configuration (2h)
4. **Lab 1.4:** Dotfiles Repository Creation (2h)

### Project: Development Environment as Code
Skapa ett automatiserat setup-script som installerar hela din utvecklingsmiljö på en ny maskin inom 30 minuter.

**Deliverables:**
- [ ] Dotfiles repository på GitHub
- [ ] Automated setup script (bootstrap.sh)
- [ ] Tool verification checklist
- [ ] Environment documentation

### Assessment
- Quiz: 20 frågor om tools och configuration
- Practical: Demonstrera environment recreation

---

## Module 02: Linux Mastery

**Duration:** 15-20 hours | **Difficulty:** ⭐⭐ Intermediate

### Overview
Djup förståelse för Linux som är grunden för all DevOps-infrastruktur. Du lär dig inte bara kommandon — du förstår *varför* saker fungerar.

### Learning Objectives
- Navigera filsystem och förstå Linux hierarchy
- Hantera processer, tjänster och systemd
- Konfigurera användare, grupper och permissions
- Felsöka system med logs och diagnostik
- Förstå nätverk från Linux-perspektiv

### Topics

#### 2.1 Filesystem Deep Dive
- FHS (Filesystem Hierarchy Standard)
- Mount points och device files
- Inodes, hard links, symbolic links
- Disk management (fdisk, lvm, df, du)
- File permissions (chmod, chown, umask, ACLs)

#### 2.2 Process Management
- Process lifecycle och states
- Foreground vs background processes
- Job control (jobs, fg, bg, nohup)
- Signals (SIGTERM, SIGKILL, SIGHUP)
- Process monitoring (ps, top, htop, pgrep)

#### 2.3 System Services
- Systemd architecture
- Unit files (service, timer, socket)
- Service management (systemctl)
- Boot process och targets
- Journald och logging

#### 2.4 Users & Security
- User/group management
- sudo configuration
- PAM modules
- SSH hardening
- Firewall basics (ufw, iptables)

#### 2.5 Text Processing & Pipelines
- grep, sed, awk mastery
- cut, sort, uniq, tr
- xargs och command substitution
- Regular expressions
- Stream editing

#### 2.6 Networking from Linux
- Network interfaces (ip, ifconfig)
- DNS resolution (dig, nslookup)
- Socket inspection (ss, netstat)
- Traffic analysis (tcpdump basics)
- curl och wget

### Hands-on Labs
1. **Lab 2.1:** Filesystem Exploration Challenge (3h)
2. **Lab 2.2:** Process Detective (2h)
3. **Lab 2.3:** Systemd Service Creation (3h)
4. **Lab 2.4:** User Security Hardening (2h)
5. **Lab 2.5:** Text Processing Olympics (4h)
6. **Lab 2.6:** Network Troubleshooting (3h)

### Project: Linux System Administration
Konfigurera en Linux-server från scratch med:
- Hardened SSH access
- Custom systemd services
- Log rotation
- Automated backups
- Monitoring scripts

**Deliverables:**
- [ ] Server configuration documentation
- [ ] Security hardening checklist
- [ ] Custom systemd unit files
- [ ] System monitoring script

### Assessment
- Quiz: 40 frågor (commands, concepts, troubleshooting)
- Practical: Live troubleshooting scenario

---

## Module 03: Shell Scripting & Automation

**Duration:** 15-20 hours | **Difficulty:** ⭐⭐ Intermediate

### Overview
Transformera manuella processer till automatiserade, pålitliga scripts. Du bygger verktyg som sparar timmar av arbete.

### Learning Objectives
- Skriva robusta bash scripts med felhantering
- Implementera logging och debugging
- Automatisera repetitiva DevOps-uppgifter
- Skapa återanvändbara funktionsbibliotek
- Integrera scripts med externa API:er

### Topics

#### 3.1 Bash Fundamentals
- Shebang och script execution
- Variables (local, global, environment)
- Quoting rules (single, double, backticks)
- Exit codes och error handling
- set options (-e, -u, -x, -o pipefail)

#### 3.2 Control Structures
- Conditionals (if, case, [[]])
- Loops (for, while, until)
- Functions och return values
- Traps och signal handling
- Subshells och command grouping

#### 3.3 Advanced Techniques
- Here documents och here strings
- Process substitution
- Arrays (indexed, associative)
- String manipulation
- Arithmetic operations

#### 3.4 Practical Automation
- Log monitoring och alerting
- Backup automation
- System health checks
- User provisioning
- Deployment scripts

#### 3.5 Script Quality
- ShellCheck för linting
- Unit testing med BATS
- Documentation standards
- Code organization
- Security considerations

### Hands-on Labs
1. **Lab 3.1:** Bash Fundamentals Exercises (3h)
2. **Lab 3.2:** Control Flow Challenges (3h)
3. **Lab 3.3:** Log Monitor with Email Alerts (4h)
4. **Lab 3.4:** Automated Backup System (3h)
5. **Lab 3.5:** System Health Dashboard (4h)

### Project: DevOps Automation Toolkit
Skapa ett komplett toolkit med:
- Server provisioning script
- Automated backup med rotation
- Log analyzer med alerting
- Deployment script med rollback

**Deliverables:**
- [ ] 5+ production-ready scripts
- [ ] Function library
- [ ] Documentation för varje script
- [ ] Test suite med BATS

### Assessment
- Quiz: 30 frågor om bash syntax och best practices
- Practical: Live scripting challenge (45 min)

---

## Module 04: Git & Collaborative Workflows

**Duration:** 12-15 hours | **Difficulty:** ⭐⭐ Intermediate

### Overview
Bemästra versionskontroll och samarbetsflöden som används av professionella team. Git är fundamentet för all modern mjukvaruutveckling och DevOps.

### Learning Objectives
- Förstå Git internals (objects, refs, index)
- Hantera branches och merging strategier
- Lösa konflikter och återställa ändringar
- Implementera GitFlow och trunk-based development
- Använda GitHub för code review och CI/CD

### Topics

#### 4.1 Git Internals
- Object model (blobs, trees, commits)
- References och HEAD
- Index (staging area)
- Packfiles och garbage collection

#### 4.2 Branching Strategies
- Feature branches
- GitFlow workflow
- Trunk-based development
- Release branches
- Hotfix management

#### 4.3 Advanced Git Operations
- Interactive rebase
- Cherry-picking
- Bisect för debugging
- Reflog och recovery
- Submodules och subtrees

#### 4.4 Collaboration
- Pull requests och code review
- Branch protection rules
- Merge strategies (merge, squash, rebase)
- Conflict resolution
- Git hooks

#### 4.5 GitHub Features
- Issues och Projects
- Actions basics (intro)
- Releases och tags
- GitHub CLI
- Security features

### Hands-on Labs
1. **Lab 4.1:** Git Internals Exploration (2h)
2. **Lab 4.2:** Branching Strategy Simulation (3h)
3. **Lab 4.3:** Conflict Resolution Scenarios (2h)
4. **Lab 4.4:** Rebase och History Rewriting (3h)
5. **Lab 4.5:** Pull Request Workflow (3h)

### Project: Team Collaboration Simulation
Simulera ett team-projekt med:
- Multiple branches
- Pull requests med review
- Conflict resolution
- Release management
- Protected main branch

**Deliverables:**
- [ ] Git workflow documentation
- [ ] Contribution guidelines (CONTRIBUTING.md)
- [ ] Branch protection configuration
- [ ] Release process documentation

### Assessment
- Quiz: 25 frågor om Git concepts och commands
- Practical: Solve complex merge scenario

---

## Module 05: Python for DevOps

**Duration:** 20-25 hours | **Difficulty:** ⭐⭐ Intermediate

### Overview
Python är det dominerande språket för DevOps-automation. Du lär dig att bygga verktyg som interagerar med cloud-APIs, automatiserar infrastruktur och processerar data.

### Learning Objectives
- Skriva clean, maintainable Python kod
- Använda boto3 för AWS automation
- Bygga CLI-verktyg med argparse/click
- Interagera med REST APIs
- Hantera konfiguration och secrets

### Topics

#### 5.1 Python Fundamentals (Refresher)
- Data types och structures
- Functions och decorators
- Classes och OOP basics
- Exception handling
- Virtual environments

#### 5.2 DevOps-Specific Libraries
- boto3 (AWS SDK)
- requests (HTTP client)
- paramiko (SSH)
- jinja2 (templating)
- pyyaml och json

#### 5.3 Automation Patterns
- Configuration management
- Secret handling
- Logging och monitoring
- Error handling strategies
- Retry logic

#### 5.4 CLI Tool Development
- argparse fundamentals
- Click framework
- Rich för beautiful output
- Configuration files
- Packaging och distribution

#### 5.5 API Integration
- REST API consumption
- Authentication (API keys, OAuth)
- Rate limiting handling
- Response parsing
- Error handling

#### 5.6 Testing & Quality
- pytest fundamentals
- Mocking external services
- Code coverage
- Type hints och mypy
- Black och flake8

### Hands-on Labs
1. **Lab 5.1:** Python Fundamentals Review (3h)
2. **Lab 5.2:** AWS Resource Manager med boto3 (4h)
3. **Lab 5.3:** CLI Tool med Click (3h)
4. **Lab 5.4:** REST API Client (3h)
5. **Lab 5.5:** Configuration Manager (3h)
6. **Lab 5.6:** Testing Your Tools (3h)

### Project: AWS Automation Suite
Bygg en komplett automation-svit:
- EC2 instance manager (start, stop, list)
- S3 backup tool
- IAM user provisioning
- Cost reporter
- Resource tagger

**Deliverables:**
- [ ] Python package med 5+ tools
- [ ] CLI interface
- [ ] Unit tests (80%+ coverage)
- [ ] Documentation
- [ ] PyPI-ready setup

### Assessment
- Quiz: 35 frågor om Python och DevOps patterns
- Practical: Build a tool from spec (2h)

---

# TRACK 2: CLOUD & INFRASTRUCTURE

## Module 06: AWS Core Services

**Duration:** 20-25 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Behärska AWS fundamentala tjänster som utgör grunden för all cloud-infrastruktur. Du bygger verklig produktionsarkitektur.

### Learning Objectives
- Designa VPC-arkitekturer med security best practices
- Deploya och hantera EC2-instanser
- Implementera load balancing och auto-scaling
- Konfigurera IAM med least privilege
- Använda S3 för storage och hosting

### Topics

#### 6.1 AWS Fundamentals
- Global infrastructure (regions, AZs)
- Account setup och Organizations
- Cost management och budgets
- Support plans
- Well-Architected Framework intro

#### 6.2 IAM Deep Dive
- Users, groups, roles
- Policies (managed, inline, custom)
- Policy evaluation logic
- Cross-account access
- Service-linked roles
- Best practices

#### 6.3 VPC Architecture
- CIDR planning
- Subnets (public, private)
- Internet Gateway
- NAT Gateway/Instance
- Route tables
- Security Groups vs NACLs
- VPC Peering
- VPC Endpoints

#### 6.4 EC2 Mastery
- Instance types och selection
- AMIs (Amazon Machine Images)
- Key pairs och SSH
- User data scripts
- Instance metadata
- EBS volumes
- Instance store
- Placement groups

#### 6.5 Load Balancing & Auto Scaling
- ALB, NLB, CLB differences
- Target groups
- Health checks
- SSL/TLS termination
- Launch templates
- Auto Scaling groups
- Scaling policies
- Predictive scaling

#### 6.6 S3 & Storage
- Bucket configuration
- Storage classes
- Lifecycle policies
- Versioning
- Encryption
- Access control (ACLs, policies)
- Static website hosting
- Cross-region replication

### Hands-on Labs
1. **Lab 6.1:** Multi-AZ VPC from Scratch (4h)
2. **Lab 6.2:** IAM Policy Workshop (3h)
3. **Lab 6.3:** EC2 Fleet Deployment (3h)
4. **Lab 6.4:** Load Balanced Application (4h)
5. **Lab 6.5:** Auto Scaling Configuration (3h)
6. **Lab 6.6:** S3 Static Website (2h)

### Project: Three-Tier Web Architecture
Bygg en komplett three-tier applikation:
- VPC med public/private subnets
- ALB + Auto Scaling web tier
- Application tier i private subnet
- RDS database tier
- Bastion host för access

**Deliverables:**
- [ ] Architecture diagram
- [ ] VPC configuration documentation
- [ ] Security group rules matrix
- [ ] Cost estimation
- [ ] Disaster recovery plan

### Assessment
- Quiz: 50 frågor (AWS Solutions Architect style)
- Practical: Design and deploy architecture from requirements

---

## Module 07: Infrastructure as Code (Terraform)

**Duration:** 20-25 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Infrastruktur som kod med Terraform — industristandarden för cloud provisioning. Du lär dig att hantera komplex infrastruktur reproducerbart och säkert.

### Learning Objectives
- Skriva modulär, återanvändbar Terraform-kod
- Hantera state säkert med remote backends
- Implementera multi-environment deployments
- Integrera Terraform med CI/CD
- Följa HashiCorp best practices

### Topics

#### 7.1 Terraform Fundamentals
- Declarative vs imperative IaC
- Provider architecture
- Resources och data sources
- Variables och outputs
- terraform init, plan, apply, destroy

#### 7.2 HCL Deep Dive
- Expressions och functions
- Conditionals och loops (count, for_each)
- Dynamic blocks
- Local values
- Type constraints

#### 7.3 State Management
- Local vs remote state
- S3 + DynamoDB backend
- State locking
- terraform state commands
- Importing existing resources
- State manipulation safety

#### 7.4 Modules
- Module structure
- Input variables
- Output values
- Module sources (local, registry, git)
- Module versioning
- Creating reusable modules

#### 7.5 Workspaces & Environments
- Workspace concept
- Environment separation strategies
- Variable files per environment
- Terraform Cloud workspaces

#### 7.6 Advanced Patterns
- Data sources
- Provisioners (when to avoid)
- null_resource
- terraform_remote_state
- Sensitive data handling
- Dependency management

#### 7.7 Testing & CI/CD
- terraform validate
- terraform fmt
- tflint och tfsec
- Terratest basics
- GitHub Actions integration
- Atlantis for PR automation

### Hands-on Labs
1. **Lab 7.1:** First Terraform Project (3h)
2. **Lab 7.2:** Variables och Outputs (2h)
3. **Lab 7.3:** Remote State Setup (2h)
4. **Lab 7.4:** Creating Modules (4h)
5. **Lab 7.5:** Multi-Environment Setup (4h)
6. **Lab 7.6:** CI/CD Pipeline for Terraform (4h)

### Project: Complete AWS Infrastructure
Bygg Module 06 arkitekturen med Terraform:
- Reusable VPC module
- EC2 module med ASG
- ALB module
- RDS module
- Multi-environment (dev, staging, prod)
- Remote state med locking
- GitHub Actions deployment

**Deliverables:**
- [ ] Terraform module library
- [ ] Environment configurations
- [ ] CI/CD pipeline
- [ ] Documentation (README per module)
- [ ] Cost tagging strategy

### Assessment
- Quiz: 40 frågor om Terraform concepts
- Practical: Convert existing infra to Terraform

---

## Module 08: Serverless Architecture

**Duration:** 15-20 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Bygg event-driven, serverless applikationer med AWS Lambda. Du lär dig att designa kostnadseffektiva, skalbara lösningar utan serverhantering.

### Learning Objectives
- Designa event-driven arkitekturer
- Utveckla och deploya Lambda functions
- Integrera med AWS event sources
- Hantera state med Step Functions
- Optimera för kostnad och performance

### Topics

#### 8.1 Serverless Fundamentals
- Serverless vs traditional
- AWS Lambda architecture
- Execution model
- Cold starts
- Pricing model
- Use cases

#### 8.2 Lambda Development
- Function handlers
- Event objects
- Context object
- Environment variables
- Layers
- Packaging och dependencies
- Local development (SAM, LocalStack)

#### 8.3 Event Sources
- API Gateway integration
- S3 triggers
- SQS triggers
- SNS triggers
- EventBridge rules
- CloudWatch Events
- DynamoDB Streams

#### 8.4 Advanced Patterns
- Step Functions orchestration
- Fan-out/fan-in
- Dead letter queues
- Retry strategies
- Idempotency
- Circuit breaker

#### 8.5 Security & Networking
- IAM execution roles
- VPC configuration
- Secrets Manager integration
- KMS encryption
- Resource policies

#### 8.6 Operations
- CloudWatch Logs
- X-Ray tracing
- Metrics och alarms
- Performance tuning
- Cost optimization

### Hands-on Labs
1. **Lab 8.1:** First Lambda Function (2h)
2. **Lab 8.2:** API Gateway + Lambda (3h)
3. **Lab 8.3:** S3 Event Processing (3h)
4. **Lab 8.4:** Step Functions Workflow (4h)
5. **Lab 8.5:** SQS Message Processing (3h)
6. **Lab 8.6:** Lambda with Terraform (3h)

### Project: Serverless Data Pipeline
Bygg en komplett data processing pipeline:
- S3 trigger för file upload
- Lambda för data transformation
- Step Functions för orchestration
- DynamoDB för state
- SNS för notifications
- All infrastructure med Terraform

**Deliverables:**
- [ ] Architecture diagram
- [ ] Lambda functions
- [ ] Step Functions definition
- [ ] Terraform code
- [ ] Monitoring dashboard
- [ ] Cost analysis

### Assessment
- Quiz: 30 frågor om serverless patterns
- Practical: Design serverless solution from requirements

---

## Module 09: Networking & Security

**Duration:** 15-20 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Fördjupa dig i nätverksarkitektur och security practices som är kritiska för enterprise-grade infrastruktur.

### Learning Objectives
- Designa säkra nätverksarkitekturer
- Implementera defense in depth
- Konfigurera DNS och CDN
- Hantera certificates och encryption
- Förstå compliance requirements

### Topics

#### 9.1 Advanced Networking
- Transit Gateway
- PrivateLink
- Direct Connect basics
- VPN connections
- Route 53 DNS
- CloudFront CDN

#### 9.2 Security Architecture
- Security groups deep dive
- Network ACLs
- WAF (Web Application Firewall)
- Shield (DDoS protection)
- Firewall Manager

#### 9.3 Identity & Access
- AWS SSO
- Federation (SAML, OIDC)
- Cognito basics
- Service Control Policies
- Permission boundaries

#### 9.4 Data Protection
- KMS (Key Management Service)
- Encryption at rest
- Encryption in transit
- Certificate Manager (ACM)
- Secrets Manager vs Parameter Store

#### 9.5 Compliance & Governance
- AWS Config
- CloudTrail
- Security Hub
- GuardDuty
- Inspector
- Compliance frameworks (SOC2, HIPAA, PCI)

#### 9.6 Incident Response
- CloudWatch Alarms
- EventBridge for security
- Automated remediation
- Forensics basics
- Incident playbooks

### Hands-on Labs
1. **Lab 9.1:** Advanced VPC Design (3h)
2. **Lab 9.2:** WAF Configuration (3h)
3. **Lab 9.3:** KMS och Encryption (3h)
4. **Lab 9.4:** CloudTrail och Config (3h)
5. **Lab 9.5:** Security Hub Setup (2h)
6. **Lab 9.6:** Automated Security Response (3h)

### Project: Secure Reference Architecture
Implementera en säker arkitektur:
- Multi-account strategy
- Transit Gateway connectivity
- Centralized logging
- Security Hub aggregation
- Automated compliance checks
- Incident response automation

**Deliverables:**
- [ ] Security architecture diagram
- [ ] Network topology diagram
- [ ] Security controls documentation
- [ ] Compliance checklist
- [ ] Incident response playbook

### Assessment
- Quiz: 40 frågor om security och networking
- Practical: Security review of architecture

---

# TRACK 3: CONTAINERS & ORCHESTRATION

## Module 10: Docker Fundamentals

**Duration:** 12-15 hours | **Difficulty:** ⭐⭐ Intermediate

### Overview
Behärska Docker — containerteknologin som revolutionerade hur vi bygger och deployar applikationer.

### Learning Objectives
- Förstå container-teknologi och isolation
- Bygga optimerade Docker images
- Hantera container lifecycle
- Implementera multi-container apps med Compose
- Följa security best practices

### Topics

#### 10.1 Container Fundamentals
- Containers vs VMs
- Docker architecture
- Images och layers
- Container lifecycle
- Docker CLI basics

#### 10.2 Dockerfile Mastery
- Instruction reference
- Build context
- Layer caching
- Multi-stage builds
- Build arguments
- Best practices

#### 10.3 Image Management
- Tagging strategies
- Registry basics (Docker Hub, ECR)
- Image scanning
- Base image selection
- Size optimization

#### 10.4 Container Operations
- Running containers
- Resource limits
- Environment variables
- Volume management
- Network basics
- Logging

#### 10.5 Docker Compose
- Compose file syntax
- Service definition
- Networks och volumes
- Environment management
- Development workflows

#### 10.6 Security
- Non-root containers
- Read-only filesystems
- Secrets handling
- Image vulnerabilities
- Runtime security

### Hands-on Labs
1. **Lab 10.1:** Docker CLI Fundamentals (2h)
2. **Lab 10.2:** Dockerfile Best Practices (3h)
3. **Lab 10.3:** Multi-Stage Builds (2h)
4. **Lab 10.4:** Docker Compose Application (3h)
5. **Lab 10.5:** Container Security Hardening (2h)

### Project: Containerized Full-Stack App
Containerisera en komplett applikation:
- Frontend (React/Next.js)
- Backend API (Python/Node)
- Database (PostgreSQL)
- Redis cache
- Nginx reverse proxy

**Deliverables:**
- [ ] Optimized Dockerfiles
- [ ] docker-compose.yml (dev + prod)
- [ ] Documentation
- [ ] Size comparison report
- [ ] Security scan results

### Assessment
- Quiz: 30 frågor om Docker concepts
- Practical: Optimize existing Dockerfile

---

## Module 11: Docker Advanced & Production

**Duration:** 12-15 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Ta Docker till produktion med avancerade patterns, monitoring och enterprise-grade practices.

### Learning Objectives
- Implementera production-ready container builds
- Konfigurera container monitoring
- Hantera secrets och configuration
- Integrera med CI/CD pipelines
- Förstå container runtime alternativ

### Topics

#### 11.1 Advanced Builds
- BuildKit features
- Cache mounts
- Secret mounts
- Build attestations
- SBOM generation
- Reproducible builds

#### 11.2 Registry Operations
- ECR setup och policies
- Image lifecycle management
- Cross-region replication
- Vulnerability scanning
- Image signing (cosign)

#### 11.3 Production Patterns
- Health checks
- Graceful shutdown
- Signal handling
- Init systems (tini, dumb-init)
- Sidecar containers

#### 11.4 Monitoring
- Container metrics
- Log aggregation
- cAdvisor
- Prometheus metrics
- Distributed tracing prep

#### 11.5 CI/CD Integration
- Build pipelines
- Image versioning
- Automated testing
- Deployment strategies
- GitOps preparation

#### 11.6 ECS Deep Dive
- Task definitions
- Services
- Auto scaling
- Load balancing
- Fargate vs EC2

### Hands-on Labs
1. **Lab 11.1:** BuildKit Advanced Features (2h)
2. **Lab 11.2:** ECR Lifecycle Management (2h)
3. **Lab 11.3:** Container Monitoring Setup (3h)
4. **Lab 11.4:** CI/CD Pipeline for Containers (4h)
5. **Lab 11.5:** ECS Deployment (4h)

### Project: Production Container Platform
Bygg en komplett container platform:
- Multi-stage builds med SBOM
- ECR med scanning och signing
- GitHub Actions pipeline
- ECS deployment
- Monitoring med Prometheus
- Log aggregation

**Deliverables:**
- [ ] Production Dockerfiles
- [ ] CI/CD pipeline
- [ ] ECS infrastructure (Terraform)
- [ ] Monitoring dashboards
- [ ] Runbook documentation

### Assessment
- Quiz: 30 frågor om production containers
- Practical: Deploy application to ECS

---

## Module 12: Kubernetes Core

**Duration:** 20-25 hours | **Difficulty:** ⭐⭐⭐ Advanced

### Overview
Kubernetes — container orchestration-standarden. Du lär dig att deploya, skala och hantera containeriserade applikationer i produktion.

### Learning Objectives
- Förstå Kubernetes arkitektur och komponenter
- Deploya applikationer med olika workload types
- Konfigurera networking och service discovery
- Hantera storage och configuration
- Implementera basic security

### Topics

#### 12.1 Architecture
- Control plane components
- Worker node components
- etcd och cluster state
- API server
- kubectl basics

#### 12.2 Workloads
- Pods
- ReplicaSets
- Deployments
- StatefulSets
- DaemonSets
- Jobs och CronJobs

#### 12.3 Networking
- Service types (ClusterIP, NodePort, LoadBalancer)
- Ingress controllers
- DNS (CoreDNS)
- Network policies basics
- CNI overview

#### 12.4 Storage
- Volumes
- PersistentVolumes
- PersistentVolumeClaims
- Storage classes
- Dynamic provisioning

#### 12.5 Configuration
- ConfigMaps
- Secrets
- Environment variables
- Resource limits
- QoS classes

#### 12.6 Operations
- Rolling updates
- Rollbacks
- Health checks (liveness, readiness, startup)
- Horizontal Pod Autoscaler
- kubectl debugging

### Hands-on Labs
1. **Lab 12.1:** Cluster Setup (Minikube/kind) (2h)
2. **Lab 12.2:** Deploying Applications (3h)
3. **Lab 12.3:** Services och Ingress (3h)
4. **Lab 12.4:** Storage Configuration (3h)
5. **Lab 12.5:** ConfigMaps och Secrets (2h)
6. **Lab 12.6:** Scaling och Updates (3h)

### Project: Microservices on Kubernetes
Deploya en microservices-applikation:
- Frontend service
- API services (2-3)
- Database (StatefulSet)
- Redis cache
- Ingress med TLS
- ConfigMaps och Secrets
- HPA configuration

**Deliverables:**
- [ ] Kubernetes manifests
- [ ] Deployment documentation
- [ ] Architecture diagram
- [ ] Troubleshooting guide
- [ ] Scaling strategy

### Assessment
- Quiz: 50 frågor (CKA-style)
- Practical: Deploy and troubleshoot application

---

# TRACK 4: PLATFORM ENGINEERING

## Module 13: Kubernetes Advanced & GitOps

**Duration:** 20-25 hours | **Difficulty:** ⭐⭐⭐⭐ Expert

### Overview
Avancerade Kubernetes-patterns och GitOps för enterprise-grade platform engineering.

### Learning Objectives
- Provisionera EKS kluster med Terraform
- Implementera GitOps med ArgoCD
- Hantera Helm charts och Kustomize
- Konfigurera advanced security
- Implementera multi-environment strategies

### Topics

#### 13.1 EKS Deep Dive
- EKS architecture
- Managed node groups
- Fargate profiles
- Add-ons (CoreDNS, kube-proxy, VPC CNI)
- IAM integration (IRSA)
- EKS Terraform modules

#### 13.2 Helm
- Chart structure
- Templates och values
- Hooks
- Chart dependencies
- Chart repositories
- Creating custom charts

#### 13.3 Kustomize
- Base och overlays
- Patches
- ConfigMap/Secret generators
- Variable substitution
- Integration med kubectl

#### 13.4 GitOps with ArgoCD
- ArgoCD architecture
- Application CRD
- Sync policies
- Health checks
- Rollbacks
- ApplicationSets
- Multi-cluster management

#### 13.5 Advanced Security
- Pod Security Standards
- OPA/Gatekeeper
- Admission controllers
- Network policies
- Service mesh intro (Istio/Linkerd)

#### 13.6 Multi-Environment
- Environment promotion
- Namespace strategies
- Resource quotas
- Limit ranges
- RBAC

### Hands-on Labs
1. **Lab 13.1:** EKS Cluster with Terraform (4h)
2. **Lab 13.2:** Helm Chart Development (3h)
3. **Lab 13.3:** Kustomize Overlays (2h)
4. **Lab 13.4:** ArgoCD Setup och GitOps (4h)
5. **Lab 13.5:** Advanced Security Policies (3h)
6. **Lab 13.6:** Multi-Environment GitOps (4h)

### Project: GitOps Platform
Bygg en komplett GitOps platform:
- EKS cluster (Terraform)
- ArgoCD installation
- App-of-apps pattern
- Helm charts för services
- Environment promotion (dev→staging→prod)
- Security policies
- Automated sync

**Deliverables:**
- [ ] EKS Terraform modules
- [ ] Helm chart library
- [ ] ArgoCD applications
- [ ] GitOps repository structure
- [ ] Promotion workflow documentation

### Assessment
- Quiz: 40 frågor om advanced Kubernetes
- Practical: Implement GitOps workflow

---

## Module 14: Observability & Monitoring

**Duration:** 15-20 hours | **Difficulty:** ⭐⭐⭐⭐ Expert

### Overview
Implementera full observability stack — metrics, logs och traces — för att driva tillförlitlig infrastruktur.

### Learning Objectives
- Designa observability strategy
- Implementera Prometheus och Grafana
- Konfigurera centralized logging
- Implementera distributed tracing
- Skapa actionable alerts

### Topics

#### 14.1 Observability Fundamentals
- Three pillars (metrics, logs, traces)
- SLIs, SLOs, SLAs
- Error budgets
- Observability vs monitoring

#### 14.2 Prometheus
- Architecture
- Data model (metrics, labels)
- PromQL
- Scrape configuration
- Service discovery
- Recording rules
- Alerting rules

#### 14.3 Grafana
- Dashboard design
- Variables och templating
- Alerting
- Provisioning
- Best practices

#### 14.4 Logging
- Logging architecture
- Loki setup
- Log aggregation patterns
- LogQL
- Structured logging
- Log-based alerts

#### 14.5 Tracing
- Distributed tracing concepts
- OpenTelemetry
- Trace propagation
- Tempo/Jaeger
- Trace analysis

#### 14.6 Alerting
- Alert design principles
- Severity levels
- Escalation policies
- Runbooks
- Alert fatigue prevention
- PagerDuty/OpsGenie integration

### Hands-on Labs
1. **Lab 14.1:** Prometheus Installation (3h)
2. **Lab 14.2:** Grafana Dashboards (3h)
3. **Lab 14.3:** Loki Log Aggregation (3h)
4. **Lab 14.4:** Application Metrics (3h)
5. **Lab 14.5:** Alerting Configuration (2h)
6. **Lab 14.6:** Full Stack Observability (4h)

### Project: Production Observability Stack
Implementera komplett observability:
- Prometheus + Alertmanager
- Grafana dashboards
- Loki for logs
- Application instrumentation
- Custom metrics
- SLO tracking
- Incident response integration

**Deliverables:**
- [ ] Observability architecture diagram
- [ ] Prometheus configuration
- [ ] Grafana dashboards (5+)
- [ ] Alert definitions
- [ ] Runbooks
- [ ] SLO documentation

### Assessment
- Quiz: 35 frågor om observability
- Practical: Debug production issue using observability stack

---

## Module 15: SRE, DevSecOps & Capstone

**Duration:** 25-30 hours | **Difficulty:** ⭐⭐⭐⭐ Expert

### Overview
Avslutande modul som kombinerar SRE practices, DevSecOps och ett capstone-projekt som demonstrerar all kunskap.

### Learning Objectives
- Implementera SRE practices
- Integrera security i CI/CD
- Hantera incidents professionellt
- Leverera ett komplett portfolio-projekt

### Topics

#### 15.1 SRE Fundamentals
- SRE vs DevOps
- Service Level Objectives
- Error budgets
- Toil reduction
- Capacity planning
- Reliability engineering

#### 15.2 Incident Management
- Incident response process
- On-call practices
- Communication during incidents
- Postmortems (blameless)
- Root cause analysis
- Action items

#### 15.3 DevSecOps
- Security shift-left
- SAST (Static Analysis)
- DAST (Dynamic Analysis)
- SCA (Software Composition Analysis)
- Container scanning
- Infrastructure scanning

#### 15.4 Security in CI/CD
- Secret scanning
- Dependency checks
- Image scanning
- Compliance as code
- Policy enforcement

#### 15.5 Advanced Automation
- ChatOps
- Self-healing infrastructure
- Automated remediation
- Chaos engineering intro

#### 15.6 Career Development
- Building your portfolio
- Interview preparation
- DevOps career paths
- Continuous learning

### Hands-on Labs
1. **Lab 15.1:** SLO Implementation (3h)
2. **Lab 15.2:** Incident Simulation (3h)
3. **Lab 15.3:** Security Scanning Pipeline (4h)
4. **Lab 15.4:** Compliance Automation (3h)
5. **Lab 15.5:** Chaos Engineering Basics (3h)

### Capstone Project: Complete DevOps Platform

Bygg en komplett, production-ready plattform som demonstrerar alla 15 modulers kunskap:

**Requirements:**
1. **Infrastructure (Terraform)**
   - EKS cluster
   - VPC med proper networking
   - RDS database
   - S3 för artifacts
   - IAM med least privilege

2. **Application**
   - Microservices (3+ services)
   - API Gateway
   - Message queue
   - Database
   - Cache layer

3. **CI/CD (GitHub Actions)**
   - Build pipeline
   - Test automation
   - Security scanning
   - Container builds
   - GitOps deployment

4. **GitOps (ArgoCD)**
   - Multi-environment
   - Automated sync
   - Promotion workflow

5. **Observability**
   - Metrics (Prometheus)
   - Logs (Loki)
   - Dashboards (Grafana)
   - Alerts

6. **Security**
   - Network policies
   - RBAC
   - Secrets management
   - Compliance checks

7. **Documentation**
   - Architecture diagrams
   - Runbooks
   - SLO definitions
   - Incident playbooks

**Deliverables:**
- [ ] Complete GitHub repository
- [ ] Working deployed application
- [ ] Infrastructure as Code
- [ ] CI/CD pipelines
- [ ] Observability stack
- [ ] Security documentation
- [ ] Architecture documentation
- [ ] Video walkthrough (optional)

### Assessment
- Code review av capstone
- Architecture presentation
- Live troubleshooting scenario
- Technical interview simulation

---

## Certification

Upon completion:

**DevOpsHub Certified DevOps Engineer**

- 15 modules completed
- 60+ hands-on labs
- 15+ portfolio projects
- Capstone project delivered
- All assessments passed

---

## Appendix

### Time Investment Summary

| Track | Modules | Hours |
|-------|---------|-------|
| Foundation | 5 | 70-80h |
| Cloud & Infrastructure | 4 | 70-90h |
| Containers & Orchestration | 3 | 45-55h |
| Platform Engineering | 3 | 60-75h |
| **Total** | **15** | **~200-300h** |

### Prerequisites

- Basic computer literacy
- English reading comprehension
- Willingness to learn
- 15-20 hours/week commitment

### Tools & Accounts Needed

- AWS account (free tier sufficient for most)
- GitHub account
- Docker Hub account
- Local machine (macOS/Linux/WSL2)
- IDE (VS Code recommended)

---

*DevOpsHub Bootcamp v3.0 — Building World-Class DevOps Engineers*
