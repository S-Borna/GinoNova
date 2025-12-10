"""
AWS Mastery Module
==================

20 noder med svensk pedagogisk stil.
Komplett AWS-administration - från IAM till produktionsarkitektur.

Track: cloud
Difficulty: intermediate
Estimated Hours: 35
"""

MODULE = {
    "name": "AWS Mastery",
    "slug": "aws-mastery",
    "description": "Komplett AWS-administration - från IAM till produktionsarkitektur med naturlig svensk pedagogik",
    "track_slug": "cloud",
    "order_index": 9,
    "difficulty": "intermediate",
    "estimated_hours": 35,
    "prerequisites": ["linux-mastery"],
    "icon": "☁️",
    "color": "#FF9900",
    "tasks": [
        {
            "title": "AWS Introduktion och Grundkoncept",
            "slug": "aws-intro-grundkoncept",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# AWS Introduktion och Grundkoncept

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor AWS-kunskap ar kritisk |
|----------|-------------------------------|
| **Infrastruktur** | 32% marknadsandel - du KOMMER arbeta med AWS |
| **Automation** | CLI och SDK for att automatisera allt |
| **Skalning** | Auto Scaling, Load Balancing, global distribution |
| **Kostnadshantering** | Forstå prissättning for att undvika overraskningar |
| **Compliance** | GDPR kräver rätt regionval |

AWS är den största molnplattformen i världen. Som DevOps-ingenjör behöver du förstå hur AWS är organiserat, hur regioner och Availability Zones fungerar, och hur du automatiserar med CLI istället för att klicka i konsolen.

------------------------------------------------------------

## AWS Global Infrastructure

```
+-------------------------------------------------------------+
|                    AWS GLOBAL STRUKTUR                      |
+-------------------------------------------------------------+
|                                                             |
|   REGION (eu-north-1 Stockholm)                             |
|   +-----------------------------------------------------+   |
|   |                                                     |   |
|   |   AZ-a              AZ-b              AZ-c          |   |
|   |   +-----+          +-----+          +-----+        |   |
|   |   | DC  |◄--------►| DC  |◄--------►| DC  |        |   |
|   |   |     |  Fiber   |     |  Fiber   |     |        |   |
|   |   +-----+          +-----+          +-----+        |   |
|   |                                                     |   |
|   |   Separata         Låg latens       Redundans      |   |
|   |   datacenter       <2ms mellan      vid fel        |   |
|   |                                                     |   |
|   +-----------------------------------------------------+   |
|                                                             |
|   Andra regioner: eu-west-1, us-east-1, ap-northeast-1...   |
|                                                             |
+-------------------------------------------------------------+
```

### Regionöversikt

| Region | Namn | Användning |
|--------|------|------------|
| `eu-north-1` | Stockholm | Svenska projekt, GDPR |
| `eu-west-1` | Irland | Europeiska användare |
| `us-east-1` | N. Virginia | Nya tjänster först, US-användare |
| `ap-northeast-1` | Tokyo | Asiatiska användare |

------------------------------------------------------------

## Installera AWS CLI

| Steg | Kommando | Beskrivning |
|------|----------|-------------|
| 1 | `curl ... -o awscliv2.zip` | Ladda ner |
| 2 | `unzip awscliv2.zip` | Packa upp |
| 3 | `sudo ./aws/install` | Installera |
| 4 | `aws --version` | Verifiera |

```bash
# Ladda ner AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Packa upp
unzip awscliv2.zip

# Installera
sudo ./aws/install

# Verifiera installation
aws --version
# aws-cli/2.15.0 Python/3.11.6 Linux/5.15.0-1051-aws
```

------------------------------------------------------------

## Konfigurera AWS CLI

```
+-------------------------------------------------------------+
|                 AWS CREDENTIAL FLOW                         |
+-------------------------------------------------------------+
|                                                             |
|   aws configure                                             |
|        |                                                    |
|        ▼                                                    |
|   +-----------------------------------------------------+   |
|   |  ~/.aws/credentials        ~/.aws/config            |   |
|   |  -----------------         -------------            |   |
|   |  [default]                 [default]                |   |
|   |  aws_access_key_id=...     region=eu-north-1        |   |
|   |  aws_secret_access_key=... output=json              |   |
|   +-----------------------------------------------------+   |
|                                                             |
|   SKYDDA CREDENTIALS: chmod 600 ~/.aws/credentials          |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Interaktiv konfiguration
aws configure
# AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key [None]: wJalrXUtn.../bPxRfiCYEXAMPLEKEY
# Default region name [None]: eu-north-1
# Default output format [None]: json

# Verifiera konfiguration
cat ~/.aws/credentials
cat ~/.aws/config
```

------------------------------------------------------------

## Grundläggande kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `aws sts get-caller-identity` | Vem är jag inloggad som? |
| `aws ec2 describe-regions` | Lista alla regioner |
| `aws ec2 describe-availability-zones` | Lista AZs i region |
| `aws s3 ls` | Lista S3-buckets |

```bash
# Verifiera credentials - "whoami" for AWS
aws sts get-caller-identity
# {
#     "UserId": "AIDAIOSFODNN7EXAMPLE",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/devops-user"
# }

# Lista regioner
aws ec2 describe-regions --output table

# Lista AZs i Stockholm
aws ec2 describe-availability-zones --region eu-north-1

# Lista S3-buckets
aws s3 ls
```

------------------------------------------------------------

## Miljövariabler for credentials

| Variabel | Beskrivning |
|----------|-------------|
| `AWS_ACCESS_KEY_ID` | Access key (överrider config) |
| `AWS_SECRET_ACCESS_KEY` | Secret key |
| `AWS_DEFAULT_REGION` | Standardregion |
| `AWS_PROFILE` | Välj named profile |

```bash
# Satt credentials via miljövariabler (CI/CD)
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_DEFAULT_REGION="eu-north-1"

# Verifiera
env | grep AWS
```

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Unable to locate credentials` | Ej konfigurerat | `aws configure` |
| `InvalidClientTokenId` | Fel access key | Kontrollera key i IAM |
| `SignatureDoesNotMatch` | Fel secret key | Skapa ny key |
| `UnauthorizedAccess` | Saknar permissions | Lägg till IAM policy |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Regioner** | Geografiska områden - välj baserat på latens och compliance |
| **Availability Zones** | Separata datacenter inom region - minst 2 for redundans |
| **AWS CLI** | Kraftfullare än konsolen - krävs for automation |
| **Credentials** | Behandla som lösenord - aldrig i kod |
| **eu-north-1** | Stockholm-regionen - bra val for svenska projekt |

**Kom ihåg:**
- Använd **eu-north-1** for svenska projekt med GDPR-krav
- **Sprid resurser** över minst 2 AZs for hög tillgänglighet
- **Skydda credentials** - chmod 600 på ~/.aws/credentials
- **aws sts get-caller-identity** är din "whoami" for AWS
- **Miljövariabler** överrider config-filer
""",
        },
        {
            "title": "IAM - Identity and Access Management",
            "slug": "iam-identity-access-management",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# IAM - Identity and Access Management

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor IAM-kunskap ar kritisk |
|----------|-------------------------------|
| **Sakerhet** | Felkonfigurerat IAM = exponerad infrastruktur |
| **Automation** | CI/CD-pipelines kraver ratt permissions |
| **Compliance** | Audit kräver spårbarhet av vem som gjorde vad |
| **Least Privilege** | Minimera skada vid komprometterad credential |
| **Multi-team** | Separera access mellan team och miljöer |

IAM ar AWS sakerhetsgrund - det kontrollerar vem som far gora vad. Utan IAM-kunskap kan du skapa sakerhetshål, lasa dig sjalv ute, eller bryta mot compliance.

------------------------------------------------------------

## IAM Komponenter

```
+-------------------------------------------------------------+
|                    IAM ARKITEKTUR                           |
+-------------------------------------------------------------+
|                                                             |
|   +-------------+     +-------------+     +-------------+   |
|   |   USERS     |     |   GROUPS    |     |   ROLES     |   |
|   |             |     |             |     |             |   |
|   |  Personer   |----▶|  Samlingar  |     |  Temporara  |   |
|   |  Service    |     |  av users   |     |  identitet  |   |
|   |  accounts   |     |             |     |  for EC2,   |   |
|   |             |     |             |     |  Lambda...  |   |
|   +-------------+     +-------------+     +-------------+   |
|          |                   |                   |          |
|          +-------------------+-------------------+          |
|                              ▼                              |
|                    +-----------------+                      |
|                    |    POLICIES     |                      |
|                    |                 |                      |
|                    |  JSON-dokument  |                      |
|                    |  som definierar |                      |
|                    |  permissions    |                      |
|                    +-----------------+                      |
|                                                             |
|   PRINCIP: Deny by default - allt ar forbjudet tills       |
|            du explicit tillåter det                         |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa IAM-anvandare

| Kommando | Beskrivning |
|----------|-------------|
| `aws iam create-user` | Skapa ny användare |
| `aws iam list-users` | Lista alla användare |
| `aws iam get-user` | Hämta info om användare |
| `aws iam delete-user` | Ta bort användare |

```bash
# Skapa användare
aws iam create-user --user-name deploy-bot
# Användaren har INGA permissions ännu

# Lista användare
aws iam list-users

# Hämta specifik användare
aws iam get-user --user-name deploy-bot
```

------------------------------------------------------------

## Access Keys

```
+-------------------------------------------------------------+
|                 ACCESS KEY LIFECYCLE                        |
+-------------------------------------------------------------+
|                                                             |
|   create-access-key          SecretAccessKey                |
|         |                    VISAS BARA EN GÅNG!            |
|         ▼                                                   |
|   +-------------+                                          |
|   |   ACTIVE    | ◄--- Används för API-anrop               |
|   +-------------+                                          |
|         |                                                   |
|         | update-access-key --status Inactive               |
|         ▼                                                   |
|   +-------------+                                          |
|   |  INACTIVE   | ◄--- Tillfälligt avstängd                |
|   +-------------+                                          |
|         |                                                   |
|         | delete-access-key                                 |
|         ▼                                                   |
|   +-------------+                                          |
|   |   DELETED   | ◄--- Permanent borttagen                 |
|   +-------------+                                          |
|                                                             |
|   MAX 2 ACCESS KEYS PER ANVÄNDARE                           |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa access key - SPARA OUTPUT DIREKT!
aws iam create-access-key --user-name deploy-bot

# Lista access keys
aws iam list-access-keys --user-name deploy-bot

# Rotera: inaktivera gammal
aws iam update-access-key --user-name deploy-bot \\
    --access-key-id AKIAOLD --status Inactive

# Ta bort gammal key
aws iam delete-access-key --user-name deploy-bot \\
    --access-key-id AKIAOLD
```

------------------------------------------------------------

## IAM Groups

| Kommando | Beskrivning |
|----------|-------------|
| `aws iam create-group` | Skapa grupp |
| `aws iam add-user-to-group` | Lägg till användare |
| `aws iam list-groups-for-user` | Visa användares grupper |
| `aws iam attach-group-policy` | Ge gruppen permissions |

```bash
# Skapa grupp
aws iam create-group --group-name Developers

# Lägg till användare i grupp
aws iam add-user-to-group --user-name deploy-bot --group-name Developers

# Ge gruppen permissions
aws iam attach-group-policy \\
    --group-name Developers \\
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

# Alla i gruppen ärver nu EC2-rättigheter
```

------------------------------------------------------------

## IAM Policies

### Policy-struktur

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3Upload",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}
```

| Fält | Beskrivning |
|------|-------------|
| `Version` | Alltid "2012-10-17" |
| `Sid` | Beskrivande namn (valfritt) |
| `Effect` | Allow eller Deny |
| `Action` | Vilka API-anrop som tillåts |
| `Resource` | Vilka resurser policyn gäller |

```bash
# Skapa custom policy
aws iam create-policy \\
    --policy-name S3UploadOnly \\
    --policy-document file://policy.json

# Attacha till user
aws iam attach-user-policy \\
    --user-name deploy-bot \\
    --policy-arn arn:aws:iam::123456789012:policy/S3UploadOnly
```

------------------------------------------------------------

## IAM Roles

```
+-------------------------------------------------------------+
|                 ROLE VS USER                                |
+-------------------------------------------------------------+
|                                                             |
|   USER                          ROLE                        |
|   ----                          ----                        |
|   Permanent credentials         Temporära credentials       |
|   Access keys                   STS tokens (expire)         |
|   För människor/CI              För AWS-tjänster            |
|                                                             |
|   Exempel:                      Exempel:                    |
|   - Utvecklare                  - EC2 som läser S3          |
|   - GitHub Actions              - Lambda som skriver DynamoDB|
|   - Deploy scripts              - ECS tasks                 |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa role for EC2
aws iam create-role \\
    --role-name EC2-S3-Access \\
    --assume-role-policy-document file://trust-policy.json

# Trust policy (vem får anta rollen):
# {
#   "Version": "2012-10-17",
#   "Statement": [{
#     "Effect": "Allow",
#     "Principal": {"Service": "ec2.amazonaws.com"},
#     "Action": "sts:AssumeRole"
#   }]
# }

# Attacha permissions till role
aws iam attach-role-policy \\
    --role-name EC2-S3-Access \\
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AccessDenied` | Saknar permission | Lägg till rätt policy |
| `InvalidClientTokenId` | Fel access key | Kontrollera credentials |
| `EntityAlreadyExists` | User/group finns redan | Använd annat namn |
| `DeleteConflict` | User har attachade policies | Detacha policies först |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Deny by default** | Inget ar tillatet forrän du explicit tillåter |
| **Groups over Users** | Attacha policies till groups, inte users |
| **Least privilege** | Ge minsta möjliga permissions |
| **Roles for services** | EC2, Lambda etc. ska använda roles |
| **Rotera keys** | Byt access keys regelbundet |

**Kom ihåg:**
- **Använd Groups** for att hantera permissions centralt
- **Aldrig root account** for dagligt arbete
- **SecretAccessKey** visas bara en gång - spara direkt
- **IAM Roles** for AWS-tjänster istället for hardcoded keys
- **Audit regelbundet** med IAM Access Analyzer
""",
        },
        {
            "title": "EC2 - Elastic Compute Cloud",
            "slug": "ec2-elastic-compute-cloud",
            "difficulty": "easy",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# EC2 - Elastic Compute Cloud

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor EC2-kunskap ar kritisk |
|----------|-------------------------------|
| **Compute** | Virtuella servrar for alla workloads |
| **Skalning** | Starta/stoppa instanser baserat pa behov |
| **Kostnader** | Fel instanstyp = slöseri med pengar |
| **Automation** | User Data for automatisk konfiguration |
| **Sakerhet** | Security Groups ar din brandvägg |

EC2 ar AWS ursprungliga och mest anvanda tjanst - virtuella servrar i molnet. Du betalar per sekund for tiden instansen ar igång.

------------------------------------------------------------

## EC2 Komponenter

```
+-------------------------------------------------------------+
|                    EC2 INSTANS                              |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------------------------------------------+   |
|   |  AMI (Amazon Machine Image)                         |   |
|   |  - Operativsystem (Ubuntu, Amazon Linux, Windows)   |   |
|   |  - Forinstallerad mjukvara                          |   |
|   +-----------------------------------------------------+   |
|                           |                                 |
|                           ▼                                 |
|   +-----------------------------------------------------+   |
|   |  Instance Type (t3.micro, m5.large, etc.)           |   |
|   |  - vCPUs, RAM, Nätverk                              |   |
|   |  - t3.micro = 2 vCPU, 1 GB RAM (Free Tier)          |   |
|   +-----------------------------------------------------+   |
|                           |                                 |
|                           ▼                                 |
|   +--------------+  +--------------+  +--------------+     |
|   |Security Group|  |   Key Pair   |  |  User Data   |     |
|   | (Brandvägg)  |  |  (SSH-nyckel)|  |  (Bootstrap) |     |
|   +--------------+  +--------------+  +--------------+     |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Instanstyper

| Typ | vCPU | RAM | Användning |
|-----|------|-----|------------|
| `t3.micro` | 2 | 1 GB | Test, dev (Free Tier) |
| `t3.small` | 2 | 2 GB | Små workloads |
| `t3.medium` | 2 | 4 GB | Webservrar |
| `m5.large` | 2 | 8 GB | Produktion |
| `c5.xlarge` | 4 | 8 GB | CPU-intensivt |
| `r5.large` | 2 | 16 GB | Minnesintensivt |

```bash
# Lista tillgängliga instanstyper
aws ec2 describe-instance-types \\
    --query "InstanceTypes[*].[InstanceType,VCpuInfo.DefaultVCpus,MemoryInfo.SizeInMiB]" \\
    --output table
```

------------------------------------------------------------

## Skapa EC2-instans

| Parameter | Beskrivning |
|-----------|-------------|
| `--image-id` | AMI (operativsystem) |
| `--instance-type` | Storlek (CPU/RAM) |
| `--key-name` | SSH-nyckel |
| `--security-group-ids` | Brandvägg |
| `--subnet-id` | Nätverk |

```bash
# Starta EC2-instans
aws ec2 run-instances \\
    --image-id ami-0c55b159cbfafe1f0 \\
    --instance-type t3.micro \\
    --key-name my-key \\
    --security-group-ids sg-12345678 \\
    --subnet-id subnet-12345678 \\
    --count 1

# Lista körande instanser
aws ec2 describe-instances \\
    --filters "Name=instance-state-name,Values=running" \\
    --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress,InstanceType]" \\
    --output table
```

------------------------------------------------------------

## Instans Lifecycle

```
+-------------------------------------------------------------+
|                 EC2 LIFECYCLE                               |
+-------------------------------------------------------------+
|                                                             |
|   run-instances                                             |
|        |                                                    |
|        ▼                                                    |
|   +---------+    start    +---------+                      |
|   | PENDING | ----------▶ | RUNNING | ◄--+                 |
|   +---------+             +----+----+    |                 |
|                                |         |                 |
|                    stop        |    start|                 |
|                                ▼         |                 |
|                           +---------+    |                 |
|                           | STOPPED | ---+                 |
|                           +----+----+                      |
|                                |                            |
|                    terminate   |                            |
|                                ▼                            |
|                          +-----------+                     |
|                          |TERMINATED |                     |
|                          +-----------+                     |
|                                                             |
|   STOPPED = Ingen compute-kostnad (EBS kostar fortfarande) |
|   TERMINATED = Permanent borttagen                         |
|                                                             |
+-------------------------------------------------------------+
```

| Kommando | Beskrivning |
|----------|-------------|
| `stop-instances` | Stäng av (data bevaras) |
| `start-instances` | Starta stoppad instans |
| `reboot-instances` | Starta om |
| `terminate-instances` | Ta bort PERMANENT |

```bash
# Stoppa instans (spara pengar)
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Starta igen
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Ta bort permanent (VARNING!)
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

------------------------------------------------------------

## Security Groups

```
+-------------------------------------------------------------+
|               SECURITY GROUP (Brandvägg)                    |
+-------------------------------------------------------------+
|                                                             |
|   Internet                                                  |
|      |                                                      |
|      | Port 443 (HTTPS) ✓ ALLOWED                          |
|      | Port 22 (SSH)    ✓ ALLOWED (från specifik IP)       |
|      | Port 3306        ✗ BLOCKED                          |
|      ▼                                                      |
|   +-----------------------------------------------------+   |
|   |              SECURITY GROUP                         |   |
|   |                                                     |   |
|   |  INBOUND RULES:                                     |   |
|   |  +--------+------+-------------+                   |   |
|   |  | Port   |Proto | Source      |                   |   |
|   |  +--------+------+-------------+                   |   |
|   |  | 22     | TCP  | 10.0.0.0/8  | (SSH)            |   |
|   |  | 443    | TCP  | 0.0.0.0/0   | (HTTPS)          |   |
|   |  +--------+------+-------------+                   |   |
|   |                                                     |   |
|   |  OUTBOUND: All traffic allowed (default)           |   |
|   |                                                     |   |
|   +-----------------------------------------------------+   |
|                          |                                  |
|                          ▼                                  |
|                    EC2 Instance                             |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa security group
aws ec2 create-security-group \\
    --group-name web-server-sg \\
    --description "Web server security group" \\
    --vpc-id vpc-12345678

# Öppna port 22 (SSH) - BEGRÄNSA TILL DIN IP!
aws ec2 authorize-security-group-ingress \\
    --group-id sg-12345678 \\
    --protocol tcp \\
    --port 22 \\
    --cidr 10.0.0.0/8

# Öppna port 443 (HTTPS) för alla
aws ec2 authorize-security-group-ingress \\
    --group-id sg-12345678 \\
    --protocol tcp \\
    --port 443 \\
    --cidr 0.0.0.0/0
```

------------------------------------------------------------

## SSH-nycklar

```bash
# Skapa nyckelpar
aws ec2 create-key-pair \\
    --key-name my-server-key \\
    --query 'KeyMaterial' \\
    --output text > my-server-key.pem

# Sätt rätt permissions (OBLIGATORISKT)
chmod 400 my-server-key.pem

# Anslut via SSH
ssh -i my-server-key.pem ec2-user@<public-ip>
# ec2-user = Amazon Linux
# ubuntu = Ubuntu
```

------------------------------------------------------------

## User Data (Bootstrap)

```bash
# userdata.sh - körs vid första boot
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
```

```bash
# Starta instans med user data
aws ec2 run-instances \\
    --image-id ami-0c55b159cbfafe1f0 \\
    --instance-type t3.micro \\
    --key-name my-key \\
    --security-group-ids sg-12345678 \\
    --user-data file://userdata.sh

# Loggar finns i:
# /var/log/cloud-init-output.log
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Permission denied (publickey)` | Fel key eller permissions | chmod 400, rätt user |
| `Connection timed out` | Security group blockerar | Öppna port 22 |
| `Instance limit exceeded` | Konto-gräns nådd | Begär limit increase |
| `InsufficientInstanceCapacity` | Ingen kapacitet i AZ | Prova annan AZ |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **t3.micro** | Free Tier - perfekt for test och dev |
| **Security Groups** | Stateful brandvägg - reply tillåts automatiskt |
| **Stop vs Terminate** | Stop bevarar data, terminate raderar allt |
| **User Data** | Bootstrap-script for automatisk konfiguration |
| **Key Pairs** | SSH-nycklar - private key sparas ALDRIG i AWS |

**Kom ihåg:**
- **Stoppa instanser** du inte använder for att spara pengar
- **Begränsa SSH** till specifika IP:er, aldrig 0.0.0.0/0
- **User Data** körs bara vid första boot
- **chmod 400** på SSH-nycklar är obligatoriskt
- **EBS-volymer** kostar även när instansen är stoppad
""",
        },
        {
            "title": "VPC - Virtual Private Cloud",
            "slug": "vpc-virtual-private-cloud",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 90,
            "content": """# VPC - Virtual Private Cloud

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor VPC-kunskap ar kritisk |
|----------|-------------------------------|
| **Isolation** | Separera resurser fran andra kunder och internet |
| **Sakerhet** | Kontrollera vem som kan na vad |
| **Arkitektur** | Design med publika och privata lager |
| **Felsökning** | Förstå nätverksflödet när saker inte fungerar |
| **Compliance** | Data i privata subnets for GDPR |

VPC ar ditt privata natverk i AWS. Utan VPC-kunskap kan du inte bygga sakra, skalbara arkitekturer.

------------------------------------------------------------

## VPC Arkitektur

```
+-------------------------------------------------------------+
|                    VPC (10.0.0.0/16)                        |
+-------------------------------------------------------------+
|                                                             |
|   Internet                                                  |
|      |                                                      |
|      ▼                                                      |
|   +------------------+                                      |
|   | Internet Gateway |                                      |
|   +--------+---------+                                      |
|            |                                                |
|   +--------+--------------------------------------------+   |
|   |              PUBLIC SUBNETS                         |   |
|   |  +-----------------+    +-----------------+        |   |
|   |  |   10.0.1.0/24   |    |   10.0.2.0/24   |        |   |
|   |  |   eu-north-1a   |    |   eu-north-1b   |        |   |
|   |  |   Load Balancer |    |   NAT Gateway   |        |   |
|   |  +-----------------+    +--------+--------+        |   |
|   +---------------------------------+-------------------+   |
|                                     |                       |
|   +---------------------------------+-------------------+   |
|   |              PRIVATE SUBNETS                        |   |
|   |  +-----------------+    +-----------------+        |   |
|   |  |  10.0.10.0/24   |    |  10.0.11.0/24   |        |   |
|   |  |   eu-north-1a   |    |   eu-north-1b   |        |   |
|   |  |   App Servers   |    |   Databases     |        |   |
|   |  +-----------------+    +-----------------+        |   |
|   +-----------------------------------------------------+   |
|                                                             |
|   PUBLIC = Route till Internet Gateway                      |
|   PRIVATE = Route till NAT Gateway (ut) eller ingen         |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## CIDR Block Planering

| CIDR | IP-adresser | Användning |
|------|-------------|------------|
| `/16` | 65,536 | Hel VPC |
| `/20` | 4,096 | Stort subnet |
| `/24` | 256 | Standard subnet |
| `/28` | 16 | Litet subnet |

```bash
# Skapa VPC
aws ec2 create-vpc \\
    --cidr-block 10.0.0.0/16 \\
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=prod-vpc}]'

# Aktivera DNS
aws ec2 modify-vpc-attribute \\
    --vpc-id vpc-12345678 \\
    --enable-dns-hostnames '{"Value":true}'
```

------------------------------------------------------------

## Skapa Subnets

| Subnet | CIDR | AZ | Typ |
|--------|------|----|----|
| public-1a | 10.0.1.0/24 | eu-north-1a | Public |
| public-1b | 10.0.2.0/24 | eu-north-1b | Public |
| private-1a | 10.0.10.0/24 | eu-north-1a | Private |
| private-1b | 10.0.11.0/24 | eu-north-1b | Private |

```bash
# Public subnet i AZ a
aws ec2 create-subnet \\
    --vpc-id vpc-12345678 \\
    --cidr-block 10.0.1.0/24 \\
    --availability-zone eu-north-1a \\
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=public-1a}]'

# Private subnet i AZ a
aws ec2 create-subnet \\
    --vpc-id vpc-12345678 \\
    --cidr-block 10.0.10.0/24 \\
    --availability-zone eu-north-1a \\
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=private-1a}]'
```

------------------------------------------------------------

## Internet Gateway

```
+-------------------------------------------------------------+
|              INTERNET GATEWAY FLOW                          |
+-------------------------------------------------------------+
|                                                             |
|   Internet ◄--------------------------------------+         |
|                                                   |         |
|   +-----------------------------------------------+---+     |
|   |         Internet Gateway (IGW)                |   |     |
|   |         1 per VPC                             |   |     |
|   +-----------------------------------------------+---+     |
|                                                   |         |
|   Route Table:                                    |         |
|   +-----------------------------------------------+---+     |
|   | Destination     | Target                      |   |     |
|   +-----------------+-----------------------------+---+     |
|   | 10.0.0.0/16     | local                       |   |     |
|   | 0.0.0.0/0       | igw-xxxxx  ◄----------------+   |     |
|   +-----------------+---------------------------------+     |
|                                                             |
|   0.0.0.0/0 = "default route" = all traffic not matching    |
|               any other route goes here                     |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa IGW
aws ec2 create-internet-gateway \\
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=prod-igw}]'

# Attacha till VPC
aws ec2 attach-internet-gateway \\
    --internet-gateway-id igw-12345678 \\
    --vpc-id vpc-12345678
```

------------------------------------------------------------

## Route Tables

| Route Table | Destination | Target | Subnet |
|-------------|-------------|--------|--------|
| public-rt | 0.0.0.0/0 | igw-xxx | public-* |
| private-rt | 0.0.0.0/0 | nat-xxx | private-* |

```bash
# Skapa public route table
aws ec2 create-route-table \\
    --vpc-id vpc-12345678 \\
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=public-rt}]'

# Lägg till route till IGW
aws ec2 create-route \\
    --route-table-id rtb-12345678 \\
    --destination-cidr-block 0.0.0.0/0 \\
    --gateway-id igw-12345678

# Associera med public subnet
aws ec2 associate-route-table \\
    --route-table-id rtb-12345678 \\
    --subnet-id subnet-public-1a
```

------------------------------------------------------------

## NAT Gateway

```
+-------------------------------------------------------------+
|              NAT GATEWAY FLOW                               |
+-------------------------------------------------------------+
|                                                             |
|   Private Subnet          NAT Gateway         Internet      |
|   (10.0.10.0/24)          (i public subnet)                 |
|                                                             |
|   +------------+          +------------+                    |
|   | App Server | --------▶|    NAT     | --------▶ Internet |
|   | 10.0.10.5  |          | 52.95.1.1  |                    |
|   +------------+          +------------+                    |
|                                                             |
|   ✓ App kan hämta uppdateringar                            |
|   ✗ Internet kan INTE nå App                               |
|                                                             |
|   NAT Gateway:                                              |
|   - Måste placeras i PUBLIC subnet                          |
|   - Behöver Elastic IP                                      |
|   - Kostar ~$0.045/timme + data transfer                    |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Allokera Elastic IP
aws ec2 allocate-address --domain vpc

# Skapa NAT Gateway i PUBLIC subnet
aws ec2 create-nat-gateway \\
    --subnet-id subnet-public-1a \\
    --allocation-id eipalloc-12345678 \\
    --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=prod-nat}]'

# Skapa private route table med route till NAT
aws ec2 create-route \\
    --route-table-id rtb-private \\
    --destination-cidr-block 0.0.0.0/0 \\
    --nat-gateway-id nat-12345678
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Kan inte nå internet | Ingen route till IGW | Lägg till 0.0.0.0/0 -> igw |
| Timeout till EC2 | Security Group blockerar | Öppna rätt portar |
| Private subnet kan inte uppdatera | Ingen NAT | Skapa NAT Gateway |
| Subnets kan inte kommunicera | Olika VPCs | VPC Peering eller samma VPC |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **VPC** | Ditt privata nätverk i AWS |
| **Public subnet** | Har route till Internet Gateway |
| **Private subnet** | Ingen direkt internetåtkomst |
| **NAT Gateway** | Låter private subnets nå ut |
| **Route Tables** | Bestämmer var trafik skickas |

**Kom ihåg:**
- **Minst 2 AZs** for high availability
- **Databaser i private subnets** - aldrig publikt
- **NAT Gateway kostar** - stäng av i dev-miljöer
- **CIDR-planering** - tänk på framtida tillväxt
- **Security Groups + NACLs** for defense in depth
""",
        },
        {
            "title": "S3 - Simple Storage Service",
            "slug": "s3-simple-storage-service",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# S3 - Simple Storage Service

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor S3-kunskap ar kritisk |
|----------|------------------------------|
| **Artifacts** | Build outputs, Docker images, logs |
| **Static hosting** | Frontend-appar (React, Vue, Angular) |
| **Backup** | Databaser, konfiguration, state-filer |
| **Data lake** | Analytics, ML datasets |
| **Terraform state** | Remote state backend |

S3 ar AWS objektlagring med 99.999999999% durability (11 nior). Du forlorar 1 objekt av 10 miljarder pa 10,000 ar.

------------------------------------------------------------

## S3 Koncept

```
+-------------------------------------------------------------+
|                    S3 STRUKTUR                              |
+-------------------------------------------------------------+
|                                                             |
|   BUCKET (globalt unikt namn)                               |
|   s3://my-company-artifacts-prod                            |
|   |                                                         |
|   +-- builds/                                               |
|   |   +-- app-v1.0.0.zip          (Objekt)                 |
|   |   +-- app-v1.0.1.zip          (Objekt)                 |
|   |   +-- app-v1.1.0.zip          (Objekt)                 |
|   |                                                         |
|   +-- logs/                                                 |
|   |   +-- 2024/12/07/access.log   (Prefix = "folder")      |
|   |   +-- 2024/12/07/error.log                             |
|   |                                                         |
|   +-- config/                                               |
|       +-- settings.json                                     |
|                                                             |
|   KEY = builds/app-v1.0.0.zip                              |
|   Det finns inga riktiga mappar - bara prefix i key         |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Bucket-operationer

| Kommando | Beskrivning |
|----------|-------------|
| `aws s3 mb s3://bucket` | Skapa bucket |
| `aws s3 ls` | Lista alla buckets |
| `aws s3 ls s3://bucket/` | Lista innehåll |
| `aws s3 rb s3://bucket` | Ta bort tom bucket |
| `aws s3 rb s3://bucket --force` | Ta bort bucket + innehåll |

```bash
# Skapa bucket (globalt unikt namn!)
aws s3 mb s3://my-company-artifacts-12345

# Lista buckets
aws s3 ls

# Lista innehåll
aws s3 ls s3://my-company-artifacts-12345/
aws s3 ls s3://my-company-artifacts-12345/ --recursive
```

------------------------------------------------------------

## Ladda upp och ner

| Kommando | Beskrivning |
|----------|-------------|
| `aws s3 cp local s3://` | Ladda upp fil |
| `aws s3 cp s3:// local` | Ladda ner fil |
| `aws s3 sync local s3://` | Synka mapp (inkrementell) |
| `aws s3 mv` | Flytta/byt namn |
| `aws s3 rm` | Ta bort |

```bash
# Ladda upp fil
aws s3 cp myfile.txt s3://my-bucket/folder/

# Ladda ner fil
aws s3 cp s3://my-bucket/folder/myfile.txt ./

# Synka mapp (bara andrade filer)
aws s3 sync ./dist s3://my-bucket/website/

# Ta bort
aws s3 rm s3://my-bucket/old-file.txt
aws s3 rm s3://my-bucket/old-folder/ --recursive
```

------------------------------------------------------------

## Storage Classes

| Klass | Användning | Kostnad |
|-------|------------|---------|
| **Standard** | Frekventa åtkomst | $$$ |
| **Standard-IA** | Sällan åtkomst, snabb hämtning | $$ |
| **Glacier** | Arkiv, minuter till timmar | $ |
| **Glacier Deep Archive** | Långtidsarkiv, 12h hämtning | ¢ |

```bash
# Ladda upp med specifik storage class
aws s3 cp backup.tar.gz s3://my-bucket/ \\
    --storage-class STANDARD_IA

# Flytta till Glacier
aws s3 cp s3://my-bucket/old-backup.tar.gz s3://my-bucket/old-backup.tar.gz \\
    --storage-class GLACIER
```

------------------------------------------------------------

## Presigned URLs

```
+-------------------------------------------------------------+
|                PRESIGNED URL FLOW                           |
+-------------------------------------------------------------+
|                                                             |
|   1. Generera URL med signatur                              |
|      aws s3 presign s3://bucket/private-file.pdf            |
|                                                             |
|   2. URL innehåller:                                        |
|      - Bucket och key                                       |
|      - Utgångstid                                           |
|      - Kryptografisk signatur                               |
|                                                             |
|   3. Dela URL med användare                                 |
|      https://bucket.s3.amazonaws.com/file?                  |
|        X-Amz-Expires=3600&                                  |
|        X-Amz-Signature=abc123...                            |
|                                                             |
|   4. Användare kan ladda ner UTAN AWS credentials           |
|      (Tills URL:en går ut)                                  |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa presigned URL (1 timme)
aws s3 presign s3://my-bucket/private-report.pdf --expires-in 3600

# Output: https://my-bucket.s3.eu-north-1.amazonaws.com/private-report.pdf?
#         X-Amz-Algorithm=AWS4-HMAC-SHA256&
#         X-Amz-Credential=...&
#         X-Amz-Expires=3600&
#         X-Amz-Signature=...
```

------------------------------------------------------------

## Bucket Policy

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

```bash
# Applicera policy
aws s3api put-bucket-policy \\
    --bucket my-website-bucket \\
    --policy file://bucket-policy.json
```

------------------------------------------------------------

## Statisk webbhosting

```bash
# Aktivera static website hosting
aws s3 website s3://my-website-bucket/ \\
    --index-document index.html \\
    --error-document error.html

# Ladda upp webbapp
aws s3 sync ./dist s3://my-website-bucket/

# URL:
# http://my-website-bucket.s3-website.eu-north-1.amazonaws.com
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `BucketAlreadyExists` | Namn upptaget globalt | Lägg till unik suffix |
| `AccessDenied` | Saknar permission | Kolla IAM policy |
| `NoSuchBucket` | Bucket finns inte | Kontrollera namn och region |
| `AllAccessDisabled` | Public access block | Inaktivera block om avsiktligt |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Bucket-namn** | Globalt unika - lägg till suffix |
| **sync** | Inkrementell - bara ändrade filer |
| **presign** | Tillfällig åtkomst utan credentials |
| **Storage Classes** | Välj baserat på åtkomstmönster |
| **Static hosting** | Billigt och enkelt for frontend |

**Kom ihåg:**
- **Bucket-namn är permanenta** - välj klokt
- **sync är smartare än cp** for mappar
- **presign för tillfällig delning** av privata filer
- **Versioning** skyddar mot oavsiktlig borttagning
- **Lifecycle policies** för automatisk arkivering
""",
        },
        {
            "title": "RDS - Relational Database Service",
            "slug": "rds-relational-database-service",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# RDS - Relational Database Service

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor RDS-kunskap ar kritisk |
|----------|-------------------------------|
| **Managed DB** | Slipper installera, patcha, säkerhetskopiera |
| **High Availability** | Multi-AZ for automatisk failover |
| **Skalning** | Ändra instanstyp utan dataförlust |
| **Backup/Restore** | Point-in-time recovery |
| **Säkerhet** | Kryptering, VPC isolation |

RDS ar managed database service. Du valjer motor och storlek - AWS sköter resten.

------------------------------------------------------------

## RDS Arkitektur

```
+-------------------------------------------------------------+
|                    RDS MULTI-AZ                             |
+-------------------------------------------------------------+
|                                                             |
|   +---------------------------------------------------+     |
|   |                     VPC                           |     |
|   |  +-----------------+    +-----------------+      |     |
|   |  |  Private Subnet |    |  Private Subnet |      |     |
|   |  |    AZ-a         |    |    AZ-b         |      |     |
|   |  |                 |    |                 |      |     |
|   |  |  +-----------+  |    |  +-----------+  |      |     |
|   |  |  |  PRIMARY  |◄-+----+-►|  STANDBY  |  |      |     |
|   |  |  |  (Read/   |  |sync|  |  (Passive)|  |      |     |
|   |  |  |   Write)  |  |    |  |           |  |      |     |
|   |  |  +-----------+  |    |  +-----------+  |      |     |
|   |  +-----------------+    +-----------------+      |     |
|   |                                                   |     |
|   |  App ansluter via ENDPOINT                        |     |
|   |  Vid failover: Endpoint pekar automatiskt         |     |
|   |  på ny primary (30-60 sekunder)                   |     |
|   |                                                   |     |
|   +---------------------------------------------------+     |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Databasmotorer

| Motor | Användning | Free Tier |
|-------|------------|-----------|
| **PostgreSQL** | Modern, feature-rich | db.t3.micro |
| **MySQL** | Populär, bred support | db.t3.micro |
| **MariaDB** | MySQL-fork, community | db.t3.micro |
| **Aurora** | AWS-optimerad, 5x snabbare | Nej |
| **SQL Server** | Microsoft-ekosystem | db.t3.small |
| **Oracle** | Enterprise, legacy | Nej |

------------------------------------------------------------

## Skapa RDS-instans

```bash
# 1. Skapa subnet group forst
aws rds create-db-subnet-group \\
    --db-subnet-group-name prod-db-subnets \\
    --db-subnet-group-description "Private subnets for RDS" \\
    --subnet-ids subnet-private-1a subnet-private-1b

# 2. Skapa databas
aws rds create-db-instance \\
    --db-instance-identifier prod-postgres \\
    --db-instance-class db.t3.micro \\
    --engine postgres \\
    --engine-version 15.4 \\
    --master-username admin \\
    --master-user-password SecretPass123! \\
    --allocated-storage 20 \\
    --vpc-security-group-ids sg-db-access \\
    --db-subnet-group-name prod-db-subnets \\
    --backup-retention-period 7 \\
    --multi-az \\
    --no-publicly-accessible

# 3. Vänta på att databasen blir tillgänglig (5-15 min)
aws rds wait db-instance-available \\
    --db-instance-identifier prod-postgres
```

------------------------------------------------------------

## Backup och Restore

```
+-------------------------------------------------------------+
|                   RDS BACKUP TYPER                          |
+-------------------------------------------------------------+
|                                                             |
|   AUTOMATISKA BACKUPS              MANUELLA SNAPSHOTS       |
|   -------------------              -----------------        |
|   - Dagliga under backup window    - Du skapar manuellt     |
|   - Retention: 1-35 dagar          - Finns tills du tar bort|
|   - Point-in-time recovery         - Fullständig kopia      |
|   - Tas bort med instansen         - Finns efter deletion   |
|                                                             |
|   POINT-IN-TIME RECOVERY:                                   |
|   +-----+  +-----+  +-----+  +-----+                       |
|   | 00:00|--| 06:00|--| 12:00|--| Nu  |                     |
|   +-----+  +-----+  +-----+  +-----+                       |
|   Kan återställa till vilken tidpunkt som helst            |
|   inom retention-perioden (med 5 min precision)            |
|                                                             |
+-------------------------------------------------------------+
```

| Kommando | Beskrivning |
|----------|-------------|
| `create-db-snapshot` | Manuell snapshot |
| `describe-db-snapshots` | Lista snapshots |
| `restore-db-instance-from-db-snapshot` | Återställ till NY instans |
| `restore-db-instance-to-point-in-time` | Point-in-time recovery |

```bash
# Skapa snapshot fore stor andring
aws rds create-db-snapshot \\
    --db-instance-identifier prod-postgres \\
    --db-snapshot-identifier prod-postgres-before-migration

# Återställ fran snapshot (skapar NY instans)
aws rds restore-db-instance-from-db-snapshot \\
    --db-instance-identifier prod-postgres-restored \\
    --db-snapshot-identifier prod-postgres-before-migration
```

------------------------------------------------------------

## Skalning

| Typ | Hur | Downtime |
|-----|-----|----------|
| **Vertikal** | Ändra instanstyp | Ja (minuter) |
| **Storage** | Öka allocated-storage | Nej |
| **Read Replicas** | Lägg till read-only kopior | Nej |

```bash
# Skala upp instanstyp (kräver omstart)
aws rds modify-db-instance \\
    --db-instance-identifier prod-postgres \\
    --db-instance-class db.t3.medium \\
    --apply-immediately

# Öka storage (ingen downtime)
aws rds modify-db-instance \\
    --db-instance-identifier prod-postgres \\
    --allocated-storage 100 \\
    --apply-immediately

# Skapa read replica
aws rds create-db-instance-read-replica \\
    --db-instance-identifier prod-postgres-read \\
    --source-db-instance-identifier prod-postgres
```

------------------------------------------------------------

## Anslutning

```bash
# Hämta endpoint
aws rds describe-db-instances \\
    --db-instance-identifier prod-postgres \\
    --query "DBInstances[0].Endpoint.Address" \\
    --output text
# prod-postgres.abc123.eu-north-1.rds.amazonaws.com

# Anslut med psql
psql -h prod-postgres.abc123.eu-north-1.rds.amazonaws.com \\
    -U admin -d postgres
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Cannot connect` | Security Group blockerar | Öppna port 5432/3306 |
| `Subnet group not found` | Saknar subnet group | Skapa med minst 2 AZs |
| `Storage full` | Disk slut | Öka allocated-storage |
| `Too many connections` | Applikation läcker | Connection pooling |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Managed** | AWS sköter patching, backups, failover |
| **Multi-AZ** | Automatisk failover - obligatoriskt for prod |
| **Subnet Groups** | Minst 2 AZs kravs |
| **Snapshots** | Ta fore stora andringar |
| **Security Groups** | Begränsa till app-servrar |

**Kom ihåg:**
- **Aldrig publicly accessible** for produktionsdatabaser
- **Multi-AZ** kostar dubbelt men ar värt det
- **Point-in-time recovery** räddar dig vid dataförlust
- **Parameter Groups** for att tweaka databasinställningar
- **Endpoint ändras inte** vid failover
""",
        },
        {
            "title": "ECS - Elastic Container Service",
            "slug": "ecs-elastic-container-service",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 95,
            "content": """# ECS - Elastic Container Service

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor ECS-kunskap ar kritisk |
|----------|-------------------------------|
| **Container orchestration** | Kor Docker i produktion |
| **Microservices** | Varje service i egen container |
| **CI/CD** | Automatiserade deployments |
| **Skalning** | Auto-scale baserat pa metrics |
| **Kostnad** | Fargate = betala per container |

ECS ar AWS managed container orchestration. Med Fargate slipper du hantera servrar - AWS kör dina containers.

------------------------------------------------------------

## ECS Komponenter

```
+-------------------------------------------------------------+
|                    ECS ARKITEKTUR                           |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------------------------------------------+   |
|   |                    CLUSTER                          |   |
|   |              (Logisk gruppering)                    |   |
|   |                                                     |   |
|   |   +---------------------------------------------+   |   |
|   |   |                SERVICE                      |   |   |
|   |   |   (Underhåller desired count av tasks)     |   |   |
|   |   |                                             |   |   |
|   |   |   +---------+  +---------+  +---------+   |   |   |
|   |   |   |  TASK   |  |  TASK   |  |  TASK   |   |   |   |
|   |   |   |         |  |         |  |         |   |   |   |
|   |   |   |+-------+|  |+-------+|  |+-------+|   |   |   |
|   |   |   || nginx ||  || nginx ||  || nginx ||   |   |   |
|   |   |   |+-------+|  |+-------+|  |+-------+|   |   |   |
|   |   |   +---------+  +---------+  +---------+   |   |   |
|   |   |                                             |   |   |
|   |   +---------------------------------------------+   |   |
|   +-----------------------------------------------------+   |
|                                                             |
|   TASK DEFINITION = Blueprint (image, cpu, memory, ports)  |
|                                                             |
+-------------------------------------------------------------+
```

| Komponent | Beskrivning |
|-----------|-------------|
| **Cluster** | Logisk gruppering av resurser |
| **Task Definition** | Blueprint for hur containers körs |
| **Task** | Körande instans av task definition |
| **Service** | Kör och underhåller önskat antal tasks |

------------------------------------------------------------

## Launch Types

| Typ | Beskrivning | Användning |
|-----|-------------|------------|
| **Fargate** | Serverless, AWS hanterar servers | Enklast, betala per task |
| **EC2** | Du hanterar EC2-instanser | Mer kontroll, reserved capacity |

------------------------------------------------------------

## Skapa Cluster och Task Definition

```bash
# Skapa cluster
aws ecs create-cluster --cluster-name prod-cluster

# Task definition (task-def.json)
{
    "family": "web-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
    "containerDefinitions": [{
        "name": "web",
        "image": "nginx:latest",
        "essential": true,
        "portMappings": [{"containerPort": 80}],
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "/ecs/web-app",
                "awslogs-region": "eu-north-1",
                "awslogs-stream-prefix": "ecs"
            }
        }
    }]
}

# Registrera task definition
aws ecs register-task-definition --cli-input-json file://task-def.json
```

------------------------------------------------------------

## Skapa Service

```bash
# Skapa service med 2 tasks
aws ecs create-service \\
    --cluster prod-cluster \\
    --service-name web-service \\
    --task-definition web-app:1 \\
    --desired-count 2 \\
    --launch-type FARGATE \\
    --network-configuration "awsvpcConfiguration={subnets=[subnet-1,subnet-2],securityGroups=[sg-xxx],assignPublicIp=ENABLED}"

# Kolla status
aws ecs describe-services \\
    --cluster prod-cluster \\
    --services web-service
```

------------------------------------------------------------

## Deployment och Skalning

```
+-------------------------------------------------------------+
|              ROLLING DEPLOYMENT                             |
+-------------------------------------------------------------+
|                                                             |
|   Före:     [v1] [v1] [v1]                                 |
|                                                             |
|   Steg 1:   [v1] [v1] [v1] [v2]     <- Starta ny task       |
|                                                             |
|   Steg 2:   [v1] [v1] [v2] [v2]     <- v2 healthy, stoppa v1|
|                                                             |
|   Steg 3:   [v1] [v2] [v2] [v2]     <- Fortsätt...          |
|                                                             |
|   Efter:    [v2] [v2] [v2]           <- Klart!              |
|                                                             |
|   ZERO DOWNTIME - ALB skickar bara trafik till healthy     |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Deploy ny version
aws ecs update-service \\
    --cluster prod-cluster \\
    --service-name web-service \\
    --task-definition web-app:2

# Skala upp
aws ecs update-service \\
    --cluster prod-cluster \\
    --service-name web-service \\
    --desired-count 5

# Skala ner till 0 (stoppa)
aws ecs update-service \\
    --cluster prod-cluster \\
    --service-name web-service \\
    --desired-count 0
```

------------------------------------------------------------

## ECR - Container Registry

```bash
# Skapa repository
aws ecr create-repository --repository-name my-app

# Logga in Docker mot ECR
aws ecr get-login-password | docker login \\
    --username AWS \\
    --password-stdin 123456789012.dkr.ecr.eu-north-1.amazonaws.com

# Tagga och pusha image
docker tag my-app:latest 123456789012.dkr.ecr.eu-north-1.amazonaws.com/my-app:latest
docker push 123456789012.dkr.ecr.eu-north-1.amazonaws.com/my-app:latest
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Task failed to start` | Image pull error | Kontrollera ECR permissions |
| `Service stuck deploying` | Health check failed | Kolla ALB target group |
| `ResourceInitializationError` | ENI/subnet problem | Kontrollera VPC config |
| `OutOfMemory` | Container använder for mycket | Öka memory i task def |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Fargate** | Serverless containers - enklast |
| **Task Definition** | Blueprint - versioneras automatiskt |
| **Service** | Underhåller desired count |
| **Rolling deployment** | Zero-downtime updates |
| **ECR** | Privat container registry |

**Kom ihåg:**
- **Fargate for enkel start** - ingen serverhantering
- **Task definitions är immutable** - ny revision vid ändring
- **Logga till CloudWatch** - awslogs driver
- **ECR + ECS** integrerat med IAM
- **desired-count 0** for att stoppa utan att ta bort
""",
        },
        {
            "title": "EKS - Elastic Kubernetes Service",
            "slug": "eks-elastic-kubernetes-service",
            "difficulty": "advanced",
            "estimated_minutes": 65,
            "xp_reward": 100,
            "content": """# EKS - Elastic Kubernetes Service

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor EKS-kunskap ar kritisk |
|----------|-------------------------------|
| **Container orchestration** | Kubernetes i produktion |
| **Multi-cloud** | Kubernetes är portabelt |
| **Microservices** | Komplex service mesh |
| **Skalning** | Horizontal Pod Autoscaler |
| **GitOps** | ArgoCD, Flux integration |

EKS ar AWS managed Kubernetes. Du far kraften av Kubernetes utan att hantera control plane.

------------------------------------------------------------

## EKS Arkitektur

```
+-------------------------------------------------------------+
|                    EKS ARKITEKTUR                           |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------------------------------------------+   |
|   |              AWS MANAGED                            |   |
|   |  +------------------------------------------------+ |   |
|   |  |           CONTROL PLANE                        | |   |
|   |  |  +----------+ +----------+ +----------+       | |   |
|   |  |  |API Server| |  etcd    | |Scheduler |       | |   |
|   |  |  +----------+ +----------+ +----------+       | |   |
|   |  |         Multi-AZ, HA                           | |   |
|   |  +------------------------------------------------+ |   |
|   +-----------------------------------------------------+   |
|                            |                                |
|                            | kubectl                        |
|                            ▼                                |
|   +-----------------------------------------------------+   |
|   |              DU HANTERAR                            |   |
|   |  +------------------------------------------------+ |   |
|   |  |           WORKER NODES                         | |   |
|   |  |  +---------+  +---------+  +---------+       | |   |
|   |  |  |   Pod   |  |   Pod   |  |   Pod   |       | |   |
|   |  |  |+-------+|  |+-------+|  |+-------+|       | |   |
|   |  |  || nginx ||  ||  api  ||  ||  db   ||       | |   |
|   |  |  |+-------+|  |+-------+|  |+-------+|       | |   |
|   |  |  +---------+  +---------+  +---------+       | |   |
|   |  |         EC2 eller Fargate                     | |   |
|   |  +------------------------------------------------+ |   |
|   +-----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa EKS Cluster

```bash
# Med eksctl (rekommenderat)
eksctl create cluster \\
    --name prod-cluster \\
    --region eu-north-1 \\
    --version 1.28 \\
    --nodegroup-name workers \\
    --node-type t3.medium \\
    --nodes 2 \\
    --nodes-min 1 \\
    --nodes-max 5

# Tar 15-20 minuter
# Skapar VPC, subnets, IAM roles automatiskt
```

------------------------------------------------------------

## Konfigurera kubectl

```bash
# Uppdatera kubeconfig
aws eks update-kubeconfig --name prod-cluster --region eu-north-1

# Verifiera anslutning
kubectl get nodes
kubectl cluster-info
```

------------------------------------------------------------

## Node Groups

| Typ | Beskrivning | Användning |
|-----|-------------|------------|
| **Managed** | AWS hanterar scaling | Standard |
| **Self-managed** | Du hanterar EC2 | Specialkrav |
| **Fargate** | Serverless pods | Per-pod billing |
| **Spot** | 90% rabatt, kan tas tillbaka | Batch jobs |

```bash
# Skapa spot node group
eksctl create nodegroup \\
    --cluster prod-cluster \\
    --name spot-workers \\
    --node-type t3.large \\
    --nodes 3 \\
    --spot

# Skala node group
eksctl scale nodegroup \\
    --cluster prod-cluster \\
    --name workers \\
    --nodes 5
```

------------------------------------------------------------

## Deploy Application

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
  - port: 80
```

```bash
kubectl apply -f deployment.yaml
kubectl get svc web-service
# EXTERNAL-IP ar AWS ELB DNS-namn
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Unauthorized` | IAM/kubeconfig fel | aws eks update-kubeconfig |
| `No nodes available` | Node group tom | Skala upp eller fixa ASG |
| `ImagePullBackOff` | Kan inte dra image | Kontrollera ECR permissions |
| `Pending pods` | Resursbrist | Skala nodes eller minska requests |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Managed control plane** | AWS sköter master nodes |
| **eksctl** | Enklaste sättet att skapa cluster |
| **Node groups** | Olika typer for olika workloads |
| **IRSA** | IAM Roles for Service Accounts |
| **ALB Controller** | AWS-native ingress |

**Kom ihåg:**
- **eksctl** ar enklast for att komma igång
- **Fargate** for serverless pods
- **Spot instances** for kostnadsbesparingar
- **IRSA** for säker IAM-integration
- **Cluster Autoscaler** for dynamisk skalning
""",
        },
        {
            "title": "Lambda - Serverless Functions",
            "slug": "lambda-serverless-functions",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Lambda - Serverless Functions

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Lambda-kunskap ar kritisk |
|----------|----------------------------------|
| **Event-driven** | Triggas av S3, SQS, API Gateway |
| **Kostnadseffektivt** | Betala bara nar kod kors |
| **Skalning** | Automatisk 0 till tusentals |
| **CI/CD automation** | Trigger vid deployments |
| **Microservices** | Sma fokuserade funktioner |

Lambda ar serverless compute - kor kod utan att hantera servrar.

------------------------------------------------------------

## Lambda Arkitektur

```
+-------------------------------------------------------------+
|                   LAMBDA ARKITEKTUR                         |
+-------------------------------------------------------------+
|                                                             |
|   +-------------+    +-------------+    +-------------+    |
|   |     S3      |    | API Gateway |    |    SQS      |    |
|   |   (event)   |    |  (request)  |    |  (message)  |    |
|   +------+------+    +------+------+    +------+------+    |
|          |                  |                  |            |
|          +------------------+------------------+            |
|                             |                               |
|                             ▼                               |
|   +-----------------------------------------------------+   |
|   |                    LAMBDA                           |   |
|   |  +---------------------------------------------+   |   |
|   |  |              Execution Environment          |   |   |
|   |  |  +----------+  +----------+  +----------+ |   |   |
|   |  |  | Handler  |  |  Memory  |  |  /tmp    | |   |   |
|   |  |  | function |  | 128MB-   |  |  512MB   | |   |   |
|   |  |  |          |  |  10GB    |  | storage  | |   |   |
|   |  |  +----------+  +----------+  +----------+ |   |   |
|   |  |         Max 15 min timeout                   |   |   |
|   |  +---------------------------------------------+   |   |
|   +-----------------------------------------------------+   |
|                             |                               |
|                             ▼                               |
|   +-----------------------------------------------------+   |
|   |  Response / CloudWatch Logs / Dead Letter Queue    |   |
|   +-----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Lambda Funktion

```python
# lambda_function.py
import json

def lambda_handler(event, context):
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}!'})
    }
```

```bash
# Paketera och skapa
zip function.zip lambda_function.py

aws lambda create-function \\
    --function-name my-hello-function \\
    --runtime python3.11 \\
    --role arn:aws:iam::123456789012:role/lambda-role \\
    --handler lambda_function.lambda_handler \\
    --zip-file fileb://function.zip
```

------------------------------------------------------------

## Testa och Anropa

| Kommando | Beskrivning |
|----------|-------------|
| `invoke --invocation-type RequestResponse` | Synkront - vantar pa svar |
| `invoke --invocation-type Event` | Asynkront - returnerar direkt |
| `invoke --log-type Tail` | Inkludera loggar i response |

```bash
# Synkront anrop
aws lambda invoke \\
    --function-name my-hello-function \\
    --payload '{"name": "DevOps"}' \\
    --cli-binary-format raw-in-base64-out \\
    response.json

cat response.json
# {"message": "Hello, DevOps!"}

# Asynkront anrop
aws lambda invoke \\
    --function-name my-hello-function \\
    --invocation-type Event \\
    --payload '{"name": "Async"}' \\
    response.json
# Returnerar 202 Accepted
```

------------------------------------------------------------

## Versioner och Alias

```
+-------------------------------------------------------------+
|                  VERSION WORKFLOW                           |
+-------------------------------------------------------------+
|                                                             |
|   $LATEST -------------► Version 1                         |
|      |                       |                              |
|      |                       |                              |
|      +--(publish)--► Version 2 ◄----- [prod alias]         |
|                          |                                  |
|                          |                                  |
|                    Version 3 ◄----- [dev alias]            |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Publicera version
aws lambda publish-version \\
    --function-name my-hello-function \\
    --description "Release v1.0"

# Skapa alias
aws lambda create-alias \\
    --function-name my-hello-function \\
    --name prod \\
    --function-version 1

# Uppdatera alias till ny version
aws lambda update-alias \\
    --function-name my-hello-function \\
    --name prod \\
    --function-version 2
```

------------------------------------------------------------

## Konfiguration

```bash
# Miljövariabler
aws lambda update-function-configuration \\
    --function-name my-hello-function \\
    --environment "Variables={DB_HOST=mydb.example.com,API_KEY=secret}"

# Minne och timeout
aws lambda update-function-configuration \\
    --function-name my-hello-function \\
    --memory-size 512 \\
    --timeout 30
```

| Parameter | Min | Max | Default |
|-----------|-----|-----|---------|
| **Memory** | 128 MB | 10 GB | 128 MB |
| **Timeout** | 1 sek | 15 min | 3 sek |
| **Ephemeral storage** | 512 MB | 10 GB | 512 MB |

------------------------------------------------------------

## Event Sources

```bash
# S3 trigger permission
aws lambda add-permission \\
    --function-name my-hello-function \\
    --statement-id s3-trigger \\
    --action lambda:InvokeFunction \\
    --principal s3.amazonaws.com \\
    --source-arn arn:aws:s3:::my-bucket

# SQS event source mapping
aws lambda create-event-source-mapping \\
    --function-name my-hello-function \\
    --event-source-arn arn:aws:sqs:eu-north-1:123456789012:my-queue \\
    --batch-size 10
```

| Event Source | Typ | Polling |
|--------------|-----|---------|
| **S3** | Push | Nej - S3 anropar Lambda |
| **API Gateway** | Push | Nej - synkront |
| **SQS** | Poll | Ja - Lambda pollar |
| **DynamoDB Streams** | Poll | Ja - Lambda pollar |
| **SNS** | Push | Nej - SNS anropar |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Task timed out` | Koden tar for lang tid | Oka timeout eller optimera |
| `Out of memory` | For lite minne | Oka memory-size |
| `Permission denied` | IAM role saknar rattigheter | Lagg till IAM policy |
| `Module not found` | Dependency saknas | Inkludera i zip/layer |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Pay per use** | Faktureras per millisekund |
| **Auto-scaling** | 0 till tusentals samtidigt |
| **Versioner** | Immutable snapshots av kod |
| **Alias** | Pekare till version (dev/prod) |
| **Layers** | Delade dependencies |

**Kom ihåg:**
- **Cold start** - forsta anropet tar langre tid
- **Versioner for rollback** - publicera innan prod
- **Alias for deployments** - byt version utan andrad ARN
- **Mer minne = mer CPU** - snabbare exekvering
- **Max 15 min timeout** - ej for langa jobb
""",
        },
        {
            "title": "API Gateway - REST och HTTP APIs",
            "slug": "api-gateway-rest-http-apis",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# API Gateway - REST och HTTP APIs

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor API Gateway-kunskap ar kritisk |
|----------|---------------------------------------|
| **Microservices** | Unified entry point |
| **Serverless** | Lambda-integration |
| **Sakerhet** | Auth, throttling, WAF |
| **Multi-platform** | Webb, mobil, IoT |
| **Monitoring** | Request metrics och logging |

API Gateway ar managed service for att skapa, publicera och hantera APIs.

------------------------------------------------------------

## API Gateway Arkitektur

```
+-------------------------------------------------------------+
|                  API GATEWAY FLOW                           |
+-------------------------------------------------------------+
|                                                             |
|   +---------+    +---------+    +---------+               |
|   |  Web    |    | Mobile  |    |  IoT    |               |
|   |  App    |    |  App    |    | Device  |               |
|   +----+----+    +----+----+    +----+----+               |
|        |              |              |                     |
|        +--------------+--------------+                     |
|                       |                                    |
|                       ▼                                    |
|   +-----------------------------------------------------+  |
|   |              API GATEWAY                            |  |
|   |  +----------+ +----------+ +----------+           |  |
|   |  |   Auth   | | Throttle | |  Cache   |           |  |
|   |  +----------+ +----------+ +----------+           |  |
|   |  +------------------------------------+           |  |
|   |  |   Routes: /users, /orders, /api    |           |  |
|   |  +------------------------------------+           |  |
|   +-----------------------------------------------------+  |
|                       |                                    |
|        +--------------+--------------+                    |
|        ▼              ▼              ▼                    |
|   +---------+    +---------+    +---------+              |
|   | Lambda  |    |   EC2   |    |   ECS   |              |
|   |Function |    | Backend |    | Service |              |
|   +---------+    +---------+    +---------+              |
|                                                           |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## HTTP API vs REST API

| Feature | HTTP API | REST API |
|---------|----------|----------|
| **Kostnad** | 70% billigare | Hogre |
| **Latens** | Lagre | Hogre |
| **Features** | Grundlaggande | Alla |
| **Caching** | Nej | Ja |
| **Request validation** | Nej | Ja |
| **Rekommendation** | Default val | Avancerade behov |

------------------------------------------------------------

## Skapa HTTP API

```bash
# Skapa HTTP API med Lambda target
aws apigatewayv2 create-api \\
    --name my-http-api \\
    --protocol-type HTTP \\
    --target arn:aws:lambda:eu-north-1:123456789012:function:my-function

# Lista APIs
aws apigatewayv2 get-apis

# Testa
curl https://abc123.execute-api.eu-north-1.amazonaws.com/
```

------------------------------------------------------------

## Routes och Integrationer

```bash
# Skapa Lambda integration
aws apigatewayv2 create-integration \\
    --api-id abc123 \\
    --integration-type AWS_PROXY \\
    --integration-uri arn:aws:lambda:eu-north-1:123456789012:function:users \\
    --payload-format-version 2.0

# Skapa route
aws apigatewayv2 create-route \\
    --api-id abc123 \\
    --route-key "GET /users" \\
    --target integrations/int123

# Skapa POST route till samma Lambda
aws apigatewayv2 create-route \\
    --api-id abc123 \\
    --route-key "POST /users" \\
    --target integrations/int123
```

| Route Key | Beskrivning |
|-----------|-------------|
| `GET /users` | Lista användare |
| `POST /users` | Skapa användare |
| `GET /users/{id}` | Hämta specifik |
| `$default` | Catch-all route |

------------------------------------------------------------

## Stages

```
+-------------------------------------------------------------+
|                    STAGE WORKFLOW                           |
+-------------------------------------------------------------+
|                                                             |
|   API Config --► deploy --► dev stage (auto-deploy)        |
|       |                                                     |
|       +-------► deploy --► prod stage (manual)             |
|                                                             |
|   URLs:                                                     |
|   - https://abc123.../dev/users                            |
|   - https://abc123.../prod/users                           |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Dev stage med auto-deploy
aws apigatewayv2 create-stage \\
    --api-id abc123 \\
    --stage-name dev \\
    --auto-deploy

# Prod stage utan auto-deploy
aws apigatewayv2 create-stage \\
    --api-id abc123 \\
    --stage-name prod

# Manuell deployment till prod
aws apigatewayv2 create-deployment \\
    --api-id abc123 \\
    --stage-name prod
```

------------------------------------------------------------

## Throttling och CORS

```bash
# Satt throttling
aws apigatewayv2 update-stage \\
    --api-id abc123 \\
    --stage-name prod \\
    --default-route-settings '{"ThrottlingBurstLimit": 100, "ThrottlingRateLimit": 50}'

# Konfigurera CORS
aws apigatewayv2 update-api \\
    --api-id abc123 \\
    --cors-configuration '{
        "AllowOrigins": ["https://example.com"],
        "AllowMethods": ["GET", "POST"],
        "AllowHeaders": ["Authorization", "Content-Type"]
    }'
```

| Setting | Beskrivning |
|---------|-------------|
| **BurstLimit** | Max samtidiga requests |
| **RateLimit** | Requests per sekund |
| **AllowOrigins** | CORS - tillåtna domäner |

------------------------------------------------------------

## JWT Authorizer

```bash
# Skapa JWT authorizer med Cognito
aws apigatewayv2 create-authorizer \\
    --api-id abc123 \\
    --authorizer-type JWT \\
    --identity-source '$request.header.Authorization' \\
    --name cognito-auth \\
    --jwt-configuration '{
        "Audience": ["my-app-client-id"],
        "Issuer": "https://cognito-idp.eu-north-1.amazonaws.com/pool-id"
    }'

# Koppla authorizer till route
aws apigatewayv2 update-route \\
    --api-id abc123 \\
    --route-id routeId \\
    --authorization-type JWT \\
    --authorizer-id authId
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **HTTP API** | Valj for de flesta fall |
| **Routes** | Map URL paths till backends |
| **Stages** | Separera dev/staging/prod |
| **Throttling** | Skydda backend mot overbelastning |
| **JWT Auth** | Cognito eller annan IdP |

**Kom ihåg:**
- **HTTP API for 70% lagre kostnad**
- **Auto-deploy for dev** - snabbare iteration
- **Manuell deploy for prod** - kontroll
- **Throttling alltid** - skydda backend
- **CORS for webb** - maste konfigureras
""",
        },
        {
            "title": "CloudWatch - Monitoring och Logging",
            "slug": "cloudwatch-monitoring-logging",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# CloudWatch - Monitoring och Logging

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor CloudWatch-kunskap ar kritisk |
|----------|--------------------------------------|
| **Observability** | Se vad som hander i systemet |
| **Troubleshooting** | Hitta och losa problem snabbt |
| **Alerting** | Fa veta innan anvandare klagar |
| **Compliance** | Audit trails och loggarkivering |
| **Cost optimization** | Identifiera overanvandning |

CloudWatch ar AWS centrala monitoring-tjanst for loggar, metrics och alarms.

------------------------------------------------------------

## CloudWatch Komponenter

```
+-------------------------------------------------------------+
|                  CLOUDWATCH OVERSIKT                        |
+-------------------------------------------------------------+
|                                                             |
|   +-------------+  +-------------+  +-------------+       |
|   |    LOGS     |  |   METRICS   |  |   ALARMS    |       |
|   |             |  |             |  |             |       |
|   | Log Groups  |  | Namespaces  |  | Thresholds  |       |
|   | Log Streams |  | Dimensions  |  | Actions     |       |
|   | Insights    |  | Statistics  |  | SNS/Lambda  |       |
|   +------+------+  +------+------+  +------+------+       |
|          |                |                |              |
|          +----------------+----------------+              |
|                           |                               |
|                           ▼                               |
|   +-----------------------------------------------------+ |
|   |                   DASHBOARDS                        | |
|   |   Visualisera metrics, loggar och alarms           | |
|   +-----------------------------------------------------+ |
|                                                           |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## CloudWatch Logs

```bash
# Skapa log group
aws logs create-log-group --log-group-name /app/my-service

# Satt retention (sparar pengar!)
aws logs put-retention-policy \\
    --log-group-name /app/my-service \\
    --retention-in-days 30

# Lista log streams
aws logs describe-log-streams \\
    --log-group-name /app/my-service \\
    --order-by LastEventTime \\
    --descending

# Hamta loggar
aws logs get-log-events \\
    --log-group-name /app/my-service \\
    --log-stream-name i-abc123 \\
    --limit 50
```

| Retention | Anvandning |
|-----------|------------|
| **7 dagar** | Dev/test |
| **30 dagar** | Standard produktion |
| **90 dagar** | Compliance |
| **365 dagar** | Audit requirements |

------------------------------------------------------------

## Logs Insights

```bash
# Starta query
aws logs start-query \\
    --log-group-name /app/my-service \\
    --start-time $(date -d '1 hour ago' +%s) \\
    --end-time $(date +%s) \\
    --query-string 'fields @timestamp, @message | filter @message like /ERROR/ | limit 20'

# Hamta resultat
aws logs get-query-results --query-id abc123

# Folja loggar i realtid
aws logs tail /app/my-service --follow
```

| Query Syntax | Beskrivning |
|--------------|-------------|
| `fields @timestamp, @message` | Valj falt |
| `filter @message like /ERROR/` | Filtrera |
| `sort @timestamp desc` | Sortera |
| `limit 20` | Begransa resultat |
| `stats count(*) by bin(1h)` | Aggregera |

------------------------------------------------------------

## CloudWatch Metrics

```bash
# Lista metrics
aws cloudwatch list-metrics \\
    --namespace AWS/EC2 \\
    --metric-name CPUUtilization

# Hamta statistik
aws cloudwatch get-metric-statistics \\
    --namespace AWS/EC2 \\
    --metric-name CPUUtilization \\
    --dimensions Name=InstanceId,Value=i-abc123 \\
    --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ) \\
    --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) \\
    --period 300 \\
    --statistics Average

# Publicera custom metric
aws cloudwatch put-metric-data \\
    --namespace Custom/MyApp \\
    --metric-name RequestLatency \\
    --value 150 \\
    --unit Milliseconds \\
    --dimensions Service=UserAPI
```

| Namespace | Tjanst |
|-----------|--------|
| `AWS/EC2` | EC2 instanser |
| `AWS/RDS` | Databaser |
| `AWS/Lambda` | Lambda funktioner |
| `AWS/ECS` | Containers |
| `Custom/MyApp` | Egna metrics |

------------------------------------------------------------

## CloudWatch Alarms

```
+-------------------------------------------------------------+
|                    ALARM STATES                             |
+-------------------------------------------------------------+
|                                                             |
|   +------------+        +------------+                     |
|   |     OK     |◄------►|   ALARM    |                     |
|   |            |        |            |                     |
|   | CPU < 80%  |        | CPU > 80%  |--► SNS --► Email   |
|   +------------+        +------------+           Lambda   |
|         |                     |                 Auto Scale|
|         |                     |                            |
|         ▼                     ▼                            |
|   +------------------------------------+                  |
|   |        INSUFFICIENT_DATA           |                  |
|   |      (Ingen data annu)             |                  |
|   +------------------------------------+                  |
|                                                           |
+-------------------------------------------------------------+
```

```bash
# Skapa alarm
aws cloudwatch put-metric-alarm \\
    --alarm-name high-cpu-alarm \\
    --metric-name CPUUtilization \\
    --namespace AWS/EC2 \\
    --dimensions Name=InstanceId,Value=i-abc123 \\
    --statistic Average \\
    --period 300 \\
    --threshold 80 \\
    --comparison-operator GreaterThanThreshold \\
    --evaluation-periods 2 \\
    --alarm-actions arn:aws:sns:eu-north-1:123456789012:alerts

# Lista alarms
aws cloudwatch describe-alarms

# Disable alarm actions (for maintenance)
aws cloudwatch disable-alarm-actions --alarm-names high-cpu-alarm
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Log Groups** | Organisera per app/tjanst |
| **Retention** | Satt policy - sparar pengar |
| **Logs Insights** | SQL-liknande sokning |
| **Custom Metrics** | Skicka fran din kod |
| **Alarms** | Proaktiv alerting via SNS |

**Kom ihåg:**
- **Satt retention** - default ar obegransat och dyrt
- **Logs Insights** for komplex sokning
- **Custom metrics** for app-specifika data
- **Alarm actions** - SNS for email/SMS
- **Dashboard** for visualisering
""",
        },
        {
            "title": "CloudFormation - Infrastructure as Code",
            "slug": "cloudformation-infrastructure-as-code",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 95,
            "content": """# CloudFormation - Infrastructure as Code

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor CloudFormation-kunskap ar kritisk |
|----------|------------------------------------------|
| **IaC** | Versionskontrollera infrastruktur |
| **Reproducerbarhet** | Samma template = samma resultat |
| **Automation** | CI/CD for infra |
| **Compliance** | Drift detection |
| **Rollback** | Automatisk vid fel |

CloudFormation ar AWS native IaC for att definiera och provisionera resurser.

------------------------------------------------------------

## CloudFormation Workflow

```
+-------------------------------------------------------------+
|                CLOUDFORMATION WORKFLOW                      |
+-------------------------------------------------------------+
|                                                             |
|   +-------------+    +-------------+    +-------------+   |
|   |  Template   |---►| Change Set  |---►|   Stack     |   |
|   |  (YAML)     |    |  (Preview)  |    |  (Deploy)   |   |
|   +-------------+    +-------------+    +-------------+   |
|         |                                      |           |
|         |                                      ▼           |
|         |                              +-------------+    |
|         |                              |  Resources  |    |
|         |                              | EC2, S3,    |    |
|         |                              | RDS, etc    |    |
|         |                              +-------------+    |
|         |                                      |           |
|         ▼                                      ▼           |
|   +---------------------------------------------------+   |
|   |                   Git Repository                  |   |
|   |           Version control templates               |   |
|   +---------------------------------------------------+   |
|                                                           |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Template Struktur

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Min infrastruktur

Parameters:
  Environment:
    Type: String
    Default: dev
    AllowedValues: [dev, staging, prod]

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub 'app-data-bucket'
      VersioningConfiguration:
        Status: Enabled

Outputs:
  BucketArn:
    Value: !GetAtt MyBucket.Arn
    Export:
      Name: !Sub 'BucketArn'
```

| Sektion | Beskrivning |
|---------|-------------|
| **Parameters** | Input-variabler |
| **Resources** | AWS-resurser att skapa |
| **Outputs** | Export-varden |
| **Mappings** | Lookup-tabeller |
| **Conditions** | Villkorlig logik |

------------------------------------------------------------

## Skapa och Hantera Stacks

```bash
# Skapa stack
aws cloudformation create-stack \\
    --stack-name my-app \\
    --template-body file://template.yaml \\
    --parameters ParameterKey=Environment,ParameterValue=prod

# Vanta tills klar
aws cloudformation wait stack-create-complete --stack-name my-app

# Visa status
aws cloudformation describe-stacks --stack-name my-app

# Lista resurser
aws cloudformation list-stack-resources --stack-name my-app
```

| Status | Betydelse |
|--------|-----------|
| `CREATE_IN_PROGRESS` | Skapar resurser |
| `CREATE_COMPLETE` | Klart |
| `CREATE_FAILED` | Fel - kollar rollback |
| `ROLLBACK_COMPLETE` | Rollback klar |
| `UPDATE_IN_PROGRESS` | Uppdaterar |

------------------------------------------------------------

## Change Sets

```
+-------------------------------------------------------------+
|                    CHANGE SET FLOW                          |
+-------------------------------------------------------------+
|                                                             |
|   Template v2 --► create-change-set --► Review changes     |
|                                              |              |
|                                              ▼              |
|                                    +-----------------+     |
|                                    | Action: Add     |     |
|                                    | Action: Modify  |     |
|                                    | Action: Remove  |     |
|                                    | Replacement?    |     |
|                                    +--------+--------+     |
|                                             |              |
|                          Approve?  ---------+----------    |
|                           YES              NO              |
|                            |                |              |
|                            ▼                ▼              |
|                    execute-change-set   delete-change-set  |
|                                                            |
+-------------------------------------------------------------+
```

```bash
# Skapa change set (preview)
aws cloudformation create-change-set \\
    --stack-name my-app \\
    --change-set-name update-v2 \\
    --template-body file://template-v2.yaml

# Visa andringar
aws cloudformation describe-change-set \\
    --stack-name my-app \\
    --change-set-name update-v2

# Applicera
aws cloudformation execute-change-set \\
    --stack-name my-app \\
    --change-set-name update-v2
```

------------------------------------------------------------

## Intrinsic Functions

| Funktion | Anvandning |
|----------|------------|
| `!Ref` | Referera resurs (returnerar ID) |
| `!GetAtt` | Hamta attribut (ARN, DNS, etc) |
| `!Sub` | String substitution |
| `!Join` | Slå ihop strängar |
| `!Select` | Välj från lista |
| `!If` | Villkorligt värde |

```yaml
Resources:
  MyEC2:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      SubnetId: !Ref MySubnet

Outputs:
  InstanceIP:
    Value: !GetAtt MyEC2.PublicIp
```

------------------------------------------------------------

## Skydda och Radera

```bash
# Aktivera termination protection
aws cloudformation update-termination-protection \\
    --stack-name my-app \\
    --enable-termination-protection

# Radera stack (alla resurser tas bort!)
aws cloudformation delete-stack --stack-name my-app

# Visa events (for debugging)
aws cloudformation describe-stack-events --stack-name my-app
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Templates** | YAML/JSON infrastruktur-definitioner |
| **Stacks** | Deployment-enhet av resurser |
| **Change Sets** | Preview innan deployment |
| **Parameters** | Gor templates ateranvandbara |
| **Outputs** | Exportera varden mellan stacks |

**Kom ihåg:**
- **Change sets for prod** - alltid preview forst
- **Termination protection** - pa alla prod-stacks
- **describe-stack-events** - for debugging
- **Rollback ar automatiskt** - vid fel
- **Drift detection** - hitta manuella andringar
""",
        },
        {
            "title": "Route 53 - DNS och Routing",
            "slug": "route53-dns-routing",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Route 53 - DNS och Routing

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Route53-kunskap ar kritisk |
|----------|-----------------------------------|
| **Domain management** | Hantera DNS for alla tjanster |
| **High availability** | Failover vid problem |
| **Load distribution** | Weighted/latency routing |
| **Global reach** | Geo-routing |
| **Service discovery** | Private hosted zones |

Route 53 ar AWS globally distribuerad DNS-tjanst med 100% SLA.

------------------------------------------------------------

## Route 53 Komponenter

```
+-------------------------------------------------------------+
|                  ROUTE 53 OVERSIKT                          |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------------------------------------------+   |
|   |              HOSTED ZONES                           |   |
|   |  +-------------+  +-------------+                  |   |
|   |  |example.com  |  |internal.com |                  |   |
|   |  |(public)     |  |(private)    |                  |   |
|   |  +------+------+  +------+------+                  |   |
|   +---------+----------------+--------------------------+   |
|             |                |                              |
|             ▼                ▼                              |
|   +-----------------------------------------------------+   |
|   |              RECORD SETS                            |   |
|   |  A      CNAME    MX      TXT     ALIAS             |   |
|   +-----------------------------------------------------+   |
|             |                                               |
|             ▼                                               |
|   +-----------------------------------------------------+   |
|   |              ROUTING POLICIES                       |   |
|   |  Simple | Weighted | Latency | Failover | Geo      |   |
|   +-----------------------------------------------------+   |
|             |                                               |
|             ▼                                               |
|   +-----------------------------------------------------+   |
|   |              HEALTH CHECKS                          |   |
|   |     Monitor endpoints for failover                  |   |
|   +-----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Hosted Zones

```bash
# Skapa hosted zone
aws route53 create-hosted-zone \\
    --name example.com \\
    --caller-reference $(date +%s)

# Lista zones
aws route53 list-hosted-zones

# Lista records i en zone
aws route53 list-resource-record-sets \\
    --hosted-zone-id Z1234567890
```

| Typ | Beskrivning |
|-----|-------------|
| **Public** | Internet-tillganglig DNS |
| **Private** | Endast inom VPC |

------------------------------------------------------------

## DNS Records

| Record | Anvandning |
|--------|------------|
| **A** | IPv4 adress |
| **AAAA** | IPv6 adress |
| **CNAME** | Alias till annan doman |
| **MX** | Mail servers |
| **TXT** | Text (verifiering, SPF) |
| **ALIAS** | AWS-specifik pekare |

```bash
# Skapa A record
aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "UPSERT",
            "ResourceRecordSet": {
                "Name": "www.example.com",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [{"Value": "1.2.3.4"}]
            }
        }]
    }'

