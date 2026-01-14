# The Linux Philosophy & Filesystem Deep-Dive

Fokus: Förståelse för att "allt är en fil" och hur lagring fungerar

## Core Concept: "Everything is a file"

I Linux är allt en fil - detta är en fundamental filosofi som gör systemet kraftfullt och konsekvent. Det betyder att inte bara vanliga filer, utan också:

- **Sockets**: Kommunikationskanaler mellan processer
- **Pipes**: Enkelriktad dataström mellan processer
- **Hardware**: Enheter representeras som filer i /dev

```bash
# Exempel: Allt är en fil
ls -l /dev/sda1          # Block device (hårddisk)
ls -l /proc/cpuinfo      # Systeminformation
ls -l /dev/tty           # Terminal
ls -l /dev/null          # "Svart hål" för data
```

## Filsystemshierarkin

Linux-filsystemet följer FHS (Filesystem Hierarchy Standard). Här är de viktigaste katalogerna:

### /bin och /sbin

- **/bin**: Grundläggande kommandon för alla användare (behövs för boot)
- **/sbin**: Systemkommandon för administratörer (behövs för boot)
- **/usr/bin**: Användarprogram (inte kritiska för boot)
- **/usr/sbin**: Systemprogram för administratörer (inte kritiska för boot)
- **/usr/local/bin**: Lokalt installerade program och scripts (inte från pakethanteraren)

**Skillnaden**: /bin och /sbin är kritiska för att systemet ska kunna starta. /usr/bin och /usr/sbin innehåller program som inte behövs för boot-processen.

```bash
ls /bin | head -5
# ls, cp, mv, rm, bash

ls /sbin | head -5
# fdisk, ifconfig, iptables, systemctl

# Var ska egna scripts placeras?
# /usr/local/bin - för systemvida scripts
# ~/bin eller ~/.local/bin - för användarspecifika scripts
```

### /etc - Configuration Files

Här ligger ALLA konfigurationsfiler:

```bash
/etc/ssh/sshd_config      # SSH server config
/etc/nginx/nginx.conf     # Nginx config
/etc/fstab                # Mount points
/etc/passwd               # Användare
/etc/shadow               # Lösenord (krypterade)
```

### /var/lib/docker

Docker lagrar all container-data här:

```bash
ls /var/lib/docker
# containers/  images/  volumes/  networks/
```

### /proc - Process Information

Virtual filesystem som visar system- och processinformation i realtid:

```bash
cat /proc/cpuinfo         # CPU-information
cat /proc/meminfo         # Minne
ls /proc/1234/            # Process med PID 1234

# Viktiga /proc-filer
cat /proc/version         # Kernel-version
cat /proc/loadavg         # Load average
cat /proc/uptime          # System uptime
cat /proc/mounts          # Monterade filsystem
cat /proc/devices         # Enheter

# Process-specifik information
cat /proc/1234/status      # Process status
cat /proc/1234/cmdline     # Kommandoraden
cat /proc/1234/environ     # Miljövariabler
ls /proc/1234/fd/         # Öppna filer (file descriptors)
```

**Viktigt**: /proc är inte ett riktigt filsystem - det är en virtuell representation av systemets tillstånd. Filerna skapas dynamiskt när du läser dem.

### /dev - Device Files

Alla enheter (hårddiskar, USB, etc.) representeras som filer:

```bash
ls -l /dev/sd*            # SATA/SCSI diskar
ls -l /dev/tty*           # Terminaler
ls -l /dev/null           # "Svart hål"
```

## Lagringsstacken: Från fysisk disk till monterat filsystem

Förståelse för hur data lagras är kritisk för DevOps:

```
Fysisk Disk → Partition → LUKS (kryptering) → Filesystem → Mount Point
```

### Partitionering (fdisk/parted)

```bash
# Visa partitioner
fdisk -l
# eller
lsblk

# Skapa partition med fdisk
sudo fdisk /dev/sda
# n = new partition
# p = primary
# w = write changes

# Modernare alternativ: parted
sudo parted /dev/sda print
```

