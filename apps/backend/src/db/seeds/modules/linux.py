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
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Filesystem Hierarchy Standard (FHS)

## Varför behöver du kunna detta?

Som DevOps-ingenjör lever du i terminalen. Du måste veta:

- **Var konfigurationer sparas** så du kan ändra inställningar
- **Var loggar hamnar** så du kan felsöka
- **Var program installeras** så du kan hantera dependencies
- **Var användare har sina filer** så du kan sätta rätt permissions

---

## Så fungerar Linux filstruktur

Alla Linux-distributioner följer något som kallas **FHS** - Filesystem Hierarchy Standard. Det betyder att oavsett om du kör Ubuntu, CentOS eller Debian så ligger saker på samma ställen. Detta gör livet mycket enklare när du hoppar mellan olika servrar!

---

## /bin - Grundläggande kommandon

Här ligger de absolut viktigaste kommandona - de som måste fungera även om resten av systemet har problem. Se det som överlevnadsverktyg.

```bash
ls /bin
# Visar innehållet i /bin-katalogen
# Här hittar du grundläggande kommandon som ls, cp, mv, cat, echo
# Dessa finns alltid tillgängliga, oavsett vad som hänt med systemet

which cp
# /bin/cp
# which-kommandot berättar var ett program finns
# Här ser vi att cp (copy) ligger i /bin
# Det är därför cp alltid fungerar - /bin laddas först av systemet
```

Se /bin som första-hjälpen-lådan - den innehåller bara det mest nödvändiga, men det räcker för att överleva!

---

## /etc - Alla inställningar

Den här katalogen är hjärtat av systemkonfigurationen. Varje gång du vill ändra hur ett program eller tjänst beter sig, är det hit du går.

```bash
cat /etc/hostname
# Visar serverns namn
# Denna fil innehåller bara en rad - datorns namn
# Om du vill byta namn på servern, ändrar du här

ls /etc/nginx/
# Visar nginx konfigurationsfiler
# nginx.conf är huvudfilen
# sites-available/ innehåller webbplatskonfigurationer
# Varje webbserver, databas, och tjänst har sina config-filer i /etc

head -5 /etc/passwd
# Visar de första 5 raderna i passwd-filen
# Här listas alla användare i systemet
# Varje rad = en användare med info om hemkatalog, shell, etc.
```

**Gyllene regeln:** Innan du rör något i /etc - ta backup!

```bash
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
# Kopierar nginx.conf till nginx.conf.bak
# .bak är en vanlig konvention för backup-filer
# Om något går fel kan du återställa med: sudo cp nginx.conf.bak nginx.conf
# Det tar 2 sekunder att göra backup, men kan spara timmar av felsökning!
```

Se /etc som kontrollrummet - alla spakar och knappar finns här, men tryck inte på något utan att veta vad det gör!

---

## /var - Data som ändras

Medan /etc innehåller statiska inställningar, innehåller /var saker som ständigt förändras - loggar som växer, databaser som uppdateras, mail som kommer in.

```bash
ls /var/log/
# Listar alla loggfiler och loggkataloger
# syslog eller messages - systemhändelser
# auth.log - inloggningsförsök
# nginx/ eller apache2/ - webbserverloggar
# Här börjar du ALLTID när något gått fel!

tail -20 /var/log/syslog
# Visar de 20 senaste raderna i systemloggen
# tail läser från slutet av filen (de nyaste händelserna)
# -20 betyder 20 rader
# Perfekt för att snabbt se vad som hänt nyligen

watch -n 2 'ls -lh /var/log/*.log'
# watch kör ett kommando upprepat
# -n 2 betyder var 2:a sekund
# Här ser vi hur loggfilerna växer i realtid
# Användbart för att upptäcka loggar som växer för fort
```

Se /var som aktivitetsloggen - allt som händer i systemet dokumenteras här. När något går fel är detta första stället att kolla!

---

## /usr - Installerade program

De flesta program du installerar hamnar här. Det är som "Program Files" på Windows, fast mer organiserat.

```bash
ls /usr/bin/ | wc -l
# Räknar hur många program som finns i /usr/bin
# wc -l räknar antal rader (en rad per program)
# Du kommer se hundratals eller tusentals program
# Allt från git till python till docker

which python3
# /usr/bin/python3
# De flesta program du installerar med apt/yum hamnar här
# Till skillnad från /bin som har grundkommandon,
# har /usr/bin användarprogram som installerats efteråt

ls /usr/local/bin/
# Här lägger du egna scripts och program
# Pakethanteraren (apt/yum) rör aldrig denna katalog
# Perfekt för deploy-scripts, cronjobs, och custom tools
# Om du vill att alla användare ska kunna köra ditt script - lägg det här
```

---

## /home - Användarnas utrymme

Varje användare får sin egen katalog under /home. Det är deras privata utrymme för filer, inställningar och scripts.

```bash
ls -la /home/
# Visar alla användarkataloger
# -la visar även dolda filer och permissions
# Varje användare har en katalog med sitt användarnamn
# Permissions är oftast 755 eller 700 (bara ägaren kan läsa)

ls -la ~/
# ~ är en genväg till din egen hemkatalog
# Samma som /home/ditt-användarnamn
# Här ser du .bashrc, .ssh/, och andra personliga filer
# Filer som börjar med . (punkt) är dolda

cat ~/.bashrc | head -20
# .bashrc körs varje gång du öppnar en terminal
# Här lägger du aliases, miljövariabler, och anpassningar
# Exempelvis: alias ll='ls -la' för att skapa genvägar
# Ändringar kräver ny terminal eller 'source ~/.bashrc'
```

---

## /tmp - Temporära filer

Skräphantering! Hit går filer som bara behövs tillfälligt. Systemet rensar denna katalog automatiskt.

```bash
ls /tmp/
# Visar temporära filer
# Program skapar temp-filer här när de kör
# Allt kan försvinna vid omstart - lita ALDRIG på att saker finns kvar här

mktemp
# /tmp/tmp.Xf4kL2
# Skapar en unik temporär fil och skriver ut sökvägen
# Använd detta i scripts för säker temp-hantering
# Filen får ett slumpmässigt namn så det inte krockar med andra
```

**Varning:** Spara aldrig viktig data i /tmp - det kan raderas när som helst!

---

## /opt - Tredjepartsprogram

Stora program som inte passar in i standardstrukturen hamnar ofta här - saker som kommer som ett komplett paket.

```bash
ls /opt/
# Visar installerade tredjepartsprogram
# Vanliga exempel: /opt/google/chrome, /opt/containerd
# Varje program får sin helt egna mapp
# Fördelen: lätt att ta bort - bara radera mappen

du -sh /opt/*
# Visar hur mycket utrymme varje program tar
# du = disk usage
# -s = summering per katalog
# -h = human-readable (MB, GB istället för bytes)
```

---

## Key Takeaways

1. **/etc** = konfiguration - hit går du för att ändra inställningar
2. **/var/log** = loggar - hit går du för att felsöka
3. **/usr/local/bin** = egna scripts - hit lägger du dina verktyg
4. **/home** = användarfiler - varje användare har sin katalog
5. **Ta alltid backup** innan du ändrar filer i /etc!
""",
        },
        {
            "title": 'Mount Points och Device Files',
            "slug": 'mount-points-device-files',
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 65,
            "content": """# Mount Points och Device Files

## Varför behöver du kunna detta?

I Linux är allt en fil - även hårddiskar, USB-minnen och nätverkslagringar. För att använda dem måste du "mounta" dem till en plats i filsystemet. Som DevOps behöver du:

- **Ansluta externa diskar** för backup och lagring
- **Förstå /dev-katalogen** där alla enheter finns
- **Konfigurera automatisk mount** så diskar fungerar efter reboot
- **Felsöka "disk full"** genom att förstå var saker är mountade

---

## Så fungerar mounting

När du kopplar in en disk i Linux dyker den upp som en fil i `/dev` - men du kan inte läsa den direkt. Du måste "mounta" den till en katalog. Tänk på det som att koppla in en extern hårddisk och ge den en bokstav på Windows - fast i Linux väljer du en katalog istället.

```bash
lsblk
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   100G  0 disk
# ├─sda1   8:1    0    99G  0 part /
# └─sda2   8:2    0     1G  0 part [SWAP]
# sdb      8:16   0   500G  0 disk
# └─sdb1   8:17   0   500G  0 part
#
# lsblk listar alla blockenheter (diskar)
# sda är första disken, sdb är andra
# sda1 är första partitionen på sda
# MOUNTPOINT visar var disken är ansluten i filsystemet
# sdb1 har ingen mountpoint - den är inte ansluten ännu!
```

---

## /dev - Alla enheter

`/dev` är en speciell katalog där Linux representerar all hårdvara som filer. Här hittar du diskar, tangentbord, mus, och till och med slumptalsgeneratorer.

```bash
ls /dev/sd*
# /dev/sda  /dev/sda1  /dev/sda2  /dev/sdb  /dev/sdb1
# sd = SCSI/SATA disk
# sda = första disken, sdb = andra disken
# sda1 = första partitionen på sda
# Dessa filer representerar fysiska diskar

ls /dev/nvme*
# /dev/nvme0n1  /dev/nvme0n1p1  /dev/nvme0n1p2
# nvme = NVMe SSD-diskar (snabbare moderna diskar)
# nvme0n1 = första NVMe-disken
# p1, p2 = partitioner

cat /dev/null
# (ingen output)
# /dev/null är en "svart hål" - allt du skriver hit försvinner
# Användbart för att tysta output: command > /dev/null

head -c 16 /dev/urandom | xxd
# Visar 16 slumpmässiga bytes
# /dev/urandom genererar slumptal
# Används för att skapa lösenord, nycklar, etc.
```

Tänk på /dev som hårdvarans telefonbok - varje enhet har en "fil" du kan prata med!

---

## Mounta en disk

När du har identifierat en disk i /dev måste du mounta den för att kunna använda filerna.

```bash
sudo mkdir /mnt/external
# Skapar en tom katalog som mount-punkt
# /mnt är standardplatsen för temporära mounts
# Du kan välja vilket namn du vill

sudo mount /dev/sdb1 /mnt/external
# Ansluter partitionen sdb1 till /mnt/external
# Nu kan du komma åt filerna via /mnt/external
# Allt du sparar här hamnar på den externa disken

ls /mnt/external
# Visar innehållet på den mountade disken
# Om disken var tom ser du inget
# Om den hade filer ser du dem nu

df -h /mnt/external
# Visar hur mycket utrymme som finns på disken
# -h = human-readable (GB istället för bytes)
# Du ser total storlek, använt, och ledigt
```

---

## Unmounta säkert

Innan du kopplar bort en disk måste du "unmounta" den - annars riskerar du datakorruption.

```bash
sudo umount /mnt/external
# Kopplar bort disken säkert
# OBS! Det heter umount, INTE unmount (vanligt misstag!)
# Se till att ingen använder disken först

# Om du får "target is busy":
lsof /mnt/external
# Visar vilka processer som använder disken
# Du måste stänga dessa innan du kan unmounta

fuser -m /mnt/external
# Alternativt sätt att se vilka processer som använder disken
# Visar process-ID:n som har filer öppna

sudo umount -l /mnt/external
# -l = lazy unmount
# Kopplar bort så fort ingen använder den längre
# Använd bara om vanlig umount inte fungerar
```

---

## Automatisk mount med /etc/fstab

Om du vill att disken ska monteras automatiskt vid boot måste du lägga till den i `/etc/fstab`.

```bash
blkid /dev/sdb1
# /dev/sdb1: UUID="abc-123-def" TYPE="ext4"
# blkid visar diskens unika ID (UUID)
# Använd UUID istället för /dev/sdb1 i fstab
# UUID ändras aldrig, men /dev/sdb kan bli /dev/sdc om du lägger till diskar

cat /etc/fstab
# <file system>  <mount point>  <type>  <options>  <dump>  <pass>
# UUID=abc-123   /mnt/external  ext4    defaults   0       2
#
# file system = vilken disk (använd UUID!)
# mount point = var den ska monteras
# type = filsystemstyp (ext4, xfs, ntfs, etc.)
# options = mount-inställningar
# dump = backup (oftast 0)
# pass = filsystemskontroll vid boot (1 för root, 2 för andra, 0 för att skippa)

sudo mount -a
# Monterar allt i fstab som inte redan är monterat
# Bra för att testa att fstab är korrekt
# Om detta misslyckas, kommer servern inte boota ordentligt!
```

**Varning:** Ett fel i fstab kan göra att servern inte startar! Testa alltid med `mount -a` innan du rebootar.

---

## Vanliga mount-typer

```bash
# NFS - nätverkslagring
sudo mount -t nfs server:/share /mnt/nfs
# -t nfs = filsystemstyp är NFS
# server:/share = NFS-serverns adress och delning
# Kräver att nfs-common är installerat

# CIFS/SMB - Windows-delningar
sudo mount -t cifs //server/share /mnt/smb -o user=admin
# -t cifs = Windows/Samba-filsystem
# -o user=admin = anslut som användaren "admin"
# Du blir tillfrågad om lösenord

# tmpfs - RAM-disk
sudo mount -t tmpfs -o size=1G tmpfs /mnt/ramdisk
# Skapar en disk i RAM-minnet
# Supersnabbt men försvinner vid reboot
# Perfekt för temporära filer som behöver vara snabba
```

---

## Key Takeaways

1. **lsblk** = se alla diskar och var de är monterade
2. **mount/umount** = anslut och koppla bort diskar (OBS: umount, inte unmount!)
3. **/etc/fstab** = automatisk mount vid boot - testa alltid med `mount -a` först
4. **UUID** = använd alltid UUID i fstab, inte /dev/sdX
5. **Unmounta innan du kopplar bort** = annars riskerar du datakorruption
""",
        },
        {
            "title": 'File Permissions',
            "slug": 'file-permissions',
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 75,
            "content": """# File Permissions

## Varför behöver du kunna detta?

Permissions avgör vem som kan göra vad med en fil. Som DevOps stöter du på permission-problem dagligen:

- **Deploy-scripts som inte kan köras** - saknar execute-permission
- **Webbservrar som inte kan läsa filer** - fel ägare
- **SSH-nycklar som inte accepteras** - för öppna permissions
- **Config-filer som inte kan ändras** - saknar write-permission

---

## Så fungerar permissions

Varje fil i Linux har tre typer av permissions för tre typer av användare. Tänk på det som ett säkerhetssystem med tre nivåer.

```bash
ls -l myfile.txt
# -rw-r--r-- 1 john developers 1024 Dec 7 10:30 myfile.txt
#
# Första tecknet: filtyp (- = fil, d = katalog, l = länk)
# Nästa 9 tecken: permissions i tre grupper
#   rw-  = owner (john) kan läsa och skriva
#   r--  = group (developers) kan bara läsa
#   r--  = others (alla andra) kan bara läsa
# john = ägare (user/owner)
# developers = grupp (group)
```

---

## Permission-bokstäverna

```bash
# r = read (läsa)
# w = write (skriva/ändra)
# x = execute (köra/öppna katalog)
# - = ingen permission

ls -la /etc/passwd
# -rw-r--r-- 1 root root 2847 Dec 1 12:00 /etc/passwd
# Alla kan LÄSA filen (viktig för systemet)
# Bara root kan ÄNDRA filen (säkerhet)
# Ingen behöver KÖRA filen (det är inte ett program)

ls -la /usr/bin/ls
# -rwxr-xr-x 1 root root 142144 Nov 5 2023 /usr/bin/ls
# Detta är ett program, därför finns x (execute)
# Alla kan köra ls-kommandot
# Bara root kan ändra programmet
```

