# ============================================================================
# AZURE BLOCK 1 - NODE 2: RESOURCE GROUPS & MANAGEMENT (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_2_V2 = {
    "node_id": 2,
    "title": "Resource Groups & Management",
    "slug": "azure-resource-management",
    "description": "Hantera Azure-resurser med Resource Groups och Tags",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Organisera Azure som ett proffs",
        "hook": "Utan struktur blir molnet kaos. Resource Groups är din ordning i stormen.",
        "learning_objectives": [
            "Förstå Azure resource hierarchy (Tenant -> Subscription -> Resource Group -> Resource)",
            "Skapa och hantera Resource Groups med Azure CLI",
            "Använda Tags för kostnadsuppföljning och organisation",
            "Sätta Resource Locks för att skydda kritiska resurser",
            "Designa en skalbar resursstruktur för enterprise"
        ],
        "prerequisites": [
            "Azure-konto (free tier räcker)",
            "Azure CLI installerat",
            "Grundläggande terminalkunskap"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "hierarchy",
            "title": "Azure Resource Hierarchy",
            "explanation": """Azure organiserar resurser i en strikt hierarki:

**1. Azure AD Tenant** (överst)
- Din organisations identitet
- Innehåller användare, grupper, service principals
- Ett företag = en tenant

**2. Management Groups** (valfritt)
- Grupperar flera subscriptions
- Applicera policies på företagsnivå
- Max 6 nivåer djupt

**3. Subscriptions**
- Faktureringsenheter
- Separera dev/test/prod
- Har egna kvoter och limits

**4. Resource Groups**
- Logiska containers för resurser
- ALLA resurser måste finnas i en RG
- Lifecycle management (ta bort allt på en gång)

**5. Resources** (nederst)
- Faktiska tjänster: VMs, databaser, storage
- Ärver permissions från RG""",
            "diagram": """
+-------------------------------------------------+
|           AZURE AD TENANT                        |
|  (contoso.onmicrosoft.com)                      |
+-------------------------------------------------+
|         MANAGEMENT GROUP                         |
|  +---------------+---------------+              |
|  |   MG-Prod     |   MG-NonProd  |              |
+--+---------------+---------------+--------------+
|           SUBSCRIPTIONS                          |
|  +---------+ +---------+ +---------+           |
|  |Sub-Prod | |Sub-Dev  | |Sub-Test |           |
+--+---------+-+---------+-+---------+------------+
|         RESOURCE GROUPS                          |
|  +------------+ +------------+                  |
|  |rg-app-prod | |rg-db-prod  |                  |
+--+------------+-+------------+------------------+
|            RESOURCES                             |
|  [VM] [Storage] [SQL] [App Service]             |
+-------------------------------------------------+
""",
            "pro_tip": "En Resource Group kan innehålla resurser från olika regioner, men RG:n själv har en 'location' för metadata.",
            "common_mistake": "Att sätta ALLA resurser i en enda Resource Group. Separera efter applikation, miljö eller livscykel."
        },
        {
            "id": "resource-groups",
            "title": "Resource Groups Best Practices",
            "explanation": """Resource Groups är containers - men hur ska du strukturera dem?

**Strategi 1: Per Applikation**
```
rg-webapp-prod
+-- app-service
+-- sql-database
+-- storage-account
```

**Strategi 2: Per Resurstyp**
```
rg-compute-prod
+-- vm-web-01
+-- vm-web-02
+-- vm-api-01

rg-data-prod
+-- sql-main
+-- cosmos-cache
```

**Strategi 3: Per Miljö (Rekommenderat)**
```
rg-myapp-dev
rg-myapp-test
rg-myapp-prod
```

**Namnkonvention:**
`rg-<app>-<env>-<region>`
Exempel: `rg-webshop-prod-neu`""",
            "diagram": """
+-------------------------------------------------+
|     RESOURCE GROUP NAMING CONVENTION            |
+-------------------------------------------------+
|                                                 |
|   rg - webshop - prod - neu                     |
|   |      |        |      |                      |
|   |      |        |      +-- Region (northeu)   |
|   |      |        +-- Environment               |
|   |      +-- Application name                   |
|   +-- Resource type prefix                      |
|                                                 |
|   Examples:                                     |
|   • rg-webshop-prod-neu                         |
|   • rg-api-dev-weu                              |
|   • rg-shared-infra-global                      |
+-------------------------------------------------+
""",
            "pro_tip": "Sätt aldrig produktion och utveckling i samma Resource Group. När någon råkar köra 'az group delete' på dev...",
            "common_mistake": "Att använda svenska/långa namn som 'MinFörstaResursGrupp'. Håll dig till engelska, lowercase, bindestreck."
        },
        {
            "id": "tags",
            "title": "Tags för Kostnads­uppföljning",
            "explanation": """Tags är key-value pairs som du kan sätta på ALLA Azure-resurser.

**Varför Tags?**
- Filtrera kostnader per projekt/team
- Hitta resurser snabbt
- Automation (stäng av alla VMs med tag 'env=dev')
- Compliance och governance

**Obligatoriska Tags (rekommendation):**
| Tag | Syfte | Exempel |
|-----|-------|---------|
| `environment` | Miljö | dev, test, prod |
| `owner` | Ansvarig | team-platform |
| `cost-center` | Fakturering | CC-12345 |
| `project` | Projekt | webshop-v2 |

**Bonus Tags:**
| Tag | Syfte | Exempel |
|-----|-------|---------|
| `created-by` | Vem skapade | terraform, manual |
| `expiry-date` | Auto-cleanup | 2024-12-31 |
| `criticality` | SLA-nivå | high, medium, low |""",
            "diagram": """
+-------------------------------------------------+
|              TAGGING STRATEGY                    |
+-------------------------------------------------+
|                                                 |
|   +-----------------------------------------+   |
|   |  vm-web-01                              |   |
|   |  +-- environment: prod                  |   |
|   |  +-- owner: team-web                    |   |
|   |  +-- cost-center: CC-WEB-001           |   |
|   |  +-- project: e-commerce               |   |
|   |  +-- criticality: high                 |   |
|   +-----------------------------------------+   |
|                                                 |
|   Cost Analysis -> Filter by tag:cost-center     |
|   +-----------------------------------------+   |
|   | CC-WEB-001:     $1,234                  |   |
|   | CC-API-001:     $567                    |   |
|   | CC-DATA-001:    $2,345                  |   |
|   +-----------------------------------------+   |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Azure Policy för att KRÄVA tags. Ingen resurs utan 'cost-center' tag får skapas.",
            "common_mistake": "Inkonsekvent tagging: 'Environment', 'environment', 'env', 'ENV'. Bestäm EN standard och håll dig till den."
        },
        {
            "id": "locks",
            "title": "Resource Locks",
            "explanation": """Resource Locks skyddar resurser från oavsiktlig radering eller ändring.

**Två typer av locks:**

**1. CanNotDelete (Delete Lock)**
- Kan modifiera resursen
- KAN INTE radera
- Perfekt för produktion

**2. ReadOnly**
- KAN INTE modifiera eller radera
- Bara läsa
- Perfekt för audit/compliance

**Lock-nivåer:**
- Subscription-nivå -> gäller alla RGs
- Resource Group-nivå -> gäller alla resurser i RG
- Resurs-nivå -> gäller enskild resurs

**OBS:** Locks ärvs nedåt men kan INTE åsidosättas underifrån.""",
            "diagram": """
+-------------------------------------------------+
|              RESOURCE LOCKS                      |
+-------------------------------------------------+
|                                                 |
|   DELETE LOCK                                   |
|   +-----------------------------------------+   |
|   |  🔒 rg-prod-database                    |   |
|   |     +-- ✅ az sql db update (OK)        |   |
|   |     +-- ❌ az sql db delete (BLOCKED)   |   |
|   +-----------------------------------------+   |
|                                                 |
|   READONLY LOCK                                 |
|   +-----------------------------------------+   |
|   |  🔒 rg-audit-logs                       |   |
|   |     +-- ❌ az storage update (BLOCKED)  |   |
|   |     +-- ❌ az storage delete (BLOCKED)  |   |
|   +-----------------------------------------+   |
|                                                 |
|   ⚠️  Owner-rättighet krävs för att ta bort    |
|       locks!                                    |
+-------------------------------------------------+
""",
            "pro_tip": "Sätt Delete Lock på ALLA produktions-databaser dag ett. Någon KOMMER råka klicka delete någon gång.",
            "common_mistake": "Att glömma ta bort lock innan planerat underhåll. Plötsligt fungerar inte ditt Terraform apply."
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du skapa en komplett resursstruktur med Resource Groups, Tags och Locks.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa Resource Group",
                "instruction": "Skapa en Resource Group för din dev-miljö i North Europe.",
                "hint": "Använd 'az group create' med --name och --location",
                "expected_command": "az group create --name rg-myapp-dev --location northeurope",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-dev",
  "location": "northeurope",
  "name": "rg-myapp-dev",
  "properties": {
    "provisioningState": "Succeeded"
  }
}""",
                "explanation": "Resource Groups har alltid en location för metadata, även om resurserna i gruppen kan finnas i andra regioner.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Lägg till Tags på Resource Group",
                "instruction": "Tagga Resource Group med environment=dev och owner=team-platform.",
                "hint": "Använd 'az group update' med --tags",
                "expected_command": "az group update --name rg-myapp-dev --tags environment=dev owner=team-platform cost-center=CC-DEV-001",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-dev",
  "location": "northeurope",
  "name": "rg-myapp-dev",
  "tags": {
    "cost-center": "CC-DEV-001",
    "environment": "dev",
    "owner": "team-platform"
  }
}""",
                "explanation": "Tags på Resource Group ärvs INTE automatiskt till resurser inuti. Du måste tagga resurser separat eller använda Azure Policy.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Skapa Production Resource Group",
                "instruction": "Skapa en produktions-RG med samma struktur.",
                "hint": "Samma kommando, byt 'dev' till 'prod'",
                "expected_command": "az group create --name rg-myapp-prod --location northeurope --tags environment=prod owner=team-platform cost-center=CC-PROD-001 criticality=high",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-prod",
  "location": "northeurope",
  "name": "rg-myapp-prod",
  "tags": {
    "cost-center": "CC-PROD-001",
    "criticality": "high",
    "environment": "prod",
    "owner": "team-platform"
  }
}""",
                "explanation": "Du kan sätta tags direkt vid skapande med --tags istället för att köra update efteråt.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Sätt Delete Lock på Produktion",
                "instruction": "Skydda produktions-RG från oavsiktlig radering.",
                "hint": "Använd 'az lock create' med --lock-type CanNotDelete",
                "expected_command": "az lock create --name DoNotDelete --resource-group rg-myapp-prod --lock-type CanNotDelete --notes 'Production environment - do not delete'",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-prod/providers/Microsoft.Authorization/locks/DoNotDelete",
  "level": "CanNotDelete",
  "name": "DoNotDelete",
  "notes": "Production environment - do not delete"
}""",
                "explanation": "Nu kan ingen radera denna Resource Group eller resurser i den utan att först ta bort låset.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Lista alla Resource Groups med Tags",
                "instruction": "Visa alla RGs med deras tags i tabellformat.",
                "hint": "Använd 'az group list' med --query och --output table",
                "expected_command": "az group list --query \"[].{Name:name,Location:location,Environment:tags.environment}\" --output table",
                "expected_output": """Name              Location      Environment