# Alias till CloudFront
aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "example.com",
                "Type": "A",
                "AliasTarget": {
                    "HostedZoneId": "Z2FDTNDATAQYW2",
                    "DNSName": "d123.cloudfront.net",
                    "EvaluateTargetHealth": false
                }
            }
        }]
    }'
```

------------------------------------------------------------

## Routing Policies

```
+-------------------------------------------------------------+
|                 ROUTING POLICIES                            |
+-------------------------------------------------------------+
|                                                             |
|   SIMPLE        WEIGHTED         FAILOVER                   |
|   ------        --------         --------                   |
|   +---+         +---+  70%       +---+ PRIMARY              |
|   | A +--►      | A +----►       | A +-------►              |
|   +---+         +---+            +-+-+                      |
|                 +---+  30%         | Health                 |
|                 | B +----►         | Check                  |
|                 +---+              ▼ fails                  |
|                                  +---+ SECONDARY            |
|                                  | B +-------►              |
|                                  +---+                      |
|                                                             |
|   LATENCY       GEOLOCATION                                 |
|   -------       -----------                                 |
|   eu-north-1    Europe ----► EU Server                     |
|   us-east-1     USA -------► US Server                     |
|                                                             |
+-------------------------------------------------------------+
```

| Policy | Anvandning |
|--------|------------|
| **Simple** | Ett svar |
| **Weighted** | Gradual rollout |
| **Latency** | Narmaste region |
| **Failover** | HA med health checks |
| **Geolocation** | Baserat pa anvandare |

------------------------------------------------------------

## Health Checks

```bash
# Skapa health check
aws route53 create-health-check \\
    --caller-reference $(date +%s) \\
    --health-check-config '{
        "IPAddress": "1.2.3.4",
        "Port": 443,
        "Type": "HTTPS",
        "ResourcePath": "/health",
        "RequestInterval": 30,
        "FailureThreshold": 3
    }'

