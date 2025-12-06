# ============================================================================
# AZURE BLOCK 2 - NODE 6: APP SERVICE (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_6_V2 = {
    "node_id": 6,
    "title": "Azure App Service",
    "slug": "azure-app-service",
    "description": "PaaS-hosting för web apps utan server-management",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Deploy utan att tänka på servrar",
        "hook": "App Service låter dig fokusera på kod istället för infrastruktur. Push code, Azure sköter resten.",
        "learning_objectives": [
            "Förstå skillnaden mellan App Service Plan och Web App",
            "Deploya applikationer med flera metoder (ZIP, Git, Containers)",
            "Konfigurera environment variables och secrets",
            "Implementera zero-downtime deployments med slots",
            "Sätta upp custom domain och SSL"
        ],
        "prerequisites": [
            "Azure CLI konfigurerat",
            "Grundläggande web-utveckling",
            "Git-kunskap"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "app-service-plan",
            "title": "App Service Plan vs Web App",
            "explanation": """App Service har två huvudkoncept:

**App Service Plan (infrastrukturen):**
- Definierar compute-resurser (CPU, RAM)
- Bestämmer pris och features
- Kan hostas av flera Web Apps

**Web App (din applikation):**
- Din faktiska kod/container
- Runtime (Node.js, Python, .NET, etc.)
- App settings, connection strings
- Custom domains, SSL

**Tiers:**
| Tier | Pris | Features | Användning |
|------|------|----------|------------|
| Free | $0 | 1GB, 60min CPU/dag | Prototyping |
| Shared | $10 | Custom domain | Dev/test |
| Basic B1 | $55 | Dedicated, SSL | Prod-light |
| Standard S1 | $73 | Slots, auto-scale | Production |
| Premium P1v2 | $81 | Bättre prestanda | High-traffic |

**En Plan, flera Apps:**
```
App Service Plan (S1)
├── Web App: api.mysite.com
├── Web App: www.mysite.com
└── Web App: admin.mysite.com
```
Alla delar samma resurser men kostar bara för planen!""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           APP SERVICE ARCHITECTURE              │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │         APP SERVICE PLAN (S1)           │   │
│   │     2 vCPU, 3.5GB RAM, $73/month        │   │
│   │                                         │   │
│   │   ┌──────────┐ ┌──────────┐ ┌────────┐ │   │
│   │   │ Web App  │ │ Web App  │ │Web App │ │   │
│   │   │   API    │ │ Frontend │ │ Admin  │ │   │
│   │   │ Node.js  │ │ React    │ │ Python │ │   │
│   │   └──────────┘ └──────────┘ └────────┘ │   │
│   │                                         │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   ✅ 3 apps, betalar bara för 1 plan!          │
│   ⚠️  Alla delar samma CPU/RAM                 │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Sätt flera små appar på samma plan för att spara pengar. Separera bara om de behöver olika scaling.",
            "common_mistake": "Att skapa en ny App Service Plan för varje Web App. Det blir dyrt snabbt!"
        },
        {
            "id": "deployment-methods",
            "title": "Deployment Methods",
            "explanation": """Det finns flera sätt att deploya till App Service:

**1. ZIP Deploy (enklast):**
```bash
az webapp deployment source config-zip \\
    --src app.zip --name myapp --resource-group rg
```
✅ Snabbt, enkelt
❌ Manuellt, inget versionshantering

**2. Local Git:**
```bash
az webapp deployment source config-local-git --name myapp
git remote add azure <url>
git push azure main
```
✅ Git-baserat, deployment on push
❌ Kräver git config på Azure-sidan

**3. GitHub Actions (rekommenderat):**
```yaml
- uses: azure/webapps-deploy@v2
  with:
    app-name: myapp
    publish-profile: ${{ secrets.PUBLISH_PROFILE }}
```
✅ Full CI/CD, versionshistorik
✅ Integration med PR workflow

**4. Container Deploy:**
```bash
az webapp create --deployment-container-image-name myregistry.azurecr.io/app:v1
```
✅ Full kontroll över runtime
✅ Konsekvent miljö

**Rekommendation:**
- Dev/test: ZIP eller Local Git
- Produktion: GitHub Actions eller Azure DevOps""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│            DEPLOYMENT METHODS                    │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌──────────────────────────────────────────┐  │
│   │ 1. ZIP DEPLOY                            │  │
│   │    [Local] → zip → az webapp deploy      │  │
│   └──────────────────────────────────────────┘  │
│                                                 │
│   ┌──────────────────────────────────────────┐  │
│   │ 2. LOCAL GIT                             │  │
│   │    [Local] → git push azure → Build      │  │
│   └──────────────────────────────────────────┘  │
│                                                 │
│   ┌──────────────────────────────────────────┐  │
│   │ 3. GITHUB ACTIONS (Recommended)          │  │
│   │    [GitHub] → PR → CI → Deploy → Slot    │  │
│   └──────────────────────────────────────────┘  │
│                                                 │
│   ┌──────────────────────────────────────────┐  │
│   │ 4. CONTAINER DEPLOY                      │  │
│   │    [ACR] → webhook → Pull → Run          │  │
│   └──────────────────────────────────────────┘  │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Använd GitHub Actions med deployment slots. Deploya till staging, testa, swap till production.",
            "common_mistake": "Att deploya direkt till produktion utan att testa. Använd alltid staging slot först."
        },
        {
            "id": "deployment-slots",
            "title": "Deployment Slots & Zero-Downtime",
            "explanation": """Deployment slots möjliggör zero-downtime deployments.

**Vad är slots?**
- Separata instanser av samma app
- Egna URLs: myapp-staging.azurewebsites.net
- Egna app settings (kan vara slot-specifika)
- Kan swappas på sekunder

**Workflow:**
1. Deploya till staging slot
2. Testa på staging URL
3. Swap staging ↔ production
4. Om problem: swap tillbaka!

**Slot-specifika settings:**
```
Production slot:
  DATABASE_URL = prod-db.azure.com
  DEBUG = false

Staging slot:
  DATABASE_URL = staging-db.azure.com
  DEBUG = true
```
Dessa byter INTE plats vid swap!

**Traffic splitting:**
- Skicka 10% trafik till staging för canary releases
- Gradvis öka till 100% om allt ser bra ut""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           DEPLOYMENT SLOT WORKFLOW              │
├─────────────────────────────────────────────────┤
│                                                 │
│   BEFORE SWAP:                                  │
│   ┌─────────────────┐ ┌─────────────────┐       │
│   │   PRODUCTION    │ │    STAGING      │       │
│   │   app v1.0      │ │    app v1.1     │       │
│   │   myapp.azure   │ │ myapp-staging   │       │
│   │   100% traffic  │ │   0% traffic    │       │
│   └─────────────────┘ └─────────────────┘       │
│                                                 │
│   az webapp deployment slot swap --slot staging │
│                    ↓↑                           │
│                                                 │
│   AFTER SWAP:                                   │
│   ┌─────────────────┐ ┌─────────────────┐       │
│   │   PRODUCTION    │ │    STAGING      │       │
│   │   app v1.1  ✨  │ │    app v1.0     │       │
│   │   myapp.azure   │ │ myapp-staging   │       │
│   │   100% traffic  │ │   0% traffic    │       │
│   └─────────────────┘ └─────────────────┘       │
│                                                 │
│   ⚡ Swap takes ~5 seconds, zero downtime!      │
│   🔄 Rollback = swap again                      │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Markera settings som 'slot-sticky' om de ska stanna i slotten (t.ex. DEBUG=true på staging).",
            "common_mistake": "Att glömma att staging har produktionsdata efter swap. Var försiktig med databas-migrations!"
        },
        {
            "id": "configuration",
            "title": "App Settings & Secrets",
            "explanation": """App Service har kraftfull konfigurationshantering.

**App Settings (Environment Variables):**
```bash
az webapp config appsettings set \\
    --name myapp --resource-group rg \\
    --settings NODE_ENV=production API_URL=https://api.example.com
```
I din kod: `process.env.NODE_ENV`

**Connection Strings:**
```bash
az webapp config connection-string set \\
    --name myapp --resource-group rg \\
    --connection-string-type SQLAzure \\
    --settings DB="Server=tcp:myserver.database.windows.net..."
```

**Key Vault Integration (rekommenderat för secrets):**
```bash
# Referera till Key Vault secret
@Microsoft.KeyVault(VaultName=myvault;SecretName=api-key)
```
Appen får bara rätt att läsa secrets, aldrig exponerat i portal!

**Best Practices:**
| Setting typ | Var? | Exempel |
|-------------|------|---------|
| Publika config | App Settings | NODE_ENV, LOG_LEVEL |
| API keys | Key Vault reference | @Microsoft.KeyVault(...) |
| Connection strings | App Settings / Key Vault | DATABASE_URL |
| Slot-specifikt | Deployment slot setting | DEBUG=true (staging only) |""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           CONFIGURATION HIERARCHY               │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │         AZURE KEY VAULT                 │   │
│   │   • Database passwords                  │   │
│   │   • API keys                           │   │
│   │   • SSL certificates                   │   │
│   └──────────────────┬──────────────────────┘   │
│                      │ @Microsoft.KeyVault(...)│
│   ┌──────────────────▼──────────────────────┐   │
│   │         APP SETTINGS                    │   │
│   │   • NODE_ENV=production                │   │
│   │   • LOG_LEVEL=info                     │   │
│   │   • API_KEY=@KeyVault(...)             │   │
│   └──────────────────┬──────────────────────┘   │
│                      │ process.env.API_KEY      │
│   ┌──────────────────▼──────────────────────┐   │
│   │         YOUR APPLICATION               │   │
│   │   const key = process.env.API_KEY      │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   ✅ Secrets never in code or portal visible   │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Använd ALLTID Key Vault references för secrets. Aldrig hårdkoda eller sätt direkt i App Settings.",
            "common_mistake": "Att lägga secrets direkt i App Settings. De syns i klartext i Azure Portal!"
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du sätta upp en komplett App Service med deployment slots och configuration.",
        "exercises": [
            {
                "step": 1,
                "title": "Skapa App Service Plan",
                "instruction": "Skapa en Linux App Service Plan med Basic tier.",
                "hint": "Använd 'az appservice plan create' med --is-linux",
                "expected_command": "az appservice plan create --name asp-webapp --resource-group rg-demo --location northeurope --sku B1 --is-linux",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.Web/serverfarms/asp-webapp",
  "kind": "linux",
  "location": "North Europe",
  "name": "asp-webapp",
  "sku": {
    "capacity": 1,
    "name": "B1",
    "tier": "Basic"
  }
}""",
                "explanation": "B1 är bra startpunkt för produktion. --is-linux krävs för Node.js, Python, etc.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Skapa Web App",
                "instruction": "Skapa en Node.js Web App på planen.",
                "hint": "Använd 'az webapp create' med --runtime",
                "expected_command": "az webapp create --name mywebapp-demo-12345 --resource-group rg-demo --plan asp-webapp --runtime \"NODE:18-lts\"",
                "expected_output": """{
  "defaultHostName": "mywebapp-demo-12345.azurewebsites.net",
  "enabled": true,
  "httpsOnly": true,
  "name": "mywebapp-demo-12345",
  "state": "Running"
}""",
                "explanation": "Web App-namn måste vara globalt unika. De blir din URL: <name>.azurewebsites.net",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Konfigurera App Settings",
                "instruction": "Sätt environment variables för produktion.",
                "hint": "Använd 'az webapp config appsettings set'",
                "expected_command": "az webapp config appsettings set --name mywebapp-demo-12345 --resource-group rg-demo --settings NODE_ENV=production LOG_LEVEL=info PORT=8080",
                "expected_output": """[
  {"name": "NODE_ENV", "value": "production"},
  {"name": "LOG_LEVEL", "value": "info"},
  {"name": "PORT", "value": "8080"}
]""",
                "explanation": "App Settings blir environment variables i din app. Tillgängliga via process.env.NODE_ENV etc.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Skapa Staging Slot",
                "instruction": "Skapa en deployment slot för staging.",
                "hint": "Använd 'az webapp deployment slot create'",
                "expected_command": "az webapp deployment slot create --name mywebapp-demo-12345 --resource-group rg-demo --slot staging",
                "expected_output": """{
  "defaultHostName": "mywebapp-demo-12345-staging.azurewebsites.net",
  "name": "mywebapp-demo-12345/staging",
  "state": "Running"
}""",
                "explanation": "Staging slot har egen URL och egna settings. Perfekt för att testa innan produktion.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Konfigurera Slot-Specifika Settings",
                "instruction": "Sätt DEBUG=true på staging (ska inte följa med vid swap).",
                "hint": "Använd --slot-settings istället för --settings",
                "expected_command": "az webapp config appsettings set --name mywebapp-demo-12345 --resource-group rg-demo --slot staging --slot-settings DEBUG=true",
                "expected_output": """[
  {"name": "DEBUG", "slotSetting": true, "value": "true"}
]""",
                "explanation": "slot-settings stannar i slotten vid swap. DEBUG=true blir kvar på staging, production får aldrig det.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Swap Slots",
                "instruction": "Swappa staging till production.",
                "hint": "Använd 'az webapp deployment slot swap'",
                "expected_command": "az webapp deployment slot swap --name mywebapp-demo-12345 --resource-group rg-demo --slot staging --target-slot production",
                "expected_output": """(Swap completed successfully)""",
                "explanation": "Swap tar ~5 sekunder. Zero downtime! Om något är fel: swap tillbaka.",
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
                "front": "Vad är skillnaden mellan App Service Plan och Web App?",
                "back": "Plan = infrastruktur (CPU, RAM, pris). Web App = din applikation. Flera apps kan dela en plan."
            },
            {
                "id": "fc2",
                "front": "Hur refererar du till en Key Vault secret i App Settings?",
                "back": "@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret)"
            },
            {
                "id": "fc3",
                "front": "Vad är en deployment slot?",
                "back": "En separat instans av samma app med egen URL och config. Används för zero-downtime deployments."
            },
            {
                "id": "fc4",
                "front": "Vad händer med 'slot-sticky' settings vid swap?",
                "back": "De stannar kvar i sin slot och byter inte plats. T.ex. DEBUG=true stannar på staging."
            },
            {
                "id": "fc5",
                "front": "Vilken tier behövs för deployment slots?",
                "back": "Standard (S1) eller högre. Free, Shared och Basic har inte slots."
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "Du har 3 små web apps. Vad är mest kostnadseffektivt?",
                "options": [
                    "3 separata App Service Plans",
                    "1 App Service Plan med 3 Web Apps",
                    "3 Free tier Web Apps",
                    "Azure Functions för alla"
                ],
                "correct_answer": 1,
                "explanation": "Flera Web Apps kan dela samma Plan och dela på kostnaden. Betala för 1 plan istället för 3."
            },
            {
                "id": "mc2",
                "question": "Du vill deploya ny version utan downtime. Vad gör du?",
                "options": [
                    "Deploya direkt till produktion",
                    "Stäng av appen, deploya, starta",
                    "Deploya till staging slot, testa, swap",
                    "Skapa ny Web App och byt DNS"
                ],
                "correct_answer": 2,
                "explanation": "Deployment slots + swap ger zero-downtime. Staging testar den nya versionen, swap tar 5 sekunder."
            },
            {
                "id": "mc3",
                "question": "Var ska du lagra API-nycklar i App Service?",
                "options": [
                    "Direkt i koden",
                    "I App Settings som plain text",
                    "I Azure Key Vault med reference",
                    "I en config-fil i repot"
                ],
                "correct_answer": 2,
                "explanation": "Key Vault references håller secrets säkra. De syns aldrig i klartext i Portal eller logs."
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "Full CI/CD Pipeline med App Service",
        "scenario": """Du ska sätta upp en komplett deployment pipeline för ett team:
- GitHub repo med Node.js app
- Automatisk deploy vid push till main
- Staging slot för testing
- Auto-swap till produktion om health check OK
- Rollback-strategi vid problem""",
        "requirements": [
            "Skapa App Service med Standard tier (för slots)",
            "Konfigurera GitHub Actions deployment",
            "Skapa staging slot med slot-sticky settings",
            "Implementera health check endpoint",
            "Konfigurera auto-swap med health check",
            "Dokumentera rollback-procedur"
        ],
        "hints": [
            "Standard S1 tier krävs för slots",
            "Download publish profile från Azure Portal",
            "Health check endpoint: /api/health returnerar 200",
            "Auto-swap kan konfigureras i slot settings"
        ],
        "solution": """# ═══════════════════════════════════════════════════════════════
# 1. INFRASTRUCTURE SETUP (run once)
# ═══════════════════════════════════════════════════════════════

#!/bin/bash
# deploy-infrastructure.sh

RESOURCE_GROUP="rg-myapp-prod"
APP_NAME="myapp-prod-12345"
LOCATION="northeurope"

# Create Resource Group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service Plan (Standard for slots)
az appservice plan create \\
    --name asp-$APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --location $LOCATION \\
    --sku S1 \\
    --is-linux

# Create Web App
az webapp create \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --plan asp-$APP_NAME \\
    --runtime "NODE:18-lts"

# Enable HTTPS only
az webapp update \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --https-only true

# Create staging slot
az webapp deployment slot create \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --slot staging

# Configure staging-specific settings (slot sticky)
az webapp config appsettings set \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --slot staging \\
    --slot-settings NODE_ENV=staging DEBUG=true

# Configure production settings
az webapp config appsettings set \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --settings NODE_ENV=production LOG_LEVEL=info

# Configure health check
az webapp config set \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --generic-configurations '{"healthCheckPath": "/api/health"}'

# Configure auto-swap from staging
az webapp deployment slot auto-swap \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --slot staging \\
    --auto-swap-slot production

echo "✅ Infrastructure created!"
echo "Download publish profile from Azure Portal for GitHub Actions"


# ═══════════════════════════════════════════════════════════════
# 2. GITHUB ACTIONS WORKFLOW
# ═══════════════════════════════════════════════════════════════

# .github/workflows/deploy.yml
name: Deploy to Azure App Service

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AZURE_WEBAPP_NAME: myapp-prod-12345
  NODE_VERSION: '18.x'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: node-app
          path: .

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://myapp-prod-12345-staging.azurewebsites.net

    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: node-app

      - name: Deploy to staging slot
        uses: azure/webapps-deploy@v2
        with:
          app-name: ${{ env.AZURE_WEBAPP_NAME }}
          slot-name: staging
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE_STAGING }}

      - name: Health check
        run: |
          echo "Waiting for app to warm up..."
          sleep 30

          HEALTH_URL="https://myapp-prod-12345-staging.azurewebsites.net/api/health"
          HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

          if [ $HTTP_STATUS -eq 200 ]; then
            echo "✅ Health check passed!"
          else
            echo "❌ Health check failed with status $HTTP_STATUS"
            exit 1
          fi

  # Auto-swap is configured in Azure, so this is optional manual swap
  swap-to-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp-prod-12345.azurewebsites.net

    steps:
      - name: Login to Azure
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Swap to production
        run: |
          az webapp deployment slot swap \\
            --name ${{ env.AZURE_WEBAPP_NAME }} \\
            --resource-group rg-myapp-prod \\
            --slot staging \\
            --target-slot production

      - name: Verify production health
        run: |
          sleep 10
          HEALTH_URL="https://myapp-prod-12345.azurewebsites.net/api/health"
          HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

          if [ $HTTP_STATUS -ne 200 ]; then
            echo "❌ Production health check failed! Initiating rollback..."
            az webapp deployment slot swap \\
              --name ${{ env.AZURE_WEBAPP_NAME }} \\
              --resource-group rg-myapp-prod \\
              --slot staging \\
              --target-slot production
            exit 1
          fi

          echo "✅ Production deployment successful!"


