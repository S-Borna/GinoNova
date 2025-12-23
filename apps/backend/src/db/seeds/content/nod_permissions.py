"""
NOD 2.2: Permissions (chmod/chown/SGID)
=======================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

PERMISSIONS_NODE = {
    "title": "Permissions - chmod/chown/SGID",
    "slug": "permissions-chmod-chown-sgid",
    "description": "Filrättigheter, ägande, SUID/SGID/Sticky bit för säker filhantering.",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "order_index": 2,
    "content": r"""# Permissions - chmod/chown/SGID

> **TL;DR:** `chmod 755` = rwxr-xr-x. `chown user:grupp fil`. SGID (2775) på kataloger = nya filer ärver gruppen. **s** på gruppen = SGID aktivt.

---

## 📖 TEORI: Grundläggande rättigheter

### Tre typer av permissions

| Symbol | Oktal | Betydelse för FIL | Betydelse för KATALOG |
|--------|-------|-------------------|----------------------|
| r | 4 | Läsa innehåll | Lista innehåll (ls) |
| w | 2 | Ändra innehåll | Skapa/ta bort filer |
| x | 1 | Köra som program | Gå in i katalogen (cd) |

### Tre nivåer

| Nivå | Symbol | Beskrivning |
|------|--------|-------------|
| Owner | u | Filens ägare |
| Group | g | Filens grupp |
| Others | o | Alla andra |
| All | a | Alla tre |

### Läsa permissions

```
-rwxr-xr-- 1 said developers 4096 Dec 23 file.txt
│├─┤├─┤├─┤
│ │  │  └── Others: r-- (4) = läsa
│ │  └───── Group: r-x (5) = läsa + köra
│ └──────── Owner: rwx (7) = allt
└────────── Filtyp: - = fil, d = katalog, l = länk
```

### Beräkna oktal

```
rwx = 4+2+1 = 7
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
--- = 0+0+0 = 0

Exempel:
rwxr-xr-- = 754
rwxrwxr-x = 775
rw-r--r-- = 644
```

---

## 📖 chmod - Ändra rättigheter

### Symbolisk notation

```bash
chmod u+x fil        # Lägg till execute för owner
chmod g-w fil        # Ta bort write för group
chmod o=r fil        # Sätt others till endast read
chmod a+x fil        # Lägg till execute för alla
chmod u+x,g+r fil    # Kombinera flera
chmod +x fil         # Lägg till x för alla (samma som a+x)
chmod -x fil         # Ta bort x för alla
```

### Oktal notation

| Oktal | Permissions | Användning |
|-------|-------------|------------|
| 755 | rwxr-xr-x | Skript, program |
| 644 | rw-r--r-- | Vanliga filer |
| 700 | rwx------ | Privata filer/kataloger |
| 750 | rwxr-x--- | Gruppdelad katalog |
| 777 | rwxrwxrwx | ⚠️ FARLIGT - undvik! |

```bash
chmod 755 skript.sh     # rwxr-xr-x
chmod 644 config.txt    # rw-r--r--
chmod 700 ~/.ssh        # rwx------
chmod -R 755 katalog    # Rekursivt
```

---

## 📖 chown - Ändra ägare

```bash
# Ändra ägare
chown alice fil.txt

# Ändra ägare och grupp
chown alice:developers fil.txt

# Ändra endast grupp
chown :developers fil.txt

# Rekursivt
chown -R alice:developers /opt/project
```

## 📖 chgrp - Ändra grupp

```bash
chgrp developers fil.txt
chgrp -R developers /opt/project
```

---

## 📖 Speciella permissions (KRITISKT FÖR TENTA!)

### SUID (Set User ID) - 4xxx

**Fil körs med ÄGARENS rättigheter**, inte den som kör.

```bash
# Sätt SUID
chmod 4755 program
chmod u+s program

# Resultat:
-rwsr-xr-x    # 's' istället för 'x' på owner
```

**Exempel:** `/usr/bin/passwd` har SUID så vanliga användare kan ändra sitt lösenord (som kräver root).

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root 68208 ... /usr/bin/passwd
```

### SGID (Set Group ID) - 2xxx

**På fil:** Körs med gruppens rättigheter.

**På katalog:** NYA FILER ÄRVER GRUPPÄGANDET! 🔥

```bash
# Sätt SGID
chmod 2775 katalog
chmod g+s katalog

