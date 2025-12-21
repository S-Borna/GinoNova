"""
Azure Block 5 Node 17: Azure Entra ID - V2 Interactive Format
"""

AZURE_NODE_17_ENTRA_V2 = {
    "node_id": 17,
    "title": "Azure Entra ID",
    "slug": "azure-entra-id",
    "description": "Identity och access management i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Entra ID",
            "content": {
                "headline": "Identity is the new perimeter",
                "hook": "Azure Entra ID (tidigare Azure AD) är kärnan i Azure-säkerhet med authentication, authorization, SSO och MFA.",
                "learning_objectives": [
                    "Förstå skillnaden mellan User, Service Principal och Managed Identity",
                    "Skapa och konfigurera Service Principals för CI/CD",
                    "Implementera Managed Identity för säker applikationsaccess",
                    "Konfigurera RBAC för Azure resources"
                ],
                "prerequisites": ["Azure fundamentals", "Basic security concepts"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Identity Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Identity Types",
                        "explanation": "User Identity (människor), Service Principal (appar/services med client ID + secret), Managed Identity (Azure-hanterad, inga credentials).",
                        "diagram": """
+---------------------------------------------+
| USER IDENTITY   | Interactive login, MFA   |
| SERVICE PRINCIPAL| App credentials, CI/CD  |
| MANAGED IDENTITY | No credentials, Azure   |
+---------------------------------------------+
Recommendation: Managed Identity > Service Principal > User""",
                        "pro_tip": "Använd ALLTID Managed Identity för Azure-resurser - inga credentials att hantera!",
                        "common_mistake": "Att hårdkoda Service Principal credentials i kod."
                    },
                    {
                        "title": "RBAC (Role-Based Access Control)",
                        "explanation": "Security principal + Role + Scope = Access. Roller: Owner, Contributor, Reader. Scope: Management Group -> Subscription -> Resource Group -> Resource.",
                        "diagram": """
+---------------------------------------------+
| WHO        | WHAT              | WHERE      |
+---------------------------------------------+
| Principal  | Role              | Scope      |
| (User/App) | (Contributor)     | (/sub/rg)  |
+---------------------------------------------+
Inheritance: MG -> Subscription -> RG -> Resource""",
                        "pro_tip": "Principle of least privilege - ge bara nödvändiga rättigheter.",
                        "common_mistake": "Att ge Owner på subscription-nivå istället för minimal scope."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Identity",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa Service Principal",
                        "instruction": "Skapa SP 'sp-cicd' med Contributor-roll på resource group",
                        "expected_command": "az ad sp create-for-rbac --name sp-cicd --role Contributor --scopes /subscriptions/<sub-id>/resourceGroups/rg-demo",
                        "hint": "Output innehåller appId, password och tenant - spara dessa!"
                    },
                    {
                        "task": "Aktivera Managed Identity på App Service",
                        "instruction": "Tilldela system-assigned identity till web app",
                        "expected_command": "az webapp identity assign --name app-myapp --resource-group rg-demo",
                        "hint": "System-assigned skapas/tas bort med resursen"
                    },
                    {
                        "task": "Tilldela RBAC-roll",
                        "instruction": "Ge Managed Identity access till Key Vault",
                        "expected_command": "az role assignment create --role 'Key Vault Secrets User' --assignee <principal-id> --scope /subscriptions/<sub>/resourceGroups/rg-demo/providers/Microsoft.KeyVault/vaults/kv-myapp",
                        "hint": "Hämta principalId från identity assign output"
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
                        {"front": "Vad är skillnaden mellan System-assigned och User-assigned Managed Identity?", "back": "System-assigned: skapas/tas bort med resursen, 1:1. User-assigned: separat resurs som kan delas mellan många resurser."},
                        {"front": "Vad innehåller Service Principal output?", "back": "appId (client ID), password (client secret), tenant - SECRET visas bara EN gång!"},
                        {"front": "Hur fungerar DefaultAzureCredential?", "back": "Försöker i ordning: Environment vars -> Managed Identity -> VS Code -> Azure CLI -> Interactive browser"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken identity-typ är säkrast för Azure-appar?",
                            "options": ["Service Principal med secret", "Managed Identity", "User credentials", "API key"],
                            "correct": 1,
                            "explanation": "Managed Identity hanteras helt av Azure - inga credentials att läcka"
                        },
                        {
                            "question": "Var bör du tilldela RBAC-roller för principle of least privilege?",
                            "options": ["Management Group", "Subscription", "Resource Group eller Resource", "Tenant root"],
                            "correct": 2,
                            "explanation": "Minsta möjliga scope - Resource Group eller enskild resource"
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
            "title": "Identity Challenge",
            "content": {
                "scenario": "Säkra en web app som behöver access till Key Vault och Storage utan hårdkodade credentials.",
                "requirements": [
                    "Aktivera Managed Identity på App Service",
                    "Ge MI läs-access till Key Vault secrets",
                    "Ge MI skrivaccess till Blob Storage",
                    "Verifiera med Python SDK och DefaultAzureCredential"
                ],
                "hints": [
                    "Key Vault Secrets User för secrets",
                    "Storage Blob Data Contributor för blob write",
                    "DefaultAzureCredential hittar MI automatiskt"
                ],
                "solution": """# 1. Aktivera Managed Identity
az webapp identity assign --name app-myapp --resource-group rg-demo

# Spara principalId från output
PRINCIPAL_ID=$(az webapp identity show --name app-myapp --resource-group rg-demo --query principalId -o tsv)

# 2. RBAC för Key Vault
az role assignment create --role "Key Vault Secrets User" \\
    --assignee $PRINCIPAL_ID \\
    --scope /subscriptions/<sub>/resourceGroups/rg-demo/providers/Microsoft.KeyVault/vaults/kv-myapp

# 3. RBAC för Storage
az role assignment create --role "Storage Blob Data Contributor" \\
    --assignee $PRINCIPAL_ID \\
    --scope /subscriptions/<sub>/resourceGroups/rg-demo/providers/Microsoft.Storage/storageAccounts/stmyapp

# 4. Python kod
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://kv-myapp.vault.azure.net", credential=credential)
secret = client.get_secret("db-password")""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
