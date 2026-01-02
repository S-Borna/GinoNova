# SSH & Brandvägg - Hands-On Session

## Konfiguration & Säkerhetsåtgärder

---

## 📋 Innehållsförteckning

1. [Brandväggskonfiguration](#brandväggskonfiguration)
2. [SSH-nycklar för Inloggning](#ssh-nycklar-för-inloggning)
3. [SSH Hardening](#ssh-hardening)
4. [SSH Client Config](#ssh-client-config)
5. [Felsökning](#felsökning)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Cheat Sheet](#cheat-sheet)

---

## 🔥 Brandväggskonfiguration

### Ubuntu - UFW (Uncomplicated Firewall)

**Kontrollera status:**

```bash
sudo ufw status
# Output: Status: inactive (om inte aktiverad än)
```

**Aktivera brandvägg (viktigt att göra EFTER att ha tillåtit SSH!):**

```bash
# 1. Tillåt SSH FÖRST (annars låser du ut dig!)
sudo ufw allow 22

# 2. Aktivera brandväggen
sudo ufw enable
# Varning: "Command may disrupt existing SSH connection"
# Svara: yes

# 3. Verifiera
sudo ufw status
```

**Output efter aktivering:**

```
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
22 (v6)                    ALLOW       Anywhere (v6)
```

**Standardbeteende:**

- **Incoming:** Deny (default) - Blockera allt inkommande
- **Outgoing:** Allow (default) - Tillåt allt utgående

⚠️ **KRITISKT**: Lägg ALLTID till SSH-regel (port 22) INNAN du aktiverar UFW!

---

### Fedora - firewalld

**Kontrollera status:**

```bash
systemctl status firewalld.service
# Ska vara: active (running) och enabled
```

**Om den inte körs:**

```bash
sudo systemctl enable --now firewalld.service
```

**Visa brandväggskonfiguration:**

```bash
sudo firewall-cmd --list-all
```

**Output exempel:**

```
public (active)
  target: default
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  ...
```

**Vad betyder detta?**

- `cockpit` - Webbinterface för serveradministration (port 9090)
- `dhcpv6-client` - DHCP för IPv6
- `ssh` - SSH-server (port 22)

**Bra att veta:**

- SSH är redan tillåtet by default i Fedora
- Brandväggen är redan aktiv
- Ingen konfiguration behövdes för grundläggande SSH-åtkomst

---

## 🔑 SSH-nycklar för Inloggning

### Kopiera SSH-nyckel till VM

**Från din dator (Mac/Linux/WSL):**

```bash
ssh-copy-id -i ~/.ssh/id_ed25519 username@ip-address
```

**Exempel:**

```bash
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.5
```

**Vad gör kommandot?**

1. Läser din **privata** nyckel (för att få rätt publik nyckel)
2. Kopierar **publika** nyckeln till servern
3. Lägger till den i `~/.ssh/authorized_keys` på servern

### Manuell kopiering (Windows PowerShell)

**Om `ssh-copy-id` inte finns (Windows):**

**Steg 1: Visa din publika nyckel**

```powershell
type C:\Users\username\.ssh\id_ed25519.pub
```

**Steg 2: Kopiera hela output**

**Steg 3: På servern (Ubuntu/Fedora)**

```bash
# Skapa .ssh-mapp om den inte finns
mkdir -p ~/.ssh

# Editera authorized_keys
vim ~/.ssh/authorized_keys

# Klistra in din publika nyckel
# Spara och stäng (ESC, :wq)
```

### Verifiera att det fungerar

**Hitta authorized_keys:**

```bash
cat ~/.ssh/authorized_keys
```

**Ska innehålla:**

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILongstring... user@hostname
```

**Testa inloggning:**

```bash
ssh username@ip-address
# Ska fråga efter passphrase för nyckel, INTE lösenord för användare
```

⚠️ **VIKTIGT**:

- Gör detta för **BÅDE Ubuntu OCH Fedora**
- Om du inte har nyckel i authorized_keys kommer du låsas ute när vi stänger av lösenordsinloggning!

---

## 🛡️ SSH Hardening

### Varför Hardening?

**Säkerhetsåtgärder för SSH:**

1. **Byt port** - Minska automatiska attackförsök
2. **Stäng av lösenord** - Endast SSH-nycklar
3. **Stäng av root-login** - Root ska aldrig logga in direkt
4. **Begränsa användare** - Whitelist vem som får logga in

### Skapa Konfigurationsfil

**På både Ubuntu och Fedora:**

```bash
# Skapa konfigurationsfil
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
```

**Filinnehåll:**

```
# Ändra port som SSH lyssnar på
Port 6622

# Stäng av lösenordsinloggning
PasswordAuthentication no

# Stäng av root-login
PermitRootLogin no

# Tillåt endast specifika användare
AllowUsers gg
```

**Anpassa:**

- `Port` - Välj valfri port (undvik 22, 80, 443, etc.)
- `AllowUsers` - Ditt användarnamn

### Varför `.d`-mappar?

**Fördelar med `/etc/ssh/sshd_config.d/`:**

- Huvudfilen (`/etc/ssh/sshd_config`) förblir orörd
- Enkelt att se vad som ändrats
- Enkelt att dela mellan system
- Enkelt att ta bort/inaktivera

**Include-direktiv i huvudfilen:**

```bash
Include /etc/ssh/sshd_config.d/*.conf
```

**Namngivning:**

- `01-` prefix anger ordning
- `.conf` suffix krävs för att inkluderas

---

### Uppdatera Brandvägg för Ny Port

⚠️ **VIKTIGT**: Lägg till nya porten INNAN du startar om SSH!

**Ubuntu (UFW):**

```bash
# Tillåt ny port
sudo ufw allow 6622

# Verifiera
sudo ufw status
```

**Fedora (firewalld):**

```bash
# Lägg till port (permanent)
sudo firewall-cmd --add-port=6622/tcp --permanent

# Ladda om regler
sudo firewall-cmd --reload

# Verifiera
sudo firewall-cmd --list-all
```

---

### Starta Om SSH-tjänsten

**Ubuntu:**

```bash
sudo systemctl restart ssh.service
```

**Fedora:**

```bash
sudo systemctl restart sshd.service
```

⚠️ **Notera skillnaden**: `ssh.service` vs `sshd.service`

**Verifiera att tjänsten körs:**

```bash
# Ubuntu
systemctl status ssh.service

# Fedora
systemctl status sshd.service
```

---

### Testa Ny Konfiguration

**Från din dator:**

```bash
# Med ny port
ssh -p 6622 username@ip-address

# Om det inte fungerar
ssh username@ip-address  # Prova gamla porten (22)
```

**Kontrollera vilken port SSH lyssnar på:**

```bash
ss -tulpn | grep ssh
# Eller
sudo ss -tulpn | grep 22
```

**Output exempel:**

```
tcp   LISTEN 0  128  0.0.0.0:6622  0.0.0.0:*
```

---

### Ta Bort Gamla Brandväggsregler

**När nya porten fungerar:**

**Ubuntu:**

```bash
# Lista regler med nummer
sudo ufw status numbered

# Output exempel:
# [1] 22          ALLOW IN    Anywhere
# [2] 6622        ALLOW IN    Anywhere
# [3] 22 (v6)     ALLOW IN    Anywhere (v6)
# [4] 6622 (v6)   ALLOW IN    Anywhere (v6)

# Ta bort regel (börja med högsta nummer!)
sudo ufw delete 3
sudo ufw delete 1
```

**Fedora:**

```bash
# Ta bort SSH-service (port 22)
sudo firewall-cmd --remove-service=ssh --permanent
sudo firewall-cmd --reload
```

---

## 📝 SSH Client Config

### Förenkla SSH-anslutning

**Problem:**

```bash
# Jobbigt att skriva varje gång
ssh -i ~/.ssh/id_ed25519 -p 6622 gg@192.168.64.5
```

**Lösning: SSH Config**

**Skapa/editera:**

```bash
vim ~/.ssh/config
```

**Exempel konfiguration:**

```
Host ubuntu
    HostName 192.168.64.5
    User gg
    Port 6622
    IdentityFile ~/.ssh/id_ed25519

Host fedora
    HostName 192.168.64.6
    User gg
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

**Efter detta:**

```bash
ssh ubuntu  # Ansluter till Ubuntu VM
ssh fedora  # Ansluter till Fedora VM
```

**Fördelar:**

- Enklare kommandon
- Inget att komma ihåg
- Centraliserad konfiguration

**Läs mer:**

```bash
man 5 ssh_config
```

---

## 🔍 Felsökning

### Problem 1: Permission Denied efter SSH-copy-id

**Symptom:**

```bash
ssh username@ip-address
# Permission denied (publickey)
```

**Lösning:**

```bash
# Kontrollera att nyckel finns
cat ~/.ssh/authorized_keys

# Om tom eller fel - kopiera manuellt
# Se "Manuell kopiering" ovan
```

---

### Problem 2: Connection Refused

**Symptom:**

```bash
ssh username@ip-address
# Connection refused
```

**Möjliga orsaker:**

**1. SSH-tjänsten körs inte**

```bash
systemctl status ssh.service     # Ubuntu
systemctl status sshd.service    # Fedora

# Starta om om nödvändigt
sudo systemctl restart ssh.service
```

**2. Fel port**

```bash
# Prova med explicit port
ssh -p 6622 username@ip-address
```

**3. Brandvägg blockerar**

```bash
# Ubuntu
sudo ufw status

# Fedora
sudo firewall-cmd --list-all
```

---

### Problem 3: Låst Ute Efter Konfigurationsändring

**Symptom:**

- Kan inte logga in efter att ha ändrat SSH-config
- Connection refused eller timeout

**Lösning via VM-konsol (TTY):**

**Steg 1: Logga in via VirtualBox-konsolen**

- Öppna VM-fönstret
- Logga in direkt (inte via SSH)

**Steg 2: Återställ konfiguration**

```bash
# Ta bort eller kommentera din config
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf

# Eller ta bort filen helt
sudo rm /etc/ssh/sshd_config.d/01-ssh-hardening.conf

# Starta om SSH
sudo systemctl restart ssh.service  # Ubuntu
sudo systemctl restart sshd.service # Fedora
```

**Steg 3: Återställ brandvägg**

```bash
# Ubuntu - lägg till port 22
sudo ufw allow 22

# Fedora - lägg till SSH-service
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --reload
```

---

### Problem 4: SSH-tjänst Startar Inte

**Symptom:**

```bash
sudo systemctl restart sshd.service
# Job for sshd.service failed
```

**Diagnos:**

```bash
# Kontrollera status
systemctl status sshd.service

# Visa loggar
journalctl -u sshd.service -n 50
```

**Vanliga fel:**

**1. Typo i config**

```
# Fel:
Port 662 2  # Mellanslag
PasswordAuthentication yes no  # Två värden

# Rätt:
Port 6622
PasswordAuthentication no
```

**2. Permission denied på port**

```
# SELinux (Fedora) blockerar icke-standard portar
# Lösning: Använd port 22 eller konfigurera SELinux
```

---

### Problem 5: Authorized Keys Fungerar Inte

**Symptom:**

- Frågar fortfarande efter lösenord
- Nyckeln är i authorized_keys

**Kontrollera permissions:**

```bash
# .ssh-mappen
ls -ld ~/.ssh
# Ska vara: drwx------ (700)

# authorized_keys
ls -l ~/.ssh/authorized_keys
# Ska vara: -rw------- (600)
```

**Fixa permissions:**

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

## 💡 Viktiga Koncept

### Brandvägg - Koncept

**Varför brandvägg?**

- Skyddar mot oönskade anslutningar
- Begränsar attack-yta
- Kontrollerar in- och utgående trafik

**Default-politik:**

- **Deny incoming** - Blockera allt inkommande (säkert)
- **Allow outgoing** - Tillåt allt utgående (bekvämt)

**Explicit tillåt:**

- Bara öppna de portar som behövs
- Mindre attack-yta = säkrare system

### SSH-nycklar vs Lösenord

**Lösenord:**

- ❌ Kan gissas/bruteforcas
- ❌ Kan läcka (post-it notes!)
- ❌ Svaga lösenord vanliga
- ❌ Samma lösenord överallt

**SSH-nycklar:**

- ✅ Extremt svåra att knäcka
- ✅ Unika per dator
- ✅ Kan ha passphrase som extra skydd
- ✅ Kan revokeras utan att ändra lösenord

### Konfigurationsfiler i Linux

**Allt är en fil:**

```
/etc/ssh/sshd_config          # Huvudkonfiguration
/etc/ssh/sshd_config.d/       # Tilläggskonfiguration
```

**Fördelar:**

- Versionshanterbart (Git)
- Enkelt att kopiera mellan system
- Enkelt att automatisera
- Tydligt vad som ändrats

### `.d`-mappar

**Koncept:**

- Huvudfil inkluderar alla `.conf`-filer från `.d`-mapp
- Enkelt att lägga till/ta bort konfiguration
- Ingen risk att förstöra huvudfil

**Exempel:**

```
/etc/ssh/sshd_config.d/
├── 01-ssh-hardening.conf
├── 02-port-forwarding.conf
└── 03-custom-settings.conf
```

### Port Numbers

**Välkända portar (1-1023):**

- 22 - SSH
- 80 - HTTP
- 443 - HTTPS

**Registrerade portar (1024-49151):**

- Används av specifika tjänster

**Dynamiska portar (49152-65535):**

- Tillfälliga/privata portar

**Välj port för SSH:**

- Undvik välkända portar
- Exempel: 6622, 2222, 22000
- Kontrollera att porten inte används: `ss -tulpn | grep port`

---

## 📋 Cheat Sheet

### Brandvägg - Snabbkommandon

| Uppgift | Ubuntu (UFW) | Fedora (firewalld) |
|---------|--------------|-------------------|
| Status | `sudo ufw status` | `sudo firewall-cmd --list-all` |
| Aktivera | `sudo ufw enable` | `systemctl enable --now firewalld` |
| Tillåt port | `sudo ufw allow 22` | `sudo firewall-cmd --add-port=22/tcp --permanent` |
| Ta bort port | `sudo ufw delete allow 22` | `sudo firewall-cmd --remove-port=22/tcp --permanent` |
| Ladda om | - | `sudo firewall-cmd --reload` |
| Lista med nummer | `sudo ufw status numbered` | - |

### SSH - Snabbkommandon

| Uppgift | Kommando |
|---------|----------|
| Kopiera nyckel | `ssh-copy-id -i ~/.ssh/id_ed25519 user@host` |
| Logga in | `ssh user@host` |
| Logga in (annan port) | `ssh -p 6622 user@host` |
| Visa authorized keys | `cat ~/.ssh/authorized_keys` |
| Kontrollera SSH-status | `systemctl status ssh.service` (Ubuntu) |
|  | `systemctl status sshd.service` (Fedora) |
| Starta om SSH | `sudo systemctl restart ssh.service` |
| Visa SSH-loggar | `journalctl -u sshd.service -n 50` |
| Kolla vilken port | `ss -tulpn | grep ssh` |

### SSH Config - Exempel

```bash
# ~/.ssh/config
Host shortname
    HostName 192.168.1.100
    User username
    Port 6622
    IdentityFile ~/.ssh/id_ed25519
```

### SSH Hardening - Template

```bash
# /etc/ssh/sshd_config.d/01-ssh-hardening.conf
Port 6622
PasswordAuthentication no
PermitRootLogin no
AllowUsers username
```

---

## ⚠️ Viktiga Säkerhetsregler

### Regel 1: Alltid Brandvägg Först

```bash
# ✅ RÄTT ordning:
sudo ufw allow 22          # 1. Tillåt SSH
sudo ufw enable            # 2. Aktivera brandvägg

# ❌ FEL ordning:
sudo ufw enable            # 1. Aktivera brandvägg
sudo ufw allow 22          # 2. För sent - utlåst!
```

### Regel 2: Testa Innan Du Tar Bort

```bash
# ✅ RÄTT:
sudo ufw allow 6622        # 1. Lägg till ny port
sudo systemctl restart ssh # 2. Starta om SSH
ssh -p 6622 user@host      # 3. TESTA att det fungerar
sudo ufw delete allow 22   # 4. Ta bort gammal port

# ❌ FEL:
sudo ufw delete allow 22   # 1. Ta bort gammal port
sudo ufw allow 6622        # 2. För sent om något är fel!
```

### Regel 3: Ha Alltid Backup-åtkomst

- **Ha VM-konsolen tillgänglig** (VirtualBox-fönster)
- **Testa från separat terminal** innan du stänger nuvarande
- **Dokumentera vad du gör** så du kan ångra

### Regel 4: En Ändring i Taget

```bash
# ✅ RÄTT:
1. Byt port -> Testa -> Fungerar
2. Stäng av lösenord -> Testa -> Fungerar
3. Begränsa användare -> Testa -> Fungerar

# ❌ FEL:
1. Byt allt samtidigt -> Fungerar inte -> Vet inte vad som är fel
```

---

## 🎓 Lösningsguide - Steg för Steg

### Ubuntu - Komplett Setup

```bash
# 1. BRANDVÄGG
sudo ufw allow 22
sudo ufw enable
sudo ufw status

# 2. SSH-NYCKEL
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.5

# 3. SSH HARDENING
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
# Lägg till:
# Port 6622
# PasswordAuthentication no
# PermitRootLogin no
# AllowUsers gg

# 4. UPPDATERA BRANDVÄGG
sudo ufw allow 6622

# 5. STARTA OM SSH
sudo systemctl restart ssh.service

# 6. TESTA (från din dator)
ssh -p 6622 gg@192.168.64.5

# 7. TA BORT GAMMAL PORT
sudo ufw status numbered
sudo ufw delete [nummer för port 22]

# 8. CLIENT CONFIG (valfritt)
vim ~/.ssh/config
# Host ubuntu
#     HostName 192.168.64.5
#     User gg
#     Port 6622
#     IdentityFile ~/.ssh/id_ed25519
```

### Fedora - Komplett Setup

```bash
# 1. BRANDVÄGG (redan aktiv)
sudo firewall-cmd --list-all

# 2. SSH-NYCKEL
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.6

# 3. SSH HARDENING
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
# Lägg till:
# PasswordAuthentication no
# PermitRootLogin no
# AllowUsers gg
# OBS: Skippa Port på Fedora (SELinux-problem)

# 4. STARTA OM SSH
sudo systemctl restart sshd.service

# 5. TESTA
ssh gg@192.168.64.6

# 6. CLIENT CONFIG (valfritt)
vim ~/.ssh/config
# Host fedora
#     HostName 192.168.64.6
#     User gg
#     IdentityFile ~/.ssh/id_ed25519
```

---

## 🔧 Verifiering

### Kontrollera Att Allt Fungerar

**1. Brandvägg är aktiv**

```bash
# Ubuntu
sudo ufw status
# Ska visa: Status: active

# Fedora
sudo firewall-cmd --list-all
# Ska visa active zones
```

**2. SSH-nyckel fungerar**

```bash
ssh user@host
# Ska fråga efter passphrase för NYCKEL
# INTE lösenord för ANVÄNDARE
```

**3. Lösenord INTE fungerar**

```bash
# Prova logga in utan nyckel
ssh -o PubkeyAuthentication=no user@host
# Ska ge: Permission denied
```

**4. Root kan INTE logga in**

```bash
ssh root@host
# Ska ge: Permission denied
```

**5. Rätt port används**

```bash
ss -tulpn | grep ssh
# Ubuntu: Ska visa port 6622
# Fedora: Ska visa port 22
```

---

## 📚 Man Pages att Läsa

**SSH:**

```bash
man 5 ssh_config        # SSH client configuration
man 5 sshd_config       # SSH daemon configuration
man ssh-keygen          # Generate SSH keys
man ssh-copy-id         # Copy keys to server
```

**Brandvägg:**

```bash
man ufw                 # Ubuntu firewall
man firewall-cmd        # Fedora firewall
```

**System:**

```bash
man systemctl           # Service management
man journalctl          # Log viewing
```

---

## 🎯 Sammanfattning

### Vad Vi Gjorde

**1. Brandväggar**

- ✅ Aktiverat UFW på Ubuntu
- ✅ Verifierat firewalld på Fedora
- ✅ Tillåtit SSH-port (22)

**2. SSH-nycklar**

- ✅ Kopierat publik nyckel till servrar
- ✅ Kan logga in med nyckel istället för lösenord

**3. SSH Hardening**

- ✅ Bytt port (endast Ubuntu, SELinux-problem på Fedora)
- ✅ Stängt av lösenordsinloggning
- ✅ Stängt av root-login
- ✅ Begränsat tillåtna användare

**4. Bonus**

- ✅ Lärt oss om `.d`-mappar
- ✅ Lärt oss om SSH client config
- ✅ Förstått varför konfiguration-som-filer är bra

### Nyckelpunkter

**Säkerhet i lager:**

1. Brandvägg - Första försvaret
2. SSH-nycklar - Stark autentisering
3. Begränsad åtkomst - Minsta möjliga rättigheter
4. Icke-standard port - Mindre buller från bots

**Alltid:**

- Testa innan du tar bort gamla regler
- Ha backup-åtkomst (VM-konsol)
- En ändring i taget
- Dokumentera vad du gör

### Nästa Steg

1. ✅ Öva på SSH client config (`~/.ssh/config`)
2. ✅ Läs relevanta man pages
3. ✅ Kom på handledning om problem
4. ✅ Fortsätt använda SSH för alla VM-anslutningar

---

## 🆘 Om Du Behöver Hjälp

**Handledning:**

- Torsdagar 10-12 (huvudtid)
- Torsdagar eftermiddag (med Martin)

**Vanliga problem:**

- Låst ute: Använd VM-konsol (VirtualBox-fönster)
- Glömt port: Kolla i config-fil
- Nyckel fungerar inte: Kolla permissions (700/.ssh, 600/authorized_keys)

**Loggar för felsökning:**

```bash
# SSH-loggar
journalctl -u sshd.service -f

# Följ i realtid
tail -f /var/log/auth.log  # Ubuntu
```

---

**Bra jobbat med hands-on! 🚀**

*Konfiguration är en fil - ändra filen, starta om tjänsten, klar!*