# Kolla status
aws route53 get-health-check-status --health-check-id abc123
```

| Parameter | Beskrivning |
|-----------|-------------|
| **RequestInterval** | 10 eller 30 sekunder |
| **FailureThreshold** | Antal misslyckanden |
| **Type** | HTTP, HTTPS, TCP |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Hosted Zones** | En per doman |
| **ALIAS** | For AWS-resurser (gratis) |
| **Health Checks** | Automatisk failover |
| **Weighted** | Gradual deployments |
| **TTL** | Lagre = snabbare andringar |

**Kom ihåg:**
- **ALIAS for root domain** - CNAME fungerar ej
- **Health checks for failover** - krävs for automatik
- **Lag TTL vid andringar** - snabbare propagering
- **100% SLA** - extremt tillforlitlig
- **Private zones** - for intern service discovery
""",
        },
        {
            "title": "CloudFront - CDN och Edge",
            "slug": "cloudfront-cdn-edge",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# CloudFront - CDN och Edge

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor CloudFront-kunskap ar kritisk |
|----------|--------------------------------------|
| **Performance** | Lag latens globalt |
| **Kostnadseffektivt** | Minska load pa origin |
| **Sakerhet** | DDoS-skydd, WAF-integration |
| **HTTPS** | Gratis SSL med ACM |
| **Static hosting** | S3 + CloudFront |

CloudFront ar AWS CDN med 400+ edge locations globalt.

------------------------------------------------------------

## CloudFront Arkitektur

```
+-------------------------------------------------------------+
|                  CLOUDFRONT FLOW                            |
+-------------------------------------------------------------+
|                                                             |
|   +---------+                        +-----------------+   |
|   |  User   |---- Request ----------►|  Edge Location  |   |
|   | Sweden  |                        |   Stockholm     |   |
|   +---------+                        +--------+--------+   |
|                                               |            |
|                                   +-----------+----------+ |
|                                   |                      | |
|                              Cache HIT?              Cache |
|                                   |                  MISS  |
|                                   ▼                      | |
|                           +-------------+                | |
|                           |  Return     |                | |
|                           |  Cached     |                | |
|                           +-------------+                | |
|                                                          | |
|                                                          ▼ |
|   +--------------------------------------------------------+
|   |                      ORIGIN                           |
|   |   +---------+    +---------+    +---------+         |
|   |   |   S3    |    |   ALB   |    | Custom  |         |
|   |   | Bucket  |    |         |    | Server  |         |
|   |   +---------+    +---------+    +---------+         |
|   +--------------------------------------------------------+
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Distribution

