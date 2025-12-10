# ============================================================================
# AZURE BLOCK 2 - NODE 5: VIRTUAL MACHINES (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_5_V2 = {
    "node_id": 5,
    "title": "Azure Virtual Machines",
    "slug": "azure-virtual-machines",
    "description": "Skapa och hantera Azure VMs som ett proffs",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Fullständig kontroll i molnet",
        "hook": "VMs ger dig total frihet - men med stor makt kommer stort ansvar (och potentiella kostnader).",
        "learning_objectives": [
            "Välja rätt VM-storlek för din workload",
            "Skapa VMs med Azure CLI",
            "Hantera diskar och storage",
            "Implementera high availability med Availability Zones",
            "Automatisera med VM Scale Sets"
        ],
        "prerequisites": [
            "Azure CLI konfigurerat",
            "Förståelse för Resource Groups",
            "Grundläggande Linux/Windows-kunskap"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "vm-sizes",
            "title": "VM Size Families",
            "explanation": """Azure har olika VM-familjer optimerade för olika workloads.

**B-series (Burstable)**
- Dev/test, låg trafik
- Billigast, sparar credits vid låg användning
- Ex: Standard_B2s (2 vCPU, 4GB RAM) ~$30/mån

**D-series (General Purpose)**
- Balanserad CPU/RAM ratio
- Web servers, applikationer
- Ex: Standard_D4s_v5 (4 vCPU, 16GB RAM) ~$140/mån

**E-series (Memory Optimized)**
- Hög RAM/CPU ratio
- Databaser, caching, analytics
- Ex: Standard_E4s_v5 (4 vCPU, 32GB RAM) ~$180/mån

**F-series (Compute Optimized)**
- Hög CPU/RAM ratio
- Batch processing, gaming
- Ex: Standard_F4s_v2 (4 vCPU, 8GB RAM) ~$120/mån

**N-series (GPU)**
- Machine learning, rendering
- Ex: Standard_NC6 (6 vCPU + K80 GPU) ~$650/mån""",
            "diagram": """
+-------------------------------------------------+
|              VM SIZE NAMING                      |
+-------------------------------------------------+
|                                                 |
|   Standard_D4as_v5                              |
|   |       ||||  |                               |
|   |       ||||  +-- Version (v5 = latest)       |
|   |       |||+-- a = AMD processor              |
|   |       ||+-- s = Premium SSD support         |
|   |       |+-- 4 = vCPU count                   |
|   |       +-- D = Family (General Purpose)      |
|   +-- Tier (Standard vs Basic)                  |
|                                                 |
|   SUFFIXES:                                     |
|   s = Premium SSD    a = AMD CPU                |
|   r = RDMA support   d = Local temp disk        |
|   i = Isolated       l = Low memory             |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Börja med B-series för dev/test och uppgradera till D-series för produktion. Du sparar 70%+ på dev.",
            "common_mistake": "Att välja för stor VM 'för säkerhets skull'. Börja litet och skala upp vid behov - du betalar per minut."
        },
        {
            "id": "vm-creation",
            "title": "Skapa VMs med CLI",
            "explanation": """Azure CLI är bästa sättet att skapa VMs reproducerbart.

**Minimal Linux VM:**
```bash
az vm create \\
    --resource-group rg-demo \\
    --name vm-web-01 \\
    --image Ubuntu2204 \\
    --size Standard_B2s \\
    --admin-username azureuser \\
    --generate-ssh-keys
```

**Produktion-ready VM:**
```bash
az vm create \\
    --resource-group rg-prod \\
    --name vm-app-01 \\
    --image Ubuntu2204 \\
    --size Standard_D4s_v5 \\
    --zone 1 \\
    --os-disk-size-gb 128 \\
    --storage-sku Premium_LRS \\
    --admin-username azureuser \\
    --ssh-key-values ~/.ssh/id_rsa.pub \\
    --public-ip-address "" \\
    --nsg ""
```

**Windows VM:**
```bash
az vm create \\
    --resource-group rg-demo \\
    --name vm-win-01 \\
    --image Win2022Datacenter \\
    --size Standard_D2s_v5 \\
    --admin-username azureadmin \\
    --admin-password "SecureP@ss123!"
```""",
            "diagram": """
+-------------------------------------------------+
|              VM CREATION FLOW                    |
+-------------------------------------------------+
|                                                 |
|   az vm create                                  |
|         |                                       |
|         ▼                                       |
|   +-----------------------------------------+   |
|   |  CREATES AUTOMATICALLY:                 |   |
|   |  • Virtual Machine                      |   |
|   |  • OS Disk (managed)                    |   |
|   |  • Network Interface (NIC)              |   |
|   |  • Virtual Network (if not exists)      |   |
|   |  • Subnet (if not exists)               |   |
|   |  • Public IP (optional)                 |   |
|   |  • Network Security Group (NSG)         |   |
|   +-----------------------------------------+   |
|                                                 |
|   ⚠️  OBS: Alla dessa resurser kostar!         |
|   💡 Radera RG för att ta bort allt på en gång |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd --public-ip-address '' för produktion. Sätt istället VMs bakom Load Balancer eller Bastion.",
            "common_mistake": "Att glömma --generate-ssh-keys och sedan inte kunna logga in. Keys sparas i ~/.ssh/"
        },
        {
            "id": "disks-storage",
            "title": "Diskar & Storage",
            "explanation": """Azure VMs har olika disktyper med olika prestanda och pris.

**Disktyper:**
| Typ | IOPS | Throughput | Pris | Användning |
|-----|------|------------|------|------------|
| Standard HDD | 500 | 60 MB/s | $ | Archive, backup |
| Standard SSD | 6000 | 750 MB/s | $$ | Dev/test, web |
| Premium SSD | 20000 | 900 MB/s | $$$ | Production, DB |
| Ultra Disk | 160000 | 4000 MB/s | $$$$ | SAP HANA, top-tier |

**OS Disk vs Data Disk:**
- **OS Disk**: Bootdisk, max 4TB, skall vara snabb
- **Data Disk**: Applikationsdata, upp till 32TB
- **Temp Disk**: Försvinner vid deallocate! Bara för temp data.

**Managed Disks (alltid):**
- Azure hanterar storage account automatiskt
- Enklare backup och restore
- Garanterad 99.9% SLA""",
            "diagram": """
+-------------------------------------------------+
|              VM DISK ARCHITECTURE               |
+-------------------------------------------------+
|                                                 |
|   +-----------------------------------------+   |
|   |              VIRTUAL MACHINE            |   |
|   |                                         |   |
|   |   /dev/sda (OS Disk)                   |   |
|   |   +-- Premium SSD                       |   |
|   |   +-- 128GB, P10 tier                  |   |
|   |                                         |   |
|   |   /dev/sdb (Temp Disk) ⚠️               |   |
|   |   +-- Local SSD (FREE!)                |   |
|   |   +-- DATA LOST on deallocate!         |   |
|   |                                         |   |
|   |   /dev/sdc (Data Disk)                 |   |
|   |   +-- Premium SSD                       |   |
|   |   +-- 256GB, P15 tier                  |   |
|   +-----------------------------------------+   |
|                                                 |
|   💡 Temp disk = pagefile/swap only!           |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Premium SSD (P10+) för OS disk. Skillnaden är ~$10/mån men boot time går från 60s till 15s.",
            "common_mistake": "Att spara data på temp disk (/dev/sdb). Den raderas vid deallocate och VM-flytt!"
        },
        {
            "id": "availability",
            "title": "High Availability",
            "explanation": """Azure erbjuder flera sätt att uppnå high availability.

**Availability Zones (99.99% SLA):**
- Fysiskt separerade datacenter i samma region
- Skyddar mot datacenter-failure
- Spread VMs across zones 1, 2, 3

**Availability Sets (99.95% SLA):**
- Logisk gruppering inom ett datacenter
- Fault Domains (rack-level failure)
- Update Domains (Azure maintenance)

**VM Scale Sets (VMSS):**
- Auto-scaling baserat på metrics
- Identiska VMs bakom load balancer
- Automatic healing

**Välja rätt:**
| Scenario | Val |
|----------|-----|
| Single VM, non-critical | Ingen (99.9% SLA) |
| Multi-VM, same datacenter | Availability Set |
| Multi-VM, datacenter failure | Availability Zones |
| Auto-scaling | VM Scale Sets |""",
            "diagram": """
+-------------------------------------------------+
|           AVAILABILITY ZONES                     |
+-------------------------------------------------+
|                                                 |
|   REGION: North Europe                          |
|   +---------+ +---------+ +---------+          |
|   | ZONE 1  | | ZONE 2  | | ZONE 3  |          |
|   |         | |         | |         |          |
|   |  [VM-1] | |  [VM-2] | |  [VM-3] |          |
|   |  [DB-1] | |  [DB-2] | |  [DB-3] |          |
|   |         | |         | |         |          |
|   +----+----+ +----+----+ +----+----+          |
|        |           |           |                |
|        +-----------+-----------+                |
|                    |                            |
|            +-------+-------+                    |
|            | LOAD BALANCER |                    |
|            |  (Zone-redundant)|                 |
|            +---------------+                    |
|                                                 |
|   ✅ If Zone 1 fails -> Zone 2 & 3 take over    |
|   ✅ 99.99% SLA                                 |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "För kritiska applikationer: minst 2 VMs i olika Availability Zones + Zone-redundant Load Balancer.",
            "common_mistake": "Att sätta alla VMs i samma zone 'för enkelhet'. En zone-failure tar ner hela tjänsten."
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du skapa en produktions-ready VM-miljö med high availability.",
        "exercises": [
            {
                "step": 1,
                "title": "Lista tillgängliga VM-storlekar",
                "instruction": "Se vilka VM-storlekar som finns i North Europe.",
                "hint": "Använd 'az vm list-sizes' med --location",
                "expected_command": "az vm list-sizes --location northeurope --query \"[?contains(name, 'Standard_B')].{Name:name, vCPUs:numberOfCores, RAM:memoryInMb}\" --output table",
                "expected_output": """Name              vCPUs    RAM
----------------  -------  ------
Standard_B1ls     1        512
Standard_B1s      1        1024
Standard_B2s      2        4096
Standard_B2ms     2        8192
Standard_B4ms     4        16384""",
                "explanation": "B-series är burstable VMs perfekta för dev/test. De ackumulerar CPU-credits vid låg användning.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Skapa Linux VM i Zone 1",
                "instruction": "Skapa en Ubuntu VM i Availability Zone 1.",
                "hint": "Använd --zone 1 flaggan",
                "expected_command": "az vm create --resource-group rg-demo --name vm-web-01 --image Ubuntu2204 --size Standard_B2s --zone 1 --admin-username azureuser --generate-ssh-keys --output json",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.Compute/virtualMachines/vm-web-01",
  "location": "northeurope",
  "powerState": "VM running",
  "publicIpAddress": "20.xx.xx.xx",
  "zones": "1"
}""",
                "explanation": "Zone 1 är ett specifikt datacenter i regionen. För HA, skapa fler VMs i zone 2 och 3.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Skapa VM i Zone 2",
                "instruction": "Skapa en till VM i Zone 2 för redundans.",
                "hint": "Samma kommando, ändra namn och zone",
                "expected_command": "az vm create --resource-group rg-demo --name vm-web-02 --image Ubuntu2204 --size Standard_B2s --zone 2 --admin-username azureuser --generate-ssh-keys",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.Compute/virtualMachines/vm-web-02",
  "location": "northeurope",
  "powerState": "VM running",
  "publicIpAddress": "20.yy.yy.yy",
  "zones": "2"
}""",
                "explanation": "Nu har du VMs i två zoner. Om zone 1 går ner, finns fortfarande zone 2.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Lägg till Data Disk",
                "instruction": "Koppla en 128GB Premium SSD till vm-web-01.",
                "hint": "Använd 'az vm disk attach' med --new och --sku",
                "expected_command": "az vm disk attach --resource-group rg-demo --vm-name vm-web-01 --name datadisk-01 --size-gb 128 --sku Premium_LRS --new",
                "expected_output": """(Disk attached successfully)""",
                "explanation": "Premium_LRS = Premium SSD med lokalt redundant lagring. Bäst för produktions-workloads.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Visa VM Status",
                "instruction": "Visa detaljerad status för båda VMs.",
                "hint": "Använd 'az vm list' med query för resource group",
                "expected_command": "az vm list --resource-group rg-demo --query \"[].{Name:name, Size:hardwareProfile.vmSize, Zone:zones[0]}\" --output table",
                "expected_output": """Name        Size           Zone
----------  -------------  ------
vm-web-01   Standard_B2s   1
vm-web-02   Standard_B2s   2""",
                "explanation": "Båda VMs körs i olika zoner = zone-redundant setup.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "SSH till VM",
                "instruction": "Anslut till vm-web-01 via SSH.",
                "hint": "Använd 'az vm ssh' eller standard ssh med IP",
                "expected_command": "az ssh vm --resource-group rg-demo --name vm-web-01",
                "expected_output": """Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-1054-azure x86_64)

azureuser@vm-web-01:~$""",
                "explanation": "'az ssh vm' hanterar nyckel-autentisering automatiskt. Alternativt: ssh azureuser@<public-ip>",
                "xp": 5
            }
        ],
        "xp": 30
    },

    # ========================================================================
    # QUIZ SECTION
    # ========================================================================
    "quiz": {
        "passing_score": 80,
        "flashcards": [
            {
                "id": "fc1",
                "front": "Vilken VM-serie är bäst för dev/test med variabel CPU-användning?",
                "back": "B-series (Burstable) - ackumulerar CPU-credits vid låg användning"
            },
            {
                "id": "fc2",
                "front": "Vad händer med data på Temp Disk vid VM deallocate?",
                "back": "DATA RADERAS! Temp disk är endast för temporär data som pagefile/swap."
            },
            {
                "id": "fc3",
                "front": "Vad är SLA för VMs i Availability Zones vs single VM?",
                "back": "Availability Zones: 99.99% SLA. Single VM med Premium SSD: 99.9% SLA."
            },
            {
                "id": "fc4",
                "front": "Vad betyder 's' i VM-namn som Standard_D4s_v5?",
                "back": "s = Premium SSD support (kan använda Premium_LRS diskar)"
            },
            {
                "id": "fc5",
                "front": "Skillnad mellan 'az vm stop' och 'az vm deallocate'?",
                "back": "stop: VM stannar, betalar fortfarande compute. deallocate: Inga compute-kostnader."
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du behöver en VM för en SQL Server databas med hög minnesanvändning. Vilken serie väljer du?",
                "options": [
                    "B-series (Burstable)",
                    "D-series (General Purpose)",
                    "E-series (Memory Optimized)",
                    "F-series (Compute Optimized)"
                ],
                "correct_answer": 2,
                "explanation": "E-series är memory-optimized med hög RAM/CPU ratio. Perfekt för databaser och caching."
            },
            {
                "id": "mc2",
                "question": "Du vill att din web app ska överleva ett helt datacenter som går ner. Vad behöver du?",
                "options": [
                    "Availability Set",
                    "Availability Zones",
                    "Single VM med Premium SSD",
                    "VM Scale Set i samma zone"
                ],
                "correct_answer": 1,
                "explanation": "Availability Zones sprider VMs över fysiskt separerade datacenter. Skyddar mot datacenter-failure."
            },
            {
                "id": "mc3",
                "question": "Vilken disktyp ska INTE användas för produktionsdatabaser?",
                "options": [
                    "Premium SSD",
                    "Ultra Disk",
                    "Standard SSD",
                    "Standard HDD"
                ],
                "correct_answer": 3,
                "explanation": "Standard HDD har 500 IOPS max - alldeles för långsamt för databaser. Minst Premium SSD för produktion."
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Bygg Produktions-Ready VM Infrastructure",
        "scenario": """Du ska sätta upp infrastruktur för en ny webapplikation:
- 2 web servers (Linux, nginx)
- 1 database server (Linux, PostgreSQL)
- High availability kravet: överleva zone failure
- Budget: minimera kostnader för dev/test""",
        "requirements": [
            "Skapa Resource Group för projektet",
            "Deploya 2 web VMs i olika Availability Zones",
            "Deploya 1 database VM med Premium SSD",
            "Konfigurera auto-shutdown på dev-miljön",
            "Tagga alla resurser med environment, owner, project",
            "Bonus: Skriv deployment script som kan köras om"
        ],
        "hints": [
            "Web servers: B2s i zone 1 och 2",
            "Database: D4s_v5 med Premium SSD data disk",
            "Auto-shutdown: 1700 UTC = 18:00 CET"
        ],
        "solution": """#!/bin/bash
# Production-Ready VM Infrastructure Deployment
# Usage: ./deploy-infrastructure.sh <environment>

set -e

ENVIRONMENT=${1:-dev}
LOCATION="northeurope"
PROJECT="webapp-v1"
RG_NAME="rg-${PROJECT}-${ENVIRONMENT}"

echo "🚀 Deploying $PROJECT to $ENVIRONMENT environment..."

# ═══════════════════════════════════════════════════════════════
# Create Resource Group
# ═══════════════════════════════════════════════════════════════
echo "📦 Creating Resource Group..."
az group create \\
    --name $RG_NAME \\
    --location $LOCATION \\
    --tags environment=$ENVIRONMENT owner=team-platform project=$PROJECT

# ═══════════════════════════════════════════════════════════════
# Create Virtual Network
# ═══════════════════════════════════════════════════════════════
echo "🌐 Creating Virtual Network..."
az network vnet create \\
    --resource-group $RG_NAME \\
    --name vnet-$PROJECT \\
    --address-prefix 10.0.0.0/16 \\
    --subnet-name subnet-web \\
    --subnet-prefix 10.0.1.0/24

az network vnet subnet create \\
    --resource-group $RG_NAME \\
    --vnet-name vnet-$PROJECT \\
    --name subnet-db \\
    --address-prefix 10.0.2.0/24

# ═══════════════════════════════════════════════════════════════
# Create Web Servers (Zone-redundant)
# ═══════════════════════════════════════════════════════════════
echo "🖥️  Creating Web Servers..."

# Size based on environment
if [ "$ENVIRONMENT" == "prod" ]; then
    VM_SIZE="Standard_D2s_v5"
else
    VM_SIZE="Standard_B2s"
fi

for ZONE in 1 2; do
    VM_NAME="vm-web-0${ZONE}"
    echo "   Creating $VM_NAME in zone $ZONE..."

    az vm create \\
        --resource-group $RG_NAME \\
        --name $VM_NAME \\
        --image Ubuntu2204 \\
        --size $VM_SIZE \\
        --zone $ZONE \\
        --vnet-name vnet-$PROJECT \\
        --subnet subnet-web \\
        --admin-username azureuser \\
        --generate-ssh-keys \\
        --public-ip-address "" \\
        --tags environment=$ENVIRONMENT owner=team-platform project=$PROJECT role=web \\
        --no-wait
done

# ═══════════════════════════════════════════════════════════════
# Create Database Server
# ═══════════════════════════════════════════════════════════════
echo "🗄️  Creating Database Server..."

DB_SIZE="Standard_D4s_v5"
if [ "$ENVIRONMENT" != "prod" ]; then
    DB_SIZE="Standard_B2ms"
fi

az vm create \\
    --resource-group $RG_NAME \\
    --name vm-db-01 \\
    --image Ubuntu2204 \\
    --size $DB_SIZE \\
    --zone 1 \\
    --vnet-name vnet-$PROJECT \\
    --subnet subnet-db \\
    --admin-username azureuser \\
    --generate-ssh-keys \\
    --public-ip-address "" \\
    --os-disk-size-gb 64 \\
    --storage-sku Premium_LRS \\
    --tags environment=$ENVIRONMENT owner=team-platform project=$PROJECT role=database

# Add data disk for database
echo "   Adding data disk..."
az vm disk attach \\
    --resource-group $RG_NAME \\
    --vm-name vm-db-01 \\
    --name ${PROJECT}-db-data \\
    --size-gb 256 \\
    --sku Premium_LRS \\
    --new

# ═══════════════════════════════════════════════════════════════
# Configure Auto-Shutdown (non-prod only)
# ═══════════════════════════════════════════════════════════════
if [ "$ENVIRONMENT" != "prod" ]; then
    echo "⏰ Configuring auto-shutdown..."

    for VM in $(az vm list -g $RG_NAME --query "[].name" -o tsv); do
        az vm auto-shutdown \\
            --resource-group $RG_NAME \\
            --name $VM \\
            --time 1700
    done
fi

# ═══════════════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════════════
echo ""
echo "✅ Deployment Complete!"
echo ""
echo "Resources created in $RG_NAME:"
az vm list -g $RG_NAME --query "[].{Name:name, Size:hardwareProfile.vmSize, Zone:zones[0]}" -o table

echo ""
echo "💰 Estimated monthly cost:"
if [ "$ENVIRONMENT" == "prod" ]; then
    echo "   Web servers: 2x D2s_v5 = ~$140"
    echo "   DB server:   1x D4s_v5 = ~$140"
    echo "   Storage:     ~$50"
    echo "   TOTAL:       ~$330/month"
else
    echo "   Web servers: 2x B2s = ~$60"
    echo "   DB server:   1x B2ms = ~$60"
    echo "   Storage:     ~$30"
    echo "   Auto-shutdown savings: -70%"
    echo "   TOTAL:       ~$50/month (with auto-shutdown)"
fi

echo ""
echo "Next steps:"
echo "1. Configure NSG rules for web/db traffic"
echo "2. Install nginx on web servers"
echo "3. Install PostgreSQL on db server"
echo "4. Set up Azure Bastion for secure access"
""",
        "xp": 20
    },

    # ========================================================================
    # METADATA
    # ========================================================================
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 10,
        "practice": 12,
        "quiz": 6,
        "challenge": 15
    },
    "xp_per_section": {
        "intro": 10,
        "concepts": 15,
        "practice": 30,
        "quiz": 25,
        "challenge": 20
    },
    "total_xp": 110,
    "topics_covered": [
        "virtual machines",
        "vm sizes",
        "availability zones",
        "managed disks",
        "premium ssd",
        "high availability",
        "azure cli",
        "infrastructure deployment"
    ]
}
