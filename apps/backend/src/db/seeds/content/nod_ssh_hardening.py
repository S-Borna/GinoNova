"""
NOD 2.3: SSH-nycklar & Härdning
===============================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

SSH_HARDENING_NODE = {
    "title": "SSH-nycklar & Härdning",
    "slug": "ssh-nycklar-hardning",
    "description": "SSH-nyckelautentisering och härdning av SSH-server för säker fjärranslutning.",
    "difficulty": "hard",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "order_index": 3,
    "content": r"""# SSH-nycklar & Härdning

> **TL;DR:** Generera med `ssh-keygen -t ed25519`. Kopiera med `ssh-copy-id`. Härda med `PasswordAuthentication no` och `PermitRootLogin no`. **TESTA NYCKLAR FÖRE DU STÄNGER LÖSENORD!**

---

## 📖 TEORI: Vad är SSH?

**SSH (Secure Shell)** - Krypterad fjärranslutning.
- Ersätter osäkra protokoll som telnet
- Default port: **22**
- Krypterar all trafik

### SSH-nycklar vs lösenord

| Lösenord | SSH-nycklar |
|----------|-------------|
| Kan gissas/bruteforcas | Praktiskt omöjligt att knäcka |
| Måste kommas ihåg | Lagras i fil |
| Skickas till servern | Privat nyckel lämnar aldrig din dator |
| Kan avlyssnas | Asymmetrisk kryptering |

### Hur fungerar nyckelautentisering?

```
┌──────────────┐                    ┌──────────────┐
│   KLIENT     │                    │   SERVER     │
│              │                    │              │
│ id_ed25519   │  ◄── Matchar ──►  │ authorized_  │
│ (PRIVAT)     │                    │ keys (PUBLIK)│
│              │                    │              │
│ HEMLIG!      │                    │ Kan delas    │
└──────────────┘                    └──────────────┘
```

---

## 📖 Generera SSH-nycklar

### ssh-keygen

```bash
# Generera ed25519-nyckel (rekommenderas!)
ssh-keygen -t ed25519 -C "din@email.com"

# Output:
# Generating public/private ed25519 key pair.
# Enter file in which to save the key (/home/user/.ssh/id_ed25519):
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
```

### Nyckeltyper

| Typ | Säkerhet | Rekommendation |
|-----|----------|----------------|
| ed25519 | ⭐⭐⭐⭐⭐ | Bäst - använd denna! |
| rsa (4096) | ⭐⭐⭐⭐ | OK om ed25519 inte stöds |
| ecdsa | ⭐⭐⭐ | Kontroversiel |
| dsa | ⭐ | Deprecated - använd inte! |

### Resulterande filer

```bash
~/.ssh/id_ed25519       # PRIVAT nyckel - DELA ALDRIG!
~/.ssh/id_ed25519.pub   # Publik nyckel - kan delas fritt
```

### Visa publik nyckel

```bash
cat ~/.ssh/id_ed25519.pub
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... din@email.com
```

---

## 📖 Kopiera nyckel till server

### ssh-copy-id (rekommenderat!)

```bash
# Automatisk kopiering
ssh-copy-id -i ~/.ssh/id_ed25519 user@server

# Med annan port
ssh-copy-id -i ~/.ssh/id_ed25519 -p 6622 user@server
```

### Manuellt (om ssh-copy-id saknas)

```bash
# 1. Visa din publika nyckel
cat ~/.ssh/id_ed25519.pub

# 2. På servern - skapa .ssh och authorized_keys
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
# Klistra in publika nyckeln

chmod 600 ~/.ssh/authorized_keys
```

### authorized_keys

Fil på **SERVERN**: `~/.ssh/authorized_keys`
- Innehåller publika nycklar som får logga in
- En nyckel per rad

```bash
# Exempel på authorized_keys
ssh-ed25519 AAAAC3Nza... user1@laptop
ssh-ed25519 AAAAC3Nzb... user1@desktop
ssh-rsa AAAAB3NzaC1y... user2@server
```

---

## 📖 SSH-härdning (KRITISKT FÖR TENTA OCH PROJEKT!)

### ⚠️ ORDNING VID HÄRDNING - FÖLJ EXAKT!

```
1. Generera SSH-nyckel på din dator
2. Kopiera nyckeln till servern (ssh-copy-id)
3. TESTA att nyckelinloggning fungerar
4. FÖRST DÅ - stäng av lösenord
5. Annars LÅSER DU UT DIG SJÄLV!
```

### Konfigurationsfil

