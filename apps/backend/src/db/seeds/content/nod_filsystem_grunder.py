"""
NOD: Linuxfilosofin och djupdykning i filsystem
===============================================
Grundläggande förståelse för Linuxfilosofin "allt är en fil" och hur datalagring fungerar i praktiken
"""

FILSYSTEM_GRUNDER_NODE = {
    "title": "Linuxfilosofin och djupdykning i filsystem",
    "slug": "filsystem-grunder",
    "description": "Grundläggande förståelse för Linuxfilosofin 'allt är en fil' och hur datalagring fungerar i praktiken",
    "difficulty": "easy",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "order_index": 1,
    "content": r"""# Linuxfilosofin och djupdykning i filsystem

Fokus: Grundprinciper om att "allt är en fil" och lagringsmekanism

## Grundkonceptet: "Allt är en fil"

En av de mest fundamentala principerna i Linux är att allt behandlas som en fil - detta är en kärnfilosofi som gör systemet både kraftfullt och genomtänkt. Detta koncept innebär att inte enbart traditionella filer, utan även:

- **Sockets**: Kommunikationskanaler för dataöverföring mellan processer
- **Pipes**: Unidirektionella dataströmmar mellan processer
- **Hardware**: Hårdvaruenheter representeras genom filer i /dev

```bash
# Allt behandlas som en fil
ls -l /dev/sda1          # Blockenheter (diskar)
ls -l /proc/cpuinfo      # Systemresursinformation
ls -l /dev/tty           # Terminalenhet
ls -l /dev/null          # Datadump ("svart hål")
```

## Filsystemets hierarkiska struktur

Linux-filsystemet följer FHS (Filesystem Hierarchy Standard). De viktigaste katalogerna omfattar:

### /bin och /sbin

- **/bin**: Essentiella användarkommandon (nödvändiga för systemstart)
- **/sbin**: Systemadministrationskommandon (nödvändiga för systemstart)
- **/usr/bin**: Användarapplikationer (ej kritiska för uppstart)
- **/usr/sbin**: Systemapplikationer för administratörer (ej kritiska för uppstart)
- **/usr/local/bin**: Manuellt installerade program och skript (utanför pakethanterare)

**Avgörande skillnad**: /bin och /sbin är absolut nödvändiga för att systemet ska kunna starta. /usr/bin och /usr/sbin innehåller applikationer som inte krävs under boot-processen.

```bash
ls /bin | head -5
# ls, cp, mv, rm, bash

ls /sbin | head -5
# fdisk, ifconfig, iptables, systemctl

# Var placerar man egna skript?
# /usr/local/bin - för systemgemensamma skript
# ~/bin eller ~/.local/bin - för användarspecifika skript
```

### /etc - Konfigurationsfiler

All systemkonfiguration finns här:

```bash
/etc/ssh/sshd_config      # SSH-serverkonfiguration
/etc/nginx/nginx.conf     # Nginx-konfiguration
/etc/fstab                # Monteringspunkter
/etc/passwd               # Användarinformation
/etc/shadow               # Krypterade lösenord
```

### /var/lib/docker

Docker-datalagring sker här:

```bash
ls /var/lib/docker
# containers/  images/  volumes/  networks/
```

### /proc - Processinformation

Virtuellt filsystem som exponerar system- och processinformation i realtid:

```bash
cat /proc/cpuinfo         # Processorinformation
cat /proc/meminfo         # Minnesinformation
ls /proc/1234/            # Data om processen med PID 1234

# Centrala /proc-filer
cat /proc/version         # Kärnversion
cat /proc/loadavg         # Systembelastning
cat /proc/uptime          # Systemens drifttid
cat /proc/mounts          # Monterade filsystem
cat /proc/devices         # Registrerade enheter

# Process-relaterad information
cat /proc/1234/status      # Processstatus
cat /proc/1234/cmdline     # Kommandorad
cat /proc/1234/environ     # Miljövariabler
ls /proc/1234/fd/         # Öppna filer (filbeskrivare)
```

**Notera**: /proc är inte ett fysiskt filsystem - det är en virtuell framställning av systemets aktuella tillstånd. Filinnehållet genereras dynamiskt vid avläsning.

### /dev - Enhetsfiler

Alla hårdvaruenheter (diskar, USB, etc.) exponeras genom filer:

```bash
ls -l /dev/sd*            # SATA/SCSI-diskar
ls -l /dev/tty*           # Terminaler
ls -l /dev/null           # Datadump
```

## Lagringsstacken: Från fysisk disk till monterad filsystem

Förståelse för datalagring är avgörande för DevOps:

```
Fysisk Disk → Partition → LUKS (kryptering) → Filsystem → Monteringspunkt
```

### Partitionering (fdisk/parted)

```bash
# Visa befintliga partitioner
fdisk -l
# alternativt
lsblk

# Skapa ny partition med fdisk
sudo fdisk /dev/sda
# n = skapa ny partition
# p = primärpartition
# w = skriv ändringar

# Modernare alternativ: parted
sudo parted /dev/sda print
```

### Kryptering med LUKS

Logiken bakom provfrågan: Block device → Partition → LUKS → Filsystem

```bash
# Initialisera LUKS-volym
sudo cryptsetup luksFormat /dev/sda1

# Öppna krypterad volym
sudo cryptsetup luksOpen /dev/sda1 my_encrypted_volume

# Nu är det möjligt att skapa filsystem på /dev/mapper/my_encrypted_volume
sudo mkfs.ext4 /dev/mapper/my_encrypted_volume
```

**Ordningsföljden är kritisk**: Först partition, sedan LUKS, därefter filsystem!

### Montering via /etc/fstab

/etc/fstab specificerar vad som ska monteras vid systemstart:

```bash
# Format: <enhet> <monteringspunkt> <filsystem> <alternativ> <dump> <pass>
/dev/mapper/my_encrypted_volume  /mnt/data  ext4  defaults  0  2
```

```bash
# Testa fstab-konfiguration
sudo mount -a

# Montera manuellt
sudo mount /dev/sda1 /mnt/data
```

## Inodes och länkar

### Vad en Inode lagrar

En inode (indexnod) innehåller filmetadata:

- Filstorlek
- Ägare och gruppinformation
- Åtkomsträttigheter
- Tidsstämplar (skapad, modifierad, läst)
- Pekare till datablcok (var filens faktiska data finns)

```bash
# Visa inode-nummer
ls -i filename

# Visa detaljerad inode-information
stat filename
```

### Skillnaden mellan ln och ln -s

**Hard Link (ln)**: Direkt referens till samma inode. Om originalfilen tas bort förblir länken giltig.

```bash
ln original.txt hardlink.txt
# Båda refererar till samma inode
# Om original.txt raderas finns hardlink.txt kvar
```

**Symbolic Link (ln -s)**: Referens till filnamnet. Om originalfilen tas bort blir länken bruten.

```bash
ln -s original.txt symlink.txt
# symlink.txt refererar till namnet "original.txt"
# Om original.txt raderas blir symlink.txt bruten
```

```bash
# Visa länkar
ls -l
# Hard link: Vanlig fil
# Symbolic link: -> visar målet

# Räkna hard links
ls -l | grep " 2 "  # Filer med 2 hard links
```

## Grundläggande filhanteringskommandon

### touch - Skapa filer eller uppdatera tidsstämplar

```bash
# Skapa tom fil
touch newfile.txt

# Uppdatera tidsstämplar på existerande fil
touch existing.txt

# Skapa flera filer på en gång
touch file1.txt file2.txt file3.txt
```

### cp - Kopiera filer och kataloger

```bash
# Kopiera fil
cp source.txt dest.txt

# Kopiera rekursivt (kataloger med innehåll)
cp -r folder1 folder2

# Kopiera med bevarad metadata
cp -p source.txt dest.txt

# Kopiera interaktivt (bekräfta överskrivning)
cp -i source.txt dest.txt
```

### cat, head, tail - Visa filinnehåll

```bash
# Visa komplett fil
cat file.txt

# Visa inledande 10 rader
head file.txt
head -n 20 file.txt  # Första 20 rader

# Visa avslutande 10 rader
tail file.txt
tail -n 20 file.txt  # Sista 20 rader

# Följ fil i realtid (praktiskt för loggfiler)
tail -f /var/log/syslog
```

### Navigering med cd och ~

```bash
# Gå till hemkatalog
cd ~
# alternativt
cd

# ~ expanderas till användarens hemkatalog
echo ~
# /home/username

# Återgå till föregående katalog
cd -
```

## Systemunderhållskommandon

### history - Kommandohistorik

```bash
# Visa kommandohistorik
history

# Visa senaste 20 kommandona
history 20

# Sök i historiken
history | grep "docker"

# Kör kommando från historiken
!123  # Exekvera kommandot på rad 123
!!    # Exekvera senaste kommandot
!docker  # Exekvera senaste kommandot som börjar med "docker"
```

### uptime - Systemdrifttid och belastning

```bash
# Visa drifttid och belastningsgenomsnitt
uptime
# 14:30:00 up 10 days,  2:15,  3 users,  load average: 1.25, 0.85, 0.60

# Mer läsbart format
uptime -p
# up 10 days, 2 hours, 15 minutes
```

### uname - Systeminformation

```bash
# Visa komplett systeminformation
uname -a
# Linux hostname 5.4.0-74-generic #83-Ubuntu x86_64 GNU/Linux

# Visa enbart kärnversion
uname -r
# 5.4.0-74-generic

# Visa operativsystem
uname -o
# GNU/Linux
```

### alias - Skapa kommandogenvägar

```bash
# Definiera alias
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# Använd alias
ll  # Exekveras som ls -la

# Visa alla definierade alias
alias

# Radera alias
unalias ll
```

### whereis - Hitta programfiler

```bash
# Lokalisera binär, källkod och manual
whereis python
# python: /usr/bin/python3.8 /usr/lib/python3.8 /etc/python3.8

# Hitta enbart binärer
whereis -b python

# Hitta enbart manualsidor
whereis -m python
```

### locate - Snabb filsökning

```bash
# Sök efter fil (använder databas, mycket snabbare än find)
locate filename.txt

# Uppdatera locate-databasen (körs automatiskt periodiskt)
sudo updatedb

# Okänslig för stora/små bokstäver
locate -i filename
```

### find - Avancerad filsökning

```bash
# Sök efter filer med namn
find /home -name "*.txt"

# Sök efter filer större än 100MB
find / -size +100M 2>/dev/null

# Sök efter filer modifierade senaste 7 dagarna
find /var/log -mtime -7

# Sök och utför kommando på resultat
find /tmp -name "*.log" -delete
```

## Logghantering

### /var/log - Systemloggar

```bash
# Viktiga loggkataloger
ls /var/log
# syslog      - Systemhändelser
# auth.log    - Autentiseringar
# kern.log    - Kärnloggar
# nginx/      - Nginx-loggar
# apache2/    - Apache-loggar
```

### tail -f - Följ loggar i realtid

```bash
# Följ systemloggen
tail -f /var/log/syslog

# Följ flera filer samtidigt
tail -f /var/log/syslog /var/log/auth.log

# Visa sista 50 rader och följ därefter
tail -n 50 -f /var/log/syslog
```

### grep - Sök i loggar

```bash
# Sök efter "error" i loggfil
grep "error" /var/log/syslog

# Invertera sökning (visa rader UTAN "error")
grep -v "error" /var/log/syslog

# Okänslig för stora/små bokstäver
grep -i "ERROR" /var/log/syslog

# Visa radnummer
grep -n "error" /var/log/syslog

# Räkna matchande rader
grep -c "error" /var/log/syslog
```

### dmesg - Kärnans ringbuffer

```bash
# Visa kärnmeddelanden
dmesg

# Visa senaste meddelanden
dmesg | tail -20

# Sök efter specifikt
dmesg | grep "error"

# Läsbara tidsstämplar
dmesg -T
```

### journalctl - systemd-loggar

```bash
# Visa alla systemd-loggar
journalctl

# Visa loggar för specifik tjänst
journalctl -u nginx

# Följ loggar i realtid
journalctl -f

# Visa senaste 100 raderna
journalctl -n 100

# Visa kärnloggar
journalctl -k
```

## LVM (Logical Volume Manager)

LVM är ett flexibelt lagringssystem i Linux. Istället för att arbeta direkt med partitioner skapar LVM ett abstraktionslager som förenklar storleksändring, flyttning och hantering av volymer.

### LVM-hierarkin

```
Fysisk Disk → Physical Volume (PV) → Volume Group (VG) → Logical Volume (LV) → Filsystem
```

**Förklaring**:
- **Physical Volume (PV)**: En fysisk disk eller partition
- **Volume Group (VG)**: En samling av Physical Volumes
- **Logical Volume (LV)**: Virtuella partitioner skapade från Volume Group

### Fördelar med LVM

```bash
# Fördelar:
# - Ändra volymstorlek utan omstart
# - Flytta data mellan diskar under drift
# - Skapa snapshots för säkerhetskopiering
# - Kombinera flera diskar till en stor volym
```

### Skapa LVM-struktur

```bash
# Steg 1: Initiera Physical Volume
sudo pvcreate /dev/sdb1
# Konverterar partition till PV

# Steg 2: Initiera Volume Group
sudo vgcreate vg_data /dev/sdb1
# Skapar VG benämnd "vg_data" från PV

# Steg 3: Initiera Logical Volume
sudo lvcreate -L 10G -n lv_data vg_data
# Skapar 10GB LV benämnd "lv_data" från VG "vg_data"

# Steg 4: Initiera filsystem
sudo mkfs.ext4 /dev/vg_data/lv_data

# Steg 5: Montera
sudo mkdir -p /mnt/data
sudo mount /dev/vg_data/lv_data /mnt/data
```

### LVM-kommandon

```bash
# Visa Physical Volumes
pvdisplay
pvs  # Kompakt format

# Visa Volume Groups
vgdisplay
vgs  # Kompakt format

# Visa Logical Volumes
lvdisplay
lvs  # Kompakt format

# Visa komplett översikt
sudo lsblk
# Visar hela strukturen: disk → partition → LVM → monteringspunkt
```

### Ändra storlek på LVM

**Utöka Logical Volume**:

```bash
# Kontrollera ledigt utrymme i VG
sudo vgs
# Free PE visar tillgängligt utrymme

# Utöka LV med 5GB
sudo lvextend -L +5G /dev/vg_data/lv_data
# Eller använd allt ledigt utrymme
sudo lvextend -l +100%FREE /dev/vg_data/lv_data

# Utöka filsystemet (ext4)
sudo resize2fs /dev/vg_data/lv_data

# För XFS
sudo xfs_growfs /mnt/data
```

**Minska Logical Volume** (riskabelt - dataförlust möjlig!):

```bash
# Avmontera först
sudo umount /mnt/data

# Kontrollera filsystem
sudo e2fsck -f /dev/vg_data/lv_data

# Minska filsystem
sudo resize2fs /dev/vg_data/lv_data 8G

# Minska LV
sudo lvreduce -L 8G /dev/vg_data/lv_data

# Återmontera
sudo mount /dev/vg_data/lv_data /mnt/data
```

**Kritiskt**: Minska alltid filsystemet INNAN du minskar LV, annars riskerar du dataförlust!

### LVM Snapshots

Snapshots skapar tidpunktskopior för säkerhetskopiering.

```bash
# Skapa snapshot (10% av originalstorlek)
sudo lvcreate -L 1G -s -n lv_data_snapshot /dev/vg_data/lv_data

# Montera snapshot
sudo mkdir -p /mnt/snapshot
sudo mount /dev/vg_data/lv_data_snapshot /mnt/snapshot

# Säkerhetskopiera från snapshot
sudo tar czf /backup/data-backup.tar.gz /mnt/snapshot

# Radera snapshot efter säkerhetskopiering
sudo umount /mnt/snapshot
sudo lvremove /dev/vg_data/lv_data_snapshot
```

### Lägga till disk till VG

```bash
# Initiera PV från ny disk
sudo pvcreate /dev/sdc1

# Lägg till i existerande VG
sudo vgextend vg_data /dev/sdc1

# Nu kan du utöka LV med det nya utrymmet
sudo lvextend -L +50G /dev/vg_data/lv_data
sudo resize2fs /dev/vg_data/lv_data
```

### Permanent montering i /etc/fstab

```bash
# Använd LVM-sökväg i fstab
/dev/vg_data/lv_data  /mnt/data  ext4  defaults  0  2

# Eller använd UUID (rekommenderas)
# Hitta UUID
sudo blkid /dev/vg_data/lv_data
# UUID=abc-123-def-456

# I /etc/fstab
UUID=abc-123-def-456  /mnt/data  ext4  defaults  0  2
```

### Felsökning av LVM

```bash
# Om VG inte visas efter omstart
sudo vgscan
sudo vgchange -ay

# Reparera metadata
sudo vgck vg_data

# Radera LV (VARNING: data raderas)
sudo umount /mnt/data
sudo lvremove /dev/vg_data/lv_data

# Radera VG
sudo vgremove vg_data

# Radera PV
sudo pvremove /dev/sdb1
```

## Pakethantering

Linux-system använder pakethanterare för att installera, uppdatera och avlägsna programvara.

### apt (Debian/Ubuntu)

apt är det moderna verktyget för pakethantering i Debian-baserade system.

```bash
# Uppdatera paketinformation
sudo apt update
# Hämtar information om nya versioner från repositories

# Uppgradera installerade paket
sudo apt upgrade
# Installerar nya versioner av befintliga paket

# Fullständig uppgradering (hanterar beroenden)
sudo apt full-upgrade
sudo apt dist-upgrade  # Tidigare namn

# Installera paket
sudo apt install nginx
sudo apt install nginx mysql-server php

# Avlägsna paket (behåll konfiguration)
sudo apt remove nginx

# Avlägsna paket (inkludera konfiguration)
sudo apt purge nginx

# Avlägsna oanvända beroenden
sudo apt autoremove
```

### apt-cache - Sök och visa paketinformation

```bash
# Sök efter paket
apt-cache search nginx
apt-cache search "web server"

# Visa paketinformation
apt-cache show nginx

# Lista tillgängliga versioner
apt-cache policy nginx

# Visa paketberoenden
apt-cache depends nginx

# Visa omvända beroenden (vad som beror på paketet)
apt-cache rdepends nginx
```

### dpkg - Lågnivåpakethantering

dpkg är det underliggande verktyget som apt använder.

```bash
# Lista installerade paket
dpkg -l
dpkg -l | grep nginx

# Kontrollera om paket är installerat
dpkg -l nginx
dpkg -s nginx  # Mer detaljerad information

# Lista filer i paket
dpkg -L nginx

# Identifiera vilket paket en fil tillhör
dpkg -S /usr/sbin/nginx

# Installera .deb-fil
sudo dpkg -i package.deb

# Avlägsna paket
sudo dpkg -r nginx
sudo dpkg -P nginx  # Purge (inkludera konfiguration)
```

### Repository-hantering

Repositories är servrar som tillhandahåller paket.

```bash
# Repositories definieras i:
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Lägg till repository
sudo add-apt-repository ppa:nginx/stable
sudo apt update

# Avlägsna repository
sudo add-apt-repository --remove ppa:nginx/stable

# Manuellt lägg till i sources.list
sudo nano /etc/apt/sources.list
# deb http://archive.ubuntu.com/ubuntu/ focal main restricted
```

### Låsa paketversion

Förhindra att ett paket uppgraderas.

```bash
# Låsa version
sudo apt-mark hold nginx

# Visa låsta paket
apt-mark showhold

# Lås upp
sudo apt-mark unhold nginx
```

### Rensa cache

```bash
# Radera nedladdade .deb-filer
sudo apt clean

# Radera föråldrade versioner (behåll senaste)
sudo apt autoclean
```

## Cron Jobs - Schemaläggning

Cron används för att exekvera kommandon automatiskt vid förutbestämda tider.

### Crontab-syntax

```bash
# Format: Min  Timme  Dag  Månad  Veckodag  Kommando
#         0-59 0-23  1-31 1-12   0-7      /sökväg/till/kommando

# Exempel
0 2 * * * /path/to/backup.sh
# Exekvera backup.sh kl 02:00 dagligen

*/15 * * * * /path/to/check.sh
# Exekvera check.sh var 15:e minut

0 */2 * * * /path/to/task.sh
# Exekvera task.sh varannan timme

0 0 * * 0 /path/to/weekly.sh
# Exekvera weekly.sh kl 00:00 på söndagar (0 eller 7 = söndag)

0 9 1 * * /path/to/monthly.sh
# Exekvera monthly.sh kl 09:00 den första varje månad
```

### Hantera crontab

```bash
# Redigera din crontab
crontab -e

# Visa din crontab
crontab -l

# Radera din crontab
crontab -r

# Redigera annan användares crontab (som root)
sudo crontab -u username -e
```

### Systemomfattande cron

```bash
# Systemets crontabs
/etc/crontab          # Systemomfattande crontab
/etc/cron.d/          # Katalog för cron-filer
/etc/cron.daily/      # Exekveras dagligen
/etc/cron.weekly/     # Exekveras veckovis
/etc/cron.monthly/    # Exekveras månadsvis

# Placera skript i dessa kataloger
sudo cp backup.sh /etc/cron.daily/
sudo chmod +x /etc/cron.daily/backup.sh
```

### Cron-miljövariabler

```bash
# I crontab, definiera miljövariabler
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=admin@example.com

# Ditt cron-jobb
0 2 * * * /path/to/backup.sh
```

### Logga cron-jobb

```bash
# Cron-loggar finns i
grep CRON /var/log/syslog

# Omdirigera utdata till fil i crontab
0 2 * * * /path/to/backup.sh >> /var/log/backup.log 2>&1

# Skicka utdata till e-post (om MAILTO är definierad)
0 2 * * * /path/to/backup.sh
```

### Speciella cron-scheman

```bash
# @reboot - Exekvera vid systemstart
@reboot /path/to/startup.sh

# @daily - Exekvera en gång per dygn (00:00)
@daily /path/to/daily.sh

# @weekly - Exekvera en gång per vecka (söndag 00:00)
@weekly /path/to/weekly.sh

# @monthly - Exekvera en gång per månad (första dagen 00:00)
@monthly /path/to/monthly.sh

# @yearly eller @annually - Exekvera en gång per år
@yearly /path/to/yearly.sh
```

### Felsökning av cron

```bash
# Kontrollera att crond exekveras
sudo systemctl status cron

# Starta/stoppa cron
sudo systemctl start cron
sudo systemctl stop cron

# Testa cron-jobb manuellt
/path/to/script.sh

# Vanliga problem:
# - PATH-miljövariabel skiljer sig från shell
# - Använd absoluta sökvägar i crontab
# - Kontrollera exekveringsrättigheter (chmod +x)
# - Kontrollera loggar för felmeddelanden
```

## Viktiga lärdomar

- **Allt är en fil**: Sockets, pipes, hårdvara - allt hanteras som filer
- **Lagringsstacken**: Disk → Partition → LUKS → Filsystem → Monteringspunkt
- **LVM-hierarki**: Physical Volume → Volume Group → Logical Volume
- **LVM-fördelar**: Flexibel storlek, snapshots, kombinera diskar
- **Inodes lagrar metadata**, inte själva fildata
- **Hard links** refererar till inode, **symbolic links** refererar till filnamn
- **/bin och /sbin** är kritiska för boot, /usr/bin och /usr/sbin är inte
- **/usr/local/bin** är korrekt plats för egna skript utanför pakethanteraren
- **/proc** är ett virtuellt filsystem som visar systemstatus i realtid
- **Loggar** finns i /var/log - använd `tail -f` för realtidsövervakning
- **apt update** hämtar paketlistor, **apt upgrade** installerar uppdateringar
- **dpkg** är lågnivå, **apt** är högnivå-pakethantering
- **Crontab-format**: Min Timme Dag Månad Veckodag Kommando
- **crontab -e** för redigering, **crontab -l** för visning
- **history, uptime, uname** är viktiga verktyg för systemunderhåll
- **find** är kraftfullt men långsamt, **locate** är snabbt men kräver uppdaterad databas

"""
}
