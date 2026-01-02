# Linux Användarhantering - Praktisk Övning

## Hands-On Lab: Användare, Grupper & Behörigheter

---

## 📋 Översikt

**Typ:** Praktisk övning (individuellt eller i grupp)
**Deadline:** Ingen fast deadline
**Obligatoriskt:** Nej (men starkt rekommenderat för lärande)
**System:** Valfritt VM (Ubuntu eller Fedora)
**Inlämning:** Via Slack

---

## 🎯 Scenario

Du arbetar på IT-avdelningen på ett företag och har fått i uppdrag att sätta upp användare på en ny server. Du har fått en kravlista som du ska implementera.

---

## 📝 Kravspecifikation

### Uppgift 1: Skapa Användare

**Skapa användarkonton för följande fem personer:**

1. Alice
2. Bob
3. Charlie
4. David
5. Evert

**Krav:**

- Alla ska ha egna användarkonton
- Användarna ska kunna logga in på systemet

---

### Uppgift 2: Skapa Grupp och Medlemmar

**Skapa en grupp:**

- Gruppnamn: `developers`

**Lägg till följande användare i gruppen:**

- Alice
- Charlie
- Evert

**Resultat:**

- Bob och David är INTE med i developers-gruppen
- De är externa konsulter

---

### Uppgift 3: Skapa Projektmapp med Behörigheter

**Skapa mapp:**

- Path: `/opt/developers`

**Säkerställ:**

1. **Bara members av developers-gruppen kan komma åt mappen**
   - Bob och David ska inte kunna komma åt den

2. **Alla filer som skapas i mappen ägs automatiskt av gruppen `developers`**
   - INTE av användarens primära grupp
   - Alla i gruppen kan komma åt alla filer by default

**Tips:**

- Detta löses med special permissions (SGID)
- Tänk på både directory permissions och group ownership

---

### Uppgift 4: Sätt Utgångsdatum för Konsulter

**Problem:**

- Bob och David är externa konsulter
- Deras uppdrag går ut vid årsskiftet

**Krav:**

- Deras konton ska sluta fungera från och med **1 januari 2026**
- Efter detta datum ska de inte kunna logga in

**Tips:**

- Läs `man usermod`
- Leta efter flaggor relaterade till expiration/expire

---

### Uppgift 5: Tvinga Lösenordsbyte

**Problem:**

- Någon har lånat Everts tangentbord
- De hittade en post-it med hans lösenord under tangentbordet
- Detta bryter mot företagets säkerhetspolicy
- Lösenordet betraktas som läckt

**Krav:**

- Tvinga Evert att byta lösenord vid nästa login
- Han ska inte kunna använda det gamla lösenordet

**Tips:**

- Läs `man passwd`
- Leta efter flaggor för password expiration/aging

---

## 📤 Inlämning

### Format

**Skicka via Slack:**

En lista med kommandon som löser varje uppgift:

```
Uppgift 1: Skapa användare
- sudo useradd alice
- sudo useradd bob
... etc

Uppgift 2: Skapa grupp och medlemmar
- sudo groupadd developers
... etc

Uppgift 3: Projektmapp och behörigheter
... etc

Uppgift 4: Utgångsdatum för konsulter
... etc

Uppgift 5: Tvinga lösenordsbyte
... etc
```

### Grupparbete

**Om ni jobbar i grupp:**

- En person skickar lösningen
- Ange **alla gruppmedlemmar** i meddelandet
- Exempel: "Löst av: Alice, Bob och Charlie"

**Viktigt:**

- Även om ni får hjälp, **förstå varje kommando**
- Kopiera inte bara - lär dig vad varje del gör
- Alla i gruppen ska kunna förklara lösningen

### Vad Ni INTE Behöver

- ❌ Inget skript krävs (men är ett plus!)
- ❌ Behöver inte köra alla kommandon i en fil
- ❌ Ingen automatisering nödvändig

**Ni kan:**

- ✅ Köra kommandon direkt i terminalen
- ✅ Anteckna kommandon vid sidan om
- ✅ Skicka kommandon som text
- ✅ (Bonus) Skapa ett skript som löser allt

---

## 🔍 Lösningsguide & Tips

### Användbara Kommandon

**Användarhantering:**

```bash
useradd          # Skapa användare
usermod          # Modifiera användare
passwd           # Hantera lösenord
userdel          # Ta bort användare
```

**Grupphantering:**

```bash
groupadd         # Skapa grupp
groupmod         # Modifiera grupp
usermod -aG      # Lägg användare till grupp
gpasswd          # Gruppåtkomst
```

**Behörigheter:**

```bash
chmod            # Ändra permissions
chown            # Ändra ägare
chgrp            # Ändra grupp
```

**Verifiering:**

