"""
Linux Tenta VG-Guide — 10 noder för komplett tentaförberedelse
Baserad på Said's studiehandbok | Tenta 7 januari 2025
"""

MODULE = {
    "id": "doe25-tentaplugg",
    "slug": "doe25-tentaplugg",
    "title": "Linux Tenta VG-Guide",
    "description": "Komplett tentaförberedelse för Linux - 10 moduler från subnetting till Docker Compose. Baserad på Said's VG-guide.",
    "icon": "🎯",
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "order_index": 2,
    "tasks": [
        # =============================================================================
        # NOD 1: Subnetting & Nätverk
        # =============================================================================
        {
            "title": "Subnetting & Nätverk",
            "slug": "subnetting-natverk",
            "description": "Binärmetoden (lådmetoden) för att räkna ut subnät, Network ID, Broadcast och hosts.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "order_index": 1,
            "content": r"""# Subnetting & Nätverk

## Varför viktigt för tentan?

Subnetting är ett av de vanligaste ämnena på tentan. Du MÅSTE kunna räkna ut:
- Network ID
- Broadcast-adress
- First/Last Host
- Antal hosts i ett subnät

---

## Binärmetoden (Lådmetoden)

### De 8 binära lådorna (en oktett)

```
128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
```

Varje position representerar en potens av 2. Tillsammans blir det 255 (maxvärde för en oktett).

---

## Steg-för-steg: Räkna ut subnät

### Exempel: 46.84.126.147/28

**Steg 1: Beräkna host-lådor**

```bash
32 - prefix = antal host-lådor
32 - 28 = 4 host-lådor
```

**Steg 2: Markera N (nät) och H (host)**

```
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
   N    N    N    N  | H   H   H   H
```

De första 4 lådorna = Nät (N)
De sista 4 lådorna = Host (H)

**Steg 3: Konvertera 147 till binärt**

```bash
147 = 128 + 16 + 2 + 1
    = 1 0 0 1 | 0 0 1 1
```

**Steg 4: Beräkna Network ID**

Behåll N-lådorna, sätt H-lådorna till 0:

```bash
1 0 0 1 | 0 0 0 0 = 128 + 16 = 144
```

**Network ID = 46.84.126.144**

**Steg 5: Beräkna Broadcast**

Behåll N-lådorna, sätt H-lådorna till 1:

```bash
1 0 0 1 | 1 1 1 1 = 128 + 16 + 8 + 4 + 2 + 1 = 159
```

**Broadcast = 46.84.126.159**

**Steg 6: First Host, Last Host, Next Subnet**

```bash
First Host  = Network + 1     = 144 + 1 = 145
Last Host   = Broadcast - 1   = 159 - 1 = 158
Next Subnet = Broadcast + 1   = 159 + 1 = 160
```

---

## Sammanfattning för 46.84.126.147/28

| Egenskap | Värde |
|----------|-------|
| Network | 46.84.126.144 |
| First Host | 46.84.126.145 |
| Last Host | 46.84.126.158 |
| Broadcast | 46.84.126.159 |
| Next Subnet | 46.84.126.160 |

---

## Vanliga prefix och antal hosts

| Prefix | Adresser | Hosts | Användning |
|--------|----------|-------|------------|
| /24 | 256 | 254 | Klass C - standard |
| /25 | 128 | 126 | Halvt C-nät |
| /26 | 64 | 62 | Kvarts C-nät |
| /27 | 32 | 30 | Litet nätverk |
| /28 | 16 | 14 | Mycket litet |
| /29 | 8 | 6 | Litet segment |
| /30 | 4 | 2 | Punkt-till-punkt |

---

## Formel: Antal hosts

```bash
Antal hosts = 2^(32-prefix) - 2
```

Exempel /28:
```bash
2^(32-28) - 2 = 2^4 - 2 = 16 - 2 = 14 hosts
```

---

## Övning: Räkna själv

**192.168.1.67/26**

```bash
1. Host-lådor: 32 - 26 = 6
2. Markering: NN | HHHHHH
3. 67 i binärt: 01000011
4. Network: 01000000 = 64
5. Broadcast: 01111111 = 127
6. First: 65, Last: 126, Next: 128
```

---

## Snabbreferens

| Uppgift | Metod |
|---------|-------|
| Host-bitar | 32 - prefix |
| Network ID | Nolla alla host-bitar |
| Broadcast | Ettställ alla host-bitar |
| First host | Network + 1 |
| Last host | Broadcast - 1 |
| Antal hosts | 2^host-bitar - 2 |

""",
            "quiz": [
                {
                    "question": "Vad är Network ID för 192.168.1.100/26?",
                    "options": [
                        "192.168.1.0",
                        "192.168.1.64",
                        "192.168.1.96",
                        "192.168.1.128",
                    ],
                    "correct": 1,
                    "explanation": "Med /26 har vi 6 host-bitar. 100 i binärt är 01100100. Nollställ de 6 sista bitarna: 01000000 = 64.",
                },
                {
                    "question": "Hur många hosts ryms i ett /28-nätverk?",
                    "options": ["16", "14", "30", "62"],
                    "correct": 1,
                    "explanation": "2^(32-28) - 2 = 2^4 - 2 = 16 - 2 = 14 hosts.",
                },
                {
                    "question": "Vad är Broadcast-adressen för 10.0.0.50/29?",
                    "options": ["10.0.0.55", "10.0.0.63", "10.0.0.48", "10.0.0.56"],
                    "correct": 0,
                    "explanation": "/29 ger 3 host-bitar. Network är 10.0.0.48, Broadcast är 10.0.0.55 (alla host-bitar = 1).",
                },
            ],
        },
        # =============================================================================
        # NOD 2: Filsystem & Grundkommandon
        # =============================================================================
        {
            "title": "Filsystem & Grundkommandon",
            "slug": "filsystem-grundkommandon",
            "description": "Linux filsystemstruktur, navigering, filhantering och sökning.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "order_index": 2,
            "content": r"""# Filsystem & Grundkommandon

## Linux Filsystemstruktur

```bash
/           # Rot - allt börjar här
/etc        # Konfigurationsfiler (passwd, shadow, ssh)
/home       # Användarnas hemmakataloger
/var        # Variabel data (loggar, cache, spool)
/opt        # Tredjepartsprogram
/tmp        # Temporära filer (rensas vid omstart)
/bin        # Grundläggande binärer (ls, cp, mv)
/sbin       # Systemadministration (fdisk, iptables)
/usr        # Användarprogram och bibliotek
/dev        # Enheter (hårddiskar, terminaler)
/proc       # Processinformation (virtuellt)
/root       # Root-användarens hemma
```

---

## Navigering

```bash
pwd                     # Print Working Directory
cd /path/to/dir         # Change Directory
cd ..                   # Upp en nivå
cd ~                    # Till hemma
cd -                    # Till förra katalogen (smart!)

ls                      # Lista filer
ls -l                   # Long format (permissions, ägare, storlek)
ls -a                   # Visa dolda filer (börjar med .)
ls -la                  # Kombinera
ls -lh                  # Human readable storlek
ls -lt                  # Sortera efter tid
ls -lS                  # Sortera efter storlek
```

---

## Fil- och kataloghantering

### Skapa

```bash
mkdir katalog           # Skapa katalog
mkdir -p a/b/c          # Skapa med föräldrar
touch fil.txt           # Skapa tom fil / uppdatera tidsstämpel
```

### Kopiera

```bash
cp fil.txt kopia.txt    # Kopiera fil
cp -r katalog/ backup/  # Kopiera rekursivt (VIKTIGT!)
cp -p fil.txt backup/   # Behåll permissions
```

### Flytta/Byt namn

```bash
mv gammal.txt ny.txt    # Byt namn
mv fil.txt /path/to/    # Flytta
```

### Ta bort

```bash
rm fil.txt              # Ta bort fil
rm -r katalog/          # Ta bort katalog rekursivt
rm -rf katalog/         # Force, ingen fråga (FARLIGT!)
rmdir tom_katalog       # Ta bort tom katalog
```

---

## Sökning

### find - sök filer

```bash
find /path -name "*.txt"              # Efter namn
find /path -type f                    # Endast filer
find /path -type d                    # Endast kataloger
find /path -size +100M                # Större än 100MB
find /path -mtime -7                  # Ändrade senaste 7 dagar
find /path -user root                 # Ägs av root
find /path -perm 755                  # Med permissions 755
find /path -name "*.log" -delete      # Hitta och ta bort
find /path -exec ls -l {} \;          # Kör kommando på resultat
```

### grep - sök i filer

```bash
grep "sökord" fil.txt                 # Sök i fil
grep -r "sökord" /path/               # Rekursivt i katalog
grep -i "sökord" fil.txt              # Case insensitive
grep -n "sökord" fil.txt              # Visa radnummer
grep -v "sökord" fil.txt              # Invertera (visa EJ matchande)
grep -c "sökord" fil.txt              # Räkna matchningar
grep -E "regex" fil.txt               # Extended regex (egrep)
```

---

## Visa filinnehåll

```bash
cat fil.txt             # Visa hela filen
head fil.txt            # Första 10 rader
head -n 20 fil.txt      # Första 20 rader
tail fil.txt            # Sista 10 rader
tail -n 20 fil.txt      # Sista 20 rader
tail -f fil.txt         # Följ filen i realtid (loggar!)
less fil.txt            # Bläddra (q för quit, / för sök)
```

---

## Pipes och Redirection

### Pipes - skicka output till nästa kommando

```bash
ls -l | grep ".txt"     # Lista, filtrera på .txt
cat fil | sort | uniq   # Visa, sortera, ta bort dubletter
ps aux | grep nginx     # Hitta nginx-processer
```

### Redirection

```bash
echo "text" > fil.txt   # Skriv till fil (skriver över!)
echo "text" >> fil.txt  # Lägg till i fil
kommando 2> error.log   # Stderr till fil
kommando &> all.log     # Både stdout och stderr
kommando 2>&1           # Stderr till stdout
kommando > /dev/null    # Kasta output
kommando 2>/dev/null    # Kasta errors
```

---

## Arkivering med tar

```bash
# Skapa arkiv
tar -cvf arkiv.tar katalog/           # Create, Verbose, File
tar -czvf arkiv.tar.gz katalog/       # Med gzip-komprimering
tar -cjvf arkiv.tar.bz2 katalog/      # Med bzip2-komprimering

# Extrahera
tar -xvf arkiv.tar                    # Extract
tar -xzvf arkiv.tar.gz                # Extrahera gzip
tar -xzvf arkiv.tar.gz -C /path/      # Till specifik katalog

# Visa innehåll
tar -tzvf arkiv.tar.gz                # Lista innehåll
```

**Viktiga flaggor:** c=create, x=extract, t=list, v=verbose, f=file, z=gzip, p=preserve

---

## Diskutrymme

```bash
df -h                   # Disk Free - visa partitioner
du -sh katalog/         # Disk Usage - katalogstorlek
du -sh *                # Storlek på allt i nuvarande katalog
du -h --max-depth=1     # En nivå djupt
```

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Var är jag? | `pwd` |
| Lista allt | `ls -lah` |
| Kopiera mapp | `cp -r källa/ mål/` |
| Ta bort mapp | `rm -rf katalog/` |
| Hitta filer | `find /path -name "*.txt"` |
| Sök i filer | `grep -r "text" /path/` |
| Följ logg | `tail -f /var/log/syslog` |
| Kolla disk | `df -h` |

""",
            "quiz": [
                {
                    "question": "Vilket kommando kopierar en katalog rekursivt?",
                    "options": [
                        "cp katalog/ backup/",
                        "cp -r katalog/ backup/",
                        "mv katalog/ backup/",
                        "copy -r katalog/ backup/",
                    ],
                    "correct": 1,
                    "explanation": "cp -r (recursive) krävs för att kopiera kataloger med innehåll.",
                },
                {
                    "question": "Vad gör kommandot 'tail -f /var/log/syslog'?",
                    "options": [
                        "Visar första 10 raderna",
                        "Visar sista 10 raderna",
                        "Följer filen i realtid",
                        "Filtrerar loggen",
                    ],
                    "correct": 2,
                    "explanation": "tail -f (follow) visar nya rader i realtid - perfekt för att övervaka loggar.",
                },
                {
                    "question": "Vad betyder 'grep -v' flaggan?",
                    "options": [
                        "Verbose output",
                        "Visa radnummer",
                        "Invertera matchning",
                        "Case insensitive",
                    ],
                    "correct": 2,
                    "explanation": "grep -v inverterar matchningen och visar rader som INTE matchar mönstret.",
                },
            ],
        },
        # =============================================================================
        # NOD 3: Bash Scripting Grund
        # =============================================================================
        {
            "title": "Bash Scripting Grund",
            "slug": "bash-scripting-grund",
            "description": "Shebang, variabler, specialvariabler, if-satser och test-operatorer.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 120,
            "order_index": 3,
            "content": r"""# Bash Scripting Grund

## Script-grunder

```bash
#!/bin/bash
# Shebang - måste vara första raden!

# Gör körbar
chmod +x script.sh

# Köra
./script.sh
bash script.sh
```

---

## Variabler

**VIKTIGT: INGET mellanslag runt =**

```bash
# Tilldela (RÄTT)
name="Said"
age=25
path="/home/said"

# FEL - ger error!
name = "Said"

# Använda
echo $name
echo ${name}            # Rekommenderat, tydligare
echo "Hej $name!"
echo "Path är: ${path}/scripts"
```

---

## Specialvariabler

```bash
$0          # Scriptets namn
$1          # Första argumentet
$2          # Andra argumentet
$#          # Antal argument
$@          # Alla argument (som lista)
$*          # Alla argument (som sträng)
$?          # Exit status från förra kommandot
$$          # Processens PID
```

---

## Command Substitution

```bash
# Kör kommando och spara output
today=$(date +%Y-%m-%d)
files=$(ls *.txt)
user=$(whoami)

echo "Datum: $today"
```

---

## Exit Status

```bash
# 0 = lyckat, annat = fel
ls /existing_dir
echo $?                 # 0

ls /nonexistent
echo $?                 # icke-noll = fel

# Avsluta script med status
exit 0                  # Lyckat
exit 1                  # Fel
```

---

## IF-satser

```bash
# Grundläggande syntax
if [ villkor ]; then
    kommandon
fi

# If-else
if [ villkor ]; then
    kommandon
else
    andra kommandon
fi

# If-elif-else
if [ villkor1 ]; then
    kommandon1
elif [ villkor2 ]; then
    kommandon2
else
    kommandon3
fi
```

---

## Test-operatorer

### Strängar
```bash
[ "$str" = "text" ]     # Lika med
[ "$str" != "text" ]    # Inte lika med
[ -z "$str" ]           # Tom sträng
[ -n "$str" ]           # Inte tom
```

### Numeriskt
```bash
[ $a -eq $b ]           # Equal
[ $a -ne $b ]           # Not equal
[ $a -lt $b ]           # Less than
[ $a -le $b ]           # Less or equal
[ $a -gt $b ]           # Greater than
[ $a -ge $b ]           # Greater or equal
```

### Filer
```bash
[ -f "$fil" ]           # Fil existerar
[ -d "$dir" ]           # Katalog existerar
[ -e "$path" ]          # Existerar (fil eller katalog)
[ -r "$fil" ]           # Läsbar
[ -w "$fil" ]           # Skrivbar
[ -x "$fil" ]           # Körbar
[ -s "$fil" ]           # Har innehåll
```

### Kombinera villkor
```bash
[ villkor1 -a villkor2 ]    # AND
[ villkor1 -o villkor2 ]    # OR
[ ! villkor ]               # NOT
```

---

## CASE-satser

```bash
case $variabel in
    pattern1)
        kommandon
        ;;
    pattern2|pattern3)
        kommandon för båda
        ;;
    *)
        default
        ;;
esac
```

---

## Viktigt att komma ihåg

1. **Citattecken runt variabler** - `"$var"` inte `$var`
2. **Inget mellanslag runt =** - `var="value"`
3. **-eq för tal, = för strängar**
4. **Mellanslag runt [ och ]**

""",
            "quiz": [
                {
                    "question": "Vilken operator jämför två tal för likhet?",
                    "options": ["=", "==", "-eq", "-e"],
                    "correct": 2,
                    "explanation": "-eq (equal) används för numeriska jämförelser. = används för strängar.",
                },
                {
                    "question": "Vad innehåller $# i ett script?",
                    "options": [
                        "Scriptets namn",
                        "Antal argument",
                        "Exit status",
                        "Process ID",
                    ],
                    "correct": 1,
                    "explanation": "$# innehåller antalet argument som skickades till scriptet.",
                },
                {
                    "question": "Vilken test-operator kontrollerar om en fil existerar?",
                    "options": ["-e", "-d", "-f", "-x"],
                    "correct": 2,
                    "explanation": "-f kontrollerar om en regular file existerar. -d är för kataloger, -e för båda.",
                },
            ],
        },
        # =============================================================================
        # NOD 4: Bash Scripting Avancerat
        # =============================================================================
        {
            "title": "Bash Scripting Avancerat",
            "slug": "bash-scripting-avancerat",
            "description": "Loopar (for, while, until), funktioner, select-menyer och read.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 120,
            "order_index": 4,
            "content": r"""# Bash Scripting Avancerat

## FOR-loop

```bash
# Lista
for item in äpple banan citron; do
    echo "Jag gillar $item"
done

# Filer
for fil in *.txt; do
    echo "Bearbetar $fil"
done

# Range
for i in {1..5}; do
    echo "Nummer: $i"
done

# C-style
for ((i=1; i<=5; i++)); do
    echo "Nummer: $i"
done
```

---

## WHILE-loop

```bash
counter=1
while [ $counter -le 5 ]; do
    echo "Nummer: $counter"
    ((counter++))
done

# Läsa fil rad för rad
while read line; do
    echo "Rad: $line"
done < fil.txt
```

---

## UNTIL-loop

```bash
# Kör TILLS villkoret blir sant
counter=1
until [ $counter -gt 5 ]; do
    echo "Nummer: $counter"
    ((counter++))
done
```

---

## BREAK och CONTINUE

```bash
# break - hoppa ur loopen
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done

# continue - hoppa till nästa iteration
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo $i     # Skriver 1, 2, 4, 5
done
```

---

## SELECT (menyer)

```bash
PS3="Välj alternativ: "
select opt in "Starta" "Stoppa" "Avsluta"; do
    case $opt in
        "Starta") echo "Startar..." ;;
        "Stoppa") echo "Stoppar..." ;;
        "Avsluta") break ;;
        *) echo "Ogiltigt" ;;
    esac
done
```

---

## SHIFT

```bash
# Shift flyttar argument åt vänster
while [ $# -gt 0 ]; do
    echo "Argument: $1"
    shift
done
```

---

## Funktioner

```bash
# Definiera funktion
greet() {
    echo "Hej $1!"
}

# Med return-värde
check_file() {
    if [ -f "$1" ]; then
        return 0
    else
        return 1
    fi
}

# Anropa
greet "Said"

if check_file "/etc/passwd"; then
    echo "Filen finns"
fi
```

---

## Lokala variabler

```bash
name="Global"

test_scope() {
    local name="Lokal"
    echo "Inne: $name"
}

echo "Före: $name"   # Global
test_scope           # Lokal
echo "Efter: $name"  # Global
```

---

## READ (användarinput)

```bash
read -p "Ditt namn: " name
echo "Hej $name!"

# Tyst input (lösenord)
read -sp "Lösenord: " password

# Med timeout
read -t 10 -p "Svar inom 10 sek: " answer
```

""",
            "quiz": [
                {
                    "question": "Vad gör 'shift' kommandot?",
                    "options": [
                        "Sorterar argument",
                        "Flyttar argument åt vänster",
                        "Lägger till argument",
                        "Tar bort alla argument",
                    ],
                    "correct": 1,
                    "explanation": "shift flyttar alla positionsparametrar ett steg åt vänster. $2 blir $1, osv.",
                },
                {
                    "question": "Vad är skillnaden mellan while och until?",
                    "options": [
                        "Ingen skillnad",
                        "while kör medan sant, until kör tills sant",
                        "until är snabbare",
                        "while kan bara användas med tal",
                    ],
                    "correct": 1,
                    "explanation": "while kör så länge villkoret är sant. until kör tills villkoret blir sant.",
                },
                {
                    "question": "Vad gör 'local' nyckelordet i en funktion?",
                    "options": [
                        "Exporterar variabeln",
                        "Gör variabeln endast tillgänglig i funktionen",
                        "Gör variabeln read-only",
                        "Tar bort variabeln",
                    ],
                    "correct": 1,
                    "explanation": "local skapar en variabel som endast existerar inom funktionen.",
                },
            ],
        },
        # =============================================================================
        # NOD 5: Användare & Rättigheter
        # =============================================================================
        {
            "title": "Användare & Rättigheter",
            "slug": "anvandare-rattigheter",
            "description": "Användarhantering, grupper, chmod, chown, umask och speciella permissions.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "order_index": 5,
            "content": r"""# Användare & Rättigheter

## Viktiga filer

### /etc/passwd (7 fält)
```
username:x:UID:GID:kommentar:hemma:shell
said:x:1000:1000:Said Ali:/home/said:/bin/bash
```

### /etc/shadow (lösenordshash)
```
username:hash:lastchange:min:max:warn:inactive:expire:reserved
```

### /etc/group (4 fält)
```
groupname:x:GID:medlemmar
sudo:x:27:said,anna
```

---

## Användarhantering

```bash
# Skapa användare
useradd -m username                   # Med hemkatalog
useradd -m -s /bin/bash username      # Med shell
useradd -m -G sudo,docker username    # Med grupper

# Sätt lösenord
passwd username

# Ändra användare
usermod -aG sudo username             # Lägg till i grupp
usermod -s /bin/zsh username          # Ändra shell

# Ta bort användare
userdel username                      # Behåll hemkatalog
userdel -r username                   # Ta bort allt
```

---

## Grupphantering

```bash
groupadd groupname              # Skapa grupp
usermod -aG groupname username  # Lägg till i grupp
groups username                 # Visa grupper
id username                     # Visa UID, GID, grupper
groupdel groupname              # Ta bort grupp
```

---

## Sudo

```bash
# Redigera sudoers (ALLTID med visudo!)
sudo visudo

# Syntax i sudoers
username ALL=(ALL:ALL) ALL

# Sudo utan lösenord
username ALL=(ALL) NOPASSWD: ALL

# Grupp med sudo
%sudo ALL=(ALL:ALL) ALL
```

---

## Permissions

```
rwx = Read, Write, Execute
4     2      1

User  Group  Others
rwx   rwx    rwx
```

---

## chmod

### Symboliskt
```bash
chmod u+x fil.sh          # User +execute
chmod g-w fil.txt         # Group -write
chmod o=r fil.txt         # Others =read only
chmod a+r fil.txt         # All +read
```

### Oktalt
```bash
chmod 755 fil.sh          # rwxr-xr-x
chmod 644 fil.txt         # rw-r--r--
chmod 700 privat/         # rwx------
chmod -R 755 katalog/     # Rekursivt
```

---

## chown

```bash
chown user fil.txt              # Ändra ägare
chown user:group fil.txt        # Ändra ägare och grupp
chown -R user:group katalog/    # Rekursivt
```

---

## umask

```bash
umask                     # Visa nuvarande (ofta 022)

# Beräkning
# Filer: 666 - umask = default
# Kataloger: 777 - umask = default

# umask 022:
# Filer:     644 (rw-r--r--)
# Kataloger: 755 (rwxr-xr-x)
```

---

## Speciella permissions

### SUID (4xxx)
```bash
chmod u+s fil             # Kör som ägaren
chmod 4755 fil
```

### SGID (2xxx)
```bash
chmod g+s katalog/        # Nya filer ärver grupp
chmod 2755 katalog/
```

### Sticky bit (1xxx)
```bash
chmod +t katalog/         # Endast ägare kan ta bort
chmod 1777 katalog/
```

---

## Snabbreferens

| Värde | Permissions | Användning |
|-------|-------------|------------|
| 755 | rwxr-xr-x | Scripts |
| 644 | rw-r--r-- | Filer |
| 700 | rwx------ | Privat katalog |
| 600 | rw------- | SSH-nycklar |

""",
            "quiz": [
                {
                    "question": "Vad är chmod 755 i symbolisk form?",
                    "options": ["rw-r--r--", "rwxr-xr-x", "rwx------", "rwxrwxrwx"],
                    "correct": 1,
                    "explanation": "755 = 7(rwx) + 5(r-x) + 5(r-x) = rwxr-xr-x",
                },
                {
                    "question": "Vilket kommando lägger till en användare i gruppen 'docker'?",
                    "options": [
                        "useradd -G docker user",
                        "usermod -aG docker user",
                        "groupadd docker user",
                        "adduser docker user",
                    ],
                    "correct": 1,
                    "explanation": "usermod -aG (append Group) lägger till användaren i gruppen utan att ta bort från andra grupper.",
                },
                {
                    "question": "Vad gör sticky bit på en katalog?",
                    "options": [
                        "Gör katalogen osynlig",
                        "Endast ägare kan ta bort sina egna filer",
                        "Alla kan ta bort alla filer",
                        "Katalogen blir read-only",
                    ],
                    "correct": 1,
                    "explanation": "Sticky bit (t) på kataloger betyder att endast filens ägare kan ta bort filen.",
                },
            ],
        },
        # =============================================================================
        # NOD 6: SSH & Säkerhet
        # =============================================================================
        {
            "title": "SSH & Säkerhet",
            "slug": "ssh-sakerhet",
            "description": "SSH-nycklar, sshd_config, scp och ssh-alias för säker åtkomst.",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "order_index": 6,
            "content": r"""# SSH & Säkerhet

## SSH-nycklar

```bash
# Generera nyckelpar (på klienten)
ssh-keygen -t ed25519 -C "said@example.com"
# Sparas i ~/.ssh/id_ed25519 (privat) och .pub (publik)

# Alternativ: RSA
ssh-keygen -t rsa -b 4096

# Kopiera publik nyckel till server
ssh-copy-id user@server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Manuellt
cat ~/.ssh/id_ed25519.pub | ssh user@server \
    "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

---

## SSH-konfiguration (server)

```bash
# Redigera /etc/ssh/sshd_config
sudo nano /etc/ssh/sshd_config

# Viktiga inställningar
Port 2222                           # Byt från default 22
PermitRootLogin no                  # Neka root-login
PasswordAuthentication no           # Endast nycklar
PubkeyAuthentication yes            # Tillåt nycklar
AllowUsers said anna                # Endast dessa användare
MaxAuthTries 3                      # Max inloggningsförsök

# Starta om SSH
sudo systemctl restart ssh          # Ubuntu/Debian
sudo systemctl restart sshd         # CentOS/Fedora
```

---

## SSH-kommandon

```bash
# Anslut
ssh user@server
ssh -p 2222 user@server             # Annan port
ssh -i ~/.ssh/mykey user@server     # Specifik nyckel

# Kör kommando remote
ssh user@server "ls -la"
ssh user@server "df -h && free -m"

# Kopiera filer (scp)
scp fil.txt user@server:/path/      # Lokal -> Remote
scp user@server:/path/fil.txt ./    # Remote -> Lokal
scp -P 2222 fil.txt user@server:    # Annan port
scp -r katalog/ user@server:/path/  # Rekursivt
```

---

## SSH-alias

```bash
# ~/.ssh/config
Host myserver
    HostName 192.168.1.100
    User said
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

# Nu kan du köra:
ssh myserver
```

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Generera nyckel | `ssh-keygen -t ed25519` |
| Kopiera nyckel | `ssh-copy-id user@server` |
| Anslut port 2222 | `ssh -p 2222 user@server` |
| Kopiera fil | `scp fil.txt user@server:/path/` |
| Kopiera mapp | `scp -r katalog/ user@server:` |

""",
            "quiz": [
                {
                    "question": "Vilken SSH-inställning nekar root att logga in?",
                    "options": [
                        "DenyRoot yes",
                        "PermitRootLogin no",
                        "RootLogin false",
                        "AllowRoot no",
                    ],
                    "correct": 1,
                    "explanation": "PermitRootLogin no i /etc/ssh/sshd_config nekar direktinloggning som root.",
                },
                {
                    "question": "Vilket kommando kopierar din publika nyckel till en server?",
                    "options": [
                        "ssh-copy",
                        "scp ~/.ssh/id_ed25519.pub",
                        "ssh-copy-id user@server",
                        "ssh-keygen -c",
                    ],
                    "correct": 2,
                    "explanation": "ssh-copy-id kopierar automatiskt din publika nyckel till serverns authorized_keys.",
                },
                {
                    "question": "Vilken flagga anger en annan port för scp?",
                    "options": ["-p", "-P", "--port", "-port"],
                    "correct": 1,
                    "explanation": "scp använder stort -P för port (ssh använder litet -p). scp -P 2222 fil.txt user@server:",
                },
            ],
        },
        # =============================================================================
        # NOD 7: Firewall
        # =============================================================================
        {
            "title": "Firewall",
            "slug": "firewall",
            "description": "UFW (Ubuntu) och FirewallD (CentOS/Fedora) för nätverkssäkerhet.",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "order_index": 7,
            "content": r"""# Firewall

## UFW (Ubuntu)

```bash
# Status
sudo ufw status
sudo ufw status numbered

# Enable/Disable
sudo ufw enable
sudo ufw disable

# Tillåt
sudo ufw allow 22                   # Port
sudo ufw allow ssh                  # Service
sudo ufw allow 22/tcp               # Specifikt protokoll
sudo ufw allow from 192.168.1.0/24  # Subnät
sudo ufw allow from 192.168.1.100 to any port 22

# Neka
sudo ufw deny 23
sudo ufw deny from 10.0.0.0/8

# Ta bort regel
sudo ufw status numbered
sudo ufw delete 2                   # Ta bort regel nummer 2

# Reset
sudo ufw reset
```

---

## FirewallD (Fedora/CentOS)

```bash
# Status
sudo firewall-cmd --state
sudo firewall-cmd --list-all

# Öppna port
sudo firewall-cmd --add-port=22/tcp --permanent
sudo firewall-cmd --add-service=ssh --permanent

# Ta bort
sudo firewall-cmd --remove-port=22/tcp --permanent
sudo firewall-cmd --remove-service=ssh --permanent

# Ladda om (KRÄVS efter --permanent!)
sudo firewall-cmd --reload

# Zoner
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --zone=public --list-all
```

---

## Snabbreferens UFW

| Uppgift | Kommando |
|---------|----------|
| Aktivera | `sudo ufw enable` |
| Status | `sudo ufw status` |
| Tillåt SSH | `sudo ufw allow ssh` |
| Tillåt port | `sudo ufw allow 8080/tcp` |
| Ta bort regel | `sudo ufw delete 2` |

## Snabbreferens FirewallD

| Uppgift | Kommando |
|---------|----------|
| Status | `firewall-cmd --state` |
| Öppna port | `firewall-cmd --add-port=80/tcp --permanent` |
| Öppna service | `firewall-cmd --add-service=http --permanent` |
| Reload | `firewall-cmd --reload` |

""",
            "quiz": [
                {
                    "question": "Vilket kommando aktiverar UFW?",
                    "options": [
                        "ufw start",
                        "ufw enable",
                        "sudo ufw enable",
                        "systemctl start ufw",
                    ],
                    "correct": 2,
                    "explanation": "sudo ufw enable aktiverar UFW-brandväggen.",
                },
                {
                    "question": "Vad måste du göra efter --permanent i firewalld?",
                    "options": [
                        "Starta om servern",
                        "Köra firewall-cmd --reload",
                        "Inget, det gäller direkt",
                        "Köra systemctl restart firewalld",
                    ],
                    "correct": 1,
                    "explanation": "--permanent sparar regeln men aktiverar den inte. Du måste köra --reload för att aktivera.",
                },
                {
                    "question": "Hur tar du bort regel nummer 3 i UFW?",
                    "options": [
                        "ufw remove 3",
                        "ufw delete 3",
                        "sudo ufw delete 3",
                        "sudo ufw remove rule 3",
                    ],
                    "correct": 2,
                    "explanation": "sudo ufw delete [nummer] tar bort regeln. Använd 'ufw status numbered' först för att se numren.",
                },
            ],
        },
        # =============================================================================
        # NOD 8: Docker Basics
        # =============================================================================
        {
            "title": "Docker Basics",
            "slug": "docker-basics",
            "description": "Containers, images, volumes och networks - grunderna i Docker.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "order_index": 8,
            "content": r"""# Docker Basics

## Grundläggande kommandon

```bash
# Kör container
docker run hello-world              # Testa installation
docker run -it ubuntu bash          # Interaktivt
docker run -d nginx                 # Bakgrund (detached)
docker run --rm alpine echo "hej"   # Ta bort efter körning
docker run --name mycontainer nginx # Namnge container
docker run -p 8080:80 nginx         # Port mapping

# Lista
docker ps                           # Körande containers
docker ps -a                        # Alla containers
docker images                       # Alla images

# Stoppa/Starta
docker stop container_name
docker start container_name
docker restart container_name

# Ta bort
docker rm container_name            # Container
docker rmi image_name               # Image
docker container prune              # Alla stoppade
docker image prune                  # Oanvända images
docker system prune                 # Städa allt
```

---

## Container-koncept

```
En container är en PROCESS som körs isolerad från systemet.

Isolering:
- Användare: root i container ≠ root på host
- Nätverk: egna interfaces
- Filsystem: eget filsystem
- Processer: ser ej host-processer
```

---

## Port Mapping

```bash
# -p host_port:container_port
docker run -p 8080:80 nginx         # Host 8080 -> Container 80
docker run -p 80:80 nginx           # Host 80 -> Container 80
docker run -p 127.0.0.1:8080:80 nginx  # Endast localhost

# OBS! Docker kringgår UFW/FirewallD!
```

---

## Volumes (beständig data)

```bash
# Named volume (Docker hanterar)
docker volume create mydata
docker run -v mydata:/data alpine

# Bind mount (specifik path)
docker run -v /host/path:/container/path alpine
docker run -v $(pwd)/data:/data alpine

# Lista volymer
docker volume ls

# Ta bort
docker volume rm mydata
docker volume prune                 # Oanvända
```

---

## Networks

```bash
# Typer
bridge    # Default, containers kan kommunicera
host      # Samma nätverk som host
none      # Ingen nätverkskoppling

# Kommandon
docker network ls
docker network create mynet
docker run --network mynet alpine
docker network rm mynet

# Container-kommunikation (samma nätverk)
docker run -d --name db --network mynet postgres
docker run -d --name web --network mynet nginx
# web kan nå db via hostname "db"
```

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Kör interaktivt | `docker run -it ubuntu bash` |
| Kör i bakgrund | `docker run -d nginx` |
| Port mapping | `docker run -p 8080:80 nginx` |
| Med volume | `docker run -v mydata:/data nginx` |
| Lista containers | `docker ps -a` |
| Stoppa | `docker stop container_name` |
| Ta bort | `docker rm container_name` |
| Städa allt | `docker system prune` |

""",
            "quiz": [
                {
                    "question": "Vad gör flaggan -d i docker run?",
                    "options": [
                        "Delete after run",
                        "Detached (bakgrund)",
                        "Debug mode",
                        "Download image",
                    ],
                    "correct": 1,
                    "explanation": "-d (detached) kör containern i bakgrunden så du får tillbaka terminalen.",
                },
                {
                    "question": "Hur mappar du host-port 8080 till container-port 80?",
                    "options": [
                        "-p 80:8080",
                        "-p 8080:80",
                        "-P 8080:80",
                        "--port 8080=80",
                    ],
                    "correct": 1,
                    "explanation": "-p host:container, alltså -p 8080:80 mappar host 8080 till container 80.",
                },
                {
                    "question": "Vad är sant om Docker och firewall?",
                    "options": [
                        "Docker följer alltid UFW-regler",
                        "Docker kringgår UFW/FirewallD",
                        "Docker kräver att firewall är avstängd",
                        "Firewall blockerar alltid Docker",
                    ],
                    "correct": 1,
                    "explanation": "Docker manipulerar iptables direkt och kan kringgå UFW/FirewallD. Var försiktig med port-exponering!",
                },
            ],
        },
        # =============================================================================
        # NOD 9: Docker Compose
        # =============================================================================
        {
            "title": "Docker Compose",
            "slug": "docker-compose",
            "description": "Multi-container-applikationer med docker-compose.yml.",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 120,
            "order_index": 9,
            "content": r"""# Docker Compose

## Vad är Docker Compose?

```
Docker Compose = hantera multi-container-applikationer
- Definiera services, networks, volumes i EN fil
- Starta allt med ETT kommando
- Automatisk nätverkshantering
```

---

## docker-compose.yml exempel

```yaml
version: "3.8"

services:
  web:
    image: nginx
    ports:
      - "8080:80"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - dbdata:/var/lib/postgresql/data

volumes:
  dbdata:
```

---

## Compose-kommandon

```bash
# Starta (i katalogen med docker-compose.yml)
docker compose up                   # Förgrund
docker compose up -d                # Bakgrund (detached)

# Stoppa
docker compose down                 # Stoppa + ta bort containers
docker compose down -v              # + ta bort volumes
docker compose down --rmi all       # + ta bort images

# Status
docker compose ps
docker compose logs
docker compose logs -f              # Follow
docker compose logs web             # Specifik service

# Skala
docker compose up -d --scale web=3  # 3 instanser av web
```

---

## Miljövariabler

```yaml
# Direkt i compose (UNDVIK för känslig data!)
services:
  db:
    environment:
      POSTGRES_PASSWORD: secret

# Från .env-fil (BÄTTRE!)
services:
  db:
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
```

**.env fil (COMMITTA ALDRIG!)**
```
DB_PASSWORD=supersecret
```

**.gitignore**
```
.env
```

---

## YAML-grunder

```yaml
# Key-value
name: Said
age: 25

# Lista
fruits:
  - apple
  - banana

# Nested
person:
  name: Said
  address:
    city: Stockholm
```

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Starta | `docker compose up -d` |
| Stoppa | `docker compose down` |
| Stoppa + volymer | `docker compose down -v` |
| Loggar | `docker compose logs -f` |
| Status | `docker compose ps` |
| Skala | `docker compose up -d --scale web=3` |

""",
            "quiz": [
                {
                    "question": "Vad gör 'docker compose down -v'?",
                    "options": [
                        "Verbose output",
                        "Stoppar och tar bort volumes",
                        "Validerar compose-fil",
                        "Visar version",
                    ],
                    "correct": 1,
                    "explanation": "-v tar även bort namngivna volumes. Utan -v behålls data i volumes.",
                },
                {
                    "question": "Var ska känslig data som lösenord lagras?",
                    "options": [
                        "Direkt i docker-compose.yml",
                        "I en .env-fil",
                        "Som kommandoradsargument",
                        "I Dockerfile",
                    ],
                    "correct": 1,
                    "explanation": "Känslig data ska lagras i .env-filer som INTE committas till git.",
                },
                {
                    "question": "Vad gör 'depends_on' i docker-compose.yml?",
                    "options": [
                        "Installerar dependencies",
                        "Anger startordning för services",
                        "Delar nätverk",
                        "Kräver specifik version",
                    ],
                    "correct": 1,
                    "explanation": "depends_on anger att en service ska starta efter en annan, t.ex. web efter db.",
                },
            ],
        },
        # =============================================================================
        # NOD 10: Systemd
        # =============================================================================
        {
            "title": "Systemd",
            "slug": "systemd",
            "description": "systemctl, journalctl och skapa egna service-filer.",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "order_index": 10,
            "content": r"""# Systemd

## systemctl

```bash
# Service-hantering
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx         # Ladda om config

# Status
systemctl status nginx
systemctl is-active nginx
systemctl is-enabled nginx

# Enable/Disable (vid boot)
sudo systemctl enable nginx
sudo systemctl disable nginx

# Lista services
systemctl list-units --type=service
systemctl list-units --type=service --state=running
```

---

## journalctl (loggar)

```bash
journalctl                          # Alla loggar
journalctl -u nginx                 # Specifik service
journalctl -u nginx -f              # Follow
journalctl -u nginx --since "1 hour ago"
journalctl -u nginx --since "2024-01-01"
journalctl -b                       # Sedan boot
journalctl -b -1                    # Förra boot
```

---

## Skapa egen service

**/etc/systemd/system/myapp.service**

```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=said
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
# Efter att skapat/ändrat service-fil
sudo systemctl daemon-reload        # VIKTIGT!
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Service-fil förklaring

| Sektion | Direktiv | Betydelse |
|---------|----------|-----------|
| [Unit] | Description | Beskrivning av tjänsten |
| [Unit] | After | Starta efter denna tjänst |
| [Service] | Type | simple, forking, oneshot |
| [Service] | User | Kör som denna användare |
| [Service] | ExecStart | Kommando att köra |
| [Service] | Restart | always, on-failure, no |
| [Install] | WantedBy | multi-user.target för boot |

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Starta service | `sudo systemctl start nginx` |
| Stoppa service | `sudo systemctl stop nginx` |
| Status | `systemctl status nginx` |
| Aktivera vid boot | `sudo systemctl enable nginx` |
| Visa loggar | `journalctl -u nginx` |
| Följ loggar | `journalctl -u nginx -f` |
| Ladda om config | `sudo systemctl daemon-reload` |

---

## Viktigt att komma ihåg

1. **daemon-reload** efter ändringar i service-filer
2. **enable** för att starta vid boot
3. **journalctl -u** för service-specifika loggar
4. Service-filer ligger i `/etc/systemd/system/`

""",
            "quiz": [
                {
                    "question": "Vad måste du köra efter att ha ändrat en service-fil?",
                    "options": [
                        "systemctl restart",
                        "systemctl reload",
                        "systemctl daemon-reload",
                        "systemctl refresh",
                    ],
                    "correct": 2,
                    "explanation": "daemon-reload laddar om systemd's konfiguration så den ser ändringarna i service-filer.",
                },
                {
                    "question": "Vilket kommando visar loggar för nginx-tjänsten?",
                    "options": [
                        "cat /var/log/nginx",
                        "journalctl nginx",
                        "journalctl -u nginx",
                        "systemctl logs nginx",
                    ],
                    "correct": 2,
                    "explanation": "journalctl -u (unit) visar loggar för en specifik systemd-tjänst.",
                },
                {
                    "question": "Vad gör 'systemctl enable nginx'?",
                    "options": [
                        "Startar nginx nu",
                        "Gör att nginx startar vid boot",
                        "Aktiverar nginx-moduler",
                        "Tillåter nginx i firewall",
                    ],
                    "correct": 1,
                    "explanation": "enable skapar en symlink så att tjänsten startar automatiskt vid systemstart.",
                },
            ],
        },
    ],
}
