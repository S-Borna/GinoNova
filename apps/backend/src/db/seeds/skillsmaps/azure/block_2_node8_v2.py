# ============================================================================
# AZURE BLOCK 2 - NODE 8: VIRTUAL NETWORKS (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_8_V2 = {
    "node_id": 8,
    "title": "Azure Virtual Networks",
    "slug": "azure-virtual-networks",
    "description": "Nätverksinfrastruktur i Azure - VNets, Subnets, NSGs",
    "difficulty": "intermediate",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Bygg säkra nätverkslösningar",
        "hook": "Virtual Networks är ryggraden i din Azure-infrastruktur. Utan VNet-förståelse bygger du på sand.",
        "learning_objectives": [
            "Designa VNet-arkitektur med subnets",
            "Konfigurera Network Security Groups (NSGs) för trafikfiltrering",
            "Implementera VNet Peering för multi-VNet kommunikation",
            "Sätta upp Azure Bastion för säker VM-access",
            "Förstå service endpoints och private endpoints"
        ],
        "prerequisites": [
            "Grundläggande nätverkskoncept (IP, subnets, TCP/UDP)",
            "Azure CLI konfigurerat",
            "VMs-kunskap (föregående node)"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "vnet-basics",
            "title": "VNet & Subnet Grunderna",
            "explanation": """Virtual Network (VNet) är ditt privata nätverk i Azure.

**VNet-egenskaper:**
- Isolerat adressutrymme (CIDR-block)
- Region-specifikt (t.ex. North Europe)
- Kan innehålla flera subnets
- Kommunikation inom VNet är öppen by default

**Subnet-design:**
| Subnet | CIDR | Användning |
|--------|------|------------|
| subnet-web | /24 (256 IP) | Web servers |
| subnet-app | /24 | Application tier |
| subnet-db | /25 (128 IP) | Databases |
| subnet-mgmt | /26 (64 IP) | Jump boxes, Bastion |
| AzureBastionSubnet | /26+ | Azure Bastion (reserved name!) |

**CIDR-planering:**
- /16 = 65,536 IPs (företagsövergripande)
- /24 = 256 IPs (per applikation)
- /26 = 64 IPs (small subnets)

**Azure reserverar 5 IPs per subnet:**
- .0 = Network address
- .1 = Gateway
- .2, .3 = Azure DNS
- .255 = Broadcast

Så /24 (256) = 251 användbara IPs.""",
            "diagram": """
+-------------------------------------------------+
|         VNET ARCHITECTURE EXAMPLE               |
+-------------------------------------------------+
|                                                 |
|   VNet: vnet-prod (10.0.0.0/16)                |
|   +-----------------------------------------+   |
|   |                                         |   |
|   |   subnet-web (10.0.1.0/24)              |   |
|   |   +---------------------------------+   |   |
|   |   |  [VM-Web-1]    [VM-Web-2]      |   |   |
|   |   |  10.0.1.4      10.0.1.5        |   |   |
|   |   +---------------------------------+   |   |
|   |                                         |   |
|   |   subnet-app (10.0.2.0/24)              |   |
|   |   +---------------------------------+   |   |
|   |   |  [VM-App-1]    [VM-App-2]      |   |   |
|   |   |  10.0.2.4      10.0.2.5        |   |   |
|   |   +---------------------------------+   |   |
|   |                                         |   |
|   |   subnet-db (10.0.3.0/25)               |   |
|   |   +---------------------------------+   |   |
|   |   |  [SQL-Primary] [SQL-Secondary] |   |   |
|   |   |  10.0.3.4      10.0.3.5        |   |   |
|   |   +---------------------------------+   |   |
|   |                                         |   |
|   +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Planera stort! Det är svårt att ändra VNet CIDR efteråt. Börja med /16 även för små miljöer.",
            "common_mistake": "Att använda överlappande CIDR-ranges mellan VNets. Gör VNet Peering omöjligt."
        },
        {
            "id": "nsg",
            "title": "Network Security Groups",
            "explanation": """NSGs är brandväggar för Azure nätverk.

**NSG-koncept:**
- Stateful brandvägg (return traffic auto-allowed)
- Kan kopplas till subnet eller NIC
- Processar regler i prioritetsordning (lägst först)
- Default: deny all inbound, allow all outbound

**Regel-komponenter:**
| Fält | Beskrivning | Exempel |
|------|-------------|---------|
| Priority | 100-4096 (lägre = högre prio) | 100 |
| Source | IP, CIDR, tag | 10.0.1.0/24 |
| Destination | IP, CIDR, tag | * |
| Port | Port eller range | 443, 22, 8080-8090 |
| Protocol | TCP, UDP, * | TCP |
| Action | Allow/Deny | Allow |

**Service Tags (inbyggda):**
- `Internet` - Allt utanför Azure
- `VirtualNetwork` - Ditt VNet + peerade VNets
- `AzureLoadBalancer` - Azure LB health probes
- `Storage` - Azure Storage IPs
- `Sql` - Azure SQL Database IPs

**Application Security Groups (ASG):**
Gruppera VMs logiskt istället för IP-ranges:
```
Source: asg-web-servers
Destination: asg-app-servers
-> Alla web-servrar kan nå alla app-servrar
```""",
            "diagram": """
+-------------------------------------------------+
|         NSG RULE PROCESSING                      |
+-------------------------------------------------+
|                                                 |
|   INBOUND TRAFFIC FLOW:                         |
|                                                 |
|   [Internet] --▶ NSG Rules (Priority order)     |
|                     |                           |
|   +-----------------▼---------------------+     |
|   | 100: Allow SSH from 1.2.3.4     ✅    |     |
|   | 200: Allow HTTPS from Internet  ✅    |     |
|   | 300: Allow HTTP from Internet   ✅    |     |
|   | 400: Deny SQL from Internet     ❌    |     |
|   | 65000: Allow VNet (default)           |     |
|   | 65001: Allow LB (default)             |     |
|   | 65500: Deny All (default)       ❌    |     |
|   +---------------------------------------+     |
|                                                 |
|   ⚡ First match wins!                          |
|   💡 Lower priority number = processed first    |
|                                                 |
|   SUBNET vs NIC:                                |
|   +----------+    +----------+                 |
|   | Subnet   |    | NIC NSG  |    +-----+      |
|   | NSG      |--▶| (optional)|--▶| VM  |      |
|   +----------+    +----------+    +-----+      |
|   Traffic must pass BOTH if both exist!        |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Service Tags istället för hårdkodade IPs. 'Storage.NorthEurope' är bättre än en lista av IPs.",
            "common_mistake": "Att koppla NSG till både subnet OCH NIC utan att förstå att traffic måste passera BÅDA."
        },
        {
            "id": "vnet-peering",
            "title": "VNet Peering",
            "explanation": """VNet Peering kopplar ihop separata VNets.

**Typer av peering:**
- **Regional Peering**: Samma Azure-region
- **Global Peering**: Olika regioner (lite latency)

**Egenskaper:**
- ✅ Låg latency (Azure backbone)
- ✅ Ingen gateway behövs
- ✅ Traffic stays private (aldrig internet)
- ⚠️ Icke-transitiv (A->B->C ≠ A->C)
- ⚠️ CIDR får inte överlappa

**Icke-transitiv förklarat:**
```
VNet-A peered med VNet-B
VNet-B peered med VNet-C
-> VNet-A kan INTE nå VNet-C automatiskt!
-> Du måste peera A->C separat
```

**Hub-and-Spoke topology:**
```
      +--------+
      | Hub    | (shared services)
      | VNet   |
      +----+---+
    +------+------+
    ▼      ▼      ▼
+------++------++------+
|Spoke1||Spoke2||Spoke3|
|(App1)||(App2)||(App3)|
+------++------++------+
```
Hub innehåller: Firewall, VPN Gateway, DNS
Spokes: Applikations-VNets""",
            "diagram": """
+-------------------------------------------------+
|           VNET PEERING TOPOLOGY                 |
+-------------------------------------------------+
|                                                 |
|   HUB-AND-SPOKE (Recommended)                   |
|                                                 |
|              +-----------------+                |
|              |    HUB VNET     |                |
|              |  (10.0.0.0/16)  |                |
|              |                 |                |
|              |  [Firewall]     |                |
|              |  [VPN Gateway]  |                |
|              |  [DNS Server]   |                |
|              +--------+--------+                |
|          +-----------+-----------+              |
|          |     Peering|         |              |
|          ▼            ▼          ▼              |
|   +-----------++-----------++-----------+      |
|   | SPOKE 1   || SPOKE 2   || SPOKE 3   |      |
|   |10.1.0.0/16||10.2.0.0/16||10.3.0.0/16|      |
|   |           ||           ||           |      |
|   | [App A]   || [App B]   || [App C]   |      |
|   +-----------++-----------++-----------+      |
|                                                 |
|   ⚠️  Spokes cannot talk directly!             |
|   -> Traffic via Hub (or add spoke-spoke peer)  |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Hub-and-Spoke med Azure Firewall i Hub ger central säkerhetskontroll och loggning.",
            "common_mistake": "Att anta att peering är transitiv. VNet A peered med B, B peered med C, betyder INTE att A kan nå C."
        },
        {
            "id": "bastion",
            "title": "Azure Bastion",
            "explanation": """Azure Bastion ger säker SSH/RDP utan public IPs.

**Problem det löser:**
- VMs med public IP = attack surface
- RDP/SSH-portar öppna till internet
- VPN krävs för att nå privata VMs

**Azure Bastion:**
- Browser-baserad SSH/RDP
- VMs behöver bara private IP
- Ingen lokal klient behövs
- AAD-authentication stöds
- Session recording möjligt

**Hur det fungerar:**
```
Du -> Azure Portal -> Bastion -> Private VM
     (HTTPS:443)    (Private IP)
```
Bastion gör 'jump host' automatiskt.

**Krav:**
- Subnet måste heta exakt `AzureBastionSubnet`
- Minst /26 CIDR
- Bastion SKU: Basic (~$140/mån) eller Standard

**Alternativ utan Bastion:**
- Jump box VM med public IP + NSG
- VPN Gateway (Point-to-Site eller Site-to-Site)
- Azure VPN Client""",
            "diagram": """
+-------------------------------------------------+
|           AZURE BASTION ARCHITECTURE            |
+-------------------------------------------------+
|                                                 |
|   WITHOUT BASTION (risky):                      |
|   +--------+      +---------------------+       |
|   |Internet|------| VM with Public IP   |       |
|   |        | RDP  | (port 3389 open!)   |       |
|   +--------+      +---------------------+       |
|       ❌ Attack surface, brute force risk       |
|                                                 |
|   WITH BASTION (secure):                        |
|   +--------+      +--------------------------+  |
|   |Browser |      | VNet                     |  |
|   |(you)   |      |                          |  |
|   +---+----+      |  AzureBastionSubnet      |  |
|       | HTTPS     |  +-----------------+     |  |
|       | :443      |  | Azure Bastion   |     |  |
|       +----------▶|  +--------+--------+     |  |
|                   |           | Private IP    |  |
|                   |  subnet-vms              |  |
|                   |  +-----------------+     |  |
|                   |  | VM (no public IP)|     |  |
|                   |  | 10.0.1.4        |     |  |
|                   |  +-----------------+     |  |
|                   +--------------------------+  |
|       ✅ No public IP needed on VMs            |
|       ✅ No RDP/SSH ports to internet          |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Azure Bastion Standard SKU har IP-based connect - du kan nå VMs via IP utan att gå via Portal.",
            "common_mistake": "Att döpa subnet till något annat än 'AzureBastionSubnet'. Det MÅSTE heta exakt så."
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du bygga en komplett nätverksinfrastruktur med VNet, subnets, NSGs och Bastion.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa Virtual Network",
                "instruction": "Skapa ett VNet med 10.0.0.0/16 adressutrymme.",
                "hint": "Använd 'az network vnet create'",
                "expected_command": "az network vnet create --name vnet-prod --resource-group rg-demo --location northeurope --address-prefixes 10.0.0.0/16",
                "expected_output": """{
  "newVNet": {
    "addressSpace": {
      "addressPrefixes": ["10.0.0.0/16"]
    },
    "location": "northeurope",
    "name": "vnet-prod"
  }
}""",
                "explanation": "/16 ger dig 65,536 IPs - gott om utrymme för framtida expansion.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Skapa Subnets",
                "instruction": "Skapa web-subnet (10.0.1.0/24) och db-subnet (10.0.2.0/24).",
                "hint": "Använd 'az network vnet subnet create' två gånger",
                "expected_command": "az network vnet subnet create --vnet-name vnet-prod --resource-group rg-demo --name subnet-web --address-prefixes 10.0.1.0/24 && az network vnet subnet create --vnet-name vnet-prod --resource-group rg-demo --name subnet-db --address-prefixes 10.0.2.0/24",
                "expected_output": """{
  "addressPrefix": "10.0.1.0/24",
  "name": "subnet-web"
}
{
  "addressPrefix": "10.0.2.0/24",
  "name": "subnet-db"
}""",
                "explanation": "Separata subnets för olika tiers gör det lättare att applicera NSG-regler.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Skapa NSG för Web Tier",
                "instruction": "Skapa en NSG som tillåter HTTP (80) och HTTPS (443) från internet.",
                "hint": "Använd 'az network nsg create' följt av 'az network nsg rule create'",
                "expected_command": "az network nsg create --name nsg-web --resource-group rg-demo && az network nsg rule create --nsg-name nsg-web --resource-group rg-demo --name AllowHTTPS --priority 100 --source-address-prefixes Internet --destination-port-ranges 443 --protocol Tcp --access Allow",
                "expected_output": """{
  "name": "nsg-web"
}
{
  "name": "AllowHTTPS",
  "priority": 100,
  "protocol": "Tcp",
  "sourceAddressPrefix": "Internet",
  "destinationPortRange": "443",
  "access": "Allow"
}""",
                "explanation": "Priority 100 = hög prioritet. Regeln processas före default deny-regeln (65500).",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Skapa NSG för DB Tier",
                "instruction": "Skapa NSG som endast tillåter SQL (1433) från web-subnet.",
                "hint": "Använd source-address-prefixes med CIDR för web-subnet",
                "expected_command": "az network nsg create --name nsg-db --resource-group rg-demo && az network nsg rule create --nsg-name nsg-db --resource-group rg-demo --name AllowSQLFromWeb --priority 100 --source-address-prefixes 10.0.1.0/24 --destination-port-ranges 1433 --protocol Tcp --access Allow",
                "expected_output": """{
  "name": "nsg-db"
}
{
  "name": "AllowSQLFromWeb",
  "priority": 100,
  "sourceAddressPrefix": "10.0.1.0/24",
  "destinationPortRange": "1433",
  "access": "Allow"
}""",
                "explanation": "Bara web-subnet (10.0.1.0/24) kan nå DB på port 1433. Allt annat blockeras.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Koppla NSG till Subnets",
                "instruction": "Associera NSGs med respektive subnet.",
                "hint": "Använd 'az network vnet subnet update' med --network-security-group",
                "expected_command": "az network vnet subnet update --vnet-name vnet-prod --resource-group rg-demo --name subnet-web --network-security-group nsg-web && az network vnet subnet update --vnet-name vnet-prod --resource-group rg-demo --name subnet-db --network-security-group nsg-db",
                "expected_output": """{
  "name": "subnet-web",
  "networkSecurityGroup": {
    "id": "/subscriptions/.../nsg-web"
  }
}
{
  "name": "subnet-db",
  "networkSecurityGroup": {
    "id": "/subscriptions/.../nsg-db"
  }
}""",
                "explanation": "Nu gäller NSG-reglerna för alla resurser i respektive subnet.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Verifiera Konfiguration",
                "instruction": "Lista alla subnets med deras NSG-kopplingar.",
                "hint": "Använd 'az network vnet subnet list' med query",
                "expected_command": "az network vnet subnet list --vnet-name vnet-prod --resource-group rg-demo --query \"[].{Name:name, CIDR:addressPrefix, NSG:networkSecurityGroup.id}\" --output table",
                "expected_output": """Name        CIDR          NSG
----------  ------------  ---------------------------------
subnet-web  10.0.1.0/24   /subscriptions/.../nsg-web
subnet-db   10.0.2.0/24   /subscriptions/.../nsg-db""",
                "explanation": "Bra! Web-subnet har nsg-web, DB-subnet har nsg-db. Trafikflödet är kontrollerat.",
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
                "front": "Hur många IPs reserverar Azure i varje subnet?",
                "back": "5 IPs: .0 (network), .1 (gateway), .2-.3 (DNS), .255 (broadcast). En /24 har 251 användbara."
            },
            {
                "id": "fc2",
                "front": "Vad betyder att VNet Peering är icke-transitiv?",
                "back": "A->B och B->C betyder INTE att A->C. Du måste explicit peera A->C."
            },
            {
                "id": "fc3",
                "front": "Vad måste Azure Bastion-subnet heta?",
                "back": "Exakt 'AzureBastionSubnet' (case sensitive) med minst /26 CIDR."
            },
            {
                "id": "fc4",
                "front": "I vilken ordning processas NSG-regler?",
                "back": "Priority order (lägst nummer först). 100 processas före 200. First match wins."
            },
            {
                "id": "fc5",
                "front": "Vad är en Service Tag i NSG?",
                "back": "Inbyggd IP-grupp som Azure underhåller. T.ex. 'Internet', 'Storage', 'AzureLoadBalancer'."
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du vill att dina VMs ska nås säkert utan public IPs. Vad behöver du?",
                "options": [
                    "VPN Gateway",
                    "Azure Bastion",
                    "Application Gateway",
                    "Traffic Manager"
                ],
                "correct_answer": 1,
                "explanation": "Azure Bastion ger browser-baserad SSH/RDP till VMs med bara private IPs."
            },
            {
                "id": "mc2",
                "question": "Du har VNet-A i North Europe och VNet-B i West Europe. Hur kopplar du ihop dem?",
                "options": [
                    "Regional VNet Peering",
                    "Global VNet Peering",
                    "VPN Gateway",
                    "De kan inte kopplas ihop"
                ],
                "correct_answer": 1,
                "explanation": "Global VNet Peering kopplar VNets i olika regioner. Traffic går via Azure backbone."
            },
            {
                "id": "mc3",
                "question": "NSG har regel: 100 Allow TCP 80, 200 Deny TCP 80. Vad händer med HTTP-trafik?",
                "options": [
                    "Trafiken blockeras",
                    "Trafiken tillåts",
                    "Beror på source IP",
                    "Error - konflikterande regler"
                ],
                "correct_answer": 1,
                "explanation": "First match wins. Priority 100 (Allow) processas före 200 (Deny), så trafiken tillåts."
            }
        ],
        "xp": 30
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Bygg Enterprise Hub-and-Spoke Nätverk",
        "scenario": """Du ska designa nätverket för ett företag med:
- Hub VNet med centrala tjänster (Firewall, Bastion)
- Spoke 1: Production application
- Spoke 2: Development environment
- Spoke 3: Shared services (AD, DNS)

Krav:
- Prod ska INTE kunna nå Dev direkt
- All internet-trafik via centrala firewallen
- Säker access till alla VMs via Bastion""",
        "requirements": [
            "Skapa Hub VNet (10.0.0.0/16) med subnets för Firewall och Bastion",
            "Skapa 3 Spoke VNets med icke-överlappande CIDR",
            "Konfigurera VNet Peering (Hub->Spoke)",
            "Sätt upp Azure Bastion i Hub",
            "Konfigurera NSGs för varje tier",
            "Dokumentera trafikflöden"
        ],
        "hints": [
            "AzureFirewallSubnet behöver /26",
            "AzureBastionSubnet behöver /26",
            "Spokes kan bara nå varandra via Hub",
            "User Defined Routes (UDR) kan tvinga trafik via Firewall"
        ],
        "solution": """#!/bin/bash
# Enterprise Hub-and-Spoke Network Deployment
# ═══════════════════════════════════════════════════════════════

set -e
LOCATION="northeurope"
RG="rg-network-hub-spoke"

echo "🌐 Creating Hub-and-Spoke Network Architecture..."

# Create Resource Group
az group create --name $RG --location $LOCATION

# ═══════════════════════════════════════════════════════════════
# HUB VNET
# ═══════════════════════════════════════════════════════════════
echo "📍 Creating Hub VNet..."

az network vnet create \\
    --name vnet-hub \\
    --resource-group $RG \\
    --location $LOCATION \\
    --address-prefixes 10.0.0.0/16

# Firewall Subnet (required name)
az network vnet subnet create \\
    --vnet-name vnet-hub \\
    --resource-group $RG \\
    --name AzureFirewallSubnet \\
    --address-prefixes 10.0.0.0/26

# Bastion Subnet (required name)
az network vnet subnet create \\
    --vnet-name vnet-hub \\
    --resource-group $RG \\
    --name AzureBastionSubnet \\
    --address-prefixes 10.0.0.64/26

# Management Subnet
az network vnet subnet create \\
    --vnet-name vnet-hub \\
    --resource-group $RG \\
    --name subnet-management \\
    --address-prefixes 10.0.1.0/24

# ═══════════════════════════════════════════════════════════════
# SPOKE VNETS
# ═══════════════════════════════════════════════════════════════

# Spoke 1: Production
echo "📍 Creating Spoke 1 (Production)..."
az network vnet create \\
    --name vnet-spoke-prod \\
    --resource-group $RG \\
    --location $LOCATION \\
    --address-prefixes 10.1.0.0/16

az network vnet subnet create \\
    --vnet-name vnet-spoke-prod \\
    --resource-group $RG \\
    --name subnet-web \\
    --address-prefixes 10.1.1.0/24

az network vnet subnet create \\
    --vnet-name vnet-spoke-prod \\
    --resource-group $RG \\
    --name subnet-app \\
    --address-prefixes 10.1.2.0/24

az network vnet subnet create \\
    --vnet-name vnet-spoke-prod \\
    --resource-group $RG \\
    --name subnet-db \\
    --address-prefixes 10.1.3.0/24

# Spoke 2: Development
echo "📍 Creating Spoke 2 (Development)..."
az network vnet create \\
    --name vnet-spoke-dev \\
    --resource-group $RG \\
    --location $LOCATION \\
    --address-prefixes 10.2.0.0/16

az network vnet subnet create \\
    --vnet-name vnet-spoke-dev \\
    --resource-group $RG \\
    --name subnet-dev \\
    --address-prefixes 10.2.1.0/24

# Spoke 3: Shared Services
echo "📍 Creating Spoke 3 (Shared Services)..."
az network vnet create \\
    --name vnet-spoke-shared \\
    --resource-group $RG \\
    --location $LOCATION \\
    --address-prefixes 10.3.0.0/16

az network vnet subnet create \\
    --vnet-name vnet-spoke-shared \\
    --resource-group $RG \\
    --name subnet-ad \\
    --address-prefixes 10.3.1.0/24

az network vnet subnet create \\
    --vnet-name vnet-spoke-shared \\
    --resource-group $RG \\
    --name subnet-dns \\
    --address-prefixes 10.3.2.0/24

# ═══════════════════════════════════════════════════════════════
# VNET PEERING
# ═══════════════════════════════════════════════════════════════
echo "🔗 Creating VNet Peerings..."

# Hub -> Prod
az network vnet peering create \\
    --name hub-to-prod \\
    --resource-group $RG \\
    --vnet-name vnet-hub \\
    --remote-vnet vnet-spoke-prod \\
    --allow-vnet-access \\
    --allow-forwarded-traffic \\
    --allow-gateway-transit

az network vnet peering create \\
    --name prod-to-hub \\
    --resource-group $RG \\
    --vnet-name vnet-spoke-prod \\
    --remote-vnet vnet-hub \\
    --allow-vnet-access \\
    --allow-forwarded-traffic \\
    --use-remote-gateways false

# Hub -> Dev
az network vnet peering create \\
    --name hub-to-dev \\
    --resource-group $RG \\
    --vnet-name vnet-hub \\
    --remote-vnet vnet-spoke-dev \\
    --allow-vnet-access \\
    --allow-forwarded-traffic

az network vnet peering create \\
    --name dev-to-hub \\
    --resource-group $RG \\
    --vnet-name vnet-spoke-dev \\
    --remote-vnet vnet-hub \\
    --allow-vnet-access \\
    --allow-forwarded-traffic

# Hub -> Shared
az network vnet peering create \\
    --name hub-to-shared \\
    --resource-group $RG \\
    --vnet-name vnet-hub \\
    --remote-vnet vnet-spoke-shared \\
    --allow-vnet-access \\
    --allow-forwarded-traffic

az network vnet peering create \\
    --name shared-to-hub \\
    --resource-group $RG \\
    --vnet-name vnet-spoke-shared \\
    --remote-vnet vnet-hub \\
    --allow-vnet-access \\
    --allow-forwarded-traffic

# ═══════════════════════════════════════════════════════════════
# NETWORK SECURITY GROUPS
# ═══════════════════════════════════════════════════════════════
echo "🔒 Creating NSGs..."

# NSG for Production Web Tier
az network nsg create --name nsg-prod-web --resource-group $RG

az network nsg rule create \\
    --nsg-name nsg-prod-web --resource-group $RG \\
    --name AllowHTTPS --priority 100 \\
    --source-address-prefixes Internet \\
    --destination-port-ranges 443 --protocol Tcp --access Allow

az network nsg rule create \\
    --nsg-name nsg-prod-web --resource-group $RG \\
    --name AllowHTTP --priority 110 \\
    --source-address-prefixes Internet \\
    --destination-port-ranges 80 --protocol Tcp --access Allow

# NSG for Production App Tier
az network nsg create --name nsg-prod-app --resource-group $RG

az network nsg rule create \\
    --nsg-name nsg-prod-app --resource-group $RG \\
    --name AllowFromWeb --priority 100 \\
    --source-address-prefixes 10.1.1.0/24 \\
    --destination-port-ranges 8080 --protocol Tcp --access Allow

# NSG for Production DB Tier
az network nsg create --name nsg-prod-db --resource-group $RG

az network nsg rule create \\
    --nsg-name nsg-prod-db --resource-group $RG \\
    --name AllowFromApp --priority 100 \\
    --source-address-prefixes 10.1.2.0/24 \\
    --destination-port-ranges 1433 --protocol Tcp --access Allow

az network nsg rule create \\
    --nsg-name nsg-prod-db --resource-group $RG \\
    --name DenyFromDev --priority 200 \\
    --source-address-prefixes 10.2.0.0/16 \\
    --destination-port-ranges '*' --protocol '*' --access Deny

# Associate NSGs
az network vnet subnet update \\
    --vnet-name vnet-spoke-prod --resource-group $RG \\
    --name subnet-web --network-security-group nsg-prod-web

az network vnet subnet update \\
    --vnet-name vnet-spoke-prod --resource-group $RG \\
    --name subnet-app --network-security-group nsg-prod-app

az network vnet subnet update \\
    --vnet-name vnet-spoke-prod --resource-group $RG \\
    --name subnet-db --network-security-group nsg-prod-db

# ═══════════════════════════════════════════════════════════════
# AZURE BASTION
# ═══════════════════════════════════════════════════════════════
echo "🏰 Creating Azure Bastion..."

# Public IP for Bastion
az network public-ip create \\
    --name pip-bastion \\
    --resource-group $RG \\
    --location $LOCATION \\
    --sku Standard \\
    --allocation-method Static

# Create Bastion
az network bastion create \\
    --name bastion-hub \\
    --resource-group $RG \\
    --location $LOCATION \\
    --vnet-name vnet-hub \\
    --public-ip-address pip-bastion \\
    --sku Basic

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║           HUB-AND-SPOKE NETWORK DEPLOYED                   ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║                                                            ║"
echo "║  Hub VNet:     10.0.0.0/16                                 ║"
echo "║  +-- AzureFirewallSubnet: 10.0.0.0/26                     ║"
echo "║  +-- AzureBastionSubnet:  10.0.0.64/26                    ║"
echo "║  +-- subnet-management:   10.0.1.0/24                     ║"
echo "║                                                            ║"
echo "║  Spoke 1 (Prod): 10.1.0.0/16                               ║"
echo "║  +-- subnet-web: 10.1.1.0/24 [nsg-prod-web]               ║"
echo "║  +-- subnet-app: 10.1.2.0/24 [nsg-prod-app]               ║"
echo "║  +-- subnet-db:  10.1.3.0/24 [nsg-prod-db]                ║"
echo "║                                                            ║"
echo "║  Spoke 2 (Dev):  10.2.0.0/16                               ║"
echo "║  +-- subnet-dev: 10.2.1.0/24                              ║"
echo "║                                                            ║"
echo "║  Spoke 3 (Shared): 10.3.0.0/16                             ║"
echo "║  +-- subnet-ad:  10.3.1.0/24                              ║"
echo "║  +-- subnet-dns: 10.3.2.0/24                              ║"
echo "║                                                            ║"
echo "║  Access: Azure Bastion (bastion-hub)                       ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"

echo ""
echo "🔍 Traffic Flow Rules:"
echo "  • Internet -> Prod Web: Allowed (HTTPS/HTTP)"
echo "  • Prod Web -> Prod App: Allowed (8080)"
echo "  • Prod App -> Prod DB: Allowed (1433)"
echo "  • Dev -> Prod DB: BLOCKED"
echo "  • All spokes -> Shared Services: Allowed via Hub"
""",
        "xp": 25
    },

    # ========================================================================
    # METADATA
    # ========================================================================
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 12,
        "practice": 12,
        "quiz": 6,
        "challenge": 18
    },
    "xp_per_section": {
        "intro": 10,
        "concepts": 15,
        "practice": 30,
        "quiz": 30,
        "challenge": 25
    },
    "total_xp": 120,
    "topics_covered": [
        "virtual networks",
        "subnets",
        "network security groups",
        "vnet peering",
        "azure bastion",
        "hub-and-spoke",
        "cidr planning",
        "traffic filtering"
    ]
}