```bash
# Skapa härdningsfil (rekommenderas framför att ändra sshd_config)
sudo nano /etc/ssh/sshd_config.d/01-hardening.conf
```

### Härdningsinställningar

```bash
# /etc/ssh/sshd_config.d/01-hardening.conf

# Byt port (security through obscurity)
Port 6622

# ENDAST nyckelautentisering - inga lösenord!
PasswordAuthentication no

# Root får INTE logga in via SSH
PermitRootLogin no

# Begränsa vilka som får SSH:a
AllowUsers said alice bob

# Extra säkerhet
PubkeyAuthentication yes
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding no
```

### Starta om SSH efter ändringar

```bash
# Ubuntu/Debian:
sudo systemctl restart ssh

# Fedora/CentOS/RHEL:
sudo systemctl restart sshd

# Kontrollera status
sudo systemctl status ssh
```

### Verifiera vilken port SSH lyssnar på

```bash
sudo ss -tulpn | grep ssh
# Output: tcp LISTEN 0 128 *:6622 *:* users:(("sshd",pid=1234))
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Komplett härdningsflow

```bash
# === PÅ DIN LOKALA DATOR ===

# 1. Generera nyckel (om du inte har)
ssh-keygen -t ed25519 -C "min@email.com"

# 2. Kopiera till server
ssh-copy-id -i ~/.ssh/id_ed25519 said@192.168.1.100

# 3. TESTA att det fungerar!
ssh said@192.168.1.100
# Om du kom in utan lösenord → fortsätt!
# Om du fick ange lösenord → felsök först!

# === PÅ SERVERN ===

# 4. Skapa härdningsfil
sudo nano /etc/ssh/sshd_config.d/01-hardening.conf

# Innehåll:
Port 6622
PasswordAuthentication no
PermitRootLogin no
AllowUsers said

# 5. VIKTIGT! Öppna nya porten i brandväggen INNAN restart!
sudo ufw allow 6622/tcp
# eller
sudo firewall-cmd --permanent --add-port=6622/tcp
sudo firewall-cmd --reload

# 6. Starta om SSH
sudo systemctl restart ssh

# === TILLBAKA PÅ DIN LOKALA DATOR ===

# 7. Testa med nya porten (i nytt terminalfönster!)
ssh -p 6622 said@192.168.1.100
```

### Exempel 2: SSH-alias i .bashrc

```bash
# Lägg till i ~/.bashrc eller ~/.bash_aliases
alias ubuntu='ssh -p 6622 said@192.168.1.100'
alias fedora='ssh said@192.168.1.101'
alias prod='ssh -i ~/.ssh/prod_key admin@production.example.com'

# Ladda om
source ~/.bashrc

# Nu kan du bara skriva:
ubuntu
```

### Exempel 3: SSH config-fil (ännu bättre!)

```bash
# ~/.ssh/config
Host ubuntu
    HostName 192.168.1.100
    User said
    Port 6622
    IdentityFile ~/.ssh/id_ed25519

Host fedora
    HostName 192.168.1.101
    User said
    IdentityFile ~/.ssh/id_ed25519

Host prod
    HostName production.example.com
    User admin
    IdentityFile ~/.ssh/prod_key

# Nu kan du bara skriva:
ssh ubuntu
ssh fedora
ssh prod
```

### Exempel 4: Felsökning

```bash
# Verbose läge för debugging
ssh -v user@server
ssh -vv user@server    # Mer verbose
ssh -vvv user@server   # Max verbose

# Kontrollera SSH-tjänstens status
sudo systemctl status ssh

# Se SSH-loggar
sudo journalctl -u ssh -f
sudo tail -f /var/log/auth.log
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | ssh-keygen -t ed25519 gör? | Genererar ed25519-nyckelpar |
| 2 | ssh-copy-id gör? | Kopierar publik nyckel till serverns authorized_keys |
| 3 | PasswordAuthentication no gör? | Stänger av lösenordsinloggning |
| 4 | PermitRootLogin no gör? | Förbjuder root att logga in via SSH |
| 5 | ~/.ssh/authorized_keys innehåller? | Publika nycklar som får logga in |
| 6 | Default SSH-port? | 22 |
| 7 | Privat nyckel heter? | id_ed25519 (eller id_rsa) |
| 8 | sudo systemctl restart ssh gör? | Startar om SSH-tjänsten |
| 9 | ssh -p 6622 gör? | Ansluter via port 6622 |
| 10 | Permissions för ~/.ssh? | 700 |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilken nyckeltyp rekommenderas för SSH?**
- A) rsa
- B) dsa
- C) ed25519 ✅
- D) ecdsa

