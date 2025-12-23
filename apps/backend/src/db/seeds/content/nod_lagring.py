"""
NOD 2.6: Lagring (Disk/Partition/LUKS/Filsystem)
=================================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

LAGRING_NODE = {
    "title": "Lagring - Disk, Partition, LUKS & Filsystem",
    "slug": "lagring-disk-partition-luks-filsystem",
    "description": "Diskhantering, partitionering, kryptering och filsystem i Linux.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "order_index": 6,
    "content": r"""# Lagring - Disk, Partition, LUKS & Filsystem

> **TL;DR:** Disk → Partition → LUKS → Filsystem → Mountpoint. Som att bygga ett hus: mark (disk), grund (partition), lås (kryptering), möbler (filsystem), dörr (mountpoint).

---

## 📖 TEORI: Lagringslagret

### Fem lager av lagring

```
┌─────────────────────────────────────────────────┐
│  5. MOUNTPOINT  /mnt/data                       │  ← Ingången
├─────────────────────────────────────────────────┤
│  4. FILSYSTEM   ext4/xfs                        │  ← Möblerna
├─────────────────────────────────────────────────┤
│  3. KRYPTERING  LUKS                            │  ← Låset (valfritt)
├─────────────────────────────────────────────────┤
│  2. PARTITION   /dev/sdb1                       │  ← Grunden
├─────────────────────────────────────────────────┤
│  1. DISK        /dev/sdb                        │  ← Marken
└─────────────────────────────────────────────────┘
```

**Kursens analogi:**
- Partition = betongen (grund)
- Kryptering = glasyr (skydd)
- Filsystem = möblerna (organisation)

### Enhetsnamn

| Enhet | Beskrivning |
|-------|-------------|
| /dev/sda | Första SATA/SCSI-disken |
| /dev/sdb | Andra disken |
| /dev/sdb1 | Första partitionen på sdb |
| /dev/nvme0n1 | Första NVMe-disken |
| /dev/nvme0n1p1 | Första partitionen på NVMe |

---

## 📖 Steg 1: Visa diskar

### lsblk (List Block devices)

```bash
# Lista alla block devices
lsblk

# Med mer info
lsblk -f   # Filsystem-info

# Typisk output:
NAME   SIZE TYPE FSTYPE MOUNTPOINT
sda    50G  disk
├─sda1  1G  part ext4   /boot
└─sda2 49G  part ext4   /
sdb    20G  disk
```

### fdisk -l

```bash
# Lista alla diskar och partitioner
sudo fdisk -l

# Bara en specifik disk
sudo fdisk -l /dev/sdb
```

---

## 📖 Steg 2: Partitionera med fdisk

```bash
# Starta fdisk för en disk
sudo fdisk /dev/sdb
```

### fdisk-kommandon (inuti programmet)

| Kommando | Betydelse |
|----------|-----------|
| m | Hjälp (manual) |
| p | Print - visa partitioner |
| n | New - skapa partition |
| d | Delete - ta bort partition |
| t | Type - ändra partitionstyp |
| w | Write - spara och avsluta |
| q | Quit - avsluta utan att spara |

### Skapa partition (interaktivt)

```bash
sudo fdisk /dev/sdb

# Inuti fdisk:
Command: n        # Ny partition
Select: p         # Primary
Partition: 1      # Nummer 1
First sector: ↵   # Enter för default
Last sector: ↵    # Enter för hela disken

Command: w        # Write/spara
```

---

## 📖 Steg 3: Kryptering med LUKS

### Vad är LUKS?
**Linux Unified Key Setup** - Standard för diskkryptering.

### Skapa krypterad volym

```bash
# 1. Kryptera partitionen (RADERAR DATA!)
sudo cryptsetup luksFormat /dev/sdb1

# Bekräfta med YES (versaler)
# Ange lösenord
```

### Öppna krypterad volym

```bash
# 2. Öppna (dekryptera)
sudo cryptsetup luksOpen /dev/sdb1 krypterad_disk

# Nu finns: /dev/mapper/krypterad_disk
```

### Stäng krypterad volym

```bash
# Stäng (lås) volymen
sudo cryptsetup luksClose krypterad_disk
```

---

## 📖 Steg 4: Skapa filsystem

### mkfs - Make Filesystem

```bash
# ext4 (vanligast på Linux)
sudo mkfs.ext4 /dev/sdb1

# Med kryptering:
sudo mkfs.ext4 /dev/mapper/krypterad_disk

# xfs
sudo mkfs.xfs /dev/sdb1
```

