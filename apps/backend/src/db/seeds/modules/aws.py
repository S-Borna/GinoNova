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

## Varför behöver du kunna detta?

AWS är den största molnplattformen i världen med över 32% marknadsandel. Som DevOps-ingenjör kommer du nästan garanterat att arbeta med AWS. Du behöver förstå:

- **Hur AWS är organiserat** så du hittar rätt tjänster bland 200+ alternativ
- **Regioner och Availability Zones** så du kan designa för hög tillgänglighet
- **Grundläggande navigation** så du snabbt kan hitta och hantera resurser
- **AWS CLI** så du kan automatisera istället för att klicka i konsolen

---

## Så fungerar AWS

AWS är uppdelat i regioner (geografiska områden) och availability zones (separata datacenter inom en region). Varje region har minst två AZs för redundans. Du väljer region baserat på var dina användare finns och vilka lagkrav du har (GDPR kräver ofta EU-region).

Tänk på regioner som städer och AZs som separata byggnader i samma stad - om en byggnad brinner ner finns fortfarande de andra kvar.

---

## Installera AWS CLI

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# Laddar ner AWS CLI installationspaketet från Amazon
# -o sparar filen med namnet awscliv2.zip
# Detta är den officiella installationsmetoden för Linux

unzip awscliv2.zip
# Packar upp zip-filen till en katalog som heter 'aws'
# Kräver att unzip är installerat (sudo apt install unzip)
# Skapar aws/install och aws/dist/ med alla filer

sudo ./aws/install
# Kör installationsscriptet med sudo
# Installerar aws-kommandot till /usr/local/bin/aws
# Skapar även symlink så kommandot fungerar direkt

aws --version
# aws-cli/2.15.0 Python/3.11.6 Linux/5.15.0-1051-aws
# Verifierar att installationen lyckades
# Visar CLI-version, Python-version, och OS-information
```

---

## Konfigurera AWS CLI

```bash
aws configure
# Startar interaktiv konfigurationsguide
# Ställer fyra frågor och sparar svaren till ~/.aws/

# AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
# Din Access Key ID från IAM-konsolen
# Fungerar som ett användarnamn för API-åtkomst

# AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Din hemliga nyckel - VISA ALDRIG DENNA FÖR NÅGON
# Fungerar som lösenord - kan inte återskapas om du tappar den

# Default region name [None]: eu-north-1
# Standardregion för alla kommandon
# eu-north-1 är Stockholm, eu-west-1 är Irland

# Default output format [None]: json
# Format för CLI-output: json, table, eller text
# json är bäst för scripting, table för manuell läsning

cat ~/.aws/credentials
# [default]
# aws_access_key_id = AKIAIOSFODNN7EXAMPLE
# aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Visar var credentials sparas
# SKYDDA DENNA FIL - chmod 600 ~/.aws/credentials

cat ~/.aws/config
# [default]
# region = eu-north-1
# output = json
# Visar konfigurationsfilen
# Separerad från credentials för säkerhet
```

---

## Grundläggande kommandon

```bash
aws sts get-caller-identity
# {
#     "UserId": "AIDAIOSFODNN7EXAMPLE",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/devops-user"
# }
# Visar vem du är inloggad som
# Perfekt för att verifiera att credentials fungerar
# Account visar ditt 12-siffriga AWS-konto-ID

aws ec2 describe-regions --output table
# Listar alla tillgängliga AWS-regioner
# --output table ger snygg tabellformatering
# Du ser RegionName och Endpoint för varje region

aws ec2 describe-availability-zones --region eu-north-1
# Listar alla AZs i Stockholm-regionen
# Visar eu-north-1a, eu-north-1b, eu-north-1c
# State visar om AZ är available eller inte
# ZoneId är en unik identifierare

aws s3 ls
# Listar alla S3-buckets i ditt konto
# Visar datum, tid och bucket-namn
# Tom output betyder inga buckets finns ännu
```

---

## Miljövariabler för credentials

```bash
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
# Sätter access key som miljövariabel
# Överrider värdet i ~/.aws/credentials
# Användbart i CI/CD-pipelines

export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# Sätter secret key som miljövariabel
# ALDRIG hårdkoda i scripts - använd secrets manager
# Lägg till i .bashrc om du vill ha permanent

export AWS_DEFAULT_REGION="eu-north-1"
# Sätter standardregion
# Överrider värdet i ~/.aws/config
# Kan också sättas per kommando med --region

env | grep AWS
# Visar alla AWS-relaterade miljövariabler
# Bra för felsökning av credential-problem
# Kontrollera att inga gamla värden ligger kvar
```

---

## Key Takeaways

1. **Regioner är geografiska** - välj baserat på latens och compliance
2. **AZs ger redundans** - sprida resurser över minst 2 AZs
3. **CLI är kraftfullare än konsolen** - automatisering kräver CLI
4. **Skydda dina credentials** - behandla dem som lösenord
5. **eu-north-1 är Stockholm** - bra val för svenska projekt
""",
        },
        {
            "title": "IAM - Identity and Access Management",
            "slug": "iam-identity-access-management",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# IAM - Identity and Access Management

## Varför behöver du kunna detta?

IAM är AWS säkerhetssystem - det kontrollerar vem som får göra vad. Utan IAM-kunskap kan du:

- **Skapa säkerhetshål** som exponerar hela infrastrukturen
- **Låsa dig själv ute** från resurser du skapat
- **Misslyckas med automation** eftersom scripts saknar rätt permissions
- **Bryta mot compliance** genom att ge för breda rättigheter

IAM är grunden för allt säkerhetsarbete i AWS.

---

## Så fungerar IAM

IAM följer principen "deny by default" - allt är förbjudet tills du explicit tillåter det. Det finns fyra huvudkomponenter:

- **Users** - mänskliga användare eller service accounts
- **Groups** - samlingar av users med gemensamma permissions
- **Roles** - temporära identiteter som kan "antas" av services
- **Policies** - JSON-dokument som definierar permissions

---

## Skapa IAM-användare

```bash
aws iam create-user --user-name deploy-bot
# {
#     "User": {
#         "UserName": "deploy-bot",
#         "UserId": "AIDAIOSFODNN7EXAMPLE",
#         "Arn": "arn:aws:iam::123456789012:user/deploy-bot",
#         "CreateDate": "2024-01-15T10:30:00Z"
#     }
# }
# Skapar en ny IAM-användare
# Användaren har INGA permissions ännu
# Arn är den unika identifieraren för resursen

aws iam list-users
# Listar alla IAM-användare i kontot
# Visar UserName, UserId, Arn och CreateDate
# Kräver iam:ListUsers permission

aws iam get-user --user-name deploy-bot
# Hämtar detaljerad info om en specifik användare
# Visar även Tags och PermissionsBoundary om satta
# Användbart för att verifiera att användaren skapades
```

---

## Access Keys för programmatisk åtkomst

```bash
aws iam create-access-key --user-name deploy-bot
# {
#     "AccessKey": {
#         "UserName": "deploy-bot",
#         "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
#         "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
#         "Status": "Active"
#     }
# }
# Skapar access keys för användaren
# SPARA SecretAccessKey NU - den visas aldrig igen!
# Användaren kan ha max 2 access keys

aws iam list-access-keys --user-name deploy-bot
# Listar alla access keys för användaren
# Visar AccessKeyId och Status (Active/Inactive)
# SecretAccessKey visas ALDRIG efter skapande

aws iam delete-access-key --user-name deploy-bot --access-key-id AKIAIOSFODNN7EXAMPLE
# Tar bort en access key permanent
# Använd för att rotera keys eller vid läcka
# Användaren förlorar åtkomst som använde denna key
```

---

## IAM Groups

```bash
aws iam create-group --group-name Developers
# Skapar en ny grupp
# Grupper har inga permissions själva
# Permissions kommer från attachade policies

aws iam add-user-to-group --user-name deploy-bot --group-name Developers
# Lägger till användaren i gruppen
# Användaren ärver alla permissions från gruppen
# En användare kan vara med i flera grupper

aws iam list-groups-for-user --user-name deploy-bot
# Visar vilka grupper användaren tillhör
# Användbart för att förstå varifrån permissions kommer
# Returnerar GroupName, GroupId och Arn

aws iam get-group --group-name Developers
# Visar gruppens detaljer och alla medlemmar
# Listar alla Users som tillhör gruppen
# Användbart för att se vem som har vilka rättigheter
```

---

## IAM Policies

```bash
aws iam list-policies --scope AWS
# Listar AWS-managed policies (fördefinierade)
# --scope AWS visar bara Amazons policies
# Det finns hundratals färdiga policies för vanliga behov

aws iam list-policies --scope Local
# Listar customer-managed policies (dina egna)
# --scope Local visar bara policies du skapat
# Dessa kan du modifiera till skillnad från AWS-managed

aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
# Hämtar metadata om en policy
# Visar DefaultVersionId och AttachmentCount
# Visar inte själva policy-dokumentet
```

---

## Attacha Policies

```bash
aws iam attach-user-policy \\
    --user-name deploy-bot \\
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
# Ger användaren S3 read-only access
# Effekten är omedelbar
# Användaren kan nu lista och läsa S3-objekt

aws iam attach-group-policy \\
    --group-name Developers \\
    --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess
# Alla i gruppen får EC2-rättigheter
# Bättre än att attacha till varje user
# Enklare att hantera och audit:a

aws iam list-attached-user-policies --user-name deploy-bot
# Visar alla policies attachade direkt till användaren
# Visar INTE policies från grupptillhörighet
# PolicyName och PolicyArn för varje policy

aws iam list-attached-group-policies --group-name Developers
# Visar alla policies attachade till gruppen
# Alla gruppmedlemmar har dessa permissions
# Centraliserad hantering av rättigheter
```

---

## Skapa custom policy

```bash
cat << 'EOF' > s3-upload-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowUploadToSpecificBucket",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::my-upload-bucket/*"
        },
        {
            "Sid": "AllowListBucket",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::my-upload-bucket"
        }
    ]
}
EOF
# Skapar en policy-fil lokalt
# Version är alltid "2012-10-17"
# Sid är en beskrivning (valfri men rekommenderad)
# Effect: Allow eller Deny
# Action: vilka API-anrop som tillåts
# Resource: vilka resurser policyn gäller

aws iam create-policy \\
    --policy-name S3UploadOnly \\
    --policy-document file://s3-upload-policy.json \\
    --description "Allows upload to specific S3 bucket"
# Skapar policyn i AWS
# file:// läser från lokal fil
# Returnerar PolicyArn som du använder för att attacha
# Policyn är nu tillgänglig att attacha till users/groups/roles
```

---

## Key Takeaways

1. **Deny by default** - inget är tillåtet förrän du säger det
2. **Använd Groups** - attacha policies till groups, inte users
3. **Least privilege** - ge minsta möjliga permissions
4. **Rotera access keys** - byt regelbundet och vid misstänkt läcka
5. **Audit regelbundet** - kolla vem som har vilka rättigheter
""",
        },
        {
            "title": "EC2 - Elastic Compute Cloud",
            "slug": "ec2-elastic-compute-cloud",
            "difficulty": "easy",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# EC2 - Elastic Compute Cloud

## Varför behöver du kunna detta?

EC2 är AWS ursprungliga och mest använda tjänst - virtuella servrar i molnet. Som DevOps behöver du kunna:

- **Starta och stoppa instanser** för att hantera kapacitet och kostnader
- **Välja rätt instanstyp** för att balansera prestanda och pris
- **Konfigurera nätverk och säkerhet** så applikationer är tillgängliga men skyddade
- **Automatisera med User Data** så nya instanser konfigureras automatiskt

---

## Så fungerar EC2

EC2 låter dig hyra virtuella maskiner (instanser) som körs i AWS datacenter. Du betalar per sekund för tiden instansen är igång. Varje instans har:

- **AMI** - Amazon Machine Image, operativsystemet och förinstallerad mjukvara
- **Instance Type** - hur mycket CPU, RAM och nätverkskapacitet
- **Security Group** - brandväggsregler för inkommande/utgående trafik
- **Key Pair** - SSH-nyckel för inloggning

---

## Skapa en EC2-instans

```bash
aws ec2 run-instances \\
    --image-id ami-0c55b159cbfafe1f0 \\
    --instance-type t3.micro \\
    --key-name my-key \\
    --security-group-ids sg-12345678 \\
    --subnet-id subnet-12345678 \\
    --count 1
# Startar en ny EC2-instans
# --image-id är AMI:n (Ubuntu, Amazon Linux, etc.)
# --instance-type bestämmer storlek (t3.micro är gratis tier)
# --key-name är SSH-nyckeln för inloggning
# --security-group-ids är brandväggen
# --count är antal instanser att starta

aws ec2 describe-instances \\
    --filters "Name=instance-state-name,Values=running" \\
    --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress,InstanceType]" \\
    --output table
# Listar alla körande instanser
# --filters begränsar till running instances
# --query väljer ut specifika fält (JMESPath)
# --output table ger snygg formatering
```

---

## Hantera instansens livscykel

```bash
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
# Stoppar instansen (som att stänga av en dator)
# Du betalar INTE för compute när instansen är stoppad
# EBS-volymer kostar fortfarande pengar
# Data på instans-storage försvinner!

aws ec2 start-instances --instance-ids i-1234567890abcdef0
# Startar en stoppad instans
# Kan ta 1-2 minuter innan den är tillgänglig
# Public IP ändras om du inte har Elastic IP

aws ec2 reboot-instances --instance-ids i-1234567890abcdef0
# Startar om instansen
# Snabbare än stop + start
# Public IP behålls

aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
# Tar bort instansen PERMANENT
# Alla data på instansen försvinner
# EBS-volymer raderas om DeleteOnTermination är true
# VARNING: Går inte att ångra!
```

---

## Security Groups

```bash
aws ec2 create-security-group \\
    --group-name web-server-sg \\
    --description "Security group for web servers" \\
    --vpc-id vpc-12345678
# Skapar en ny security group
# Börjar utan några regler (all trafik blockerad)
# --vpc-id anger vilken VPC den tillhör

aws ec2 authorize-security-group-ingress \\
    --group-id sg-12345678 \\
    --protocol tcp \\
    --port 22 \\
    --cidr 0.0.0.0/0
# Öppnar port 22 (SSH) från alla IP-adresser
# VARNING: 0.0.0.0/0 är hela internet - använd med försiktighet
# Bättre att begränsa till ditt kontor eller VPN