### Kryptering med LUKS

Logiken bakom provfrågan: Block device → Partition → LUKS → Filesystem

```bash
# Skapa LUKS-volym
sudo cryptsetup luksFormat /dev/sda1

# Öppna krypterad volym
sudo cryptsetup luksOpen /dev/sda1 my_encrypted_volume

# Nu kan du skapa filsystem på /dev/mapper/my_encrypted_volume
sudo mkfs.ext4 /dev/mapper/my_encrypted_volume
```

**Ordningen är viktig**: Först partition, sedan LUKS, sedan filsystem!

### Montering via /etc/fstab

/etc/fstab definierar vad som ska monteras vid boot:

```bash
# Format: <device> <mountpoint> <filesystem> <options> <dump> <pass>
/dev/mapper/my_encrypted_volume  /mnt/data  ext4  defaults  0  2
```

```bash
# Testa fstab-konfiguration
sudo mount -a

# Montera manuellt
sudo mount /dev/sda1 /mnt/data
```

## Inodes & Länkar

### Vad en Inode faktiskt lagrar

En inode (index node) lagrar metadata om en fil:

- Filstorlek
- Ägare och grupp
- Behörigheter
- Tidsstämplar (created, modified, accessed)
- Länkar till datablock (var filens data faktiskt ligger)

```bash
# Visa inode-nummer
ls -i filename

# Visa inode-information
stat filename
```

### Skillnaden mellan ln och ln -s

**Hard Link (ln)**: Direkt pekare till samma inode. Om originalfilen raderas, finns länken kvar.

```bash
ln original.txt hardlink.txt
# Båda pekar på samma inode
# Om original.txt raderas, finns hardlink.txt kvar
```

**Symbolic Link (ln -s)**: Pekare till filnamnet. Om originalfilen raderas, blir länken trasig.

```bash
ln -s original.txt symlink.txt
# symlink.txt pekar på namnet "original.txt"
# Om original.txt raderas, blir symlink.txt trasig
```

```bash
# Visa länkar
ls -l
# Hard link: Normal fil
# Symbolic link: -> pekar på mål

# Räkna hard links
ls -l | grep " 2 "  # Filer med 2 hard links
```

## Grundläggande kommandon för filhantering

### touch - Skapa eller uppdatera tidsstämplar

```bash
# Skapa en tom fil
touch newfile.txt

# Uppdatera tidsstämplar på befintlig fil
touch existing.txt

# Skapa flera filer samtidigt
touch file1.txt file2.txt file3.txt
```

### cp - Kopiera filer och mappar

```bash
# Kopiera fil
cp source.txt dest.txt

# Kopiera rekursivt (mappar och allt innehåll)
cp -r folder1 folder2

# Kopiera med bevarade rättigheter
cp -p source.txt dest.txt

# Kopiera interaktivt (frågar innan överskrivning)
cp -i source.txt dest.txt
```

### cat, head, tail - Visa filinnehåll

```bash
# Visa hela filen
cat file.txt

# Visa första 10 raderna
head file.txt
head -n 20 file.txt  # Första 20 raderna

# Visa sista 10 raderna
tail file.txt
tail -n 20 file.txt  # Sista 20 raderna

# Följ fil i realtid (användbart för loggar)
tail -f /var/log/syslog
```

### Navigering med cd och ~

```bash
# Gå till hemkatalog
cd ~
# eller
cd

# ~ expanderas till användarens hemkatalog
echo ~
# /home/username

# Gå tillbaka till föregående katalog
cd -
```

## Systemunderhållskommandon

### history - Kommandohistorik

```bash
# Visa kommandohistorik
history

# Visa sista 20 kommandona
history 20

# Sök i historiken
history | grep "docker"

# Kör ett kommando från historiken
!123  # Kör kommandot på rad 123
!!    # Kör senaste kommandot
!docker  # Kör senaste kommandot som börjar med "docker"
```

### uptime - Systemuptime och belastning