```bash
# Lista distributions
aws cloudfront list-distributions

# Skapa distribution (forenklad)
aws cloudfront create-distribution \\
    --origin-domain-name my-bucket.s3.eu-north-1.amazonaws.com
```

| Origin Type | Anvandning |
|-------------|------------|
| **S3** | Statiska filer |
| **ALB** | Dynamiskt content |
| **Custom** | Externa servrar |
| **MediaStore** | Video streaming |

------------------------------------------------------------

## Origin Access Control (OAC)

```
+-------------------------------------------------------------+
|                    S3 + CLOUDFRONT                          |
+-------------------------------------------------------------+
|                                                             |
|   User --► CloudFront --► S3 Bucket                        |
|               |              |                              |
|               |              |                              |
|           Signerar        Policy:                          |
|           requests        "Endast CloudFront"              |
|                                                             |
|   User -----X---------► S3 Bucket (BLOCKED)               |
|            Direct access blocked                           |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa OAC
aws cloudfront create-origin-access-control \\
    --origin-access-control-config '{
        "Name": "my-oac",
        "SigningProtocol": "sigv4",
        "SigningBehavior": "always",
        "OriginAccessControlOriginType": "s3"
    }'
```

------------------------------------------------------------

## Cache Invalidering

```bash
# Invalidera specifika filer
aws cloudfront create-invalidation \\
    --distribution-id E1234567890 \\
    --paths '/images/*' '/index.html'

# Lista invalideringar
aws cloudfront list-invalidations --distribution-id E1234567890
```

