"""
Linux Mastery Module
====================

20 noder med svensk pedagogisk stil.
Komplett Linux-administration - från filsystem till brandväggar.

Track: foundation
Difficulty: intermediate
Estimated Hours: 30
"""

MODULE = {
    "name": "Linux Mastery",
    "slug": "linux-mastery",
    "description": "Komplett Linux-administration - från filsystem till brandväggar med naturlig svensk pedagogik",
    "track_slug": "foundation",
    "order_index": 2,
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "prerequisites": ["environment-tooling-setup"],
    "icon": "🐧",
    "color": "#FCC624",
    "tasks": [
        {
            "title": 'Filesystem Hierarchy Standard (FHS)',
            "slug": 'filesystem-hierarchy-standard',
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Filesystem Hierarchy Standard (FHS)

Valkommen till Linux-varlden! Har lar du dig hur Linux organiserar sina filer - grunden for allt du kommer gora som DevOps-ingenjor.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation och Setup

For att folja med i denna modul behover du tillgang till en Linux-miljo:

| Alternativ | Beskrivning | Rekommendation |
|------------|-------------|----------------|
| **WSL2** | Windows Subsystem for Linux | Bast for Windows |
| **Virtuell maskin** | VirtualBox/VMware med Ubuntu | Bra for larande |
| **Cloud server** | AWS EC2, DigitalOcean, etc | Bra for praktik |
| **Docker** | `docker run -it ubuntu bash` | Snabbast att starta |

```bash
# Windows - Installera WSL2
wsl --install -d Ubuntu

# macOS - Anvand terminalen direkt eller Docker
docker run -it ubuntu:22.04 bash

# Verifiera att du har tillgang
cat /etc/os-release
# NAME="Ubuntu"
# VERSION="22.04.3 LTS (Jammy Jellyfish)"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Konfigurationer** | Var installningar sparas |
| **Felsökning** | Var loggar hamnar |
| **Installation** | Var program installeras |
| **Permissions** | Var anvandare har sina filer |

Som DevOps-ingenjor lever du i terminalen. Du maste veta var saker ligger!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Linux Filstruktur - Oversikt

```
┌─────────────────────────────────────────────────────────────┐
│                         / (root)                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   /bin ────── Grundlaggande kommandon (ls, cp, mv)         │
│   /etc ────── Konfigurationsfiler                          │
│   /var ────── Variabel data (loggar, databaser)            │
│   /usr ────── Installerade program                         │
│   /home ───── Anvandarkataloger                            │
│   /tmp ────── Temporara filer                              │
│   /opt ────── Tredjepartsprogram                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Katalog | Syfte | Exempel |
|---------|-------|---------|
| `/bin` | Grundkommandon | ls, cp, mv, cat |
| `/etc` | Konfiguration | nginx.conf, passwd |
| `/var` | Variabel data | Loggar, databaser |
| `/usr` | Program | python, git, docker |
| `/home` | Anvandarfiler | /home/devops |
| `/tmp` | Temporart | Rensas vid reboot |
| `/opt` | Tredjepartsprogram | Chrome, containerd |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /bin - Grundlaggande kommandon

Har ligger de absolut viktigaste kommandona - de som maste fungera aven om resten av systemet har problem.

```bash
# Lista innehall i /bin
ls /bin

# Se var ett kommando finns
which cp
# /bin/cp
```

| Kommando | Beskrivning |
|----------|-------------|
| `ls` | Lista filer |
| `cp` | Kopiera filer |
| `mv` | Flytta/byt namn |
| `cat` | Visa filinnehall |
| `echo` | Skriv ut text |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /etc - Alla installningar

Hjartat av systemkonfigurationen. Varje gang du vill andra hur ett program beter sig, ar det hit du gar.

```bash
# Serverns namn
cat /etc/hostname

# Nginx konfiguration
ls /etc/nginx/

# Visa forsta 5 anvandare
head -5 /etc/passwd
```

| Fil | Innehall |
|-----|----------|
| `/etc/hostname` | Serverns namn |
| `/etc/passwd` | Anvandarlista |
| `/etc/nginx/` | Nginx-config |
| `/etc/ssh/` | SSH-config |

**Gyllene regeln:** Innan du ror nagot i /etc - ta backup!

```bash
# Ta backup innan andring
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /var - Data som andras

Medan /etc innehaller statiska installningar, innehaller /var saker som standigt forandras.

```bash
# Lista loggfiler
ls /var/log/

# Visa senaste systemhändelser
tail -20 /var/log/syslog

# Overvaka loggstorlek i realtid
watch -n 2 'ls -lh /var/log/*.log'
```

| Katalog | Innehall |
|---------|----------|
| `/var/log/` | Loggfiler |
| `/var/log/syslog` | Systemhändelser |
| `/var/log/auth.log` | Inloggningsforsok |
| `/var/lib/` | Databaser, state |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /usr - Installerade program

De flesta program du installerar hamnar har. Som "Program Files" pa Windows.

```bash
# Rakna program i /usr/bin
ls /usr/bin/ | wc -l

# Se var python finns
which python3
# /usr/bin/python3

# Egna scripts (roras inte av pakethanterare)
ls /usr/local/bin/
```

| Katalog | Anvandning |
|---------|------------|
| `/usr/bin/` | Installerade program |
| `/usr/local/bin/` | Egna scripts |
| `/usr/lib/` | Bibliotek |
| `/usr/share/` | Delad data |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /home - Anvandarnas utrymme

Varje anvandare far sin egen katalog under /home.

```bash
# Visa alla anvandarkataloger
ls -la /home/

# Din egen hemkatalog
ls -la ~/

# Visa .bashrc
cat ~/.bashrc | head -20
```

| Fil | Syfte |
|-----|-------|
| `~/.bashrc` | Shell-installningar |
| `~/.ssh/` | SSH-nycklar |
| `~/.profile` | Miljövariabler |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /tmp och /opt

```bash
# Temporara filer (rensas vid reboot)
ls /tmp/

# Skapa unik temp-fil
mktemp
# /tmp/tmp.Xf4kL2

# Tredjepartsprogram
ls /opt/

# Se storlek per program
du -sh /opt/*
```

| Katalog | Egenskap |
|---------|----------|
| `/tmp` | Rensas automatiskt |
| `/opt` | Ett program per mapp |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Behov | Katalog |
|-------|---------|
| Andra config | `/etc` |
| Felsoka | `/var/log` |
| Egna scripts | `/usr/local/bin` |
| Anvandarfiler | `/home` |
| Temp-filer | `/tmp` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **/etc** | Konfiguration - hit for installningar |
| **/var/log** | Loggar - hit for felsökning |
| **/usr/local/bin** | Egna scripts - roras inte av apt |
| **/home** | Anvandarfiler - varje anvandare har sin |
| **Backup** | Ta ALLTID backup innan /etc-andring |

**Kom ihag:**
- `/etc` = konfiguration
- `/var/log` = loggar
- `/usr/local/bin` = egna scripts
- `/home` = anvandarfiler
- Ta alltid backup innan du andrar i /etc!
""",
        },
        {
            "title": 'Mount Points och Device Files',
            "slug": 'mount-points-device-files',
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 65,
            "content": """# Mount Points och Device Files

I Linux ar allt en fil - aven harddiskar och USB-minnen. Har lar du dig hur Linux hanterar lagringsenheter och hur du kopplar dem till filsystemet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Backup** | Ansluta externa diskar |
| **Felsökning** | Forsta /dev-katalogen |
| **Automatisering** | Konfigurera auto-mount |
| **Disk full** | Forsta var saker ar mountade |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Sa fungerar mounting

```
┌─────────────────────────────────────────────────────────────┐
│                    MOUNT PROCESS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   /dev/sdb1 ──────────► mount ──────────► /mnt/external    │
│   (fysisk disk)                           (tillganglig)     │
│                                                             │
│   Disk dyker upp      Kommando           Nu kan du          │
│   i /dev              kopplar ihop       lasa/skriva        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Lista alla diskar och partitioner
lsblk
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   100G  0 disk
# ├─sda1   8:1    0    99G  0 part /
# └─sda2   8:2    0     1G  0 part [SWAP]
# sdb      8:16   0   500G  0 disk
# └─sdb1   8:17   0   500G  0 part
```

| Kolumn | Betydelse |
|--------|-----------|
| NAME | Enhetsnamn |
| SIZE | Storlek |
| TYPE | disk/part |
| MOUNTPOINT | Var den ar monterad |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## /dev - Alla enheter

`/dev` ar en speciell katalog dar Linux representerar all hardvara som filer.

```bash
# SATA/SCSI diskar
ls /dev/sd*
# /dev/sda  /dev/sda1  /dev/sdb  /dev/sdb1

# NVMe SSD-diskar
ls /dev/nvme*
# /dev/nvme0n1  /dev/nvme0n1p1

# Specialenheter
cat /dev/null          # Svart hal - allt forsvinner
head -c 16 /dev/urandom | xxd   # Slumptal
```

| Enhet | Typ |
|-------|-----|
| `/dev/sda` | Forsta SATA-disk |
| `/dev/sdb1` | Forsta partition pa andra disk |
| `/dev/nvme0n1` | Forsta NVMe-disk |
| `/dev/null` | Svart hal |
| `/dev/urandom` | Slumptalsgenerator |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Mounta en disk

| Kommando | Beskrivning |
|----------|-------------|
| `mkdir /mnt/external` | Skapa mount-punkt |
| `mount /dev/sdb1 /mnt/external` | Mounta disk |
| `df -h /mnt/external` | Visa diskutrymme |
| `ls /mnt/external` | Lista innehall |

```bash
# Skapa mount-punkt
sudo mkdir /mnt/external

# Mounta partition
sudo mount /dev/sdb1 /mnt/external

# Visa innehall
ls /mnt/external

# Kontrollera utrymme
df -h /mnt/external
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Unmounta sakert

| Kommando | Beskrivning |
|----------|-------------|
| `umount /mnt/external` | Koppla bort (OBS: umount!) |
| `lsof /mnt/external` | Se vad som anvander disken |
| `fuser -m /mnt/external` | Lista processer |
| `umount -l /mnt/external` | Lazy unmount |

```bash
# Koppla bort sakert
sudo umount /mnt/external

# Om "target is busy":
lsof /mnt/external        # Se vilka processer
sudo umount -l /mnt/external   # Lazy unmount
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Automatisk mount med /etc/fstab

```bash
# Hamta diskens UUID
blkid /dev/sdb1
# /dev/sdb1: UUID="abc-123-def" TYPE="ext4"
```

```
/etc/fstab format:
┌──────────────────────────────────────────────────────────┐
│ <file system>  <mount point>  <type>  <options>  <dump>  │
│ UUID=abc-123   /mnt/external  ext4    defaults   0    2  │
└──────────────────────────────────────────────────────────┘
```

| Falt | Betydelse |
|------|-----------|
| file system | UUID eller /dev/sdX |
| mount point | Var den monteras |
| type | ext4, xfs, ntfs |
| options | defaults, ro, rw |
| dump | Backup (0=nej) |
| pass | fsck vid boot (1=root, 2=andra) |

```bash
# Testa fstab (VIKTIGT!)
sudo mount -a
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga mount-typer

| Typ | Kommando | Anvandning |
|-----|----------|------------|
| NFS | `mount -t nfs server:/share /mnt/nfs` | Natverkslagring |
| CIFS | `mount -t cifs //server/share /mnt/smb` | Windows-delning |
| tmpfs | `mount -t tmpfs -o size=1G tmpfs /mnt/ram` | RAM-disk |

```bash
# NFS (natverkslagring)
sudo mount -t nfs server:/share /mnt/nfs

# CIFS/SMB (Windows-delningar)
sudo mount -t cifs //server/share /mnt/smb -o user=admin

# tmpfs (RAM-disk - supersnabb, forsvinner vid reboot)
sudo mount -t tmpfs -o size=1G tmpfs /mnt/ramdisk
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| "target is busy" | Nagon anvander disken | `lsof /mnt/...` |
| "wrong fs type" | Fel filsystemstyp | Ange `-t ext4` |
| Boot failar | Fel i fstab | `mount -a` forst! |
| "permission denied" | Fel rattigheter | `sudo mount` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **lsblk** | Se alla diskar och mount points |
| **mount/umount** | Anslut/koppla bort (OBS: umount!) |
| **/etc/fstab** | Automatisk mount vid boot |
| **UUID** | Anvand alltid UUID i fstab |
| **mount -a** | Testa ALLTID innan reboot |

**Kom ihag:**
- `lsblk` for att se diskar
- `umount` (INTE unmount!)
- Testa `mount -a` innan reboot
- Anvand UUID i fstab
- Unmounta innan du kopplar bort fysiskt
""",
        },
        {
            "title": 'File Permissions',
            "slug": 'file-permissions',
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 75,
            "content": """# File Permissions

Permissions ar Linux sakerhetssystem - de avgor vem som kan lasa, skriva och kora filer. Utan denna kunskap kommer du stota pa "Permission denied" overallt!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Problem |
|----------|---------|
| **Deploy-scripts** | Kan inte koras - saknar execute |
| **Webbservrar** | Kan inte lasa filer - fel agare |
| **SSH-nycklar** | Accepteras inte - for oppna permissions |
| **Config-filer** | Kan inte andras - saknar write |

Permissions avgor vem som kan gora vad med en fil. Du stoter pa detta dagligen!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Sa fungerar permissions

```
┌─────────────────────────────────────────────────────────────┐
│                    PERMISSION STRING                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   -rw-r--r-- 1 john developers 1024 Dec 7 myfile.txt       │
│   │└┬┘└┬┘└┬┘                                                │
│   │ │  │  └── Others: r-- (bara lasa)                      │
│   │ │  └───── Group:  r-- (bara lasa)                      │
│   │ └──────── Owner:  rw- (lasa och skriva)                │
│   └────────── Filtyp: - (fil), d (katalog), l (lank)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Tecken | Betydelse |
|--------|-----------|
| `r` | Read - lasa |
| `w` | Write - skriva/andra |
| `x` | Execute - kora/oppna katalog |
| `-` | Ingen permission |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Oktala permissions (siffror)

| Siffra | Binart | Permissions |
|--------|--------|-------------|
| 7 | 4+2+1 | rwx (alla) |
| 6 | 4+2 | rw- (lasa+skriva) |
| 5 | 4+1 | r-x (lasa+kora) |
| 4 | 4 | r-- (bara lasa) |
| 0 | 0 | --- (inga) |

```bash
# Vanliga kombinationer
chmod 755 script.sh    # rwxr-xr-x - scripts
chmod 644 config.txt   # rw-r--r-- - config-filer
chmod 600 ~/.ssh/id_rsa # rw------- - SSH-nycklar (OBLIGATORISKT!)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Andra permissions med chmod

| Kommando | Beskrivning |
|----------|-------------|
| `chmod u+x file` | Lagg till execute for owner |
| `chmod g-w file` | Ta bort write for group |
| `chmod o=r file` | Satt only read for others |
| `chmod a+r file` | Lagg till read for alla |
| `chmod 755 file` | rwxr-xr-x |
| `chmod 644 file` | rw-r--r-- |

```bash
# Symboliskt
chmod u+x script.sh      # Owner kan kora
chmod g-w file.txt       # Group kan inte skriva
chmod o=r document.txt   # Others bara lasa
chmod a+r public.html    # Alla kan lasa

# Oktalt (vanligast)
chmod 755 deploy.sh      # Script alla kan kora
chmod 644 nginx.conf     # Config bara owner andrar
chmod 600 secrets.env    # Hemligt - bara owner
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Andra agare med chown

| Kommando | Beskrivning |
|----------|-------------|
| `chown user file` | Andra agare |
| `chown user:group file` | Andra agare OCH grupp |
| `chown -R user dir/` | Rekursivt (alla filer under) |

```bash
# Andra agare
sudo chown nginx /var/www/html/index.html

# Andra agare OCH grupp
sudo chown nginx:www-data /var/www/html/index.html

# Rekursivt (vanligt vid deploy)
sudo chown -R deploy:deploy /var/www/app/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga permission-monster

| Anvandning | Permission | Forklaring |
|------------|------------|------------|
| Scripts | 755 | Alla kan kora |
| Config-filer | 644 | Alla laser, owner skriver |
| Hemligheter | 600 | BARA owner |
| SSH-katalog | 700 | BARA owner |
| Webbfiler | 644 | Webbserver laser |

```bash
# Scripts och program
chmod 755 deploy.sh

# Config-filer
chmod 644 nginx.conf

# Hemliga filer (nycklar, losenord)
chmod 600 secrets.env

# Kataloger - offentliga
chmod 755 /var/www/

# Kataloger - privata
chmod 700 ~/.ssh/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| "Permission denied" vid kor | Saknar x | `chmod +x script.sh` |
| SSH "permissions too open" | For oppna nycklar | `chmod 600 ~/.ssh/id_rsa` |
| Webbserver 403 | Fel agare | `chown www-data:www-data` |
| Kan inte cd till katalog | Saknar x pa katalog | `chmod +x directory/` |

```bash
# Felsok: se permissions
ls -la script.sh

# Fix: lagg till execute
chmod +x script.sh

# SSH-nyckel maste vara 600
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh/

# Webbserver-fix
sudo chown -R www-data:www-data /var/www/html/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **rwx = 4,2,1** | Lar dig siffrorna! |
| **755** | Scripts och kataloger |
| **644** | Config-filer |
| **600** | Hemligheter och SSH-nycklar |
| **chown -R** | Rekursiv agarandring vid deploy |

**Kom ihag:**
- `rwx` = read (4), write (2), execute (1)
- `755` for scripts
- `644` for config
- `600` for hemligheter (SSH KRAVER detta!)
- `chown -R` for rekursiv andring
""",
        },
        {
            "title": 'Inodes, Hard Links och Symbolic Links',
            "slug": 'inodes-links',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Inodes, Hard Links och Symbolic Links

Lankar ar kraftfulla verktyg i Linux som mojliggor zero-downtime deploys, flexibel filhantering och effektiv lagring. Har lar du dig hur de fungerar under huven.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Anvandning |
|----------|------------|
| **Zero-downtime deploy** | Symlinks byter version atomiskt |
| **Disk full trots ledigt** | Slut pa inodes |
| **Raderade filer tar plats** | Hard links haller data |
| **Delad config** | Lankar mellan miljoer |

Lankar ar fundamentala for hur Linux fungerar och anvands overallt i produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar en inode?

```
┌─────────────────────────────────────────────────────────────┐
│                         INODE                               │
├─────────────────────────────────────────────────────────────┤
│  Varje fil har en inode - ett "ID-kort" med metadata        │
│                                                             │
│  ┌─────────────┐                                            │
│  │ Inode 12345 │                                            │
│  ├─────────────┤                                            │
│  │ Permissions │                                            │
│  │ Owner/Group │                                            │
│  │ Timestamps  │                                            │
│  │ Size        │                                            │
│  │ Data blocks │──────► [Faktisk data pa disk]             │
│  └─────────────┘                                            │
│         ▲                                                   │
│         │                                                   │
│   "myfile.txt" (filnamn ar bara en etikett)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Visa inode-nummer
ls -i myfile.txt
# 12345678 myfile.txt

# Visa ALL metadata
stat myfile.txt
# Inode: 12345678    Links: 1
```

| Kommando | Visar |
|----------|-------|
| `ls -i` | Inode-nummer |
| `stat file` | All metadata |
| `df -i` | Inode-anvandning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hard Links

En hard link ar ett extra namn som pekar pa SAMMA inode.

```
┌─────────────────────────────────────────────────────────────┐
│                      HARD LINK                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   "original.txt" ─────┐                                     │
│                       │                                     │
│                       ▼                                     │
│               ┌─────────────┐                               │
│               │ Inode 12345 │──────► [Data]                │
│               └─────────────┘                               │
│                       ▲                                     │
│                       │                                     │
│   "hardlink.txt" ─────┘                                     │
│                                                             │
│   Bada namnen ar LIKVARDIGA - samma inode, samma data      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Skapa original
echo "Hello World" > original.txt

# Skapa hard link
ln original.txt hardlink.txt

# Se att de har SAMMA inode
ls -li original.txt hardlink.txt
# 12345678 -rw-r--r-- 2 john john 12 original.txt
# 12345678 -rw-r--r-- 2 john john 12 hardlink.txt

# Radera original - data finns kvar!
rm original.txt
cat hardlink.txt
# Hello World
```

| Egenskap | Hard Link |
|----------|-----------|
| Samma inode | Ja |
| Data kvar om original raderas | Ja |
| Fungerar over filsystem | Nej |
| Kan lanka kataloger | Nej |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Symbolic Links (Symlinks)

En symlink ar en pekare till ett FILNAMN - inte inoden.

```
┌─────────────────────────────────────────────────────────────┐
│                     SYMBOLIC LINK                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   "symlink" ─────► "/path/to/original.txt" ─────► [Data]   │
│   (egen inode)     (pekar pa NAMNET)                        │
│                                                             │
│   Om original.txt raderas:                                  │
│   "symlink" ─────► "/path/to/original.txt" ─────► BROKEN!  │
│                    (namnet finns inte langre)               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Skapa symlink
ln -s /var/log/syslog loggen

# Se lanken
ls -la loggen
# lrwxrwxrwx 1 john john 15 loggen -> /var/log/syslog

# Anvand lanken
cat loggen   # Visar syslog
```

| Egenskap | Symlink |
|----------|---------|
| Egen inode | Ja |
| Data kvar om original raderas | Nej (broken) |
| Fungerar over filsystem | Ja |
| Kan lanka kataloger | Ja |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jamforelse

| Aspekt | Hard Link | Symlink |
|--------|-----------|---------|
| Skapas med | `ln file link` | `ln -s file link` |
| Samma inode | Ja | Nej |
| Original raderas | Data kvar | Broken link |
| Over filsystem | Nej | Ja |
| Kataloger | Nej | Ja |
| Anvandning | Backup, dedup | Deploy, genvagar |

```bash
# Test: skapa bada typer
echo "Test" > source.txt
ln source.txt hard_copy      # Hard link
ln -s source.txt soft_copy   # Symlink

# Se skillnaden
ls -li source.txt hard_copy soft_copy
# 12345 ... source.txt
# 12345 ... hard_copy      <- SAMMA inode
# 67890 ... soft_copy -> source.txt   <- ANNAN inode

# Radera original
rm source.txt
cat hard_copy    # FUNGERAR
cat soft_copy    # BROKEN!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inode Exhaustion

Du kan ha ledigt diskutrymme men slut pa inodes!

```bash
# Kolla inode-anvandning
df -i
# Filesystem      Inodes   IUsed   IFree IUse% Mounted on
# /dev/sda1     6553600 1234567 5319033   19% /

# 100% IUse% = kan inte skapa fler filer!

# Hitta manga smafiler
find /tmp -type f | wc -l
```

| Problem | Orsak | Losning |
|---------|-------|---------|
| IUse% = 100% | For manga filer | Radera filer |
| Ledigt utrymme finns | Smafiler (cache) | `find ... -delete` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Symlinks for Deployment

```
Zero-Downtime Deploy:
┌─────────────────────────────────────────────────────────────┐
│  /app/releases/v1.0.0/                                      │
│  /app/releases/v1.1.0/                                      │
│  /app/current ─────► releases/v1.0.0                        │
│                                                             │
│  Deploy ny version:                                         │
│  ln -sfn /app/releases/v1.1.0 /app/current                 │
│                                                             │
│  /app/current ─────► releases/v1.1.0  (atomiskt byte!)     │
│                                                             │
│  Rollback:                                                  │
│  ln -sfn /app/releases/v1.0.0 /app/current                 │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Atomisk symlink-switch
ln -sfn /app/releases/v1.1.0 /app/current
# -s = symbolic
# -f = force (ersatt)
# -n = no-dereference

# Rollback pa 1 sekund!
ln -sfn /app/releases/v1.0.0 /app/current
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Inode** | Filens ID-kort, filnamn ar bara etikett |
| **Hard link** | Extra namn, data kvar till alla borta |
| **Symlink** | Pekare till namn, blir broken om mal forsvinner |
| **df -i** | Kolla inodes, 100% = problem |
| **ln -sfn** | Atomisk switch for deploys |

**Kom ihag:**
- Inode = metadata, filnamn = etikett
- Hard link = samma inode
- Symlink = pekare till namn
- `df -i` for inode-kontroll
- `ln -sfn` for zero-downtime deploys
""",
        },
        {
            "title": 'Disk Management',
            "slug": 'disk-management',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Disk Management

Nar disken blir full stannar allt. Har lar du dig hitta vad som tar plats, rensa upp, och hantera diskar som ett proffs.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Disk full larm** | Snabbt hitta vad som tar plats |
| **Nya diskar** | Partitionera och formatera |
| **Utokad lagring** | Nar applikationer vaxer |
| **LVM** | Flexibel diskhantering i produktion |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kolla diskutrymme med df

```
Disk Usage Overview:
┌─────────────────────────────────────────────────────────────┐
│  df -h                                                      │
├─────────────────────────────────────────────────────────────┤
│  Filesystem      Size  Used Avail Use% Mounted on          │
│  /dev/sda1        50G   35G   13G  73% /                   │
│  /dev/sdb1       100G   80G   15G  85% /data               │
│  tmpfs           2.0G  100M  1.9G   5% /tmp                │
└─────────────────────────────────────────────────────────────┘
```

| Kommando | Beskrivning |
|----------|-------------|
| `df -h` | Diskutrymme (human-readable) |
| `df -h /var/log` | Specifik katalog |
| `df -i` | Inode-anvandning |

```bash
# Oversikt av alla filsystem
df -h

# Specifik katalog
df -h /var/log

# Inodes (kan ta slut aven om disk har plats)
df -i
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hitta vad som tar plats med du

| Kommando | Beskrivning |
|----------|-------------|
| `du -sh /path` | Storlek pa katalog |
| `du -sh /path/*` | Storlek per underkatalog |
| `du -sh /* \\| sort -rh` | Storsta forst |

```bash
# Storlek pa katalog
du -sh /var/log
# 2.5G    /var/log

# Per underkatalog
du -sh /var/log/*
# 1.2G    /var/log/syslog
# 800M    /var/log/nginx

# Hitta storsta katalogerna
du -sh /* 2>/dev/null | sort -rh | head -10
# 15G     /var
# 8.5G    /usr
# 3.2G    /home
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hitta stora filer

| Kommando | Beskrivning |
|----------|-------------|
| `find / -size +100M` | Filer storre an 100MB |
| `find /var -size +50M -exec ls -lh {} \\;` | Med detaljer |

```bash
# Hitta filer storre an 100MB
find / -type f -size +100M 2>/dev/null

# Med storlek och datum
find /var/log -type f -size +50M -exec ls -lh {} \\;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbstadning

| Kommando | Effekt |
|----------|--------|
| `journalctl --vacuum-time=7d` | Rensa loggar aldre an 7 dagar |
| `apt clean` | Rensa paket-cache |
| `find ... -delete` | Radera gamla filer |

```bash
# Rensa systemloggar (behall senaste veckan)
sudo journalctl --vacuum-time=7d

# Rensa apt cache (Ubuntu/Debian)
sudo apt clean

# Radera komprimerade loggar aldre an 30 dagar
find /var/log -name "*.log.*.gz" -mtime +30 -delete
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Partitioner och filsystem

```
Disk Structure:
┌─────────────────────────────────────────────────────────────┐
│  lsblk                                                      │
├─────────────────────────────────────────────────────────────┤
│  NAME   SIZE TYPE MOUNTPOINT                                │
│  sda    100G disk                                           │
│  ├─sda1  99G part /                                        │
│  └─sda2   1G part [SWAP]                                   │
│  sdb    500G disk                                           │
│  └─sdb1 500G part /data                                    │
└─────────────────────────────────────────────────────────────┘
```

| Kommando | Beskrivning |
|----------|-------------|
| `lsblk` | Lista diskar och partitioner |
| `fdisk /dev/sdb` | Skapa partition |
| `mkfs.ext4 /dev/sdb1` | Formatera |
| `mount /dev/sdb1 /mnt` | Mounta |

```bash
# Lista diskar
lsblk

# Skapa partition (interaktivt)
sudo fdisk /dev/sdb
# n = ny partition, w = spara

# Formatera
sudo mkfs.ext4 /dev/sdb1

# Mounta
sudo mkdir /mnt/newdisk
sudo mount /dev/sdb1 /mnt/newdisk
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LVM Basics

```
LVM Architecture:
┌─────────────────────────────────────────────────────────────┐
│  Physical Volumes (PV)  ──►  Volume Group (VG)             │
│  /dev/sda3                   ubuntu-vg                      │
│  /dev/sdb1                        │                         │
│                                   ▼                         │
│                          Logical Volumes (LV)               │
│                          root-lv, swap-lv                   │
└─────────────────────────────────────────────────────────────┘
```

| Kommando | Beskrivning |
|----------|-------------|
| `pvs` | Lista Physical Volumes |
| `vgs` | Lista Volume Groups |
| `lvs` | Lista Logical Volumes |
| `lvextend -L +50G` | Utoka volym |
| `resize2fs` | Utoka filsystem |

```bash
# Visa LVM-struktur
sudo pvs   # Physical Volumes
sudo vgs   # Volume Groups
sudo lvs   # Logical Volumes

# Utoka en LVM-volym
sudo lvextend -L +50G /dev/ubuntu/root
sudo resize2fs /dev/ubuntu/root
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| "No space left" | Disk full | `du -sh /* \\| sort -rh` |
| "No space" men df visar plats | Slut pa inodes | `df -i` |
| Kan inte mounta | Fel filsystemstyp | `mkfs.ext4` |
| resize2fs funkar inte | XFS filsystem | `xfs_growfs` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **df -h** | Snabb oversikt per filsystem |
| **du -sh** | Hitta vad som tar plats |
| **find -size** | Hitta stora filer |
| **journalctl --vacuum** | Rensa loggar |
| **LVM** | Flexibel diskhantering |

**Kom ihag:**
- `df -h` for oversikt
- `du -sh /path/* | sort -rh` for att hitta storheter
- `find -size +100M` for stora filer
- LVM kan utoka volymer live
- Rensa loggar regelbundet
""",
        },
        {
            "title": 'Process Lifecycle and States',
            "slug": 'process-lifecycle',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Process Lifecycle and States

Processer ar allt som kor i Linux - fran din terminal till webservrar. Har lar du dig forsta hur de fungerar, vilka tillstand de kan vara i, och hur du hanterar dem.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Process hanger** | Forsta och fixa problemet |
| **Zombie-processer** | Identifiera och stada upp |
| **Processtrad** | Forsta vad som startade vad |
| **Optimering** | Resource-anvandning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Processer i Linux

```
Process Hierarchy:
┌─────────────────────────────────────────────────────────────┐
│  systemd (PID 1) ─────────── Forsta processen              │
│       │                                                     │
│       ├── sshd ─────────────── SSH-daemon                  │
│       │     └── bash ────────── Ditt shell                 │
│       │           └── vim ───── Din editor                 │
│       │                                                     │
│       ├── nginx ────────────── Webbserver                  │
│       │     ├── worker                                     │
│       │     └── worker                                     │
│       │                                                     │
│       └── mysqld ───────────── Databas                     │
└─────────────────────────────────────────────────────────────┘
```

| Begrepp | Beskrivning |
|---------|-------------|
| **PID** | Process ID (unikt nummer) |
| **PPID** | Parent PID (foraldern) |
| **USER** | Vem kor processen |
| **STAT** | Processtillstand |

```bash
# Visa processer
ps aux | head -5

# Ditt shells PID
echo $$

# Foralderns PID
echo $PPID
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Process States (STAT)

| State | Namn | Beskrivning |
|-------|------|-------------|
| `R` | Running | Kor just nu pa CPU |
| `S` | Sleeping | Vantar pa nago (disk, natverk) |
| `D` | Uninterruptible | Vantar pa I/O, kan inte avbrytas |
| `T` | Stopped | Pausad (t.ex. Ctrl+Z) |
| `Z` | Zombie | Klar men foraldern har inte hamtat |

| Extra | Betydelse |
|-------|-----------|
| `s` | Session leader |
| `l` | Multi-threaded |
| `+` | I forgrunden |
| `<` | Hog prioritet |
| `N` | Lag prioritet |

```bash
# Se STAT for processer
ps aux | grep nginx
# root  1234  0.0  0.1 Ss   nginx: master
# www   1235  0.2  0.5 S    nginx: worker
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Zombie-processer

```
Zombie Process:
┌─────────────────────────────────────────────────────────────┐
│  En zombie ar en process som ar KLAR men vars foralder     │
│  inte har "hamtat" den annu.                               │
│                                                             │
│  - Tar ingen CPU eller minne                               │
│  - Upptar plats i processtabellen                          │
│  - KAN INTE dodas med kill!                                │
│  - Losning: doda foraldern                                 │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Hitta zombies
ps aux | grep Z

# Hitta zombiens foralder
ps -o ppid= -p 5678

# Doda foraldern (zombien forsvinner)
kill 1234
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Processtrad

| Kommando | Beskrivning |
|----------|-------------|
| `pstree` | Visa processtrad |
| `pstree -p` | Med PID |
| `pstree -p 1234` | Fran specifik process |

```bash
# Visa processtrad
pstree
# systemd─┬─sshd───sshd───bash───pstree
#         ├─nginx─┬─nginx
#         │       └─nginx
#         └─mysqld

# Med PID
pstree -p
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Process-information i /proc

| Fil | Innehall |
|-----|----------|
| `/proc/PID/status` | Overgripande info |
| `/proc/PID/fd/` | Oppna filer |
| `/proc/PID/cmdline` | Startkommando |
| `/proc/PID/environ` | Miljovariabler |

```bash
# Detaljerad info
cat /proc/1234/status

# Oppna filer
ls /proc/1234/fd/

# Hur processen startades
cat /proc/1234/cmdline | tr '\\0' ' '
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Zombies hopar sig | Dalig foralder | Doda foraldern |
| Process i D-state | Vantar pa disk | Vanta eller reboot |
| Hogt CPU | Runaway process | `top`, sedan `kill` |
| Processen kan inte dodas | Kernel-state | `kill -9` eller reboot |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **PID/PPID** | Unikt ID och foralder |
| **STAT** | R=running, S=sleeping, Z=zombie |
| **Zombies** | Doda foraldern, inte zombien |
| **pstree** | Se hur processer hanger ihop |
| **/proc/PID/** | All info om en process |

**Kom ihag:**
- PID = unikt, PPID = foralder
- Zombies kan inte dodas - doda foraldern
- `pstree` visar relationer
- `/proc/PID/` innehaller allt
""",
        },
        {
            "title": 'Foreground vs Background Processes',
            "slug": 'foreground-background-processes',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Foreground vs Background Processes

Nar du jobbar med Linux-servrar maste du kunna kora langvariga processer utan att blockera terminalen. Har lar du dig skilja pa forgrund och bakgrund.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Problem utan kunskap |
|----------|---------------------|
| **SSH tappar anslutning** | Langvarigt jobb avbryts |
| **Maste gora flera saker** | Terminaln blockerad |
| **Backup pa natten** | Maste vara inloggad |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Forgrund vs Bakgrund

```
Terminal Control:
┌─────────────────────────────────────────────────────────────┐
│  FORGRUND                   │  BAKGRUND                    │
│  ─────────                  │  ─────────                   │
│  - Blockerar terminalen     │  - Terminal fri              │
│  - Ctrl+C avbryter          │  - Maste anvanda kill        │
│  - Direkt output            │  - Output kan ga forlorad    │
│  - Standard for kommandon   │  - Kraver & eller bg         │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Forgrund - terminalen blockeras
sleep 60
# Ctrl+C avbryter

# Bakgrund med &
sleep 60 &
# [1] 12345
# Terminalen fri
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jobs-kommandot

| Kommando | Beskrivning |
|----------|-------------|
| `jobs` | Lista alla jobb |
| `jobs -l` | Med PID |
| `jobs -p` | Bara PID |

| Symbol | Betydelse |
|--------|-----------|
| `+` | Current job (default for fg) |
| `-` | Previous job |

```bash
jobs
# [1]+  Running    sleep 60 &
# [2]-  Stopped    vim file.txt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Flytta mellan forgrund och bakgrund

| Kommando | Funktion |
|----------|----------|
| `Ctrl+Z` | Pausa forgrundsprocess |
| `fg` | Ta tillbaka till forgrund |
| `fg %1` | Specifikt jobb till forgrund |
| `bg` | Fortsatt i bakgrund |
| `bg %1` | Specifikt jobb i bakgrund |

```bash
# Pausa med Ctrl+Z
vim file.txt
# [1]+  Stopped    vim file.txt

# Tillbaka till forgrund
fg %1

# Eller bakgrund
bg %1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Overleva logout med nohup

| Problem | Losning |
|---------|---------|
| Process dor vid logout | `nohup` |
| Output forsvinner | Redirect till fil |
| Glomde nohup | `disown` |

```bash
# Overlev logout
nohup ./backup.sh &

# Med loggfil
nohup ./backup.sh > backup.log 2>&1 &

# Glomde nohup? Anvand disown
./long_job.sh &
disown %1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Screen/tmux for langvariga jobb

```
Session Management:
┌─────────────────────────────────────────────────────────────┐
│  screen -S deploy      Skapa session                       │
│  Ctrl+A, D             Detach (koppla loss)                │
│  screen -ls            Lista sessioner                     │
│  screen -r deploy      Ateranslut                          │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Starta session
screen -S deploy

# Kor kommandon, sen Ctrl+A, D

# Ateranslut senare
screen -r deploy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt exempel

```bash
# Dalligt - dor vid disconnect
./deploy.sh

# Bra - bakgrund
./deploy.sh &

# Bast - overlever logout med logg
nohup ./deploy.sh > /var/log/deploy.log 2>&1 &
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **&** | Starta i bakgrund |
| **Ctrl+Z** | Pausa process |
| **jobs** | Lista bakgrundsjobb |
| **fg/bg** | Flytta mellan forgrund/bakgrund |
| **nohup** | Overlev logout |
| **screen** | Battre for interaktiva jobb |

**Kom ihag:**
- & startar direkt i bakgrund
- Ctrl+Z pausar, bg fortsatter
- nohup for langvariga jobb
- screen/tmux for interaktiva sessioner
""",
        },
        {
            "title": 'Job Control (jobs, fg, bg, nohup)',
            "slug": 'job-control',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Job Control (jobs, fg, bg, nohup)

Jobbkontroll ar konsten att hantera flera processer fran en terminal - pausa, ateruppta, och se till att de overlever aven om du tappar anslutningen.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Langvarig backup** | Kor i bakgrund |
| **SSH tappar** | Jobb maste overleva |
| **Flera jobb** | Parallellt arbete |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jobs-kommandot

```
Job Notation:
┌─────────────────────────────────────────────────────────────┐
│  %1    Jobb nummer 1                                       │
│  %+    Current job (default)                               │
│  %-    Previous job                                        │
│  %%    Samma som %+                                        │
└─────────────────────────────────────────────────────────────┘
```

| Kommando | Beskrivning |
|----------|-------------|
| `jobs` | Lista alla jobb |
| `jobs -l` | Med PID |
| `jobs -p` | Bara PID |

```bash
jobs
# [1]+  Running    ./backup.sh &
# [2]-  Stopped    vim config.txt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pausa och ateruppta

| Aktion | Kommando |
|--------|----------|
| Pausa | `Ctrl+Z` |
| Bakgrund | `bg %1` |
| Forgrund | `fg %1` |
| Starta i bakgrund | `kommando &` |

```bash
# Pausa korande process
./script.sh
# Ctrl+Z
# [1]+  Stopped    ./script.sh

# Fortsatt i bakgrund
bg %1

# Eller forgrund
fg %1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Starta flera jobb parallellt

```bash
# Tre jobb samtidigt
./job1.sh &
./job2.sh &
./job3.sh &

# Kontrollera
jobs
# [1]   Running    ./job1.sh &
# [2]-  Running    ./job2.sh &
# [3]+  Running    ./job3.sh &
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## nohup - overlev logout

| Kommando | Funktion |
|----------|----------|
| `nohup cmd &` | Ignorera SIGHUP |
| `nohup cmd > log 2>&1 &` | Med loggfil |

```bash
# Basic nohup
nohup ./backup.sh &
# Output till nohup.out

# Med egen loggfil
nohup ./backup.sh > backup.log 2>&1 &
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## disown - radda glomda jobb

| Kommando | Funktion |
|----------|----------|
| `disown %1` | Ta bort fran shell |
| `disown -h %1` | Markera att ignorera SIGHUP |

```bash
# Glomde nohup?
./long_job.sh &
disown %1
# Nu overlever den logout
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt exempel

```bash
# Starta migrering
./migrate.sh
# Tar lang tid... Ctrl+Z

# Flytta till bakgrund
bg %1

# Se till att overleva logout
disown -h %1

# Kolla senare
ps aux | grep migrate
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Ctrl+Z** | Pausa process |
| **bg/fg** | Flytta mellan bakgrund/forgrund |
| **nohup** | Overlev logout |
| **disown** | Radda glomda jobb |
| **%n** | Referera till jobb nummer n |

**Kom ihag:**
- Ctrl+Z pausar, bg fortsatter
- nohup for nya jobb, disown for gloemda
- jobs visar alla jobb i sessionen
- PID och jobbnummer ar olika saker
""",
        },
        {
            "title": 'Signals (SIGTERM, SIGKILL, SIGHUP)',
            "slug": 'signals',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Signals (SIGTERM, SIGKILL, SIGHUP)

Signaler ar hur Linux kommunicerar med processer - fran Ctrl+C till graceful shutdown. Har lar du dig anvanda dem ratt for att undvika dataforlust.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Graceful shutdown** | Lat process stada upp |
| **Reload config** | Utan omstart |
| **Hanterad process** | Doda korrekt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## De viktigaste signalerna

| Signal | Nummer | Beskrivning | Kan ignoreras? |
|--------|--------|-------------|----------------|
| SIGTERM | 15 | Be snallt avsluta | Ja |
| SIGKILL | 9 | Tvangsavsluta | Nej |
| SIGINT | 2 | Avbryt (Ctrl+C) | Ja |
| SIGHUP | 1 | Terminal stangdes / reload | Ja |
| SIGSTOP | 19 | Pausa process | Nej |
| SIGCONT | 18 | Fortsatt process | Ja |

```bash
# Lista alla signaler
kill -l
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SIGTERM vs SIGKILL

```
Signal Comparison:
┌─────────────────────────────────────────────────────────────┐
│  SIGTERM (15)               │  SIGKILL (9)                 │
│  ────────────               │  ────────────                │
│  - "Snalla avsluta"         │  - "Do. Nu."                 │
│  - Process far stada        │  - Ingen cleanup             │
│  - Kan ignoreras            │  - Kan INTE ignoreras        │
│  - Forst val                │  - Sista utväg               │
│  - Sparar data              │  - Risk for dataforlust      │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Ratt ordning:
kill 12345          # SIGTERM forst
sleep 5             # Vanta
kill -9 12345       # SIGKILL om nodvandigt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## kill, killall, pkill

| Kommando | Anvandning |
|----------|------------|
| `kill PID` | Doda via PID |
| `kill -9 PID` | Tvangsavsluta |
| `killall namn` | Doda alla med namn |
| `pkill -f monster` | Doda via monster |
| `pgrep namn` | Hitta PID |

```bash
# Via PID
kill 12345

# Via namn
killall nginx

# Via monster i kommandorad
pkill -f "python backup.py"

# Hitta forst
pgrep nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SIGHUP for reload

| Tjanst | Effekt av SIGHUP |
|--------|------------------|
| nginx | Laser om config |
| sshd | Laser om config |
| apache | Graceful restart |

```bash
# Reload nginx
kill -HUP $(cat /var/run/nginx.pid)

# Eller via systemd
sudo systemctl reload nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## trap i scripts

```bash
#!/bin/bash
cleanup() {
    echo "Stadar upp..."
    rm -f /tmp/myapp_*
    exit 0
}

# Fanga signaler
trap cleanup SIGTERM SIGINT

# Script logik har...
while true; do
    sleep 1
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **SIGTERM** | Be snallt, lat stada |
| **SIGKILL** | Tvinga, sista utvag |
| **SIGHUP** | Reload config |
| **Ctrl+C** | Skickar SIGINT |
| **trap** | Fanga signaler i script |

**Kom ihag:**
- Alltid SIGTERM forst
- SIGKILL bara om nodvandigt
- SIGHUP for reload utan omstart
- Anvand trap for graceful cleanup
""",
        },
        {
            "title": 'Process Monitoring (ps, top, htop)',
            "slug": 'process-monitoring',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Process Monitoring (ps, top, htop)

Nar servern blir langsam ar processovervakning ditt forsta verktyg. Har lar du dig identifiera vilken process som ater CPU eller minne.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Verktyg |
|----------|---------|
| **Hog CPU** | top, htop |
| **Minneslacka** | ps --sort=-%mem |
| **Port upptagen** | lsof -i :port |
| **Hitta PID** | pgrep |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ps - ogonblicksbild

| Flagga | Betydelse |
|--------|-----------|
| `a` | Alla anvandarnas processer |
| `u` | User-format |
| `x` | Aven utan terminal |
| `--sort=-cpu` | Sortera pa CPU |
| `--sort=-mem` | Sortera pa minne |

| Kolumn | Betydelse |
|--------|-----------|
| PID | Process ID |
| %CPU | CPU-anvandning |
| %MEM | Minnesanvandning |
| RSS | Fysiskt minne |
| STAT | Tillstand |

```bash
ps aux | head -5
ps aux | grep nginx
ps aux --sort=-%mem | head -10
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## top - realtidsovervakning

```
Top Interface:
┌─────────────────────────────────────────────────────────────┐
│  load average: 0.52, 0.48, 0.45                            │
│  ──────────────────────────                                │
│  1 min  5 min  15 min                                      │
│  Under antal CPU-karnor = OK                               │
└─────────────────────────────────────────────────────────────┘
```

| Tangent | Funktion |
|---------|----------|
| `M` | Sortera pa minne |
| `P` | Sortera pa CPU |
| `k` | Doda process |
| `1` | Visa alla CPU-karnor |
| `q` | Avsluta |

```bash
top
top -bn1 | head -20  # Batch mode for scripts
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## htop - modern overvakning

| Funktion | Tangent |
|----------|---------|
| Tradvy | `F5` |
| Doda process | `F9` |
| Sok | `F3` |
| Filter | `F4` |

```bash
# Installera
sudo apt install htop

# Kor
htop

# For specifik anvandare
htop -u www-data
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pgrep och lsof

| Kommando | Funktion |
|----------|----------|
| `pgrep namn` | Hitta PID for process |
| `pgrep -f monster` | Sok i kommandorad |
| `lsof -i :port` | Vad anvander porten? |
| `lsof -p PID` | Vad har processen oppet? |

```bash
# Hitta nginx PID
pgrep nginx

# Vem lyssnar pa port 80?
lsof -i :80

# Vad har process 1234 oppet?
lsof -p 1234
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsokningsworkflow

```bash
# 1. Kolla load
uptime

# 2. Hitta CPU-slukare
top -bn1 | head -20

# 3. Kolla minne
free -h

# 4. Hitta minnesslukare
ps aux --sort=-%mem | head -10

# 5. Kolla specifik port
lsof -i :3000
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **ps aux** | Ogonblicksbild av processer |
| **top/htop** | Realtidsovervakning |
| **pgrep** | Hitta PID snabbt |
| **lsof** | Oppna filer och portar |
| **load average** | Under antal karnor = OK |

**Kom ihag:**
- ps for ogonblicksbild, top for realtid
- htop ar lattare att anvanda
- lsof -i :port for "address in use"
- load average under antal karnor ar bra
""",
        },
        {
            "title": 'Systemd Architecture',
            "slug": 'systemd-architecture',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Systemd Architecture

Systemd ar hjartat i moderna Linux - det ar PID 1 som startar och hanterar alla tjanster. Har lar du dig forsta hur det fungerar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Tjanst startar inte** | Forsta dependencies |
| **Automatisk omstart** | Konfigurera korrekt |
| **Boot-ordning** | Hantera beroenden |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Systemd oversikt

```
Systemd Hierarchy:
┌─────────────────────────────────────────────────────────────┐
│  systemd (PID 1)                                           │
│       │                                                     │
│       ├── service units ────── nginx, postgres, etc        │
│       ├── socket units ─────── aktivering via socket       │
│       ├── timer units ──────── schemalagda jobb            │
│       ├── target units ─────── grupper (multi-user)        │
│       └── mount units ──────── filsystem                   │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Verifiera PID 1
ps -p 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Unit-typer

| Typ | Anvandning |
|-----|------------|
| `service` | Tjanster (nginx, postgres) |
| `socket` | Aktivering via socket |
| `timer` | Schemalagda jobb |
| `target` | Grupper av units |
| `mount` | Filsystem |
| `path` | Overvaka filer |

```bash
# Lista services
systemctl list-units --type=service --state=running
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Unit-filer - var finns de?

| Sokväg | Anvandning |
|--------|------------|
| `/lib/systemd/system/` | Paketinstallerade (ror ej) |
| `/etc/systemd/system/` | Dina egna |
| `/run/systemd/system/` | Runtime (temporara) |

```bash
# Hitta var unit kommer fran
systemctl show nginx --property=FragmentPath
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dependencies

| Direktiv | Betydelse |
|----------|-----------|
| `After=` | Starta efter |
| `Before=` | Starta fore |
| `Requires=` | Hard dependency |
| `Wants=` | Mjuk dependency |

```bash
# Se dependencies
systemctl list-dependencies nginx

# Reverse dependencies
systemctl list-dependencies --reverse nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Targets

| Target | Beskrivning |
|--------|-------------|
| `multi-user.target` | Normalt korlage |
| `graphical.target` | Skrivbord |
| `rescue.target` | Rescue mode |
| `emergency.target` | Minimal boot |

```bash
# Aktuellt target
systemctl get-default

# Andra default
sudo systemctl set-default multi-user.target
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cgroups - resurskontroll

```bash
# Se process-hierarki
systemd-cgls

# Resursanvandning per tjanst
systemd-cgtop
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **PID 1** | systemd ar forst |
| **Units** | Services, timers, targets |
| **/etc/systemd/system/** | Dina egna tjanster |
| **Targets** | Grupper av tjanster |
| **daemon-reload** | Las om efter andringar |

**Kom ihag:**
- systemd startar och overvakar allt
- Units ar byggstenarna
- /etc/systemd/system for egna tjanster
- daemon-reload efter varje andring
""",
        },
        {
            "title": 'Unit Files (service, timer, socket)',
            "slug": 'unit-files',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Unit Files (service, timer, socket)

For att kora dina applikationer som tjanster maste du skapa unit-filer. Har lar du dig syntaxen for services, timers och sockets.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Egen app som tjanst** | Automatisk start vid boot |
| **Schemalagda jobb** | Timer istallet for cron |
| **On-demand start** | Socket activation |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service unit struktur

```
Unit File Sections:
┌─────────────────────────────────────────────────────────────┐
│  [Unit]        Beskrivning och dependencies                │
│  [Service]     Hur tjansten kors                           │
│  [Install]     Nar den aktiveras                           │
└─────────────────────────────────────────────────────────────┘
```

| Sektion | Direktiv | Betydelse |
|---------|----------|-----------|
| [Unit] | Description | Vad tjansten gor |
| [Unit] | After | Starta efter |
| [Unit] | Requires | Hard dependency |
| [Service] | Type | simple, forking, oneshot |
| [Service] | ExecStart | Startkommando |
| [Service] | Restart | on-failure, always |
| [Install] | WantedBy | multi-user.target |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Exempel: Service unit

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/server
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Timer units

| OnCalendar | Betydelse |
|------------|-----------|
| `*-*-* 02:00:00` | Varje dag kl 02:00 |
| `*-*-* *:00:00` | Varje timme |
| `Mon *-*-* 10:00` | Mandag 10:00 |
| `*-*-01 00:00:00` | Forsta dagen varje manad |

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable --now backup.timer
systemctl list-timers
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Socket units

```ini
# /etc/systemd/system/myapp.socket
[Unit]
Description=MyApp Socket

[Socket]
ListenStream=8080
Accept=no

[Install]
WantedBy=sockets.target
```

Tjansten startas forst nar nagon ansluter till porten.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Viktiga direktiv

| Direktiv | Varde | Betydelse |
|----------|-------|-----------|
| Type | simple | ExecStart ar huvudprocess |
| Type | forking | Process forkar |
| Type | oneshot | Kor en gang |
| Restart | on-failure | Vid krasch |
| Restart | always | Alltid |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **[Unit]** | Beskrivning och dependencies |
| **[Service]** | Hur den kors |
| **[Install]** | Nar den aktiveras |
| **daemon-reload** | ALLTID efter andringar |
| **Timer** | Modern cron |

**Kom ihag:**
- daemon-reload efter varje andring
- enable --now for bade enable och start
- Timer units ar battre an cron
- Socket activation sparar resurser
""",
        },
        {
            "title": 'Service Management (systemctl)',
            "slug": 'service-management',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Service Management (systemctl)

Varje webbserver, databas och applikation pa en Linux-server kor som en tjanst. Har lar du dig hantera dem med systemctl.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Kommando |
|----------|----------|
| **Starta tjanst** | `systemctl start` |
| **Starta om efter deploy** | `systemctl restart` |
| **Reload config** | `systemctl reload` |
| **Felsokning** | `systemctl status` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande kommandon

| Kommando | Funktion |
|----------|----------|
| `start` | Starta tjanst |
| `stop` | Stoppa tjanst |
| `restart` | Stop + start |
| `reload` | Las om config (ingen nedtid) |
| `status` | Visa status |

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
systemctl status nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Enable/Disable

| Kommando | Funktion |
|----------|----------|
| `enable` | Starta vid boot |
| `disable` | Starta INTE vid boot |
| `enable --now` | Enable + start |
| `is-enabled` | Kolla om enabled |

```bash
sudo systemctl enable nginx
sudo systemctl enable --now nginx
systemctl is-enabled nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lista tjanster

| Kommando | Visar |
|----------|-------|
| `list-units --type=service` | Aktiva tjanster |
| `--state=running` | Korande |
| `--state=failed` | Kraschade |
| `list-unit-files --type=service` | Alla installerade |

```bash
systemctl list-units --type=service --state=running
systemctl list-units --type=service --state=failed
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Mask/Unmask

| Kommando | Funktion |
|----------|----------|
| `mask` | Forhindra start helt |
| `unmask` | Ta bort maskering |

```bash
# Mask - kan INTE startas
sudo systemctl mask apache2

# Unmask - kan startas igen
sudo systemctl unmask apache2
```

| Metod | Kan startas manuellt? | Startar vid boot? |
|-------|----------------------|-------------------|
| disable | Ja | Nej |
| mask | Nej | Nej |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deploy-workflow

```bash
# 1. Kolla status
systemctl is-active myapp

# 2. Deploy kod...

# 3. Restart
sudo systemctl restart myapp

# 4. Verifiera
systemctl status myapp
journalctl -u myapp -n 20
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **start/stop/restart** | Kontrollera tjanster |
| **reload** | Ingen nedtid |
| **enable --now** | Enable + start |
| **status** | Forsta vid problem |
| **--failed** | Hitta kraschade |

**Kom ihag:**
- restart for kod-andringar
- reload for config-andringar
- status visar senaste loggar
- is-active for scripts
""",
        },
        {
            "title": 'Boot Process and Targets',
            "slug": 'boot-process-targets',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Boot Process and Targets

Nar en server inte startar behover du forsta bootprocessen for att felstoka. Har lar du dig hela kedjan fran strom till korande system.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Server bootar inte** | Felstok i kedjan |
| **Rescue mode** | Fixa trasigt system |
| **Boot-ordning** | Konfigurera targets |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Boot-sekvensen

```
Boot Process:
┌─────────────────────────────────────────────────────────────┐
│  1. BIOS/UEFI ──── Hittar boot-enhet                       │
│         │                                                   │
│  2. GRUB ─────── Laddar kernel + initramfs                 │
│         │                                                   │
│  3. Kernel ───── Initierar hardvara                        │
│         │                                                   │
│  4. Initramfs ── Mountar riktiga root                      │
│         │                                                   │
│  5. Systemd ──── Startar tjanster                          │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Targets (systemds runlevels)

| Target | Beskrivning | Runlevel |
|--------|-------------|----------|
| poweroff.target | Stang av | 0 |
| rescue.target | Single user | 1 |
| multi-user.target | Server-standard | 3 |
| graphical.target | Med GUI | 5 |
| reboot.target | Omstart | 6 |

```bash
# Aktuellt default target
systemctl get-default

# Andra default
sudo systemctl set-default multi-user.target
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Byta target vid korning

| Kommando | Funktion |
|----------|----------|
| `isolate rescue.target` | Ga till rescue |
| `isolate multi-user.target` | Tillbaka till normalt |
| `poweroff` | Stang av |
| `reboot` | Starta om |

```bash
sudo systemctl isolate rescue.target
sudo systemctl reboot
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GRUB bootloader

| Fil | Funktion |
|-----|----------|
| `/etc/default/grub` | Konfiguration |
| `GRUB_DEFAULT` | Vilken menypost |
| `GRUB_TIMEOUT` | Sekunder innan boot |

```bash
# Uppdatera GRUB efter andringar
sudo update-grub
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rescue och Emergency mode

| Mode | Anvandning |
|------|------------|
| rescue | Root-shell, minimala tjanster |
| emergency | Annu mer minimalt, ro filsystem |

```bash
# Via GRUB:
# 1. Tryck 'e' vid menyn
# 2. Lagg till: systemd.unit=rescue.target
# 3. Ctrl+X for att boota

# I emergency mode:
mount -o remount,rw /
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felstok boot-problem

```bash
# Loggar fran aktuell boot
journalctl -b

# Foregaende boot
journalctl -b -1

# Bara fel
journalctl -b -p err
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Boot-sekvens** | BIOS > GRUB > Kernel > systemd |
| **multi-user.target** | Server-standard |
| **rescue.target** | Felstokningslage |
| **journalctl -b** | Boot-loggar |
| **update-grub** | Efter GRUB-andringar |

**Kom ihag:**
- multi-user.target for servrar
- rescue.target for att fixa trasiga system
- journalctl -b -1 for forra bootens loggar
- mount -o remount,rw / i emergency
""",
        },
        {
            "title": 'Journald and Logging',
            "slug": 'journald-logging',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Journald and Logging

Loggar ar dina ogon in i systemet. Nar nagot gar fel ar journalctl forsta verktyget du anvander. Har lar du dig bemstra logganalys.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Kommando |
|----------|----------|
| **Tjanst kraschade** | `journalctl -u tjanst` |
| **Senaste errors** | `journalctl -p err` |
| **Realtid** | `journalctl -f` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## journalctl grundlaggande

| Kommando | Funktion |
|----------|----------|
| `journalctl` | Alla loggar |
| `journalctl -f` | Follow (realtid) |
| `journalctl -n 50` | Senaste 50 rader |
| `journalctl --since "1 hour ago"` | Senaste timmen |

```bash
journalctl -f
# Ctrl+C for att avsluta
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filtrera efter tjanst

| Kommando | Funktion |
|----------|----------|
| `-u nginx` | Nginx loggar |
| `-u nginx -f` | Follow nginx |
| `-u nginx -u postgres` | Flera tjanster |

```bash
journalctl -u nginx -n 100
journalctl -u nginx -f
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filtrera efter prioritet

| Prioritet | Nummer | Beskrivning |
|-----------|--------|-------------|
| emerg | 0 | System oanvandbart |
| alert | 1 | Atgard kravs nu |
| crit | 2 | Kritiskt |
| err | 3 | Fel |
| warning | 4 | Varning |
| notice | 5 | Normalt men viktigt |
| info | 6 | Information |
| debug | 7 | Debug |

```bash
journalctl -p err          # Errors och varre
journalctl -p warning      # Warnings och varre
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Boot-loggar

| Kommando | Funktion |
|----------|----------|
| `-b` | Aktuell boot |
| `-b -1` | Forra booten |
| `--list-boots` | Lista alla bootar |

```bash
journalctl -b
journalctl -b -1 -p err
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Traditionella loggar i /var/log/

| Fil | Innehall |
|-----|----------|
| `auth.log` | Inloggningar, sudo |
| `syslog` | Systemmeddelanden |
| `nginx/access.log` | HTTP requests |
| `nginx/error.log` | Nginx fel |

```bash
sudo tail -f /var/log/auth.log
sudo tail -f /var/log/nginx/error.log
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logrotate

Automatisk rotation av loggar for att spara diskutrymme.

```bash
cat /etc/logrotate.d/nginx
# daily, rotate 14, compress
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsokningsworkflow

```bash
# 1. Status
systemctl status myapp

# 2. Senaste loggar
journalctl -u myapp -n 100

# 3. Bara errors
journalctl -u myapp -p err --since "1 hour ago"

# 4. Specifik tid
journalctl -u myapp --since "10:00" --until "10:05"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **-u tjanst** | Loggar for tjanst |
| **-f** | Follow realtid |
| **-p err** | Bara errors |
| **-b** | Boot-loggar |
| **/var/log/** | Traditionella filer |

**Kom ihag:**
- journalctl -u tjanst -f for realtid
- -p err for att filtrera bort brus
- -b -1 for forra bootens loggar
- /var/log for applikationsloggar
""",
        },
        {
            "title": 'User and Group Management',
            "slug": 'user-group-management',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# User and Group Management

Linux ar ett multiuser-system. Du maste kunna skapa anvandare for deploy, services och teammedlemmar. Har lar du dig grunderna.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Deploy-anvandare** | CI/CD access |
| **Service accounts** | Applikationer |
| **Teammedlemmar** | SSH-access |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa anvandare

| Kommando | Funktion |
|----------|----------|
| `useradd namn` | Skapa anvandare (minimal) |
| `useradd -m namn` | Med home directory |
| `useradd -m -s /bin/bash namn` | Med home + bash |
| `passwd namn` | Satt losenord |

```bash
sudo useradd -m -s /bin/bash deploy
sudo passwd deploy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Viktiga filer

| Fil | Innehall |
|-----|----------|
| `/etc/passwd` | Anvandare |
| `/etc/shadow` | Hashade losenord |
| `/etc/group` | Grupper |

```bash
# passwd-format:
# namn:x:UID:GID:Kommentar:Home:Shell
cat /etc/passwd | grep deploy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Modifiera anvandare

| Kommando | Funktion |
|----------|----------|
| `usermod -aG grupp user` | Lagg till i grupp |
| `usermod -s /bin/zsh user` | Byt shell |
| `usermod -L user` | Las konto |
| `usermod -U user` | Las upp konto |

```bash
# VIKTIGT: -a betyder append!
sudo usermod -aG docker deploy
# Utan -a tas andra grupper bort!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grupper

| Kommando | Funktion |
|----------|----------|
| `groupadd namn` | Skapa grupp |
| `groups user` | Visa anvandares grupper |
| `id user` | Detaljerad info |

```bash
sudo groupadd developers
sudo usermod -aG developers john
groups john
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ta bort anvandare

| Kommando | Funktion |
|----------|----------|
| `userdel user` | Ta bort (behall home) |
| `userdel -r user` | Ta bort inkl home |

```bash
# Sakert satt:
sudo tar -czvf /backup/user_home.tar.gz /home/user
sudo userdel -r user
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service accounts

```bash
# System-konto utan login
sudo useradd -r -s /usr/sbin/nologin myapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt: Deploy-anvandare

```bash
# Skapa
sudo useradd -m -s /bin/bash deploy

# SSH-nyckel istallet for losenord
sudo passwd -l deploy
sudo mkdir -p /home/deploy/.ssh
sudo chmod 700 /home/deploy/.ssh

# Lagg till i docker
sudo usermod -aG docker deploy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **useradd -m -s** | Skapa med home och shell |
| **usermod -aG** | Lagg till i grupp (GLOM INTE -a) |
| **groups** | Se anvandares grupper |
| **/usr/sbin/nologin** | For service accounts |
| **userdel -r** | Ta bort inkl home |

**Kom ihag:**
- Alltid -a med usermod -G
- Service accounts med nologin shell
- Backupa innan userdel -r
- id visar all anvandareinfo
""",
        },
        {
            "title": 'Sudo Configuration',
            "slug": 'sudo-configuration',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Sudo Configuration

sudo ar hur anvandare far tillfallig root-access. Ratt konfigurerad sudo ger kontroll over vem som kan gora vad, med fullstandig audit trail.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **CI/CD** | Deploy utan losenord |
| **Automation** | Specifika kommandon |
| **Sakerhet** | Begransad access |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande sudo

| Kommando | Funktion |
|----------|----------|
| `sudo kommando` | Kor som root |
| `sudo -i` | Root shell |
| `sudo -u user kommando` | Kor som annan user |
| `sudo -l` | Lista dina rattigheter |

```bash
sudo apt update
sudo -i
sudo -u postgres psql
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## visudo - redigera sudoers

```bash
# ENDA ratta sattet
sudo visudo

# ALDRIG redigera direkt!
# nano /etc/sudoers  # FEL!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## sudoers syntax

```
Format: vem   var=(som vem)  vad
```

| Exempel | Betydelse |
|---------|-----------|
| `john ALL=(ALL) ALL` | Full access |
| `%admin ALL=(ALL) ALL` | Grupp admin |
| `deploy ALL=(ALL) NOPASSWD: ALL` | Utan losenord (farligt!) |
| `deploy ALL=(ALL) NOPASSWD: /bin/cmd` | Specifikt kommando |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filer i /etc/sudoers.d/

```bash
# Battre an att andra /etc/sudoers
sudo visudo -f /etc/sudoers.d/deploy

# Innehall:
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status myapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best practices

| Godt | Dalligt |
|------|---------|
| NOPASSWD for specifika cmd | NOPASSWD: ALL |
| Anvand sudoers.d/ | Redigera /etc/sudoers direkt |
| Anvand visudo | nano /etc/sudoers |
| Begransade rattigheter | Full access |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsok

```bash
# Kolla syntax
sudo visudo -c

# Se anvandares grupper
groups username

# Kolla sudo-logg
sudo grep sudo /var/log/auth.log
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **visudo** | ENDA sattet att redigera |
| **/etc/sudoers.d/** | Separata filer |
| **NOPASSWD** | Bara specifika cmd |
| **%grupp** | Sudo for grupp |
| **sudo -l** | Se dina rattigheter |

**Kom ihag:**
- Alltid visudo, aldrig nano/vim direkt
- NOPASSWD bara for specifika kommandon
- /etc/sudoers.d/ for egna regler
- Allt loggas i auth.log
""",
        },
        {
            "title": 'PAM Modules',
            "slug": 'pam-modules',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 85,
            "content": """# PAM Modules

PAM (Pluggable Authentication Modules) ar Linux modulsystem for autentisering. Istallet for att varje program har egen auth-kod delegerar de till PAM.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor du behover detta |
|----------|------------------------|
| **Losenordspolicy** | Starka losenord |
| **Grupprestriktioner** | Begransat sudo |
| **Resurslimits** | Processer, filer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PAM-arkitektur

```
PAM Flow:
┌─────────────────────────────────────────────────────────────┐
│  Program (ssh, sudo, login)                                │
│         │                                                   │
│         v                                                   │
│  /etc/pam.d/tjanst ────── Konfiguration                   │
│         │                                                   │
│         v                                                   │
│  PAM moduler (/lib/security/) ── .so filer                 │
└─────────────────────────────────────────────────────────────┘
```

```bash
ls /etc/pam.d/
cat /etc/pam.d/sudo
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PAM-typer

| Typ | Funktion |
|-----|----------|
| auth | Vem ar du? (losenord, etc) |
| account | Far kontot anvandas? |
| password | Losenordsandringar |
| session | Vid login/logout |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kontrollflaggor

| Flagga | Beteende |
|--------|----------|
| required | Maste lyckas, fortsatt anda |
| requisite | Maste lyckas, avbryt vid fel |
| sufficient | Lyckas = klart |
| optional | Spelar ingen roll |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga moduler

| Modul | Funktion |
|-------|----------|
| pam_unix.so | Standard Unix auth |
| pam_wheel.so | Krav wheel-grupp |
| pam_limits.so | Resursbegransningar |
| pam_pwquality.so | Losenordspolicy |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Limits i /etc/security/limits.conf

| Doman | Typ | Objekt | Varde |
|-------|-----|--------|-------|
| @developers | soft | nproc | 1000 |
| * | hard | nofile | 8192 |

```bash
cat /etc/security/limits.conf
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsokning

```bash
# PAM-loggar
sudo grep -i pam /var/log/auth.log

# Testa
pamtester sudo user authenticate
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **/etc/pam.d/** | Konfiguration per tjanst |
| **auth/account/password/session** | Fyra typer |
| **required** | Maste lyckas |
| **pam_limits** | Resursbegransningar |
| **auth.log** | PAM-loggar |

**Kom ihag:**
- En fil per tjanst i /etc/pam.d/
- Ha backup-terminal vid andringar
- Loggar i /var/log/auth.log
- pam_limits for ulimit-settings
""",
        },
        {
            "title": 'SSH Hardening',
            "slug": 'ssh-hardening',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# SSH Hardening

SSH ar dorren till din server och varje exponerad maskin bombarderas konstant med automatiska inloggningsattacker. Hardening handlar om att gora den dorren sa svar att forcera som mojligt genom att lasa ut angripare pa flera nivaer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SSH Hardening Checklista

```
┌─────────────────────────────────────────────────────────────────┐
│                    SSH HARDENING STEG                           │
├─────────────────────────────────────────────────────────────────┤
│  [ ] 1. Byt SSH-port (2222 eller annan)                        │
│  [ ] 2. Inaktivera root login (PermitRootLogin no)             │
│  [ ] 3. Generera SSH-nycklar (ed25519)                         │
│  [ ] 4. Inaktivera losenord (PasswordAuthentication no)        │
│  [ ] 5. Begränsa anvandare (AllowUsers/AllowGroups)            │
│  [ ] 6. Installera fail2ban                                     │
│  [ ] 7. Konfigurera timeouts                                    │
│  [ ] 8. Verifiera med sshd -t                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SSH-konfigurationsfilen

| Kommando | Beskrivning |
|----------|-------------|
| `cat /etc/ssh/sshd_config` | Visa hela konfigurationen |
| `grep -v "^#" /etc/ssh/sshd_config \\| grep -v "^$"` | Visa endast aktiva rader |
| `sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup` | Skapa backup |
| `sudo sshd -t` | Testa konfigurationssyntax |
| `sudo sshd -T` | Visa effektiv konfiguration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 1: Byt SSH-port

```
Port 22 (default)         Port 2222 (ny)
       │                         │
       ▼                         ▼
   ┌───────┐                 ┌───────┐
   │ 99%   │   ───────►      │ <1%   │
   │ bots  │   efter byte    │ bots  │
   └───────┘                 └───────┘
```

```bash
# I /etc/ssh/sshd_config:
Port 2222

# Under overgang - bada portar aktiva:
Port 22
Port 2222

# Testa och applicera
sudo sshd -t                     # verifiera syntax
sudo systemctl restart sshd      # applicera

# Oppna brandvagg
sudo ufw allow 2222/tcp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 2: Inaktivera root-login

| Installning | Effekt |
|-------------|--------|
| `PermitRootLogin no` | Blockerar root helt (rekommenderat) |
| `PermitRootLogin prohibit-password` | Endast nyckel-login for root |
| `PermitRootLogin yes` | Tillater allt (farligt!) |

```bash
# I /etc/ssh/sshd_config:
PermitRootLogin no

# Verifiera att du har sudo-access forst!
sudo grep "^sudo" /etc/group
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 3: SSH-nycklar

| Nyckeltyp | Kommando | Rekommendation |
|-----------|----------|----------------|
| Ed25519 | `ssh-keygen -t ed25519` | Modernast, sakrast |
| RSA 4096 | `ssh-keygen -t rsa -b 4096` | Bred kompatibilitet |
| ECDSA | `ssh-keygen -t ecdsa` | Snabb, god sakerhet |

```bash
# Generera nyckel (lokal dator)
ssh-keygen -t ed25519 -C "user@example.com"

# Kopiera till server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Manuell installation pa server
mkdir -p ~/.ssh && chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys          # klistra in publik nyckel
chmod 600 ~/.ssh/authorized_keys
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 4: Inaktivera losenord

```
INNAN: Losenord + Nycklar           EFTER: Endast Nycklar
      ┌─────────────┐                    ┌─────────────┐
      │  Losenord   │ ──► X              │   Nyckel    │
      │    eller    │      STANG AV      │   ENDAST    │
      │   Nyckel    │                    └─────────────┘
      └─────────────┘
```

```bash
# I /etc/ssh/sshd_config:
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no

# VIKTIGT: Testa nyckel-login FORST!
# Ha backup-session oppen!
sudo sshd -t && sudo systemctl restart sshd
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 5: Begransa atkomst

| Direktiv | Exempel | Effekt |
|----------|---------|--------|
| `AllowUsers` | `AllowUsers alice bob` | Endast dessa anvandare |
| `AllowGroups` | `AllowGroups sshusers` | Endast gruppmedlemmar |
| `AllowUsers` | `AllowUsers alice@192.168.1.*` | Anvandare + IP-filter |
| `DenyUsers` | `DenyUsers guest` | Blocklista anvandare |

```bash
# I /etc/ssh/sshd_config:
AllowUsers alice bob deploy
# eller
AllowGroups sshusers admins
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Steg 6: Sakerhetsinställningar

| Installning | Varde | Beskrivning |
|-------------|-------|-------------|
| `MaxAuthTries` | 3 | Max inloggningsforsk |
| `LoginGraceTime` | 60 | Sekunder for login |
| `ClientAliveInterval` | 300 | Keepalive interval |
| `ClientAliveCountMax` | 2 | Max missade keepalives |
| `X11Forwarding` | no | Stang av X11 |
| `AllowTcpForwarding` | no | Stang av port forwarding |
| `Protocol` | 2 | Endast SSH v2 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fail2ban Installation

```
┌─────────────────────────────────────────────────────────────────┐
│                    FAIL2BAN FLODE                               │
│                                                                 │
│    /var/log/auth.log                                           │
│           │                                                     │
│           ▼                                                     │
│    ┌─────────────┐    3 fel inom    ┌─────────────┐            │
│    │  Fail2ban   │ ──────────────►  │   BANNED    │            │
│    │  overvakar  │    10 minuter    │   1 timme   │            │
│    └─────────────┘                  └─────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

```bash
# Installation
sudo apt install fail2ban            # Debian/Ubuntu
sudo dnf install fail2ban            # RHEL/Fedora

# Konfigurera
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```

Lagg till i jail.local:
```
[sshd]
enabled = true
port = ssh,2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
```

```bash
# Aktivera
sudo systemctl enable --now fail2ban

# Status
sudo fail2ban-client status sshd
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Komplett Hardened sshd_config

```bash
# /etc/ssh/sshd_config - Hardened

# Natverksinstallningar
Port 2222
Protocol 2

# Autentisering
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no

# Auktorisering
AllowGroups sshusers

# Granser
MaxAuthTries 3
MaxSessions 2
LoginGraceTime 60
ClientAliveInterval 300
ClientAliveCountMax 2

# Sakerhet
X11Forwarding no
AllowTcpForwarding no
AllowAgentForwarding no
PermitUserEnvironment no

# Loggning
LogLevel VERBOSE
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Verifiering

| Uppgift | Kommando |
|---------|----------|
| Visa lyssnande port | `sudo ss -tlnp \\| grep sshd` |
| Testa konfiguration | `sudo sshd -T` |
| Misslyckade forsok | `sudo grep "Failed password" /var/log/auth.log \\| tail -20` |
| Lyckade logins | `sudo grep "Accepted" /var/log/auth.log \\| tail -10` |
| Fail2ban status | `sudo fail2ban-client status sshd` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Nyckelbaserad auth | ed25519-nycklar + PasswordAuthentication no |
| Root-blockering | PermitRootLogin no, anvand sudo istallet |
| Atkomstbegransning | AllowUsers/AllowGroups for explicit kontroll |
| Fail2ban | Automatisk IP-blockering vid upprepade fel |
| Testning | sshd -t innan restart, backup-session oppen |

**Kom ihag:**
- Testa ALLTID nyckel-login innan du stangar av losenord
- Ha en backup-session oppen vid SSH-andringar
- Uppdatera brandvagg om du byter port
- fail2ban ar standard for produktionsservrar
- Loggar i /var/log/auth.log for felsokning
""",
        },
        {
            "title": 'Firewall Basics (ufw, iptables)',
            "slug": 'firewall-basics',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Firewall Basics (ufw, iptables)

En brandvagg ar vakten vid varje port pa din server och bestammer vilken trafik som far komma in och ga ut. Utan brandvagg ar alla portar oppna for vem som helst pa internet att forsoka ansluta till.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Brandvagg Oversikt

```
┌─────────────────────────────────────────────────────────────────┐
│                      INTERNET                                   │
│                          │                                      │
│                          ▼                                      │
│                    ┌───────────┐                                │
│                    │ BRANDVAGG │                                │
│                    └─────┬─────┘                                │
│                          │                                      │
│          ┌───────────────┼───────────────┐                      │
│          ▼               ▼               ▼                      │
│     Port 22         Port 80        Port 443     Port 3306       │
│      ALLOW           ALLOW          ALLOW         DENY          │
│       SSH            HTTP          HTTPS         MySQL          │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UFW vs iptables vs firewalld

| Verktyg | Distribution | Komplexitet | Anvandningsfall |
|---------|--------------|-------------|-----------------|
| UFW | Ubuntu/Debian | Enkel | De flesta servrar |
| iptables | Alla | Avancerad | Full kontroll |
| firewalld | RHEL/CentOS | Medel | Zoner och services |
| nftables | Moderna | Avancerad | Ersatter iptables |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UFW - Uncomplicated Firewall

| Kommando | Beskrivning |
|----------|-------------|
| `sudo ufw status` | Visa brandvaggsstatus |
| `sudo ufw status verbose` | Detaljerad status |
| `sudo ufw status numbered` | Regler med nummer |
| `sudo ufw enable` | Aktivera brandvagg |
| `sudo ufw disable` | Inaktivera brandvagg |
| `sudo ufw reset` | Aterstall allt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UFW Grundkonfiguration

```
VIKTIGT ORDNING:
                    1. allow ssh
                          │
                          ▼
                    2. default deny incoming
                          │
                          ▼
                    3. default allow outgoing
                          │
                          ▼
                    4. ufw enable
```

```bash
# FORST: Tillat SSH (lasa inte ut dig!)
sudo ufw allow ssh               # port 22
# eller
sudo ufw allow 2222/tcp          # annan SSH-port

# Satt defaults
sudo ufw default deny incoming   # neka all inkommande
sudo ufw default allow outgoing  # tillat all utgaende

# Aktivera
sudo ufw enable
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UFW Vanliga Regler

| Kommando | Beskrivning |
|----------|-------------|
| `sudo ufw allow http` | Port 80 |
| `sudo ufw allow https` | Port 443 |
| `sudo ufw allow 'Nginx Full'` | Port 80 + 443 |
| `sudo ufw allow 5432/tcp` | PostgreSQL |
| `sudo ufw allow 3306/tcp` | MySQL |
| `sudo ufw allow from 192.168.1.100` | Specifik IP |
| `sudo ufw allow from 192.168.1.0/24` | Hela subnet |
| `sudo ufw allow from 192.168.1.100 to any port 22` | IP + port |
| `sudo ufw allow 6000:6007/tcp` | Portintervall |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ta Bort UFW-regler

```bash
# Visa med nummer
sudo ufw status numbered
# Output: [1] 22/tcp ALLOW IN Anywhere
#         [2] 80/tcp ALLOW IN Anywhere

# Ta bort med nummer
sudo ufw delete 2                # tar bort regel 2

# Ta bort med regel-syntax
sudo ufw delete allow http
sudo ufw delete allow from 192.168.1.100

# Aterstall allt
sudo ufw reset
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## iptables Grunder

```
┌─────────────────────────────────────────────────────────────────┐
│                     IPTABLES CHAINS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INKOMMANDE ──► [INPUT]    ──► Lokal process                   │
│                                                                 │
│  Lokal process ──► [OUTPUT] ──► UTGAENDE                       │
│                                                                 │
│  INKOMMANDE ──► [FORWARD] ──► UTGAENDE (routing)               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Kommando | Beskrivning |
|----------|-------------|
| `sudo iptables -L` | Lista alla regler |
| `sudo iptables -L -n` | Numeriska portar |
| `sudo iptables -L -v` | Verbose med raknare |
| `sudo iptables -L -n -v --line-numbers` | Allt |
| `sudo iptables -F` | Flush (rensa) allt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## iptables Syntax

```
iptables -A CHAIN -p PROTOKOLL --dport PORT -j ACTION

Flaggor:
  -A    Append (lagg till i slutet)
  -I    Insert (lagg till i borjan)
  -D    Delete (ta bort)
  -p    Protokoll (tcp, udp, icmp)
  --dport  Destinationsport
  -j    Jump/Action (ACCEPT, DROP, REJECT)
  -s    Source IP
  -i    Input interface
```

```bash
# Tillat SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Tillat HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Tillat etablerade anslutningar (VIKTIGT!)
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Tillat loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Droppa allt annat (SIST!)
sudo iptables -A INPUT -j DROP
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## iptables Spara Regler

| Distribution | Kommando |
|--------------|----------|
| Debian/Ubuntu | `sudo apt install iptables-persistent` |
| | `sudo netfilter-persistent save` |
| | `sudo netfilter-persistent reload` |
| RHEL/CentOS | `sudo service iptables save` |
| | Sparas i /etc/sysconfig/iptables |

```bash
# Ta bort specifik regel
sudo iptables -L INPUT --line-numbers
sudo iptables -D INPUT 3             # ta bort regel 3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt Exempel: Webbserver

```bash
# UFW (enklast)
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
sudo ufw status verbose

# iptables (samma sak)
sudo iptables -F                                              # rensa
sudo iptables -A INPUT -i lo -j ACCEPT                        # localhost
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT            # SSH
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT            # HTTP
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT           # HTTPS
sudo iptables -A INPUT -j DROP                                # neka resten
sudo netfilter-persistent save                                # spara
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## firewalld (RHEL/CentOS)

| Kommando | Beskrivning |
|----------|-------------|
| `sudo firewall-cmd --state` | Visa status |
| `sudo firewall-cmd --list-all` | Lista regler |
| `sudo firewall-cmd --add-service=ssh --permanent` | Tillat SSH |
| `sudo firewall-cmd --add-service=http --permanent` | Tillat HTTP |
| `sudo firewall-cmd --add-port=8080/tcp --permanent` | Tillat port |
| `sudo firewall-cmd --reload` | Ladda om |
| `sudo firewall-cmd --remove-service=http --permanent` | Ta bort |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsokning

| Uppgift | Kommando |
|---------|----------|
| Testa port utifran | `nc -zv server.example.com 80` |
| Lyssnande portar | `sudo ss -tulnp` |
| UFW status | `sudo ufw status` |
| iptables regler | `sudo iptables -L -n -v` |
| Aktivera UFW-logg | `sudo ufw logging on` |
| Visa logg | `sudo tail -f /var/log/ufw.log` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Misstag

```
┌─────────────────────────────────────────────────────────────────┐
│                   MISSTAG ATT UNDVIKA                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Aktivera brandvagg INNAN SSH ar tillaten                   │
│     Losning: ufw allow ssh FORST                               │
│                                                                 │
│  2. Glommer ESTABLISHED,RELATED i iptables                     │
│     Losning: -m state --state ESTABLISHED,RELATED -j ACCEPT    │
│                                                                 │
│  3. Blockera loopback (localhost)                              │
│     Losning: -A INPUT -i lo -j ACCEPT                          │
│                                                                 │
│  4. Glommer spara iptables-regler                              │
│     Losning: netfilter-persistent save                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| UFW for enkelhet | "allow ssh" innan "enable", deny incoming default |
| iptables chains | INPUT (in), OUTPUT (ut), FORWARD (routing) |
| ESTABLISHED | Glom aldrig tillata etablerade anslutningar |
| Spara regler | iptables-regler forsvinner vid omstart utan save |
| Felsokning | ss -tulnp for lyssnande, nc -zv for test |

**Kom ihag:**
- ALLTID tillat SSH innan du aktiverar brandvaggen
- UFW ar wrapper runt iptables - samma sakerhet
- iptables-regler forsvinner vid reboot utan persistent
- Loopback (lo) maste vara tillaten for localhost
- firewalld pa RHEL/CentOS, UFW pa Ubuntu/Debian
""",
        },
    ],
}
