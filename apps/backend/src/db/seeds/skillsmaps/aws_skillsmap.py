# -*- coding: utf-8 -*-
"""
AWS SkillsMap - 20 Consolidated Nodes (DevOps Focus)
Version: 1.0
Date: 2025-12-02

Pedagogical Style: Akhilesh (Intro -> Concept -> Commands -> Pro Tips -> Task)
Focus: AWS Core Services for DevOps Engineers
"""

from typing import Literal, List, Dict, Any

DifficultyLevel = Literal["beginner", "intermediate", "advanced", "expert"]


# =============================================================================
# AWS SKILLSMAP METADATA
# =============================================================================

AWS_SKILLSMAP_INFO = {
    "name": "AWS for DevOps",
    "slug": "aws-devops",
    "description": "Master AWS core services for cloud infrastructure and DevOps",
    "total_nodes": 20,
    "estimated_hours": 50,
    "difficulty_range": "beginner to advanced",
    "focus": "EC2, VPC, IAM, S3, Lambda, ECS, CloudFormation",
}


# =============================================================================
# NODE 1: AWS INTRODUCTION & ACCOUNT SETUP
# =============================================================================

NODE_01_AWS_INTRO = {
    "node_id": 1,
    "title": "AWS Introduction & Account Setup",
    "slug": "aws-intro",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 50,
    "topics_covered": [
        "cloud computing", "AWS regions", "availability zones",
        "account setup", "root user", "billing alerts", "free tier"
    ],
    "content": r'''# AWS Introduction & Account Setup

## Varfor AWS for DevOps?

> "AWS ar inte bara 'molnet' - det ar 200+ tjanster som later dig bygga allt fran en enkel webbsida till Netflix-skala infrastruktur. Som DevOps Engineer maste du kunna AWS."

AWS dominerar molnmarknaden med ~32% market share. Nastan varje DevOps-jobb kraver AWS-kunskap.

---

## Cloud Computing Basics

### Vad ar Cloud Computing?

```
TRADITIONELLT (On-Premise)          CLOUD (AWS)
┌─────────────────────┐            ┌─────────────────────┐
│  Kop servrar        │            │  Hyr kapacitet      │
│  Installera i DC    │     →      │  Starta pa sekunder │
│  Underhall hardvara │            │  Betala per anvand. │
│  Skala manuellt     │            │  Skala automatiskt  │
└─────────────────────┘            └─────────────────────┘
     Veckor/Manader                      Minuter
```

### AWS Service Categories

| Kategori | Exempel-tjanster | Anvandning |
|----------|------------------|------------|
| Compute | EC2, Lambda, ECS | Kora applikationer |
| Storage | S3, EBS, EFS | Lagra data |
| Database | RDS, DynamoDB | Databaser |
| Networking | VPC, Route53, CloudFront | Natverk & DNS |
| Security | IAM, KMS, Secrets Manager | Sakerhet |
| DevOps | CodePipeline, CloudFormation | Automation |

---

## AWS Global Infrastructure

### Regions & Availability Zones

```
                    AWS GLOBAL INFRASTRUCTURE
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   REGION: eu-north-1 (Stockholm)                           │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                                                     │  │
│   │   AZ: eu-north-1a    AZ: eu-north-1b    AZ: eu-north-1c │
│   │   ┌─────────┐        ┌─────────┐        ┌─────────┐ │  │
│   │   │ Datacenter│      │ Datacenter│      │ Datacenter│ │  │
│   │   │ Cluster  │       │ Cluster  │       │ Cluster  │ │  │
│   │   └─────────┘        └─────────┘        └─────────┘ │  │
│   │         ↑                 ↑                 ↑       │  │
│   │         └────── High-speed links ───────────┘       │  │
│   │                                                     │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Region:** Geografiskt omrade (t.ex. eu-north-1 = Stockholm)
**Availability Zone (AZ):** Isolerat datacenter inom en region
**Edge Location:** CDN-noder for CloudFront (200+ globalt)

### Valj Ratt Region

| Faktor | Overvagande |
|--------|-------------|
| **Latency** | Nara dina anvandare |
| **Compliance** | GDPR kraver EU-data |
| **Kostnad** | Priserna varierar per region |
| **Tjanster** | Inte alla tjanster finns overallt |

---

## AWS Account Setup

### Skapa AWS Account

1. Ga till https://aws.amazon.com
2. Klicka "Create an AWS Account"
3. Ange email, losen, account name
4. Valj "Personal" eller "Business"
5. Lagg till betalningsmetod (kreditkort)
6. Verifiera telefonnummer
7. Valj Support Plan (Basic = gratis)

### Sakra Root User DIREKT

```bash
# ROOT USER = Gud-mode - ALDRIG anvand for dagligt arbete!

# Steg 1: Aktivera MFA pa root
AWS Console → Security Credentials → MFA → Activate MFA
# Anvand app som Google Authenticator eller Authy

# Steg 2: Skapa admin IAM-anvandare
AWS Console → IAM → Users → Add User
# Ge AdministratorAccess policy
# Anvand DENNA for dagligt arbete
```

### Free Tier - Vad ar gratis?

| Tjanst | Free Tier Limit | Giltig |
|--------|-----------------|--------|
| EC2 | 750 tim t2.micro/manad | 12 manader |
| S3 | 5 GB storage | 12 manader |
| RDS | 750 tim db.t2.micro/manad | 12 manader |
| Lambda | 1M requests/manad | ALLTID gratis |
| DynamoDB | 25 GB storage | ALLTID gratis |

---

## AWS CLI Setup

### Installation

```bash
# macOS
brew install awscli

# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install awscli -y

# Eller via pip
pip install awscli

# Verifiera installation
aws --version
# aws-cli/2.15.0 Python/3.11.6 Darwin/23.0.0
```

### Konfigurera Credentials

```bash
# Skapa Access Key i IAM Console:
# IAM → Users → [din user] → Security credentials → Create access key

# Konfigurera CLI
aws configure
# AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Default region name: eu-north-1
# Default output format: json

# Verifiera
aws sts get-caller-identity
# {
#     "UserId": "AIDAEXAMPLE",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/admin"
# }
```

### Multiple Profiles

```bash
# ~/.aws/credentials
[default]
aws_access_key_id = AKIADEFAULT
aws_secret_access_key = secretdefault

[prod]
aws_access_key_id = AKIAPROD
aws_secret_access_key = secretprod

[dev]
aws_access_key_id = AKIADEV
aws_secret_access_key = secretdev

# Anvand specifik profil
aws s3 ls --profile prod
export AWS_PROFILE=dev
aws ec2 describe-instances
```

---

## Billing & Cost Management

### Satt upp Billing Alerts

```bash
# KRITISKT: Undvik overraskningar!

# Via Console:
# 1. Billing → Budgets → Create budget
# 2. Valj "Cost budget"
# 3. Satt manadlig budget (t.ex. $10)
# 4. Lagg till email-alert vid 80% och 100%
```

### Cost Explorer

```bash
# Aktivera Cost Explorer (tar 24h forsta gangen)
# Billing → Cost Explorer → Enable

# Se kostnader per tjanst
aws ce get-cost-and-usage \
    --time-period Start=2025-12-01,End=2025-12-31 \
    --granularity MONTHLY \
    --metrics "BlendedCost" \
    --group-by Type=DIMENSION,Key=SERVICE
```

---

## Pro Tips

> **Tip 1:** ALDRIG hardkoda credentials i kod. Anvand IAM roles, environment variables, eller AWS Secrets Manager.

> **Tip 2:** Aktivera CloudTrail DIREKT. Det loggar alla API-anrop och ar ovarderlligt for security och debugging.

> **Tip 3:** Anvand AWS Organizations om du har flera accounts (dev, staging, prod). Separera miljöer helt.

> **Tip 4:** Tagga ALLT! `Environment: prod`, `Project: webapp`, `Owner: team-x`. Gor kostnadsallokering mojlig.

---

## Hands-on Task

### Uppgift: Satt upp ditt AWS Account sakert

1. **Skapa AWS Account** (om du inte har ett)
   - Anvand en dedikerad email
   - Valj eu-north-1 (Stockholm) som default region

2. **Sakra Root User**
   - Aktivera MFA (Google Authenticator)
   - Spara backup-koder sakert

3. **Skapa Admin IAM User**
   - Username: `admin`
   - Ge `AdministratorAccess` policy
   - Aktivera MFA pa denna ocksa
   - Skapa Access Key for CLI

4. **Konfigurera AWS CLI**
   ```bash
   aws configure
   aws sts get-caller-identity  # Verifiera
   ```

5. **Satt upp Billing Alert**
   - Budget: $10/manad
   - Alert vid 80%

**Verification:**
```bash
# Kör detta - ska visa ditt account ID
aws sts get-caller-identity --query Account --output text
```

''',
    "task": {
        "title": "AWS Account Setup",
        "description": "Satt upp AWS account med MFA, IAM admin user, CLI och billing alerts",
        "xp_reward": 50,
        "estimated_minutes": 30,
        "deliverables": [
            "AWS account med MFA pa root",
            "IAM admin user med MFA",
            "AWS CLI konfigurerad",
            "Billing alert aktiverad"
        ]
    }
}


# =============================================================================
# NODE 2: IAM - Identity & Access Management
# =============================================================================

NODE_02_IAM = {
    "node_id": 2,
    "title": "IAM - Identity & Access Management",
    "slug": "aws-iam",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 70,
    "topics_covered": [
        "IAM users", "IAM groups", "IAM roles", "IAM policies",
        "least privilege", "policy types", "service roles"
    ],
    "content": r'''# IAM - Identity & Access Management

## Varfor IAM ar Kritiskt

> "IAM ar grindvakten till ditt AWS-rike. En felkonfigurerad policy kan antingen lasa ute alla eller ge en hackare nycklarna till kungariket."

IAM ar gratis men det viktigaste du konfigurerar i AWS.

---

## IAM Koncept

### IAM Byggstenar

```
                        IAM STRUCTURE
┌─────────────────────────────────────────────────────────────┐
│                         AWS ACCOUNT                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                        IAM                           │    │
│  │                                                      │    │
│  │   USERS          GROUPS           ROLES             │    │
│  │   ┌─────┐        ┌─────┐         ┌─────┐           │    │
│  │   │Alice│        │Devs │         │EC2  │           │    │
│  │   │Bob  │   →    │Admin│    ←    │Role │           │    │
│  │   │Carl │        │     │         │     │           │    │
│  │   └─────┘        └─────┘         └─────┘           │    │
│  │      │              │               │               │    │
│  │      └──────────────┴───────────────┘               │    │
│  │                     │                               │    │
│  │              ┌──────▼──────┐                        │    │
│  │              │  POLICIES   │                        │    │
│  │              │ (JSON docs) │                        │    │
│  │              └─────────────┘                        │    │
│  │                                                      │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

| Komponent | Beskrivning | Exempel |
|-----------|-------------|---------|
| **User** | En person eller applikation | `alice`, `ci-bot` |
| **Group** | Samling av users | `developers`, `admins` |
| **Role** | Temporara credentials | `ec2-s3-role` |
| **Policy** | Permissions (JSON) | `AmazonS3ReadOnlyAccess` |

---

## IAM Users & Groups

### Skapa User via CLI

```bash
# Skapa user
aws iam create-user --user-name developer-alice

# Lagg till i grupp
aws iam add-user-to-group \
    --user-name developer-alice \
    --group-name Developers

# Skapa access key (for CLI/SDK)
aws iam create-access-key --user-name developer-alice

# Skapa login profile (for Console)
aws iam create-login-profile \
    --user-name developer-alice \
    --password "TempPass123!" \
    --password-reset-required
```

### Skapa Group

```bash
# Skapa grupp
aws iam create-group --group-name Developers

# Attacha policy till grupp
aws iam attach-group-policy \
    --group-name Developers \
    --policy-arn arn:aws:iam::aws:policy/PowerUserAccess

# Lista grupp-medlemmar
aws iam get-group --group-name Developers
```

---

## IAM Policies

### Policy Structure

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3Read",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "192.168.1.0/24"
                }
            }
        }
    ]
}
```

| Element | Beskrivning |
|---------|-------------|
| `Version` | Alltid "2012-10-17" |
| `Statement` | Array av permissions |
| `Sid` | Statement ID (valfritt) |
| `Effect` | Allow eller Deny |
| `Action` | API-operationer |
| `Resource` | ARN till resurser |
| `Condition` | Extra villkor |

### Policy Types

```
┌─────────────────────────────────────────────────────────┐
│                    POLICY TYPES                          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  AWS MANAGED          CUSTOMER MANAGED     INLINE       │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐ │
│  │ Skapade  │         │ Du skapar│        │ Direkt pa│ │
│  │ av AWS   │         │ sjalv    │        │ user/role│ │
│  │          │         │          │        │          │ │
│  │ ReadOnly │         │ CustomS3 │        │ {inline} │ │
│  │ PowerUser│         │ MyAppPol │        │          │ │
│  └──────────┘         └──────────┘        └──────────┘ │
│       ↓                    ↓                   ↓        │
│  Anvand forst!       For specifika          Undvik!    │
│  Enkelt, sakert      behov                  Svart att  │
│                                             underhalla │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Vanliga AWS Managed Policies

| Policy | Ger tillgang till |
|--------|-------------------|
| `AdministratorAccess` | ALLT (farligt!) |
| `PowerUserAccess` | Allt utom IAM/Org |
| `ReadOnlyAccess` | Lasa allt |
| `AmazonS3FullAccess` | S3 full access |
| `AmazonEC2FullAccess` | EC2 full access |
| `AmazonVPCReadOnlyAccess` | VPC read-only |

---

## IAM Roles

### Varfor Roles?

```
SCENARIO: EC2 behover lasa fran S3

DÅLIGT (hardkodade credentials):
┌─────────┐
│   EC2   │ ──── Access Key i kod ──── RISK! Kan lackas
└─────────┘

BRA (IAM Role):
┌─────────┐     ┌─────────┐     ┌─────────┐
│   EC2   │ ←── │  Role   │ ←── │  Policy │
└─────────┘     └─────────┘     └─────────┘
                     ↓
              Temporara credentials
              Roteras automatiskt
```

### Skapa EC2 Role

```bash
# 1. Skapa trust policy (vem far anvanda rollen)
cat > trust-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF

# 2. Skapa rollen
aws iam create-role \
    --role-name EC2-S3-Access \
    --assume-role-policy-document file://trust-policy.json

# 3. Attacha policy
aws iam attach-role-policy \
    --role-name EC2-S3-Access \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# 4. Skapa instance profile (for EC2)
aws iam create-instance-profile \
    --instance-profile-name EC2-S3-Access-Profile

aws iam add-role-to-instance-profile \
    --instance-profile-name EC2-S3-Access-Profile \
    --role-name EC2-S3-Access
```

### Assume Role (Cross-Account)

```bash
# Anta en roll i annat account
aws sts assume-role \
    --role-arn arn:aws:iam::987654321098:role/CrossAccountRole \
    --role-session-name my-session

# Returnerar temporara credentials:
# {
#     "Credentials": {
#         "AccessKeyId": "ASIA...",
#         "SecretAccessKey": "...",
#         "SessionToken": "...",
#         "Expiration": "2025-12-02T12:00:00Z"
#     }
# }

# Anvand credentials
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
```

---

## Least Privilege Principle

### Vad ar Least Privilege?

```
┌─────────────────────────────────────────────────────────┐
│                  LEAST PRIVILEGE                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  DÅLIGT: "Give them admin, easier that way"             │
│  ┌─────────────────────────────────────────────┐        │
│  │  User → AdministratorAccess → ALLT          │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
│  BRA: "Give minimum needed to do the job"               │
│  ┌─────────────────────────────────────────────┐        │
│  │  User → S3ReadOnly → Endast lasa S3         │        │
│  │       → EC2Describe → Endast lista EC2      │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Praktiskt Exempel

```json
// DÅLIGT: Full S3 access
{
    "Effect": "Allow",
    "Action": "s3:*",
    "Resource": "*"
}

// BRA: Endast specifik bucket, endast lasa
{
    "Effect": "Allow",
    "Action": [
        "s3:GetObject",
        "s3:ListBucket"
    ],
    "Resource": [
        "arn:aws:s3:::my-app-logs",
        "arn:aws:s3:::my-app-logs/*"
    ]
}
```

---

## Pro Tips

> **Tip 1:** Anvand ALLTID groups for users. Lagg aldrig policies direkt pa users.

> **Tip 2:** Starta med AWS Managed Policies, skapa custom endast vid behov.

> **Tip 3:** Anvand IAM Access Analyzer for att hitta unused permissions och over-privileged roles.

> **Tip 4:** Enable MFA for alla users, speciellt de med console access.

> **Tip 5:** Anvand `aws iam simulate-principal-policy` for att testa policies innan deployment.

---

## Hands-on Task

### Uppgift: Skapa en saker IAM-struktur

1. **Skapa Groups**
   ```bash
   aws iam create-group --group-name Developers
   aws iam create-group --group-name ReadOnlyUsers
   ```

2. **Attacha Policies till Groups**
   ```bash
   # Developers far PowerUser
   aws iam attach-group-policy \
       --group-name Developers \
       --policy-arn arn:aws:iam::aws:policy/PowerUserAccess

   # ReadOnly far bara lasa
   aws iam attach-group-policy \
       --group-name ReadOnlyUsers \
       --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
   ```

3. **Skapa en custom policy for S3**
   ```bash
   # Skapa policy.json med specifik bucket access
   aws iam create-policy \
       --policy-name MyAppS3Policy \
       --policy-document file://s3-policy.json
   ```

4. **Skapa EC2 Role**
   - Trust policy for ec2.amazonaws.com
   - Attacha S3 read policy
   - Skapa instance profile

**Verification:**
```bash
aws iam list-groups
aws iam list-attached-group-policies --group-name Developers
aws iam list-roles --query "Roles[?RoleName=='EC2-S3-Access']"
```

''',
    "task": {
        "title": "IAM Structure Setup",
        "description": "Skapa saker IAM-struktur med groups, users, roles och policies",
        "xp_reward": 70,
        "estimated_minutes": 45,
        "deliverables": [
            "Developers och ReadOnly groups",
            "Custom S3 policy",
            "EC2 role med instance profile",
            "Dokumenterad permission-struktur"
        ]
    }
}


