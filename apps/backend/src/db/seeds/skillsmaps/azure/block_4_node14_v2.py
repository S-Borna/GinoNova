"""
Azure Block 4 Node 14: Azure Container Registry - V2 Interactive Format
"""

AZURE_NODE_14_ACR_V2 = {
    "node_id": 14,
    "title": "Azure Container Registry",
    "slug": "azure-container-registry",
    "description": "Privat Docker registry i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Container Registry",
            "content": {
                "headline": "Your private Docker Hub, but in Azure",
                "hook": "ACR är managed container registry som integrerar sömlöst med AKS, App Service och Azure DevOps Pipelines.",
                "learning_objectives": [
                    "Skapa och konfigurera Azure Container Registry",
                    "Push och pull Docker images",
                    "Använda ACR Tasks för cloud builds",
                    "Integrera ACR med AKS och App Service"
                ],
                "prerequisites": ["Docker basics", "Azure fundamentals"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "ACR Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "ACR Tiers",
                        "explanation": "Basic (10GB, ~$5/mån), Standard (100GB, ~$20/mån), Premium (500GB, ~$50/mån med geo-replication och private link).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ Basic      │ 10GB, dev/test               │
│ Standard   │ 100GB, produktion            │
│ Premium    │ 500GB, geo-rep, private link │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Standard räcker för de flesta produktionsmiljöer.",
                        "common_mistake": "Att aktivera admin user i produktion - använd managed identity istället."
                    },
                    {
                        "title": "ACR Tasks",
                        "explanation": "Bygg Docker images direkt i Azure utan lokal Docker installation. Triggered av commits, base image updates eller schedule.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ Source (Git/Local) → ACR Task → Image       │
├─────────────────────────────────────────────┤
│ Triggers:                                   │
│ • Git commit                                │
│ • Base image update                         │
│ • Schedule                                  │
│ • Manual                                    │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "ACR Tasks är perfekt för CI - inget behov av Docker på build agent.",
                        "common_mistake": "Att glömma --platform linux/amd64 vid multi-arch builds."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on ACR",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa Container Registry",
                        "instruction": "Skapa ACR 'myregistry123' med Standard tier",
                        "expected_command": "az acr create --name myregistry123 --resource-group rg-demo --location northeurope --sku Standard",
                        "hint": "Registry name måste vara globalt unikt"
                    },
                    {
                        "task": "Logga in till ACR",
                        "instruction": "Autentisera Docker mot ACR",
                        "expected_command": "az acr login --name myregistry123",
                        "hint": "Detta konfigurerar Docker credentials automatiskt"
                    },
                    {
                        "task": "Bygg image med ACR Tasks",
                        "instruction": "Bygg Dockerfile i current directory och push till ACR",
                        "expected_command": "az acr build --registry myregistry123 --image myapp:v1 .",
                        "hint": "ACR Tasks bygger i molnet - ingen lokal Docker behövs"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Vad är ACR Tasks?", "back": "Cloud-baserad Docker build service som kan triggas av git commits, base image updates eller schedule"},
                        {"front": "Hur autentiserar AKS mot ACR?", "back": "Via managed identity (attach) eller service principal"},
                        {"front": "Vilken tier krävs för geo-replication?", "back": "Premium tier"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad är bästa sättet att autentisera mot ACR i produktion?",
                            "options": ["Admin user", "Managed Identity", "Username/password", "Anonymous"],
                            "correct": 1,
                            "explanation": "Managed Identity ger säker autentisering utan lösenordshantering"
                        },
                        {
                            "question": "Hur kopplar du ACR till AKS?",
                            "options": ["Manuell config", "az aks update --attach-acr", "Docker login", "Service Connection"],
                            "correct": 1,
                            "explanation": "az aks update --attach-acr skapar automatiskt rätt RBAC"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "ACR Challenge",
            "content": {
                "scenario": "Sätt upp ett container registry för en produktions-pipeline.",
                "requirements": [
                    "Skapa Premium ACR med geo-replication",
                    "Konfigurera webhook för image push events",
                    "Attach ACR till existerande AKS cluster",
                    "Sätt upp retention policy för gamla images"
                ],
                "hints": [
                    "Premium tier krävs för geo-replication",
                    "az acr webhook create för webhooks",
                    "az aks update --attach-acr för AKS",
                    "az acr config retention update för cleanup"
                ],
                "solution": """# Premium ACR med geo-rep
az acr create --name acrmyapp --resource-group rg-demo --sku Premium --location northeurope

# Geo-replication
az acr replication create --registry acrmyapp --location westeurope

# Webhook för push events
az acr webhook create --registry acrmyapp --name webhookprod \\
    --uri https://myapp.com/webhook \\
    --actions push delete

# Attach till AKS
az aks update --name myaks --resource-group rg-demo --attach-acr acrmyapp

# Retention policy (behåll 30 dagar)
az acr config retention update --registry acrmyapp --status enabled --days 30 --type UntaggedManifests""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
