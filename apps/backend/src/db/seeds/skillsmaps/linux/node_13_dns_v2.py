"""
Linux Mastery Node 13: DNS & Name Resolution - V2 Interactive Format
"""

LINUX_NODE_13_DNS_V2 = {
    "node_id": 13,
    "title": "DNS & Name Resolution",
    "slug": "dns-resolution",
    "description": "DNS-lookup, records och felsökning",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "DNS & Name Resolution",
            "content": {
                "headline": "DNS är internets telefonbok",
                "hook": "När DNS failar fungerar ingenting - användare kan inte nå din sajt, tjänster kan inte ansluta. Att förstå DNS är grundläggande för att felsöka connectivity-problem.",
                "learning_objectives": [
                    "Förstå hur DNS resolution fungerar",
                    "Använda dig, host och nslookup för lookups",
                    "Känna igen olika DNS record-typer",
                    "Felsöka DNS-problem"
                ],
                "prerequisites": ["Networking basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "DNS Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "DNS Resolution Flow",
                        "explanation": "DNS översätter hostname till IP. Systemet kollar: /etc/hosts → lokal cache → DNS resolver → internet.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ DNS RESOLUTION FLOW                                 │
├─────────────────────────────────────────────────────┤
│ User: "google.com"                                  │
│        │                                            │
│        ▼                                            │
│ 1. /etc/hosts         (lokal override)             │
│        │ (not found)                               │
│        ▼                                            │
│ 2. Local DNS cache    (tidigare lookups)           │
│        │ (not found)                               │
│        ▼                                            │
│ 3. DNS resolver       (/etc/resolv.conf)           │
│        │                                            │
│        ▼                                            │
│ 4. Internet: Root → .com → google.com              │
│        │                                            │
│        ▼                                            │
│ 5. Return IP: 142.250.185.78                       │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "/etc/hosts har högst prioritet - perfekt för lokala overrides!",
                        "common_mistake": "Att glömma att cache kan ge gamla svar - flush cache vid problem."
                    },
                    {
                        "title": "DNS Record Types",
                        "explanation": "Olika records har olika syften: A=IPv4, AAAA=IPv6, CNAME=alias, MX=mail, TXT=verifiering, NS=nameservers.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ DNS RECORD TYPES                                    │
├─────────────────────────────────────────────────────┤
│ A     │ example.com → 93.184.216.34    (IPv4)      │
│ AAAA  │ example.com → 2606:2800:...    (IPv6)      │
│ CNAME │ www.example.com → example.com  (alias)     │
│ MX    │ example.com → mail.example.com (mail)      │
│ TXT   │ SPF, DKIM, verifiering records             │
│ NS    │ example.com → ns1.example.com  (nameserv)  │
│ PTR   │ IP → hostname (reverse lookup)             │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "TXT records används för domänverifiering (Google, AWS, etc.)",
                        "common_mistake": "Att glömma att CNAME inte kan finnas på apex domain (example.com)."
                    },
                    {
                        "title": "dig - DNS Swiss Army Knife",
                        "explanation": "dig är det kraftfullaste DNS-verktyget. +short för bara svaret, specifik record-typ med A/MX/TXT etc.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ DIG KOMMANDON                                       │
├─────────────────────────────────────────────────────┤
│ dig example.com          │ Full DNS lookup         │
│ dig +short example.com   │ Bara IP-svaret          │
│ dig example.com A        │ Bara A-records          │
│ dig example.com MX       │ Mail servers            │
│ dig example.com TXT      │ TXT records             │
│ dig +trace example.com   │ Visa hela resolution    │
│ dig @8.8.8.8 example.com │ Fråga specifik DNS      │
│ dig -x 8.8.8.8           │ Reverse lookup          │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "@8.8.8.8 låter dig testa mot specifik DNS - perfekt för att jämföra!",
                        "common_mistake": "Att tro att DNS ändras direkt - TTL kan göra att gamla svar cachas."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on DNS",
            "content": {
                "exercises": [
                    {
                        "task": "Enkel DNS lookup",
                        "instruction": "Slå upp IP-adressen för google.com",
                        "expected_command": "dig +short google.com",
                        "hint": "+short ger bara IP utan extra info"
                    },
                    {
                        "task": "MX records",
                        "instruction": "Hitta mailservrar för gmail.com",
                        "expected_command": "dig gmail.com MX",
                        "hint": "MX records pekar på mail servers"
                    },
                    {
                        "task": "Specifik DNS-server",
                        "instruction": "Fråga Google DNS (8.8.8.8) om example.com",
                        "expected_command": "dig @8.8.8.8 example.com",
                        "hint": "@server anger vilken DNS att fråga"
                    },
                    {
                        "task": "Reverse lookup",
                        "instruction": "Hitta hostname för IP 8.8.8.8",
                        "expected_command": "dig -x 8.8.8.8",
                        "hint": "-x gör reverse lookup (IP → hostname)"
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
                        {"front": "Vad är TTL i DNS?", "back": "Time To Live - hur länge ett DNS-svar cachas innan ny lookup"},
                        {"front": "Skillnad mellan A och CNAME?", "back": "A pekar direkt på IP, CNAME är alias till annat hostname"},
                        {"front": "Var konfigureras DNS-servrar på Linux?", "back": "/etc/resolv.conf (eller via systemd-resolved)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken fil har högst prioritet för name resolution?",
                            "options": ["/etc/resolv.conf", "/etc/hosts", "~/.dns", "/etc/nsswitch.conf"],
                            "correct": 1,
                            "explanation": "/etc/hosts kollas först - lokal override för alla DNS"
                        },
                        {
                            "question": "Hur flushar du DNS cache i systemd-resolved?",
                            "options": ["dns-flush", "systemctl flush dns", "resolvectl flush-caches", "dig --flush"],
                            "correct": 2,
                            "explanation": "resolvectl flush-caches (eller sudo systemd-resolve --flush-caches)"
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
            "title": "DNS Challenge",
            "content": {
                "scenario": "DNS ger fel IP för en intern tjänst. Diagnostisera och åtgärda.",
                "requirements": [
                    "Jämför DNS-svar från olika servrar",
                    "Kontrollera lokal /etc/hosts",
                    "Verifiera vilken DNS din maskin använder",
                    "Lägg till en lokal override"
                ],
                "hints": [
                    "dig @server för att jämföra svar",
                    "cat /etc/hosts för lokala overrides",
                    "cat /etc/resolv.conf för DNS-servrar"
                ],
                "solution": """# 1. Vad svarar din lokala DNS?
dig myapp.internal.com

# 2. Jämför med annan DNS (t.ex. 8.8.8.8)
dig @8.8.8.8 myapp.internal.com

# 3. Kolla vilken DNS du använder
cat /etc/resolv.conf
# eller
resolvectl status

# 4. Kolla om det finns lokal override
cat /etc/hosts | grep myapp

# 5. Lägg till lokal override
echo "192.168.1.100 myapp.internal.com" | sudo tee -a /etc/hosts

# 6. Verifiera
ping myapp.internal.com

# 7. Flush cache om det inte fungerar direkt
resolvectl flush-caches

# 8. Om problemet är på DNS-server nivå
# Kontrollera med authoritative nameserver
dig +trace myapp.internal.com""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
