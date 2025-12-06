# ============================================================================
# AZURE BLOCK 2 - NODE 7: AZURE FUNCTIONS (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_7_V2 = {
    "node_id": 7,
    "title": "Azure Functions",
    "slug": "azure-functions",
    "description": "Serverless compute - betala bara när koden körs",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Kod utan servrar",
        "hook": "Med Azure Functions betalar du per exekvering, inte per timme. Perfekt för event-driven arkitektur.",
        "learning_objectives": [
            "Förstå serverless-konceptet och när det passar",
            "Skapa och deploya Azure Functions",
            "Konfigurera olika triggers (HTTP, Timer, Queue, etc.)",
            "Förstå bindings för input/output",
            "Optimera cold start och kostnader"
        ],
        "prerequisites": [
            "Grundläggande programmering (JavaScript/Python/C#)",
            "Azure CLI konfigurerat",
            "Förståelse för App Service (rekommenderat)"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "serverless-concept",
            "title": "Serverless Förklarat",
            "explanation": """Serverless betyder inte 'inga servrar' - det betyder att DU inte hanterar dem.

**Traditionell vs Serverless:**
| Aspekt | VM/App Service | Azure Functions |
|--------|---------------|-----------------|
| Kostnad | Per timme | Per exekvering |
| Skalning | Manuell/Auto | Automatisk, instant |
| Management | OS, runtime | Bara koden |
| Cold start | Ingen | 1-10 sekunder |
| Max runtime | Obegränsad | 5-10 min default |

**När passar Functions?**
✅ Event-driven (webhooks, queues)
✅ Sporadisk trafik
✅ Microservices
✅ Scheduled tasks (cron)
✅ API endpoints

**När passar INTE Functions?**
❌ Long-running jobs (>10 min)
❌ Konstant hög trafik (billigare med App Service)
❌ Stateful applications
❌ Real-time WebSocket

**Hosting Plans:**
| Plan | Cold Start | Max Runtime | Pris |
|------|------------|-------------|------|
| Consumption | Ja | 5-10 min | Per exekvering |
| Premium | Nej | Obegränsad | Per sekund |
| Dedicated | Nej | Obegränsad | Som App Service |""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│            SERVERLESS VS TRADITIONAL            │
├─────────────────────────────────────────────────┤
│                                                 │
│   TRADITIONAL (VM/App Service)                  │
│   ┌─────────────────────────────────────────┐   │
│   │  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  │   │
│   │  ↑ Betalar hela tiden                   │   │
│   │  |____________________________________  │   │
│   │  0:00        12:00         24:00       │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   SERVERLESS (Azure Functions)                  │
│   ┌─────────────────────────────────────────┐   │
│   │           $    $$   $      $$    $      │   │
│   │  ↑        │    ││   │      ││    │      │   │
│   │  |________│____││___│______││____│____  │   │
│   │  0:00        12:00         24:00       │   │
│   │           ↑ Betalar bara vid exekvering │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   💰 Kan spara 90%+ för sporadisk trafik       │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Consumption Plan är nästan gratis för låg trafik. 1M exekveringar/månad = ~$0.20.",
            "common_mistake": "Att använda Functions för konstant hög trafik. Då blir App Service billigare."
        },
        {
            "id": "triggers-bindings",
            "title": "Triggers & Bindings",
            "explanation": """Functions aktiveras av triggers och kan ha bindings för I/O.

**Triggers (vad som startar funktionen):**
| Trigger | Användning | Exempel |
|---------|-----------|---------|
| HTTP | REST API | POST /api/users |
| Timer | Cron-jobb | Varje natt kl 02:00 |
| Queue | Meddelandekö | Service Bus, Storage Queue |
| Blob | Fil-upload | Ny bild → thumbnail |
| Cosmos DB | Databas-ändringar | Ny order → email |
| Event Grid | Events | Azure-events |

**Bindings (input/output utan kod):**
```javascript
// Utan binding - manuell kod
const { BlobServiceClient } = require('@azure/storage-blob');
const blob = await blobClient.downloadToBuffer();

// Med binding - automatiskt!
module.exports = async function (context, myBlob) {
    // myBlob är redan nedladdat
    context.log('Blob size:', myBlob.length);

    // Output binding - sparas automatiskt
    context.bindings.outputBlob = processedData;
};
```

**function.json exempel:**
```json
{
  "bindings": [
    {
      "type": "blobTrigger",
      "name": "myBlob",
      "path": "images/{name}",
      "direction": "in"
    },
    {
      "type": "blob",
      "name": "outputBlob",
      "path": "thumbnails/{name}",
      "direction": "out"
    }
  ]
}
```""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           TRIGGERS & BINDINGS                    │
├─────────────────────────────────────────────────┤
│                                                 │
│   TRIGGER (Input - startar funktionen)          │
│   ┌─────────────┐                              │
│   │ HTTP POST   │──┐                           │
│   │ Timer       │  │                           │
│   │ Queue msg   │  │   ┌─────────────────┐     │
│   │ Blob upload │──┼──▶│  YOUR FUNCTION  │     │
│   │ Cosmos DB   │  │   │                 │     │
│   │ Event Grid  │──┘   └────────┬────────┘     │
│   └─────────────┘               │              │
│                                 │              │
│   INPUT BINDINGS               │              │
│   ┌─────────────┐              │              │
│   │ Read Blob   │──────────────┤              │
│   │ Read Table  │              │              │
│   │ Read Cosmos │              │              │
│   └─────────────┘              │              │
│                                 │              │
│   OUTPUT BINDINGS              ▼              │
│                      ┌─────────────────┐       │
│                      │ Write Blob      │       │
│                      │ Send Email      │       │
│                      │ Queue Message   │       │
│                      │ HTTP Response   │       │
│                      └─────────────────┘       │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Bindings sparar MYCKET kod. Istället för att connecta till Blob Storage manuellt, lägg till binding i function.json.",
            "common_mistake": "Att inte använda bindings och skriva egen connection-kod. Bindings hanterar retry, connection pooling etc."
        },
        {
            "id": "cold-start",
            "title": "Cold Start & Optimering",
            "explanation": """Cold start är den tid det tar att starta en function-instans.

**Vad orsakar cold start?**
1. Function App har inga aktiva instanser
2. Azure måste allokera resurser
3. Runtime startar (Node.js, Python, etc.)
4. Din kod laddas

**Cold start tider:**
| Runtime | Consumption | Premium |
|---------|-------------|---------|
| .NET | 1-3 sek | <1 sek |
| Node.js | 2-5 sek | <1 sek |
| Python | 3-10 sek | <1 sek |
| Java | 5-15 sek | <1 sek |

**Minimera cold start:**

1. **Smaller packages:**
```bash
# Undvik onödiga dependencies
npm prune --production
```

2. **Keep warm (Premium/Dedicated):**
```json
// host.json
{
  "functionTimeout": "00:10:00",
  "extensions": {
    "http": {
      "routePrefix": "api"
    }
  }
}
```

3. **Premium Plan:**
- Pre-warmed instances (alltid 1 redo)
- VNET integration
- Ingen cold start

4. **Dedicated Plan:**
- Samma som App Service
- Kör alltid
- Ingen cold start""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│              COLD START TIMELINE                │
├─────────────────────────────────────────────────┤
│                                                 │
│   Request arrives at cold function:             │
│   ─────────────────────────────────────────────│
│   │                                            │
│   ├─ 0ms    Request received                   │
│   │         (Function App sleeping 💤)         │
│   │                                            │
│   ├─ 500ms  Allocate resources                 │
│   │                                            │
│   ├─ 1500ms Start runtime (Node.js)            │
│   │                                            │
│   ├─ 2500ms Load your code                     │
│   │                                            │
│   ├─ 3000ms Execute function                   │
│   │                                            │
│   └─ 3100ms Return response                    │
│                                                 │
│   TOTAL: ~3 seconds (cold start)               │
│   vs ~100ms (warm)                             │
│                                                 │
│   SOLUTIONS:                                    │
│   • Premium Plan: Pre-warmed instances         │
│   • Timer trigger: Keep-alive every 5 min      │
│   • Smaller dependencies                       │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "För API:er med SLA-krav, använd Premium Plan. Cold start på 5-10 sek är inte acceptabelt för användare.",
            "common_mistake": "Att välja Consumption Plan för produktions-API:er och sedan bli överraskad av cold start."
        },
        {
            "id": "durable-functions",
            "title": "Durable Functions",
            "explanation": """Durable Functions löser begränsningar med vanliga Functions.

**Vanliga Functions-begränsningar:**
- Max 10 min exekveringstid
- Stateless
- Svårt att orkestrera flera steg

**Durable Functions-patterns:**

**1. Function Chaining:**
```
F1 → F2 → F3 → F4
```
Kör funktioner i sekvens, behåll state.

**2. Fan-out/Fan-in:**
```
     ┌─ F1 ─┐
Start┼─ F2 ─┼─ Aggregate
     └─ F3 ─┘
```
Parallell exekvering, samla resultat.

**3. Async HTTP API:**
```
POST → Start → 202 Accepted
       ↓
       Processing...
       ↓
GET /status → 200 Done
```
Long-running job med polling.

**4. Monitor:**
```
Loop: Check condition → Wait → Check → ...
```
Polling med intelligent backoff.

**Exempel:**
```javascript
// Orchestrator
const df = require('durable-functions');

module.exports = df.orchestrator(function* (context) {
    // Sequential execution
    const x = yield context.df.callActivity('Step1', input);
    const y = yield context.df.callActivity('Step2', x);
    const z = yield context.df.callActivity('Step3', y);

    // Or parallel execution
    const tasks = [];
    for (const item of items) {
        tasks.push(context.df.callActivity('ProcessItem', item));
    }
    const results = yield context.df.Task.all(tasks);

    return results;
});
```""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│          DURABLE FUNCTIONS PATTERNS             │
├─────────────────────────────────────────────────┤
│                                                 │
│   FUNCTION CHAINING                             │
│   ┌────┐   ┌────┐   ┌────┐   ┌────┐            │
│   │ F1 │──▶│ F2 │──▶│ F3 │──▶│ F4 │            │
│   └────┘   └────┘   └────┘   └────┘            │
│                                                 │
│   FAN-OUT / FAN-IN                              │
│              ┌────┐                             │
│   ┌────┐  ┌─▶│ F2 │─┐  ┌────┐                  │
│   │ F1 │──┼─▶│ F3 │─┼─▶│ F5 │                  │
│   └────┘  └─▶│ F4 │─┘  └────┘                  │
│              └────┘                             │
│                                                 │
│   ASYNC HTTP API                                │
│   ┌──────┐   ┌──────────┐   ┌──────┐           │
│   │Client│──▶│ Start job│──▶│ 202  │           │
│   │      │   └──────────┘   │Accept│           │
│   │      │                  └──────┘           │
│   │      │   ┌──────────┐   ┌──────┐           │
│   │      │──▶│GET status│──▶│ 200  │           │
│   │      │   └──────────┘   │ Done │           │
│   └──────┘                  └──────┘           │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Durable Functions sparar state automatiskt i Azure Storage. Perfekt för långkörande workflows som kan ta timmar/dagar.",
            "common_mistake": "Att försöka implementera orkestreringslogik i vanliga Functions. Durable Functions hanterar retry, checkpoints etc."
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du skapa Azure Functions med olika triggers.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa Function App",
                "instruction": "Skapa en Function App med Consumption Plan (Node.js).",
                "hint": "Använd 'az functionapp create' med --consumption-plan-location",
                "expected_command": "az functionapp create --name func-demo-12345 --resource-group rg-demo --consumption-plan-location northeurope --runtime node --runtime-version 18 --storage-account stfuncdemo12345 --functions-version 4",
                "expected_output": """{
  "defaultHostName": "func-demo-12345.azurewebsites.net",
  "name": "func-demo-12345",
  "state": "Running",
  "kind": "functionapp,linux"
}""",
                "explanation": "Consumption Plan = betala per exekvering. Storage account krävs för att spara function-state.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Initiera Lokalt Projekt",
                "instruction": "Initiera ett nytt Functions-projekt lokalt med JavaScript.",
                "hint": "Använd 'func init' kommandot",
                "expected_command": "func init my-functions --worker-runtime node --language javascript",
                "expected_output": """Writing .gitignore
Writing host.json
Writing local.settings.json
Writing package.json""",
                "explanation": "func CLI skapar projektstruktur med nödvändiga config-filer.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Skapa HTTP-trigger Function",
                "instruction": "Skapa en function med HTTP-trigger.",
                "hint": "Använd 'func new' med --template",
                "expected_command": "cd my-functions && func new --name HttpExample --template \"HTTP trigger\"",
                "expected_output": """Select a language: javascript
Select a template: HTTP trigger
Function name: [HttpExample]

The function "HttpExample" was created successfully.""",
                "explanation": "HTTP trigger är vanligast - skapar en REST API endpoint.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Testa Lokalt",
                "instruction": "Starta functions lokalt för testing.",
                "hint": "Använd 'func start' kommandot",
                "expected_command": "func start",
                "expected_output": """Azure Functions Core Tools
Core Tools Version:       4.x
Function Runtime Version: 4.x

Functions:
    HttpExample: [GET,POST] http://localhost:7071/api/HttpExample

For detailed output, run func with --verbose flag.""",
                "explanation": "func start kör dina functions lokalt. Perfekt för utveckling och debugging.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Deploya till Azure",
                "instruction": "Publicera dina functions till Azure.",
                "hint": "Använd 'func azure functionapp publish'",
                "expected_command": "func azure functionapp publish func-demo-12345",
                "expected_output": """Getting site publishing info...
Uploading package...
Upload completed successfully.

Functions in func-demo-12345:
    HttpExample - [httpTrigger]
        Invoke url: https://func-demo-12345.azurewebsites.net/api/httpexample""",
                "explanation": "Nu är din function live! URL:en fungerar direkt.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Visa Function Logs",
                "instruction": "Streama logs från din function i realtid.",
                "hint": "Använd 'az functionapp logs'",
                "expected_command": "az webapp log tail --name func-demo-12345 --resource-group rg-demo",
                "expected_output": """2024-12-06T10:23:45 Connected to log stream
2024-12-06T10:23:51 Executing 'HttpExample' (Reason='HTTP trigger')
2024-12-06T10:23:51 Function completed (Success, Duration=52ms)""",
                "explanation": "Log streaming hjälper vid debugging. Ctrl+C för att avsluta.",
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
                "front": "Vad är cold start i Azure Functions?",
                "back": "Fördröjning (1-10 sek) när en function startar från inaktivt läge. Orsakas av att Azure måste allokera resurser och ladda runtime."
            },
            {
                "id": "fc2",
                "front": "Vilka hosting plans finns för Azure Functions?",
                "back": "1) Consumption (betala per exekvering), 2) Premium (pre-warmed), 3) Dedicated (som App Service)"
            },
            {
                "id": "fc3",
                "front": "Vad är en binding i Azure Functions?",
                "back": "Deklarativ koppling till externa resurser (Blob, Queue, Cosmos DB) utan att skriva connection-kod."
            },
            {
                "id": "fc4",
                "front": "När ska du använda Durable Functions?",
                "back": "För workflows som är längre än 10 min, behöver state, eller kräver orkestering av flera steg."
            },
            {
                "id": "fc5",
                "front": "Hur minimerar du cold start?",
                "back": "1) Premium Plan, 2) Smaller package size, 3) Keep-alive timer trigger, 4) Faster runtime (.NET)"
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Din API har strikt SLA på max 500ms svarstid. Vilken hosting plan väljer du?",
                "options": [
                    "Consumption Plan (billigast)",
                    "Premium Plan (pre-warmed instances)",
                    "Dedicated Plan (App Service)",
                    "Spelar ingen roll"
                ],
                "correct_answer": 1,
                "explanation": "Premium Plan har pre-warmed instances = ingen cold start. Consumption kan ha 5-10 sek cold start."
            },
            {
                "id": "mc2",
                "question": "Du behöver köra ett jobb varje natt kl 02:00. Vilken trigger använder du?",
                "options": [
                    "HTTP trigger",
                    "Timer trigger",
                    "Queue trigger",
                    "Blob trigger"
                ],
                "correct_answer": 1,
                "explanation": "Timer trigger kör på schema (cron). Perfekt för nattliga batch-jobb, cleanup etc."
            },
            {
                "id": "mc3",
                "question": "Din function tar ~30 minuter att köra. Vad behöver du?",
                "options": [
                    "Vanlig HTTP-trigger function",
                    "Timer trigger med längre timeout",
                    "Durable Functions",
                    "Byt till App Service"
                ],
                "correct_answer": 2,
                "explanation": "Vanliga Functions har 5-10 min timeout. Durable Functions kan köra timmar/dagar med checkpoints."
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Image Processing Pipeline",
        "scenario": """Du ska bygga en bildbehandlings-pipeline:
1. Användare laddar upp bild via HTTP
2. Bilden sparas i Blob Storage
3. En function triggas automatiskt
4. Thumbnails genereras i olika storlekar
5. Metadata sparas i Cosmos DB
6. Email skickas till admin""",
        "requirements": [
            "HTTP-trigger för upload (returnerar upload URL)",
            "Blob-trigger för bildbehandling",
            "Output bindings till Blob (thumbnails) och Cosmos DB (metadata)",
            "SendGrid binding för email-notifiering",
            "Hantera fel gracefully med retry"
        ],
        "hints": [
            "Använd SAS-token för säker blob upload",
            "sharp-paketet för Node.js bildbehandling",
            "Cosmos DB output binding sparar automatiskt"
        ],
        "solution": """// ═══════════════════════════════════════════════════════════════
// function.json - Blob Trigger with bindings
// ═══════════════════════════════════════════════════════════════

{
  "bindings": [
    {
      "name": "inputBlob",
      "type": "blobTrigger",
      "direction": "in",
      "path": "uploads/{name}",
      "connection": "AzureStorageConnection"
    },
    {
      "name": "thumbnailSmall",
      "type": "blob",
      "direction": "out",
      "path": "thumbnails/small-{name}",
      "connection": "AzureStorageConnection"
    },
    {
      "name": "thumbnailMedium",
      "type": "blob",
      "direction": "out",
      "path": "thumbnails/medium-{name}",
      "connection": "AzureStorageConnection"
    },
    {
      "name": "metadata",
      "type": "cosmosDB",
      "direction": "out",
      "databaseName": "ImageDB",
      "containerName": "metadata",
      "connection": "CosmosDBConnection",
      "createIfNotExists": true
    },
    {
      "name": "email",
      "type": "sendGrid",
      "direction": "out",
      "apiKey": "SendGridApiKey",
      "from": "noreply@myapp.com"
    }
  ]
}

// ═══════════════════════════════════════════════════════════════
// index.js - Image Processing Function
// ═══════════════════════════════════════════════════════════════

const sharp = require('sharp');

module.exports = async function (context, inputBlob) {
    const imageName = context.bindingData.name;

    context.log(`Processing image: ${imageName}`);
    context.log(`Size: ${inputBlob.length} bytes`);

    try {
        // Generate thumbnails
        const [smallThumb, mediumThumb, imageMetadata] = await Promise.all([
            sharp(inputBlob)
                .resize(100, 100, { fit: 'cover' })
                .jpeg({ quality: 80 })
                .toBuffer(),
            sharp(inputBlob)
                .resize(300, 300, { fit: 'cover' })
                .jpeg({ quality: 85 })
                .toBuffer(),
            sharp(inputBlob).metadata()
        ]);

        // Output bindings - automatically saved
        context.bindings.thumbnailSmall = smallThumb;
        context.bindings.thumbnailMedium = mediumThumb;

        // Save metadata to Cosmos DB
        context.bindings.metadata = {
            id: `img-${Date.now()}`,
            originalName: imageName,
            originalSize: inputBlob.length,
            dimensions: {
                width: imageMetadata.width,
                height: imageMetadata.height
            },
            format: imageMetadata.format,
            thumbnails: {
                small: `thumbnails/small-${imageName}`,
                medium: `thumbnails/medium-${imageName}`
            },
            processedAt: new Date().toISOString(),
            status: 'completed'
        };

        // Send notification email
        context.bindings.email = {
            to: 'admin@company.com',
            subject: `Image Processed: ${imageName}`,
            content: [{
                type: 'text/html',
                value: `
                    <h2>Image Processing Complete</h2>
                    <p><strong>File:</strong> ${imageName}</p>
                    <p><strong>Size:</strong> ${(inputBlob.length / 1024).toFixed(2)} KB</p>
                    <p><strong>Dimensions:</strong> ${imageMetadata.width}x${imageMetadata.height}</p>
                    <p><strong>Thumbnails created:</strong> 100x100, 300x300</p>
                `
            }]
        };

        context.log(`Successfully processed ${imageName}`);

    } catch (error) {
        context.log.error(`Error processing image: ${error.message}`);

        // Save error to Cosmos DB for monitoring
        context.bindings.metadata = {
            id: `err-${Date.now()}`,
            originalName: imageName,
            status: 'failed',
            error: error.message,
            processedAt: new Date().toISOString()
        };

        // Alert on failure
        context.bindings.email = {
            to: 'admin@company.com',
            subject: `⚠️ Image Processing Failed: ${imageName}`,
            content: [{
                type: 'text/html',
                value: `
                    <h2>Image Processing Failed</h2>
                    <p><strong>File:</strong> ${imageName}</p>
                    <p><strong>Error:</strong> ${error.message}</p>
                `
            }]
        };

        throw error; // Re-throw for retry policy
    }
};


// ═══════════════════════════════════════════════════════════════
// HTTP Trigger - Get Upload URL (SAS token)
// ═══════════════════════════════════════════════════════════════

// getUploadUrl/index.js
const { BlobServiceClient, generateBlobSASQueryParameters, BlobSASPermissions } = require('@azure/storage-blob');

module.exports = async function (context, req) {
    const fileName = req.query.filename || `image-${Date.now()}.jpg`;

    const blobServiceClient = BlobServiceClient.fromConnectionString(
        process.env.AzureStorageConnection
    );

    const containerClient = blobServiceClient.getContainerClient('uploads');
    const blobClient = containerClient.getBlobClient(fileName);

    // Generate SAS token valid for 5 minutes
    const sasToken = generateBlobSASQueryParameters({
        containerName: 'uploads',
        blobName: fileName,
        permissions: BlobSASPermissions.parse('cw'), // create, write
        expiresOn: new Date(Date.now() + 5 * 60 * 1000)
    }, blobServiceClient.credential).toString();

    const uploadUrl = `${blobClient.url}?${sasToken}`;

    context.res = {
        body: {
            uploadUrl,
            fileName,
            expiresIn: '5 minutes',
            instructions: 'PUT your file to uploadUrl with Content-Type header'
        }
    };
};


// ═══════════════════════════════════════════════════════════════
// host.json - Configuration
// ═══════════════════════════════════════════════════════════════

{
  "version": "2.0",
  "functionTimeout": "00:10:00",
  "extensions": {
    "blobs": {
      "maxDegreeOfParallelism": 4
    },
    "cosmosDB": {
      "connectionMode": "Direct"
    }
  },
  "retry": {
    "strategy": "exponentialBackoff",
    "maxRetryCount": 3,
    "minimumInterval": "00:00:05",
    "maximumInterval": "00:00:30"
  }
}
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
        "azure functions",
        "serverless",
        "triggers",
        "bindings",
        "cold start",
        "durable functions",
        "event-driven"
    ]
}
