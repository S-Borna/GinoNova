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
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# Filesystem Hierarchy Standard (FHS)

------------------------------------------------------------

## Introduktion

Filesystem Hierarchy Standard (FHS) definierar den logiska strukturen för hur filer och kataloger organiseras i Unix- och Linux-system. Detta är inte bara en teknisk specifikation utan en grundläggande del av Linux-ekosystemet som möjliggör portabilitet, förutsägbarhet och standardisering över olika distributioner.

För en DevOps-ingenjör är förståelsen av FHS absolut kritisk. När du felsöker en produktionsserver klockan tre på natten behöver du intuitivt veta var konfigurationsfiler, loggar och binärer finns. När du skriver automatiseringsskript, Dockerfiles eller Ansible-playbooks förväntas du följa dessa konventioner. Kunskapen om FHS skiljer en junior administratör från en erfaren DevOps-professionell.

FHS-standarden underhålls av Linux Foundation och definierar syftet med varje katalog i roothierarkin. Genom att följa dessa konventioner kan mjukvaruutvecklare skapa program som fungerar konsekvent oavsett vilken Linux-distribution de installeras på.

------------------------------------------------------------

## Teori

### Roothierarkin och dess filosofi

Linux filsystem börjar vid roten, representerad av ett enda snedstreck (/). Till skillnad från Windows med sina separata enhetsbokstäver (C:, D:) har Linux ett enhetligt träd där alla enheter, partitioner och nätverksresurser monteras som grenar.

Denna design följer Unix-filosofin: allt är en fil. Enheter representeras som filer i /dev, processinformation som filer i /proc, och systeminformation i /sys. Detta ger en konsekvent gränssnitt för interaktion med alla systemresurser.

### Primära kataloger och deras syften

```
                            / (root)
                               |
     +---------+-------+-------+-------+-------+-------+-------+
     |         |       |       |       |       |       |       |
   /bin     /etc    /home   /usr    /var    /tmp    /opt    /dev
     |         |       |       |       |       |
  essentiella konfig  users  program  data   temp
  binärer                              loggar
```

**/bin** - Essential User Binaries
Innehåller grundläggande kommandon som måste vara tillgängliga i single-user mode och för alla användare. Här finns ls, cp, mv, cat, echo och andra fundamentala verktyg. I moderna distributioner är /bin ofta en symbolisk länk till /usr/bin.

**/sbin** - System Binaries
Systemadministrationskommandon som normalt kräver root-privilegier: fdisk, fsck, ifconfig, iptables, shutdown. Dessa är nödvändiga för systemunderhåll och återställning.

**/etc** - Configuration Files
Systemomfattande konfigurationsfiler i textformat. Varje installerat program kan ha sin konfiguration här. Kritiska filer inkluderar /etc/passwd (användare), /etc/fstab (filsystemmonteringar), /etc/hosts (namnmappning).

**/home** - User Home Directories
Personliga kataloger för vanliga användare. Varje användare har typiskt /home/användarnamn med egna dokument, konfigurationer och data. Root-användaren har istället /root.

**/var** - Variable Data
Data som ändras under normal systemdrift: loggar (/var/log), email-köer (/var/spool), databaser, cache. Storleken kan växa betydligt och bör ofta vara på separat partition.

**/tmp** - Temporary Files
Temporära filer skapade av program och användare. Rensas typiskt vid omstart. Alla användare har skrivrättigheter men med sticky bit satt (endast ägaren kan ta bort sina filer).

**/usr** - User Programs
Sekundär hierarki för skrivskyddade användardata. Innehåller majoriteten av användarprogrammen och deras dokumentation. Strukturen speglar roothierarkin med /usr/bin, /usr/lib, /usr/share.

**/opt** - Optional Software
Tredjepartsprogramvara som installeras som kompletta paket. Varje program får sin egen katalog: /opt/google/chrome, /opt/containerd. Underlättar installation och borttagning av proprietär mjukvara.

**/dev** - Device Files
Speciella filer som representerar hårdvaruenheter. /dev/sda är första hårddisken, /dev/null är en svart hål som absorberar all output, /dev/random genererar slumpdata.

**/proc** - Process Information
Virtuellt filsystem som exponerar kernel- och processinformation. /proc/cpuinfo visar processordetaljer, /proc/meminfo minnesstatistik, /proc/PID/ information om specifika processer.

**/sys** - System Information
Modernt virtuellt filsystem för enhetsinformation och kernelparametrar. Möjliggör dynamisk konfiguration av kernel utan omstart.

### Skillnaden mellan /bin, /usr/bin och /usr/local/bin

Historiskt separerades dessa för att hantera begränsat diskutrymme och nätverksmontering:

| Katalog | Syfte | Pakethanterare |
|---------|-------|----------------|
| /bin | Essentiella för boot och single-user | Ja |
| /usr/bin | Majoriteten av installerade program | Ja |
| /usr/local/bin | Lokalt kompilerade/installerade | Nej |

I moderna system är /bin ofta en symbolisk länk till /usr/bin, men /usr/local/bin förblir separat för administratörsinstallerade program som inte ska skrivas över av pakethanteraren.

------------------------------------------------------------

## Steg-för-steg Guide

### Utforska rotkatalogen

Börja med att lista innehållet i roten:

```bash
ls -la /
```

Notera de olika katalogtyperna och deras rättigheter. De flesta ägs av root och har begränsade skrivrättigheter.

### Undersök symboliska länkar

Moderna distributioner använder merged-usr-layout:

```bash
ls -la /bin /sbin /lib
```

Du kommer troligen se att dessa är symboliska länkar till motsvarande kataloger under /usr.

### Navigera konfigurationskatalogen

```bash
ls /etc | head -20
cat /etc/os-release
cat /etc/hostname
```

Varje rad i output representerar ett programs eller systems konfiguration.

### Utforska variabel data

```bash
ls -la /var/log
du -sh /var/log/*
tail -f /var/log/syslog
```

Loggar växer kontinuerligt och kräver rotation och övervakning.

### Hitta installerade program

```bash
which python3
whereis nginx
type -a ls
```

Dessa kommandon visar var binärer finns i systemet.

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Felsöka webbserverkonfiguration

```bash
# Hitta nginx-konfiguration
ls -la /etc/nginx/

# Granska huvudkonfigurationen
cat /etc/nginx/nginx.conf

# Kontrollera site-konfigurationer
ls /etc/nginx/sites-enabled/

# Verifiera konfigurationssyntax
nginx -t

# Granska felloggar
tail -100 /var/log/nginx/error.log

# Följ accessloggar i realtid
tail -f /var/log/nginx/access.log
```

### Scenario 2: Installera eget skript systemomfattande

```bash
# Skapa skriptet
cat > ~/myscript.sh << 'EOF'
#!/bin/bash
echo "System uptime: $(uptime -p)"
echo "Disk usage: $(df -h / | tail -1 | awk '{print $5}')"
EOF

# Gör körbart
chmod +x ~/myscript.sh

# Installera i /usr/local/bin (kräver sudo)
sudo cp ~/myscript.sh /usr/local/bin/myscript
sudo chmod 755 /usr/local/bin/myscript

# Verifiera att det finns i PATH
which myscript
myscript
```

### Scenario 3: Analysera diskanvändning per katalog

```bash
# Översikt av rotkatalogernas storlek
sudo du -sh /* 2>/dev/null | sort -h

# Detaljerad analys av /var
sudo du -sh /var/* | sort -h

# Hitta stora filer i loggar
sudo find /var/log -type f -size +100M -exec ls -lh {} \\;

# Kontrollera inodes-användning
df -i
```

------------------------------------------------------------

## Bästa Praxis

**Följ konventionerna**
Placera alltid konfigurationsfiler i /etc, loggar i /var/log, och egna skript i /usr/local/bin. Detta gör systemet förutsägbart för andra administratörer.

**Separera /var på produktionsservrar**
Variabel data, särskilt loggar, kan växa okontrollerat. En separat partition för /var förhindrar att fulla loggar kraschar hela systemet.

**Använd /opt för tredjepartsapplikationer**
Program som inte kommer från distributionens pakethanterare bör installeras i /opt/programnamn för enkel hantering och borttagning.

**Rör aldrig /bin, /lib eller /sbin manuellt**
Dessa hanteras av pakethanteraren. Manuella ändringar kan bryta systemet vid uppdateringar.

**Säkerhetskopiera /etc regelbundet**
Konfigurationskataloger är kritiska. Använd versionskontroll (git) för /etc på servrar eller automatiserade backuper.

**Övervaka /var/log**
Implementera logrotation och övervakning. Fulla diskar på grund av loggar är en vanlig orsak till produktionsproblem.

------------------------------------------------------------

## Vanliga Fallgropar

**Felaktig tolkning av symboliska länkar**
I moderna system är /bin en länk till /usr/bin. Skript som antar absoluta sökvägar kan bete sig olika mellan distributioner.

**Skriva temporära filer till /tmp utan cleanup**
Program som skapar temporära filer måste ta bort dem. /tmp rensas vid omstart men kan fyllas under drift.

**Ignorera loggrotation**
Utan konfigurerad logrotate kan /var/log fylla disken. Kontrollera alltid att /etc/logrotate.d/ har konfiguration för dina applikationer.

**Installera program i /usr/bin manuellt**
Pakethanteraren äger /usr/bin. Manuellt installerade binärer kan skrivas över eller orsaka konflikter.

**Förutsätta identisk struktur över distributioner**
Medan FHS är standard varierar implementationen. Red Hat använder /etc/sysconfig medan Debian använder /etc/default för systemkonfiguration.

------------------------------------------------------------

## Övningar

### Övning 1: Kartlägg systemkonfiguration
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa ett skript som inventerar systemets viktigaste konfigurationsfiler.

**Steg:**
1. Lista alla .conf-filer i /etc
2. Identifiera vilka tjänster som har konfiguration i /etc
3. Kontrollera vilka konfigurationsfiler som ändrats senaste veckan

**Förväntat resultat:**
```bash
#!/bin/bash
echo "=== Konfigurationsfiler i /etc ==="
find /etc -name "*.conf" -type f 2>/dev/null | wc -l

echo "=== Nyligen ändrade (7 dagar) ==="
find /etc -type f -mtime -7 2>/dev/null | head -20

echo "=== Tjänster med konfiguration ==="
ls -d /etc/*/ 2>/dev/null | head -15
```
</details>

### Övning 2: Logganalys och övervakning
<details>
<summary>Visa övning</summary>

**Uppgift:** Analysera systemloggar för att identifiera potentiella problem.

**Steg:**
1. Hitta de 10 största loggfilerna i /var/log
2. Sök efter felmeddelanden i syslog
3. Kontrollera diskutrymme för /var

**Förväntat resultat:**
```bash
# Största loggfilerna
sudo du -sh /var/log/* 2>/dev/null | sort -rh | head -10

# Felmeddelanden senaste timmen
sudo journalctl -p err --since "1 hour ago"

# Diskutrymme
df -h /var
```
</details>

### Övning 3: Skapa FHS-kompatibel applikationsstruktur
<details>
<summary>Visa övning</summary>

**Uppgift:** Designa och implementera en korrekt katalogstruktur för en egen applikation.

**Scenario:** Du ska installera "myapp" version 1.0 på ett system.

**Steg:**
1. Skapa binärkatalog i /opt/myapp
2. Skapa konfiguration i /etc/myapp
3. Skapa loggkatalog i /var/log/myapp
4. Skapa symbolisk länk i /usr/local/bin

**Förväntat resultat:**
```bash
# Skapa strukturen
sudo mkdir -p /opt/myapp/bin
sudo mkdir -p /etc/myapp
sudo mkdir -p /var/log/myapp

# Sätt rättigheter
sudo chmod 755 /opt/myapp /opt/myapp/bin
sudo chmod 755 /etc/myapp
sudo chmod 755 /var/log/myapp

# Skapa en placeholder-binär
echo '#!/bin/bash' | sudo tee /opt/myapp/bin/myapp
echo 'echo "MyApp v1.0"' | sudo tee -a /opt/myapp/bin/myapp
sudo chmod +x /opt/myapp/bin/myapp

# Länka till PATH
sudo ln -s /opt/myapp/bin/myapp /usr/local/bin/myapp

# Verifiera
which myapp
myapp
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående kunskaper:**
- Grundläggande terminalnavigering (cd, ls, pwd)
- Förståelse för fil- och katalogrättigheter

**Relaterade moduler:**
- Mount Points och Device Files - hur externa enheter integreras i FHS
- File Permissions - säkerhet och åtkomstkontroll i filsystemet
- Disk Management - partitionering och filsystemshantering

**Tillämpning i DevOps:**
- Docker: Förståelse för volume mounts och hur containerfilsystem mappar till värd
- Kubernetes: ConfigMaps och Secrets monteras enligt FHS-principer
- Ansible: Templating och filhantering följer FHS-konventioner
- CI/CD: Byggservrar förväntar FHS-struktur för artefakter

------------------------------------------------------------

## Sammanfattning

Filesystem Hierarchy Standard är grunden för all Linux-administration. Genom att förstå syftet med varje katalog kan du effektivt navigera, felsöka och underhålla Linux-system.

De viktigaste katalogerna att memorera är /etc för konfiguration, /var/log för loggar, /usr för program, /home för användardata och /tmp för temporära filer. Moderna system använder ofta merged-usr där /bin, /sbin och /lib är symboliska länkar till motsvarigheter under /usr.

För DevOps-ingenjörer är FHS särskilt relevant vid containerisering, konfigurationshantering och automatisering. Att följa standarderna säkerställer portabilitet och underlättar samarbete i team.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ls -la /` | Visa rotkatalogernas innehåll |
| `which kommando` | Hitta var en binär finns |
| `whereis program` | Hitta binär, källa och manualsida |
| `type -a kommando` | Visa alla platser för ett kommando |
| `du -sh /katalog/*` | Visa storlek per underkatalog |
| `df -h` | Visa diskutrymme per partition |
| `find /etc -name "*.conf"` | Sök efter konfigurationsfiler |
| `tree -L 2 /` | Visa katalogträd (kräver tree) |

------------------------------------------------------------

## Referenser

