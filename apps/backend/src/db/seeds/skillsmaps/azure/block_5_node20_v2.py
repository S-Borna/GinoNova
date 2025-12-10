"""
Azure Block 5 Node 20: Azure Governance - V2 Interactive Format
"""

AZURE_NODE_20_GOVERNANCE_V2 = {
    "node_id": 20,
    "title": "Azure Governance",
    "slug": "azure-governance",
    "description": "Policy, Management Groups och Cost Management",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Governance",
            "content": {
                "headline": "Control without constraints, compliance without complexity",
                "hook": "Azure Governance ger centraliserad kontroll över policies, kostnader och compliance för hela organisationen.",
                "learning_objectives": [
                    "Förstå Management Groups hierarchy och policy inheritance",
                    "Skapa och tilldela Azure Policies (audit vs deny)",
                    "Implementera tagging-strategi för kostnadsallokering",
                    "Konfigurera budgets och cost alerts"
                ],
                "prerequisites": ["Azure fundamentals", "RBAC understanding"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Governance Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Management Groups Hierarchy",
                        "explanation": "Root Tenant -> Management Groups -> Subscriptions -> Resource Groups -> Resources. Policies och RBAC ärvs nedåt.",
                        "diagram": """
+---------------------------------------------+
| ROOT TENANT                                 |
| +-- MG: Organization                        |
|     +-- MG: Production   <- Strict policies |
|     |   +-- Sub: Prod-1                    |
|     +-- MG: Development  <- Relaxed policies|
|     |   +-- Sub: Dev-1                     |
|     +-- MG: Shared                          |
|         +-- Sub: Networking                 |
+---------------------------------------------+
Policy inheritance: Top -> Down""",
                        "pro_tip": "Använd MG för att skilja prod/dev policy strictness.",
                        "common_mistake": "Att inte planera MG-struktur innan du börjar - svårt att ändra efteråt."
                    },
                    {
                        "title": "Azure Policy Effects",
                        "explanation": "Disabled (ingen effekt), Audit (logga), Deny (blockera), DeployIfNotExists (auto-remediate), Modify (ändra).",
                        "diagram": """
+---------------------------------------------+
| POLICY EFFECTS                              |
+---------------------------------------------+
| Disabled          | Policy inactive        |
| Audit             | Log non-compliance     |
| Deny              | Block deployment       |
| DeployIfNotExists | Auto-create resources  |
| Modify            | Change resource config |
+---------------------------------------------+""",
                        "pro_tip": "Börja med Audit, byt till Deny när du verifierat impact.",
                        "common_mistake": "Att sätta Deny direkt - kan blockera legitima deployments."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Governance",
            "content": {
                "exercises": [
                    {
                        "task": "Lista built-in policies",
                        "instruction": "Visa tillgängliga Azure policies",
                        "expected_command": "az policy definition list --query \"[?policyType=='BuiltIn'].{Name:displayName}\" --output table | head -20",
                        "hint": "Det finns 100+ built-in policies"
                    },
                    {
                        "task": "Tilldela policy",
                        "instruction": "Kräv Environment-tag på alla resurser",
                        "expected_command": "az policy assignment create --name require-env-tag --policy 'Require a tag on resources' --scope /subscriptions/<sub-id> --params '{\"tagName\": {\"value\": \"Environment\"}}'",
                        "hint": "Policy name eller ID kan användas"
                    },
                    {
                        "task": "Skapa budget",
                        "instruction": "Skapa månatlig budget på $500 med alert vid 80%",
                        "expected_command": "az consumption budget create --budget-name monthly-budget --amount 500 --time-grain Monthly --category Cost --resource-group rg-demo",
                        "hint": "Notifications konfigureras i Portal eller ARM"
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
                        {"front": "Vad är skillnaden mellan Audit och Deny effect?", "back": "Audit loggar non-compliance men tillåter deployment. Deny blockerar deployment helt."},
                        {"front": "Hur ärvs policies i Azure?", "back": "Top-down: Management Group -> Subscription -> Resource Group -> Resource"},
                        {"front": "Vad gör Resource Locks?", "back": "ReadOnly = kan ej modifiera, CanNotDelete = kan modifiera men ej ta bort"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken policy effect bör du börja med för nya policies?",
                            "options": ["Deny", "Audit", "DeployIfNotExists", "Disabled"],
                            "correct": 1,
                            "explanation": "Audit låter dig se impact innan du blockerar med Deny"
                        },
                        {
                            "question": "Var bör du tilldela organisation-wide policies?",
                            "options": ["Varje Resource Group", "Varje Subscription", "Root Management Group", "Varje resurs"],
                            "correct": 2,
                            "explanation": "Root Management Group ärvs till alla subscriptions och resurser"
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
            "title": "Governance Challenge",
            "content": {
                "scenario": "Implementera governance framework för en organisation med prod och dev miljöer.",
                "requirements": [
                    "Skapa Management Groups för Production och Development",
                    "Tilldela strikt policy på Production (deny public storage)",
                    "Tilldela audit policy på Development",
                    "Implementera tagging-strategi och budget alerts"
                ],
                "hints": [
                    "az account management-group create",
                    "Deny public storage: Microsoft.Storage/storageAccounts/allowBlobPublicAccess",
                    "Inherit tag policy: cd3aa116-8754-49c9-a813-ad46512ece54"
                ],
                "solution": """# 1. Skapa Management Groups
az account management-group create --name mg-production --display-name "Production"
az account management-group create --name mg-development --display-name "Development"

# 2. Flytta subscriptions till MGs
az account management-group subscription add --name mg-production --subscription prod-sub-id
az account management-group subscription add --name mg-development --subscription dev-sub-id

# 3. Strikt policy på Production (Deny public storage)
az policy assignment create --name deny-public-storage \\
    --policy "Deny public blob access on storage accounts" \\
    --scope /providers/Microsoft.Management/managementGroups/mg-production \\
    --enforcement-mode Default

# 4. Audit policy på Development
az policy assignment create --name audit-public-storage \\
    --policy "Deny public blob access on storage accounts" \\
    --scope /providers/Microsoft.Management/managementGroups/mg-development \\
    --enforcement-mode DoNotEnforce

# 5. Require Environment tag
az policy assignment create --name require-env-tag \\
    --policy "Require a tag on resources" \\
    --scope /providers/Microsoft.Management/managementGroups/mg-production \\
    --params '{"tagName": {"value": "Environment"}}'

# 6. Budget med alert (Portal: Cost Management -> Budgets)""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