```bash
id username      # Visa användarinfo
groups username  # Visa grupptillhörighet
ls -l            # Visa permissions
getent passwd    # Lista användare
getent group     # Lista grupper
```

### Viktiga Man Pages

```bash
man useradd      # Skapa användare
man usermod      # Modifiera användare (Uppgift 4!)
man passwd       # Lösenordshantering (Uppgift 5!)
man groupadd     # Skapa grupper
man chmod        # Permissions
man chown        # Ownership
```

### Special Permissions

**SGID (Set Group ID):**

- Används för Uppgift 3
- Gör att filer skapade i mappen ärver gruppägande
- Sätts med `chmod g+s` eller `chmod 2xxx`

**Exempel:**

```bash
chmod g+s /opt/developers        # Sätt SGID
chmod 2770 /opt/developers       # SGID + full access för grupp
```

### Tänk På

**Uppgift 1: Skapa användare**

- Använd `useradd` eller `adduser`
- Kanske vill ni sätta lösenord med `passwd`

**Uppgift 2: Grupper**

- Skapa gruppen först
- Lägg till användare med `usermod -aG`
- Verifiera med `groups username`

**Uppgift 3: Mapp och behörigheter**

- Skapa mappen: `mkdir /opt/developers`
- Sätt gruppägande: `chgrp developers /opt/developers`
- Sätt SGID: `chmod g+s /opt/developers`
- Sätt permissions: `chmod 770 /opt/developers`
  - 7 (owner): rwx
  - 7 (group): rwx
  - 0 (other): ---

**Uppgift 4: Expiration date**

- `usermod` har en flagga för expire date
- Datumet ska vara 2026-01-01
- Format: YYYY-MM-DD

**Uppgift 5: Force password change**

- `passwd` kan sätta password expiration
- Leta efter "expire" i man page
- Användaren tvingas byta vid nästa login

---

## ✅ Verifieringschecklist

### Uppgift 1: Användare skapade?

```bash
getent passwd alice
getent passwd bob
getent passwd charlie
getent passwd david
getent passwd evert
# Alla ska finnas i listan
```

### Uppgift 2: Grupp och medlemmar?

```bash
getent group developers
# Output ska visa: developers:x:1001:alice,charlie,evert

groups alice    # Ska inkludera developers
groups charlie  # Ska inkludera developers
groups evert    # Ska inkludera developers
groups bob      # Ska INTE inkludera developers
groups david    # Ska INTE inkludera developers
```

### Uppgift 3: Mapp och behörigheter?

```bash
ls -ld /opt/developers
# Output ska visa:
# drwxrws--- ... developers /opt/developers
#      ^
#      SGID-bit (s istället för x)

# Testa skapa fil som alice
sudo -u alice touch /opt/developers/test.txt
ls -l /opt/developers/test.txt
# Filen ska ägas av gruppen developers

# Testa åtkomst som bob (ska INTE fungera)
sudo -u bob ls /opt/developers
# Ska ge "Permission denied"
```

### Uppgift 4: Expiration date?

```bash
sudo chage -l bob
# Account expires: Jan 01, 2026

sudo chage -l david
# Account expires: Jan 01, 2026
```

### Uppgift 5: Password expire?

```bash
sudo chage -l evert
# Last password change: ... (ska visa att lösenord har expired)

# Eller prova logga in som evert
sudo -u evert bash
# Ska fråga om nytt lösenord
```

---

## 🎓 Lärandemål

Efter att ha genomfört denna övning ska du kunna:

1. ✅ Skapa och hantera användarkonton
2. ✅ Skapa och hantera grupper
3. ✅ Lägga till användare i grupper
4. ✅ Sätta och förstå file permissions
5. ✅ Använda special permissions (SGID)
6. ✅ Sätta utgångsdatum för användarkonton
7. ✅ Tvinga lösenordsbyte
8. ✅ Verifiera konfiguration
9. ✅ Läsa och förstå man pages

---

## 🚀 Steg-för-Steg Process

### Rekommenderad Arbetsordning

1. **Läs igenom hela uppgiften först**
   - Förstå vad som krävs
   - Identifiera vilka kommandon du behöver

2. **Börja med att läsa relevanta man pages**

   ```bash
   man useradd
   man usermod
   man groupadd
   man chmod
   man passwd
   ```

3. **Kolla inspelningen igen vid behov**
   - Om något är oklart
   - För att se praktiska exempel

4. **Jobba genom uppgifterna i ordning**
   - En uppgift i taget
   - Verifiera innan du går vidare

5. **Testa varje steg**
   - Använd verifieringskommandona
   - Se till att allt fungerar som det ska

6. **Dokumentera dina kommandon**
   - Anteckna vad du kör
   - Kommentera varför

7. **Skicka in när du är klar**
   - Via Slack
   - Inkludera alla gruppmedlemmar om tillämpligt