```bash
# Visa uptime och load average
uptime
# 14:30:00 up 10 days,  2:15,  3 users,  load average: 1.25, 0.85, 0.60

# Mer läsbart format
uptime -p
# up 10 days, 2 hours, 15 minutes
```

### uname - Systeminformation

```bash
# Visa all systeminformation
uname -a
# Linux hostname 5.4.0-74-generic #83-Ubuntu x86_64 GNU/Linux

# Visa bara kernel-version
uname -r
# 5.4.0-74-generic

# Visa operativsystem
uname -o
# GNU/Linux
```

### alias - Skapa genvägar

```bash
# Skapa alias
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# Använd alias
ll  # Körs som ls -la

# Visa alla alias
alias

# Ta bort alias
unalias ll
```

### whereis - Hitta programfiler

```bash
# Hitta binär, källkod och manualsidor
whereis python
# python: /usr/bin/python3.8 /usr/lib/python3.8 /etc/python3.8

# Hitta bara binärer
whereis -b python

# Hitta bara manualsidor
whereis -m python
```

### locate - Snabb filsökning

```bash
# Sök efter fil (använder databas, mycket snabbare än find)
locate filename.txt

# Uppdatera locate-databasen (körs ofta automatiskt)
sudo updatedb

# Case-insensitive sökning
locate -i filename
```

### find - Avancerad filsökning

```bash
# Sök efter filer med namn
find /home -name "*.txt"

# Sök efter filer större än 100MB
find / -size +100M 2>/dev/null

# Sök efter filer ändrade senaste 7 dagarna
find /var/log -mtime -7

# Sök och kör kommando på resultat
find /tmp -name "*.log" -delete
```

## Logghantering

### /var/log - Systemloggar

```bash
# Viktiga loggkataloger
ls /var/log
# syslog      - Systemloggar
# auth.log    - Autentiseringsloggar
# kern.log    - Kernel-loggar
# nginx/      - Nginx-loggar
# apache2/    - Apache-loggar
```

### tail -f - Följ loggar i realtid

```bash
# Följ systemloggen
tail -f /var/log/syslog

# Följ flera filer samtidigt
tail -f /var/log/syslog /var/log/auth.log

# Visa sista 50 raderna och följ sedan
tail -n 50 -f /var/log/syslog
```

### grep - Sök i loggar

```bash
# Sök efter "error" i logg
grep "error" /var/log/syslog

# Invertera sökning (visa rader UTAN "error")
grep -v "error" /var/log/syslog

# Case-insensitive
grep -i "ERROR" /var/log/syslog

# Visa radnummer
grep -n "error" /var/log/syslog

# Räkna antal träffar
grep -c "error" /var/log/syslog
```

### dmesg - Kernel ring buffer

```bash
# Visa kernel-meddelanden
dmesg

# Visa senaste meddelanden
dmesg | tail -20

# Sök efter specifikt
dmesg | grep "error"

# Tidsstämplar
dmesg -T  # Visa med läsbara tidsstämplar
```

### journalctl - systemd loggar

```bash
# Visa alla systemd-loggar
journalctl

# Visa loggar för specifik tjänst
journalctl -u nginx

# Följ loggar i realtid
journalctl -f

# Visa senaste 100 raderna
journalctl -n 100

# Visa kernel-loggar
journalctl -k
```

## Praktiska exempel

```bash
# Se hela lagringsstacken
lsblk -f
# Visar: disk → partition → filesystem → mount point

# Kontrollera inode-användning
df -i
# Visar hur många inodes som används

# Hitta filer med många hard links
find / -links +5 2>/dev/null

# Kombinera kommandon för logganalys
tail -f /var/log/syslog | grep -i error

# Packa upp .tar.gz-fil
tar -xzf archive.tar.gz

# Packa filer till .tar.gz
tar -czf archive.tar.gz folder/
```

## LVM (Logical Volume Manager)