# =============================================================================
# NODE 3: VPC - Virtual Private Cloud
# =============================================================================

NODE_03_VPC = {
    "node_id": 3,
    "title": "VPC - Virtual Private Cloud",
    "slug": "aws-vpc",
    "difficulty": "intermediate",
    "estimated_minutes": 75,
    "xp_reward": 80,
    "topics_covered": [
        "VPC", "subnets", "route tables", "internet gateway",
        "NAT gateway", "security groups", "NACLs", "CIDR"
    ],
    "content": r'''# VPC - Virtual Private Cloud

## Varfor VPC ar Fundamentalt

> "VPC ar ditt privata natverk i molnet. Utan forstaelse for VPC kan du inte bygga saker, skalbar infrastruktur i AWS."

Tanka pa VPC som ditt eget datacenter i AWS - du bestammer vilka IP-ranges, subnets, routing och brandvaggar.

---

## VPC Koncept

### VPC Arkitektur

```
                        VPC ARCHITECTURE
┌─────────────────────────────────────────────────────────────┐
│  VPC: 10.0.0.0/16 (65,536 IPs)                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                                                     │    │
│  │   PUBLIC SUBNETS                PRIVATE SUBNETS    │    │
│  │   ┌──────────────┐              ┌──────────────┐   │    │
│  │   │ 10.0.1.0/24  │              │ 10.0.3.0/24  │   │    │
│  │   │ (AZ-a)       │              │ (AZ-a)       │   │    │
│  │   │  ┌────────┐  │              │  ┌────────┐  │   │    │
│  │   │  │  EC2   │  │              │  │  EC2   │  │   │    │
│  │   │  │ (web)  │  │              │  │ (app)  │  │   │    │
│  │   │  └────────┘  │              │  └────────┘  │   │    │
│  │   └──────────────┘              └──────────────┘   │    │
│  │   ┌──────────────┐              ┌──────────────┐   │    │
│  │   │ 10.0.2.0/24  │              │ 10.0.4.0/24  │   │    │
│  │   │ (AZ-b)       │              │ (AZ-b)       │   │    │
│  │   │  ┌────────┐  │              │  ┌────────┐  │   │    │
│  │   │  │  EC2   │  │              │  │  RDS   │  │   │    │
│  │   │  │ (web)  │  │              │  │ (db)   │  │   │    │
│  │   │  └────────┘  │              │  └────────┘  │   │    │
│  │   └──────────────┘              └──────────────┘   │    │
│  │         │                              │           │    │
│  │         ▼                              ▼           │    │
│  │   ┌──────────┐                   ┌──────────┐     │    │
│  │   │ Internet │                   │   NAT    │     │    │
│  │   │ Gateway  │                   │ Gateway  │     │    │
│  │   └──────────┘                   └──────────┘     │    │
│  │         │                              │           │    │
│  └─────────┼──────────────────────────────┼───────────┘    │
│            │                              │                 │
│            ▼                              ▼                 │
│       INTERNET                    Outbound only            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Komponenter

| Komponent | Syfte |
|-----------|-------|
| **VPC** | Ditt isolerade natverk |
| **Subnet** | Del av VPC i en AZ |
| **Route Table** | Routing-regler |
| **Internet Gateway** | VPC ↔ Internet |
| **NAT Gateway** | Private subnet → Internet |
| **Security Group** | Instans-firewall |
| **NACL** | Subnet-firewall |

---

## CIDR Blocks

### Forsta CIDR Notation

```
10.0.0.0/16
    │    │
    │    └── Prefix length (hur manga bits ar natverk)
    └────── Natverk-adress

/16 = 65,536 IPs (2^16)
/24 = 256 IPs (2^8)
/28 = 16 IPs (2^4)
```

### Vanliga CIDR Blocks

| CIDR | IPs | Anvandning |
|------|-----|------------|
| 10.0.0.0/16 | 65,536 | Stor VPC |
| 10.0.0.0/24 | 256 | Typisk subnet |
| 10.0.0.0/28 | 16 | Minsta subnet i AWS |

### Planera Subnets

```
VPC: 10.0.0.0/16

Public Subnets:
├── 10.0.1.0/24  (AZ-a) - 256 IPs
├── 10.0.2.0/24  (AZ-b) - 256 IPs
└── 10.0.3.0/24  (AZ-c) - 256 IPs

Private Subnets:
├── 10.0.10.0/24 (AZ-a) - 256 IPs
├── 10.0.11.0/24 (AZ-b) - 256 IPs
└── 10.0.12.0/24 (AZ-c) - 256 IPs

Database Subnets:
├── 10.0.20.0/24 (AZ-a) - 256 IPs
├── 10.0.21.0/24 (AZ-b) - 256 IPs
└── 10.0.22.0/24 (AZ-c) - 256 IPs
```

---

## Skapa VPC med CLI

### Steg 1: Skapa VPC

```bash
# Skapa VPC
VPC_ID=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=MyVPC}]' \
    --query 'Vpc.VpcId' \
    --output text)

echo "VPC created: $VPC_ID"

# Aktivera DNS hostnames
aws ec2 modify-vpc-attribute \
    --vpc-id $VPC_ID \
    --enable-dns-hostnames '{"Value": true}'
```

### Steg 2: Skapa Subnets

```bash
# Public Subnet AZ-a
PUBLIC_SUBNET_A=$(aws ec2 create-subnet \
    --vpc-id $VPC_ID \
    --cidr-block 10.0.1.0/24 \
    --availability-zone eu-north-1a \
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-AZ-a}]' \
    --query 'Subnet.SubnetId' \
    --output text)

# Private Subnet AZ-a
PRIVATE_SUBNET_A=$(aws ec2 create-subnet \
    --vpc-id $VPC_ID \
    --cidr-block 10.0.10.0/24 \
    --availability-zone eu-north-1a \
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-AZ-a}]' \
    --query 'Subnet.SubnetId' \
    --output text)

echo "Public: $PUBLIC_SUBNET_A"
echo "Private: $PRIVATE_SUBNET_A"
```

### Steg 3: Internet Gateway

```bash
# Skapa Internet Gateway
IGW_ID=$(aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=MyIGW}]' \
    --query 'InternetGateway.InternetGatewayId' \
    --output text)

# Attacha till VPC
aws ec2 attach-internet-gateway \
    --internet-gateway-id $IGW_ID \
    --vpc-id $VPC_ID

echo "IGW attached: $IGW_ID"
```

### Steg 4: Route Tables

```bash
# Skapa public route table
PUBLIC_RT=$(aws ec2 create-route-table \
    --vpc-id $VPC_ID \
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Public-RT}]' \
    --query 'RouteTable.RouteTableId' \
    --output text)

# Lagg till route till Internet
aws ec2 create-route \
    --route-table-id $PUBLIC_RT \
    --destination-cidr-block 0.0.0.0/0 \
    --gateway-id $IGW_ID

# Associera med public subnet
aws ec2 associate-route-table \
    --route-table-id $PUBLIC_RT \
    --subnet-id $PUBLIC_SUBNET_A
```

### Steg 5: NAT Gateway (for private subnets)

```bash
# Skapa Elastic IP
EIP_ALLOC=$(aws ec2 allocate-address \
    --domain vpc \
    --query 'AllocationId' \
    --output text)

# Skapa NAT Gateway i public subnet
NAT_GW=$(aws ec2 create-nat-gateway \
    --subnet-id $PUBLIC_SUBNET_A \
    --allocation-id $EIP_ALLOC \
    --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=MyNAT}]' \
    --query 'NatGateway.NatGatewayId' \
    --output text)

# Vanta tills NAT ar available
aws ec2 wait nat-gateway-available --nat-gateway-ids $NAT_GW

# Skapa private route table
PRIVATE_RT=$(aws ec2 create-route-table \
    --vpc-id $VPC_ID \
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Private-RT}]' \
    --query 'RouteTable.RouteTableId' \
    --output text)

# Route till NAT Gateway
aws ec2 create-route \
    --route-table-id $PRIVATE_RT \
    --destination-cidr-block 0.0.0.0/0 \
    --nat-gateway-id $NAT_GW

# Associera med private subnet
aws ec2 associate-route-table \
    --route-table-id $PRIVATE_RT \
    --subnet-id $PRIVATE_SUBNET_A
```

---

## Security Groups vs NACLs

### Jamforelse

```
┌─────────────────────────────────────────────────────────────┐
│           SECURITY GROUPS vs NACLs                          │
├─────────────────────┬───────────────────────────────────────┤
│   SECURITY GROUP    │              NACL                     │
├─────────────────────┼───────────────────────────────────────┤
│ Instans-niva        │ Subnet-niva                           │
│ Stateful            │ Stateless                             │
│ Bara Allow-regler   │ Allow + Deny                          │
│ Utvardering: Alla   │ Utvardering: Ordning (nummer)         │
│ Default: Deny all in│ Default: Allow all                    │
└─────────────────────┴───────────────────────────────────────┘
```

### Security Group Exempel

```bash
# Skapa Security Group
WEB_SG=$(aws ec2 create-security-group \
    --group-name WebServerSG \
    --description "Web Server Security Group" \
    --vpc-id $VPC_ID \
    --query 'GroupId' \
    --output text)

# Tillt HTTP fran Internet
aws ec2 authorize-security-group-ingress \
    --group-id $WEB_SG \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0

# Tillt HTTPS fran Internet
aws ec2 authorize-security-group-ingress \
    --group-id $WEB_SG \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0

# Tillt SSH bara fran din IP
MY_IP=$(curl -s https://checkip.amazonaws.com)
aws ec2 authorize-security-group-ingress \
    --group-id $WEB_SG \
    --protocol tcp \
    --port 22 \
    --cidr ${MY_IP}/32
```

### NACL Exempel

```bash
# Skapa NACL
NACL_ID=$(aws ec2 create-network-acl \
    --vpc-id $VPC_ID \
    --tag-specifications 'ResourceType=network-acl,Tags=[{Key=Name,Value=Public-NACL}]' \
    --query 'NetworkAcl.NetworkAclId' \
    --output text)

# Allow inbound HTTP
aws ec2 create-network-acl-entry \
    --network-acl-id $NACL_ID \
    --ingress \
    --rule-number 100 \
    --protocol tcp \
    --port-range From=80,To=80 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow

# Allow outbound all
aws ec2 create-network-acl-entry \
    --network-acl-id $NACL_ID \
    --egress \
    --rule-number 100 \
    --protocol -1 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow
```

---

## Pro Tips

> **Tip 1:** Planera dina CIDR blocks noggrant - du kan INTE andra VPC CIDR efter skapande (men kan lagga till sekundara).

> **Tip 2:** NAT Gateway kostar ~$32/manad + dataoverforings-kostnader. For dev/test, overvag NAT Instance (billigare men mer arbete).

> **Tip 3:** Anvand VPC Flow Logs for att logga all natverkstrafik - ovarderlligt for security och debugging.

> **Tip 4:** En Security Group kan referera till en annan SG istallet for CIDR - mycket sakrare for inter-service kommunikation.

---

## Hands-on Task

### Uppgift: Bygg en produktionsklar VPC

Skapa en VPC med:
- 2 public subnets (olika AZ)
- 2 private subnets (olika AZ)
- Internet Gateway
- NAT Gateway
- Route tables korrekt konfigurerade
- Security groups for web och app tiers

**Script att kora:**
```bash
#!/bin/bash
# vpc-setup.sh

REGION="eu-north-1"
VPC_CIDR="10.0.0.0/16"
PUBLIC_A="10.0.1.0/24"
PUBLIC_B="10.0.2.0/24"
PRIVATE_A="10.0.10.0/24"
PRIVATE_B="10.0.11.0/24"

# ... implementera resten
```

**Verification:**
```bash
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=MyVPC"
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC_ID"
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$VPC_ID"
```

''',
    "task": {
        "title": "Production VPC Setup",
        "description": "Bygg en multi-AZ VPC med public/private subnets och korrekt routing",
        "xp_reward": 80,
        "estimated_minutes": 60,
        "deliverables": [
            "VPC med 10.0.0.0/16 CIDR",
            "4 subnets (2 public, 2 private)",
            "Internet Gateway + NAT Gateway",
            "Route tables konfigurerade",
            "Security groups for web tier"
        ]
    }
}


# =============================================================================
# NODE 4: EC2 - Elastic Compute Cloud
# =============================================================================

