"""
NOD 2.4: Brandvägg - UFW (Ubuntu)
=================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

UFW_NODE = {
    "title": "Brandvägg - UFW (Ubuntu)",
    "slug": "brandvagg-ufw-ubuntu",
    "description": "Uncomplicated Firewall - enkel brandväggskonfiguration för Ubuntu.",
    "difficulty": "medium",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "order_index": 4,
    "content": r"""# Brandvägg - UFW (Ubuntu)

> **TL;DR:** `sudo ufw allow ssh` FÖRST, sedan `sudo ufw enable`. Glöm aldrig öppna SSH innan aktivering - annars låser du ut dig!

---

## 📖 TEORI: Vad är UFW?

**UFW = Uncomplicated Firewall**
- Frontend för iptables (enklare syntax)
- Standard i Ubuntu/Debian
- Filtrerar inkommande/utgående trafik

### Grundläggande koncept

| Riktning | Beskrivning | Default |
|----------|-------------|---------|
| INPUT | Inkommande trafik (till servern) | **BLOCKERA** |
| OUTPUT | Utgående trafik (från servern) | Tillåt |
| FORWARD | Trafik som passerar genom | Blockera |

---

## 📖 Grundläggande kommandon

### Aktivera/avaktivera

```bash
# Aktivera brandvägg
sudo ufw enable

# Avaktivera
sudo ufw disable

# Visa status
sudo ufw status

# Detaljerad status
sudo ufw status verbose

# Visa med radnummer (för borttagning)
sudo ufw status numbered
```

### ⚠️ SÄKER ORDNING VID AKTIVERING!

```bash
# 1. FÖRST - tillåt SSH (annars låser du ut dig!)
sudo ufw allow ssh

# 2. SEDAN - aktivera brandväggen
sudo ufw enable
```

---

## 📖 Tillåta trafik (allow)

### Portar och tjänster

```bash
# Tillåt port (TCP och UDP)
sudo ufw allow 22

# Endast TCP
sudo ufw allow 22/tcp

# Endast UDP
sudo ufw allow 53/udp

# Använd tjänstnamn
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# Flera portar
sudo ufw allow 80,443/tcp
```

### Port-range

```bash
# Tillåt portintervall
sudo ufw allow 6000:6010/tcp
```

### IP-baserade regler

```bash
# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100

# Tillåt subnät
sudo ufw allow from 192.168.1.0/24

# Tillåt IP till specifik port
sudo ufw allow from 192.168.1.100 to any port 22

# Tillåt subnät till port
sudo ufw allow from 10.0.0.0/8 to any port 3306
```

---

## 📖 Blockera trafik (deny)

```bash
# Blockera port
sudo ufw deny 23

# Blockera specifik IP
sudo ufw deny from 10.0.0.5

# Blockera IP från specifik port
sudo ufw deny from 10.0.0.5 to any port 22
```

---

## 📖 Ta bort regler

### Metod 1: Med nummer

```bash
# Visa regler med nummer
sudo ufw status numbered

# Output:
# Status: active
#      To                         Action      From
#      --                         ------      ----
# [ 1] 22/tcp                     ALLOW IN    Anywhere
# [ 2] 80/tcp                     ALLOW IN    Anywhere
# [ 3] 6622/tcp                   ALLOW IN    Anywhere

# Ta bort regel nummer 2
sudo ufw delete 2
```

### Metod 2: Med exakt regel

```bash
# Ta bort specifik allow-regel
sudo ufw delete allow 22

# Ta bort specifik deny-regel
sudo ufw delete deny 23
```

---

## 📖 Default policies

```bash
# Sätt default (rekommenderat)
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Visa default
sudo ufw status verbose
```

---

## 📖 Reset

```bash
# Återställ alla regler (börja om)
sudo ufw reset
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Initial setup

```bash
#!/usr/bin/env bash

# Sätt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Tillåt SSH (KRITISKT!)
sudo ufw allow ssh

# Tillåt HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Aktivera
sudo ufw enable

