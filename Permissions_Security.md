# Advanced Permissions & Security

Fokus: Skydda data och hantera identiteter

## Permission Matrix

Linux-filbehörigheter använder en numerisk kod baserad på tre bitar:

- **Read (4)**: Läsa filer, lista kataloger
- **Write (2)**: Skriva/modifiera filer, skapa/radera i kataloger
- **Execute (1)**: Köra filer, gå in i kataloger

Behörigheter ges till tre grupper:

- **User (u)**: Ägaren av filen
- **Group (g)**: Medlemmar i filens grupp
- **Others (o)**: Alla andra

```bash
# Exempel: rwxr-xr--
# User:   rwx = 4+2+1 = 7 (read, write, execute)
# Group:  r-x = 4+0+1 = 5 (read, execute)
# Others: r-- = 4+0+0 = 4 (read only)

chmod 754 filename
# User: read, write, execute
# Group: read, execute
# Others: read only
```

### Numeriska vs Symboliska behörigheter

```bash
# Numerisk (octal)
chmod 755 script.sh
chmod 644 file.txt
chmod 600 private.key

# Symbolisk
chmod u+x script.sh        # Lägg till execute för user
chmod g-w file.txt         # Ta bort write för group
chmod o+r file.txt         # Lägg till read för others
chmod a+x script.sh        # Lägg till execute för alla (a=all)
```

### Vad händer om en katalog får rättigheten 644?

**Viktigt**: En katalog behöver execute-rättighet (x) för att man ska kunna gå in i den med `cd`.

```bash
# Fel: Katalog utan execute
chmod 644 directory/
# Du kan lista filerna (read), men INTE gå in (cd directory/ misslyckas)

# Rätt: Katalog med execute
chmod 755 directory/
# Nu kan du både lista och gå in i katalogen
```

**Regel**: För kataloger behöver du minst r-x (5) för att kunna navigera in i dem.

## Umask och Standardrättigheter

### Vad är umask?

umask (user file creation mask) bestämmer standardrättigheterna för nya filer och mappar.

```bash
# Visa nuvarande umask
umask
# 0022

# Förklaring av 0022:
# 0 = special bits (SUID, SGID, Sticky)
# 022 = mask för user, group, others
```

### Hur umask fungerar

Umask subtraheras från standardrättigheterna:

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

# 0002 - Mer öppet (group kan skriva)
umask 0002
# Filer: 664, Kataloger: 775

# 0077 - Mycket privat (endast user)
umask 0077
# Filer: 600, Kataloger: 700
```

### Sätt umask permanent

```bash
# För användare: lägg till i ~/.bashrc eller ~/.profile
umask 0022

# Systemvida: /etc/profile eller /etc/bash.bashrc
```

**Viktigt**: Linux sätter aldrig execute (x) på filer som standard, även om umask tillåter det.

## Special Bits

### Sticky Bit (används i /tmp)

Sticky bit säkerställer att bara filägaren kan radera sina egna filer, även om katalogen är skrivbar för alla.

```bash
# Sätt sticky bit
chmod +t /tmp
# eller
chmod 1777 /tmp

# Kontrollera
ls -ld /tmp
# drwxrwxrwt  # 't' i slutet = sticky bit
```

**Användning**: /tmp - alla kan skriva, men bara ägaren kan radera sina filer.

### SUID (Set User ID)

När en fil med SUID körs, körs den med filägarens behörigheter, inte användarens.

```bash
# Exempel: passwd-kommandot
ls -l /usr/bin/passwd
# -rwsr-xr-x  # 's' i user-position = SUID

# Sätt SUID
chmod u+s program
chmod 4755 program  # 4 = SUID bit
```

**Säkerhetsvarning**: SUID kan vara farligt om missbrukat!

### SGID (Set Group ID)

När en fil med SGID körs, körs den med filens gruppbehörigheter.

```bash
# Sätt SGID
chmod g+s program
chmod 2755 program  # 2 = SGID bit

