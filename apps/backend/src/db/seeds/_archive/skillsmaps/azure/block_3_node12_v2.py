"""
Azure Block 3 Node 12: Azure Cache for Redis - V2 Interactive Format
"""

AZURE_NODE_12_REDIS_V2 = {
    "node_id": 12,
    "title": "Azure Cache for Redis",
    "slug": "azure-redis-cache",
    "description": "High-performance caching med Redis",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Cache for Redis",
            "content": {
                "headline": "Snabbaste sättet att inte slå databasen",
                "hook": "Redis caching ger microsekund-latency - 100x snabbare än databas. Minska DB-load och få dramatisk prestanda-boost.",
                "learning_objectives": [
                    "Förstå caching patterns (Cache-Aside, Write-Through)",
                    "Skapa och konfigurera Azure Redis Cache",
                    "Implementera session management och rate limiting",
                    "Använda Redis datatyper effektivt"
                ],
                "prerequisites": ["Azure fundamentals", "Grundläggande programmering"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Redis Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Cache-Aside Pattern",
                        "explanation": "1) Kolla cache först. 2) Om miss -> hämta från DB. 3) Spara i cache med TTL. 4) Returnera data.",
                        "diagram": """
+--------+     +-----+     +--------+
| Client |----->| App |----->| Redis  | Cache hit? Return!
+--------+     +-----+     +--------+
                  |              ↑
                  ↓ Cache miss   |
              +--------+         |
              |   DB   |---------+ Store in cache
              +--------+""",
                        "pro_tip": "Sätt alltid TTL för att undvika stale data.",
                        "common_mistake": "Att glömma cache invalidation vid DB-uppdateringar."
                    },
                    {
                        "title": "Redis Tiers",
                        "explanation": "Basic (dev/test, ingen SLA), Standard (99.9% SLA, replicas), Premium (clustering, VNet), Enterprise (99.999%, Redis modules).",
                        "diagram": """
+---------------------------------------------+
| Basic      | Dev/test, 250MB+, ingen SLA    |
| Standard   | HA replicas, 99.9% SLA         |
| Premium    | Clustering, VNet, zones        |
| Enterprise | 99.999%, Active-geo, modules   |
+---------------------------------------------+""",
                        "pro_tip": "Standard C1 (~$40/mån) räcker för de flesta appar.",
                        "common_mistake": "Att använda Basic i produktion - ingen HA!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Redis Cache",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa Redis Cache",
                        "instruction": "Skapa Standard tier Redis 'redis-demo' med C1 storlek",
                        "expected_command": "az redis create --name redis-demo --resource-group rg-demo --location northeurope --sku Standard --vm-size c1",
                        "hint": "Standard ger HA med replicas"
                    },
                    {
                        "task": "Hämta access keys",
                        "instruction": "Visa Redis access keys",
                        "expected_command": "az redis list-keys --name redis-demo --resource-group rg-demo",
                        "hint": "list-keys visar primary och secondary keys"
                    },
                    {
                        "task": "Visa connection info",
                        "instruction": "Hämta hostname och SSL port",
                        "expected_command": "az redis show --name redis-demo --resource-group rg-demo --query '{Host:hostName,Port:sslPort}'",
                        "hint": "Använd --query för att filtrera output"
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
                        {"front": "Vad är Cache-Aside pattern?", "back": "Kolla cache först, vid miss hämta från DB och spara i cache med TTL"},
                        {"front": "Varför använda TTL?", "back": "Förhindrar stale data och säkerställer att cache uppdateras periodiskt"},
                        {"front": "Vad är Redis Sorted Set bra för?", "back": "Leaderboards, rankings, top-N queries med automatisk sortering"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilket Redis tier bör du använda i produktion?",
                            "options": ["Basic", "Standard eller högre", "Spelar ingen roll", "Endast Enterprise"],
                            "correct": 1,
                            "explanation": "Standard eller högre ger HA med replicas och SLA"
                        },
                        {
                            "question": "Hur implementerar du rate limiting med Redis?",
                            "options": ["GET/SET", "INCR med EXPIRE", "LPUSH/LPOP", "HSET/HGET"],
                            "correct": 1,
                            "explanation": "INCR är atomic och kombinerat med EXPIRE ger sliding window rate limiting"
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
            "title": "Redis Challenge",
            "content": {
                "scenario": "Implementera session management och rate limiting för en web app.",
                "requirements": [
                    "Skapa Premium Redis med zone redundancy",
                    "Designa session storage med TTL",
                    "Implementera rate limiting (100 req/min per user)",
                    "Planera för cache invalidation"
                ],
                "hints": [
                    "Premium tier stöder zones",
                    "Session key format: session:{session_id}",
                    "Rate limit key: ratelimit:{user_id}"
                ],
                "solution": """# Premium Redis med zones
az redis create --name redis-prod --resource-group rg-demo --location northeurope \\
    --sku Premium --vm-size p1 --zones 1 2 3

# Python session implementation
import redis
import json
import uuid

r = redis.Redis(host='redis-prod.redis.cache.windows.net', port=6380, password='key', ssl=True)

# Session management
def create_session(user_id):
    session_id = str(uuid.uuid4())
    r.setex(f'session:{session_id}', 86400, json.dumps({'user_id': user_id}))
    return session_id

# Rate limiting
def check_rate_limit(user_id, max_req=100, window=60):
    key = f'ratelimit:{user_id}'
    current = r.incr(key)
    if current == 1:
        r.expire(key, window)
    return current <= max_req""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