LVM är ett flexibelt system för att hantera lagring i Linux. Istället för att arbeta direkt med partitioner, bygger LVM ett abstraktionslager som gör det enklare att ändra storlek, flytta och hantera volymer.

### LVM-hierarkin

```
Physical Disk → Physical Volume (PV) → Volume Group (VG) → Logical Volume (LV) → Filesystem
```

**Förklaring**:
- **Physical Volume (PV)**: En fysisk disk eller partition
- **Volume Group (VG)**: En pool av Physical Volumes
- **Logical Volume (LV)**: Virtuella partitioner som kan skapas från Volume Group

### Varför använda LVM?

```bash
# Fördelar:
# - Ändra storlek på volymer utan att starta om
# - Flytta data mellan diskar i drift
# - Skapa snapshots för backup
# - Kombinera flera diskar till en stor volym
```

### Skapa LVM-struktur

```bash
# Steg 1: Skapa Physical Volume
sudo pvcreate /dev/sdb1
# Konverterar en partition till en PV

# Steg 2: Skapa Volume Group
sudo vgcreate vg_data /dev/sdb1
# Skapar en VG kallad "vg_data" från PV

# Steg 3: Skapa Logical Volume
sudo lvcreate -L 10G -n lv_data vg_data
# Skapar en 10GB LV kallad "lv_data" från VG "vg_data"

# Steg 4: Skapa filsystem
sudo mkfs.ext4 /dev/vg_data/lv_data

# Steg 5: Montera
sudo mkdir -p /mnt/data
sudo mount /dev/vg_data/lv_data /mnt/data
```

### LVM-kommandon

```bash
# Visa Physical Volumes
pvdisplay
pvs  # Kort format

# Visa Volume Groups
vgdisplay
vgs  # Kort format

# Visa Logical Volumes
lvdisplay
lvs  # Kort format

# Visa allt
sudo lsblk
# Visar hela strukturen: disk → partition → LVM → mountpoint
```

### Ändra storlek på LVM

**Utöka Logical Volume**:

```bash
# Kontrollera tillgängligt utrymme i VG
sudo vgs
# Free PE visar ledigt utrymme

# Utöka LV med 5GB
sudo lvextend -L +5G /dev/vg_data/lv_data
# Eller använd allt ledigt utrymme
sudo lvextend -l +100%FREE /dev/vg_data/lv_data

# Utöka filsystemet (ext4)
sudo resize2fs /dev/vg_data/lv_data

# För XFS
sudo xfs_growfs /mnt/data
```

**Minska Logical Volume** (farligt - kan förlora data!):

```bash
# Avmontera först
sudo umount /mnt/data

# Kontrollera filsystem
sudo e2fsck -f /dev/vg_data/lv_data

# Minska filsystem
sudo resize2fs /dev/vg_data/lv_data 8G

# Minska LV
sudo lvreduce -L 8G /dev/vg_data/lv_data

# Montera igen
sudo mount /dev/vg_data/lv_data /mnt/data
```

**Viktigt**: Minska alltid filsystemet FÖRE du minskar LV, annars riskerar du dataförlust!

### LVM Snapshots

Snapshots låter dig skapa point-in-time kopior för backup.

```bash
# Skapa snapshot (10% av original-storlek)
sudo lvcreate -L 1G -s -n lv_data_snapshot /dev/vg_data/lv_data

# Montera snapshot
sudo mkdir -p /mnt/snapshot
sudo mount /dev/vg_data/lv_data_snapshot /mnt/snapshot

# Backup från snapshot
sudo tar czf /backup/data-backup.tar.gz /mnt/snapshot

# Ta bort snapshot efter backup
sudo umount /mnt/snapshot
sudo lvremove /dev/vg_data/lv_data_snapshot
```

### Lägga till disk till VG

```bash
# Skapa PV från ny disk
sudo pvcreate /dev/sdc1

# Lägg till i befintlig VG
sudo vgextend vg_data /dev/sdc1

# Nu kan du utöka LV med det nya utrymmet
sudo lvextend -L +50G /dev/vg_data/lv_data
sudo resize2fs /dev/vg_data/lv_data
```