NODE_04_EC2 = {
    "node_id": 4,
    "title": "EC2 - Elastic Compute Cloud",
    "slug": "aws-ec2",
    "difficulty": "intermediate",
    "estimated_minutes": 75,
    "xp_reward": 80,
    "topics_covered": [
        "EC2 instances", "AMIs", "instance types", "key pairs",
        "user data", "EBS volumes", "elastic IPs", "placement groups"
    ],
    "content": r'''# EC2 - Elastic Compute Cloud

## Varfor EC2 ar Fundamentalt

> "EC2 ar AWS:s brød och smoør - virtuella servrar pa demand. Forstar du EC2, forstar du cloud computing."

Med EC2 kan du starta en server pa sekunder och betala per timme (eller sekund).

---

## EC2 Koncept

### EC2 Arkitektur

```
                         EC2 INSTANCE
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    EC2 INSTANCE                       │  │
│  │                                                       │  │
│  │   ┌─────────────┐    ┌─────────────┐                 │  │
│  │   │    vCPU     │    │   Memory    │                 │  │
│  │   │   (2-128+)  │    │  (1-768GB)  │                 │  │
│  │   └─────────────┘    └─────────────┘                 │  │
│  │                                                       │  │
│  │   ┌─────────────────────────────────────────────┐    │  │
│  │   │              ROOT VOLUME (EBS)               │    │  │
│  │   │         /dev/xvda (8-16GB typical)          │    │  │
│  │   └─────────────────────────────────────────────┘    │  │
│  │                                                       │  │
│  │   ┌─────────────────────────────────────────────┐    │  │
│  │   │            NETWORK INTERFACE                 │    │  │
│  │   │     Private IP: 10.0.1.45                   │    │  │
│  │   │     Public IP: 52.xxx.xxx.xxx (optional)    │    │  │
│  │   └─────────────────────────────────────────────┘    │  │
│  │                                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                 │
│              ┌────────────┴────────────┐                   │
│              │     Security Group      │                   │
│              │    (Virtual Firewall)   │                   │
│              └─────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Instance Types

### Instance Type Naming

```
m5.xlarge
│ │  │
│ │  └── Size: nano, micro, small, medium, large, xlarge, 2xlarge...
│ └───── Generation: 5th generation
└────── Family: m = general purpose
```

### Instance Families

| Family | Optimerat for | Exempel |
|--------|---------------|---------|
| **t3** | Burstable, general | t3.micro, t3.small |
| **m6i** | General purpose | m6i.large, m6i.xlarge |
| **c6i** | Compute | c6i.large (high CPU) |
| **r6i** | Memory | r6i.large (high RAM) |
| **i3** | Storage | i3.large (high IOPS) |
| **g5** | GPU/Graphics | g5.xlarge (ML, gaming) |

### Vanliga Val

| Use Case | Rekommendation |
|----------|----------------|
| Dev/Test | t3.micro (free tier) |
| Web Server | t3.small - t3.medium |
| Application | m6i.large - m6i.xlarge |
| Database | r6i.large - r6i.2xlarge |
| CI/CD Build | c6i.large - c6i.xlarge |

---

## Starta EC2 Instance

### Via CLI

```bash
# Hinta senaste Amazon Linux 2023 AMI
AMI_ID=$(aws ec2 describe-images \
    --owners amazon \
    --filters \
        "Name=name,Values=al2023-ami-2023*-x86_64" \
        "Name=state,Values=available" \
    --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
    --output text)

echo "Latest AMI: $AMI_ID"

# Starta instans
INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $AMI_ID \
    --instance-type t3.micro \
    --key-name my-key \
    --security-group-ids $WEB_SG \
    --subnet-id $PUBLIC_SUBNET_A \
    --associate-public-ip-address \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
    --query 'Instances[0].InstanceId' \
    --output text)

echo "Instance started: $INSTANCE_ID"

# Vanta tills running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Hamta public IP
PUBLIC_IP=$(aws ec2 describe-instances \
    --instance-ids $INSTANCE_ID \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text)

echo "Public IP: $PUBLIC_IP"
```

### Key Pairs

```bash
# Skapa key pair
aws ec2 create-key-pair \
    --key-name my-key \
    --query 'KeyMaterial' \
    --output text > my-key.pem

# Satt permissions
chmod 400 my-key.pem

# SSH till instans
ssh -i my-key.pem ec2-user@$PUBLIC_IP
```

---

## User Data (Bootstrap Scripts)

### Vad ar User Data?

```
┌─────────────────────────────────────────────────────────────┐
│                      USER DATA                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Script som kors AUTOMATISKT vid forsta boot                │
│                                                              │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐      │
│  │  EC2 Start │ ──▶ │ User Data  │ ──▶ │   Server   │      │
│  │            │     │   Script   │     │   Ready!   │      │
│  └────────────┘     └────────────┘     └────────────┘      │
│                                                              │
│  Perfekt for:                                                │
│  - Installera software                                       │
│  - Konfigurera services                                      │
│  - Ladda ner applikation                                     │
│  - Starta processer                                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### User Data Exempel

```bash
#!/bin/bash
# user-data.sh

# Uppdatera system
yum update -y

# Installera nginx
amazon-linux-extras install nginx1 -y

# Starta nginx
systemctl start nginx
systemctl enable nginx

# Skapa enkel sida
cat > /usr/share/nginx/html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>EC2 Web Server</title></head>
<body>
<h1>Hello from EC2!</h1>
<p>Instance ID: $(curl -s http://169.254.169.254/latest/meta-data/instance-id)</p>
<p>AZ: $(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)</p>
</body>
</html>
EOF

# Restart nginx
systemctl restart nginx
```

### Anvand User Data vid Launch

```bash
# Base64-encode scriptet
USER_DATA=$(base64 -w 0 user-data.sh)

# Starta med user data
aws ec2 run-instances \
    --image-id $AMI_ID \
    --instance-type t3.micro \
    --key-name my-key \
    --security-group-ids $WEB_SG \
    --subnet-id $PUBLIC_SUBNET_A \
    --associate-public-ip-address \
    --user-data file://user-data.sh \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]'
```

---

## EBS Volumes

### Volume Types

| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| **gp3** | 3000-16000 | 125-1000 MB/s | General (default) |
| **gp2** | 100-16000 | Burst | Legacy general |
| **io2** | 64000 | 1000 MB/s | High-perf DB |
| **st1** | 500 | 500 MB/s | Big data, logs |
| **sc1** | 250 | 250 MB/s | Cold storage |

### Skapa och Attacha Volume

```bash
# Skapa 100GB gp3 volume
VOLUME_ID=$(aws ec2 create-volume \
    --availability-zone eu-north-1a \
    --size 100 \
    --volume-type gp3 \
    --tag-specifications 'ResourceType=volume,Tags=[{Key=Name,Value=DataVolume}]' \
    --query 'VolumeId' \
    --output text)

# Vanta tills available
aws ec2 wait volume-available --volume-ids $VOLUME_ID

# Attacha till instans
aws ec2 attach-volume \
    --volume-id $VOLUME_ID \
    --instance-id $INSTANCE_ID \
    --device /dev/xvdf

# Pa instansen: formatera och mounta
ssh -i my-key.pem ec2-user@$PUBLIC_IP << 'EOF'
sudo mkfs -t xfs /dev/xvdf
sudo mkdir /data
sudo mount /dev/xvdf /data
echo "/dev/xvdf /data xfs defaults,nofail 0 2" | sudo tee -a /etc/fstab
EOF
```

---

## Instance Metadata

### Hamta Metadata fran Instansen

```bash
# Pa EC2-instansen:

# Instance ID
curl http://169.254.169.254/latest/meta-data/instance-id
# i-0abcd1234567890ef

# Availability Zone
curl http://169.254.169.254/latest/meta-data/placement/availability-zone
# eu-north-1a

# Public IP
curl http://169.254.169.254/latest/meta-data/public-ipv4
# 52.xxx.xxx.xxx

# Instance Type
curl http://169.254.169.254/latest/meta-data/instance-type
# t3.micro

# IAM Role credentials (om role ar attachad)
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/MyRole

# User Data
curl http://169.254.169.254/latest/user-data
```

### IMDSv2 (Sakrare)

```bash
# Hamta token forst
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
    -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Anvand token
curl -H "X-aws-ec2-metadata-token: $TOKEN" \
    http://169.254.169.254/latest/meta-data/instance-id
```

---

## EC2 Lifecycle

### Instance States

```
┌─────────────────────────────────────────────────────────────┐
│                    EC2 LIFECYCLE                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────┐                                               │
│   │ pending │ ──── Instance starting                        │
│   └────┬────┘                                               │
│        │                                                     │
│        ▼                                                     │
│   ┌─────────┐                                               │
│   │ running │ ◀──── Normal operation                        │
│   └────┬────┘                                               │
│        │                                                     │
│   ┌────┴────┐                                               │
│   │         │                                                │
│   ▼         ▼                                                │
│ ┌─────────┐ ┌──────────┐                                    │
│ │stopping │ │shutting- │                                    │
│ │         │ │down      │                                    │
│ └────┬────┘ └────┬─────┘                                    │
│      │           │                                           │
│      ▼           ▼                                           │
│ ┌─────────┐ ┌──────────┐                                    │
│ │ stopped │ │terminated│                                    │
│ │(no cost)│ │ (gone!)  │                                    │
│ └─────────┘ └──────────┘                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘

VIKTIGT:
- Stopped = No compute cost, EBS cost continues
- Terminated = Instance DELETED, data lost (unless EBS preserved)
```

### Hantera Instances

```bash
# Stoppa instans (bevarar data)
aws ec2 stop-instances --instance-ids $INSTANCE_ID

# Starta igen
aws ec2 start-instances --instance-ids $INSTANCE_ID

# Reboota
aws ec2 reboot-instances --instance-ids $INSTANCE_ID

# Terminera (RADERA!)
aws ec2 terminate-instances --instance-ids $INSTANCE_ID
```

---

## Pro Tips

> **Tip 1:** Anvand Launch Templates istallet for att manuellt specificera parametrar varje gang.

> **Tip 2:** Satt `DeleteOnTermination: false` pa viktiga EBS volumes for att undvika dataforlust.

> **Tip 3:** Anvand Spot Instances for up to 90% rabatt pa non-critical workloads.

> **Tip 4:** Aktivera detailed monitoring ($2.10/instans/manad) for 1-minute metrics istallet for 5-minute.

> **Tip 5:** Anvand EC2 Instance Connect for att SSH utan att hantera key pairs.

---

## Hands-on Task

### Uppgift: Deploya en Web Server

1. **Skapa Key Pair**
   ```bash
   aws ec2 create-key-pair --key-name webserver-key ...
   ```

2. **Skapa Security Group**
   - Allow HTTP (80) fran Internet
   - Allow SSH (22) fran din IP

3. **Starta EC2 med User Data**
   - Amazon Linux 2023
   - t3.micro
   - User data som installerar nginx

4. **Verifiera**
   - SSH in och kolla nginx status
   - Oppna public IP i webblasare

5. **Cleanup**
   - Stoppa (inte terminera!) instansen

**Verification:**
```bash
curl http://$PUBLIC_IP
# Ska visa din nginx-sida
```

''',
    "task": {
        "title": "Deploy EC2 Web Server",
        "description": "Starta en EC2 instans med nginx via user data",
        "xp_reward": 80,
        "estimated_minutes": 45,
        "deliverables": [
            "Key pair skapad",
            "Security group med HTTP/SSH",
            "EC2 instans med nginx",
            "Fungerande webbsida pa public IP"
        ]
    }
}


# =============================================================================
# AGGREGATE ALL NODES (Block 1: 1-4)
# =============================================================================

AWS_SKILLSMAP_NODES_BLOCK_1 = [
    NODE_01_AWS_INTRO,
    NODE_02_IAM,
    NODE_03_VPC,
    NODE_04_EC2,
]


# =============================================================================
# NODE 5: S3 - Simple Storage Service
# =============================================================================

NODE_05_S3 = {
    "node_id": 5,
    "title": "S3 - Simple Storage Service",
    "slug": "aws-s3",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 70,
    "topics_covered": [
        "S3 buckets", "objects", "storage classes", "versioning",
        "lifecycle policies", "encryption", "access control", "static hosting"
    ],
    "content": r'''# S3 - Simple Storage Service

## Varfor S3 ar Overallt

> "S3 ar inte bara storage - det ar fundamentet for AWS. Lambda kod lagras i S3. CloudFormation templates. Application logs. Backups. Allt."

S3 ar designat for 99.999999999% (11 9:or) durability. Du forlorar 1 objekt av 10 miljarder pa 10,000 ar.

---

## S3 Koncept

### S3 Arkitektur

```
                           S3 STRUCTURE
┌─────────────────────────────────────────────────────────────┐
│                         S3 BUCKET                            │
│                    my-company-data-prod                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                                                     │    │
│  │   /logs/                                            │    │
│  │   ├── app/                                          │    │
│  │   │   ├── 2025-12-01.log                           │    │
│  │   │   └── 2025-12-02.log                           │    │
│  │   └── access/                                       │    │
│  │       └── access.log                                │    │
│  │                                                     │    │
│  │   /backups/                                         │    │
│  │   ├── db-backup-2025-12-01.sql.gz                  │    │
│  │   └── db-backup-2025-12-02.sql.gz                  │    │
│  │                                                     │    │
│  │   /static/                                          │    │
│  │   ├── images/                                       │    │
│  │   │   └── logo.png                                 │    │
│  │   └── css/                                          │    │
│  │       └── style.css                                │    │
│  │                                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘

VIKTIGT:
- Bucket name = Globalt unikt (hela AWS)
- Object key = Full path (logs/app/2025-12-01.log)
- Max object size = 5TB
- Max PUT = 5GB (anvand multipart for storre)
```

---

## Bucket Operations

### Skapa Bucket

```bash
# Skapa bucket (namn maste vara globalt unikt!)
aws s3 mb s3://my-unique-bucket-name-12345

# Med specifik region
aws s3api create-bucket \
    --bucket my-unique-bucket-name-12345 \
    --region eu-north-1 \
    --create-bucket-configuration LocationConstraint=eu-north-1

# Lista buckets
aws s3 ls

# Lista innehall
aws s3 ls s3://my-bucket/
aws s3 ls s3://my-bucket/logs/ --recursive
```

### Upload/Download

```bash
# Upload en fil
aws s3 cp myfile.txt s3://my-bucket/

# Upload med specifik key
aws s3 cp myfile.txt s3://my-bucket/data/myfile.txt

# Upload hel mapp
aws s3 cp ./local-folder s3://my-bucket/folder/ --recursive

# Download
aws s3 cp s3://my-bucket/myfile.txt ./

# Sync (smart upload - bara forandringar)
aws s3 sync ./local-folder s3://my-bucket/folder/
aws s3 sync s3://my-bucket/folder/ ./local-folder

# Ta bort
aws s3 rm s3://my-bucket/myfile.txt
aws s3 rm s3://my-bucket/folder/ --recursive
```

---

## Storage Classes

### Jamforelse

```
┌─────────────────────────────────────────────────────────────┐
│                    S3 STORAGE CLASSES                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  STANDARD          STANDARD-IA       GLACIER               │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐          │
│  │ Frequent │      │Infrequent│      │  Archive │          │
│  │  Access  │      │  Access  │      │          │          │
│  │          │      │          │      │          │          │
│  │ $0.023/GB│      │ $0.0125/GB│     │$0.004/GB │          │
│  │          │      │ +retrieval│      │ +hours   │          │
│  └──────────┘      └──────────┘      └──────────┘          │
│       │                 │                  │                │
│       ▼                 ▼                  ▼                │
│  App data,        Backups >30d,      Archives,             │
│  frequently       DR data            compliance            │
│  accessed                            7+ years              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

| Class | Cost/GB | Retrieval | Use Case |
|-------|---------|-----------|----------|
| **Standard** | $0.023 | Instant | Frequent access |
| **Standard-IA** | $0.0125 | Instant | Infrequent (30+ days) |
| **One Zone-IA** | $0.01 | Instant | Non-critical |
| **Glacier Instant** | $0.004 | Instant | Long-term, rare |
| **Glacier Flexible** | $0.0036 | 1-5 hours | Archives |
| **Glacier Deep** | $0.00099 | 12 hours | Compliance |

### Satt Storage Class

```bash
# Upload med specifik class
aws s3 cp backup.tar.gz s3://my-bucket/ --storage-class STANDARD_IA

# Andra class for existerande objekt
aws s3 cp s3://my-bucket/old-data.zip s3://my-bucket/old-data.zip \
    --storage-class GLACIER
```

---

## Versioning

### Aktivera Versioning

```bash
# Aktivera versioning pa bucket
aws s3api put-bucket-versioning \
    --bucket my-bucket \
    --versioning-configuration Status=Enabled

# Kolla status
aws s3api get-bucket-versioning --bucket my-bucket

# Lista alla versioner
aws s3api list-object-versions --bucket my-bucket
```

### Arbeta med Versions

```bash
# Ladda upp ny version (automatiskt om versioning ar aktiverat)
aws s3 cp config.json s3://my-bucket/

# Hamta specifik version
aws s3api get-object \
    --bucket my-bucket \
    --key config.json \
    --version-id "abc123xyz" \
    config-old.json

# Ta bort specifik version
aws s3api delete-object \
    --bucket my-bucket \
    --key config.json \
    --version-id "abc123xyz"
```

---

## Lifecycle Policies

### Automatisk Tiering

```json
{
    "Rules": [
        {
            "ID": "MoveToIAAfter30Days",
            "Status": "Enabled",
            "Filter": {
                "Prefix": "logs/"
            },
            "Transitions": [
                {
                    "Days": 30,
                    "StorageClass": "STANDARD_IA"
                },
                {
                    "Days": 90,
                    "StorageClass": "GLACIER"
                }
            ],
            "Expiration": {
                "Days": 365
            }
        }
    ]
}
```

```bash
# Applicera lifecycle policy
aws s3api put-bucket-lifecycle-configuration \
    --bucket my-bucket \
    --lifecycle-configuration file://lifecycle.json
```

---

## Access Control

### Bucket Policy Exempel

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForWebsite",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-website-bucket/*"
        }
    ]
}
```

### Block Public Access

```bash
# Blockera ALL public access (rekommenderat!)
aws s3api put-public-access-block \
    --bucket my-bucket \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

---

## Static Website Hosting

### Konfigurera Website

```bash
# Aktivera website hosting
aws s3 website s3://my-website-bucket \
    --index-document index.html \
    --error-document error.html

# Upload website files
aws s3 sync ./website s3://my-website-bucket/

# URL format:
# http://my-website-bucket.s3-website-eu-north-1.amazonaws.com
```

---

## Pro Tips

> **Tip 1:** Anvand S3 Transfer Acceleration for snabbare uploads over langa avstand (aktivera pa bucket).

> **Tip 2:** S3 Select later dig querya data INNE i objekt (CSV, JSON, Parquet) utan att ladda ner allt.

> **Tip 3:** Anvand presigned URLs for temporar access till privata objekt.

> **Tip 4:** Aktivera S3 Object Lock for WORM (Write Once Read Many) compliance.

---

## Hands-on Task

### Uppgift: S3 for Backup och Static Website

1. **Skapa backup bucket med versioning**
2. **Konfigurera lifecycle policy** (move to IA after 30 days)
3. **Skapa website bucket**
4. **Deploya statisk webbsida**

**Verification:**
```bash
aws s3api get-bucket-versioning --bucket backup-bucket
curl http://website-bucket.s3-website-eu-north-1.amazonaws.com
```

''',
    "task": {
        "title": "S3 Backup & Website",
        "description": "Konfigurera S3 for backups med versioning och statisk webbsida",
        "xp_reward": 70,
        "estimated_minutes": 40,
        "deliverables": [
            "Backup bucket med versioning",
            "Lifecycle policy konfigurerad",
            "Website bucket med static hosting",
            "Fungerande webbsida"
        ]
    }
}


