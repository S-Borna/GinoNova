"""
NOD 2.7: Backup med tar
=======================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

BACKUP_TAR_NODE = {
    "title": "Backup med tar",
    "slug": "backup-med-tar",
    "description": "Arkivering och backup med tar - flaggor, komprimering, inkrementell backup.",
    "difficulty": "medium",
    "estimated_minutes": 40,
    "xp_reward": 100,
    "order_index": 7,
    "content": r"""# Backup med tar

> **TL;DR:** `tar -czvf backup.tar.gz /katalog` = skapa komprimerad backup. `tar -xzvf backup.tar.gz` = extrahera.

---

## 📖 TEORI: Vad är tar?

**tar** = Tape ARchive
- Ursprungligen för bandbackup
- Samlar filer till ETT arkiv
- Kombineras med komprimering (gzip, bzip2, xz)

### De viktigaste flaggorna

| Flagga | Betydelse | Minnesteknik |
|--------|-----------|--------------|
| c | Create - skapa arkiv | **C**reate |
| x | eXtract - packa upp | e**X**tract |
| t | lisT - visa innehåll | lis**T** |
| v | Verbose - visa vad som händer | **V**erbose |
| f | File - ange filnamn | **F**ile |
| z | gZip-komprimering | g**Z**ip |
| j | bzip2-komprimering | bzip**2** → j |
| J | xz-komprimering (bäst) | **X**z → J |
| p | Preserve permissions | **P**ermissions |
| C | Change directory | **C**hange dir |

### Komprimeringsformat

| Flagga | Format | Ändelse | Komprimering |
|--------|--------|---------|--------------|
| z | gzip | .tar.gz / .tgz | Snabb, ok |
| j | bzip2 | .tar.bz2 | Långsam, bra |
| J | xz | .tar.xz | Långsam, bäst |
| (ingen) | ingen | .tar | Ingen komprimering |

---

## 📖 Skapa arkiv (c)

### Grundläggande

```bash
# Utan komprimering
tar -cvf arkiv.tar katalog/

# Med gzip (vanligast)
tar -czvf arkiv.tar.gz katalog/

# Med bzip2
tar -cjvf arkiv.tar.bz2 katalog/

# Med xz (bäst komprimering)
tar -cJvf arkiv.tar.xz katalog/
```

### Med datum i filnamn

```bash
# YYYY-MM-DD format (sorterar kronologiskt!)
tar -czvf backup_$(date +%Y-%m-%d).tar.gz /home/user/

# Eller med tid
tar -czvf backup_$(date +%Y-%m-%d_%H%M).tar.gz /data/
```

### Exkludera filer

```bash
# Exkludera en katalog
tar -czvf backup.tar.gz --exclude='*.log' /data/

# Exkludera flera
tar -czvf backup.tar.gz \
    --exclude='*.log' \
    --exclude='cache/*' \
    --exclude='tmp/*' \
    /data/
```

---

## 📖 Extrahera arkiv (x)

### Grundläggande

```bash
# gzip
tar -xzvf arkiv.tar.gz

# bzip2
tar -xjvf arkiv.tar.bz2

# xz
tar -xJvf arkiv.tar.xz
```

### Extrahera till specifik katalog

```bash
# -C = Change directory
tar -xzvf arkiv.tar.gz -C /mnt/restore/
```

### Bevara permissions

```bash
# -p = preserve permissions
sudo tar -xzvpf arkiv.tar.gz -C /
```

---

## 📖 Lista innehåll (t)

```bash
# Visa vad som finns i arkivet
tar -tzvf arkiv.tar.gz

# Utan verbose (bara filer)
tar -tzf arkiv.tar.gz

# Sök efter specifik fil
tar -tzf arkiv.tar.gz | grep "filename"
```

---

## 📖 Inkrementell backup

### Vad är inkrementell?
- **Full backup**: Allt varje gång
- **Inkrementell**: Bara ändrade filer sedan förra

### Med snapshot-fil (-g)

```bash
# Första körningen (full backup)
tar -czvf backup_full.tar.gz -g snapshot.snar /data/

# Efterföljande körningar (inkrementella)
tar -czvf backup_incr_$(date +%Y-%m-%d).tar.gz -g snapshot.snar /data/
```

