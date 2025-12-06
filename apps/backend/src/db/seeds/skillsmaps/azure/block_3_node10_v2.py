"""
Azure Block 3 Node 10: Azure SQL Database - V2 Interactive Format
"""

AZURE_NODE_10_SQL_V2 = {
    "node_id": 10,
    "title": "Azure SQL Database",
    "slug": "azure-sql-database",
    "description": "Managed relational database i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        # SECTION 1: INTRO
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure SQL Database",
            "content": {
                "headline": "Din databas, hanterad av Microsoft",
                "hook": "Azure SQL ger dig enterprise-grade databas med 99.99% SLA utan att du behöver hantera patching, backups eller HA.",
                "learning_objectives": [
                    "Förstå skillnaden mellan SQL Database, Elastic Pool och Managed Instance",
                    "Skapa och konfigurera Azure SQL databaser",
                    "Implementera geo-replication och backup-strategier",
                    "Optimera prestanda med rätt pricing tier"
                ],
                "prerequisites": ["Azure fundamentals", "Grundläggande SQL-kunskap"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        # SECTION 2: CONCEPTS
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "SQL Database Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Azure SQL Options",
                        "explanation": "Azure SQL Database (PaaS single DB), Elastic Pool (delad kapacitet för SaaS), Managed Instance (närmast on-prem SQL Server), SQL Server på VM (IaaS full kontroll).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│         AZURE SQL OPTIONS                   │
├─────────────────────────────────────────────┤
│ SQL Database    │ Enklast, per-databas pris │
│ Elastic Pool    │ Dela resurser, SaaS       │
│ Managed Instance│ Lift-and-shift migration  │
│ SQL on VM       │ Full kontroll, IaaS       │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Serverless-läge för SQL Database auto-pausar och sparar pengar på dev/test.",
                        "common_mistake": "Att välja Managed Instance när SQL Database räcker - MI kostar mycket mer."
                    },
                    {
                        "title": "Pricing Tiers",
                        "explanation": "DTU-modell (Basic/Standard/Premium) bundlar resurser enkelt. vCore-modell (General Purpose/Business Critical) ger mer flexibilitet med separata CPU/storage-inställningar.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ DTU Model       │ vCore Model               │
├─────────────────────────────────────────────┤
│ Bundled CPU/IO  │ Separate CPU & Storage    │
│ Enklare prissätt│ Mer flexibelt             │
│ Från ~$5/mån    │ Från ~$30/mån             │
│ Basic/Std/Prem  │ GenPurpose/BusinessCrit   │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "DTU S0 (~$15/mån) räcker för de flesta små appar.",
                        "common_mistake": "Att välja för stor tier från början - skala upp när behov finns."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        # SECTION 3: PRACTICE
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on SQL Database",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa en SQL Server (logical server)",
                        "instruction": "Skapa SQL Server 'sqlserver-demo' i resource group 'rg-demo' med admin 'sqladmin'",
                        "expected_command": "az sql server create --name sqlserver-demo --resource-group rg-demo --location northeurope --admin-user sqladmin --admin-password 'SecureP@ss123!'",
                        "hint": "Använd --admin-user och --admin-password för credentials"
                    },
                    {
                        "task": "Skapa en SQL Database",
                        "instruction": "Skapa databas 'mydb' med S0 service tier",
                        "expected_command": "az sql db create --name mydb --resource-group rg-demo --server sqlserver-demo --service-objective S0",
                        "hint": "--service-objective bestämmer prestanda-tier"
                    },
                    {
                        "task": "Konfigurera firewall",
                        "instruction": "Tillåt Azure services att ansluta",
                        "expected_command": "az sql server firewall-rule create --name AllowAzure --resource-group rg-demo --server sqlserver-demo --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0",
                        "hint": "0.0.0.0 till 0.0.0.0 tillåter Azure services"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        # SECTION 4: QUIZ
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Vad är skillnaden mellan DTU och vCore?", "back": "DTU bundlar resurser i paket, vCore ger separat kontroll över CPU och storage"},
                        {"front": "Vad gör serverless SQL Database?", "back": "Auto-pausar databasen när den inte används och skalas automatiskt vid behov"},
                        {"front": "Hur fungerar geo-replication?", "back": "Skapar läs-replicas i andra regioner för DR och read offloading"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken Azure SQL option är bäst för SaaS multi-tenant appar?",
                            "options": ["SQL Database", "Elastic Pool", "Managed Instance", "SQL on VM"],
                            "correct": 1,
                            "explanation": "Elastic Pool låter flera databaser dela resurser kostnadseffektivt"
                        },
                        {
                            "question": "Vad händer vid Azure SQL automatisk backup?",
                            "options": ["Endast manuell backup", "Full weekly, diff 12h, log 5-10min", "Endast transaction logs", "Ingen backup inkluderad"],
                            "correct": 1,
                            "explanation": "Azure SQL tar automatiskt full backup varje vecka, differential var 12:e timme, och transaction log var 5-10:e minut"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        # SECTION 5: CHALLENGE
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "SQL Database Challenge",
            "content": {
                "scenario": "Du bygger en produktionsdatabas för en e-commerce app som behöver hög tillgänglighet.",
                "requirements": [
                    "Skapa SQL Server med Azure AD authentication",
                    "Skapa databas med General Purpose vCore tier",
                    "Konfigurera geo-replication till secondary region",
                    "Sätt upp firewall rules för din IP"
                ],
                "hints": [
                    "Använd --edition GeneralPurpose för vCore",
                    "az sql db replica create för geo-replication",
                    "az sql server ad-admin create för Azure AD"
                ],
                "solution": """# Skapa primary server
az sql server create --name sql-ecom-primary --resource-group rg-demo --location northeurope --admin-user sqladmin --admin-password 'SecureP@ss!'

# Skapa databas med vCore
az sql db create --name ecomdb --resource-group rg-demo --server sql-ecom-primary --edition GeneralPurpose --compute-model Provisioned --family Gen5 --capacity 2

# Skapa secondary server
az sql server create --name sql-ecom-secondary --resource-group rg-demo --location westeurope --admin-user sqladmin --admin-password 'SecureP@ss!'

# Geo-replication
az sql db replica create --name ecomdb --resource-group rg-demo --server sql-ecom-primary --partner-server sql-ecom-secondary""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
