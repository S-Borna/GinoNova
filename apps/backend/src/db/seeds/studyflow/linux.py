"""
Linux Studyflow Data
Flashcards och Multiple Choice för Linux-modulen
"""

LINUX_MODULE = {
    "slug": "linux",
    "title": "Linux Mastery",
    "description": "Komplett Linux-kurs för DevOps",
    "icon": "Terminal",
    "topics": [
        {
            "id": "linux-basics",
            "title": "Linux Basics",
            "flashcards": [
                {"front": "Vad gör kommandot 'pwd'?", "back": "Print Working Directory - visar nuvarande katalog"},
                {"front": "Vad gör kommandot 'ls -la'?", "back": "Listar alla filer inkl. dolda (-a) i långt format (-l)"},
                {"front": "Vad är skillnaden mellan relativ och absolut sökväg?", "back": "Absolut börjar från / (root), relativ från nuvarande katalog"},
                {"front": "Vad gör 'cd ..'?", "back": "Går upp en katalognivå till parent directory"},
                {"front": "Vad är ~ i Linux?", "back": "Home-katalogen för nuvarande användare"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilket kommando visar nuvarande katalog?",
                    "options": ["cd", "pwd", "ls", "dir"],
                    "correct": 1,
                    "explanation": "pwd (Print Working Directory) visar den fullständiga sökvägen till nuvarande katalog."
                },
                {
                    "question": "Vad betyder flaggan -a i 'ls -a'?",
                    "options": ["Alla detaljer", "Alla filer inkl. dolda", "Alfabetisk ordning", "Arkivläge"],
                    "correct": 1,
                    "explanation": "Flaggan -a (all) visar alla filer, inklusive dolda filer som börjar med punkt."
                },
            ]
        },
        {
            "id": "linux-filesystem",
            "title": "Filesystem Hierarchy",
            "flashcards": [
                {"front": "Vad innehåller /etc?", "back": "Systemkonfigurationsfiler"},
                {"front": "Vad innehåller /var?", "back": "Variabel data - loggar, cache, spool"},
                {"front": "Vad innehåller /home?", "back": "Användarnas hemkataloger"},
                {"front": "Vad innehåller /tmp?", "back": "Temporära filer som rensas vid omstart"},
                {"front": "Vad innehåller /usr?", "back": "User programs - applikationer och bibliotek"},
                {"front": "Vad innehåller /bin?", "back": "Essential binaries - grundläggande kommandon"},
            ],
            "multiple_choice": [
                {
                    "question": "Var lagras systemloggar i Linux?",
                    "options": ["/etc/logs", "/var/log", "/home/logs", "/tmp/log"],
                    "correct": 1,
                    "explanation": "/var/log innehåller systemloggar som syslog, auth.log, kern.log etc."
                },
                {
                    "question": "Vilken katalog innehåller systemkonfiguration?",
                    "options": ["/config", "/etc", "/sys", "/settings"],
                    "correct": 1,
                    "explanation": "/etc (et cetera) innehåller alla systemkonfigurationsfiler."
                },
            ]
        },
        {
            "id": "linux-permissions",
            "title": "File Permissions",
            "flashcards": [
                {"front": "Vad betyder rwx?", "back": "Read (4), Write (2), Execute (1)"},
                {"front": "Vad är chmod 755?", "back": "rwxr-xr-x - Ägare full access, andra kan läsa/köra"},
                {"front": "Vad är chmod 644?", "back": "rw-r--r-- - Ägare läs/skriv, andra bara läsa"},
                {"front": "Vad gör chown?", "back": "Change Owner - ändrar ägare av fil/katalog"},
                {"front": "Vad gör chgrp?", "back": "Change Group - ändrar gruppägare"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad betyder permission 777?",
                    "options": ["Ingen access", "Bara läsning", "Full access för alla", "Bara ägaren har access"],
                    "correct": 2,
                    "explanation": "777 = rwxrwxrwx - full läs/skriv/kör-access för ägare, grupp och andra."
                },
                {
                    "question": "Vilket kommando ändrar filrättigheter?",
                    "options": ["chown", "chmod", "chgrp", "perm"],
                    "correct": 1,
                    "explanation": "chmod (change mode) ändrar filrättigheter."
                },
            ]
        },
        {
            "id": "linux-processes",
            "title": "Process Management",
            "flashcards": [
                {"front": "Vad gör 'ps aux'?", "back": "Visar alla körande processer med detaljer"},
                {"front": "Vad gör 'top'?", "back": "Realtidsvy av processer och systemresurser"},
                {"front": "Vad gör 'kill -9 PID'?", "back": "Tvingar avslut av process (SIGKILL)"},
                {"front": "Vad är PID?", "back": "Process ID - unikt nummer för varje process"},
                {"front": "Vad gör 'htop'?", "back": "Interaktiv processhanterare (bättre än top)"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilken signal skickar 'kill -9'?",
                    "options": ["SIGTERM", "SIGKILL", "SIGHUP", "SIGINT"],
                    "correct": 1,
                    "explanation": "kill -9 skickar SIGKILL som tvingar omedelbar avslutning utan cleanup."
                },
                {
                    "question": "Vad visar kommandot 'top'?",
                    "options": ["Filsystem", "Nätverkstrafik", "Processer i realtid", "Diskutrymme"],
                    "correct": 2,
                    "explanation": "top visar processer, CPU-användning, minne i realtid."
                },
            ]
        },
        {
            "id": "linux-networking",
            "title": "Networking",
            "flashcards": [
                {"front": "Vad gör 'ip addr'?", "back": "Visar nätverksinterface och IP-adresser"},
                {"front": "Vad gör 'ping'?", "back": "Testar nätverksanslutning till en host"},
                {"front": "Vad gör 'netstat -tulpn'?", "back": "Visar aktiva nätverksanslutningar och portar"},
                {"front": "Vad gör 'ss -tulpn'?", "back": "Modern ersättare för netstat - visar sockets"},
                {"front": "Vad gör 'curl'?", "back": "Hämtar data från URL:er via HTTP/HTTPS"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilket kommando testar nätverksanslutning?",
                    "options": ["wget", "curl", "ping", "ssh"],
                    "correct": 2,
                    "explanation": "ping skickar ICMP-paket för att testa om en host är nåbar."
                },
                {
                    "question": "Vad ersätter 'ifconfig' i moderna Linux-system?",
                    "options": ["ipconfig", "ip", "netstat", "route"],
                    "correct": 1,
                    "explanation": "Kommandot 'ip' (ip addr, ip route) ersätter ifconfig i moderna system."
                },
            ]
        },
        {
            "id": "linux-services",
            "title": "Systemd & Services",
            "flashcards": [
                {"front": "Vad gör 'systemctl status nginx'?", "back": "Visar status för nginx-tjänsten"},
                {"front": "Vad gör 'systemctl enable nginx'?", "back": "Aktiverar nginx att starta vid boot"},
                {"front": "Vad gör 'systemctl restart nginx'?", "back": "Startar om nginx-tjänsten"},
                {"front": "Vad gör 'journalctl -u nginx'?", "back": "Visar loggar för nginx-tjänsten"},
                {"front": "Vad är en unit-fil?", "back": "Konfigurationsfil för systemd-tjänster (.service)"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur startar man om en tjänst i systemd?",
                    "options": ["service restart nginx", "systemctl restart nginx", "nginx restart", "/etc/init.d/nginx restart"],
                    "correct": 1,
                    "explanation": "systemctl restart <service> är det moderna sättet i systemd."
                },
                {
                    "question": "Var finns systemd unit-filer?",
                    "options": ["/etc/services", "/etc/systemd/system", "/var/systemd", "/lib/init"],
                    "correct": 1,
                    "explanation": "Custom unit-filer placeras i /etc/systemd/system/"
                },
            ]
        },
        {
            "id": "linux-packages",
            "title": "Package Management",
            "flashcards": [
                {"front": "Vad gör 'apt update'?", "back": "Uppdaterar paketlistor från repositories"},
                {"front": "Vad gör 'apt upgrade'?", "back": "Uppgraderar installerade paket"},
                {"front": "Vad gör 'apt install nginx'?", "back": "Installerar nginx-paketet"},
                {"front": "Vad gör 'apt remove nginx'?", "back": "Avinstallerar nginx men behåller config"},
                {"front": "Skillnad apt vs apt-get?", "back": "apt är nyare med bättre output, apt-get för scripts"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilken pakethanterare används i Debian/Ubuntu?",
                    "options": ["yum", "dnf", "apt", "pacman"],
                    "correct": 2,
                    "explanation": "apt (Advanced Package Tool) används i Debian-baserade system."
                },
                {
                    "question": "Vad ska man köra innan 'apt upgrade'?",
                    "options": ["apt install", "apt update", "apt clean", "apt search"],
                    "correct": 1,
                    "explanation": "apt update hämtar senaste paketlistor innan upgrade."
                },
            ]
        },
        {
            "id": "linux-ssh",
            "title": "SSH & Remote Access",
            "flashcards": [
                {"front": "Vad gör 'ssh user@host'?", "back": "Ansluter till remote host via SSH"},
                {"front": "Vad gör 'ssh-keygen'?", "back": "Genererar SSH-nyckelpar (public/private)"},
                {"front": "Var lagras SSH-nycklar?", "back": "~/.ssh/ (id_rsa, id_rsa.pub)"},
                {"front": "Vad är authorized_keys?", "back": "Fil med publika nycklar som får ansluta"},
                {"front": "Vad gör 'scp'?", "back": "Secure Copy - kopierar filer över SSH"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilken port använder SSH som standard?",
                    "options": ["21", "22", "23", "80"],
                    "correct": 1,
                    "explanation": "SSH använder port 22 som standard."
                },
                {
                    "question": "Vilken fil innehåller tillåtna publika nycklar?",
                    "options": ["~/.ssh/id_rsa", "~/.ssh/authorized_keys", "~/.ssh/known_hosts", "~/.ssh/config"],
                    "correct": 1,
                    "explanation": "authorized_keys innehåller publika nycklar som får logga in."
                },
            ]
        },
    ]
}
