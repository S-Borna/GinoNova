"""
Linux Mastery Node 12: Networking Basics - V2 Interactive Format
"""

LINUX_NODE_12_NETWORKING_V2 = {
    "node_id": 12,
    "title": "Networking Basics",
    "slug": "networking",
    "description": "IP-adresser, interfaces, portar och connectivity",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Networking Basics",
            "content": {
                "headline": "Något kan inte ansluta - var är problemet?",
                "hook": "Varje modern applikation är nätverksberoende. API-anrop, databasanslutningar, load balancers - allt beror på nätverk. När något inte kan ansluta måste du diagnostisera: DNS? Firewall? Routing?",
                "learning_objectives": [
                    "Visa och hantera nätverksinterfaces med ip-kommandot",
                    "Testa connectivity med ping och traceroute",
                    "Analysera portar och connections med ss",
                    "Felsöka nätverksproblem systematiskt"
                ],
                "prerequisites": ["Basic terminal usage"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Networking Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "ip - Network Interfaces",
                        "explanation": "ip-kommandot ersätter ifconfig. 'ip addr' visar interfaces och IP-adresser, 'ip route' visar routing.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ IP ADDR OUTPUT                                      │
├─────────────────────────────────────────────────────┤
│ $ ip addr                                           │
│ 1: lo: <LOOPBACK,UP>                               │
│     inet 127.0.0.1/8 scope host lo                 │
│ 2: eth0: <BROADCAST,UP>                            │
│     inet 192.168.1.10/24 scope global eth0         │
├─────────────────────────────────────────────────────┤
│ IP KOMMANDON                                        │
│ ip addr          │ Visa alla interfaces            │
│ ip route         │ Visa routing table              │
│ ip link show     │ Visa link-status                │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "'ip a' är kortform för 'ip addr show'",
                        "common_mistake": "Att använda ifconfig på moderna system - det är deprecated!"
                    },
                    {
                        "title": "ss - Socket Statistics",
                        "explanation": "ss visar nätverksanslutningar och lyssnande portar. Ersätter netstat. -t=TCP, -u=UDP, -l=listening, -n=numerisk, -p=process.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ SS KOMMANDON                                        │
├─────────────────────────────────────────────────────┤
│ ss -tuln        │ Alla lyssnande TCP/UDP-portar    │
│ ss -tulnp       │ Med process-info (kräver sudo)   │
│ ss -tun         │ Etablerade connections           │
│ ss -tuln|grep :80│ Filtrera på port 80             │
├─────────────────────────────────────────────────────┤
│ FLAGS:                                              │
│ -t = TCP    -u = UDP    -l = Listening             │
│ -n = Numeric (port nr)  -p = Process               │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "sudo ss -tulnp visar vilken process som lyssnar på varje port",
                        "common_mistake": "Att glömma -n och få service-namn istället för portnummer."
                    },
                    {
                        "title": "Connectivity Testing",
                        "explanation": "ping testar om en host är nåbar. traceroute visar vägen genom nätverket. Kombination ger komplett bild.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ DEBUGGING FLOW                                      │
├─────────────────────────────────────────────────────┤
│ 1. ping -c 4 8.8.8.8     │ Fungerar internet?      │
│ 2. ping -c 4 google.com  │ Fungerar DNS?           │
│ 3. traceroute google.com │ Var fastnar trafiken?   │
│ 4. ss -tuln              │ Lyssnar tjänsten?       │
│ 5. nc -zv host 443       │ Är porten öppen?        │
├─────────────────────────────────────────────────────┤
│ mtr google.com = ping + traceroute kombinerat      │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "mtr ger live-uppdaterad traceroute - perfekt för att hitta intermittenta problem!",
                        "common_mistake": "Att bara testa DNS (hostname) - börja med IP (8.8.8.8) för att isolera problemet."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Networking",
            "content": {
                "exercises": [
                    {
                        "task": "Visa IP-adresser",
                        "instruction": "Lista alla nätverksinterfaces med deras IP-adresser",
                        "expected_command": "ip addr",
                        "hint": "ip a är en kortform"
                    },
                    {
                        "task": "Visa lyssnande portar",
                        "instruction": "Visa alla TCP/UDP-portar som lyssnar",
                        "expected_command": "ss -tuln",
                        "hint": "-t=TCP, -u=UDP, -l=listening, -n=numeric"
                    },
                    {
                        "task": "Testa connectivity",
                        "instruction": "Pinga Google 4 gånger",
                        "expected_command": "ping -c 4 google.com",
                        "hint": "-c begränsar antal paket"
                    },
                    {
                        "task": "Visa routing",
                        "instruction": "Visa routingtabellen och identifiera default gateway",
                        "expected_command": "ip route",
                        "hint": "Titta efter raden som börjar med 'default'"
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
                        {"front": "Vad visar 'ip route | grep default'?", "back": "Din default gateway - den router som används för trafik utanför lokalt nät"},
                        {"front": "Skillnad mellan ss -l och ss utan -l?", "back": "-l visar lyssnande (servrar), utan -l visar etablerade connections"},
                        {"front": "Vad gör traceroute?", "back": "Visar varje hop/router mellan dig och målet - perfekt för att hitta var trafik fastnar"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken port använder HTTPS som default?",
                            "options": ["80", "443", "8080", "22"],
                            "correct": 1,
                            "explanation": "443 är standard för HTTPS, 80 är HTTP, 22 är SSH"
                        },
                        {
                            "question": "Hur testar du om port 443 är öppen på en server?",
                            "options": ["ping server:443", "traceroute server 443", "nc -zv server 443", "ss server 443"],
                            "correct": 2,
                            "explanation": "nc (netcat) med -zv testar om en port är öppen och visar resultatet"
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
            "title": "Network Challenge",
            "content": {
                "scenario": "En applikation rapporterar 'Connection refused'. Diagnostisera nätverksproblemet systematiskt.",
                "requirements": [
                    "Verifiera att du har nätverksanslutning",
                    "Kontrollera att DNS fungerar",
                    "Hitta vilka tjänster som lyssnar lokalt",
                    "Testa om måltjänsten är nåbar"
                ],
                "hints": [
                    "Börja med grundläggande ping till IP",
                    "Testa sedan DNS med host/dig",
                    "Använd ss för lokala portar",
                    "nc för att testa remote port"
                ],
                "solution": """# 1. Har jag nätverksanslutning?
ip addr  # Har jag IP?
ping -c 2 8.8.8.8  # Fungerar internet?

# 2. Fungerar DNS?
ping -c 2 google.com
host google.com

# 3. Vilka tjänster lyssnar lokalt?
ss -tulnp

# 4. Är måltjänsten nåbar?
# Antag att vi ska nå server.example.com:443
ping -c 2 server.example.com
nc -zv server.example.com 443

# 5. Traceroute om ping fungerar men nc misslyckas
traceroute server.example.com

# 6. Om lokalt, kolla att tjänsten lyssnar
ss -tuln | grep :443

# Common issues:
# - Tjänsten lyssnar på 127.0.0.1 istället för 0.0.0.0
# - Firewall blockerar porten
# - DNS ger fel IP""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