### Permanent montering i /etc/fstab

```bash
# Använd LVM-path i fstab
/dev/vg_data/lv_data  /mnt/data  ext4  defaults  0  2

# Eller använd UUID (rekommenderat)
# Hitta UUID
sudo blkid /dev/vg_data/lv_data
# UUID=abc-123-def-456

# I /etc/fstab
UUID=abc-123-def-456  /mnt/data  ext4  defaults  0  2
```

### Troubleshooting LVM

```bash
# Om VG inte syns efter reboot
sudo vgscan
sudo vgchange -ay

# Reparera metadata
sudo vgck vg_data

# Ta bort LV (VARNING: data förloras)
sudo umount /mnt/data
sudo lvremove /dev/vg_data/lv_data

# Ta bort VG
sudo vgremove vg_data

# Ta bort PV
sudo pvremove /dev/sdb1
```

## Package Management

Linux-system använder pakethanterare för att installera, uppdatera och ta bort programvara.

### apt (Debian/Ubuntu)

apt är det moderna kommandot för pakethantering i Debian-baserade system.

```bash
# Uppdatera paketlistan
sudo apt update
# Hämtar info om nya versioner från repositories

# Uppgradera alla paket
sudo apt upgrade
# Installerar nya versioner av installerade paket

# Full uppgradering (hanterar dependencies)
sudo apt full-upgrade
sudo apt dist-upgrade  # Äldre namn

# Installera paket
sudo apt install nginx
sudo apt install nginx mysql-server php

# Ta bort paket (behåll config)
sudo apt remove nginx

# Ta bort paket (inkl config)
sudo apt purge nginx

# Ta bort oanvända dependencies
sudo apt autoremove
```

### apt-cache - Sök och visa paketinformation

```bash
# Sök efter paket
apt-cache search nginx
apt-cache search "web server"

# Visa paketinformation
apt-cache show nginx

# Lista alla tillgängliga versioner
apt-cache policy nginx

# Visa dependencies
apt-cache depends nginx

# Visa reverse dependencies (vad som beror på paketet)
apt-cache rdepends nginx
```

### dpkg - Low-level pakethantering

dpkg är det underliggande verktyget som apt använder.

```bash
# Lista installerade paket
dpkg -l
dpkg -l | grep nginx

# Visa om paket är installerat
dpkg -l nginx
dpkg -s nginx  # Mer detaljerad info

# Lista filer i paket
dpkg -L nginx

# Hitta vilket paket en fil tillhör
dpkg -S /usr/sbin/nginx

# Installera .deb-fil
sudo dpkg -i package.deb

# Ta bort paket
sudo dpkg -r nginx
sudo dpkg -P nginx  # Purge (inkl config)
```

### Repository Management

Repositories är servrar som innehåller paket.

```bash
# Repositories definieras i:
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Lägg till repository
sudo add-apt-repository ppa:nginx/stable
sudo apt update

# Ta bort repository
sudo add-apt-repository --remove ppa:nginx/stable

# Manuellt lägg till i sources.list
sudo nano /etc/apt/sources.list
# deb http://archive.ubuntu.com/ubuntu/ focal main restricted
```

### Låsa paket-version

Förhindra att ett paket uppgraderas.

```bash
# Låsa version
sudo apt-mark hold nginx

# Visa låsta paket
apt-mark showhold

# Låsa upp
sudo apt-mark unhold nginx
```

### Rensa cache

```bash
# Ta bort nedladdade .deb-filer
sudo apt clean

# Ta bort gamla versioner (behåll senaste)
sudo apt autoclean
```

## Cron Jobs - Schemaläggning

Cron används för att köra kommandon automatiskt vid specifika tider.

### Crontab-syntax

