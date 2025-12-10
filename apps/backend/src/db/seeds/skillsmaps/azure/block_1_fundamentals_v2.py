"""
Azure Cloud SkillsMap - Block 1: Azure Fundamentals (V2 - Interactive)
Node 2: Resource Groups & Management - DEMO av ny struktur
"""

from typing import Any

# ============================================================================
# NODE 2: RESOURCE MANAGEMENT (V2 - NY STRUKTUR)
# ============================================================================

AZURE_NODE_2_RESOURCES_V2 = {
    "node_id": 2,
    "title": "Resource Groups & Management",
    "slug": "azure-resource-management",
    "description": "Hantera Azure-resurser med Resource Groups och Tags",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,

    # Tidsfördelning per sektion (minuter)
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 8,
        "practice": 10,
        "quiz": 5,
        "challenge": 5
    },

    # =========================================================================
    # SEKTION 1: INTRO
    # =========================================================================
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

    # =========================================================================
    # SEKTION 2: KONCEPT
    # =========================================================================
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
| Storage Account | st | stwebshopprodne001 (inga bindestreck!) |
| Key Vault | kv | kv-webshop-prod-ne-001 |

**Regioner:**
- ne = North Europe (Irland)
- we = West Europe (Nederländerna)
- sc = Sweden Central (Gävle)
""",
            "common_mistake": "Storage Accounts tillåter INTE bindestreck. `st-webshop-prod` är ogiltigt, måste vara `stwebshopprod`."
        },
        {
            "title": "Tags - Din räddning för kostnadsspårning",
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
            "pro_tip": "Sätt ALLTID minst dessa tags: Environment, Project, Owner. Framtida-du kommer tacka dig."
        },
        {
            "title": "Resource Locks - Skydd mot misstag",
            "explanation": """
Locks förhindrar oavsiktlig radering eller ändring:

| Lock Type | Effekt |
|-----------|--------|
| **CanNotDelete** | Kan ändra, men EJ radera |
| **ReadOnly** | Kan INTE ändra eller radera |