# =============================================================================
# NODE 6: RDS - Relational Database Service
# =============================================================================

NODE_06_RDS = {
    "node_id": 6,
    "title": "RDS - Relational Database Service",
    "slug": "aws-rds",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 75,
    "topics_covered": [
        "RDS engines", "instance classes", "multi-AZ", "read replicas",
        "backups", "snapshots", "parameter groups", "security"
    ],
    "content": r'''# RDS - Relational Database Service

## Varfor RDS istallet for EC2 + Database?

> "Du VILL inte hantera database-servrar. Patching, backups, failover, replication - lat AWS gora det."

RDS ar managed database - du fokuserar pa schema och queries, AWS skoter resten.

---

## RDS vs EC2 Database

```
┌─────────────────────────────────────────────────────────────┐
│             RDS vs SELF-MANAGED (EC2)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  YOU MANAGE              │      AWS MANAGES (RDS)           │
│  ┌───────────────────┐   │   ┌───────────────────┐          │
│  │ Application       │   │   │ Application       │          │
│  │ Optimization      │   │   │ Optimization      │          │
│  │ Queries           │   │   │ Queries           │          │
│  ├───────────────────┤   │   └───────────────────┘          │
│  │ Schema            │   │                                   │
│  │ Scaling           │   │         ┌───────────────┐        │
│  │ High Availability │   │         │ MANAGED:      │        │
│  │ Backups           │   │         │ - Patching    │        │
│  │ Patching          │   │         │ - Backups     │        │
│  │ OS Installation   │   │         │ - HA/Failover │        │
│  │ Server Maintenance│   │         │ - Monitoring  │        │
│  │ Power/Network     │   │         │ - Scaling     │        │
│  └───────────────────┘   │         └───────────────┘        │
│                                                              │
│  Timmar/vecka             │         Minuter/manad           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Supported Engines

| Engine | Version | Use Case |
|--------|---------|----------|
| **PostgreSQL** | 11-16 | OLTP, PostGIS, JSON |
| **MySQL** | 5.7, 8.0 | WordPress, web apps |
| **MariaDB** | 10.x | MySQL-compatible |
| **Oracle** | 12-19c | Enterprise, legacy |
| **SQL Server** | 2014-2022 | .NET applications |
| **Aurora** | MySQL/PostgreSQL | High-perf, auto-scale |

---

## Skapa RDS Instance

### Via CLI

```bash
# Skapa DB subnet group (kraver minst 2 AZs)
aws rds create-db-subnet-group \
    --db-subnet-group-name my-db-subnets \
    --db-subnet-group-description "Private subnets for RDS" \
    --subnet-ids $PRIVATE_SUBNET_A $PRIVATE_SUBNET_B

# Skapa Security Group for RDS
DB_SG=$(aws ec2 create-security-group \
    --group-name DatabaseSG \
    --description "Database Security Group" \
    --vpc-id $VPC_ID \
    --query 'GroupId' --output text)

# Tillt PostgreSQL fran app tier
aws ec2 authorize-security-group-ingress \
    --group-id $DB_SG \
    --protocol tcp \
    --port 5432 \
    --source-group $APP_SG

# Skapa RDS instance
aws rds create-db-instance \
    --db-instance-identifier myapp-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --engine-version 16.1 \
    --master-username admin \
    --master-user-password "SuperSecret123!" \
    --allocated-storage 20 \
    --storage-type gp3 \
    --db-subnet-group-name my-db-subnets \
    --vpc-security-group-ids $DB_SG \
    --no-publicly-accessible \
    --backup-retention-period 7 \
    --preferred-backup-window "03:00-04:00" \
    --preferred-maintenance-window "Mon:04:00-Mon:05:00"

# Vanta tills available (10-15 min)
aws rds wait db-instance-available \
    --db-instance-identifier myapp-db

# Hamta endpoint
ENDPOINT=$(aws rds describe-db-instances \
    --db-instance-identifier myapp-db \
    --query 'DBInstances[0].Endpoint.Address' \
    --output text)

echo "RDS Endpoint: $ENDPOINT"
```

---

## Multi-AZ Deployment

### High Availability

```
┌─────────────────────────────────────────────────────────────┐
│                    MULTI-AZ DEPLOYMENT                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   AZ-a (Primary)              AZ-b (Standby)               │
│   ┌──────────────┐            ┌──────────────┐             │
│   │     RDS      │◀──────────▶│     RDS      │             │
│   │   PRIMARY    │  Sync      │   STANDBY    │             │
│   │              │  Repl.     │              │             │
│   └──────────────┘            └──────────────┘             │
│          │                           │                      │
│          │                           │                      │
│          ▼                           ▼                      │
│   ┌──────────────┐            ┌──────────────┐             │
│   │     EBS      │            │     EBS      │             │
│   └──────────────┘            └──────────────┘             │
│                                                              │
│   VID FAILOVER:                                             │
│   1. Primary fails                                          │
│   2. Standby promoted (60-120 sek)                         │
│   3. DNS endpoint resolves to new primary                  │
│   4. Din app marker inget (samma endpoint)                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Aktivera Multi-AZ
aws rds modify-db-instance \
    --db-instance-identifier myapp-db \
    --multi-az \
    --apply-immediately
```

---

## Read Replicas

### For Read-Heavy Workloads

```bash
# Skapa read replica
aws rds create-db-instance-read-replica \
    --db-instance-identifier myapp-db-replica \
    --source-db-instance-identifier myapp-db \
    --db-instance-class db.t3.micro

# Hamta replica endpoint
REPLICA_ENDPOINT=$(aws rds describe-db-instances \
    --db-instance-identifier myapp-db-replica \
    --query 'DBInstances[0].Endpoint.Address' \
    --output text)

# I din app:
# Writes → Primary endpoint
# Reads → Replica endpoint
```

---

## Backups & Snapshots

### Automated Backups

```bash
# Konfigurera automated backups (retention 7 days)
aws rds modify-db-instance \
    --db-instance-identifier myapp-db \
    --backup-retention-period 7 \
    --preferred-backup-window "03:00-04:00"
```

### Manual Snapshots

```bash
# Skapa snapshot
aws rds create-db-snapshot \
    --db-instance-identifier myapp-db \
    --db-snapshot-identifier myapp-db-snapshot-20251202

# Lista snapshots
aws rds describe-db-snapshots \
    --db-instance-identifier myapp-db

# Restore fran snapshot
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier myapp-db-restored \
    --db-snapshot-identifier myapp-db-snapshot-20251202
```

---

## Pro Tips

> **Tip 1:** ALDRIG gör RDS publicly accessible i produktion. Alltid i private subnet.

> **Tip 2:** Anvand Parameter Groups for att tuna database settings.

> **Tip 3:** Aktivera Performance Insights (gratis 7 dagars retention) for query-analys.

> **Tip 4:** Anvand IAM database authentication for extra sakerhet.

---

## Hands-on Task

### Uppgift: Deploya PostgreSQL med High Availability

1. **Skapa DB subnet group**
2. **Skapa RDS PostgreSQL** (db.t3.micro)
3. **Aktivera Multi-AZ**
4. **Skapa en read replica**
5. **Ta en manual snapshot**

**Verification:**
```bash
aws rds describe-db-instances --query 'DBInstances[].{ID:DBInstanceIdentifier,MultiAZ:MultiAZ,Status:DBInstanceStatus}'
```

''',
    "task": {
        "title": "RDS High Availability Setup",
        "description": "Deploya PostgreSQL med Multi-AZ och read replica",
        "xp_reward": 75,
        "estimated_minutes": 45,
        "deliverables": [
            "RDS PostgreSQL i private subnet",
            "Multi-AZ aktiverat",
            "Read replica skapad",
            "Manual snapshot tagen"
        ]
    }
}


# =============================================================================
# NODE 7: Route53 - DNS Service
# =============================================================================

NODE_07_ROUTE53 = {
    "node_id": 7,
    "title": "Route53 - DNS Service",
    "slug": "aws-route53",
    "difficulty": "intermediate",
    "estimated_minutes": 45,
    "xp_reward": 65,
    "topics_covered": [
        "hosted zones", "record types", "routing policies",
        "health checks", "domain registration", "DNS resolution"
    ],
    "content": r'''# Route53 - DNS Service

## Varfor Route53?

> "Route53 ar mer an DNS - det ar global traffic management. Health checks, failover, geo-routing, latency-based routing."

Namn kommer fran TCP/UDP port 53 (DNS) + Route 66 (highway).

---

## DNS Basics

### DNS Resolution

```
┌─────────────────────────────────────────────────────────────┐
│                    DNS RESOLUTION                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   User types: www.example.com                               │
│                     │                                        │
│                     ▼                                        │
│   ┌─────────────────────────────────┐                       │
│   │      Recursive Resolver         │                       │
│   │   (ISP or 8.8.8.8)              │                       │
│   └─────────────────────────────────┘                       │
│                     │                                        │
│         ┌───────────┴───────────┐                           │
│         ▼                       ▼                           │
│   ┌──────────┐           ┌──────────┐                       │
│   │   Root   │           │   TLD    │                       │
│   │  Server  │    →      │ (.com)   │                       │
│   └──────────┘           └──────────┘                       │
│                                │                             │
│                                ▼                             │
│                         ┌──────────────┐                    │
│                         │   Route53    │                    │
│                         │  (Authorit.) │                    │
│                         └──────────────┘                    │
│                                │                             │
│                                ▼                             │
│                         52.xx.xx.xx (IP)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Record Types

| Type | Syfte | Exempel |
|------|-------|---------|
| **A** | Name → IPv4 | www → 52.1.2.3 |
| **AAAA** | Name → IPv6 | www → 2001:db8::1 |
| **CNAME** | Name → Name | www → app.example.com |
| **ALIAS** | Name → AWS resource | www → d123.cloudfront.net |
| **MX** | Mail servers | @ → mail.example.com |
| **TXT** | Text records | Verification, SPF |
| **NS** | Name servers | Delegation |

### A vs CNAME vs ALIAS

```
A RECORD:
www.example.com → 52.1.2.3
(Direkt till IP)

CNAME:
www.example.com → app.example.com
(Pointer till annat namn - INTE pa apex/root!)

ALIAS (AWS-specifik):
example.com → d123.cloudfront.net
(Fungerar pa apex, gratis queries till AWS resources)
```

---

## Skapa Hosted Zone

```bash
# Skapa public hosted zone
ZONE_ID=$(aws route53 create-hosted-zone \
    --name example.com \
    --caller-reference $(date +%s) \
    --query 'HostedZone.Id' \
    --output text | cut -d'/' -f3)

echo "Hosted Zone ID: $ZONE_ID"

# Lista name servers (uppdatera hos din registrar)
aws route53 get-hosted-zone \
    --id $ZONE_ID \
    --query 'DelegationSet.NameServers'
```

### Skapa Records

```bash
# Skapa A record
aws route53 change-resource-record-sets \
    --hosted-zone-id $ZONE_ID \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "www.example.com",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [{"Value": "52.1.2.3"}]
            }
        }]
    }'

# Skapa ALIAS till ALB
aws route53 change-resource-record-sets \
    --hosted-zone-id $ZONE_ID \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "api.example.com",
                "Type": "A",
                "AliasTarget": {
                    "HostedZoneId": "Z2FDTNDATAQYW2",
                    "DNSName": "my-alb-123456.eu-north-1.elb.amazonaws.com",
                    "EvaluateTargetHealth": true
                }
            }
        }]
    }'
```

---

## Routing Policies

### Simple vs Weighted vs Latency

```
SIMPLE (default):
User → DNS → Single endpoint

WEIGHTED (A/B testing, gradual rollout):
User → DNS → 70% old version
           → 30% new version

LATENCY (lowest latency):
User (EU) → DNS → eu-north-1 endpoint
User (US) → DNS → us-east-1 endpoint

FAILOVER (disaster recovery):
User → DNS → Primary (healthy) ✓
           → Secondary (standby)

GEOLOCATION (based on location):
User (Sweden) → DNS → Swedish content
User (Germany) → DNS → German content
```

### Weighted Routing Exempel

```bash
# 80% traffic till old version
aws route53 change-resource-record-sets \
    --hosted-zone-id $ZONE_ID \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "app.example.com",
                "Type": "A",
                "SetIdentifier": "old-version",
                "Weight": 80,
                "TTL": 60,
                "ResourceRecords": [{"Value": "52.1.1.1"}]
            }
        }]
    }'

# 20% traffic till new version
aws route53 change-resource-record-sets \
    --hosted-zone-id $ZONE_ID \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "app.example.com",
                "Type": "A",
                "SetIdentifier": "new-version",
                "Weight": 20,
                "TTL": 60,
                "ResourceRecords": [{"Value": "52.2.2.2"}]
            }
        }]
    }'
```

---

## Health Checks

```bash
# Skapa health check
HEALTH_CHECK_ID=$(aws route53 create-health-check \
    --caller-reference $(date +%s) \
    --health-check-config '{
        "IPAddress": "52.1.2.3",
        "Port": 80,
        "Type": "HTTP",
        "ResourcePath": "/health",
        "RequestInterval": 30,
        "FailureThreshold": 3
    }' \
    --query 'HealthCheck.Id' \
    --output text)

# Anvand med failover routing
# Primary pekar till health-checked endpoint
# Secondary tar over vid failure
```

---

## Pro Tips

> **Tip 1:** Anvand ALIAS istallet for CNAME for AWS resources - snabbare och gratis.

> **Tip 2:** Satt laga TTL (60s) under migrations, hoja sedan (300-3600s).

> **Tip 3:** Route53 health checks kan trigga CloudWatch alarms och SNS notifications.

---

## Hands-on Task

### Uppgift: Konfigurera DNS for en Web App

1. **Skapa hosted zone** for din doman
2. **Skapa A record** for www
3. **Skapa health check** for endpointen
4. **Konfigurera weighted routing** (om du har tva endpoints)

**Verification:**
```bash
dig www.example.com
nslookup www.example.com
```

''',
    "task": {
        "title": "Route53 DNS Setup",
        "description": "Konfigurera DNS med health checks och routing",
        "xp_reward": 65,
        "estimated_minutes": 30,
        "deliverables": [
            "Hosted zone skapad",
            "A/ALIAS records",
            "Health check konfigurerad"
        ]
    }
}


# =============================================================================
# NODE 8: CloudWatch - Monitoring & Logging
# =============================================================================