aws ec2 authorize-security-group-ingress \\
    --group-id sg-12345678 \\
    --protocol tcp \\
    --port 443 \\
    --cidr 0.0.0.0/0
# Öppnar port 443 (HTTPS) för webbtrafik
# Detta är säkert att öppna för hela internet
# Din webbserver behöver vara tillgänglig

aws ec2 describe-security-groups --group-ids sg-12345678
# Visar alla regler för security group
# IpPermissions visar ingress (inkommande)
# IpPermissionsEgress visar egress (utgående)
```

---

## SSH-nycklar

```bash
aws ec2 create-key-pair \\
    --key-name my-server-key \\
    --query 'KeyMaterial' \\
    --output text > my-server-key.pem
# Skapar ett nytt nyckelpar
# Private key sparas lokalt (my-server-key.pem)
# Public key sparas i AWS
# SPARA PRIVATE KEY - den kan aldrig hämtas igen!

chmod 400 my-server-key.pem
# Sätter rätt permissions på nyckeln
# SSH kräver att endast ägaren kan läsa
# Utan detta får du "permission denied"

ssh -i my-server-key.pem ec2-user@<public-ip>
# Ansluter till instansen via SSH
# ec2-user är standardanvändaren på Amazon Linux
# ubuntu är standardanvändaren på Ubuntu
# Använd public IP eller DNS-namn

aws ec2 describe-key-pairs
# Listar alla sparade nycklar i AWS
# Visar bara namn och fingerprint
# Private keys lagras INTE i AWS
```

---

## User Data - automatisk konfiguration

```bash
cat << 'EOF' > userdata.sh
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
EOF
# Skapar ett bootstrap-script
# Körs automatiskt när instansen startar första gången
# Körs som root - inget sudo behövs
# Perfekt för att installera mjukvara och konfigurera

aws ec2 run-instances \\
    --image-id ami-0c55b159cbfafe1f0 \\
    --instance-type t3.micro \\
    --key-name my-key \\
    --security-group-ids sg-12345678 \\
    --user-data file://userdata.sh
# Startar instans med user data
# file:// läser från lokal fil
# Scriptet körs vid första boot
# Loggar finns i /var/log/cloud-init-output.log
```

---

## Key Takeaways

1. **t3.micro är gratis** - perfekt för test och utveckling
2. **Security Groups är stateful** - reply-trafik tillåts automatiskt
3. **Stoppa istället för terminate** - om du vill spara instansen
4. **User Data för automation** - konfigurera instanser automatiskt
5. **Skydda dina SSH-nycklar** - de är nyckeln till dina servrar
""",
        },
        {
            "title": "VPC - Virtual Private Cloud",
            "slug": "vpc-virtual-private-cloud",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 90,
            "content": """# VPC - Virtual Private Cloud

## Varför behöver du kunna detta?

VPC är ditt privata nätverk i AWS - det isolerar dina resurser från andra kunder och internet. Som DevOps behöver du kunna:

- **Designa nätverksarkitektur** med publika och privata subnets
- **Kontrollera trafik** med route tables och network ACLs
- **Ansluta till internet** via Internet Gateway och NAT Gateway
- **Felsöka anslutningsproblem** genom att förstå nätverksflödet

---

## Så fungerar VPC

En VPC är ett virtuellt nätverk som du definierar med ett IP-adressintervall (CIDR block). Inuti VPC:n skapar du subnets i olika Availability Zones. Subnets kan vara publika (har route till internet) eller privata (ingen direkt internetåtkomst).

Tänk på VPC som ett kontorsbyggnad - du bestämmer vilka våningar som finns och vilka dörrar som leder vart.

---

## Skapa en VPC

```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=my-vpc}]'
# {
#     "Vpc": {
#         "VpcId": "vpc-1234567890abcdef0",
#         "CidrBlock": "10.0.0.0/16",
#         "State": "available"
#     }
# }
# Skapar en VPC med 65,536 IP-adresser (10.0.0.0 - 10.0.255.255)
# /16 är ett vanligt val - tillräckligt stort för de flesta projekt
# Mindre VPCs: /24 ger 256 adresser, /20 ger 4096 adresser

aws ec2 describe-vpcs --filters "Name=tag:Name,Values=my-vpc"
# Hittar VPC:n baserat på Name-taggen
# Visar VpcId, CidrBlock, State och DhcpOptionsId
# State bör vara "available"

aws ec2 modify-vpc-attribute --vpc-id vpc-12345678 --enable-dns-hostnames '{"Value":true}'
# Aktiverar DNS-hostnames för instanser i VPC:n
# EC2-instanser får automatiskt DNS-namn
# Krävs för många AWS-tjänster att fungera korrekt
```

---

## Skapa Subnets

```bash
aws ec2 create-subnet \\
    --vpc-id vpc-12345678 \\
    --cidr-block 10.0.1.0/24 \\
    --availability-zone eu-north-1a \\
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=public-subnet-1a}]'
# Skapar ett subnet med 256 IP-adresser
# Placeras i en specifik Availability Zone
# Namn indikerar att det kommer vara publikt
# AWS reserverar 5 adresser per subnet (.0, .1, .2, .3, .255)

aws ec2 create-subnet \\
    --vpc-id vpc-12345678 \\
    --cidr-block 10.0.2.0/24 \\
    --availability-zone eu-north-1b \\
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=public-subnet-1b}]'
# Andra publika subnet i annan AZ för redundans
# Samma storlek som första subnetet
# Tillsammans ger de high availability

aws ec2 create-subnet \\
    --vpc-id vpc-12345678 \\
    --cidr-block 10.0.10.0/24 \\
    --availability-zone eu-north-1a \\
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=private-subnet-1a}]'
# Privat subnet för databaser och backend
# Separerat CIDR-block (10.0.10.x vs 10.0.1.x)
# Kommer inte ha direkt internetåtkomst
```

---

## Internet Gateway

```bash
aws ec2 create-internet-gateway \\
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]'
# Skapar en Internet Gateway
# Behövs för att resurser ska nå internet
# En IGW per VPC är tillräckligt

aws ec2 attach-internet-gateway --internet-gateway-id igw-12345678 --vpc-id vpc-12345678
# Kopplar IGW till VPC:n
# Nu kan VPC:n kommunicera med internet
# Men subnets behöver fortfarande route tables

aws ec2 describe-internet-gateways --filters "Name=attachment.vpc-id,Values=vpc-12345678"
# Visar vilken IGW som är kopplad till VPC:n
# Attachments visar State: available
# En VPC kan bara ha en IGW
```

---

## Route Tables

```bash
aws ec2 create-route-table --vpc-id vpc-12345678 \\
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=public-rt}]'
# Skapar en route table för publika subnets
# Route tables bestämmer var trafik skickas
# Varje subnet associeras med en route table

aws ec2 create-route \\
    --route-table-id rtb-12345678 \\
    --destination-cidr-block 0.0.0.0/0 \\
    --gateway-id igw-12345678
# Lägger till default route till Internet Gateway
# 0.0.0.0/0 betyder "all trafik som inte matchar något annat"
# Detta gör subnetet publikt!

aws ec2 associate-route-table --route-table-id rtb-12345678 --subnet-id subnet-12345678
# Kopplar subnetet till route table
# Nu kan instanser i subnetet nå internet
# Glöm inte att associera alla publika subnets

aws ec2 describe-route-tables --route-table-ids rtb-12345678
# Visar alla routes i tabellen
# local route finns alltid (trafik inom VPC)
# 0.0.0.0/0 -> igw visar internetåtkomst
```

---

## NAT Gateway för privata subnets

```bash
aws ec2 allocate-address --domain vpc
# {
#     "PublicIp": "52.95.1.1",
#     "AllocationId": "eipalloc-12345678"
# }
# Allokerar en Elastic IP för NAT Gateway
# NAT Gateway behöver en publik IP
# Denna IP kostar pengar även när den inte används

aws ec2 create-nat-gateway \\
    --subnet-id subnet-12345678 \\
    --allocation-id eipalloc-12345678 \\
    --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=my-nat}]'
# Skapar NAT Gateway i ett PUBLIKT subnet
# Privata subnets routar genom denna för internetåtkomst
# Tar några minuter att bli available

aws ec2 create-route \\
    --route-table-id rtb-private \\
    --destination-cidr-block 0.0.0.0/0 \\
    --nat-gateway-id nat-12345678
# Lägger till route från privat subnet till NAT
# Instanser kan nå ut men internet kan inte nå in
# Perfekt för databaser som behöver hämta uppdateringar
```

---

## Key Takeaways

1. **VPC isolerar dina resurser** - ditt eget privata nätverk i molnet
2. **Publika subnets har route till IGW** - privata har det inte
3. **Minst 2 AZs för redundans** - alltid ha subnets i flera zoner
4. **NAT Gateway kostar pengar** - stäng av i dev om möjligt
5. **CIDR-planering är viktig** - tänk på framtida tillväxt
""",
        },
        {
            "title": "S3 - Simple Storage Service",
            "slug": "s3-simple-storage-service",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# S3 - Simple Storage Service

## Varför behöver du kunna detta?

S3 är AWS objektlagring - oändligt skalbar, billig och extremt tillförlitlig (99.999999999% durability). Som DevOps använder du S3 för:

- **Statisk webbhosting** för frontend-applikationer
- **Backup och arkivering** av data och loggar
- **Artifact storage** för build-outputs och Docker images
- **Data lake** för analytics och machine learning

---

## Så fungerar S3

S3 lagrar objekt (filer) i buckets (behållare). Varje objekt identifieras av en unik key (sökväg). Buckets har globalt unika namn - om någon annan har tagit namnet kan du inte använda det.

Tänk på S3 som en oändligt stor filserver där du betalar per GB lagring och per request.

---

## Skapa och hantera buckets

```bash
aws s3 mb s3://my-unique-bucket-name-12345
# make bucket - skapar en ny bucket
# Namnet måste vara globalt unikt i hela AWS
# Använd datum eller slumpmässiga suffix för unikhet
# Bucket skapas i din default region

aws s3 ls
# Listar alla dina buckets
# Visar CreationDate och BucketName
# Snabb överblick av ditt S3-innehav

aws s3 ls s3://my-bucket/
# Listar innehållet i en specifik bucket
# Visar LastModified, Size och Key (filnamn)
# Lägg till --recursive för alla undermappar

aws s3 rb s3://my-empty-bucket
# remove bucket - tar bort en TOM bucket
# Bucket måste vara helt tom först
# Använd --force för att ta bort bucket och innehåll
```

---

## Ladda upp och ner filer

```bash
aws s3 cp myfile.txt s3://my-bucket/
# Kopierar lokal fil till S3
# Filen får samma namn i bucket
# Lägg till path för att organisera: s3://my-bucket/folder/myfile.txt

aws s3 cp s3://my-bucket/myfile.txt ./
# Laddar ner fil från S3 till nuvarande katalog
# Skriver över om filen redan finns lokalt
# Använd --recursive för hela mappar

aws s3 sync ./my-folder s3://my-bucket/backup/
# Synkroniserar lokal mapp till S3
# Bara ändrade filer kopieras (inkrementell)
# Perfekt för backups och deployments

aws s3 sync s3://my-bucket/backup/ ./restored/
# Synkroniserar S3 till lokal mapp
# Laddar bara ner nya eller ändrade filer
# Snabbare än att ladda ner allt varje gång
```

---

## Hantera objekt

```bash
aws s3 rm s3://my-bucket/unwanted-file.txt
# Tar bort ett enskilt objekt
# Permanent om versioning är av
# Med versioning skapas en delete marker

aws s3 rm s3://my-bucket/old-folder/ --recursive
# Tar bort alla objekt i en mapp
# --recursive krävs för mappar
# VARNING: Går inte att ångra utan versioning!

aws s3 mv s3://my-bucket/old-name.txt s3://my-bucket/new-name.txt
# Byter namn på ett objekt
# Tekniskt en copy + delete operation
# Fungerar även mellan buckets