| Invalidering | Kostnad |
|--------------|---------|
| **Forsta 1000/manad** | Gratis |
| **Darutover** | $0.005 per path |
| **Wildcard /**** | Rakas som 1 path |

------------------------------------------------------------

## HTTPS och Custom Domain

```bash
# Bestall certifikat (MASTE vara us-east-1!)
aws acm request-certificate \\
    --domain-name example.com \\
    --subject-alternative-names "*.example.com" \\
    --validation-method DNS \\
    --region us-east-1

# Kolla certifikatstatus
aws acm describe-certificate \\
    --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/abc \\
    --region us-east-1
```

| Krav | Detalj |
|------|--------|
| **ACM region** | us-east-1 for CloudFront |
| **Validering** | DNS eller Email |
| **Wildcard** | *.example.com |

------------------------------------------------------------

## Cache Behaviors

| Path Pattern | Cache Policy |
|--------------|--------------|
| `/api/*` | Ingen caching |
| `/static/*` | Max caching |
| `*.jpg` | Bilder - 1 ar |
| `Default (*)` | Standard policy |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Edge caching** | 400+ locations globalt |
| **OAC** | Blockera direkt S3-access |
| **Invalidering** | Tvinga cache refresh |
| **ACM us-east-1** | KRAV for CloudFront |
| **Behaviors** | Olika caching per path |

**Kom ihåg:**
- **ACM maste vara i us-east-1**
- **OAC for S3** - sakerhet
- **Invalidering kostar** - planera releases
- **Cache headers** - origin kontrollerar TTL
- **Versioning i filnamn** - battre an invalidering
""",
        },
        {
            "title": "SNS och SQS - Meddelandetjänster",
            "slug": "sns-sqs-meddelandetjanster",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# SNS och SQS - Meddelandetjanster

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor SNS/SQS-kunskap ar kritisk |
|----------|-----------------------------------|
| **Decoupling** | Loskoppla system |
| **Async processing** | Bakgrundsjobb |
| **Event-driven** | Reagera pa handelser |
| **Fan-out** | Ett event till manga |
| **Reliability** | Garanterad leverans |

SNS (pub/sub) och SQS (koer) ar grundlaggande for moderna arkitekturer.

------------------------------------------------------------

## SNS vs SQS

```
+-------------------------------------------------------------+
|                   SNS vs SQS                                |
+-------------------------------------------------------------+
|                                                             |
|   SNS (Pub/Sub)              SQS (Queue)                   |
|   -------------              ----------                    |
|                                                             |
|   Publisher --► Topic        Producer --► Queue            |
|                  |                          |              |
|        +---------+---------+               |              |
|        ▼         ▼         ▼               ▼              |
|     Email     Lambda      SQS          Consumer           |
|                                                            |
|   PUSH model              PULL model                       |
|   Many receivers          One receiver                     |
|   Broadcast               Point-to-point                   |
|                                                            |
+-------------------------------------------------------------+
```

| Feature | SNS | SQS |
|---------|-----|-----|
| **Model** | Push | Pull |
| **Receivers** | Manga | En per meddelande |
| **Persistence** | Nej | Ja (14 dagar) |
| **Use case** | Notifications | Job queue |

------------------------------------------------------------

## SNS Topics

```bash
# Skapa topic
aws sns create-topic --name order-events

# Skapa email subscription
aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --protocol email \\
    --notification-endpoint user@example.com

# Skapa SQS subscription (fan-out)
aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --protocol sqs \\
    --notification-endpoint arn:aws:sqs:eu-north-1:123456789012:my-queue

# Publicera meddelande
aws sns publish \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --message '{"orderId": "123", "status": "created"}'
```

| Protocol | Beskrivning |
|----------|-------------|
| **email** | Skickar email |
| **sqs** | Pushar till ko |
| **lambda** | Anropar funktion |
| **http/https** | Webhook |

------------------------------------------------------------

## SQS Koer

```bash
# Skapa Standard queue
aws sqs create-queue \\
    --queue-name order-processing \\
    --attributes '{
        "VisibilityTimeout": "30",
        "MessageRetentionPeriod": "345600"
    }'

# Skapa FIFO queue
aws sqs create-queue \\
    --queue-name order-processing.fifo \\
    --attributes '{"FifoQueue": "true"}'
```

| Typ | Throughput | Ordering | Duplicates |
|-----|------------|----------|------------|
| **Standard** | Unlimited | Best-effort | Possible |
| **FIFO** | 300 msg/s | Guaranteed | Never |

------------------------------------------------------------

## Skicka och Ta Emot

```bash
# Skicka meddelande
aws sqs send-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --message-body '{"orderId": "123"}'

# Ta emot (long polling)
aws sqs receive-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --wait-time-seconds 20

# Radera efter processing
aws sqs delete-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --receipt-handle "AQEBwJnKyr..."
```

| Parameter | Beskrivning |
|-----------|-------------|
| **VisibilityTimeout** | Tid meddelande ar osynligt |
| **WaitTimeSeconds** | Long polling timeout |
| **ReceiptHandle** | Kravs for delete |

------------------------------------------------------------

## Dead Letter Queue (DLQ)

```
+-------------------------------------------------------------+
|                  DLQ WORKFLOW                               |
+-------------------------------------------------------------+
|                                                             |
|   Message --► Main Queue --► Consumer                      |
|                   |              |                          |
|                   |         Processing                      |
|                   |         fails 3x                        |
|                   |              |                          |
|                   |              ▼                          |
|                   +--------► DLQ --► Investigation         |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Skapa DLQ
aws sqs create-queue --queue-name order-processing-dlq

# Konfigurera redrive policy
aws sqs set-queue-attributes \\
    --queue-url https://sqs.../order-processing \\
    --attributes '{
        "RedrivePolicy": "{\\"deadLetterTargetArn\\":\\"arn:aws:sqs:...:dlq\\",\\"maxReceiveCount\\":\\"3\\"}"
    }'
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **SNS** | Pub/sub - broadcast till manga |
| **SQS** | Queue - en consumer per message |
| **Long polling** | wait-time-seconds = 20 |
| **DLQ** | Fanga misslyckade meddelanden |
| **Fan-out** | SNS -> flera SQS |

**Kom ihåg:**
- **SNS + SQS** - vanligt fan-out pattern
- **Long polling** - effektivare an short
- **DLQ for alla prod-koer** - kraver investigation
- **FIFO for ordering** - langsammare men garanterat
- **VisibilityTimeout** - langre an processing time
""",
        },
        {
            "title": "DynamoDB - NoSQL Database",
            "slug": "dynamodb-nosql-database",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# DynamoDB - NoSQL Database

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor DynamoDB-kunskap ar kritisk |
|----------|-------------------------------------|
| **Serverless** | Lambda + DynamoDB ar standard |
| **Skalbarhet** | Automatisk utan downtime |
| **Latens** | Single-digit millisekund |
| **Global** | Multi-region replikering |
| **NoOps** | Fully managed |

DynamoDB ar AWS serverless NoSQL-databas med oandlig skalning.

------------------------------------------------------------

## DynamoDB Datamodell

```
+-------------------------------------------------------------+
|                  DYNAMODB STRUKTUR                          |
+-------------------------------------------------------------+
|                                                             |
|   TABLE: Orders                                             |
|   +-----------------------------------------------------+  |
|   |  Partition Key (PK)  |  Sort Key (SK)  | Attributes |  |
|   +-----------------------------------------------------+  |
|   |  customerId: C001    |  order#001      | total: 100 |  |
|   |  customerId: C001    |  order#002      | total: 250 |  |
|   |  customerId: C002    |  order#001      | total: 75  |  |
|   +-----------------------------------------------------+  |
|                                                             |
|   PK = Partition (which server)                            |
|   SK = Sort (order within partition)                       |
|   PK alone = Simple key                                    |
|   PK + SK = Composite key                                  |
|                                                             |
+-------------------------------------------------------------+
```

| Term | Beskrivning |
|------|-------------|
| **Table** | Samling av items |
| **Item** | En rad (max 400KB) |
| **Attribute** | Falt i item |
| **Partition Key** | HASH - bestammer partition |
| **Sort Key** | RANGE - sortering inom partition |

------------------------------------------------------------

## Skapa Tabell

```bash
# Enkel tabell (endast PK)
aws dynamodb create-table \\
    --table-name Users \\
    --attribute-definitions AttributeName=userId,AttributeType=S \\
    --key-schema AttributeName=userId,KeyType=HASH \\
    --billing-mode PAY_PER_REQUEST

# Composite key (PK + SK)
aws dynamodb create-table \\
    --table-name Orders \\
    --attribute-definitions \\
        AttributeName=customerId,AttributeType=S \\
        AttributeName=orderId,AttributeType=S \\
    --key-schema \\
        AttributeName=customerId,KeyType=HASH \\
        AttributeName=orderId,KeyType=RANGE \\
    --billing-mode PAY_PER_REQUEST
```

| Billing Mode | Anvandning |
|--------------|------------|
| **PAY_PER_REQUEST** | Variabel last |
| **PROVISIONED** | Forutsagbar last |

------------------------------------------------------------

## CRUD Operationer

```bash
# Skapa/Ersatt item
aws dynamodb put-item \\
    --table-name Users \\
    --item '{
        "userId": {"S": "user123"},
        "name": {"S": "Anna Andersson"},
        "email": {"S": "anna@example.com"}
    }'

# Hamta item
aws dynamodb get-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}'

# Uppdatera
aws dynamodb update-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}' \\
    --update-expression "SET #n = :name" \\
    --expression-attribute-names '{"#n": "name"}' \\
    --expression-attribute-values '{":name": {"S": "Anna Svensson"}}'

# Radera
aws dynamodb delete-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}'
```

| Type | Notation |
|------|----------|
| **String** | S |
| **Number** | N |
| **Binary** | B |
| **List** | L |
| **Map** | M |

------------------------------------------------------------

## Query vs Scan

```
+-------------------------------------------------------------+
|                  QUERY vs SCAN                              |
+-------------------------------------------------------------+
|                                                             |
|   QUERY                      SCAN                          |
|   -----                      ----                          |
|   Anvander index             Laser HELA tabellen           |
|   Snabbt och effektivt       Langsamt och dyrt            |
|   Kraver PK                  Inga krav                     |
|                                                             |
|   +---+                      +---+---+---+---+---+        |
|   | X |◄-- Hamtar            | X | X | X | X | X |        |
|   +---+    specifik          +---+---+---+---+---+        |
|            partition              Laser alla              |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Query (EFFEKTIVT)
aws dynamodb query \\
    --table-name Orders \\
    --key-condition-expression "customerId = :cid" \\
    --expression-attribute-values '{":cid": {"S": "C001"}}'

# Scan (UNDVIK I PROD)
aws dynamodb scan \\
    --table-name Users \\
    --filter-expression "contains(email, :domain)" \\
    --expression-attribute-values '{":domain": {"S": "@example.com"}}'
```

------------------------------------------------------------

## Backups och Global Tables

```bash
# Aktivera Point-in-Time Recovery
aws dynamodb update-continuous-backups \\
    --table-name Orders \\
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true

# Skapa on-demand backup
aws dynamodb create-backup \\
    --table-name Orders \\
    --backup-name orders-backup-2024

# Skapa Global Table replica
aws dynamodb update-table \\
    --table-name Orders \\
    --replica-updates '[{"Create": {"RegionName": "us-east-1"}}]'
```

| Feature | Beskrivning |
|---------|-------------|
| **PITR** | Restore till vilken sekund (35 dagar) |
| **On-demand** | Manuell backup (bevaras for evigt) |
| **Global Tables** | Multi-region active-active |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Partition Key** | Kritisk for prestanda |
| **On-demand** | Betala per request |
| **Query** | Anvand ALLTID over Scan |
| **PITR** | Aktivera for prod-tabeller |
| **Global Tables** | Multi-region DR |

**Kom ihåg:**
- **PK design ar kritiskt** - paverkar all prestanda
- **Query over Scan** - Scan laser ALLT
- **On-demand for variabel last** - ingen kapacitetsplanering
- **PITR for alla prod-tabeller** - kraver backup
- **Single-digit ms latens** - konsistent snabbt
""",
        },
        {
            "title": "Secrets Manager - Hemlighetshantering",
            "slug": "secrets-manager-hemlighetshantering",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Secrets Manager - Hemlighetshantering

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Secrets Manager-kunskap ar kritisk |
|----------|-------------------------------------------|
| **Sakerhet** | Inga hardkodade losenord |
| **Rotation** | Automatisk losenordsbyte |
| **Compliance** | Audit trail for access |
| **Integration** | RDS, Redshift, DocumentDB |
| **Multi-env** | Separera dev/prod secrets |

Secrets Manager lagrar och roterar hemligheter sakert.

------------------------------------------------------------

## Secrets Manager vs Parameter Store

| Feature | Secrets Manager | Parameter Store |
|---------|-----------------|-----------------|
| **Rotation** | Inbyggd | Manuell |
| **Kostnad** | $0.40/secret/manad | Gratis (standard) |
| **RDS integration** | Ja | Nej |
| **KMS** | Alltid krypterat | SecureString |
| **Anvandning** | Databas-losenord | Config values |

------------------------------------------------------------

## Skapa och Hantera Secrets

```bash
# Skapa secret (JSON)
aws secretsmanager create-secret \\
    --name prod/myapp/db-credentials \\
    --description "Production database credentials" \\
    --secret-string '{"username": "admin", "password": "SuperSecret123!"}'

# Skapa enkel string
aws secretsmanager create-secret \\
    --name prod/myapp/api-key \\
    --secret-string "sk-abc123def456"

# Lista secrets
aws secretsmanager list-secrets --filters Key=name,Values=prod/
```

| Namning | Beskrivning |
|---------|-------------|
| `prod/app/secret` | Hierarkisk struktur |
| `dev/app/secret` | Separera miljoer |

------------------------------------------------------------

## Hamta Secrets

```bash
# Hamta secret
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials

# Hamta forega version
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --version-stage AWSPREVIOUS

# Extrahera specifikt varde
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --query 'SecretString' \\
    --output text | jq -r '.password'
```

| Version Stage | Beskrivning |
|---------------|-------------|
| **AWSCURRENT** | Aktuell version |
| **AWSPREVIOUS** | Foreg version |
| **AWSPENDING** | Under rotation |

------------------------------------------------------------

## Rotation

```
+-------------------------------------------------------------+
|                  ROTATION WORKFLOW                          |
+-------------------------------------------------------------+
|                                                             |
|   1. Schedule triggers                                      |
|              |                                              |
|              ▼                                              |
|   2. Lambda skapar nytt losenord --► AWSPENDING            |
|              |                                              |
|              ▼                                              |
|   3. Lambda uppdaterar databas                             |
|              |                                              |
|              ▼                                              |
|   4. Lambda testar anslutning                              |
|              |                                              |
|              ▼                                              |
|   5. AWSPENDING --► AWSCURRENT (gammalt --► AWSPREVIOUS)  |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Konfigurera rotation
aws secretsmanager rotate-secret \\
    --secret-id prod/myapp/db-credentials \\
    --rotation-lambda-arn arn:aws:lambda:eu-north-1:123456789012:function:rotator \\
    --rotation-rules AutomaticallyAfterDays=30

# Trigga manuell rotation
aws secretsmanager rotate-secret \\
    --secret-id prod/myapp/db-credentials
```

------------------------------------------------------------

## Anvand i Scripts

```bash
# Satt miljovariabel
export DB_PASSWORD=$(aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --query 'SecretString' \\
    --output text | jq -r '.password')

# Radera secret
aws secretsmanager delete-secret \\
    --secret-id prod/myapp/old-credentials \\
    --recovery-window-in-days 7
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Hierarkiska namn** | prod/app/secret |
| **Automatisk kryptering** | KMS by default |
| **Versionering** | AWSCURRENT, AWSPREVIOUS |
| **Rotation** | Lambda for automatik |
| **Recovery window** | 7-30 dagar soft delete |

**Kom ihåg:**
- **Alltid krypterat** - KMS-nycklar
- **Rotation for databaser** - anvand AWS templates
- **jq for JSON** - extrahera specifika varden
- **Soft delete** - aterhamtning mojlig
- **Kostnad** - $0.40/secret/manad
""",
        },
        {
            "title": "Systems Manager - Operationell Hantering",
            "slug": "systems-manager-operationell-hantering",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Systems Manager - Operationell Hantering

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor SSM-kunskap ar kritisk |
|----------|-------------------------------|
| **No SSH** | Saker access utan portar |
| **Config management** | Parameter Store |
| **Automation** | Runbooks och scripting |
| **Patching** | Automatiska uppdateringar |
| **Inventory** | Asset management |

Systems Manager ar AWS operationella nav for EC2 och hybrid.

------------------------------------------------------------

## SSM Komponenter

```
+-------------------------------------------------------------+
|                  SYSTEMS MANAGER                            |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------+  +-----------------+                |
|   | Parameter Store |  |  Run Command    |                |
|   |  Config values  |  |  Remote exec    |                |
|   |  Secrets        |  |  No SSH needed  |                |
|   +-----------------+  +-----------------+                |
|                                                             |
|   +-----------------+  +-----------------+                |
|   | Session Manager |  |   Automation    |                |
|   |  Secure shell   |  |   Runbooks      |                |
|   |  Port forward   |  |   Multi-step    |                |
|   +-----------------+  +-----------------+                |
|                                                             |
|   +-----------------+  +-----------------+                |
|   | Patch Manager   |  |    Inventory    |                |
|   |  Auto patching  |  |  Asset mgmt     |                |
|   +-----------------+  +-----------------+                |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Parameter Store

```bash
# Skapa String parameter
aws ssm put-parameter \\
    --name /myapp/prod/db-host \\
    --value "db.example.com" \\
    --type String

# Skapa SecureString (krypterad)
aws ssm put-parameter \\
    --name /myapp/prod/db-password \\
    --value "SuperSecret123!" \\
    --type SecureString

# Hamta parameter
aws ssm get-parameter \\
    --name /myapp/prod/db-host

# Hamta och dekryptera
aws ssm get-parameter \\
    --name /myapp/prod/db-password \\
    --with-decryption

# Hamta alla under path
aws ssm get-parameters-by-path \\
    --path /myapp/prod/ \\
    --recursive \\
    --with-decryption
```

| Type | Kostnad | Max storlek |
|------|---------|-------------|
| **String** | Gratis | 4KB |
| **SecureString** | Gratis | 4KB |
| **Advanced** | $0.05/param | 8KB |

------------------------------------------------------------

## Run Command

```bash
# Kor kommando via taggar
aws ssm send-command \\
    --document-name AWS-RunShellScript \\
    --targets Key=tag:Environment,Values=production \\
    --parameters 'commands=["yum update -y"]'

# Kor pa specifika instanser
aws ssm send-command \\
    --document-name AWS-RunShellScript \\
    --instance-ids i-abc123 i-def456 \\
    --parameters 'commands=["systemctl restart nginx"]'

# Visa resultat
aws ssm list-command-invocations \\
    --command-id abc123 \\
    --details
```

| Document | Beskrivning |
|----------|-------------|
| `AWS-RunShellScript` | Linux bash |
| `AWS-RunPowerShellScript` | Windows PS |
| `AWS-UpdateSSMAgent` | Uppdatera agent |

------------------------------------------------------------

## Session Manager

```
+-------------------------------------------------------------+
|                  SESSION MANAGER                            |
+-------------------------------------------------------------+
|                                                             |
|   Traditional SSH           Session Manager                 |
|   -----------------         ---------------                |
|                                                             |
|   +------+                  +------+                       |
|   | User |                  | User |                       |
|   +--+---+                  +--+---+                       |
|      |                         |                            |
|      | SSH port 22             | HTTPS to SSM endpoint     |
|      ▼                         ▼                            |
|   +------+                  +------+                       |
|   | EC2  |                  | EC2  | (SSM Agent)           |
|   +------+                  +------+                       |
|                                                             |
|   Requires:                 Requires:                      |
|   - Open port 22            - SSM Agent                    |
|   - SSH keys                - IAM role                     |
|   - Bastion host            - NO open ports                |
|                                                             |
+-------------------------------------------------------------+
```

```bash
# Starta interaktiv session
aws ssm start-session --target i-abc123

# Port forwarding
aws ssm start-session \\
    --target i-abc123 \\
    --document-name AWS-StartPortForwardingSession \\
    --parameters '{"portNumber":["3306"],"localPortNumber":["3306"]}'

# Lista aktiva sessioner
aws ssm describe-sessions --state Active
```

------------------------------------------------------------

## Automation

```bash
# Lista automation documents
aws ssm list-documents \\
    --filters Key=DocumentType,Values=Automation

# Kor automation
aws ssm start-automation-execution \\
    --document-name AWS-RestartEC2Instance \\
    --parameters '{"InstanceId":["i-abc123"]}'

# Visa status
aws ssm describe-automation-executions \\
    --filters Key=ExecutionStatus,Values=InProgress
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Parameter Store** | Gratis config management |
| **SecureString** | KMS-krypterat |
| **Run Command** | Remote exec utan SSH |
| **Session Manager** | Saker shell utan portar |
| **Automation** | Multi-step runbooks |

**Kom ihåg:**
- **SSM Agent** - maste installeras (pre-installed pa Amazon Linux)
- **IAM role** - EC2 behover SSM permissions
- **Inga oppna portar** - all trafik via SSM endpoint
- **Parameter Store** - gratis for standard tier
- **Session logging** - CloudWatch/S3 for audit
""",
        },
        {
            "title": "Cost Management - Kostnadsoptimering",
            "slug": "cost-management-kostnadsoptimering",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Cost Management - Kostnadsoptimering

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Cost Management ar kritiskt |
|----------|-------------------------------------|
| **Budget** | Forhindra overskridanden |
| **Optimering** | Hitta besparingar |
| **Allokering** | Fordelning per team/projekt |
| **Forecast** | Planera framtida kostnader |
| **Anomalier** | Upptack ovantade okningar |

Kostnadshantering ar en karnkompetens for alla DevOps-ingenjorer.

------------------------------------------------------------

## Cost Management Verktyg

```
+-------------------------------------------------------------+
|                  AWS COST TOOLS                             |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------+  +-----------------+                |
|   | Cost Explorer   |  |   Budgets       |                |
|   | Visualisering   |  |   Alerts        |                |
|   | Analys          |  |   Forecasts     |                |
|   +-----------------+  +-----------------+                |
|                                                             |
|   +-----------------+  +-----------------+                |
|   | Savings Plans   |  | Right-sizing    |                |
|   | Rabatter        |  | Compute Opt.    |                |
|   | 30-70% off      |  | Recommendations |                |
|   +-----------------+  +-----------------+                |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Cost Explorer CLI

```bash
# Total kostnad for manad
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics UnblendedCost

# Kostnad per tjanst
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity DAILY \\
    --metrics UnblendedCost \\
    --group-by Type=DIMENSION,Key=SERVICE

# Kostnadsprognos
aws ce get-cost-forecast \\
    --time-period Start=2024-02-01,End=2024-02-28 \\
    --metric UNBLENDED_COST \\
    --granularity MONTHLY
```

| Metric | Beskrivning |
|--------|-------------|
| **UnblendedCost** | Faktisk kostnad |
| **BlendedCost** | Konsoliderad billing |
| **AmortizedCost** | Fordelad RI/SP kostnad |

------------------------------------------------------------

## AWS Budgets

```bash
# Skapa budget med alert
aws budgets create-budget \\
    --account-id 123456789012 \\
    --budget '{
        "BudgetName": "monthly-budget",
        "BudgetType": "COST",
        "BudgetLimit": {"Amount": "1000", "Unit": "USD"},
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

# Lista budgets
aws budgets describe-budgets --account-id 123456789012
```

| Alert Type | Beskrivning |
|------------|-------------|
| **ACTUAL** | Faktisk forbrukning |
| **FORECASTED** | Prognostiserad |

------------------------------------------------------------

## Tagging for Kostnadsallokering

```bash
# Tagga resurser
aws ec2 create-tags \\
    --resources i-abc123 \\
    --tags Key=CostCenter,Value=engineering Key=Environment,Value=production

# Kostnad per tag
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics UnblendedCost \\
    --group-by Type=TAG,Key=CostCenter
```

| Tag | Anvandning |
|-----|------------|
| **CostCenter** | Avdelning/team |
| **Environment** | dev/staging/prod |
| **Project** | Projektnamn |

------------------------------------------------------------

## Savings Plans och Recommendations

```bash
# Savings Plans anvandning
aws ce get-savings-plans-utilization \\
    --time-period Start=2024-01-01,End=2024-01-31

# Kop-rekommendationer
aws ce get-savings-plans-purchase-recommendation \\
    --savings-plans-type COMPUTE_SP \\
    --term-in-years ONE_YEAR \\
    --payment-option NO_UPFRONT \\
    --lookback-period-in-days SIXTY_DAYS

# Right-sizing rekommendationer
aws ce get-rightsizing-recommendation \\
    --service AmazonEC2
```

| Savings Type | Rabatt | Flexibilitet |
|--------------|--------|--------------|
| **Compute SP** | 30-40% | Hog (EC2, Lambda, Fargate) |
| **EC2 SP** | 40-50% | Medium (EC2 family) |
| **Reserved** | 50-70% | Lag (specific instance) |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Budgets** | Forsta forsvaret mot overraskningar |
| **Tagging** | Obligatoriskt for allokering |
| **Cost Explorer** | Daglig kontroll |
| **Savings Plans** | 30-70% besparing |
| **Right-sizing** | Betala inte for overkapacitet |

**Kom ihåg:**
- **Budget alerts vid 80%** - tid att reagera
- **Tagga ALLT** - kan inte allokera utan taggar
- **Cost Explorer dagligen** - fanga anomalier tidigt
- **Compute SP** - flexiblast for de flesta
- **Right-sizing forst** - sedan Savings Plans
""",
        },
        {
            "title": "AWS Best Practices och Well-Architected",
            "slug": "aws-best-practices-well-architected",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# AWS Best Practices och Well-Architected

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Well-Architected ar kritiskt |
|----------|--------------------------------------|
| **Design** | Bygga ratt fran start |
| **Review** | Hitta svagheter |
| **Compliance** | Uppfyll branschkrav |
| **Optimering** | Kontinuerlig forbattring |
| **Dokumentation** | Best practices samlade |

Well-Architected Framework ar AWS officiella guide for att bygga sakra, effektiva och pålitliga system.

------------------------------------------------------------

## De Sex Pelarna

```
+-------------------------------------------------------------+
|               WELL-ARCHITECTED FRAMEWORK                    |
+-------------------------------------------------------------+
|                                                             |
|   +--------------+  +--------------+  +--------------+    |
|   | Operational  |  |   Security   |  | Reliability  |    |
|   | Excellence   |  |              |  |              |    |
|   |  Automate    |  |  Defense     |  |  Recover     |    |
|   +--------------+  +--------------+  +--------------+    |
|                                                             |
|   +--------------+  +--------------+  +--------------+    |
|   | Performance  |  |    Cost      |  |Sustainability|    |
|   | Efficiency   |  | Optimization |  |              |    |
|   |  Right-size  |  |  No waste    |  |  Green IT    |    |
|   +--------------+  +--------------+  +--------------+    |
|                                                             |
+-------------------------------------------------------------+
```

| Pelare | Fokus |
|--------|-------|
| **Operational Excellence** | Automation, monitoring, runbooks |
| **Security** | IAM, encryption, network isolation |
| **Reliability** | Multi-AZ, backup, disaster recovery |
| **Performance** | Right-sizing, caching, CDN |
| **Cost Optimization** | Savings Plans, tagging, right-sizing |
| **Sustainability** | Effektivitet, green regions |

------------------------------------------------------------

## Well-Architected Tool

```bash
# Skapa workload for review
aws wellarchitected create-workload \\
    --workload-name "production-api" \\
    --environment PRODUCTION \\
    --lenses wellarchitected \\
    --review-owner "devops-team" \\
    --aws-regions us-east-1

# Lista workloads
aws wellarchitected list-workloads

# Hamta fråga och svar
aws wellarchitected get-answer \\
    --workload-id abc123 \\
    --lens-alias wellarchitected \\
    --pillar-id operationalExcellence \\
    --question-id ops-1

# Uppdatera svar
aws wellarchitected update-answer \\
    --workload-id abc123 \\
    --lens-alias wellarchitected \\
    --pillar-id operationalExcellence \\
    --question-id ops-1 \\
    --selected-choices choice1 choice3 \\
    --notes "Implemented dashboards and runbooks"
```

| Lens | Beskrivning |
|------|-------------|
| **wellarchitected** | Generell framework |
| **serverless** | Lambda, API GW focus |
| **saas** | Multi-tenant patterns |

------------------------------------------------------------

## Operational Excellence Patterns

```bash
# CloudWatch dashboard
aws cloudwatch put-dashboard \\
    --dashboard-name MyAppOverview \\
    --dashboard-body file://dashboard.json

# EventBridge for deployment notifications
aws events put-rule \\
    --name deployment-failures \\
    --event-pattern '{
        "source": ["aws.codedeploy"],
        "detail-type": ["CodeDeploy Deployment State-change"],
        "detail": {"state": ["FAILURE"]}
    }'
```

```
+-------------------------------------------------------------+
|              OPERATIONAL EXCELLENCE                         |
+-------------------------------------------------------------+
|                                                             |
|   Dashboard --► Metrics --► Alarms --► Actions             |
|       |                        |                            |
|       ▼                        ▼                            |
|   Observability           Auto-remediation                  |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Security Best Practices

```bash
# IAM audit
aws iam get-account-summary
aws iam generate-credential-report
aws iam get-credential-report --output text --query Content | base64 -d

# Security Hub
aws securityhub enable-security-hub
aws securityhub get-findings \\
    --filters '{"SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}]}'

# GuardDuty
aws guardduty create-detector --enable
```

| Princip | Implementering |
|---------|----------------|
| **Least Privilege** | Specifika permissions, inga wildcards |
| **MFA** | Alla konsol-users |
| **Encryption** | At-rest och in-transit |
| **Audit** | CloudTrail, credential reports |

------------------------------------------------------------

## Reliability Patterns

```bash
# Auto Scaling audit
aws autoscaling describe-auto-scaling-groups \\
    --query 'AutoScalingGroups[*].[AutoScalingGroupName,MinSize,MaxSize]'

# RDS HA check
aws rds describe-db-instances \\
    --query 'DBInstances[*].[DBInstanceIdentifier,MultiAZ,BackupRetentionPeriod]'

# S3 versioning
aws s3api get-bucket-versioning --bucket my-bucket

# Target health
aws elbv2 describe-target-health \\
    --target-group-arn arn:aws:elasticloadbalancing:region:account:targetgroup/name/id
```

| Pattern | Benefit |
|---------|---------|
| **Multi-AZ** | Automatisk failover |
| **Auto Scaling** | Hantera lastspikes |
| **Versioning** | Skydd mot accidental delete |

------------------------------------------------------------

## Performance och Sustainability

```bash
# Compute Optimizer
aws compute-optimizer get-ec2-instance-recommendations

# Cost and usage
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity DAILY \\
    --metrics UsageQuantity \\
    --group-by Type=DIMENSION,Key=USAGE_TYPE
```

| Fokus | Action |
|-------|--------|
| **Right-sizing** | Folj Compute Optimizer |
| **Caching** | ElastiCache, CloudFront |
| **Sustainability** | Mindre resurser = mindre impact |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **6 Pelare** | Komplett arkitekturramverk |
| **Reviews** | Regelbundet, inte bara vid launch |
| **Automation** | Grund for operational excellence |
| **Multi-AZ** | Minimum for produktion |
| **Measure** | Metrics driver beslut |

**Kom ihåg:**
- **Well-Architected reviews kvartalvis** - kontinuerlig forbattring
- **Least privilege alltid** - borja restriktivt
- **Multi-AZ for allt kritiskt** - ingen SPOF
- **GuardDuty + Security Hub** - sakerhet i lager
- **Compute Optimizer** - data-driven rightsizing
""",
        },
    ],
}

