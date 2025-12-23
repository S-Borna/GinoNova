"""
NOD 2.5: Brandvägg - FirewallD (Fedora)
=======================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

FIREWALLD_NODE = {
    "title": "Brandvägg - FirewallD (Fedora)",
    "slug": "brandvagg-firewalld-fedora",
    "description": "Dynamisk zone-baserad brandvägg för Fedora/RHEL/CentOS.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "order_index": 5,
    "content": r"""# Brandvägg - FirewallD (Fedora)

> **TL;DR:** `firewall-cmd --add-port=6622/tcp --permanent` + `firewall-cmd --reload`. Utan `--permanent` försvinner regeln vid omstart!

---

## 📖 TEORI: Vad är FirewallD?

**FirewallD** - Dynamisk brandvägg för Fedora/RHEL/CentOS
- Zone-baserad (olika regler för olika nätverk)
- Runtime vs permanent konfiguration
- Mer avancerad än UFW

### Runtime vs Permanent

| Typ | Beskrivning | Kräver reload? |
|-----|-------------|----------------|
| Runtime | Aktiv nu, försvinner vid omstart | Nej |
| Permanent | Sparas, aktiveras vid reload/omstart | Ja |

```bash
# Runtime (temporärt)
sudo firewall-cmd --add-port=8080/tcp

# Permanent (bestående)
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload    # Aktivera ändringen
```

### Zoner

| Zon | Beskrivning |
|-----|-------------|
| public | Default, begränsad access |
| home | Mer tillåtande, för hemnätverk |
| work | Arbetsnätverk |
| trusted | Allt tillåtet |
| drop | Blockera allt utan svar |
| block | Blockera allt med reject-svar |

---

## 📖 Grundläggande kommandon

### Status

```bash
# Kolla om aktiv
sudo firewall-cmd --state
# Output: running

# Visa alla regler
sudo firewall-cmd --list-all

# Visa för specifik zon
sudo firewall-cmd --list-all --zone=public

# Visa aktiva zoner
sudo firewall-cmd --get-active-zones

# Visa default zon
sudo firewall-cmd --get-default-zone
```

### Tjänster och portar

```bash
# Lista tillgängliga tjänster
sudo firewall-cmd --get-services

# Lista öppna tjänster i aktiv zon
sudo firewall-cmd --list-services

# Lista öppna portar
sudo firewall-cmd --list-ports
```

---

## 📖 Tillåta trafik

### Tjänster

```bash
# Runtime (temporärt)
sudo firewall-cmd --add-service=ssh
sudo firewall-cmd --add-service=http
sudo firewall-cmd --add-service=https

# Permanent
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
```

### Portar

```bash
# Runtime
sudo firewall-cmd --add-port=6622/tcp
sudo firewall-cmd --add-port=8080/tcp

# Permanent
sudo firewall-cmd --add-port=6622/tcp --permanent
sudo firewall-cmd --add-port=3306/tcp --permanent
sudo firewall-cmd --reload
```

### Flera portar samtidigt

```bash
sudo firewall-cmd --add-port={80,443,8080}/tcp --permanent
sudo firewall-cmd --reload
```

---

## 📖 Ta bort regler

```bash
# Ta bort tjänst
sudo firewall-cmd --remove-service=http --permanent

# Ta bort port
sudo firewall-cmd --remove-port=8080/tcp --permanent

# Reload för att aktivera
sudo firewall-cmd --reload
```

---

## 📖 SELinux-problem (VIKTIGT!)

På Fedora kan **SELinux blockera SSH på icke-standard portar**!

```bash
# Kolla om SELinux blockerar
sudo ausearch -m avc -ts recent

# Tillåt SSH på custom port
sudo semanage port -a -t ssh_port_t -p tcp 6622

# Om semanage saknas:
sudo dnf install policycoreutils-python-utils
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Tillåt custom SSH-port

```bash
#!/usr/bin/env bash

NEW_PORT=6622

# 1. Lägg till port permanent
sudo firewall-cmd --add-port=${NEW_PORT}/tcp --permanent

# 2. Reload brandvägg
sudo firewall-cmd --reload

# 3. Verifiera
sudo firewall-cmd --list-all

