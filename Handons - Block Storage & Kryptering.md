# Block Storage & Kryptering
## Hands-On Demonstration: Disk, Partition, Encryption, Filesystem

---

## 📋 Innehållsförteckning

1. [Hierarkin - Övergripande](#hierarkin---övergripande)
2. [Lägga till en Ny Disk](#lägga-till-en-ny-disk)
3. [Partitionering med fdisk](#partitionering-med-fdisk)
4. [Kryptering med LUKS](#kryptering-med-luks)
5. [Skapa Filsystem](#skapa-filsystem)
6. [Mount och Unmount](#mount-och-unmount)
7. [Obligatorisk Assignment](#obligatorisk-assignment)
8. [Viktiga Koncept](#viktiga-koncept)
9. [Kommandoreferens](#kommandoreferens)

---

## 🏗️ Hierarkin - Övergripande

### Lagren från Hårdvara till Tillgänglig Data

```
┌─────────────────────────────────────┐
│   FYSISK DISK (Hårdvara)            │
│   /dev/sdb (5 GB)                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   PARTITION                          │
│   /dev/sdb1 (5 GB)                  │
│   (Logisk uppdelning av disk)       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   KRYPTERING (Valfritt)             │
│   /dev/mapper/cryptodisk            │
│   (LUKS-krypterad volym)            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   FILSYSTEM                          │
│   ext4                               │
│   (Organiserar filer och mappar)    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   MOUNT POINT                        │
│   /mnt                               │
│   (Tillgängligt i filträdet)        │
└─────────────────────────────────────┘
```

### Varför Denna Ordning?

1. **Disk (Device)** - Fysisk eller virtuell hårdvara
2. **Partition** - Logisk uppdelning (även om bara en partition)
3. **Kryptering** - Säkerhetslager (valfritt)
4. **Filsystem** - Struktur för data
5. **Mount Point** - Åtkomstpunkt i filträdet

⚠️ **VIKTIGT**: Ordningen är kritisk och kan inte ändras!

---

## 💿 Lägga till en Ny Disk

### I VirtualBox

**Steg 1: Stäng av VM**
```bash
sudo systemctl poweroff
```

**Steg 2: VirtualBox Settings**
1. Högerklicka på VM → Settings
2. Storage → Controller: SATA
3. Klicka på "+" för att lägga till disk
4. "Create new disk" → VDI → Dynamically allocated
5. Storlek: 5 GB (eller valfri storlek)
6. OK

**Steg 3: Starta VM**
```bash
# Starta utan GUI
```

### Verifiera Ny Disk

**Lista alla block devices:**
```bash
lsblk
```

**Output exempel:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   24G  0 part /
sdb      8:16   0    5G  0 disk
sr0     11:0    1 1024M  0 rom
```

**Förklaring:**
- `sda` - Första disken (25 GB, root-disk)
  - `sda1` - Boot-partition (1 GB)
  - `sda2` - Root-partition (24 GB)
- `sdb` - **Nya disken** (5 GB, omonterad)
- `sr0` - Virtuell CD/DVD-läsare

**Kontrollera device-filer:**
```bash
ls -l /dev/sd*
```

**Output:**
```
brw-rw---- 1 root disk 8,  0 Nov 28 10:00 /dev/sda
brw-rw---- 1 root disk 8,  1 Nov 28 10:00 /dev/sda1
brw-rw---- 1 root disk 8,  2 Nov 28 10:00 /dev/sda2
brw-rw---- 1 root disk 8, 16 Nov 28 10:00 /dev/sdb
```

- `b` = **Block device**
- `rw-rw----` = Permissions
- `/dev/sdb` = Hela disken
- Inga partitioner på `sdb` än

---

## 🔧 Partitionering med fdisk

### Varför Partitionera?

**Även för en partition:**
- Best practice att alltid partitionera
- Möjliggör framtida uppdelning
- Struktur och organisation

**Kommando:**
```bash
sudo fdisk /dev/sdb
```

⚠️ **VARNING**: Dubbelkolla att du anger rätt disk! Fel disk = dataförlust!

### fdisk - Interaktiv Session

**Viktiga kommandon i fdisk:**

| Kommando | Funktion |
|----------|----------|
| `m` | Visa hjälp |
| `p` | Print (visa partitioner) |
| `g` | Skapa GPT partition table |
| `n` | New partition |
| `w` | Write (spara ändringar) |
| `q` | Quit (avsluta utan att spara) |

### Steg-för-Steg Partitionering

**Steg 1: Starta fdisk**
```bash
sudo fdisk /dev/sdb
```

**Output:**
```
Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x...

Command (m for help):
```

**Steg 2: Skapa GPT Partition Table**
```
Command (m for help): g
```

**Output:**
```
Created a new GPT disklabel (GUID Partition Table).
```

**Steg 3: Visa nuvarande status**
```
Command (m for help): p
```

**Output:**
```
Disk /dev/sdb: 5 GiB
...
Disk identifier: ...

No partitions found
```

**Steg 4: Skapa ny partition**
```
Command (m for help): n
```

**Dialog:**
```
Partition number (1-128, default 1): [Enter]
First sector (2048-..., default 2048): [Enter]
Last sector (..., default ...): [Enter]

Created a new partition 1 of type 'Linux filesystem' and of size 5 GiB.
```

**Förklaring:**
- Partition number: 1 (default är bra)
- First sector: 2048 (default är bra)
- Last sector: Default tar hela disken

**Steg 5: Verifiera partition**
```
Command (m for help): p
```

**Output:**
```
Device     Start      End  Sectors Size Type
/dev/sdb1   2048 10485759 10483712   5G Linux filesystem
```

**Steg 6: Spara ändringar**
```
Command (m for help): w
```

**Output:**
```
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

⚠️ **VIKTIGT**: Ändringar sparas INTE förrän du trycker `w`!

### Verifiera Partitionen

```bash
lsblk
```

**Output:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb      8:16   0    5G  0 disk
└─sdb1   8:17   0    5G  0 part
```

Nu har vi en partition! ✅

---

## 🔐 Kryptering med LUKS

### Vad är LUKS?

**LUKS** = Linux Unified Key Setup
- Standard för disk-kryptering i Linux
- Krypterar hela partitioner
- Lösenordsskyddad
- Transparent kryptering/dekryptering

### cryptsetup - Huvudkommando

**Subkommandon:**
- `luksFormat` - Initiera LUKS-partition
- `open` - Öppna (dekryptera) volym
- `close` - Stäng (kryptera) volym
- `status` - Visa status

### Kryptera Partitionen

**Kommando:**
```bash
sudo cryptsetup luksFormat /dev/sdb1
```

⚠️ **VARNING**: Dubbelkolla partition! Fel partition = dataförlust!

**Dialog:**
```
WARNING!
========
This will overwrite data on /dev/sdb1 irrevocably.

Are you sure? (Type 'yes' in capital letters): YES

Enter passphrase for /dev/sdb1: [skriv lösenord]
Verify passphrase: [upprepa lösenord]
```

**Viktiga punkter:**
- Måste skriva **`YES`** i VERSALER
- Lösenordet syns INTE när du skriver (säkerhet)
- Lösenordslängden döljs för säkerhet (metadata)
- **Det finns INGET sätt att återställa lösenordet!**

### Varför Syns Inte Lösenordet?

**Säkerhet:**
- Längden på lösenordet är metadata
- Metadata hjälper vid lösenordsknäckning
- Ingen visuell feedback = säkrare

**Exempel:**
```
Synligt: ********  (8 tecken)
→ Angripare vet: "Lösenord är 8 tecken"

Osynligt:
→ Angripare vet: "Okänd längd"
```

### Öppna Krypterad Volym

**Kommando:**
```bash
sudo cryptsetup open /dev/sdb1 cryptodisk
```

**Förklaring:**
- `/dev/sdb1` - Partition att öppna
- `cryptodisk` - Namn på dekrypterad volym (välj själv)

**Dialog:**
```
Enter passphrase for /dev/sdb1: [lösenord]
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt
```

- `sdb1` = Krypterad partition
- `cryptodisk` = Dekrypterad volym (type: `crypt`)

### Device-fil för Krypterad Volym

```bash
ls -l /dev/mapper/cryptodisk
```

**Output:**
```
lrwxrwxrwx 1 root root 7 Nov 28 10:30 /dev/mapper/cryptodisk -> ../dm-0
```

- Länk till `/dev/dm-0`
- `dm` = Device Mapper

```bash
ls -l /dev/dm-0
```

**Output:**
```
brw-rw---- 1 root disk 253, 0 Nov 28 10:30 /dev/dm-0
```

- Block device (`b`)
- Används för att skapa filsystem

---

## 📁 Skapa Filsystem

### mkfs - Make Filesystem

**Kommando:**
```bash
sudo mkfs.ext4 /dev/mapper/cryptodisk
```

**Förklaring:**
- `mkfs.ext4` - Skapa ext4-filsystem
- `/dev/mapper/cryptodisk` - På krypterad volym

**Output:**
```
mke2fs 1.46.5 (30-Dec-2021)
Creating filesystem with 1310720 4k blocks and 327680 inodes
Filesystem UUID: ...
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```

**Nu har vi:**
- ✅ Disk
- ✅ Partition
- ✅ Kryptering
- ✅ Filsystem

### Varför ext4?

**Ext4 (Extended File System 4):**
- Standard i de flesta Linux-distributioner
- Journaling (återhämtning vid krasch)
- Lost+Found för återhämtning
- Snabb och pålitlig

**Andra alternativ:**
- `ext3` - Äldre version
- `xfs` - Bra för stora filer
- `btrfs` - Avancerad (snapshots, compression)
- `fat32` - Windows-kompatibel
- `ntfs` - Windows native

---

## 🔗 Mount och Unmount

### Vad är Mount?

**Mount** = Göra ett filsystem tillgängligt i filträdet

**Koncept:**
```
Innan mount:
/mnt/  [tom mapp]

Efter mount av cryptodisk till /mnt:
/mnt/  [cryptodisk innehåll]
```

### Mount-kommandot

**Syntax:**
```bash
sudo mount [device] [mount-point]
```

**Exempel:**
```bash
sudo mount /dev/mapper/cryptodisk /mnt
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt /mnt
```

Nu är `cryptodisk` monterad på `/mnt`! ✅

### Undersöka Monterad Volym

```bash
ls -la /mnt
```

**Output:**
```
total 24
drwxr-xr-x  3 root root  4096 Nov 28 10:35 .
drwxr-xr-x 19 root root  4096 Nov 28 10:00 ..
drwx------  2 root root 16384 Nov 28 10:35 lost+found
```

**lost+found:**
- Speciell mapp i ext4
- För journaling och återhämtning
- Används vid filsystem-krasch
- Mer pålitligt: Ha backups och RAID!

### Skapa Filer på Krypterad Volym

```bash
sudo touch /mnt/my-secret-encrypted-file
```

```bash
ls -l /mnt
```

**Output:**
```
drwx------  2 root root 16384 Nov 28 10:35 lost+found
-rw-r--r--  1 root root     0 Nov 28 10:40 my-secret-encrypted-file
```

**Innehåll i fil:**
```bash
echo "This is secret!" | sudo tee /mnt/my-secret-encrypted-file
cat /mnt/my-secret-encrypted-file
```

**Output:**
```
This is secret!
```

### Filen är Inte Krypterad?

**Viktigt att förstå:**
- Filen på disk ÄR krypterad (nollor och ettor)
- Kryptering/dekryptering sker transparent vid läs/skriv
- När volymen är "öppen" (monterad) → data tillgänglig
- När volymen är "stängd" (krypterad) → data otillgänglig

**Visualisering:**
```
DISK (fysiskt):
[Krypterade nollor och ettor - ej läsbart]

↓ cryptsetup open (med lösenord)

RAM (dekrypterat):
[This is secret! - läsbart]
```

### df - Disk Free

**Visa monterade filsystem:**
```bash
df -h
```

**Output:**
```
Filesystem              Size  Used Avail Use% Mounted on
/dev/mapper/cryptodisk  5.0G   24M  4.7G   1% /mnt
/dev/sda2                24G  5.5G   17G  25% /
```

**Förklaring:**
- `-h` = Human-readable (GB, MB istället för bytes)
- Visar bara monterade filsystem
- Krypterad disk visas när monterad

### Unmount

**Kommando:**
```bash
sudo umount /mnt
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt
```

Mount point borta! Men `cryptodisk` finns kvar (öppen).

```bash
ls /mnt
```

**Output:**
```
(tom eller ursprungligt innehåll)
```

### Mount "Tar Över" en Mapp

**Koncept:**

```bash
# Skapa fil i /mnt (inte monterad)
sudo touch /mnt/myfile
ls /mnt
# Output: myfile

# Montera cryptodisk på /mnt
sudo mount /dev/mapper/cryptodisk /mnt
ls /mnt
# Output: lost+found  my-secret-encrypted-file
# myfile är "gömd"

# Unmount
sudo umount /mnt
ls /mnt
# Output: myfile
# myfile tillbaka!
```

**Analogi - Heltäckningsmatta:**
- Stengolv = `/mnt/myfile`
- Matta = Monterad volym
- Mattan täcker golvet temporärt
- Ta bort mattan → golvet synligt igen

### Stänga Krypterad Volym

**Fel ordning (fails):**
```bash
sudo cryptsetup close cryptodisk
# Error: Device cryptodisk is still in use
```

**Rätt ordning:**
```bash
# 1. Unmount först
sudo umount /mnt

# 2. Stäng krypterad volym
sudo cryptsetup close cryptodisk
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb      8:16   0    5G  0 disk
└─sdb1   8:17   0    5G  0 part
```

`cryptodisk` borta! Volymen är nu krypterad och ej tillgänglig. ✅

---

## 📋 Obligatorisk Assignment

### Uppgiftsbeskrivning

**Skapa ett automatiskt backup-system:**

1. **Backup-verktyg:** Restic
2. **Källa:** Ubuntu VM (hemmamapp eller del av)
3. **Destination:** Fedora VM (eller tvärtom)
4. **Automation:** systemd timer + service
5. **Trigger:** 5 minuter efter boot
6. **Inlämning:** Git repo på `git.chasslab.dev`

### Komponenter

**1. Systemd Service**
- Kör restic backup
- Definierar vad som ska köras

**2. Systemd Timer**
- Triggar service
- 5 minuter efter boot
- `OnBootSec=5min`

**3. Restic**
- Backup-verktyg
- Inkrementella backups
- Kryptering
- Deduplicering

### GitLab - git.chasslab.dev

**Registrera dig:**
1. Gå till: https://git.chasslab.dev
2. Registrera med **@chassutbildning.se** email
3. Vänta på godkännande (1 arbetsdag)

**Skapa repo:**
1. New Project
2. Project name: `linux-backup` (eller valfritt)
3. Private eller Public (din val)
4. Create project

**Innehåll i repo:**
```
backup-system/
├── README.md              # Dokumentation
├── backup.service         # Systemd service-fil
├── backup.timer           # Systemd timer-fil
└── scripts/
    └── backup.sh          # Backup-script (om du vill)
```

### Inlämning

**Vad ska lämnas in:**
- ✅ Länk till Git repo på `git.chasslab.dev`

**Vad ska INTE lämnas in:**
- ❌ Dokument
- ❌ Text
- ❌ Zipfiler
- ❌ Screenshots

**Deadline:**
- Slutet av kursen
- Obligatoriskt för betyg
- Börja tidigt!

### Varför Detta är Viktigt

**Praktisk användning:**
- När ni får molnservrar kommer de resettas ibland
- Automatiska backups = ingen dataförlust
- Systemd automation = "set it and forget it"

**Lärande:**
- Systemd timers och services
- Backup-strategi
- Git för versionhantering
- Automation

---

## 💡 Viktiga Koncept

### Block Devices

**Vad är en Block Device?**
- Hanterar data i "block" (chunks)
- Random access (kan läsa vilken del som helst)
- Exempel: Hårddiskar, USB-stickor, SD-kort

**Identifiering:**
```bash
ls -l /dev/sdb
# brw-rw---- ... /dev/sdb
# ↑
# b = Block device
```

**Jämförelse:**
- Block device (`b`) - Hårddisk, USB
- Character device (`c`) - Keyboard, mouse
- Directory (`d`) - Mapp
- Regular file (`-`) - Vanlig fil

### Allt är en Fil

**Linux-filosofi:**
- Disk = Fil (`/dev/sdb`)
- Partition = Fil (`/dev/sdb1`)
- Krypterad volym = Fil (`/dev/mapper/cryptodisk`)

**Varför?**
- Enhetligt interface
- Samma kommandon för allt
- Flexibilitet

### Kryptering - Software vs Hardware

**Software Encryption (LUKS):**
- Kryptering sker i OS
- Data på disk: Alltid krypterad
- Data i minne: Dekrypterad
- Minimal overhead

**När är data säker?**
- ✅ Disk stulen (utan lösenord)
- ✅ Dator avstängd
- ❌ Dator på och volym öppen
- ❌ Någon har lösenordet

### Sync - Säkerställ Skrivningar

**Problem:**
- Skrivningar kan cachas (köas)
- USB bortkopplad innan skrivet = korrupt data

**Lösning:**
```bash
sudo sync
```

**Vad gör sync?**
- Tvingar alla cachade skrivningar att slutföras
- Säkerställer att data är på disk
- Bra innan unmount eller bortkoppling

**Bästa praxis:**
```bash
# 1. Synka cachade skrivningar
sudo sync

# 2. Unmount
sudo umount /mnt

# 3. Säkert att koppla bort
```

### Lost+Found

**Vad är lost+found?**
- Speciell mapp i ext4 (journaled filesystem)
- Återhämtning vid filsystem-krasch
- Innehåller "hittade" filer vid fsck

**Pålitlighet:**
- ⚠️ Inte 100% pålitlig
- ✅ Bättre: Regelbundna backups
- ✅ Bättre: RAID för redundans

---

## 📖 Kommandoreferens

### Disk Management

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `lsblk` | Lista block devices | `lsblk` |
| `fdisk` | Partitionera disk | `sudo fdisk /dev/sdb` |
| `parted` | Alternativ till fdisk | `sudo parted /dev/sdb` |

### Kryptering

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `cryptsetup luksFormat` | Kryptera partition | `sudo cryptsetup luksFormat /dev/sdb1` |
| `cryptsetup open` | Öppna krypterad volym | `sudo cryptsetup open /dev/sdb1 name` |
| `cryptsetup close` | Stäng krypterad volym | `sudo cryptsetup close name` |
| `cryptsetup status` | Visa status | `sudo cryptsetup status name` |

### Filsystem

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `mkfs.ext4` | Skapa ext4-filsystem | `sudo mkfs.ext4 /dev/sdb1` |
| `mkfs.xfs` | Skapa xfs-filsystem | `sudo mkfs.xfs /dev/sdb1` |
| `mkfs.fat` | Skapa FAT-filsystem | `sudo mkfs.fat -F 32 /dev/sdb1` |

### Mount

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `mount` | Montera filsystem | `sudo mount /dev/sdb1 /mnt` |
| `umount` | Avmontera filsystem | `sudo umount /mnt` |
| `df` | Visa monterade filsystem | `df -h` |
| `sync` | Synka cachade skrivningar | `sudo sync` |

---

## 🎓 Steg-för-Steg Sammanfattning

### Komplett Process

**1. Lägg till disk i VirtualBox**
```
VirtualBox → Settings → Storage → Add Disk (5 GB)
```

**2. Verifiera disk**
```bash
lsblk
# Hitta ny disk (t.ex. sdb)
```

**3. Partitionera**
```bash
sudo fdisk /dev/sdb
# g (GPT table)
# n (new partition, alla defaults)
# w (write)
```

**4. Kryptera partition**
```bash
sudo cryptsetup luksFormat /dev/sdb1
# Skriv YES
# Ange lösenord (2 gånger)
```

**5. Öppna krypterad volym**
```bash
sudo cryptsetup open /dev/sdb1 cryptodisk
# Ange lösenord
```

**6. Skapa filsystem**
```bash
sudo mkfs.ext4 /dev/mapper/cryptodisk
```

**7. Montera**
```bash
sudo mount /dev/mapper/cryptodisk /mnt
```

**8. Använd**
```bash
cd /mnt
sudo touch secret-file
echo "Secret data" | sudo tee secret-file
```

**9. Avmontera (när klar)**
```bash
sudo umount /mnt
sudo cryptsetup close cryptodisk
```

---

## ⚠️ Säkerhetsvarningar

### Kritiska Punkter

**1. Rätt Disk/Partition**
```bash
# ✅ RÄTT
sudo fdisk /dev/sdb  # Ny disk

# ❌ FEL
sudo fdisk /dev/sda  # Root disk - FÖRSTÖR SYSTEMET!
```

**Alltid dubbelkolla med:**
```bash
lsblk
# Hitta rätt disk INNAN du kör kommandon
```

**2. Lösenord för LUKS**
- ❌ Finns INGET sätt att återställa
- ✅ Spara i lösenordshanterare
- ✅ Välj något du kommer ihåg
- ⚠️ Förlorat lösenord = förlorad data

**3. Unmount Innan Close**
```bash
# ✅ RÄTT ordning
sudo umount /mnt
sudo cryptsetup close cryptodisk

# ❌ FEL ordning
sudo cryptsetup close cryptodisk  # Fails!
sudo umount /mnt
```

**4. Sync Innan Unmount**
```bash
# ✅ SÄKERT
sudo sync
sudo umount /mnt

# ❌ RISKABELT
sudo umount /mnt  # Cachad data kan förloras
```

---

## 🎯 Sammanfattning

### Vad Vi Lärde Oss

1. ✅ Hierarkin: Disk → Partition → Encryption → Filesystem → Mount
2. ✅ Lägga till virtuella diskar i VirtualBox
3. ✅ Partitionera med fdisk
4. ✅ Kryptera med LUKS (cryptsetup)
5. ✅ Skapa filsystem (mkfs.ext4)
6. ✅ Montera och avmontera
7. ✅ Förstå mount points och hur de fungerar

### Nyckelpunkter

**Ordningen är Viktig:**
1. Device först
2. Partition på device
3. Kryptering på partition (valfritt)
4. Filsystem på kryptering/partition
5. Mount för att göra tillgängligt

**Säkerhet:**
- LUKS krypterar data på disk
- Lösenord MÅSTE kommas ihåg
- Data säker när volym stängd
- Data tillgänglig när volym öppen

**Mount Points:**
- `/mnt` - Manuella mounts
- `/media` - Automatiska mounts (USB, CD)
- Mount "tar över" en mapp temporärt

### Praktisk Tillämpning

**Assignment:**
- Automatisk backup med restic
- Systemd timer (5 min efter boot)
- Systemd service (kör backup)
- Git repo på git.chasslab.dev

**Varför Viktigt:**
- Backups = Ingen dataförlust
- Automation = Mindre manuellt arbete
- Systemd = Standard i Linux

### Nästa Steg

1. 📝 Registrera på git.chasslab.dev
2. 🔧 Börja planera backup-system
3. 📖 Läs man pages:
   - `man cryptsetup`
   - `man mount`
   - `man lsblk`
   - `man fdisk`
4. 🎯 Börja med assignment (deadline: kursslutet)

---

## 📚 Man Pages att Läsa

**Disk & Partition:**
```bash
man lsblk
man fdisk
man parted
```

**Kryptering:**
```bash
man cryptsetup
man cryptsetup-luksFormat
```

**Filsystem:**
```bash
man mkfs
man mkfs.ext4
man mount
man umount
```

**Övrigt:**
```bash
man df
man sync
```

---

**Lycka till med disk management och kryptering! 🔐**

*Allt är en fil - även dina hemligheter (när de är krypterade)!*