```bash
# Format: Min  Hour  Day  Month  Weekday  Command
#         0-59 0-23  1-31 1-12   0-7      /path/to/command

# Exempel
0 2 * * * /path/to/backup.sh
# Kör backup.sh kl 02:00 varje dag

*/15 * * * * /path/to/check.sh
# Kör check.sh var 15:e minut

0 */2 * * * /path/to/task.sh
# Kör task.sh varannan timme

0 0 * * 0 /path/to/weekly.sh
# Kör weekly.sh kl 00:00 på söndagar (0 eller 7 = söndag)

0 9 1 * * /path/to/monthly.sh
# Kör monthly.sh kl 09:00 den första varje månad
```

### Hantera crontab

```bash
# Öppna din crontab för redigering
crontab -e

# Visa din crontab
crontab -l

# Ta bort din crontab
crontab -r

# Redigera annan användares crontab (root)
sudo crontab -u username -e
```

### System-wide cron

```bash
# System crontabs
/etc/crontab          # System-wide crontab
/etc/cron.d/          # Katalog för cron-filer
/etc/cron.daily/      # Körs dagligen
/etc/cron.weekly/     # Körs veckovis
/etc/cron.monthly/    # Körs månadsvis

# Lägg skript i dessa kataloger
sudo cp backup.sh /etc/cron.daily/
sudo chmod +x /etc/cron.daily/backup.sh
```

### Cron-miljövariabler

```bash
# I crontab, sätt miljövariabler
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=admin@example.com

# Ditt cron job
0 2 * * * /path/to/backup.sh
```

### Logga cron-jobb

```bash
# Cron logs finns i
grep CRON /var/log/syslog

# Omdirigera output till fil i crontab
0 2 * * * /path/to/backup.sh >> /var/log/backup.log 2>&1

# Skicka output till email (om MAILTO är satt)
0 2 * * * /path/to/backup.sh
```

### Speciala cron-scheman

```bash
# @reboot - Kör vid systemstart
@reboot /path/to/startup.sh

# @daily - Kör en gång per dag (00:00)
@daily /path/to/daily.sh

# @weekly - Kör en gång per vecka (söndag 00:00)
@weekly /path/to/weekly.sh

# @monthly - Kör en gång per månad (första dagen 00:00)
@monthly /path/to/monthly.sh

# @yearly eller @annually - Kör en gång per år
@yearly /path/to/yearly.sh
```

### Troubleshooting cron

```bash
# Kontrollera att crond körs
sudo systemctl status cron

# Starta/stoppa cron
sudo systemctl start cron
sudo systemctl stop cron

# Testa cron-jobb manuellt
/path/to/script.sh

# Vanliga problem:
# - PATH-miljövariabel är inte densamma som i shell
# - Använd absoluta paths i crontab
# - Kontrollera execute-rättigheter (chmod +x)
# - Kontrollera logs för fel
```

## Viktiga takeaways

- **Allt är en fil**: Sockets, pipes, hardware - allt kan hanteras som filer
- **Lagringsstacken**: Disk → Partition → LUKS → Filesystem → Mount
- **LVM-hierarki**: Physical Volume → Volume Group → Logical Volume
- **LVM fördelar**: Flexibel storlek, snapshots, kombinera diskar
- **Inodes lagrar metadata**, inte själva filinnehållet
- **Hard links** pekar på inode, **symbolic links** pekar på filnamn
- **/bin och /sbin** är kritiska för boot, /usr/bin och /usr/sbin är inte
- **/usr/local/bin** är rätt plats för egna scripts som inte kommer från pakethanteraren
- **/proc** är ett virtuellt filsystem som visar systemtillstånd i realtid
- **Loggar** finns i /var/log - använd `tail -f` för realtidsövervakning
- **apt update** hämtar paketlistor, **apt upgrade** installerar uppdateringar
- **dpkg** är low-level, **apt** är high-level pakethantering
- **Crontab-format**: Min Hour Day Month Weekday Command
- **crontab -e** för att redigera, **crontab -l** för att lista
- **history, uptime, uname** är viktiga verktyg för systemunderhåll
- **find** är kraftfullt men långsamt, **locate** är snabbt men kräver uppdaterad databas
