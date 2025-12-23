"""
NOD 2.8: Systemd & Services
===========================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
SISTA NODEN I MODUL 2 - LINUX SYSTEM KOMPLETT!
"""

SYSTEMD_NODE = {
    "title": "Systemd & Services",
    "slug": "systemd-services",
    "description": "Init-system, tjänsthantering med systemctl, egna service-filer och journalctl.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "order_index": 8,
    "content": r"""# Systemd & Services

> **TL;DR:** `systemctl enable --now tjänst` = aktivera vid boot + starta direkt. `systemctl daemon-reload` efter ändringar i service-filer!

---

## 📖 TEORI: Vad är systemd?

**systemd** - Modern init-system för Linux
- Första processen som startar (PID 1)
- Hanterar ALLA tjänster (services)
- Ersätter gamla SysVinit

### Init-system evolution

```
SysVinit (gammalt) → Upstart → systemd (modern standard)
```

### Varför systemd?

| Funktion | SysVinit | systemd |
|----------|----------|---------|
| Parallell start | Nej | Ja (snabbare boot) |
| Beroenden | Manuellt | Automatiskt |
| Loggar | Spridda filer | journalctl (centralt) |
| Schemaläggning | cron separat | Timers inbyggt |

---

## 📖 Grundläggande systemctl-kommandon

### Status

```bash
# Detaljerad status
systemctl status sshd

# Snabbkoll
systemctl is-active sshd      # active/inactive
systemctl is-enabled sshd     # enabled/disabled
systemctl is-failed sshd      # failed/active
```

### Starta och stoppa

```bash
# Starta tjänst
sudo systemctl start sshd

# Stoppa tjänst
sudo systemctl stop sshd

# Starta om (stop + start)
sudo systemctl restart sshd

# Ladda om config (utan omstart)
sudo systemctl reload sshd
```

### Aktivera vid boot

```bash
# Starta automatiskt vid boot
sudo systemctl enable sshd

# INTE starta vid boot
sudo systemctl disable sshd

# Enable + start direkt (VANLIGAST!)
sudo systemctl enable --now sshd
```

### Lista tjänster

```bash
# Alla laddade tjänster
systemctl list-units --type=service

# Bara körande
systemctl list-units --type=service --state=running

# Alla installerade (även inaktiva)
systemctl list-unit-files --type=service

# Misslyckade tjänster
systemctl --failed
```

---

## 📖 Viktiga tjänster att känna till

| Tjänst | Beskrivning | Distro |
|--------|-------------|--------|
| sshd | SSH-server | Alla |
| docker | Docker daemon | Alla |
| firewalld | Brandvägg | Fedora/RHEL |
| ufw | Brandvägg | Ubuntu |
| nginx | Webbserver | Alla |
| apache2/httpd | Webbserver | Ubuntu/Fedora |
| cron/crond | Schemalagda jobb | Alla |
| systemd-resolved | DNS-resolver | Alla |
| NetworkManager | Nätverkshantering | Alla |

---

## 📖 Skapa egen systemd service (VIKTIGT!)

### Var placeras service-filer?

| Plats | Användning |
|-------|------------|
| /etc/systemd/system/ | **Custom services** (dina egna) |
| /lib/systemd/system/ | System services (pakethanteraren) |

### Grundläggande service-fil struktur

```ini
# /etc/systemd/system/mitt-program.service

[Unit]
Description=Min Custom Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/mitt-skript.sh
Restart=on-failure
User=nobody
Group=nobody

[Install]
WantedBy=multi-user.target
```

### Sektioner förklarade

**[Unit]** - Metadata och beroenden
```ini
[Unit]
Description=Beskrivning av tjänsten
After=network.target        # Starta EFTER nätverk
Requires=docker.service     # Kräver docker
Wants=redis.service         # Vill ha redis (ej krav)
```

**[Service]** - Hur tjänsten körs
```ini
[Service]
Type=simple                 # Processtyp
ExecStart=/path/to/program  # Kommando att köra
ExecStop=/path/to/stop      # Stopp-kommando (valfritt)
Restart=on-failure          # Restart-policy
User=www-data               # Kör som användare
WorkingDirectory=/app       # Arbetskatalog
Environment=NODE_ENV=prod   # Miljövariabler
```

**[Install]** - När tjänsten aktiveras
```ini
[Install]
WantedBy=multi-user.target  # Normalt boot-mål
```

### Service-typer (Type=)

| Type | Beskrivning |
|------|-------------|
| simple | Default. Processen ÄR tjänsten |
| forking | Processen forkar (traditionella daemons) |
| oneshot | Körs en gång och avslutas |
| notify | Som simple men signalerar när redo |

### Restart-policies

| Policy | När startar om? |
|--------|-----------------|
| no | Aldrig |
| on-failure | Vid fel (exit code != 0) |
| always | Alltid (även vid normal exit) |
| on-abnormal | Vid crash/signal |
| on-abort | Vid abort signal |

---

## 📖 Aktivera efter ändringar

```bash
# VIKTIGT! Efter varje ändring i service-fil:
sudo systemctl daemon-reload

# Sedan aktivera och starta
sudo systemctl enable --now mitt-program.service

# Kolla status
sudo systemctl status mitt-program.service
```

---

## 📖 Loggar med journalctl

### Grundläggande

```bash
# Alla loggar
journalctl

# Loggar för specifik tjänst
journalctl -u sshd
journalctl -u docker

# Följ loggar i realtid (-f = follow)
journalctl -u nginx -f

# Senaste N rader
journalctl -u nginx -n 50
journalctl -u nginx -n 100
```

### Filtrera på tid

```bash
# Loggar sedan senaste boot
journalctl -b

# Loggar från föregående boot
journalctl -b -1

# Loggar för viss tidsperiod
journalctl --since "2025-12-23 10:00"
journalctl --since "1 hour ago"
journalctl --since "2025-12-23 10:00" --until "2025-12-23 12:00"
```

### Praktiska flaggor

```bash
# Visa bara errors
journalctl -p err

# Visa kernel-meddelanden
journalctl -k

# Output som JSON
journalctl -u nginx -o json-pretty
```

---

## 📖 Timers (systemd schemaläggning)

### Ersätter cron!

**Service-fil (vad som ska köras):**
```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Daglig backup

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

**Timer-fil (när det ska köras):**
```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Kör backup dagligen

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

### OnCalendar-format

| Värde | Betydelse |
|-------|-----------|
| daily | Varje dag 00:00 |
| weekly | Varje vecka |
| monthly | Varje månad |
| hourly | Varje timme |
| *:0/15 | Var 15:e minut |
| Mon *-*-* 10:00 | Måndag 10:00 |

### Aktivera timer

```bash
# Aktivera timer (inte service!)
sudo systemctl enable --now backup.timer

# Lista alla timers
systemctl list-timers

# Kolla specifik timer
systemctl status backup.timer
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Enkel Bash-tjänst

```bash
#!/usr/bin/env bash
# /usr/local/bin/hello-service.sh

while true; do
    echo "Hello från service! $(date)"
    sleep 60
done
```

```ini
# /etc/systemd/system/hello.service
[Unit]
Description=Hello World Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/hello-service.sh
Restart=always
User=nobody

[Install]
WantedBy=multi-user.target
```

```bash
# Aktivera
sudo chmod +x /usr/local/bin/hello-service.sh
sudo systemctl daemon-reload
sudo systemctl enable --now hello.service
sudo systemctl status hello.service
journalctl -u hello.service -f
```

### Exempel 2: Docker container som service (GRUPPPROJEKT!)

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Docker Application
Requires=docker.service
After=docker.service

[Service]
Type=simple
Restart=always
RestartSec=10
ExecStartPre=-/usr/bin/docker stop myapp
ExecStartPre=-/usr/bin/docker rm myapp
ExecStart=/usr/bin/docker run --rm --name myapp -p 8080:80 nginx
ExecStop=/usr/bin/docker stop myapp

[Install]
WantedBy=multi-user.target
```

```bash
# Aktivera
sudo systemctl daemon-reload
sudo systemctl enable --now myapp.service

# Verifiera
sudo systemctl status myapp.service
curl localhost:8080
```

### Exempel 3: Node.js applikation

```ini
# /etc/systemd/system/nodeapp.service
[Unit]
Description=Node.js Application
After=network.target

[Service]
Type=simple
User=nodejs
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/node server.js
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```

### Exempel 4: Komplett backup-timer

```bash
#!/usr/bin/env bash
# /usr/local/bin/backup.sh
DATE=$(date +%Y-%m-%d)
tar -czvf /backup/home_${DATE}.tar.gz /home/
```

```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Home Directory Backup

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
# Aktivera timer
sudo chmod +x /usr/local/bin/backup.sh
sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer
systemctl list-timers | grep backup
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | systemctl status sshd visar? | Detaljerad info om tjänsten |
| 2 | systemctl enable --now gör? | Enable vid boot + start direkt |
| 3 | systemctl daemon-reload gör? | Laddar om service-filer efter ändringar |
| 4 | Var placeras custom services? | /etc/systemd/system/ |
| 5 | Type=simple betyder? | Processen ÄR tjänsten (default) |
| 6 | Restart=on-failure gör? | Startar om vid exit code != 0 |
| 7 | journalctl -u nginx -f gör? | Följer nginx-loggar i realtid |
| 8 | WantedBy=multi-user.target betyder? | Startar vid normalt boot |
| 9 | After=network.target gör? | Startar EFTER nätverk är uppe |
| 10 | systemctl list-timers visar? | Alla schemalagda timers |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är systemd?**
- A) En texteditor
- B) Init-system som hanterar tjänster ✅
- C) En brandvägg
- D) En pakethanterare

**2. Hur startar du en tjänst och aktiverar vid boot i ett kommando?**
- A) systemctl start --enable
- B) systemctl enable --now ✅
- C) systemctl activate
- D) systemctl boot

**3. Var placerar du custom service-filer?**
- A) /lib/systemd/system/
- B) /etc/systemd/system/ ✅
- C) /var/systemd/
- D) /usr/systemd/

**4. Vad MÅSTE du köra efter att ha ändrat en service-fil?**
- A) systemctl reload
- B) systemctl restart
- C) systemctl daemon-reload ✅
- D) systemctl refresh

**5. Vilken Type är default?**
- A) forking
- B) simple ✅
- C) oneshot
- D) notify

**6. Restart=on-failure startar om när?**
- A) Alltid
- B) Aldrig
- C) Vid exit code != 0 ✅
- D) Endast vid crash

**7. Hur följer du loggar i realtid?**
- A) journalctl -u nginx --live
- B) journalctl -u nginx -f ✅
- C) journalctl -u nginx --follow
- D) journalctl -u nginx -r

**8. Vad gör After=docker.service?**
- A) Stoppar efter docker
- B) Startar EFTER docker ✅
- C) Kräver docker
- D) Installerar docker

**9. Hur listar du alla aktiva timers?**
- A) systemctl timers
- B) systemctl list-timers ✅
- C) timerctl list
- D) journalctl --timers

**10. OnCalendar=daily kör när?**
- A) Varje timme
- B) Varje dag 00:00 ✅
- C) Varje vecka
- D) Varje månad

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Utforska systemd
```bash
# 1. Lista alla körande tjänster
systemctl list-units --type=service --state=running

# 2. Kolla SSH-status
systemctl status sshd

# 3. Kolla om enabled vid boot
systemctl is-enabled sshd

# 4. Visa misslyckade tjänster
systemctl --failed
```

### Övning 2: Skapa enkel service
```bash
# 1. Skapa skript
sudo tee /usr/local/bin/testservice.sh << 'EOF'
#!/bin/bash
while true; do
    echo "Test service running: $(date)" >> /tmp/testservice.log
    sleep 30
done
EOF

sudo chmod +x /usr/local/bin/testservice.sh

# 2. Skapa service-fil
sudo tee /etc/systemd/system/testservice.service << 'EOF'
[Unit]
Description=Test Service

[Service]
Type=simple
ExecStart=/usr/local/bin/testservice.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# 3. Aktivera
sudo systemctl daemon-reload
sudo systemctl start testservice

# 4. Verifiera
systemctl status testservice
tail -f /tmp/testservice.log

# 5. Städa
sudo systemctl stop testservice
sudo systemctl disable testservice
sudo rm /etc/systemd/system/testservice.service
sudo rm /usr/local/bin/testservice.sh
sudo systemctl daemon-reload
```

### Övning 3: journalctl
```bash
# 1. Visa alla loggar sedan boot
journalctl -b

# 2. Filtrera på tjänst
journalctl -u sshd -n 20

# 3. Visa errors
journalctl -p err -n 50

# 4. Loggar senaste timmen
journalctl --since "1 hour ago"

# 5. Följ systemloggar live
journalctl -f
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Glömma daemon-reload | Ändringar ignoreras | Alltid efter fil-ändringar! |
| Fel path i ExecStart | Service startar inte | Använd absoluta paths |
| Glömma [Install] | enable fungerar inte | Lägg till WantedBy |
| enable utan --now | Startar inte direkt | Använd enable --now |

---

## 📝 SAMMANFATTNING

```bash
# STATUS
systemctl status tjänst
systemctl is-active tjänst
systemctl is-enabled tjänst

# STARTA/STOPPA
sudo systemctl start tjänst
sudo systemctl stop tjänst
sudo systemctl restart tjänst

# BOOT-AKTIVERING
sudo systemctl enable tjänst      # Aktivera vid boot
sudo systemctl enable --now tjänst # Enable + start
sudo systemctl disable tjänst     # Avaktivera

# EFTER ÄNDRINGAR I SERVICE-FIL
sudo systemctl daemon-reload

# LISTA
systemctl list-units --type=service
systemctl list-units --type=service --state=running
systemctl --failed

# LOGGAR
journalctl -u tjänst           # Loggar för tjänst
journalctl -u tjänst -f        # Följ live
journalctl -u tjänst -n 50     # Senaste 50 rader
journalctl -b                  # Sedan boot
journalctl --since "1 hour ago"

# TIMERS
systemctl list-timers
sudo systemctl enable --now backup.timer

# SERVICE-FIL STRUKTUR
# /etc/systemd/system/myservice.service
[Unit]
Description=Min tjänst
After=network.target

[Service]
Type=simple
ExecStart=/path/to/program
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

""",
    "quiz": [
        {
            "question": "Vad är systemd?",
            "options": [
                "En texteditor",
                "Init-system som hanterar tjänster",
                "En brandvägg",
                "En pakethanterare"
            ],
            "correct": 1,
            "explanation": "systemd är Linux moderna init-system (PID 1) som startar och hanterar alla tjänster."
        },
        {
            "question": "Hur startar du en tjänst och aktiverar vid boot i ett kommando?",
            "options": [
                "systemctl start --enable",
                "systemctl enable --now",
                "systemctl activate",
                "systemctl boot"
            ],
            "correct": 1,
            "explanation": "--now flaggan kombinerar enable (boot) med start (direkt)."
        },
        {
            "question": "Var placerar du custom service-filer?",
            "options": [
                "/lib/systemd/system/",
                "/etc/systemd/system/",
                "/var/systemd/",
                "/usr/systemd/"
            ],
            "correct": 1,
            "explanation": "/etc/systemd/system/ är för dina egna custom services."
        },
        {
            "question": "Vad MÅSTE du köra efter att ha ändrat en service-fil?",
            "options": [
                "systemctl reload",
                "systemctl restart",
                "systemctl daemon-reload",
                "systemctl refresh"
            ],
            "correct": 2,
            "explanation": "daemon-reload läser om alla service-filer från disk."
        },
        {
            "question": "Vilken Type är default i [Service]?",
            "options": [
                "forking",
                "simple",
                "oneshot",
                "notify"
            ],
            "correct": 1,
            "explanation": "Type=simple är default - processen ÄR tjänsten."
        },
        {
            "question": "Restart=on-failure startar om när?",
            "options": [
                "Alltid",
                "Aldrig",
                "Vid exit code != 0",
                "Endast vid crash"
            ],
            "correct": 2,
            "explanation": "on-failure startar om vid icke-noll exit code (fel)."
        },
        {
            "question": "Hur följer du loggar i realtid?",
            "options": [
                "journalctl -u nginx --live",
                "journalctl -u nginx -f",
                "journalctl -u nginx --follow",
                "journalctl -u nginx -r"
            ],
            "correct": 1,
            "explanation": "-f (follow) visar nya loggrader i realtid."
        },
        {
            "question": "Vad gör After=docker.service?",
            "options": [
                "Stoppar efter docker",
                "Startar EFTER docker",
                "Kräver docker",
                "Installerar docker"
            ],
            "correct": 1,
            "explanation": "After anger startordning - väntar på docker först."
        },
        {
            "question": "Hur listar du alla aktiva timers?",
            "options": [
                "systemctl timers",
                "systemctl list-timers",
                "timerctl list",
                "journalctl --timers"
            ],
            "correct": 1,
            "explanation": "list-timers visar alla schemalagda systemd timers."
        },
        {
            "question": "OnCalendar=daily kör när?",
            "options": [
                "Varje timme",
                "Varje dag 00:00",
                "Varje vecka",
                "Varje månad"
            ],
            "correct": 1,
            "explanation": "daily = varje dag kl 00:00."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
SYSTEMD_FLASHCARDS = [
    {"front": "systemctl status sshd visar?", "back": "Detaljerad info om tjänsten"},
    {"front": "systemctl enable --now gör?", "back": "Enable vid boot + start direkt"},
    {"front": "systemctl daemon-reload gör?", "back": "Laddar om service-filer efter ändringar"},
    {"front": "Var placeras custom services?", "back": "/etc/systemd/system/"},
    {"front": "Type=simple betyder?", "back": "Processen ÄR tjänsten (default)"},
    {"front": "Type=oneshot betyder?", "back": "Körs en gång och avslutas"},
    {"front": "Type=forking betyder?", "back": "Processen forkar (traditionella daemons)"},
    {"front": "Restart=on-failure gör?", "back": "Startar om vid exit code != 0"},
    {"front": "Restart=always gör?", "back": "Startar alltid om"},
    {"front": "journalctl -u nginx -f gör?", "back": "Följer nginx-loggar i realtid"},
    {"front": "journalctl -b visar?", "back": "Loggar sedan boot"},
    {"front": "journalctl -n 50 gör?", "back": "Visar senaste 50 rader"},
    {"front": "WantedBy=multi-user.target betyder?", "back": "Startar vid normalt boot"},
    {"front": "After=network.target gör?", "back": "Startar EFTER nätverk är uppe"},
    {"front": "Requires=docker.service gör?", "back": "Kräver att docker körs"},
    {"front": "systemctl list-timers visar?", "back": "Alla schemalagda timers"},
    {"front": "OnCalendar=daily betyder?", "back": "Varje dag kl 00:00"},
    {"front": "systemctl is-enabled visar?", "back": "Om tjänsten startar vid boot"},
    {"front": "systemctl --failed visar?", "back": "Alla misslyckade tjänster"},
    {"front": "ExecStart= anger?", "back": "Kommandot som startar tjänsten"},
]
