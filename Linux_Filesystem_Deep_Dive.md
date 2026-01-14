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

## Viktiga takeaways

- **Allt är en fil**: Sockets, pipes, hardware - allt kan hanteras som filer
- **Lagringsstacken**: Disk → Partition → LUKS → Filesystem → Mount
- **Inodes lagrar metadata**, inte själva filinnehållet
- **Hard links** pekar på inode, **symbolic links** pekar på filnamn
- **/bin och /sbin** är kritiska för boot, /usr/bin och /usr/sbin är inte
- **/usr/local/bin** är rätt plats för egna scripts som inte kommer från pakethanteraren
- **/proc** är ett virtuellt filsystem som visar systemtillstånd i realtid
- **Loggar** finns i /var/log - använd `tail -f` för realtidsövervakning
- **history, uptime, uname** är viktiga verktyg för systemunderhåll
- **find** är kraftfullt men långsamt, **locate** är snabbt men kräver uppdaterad databas