---

## Ändra permissions med chmod

chmod (change mode) ändrar permissions på filer och kataloger.

```bash
chmod u+x script.sh
# u = user (ägaren)
# + = lägg till
# x = execute-permission
# Nu kan ägaren köra scriptet

chmod g-w file.txt
# g = group
# - = ta bort
# w = write-permission
# Gruppen kan inte längre ändra filen

chmod o=r document.txt
# o = others (alla andra)
# = = sätt exakt dessa permissions
# r = bara läsa
# Andra kan bara läsa, inget annat

chmod a+r public.html
# a = all (alla: user, group, others)
# Alla får läsa filen
```

---

## Oktala permissions (siffror)

Istället för bokstäver kan du använda siffror - detta är vanligast i scripts och dokumentation.

```bash
# Varje siffra är summan av:
# r = 4
# w = 2
# x = 1

# 7 = 4+2+1 = rwx (alla permissions)
# 6 = 4+2   = rw- (läsa och skriva)
# 5 = 4+1   = r-x (läsa och köra)
# 4 = 4     = r-- (bara läsa)
# 0 = 0     = --- (inga permissions)

chmod 755 script.sh
# 7 = rwx för owner (full kontroll)
# 5 = r-x för group (läsa och köra)
# 5 = r-x för others (läsa och köra)
# Perfekt för scripts som alla ska kunna köra

chmod 644 config.txt
# 6 = rw- för owner (läsa och skriva)
# 4 = r-- för group (bara läsa)
# 4 = r-- för others (bara läsa)
# Standard för vanliga filer

chmod 600 ~/.ssh/id_rsa
# 6 = rw- för owner (läsa och skriva)
# 0 = --- för group (ingenting)
# 0 = --- för others (ingenting)
# OBLIGATORISKT för SSH-nycklar! SSH vägrar annars.
```

---

## Ändra ägare med chown

chown (change owner) ändrar vem som äger en fil.

```bash
sudo chown nginx /var/www/html/index.html
# Ändrar ägaren till nginx
# Bara root kan ändra ägare (därför sudo)

sudo chown nginx:www-data /var/www/html/index.html
# Ändrar BÅDE ägare (nginx) OCH grupp (www-data)
# : separerar user och group

sudo chown -R deploy:deploy /var/www/app/
# -R = recursive (alla filer och mappar under)
# Ändrar ägare på ALLT under /var/www/app/
# Vanligt vid deployment-setup
```

---

## Vanliga permission-mönster

```bash
# För scripts och körbara filer
chmod 755 deploy.sh
# Owner: full kontroll, Alla andra: kan köra

# För config-filer
chmod 644 nginx.conf
# Owner: kan ändra, Alla andra: kan bara läsa

# För hemliga filer (nycklar, lösenord)
chmod 600 secrets.env
# BARA owner kan läsa och skriva

# För kataloger som alla ska kunna lista
chmod 755 /var/www/
# Alla kan gå in och se innehållet

# För privata kataloger
chmod 700 ~/.ssh/
# BARA ägaren kan gå in
```

---

## Felsökning

```bash
# "Permission denied" när du kör ett script
ls -la script.sh
# Kolla om x (execute) finns
chmod +x script.sh
# Lägg till execute-permission

# SSH-nyckel "permissions too open"
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh/
# SSH kräver strikt permissions

# Webbserver kan inte läsa filer
ls -la /var/www/html/
# Kolla att www-data (eller nginx) kan läsa
sudo chown -R www-data:www-data /var/www/html/
```

---

## Key Takeaways

