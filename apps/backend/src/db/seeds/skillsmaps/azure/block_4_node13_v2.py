"""
Azure Block 4 Node 13: Azure DevOps Services - V2 Interactive Format
"""

AZURE_NODE_13_DEVOPS_V2 = {
    "node_id": 13,
    "title": "Azure DevOps Services",
    "slug": "azure-devops-services",
    "description": "DevOps-plattformen för planering, kodning och deployment",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure DevOps Services",
            "content": {
                "headline": "Plan smarter, collaborate better, ship faster",
                "hook": "Azure DevOps är komplett DevOps-plattform med Boards, Repos, Pipelines, Artifacts och Test Plans - allt integrerat.",
                "learning_objectives": [
                    "Förstå Azure DevOps komponenter och användning",
                    "Konfigurera organization och projekt",
                    "Sätta upp Repos med branch policies",
                    "Integrera med Azure resources via Service Connections"
                ],
                "prerequisites": ["Azure fundamentals", "Git basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Azure DevOps Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "DevOps Services",
                        "explanation": "Boards (agil planering), Repos (Git hosting), Pipelines (CI/CD), Artifacts (package management), Test Plans (testning).",
                        "diagram": """
+---------------------------------------------+
| ORGANIZATION -> PROJECT                      |
+---------------------------------------------+
| Boards    | Work items, Sprints, Kanban     |
| Repos     | Git hosting, PRs, Branch policy |
| Pipelines | Build, Release, YAML/Classic    |
| Artifacts | NuGet, npm, Maven, Python, Docker|
| Test Plans| Manual & automated testing      |
+---------------------------------------------+""",
                        "pro_tip": "Free tier ger 5 users och unlimited private repos.",
                        "common_mistake": "Att hoppa över branch policies - kräv PRs och code review!"
                    },
                    {
                        "title": "Service Connections",
                        "explanation": "Kopplar Azure DevOps till externa resurser som Azure subscriptions, Docker registries, Kubernetes clusters.",
                        "diagram": """
+---------------------------------------------+
| Azure DevOps --> Service Connection          |
+---------------------------------------------+
| Azure RM      | Deploy till Azure           |
| Docker Registry| Push/pull images           |
| Kubernetes    | Deploy till AKS             |
| GitHub        | Cross-platform CI           |
+---------------------------------------------+""",
                        "pro_tip": "Använd Service Principal med minsta nödvändiga permissions.",
                        "common_mistake": "Att ge Service Connection Owner-rättigheter på subscription."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Azure DevOps",
            "content": {
                "exercises": [
                    {
                        "task": "Installera Azure DevOps CLI extension",
                        "instruction": "Lägg till azure-devops extension till Azure CLI",
                        "expected_command": "az extension add --name azure-devops",
                        "hint": "Extensions lägger till nya funktioner i Azure CLI"
                    },
                    {
                        "task": "Konfigurera defaults",
                        "instruction": "Sätt default organization och projekt",
                        "expected_command": "az devops configure --defaults organization=https://dev.azure.com/myorg project=MyProject",
                        "hint": "Defaults sparar tid på framtida kommandon"
                    },
                    {
                        "task": "Lista projekt",
                        "instruction": "Visa alla projekt i organization",
                        "expected_command": "az devops project list --output table",
                        "hint": "--output table ger snygg formatering"
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
                        {"front": "Vad är Azure Boards?", "back": "Agil projekthantering med work items, sprints och Kanban boards"},
                        {"front": "Vad gör Service Connections?", "back": "Kopplar Azure DevOps till externa resurser som Azure subscriptions och Docker registries"},
                        {"front": "Vad är PAT (Personal Access Token)?", "back": "Autentiseringstoken för CLI/API access till Azure DevOps"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken komponent hanterar CI/CD i Azure DevOps?",
                            "options": ["Boards", "Repos", "Pipelines", "Artifacts"],
                            "correct": 2,
                            "explanation": "Pipelines hanterar build och release automation"
                        },
                        {
                            "question": "Vad ingår i Azure DevOps free tier?",
                            "options": ["1 user", "5 users + unlimited repos", "Endast public repos", "Ingen free tier"],
                            "correct": 1,
                            "explanation": "Free tier ger 5 users och unlimited private/public repos"
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
            "title": "Azure DevOps Challenge",
            "content": {
                "scenario": "Sätt upp ett nytt DevOps-projekt för ett utvecklingsteam.",
                "requirements": [
                    "Skapa organization och projekt",
                    "Konfigurera Git repo med branch policies",
                    "Kräv minst 1 reviewer på PRs till main",
                    "Skapa Service Connection till Azure"
                ],
                "hints": [
                    "Portal: dev.azure.com -> Create organization",
                    "Project Settings -> Repos -> Branch policies",
                    "Project Settings -> Service connections"
                ],
                "solution": """# 1. Skapa organization på dev.azure.com
# 2. Skapa projekt: New project -> Name, Visibility

# CLI setup
az extension add --name azure-devops
az devops configure --defaults organization=https://dev.azure.com/myorg project=MyProject

# Lista repos
az repos list --output table

# Branch policy via Portal:
# Repos -> Branches -> main -> ... -> Branch policies
# ✓ Require minimum number of reviewers: 1
# ✓ Check for linked work items
# ✓ Build validation (lägg till pipeline)

# Service Connection:
# Project Settings -> Service connections -> New
# Azure Resource Manager -> Service principal (automatic)""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
