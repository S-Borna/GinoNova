"""
NOD: Avancerade behörigheter och säkerhet
=========================================
Säkra data och hantera identiteter med behörigheter, ACL och särskilda attribut
"""

RATTIGHETER_SAKERHET_NODE = {
    "title": "Avancerade behörigheter och säkerhet",
    "slug": "rattigheter-sakerhet",
    "description": "Säkra data och hantera identiteter med behörigheter, ACL och särskilda attribut",
    "difficulty": "medium",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "order_index": 2,
    "content": r"""# Avancerade behörigheter och säkerhet

Fokus: Dataskydd och identitetshantering

## Behörighetsmatris

Linux-filbehörigheter baseras på en numerisk kod med tre bitar:

- **Read (4)**: Läsa filer, lista innehåll i kataloger
- **Write (2)**: Skriva/modifiera filer, skapa/radera i kataloger
- **Execute (1)**: Exekvera filer, navigera in i kataloger

Behörigheter tilldelas tre kategorier:

- **User (u)**: Filägaren
- **Group (g)**: Gruppmedlemmar
- **Others (o)**: Övriga användare

```bash
# Exempel: rwxr-xr--
# User:   rwx = 4+2+1 = 7 (läs, skriv, exekvera)
# Group:  r-x = 4+0+1 = 5 (läs, exekvera)
# Others: r-- = 4+0+0 = 4 (endast läs)

chmod 754 filename
# User: läs, skriv, exekvera
# Group: läs, exekvera
# Others: endast läs
```

### Numeriska vs Symboliska behörigheter

```bash
# Numerisk (oktal)
chmod 755 script.sh
chmod 644 file.txt
chmod 600 private.key

# Symbolisk
chmod u+x script.sh        # Lägg till exekvera för user
chmod g-w file.txt         # Ta bort skriv för group
chmod o+r file.txt         # Lägg till läs för others
chmod a+x script.sh        # Lägg till exekvera för alla (a=all)
```

### Vad händer om en katalog får behörigheten 644?

**Kritiskt**: En katalog kräver exekveringsbehörighet (x) för att kunna navigeras med `cd`.

```bash
# Felaktig: Katalog utan exekvera
chmod 644 directory/
# Du kan lista innehållet (läs), men INTE navigera in (cd directory/ misslyckas)

# Korrekt: Katalog med exekvera
chmod 755 directory/
# Nu kan du både lista och navigera in i katalogen
```

**Regel**: För kataloger behövs minst r-x (5) för att kunna navigera.

## Umask och standardbehörigheter

### Vad är umask?

umask (user file creation mask) bestämmer standardbehörigheterna för nya filer och kataloger.

```bash
# Visa aktuell umask
umask
# 0022

# Förklaring av 0022:
# 0 = särskilda bitar (SUID, SGID, Sticky)
# 022 = mask för user, group, others
```

### Hur umask fungerar

Umask subtraheras från standardbehörigheterna:

- **Filer**: Standard 666 (rw-rw-rw-), umask 022 → Resultat: 644 (rw-r--r--)
- **Kataloger**: Standard 777 (rwxrwxrwx), umask 022 → Resultat: 755 (rwxr-xr-x)

```bash
# Exempel med umask 0022
umask 0022
touch newfile.txt
mkdir newdir
ls -l
# -rw-r--r-- newfile.txt  (644)
# drwxr-xr-x newdir       (755)
```

### Vanliga umask-värden

```bash
# 0022 - Standard (user: rwx, group/others: r-x)
umask 0022
# Filer: 644, Kataloger: 755

# 0002 - Mer öppen (group kan skriva)
umask 0002
# Filer: 664, Kataloger: 775

# 0077 - Mycket privat (endast user)
umask 0077
# Filer: 600, Kataloger: 700
```

### Permanenta umask-inställningar

```bash
# För användare: lägg till i ~/.bashrc eller ~/.profile
umask 0022

# Systemomfattande: /etc/profile eller /etc/bash.bashrc
```

**Notera**: Linux tilldelar aldrig exekveringsbehörighet (x) på filer som standard, även om umask tillåter det.

## Särskilda bitar

### Sticky Bit (används i /tmp)

Sticky bit garanterar att endast filägaren kan radera egna filer, även om katalogen är skrivbar för alla.

```bash
# Aktivera sticky bit
chmod +t /tmp
# eller
chmod 1777 /tmp

# Kontrollera
ls -ld /tmp
# drwxrwxrwt  # 't' i slutet = sticky bit
```

**Användning**: /tmp - alla kan skriva, men endast ägaren kan radera egna filer.

### SUID (Set User ID)

När en fil med SUID exekveras, körs den med filägarens behörigheter, inte användarens.

```bash
# Exempel: passwd-kommandot
ls -l /usr/bin/passwd
# -rwsr-xr-x  # 's' i user-position = SUID

# Aktivera SUID
chmod u+s program
chmod 4755 program  # 4 = SUID-bit
```

**Säkerhetsvarning**: SUID kan vara farligt om det missbrukas!

### SGID (Set Group ID)

När en fil med SGID exekveras, körs den med filens gruppbehörigheter.

```bash
# Aktivera SGID
chmod g+s program
chmod 2755 program  # 2 = SGID-bit

# För kataloger: nya filer får samma grupp
chmod g+s /shared/directory
```

## Användarhantering

### Skillnaden mellan /etc/passwd och /etc/shadow

**/etc/passwd**: Innehåller grundläggande användarinformation (läsbar för alla)

```bash
cat /etc/passwd
# Format: användarnamn:x:UID:GID:kommentar:hem:skal
# 'x' indikerar att lösenordet finns i /etc/shadow
```

**/etc/shadow**: Innehåller krypterade lösenord (endast root kan läsa)

```bash
sudo cat /etc/shadow
# Format: användarnamn:krypterat_lösenord:senast_ändrad:min:max:varna:inaktiv:utgång
```

```bash
# Skapa användare
sudo useradd -m -s /bin/bash newuser

# Ändra lösenord
sudo passwd newuser

# Lägg till användare i grupp
sudo usermod -aG sudo newuser
sudo usermod -aG docker newuser

# Visa vilka grupper en användare tillhör
groups
# eller
groups username

# Visa användar-ID och grupp-ID
id
# uid=1000(user) gid=1000(user) groups=1000(user),27(sudo),999(docker)
```

### /etc/group

Innehåller information om grupper och medlemmar:

```bash
cat /etc/group
# Format: gruppnamn:lösenord:GID:medlemmar
# docker:x:999:user1,user2
```

### /etc/login.defs

Systemomfattande inställningar för användarhantering:

```bash
# Visa viktiga inställningar
grep -E "^[A-Z]" /etc/login.defs

# Vanliga inställningar:
# UID_MIN / UID_MAX - Intervall för vanliga användare
# GID_MIN / GID_MAX - Intervall för vanliga grupper
# CREATE_HOME yes - Skapa hemkatalog automatiskt
# UMASK 022 - Standard umask
```

### su vs sudo

**su (switch user)**: Byter till en annan användare (kräver målanvändarens lösenord)

```bash
# Byta till root (kräver root-lösenord)
su -

# Byta till annan användare
su - username

# Byta utan att ladda miljövariabler
su username
```

**sudo (superuser do)**: Exekverar kommandon med root-behörigheter (kräver eget lösenord)

```bash
# Exekvera kommando som root
sudo command

# Byta till root med sudo
sudo -i
sudo -s

# Exekvera som annan användare
sudo -u username command
```

**Skillnad**: su kräver målanvändarens lösenord, sudo kräver eget lösenord och konfiguration i /etc/sudoers.

### stat - Detaljerad filinformation

stat visar mer omfattande information än `ls -l`:

```bash
# Visa detaljerad information
stat file.txt
# File: file.txt
# Size: 1024        Blocks: 8          IO Block: 4096   regular file
# Device: 803h/2051d      Inode: 123456     Links: 1
# Access: (0644/-rw-r--r--)  Uid: ( 1000/   user)   Gid: ( 1000/   user)
# Access: 2024-01-15 10:30:00.000000000 +0100
# Modify: 2024-01-15 10:30:00.000000000 +0100
# Change: 2024-01-15 10:30:00.000000000 +0100
# Birth: -

# Visa endast specifik information
stat -c "%a %n" file.txt  # Numeriska behörigheter
stat -c "%U:%G" file.txt  # Ägare:grupp
stat -c "%y" file.txt     # Modifieringstid
```

### Ägande: Rekursiv användning av chown och chmod -R

```bash
# Ändra ägare rekursivt
sudo chown -R user:group /path/to/directory

# Ändra behörigheter rekursivt
chmod -R 755 /path/to/directory

# Kombinera
sudo chown -R www-data:www-data /var/www
sudo chmod -R 755 /var/www
```

**Varning**: -R är kraftfullt - kontrollera sökvägen noggrant!

```bash
# Säkrare metod: testa först med find
find /path/to/dir -type f -exec chmod 644 {} \;
find /path/to/dir -type d -exec chmod 755 {} \;
```

## Capabilities

Capabilities ger processer root-liknande förmågor utan att vara root. Exempel: binda port 80 (som normalt kräver root).

```bash
# Visa capabilities för ett program
getcap /usr/bin/ping

# Tilldela capability
sudo setcap cap_net_bind_service=+ep /usr/bin/myprogram

# Exempel: Nginx kan binda port 80 utan root
sudo setcap cap_net_bind_service=+ep /usr/sbin/nginx
```

### Vanliga capabilities

- **cap_net_bind_service**: Binda privilegierade portar (< 1024)
- **cap_net_raw**: Använda raw sockets (t.ex. ping)
- **cap_sys_admin**: Administrativa operationer

```bash
# Lista alla capabilities
capsh --print

# Exekvera program med capabilities
sudo capsh --caps="cap_net_bind_service+ep" -- -c "./server"
```

## ACL (Access Control Lists)

ACL möjliggör specifika behörigheter till specifika användare/grupper utöver standard Owner/Group/Others.

### Begränsning med klassiska behörigheter

Klassiska Linux-behörigheter kan endast tilldela behörigheter till:
- En användare (owner)
- En grupp (group)
- Alla andra (others)

**Problem**: Om du vill tilldela behörigheter till flera specifika användare eller grupper behövs ACL.

### setfacl - Tilldela ACL

```bash
# Tilldela specifik användare läsbehörighet
setfacl -m u:username:r file.txt

# Tilldela grupp skrivbehörighet
setfacl -m g:developers:w file.txt

# Kombinera flera behörigheter
setfacl -m u:alice:rwx file.txt
setfacl -m g:team:r-x file.txt

# Rekursivt för kataloger
setfacl -R -m u:username:rwx /path/to/directory
```

### getfacl - Visa ACL

```bash
# Visa ACL för fil
getfacl file.txt
# # file: file.txt
# # owner: user
# # group: user
# user::rw-
# user:alice:rwx
# group::r--
# group:developers:rw-
# mask::rwx
# other::r--

# ls -l visar + när ACL finns
ls -l file.txt
# -rw-r--r--+ 1 user user 1024 file.txt
#                              ↑
#                              + = ACL finns
```

### Avlägsna ACL

```bash
# Avlägsna specifik ACL-post
setfacl -x u:username file.txt

# Avlägsna alla ACL:er
setfacl -b file.txt
```

### Krav för ACL

```bash
# Filsystemet måste stödja ACL (ofta standard i moderna system)
# Kontrollera monteringsalternativ
mount | grep " acl"

# Om inte monterat med ACL, lägg till i /etc/fstab:
# /dev/sda1 /mnt/data ext4 defaults,acl 0 2
```

## Filattribut (chattr och lsattr)

Utöver behörigheter kan filer ha attribut som ger extra säkerhet eller funktionalitet.

### lsattr - Visa attribut

```bash
# Visa attribut för fil
lsattr file.txt
# ----i--------e-- file.txt

# Rekursivt
lsattr -R directory/
```

### chattr - Ändra attribut

```bash
# Immutable (+i) - Filen kan INTE ändras, raderas eller byta namn (inte ens root)
sudo chattr +i important_file.txt
# Nu kan ingen ändra filen förrän attributet avlägsnas
sudo chattr -i important_file.txt  # Avlägsna immutable

# Append-only (+a) - Kan endast lägga till data i slutet, inte ändra eller radera
sudo chattr +a logfile.txt
echo "new line" >> logfile.txt  # OK
rm logfile.txt  # Misslyckas
sudo chattr -a logfile.txt  # Avlägsna append-only

# No dump (+d) - Filen ska inte säkerhetskopieras av backup-verktyg
sudo chattr +d backup_file.tar.gz
```

### Vanliga attribut

- **i (immutable)**: Filen är oföränderlig
- **a (append-only)**: Kan endast lägga till data
- **d (no dump)**: Hoppa över vid säkerhetskopiering
- **e (extent)**: Extent-baserad allokering (standard på ext4)

**Notera**: Endast root kan ändra de flesta attribut (särskilt +i och +a).

## Principle of Least Privilege (PoLP)

Principle of Least Privilege innebär att användare och processer endast ska ha minimala behörigheter de behöver för att utföra sina uppgifter.

### Praktiska exempel

```bash
# ❌ Felaktigt: Tilldela alla fullständiga behörigheter
chmod 777 /data

# ✅ Korrekt: Tilldela endast nödvändiga behörigheter
chmod 755 /data  # Ägare kan allt, andra kan läsa och exekvera

# ❌ Felaktigt: Exekvera allt som root
sudo ./script.sh

# ✅ Korrekt: Använd capabilities eller sudo för specifika kommandon
sudo setcap cap_net_bind_service=+ep /usr/bin/myapp
```

### Säkerhetsfördelar

- **Begränsar skadeverkningar**: Om en process komprometteras kan den endast göra begränsade saker
- **Förbättrar spårbarhet**: Enklare att se vem som gjorde vad
- **Minskar risk för misstag**: Mindre risk att oavsiktligt ändra eller radera viktiga filer

## Praktiska säkerhetsexempel

### Skydda privata nycklar

```bash
# SSH private key
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh
```

### Webbserver-kataloger

```bash
# Webbrot
sudo chown -R www-data:www-data /var/www/html
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

### Delade kataloger med SGID

```bash
# Skapa delad katalog där alla filer får samma grupp
sudo mkdir /shared
sudo chgrp developers /shared
sudo chmod 2775 /shared  # 2 = SGID
# Nya filer får automatiskt gruppen 'developers'
```

### Säkerhetschecklista

```bash
# Kontrollera filer med SUID/SGID
find / -type f -perm /4000 2>/dev/null  # SUID
find / -type f -perm /2000 2>/dev/null  # SGID

# Kontrollera world-writable filer
find / -type f -perm -002 2>/dev/null

# Kontrollera filer utan ägare
find / -nouser -o -nogroup 2>/dev/null
```

## Viktiga lärdomar

- **Behörighetsmatris**: 4 (läs) + 2 (skriv) + 1 (exekvera) = 7
- **Kataloger kräver exekvera (x)** för att kunna navigeras med `cd`
- **umask** bestämmer standardbehörigheter: Filer (666-umask), Kataloger (777-umask)
- **Sticky Bit**: Används i /tmp - endast ägaren kan radera
- **SUID/SGID**: Exekvera program med ägarens/gruppens behörigheter
- **/etc/passwd vs /etc/shadow**: Grundinformation vs krypterade lösenord
- **ACL** möjliggör behörigheter till flera specifika användare/grupper
- **chattr +i** gör filer oföränderliga (immutable), även för root
- **chattr +a** gör filer append-only (kan endast lägga till data)
- **stat** visar mer omfattande filinformation än `ls -l`
- **su** kräver målanvändarens lösenord, **sudo** kräver eget lösenord
- **Principle of Least Privilege**: Tilldela endast nödvändiga behörigheter
- **Capabilities**: Tilldela specifika root-förmågor utan att vara root

"""
}