# Verifiera
sudo ufw status verbose
```

### Exempel 2: Byta SSH-port (22 → 6622)

```bash
#!/usr/bin/env bash

# 1. Kolla nuvarande status
sudo ufw status numbered

# 2. Tillåt NYA porten FÖRST!
sudo ufw allow 6622/tcp

# 3. Uppdatera SSH-config
sudo nano /etc/ssh/sshd_config.d/01-hardening.conf
# Port 6622

# 4. Starta om SSH
sudo systemctl restart ssh

# 5. TESTA NYA PORTEN (i nytt terminalfönster!)
ssh -p 6622 user@server

# 6. NÄR DET FUNGERAR - ta bort gamla porten
sudo ufw status numbered
sudo ufw delete allow 22/tcp
# eller
sudo ufw delete allow ssh

# 7. Verifiera
sudo ufw status numbered
```

### Exempel 3: Webserver med databasaccess

```bash
#!/usr/bin/env bash

# Publikt tillgängligt
sudo ufw allow 80/tcp      # HTTP
sudo ufw allow 443/tcp     # HTTPS

# SSH endast från admin-nätverk
sudo ufw allow from 10.0.1.0/24 to any port 22

# MySQL endast från app-servrar
sudo ufw allow from 10.0.2.0/24 to any port 3306

# Aktivera
sudo ufw enable
sudo ufw status verbose
```

### Exempel 4: Visa detaljerad status

```bash
sudo ufw status verbose

# Output:
# Status: active
# Logging: on (low)
# Default: deny (incoming), allow (outgoing), disabled (routed)
# New profiles: skip
#
# To                         Action      From
# --                         ------      ----
# 6622/tcp                   ALLOW IN    Anywhere
# 80/tcp                     ALLOW IN    Anywhere
# 443/tcp                    ALLOW IN    Anywhere
# 6622/tcp (v6)              ALLOW IN    Anywhere (v6)
# 80/tcp (v6)                ALLOW IN    Anywhere (v6)
# 443/tcp (v6)               ALLOW IN    Anywhere (v6)
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | ufw enable gör? | Aktiverar brandväggen |
| 2 | ufw allow ssh gör? | Tillåter SSH (port 22) |
| 3 | ufw status numbered visar? | Regler med radnummer |
| 4 | ufw delete 2 gör? | Tar bort regel nummer 2 |
| 5 | Säker ordning vid aktivering? | allow ssh FÖRST, sedan enable |
| 6 | ufw default deny incoming gör? | Blockerar all inkommande som standard |
| 7 | ufw allow 80,443/tcp gör? | Tillåter HTTP och HTTPS |
| 8 | ufw allow from IP gör? | Tillåter all trafik från IP |
| 9 | ufw reset gör? | Återställer alla regler |
| 10 | ufw deny vs ufw reject? | deny = tyst drop, reject = svarar med error |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad måste du göra INNAN du aktiverar UFW på en remote server?**
- A) Starta om servern
- B) Tillåta SSH ✅
- C) Avaktivera SELinux
- D) Skapa backup

**2. Vilket kommando aktiverar UFW?**
- A) ufw start
- B) ufw enable ✅
- C) systemctl start ufw
- D) ufw on

**3. Hur tillåter du endast TCP på port 443?**
- A) ufw allow 443
- B) ufw allow 443/tcp ✅
- C) ufw allow tcp 443
- D) ufw allow --tcp 443

**4. Hur tar du bort en regel?**
- A) ufw remove 22
- B) ufw delete allow 22 ✅
- C) ufw drop 22
- D) ufw clear 22

**5. Vad är default för inkommande trafik i UFW?**
- A) Tillåt allt
- B) Blockera allt ✅
- C) Logga allt
- D) Ingen default

**6. Hur visar du regler med nummer?**
- A) ufw status -n
- B) ufw status numbered ✅
- C) ufw list numbers
- D) ufw show numbered

**7. Hur tillåter du SSH endast från 192.168.1.0/24?**
- A) ufw allow ssh from 192.168.1.0/24
- B) ufw allow from 192.168.1.0/24 to any port 22 ✅
- C) ufw allow 22 192.168.1.0/24
- D) ufw allow ssh --source 192.168.1.0/24