aws s3 presign s3://my-bucket/private-file.txt --expires-in 3600
# Skapar en tidsbegränsad URL för nedladdning
# --expires-in är sekunder (3600 = 1 timme)
# Perfekt för att dela privata filer tillfälligt
# URL:en innehåller signatur som autentiserar
```

---

## Bucket policies och åtkomst

```bash
cat << 'EOF' > bucket-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-website-bucket/*"
        }
    ]
}
EOF
# Policy för att göra bucket publikt läsbar
# Principal: "*" betyder alla (anonyma användare)
# Action: s3:GetObject tillåter nedladdning
# Resource: /* betyder alla objekt i bucket

aws s3api put-bucket-policy \\
    --bucket my-website-bucket \\
    --policy file://bucket-policy.json
# Applicerar policy på bucket
# Alla kan nu ladda ner filer från bucket
# Perfekt för statisk webbhosting

aws s3api get-bucket-policy --bucket my-bucket
# Visar nuvarande bucket policy
# Returnerar JSON-dokumentet
# Tomt om ingen policy är satt
```

---

## Statisk webbhosting

```bash
aws s3 website s3://my-website-bucket/ \\
    --index-document index.html \\
    --error-document error.html
# Aktiverar statisk webbhosting
# index.html visas för rot-URL
# error.html visas vid 404
# Bucket måste ha publik läsåtkomst

aws s3 sync ./dist s3://my-website-bucket/
# Laddar upp din byggda webbapp
# React, Vue, Angular - alla fungerar
# Glöm inte att bygga först (npm run build)

echo "Website URL: http://my-website-bucket.s3-website.eu-north-1.amazonaws.com"
# S3-webbplatsens URL
# Formatet är bucket.s3-website.region.amazonaws.com
# Använd CloudFront för HTTPS och bättre prestanda
```

---

## Key Takeaways

1. **Bucket-namn är globalt unika** - använd prefix eller suffix
2. **sync är inkrementell** - snabbare än att kopiera allt
3. **presign för tillfällig åtkomst** - dela privata filer säkert
4. **S3 för statisk hosting** - billigt och enkelt för frontend
5. **Bucket policies för publik åtkomst** - var försiktig med Principal: *
""",
        },
        {
            "title": "RDS - Relational Database Service",
            "slug": "rds-relational-database-service",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# RDS - Relational Database Service

## Varför behöver du kunna detta?

RDS är AWS managed database service - du slipper installera, patcha och säkerhetskopiera databaser själv. Som DevOps behöver du kunna:

- **Skapa och konfigurera databaser** för applikationer
- **Hantera backups och snapshots** för disaster recovery
- **Skala upp och ner** baserat på load
- **Konfigurera high availability** med Multi-AZ

---

## Så fungerar RDS

RDS hanterar databasadministration åt dig - patching, backups, failover. Du väljer databasmotor (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora) och instansstorlek. RDS kör i din VPC och skyddas av Security Groups.

Tänk på RDS som "database as a service" - du fokuserar på datan, AWS sköter infrastrukturen.

---

## Skapa en RDS-instans

```bash
aws rds create-db-instance \\
    --db-instance-identifier my-postgres-db \\
    --db-instance-class db.t3.micro \\
    --engine postgres \\
    --engine-version 15.4 \\
    --master-username admin \\
    --master-user-password MySecretPass123! \\
    --allocated-storage 20 \\
    --vpc-security-group-ids sg-12345678 \\
    --db-subnet-group-name my-db-subnet-group \\
    --backup-retention-period 7 \\
    --no-publicly-accessible
# Skapar en PostgreSQL-databas
# --db-instance-class bestämmer CPU och RAM
# --allocated-storage är disk i GB
# --backup-retention-period är dagar att spara backups
# --no-publicly-accessible = bara åtkomst inom VPC

aws rds describe-db-instances --db-instance-identifier my-postgres-db
# Visar status och detaljer
# DBInstanceStatus: creating -> available
# Endpoint.Address är hostname att ansluta till
# Tar 5-15 minuter att skapa
```

---

## Subnet Groups

```bash
aws rds create-db-subnet-group \\
    --db-subnet-group-name my-db-subnet-group \\
    --db-subnet-group-description "Subnets for RDS" \\
    --subnet-ids subnet-11111111 subnet-22222222
# Skapar en grupp av subnets för RDS
# Måste innehålla subnets i minst 2 AZs
# RDS placerar instansen i ett av dessa subnets
# Krävs före create-db-instance

aws rds describe-db-subnet-groups
# Listar alla subnet groups
# Visar vilka subnets och AZs som ingår
# SubnetGroupStatus bör vara "Complete"
```

---

## Parameter Groups och Option Groups

```bash
aws rds create-db-parameter-group \\
    --db-parameter-group-name my-postgres-params \\
    --db-parameter-group-family postgres15 \\
    --description "Custom PostgreSQL parameters"
# Skapar en parameter group för databasinställningar
# Familjen måste matcha engine-version
# Kopiera från default och anpassa

aws rds modify-db-parameter-group \\
    --db-parameter-group-name my-postgres-params \\
    --parameters "ParameterName=log_statement,ParameterValue=all,ApplyMethod=pending-reboot"
# Ändrar en databasparameter
# log_statement=all loggar alla queries
# ApplyMethod: immediate eller pending-reboot
# Vissa ändringar kräver omstart

aws rds modify-db-instance \\
    --db-instance-identifier my-postgres-db \\
    --db-parameter-group-name my-postgres-params \\
    --apply-immediately
# Applicerar parameter group på instansen
# --apply-immediately gör ändringen nu
# Utan flaggan väntar den till maintenance window
```

---

## Backups och Snapshots

```bash
aws rds create-db-snapshot \\
    --db-instance-identifier my-postgres-db \\
    --db-snapshot-identifier my-db-snapshot-20241215
# Skapar en manuell snapshot
# Automatiska backups är inkrementella, snapshots är fullständiga
# Snapshots finns kvar tills du tar bort dem
# Bra att ta före stora ändringar

aws rds describe-db-snapshots \\
    --db-instance-identifier my-postgres-db
# Listar alla snapshots för instansen
# Visar Status, SnapshotCreateTime och AllocatedStorage
# Status: creating -> available

aws rds restore-db-instance-from-db-snapshot \\
    --db-instance-identifier my-restored-db \\
    --db-snapshot-identifier my-db-snapshot-20241215
# Återställer från snapshot till NY instans
# Kan inte återställa till befintlig instans
# Den nya instansen har samma data som snapshot
# Uppdatera connection string i applikationen

aws rds delete-db-snapshot --db-snapshot-identifier my-db-snapshot-20241215
# Tar bort en snapshot
# Frigör lagringskostnader
# VARNING: Kan inte återställas efter borttagning
```

---

## Multi-AZ för High Availability

```bash
aws rds modify-db-instance \\
    --db-instance-identifier my-postgres-db \\
    --multi-az \\
    --apply-immediately
# Aktiverar Multi-AZ deployment
# AWS skapar en standby-instans i annan AZ
# Automatisk failover vid problem
# Kostar ungefär dubbelt så mycket

aws rds describe-db-instances \\
    --db-instance-identifier my-postgres-db \\
    --query "DBInstances[0].{MultiAZ:MultiAZ,SecondaryAZ:SecondaryAvailabilityZone}"
# Visar Multi-AZ status
# SecondaryAZ visar var standby finns
# Vid failover blir standby primary

aws rds reboot-db-instance \\
    --db-instance-identifier my-postgres-db \\
    --force-failover
# Testar failover manuellt
# --force-failover byter till standby
# Bra för att testa att failover fungerar
# Kortare avbrott än vanlig omstart
```

---

## Ansluta till RDS

```bash
aws rds describe-db-instances \\
    --db-instance-identifier my-postgres-db \\
    --query "DBInstances[0].Endpoint.Address" \\
    --output text
# Hämtar endpointens hostname
# Använd detta i din connection string
# Formatet är: instance-id.random.region.rds.amazonaws.com

psql -h my-postgres-db.abc123.eu-north-1.rds.amazonaws.com \\
    -U admin \\
    -d postgres
# Ansluter med psql-klienten
# -h hostname från endpoint
# -U är master username
# Du blir promptad för lösenord
# Kräver att Security Group tillåter port 5432
```

---

## Key Takeaways

1. **RDS hanterar admin** - patching, backups, failover automatiskt
2. **Subnet Groups krävs** - minst 2 AZs för RDS
3. **Multi-AZ för produktion** - automatisk failover vid problem
4. **Snapshots före ändringar** - enkelt att återställa
5. **Security Groups** - begränsa åtkomst till applikationsservrar
""",
        },
        {
            "title": "ECS - Elastic Container Service",
            "slug": "ecs-elastic-container-service",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 95,
            "content": """# ECS - Elastic Container Service

## Varför behöver du kunna detta?

ECS är AWS tjänst för att köra Docker-containers i produktion. Som DevOps behöver du kunna:

- **Deploya containeriserade applikationer** med hög tillgänglighet
- **Skala automatiskt** baserat på CPU/minnesanvändning
- **Integrera med andra AWS-tjänster** som ALB, CloudWatch och Secrets Manager
- **Välja mellan Fargate och EC2** launch types för olika behov

---

## Så fungerar ECS

ECS har tre huvudkomponenter:
- **Cluster** - logisk gruppering av resurser
- **Task Definition** - blueprint för hur containers ska köras
- **Service** - kör och underhåller önskat antal tasks

Med Fargate slipper du hantera servrar - AWS kör dina containers. Med EC2 launch type har du mer kontroll men måste hantera instanserna.

---

## Skapa ett ECS Cluster

```bash
aws ecs create-cluster --cluster-name my-cluster
# {
#     "cluster": {
#         "clusterArn": "arn:aws:ecs:eu-north-1:123456789012:cluster/my-cluster",
#         "clusterName": "my-cluster",
#         "status": "ACTIVE"
#     }
# }
# Skapar ett tomt cluster
# Med Fargate behövs ingen underliggande infrastruktur
# Cluster är bara en logisk gruppering

aws ecs list-clusters
# Listar alla dina clusters
# Visar bara ARN:s - använd describe för detaljer
# Bra för att verifiera att cluster skapades

aws ecs describe-clusters --clusters my-cluster
# Visar detaljerad info om cluster
# registeredContainerInstancesCount (EC2 mode)
# runningTasksCount och pendingTasksCount
# status bör vara ACTIVE
```

---

## Task Definition

```bash
cat << 'EOF' > task-def.json
{
    "family": "my-web-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
    "containerDefinitions": [
        {
            "name": "web",
            "image": "nginx:latest",
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
                    "awslogs-group": "/ecs/my-web-app",
                    "awslogs-region": "eu-north-1",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]
}
EOF
# Task definition i JSON-format
# family är namnet (versioneras automatiskt)
# cpu/memory i Fargate-enheter (256 cpu = 0.25 vCPU)
# containerDefinitions listar alla containers i tasken

aws ecs register-task-definition --cli-input-json file://task-def.json
# Registrerar task definition
# Skapar revision 1 (ökar för varje uppdatering)
# Task definition är immutable - ändringar skapar ny revision

aws ecs list-task-definitions --family-prefix my-web-app
# Listar alla revisioner av task definition
# Senaste revisionen är den som används
# Äldre revisioner kan användas för rollback
```

---

## Skapa en ECS Service

```bash
aws ecs create-service \\
    --cluster my-cluster \\
    --service-name my-web-service \\
    --task-definition my-web-app:1 \\
    --desired-count 2 \\
    --launch-type FARGATE \\
    --network-configuration "awsvpcConfiguration={subnets=[subnet-111,subnet-222],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
# Skapar en service som kör 2 tasks
# --desired-count är antal tasks att underhålla
# FARGATE = AWS hanterar servrarna
# awsvpcConfiguration anger nätverksinställningar

aws ecs describe-services --cluster my-cluster --services my-web-service
# Visar service-status
# runningCount ska matcha desiredCount
# events visar vad som hänt (deployment, errors)
# deployments visar aktiva deploymenter

aws ecs list-tasks --cluster my-cluster --service-name my-web-service
# Listar alla tasks i servicen
# Visar taskArn för varje körande task
# Använd describe-tasks för mer detaljer
```

---

## Uppdatera en Service

```bash
aws ecs update-service \\
    --cluster my-cluster \\
    --service-name my-web-service \\
    --task-definition my-web-app:2
# Rullar ut ny version av task definition
# ECS startar nya tasks med nya versionen
# Gamla tasks stoppas när nya är healthy
# Zero-downtime deployment

aws ecs update-service \\
    --cluster my-cluster \\
    --service-name my-web-service \\
    --desired-count 4
# Skalar upp till 4 tasks
# Nya tasks startas omedelbart
# Perfekt för att hantera ökad load

aws ecs update-service \\
    --cluster my-cluster \\
    --service-name my-web-service \\
    --desired-count 0
# Skalar ner till 0 tasks
# Stoppar alla körande containers
# Service finns kvar men kör inget
# Bra för att spara pengar i dev
```

---

## ECR - Container Registry

```bash
aws ecr create-repository --repository-name my-app
# Skapar ett privat container registry
# Här pushar du dina Docker images
# Integrerat med ECS och IAM

aws ecr get-login-password | docker login --username AWS --password-stdin 123456789012.dkr.ecr.eu-north-1.amazonaws.com
# Loggar in Docker mot ECR
# Tokenen gäller i 12 timmar
# Krävs före docker push

docker tag my-app:latest 123456789012.dkr.ecr.eu-north-1.amazonaws.com/my-app:latest
# Taggar imagen med ECR-repository
# Formatet är: account.dkr.ecr.region.amazonaws.com/repo:tag
# latest och version tags är vanliga

docker push 123456789012.dkr.ecr.eu-north-1.amazonaws.com/my-app:latest
# Pushar imagen till ECR
# Uppdatera task definition med nya image-URIn
# ECS drar automatiskt från ECR
```

---

## Key Takeaways

1. **Fargate = serverless containers** - AWS hanterar infrastrukturen
2. **Task Definition är blueprint** - versioneras automatiskt
3. **Service underhåller desired count** - startar om kraschade tasks
4. **ECR för privata images** - integrerat med IAM
5. **Rolling deployment** - zero-downtime updates
""",
        },
        {
            "title": "EKS - Elastic Kubernetes Service",
            "slug": "eks-elastic-kubernetes-service",
            "difficulty": "advanced",
            "estimated_minutes": 65,
            "xp_reward": 100,
            "content": """# EKS - Elastic Kubernetes Service

## Varför behöver du kunna detta?

EKS är AWS managed Kubernetes service - du får kraften av Kubernetes utan att hantera control plane. Som DevOps behöver du kunna:

- **Skapa och hantera EKS-kluster** för containerorkestreringsplattform
- **Konfigurera node groups** för compute capacity
- **Integrera med AWS-tjänster** som IAM, ALB och CloudWatch
- **Använda kubectl** för att hantera workloads

---

## Så fungerar EKS

EKS kör Kubernetes control plane (API server, etcd, scheduler) i AWS managed infrastruktur med hög tillgänglighet över flera AZs. Du hanterar worker nodes via node groups - antingen EC2-instanser eller Fargate för serverless.

Tänk på EKS som Kubernetes-as-a-Service - du fokuserar på workloads, AWS sköter mastern.

---

## Skapa ett EKS-kluster

```bash
eksctl create cluster \\
    --name my-eks-cluster \\
    --region eu-north-1 \\
    --version 1.28 \\
    --nodegroup-name standard-workers \\
    --node-type t3.medium \\
    --nodes 2 \\
    --nodes-min 1 \\
    --nodes-max 4
# eksctl är det rekommenderade verktyget för EKS
# Skapar kluster med managed node group
# --version är Kubernetes-version
# --nodes är initial antal worker nodes
# Tar 15-20 minuter att skapa

aws eks describe-cluster --name my-eks-cluster
# Visar klusterstatus och konfiguration
# status: CREATING -> ACTIVE
# endpoint är API server URL
# certificateAuthority för kubectl

aws eks list-clusters
# Listar alla EKS-kluster i regionen
# Enkel överblick av dina kluster
# Returnerar bara namn - använd describe för detaljer
```

---

## Konfigurera kubectl

```bash
aws eks update-kubeconfig --name my-eks-cluster --region eu-north-1
# Konfigurerar kubectl att prata med EKS
# Uppdaterar ~/.kube/config
# Använder IAM för autentisering
# Du kan nu köra kubectl-kommandon

kubectl get nodes
# Visar alla worker nodes i klustret
# STATUS bör vara Ready
# VERSION visar Kubernetes-version
# AGE visar hur länge noden funnits

kubectl cluster-info
# Visar kluster-endpoints
# Kubernetes control plane URL
# CoreDNS service URL
# Verifierar att anslutningen fungerar
```

---

## Node Groups

```bash
eksctl create nodegroup \\
    --cluster my-eks-cluster \\
    --name spot-workers \\
    --node-type t3.large \\
    --nodes 3 \\
    --spot
# Skapar en ny node group med spot instances
# --spot ger upp till 90% rabatt men kan tas tillbaka
# Bra för batch-jobb och stateless workloads
# Blanda on-demand och spot för balans

aws eks list-nodegroups --cluster-name my-eks-cluster
# Listar alla node groups i klustret
# Visar namn på varje grupp
# Olika grupper för olika workloads

eksctl scale nodegroup \\
    --cluster my-eks-cluster \\
    --name standard-workers \\
    --nodes 5
# Skalar node group till 5 noder
# Nya noder startas automatiskt
# Pods schemaläggs på nya noder

eksctl delete nodegroup \\
    --cluster my-eks-cluster \\
    --name spot-workers
# Tar bort en node group
# Pods evicteras först
# Nodes termineras
# Klustret fortsätter med andra node groups
```

---

## EKS med Fargate

```bash
eksctl create fargateprofile \\
    --cluster my-eks-cluster \\
    --name my-fargate-profile \\
    --namespace default \\
    --labels app=backend
# Skapar Fargate-profil för serverless pods
# --namespace anger vilka namespaces som matchar
# --labels ytterligare matchning
# Pods som matchar körs på Fargate

kubectl apply -f - << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: fargate-test
  namespace: default
  labels:
    app: backend
spec:
  containers:
  - name: nginx
    image: nginx:latest
EOF
# Skapar en pod som matchar Fargate-profilen
# Körs automatiskt på Fargate istället för EC2
# Ingen förhandsallokering av kapacitet
# Betala per pod-sekund

kubectl get pods -o wide
# Visar pods och vilken node de kör på
# Fargate-noder har namn som fargate-ip-x-x-x-x
# EC2-noder har namn som ip-x-x-x-x
```

---

## AWS Load Balancer Controller

```bash
eksctl create iamserviceaccount \\
    --cluster my-eks-cluster \\
    --namespace kube-system \\
    --name aws-load-balancer-controller \\
    --attach-policy-arn arn:aws:iam::123456789012:policy/AWSLoadBalancerControllerIAMPolicy \\
    --override-existing-serviceaccounts \\
    --approve
# Skapar IAM service account för controller
# IRSA (IAM Roles for Service Accounts)
# Controller behöver skapa ALBs och NLBs
# Säker integration med IAM

helm repo add eks https://aws.github.io/eks-charts
helm repo update
# Lägger till AWS Helm repository
# Innehåller EKS-specifika charts
# update hämtar senaste versioner

helm install aws-load-balancer-controller eks/aws-load-balancer-controller \\
    -n kube-system \\
    --set clusterName=my-eks-cluster \\
    --set serviceAccount.create=false \\
    --set serviceAccount.name=aws-load-balancer-controller
# Installerar controller med Helm
# Skapar inte service account (gjordes ovan)
# Lyssnar på Ingress-resurser
# Skapar automatiskt ALBs
```

---

## Deploying till EKS

```bash
kubectl apply -f - << 'EOF'
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
    targetPort: 80
EOF
# Skapar Deployment och Service
# 3 replicas för high availability
# Service type LoadBalancer skapar AWS ELB
# Trafiken lastbalanseras mellan pods

kubectl get svc web-service
# Visar service med EXTERNAL-IP
# ELB DNS-namn i EXTERNAL-IP kolumnen
# Kan ta några minuter att provisionera
# Använd detta DNS-namn för att nå appen
```

---

## Key Takeaways

1. **EKS = managed Kubernetes** - AWS sköter control plane
2. **eksctl förenklar** - skapa kluster med ett kommando
3. **Fargate för serverless** - inga noder att hantera
4. **IRSA för säker IAM** - pods får egna IAM-roller
5. **ALB Ingress Controller** - AWS-native lastbalansering
""",
        },
        {
            "title": "Lambda - Serverless Functions",
            "slug": "lambda-serverless-functions",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Lambda - Serverless Functions

## Varför behöver du kunna detta?

Lambda är AWS serverless compute - kör kod utan att hantera servrar. Som DevOps behöver du kunna:

- **Deploya funktioner** för event-driven arkitektur
- **Konfigurera triggers** från S3, API Gateway, SNS etc.
- **Hantera miljövariabler** och secrets
- **Optimera prestanda** med rätt minneskonfiguration

---

## Så fungerar Lambda

Lambda kör din kod som svar på events. Du betalar bara för exekveringstid (faktureras per millisekund). Lambda hanterar:
- Skalning (från 0 till tusentals samtidiga körningar)
- High availability (multi-AZ automatiskt)
- Patching och infrastruktur

Tänk på Lambda som "function as a service" - du skriver funktioner, AWS kör dem.

---

## Skapa en Lambda-funktion

```bash
cat << 'EOF' > lambda_function.py
import json

def lambda_handler(event, context):
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}!'})
    }
EOF
# Skapar en enkel Lambda-funktion i Python
# lambda_handler är default entry point
# event innehåller input-data
# context har runtime-information

zip function.zip lambda_function.py
# Paketerar koden i en zip-fil
# Lambda kräver zip eller container image
# Inkludera dependencies i zippen

aws lambda create-function \\
    --function-name my-hello-function \\
    --runtime python3.11 \\
    --role arn:aws:iam::123456789012:role/lambda-execution-role \\
    --handler lambda_function.lambda_handler \\
    --zip-file fileb://function.zip
# Skapar Lambda-funktionen
# --runtime är programmeringsspråk/version
# --role är IAM-rollen funktionen kör som
# --handler är module.function_name
# fileb:// för binär fil
```

---

## Testa och anropa funktioner

```bash
aws lambda invoke \\
    --function-name my-hello-function \\
    --payload '{"name": "DevOps"}' \\
    --cli-binary-format raw-in-base64-out \\
    response.json
# Anropar funktionen synkront
# --payload är JSON-input till funktionen
# Output sparas i response.json
# StatusCode 200 = lyckad körning

cat response.json
# {"message": "Hello, DevOps!"}
# Visar funktionens svar
# body är det som returnerades

aws lambda invoke \\
    --function-name my-hello-function \\
    --invocation-type Event \\
    --payload '{"name": "Async"}' \\
    response.json
# Asynkron anrop (fire and forget)
# --invocation-type Event
# Returnerar 202 Accepted
# Kör i bakgrunden
```

---

## Uppdatera och versionshantera

```bash
aws lambda update-function-code \\
    --function-name my-hello-function \\
    --zip-file fileb://function.zip
# Uppdaterar funktionskoden
# Tidigare version skrivs över
# Ta snapshot först om du vill ha rollback

aws lambda publish-version \\
    --function-name my-hello-function \\
    --description "Initial release"
# Publicerar en oföränderlig version
# Returnerar VersionId (1, 2, 3...)
# Versioner kan inte ändras
# Bra för rollback

aws lambda create-alias \\
    --function-name my-hello-function \\
    --name prod \\
    --function-version 1
# Skapar ett alias som pekar på en version
# Anropa via alias: my-hello-function:prod
# Byt version utan att ändra triggers

aws lambda update-alias \\
    --function-name my-hello-function \\
    --name prod \\
    --function-version 2
# Uppdaterar alias till ny version
# Traffic shift till version 2
# Instant deployment
```

---

## Miljövariabler och konfiguration

```bash
aws lambda update-function-configuration \\
    --function-name my-hello-function \\
    --environment "Variables={DB_HOST=mydb.example.com,API_KEY=secret123}"
# Sätter miljövariabler
# Tillgängliga via os.environ i koden
# Krypteras automatiskt med KMS
# Ändring triggar cold start

aws lambda update-function-configuration \\
    --function-name my-hello-function \\
    --memory-size 512 \\
    --timeout 30
# Justerar minne och timeout
# Minne: 128 MB - 10 GB
# Timeout: 1 sek - 15 min
# Mer minne = mer CPU = snabbare

aws lambda get-function-configuration \\
    --function-name my-hello-function
# Visar all konfiguration
# MemorySize, Timeout, Environment
# Runtime, Handler, Role
# VpcConfig om ansluten till VPC
```

---

## Triggers och Event Sources

```bash
aws lambda add-permission \\
    --function-name my-hello-function \\
    --statement-id s3-trigger \\
    --action lambda:InvokeFunction \\
    --principal s3.amazonaws.com \\
    --source-arn arn:aws:s3:::my-bucket
# Ger S3 permission att trigga funktionen
# statement-id är en unik identifierare
# principal är AWS-tjänsten som anropar
# source-arn begränsar till specifik bucket

aws s3api put-bucket-notification-configuration \\
    --bucket my-bucket \\
    --notification-configuration '{
        "LambdaFunctionConfigurations": [{
            "LambdaFunctionArn": "arn:aws:lambda:eu-north-1:123456789012:function:my-hello-function",
            "Events": ["s3:ObjectCreated:*"]
        }]
    }'
# Konfigurerar S3 att trigga Lambda
# Events: ObjectCreated, ObjectRemoved, etc.
# Funktionen körs för varje nytt objekt
# Event innehåller bucket och key

aws lambda create-event-source-mapping \\
    --function-name my-hello-function \\
    --event-source-arn arn:aws:sqs:eu-north-1:123456789012:my-queue \\
    --batch-size 10
# Kopplar Lambda till SQS-kö
# Lambda pollar kön automatiskt
# batch-size är antal meddelanden per anrop
# Perfekt för asynkron bearbetning
```

---

## Key Takeaways

1. **Betala per millisekund** - ingen kostnad när inget körs
2. **Automatisk skalning** - från 0 till tusentals samtidigt
3. **Versioner för rollback** - publicera innan production
4. **Alias för deployment** - byt version utan triggers-ändring
5. **Cold starts** - första anropet tar längre tid
""",
        },
        {
            "title": "API Gateway - REST och HTTP APIs",
            "slug": "api-gateway-rest-http-apis",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# API Gateway - REST och HTTP APIs

## Varför behöver du kunna detta?

API Gateway är AWS tjänst för att skapa och hantera APIs. Som DevOps behöver du kunna:

- **Skapa REST/HTTP APIs** som frontend för Lambda eller andra backend-tjänster
- **Konfigurera säkerhet** med API keys, IAM, eller Cognito
- **Hantera stages** för dev, staging och production
- **Sätta upp throttling** för att skydda backend

---

## Så fungerar API Gateway

API Gateway är en managed tjänst som:
- Tar emot HTTP-requests från klienter
- Routar till rätt backend (Lambda, EC2, externa URLs)
- Hanterar autentisering, throttling och caching
- Transformerar requests/responses vid behov

Du har två huvudtyper:
- **REST API** - fullständig kontroll, mer features, högre kostnad
- **HTTP API** - enklare, snabbare, billigare (70% mindre)

---

## Skapa ett HTTP API

```bash
aws apigatewayv2 create-api \\
    --name my-http-api \\
    --protocol-type HTTP \\
    --target arn:aws:lambda:eu-north-1:123456789012:function:my-function
# Skapar ett HTTP API
# protocol-type HTTP (inte WEBSOCKET)
# --target skapar default route till Lambda
# Returnerar ApiId och ApiEndpoint

aws apigatewayv2 get-apis
# Listar alla HTTP APIs
# Visar ApiId, Name, ApiEndpoint
# ApiEndpoint är den publika URL:en
# Formatet: https://{api-id}.execute-api.{region}.amazonaws.com

curl https://abc123.execute-api.eu-north-1.amazonaws.com/
# Anropar API:et
# Default route skickar till Lambda
# Svar från Lambda returneras till klient
# Content-Type beror på Lambda response
```

---

## Konfigurera routes och integrationer

```bash
aws apigatewayv2 create-integration \\
    --api-id abc123 \\
    --integration-type AWS_PROXY \\
    --integration-uri arn:aws:lambda:eu-north-1:123456789012:function:users-function \\
    --payload-format-version 2.0
# Skapar en Lambda-integration
# AWS_PROXY skickar hela requesten till Lambda
# payload-format-version 2.0 är nyare format
# Returnerar IntegrationId

aws apigatewayv2 create-route \\
    --api-id abc123 \\
    --route-key "GET /users" \\
    --target integrations/int123
# Skapar en route
# route-key är HTTP-metod + path
# --target kopplar till integration
# GET /users -> users-function Lambda

aws apigatewayv2 create-route \\
    --api-id abc123 \\
    --route-key "POST /users" \\
    --target integrations/int123
# Samma integration, annan metod
# Lambda får info om metod i event
# event['requestContext']['http']['method']
# Logik i Lambda hanterar skillnaden

aws apigatewayv2 get-routes --api-id abc123
# Listar alla routes
# Visar RouteKey, Target, RouteId
# Använd för att verifiera setup
# DELETE /routes/{routeId} för att ta bort
```

---

## Stages och deployment

```bash
aws apigatewayv2 create-stage \\
    --api-id abc123 \\
    --stage-name dev \\
    --auto-deploy
# Skapar en stage
# stage-name blir del av URL
# --auto-deploy deployer automatiskt
# URL: https://{api-id}.execute-api.{region}.amazonaws.com/dev

aws apigatewayv2 create-stage \\
    --api-id abc123 \\
    --stage-name prod
# Prod-stage utan auto-deploy
# Kräver manuell deployment
# Säkrare för production
# Kontrollera exakt vad som deployas

aws apigatewayv2 create-deployment \\
    --api-id abc123 \\
    --stage-name prod
# Deployer till prod stage
# Tar aktuell API-config
# Alla routes och integrationer
# Atomic - allt eller inget

aws apigatewayv2 update-stage \\
    --api-id abc123 \\
    --stage-name prod \\
    --stage-variables "ENV=production,DB_HOST=prod-db.example.com"
# Stage variables - miljövariabler per stage
# Tillgängliga i Lambda via event
# Använd för config per miljö
# stageVariables['ENV'] i Lambda
```

---

## Throttling och säkerhet

```bash
aws apigatewayv2 update-stage \\
    --api-id abc123 \\
    --stage-name prod \\
    --default-route-settings '{"ThrottlingBurstLimit": 100, "ThrottlingRateLimit": 50}'
# Sätter throttling för alla routes
# BurstLimit: max samtidiga requests
# RateLimit: requests per sekund
# Skyddar backend mot överbelastning

aws apigatewayv2 update-api \\
    --api-id abc123 \\
    --cors-configuration '{
        "AllowOrigins": ["https://example.com"],
        "AllowMethods": ["GET", "POST"],
        "AllowHeaders": ["Authorization", "Content-Type"]
    }'
# Konfigurerar CORS
# AllowOrigins: tillåtna domäner
# AllowMethods: tillåtna HTTP-metoder
# Viktigt för webb-klienter

aws apigatewayv2 create-authorizer \\
    --api-id abc123 \\
    --authorizer-type JWT \\
    --identity-source '$request.header.Authorization' \\
    --name cognito-auth \\
    --jwt-configuration '{
        "Audience": ["my-app-client-id"],
        "Issuer": "https://cognito-idp.eu-north-1.amazonaws.com/eu-north-1_abc123"
    }'
# JWT authorizer med Cognito
# Validerar tokens automatiskt
# identity-source är var token finns
# 401 om token saknas/ogiltig
```

---

## Key Takeaways

1. **HTTP API för de flesta fall** - billigare och snabbare
2. **Routes + Integrations** - koppla URL-paths till backends
3. **Stages för miljöer** - dev, staging, prod
4. **Auto-deploy för dev** - snabbare iteration
5. **Throttling skyddar backend** - sätt alltid limits
""",
        },
        {
            "title": "CloudWatch - Monitoring och Logging",
            "slug": "cloudwatch-monitoring-logging",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# CloudWatch - Monitoring och Logging

## Varför behöver du kunna detta?

CloudWatch är AWS centrala monitoring- och loggningstjänst. Som DevOps behöver du kunna:

- **Samla och söka loggar** från alla AWS-tjänster
- **Skapa metrics och dashboards** för att visualisera prestanda
- **Sätta upp alarms** som notifierar vid problem
- **Automatisera actions** baserat på metrics

---

## Så fungerar CloudWatch

CloudWatch består av flera komponenter:
- **Logs** - samla och sök i loggdata
- **Metrics** - tidsserie-data för resurser
- **Alarms** - notifieringar vid tröskelvärden
- **Dashboards** - visualisering av metrics

Alla AWS-tjänster skickar automatiskt metrics till CloudWatch. Loggar måste ofta konfigureras explicit.

---

## CloudWatch Logs

```bash
aws logs create-log-group \\
    --log-group-name /app/my-service
# Skapar en log group
# Log groups organiserar loggar per app/tjänst
# /app/prefix är konvention
# Retention är obegränsad default

aws logs put-retention-policy \\
    --log-group-name /app/my-service \\
    --retention-in-days 30
# Sätter retention policy
# Raderar loggar äldre än 30 dagar
# Sparar lagringskostnader
# Vanliga värden: 7, 14, 30, 90, 365

aws logs describe-log-streams \\
    --log-group-name /app/my-service \\
    --order-by LastEventTime \\
    --descending
# Listar log streams i gruppen
# En stream per instans/container
# order-by sorterar efter senaste logg
# Visar logStreamName att använda

aws logs get-log-events \\
    --log-group-name /app/my-service \\
    --log-stream-name i-abc123 \\
    --limit 50
# Hämtar logghändelser
# --limit begränsar antal
# Returnerar events med timestamp
# message innehåller loggtext
```

---

## Logs Insights - sökning

```bash
aws logs start-query \\
    --log-group-name /app/my-service \\
    --start-time $(date -d '1 hour ago' +%s) \\
    --end-time $(date +%s) \\
    --query-string 'fields @timestamp, @message | filter @message like /ERROR/ | limit 20'
# Startar en Logs Insights-query
# Returnerar queryId
# Asynkron - resultat hämtas separat
# Query language liknande SQL

aws logs get-query-results \\
    --query-id abc123-def456
# Hämtar query-resultat
# status: Running, Complete, Failed
# results innehåller matchande loggar
# Kör flera gånger tills Complete

aws logs filter-log-events \\
    --log-group-name /app/my-service \\
    --filter-pattern "ERROR" \\
    --start-time $(date -d '1 hour ago' +%s)000
# Enklare synkron sökning
# filter-pattern är enkelt mönster
# start-time i millisekunder (lägg till 000)
# Bra för snabba sökningar

aws logs tail /app/my-service --follow
# Följer loggar i realtid
# Som tail -f för CloudWatch
# Ctrl+C för att avsluta
# Kräver AWS CLI v2
```

---

## CloudWatch Metrics

```bash
aws cloudwatch list-metrics \\
    --namespace AWS/EC2 \\
    --metric-name CPUUtilization
# Listar metrics
# namespace grupperar per tjänst
# AWS/EC2, AWS/RDS, AWS/Lambda etc.
# Visar Dimensions (InstanceId etc.)

aws cloudwatch get-metric-statistics \\
    --namespace AWS/EC2 \\
    --metric-name CPUUtilization \\
    --dimensions Name=InstanceId,Value=i-abc123 \\
    --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ) \\
    --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) \\
    --period 300 \\
    --statistics Average
# Hämtar metric-data
# period 300 = 5 minuters intervall
# statistics: Average, Sum, Min, Max
# Returnerar Datapoints array

aws cloudwatch put-metric-data \\
    --namespace Custom/MyApp \\
    --metric-name RequestLatency \\
    --value 150 \\
    --unit Milliseconds \\
    --dimensions Service=UserAPI
# Publicerar custom metric
# Custom/ namespace för egna metrics
# unit ger kontext (Milliseconds, Count, etc.)
# Dimensions för filtrering
```

---

## CloudWatch Alarms

```bash
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
# Skapar ett alarm
# Triggas när CPU > 80% i 2 perioder (10 min)
# alarm-actions är SNS topic för notifiering
# Skickar email, SMS, eller trigger Lambda

aws cloudwatch describe-alarms
# Listar alla alarms
# StateValue: OK, ALARM, INSUFFICIENT_DATA
# Visar när alarm senast ändrades
# Använd för att debugga

aws cloudwatch set-alarm-state \\
    --alarm-name high-cpu-alarm \\
    --state-value OK \\
    --state-reason "Manually reset"
# Manuellt återställer alarm
# Användbart för test eller override
# StateReason loggas
# Alarm går tillbaka om condition kvarstår

aws cloudwatch disable-alarm-actions \\
    --alarm-names high-cpu-alarm
# Stänger av alarm-actions
# Alarm övervakar fortfarande
# Bra under maintenance
# enable-alarm-actions för att aktivera igen
```

---

## Key Takeaways

1. **Log Groups organiserar** - en per app eller tjänst
2. **Retention sparar pengar** - sätt alltid policy
3. **Logs Insights för sökning** - kraftfullt query-språk
4. **Custom metrics för app-data** - skicka från din kod
5. **Alarms för proaktiv monitoring** - SNS för notifiering
""",
        },
        {
            "title": "CloudFormation - Infrastructure as Code",
            "slug": "cloudformation-infrastructure-as-code",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 95,
            "content": """# CloudFormation - Infrastructure as Code

## Varför behöver du kunna detta?

CloudFormation är AWS IaC-tjänst för att definiera infrastruktur som kod. Som DevOps behöver du kunna:

- **Definiera resurser** i YAML/JSON-templates
- **Skapa och uppdatera stacks** reproducerbart
- **Hantera beroenden** mellan resurser
- **Använda parametrar** för återanvändbara templates

---

## Så fungerar CloudFormation

CloudFormation tar en template (YAML eller JSON) och skapar en "stack" med alla definierade resurser. Fördelar:
- **Reproducerbart** - samma template ger samma infrastruktur
- **Versionskontroll** - templates i Git
- **Rollback** - vid fel rullas allt tillbaka
- **Dependency management** - CloudFormation förstår beroenden

---

## Grundläggande template-struktur

```bash
cat << 'EOF' > template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple S3 bucket with versioning

Parameters:
  BucketName:
    Type: String
    Description: Name of the S3 bucket
    Default: my-app-bucket

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub '\${BucketName}-\${AWS::AccountId}'
      VersioningConfiguration:
        Status: Enabled
      Tags:
        - Key: Environment
          Value: production

Outputs:
  BucketArn:
    Description: ARN of the created bucket
    Value: !GetAtt MyBucket.Arn
    Export:
      Name: !Sub '\${AWS::StackName}-BucketArn'
EOF
# AWSTemplateFormatVersion alltid 2010-09-09
# Parameters gör templaten återanvändbar
# Resources definierar AWS-resurser
# !Sub substituerar variabler
# !GetAtt hämtar resurs-attribut
# Outputs exporterar värden
```

---

## Skapa och hantera stacks

```bash
aws cloudformation create-stack \\
    --stack-name my-app-storage \\
    --template-body file://template.yaml \\
    --parameters ParameterKey=BucketName,ParameterValue=my-app-data
# Skapar en ny stack
# --stack-name unik identifierare
# file:// för lokal fil
# --parameters sätter parametervärden
# Returnerar StackId

aws cloudformation describe-stacks \\
    --stack-name my-app-storage
# Visar stack-status
# StackStatus: CREATE_IN_PROGRESS, CREATE_COMPLETE
# Om fel: CREATE_FAILED, ROLLBACK_COMPLETE
# Outputs visas när COMPLETE

aws cloudformation list-stack-resources \\
    --stack-name my-app-storage
# Listar alla resurser i stacken
# PhysicalResourceId är faktiska resurs-id
# ResourceStatus per resurs
# Användbart för debugging

aws cloudformation wait stack-create-complete \\
    --stack-name my-app-storage
# Väntar tills stack är klar
# Blockar tills CREATE_COMPLETE
# Exit code 0 = success
# Timeout efter ~25 min
```

---

## Uppdatera stacks

```bash
aws cloudformation update-stack \\
    --stack-name my-app-storage \\
    --template-body file://template-v2.yaml \\
    --parameters ParameterKey=BucketName,ParameterValue=my-app-data
# Uppdaterar befintlig stack
# CloudFormation beräknar diff
# Endast ändrade resurser uppdateras
# Vissa ändringar kräver replacement

aws cloudformation describe-stack-events \\
    --stack-name my-app-storage
# Visar alla händelser
# Kronologisk logg av skapande/uppdatering
# ResourceStatusReason vid fel
# Ovärderligt för debugging

aws cloudformation create-change-set \\
    --stack-name my-app-storage \\
    --change-set-name update-bucket \\
    --template-body file://template-v2.yaml
# Skapar change set utan att applicera
# Visar exakt vad som kommer ändras
# Action: Add, Modify, Remove
# Replacement: True om resursen återskapas

aws cloudformation execute-change-set \\
    --stack-name my-app-storage \\
    --change-set-name update-bucket
# Applicerar change set
# Säkrare än direkt update-stack
# Best practice för production
# Kan reviewas innan körning
```

---

## Template-funktioner och beroenden

```bash
cat << 'EOF' > multi-resource.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with subnet and security group

Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: !Sub '\${AWS::StackName}-vpc'

  PublicSubnet:
    Type: AWS::EC2::Subnet
    DependsOn: MyVPC
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: true

  WebSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP traffic
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0

Outputs:
  VpcId:
    Value: !Ref MyVPC
  SubnetId:
    Value: !Ref PublicSubnet
  SecurityGroupId:
    Value: !GetAtt WebSecurityGroup.GroupId
EOF
# !Ref refererar till resurs (returnerar ID)
# !GetAtt hämtar specifikt attribut
# !Select väljer från lista
# !GetAZs '' hämtar AZs i regionen
# DependsOn explicit beroende
# Implicita beroenden via !Ref
```

---

## Radera och skydda stacks

```bash
aws cloudformation delete-stack \\
    --stack-name my-app-storage
# Raderar stack och alla resurser
# VIKTIGT: tar bort allt i stacken
# Ingen confirmation prompt
# Vissa resurser kan ha deletion protection

aws cloudformation update-termination-protection \\
    --stack-name my-app-storage \\
    --enable-termination-protection
# Skyddar mot oavsiktlig radering
# delete-stack misslyckas
# Måste explicit stänga av först
# Best practice för production

aws cloudformation describe-stack-resources \\
    --stack-name my-app-storage \\
    --query 'StackResources[*].{Name:LogicalResourceId,Type:ResourceType,Status:ResourceStatus}'
# Query för att formatera output
# Visar resursnamn, typ och status
# --query använder JMESPath
# Perfekt för scripting
```

---

## Key Takeaways

1. **Infrastructure as Code** - versionskontrollera din infrastruktur
2. **Parameters för återanvändning** - samma template, olika miljöer
3. **Change sets för säkerhet** - granska innan applicering
4. **!Ref och !GetAtt** - referera mellan resurser
5. **Termination protection** - skydda production stacks
""",
        },
        {
            "title": "Route 53 - DNS och Routing",
            "slug": "route53-dns-routing",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Route 53 - DNS och Routing

## Varför behöver du kunna detta?

Route 53 är AWS DNS-tjänst för domänhantering och routing. Som DevOps behöver du kunna:

- **Hantera DNS-zoner** och records för dina domäner
- **Konfigurera routing policies** för high availability
- **Sätta upp health checks** för failover
- **Integrera med andra AWS-tjänster** via alias records

---

## Så fungerar Route 53

Route 53 är en globally distribuerad DNS-tjänst med 100% SLA. Funktioner:
- **Hosted Zones** - DNS-zoner för dina domäner
- **Record Sets** - DNS-poster (A, CNAME, MX, etc.)
- **Routing Policies** - simple, weighted, latency, failover, geolocation
- **Health Checks** - övervakar endpoints

---

## Skapa och hantera Hosted Zones

```bash
aws route53 create-hosted-zone \\
    --name example.com \\
    --caller-reference $(date +%s)
# Skapar en hosted zone
# caller-reference måste vara unik
# Returnerar HostedZoneId och NS records
# NS records konfigureras hos domänregistrar

aws route53 list-hosted-zones
# Listar alla hosted zones
# Visar Id, Name, ResourceRecordSetCount
# Id format: /hostedzone/Z1234567890
# Använd Id för att hantera records

aws route53 get-hosted-zone \\
    --id Z1234567890
# Hämtar zone-detaljer
# DelegationSet innehåller NS records
# ResourceRecordSetCount totalt antal records
# Config visar om privat eller publik

aws route53 list-resource-record-sets \\
    --hosted-zone-id Z1234567890
# Listar alla DNS records i zonen
# Name, Type, TTL, ResourceRecords
# Alias records har AliasTarget istället
# Pagination om många records
```

---

## Skapa DNS Records

```bash
aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "www.example.com",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [{"Value": "1.2.3.4"}]
            }
        }]
    }'
# Skapar A record
# Action: CREATE, DELETE, UPSERT
# TTL i sekunder (300 = 5 min)
# ResourceRecords innehåller IP-adresser
# UPSERT skapar eller uppdaterar

aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "api.example.com",
                "Type": "CNAME",
                "TTL": 300,
                "ResourceRecords": [{"Value": "api.otherdomain.com"}]
            }
        }]
    }'
# CNAME record pekar till annat domännamn
# Används för underdomäner
# Kan inte användas för root domain (example.com)
# Använd Alias istället för root

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
# Alias record till AWS-resurs
# Fungerar för root domain
# Ingen TTL - AWS hanterar det
# HostedZoneId är för CloudFront
# Gratis queries för alias till AWS
```

---

## Health Checks

```bash
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
# Skapar health check
# Kontrollerar /health var 30:e sekund
# FailureThreshold 3 = unhealthy efter 3 misslyckanden
# Type: HTTP, HTTPS, TCP
# Returnerar HealthCheckId

aws route53 get-health-check-status \\
    --health-check-id abc123
# Visar hälsostatus
# Status från alla Route 53 health checkers
# StatusReport per region
# Aggregerad status i StatusReport
```

---

## Routing Policies

```bash
aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "api.example.com",
                "Type": "A",
                "SetIdentifier": "primary",
                "Failover": "PRIMARY",
                "TTL": 60,
                "ResourceRecords": [{"Value": "1.2.3.4"}],
                "HealthCheckId": "abc123"
            }
        }, {
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "api.example.com",
                "Type": "A",
                "SetIdentifier": "secondary",
                "Failover": "SECONDARY",
                "TTL": 60,
                "ResourceRecords": [{"Value": "5.6.7.8"}]
            }
        }]
    }'
# Failover routing
# PRIMARY används om health check OK
# SECONDARY vid failover
# SetIdentifier unikt namn per record
# Health check krävs för PRIMARY

aws route53 change-resource-record-sets \\
    --hosted-zone-id Z1234567890 \\
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "app.example.com",
                "Type": "A",
                "SetIdentifier": "eu-traffic",
                "Weight": 70,
                "TTL": 300,
                "ResourceRecords": [{"Value": "1.2.3.4"}]
            }
        }, {
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "app.example.com",
                "Type": "A",
                "SetIdentifier": "us-traffic",
                "Weight": 30,
                "TTL": 300,
                "ResourceRecords": [{"Value": "5.6.7.8"}]
            }
        }]
    }'
# Weighted routing
# 70% trafik till EU, 30% till US
# Bra för gradual rollouts
# Weight 0 stänger av endpoint
```

---

## Key Takeaways

1. **Hosted Zones för domäner** - en zone per domän
2. **Alias för AWS-resurser** - gratis och snabbt
3. **Health checks för failover** - automatisk failover vid problem
4. **Weighted routing** - gradual deployments
5. **TTL påverkar propagering** - lägre TTL = snabbare ändringar
""",
        },
        {
            "title": "CloudFront - CDN och Edge",
            "slug": "cloudfront-cdn-edge",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# CloudFront - CDN och Edge

## Varför behöver du kunna detta?

CloudFront är AWS Content Delivery Network (CDN). Som DevOps behöver du kunna:

- **Distribuera statiskt innehåll** globalt med låg latens
- **Konfigurera origins** för S3, ALB eller custom endpoints
- **Hantera cache** för optimal prestanda
- **Sätta upp HTTPS** med SSL/TLS-certifikat

---

## Så fungerar CloudFront

CloudFront cachar innehåll på edge locations runt världen. När en användare efterfrågar innehåll:
1. Request går till närmaste edge location
2. Om cachat - returneras direkt (cache hit)
3. Om inte cachat - hämtas från origin, cachas, returneras

Fördelar: lägre latens, minskad load på origin, DDoS-skydd.

---

## Skapa en CloudFront Distribution

```bash
aws cloudfront create-distribution \\
    --distribution-config '{
        "CallerReference": "my-dist-'$(date +%s)'",
        "Origins": {
            "Quantity": 1,
            "Items": [{
                "Id": "S3Origin",
                "DomainName": "my-bucket.s3.eu-north-1.amazonaws.com",
                "S3OriginConfig": {
                    "OriginAccessIdentity": ""
                }
            }]
        },
        "DefaultCacheBehavior": {
            "TargetOriginId": "S3Origin",
            "ViewerProtocolPolicy": "redirect-to-https",
            "AllowedMethods": {
                "Quantity": 2,
                "Items": ["GET", "HEAD"]
            },
            "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
            "Compress": true
        },
        "Enabled": true,
        "Comment": "My static website CDN"
    }'
# Skapar CloudFront distribution
# CallerReference måste vara unik
# Origins definierar backend-källor
# DefaultCacheBehavior för alla requests
# CachePolicyId är AWS managed policy
# 658327ea... = CachingOptimized
# Returnerar Distribution och DomainName

aws cloudfront list-distributions
# Listar alla distributions
# Visar Id, DomainName (d123.cloudfront.net)
# Status: Deployed eller InProgress
# Origins visar var content hämtas
```

---

## Origins och Origin Access Control

```bash
aws cloudfront create-origin-access-control \\
    --origin-access-control-config '{
        "Name": "my-oac",
        "SigningProtocol": "sigv4",
        "SigningBehavior": "always",
        "OriginAccessControlOriginType": "s3"
    }'
# Skapar Origin Access Control (OAC)
# Ersätter äldre Origin Access Identity (OAI)
# Signerar requests till S3
# S3 kan blockera direktåtkomst
# Returnerar OAC Id

aws s3api put-bucket-policy \\
    --bucket my-bucket \\
    --policy '{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1234567890"
                }
            }
        }]
    }'
# Bucket policy för CloudFront
# Tillåter endast CloudFront att läsa
# SourceArn begränsar till specifik distribution
# Blockerar direkta S3-anrop
# Best practice för säkerhet
```

---

## Cache Behaviors och Invalidering

```bash
aws cloudfront get-distribution-config \\
    --id E1234567890 \\
    --query '{ETag: ETag, CacheBehaviors: DistributionConfig.CacheBehaviors}'
# Hämtar cache behaviors
# Olika caching per path pattern
# /api/* kan ha annan policy än /static/*
# ETag behövs för uppdateringar

aws cloudfront create-invalidation \\
    --distribution-id E1234567890 \\
    --paths '/images/*' '/index.html'
# Invaliderar cachad content
# Tvingar refresh från origin
# Första 1000/månad gratis
# /*' invaliderar allt (dyrt)

aws cloudfront list-invalidations \\
    --distribution-id E1234567890
# Listar invalideringar
# Status: InProgress eller Completed
# CreateTime visar när
# Invalidering tar 1-15 minuter

aws cloudfront get-invalidation \\
    --distribution-id E1234567890 \\
    --id ABCD1234
# Detaljer om specifik invalidering
# InvalidationBatch visar paths
# Status när den är klar
# Använd för att vänta på completion
```

---

## HTTPS och Custom Domains

```bash
aws acm request-certificate \\
    --domain-name example.com \\
    --subject-alternative-names "*.example.com" \\
    --validation-method DNS \\
    --region us-east-1
# Begär SSL-certifikat i ACM
# VIKTIGT: CloudFront kräver us-east-1
# subject-alternative-names för wildcard
# DNS-validering enklast
# Email-validering också möjlig

aws acm describe-certificate \\
    --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/abc123 \\
    --region us-east-1
# Visar certifikatstatus
# Status: PENDING_VALIDATION, ISSUED
# DomainValidationOptions innehåller DNS records
# Lägg till CNAME i Route 53

aws cloudfront update-distribution \\
    --id E1234567890 \\
    --distribution-config '{
        ...
        "Aliases": {
            "Quantity": 2,
            "Items": ["example.com", "www.example.com"]
        },
        "ViewerCertificate": {
            "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/abc123",
            "SSLSupportMethod": "sni-only",
            "MinimumProtocolVersion": "TLSv1.2_2021"
        }
    }'
# Lägger till custom domain och cert
# Aliases är dina domäner
# sni-only är standard (gratis)
# MinimumProtocolVersion för säkerhet
# dedicated-ip kostar $600/månad
```

---

## Key Takeaways

1. **Edge caching** - innehåll nära användarna
2. **OAC för S3** - blockera direktåtkomst till bucket
3. **Invalidering kostar** - planera deploys för att minimera
4. **ACM i us-east-1** - krav för CloudFront certifikat
5. **Cache behaviors** - olika policies för olika paths
""",
        },
        {
            "title": "SNS och SQS - Meddelandetjänster",
            "slug": "sns-sqs-meddelandetjanster",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# SNS och SQS - Meddelandetjänster

## Varför behöver du kunna detta?

SNS (Simple Notification Service) och SQS (Simple Queue Service) är AWS meddelandetjänster. Som DevOps behöver du kunna:

- **Implementera pub/sub** med SNS för notifieringar
- **Bygga köbaserade system** med SQS för async processing
- **Kombinera SNS + SQS** för fan-out arkitektur
- **Hantera dead-letter queues** för felhantering

---

## Så fungerar SNS och SQS

**SNS (Pub/Sub):**
- Publisher skickar meddelande till topic
- Alla subscribers får meddelandet
- Push-modell (SNS pushar till mottagare)

**SQS (Queue):**
- Producer skickar meddelande till kö
- Consumer pollar och processar ett meddelande
- Pull-modell (consumer hämtar)

Vanligt mönster: SNS → SQS (fan-out till flera köer)

---

## SNS Topics och Subscriptions

```bash
aws sns create-topic \\
    --name order-events
# Skapar SNS topic
# Returnerar TopicArn
# Arn format: arn:aws:sns:region:account:topic-name
# Topics är regionala

aws sns list-topics
# Listar alla topics
# Visar TopicArn för varje
# Använd för att hitta befintliga topics
# Paginering om många topics

aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --protocol email \\
    --notification-endpoint user@example.com
# Skapar email-subscription
# protocol: email, sqs, lambda, http, sms
# Email kräver bekräftelse
# Returnerar SubscriptionArn (pending confirmation)

aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --protocol sqs \\
    --notification-endpoint arn:aws:sqs:eu-north-1:123456789012:order-processing
# SQS subscription
# Meddelanden pushas till kön
# Kräver SQS policy som tillåter SNS
# Perfekt för fan-out

aws sns publish \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --message '{"orderId": "123", "status": "created"}' \\
    --message-attributes '{"eventType": {"DataType": "String", "StringValue": "OrderCreated"}}'
# Publicerar meddelande
# message är payload
# message-attributes för metadata/filtrering
# Alla subscribers får meddelandet
```

---

## SQS Köer

```bash
aws sqs create-queue \\
    --queue-name order-processing \\
    --attributes '{
        "VisibilityTimeout": "30",
        "MessageRetentionPeriod": "345600",
        "ReceiveMessageWaitTimeSeconds": "20"
    }'
# Skapar Standard SQS kö
# VisibilityTimeout: hur länge meddelande är osynligt under processing
# MessageRetentionPeriod: 4 dagar (345600 sek)
# ReceiveMessageWaitTimeSeconds: long polling (20 sek)
# Returnerar QueueUrl

aws sqs create-queue \\
    --queue-name order-processing.fifo \\
    --attributes '{
        "FifoQueue": "true",
        "ContentBasedDeduplication": "true"
    }'
# FIFO-kö för ordnad leverans
# Namn måste sluta med .fifo
# ContentBasedDeduplication undviker dubbletter
# Lägre throughput än standard

aws sqs get-queue-attributes \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible
# Visar kö-statistik
# ApproximateNumberOfMessages: väntande meddelanden
# MessagesNotVisible: under processing
# Bra för monitoring
```

---

## Skicka och ta emot meddelanden

```bash
aws sqs send-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --message-body '{"orderId": "123", "items": ["item1", "item2"]}'
# Skickar meddelande till kö
# message-body är payload
# Returnerar MessageId och MD5
# Max 256 KB per meddelande

aws sqs receive-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --max-number-of-messages 10 \\
    --wait-time-seconds 20
# Tar emot meddelanden
# max-number-of-messages: 1-10
# wait-time-seconds: long polling
# Returnerar Messages array
# Varje message har ReceiptHandle

aws sqs delete-message \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --receipt-handle "AQEBwJnKyr..."
# Raderar meddelande efter processing
# ReceiptHandle från receive-message
# VIKTIGT: radera efter lyckad processing
# Annars blir meddelandet synligt igen
```

---

## Dead Letter Queues och SNS Filter

```bash
aws sqs create-queue \\
    --queue-name order-processing-dlq
# Skapar Dead Letter Queue
# Hit går meddelanden som misslyckats
# Separat kö för analys/retry
# Samma region som huvudkön

aws sqs set-queue-attributes \\
    --queue-url https://sqs.eu-north-1.amazonaws.com/123456789012/order-processing \\
    --attributes '{
        "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:eu-north-1:123456789012:order-processing-dlq\",\"maxReceiveCount\":\"3\"}"
    }'
# Kopplar DLQ till huvudkö
# maxReceiveCount: antal försök innan DLQ
# RedrivePolicy är JSON-sträng i JSON
# Escape noga

aws sns subscribe \\
    --topic-arn arn:aws:sns:eu-north-1:123456789012:order-events \\
    --protocol sqs \\
    --notification-endpoint arn:aws:sqs:eu-north-1:123456789012:priority-orders \\
    --attributes '{"FilterPolicy": "{\"priority\": [\"high\"]}"}'
# SNS filter policy
# Endast meddelanden med priority=high
# Baserat på message-attributes
# Minskar onödig processing
# FilterPolicy är JSON-sträng
```

---

## Key Takeaways

1. **SNS för pub/sub** - ett meddelande till många mottagare
2. **SQS för köer** - en consumer per meddelande
3. **Long polling** - effektivare än short polling
4. **DLQ för felhantering** - fånga misslyckade meddelanden
5. **SNS + SQS fan-out** - vanligt mönster för decoupling
""",
        },
        {
            "title": "DynamoDB - NoSQL Database",
            "slug": "dynamodb-nosql-database",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# DynamoDB - NoSQL Database

## Varför behöver du kunna detta?

DynamoDB är AWS managed NoSQL-databas. Som DevOps behöver du kunna:

- **Skapa och konfigurera tabeller** med rätt nyckeldesign
- **Hantera kapacitet** med on-demand eller provisioned mode
- **Sätta upp Global Tables** för multi-region
- **Konfigurera backups** och point-in-time recovery

---

## Så fungerar DynamoDB

DynamoDB är en key-value och document database med:
- **Partition Key (PK)** - obligatoriskt, bestämmer partition
- **Sort Key (SK)** - valfritt, för sortering inom partition
- **Single-digit millisecond latency** - konsistent snabbhet
- **Automatisk skalning** - hanterar last automatiskt

Data organiseras i tabeller → items → attributes.

---

## Skapa tabeller

```bash
aws dynamodb create-table \\
    --table-name Users \\
    --attribute-definitions \\
        AttributeName=userId,AttributeType=S \\
    --key-schema \\
        AttributeName=userId,KeyType=HASH \\
    --billing-mode PAY_PER_REQUEST
# Skapar tabell med partition key
# AttributeType: S (string), N (number), B (binary)
# KeyType HASH = partition key
# PAY_PER_REQUEST = on-demand pricing
# Betala per request, ingen kapacitetsplanering

aws dynamodb create-table \\
    --table-name Orders \\
    --attribute-definitions \\
        AttributeName=customerId,AttributeType=S \\
        AttributeName=orderId,AttributeType=S \\
    --key-schema \\
        AttributeName=customerId,KeyType=HASH \\
        AttributeName=orderId,KeyType=RANGE \\
    --billing-mode PAY_PER_REQUEST
# Tabell med composite key (PK + SK)
# customerId är partition key (HASH)
# orderId är sort key (RANGE)
# Alla orders för en kund i samma partition
# Effektivt för query på customerId

aws dynamodb describe-table \\
    --table-name Orders
# Visar tabell-info
# TableStatus: CREATING, ACTIVE, DELETING
# ItemCount, TableSizeBytes
# KeySchema och AttributeDefinitions
```

---

## CRUD-operationer

```bash
aws dynamodb put-item \\
    --table-name Users \\
    --item '{
        "userId": {"S": "user123"},
        "name": {"S": "Anna Andersson"},
        "email": {"S": "anna@example.com"},
        "createdAt": {"S": "2024-01-15T10:30:00Z"}
    }'
# Skapar eller ersätter item
# Alla värden har typ-annotation (S, N, etc.)
# userId är primary key
# Övriga attribut är fria (schemaless)
# Returnerar inget vid success

aws dynamodb get-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}'
# Hämtar item med primary key
# Returnerar Item med alla attribut
# Null om item inte finns
# Extremt snabbt (single-digit ms)

aws dynamodb update-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}' \\
    --update-expression "SET #n = :name, updatedAt = :now" \\
    --expression-attribute-names '{"#n": "name"}' \\
    --expression-attribute-values '{":name": {"S": "Anna Svensson"}, ":now": {"S": "2024-01-16T14:00:00Z"}}'
# Uppdaterar specifika attribut
# update-expression med SET, REMOVE, ADD, DELETE
# #n är placeholder för reserverade ord (name)
# :name är värde-placeholder
# Atomic operation

aws dynamodb delete-item \\
    --table-name Users \\
    --key '{"userId": {"S": "user123"}}'
# Raderar item
# Kräver primary key
# Idempotent - ok att köra flera gånger
# Returnerar inget
```

---

## Query och Scan

```bash
aws dynamodb query \\
    --table-name Orders \\
    --key-condition-expression "customerId = :cid" \\
    --expression-attribute-values '{":cid": {"S": "customer456"}}'
# Query använder index
# Hämtar alla orders för en kund
# Mycket effektivt
# Kräver partition key i condition
# Returnerar Items array

aws dynamodb query \\
    --table-name Orders \\
    --key-condition-expression "customerId = :cid AND orderId BETWEEN :start AND :end" \\
    --expression-attribute-values '{
        ":cid": {"S": "customer456"},
        ":start": {"S": "2024-01"},
        ":end": {"S": "2024-12"}
    }'
# Query med sort key condition
# BETWEEN, begins_with, =, <, >, etc.
# Filtrerar inom partition
# Fortfarande effektivt

aws dynamodb scan \\
    --table-name Users \\
    --filter-expression "contains(email, :domain)" \\
    --expression-attribute-values '{":domain": {"S": "@example.com"}}'
# Scan läser HELA tabellen
# filter-expression filtrerar efteråt
# DYRT för stora tabeller
# Undvik i produktion
# Använd query + index istället
```

---

## Backups och Global Tables

```bash
aws dynamodb update-continuous-backups \\
    --table-name Orders \\
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
# Aktiverar Point-in-Time Recovery
# Backup senaste 35 dagarna
# Restore till vilken sekund som helst
# Extra kostnad men värt det

aws dynamodb create-backup \\
    --table-name Orders \\
    --backup-name orders-backup-2024-01
# Skapar on-demand backup
# Bevaras tills du raderar
# Bra för major changes
# Restore skapar ny tabell

aws dynamodb update-table \\
    --table-name Orders \\
    --replica-updates '[{"Create": {"RegionName": "us-east-1"}}]'
# Skapar Global Table replica
# Multi-region active-active
# Automatisk replikering
# Konflikthantering: last-writer-wins
# Kräver on-demand eller samma provisioned capacity

aws dynamodb describe-table \\
    --table-name Orders \\
    --query 'Table.Replicas'
# Visar alla replicas
# RegionName och ReplicaStatus
# ACTIVE när synkroniserad
# Global Tables för DR och latens
```

---

## Key Takeaways

1. **Partition key design** - kritiskt för prestanda
2. **On-demand för variabel last** - ingen kapacitetsplanering
3. **Query över Scan** - använd index, undvik full scan
4. **Point-in-Time Recovery** - aktivera för alla prod-tabeller
5. **Global Tables** - multi-region för DR och låg latens
""",
        },
        {
            "title": "Secrets Manager - Hemlighetshantering",
            "slug": "secrets-manager-hemlighetshantering",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Secrets Manager - Hemlighetshantering

## Varför behöver du kunna detta?

Secrets Manager är AWS tjänst för säker lagring av hemligheter. Som DevOps behöver du kunna:

- **Lagra och hämta secrets** säkert (API-nycklar, lösenord)
- **Konfigurera automatisk rotation** för databaspassord
- **Integrera med applikationer** via SDK eller CLI
- **Hantera åtkomst** med IAM policies

---

## Så fungerar Secrets Manager

Secrets Manager:
- Krypterar secrets med AWS KMS
- Hanterar versionering automatiskt
- Kan rotera secrets automatiskt
- Integrerar med RDS för databaspassword

Skillnad mot Parameter Store:
- Secrets Manager har inbyggd rotation
- Parameter Store är billigare för enkel lagring
- Secrets Manager optimerat för hemligheter

---

## Skapa och hantera secrets

```bash
aws secretsmanager create-secret \\
    --name prod/myapp/db-credentials \\
    --description "Production database credentials" \\
    --secret-string '{"username": "admin", "password": "SuperSecret123!"}'
# Skapar en ny secret
# Namn följer hierarki (prod/app/secret)
# secret-string för key-value JSON
# Krypteras automatiskt med default KMS key
# Returnerar ARN och VersionId

aws secretsmanager create-secret \\
    --name prod/myapp/api-key \\
    --secret-string "sk-abc123def456"
# Enkel string istället för JSON
# Bra för enkla API-nycklar
# Samma kryptering och versionering
# Hämtas som plain string

aws secretsmanager list-secrets \\
    --filters Key=name,Values=prod/
# Listar secrets
# Filtrerar på namn-prefix
# Visar ARN, Name, LastChangedDate
# SecretVersionsToStages visar versioner

aws secretsmanager describe-secret \\
    --secret-id prod/myapp/db-credentials
# Detaljer om secret
# RotationEnabled, RotationLambdaARN
# VersionIdsToStages (AWSCURRENT, AWSPREVIOUS)
# Visar INTE secret value
```

---

## Hämta secrets

```bash
aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials
# Hämtar secret värde
# SecretString innehåller värdet
# AWSCURRENT version by default
# Använd i scripts: $(aws secretsmanager get-secret-value --secret-id x --query SecretString --output text)

aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --version-stage AWSPREVIOUS
# Hämtar föregående version
# Bra vid rotation-problem
# AWSCURRENT, AWSPREVIOUS, AWSPENDING
# version-id för specifik version

aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --query 'SecretString' \\
    --output text | jq -r '.password'
# Extraherar specifikt värde
# --query hämtar bara SecretString
# jq parsar JSON
# Perfekt för shell scripts
```

---

## Uppdatera och rotera

```bash
aws secretsmanager update-secret \\
    --secret-id prod/myapp/db-credentials \\
    --secret-string '{"username": "admin", "password": "NewPassword456!"}'
# Uppdaterar secret
# Skapar ny version automatiskt
# Förra versionen blir AWSPREVIOUS
# Inga avbrott - applikationer hämtar ny

aws secretsmanager put-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --secret-string '{"username": "admin", "password": "AnotherPass789!"}' \\
    --version-stages AWSCURRENT
# Alternativ för att sätta värde
# Explicit version-stages
# Kan användas för custom rotation
# put-secret-value vs update-secret

aws secretsmanager rotate-secret \\
    --secret-id prod/myapp/db-credentials
# Triggar rotation manuellt
# Kräver rotation Lambda konfigurerad
# Skapar ny version med AWSPENDING
# Lambda flyttar till AWSCURRENT

aws secretsmanager rotate-secret \\
    --secret-id prod/myapp/db-credentials \\
    --rotation-lambda-arn arn:aws:lambda:eu-north-1:123456789012:function:db-rotator \\
    --rotation-rules AutomaticallyAfterDays=30
# Konfigurerar automatisk rotation
# Lambda roterar var 30:e dag
# AWS har färdiga Lambda templates
# RDS rotation är enklast
```

---

## Cross-account och CLI-användning

```bash
aws secretsmanager get-resource-policy \\
    --secret-id prod/myapp/db-credentials
# Visar resource policy
# Styr cross-account access
# Null om ingen policy finns
# Använd put-resource-policy för att sätta

aws secretsmanager put-resource-policy \\
    --secret-id prod/myapp/db-credentials \\
    --resource-policy '{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::987654321098:root"},
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "*"
        }]
    }'
# Tillåter annat konto läsa secret
# Principal är det andra kontot
# Behöver också IAM policy i det kontot
# Resource: * = denna secret

export DB_PASSWORD=$(aws secretsmanager get-secret-value \\
    --secret-id prod/myapp/db-credentials \\
    --query 'SecretString' \\
    --output text | jq -r '.password')
# Sätter miljövariabel från secret
# Användbart i deployment scripts
# Undvik att logga värdet
# set +x innan echo

aws secretsmanager delete-secret \\
    --secret-id prod/myapp/old-credentials \\
    --recovery-window-in-days 7
# Raderar secret
# 7-30 dagars recovery window
# --force-delete-without-recovery för omedelbar
# Soft delete - kan återställas under window
```

---

## Key Takeaways

1. **Hierarkiska namn** - prod/app/secret för organisation
2. **Automatisk kryptering** - KMS-krypterat by default
3. **Versionering inbyggd** - AWSCURRENT, AWSPREVIOUS
4. **Rotation för databaser** - använd AWS Lambda templates
5. **Resource policies** - cross-account access
""",
        },
        {
            "title": "Systems Manager - Operationell Hantering",
            "slug": "systems-manager-operationell-hantering",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Systems Manager - Operationell Hantering

## Varför behöver du kunna detta?

Systems Manager (SSM) är AWS svit för operationell hantering. Som DevOps behöver du kunna:

- **Köra kommandon på EC2** utan SSH via Run Command
- **Hantera parametrar** med Parameter Store
- **Automatisera med dokument** och Automation
- **Säkra åtkomst** med Session Manager

---

## Så fungerar Systems Manager

Systems Manager kräver SSM Agent på EC2 (förinstallerad på Amazon Linux). Komponenter:
- **Run Command** - kör kommandon på instanser
- **Parameter Store** - konfigurations- och hemlighetshantering
- **Session Manager** - säker shell-åtkomst utan SSH
- **Automation** - runbooks för komplexa operationer

---

## Parameter Store

```bash
aws ssm put-parameter \\
    --name /myapp/prod/db-host \\
    --value "db.example.com" \\
    --type String
# Skapar parameter
# Hierarkiskt namn (/app/env/param)
# Type: String, StringList, SecureString
# String för klartext config

aws ssm put-parameter \\
    --name /myapp/prod/db-password \\
    --value "SuperSecret123!" \\
    --type SecureString
# SecureString för hemligheter
# Krypteras med KMS (default key)
# Gratis för standard tier
# Advanced tier för >10KB

aws ssm get-parameter \\
    --name /myapp/prod/db-host
# Hämtar parameter
# Value, Type, Version, ARN
# LastModifiedDate
# Perfekt för config

aws ssm get-parameter \\
    --name /myapp/prod/db-password \\
    --with-decryption
# Hämtar och dekrypterar
# --with-decryption krävs för SecureString
# Utan flaggan får du krypterat värde
# IAM behöver kms:Decrypt permission

aws ssm get-parameters-by-path \\
    --path /myapp/prod/ \\
    --recursive \\
    --with-decryption
# Hämtar alla under path
# --recursive inkluderar subpaths
# Bra för att ladda all config
# Returnerar Parameters array
```

---

## Run Command

```bash
aws ssm send-command \\
    --document-name AWS-RunShellScript \\
    --targets Key=tag:Environment,Values=production \\
    --parameters 'commands=["yum update -y"]'
# Kör kommando på instanser
# AWS-RunShellScript för Linux
# targets väljer instanser via taggar
# Returnerar CommandId

aws ssm send-command \\
    --document-name AWS-RunShellScript \\
    --instance-ids i-abc123 i-def456 \\
    --parameters 'commands=["systemctl restart nginx", "systemctl status nginx"]'
# Specifika instanser
# Flera kommandon i array
# Kör i ordning
# Bra för deployment/restart

aws ssm list-command-invocations \\
    --command-id abc123-def456 \\
    --details
# Visar resultat per instans
# Status: Pending, InProgress, Success, Failed
# StandardOutputContent med output
# --details för full output

aws ssm get-command-invocation \\
    --command-id abc123-def456 \\
    --instance-id i-abc123
# Detaljerat resultat för en instans
# StandardOutputContent
# StandardErrorContent
# ResponseCode
```

---

## Session Manager

```bash
aws ssm start-session \\
    --target i-abc123
# Startar interaktiv session
# Som SSH men utan SSH keys/ports
# All trafik via SSM endpoint
# Session loggas i CloudWatch/S3

aws ssm start-session \\
    --target i-abc123 \\
    --document-name AWS-StartPortForwardingSession \\
    --parameters '{"portNumber":["3306"],"localPortNumber":["3306"]}'
# Port forwarding
# Åtkomst till RDS via bastion
# Ingen publik IP behövs
# Säkrare än SSH tunnels

aws ssm describe-sessions \\
    --state Active
# Listar aktiva sessioner
# SessionId, Target, Owner
# StartDate, Status
# Bra för audit

aws ssm terminate-session \\
    --session-id session-abc123
# Avslutar session
# Använd för att tvinga disconnect
# Administratörer kan avsluta andras
# Session timeout default 20 min
```

---

## Automation och Documents

```bash
aws ssm list-documents \\
    --filters Key=DocumentType,Values=Automation \\
    --query 'DocumentIdentifiers[*].Name'
# Listar automation documents
# AWS-prefixade är AWS managed
# Skapa egna för custom workflows
# DocumentType: Command, Automation, etc.

aws ssm start-automation-execution \\
    --document-name AWS-RestartEC2Instance \\
    --parameters '{"InstanceId":["i-abc123"]}'
# Kör automation
# AWS-RestartEC2Instance stoppar och startar
# Multi-step med error handling
# Returnerar AutomationExecutionId

aws ssm describe-automation-executions \\
    --filters Key=ExecutionStatus,Values=InProgress
# Visar körningar
# AutomationExecutionStatus
# StepExecutions för varje steg
# Outputs med resultat

aws ssm get-automation-execution \\
    --automation-execution-id abc123
# Detaljer om körning
# Alla steg och status
# Outputs och errors
# Duration och timing
```

---

## Key Takeaways

1. **Parameter Store** - hierarkisk config, gratis standard tier
2. **SecureString för hemligheter** - KMS-krypterat
3. **Run Command** - kommandon utan SSH
4. **Session Manager** - säker shell utan ports/keys
5. **Automation** - multi-step runbooks
""",
        },
        {
            "title": "Cost Management - Kostnadsoptimering",
            "slug": "cost-management-kostnadsoptimering",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Cost Management - Kostnadsoptimering

## Varför behöver du kunna detta?

Kostnadshantering är kritiskt i AWS. Som DevOps behöver du kunna:

- **Övervaka kostnader** med Cost Explorer och budgets
- **Analysera användning** för att hitta besparingar
- **Implementera tagging** för kostnadsallokering
- **Sätta upp alerts** för oväntade kostnader

---

## Så fungerar AWS Cost Management

AWS tillhandahåller flera verktyg:
- **Cost Explorer** - visualisering och analys
- **Budgets** - budgetar och alerts
- **Cost and Usage Reports** - detaljerad data
- **Savings Plans/Reserved Instances** - rabatter

Kostnader kommer med ~24h fördröjning.

---

## Cost Explorer via CLI

```bash
aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics UnblendedCost
# Hämtar total kostnad
# UnblendedCost är faktisk kostnad
# BlendedCost för konsoliderad billing
# Granularity: DAILY, MONTHLY, HOURLY

aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity DAILY \\
    --metrics UnblendedCost \\
    --group-by Type=DIMENSION,Key=SERVICE
# Grupperat per tjänst
# Visar var pengarna går
# SERVICE, REGION, USAGE_TYPE
# Perfekt för kostnadsfördelning

aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics UnblendedCost \\
    --filter '{
        "Dimensions": {
            "Key": "SERVICE",
            "Values": ["Amazon EC2"]
        }
    }'
# Filtrerar på tjänst
# Endast EC2-kostnader
# Kombinera filter för precision
# And, Or, Not för komplexa filter

aws ce get-cost-forecast \\
    --time-period Start=2024-02-01,End=2024-02-28 \\
    --metric UNBLENDED_COST \\
    --granularity MONTHLY
# Prognostiserar framtida kostnad
# Baserat på historik
# 80% confidence interval
# Bra för budgetplanering
```

---

## AWS Budgets

```bash
aws budgets create-budget \\
    --account-id 123456789012 \\
    --budget '{
        "BudgetName": "monthly-budget",
        "BudgetType": "COST",
        "BudgetLimit": {
            "Amount": "1000",
            "Unit": "USD"
        },
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
# Skapar månadsbudget på $1000
# Alert vid 80% förbrukning
# Email till alerts@example.com
# ACTUAL för faktisk, FORECASTED för prognos

aws budgets describe-budgets \\
    --account-id 123456789012
# Listar alla budgets
# BudgetName, BudgetLimit
# CalculatedSpend vs BudgetLimit
# Visar om du är on track

aws budgets create-budget \\
    --account-id 123456789012 \\
    --budget '{
        "BudgetName": "ec2-budget",
        "BudgetType": "COST",
        "BudgetLimit": {"Amount": "500", "Unit": "USD"},
        "TimeUnit": "MONTHLY",
        "CostFilters": {
            "Service": ["Amazon Elastic Compute Cloud - Compute"]
        }
    }'
# Budget för specifik tjänst
# CostFilters begränsar scope
# Bra för per-team budgets
# Service-namn från Cost Explorer
```

---

## Tagging för kostnadsallokering

```bash
aws ec2 create-tags \\
    --resources i-abc123 \\
    --tags Key=CostCenter,Value=engineering Key=Environment,Value=production
# Taggar resurser för kostnadsallokering
# CostCenter för avdelning
# Environment för miljö
# Project för projekt

aws organizations enable-aws-service-access \\
    --service-principal cost-allocation-tags.amazonaws.com
# Aktiverar cost allocation tags
# Kräver Organizations
# Gör taggar synliga i Cost Explorer
# Kan ta 24h att aktivera

aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity MONTHLY \\
    --metrics UnblendedCost \\
    --group-by Type=TAG,Key=CostCenter
# Grupperar kostnad per CostCenter tag
# Visar fördelning per avdelning
# Untagged resurser i separat grupp
# Aktivera tags i Billing först

aws resourcegroupstaggingapi get-resources \\
    --tag-filters Key=CostCenter,Values=engineering \\
    --resource-type-filters ec2:instance
# Hitta resurser utan/med specifik tag
# Audit för tagging compliance
# Alla regioner och tjänster
# resource-type-filters begränsar scope
```

---

## Savings Plans och Reserved Instances

```bash
aws ce get-savings-plans-utilization \\
    --time-period Start=2024-01-01,End=2024-01-31
# Visar Savings Plans användning
# UtilizationPercentage bör vara >80%
# TotalCommitment vs UsedCommitment
# Optimera om låg utilization

aws ce get-reservation-utilization \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --group-by Type=DIMENSION,Key=SERVICE
# Reserved Instances utilization
# Per tjänst (EC2, RDS, etc.)
# UnusedHours visar waste
# Köp mer om hög on-demand usage

aws ce get-savings-plans-purchase-recommendation \\
    --savings-plans-type COMPUTE_SP \\
    --term-in-years ONE_YEAR \\
    --payment-option NO_UPFRONT \\
    --lookback-period-in-days SIXTY_DAYS
# Rekommendation för Savings Plans
# Baserat på 60 dagars historik
# EstimatedMonthlySavingsAmount
# Compute SP flexiblast

aws ce get-rightsizing-recommendation \\
    --service AmazonEC2 \\
    --configuration '{
        "BenefitsConsidered": true,
        "RecommendationTarget": "SAME_INSTANCE_FAMILY"
    }'
# Right-sizing rekommendationer
# Undersized och oversized instanser
# EstimatedMonthlySavings
# BenefitsConsidered inkluderar RI/SP
```

---

## Key Takeaways

1. **Budgets med alerts** - första försvaret mot överraskningar
2. **Tagging obligatoriskt** - kan inte allokera utan taggar
3. **Cost Explorer dagligen** - fånga anomalier tidigt
4. **Savings Plans för rabatt** - 30-70% besparing på commit
5. **Right-sizing** - betala inte för outnyttjad kapacitet
""",
        },
        {
            "title": "AWS Best Practices och Well-Architected",
            "slug": "aws-best-practices-well-architected",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# AWS Best Practices och Well-Architected

## Varför behöver du kunna detta?

Well-Architected Framework är AWS best practices för molnarkitektur. Som DevOps behöver du kunna:

- **Tillämpa de sex pelarna** för robusta system
- **Göra Well-Architected Reviews** för att hitta förbättringar
- **Implementera DevOps-principer** i AWS
- **Designa för failure** med resilient arkitektur

---

## De Sex Pelarna

Well-Architected Framework har sex pelare:

1. **Operational Excellence** - automatisera, dokumentera, lär av failure
2. **Security** - identitet, åtkomst, data-skydd
3. **Reliability** - återhämtning, skalning, change management
4. **Performance Efficiency** - rätt resurser, övervakning
5. **Cost Optimization** - kostnadskontroll, rätt storlek
6. **Sustainability** - miljöpåverkan, effektiv användning

---

## Well-Architected Tool

```bash
aws wellarchitected create-workload \\
    --workload-name "MyApplication" \\
    --description "Production web application" \\
    --environment PRODUCTION \\
    --lenses wellarchitected \\
    --aws-regions eu-north-1 \\
    --review-owner "devops-team"
# Skapar workload för review
# PRODUCTION eller PREPRODUCTION
# wellarchitected är standard lens
# Kan lägga till serverless, SaaS lenses
# Returnerar WorkloadId

aws wellarchitected list-workloads
# Listar alla workloads
# WorkloadName, RiskCounts
# HIGH_RISK, MEDIUM_RISK counts
# Använd för översikt

aws wellarchitected get-answer \\
    --workload-id abc123 \\
    --lens-alias wellarchitected \\
    --pillar-id operationalExcellence \\
    --question-id ops-1
# Hämtar specifik fråga och svar
# Choices med bästa praxis
# SelectedChoices markerar ditt svar
# Notes för kommentarer

aws wellarchitected update-answer \\
    --workload-id abc123 \\
    --lens-alias wellarchitected \\
    --pillar-id operationalExcellence \\
    --question-id ops-1 \\
    --selected-choices choice1 choice3 \\
    --notes "Implemented CloudWatch dashboards and automated runbooks"
# Uppdaterar svar
# Välj applicerbara best practices
# Notes dokumenterar implementation
# Risk uppdateras automatiskt
```

---

## Operational Excellence Patterns

```bash
cat << 'EOF' > cloudwatch-dashboard.json
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/ECS", "CPUUtilization", "ServiceName", "my-service"],
          [".", "MemoryUtilization", ".", "."]
        ],
        "title": "ECS Service Health",
        "period": 60,
        "stat": "Average"
      }
    },
    {
      "type": "log",
      "properties": {
        "query": "fields @timestamp, @message | filter @message like /ERROR/ | limit 20",
        "logGroupName": "/ecs/my-service",
        "title": "Recent Errors"
      }
    }
  ]
}
EOF
aws cloudwatch put-dashboard \\
    --dashboard-name MyAppOverview \\
    --dashboard-body file://cloudwatch-dashboard.json
# Operational dashboard
# Samlad vy av metrics och loggar
# Snabb problemidentifiering
# Dela med teamet

aws events put-rule \\
    --name deployment-notifications \\
    --event-pattern '{
        "source": ["aws.codedeploy"],
        "detail-type": ["CodeDeploy Deployment State-change Notification"],
        "detail": {"state": ["FAILURE"]}
    }'
# EventBridge regel för deployment failures
# Notifiera teamet vid problem
# Lär av failures
# Koppla till SNS eller Lambda
```

---

## Security Best Practices

```bash
aws iam get-account-summary
# IAM översikt
# Users, Groups, Roles counts
# MFADevices aktiverade
# AccountMFAEnabled bör vara 1

aws iam generate-credential-report
aws iam get-credential-report --output text --query Content | base64 -d
# Credential report
# Visar alla användare
# password_enabled, mfa_active
# access_key_last_used
# Audit regelbundet

aws securityhub enable-security-hub
aws securityhub get-findings \\
    --filters '{"SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}]}'
# Security Hub för överblick
# Samlar findings från GuardDuty, Inspector, etc.
# CRITICAL findings kräver omedelbar action
# Integrera i incident response

aws guardduty create-detector \\
    --enable
# GuardDuty för threat detection
# Analyserar VPC Flow, CloudTrail, DNS
# Hittar suspicious activity
# Minimal performance impact
```

---

## Reliability Patterns

```bash
aws autoscaling describe-auto-scaling-groups \\
    --query 'AutoScalingGroups[*].[AutoScalingGroupName,MinSize,MaxSize,DesiredCapacity]'
# Auto Scaling konfiguration
# MinSize >= 2 för HA
# Multi-AZ för redundans
# HealthCheckType: ELB för webb

aws rds describe-db-instances \\
    --query 'DBInstances[*].[DBInstanceIdentifier,MultiAZ,BackupRetentionPeriod]'
# RDS high availability
# MultiAZ: true för failover
# BackupRetentionPeriod > 0
# EnablePerformanceInsights för monitoring

aws s3api get-bucket-versioning --bucket my-bucket
aws s3api get-bucket-replication --bucket my-bucket
# S3 data protection
# Versioning för accidental delete
# Replication för DR
# Lifecycle policies för kostnad

aws elasticloadbalancing describe-target-health \\
    --target-group-arn arn:aws:elasticloadbalancing:eu-north-1:123456789012:targetgroup/my-tg/abc123
# Health check status
# Healthy targets per AZ
# Draining targets vid deployment
# Unhealthy kräver investigation
```

---

## Performance och Sustainability

```bash
aws compute-optimizer get-ec2-instance-recommendations
# Rightsizing recommendations
# Over-provisioned = kostnad + miljö
# Under-provisioned = performance
# VERY_LOW/LOW/MEDIUM/HIGH risk

aws trustedadvisor describe-check-result \\
    --check-id Qch7DwouX1 \\
    --language en
# Trusted Advisor checks
# Cost optimization, performance
# Security, fault tolerance
# Requires Business/Enterprise Support

aws ce get-cost-and-usage \\
    --time-period Start=2024-01-01,End=2024-01-31 \\
    --granularity DAILY \\
    --metrics UsageQuantity \\
    --group-by Type=DIMENSION,Key=USAGE_TYPE \\
    --filter '{"Dimensions": {"Key": "SERVICE", "Values": ["Amazon EC2"]}}'
# Usage patterns
# Identifiera peak times
# Rightsizing potential
# Sustainability: mindre användning = mindre impact
```

---

## Key Takeaways

1. **Well-Architected Reviews** - regelbundet, inte bara vid launch
2. **Automatisera allt** - minska manuella fel och tid
3. **Security by default** - GuardDuty, Security Hub, MFA
4. **Design for failure** - Multi-AZ, Auto Scaling, backups
5. **Mät och optimera** - metrics driver beslut
""",
        },
    ],
}