# ═══════════════════════════════════════════════════════════════
# 3. HEALTH CHECK ENDPOINT
# ═══════════════════════════════════════════════════════════════

// routes/health.js
const express = require('express');
const router = express.Router();

router.get('/api/health', async (req, res) => {
  try {
    // Check database connection
    // await db.query('SELECT 1');

    // Check external services
    // await redis.ping();

    res.status(200).json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      version: process.env.npm_package_version || '1.0.0',
      environment: process.env.NODE_ENV
    });
  } catch (error) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message
    });
  }
});

module.exports = router;


# ═══════════════════════════════════════════════════════════════
# 4. ROLLBACK PROCEDURE
# ═══════════════════════════════════════════════════════════════

# Manual rollback (if auto-rollback didn't trigger)
#!/bin/bash
# rollback.sh

APP_NAME="myapp-prod-12345"
RESOURCE_GROUP="rg-myapp-prod"

echo "🔄 Initiating rollback..."

# Swap staging (which now has old production) back to production
az webapp deployment slot swap \\
    --name $APP_NAME \\
    --resource-group $RESOURCE_GROUP \\
    --slot staging \\
    --target-slot production

echo "✅ Rollback complete!"
echo "Previous production version is now live."
echo ""
echo "Next steps:"
echo "1. Investigate what went wrong in staging slot"
echo "2. Fix the issue"
echo "3. Redeploy to staging"
echo "4. Test thoroughly before next swap"
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
        "app service",
        "app service plan",
        "deployment slots",
        "zero downtime",
        "github actions",
        "ci/cd",
        "configuration",
        "key vault"
    ]
}
