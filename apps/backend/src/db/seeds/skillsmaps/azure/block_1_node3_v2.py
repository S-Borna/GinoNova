# ============================================================================
# AZURE BLOCK 1 - NODE 3: AZURE PORTAL & CLI (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_3_V2 = {
    "node_id": 3,
    "title": "Azure Portal & CLI",
    "slug": "azure-portal-cli",
    "description": "Navigera Azure Portal och automatisera med CLI",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Portal för utforskning, CLI för automation",
        "hook": "Azure Portal är din karta. Azure CLI är din turboknapp. Lär dig båda.",
        "learning_objectives": [
            "Navigera Azure Portal effektivt",
            "Installera och konfigurera Azure CLI",
            "Använda az-kommandon för resurshantering",
            "Filtrera output med JMESPath queries",
            "Utnyttja Cloud Shell när CLI inte finns lokalt"
        ],
        "prerequisites": [
            "Azure-konto med aktiv subscription",
            "Terminal/kommandotolk",
            "Grundläggande bash-kunskap"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "portal-navigation",
            "title": "Azure Portal Navigering",
            "explanation": """Azure Portal (portal.azure.com) är det grafiska gränssnittet för Azure.

**Huvuddelar:**
- **Dashboard** - Anpassningsbar startsida
- **All Resources** - Sök alla resurser
- **Resource Groups** - Organiserade containers
- **Subscriptions** - Fakturering och kvoter
- **Cost Management** - Spåra utgifter
- **Azure Active Directory** - Identitetshantering

**Power Features:**
- 🔍 **Global Search (G+/)** - Sök vad som helst
- ⭐ **Favorites** - Snabbåtkomst till vanliga tjänster
- 📌 **Pin to Dashboard** - Fäst resurser för överblick
- 🔔 **Notifications** - Deployment-status

**Keyboard Shortcuts:**
| Shortcut | Action |
|----------|--------|
| `G + /` | Global search |
| `G + N` | Create resource |
| `G + D` | Go to Dashboard |
| `G + R` | Go to Resource Groups |""",
            "diagram": """
+-------------------------------------------------+
|               AZURE PORTAL LAYOUT               |
+-------------------------------------------------+
|  +------+ +---------------------------------+   |
|  | ☰    | | 🔍 Search resources, services   |   |
|  | Home | +---------------------------------+   |
|  | Dash |                                       |
|  | All  |  +---------------------------------+  |
|  | RGs  |  |      DASHBOARD / CONTENT        |  |
|  | Subs |  |                                 |  |
|  | Cost |  |  +-----+ +-----+ +-----+       |  |
|  | ...  |  |  | VM  | | DB  | | App |       |  |
|  |      |  |  |Tile | |Tile | |Tile |       |  |
|  | ⭐    |  |  +-----+ +-----+ +-----+       |  |
|  |Favs  |  |                                 |  |
|  +------+  +---------------------------------+  |
|               🔔 Notifications    👤 Profile    |
+-------------------------------------------------+
""",
            "pro_tip": "Använd 'G + /' för global search - snabbare än att klicka igenom menyer.",
            "common_mistake": "Att försöka göra allt i Portal. Det fungerar för utforskning, men repetitiva uppgifter = CLI."
        },
        {
            "id": "cli-installation",
            "title": "Azure CLI Installation",
            "explanation": """Azure CLI är kommandoradsverktyget för Azure. Finns för alla OS.

**Installation per OS:**

**macOS:**
```bash
brew install azure-cli
```

**Ubuntu/Debian:**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Windows:**
```powershell
winget install Microsoft.AzureCLI
```

**Docker (ingen installation):**
```bash
docker run -it mcr.microsoft.com/azure-cli
```

**Verifiera:**
```bash
az --version
# azure-cli 2.x.x
```

**Logga in:**
```bash
az login
# Öppnar webbläsare för autentisering
```""",
            "diagram": """
+-------------------------------------------------+
|           AZURE CLI INSTALLATION                |
+-------------------------------------------------+
|                                                 |
|   macOS     ->  brew install azure-cli          |
|   Ubuntu    ->  curl script | sudo bash         |
|   Windows   ->  winget install                  |
|   Docker    ->  docker run -it az-cli           |
|                                                 |
|   +-----------------------------------------+   |
|   |  $ az --version                         |   |
|   |  azure-cli    2.55.0                    |   |
|   |  core         2.55.0                    |   |
|   |  telemetry    1.1.0                     |   |
|   |                                         |   |
|   |  $ az login                             |   |
|   |  Opening browser for authentication...  |   |
|   |  ✓ Logged in as user@company.com        |   |
|   +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Docker-versionen om du inte vill installera något permanent eller jobbar på en delad maskin.",
            "common_mistake": "Att köra 'az login' på en server utan webbläsare. Använd 'az login --use-device-code' istället."
        },
        {
            "id": "cli-basics",
            "title": "Azure CLI Syntax",
            "explanation": """Azure CLI följer en konsekvent struktur:

**Grundstruktur:**
```
az <group> <subgroup> <action> --<parameter> <value>
```

**Exempel:**
```bash
az vm create --name myvm --resource-group myrg
|   |  |       |           |
|   |  |       |           +-- Parameter med värde
|   |  |       +-- Parameter med värde
|   |  +-- Action (create, list, show, delete)
|   +-- Resource type (vm, storage, network)
+-- Azure CLI

# Jämför med AWS CLI:
# aws ec2 run-instances --instance-type t2.micro
# az vm create --size Standard_B1s
```

**Vanliga actions:**
| Action | Beskrivning |
|--------|-------------|
| `create` | Skapa ny resurs |
| `list` | Lista alla |
| `show` | Visa en specifik |
| `update` | Modifiera |
| `delete` | Radera |

**Hjälpsystemet:**
```bash
az --help                    # Alla commands
az vm --help                 # VM-specifika
az vm create --help          # Specifikt command
az find "create vm"          # Sök efter command
az interactive               # Interaktivt läge!
```""",
            "diagram": """
+-------------------------------------------------+
|              CLI COMMAND STRUCTURE              |
+-------------------------------------------------+
|                                                 |
|   az   group   create   --name rg   --loc neu  |
|   |      |       |         |           |        |
|   |      |       |         |           +-- Value|
|   |      |       |         +-- Parameter        |
|   |      |       +-- Action                     |
|   |      +-- Resource type                      |
|   +-- CLI prefix                                |
|                                                 |
|   COMMON PATTERNS:                              |
|   +-----------------------------------------+   |
|   |  az <type> list                         |   |
|   |  az <type> show --name X --resource-group Y |
|   |  az <type> create --name X [options]    |   |
|   |  az <type> delete --name X --yes        |   |
|   +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd 'az interactive' för auto-complete och inline dokumentation. Perfekt när du lär dig.",
            "common_mistake": "Att inte använda --yes på delete-kommandon i scripts. Scriptet hänger sig och väntar på bekräftelse."
        },
        {
            "id": "output-jmespath",
            "title": "Output Formats & JMESPath",
            "explanation": """Azure CLI kan returnera data i olika format. JMESPath låter dig filtrera.

**Output Formats:**
```bash
az vm list --output json      # Default, full data
az vm list --output table     # Human-readable
az vm list --output yaml      # YAML format
az vm list --output tsv       # Tab-separated (scripting)
az vm list --output jsonc     # Colorized JSON
```

**JMESPath Queries:**
```bash
# Välj specifika fält
az vm list --query "[].name"
# ["vm-1", "vm-2"]

# Flera fält
az vm list --query "[].{Name:name, Size:hardwareProfile.vmSize}"

# Filtrera
az vm list --query "[?location=='northeurope'].name"

# Första elementet
az vm list --query "[0].name"

# Spara till variabel
VM_IP=$(az vm show -g myRG -n myVM --query publicIps -o tsv)
```

**Vanliga patterns:**
| Query | Resultat |
|-------|----------|
| `[].name` | Alla namn som array |
| `[0]` | Första elementet |
| `[?tag=='x']` | Filtrera |
| `{N:name,L:location}` | Välj och rename |""",
            "diagram": """
+-------------------------------------------------+
|              OUTPUT FORMATS                      |
+-------------------------------------------------+
|                                                 |
|  --output json (default)                        |
|  +-----------------------------------------+   |
|  | [{"name":"vm-1","location":"northeu"}, |   |
|  |  {"name":"vm-2","location":"westeu"}]  |   |
|  +-----------------------------------------+   |
|                                                 |
|  --output table                                 |
|  +-----------------------------------------+   |
|  | Name    Location                        |   |
|  | ------  -----------                     |   |
|  | vm-1    northeurope                     |   |
|  | vm-2    westeurope                      |   |
|  +-----------------------------------------+   |
|                                                 |
|  --query "[].name" --output tsv                 |
|  +-----------------------------------------+   |
|  | vm-1                                    |   |
|  | vm-2                                    |   |
|  +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd 'tsv' output när du sparar till variabler: VM=$(az vm show ... -o tsv). Ingen parsing behövs.",
            "common_mistake": "Att använda json output och sedan grep/sed för att extrahera data. JMESPath är mycket säkrare."
        },
        {
            "id": "cloud-shell",
            "title": "Azure Cloud Shell",
            "explanation": """Cloud Shell är en browser-baserad terminal med Azure CLI förinstallerat.

**Öppna:**
- Gå till shell.azure.com
- Eller klicka på >_ ikonen i Azure Portal

**Fördelar:**
- ✅ Ingen installation krävs
- ✅ Alltid senaste versionen
- ✅ Persistent storage (5GB Azure Files)
- ✅ Förinstallerat: az, kubectl, terraform, ansible, git
- ✅ Fungerar på vilken dator som helst

**Nackdelar:**
- ❌ Kräver internet
- ❌ 20-min timeout vid inaktivitet
- ❌ Kan vara lite långsammare

**Välja shell:**
- **Bash** - Linux/macOS-vana användare
- **PowerShell** - Windows/Azure PowerShell

**Tips:**
```bash
# Ladda upp filer
# Klicka på Upload/Download-ikonen

# Kör editor
code myfile.sh    # VS Code i browsern!

# Din persistent storage
cd ~/clouddrive
ls
```""",
            "diagram": """
+-------------------------------------------------+
|              AZURE CLOUD SHELL                  |
+-------------------------------------------------+
|                                                 |
|   +-----------------------------------------+   |
|   |  🌐 shell.azure.com                     |   |
|   |                                         |   |
|   |  Bash ○  PowerShell ●                  |   |
|   |                                         |   |
|   |  user@Azure:~$ az account show          |   |
|   |  {                                      |   |
|   |    "name": "My Subscription",           |   |
|   |    "state": "Enabled"                   |   |
|   |  }                                      |   |
|   |                                         |   |
|   |  user@Azure:~$ kubectl get nodes        |   |
|   |  NAME        STATUS   ROLES             |   |
|   |  aks-node1   Ready    agent             |   |
|   |                                         |   |
|   |  [Upload] [Download] [Settings] [⚙️]    |   |
|   +-----------------------------------------+   |
|                                                 |
|   INCLUDED TOOLS:                               |
|   az, kubectl, terraform, ansible, git,         |
|   python, node, docker, helm, vault...          |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Cloud Shell när du snabbt behöver köra az-kommandon från en dator utan CLI installerat.",
            "common_mistake": "Att förlita sig 100% på Cloud Shell. Timeout på 20 min kan avbryta långa operationer."
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du konfigurera Azure CLI och köra dina första kommandon.",
        "exercises": [
            {
                "step": 1,
                "title": "Verifiera CLI Installation",
                "instruction": "Kontrollera att Azure CLI är installerat och visa versionen.",
                "hint": "Använd 'az' med --version flaggan",
                "expected_command": "az --version",
                "expected_output": """azure-cli                         2.55.0
core                              2.55.0
telemetry                          1.1.0

Dependencies:
msal                            1.24.0b2
azure-mgmt-resource             23.1.0b2""",
                "explanation": "Azure CLI uppdateras ofta. Håll den uppdaterad för nya features och säkerhetsfixar.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Logga in i Azure",
                "instruction": "Autentisera mot Azure (öppnar webbläsare).",
                "hint": "Använd 'az login'",
                "expected_command": "az login",
                "expected_output": """Opening in existing browser session.
[
  {
    "cloudName": "AzureCloud",
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "isDefault": true,
    "name": "My Subscription",
    "state": "Enabled",
    "tenantId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
    "user": {
      "name": "user@company.com",
      "type": "user"
    }
  }
]""",
                "explanation": "az login öppnar webbläsaren för säker inloggning. Dina credentials sparas lokalt.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Visa Aktuell Subscription",
                "instruction": "Se vilken subscription som är aktiv just nu.",
                "hint": "Använd 'az account show'",
                "expected_command": "az account show --query \"{Name:name, ID:id, State:state}\" --output table",
                "expected_output": """Name               ID                                    State
-----------------  ------------------------------------  --------
My Subscription    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  Enabled""",
                "explanation": "Alltid viktigt att verifiera vilken subscription du jobbar mot innan du skapar resurser!",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Lista Resource Groups",
                "instruction": "Visa alla Resource Groups i din subscription.",
                "hint": "Använd 'az group list' med table output",
                "expected_command": "az group list --output table",
                "expected_output": """Name              Location      Status
----------------  ------------  ---------
rg-myapp-dev      northeurope   Succeeded
rg-myapp-prod     northeurope   Succeeded
NetworkWatcherRG  northeurope   Succeeded""",
                "explanation": "table output är bäst för snabb överblick. json output för scripting och automation.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Skapa en Storage Account",
                "instruction": "Skapa ett storage account i din dev Resource Group.",
                "hint": "Storage account namn måste vara globalt unikt, endast lowercase a-z och siffror",
                "expected_command": "az storage account create --name stdevdemo12345 --resource-group rg-myapp-dev --location northeurope --sku Standard_LRS",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-dev/providers/Microsoft.Storage/storageAccounts/stdevdemo12345",
  "kind": "StorageV2",
  "location": "northeurope",
  "name": "stdevdemo12345",
  "provisioningState": "Succeeded",
  "sku": {
    "name": "Standard_LRS",
    "tier": "Standard"
  }
}""",
                "explanation": "Storage account-namn måste vara 3-24 tecken, endast lowercase och siffror. Standard_LRS = billigast.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "JMESPath Query",
                "instruction": "Hitta alla storage accounts och visa bara namn och location.",
                "hint": "Använd --query med JMESPath syntax",
                "expected_command": "az storage account list --query \"[].{Name:name, Location:location}\" --output table",
                "expected_output": """Name             Location
---------------  ------------
stdevdemo12345   northeurope""",
                "explanation": "JMESPath låter dig extrahera exakt den data du behöver. Perfekt för scripting.",
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
                "front": "Hur öppnar du Cloud Shell?",
                "back": "shell.azure.com eller klicka på >_ ikonen i Azure Portal"
            },
            {
                "id": "fc2",
                "front": "Vilken output format är bäst för scripting och variabler?",
                "back": "tsv (tab-separated values) - ingen parsing behövs"
            },
            {
                "id": "fc3",
                "front": "Hur loggar du in på Azure CLI utan webbläsare?",
                "back": "az login --use-device-code"
            },
            {
                "id": "fc4",
                "front": "Vad är keyboard shortcut för global search i Portal?",
                "back": "G + /"
            },
            {
                "id": "fc5",
                "front": "Hur startar du Azure CLI:s interaktiva läge?",
                "back": "az interactive"
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du vill extrahera alla VM-namn från 'az vm list' output. Vilken JMESPath query använder du?",
                "options": [
                    "--query 'name'",
                    "--query '[].name'",
                    "--query 'names[]'",
                    "--query '{name}'"
                ],
                "correct_answer": 1,
                "explanation": "[].name itererar över alla objekt i arrayen och extraherar 'name' från varje."
            },
            {
                "id": "mc2",
                "question": "Vilken är fördelen med Cloud Shell jämfört med lokal CLI?",
                "options": [
                    "Snabbare exekvering",
                    "Ingen installation krävs, alltid senaste version",
                    "Kan köra offline",
                    "Obegränsad session-tid"
                ],
                "correct_answer": 1,
                "explanation": "Cloud Shell kräver ingen installation och har alltid senaste Azure CLI. Nackdelen är 20-min timeout."
            },
            {
                "id": "mc3",
                "question": "Du ska spara en VM:s IP-adress till en bash-variabel. Vilken output format bör du använda?",
                "options": [
                    "--output json",
                    "--output table",
                    "--output tsv",
                    "--output yaml"
                ],
                "correct_answer": 2,
                "explanation": "tsv ger ren text utan formatering, perfekt för: IP=$(az vm show ... -o tsv)"
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Automation Script: Resource Inventory",
        "scenario": """Din chef vill ha en daglig rapport över alla Azure-resurser.
Rapporten ska visa:
- Alla Resource Groups med antal resurser i varje
- Alla VMs med status (running/deallocated)
- Alla Storage Accounts med storlek
- Total uppskattad månadskostnad per RG (baserat på tags)""",
        "requirements": [
            "Skriv ett bash-script som genererar rapporten",
            "Använd JMESPath för att filtrera relevant data",
            "Output ska vara human-readable (table format)",
            "Spara rapporten till en fil med dagens datum",
            "Bonus: Skicka rapporten via email (Azure Logic App)"
        ],
        "hints": [
            "Använd 'az resource list --resource-group X' för resurser per RG",
            "VM power state: az vm get-instance-view --query instanceView.statuses[1].displayStatus",
            "Kombinera flera az-kommandon med variabler"
        ],
        "solution": """#!/bin/bash
# Azure Resource Inventory Report
# Run daily via cron or Azure Automation

REPORT_DATE=$(date +%Y-%m-%d)
REPORT_FILE="azure-inventory-${REPORT_DATE}.txt"

echo "========================================" > $REPORT_FILE
echo "   AZURE RESOURCE INVENTORY REPORT     " >> $REPORT_FILE
echo "   Generated: $(date)                  " >> $REPORT_FILE
echo "========================================" >> $REPORT_FILE

# Current subscription
echo "" >> $REPORT_FILE
echo "SUBSCRIPTION:" >> $REPORT_FILE
az account show --query "{Name:name, ID:id}" -o table >> $REPORT_FILE

# Resource Groups with resource count
echo "" >> $REPORT_FILE
echo "RESOURCE GROUPS:" >> $REPORT_FILE
echo "----------------" >> $REPORT_FILE
for RG in $(az group list --query "[].name" -o tsv); do
  COUNT=$(az resource list --resource-group $RG --query "length(@)")
  TAGS=$(az group show --name $RG --query "tags.environment" -o tsv 2>/dev/null || echo "no-tag")
  echo "$RG: $COUNT resources (env: $TAGS)" >> $REPORT_FILE
done

# Virtual Machines
echo "" >> $REPORT_FILE
echo "VIRTUAL MACHINES:" >> $REPORT_FILE
az vm list --query "[].{Name:name, RG:resourceGroup, Size:hardwareProfile.vmSize}" -o table >> $REPORT_FILE

# VM Power States
echo "" >> $REPORT_FILE
echo "VM POWER STATES:" >> $REPORT_FILE
for VM_INFO in $(az vm list --query "[].{name:name, rg:resourceGroup}" -o tsv); do
  VM_NAME=$(echo $VM_INFO | cut -f1)
  VM_RG=$(echo $VM_INFO | cut -f2)
  STATUS=$(az vm get-instance-view --name $VM_NAME --resource-group $VM_RG \\
    --query "instanceView.statuses[1].displayStatus" -o tsv 2>/dev/null || echo "Unknown")
  echo "$VM_NAME ($VM_RG): $STATUS" >> $REPORT_FILE
done

# Storage Accounts
echo "" >> $REPORT_FILE
echo "STORAGE ACCOUNTS:" >> $REPORT_FILE
az storage account list --query "[].{Name:name, Location:location, SKU:sku.name}" -o table >> $REPORT_FILE

# Summary
echo "" >> $REPORT_FILE
echo "========================================" >> $REPORT_FILE
TOTAL_RG=$(az group list --query "length(@)")
TOTAL_VM=$(az vm list --query "length(@)")
TOTAL_SA=$(az storage account list --query "length(@)")
echo "SUMMARY: $TOTAL_RG RGs, $TOTAL_VM VMs, $TOTAL_SA Storage Accounts" >> $REPORT_FILE
echo "========================================" >> $REPORT_FILE

echo "✅ Report saved to: $REPORT_FILE"
cat $REPORT_FILE""",
        "xp": 20
    },

    # ========================================================================
    # METADATA
    # ========================================================================
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 10,
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
        "azure portal",
        "azure cli",
        "az commands",
        "jmespath queries",
        "cloud shell",
        "output formats",
        "automation"
    ]
}