NODE_08_CLOUDWATCH = {
    "node_id": 8,
    "title": "CloudWatch - Monitoring & Logging",
    "slug": "aws-cloudwatch",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 70,
    "topics_covered": [
        "metrics", "alarms", "logs", "log groups", "log insights",
        "dashboards", "events", "custom metrics"
    ],
    "content": r'''# CloudWatch - Monitoring & Logging

## Varfor CloudWatch ar Essential

> "Du kan inte fixa det du inte kan se. CloudWatch ar dina ogon och oron i AWS."

CloudWatch ar centralen for all monitoring, logging och alerting i AWS.

---

## CloudWatch Components

```
┌─────────────────────────────────────────────────────────────┐
│                    CLOUDWATCH                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   METRICS              LOGS                ALARMS           │
│   ┌──────────┐        ┌──────────┐        ┌──────────┐     │
│   │ CPU %    │        │ App logs │        │ CPU > 80%│     │
│   │ Memory   │        │ Access   │        │ Errors   │     │
│   │ Network  │        │ System   │        │ Latency  │     │
│   └──────────┘        └──────────┘        └──────────┘     │
│        │                   │                   │            │
│        └───────────────────┴───────────────────┘            │
│                            │                                 │
│                            ▼                                 │
│                    ┌──────────────┐                         │
│                    │  DASHBOARDS  │                         │
│                    │  (Visualize) │                         │
│                    └──────────────┘                         │
│                            │                                 │
│                            ▼                                 │
│                    ┌──────────────┐                         │
│                    │    ACTIONS   │                         │
│                    │ SNS, Lambda  │                         │
│                    │ Auto Scaling │                         │
│                    └──────────────┘                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## CloudWatch Metrics

### Hamta Metrics

```bash
# Lista metrics for EC2
aws cloudwatch list-metrics \
    --namespace AWS/EC2 \
    --dimensions Name=InstanceId,Value=$INSTANCE_ID

# Hamta CPU utilization
aws cloudwatch get-metric-statistics \
    --namespace AWS/EC2 \
    --metric-name CPUUtilization \
    --dimensions Name=InstanceId,Value=$INSTANCE_ID \
    --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ) \
    --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) \
    --period 300 \
    --statistics Average Maximum
```

### Vanliga Metrics

| Service | Metric | Beskrivning |
|---------|--------|-------------|
| EC2 | CPUUtilization | CPU % |
| EC2 | NetworkIn/Out | Bytes |
| RDS | DatabaseConnections | Connections |
| RDS | FreeStorageSpace | Bytes |
| ALB | RequestCount | Requests |
| ALB | TargetResponseTime | Latency |
| Lambda | Invocations | Calls |
| Lambda | Errors | Error count |

### Custom Metrics

```bash
# Publicera custom metric
aws cloudwatch put-metric-data \
    --namespace "MyApp" \
    --metric-name "ActiveUsers" \
    --value 42 \
    --unit Count \
    --dimensions Environment=prod,Service=api

# Med timestamp
aws cloudwatch put-metric-data \
    --namespace "MyApp" \
    --metric-data '[
        {
            "MetricName": "RequestLatency",
            "Value": 125.5,
            "Unit": "Milliseconds",
            "Timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
        }
    ]'
```

---

## CloudWatch Alarms

### Skapa Alarm

```bash
# CPU alarm - notify via SNS
aws cloudwatch put-metric-alarm \
    --alarm-name "HighCPU-WebServer" \
    --alarm-description "CPU over 80% for 5 minutes" \
    --metric-name CPUUtilization \
    --namespace AWS/EC2 \
    --statistic Average \
    --period 300 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 2 \
    --dimensions Name=InstanceId,Value=$INSTANCE_ID \
    --alarm-actions arn:aws:sns:eu-north-1:123456789012:alerts \
    --ok-actions arn:aws:sns:eu-north-1:123456789012:alerts

# Lista alarms
aws cloudwatch describe-alarms \
    --alarm-names "HighCPU-WebServer"
```

### Alarm States

```
┌─────────────────────────────────────────────────────────────┐
│                    ALARM STATES                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   OK              ALARM           INSUFFICIENT_DATA         │
│   ┌─────┐         ┌─────┐         ┌─────┐                  │
│   │ ✓   │    →    │ ⚠️  │    →    │ ?   │                  │
│   │     │         │     │         │     │                  │
│   └─────┘         └─────┘         └─────┘                  │
│   Threshold       Threshold       Not enough               │
│   not breached    breached        data points              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## CloudWatch Logs

### Log Groups & Streams

```bash
# Skapa log group
aws logs create-log-group \
    --log-group-name /myapp/production

# Skapa log stream
aws logs create-log-stream \
    --log-group-name /myapp/production \
    --log-stream-name webserver-001

# Skicka logs
aws logs put-log-events \
    --log-group-name /myapp/production \
    --log-stream-name webserver-001 \
    --log-events \
    timestamp=$(date +%s000),message="Application started" \
    timestamp=$(date +%s000),message="Listening on port 8080"
```

### CloudWatch Agent (for EC2)

```bash
# Installera agent pa EC2
sudo yum install amazon-cloudwatch-agent -y

# Konfigurera
cat > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json << 'EOF'
{
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/var/log/myapp/*.log",
                        "log_group_name": "/myapp/production",
                        "log_stream_name": "{instance_id}"
                    }
                ]
            }
        }
    },
    "metrics": {
        "metrics_collected": {
            "mem": {
                "measurement": ["mem_used_percent"]
            },
            "disk": {
                "measurement": ["used_percent"],
                "resources": ["/"]
            }
        }
    }
}
EOF

# Starta agent
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a fetch-config \
    -m ec2 \
    -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
    -s
```

---

## CloudWatch Logs Insights

### Query Logs

```sql
-- Hitta errors senaste 24h
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100

-- Aggregera requests per minut
fields @timestamp, @message
| stats count() by bin(1m)

-- Top 10 IP-adresser
fields @timestamp, clientIP
| stats count(*) as requests by clientIP
| sort requests desc
| limit 10
```

```bash
# Kor query via CLI
aws logs start-query \
    --log-group-name /myapp/production \
    --start-time $(date -d '1 hour ago' +%s) \
    --end-time $(date +%s) \
    --query-string 'fields @timestamp, @message | filter @message like /ERROR/'
```

---

## Pro Tips

> **Tip 1:** Satt retention policy pa log groups - default ar FOREVER (dyrt!).

> **Tip 2:** Anvand metric filters for att skapa metrics fran logs.

> **Tip 3:** Anomaly detection alarms ar smartare an statiska thresholds.

> **Tip 4:** Export logs till S3 for lang-tids lagring (billigare).

---

## Hands-on Task

### Uppgift: Komplett Monitoring Setup

1. **Installera CloudWatch Agent** pa EC2
2. **Konfigurera log collection** for app logs
3. **Skapa CPU alarm** med SNS notification
4. **Skapa Dashboard** med viktiga metrics
5. **Skriv Logs Insights query** for errors

**Verification:**
```bash
aws cloudwatch describe-alarms --state-value ALARM
aws logs describe-log-groups --query 'logGroups[].logGroupName'
```

''',
    "task": {
        "title": "CloudWatch Monitoring Setup",
        "description": "Implementera komplett monitoring med metrics, logs och alarms",
        "xp_reward": 70,
        "estimated_minutes": 45,
        "deliverables": [
            "CloudWatch Agent installerad",
            "Log groups konfigurerade",
            "CPU alarm skapad",
            "Dashboard med metrics"
        ]
    }
}


# =============================================================================
# AGGREGATE ALL NODES (Block 1-2: 1-8)
# =============================================================================

AWS_SKILLSMAP_NODES_BLOCK_2 = [
    NODE_05_S3,
    NODE_06_RDS,
    NODE_07_ROUTE53,
    NODE_08_CLOUDWATCH,
]

# =============================================================================
# BLOCK 3: Compute & Infrastructure (Lambda, CloudFormation, CloudFront, ELB)
# =============================================================================