# Resultat:
drwxrwsr-x    # 's' istället för 'x' på group
```

### Sticky bit - 1xxx

**På katalog:** Endast filens ägare (eller root) kan ta bort sina egna filer.

```bash
# Sätt sticky bit
chmod 1777 katalog
chmod +t katalog

# Resultat:
drwxrwxrwt    # 't' på others
```

**Exempel:** `/tmp` har sticky bit så användare inte kan ta bort varandras filer.

```bash
ls -ld /tmp
# drwxrwxrwt 1 root root 4096 ... /tmp
```

### Sammanfattning speciella permissions

| Permission | Oktal | Symbol | På fil | På katalog |
|------------|-------|--------|--------|------------|
| SUID | 4 | s på owner | Kör som ägare | - |
| SGID | 2 | s på group | Kör som grupp | Nya filer ärver grupp |
| Sticky | 1 | t på others | - | Endast ägare kan ta bort |

### Beräkna med speciella permissions

```bash
chmod 4755 fil    # SUID + rwxr-xr-x
chmod 2775 dir    # SGID + rwxrwxr-x
chmod 1777 dir    # Sticky + rwxrwxrwx
chmod 6755 fil    # SUID + SGID + rwxr-xr-x
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Delad mapp för developers (VANLIG TENTAFRÅGA!)

```bash
#!/usr/bin/env bash

# 1. Skapa katalog
sudo mkdir -p /opt/developers

# 2. Sätt ägare och grupp
sudo chown root:developers /opt/developers

# 3. Sätt SGID + permissions
sudo chmod 2770 /opt/developers
# 2 = SGID (nya filer ärver developers-gruppen)
# 770 = rwxrwx--- (owner och group har full access)

# Verifiera
ls -ld /opt/developers
# drwxrws--- 2 root developers 4096 Dec 23 /opt/developers
#      └── 's' visar att SGID är aktivt
```

**Test:**
```bash
# Som användare alice (medlem i developers)
touch /opt/developers/test.txt
ls -l /opt/developers/test.txt
# -rw-r--r-- 1 alice developers ...
#                   └── Ärver gruppen automatiskt!
```

### Exempel 2: Projektstruktur

```bash
#!/usr/bin/env bash

PROJECT_DIR="/opt/webapp"
GROUP="webteam"

# Skapa struktur
sudo mkdir -p "$PROJECT_DIR"/{src,logs,config}

# Sätt ägande
sudo chown -R root:$GROUP "$PROJECT_DIR"

# Sätt permissions
sudo chmod 2775 "$PROJECT_DIR"          # SGID + rwxrwxr-x
sudo chmod 2775 "$PROJECT_DIR/src"
sudo chmod 2775 "$PROJECT_DIR/config"
sudo chmod 2770 "$PROJECT_DIR/logs"     # Mer restriktiv för loggar
```

### Exempel 3: Säkra SSH-kataloger

```bash
# Korrekt permissions för SSH
chmod 700 ~/.ssh                  # rwx------
chmod 600 ~/.ssh/id_ed25519       # rw------- (privat nyckel)
chmod 644 ~/.ssh/id_ed25519.pub   # rw-r--r-- (publik nyckel)
chmod 600 ~/.ssh/authorized_keys  # rw-------
chmod 644 ~/.ssh/known_hosts      # rw-r--r--
```

### Exempel 4: Skript som alla kan köra