# 4. GLÖM INTE SELinux!
sudo semanage port -a -t ssh_port_t -p tcp ${NEW_PORT}
```

### Exempel 2: Webserver setup

```bash
#!/usr/bin/env bash

# Lägg till tjänster
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent

# Custom app-port
sudo firewall-cmd --add-port=3000/tcp --permanent

# Reload
sudo firewall-cmd --reload

# Visa resultat
sudo firewall-cmd --list-all
```

**Output:**
```
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources:
  services: cockpit dhcpv6-client http https ssh
  ports: 3000/tcp 6622/tcp
  protocols:
  masquerade: no
```

### Exempel 3: Byta SSH-port komplett (Fedora)

```bash
#!/usr/bin/env bash
set -e

OLD_PORT=22
NEW_PORT=6622

echo "=== Steg 1: Lägg till ny port i brandvägg ==="
sudo firewall-cmd --add-port=${NEW_PORT}/tcp --permanent
sudo firewall-cmd --reload

echo "=== Steg 2: Tillåt i SELinux ==="
sudo semanage port -a -t ssh_port_t -p tcp ${NEW_PORT}

echo "=== Steg 3: Uppdatera SSH-config ==="
echo "Port ${NEW_PORT}" | sudo tee /etc/ssh/sshd_config.d/01-port.conf

echo "=== Steg 4: Starta om SSH ==="
sudo systemctl restart sshd

echo "=== Steg 5: TESTA FÖRST! ==="
echo "Kör i ny terminal: ssh -p ${NEW_PORT} user@server"
echo "Om det fungerar, ta bort gamla porten:"
echo "sudo firewall-cmd --remove-service=ssh --permanent"
echo "sudo firewall-cmd --reload"
```

### Exempel 4: Jämförelse UFW vs FirewallD

| Uppgift | UFW (Ubuntu) | FirewallD (Fedora) |
|---------|--------------|-------------------|
| Tillåt port 22 | `ufw allow 22` | `firewall-cmd --add-port=22/tcp --permanent` |
| Tillåt tjänst | `ufw allow ssh` | `firewall-cmd --add-service=ssh --permanent` |
| Aktivera | `ufw enable` | `systemctl start firewalld` |
| Visa status | `ufw status` | `firewall-cmd --list-all` |
| Ta bort regel | `ufw delete allow 22` | `firewall-cmd --remove-port=22/tcp --permanent` |
| Applicera ändringar | Direkt | `firewall-cmd --reload` |

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | firewall-cmd --state visar? | Om brandväggen är running |
| 2 | --permanent gör? | Sparar regeln permanent |
| 3 | firewall-cmd --reload gör? | Aktiverar permanenta ändringar |
| 4 | firewall-cmd --list-all visar? | Alla regler för aktiv zon |
| 5 | --add-service=ssh gör? | Tillåter SSH-tjänsten |
| 6 | --add-port=8080/tcp gör? | Öppnar port 8080 TCP |
| 7 | Vad är en zon i FirewallD? | Uppsättning regler för ett nätverk |
| 8 | Default zon? | public |
| 9 | SELinux kan blockera? | SSH på icke-standard portar |
| 10 | semanage port -a gör? | Lägger till port i SELinux-policy |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad skiljer runtime från permanent i FirewallD?**
- A) Runtime är snabbare
- B) Permanent sparas och behöver reload ✅
- C) Ingen skillnad
- D) Runtime fungerar bara lokalt

**2. Hur aktiverar du permanenta ändringar?**
- A) firewall-cmd --apply
- B) firewall-cmd --reload ✅
- C) systemctl reload firewalld
- D) firewall-cmd --commit

**3. Vilket kommando visar alla regler?**
- A) firewall-cmd --status
- B) firewall-cmd --list-all ✅
- C) firewall-cmd --show
- D) firewall-cmd --rules

**4. Hur öppnar du port 3000 permanent?**
- A) firewall-cmd --port=3000
- B) firewall-cmd --add-port=3000/tcp --permanent ✅
- C) firewall-cmd --open 3000 --permanent
- D) firewall-cmd --allow 3000/tcp

**5. Vad kan blockera SSH på port 6622 på Fedora?**
- A) Bara FirewallD
- B) Bara SSH-config
- C) SELinux ✅
- D) systemd

**6. Hur fixar du SELinux för custom SSH-port?**
- A) selinux --allow ssh 6622
- B) semanage port -a -t ssh_port_t -p tcp 6622 ✅
- C) setsebool -P ssh_port_6622
- D) chcon ssh 6622

**7. Vad är default zone i FirewallD?**
- A) trusted
- B) public ✅
- C) home
- D) work

**8. Hur tar du bort en tjänst permanent?**
- A) firewall-cmd --delete-service=http
- B) firewall-cmd --remove-service=http --permanent ✅
- C) firewall-cmd --drop http
- D) firewall-cmd --disable http

**9. Vilket kommando listar tillgängliga tjänster?**
- A) firewall-cmd --services
- B) firewall-cmd --get-services ✅
- C) firewall-cmd --list-available
- D) firewall-cmd --show-services

**10. När försvinner runtime-regler?**
- A) Efter 1 timme
- B) Vid omstart/reload ✅
- C) Aldrig
- D) Efter logout

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande FirewallD
```bash
# 1. Kolla status
sudo firewall-cmd --state

