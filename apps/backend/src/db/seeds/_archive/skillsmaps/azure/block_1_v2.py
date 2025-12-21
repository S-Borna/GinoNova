"""
Azure Cloud SkillsMap - Block 1: Azure Fundamentals (V2 Interactive)
Nodes 1-4: Intro, Resource Management, Portal/CLI, Subscriptions
"""

from typing import Any

# ============================================================================
# NODE 1: INTRODUCTION TO AZURE (V2)
# ============================================================================

AZURE_NODE_1_INTRO_V2 = {
    "node_id": 1,
    "title": "Introduction to Azure",
    "slug": "azure-introduction",
    "description": "Förstå Microsoft Azure och cloud computing koncept",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,

    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 10,
        "practice": 8,
        "quiz": 5,
        "challenge": 5
    },

    "intro": {
        "headline": "Välkommen till molnet",
        "hook": "Azure driver allt från Xbox Live till LinkedIn. Med 200+ tjänster och 60+ regioner är det plattformen som Fortune 500-företag litar på. Nu ska du lära dig grunderna.",
        "learning_objectives": [
            "Förstå skillnaden mellan IaaS, PaaS och SaaS",
            "Navigera Azures globala infrastruktur (Regioner, Zoner)",
            "Identifiera vilka Azure-tjänster som passar olika behov",
            "Skapa ett gratis Azure-konto och undvika kostnadsmisstag"
        ],
        "prerequisites": [
            "Grundläggande datorkunskap",
            "Ett Microsoft-konto (eller skapa ett gratis)"
        ],
        "estimated_time": "30 minuter"
    },

    "concepts": [
        {
            "title": "Cloud Computing Models",
            "explanation": """
Det finns tre huvudmodeller för molntjänster. Skillnaden handlar om **vem som ansvarar för vad**:

**IaaS (Infrastructure as a Service)**
- Du hyr virtuell hårdvara (VMs, nätverk, lagring)
- Du ansvarar för OS, runtime, applikationer
- Exempel: Azure VMs, Azure Storage

**PaaS (Platform as a Service)**
- Azure hanterar OS och runtime
- Du fokuserar på din kod
- Exempel: App Service, Azure Functions

**SaaS (Software as a Service)**
- Färdig mjukvara via webbläsaren
- Du använder, Azure sköter allt annat
- Exempel: Microsoft 365, Dynamics 365
""",
            "diagram": """
+-------------------------------------------------------------+
|           ANSVAR PER MODELL                                 |
+-------------------------------------------------------------+
|                                                             |
|  ON-PREM      IaaS        PaaS        SaaS                 |
|  +------+   +------+    +------+    +------+              |
|  | App  |   | App  |    | App  |    | App  | <- Azure      |
|  | Data |   | Data |    | Data |    | Data | <- Azure      |
|  | RT   |   | RT   |    | RT   | <-  | RT   | <- Azure      |
|  | OS   |   | OS   | <-  | OS   | <-  | OS   | <- Azure      |
|  | VM   |   | VM   | <-  | VM   | <-  | VM   | <- Azure      |
|  | HW   |   | HW   | <-  | HW   | <-  | HW   | <- Azure      |
|  +------+   +------+    +------+    +------+              |
|                                                             |
|  <- = Azure ansvarar                                        |
+-------------------------------------------------------------+
""",
            "pro_tip": "Starta med PaaS (App Service) för webappar. Du slipper hantera OS-uppdateringar och kan fokusera på kod.",
            "common_mistake": "Att välja IaaS (VMs) när PaaS räcker. VMs kräver underhåll och kostar mer."
        },
        {
            "title": "Azure Global Infrastructure",
            "explanation": """
Azure är uppbyggt i tre nivåer:

**Geography (Geografi)**
- Geopolitisk gräns (EU, US, Asia)
- Data stannar inom geografin för compliance

**Region**
- Ett kluster av datacenter (t.ex. "North Europe" i Irland)
- 60+ regioner globalt

**Availability Zone**
- Isolerade datacenter inom en region
- Egen ström, kyla, nätverk
- Skyddar mot datacenter-fel

**Populära regioner för Sverige:**
- Sweden Central (Gävle) - närmast
- North Europe (Irland) - billigare
- West Europe (Nederländerna) - stort utbud
""",
            "diagram": """
+-------------------------------------------------+
|        EUROPE GEOGRAPHY                         |
+-------------------------------------------------+
|                                                 |
|  +-----------------------------------------+   |
|  |  Sweden Central Region                   |   |
|  |  +-------+ +-------+ +-------+         |   |
|  |  | AZ 1  | | AZ 2  | | AZ 3  |         |   |
|  |  +-------+ +-------+ +-------+         |   |
|  +-----------------------------------------+   |
|                                                 |
|  +-----------------------------------------+   |
|  |  North Europe Region (Ireland)           |   |
|  |  +-------+ +-------+ +-------+         |   |
|  |  | AZ 1  | | AZ 2  | | AZ 3  |         |   |
|  |  +-------+ +-------+ +-------+         |   |
|  +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Välj Sweden Central för lägst latens från Sverige. North Europe är ofta billigare om latens inte är kritiskt."
        },
        {
            "title": "Core Azure Services",
            "explanation": """
Azure har 200+ tjänster. Här är de viktigaste per kategori:

| Kategori | Tjänst | Användning |
|----------|--------|------------|
| **Compute** | Virtual Machines | Kör hela servrar |
| **Compute** | App Service | Hosta webbappar (PaaS) |
| **Compute** | Functions | Serverless kod |
| **Compute** | AKS | Kubernetes-kluster |
| **Storage** | Blob Storage | Filer, bilder, backups |
| **Storage** | Files | Fildelning (SMB) |
| **Database** | Azure SQL | Managed SQL Server |
| **Database** | Cosmos DB | Global NoSQL |
| **Network** | Virtual Network | Isolerade nätverk |
| **Network** | Load Balancer | Trafikfördelning |
| **Identity** | Azure AD | Användare & grupper |
| **DevOps** | Azure DevOps | CI/CD pipelines |
""",
            "pro_tip": "Börja med App Service + Azure SQL för en typisk webbapp. Det täcker 80% av användningsfallen."
        }
    ],

    "practice": {
        "description": "Låt oss utforska Azure CLI - verktyget du kommer använda dagligen för att hantera Azure-resurser.",
        "exercises": [
            {
                "step": 1,
                "title": "Logga in på Azure",
                "instruction": "Öppna Azure CLI och logga in med ditt konto",
                "command": "az login",
                "expected_output": """[
  {
    "cloudName": "AzureCloud",
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "isDefault": true,
    "name": "Din Subscription",
    "state": "Enabled",
    "tenantId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
]""",
                "explanation": "Detta öppnar en webbläsare för autentisering och kopplar din CLI till ditt Azure-konto."
            },
            {
                "step": 2,
                "title": "Lista tillgängliga regioner",
                "instruction": "Se vilka regioner som finns tillgängliga",
                "command": "az account list-locations --output table",
                "expected_output": """DisplayName          Name                 RegionalDisplayName
-------------------  -------------------  -----------------------
Sweden Central       swedencentral        (Europe) Sweden Central
North Europe         northeurope          (Europe) North Europe
West Europe          westeurope           (Europe) West Europe
UK South             uksouth              (Europe) UK South""",
                "explanation": "Azure har 60+ regioner. 'Name' är vad du använder i kommandon (t.ex. 'swedencentral')."
            },
            {
                "step": 3,
                "title": "Kolla din subscription",
                "instruction": "Verifiera vilken subscription du är kopplad till",
                "command": "az account show --output table",
                "expected_output": """Name              CloudName    State    IsDefault
----------------  -----------  -------  ----------
Din Subscription  AzureCloud   Enabled  True""",
                "explanation": "Du kan ha flera subscriptions. --output table ger en läsbar vy."
            },
            {
                "step": 4,
                "title": "Se tillgängliga VM-storlekar",
                "instruction": "Lista VM-storlekar i Sweden Central",
                "command": "az vm list-sizes --location swedencentral --output table | head -10",
                "expected_output": """MaxDataDiskCount    MemoryInMb    Name              NumberOfCores    OsDiskSizeInMb
------------------  ------------  ----------------  ---------------  ----------------
4                   3584          Standard_B1ms     1                1047552
4                   7168          Standard_B2s      2                1047552
8                   16384         Standard_B4ms     4                1047552""",
                "explanation": "B-serien är burstable VMs - perfekt för dev/test. D-serien för produktion."
            }
        ]
    },

    "quiz": {
        "passing_score": 80,
        "flashcards": [
            {
                "term": "IaaS",
                "definition": "Infrastructure as a Service - Du hyr virtuell hårdvara och ansvarar för OS och applikationer. Exempel: Azure VMs."
            },
            {
                "term": "PaaS",
                "definition": "Platform as a Service - Azure hanterar infrastruktur och OS, du fokuserar på kod. Exempel: App Service."
            },
            {
                "term": "SaaS",
                "definition": "Software as a Service - Färdig mjukvara via webben. Exempel: Microsoft 365."
            },
            {
                "term": "Region",
                "definition": "Ett kluster av Azure-datacenter på en geografisk plats. Exempel: Sweden Central, North Europe."
            },
            {
                "term": "Availability Zone",
                "definition": "Ett isolerat datacenter inom en region med egen ström och nätverk. Skyddar mot datacenter-fel."
            }
        ],
        "multiple_choice": [
            {
                "question": "Du vill hosta en webbapp utan att hantera operativsystem. Vilken tjänst väljer du?",
                "options": [
                    "Azure Virtual Machines",
                    "Azure App Service",
                    "Azure Blob Storage",
                    "Azure Virtual Network"
                ],
                "correct_answer": 1,
                "explanation": "App Service är PaaS - Azure hanterar OS och du fokuserar på din kod. VMs (IaaS) kräver att du hanterar OS själv."
            },
            {
                "question": "Vad är skillnaden mellan en Region och en Availability Zone?",
                "options": [
                    "De betyder samma sak",
                    "En Region innehåller flera Availability Zones",
                    "En Availability Zone innehåller flera Regioner",
                    "Availability Zones finns bara i USA"
                ],
                "correct_answer": 1,
                "explanation": "En Region är ett kluster av datacenter. Availability Zones är isolerade datacenter INOM en region för högre tillgänglighet."
            },
            {
                "question": "Vilken region bör du välja för lägst latens från Sverige?",
                "options": [
                    "North Europe (Irland)",
                    "West Europe (Nederländerna)",
                    "Sweden Central (Gävle)",
                    "UK South (London)"
                ],
                "correct_answer": 2,
                "explanation": "Sweden Central ligger i Gävle och ger lägst latens för svenska användare."
            },
            {
                "question": "Vad är Azure Blob Storage bäst för?",
                "options": [
                    "Köra virtuella maskiner",
                    "Lagra filer, bilder och backups",
                    "Hosta webbapplikationer",
                    "Skapa virtuella nätverk"
                ],
                "correct_answer": 1,
                "explanation": "Blob Storage är för ostrukturerad data som filer, bilder, videos och backups."
            },
            {
                "question": "Vilket CLI-kommando visar vilka Azure-regioner som finns?",
                "options": [
                    "az region list",
                    "az account list-locations",
                    "az location show",
                    "az regions get"
                ],
                "correct_answer": 1,
                "explanation": "az account list-locations visar alla tillgängliga regioner för din subscription."
            }
        ]
    },

    "challenge": {
        "title": "Utforska Azure Portal",
        "scenario": """
Du har precis fått tillgång till ett Azure-konto. Innan du skapar några resurser behöver du
bekanta dig med miljön och sätta upp grundläggande kostnadskontroll.
""",
        "requirements": [
            "Logga in på Azure Portal (portal.azure.com)",
            "Hitta Cost Management + Billing i menyn",
            "Skapa en budget-alert för $10 (eller valfritt belopp)",
            "Hitta minst 3 olika Azure-tjänster i 'Create a resource'",
            "Identifiera vilken region som är närmast dig"
        ],
        "hints": [
            "Sök efter 'Budgets' i sökfältet högst upp",
            "Cost Management finns under din Subscription",
            "'Create a resource' visar alla tillgängliga tjänster"
        ],
        "solution": """
# 1. Gå till portal.azure.com och logga in

# 2. Hitta Cost Management:
#    - Klicka på din Subscription i vänstermenyn
#    - Välj "Cost Management" -> "Budgets"
#    - Klicka "Add" för att skapa budget

# 3. Skapa budget:
#    - Name: "Monthly-Alert"
#    - Amount: 10 (eller valfritt)
#    - Alert conditions: 80% of budget
#    - Alert recipients: din email

# 4. Utforska tjänster:
#    - Klicka "Create a resource"
#    - Kategorier: Compute, Networking, Storage, Databases

# 5. Hitta närmaste region:
#    - Sök efter "Virtual Machines"
#    - Klicka "Create"
#    - Dropdown "Region" visar alla, välj Sweden Central
""",
        "xp_bonus": 20
    },

    "completion_requirements": {
        "quiz_minimum_score": 80,
        "practice_completed": True,
        "challenge_optional": True
    },
    "xp_breakdown": {
        "concepts_read": 20,
        "practice_completed": 30,
        "quiz_passed": 30,
        "challenge_completed": 20
    },
    "next_node": "azure-resource-management",
    "related_nodes": []
}


# ============================================================================
# NODE 2: RESOURCE MANAGEMENT (V2)
# ============================================================================

AZURE_NODE_2_RESOURCES_V2 = {
    "node_id": 2,
    "title": "Resource Groups & Management",
    "slug": "azure-resource-management",
    "description": "Hantera Azure-resurser med Resource Groups och Tags",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,

    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 8,
        "practice": 10,
        "quiz": 5,
        "challenge": 5
    },

    "intro": {
        "headline": "Organisera ditt Azure-kaos",
        "hook": "Utan Resource Groups blir din Azure-miljö en röra av 200 resurser utan struktur. Med rätt organisation hittar du allt på sekunder och kan radera hela miljöer med ett kommando.",
        "learning_objectives": [
            "Förstå Azure-hierarkin (Tenant -> Subscription -> Resource Group -> Resource)",
            "Skapa och hantera Resource Groups med Azure CLI",
            "Använda naming conventions enligt Microsoft CAF",
            "Skydda resurser med Tags och Locks"
        ],
        "prerequisites": [
            "Azure-konto (gratis fungerar)",
            "Azure CLI installerat (eller använd Cloud Shell)"
        ],
        "estimated_time": "30 minuter"
    },

    "concepts": [
        {
            "title": "Azure Resource Hierarchy",
            "explanation": """
Allt i Azure följer en hierarki. Tänk på det som mappar på din dator:

**Tenant** (Azure AD) -> Din organisation
  +-- **Subscription** -> Faktureringscontainer (en per miljö/avdelning)
      +-- **Resource Group** -> Logisk mapp för relaterade resurser
          +-- **Resources** -> VMs, databaser, storage, etc.

**Varför detta spelar roll:**
- RBAC (rättigheter) ärvs nedåt i hierarkin
- Kostnader aggregeras uppåt
- Radera en Resource Group = alla resurser i den försvinner
""",
            "diagram": """
+-------------------------------------------------+
|           AZURE AD TENANT                       |
|           (din-organisation.onmicrosoft.com)    |
+-------------------------------------------------+
|  +--------------+  +--------------+            |
|  | Dev Subscr.  |  | Prod Subscr. |            |
|  +------+-------+  +------+-------+            |
|         |                 |                     |
|   +-----+-----+     +-----+-----+              |
|   | rg-app-dev|     |rg-app-prod|              |
|   +-----+-----+     +-----+-----+              |
|         |                 |                     |
|    [VM] [DB]         [VM] [DB]                 |
+-------------------------------------------------+
""",
            "pro_tip": "Ha separata Subscriptions för Dev och Prod - det är det enklaste sättet att isolera kostnader och förhindra misstag."
        },
        {
            "title": "Naming Conventions (Microsoft CAF)",
            "explanation": """
Ett bra namn berättar allt du behöver veta:

**Format:** `{typ}-{app}-{miljö}-{region}-{nummer}`

| Resurs | Prefix | Exempel |
|--------|--------|---------|
| Resource Group | rg | rg-webshop-prod-ne-001 |
| Virtual Machine | vm | vm-webshop-prod-ne-001 |
| Storage Account | st | stwebshopprodne001 |
| Key Vault | kv | kv-webshop-prod-ne-001 |

**Regioner:**
- ne = North Europe
- we = West Europe
- sc = Sweden Central
""",
            "common_mistake": "Storage Accounts tillåter INTE bindestreck. `st-webshop-prod` är ogiltigt, måste vara `stwebshopprod`."
        },
        {
            "title": "Tags - Kostnadsspårning",
            "explanation": """
Tags är key-value par du sätter på resurser:

```
Environment = Production
Project = Webshop
CostCenter = CC-123
Owner = team@company.com
```

**Varför tags är livsviktiga:**
1. **Cost Management** - Filtrera kostnader per projekt
2. **Automation** - "Stäng av alla VMs med Environment=Dev kl 18:00"
3. **Governance** - Azure Policy kan kräva tags
""",
            "pro_tip": "Sätt ALLTID minst dessa tags: Environment, Project, Owner."
        },
        {
            "title": "Resource Locks",
            "explanation": """
Locks förhindrar oavsiktlig radering eller ändring:

| Lock Type | Effekt |
|-----------|--------|
| **CanNotDelete** | Kan ändra, men EJ radera |
| **ReadOnly** | Kan INTE ändra eller radera |

**När använda:**
- CanNotDelete på alla produktions-Resource Groups
- ReadOnly på kritisk infrastruktur
""",
            "common_mistake": "Glömmer att ta bort lock innan du försöker radera -> förvirrande felmeddelanden."
        }
    ],

    "practice": {
        "description": "Testa kommandona i den simulerade terminalen.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa Resource Group",
                "instruction": "Skapa en resource group för ett dev-projekt i North Europe",
                "command": "az group create --name rg-demo-dev-ne-001 --location northeurope",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-demo-dev-ne-001",
  "location": "northeurope",
  "name": "rg-demo-dev-ne-001",
  "properties": { "provisioningState": "Succeeded" }
}""",
                "explanation": "Resource groupen skapas i North Europe med CAF-namnkonvention."
            },
            {
                "step": 2,
                "title": "Lägg till Tags",
                "instruction": "Tagga resource groupen med Environment och Project",
                "command": "az group update --name rg-demo-dev-ne-001 --tags Environment=Development Project=Demo Owner=dig@email.com",
                "expected_output": """{
  "name": "rg-demo-dev-ne-001",
  "tags": {
    "Environment": "Development",
    "Project": "Demo",
    "Owner": "dig@email.com"
  }
}""",
                "explanation": "Tags hjälper dig filtrera kostnader och hitta resurser."
            },
            {
                "step": 3,
                "title": "Lista Resource Groups",
                "instruction": "Visa alla resource groups i tabellformat",
                "command": "az group list --output table",
                "expected_output": """Name                    Location     Status
----------------------  -----------  ---------
rg-demo-dev-ne-001      northeurope  Succeeded""",
                "explanation": "--output table ger en läsbar översikt."
            },
            {
                "step": 4,
                "title": "Skapa Lock",
                "instruction": "Skydda resource groupen från radering",
                "command": "az lock create --name DoNotDelete --resource-group rg-demo-dev-ne-001 --lock-type CanNotDelete",
                "expected_output": """{
  "name": "DoNotDelete",
  "level": "CanNotDelete"
}""",
                "explanation": "Nu kan ingen radera denna resource group utan att först ta bort låset."
            },
            {
                "step": 5,
                "title": "Ta bort Lock",
                "instruction": "Ta bort låset (för att kunna städa upp)",
                "command": "az lock delete --name DoNotDelete --resource-group rg-demo-dev-ne-001",
                "expected_output": "",
                "explanation": "Inget output betyder success."
            }
        ]
    },

    "quiz": {
        "passing_score": 80,
        "flashcards": [
            {
                "term": "Resource Group",
                "definition": "Logisk container som grupperar relaterade Azure-resurser för hantering, åtkomstkontroll och livscykel."
            },
            {
                "term": "Subscription",
                "definition": "Fakturerings- och åtkomstkontrollgräns i Azure. Resurser i en subscription delar samma faktura."
            },
            {
                "term": "Tag",
                "definition": "Key-value par på resurser för organisation, kostnadsspårning och automation."
            },
            {
                "term": "Resource Lock",
                "definition": "Skydd som förhindrar radering (CanNotDelete) eller ändringar (ReadOnly) av resurser."
            },
            {
                "term": "CAF",
                "definition": "Cloud Adoption Framework - Microsofts best practices för Azure, inklusive naming conventions."
            }
        ],
        "multiple_choice": [
            {
                "question": "Vad är rätt naming convention för en Storage Account?",
                "options": [
                    "st-webshop-prod-ne-001",
                    "stwebshopprodne001",
                    "storage-webshop-prod",
                    "sa-webshop-prod-ne-001"
                ],
                "correct_answer": 1,
                "explanation": "Storage Accounts tillåter inte bindestreck. Prefix är 'st' och allt skrivs ihop."
            },
            {
                "question": "Du vill förhindra att någon raderar produktionsdatabasen. Vad använder du?",
                "options": [
                    "Tag med Environment=Production",
                    "Resource Lock med CanNotDelete",
                    "Resource Lock med ReadOnly",
                    "Flytta till separat Subscription"
                ],
                "correct_answer": 1,
                "explanation": "CanNotDelete-lock tillåter ändringar men förhindrar radering."
            },
            {
                "question": "Vad händer när du raderar en Resource Group?",
                "options": [
                    "Endast tomma resource groups kan raderas",
                    "Du får en varning men resurserna finns kvar",
                    "ALLA resurser i gruppen raderas permanent",
                    "Resurserna flyttas till en default-grupp"
                ],
                "correct_answer": 2,
                "explanation": "Att radera en resource group raderar ALLT i den."
            },
            {
                "question": "Vilken hierarki är korrekt?",
                "options": [
                    "Resource -> Resource Group -> Subscription -> Tenant",
                    "Tenant -> Resource Group -> Subscription -> Resource",
                    "Tenant -> Subscription -> Resource Group -> Resource",
                    "Subscription -> Tenant -> Resource Group -> Resource"
                ],
                "correct_answer": 2,
                "explanation": "Tenant är toppen, sedan Subscription, Resource Group, och sist resurser."
            },
            {
                "question": "Varför är Tags viktiga?",
                "options": [
                    "De är obligatoriska i Azure",
                    "De förbättrar prestanda",
                    "De möjliggör kostnadsspårning per projekt",
                    "De ersätter Resource Groups"
                ],
                "correct_answer": 2,
                "explanation": "Tags låter dig filtrera kostnader och automatisera hantering."
            }
        ]
    },

    "challenge": {
        "title": "Sätt upp projektstruktur",
        "scenario": "Du ska sätta upp Azure-infrastrukturen för projekt 'OrderAPI' med Dev och Prod-miljöer.",
        "requirements": [
            "Skapa rg-orderapi-dev-sc-001 i Sweden Central",
            "Skapa rg-orderapi-prod-sc-001 i Sweden Central",
            "Tagga båda med Environment, Project=OrderAPI, Owner",
            "Sätt CanNotDelete-lock på prod-gruppen"
        ],
        "hints": [
            "Region-kod för Sweden Central är 'swedencentral'",
            "Lock-typen heter 'CanNotDelete' (med stort C och D)"
        ],
        "solution": """
# Dev
az group create --name rg-orderapi-dev-sc-001 --location swedencentral \\
    --tags Environment=Development Project=OrderAPI Owner=dig

# Prod
az group create --name rg-orderapi-prod-sc-001 --location swedencentral \\
    --tags Environment=Production Project=OrderAPI Owner=dig

# Lock
az lock create --name DoNotDelete --resource-group rg-orderapi-prod-sc-001 \\
    --lock-type CanNotDelete
""",
        "xp_bonus": 20
    },

    "completion_requirements": {
        "quiz_minimum_score": 80,
        "practice_completed": True,
        "challenge_optional": True
    },
    "xp_breakdown": {
        "concepts_read": 20,
        "practice_completed": 30,
        "quiz_passed": 30,
        "challenge_completed": 20
    },
    "next_node": "azure-portal-cli",
    "related_nodes": ["azure-introduction"]
}


# ============================================================================
# BLOCK 1 NODES LIST (V2)
# ============================================================================

BLOCK_1_NODES_V2 = [
    AZURE_NODE_1_INTRO_V2,
    AZURE_NODE_2_RESOURCES_V2,
    # Node 3 och 4 kommer här
]