AWS_SKILLSMAP_NODES_BLOCK_3 = [
    {
        "id": "aws-9",
        "title": "AWS Lambda",
        "description": "Serverless compute - kör kod utan servrar",
        "content": """
# 🎯 Hook
Vad om du kunde köra kod utan att tänka på servrar överhuvudtaget?

AWS Lambda är **serverless computing** - du betalar bara för exekveringstiden!

---

## 📚 Koncept

### Vad är Lambda?
- **Function-as-a-Service (FaaS)** - kör funktioner on-demand
- **Event-driven** - triggas av händelser
- **Auto-scaling** - från 0 till tusentals parallella körningar
- **Pay-per-use** - betala per millisekund

### Lambda Execution Model:
```
Event → Lambda Function → Response
  ↓
- API Gateway request
- S3 upload
- DynamoDB change
- CloudWatch Event
- SQS message
```

### Anatomy of a Lambda Function:
```python
def lambda_handler(event, context):
    # event - input data
    # context - runtime info

    name = event.get('name', 'World')

    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
```

---

## 💻 Kommandon (AWS CLI)

```bash
# Skapa deployment package
zip function.zip lambda_function.py

# Skapa Lambda function
aws lambda create-function \\
    --function-name hello-world \\
    --runtime python3.11 \\
    --role arn:aws:iam::ACCOUNT:role/lambda-role \\
    --handler lambda_function.lambda_handler \\
    --zip-file fileb://function.zip

# Testa function
aws lambda invoke \\
    --function-name hello-world \\
    --payload '{"name": "DevOps"}' \\
    response.json

# Lista functions
aws lambda list-functions

# Uppdatera kod
aws lambda update-function-code \\
    --function-name hello-world \\
    --zip-file fileb://function.zip

# Konfigurera environment variables
aws lambda update-function-configuration \\
    --function-name hello-world \\
    --environment Variables={DB_HOST=mydb.com}

# Lägg till trigger (S3)
aws lambda add-permission \\
    --function-name processImage \\
    --statement-id s3-trigger \\
    --action lambda:InvokeFunction \\
    --principal s3.amazonaws.com \\
    --source-arn arn:aws:s3:::my-bucket
```

---

## 🔥 Pro Tips

1. **Cold Starts** - Håll functions varma med provisioned concurrency
2. **Timeout** - Default 3s, max 15min - välj rätt!
3. **Memory = CPU** - Mer minne = snabbare CPU
4. **Layers** - Dela dependencies mellan functions
5. **X-Ray** - Tracing för debugging

---

## 🎯 Hands-on Task

Skapa en "URL Shortener" Lambda:

```python
# url_shortener.py
import json
import boto3
import hashlib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-mappings')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        long_url = body['url']

        # Generate short code
        short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]

        # Store mapping
        table.put_item(Item={
            'short_code': short_code,
            'long_url': long_url
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'short_url': f'https://short.ly/{short_code}'})
        }

    elif event['httpMethod'] == 'GET':
        short_code = event['pathParameters']['code']

        response = table.get_item(Key={'short_code': short_code})

        if 'Item' in response:
            return {
                'statusCode': 301,
                'headers': {'Location': response['Item']['long_url']}
            }

        return {'statusCode': 404, 'body': 'Not found'}
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/lambda/"},
            {"type": "workshop", "url": "https://serverlessland.com/"}
        ],
        "prerequisites": ["aws-4"],
        "learning_outcomes": [
            "Skapa och deploya Lambda functions",
            "Konfigurera triggers och permissions",
            "Förstå cold starts och optimering"
        ],
        "estimated_time": "90 min",
        "difficulty": "intermediate",
        "category": "compute",
        "order": 9
    },
    {
        "id": "aws-10",
        "title": "CloudFormation",
        "description": "Infrastructure as Code - definiera AWS i YAML/JSON",
        "content": """
# 🎯 Hook
Klicka-och-skapa i AWS Console? Det är för amatörer!

**CloudFormation** = Infrastructure as Code för AWS. Versionera, återskapa, automatisera!

---

## 📚 Koncept

### Vad är CloudFormation?
- **Deklarativ IaC** - beskriv VAD, inte HUR
- **Stacks** - samling av resurser som hanteras tillsammans
- **Templates** - YAML/JSON-filer som beskriver infrastruktur
- **Drift Detection** - upptäck manuella ändringar

### CloudFormation Stack Lifecycle:
```
Template → Create Stack → Resources Provisioned
                ↓
         Update Stack → Rolling updates
                ↓
         Delete Stack → All resources removed
```

### Template Anatomy:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: My awesome stack

Parameters:          # Input values
  EnvironmentType:
    Type: String
    Default: dev

Mappings:           # Static key-value lookups
  RegionMap:
    eu-north-1:
      AMI: ami-12345

Conditions:         # Conditional resource creation
  IsProd: !Equals [!Ref EnvironmentType, prod]

Resources:          # AWS resources (required!)
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro

Outputs:           # Return values
  InstanceId:
    Value: !Ref MyEC2Instance
```

---

## 💻 Kommandon

```bash
# Validera template
aws cloudformation validate-template \\
    --template-body file://template.yaml

# Skapa stack
aws cloudformation create-stack \\
    --stack-name my-app \\
    --template-body file://template.yaml \\
    --parameters ParameterKey=Env,ParameterValue=prod \\
    --capabilities CAPABILITY_IAM

# Vänta på completion
aws cloudformation wait stack-create-complete \\
    --stack-name my-app

# Lista stacks
aws cloudformation list-stacks \\
    --stack-status-filter CREATE_COMPLETE

# Describe stack
aws cloudformation describe-stacks \\
    --stack-name my-app

# Uppdatera stack
aws cloudformation update-stack \\
    --stack-name my-app \\
    --template-body file://template-v2.yaml

# Change sets (preview changes)
aws cloudformation create-change-set \\
    --stack-name my-app \\
    --change-set-name my-changes \\
    --template-body file://template-v2.yaml

# Execute change set
aws cloudformation execute-change-set \\
    --stack-name my-app \\
    --change-set-name my-changes

# Delete stack
aws cloudformation delete-stack \\
    --stack-name my-app
```

---

## 🔥 Pro Tips

1. **Change Sets** - Alltid preview innan update i prod!
2. **Stack Policies** - Skydda kritiska resurser från deletion
3. **Nested Stacks** - Bryt ner stora templates
4. **Cross-Stack References** - Dela outputs mellan stacks
5. **SAM** - Serverless Application Model för Lambda-fokuserat

---

## 🎯 Hands-on Task

Skapa en komplett web stack:

```yaml
# web-stack.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Web application stack

Parameters:
  EnvironmentName:
    Type: String
    Default: dev
    AllowedValues: [dev, staging, prod]

Resources:
  # VPC
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-vpc

  # Public Subnet
  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-public

  # Internet Gateway
  InternetGateway:
    Type: AWS::EC2::InternetGateway

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  # Security Group
  WebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP/HTTPS
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0

  # EC2 Instance
  WebServer:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: !Sub '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
      SubnetId: !Ref PublicSubnet
      SecurityGroupIds:
        - !Ref WebSecurityGroup
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-webserver

Outputs:
  WebServerIP:
    Description: Public IP of web server
    Value: !GetAtt WebServer.PublicIp
    Export:
      Name: !Sub ${EnvironmentName}-WebServerIP
```

Kör: `aws cloudformation create-stack --stack-name web-app --template-body file://web-stack.yaml`
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/cloudformation/"},
            {"type": "reference", "url": "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"}
        ],
        "prerequisites": ["aws-3"],
        "learning_outcomes": [
            "Skriva CloudFormation templates",
            "Hantera stacks med CLI",
            "Använda Parameters, Mappings, Outputs"
        ],
        "estimated_time": "120 min",
        "difficulty": "intermediate",
        "category": "devops",
        "order": 10
    },
    {
        "id": "aws-11",
        "title": "CloudFront",
        "description": "Global CDN - snabba upp content delivery världen över",
        "content": """
# 🎯 Hook
Din webbsida laddar på 3 sekunder? Det är en EVIGHET på internet!

**CloudFront** = AWS CDN. Cacha content nära användarna, ladda på millisekunder.

---

## 📚 Koncept

### Vad är CloudFront?
- **CDN (Content Delivery Network)** - distribuerar content globalt
- **Edge Locations** - 450+ PoPs världen över
- **Caching** - minska load på origin
- **Security** - DDoS-skydd, SSL/TLS, WAF-integration

### CloudFront Architecture:
```
User → Edge Location → Regional Cache → Origin
         ↓
    Cache HIT? → Return cached content
         ↓
    Cache MISS → Fetch from origin → Cache → Return
```

### Origin Types:
- **S3 Bucket** - static websites, assets
- **EC2/ALB** - dynamic applications
- **Custom Origin** - any HTTP server
- **MediaStore** - video streaming

### Cache Behaviors:
```
/api/*     → ALB (no cache, TTL 0)
/static/*  → S3 (cache 1 year)
/images/*  → S3 (cache 1 week)
/*         → ALB (cache 5 min)
```

---

## 💻 Kommandon

```bash
# Skapa distribution (via JSON config)
aws cloudfront create-distribution \\
    --distribution-config file://cf-config.json

# Lista distributions
aws cloudfront list-distributions

# Hämta distribution info
aws cloudfront get-distribution \\
    --id E1234567890ABC

# Invalidera cache
aws cloudfront create-invalidation \\
    --distribution-id E1234567890ABC \\
    --paths "/*"

# Invalidera specifika filer
aws cloudfront create-invalidation \\
    --distribution-id E1234567890ABC \\
    --paths "/index.html" "/css/*"

# Lista invalidations
aws cloudfront list-invalidations \\
    --distribution-id E1234567890ABC

# Disable distribution (före deletion)
aws cloudfront get-distribution-config --id E123 > config.json
# Edit: Enabled: false
aws cloudfront update-distribution \\
    --id E123 \\
    --distribution-config file://config.json \\
    --if-match ETAG123
```

---

## 🔥 Pro Tips

1. **Cache-Control headers** - Kontrollera TTL från origin
2. **Invalidation costs** - Första 1000 paths/månad gratis, sen $0.005/path
3. **Compression** - Aktivera Gzip/Brotli automatiskt
4. **Lambda@Edge** - Kör kod vid edge locations
5. **Origin Shield** - Extra caching layer för burst traffic

---

## 🎯 Hands-on Task

Sätt upp CloudFront för S3 static site:

```json
// cf-s3-config.json
{
  "CallerReference": "my-static-site-2024",
  "Origins": {
    "Quantity": 1,
    "Items": [
      {
        "Id": "S3-my-bucket",
        "DomainName": "my-bucket.s3.eu-north-1.amazonaws.com",
        "S3OriginConfig": {
          "OriginAccessIdentity": ""
        }
      }
    ]
  },
  "DefaultCacheBehavior": {
    "TargetOriginId": "S3-my-bucket",
    "ViewerProtocolPolicy": "redirect-to-https",
    "AllowedMethods": {
      "Quantity": 2,
      "Items": ["GET", "HEAD"]
    },
    "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
    "Compress": true
  },
  "DefaultRootObject": "index.html",
  "Enabled": true,
  "Comment": "Static website CDN"
}
```

Test med curl:
```bash
curl -I https://d1234567890.cloudfront.net/
# Check headers: X-Cache: Hit from cloudfront
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/cloudfront/"},
            {"type": "pricing", "url": "https://aws.amazon.com/cloudfront/pricing/"}
        ],
        "prerequisites": ["aws-5"],
        "learning_outcomes": [
            "Konfigurera CloudFront distributions",
            "Optimera caching strategier",
            "Hantera cache invalidation"
        ],
        "estimated_time": "60 min",
        "difficulty": "intermediate",
        "category": "networking",
        "order": 11
    },
    {
        "id": "aws-12",
        "title": "Elastic Load Balancing",
        "description": "Lastbalansering - distribuera trafik över flera targets",
        "content": """
# 🎯 Hook
En server down = site down? Nej tack!

**Elastic Load Balancing** = Automatisk lastbalansering och high availability.

---

## 📚 Koncept

### ELB-typer:

| Type | Layer | Use Case |
|------|-------|----------|
| **ALB** | Layer 7 (HTTP/S) | Web apps, microservices |
| **NLB** | Layer 4 (TCP/UDP) | High performance, gaming |
| **GLB** | Layer 3 (IP) | Third-party appliances |
| **CLB** | Layer 4/7 | Legacy (avoid) |

### ALB Architecture:
```
Internet → ALB → Target Group 1 (EC2 instances)
              → Target Group 2 (Lambda functions)
              → Target Group 3 (IP addresses)
```

### Key Components:
- **Listeners** - port + protocol (80/HTTP, 443/HTTPS)
- **Rules** - routing logic (path, host, headers)
- **Target Groups** - backend servers
- **Health Checks** - verify targets are healthy

### Routing Examples:
```
api.example.com/*     → API Target Group
www.example.com/*     → Web Target Group
example.com/images/*  → S3 (via Lambda)
```

---

## 💻 Kommandon

```bash
# Skapa Application Load Balancer
aws elbv2 create-load-balancer \\
    --name my-alb \\
    --subnets subnet-111 subnet-222 \\
    --security-groups sg-123456 \\
    --type application

# Skapa Target Group
aws elbv2 create-target-group \\
    --name my-targets \\
    --protocol HTTP \\
    --port 80 \\
    --vpc-id vpc-123456 \\
    --health-check-path /health \\
    --health-check-interval-seconds 30

# Registrera targets
aws elbv2 register-targets \\
    --target-group-arn arn:aws:... \\
    --targets Id=i-111111 Id=i-222222

# Skapa Listener
aws elbv2 create-listener \\
    --load-balancer-arn arn:aws:... \\
    --protocol HTTP \\
    --port 80 \\
    --default-actions Type=forward,TargetGroupArn=arn:aws:...

# HTTPS Listener med certifikat
aws elbv2 create-listener \\
    --load-balancer-arn arn:aws:... \\
    --protocol HTTPS \\
    --port 443 \\
    --certificates CertificateArn=arn:aws:acm:... \\
    --default-actions Type=forward,TargetGroupArn=arn:aws:...

# Lägg till routing rule
aws elbv2 create-rule \\
    --listener-arn arn:aws:... \\
    --priority 10 \\
    --conditions Field=path-pattern,Values='/api/*' \\
    --actions Type=forward,TargetGroupArn=arn:aws:api-targets

# Describe load balancer
aws elbv2 describe-load-balancers --names my-alb

# Describe target health
aws elbv2 describe-target-health \\
    --target-group-arn arn:aws:...
```

---

## 🔥 Pro Tips

1. **Cross-zone** - Aktivera för jämn distribution
2. **Connection Draining** - Vänta på aktiva requests vid deregistration
3. **Sticky Sessions** - Använd för stateful apps (men undvik om möjligt)
4. **Access Logs** - Logga till S3 för analys
5. **WAF** - Integrera för web application firewall

---

## 🎯 Hands-on Task

Sätt upp ALB med path-based routing:

```bash
# 1. Skapa ALB
ALB_ARN=$(aws elbv2 create-load-balancer \\
    --name demo-alb \\
    --subnets subnet-1 subnet-2 \\
    --security-groups sg-web \\
    --query 'LoadBalancers[0].LoadBalancerArn' \\
    --output text)

# 2. Skapa Target Groups
API_TG=$(aws elbv2 create-target-group \\
    --name api-targets \\
    --protocol HTTP --port 8080 \\
    --vpc-id vpc-123 \\
    --query 'TargetGroups[0].TargetGroupArn' \\
    --output text)

WEB_TG=$(aws elbv2 create-target-group \\
    --name web-targets \\
    --protocol HTTP --port 80 \\
    --vpc-id vpc-123 \\
    --query 'TargetGroups[0].TargetGroupArn' \\
    --output text)

# 3. Skapa Listener med default action
LISTENER_ARN=$(aws elbv2 create-listener \\
    --load-balancer-arn $ALB_ARN \\
    --protocol HTTP --port 80 \\
    --default-actions Type=forward,TargetGroupArn=$WEB_TG \\
    --query 'Listeners[0].ListenerArn' \\
    --output text)

# 4. Lägg till /api/* rule
aws elbv2 create-rule \\
    --listener-arn $LISTENER_ARN \\
    --priority 10 \\
    --conditions Field=path-pattern,Values='/api/*' \\
    --actions Type=forward,TargetGroupArn=$API_TG

# Test
curl http://$(aws elbv2 describe-load-balancers --names demo-alb --query 'LoadBalancers[0].DNSName' --output text)/
curl http://ALB-DNS/api/health
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/elasticloadbalancing/"},
            {"type": "comparison", "url": "https://aws.amazon.com/elasticloadbalancing/features/"}
        ],
        "prerequisites": ["aws-3", "aws-4"],
        "learning_outcomes": [
            "Välja rätt ELB-typ för use case",
            "Konfigurera ALB med path-based routing",
            "Sätta upp health checks och target groups"
        ],
        "estimated_time": "90 min",
        "difficulty": "intermediate",
        "category": "networking",
        "order": 12
    }
]

# =============================================================================
# BLOCK 4: Advanced Services (DynamoDB, SNS/SQS, Secrets Manager, ECS)
# =============================================================================

AWS_SKILLSMAP_NODES_BLOCK_4 = [
    {
        "id": "aws-13",
        "title": "DynamoDB",
        "description": "NoSQL-databas - millisekund-latens i vilken skala som helst",
        "content": """
# 🎯 Hook
Behöver du en databas som skalar från 0 till miljoner requests/sekund?

**DynamoDB** = Fullt managed NoSQL. Single-digit millisecond latency. Oändlig skalbarhet.

---

## 📚 Koncept

### Vad är DynamoDB?
- **Key-Value & Document DB** - flexibel datamodell
- **Serverless** - ingen server att hantera
- **Auto-scaling** - on-demand eller provisioned capacity
- **Global Tables** - multi-region replication

### Data Model:
```
Table: users
├── Partition Key: user_id (required)
├── Sort Key: created_at (optional)
└── Attributes: name, email, settings (any JSON)

Primary Key = Partition Key + Sort Key (if exists)
```

### Capacity Modes:
| Mode | Use Case | Billing |
|------|----------|---------|
| **On-Demand** | Unpredictable traffic | Pay per request |
| **Provisioned** | Predictable traffic | RCU/WCU per second |

### Access Patterns:
```python
# Single item
GetItem(PK="user123")

# Query (PK + optional SK filter)
Query(PK="user123", SK begins_with "order#")

# Scan (full table - AVOID!)
Scan(FilterExpression="status = 'active'")
```

---

## 💻 Kommandon

```bash
# Skapa table
aws dynamodb create-table \\
    --table-name users \\
    --attribute-definitions \\
        AttributeName=user_id,AttributeType=S \\
    --key-schema \\
        AttributeName=user_id,KeyType=HASH \\
    --billing-mode PAY_PER_REQUEST

# Table med Sort Key
aws dynamodb create-table \\
    --table-name orders \\
    --attribute-definitions \\
        AttributeName=user_id,AttributeType=S \\
        AttributeName=order_id,AttributeType=S \\
    --key-schema \\
        AttributeName=user_id,KeyType=HASH \\
        AttributeName=order_id,KeyType=RANGE \\
    --billing-mode PAY_PER_REQUEST

# Put item
aws dynamodb put-item \\
    --table-name users \\
    --item '{
        "user_id": {"S": "u123"},
        "name": {"S": "Alice"},
        "email": {"S": "alice@example.com"}
    }'

# Get item
aws dynamodb get-item \\
    --table-name users \\
    --key '{"user_id": {"S": "u123"}}'

# Query
aws dynamodb query \\
    --table-name orders \\
    --key-condition-expression "user_id = :uid" \\
    --expression-attribute-values '{":uid": {"S": "u123"}}'

# Update item
aws dynamodb update-item \\
    --table-name users \\
    --key '{"user_id": {"S": "u123"}}' \\
    --update-expression "SET email = :e" \\
    --expression-attribute-values '{":e": {"S": "new@email.com"}}'

# Delete item
aws dynamodb delete-item \\
    --table-name users \\
    --key '{"user_id": {"S": "u123"}}'

# Describe table
aws dynamodb describe-table --table-name users
```

---

## 🔥 Pro Tips

1. **Design for access patterns** - Tänk query first, schema second
2. **Avoid Scans** - Designa keys så du kan Query istället
3. **GSI/LSI** - Global/Local Secondary Indexes för alternativa queries
4. **TTL** - Auto-delete items efter viss tid
5. **Streams** - Reagera på ändringar i realtid

---

## 🎯 Hands-on Task

Bygg ett leaderboard med DynamoDB:

```python
# leaderboard.py
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('game-leaderboard')

def add_score(game_id: str, player_id: str, score: int):
    table.put_item(Item={
        'game_id': game_id,
        'player_score': f'{score:010d}#{player_id}',  # Zero-pad for sorting
        'player_id': player_id,
        'score': score
    })

def get_top_10(game_id: str):
    response = table.query(
        KeyConditionExpression='game_id = :gid',
        ExpressionAttributeValues={':gid': game_id},
        ScanIndexForward=False,  # Descending order
        Limit=10
    )
    return response['Items']