**När använda:**
- CanNotDelete på alla produktions-Resource Groups
- ReadOnly på kritisk infrastruktur (VNet, DNS)
""",
            "common_mistake": "Glömmer att ta bort lock innan du försöker radera -> förvirrande felmeddelanden."
        }
    ],

    # =========================================================================
    # SEKTION 3: PRAKTIK (Simulerad terminal)
    # =========================================================================
    "practice": {
        "description": "Testa kommandona i den simulerade terminalen. Du kan inte göra något fel!",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa din första Resource Group",
                "instruction": "Skapa en resource group för ett dev-projekt i North Europe",
                "command": "az group create --name rg-demo-dev-ne-001 --location northeurope",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-demo-dev-ne-001",
  "location": "northeurope",
  "name": "rg-demo-dev-ne-001",
  "properties": {
    "provisioningState": "Succeeded"
  }
}""",
                "explanation": "Resource groupen skapas i North Europe. Namnet följer CAF-konventionen."
            },
            {
                "step": 2,
                "title": "Lägg till Tags",
                "instruction": "Lägg till tags för Environment och Project",
                "command": "az group update --name rg-demo-dev-ne-001 --tags Environment=Development Project=Demo Owner=dig@email.com",
                "expected_output": """{
  "name": "rg-demo-dev-ne-001",
  "tags": {
    "Environment": "Development",
    "Project": "Demo",
    "Owner": "dig@email.com"
  }
}""",
                "explanation": "Tags hjälper dig filtrera kostnader och hitta resurser snabbt."
            },
            {
                "step": 3,
                "title": "Lista alla Resource Groups",
                "instruction": "Visa alla resource groups i tabellformat",
                "command": "az group list --output table",
                "expected_output": """Name                    Location     Status
----------------------  -----------  ---------
rg-demo-dev-ne-001      northeurope  Succeeded
rg-webshop-prod-ne-001  northeurope  Succeeded""",
                "explanation": "--output table ger en läsbar översikt. Prova även --output json för scripting."
            },
            {
                "step": 4,
                "title": "Skapa ett Lock",
                "instruction": "Skydda resource groupen från oavsiktlig radering",
                "command": "az lock create --name DoNotDelete --resource-group rg-demo-dev-ne-001 --lock-type CanNotDelete",
                "expected_output": """{
  "name": "DoNotDelete",
  "level": "CanNotDelete",
  "notes": null
}""",
                "explanation": "Nu kan ingen radera denna resource group utan att först ta bort låset."
            },
            {
                "step": 5,
                "title": "Ta bort Lock (för att kunna radera)",
                "instruction": "Ta bort låset så du kan städa upp",
                "command": "az lock delete --name DoNotDelete --resource-group rg-demo-dev-ne-001",
                "expected_output": "",
                "explanation": "Inget output betyder success. Låset är nu borta."
            }
        ]
    },

    # =========================================================================
    # SEKTION 4: QUIZ
    # =========================================================================
    "quiz": {
        "passing_score": 80,  # Procent rätt för att klara
        "flashcards": [
            {
                "term": "Resource Group",
                "definition": "En logisk container som grupperar relaterade Azure-resurser för enklare hantering, åtkomstkontroll och livscykelhantering."
            },
            {
                "term": "Subscription",
                "definition": "En fakturerings- och åtkomstkontrollgräns i Azure. Resurser i en subscription delar samma faktura."
            },
            {
                "term": "Tag",
                "definition": "Ett key-value par som du lägger på resurser för organisation, kostnadsspårning och automation."
            },
            {
                "term": "Resource Lock (CanNotDelete)",
                "definition": "Ett skydd som förhindrar radering av en resurs, men tillåter ändringar."
            },
            {
                "term": "CAF (Cloud Adoption Framework)",
                "definition": "Microsofts best practices för Azure, inklusive naming conventions och organisationsstruktur."
            }
        ],
        "multiple_choice": [
            {
                "question": "Vad är rätt naming convention för en Storage Account enligt Microsoft CAF?",
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
                "question": "Du vill förhindra att någon raderar produktionsdatabasen av misstag. Vad använder du?",
                "options": [
                    "Tag med Environment=Production",
                    "Resource Lock med CanNotDelete",
                    "Resource Lock med ReadOnly",
                    "Flytta till separat Subscription"
                ],
                "correct_answer": 1,
                "explanation": "CanNotDelete-lock tillåter ändringar men förhindrar radering. ReadOnly skulle blockera även nödvändiga uppdateringar."
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
                "explanation": "Att radera en resource group raderar ALLT i den. Därför är locks och bra organisation så viktiga!"
            },
            {
                "question": "Vilken hierarki är korrekt i Azure?",
                "options": [
                    "Resource -> Resource Group -> Subscription -> Tenant",
                    "Tenant -> Resource Group -> Subscription -> Resource",
                    "Tenant -> Subscription -> Resource Group -> Resource",
                    "Subscription -> Tenant -> Resource Group -> Resource"
                ],
                "correct_answer": 2,
                "explanation": "Tenant (Azure AD) är toppen, sedan Subscription, Resource Group, och sist själva resurserna."
            },
            {
                "question": "Varför är Tags viktiga?",
                "options": [
                    "De är obligatoriska i Azure",
                    "De förbättrar prestanda",
                    "De möjliggör kostnadsspårning per projekt/team",
                    "De ersätter behov av Resource Groups"
                ],
                "correct_answer": 2,
                "explanation": "Tags låter dig filtrera kostnader, automatisera hantering och hitta resurser. De är inte obligatoriska men extremt värdefulla."
            }
        ]
    },

    # =========================================================================
    # SEKTION 5: CHALLENGE
    # =========================================================================
    "challenge": {
        "title": "Sätt upp en komplett projektstruktur",
        "scenario": """
Du har fått i uppdrag att sätta upp Azure-infrastrukturen för ett nytt projekt kallat "OrderAPI".
Projektet ska ha separata miljöer för Development och Production.
""",
        "requirements": [
            "Skapa två resource groups med korrekt naming convention (dev och prod)",
            "Båda ska vara i Sweden Central (swedencentral)",
            "Sätt tags: Environment, Project=OrderAPI, Owner=ditt-namn",
            "Sätt CanNotDelete-lock på prod-miljön"
        ],
        "validation": {
            "commands_to_run": [
                "az group list --query \"[?contains(name, 'orderapi')]\" --output table",
                "az lock list --resource-group rg-orderapi-prod-sc-001 --output table"
            ],
            "expected_results": [
                "Två resource groups: rg-orderapi-dev-sc-001 och rg-orderapi-prod-sc-001",
                "Lock 'DoNotDelete' finns på prod-gruppen"
            ]
        },
        "hints": [
            "Region-kod för Sweden Central är 'sc'",
            "Kom ihåg att sätta tags med --tags flaggan",
            "Lock-typen heter 'CanNotDelete' (med stort C och D)"
        ],
        "solution": """
# Steg 1: Skapa dev resource group
az group create \\
    --name rg-orderapi-dev-sc-001 \\
    --location swedencentral \\
    --tags Environment=Development Project=OrderAPI Owner=ditt-namn

# Steg 2: Skapa prod resource group
az group create \\
    --name rg-orderapi-prod-sc-001 \\
    --location swedencentral \\
    --tags Environment=Production Project=OrderAPI Owner=ditt-namn

# Steg 3: Sätt lock på prod
az lock create \\
    --name DoNotDelete \\
    --resource-group rg-orderapi-prod-sc-001 \\
    --lock-type CanNotDelete \\
    --notes "Production environment - do not delete"
"""
    },

    # =========================================================================
    # METADATA
    # =========================================================================
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
    "related_nodes": ["azure-introduction", "azure-subscriptions"]
}


# För jämförelse - exportera båda versionerna
def get_comparison():
    """Returnerar jämförelse mellan gammal och ny struktur"""
    return {
        "old_structure": {
            "fields": ["node_id", "title", "slug", "description", "difficulty",
                      "estimated_minutes", "xp_reward", "topics_covered", "content"],
            "content_type": "Endast markdown-text",
            "interactivity": "Ingen",
            "quiz": "Ingen",
            "practice": "Copy-paste exempel utan validering"
        },
        "new_structure": {
            "fields": ["node_id", "title", "slug", "description", "difficulty",
                      "estimated_minutes", "xp_reward", "intro", "concepts",
                      "practice", "quiz", "challenge", "completion_requirements",
                      "xp_breakdown", "next_node", "related_nodes"],
            "content_type": "Strukturerad data",
            "interactivity": "Simulerad terminal med validering",
            "quiz": "Flashcards + flervalsfrågor med 80% krav",
            "practice": "Steg-för-steg med förväntad output"
        }
    }