**8. Vad gör ufw reset?**
- A) Startar om UFW-tjänsten
- B) Återställer till fabriksinställningar ✅
- C) Rensar loggarna
- D) Aktiverar UFW

**9. Vilken fil konfigurerar UFW permanent?**
- A) /etc/ufw/ufw.conf
- B) /etc/default/ufw ✅
- C) /etc/firewall/rules
- D) /etc/ufw.rules

**10. Vad händer om du kör ufw enable utan att tillåta SSH?**
- A) SSH tillåts automatiskt
- B) Du låses ut från servern ✅
- C) UFW vägrar aktivera
- D) SSH fungerar ändå

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande setup
```bash
# 1. Kontrollera status
sudo ufw status

# 2. Sätt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 3. Tillåt SSH
sudo ufw allow ssh

# 4. Aktivera (försiktigt!)
sudo ufw enable

# 5. Verifiera
sudo ufw status verbose
```

### Övning 2: Webserver-regler
```bash
# Lägg till HTTP och HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Visa med nummer
sudo ufw status numbered

# Ta bort HTTP (behåll bara HTTPS)
sudo ufw delete allow 80/tcp
```

### Övning 3: IP-baserade regler
```bash
# Tillåt MySQL endast från specifik IP
sudo ufw allow from 10.0.0.5 to any port 3306

# Verifiera
sudo ufw status

# Ta bort regeln
sudo ufw delete allow from 10.0.0.5 to any port 3306
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Aktivera utan allow ssh | Låses ut | ALLTID allow ssh först |
| Ta bort port 22 före nya porten testad | Låses ut | Testa nya porten först! |
| Glömma /tcp | Öppnar både TCP och UDP | Ange /tcp eller /udp |
| Glömma numbered | Vet inte vilken regel som ska tas bort | ufw status numbered |

---

## 📝 SAMMANFATTNING

```bash
# SÄKER ORDNING
sudo ufw allow ssh        # 1. FÖRST!
sudo ufw enable           # 2. Sedan aktivera

# GRUNDLÄGGANDE
sudo ufw status           # Visa status
sudo ufw status numbered  # Med nummer
sudo ufw status verbose   # Detaljerat

# TILLÅT
sudo ufw allow 22         # Port
sudo ufw allow 22/tcp     # Endast TCP
sudo ufw allow ssh        # Tjänstnamn
sudo ufw allow from IP    # Från IP
sudo ufw allow from IP to any port 22  # IP till port

# BLOCKERA
sudo ufw deny 23
sudo ufw deny from IP

# TA BORT
sudo ufw delete allow 22
sudo ufw delete 3         # Regel nummer 3

# RESET
sudo ufw reset

# DEFAULTS
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