----------------  ------------  -------------
rg-myapp-dev      northeurope   dev
rg-myapp-prod     northeurope   prod""",
                "explanation": "JMESPath queries med --query låter dig välja exakt vilka fält du vill se. Perfekt för scripting.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Verifiera Lock",
                "instruction": "Kontrollera att låset är på plats.",
                "hint": "Använd 'az lock list'",
                "expected_command": "az lock list --resource-group rg-myapp-prod --output table",
                "expected_output": """Name          Level          Notes
------------  -------------  ------------------------------------
DoNotDelete   CanNotDelete   Production environment - do not delete""",
                "explanation": "Kom ihåg: för att ta bort ett lock behöver du Owner eller User Access Administrator-rollen.",
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
                "front": "Vad är hierarkin i Azure uppifrån och ner?",
                "back": "Tenant -> Management Groups -> Subscriptions -> Resource Groups -> Resources"
            },
            {
                "id": "fc2",
                "front": "Kan en Resource Group innehålla resurser från olika regioner?",
                "back": "JA! RG har en location för metadata, men resurser inuti kan vara i vilken region som helst."
            },
            {
                "id": "fc3",
                "front": "Vad är skillnaden mellan CanNotDelete och ReadOnly lock?",
                "back": "CanNotDelete: Kan ändra, ej radera. ReadOnly: Kan varken ändra eller radera."
            },
            {
                "id": "fc4",
                "front": "Ärver resurser tags från sin Resource Group?",
                "back": "NEJ! Tags ärvs inte automatiskt. Använd Azure Policy för att tvinga tag-arv."
            },
            {
                "id": "fc5",
                "front": "Vilken roll krävs för att ta bort en Resource Lock?",
                "back": "Owner eller User Access Administrator på den nivå där låset sitter."
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du vill spåra kostnader per projekt i Azure. Vilket är bästa sättet?",
                "options": [
                    "Skapa en subscription per projekt",
                    "Använda konsekvent tagging med cost-center",
                    "Sätta alla projektresurser i samma region",
                    "Använda Resource Locks"
                ],
                "correct_answer": 1,
                "explanation": "Tags med cost-center eller project-namn låter dig filtrera kostnader i Cost Analysis utan att behöva separata subscriptions."
            },
            {
                "id": "mc2",
                "question": "Vad händer om du försöker radera en resurs som har ett CanNotDelete lock?",
                "options": [
                    "Resursen raderas ändå",
                    "Du får en varning men kan fortsätta",
                    "Operationen blockeras med ett felmeddelande",
                    "Låset tas bort automatiskt"
                ],
                "correct_answer": 2,
                "explanation": "CanNotDelete lock blockerar all delete-operationer. Du måste explicit ta bort låset först (kräver rätt behörighet)."
            },
            {
                "id": "mc3",
                "question": "Vilken namnkonvention rekommenderas för Resource Groups?",
                "options": [
                    "RG_AppName_Environment",
                    "rg-<app>-<env>-<region>",
                    "ResourceGroup.AppName.Env",
                    "Valfritt namn som beskriver innehållet"
                ],
                "correct_answer": 1,
                "explanation": "Azure rekommenderar lowercase med bindestreck: rg-<app>-<env>-<region>. Exempel: rg-webshop-prod-neu"
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Bygg Enterprise Resource Structure",
        "scenario": """Du är ny på ett företag som ska migrera till Azure. De har tre applikationer:
- **webshop** (e-commerce, kritisk)
- **internal-tools** (interna verktyg, medium)
- **sandbox** (experiment, låg prioritet)

Varje app behöver dev, test och prod-miljöer. VD:n vill kunna se kostnader per app OCH per miljö.""",
        "requirements": [
            "Skapa Resource Groups för alla kombinationer (9 st totalt)",
            "Använd konsekvent namnkonvention: rg-<app>-<env>",
            "Tagga ALLA med: environment, owner, cost-center, criticality",
            "Sätt Delete Lock på ALLA prod-RGs",
            "Bonus: Skriv ett bash-script som skapar allt automatiskt"
        ],
        "hints": [
            "Använd variabler i bash för att undvika upprepning",
            "Kritikalitet: webshop=high, internal-tools=medium, sandbox=low",
            "Cost-centers: CC-WEBSHOP, CC-INTERNAL, CC-SANDBOX"
        ],
        "solution": """#!/bin/bash
# Enterprise Resource Group Setup

LOCATION="northeurope"
APPS=("webshop" "internal-tools" "sandbox")
ENVS=("dev" "test" "prod")

# Criticality mapping
declare -A CRIT
CRIT[webshop]="high"
CRIT[internal-tools]="medium"
CRIT[sandbox]="low"

for APP in "${APPS[@]}"; do
  for ENV in "${ENVS[@]}"; do
    RG_NAME="rg-${APP}-${ENV}"
    CC="CC-${APP^^}"  # Uppercase

    echo "Creating ${RG_NAME}..."
    az group create \\
      --name "$RG_NAME" \\
      --location "$LOCATION" \\
      --tags environment="$ENV" \\
              owner="team-platform" \\
              cost-center="$CC" \\
              criticality="${CRIT[$APP]}" \\
              app="$APP"

    # Lock production
    if [ "$ENV" == "prod" ]; then
      echo "Adding delete lock to ${RG_NAME}..."
      az lock create \\
        --name "DoNotDelete" \\
        --resource-group "$RG_NAME" \\
        --lock-type CanNotDelete \\
        --notes "Production - requires approval to delete"
    fi
  done
done

echo "✅ Created 9 Resource Groups with tags and locks!"

# Verify
az group list --query "[?tags.owner=='team-platform'].{Name:name,Env:tags.environment,App:tags.app}" -o table""",
        "xp": 20
    },

    # ========================================================================
    # METADATA
    # ========================================================================
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 8,
        "practice": 10,
        "quiz": 5,
        "challenge": 10
    },
    "xp_per_section": {
        "intro": 10,
        "concepts": 15,
        "practice": 30,
        "quiz": 25,
        "challenge": 20
    },
    "total_xp": 100,
    "topics_covered": [
        "resource groups",
        "azure hierarchy",
        "tags",
        "resource locks",
        "naming conventions",
        "cost management",
        "azure cli"
    ]
}