- Filesystem Hierarchy Standard 3.0: https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
- Linux Foundation FHS Specification
- hier(7) - Linux manual page: `man hier`
- Ubuntu File System Documentation
- Red Hat System Administrator's Guide - File System Structure
""",
        },
        {
            "title": 'Mount Points och Device Files',
            "slug": 'mount-points-device-files',
            "difficulty": "easy",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Mount Points och Device Files

------------------------------------------------------------

## Introduktion

I Unix-filosofin är allt en fil - inklusive hårdvaruenheter, processer och till och med nätverksanslutningar. Denna eleganta abstraktion innebär att samma verktyg och tekniker kan användas för att interagera med vitt skilda resurser. Mount points och device files är fundamentala koncept som möjliggör denna enhetliga vy av systemet.

För DevOps-ingenjörer är förståelsen av hur lagringsenheter representeras och monteras absolut kritisk. Du kommer att arbeta med molnvolymer som dynamiskt ansluts till instanser, containrar som monterar externa volymer, och produktionssystem där diskhantering är en daglig uppgift. Felaktig hantering av mount points kan leda till dataförlust eller systemkrascher.

Mount-konceptet härstammar från Unix tidiga dagar när olika fysiska diskar behövde integreras i ett enhetligt filsystemsträd. Idag omfattar detta även virtuella filsystem, nätverkslagringar och container-volymer, men principerna förblir desamma.

------------------------------------------------------------

## Teori

### Allt är en fil i Linux

Linux representerar alla enheter som filer i /dev-katalogen. Denna design ger flera fördelar:

```
+---------------------------------------------------------------+
|                    Linux Device Model                         |
+---------------------------------------------------------------+
|                                                               |
|   Hårdvara          /dev-fil            Användning            |
|   --------          --------            ----------            |
|   SATA disk    -->  /dev/sda       -->  fdisk, mount          |
|   USB minne    -->  /dev/sdb       -->  mount /mnt/usb        |
|   Terminal     -->  /dev/tty1      -->  echo "test" > tty1    |
|   Slumptal     -->  /dev/urandom   -->  head -c 32 /dev/urandom
|   Null sink    -->  /dev/null      -->  command > /dev/null   |
|                                                               |
+---------------------------------------------------------------+
```

Standardfiloperationer (läsa, skriva, öppna, stänga) fungerar på device files, vilket möjliggör kraftfull scripting och automation.

### Device File Kategorier

**Block devices** representerar enheter som läser och skriver data i block (sektorer). Hårddiskar, SSD:er och USB-minnen är block devices. De har buffrad I/O och stödjer random access.

**Character devices** hanterar data som en ström av tecken. Terminaler, serieportar och ljudenheter är character devices. De är typiskt obuffrade och sekventiella.

```bash
ls -la /dev/sda /dev/tty1
# brw-rw---- 1 root disk    8, 0 Dec  1 10:00 /dev/sda
# crw--w---- 1 root tty     4, 1 Dec  1 10:00 /dev/tty1
```

Första tecknet indikerar typ: 'b' för block, 'c' för character.

### Enhetsnamnskonventioner

| Mönster | Enhetstyp | Exempel |
|---------|-----------|---------|
| sd[a-z] | SATA/SCSI/USB disk | sda, sdb, sdc |
| sd[a-z][1-9] | Partition på disk | sda1, sda2, sdb1 |
| nvme[0-9]n[1-9] | NVMe SSD | nvme0n1, nvme1n1 |
| nvme[0-9]n[1-9]p[1-9] | NVMe partition | nvme0n1p1 |
| vd[a-z] | Virtio disk (KVM/QEMU) | vda, vdb |
| xvd[a-z] | Xen virtual disk (AWS) | xvda, xvdf |
| loop[0-9] | Loop device (mount fil som disk) | loop0, loop1 |

### Mount Points - Konceptet

Ett mount point är en katalog i filsystemsträdet där ett filsystem ansluts. När en enhet monteras blir dess innehåll tillgängligt under den katalogen.

```
Före mount:                    Efter mount:

/                              /
├── home/                      ├── home/
├── var/                       ├── var/
└── mnt/                       └── mnt/
    └── data/ (tom)                └── data/
                                       ├── file1.txt
                                       ├── file2.txt
                                       └── subdir/

                               /dev/sdb1 monterad på /mnt/data
```

### Filsystemstyper

| Filsystem | Användning | Egenskaper |
|-----------|------------|------------|
| ext4 | Linux standard | Journaling, stabil, vältestad |
| xfs | Enterprise, stora filer | Hög prestanda, skalbart |
| btrfs | Moderna system | Copy-on-write, snapshots |
| ntfs | Windows-kompabilitet | Fullt stöd via ntfs-3g |
| vfat/fat32 | USB, SD-kort | Universell kompatibilitet |
| tmpfs | RAM-baserat | Volatilt, extremt snabbt |
| nfs | Nätverkslagring | Delad åtkomst över nätverk |

### /etc/fstab - Permanent Konfiguration

Filen /etc/fstab definierar vilka filsystem som ska monteras vid boot:

```
# <file system>        <mount point>  <type>  <options>       <dump>  <pass>
UUID=abc123-def456     /              ext4    defaults        0       1
UUID=789ghi-012jkl     /home          ext4    defaults        0       2
UUID=mno345-pqr678     /var/log       xfs     defaults        0       2
/dev/sdb1              /mnt/data      ext4    defaults,nofail 0       2
tmpfs                  /tmp           tmpfs   size=2G         0       0
```

| Fält | Beskrivning |
|------|-------------|
| file system | UUID, LABEL, eller device path |
| mount point | Katalog där filsystemet monteras |
| type | Filsystemstyp (ext4, xfs, nfs, etc.) |
| options | Mount-optioner (defaults, ro, noexec, etc.) |
| dump | Backup med dump (0=nej, 1=ja) |
| pass | fsck ordning (0=hoppa, 1=root först, 2=efteråt) |

### Viktiga Mount-optioner

| Option | Beskrivning |
|--------|-------------|
| defaults | rw, suid, dev, exec, auto, nouser, async |
| ro / rw | Read-only / Read-write |
| noexec | Förhindra körning av binärer |
| nosuid | Ignorera setuid/setgid bits |
| noatime | Uppdatera inte access time (prestanda) |
| nofail | Boot fortsätter även om mount misslyckas |
| _netdev | Vänta på nätverk (för nätverksvolymer) |

------------------------------------------------------------

## Steg-för-steg Guide

### Identifiera tillgängliga enheter

```bash
# Lista alla blockenheter
lsblk

# Mer detaljerad information
lsblk -f

# Visa partitionstabell
sudo fdisk -l

# Identifiera enhets-UUID
blkid
```

### Skapa mount point och montera

```bash
# Skapa katalog för mount point
sudo mkdir -p /mnt/data

# Montera enheten
sudo mount /dev/sdb1 /mnt/data

# Verifiera
df -h /mnt/data
mount | grep sdb1
```

### Konfigurera permanent mount

```bash
# Hämta UUID
sudo blkid /dev/sdb1
# /dev/sdb1: UUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890" TYPE="ext4"

# Lägg till i fstab
echo 'UUID=a1b2c3d4-e5f6-7890-abcd-ef1234567890 /mnt/data ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab

# VIKTIGT: Testa innan reboot
sudo mount -a

# Verifiera
mount | grep /mnt/data
```

### Avmontera säkert

```bash
# Kontrollera om enheten används
lsof /mnt/data

# Avmontera
sudo umount /mnt/data

# Om "target is busy" - hitta processer
sudo fuser -mv /mnt/data

# Tvingad avmontering (lazy unmount)
sudo umount -l /mnt/data
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Montera AWS EBS-volym

```bash
# Lista tillgängliga enheter (ny volym visas som xvdf)
lsblk
# NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
# xvda    202:0    0  8G   0 disk
# └─xvda1 202:1    0  8G   0 part /
# xvdf    202:80   0 100G  0 disk

# Kontrollera om volymen har filsystem
sudo file -s /dev/xvdf
# /dev/xvdf: data  (betyder ingen filsystem)

# Skapa filsystem (ENDAST för nya volymer!)
sudo mkfs -t ext4 /dev/xvdf

# Skapa mount point
sudo mkdir /data

# Montera
sudo mount /dev/xvdf /data

# Gör permanent (hämta UUID först)
UUID=$(sudo blkid -s UUID -o value /dev/xvdf)
echo "UUID=$UUID /data ext4 defaults,nofail 0 2" | sudo tee -a /etc/fstab

# Sätt ägarskap för applikationsanvändare
sudo chown -R appuser:appgroup /data
```

### Scenario 2: Montera NFS-share

```bash
# Installera NFS-klient
sudo apt install nfs-common  # Debian/Ubuntu
sudo yum install nfs-utils   # RHEL/CentOS

# Visa tillgängliga exports från NFS-server
showmount -e nfs-server.example.com

# Skapa mount point
sudo mkdir -p /mnt/nfs/shared

# Montera NFS-share
sudo mount -t nfs nfs-server.example.com:/exports/shared /mnt/nfs/shared

# Permanent mount i fstab
echo 'nfs-server.example.com:/exports/shared /mnt/nfs/shared nfs defaults,_netdev 0 0' | sudo tee -a /etc/fstab
```

### Scenario 3: RAM-disk för temporär högpresterande lagring

```bash
# Skapa mount point
sudo mkdir /mnt/ramdisk

# Montera tmpfs med 2GB storlek
sudo mount -t tmpfs -o size=2G tmpfs /mnt/ramdisk

# Verifiera
df -h /mnt/ramdisk
# Filesystem      Size  Used Avail Use% Mounted on
# tmpfs           2.0G     0  2.0G   0% /mnt/ramdisk

# Permanent i fstab
echo 'tmpfs /mnt/ramdisk tmpfs size=2G,mode=1777 0 0' | sudo tee -a /etc/fstab
```

------------------------------------------------------------

## Bästa Praxis

**Använd alltid UUID i fstab**
Enhetsnamn som /dev/sdb kan ändras om diskar läggs till eller tas bort. UUID är garanterat unikt och stabilt.

**Inkludera nofail för icke-kritiska volymer**
Optionen nofail förhindrar att systemet fastnar vid boot om en volym saknas. Kritiskt för molnmiljöer där volymer kan vara tillfälligt otillgängliga.

**Testa alltid med mount -a**
Innan du startar om systemet, validera fstab genom att köra mount -a. Ett fel i fstab kan förhindra boot.

**Dokumentera mount points**
Kommentera fstab-rader med syftet för varje volym. Framtida administratörer (inklusive du själv) kommer att tacka dig.

**Använd noexec och nosuid för datavolymer**
Volymer som endast innehåller data bör monteras med noexec,nosuid för ökad säkerhet.

**Övervaka diskanvändning**
Implementera övervakning för mount points för att upptäcka fulla diskar innan de orsakar problem.

------------------------------------------------------------

## Vanliga Fallgropar

**Redigera fstab utan att testa**
Ett syntaxfel eller felaktig UUID i fstab kan göra systemet obootbart. Testa alltid med mount -a och ha en recovery-plan.

**Glömma _netdev för nätverksvolymer**
NFS och iSCSI-volymer kräver att nätverket är tillgängligt. Utan _netdev försöker systemet montera innan nätverk är uppe.

**Använda /dev/sdX istället för UUID**
Enhetsnamn kan ändras mellan omstarter eller när hårdvara läggs till/tas bort. UUID är den säkra metoden.

**Avmontera utan att kontrollera användning**
Att tvinga avmontering medan processer använder volymen kan orsaka dataförlust. Kontrollera alltid med lsof först.

**Skapa filsystem på fel enhet**
Kommandot mkfs raderar all data. Dubbelkolla alltid enhetsnamnet och att det är rätt disk före formatering.

**Glömma att skapa mount point**
Mount-kommandot kräver att målkatalogen existerar. Skapa alltid katalogen först med mkdir -p.

------------------------------------------------------------

## Övningar

### Övning 1: Utforska systemets enheter
<details>
<summary>Visa övning</summary>

**Uppgift:** Kartlägg alla blockenheter och deras mount status på ditt system.

**Steg:**
1. Använd lsblk för att lista alla blockenheter
2. Identifiera vilka enheter som är monterade och var
3. Använd blkid för att hitta UUID för varje partition
4. Jämför med /etc/fstab

**Förväntade kommandon:**
```bash
lsblk -f
sudo blkid
cat /etc/fstab
findmnt --fstab
```
</details>

### Övning 2: Säker volymhantering
<details>
<summary>Visa övning</summary>

**Uppgift:** Simulera att montera en ny datavolym (använd loop device om du inte har extra disk).

**Steg:**
1. Skapa en fil som fungerar som virtuell disk
2. Associera med loop device
3. Skapa filsystem
4. Montera och testa
5. Lägg till i fstab med nofail

**Lösning:**
```bash
# Skapa 100MB diskfil
dd if=/dev/zero of=/tmp/virtual_disk.img bs=1M count=100

# Associera med loop device
sudo losetup /dev/loop0 /tmp/virtual_disk.img

# Skapa filsystem
sudo mkfs.ext4 /dev/loop0

# Montera
sudo mkdir /mnt/virtual
sudo mount /dev/loop0 /mnt/virtual

# Verifiera
df -h /mnt/virtual
echo "test" | sudo tee /mnt/virtual/testfile

# Städa upp
sudo umount /mnt/virtual
sudo losetup -d /dev/loop0
```
</details>

### Övning 3: Felsökning av mount-problem
<details>
<summary>Visa övning</summary>

**Uppgift:** Diagnostisera och åtgärda vanliga mount-problem.

**Scenario:** En volym vägrar avmonteras med "target is busy".

**Steg:**
1. Identifiera vilka processer som använder volymen
2. Avsluta eller flytta processerna
3. Avmontera säkert

**Lösning:**
```bash
# Hitta processer som använder mount point
sudo lsof +D /mnt/data

# Alternativt
sudo fuser -mv /mnt/data

# Avsluta processer (varsamt)
sudo fuser -k /mnt/data

# Nu kan vi avmontera
sudo umount /mnt/data

# Verifier
mount | grep /mnt/data
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående kunskaper:**
- Filesystem Hierarchy Standard (FHS) - förståelse för Linux katalogstruktur
- Grundläggande terminalkommandon

**Relaterade moduler:**
- Disk Management (LVM, partitionering) - avancerad volymhantering
- File Permissions - säkerhet för monterade volymer
- systemd - mount units som alternativ till fstab

**Tillämpning i DevOps:**
- Docker volumes och bind mounts
- Kubernetes Persistent Volumes och Storage Classes
- AWS EBS, Azure Disks, GCP Persistent Disks
- NFS för delad lagring i kluster

------------------------------------------------------------

## Sammanfattning

Mount points och device files är grundläggande koncept för Linux-lagring. Alla enheter representeras som filer i /dev-katalogen, och mount-processen integrerar filsystem i det enhetliga katalogträdet.

Nyckelverktyg inkluderar lsblk för att lista enheter, mount och umount för att ansluta och koppla bort volymer, samt blkid för att identifiera UUID. Filen /etc/fstab konfigurerar permanenta mount points som aktiveras vid boot.

Bästa praxis omfattar att alltid använda UUID istället för enhetsnamn, inkludera nofail för icke-kritiska volymer, och testa med mount -a innan omstart. Säker avmontering kräver att inga processer använder volymen.

Förståelse för dessa koncept är direkt tillämpbar i molnmiljöer (EBS, Azure Disks), containerplattformar (Docker volumes, K8s PV), och traditionell serveradministration.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `lsblk` | Lista blockenheter och mount points |
| `lsblk -f` | Inkludera filsystem och UUID |
| `blkid` | Visa UUID och filsystemtyp |
| `mount /dev/sdb1 /mnt/data` | Montera enhet |
| `umount /mnt/data` | Avmontera enhet |
| `mount -a` | Montera allt i fstab |
| `findmnt` | Visa mount-träd |
| `df -h` | Visa diskutrymme per mount |
| `lsof +D /mnt/data` | Hitta processer som använder path |
| `fuser -mv /mnt/data` | Visa processer på mount point |

------------------------------------------------------------

## Referenser

- mount(8) - Linux manual page
- fstab(5) - File systems table manual
- blkid(8) - Block device attributes
- Linux Kernel Documentation - Block Devices
- Red Hat Storage Administration Guide
- Ubuntu Server Guide - Disk Management
""",
        },
        {
            "title": 'File Permissions',
            "slug": 'file-permissions',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# File Permissions

------------------------------------------------------------

## Introduktion

Linux file permissions utgör fundamentet för systemsäkerhet och åtkomstkontroll. I DevOps-sammanhang möter du permissions dagligen när deploy-scripts vägrar köra, webbservrar returnerar 403 Forbidden, eller SSH-nycklar inte accepteras. Att behärska permissions är skillnaden mellan frustrerande felsökning och snabb problemlösning. Denna modul ger dig djup förståelse för hur permissions fungerar, från grundläggande rwx-koncept till avancerade ACLs och special bits.

------------------------------------------------------------

## Teori

Linux permissions-modellen bygger på tre grundpelare: ägare (owner), grupp (group), och övriga (others). Varje fil och katalog har tre typer av åtkomsträttigheter: read (r), write (w), och execute (x).

```
+------------------------------------------------------------------+
|                    PERMISSION STRING ANATOMY                      |
+------------------------------------------------------------------+
|                                                                   |
|   -rwxr-xr-- 1 deploy www-data 4096 Jun 15 10:30 app.py          |
|   ||||||||||                                                      |
|   |||||||||+-- Others: r-- (read only)                           |
|   ||||||+++--- Group:  r-x (read + execute)                      |
|   |||+++------ Owner:  rwx (full access)                         |
|   ||+--------- Sticky/SetGID/SetUID bits                         |
|   |+---------- File type: - (regular file)                       |
|   |                       d (directory)                          |
|   |                       l (symbolic link)                      |
|   |                       c (character device)                   |
|   |                       b (block device)                       |
|   |                       s (socket)                             |
|   |                       p (named pipe)                         |
|                                                                   |
+------------------------------------------------------------------+
```

Permissions representeras både symboliskt (rwx) och oktalt (siffror). Det oktala systemet baseras på binär representation där varje permission har ett värde: read=4, write=2, execute=1.

```
+------------------------------------------------------------------+
|                    OKTAL PERMISSION BERÄKNING                     |
+------------------------------------------------------------------+
|                                                                   |
|   Permission    Binary    Decimal                                 |
|   ---------    ------    -------                                  |
|   ---          000       0                                        |
|   --x          001       1                                        |
|   -w-          010       2                                        |
|   -wx          011       3                                        |
|   r--          100       4                                        |
|   r-x          101       5                                        |
|   rw-          110       6                                        |
|   rwx          111       7                                        |
|                                                                   |
|   Exempel: rwxr-xr-- = 754                                        |
|   Owner:  rwx = 4+2+1 = 7                                         |
|   Group:  r-x = 4+0+1 = 5                                         |
|   Others: r-- = 4+0+0 = 4                                         |
|                                                                   |
+------------------------------------------------------------------+
```

Special permission bits utökar standardmodellen. SetUID (4000) kör programmet som filens ägare, SetGID (2000) kör som gruppägare eller ärvs till nya filer i kataloger, och Sticky bit (1000) förhindrar att användare raderar andras filer i delade kataloger.

```
+------------------------------------------------------------------+
|                    SPECIAL PERMISSION BITS                        |
+------------------------------------------------------------------+
|                                                                   |
|   SetUID (4xxx) - Execute as file owner                          |
|   +---------------+                                               |
|   | /usr/bin/sudo |  -rwsr-xr-x  (s i owner execute)            |
|   +---------------+                                               |
|   Användare kör sudo -> körs som root                            |
|                                                                   |
|   SetGID (2xxx) - Execute as group / inherit group               |
|   +---------------+                                               |
|   | /shared/docs  |  drwxrwsr-x  (s i group execute)            |
|   +---------------+                                               |
|   Nya filer ärver gruppägare                                     |
|                                                                   |
|   Sticky Bit (1xxx) - Restricted deletion                        |
|   +---------------+                                               |
|   | /tmp          |  drwxrwxrwt  (t i others execute)           |
|   +---------------+                                               |
|   Endast ägare kan radera sina filer                             |
|                                                                   |
+------------------------------------------------------------------+
```

Umask bestämmer standardpermissions för nya filer genom att subtrahera från maxvärdet. Default umask 022 ger filer 644 (666-022) och kataloger 755 (777-022).

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Analysera befintliga permissions**

```bash
# Visa detaljerad fillista
ls -la /var/www/app/

# Tolka output
# -rw-r--r-- = fil med 644 permissions
# drwxr-xr-x = katalog med 755 permissions

# Visa numeriska permissions
stat -c "%a %n" /var/www/app/*

# Visa ägare och grupp
stat -c "%U:%G %n" /var/www/app/*
```

**Steg 2: Ändra permissions med chmod**

```bash
# Symbolisk notation
chmod u+x script.sh          # Lägg till execute för owner
chmod g-w config.yml         # Ta bort write för group
chmod o=r public.html        # Sätt endast read för others
chmod a+r README.md          # Lägg till read för alla
chmod u=rwx,g=rx,o=r file    # Explicit sätta alla

# Oktal notation (vanligast)
chmod 755 deploy.sh          # rwxr-xr-x - körbara scripts
chmod 644 config.yml         # rw-r--r-- - konfigurationsfiler
chmod 600 secrets.env        # rw------- - känsliga filer
chmod 700 ~/.ssh             # rwx------ - SSH-katalog

# Rekursivt
chmod -R 755 /var/www/app/
chmod -R u+rwX,g+rX,o+rX /var/www/  # X = execute endast för kataloger
```

**Steg 3: Ändra ägare med chown**

```bash
# Ändra endast ägare
sudo chown deploy script.sh

# Ändra ägare och grupp
sudo chown deploy:www-data /var/www/app/

# Rekursivt ändra ägare
sudo chown -R deploy:deploy /opt/app/

# Kopiera ägare från annan fil
sudo chown --reference=/var/www/index.html newfile.html
```

**Steg 4: Ändra grupp med chgrp**

```bash
# Ändra grupp
sudo chgrp www-data /var/www/app/

# Rekursivt
sudo chgrp -R developers /opt/projects/
```

**Steg 5: Konfigurera special bits**

```bash
# SetGID på delad katalog (nya filer ärver grupp)
sudo chmod g+s /shared/projects/

# Sticky bit på temporär katalog
sudo chmod +t /var/tmp/uploads/

# SetUID (använd med försiktighet!)
sudo chmod u+s /usr/local/bin/special-tool

# Oktal notation med special bits
chmod 2775 /shared/projects/  # SetGID + rwxrwxr-x
chmod 1777 /tmp/uploads/      # Sticky + rwxrwxrwx
```

**Steg 6: Konfigurera umask**

```bash
# Visa aktuell umask
umask

# Sätt umask för sessionen
umask 027  # Nya filer: 640, kataloger: 750

# Permanent i bashrc
echo "umask 027" >> ~/.bashrc

# Testa umask
umask 022
touch testfile
ls -la testfile  # -rw-r--r-- (644)
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Webbserver-konfiguration**

```bash
# Struktur för Nginx/Apache-sajt
/var/www/myapp/
    ├── public/          # Webbåtkomliga filer
    ├── storage/         # Uppladdningar, cache
    ├── config/          # Konfiguration
    └── .env             # Miljövariabler

# Sätt korrekta permissions
sudo chown -R deploy:www-data /var/www/myapp/
sudo chmod -R 750 /var/www/myapp/
sudo chmod -R 755 /var/www/myapp/public/
sudo chmod -R 770 /var/www/myapp/storage/
sudo chmod 640 /var/www/myapp/.env
sudo chmod 640 /var/www/myapp/config/*

# Säkerställ SetGID för storage (nya filer ärver www-data grupp)
sudo chmod g+s /var/www/myapp/storage/
```

**Exempel 2: SSH-säkerhet**

```bash
# SSH-katalogstruktur
~/.ssh/
    ├── authorized_keys  # Publika nycklar för inloggning
    ├── config           # SSH-klientkonfiguration
    ├── id_rsa           # Privat nyckel
    ├── id_rsa.pub       # Publik nyckel
    └── known_hosts      # Kända servrar

# KRITISKA permissions (SSH vägrar annars!)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/config
chmod 644 ~/.ssh/known_hosts

# Verifiera
ls -la ~/.ssh/
# drwx------ .ssh
# -rw------- id_rsa
# -rw-r--r-- id_rsa.pub
```

**Exempel 3: CI/CD Deploy Pipeline**

```bash
#!/bin/bash
# deploy.sh - Production deployment script

APP_DIR="/var/www/production"
DEPLOY_USER="deploy"
WEB_GROUP="www-data"

# Säkerställ korrekta permissions efter deploy
fix_permissions() {
    echo "Fixing permissions..."

    # Ägare och grupp
    sudo chown -R $DEPLOY_USER:$WEB_GROUP $APP_DIR

    # Kataloger: 755 (rwxr-xr-x)
    find $APP_DIR -type d -exec chmod 755 {} \;

    # Filer: 644 (rw-r--r--)
    find $APP_DIR -type f -exec chmod 644 {} \;

    # Körbara scripts: 755
    find $APP_DIR/bin -type f -exec chmod 755 {} \;

    # Känsliga filer: 640
    chmod 640 $APP_DIR/.env
    chmod 640 $APP_DIR/config/secrets.yml

    # Skrivbara kataloger för webbserver
    chmod 775 $APP_DIR/storage
    chmod 775 $APP_DIR/cache

    echo "Permissions fixed!"
}

fix_permissions
```

**Exempel 4: Delad utvecklingsmiljö**

```bash
# Skapa delad projektkatalog
sudo mkdir -p /opt/projects/team-app
sudo groupadd developers
sudo usermod -aG developers alice
sudo usermod -aG developers bob

# Konfigurera permissions
sudo chown root:developers /opt/projects/team-app
sudo chmod 2775 /opt/projects/team-app

# SetGID (2) säkerställer att nya filer ärver 'developers' grupp
# 775 = rwxrwxr-x

# Testa
su - alice
cd /opt/projects/team-app
touch alices-file.txt
ls -la alices-file.txt
# -rw-rw-r-- alice developers  <- grupp ärvdes!
```

------------------------------------------------------------

## Bästa Praxis

**Principle of Least Privilege**
Ge aldrig mer permissions än nödvändigt. En webbserver behöver sällan skrivåtkomst utanför specifika kataloger.

**Använd grupper för åtkomstkontroll**
Istället för att ge permissions till 'others', skapa grupper och lägg till användare i rätt grupper.

**Standardisera permissions i deployment**
Inkludera permission-fixing i alla deploy-scripts för konsistens.

**Dokumentera avvikelser**
Om en fil kräver ovanliga permissions (t.ex. SetUID), dokumentera varför.

**Granska regelbundet**
Kör periodiska audits för att hitta filer med för öppna permissions.

```bash
# Hitta världsskrivbara filer
find /var/www -type f -perm -002 -ls

# Hitta SetUID/SetGID-filer
find / -type f \( -perm -4000 -o -perm -2000 \) -ls 2>/dev/null

# Hitta filer utan ägare
find / -nouser -o -nogroup 2>/dev/null
```

------------------------------------------------------------

## Vanliga Fallgropar

**Rekursiv chmod 777**
Absolut förbjudet i produktion. Gör systemet sårbart och bryter applikationer som förväntar sig specifika permissions.

**Glömma X för kataloger**
Execute på kataloger krävs för att kunna "gå in" i dem. Utan x kan du inte lista innehållet även med r.

**SSH permission errors**
SSH är strikt med permissions. Privata nycklar MÅSTE vara 600, .ssh-katalogen 700.

**Ändra permissions på systemfiler**
Ändra aldrig permissions på /etc, /usr eller andra systemkataloger utan att veta exakt vad du gör.

**Glömma rekursiv flagga**
`chown deploy:deploy /var/www/app` ändrar bara katalogen, inte innehållet.

------------------------------------------------------------

## Övningar

### Övning 1: Permission Audit
<details>
<summary>Visa övning</summary>

**Uppgift:** Analysera och dokumentera permissions för en webbapplikation.

**Steg:**
1. Skapa en teststruktur som simulerar en webbapp
2. Analysera permissions med olika verktyg
3. Identifiera säkerhetsproblem
4. Åtgärda och dokumentera ändringar

**Lösning:**
```bash
# Skapa teststruktur
mkdir -p /tmp/webapp/{public,config,storage,logs}
touch /tmp/webapp/.env
touch /tmp/webapp/config/database.yml
touch /tmp/webapp/public/index.html

# Simulera osäkra permissions
chmod 777 /tmp/webapp/storage
chmod 644 /tmp/webapp/.env
chmod 755 /tmp/webapp/config/database.yml

# Audit
echo "=== Permission Audit ==="
find /tmp/webapp -ls

# Hitta problem
echo "=== Världsskrivbara filer ==="
find /tmp/webapp -perm -002 -ls

# Åtgärda
chmod 770 /tmp/webapp/storage
chmod 600 /tmp/webapp/.env
chmod 640 /tmp/webapp/config/database.yml

# Verifiera
echo "=== Efter åtgärd ==="
find /tmp/webapp -ls
```
</details>

### Övning 2: Delad utvecklingskatalog
<details>
<summary>Visa övning</summary>

**Uppgift:** Konfigurera en delad katalog där flera utvecklare kan samarbeta.

**Scenario:** Team "devops" behöver en delad katalog där alla kan skapa och redigera filer, men bara ägaren kan radera sina egna filer.

**Steg:**
1. Skapa grupp och användare
2. Konfigurera katalog med korrekta permissions
3. Testa collaboration-scenariot

**Lösning:**
```bash
# Skapa grupp
sudo groupadd devops-team

# Skapa testanvändare (eller lägg till befintliga)
sudo useradd -m -G devops-team dev1
sudo useradd -m -G devops-team dev2

# Skapa delad katalog
sudo mkdir /opt/shared-projects
sudo chown root:devops-team /opt/shared-projects

# SetGID + Sticky bit
# SetGID: nya filer ärver grupp
# Sticky: endast ägare kan radera sina filer
sudo chmod 3775 /opt/shared-projects
# 3 = 2 (SetGID) + 1 (Sticky)

# Verifiera
ls -la /opt/shared-projects
# drwxrwsr-t root devops-team

# Testa som dev1
sudo -u dev1 touch /opt/shared-projects/dev1-file.txt

# Verifiera att grupp ärvdes
ls -la /opt/shared-projects/dev1-file.txt
# -rw-rw-r-- dev1 devops-team

# dev2 kan INTE radera dev1s fil (sticky bit)
sudo -u dev2 rm /opt/shared-projects/dev1-file.txt
# rm: cannot remove: Operation not permitted
```
</details>

### Övning 3: Deploy Permission Script
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa ett robust script för att sätta korrekta permissions vid deployment.

**Krav:**
- Sätt ägare till deploy:www-data
- Kataloger: 755, Filer: 644
- Scripts i bin/: 755
- Känsliga filer: 640
- Storage-katalog: 775 med SetGID

**Lösning:**
```bash
#!/bin/bash
# fix-deploy-permissions.sh

set -e

APP_DIR="${1:-/var/www/app}"
OWNER="deploy"
GROUP="www-data"

if [ ! -d "$APP_DIR" ]; then
    echo "Error: Directory $APP_DIR does not exist"
    exit 1
fi

echo "Fixing permissions for $APP_DIR..."

# Ägare och grupp
sudo chown -R $OWNER:$GROUP "$APP_DIR"

# Kataloger: 755
find "$APP_DIR" -type d -exec chmod 755 {} \;

# Filer: 644
find "$APP_DIR" -type f -exec chmod 644 {} \;

# Körbara scripts
if [ -d "$APP_DIR/bin" ]; then
    find "$APP_DIR/bin" -type f -exec chmod 755 {} \;
fi

# Känsliga filer
for sensitive in ".env" "config/secrets.yml" "config/database.yml"; do
    if [ -f "$APP_DIR/$sensitive" ]; then
        chmod 640 "$APP_DIR/$sensitive"
    fi
done

# Storage med SetGID
if [ -d "$APP_DIR/storage" ]; then
    chmod 2775 "$APP_DIR/storage"
    find "$APP_DIR/storage" -type d -exec chmod 2775 {} \;
fi

echo "Permissions fixed successfully!"

# Visa resultat
echo "=== Verification ==="
ls -la "$APP_DIR"
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Filesystem Hierarchy Standard (FHS) - förståelse för katalogstruktur
- Mount Points och Device Files - förståelse för filsystemtyper

**Relaterade noder:**
- User and Group Management - skapa och hantera användare/grupper
- SSH Hardening - SSH-specifika permission-krav
- Sudo Configuration - privilege escalation

**Kommande noder:**
- PAM Modules - avancerad autentisering
- SELinux/AppArmor - mandatory access control (MAC)

------------------------------------------------------------

## Sammanfattning

Linux file permissions är grundläggande för systemsäkerhet och DevOps-arbete. Modellen baseras på tre användarkategorier (owner, group, others) och tre åtkomsttyper (read, write, execute). Permissions uttrycks symboliskt (rwx) eller oktalt (siffror), där standardvärden för filer är 644 och för kataloger 755.

Special bits (SetUID, SetGID, Sticky) utökar funktionaliteten för specifika användningsfall som delade kataloger och privilegierade program. SSH har strikta krav där privata nycklar måste vara 600 och .ssh-katalogen 700.

Best practices inkluderar principle of least privilege, användning av grupper istället för 'others', och inkludering av permission-fixing i deploy-scripts. Rekursiv chmod 777 är alltid fel i produktion.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ls -la` | Lista filer med permissions |
| `stat file` | Detaljerad filinformation |
| `chmod 755 file` | Sätt permissions oktalt |
| `chmod u+x file` | Lägg till execute för owner |
| `chmod -R 644 dir/` | Rekursiv permission-ändring |
| `chown user:group file` | Ändra ägare och grupp |
| `chown -R user dir/` | Rekursiv ägarändring |
| `chgrp group file` | Ändra endast grupp |
| `umask` | Visa/sätt default permissions |
| `chmod g+s dir/` | Sätt SetGID på katalog |
| `chmod +t dir/` | Sätt Sticky bit |
| `find -perm -002` | Hitta världsskrivbara filer |

------------------------------------------------------------

## Referenser

- Linux man pages: chmod(1), chown(1), stat(1)
- Linux Documentation Project - File Permissions
- OWASP File System Security Guidelines
- CIS Benchmark - Linux File Permissions
- Red Hat Security Guide - Securing Files
""",
        },
        {
            "title": 'Inodes, Hard Links och Symbolic Links',
            "slug": 'inodes-links',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Inodes, Hard Links och Symbolic Links

------------------------------------------------------------

## Introduktion

Inodes och länkar är fundamentala koncept för att förstå hur Linux filsystem verkligen fungerar. För DevOps-ingenjörer är denna kunskap kritisk för zero-downtime deployments (via symlinks), felsökning av "disk full" när utrymme finns (inode exhaustion), och förståelse för varför raderade filer fortfarande tar plats. Denna modul tar dig under huven på Linux filsystem och visar hur du utnyttjar länkar för robusta deployment-strategier.

------------------------------------------------------------

## Teori

En inode (index node) är en datastruktur som lagrar all metadata om en fil utom dess namn. Varje fil och katalog i ett Linux-filsystem har exakt en inode som innehåller permissions, ägare, timestamps, storlek och pekare till datablockens.

```
+------------------------------------------------------------------+
|                         INODE STRUCTURE                           |
+------------------------------------------------------------------+
|                                                                   |
|   Filnamn: "config.yml"                                          |
|         |                                                         |
|         v                                                         |
|   +--------------------+                                          |
|   | Directory Entry    |                                          |
|   | Name: config.yml   |                                          |
|   | Inode: 2847593     |---+                                      |
|   +--------------------+   |                                      |
|                            |                                      |
|                            v                                      |
|   +--------------------------------------------+                  |
|   | Inode 2847593                              |                  |
|   +--------------------------------------------+                  |
|   | Mode:        100644 (rw-r--r--)            |                  |
|   | Link count:  1                             |                  |
|   | UID:         1000 (deploy)                 |                  |
|   | GID:         1000 (deploy)                 |                  |
|   | Size:        2048 bytes                    |                  |
|   | Timestamps:  atime, mtime, ctime           |                  |
|   | Block ptrs:  [234] [235] [236]             |---+              |
|   +--------------------------------------------+   |              |
|                                                    |              |
|                                                    v              |
|   +------------------+------------------+------------------+      |
|   | Data Block 234   | Data Block 235   | Data Block 236   |      |
|   | [actual file     | [content         | [continued...]   |      |
|   |  content...]     |  continued...]   |                  |      |
|   +------------------+------------------+------------------+      |
|                                                                   |
+------------------------------------------------------------------+
```

Filnamnet är bara en etikett (directory entry) som pekar på en inode. Detta möjliggör att samma inode kan ha flera namn - detta kallas hard links.

```
+------------------------------------------------------------------+
|                         HARD LINKS                                |
+------------------------------------------------------------------+
|                                                                   |
|   "original.txt" --------+                                        |
|                          |                                        |
|                          v                                        |
|                  +---------------+                                |
|                  | Inode 12345   |                                |
|                  +---------------+                                |
|                  | Link count: 2 |------> [Data Blocks]          |
|                  +---------------+                                |
|                          ^                                        |
|                          |                                        |
|   "backup.txt" ----------+                                        |
|                                                                   |
|   Båda namnen är LIKVÄRDIGA                                      |
|   Data raderas först när link count = 0                          |
|                                                                   |
+------------------------------------------------------------------+
```

Symbolic links (symlinks) är en helt annan mekanism. En symlink är en egen fil med egen inode som innehåller en sökväg till en annan fil.

```
+------------------------------------------------------------------+
|                      SYMBOLIC LINKS                               |
+------------------------------------------------------------------+
|                                                                   |
|   +-------------------+                                           |
|   | "current"         |                                           |
|   | Inode: 99999      |                                           |
|   +-------------------+                                           |
|            |                                                      |
|            v                                                      |
|   +-------------------+                                           |
|   | Inode 99999       |                                           |
|   | Type: symlink     |                                           |
|   | Content: path     |---> "/app/releases/v2.0"                 |
|   +-------------------+                                           |
|                                     |                             |
|                                     v                             |
|                            +-------------------+                  |
|                            | Directory Entry   |                  |
|                            | v2.0 -> Inode X   |                  |
|                            +-------------------+                  |
|                                     |                             |
|                                     v                             |
|                            [Actual Application Files]             |
|                                                                   |
+------------------------------------------------------------------+
```

Skillnaderna mellan hard links och symlinks:

```
+------------------------------------------------------------------+
|              HARD LINKS vs SYMBOLIC LINKS                         |
+------------------------------------------------------------------+
|                                                                   |
|   Aspekt              Hard Link           Symbolic Link           |
|   ----------------------------------------------------------------|
|   Inode               Samma som mål       Egen inode              |
|   Korsning filsystem  Nej                 Ja                      |
|   Länka kataloger     Nej (farligt)       Ja                      |
|   Mål raderas         Data kvar           Broken link             |
|   Relativa sökvägar   N/A                 Ja                      |
|   Identifiering       ls -i (samma nr)    ls -l (-> visas)       |
|   Storlek             0 (bara entry)      Sökvägslängd            |
|                                                                   |
+------------------------------------------------------------------+
```

Inode exhaustion uppstår när filsystemet har slut på lediga inodes, även om det finns ledigt diskutrymme. Detta händer typiskt med många små filer (sessions, cache, temp-filer).

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Analysera inodes**

```bash
# Visa inode-nummer för filer
ls -i /etc/passwd
# 1234567 /etc/passwd

# Detaljerad inode-information
stat /etc/passwd
# File: /etc/passwd
# Size: 2847      Blocks: 8      IO Block: 4096   regular file
# Device: 801h/2049d  Inode: 1234567    Links: 1
# Access: (0644/-rw-r--r--)  Uid: ( 0/ root)  Gid: ( 0/ root)
# Access: 2024-01-15 10:30:00
# Modify: 2024-01-10 14:20:00
# Change: 2024-01-10 14:20:00

# Visa filsystemets inode-användning
df -i
# Filesystem      Inodes   IUsed   IFree IUse% Mounted on
# /dev/sda1     6553600 1234567 5319033   19% /

# Visa inodes per katalog
find /var -xdev -printf '%h\n' | sort | uniq -c | sort -rn | head -20
```

**Steg 2: Arbeta med hard links**

```bash
# Skapa en fil
echo "Important data" > original.txt

# Skapa hard link
ln original.txt hardlink.txt

# Verifiera samma inode
ls -li original.txt hardlink.txt
# 2847593 -rw-r--r-- 2 user user 15 Jan 15 10:00 original.txt
# 2847593 -rw-r--r-- 2 user user 15 Jan 15 10:00 hardlink.txt
#         Link count: 2

# Ändring syns i båda (samma data!)
echo "More data" >> original.txt
cat hardlink.txt
# Important data
# More data

# Radera original - data finns kvar!
rm original.txt
cat hardlink.txt  # Fungerar fortfarande!
# Important data
# More data

# Hitta alla hard links till en inode
find / -inum 2847593 2>/dev/null
```

**Steg 3: Arbeta med symbolic links**

```bash
# Skapa symlink
ln -s /var/log/syslog mylog

# Visa symlink
ls -la mylog
# lrwxrwxrwx 1 user user 15 Jan 15 mylog -> /var/log/syslog

# Symlink till katalog
ln -s /var/www/html/v2.0.0 /var/www/html/current

# Relativ symlink (rekommenderas för portabilitet)
cd /var/www/html
ln -s ../releases/v2.0.0 current

# Visa vart symlink pekar
readlink current
# ../releases/v2.0.0

# Fullständig upplöst sökväg
readlink -f current
# /var/www/releases/v2.0.0

# Skapa symlink med force (ersätt befintlig)
ln -sf /new/target mylink

# Atomisk symlink-switch (för deployments)
ln -sfn /app/releases/v2.1.0 /app/current
# -s = symbolic
# -f = force (överskriv)
# -n = no-dereference (behandla symlink som fil, inte mål)
```

**Steg 4: Hantera broken symlinks**

```bash
# Hitta alla broken symlinks
find /var/www -xtype l

# Hitta och visa vart de pekar
find /var/www -xtype l -exec ls -la {} \;

# Radera alla broken symlinks (försiktigt!)
find /var/www -xtype l -delete

# Kontrollera om symlink är broken
if [ ! -e /app/current ]; then
    echo "Symlink is broken!"
fi
```

**Steg 5: Diagnostisera inode exhaustion**

```bash
# Kontrollera inode-användning
df -i /

# Om IUse% är 100% men df visar ledigt utrymme:

# Hitta kataloger med flest filer
find / -xdev -type f -printf '%h\n' 2>/dev/null | \
    sort | uniq -c | sort -rn | head -20

# Typiska syndare
find /tmp -type f | wc -l
find /var/spool -type f | wc -l
find /var/cache -type f | wc -l

# Rensa gamla session-filer
find /var/lib/php/sessions -type f -mtime +7 -delete

# Rensa gamla temp-filer
find /tmp -type f -atime +3 -delete
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Zero-Downtime Deployment med Symlinks**

```bash
#!/bin/bash
# deploy.sh - Atomic deployment using symlinks

APP_NAME="myapp"
RELEASES_DIR="/var/www/$APP_NAME/releases"
CURRENT_LINK="/var/www/$APP_NAME/current"
SHARED_DIR="/var/www/$APP_NAME/shared"

VERSION=$1
RELEASE_DIR="$RELEASES_DIR/$VERSION"

echo "Deploying $APP_NAME version $VERSION..."

# 1. Skapa release-katalog
mkdir -p "$RELEASE_DIR"

# 2. Extrahera eller klona kod
tar -xzf "/tmp/$APP_NAME-$VERSION.tar.gz" -C "$RELEASE_DIR"

# 3. Länka delade resurser (uploads, logs, etc.)
ln -sfn "$SHARED_DIR/uploads" "$RELEASE_DIR/uploads"
ln -sfn "$SHARED_DIR/logs" "$RELEASE_DIR/logs"
ln -sfn "$SHARED_DIR/.env" "$RELEASE_DIR/.env"

# 4. Sätt permissions
chown -R www-data:www-data "$RELEASE_DIR"

# 5. ATOMISK SWITCH - detta är nyckeln!
ln -sfn "$RELEASE_DIR" "$CURRENT_LINK"

echo "Deployment complete!"
echo "Active: $(readlink -f $CURRENT_LINK)"

# Struktur efter deploy:
# /var/www/myapp/
# ├── current -> releases/v2.1.0
# ├── releases/
# │   ├── v2.0.0/
# │   └── v2.1.0/
# └── shared/
#     ├── uploads/
#     ├── logs/
#     └── .env
```

**Exempel 2: Rollback Script**

```bash
#!/bin/bash
# rollback.sh - Quick rollback to previous version

RELEASES_DIR="/var/www/myapp/releases"
CURRENT_LINK="/var/www/myapp/current"

# Hitta nuvarande version
CURRENT_VERSION=$(basename $(readlink -f $CURRENT_LINK))

# Lista alla versioner, sorterade
VERSIONS=($(ls -t $RELEASES_DIR))

# Hitta föregående version
PREV_VERSION=""
for i in "${!VERSIONS[@]}"; do
    if [ "${VERSIONS[$i]}" = "$CURRENT_VERSION" ]; then
        PREV_VERSION="${VERSIONS[$((i+1))]}"
        break
    fi
done

if [ -z "$PREV_VERSION" ]; then
    echo "No previous version found!"
    exit 1
fi

echo "Rolling back from $CURRENT_VERSION to $PREV_VERSION..."

# Atomisk rollback
ln -sfn "$RELEASES_DIR/$PREV_VERSION" "$CURRENT_LINK"

echo "Rollback complete!"
echo "Active: $(readlink -f $CURRENT_LINK)"
```

**Exempel 3: Inode Monitoring Script**

```bash
#!/bin/bash
# check_inodes.sh - Monitor inode usage

THRESHOLD=80
ALERT_EMAIL="admin@example.com"

check_inodes() {
    df -i | tail -n +2 | while read line; do
        filesystem=$(echo $line | awk '{print $1}')
        iuse=$(echo $line | awk '{print $5}' | tr -d '%')
        mount=$(echo $line | awk '{print $6}')

        if [ "$iuse" -ge "$THRESHOLD" ]; then
            echo "WARNING: $mount is ${iuse}% inodes used"

            # Hitta top directories
            echo "Top directories by file count:"
            find "$mount" -xdev -type f -printf '%h\n' 2>/dev/null | \
                sort | uniq -c | sort -rn | head -10
        fi
    done
}

result=$(check_inodes)
if [ -n "$result" ]; then
    echo "$result"
    # Skicka alert
    # echo "$result" | mail -s "Inode Warning" $ALERT_EMAIL
fi
```

**Exempel 4: Hard Links för Backup-deduplicering**

```bash
#!/bin/bash
# incremental_backup.sh - Använd hard links för space-efficient backups

BACKUP_BASE="/backup"
SOURCE="/var/www/app"
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -d 'yesterday' +%Y-%m-%d)

BACKUP_TODAY="$BACKUP_BASE/$TODAY"
BACKUP_YESTERDAY="$BACKUP_BASE/$YESTERDAY"

if [ -d "$BACKUP_YESTERDAY" ]; then
    echo "Creating incremental backup with hard links..."

    # Kopiera med hard links för oförändrade filer
    cp -al "$BACKUP_YESTERDAY" "$BACKUP_TODAY"

    # Synka ändringar (ersätter modifierade filer)
    rsync -a --delete "$SOURCE/" "$BACKUP_TODAY/"
else
    echo "Creating full backup..."
    rsync -a "$SOURCE/" "$BACKUP_TODAY/"
fi

# Resultat: oförändrade filer delar inodes = minimal extra diskplats
du -sh "$BACKUP_BASE"/*
```

------------------------------------------------------------

## Bästa Praxis

**Använd relativa symlinks för portabilitet**
Relativa symlinks (`ln -s ../releases/v2 current`) fungerar även om parent-katalogen flyttas.

**Atomisk symlink-switch för deployments**
`ln -sfn` är atomisk operation - request routas alltid till en komplett version.

**Behåll N senaste releases**
Ta inte bort gamla releases direkt. Behåll minst 3-5 för snabb rollback.

**Monitorera inode-användning**
Lägg till inode-checks i monitoring. 90% är varning, 95% är kritiskt.

**Undvik hard links för kataloger**
Hard links för kataloger kan skapa filesystem-loopar. Använd symlinks istället.

**Dokumentera symlink-struktur**
Håll koll på vilka symlinks som finns och vart de pekar, särskilt i produktionsmiljöer.

------------------------------------------------------------

## Vanliga Fallgropar

**Broken symlinks efter radering**
Om målet raderas blir symlinken "broken". Testa alltid med `[ -e link ]` inte `[ -L link ]`.

**Relativa symlinks i fel katalog**
En relativ symlink skapas relativt till var symlinken ligger, inte pwd.

**Glömma -n flaggan vid symlink-switch**
Utan `-n` kan `ln -sf` skapa symlink inuti målet istället för att ersätta.

**Inode exhaustion på /var**
Många applikationer skapar små filer i /var (sessions, cache). Övervaka och rensa regelbundet.

**Permissions på symlinks**
Symlink-permissions (lrwxrwxrwx) är irrelevanta - det är målets permissions som gäller.

------------------------------------------------------------

## Övningar

### Övning 1: Förstå Inodes
<details>
<summary>Visa övning</summary>

**Uppgift:** Utforska hur inodes fungerar och demonstrera skillnaden mellan filnamn och inode.

**Steg:**
1. Skapa en fil och notera dess inode
2. Skapa hard link och verifiera samma inode
3. Skapa symlink och verifiera olika inode
4. Radera originalfilen och testa åtkomst via båda länktyper

**Lösning:**
```bash
# Skapa testmiljö
mkdir -p /tmp/inode-lab && cd /tmp/inode-lab

# Skapa original
echo "Original content" > original.txt

# Visa inode
ls -li original.txt
stat original.txt

# Skapa hard link
ln original.txt hardlink.txt

# Skapa symlink
ln -s original.txt symlink.txt

# Jämför inodes
echo "=== Inode comparison ==="
ls -li original.txt hardlink.txt symlink.txt
# original och hardlink har SAMMA inode-nummer
# symlink har EGET inode-nummer

# Radera original
rm original.txt

# Testa åtkomst
echo "=== After removing original ==="
cat hardlink.txt   # FUNGERAR - data finns kvar
cat symlink.txt    # FEL - broken link

# Visa broken symlink
ls -la symlink.txt
# symlink.txt -> original.txt (röd/blinkande i terminal)

# Cleanup
cd && rm -rf /tmp/inode-lab
```
</details>

### Övning 2: Zero-Downtime Deployment
<details>
<summary>Visa övning</summary>

**Uppgift:** Implementera en komplett deployment-struktur med atomic symlink switching.

**Steg:**
1. Skapa katalogstruktur för releases och shared
2. Simulera två versioner
3. Implementera atomic switch
4. Verifiera att switch är sömlös

**Lösning:**
```bash
# Skapa deployment-struktur
mkdir -p /tmp/deploy/{releases,shared}
cd /tmp/deploy

# Skapa shared resources
mkdir -p shared/{uploads,logs}
echo "DB_HOST=localhost" > shared/.env

# Simulera version 1.0
mkdir -p releases/v1.0.0
echo "App version 1.0" > releases/v1.0.0/index.html
ln -s ../../shared/uploads releases/v1.0.0/uploads
ln -s ../../shared/.env releases/v1.0.0/.env

# Skapa initial current symlink
ln -sfn releases/v1.0.0 current

# Verifiera
echo "=== Version 1.0 deployed ==="
cat current/index.html
readlink -f current

# Simulera version 2.0
mkdir -p releases/v2.0.0
echo "App version 2.0 - New features!" > releases/v2.0.0/index.html
ln -s ../../shared/uploads releases/v2.0.0/uploads
ln -s ../../shared/.env releases/v2.0.0/.env

# ATOMIC SWITCH
echo "=== Performing atomic switch ==="
ln -sfn releases/v2.0.0 current

# Verifiera
cat current/index.html
readlink -f current

# Rollback
echo "=== Rolling back ==="
ln -sfn releases/v1.0.0 current
cat current/index.html

# Visa struktur
echo "=== Final structure ==="
find . -maxdepth 3 -ls

# Cleanup
cd && rm -rf /tmp/deploy
```
</details>

### Övning 3: Inode Exhaustion Simulation
<details>
<summary>Visa övning</summary>

**Uppgift:** Simulera och diagnostisera inode exhaustion scenario.

**Steg:**
1. Skapa många små filer
2. Övervaka inode-användning
3. Identifiera problemkatalog
4. Rensa och verifiera

**Lösning:**
```bash
# Skapa testmiljö
mkdir -p /tmp/inode-test && cd /tmp/inode-test

# Visa baseline inode-användning
echo "=== Baseline ==="
df -i /tmp

# Skapa många små filer (simulerar sessions, cache, etc.)
echo "Creating 10000 small files..."
mkdir -p sessions
for i in $(seq 1 10000); do
    echo "session data" > sessions/sess_$i
done

# Visa påverkan på inodes
echo "=== After creating files ==="
df -i /tmp

# Diagnostisera - hitta katalog med flest filer
echo "=== Top directories by file count ==="
find /tmp/inode-test -type f -printf '%h\n' | sort | uniq -c | sort -rn | head

# Analysera filernas ålder
echo "=== Files older than 1 minute ==="
find /tmp/inode-test/sessions -type f -mmin +1 | wc -l

# Rensa gamla filer
echo "=== Cleaning old files ==="
find /tmp/inode-test/sessions -type f -mmin +1 -delete

# Verifiera
echo "=== After cleanup ==="
df -i /tmp
find /tmp/inode-test -type f | wc -l

# Cleanup
cd && rm -rf /tmp/inode-test
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- File Permissions - förståelse för åtkomsträttigheter
- Filesystem Hierarchy Standard - katalogstruktur

**Relaterade noder:**
- Disk Management - partitionering och LVM
- Process Lifecycle - processer som håller filer öppna

**Kommande noder:**
- Backup Strategies - hard links för inkrementella backups
- Container Storage - volume mounts och bind mounts

------------------------------------------------------------

## Sammanfattning

Inodes är datastrukturer som lagrar all metadata om filer utom filnamnet. Filnamn är bara etiketter (directory entries) som pekar på inodes. Detta möjliggör hard links - flera namn som delar samma inode och data.

Hard links skapas med `ln`, delar inode med målet, och data finns kvar tills alla links är borta. De fungerar endast inom samma filsystem och kan inte länka kataloger.

Symbolic links (symlinks) skapas med `ln -s`, har egen inode och innehåller en sökväg. De kan korsa filsystem och länka kataloger, men blir "broken" om målet raderas.

För DevOps är symlinks kritiska för zero-downtime deployments. Tekniken `ln -sfn new_version current` utför atomisk version-switch. Inode exhaustion uppstår när filsystemet har slut på inodes trots ledigt utrymme - vanligt med många små filer.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ls -i` | Visa inode-nummer |
| `stat file` | Visa all inode-metadata |
| `df -i` | Visa filsystems inode-användning |
| `ln file link` | Skapa hard link |
| `ln -s target link` | Skapa symbolic link |
| `ln -sfn target link` | Atomic symlink switch |
| `readlink link` | Visa symlink-mål |
| `readlink -f link` | Visa fullständigt upplöst mål |
| `find -xtype l` | Hitta broken symlinks |
| `find -inum N` | Hitta alla hard links till inode N |

------------------------------------------------------------

## Referenser

- Linux man pages: ln(1), stat(1), readlink(1)
- Linux Documentation Project - Inodes
- Capistrano Deployment Strategy Documentation
- "The Linux Programming Interface" - Kerrisk (Chapter 18)
- ext4 Filesystem Documentation
""",
        },
        {
            "title": 'Disk Management',
            "slug": 'disk-management',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Disk Management

------------------------------------------------------------

## Introduktion

Diskhantering är en kritisk kompetens för DevOps-ingenjörer. När disken blir full stannar databaser, loggar slutar skrivas, och applikationer kraschar. Denna modul lär dig att diagnostisera diskproblem, hantera partitioner, arbeta med LVM för flexibel volymhantering, och förstå grunderna i RAID. Du får praktiska verktyg för både akut felsökning och proaktiv kapacitetsplanering.

------------------------------------------------------------

## Teori

Linux hanterar diskar genom en hierarkisk struktur: fysiska diskar delas upp i partitioner, som formateras med filsystem och monteras i katalogträdet. Moderna system använder ofta LVM (Logical Volume Manager) som lägger till ett abstraktionslager för flexibilitet.

```
+------------------------------------------------------------------+
|                    DISK STORAGE HIERARCHY                         |
+------------------------------------------------------------------+
|                                                                   |
|   Physical Disk (/dev/sda)                                       |
|   +----------------------------------------------------------+   |
|   |  Partition Table (GPT/MBR)                               |   |
|   +----------------------------------------------------------+   |
|   |                                                          |   |
|   |  sda1        sda2           sda3                        |   |
|   |  [EFI]       [Boot]         [LVM PV]                    |   |
|   |  512MB       1GB            Rest                        |   |
|   |                                                          |   |
|   +----------------------------------------------------------+   |
|                                    |                              |
|                                    v                              |
|   +----------------------------------------------------------+   |
|   |  LVM Layer                                               |   |
|   |  +------------------------+                              |   |
|   |  | Volume Group: vg-data |                              |   |
|   |  +------------------------+                              |   |
|   |  |                        |                              |   |
|   |  | lv-root    lv-var     |                              |   |
|   |  | 50GB       100GB      |                              |   |
|   |  |                        |                              |   |
|   |  +------------------------+                              |   |
|   +----------------------------------------------------------+   |
|                     |               |                             |
|                     v               v                             |
|   +----------------------------------------------------------+   |
|   |  Filesystems                                             |   |
|   |  ext4:/        ext4:/var                                 |   |
|   +----------------------------------------------------------+   |
|                                                                   |
+------------------------------------------------------------------+
```

LVM introducerar tre koncept: Physical Volumes (PV) är partitioner eller hela diskar tillägnade LVM, Volume Groups (VG) pooler ihop flera PV, och Logical Volumes (LV) är flexibla "partitioner" som kan växa och krympa.

```
+------------------------------------------------------------------+
|                    LVM ARCHITECTURE                               |
+------------------------------------------------------------------+
|                                                                   |
|   Physical Volumes (PV)                                          |
|   +------------+  +------------+  +------------+                  |
|   | /dev/sda3  |  | /dev/sdb1  |  | /dev/sdc1  |                  |
|   | 100GB      |  | 200GB      |  | 200GB      |                  |
|   +------------+  +------------+  +------------+                  |
|         |               |               |                         |
|         +---------------+---------------+                         |
|                         |                                         |
|                         v                                         |
|   Volume Group (VG)                                              |
|   +------------------------------------------------+             |
|   |              vg-production                     |             |
|   |              Total: 500GB                      |             |
|   +------------------------------------------------+             |
|         |               |               |                         |
|         v               v               v                         |
|   Logical Volumes (LV)                                           |
|   +------------+  +------------+  +------------+                  |
|   | lv-root    |  | lv-var     |  | lv-data    |                  |
|   | 50GB       |  | 150GB      |  | 250GB      |                  |
|   | ext4       |  | ext4       |  | xfs        |                  |
|   | mounted /  |  | mounted    |  | mounted    |                  |
|   |            |  | /var       |  | /data      |                  |
|   +------------+  +------------+  +------------+                  |
|                                                                   |
+------------------------------------------------------------------+
```

RAID (Redundant Array of Independent Disks) kombinerar flera diskar för prestanda och/eller redundans. De vanligaste nivåerna är RAID 0 (striping, ingen redundans), RAID 1 (mirroring), RAID 5 (striping med paritet), och RAID 10 (kombinerad mirroring och striping).

```
+------------------------------------------------------------------+
|                    COMMON RAID LEVELS                             |
+------------------------------------------------------------------+
|                                                                   |
|   RAID 0 - Striping (Performance)                                |
|   +-------+  +-------+                                            |
|   | Disk1 |  | Disk2 |   Data: A B C D E F                       |
|   | A C E |  | B D F |   Kapacitet: 100%                         |
|   +-------+  +-------+   Redundans: Ingen                         |
|                                                                   |
|   RAID 1 - Mirroring (Redundancy)                                |
|   +-------+  +-------+                                            |
|   | Disk1 |  | Disk2 |   Data: A B C                             |
|   | A B C |  | A B C |   Kapacitet: 50%                          |
|   +-------+  +-------+   Redundans: 1 disk kan gå                |
|                                                                   |
|   RAID 5 - Striping with Parity                                  |
|   +-------+  +-------+  +-------+                                 |
|   | Disk1 |  | Disk2 |  | Disk3 |  Data: A B C D                 |
|   | A  D  |  | B  P1 |  | C  P2 |  Kapacitet: 66%               |
|   +-------+  +-------+  +-------+  Redundans: 1 disk kan gå     |
|                                                                   |
|   RAID 10 - Mirrored Stripes                                     |
|   +-------+  +-------+  +-------+  +-------+                      |
|   | D1    |  | D2    |  | D3    |  | D4    |                      |
|   | A  C  |  | A  C  |  | B  D  |  | B  D  |                      |
|   +-------+  +-------+  +-------+  +-------+                      |
|   Kapacitet: 50%, Redundans: 1 per mirror-par                    |
|                                                                   |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Analysera diskutrymme**

```bash
# Översikt av alla filsystem
df -h
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1        50G   35G   13G  73% /
# /dev/sdb1       100G   80G   15G  85% /data

# Specifik katalog
df -h /var/log

# Inode-användning (kan vara fullt trots ledigt utrymme)
df -i

# Visa blockenheter och deras mount points
lsblk
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   100G  0 disk
# ├─sda1   8:1    0   512M  0 part /boot/efi
# └─sda2   8:2    0  99.5G  0 part /

# Mer detaljer med filsystemstyp
lsblk -f
```

**Steg 2: Hitta vad som tar plats**

```bash
# Storlek på specifik katalog
du -sh /var/log
# 2.5G    /var/log

# Storleken på varje underkatalog
du -sh /var/log/*

# Hitta de största katalogerna i systemet
du -sh /* 2>/dev/null | sort -rh | head -10

# Hitta stora filer (>100MB)
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null

# ncdu - interaktivt verktyg (installera först)
sudo apt install ncdu
ncdu /var
```

**Steg 3: Rensa diskutrymme**

```bash
# Rensa systemloggar (behåll 7 dagar)
sudo journalctl --vacuum-time=7d

# Rensa apt cache
sudo apt clean
sudo apt autoremove

# Radera gamla komprimerade loggar
sudo find /var/log -name "*.gz" -mtime +30 -delete

# Hitta och radera core dumps
sudo find / -name "core.*" -type f -delete 2>/dev/null

# Rensa /tmp (försiktigt!)
sudo find /tmp -type f -atime +7 -delete
```

**Steg 4: Partitionera ny disk**

```bash
# Lista alla diskar
sudo fdisk -l

# Starta partitionering (interaktivt)
sudo fdisk /dev/sdb

# fdisk kommandon:
# g = skapa ny GPT-tabell
# n = ny partition
# t = ändra typ (8e för LVM)
# w = skriv och avsluta

# Alternativt med parted (stöder GPT bättre)
sudo parted /dev/sdb
# (parted) mklabel gpt
# (parted) mkpart primary ext4 0% 100%
# (parted) quit

# Formatera partitionen
sudo mkfs.ext4 /dev/sdb1

# Eller för XFS (rekommenderat för stora volymer)
sudo mkfs.xfs /dev/sdb1
```

**Steg 5: LVM-hantering**

```bash
# Visa nuvarande LVM-struktur
sudo pvs  # Physical Volumes
sudo vgs  # Volume Groups
sudo lvs  # Logical Volumes

# Skapa LVM från ny disk
sudo pvcreate /dev/sdb1
sudo vgcreate vg-data /dev/sdb1
sudo lvcreate -n lv-app -L 50G vg-data

# Formatera och montera
sudo mkfs.ext4 /dev/vg-data/lv-app
sudo mkdir /app
sudo mount /dev/vg-data/lv-app /app

# UTÖKA befintlig LVM-volym
# 1. Lägg till ny PV till VG
sudo pvcreate /dev/sdc1
sudo vgextend vg-data /dev/sdc1

# 2. Utöka LV
sudo lvextend -L +100G /dev/vg-data/lv-app
# Eller använd all tillgänglig plats:
sudo lvextend -l +100%FREE /dev/vg-data/lv-app

# 3. Utöka filsystemet
sudo resize2fs /dev/vg-data/lv-app  # För ext4
# eller
sudo xfs_growfs /app  # För XFS (använder mount point)
```

**Steg 6: Permanent mount via fstab**

```bash
# Hitta UUID
sudo blkid /dev/vg-data/lv-app
# /dev/vg-data/lv-app: UUID="abc123..."

# Lägg till i fstab
echo 'UUID=abc123... /app ext4 defaults 0 2' | sudo tee -a /etc/fstab

# Testa (montera allt i fstab)
sudo mount -a

# Verifiera
df -h /app
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Emergency Disk Cleanup**

```bash
#!/bin/bash
# emergency-cleanup.sh - Frigör diskutrymme snabbt

set -e

echo "=== Disk Status Before ==="
df -h /

echo "=== Cleaning package cache ==="
sudo apt clean
sudo apt autoremove -y

echo "=== Cleaning old journals ==="
sudo journalctl --vacuum-time=3d

echo "=== Removing old kernels ==="
sudo apt autoremove --purge -y

echo "=== Cleaning /tmp ==="
sudo find /tmp -type f -atime +3 -delete

echo "=== Cleaning old logs ==="
sudo find /var/log -name "*.gz" -delete
sudo find /var/log -name "*.old" -delete

echo "=== Disk Status After ==="
df -h /

echo "=== Top space consumers ==="
sudo du -sh /var/* 2>/dev/null | sort -rh | head -10
```

**Exempel 2: LVM Expansion Script**

```bash
#!/bin/bash
# expand-lv.sh - Utöka LVM-volym

LV_PATH="${1:-/dev/vg-data/lv-app}"
SIZE="${2:-+50G}"

if [ ! -e "$LV_PATH" ]; then
    echo "Error: $LV_PATH does not exist"
    exit 1
fi

# Visa nuvarande storlek
echo "Current size:"
sudo lvs "$LV_PATH"

# Utöka LV
echo "Extending by $SIZE..."
sudo lvextend -L "$SIZE" "$LV_PATH"

# Bestäm filsystemstyp
FSTYPE=$(sudo blkid -o value -s TYPE "$LV_PATH")

# Utöka filsystem
echo "Resizing filesystem ($FSTYPE)..."
case $FSTYPE in
    ext4|ext3|ext2)
        sudo resize2fs "$LV_PATH"
        ;;
    xfs)
        MOUNT_POINT=$(findmnt -n -o TARGET "$LV_PATH")
        sudo xfs_growfs "$MOUNT_POINT"
        ;;
    *)
        echo "Unknown filesystem: $FSTYPE"
        exit 1
        ;;
esac

echo "New size:"
sudo lvs "$LV_PATH"
df -h $(findmnt -n -o TARGET "$LV_PATH")
```

**Exempel 3: Disk Monitoring Script**

```bash
#!/bin/bash
# disk-monitor.sh - Övervaka diskutrymme

THRESHOLD=80
ALERT_EMAIL="admin@example.com"

check_disk() {
    df -h | tail -n +2 | while read line; do
        usage=$(echo "$line" | awk '{print $5}' | tr -d '%')
        mount=$(echo "$line" | awk '{print $6}')

        if [ "$usage" -ge "$THRESHOLD" ]; then
            echo "WARNING: $mount is ${usage}% full"

            # Visa vad som tar plats
            echo "Top consumers in $mount:"
            du -sh "$mount"/* 2>/dev/null | sort -rh | head -5
            echo "---"
        fi
    done
}

result=$(check_disk)
if [ -n "$result" ]; then
    echo "$result"
    # Skicka email
    # echo "$result" | mail -s "Disk Warning" $ALERT_EMAIL
fi
```

**Exempel 4: Setup RAID 1 med mdadm**

```bash
#!/bin/bash
# setup-raid1.sh - Skapa RAID 1 mirror

# Installera mdadm
sudo apt install mdadm -y

# Skapa RAID 1 array
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1

# Vänta på sync
cat /proc/mdstat

# Skapa filsystem
sudo mkfs.ext4 /dev/md0

# Montera
sudo mkdir /data
sudo mount /dev/md0 /data

# Spara RAID-konfiguration
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf

# Uppdatera initramfs
sudo update-initramfs -u

# Lägg till i fstab
echo '/dev/md0 /data ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

------------------------------------------------------------

## Bästa Praxis

**Monitorera proaktivt**
Sätt upp alerts vid 80% användning, inte 95%. Diskar som närmar sig 100% orsakar svårlösta problem.

**Använd LVM för flexibilitet**
LVM låter dig utöka volymer utan nertid. Standardinstallationer bör använda LVM.

**Separera system och data**
Ha /var och /home på separata volymer så att en fullskriven logg inte kraschar systemet.

**UUID i fstab istället för device names**
Device names (/dev/sdb1) kan ändras mellan omstarter. UUID är stabila.

**Testa fstab före reboot**
Kör alltid `mount -a` efter fstab-ändringar. Felaktig fstab kan förhindra boot.

**Dokumentera LVM-struktur**
Spara output från pvs, vgs, lvs. Vid recovery behöver du veta hur det såg ut.

------------------------------------------------------------

## Vanliga Fallgropar

**Ignorera /var/log tillväxt**
Loggar kan växa obegränsat. Konfigurera logrotate och max-storlek.

**Glömma resize2fs efter lvextend**
LV:n är större men filsystemet ser inte det. Alltid resize2fs (ext4) eller xfs_growfs (xfs) efter.

**Formatera fel disk**
Dubbelkolla ALLTID med lsblk innan mkfs. Det finns ingen undo.

**Radera filer som fortfarande är öppna**
Diskutrymme frigörs inte förrän processen stänger filen. Använd lsof för att hitta öppna filer.

**Missa inode exhaustion**
df visar ledigt utrymme men du kan inte skapa filer. Kolla df -i.

------------------------------------------------------------

## Övningar

### Övning 1: Disk Audit
<details>
<summary>Visa övning</summary>

**Uppgift:** Genomför en komplett disk-audit av systemet.

**Steg:**
1. Analysera diskutrymme per filsystem
2. Hitta de 10 största katalogerna
3. Hitta filer större än 100MB
4. Kontrollera inode-användning
5. Dokumentera fynd och rekommendationer

**Lösning:**
```bash
#!/bin/bash
# disk-audit.sh

echo "=== DISK AUDIT REPORT ==="
echo "Date: $(date)"
echo ""

echo "=== 1. Filesystem Usage ==="
df -h

echo ""
echo "=== 2. Inode Usage ==="
df -i

echo ""
echo "=== 3. Top 10 Largest Directories ==="
du -sh /* 2>/dev/null | sort -rh | head -10

echo ""
echo "=== 4. Files Larger Than 100MB ==="
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | head -20

echo ""
echo "=== 5. Old Log Files (>30 days) ==="
find /var/log -name "*.gz" -mtime +30 -exec ls -lh {} \; 2>/dev/null

echo ""
echo "=== 6. Temporary Files ==="
du -sh /tmp /var/tmp 2>/dev/null

echo ""
echo "=== 7. Package Cache ==="
du -sh /var/cache/apt 2>/dev/null

echo ""
echo "=== RECOMMENDATIONS ==="
echo "1. Review large files and directories"
echo "2. Clean old logs: journalctl --vacuum-time=7d"
echo "3. Clean package cache: apt clean"
```
</details>

### Övning 2: LVM Expansion
<details>
<summary>Visa övning</summary>

**Uppgift:** Simulera att utöka en LVM-volym med en ny disk.

**Scenario:** /data volymen är 80% full. Du har lagt till en ny 100GB disk (/dev/sdc).

**Steg:**
1. Verifiera nuvarande LVM-struktur
2. Partitionera ny disk för LVM
3. Skapa PV och lägg till i VG
4. Utöka LV och filsystem
5. Verifiera att kapaciteten ökade

**Lösning:**
```bash
# 1. Verifiera nuvarande struktur
sudo pvs
sudo vgs
sudo lvs
df -h /data

# 2. Partitionera ny disk
sudo fdisk /dev/sdc
# g (GPT), n (new), default values, t (type), 8e (LVM), w (write)

# 3. Skapa PV och utöka VG
sudo pvcreate /dev/sdc1
sudo vgextend vg-data /dev/sdc1

# Verifiera VG utökats
sudo vgs

# 4. Utöka LV med all ny plats
sudo lvextend -l +100%FREE /dev/vg-data/lv-data

# Utöka filsystem
sudo resize2fs /dev/vg-data/lv-data  # ext4
# eller
sudo xfs_growfs /data  # xfs

# 5. Verifiera
df -h /data
sudo lvs
```
</details>

### Övning 3: Disk Emergency Response
<details>
<summary>Visa övning</summary>

**Uppgift:** Praktisera emergency response när disk är 95% full.

**Scenario:** Produktion-servern larmar om 95% disk. Hitta och åtgärda orsaken snabbt.

**Steg:**
1. Identifiera vilket filsystem som är fullt
2. Hitta vad som tar mest plats
3. Genomför säker cleanup
4. Implementera förebyggande åtgärd

**Lösning:**
```bash
#!/bin/bash
# emergency-response.sh

echo "=== STEP 1: Identify Full Filesystem ==="
df -h | grep -E '9[0-9]%|100%'

echo ""
echo "=== STEP 2: Find Space Consumers ==="
# Antag / är problemet
echo "Top directories in /var:"
du -sh /var/* 2>/dev/null | sort -rh | head -5

echo ""
echo "Large files in /var/log:"
find /var/log -type f -size +50M -exec ls -lh {} \;

echo ""
echo "=== STEP 3: Safe Cleanup ==="

# Rensa loggar (säkert)
echo "Cleaning journals..."
sudo journalctl --vacuum-size=500M

echo "Cleaning old compressed logs..."
sudo find /var/log -name "*.gz" -mtime +7 -delete

echo "Cleaning apt cache..."
sudo apt clean

echo ""
echo "=== STEP 4: Verify ==="
df -h /

echo ""
echo "=== STEP 5: Prevention ==="
echo "Add to crontab for weekly cleanup:"
echo "0 2 * * 0 /usr/local/bin/disk-cleanup.sh"
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Filesystem Hierarchy Standard - förståelse för katalogstruktur
- Mount Points och Device Files - montering av diskar

**Relaterade noder:**
- Inodes, Hard Links och Symbolic Links - inode exhaustion
- Process Lifecycle - processer som håller filer öppna

**Kommande noder:**
- Backup Strategies - backup av volymer
- Cloud Storage - AWS EBS, Azure Disks

------------------------------------------------------------

## Sammanfattning

Diskhantering omfattar diagnostik med df och du, partitionering med fdisk eller parted, och flexibel volymhantering med LVM. LVM:s tre lager (PV, VG, LV) möjliggör online-expansion av volymer utan nertid.

För akut felsökning: använd df -h för översikt, du -sh för att hitta vad som tar plats, och journalctl --vacuum samt apt clean för snabb cleanup. Kontrollera alltid df -i för inode exhaustion.

Best practices inkluderar proaktiv monitoring vid 80% användning, separata volymer för system och data, UUID i fstab, och regelbunden log rotation. RAID ger redundans men ersätter inte backup.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `df -h` | Visa diskutrymme per filsystem |
| `df -i` | Visa inode-användning |
| `du -sh /path` | Storlek på katalog |
| `du -sh /* | sort -rh` | Största katalogerna |
| `lsblk` | Lista blockenheter |
| `fdisk /dev/sdb` | Partitionera disk |
| `mkfs.ext4 /dev/sdb1` | Skapa ext4-filsystem |
| `pvs/vgs/lvs` | Visa LVM-struktur |
| `pvcreate /dev/sdb1` | Skapa Physical Volume |
| `vgextend vg /dev/sdb1` | Lägg till PV i VG |
| `lvextend -L +50G /dev/vg/lv` | Utöka Logical Volume |
| `resize2fs /dev/vg/lv` | Utöka ext4-filsystem |
| `xfs_growfs /mount` | Utöka XFS-filsystem |

------------------------------------------------------------

## Referenser

- Linux man pages: df(1), du(1), fdisk(8), lvm(8)
- Red Hat LVM Administration Guide
- Linux Documentation Project - Disk Management
- Ubuntu Server Guide - Storage
- mdadm Documentation - RAID Administration
""",
        },
        {
            "title": 'Process Lifecycle and States',
            "slug": 'process-lifecycle',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Process Lifecycle and States

------------------------------------------------------------

## Introduktion

Processer är fundamentet för allt som körs i Linux - från din terminal till webbservrar och databaser. För DevOps-ingenjörer är förståelse för processlivscykeln avgörande för felsökning av hängda tjänster, identifiering av zombie-processer, och optimering av systemresurser. Denna modul ger dig djup kunskap om hur processer skapas, lever, och dör i Linux-kärnan.

------------------------------------------------------------

## Teori

En process är en körande instans av ett program. Linux-kärnan tilldelar varje process ett unikt Process ID (PID) och håller reda på dess tillstånd, resurser och relationer till andra processer.

```
+------------------------------------------------------------------+
|                    PROCESS HIERARCHY                              |
+------------------------------------------------------------------+
|                                                                   |
|   systemd (PID 1) ─── Init-processen, "moder" till alla          |
|       │                                                           |
|       ├── sshd ─────────────────── SSH-daemon                    |
|       │    └── sshd ────────────── SSH-session                   |
|       │         └── bash ───────── Ditt shell                    |
|       │              └── vim ───── Din editor                    |
|       │                                                           |
|       ├── nginx ────────────────── Master process                |
|       │    ├── nginx ───────────── Worker 1                      |
|       │    └── nginx ───────────── Worker 2                      |
|       │                                                           |
|       ├── containerd ───────────── Container runtime             |
|       │    └── containerd-shim ─── Container process             |
|       │         └── app ─────────── Din applikation              |
|       │                                                           |
|       └── postgres ─────────────── Databas                       |
|            ├── postgres ─────────── Background writer            |
|            └── postgres ─────────── Autovacuum                   |
|                                                                   |
+------------------------------------------------------------------+
```

Process-skapande sker via fork() och exec() systemanrop. Fork skapar en kopia av föräldraprocessen, och exec ersätter processens minne med ett nytt program.

```
+------------------------------------------------------------------+
|                    PROCESS CREATION (fork/exec)                   |
+------------------------------------------------------------------+
|                                                                   |
|   Bash (PID 1000)                                                |
|        │                                                          |
|        │ fork()                                                   |
|        v                                                          |
|   +----------+    +----------+                                    |
|   | Bash     |    | Bash     |  <- Exakt kopia av förälder       |
|   | PID 1000 |    | PID 2001 |                                    |
|   | (parent) |    | (child)  |                                    |
|   +----------+    +----------+                                    |
|                        │                                          |
|                        │ exec("ls")                               |
|                        v                                          |
|                   +----------+                                    |
|                   | ls       |  <- Nytt program, samma PID       |
|                   | PID 2001 |                                    |
|                   +----------+                                    |
|                        │                                          |
|                        │ exit(0)                                  |
|                        v                                          |
|                   [Zombie state]                                  |
|                        │                                          |
|                        │ wait() av förälder                      |
|                        v                                          |
|                   [Terminated]                                    |
|                                                                   |
+------------------------------------------------------------------+
```

Processtillstånd (STAT) indikerar vad en process gör vid ett givet ögonblick:

```
+------------------------------------------------------------------+
|                    PROCESS STATES                                 |
+------------------------------------------------------------------+
|                                                                   |
|   R (Running)                                                     |
|   +------------+                                                  |
|   | Körs på    |<--------------------------------------------+   |
|   | CPU        |                                             |   |
|   +-----+------+                                             |   |
|         |                                                    |   |
|         | I/O request                                        |   |
|         v                                                    |   |
|   +------------+        +------------+                       |   |
|   | S (Sleep)  |------->| D (Unintr. |                       |   |
|   | Interr.    |        | Sleep)     |                       |   |
|   +-----+------+        +-----+------+                       |   |
|         |                     |                              |   |
|         | Signal/Event        | I/O complete                 |   |
|         +---------------------+------------------------------+   |
|                                                                   |
|   +------------+                                                  |
|   | T (Stopped)|  <-- Ctrl+Z eller SIGSTOP                       |
|   +------------+                                                  |
|         |                                                         |
|         | fg/SIGCONT                                              |
|         v                                                         |
|   [Tillbaka till Running]                                         |
|                                                                   |
|   +------------+                                                  |
|   | Z (Zombie) |  <-- Avslutad, väntar på förälder               |
|   +------------+                                                  |
|                                                                   |
+------------------------------------------------------------------+
```

STAT-kolumnen i ps visar både huvudtillstånd och modifierare:

| Tillstånd | Namn | Beskrivning |
|-----------|------|-------------|
| R | Running | Körs eller redo att köra |
| S | Sleeping (interruptible) | Väntar på event, kan avbrytas |
| D | Sleeping (uninterruptible) | Väntar på I/O, kan EJ avbrytas |
| T | Stopped | Pausad (Ctrl+Z, SIGSTOP) |
| Z | Zombie | Avslutad, väntar på förälder |

| Modifierare | Betydelse |
|-------------|-----------|
| s | Session leader |
| l | Multi-threaded |
| + | Förgrunds-process |
| < | Hög prioritet (nice < 0) |
| N | Låg prioritet (nice > 0) |

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Visa processöversikt**

```bash
# Standardvy av alla processer
ps aux
# USER       PID %CPU %MEM    VSZ   RSS TTY  STAT START   TIME COMMAND
# root         1  0.0  0.1 169584 13428 ?    Ss   Jan01   0:05 /lib/systemd/systemd

# Hierarkisk vy
ps auxf

# Anpassad output
ps -eo pid,ppid,user,stat,time,comm --sort=-time | head -20

# Processer för specifik användare
ps -u www-data
```

**Steg 2: Förstå PID och PPID**

```bash
# Ditt shells PID
echo $$
# 1234

# Ditt shells förälder (PPID)
echo $PPID
# 999 (sshd eller terminal)

# Hitta föräldrakedja
pstree -p $$
# bash(1234)───pstree(5678)

# Detaljerad process-info
ps -p 1234 -o pid,ppid,pgid,sid,user,comm
```

**Steg 3: Analysera processtillstånd**

```bash
# Hitta processer i olika tillstånd
# Running (R)
ps aux | awk '$8 ~ /R/'

# Sleeping (S)
ps aux | awk '$8 ~ /S/'

# Uninterruptible sleep (D) - ofta I/O-problem
ps aux | awk '$8 ~ /D/'

# Stopped (T)
ps aux | awk '$8 ~ /T/'

# Zombies (Z)
ps aux | awk '$8 ~ /Z/'
```

**Steg 4: Hantera zombie-processer**

```bash
# Identifiera zombies
ps aux | grep -w Z

# Hitta zombiens förälder
ps -o ppid= -p <zombie_pid>

# Visa processträd för föräldern
pstree -p <parent_pid>

# Skicka SIGCHLD till föräldern (triggar wait())
kill -SIGCHLD <parent_pid>

# Om föräldern inte reagerar, döda föräldern
kill <parent_pid>

# Extremfall: döda med SIGKILL
kill -9 <parent_pid>
```

**Steg 5: Utforska /proc**

```bash
# Processinfo för PID 1234
# Statusöversikt
cat /proc/1234/status

# Startkommando
cat /proc/1234/cmdline | tr '\0' ' '

# Miljövariabler
cat /proc/1234/environ | tr '\0' '\n'

# Öppna filer
ls -la /proc/1234/fd/

# Minneskartor
cat /proc/1234/maps

# Current working directory
readlink /proc/1234/cwd

# Executable path
readlink /proc/1234/exe
```

**Steg 6: Processträd-visualisering**

```bash
# Komplett processträd
pstree

# Med PIDs
pstree -p

# Med argument
pstree -a

# Från specifik process
pstree -p 1

# Visa trådar
pstree -t
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Process Audit Script**

```bash
#!/bin/bash
# process-audit.sh - Detaljerad processanalys

echo "=== PROCESS AUDIT REPORT ==="
echo "Date: $(date)"
echo ""

echo "=== System Overview ==="
echo "Total processes: $(ps aux | wc -l)"
echo "Running (R): $(ps aux | awk '$8 ~ /R/' | wc -l)"
echo "Sleeping (S): $(ps aux | awk '$8 ~ /S/' | wc -l)"
echo "Uninterruptible (D): $(ps aux | awk '$8 ~ /D/' | wc -l)"
echo "Zombies (Z): $(ps aux | awk '$8 ~ /Z/' | wc -l)"
echo ""

echo "=== Top CPU Consumers ==="
ps aux --sort=-%cpu | head -6
echo ""

echo "=== Top Memory Consumers ==="
ps aux --sort=-%mem | head -6
echo ""

echo "=== Long-Running Processes ==="
ps -eo pid,user,etime,comm --sort=-etime | head -10
echo ""

echo "=== Zombie Processes ==="
zombies=$(ps aux | awk '$8 ~ /Z/ {print $2, $11}')
if [ -n "$zombies" ]; then
    echo "$zombies"
    echo ""
    echo "Zombie parents:"
    ps aux | awk '$8 ~ /Z/ {print $2}' | while read zpid; do
        ppid=$(ps -o ppid= -p $zpid 2>/dev/null)
        echo "Zombie $zpid -> Parent $ppid ($(ps -o comm= -p $ppid 2>/dev/null))"
    done
else
    echo "No zombies found"
fi
echo ""

echo "=== Processes in D-state (potential I/O issues) ==="
ps aux | awk '$8 ~ /D/ {print $2, $11}'
```

**Exempel 2: Zombie Cleanup Script**

```bash
#!/bin/bash
# zombie-cleanup.sh - Identifiera och hantera zombies

echo "Scanning for zombie processes..."

zombies=$(ps aux | awk '$8 ~ /Z/ {print $2}')

if [ -z "$zombies" ]; then
    echo "No zombie processes found."
    exit 0
fi

echo "Found zombies:"
ps aux | head -1
ps aux | awk '$8 ~ /Z/'
echo ""

for zpid in $zombies; do
    ppid=$(ps -o ppid= -p $zpid 2>/dev/null | tr -d ' ')
    pname=$(ps -o comm= -p $ppid 2>/dev/null)

    echo "Zombie PID $zpid"
    echo "  Parent: $ppid ($pname)"

    # Försök trigga cleanup med SIGCHLD
    echo "  Sending SIGCHLD to parent..."
    kill -SIGCHLD $ppid 2>/dev/null
done

sleep 2

# Kontrollera om zombies finns kvar
remaining=$(ps aux | awk '$8 ~ /Z/' | wc -l)
echo ""
echo "Remaining zombies: $remaining"

if [ "$remaining" -gt 0 ]; then
    echo "Some zombies remain. Parent processes may need to be restarted."
fi
```

**Exempel 3: Process Monitor for Services**

```bash
#!/bin/bash
# service-monitor.sh - Övervaka viktiga tjänster

SERVICES="nginx postgresql docker"
LOG_FILE="/var/log/service-monitor.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

check_service() {
    local service=$1

    # Hitta huvudprocess
    pid=$(pgrep -x $service | head -1)

    if [ -z "$pid" ]; then
        log "WARNING: $service not running!"
        return 1
    fi

    # Kontrollera tillstånd
    state=$(ps -o stat= -p $pid | head -c1)

    case $state in
        R|S)
            log "OK: $service (PID $pid) state: $state"
            ;;
        D)
            log "WARNING: $service (PID $pid) in uninterruptible sleep (I/O issue?)"
            ;;
        T)
            log "WARNING: $service (PID $pid) is stopped!"
            ;;
        Z)
            log "CRITICAL: $service (PID $pid) is zombie!"
            ;;
    esac

    # Visa resurser
    cpu=$(ps -o %cpu= -p $pid)
    mem=$(ps -o %mem= -p $pid)
    log "  Resources: CPU ${cpu}%, MEM ${mem}%"
}

log "=== Service Check Started ==="
for service in $SERVICES; do
    check_service $service
done
log "=== Service Check Complete ==="
```

**Exempel 4: Process Lifecycle Tracing**

```bash
#!/bin/bash
# trace-lifecycle.sh - Visa en process livscykel

TARGET_CMD="${1:-sleep 5}"

echo "Tracing lifecycle of: $TARGET_CMD"
echo ""

# Starta processen i bakgrunden
$TARGET_CMD &
PID=$!

echo "Process started with PID: $PID"
echo ""

# Övervaka tills processen avslutas
while kill -0 $PID 2>/dev/null; do
    state=$(ps -o stat= -p $PID 2>/dev/null)
    time=$(ps -o etime= -p $PID 2>/dev/null)
    echo "State: $state | Elapsed: $time"
    sleep 1
done

# Kontrollera efter zombie
if ps -p $PID -o stat= 2>/dev/null | grep -q Z; then
    echo "Process became zombie!"
    wait $PID  # Cleanup
    echo "Zombie reaped"
fi

echo ""
echo "Process $PID has terminated"
wait $PID
echo "Exit status: $?"
```

------------------------------------------------------------

## Bästa Praxis

**Övervaka zombie-processer**
Zombies indikerar dåligt designade föräldraprocesser. En eller två är ok, många är problem.

**Undersök D-state processer**
Processer i uninterruptible sleep väntar på I/O. Många indikerar disk- eller nätverksproblem.

**Använd pstree för felsökning**
Processträdet visar relationer som hjälper identifiera källan till problem.

**Logga processhistorik**
Verktyg som atop och sar sparar historisk processdata för post-mortem-analys.

**Använd namespaces i containers**
Containers har egen PID-namespace. PID 1 i container är inte systemets PID 1.

------------------------------------------------------------

## Vanliga Fallgropar

**Försöka döda zombies**
Zombies är redan döda - kill fungerar inte. Du måste hantera föräldern.

**Ignorera D-state**
Processer i D-state kan inte avbrytas. Om många fastnar kan systemet bli ohanterat.

**Glömma wait() i scripts**
Shell-scripts som startar bakgrundsprocesser bör wait:a för att undvika zombies.

**Förväxla PID 1 i containers**
I containers är applikationen ofta PID 1 med speciella signalhanteringsregler.

------------------------------------------------------------

## Övningar

### Övning 1: Processanalys
<details>
<summary>Visa övning</summary>

**Uppgift:** Analysera processerna på ditt system och identifiera relationer.

**Steg:**
1. Lista alla processer och deras tillstånd
2. Hitta de fem processer som använder mest CPU
3. Visa processträdet för din SSH-session
4. Identifiera alla processer ägda av www-data (eller annan service-användare)

**Lösning:**
```bash
# 1. Lista processer och tillstånd
ps aux | awk '{print $8}' | sort | uniq -c | sort -rn

# 2. Top 5 CPU
ps aux --sort=-%cpu | head -6

# 3. Processträd för SSH
pstree -p $PPID

# 4. Processer för service-användare
ps -u www-data -f
# eller
ps aux | grep "^www-data"
```
</details>

### Övning 2: Skapa och hantera zombie
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa en kontrollerad zombie och praktisera cleanup.

**Steg:**
1. Skriv ett script som skapar en zombie (fork utan wait)
2. Verifiera att zombien existerar
3. Trigga cleanup
4. Verifiera att zombien försvann

**Lösning:**
```bash
# Skapa zombie-genererande script
cat > /tmp/make_zombie.sh << 'EOF'
#!/bin/bash
# Förälder som inte wait:ar
( exit 0 ) &
echo "Child PID: $!"
echo "Parent sleeping, child will zombie..."
sleep 30
EOF
chmod +x /tmp/make_zombie.sh

# Starta i bakgrunden
/tmp/make_zombie.sh &
PARENT_PID=$!

# Vänta lite och kolla efter zombie
sleep 2
echo "Looking for zombies..."
ps aux | grep -w Z

# Avbryt föräldern (cleanup sker)
kill $PARENT_PID

# Verifiera
sleep 1
ps aux | grep -w Z
```
</details>

### Övning 3: Process monitoring
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa ett script som övervakar en specifik process.

**Krav:**
- Ta processnamn som argument
- Rapportera PID, tillstånd, CPU, minne
- Varna om process saknas eller är i D/Z-state
- Kör i loop med 5 sekunders intervall

**Lösning:**
```bash
#!/bin/bash
# monitor-process.sh

PROCESS="${1:-nginx}"
INTERVAL=5

echo "Monitoring: $PROCESS (Ctrl+C to stop)"
echo ""

while true; do
    pid=$(pgrep -x "$PROCESS" | head -1)

    if [ -z "$pid" ]; then
        echo "[$(date '+%H:%M:%S')] WARNING: $PROCESS not running!"
    else
        state=$(ps -o stat= -p $pid | head -c1)
        cpu=$(ps -o %cpu= -p $pid | tr -d ' ')
        mem=$(ps -o %mem= -p $pid | tr -d ' ')

        status="OK"
        case $state in
            D) status="WARNING: I/O Wait" ;;
            Z) status="CRITICAL: Zombie" ;;
            T) status="WARNING: Stopped" ;;
        esac

        echo "[$(date '+%H:%M:%S')] PID:$pid State:$state CPU:${cpu}% MEM:${mem}% - $status"
    fi

    sleep $INTERVAL
done
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Filesystem Hierarchy Standard - /proc virtuella filsystem
- User and Group Management - process ägare

**Relaterade noder:**
- Foreground vs Background Processes - processstyrning
- Signals - processkommunikation
- Process Monitoring (ps, top, htop) - övervakningsverktyg

**Kommande noder:**
- Systemd Architecture - process management
- Container Fundamentals - process namespaces

------------------------------------------------------------

## Sammanfattning

Processer är körande programinstanser identifierade av unika PIDs. Varje process har en förälder (PPID), och alla härstammar från PID 1 (systemd). Processer skapas med fork/exec och går igenom tillstånd: Running (R), Sleeping (S/D), Stopped (T), och Zombie (Z).

Zombie-processer är avslutade processer som väntar på att föräldern ska anropa wait(). De kan inte dödas - lösningen är att hantera föräldern. D-state processer väntar på I/O och kan inte avbrytas.

/proc-filsystemet exponerar processdata: status, kommandorad, miljövariabler, öppna filer med mera. Verktyg som pstree visualiserar processhierarkin för felsökning.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ps aux` | Lista alla processer |
| `ps auxf` | Hierarkisk processvy |
| `pstree -p` | Visa processträd med PIDs |
| `echo $$` | Visa nuvarande process PID |
| `echo $PPID` | Visa förälderns PID |
| `cat /proc/PID/status` | Detaljerad processstatus |
| `cat /proc/PID/cmdline` | Processens startkommando |
| `ls /proc/PID/fd/` | Öppna filer |
| `ps aux \| grep Z` | Hitta zombie-processer |
| `kill -SIGCHLD PID` | Trigga zombie cleanup |

------------------------------------------------------------

## Referenser

- Linux man pages: ps(1), pstree(1), proc(5)
- "The Linux Programming Interface" - Kerrisk
- Linux Kernel Documentation - Process Management
- Red Hat System Administrator's Guide
- Understanding the Linux Kernel - Bovet & Cesati
""",
        },
        {
            "title": 'Foreground vs Background Processes',
            "slug": 'foreground-background-processes',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Foreground vs Background Processes

------------------------------------------------------------

## Introduktion

När du arbetar med Linux-servrar över SSH är förmågan att hantera processer i förgrund och bakgrund avgörande. Utan denna kunskap riskerar du att långvariga jobb avbryts vid nätverksproblem, eller att din terminal blockeras av ett kommando. Denna modul lär dig skillnaderna mellan förgrunds- och bakgrundsprocesser, hur du flyttar processer mellan dem, och hur du säkerställer att kritiska jobb överlever logout.

------------------------------------------------------------

## Teori

Linux-terminalen kan ha processer i två lägen: förgrund (foreground) och bakgrund (background). Förgrunden tar emot input från tangentbordet och blockerar terminalen, medan bakgrundsprocesser körs oberoende.

```
+------------------------------------------------------------------+
|                 TERMINAL PROCESS CONTROL                          |
+------------------------------------------------------------------+
|                                                                   |
|   Terminal (pts/0)                                                |
|   +----------------------------------------------------------+   |
|   |                                                          |   |
|   |   FOREGROUND                BACKGROUND                   |   |
|   |   +---------------+         +---------------+            |   |
|   |   | Process A     |         | Process B     |            |   |
|   |   | (vim)         |         | (backup.sh &) |            |   |
|   |   +---------------+         +---------------+            |   |
|   |         ^                         |                      |   |
|   |         |                         | (ingen direkt       |   |
|   |    Keyboard                       |  terminal-I/O)      |   |
|   |    Input                          |                      |   |
|   |         |                         |                      |   |
|   |         v                         v                      |   |
|   |   +---------------+         +---------------+            |   |
|   |   | Screen        |         | Output till   |            |   |
|   |   | Output        |         | fil/nowhere   |            |   |
|   |   +---------------+         +---------------+            |   |
|   |                                                          |   |
|   +----------------------------------------------------------+   |
|                                                                   |
+------------------------------------------------------------------+
```

Process groups och sessions är nyckeln till hur terminalen hanterar processer:

```
+------------------------------------------------------------------+
|                    SESSION AND PROCESS GROUPS                     |
+------------------------------------------------------------------+
|                                                                   |
|   Session (SID: 1000) - Kontrollerad av terminal pts/0           |
|   +----------------------------------------------------------+   |
|   |                                                          |   |
|   |   Session Leader: bash (PID 1000)                       |   |
|   |                                                          |   |
|   |   Foreground Process Group (PGID: 1001)                 |   |
|   |   +----------------------------------------------+       |   |
|   |   | vim (PID 1001, PGID 1001)                   |       |   |
|   |   +----------------------------------------------+       |   |
|   |                                                          |   |
|   |   Background Process Groups                              |   |
|   |   +----------------------+  +----------------------+     |   |
|   |   | backup.sh (PID 1002)|  | download (PID 1003) |     |   |
|   |   | PGID: 1002          |  | PGID: 1003          |     |   |
|   |   +----------------------+  +----------------------+     |   |
|   |                                                          |   |
|   +----------------------------------------------------------+   |
|                                                                   |
|   Signaler:                                                       |
|   - SIGHUP: Skickas till alla i session vid logout               |
|   - SIGINT (Ctrl+C): Skickas till foreground process group       |
|   - SIGTSTP (Ctrl+Z): Skickas till foreground process group      |
|                                                                   |
+------------------------------------------------------------------+
```

När du loggar ut skickas SIGHUP (hangup) till alla processer i sessionen. Processer som inte hanterar signalen avslutas.

```
+------------------------------------------------------------------+
|                    LOGOUT / DISCONNECT BEHAVIOR                   |
+------------------------------------------------------------------+
|                                                                   |
|   SSH Connection Active:                                          |
|   +------------------+                                            |
|   | sshd             |                                            |
|   |   └── bash       |  <-- Session leader                       |
|   |         ├── vim  |  <-- Foreground                           |
|   |         └── job &|  <-- Background                           |
|   +------------------+                                            |
|                                                                   |
|   Disconnect / Logout:                                            |
|   +------------------+                                            |
|   | sshd terminates  |                                            |
|   |      |           |                                            |
|   |      v SIGHUP    |                                            |
|   |   bash receives  |                                            |
|   |      |           |                                            |
|   |      v SIGHUP    |                                            |
|   |   All children   |  --> vim: terminates                      |
|   |   receive signal |  --> job: terminates (without nohup)      |
|   +------------------+                                            |
|                                                                   |
|   Med nohup:                                                      |
|   nohup job &        |  --> job: ignores SIGHUP, continues       |
|                                                                   |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Starta process i bakgrunden**

```bash
# Lägg till & i slutet
./long_running_script.sh &
# [1] 12345

# Output visar: [jobnummer] PID

# Verifiera att processen körs
jobs
# [1]+  Running    ./long_running_script.sh &

# Se processdetaljer
ps -p 12345
```

**Steg 2: Pausa och flytta till bakgrund**

```bash
# Starta ett kommando i förgrund
tar -czf backup.tar.gz /home/user

# Pausa med Ctrl+Z
# [1]+  Stopped    tar -czf backup.tar.gz /home/user

# Fortsätt i bakgrunden
bg
# [1]+ tar -czf backup.tar.gz /home/user &

# Eller ange specifikt jobb
bg %1
```

**Steg 3: Ta fram process till förgrund**

```bash
# Lista bakgrundsjobb
jobs
# [1]-  Running    ./script1.sh &
# [2]+  Running    ./script2.sh &

# Ta fram senaste jobbet
fg
# Eller specifikt jobb
fg %1
# Eller med jobbnummer
fg %2
```

**Steg 4: Håll processer vid liv efter logout**

```bash
# nohup - ignorera SIGHUP
nohup ./long_job.sh &
# nohup: ignoring input and appending output to 'nohup.out'

# Med specifik output
nohup ./long_job.sh > /var/log/job.log 2>&1 &

# Disown - ta bort från job table (glömde nohup)
./long_job.sh &
disown %1
# Processen fortsätter men syns inte i jobs

# Disown alla bakgrundsjobb
disown -a
```

**Steg 5: Använd screen/tmux för sessioner**

```bash
# Screen - skapa namngiven session
screen -S deploy

# Kör kommandon i screen-sessionen
./deploy.sh

# Detach: Ctrl+A, sedan D
# Session fortsätter i bakgrunden

# Lista sessioner
screen -ls
# There are screens on:
#   12345.deploy    (Detached)

# Återanslut
screen -r deploy

# Avsluta session inifrån
exit
# eller Ctrl+D
```

```bash
# Tmux - modern alternativ
tmux new -s deploy

# Detach: Ctrl+B, sedan D

# Lista sessioner
tmux ls
# deploy: 1 windows

# Återanslut
tmux attach -t deploy
```

**Steg 6: Hantera output från bakgrundsprocesser**

```bash
# Problem: output blandas med terminal
./noisy_script.sh &
# Script output appears randomly in terminal

# Lösning: redirect output
./noisy_script.sh > output.log 2>&1 &

# Eller till /dev/null
./noisy_script.sh > /dev/null 2>&1 &

# Följ output i realtid
tail -f output.log
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Safe Long-Running Job**

```bash
#!/bin/bash
# safe-deploy.sh - Deployment som överlever disconnect

LOGFILE="/var/log/deploy-$(date +%Y%m%d-%H%M%S).log"

deploy() {
    echo "Starting deployment at $(date)" >> $LOGFILE

    # Deployment steps
    git pull >> $LOGFILE 2>&1
    npm install >> $LOGFILE 2>&1
    npm run build >> $LOGFILE 2>&1

    # Restart service
    sudo systemctl restart myapp >> $LOGFILE 2>&1

    echo "Deployment complete at $(date)" >> $LOGFILE
}

# Kör deployment
echo "Starting deployment..."
echo "Log: $LOGFILE"
nohup bash -c "$(declare -f deploy); deploy" > /dev/null 2>&1 &

echo "Deployment running in background (PID: $!)"
echo "Monitor with: tail -f $LOGFILE"
```

**Exempel 2: Multiple Background Jobs**

```bash
#!/bin/bash
# parallel-backup.sh - Parallella backups

BACKUP_DIR="/backup/$(date +%Y-%m-%d)"
mkdir -p $BACKUP_DIR

# Starta flera backups parallellt
echo "Starting parallel backups..."

tar -czf $BACKUP_DIR/home.tar.gz /home &
PID1=$!
echo "Home backup started (PID: $PID1)"

tar -czf $BACKUP_DIR/var.tar.gz /var &
PID2=$!
echo "Var backup started (PID: $PID2)"

mysqldump --all-databases > $BACKUP_DIR/mysql.sql &
PID3=$!
echo "MySQL backup started (PID: $PID3)"

# Vänta på alla
echo "Waiting for all backups to complete..."
wait $PID1 && echo "Home backup done"
wait $PID2 && echo "Var backup done"
wait $PID3 && echo "MySQL backup done"

echo "All backups complete!"
ls -lh $BACKUP_DIR/
```

**Exempel 3: Job Control Workflow**

```bash
# Praktiskt arbetsflöde med job control

# 1. Starta en editor
vim config.yml
# ^Z (Ctrl+Z)
# [1]+  Stopped    vim config.yml

# 2. Starta backup i bakgrunden
tar -czf backup.tar.gz /data &
# [2] 12346

# 3. Kolla jobb
jobs -l
# [1]+ 12345 Stopped    vim config.yml
# [2]- 12346 Running    tar -czf backup.tar.gz /data &

# 4. Växla tillbaka till vim
fg %1
# (gör klart redigeringen, spara och avsluta)

# 5. Kolla backup-status
jobs
# [2]+  Running    tar -czf backup.tar.gz /data &

# 6. Vänta på backup
wait %2
echo "Backup klart!"
```

**Exempel 4: Screen för Deploy med Monitoring**

```bash
# Starta screen med flera fönster
screen -S production

# Fönster 0: Deploy
./deploy.sh

# Ctrl+A, c (skapa nytt fönster)
# Fönster 1: Log monitoring
tail -f /var/log/app/app.log

# Ctrl+A, c (skapa nytt fönster)
# Fönster 2: System monitoring
htop

# Navigera mellan fönster:
# Ctrl+A, 0-2 (specifikt fönster)
# Ctrl+A, n (nästa)
# Ctrl+A, p (föregående)

# Dela fönster horisontellt:
# Ctrl+A, S
# Ctrl+A, Tab (växla mellan regioner)

# Detach och gå hem:
# Ctrl+A, d

# Nästa dag, återanslut:
screen -r production
```

------------------------------------------------------------

## Bästa Praxis

**Alltid redirect output för bakgrundsjobb**
Output från bakgrundsprocesser kan blandas med terminal eller gå förlorad. Redirect till fil.

**Använd nohup för jobb som måste överleva logout**
SSH-anslutningar kan brytas. nohup + & säkerställer att jobbet fortsätter.

**Screen/tmux för interaktiva sessioner**
För jobb där du behöver interagera eller se output, använd session managers.

**Dokumentera långkörande processer**
Logga PID och syfte så du vet vad som körs och varför.

**Rensa gamla bakgrundsjobb**
Använd jobs regelbundet och avsluta jobb som inte längre behövs.

------------------------------------------------------------

## Vanliga Fallgropar

**Glömma & - terminalen blockeras**
Utan & startar processen i förgrund och blockerar terminalen tills den är klar.

**Output förstör terminalen**
Bakgrundsprocess som skriver output blandar sig med ditt arbete. Redirect!

**Logout dödar jobbet**
Utan nohup eller disown avslutas bakgrundsprocesser vid logout.

**Förväxla jobs och ps**
jobs visar bara shell-jobb, ps visar alla processer. Ett nohup-jobb syns inte i jobs.

**Screen-sessioner hopar sig**
Glömda screen-sessioner fortsätter köra. Rensa med screen -X quit.

------------------------------------------------------------

## Övningar

### Övning 1: Basic Job Control
<details>
<summary>Visa övning</summary>

**Uppgift:** Praktisera grundläggande job control.

**Steg:**
1. Starta ett långt kommando i förgrund
2. Pausa det med Ctrl+Z
3. Starta ett nytt kommando i bakgrunden
4. Lista alla jobb
5. Flytta det pausade jobbet till bakgrund
6. Ta fram det nya jobbet till förgrund

**Lösning:**
```bash
# 1. Starta i förgrund
sleep 300
# ^Z
# [1]+  Stopped    sleep 300

# 2. Starta i bakgrund
sleep 200 &
# [2] 12346

# 3. Lista jobb
jobs -l
# [1]+ 12345 Stopped    sleep 300
# [2]- 12346 Running    sleep 200 &

# 4. Flytta jobb 1 till bakgrund
bg %1
# [1]+ sleep 300 &

# 5. Verifiera
jobs
# [1]-  Running    sleep 300 &
# [2]+  Running    sleep 200 &

# 6. Ta fram jobb 2
fg %2
# sleep 200
# ^C (avbryt)
```
</details>

### Övning 2: Survive Logout
<details>
<summary>Visa övning</summary>

**Uppgift:** Starta ett jobb som överlever logout.

**Scenario:** Du ska köra en backup som tar 2 timmar, men du vill kunna stänga din laptop.

**Steg:**
1. Skapa ett script som simulerar lång körning
2. Starta det så det överlever logout
3. Verifiera att det körs
4. Simulera "logout" och verifiera

**Lösning:**
```bash
# Skapa test-script
cat > /tmp/long_job.sh << 'EOF'
#!/bin/bash
for i in {1..60}; do
    echo "[$(date)] Iteration $i" >> /tmp/job_log.txt
    sleep 2
done
echo "[$(date)] Job complete" >> /tmp/job_log.txt
EOF
chmod +x /tmp/long_job.sh

# Starta med nohup
nohup /tmp/long_job.sh > /tmp/nohup_job.log 2>&1 &
echo "Job PID: $!"

# Verifiera
ps aux | grep long_job
tail -f /tmp/job_log.txt

# Simulera logout (ny terminal):
# Döda bash-processen som startade jobbet
# Verifiera att jobbet fortfarande körs
ps aux | grep long_job
```
</details>

### Övning 3: Screen Workflow
<details>
<summary>Visa övning</summary>

**Uppgift:** Använd screen för en deployment-session.

**Steg:**
1. Skapa en namngiven screen-session
2. Starta ett "deployment" (simulerat)
3. Skapa ett andra fönster för logövervakning
4. Detach
5. Lista sessioner
6. Återanslut

**Lösning:**
```bash
# 1. Skapa session
screen -S deploy

# 2. I screen, starta "deployment"
for i in {1..30}; do echo "Deploying step $i..."; sleep 2; done

# 3. Skapa nytt fönster: Ctrl+A, c
# I nya fönstret:
watch -n 1 'ps aux | head -10'

# 4. Detach: Ctrl+A, d
# [detached from 12345.deploy]

# 5. Lista sessioner
screen -ls
# There are screens on:
#   12345.deploy    (Detached)

# 6. Återanslut
screen -r deploy

# Navigera: Ctrl+A, n (nästa fönster)
# Avsluta: exit i varje fönster eller
# Ctrl+A, :quit (avsluta hela sessionen)
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Process Lifecycle and States - förståelse för processer
- Signals - SIGHUP, SIGTSTP

**Relaterade noder:**
- Job Control (jobs, fg, bg, nohup) - mer detaljer
- Systemd Services - alternativ till nohup

**Kommande noder:**
- Process Monitoring (ps, top, htop) - övervakning
- Container Processes - process management i containers

------------------------------------------------------------

## Sammanfattning

Förgrunds-processer blockerar terminalen och tar emot keyboard-input, medan bakgrundsprocesser (startade med &) körs oberoende. Ctrl+Z pausar en förgrunds-process (SIGTSTP), bg fortsätter den i bakgrunden, och fg tar fram den till förgrund.

Vid logout skickas SIGHUP till alla processer i sessionen. nohup gör att processen ignorerar SIGHUP och fortsätter köra. disown tar bort processen från shell:ets job-table.

Screen och tmux är session managers som skapar persistenta terminalsessioner som överlever disconnect och kan återanslutas senare. De är ideala för långkörande interaktiva jobb.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `command &` | Starta i bakgrund |
| `Ctrl+Z` | Pausa förgrunds-process |
| `jobs` | Lista shell-jobb |
| `jobs -l` | Lista med PIDs |
| `fg %N` | Ta fram jobb N till förgrund |
| `bg %N` | Fortsätt jobb N i bakgrund |
| `nohup cmd &` | Kör och överlev logout |
| `disown %N` | Ta bort jobb från job-table |
| `screen -S name` | Skapa namngiven session |
| `screen -r name` | Återanslut till session |
| `Ctrl+A, d` | Detach från screen |
| `tmux new -s name` | Skapa tmux-session |
| `tmux attach -t name` | Återanslut till tmux |

------------------------------------------------------------

## Referenser

- Linux man pages: bash(1), screen(1), tmux(1)
- GNU Bash Manual - Job Control
- Screen User's Manual
- tmux Wiki
- "The Linux Command Line" - William Shotts
""",
        },
        {
            "title": 'Job Control (jobs, fg, bg, nohup)',
            "slug": 'job-control',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Job Control (jobs, fg, bg, nohup)

------------------------------------------------------------

## Introduktion

Job control är en kraftfull funktion i Unix-shells som låter dig hantera flera processer från en enda terminal. Som DevOps-ingenjör använder du job control dagligen för att köra backups i bakgrunden, hantera långvariga deployments, och säkerställa att kritiska processer fortsätter även om SSH-anslutningen bryts. Denna modul ger dig komplett behärskning av job control-mekanismerna.

------------------------------------------------------------

## Teori

Shell:et håller reda på processer genom ett job table där varje jobb har ett jobbnummer. Jobs kan vara i tre tillstånd: Running (körs), Stopped (pausad), eller Done (avslutad).

```
+------------------------------------------------------------------+
|                      JOB CONTROL OVERVIEW                         |
+------------------------------------------------------------------+
|                                                                   |
|   Shell (bash)                                                    |
|   +----------------------------------------------------------+   |
|   |                                                          |   |
|   |   Job Table                                              |   |
|   |   +--------------------------------------------------+   |   |
|   |   | Job# | PID   | State   | Command                |   |   |
|   |   |------|-------|---------|------------------------|   |   |
|   |   | 1    | 12345 | Running | ./backup.sh &          |   |   |
|   |   | 2    | 12346 | Stopped | vim config.yml         |   |   |
|   |   | 3    | 12347 | Running | tail -f /var/log/app & |   |   |
|   |   +--------------------------------------------------+   |   |
|   |                                                          |   |
|   |   Job Notation:                                          |   |
|   |   %1  = Job nummer 1                                     |   |
|   |   %+  = Current job (senast interagerat)                 |   |
|   |   %-  = Previous job                                     |   |
|   |   %%  = Samma som %+                                     |   |
|   |   %?string = Jobb vars kommando innehåller "string"      |   |
|   |                                                          |   |
|   +----------------------------------------------------------+   |
|                                                                   |
+------------------------------------------------------------------+
```

Processer och signaler relaterade till job control:

```
+------------------------------------------------------------------+
|                    JOB CONTROL SIGNALS                            |
+------------------------------------------------------------------+
|                                                                   |
|   Ctrl+Z  -->  SIGTSTP (Terminal Stop)                           |
|   +----------+     +----------+                                   |
|   | Foreground| --> | Stopped  |                                  |
|   | Process   |     | State    |                                  |
|   +----------+     +----------+                                   |
|                          |                                        |
|                          v                                        |
|                    +-----------+                                  |
|                    | bg %n     |  --> SIGCONT --> Running (bg)   |
|                    +-----------+                                  |
|                    | fg %n     |  --> SIGCONT --> Running (fg)   |
|                    +-----------+                                  |
|                                                                   |
|   SIGHUP vid logout:                                              |
|   +---------------+                                               |
|   | Shell logout  | --> SIGHUP till alla jobb                    |
|   +---------------+                                               |
|          |                                                        |
|          v                                                        |
|   +---------------+     +---------------+                         |
|   | Normalt jobb  |     | nohup/disown  |                         |
|   | TERMINERAS    |     | FORTSÄTTER    |                         |
|   +---------------+     +---------------+                         |
|                                                                   |
+------------------------------------------------------------------+
```

nohup och disown fungerar på olika sätt:

```
+------------------------------------------------------------------+
|                    nohup vs disown                                |
+------------------------------------------------------------------+
|                                                                   |
|   nohup:                                                          |
|   - Startar process med SIGHUP ignorerad                         |
|   - Redirect stdout till nohup.out om inte omdirigerad           |
|   - Process finns kvar i job table                               |
|   - Används INNAN start                                          |
|                                                                   |
|   disown:                                                         |
|   - Tar bort jobb från shell:ets job table                       |
|   - Shell skickar inte SIGHUP vid logout                         |
|   - Processen fortsätter men syns inte i jobs                    |
|   - Används EFTER start (glömt nohup)                            |
|                                                                   |
|   disown -h:                                                      |
|   - Markerar jobb att inte ta emot SIGHUP                        |
|   - Jobbet finns KVAR i job table                                |
|   - Kan fortfarande använda fg/bg                                |
|                                                                   |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Grundläggande job control**

```bash
# Starta process i förgrund
./long_script.sh
# Terminalen blockeras...

# Pausa med Ctrl+Z
# [1]+  Stopped    ./long_script.sh

# Visa alla jobb
jobs
# [1]+  Stopped    ./long_script.sh

# Med PIDs
jobs -l
# [1]+ 12345 Stopped    ./long_script.sh

# Bara PIDs
jobs -p
# 12345
```

**Steg 2: Flytta jobb mellan förgrund och bakgrund**

```bash
# Fortsätt pausat jobb i bakgrunden
bg %1
# [1]+ ./long_script.sh &

# Verifiera
jobs
# [1]+  Running    ./long_script.sh &

# Ta fram till förgrund
fg %1
# ./long_script.sh
# (nu i förgrund igen)
```

**Steg 3: Starta direkt i bakgrund**

```bash
# Lägg till & i slutet
./backup.sh &
# [1] 12345

# Flera jobb
./job1.sh &
./job2.sh &
./job3.sh &

# Lista alla
jobs
# [1]   Running    ./job1.sh &
# [2]-  Running    ./job2.sh &
# [3]+  Running    ./job3.sh &
```

**Steg 4: Använd nohup för persistens**

```bash
# Basic nohup
nohup ./long_job.sh &
# nohup: ignoring input and appending output to 'nohup.out'
# [1] 12345

# Med egen loggfil
nohup ./long_job.sh > /var/log/job.log 2>&1 &

# Verifiera att den kör
jobs
# [1]+  Running    nohup ./long_job.sh &

# Logga ut - processen fortsätter
exit
```

**Steg 5: Rädda jobb med disown**

```bash
# Oops, glömde nohup!
./critical_backup.sh &
# [1] 12345

# Rädda med disown
disown %1

# Jobbet syns inte längre
jobs
# (tomt)

# Men processen kör fortfarande
ps aux | grep critical_backup
# user 12345 ... ./critical_backup.sh
```

**Steg 6: Avancerad jobbhantering**

```bash
# Referera jobb med sökord
sleep 100 &
tail -f /var/log/syslog &

# Hitta jobb som matchar
fg %?tail
# tail -f /var/log/syslog

# disown med -h (behåll i job table men ignorera SIGHUP)
./monitoring.sh &
disown -h %1

# Kan fortfarande använda job control
fg %1
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Deploy med Job Control**

```bash
#!/bin/bash
# controlled-deploy.sh

echo "=== Starting Deployment ==="

# Steg 1: Database backup i bakgrunden
echo "Starting database backup..."
pg_dump mydb > backup.sql &
BACKUP_PID=$!
echo "Backup running as job $!"

# Steg 2: Asset compilation
echo "Compiling assets..."
npm run build &
BUILD_PID=$!

# Steg 3: Visa jobbstatus
echo ""
echo "Jobs running:"
jobs -l

# Steg 4: Vänta på båda
echo ""
echo "Waiting for jobs to complete..."
wait $BACKUP_PID
echo "Backup complete!"
wait $BUILD_PID
echo "Build complete!"

# Steg 5: Fortsätt med deployment
echo ""
echo "Deploying application..."
./deploy-app.sh
```

**Exempel 2: Multi-task Workflow**

```bash
# Scenario: Hantera flera uppgifter från en terminal

# 1. Starta editor för config
vim config.yml
# ^Z (pausa)
# [1]+  Stopped    vim config.yml

# 2. Starta logövervakning i bakgrunden
tail -f /var/log/app.log &
# [2] 12346

# 3. Kör ett test
./run_tests.sh
# ^Z (pausa - tar för lång tid)
# [3]+  Stopped    ./run_tests.sh

# 4. Flytta test till bakgrund så det fortsätter
bg %3
# [3]+ ./run_tests.sh &

# 5. Gå tillbaka till vim
fg %1
# (redigera klart, :wq)

# 6. Kolla jobbstatus
jobs
# [2]-  Running    tail -f /var/log/app.log &
# [3]+  Running    ./run_tests.sh &

# 7. Ta fram logövervakning när tester är klara
wait %3
fg %2
```

**Exempel 3: Safe Long-Running Operations**

```bash
#!/bin/bash
# safe-operation.sh - Kör operationer som överlever disconnect

operation_name="${1:-backup}"
log_file="/var/log/${operation_name}-$(date +%Y%m%d-%H%M%S).log"

echo "Starting $operation_name operation..."
echo "Log file: $log_file"

case $operation_name in
    backup)
        nohup tar -czf /backup/full-backup.tar.gz /data > "$log_file" 2>&1 &
        ;;
    migrate)
        nohup ./database-migration.sh > "$log_file" 2>&1 &
        ;;
    sync)
        nohup rsync -avz /data remote:/backup > "$log_file" 2>&1 &
        ;;
    *)
        echo "Unknown operation: $operation_name"
        exit 1
        ;;
esac

pid=$!
echo "Operation started with PID: $pid"
echo ""
echo "Commands:"
echo "  Check status:  ps -p $pid"
echo "  Watch log:     tail -f $log_file"
echo "  Kill if needed: kill $pid"
echo ""
echo "Safe to disconnect - operation will continue."
```

**Exempel 4: Parallel Execution with Wait**

```bash
#!/bin/bash
# parallel-jobs.sh - Kör flera jobb parallellt och vänta

declare -a pids

# Starta jobb parallellt
echo "Starting parallel jobs..."

./task1.sh &
pids+=($!)

./task2.sh &
pids+=($!)

./task3.sh &
pids+=($!)

echo "Jobs started: ${pids[*]}"

# Visa jobbstatus
jobs -l

# Vänta på alla med felhantering
failed=0
for pid in "${pids[@]}"; do
    if ! wait $pid; then
        echo "Job $pid failed!"
        ((failed++))
    fi
done

if [ $failed -gt 0 ]; then
    echo "WARNING: $failed job(s) failed"
    exit 1
else
    echo "All jobs completed successfully!"
fi
```

------------------------------------------------------------

## Bästa Praxis

**Använd nohup för planerade långvariga jobb**
När du vet att ett jobb tar lång tid, starta med nohup från början.

**disown -h istället för disown**
Med -h flaggan kan du fortfarande använda job control medan jobbet skyddas mot SIGHUP.

**Redirect output för alla bakgrundsjobb**
Undvik förlorad output och rörig terminal genom att alltid redirect.

**Använd wait för att synkronisera parallella jobb**
wait med PID eller jobbnummer låter dig vänta på specifika jobb.

**Dokumentera PID för kritiska jobb**
Spara PID så du kan hitta processen senare med ps.

------------------------------------------------------------

## Vanliga Fallgropar

**Glömma & - terminalen blockeras**
Utan & startar processen i förgrund. Använd Ctrl+Z + bg om du glömmer.

**Logout med aktiva jobb**
Shell varnar ofta "You have stopped jobs". Använd disown eller nohup.

**Förväxla jobbnummer och PID**
%1 är jobbnummer, 12345 är PID. jobs visar båda med -l.

**disown på pausat jobb**
disown på ett Stopped jobb startar det inte - det förblir pausat.

**nohup.out fyller disk**
Om du inte redirect:ar skapas nohup.out som kan växa obegränsat.

------------------------------------------------------------

## Övningar

### Övning 1: Basic Job Manipulation
<details>
<summary>Visa övning</summary>

**Uppgift:** Praktisera grundläggande job control operationer.

**Steg:**
1. Starta tre sleep-kommandon med olika tider
2. Pausa ett, kör ett i bakgrund direkt
3. Flytta det pausade till bakgrund
4. Lista alla jobb med PIDs
5. Ta fram ett till förgrund och avbryt det

**Lösning:**
```bash
# 1. Starta jobb
sleep 100 &
# [1] 12345
sleep 200
# ^Z
# [2]+  Stopped    sleep 200
sleep 300 &
# [3] 12347

# 2. Lista jobb
jobs -l
# [1]   12345 Running    sleep 100 &
# [2]+  12346 Stopped    sleep 200
# [3]-  12347 Running    sleep 300 &

# 3. Flytta stoppat jobb till bakgrund
bg %2
# [2]+ sleep 200 &

# 4. Lista igen
jobs
# [1]   Running    sleep 100 &
# [2]-  Running    sleep 200 &
# [3]+  Running    sleep 300 &

# 5. Ta fram och avbryt
fg %3
# sleep 300
# ^C
```
</details>

### Övning 2: Survive Logout
<details>
<summary>Visa övning</summary>

**Uppgift:** Starta ett jobb som garanterat överlever logout.

**Scenario:** Du ska köra en 2-timmars backup men behöver kunna stänga laptopen.

**Steg:**
1. Skapa ett test-script som kör länge
2. Starta det med nohup
3. Verifiera att det körs
4. Simulera logout och kontrollera

**Lösning:**
```bash
# Skapa test-script
cat > /tmp/long_backup.sh << 'EOF'
#!/bin/bash
for i in {1..120}; do
    echo "[$(date)] Minute $i of backup" >> /tmp/backup.log
    sleep 60
done
echo "[$(date)] Backup complete" >> /tmp/backup.log
EOF
chmod +x /tmp/long_backup.sh

# Starta med nohup
nohup /tmp/long_backup.sh > /tmp/backup_nohup.log 2>&1 &
echo "Backup PID: $!"
# Backup PID: 12345

# Verifiera
jobs -l
ps -p 12345

# Testa logout-överlevnad (i ny terminal)
# kill -HUP 12345
# ps -p 12345  # Fortfarande igång!

# Övervaka
tail -f /tmp/backup.log
```
</details>

### Övning 3: Rescue Forgotten Job
<details>
<summary>Visa övning</summary>

**Uppgift:** Rädda ett jobb som startades utan nohup.

**Scenario:** Du startade en migration i bakgrunden men glömde nohup. Du måste gå hem.

**Steg:**
1. Starta ett "migrations"-script
2. Inse att du glömde nohup
3. Rädda jobbet med disown
4. Verifiera att det överlever SIGHUP

**Lösning:**
```bash
# Simulera migration
cat > /tmp/migration.sh << 'EOF'
#!/bin/bash
echo "Starting migration..."
for i in {1..60}; do
    echo "Migrating batch $i..."
    sleep 5
done
echo "Migration complete!"
EOF
chmod +x /tmp/migration.sh

# Starta (oops, glömde nohup!)
/tmp/migration.sh > /tmp/migration.log 2>&1 &
# [1] 12345

# Kontrollera
jobs
# [1]+  Running    /tmp/migration.sh > /tmp/migration.log 2>&1 &

# Rädda med disown -h (behåller i job table)
disown -h %1

# Eller ta bort helt
disown %1

# Verifiera att processen fortsätter
ps -p 12345

# Testa SIGHUP (från annan terminal)
# kill -HUP 12345
# ps -p 12345  # Fortfarande igång!
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Process Lifecycle and States - processgrunder
- Foreground vs Background Processes - översikt

**Relaterade noder:**
- Signals - SIGHUP och andra signaler
- Process Monitoring - ps, top, htop

**Kommande noder:**
- Systemd Services - alternativ till job control
- Container Process Management - jobb i containers

------------------------------------------------------------

## Sammanfattning

Job control låter dig hantera flera processer från en terminal. Jobb kan vara Running, Stopped, eller Done och refereras med %n notation. Ctrl+Z pausar förgrunds-processer (SIGTSTP), bg och fg flyttar jobb mellan bakgrund och förgrund.

nohup startar processer som ignorerar SIGHUP och därmed överlever logout. disown tar bort jobb från shell:ets job table så att SIGHUP inte skickas vid logout. disown -h markerar jobb att ignorera SIGHUP men behåller dem i job table.

wait låter dig vänta på specifika jobb eller alla bakgrundsjobb, användbart för att synkronisera parallella operationer.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `jobs` | Lista alla shell-jobb |
| `jobs -l` | Lista med PIDs |
| `jobs -p` | Visa bara PIDs |
| `Ctrl+Z` | Pausa förgrunds-process |
| `bg %n` | Fortsätt jobb n i bakgrund |
| `fg %n` | Ta fram jobb n till förgrund |
| `%n` | Referera till jobb nummer n |
| `%?str` | Jobb vars kommando matchar str |
| `nohup cmd &` | Kör cmd immun mot SIGHUP |
| `disown %n` | Ta bort jobb från job table |
| `disown -h %n` | Markera jobb att ignorera SIGHUP |
| `wait %n` | Vänta på jobb n |
| `wait` | Vänta på alla bakgrundsjobb |

------------------------------------------------------------

## Referenser

- Bash Reference Manual - Job Control
- Linux man pages: bash(1), jobs(1)
- POSIX Shell Job Control
- "The Linux Command Line" - William Shotts
- Advanced Bash-Scripting Guide
""",
        },
        {
            "title": 'Signals (SIGTERM, SIGKILL, SIGHUP)',
            "slug": 'signals',
            "difficulty": "intermediate",
            "estimated_minutes": 90,
            "xp_reward": 150,
            "content": """# Signals (SIGTERM, SIGKILL, SIGHUP)

------------------------------------------------------------

## Introduktion

Signaler är Linux-kärnans mekanism för att kommunicera med processer - allt från Ctrl+C som avbryter ett kommando till graceful shutdown av en webbserver. Som DevOps-ingenjör måste du förstå signaler för att kunna stoppa tjänster utan dataförlust, ladda om konfiguration utan nertid, och bygga robusta scripts som städar upp efter sig. Denna modul ger dig fullständig behärskning av Linux-signaler.

------------------------------------------------------------

## Teori

Signaler är asynkrona notifikationer skickade till processer. När en process tar emot en signal kan den hantera den (handle), ignorera den (ignore), eller låta standardbeteendet ske (default).

```
+------------------------------------------------------------------+
|                    SIGNAL DELIVERY                                |
+------------------------------------------------------------------+
|                                                                   |
|   Signal Sources:                                                 |
|   +------------+  +------------+  +------------+                  |
|   | Terminal   |  | Kernel     |  | Other      |                  |
|   | Ctrl+C     |  | Segfault   |  | Process    |                  |
|   | Ctrl+Z     |  | Alarm      |  | kill cmd   |                  |
|   +------------+  +------------+  +------------+                  |
|         |               |               |                         |
|         +---------------+---------------+                         |
|                         |                                         |
|                         v                                         |
|   +--------------------------------------------------+           |
|   |              Signal Delivery                     |           |
|   +--------------------------------------------------+           |
|                         |                                         |
|                         v                                         |
|   +--------------------------------------------------+           |
|   | Process Signal Handling                          |           |
|   +--------------------------------------------------+           |
|   |                                                  |           |
|   |  1. Custom Handler  -->  Execute handler func   |           |
|   |  2. Ignore (SIG_IGN) --> Do nothing             |           |
|   |  3. Default Action   --> Terminate/Stop/Ignore  |           |
|   |                                                  |           |
|   +--------------------------------------------------+           |
|                                                                   |
+------------------------------------------------------------------+
```

De viktigaste signalerna för DevOps:

```
+------------------------------------------------------------------+
|                    CRITICAL SIGNALS                               |
+------------------------------------------------------------------+
|                                                                   |
|   Signal    | Num | Default Action | Can Catch? | Use Case       |
|   ----------|-----|----------------|------------|----------------|
|   SIGTERM   | 15  | Terminate      | Yes        | Graceful stop  |
|   SIGKILL   | 9   | Terminate      | NO         | Force kill     |
|   SIGINT    | 2   | Terminate      | Yes        | Ctrl+C         |
|   SIGHUP    | 1   | Terminate      | Yes        | Reload config  |
|   SIGSTOP   | 19  | Stop           | NO         | Pause process  |
|   SIGCONT   | 18  | Continue       | Yes        | Resume process |
|   SIGQUIT   | 3   | Core dump      | Yes        | Quit + dump    |
|   SIGUSR1   | 10  | Terminate      | Yes        | Custom use     |
|   SIGUSR2   | 12  | Terminate      | Yes        | Custom use     |
|   SIGCHLD   | 17  | Ignore         | Yes        | Child stopped  |
|                                                                   |
+------------------------------------------------------------------+
```

SIGTERM vs SIGKILL är kritiskt att förstå:

```
+------------------------------------------------------------------+
|                    SIGTERM vs SIGKILL                             |
+------------------------------------------------------------------+
|                                                                   |
|   SIGTERM (kill)                  SIGKILL (kill -9)              |
|   +----------------------+        +----------------------+        |
|   | "Please terminate"   |        | "DIE. NOW."          |        |
|   +----------------------+        +----------------------+        |
|            |                               |                      |
|            v                               v                      |
|   +----------------------+        +----------------------+        |
|   | Process receives     |        | Kernel terminates    |        |
|   | signal               |        | process immediately  |        |
|   +----------------------+        +----------------------+        |
|            |                               |                      |
|            v                               v                      |
|   +----------------------+        +----------------------+        |
|   | Handler runs:        |        | NO cleanup happens   |        |
|   | - Save state         |        | - Open files lost    |        |
|   | - Close connections  |        | - Temp files remain  |        |
|   | - Cleanup temp files |        | - Transactions lost  |        |
|   | - Log shutdown       |        | - Locks not released |        |
|   +----------------------+        +----------------------+        |
|            |                               |                      |
|            v                               v                      |
|   +----------------------+        +----------------------+        |
|   | Clean exit           |        | Dirty termination    |        |
|   +----------------------+        +----------------------+        |
|                                                                   |
|   Use SIGTERM first, SIGKILL only as last resort!                |
|                                                                   |
+------------------------------------------------------------------+
```

SIGHUP har dubbel betydelse - traditionellt "terminal hangup" men modern användning är "reload configuration":

```
+------------------------------------------------------------------+
|                    SIGHUP EVOLUTION                               |
+------------------------------------------------------------------+
|                                                                   |
|   Traditional (Terminal)          Modern (Daemons)               |
|   +----------------------+        +----------------------+        |
|   | Terminal disconnects |        | Admin sends SIGHUP   |        |
|   +----------------------+        +----------------------+        |
|            |                               |                      |
|            v                               v                      |
|   +----------------------+        +----------------------+        |
|   | SIGHUP sent to       |        | Daemon catches       |        |
|   | session processes    |        | SIGHUP               |        |
|   +----------------------+        +----------------------+        |
|            |                               |                      |
|            v                               v                      |
|   +----------------------+        +----------------------+        |
|   | Processes terminate  |        | Daemon reloads:      |        |
|   | (default action)     |        | - Config files       |        |
|   |                      |        | - Log files          |        |
|   |                      |        | - Certificates       |        |
|   +----------------------+        +----------------------+        |
|                                                                   |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

**Steg 1: Skicka signaler med kill**

```bash
# Lista alla signaler
kill -l
# 1) SIGHUP    2) SIGINT    3) SIGQUIT   ...

# Skicka SIGTERM (default)
kill 12345

# Skicka specifik signal (namn)
kill -SIGTERM 12345
kill -TERM 12345

# Skicka specifik signal (nummer)
kill -15 12345

# SIGKILL (tvinga)
kill -9 12345
kill -KILL 12345

# SIGHUP (reload)
kill -1 12345
kill -HUP 12345
```

**Steg 2: Använd killall och pkill**

```bash
# Döda alla processer med namn
killall nginx

# Döda med signal
killall -TERM nginx
killall -9 nginx

# pkill - mer flexibelt
pkill nginx              # Matcha processnamn
pkill -f "python app.py" # Matcha hela kommandoraden
pkill -u www-data        # Matcha användare
pkill -P 1234            # Matcha parent PID

# pgrep - hitta först
pgrep nginx
# 12345
# 12346

pgrep -l nginx
# 12345 nginx
# 12346 nginx
```

**Steg 3: Graceful shutdown sekvens**

```bash
#!/bin/bash
# graceful-kill.sh - Korrekt avslutningssekvens

PID=$1
TIMEOUT=${2:-10}

if [ -z "$PID" ]; then
    echo "Usage: $0 <pid> [timeout]"
    exit 1
fi

# Kontrollera att processen finns
if ! kill -0 "$PID" 2>/dev/null; then
    echo "Process $PID does not exist"
    exit 0
fi

echo "Sending SIGTERM to $PID..."
kill -TERM "$PID"

# Vänta på graceful shutdown
for i in $(seq 1 $TIMEOUT); do
    if ! kill -0 "$PID" 2>/dev/null; then
        echo "Process terminated gracefully"
        exit 0
    fi
    echo "Waiting... ($i/$TIMEOUT)"
    sleep 1
done

# Fortfarande igång - använd SIGKILL
echo "Process still running, sending SIGKILL..."
kill -9 "$PID"
sleep 1

if kill -0 "$PID" 2>/dev/null; then
    echo "ERROR: Could not kill process $PID"
    exit 1
else
    echo "Process killed"
    exit 0
fi
```

**Steg 4: Reload configuration med SIGHUP**

```bash
# Nginx reload
kill -HUP $(cat /var/run/nginx.pid)

# Eller via systemctl (rekommenderat)
sudo systemctl reload nginx

# SSH daemon
sudo kill -HUP $(pgrep -o sshd)

# Syslog
sudo kill -HUP $(cat /var/run/rsyslogd.pid)
```

**Steg 5: Signal handling i scripts**

```bash
#!/bin/bash
# robust-script.sh - Script med signalhantering

TEMPFILE=""
LOCKFILE="/var/run/myapp.lock"

# Cleanup-funktion
cleanup() {
    echo "Cleaning up..."
    [ -f "$TEMPFILE" ] && rm -f "$TEMPFILE"
    [ -f "$LOCKFILE" ] && rm -f "$LOCKFILE"
    exit 0
}

# Fånga signaler
trap cleanup SIGTERM SIGINT SIGHUP

# Skapa lock och temp
touch "$LOCKFILE"
TEMPFILE=$(mktemp)

echo "Running (PID $$)... Press Ctrl+C to stop"

# Huvudloop
while true; do
    echo "Working..." >> "$TEMPFILE"
    sleep 2
done
```

**Steg 6: Avancerad signalhantering**

```bash
#!/bin/bash
# advanced-signals.sh

# Olika handlers för olika signaler
handle_term() {
    echo "Received SIGTERM, initiating graceful shutdown..."
    # Stäng anslutningar, spara state
    exit 0
}

handle_hup() {
    echo "Received SIGHUP, reloading configuration..."
    # Läs om config-filer
    source /etc/myapp/config
}

handle_usr1() {
    echo "Received SIGUSR1, dumping status..."
    # Custom action, t.ex. dump statistics
    echo "Status: Running, Uptime: $SECONDS seconds"
}

# Registrera handlers
trap handle_term SIGTERM
trap handle_hup SIGHUP
trap handle_usr1 SIGUSR1

echo "Script running (PID $$)"
echo "Send signals with: kill -TERM/HUP/USR1 $$"

while true; do
    sleep 1
done
```

------------------------------------------------------------

## Praktiska Exempel

**Exempel 1: Service Shutdown Script**

```bash
#!/bin/bash
# stop-service.sh - Graceful service shutdown

SERVICE_NAME="${1:-myapp}"
PID_FILE="/var/run/${SERVICE_NAME}.pid"
GRACEFUL_TIMEOUT=30
KILL_TIMEOUT=5

if [ ! -f "$PID_FILE" ]; then
    echo "PID file not found: $PID_FILE"
    exit 1
fi

PID=$(cat "$PID_FILE")

if ! kill -0 "$PID" 2>/dev/null; then
    echo "Process $PID is not running"
    rm -f "$PID_FILE"
    exit 0
fi

echo "Stopping $SERVICE_NAME (PID: $PID)..."

# Steg 1: SIGTERM
echo "Sending SIGTERM..."
kill -TERM "$PID"

# Vänta på graceful shutdown
waited=0
while kill -0 "$PID" 2>/dev/null; do
    if [ $waited -ge $GRACEFUL_TIMEOUT ]; then
        break
    fi
    sleep 1
    ((waited++))
    echo -ne "\rWaiting for graceful shutdown... ${waited}s"
done
echo ""

# Steg 2: SIGKILL om nödvändigt
if kill -0 "$PID" 2>/dev/null; then
    echo "Process still running, sending SIGKILL..."
    kill -KILL "$PID"

    # Vänta på SIGKILL
    waited=0
    while kill -0 "$PID" 2>/dev/null; do
        if [ $waited -ge $KILL_TIMEOUT ]; then
            echo "ERROR: Process $PID could not be killed"
            exit 1
        fi
        sleep 1
        ((waited++))
    done
fi

echo "$SERVICE_NAME stopped"
rm -f "$PID_FILE"
```

**Exempel 2: Zero-Downtime Reload**

```bash
#!/bin/bash
# hot-reload.sh - Reload service utan nertid

SERVICE="nginx"
PID_FILE="/var/run/nginx.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "Service not running"
    exit 1
fi

MASTER_PID=$(cat "$PID_FILE")

echo "Testing new configuration..."
if ! nginx -t 2>&1; then
    echo "Configuration test failed!"
    exit 1
fi

echo "Configuration OK, reloading..."
kill -HUP "$MASTER_PID"

# Vänta på nya workers
sleep 2

# Verifiera
echo "Checking service status..."
if kill -0 "$MASTER_PID" 2>/dev/null; then
    echo "Reload successful!"
    nginx -v
    ps aux | grep "[n]ginx"
else
    echo "ERROR: Service died during reload!"
    exit 1
fi
```

**Exempel 3: Signal-Aware Application**

```bash
#!/bin/bash
# worker-app.sh - Application med fullständig signalhantering

WORKER_COUNT=3
declare -a WORKER_PIDS
SHUTDOWN_REQUESTED=false

# Cleanup alla workers
cleanup_workers() {
    echo "Shutting down workers..."
    for pid in "${WORKER_PIDS[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            kill -TERM "$pid"
        fi
    done
    wait
    echo "All workers stopped"
}

# Signal handlers
handle_term() {
    echo "SIGTERM received, initiating shutdown..."
    SHUTDOWN_REQUESTED=true
    cleanup_workers
    exit 0
}

handle_hup() {
    echo "SIGHUP received, restarting workers..."
    cleanup_workers
    start_workers
}

handle_usr1() {
    echo "Worker Status:"
    for i in "${!WORKER_PIDS[@]}"; do
        pid=${WORKER_PIDS[$i]}
        if kill -0 "$pid" 2>/dev/null; then
            echo "  Worker $i (PID $pid): Running"
        else
            echo "  Worker $i (PID $pid): Dead"
        fi
    done
}

# Worker-process
worker_process() {
    local id=$1
    echo "Worker $id started (PID $$)"
    while true; do
        echo "Worker $id processing..."
        sleep 5
    done
}

# Starta workers
start_workers() {
    echo "Starting $WORKER_COUNT workers..."
    for i in $(seq 1 $WORKER_COUNT); do
        worker_process $i &
        WORKER_PIDS+=($!)
    done
    echo "Workers started: ${WORKER_PIDS[*]}"
}

# Registrera handlers
trap handle_term SIGTERM SIGINT
trap handle_hup SIGHUP
trap handle_usr1 SIGUSR1

echo "Application starting (PID $$)"
start_workers

# Supervise workers
while ! $SHUTDOWN_REQUESTED; do
    for i in "${!WORKER_PIDS[@]}"; do
        pid=${WORKER_PIDS[$i]}
        if ! kill -0 "$pid" 2>/dev/null; then
            echo "Worker $i died, restarting..."
            worker_process $i &
            WORKER_PIDS[$i]=$!
        fi
    done
    sleep 1
done
```

**Exempel 4: Log Rotation med SIGHUP**

```bash
#!/bin/bash
# logrotate-signal.sh - Manuell log rotation

APP_PID_FILE="/var/run/myapp.pid"
LOG_FILE="/var/log/myapp/app.log"
ARCHIVE_DIR="/var/log/myapp/archive"

# Skapa arkivkatalog
mkdir -p "$ARCHIVE_DIR"

# Rotera loggen
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mv "$LOG_FILE" "$ARCHIVE_DIR/app-${TIMESTAMP}.log"

# Skapa ny tom logg
touch "$LOG_FILE"
chmod 644 "$LOG_FILE"

# Signalera applikationen att öppna ny loggfil
if [ -f "$APP_PID_FILE" ]; then
    PID=$(cat "$APP_PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        echo "Sending SIGHUP to $PID..."
        kill -HUP "$PID"
    fi
fi

# Komprimera gamla loggar
gzip "$ARCHIVE_DIR/app-${TIMESTAMP}.log"

# Rensa loggar äldre än 30 dagar
find "$ARCHIVE_DIR" -name "*.log.gz" -mtime +30 -delete

echo "Log rotation complete"
```

------------------------------------------------------------

## Bästa Praxis

**Alltid SIGTERM före SIGKILL**
Ge processer chans att städa upp. SIGKILL orsakar dataförlust och korruption.

**Implementera signal handlers i applikationer**
Alla produktionsapplikationer bör hantera SIGTERM för graceful shutdown.

**Använd SIGHUP för reload**
Standard för att ladda om konfiguration utan att starta om tjänsten.

**Timeout mellan SIGTERM och SIGKILL**
10-30 sekunder är rimligt beroende på applikationens komplexitet.

**Dokumentera vilka signaler din applikation stödjer**
SIGUSR1/SIGUSR2 har ingen standardbetydelse - dokumentera din användning.

------------------------------------------------------------

## Vanliga Fallgropar

**kill -9 som första val**
Orsakar dataförlust, lämnar temporära filer, bryter transaktioner.

**Glömma trap cleanup i scripts**
Temporära filer och locks blir kvar när scriptet avbryts.

**SIGHUP till processer startade utan nohup**
Dödar processen istället för att ladda om config.

**Ignorera SIGTERM i containers**
Container processes (PID 1) måste hantera SIGTERM explicit.

**Skicka signaler till fel process**
Verifiera alltid PID innan kill, särskilt med kill -9.

------------------------------------------------------------

## Övningar

### Övning 1: Graceful Shutdown
<details>
<summary>Visa övning</summary>

**Uppgift:** Implementera och testa graceful shutdown.

**Steg:**
1. Skapa ett script med trap för SIGTERM
2. Starta scriptet i bakgrunden
3. Skicka SIGTERM och observera cleanup
4. Jämför med SIGKILL

**Lösning:**
```bash
# Skapa script
cat > /tmp/graceful.sh << 'EOF'
#!/bin/bash
TEMPFILE=$(mktemp)
echo "Started with PID $$, temp: $TEMPFILE"

cleanup() {
    echo "Cleanup: removing $TEMPFILE"
    rm -f "$TEMPFILE"
    echo "Graceful shutdown complete"
    exit 0
}

trap cleanup SIGTERM

while true; do
    echo "Working..."
    sleep 2
done
EOF
chmod +x /tmp/graceful.sh

# Testa graceful (SIGTERM)
/tmp/graceful.sh &
PID=$!
sleep 3
kill -TERM $PID
# Observera cleanup-meddelanden

# Testa force (SIGKILL) - skapa nytt
/tmp/graceful.sh &
PID=$!
sleep 3
kill -9 $PID
# Ingen cleanup sker, temp-fil finns kvar
ls /tmp/tmp.*
```
</details>

### Övning 2: Configuration Reload
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa ett script som laddar om konfiguration vid SIGHUP.

**Steg:**
1. Skapa ett script som läser en config-fil
2. Implementera SIGHUP-handler som läser om filen
3. Ändra config och skicka SIGHUP
4. Verifiera att nya värden används

**Lösning:**
```bash
# Skapa config
echo 'GREETING="Hello"' > /tmp/myconfig

# Skapa script
cat > /tmp/reloadable.sh << 'EOF'
#!/bin/bash
CONFIG_FILE="/tmp/myconfig"

load_config() {
    echo "Loading config from $CONFIG_FILE..."
    source "$CONFIG_FILE"
    echo "Config loaded: GREETING=$GREETING"
}

handle_hup() {
    echo "SIGHUP received, reloading..."
    load_config
}

trap handle_hup SIGHUP

load_config

echo "Running (PID $$), send SIGHUP to reload"
while true; do
    echo "Current greeting: $GREETING"
    sleep 5
done
EOF
chmod +x /tmp/reloadable.sh

# Kör
/tmp/reloadable.sh &
PID=$!

# Ändra config
sleep 3
echo 'GREETING="Hejsan"' > /tmp/myconfig

# Skicka SIGHUP
kill -HUP $PID

# Observera nya värdet
sleep 5
kill $PID
```
</details>

### Övning 3: Multi-Signal Handler
<details>
<summary>Visa övning</summary>

**Uppgift:** Skapa ett script som hanterar flera signaler olika.

**Krav:**
- SIGTERM: Graceful shutdown
- SIGHUP: Reload config
- SIGUSR1: Dumpa status
- SIGUSR2: Rotera loggfil

**Lösning:**
```bash
cat > /tmp/multisignal.sh << 'EOF'
#!/bin/bash

LOGFILE="/tmp/multisignal.log"
REQUEST_COUNT=0

handle_term() {
    echo "SIGTERM: Shutting down..."
    echo "Total requests processed: $REQUEST_COUNT"
    exit 0
}

handle_hup() {
    echo "SIGHUP: Reloading configuration..."
    # Simulera config reload
    echo "Configuration reloaded at $(date)"
}

handle_usr1() {
    echo "SIGUSR1: Status dump"
    echo "  PID: $$"
    echo "  Uptime: $SECONDS seconds"
    echo "  Requests: $REQUEST_COUNT"
}

handle_usr2() {
    echo "SIGUSR2: Rotating log..."
    mv "$LOGFILE" "${LOGFILE}.old"
    touch "$LOGFILE"
    echo "Log rotated at $(date)"
}

trap handle_term SIGTERM SIGINT
trap handle_hup SIGHUP
trap handle_usr1 SIGUSR1
trap handle_usr2 SIGUSR2

echo "Multi-signal handler (PID $$)"
echo "Commands:"
echo "  kill -TERM $$  # Shutdown"
echo "  kill -HUP $$   # Reload"
echo "  kill -USR1 $$  # Status"
echo "  kill -USR2 $$  # Rotate log"

while true; do
    ((REQUEST_COUNT++))
    echo "Processing request $REQUEST_COUNT..." >> "$LOGFILE"
    sleep 2
done
EOF
chmod +x /tmp/multisignal.sh

# Testa
/tmp/multisignal.sh &
PID=$!

sleep 3
kill -USR1 $PID  # Status
sleep 2
kill -USR2 $PID  # Rotate
sleep 2
kill -HUP $PID   # Reload
sleep 2
kill -TERM $PID  # Shutdown
```
</details>

------------------------------------------------------------

## Kopplingar

**Föregående noder:**
- Process Lifecycle and States - processgrunder
- Job Control - SIGHUP vid logout

**Relaterade noder:**
- Process Monitoring - identifiera processer att signalera
- Systemd Services - modern tjänstehantering

**Kommande noder:**
- Container Signals - signaler i Docker/Kubernetes
- Application Logging - logrotation med SIGHUP

------------------------------------------------------------

## Sammanfattning

Signaler är Linux-kärnans inter-process kommunikation för att styra processer. De viktigaste signalerna för DevOps är SIGTERM (graceful shutdown), SIGKILL (force kill), SIGHUP (reload config), SIGINT (Ctrl+C), och SIGSTOP/SIGCONT (pause/resume).

Alltid använd SIGTERM före SIGKILL - ge processer chans att städa upp, spara data och stänga anslutningar. SIGKILL ska vara sista utväg då det inte kan fångas och orsakar dirty termination.

SIGHUP har evolution från "terminal hangup" till "reload configuration" för daemons. Många tjänster (nginx, sshd, apache) stödjer SIGHUP för att ladda om config utan restart.

trap i bash-scripts låter dig definiera handlers för att fånga signaler och köra cleanup-kod, vilket är kritiskt för robusta scripts.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `kill PID` | Skicka SIGTERM (default) |
| `kill -9 PID` | Skicka SIGKILL (force) |
| `kill -HUP PID` | Skicka SIGHUP (reload) |
| `kill -l` | Lista alla signaler |
| `killall name` | Döda alla med processnamn |
| `pkill pattern` | Döda matchande processer |
| `pkill -f pattern` | Matcha hela kommandoraden |
| `pgrep pattern` | Hitta matchande PIDs |
| `trap handler SIGNAL` | Fånga signal i script |
| `kill -0 PID` | Testa om process finns |

------------------------------------------------------------

## Referenser

- Linux man pages: signal(7), kill(1), trap(1)
- POSIX Signal Handling
- "The Linux Programming Interface" - Kerrisk
- Linux Kernel Documentation - Signals
- Bash Reference Manual - Signals
""",
        },
        {
            "title": 'Process Monitoring (ps, top, htop)',
            "slug": 'process-monitoring',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Process Monitoring (ps, top, htop)

------------------------------------------------------------

## Introduktion

Processovervakning ar en av de mest fundamentala fardigheterna for alla som arbetar med Linux-system. Oavsett om du ar systemadministrator, DevOps-ingenjor eller utvecklare kommer du regelbundet behova analysera vilka processer som konsumerar systemresurser.

I en produktionsmiljo kan en enda process som skenar ivag med CPU- eller minnesanvandning paverka tusentals anvandare. Forsta hur du snabbt identifierar och diagnostiserar problemprocesser ar skillnaden mellan minuters och timmars nedtid. Verktygen ps, top och htop ar dina forsta forsvarslinjer vid prestandaproblem.

Nar en server borjar svara langsamt ar din forsta instinkt att kolla processerna. Ar det en databas som ater minne? En webserver med for manga arbetare? Ett script som loopar oandligt? Processovervakning ger svaren.

------------------------------------------------------------

## Teori

### Processmodellen i Linux

Varje program som kor pa Linux ar en process med ett unikt Process ID (PID). Kernel schemalagger dessa processer for att dela CPU-tid, och varje process har sin egen minnesrymd.

```
                    Linux Process Model
    +--------------------------------------------------+
    |                    Kernel                        |
    |  +--------------------------------------------+  |
    |  |            Process Scheduler               |  |
    |  |                                            |  |
    |  |   CPU Time    Memory    I/O    Signals    |  |
    |  +--------------------------------------------+  |
    +--------------------------------------------------+
              |              |              |
         +--------+    +--------+    +--------+
         | PID 1  |    | PID 234|    | PID 567|
         | init   |    | nginx  |    | python |
         +--------+    +--------+    +--------+
              |
    +---------+---------+
    |                   |
+--------+         +--------+
| PID 45 |         | PID 46 |
| sshd   |         | cron   |
+--------+         +--------+
```

### Process States

Processer befinner sig alltid i ett av flera tillstand:

```
+-------+     +--------+     +---------+
|  New  | --> |  Ready | --> | Running |
+-------+     +--------+     +---------+
                  ^              |
                  |              v
              +--------+    +----------+
              | Waiting| <--| Sleeping |
              +--------+    +----------+
                               |
                               v
                          +---------+
                          | Zombie  |
                          +---------+
                               |
                               v
                         +----------+
                         |Terminated|
                         +----------+
```

### Resursmetriker att overvaka

| Metrik | Beskrivning | Varningsniva |
|--------|-------------|--------------|
| %CPU | Processoranvandning | >80% sustained |
| %MEM | Minnesanvandning | >90% av RAM |
| RSS | Resident Set Size (fysiskt minne) | Ovantat hogt |
| VSZ | Virtual Memory Size | Oftast hogre an RSS |
| STAT | Process state | D (uninterruptible) |
| TIME | Total CPU-tid | Ovantat hog |

### Load Average forklarat

Load average visar genomsnittligt antal processer som vantar pa CPU-tid.

```
$ uptime
 14:23:45 up 30 days, load average: 1.50, 2.10, 1.80
                                     |     |     |
                                  1 min  5 min  15 min

Tumregel:
- Load < antal CPU-karnor = Bra
- Load = antal CPU-karnor = Maxkapacitet
- Load > antal CPU-karnor = Overbelastat

Exempel (4-karnig server):
- Load 2.0 = 50% kapacitet anvands
- Load 4.0 = 100% kapacitet
- Load 8.0 = Ko pa 4 processer
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Grundlaggande processlistning med ps

```bash
# Visa alla processer i user-friendly format
ps aux

# Forsta outputen:
# USER       PID %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
# root         1  0.0  0.1 169584 13256 ?   Ss   Jan01   2:45 /sbin/init

# Forklaring av STAT-kolumnen:
# S = Sleeping (vantar pa input)
# R = Running (aktiv)
# D = Uninterruptible sleep (vantar pa I/O)
# Z = Zombie (avslutad men inte rensad)
# T = Stopped (pausad)
# + = Foreground process
# s = Session leader
# l = Multi-threaded
```

### Steg 2: Filtrera och sortera processer

```bash
# Hitta processer som anvander mest CPU
ps aux --sort=-%cpu | head -10

# Hitta processer som anvander mest minne
ps aux --sort=-%mem | head -10

# Sok efter specifik process
ps aux | grep nginx
ps aux | grep -E "nginx|apache"

# Visa bara PID och kommando
ps -eo pid,cmd | grep python

# Visa processer for specifik anvandare
ps -u www-data

# Visa processer i tradformat
ps auxf
```

### Steg 3: Realtidsovervakning med top

```bash
# Starta top
top

# Top-granssnitt:
# +----------------------------------------------------------+
# | top - 14:30:00 up 5 days, 2 users, load average: 0.5,0.4 |
# | Tasks: 156 total, 1 running, 155 sleeping, 0 stopped     |
# | %Cpu(s): 5.0 us, 2.0 sy, 0.0 ni, 92.0 id, 1.0 wa        |
# | MiB Mem:  7976.4 total, 2345.6 free, 3456.7 used        |
# | MiB Swap: 2048.0 total, 2048.0 free, 0.0 used           |
# |                                                          |
# |  PID USER     PR  NI VIRT   RES   SHR S %CPU %MEM   CMD  |
# | 1234 www-data 20   0 450M  120M   45M S  5.0  1.5 nginx  |
# +----------------------------------------------------------+

# Kortkommandon i top:
# P - Sortera pa CPU
# M - Sortera pa minne
# k - Doda process (ange PID)
# r - Renice process
# 1 - Visa alla CPU-karnor
# c - Visa fullstandigt kommando
# q - Avsluta
```

### Steg 4: Batch mode for scripting

```bash
# Kora top en gang (for scripts)
top -bn1 | head -20

# Spara top-output till fil
top -bn1 > /var/log/top_snapshot.txt

# Automatisk overvakning var 5:e sekund, 10 ganger
top -bn10 -d5 | grep nginx >> /var/log/nginx_cpu.log
```

### Steg 5: Htop - det moderna alternativet

```bash
# Installera htop
sudo apt update && sudo apt install htop  # Ubuntu/Debian
sudo yum install htop                       # RHEL/CentOS

# Starta htop
htop

# Htop-funktioner:
# F1 - Hjalp
# F2 - Setup (konfigurera visning)
# F3 - Sok efter process
# F4 - Filter (visa bara matchande)
# F5 - Tradvy (tree view)
# F6 - Sortering
# F9 - Doda process
# F10 - Avsluta

# Htop for specifik anvandare
htop -u www-data

# Htop med PID-filter
htop -p 1234,5678
```

### Steg 6: Hitta processer med pgrep och pkill

```bash
# Hitta PID for process
pgrep nginx
# Output: 1234
#         1235

# Hitta med mer detaljer
pgrep -a nginx
# Output: 1234 nginx: master process
#         1235 nginx: worker process

# Sok i hela kommandoraden
pgrep -f "python manage.py"

# Lista processer for en anvandare
pgrep -u www-data

# Rakna antal matchande processer
pgrep -c nginx
```

### Steg 7: Identifiera oppna filer och portar med lsof

```bash
# Vilken process lyssnar pa port 80?
sudo lsof -i :80
# Output:
# COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# nginx   1234 www-data    6u  IPv4  12345      0t0  TCP *:http

# Vilka portar anvander nginx?
sudo lsof -i -P -n | grep nginx

# Vilka filer har process 1234 oppna?
sudo lsof -p 1234

# Vem anvander en specifik fil?
sudo lsof /var/log/nginx/access.log

# Hitta processer som anvander en katalog
sudo lsof +D /var/www/
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Servern ar langsam - fullstandig felsokningsprocess

```bash
#!/bin/bash
# performance_check.sh - Snabb prestandadiagnostik

echo "=== System Performance Check ==="
echo ""

# 1. Kolla load average
echo "--- Load Average ---"
uptime
echo ""

# 2. CPU-info
echo "--- Top 5 CPU Consumers ---"
ps aux --sort=-%cpu | head -6
echo ""

# 3. Minne
echo "--- Memory Usage ---"
free -h
echo ""

# 4. Top minnesanvandare
echo "--- Top 5 Memory Consumers ---"
ps aux --sort=-%mem | head -6
echo ""

# 5. Disk I/O
echo "--- Disk Usage ---"
df -h | grep -E "^/dev|Filesystem"
echo ""

# 6. Processer i D-state (vantar pa I/O)
echo "--- Processes in D-state (I/O wait) ---"
ps aux | awk '$8 ~ /D/'
```

### Scenario 2: Hitta en minneslacka

```bash
# Overvaka minnesanvandning over tid
while true; do
    echo "$(date): $(ps aux --sort=-%mem | head -2 | tail -1 | awk '{print $4"%", $11}')"
    sleep 60
done >> /var/log/memory_watch.log

# Analysera minnesanvandning for specifik process
watch -n 5 "ps -p \$(pgrep python) -o pid,%mem,rss,vsz,cmd"

# Hitta processer som vaxer
for i in {1..10}; do
    ps aux --sort=-%mem | head -5
    echo "---"
    sleep 60
done
```

### Scenario 3: Port redan i bruk

```bash
# Problemet: "Address already in use" vid start
# Error: bind(): Address already in use

# Hitta vad som anvander porten
sudo lsof -i :3000

# Detaljerad info
sudo ss -tulnp | grep 3000

# Om det ar en gammal process, doda den
sudo fuser -k 3000/tcp

# Eller mer forsiktigt
PID=$(sudo lsof -t -i :3000)
if [ -n "$PID" ]; then
    echo "Killing process $PID"
    sudo kill $PID
    sleep 2
    # Om den inte dog, tving
    sudo kill -9 $PID 2>/dev/null
fi
```

### Scenario 4: Skapa process monitoring script

```bash
#!/bin/bash
# process_monitor.sh - Overvaka kritiska processer

PROCESSES=("nginx" "postgres" "redis-server")
ALERT_EMAIL="admin@example.com"
LOG_FILE="/var/log/process_monitor.log"

check_process() {
    local process=$1
    if ! pgrep -x "$process" > /dev/null; then
        echo "$(date): ALERT - $process is not running!" | tee -a "$LOG_FILE"
        echo "$process crashed on $(hostname)" | mail -s "Process Alert" "$ALERT_EMAIL"
        return 1
    fi
    return 0
}

echo "$(date): Starting process check" >> "$LOG_FILE"

for proc in "${PROCESSES[@]}"; do
    if check_process "$proc"; then
        echo "$(date): $proc OK" >> "$LOG_FILE"
    fi
done
```

------------------------------------------------------------

## Bästa Praxis

### 1. Anvand ratt verktyg for ratten situation

```
Situation                    Verktyg
-----------------------------------------
Snabb ogonblicksbild    --> ps aux
Realtidsovervakning     --> top/htop
Scripting               --> top -bn1
Hitta PID               --> pgrep
Port-problem            --> lsof -i
Interaktiv felsok       --> htop
```

### 2. Satt upp proaktiv overvakning

```bash
# Cron-jobb for att logga resursanvandning
# Lagg till i crontab -e:
*/5 * * * * /usr/local/bin/performance_check.sh >> /var/log/perf.log 2>&1

# Alert nar load ar for hog
*/1 * * * * [ $(cat /proc/loadavg | cut -d. -f1) -gt 4 ] && echo "High load" | mail -s "Alert" admin@example.com
```

### 3. Dokumentera normala varden

```bash
# Spara baseline for jamforelse
top -bn1 > /var/log/baseline/top_$(date +%Y%m%d).txt
ps aux > /var/log/baseline/ps_$(date +%Y%m%d).txt

# Jamfor med tidigare
diff /var/log/baseline/ps_yesterday.txt /var/log/baseline/ps_today.txt
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                    MISSTAG ATT UNDVIKA                         |
+----------------------------------------------------------------+
|                                                                |
|  1. Forvirrar VSZ med RSS                                     |
|     VSZ = virtuellt minne (kan vara enormt)                   |
|     RSS = faktiskt fysiskt minne (det som matters)            |
|                                                                |
|  2. Ignorerar zombie-processer                                |
|     Z-state processer atar inte resurser men indikerar        |
|     problem med parent-processen                              |
|                                                                |
|  3. Dolda kolumner i ps                                       |
|     Kommando kan vara trunkerat - anvand ps auxww             |
|                                                                |
|  4. Glommer sudo med lsof                                     |
|     Utan sudo ser du bara dina egna processer                 |
|                                                                |
|  5. Missforstar load average                                  |
|     Load 4.0 pa 8-karnig maskin ar bra                       |
|     Load 4.0 pa 2-karnig maskin ar daligt                    |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Hitta resurstjuvar

<details>
<summary>Visa losning</summary>

```bash
# Uppgift: Hitta de 5 processer som anvander mest CPU och minne

# CPU-toppen
echo "=== Top 5 CPU ==="
ps aux --sort=-%cpu | head -6

# Minnes-toppen
echo "=== Top 5 Memory ==="
ps aux --sort=-%mem | head -6

# Kombinerat i ett kommando
echo "=== Top 5 CPU + Memory combined ==="
ps aux --sort=-%cpu,%mem | head -6

# Med htop (interaktivt)
# Starta htop, tryck F6 och valj PERCENT_CPU
```

</details>

### Ovning 2: Overvaka specifik applikation

<details>
<summary>Visa losning</summary>

```bash
# Uppgift: Overvaka nginx-processernas resursanvandning

# Hitta alla nginx-processer
pgrep -a nginx

# Realtidsovervakning av nginx
watch -n 2 "ps aux | grep [n]ginx"

# Detaljerad minnesinfo
ps -p $(pgrep nginx | tr '\n' ',') -o pid,%cpu,%mem,rss,vsz,cmd

# Logga over tid
while true; do
    echo "$(date)"
    ps aux | grep [n]ginx
    echo "---"
    sleep 30
done >> /var/log/nginx_monitor.log
```

</details>

### Ovning 3: Diagnostisera port-konflikt

<details>
<summary>Visa losning</summary>

```bash
# Uppgift: Applikation kan inte starta pa port 8080

# Steg 1: Vad anvander porten?
sudo lsof -i :8080

# Steg 2: Mer info om processen
sudo ss -tulnp | grep 8080

# Steg 3: Om du behover doda processen
PID=$(sudo lsof -t -i :8080)
echo "Process using port 8080: $PID"

# Steg 4: Verifiera forst vad det ar
ps aux | grep $PID

# Steg 5: Doda om sakert
sudo kill $PID

# Steg 6: Verifiera att porten ar fri
sudo lsof -i :8080  # Bor ge tom output
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Signals | Skicka signaler till processer du hittar |
| Systemd | Hantera tjanster istallet for manuella processer |
| Cgroups | Begransar resurser for processgrupper |
| Logging | Kombinera med logganalys for fullstandig bild |

------------------------------------------------------------

## Sammanfattning

Processovervakning ar din forstaforsvarslinje vid prestandaproblem. Med ps far du ogonblicksbilder, med top/htop realtidsovervakning, och med lsof hittar du vad som anvander portar och filer. Kom ihag att alltid jamfora med baseline-varden och att load average ska tolkas relativt antalet CPU-karnor.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ps aux` | Lista alla processer |
| `ps aux --sort=-%cpu` | Sortera pa CPU |
| `ps aux --sort=-%mem` | Sortera pa minne |
| `top` | Realtidsovervakning |
| `top -bn1` | Batch mode for scripts |
| `htop` | Modern interaktiv overvakare |
| `pgrep processnamn` | Hitta PID |
| `pgrep -a processnamn` | PID med full kommandorad |
| `lsof -i :port` | Hitta vad som anvander port |
| `lsof -p PID` | Oppna filer for process |
| `uptime` | Visa load average |
| `free -h` | Visa minnesanvandning |

------------------------------------------------------------

## Referenser

- Linux man pages: ps(1), top(1), htop(1), lsof(8), pgrep(1)
- https://man7.org/linux/man-pages/man1/ps.1.html
- https://man7.org/linux/man-pages/man1/top.1.html
- https://htop.dev/
- Linux Performance (Brendan Gregg)
""",
        },
        {
            "title": 'Systemd Architecture',
            "slug": 'systemd-architecture',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Systemd Architecture

------------------------------------------------------------

## Introduktion

Systemd ar det moderna init-systemet som har blivit standard i praktiskt taget alla stora Linux-distributioner. Som PID 1 ar systemd den forsta processen som startar och den ansvarar for att starta och hantera alla andra processer och tjanster pa systemet.

For DevOps-ingenjorer ar systemd avgonrande. Varje gang du deployar en applikation, konfigurerar en server eller felsoker varfor en tjanst inte startar kommer du att interagera med systemd. Att forsta dess arkitektur - units, dependencies, targets och cgroups - ar grundlaggande for effektiv Linux-administration.

Systemd ersatte aldre init-system som SysVinit och Upstart genom att erbjuda parallell uppstart, on-demand aktivering, automatisk beroendehantering och integrerad loggning. Denna kunskap ar oumbärlig i moderna Linux-miljöer.

------------------------------------------------------------

## Teori

### Systemd som PID 1

Nar Linux-kärnan startar skapar den den forsta processen - PID 1 - som sedan ansvarar for att starta alla andra processer.

```
Boot Process:
+------------------+
|     BIOS/UEFI    |
+--------+---------+
         |
+--------v---------+
|   Bootloader     |
|   (GRUB)         |
+--------+---------+
         |
+--------v---------+
|   Linux Kernel   |
+--------+---------+
         |
+--------v---------+
|   systemd        |  <-- PID 1
|   (init system)  |
+--------+---------+
         |
    +----+----+----+----+
    |    |    |    |    |
  nginx  ssh  cron postgres ...
```

### Units - byggstenar i systemd

Allt i systemd ar organiserat som "units" - konfigurationsfiler som beskriver resurser att hantera:

```
Systemd Unit Types:
+----------------------------------------------------------+
|  .service  - Tjanster (nginx, postgres, din app)         |
|  .socket   - Nätverks- eller IPC-sockets                 |
|  .timer    - Schemalagda jobb (modern cron)              |
|  .target   - Grupper av units (boot stages)              |
|  .mount    - Filsystem mount points                      |
|  .device   - Kernel devices                              |
|  .path     - Filsystem path monitoring                   |
|  .slice    - Cgroup resource management                  |
+----------------------------------------------------------+
```

### Dependency Management

Systemd hanterar automatiskt i vilken ordning units startar baserat pa deklarerade beroenden:

```
Dependency Types:
                    +-------------+
                    |   network   |
                    |   .target   |
                    +------+------+
                           |
           +---------------+---------------+
           |               |               |
     +-----v-----+   +-----v-----+   +-----v-----+
     |  nginx    |   | postgres  |   |   sshd    |
     | .service  |   | .service  |   | .service  |
     +-----------+   +-----+-----+   +-----------+
                           |
                     +-----v-----+
                     |  myapp    |
                     | .service  |
                     |After=     |
                     |postgres   |
                     +-----------+

Relationship Directives:
- After/Before  = Ordning (om bada startar)
- Requires      = Hard dependency (misslyckas om dep. misslyckas)
- Wants         = Soft dependency (fortsatter aven om dep. misslyckas)
- BindsTo       = Starkare an Requires (stoppar om dep. stoppar)
```

### Targets - boot stages

Targets ar grupper av units som representerar systemtillstand:

```
Target Hierarchy:
+-----------------------------------------------------------------+
|                                                                 |
|  emergency.target --> rescue.target --> multi-user.target      |
|        |                   |                    |               |
|   Minimal shell       Single user         Full system          |
|   Only root           Limited services    All services         |
|                                                 |               |
|                                                 v               |
|                                         graphical.target        |
|                                         (Desktop environment)   |
+-----------------------------------------------------------------+
```

### Cgroups integration

Systemd anvander Linux cgroups for att isolera och begränsa resurser per tjanst:

```
Cgroup Hierarchy:
/
├── user.slice/         # User sessions
│   └── user-1000.slice
├── system.slice/       # System services
│   ├── nginx.service
│   ├── postgres.service
│   └── sshd.service
└── machine.slice/      # Containers/VMs
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Utforska systemd status

```bash
# Verifiera att systemd ar PID 1
ps -p 1 -o comm=
# Output: systemd

# Systemd version och features
systemd --version

# Aktuell systemstatus
systemctl status
# Visar: State, Jobs, Failed, Since
```

### Steg 2: Lista och filtrera units

```bash
# Lista alla laddade units
systemctl list-units

# Endast services
systemctl list-units --type=service

# Endast aktiva services
systemctl list-units --type=service --state=running

# Misslyckade units
systemctl list-units --failed

# Alla installerade unit-filer
systemctl list-unit-files

# Filtera pa enabled
systemctl list-unit-files --state=enabled
```

### Steg 3: Forsta unit-filernas plats

```bash
# Var unit-filer finns (prioritetsordning):
# 1. /etc/systemd/system/    - Admin/lokala overrides (hogst prio)
# 2. /run/systemd/system/    - Runtime-genererade
# 3. /lib/systemd/system/    - Paketinstallerade (ror ej!)

# Hitta var en specifik unit kommer fran
systemctl show nginx --property=FragmentPath

# Visa unit-filens innehall
systemctl cat nginx

# Lista alla filer som paverkar en unit
systemctl show nginx --property=DropInPaths
```

### Steg 4: Analysera dependencies

```bash
# Se vad en unit beror pa
systemctl list-dependencies nginx

# Reverse - vad beror pa denna unit?
systemctl list-dependencies nginx --reverse

# Endast Wants-dependencies
systemctl list-dependencies nginx --type=wants

# Grafisk dependency-visualisering
systemd-analyze dot nginx.service | dot -Tsvg > deps.svg
```

### Steg 5: Forsta targets

```bash
# Se aktuellt default target
systemctl get-default
# Output: multi-user.target (server) eller graphical.target (desktop)

# Se alla targets
systemctl list-units --type=target

# Se vad som ingar i ett target
systemctl list-dependencies multi-user.target

# Andra default target
sudo systemctl set-default multi-user.target
```

### Steg 6: Cgroups och resursovervakning

```bash
# Se cgroup-hierarkin for services
systemd-cgls

# Realtids resursanvandning per service
systemd-cgtop

# Detaljerad info om en service's cgroup
systemctl show nginx --property=ControlGroup
systemctl show nginx --property=MemoryCurrent,CPUUsageNSec
```

### Steg 7: Boot-analys

```bash
# Total boot-tid
systemd-analyze

# Tid per service
systemd-analyze blame

# Kritisk boot-kedja
systemd-analyze critical-chain

# Grafisk boot-timeline
systemd-analyze plot > boot.svg
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Felsoka varfor en tjanst inte startar

```bash
#!/bin/bash
# debug_service.sh - Felsok en service

SERVICE=${1:-nginx}

echo "=== Debugging $SERVICE ==="
echo ""

# 1. Aktuell status
echo "--- Status ---"
systemctl status $SERVICE

# 2. Dependencies
echo ""
echo "--- Dependencies ---"
systemctl list-dependencies $SERVICE

# 3. Senaste loggar
echo ""
echo "--- Recent logs ---"
journalctl -u $SERVICE -n 20 --no-pager

# 4. Unit-fil
echo ""
echo "--- Unit file ---"
systemctl cat $SERVICE

# 5. Property check
echo ""
echo "--- Key properties ---"
systemctl show $SERVICE --property=ActiveState,SubState,UnitFileState
```

### Scenario 2: Skapa en dependency-kedja

```bash
# Scenario: myapp beror pa postgres och redis

# 1. Skapa app service
sudo cat > /etc/systemd/system/myapp.service << 'EOF'
[Unit]
Description=My Application
After=network.target postgresql.service redis.service
Requires=postgresql.service
Wants=redis.service

[Service]
Type=simple
User=myapp
ExecStart=/opt/myapp/bin/server
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# 2. Reload och verifiera
sudo systemctl daemon-reload
systemctl list-dependencies myapp

# 3. Starta - postgres kommer starta automatiskt
sudo systemctl start myapp
```

### Scenario 3: Boot-optimering

```bash
# Hitta langsamma services
systemd-analyze blame | head -10

# Hitta kritiska kedjor
systemd-analyze critical-chain

# Exempel output analys:
# graphical.target @20.5s
# └─multi-user.target @20.5s
#   └─nginx.service @19.2s +1.3s
#     └─network-online.target @19.1s
#       └─NetworkManager-wait-online.service @4.2s +14.9s

# NetworkManager-wait-online ar langsammast - kan den paralleliseras?
```

------------------------------------------------------------

## Bästa Praxis

### 1. Unit file organisation

```bash
# Lokala overrides - skapa drop-in istallet for att redigera original
sudo systemctl edit nginx
# Skapar /etc/systemd/system/nginx.service.d/override.conf

# Innehall av override:
[Service]
LimitNOFILE=65536
Environment="NGINX_WORKER_PROCESSES=auto"
```

### 2. Documentation i units

```ini
[Unit]
Description=Production Web Server
Documentation=https://wiki.example.com/nginx
Documentation=man:nginx(8)
```

### 3. Hardening

```ini
[Service]
# Security hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadOnlyPaths=/etc
ReadWritePaths=/var/log/myapp
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+---------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                         |
+---------------------------------------------------------------+
|                                                               |
|  1. Glommer daemon-reload                                    |
|     ALLTID: sudo systemctl daemon-reload                     |
|     efter att ha andrat unit-filer                           |
|                                                               |
|  2. Redigerar filer i /lib/systemd/system/                  |
|     Dessa skrivs over vid paketuppdateringar!               |
|     Anvand /etc/systemd/system/ eller drop-ins              |
|                                                               |
|  3. Forvirrar After med Requires                            |
|     After = ordning (om bada startar)                       |
|     Requires = starta dependency                            |
|     Oftast behovs bada: After=X och Requires=X              |
|                                                               |
|  4. Felaktig Type=                                          |
|     Type=simple for processer som stannar i forgund        |
|     Type=forking for daemoniserande processer              |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Utforska ditt systems arkitektur

<details>
<summary>Visa losning</summary>

```bash
# 1. Hur manga services kor?
systemctl list-units --type=service --state=running | wc -l

# 2. Vilka targets ar aktiva?
systemctl list-units --type=target --state=active

# 3. Se boot-tiden
systemd-analyze

# 4. Topp 5 langsamma services
systemd-analyze blame | head -5

# 5. Visualisera cgroup-hierarkin
systemd-cgls
```

</details>

### Ovning 2: Analysera dependencies

<details>
<summary>Visa losning</summary>

```bash
# Valj en kritisk service, t.ex. sshd
SERVICE=sshd

# Se vad den beror pa
echo "=== $SERVICE depends on: ==="
systemctl list-dependencies $SERVICE

# Se vad som beror pa den
echo "=== Depends on $SERVICE: ==="
systemctl list-dependencies $SERVICE --reverse

# Se unit-filen
echo "=== Unit file: ==="
systemctl cat $SERVICE

# Hitta After= och Requires= directives
systemctl show $SERVICE --property=After,Requires,Wants
```

</details>

### Ovning 3: Boot-analys

<details>
<summary>Visa losning</summary>

```bash
# Fullstandig boot-analys

# 1. Total tid
echo "=== Boot time ==="
systemd-analyze

# 2. Per-service breakdown
echo "=== Blame (slowest first) ==="
systemd-analyze blame | head -10

# 3. Kritisk kedja
echo "=== Critical chain ==="
systemd-analyze critical-chain

# 4. Exportera grafisk timeline
systemd-analyze plot > /tmp/boot.svg
echo "Boot timeline saved to /tmp/boot.svg"
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Unit Files | Nasta nod - skriva egna services |
| Journald | Systemd's integrerade loggning |
| Cgroups | Resursbegransning for containers |
| Boot Process | Forsta uppstartssekvensen |

------------------------------------------------------------

## Sammanfattning

Systemd ar ryggraden i moderna Linux-system. Som PID 1 ansvarar det for att starta och hantera alla processer. Units ar byggblocken - services, timers, targets - som konfigureras genom deklarativa filer. Dependencies hanteras automatiskt med After/Requires/Wants. Targets grupperar units i boot stages. Cgroups ger resursisolering. Kom alltid ihag daemon-reload efter andringar!

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `systemctl status` | Systemstatus |
| `systemctl list-units` | Lista units |
| `systemctl list-units --failed` | Misslyckade units |
| `systemctl list-dependencies X` | Dependencies for X |
| `systemctl cat X` | Visa unit-fil |
| `systemctl show X --property=Y` | Visa specifik property |
| `systemctl get-default` | Default target |
| `systemd-cgls` | Cgroup-hierarki |
| `systemd-cgtop` | Cgroup resursanvandning |
| `systemd-analyze` | Boot-tid |
| `systemd-analyze blame` | Per-service boot-tid |

------------------------------------------------------------

## Referenser

- systemd.io - Official documentation
- man systemd(1), systemctl(1)
- https://www.freedesktop.org/wiki/Software/systemd/
- Lennart Poettering's systemd blog posts
- Red Hat System Administrator's Guide - Managing Services with systemd
""",
        },
        {
            "title": 'Unit Files (service, timer, socket)',
            "slug": 'unit-files',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Unit Files (service, timer, socket)

------------------------------------------------------------

## Introduktion

Unit-filer ar konfigurationsfiler som talar om for systemd hur tjanster, timers och sockets ska hanteras. De ar det moderna sattet att hantera allt fran webbservrar till schemalagda jobb, och ersatter aldre tekniker som SysV init-scripts och cron.

For DevOps-ingenjorer ar unit-filer vardagsmat. Varje applikation du deployar behover troligen en service-fil for att kora som en hanterad tjanst. Varje schemalagt jobb kan implementeras som en timer. Socket activation mojliggor on-demand start av tjanster.

Att beharska unit-filernas syntax och struktur ar fundamentalt for att bygga pålitliga, sjalvlakande system dar tjanster automatiskt startar vid boot, startar om vid krasch, och hanterar resurser korrekt.

------------------------------------------------------------

## Teori

### Unit-filens tre sektioner

Varje unit-fil bestar av tre huvudsektioner:

```
Unit File Structure:
+----------------------------------------------------------+
|  [Unit]                                                   |
|  - Description, Documentation                             |
|  - Dependencies (After, Requires, Wants)                  |
|  - Conditions and Assertions                              |
+----------------------------------------------------------+
|  [Service/Timer/Socket/...]                               |
|  - Type-specifik konfiguration                           |
|  - For services: Type, ExecStart, Restart                |
|  - For timers: OnCalendar, OnBootSec                     |
|  - For sockets: ListenStream, Accept                     |
+----------------------------------------------------------+
|  [Install]                                                |
|  - WantedBy, RequiredBy                                  |
|  - Alias, Also                                           |
+----------------------------------------------------------+
```

### Service Types

Systemd behover veta hur din process beter sig:

```
Service Types:
+----------------------------------------------------------------+
|                                                                |
|  simple (default)                                              |
|  +----------------------+                                      |
|  | ExecStart startar    |                                      |
|  | huvudprocessen       |                                      |
|  | (stannar i forgund)  |                                      |
|  +----------------------+                                      |
|                                                                |
|  forking                                                       |
|  +----------------------+    +------------------+              |
|  | ExecStart startar    | -> | Daemonprocess    |              |
|  | och forkar           |    | (parent exits)   |              |
|  +----------------------+    +------------------+              |
|                                                                |
|  oneshot                                                       |
|  +----------------------+                                      |
|  | Kor en gang          |                                      |
|  | och avslutar         |                                      |
|  | (init scripts)       |                                      |
|  +----------------------+                                      |
|                                                                |
|  notify                                                        |
|  +----------------------+    +------------------+              |
|  | Som simple men       | -> | Skickar signal   |              |
|  | skickar sd_notify()  |    | nar redo         |              |
|  +----------------------+    +------------------+              |
|                                                                |
+----------------------------------------------------------------+
```

### Timer-typer

Timers kan triggas pa flera satt:

| Timer-typ | Beskrivning | Anvandning |
|-----------|-------------|------------|
| OnCalendar | Kalenderbaserad | "Kl 02:00 varje dag" |
| OnBootSec | Tid efter boot | "5 minuter efter boot" |
| OnUnitActiveSec | Tid efter senaste korning | "Var 6:e timme" |
| OnStartupSec | Tid efter systemd start | "2 min efter systemd" |

### OnCalendar-syntax

```
OnCalendar Syntax:
+----------------------------------------------------------+
|  Format: DayOfWeek Year-Month-Day Hour:Minute:Second     |
|                                                          |
|  Exempel:                                                |
|  *-*-* *:*:00          Varje minut                       |
|  *-*-* *:00:00         Varje timme                       |
|  *-*-* 02:00:00        Varje dag kl 02:00               |
|  Mon *-*-* 10:00:00    Varje mandag kl 10:00            |
|  *-*-01 00:00:00       Forsta varje manad               |
|  Mon..Fri *-*-* 09:00  Vardagar kl 09:00                |
|                                                          |
|  Specialord:                                             |
|  hourly, daily, weekly, monthly, yearly                  |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa en enkel service

```bash
# 1. Skapa service-filen
sudo nano /etc/systemd/system/myapp.service
```

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Server
Documentation=https://github.com/example/myapp
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
Environment="NODE_ENV=production"
Environment="PORT=3000"
ExecStart=/usr/bin/node /opt/myapp/server.js
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myapp

[Install]
WantedBy=multi-user.target
```

```bash
# 2. Aktivera och starta
sudo systemctl daemon-reload
sudo systemctl enable --now myapp

# 3. Verifiera
systemctl status myapp
journalctl -u myapp -f
```

### Steg 2: Service med forking daemon

```ini
# /etc/systemd/system/legacy-daemon.service
[Unit]
Description=Legacy Daemon that forks
After=network.target

[Service]
Type=forking
PIDFile=/var/run/legacy.pid
ExecStart=/opt/legacy/bin/daemon start
ExecStop=/opt/legacy/bin/daemon stop
ExecReload=/opt/legacy/bin/daemon reload
TimeoutStartSec=30
TimeoutStopSec=30
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### Steg 3: Oneshot for initialisering

```ini
# /etc/systemd/system/init-database.service
[Unit]
Description=Initialize Database Schema
After=postgresql.service
Requires=postgresql.service

[Service]
Type=oneshot
User=postgres
ExecStart=/opt/app/scripts/init-db.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

### Steg 4: Skapa timer for schemalagt jobb

```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Daily Backup Job
After=network.target

[Service]
Type=oneshot
User=backup
ExecStart=/opt/scripts/backup.sh
StandardOutput=journal
StandardError=journal
```

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Run backup daily at 02:00

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true
RandomizedDelaySec=300

[Install]
WantedBy=timers.target
```

```bash
# Aktivera timer (INTE service!)
sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer

# Lista aktiva timers
systemctl list-timers

# Testa manuellt
sudo systemctl start backup.service
```

### Steg 5: Socket activation

```ini
# /etc/systemd/system/myapp.socket
[Unit]
Description=MyApp Socket
PartOf=myapp.service

[Socket]
ListenStream=8080
Accept=no
NoDelay=true

[Install]
WantedBy=sockets.target
```

```ini
# /etc/systemd/system/myapp.service (modifierad)
[Unit]
Description=MyApp Server
Requires=myapp.socket
After=myapp.socket

[Service]
Type=simple
User=myapp
ExecStart=/opt/myapp/bin/server
StandardInput=socket

[Install]
WantedBy=multi-user.target
```

```bash
# Aktivera socket (inte service!)
sudo systemctl enable --now myapp.socket

# Service startar forst nar nagon ansluter till port 8080!
curl http://localhost:8080  # Nu startar myapp.service
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Python-applikation med Gunicorn

```ini
# /etc/systemd/system/mywebapp.service
[Unit]
Description=Gunicorn instance for MyWebApp
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/mywebapp
Environment="PATH=/var/www/mywebapp/venv/bin"
ExecStart=/var/www/mywebapp/venv/bin/gunicorn \\
    --workers 4 \\
    --bind unix:mywebapp.sock \\
    --access-logfile /var/log/mywebapp/access.log \\
    --error-logfile /var/log/mywebapp/error.log \\
    wsgi:app
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### Exempel 2: Docker container som service

```ini
# /etc/systemd/system/mycontainer.service
[Unit]
Description=My Docker Container
Requires=docker.service
After=docker.service

[Service]
Type=simple
ExecStartPre=-/usr/bin/docker stop mycontainer
ExecStartPre=-/usr/bin/docker rm mycontainer
ExecStart=/usr/bin/docker run --name mycontainer \\
    -p 8080:8080 \\
    -v /data:/data \\
    myimage:latest
ExecStop=/usr/bin/docker stop mycontainer
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Exempel 3: Log rotation timer

```ini
# /etc/systemd/system/logrotate.timer
[Unit]
Description=Rotate logs daily

[Timer]
OnCalendar=daily
Persistent=true
AccuracySec=12h

[Install]
WantedBy=timers.target
```

------------------------------------------------------------

## Bästa Praxis

### 1. Anvand drop-ins for overrides

```bash
# Istallet for att redigera originalet:
sudo systemctl edit nginx

# Skapar /etc/systemd/system/nginx.service.d/override.conf
# Innehall:
[Service]
LimitNOFILE=65536
```

### 2. Security hardening

```ini
[Service]
# Kör som icke-root
User=myapp
Group=myapp

# Security restrictions
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/log/myapp /var/lib/myapp

# Resource limits
LimitNOFILE=65536
MemoryMax=512M
CPUQuota=50%
```

### 3. Robust restart-policy

```ini
[Service]
Restart=on-failure
RestartSec=5
StartLimitIntervalSec=300
StartLimitBurst=5
# = Max 5 restarts inom 5 minuter
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+---------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                         |
+---------------------------------------------------------------+
|                                                               |
|  1. Glommer daemon-reload                                    |
|     Systemd laser inte om filer automatiskt!                 |
|     ALLTID: sudo systemctl daemon-reload                     |
|                                                               |
|  2. Fel Type=                                                |
|     simple (default): process stannar i forgund              |
|     forking: process daemoniserar (forkar)                   |
|     Fel val = tjansten ser "startad" men ar kraschad        |
|                                                               |
|  3. Absoluta sökvägar                                        |
|     ExecStart MÅSTE ha absolut path                         |
|     ExecStart=/usr/bin/node  (RATT)                         |
|     ExecStart=node           (FEL!)                         |
|                                                               |
|  4. Aktiverar timer.service istallet for timer.timer        |
|     systemctl enable backup.timer  (RATT)                   |
|     systemctl enable backup.service (FEL - kor en gang)    |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Skapa en enkel service

<details>
<summary>Visa losning</summary>

```bash
# Skapa ett enkelt script
sudo mkdir -p /opt/myservice
sudo cat > /opt/myservice/run.sh << 'EOF'
#!/bin/bash
while true; do
    echo "$(date): Service is running" >> /var/log/myservice.log
    sleep 60
done
EOF
sudo chmod +x /opt/myservice/run.sh

# Skapa service-fil
sudo cat > /etc/systemd/system/myservice.service << 'EOF'
[Unit]
Description=My Test Service

[Service]
Type=simple
ExecStart=/opt/myservice/run.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# Aktivera
sudo systemctl daemon-reload
sudo systemctl enable --now myservice
systemctl status myservice
```

</details>

### Ovning 2: Skapa en timer

<details>
<summary>Visa losning</summary>

```bash
# Skapa oneshot service
sudo cat > /etc/systemd/system/myjob.service << 'EOF'
[Unit]
Description=My Scheduled Job

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo "Job ran at $(date)" >> /var/log/myjob.log'
EOF

# Skapa timer
sudo cat > /etc/systemd/system/myjob.timer << 'EOF'
[Unit]
Description=Run myjob every 5 minutes

[Timer]
OnCalendar=*:0/5
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Aktivera timer
sudo systemctl daemon-reload
sudo systemctl enable --now myjob.timer

# Verifiera
systemctl list-timers | grep myjob
```

</details>

### Ovning 3: Konvertera cron-jobb till timer

<details>
<summary>Visa losning</summary>

```bash
# Gammalt cron-jobb: 0 2 * * * /usr/local/bin/backup.sh

# Service
sudo cat > /etc/systemd/system/backup.service << 'EOF'
[Unit]
Description=Backup Job

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
StandardOutput=journal
StandardError=journal
EOF

# Timer
sudo cat > /etc/systemd/system/backup.timer << 'EOF'
[Unit]
Description=Run backup at 02:00 daily

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Systemd Architecture | Forsta hur units hanger ihop |
| Service Management | Hantera dina services med systemctl |
| Journald | Loggar for dina services |
| Cgroups | Resursbegransning med slices |

------------------------------------------------------------

## Sammanfattning

Unit-filer ar hjärtat i systemd-konfiguration. Services definierar hur applikationer kor och hanteras, timers ersätter cron med battare kontroll och loggning, och sockets möjliggör on-demand start. Kom ihåg att alltid kora daemon-reload efter ändringar, använda rätt Type=, och aktivera timers (inte services) för schemalagda jobb.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `systemctl daemon-reload` | Läs om unit-filer |
| `systemctl enable --now X` | Enable och starta |
| `systemctl edit X` | Skapa drop-in override |
| `systemctl cat X` | Visa unit-fil |
| `systemctl list-timers` | Lista aktiva timers |
| `systemd-analyze verify X` | Validera unit-fil |
| `journalctl -u X` | Loggar för service |

------------------------------------------------------------

## Referenser

- man systemd.service, systemd.timer, systemd.socket
- https://www.freedesktop.org/software/systemd/man/
- https://wiki.archlinux.org/title/Systemd
- Red Hat documentation on systemd
""",
        },
        {
            "title": 'Service Management (systemctl)',
            "slug": 'service-management',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Service Management (systemctl)

------------------------------------------------------------

## Introduktion

Systemctl ar kommandoradsgranssnittet for att interagera med systemd - Linux moderna service manager. Varje tjanst pa ett Linux-system, fran webbservrar till databaser, hanteras genom systemctl-kommandon.

For DevOps-ingenjorer ar systemctl lika fundamentalt som git. Du kommer anvanda det flera ganger om dagen: starta tjanster efter deployment, felstoka varfor en applikation inte fungerar, konfigurera vad som startar vid boot, och overvaka systemets halsostatus.

Beharskar du systemctl kan du effektivt hantera produktionsmiljoer, automatisera service-livscykeln, och snabbt diagnostisera problem. Det ar skillnaden mellan att gissa och att veta.

------------------------------------------------------------

## Teori

### Service States

En systemd service kan befinna sig i flera tillstand:

```
Service Lifecycle:
                    +-------------+
                    |   inactive  |
                    | (stopped)   |
                    +------+------+
                           |
                    systemctl start
                           |
                    +------v------+
              +---->|   active    |<----+
              |     | (running)   |     |
              |     +------+------+     |
              |            |            |
        systemctl     systemctl    systemctl
         restart        stop        reload
              |            |            |
              |     +------v------+     |
              +-----+   inactive  |-----+
                    | (stopped)   |
                    +-------------+

Special States:
+-------------+  +-------------+  +-------------+
|  activating |  | deactivating|  |   failed    |
| (starting)  |  | (stopping)  |  |  (crashed)  |
+-------------+  +-------------+  +-------------+
```

### Enable vs Start

Det ar kritiskt att forsta skillnaden:

```
Enable vs Start:
+----------------------------------------------------------------+
|                                                                |
|  systemctl start nginx                                         |
|  - Startar nginx NU                                           |
|  - Effekt: Omedelbar                                          |
|  - Persistence: Forsvinner vid reboot                         |
|                                                                |
|  systemctl enable nginx                                        |
|  - Konfigurerar nginx att starta vid BOOT                     |
|  - Effekt: Ingen omedelbar                                    |
|  - Persistence: Permanent                                      |
|                                                                |
|  systemctl enable --now nginx                                  |
|  - Bade enable OCH start                                      |
|  - Basta praxis for deployment                                |
|                                                                |
+----------------------------------------------------------------+
```

### Mask vs Disable

Ytterligare en viktig distinktion:

| Aktion | Startar vid boot | Kan startas manuellt | Anvandning |
|--------|-----------------|---------------------|------------|
| enable | Ja | Ja | Normal drift |
| disable | Nej | Ja | Tillfälligt av |
| mask | Nej | Nej | Permanent blockerad |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Grundlaggande tjansthantering

```bash
# Starta en tjanst
sudo systemctl start nginx

# Stoppa en tjanst
sudo systemctl stop nginx

# Starta om (stop + start)
sudo systemctl restart nginx

# Ladda om konfiguration (ingen nedtid)
sudo systemctl reload nginx
# Obs: Inte alla tjanster stodjer reload

# Reload eller restart (automatiskt val)
sudo systemctl reload-or-restart nginx
```

### Steg 2: Visa status och diagnostik

```bash
# Komplett status
systemctl status nginx
# Output:
# * nginx.service - A high performance web server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
#      Active: active (running) since Mon 2024-01-01 10:00:00 UTC
#        Docs: man:nginx(8)
#    Main PID: 1234 (nginx)
#       Tasks: 5
#      Memory: 10.5M
#         CPU: 32ms
#      CGroup: /system.slice/nginx.service
#              ├─1234 nginx: master process
#              └─1235 nginx: worker process

# Snabb status for scripts
systemctl is-active nginx     # active/inactive
systemctl is-enabled nginx    # enabled/disabled
systemctl is-failed nginx     # failed/active

# Exit codes for scripting
if systemctl is-active --quiet nginx; then
    echo "nginx is running"
fi
```

### Steg 3: Boot-konfiguration

```bash
# Aktivera for autostart vid boot
sudo systemctl enable nginx

# Avaktivera autostart
sudo systemctl disable nginx

# Enable OCH start direkt (basta praxis)
sudo systemctl enable --now nginx

# Disable OCH stoppa
sudo systemctl disable --now nginx
```

### Steg 4: Lista tjanster

```bash
# Alla laddade service-units
systemctl list-units --type=service

# Endast korande
systemctl list-units --type=service --state=running

# Endast misslyckade
systemctl list-units --type=service --state=failed
# Eller kortare:
systemctl --failed

# Alla installerade (oavsett laddad)
systemctl list-unit-files --type=service

# Endast enabled services
systemctl list-unit-files --type=service --state=enabled
```

### Steg 5: Mask och unmask

```bash
# Mask - helt blockera en tjanst
sudo systemctl mask apache2
# Skapar symlink till /dev/null

# Forsok starta en maskerad tjanst
sudo systemctl start apache2
# Error: Unit apache2.service is masked.

# Ta bort maskeringen
sudo systemctl unmask apache2

# Anvandning: Forhindra att nagon av misstag startar fel tjanst
# T.ex. om du kör nginx, maska apache2
```

### Steg 6: Hantera dependencies

```bash
# Se vad en tjanst beror pa
systemctl list-dependencies nginx

# Se vad som beror pa en tjanst (reverse)
systemctl list-dependencies nginx --reverse

# Visa alla properties
systemctl show nginx

# Visa specifik property
systemctl show nginx --property=MainPID
systemctl show nginx --property=ActiveState,SubState
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Deployment workflow

```bash
#!/bin/bash
# deploy.sh - Safe deployment with systemctl

SERVICE="myapp"
DEPLOY_DIR="/opt/myapp"

echo "=== Starting deployment ==="

# 1. Kolla nuvarande status
echo "Current status:"
systemctl is-active "$SERVICE" && echo "Running" || echo "Not running"

# 2. Stoppa forsiktigt
echo "Stopping service..."
sudo systemctl stop "$SERVICE"

# 3. Vanta pa att tjansten verkligen stoppat
while systemctl is-active --quiet "$SERVICE"; do
    sleep 1
done

# 4. Uppdatera kod (simulerat)
echo "Deploying new code..."
# rsync, git pull, etc.

# 5. Starta om
echo "Starting service..."
sudo systemctl start "$SERVICE"

# 6. Vanta och verifiera
sleep 3
if systemctl is-active --quiet "$SERVICE"; then
    echo "Deployment successful!"
    systemctl status "$SERVICE" --no-pager
else
    echo "ERROR: Service failed to start!"
    journalctl -u "$SERVICE" -n 20 --no-pager
    exit 1
fi
```

### Scenario 2: Health check script

```bash
#!/bin/bash
# health_check.sh - Monitor critical services

SERVICES=("nginx" "postgresql" "redis-server")
ALERT_EMAIL="ops@example.com"
FAILURES=""

for svc in "${SERVICES[@]}"; do
    if ! systemctl is-active --quiet "$svc"; then
        FAILURES+="$svc "

        # Forsok starta om
        echo "Attempting to restart $svc..."
        sudo systemctl restart "$svc"
        sleep 5

        if ! systemctl is-active --quiet "$svc"; then
            echo "CRITICAL: $svc failed to restart!"
        fi
    fi
done

if [[ -n "$FAILURES" ]]; then
    echo "Failed services: $FAILURES" | mail -s "Service Alert" "$ALERT_EMAIL"
fi
```

### Scenario 3: Graceful reload vs restart

```bash
# For tjanster som stodjer reload (t.ex. nginx):
# - reload = las om config UTAN att avbryta anslutningar
# - restart = stoppa och starta (avbryter anslutningar)

# Kolla om reload stods
systemctl cat nginx | grep ExecReload
# Om ExecReload finns stods reload

# Safe approach:
sudo systemctl reload nginx 2>/dev/null || sudo systemctl restart nginx

# Eller anvand:
sudo systemctl reload-or-restart nginx
```

------------------------------------------------------------

## Bästa Praxis

### 1. Anvand enable --now

```bash
# Istallet for:
sudo systemctl enable myapp
sudo systemctl start myapp

# Anvand:
sudo systemctl enable --now myapp
```

### 2. Verifiera alltid efter andring

```bash
sudo systemctl restart myapp && systemctl status myapp
```

### 3. Anvand --no-pager i scripts

```bash
# For renare output i scripts
systemctl status nginx --no-pager
journalctl -u nginx --no-pager -n 20
```

### 4. Dokumentera maskerade services

```bash
# Lista alla maskerade
systemctl list-unit-files --state=masked
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Glommer enable efter att ha startat                       |
|     start = nu, enable = vid boot                             |
|     Losning: enable --now                                      |
|                                                                |
|  2. Forvirrar reload och restart                              |
|     reload = config, restart = helt ny process                |
|     Anvand reload-or-restart om osakar                        |
|                                                                |
|  3. Ignorerar misslyckade tjanster                           |
|     systemctl --failed visar problem!                         |
|     Fixa eller maska tjanster du inte anvander               |
|                                                                |
|  4. Inte kollar journalctl efter restart                     |
|     Alltid: journalctl -u service -n 20                      |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Deployment simulation

<details>
<summary>Visa losning</summary>

```bash
# Simulera full deployment-cykel

# 1. Kolla status
systemctl status nginx

# 2. Stoppa
sudo systemctl stop nginx
systemctl is-active nginx  # Bor vara "inactive"

# 3. "Deploy" (simulerat)
echo "Deploying..."
sleep 2

# 4. Starta
sudo systemctl start nginx

# 5. Verifiera
systemctl is-active nginx  # Bor vara "active"
curl -I localhost  # Testa
```

</details>

### Ovning 2: Hitta och fixa misslyckade tjanster

<details>
<summary>Visa losning</summary>

```bash
# 1. Lista misslyckade
systemctl --failed

# 2. For varje misslyckad, kolla loggar
# Exempel: om "mybroken.service" ar failed
journalctl -u mybroken -n 50

# 3. Antingen fixa problemet eller maska
# Om tjansten inte behovs:
sudo systemctl mask mybroken
sudo systemctl reset-failed mybroken

# Om den behovs, fixa och starta om
sudo systemctl restart mybroken
```

</details>

### Ovning 3: Scripta service monitoring

<details>
<summary>Visa losning</summary>

```bash
#!/bin/bash
# check_services.sh

for service in nginx postgresql redis-server; do
    status=$(systemctl is-active "$service")
    enabled=$(systemctl is-enabled "$service" 2>/dev/null)

    echo "$service: $status (enabled: $enabled)"
done
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Unit Files | Skapa egna services |
| Journald | Loggar for felsökning |
| Systemd Architecture | Forsta helheten |
| Boot Process | Startup-ordning |

------------------------------------------------------------

## Sammanfattning

Systemctl ar din huvudsakliga kontrollpunkt for alla tjanster i Linux. Kom ihag skillnaden mellan start/enable, reload/restart, och disable/mask. Anvand alltid enable --now for nya deployments, och verifiera med status och journalctl efter varje andring.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `systemctl start X` | Starta tjanst |
| `systemctl stop X` | Stoppa tjanst |
| `systemctl restart X` | Starta om |
| `systemctl reload X` | Ladda om config |
| `systemctl status X` | Visa status |
| `systemctl enable --now X` | Enable + start |
| `systemctl disable X` | Ta bort fran boot |
| `systemctl mask X` | Blockera helt |
| `systemctl is-active X` | Check if running |
| `systemctl --failed` | Lista misslyckade |
| `systemctl list-units --type=service` | Lista services |

------------------------------------------------------------

## Referenser

- man systemctl
- https://www.freedesktop.org/software/systemd/man/systemctl.html
- Red Hat System Administrator's Guide
- Arch Wiki: systemd
""",
        },
        {
            "title": 'Boot Process and Targets',
            "slug": 'boot-process-targets',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Boot Process and Targets

------------------------------------------------------------

## Introduktion

Forstaelsen av Linux boot-processen ar kritisk for varje DevOps-ingenjor. Nar en server vangar sig pa eller inte startar korrekt, maste du kunna diagnostisera var i kedjan problemet uppstar - fran BIOS till fullt korande system.

Systemd targets ar det moderna sattet att definiera systemtillstand och ersatter aldre runlevels. Genom att forsta targets kan du kontrollera exakt vilka tjanster som startar, i vilken ordning, och hur systemet beter sig vid olika scenarios som normal drift, felsokningslagen, eller recovery.

Denna kunskap ar ovärderlig nar du behover reparera ett system som inte bootar, optimera boot-tiden, eller konfigurera servrar for specifika andamal.

------------------------------------------------------------

## Teori

### Boot-sekvensen i detalj

```
Complete Boot Sequence:
+------------------------------------------------------------------+
|                                                                  |
|  1. POWER ON                                                     |
|     Hardvara far strom                                           |
|                                                                  |
|  2. BIOS/UEFI                                                    |
|     +---------------------------+                                |
|     | - POST (Power-On Self-Test)                                |
|     | - Hittar boot device                                       |
|     | - Laddar bootloader                                        |
|     +---------------------------+                                |
|                |                                                 |
|  3. GRUB (Bootloader)                                            |
|     +---------------------------+                                |
|     | - Visar boot-meny                                          |
|     | - Laddar kernel + initramfs                                |
|     | - Skickar kernel parameters                                |
|     +---------------------------+                                |
|                |                                                 |
|  4. KERNEL                                                       |
|     +---------------------------+                                |
|     | - Initierar hardvara                                       |
|     | - Mountar initramfs                                        |
|     | - Startar init (systemd)                                   |
|     +---------------------------+                                |
|                |                                                 |
|  5. SYSTEMD (PID 1)                                              |
|     +---------------------------+                                |
|     | - Mountar root filesystem                                  |
|     | - Startar services                                         |
|     | - Nar default.target                                       |
|     +---------------------------+                                |
|                |                                                 |
|  6. LOGIN PROMPT / SERVICES READY                                |
|                                                                  |
+------------------------------------------------------------------+
```

### Targets forklarade

Targets ar systemd-units som representerar synchronization points - logiska tillstand som systemet kan na:

```
Target Hierarchy:
+----------------------------------------------------------------+
|                                                                |
|    sysinit.target                                              |
|         |                                                      |
|    basic.target                                                |
|         |                                                      |
|    +----+----+                                                 |
|    |         |                                                 |
|    v         v                                                 |
| multi-user.target  (servers - default)                         |
|         |                                                      |
|         v                                                      |
| graphical.target   (desktops med GUI)                          |
|                                                                |
| Special targets:                                               |
| - rescue.target    (single user for repair)                    |
| - emergency.target (minimal, read-only root)                   |
| - poweroff.target  (shutdown)                                  |
| - reboot.target    (restart)                                   |
|                                                                |
+----------------------------------------------------------------+
```

### Target-till-runlevel mappning

| Target | Gamla Runlevel | Beskrivning |
|--------|----------------|-------------|
| poweroff.target | 0 | Stang av systemet |
| rescue.target | 1 | Single user mode |
| multi-user.target | 3 | Multiuser, ingen GUI |
| graphical.target | 5 | Full med desktop |
| reboot.target | 6 | Starta om |

### GRUB konfiguration

```
GRUB Configuration:
/etc/default/grub
+----------------------------------------------------------+
|  GRUB_DEFAULT=0        # Forsta menyn (0-indexerat)       |
|  GRUB_TIMEOUT=5        # Sekunder att vanta               |
|  GRUB_CMDLINE_LINUX="" # Extra kernel parameters          |
+----------------------------------------------------------+

Genererade filer (ror ej!):
/boot/grub/grub.cfg  (update-grub genererar denna)
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Forsta nuvarande target

```bash
# Se default target
systemctl get-default
# Output: multi-user.target (server) eller graphical.target (desktop)

# Se aktuellt aktivt target
systemctl list-units --type=target --state=active

# Se vad som ingar i default target
systemctl list-dependencies default.target
```

### Steg 2: Andra default target

```bash
# Satt multi-user (server standard)
sudo systemctl set-default multi-user.target

# Satt graphical (desktop)
sudo systemctl set-default graphical.target

# Verifiera
systemctl get-default
```

### Steg 3: Byta target vid korning

```bash
# Ga till rescue mode (single user)
sudo systemctl isolate rescue.target

# Tillbaka till normalt
sudo systemctl isolate multi-user.target

# Starta om
sudo systemctl reboot
# Eller: reboot

# Stang av
sudo systemctl poweroff
# Eller: poweroff
```

### Steg 4: GRUB-konfiguration

```bash
# Redigera GRUB-konfiguration
sudo nano /etc/default/grub

# Exempel andringar:
# GRUB_TIMEOUT=3          # Kortare vantetid
# GRUB_CMDLINE_LINUX=""   # Kernel parameters

# VIKTIGT: Regenerera grub.cfg efter andringar
sudo update-grub   # Ubuntu/Debian
sudo grub2-mkconfig -o /boot/grub2/grub.cfg  # RHEL/CentOS
```

### Steg 5: Boot i rescue/emergency mode

```bash
# Metod 1: Via GRUB (vid boot)
# 1. Tryck 'e' vid GRUB-menyn
# 2. Hitta raden som borjar med 'linux'
# 3. Lagg till i slutet: systemd.unit=rescue.target
#    Eller: systemd.unit=emergency.target
# 4. Tryck Ctrl+X for att boota

# Skillnad:
# rescue.target = fler tjanster, rw filsystem
# emergency.target = minimalt, ro filsystem
```

### Steg 6: Boot-analys och optimering

```bash
# Total boot-tid
systemd-analyze

# Tid per tjanst (sorterat)
systemd-analyze blame

# Kritisk kedja (flaskhalsar)
systemd-analyze critical-chain

# Grafisk tidslinje
systemd-analyze plot > boot.svg
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Server bootar inte - felsokning

```bash
# 1. Boota i rescue mode via GRUB
# Lagg till: systemd.unit=rescue.target

# 2. Nar du far shell, kolla loggar
journalctl -xb -p err
# -x = extra forklaring
# -b = denna boot
# -p err = errors och varre

# 3. Kolla misslyckade services
systemctl --failed

# 4. Kolla filesystem
df -h           # Disk full?
fsck /dev/sda1  # Endast om unmounted!

# 5. Kolla senaste andringar
ls -lt /etc/ | head -20
cat /var/log/dpkg.log | tail -50  # Debian/Ubuntu
```

### Scenario 2: Fixa trasigt system i emergency mode

```bash
# 1. Boota med: systemd.unit=emergency.target

# 2. Filsystem ar read-only, remountera
mount -o remount,rw /

# 3. Nu kan du redigera filer
nano /etc/fstab  # Fixa felaktig entry

# 4. Reparera och starta om
systemctl reboot
```

### Scenario 3: Optimera boot-tid

```bash
#!/bin/bash
# boot_audit.sh - Identifiera langsamma services

echo "=== Boot Time Analysis ==="
systemd-analyze

echo ""
echo "=== Top 10 Slowest Services ==="
systemd-analyze blame | head -10

echo ""
echo "=== Critical Chain ==="
systemd-analyze critical-chain

echo ""
echo "=== Services that can be disabled? ==="
systemctl list-unit-files --state=enabled --type=service | grep -E "cups|bluetooth|avahi"
# Dessa behövs sällan pa servrar
```

------------------------------------------------------------

## Bästa Praxis

### 1. Servrar bor anvanda multi-user.target

```bash
# Kontrollera
systemctl get-default

# Om graphical, andra till multi-user
sudo systemctl set-default multi-user.target
# Sparar resurser, snabbare boot
```

### 2. Dokumentera kernel parameters

```bash
# Se aktiva kernel parameters
cat /proc/cmdline

# Dokumentera varfor du lagt till nagot
# i /etc/default/grub med kommentarer
```

### 3. Testa boot-andringar forsiktigt

```bash
# Innan production:
# 1. Ta snapshot/backup
# 2. Ha konsol-access (inte bara SSH)
# 3. Ha rescue-metod forberedd
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Glommer update-grub efter /etc/default/grub andring       |
|     Andringar tar inte effekt utan regenerering!              |
|                                                                |
|  2. Redigerar /boot/grub/grub.cfg direkt                     |
|     Denna fil skrivs over! Anvand /etc/default/grub          |
|                                                                |
|  3. Forvirrar isolate med set-default                        |
|     isolate = nu, set-default = nasta boot                   |
|                                                                |
|  4. Kor fsck pa monterat filsystem                           |
|     KAN FORSTORA DATA! Endast pa unmounted                   |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Utforska din boot-konfiguration

<details>
<summary>Visa losning</summary>

```bash
# 1. Se default target
systemctl get-default

# 2. Se boot-tid
systemd-analyze

# 3. Se langsamma services
systemd-analyze blame | head -5

# 4. Se GRUB-config
cat /etc/default/grub

# 5. Se aktiva kernel params
cat /proc/cmdline
```

</details>

### Ovning 2: Boot-analys

<details>
<summary>Visa losning</summary>

```bash
# Fullstandig boot-analys

# 1. Total tid
systemd-analyze
# Exempel: 25.5s

# 2. Blame - vad tar tid?
systemd-analyze blame | head -10
# Kanske NetworkManager-wait-online ar langsamst?

# 3. Kritisk kedja
systemd-analyze critical-chain

# 4. Finns services som kan disablas?
systemctl list-units --type=service --state=running
# cups? bluetooth? avahi?
```

</details>

### Ovning 3: Simulera rescue

<details>
<summary>Visa losning</summary>

```bash
# OBS: Gor inte pa produktion!

# Se vad rescue target innehaller
systemctl list-dependencies rescue.target

# Jamfor med multi-user
systemctl list-dependencies multi-user.target | wc -l
systemctl list-dependencies rescue.target | wc -l
# Rescue har betydligt farre services
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Systemd Architecture | Targets ar en del av systemd |
| Journald | Boot-loggar for felsokning |
| Service Management | Hantera vad som startar |
| Disk Management | Boot-partitioner |

------------------------------------------------------------

## Sammanfattning

Boot-processen gar fran BIOS genom GRUB till kernel och slutligen systemd. Targets definierar systemtillstand - multi-user.target for servrar, graphical.target for desktops, och rescue/emergency for felsökning. Kom ihåg att alltid kora update-grub efter GRUB-andringar och ha en recovery-plan innan du andrar boot-konfiguration.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `systemctl get-default` | Se default target |
| `systemctl set-default X` | Ändra default target |
| `systemctl isolate X` | Byt target nu |
| `systemd-analyze` | Boot-tid |
| `systemd-analyze blame` | Tid per service |
| `journalctl -xb` | Boot-loggar |
| `update-grub` | Regenerera GRUB |
| `reboot` | Starta om |
| `poweroff` | Stäng av |

------------------------------------------------------------

## Referenser

- man systemd.target
- man bootup(7)
- https://www.freedesktop.org/software/systemd/man/bootup.html
- GNU GRUB Manual
- Red Hat Boot Process Guide
""",
        },
        {
            "title": 'Journald and Logging',
            "slug": 'journald-logging',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Journald and Logging

------------------------------------------------------------

## Introduktion

Loggar ar dina ogon in i vad som hander pa ett Linux-system. Nar en tjanst kraschar, nar nagot beter sig konstigt, eller nar du behover forsta vad som hande vid en specifik tidpunkt - loggar ar svaret.

Systemd introducerade journald som ett centraliserat loggningssystem med kraftfulla filtreringsmojligheter. Journalctl ar kommandot som ger dig tillgang till denna skattkista av diagnostisk information.

For DevOps-ingenjorer ar effektiv loggsökning en grundläggande färdighet. Att snabbt kunna isolera relevanta loggrader bland miljoner kan vara skillnaden mellan minuters och timmars felsökning.

------------------------------------------------------------

## Teori

### Journald vs traditionell loggning

```
Logging Architecture:
+----------------------------------------------------------------+
|                                                                |
|  Traditional (/var/log/)         Systemd (journald)            |
|  +-----------------------+       +-----------------------+     |
|  | - Text files          |       | - Binary database     |     |
|  | - Multiple locations  |       | - Centralized         |     |
|  | - grep/awk for search |       | - Structured queries  |     |
|  | - Manual rotation     |       | - Auto-rotation       |     |
|  | - No metadata         |       | - Rich metadata       |     |
|  +-----------------------+       +-----------------------+     |
|                                                                |
|  /var/log/syslog                journalctl                     |
|  /var/log/auth.log              journalctl -u sshd             |
|  /var/log/nginx/access.log      (still in /var/log/)          |
|                                                                |
+----------------------------------------------------------------+
```

### Log Priorities (Syslog levels)

Loggar kategoriseras efter allvarlighetsgrad:

```
Priority Levels:
+----------------------------------------------------------------+
|  Level  | Name    | Description                 | When to use  |
+----------------------------------------------------------------+
|    0    | emerg   | System is unusable          | Kernel panic |
|    1    | alert   | Action must be taken NOW    | Critical hw  |
|    2    | crit    | Critical conditions         | Disk failure |
|    3    | err     | Error conditions            | Service fail |
|    4    | warning | Warning conditions          | Degraded     |
|    5    | notice  | Normal but significant      | Startup info |
|    6    | info    | Informational               | Status msgs  |
|    7    | debug   | Debug-level messages        | Development  |
+----------------------------------------------------------------+

Filter: -p err   = shows err and more severe (0-3)
        -p warning = shows warning and more severe (0-4)
```

### Journal-metadata

Varje loggrad i journald har metadata:

| Falt | Beskrivning | Exempel |
|------|-------------|---------|
| _PID | Process ID | 1234 |
| _UID | User ID | 0 (root) |
| _SYSTEMD_UNIT | Service name | nginx.service |
| _HOSTNAME | Server name | webserver01 |
| PRIORITY | Log level | 3 (err) |
| MESSAGE | Actual message | "Connection refused" |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Grundlaggande journalctl

```bash
# Alla loggar (aldre forst)
journalctl

# Alla loggar (nyaste forst)
journalctl -r

# Senaste 100 rader
journalctl -n 100

# Follow-mode (som tail -f)
journalctl -f
# Ctrl+C for att avsluta

# Utan pager (for scripts)
journalctl --no-pager -n 50
```

### Steg 2: Filtrera pa service

```bash
# Specifik service
journalctl -u nginx

# Service + follow
journalctl -u nginx -f

# Flera services
journalctl -u nginx -u php-fpm

# Senaste 50 rader for service
journalctl -u nginx -n 50
```

### Steg 3: Filtrera pa prioritet

```bash
# Endast errors och varre (emerg, alert, crit, err)
journalctl -p err

# Warnings och varre
journalctl -p warning

# Specifik service + errors
journalctl -u nginx -p err
```

### Steg 4: Filtrera pa tid

```bash
# Sedan en timme
journalctl --since "1 hour ago"

# Sedan specifik tid
journalctl --since "2024-01-15 10:00"

# Tidsspan
journalctl --since "10:00" --until "11:00"

# Idag
journalctl --since today

# Gårdag
journalctl --since yesterday --until today
```

### Steg 5: Boot-loggar

```bash
# Aktuell boot
journalctl -b

# Foregaende boot
journalctl -b -1

# Boot for tva bootar sedan
journalctl -b -2

# Lista alla bootar
journalctl --list-boots

# Errors fran forra booten (varfor kraschade den?)
journalctl -b -1 -p err
```

### Steg 6: Output-format

```bash
# Kortformat (en rad per entry)
journalctl -o short

# JSON (for parsing)
journalctl -o json-pretty -n 5

# Verbose (alla metadata-falt)
journalctl -o verbose -n 5

# Export (for backup)
journalctl -o export > /backup/journal_export.log
```

### Steg 7: Traditionella loggar i /var/log

```bash
# Fortfarande viktiga:
sudo tail -f /var/log/auth.log       # SSH, sudo, inloggningar
sudo tail -f /var/log/syslog         # Systemmeddelanden
sudo tail -f /var/log/nginx/access.log   # HTTP requests
sudo tail -f /var/log/nginx/error.log    # Nginx errors

# Kombinera flera loggar
sudo tail -f /var/log/auth.log /var/log/syslog

# Sok i loggar
sudo grep "Failed password" /var/log/auth.log
sudo grep "error" /var/log/nginx/error.log | tail -20
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Varfor kraschade tjansten?

```bash
#!/bin/bash
# debug_crash.sh - Felsok en kraschad tjanst

SERVICE=${1:-myapp}

echo "=== Debugging $SERVICE ==="

# 1. Aktuell status
echo "--- Status ---"
systemctl status "$SERVICE" --no-pager

# 2. Senaste loggar
echo ""
echo "--- Recent logs ---"
journalctl -u "$SERVICE" -n 50 --no-pager

# 3. Bara errors
echo ""
echo "--- Errors only ---"
journalctl -u "$SERVICE" -p err -n 20 --no-pager

# 4. Tid for senaste krasch?
echo ""
echo "--- Last restart ---"
systemctl show "$SERVICE" --property=ActiveEnterTimestamp
```

### Scenario 2: Security audit - vem loggade in?

```bash
#!/bin/bash
# security_audit.sh - Granska logins

echo "=== Login Audit ==="

# SSH logins (senaste dygnet)
echo "--- SSH Logins (last 24h) ---"
journalctl -u sshd --since "24 hours ago" | grep "Accepted"

# Misslyckade login-forsok
echo ""
echo "--- Failed SSH attempts ---"
journalctl -u sshd --since "24 hours ago" | grep "Failed password"

# Sudo-anvandning
echo ""
echo "--- Sudo usage ---"
sudo grep "sudo:" /var/log/auth.log | tail -20
```

### Scenario 3: Realtidsovervakning

```bash
# Overvaka kritiska services
journalctl -f -u nginx -u postgresql -u redis -p warning

# Eller med watch for periodisk koll
watch -n 5 'journalctl -u nginx -n 10 --no-pager'
```

### Scenario 4: Logrotate konfiguration

```bash
# Se nuvarande konfiguration
cat /etc/logrotate.d/nginx

# Exempel:
# /var/log/nginx/*.log {
#     daily
#     missingok
#     rotate 14
#     compress
#     delaycompress
#     notifempty
#     create 0640 www-data adm
#     sharedscripts
#     postrotate
#         [ -f /run/nginx.pid ] && kill -USR1 $(cat /run/nginx.pid)
#     endscript
# }

# Tvinga rotation (test)
sudo logrotate -f /etc/logrotate.d/nginx
```

------------------------------------------------------------

## Bästa Praxis

### 1. Standardiserad felsokningsworkflow

```bash
# Alltid samma ordning:
systemctl status service          # 1. Status
journalctl -u service -n 50       # 2. Recent logs
journalctl -u service -p err      # 3. Errors only
journalctl -b -p err              # 4. System-wide errors
```

### 2. Spara loggar for analys

```bash
# Exportera till fil
journalctl -u nginx --since today > /tmp/nginx_logs.txt

# JSON for programmering
journalctl -u nginx -o json > /tmp/nginx.json
```

### 3. Journal disk usage

```bash
# Se hur mycket disk journalen anvander
journalctl --disk-usage

# Rensa gamla loggar
sudo journalctl --vacuum-time=7d    # Behall 7 dagar
sudo journalctl --vacuum-size=500M  # Max 500MB
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Glommer -u for service                                    |
|     journalctl visar ALLT - anvand -u service                 |
|                                                                |
|  2. Soker i for manga loggar                                  |
|     Anvand --since/--until for att begränsa                  |
|                                                                |
|  3. Ignorerar -p for prioritet                                |
|     -p err filtrerar bort 90% av bruset                       |
|                                                                |
|  4. Glommer sudo for /var/log/                               |
|     Manga filer kraver root-access                           |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Hitta errors fran senaste timmen

<details>
<summary>Visa losning</summary>

```bash
# Alla errors senaste timmen
journalctl -p err --since "1 hour ago"

# For specifik service
journalctl -u nginx -p err --since "1 hour ago"

# Med antal
journalctl -p err --since "1 hour ago" | wc -l
```

</details>

### Ovning 2: Granska boot-loggar

<details>
<summary>Visa losning</summary>

```bash
# Lista bootar
journalctl --list-boots

# Errors fran senaste boot
journalctl -b -p err

# Errors fran foregaende boot (om systemet kraschade)
journalctl -b -1 -p err

# Tid for boot
systemd-analyze
```

</details>

### Ovning 3: Skapa loggsammanfattning

<details>
<summary>Visa losning</summary>

```bash
#!/bin/bash
# log_summary.sh

echo "=== Log Summary ==="
echo "Date: $(date)"
echo ""

echo "--- Error count (last 24h) ---"
journalctl --since "24 hours ago" -p err --no-pager | wc -l

echo ""
echo "--- Services with errors ---"
journalctl --since "24 hours ago" -p err -o json | \\
    jq -r '._SYSTEMD_UNIT' 2>/dev/null | sort | uniq -c | sort -rn

echo ""
echo "--- Disk usage ---"
journalctl --disk-usage
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| Systemd | Journald ar en del av systemd |
| Service Management | Status inkluderar loggar |
| Monitoring | Loggar ar grunden for alerting |
| Security | Audit logs for compliance |

------------------------------------------------------------

## Sammanfattning

Journalctl ar din huvudsakliga ingång till systemloggar. Kom ihåg de viktigaste flaggorna: -u for service, -f for follow, -p for prioritet, -b for boot, och --since/--until for tid. Kombinera med traditionella loggar i /var/log/ for applikationsspecifika behov.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `journalctl -f` | Follow-mode |
| `journalctl -u service` | Service-loggar |
| `journalctl -p err` | Errors only |
| `journalctl -b` | Denna boot |
| `journalctl -b -1` | Forra boot |
| `journalctl --since "1 hour ago"` | Tidsfilter |
| `journalctl --disk-usage` | Disk usage |
| `journalctl --vacuum-time=7d` | Rensa |
| `tail -f /var/log/auth.log` | Auth-loggar |

------------------------------------------------------------

## Referenser

- man journalctl
- man systemd-journald
- https://www.freedesktop.org/software/systemd/man/journalctl.html
- Red Hat Logging Guide
- Linux Journal - Mastering journalctl
""",
        },
        {
            "title": 'User and Group Management',
            "slug": 'user-group-management',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# User and Group Management

------------------------------------------------------------

## Introduktion

Linux ar ett multiuser-operativsystem fran grunden. Varje fil, process och resurs har en agare och grupptillhorighet. For DevOps-ingenjorer ar korrekta hantering av anvandare och grupper grundlaggande for sakerhet, accesskontroll och systemadministration.

Du behover skapa deploy-anvandare for CI/CD-pipelines, service accounts for applikationer, och personliga konton for teammedlemmar. Varje scenario kraver olika konfiguration och rattigheter.

Att forsta hur anvandare, grupper och permissions hangs ihop ar nyckeln till att bygga sakra och valhanterade system.

------------------------------------------------------------

## Teori

### Anvandare och grupper i Linux

```
User/Group Hierarchy:
+----------------------------------------------------------------+
|                                                                |
|  /etc/passwd ─────── Anvandardefinitioner                      |
|  /etc/shadow ─────── Krypterade losenord                       |
|  /etc/group  ─────── Gruppdefinitioner                         |
|                                                                |
|  User john:                                                    |
|  +------------------+                                          |
|  | UID: 1000        |  Primary Group: john (GID 1000)         |
|  | Home: /home/john |  Secondary Groups: docker, sudo         |
|  | Shell: /bin/bash |                                          |
|  +------------------+                                          |
|                                                                |
+----------------------------------------------------------------+
```

### UID/GID ranges

| Range | Anvandning |
|-------|------------|
| 0 | root |
| 1-999 | System accounts |
| 1000+ | Vanliga anvandare |

### /etc/passwd format

```
username:x:UID:GID:Comment:HomeDir:Shell
   │     │  │   │     │       │      │
   │     │  │   │     │       │      └─ Login shell
   │     │  │   │     │       └──────── Home directory
   │     │  │   │     └────────────────── GECOS (namn/beskrivning)
   │     │  │   └──────────────────────── Primary group ID
   │     │  └──────────────────────────── User ID
   │     └─────────────────────────────── x = password i shadow
   └───────────────────────────────────── Username

Exempel:
john:x:1000:1000:John Smith:/home/john:/bin/bash
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa anvandare

```bash
# Minimal anvandare (ingen home, default shell)
sudo useradd username

# Standard anvandare med home och bash
sudo useradd -m -s /bin/bash john

# Med specifikationer
sudo useradd -m -s /bin/bash -c "John Smith" -G docker,developers john

# Satt losenord
sudo passwd john

# Alternativt: adduser (interaktivt, Debian/Ubuntu)
sudo adduser jane
```

### Steg 2: Modifiera anvandare

```bash
# Lagg till i grupp (VIKTIGT: -a for append!)
sudo usermod -aG docker john

# VARNING: Utan -a ersatts alla grupper!
# sudo usermod -G docker john  # FEL! Tar bort alla andra grupper

# Byt shell
sudo usermod -s /bin/zsh john

# Byt home directory
sudo usermod -d /new/home john

# Las konto (ingen login)
sudo usermod -L john

# Las upp konto
sudo usermod -U john

# Byt username
sudo usermod -l newname oldname
```

### Steg 3: Hantera grupper

```bash
# Skapa grupp
sudo groupadd developers

# Skapa med specifik GID
sudo groupadd -g 5000 webteam

# Visa anvandares grupper
groups john
# Output: john : john docker developers

# Detaljerad info
id john
# Output: uid=1000(john) gid=1000(john) groups=1000(john),998(docker),1001(developers)

# Ta bort grupp
sudo groupdel developers
```

### Steg 4: Ta bort anvandare

```bash
# Ta bort anvandare (behall home)
sudo userdel john

# Ta bort inkl home och mail spool
sudo userdel -r john

# Rekommenderat: Backupa forst
sudo tar -czvf /backup/john_home_$(date +%Y%m%d).tar.gz /home/john
sudo userdel -r john
```

### Steg 5: Service accounts

```bash
# Skapa system account (UID < 1000)
sudo useradd -r -s /usr/sbin/nologin myapp

# Verifiera
grep myapp /etc/passwd
# myapp:x:999:999::/home/myapp:/usr/sbin/nologin

# For en specifik directory owner
sudo useradd -r -d /opt/myapp -s /usr/sbin/nologin myapp
sudo chown -R myapp:myapp /opt/myapp
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: CI/CD Deploy-anvandare

```bash
#!/bin/bash
# create_deploy_user.sh

USERNAME="deploy"

# 1. Skapa anvandare
sudo useradd -m -s /bin/bash -c "Deployment User" "$USERNAME"

# 2. Inaktivera losenord (endast SSH-nyckel)
sudo passwd -l "$USERNAME"

# 3. Lagg till i relevanta grupper
sudo usermod -aG docker,www-data "$USERNAME"

# 4. Setup SSH
sudo mkdir -p /home/$USERNAME/.ssh
sudo chmod 700 /home/$USERNAME/.ssh
sudo touch /home/$USERNAME/.ssh/authorized_keys
sudo chmod 600 /home/$USERNAME/.ssh/authorized_keys
sudo chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh

# 5. Lagg till CI/CD public key
echo "ssh-ed25519 AAAA... ci-cd@company.com" | sudo tee -a /home/$USERNAME/.ssh/authorized_keys

echo "Deploy user created. Add sudo rules in /etc/sudoers.d/deploy"
```

### Scenario 2: Team onboarding script

```bash
#!/bin/bash
# onboard_user.sh username email

USERNAME=$1
EMAIL=$2

if [[ -z "$USERNAME" || -z "$EMAIL" ]]; then
    echo "Usage: $0 username email"
    exit 1
fi

# Skapa anvandare
sudo useradd -m -s /bin/bash -c "$EMAIL" "$USERNAME"

# Lagg till i developers grupp
sudo usermod -aG developers "$USERNAME"

# Tvinga losenordsbyte vid forsta login
sudo passwd -e "$USERNAME"

# Skapa SSH-katalog
sudo -u "$USERNAME" mkdir -p /home/$USERNAME/.ssh
sudo -u "$USERNAME" chmod 700 /home/$USERNAME/.ssh

echo "User $USERNAME created. Set temporary password:"
sudo passwd "$USERNAME"
```

### Scenario 3: Audit script

```bash
#!/bin/bash
# audit_users.sh - Granska anvandare

echo "=== User Audit Report ==="
echo "Date: $(date)"
echo ""

echo "--- Users with login shell ---"
grep -E "/bin/(ba)?sh$" /etc/passwd | cut -d: -f1

echo ""
echo "--- Users in sudo group ---"
grep "^sudo:" /etc/group | cut -d: -f4

echo ""
echo "--- Users in docker group ---"
grep "^docker:" /etc/group | cut -d: -f4

echo ""
echo "--- Last 10 logins ---"
last -10
```

------------------------------------------------------------

## Bästa Praxis

### 1. Alltid -a med usermod -G

```bash
# RATT
sudo usermod -aG docker john

# FEL - tar bort alla andra grupper!
sudo usermod -G docker john
```

### 2. Service accounts med nologin

```bash
# Applikationer ska inte kunna logga in interaktivt
sudo useradd -r -s /usr/sbin/nologin myservice
```

### 3. Dokumentera accounts

```bash
# Anvand kommentarsfältet (-c)
sudo useradd -c "CI/CD Deploy - Jenkins" deploy
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Glommer -a vid usermod -G                                 |
|     sudo usermod -G docker john                               |
|     TAR BORT alla andra grupper! Anvand -aG                   |
|                                                                |
|  2. Redigerar /etc/passwd direkt                             |
|     Anvand useradd/usermod - aldrig nano!                    |
|     Risk for syntaxfel som laser ute alla                    |
|                                                                |
|  3. Glommer omloggning efter gruppandring                    |
|     Anvandaren maste logga ut och in for                     |
|     att nya grupper ska ta effekt                            |
|                                                                |
|  4. Delat konto for flera personer                           |
|     Skapar problem med audit trail                           |
|     En person = ett konto                                    |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Skapa en full anvandare

<details>
<summary>Visa losning</summary>

```bash
# Skapa anvandare med allt
sudo useradd -m -s /bin/bash -c "Developer User" devuser

# Satt losenord
sudo passwd devuser

# Lagg till i grupper
sudo usermod -aG docker,sudo devuser

# Verifiera
id devuser
groups devuser
```

</details>

### Ovning 2: Skapa service account

<details>
<summary>Visa losning</summary>

```bash
# Skapa service account
sudo useradd -r -d /opt/myapp -s /usr/sbin/nologin myapp

# Skapa och aga katalog
sudo mkdir -p /opt/myapp
sudo chown myapp:myapp /opt/myapp

# Verifiera
grep myapp /etc/passwd
ls -la /opt/myapp
```

</details>

### Ovning 3: Grupphantering

<details>
<summary>Visa losning</summary>

```bash
# Skapa grupp
sudo groupadd webteam

# Skapa anvandare och lagg till
sudo useradd -m alice
sudo useradd -m bob
sudo usermod -aG webteam alice
sudo usermod -aG webteam bob

# Verifiera
grep webteam /etc/group
groups alice bob
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| File Permissions | Rattigheter baseras pa user/group |
| Sudo | Privilegierad access for anvandare |
| SSH | Autentisering for remote access |
| PAM | Pluggbar autentisering |

------------------------------------------------------------

## Sammanfattning

Användarhantering i Linux kretsar kring tre filer: /etc/passwd, /etc/shadow och /etc/group. Useradd skapar anvandare, usermod modifierar dem (glom inte -a vid -G!), och grupper samlar anvandare for gemensamma rattigheter. Service accounts bor alltid ha nologin shell och egna UIDs under 1000.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `useradd -m -s /bin/bash user` | Skapa anvandare |
| `passwd user` | Satt losenord |
| `usermod -aG group user` | Lagg till i grupp |
| `userdel -r user` | Ta bort inkl home |
| `groupadd group` | Skapa grupp |
| `groups user` | Visa grupptillhorighet |
| `id user` | Detaljerad info |
| `getent passwd user` | Kolla anvandare |
| `chage -l user` | Losenordspolicy |

------------------------------------------------------------

## Referenser

- man useradd, usermod, userdel
- man passwd, shadow, group
- https://wiki.archlinux.org/title/Users_and_groups
- Linux System Administration Handbook
""",
        },
        {
            "title": 'Sudo Configuration',
            "slug": 'sudo-configuration',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Sudo Configuration

------------------------------------------------------------

## Introduktion

Sudo (superuser do) ar mekanismen som ger vanliga anvandare mojlighet att utfora administrativa uppgifter. Istallet for att anvanda root-kontot direkt, vilket ar en sakerhetsrisk, anvander vi sudo for att tillfälligt fa forhojda rattigheter.

For DevOps-ingenjorer ar korrekt sudo-konfiguration kritiskt. Du behover ge CI/CD-pipelines rattigheter att starta om tjanster, ge utvecklare tillgang till specifika kommandon, och allt detta utan att offra sakerhet genom att ge alla full root-access.

Sudoers-filen ar kraftfull men ocksa farlig - felkonfiguration kan lasa ute alla fran systemet. Darfor anvander vi ALLTID visudo som validerar syntax innan sparande.

------------------------------------------------------------

## Teori

### Sudo-arkitektur

```
Sudo Flow:
+----------------------------------------------------------------+
|                                                                |
|  User types: sudo apt update                                   |
|         |                                                      |
|         v                                                      |
|  /etc/sudoers  +  /etc/sudoers.d/*                            |
|         |                                                      |
|         v                                                      |
|  Check: Ar user tillaten?                                     |
|  Check: Kravs losenord?                                       |
|  Check: Ar kommandot tillatet?                                |
|         |                                                      |
|         v                                                      |
|  [Granted] ----> Execute as root                              |
|  [Denied]  ----> "user is not in the sudoers file"           |
|         |                                                      |
|         v                                                      |
|  Loggas till /var/log/auth.log                               |
|                                                                |
+----------------------------------------------------------------+
```

### Sudoers syntax

```
Grundformat:
who    where=(as_whom)    what

Exempel:
john   ALL=(ALL)          ALL
 │      │    │             │
 │      │    │             └─ Vilka kommandon
 │      │    └─────────────── Vilken anvandare att kora som
 │      └──────────────────── Vilka hosts
 └─────────────────────────── Vem som far kora
```

### Sudoers flaggor

| Flagga | Betydelse | Anvandning |
|--------|-----------|------------|
| NOPASSWD | Inget losenord | CI/CD, automation |
| NOEXEC | Inga subprocesser | Sakerhet |
| PASSWD | Krav losenord | Default |
| ALL | Allt tillatet | Full access |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Anvand visudo

```bash
# ENDA ratta sattet att redigera sudoers
sudo visudo

# For specifik fil i /etc/sudoers.d/
sudo visudo -f /etc/sudoers.d/deploy

# Validera syntax utan att redigera
sudo visudo -c

# ALDRIG:
# sudo nano /etc/sudoers  # FARLIGT!
```

### Steg 2: Grundlaggande sudo-anvandning

```bash
# Kor kommando som root
sudo apt update

# Kor som annan anvandare
sudo -u postgres psql

# Oppna root-shell
sudo -i

# Bevara environment
sudo -E command

# Lista dina sudo-rattigheter
sudo -l

# Kora flera kommandon
sudo sh -c "apt update && apt upgrade -y"
```

### Steg 3: Skapa sudo-regler

```bash
# Oppna visudo
sudo visudo

# Grundlaggande syntax-exempel:

# Full sudo for anvandare
john ALL=(ALL) ALL

# Full sudo for grupp
%admin ALL=(ALL) ALL

# Utan losenord (NOPASSWD)
deploy ALL=(ALL) NOPASSWD: ALL

# Specifika kommandon utan losenord
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status nginx

# Flera kommandon
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, /usr/bin/systemctl reload nginx
```

### Steg 4: Anvand /etc/sudoers.d/

```bash
# Battre praxis: separata filer i /etc/sudoers.d/
sudo visudo -f /etc/sudoers.d/deploy

# Innehall:
# Deploy user sudo rules
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status myapp
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl reload nginx

# Viktigt: filer maste ha ratta permissions
sudo chmod 440 /etc/sudoers.d/deploy
```

### Steg 5: Gruppregler

```bash
# I /etc/sudoers eller sudoers.d/:

# Developers kan starta om webservrar
%developers ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, \
                                /usr/bin/systemctl restart php-fpm

# DBAs kan hantera databaser
%dbadmins ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart postgresql, \
                              /usr/bin/pg_dump *

# Fullstandig admin-grupp
%sysadmins ALL=(ALL) ALL
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: CI/CD Deploy-rattigheter

```bash
# /etc/sudoers.d/ci-deploy
# CI/CD system sudo rules

# Restart specific services
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl reload nginx
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status *

# Deploy-relaterade operationer
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/rsync -avz * /var/www/*
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/chown -R www-data\:www-data /var/www/*

# Log viewing
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/tail -f /var/log/myapp/*
ci-deploy ALL=(ALL) NOPASSWD: /usr/bin/journalctl -u myapp *
```

### Scenario 2: Sakerhetsfokuserat setup

```bash
# /etc/sudoers.d/secure-sudo

# Krav losenord for kansliga kommandon
%developers ALL=(ALL) PASSWD: /usr/bin/docker exec *

# Logg alla sudo-kommandon
Defaults log_output
Defaults!/usr/bin/sudoreplay !log_output
Defaults!/usr/bin/reboot !log_output

# Timeout for sudo-session
Defaults timestamp_timeout=15

# Visa asterisker vid losenordsinmatning
Defaults pwfeedback
```

### Scenario 3: Felsokningsscript

```bash
#!/bin/bash
# check_sudo.sh - Diagnostisera sudo-problem

echo "=== Sudo Diagnostics ==="

# Kolla sudoers syntax
echo "--- Syntax check ---"
sudo visudo -c

# Visa aktuella rattigheter
echo ""
echo "--- Your sudo rights ---"
sudo -l

# Kolla grupptillhorighet
echo ""
echo "--- Your groups ---"
groups

# Senaste sudo-aktivitet
echo ""
echo "--- Recent sudo activity ---"
sudo grep "sudo:" /var/log/auth.log | tail -10
```

------------------------------------------------------------

## Bästa Praxis

### 1. Alltid visudo

```bash
# RATT
sudo visudo
sudo visudo -f /etc/sudoers.d/myfile

# FEL (ingen syntaxvalidering)
sudo nano /etc/sudoers
```

### 2. Minimala rattigheter

```bash
# RATT - specifika kommandon
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx

# FEL - for breda rattigheter
deploy ALL=(ALL) NOPASSWD: ALL
```

### 3. Anvand sudoers.d/

```bash
# Separata filer for olika andamal
/etc/sudoers.d/developers
/etc/sudoers.d/ci-deploy
/etc/sudoers.d/monitoring
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Redigerar /etc/sudoers utan visudo                        |
|     Syntaxfel kan lasa ute alla!                              |
|     ALLTID: sudo visudo                                        |
|                                                                |
|  2. NOPASSWD: ALL for alla                                    |
|     Helt oskyddad! Anvand specifika kommandon                 |
|                                                                |
|  3. Felaktig filpermission i sudoers.d/                      |
|     Maste vara 440: sudo chmod 440 /etc/sudoers.d/file       |
|                                                                |
|  4. Glommer %prefix for grupper                               |
|     admin = anvandare, %admin = grupp                         |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Skapa deploy-regler

<details>
<summary>Visa losning</summary>

```bash
# Skapa fil
sudo visudo -f /etc/sudoers.d/deploy

# Innehall:
# Deploy user
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl reload nginx
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status nginx

# Satt permissions
sudo chmod 440 /etc/sudoers.d/deploy

# Testa
sudo -l -U deploy
```

</details>

### Ovning 2: Gruppregel

<details>
<summary>Visa losning</summary>

```bash
# Skapa grupp
sudo groupadd webadmins

# Skapa sudo-regel
sudo visudo -f /etc/sudoers.d/webadmins

# Innehall:
%webadmins ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, \\
                               /usr/bin/systemctl restart apache2, \\
                               /usr/bin/systemctl restart php*-fpm

# Lagg till anvandare i gruppen
sudo usermod -aG webadmins john
```

</details>

### Ovning 3: Audit sudo-anvandning

<details>
<summary>Visa losning</summary>

```bash
# Visa senaste sudo-kommandon
sudo grep "sudo:" /var/log/auth.log | tail -20

# Visa misslyckade forsok
sudo grep "authentication failure" /var/log/auth.log | grep sudo

# Visa specifik anvandares aktivitet
sudo grep "deploy.*sudo" /var/log/auth.log | tail -10
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| User Management | Anvandare som far sudo |
| PAM | Autentisering bakom sudo |
| SSH | Remote sudo-access |
| Security | Principen om minsta privilegium |

------------------------------------------------------------

## Sammanfattning

Sudo ger kontrollerad root-access. Anvand ALLTID visudo for att redigera sudoers-filer. Skapa separata filer i /etc/sudoers.d/ for olika andamal. Anvand NOPASSWD endast for specifika kommandon, aldrig ALL. Grupper prefixas med %.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `sudo kommando` | Kor som root |
| `sudo -i` | Root shell |
| `sudo -l` | Lista dina rattigheter |
| `sudo -u user cmd` | Kor som annan anvandare |
| `sudo visudo` | Redigera sudoers |
| `sudo visudo -f file` | Redigera specifik fil |
| `sudo visudo -c` | Validera syntax |
| `grep sudo /var/log/auth.log` | Sudo-loggar |

------------------------------------------------------------

## Referenser

- man sudo, sudoers, visudo
- https://www.sudo.ws/docs/man/sudoers.man/
- Linux Security Handbook
- CIS Benchmarks for Linux
""",
        },
        {
            "title": 'PAM Modules',
            "slug": 'pam-modules',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 85,
            "content": """# PAM Modules

------------------------------------------------------------

## Introduktion

PAM (Pluggable Authentication Modules) ar Linux ramverk for autentisering. Istallet for att varje program implementerar sin egen inloggningslogik delegerar de till PAM-systemet. Detta ger centraliserad kontroll over autentisering, konto-policies, och sessionshantering.

For DevOps-ingenjorer ar forstaelse av PAM viktigt for att konfigurera losenordspolicies, tvafaktorsautentisering, resursbegransningar, och specialiserad accesskontroll. Nar du behover implementera starkare sakerhetskrav eller felsoka autentiseringsproblem ar PAM ofta inblandat.

PAM-konfiguration ar kraftfullt men ocksa riskabelt - felkonfiguration kan lasa ut alla anvandare fran systemet. Arbeta alltid med en backup-terminal oppen.

------------------------------------------------------------

## Teori

### PAM-arkitektur

```
PAM Architecture:
+----------------------------------------------------------------+
|                                                                |
|  Applications                                                  |
|  +--------+  +--------+  +--------+  +--------+               |
|  |  sshd  |  |  sudo  |  | login  |  |  su    |               |
|  +---+----+  +---+----+  +---+----+  +---+----+               |
|      |           |           |           |                    |
|      +-----+-----+-----+-----+-----+-----+                    |
|            |                                                  |
|            v                                                  |
|    +-------------------+                                      |
|    | /etc/pam.d/sshd  |   (per-application config)           |
|    | /etc/pam.d/sudo  |                                       |
|    | /etc/pam.d/login |                                       |
|    +--------+---------+                                       |
|             |                                                 |
|             v                                                 |
|    +---------------------+                                    |
|    |   PAM Modules       |   (/lib/security/*.so)            |
|    |   pam_unix.so       |                                    |
|    |   pam_limits.so     |                                    |
|    |   pam_wheel.so      |                                    |
|    +---------------------+                                    |
|                                                                |
+----------------------------------------------------------------+
```

### PAM module types

```
PAM Module Types:
+----------------------------------------------------------------+
|                                                                |
|  auth      - Verifiera anvandares identitet                   |
|              "Vem ar du?" (losenord, nycklar, biometri)       |
|                                                                |
|  account   - Kontrollera konto-status                         |
|              "Far du anvanda systemet?" (utganget, locked)    |
|                                                                |
|  password  - Hantera losenordsandringar                       |
|              "Ar det nya losenordet tillrackligt starkt?"     |
|                                                                |
|  session   - Session setup och teardown                       |
|              "Vad ska handa vid login/logout?"                |
|                                                                |
+----------------------------------------------------------------+
```

### Kontrollflaggor

```
Control Flags:
+----------------------------------------------------------------+
|                                                                |
|  required   ──► Maste lyckas, fortsatt anda (samla resultat)  |
|                 ✓ eller ✗, men testa alla moduler             |
|                                                                |
|  requisite  ──► Maste lyckas, avbryt vid fel                  |
|                 ✗ = avbryt OMEDELBART                          |
|                                                                |
|  sufficient ──► Lyckas = klart (om tidigare okat)             |
|                 ✓ = skippa resten                              |
|                                                                |
|  optional   ──► Resultat spelar ingen roll                    |
|                 Anvands for extra funktionalitet              |
|                                                                |
+----------------------------------------------------------------+
```

### Vanliga moduler

| Modul | Funktion | Anvandning |
|-------|----------|------------|
| pam_unix.so | Standard Unix auth | Losenord mot /etc/shadow |
| pam_wheel.so | Wheel-grupp krav | Begransat su |
| pam_limits.so | Resursbegransningar | ulimits |
| pam_pwquality.so | Losenordspolicy | Starka losenord |
| pam_tally2.so | Felhantering | Lasa konto efter misslyckade |
| pam_nologin.so | Blockera login | Maintenance mode |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Utforska PAM-konfiguration

```bash
# Lista PAM-filer
ls /etc/pam.d/

# Se konfiguration for specifik tjanst
cat /etc/pam.d/sudo

# Se vilka moduler som finns
ls /lib/security/ | head -20
# eller
ls /lib/x86_64-linux-gnu/security/  # Ubuntu
```

### Steg 2: Forsta en PAM-fil

```bash
# Visa /etc/pam.d/sshd
cat /etc/pam.d/sshd

# Typiskt innehall:
# @include common-auth
# @include common-account
# @include common-session
# @include common-password

# Gemensamma filer:
cat /etc/pam.d/common-auth
```

### Steg 3: Limits-konfiguration

```bash
# Visa aktuella limits
ulimit -a

# Konfigurationsfil
cat /etc/security/limits.conf

# Format:
# <domain>   <type>   <item>   <value>
# @developers  soft     nproc    1000
# @developers  hard     nproc    2000
# *            hard     nofile   65535

# Tillampas via pam_limits.so i PAM-stacken
```

### Steg 4: Losenordspolicy med pam_pwquality

```bash
# Konfigurationsfil
cat /etc/security/pwquality.conf

# Exempel-installningar:
# minlen = 12          # Minimum langd
# dcredit = -1         # Minst 1 siffra
# ucredit = -1         # Minst 1 stor bokstav
# lcredit = -1         # Minst 1 liten bokstav
# ocredit = -1         # Minst 1 specialtecken
# difok = 3            # Minst 3 tecken annorlunda fran gamla
```

### Steg 5: Begransat su med pam_wheel

```bash
# I /etc/pam.d/su:
# auth required pam_wheel.so

# Krav: anvandare maste vara i wheel-gruppen for att kora su
sudo usermod -aG wheel admin_user

# Verifiera
groups admin_user
```

------------------------------------------------------------

## Praktiska Exempel

### Scenario 1: Konfigurera resurslimits for utvecklare

```bash
# 1. Skapa utvecklargrupp
sudo groupadd developers

# 2. Redigera limits.conf
sudo nano /etc/security/limits.conf

# Lagg till:
@developers  soft     nproc      1000
@developers  hard     nproc      2000
@developers  soft     nofile     8192
@developers  hard     nofile     65535
@developers  soft     as         unlimited
@developers  hard     as         unlimited

# 3. Verifiera att pam_limits.so ar aktiv
grep pam_limits /etc/pam.d/common-session

# 4. Lagg till anvandare och testa
sudo usermod -aG developers john
# John maste logga in pa nytt
su - john
ulimit -a
```

### Scenario 2: Starkare losenordspolicy

```bash
# 1. Redigera pwquality
sudo nano /etc/security/pwquality.conf

# Innehall:
minlen = 14
dcredit = -2
ucredit = -2
lcredit = -2
ocredit = -1
difok = 5
maxrepeat = 3
gecoscheck = 1

# 2. Verifiera PAM anvander pwquality
grep pwquality /etc/pam.d/common-password

# 3. Testa
passwd testuser
# Svaga losenord avvisas nu
```

### Scenario 3: Lasa konto efter felaktiga forsok

```bash
# I /etc/pam.d/common-auth:
# Lagg till (FORST i filen):
auth required pam_faillock.so preauth silent deny=5 unlock_time=900 fail_interval=900
auth required pam_faillock.so authfail deny=5 unlock_time=900 fail_interval=900

# I /etc/pam.d/common-account:
account required pam_faillock.so

# Resultat: 5 felaktiga forsok = last i 15 minuter

# Administrera:
sudo faillock --user john            # Se status
sudo faillock --user john --reset    # Aterstall
```

------------------------------------------------------------

## Bästa Praxis

### 1. Ha alltid backup-terminal

```bash
# Innan du andrar PAM:
# 1. Oppna ett NYTT terminalfonster
# 2. Bli root: sudo -i
# 3. LAT DEN VARA OPPEN
# 4. Gör andringar
# 5. Testa i ORIGINAL-terminalen
```

### 2. Testa andringar forsiktigt

```bash
# Anvand pamtester for att testa utan att lasa ut dig
sudo apt install pamtester
pamtester sshd john authenticate
pamtester sudo john authenticate
```

### 3. Dokumentera andringar

```bash
# Lagg till kommentarer i PAM-filer
# DevOps team change 2024-01-15 - Stronger password policy
# auth required pam_pwquality.so retry=3
```

------------------------------------------------------------

## Vanliga Fallgropar

```
+----------------------------------------------------------------+
|                   MISSTAG ATT UNDVIKA                          |
+----------------------------------------------------------------+
|                                                                |
|  1. Redigera PAM utan backup-terminal                        |
|     Felkonfiguration kan lasa ut ALLA!                        |
|     HA ALLTID root-shell oppet vid andringar                 |
|                                                                |
|  2. required vs requisite forvirring                         |
|     required = fortsatter testa (battre felmeddelanden)       |
|     requisite = avbryter direkt (snabbare men mindre info)    |
|                                                                |
|  3. Glommer test efter andring                               |
|     Testa ALLTID med pamtester eller ny session              |
|                                                                |
|  4. Limits galler inte for inloggade                         |
|     Anvandare maste logga ut och in pa nytt                  |
|                                                                |
+----------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Utforska PAM

<details>
<summary>Visa losning</summary>

```bash
# Se vilka filer som finns
ls /etc/pam.d/

# Titta pa sshd
cat /etc/pam.d/sshd

# Titta pa common-auth
cat /etc/pam.d/common-auth

# Hitta var pam_unix.so anvands
grep pam_unix /etc/pam.d/*
```

</details>

### Ovning 2: Konfigurera limits

<details>
<summary>Visa losning</summary>

```bash
# Se nuvarande limits
ulimit -a

# Lagg till limits for grupp
sudo nano /etc/security/limits.conf

# Lagg till:
@mygroup  soft  nofile  4096
@mygroup  hard  nofile  8192

# Logga ut och in, verifiera
ulimit -n
```

</details>

### Ovning 3: Testa PAM med pamtester

<details>
<summary>Visa losning</summary>

```bash
# Installera
sudo apt install pamtester

# Testa autentisering
pamtester sshd $(whoami) authenticate

# Testa account
pamtester sshd $(whoami) acct_mgmt

# Testa session
pamtester sshd $(whoami) open_session
```

</details>

------------------------------------------------------------

## Kopplingar

| Relaterat amne | Relevans |
|----------------|----------|
| User Management | Anvandarkonton som autentiseras |
| Sudo | Sudo anvander PAM |
| SSH | SSHD anvander PAM |
| Security | PAM ar centralt for sakerhet |

------------------------------------------------------------

## Sammanfattning

PAM ar Linux pluggbara autentiseringssystem. Konfiguration per tjanst i /etc/pam.d/. Fyra modultyper: auth, account, password, session. Kontrollflaggor: required, requisite, sufficient, optional. Vanliga moduler inkluderar pam_unix, pam_limits, pam_pwquality. Ha ALLTID backup-terminal vid PAM-andringar!

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ls /etc/pam.d/` | Lista PAM-konfigurationer |
| `cat /etc/pam.d/sshd` | Visa service-config |
| `ulimit -a` | Visa limits |
| `cat /etc/security/limits.conf` | Limits-konfiguration |
| `pamtester service user func` | Testa PAM |
| `faillock --user X` | Visa lockstatus |
| `faillock --user X --reset` | Aterstall lock |

------------------------------------------------------------

## Referenser

- man pam, pam.conf, pam.d
- Linux-PAM System Administrators' Guide
- https://wiki.archlinux.org/title/PAM
- Red Hat PAM Configuration Guide
""",
        },
        {
            "title": 'SSH Hardening',
            "slug": 'ssh-hardening',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# SSH Hardening

------------------------------------------------------------

## Introduktion

SSH ar den kritiska ingangspunkten till dina servrar och varje exponerad server bombarderas konstant med tusentals automatiserade inloggningsattacker varje dag. SSH Hardening handlar om att systematiskt stanga alla onnodiga oppningar och gora det praktiskt omojligt for angripare att ta sig in. Denna nod lär dig implementera flerlagrat forsvar med nyckelbaserad autentisering, atkomstbegransningar, fail2ban och sakra konfigurationer som tillsammans skapar en robust SSH-sakerhet.

------------------------------------------------------------

## Teori

SSH-sakerheten bygger pa principen om defense-in-depth dar flera oberoende sakerhetsatgarder samverkar. Traditionell losenordsautentisering ar sarbar for brute-force-attacker dar angripare testar miljontals kombinationer automatiskt. Nyckelbaserad autentisering eliminerar denna risk genom att krava bade nagon du har (privat nyckel) och nagon du vet (nyckelns losen). Ed25519-nycklar erbjuder modernast kryptografi med kortare nycklar an RSA men samma eller hogre sakerhet. AllowUsers och AllowGroups implementerar principen om minsta mojliga atkomst genom att explicit definiera vilka som far ansluta. Fail2ban overvakar loggfiler och blockerar automatiskt IP-adresser som uppvisar misstankt beteende. Tillsammans skapar dessa lager ett forsvar dar en angripare maste ta sig forbi flera oberoende hinder.

```
SSH SECURITY LAYERS
------------------------------------------------------------

    INTERNET (angripare)
           |
           v
    +------+------+
    |  Port 2222  |  <-- Icke-standard port (dold)
    +------+------+
           |
           v
    +------+------+
    |  Fail2ban   |  <-- Blockerar efter 3 fel
    +------+------+
           |
           v
    +------+------+
    | AllowUsers  |  <-- Endast listade anvandare
    +------+------+
           |
           v
    +------+------+
    |  SSH-nyckel |  <-- Kryptografisk autentisering
    +------+------+
           |
           v
    [  SERVER  ]  <-- Endast legitimt trafik
```

------------------------------------------------------------

## Steg-för-steg Guide

Komplett SSH-hardening fran grunden:

```bash
# Steg 1: Skapa backup av original
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d)
echo "Backup skapad"

# Steg 2: Generera SSH-nyckel pa LOKAL dator
ssh-keygen -t ed25519 -C "$(whoami)@$(hostname)-$(date +%Y%m%d)"
# Ange stark losen for extra sakerhet

# Steg 3: Kopiera nyckel till server (medan losenord fortfarande fungerar)
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server
# TESTA: ssh user@server  (ska fungera utan losenord)

# Steg 4: Konfigurera sshd_config pa servern
sudo tee /etc/ssh/sshd_config.d/hardening.conf << 'EOF'
# SSH Hardening Configuration
Port 2222
Protocol 2

# Autentisering
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes

# Atkomstbegransning
AllowGroups sshusers

# Tidsgranser
LoginGraceTime 30
MaxAuthTries 3
MaxSessions 2
ClientAliveInterval 300
ClientAliveCountMax 2

# Sakerhet
X11Forwarding no
AllowTcpForwarding no
AllowAgentForwarding no
PermitUserEnvironment no

# Loggning
LogLevel VERBOSE
EOF

# Steg 5: Skapa SSH-grupp och lagg till anvandare
sudo groupadd -f sshusers
sudo usermod -aG sshusers $(whoami)

# Steg 6: Uppdatera brandvagg
sudo ufw allow 2222/tcp
sudo ufw delete allow 22/tcp  # Ta bort gammal port efter test

# Steg 7: Testa och applicera
sudo sshd -t
sudo systemctl restart sshd

# Steg 8: Installera fail2ban
sudo apt install -y fail2ban
sudo tee /etc/fail2ban/jail.d/sshd.local << 'EOF'
[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
EOF
sudo systemctl enable --now fail2ban
```

------------------------------------------------------------

## Praktiska Exempel

Exempel 1 - Nyckelbaserad autentisering:
```bash
# Skapa hogsakerhetsnyckel med losen
ssh-keygen -t ed25519 -a 100 -C "admin@production"
# -a 100 = 100 KDF-rundor (langsam att knacka)

# Visa publik nyckel
cat ~/.ssh/id_ed25519.pub
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... admin@production

# Satt korrekta rattigheter
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys

# Testa anslutning med verbose output
ssh -v user@server -p 2222
```

Exempel 2 - AllowUsers med IP-begransning:
```bash
# Tillat specifika anvandare fran specifika IP
echo 'AllowUsers admin@192.168.1.* deploy@10.0.0.0/8' | sudo tee -a /etc/ssh/sshd_config.d/hardening.conf

# Kombinera med AllowGroups
echo 'Match Group developers
    AllowTcpForwarding yes
    X11Forwarding no' | sudo tee -a /etc/ssh/sshd_config.d/hardening.conf

# Verifiera konfiguration
sudo sshd -T | grep -i allow
```

Exempel 3 - Fail2ban avancerad konfiguration:
```bash
# Skapa anpassad jail med aggressiv blockering
sudo tee /etc/fail2ban/jail.d/ssh-aggressive.local << 'EOF'
[sshd-aggressive]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 2
bantime = 86400
findtime = 300
action = %(action_mwl)s
EOF

# Visa bannlysningar
sudo fail2ban-client status sshd
sudo fail2ban-client get sshd banip

# Avblockera IP manuellt
sudo fail2ban-client set sshd unbanip 192.168.1.100
```

------------------------------------------------------------

## Bästa Praxis

1. Nyckelbaserad autentisering - Generera ed25519-nycklar med stark losen och inaktivera losenordsautentisering helt efter verifierad nyckel-login
2. Minimal atkomst - Anvand AllowGroups istallet for AllowUsers for enklare administration och lagg endast till nodvandiga anvandare
3. Icke-standard port - Byt till port over 1024 for att undvika majoriteten av automatiserade skanningar
4. Fail2ban - Installera och konfigurera med korta findtime och langa bantime for aggressivt forsvar
5. Testa fore omstart - Kor alltid sshd -t fore systemctl restart och ha backup-session oppen
6. Loggning - Satt LogLevel VERBOSE och overvaka /var/log/auth.log regelbundet
7. Backup-konfiguration - Spara alltid original sshd_config med datum innan andringar
8. Timeout-installningar - Konfigurera ClientAliveInterval for att stanga inaktiva sessioner automatiskt

------------------------------------------------------------

## Vanliga Fallgropar

1. Lasa ut sig sjalv - Aktivera nyckelautentisering utan att testa nyckel-login forst stanger ute dig permanent
2. Glomma brandvagg - Byta SSH-port utan att oppna ny port i UFW blockerar all atkomst
3. Fel rattigheter - .ssh-katalogen maste ha 700 och authorized_keys 600 annars ignoreras nycklar
4. Ingen backup-session - Gora SSH-andringar utan parallell session betyder ingen aterhamtning vid fel
5. AllowUsers utan sig sjalv - Lagga till AllowUsers utan att inkludera aktuell anvandare laser ut direkt
6. Root-beroende - Inaktivera PermitRootLogin utan fungerande sudo-anvandare gor servern oadministrerbar
7. Glomma sshusers-grupp - AllowGroups sshusers utan att skapa gruppen eller lagga till anvandare blockerar alla
8. Fail2ban pa fel port - Konfigurera fail2ban for port 22 nar SSH kor pa 2222 ger inget skydd

------------------------------------------------------------

## Övningar

### Ovning 1: Grundlaggande SSH Hardening
Implementera komplett SSH-hardening pa en testserver med nyckelbaserad autentisering, PermitRootLogin no, och anpassad port.

<details>
<summary>Visa losning</summary>

```bash
# Pa lokal dator - skapa nyckel
ssh-keygen -t ed25519 -C "test@hardening"
ssh-copy-id user@testserver

# Verifiera nyckel-login fungerar
ssh user@testserver "echo 'Nyckel-login OK'"

# Pa server - konfigurera
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

sudo tee /etc/ssh/sshd_config.d/secure.conf << 'EOF'
Port 2222
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
MaxAuthTries 3
EOF

sudo ufw allow 2222/tcp
sudo sshd -t && sudo systemctl restart sshd

# Testa fran ny terminal
ssh -p 2222 user@testserver
```

</details>

### Ovning 2: Fail2ban SSH-skydd
Installera och konfigurera fail2ban for SSH med anpassade granser och verifiera funktionaliteten.

<details>
<summary>Visa losning</summary>

```bash
# Installation
sudo apt update && sudo apt install -y fail2ban

# Skapa SSH-jail
sudo tee /etc/fail2ban/jail.d/ssh-custom.local << 'EOF'
[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
ignoreip = 127.0.0.1/8 192.168.1.0/24
EOF

# Starta och aktivera
sudo systemctl enable fail2ban
sudo systemctl restart fail2ban

# Verifiera
sudo fail2ban-client status
sudo fail2ban-client status sshd

# Visa regler
sudo iptables -L f2b-sshd -n -v
```

</details>

### Ovning 3: Grupp-baserad atkomst
Konfigurera SSH for att endast tillata anvandare i specifik grupp med olika behorighetnivaer.

<details>
<summary>Visa losning</summary>

```bash
# Skapa grupper
sudo groupadd ssh-admins
sudo groupadd ssh-developers

# Lagg till anvandare
sudo usermod -aG ssh-admins adminuser
sudo usermod -aG ssh-developers devuser

# Konfigurera differentierad atkomst
sudo tee /etc/ssh/sshd_config.d/groups.conf << 'EOF'
# Grundlaggande begransning
AllowGroups ssh-admins ssh-developers

# Admins - full atkomst
Match Group ssh-admins
    AllowTcpForwarding yes
    X11Forwarding yes
    PermitTunnel yes

# Utvecklare - begransad
Match Group ssh-developers
    AllowTcpForwarding local
    X11Forwarding no
    PermitTunnel no
    ForceCommand /usr/local/bin/dev-shell.sh
EOF

sudo sshd -t && sudo systemctl restart sshd

# Verifiera
sudo sshd -T | grep -i allowgroups
groups adminuser
groups devuser
```

</details>

------------------------------------------------------------

## Kopplingar

- Firewall Basics - SSH-hardening kombineras med brandvaggsregler for port-begransning och IP-filtrering
- PAM Modules - PAM integrerar med SSH for tva-faktorsautentisering och ytterligare autentiseringspolicies
- User and Group Management - AllowGroups och AllowUsers bygger pa Linux grupphantering
- Systemd Services - SSH ar en systemd-service som hanteras med systemctl for start/stopp/restart
- Journald Logging - SSH-loggar samlas av journald och kan analyseras med journalctl -u sshd

------------------------------------------------------------

## Sammanfattning

SSH Hardening implementerar flerlagrat forsvar som tillsammans gor obehorigad atkomst praktiskt omojlig. Nyckelbaserad autentisering med ed25519 eliminerar losenordsattacker helt. AllowGroups och AllowUsers begransar exakt vilka som far ansluta. Fail2ban blockerar automatiskt angripare efter upprepade misslyckade forsok. Kombinationen av icke-standard port, inaktiverad root-login, strikta timeouts och VERBOSE-loggning skapar en robust sakerhetsprofil. Nyckeln till framgang ar metodisk implementation dar varje steg testas innan nasta, alltid med backup-session oppen och konfigurationsbackup sparad.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ssh-keygen -t ed25519` | Generera modern SSH-nyckel |
| `ssh-copy-id user@server` | Kopiera publik nyckel till server |
| `sudo sshd -t` | Testa SSH-konfigurationssyntax |
| `sudo sshd -T` | Visa effektiv SSH-konfiguration |
| `sudo systemctl restart sshd` | Starta om SSH-tjanst |
| `sudo fail2ban-client status sshd` | Visa fail2ban SSH-status |
| `sudo fail2ban-client set sshd unbanip IP` | Avblockera IP fran fail2ban |
| `sudo grep "Failed" /var/log/auth.log` | Visa misslyckade inloggningsforsk |
| `sudo ss -tlnp \\| grep sshd` | Visa SSH-lyssnande portar |
| `chmod 700 ~/.ssh` | Satt korrekta .ssh-rattigheter |

------------------------------------------------------------

## Referenser

- OpenSSH Manual - man sshd_config for alla konfigurationsalternativ
- Fail2ban Documentation - fail2ban.org for filter och actions
- Mozilla SSH Guidelines - Infosec SSH hardening best practices
- CIS Benchmarks - SSH-sektionen for enterprise-hardening
- NIST SP 800-123 - Guide to General Server Security SSH-kapitel
""",
        },
        {
            "title": 'Firewall Basics (ufw, iptables)',
            "slug": 'firewall-basics',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Firewall Basics (ufw, iptables)

------------------------------------------------------------

## Introduktion

En brandvagg ar den forsta och viktigaste forsvarslinjen for varje server som bestammer exakt vilken natverkstrafik som tillats passera. Utan brandvagg star alla portar oppna for vem som helst pa internet att ansluta till, vilket gor servern extremt sarbar. Denna nod lär dig implementera brandvaggsregler med bade UFW for enkelhet och iptables for full kontroll, sa att du kan bygga robusta natverkssakerhetsbarriarer for alla typer av serverinstallationer.

------------------------------------------------------------

## Teori

Linux-brandvaggar fungerar genom att inspektera varje natverskpaket och matcha det mot en uppsattning regler som bestammer om paketet ska accepteras, nekas eller droppas. Netfilter ar karnmodulen som utfor filtreringen medan iptables och nftables ar verktyg for att konfigurera dessa regler. UFW (Uncomplicated Firewall) ar ett hogniva-granssnitt som forenklar iptables-konfiguration dramatiskt. Regler utvärderas i ordning dar forsta matchande regel bestammer paketets ode. Chains organiserar regler i kategorier - INPUT for inkommande, OUTPUT for utgaende och FORWARD for vidarebefordrad trafik. States som ESTABLISHED och RELATED tillater svar pa utgaende anslutningar att komma tillbaka in. Principen ar default deny - neka allt utom explicit tillatna tjanster.

```
PACKET FLOW THROUGH FIREWALL
------------------------------------------------------------

    INCOMING PACKET                    OUTGOING PACKET
          |                                  ^
          v                                  |
    +-----+-----+                      +-----+-----+
    |   INPUT   |                      |  OUTPUT   |
    |   CHAIN   |                      |   CHAIN   |
    +-----+-----+                      +-----+-----+
          |                                  ^
          v                                  |
    [Rule 1: SSH]--MATCH--> ACCEPT     [Local Process]
          |                                  |
          v                                  |
    [Rule 2: HTTP]-MATCH--> ACCEPT     -----+
          |
          v
    [Rule 3: HTTPS]-MATCH-> ACCEPT
          |
          v
    [Default Policy]----> DROP

    FORWARD CHAIN (for routing/NAT):
    INCOMING --> [FORWARD] --> OUTGOING
```

------------------------------------------------------------

## Steg-för-steg Guide

Komplett brandvaggskonfiguration med UFW:

```bash
# Steg 1: Kontrollera aktuell status
sudo ufw status verbose
# Om inaktiv, fortsatt med konfiguration

# Steg 2: KRITISKT - Tillat SSH forst (las inte ut dig!)
sudo ufw allow ssh
# eller for annan port:
sudo ufw allow 2222/tcp

# Steg 3: Satt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing
# Nu blockeras all inkommande utom SSH

# Steg 4: Tillat nodvandiga tjanster
sudo ufw allow http          # Port 80
sudo ufw allow https         # Port 443
sudo ufw allow 'Nginx Full'  # Bade 80 och 443

# Steg 5: Aktivera brandvaggen
sudo ufw enable
# Svara 'y' pa varningen

# Steg 6: Verifiera
sudo ufw status verbose
# Ska visa: Status: active med alla regler

# Steg 7: Avancerade regler (vid behov)
# Specifik IP
sudo ufw allow from 192.168.1.100

# Subnet till specifik port
sudo ufw allow from 10.0.0.0/8 to any port 5432

# Portintervall
sudo ufw allow 6000:6100/tcp

# Steg 8: Aktivera loggning
sudo ufw logging on
sudo ufw logging medium
```

------------------------------------------------------------

## Praktiska Exempel

Exempel 1 - Webbserver med UFW:
```bash
# Grundlaggande webbserver
sudo ufw reset                     # Borja fran rent blad
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# Verifiera
sudo ufw status numbered
# Status: active
#      To                         Action      From
# [1]  22/tcp                     ALLOW IN    Anywhere
# [2]  80/tcp                     ALLOW IN    Anywhere
# [3]  443/tcp                    ALLOW IN    Anywhere
```

Exempel 2 - Databasserver med IP-begransning:
```bash
# Databas som endast accepterar fran appservrar
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
# PostgreSQL endast fran specifika IP
sudo ufw allow from 10.0.1.10 to any port 5432
sudo ufw allow from 10.0.1.11 to any port 5432
# MySQL endast fran app-subnet
sudo ufw allow from 10.0.2.0/24 to any port 3306
sudo ufw enable

sudo ufw status
```

Exempel 3 - iptables direkt konfiguration:
```bash
# Rensa befintliga regler
sudo iptables -F
sudo iptables -X

# Satt default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Tillat loopback (localhost)
sudo iptables -A INPUT -i lo -j ACCEPT

# Tillat etablerade anslutningar (KRITISKT!)
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Tillat SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Tillat HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Tillat ICMP (ping)
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Spara regler persistent
sudo apt install iptables-persistent
sudo netfilter-persistent save

# Visa regler
sudo iptables -L -n -v --line-numbers
```

------------------------------------------------------------

## Bästa Praxis

1. SSH forst alltid - Tillat ALLTID SSH innan du aktiverar brandvaggen eller sattar default deny policy
2. Default deny incoming - Satt default policy till deny och tillat endast nodvandiga portar explicit
3. ESTABLISHED state - I iptables, tillat alltid ESTABLISHED,RELATED for att svar ska komma tillbaka
4. Loopback interface - Tillat alltid trafik pa lo-interfacet for att localhost-kommunikation ska fungera
5. Specifika IP nar mojligt - Begransa databasportar till endast appservrars IP istallet for oppet
6. Dokumentera regler - Kommentera varfor varje regel finns for framtida underhall
7. Testa fore produktion - Verifiera brandvaggsregler i staging innan produktionsdeploy
8. Backup-access - Ha alltid alternativ atkomst (console, IPMI) vid SSH-problem

------------------------------------------------------------

## Vanliga Fallgropar

1. Las ut sig sjalv - Aktivera brandvagg utan SSH-regel stanger ute dig permanent fran servern
2. Glomma ESTABLISHED - Utan state-regel i iptables kan inga svar pa utgaende trafik komma in
3. Blockera localhost - Utan loopback-regel kan applikationer inte kommunicera internt
4. Fel regelordning - Iptables utvärderar i ordning sa en tidig DROP blockerar senare ACCEPT
5. Glomma spara regler - Iptables-regler forsvinner vid omstart utan netfilter-persistent
6. Oppna ranges istallet for portar - Oppna 3000-9000 istallet for specifika portar exponerar for mycket
7. Ignorera utgaende - Default allow outgoing ar bekvämt men kan tillata data-exfiltrering
8. Glömma IPv6 - UFW hanterar IPv6 automatiskt men iptables kraver separat ip6tables-konfiguration

------------------------------------------------------------

## Övningar

### Ovning 1: Grundlaggande webbserver-brandvagg
Konfigurera UFW for en webbserver som ska tillata SSH, HTTP och HTTPS men blockera allt annat.

<details>
<summary>Visa losning</summary>

```bash
# Kontrollera status och aterstall om nodvandigt
sudo ufw status
sudo ufw reset

# Konfigurera
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Tillat nodvandiga portar
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# Aktivera
sudo ufw enable

# Verifiera
sudo ufw status verbose
# Expected output:
# Status: active
# Default: deny (incoming), allow (outgoing)
# To                         Action      From
# 22/tcp                     ALLOW IN    Anywhere
# 80/tcp                     ALLOW IN    Anywhere
# 443/tcp                    ALLOW IN    Anywhere

# Testa
nc -zv localhost 22   # Ska lyckas
nc -zv localhost 80   # Ska lyckas
nc -zv localhost 3306 # Ska misslyckas
```

</details>

### Ovning 2: IP-begransad databastjanst
Konfigurera brandvagg dar PostgreSQL (5432) endast ar atkomlig fran specifika appserver-IP:n.

<details>
<summary>Visa losning</summary>

```bash
# Scenario: Appservrar pa 10.0.1.10 och 10.0.1.11

# Med UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
# PostgreSQL endast fran appservrar
sudo ufw allow from 10.0.1.10 to any port 5432 proto tcp
sudo ufw allow from 10.0.1.11 to any port 5432 proto tcp
# Tillat aven fran lokalt natwerk for administration
sudo ufw allow from 10.0.1.0/24 to any port 22
sudo ufw enable

# Verifiera
sudo ufw status numbered
# [1] 22/tcp                     ALLOW IN    Anywhere
# [2] 5432/tcp                   ALLOW IN    10.0.1.10
# [3] 5432/tcp                   ALLOW IN    10.0.1.11
# [4] 22                         ALLOW IN    10.0.1.0/24

# Alternativ med iptables
sudo iptables -A INPUT -p tcp -s 10.0.1.10 --dport 5432 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 10.0.1.11 --dport 5432 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5432 -j DROP
```

</details>

### Ovning 3: iptables fran grunden
Konfigurera iptables manuellt for en server med SSH, HTTP, HTTPS och inkludera korrekta state-regler.

<details>
<summary>Visa losning</summary>

```bash
# Rensa allt
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X

# Satt default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Loopback - KRITISKT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# Etablerade anslutningar - KRITISKT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SSH (med rate limiting)
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# ICMP (ping)
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Logga droppade paket (valfritt)
sudo iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: " --log-level 4

# Spara
sudo netfilter-persistent save

# Verifiera
sudo iptables -L -n -v --line-numbers
```

</details>

------------------------------------------------------------

## Kopplingar

- SSH Hardening - Brandvaggsregler kompletterar SSH-hardening genom port-andring och IP-begransning
- Systemd Services - UFW och iptables ar tjanster som hanteras med systemctl
- Process Monitoring - Anvand ss och netstat for att se vilka portar som behover oppnas
- Journald Logging - Brandvaggsloggar samlas i journald med UFW-loggning aktiverad
- Network Troubleshooting - tcpdump och nc anvands for att felsoka brandvaggsproblem

------------------------------------------------------------

## Sammanfattning

Linux-brandvaggar med UFW och iptables ar grundlaggande for serversakerhet och implementerar principen default deny dar endast explicit tillatna tjanster accepteras. UFW forenklar konfigurationen dramatiskt med lattlasta kommandon medan iptables ger full kontroll over paketfiltrering. Kritiska regler inkluderar alltid SSH fore aktivering, ESTABLISHED state for svarstraffik, och loopback for intern kommunikation. IP-begransning for databaser och andra känsliga tjanster minimerar attackytan. Kombinationen av brandvagg, SSH-hardening och fail2ban skapar ett robust flerlagrat forsvar som skyddar servrar mot de flesta natverksbaserade attacker.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `sudo ufw status verbose` | Visa detaljerad brandvaggsstatus |
| `sudo ufw enable/disable` | Aktivera eller inaktivera UFW |
| `sudo ufw allow ssh` | Tillat SSH-trafik |
| `sudo ufw default deny incoming` | Satt default policy till neka |
| `sudo ufw allow from IP to any port PORT` | IP-begransad portregel |
| `sudo ufw delete RULE` | Ta bort specifik regel |
| `sudo iptables -L -n -v` | Lista iptables-regler detaljerat |
| `sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT` | Lagg till iptables-regel |
| `sudo netfilter-persistent save` | Spara iptables-regler persistent |
| `sudo ss -tulnp` | Visa lyssnande portar for regelplanering |

------------------------------------------------------------

## Referenser

- UFW Documentation - Ubuntu community wiki for UFW-guider
- Netfilter/iptables - netfilter.org for officiell dokumentation
- DigitalOcean UFW Guide - Praktiska UFW-tutorials
- CIS Benchmarks - Brandvaggssektionen for enterprise-hardening
- NIST SP 800-41 - Guidelines on Firewalls and Firewall Policy
""",
        },
    ],
}
