"""
Azure Block 4 Node 15: ARM Templates & Bicep - V2 Interactive Format
"""

AZURE_NODE_15_BICEP_V2 = {
    "node_id": 15,
    "title": "ARM Templates & Bicep",
    "slug": "azure-arm-bicep",
    "description": "Infrastructure as Code för Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "ARM Templates & Bicep",
            "content": {
                "headline": "Define your infrastructure in code",
                "hook": "Bicep är Azures moderna IaC-språk som kompileras till ARM templates - enklare syntax, full IntelliSense och moduler.",
                "learning_objectives": [
                    "Förstå skillnaden mellan ARM och Bicep",
                    "Skriva Bicep templates med parameters och modules",
                    "Deploya infrastruktur med what-if validation",
                    "Organisera Bicep-kod med moduler"
                ],
                "prerequisites": ["Azure fundamentals", "Resource Groups"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "IaC Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "ARM vs Bicep",
                        "explanation": "ARM är JSON-baserat (verbose), Bicep är DSL som kompileras till ARM. Bicep har enklare syntax, typsäkerhet och IntelliSense.",
                        "diagram": """
+---------------------------------------------+
| ARM Template (JSON)  | Bicep (.bicep)       |
+---------------------------------------------+
| Verbose, 100+ lines  | Koncis, 30 lines     |
| Svårt att läsa       | Lätt att läsa        |
| Ingen IntelliSense   | Full IntelliSense    |
| Ingen moduler        | Moduler för reuse    |
+---------------------------------------------+
Bicep kompileras -> ARM JSON -> Azure deployment""",
                        "pro_tip": "Använd ALLTID Bicep för nya projekt - ARM är legacy.",
                        "common_mistake": "Att skriva ARM JSON manuellt - Bicep är mycket enklare."
                    },
                    {
                        "title": "Bicep Modules",
                        "explanation": "Moduler bryter upp templates i återanvändbara komponenter. En modul = en .bicep fil som kan anropas från main.bicep.",
                        "diagram": """
+---------------------------------------------+
| main.bicep                                  |
| +-- modules/storage.bicep                   |
| +-- modules/network.bicep                   |
| +-- modules/webapp.bicep                    |
+---------------------------------------------+
| module storage 'modules/storage.bicep' = {  |
|   name: 'storage-deploy'                    |
|   params: { ... }                           |
| }                                           |
+---------------------------------------------+""",
                        "pro_tip": "Skapa ett library av modules för vanliga patterns.",
                        "common_mistake": "Att inte använda outputs från modules - de kopplar ihop resurser."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Bicep",
            "content": {
                "exercises": [
                    {
                        "task": "Validera Bicep template",
                        "instruction": "Bygg Bicep till ARM för validering",
                        "expected_command": "az bicep build --file main.bicep",
                        "hint": "Build kompilerar till ARM JSON utan deployment"
                    },
                    {
                        "task": "What-if deployment",
                        "instruction": "Visa vad som kommer att ändras utan att deploya",
                        "expected_command": "az deployment group what-if --resource-group rg-demo --template-file main.bicep",
                        "hint": "What-if är som terraform plan - visar ändringar"
                    },
                    {
                        "task": "Deploy Bicep template",
                        "instruction": "Deploya main.bicep till resource group",
                        "expected_command": "az deployment group create --resource-group rg-demo --template-file main.bicep --parameters environment=dev",
                        "hint": "--parameters skickar värden till template"
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
                        {"front": "Vad gör 'az bicep build'?", "back": "Kompilerar Bicep till ARM JSON utan deployment - bra för validering"},
                        {"front": "Vad är what-if?", "back": "Visar vad som kommer att ändras vid deployment utan att faktiskt deploya"},
                        {"front": "Hur refererar man till module output?", "back": "module.outputs.propertyName - t.ex. storage.outputs.connectionString"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken fil-extension har Bicep?",
                            "options": [".arm", ".bicep", ".json", ".yaml"],
                            "correct": 1,
                            "explanation": "Bicep-filer har .bicep extension"
                        },
                        {
                            "question": "Vad händer om resursen redan finns vid deployment?",
                            "options": ["Error", "Uppdateras", "Ignoreras", "Raderas först"],
                            "correct": 1,
                            "explanation": "Bicep är deklarativt - existerande resurser uppdateras till önskat state"
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
            "title": "Bicep Challenge",
            "content": {
                "scenario": "Skapa IaC för en web app med storage och databas.",
                "requirements": [
                    "Skapa main.bicep med parameters för environment",
                    "Använd modules för storage, database och webapp",
                    "Webapp ska referera till database connection string",
                    "Validera med what-if innan deployment"
                ],
                "hints": [
                    "param environment string med @allowed",
                    "module database 'modules/db.bicep' = {...}",
                    "connectionString: database.outputs.connString"
                ],
                "solution": """// main.bicep
@allowed(['dev', 'prod'])
param environment string
param location string = resourceGroup().location

module storage 'modules/storage.bicep' = {
  name: 'storage-${environment}'
  params: {
    location: location
    environment: environment
  }
}

module database 'modules/database.bicep' = {
  name: 'db-${environment}'
  params: {
    location: location
  }
}

module webapp 'modules/webapp.bicep' = {
  name: 'webapp-${environment}'
  params: {
    location: location
    dbConnectionString: database.outputs.connectionString
    storageAccount: storage.outputs.accountName
  }
}

output appUrl string = webapp.outputs.url

// Deploy med what-if först
// az deployment group what-if -g rg-demo -f main.bicep -p environment=dev
// az deployment group create -g rg-demo -f main.bicep -p environment=dev""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