""",
    "quiz": [
        {
            "question": "Vad måste du göra INNAN du aktiverar UFW på en remote server?",
            "options": [
                "Starta om servern",
                "Tillåta SSH",
                "Avaktivera SELinux",
                "Skapa backup"
            ],
            "correct": 1,
            "explanation": "Om du aktiverar UFW utan att tillåta SSH låser du ut dig från servern!"
        },
        {
            "question": "Vilket kommando aktiverar UFW?",
            "options": [
                "ufw start",
                "ufw enable",
                "systemctl start ufw",
                "ufw on"
            ],
            "correct": 1,
            "explanation": "ufw enable aktiverar brandväggen. ufw disable stänger av den."
        },
        {
            "question": "Hur tillåter du endast TCP på port 443?",
            "options": [
                "ufw allow 443",
                "ufw allow 443/tcp",
                "ufw allow tcp 443",
                "ufw allow --tcp 443"
            ],
            "correct": 1,
            "explanation": "Använd /tcp eller /udp efter portnumret för att specificera protokoll."
        },
        {
            "question": "Hur tar du bort en regel?",
            "options": [
                "ufw remove 22",
                "ufw delete allow 22",
                "ufw drop 22",
                "ufw clear 22"
            ],
            "correct": 1,
            "explanation": "ufw delete följt av den exakta regeln, eller ufw delete <nummer>."
        },
        {
            "question": "Vad är default för inkommande trafik i UFW?",
            "options": [
                "Tillåt allt",
                "Blockera allt",
                "Logga allt",
                "Ingen default"
            ],
            "correct": 1,
            "explanation": "UFW blockerar inkommande och tillåter utgående som standard."
        },
        {
            "question": "Hur visar du regler med nummer?",
            "options": [
                "ufw status -n",
                "ufw status numbered",
                "ufw list numbers",
                "ufw show numbered"
            ],
            "correct": 1,
            "explanation": "ufw status numbered visar regler med radnummer för enkel borttagning."
        },
        {
            "question": "Hur tillåter du SSH endast från 192.168.1.0/24?",
            "options": [
                "ufw allow ssh from 192.168.1.0/24",
                "ufw allow from 192.168.1.0/24 to any port 22",
                "ufw allow 22 192.168.1.0/24",
                "ufw allow ssh --source 192.168.1.0/24"
            ],
            "correct": 1,
            "explanation": "Syntaxen är: ufw allow from <source> to any port <port>."
        },
        {
            "question": "Vad gör ufw reset?",
            "options": [
                "Startar om UFW-tjänsten",
                "Återställer alla regler till default",
                "Rensar loggarna",
                "Aktiverar UFW"
            ],
            "correct": 1,
            "explanation": "ufw reset tar bort alla regler och återställer till utgångsläget."
        },
        {
            "question": "Vilken fil konfigurerar UFW default-beteende?",
            "options": [
                "/etc/ufw/ufw.conf",
                "/etc/default/ufw",
                "/etc/firewall/rules",
                "/etc/ufw.rules"
            ],
            "correct": 1,
            "explanation": "/etc/default/ufw innehåller default-inställningar för UFW."
        },
        {
            "question": "Vad händer om du kör ufw enable utan att tillåta SSH?",
            "options": [
                "SSH tillåts automatiskt",
                "Du låses ut från servern",
                "UFW vägrar aktivera",
                "SSH fungerar ändå"
            ],
            "correct": 1,
            "explanation": "SSH blockeras och du kan inte längre ansluta remote!"
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
UFW_FLASHCARDS = [
    {"front": "ufw enable gör?", "back": "Aktiverar brandväggen"},
    {"front": "ufw disable gör?", "back": "Avaktiverar brandväggen"},
    {"front": "ufw allow ssh gör?", "back": "Tillåter SSH (port 22)"},
    {"front": "ufw allow 443/tcp gör?", "back": "Tillåter HTTPS endast TCP"},
    {"front": "ufw status numbered visar?", "back": "Regler med radnummer"},
    {"front": "ufw delete 2 gör?", "back": "Tar bort regel nummer 2"},
    {"front": "Säker ordning vid aktivering?", "back": "allow ssh FÖRST, sedan enable"},
    {"front": "ufw default deny incoming gör?", "back": "Blockerar all inkommande som standard"},
    {"front": "ufw allow from IP gör?", "back": "Tillåter all trafik från specifik IP"},
    {"front": "ufw reset gör?", "back": "Återställer alla regler"},
    {"front": "UFW står för?", "back": "Uncomplicated Firewall"},
    {"front": "UFW är frontend för?", "back": "iptables"},
    {"front": "Default inkommande i UFW?", "back": "deny (blockera)"},
    {"front": "Default utgående i UFW?", "back": "allow (tillåt)"},
    {"front": "ufw status verbose visar?", "back": "Detaljerad status med defaults"},
    {"front": "ufw deny from IP gör?", "back": "Blockerar all trafik från IP"},
    {"front": "ufw allow 80,443/tcp gör?", "back": "Tillåter flera portar"},
    {"front": "Port för SSH?", "back": "22"},
    {"front": "Port för HTTP?", "back": "80"},
    {"front": "Port för HTTPS?", "back": "443"},
]
