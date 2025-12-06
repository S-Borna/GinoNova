"""
Linux Mastery Node 15: SSH & Remote Access - V2 Interactive Format
"""

LINUX_NODE_15_SSH_V2 = {
    "node_id": 15,
    "title": "SSH & Remote Access",
    "slug": "ssh-remote",
    "description": "Säker fjärråtkomst med SSH, nycklar och tunneling",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "SSH & Remote Access",
            "content": {
                "headline": "SSH är hur du kommer åt servrar. Punkt.",
                "hook": "Varje produktionsserver, varje cloud-instans, varje container - du når dem genom SSH. Behärska SSH och du kan hantera vad som helst, var som helst.",
                "learning_objectives": [
                    "Generera och använda SSH-nycklar",
                    "Konfigurera ~/.ssh/config för effektiv access",
                    "Kopiera filer säkert med scp och rsync",
                    "Skapa SSH-tunnlar för port forwarding"
                ],
                "prerequisites": ["Networking basics", "Basic terminal"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "SSH Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "SSH-nycklar",
                        "explanation": "Lösenord är osäkert - använd nycklar! Ed25519 är modernast och snabbast. Privata nyckeln SKA ALDRIG delas.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ SSH KEY WORKFLOW                                    │
├─────────────────────────────────────────────────────┤
│ 1. Generera nyckelpar                              │
│    ssh-keygen -t ed25519 -C "email@example.com"    │
│                                                     │
│ 2. Resultat:                                        │
│    ~/.ssh/id_ed25519      ← PRIVAT (skydda!)       │
│    ~/.ssh/id_ed25519.pub  ← Publik (dela fritt)    │
│                                                     │
│ 3. Kopiera publik till server                       │
│    ssh-copy-id user@server                         │
│                                                     │
│ 4. Nu kan du logga in utan lösenord                │
│    ssh user@server                                 │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "Använd passphrase på nyckeln + ssh-agent för bästa säkerhet!",
                        "common_mistake": "Fel permissions - .ssh måste vara 700, privat nyckel 600."
                    },
                    {
                        "title": "~/.ssh/config",
                        "explanation": "Spara host-inställningar så du slipper skriva långa kommandon. 'ssh prod' istället för 'ssh -p 2222 -i ~/.ssh/prod_key user@server.com'",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ ~/.ssh/config EXAMPLE                               │
├─────────────────────────────────────────────────────┤
│ Host prod                                           │
│     HostName production.example.com                 │
│     User deploy                                     │
│     Port 22                                         │
│     IdentityFile ~/.ssh/prod_key                   │
│                                                     │
│ Host dev                                            │
│     HostName dev.example.com                        │
│     User developer                                  │
│     Port 2222                                       │
│                                                     │
│ Host *                                              │
│     ServerAliveInterval 60                          │
│     ServerAliveCountMax 3                           │
├─────────────────────────────────────────────────────┤
│ ANVÄNDNING: ssh prod   ← Så enkelt!                │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "Host * gäller alla anslutningar - perfekt för globala inställningar",
                        "common_mistake": "Att glömma att Host-namn är case-sensitive."
                    },
                    {
                        "title": "Filkopiering & Tunneling",
                        "explanation": "scp för enkla kopior, rsync för synk/backup. SSH tunnels ger säker access till remote tjänster.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ KOPIERA FILER                                       │
├─────────────────────────────────────────────────────┤
│ scp file.txt user@host:/path/      │ Upload        │
│ scp user@host:/path/file.txt ./    │ Download      │
│ scp -r folder/ user@host:/path/    │ Rekursiv      │
│                                                     │
│ rsync -avz src/ user@host:/dest/   │ Synk (bäst)   │
│ rsync -avz --delete src/ host:/d/  │ Spegla exakt  │
├─────────────────────────────────────────────────────┤
│ SSH TUNNELING                                       │
├─────────────────────────────────────────────────────┤
│ # Lokal port → Remote service                       │
│ ssh -L 5432:localhost:5432 user@dbserver           │
│ # Nu: psql -h localhost -p 5432                    │
│                                                     │
│ # Remote port → Lokal service                       │
│ ssh -R 8080:localhost:80 user@server               │
│ # Server:8080 → Din maskin:80                      │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "rsync -n (dry-run) för att se vad som händer innan!",
                        "common_mistake": "scp -P (stor P) för port, ssh -p (liten p) - förvirrande!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on SSH",
            "content": {
                "exercises": [
                    {
                        "task": "Generera SSH-nyckel",
                        "instruction": "Skapa ett ed25519 nyckelpar",
                        "expected_command": "ssh-keygen -t ed25519",
                        "hint": "Lägg till -C 'email' för kommentar"
                    },
                    {
                        "task": "Visa publik nyckel",
                        "instruction": "Visa din publika SSH-nyckel",
                        "expected_command": "cat ~/.ssh/id_ed25519.pub",
                        "hint": "Den publika nyckeln slutar på .pub"
                    },
                    {
                        "task": "Kopiera fil till server",
                        "instruction": "Kopiera backup.tar.gz till /tmp på server 192.168.1.10",
                        "expected_command": "scp backup.tar.gz user@192.168.1.10:/tmp/",
                        "hint": "scp source destination"
                    },
                    {
                        "task": "Synka katalog",
                        "instruction": "Synka lokala ./logs/ till /var/backup/ på server med rsync",
                        "expected_command": "rsync -avz ./logs/ user@server:/var/backup/",
                        "hint": "-a=archive, -v=verbose, -z=compress"
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
                        {"front": "Vilken fil innehåller auktoriserade nycklar på servern?", "back": "~/.ssh/authorized_keys"},
                        {"front": "Vad gör ssh-copy-id?", "back": "Kopierar din publika nyckel till serverns authorized_keys"},
                        {"front": "Rätt permissions för privat SSH-nyckel?", "back": "600 (läs/skriv bara för ägare)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad gör 'ssh -L 3306:localhost:3306 user@db'?",
                            "options": [
                                "Startar MySQL lokalt",
                                "Tunnel: lokal port 3306 → remote MySQL",
                                "Kopierar MySQL-data",
                                "Listar databaser"
                            ],
                            "correct": 1,
                            "explanation": "-L skapar lokal tunnel så du kan nå remote MySQL via localhost:3306"
                        },
                        {
                            "question": "Vilken algoritm är rekommenderad för nya SSH-nycklar?",
                            "options": ["rsa", "dsa", "ed25519", "ecdsa"],
                            "correct": 2,
                            "explanation": "ed25519 är snabbast, säkrast och har kortast nycklar"
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
            "title": "SSH Challenge",
            "content": {
                "scenario": "Sätt upp lösenordsfri SSH-access till en server med säkra inställningar.",
                "requirements": [
                    "Generera ed25519 SSH-nyckel med passphrase",
                    "Kopiera nyckeln till servern",
                    "Skapa ~/.ssh/config för enkel access",
                    "Verifiera att du kan logga in med 'ssh myserver'",
                    "Sätt korrekta permissions på alla filer"
                ],
                "hints": [
                    "ssh-keygen -t ed25519",
                    "ssh-copy-id user@server",
                    "Skapa config med Host-block"
                ],
                "solution": """# 1. Generera nyckel med passphrase
ssh-keygen -t ed25519 -C "admin@company.com"
# Enter passphrase: ****

# 2. Sätt korrekta permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# 3. Kopiera till server
ssh-copy-id user@192.168.1.50

# 4. Skapa config
cat << 'EOF' >> ~/.ssh/config
Host myserver
    HostName 192.168.1.50
    User user
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
EOF

chmod 600 ~/.ssh/config

# 5. Testa
ssh myserver

# 6. (Bonus) Starta ssh-agent för att slippa skriva passphrase
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519

# 7. (Valfritt) Inaktivera lösenordsinloggning på servern
# På servern: sudo vim /etc/ssh/sshd_config
# PasswordAuthentication no
# sudo systemctl restart sshd""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