1. **rwx** = read (4), write (2), execute (1) - lär dig siffrorna!
2. **755** = för scripts och kataloger som alla ska kunna använda
3. **644** = för config-filer som bara ägaren ska ändra
4. **600** = för hemligheter - SSH-nycklar, lösenord, tokens
5. **chown -R** = ändra ägare rekursivt - vanligt vid deploy
""",
        },
        {
            "title": 'Inodes, Hard Links och Symbolic Links',
            "slug": 'inodes-links',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Inodes, Hard Links och Symbolic Links

## Varför behöver du kunna detta?

Länkar är fundamentala för hur Linux fungerar. Du stöter på dem överallt:

- **Zero-downtime deploys** använder symlinks för att byta version
- **"Disk full" trots ledigt utrymme** kan bero på slut på inodes
- **Raderade filer som fortfarande tar plats** beror på hur inodes fungerar
- **Delade config-filer** mellan miljöer använder ofta länkar

---

## Vad är en inode?

Varje fil i Linux har en inode - en datastruktur som innehåller all metadata om filen. Tänk på det som ett "ID-kort" för filen.

```bash
ls -i myfile.txt
# 12345678 myfile.txt
#
# 12345678 är filens inode-nummer
# Detta nummer är unikt inom filsystemet
# Inode-numret är filens verkliga identitet - filnamnet är bara en etikett

stat myfile.txt
# File: myfile.txt
# Size: 1024       Blocks: 8          IO Block: 4096   regular file
# Device: 801h/2049d      Inode: 12345678    Links: 1
# Access: (0644/-rw-r--r--)  Uid: ( 1000/john)   Gid: ( 1000/john)
# Access: 2024-12-07 10:00:00
# Modify: 2024-12-07 09:30:00
# Change: 2024-12-07 09:30:00
#
# stat visar ALLT om filen
# Inode: 12345678 - filens unika nummer
# Links: 1 - hur många namn som pekar på denna inode
# Access/Modify/Change - tre olika timestamps!
```

---

## Hard Links

En hard link är ett extra namn som pekar på samma inode. Tänk på det som att ge samma person ett smeknamn - det är fortfarande samma person.

```bash
echo "Hello World" > original.txt
# Skapar en fil med innehållet "Hello World"

ln original.txt hardlink.txt
# Skapar en hard link
# Nu finns det TVÅ namn som pekar på SAMMA inode
# Ingen av dem är "originalet" - de är likvärdiga

ls -li original.txt hardlink.txt
# 12345678 -rw-r--r-- 2 john john 12 Dec 7 10:00 original.txt
# 12345678 -rw-r--r-- 2 john john 12 Dec 7 10:00 hardlink.txt
#
# SAMMA inode-nummer (12345678)!
# Links: 2 - nu finns två namn för denna inode
# Båda filerna är identiska och delar samma data

rm original.txt
# Raderar BARA namnet "original.txt"
# Datan finns fortfarande kvar!

cat hardlink.txt
# Hello World
# Innehållet finns kvar via hardlink.txt
# Datan raderas först när ALLA hard links är borta
```

---

## Symbolic Links (Symlinks)

En symlink är en pekare till ett filnamn - inte till inoden. Tänk på det som en genväg på skrivbordet.

```bash
ln -s /var/log/syslog loggen
# Skapar en symlink som heter "loggen"
# -s = symbolic (annars blir det hard link)
# loggen pekar på /var/log/syslog

ls -la loggen
# lrwxrwxrwx 1 john john 15 Dec 7 10:00 loggen -> /var/log/syslog
#
# l i början = detta är en länk
# -> visar vart länken pekar
# Storleken (15) är längden på sökvägen, inte filen

cat loggen
# (visar innehållet i /var/log/syslog)
# Linux följer länken automatiskt

rm /var/log/syslog
# Nu är länken "broken" - målet finns inte längre

cat loggen
# cat: loggen: No such file or directory
# Symlinken pekar på ett namn som inte längre finns
```

---

## Skillnaden i praktiken

```bash
# Skapa testfil
echo "Test data" > source.txt

# Skapa båda typer av länkar
ln source.txt hard_copy
ln -s source.txt soft_copy

# Se skillnaden
ls -li source.txt hard_copy soft_copy
# 12345 -rw-r--r-- 2 john john 10 Dec 7 source.txt
# 12345 -rw-r--r-- 2 john john 10 Dec 7 hard_copy    <- SAMMA inode!
# 67890 lrwxrwxrwx 1 john john 10 Dec 7 soft_copy -> source.txt  <- ANNAN inode

# Radera originalet
rm source.txt

cat hard_copy
# Test data
# FUNGERAR! Hard link har fortfarande datan

cat soft_copy
# cat: soft_copy: No such file or directory
# FUNKAR INTE! Symlink pekar på ett namn som inte finns
```

---

## Inode Exhaustion

Varje filsystem har ett begränsat antal inodes. Du kan ha ledigt diskutrymme men ändå inte kunna skapa filer!

```bash
df -i
# Filesystem      Inodes   IUsed   IFree IUse% Mounted on
# /dev/sda1     6553600 1234567 5319033   19% /
#
# df -i visar inode-användning
# Om IUse% är 100% kan du inte skapa fler filer!
# Vanligt problem: miljontals små filer (cache, sessions)

df -ih
# Samma sak men med human-readable format

# Om du har slut på inodes:
find /tmp -type f | wc -l
# Räknar antal filer i /tmp
# Ofta är det temporära filer som tar slut på inodes

find /var/spool -type f -delete
# VARNING: Raderar alla filer i /var/spool
# Gör bara detta om du vet vad du gör!
```

---

## Symlinks för deployment

Symlinks är perfekta för zero-downtime deploys:

```bash
# Struktur:
# /app/releases/v1.0.0/
# /app/releases/v1.1.0/
# /app/current -> releases/v1.0.0

# Deploy ny version
ln -sfn /app/releases/v1.1.0 /app/current
# -s = symbolic link
# -f = force (ersätt om finns)
# -n = no-dereference (behandla destination som fil, inte katalog)
#
# Nu pekar /app/current på v1.1.0
# Bytet är atomiskt - ingen downtime!

# Rollback är enkelt:
ln -sfn /app/releases/v1.0.0 /app/current
# Tillbaka till v1.0.0 på en sekund!
```

---

## Key Takeaways

1. **Inode** = filens ID-kort med all metadata, filnamnet är bara en etikett
2. **Hard link** = extra namn till samma inode, datan finns kvar tills alla namn är borta
3. **Symlink** = pekare till ett filnamn, blir broken om målet försvinner
4. **df -i** = kolla inode-användning, 100% = kan inte skapa filer
5. **ln -sfn** = atomisk symlink-switch, perfekt för deploys
""",
        },
        {
            "title": 'Disk Management',
            "slug": 'disk-management',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Disk Management

## Varför behöver du kunna detta?

Diskar är kritiska i alla system. Som DevOps hanterar du:

- **"Disk full" larm** - måste snabbt hitta vad som tar plats
- **Nya diskar** som ska partitioneras och formateras
- **Utökad lagring** när applikationer växer
- **LVM** för flexibel diskhantering i produktion

---

## Kolla diskutrymme med df

df (disk free) visar hur mycket utrymme som är ledigt på monterade filsystem.

```bash
df -h
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1        50G   35G   13G  73% /
# /dev/sdb1       100G   80G   15G  85% /data
# tmpfs           2.0G  100M  1.9G   5% /tmp
#
# -h = human-readable (GB, MB istället för bytes)
# Size = total storlek
# Used = använt utrymme
# Avail = ledigt utrymme
# Use% = procent använt - när detta når 100% är det problem!
# Mounted on = var disken är ansluten

df -h /var/log
# Visar bara filsystemet som /var/log ligger på
# Snabbt sätt att kolla hur det står till med en specifik katalog

df -i
# Filesystem      Inodes   IUsed   IFree IUse% Mounted on
# /dev/sda1      3276800  234567 3042233    8% /
#
# -i = inodes istället för bytes
# Du kan ha ledigt utrymme men slut på inodes!
# Varje fil kräver en inode
```

---

## Hitta vad som tar plats med du

du (disk usage) visar hur mycket utrymme filer och kataloger tar.

```bash
du -sh /var/log
# 2.5G    /var/log
#
# -s = summary (bara totalen, inte varje fil)
# -h = human-readable
# Visar att /var/log tar 2.5 GB

du -sh /var/log/*
# 1.2G    /var/log/syslog
# 800M    /var/log/nginx
# 300M    /var/log/auth.log
# 200M    /var/log/kern.log
#
# Listar storleken på varje fil/katalog i /var/log
# Nu ser du vad som tar mest plats!

du -sh /* 2>/dev/null | sort -rh | head -10
# 15G     /var
# 8.5G    /usr
# 3.2G    /home
# 1.1G    /opt
#
# Visar de 10 största katalogerna i root
# sort -rh = sortera numeriskt, störst först
# 2>/dev/null = tystar "permission denied" errors
# Perfekt för att snabbt hitta var utrymmet tar slut!

# Gå djupare i den största katalogen:
du -sh /var/* 2>/dev/null | sort -rh | head -10
# 12G     /var/log
# 2G      /var/cache
# 500M    /var/lib
```

---

## Hitta stora filer

```bash
find / -type f -size +100M 2>/dev/null
# /var/log/syslog.1
# /var/log/nginx/access.log
# /home/john/backup.tar.gz
#
# Hittar alla filer större än 100 MB
# -type f = bara filer (inte kataloger)
# -size +100M = större än 100 megabyte
# Perfekt för att hitta oväntade stora filer

find /var/log -type f -size +50M -exec ls -lh {} \\;
# -rw-r--r-- 1 root root 250M Dec 7 10:00 /var/log/syslog
# -rw-r--r-- 1 root root 180M Dec 7 09:00 /var/log/nginx/access.log
#
# -exec ls -lh {} \\; kör ls -lh på varje hittad fil
# Visar storlek och datum för varje stor fil
```

---

## Snabbstädning

```bash
# Rensa systemloggar (behåll senaste veckan)
sudo journalctl --vacuum-time=7d
# Freed 500M of archived journals
# journalctl hanterar systemd-loggar
# --vacuum-time=7d raderar loggar äldre än 7 dagar

# Rensa apt cache (Ubuntu/Debian)
sudo apt clean
# Raderar nedladdade paketfiler
# Kan frigöra flera GB

# Hitta och radera gamla loggar
find /var/log -name "*.log.*.gz" -mtime +30 -delete
# Raderar komprimerade loggar äldre än 30 dagar
# -mtime +30 = modified more than 30 days ago
# -delete = radera (VARNING: ingen bekräftelse!)
```

---

## Partitioner och filsystem

```bash
lsblk
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   100G  0 disk
# ├─sda1   8:1    0    99G  0 part /
# └─sda2   8:2    0     1G  0 part [SWAP]
# sdb      8:16   0   500G  0 disk
#
# Visar alla diskar och partitioner
# sda = första disken
# sda1 = första partitionen på sda
# sdb har ingen partition ännu

# Skapa partition på ny disk (FÖRSIKTIGT!)
sudo fdisk /dev/sdb
# m = visa hjälp
# n = ny partition
# p = primary partition
# 1 = partition nummer
# (enter för default start)
# (enter för default end - hela disken)
# w = write och avsluta

# Formatera med ext4
sudo mkfs.ext4 /dev/sdb1
# Skapar ext4-filsystem på partitionen
# VARNING: Detta raderar all data!

# Mounta
sudo mkdir /mnt/newdisk
sudo mount /dev/sdb1 /mnt/newdisk
```

---

## LVM Basics

LVM (Logical Volume Manager) ger flexibel diskhantering - du kan enkelt utöka volymer utan omstart.

```bash
# Visa LVM-struktur
sudo pvs
# PV         VG     Fmt  Attr PSize   PFree
# /dev/sda3  ubuntu lvm2 a--  <99.00g    0
#
# PV = Physical Volume (fysisk disk/partition)
# VG = Volume Group (grupp av diskar)

sudo vgs
# VG     #PV #LV #SN Attr   VSize   VFree
# ubuntu   1   2   0 wz--n- <99.00g    0
#
# Visar volymgrupper

sudo lvs
# LV     VG     Attr       LSize   Pool Origin Data%
# root   ubuntu -wi-ao---- <98.00g
# swap_1 ubuntu -wi-ao----   1.00g
#
# Visar logiska volymer

# Utöka en LVM-volym (efter att ha lagt till disk)
sudo lvextend -L +50G /dev/ubuntu/root
# Utökar volymen med 50 GB

sudo resize2fs /dev/ubuntu/root
# Utökar filsystemet till att fylla volymen
# Fungerar på ext4-filsystem
```

---

## Key Takeaways

1. **df -h** = snabb överblick av diskutrymme per filsystem
2. **du -sh /path/* | sort -rh** = hitta vad som tar plats
3. **find -size +100M** = hitta stora filer
4. **journalctl --vacuum-time=7d** = rensa gamla systemloggar
5. **LVM** = flexibel diskhantering, kan utöka volymer live
""",
        },
        {
            "title": 'Process Lifecycle and States',
            "slug": 'process-lifecycle',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Process Lifecycle and States

## Varför behöver du kunna detta?

Processer är allt som körs i Linux. Som DevOps måste du förstå:

- **Varför en process hänger** och hur du fixar det
- **Zombie-processer** som tar upp resurser
- **Processträd** för att förstå vad som startade vad
- **Resource-användning** för att optimera servrar

---

## Processer i Linux

Varje program som körs är en process. Varje process har ett unikt ID (PID) och en förälder (PPID).

```bash
ps aux | head -5
# USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root         1  0.0  0.1 169936 11896 ?        Ss   Dec06   0:03 /sbin/init
# root         2  0.0  0.0      0     0 ?        S    Dec06   0:00 [kthreadd]
# root         3  0.0  0.0      0     0 ?        I<   Dec06   0:00 [rcu_gp]
#
# PID = Process ID (unikt nummer)
# USER = vilken användare som kör processen
# %CPU = hur mycket CPU processen använder
# %MEM = hur mycket minne processen använder
# STAT = processens tillstånd (se nedan)
# COMMAND = vilket program som körs

echo $$
# 12345
# $$ är en speciell variabel som visar nuvarande shells PID
# Användbart i scripts för att skapa unika filnamn

echo $PPID
# 12340
# PPID = Parent Process ID
# Visar vilken process som startade den här processen
```

---

## Process States (STAT-kolumnen)

```bash
ps aux | grep -E "^USER|nginx|mysql"
# USER       PID %CPU %MEM STAT COMMAND
# root      1234  0.0  0.1 Ss   nginx: master
# www-data  1235  0.2  0.5 S    nginx: worker
# mysql     2345  1.5  5.0 Sl   /usr/sbin/mysqld

# Vanliga tillstånd:
# R = Running (körs just nu på CPU)
# S = Sleeping (väntar på något, t.ex. disk eller nätverk)
# D = Uninterruptible sleep (väntar på I/O, kan inte avbrytas)
# T = Stopped (pausad, t.ex. med Ctrl+Z)
# Z = Zombie (färdig men föräldern har inte hämtat exit-status)

# Extra bokstäver:
# s = session leader (t.ex. login shell)
# l = multi-threaded
# + = i förgrunden
# < = hög prioritet
# N = låg prioritet
```

---

## Zombie-processer

En zombie är en process som är klar men vars förälder inte har "hämtat" den ännu. Den tar ingen CPU eller minne, men upptar en plats i processtabellen.

```bash
ps aux | grep Z
# USER       PID %CPU %MEM STAT COMMAND
# john      5678  0.0  0.0 Z    [defunct]
#
# Z i STAT-kolumnen = zombie
# [defunct] visas ibland som COMMAND
# Zombies kan inte dödas med kill!

# Hitta zombiens förälder
ps -o ppid= -p 5678
# 1234
# PPID 1234 är föräldern som borde städa upp zombien

# Lösning: döda föräldern (eller vänta tills den gör det själv)
kill 1234
# När föräldern dör ärver init (PID 1) zombien och städar upp
```

---

## Processträd

```bash
pstree
# systemd─┬─sshd───sshd───bash───pstree
#         ├─nginx─┬─nginx
#         │       └─nginx
#         └─mysqld
#
# Visar hur processer hänger ihop
# systemd (PID 1) är föräldern till allt
# sshd startade en bash som kör pstree

pstree -p
# systemd(1)─┬─sshd(1234)───sshd(5678)───bash(5680)───pstree(5690)
#
# -p visar PID för varje process
# Användbart för att hitta vilken process som startade vad

pstree -p 1234
# Visar trädet under en specifik process
# Perfekt för att se alla barnprocesser till t.ex. en webserver
```

---

## Skapa processer

```bash
# Bakgrundsprocess med &
sleep 60 &
# [1] 12345
# Startar sleep i bakgrunden
# [1] = jobbnummer
# 12345 = PID

# Visa bakgrundsjobb
jobs
# [1]+  Running    sleep 60 &
# Visar alla jobb i nuvarande shell

# Subshell
(cd /tmp && ls)
# Kör kommandon i en subshell
# cd påverkar inte nuvarande shell
# Parenteser skapar ny process

# Fork bomb (KÖR ALDRIG I PRODUKTION!)
# :(){ :|:& };:
# Klassisk fork bomb som skapar oändligt många processer
# Kan krascha hela systemet på sekunder
```

---

## Process-information

```bash
# Detaljerad info om en process
cat /proc/1234/status
# Name:   nginx
# State:  S (sleeping)
# Pid:    1234
# PPid:   1
# Uid:    33  33  33  33
# VmRSS:  12340 kB
#
# /proc/PID/ innehåller allt om en process
# status visar övergripande info

ls /proc/1234/fd/
# 0  1  2  3  4
# Visar alla öppna filedescriptors
# 0 = stdin, 1 = stdout, 2 = stderr
# 3, 4, ... = andra öppna filer/sockets

cat /proc/1234/cmdline | tr '\\0' ' '
# /usr/sbin/nginx -g daemon off;
# Visar exakt hur processen startades
# tr ersätter null-tecken med mellanslag för läsbarhet
```

---

## Key Takeaways

1. **PID** = unikt process-ID, **PPID** = förälderns ID
2. **STAT** = processtillstånd (R=running, S=sleeping, Z=zombie)
3. **Zombies** kan inte dödas - döda föräldern istället
4. **pstree** = se hur processer hänger ihop
5. **/proc/PID/** = all info om en specifik process
""",
        },
        {
            "title": 'Foreground vs Background Processes',
            "slug": 'foreground-background-processes',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Foreground vs Background Processes

## Varför behöver du kunna detta?

När du jobbar med Linux-servrar behöver du ofta köra långvariga processer - backups, databasmigrering, byggjobb. Om du kör dem i förgrunden och tappar SSH-anslutningen avbryts allt. Förståelse för förgrund och bakgrund är skillnaden mellan att behöva starta om ett 4-timmars jobb eller låta det köra klart medan du gör annat.

---

## Förgrund och bakgrund

Tänk på det som en restaurangkock. Förgrunden är det du aktivt lagar just nu - du står vid spisen och rör i grytan. Bakgrunden är ugnen som jobbar på egen hand medan du gör annat.

```bash
sleep 60
# Kör i förgrunden - terminalen är blockerad
# Du kan inte skriva något annat förrän sleep är klar
# Ctrl+C avbryter kommandot

sleep 60 &
# [1] 12345
# & startar processen i bakgrunden
# [1] är jobbnumret i ditt shell
# 12345 är processens PID
# Terminalen är fri - du kan fortsätta jobba
```

---

## Hantera bakgrundsjobb

```bash
jobs
# [1]+  Running    sleep 60 &
# [2]-  Stopped    vim file.txt
#
# Visar alla jobb i nuvarande shell-session
# + markerar "current job" (default för fg/bg)
# - markerar "previous job"
# Running = körs i bakgrunden
# Stopped = pausad (t.ex. med Ctrl+Z)

jobs -l
# [1]+ 12345 Running    sleep 60 &
# [2]- 12346 Stopped    vim file.txt
#
# -l visar även PID för varje jobb
# Användbart om du behöver skicka signaler
```

---

## Flytta mellan förgrund och bakgrund

```bash
# Starta något i förgrunden
vim file.txt
# Tryck Ctrl+Z för att pausa
# [1]+  Stopped    vim file.txt

bg %1
# [1]+ vim file.txt &
# bg återupptar jobbet i bakgrunden
# %1 refererar till jobb nummer 1
# Fungerar inte för vim (behöver terminal), men bra för scripts

fg %1
# vim öppnas igen i förgrunden
# fg tar tillbaka ett jobb till förgrunden
# Nu kan du fortsätta redigera

# Kortform
fg
# Tar tillbaka senaste jobbet (markerat med +)
# Ingen %nummer behövs för current job
```

---

## Hålla processer vid liv efter logout

Problemet med bakgrundsprocesser är att de dör när du loggar ut. Din SSH-session äger processen, och när sessionen stängs skickas SIGHUP till alla barnprocesser.

```bash
nohup ./long_running_script.sh &
# nohup: ignoring input and appending output to 'nohup.out'
# [1] 12345
#
# nohup = "no hangup"
# Processen ignorerar SIGHUP-signalen
# Output sparas automatiskt i nohup.out
# Processen överlever även om du stänger terminalen

nohup ./backup.sh > /var/log/backup.log 2>&1 &
# Samma princip men med egen loggfil
# 2>&1 skickar stderr till samma fil som stdout
# Nu loggas allt till /var/log/backup.log
```

---

## disown - ta bort från jobbkontroll

Om du glömde nohup kan du rädda situationen med disown:

```bash
./long_job.sh &
# [1] 12345
# Ups, glömde nohup!

disown %1
# Tar bort jobbet från shell:ets jobbkontroll
# Nu skickas inte SIGHUP när du loggar ut
# Jobbet är fortfarande igång men syns inte i jobs

disown -h %1
# -h markerar bara att SIGHUP ska ignoreras
# Jobbet syns fortfarande i jobs
# Säkrare alternativ - du behåller kontrollen
```

---

## Praktiskt exempel: Deploy-script

```bash
# Dåligt sätt - dör om SSH tappar anslutning
./deploy.sh

# Bättre - körs i bakgrunden
./deploy.sh &

# Bäst - överlever logout och loggar allt
nohup ./deploy.sh > /var/log/deploy-$(date +%Y%m%d).log 2>&1 &
# date +%Y%m%d ger dagens datum (20250615)
# All output går till en datummärkt loggfil
# Processen överlever även om du tappar anslutningen

# Kolla status senare
tail -f /var/log/deploy-20250615.log
# -f följer filen i realtid
# Ctrl+C avslutar tail, inte deploy-scriptet
```

---

## Screen och tmux för riktiga jobb

För långvariga interaktiva jobb är screen eller tmux bättre än nohup:

```bash
# Starta en screen-session
screen -S deploy
# Skapar en session med namn "deploy"
# Nu är du inne i screen

# Kör dina kommandon
./deploy.sh

# Koppla loss sessionen (behåll körande)
# Tryck Ctrl+A, sedan D

# Lista sessioner
screen -ls
# There is a screen on:
#     12345.deploy (Detached)

# Återanslut till sessionen
screen -r deploy
# Nu är du tillbaka i samma session
# Fungerar även från en annan dator!
```

---

## Key Takeaways

1. **&** = starta process i bakgrunden
2. **Ctrl+Z** = pausa förgrundsprocess
3. **jobs** = lista bakgrundsjobb
4. **fg/bg** = flytta jobb mellan förgrund/bakgrund
5. **nohup** = överlev logout
""",
        },
        {
            "title": 'Job Control (jobs, fg, bg, nohup)',
            "slug": 'job-control',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Job Control (jobs, fg, bg, nohup)

## Varför behöver du kunna detta?

Som DevOps-ingenjör kommer du ofta att köra långvariga kommandon - databasexporter, logganalyser, backup-skript. Du måste kunna pausa dem, flytta dem till bakgrunden, och se till att de överlever även om du tappar din SSH-anslutning.

---

## Jobs-kommandot

Tänk på det som en lista över allt du har igång i din terminal. Precis som du kan ha flera flikar öppna i webbläsaren kan du ha flera processer körande i samma terminal.

```bash
jobs
# [1]+  Running    ./backup.sh &
# [2]-  Stopped    vim config.txt
#
# [1] och [2] är jobbnummer - används med fg och bg
# + markerar "current job" (det fg tar om du inte anger nummer)
# - markerar "previous job"
# Running = körs i bakgrunden
# Stopped = pausad med Ctrl+Z

jobs -l
# [1]+ 12345 Running    ./backup.sh &
# [2]- 12346 Stopped    vim config.txt
#
# -l lägger till PID för varje jobb
# PID:et behövs om du vill skicka signaler direkt
```

---

## Pausa och återuppta processer

```bash
# Starta en process i förgrunden
./long_script.sh
# Processen körs, terminalen är blockerad

# Tryck Ctrl+Z för att pausa
# [1]+  Stopped    ./long_script.sh
# Processen fryses mitt i allt den gör
# Som att trycka paus på en video

# Se pausade jobb
jobs
# [1]+  Stopped    ./long_script.sh

# Återuppta i bakgrunden
bg %1
# [1]+ ./long_script.sh &
# Processen fortsätter köra
# Du får tillbaka terminalen

# Eller återuppta i förgrunden
fg %1
# Processen tar över terminalen igen
# Du ser outputen i realtid
```

---

## Starta direkt i bakgrunden

```bash
./backup.sh &
# [1] 12345
# & efter kommandot startar det i bakgrunden
# [1] = jobbnummer
# 12345 = processens PID

# Flera jobb samtidigt
./job1.sh &
./job2.sh &
./job3.sh &
# Nu körs tre jobb parallellt
# Alla tre arbetar samtidigt

jobs
# [1]   Running    ./job1.sh &
# [2]-  Running    ./job2.sh &
# [3]+  Running    ./job3.sh &
```

---

## nohup - överlev avbruten anslutning

Det stora problemet med bakgrundsjobb är att de dör om du loggar ut eller tappar SSH-anslutningen. Signalen SIGHUP skickas till alla processer som tillhör din session.

```bash
nohup ./backup.sh &
# [1] 12345
# nohup: ignoring input and appending output to 'nohup.out'
#
# nohup betyder "no hangup"
# Processen ignorerar SIGHUP
# Output skrivs till nohup.out om du inte anger annat

# Med egen loggfil
nohup ./backup.sh > /var/log/backup.log 2>&1 &
# > /var/log/backup.log skickar stdout till loggfilen
# 2>&1 skickar stderr till samma ställe
# Nu loggas allt snyggt

# Verifiera att processen körs
ps aux | grep backup.sh
# Processen syns även efter du loggat ut och in igen
```

---

## disown - rädda glömda jobb

Ibland startar du ett jobb utan nohup och inser sedan att du behöver logga ut:

```bash
./important_job.sh &
# [1] 12345
# Ops, glömde nohup!

disown %1
# Jobbet tas bort från shell:ets kontroll
# Nu skickas inte SIGHUP när du loggar ut
# Men jobbet syns inte längre i jobs

# Alternativ: behåll i jobs men ignorera SIGHUP
disown -h %1
# -h = håll jobbet i listan
# Men markera att det ska ignorera SIGHUP
# Bästa av båda världar
```

---

## Praktiskt exempel: Databasmigrering

```bash
# Starta migreringsscript
./migrate_database.sh
# Märker att det tar timmar...
# Tryck Ctrl+Z
# [1]+  Stopped    ./migrate_database.sh

# Flytta till bakgrunden
bg %1
# [1]+ ./migrate_database.sh &
# Nu körs migreringen i bakgrunden

# Se till att den överlever logout
disown -h %1
# Nu kan du logga ut tryggt

# Kolla statusen senare från var som helst
ps aux | grep migrate
# Se att processen fortfarande körs
```

---

## Key Takeaways

1. **Ctrl+Z** = pausa förgrundsprocess
2. **bg %n** = fortsätt pausat jobb i bakgrunden
3. **fg %n** = ta tillbaka jobb till förgrunden
4. **nohup** = starta process som överlever logout
5. **disown** = rädda redan startade jobb
""",
        },
        {
            "title": 'Signals (SIGTERM, SIGKILL, SIGHUP)',
            "slug": 'signals',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Signals (SIGTERM, SIGKILL, SIGHUP)

## Varför behöver du kunna detta?

Signaler är hur Linux kommunicerar med processer. När du trycker Ctrl+C, startar om en tjänst, eller stänger av en server - allt sker via signaler. Som DevOps måste du veta skillnaden mellan att be en process snällt att avsluta och att tvångsstänga den, annars riskerar du dataförlust och korrupta filer.

---

## Vad är signaler?

Tänk på det som meddelanden till processer. En del meddelanden är förfrågningar som processen kan ignorera, andra är tvingande order. Precis som skillnaden mellan att be någon gå hem och att fysiskt lyfta ut dem.

```bash
kill -l
# Lista alla tillgängliga signaler
#  1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
#  9) SIGKILL     15) SIGTERM     18) SIGCONT     19) SIGSTOP
# ...och många fler

# Signaler har både nummer och namn
# kill -15 = kill -SIGTERM = kill -TERM
# Alla tre gör samma sak
```

---

## De viktigaste signalerna

```bash
# SIGTERM (15) - "Var snäll och avsluta"
kill 12345
# Samma som kill -15 12345
# Processen får chansen att städa upp
# Stänga databasanslutningar, spara filer
# Det civiliserade sättet att avsluta

# SIGKILL (9) - "Dö. Nu."
kill -9 12345
# Processen kan INTE ignorera detta
# Ingen cleanup, ingen nåd
# Använd bara som sista utväg
# Kan lämna temporära filer, låsta resurser

# SIGINT (2) - "Avbryt det du gör"
# Samma som Ctrl+C
kill -2 12345
# Processen får signal att avbryta
# Brukar leda till exit

# SIGHUP (1) - "Terminalen stängdes"
kill -1 12345
# Skickas automatiskt när terminal stängs
# Många daemoner läser om config vid SIGHUP
# T.ex. nginx reload sker via SIGHUP
```

---

## Skillnaden mellan SIGTERM och SIGKILL

```bash
# SIGTERM - rätt sätt
kill 12345
# Processen får besked: "Snälla avsluta"
# Processen kan:
#   - Spara data till disk
#   - Stänga databaskopplingar
#   - Skriva loggmeddelande
#   - Ta bort temporära filer
# Sedan avslutar den frivilligt

# SIGKILL - nödläge
kill -9 12345
# Kerneln terminerar processen omedelbart
# Processen får ingen chans att göra något
# Potentiella problem:
#   - Osparat data försvinner
#   - Låsta filer kan förbli låsta
#   - Temporära filer städas inte
#   - Databaskorruption möjlig
```

---

## kill, killall och pkill

```bash
# kill - döda via PID
kill 12345
# Skickar SIGTERM till process 12345

# killall - döda via namn
killall nginx
# Dödar ALLA processer som heter "nginx"
# Var försiktig - kan träffa fel processer!

# pkill - döda via mönster
pkill -f "python backup.py"
# -f matchar mot hela kommandoraden
# Mer flexibelt än killall

# Hitta PID först
pgrep nginx
# 12345
# 12346
# Visar PID för processer som matchar

pgrep -f "python backup"
# 23456
# -f söker i hela kommandoraden
```

---

## Graceful shutdown

```bash
# Steg 1: Be snällt
kill 12345
# Vänta några sekunder

# Steg 2: Kolla om den lever
ps aux | grep 12345
# Om den fortfarande finns...

# Steg 3: Tvinga (om nödvändigt)
kill -9 12345

# Som script:
PID=12345
kill $PID
# Vänta max 10 sekunder på graceful shutdown
for i in {1..10}; do
    if ! ps -p $PID > /dev/null 2>&1; then
        echo "Process avslutad gracefully"
        exit 0
    fi
    sleep 1
done
# Om fortfarande vid liv, tvinga
kill -9 $PID
echo "Process tvångsstängd"
```

---

## SIGHUP för reload

Många tjänster använder SIGHUP för att läsa om sin konfiguration utan att starta om:

```bash
# Nginx reload via signal
kill -HUP $(cat /var/run/nginx.pid)
# Nginx läser om nginx.conf
# Inga aktiva anslutningar avbryts
# Samma som: nginx -s reload

# SSH daemon
kill -HUP $(pgrep sshd)
# Läser om sshd_config
# Befintliga SSH-sessioner påverkas inte

# Systemd-sättet (rekommenderat)
sudo systemctl reload nginx
# Gör samma sak men mer robust
```

---

## Trap i scripts

Du kan fånga signaler i dina egna scripts:

```bash
#!/bin/bash
# cleanup.sh

cleanup() {
    echo "Städar upp temporära filer..."
    rm -f /tmp/myapp_*
    echo "Klar!"
    exit 0
}

# Fånga SIGTERM och SIGINT
trap cleanup SIGTERM SIGINT

echo "Script kör... (Ctrl+C för att avsluta)"
while true; do
    # Gör arbete här
    sleep 1
done

# Nu när scriptet får Ctrl+C eller kill
# körs cleanup-funktionen först
```

---

## Key Takeaways

1. **SIGTERM (kill)** = be snällt, låt processen städa
2. **SIGKILL (kill -9)** = tvinga, sista utväg
3. **SIGHUP** = läs om config (reload)
4. **Ctrl+C** = SIGINT
5. **Alltid SIGTERM först**, SIGKILL bara om nödvändigt
""",
        },
        {
            "title": 'Process Monitoring (ps, top, htop)',
            "slug": 'process-monitoring',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Process Monitoring (ps, top, htop)

## Varför behöver du kunna detta?

När en server blir långsam eller slutar svara är processövervakning ditt första diagnostikverktyg. Du måste kunna identifiera vilken process som äter all CPU, vilket program som läcker minne, och vad som blockerar din databas.

---

## ps - ögonblicksbild av processer

ps visar processer vid ett specifikt ögonblick, som en stillbild. Det är perfekt för att lista vad som körs och filtrera med grep.

```bash
ps aux
# USER       PID %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
# root         1  0.0  0.1 169936 11896 ?   Ss   Dec06   0:03 /sbin/init
# postgres  1234  2.3  5.0 421532 51200 ?   Ssl  10:30   1:23 postgres
# nginx     2345  0.1  0.2  98765  2048 ?   S    10:30   0:05 nginx: worker
#
# a = alla användares processer
# u = user-format med mer detaljer
# x = även processer utan terminal

# Viktiga kolumner:
# PID = process ID
# %CPU = CPU-användning just nu
# %MEM = minnesanvändning
# VSZ = virtuellt minne (kan vara stort, oroa dig inte)
# RSS = faktiskt fysiskt minne (detta är vad som räknas)
# STAT = status (S=sleeping, R=running, Z=zombie)
# TIME = total CPU-tid sedan start

ps aux | grep nginx
# Filtrera på processnamn
# Visar bara nginx-processer
# Inkluderar även grep-kommandot självt

ps aux | grep "[n]ginx"
# Fint trick - [n] matchar inte grep-kommandot
# Så du slipper se "grep nginx" i outputen
```

---

## top - realtidsövervakning

```bash
top
# top visar processer i realtid, uppdateras varannan sekund
# Som att titta på aktivitetshanteraren
#
# top - 14:23:45 up 5 days,  3:12,  2 users,  load average: 0.52, 0.48, 0.45
# Tasks: 234 total,   1 running, 232 sleeping,   0 stopped,   1 zombie
# %Cpu(s):  5.2 us,  2.1 sy,  0.0 ni, 92.3 id,  0.3 wa,  0.0 hi,  0.1 si
# MiB Mem :  16000.0 total,   4523.2 free,   8234.1 used,   3242.7 buff/cache
#
# load average: 0.52, 0.48, 0.45
# = belastning senaste 1, 5, 15 minuter
# Under antal CPU-kärnor = okej
# Över = överlast

# Tangenter i top:
# M = sortera efter minne
# P = sortera efter CPU
# k = döda process (frågar om PID)
# q = avsluta
# 1 = visa alla CPU-kärnor separat
# h = hjälp
```

---

## htop - modern processövervakning

```bash
htop
# htop är top med färger och mus-stöd
# Mycket lättare att läsa
# Visar CPU och minne som grafer
#
# Fördelar över top:
# - Färgkodning
# - Kan scrolla horisontellt
# - Visar hela kommandorader
# - Träd-vy (F5)
# - Enklare att döda processer (F9)
# - Sök med F3
# - Filter med F4

# Installera om det saknas
sudo apt install htop
# eller
brew install htop

# Kör för specifik användare
htop -u www-data
# Visar bara processer för www-data
# Bra för att se vad en tjänst gör
```

---

## Hitta processer

```bash
pgrep nginx
# 1234
# 1235
# pgrep hittar PID för processer som matchar
# Enklare än ps aux | grep

pgrep -l nginx
# 1234 nginx
# 1235 nginx
# -l visar även processnamn

pgrep -f "python backup.py"
# 5678
# -f söker i hela kommandoraden
# Hittar "python backup.py" även om processnamnet bara är "python"

pidof nginx
# 1234 1235
# Liknande men alla PID på en rad
# Användbart i scripts
```

---

## lsof - öppna filer och portar

```bash
lsof -i :80
# COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# nginx    1234   root    6u  IPv4  12345      0t0  TCP *:http (LISTEN)
# nginx    1235   www-data 6u  IPv4  12345      0t0  TCP *:http (LISTEN)
#
# Visar vad som lyssnar på port 80
# Perfekt för "address already in use" fel

lsof -i :3000
# Kolla vilken process som använder port 3000
# Vanligt problem: app startar inte för porten är upptagen

lsof -p 1234
# Visa alla filer öppna av process 1234
# Inkluderar nätverksanslutningar, loggfiler, etc.

lsof -u postgres
# Visa allt som postgres-användaren har öppet
# Bra för att förstå vad en tjänst gör
```

---

## Praktiskt exempel: Felsök långsam server

```bash
# Steg 1: Kolla load
uptime
# 14:23:45 up 5 days, load average: 8.52, 7.48, 6.45
# Load över antal kärnor = problem!

# Steg 2: Hitta vad som äter CPU
top -bn1 | head -20
# -b = batch mode (för scripts)
# -n1 = bara en iteration
# Kolla vilken process har högst %CPU

# Steg 3: Kolla minne
free -h
#               total        used        free      shared  buff/cache   available
# Mem:           16Gi       14Gi       500Mi       256Mi        1.5Gi        1.2Gi
# Om "available" är lågt = minnesproblem

# Steg 4: Hitta minnesslukare
ps aux --sort=-%mem | head -10
# Sorterar efter minne, högst först
# --sort=-%cpu för CPU istället
```

---

## Key Takeaways

1. **ps aux** = lista alla processer (ögonblicksbild)
2. **top/htop** = realtidsövervakning
3. **pgrep** = hitta PID snabbt
4. **lsof -i :port** = vad använder porten?
5. **load average** = under antal kärnor är okej
""",
        },
        {
            "title": 'Systemd Architecture',
            "slug": 'systemd-architecture',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Systemd Architecture

## Varför behöver du kunna detta?

Systemd är hjärtat i moderna Linux-system. Det är processen som startar först (PID 1) och ansvarar för att starta alla andra tjänster. Som DevOps måste du förstå hur systemd fungerar för att kunna felsöka startproblem, konfigurera tjänster rätt, och förstå varför saker ibland inte fungerar som förväntat.

---

## Vad är systemd?

Tänk på det som en projektledare som ansvarar för att koordinera alla arbetare (tjänster) på en byggarbetsplats. Projektledaren vet vilka som måste komma först, vilka som är beroende av varandra, och ser till att alla startar i rätt ordning.

```bash
ps -p 1
# PID TTY      TIME CMD
#   1 ?        00:00:03 systemd
#
# PID 1 är alltid den första processen
# På moderna Linux är detta systemd
# Alla andra processer är barn eller barnbarn till denna

pstree -p 1 | head -20
# systemd(1)─┬─agetty(456)
#            ├─cron(789)
#            ├─nginx(1234)─┬─nginx(1235)
#            │             └─nginx(1236)
#            └─sshd(2345)───sshd(3456)───bash(3457)
#
# Visar hur alla processer härstammar från systemd
# Om en tjänst kraschar kan systemd starta om den
```

---

## Units - systemds byggstenar

Systemd hanterar allt som "units". Det finns olika typer beroende på vad de gör:

```bash
systemctl list-units --type=help
# Available unit types:
# service  - Tjänster/daemoner (nginx, postgresql)
# socket   - Nätverkssockets
# target   - Grupper av units (multi-user.target)
# timer    - Schemalagda jobb (som cron)
# mount    - Filsystem att mounta
# device   - Hårdvaruenheter
# path     - Övervaka filer/kataloger

systemctl list-units --type=service --state=running
# UNIT                    LOAD   ACTIVE SUB     DESCRIPTION
# cron.service            loaded active running Regular background program processing daemon
# nginx.service           loaded active running A high performance web server
# postgresql.service      loaded active running PostgreSQL RDBMS
# ssh.service             loaded active running OpenBSD Secure Shell server
#
# Visar alla körande tjänster
# --state= kan vara running, failed, inactive
```

---

## Var finns unit-filer?

```bash
# Systemets unit-filer (paketinstallerade)
ls /lib/systemd/system/*.service | head -5
# /lib/systemd/system/cron.service
# /lib/systemd/system/nginx.service
# /lib/systemd/system/ssh.service
# Rör INTE dessa - de skrivs över vid uppgradering

# Administratörens unit-filer (dina egna)
ls /etc/systemd/system/*.service 2>/dev/null
# /etc/systemd/system/myapp.service
# Här lägger du egna tjänster
# Har prioritet över /lib-versioner

# Runtime units (skapas dynamiskt)
ls /run/systemd/system/
# Skapas och försvinner vid körning
# Sällan något du behöver röra

# Se var en specifik unit kommer från
systemctl show nginx.service --property=FragmentPath
# FragmentPath=/lib/systemd/system/nginx.service
```

---

## Dependencies och ordning

```bash
# Vad beror nginx på?
systemctl list-dependencies nginx.service
# nginx.service
# ├─system.slice
# └─sysinit.target
#   ├─dev-hugepages.mount
#   └─...
#
# nginx beror på att sysinit.target är klar
# systemd startar dependencies först

# Vad beror på nginx?
systemctl list-dependencies --reverse nginx.service
# Visar vilka units som kräver att nginx körs

# Detaljerade dependencies
systemctl show nginx.service | grep -E "^(Wants|Requires|After|Before)="
# Wants=      - mjuka beroenden (startas om möjligt)
# Requires=   - hårda beroenden (måste finnas)
# After=      - starta efter dessa
# Before=     - starta före dessa
```

---

## Targets - grupper av tjänster

Targets är som bokmärken för systemtillstånd. multi-user.target är normalt körläge, graphical.target inkluderar skrivbordet.

```bash
systemctl list-units --type=target
# UNIT                   LOAD   ACTIVE DESCRIPTION
# basic.target           loaded active Basic System
# multi-user.target      loaded active Multi-User System
# network-online.target  loaded active Network is Online
# network.target         loaded active Network
#
# Targets grupperar relaterade tjänster
# multi-user.target = "servern är redo"

# Vilket target körs nu?
systemctl get-default
# multi-user.target
# Detta är vad systemet siktar på vid boot

# Ändra default target (för servrar behövs sällan)
sudo systemctl set-default multi-user.target
# Nu bootar systemet till textkonsol, inte grafiskt
```

---

## Cgroups - resurskontroll

Systemd använder Linux cgroups för att isolera och begränsa resurser:

```bash
systemd-cgls
# Control group /:
# ├─1 /sbin/init
# ├─user.slice
# │ └─user-1000.slice
# │   └─session-1.scope
# │     ├─3456 sshd: user@pts/0
# │     └─3457 -bash
# └─system.slice
#   ├─nginx.service
#   │ ├─1234 nginx: master process
#   │ └─1235 nginx: worker process
#
# Visar process-hierarkin organiserad i cgroups
# Varje tjänst kör i sin egen grupp

# Resursanvändning per tjänst
systemd-cgtop
# Control Group                          Tasks   %CPU   Memory
# /system.slice/nginx.service                3    0.2   128.0M
# /system.slice/postgresql.service          15    1.5   512.0M
#
# Som top men grupperat per tjänst
# Perfekt för att se vilken tjänst som är resurskrävande
```

---

## Praktiskt exempel: Felsök startproblem

```bash
# Tjänsten startar inte - vad är fel?
systemctl status myapp.service
# ● myapp.service - My Application
#    Loaded: loaded (/etc/systemd/system/myapp.service; enabled)
#    Active: failed (Result: exit-code) since Mon 2025-01-15 10:30:00 UTC
# Main PID: 12345 (code=exited, status=1/FAILURE)

# Kolla loggarna
journalctl -u myapp.service -n 50
# Se vad som gick fel vid senaste start

# Kolla dependency-ordning
systemctl list-dependencies myapp.service --all
# Kanske beror den på något som inte startat?

# Starta om efter fix
sudo systemctl daemon-reload
# Läser om unit-filer efter ändringar

sudo systemctl restart myapp.service
# Försök starta igen
```

---

## Key Takeaways

1. **systemd är PID 1** - förälder till alla processer
2. **Units** = tjänster, sockets, targets, timers
3. **/etc/systemd/system/** = dina egna tjänster
4. **Targets** = grupper av tjänster (multi-user.target)
5. **daemon-reload** = läs om efter ändringar i unit-filer
""",
        },
        {
            "title": 'Unit Files (service, timer, socket)',
            "slug": 'unit-files',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# Unit Files (service, timer, socket)

## Varför behöver du kunna detta?

För att köra dina egna applikationer som tjänster på Linux måste du skapa unit-filer. Det är också så du sätter upp schemalagda jobb med timers istället för det äldre cron-systemet. Att förstå unit-filers syntax gör dig kapabel att konfigurera exakt hur din app ska starta, starta om vid krasch, och bero på andra tjänster.

---

## Service units

En service unit beskriver en tjänst som ska köras. Det är den vanligaste typen.

```bash
cat /etc/systemd/system/myapp.service
# [Unit]
# Description=My Application
# After=network.target postgresql.service
# Requires=postgresql.service
#
# [Unit]-sektionen beskriver tjänsten
# Description = vad användare ser i systemctl status
# After = starta EFTER dessa tjänster
# Requires = dessa MÅSTE köra (hard dependency)

# [Service]
# Type=simple
# User=myapp
# Group=myapp
# WorkingDirectory=/opt/myapp
# ExecStart=/opt/myapp/bin/server
# ExecReload=/bin/kill -HUP $MAINPID
# Restart=on-failure
# RestartSec=5
#
# [Service]-sektionen beskriver hur tjänsten körs
# Type=simple = processen ÄR tjänsten
# User/Group = vilken användare som kör
# WorkingDirectory = cd hit före start
# ExecStart = kommandot som startar tjänsten
# Restart=on-failure = starta om vid krasch
# RestartSec=5 = vänta 5 sekunder före omstart

# [Install]
# WantedBy=multi-user.target
#
# [Install]-sektionen beskriver när tjänsten ska vara aktiv
# WantedBy = aktiveras när denna target nås
# multi-user.target = normalt körläge för servrar
```

---

## Skapa en egen service

```bash
sudo vim /etc/systemd/system/myapp.service
# Skriv innehållet ovan

# Läs om konfigurationen
sudo systemctl daemon-reload
# ALLTID efter ändringar i unit-filer
# Annars ser systemd inte dina ändringar

# Aktivera tjänsten
sudo systemctl enable myapp.service
# Skapar symlink så den startar vid boot

# Starta tjänsten
sudo systemctl start myapp.service
# Nu körs din app

# Kolla status
systemctl status myapp.service
# Visar om den körs, senaste loggraderna, PID mm
```

---

## Timer units

Timer units är moderna ersättaren för cron. De är mer flexibla och integrerar med journald för loggning.

```bash
cat /etc/systemd/system/backup.timer
# [Unit]
# Description=Run backup every night
#
# [Timer]
# OnCalendar=*-*-* 02:00:00
# Persistent=true
#
# [Install]
# WantedBy=timers.target

# OnCalendar följer formatet: År-Månad-Dag Tim:Minut:Sekund
# *-*-* 02:00:00 = varje dag kl 02:00
# *-*-* *:00:00 = varje timme
# Mon *-*-* 10:00:00 = varje måndag kl 10:00
# *-*-01 00:00:00 = första dagen varje månad

# Persistent=true = kör om missad (t.ex. om servern var av)

cat /etc/systemd/system/backup.service
# [Unit]
# Description=Backup script
#
# [Service]
# Type=oneshot
# ExecStart=/usr/local/bin/backup.sh
#
# Type=oneshot = kör en gång och avsluta
# Ingen [Install]-sektion behövs - timern startar den
```

---

## Aktivera timer

```bash
sudo systemctl daemon-reload
# Läs om nya filer

sudo systemctl enable backup.timer
# Aktivera timern vid boot

sudo systemctl start backup.timer
# Starta timern nu

systemctl list-timers
# NEXT                         LEFT          LAST                         PASSED       UNIT
# Tue 2025-01-16 02:00:00 UTC  11h left      Mon 2025-01-15 02:00:00 UTC  12h ago      backup.timer
#
# Visar alla aktiva timers
# NEXT = när den körs nästa gång
# LAST = senaste körning
```

---

## Socket units

Socket units startar tjänster on-demand - först när någon ansluter till porten. Sparar resurser för sällan använda tjänster.

```bash
cat /etc/systemd/system/myapp.socket
# [Unit]
# Description=MyApp Socket
#
# [Socket]
# ListenStream=8080
# Accept=no
#
# [Install]
# WantedBy=sockets.target

# ListenStream=8080 = lyssna på TCP port 8080
# Accept=no = starta tjänsten vid första anslutning
#             (Accept=yes = en instans per anslutning)

# Tjänsten startas automatiskt:
# myapp.socket -> myapp.service
# Namnen måste matcha (minus suffixet)
```

---

## Viktiga direktiv

```bash
# Restart-beteende
# Restart=no          - starta aldrig om (default)
# Restart=on-failure  - starta om vid krasch (exit != 0)
# Restart=always      - starta alltid om (även vid success)
# Restart=on-abnormal - vid signaler, timeout, watchdog

# Service-typer
# Type=simple   - ExecStart är huvudprocessen
# Type=forking  - processen forkar (äldre daemons)
# Type=oneshot  - kör en gång och avsluta
# Type=notify   - tjänsten meddelar när den är redo

# Environment
# Environment=NODE_ENV=production
# EnvironmentFile=/etc/myapp/config
```

---

## Praktiskt exempel: Node.js app som service

```bash
sudo vim /etc/systemd/system/nodeapp.service
```

```ini
[Unit]
Description=Node.js Application
After=network.target

[Service]
Type=simple
User=nodeapp
Group=nodeapp
WorkingDirectory=/opt/nodeapp
ExecStart=/usr/bin/node /opt/nodeapp/server.js
Restart=on-failure
RestartSec=10
Environment=NODE_ENV=production
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now nodeapp.service
# enable --now = enable + start i ett kommando
```

---

## Key Takeaways

1. **[Unit]** = beskrivning och dependencies
2. **[Service]** = hur tjänsten körs
3. **[Install]** = när den aktiveras
4. **daemon-reload** = ALLTID efter ändringar
5. **timer units** = moderna cron-jobb
""",
        },
        {
            "title": 'Service Management (systemctl)',
            "slug": 'service-management',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Service Management (systemctl)

## Varför behöver du kunna detta?

Varje webbserver, databas, cache och applikation på en Linux-server körs som en tjänst hanterad av systemd. Du måste kunna starta, stoppa, starta om och felsöka tjänster. Det är vad du gör varje dag som DevOps-ingenjör.

---

## Grundläggande tjänsthantering

```bash
sudo systemctl start nginx
# Startar nginx-tjänsten omedelbart
# Gör ingenting om den redan körs
# Kräver sudo för de flesta tjänster

sudo systemctl stop nginx
# Stoppar nginx-tjänsten
# Skickar SIGTERM, väntar, sedan SIGKILL om nödvändigt
# Alla anslutningar stängs

sudo systemctl restart nginx
# Stop + start i en operation
# Orsakar kort nedtid
# Använd för större konfigurationsändringar

sudo systemctl reload nginx
# Läser om konfiguration utan att stoppa
# Skickar SIGHUP till processen
# INGEN nedtid - befintliga anslutningar fortsätter
# Fungerar bara om tjänsten stödjer det
```

---

## Status och information

```bash
systemctl status nginx
# ● nginx.service - A high performance web server
#    Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
#    Active: active (running) since Mon 2025-01-15 10:00:00 UTC; 2h ago
#  Main PID: 1234 (nginx)
#     Tasks: 3 (limit: 4915)
#    Memory: 12.5M
#    CGroup: /system.slice/nginx.service
#            ├─1234 nginx: master process /usr/sbin/nginx
#            ├─1235 nginx: worker process
#            └─1236 nginx: worker process
#
# Visar:
# - Om tjänsten körs (active/running)
# - Sedan när
# - Process-ID
# - Minnesanvändning
# - Senaste loggraderna

systemctl is-active nginx
# active
# Returkod 0 = körs
# Returkod != 0 = körs inte
# Perfekt för scripts

systemctl is-enabled nginx
# enabled
# Visar om tjänsten startar vid boot

systemctl show nginx --property=MainPID
# MainPID=1234
# Hämta specifik egenskap
# Användbart för automation
```

---

## Enable och disable

```bash
sudo systemctl enable nginx
# Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service
# → /lib/systemd/system/nginx.service
#
# Tjänsten startar nu automatiskt vid boot
# Skapar en symlink i target-katalogen
# Startar INTE tjänsten just nu

sudo systemctl disable nginx
# Removed symlink /etc/systemd/system/multi-user.target.wants/nginx.service
#
# Tjänsten startar INTE vid boot längre
# Stoppar INTE tjänsten just nu

sudo systemctl enable --now nginx
# Gör båda i ett kommando:
# 1. Aktiverar vid boot
# 2. Startar omedelbart
# Perfekt för nya installationer
```

---

## Lista tjänster

```bash
systemctl list-units --type=service
# UNIT                      LOAD   ACTIVE SUB     DESCRIPTION
# cron.service              loaded active running Regular background program
# nginx.service             loaded active running A high performance web server
# postgresql.service        loaded active running PostgreSQL RDBMS
#
# Visar alla laddade och aktiva tjänster
# LOAD = om unit-filen hittades
# ACTIVE = övergripande tillstånd
# SUB = detaljerat tillstånd

systemctl list-units --type=service --state=running
# Bara körande tjänster
# --state= kan vara running, failed, inactive, dead

systemctl list-units --type=service --state=failed
# Visar tjänster som kraschat
# Första stoppet vid felsökning

systemctl list-unit-files --type=service
# UNIT FILE                  STATE
# nginx.service              enabled
# postgresql.service         enabled
# apache2.service            disabled
#
# Visar alla installerade tjänster
# Oavsett om de körs eller inte
# STATE = enabled/disabled/masked
```

---

## Mask och unmask

```bash
sudo systemctl mask apache2
# Created symlink /etc/systemd/system/apache2.service → /dev/null
#
# Tjänsten kan INTE startas alls
# Inte ens manuellt
# Använd för att förhindra konflikt
# T.ex. nginx OCH apache på samma server

sudo systemctl unmask apache2
# Removed symlink /etc/systemd/system/apache2.service
#
# Tar bort maskeringen
# Nu kan tjänsten startas igen

# Skillnad: disable vs mask
# disable = startar inte vid boot, KAN startas manuellt
# mask = kan INTE startas överhuvudtaget
```

---

## Praktiskt exempel: Deploy ny version

```bash
# 1. Kolla att tjänsten körs
systemctl is-active myapp
# active

# 2. Deployka ny kod
# ... (kopiera filer, etc)

# 3. Starta om tjänsten
sudo systemctl restart myapp

# 4. Verifiera att den startade
systemctl status myapp
# Se att den är active och inga felmeddelanden

# 5. Kolla loggarna för säkerhets skull
journalctl -u myapp -n 20
# Se att starten gick bra

# Eller som ett script:
#!/bin/bash
deploy_app() {
    echo "Deploying..."
    # ... kopiera filer ...

    sudo systemctl restart myapp
    sleep 2

    if systemctl is-active --quiet myapp; then
        echo "Deploy successful!"
    else
        echo "Deploy FAILED! Check logs:"
        journalctl -u myapp -n 30
        exit 1
    fi
}
```

---

## Key Takeaways

1. **start/stop/restart** = kontrollera tjänster
2. **reload** = läs om config utan nedtid
3. **enable --now** = aktivera + starta
4. **status** = första kommandot vid problem
5. **--failed** = hitta kraschade tjänster
""",
        },
        {
            "title": 'Boot Process and Targets',
            "slug": 'boot-process-targets',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Boot Process and Targets

## Varför behöver du kunna detta?

När en server inte startar behöver du förstå bootprocessen för att felsöka. Var i kedjan fastnade den? BIOS? Bootloader? Kernel? Systemd? Du behöver också förstå targets för att konfigurera vad som ska starta automatiskt och kunna boota till rescue mode för att fixa trasiga system.

---

## Bootprocessen steg för steg

```bash
# Linux boot-sekvens:
#
# 1. BIOS/UEFI
#    - Firmware på moderkortet
#    - Hittar boot-enhet (disk, USB, nätverk)
#    - Laddar bootloader från första sektorn
#
# 2. GRUB (bootloader)
#    - Visar boot-meny
#    - Laddar Linux-kernel och initramfs
#    - Du kan redigera boot-parametrar här
#
# 3. Kernel
#    - Startar och initierar hårdvara
#    - Mountar initramfs som temporärt root
#    - Laddar drivrutiner
#
# 4. Initramfs
#    - Temporärt mini-filsystem i RAM
#    - Innehåller moduler för att mounta riktiga diskar
#    - Överlämnar till riktiga root-filsystemet
#
# 5. Systemd (PID 1)
#    - Tar över från initramfs
#    - Startar tjänster enligt target
#    - Mountar filsystem enligt /etc/fstab
```

---

## Targets - systemds runlevels

Targets ersätter de gamla runlevels. De definierar systemtillstånd.

```bash
systemctl list-units --type=target
# UNIT                   LOAD   ACTIVE DESCRIPTION
# basic.target           loaded active Basic System
# emergency.target       loaded active Emergency Mode
# graphical.target       loaded active Graphical Interface
# multi-user.target      loaded active Multi-User System
# network.target         loaded active Network
# rescue.target          loaded active Rescue Mode
#
# Vanliga targets:
# poweroff.target   - Stäng av (runlevel 0)
# rescue.target     - Single user, minimal system
# multi-user.target - Fullständigt system utan GUI (runlevel 3)
# graphical.target  - Med GUI (runlevel 5)
# reboot.target     - Omstart (runlevel 6)

# Vilket target är default?
systemctl get-default
# multi-user.target
# Detta är vad systemet bootar till

# Ändra default target
sudo systemctl set-default multi-user.target
# Servrar ska vara multi-user
# Skrivbord ska vara graphical
```

---

## Byta target vid körning

```bash
# Byt till rescue mode (single user)
sudo systemctl isolate rescue.target
# Stoppar nästan alla tjänster
# Bara root-shell
# Nätverket är nere
# Användbart för systemunderhåll

# Tillbaka till normalt
sudo systemctl isolate multi-user.target
# Startar alla tjänster igen

# Stäng av
sudo systemctl poweroff
# Samma som: shutdown -h now

# Starta om
sudo systemctl reboot
# Samma som: shutdown -r now
```

---

## GRUB bootloader

```bash
# GRUB-konfiguration
cat /etc/default/grub
# GRUB_DEFAULT=0
# GRUB_TIMEOUT=5
# GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
# GRUB_CMDLINE_LINUX=""
#
# GRUB_DEFAULT = vilken menypost som väljs automatiskt
# GRUB_TIMEOUT = sekunder innan auto-boot
# GRUB_CMDLINE = kernel-parametrar

# Efter ändringar, uppdatera GRUB
sudo update-grub
# eller
sudo grub-mkconfig -o /boot/grub/grub.cfg
# Regenererar GRUB-konfigurationen
```

---

## Emergency och rescue mode

Om systemet inte startar normalt kan du boota till speciella lägen:

```bash
# Vid GRUB-menyn:
# 1. Tryck 'e' för att redigera boot-entry
# 2. Hitta raden som börjar med 'linux'
# 3. Lägg till 'systemd.unit=rescue.target' eller 'single'
# 4. Tryck Ctrl+X för att boota

# Rescue mode
# - Root-shell med lösenord
# - Minimala tjänster
# - Filsystem mountade
# - Nätverket nere

# Emergency mode
# - Ännu mer minimalt
# - Bara root-filsystem mountat (read-only)
# - Används när rescue misslyckas

# Mounta filsystem read-write i emergency
mount -o remount,rw /
# Nu kan du redigera filer
```

---

## Felsök boot-problem

```bash
# Kolla senaste boot
journalctl -b
# Visar alla meddelanden från senaste boot
# Scrolla med piltangenter, q för att avsluta

# Föregående boot
journalctl -b -1
# -1 = förra booten
# -2 = två bootar sedan
# Bra när systemet inte startade senast

# Bara fel och varningar
journalctl -b -p err
# -p err = priority error och värre
# Filtrera bort allt brus

# Bootlog för specifik tjänst
journalctl -b -u nginx
# Varför startade inte nginx vid boot?
```

---

## Praktiskt exempel: Fixa trasigt system

```bash
# Server bootar inte - disk full
# 1. Boota till rescue mode (via GRUB)

# 2. Mounta root-filsystem read-write
mount -o remount,rw /

# 3. Ta reda på vad som tar plats
du -sh /* | sort -rh | head

# 4. Rensa t.ex. gamla loggar
rm -rf /var/log/*.gz
rm -rf /var/log/*.1

# 5. Starta om normalt
reboot
```

---

## Key Takeaways

1. **Boot-sekvens**: BIOS → GRUB → Kernel → initramfs → systemd
2. **Targets** = systemtillstånd (multi-user = server-standard)
3. **set-default** = ändra boot-target
4. **rescue.target** = felsökning med minimal system
5. **journalctl -b** = kolla boot-loggar
""",
        },
        {
            "title": 'Journald and Logging',
            "slug": 'journald-logging',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Journald and Logging

## Varför behöver du kunna detta?

Loggar är dina ögon in i systemet. När något går fel är loggarna första stället du tittar. Som DevOps-ingenjör kommer du spendera mycket tid med journalctl för att förstå varför en tjänst kraschade, vem som loggade in, och vad som hände vid en specifik tidpunkt.

---

## journalctl - det centrala loggverktyget

```bash
journalctl
# Visar alla systemloggar från början
# Scrolla med piltangenter, sök med /
# q för att avsluta (som i less)

journalctl -f
# Follow mode - visar nya loggar i realtid
# Som tail -f men för alla tjänster
# Ctrl+C för att avsluta

journalctl -n 50
# Visa senaste 50 rader
# Bra för snabb överblick
# Default är 10 rader

journalctl --since "1 hour ago"
# Loggar från senaste timmen
# Kan också vara: "yesterday", "today", "2025-01-15 10:00"

journalctl --since "2025-01-15 10:00" --until "2025-01-15 12:00"
# Specifikt tidsintervall
# Perfekt för att undersöka en incident
```

---

## Filtrera efter tjänst

```bash
journalctl -u nginx
# Alla loggar för nginx-tjänsten
# -u = unit (tjänstens namn)

journalctl -u nginx -f
# Follow nginx-loggar i realtid
# Det du använder oftast vid felsökning

journalctl -u nginx -n 100 --no-pager
# Senaste 100 rader utan pager
# --no-pager skriver direkt till terminalen
# Användbart för scripts

journalctl -u nginx -u postgresql
# Flera tjänster samtidigt
# Se hur de interagerar
```

---

## Filtrera efter prioritet

```bash
journalctl -p err
# Bara errors och värre
# Priorities (0 = värst):
# 0 = emerg   - Systemet är oanvändbart
# 1 = alert   - Åtgärd krävs omedelbart
# 2 = crit    - Kritiskt tillstånd
# 3 = err     - Fel
# 4 = warning - Varningar
# 5 = notice  - Normalt men viktigt
# 6 = info    - Informativa meddelanden
# 7 = debug   - Debug-meddelanden

journalctl -p warning
# warning och allt allvarligare (0-4)
# Filtrerar bort info och debug

journalctl -u nginx -p err --since today
# Kombinera filter
# Nginx errors från idag
```

---

## Boot-relaterade loggar

```bash
journalctl -b
# Alla loggar från aktuell boot
# Från det att systemet startade

journalctl -b -1
# Förra booten
# -2 = två bootar sedan
# Användbart om systemet kraschade

journalctl --list-boots
# Lista alla sparade bootar
# IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
#  -1 abc123...                        Mon 2025-01-14 08:00:00 UTC Mon 2025-01-14 23:59:59 UTC
#   0 def456...                        Tue 2025-01-15 00:00:01 UTC Tue 2025-01-15 14:30:00 UTC

journalctl -b -1 -p err
# Errors från förra booten
# Varför startade inte servern igår?
```

---

## Kernel-loggar

```bash
journalctl -k
# Bara kernel-meddelanden
# Hårdvaruproblem, drivrutiner, etc.
# Samma som dmesg men med tidsstämplar

journalctl -k --since "5 minutes ago"
# Senaste kernel-meddelanden
# Vad hände nyss med hårdvaran?
```

---

## Traditionella loggfiler

Förutom journald finns fortfarande klassiska loggfiler i /var/log:

```bash
ls /var/log/
# auth.log      - Inloggningar, sudo
# syslog        - Systemmeddelanden
# kern.log      - Kernel-meddelanden
# nginx/        - Nginx-specifika loggar
# mysql/        - MySQL-loggar
# apt/          - Pakethantering

# Kolla inloggningsförsök
sudo tail -f /var/log/auth.log
# Se SSH-inloggningar och sudo-användning
# Bra för säkerhetsövervakning

# Nginx access log
sudo tail -f /var/log/nginx/access.log
# Se alla HTTP-requests
# IP, tid, URL, status, user-agent

# Nginx error log
sudo tail -f /var/log/nginx/error.log
# Se fel - 404, 500, config-problem
```

---

## Logrotate - hantera loggstorlek

```bash
cat /etc/logrotate.conf
# Hur loggar roteras (arkiveras)
# weekly        - Rotera varje vecka
# rotate 4      - Behåll 4 gamla versioner
# compress      - Komprimera gamla loggar

cat /etc/logrotate.d/nginx
# /var/log/nginx/*.log {
#     daily
#     rotate 14
#     compress
#     delaycompress
#     notifempty
#     create 0640 www-data adm
#     sharedscripts
#     postrotate
#         /bin/kill -USR1 $(cat /var/run/nginx.pid)
#     endscript
# }
#
# daily = rotera varje dag
# rotate 14 = behåll 14 dagar
# compress = gzip gamla filer
# postrotate = kör efter rotation (signalera nginx)
```

---

## Praktiskt exempel: Felsök kraschad tjänst

```bash
# Tjänsten är nere
systemctl status myapp
# Active: failed

# Kolla loggarna
journalctl -u myapp -n 100
# Scrolla och leta efter error-meddelanden

# Filtrera bara errors
journalctl -u myapp -p err --since "1 hour ago"
# Vad gick fel?

# Kolla vid vilken tidpunkt
journalctl -u myapp --since "10:00" --until "10:05"
# Exakt vad hände vid kraschen?
```

---

## Key Takeaways

1. **journalctl -u tjänst** = loggar för specifik tjänst
2. **journalctl -f** = följ loggar i realtid
3. **journalctl -p err** = bara errors
4. **journalctl -b** = loggar från aktuell boot
5. **/var/log/** = traditionella loggfiler
""",
        },
        {
            "title": 'User and Group Management',
            "slug": 'user-group-management',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# User and Group Management

## Varför behöver du kunna detta?

Linux är ett multiuser-system. Du måste kunna skapa användare för olika ändamål - deploy-användare för CI/CD, service-konton för applikationer, och personliga konton för teammedlemmar. Rätt hantering av användare och grupper är grundläggande för säkerhet och åtkomstkontroll.

---

## Skapa användare

```bash
sudo useradd deploy
# Skapar en ny användare "deploy"
# Skapar INTE home directory (!)
# Skapar INTE lösenord
# Användaren kan inte logga in ännu

sudo useradd -m -s /bin/bash deploy
# -m = skapa home directory (/home/deploy)
# -s = ange shell (annars /bin/sh)
# Nu har användaren ett hem och bash-shell

sudo passwd deploy
# Sätt lösenord för användaren
# Du uppmanas skriva lösenordet två gånger

# Eller gör allt på en gång
sudo useradd -m -s /bin/bash -c "Deploy User" devops
# -c = kommentar (ofta fullständigt namn)
```

---

## Förstå användarfilerna

```bash
cat /etc/passwd
# deploy:x:1001:1001:Deploy User:/home/deploy:/bin/bash
#
# Fält separerade med :
# 1. Användarnamn: deploy
# 2. Lösenord: x (betyder att det finns i /etc/shadow)
# 3. UID: 1001 (User ID)
# 4. GID: 1001 (Primary Group ID)
# 5. GECOS: Deploy User (kommentar/namn)
# 6. Home: /home/deploy
# 7. Shell: /bin/bash

sudo cat /etc/shadow
# deploy:$6$xyz...:19377:0:99999:7:::
#
# Här ligger hashade lösenord
# Bara root kan läsa denna fil
# $6$ = SHA-512 hash

cat /etc/group
# deploy:x:1001:
# developers:x:1002:deploy,john,jane
#
# Gruppdefinitioner
# Sista fältet = medlemmar (kommaseparerat)
```

---

## Modifiera användare

```bash
sudo usermod -aG docker deploy
# Lägg till "deploy" i gruppen "docker"
# -a = append (lägg till, ta INTE bort andra grupper)
# -G = supplementary groups
# VIKTIGT: Glöm INTE -a, annars tas alla andra grupper bort!

sudo usermod -s /bin/zsh deploy
# Byt shell till zsh

sudo usermod -L deploy
# Lås kontot (kan inte logga in)
# Sätter ! framför lösenordshash i /etc/shadow

sudo usermod -U deploy
# Lås upp kontot igen

sudo usermod -l newname oldname
# Byt användarnamn
# Home directory ändras INTE automatiskt
```

---

## Grupper

```bash
sudo groupadd developers
# Skapa en ny grupp

sudo usermod -aG developers john
sudo usermod -aG developers jane
# Lägg till användare i gruppen

groups john
# john : john developers docker
# Visar alla grupper john tillhör
# Första = primär grupp

id john
# uid=1001(john) gid=1001(john) groups=1001(john),1002(developers),999(docker)
# Mer detaljerad info

sudo gpasswd -d john developers
# Ta bort john från gruppen developers
# Alternativ till usermod
```

---

## Ta bort användare

```bash
sudo userdel deploy
# Tar bort användaren
# Behåller home directory och filer

sudo userdel -r deploy
# Tar bort användaren OCH home directory
# -r = remove home directory
# VARNING: Data försvinner permanent!

# Säkrare metod:
sudo tar -czvf /backup/deploy_home.tar.gz /home/deploy
sudo userdel -r deploy
# Säkerhetskopiera först, ta bort sedan
```

---

## Service accounts

För applikationer skapar du ofta service accounts utan login-möjlighet:

```bash
sudo useradd -r -s /usr/sbin/nologin myapp
# -r = system account (lågt UID, ingen home)
# -s /usr/sbin/nologin = kan inte logga in
# Perfekt för tjänster som kör som specifik användare

# I systemd service:
# [Service]
# User=myapp
# Group=myapp
```

---

## Lösenordspolicies

```bash
sudo chage -l deploy
# Last password change                    : Jan 15, 2025
# Password expires                        : never
# Account expires                         : never
# Minimum number of days between password change : 0
# Maximum number of days between password change : 99999

sudo chage -M 90 deploy
# Lösenord måste bytas var 90:e dag

sudo chage -E 2025-12-31 contractor
# Kontot upphör 2025-12-31
# Bra för tillfälliga användare
```

---

## Praktiskt exempel: Sätt upp deploy-användare

```bash
# Skapa användaren
sudo useradd -m -s /bin/bash -c "Deployment User" deploy

# Sätt inget lösenord (SSH-nyckel only)
sudo passwd -l deploy

# Lägg till i docker-gruppen (om Docker används)
sudo usermod -aG docker deploy

# Sätt upp SSH-nyckel
sudo mkdir -p /home/deploy/.ssh
sudo touch /home/deploy/.ssh/authorized_keys
sudo chown -R deploy:deploy /home/deploy/.ssh
sudo chmod 700 /home/deploy/.ssh
sudo chmod 600 /home/deploy/.ssh/authorized_keys

# Lägg till public key
echo "ssh-ed25519 AAAA... deploy@ci" | sudo tee -a /home/deploy/.ssh/authorized_keys
```

---

## Key Takeaways

1. **useradd -m -s /bin/bash** = skapa användare med home och shell
2. **usermod -aG grupp user** = lägg till i grupp (glöm inte -a!)
3. **groups user** = visa vilka grupper användaren tillhör
4. **/usr/sbin/nologin** = shell för service accounts
5. **userdel -r** = ta bort användare inklusive home
""",
        },
        {
            "title": 'Sudo Configuration',
            "slug": 'sudo-configuration',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Sudo Configuration

## Varför behöver du kunna detta?

sudo är hur användare får tillfällig root-access på Linux. Rätt konfigurerad sudo ger dig kontroll över vem som kan göra vad, med fullständig audit trail. Fel konfigurerad sudo är en säkerhetsrisk. Som DevOps måste du förstå hur man ger just tillräckligt med rättigheter - inte mer, inte mindre.

---

## Grundläggande sudo

```bash
sudo apt update
# Kör apt update som root
# Frågar efter DITT lösenord (inte roots)
# Loggas i /var/log/auth.log

sudo -i
# Öppna ett root-shell (som su -)
# Behåller sudo:s audit trail
# exit för att återgå

sudo -u postgres psql
# Kör kommando som annan användare
# -u = vilken användare
# Användbart för databashantering

sudo -l
# Lista vad du får göra med sudo
# User john may run the following commands:
#     (ALL) ALL
# eller
#     (ALL) NOPASSWD: /usr/bin/systemctl restart nginx
```

---

## visudo - redigera sudoers

```bash
sudo visudo
# ENDA rätta sättet att redigera /etc/sudoers
# Kontrollerar syntax innan sparning
# Förhindrar att du låser ut dig själv

# NIR ALDRIG redigera /etc/sudoers direkt!
# Om filen blir korrupt kan ingen köra sudo
```

---

## sudoers syntax

```bash
# /etc/sudoers format:
# vem    var=(som vem)  vad

# Exempel:
john    ALL=(ALL)       ALL
# john kan köra allt, på alla maskiner, som alla användare

%admin  ALL=(ALL)       ALL
# Alla i gruppen admin (% = grupp)

deploy  ALL=(ALL)       NOPASSWD: ALL
# deploy behöver inte skriva lösenord
# FARLIGT! Använd bara för automation

deploy  ALL=(ALL)       NOPASSWD: /usr/bin/systemctl restart nginx
# deploy kan BARA starta om nginx utan lösenord
# SÄKRARE - begränsa till specifika kommandon
```

---

## Fil i /etc/sudoers.d/

Bättre än att ändra i /etc/sudoers är att skapa egna filer:

```bash
sudo visudo -f /etc/sudoers.d/deploy
# Skapa en fil för deploy-användaren

# Innehåll:
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status myapp

# Kontrollera att /etc/sudoers har:
# @includedir /etc/sudoers.d
# (finns där som default på moderna system)
```

---

## Praktiska exempel

```bash
# CI/CD deploy-användare
sudo visudo -f /etc/sudoers.d/deploy
# deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
# deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status myapp

# Docker-access utan sudo (bättre alternativ)
sudo usermod -aG docker deploy
# Istället för sudo docker, lägg användaren i docker-gruppen

# Ge grupp sudo-access
sudo visudo -f /etc/sudoers.d/developers
# %developers ALL=(ALL) ALL
# Alla i developers-gruppen får sudo med lösenord
```

---

## Säkerhetsaspekter

```bash
# Loggar
sudo grep sudo /var/log/auth.log
# Jan 15 10:30:00 server sudo: john : TTY=pts/0 ; PWD=/home/john ; USER=root ; COMMAND=/usr/bin/apt update
# Alla sudo-kommandon loggas

# Defaults i sudoers
Defaults        logfile="/var/log/sudo.log"
# Separat loggfil för sudo

Defaults        timestamp_timeout=5
# Fråga om lösenord igen efter 5 minuter inaktivitet

Defaults        requiretty
# Kräv terminal (skyddar mot vissa attacker)
```

---

## Felsökning

```bash
# Syntaxfel i sudoers
sudo visudo -c
# /etc/sudoers: parsed OK
# /etc/sudoers.d/deploy: parsed OK

# Om du låst ut dig själv:
# 1. Starta om i recovery mode
# 2. Eller använd root-konto (om tillgängligt)
# 3. Fixa /etc/sudoers

# Kolla om användare är i sudo-grupp
groups username
id username
# Se om sudo eller wheel finns med
```

---

## Key Takeaways

1. **visudo** = ENDA sättet att redigera sudoers
2. **/etc/sudoers.d/** = lägg egna regler i separata filer
3. **NOPASSWD:** = bara för specifika kommandon, inte ALL
4. **%grupp** = ge sudo till en hel grupp
5. **sudo -l** = se vad du får göra
""",
        },
        {
            "title": 'PAM Modules',
            "slug": 'pam-modules',
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 85,
            "content": """# PAM Modules

PAM står för Pluggable Authentication Modules. Tänk på det som ett modulsystem för autentisering där Linux kan plugga in olika sätt att verifiera användare. Istället för att varje program (login, ssh, sudo) ska ha sin egen autentiseringskod, så delegerar de till PAM som sköter allt på ett ställe.

Det smarta med PAM är att du kan stapla moduler på varandra. En användare kan behöva lösenord OCH ha rätt IP OCH logga in under rätt tider. PAM låter dig bygga dessa kedjor av krav utan att röra programmen själva.

---

## Hur PAM fungerar

När ett program vill autentisera en användare frågar det PAM. PAM tittar i sin konfiguration och kör igenom alla moduler som är definierade. Varje modul svarar "ja", "nej" eller "skippa mig", och PAM sammanställer resultatet.

```bash
# Visa vilka PAM-moduler som finns installerade
ls -la /lib/security/                # modulfilerna finns här som .so-filer

# Eller på vissa system
ls -la /lib/x86_64-linux-gnu/security/   # debian/ubuntu lägger dem här

# Visa PAM-konfiguration för olika tjänster
ls -la /etc/pam.d/                   # varje fil = en tjänst (sshd, sudo, login, etc)

# Läs konfigurationen för sudo
cat /etc/pam.d/sudo                  # visar vilka moduler sudo använder
```

---

## PAM-konfigurationsformat

Varje rad i en PAM-fil har fyra delar: typ, kontrollflagga, modul och argument.

```bash
# Titta på login-konfigurationen
cat /etc/pam.d/login

# Formatet är:
# typ       kontrollflagga    modul                 argument
# auth      required          pam_unix.so           nullok
# account   required          pam_unix.so
# password  required          pam_unix.so           sha512
# session   required          pam_unix.so
```

De fyra typerna är:

- **auth** - kollar vem användaren är (lösenord, fingeravtryck, etc)
- **account** - kollar om kontot får användas (utgånget? låst?)
- **password** - hanterar lösenordsändringar
- **session** - saker som ska ske vid login/logout (mount home, sätt miljövariabler)

---

## Kontrollflaggor

Kontrollflaggan bestämmer vad som händer om en modul lyckas eller misslyckas:

```bash
# Visa common-auth för att se typiska kontrollflaggor
cat /etc/pam.d/common-auth

# Förklaring av flaggorna:
# required    - måste lyckas, men fortsätt köra resten av modulerna ändå
# requisite   - måste lyckas, avbryt direkt vid fel
# sufficient  - om denna lyckas, skippa resten (om inget required misslyckat tidigare)
# optional    - spelar ingen roll om den lyckas eller misslyckas
# include     - inkludera en annan PAM-fil
```

Tänk på det som en kedja av vakter. "required" betyder att vakten måste släppa igenom dig, men nästa vakt får ändå titta. "requisite" betyder att om vakten säger nej så blir du utslängd direkt.

---

## Vanliga PAM-moduler

```bash
# pam_unix.so - standard Unix-autentisering (kollar /etc/passwd och /etc/shadow)
# pam_deny.so - nekar alltid, används för att blockera
# pam_permit.so - tillåter alltid, används för tjänster som inte behöver auth
# pam_wheel.so - kräver att användaren är medlem i wheel-gruppen
# pam_limits.so - sätter resursbegränsningar (ulimit)
# pam_env.so - sätter miljövariabler vid login

# Se vilken modul som används var
grep -r "pam_unix" /etc/pam.d/       # hitta alla användningar av pam_unix
grep -r "pam_wheel" /etc/pam.d/      # hitta var pam_wheel används
```

---

## Begränsa sudo till wheel-gruppen

Ett klassiskt sätt att begränsa vem som får köra sudo är att kräva medlemskap i wheel-gruppen:

```bash
# Redigera sudo PAM-konfiguration
sudo nano /etc/pam.d/sudo

# Lägg till denna rad i början (efter eventuella includes):
# auth       required     pam_wheel.so use_uid

# use_uid betyder att den kollar användarens riktiga UID, inte effektiva
```

Efter denna ändring måste användare vara medlemmar i wheel-gruppen för att kunna använda sudo, även om de finns i sudoers.

---

## Lösenordspolicy med PAM

Du kan sätta krav på hur lösenord ska se ut:

```bash
# På Debian/Ubuntu, redigera common-password
cat /etc/pam.d/common-password

# Modulen pam_pwquality.so (eller pam_cracklib.so på äldre system) hanterar detta
# Exempel på konfiguration:
# password  requisite  pam_pwquality.so retry=3 minlen=12 difok=3 ucredit=-1 lcredit=-1 dcredit=-1

# retry=3    - användaren får 3 försök att ange ett godkänt lösenord
# minlen=12  - minst 12 tecken
# difok=3    - minst 3 tecken måste skilja från gamla lösenordet
# ucredit=-1 - kräv minst 1 versal (-1 betyder "kräv minst 1")
# lcredit=-1 - kräv minst 1 gemen
# dcredit=-1 - kräv minst 1 siffra
```

---

## Session-begränsningar med pam_limits

pam_limits.so läser från /etc/security/limits.conf för att sätta resursbegränsningar:

```bash
# Visa nuvarande limits-konfiguration
cat /etc/security/limits.conf

# Formatet är:
# domän        typ      objekt    värde
# @developers  soft     nproc     1000
# @developers  hard     nproc     2000
# *            soft     nofile    4096
# *            hard     nofile    8192

# domän kan vara användarnamn, @gruppnamn eller * för alla
# typ är soft (varning) eller hard (absolut gräns)
# vanliga objekt: nproc (processer), nofile (öppna filer), maxlogins

# Kolla att pam_limits är aktiverad för login
grep pam_limits /etc/pam.d/common-session
```

---

## Felsökning av PAM

När PAM-autentisering misslyckas loggas det till syslog:

```bash
# Se PAM-relaterade loggmeddelanden
sudo grep -i pam /var/log/auth.log       # Debian/Ubuntu
sudo grep -i pam /var/log/secure         # RHEL/CentOS

# Vanliga felmeddelanden:
# "authentication failure" - fel lösenord eller blockerad modul
# "account expired" - kontot har gått ut
# "Permission denied" - pam_wheel eller liknande blockerade

# Testa PAM-konfiguration utan att låsa ut dig
# VARNING: ha alltid en root-terminal öppen som backup!
pamtester sudo dinuser authenticate      # testa sudo-autentisering
```

---

## Praktiskt exempel: Begränsa SSH-inloggning

Låt oss säga att du bara vill tillåta användare i gruppen "sshusers" att logga in via SSH:

```bash
# Skapa gruppen om den inte finns
sudo groupadd sshusers                   # skapa gruppen sshusers

# Lägg till tillåtna användare
sudo usermod -aG sshusers alice          # lägg till alice i gruppen
sudo usermod -aG sshusers bob            # lägg till bob i gruppen

# Redigera PAM-konfigurationen för sshd
sudo nano /etc/pam.d/sshd

# Lägg till denna rad tidigt i filen (efter auth includes):
# auth       required     pam_succeed_if.so user ingroup sshusers

# pam_succeed_if.so kollar ett villkor och lyckas om det stämmer
# "user ingroup sshusers" = användaren måste vara i gruppen sshusers
```

---

## Key Takeaways

**PAM-strukturen** - Konfiguration finns i /etc/pam.d/ med en fil per tjänst. Modulerna är .so-filer i /lib/security/. Varje rad har typ, kontrollflagga, modul och argument.

**De fyra typerna** - auth (vem är du?), account (får kontot användas?), password (lösenordsändring), session (vid login/logout).

**Kontrollflaggor** - required (måste lyckas, kör vidare), requisite (måste lyckas, avbryt vid fel), sufficient (lyckas = klart), optional (spelar ingen roll).

**Vanliga säkerhetsåtgärder** - pam_wheel.so för att begränsa sudo till wheel-gruppen, pam_pwquality.so för lösenordspolicy, pam_limits.so för resursbegränsningar.

**Felsökning** - Loggarna i /var/log/auth.log visar PAM-fel. Ha alltid en backup-root-terminal öppen när du ändrar PAM-konfiguration.
""",
        },
        {
            "title": 'SSH Hardening',
            "slug": 'ssh-hardening',
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# SSH Hardening

SSH är dörren till din server. Varje Linux-server som är exponerad mot internet bombarderas konstant av automatiska inloggningsförsök. Utan rätt konfiguration är det bara en tidsfråga innan någon gissar rätt lösenord. SSH hardening handlar om att göra den dörren så svår att forcera som möjligt.

Tänk på det som att säkra ingången till ditt hus. Du vill inte bara ha ett lås, du vill ha flera lås, en kamera, och kanske till och med flytta dörren så tjuvarna inte ens hittar den.

---

## SSH-konfigurationsfilen

All SSH-serverkonfiguration finns i /etc/ssh/sshd_config:

```bash
# Visa nuvarande konfiguration
cat /etc/ssh/sshd_config             # hela filen med alla inställningar

# Visa bara aktiva rader (inte kommentarer)
grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"   # filtrera bort tomma och kommentarer

# Innan du ändrar något, ta en backup
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup   # alltid backup först!
```

---

## Steg 1: Byt port (security through obscurity)

Att byta SSH-port stoppar inte en målmedveten angripare, men det minskar 99% av automatiska attacker:

```bash
# Redigera sshd_config
sudo nano /etc/ssh/sshd_config

# Ändra eller lägg till:
# Port 2222

# Du kan ha flera portar aktiva samtidigt under övergången:
# Port 22
# Port 2222

# Testa konfigurationen innan du applicerar
sudo sshd -t                         # -t = test mode, visar syntax-fel

# Starta om SSH-tjänsten
sudo systemctl restart sshd          # applicera ändringar

# Glöm inte öppna nya porten i brandväggen!
sudo ufw allow 2222/tcp              # om du kör ufw
```

---

## Steg 2: Inaktivera root-login

Root-kontot är första målet för angripare. Inaktivera SSH-login för root:

```bash
# I /etc/ssh/sshd_config, sätt:
# PermitRootLogin no

# Om du fortfarande behöver root-åtkomst ibland:
# PermitRootLogin prohibit-password

# "prohibit-password" tillåter endast nyckel-baserad login för root
# "no" blockerar root helt (rekommenderat)

# Verifiera att du har ett annat konto med sudo-rättigheter först!
sudo grep "^sudo" /etc/group         # se vilka som har sudo-access
```

---

## Steg 3: Nyckelbaserad autentisering

SSH-nycklar är både säkrare och smidigare än lösenord:

```bash
# PÅ DIN LOKALA DATOR - generera ett nyckelpar
ssh-keygen -t ed25519 -C "din.email@example.com"   # ed25519 är modernast och säkrast

# Du kan också använda RSA med stor nyckel
ssh-keygen -t rsa -b 4096 -C "din.email@example.com"  # -b 4096 = 4096 bitar

# Kopiera din publika nyckel till servern
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server   # enklaste sättet

# Eller manuellt - på servern:
mkdir -p ~/.ssh                      # skapa .ssh-mappen om den inte finns
chmod 700 ~/.ssh                     # bara ägaren får läsa
nano ~/.ssh/authorized_keys          # klistra in din publika nyckel här
chmod 600 ~/.ssh/authorized_keys     # bara ägaren får läsa/skriva
```

---

## Steg 4: Inaktivera lösenordsautentisering

När nycklar fungerar, stäng av lösenord helt:

```bash
# VIKTIGT: Testa att nyckel-login fungerar FÖRST
# Ha en backup-session öppen ifall något går fel!

# I /etc/ssh/sshd_config:
# PasswordAuthentication no
# PubkeyAuthentication yes
# ChallengeResponseAuthentication no

# Testa och starta om
sudo sshd -t                         # verifiera syntax
sudo systemctl restart sshd          # applicera ändringar

# Testa från en NY terminal (stäng inte den gamla!)
ssh -i ~/.ssh/id_ed25519 user@server   # explicit ange nyckel för att testa
```

---

## Steg 5: Begränsa vilka som får logga in

Du kan explicit ange vilka användare eller grupper som får SSH-åtkomst:

```bash
# I /etc/ssh/sshd_config, lägg till:
# AllowUsers alice bob deploy
# Endast dessa tre användare kan logga in via SSH

# Eller begränsa per grupp:
# AllowGroups sshusers admins
# Endast medlemmar i dessa grupper får logga in

# Du kan kombinera med IP-begränsningar:
# AllowUsers alice@192.168.1.* bob@10.0.0.*
# alice kan bara logga in från 192.168.1.x-nätverket

# Det finns även DenyUsers och DenyGroups för blocklisting
```

---

## Steg 6: Ytterligare säkerhetsinställningar

```bash
# I /etc/ssh/sshd_config, överväg dessa inställningar:

# MaxAuthTries 3
# Begränsa antal inloggningsförsök per session

# LoginGraceTime 60
# Hur länge (sekunder) en användare har på sig att logga in

# ClientAliveInterval 300
# ClientAliveCountMax 2
# Koppla bort inaktiva sessioner efter 10 minuter (300*2 sekunder)

# X11Forwarding no
# Stäng av X11-forwarding om du inte behöver det

# AllowTcpForwarding no
# Stäng av port forwarding om du inte behöver det

# Protocol 2
# Tvinga SSH version 2 (version 1 är osäker)
```

---

## Fail2ban - Automatisk blockering

Fail2ban övervakar loggfiler och blockerar IP-adresser som gör för många misslyckade inloggningsförsök:

```bash
# Installera fail2ban
sudo apt install fail2ban            # Debian/Ubuntu
sudo dnf install fail2ban            # RHEL/Fedora

# Skapa lokal konfiguration (ändra aldrig jail.conf direkt)
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local   # lokal fil åsidosätter

# Redigera jail.local
sudo nano /etc/fail2ban/jail.local

# Aktivera SSH-skydd:
# [sshd]
# enabled = true
# port = ssh,2222
# filter = sshd
# logpath = /var/log/auth.log
# maxretry = 3
# bantime = 3600
# findtime = 600

# maxretry = 3 fel inom findtime = 600 sekunder = ban i bantime = 3600 sekunder

# Starta fail2ban
sudo systemctl enable fail2ban       # starta vid boot
sudo systemctl start fail2ban        # starta nu

# Se status
sudo fail2ban-client status sshd     # visa aktuella bans för SSH
```

---

## Komplett säker sshd_config

Här är ett exempel på en härdad konfiguration:

```bash
# Visa exempel på säker konfiguration
cat << 'EOF'
# /etc/ssh/sshd_config - Hardened configuration

Port 2222
Protocol 2

# Authentication
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no

# Authorization
AllowGroups sshusers

# Limits
MaxAuthTries 3
MaxSessions 2
LoginGraceTime 60
ClientAliveInterval 300
ClientAliveCountMax 2

# Security
X11Forwarding no
AllowTcpForwarding no
AllowAgentForwarding no
PermitUserEnvironment no

# Logging
LogLevel VERBOSE
EOF
```

---

## Verifiera din SSH-säkerhet

```bash
# Kolla vilken port SSH lyssnar på
sudo ss -tlnp | grep sshd            # visa SSH-lyssnande sockets

# Kontrollera SSH-konfiguration
sudo sshd -T                         # visa effektiv konfiguration

# Se misslyckade inloggningsförsök
sudo grep "Failed password" /var/log/auth.log | tail -20   # senaste 20 misslyckade

# Se lyckade inloggningar
sudo grep "Accepted" /var/log/auth.log | tail -10          # senaste 10 lyckade

# Kolla fail2ban-status
sudo fail2ban-client status sshd     # visa bannade IP-adresser
```

---

## Key Takeaways

**Nyckelbaserad autentisering** - Byt från lösenord till SSH-nycklar. Generera med ssh-keygen, kopiera med ssh-copy-id, inaktivera sedan PasswordAuthentication.

**Inaktivera root-login** - Sätt PermitRootLogin no och använd istället ett vanligt konto med sudo-rättigheter.

**Begränsa åtkomst** - Använd AllowUsers eller AllowGroups för att explicit ange vem som får logga in via SSH.

**Fail2ban** - Installera och konfigurera fail2ban för att automatiskt blockera IP-adresser som gör upprepade misslyckade inloggningsförsök.

**Testa innan du applicerar** - Kör alltid sshd -t för att verifiera konfigurationen. Ha en backup-session öppen när du ändrar SSH-inställningar så du inte låser ut dig själv.
""",
        },
        {
            "title": 'Firewall Basics (ufw, iptables)',
            "slug": 'firewall-basics',
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Firewall Basics (ufw, iptables)

En brandvägg är som en vakt vid varje dörr till din server. Den bestämmer vilken trafik som får komma in och vilken som får gå ut. Utan brandvägg är alla portar öppna för vem som helst på internet att försöka ansluta till.

Tänk på det som ett hus med hundra dörrar. Utan brandvägg står alla dörrar vidöppna. Med brandvägg låser du alla utom de du aktivt vill ha öppna.

---

## UFW - Uncomplicated Firewall

UFW är ett användarvänligt gränssnitt till iptables. Det är standard på Ubuntu och perfekt för de flesta användningsfall:

```bash
# Installera UFW om det saknas
sudo apt install ufw                 # Debian/Ubuntu

# Kolla status
sudo ufw status                      # visar om brandväggen är aktiv
sudo ufw status verbose              # mer detaljerad status
sudo ufw status numbered             # visar regler med nummer (för borttagning)
```

---

## Grundläggande UFW-konfiguration

Innan du aktiverar brandväggen, se till att tillåta SSH så du inte låser ut dig:

```bash
# VIKTIGT: Tillåt SSH FÖRST innan du aktiverar brandväggen
sudo ufw allow ssh                   # tillåter port 22

# Eller om du kör SSH på annan port
sudo ufw allow 2222/tcp              # tillåter port 2222 för TCP

# Sätt default policies
sudo ufw default deny incoming       # neka all inkommande trafik som standard
sudo ufw default allow outgoing      # tillåt all utgående trafik som standard

# Aktivera brandväggen
sudo ufw enable                      # slå på brandväggen

# Du kan alltid inaktivera den om något går fel
sudo ufw disable                     # stäng av brandväggen
```

---

## UFW-regler för vanliga tjänster

```bash
# Webbtrafik
sudo ufw allow http                  # tillåter port 80
sudo ufw allow https                 # tillåter port 443
sudo ufw allow 'Nginx Full'          # tillåter både 80 och 443 för Nginx

# Databasportar (var försiktig med dessa!)
sudo ufw allow 5432/tcp              # PostgreSQL
sudo ufw allow 3306/tcp              # MySQL
sudo ufw allow 27017/tcp             # MongoDB

# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100    # tillåt all trafik från denna IP
sudo ufw allow from 192.168.1.0/24   # tillåt hela subnätet

# Tillåt specifik port från specifik IP
sudo ufw allow from 192.168.1.100 to any port 22   # SSH bara från denna IP

# Tillåt portintervall
sudo ufw allow 6000:6007/tcp         # tillåt TCP-portar 6000-6007
```

---

## Ta bort UFW-regler

```bash
# Visa regler med nummer
sudo ufw status numbered             # visar regler som [1], [2], etc

# Ta bort regel med nummer
sudo ufw delete 3                    # tar bort regel nummer 3

# Eller ta bort genom att upprepa regeln med "delete"
sudo ufw delete allow http           # tar bort regeln som tillåter port 80
sudo ufw delete allow from 192.168.1.100   # tar bort IP-baserad regel

# Återställ alla regler
sudo ufw reset                       # tar bort ALLA regler, inaktiverar brandväggen
```

---

## iptables - Den kraftfulla grunden

UFW är egentligen ett gränssnitt till iptables. För mer avancerade scenarier behöver du förstå iptables direkt:

```bash
# Visa alla iptables-regler
sudo iptables -L                     # lista alla regler
sudo iptables -L -n                  # numeriska portar (snabbare)
sudo iptables -L -v                  # verbose med byte/paket-räknare
sudo iptables -L -n -v --line-numbers   # allt på en gång

# iptables har tre huvudsakliga "chains":
# INPUT   - trafik som kommer IN till servern
# OUTPUT  - trafik som går UT från servern
# FORWARD - trafik som passerar GENOM servern (routing)
```

---

## iptables-regler

```bash
# Grundläggande syntax:
# iptables -A CHAIN -p protokoll --dport port -j ACTION
# -A = append (lägg till i slutet)
# -I = insert (lägg till i början)
# -p = protokoll (tcp, udp, icmp)
# --dport = destination port
# -j = jump (vad som ska hända: ACCEPT, DROP, REJECT)

# Tillåt SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # acceptera SSH

# Tillåt HTTP och HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # acceptera HTTP
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # acceptera HTTPS

# Tillåt etablerade anslutningar
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT   # viktigt!

# Tillåt loopback (localhost)
sudo iptables -A INPUT -i lo -j ACCEPT               # tillåt trafik på lo-interface

# Droppa allt annat (sätt som sista regel)
sudo iptables -A INPUT -j DROP                       # neka allt som inte matchat
```

---

## iptables - Ta bort och spara regler

```bash
# Visa regler med radnummer
sudo iptables -L INPUT --line-numbers   # visa INPUT-chain med nummer

# Ta bort specifik regel
sudo iptables -D INPUT 3                # ta bort regel 3 från INPUT

# Ta bort alla regler (flush)
sudo iptables -F                        # VARNING: rensar ALLT

# Spara regler permanent (Debian/Ubuntu)
sudo apt install iptables-persistent    # installera för automatisk restore
sudo netfilter-persistent save          # spara nuvarande regler
sudo netfilter-persistent reload        # ladda sparade regler

# På RHEL/CentOS
sudo service iptables save              # spara till /etc/sysconfig/iptables
```

---

## Praktiskt exempel: Webbserver-brandvägg

Här är en komplett brandväggskonfiguration för en webbserver:

```bash
# Med UFW (enklast)
sudo ufw default deny incoming       # neka all inkommande
sudo ufw default allow outgoing      # tillåt all utgående
sudo ufw allow ssh                   # tillåt SSH (port 22)
sudo ufw allow http                  # tillåt HTTP (port 80)
sudo ufw allow https                 # tillåt HTTPS (port 443)
sudo ufw enable                      # aktivera

# Verifiera
sudo ufw status verbose              # kolla att allt ser rätt ut
```

Samma sak med iptables:

```bash
# Rensa befintliga regler först
sudo iptables -F                     # flush alla regler

# Tillåt loopback
sudo iptables -A INPUT -i lo -j ACCEPT   # localhost måste fungera

# Tillåt etablerade anslutningar
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Tillåt SSH, HTTP, HTTPS
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Neka allt annat
sudo iptables -A INPUT -j DROP

# Spara permanent
sudo netfilter-persistent save       # på Debian/Ubuntu med iptables-persistent
```

---

## Felsökning av brandväggsregler

```bash
# Testa om en port är öppen utifrån
nc -zv server.example.com 80         # testa port 80

# Se vilka portar som lyssnar på servern
sudo ss -tulnp                       # visa alla lyssnande portar

# Kolla brandväggsregler
sudo ufw status                      # UFW
sudo iptables -L -n -v               # iptables

# Tillfälligt inaktivera brandväggen för test (BARA för felsökning!)
sudo ufw disable                     # stäng av UFW
# Kom ihåg att slå på den igen: sudo ufw enable

# Logga droppade paket för debugging
sudo ufw logging on                  # aktivera loggning
sudo tail -f /var/log/ufw.log        # följ brandväggsloggen
```

---

## Vanliga misstag att undvika

```bash
# MISSTAG 1: Aktivera brandvägg innan SSH är tillåten
# LÖSNING: Alltid "ufw allow ssh" INNAN "ufw enable"

# MISSTAG 2: Glömma att tillåta etablerade anslutningar med iptables
# LÖSNING: Lägg alltid till:
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# MISSTAG 3: Blockera loopback-interface
# LÖSNING: Tillåt alltid localhost:
sudo iptables -A INPUT -i lo -j ACCEPT

# MISSTAG 4: Glömma att spara iptables-regler
# LÖSNING: Reglerna försvinner vid omstart! Spara dem:
sudo netfilter-persistent save
```

---

## firewalld (RHEL/CentOS/Fedora)

På Red Hat-baserade system är firewalld standard istället för UFW:

```bash
# Kolla status
sudo firewall-cmd --state            # visar om firewalld kör
sudo firewall-cmd --list-all         # visa alla regler

# Tillåt tjänster
sudo firewall-cmd --add-service=ssh --permanent    # tillåt SSH permanent
sudo firewall-cmd --add-service=http --permanent   # tillåt HTTP permanent
sudo firewall-cmd --add-service=https --permanent  # tillåt HTTPS permanent

# Tillåt specifik port
sudo firewall-cmd --add-port=8080/tcp --permanent  # tillåt port 8080

# Ladda om efter ändringar
sudo firewall-cmd --reload           # applicera permanenta ändringar

# Ta bort regel
sudo firewall-cmd --remove-service=http --permanent   # ta bort HTTP
sudo firewall-cmd --reload                            # applicera
```

---

## Key Takeaways

**UFW för enkelhet** - På Ubuntu/Debian är UFW enklast. Alltid "allow ssh" innan "enable". Default deny incoming, allow outgoing är en bra utgångspunkt.

**iptables för kontroll** - UFW är ett gränssnitt till iptables. För avancerade scenarier, lär dig iptables chains (INPUT, OUTPUT, FORWARD) och actions (ACCEPT, DROP, REJECT).

**Etablerade anslutningar** - Med iptables, glöm aldrig att tillåta ESTABLISHED,RELATED så att svar på utgående förfrågningar kommer tillbaka.

**Spara regler** - iptables-regler försvinner vid omstart. Använd iptables-persistent eller netfilter-persistent för att spara dem permanent.

**Felsökning** - "ss -tulnp" visar lyssnande portar, "nc -zv" testar om portar är nåbara utifrån. Aktivera brandväggsloggning vid problem.
""",
        },
    ],
}