```bash
#!/usr/bin/env bash

# Skapa gemensamt skript
cat > /usr/local/bin/deploy.sh << 'EOF'
#!/usr/bin/env bash
echo "Deploying..."
EOF

# Sätt permissions
sudo chmod 755 /usr/local/bin/deploy.sh
# Alla kan köra, endast root kan ändra

# Verifiera
ls -l /usr/local/bin/deploy.sh
# -rwxr-xr-x 1 root root ... /usr/local/bin/deploy.sh
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | chmod 755 ger? | rwxr-xr-x |
| 2 | chmod 644 ger? | rw-r--r-- |
| 3 | r+w+x i oktal? | 4+2+1 = 7 |
| 4 | SGID på katalog gör? | Nya filer ärver gruppägandet |
| 5 | chmod 2775 betyder? | SGID + rwxrwxr-x |
| 6 | Sticky bit gör? | Endast ägare kan ta bort sina filer |
| 7 | 's' på gruppen betyder? | SGID är aktivt |
| 8 | chown user:grupp fil gör? | Ändrar både ägare och grupp |
| 9 | chmod +x fil gör? | Gör filen körbar för alla |
| 10 | /tmp har vilken special permission? | Sticky bit (t) |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad betyder permission 755?**
- A) rwxrwxrwx
- B) rwxr-xr-x ✅
- C) rw-r--r--
- D) rwx------

**2. Vad gör SGID på en katalog?**
- A) Alla kan läsa katalogen
- B) Nya filer ärver katalogen gruppägande ✅
- C) Endast root kan ändra
- D) Filerna blir osynliga

**3. Hur ser du att SGID är aktivt?**
- A) 'd' i början
- B) 's' på group-positionen ✅
- C) 't' på other-positionen
- D) '+' i slutet

**4. Vad är korrekt kommando för delad katalog?**
- A) chmod 777 /shared
- B) chmod 2770 /shared ✅
- C) chmod 1755 /shared
- D) chmod 4755 /shared

**5. Vad gör sticky bit på /tmp?**
- A) Gör katalogen osynlig
- B) Endast root kan läsa
- C) Användare kan bara ta bort sina egna filer ✅
- D) Alla filer raderas automatiskt

**6. Hur beräknas rw-r--r-- i oktal?**
- A) 755
- B) 644 ✅
- C) 700
- D) 666

**7. Vad gör chmod u+s på en fil?**
- A) Sätter sticky bit
- B) Sätter SUID ✅
- C) Sätter SGID
- D) Tar bort execute

**8. Korrekt SSH-permission för ~/.ssh?**
- A) 777
- B) 755
- C) 700 ✅
- D) 644

**9. Vad betyder 't' i drwxrwxrwt?**
- A) Temporary file
- B) Sticky bit är aktivt ✅
- C) Transfer mode
- D) Trusted directory

**10. chown :developers fil ändrar?**
- A) Endast ägare
- B) Endast grupp ✅
- C) Både ägare och grupp
- D) Permissions

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Beräkna permissions
Vad blir oktalvärdet för:
```
rwxr-x--- = ?   # 750
rw-rw-r-- = ?   # 664
rwxrwxrwx = ?   # 777
```

### Övning 2: Skapa delad katalog
```bash
# 1. Skapa grupp och katalog
sudo groupadd projekt
sudo mkdir /opt/projekt

# 2. Sätt rätt ägande
sudo chown root:projekt /opt/projekt

# 3. Sätt SGID + permissions
sudo chmod 2775 /opt/projekt

# 4. Verifiera med ls -ld
ls -ld /opt/projekt
# Bör visa: drwxrwsr-x ... root projekt ...
```

### Övning 3: Identifiera speciella permissions
```bash
ls -l /usr/bin/passwd    # Hitta SUID
ls -ld /tmp              # Hitta sticky bit
# Skapa egen SGID-katalog och verifiera
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| chmod 777 | Alla kan göra allt = osäkert | Använd 755/750/644 |
| Glömma SGID | Filer får fel grupp | chmod 2775 för delade kataloger |
| Fel på ~/.ssh | SSH vägrar fungera | 700 för .ssh, 600 för nycklar |
| Rekursiv SGID | Sätter SGID på filer också | Sätt endast på kataloger |

---

## 📝 SAMMANFATTNING

```bash
# BERÄKNA PERMISSIONS
r=4, w=2, x=1
rwxr-xr-x = 755
rw-r--r-- = 644

# CHMOD
chmod 755 fil           # Oktal
chmod u+x fil           # Symbolisk
chmod -R 755 katalog    # Rekursiv

# CHOWN
chown user fil
chown user:grupp fil
chown -R user:grupp dir

# SPECIELLA PERMISSIONS
chmod 4755 fil          # SUID (kör som ägare)
chmod 2775 katalog      # SGID (ärv grupp) ← VIKTIGAST!
chmod 1777 katalog      # Sticky (endast ägare raderar)

# DELAD KATALOG (TENTA-KLASSIKER!)
sudo mkdir /opt/shared
sudo chown root:grupp /opt/shared
sudo chmod 2770 /opt/shared
# 2 = SGID, nya filer ärver gruppen automatiskt
```

"""
}