---

## 💡 Vanliga Fallgropar

### ❌ Fel 1: Glömmer sudo

```bash
useradd alice           # ❌ Permission denied
sudo useradd alice      # ✅ Fungerar
```

### ❌ Fel 2: Skriver över grupper

```bash
usermod -G developers alice    # ❌ Tar bort från andra grupper
usermod -aG developers alice   # ✅ Lägger till i grupp
```

### ❌ Fel 3: Glömmer SGID

```bash
chmod 770 /opt/developers      # ❌ Filer ärver inte grupp
chmod 2770 /opt/developers     # ✅ SGID satt, filer ärver grupp
# Eller
chmod g+s /opt/developers      # ✅ Sätt SGID explicit
```

### ❌ Fel 4: Fel datumformat

```bash
usermod --expiredate 01-01-2026 bob    # ❌ Fel format
usermod --expiredate 2026-01-01 bob    # ✅ YYYY-MM-DD
```

### ❌ Fel 5: Fel permission kommando för lösenord

```bash
passwd --expire evert           # ✅ Rätt kommando
chage -E 0 evert               # ✅ Alternativ metod
usermod --expire evert         # ❌ Fel kommando för lösenord
```

---

## 📚 Referensmaterial

### Viktiga Koncept från Föreläsningen

**Användare:**

- Varje person har eget konto
- Hanteras med `useradd`, `usermod`, `userdel`
- Lösenord hanteras med `passwd`

**Grupper:**

- Samlingar av användare
- Underlättar behörighetshantering
- Varje användare har en primär grupp
- Kan vara medlem i flera grupper

**Permissions:**

- Read (r), Write (w), Execute (x)
- För Owner, Group, Others
- Representeras som tre siffror (ex: 770)

**Special Permissions:**

- SGID (2000): Filer ärver gruppägande
- SUID (4000): Körs som filägare
- Sticky bit (1000): Bara ägare kan radera

**Account Expiration:**

- Användarkonton kan sättas att sluta fungera vid visst datum
- Hanteras med `usermod` eller `chage`

**Password Expiration:**

- Tvinga användare att byta lösenord
- Hanteras med `passwd` eller `chage`

---

## 🔧 Exempelkommandon (utan lösning)

**Dessa är exempel på kommandostruktur, inte kompletta lösningar:**

```bash
# Skapa användare (exempel struktur)
sudo useradd [options] username

# Lägg till i grupp (exempel struktur)
sudo usermod -aG groupname username

# Skapa mapp (exempel struktur)
sudo mkdir /path/to/directory

# Sätt permissions (exempel struktur)
sudo chmod [permissions] /path/to/directory

# Sätt gruppägande (exempel struktur)
sudo chgrp groupname /path/to/directory

# Sätt utgångsdatum (exempel struktur)
sudo usermod --expiredate YYYY-MM-DD username

# Tvinga lösenordsbyte (exempel struktur)
sudo passwd [option] username
```

---

## 🎯 Sammanfattning

**Uppgift:** Konfigurera användarhantering på en server

**Krav:**

1. ✅ 5 användare (Alice, Bob, Charlie, David, Evert)
2. ✅ 1 grupp (developers) med 3 medlemmar (Alice, Charlie, Evert)
3. ✅ 1 mapp (/opt/developers) med:
   - Endast developers-gruppen har åtkomst
   - SGID så filer ärver gruppägande
4. ✅ 2 konsulter (Bob, David) med utgångsdatum 2026-01-01
5. ✅ 1 användare (Evert) som måste byta lösenord vid nästa login

**Verktyg:**

- `useradd`, `usermod`, `passwd`
- `groupadd`, `gpasswd`
- `chmod`, `chown`, `chgrp`
- Man pages som guider

**Inlämning:**

- Slack
- Lista med kommandon per uppgift
- Ange gruppmedlemmar om tillämpligt

**Mål:**

- Praktisera allt från dagens föreläsning
- Förstå användarhantering i verkliga scenarion
- Kunna sätta upp och hantera användare professionellt

---

## 🆘 Om Du Fastnar

1. **Läs man pages**

   ```bash
   man useradd
   man usermod
   man passwd
   man chmod
   ```

2. **Kolla inspelningen igen**
   - Går igenom varje koncept praktiskt
   - Visar exempel

3. **Använd verifieringskommandon**

   ```bash
   id username
   groups username
   ls -l directory
   ```

4. **Fråga på handledning**
   - Torsdagar finns handledning
   - Ingen fråga är för enkel

5. **Jobba med klasskompis**
   - Diskutera lösningar
   - Förklara för varandra
   - Men se till att båda förstår

---

**Lycka till med övningen! 🚀**

*En praktisk övning i Linux-systemadministration*