# För kataloger: nya filer får samma grupp
chmod g+s /shared/directory
```

## User Management

### Skillnaden mellan /etc/passwd och /etc/shadow

**/etc/passwd**: Innehåller grundläggande användarinformation (läsbar för alla)

```bash
cat /etc/passwd
# Format: username:x:UID:GID:comment:home:shell
# 'x' betyder att lösenordet finns i /etc/shadow
```

**/etc/shadow**: Innehåller krypterade lösenord (endast root kan läsa)

```bash
sudo cat /etc/shadow
# Format: username:encrypted_password:last_change:min:max:warn:inactive:expire
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
# Format: groupname:password:GID:members
# docker:x:999:user1,user2
```

### /etc/login.defs

Systemvida inställningar för användarhantering:

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

**su (switch user)**: Byter till en annan användare (kräver lösenord för målanvändaren)

```bash
# Byta till root (kräver root-lösenord)
su -

# Byta till annan användare
su - username

# Byta utan att ladda miljövariabler
su username
```

**sudo (superuser do)**: Kör kommandon med root-rättigheter (kräver ditt eget lösenord)

```bash
# Kör kommando som root
sudo command

# Byta till root med sudo
sudo -i
sudo -s

# Kör som annan användare
sudo -u username command
```

**Skillnad**: su kräver målanvändarens lösenord, sudo kräver ditt eget lösenord och konfiguration i /etc/sudoers.

### stat - Detaljerad filinformation

stat visar mer detaljerad information än `ls -l`:

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

# Visa bara specifik information
stat -c "%a %n" file.txt  # Numeriska rättigheter
stat -c "%U:%G" file.txt  # Ägare:grupp
stat -c "%y" file.txt     # Modifieringstid
```

### Ownership: Rekursiv användning av chown och chmod -R

```bash
# Ändra ägare rekursivt
sudo chown -R user:group /path/to/directory

# Ändra behörigheter rekursivt
chmod -R 755 /path/to/directory

# Kombinera
sudo chown -R www-data:www-data /var/www
sudo chmod -R 755 /var/www
```

**Varning**: -R är kraftfullt - kontrollera sökvägen noga!

```bash
# Säker metod: testa först med find
find /path/to/dir -type f -exec chmod 644 {} \;
find /path/to/dir -type d -exec chmod 755 {} \;
```

## Capabilities

Capabilities låter processer ha root-liknande krafter utan att vara root. Exempel: binda port 80 (som normalt kräver root).

```bash
# Visa capabilities för ett program
getcap /usr/bin/ping

# Sätt capability
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

# Kör program med capabilities
sudo capsh --caps="cap_net_bind_service+ep" -- -c "./server"
```

## ACL (Access Control Lists)

ACL låter dig ge specifika rättigheter till specifika användare/grupper utöver standard Owner/Group/Others.

### Begränsning med klassiska rättigheter

Klassiska Linux-rättigheter kan bara ge rättigheter till:

- En användare (owner)
- En grupp (group)
- Alla andra (others)

**Problem**: Om du vill ge rättigheter till flera specifika användare eller grupper behöver du ACL.

### setfacl - Sätt ACL

```bash
# Ge en specifik användare läsrättighet
setfacl -m u:username:r file.txt

# Ge en grupp skrivrättighet
setfacl -m g:developers:w file.txt

# Kombinera flera rättigheter
setfacl -m u:alice:rwx file.txt
setfacl -m g:team:r-x file.txt

# Rekursivt för kataloger
setfacl -R -m u:username:rwx /path/to/directory
```

### getfacl - Visa ACL

```bash
# Visa ACL för en fil
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

### Ta bort ACL

```bash
# Ta bort specifik ACL-post
setfacl -x u:username file.txt

# Ta bort alla ACL:er
setfacl -b file.txt
```

### Krav för ACL

```bash
# Filsystemet måste stödja ACL (ofta default i moderna system)
# Kontrollera mount-options
mount | grep " acl"