# 2. Visa aktiv zon
sudo firewall-cmd --get-active-zones

# 3. Lista alla regler
sudo firewall-cmd --list-all
```

### Övning 2: Öppna portar
```bash
# 1. Öppna port 8080 (runtime först)
sudo firewall-cmd --add-port=8080/tcp

# 2. Verifiera
sudo firewall-cmd --list-ports

# 3. Gör permanent
sudo firewall-cmd --add-port=8080/tcp --permanent

# 4. Ta bort (båda)
sudo firewall-cmd --remove-port=8080/tcp
sudo firewall-cmd --remove-port=8080/tcp --permanent
```

### Övning 3: Tjänsthantering
```bash
# 1. Lista tillgängliga tjänster
sudo firewall-cmd --get-services | tr ' ' '\n' | grep -E "^(http|ssh|mysql)"

# 2. Lägg till http permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

# 3. Verifiera
sudo firewall-cmd --list-services
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Glömma --permanent | Försvinner vid omstart | Lägg alltid till --permanent |
| Glömma --reload | Permanent regel aktiveras inte | firewall-cmd --reload |
| Glömma SELinux | SSH blockeras på custom port | semanage port -a ... |
| Fel zon | Regler gäller inte | Kolla --get-active-zones |

---

## 📝 SAMMANFATTNING

```bash
# STATUS
sudo firewall-cmd --state
sudo firewall-cmd --list-all
sudo firewall-cmd --get-active-zones

# TILLÅT (permanent + reload!)
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --add-port=6622/tcp --permanent
sudo firewall-cmd --reload

# TA BORT
sudo firewall-cmd --remove-service=http --permanent
sudo firewall-cmd --remove-port=8080/tcp --permanent
sudo firewall-cmd --reload

# SELINUX (för custom SSH-port!)
sudo semanage port -a -t ssh_port_t -p tcp 6622

# JÄMFÖRELSE MED UFW
# UFW: ufw allow 22
# FirewallD: firewall-cmd --add-port=22/tcp --permanent && firewall-cmd --reload
```