### Vanliga filsystem

| Filsystem | Användning |
|-----------|------------|
| ext4 | Standard Linux |
| xfs | Enterprise/stora filer |
| btrfs | Modern, snapshots |
| vfat | USB-stickor, delning med Windows |

---

## 📖 Steg 5: Montera

### mount

```bash
# Skapa mountpoint
sudo mkdir -p /mnt/data

# Montera
sudo mount /dev/sdb1 /mnt/data

# Med kryptering:
sudo mount /dev/mapper/krypterad_disk /mnt/data
```

### Verifiera

```bash
# Kolla monterade filsystem
df -h

# Eller
mount | grep sdb
```

### Avmontera

```bash
sudo umount /mnt/data
```

---

## 📖 Permanent montering i /etc/fstab

### Format

```bash
# /etc/fstab
# <device>           <mountpoint>  <type>  <options>    <dump> <pass>
/dev/sdb1            /mnt/data     ext4    defaults     0      2
UUID=abc123...       /mnt/backup   ext4    defaults     0      2
```

### Hitta UUID

```bash
# Visa UUID för alla enheter
sudo blkid

# Eller
lsblk -f
```

### Testa fstab utan omstart

```bash
# Montera allt i fstab
sudo mount -a

# Om fel → fixa innan omstart!
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Grundläggande disk setup

```bash
#!/usr/bin/env bash
set -e

DISK=/dev/sdb
MOUNT=/mnt/data

echo "=== Skapa partition ==="
# Skapa en partition som tar hela disken
echo -e "n\np\n1\n\n\nw" | sudo fdisk ${DISK}

echo "=== Skapa filsystem ==="
sudo mkfs.ext4 ${DISK}1

echo "=== Montera ==="
sudo mkdir -p ${MOUNT}
sudo mount ${DISK}1 ${MOUNT}

echo "=== Verifiera ==="
df -h ${MOUNT}
```

### Exempel 2: Krypterad disk komplett

```bash
#!/usr/bin/env bash
set -e

DISK=/dev/sdb
PARTITION=${DISK}1
MAPPER_NAME=encrypted_data
MOUNT=/mnt/encrypted

echo "=== 1. Partitionera ==="
echo -e "n\np\n1\n\n\nw" | sudo fdisk ${DISK}

echo "=== 2. LUKS-kryptera ==="
# OBS: Interaktivt - kräver YES och lösenord
sudo cryptsetup luksFormat ${PARTITION}

echo "=== 3. Öppna krypterad volym ==="
sudo cryptsetup luksOpen ${PARTITION} ${MAPPER_NAME}

echo "=== 4. Skapa filsystem ==="
sudo mkfs.ext4 /dev/mapper/${MAPPER_NAME}

echo "=== 5. Montera ==="
sudo mkdir -p ${MOUNT}
sudo mount /dev/mapper/${MAPPER_NAME} ${MOUNT}

echo "=== Klart! ==="
lsblk
df -h ${MOUNT}
```

### Exempel 3: Avmontera och stäng krypterad disk

```bash
#!/usr/bin/env bash
MAPPER_NAME=encrypted_data
MOUNT=/mnt/encrypted

# 1. Avmontera
sudo umount ${MOUNT}

# 2. Stäng kryptering (låser volymen)
sudo cryptsetup luksClose ${MAPPER_NAME}

echo "Disk låst och avmonterad!"
```

### Exempel 4: fstab-entry för permanent montering

```bash
#!/usr/bin/env bash

DEVICE=/dev/sdb1
MOUNT=/mnt/data

# Hämta UUID
UUID=$(sudo blkid -s UUID -o value ${DEVICE})

# Skapa backup av fstab
sudo cp /etc/fstab /etc/fstab.backup

# Lägg till entry
echo "UUID=${UUID}  ${MOUNT}  ext4  defaults  0  2" | sudo tee -a /etc/fstab

# Testa!
sudo mount -a
df -h ${MOUNT}
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | lsblk visar? | Lista block devices (diskar/partitioner) |
| 2 | fdisk /dev/sdb gör? | Startar partitioneringsverktyget |
| 3 | fdisk: n gör? | Skapar ny partition |
| 4 | fdisk: w gör? | Skriver ändringar och avslutar |
| 5 | cryptsetup luksFormat gör? | Krypterar partition (raderar data!) |
| 6 | cryptsetup luksOpen gör? | Dekrypterar och öppnar volymen |
| 7 | mkfs.ext4 gör? | Skapar ext4-filsystem |
| 8 | mount /dev/sdb1 /mnt/data gör? | Monterar partition till katalog |
| 9 | /etc/fstab används för? | Automatisk montering vid boot |
| 10 | blkid visar? | UUID för alla enheter |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Rätt ordning för disk setup?**
- A) Filsystem → Partition → Mount
- B) Partition → Filsystem → Mount ✅
- C) Mount → Partition → Filsystem
- D) Filsystem → Mount → Partition