### Hur det fungerar

```
snapshot.snar innehåller:
- Filnamn
- Tidsstämplar
- Metadata

tar jämför och tar bara med ändrade filer!
```

### Restore av inkrementell

```bash
# 1. Först full backup
tar -xzvf backup_full.tar.gz -g /dev/null -C /restore/

# 2. Sedan varje inkrementell i ordning
tar -xzvf backup_incr_2024-01-02.tar.gz -g /dev/null -C /restore/
tar -xzvf backup_incr_2024-01-03.tar.gz -g /dev/null -C /restore/
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Enkel backup-rutin

```bash
#!/usr/bin/env bash

# Variabler
SOURCE="/home/user/important"
DEST="/backup"
DATE=$(date +%Y-%m-%d)
FILENAME="backup_${DATE}.tar.gz"

# Skapa backup
tar -czvf "${DEST}/${FILENAME}" "${SOURCE}"

echo "Backup skapad: ${DEST}/${FILENAME}"
```

### Exempel 2: Backup med exclude

```bash
#!/usr/bin/env bash

SOURCE="/var/www"
DEST="/backup"
DATE=$(date +%Y-%m-%d)

tar -czvf "${DEST}/www_${DATE}.tar.gz" \
    --exclude='*.log' \
    --exclude='cache/*' \
    --exclude='node_modules/*' \
    --exclude='.git/*' \
    "${SOURCE}"
```

### Exempel 3: Inkrementell backup-script

```bash
#!/usr/bin/env bash
# Från kursmaterialet

SOURCE="/data"
DEST="/backup"
SNAPSHOT="${DEST}/snapshot.snar"
DATE=$(date +%Y-%m-%d)

# Kolla om snapshot finns (avgör om full eller inkr)
if [[ -f "${SNAPSHOT}" ]]; then
    TYPE="incr"
else
    TYPE="full"
fi

FILENAME="backup_${TYPE}_${DATE}.tar.gz"

# Kör backup
tar -czvf "${DEST}/${FILENAME}" -g "${SNAPSHOT}" "${SOURCE}"

echo "=== ${TYPE^^} backup klar ==="
echo "Fil: ${FILENAME}"
```

### Exempel 4: Komplett backup-system

```bash
#!/usr/bin/env bash
set -e

# Konfiguration
SOURCE="/home/user"
BACKUP_DIR="/backup"
RETENTION=7  # Behåll 7 dagar

DATE=$(date +%Y-%m-%d)
FILENAME="backup_${DATE}.tar.gz"

# Skapa katalog om den inte finns
mkdir -p "${BACKUP_DIR}"

echo "=== Startar backup ==="

# Skapa backup
tar -czvf "${BACKUP_DIR}/${FILENAME}" \
    --exclude='*.tmp' \
    --exclude='cache/*' \
    "${SOURCE}"

# Ta bort gamla backups
find "${BACKUP_DIR}" -name "backup_*.tar.gz" -mtime +${RETENTION} -delete

echo "=== Backup klar ==="
ls -lh "${BACKUP_DIR}/${FILENAME}"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | tar -c gör? | Create - skapar arkiv |
| 2 | tar -x gör? | eXtract - packar upp |
| 3 | tar -t gör? | lisT - visar innehåll |
| 4 | tar -v gör? | Verbose - visar filer |
| 5 | tar -f gör? | File - anger filnamn |
| 6 | tar -z gör? | gZip-komprimering |
| 7 | tar -j gör? | bzip2-komprimering |
| 8 | tar -J gör? | xz-komprimering (bäst) |
| 9 | tar -C gör? | Change dir vid extract |
| 10 | tar -g gör? | Inkrementell backup (snapshot) |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad betyder c i tar -cvf?**
- A) Compress
- B) Create ✅
- C) Copy
- D) Check

**2. Vilken flagga extraherar arkiv?**
- A) e
- B) u
- C) x ✅
- D) o

**3. Vilken flagga ger gzip-komprimering?**
- A) g
- B) z ✅
- C) c
- D) p

**4. Hur listar du innehåll i ett arkiv?**
- A) tar -l
- B) tar -t ✅
- C) tar -v
- D) tar -s

**5. Vilket kommando skapar .tar.gz?**
- A) tar -cvf
- B) tar -czvf ✅
- C) tar -cjvf
- D) tar -xzvf