# Usage
add_score('tetris', 'player1', 15000)
add_score('tetris', 'player2', 12000)
top = get_top_10('tetris')
```

Table schema:
```bash
aws dynamodb create-table \\
    --table-name game-leaderboard \\
    --attribute-definitions \\
        AttributeName=game_id,AttributeType=S \\
        AttributeName=player_score,AttributeType=S \\
    --key-schema \\
        AttributeName=game_id,KeyType=HASH \\
        AttributeName=player_score,KeyType=RANGE \\
    --billing-mode PAY_PER_REQUEST
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/dynamodb/"},
            {"type": "best-practices", "url": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html"}
        ],
        "prerequisites": ["aws-6"],
        "learning_outcomes": [
            "Designa DynamoDB tables för access patterns",
            "CRUD-operationer med CLI och SDK",
            "Förstå partition keys och sort keys"
        ],
        "estimated_time": "90 min",
        "difficulty": "intermediate",
        "category": "database",
        "order": 13
    },
    {
        "id": "aws-14",
        "title": "SNS & SQS",
        "description": "Messaging - pub/sub och message queues för decoupling",
        "content": """
# 🎯 Hook
Tight coupling mellan services? Det är en tidsbomd!

**SNS + SQS** = Messaging backbone. Decoupla allt, skala oberoende.

---

## 📚 Koncept

### SNS (Simple Notification Service):
- **Pub/Sub** - 1 publisher → many subscribers
- **Push-based** - meddelanden skickas direkt
- **Fan-out** - ett meddelande till många endpoints

### SQS (Simple Queue Service):
- **Message Queue** - 1 producer → 1 consumer (per message)
- **Pull-based** - consumers pollar för meddelanden
- **Buffering** - hantera traffic spikes

### SNS vs SQS:
```
SNS: Publisher → Topic → [Email, SMS, Lambda, SQS, HTTP]
     (Push to all subscribers immediately)

SQS: Producer → Queue → Consumer
     (Pull when ready, messages persist until processed)
```

### Common Pattern - Fan-out:
```
Order Service → SNS Topic "new-order"
                    ├→ SQS: inventory-queue → Inventory Service
                    ├→ SQS: shipping-queue → Shipping Service
                    ├→ SQS: notification-queue → Email Service
                    └→ Lambda: analytics → DynamoDB
```

---

## 💻 Kommandon

```bash
# === SNS ===

# Skapa topic
aws sns create-topic --name order-events

# Lista topics
aws sns list-topics

# Subscriptions
aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123:order-events \\
    --protocol email \\
    --notification-endpoint user@example.com

aws sns subscribe \\
    --topic-arn arn:aws:sns:... \\
    --protocol sqs \\
    --notification-endpoint arn:aws:sqs:...

# Publicera meddelande
aws sns publish \\
    --topic-arn arn:aws:sns:... \\
    --message '{"orderId": "123", "status": "created"}' \\
    --message-attributes '{"event":{"DataType":"String","StringValue":"order.created"}}'

# === SQS ===

# Skapa standard queue
aws sqs create-queue --queue-name orders-queue

# Skapa FIFO queue (guaranteed order)
aws sqs create-queue \\
    --queue-name orders-queue.fifo \\
    --attributes FifoQueue=true,ContentBasedDeduplication=true

# Get queue URL
aws sqs get-queue-url --queue-name orders-queue

# Skicka meddelande
aws sqs send-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123/orders-queue \\
    --message-body '{"orderId": "456"}'

# Ta emot meddelanden
aws sqs receive-message \\
    --queue-url https://sqs... \\
    --max-number-of-messages 10 \\
    --wait-time-seconds 20

# Radera meddelande (efter processing)
aws sqs delete-message \\
    --queue-url https://sqs... \\
    --receipt-handle "AQEBwJ..."

# Dead Letter Queue - mislyckade meddelanden
aws sqs create-queue --queue-name orders-dlq
aws sqs set-queue-attributes \\
    --queue-url https://sqs.../orders-queue \\
    --attributes '{
        "RedrivePolicy": "{\\\"deadLetterTargetArn\\\":\\\"arn:aws:sqs:...:orders-dlq\\\",\\\"maxReceiveCount\\\":\\\"3\\\"}"
    }'
```

---

## 🔥 Pro Tips

1. **Visibility Timeout** - Sätt längre än processing time
2. **Long Polling** - WaitTimeSeconds=20 för kostnadseffektivitet
3. **DLQ** - Alltid! Fånga misslyckade meddelanden
4. **FIFO** - När ordning spelar roll (men lägre throughput)
5. **Message Filtering** - Filtrera på SNS-nivå, inte i consumers

---

## 🎯 Hands-on Task

Bygg event-driven order system:

```python
# order_publisher.py
import boto3
import json

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:eu-north-1:123:order-events'

def publish_order_event(order_id: str, event_type: str, data: dict):
    message = {
        'order_id': order_id,
        'event_type': event_type,
        'data': data
    }

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=json.dumps(message),
        MessageAttributes={
            'event_type': {
                'DataType': 'String',
                'StringValue': event_type
            }
        }
    )

# order_consumer.py (Lambda or long-running service)
import boto3
import json

sqs = boto3.client('sqs')
QUEUE_URL = 'https://sqs.eu-north-1.amazonaws.com/123/orders-queue'

def process_orders():
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )

        for message in response.get('Messages', []):
            body = json.loads(message['Body'])
            order_data = json.loads(body['Message'])

            print(f"Processing order: {order_data['order_id']}")
            # ... process order ...

            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/sns/"},
            {"type": "docs", "url": "https://docs.aws.amazon.com/sqs/"}
        ],
        "prerequisites": ["aws-9"],
        "learning_outcomes": [
            "Förstå pub/sub vs queue patterns",
            "Konfigurera SNS topics och SQS queues",
            "Implementera fan-out och DLQ"
        ],
        "estimated_time": "90 min",
        "difficulty": "intermediate",
        "category": "integration",
        "order": 14
    },
    {
        "id": "aws-15",
        "title": "Secrets Manager",
        "description": "Secrets management - säker hantering av känslig data",
        "content": """
# 🎯 Hook
Hardcodade passwords i kod? 😱 Det är en säkerhetskatastrof!

**Secrets Manager** = Centraliserad, krypterad secrets-hantering med automatisk rotation.

---

## 📚 Koncept

### Vad är Secrets Manager?
- **Secure Storage** - AES-256 kryptering
- **Access Control** - IAM-baserad åtkomst
- **Automatic Rotation** - Rotera credentials automatiskt
- **Audit** - CloudTrail logging av all access

### Secret Types:
```
- Database credentials (RDS, Aurora, etc.)
- API keys
- OAuth tokens
- SSH keys
- Certificates
- Any key-value pairs
```

### Secrets Manager vs Parameter Store:
| Feature | Secrets Manager | Parameter Store |
|---------|-----------------|-----------------|
| Auto-rotation | ✅ Built-in | ❌ Manual |
| Cost | $0.40/secret/month | Free (standard) |
| Size limit | 64 KB | 8 KB (standard) |
| Cross-account | ✅ Easy | More complex |

---

## 💻 Kommandon

```bash
# Skapa secret
aws secretsmanager create-secret \\
    --name prod/myapp/database \\
    --description "Production database credentials" \\
    --secret-string '{"username":"admin","password":"supersecret123"}'

# Skapa från fil
aws secretsmanager create-secret \\
    --name prod/myapp/config \\
    --secret-string file://secrets.json

# Hämta secret value
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/database

# Hämta specifik version
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/database \\
    --version-stage AWSPREVIOUS

# Lista secrets
aws secretsmanager list-secrets

# Uppdatera secret
aws secretsmanager put-secret-value \\
    --secret-id prod/myapp/database \\
    --secret-string '{"username":"admin","password":"newpassword456"}'

# Konfigurera rotation (RDS)
aws secretsmanager rotate-secret \\
    --secret-id prod/myapp/database \\
    --rotation-lambda-arn arn:aws:lambda:...:rotation-function \\
    --rotation-rules AutomaticallyAfterDays=30

# Ta bort (med recovery window)
aws secretsmanager delete-secret \\
    --secret-id prod/myapp/database \\
    --recovery-window-in-days 7

# Restore deleted secret
aws secretsmanager restore-secret \\
    --secret-id prod/myapp/database
```

---

## 🔥 Pro Tips

1. **Naming convention** - `{env}/{app}/{type}` ex: `prod/api/database`
2. **Least privilege** - IAM policy per secret, inte wildcards
3. **Caching** - SDK cachar secrets, sätt lämplig TTL
4. **Tags** - Använd för cost allocation och access control
5. **Rotation** - Aktivera för alla prod secrets!

---

## 🎯 Hands-on Task

Integrera Secrets Manager i din app:

```python
# config.py
import boto3
import json
from functools import lru_cache

secrets_client = boto3.client('secretsmanager')

@lru_cache(maxsize=10)
def get_secret(secret_name: str) -> dict:
    \"\"\"Get secret from Secrets Manager with caching.\"\"\"
    response = secrets_client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# Usage in app
def get_database_connection():
    creds = get_secret('prod/myapp/database')

    return psycopg2.connect(
        host=creds['host'],
        port=creds['port'],
        database=creds['database'],
        user=creds['username'],
        password=creds['password']
    )

# IAM Policy for app
'''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:eu-north-1:123:secret:prod/myapp/*"
            ]
        }
    ]
}
'''
```

CLI test:
```bash
# Skapa test secret
aws secretsmanager create-secret \\
    --name test/demo/api-key \\
    --secret-string '{"api_key":"sk-test-12345"}'

# Verifiera
aws secretsmanager get-secret-value \\
    --secret-id test/demo/api-key \\
    --query SecretString --output text | jq
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/secretsmanager/"},
            {"type": "rotation", "url": "https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html"}
        ],
        "prerequisites": ["aws-2"],
        "learning_outcomes": [
            "Skapa och hantera secrets säkert",
            "Integrera secrets i applikationer",
            "Konfigurera automatisk rotation"
        ],
        "estimated_time": "45 min",
        "difficulty": "intermediate",
        "category": "security",
        "order": 15
    },
    {
        "id": "aws-16",
        "title": "ECS (Elastic Container Service)",
        "description": "Container orchestration - kör Docker containers i AWS",
        "content": """
# 🎯 Hook
Docker på din laptop är nice. Men hur kör du 100 containers i produktion?

**ECS** = AWS container orchestration. Kör Docker containers utan att hantera servrar.

---

## 📚 Koncept

### ECS Launch Types:

| Type | Description | Use Case |
|------|-------------|----------|
| **Fargate** | Serverless containers | Enklast, ingen EC2 |
| **EC2** | Self-managed instances | Mer kontroll, GPU |

### ECS Architecture:
```
Cluster
├── Service (long-running)
│   ├── Task Definition (blueprint)
│   │   └── Container Definitions
│   └── Tasks (running instances)
│       ├── Task 1 (container1, container2)
│       └── Task 2 (container1, container2)
└── Task (one-off job)
```

### Key Components:
- **Cluster** - logisk gruppering av resurser
- **Task Definition** - blueprint för containers (image, CPU, memory, ports)
- **Service** - maintains desired count of tasks
- **Task** - running instance av task definition

### Task Definition Example:
```json
{
  "family": "my-web-app",
  "cpu": "256",
  "memory": "512",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "web",
      "image": "nginx:latest",
      "portMappings": [{"containerPort": 80}],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/my-web-app"
        }
      }
    }
  ]
}
```

---

## 💻 Kommandon

```bash
# Skapa cluster
aws ecs create-cluster --cluster-name my-cluster

# Registrera task definition
aws ecs register-task-definition \\
    --cli-input-json file://task-definition.json

# Lista task definitions
aws ecs list-task-definitions

# Skapa service (Fargate)
aws ecs create-service \\
    --cluster my-cluster \\
    --service-name web-service \\
    --task-definition my-web-app:1 \\
    --desired-count 2 \\
    --launch-type FARGATE \\
    --network-configuration "awsvpcConfiguration={subnets=[subnet-123],securityGroups=[sg-456],assignPublicIp=ENABLED}"

# Uppdatera service (deploy new version)
aws ecs update-service \\
    --cluster my-cluster \\
    --service web-service \\
    --task-definition my-web-app:2 \\
    --force-new-deployment

# Scale service
aws ecs update-service \\
    --cluster my-cluster \\
    --service web-service \\
    --desired-count 5

# Lista services
aws ecs list-services --cluster my-cluster

# Lista tasks
aws ecs list-tasks --cluster my-cluster

# Describe task
aws ecs describe-tasks \\
    --cluster my-cluster \\
    --tasks arn:aws:ecs:...:task/abc123

# Run one-off task
aws ecs run-task \\
    --cluster my-cluster \\
    --task-definition migration-task:1 \\
    --launch-type FARGATE \\
    --network-configuration "awsvpcConfiguration={subnets=[subnet-123]}"

# Se logs
aws logs tail /ecs/my-web-app --follow
```

---

## 🔥 Pro Tips

1. **Fargate first** - Använd Fargate om du inte har specifikt EC2-behov
2. **Task IAM Role** - Ge tasks egna IAM roles, inte EC2 instance role
3. **awslogs** - Alltid logga till CloudWatch
4. **Health checks** - Konfigurera i target group för ALB
5. **Auto Scaling** - Application Auto Scaling för services

---

## 🎯 Hands-on Task

Deploy en web app med ECS Fargate:

```json
// task-definition.json
{
  "family": "demo-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::123:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "app",
      "image": "nginx:alpine",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 80,
          "protocol": "tcp"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/demo-app",
          "awslogs-region": "eu-north-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

Deploy steps:
```bash
# 1. Skapa log group
aws logs create-log-group --log-group-name /ecs/demo-app

# 2. Registrera task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# 3. Skapa cluster
aws ecs create-cluster --cluster-name demo-cluster

# 4. Skapa service
aws ecs create-service \\
    --cluster demo-cluster \\
    --service-name demo-service \\
    --task-definition demo-app:1 \\
    --desired-count 2 \\
    --launch-type FARGATE \\
    --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],securityGroups=[sg-xxx],assignPublicIp=ENABLED}"

# 5. Verifiera
aws ecs describe-services --cluster demo-cluster --services demo-service
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/ecs/"},
            {"type": "workshop", "url": "https://ecsworkshop.com/"}
        ],
        "prerequisites": ["aws-4", "aws-12"],
        "learning_outcomes": [
            "Förstå ECS arkitektur och komponenter",
            "Deploya containers med Fargate",
            "Konfigurera services med auto scaling"
        ],
        "estimated_time": "120 min",
        "difficulty": "intermediate",
        "category": "compute",
        "order": 16
    }
]

# =============================================================================
# BLOCK 5: Expert & Certification (EKS, Security, Cost, Cert Path)
# =============================================================================

AWS_SKILLSMAP_NODES_BLOCK_5 = [
    {
        "id": "aws-17",
        "title": "EKS (Elastic Kubernetes Service)",
        "description": "Managed Kubernetes - enterprise container orchestration",
        "content": """
# 🎯 Hook
Kubernetes är kraftfullt men komplext. Vem vill hantera control plane?

**EKS** = AWS-managed Kubernetes. Du fokuserar på workloads, AWS sköter cluster.

---

## 📚 Koncept

### EKS Architecture:
```
EKS Control Plane (AWS-managed)
├── API Server
├── etcd (HA across 3 AZs)
└── Controller Manager

Data Plane (You manage)
├── Managed Node Groups (recommended)
├── Self-managed nodes (EC2)
└── Fargate (serverless)
```

### EKS vs ECS:
| Feature | EKS | ECS |
|---------|-----|-----|
| Orchestrator | Kubernetes | AWS proprietary |
| Portability | Multi-cloud | AWS only |
| Complexity | Higher | Lower |
| Ecosystem | Huge (CNCF) | AWS integrations |

### Node Types:
- **Managed Node Groups** - AWS handles node lifecycle, updates
- **Self-managed** - Full control, more operational burden
- **Fargate** - Serverless, no nodes to manage

---

## 💻 Kommandon

```bash
# === eksctl (recommended) ===

# Skapa cluster med managed nodes
eksctl create cluster \\
    --name my-cluster \\
    --region eu-north-1 \\
    --nodegroup-name standard-workers \\
    --node-type t3.medium \\
    --nodes 3 \\
    --nodes-min 1 \\
    --nodes-max 5 \\
    --managed

# Skapa Fargate cluster
eksctl create cluster \\
    --name fargate-cluster \\
    --fargate

# Lägg till node group
eksctl create nodegroup \\
    --cluster my-cluster \\
    --name gpu-nodes \\
    --node-type p3.2xlarge \\
    --nodes 2

# Scale node group
eksctl scale nodegroup \\
    --cluster my-cluster \\
    --name standard-workers \\
    --nodes 5

# === AWS CLI ===

# Lista clusters
aws eks list-clusters

# Describe cluster
aws eks describe-cluster --name my-cluster

# Uppdatera kubeconfig
aws eks update-kubeconfig --name my-cluster --region eu-north-1

# === kubectl (after kubeconfig) ===

# Verifiera anslutning
kubectl get nodes
kubectl get pods -A

# Deploy app
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Get LoadBalancer URL
kubectl get svc nginx -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

# === Add-ons ===

# Lista add-ons
aws eks describe-addon-versions --kubernetes-version 1.29

# Installera AWS Load Balancer Controller
eksctl create iamserviceaccount \\
    --cluster my-cluster \\
    --namespace kube-system \\
    --name aws-load-balancer-controller \\
    --attach-policy-arn arn:aws:iam::aws:policy/... \\
    --approve

# Delete cluster
eksctl delete cluster --name my-cluster
```

---

## 🔥 Pro Tips

1. **eksctl** - Använd för cluster management, mycket enklare än raw CLI
2. **IRSA** - IAM Roles for Service Accounts, aldrig node-level IAM
3. **Cluster Autoscaler** - Auto-scale nodes baserat på pending pods
4. **ALB Ingress Controller** - Native AWS ALB för Kubernetes ingress
5. **EKS Blueprints** - Terraform/CDK templates för production-ready clusters

---

## 🎯 Hands-on Task

Deploy en microservice på EKS:

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-api
  labels:
    app: demo-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demo-api
  template:
    metadata:
      labels:
        app: demo-api
    spec:
      containers:
      - name: api
        image: nginx:alpine
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 200m
            memory: 256Mi
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: demo-api
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
spec:
  type: LoadBalancer
  selector:
    app: demo-api
  ports:
  - port: 80
    targetPort: 80
```

```bash
# Deploy
kubectl apply -f deployment.yaml

# Verifiera
kubectl get pods -l app=demo-api
kubectl get svc demo-api

# Test
curl http://$(kubectl get svc demo-api -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/eks/"},
            {"type": "workshop", "url": "https://www.eksworkshop.com/"}
        ],
        "prerequisites": ["aws-16"],
        "learning_outcomes": [
            "Skapa och hantera EKS clusters",
            "Välja rätt node type för workload",
            "Deploya applications på EKS"
        ],
        "estimated_time": "150 min",
        "difficulty": "advanced",
        "category": "compute",
        "order": 17
    },
    {
        "id": "aws-18",
        "title": "AWS Security Best Practices",
        "description": "Säkerhet - defense in depth för AWS-miljöer",
        "content": """
# 🎯 Hook
"Det händer inte oss" - sa alla som blev hackade.

AWS Security är DITT ansvar (Shared Responsibility Model). Lär dig göra det rätt!

---

## 📚 Koncept

### Shared Responsibility Model:
```
AWS ansvarar för:          Du ansvarar för:
├── Hardware               ├── Data
├── Networking             ├── IAM
├── Virtualization         ├── OS patching (EC2)
└── Managed services       ├── Network config
                           ├── Encryption
                           └── Application security
```

### Security Pillars:
1. **Identity & Access** - IAM, MFA, least privilege
2. **Detection** - CloudTrail, GuardDuty, Config
3. **Infrastructure Protection** - VPC, Security Groups, WAF
4. **Data Protection** - Encryption, key management
5. **Incident Response** - Automation, forensics

### Defense in Depth:
```
Internet
    ↓
WAF (Layer 7 filtering)
    ↓
CloudFront (DDoS, edge)
    ↓
ALB (SSL termination)
    ↓
Security Group (stateful firewall)
    ↓
NACL (stateless firewall)
    ↓
EC2/Container (hardened)
    ↓
Encrypted data at rest
```

---

## 💻 Praktiska Åtgärder

```bash
# === IAM Security ===

# Aktivera MFA för root
# (Måste göras i Console)

# Skapa password policy
aws iam update-account-password-policy \\
    --minimum-password-length 14 \\
    --require-symbols \\
    --require-numbers \\
    --require-uppercase-characters \\
    --require-lowercase-characters \\
    --max-password-age 90 \\
    --password-reuse-prevention 12

# Lista users utan MFA
aws iam generate-credential-report
aws iam get-credential-report --output text | base64 -d | grep "false"

# === Encryption ===

# Skapa KMS key
aws kms create-key --description "App encryption key"

# Kryptera S3 bucket default
aws s3api put-bucket-encryption \\
    --bucket my-bucket \\
    --server-side-encryption-configuration '{
        "Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms"}}]
    }'