**2. Vad visar lsblk?**
- A) Bara monterade diskar
- B) Alla block devices ✅
- C) Bara partitioner
- D) Bara LUKS-volymer

**3. Hur skapar du en partition i fdisk?**
- A) c
- B) p
- C) n ✅
- D) w

**4. Hur sparar du ändringar i fdisk?**
- A) s
- B) q
- C) w ✅
- D) p

**5. Vad gör cryptsetup luksFormat?**
- A) Formaterar till ext4
- B) Krypterar partitionen ✅
- C) Monterar disk
- D) Öppnar krypterad volym

**6. Var hamnar öppnad LUKS-volym?**
- A) /dev/luks/
- B) /dev/mapper/ ✅
- C) /dev/crypt/
- D) /mnt/

**7. Hur stänger du en LUKS-volym?**
- A) cryptsetup close
- B) cryptsetup luksClose ✅
- C) umount
- D) cryptsetup lock

**8. Vilket kommando skapar ext4-filsystem?**
- A) format ext4
- B) mkfs.ext4 ✅
- C) mkext4
- D) newfs ext4

**9. Var konfigureras permanent montering?**
- A) /etc/mount
- B) /etc/fstab ✅
- C) /etc/disk
- D) /etc/volumes

**10. Hur testar du fstab utan omstart?**
- A) fstab --test
- B) mount -a ✅
- C) mount --test
- D) systemctl reload fstab

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Utforska diskar
```bash
# 1. Lista block devices
lsblk

# 2. Med filsystem-info
lsblk -f

# 3. Lista diskar med fdisk
sudo fdisk -l

# 4. Visa UUIDs
sudo blkid
```

### Övning 2: Simulera partitionering (read-only)
```bash
# Skapa en fil som disk (för övning)
dd if=/dev/zero of=/tmp/fake_disk bs=1M count=100

# Skapa loop device
sudo losetup /dev/loop0 /tmp/fake_disk

# Partitionera
sudo fdisk /dev/loop0
# Prova: n, p, 1, Enter, Enter, p, w

# Skapa filsystem
sudo mkfs.ext4 /dev/loop0

# Montera
sudo mkdir -p /mnt/test
sudo mount /dev/loop0 /mnt/test

# Verifiera
df -h /mnt/test

# Städa
sudo umount /mnt/test
sudo losetup -d /dev/loop0
rm /tmp/fake_disk
```

### Övning 3: Läs fstab
```bash
# Visa fstab
cat /etc/fstab

# Förstå kolumner:
# 1. Device/UUID
# 2. Mountpoint
# 3. Filsystemtyp
# 4. Options
# 5. Dump (0=no)
# 6. Pass (boot check order)
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Glömma fdisk w | Partitionen sparas inte | Alltid avsluta med w |
| luksFormat utan backup | Data raderas permanent | Backup först! |
| Fel enhet vid fdisk | Raderar fel disk! | Dubbelkolla med lsblk |
| Glömma mount -a test | System bootar inte | Testa alltid före omstart |

---

## 📝 SAMMANFATTNING

```bash
# VISA DISKAR
lsblk
lsblk -f
sudo fdisk -l
sudo blkid

# PARTITIONERA
sudo fdisk /dev/sdb
# n = new, p = primary, w = write

# KRYPTERA (LUKS)
sudo cryptsetup luksFormat /dev/sdb1    # Skapa
sudo cryptsetup luksOpen /dev/sdb1 namn  # Öppna
sudo cryptsetup luksClose namn           # Stäng

# FILSYSTEM
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.ext4 /dev/mapper/namn

# MONTERA
sudo mkdir -p /mnt/data
sudo mount /dev/sdb1 /mnt/data
sudo umount /mnt/data

# PERMANENT (fstab)
# UUID=xxx  /mnt/data  ext4  defaults  0  2
sudo mount -a  # Testa!

# ORDNING: Disk → Partition → LUKS → Filsystem → Mount
```

"""
}