**6. Flaggan -C vid extract gör?**
- A) Komprimerar
- B) Byter målkatalog ✅
- C) Skapar katalog
- D) Checkar arkiv

**7. Vad används -g för?**
- A) gzip-komprimering
- B) Inkrementell backup ✅
- C) Gruppägare
- D) Global sökning

**8. Vilken komprimering är bäst?**
- A) gzip (-z)
- B) bzip2 (-j)
- C) xz (-J) ✅
- D) Ingen skillnad

**9. Varför date +%Y-%m-%d format?**
- A) ISO-standard
- B) Kortare namn
- C) Sorterar kronologiskt ✅
- D) Komprimerar bättre

**10. Hur exkluderar du filer?**
- A) --skip=
- B) --exclude= ✅
- C) --ignore=
- D) --without=

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande tar
```bash
# Skapa testfiler
mkdir -p /tmp/tartest
echo "fil1" > /tmp/tartest/test1.txt
echo "fil2" > /tmp/tartest/test2.txt

# 1. Skapa arkiv
tar -cvf /tmp/test.tar /tmp/tartest/

# 2. Lista innehåll
tar -tvf /tmp/test.tar

# 3. Packa upp
mkdir /tmp/restore
tar -xvf /tmp/test.tar -C /tmp/restore/

# 4. Verifiera
ls -la /tmp/restore/tmp/tartest/

# Städa
rm -rf /tmp/tartest /tmp/test.tar /tmp/restore
```

### Övning 2: Komprimering
```bash
# Skapa testdata
mkdir -p /tmp/comptest
dd if=/dev/urandom of=/tmp/comptest/data.bin bs=1M count=10

# Jämför komprimering
tar -cvf /tmp/test.tar /tmp/comptest/
tar -czvf /tmp/test.tar.gz /tmp/comptest/
tar -cjvf /tmp/test.tar.bz2 /tmp/comptest/
tar -cJvf /tmp/test.tar.xz /tmp/comptest/

# Jämför storlekar
ls -lh /tmp/test.tar*

# Städa
rm -rf /tmp/comptest /tmp/test.tar*
```

### Övning 3: Datum och exclude
```bash
# Backup med datum
DATE=$(date +%Y-%m-%d)
tar -czvf "/tmp/backup_${DATE}.tar.gz" \
    --exclude='*.log' \
    /etc/

# Verifiera
ls -lh /tmp/backup_*.tar.gz
tar -tzf /tmp/backup_*.tar.gz | head

# Städa
rm /tmp/backup_*.tar.gz
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Glömma f | stdin/stdout | Ange alltid -f filnamn |
| Fel ordning på flaggor | Funkar ändå oftast | cvf inte fvc |
| Fel komprimering vid extract | Fel/korrupt | Matcha: -z för .gz |
| Absoluta paths i arkiv | Svårt att restore | Använd relativa paths |

---

## 📝 SAMMANFATTNING

```bash
# SKAPA (c = create)
tar -cvf arkiv.tar katalog/          # Ingen komprimering
tar -czvf arkiv.tar.gz katalog/      # gzip
tar -cjvf arkiv.tar.bz2 katalog/     # bzip2
tar -cJvf arkiv.tar.xz katalog/      # xz (bäst)

# EXTRAHERA (x = extract)
tar -xzvf arkiv.tar.gz               # Till nuvarande
tar -xzvf arkiv.tar.gz -C /mnt/      # Till specifik katalog

# LISTA (t = list)
tar -tzvf arkiv.tar.gz

# DATUM I FILNAMN
tar -czvf backup_$(date +%Y-%m-%d).tar.gz /data/

# EXCLUDE
tar -czvf backup.tar.gz --exclude='*.log' /data/

# INKREMENTELL (-g snapshot)
tar -czvf full.tar.gz -g snap.snar /data/    # Första
tar -czvf incr.tar.gz -g snap.snar /data/    # Efterföljande

# FLAGGOR ATT MINNAS
# c = Create
# x = eXtract
# t = lisT
# v = Verbose
# f = File
# z = gZip
# j = bzip2
# J = xz
# C = Change dir
# g = snapshot (inkrementell)
```

"""
}

