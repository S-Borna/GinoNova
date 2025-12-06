"""
Linux Mastery Node 9: Package Management - V2 Interactive Format
"""

LINUX_NODE_9_PACKAGES_V2 = {
    "node_id": 9,
    "title": "Package Management",
    "slug": "package-management",
    "description": "Installera och hantera programvara",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Package Management",
            "content": {
                "headline": "Första steget på en ny server: uppdatera paket",
                "hook": "Package management är hur du får programvara på Linux och håller systemet säkert med uppdateringar. apt, yum, dnf - du måste kunna dem.",
                "learning_objectives": [
                    "Använda apt/apt-get för Debian/Ubuntu",
                    "Använda yum/dnf för RHEL/CentOS/Fedora",
                    "Hantera repositories och GPG-nycklar",
                    "Felsöka dependency-problem"
                ],
                "prerequisites": ["Basic terminal usage"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Package Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "apt (Debian/Ubuntu)",
                        "explanation": "apt update (hämta paketlista), apt upgrade (uppgradera), apt install (installera), apt remove (ta bort), apt autoremove (städa).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ APT WORKFLOW                                │
├─────────────────────────────────────────────┤
│ apt update         │ Hämta ny paketlista    │
│ apt upgrade        │ Uppgradera alla paket │
│ apt install pkg    │ Installera paket      │
│ apt remove pkg     │ Ta bort paket         │
│ apt autoremove     │ Ta bort oanvända deps │
│ apt search term    │ Sök paket             │
│ apt show pkg       │ Visa paketinfo        │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "apt update && apt upgrade -y för att köra båda i ett steg.",
                        "common_mistake": "Att glömma 'apt update' innan install - du får gamla versioner!"
                    },
                    {
                        "title": "yum/dnf (RHEL/CentOS)",
                        "explanation": "dnf är nya yum (RHEL 8+). Samma syntax: dnf install, dnf update, dnf remove. EPEL repo ger extra paket.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ DNF/YUM WORKFLOW                            │
├─────────────────────────────────────────────┤
│ dnf check-update   │ Visa tillgängliga upd │
│ dnf update         │ Uppgradera alla       │
│ dnf install pkg    │ Installera            │
│ dnf remove pkg     │ Ta bort               │
│ dnf search term    │ Sök                   │
│ dnf info pkg       │ Visa info             │
│ dnf history        │ Visa historik         │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "dnf history undo <id> kan ångra en installation!",
                        "common_mistake": "Att blanda yum och dnf - håll dig till en."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Packages",
            "content": {
                "exercises": [
                    {
                        "task": "Uppdatera paketlista",
                        "instruction": "Hämta senaste paketinformation (Debian/Ubuntu)",
                        "expected_command": "sudo apt update",
                        "hint": "update hämtar listan, upgrade installerar"
                    },
                    {
                        "task": "Installera paket",
                        "instruction": "Installera nginx webbserver",
                        "expected_command": "sudo apt install -y nginx",
                        "hint": "-y svarar 'yes' automatiskt"
                    },
                    {
                        "task": "Sök efter paket",
                        "instruction": "Sök efter paket relaterade till 'python'",
                        "expected_command": "apt search python3",
                        "hint": "search kräver inte sudo"
                    },
                    {
                        "task": "Visa paketinfo",
                        "instruction": "Visa information om nginx-paketet",
                        "expected_command": "apt show nginx",
                        "hint": "show visar version, dependencies, description"
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
                        {"front": "Skillnad mellan apt update och apt upgrade?", "back": "update hämtar paketlista, upgrade installerar nya versioner"},
                        {"front": "Vad gör apt autoremove?", "back": "Tar bort paket som installerats som dependencies men inte längre behövs"},
                        {"front": "Vilken pakethanterare använder Ubuntu?", "back": "apt (baserat på dpkg)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken fil innehåller apt repositories på Ubuntu?",
                            "options": ["/etc/apt/sources.list", "/etc/yum.repos.d/", "/etc/packages", "/var/apt/sources"],
                            "correct": 0,
                            "explanation": "sources.list och sources.list.d/ innehåller apt repositories"
                        },
                        {
                            "question": "Hur installerar du specifik version av ett paket?",
                            "options": ["apt install pkg", "apt install pkg=version", "apt install pkg --version", "apt install pkg@version"],
                            "correct": 1,
                            "explanation": "apt install nginx=1.18.0-0ubuntu1 installerar specifik version"
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
            "title": "Package Challenge",
            "content": {
                "scenario": "Sätt upp en utvecklingsmiljö med nödvändiga paket.",
                "requirements": [
                    "Uppdatera systemet fullständigt",
                    "Installera build-essential, git, curl, vim",
                    "Lägg till en extern repository (t.ex. Docker)",
                    "Installera paket från den nya repo:n"
                ],
                "hints": [
                    "apt update && apt upgrade",
                    "apt install pkg1 pkg2 pkg3",
                    "Lägg till GPG-nyckel med curl | gpg"
                ],
                "solution": """# 1. Uppdatera system
sudo apt update && sudo apt upgrade -y

# 2. Installera dev-tools
sudo apt install -y build-essential git curl vim wget

# 3. Lägg till Docker repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# 4. Installera Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# 5. Verifiera
docker --version""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
