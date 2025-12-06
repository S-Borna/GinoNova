"""
Azure Block 5 Node 18: Azure Key Vault - V2 Interactive Format
"""

AZURE_NODE_18_KEYVAULT_V2 = {
    "node_id": 18,
    "title": "Azure Key Vault",
    "slug": "azure-key-vault",
    "description": "Säker lagring av hemligheter, nycklar och certifikat",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Key Vault",
            "content": {
                "headline": "Never store secrets in code. Ever.",
                "hook": "Key Vault är Azures centrala tjänst för secrets, krypteringsnycklar och certifikat med RBAC-baserad access control.",
                "learning_objectives": [
                    "Skapa och konfigurera Key Vault med RBAC",
                    "Hantera secrets med versioning",
                    "Integrera Key Vault med appar via Managed Identity",
                    "Implementera soft-delete och purge protection"
                ],
                "prerequisites": ["Azure Entra ID basics", "RBAC understanding"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Key Vault Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Key Vault Objects",
                        "explanation": "Secrets (connection strings, API keys), Keys (kryptografiska nycklar), Certificates (SSL/TLS). Standard = software-backed, Premium = HSM-backed.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ KEY VAULT: kv-myapp                         │
├─────────────────────────────────────────────┤
│ Secrets      │ db-password, api-key        │
│ Keys         │ encryption-key, signing-key │
│ Certificates │ ssl-cert, code-sign-cert    │
├─────────────────────────────────────────────┤
│ Standard (~$0.03/op) │ Premium (HSM ~$1/key)│
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Secrets versioneras automatiskt - du kan rollback till tidigare version.",
                        "common_mistake": "Att inte aktivera purge protection i produktion."
                    },
                    {
                        "title": "Access Control",
                        "explanation": "RBAC (rekommenderat) eller Access Policies. RBAC-roller: Key Vault Secrets User (läs), Key Vault Secrets Officer (hantera), Key Vault Administrator (full).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ RBAC (Recommended)                          │
├─────────────────────────────────────────────┤
│ Secrets User    │ Get, List secrets        │
│ Secrets Officer │ + Set, Delete, Backup    │
│ Administrator   │ Full access + purge      │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Använd --enable-rbac-authorization vid vault creation.",
                        "common_mistake": "Att blanda Access Policies och RBAC - välj en modell."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Key Vault",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa Key Vault med RBAC",
                        "instruction": "Skapa vault 'kv-demo' med RBAC authorization",
                        "expected_command": "az keyvault create --name kv-demo-unique123 --resource-group rg-demo --location northeurope --enable-rbac-authorization true",
                        "hint": "Vault name måste vara globalt unikt"
                    },
                    {
                        "task": "Skapa en secret",
                        "instruction": "Lägg till secret 'db-password' med värde",
                        "expected_command": "az keyvault secret set --vault-name kv-demo-unique123 --name db-password --value 'SuperSecret123!'",
                        "hint": "Värdet kan också läsas från fil med @filename"
                    },
                    {
                        "task": "Hämta secret",
                        "instruction": "Läs ut secret värdet",
                        "expected_command": "az keyvault secret show --vault-name kv-demo-unique123 --name db-password --query value -o tsv",
                        "hint": "--query value extraherar bara värdet"
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
                        {"front": "Vad är skillnaden mellan Standard och Premium tier?", "back": "Standard = software-backed keys, Premium = HSM-backed keys (FIPS 140-2 Level 2)"},
                        {"front": "Vad gör soft-delete?", "back": "Borttagna secrets behålls i 7-90 dagar och kan återställas med az keyvault secret recover"},
                        {"front": "Vilken RBAC-roll behövs för att läsa secrets?", "back": "Key Vault Secrets User"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken access model rekommenderas för Key Vault?",
                            "options": ["Access Policies", "RBAC", "Public access", "Firewall rules"],
                            "correct": 1,
                            "explanation": "RBAC ger finare kontroll och integrerar med Azure IAM"
                        },
                        {
                            "question": "Vad händer när du uppdaterar en secret?",
                            "options": ["Gamla värdet raderas", "Ny version skapas", "Error", "Måste ta bort först"],
                            "correct": 1,
                            "explanation": "Secrets versioneras automatiskt - gamla versioner finns kvar"
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
            "title": "Key Vault Challenge",
            "content": {
                "scenario": "Sätt upp Key Vault för en produktionsapp med alla säkerhetsfunktioner.",
                "requirements": [
                    "Skapa Key Vault med RBAC, soft-delete och purge protection",
                    "Lägg till secrets för databas och API",
                    "Ge App Service Managed Identity access",
                    "Verifiera access med Python SDK"
                ],
                "hints": [
                    "--enable-purge-protection för produktion",
                    "--retention-days 90 för compliance",
                    "Key Vault Secrets User räcker för läsning"
                ],
                "solution": """# 1. Skapa production Key Vault
az keyvault create --name kv-prod-myapp --resource-group rg-demo --location northeurope \\
    --enable-rbac-authorization true \\
    --enable-soft-delete true \\
    --retention-days 90 \\
    --enable-purge-protection true

# 2. Lägg till secrets
az keyvault secret set --vault-name kv-prod-myapp --name db-connection --value 'Server=sql...;Password=xxx'
az keyvault secret set --vault-name kv-prod-myapp --name api-key --value 'sk-xxx'

# 3. RBAC för App Service MI
PRINCIPAL_ID=$(az webapp identity show --name app-myapp --resource-group rg-demo --query principalId -o tsv)
az role assignment create --role "Key Vault Secrets User" \\
    --assignee $PRINCIPAL_ID \\
    --scope /subscriptions/<sub>/resourceGroups/rg-demo/providers/Microsoft.KeyVault/vaults/kv-prod-myapp

# 4. Python verification
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://kv-prod-myapp.vault.azure.net", credential=credential)
db_conn = client.get_secret("db-connection").value""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