# Block public access
aws s3api put-public-access-block \\
    --bucket my-bucket \\
    --public-access-block-configuration '{
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    }'

# === Detection ===

# Enable CloudTrail (all regions)
aws cloudtrail create-trail \\
    --name org-trail \\
    --s3-bucket-name cloudtrail-logs-bucket \\
    --is-multi-region-trail \\
    --enable-log-file-validation

aws cloudtrail start-logging --name org-trail

# Enable GuardDuty
aws guardduty create-detector --enable

# === VPC Security ===

# Flow logs
aws ec2 create-flow-logs \\
    --resource-type VPC \\
    --resource-ids vpc-123 \\
    --traffic-type ALL \\
    --log-destination-type cloud-watch-logs \\
    --log-group-name vpc-flow-logs

# === Security Hub (aggregated view) ===
aws securityhub enable-security-hub
```

---

## 🔥 Security Checklist

### IAM:
- [ ] MFA på root account
- [ ] MFA på alla IAM users
- [ ] Inga access keys för root
- [ ] Least privilege policies
- [ ] Regular access review

### Data:
- [ ] S3 buckets ej publika
- [ ] Encryption at rest (EBS, RDS, S3)
- [ ] Encryption in transit (TLS)
- [ ] Secrets i Secrets Manager

### Network:
- [ ] VPC Flow Logs enabled
- [ ] Security Groups - minimal ports
- [ ] Private subnets för databases
- [ ] WAF för publika endpoints

### Monitoring:
- [ ] CloudTrail i alla regioner
- [ ] GuardDuty enabled
- [ ] CloudWatch Alarms på anomalier
- [ ] AWS Config rules

---

## 🎯 Hands-on Task

Säkra ett AWS account:

```bash
# 1. Audit current state
aws iam generate-credential-report
aws iam get-credential-report --output text | base64 -d > cred-report.csv

# 2. Find issues
# - Users without MFA
# - Old access keys (> 90 days)
# - Unused credentials

# 3. Enable GuardDuty
aws guardduty create-detector --enable \\
    --finding-publishing-frequency FIFTEEN_MINUTES

# 4. Check S3 buckets
for bucket in $(aws s3api list-buckets --query 'Buckets[].Name' --output text); do
    echo "Checking $bucket..."
    aws s3api get-bucket-acl --bucket $bucket
    aws s3api get-public-access-block --bucket $bucket 2>/dev/null || echo "No public block!"
done

# 5. Review Security Hub findings
aws securityhub get-findings --filters '{
    "SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}]
}'
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/security/"},
            {"type": "well-architected", "url": "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/"}
        ],
        "prerequisites": ["aws-2", "aws-3"],
        "learning_outcomes": [
            "Implementera defense in depth",
            "Konfigurera detection services",
            "Audita och härda AWS accounts"
        ],
        "estimated_time": "120 min",
        "difficulty": "advanced",
        "category": "security",
        "order": 18
    },
    {
        "id": "aws-19",
        "title": "AWS Cost Optimization",
        "description": "Kostnadsoptimering - få mer värde för pengarna",
        "content": """
# 🎯 Hook
AWS-fakturan gick genom taket? Du är inte ensam.

**Cost Optimization** = Rätt resurser, rätt storlek, rätt pricing. Spara 30-70%!

---

## 📚 Koncept

### Cost Optimization Pillars:
1. **Right-sizing** - Matcha kapacitet med behov
2. **Pricing models** - On-Demand, Reserved, Spot, Savings Plans
3. **Architecture** - Serverless, managed services
4. **Visibility** - Tagga allt, analysera kostnader

### Pricing Models:
| Model | Discount | Commitment | Use Case |
|-------|----------|------------|----------|
| On-Demand | 0% | None | Variable workloads |
| Reserved | 30-72% | 1-3 years | Steady-state |
| Spot | 60-90% | None | Fault-tolerant |
| Savings Plans | 30-66% | 1-3 years | Flexible |

### Cost Hierarchy:
```
Organization (consolidated billing)
├── Account 1 (Production)
│   ├── Service: EC2
│   │   └── Tags: Environment=prod, Team=backend
│   └── Service: RDS
└── Account 2 (Development)
```

---

## 💻 Kommandon & Tools

```bash
# === Cost Explorer CLI ===

# Get costs by service (last 30 days)
aws ce get-cost-and-usage \\
    --time-period Start=$(date -d "30 days ago" +%Y-%m-%d),End=$(date +%Y-%m-%d) \\
    --granularity MONTHLY \\
    --metrics "UnblendedCost" \\
    --group-by Type=DIMENSION,Key=SERVICE

# Get costs by tag
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics "UnblendedCost" \\
    --group-by Type=TAG,Key=Environment

# Get rightsizing recommendations
aws ce get-rightsizing-recommendation \\
    --service EC2

# Get Reserved Instance recommendations
aws ce get-reservation-purchase-recommendation \\
    --service EC2 \\
    --lookback-period-in-days SIXTY_DAYS

# === Savings Plans ===
aws ce get-savings-plans-purchase-recommendation \\
    --savings-plans-type COMPUTE_SP \\
    --lookback-period-in-days SIXTY_DAYS \\
    --payment-option NO_UPFRONT \\
    --term-in-years ONE_YEAR

# === Budgets ===

# Skapa budget med alert
aws budgets create-budget \\
    --account-id 123456789012 \\
    --budget '{
        "BudgetName": "Monthly-Budget",
        "BudgetLimit": {"Amount": "1000", "Unit": "USD"},
        "BudgetType": "COST",
        "TimeUnit": "MONTHLY"
    }' \\
    --notifications-with-subscribers '[{
        "Notification": {
            "NotificationType": "ACTUAL",
            "ComparisonOperator": "GREATER_THAN",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [{
            "SubscriptionType": "EMAIL",
            "Address": "alerts@example.com"
        }]
    }]'

# === Trusted Advisor ===
aws support describe-trusted-advisor-checks \\
    --language en \\
    --query 'checks[?category==`cost_optimizing`].name'
```

---

## 🔥 Quick Wins

### 1. Delete Unused Resources:
```bash
# Unattached EBS volumes
aws ec2 describe-volumes \\
    --filters Name=status,Values=available \\
    --query 'Volumes[].{ID:VolumeId,Size:Size}'

# Old snapshots
aws ec2 describe-snapshots \\
    --owner-ids self \\
    --query 'Snapshots[?StartTime<`2023-01-01`].{ID:SnapshotId,Size:VolumeSize}'

# Unused Elastic IPs
aws ec2 describe-addresses \\
    --query 'Addresses[?InstanceId==null].PublicIp'
```

### 2. Right-size EC2:
```bash
# Check CPU utilization (CloudWatch)
aws cloudwatch get-metric-statistics \\
    --namespace AWS/EC2 \\
    --metric-name CPUUtilization \\
    --dimensions Name=InstanceId,Value=i-123 \\
    --start-time 2024-01-01T00:00:00Z \\
    --end-time 2024-01-31T00:00:00Z \\
    --period 86400 \\
    --statistics Average
```

### 3. Use Spot for non-critical:
```bash
# Spot instance request
aws ec2 request-spot-instances \\
    --instance-count 5 \\
    --type "one-time" \\
    --launch-specification file://spot-spec.json
```

---

## 🎯 Hands-on Task

Bygg en cost dashboard:

```python
# cost_report.py
import boto3
from datetime import datetime, timedelta

ce = boto3.client('ce')

def get_monthly_costs():
    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    print("=== Cost by Service (Last 30 Days) ===")
    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        cost = float(group['Metrics']['UnblendedCost']['Amount'])
        if cost > 1:  # Filter small costs
            print(f"{service}: ${cost:.2f}")

def get_recommendations():
    response = ce.get_rightsizing_recommendation(Service='EC2')

    print("\\n=== Rightsizing Recommendations ===")
    for rec in response.get('RightsizingRecommendations', [])[:5]:
        instance = rec['CurrentInstance']['InstanceName']
        savings = rec['RightsizingRecommendation']['EstimatedMonthlySavings']
        print(f"{instance}: Save ${savings:.2f}/month")

if __name__ == '__main__':
    get_monthly_costs()
    get_recommendations()
```
""",
        "resources": [
            {"type": "docs", "url": "https://docs.aws.amazon.com/cost-management/"},
            {"type": "well-architected", "url": "https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/"}
        ],
        "prerequisites": ["aws-1"],
        "learning_outcomes": [
            "Analysera AWS-kostnader med Cost Explorer",
            "Implementera tagging strategy",
            "Välja rätt pricing model för workloads"
        ],
        "estimated_time": "90 min",
        "difficulty": "intermediate",
        "category": "finops",
        "order": 19
    },
    {
        "id": "aws-20",
        "title": "AWS Certification Path",
        "description": "Certifieringsvägen - validera dina AWS-kunskaper",
        "content": """
# 🎯 Hook
Kunskaper utan bevis? Certifieringar öppnar dörrar!

**AWS Certifications** = Branscherkända bevis på expertis. Bra för karriär OCH lärande.

---

## 📚 Certifieringsöversikt

### Foundational (ingen förkunskap):
```
┌─────────────────────────────────────┐
│  AWS Certified Cloud Practitioner   │
│  - Grundläggande AWS-kunskap        │
│  - 90 min, 65 frågor                │
│  - Bra för alla roller              │
└─────────────────────────────────────┘
```

### Associate (1+ år erfarenhet):
```
┌────────────────────┬────────────────────┬────────────────────┐
│ Solutions Architect│   Developer        │   SysOps Admin     │
│   Associate        │   Associate        │   Associate        │
│                    │                    │                    │
│ Arkitektur &       │ Utveckling &       │ Drift &            │
│ Design patterns    │ CI/CD, Lambda      │ Övervakning        │
└────────────────────┴────────────────────┴────────────────────┘
```

### Professional (2+ år erfarenhet):
```
┌────────────────────────────┬────────────────────────────┐
│ Solutions Architect Pro    │   DevOps Engineer Pro      │
│                            │                            │
│ Komplexa multi-tier        │ CI/CD, Automation          │
│ Enterprise arkitektur      │ IaC, Monitoring            │
└────────────────────────────┴────────────────────────────┘
```

### Specialty:
```
- Advanced Networking
- Security
- Machine Learning
- Database
- Data Analytics
- SAP on AWS
```

---

## 📋 Rekommenderad Path för DevOps

```
START
  │
  ▼
Cloud Practitioner (valfritt men bra grund)
  │
  ▼
Solutions Architect Associate ← REKOMMENDERAS FÖRST
  │
  ├─────────────────────┐
  ▼                     ▼
Developer Associate   SysOps Associate
  │                     │
  └─────────┬───────────┘
            ▼
    DevOps Engineer Professional
            │
            ▼
    Security Specialty (valfritt)
```

---

## 📚 Studieresurser

### Officiellt:
- **AWS Skill Builder** - Gratis kurser från AWS
- **AWS Whitepapers** - Arkitektur best practices
- **AWS FAQs** - Service-specifika deep dives
- **AWS re:Invent videos** - YouTube

### Tredjepartskurser:
- **Adrian Cantrill** - Djupgående, hands-on (cantrill.io)
- **Stephane Maarek** - Utmärkt för certprep (Udemy)
- **A Cloud Guru** - Bra för nybörjare
- **Tutorials Dojo** - Practice exams (Jon Bonso)

### Hands-on:
- **AWS Free Tier** - 12 månader gratis
- **AWS Workshops** - workshops.aws
- **Qwiklabs** - Guidade labs

---

## 💻 Studieplan (SA Associate)

### Vecka 1-2: Compute & Storage
- [ ] EC2 (instance types, pricing, AMIs)
- [ ] EBS (volume types, snapshots)
- [ ] S3 (storage classes, lifecycle)
- [ ] Lambda basics

### Vecka 3-4: Networking & Security
- [ ] VPC (subnets, route tables, NAT)
- [ ] Security Groups & NACLs
- [ ] IAM (policies, roles, federation)
- [ ] Route 53

### Vecka 5-6: Databases & HA
- [ ] RDS (engines, Multi-AZ, read replicas)
- [ ] DynamoDB
- [ ] ElastiCache
- [ ] ELB & Auto Scaling

### Vecka 7-8: Services & Review
- [ ] SQS, SNS, EventBridge
- [ ] CloudWatch, CloudTrail
- [ ] CloudFormation basics
- [ ] Practice exams!

---

## 🔥 Exam Tips

1. **Läs frågan NOGA** - AWS älskar "most cost-effective" vs "fastest"
2. **Eliminera** - Oftast 2 svar är uppenbart fel
3. **Tidhantering** - ~2 min per fråga, flagga och gå vidare
4. **Fokus på scenarios** - Förstå USE CASES, inte bara features
5. **Whitepapers** - Well-Architected Framework är GULD

---

## 🎯 Hands-on Task

Skapa din certifieringsplan:

```markdown
# Min AWS Certifieringsplan

## Mål
- [ ] Cloud Practitioner: Q2 2024
- [ ] SA Associate: Q3 2024
- [ ] DevOps Pro: Q1 2025

## Daglig rutin (1-2 timmar)
- 30 min: Video/kurs
- 30 min: Hands-on lab
- 30 min: Practice questions

## Resurser jag använder
1. Adrian Cantrill SA Associate kurs
2. Tutorials Dojo practice exams
3. AWS Free Tier för labs

## Tracking
| Datum | Ämne | Tid | Anteckningar |
|-------|------|-----|--------------|
| 2024-01-15 | VPC basics | 2h | Förstår subnets! |
| ... | ... | ... | ... |
```

Boka certifieringstillfälle i förväg för att skapa deadline! 🎯
""",
        "resources": [
            {"type": "official", "url": "https://aws.amazon.com/certification/"},
            {"type": "skill-builder", "url": "https://explore.skillbuilder.aws/"},
            {"type": "practice", "url": "https://tutorialsdojo.com/"}
        ],
        "prerequisites": ["aws-1"],
        "learning_outcomes": [
            "Förstå AWS certification paths",
            "Skapa en personlig studieplan",
            "Hitta rätt resurser för certification prep"
        ],
        "estimated_time": "60 min",
        "difficulty": "beginner",
        "category": "career",
        "order": 20
    }
]

AWS_SKILLSMAP_NODES = AWS_SKILLSMAP_NODES_BLOCK_1 + AWS_SKILLSMAP_NODES_BLOCK_2 + AWS_SKILLSMAP_NODES_BLOCK_3 + AWS_SKILLSMAP_NODES_BLOCK_4 + AWS_SKILLSMAP_NODES_BLOCK_5

# Verify node count
assert len(AWS_SKILLSMAP_NODES) == 20, f"Expected 20 nodes, got {len(AWS_SKILLSMAP_NODES)}"

print(f"✅ AWS SkillsMap COMPLETE: {len(AWS_SKILLSMAP_NODES)} nodes loaded")
print("Block 1: AWS Intro, IAM, VPC, EC2")
print("Block 2: S3, RDS, Route53, CloudWatch")
print("Block 3: Lambda, CloudFormation, CloudFront, ELB")
print("Block 4: DynamoDB, SNS/SQS, Secrets Manager, ECS")
print("Block 5: EKS, Security, Cost Optimization, Certification")