""",
    "quiz": [
        {
            "question": "Vad skiljer runtime från permanent i FirewallD?",
            "options": [
                "Runtime är snabbare",
                "Permanent sparas och behöver reload",
                "Ingen skillnad",
                "Runtime fungerar bara lokalt"
            ],
            "correct": 1,
            "explanation": "Runtime gäller direkt men försvinner vid omstart. Permanent sparas men kräver --reload."
        },
        {
            "question": "Hur aktiverar du permanenta ändringar?",
            "options": [
                "firewall-cmd --apply",
                "firewall-cmd --reload",
                "systemctl reload firewalld",
                "firewall-cmd --commit"
            ],
            "correct": 1,
            "explanation": "--reload läser om konfigurationen och aktiverar permanenta ändringar."
        },
        {
            "question": "Vilket kommando visar alla regler?",
            "options": [
                "firewall-cmd --status",
                "firewall-cmd --list-all",
                "firewall-cmd --show",
                "firewall-cmd --rules"
            ],
            "correct": 1,
            "explanation": "--list-all visar alla regler för den aktiva zonen."
        },
        {
            "question": "Hur öppnar du port 3000 permanent?",
            "options": [
                "firewall-cmd --port=3000",
                "firewall-cmd --add-port=3000/tcp --permanent",
                "firewall-cmd --open 3000 --permanent",
                "firewall-cmd --allow 3000/tcp"
            ],
            "correct": 1,
            "explanation": "--add-port=PORT/PROTOCOL --permanent, följt av --reload."
        },
        {
            "question": "Vad kan blockera SSH på port 6622 på Fedora (utöver brandvägg)?",
            "options": [
                "Bara FirewallD",
                "Bara SSH-config",
                "SELinux",
                "systemd"
            ],
            "correct": 2,
            "explanation": "SELinux har egna portriktlinjer och kan blockera icke-standard portar."
        },
        {
            "question": "Hur fixar du SELinux för custom SSH-port?",
            "options": [
                "selinux --allow ssh 6622",
                "semanage port -a -t ssh_port_t -p tcp 6622",
                "setsebool -P ssh_port_6622",
                "chcon ssh 6622"
            ],
            "correct": 1,
            "explanation": "semanage port lägger till porten till ssh_port_t typen."
        },
        {
            "question": "Vad är default zone i FirewallD?",
            "options": [
                "trusted",
                "public",
                "home",
                "work"
            ],
            "correct": 1,
            "explanation": "public är standard-zonen med begränsad access."
        },
        {
            "question": "Hur tar du bort en tjänst permanent?",
            "options": [
                "firewall-cmd --delete-service=http",
                "firewall-cmd --remove-service=http --permanent",
                "firewall-cmd --drop http",
                "firewall-cmd --disable http"
            ],
            "correct": 1,
            "explanation": "--remove-service tar bort tjänsten, --permanent gör det bestående."
        },
        {
            "question": "Vilket kommando listar tillgängliga tjänster?",
            "options": [
                "firewall-cmd --services",
                "firewall-cmd --get-services",
                "firewall-cmd --list-available",
                "firewall-cmd --show-services"
            ],
            "correct": 1,
            "explanation": "--get-services visar alla fördefinierade tjänster."
        },
        {
            "question": "När försvinner runtime-regler?",
            "options": [
                "Efter 1 timme",
                "Vid omstart eller reload",
                "Aldrig",
                "Efter logout"
            ],
            "correct": 1,
            "explanation": "Runtime-regler finns bara i minnet och försvinner vid omstart/reload."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
FIREWALLD_FLASHCARDS = [
    {"front": "firewall-cmd --state visar?", "back": "Om brandväggen är running"},
    {"front": "--permanent gör?", "back": "Sparar regeln permanent (kräver reload)"},
    {"front": "firewall-cmd --reload gör?", "back": "Aktiverar permanenta ändringar"},
    {"front": "firewall-cmd --list-all visar?", "back": "Alla regler för aktiv zon"},
    {"front": "--add-service=ssh gör?", "back": "Tillåter SSH-tjänsten"},
    {"front": "--add-port=8080/tcp gör?", "back": "Öppnar port 8080 TCP"},
    {"front": "Vad är en zon?", "back": "Uppsättning regler för ett nätverk"},
    {"front": "Default zon?", "back": "public"},
    {"front": "Runtime vs permanent?", "back": "Runtime försvinner vid omstart, permanent sparas"},
    {"front": "SELinux kan blockera?", "back": "SSH på icke-standard portar"},
    {"front": "semanage port -a gör?", "back": "Lägger till port i SELinux-policy"},
    {"front": "--get-services visar?", "back": "Alla tillgängliga tjänster"},
    {"front": "--get-active-zones visar?", "back": "Aktiva zoner och interfaces"},
    {"front": "--remove-port gör?", "back": "Tar bort en öppen port"},
    {"front": "FirewallD på Fedora/RHEL vs UFW på?", "back": "Ubuntu/Debian"},
    {"front": "trusted zon betyder?", "back": "All trafik tillåts"},
    {"front": "drop zon betyder?", "back": "All trafik blockeras tyst"},
    {"front": "Varför --reload efter --permanent?", "back": "Permanent sparas men aktiveras vid reload"},
    {"front": "Paket för semanage?", "back": "policycoreutils-python-utils"},
    {"front": "SSH-port SELinux-typ?", "back": "ssh_port_t"},
]