**2. Var lagras publika nycklar på servern?**
- A) /etc/ssh/keys
- B) ~/.ssh/authorized_keys ✅
- C) ~/.ssh/id_ed25519.pub
- D) /etc/ssh/authorized_keys

**3. Vad gör PasswordAuthentication no?**
- A) Låser alla konton
- B) Endast nyckelautentisering tillåts ✅
- C) Tar bort alla lösenord
- D) Krypterar lösenord

**4. I vilken ordning ska du härda SSH?**
- A) Stäng lösenord → kopiera nyckel → testa
- B) Kopiera nyckel → testa → stäng lösenord ✅
- C) Stäng lösenord → byt port → kopiera nyckel
- D) Ordningen spelar ingen roll

**5. Vad är SSH:s default port?**
- A) 21
- B) 22 ✅
- C) 80
- D) 443

**6. Vad gör ssh-copy-id?**
- A) Kopierar privat nyckel till server
- B) Kopierar publik nyckel till authorized_keys ✅
- C) Kopierar SSH-config
- D) Skapar en ny nyckel

**7. Hur ansluter du till SSH på port 6622?**
- A) ssh user@server:6622
- B) ssh -p 6622 user@server ✅
- C) ssh --port 6622 user@server
- D) ssh user@server -port 6622

**8. Vilken permission ska ~/.ssh ha?**
- A) 777
- B) 755
- C) 700 ✅
- D) 644

**9. Vilket kommando startar om SSH-tjänsten på Ubuntu?**
- A) sudo restart ssh
- B) sudo systemctl restart ssh ✅
- C) sudo service ssh reload
- D) ssh --restart

**10. Vad händer om du stänger PasswordAuthentication utan fungerande nyckel?**
- A) SSH går till backup-läge
- B) Du låses ut från servern ✅
- C) Lösenord fungerar ändå
- D) Servern startar om automatiskt

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Generera och inspektera nyckel
```bash
# 1. Generera nyckel
ssh-keygen -t ed25519 -C "test@example.com" -f ~/.ssh/test_key

# 2. Inspektera
ls -la ~/.ssh/test_key*
cat ~/.ssh/test_key.pub

# 3. Rensa (valfritt)
rm ~/.ssh/test_key*
```

### Övning 2: SSH config
```bash
# Skapa ~/.ssh/config
nano ~/.ssh/config

# Lägg till:
Host testserver
    HostName 192.168.1.100
    User testuser
    Port 22
    IdentityFile ~/.ssh/id_ed25519

# Testa (om du har en server)
ssh testserver
```

### Övning 3: Simulera härdning (LÄSÖVNING)
Gå igenom dessa steg mentalt och förstå ordningen:
1. ssh-keygen på klient
2. ssh-copy-id till server
3. Testa ssh utan lösenord
4. Skapa härdningsfil
5. Öppna ny port i brandvägg
6. Starta om SSH
7. Testa med ny port

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| Stänga lösenord före nycklar funkar | Låser ut sig själv | ALLTID testa nycklar först! |
| Glömma öppna ny port i brandvägg | Kan inte ansluta | ufw allow PORT/tcp före restart |
| Fel permissions på ~/.ssh | SSH vägrar | chmod 700 ~/.ssh, chmod 600 nycklar |
| Redigera /etc/ssh/sshd_config direkt | Svårt att underhålla | Använd sshd_config.d/*.conf |

---

## 📝 SAMMANFATTNING

```bash
# GENERERA NYCKEL
ssh-keygen -t ed25519 -C "email@example.com"

# KOPIERA TILL SERVER
ssh-copy-id -i ~/.ssh/id_ed25519 user@server

# TESTA (INNAN HÄRDNING!)
ssh user@server

# HÄRDNINGSFIL
sudo nano /etc/ssh/sshd_config.d/01-hardening.conf
# Innehåll:
Port 6622
PasswordAuthentication no
PermitRootLogin no
AllowUsers said

# ÖPPNA PORT I BRANDVÄGG (INNAN RESTART!)
sudo ufw allow 6622/tcp

# STARTA OM SSH
sudo systemctl restart ssh

# TESTA MED NY PORT
ssh -p 6622 user@server

# SSH CONFIG (~/.ssh/config)
Host server
    HostName 192.168.1.100
    User said
    Port 6622
    IdentityFile ~/.ssh/id_ed25519

# PERMISSIONS
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
```

"""
}

