# ============================================================================
# AZURE BLOCK 3 - NODE 9: BLOB STORAGE (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_9_V2 = {
    "node_id": 9,
    "title": "Azure Blob Storage",
    "slug": "azure-blob-storage",
    "description": "Objektlagring för ostrukturerad data i molnet",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "version": "2.0",

    "intro": {
        "headline": "Lagra vad som helst, hur mycket som helst",
        "hook": "Blob Storage är Azures S3 - oändlig lagring för bilder, videos, backups och big data.",
        "learning_objectives": [
            "Förstå Storage Account-hierarkin (Account -> Container -> Blob)",
            "Välja rätt access tier (Hot, Cool, Archive)",
            "Konfigurera access med SAS-tokens och policies",
            "Implementera lifecycle management för kostnadsoptimering",
            "Använda Azure CLI och SDKs för blob-operationer"
        ],
        "prerequisites": ["Azure CLI konfigurerat", "Grundläggande förståelse för objektlagring"],
        "xp": 10
    },

    "concepts": [
        {
            "id": "storage-hierarchy",
            "title": "Storage Account Hierarki",
            "explanation": """Azure Storage har en tydlig hierarki:

**Storage Account** (toppnivå)
- Globalt unikt namn (3-24 tecken, lowercase + siffror)
- Innehåller alla storage-tjänster
- Faktureras på denna nivå

**Container** (som en mapp)
- Grupperar relaterade blobs
- Access policy sätts här
- Obegränsat antal containers

**Blob** (själva filen)
- Max 190.7 TB per blob
- Tre typer: Block, Append, Page

**Blob-typer:**
| Typ | Användning | Max storlek |
|-----|-----------|-------------|
| Block Blob | Filer, media, backups | 190.7 TB |
| Append Blob | Loggar (append-only) | 195 GB |
| Page Blob | VM-diskar, random I/O | 8 TB |""",
            "diagram": """
+-------------------------------------------------+
|         STORAGE ACCOUNT HIERARCHY               |
+-------------------------------------------------+
|                                                 |
|   Storage Account: stproddata12345              |
|   +-- Container: images/                        |
|   |   +-- logo.png                             |
|   |   +-- banner.jpg                           |
|   |   +-- products/                            |
|   |       +-- product-1.png                    |
|   |       +-- product-2.png                    |
|   |                                             |
|   +-- Container: backups/                       |
|   |   +-- db-2024-12-01.sql.gz                 |
|   |   +-- db-2024-12-02.sql.gz                 |
|   |                                             |
|   +-- Container: logs/                          |
|       +-- app-2024-12-01.log                   |
|       +-- app-2024-12-02.log                   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd virtual directories med / i blob-namn. 'images/products/item.png' fungerar som mappar.",
            "common_mistake": "Att tro att containers är mappar. De är flat - 'mapp-strukturen' är bara blob-namnkonvention."
        },
        {
            "id": "access-tiers",
            "title": "Access Tiers & Kostnadsoptimering",
            "explanation": """Azure har tre access tiers med olika pris/prestanda.

**Hot Tier** (default)
- Högsta lagringskostnad
- Lägsta access-kostnad
- För data som används ofta

**Cool Tier**
- 50% lägre lagringskostnad
- Högre access-kostnad
- Min 30 dagars lagring
- För data som används sällan

**Archive Tier**
- 90% lägre lagringskostnad
- Rehydration tar timmar
- Min 180 dagars lagring
- För långtidsarkivering

**Kostnadsexempel (per GB/månad, North Europe):**
| Tier | Lagring | Read/10k | Write/10k |
|------|---------|----------|-----------|
| Hot | $0.021 | $0.004 | $0.05 |
| Cool | $0.01 | $0.01 | $0.10 |
| Archive | $0.002 | $5.00 | $0.10 |

**Rekommendation:**
- Aktiv data -> Hot
- >30 dagar utan access -> Cool
- >180 dagar -> Archive""",
            "diagram": """
+-------------------------------------------------+
|            ACCESS TIER COMPARISON               |
+-------------------------------------------------+
|                                                 |
|   STORAGE COST         ACCESS COST              |
|   (per GB/month)       (per operation)          |
|                                                 |
|   HOT      ########    #                        |
|            $0.021      Low                      |
|                                                 |
|   COOL     ####        ###                      |
|            $0.01       Medium                   |
|                                                 |
|   ARCHIVE  #           ################         |
|            $0.002      High + rehydration       |
|                                                 |
|   USE CASE:                                     |
|   HOT     -> Active data, frequent access        |
|   COOL    -> Backups, monthly reports            |
|   ARCHIVE -> Compliance, yearly archives         |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd Lifecycle Management för automatisk tier-övergång. Blob som inte accessas på 30 dagar -> Cool.",
            "common_mistake": "Att lagra allt på Hot tier. 80% av data accessas aldrig efter 30 dagar."
        },
        {
            "id": "access-control",
            "title": "Access Control & SAS Tokens",
            "explanation": """Det finns flera sätt att kontrollera access till blobs.

**1. Storage Account Keys**
- Full access till allt
- Två nycklar för rotation
- ALDRIG dela publikt!

**2. Shared Access Signature (SAS)**
- Tidsbegränsad access
- Specifika permissions
- Kan begränsas till container/blob
- Perfekt för externa användare

**3. Azure AD (Managed Identity)**
- Ingen nyckelhantering
- RBAC-roller
- Best practice för applikationer

**SAS Token-typer:**
| Typ | Scope | Användning |
|-----|-------|------------|
| Account SAS | Hela kontot | Admin-verktyg |
| Service SAS | En tjänst | App-integration |
| User delegation SAS | AD-baserad | Säkrast |

**SAS URL-format:**
```
https://myaccount.blob.core.windows.net/container/blob?
sv=2021-06-08           # API version
&st=2024-01-01T00:00:00Z  # Start time
&se=2024-12-31T23:59:59Z  # Expiry time
&sr=b                    # Resource (b=blob, c=container)
&sp=r                    # Permissions (r=read, w=write)
&sig=xxxxx              # Signature
```""",
            "diagram": """
+-------------------------------------------------+
|           ACCESS CONTROL METHODS                |
+-------------------------------------------------+
|                                                 |
|   METHOD              SECURITY    USE CASE      |
|   ---------------------------------------------|
|                                                 |
|   Storage Key         ⚠️ LOW      Admin only    |
|   [Full Access]       Never share publicly!    |
|                                                 |
|   SAS Token           ✅ MEDIUM   External users|
|   [Time-limited]      Upload links, downloads  |
|                                                 |
|   Azure AD + RBAC     ✅✅ HIGH   Applications  |
|   [Managed Identity]  No keys to manage!       |
|                                                 |
|   +-----------------------------------------+   |
|   | BEST PRACTICE:                          |   |
|   | • Apps: Managed Identity                |   |
|   | • External: User Delegation SAS         |   |
|   | • NEVER: Storage keys in code           |   |
|   +-----------------------------------------+   |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Använd User Delegation SAS med Azure AD - säkrare än Account SAS och kan revokeras.",
            "common_mistake": "Att hardcoda storage keys i kod. Använd Managed Identity eller Key Vault!"
        },
        {
            "id": "lifecycle-management",
            "title": "Lifecycle Management",
            "explanation": """Automatisera tier-övergångar och borttagning.

**Lifecycle Policy:**
```json
{
  "rules": [
    {
      "name": "move-to-cool",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["logs/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 30
            },
            "tierToArchive": {
              "daysAfterModificationGreaterThan": 90
            },
            "delete": {
              "daysAfterModificationGreaterThan": 365
            }
          }
        }
      }
    }
  ]
}
```

**Vanliga policies:**
| Scenario | Policy |
|----------|--------|
| Logs | Cool efter 30d, Archive 90d, Delete 365d |
| Backups | Cool efter 7d, Archive 30d, Delete 90d |
| User uploads | Cool efter 60d, Archive 180d |
| Compliance | Archive efter 1d, Keep 7 years |""",
            "diagram": """
+-------------------------------------------------+
|          LIFECYCLE MANAGEMENT FLOW              |
+-------------------------------------------------+
|                                                 |
|   Day 0          Day 30        Day 90    Day 365|
|   ---------------------------------------------|
|                                                 |
|   +-----+       +-----+      +-------+   🗑️    |
|   | HOT | ----▶ |COOL | ---▶ |ARCHIVE| -▶ DEL  |
|   +-----+       +-----+      +-------+         |
|   $0.021/GB     $0.01/GB     $0.002/GB         |
|                                                 |
|   AUTOMATIC TRANSITIONS:                        |
|   • No manual intervention needed              |
|   • Runs daily                                 |
|   • Can be filtered by prefix, tags, etc.      |
|                                                 |
|   SAVINGS EXAMPLE (1TB logs/month):             |
|   Without policy: $252/year (all Hot)          |
|   With policy:    $52/year                     |
|   SAVINGS:        $200/year (80%)              |
|                                                 |
+-------------------------------------------------+
""",
            "pro_tip": "Kombinera lifecycle med blob index tags. Tagga med 'retention=7years' och ha policy baserad på tag.",
            "common_mistake": "Att glömma lifecycle policies. Data ackumuleras och kostnaderna exploderar."
        }
    ],

    "practice": {
        "introduction": "Nu ska du sätta upp ett Storage Account med containers, access control och lifecycle policies.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa Storage Account",
                "instruction": "Skapa ett Storage Account med Standard_LRS.",
                "hint": "Namn måste vara globalt unikt, 3-24 tecken, lowercase + siffror",
                "expected_command": "az storage account create --name stdemoblob12345 --resource-group rg-demo --location northeurope --sku Standard_LRS --kind StorageV2",
                "expected_output": """{"name": "stdemoblob12345", "primaryEndpoints": {"blob": "https://stdemoblob12345.blob.core.windows.net/"}}""",
                "explanation": "Standard_LRS = lokalt redundant, billigast. StorageV2 har alla features.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Skapa Container",
                "instruction": "Skapa en container för images med private access.",
                "hint": "Använd 'az storage container create'",
                "expected_command": "az storage container create --name images --account-name stdemoblob12345 --public-access off",
                "expected_output": """{"created": true}""",
                "explanation": "public-access off = endast autentiserade requests. Säkrast för känslig data.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Ladda upp Blob",
                "instruction": "Ladda upp en fil till containern.",
                "hint": "Använd 'az storage blob upload'",
                "expected_command": "az storage blob upload --account-name stdemoblob12345 --container-name images --name logo.png --file ./logo.png --overwrite",
                "expected_output": """{"etag": "0x8DC...", "lastModified": "2024-12-06T10:30:00Z"}""",
                "explanation": "--overwrite tillåter att ersätta existerande blob. Utan det får du error om blob finns.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Generera SAS Token",
                "instruction": "Skapa en tidsbegränsad SAS URL för blob download.",
                "hint": "Använd 'az storage blob generate-sas'",
                "expected_command": "az storage blob generate-sas --account-name stdemoblob12345 --container-name images --name logo.png --permissions r --expiry 2024-12-07T00:00:00Z --https-only --full-uri",
                "expected_output": """https://stdemoblob12345.blob.core.windows.net/images/logo.png?sv=2021-06-08&se=2024-12-07T00%3A00%3A00Z&sr=b&sp=r&sig=xxx""",
                "explanation": "SAS URL är giltig till expiry. --permissions r = read only. Perfekt för att dela filer.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Ändra Access Tier",
                "instruction": "Flytta en blob till Cool tier för att spara pengar.",
                "hint": "Använd 'az storage blob set-tier'",
                "expected_command": "az storage blob set-tier --account-name stdemoblob12345 --container-name images --name logo.png --tier Cool",
                "expected_output": """(Success - no output)""",
                "explanation": "Tier-byte är gratis från Hot->Cool. Cool->Hot har en liten kostnad.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Lista Blobs",
                "instruction": "Visa alla blobs i containern med deras tier.",
                "hint": "Använd 'az storage blob list' med query",
                "expected_command": "az storage blob list --account-name stdemoblob12345 --container-name images --query \"[].{Name:name, Tier:properties.blobTier, Size:properties.contentLength}\" --output table",
                "expected_output": """Name      Tier    Size
--------  ------  ------
logo.png  Cool    12543""",
                "explanation": "Nu ser du att blob är på Cool tier. Kolumnerna visar namn, tier och storlek.",
                "xp": 5
            }
        ],
        "xp": 30
    },

    "quiz": {
        "passing_score": 80,
        "flashcards": [
            {"id": "fc1", "front": "Vilka tre access tiers finns för Blob Storage?", "back": "Hot (frequent access), Cool (infrequent, 30d min), Archive (rare, 180d min, rehydration needed)"},
            {"id": "fc2", "front": "Vad är skillnaden mellan Block Blob och Append Blob?", "back": "Block Blob: Generella filer, kan modifieras. Append Blob: Endast append, perfekt för loggar."},
            {"id": "fc3", "front": "Vad är ett SAS token?", "back": "Shared Access Signature - tidsbegränsad, permission-scopad URL för att ge access utan att dela account key."},
            {"id": "fc4", "front": "Hur lång tid tar det att rehydrate en blob från Archive?", "back": "Standard: upp till 15 timmar. High Priority: under 1 timme (kostar mer)."},
            {"id": "fc5", "front": "Vilken access metod är säkrast för applikationer?", "back": "Managed Identity med Azure AD RBAC - inga nycklar att hantera eller rotera."}
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du har 10TB loggar som accessas dagligen första veckan, sedan aldrig. Bästa strategi?",
                "options": ["Allt på Hot tier", "Lifecycle policy: Hot->Cool efter 7d->Archive efter 30d", "Direkt till Archive", "Radera efter 7 dagar"],
                "correct_answer": 1,
                "explanation": "Lifecycle policy automatiserar tier-övergångar baserat på access patterns. Sparar 80%+ på lagring."
            },
            {
                "id": "mc2",
                "question": "Du ska ge en extern partner tillfällig read-access till en fil. Vad använder du?",
                "options": ["Storage Account Key", "SAS Token med expiry", "Gör containern public", "Skapa Azure AD-användare"],
                "correct_answer": 1,
                "explanation": "SAS Token ger tidsbegränsad access utan att exponera account key eller göra data public."
            },
            {
                "id": "mc3",
                "question": "Vad händer om du försöker läsa en blob på Archive tier?",
                "options": ["Läsning fungerar direkt", "Du får 404 Not Found", "Du måste rehydrate först", "Automatisk rehydration"],
                "correct_answer": 2,
                "explanation": "Archive blobs måste rehydrates till Hot/Cool först. Det tar timmar och kostar per GB."
            }
        ],
        "xp": 25
    },

    "challenge": {
        "title": "Media Storage Backend",
        "scenario": "Bygg ett storage-backend för en media-app: användare laddar upp bilder, de processas, thumbnails genereras, och gamla filer arkiveras automatiskt.",
        "requirements": [
            "Storage Account med containers: uploads, processed, thumbnails, archive",
            "SAS-policy för säker upload utan att exponera keys",
            "Lifecycle policy: processed->Cool 30d, ->Archive 90d",
            "Event Grid trigger för blob-upload notifications",
            "Dokumentera kostnadsuppskattning"
        ],
        "hints": ["Använd User Delegation SAS", "Event Grid kan trigga Functions vid upload", "Blob index tags för metadata"],
        "solution": """#!/bin/bash
# Media Storage Backend Setup
# ═══════════════════════════════════════════════════════════════

RESOURCE_GROUP="rg-media-storage"
STORAGE_ACCOUNT="stmedia$(date +%s)"
LOCATION="northeurope"

# Create resources
az group create --name $RESOURCE_GROUP --location $LOCATION

az storage account create \\
    --name $STORAGE_ACCOUNT \\
    --resource-group $RESOURCE_GROUP \\
    --location $LOCATION \\
    --sku Standard_LRS \\
    --kind StorageV2 \\
    --access-tier Hot \\
    --allow-blob-public-access false

# Create containers
for CONTAINER in uploads processed thumbnails archive; do
    az storage container create --account-name $STORAGE_ACCOUNT --name $CONTAINER
done

# Lifecycle Policy
cat > lifecycle-policy.json << 'EOF'
{
  "rules": [
    {
      "name": "archive-old-processed",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": {"blobTypes": ["blockBlob"], "prefixMatch": ["processed/"]},
        "actions": {
          "baseBlob": {
            "tierToCool": {"daysAfterModificationGreaterThan": 30},
            "tierToArchive": {"daysAfterModificationGreaterThan": 90}
          }
        }
      }
    }
  ]
}
EOF

az storage account management-policy create \\
    --account-name $STORAGE_ACCOUNT \\
    --resource-group $RESOURCE_GROUP \\
    --policy @lifecycle-policy.json

echo "✅ Storage Account: $STORAGE_ACCOUNT"
echo "Cost estimate: ~$0.02/GB/month (Hot) + lifecycle savings"
""",
        "xp": 20
    },

    "estimated_time_per_section": {"intro": 2, "concepts": 10, "practice": 12, "quiz": 6, "challenge": 15},
    "xp_per_section": {"intro": 10, "concepts": 15, "practice": 30, "quiz": 25, "challenge": 20},
    "total_xp": 110,
    "topics_covered": ["blob storage", "access tiers", "sas tokens", "lifecycle management", "containers"]
}