# Om inte monterat med ACL, lägg till i /etc/fstab:
# /dev/sda1 /mnt/data ext4 defaults,acl 0 2
```

## Fil-attribut (chattr och lsattr)

Förutom rättigheter kan filer ha attribut som ger extra säkerhet eller funktionalitet.

### lsattr - Visa attribut

```bash
# Visa attribut för en fil
lsattr file.txt
# ----i--------e-- file.txt

# Rekursivt
lsattr -R directory/
```

### chattr - Ändra attribut

```bash
# Immutable (+i) - Filen kan INTE ändras, raderas eller döpas om (inte ens root)
sudo chattr +i important_file.txt
# Nu kan ingen ändra filen förrän attributet tas bort
sudo chattr -i important_file.txt  # Ta bort immutable

# Append-only (+a) - Kan bara lägga till data i slutet, inte ändra eller radera
sudo chattr +a logfile.txt
echo "new line" >> logfile.txt  # OK
rm logfile.txt  # Misslyckas
sudo chattr -a logfile.txt  # Ta bort append-only

# No dump (+d) - Filen ska inte dumpas av backup-verktyg
sudo chattr +d backup_file.tar.gz
```

### Vanliga attribut

- **i (immutable)**: Filen är oföränderlig
- **a (append-only)**: Kan bara lägga till data
- **d (no dump)**: Hoppa över vid backup
- **e (extent)**: Extent-baserad allokering (standard på ext4)

**Viktigt**: Endast root kan ändra de flesta attribut (särskilt +i och +a).

## Principle of Least Privilege (PoLP)

Principle of Least Privilege innebär att användare och processer endast ska ha de minsta rättigheter de behöver för att utföra sitt jobb.

### Praktiska exempel

```bash
# ❌ Dåligt: Ge alla fullständiga rättigheter
chmod 777 /data

# ✅ Bra: Ge endast nödvändiga rättigheter
chmod 755 /data  # Ägare kan allt, andra kan läsa och köra

# ❌ Dåligt: Kör allt som root
sudo ./script.sh

# ✅ Bra: Använd capabilities eller sudo för specifika kommandon
sudo setcap cap_net_bind_service=+ep /usr/bin/myapp
```

### Säkerhetsfördelar

- **Begränsar skadeverkningar**: Om en process komprometteras, kan den bara göra begränsade saker
- **Förbättrar spårbarhet**: Lättare att se vem som gjorde vad
- **Minskar risk för misstag**: Mindre risk att oavsiktligt ändra eller radera viktiga filer

## Praktiska säkerhetsexempel

### Skydda privata nycklar

```bash
# SSH private key
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh
```

### Web server directories

```bash
# Web root
sudo chown -R www-data:www-data /var/www/html
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

### Shared directories med SGID

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

## Viktiga takeaways

- **Permission Matrix**: 4 (read) + 2 (write) + 1 (execute) = 7
- **Kataloger behöver execute (x)** för att man ska kunna gå in i dem med `cd`
- **umask** bestämmer standardrättigheter: Filer (666-umask), Kataloger (777-umask)
- **Sticky Bit**: Används i /tmp - bara ägaren kan radera
- **SUID/SGID**: Kör program med ägarens/gruppens behörigheter
- **/etc/passwd vs /etc/shadow**: Grundinfo vs krypterade lösenord
- **ACL** låter dig ge rättigheter till flera specifika användare/grupper
- **chattr +i** gör filer oföränderliga (immutable), även för root
- **chattr +a** gör filer append-only (kan bara lägga till data)
- **stat** visar mer detaljerad filinformation än `ls -l`
- **su** kräver målanvändarens lösenord, **sudo** kräver ditt eget lösenord
- **Principle of Least Privilege**: Ge endast nödvändiga rättigheter
- **Capabilities**: Ge specifika root-krafter utan att vara root
