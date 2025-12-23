"""
NOD 2.1: Users & Groups
=======================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 2: LINUX SYSTEM
"""

USERS_GROUPS_NODE = {
    "title": "Users & Groups",
    "slug": "users-groups",
    "description": "Användarhantering, grupper, lösenordspolicies och systemfiler.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "order_index": 1,
    "content": r"""# Users & Groups

> **TL;DR:** `useradd -m -s /bin/bash user` skapar användare. `usermod -aG grupp user` lägger till i grupp (glöm inte -a!). `passwd user` sätter lösenord.

---

## 📖 TEORI: Viktiga systemfiler

### /etc/passwd - Användarinformation

```
username:x:UID:GID:kommentar:hemkatalog:shell
said:x:1000:1000:Said User:/home/said:/bin/bash
```

| Fält | Betydelse | Exempel |
|------|-----------|---------|
| username | Användarnamn | said |
| x | Lösenord (i /etc/shadow) | x |
| UID | User ID | 1000 |
| GID | Primary Group ID | 1000 |
| kommentar | Fullständigt namn/info | Said User |
| hemkatalog | Home directory | /home/said |
| shell | Login shell | /bin/bash |

### /etc/shadow - Lösenord & policies

```
username:krypterat_lösenord:senast_ändrat:min:max:warn:inactive:expire
said:$6$xyz...:19500:0:99999:7:::
```

| Fält | Betydelse |
|------|-----------|
| krypterat_lösenord | Hash av lösenord |
| senast_ändrat | Dagar sedan 1970-01-01 |
| min | Min dagar mellan byten |
| max | Max dagar innan byte krävs |
| warn | Dagar före varning |
| inactive | Dagar efter expire innan lås |
| expire | Kontots utgångsdatum |

### /etc/group - Gruppinformation

```
gruppnamn:x:GID:medlemmar
developers:x:1001:alice,bob,charlie
```

### /etc/skel - Mall för hemkataloger

Filer som kopieras till nya användares hemkataloger:
- .bashrc
- .profile
- .bash_logout

---

## 📖 Skapa användare

### useradd - Grundläggande

```bash
# Minimal (ingen hemkatalog!)
sudo useradd username

# Med hemkatalog (-m)
sudo useradd -m username

# Med hemkatalog och shell
sudo useradd -m -s /bin/bash username

# Med kommentar
sudo useradd -m -s /bin/bash -c "Alice Admin" alice

# Med specifikt UID
sudo useradd -m -u 1500 username

# Med primärgrupp
sudo useradd -m -g developers username

# Med extra grupper
sudo useradd -m -G sudo,docker username
```

### adduser - Interaktiv (Debian/Ubuntu)

```bash
sudo adduser username
# Frågar efter lösenord, namn, etc.
```

### Skapa flera användare med loop

```bash
#!/usr/bin/env bash
for user in Alice Bob Charlie David Evert; do
    sudo useradd -m -s /bin/bash "$user"
    echo "Skapade användare: $user"
done
```

---

## 📖 Ta bort användare

```bash
# Behåll hemkatalog
sudo userdel username

# Ta bort hemkatalog också (-r)
sudo userdel -r username
```

---

## 📖 Modifiera användare (usermod)

### ⚠️ KRITISKT: -a flaggan!

```bash
# FEL - ERSÄTTER alla grupper!
sudo usermod -G developers alice  # ❌ Alice förlorar alla andra grupper!

# RÄTT - LÄGGER TILL i grupp
sudo usermod -aG developers alice  # ✅ -a = append
```

### Alla viktiga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-aG` | Lägg till i grupp | `usermod -aG sudo alice` |
| `-s` | Byt shell | `usermod -s /bin/zsh alice` |
| `-d` | Byt hemkatalog | `usermod -d /home/new alice` |
| `-l` | Byt användarnamn | `usermod -l newname oldname` |
| `-L` | Lås konto | `usermod -L alice` |
| `-U` | Lås upp konto | `usermod -U alice` |
| `-e` | Sätt utgångsdatum | `usermod -e 2025-12-31 alice` |

### Praktiskt: Lägg till användare i grupp

```bash
# Skapa grupp
sudo groupadd developers

# Lägg till användare (en i taget)
sudo usermod -aG developers alice
sudo usermod -aG developers bob

# Med loop
for user in Alice Charlie Evert; do
    sudo usermod -aG developers "$user"
done
```

### Sätt utgångsdatum

```bash
# Sätt utgångsdatum för flera användare
for user in Bob David; do
    sudo usermod --expiredate 2025-12-31 "$user"
done
```

---

## 📖 Grupper

### Skapa och ta bort

```bash
# Skapa grupp
sudo groupadd developers
sudo groupadd -g 2000 custom_group  # Med specifikt GID

# Ta bort grupp
sudo groupdel developers
```

### Visa grupptillhörighet

```bash
# Visa användarens grupper
groups alice
# Output: alice : alice developers sudo

# Detaljerad info
id alice
# Output: uid=1001(alice) gid=1001(alice) groups=1001(alice),1002(developers),27(sudo)
```

---

## 📖 Lösenord (passwd & chage)

### passwd - Sätt/byt lösenord

```bash
# Sätt lösenord för användare
sudo passwd alice

# Tvinga byte vid nästa inloggning
sudo passwd --expire alice

# Lås konto
sudo passwd -l alice

# Lås upp
sudo passwd -u alice
```

### chage - Lösenordspolicy

```bash
# Visa lösenordspolicy
sudo chage -l alice

# Output:
# Last password change                : Dec 23, 2025
# Password expires                    : never
# Account expires                     : Dec 31, 2025
# Minimum number of days between password change : 0
# Maximum number of days between password change : 99999
# Number of days of warning before password expires : 7
```

```bash
# Sätt utgångsdatum för KONTO
sudo chage -E 2025-12-31 alice

# Sätt max dagar för lösenord
sudo chage -M 90 alice

# Tvinga lösenordsbyte vid nästa inloggning
sudo chage -d 0 alice
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Komplett användarsetup

```bash
#!/usr/bin/env bash
set -euo pipefail

# Skapa developers-grupp
sudo groupadd -f developers

# Skapa användare
for user in Alice Bob Charlie; do
    if ! id "$user" &>/dev/null; then
        sudo useradd -m -s /bin/bash -c "$user Developer" "$user"
        echo "Skapade: $user"
    else
        echo "Finns redan: $user"
    fi

    # Lägg till i grupp
    sudo usermod -aG developers "$user"
done

# Sätt tillfälliga lösenord
for user in Alice Bob Charlie; do
    echo "$user:TempPass123" | sudo chpasswd
    sudo passwd --expire "$user"
done

echo "Klart! Användare måste byta lösenord vid första inloggning."
```

### Exempel 2: Kontraktanställda med utgångsdatum

```bash
#!/usr/bin/env bash

# Kontraktanställda som slutar 2025-12-31
contractors=(Bob David)

for user in "${contractors[@]}"; do
    sudo usermod --expiredate 2025-12-31 "$user"
    echo "Satte utgångsdatum för $user"
done

# Verifiera
for user in "${contractors[@]}"; do
    echo "=== $user ==="
    sudo chage -l "$user" | grep "Account expires"
done
```

### Exempel 3: Cleanup - Ta bort användare

```bash
#!/usr/bin/env bash

users_to_remove=(TestUser1 TestUser2)

for user in "${users_to_remove[@]}"; do
    if id "$user" &>/dev/null; then
        sudo userdel -r "$user"
        echo "Borttagen: $user"
    else
        echo "Finns inte: $user"
    fi
done
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | useradd -m gör? | Skapar användare MED hemkatalog |
| 2 | usermod -aG grupp user gör? | Lägger TILL användare i grupp |
| 3 | Varför -a i usermod -aG? | Append! Utan -a ersätts alla grupper |
| 4 | passwd --expire user gör? | Tvingar lösenordsbyte vid nästa inloggning |
| 5 | /etc/passwd innehåller? | Användarinfo (UID, GID, shell, hemkatalog) |
| 6 | /etc/shadow innehåller? | Krypterade lösenord och policies |
| 7 | userdel -r gör? | Tar bort användare OCH hemkatalog |
| 8 | groups username visar? | Användarens grupptillhörigheter |
| 9 | chage -l user visar? | Lösenordspolicy och utgångsdatum |
| 10 | /etc/skel är? | Mall för nya hemkataloger |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilket kommando skapar användare MED hemkatalog?**
- A) useradd username
- B) useradd -m username ✅
- C) adduser -m username
- D) newuser username

**2. Vad händer om du kör `usermod -G sudo alice` (utan -a)?**
- A) Alice läggs till i sudo-gruppen
- B) Alice ersätts i alla grupper med ENDAST sudo ✅
- C) Kommandot misslyckas
- D) Inget händer

**3. Var lagras krypterade lösenord?**
- A) /etc/passwd
- B) /etc/shadow ✅
- C) /etc/group
- D) /etc/security

**4. Hur tvingar du en användare att byta lösenord vid nästa inloggning?**
- A) passwd -f username
- B) passwd --expire username ✅
- C) passwd --force username
- D) usermod --expire username

**5. Vad visar kommandot `id alice`?**
- A) Endast UID
- B) Endast GID
- C) UID, GID och alla grupptillhörigheter ✅
- D) Bara gruppnamn

**6. Hur tar du bort en användare OCH dess hemkatalog?**
- A) userdel username
- B) userdel -r username ✅
- C) deluser --remove username
- D) rmuser -h username

**7. Vad är /etc/skel?**
- A) Katalog med systemloggar
- B) Mall för nya hemkataloger ✅
- C) Lista över inaktiva konton
- D) Backup av användarkonton

**8. Vilket kommando visar lösenordspolicy för en användare?**
- A) passwd -l username
- B) chage -l username ✅
- C) shadow -l username
- D) policy username

**9. Hur sätter du utgångsdatum 2025-12-31 för ett konto?**
- A) usermod -e 2025-12-31 user ✅
- B) passwd -e 2025-12-31 user
- C) expire 2025-12-31 user
- D) chage -e 2025-12-31 user

**10. Vad betyder fältet 'x' i /etc/passwd?**
- A) Kontot är låst
- B) Lösenordet finns i /etc/shadow ✅
- C) Ingen hemkatalog
- D) Kontot är inaktivt

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Skapa användarstruktur
```bash
# 1. Skapa gruppen "webteam"
sudo groupadd webteam

# 2. Skapa användare Anna, Erik, Lisa med bash som shell
for user in Anna Erik Lisa; do
    sudo useradd -m -s /bin/bash "$user"
done

# 3. Lägg till alla i webteam
for user in Anna Erik Lisa; do
    sudo usermod -aG webteam "$user"
done

# 4. Verifiera
groups Anna Erik Lisa
```

### Övning 2: Kontraktanställd
```bash
# Skapa användare som slutar 2025-06-30
sudo useradd -m -s /bin/bash contractor
sudo usermod -e 2025-06-30 contractor
sudo chage -l contractor | grep "Account expires"
```

### Övning 3: Säkerhetsrutiner
```bash
# 1. Sätt tillfälligt lösenord
sudo passwd testuser

# 2. Tvinga byte vid nästa inloggning
sudo passwd --expire testuser

# 3. Verifiera
sudo chage -l testuser
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `usermod -G` utan `-a` | Alla andra grupper försvinner | ALLTID `usermod -aG` |
| `useradd` utan `-m` | Ingen hemkatalog skapas | Använd `-m` flaggan |
| Glömma sätta lösenord | Kontot kan inte logga in | `passwd username` efteråt |
| Glömma shell | Användare får /bin/sh | Ange `-s /bin/bash` |

---

## 📝 SAMMANFATTNING

```bash
# SKAPA ANVÄNDARE
sudo useradd -m -s /bin/bash username
sudo useradd -m -s /bin/bash -c "Full Name" username

# GRUPPER
sudo groupadd gruppnamn
sudo usermod -aG grupp username    # ⚠️ -a är KRITISKT!
groups username
id username

# LÖSENORD
sudo passwd username
sudo passwd --expire username      # Tvinga byte
sudo chage -l username             # Visa policy
sudo chage -E YYYY-MM-DD username  # Utgångsdatum

# MODIFIERA
sudo usermod -s /bin/zsh username  # Byt shell
sudo usermod -L username           # Lås
sudo usermod -U username           # Lås upp
sudo usermod -e YYYY-MM-DD username # Utgångsdatum

# TA BORT
sudo userdel username              # Behåll hem
sudo userdel -r username           # Ta bort allt
```

"""
}

