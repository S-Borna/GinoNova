"""
Azure Block 3 Node 11: Azure Cosmos DB - V2 Interactive Format
"""

AZURE_NODE_11_COSMOS_V2 = {
    "node_id": 11,
    "title": "Azure Cosmos DB",
    "slug": "azure-cosmos-db",
    "description": "Globally distributed NoSQL database",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Cosmos DB",
            "content": {
                "headline": "Single-digit millisecond latency, anywhere in the world",
                "hook": "Cosmos DB är Azures flagship NoSQL med 99.999% SLA, global distribution och multi-model support.",
                "learning_objectives": [
                    "Förstå Cosmos DB arkitektur och partition keys",
                    "Hantera Request Units (RU) och kostnadsoptimering",
                    "Konfigurera consistency levels",
                    "Implementera global distribution"
                ],
                "prerequisites": ["Azure fundamentals", "Grundläggande NoSQL-förståelse"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Cosmos DB Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Partition Keys",
                        "explanation": "Partition key bestämmer hur data distribueras. Bra val: userId, customerId, tenantId. Dåliga val: country, status (låg kardinalitet).",
                        "diagram": """
+---------------------------------------------+
| Account -> Database -> Container -> Items      |
+---------------------------------------------+
| Container: orders                           |
| Partition key: /customerId                  |
| +-- Partition A (cust-001)                  |
| +-- Partition B (cust-002)                  |
| +-- Partition C (cust-003)                  |
+---------------------------------------------+""",
                        "pro_tip": "Partition key kan INTE ändras efteråt - välj rätt från början!",
                        "common_mistake": "Att använda datum som partition key skapar hot partitions."
                    },
                    {
                        "title": "Request Units (RU)",
                        "explanation": "RU är Cosmos DB valuta. Read 1KB = ~1 RU. Write 1KB = ~5 RU. Cross-partition query = dyrt!",
                        "diagram": """
+---------------------------------------------+
| OPERATION                     COST          |
+---------------------------------------------+
| Read 1KB by ID + partition    ~1 RU         |
| Read 1KB by query             ~3 RU         |
| Write 1KB                     ~5 RU         |
| Cross-partition query         10-100+ RU    |
+---------------------------------------------+""",
                        "pro_tip": "Autoscale (400-4000 RU) är bäst för variabel workload.",
                        "common_mistake": "Cross-partition queries utan partition key kostar extremt mycket."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Cosmos DB",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa Cosmos DB account",
                        "instruction": "Skapa account 'cosmos-demo' med Session consistency",
                        "expected_command": "az cosmosdb create --name cosmos-demo --resource-group rg-demo --locations regionName=northeurope --default-consistency-level Session",
                        "hint": "Session consistency är default och bäst för de flesta appar"
                    },
                    {
                        "task": "Skapa databas",
                        "instruction": "Skapa databas 'appdb'",
                        "expected_command": "az cosmosdb sql database create --account-name cosmos-demo --resource-group rg-demo --name appdb",
                        "hint": "Använd 'sql database create' för SQL API"
                    },
                    {
                        "task": "Skapa container med partition key",
                        "instruction": "Skapa container 'users' med partition key /userId och autoscale 4000 RU",
                        "expected_command": "az cosmosdb sql container create --account-name cosmos-demo --resource-group rg-demo --database-name appdb --name users --partition-key-path /userId --max-throughput 4000",
                        "hint": "--max-throughput aktiverar autoscale"
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
                        {"front": "Varför är partition key viktigt?", "back": "Bestämmer data-distribution, prestanda och skalbarhet. Kan ej ändras efteråt."},
                        {"front": "Vad är Request Units (RU)?", "back": "Cosmos DB throughput-valuta. Kombinerar CPU, IOPS och minne."},
                        {"front": "Vilka consistency levels finns?", "back": "Strong, Bounded Staleness, Session (default), Consistent Prefix, Eventual"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilket är det billigaste sättet att läsa ett dokument?",
                            "options": ["Query utan filter", "Point read med ID + partition key", "Cross-partition query", "Full scan"],
                            "correct": 1,
                            "explanation": "Point read med ID och partition key kostar endast ~1 RU"
                        },
                        {
                            "question": "Vad är bästa partition key för orders i e-commerce?",
                            "options": ["orderDate", "status", "customerId", "country"],
                            "correct": 2,
                            "explanation": "customerId ger hög kardinalitet och queries är oftast per kund"
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
            "title": "Cosmos DB Challenge",
            "content": {
                "scenario": "Bygg en global e-commerce databas med låg latency i både Europa och USA.",
                "requirements": [
                    "Skapa Cosmos account med multi-region",
                    "Aktivera multi-region writes",
                    "Skapa container med rätt partition key för orders",
                    "Konfigurera autoscale throughput"
                ],
                "hints": [
                    "Använd --locations flera gånger för multi-region",
                    "--enable-multiple-write-locations true",
                    "customerId är bra partition key för orders"
                ],
                "solution": """# Multi-region Cosmos account
az cosmosdb create --name cosmos-global --resource-group rg-demo \\
    --locations regionName=northeurope failoverPriority=0 \\
    --locations regionName=eastus failoverPriority=1 \\
    --enable-multiple-write-locations true \\
    --default-consistency-level Session

# Databas
az cosmosdb sql database create --account-name cosmos-global --resource-group rg-demo --name ecomdb

# Container med autoscale
az cosmosdb sql container create --account-name cosmos-global --resource-group rg-demo \\
    --database-name ecomdb --name orders \\
    --partition-key-path /customerId \\
    --max-throughput 10000""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
