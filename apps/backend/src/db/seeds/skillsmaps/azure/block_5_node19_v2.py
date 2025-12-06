"""
Azure Block 5 Node 19: Microsoft Defender for Cloud - V2 Interactive Format
"""

AZURE_NODE_19_DEFENDER_V2 = {
    "node_id": 19,
    "title": "Microsoft Defender for Cloud",
    "slug": "azure-defender-cloud",
    "description": "Cloud security posture management och workload protection",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Microsoft Defender for Cloud",
            "content": {
                "headline": "Security that keeps pace with your cloud",
                "hook": "Defender for Cloud ger CSPM (posture management) och CWPP (workload protection) med Secure Score, recommendations och alerts.",
                "learning_objectives": [
                    "Förstå CSPM vs CWPP och free vs paid tiers",
                    "Använda Secure Score för säkerhetsmätning",
                    "Aktivera Defender plans för workload protection",
                    "Hantera security recommendations och alerts"
                ],
                "prerequisites": ["Azure fundamentals", "Basic security concepts"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Defender Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Free vs Paid Tiers",
                        "explanation": "Free: Secure Score, recommendations, asset inventory. Paid (per resource): JIT access, vulnerability scanning, security alerts, compliance dashboards.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ FREE (CSPM Basic)                           │
├─────────────────────────────────────────────┤
│ ✓ Secure Score   ✓ Recommendations         │
│ ✓ Asset inventory ✓ Azure best practices   │
├─────────────────────────────────────────────┤
│ PAID (CWPP) - per resource                  │
├─────────────────────────────────────────────┤
│ Servers ~$15/mo │ SQL ~$15/mo              │
│ Containers ~$7  │ Storage ~$0.02/10k       │
│ + JIT, Vuln scan, Alerts, Compliance       │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Börja med free tier - aktivera paid för kritiska workloads.",
                        "common_mistake": "Att aktivera alla Defender plans utan kostnadskalkyl."
                    },
                    {
                        "title": "Secure Score",
                        "explanation": "Procent (0-100%) som mäter säkerhetsläget. Varje recommendation har poäng. Uppdateras var 24:e timme.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ SECURE SCORE: 67%                           │
├─────────────────────────────────────────────┤
│ Controls:                                   │
│ • Enable MFA              +10 points        │
│ • Encrypt data at rest    +8 points         │
│ • Restrict network access +5 points         │
│ • Enable Azure Defender   +15 points        │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Fokusera på High severity recommendations först.",
                        "common_mistake": "Att jaga 100% score - vissa recommendations passar inte alla miljöer."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Defender",
            "content": {
                "exercises": [
                    {
                        "task": "Visa Secure Score",
                        "instruction": "Lista secure score för subscription",
                        "expected_command": "az security secure-score list --output table",
                        "hint": "Score visas per control area"
                    },
                    {
                        "task": "Lista recommendations",
                        "instruction": "Visa high severity security recommendations",
                        "expected_command": "az security recommendation list --query \"[?severity=='High']\" --output table",
                        "hint": "Filtrera på High, Medium, Low severity"
                    },
                    {
                        "task": "Aktivera Defender for Servers",
                        "instruction": "Aktivera paid plan för Virtual Machines",
                        "expected_command": "az security pricing create --name VirtualMachines --tier Standard",
                        "hint": "Standard = paid tier, Free = basic"
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
                        {"front": "Vad är skillnaden mellan CSPM och CWPP?", "back": "CSPM = Cloud Security Posture Management (konfiguration). CWPP = Cloud Workload Protection Platform (runtime protection)."},
                        {"front": "Vad är Secure Score?", "back": "Procentuell mätning av säkerhetsläget baserat på implementerade recommendations"},
                        {"front": "Vad gör JIT VM Access?", "back": "Just-In-Time access - öppnar VM-portar temporärt vid begäran istället för permanent"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad ingår i free tier av Defender for Cloud?",
                            "options": ["JIT access", "Vulnerability scanning", "Secure Score och recommendations", "Security alerts"],
                            "correct": 2,
                            "explanation": "Free tier ger Secure Score, recommendations och asset inventory"
                        },
                        {
                            "question": "Hur ofta uppdateras Secure Score?",
                            "options": ["Real-time", "Var timme", "Var 24:e timme", "Manuellt"],
                            "correct": 2,
                            "explanation": "Secure Score uppdateras var 24:e timme"
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
            "title": "Defender Challenge",
            "content": {
                "scenario": "Implementera security baseline för en produktionsmiljö.",
                "requirements": [
                    "Aktivera Defender for Servers och SQL",
                    "Granska och åtgärda top 3 High severity recommendations",
                    "Konfigurera security alerts notification",
                    "Dokumentera Secure Score före och efter"
                ],
                "hints": [
                    "az security pricing create för aktivering",
                    "Portal: Defender for Cloud → Recommendations",
                    "Security contacts för alert notifications"
                ],
                "solution": """# 1. Visa nuvarande score
az security secure-score list --output table

# 2. Aktivera Defender plans
az security pricing create --name VirtualMachines --tier Standard
az security pricing create --name SqlServers --tier Standard

# 3. Lista High severity recommendations
az security recommendation list --query "[?severity=='High']" --output table

# 4. Konfigurera security contacts
az security contact create --email security@company.com --name default \\
    --alert-notifications on --alerts-to-admins on

# 5. Vanliga remediations:
# - Enable MFA: Portal → Entra ID → Security → MFA
# - Encrypt disks: az vm encryption enable
# - Network security: NSG rules, Private Endpoints
# - Enable audit logs: Diagnostic settings

# 6. Verifiera score efter 24h
az security secure-score list --output table""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
