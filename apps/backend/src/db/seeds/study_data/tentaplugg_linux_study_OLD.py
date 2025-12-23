"""
Tentaplugg Linux - Study Data
==============================

Flashcards och Quiz för DOE25 Linux-tentan.
100 flashcards per nod, 150 quiz per nod.

16 noder totalt:
1. Subnetting & Nätverk
2. Filsystem & Grundkommandon
3. Bash Scripting Grund
4. Bash Scripting Avancerat
5. Användare & Rättigheter
6. SSH & Säkerhet
7. Firewall
8. Docker Basics
9. Docker Compose
10. Systemd
11. grep, sed, awk
12. Regex
13. Arrays & Parameter Expansion
14. Dockerfile & Docker Build
15. Git
16. Backup & Arkivering
"""

TENTAPLUGG_LINUX_STUDY = {
    "module_slug": "tentaplugg-linux",
    "module_title": "Tentaplugg Linux",
    "module_description": "Komplett tentaförberedelse för DOE25 Linux-kursen",
    "icon": "GraduationCap",
    # =========================================================================
    # FLASHCARDS - TENTA-STIL (korta, direkta, praktiska)
    # =========================================================================
    "flashcards": {
        # =====================================================================
        # NOD 1: SUBNETTING & NÄTVERK
        # =====================================================================
        "nod1_subnetting": [
            # LÅDMETODEN
            {
                "front": "Lådmetoden - vilka 8 värden?",
                "back": "128 | 64 | 32 | 16 | 8 | 4 | 2 | 1",
            },
            {"front": "Block size för /24?", "back": "256"},
            {"front": "Block size för /25?", "back": "128"},
            {"front": "Block size för /26?", "back": "64"},
            {"front": "Block size för /27?", "back": "32"},
            {"front": "Block size för /28?", "back": "16"},
            {"front": "Block size för /29?", "back": "8"},
            {"front": "Block size för /30?", "back": "4"},
            # ANTAL HOSTS
            {"front": "Hosts i /24?", "back": "254"},
            {"front": "Hosts i /25?", "back": "126"},
            {"front": "Hosts i /26?", "back": "62"},
            {"front": "Hosts i /27?", "back": "30"},
            {"front": "Hosts i /28?", "back": "14"},
            {"front": "Hosts i /29?", "back": "6"},
            {"front": "Hosts i /30?", "back": "2"},
            # SUBNÄTMASKER
            {"front": "Subnätmask /24?", "back": "255.255.255.0"},
            {"front": "Subnätmask /25?", "back": "255.255.255.128"},
            {"front": "Subnätmask /26?", "back": "255.255.255.192"},
            {"front": "Subnätmask /27?", "back": "255.255.255.224"},
            {"front": "Subnätmask /28?", "back": "255.255.255.240"},
            {"front": "Subnätmask /29?", "back": "255.255.255.248"},
            {"front": "Subnätmask /30?", "back": "255.255.255.252"},
            # FORMLER
            {"front": "Formel: antal host-bitar?", "back": "32 - prefix"},
            {"front": "Formel: antal hosts?", "back": "2^(host-bitar) - 2"},
            {"front": "Formel: First Host?", "back": "Network ID + 1"},
            {"front": "Formel: Last Host?", "back": "Broadcast - 1"},
            # BERÄKNINGSÖVNINGAR (det som kommer på tentan!)
            {"front": "Network ID för 192.168.1.100/26?", "back": "192.168.1.64"},
            {"front": "Broadcast för 192.168.1.100/26?", "back": "192.168.1.127"},
            {"front": "First Host för 192.168.1.100/26?", "back": "192.168.1.65"},
            {"front": "Last Host för 192.168.1.100/26?", "back": "192.168.1.126"},
            {"front": "Network ID för 192.168.1.200/26?", "back": "192.168.1.192"},
            {"front": "Broadcast för 192.168.1.200/26?", "back": "192.168.1.255"},
            {"front": "First Host för 192.168.1.200/26?", "back": "192.168.1.193"},
            {"front": "Last Host för 192.168.1.200/26?", "back": "192.168.1.254"},
            {"front": "Network ID för 192.168.1.50/27?", "back": "192.168.1.32"},
            {"front": "Broadcast för 192.168.1.50/27?", "back": "192.168.1.63"},
            {"front": "Network ID för 192.168.1.100/27?", "back": "192.168.1.96"},
            {"front": "Broadcast för 192.168.1.100/27?", "back": "192.168.1.127"},
            {"front": "Network ID för 10.0.0.50/28?", "back": "10.0.0.48"},
            {"front": "Broadcast för 10.0.0.50/28?", "back": "10.0.0.63"},
            {"front": "Network ID för 10.0.0.100/28?", "back": "10.0.0.96"},
            {"front": "Broadcast för 10.0.0.100/28?", "back": "10.0.0.111"},
            {"front": "Network ID för 10.0.0.50/29?", "back": "10.0.0.48"},
            {"front": "Broadcast för 10.0.0.50/29?", "back": "10.0.0.55"},
            {"front": "Network ID för 172.16.5.250/29?", "back": "172.16.5.248"},
            {"front": "Broadcast för 172.16.5.250/29?", "back": "172.16.5.255"},
            {"front": "Network ID för 192.168.10.67/30?", "back": "192.168.10.64"},
            {"front": "Broadcast för 192.168.10.67/30?", "back": "192.168.10.67"},
            {"front": "Network ID för 10.10.10.100/25?", "back": "10.10.10.0"},
            {"front": "Broadcast för 10.10.10.100/25?", "back": "10.10.10.127"},
            {"front": "Network ID för 10.10.10.200/25?", "back": "10.10.10.128"},
            {"front": "Broadcast för 10.10.10.200/25?", "back": "10.10.10.255"},
            # FLER ÖVNINGAR
            {"front": "Network ID för 192.168.5.130/26?", "back": "192.168.5.128"},
            {"front": "Network ID för 172.16.0.45/28?", "back": "172.16.0.32"},
            {"front": "Network ID för 10.0.0.200/27?", "back": "10.0.0.192"},
            {"front": "Network ID för 192.168.1.15/29?", "back": "192.168.1.8"},
            {"front": "Network ID för 10.10.10.77/30?", "back": "10.10.10.76"},
            {"front": "Broadcast för 192.168.5.130/26?", "back": "192.168.5.191"},
            {"front": "Broadcast för 172.16.0.45/28?", "back": "172.16.0.47"},
            {"front": "Broadcast för 10.0.0.200/27?", "back": "10.0.0.223"},
            {"front": "Broadcast för 192.168.1.15/29?", "back": "192.168.1.15"},
            {"front": "Broadcast för 10.10.10.77/30?", "back": "10.10.10.79"},
            # PRAKTISKA FRÅGOR
            {"front": "Behöver 50 hosts - vilket prefix?", "back": "/26 (62 hosts)"},
            {"front": "Behöver 100 hosts - vilket prefix?", "back": "/25 (126 hosts)"},
            {"front": "Behöver 25 hosts - vilket prefix?", "back": "/27 (30 hosts)"},
            {"front": "Behöver 10 hosts - vilket prefix?", "back": "/28 (14 hosts)"},
            {"front": "Behöver 5 hosts - vilket prefix?", "back": "/29 (6 hosts)"},
            {"front": "Point-to-point länk - vilket prefix?", "back": "/30 (2 hosts)"},
            # SUBNÄT UPPDELNING
            {
                "front": "192.168.1.0/24 delas i 4 - vilka subnät?",
                "back": ".0/26, .64/26, .128/26, .192/26",
            },
            {
                "front": "192.168.1.0/24 delas i 8 - vilka prefix?",
                "back": "/27 (32 adresser var)",
            },
            {
                "front": "10.0.0.0/24 delas i 16 - vilka prefix?",
                "back": "/28 (16 adresser var)",
            },
            # SAMMA SUBNÄT?
            {
                "front": "192.168.1.30 och .40 i samma /28?",
                "back": "Nej. .30 i .16-.31, .40 i .32-.47",
            },
            {
                "front": "192.168.1.100 och .120 i samma /27?",
                "back": "Ja. Båda i .96-.127",
            },
            {"front": "10.0.0.50 och .60 i samma /26?", "back": "Ja. Båda i .0-.63"},
            {"front": "10.0.0.65 och .100 i samma /26?", "back": "Ja. Båda i .64-.127"},
            {"front": "172.16.0.10 och .20 i samma /28?", "back": "Ja. Båda i .0-.15"},
            # SPECIAL
            {
                "front": "Vad är Network ID?",
                "back": "Första adressen i subnätet (ej för hosts)",
            },
            {
                "front": "Vad är Broadcast?",
                "back": "Sista adressen i subnätet (ej för hosts)",
            },
            {
                "front": "Varför -2 vid hosts?",
                "back": "Network ID och Broadcast kan ej användas",
            },
            {
                "front": "/30 - varför för routrar?",
                "back": "Ger exakt 2 IP:er - en per router",
            },
            # SNABBRÄKNING
            {
                "front": "Snabbmetod: hitta block?",
                "back": "IP ÷ block size → avrunda ner → multiplicera",
            },
            {"front": "Snabbmetod: broadcast?", "back": "Network ID + block size - 1"},
            {"front": "Host-bitar i /26?", "back": "6 (32-26=6)"},
            {"front": "Host-bitar i /27?", "back": "5 (32-27=5)"},
            {"front": "Host-bitar i /28?", "back": "4 (32-28=4)"},
            {"front": "Host-bitar i /29?", "back": "3 (32-29=3)"},
            {"front": "Host-bitar i /30?", "back": "2 (32-30=2)"},
        ],
        # =====================================================================
        # NOD 2: FILSYSTEM & GRUNDKOMMANDON (100 flashcards)
        # =====================================================================
        "nod2_filsystem": [
            {
                "front": "Vad gör kommandot 'ls'?",
                "back": "Listar filer och kataloger. -l för detaljer, -a för dolda filer, -h för läsbar storlek.",
            },
            {
                "front": "Vad gör 'ls -la'?",
                "back": "Listar ALLA filer (även dolda) med detaljerad info: rättigheter, ägare, storlek, datum.",
            },
            {
                "front": "Vad gör kommandot 'cd'?",
                "back": "Change Directory - byter aktuell katalog. cd ~ = hem, cd .. = upp, cd - = föregående.",
            },
            {
                "front": "Vad gör 'pwd'?",
                "back": "Print Working Directory - visar absolut sökväg till aktuell katalog.",
            },
            {
                "front": "Vad gör 'mkdir'?",
                "back": "Make Directory - skapar en katalog. -p skapar föräldrakataloger om de saknas.",
            },
            {
                "front": "Vad gör 'rmdir'?",
                "back": "Remove Directory - tar bort TOM katalog. Använd rm -r för icke-tomma.",
            },
            {
                "front": "Vad gör 'rm'?",
                "back": "Remove - tar bort filer. -r = rekursivt, -f = force (utan fråga). VARNING: Ingen papperskorg!",
            },
            {
                "front": "Vad gör 'rm -rf'?",
                "back": "Tar bort filer och kataloger rekursivt utan bekräftelse. EXTREMT FARLIGT om felaktigt använt!",
            },
            {
                "front": "Vad gör 'cp'?",
                "back": "Copy - kopierar filer. -r för kataloger, -p bevarar attribut.",
            },
            {
                "front": "Vad gör 'mv'?",
                "back": "Move - flyttar eller byter namn på filer/kataloger.",
            },
            {
                "front": "Vad gör 'touch'?",
                "back": "Skapar tom fil eller uppdaterar tidsstämpel på befintlig fil.",
            },
            {
                "front": "Vad gör 'cat'?",
                "back": "Concatenate - visar filinnehåll. cat fil1 fil2 slår ihop filer.",
            },
            {
                "front": "Vad gör 'less'?",
                "back": "Visar fil sida för sida. Navigera med pilar, sök med /, avsluta med q.",
            },
            {
                "front": "Vad gör 'more'?",
                "back": "Äldre variant av less. Visar fil framåt, mer begränsad navigation.",
            },
            {
                "front": "Vad gör 'head'?",
                "back": "Visar första raderna av en fil. head -n 20 visar första 20 raderna.",
            },
            {
                "front": "Vad gör 'tail'?",
                "back": "Visar sista raderna. tail -f följer filen live (bra för loggar).",
            },
            {
                "front": "Vad gör 'tail -f'?",
                "back": "Följer fil i realtid - visar nya rader direkt när de skrivs. Perfekt för loggar!",
            },
            {
                "front": "Vad gör 'wc'?",
                "back": "Word Count - räknar rader (-l), ord (-w) och tecken/bytes (-c).",
            },
            {
                "front": "Vad gör 'find'?",
                "back": "Söker efter filer. find /sökväg -name 'mönster' hittar matchande filer.",
            },
            {
                "front": "Vad gör 'locate'?",
                "back": "Snabb filsökning via databas. Kräver 'updatedb' för att vara aktuell.",
            },
            {
                "front": "Vad gör 'which'?",
                "back": "Visar sökvägen till ett kommando. which python visar var python ligger.",
            },
            {
                "front": "Vad gör 'whereis'?",
                "back": "Hittar binär, källkod och manualsidor för ett kommando.",
            },
            {
                "front": "Vad gör 'file'?",
                "back": "Identifierar filtyp baserat på innehåll, inte filändelse.",
            },
            {
                "front": "Vad är en absolut sökväg?",
                "back": "Börjar från rot (/). T.ex. /home/user/dokument/fil.txt",
            },
            {
                "front": "Vad är en relativ sökväg?",
                "back": "Relativt till aktuell katalog. T.ex. ./dokument/fil.txt eller ../annan/",
            },
            {
                "front": "Vad betyder ~ i Linux?",
                "back": "Hemkatalogen för aktuell användare. cd ~ = cd /home/användarnamn.",
            },
            {
                "front": "Vad betyder . (punkt)?",
                "back": "Aktuell katalog. ./script.sh kör skript i aktuell katalog.",
            },
            {
                "front": "Vad betyder .. (dubbla punkter)?",
                "back": "Föräldrakatalogen. cd .. går upp ett steg.",
            },
            {
                "front": "Vad är /root?",
                "back": "Hemkatalog för root-användaren. INTE samma som / (rot).",
            },
            {
                "front": "Vad är /?",
                "back": "Rotkatalogen - toppen av filsystemshierarkin. Alla filer utgår härifrån.",
            },
            {
                "front": "Vad är /home?",
                "back": "Innehåller användarnas hemkataloger. /home/anna, /home/bob, etc.",
            },
            {
                "front": "Vad är /etc?",
                "back": "Konfigurationsfiler för system och program. Nästan alla inställningar finns här.",
            },
            {
                "front": "Vad är /var?",
                "back": "Variable data - loggar (/var/log), mail, temporära filer som ändras.",
            },
            {
                "front": "Vad är /var/log?",
                "back": "Systemloggar. syslog, auth.log, dmesg, och applikationsloggar.",
            },
            {
                "front": "Vad är /tmp?",
                "back": "Temporära filer. Rensas vid omstart. Vem som helst kan skriva här.",
            },
            {
                "front": "Vad är /bin?",
                "back": "Grundläggande binärer (kommandon) som alltid måste fungera: ls, cp, cat...",
            },
            {
                "front": "Vad är /sbin?",
                "back": "Systembinärer för administration: fdisk, mkfs, reboot. Kräver ofta root.",
            },
            {
                "front": "Vad är /usr?",
                "back": "User System Resources - program, bibliotek, dokumentation för användare.",
            },
            {
                "front": "Vad är /usr/bin?",
                "back": "De flesta användarprogram installeras här. python, vim, firefox...",
            },
            {
                "front": "Vad är /usr/local?",
                "back": "Lokalt installerade program (utanför pakethanteraren).",
            },
            {
                "front": "Vad är /opt?",
                "back": "Optional - tredjepartsprogram som inte följer FHS-strukturen.",
            },
            {
                "front": "Vad är /boot?",
                "back": "Boot-filer: kernel, initrd, GRUB-konfiguration.",
            },
            {
                "front": "Vad är /dev?",
                "back": "Device files - representerar hårdvara. /dev/sda = första disken.",
            },
            {
                "front": "Vad är /dev/null?",
                "back": "Svart hål - allt som skrivs hit försvinner. Används för att tysta output.",
            },
            {
                "front": "Vad är /dev/zero?",
                "back": "Oändlig källa av noll-bytes. Används för att skapa tomma filer.",
            },
            {
                "front": "Vad är /proc?",
                "back": "Virtuellt filsystem med processinformation och kernel-data.",
            },
            {
                "front": "Vad är /proc/cpuinfo?",
                "back": "Information om processorn: modell, hastighet, kärnor.",
            },
            {
                "front": "Vad är /sys?",
                "back": "Virtuellt filsystem för kernel- och hårdvarukonfiguration.",
            },
            {
                "front": "Vad är /mnt?",
                "back": "Mount point för tillfälligt monterade filsystem.",
            },
            {
                "front": "Vad är /media?",
                "back": "Automatiskt monterade media: USB, CD-ROM.",
            },
            {
                "front": "Vad gör 'df'?",
                "back": "Disk Free - visar diskutrymme för monterade filsystem. -h för läsbart format.",
            },
            {
                "front": "Vad gör 'df -h'?",
                "back": "Visar diskutrymme i human-readable format (GB, MB istället för bytes).",
            },
            {
                "front": "Vad gör 'du'?",
                "back": "Disk Usage - visar storlek på filer/kataloger. du -sh katalog ger total storlek.",
            },
            {
                "front": "Vad gör 'du -sh *'?",
                "back": "Visar storlek för varje fil/katalog i aktuell mapp, summerat och läsbart.",
            },
            {
                "front": "Vad gör 'mount'?",
                "back": "Monterar filsystem. mount /dev/sdb1 /mnt/disk kopplar partition till katalog.",
            },
            {
                "front": "Vad gör 'umount'?",
                "back": "Avmonterar filsystem. Stavar UMOUNT inte unmount!",
            },
            {
                "front": "Vad är /etc/fstab?",
                "back": "Konfigurerar automatisk montering vid systemstart. Definerar vad som monteras var.",
            },
            {
                "front": "Vad gör 'ln'?",
                "back": "Skapar länkar. ln -s mål länk skapar symbolisk länk (genväg).",
            },
            {
                "front": "Skillnad mellan hård och symbolisk länk?",
                "back": "Hård = samma inode (data), symbolisk = pekare till sökväg. Symbolisk kan korsa filsystem.",
            },
            {
                "front": "Vad gör 'stat'?",
                "back": "Visar detaljerad information om en fil: storlek, inode, rättigheter, tider.",
            },
            {
                "front": "Vad är en inode?",
                "back": "Datastruktur som lagrar filmetadata: ägare, rättigheter, plats på disk. Filnamn finns i katalog.",
            },
            {
                "front": "Vad gör 'echo'?",
                "back": "Skriver ut text till terminalen. echo $PATH visar PATH-variabeln.",
            },
            {
                "front": "Vad gör 'clear'?",
                "back": "Rensar terminalskärmen. Kortkommando: Ctrl+L.",
            },
            {
                "front": "Vad gör 'man'?",
                "back": "Manual pages - visar dokumentation för kommandon. man ls förklarar ls.",
            },
            {
                "front": "Hur avslutar man 'man'?",
                "back": "Tryck 'q'. Navigera med pilar, sök med /sökterm.",
            },
            {
                "front": "Vad gör 'history'?",
                "back": "Visar kommandohistorik. !nummer kör kommando igen. !! upprepar senaste.",
            },
            {
                "front": "Vad gör Ctrl+R?",
                "back": "Reverse search - sök i kommandohistoriken genom att börja skriva.",
            },
            {
                "front": "Vad gör 'alias'?",
                "back": "Skapar kortkommando. alias ll='ls -la' gör ll till ls -la.",
            },
            {
                "front": "Vad gör 'sort'?",
                "back": "Sorterar rader. sort -n numeriskt, sort -r omvänt, sort -u unika.",
            },
            {
                "front": "Vad gör 'uniq'?",
                "back": "Tar bort dubbletter (måste vara sorterad först!). uniq -c räknar förekomster.",
            },
            {
                "front": "Vad gör 'cut'?",
                "back": "Klipper ut kolumner. cut -d: -f1 /etc/passwd tar ut användarnamn.",
            },
            {
                "front": "Vad gör 'paste'?",
                "back": "Slår ihop filer kolumnvis. Motsatsen till cut.",
            },
            {
                "front": "Vad gör 'tr'?",
                "back": "Translate - ersätter tecken. tr 'a-z' 'A-Z' gör allt till versaler.",
            },
            {
                "front": "Vad gör 'tee'?",
                "back": "Skriver till både fil OCH stdout. ls | tee lista.txt visar och sparar.",
            },
            {
                "front": "Vad gör 'xargs'?",
                "back": "Bygger kommandon från stdin. find . -name '*.txt' | xargs rm tar bort hittade filer.",
            },
            {
                "front": "Vad gör 'diff'?",
                "back": "Visar skillnader mellan två filer rad för rad.",
            },
            {
                "front": "Vad gör 'cmp'?",
                "back": "Jämför filer byte för byte. Tystare än diff - visar bara om olika.",
            },
            {
                "front": "Vad gör 'md5sum'?",
                "back": "Beräknar MD5-checksumma för att verifiera filintegritet.",
            },
            {
                "front": "Vad gör 'sha256sum'?",
                "back": "Beräknar SHA-256-checksumma. Säkrare än MD5 för verifiering.",
            },
            {
                "front": "Vad gör 'ln -s'?",
                "back": "Skapar symbolisk länk (symlink/genväg). ln -s /mål /länk.",
            },
            {
                "front": "Vad gör 'readlink'?",
                "back": "Visar vart en symbolisk länk pekar. readlink -f ger absolut sökväg.",
            },
            {
                "front": "Vad gör 'basename'?",
                "back": "Extraherar filnamn från sökväg. basename /home/user/fil.txt = fil.txt.",
            },
            {
                "front": "Vad gör 'dirname'?",
                "back": "Extraherar katalogdelen av sökväg. dirname /home/user/fil.txt = /home/user.",
            },
            {
                "front": "Vad är en dold fil i Linux?",
                "back": "Filer som börjar med punkt (.). T.ex. .bashrc, .ssh. Visas med ls -a.",
            },
            {
                "front": "Vad är .bashrc?",
                "back": "Konfigurationsfil för Bash som körs vid nya terminal-sessioner.",
            },
            {
                "front": "Vad är .profile?",
                "back": "Körs vid inloggning. Sätter miljövariabler för sessionen.",
            },
            {
                "front": "Vad är .bash_history?",
                "back": "Sparad kommandohistorik. history-kommandot läser härifrån.",
            },
            {
                "front": "Vad gör 'tree'?",
                "back": "Visar katalogstruktur som ett träd. tree -L 2 visar 2 nivåer.",
            },
            {
                "front": "Hur skapar man en tom fil snabbt?",
                "back": "touch filnamn eller > filnamn (omdirigerar ingenting till fil).",
            },
            {
                "front": "Vad gör 'split'?",
                "back": "Delar upp stora filer i mindre delar. split -b 1M stor.fil del_",
            },
            {
                "front": "Vad gör 'dd'?",
                "back": "Data duplicator - kopierar och konverterar data. Används för disk-images.",
            },
            {
                "front": "Vad gör 'dd if=/dev/zero of=fil bs=1M count=100'?",
                "back": "Skapar en 100MB fil fylld med nollor. if=input, of=output, bs=blocksize.",
            },
            {
                "front": "Vad är FHS?",
                "back": "Filesystem Hierarchy Standard - definierar var filer ska ligga i Linux.",
            },
            {
                "front": "Hur ser man filtyp utan filändelse?",
                "back": "Kommandot 'file' analyserar innehållet och identifierar typen.",
            },
            {
                "front": "Vad är glob patterns?",
                "back": "Jokertecken: * matchar allt, ? matchar ett tecken, [abc] matchar a, b eller c.",
            },
            {
                "front": "Vad gör 'ls *.txt'?",
                "back": "Listar alla filer som slutar på .txt i aktuell katalog.",
            },
            {
                "front": "Vad gör 'ls [a-z]*'?",
                "back": "Listar filer som börjar med liten bokstav.",
            },
        ],
        # =====================================================================
        # NOD 3: BASH SCRIPTING GRUND - 100 Flashcards
        # =====================================================================
        "nod3_bash_grund": [
            {
                "front": "Vad är shebang?",
                "back": "#!/bin/bash på första raden. Talar om vilken tolk som kör scriptet.",
            },
            {
                "front": "Hur gör man script körbart?",
                "back": "chmod +x script.sh - lägger till execute-rättighet.",
            },
            {
                "front": "Hur skapar man variabel i bash?",
                "back": "namn=värde (INGA mellanslag runt =!)",
            },
            {
                "front": "Hur läser man variabel?",
                "back": "$variabelnamn eller ${variabelnamn} för tydlighet.",
            },
            {
                "front": "Vad är $1, $2, $3?",
                "back": "Positionella parametrar - argument som skickas till scriptet.",
            },
            {
                "front": "Vad är $0?",
                "back": "Scriptets namn/sökväg som det anropades med.",
            },
            {
                "front": "Vad är $#?",
                "back": "Antal argument som skickades till scriptet.",
            },
            {
                "front": "Vad är $@?",
                "back": "Alla argument som separata ord (för loopar).",
            },
            {"front": "Vad är $*?", "back": "Alla argument som en enda sträng."},
            {
                "front": "Vad är $??",
                "back": "Exit-kod från senaste kommando. 0=lyckat.",
            },
            {
                "front": "Vad är $$?",
                "back": "Process-ID (PID) för aktuellt script/shell.",
            },
            {"front": "Hur skriver man kommentar?", "back": "# detta är en kommentar"},
            {"front": "if-sats syntax?", "back": "if [ villkor ]; then kommandon; fi"},
            {
                "front": "if-else syntax?",
                "back": "if [ villkor ]; then ... else ... fi",
            },
            {
                "front": "if-elif-else syntax?",
                "back": "if [ ]; then ... elif [ ]; then ... else ... fi",
            },
            {
                "front": "Vad betyder -eq?",
                "back": "Equal - jämför tal. if [ $a -eq $b ]",
            },
            {"front": "Vad betyder -ne?", "back": "Not equal - tal är olika."},
            {"front": "Vad betyder -lt?", "back": "Less than - mindre än (tal)."},
            {
                "front": "Vad betyder -le?",
                "back": "Less than or equal - mindre eller lika (tal).",
            },
            {"front": "Vad betyder -gt?", "back": "Greater than - större än (tal)."},
            {
                "front": "Vad betyder -ge?",
                "back": "Greater than or equal - större eller lika (tal).",
            },
            {
                "front": "Hur jämför man strängar?",
                "back": '= för lika, != för olika. [ "$a" = "$b" ]',
            },
            {
                "front": "Vad betyder -z?",
                "back": 'Strängen är tom (zero length). [ -z "$var" ]',
            },
            {"front": "Vad betyder -n?", "back": 'Strängen är INTE tom. [ -n "$var" ]'},
            {
                "front": "Vad betyder -f?",
                "back": "Fil finns och är en vanlig fil (file).",
            },
            {"front": "Vad betyder -d?", "back": "Sökvägen är en katalog (directory)."},
            {
                "front": "Vad betyder -e?",
                "back": "Något finns (exists) - fil, katalog, länk...",
            },
            {"front": "Vad betyder -r?", "back": "Filen är läsbar (readable)."},
            {"front": "Vad betyder -w?", "back": "Filen är skrivbar (writable)."},
            {"front": "Vad betyder -x?", "back": "Filen är körbar (executable)."},
            {
                "front": "Vad betyder -s?",
                "back": "Filen finns och har storlek > 0 (size).",
            },
            {
                "front": "Vad gör read?",
                "back": "Läser input från användaren till variabel. read namn",
            },
            {
                "front": "Vad gör read -p?",
                "back": 'Visar prompt före input. read -p "Namn: " namn',
            },
            {
                "front": "Vad gör read -s?",
                "back": "Silent - döljer input (för lösenord).",
            },
            {"front": "Vad gör read -t?", "back": "Timeout i sekunder. read -t 5 svar"},
            {"front": "Vad gör echo?", "back": 'Skriver ut text. echo "Hej $namn"'},
            {
                "front": "Vad gör echo -n?",
                "back": "Skriver utan avslutande radbrytning.",
            },
            {
                "front": "Vad gör echo -e?",
                "back": "Tolkar escape-sekvenser som \\n och \\t.",
            },
            {
                "front": "Skillnad ' ' och \" \"?",
                "back": "' ' = bokstavligt. \" \" = expanderar $variabler.",
            },
            {
                "front": 'Vad skriver echo "$HOME"?',
                "back": "Din hemkatalog-sökväg (variabeln expanderas).",
            },
            {
                "front": "Vad skriver echo '$HOME'?",
                "back": "$HOME bokstavligt (ingen expansion i single quotes).",
            },
            {
                "front": "Hur kör man kommando och sparar output?",
                "back": "variabel=$(kommando) eller variabel=`kommando`",
            },
            {
                "front": "Vad är command substitution?",
                "back": "$(kommando) - kör kommando och använder resultatet.",
            },
            {
                "front": "Hur gör man aritmetik?",
                "back": "$((uttryck)) - t.ex. $((5 + 3))",
            },
            {
                "front": "Vad är exit-kod?",
                "back": "Värde som kommando returnerar. 0 = OK, annat = fel.",
            },
            {
                "front": "Hur avslutar man script med status?",
                "back": "exit 0 (lyckat) eller exit 1 (fel).",
            },
            {
                "front": "Vad gör source?",
                "back": "Kör script i aktuell shell (variabler bevaras). source script.sh",
            },
            {
                "front": "Skillnad ./script.sh och source script.sh?",
                "back": "./ kör i subshell (isolerat), source kör i samma shell.",
            },
            {
                "front": "Hur exporterar man variabel?",
                "back": "export VAR=värde - gör tillgänglig för subprocesser.",
            },
            {
                "front": "Vad är miljövariabel?",
                "back": "Variabel synlig för alla processer. T.ex. PATH, HOME.",
            },
            {
                "front": "Vad är PATH?",
                "back": "Lista med kataloger där shell letar efter kommandon.",
            },
            {
                "front": "Vad är HOME?",
                "back": "Sökväg till din hemkatalog. ~ expanderar till $HOME.",
            },
            {
                "front": "Vad är PWD?",
                "back": "Present Working Directory - aktuell katalog.",
            },
            {"front": "Vad är USER?", "back": "Ditt användarnamn."},
            {
                "front": "Vad är SHELL?",
                "back": "Sökväg till din standard-shell. /bin/bash vanligt.",
            },
            {
                "front": "Hur kör man script från var som helst?",
                "back": "Lägg det i katalog som finns i PATH, eller ange full sökväg.",
            },
            {
                "front": "Vad gör test-kommandot?",
                "back": "Utvärderar villkor. test -f fil är samma som [ -f fil ].",
            },
            {
                "front": "Varför mellanslag i [ ]?",
                "back": "[ är ett kommando! [ -f fil ] behöver mellanslag runt.",
            },
            {
                "front": "Logisk AND i [ ]?",
                "back": "[ villkor1 ] && [ villkor2 ] - båda måste vara sanna.",
            },
            {
                "front": "Logisk OR i [ ]?",
                "back": "[ villkor1 ] || [ villkor2 ] - minst ett måste vara sant.",
            },
            {
                "front": "Logisk NOT i [ ]?",
                "back": "[ ! villkor ] - inverterar resultatet.",
            },
            {
                "front": "Vad gör -a i [ ]?",
                "back": "AND inuti [ ]. [ -f fil -a -r fil ] - finns OCH läsbar.",
            },
            {
                "front": "Vad gör -o i [ ]?",
                "back": "OR inuti [ ]. [ -f fil -o -d fil ] - fil ELLER katalog.",
            },
            {
                "front": "Vad är true i bash?",
                "back": "Kommando som alltid returnerar 0 (lyckat).",
            },
            {
                "front": "Vad är false i bash?",
                "back": "Kommando som alltid returnerar 1 (misslyckat).",
            },
            {
                "front": "Vad gör :?",
                "back": "Null-kommando - gör inget, returnerar 0. Platshållare.",
            },
            {
                "front": "Hur skriver man flerradig sträng?",
                "back": "Heredoc: cat <<EOF\\nrad1\\nrad2\\nEOF",
            },
            {
                "front": "Vad är heredoc?",
                "back": "<<DELIMITER för flerradig input till kommando.",
            },
            {
                "front": "Hur omdirigerar man stdout?",
                "back": "> fil (skriv över) eller >> fil (lägg till).",
            },
            {
                "front": "Hur omdirigerar man stderr?",
                "back": "2> fil - skickar felmeddelanden till fil.",
            },
            {
                "front": "Hur omdirigerar man båda?",
                "back": "&> fil eller > fil 2>&1 - stdout och stderr till fil.",
            },
            {
                "front": "Vad betyder /dev/null?",
                "back": "Svart hål - allt som skrivs dit försvinner.",
            },
            {
                "front": "Hur tystar man ett kommando helt?",
                "back": "kommando > /dev/null 2>&1",
            },
            {
                "front": "Vad är pipe?",
                "back": "| - skickar output från ett kommando som input till nästa.",
            },
            {
                "front": "Exempel på pipe?",
                "back": "ls | grep txt - listar filer, filtrerar de med 'txt'.",
            },
            {
                "front": "Vad gör seq?",
                "back": "Genererar sekvens av tal. seq 1 10 ger 1 2 3...10.",
            },
            {
                "front": "Hur skapar man array?",
                "back": "arr=(element1 element2 element3)",
            },
            {
                "front": "Hur läser man array-element?",
                "back": "${arr[0]} för första, ${arr[1]} för andra, etc.",
            },
            {
                "front": "Hur får man alla array-element?",
                "back": "${arr[@]} eller ${arr[*]}",
            },
            {
                "front": "Hur får man array-längd?",
                "back": "${#arr[@]} - antal element i arrayen.",
            },
            {"front": "Hur lägger man till i array?", "back": "arr+=(nytt_element)"},
            {
                "front": "Vad är associativ array?",
                "back": "Array med nyckel-värde. declare -A arr; arr[key]=värde",
            },
            {
                "front": "Vad gör printf?",
                "back": 'Formaterad utskrift. printf "%s är %d år" "Anna" 25',
            },
            {"front": "Vad är %s i printf?", "back": "Placeholder för sträng."},
            {
                "front": "Vad är %d i printf?",
                "back": "Placeholder för heltal (decimal).",
            },
            {
                "front": "Vad är %f i printf?",
                "back": "Placeholder för flyttal (float).",
            },
            {
                "front": "Hur gör man variabel read-only?",
                "back": "readonly VAR=värde - kan inte ändras.",
            },
            {"front": "Hur tar man bort variabel?", "back": "unset variabelnamn"},
            {"front": "Vad gör env?", "back": "Visar alla miljövariabler."},
            {
                "front": "Vad gör printenv?",
                "back": "Visar miljövariabler. printenv HOME visar specifik.",
            },
            {
                "front": "Vad gör set utan argument?",
                "back": "Visar alla variabler och funktioner i aktuell shell.",
            },
            {
                "front": "Hur kör man kommando bara om föregående lyckades?",
                "back": "kommando1 && kommando2 - AND.",
            },
            {
                "front": "Hur kör man kommando bara om föregående misslyckades?",
                "back": "kommando1 || kommando2 - OR.",
            },
            {
                "front": "Vad gör which?",
                "back": "Visar sökväg till ett kommando. which ls → /bin/ls",
            },
            {
                "front": "Vad gör type?",
                "back": "Visar vad ett kommando är - alias, funktion, inbyggt, fil.",
            },
            {
                "front": "Hur definierar man alias?",
                "back": "alias namn='kommando' - t.ex. alias ll='ls -la'",
            },
        ],
        # =====================================================================
        # NOD 4: BASH SCRIPTING AVANCERAT - 100 Flashcards
        # =====================================================================
        "nod4_bash_avancerat": [
            {
                "front": "for-loop syntax?",
                "back": "for var in lista; do kommandon; done",
            },
            {
                "front": "for-loop med range?",
                "back": "for i in {1..10}; do echo $i; done",
            },
            {
                "front": "for-loop C-stil?",
                "back": "for ((i=0; i<10; i++)); do echo $i; done",
            },
            {
                "front": "while-loop syntax?",
                "back": "while [ villkor ]; do kommandon; done",
            },
            {
                "front": "until-loop syntax?",
                "back": "until [ villkor ]; do kommandon; done (kör tills sant)",
            },
            {
                "front": "Oändlig loop?",
                "back": "while true; do ...; done eller while :; do ...; done",
            },
            {"front": "Hur bryter man loop?", "back": "break - hoppar ur loopen helt."},
            {
                "front": "Hur hoppar man till nästa iteration?",
                "back": "continue - skippar resten av aktuell iteration.",
            },
            {"front": "Vad gör break 2?", "back": "Bryter ur två nästlade loopar."},
            {"front": "Funktion syntax?", "back": "funktionsnamn() { kommandon; }"},
            {
                "front": "Funktion med function-keyword?",
                "back": "function namn { kommandon; }",
            },
            {
                "front": "Hur anropar man funktion?",
                "back": "Bara skriv namnet - inga parenteser! funktionsnamn arg1 arg2",
            },
            {
                "front": "Hur får funktion argument?",
                "back": "Samma som script: $1, $2, $@, $#",
            },
            {
                "front": "Vad gör return?",
                "back": "Avslutar funktion med exit-kod. return 0 = OK.",
            },
            {
                "front": "Hur returnerar funktion värde?",
                "back": 'echo "värde" i funktionen, anropa med $(funktionsnamn)',
            },
            {
                "front": "Vad gör local?",
                "back": "Gör variabel lokal i funktion. local var=värde",
            },
            {
                "front": "Skillnad global vs local variabel?",
                "back": "Global syns överallt, local bara i funktionen.",
            },
            {
                "front": "Vad gör set -e?",
                "back": "Avsluta script vid första fel (errexit).",
            },
            {
                "front": "Vad gör set -u?",
                "back": "Fel vid användning av osatt variabel (nounset).",
            },
            {
                "front": "Vad gör set -x?",
                "back": "Debug - visar varje kommando innan det körs (xtrace).",
            },
            {
                "front": "Vad gör set -o pipefail?",
                "back": "Pipeline misslyckas om något kommando i den misslyckas.",
            },
            {
                "front": "Bra start på robusta script?",
                "back": "#!/bin/bash\\nset -euo pipefail",
            },
            {
                "front": "Skillnad [ ] och [[ ]]?",
                "back": "[[ ]] är bash-specifik, hanterar && || direkt, säkrare.",
            },
            {
                "front": "Pattern matching i [[ ]]?",
                "back": "[[ $str == *.txt ]] - matchar med glob patterns.",
            },
            {
                "front": "Regex i [[ ]]?",
                "back": "[[ $str =~ mönster ]] - regex matching.",
            },
            {
                "front": "case syntax?",
                "back": "case $var in\\nmönster1) kommandon;;\\nmönster2) kommandon;;\\nesac",
            },
            {
                "front": "Wildcard i case?",
                "back": "*) matchar allt - används som default/else.",
            },
            {
                "front": "Vad gör shift?",
                "back": "Tar bort $1, flyttar $2→$1, $3→$2, etc.",
            },
            {
                "front": "Vad gör shift 2?",
                "back": "Skiftar två positioner - tar bort $1 och $2.",
            },
            {
                "front": "Vad gör getopts?",
                "back": 'Parsar kommandoradsargument. getopts "ab:c" opt',
            },
            {
                "front": "Vad betyder b: i getopts?",
                "back": ": efter bokstav = flaggan kräver argument.",
            },
            {
                "front": "Vad är OPTARG?",
                "back": "Innehåller argumentet till en getopts-flagga.",
            },
            {
                "front": "Vad är OPTIND?",
                "back": "Index för nästa argument att processa i getopts.",
            },
            {
                "front": "Vad gör trap?",
                "back": "Fångar signaler och kör kod. trap 'cleanup' EXIT",
            },
            {
                "front": "Vanliga signaler att trappa?",
                "back": "EXIT, INT (Ctrl+C), TERM, ERR",
            },
            {
                "front": "Hur kör man kommando i bakgrunden?",
                "back": "kommando & - lägg & i slutet.",
            },
            {"front": "Vad är $!?", "back": "PID för senaste bakgrundsjobb."},
            {
                "front": "Vad gör wait?",
                "back": "Väntar på bakgrundsjobb. wait $pid för specifik.",
            },
            {"front": "Vad gör fg?", "back": "Tar bakgrundsjobb till förgrunden."},
            {"front": "Vad gör bg?", "back": "Fortsätter pausat jobb i bakgrunden."},
            {"front": "Vad gör jobs?", "back": "Listar aktiva jobb i aktuell shell."},
            {
                "front": "Hur pausar man körande process?",
                "back": "Ctrl+Z - suspenderar till bakgrunden.",
            },
            {
                "front": "Vad gör nohup?",
                "back": "Kör kommando immunt mot hangup. nohup kommando &",
            },
            {
                "front": "Vad gör disown?",
                "back": "Tar bort jobb från shell:ens jobblista.",
            },
            {
                "front": "Vad gör exec?",
                "back": "Ersätter shell-processen med nytt kommando.",
            },
            {"front": "Vad gör eval?", "back": 'Kör sträng som kommando. eval "$cmd"'},
            {
                "front": "Varför är eval farligt?",
                "back": "Kan köra godtycklig kod - säkerhetsrisk med user input.",
            },
            {
                "front": "Vad är subshell?",
                "back": "( kommandon ) - kör i barn-process, isolerat.",
            },
            {
                "front": "Vad är command group?",
                "back": "{ kommandon; } - kör i samma shell (behöver ;).",
            },
            {
                "front": "Skillnad ( ) och { }?",
                "back": "( ) = subshell (isolerat), { } = samma shell.",
            },
            {
                "front": "Vad gör let?",
                "back": 'Aritmetik. let "x = 5 + 3" eller let x++',
            },
            {
                "front": "Vad gör expr?",
                "back": "Äldre aritmetik. expr 5 + 3 (mellanslag krävs).",
            },
            {"front": "Modulo i bash?", "back": "$((10 % 3)) = 1 (rest vid division)"},
            {"front": "Exponent i bash?", "back": "$((2 ** 8)) = 256"},
            {
                "front": "Pre-increment?",
                "back": "$((++x)) - ökar först, returnerar sedan.",
            },
            {
                "front": "Post-increment?",
                "back": "$((x++)) - returnerar först, ökar sedan.",
            },
            {
                "front": "String length?",
                "back": "${#variabel} - antal tecken i sträng.",
            },
            {
                "front": "Substring extraction?",
                "back": "${variabel:start:längd} - t.ex. ${str:0:5} första 5.",
            },
            {
                "front": "Ta bort från början av sträng?",
                "back": "${var#mönster} - kortaste match, ## längsta.",
            },
            {
                "front": "Ta bort från slutet av sträng?",
                "back": "${var%mönster} - kortaste match, %% längsta.",
            },
            {
                "front": "Ersätt i sträng?",
                "back": "${var/sök/ersätt} - första, // alla förekomster.",
            },
            {
                "front": "Sträng till uppercase?",
                "back": "${var^^} - allt till versaler.",
            },
            {
                "front": "Sträng till lowercase?",
                "back": "${var,,} - allt till gemener.",
            },
            {
                "front": "Default value om osatt?",
                "back": "${var:-default} - använd default om var är tom/osatt.",
            },
            {
                "front": "Sätt default om osatt?",
                "back": "${var:=default} - sätter var till default om osatt.",
            },
            {
                "front": "Fel om osatt?",
                "back": "${var:?felmeddelande} - skriv fel och avsluta om osatt.",
            },
            {
                "front": "Vad gör select?",
                "back": "Skapar numrerad meny. select val in a b c; do ...; done",
            },
            {
                "front": "Vad är REPLY i select?",
                "back": "Innehåller det användaren skrev (inte valet).",
            },
            {
                "front": "Vad är PS3?",
                "back": 'Prompten för select-menyer. PS3="Välj: "',
            },
            {
                "front": "Vad är IFS?",
                "back": "Internal Field Separator - bestämmer orddelning.",
            },
            {"front": "Standard IFS?", "back": "Space, tab, newline."},
            {
                "front": "Hur läser man fil rad för rad?",
                "back": "while IFS= read -r rad; do ...; done < fil",
            },
            {
                "front": "Varför read -r?",
                "back": "Raw - tolkar inte backslash som escape.",
            },
            {
                "front": "Varför IFS= vid read?",
                "back": "Bevarar ledande/avslutande whitespace på rader.",
            },
            {
                "front": "Vad gör mapfile/readarray?",
                "back": "Läser fil till array. mapfile -t arr < fil",
            },
            {
                "front": "Process substitution?",
                "back": "<(kommando) - kör kommando, ge output som fil.",
            },
            {
                "front": "Exempel process substitution?",
                "back": "diff <(ls dir1) <(ls dir2) - jämför output.",
            },
            {
                "front": "Vad är here string?",
                "back": '<<< "sträng" - skickar sträng som stdin.',
            },
            {
                "front": "Named pipe (FIFO)?",
                "back": "mkfifo pipe - skapa, kan läsas/skrivas som fil.",
            },
            {
                "front": "Vad gör coproc?",
                "back": "Kör kommando som coprocess med tvåvägs-pipe.",
            },
            {
                "front": "Debugging med bash -x?",
                "back": "bash -x script.sh - kör med debug-output.",
            },
            {
                "front": "Vad gör BASH_SOURCE?",
                "back": "Array med källfiler. ${BASH_SOURCE[0]} = aktuellt script.",
            },
            {
                "front": "Vad gör FUNCNAME?",
                "back": "Array med anropsstack av funktionsnamn.",
            },
            {"front": "Vad gör LINENO?", "back": "Aktuellt radnummer i scriptet."},
            {
                "front": "Hur sparar man funktion till fil?",
                "back": "declare -f funktionsnamn > fil",
            },
            {
                "front": "Hur exporterar man funktion?",
                "back": "export -f funktionsnamn - gör tillgänglig i subshells.",
            },
            {
                "front": "Vad gör complete?",
                "back": "Definierar tab-completion för kommandon.",
            },
            {"front": "Vad gör compgen?", "back": "Genererar completion-förslag."},
            {
                "front": "Vad är shopt?",
                "back": "Sätter shell-options. shopt -s nullglob",
            },
            {
                "front": "Vad gör nullglob?",
                "back": "Glob som inte matchar blir tomt istället för bokstavligt.",
            },
            {
                "front": "Vad gör globstar?",
                "back": "** matchar rekursivt genom kataloger.",
            },
            {
                "front": "Vad gör extglob?",
                "back": "Extended glob patterns som !(mönster), *(mönster).",
            },
            {
                "front": "Hur tidsmäter man kommando?",
                "back": "time kommando - visar real, user, sys tid.",
            },
        ],
        # =====================================================================
        # NOD 5: ANVÄNDARE & BEHÖRIGHETER - 100 Flashcards
        # =====================================================================
        "nod5_anvandare": [
            {
                "front": "Vem är root?",
                "back": "Superuser med UID 0. Har fullständig systemåtkomst.",
            },
            {"front": "Vad gör sudo?", "back": "Kör kommando som root. sudo kommando."},
            {
                "front": "Var lagras användare?",
                "back": "/etc/passwd - namn, UID, GID, hemkatalog, shell.",
            },
            {
                "front": "Var lagras lösenord?",
                "back": "/etc/shadow - krypterade lösenord, läsbar endast av root.",
            },
            {
                "front": "Var lagras grupper?",
                "back": "/etc/group - gruppnamn, GID, medlemmar.",
            },
            {
                "front": "Vad är UID?",
                "back": "User ID - unikt nummer för varje användare. root=0.",
            },
            {
                "front": "Vad är GID?",
                "back": "Group ID - unikt nummer för varje grupp.",
            },
            {
                "front": "Vad gör useradd?",
                "back": "Skapar ny användare. useradd -m skapar hemkatalog.",
            },
            {
                "front": "useradd -m anna?",
                "back": "Skapar användare anna MED hemkatalog /home/anna.",
            },
            {"front": "useradd -s /bin/bash?", "back": "Anger shell för ny användare."},
            {
                "front": "useradd -G grupp1,grupp2?",
                "back": "Lägger till i extra grupper vid skapande.",
            },
            {
                "front": "Vad gör userdel?",
                "back": "Tar bort användare. -r tar även bort hemkatalog.",
            },
            {
                "front": "userdel -r anna?",
                "back": "Tar bort anna OCH hennes hemkatalog/mail.",
            },
            {"front": "Vad gör usermod?", "back": "Modifierar befintlig användare."},
            {
                "front": "usermod -aG docker anna?",
                "back": "Lägger TILL anna i docker-gruppen (append).",
            },
            {
                "front": "Varför -a med -G?",
                "back": "Utan -a ersätts alla grupper! -a lägger till.",
            },
            {
                "front": "usermod -l nytt anna?",
                "back": "Byter login-namn från anna till nytt.",
            },
            {
                "front": "usermod -d /ny/hem anna?",
                "back": "Ändrar annas hemkatalog (flyttar ej filer).",
            },
            {
                "front": "usermod -L anna?",
                "back": "Låser (Lock) kontot - kan ej logga in.",
            },
            {"front": "usermod -U anna?", "back": "Låser upp (Unlock) kontot."},
            {
                "front": "Vad gör passwd?",
                "back": "Ändrar lösenord. passwd ändrar ditt, passwd anna ändrar annas.",
            },
            {
                "front": "passwd -l anna?",
                "back": "Låser kontot genom att inaktivera lösenord.",
            },
            {"front": "passwd -u anna?", "back": "Låser upp kontot."},
            {
                "front": "passwd -e anna?",
                "back": "Tvingar lösenordsbyte vid nästa inloggning (expire).",
            },
            {
                "front": "Vad gör chage?",
                "back": "Ändrar lösenords-åldringsinställningar.",
            },
            {"front": "chage -l anna?", "back": "Visar lösenordspolicy för anna."},
            {
                "front": "chage -M 90 anna?",
                "back": "Lösenord måste bytas var 90:e dag.",
            },
            {
                "front": "Vad gör groupadd?",
                "back": "Skapar ny grupp. groupadd utvecklare.",
            },
            {
                "front": "Vad gör groupdel?",
                "back": "Tar bort grupp. groupdel utvecklare.",
            },
            {"front": "Vad gör groupmod?", "back": "Modifierar grupp. -n byter namn."},
            {
                "front": "Vad gör groups?",
                "back": "Visar vilka grupper en användare tillhör.",
            },
            {
                "front": "Vad gör id?",
                "back": "Visar UID, GID och alla grupper för användare.",
            },
            {"front": "Vad gör whoami?", "back": "Visar nuvarande användarnamn."},
            {
                "front": "Vad gör w?",
                "back": "Visar inloggade användare och vad de gör.",
            },
            {"front": "Vad gör who?", "back": "Visar vem som är inloggad."},
            {
                "front": "Vad gör last?",
                "back": "Visar senaste inloggningar från /var/log/wtmp.",
            },
            {
                "front": "Vad gör lastlog?",
                "back": "Visar senaste inloggning per användare.",
            },
            {
                "front": "Vad gör su?",
                "back": "Switch User - byter till annan användare.",
            },
            {
                "front": "Skillnad su och su -?",
                "back": "su - laddar målanvändarens miljö (login shell).",
            },
            {
                "front": "Vad gör sudo -i?",
                "back": "Startar interaktiv root-shell med roots miljö.",
            },
            {
                "front": "Vad gör sudo -s?",
                "back": "Startar shell som root men behåller din miljö.",
            },
            {
                "front": "Var konfigureras sudo?",
                "back": "/etc/sudoers - redigera med visudo!",
            },
            {
                "front": "Varför visudo?",
                "back": "Validerar syntax innan sparning - förhindrar att låsa ut dig.",
            },
            {
                "front": "Vad är primär grupp?",
                "back": "Gruppen som tilldelas nya filer användaren skapar.",
            },
            {
                "front": "Vad är supplementära grupper?",
                "back": "Extra grupper utöver primär, för åtkomst till resurser.",
            },
            {
                "front": "Vad gör newgrp?",
                "back": "Byter primär grupp för aktuell session.",
            },
            {
                "front": "Vad är rwx?",
                "back": "Read (4), Write (2), Execute (1) - filrättigheter.",
            },
            {
                "front": "Vad betyder 755?",
                "back": "rwxr-xr-x - ägare allt, andra läsa/köra.",
            },
            {
                "front": "Vad betyder 644?",
                "back": "rw-r--r-- - ägare läsa/skriva, andra bara läsa.",
            },
            {
                "front": "Vad betyder 700?",
                "back": "rwx------ - endast ägare har åtkomst.",
            },
            {
                "front": "Vad betyder 777?",
                "back": "rwxrwxrwx - alla kan allt. FARLIGT!",
            },
            {"front": "Vad gör chmod?", "back": "Change mode - ändrar filrättigheter."},
            {
                "front": "chmod +x fil?",
                "back": "Lägger till execute-rättighet för alla.",
            },
            {
                "front": "chmod u+x fil?",
                "back": "Lägger till execute endast för ägare (user).",
            },
            {"front": "chmod g+w fil?", "back": "Lägger till write för grupp."},
            {"front": "chmod o-r fil?", "back": "Tar bort read för others."},
            {"front": "chmod a=r fil?", "back": "Sätter exakt read för alla (all)."},
            {
                "front": "chmod -R 755 dir?",
                "back": "Recursive - ändrar katalog och allt i den.",
            },
            {"front": "Vad gör chown?", "back": "Change owner - ändrar filägare."},
            {"front": "chown anna fil?", "back": "Ändrar ägare till anna."},
            {
                "front": "chown anna:dev fil?",
                "back": "Ändrar ägare till anna OCH grupp till dev.",
            },
            {"front": "chown :dev fil?", "back": "Ändrar bara grupp till dev."},
            {"front": "chown -R anna dir?", "back": "Ändrar ägare rekursivt."},
            {"front": "Vad gör chgrp?", "back": "Change group - ändrar filgrupp."},
            {
                "front": "Vad är setuid (s)?",
                "back": "Fil körs som ägarens användare. chmod u+s.",
            },
            {
                "front": "Vad är setgid på fil?",
                "back": "Fil körs som ägarens grupp. chmod g+s.",
            },
            {
                "front": "Vad är setgid på katalog?",
                "back": "Nya filer i katalogen ärver gruppägare.",
            },
            {
                "front": "Vad är sticky bit (t)?",
                "back": "Endast ägare kan ta bort sina filer i katalogen.",
            },
            {
                "front": "Var används sticky bit?",
                "back": "/tmp - alla kan skriva men bara ta bort sitt eget.",
            },
            {"front": "chmod 1755?", "back": "Sticky bit (1) + rwxr-xr-x."},
            {"front": "chmod 2755?", "back": "SetGID (2) + rwxr-xr-x."},
            {"front": "chmod 4755?", "back": "SetUID (4) + rwxr-xr-x."},
            {
                "front": "Vad gör umask?",
                "back": "Bestämmer default-rättigheter för nya filer.",
            },
            {"front": "umask 022?", "back": "Nya filer: 644, nya kataloger: 755."},
            {
                "front": "Hur beräknas umask?",
                "back": "777-umask för kataloger, 666-umask för filer.",
            },
            {
                "front": "Vad är ACL?",
                "back": "Access Control List - finare rättighetskontroll.",
            },
            {"front": "Vad gör getfacl?", "back": "Visar ACL för fil. getfacl fil."},
            {
                "front": "Vad gör setfacl?",
                "back": "Sätter ACL. setfacl -m u:anna:rw fil.",
            },
            {
                "front": "setfacl -m u:anna:rwx fil?",
                "back": "Ger anna rwx utöver vanliga rättigheter.",
            },
            {
                "front": "setfacl -m g:dev:rx fil?",
                "back": "Ger gruppen dev rx-rättigheter.",
            },
            {"front": "setfacl -x u:anna fil?", "back": "Tar bort annas ACL-entry."},
            {
                "front": "Vad betyder + i ls -l?",
                "back": "-rw-r--r--+ visar att filen har ACL.",
            },
            {
                "front": "Vad är PAM?",
                "back": "Pluggable Authentication Modules - autentiseringsramverk.",
            },
            {
                "front": "Var ligger PAM-config?",
                "back": "/etc/pam.d/ - en fil per tjänst.",
            },
            {
                "front": "Vad är /etc/login.defs?",
                "back": "Standardvärden för användarskapande (UID-range, etc).",
            },
            {
                "front": "Vad är /etc/skel?",
                "back": "Skeleton - filer som kopieras till nya hemkataloger.",
            },
            {
                "front": "Vad gör finger?",
                "back": "Visar information om användare (om installerat).",
            },
            {
                "front": "Vad gör chfn?",
                "back": "Ändrar användarinfo (fullständigt namn, telefon, etc).",
            },
            {"front": "Vad gör chsh?", "back": "Ändrar login-shell för användare."},
            {
                "front": "Var listas giltiga shells?",
                "back": "/etc/shells - shells som är tillåtna.",
            },
            {
                "front": "Vad är /sbin/nologin?",
                "back": "Shell för konton som inte ska kunna logga in.",
            },
            {
                "front": "Hur skapar man systemanvändare?",
                "back": "useradd -r namn - skapar systemkonto utan hemkatalog.",
            },
        ],
        # =====================================================================
        # NOD 6: SSH & SÄKERHET - 100 Flashcards
        # =====================================================================
        "nod6_ssh": [
            {
                "front": "Vad är SSH?",
                "back": "Secure Shell - krypterat protokoll för fjärranslutning.",
            },
            {"front": "SSH standardport?", "back": "22"},
            {
                "front": "Hur ansluter man?",
                "back": "ssh user@host eller ssh -p port user@host",
            },
            {
                "front": "ssh -p 2222 anna@server?",
                "back": "Ansluter på port 2222 istället för 22.",
            },
            {
                "front": "Hur genererar man nyckel?",
                "back": "ssh-keygen - skapar nyckelpar.",
            },
            {
                "front": "ssh-keygen -t ed25519?",
                "back": "Skapar ED25519-nyckel (rekommenderat).",
            },
            {
                "front": "ssh-keygen -t rsa -b 4096?",
                "back": "Skapar RSA-nyckel med 4096 bitar.",
            },
            {
                "front": "Var sparas privat nyckel?",
                "back": "~/.ssh/id_rsa eller ~/.ssh/id_ed25519",
            },
            {
                "front": "Var sparas publik nyckel?",
                "back": "~/.ssh/id_rsa.pub eller ~/.ssh/id_ed25519.pub",
            },
            {"front": "Ska privat nyckel delas?", "back": "ALDRIG! Den är hemlig."},
            {
                "front": "Vad är authorized_keys?",
                "back": "~/.ssh/authorized_keys - publika nycklar som får logga in.",
            },
            {
                "front": "Hur lägger man till nyckel på server?",
                "back": "ssh-copy-id user@host - kopierar publik nyckel.",
            },
            {
                "front": "Vad är known_hosts?",
                "back": "~/.ssh/known_hosts - sparade serverfingerprints.",
            },
            {
                "front": "Varför varnas om host key changed?",
                "back": "Kan vara man-in-the-middle-attack! Verifiera.",
            },
            {
                "front": "Vad gör ssh-agent?",
                "back": "Lagrar olåsta nycklar i minnet för bekvämlighet.",
            },
            {
                "front": "Hur startar man ssh-agent?",
                "back": "eval $(ssh-agent) - startar och exporterar variabler.",
            },
            {"front": "Vad gör ssh-add?", "back": "Lägger till nyckel i ssh-agent."},
            {"front": "ssh-add -l?", "back": "Listar nycklar i agenten."},
            {"front": "ssh-add -D?", "back": "Tar bort alla nycklar från agenten."},
            {
                "front": "Hur kör kommando utan login?",
                "back": "ssh user@host 'kommando' - kör och avslutar.",
            },
            {"front": "Vad gör scp?", "back": "Secure Copy - kopierar filer över SSH."},
            {
                "front": "scp fil user@host:/sökväg?",
                "back": "Kopierar lokal fil till fjärrserver.",
            },
            {
                "front": "scp user@host:/fil .?",
                "back": "Kopierar fil från server till lokalt.",
            },
            {
                "front": "scp -r katalog user@host:?",
                "back": "Kopierar katalog rekursivt.",
            },
            {
                "front": "Vad gör sftp?",
                "back": "Secure FTP - interaktiv filöverföring över SSH.",
            },
            {
                "front": "Vad gör rsync?",
                "back": "Synkroniserar filer effektivt (bara skillnader).",
            },
            {
                "front": "rsync -avz källa dest?",
                "back": "Archive, Verbose, Compress - vanliga flaggor.",
            },
            {
                "front": "rsync -e ssh?",
                "back": "Använd SSH som transport (ofta default).",
            },
            {
                "front": "rsync --delete?",
                "back": "Tar bort filer på dest som inte finns på källa.",
            },
            {"front": "Var är SSH-serverkonfig?", "back": "/etc/ssh/sshd_config"},
            {
                "front": "Var är SSH-klientkonfig?",
                "back": "/etc/ssh/ssh_config (global), ~/.ssh/config (per user).",
            },
            {
                "front": "Hur stänger man av root-login?",
                "back": "PermitRootLogin no i sshd_config.",
            },
            {
                "front": "Hur stänger man av lösenord?",
                "back": "PasswordAuthentication no i sshd_config.",
            },
            {
                "front": "Hur tillåter man bara nycklar?",
                "back": "PubkeyAuthentication yes + PasswordAuthentication no.",
            },
            {
                "front": "Hur begränsar man användare?",
                "back": "AllowUsers anna bob - bara dessa får SSH:a.",
            },
            {
                "front": "Hur begränsar man grupper?",
                "back": "AllowGroups sshusers - bara gruppen får SSH:a.",
            },
            {
                "front": "Hur byter man SSH-port?",
                "back": "Port 2222 i sshd_config. Glöm inte brandvägg!",
            },
            {
                "front": "Hur applicerar man SSH-ändringar?",
                "back": "sudo systemctl restart sshd",
            },
            {
                "front": "Vad är local port forwarding?",
                "back": "ssh -L lokal:host:fjärr - tunnel från din dator.",
            },
            {
                "front": "ssh -L 8080:localhost:80?",
                "back": "Din port 8080 → serverns localhost:80.",
            },
            {
                "front": "Vad är remote port forwarding?",
                "back": "ssh -R fjärr:host:lokal - tunnel till din dator.",
            },
            {
                "front": "Vad är dynamic port forwarding?",
                "back": "ssh -D 1080 - SOCKS-proxy genom SSH.",
            },
            {
                "front": "Vad är SSH jump host?",
                "back": "ssh -J hophost destination - gå via mellanserver.",
            },
            {
                "front": "ProxyJump i config?",
                "back": "ProxyJump hophost - konfigurerar jump host.",
            },
            {
                "front": "Vad är ~/.ssh/config för?",
                "back": "Sparar SSH-inställningar per host.",
            },
            {
                "front": "Host-block i config?",
                "back": "Host namn\\n  Hostname ip\\n  User anna",
            },
            {"front": "Rättigheter ~/.ssh?", "back": "700 (rwx------)"},
            {"front": "Rättigheter authorized_keys?", "back": "600 (rw-------)"},
            {"front": "Rättigheter privat nyckel?", "back": "600 (rw-------)"},
            {
                "front": "Vad är fail2ban?",
                "back": "Blockerar IP:n efter misslyckade inloggningar.",
            },
            {
                "front": "Var loggas SSH?",
                "back": "/var/log/auth.log eller /var/log/secure",
            },
            {
                "front": "Vad gör ssh -v?",
                "back": "Verbose - visar debug-info vid anslutning.",
            },
            {"front": "ssh -vvv?", "back": "Ännu mer debug-info (3 nivåer)."},
            {
                "front": "Vad är X11 forwarding?",
                "back": "ssh -X - kör grafiska program via SSH.",
            },
            {
                "front": "Hur aktiveras X11 forwarding?",
                "back": "X11Forwarding yes i sshd_config + ssh -X.",
            },
            {
                "front": "Vad är agent forwarding?",
                "back": "ssh -A - vidarebefordra ssh-agent till server.",
            },
            {
                "front": "Varför är -A riskabelt?",
                "back": "Server kan använda din agent för vidare anslutningar.",
            },
            {
                "front": "Vad är ControlMaster?",
                "back": "Delar SSH-anslutning för snabbare upprepade sessioner.",
            },
            {
                "front": "ControlMaster auto?",
                "back": "Skapar delad anslutning om ingen finns.",
            },
            {
                "front": "ControlPath i config?",
                "back": "Sökväg för socket. ~/.ssh/sockets/%r@%h-%p",
            },
            {
                "front": "ControlPersist?",
                "back": "Hur länge bakgrundsanslutning lever. 10m = 10 min.",
            },
            {
                "front": "Vad är SSH escape-sekvenser?",
                "back": "~. avslutar, ~? visar hjälp (efter Enter).",
            },
            {
                "front": "Hur avslutar man hängd SSH?",
                "back": "Enter, sedan ~. (tilde punkt).",
            },
            {
                "front": "~C i SSH?",
                "back": "Öppnar kommandorad för port forwarding i session.",
            },
            {
                "front": "Vad är host key fingerprint?",
                "back": "Unik identifierare för serverns nyckel.",
            },
            {
                "front": "ssh-keyscan?",
                "back": "Hämtar host key från server. ssh-keyscan server.",
            },
            {
                "front": "StrictHostKeyChecking?",
                "back": "yes = avvisa okända, no = acceptera (riskabelt).",
            },
            {
                "front": "Vad är sshd?",
                "back": "SSH daemon - servern som lyssnar på anslutningar.",
            },
            {
                "front": "Hur testar man sshd-config?",
                "back": "sshd -t - testar syntax utan att starta om.",
            },
            {
                "front": "Vad är authorized_keys options?",
                "back": "Begränsningar före nyckel: command=, from=, etc.",
            },
            {
                "front": "from= i authorized_keys?",
                "back": 'from="192.168.1.*" - begränsa varifrån nyckeln får användas.',
            },
            {
                "front": "command= i authorized_keys?",
                "back": 'command="git-shell" - tvingar specifikt kommando.',
            },
            {
                "front": "Vad är ForwardAgent?",
                "back": "yes/no - om agent forwarding ska vara på.",
            },
            {"front": "Vad är Compression?", "back": "yes - komprimerar SSH-trafik."},
            {
                "front": "Vad är ServerAliveInterval?",
                "back": "Sekunder mellan keepalive-paket.",
            },
            {
                "front": "ServerAliveCountMax?",
                "back": "Antal missade keepalives innan disconnect.",
            },
            {"front": "TCPKeepAlive?", "back": "yes - TCP-nivå keepalive (default)."},
            {
                "front": "Vad är ClientAliveInterval?",
                "back": "Server-setting för keepalive till klient.",
            },
            {
                "front": "HashKnownHosts?",
                "back": "yes - hashar hostnamn i known_hosts.",
            },
            {
                "front": "Vad är SSH tunneling?",
                "back": "Skicka annan trafik genom krypterad SSH-anslutning.",
            },
            {
                "front": "Vad är reverse SSH tunnel?",
                "back": "Server ansluter till dig, du når server bakom NAT.",
            },
            {
                "front": "SSH multiplexing?",
                "back": "Dela en TCP-anslutning för flera SSH-sessioner.",
            },
            {
                "front": "Vad är SSH bastion host?",
                "back": "Säker språngbräda för att nå interna servrar.",
            },
            {
                "front": "Vad är SSH certificate?",
                "back": "Alternativ till authorized_keys, signerad av CA.",
            },
            {
                "front": "ssh-keygen -s ca_key?",
                "back": "Signerar användarnyckel med CA-nyckel.",
            },
            {
                "front": "Vad är ecdsa-sk/ed25519-sk?",
                "back": "Hardware security key-backade SSH-nycklar.",
            },
            {
                "front": "Hur listar man anslutna SSH-sessioner?",
                "back": "who eller w - visar inloggade användare.",
            },
            {
                "front": "Hur tar man bort gammal host key?",
                "back": "ssh-keygen -R hostname - tar bort från known_hosts.",
            },
            {
                "front": "LogLevel i sshd_config?",
                "back": "VERBOSE eller DEBUG för mer loggning.",
            },
            {
                "front": "Vad är 2FA för SSH?",
                "back": "Tvåfaktorsautentisering - t.ex. Google Authenticator.",
            },
            {
                "front": "Hur installerar man 2FA SSH?",
                "back": "libpam-google-authenticator + PAM-config.",
            },
        ],
        # =====================================================================
        # NOD 7: FIREWALL & NÄTVERK - 100 Flashcards
        # =====================================================================
        "nod7_firewall": [
            {
                "front": "Vad är UFW?",
                "back": "Uncomplicated Firewall - användarvänligt gränssnitt för iptables.",
            },
            {"front": "Hur aktiverar man UFW?", "back": "sudo ufw enable"},
            {"front": "Hur inaktiverar man UFW?", "back": "sudo ufw disable"},
            {
                "front": "Hur kollar man UFW-status?",
                "back": "sudo ufw status eller ufw status verbose",
            },
            {"front": "ufw allow ssh?", "back": "Tillåter SSH-trafik (port 22)."},
            {"front": "ufw allow 80/tcp?", "back": "Tillåter TCP på port 80."},
            {"front": "ufw deny 23?", "back": "Blockerar port 23 (Telnet)."},
            {
                "front": "ufw delete allow 80?",
                "back": "Tar bort regeln som tillåter port 80.",
            },
            {
                "front": "ufw allow from 192.168.1.0/24?",
                "back": "Tillåter hela subnätet 192.168.1.x.",
            },
            {
                "front": "ufw allow from 10.0.0.5 to any port 22?",
                "back": "Tillåter SSH endast från specifik IP.",
            },
            {
                "front": "ufw default deny incoming?",
                "back": "Blockerar all inkommande trafik som default.",
            },
            {
                "front": "ufw default allow outgoing?",
                "back": "Tillåter all utgående trafik som default.",
            },
            {"front": "ufw reset?", "back": "Återställer alla regler till default."},
            {
                "front": "ufw status numbered?",
                "back": "Visar regler med nummer för enkel borttagning.",
            },
            {"front": "ufw delete 3?", "back": "Tar bort regel nummer 3."},
            {
                "front": "ufw logging on?",
                "back": "Aktiverar loggning av brandväggshändelser.",
            },
            {
                "front": "ufw allow 6000:6007/tcp?",
                "back": "Tillåter port-range 6000-6007 TCP.",
            },
            {
                "front": "ufw app list?",
                "back": "Listar fördefinierade applikationsprofiler.",
            },
            {
                "front": "ufw allow 'Nginx Full'?",
                "back": "Tillåter både HTTP och HTTPS för Nginx.",
            },
            {
                "front": "ufw insert 1 deny from 10.0.0.5?",
                "back": "Infogar regel först (prioritet).",
            },
            {
                "front": "Vad är iptables?",
                "back": "Linux kärnans klassiska brandväggsverktyg.",
            },
            {
                "front": "iptables -L?",
                "back": "Listar alla regler. -n för numeriskt, -v för verbose.",
            },
            {
                "front": "iptables chains?",
                "back": "INPUT (in), OUTPUT (ut), FORWARD (vidare).",
            },
            {
                "front": "iptables -A INPUT?",
                "back": "Append - lägg till regel i INPUT-kedjan.",
            },
            {
                "front": "iptables -I INPUT?",
                "back": "Insert - lägg till regel först i INPUT.",
            },
            {
                "front": "iptables -D INPUT 3?",
                "back": "Delete - ta bort regel 3 från INPUT.",
            },
            {"front": "iptables -F?", "back": "Flush - ta bort alla regler."},
            {
                "front": "iptables -P INPUT DROP?",
                "back": "Policy - sätt default till DROP för INPUT.",
            },
            {"front": "-j ACCEPT?", "back": "Jump to ACCEPT - tillåt paketet."},
            {"front": "-j DROP?", "back": "Jump to DROP - kasta paketet tyst."},
            {"front": "-j REJECT?", "back": "Avvisa och skicka felmeddelande."},
            {"front": "-s 192.168.1.0/24?", "back": "Source - matcha källadress."},
            {
                "front": "-d 10.0.0.5?",
                "back": "Destination - matcha destinationsadress.",
            },
            {"front": "--dport 80?", "back": "Destination port - matcha port 80."},
            {"front": "--sport 443?", "back": "Source port - matcha källport 443."},
            {"front": "-p tcp?", "back": "Protocol - matcha TCP-trafik."},
            {"front": "-i eth0?", "back": "Interface in - matcha inkommande på eth0."},
            {"front": "-o eth1?", "back": "Interface out - matcha utgående på eth1."},
            {
                "front": "-m state --state ESTABLISHED?",
                "back": "Matcha etablerade anslutningar.",
            },
            {"front": "iptables-save > rules.v4?", "back": "Spara regler till fil."},
            {"front": "iptables-restore < rules.v4?", "back": "Ladda regler från fil."},
            {"front": "Vad är nftables?", "back": "Modernare ersättare för iptables."},
            {"front": "nft list ruleset?", "back": "Visa alla nftables-regler."},
            {
                "front": "Vad är firewalld?",
                "back": "Dynamisk brandvägg, standard på RHEL/CentOS.",
            },
            {"front": "firewall-cmd --state?", "back": "Visa om firewalld är aktiv."},
            {
                "front": "firewall-cmd --list-all?",
                "back": "Lista alla regler och zoner.",
            },
            {
                "front": "firewall-cmd --add-service=http?",
                "back": "Tillåt HTTP (tillfälligt).",
            },
            {"front": "firewall-cmd --permanent?", "back": "Gör ändring permanent."},
            {
                "front": "firewall-cmd --reload?",
                "back": "Ladda om permanent konfiguration.",
            },
            {"front": "firewall-cmd --get-zones?", "back": "Lista tillgängliga zoner."},
            {
                "front": "firewall-cmd --zone=public?",
                "back": "Ange vilken zon regeln gäller.",
            },
            {"front": "Vad är ss?", "back": "Socket Statistics - ersätter netstat."},
            {"front": "ss -tulpn?", "back": "TCP/UDP listening portar med process."},
            {"front": "ss -t?", "back": "Visa TCP-anslutningar."},
            {"front": "ss -u?", "back": "Visa UDP-sockets."},
            {"front": "ss -l?", "back": "Visa lyssnande sockets."},
            {"front": "ss -n?", "back": "Visa numeriskt (ej resolva namn)."},
            {"front": "ss -p?", "back": "Visa process som äger socket."},
            {
                "front": "Vad är netstat?",
                "back": "Äldre verktyg för nätverksstatistik.",
            },
            {
                "front": "netstat -tulpn?",
                "back": "TCP/UDP listening med PID (samma som ss).",
            },
            {"front": "Vad gör ping?", "back": "Testar anslutning med ICMP echo."},
            {"front": "ping -c 4 host?", "back": "Skicka 4 ping och avsluta."},
            {
                "front": "Vad gör traceroute?",
                "back": "Visar vägen paket tar till destination.",
            },
            {
                "front": "traceroute google.com?",
                "back": "Visa alla hopp till google.com.",
            },
            {
                "front": "Vad gör mtr?",
                "back": "My TraceRoute - kombinerar ping och traceroute.",
            },
            {
                "front": "Vad gör nmap?",
                "back": "Network mapper - skannar portar och tjänster.",
            },
            {"front": "nmap -p 22,80,443 host?", "back": "Skanna specifika portar."},
            {"front": "nmap -sV host?", "back": "Service/version detection."},
            {"front": "nmap -O host?", "back": "OS-detection."},
            {"front": "nmap 192.168.1.0/24?", "back": "Skanna hela subnätet."},
            {
                "front": "Vad gör nc (netcat)?",
                "back": "Swiss army knife - läsa/skriva nätverksdata.",
            },
            {"front": "nc -zv host 22?", "back": "Testa om port 22 är öppen."},
            {"front": "nc -l 8080?", "back": "Lyssna på port 8080."},
            {
                "front": "Vad gör tcpdump?",
                "back": "Fångar och analyserar nätverkstrafik.",
            },
            {"front": "tcpdump -i eth0?", "back": "Fånga trafik på interface eth0."},
            {"front": "tcpdump port 80?", "back": "Fånga endast HTTP-trafik."},
            {"front": "tcpdump -w capture.pcap?", "back": "Spara till fil för analys."},
            {"front": "Vad gör wireshark?", "back": "GUI-baserad paketanalys."},
            {"front": "Vad gör ip addr?", "back": "Visa IP-adresser på interfaces."},
            {"front": "Vad gör ip route?", "back": "Visa routing-tabell."},
            {"front": "Vad gör ip link?", "back": "Visa nätverksinterfaces."},
            {
                "front": "ip addr add 10.0.0.1/24 dev eth0?",
                "back": "Lägg till IP på interface.",
            },
            {
                "front": "ip route add default via 10.0.0.254?",
                "back": "Lägg till default gateway.",
            },
            {"front": "Vad gör dig?", "back": "DNS-lookup verktyg."},
            {"front": "dig google.com?", "back": "Fråga DNS om google.com."},
            {"front": "dig +short google.com?", "back": "Bara visa IP-adressen."},
            {"front": "Vad gör nslookup?", "back": "Äldre DNS-lookup verktyg."},
            {"front": "Vad gör host?", "back": "Enkel DNS-lookup."},
            {"front": "Var konfigureras DNS?", "back": "/etc/resolv.conf"},
            {"front": "Var konfigureras hosts lokalt?", "back": "/etc/hosts"},
            {"front": "Vad gör curl?", "back": "Hämtar data från URL."},
            {"front": "curl -I url?", "back": "Visa bara HTTP-headers."},
            {"front": "Vad gör wget?", "back": "Laddar ner filer från webb."},
            {"front": "wget -c url?", "back": "Fortsätt avbruten nedladdning."},
        ],
        # =====================================================================
        # NOD 8: DOCKER BASICS - 100 Flashcards
        # =====================================================================
        "nod8_docker_basics": [
            {
                "front": "Vad är Docker?",
                "back": "Containerplattform - paketerar app + beroenden.",
            },
            {
                "front": "Container vs VM?",
                "back": "Container delar OS-kärna, VM har egen kärna = lättare.",
            },
            {
                "front": "Vad är Docker image?",
                "back": "Skrivskyddad mall för att skapa containers.",
            },
            {"front": "Vad är container?", "back": "Körande instans av en image."},
            {
                "front": "Vad är Docker daemon?",
                "back": "Bakgrundsprocess som hanterar containers (dockerd).",
            },
            {
                "front": "Vad är Docker client?",
                "back": "Kommandoradsverktyget docker som pratar med daemon.",
            },
            {
                "front": "Vad är Docker Hub?",
                "back": "Publikt registry för Docker images.",
            },
            {
                "front": "docker pull nginx?",
                "back": "Hämta nginx-image från Docker Hub.",
            },
            {"front": "docker images?", "back": "Lista alla lokala images."},
            {"front": "docker image ls?", "back": "Samma som docker images."},
            {"front": "docker ps?", "back": "Lista körande containers."},
            {
                "front": "docker ps -a?",
                "back": "Lista ALLA containers (även stoppade).",
            },
            {
                "front": "docker run nginx?",
                "back": "Skapa och starta container från nginx-image.",
            },
            {"front": "docker run -d nginx?", "back": "Kör detached (i bakgrunden)."},
            {
                "front": "docker run -p 8080:80?",
                "back": "Mappa värd-port 8080 till container-port 80.",
            },
            {
                "front": "docker run --name web nginx?",
                "back": "Ge containern namnet 'web'.",
            },
            {
                "front": "docker run --rm nginx?",
                "back": "Ta bort container automatiskt när den stoppas.",
            },
            {
                "front": "docker run -it ubuntu bash?",
                "back": "Interaktiv terminal i ubuntu-container.",
            },
            {"front": "Vad betyder -i?", "back": "Interactive - håll stdin öppen."},
            {"front": "Vad betyder -t?", "back": "TTY - allokera pseudo-terminal."},
            {
                "front": "docker stop web?",
                "back": "Stoppa container (SIGTERM, sen SIGKILL).",
            },
            {
                "front": "docker kill web?",
                "back": "Tvångsstoppa container (SIGKILL direkt).",
            },
            {"front": "docker start web?", "back": "Starta stoppad container."},
            {"front": "docker restart web?", "back": "Starta om container."},
            {"front": "docker rm web?", "back": "Ta bort stoppad container."},
            {"front": "docker rm -f web?", "back": "Tvinga bort körande container."},
            {"front": "docker rmi nginx?", "back": "Ta bort image."},
            {
                "front": "docker exec -it web bash?",
                "back": "Öppna shell i körande container.",
            },
            {"front": "docker exec web ls?", "back": "Kör ls i körande container."},
            {"front": "docker logs web?", "back": "Visa container-loggar."},
            {"front": "docker logs -f web?", "back": "Följ loggar i realtid."},
            {"front": "docker logs --tail 100 web?", "back": "Visa sista 100 rader."},
            {
                "front": "docker inspect web?",
                "back": "Visa detaljerad JSON-info om container.",
            },
            {
                "front": "docker stats?",
                "back": "Visa CPU/RAM-användning för containers.",
            },
            {"front": "docker top web?", "back": "Visa processer i container."},
            {"front": "docker diff web?", "back": "Visa filändringar i container."},
            {"front": "docker cp fil web:/app?", "back": "Kopiera fil till container."},
            {
                "front": "docker cp web:/app/fil .?",
                "back": "Kopiera fil från container.",
            },
            {
                "front": "Vad är volume?",
                "back": "Persistent lagring som överlever container-borttag.",
            },
            {
                "front": "docker volume create mydata?",
                "back": "Skapa namngiven volume.",
            },
            {"front": "docker volume ls?", "back": "Lista volumes."},
            {"front": "docker volume inspect mydata?", "back": "Visa volume-detaljer."},
            {"front": "-v mydata:/app?", "back": "Montera volume i container."},
            {"front": "-v $(pwd):/app?", "back": "Bind mount - montera lokal katalog."},
            {
                "front": "Skillnad volume vs bind mount?",
                "back": "Volume hanteras av Docker, bind mount är lokal sökväg.",
            },
            {
                "front": "Vad är Docker network?",
                "back": "Isolerat nätverk för container-kommunikation.",
            },
            {"front": "docker network ls?", "back": "Lista nätverk."},
            {"front": "docker network create mynet?", "back": "Skapa nätverk."},
            {"front": "--network mynet?", "back": "Anslut container till nätverk."},
            {
                "front": "Bridge network?",
                "back": "Default - containers kan kommunicera via IP.",
            },
            {
                "front": "Host network?",
                "back": "Delar värd-nätverket (ingen isolation).",
            },
            {
                "front": "docker run -e VAR=val?",
                "back": "Sätt miljövariabel i container.",
            },
            {
                "front": "docker run --env-file .env?",
                "back": "Ladda miljövariabler från fil.",
            },
            {
                "front": "docker commit web myimage?",
                "back": "Skapa image från container.",
            },
            {"front": "docker tag image:tag?", "back": "Tagga image med nytt namn."},
            {"front": "docker push myimage?", "back": "Pusha image till registry."},
            {"front": "docker login?", "back": "Logga in på Docker Hub."},
            {"front": "docker logout?", "back": "Logga ut från Docker Hub."},
            {"front": "docker search nginx?", "back": "Sök images på Docker Hub."},
            {
                "front": "docker history nginx?",
                "back": "Visa image-lager och kommandon.",
            },
            {
                "front": "docker system df?",
                "back": "Visa diskutrymme som Docker använder.",
            },
            {
                "front": "docker system prune?",
                "back": "Ta bort oanvända data (containers, images, etc).",
            },
            {
                "front": "docker container prune?",
                "back": "Ta bort stoppade containers.",
            },
            {"front": "docker image prune?", "back": "Ta bort oanvända images."},
            {"front": "docker volume prune?", "back": "Ta bort oanvända volumes."},
            {
                "front": "Vad är restart policy?",
                "back": "Hur Docker hanterar container-restart.",
            },
            {
                "front": "--restart=always?",
                "back": "Starta alltid om, även vid reboot.",
            },
            {
                "front": "--restart=unless-stopped?",
                "back": "Starta om om inte manuellt stoppad.",
            },
            {
                "front": "--restart=on-failure?",
                "back": "Starta om bara vid fel (exit code != 0).",
            },
            {"front": "docker rename old new?", "back": "Byt namn på container."},
            {
                "front": "docker pause web?",
                "back": "Pausa container (freeze processer).",
            },
            {"front": "docker unpause web?", "back": "Återuppta pausad container."},
            {
                "front": "docker attach web?",
                "back": "Anslut terminal till körande container.",
            },
            {
                "front": "docker create nginx?",
                "back": "Skapa container utan att starta.",
            },
            {
                "front": "docker update --memory 512m web?",
                "back": "Uppdatera resursbegränsningar.",
            },
            {"front": "--memory 512m?", "back": "Begränsa RAM till 512 MB."},
            {"front": "--cpus 0.5?", "back": "Begränsa till 0.5 CPU-kärnor."},
            {"front": "docker port web?", "back": "Visa portmappningar för container."},
            {
                "front": "docker wait web?",
                "back": "Vänta tills container stoppas, visa exit code.",
            },
            {"front": "docker events?", "back": "Streama Docker-händelser i realtid."},
            {"front": "docker info?", "back": "Visa Docker-systeminfo."},
            {
                "front": "docker version?",
                "back": "Visa Docker-versioner (client och server).",
            },
            {
                "front": "ENTRYPOINT vs CMD?",
                "back": "ENTRYPOINT = fast kommando, CMD = default argument.",
            },
            {
                "front": "docker save -o nginx.tar nginx?",
                "back": "Exportera image till tar-fil.",
            },
            {
                "front": "docker load -i nginx.tar?",
                "back": "Importera image från tar-fil.",
            },
            {
                "front": "docker export -o backup.tar web?",
                "back": "Exportera container-filsystem.",
            },
            {
                "front": "docker import backup.tar?",
                "back": "Importera filsystem som image.",
            },
            {
                "front": "Vad är container layer?",
                "back": "Skrivbart lager ovanpå image-lager.",
            },
            {
                "front": "Vad är Union filesystem?",
                "back": "Hur Docker staplar lager till ett filsystem.",
            },
        ],
        # =====================================================================
        # NOD 9: DOCKER COMPOSE - 100 Flashcards
        # =====================================================================
        "nod9_docker_compose": [
            {
                "front": "Vad är Docker Compose?",
                "back": "Verktyg för att definiera och köra multi-container appar.",
            },
            {
                "front": "Standard compose-fil?",
                "back": "docker-compose.yml eller compose.yaml",
            },
            {
                "front": "docker compose up?",
                "back": "Startar alla tjänster definierade i compose-fil.",
            },
            {
                "front": "docker compose up -d?",
                "back": "Startar i bakgrunden (detached).",
            },
            {
                "front": "docker compose down?",
                "back": "Stoppar och tar bort containers, nätverk.",
            },
            {"front": "docker compose down -v?", "back": "Tar även bort volumes."},
            {
                "front": "docker compose stop?",
                "back": "Stoppar containers utan att ta bort dem.",
            },
            {"front": "docker compose start?", "back": "Startar stoppade containers."},
            {"front": "docker compose restart?", "back": "Startar om alla tjänster."},
            {
                "front": "docker compose ps?",
                "back": "Listar körande compose-containers.",
            },
            {
                "front": "docker compose logs?",
                "back": "Visar loggar för alla tjänster.",
            },
            {"front": "docker compose logs -f?", "back": "Följer loggar i realtid."},
            {
                "front": "docker compose logs web?",
                "back": "Loggar för specifik tjänst.",
            },
            {
                "front": "docker compose exec web bash?",
                "back": "Kör bash i körande container.",
            },
            {
                "front": "docker compose run web bash?",
                "back": "Skapar NY container och kör bash.",
            },
            {
                "front": "Skillnad exec och run?",
                "back": "exec = befintlig container, run = skapar ny.",
            },
            {
                "front": "docker compose build?",
                "back": "Bygger images definierade med build:.",
            },
            {
                "front": "docker compose pull?",
                "back": "Hämtar senaste images från registry.",
            },
            {
                "front": "docker compose push?",
                "back": "Pushar byggda images till registry.",
            },
            {
                "front": "docker compose config?",
                "back": "Validerar och visar compose-konfiguration.",
            },
            {
                "front": "-f docker-compose.prod.yml?",
                "back": "Anger specifik compose-fil.",
            },
            {
                "front": "-p projektnamn?",
                "back": "Sätter projektnamn (prefix för containers).",
            },
            {
                "front": "Vad är services:?",
                "back": "Definierar containers/tjänster som ska köras.",
            },
            {"front": "Vad är volumes:?", "back": "Definierar persistent lagring."},
            {"front": "Vad är networks:?", "back": "Definierar anpassade nätverk."},
            {"front": "image: nginx?", "back": "Använd nginx-image från registry."},
            {"front": "build: ./app?", "back": "Bygg image från Dockerfile i ./app."},
            {
                "front": "build context och dockerfile?",
                "back": "build:\\n  context: .\\n  dockerfile: Dockerfile.dev",
            },
            {
                "front": "ports:?",
                "back": "Mappar portar: - '8080:80' (värd:container).",
            },
            {
                "front": "expose:?",
                "back": "Exponerar port internt för andra containers.",
            },
            {
                "front": "Skillnad ports och expose?",
                "back": "ports = externt tillgänglig, expose = bara internt.",
            },
            {"front": "environment:?", "back": "Sätter miljövariabler i container."},
            {
                "front": "environment lista?",
                "back": "environment:\\n  - DEBUG=true\\n  - API_KEY=abc",
            },
            {
                "front": "environment dict?",
                "back": "environment:\\n  DEBUG: 'true'\\n  API_KEY: abc",
            },
            {
                "front": "env_file:?",
                "back": "Laddar miljövariabler från fil. env_file: .env",
            },
            {
                "front": "volumes: short syntax?",
                "back": "volumes:\\n  - ./data:/app/data",
            },
            {
                "front": "volumes: named volume?",
                "back": "volumes:\\n  - mydata:/app/data",
            },
            {"front": "depends_on:?", "back": "Definierar startordning/beroenden."},
            {"front": "depends_on: lista?", "back": "depends_on:\\n  - db\\n  - redis"},
            {"front": "command:?", "back": "Överskrider image:s CMD."},
            {"front": "entrypoint:?", "back": "Överskrider image:s ENTRYPOINT."},
            {
                "front": "restart:?",
                "back": "Restart policy: no, always, on-failure, unless-stopped.",
            },
            {
                "front": "restart: always?",
                "back": "Starta alltid om vid krasch/reboot.",
            },
            {
                "front": "restart: unless-stopped?",
                "back": "Starta om om inte manuellt stoppad.",
            },
            {"front": "container_name:?", "back": "Sätter specifikt containernamn."},
            {"front": "hostname:?", "back": "Sätter hostname inuti containern."},
            {"front": "working_dir:?", "back": "Sätter arbetskatalog i container."},
            {
                "front": "user:?",
                "back": "Kör som specifik användare. user: '1000:1000'",
            },
            {"front": "healthcheck:?", "back": "Definierar hälsokontroll för tjänst."},
            {
                "front": "healthcheck test?",
                "back": "healthcheck:\\n  test: curl -f http://localhost/",
            },
            {
                "front": "healthcheck interval?",
                "back": "Hur ofta check körs. interval: 30s",
            },
            {
                "front": "healthcheck timeout?",
                "back": "Max tid för check. timeout: 10s",
            },
            {
                "front": "healthcheck retries?",
                "back": "Antal försök innan unhealthy. retries: 3",
            },
            {"front": "logging:?", "back": "Konfigurerar container-loggning."},
            {"front": "logging driver?", "back": "logging:\\n  driver: json-file"},
            {
                "front": "logging options?",
                "back": "options:\\n  max-size: '10m'\\n  max-file: '3'",
            },
            {"front": "labels:?", "back": "Metadata för containers."},
            {"front": "deploy:?", "back": "Deployment-konfiguration (Swarm/k8s)."},
            {"front": "deploy replicas?", "back": "deploy:\\n  replicas: 3"},
            {"front": "deploy resources?", "back": "Resursbegränsningar i deploy."},
            {"front": "profiles:?", "back": "Aktivera tjänster baserat på profil."},
            {
                "front": "--profile debug?",
                "back": "Startar tjänster med profil 'debug'.",
            },
            {
                "front": "extends:?",
                "back": "Ärver konfiguration från annan tjänst/fil.",
            },
            {
                "front": "networks: i tjänst?",
                "back": "Anger vilka nätverk tjänsten ska ansluta till.",
            },
            {
                "front": "network_mode: host?",
                "back": "Använd värd-nätverk (ingen isolation).",
            },
            {"front": "extra_hosts:?", "back": "Lägg till entries i /etc/hosts."},
            {"front": "dns:?", "back": "Ange DNS-servrar. dns: 8.8.8.8"},
            {"front": "cap_add:?", "back": "Lägg till Linux capabilities."},
            {"front": "cap_drop:?", "back": "Ta bort Linux capabilities."},
            {
                "front": "privileged:?",
                "back": "Kör med utökade privilegier (farligt!).",
            },
            {"front": "read_only:?", "back": "Skrivskyddat filsystem i container."},
            {"front": "stdin_open:?", "back": "Håll stdin öppen (motsvarar -i)."},
            {"front": "tty:?", "back": "Allokera pseudo-TTY (motsvarar -t)."},
            {"front": "secrets:?", "back": "Hantera känslig data säkert."},
            {"front": "configs:?", "back": "Hantera konfigurationsfiler."},
            {"front": "version:?", "back": "Compose-filversion (deprecated i v3.8+)."},
            {
                "front": "Variable substitution?",
                "back": "${VAR} i compose använder miljövariabler.",
            },
            {"front": "${VAR:-default}?", "back": "Använd 'default' om VAR ej satt."},
            {"front": "${VAR:?error}?", "back": "Ge fel om VAR ej satt."},
            {
                "front": ".env i samma katalog?",
                "back": "Laddas automatiskt av compose.",
            },
            {
                "front": "docker compose up --build?",
                "back": "Bygg om images innan start.",
            },
            {
                "front": "docker compose up --force-recreate?",
                "back": "Skapa om containers även om config ej ändrats.",
            },
            {"front": "--scale web=3?", "back": "Starta 3 instanser av web-tjänst."},
            {
                "front": "docker compose top?",
                "back": "Visa processer i alla containers.",
            },
            {"front": "docker compose events?", "back": "Streama compose-händelser."},
            {"front": "docker compose images?", "back": "Lista images som används."},
            {
                "front": "docker compose port web 80?",
                "back": "Visa publik port för container-port 80.",
            },
            {
                "front": "docker compose kill?",
                "back": "Tvångsstoppar containers (SIGKILL).",
            },
            {"front": "docker compose pause?", "back": "Pausar alla containers."},
            {
                "front": "docker compose unpause?",
                "back": "Återupptar pausade containers.",
            },
            {"front": "docker compose rm?", "back": "Tar bort stoppade containers."},
            {
                "front": "docker compose convert?",
                "back": "Konvertera compose-fil till annat format.",
            },
        ],
        # =====================================================================
        # NOD 10: SYSTEMD - 100 Flashcards
        # =====================================================================
        "nod10_systemd": [
            {
                "front": "Vad är systemd?",
                "back": "Init-system och service manager för Linux.",
            },
            {
                "front": "Vad är init?",
                "back": "Första processen (PID 1) som startar alla andra.",
            },
            {
                "front": "Vad är en unit?",
                "back": "Resurs som systemd hanterar - service, mount, timer...",
            },
            {
                "front": "Vad är en service unit?",
                "back": "Definierar en tjänst/daemon.",
            },
            {
                "front": "Vad är en target unit?",
                "back": "Grupp av units, motsvarar runlevels.",
            },
            {
                "front": "Vad är en mount unit?",
                "back": "Definierar en filsystem-montering.",
            },
            {
                "front": "Vad är en socket unit?",
                "back": "Socket-baserad aktivering av tjänster.",
            },
            {
                "front": "Vad är en timer unit?",
                "back": "Schemalagda uppgifter (som cron).",
            },
            {
                "front": "Var ligger system-units?",
                "back": "/lib/systemd/system/ (paket-installerade).",
            },
            {
                "front": "Var lägger man egna units?",
                "back": "/etc/systemd/system/ (admin-skapade).",
            },
            {"front": "systemctl start nginx?", "back": "Starta nginx-tjänsten nu."},
            {"front": "systemctl stop nginx?", "back": "Stoppa nginx-tjänsten."},
            {
                "front": "systemctl restart nginx?",
                "back": "Stoppa och starta om nginx.",
            },
            {
                "front": "systemctl reload nginx?",
                "back": "Ladda om config utan att stoppa.",
            },
            {
                "front": "systemctl status nginx?",
                "back": "Visa status, PID, senaste loggar.",
            },
            {
                "front": "systemctl enable nginx?",
                "back": "Aktivera autostart vid boot.",
            },
            {
                "front": "systemctl disable nginx?",
                "back": "Inaktivera autostart vid boot.",
            },
            {"front": "systemctl is-active nginx?", "back": "Kolla om tjänst körs."},
            {
                "front": "systemctl is-enabled nginx?",
                "back": "Kolla om autostart är på.",
            },
            {
                "front": "systemctl is-failed nginx?",
                "back": "Kolla om tjänst har crashat.",
            },
            {"front": "systemctl list-units?", "back": "Lista alla aktiva units."},
            {
                "front": "systemctl list-units --type=service?",
                "back": "Lista bara service-units.",
            },
            {
                "front": "systemctl list-units --failed?",
                "back": "Lista misslyckade units.",
            },
            {
                "front": "systemctl list-unit-files?",
                "back": "Lista alla installerade units.",
            },
            {
                "front": "systemctl cat nginx.service?",
                "back": "Visa unit-filens innehåll.",
            },
            {
                "front": "systemctl show nginx?",
                "back": "Visa alla egenskaper för tjänst.",
            },
            {"front": "systemctl edit nginx?", "back": "Redigera/override unit-fil."},
            {
                "front": "systemctl daemon-reload?",
                "back": "Ladda om ändrade unit-filer.",
            },
            {
                "front": "systemctl mask nginx?",
                "back": "Förhindra att tjänsten kan startas.",
            },
            {
                "front": "systemctl unmask nginx?",
                "back": "Ta bort mask, tillåt start igen.",
            },
            {"front": "systemctl get-default?", "back": "Visa default boot-target."},
            {
                "front": "systemctl set-default multi-user.target?",
                "back": "Sätt boot utan GUI.",
            },
            {
                "front": "systemctl isolate rescue.target?",
                "back": "Byt till rescue mode nu.",
            },
            {"front": "systemctl reboot?", "back": "Starta om systemet."},
            {"front": "systemctl poweroff?", "back": "Stäng av systemet."},
            {
                "front": "[Unit]-sektion?",
                "back": "Metadata: Description, After, Requires...",
            },
            {
                "front": "[Service]-sektion?",
                "back": "Körning: ExecStart, Type, User, Restart...",
            },
            {"front": "[Install]-sektion?", "back": "Aktivering: WantedBy, Alias..."},
            {"front": "Description=?", "back": "Beskrivning av tjänsten."},
            {"front": "After=?", "back": "Starta efter dessa units (ordning)."},
            {"front": "Before=?", "back": "Starta före dessa units (ordning)."},
            {"front": "Requires=?", "back": "Hårt beroende - måste vara igång."},
            {"front": "Wants=?", "back": "Mjukt beroende - starta om möjligt."},
            {"front": "Conflicts=?", "back": "Kan inte köras samtidigt som dessa."},
            {"front": "Type=simple?", "back": "Default - processen är huvudprocessen."},
            {"front": "Type=forking?", "back": "Tjänsten forkar och parent exits."},
            {"front": "Type=oneshot?", "back": "Körs en gång och avslutas."},
            {"front": "Type=notify?", "back": "Tjänsten signalerar när den är redo."},
            {"front": "ExecStart=?", "back": "Kommando för att starta tjänsten."},
            {"front": "ExecStop=?", "back": "Kommando för att stoppa tjänsten."},
            {"front": "ExecReload=?", "back": "Kommando för att ladda om config."},
            {"front": "ExecStartPre=?", "back": "Kör innan huvudkommandot."},
            {"front": "ExecStartPost=?", "back": "Kör efter huvudkommandot startat."},
            {"front": "Restart=always?", "back": "Starta alltid om vid exit."},
            {"front": "Restart=on-failure?", "back": "Starta om bara vid fel-exit."},
            {"front": "RestartSec=5?", "back": "Vänta 5 sekunder innan omstart."},
            {"front": "User=www-data?", "back": "Kör som användare www-data."},
            {"front": "Group=www-data?", "back": "Kör med grupp www-data."},
            {"front": "WorkingDirectory=?", "back": "Arbetskatalog för tjänsten."},
            {"front": "Environment=?", "back": "Sätt miljövariabel."},
            {"front": "EnvironmentFile=?", "back": "Ladda miljövariabler från fil."},
            {"front": "StandardOutput=journal?", "back": "Skicka stdout till journal."},
            {"front": "StandardError=journal?", "back": "Skicka stderr till journal."},
            {
                "front": "WantedBy=multi-user.target?",
                "back": "Aktiveras vid normal boot.",
            },
            {"front": "WantedBy=graphical.target?", "back": "Aktiveras vid GUI boot."},
            {"front": "journalctl?", "back": "Visa systemloggar."},
            {"front": "journalctl -u nginx?", "back": "Loggar för nginx-tjänst."},
            {"front": "journalctl -f?", "back": "Följ loggar i realtid."},
            {"front": "journalctl -b?", "back": "Loggar sedan boot."},
            {"front": "journalctl -b -1?", "back": "Loggar från förra boot."},
            {"front": "journalctl --since today?", "back": "Loggar från idag."},
            {"front": "journalctl --since '2024-01-01'?", "back": "Loggar från datum."},
            {"front": "journalctl -p err?", "back": "Bara errors och värre."},
            {"front": "journalctl -k?", "back": "Bara kernel-meddelanden."},
            {
                "front": "journalctl --disk-usage?",
                "back": "Visa hur mycket plats loggar tar.",
            },
            {
                "front": "journalctl --vacuum-size=100M?",
                "back": "Begränsa loggar till 100MB.",
            },
            {
                "front": "journalctl --vacuum-time=7d?",
                "back": "Ta bort loggar äldre än 7 dagar.",
            },
            {
                "front": "Vad är multi-user.target?",
                "back": "Flerbrukarläge utan GUI (runlevel 3).",
            },
            {"front": "Vad är graphical.target?", "back": "GUI-läge (runlevel 5)."},
            {
                "front": "Vad är rescue.target?",
                "back": "Single user mode för reparation.",
            },
            {"front": "Vad är emergency.target?", "back": "Minimal boot för nödfall."},
            {
                "front": "systemctl list-dependencies nginx?",
                "back": "Visa beroenden för tjänst.",
            },
            {"front": "systemd-analyze?", "back": "Analysera boot-tid."},
            {"front": "systemd-analyze blame?", "back": "Visa vad som tog längst tid."},
            {
                "front": "systemd-analyze critical-chain?",
                "back": "Visa kritisk boot-kedja.",
            },
            {
                "front": "Override-fil?",
                "back": "/etc/systemd/system/nginx.service.d/override.conf",
            },
            {
                "front": "systemctl edit nginx --full?",
                "back": "Redigera hela unit-filen.",
            },
            {
                "front": "Vad är socket activation?",
                "back": "Tjänst startas först när socket får anslutning.",
            },
            {
                "front": "Vad är timer i systemd?",
                "back": "Schemalagd körning, ersätter cron.",
            },
            {"front": "systemctl list-timers?", "back": "Lista aktiva timers."},
            {"front": "OnCalendar=daily?", "back": "Kör en gång per dag."},
            {"front": "OnBootSec=5min?", "back": "Kör 5 min efter boot."},
            {
                "front": "Persistent=true?",
                "back": "Kör missade jobb efter uppvaknande.",
            },
            {"front": "loginctl?", "back": "Hantera användarsessioner."},
            {"front": "hostnamectl?", "back": "Visa/ändra hostname."},
            {"front": "timedatectl?", "back": "Visa/ändra tid och tidszon."},
        ],
    },
    "quiz": {
        # =====================================================================
        # NOD 1: SUBNETTING & NÄTVERK QUIZ (150 frågor) - Del 1 av 3
        # =====================================================================
        "nod1_subnetting": [
            {
                "question": "Hur många användbara IP-adresser finns i ett /24-nät?",
                "options": ["256", "254", "255", "252"],
                "correct": 1,
                "explanation": "256 totalt minus nätverksadress och broadcast = 254 användbara.",
            },
            {
                "question": "Vilken är broadcast-adressen i 192.168.1.0/24?",
                "options": [
                    "192.168.1.0",
                    "192.168.1.1",
                    "192.168.1.254",
                    "192.168.1.255",
                ],
                "correct": 3,
                "explanation": "Broadcast är alltid sista adressen i subnätet - 192.168.1.255.",
            },
            {
                "question": "Vilken subnätmask motsvarar /16?",
                "options": [
                    "255.0.0.0",
                    "255.255.0.0",
                    "255.255.255.0",
                    "255.255.255.128",
                ],
                "correct": 1,
                "explanation": "/16 betyder att första 16 bitarna är nätverksdel = 255.255.0.0.",
            },
            {
                "question": "Vilket prefix behövs för att få minst 500 hosts?",
                "options": ["/24", "/23", "/22", "/25"],
                "correct": 1,
                "explanation": "/23 ger 510 hosts. /24 ger bara 254 vilket är för lite.",
            },
            {
                "question": "Vilken port använder SSH som standard?",
                "options": ["21", "22", "23", "80"],
                "correct": 1,
                "explanation": "SSH (Secure Shell) använder port 22 som standard.",
            },
            {
                "question": "Vad är syftet med NAT?",
                "options": [
                    "Kryptera nätverkstrafik",
                    "Översätta privata IP till publika",
                    "Blockera oönskad trafik",
                    "Tilldela IP-adresser automatiskt",
                ],
                "correct": 1,
                "explanation": "NAT (Network Address Translation) översätter privata IP-adresser till publika för internetåtkomst.",
            },
            {
                "question": "Vilket kommando visar din IP-adress i Linux?",
                "options": ["ipconfig", "ip addr", "netstat", "route"],
                "correct": 1,
                "explanation": "'ip addr' eller 'ip a' visar IP-adresser på alla interface. ipconfig är Windows.",
            },
            {
                "question": "Hur många subnät får du om du delar /24 i /26?",
                "options": ["2", "4", "8", "16"],
                "correct": 1,
                "explanation": "/24 till /26 = 2 extra bitar = 2² = 4 subnät.",
            },
            {
                "question": "Vilket IP-intervall är privat?",
                "options": [
                    "8.8.8.0/24",
                    "192.168.0.0/16",
                    "1.1.1.0/24",
                    "208.67.0.0/16",
                ],
                "correct": 1,
                "explanation": "192.168.0.0/16 är ett av tre privata intervall (tillsammans med 10.0.0.0/8 och 172.16.0.0/12).",
            },
            {
                "question": "Vad är default gateway?",
                "options": [
                    "DNS-servern",
                    "Första användbara IP i nätverket",
                    "Routern för trafik utanför lokala nätverket",
                    "Broadcast-adressen",
                ],
                "correct": 2,
                "explanation": "Default gateway är IP-adressen till routern som skickar trafik utanför det lokala nätverket.",
            },
            {
                "question": "Vilken adress är loopback?",
                "options": ["0.0.0.0", "127.0.0.1", "255.255.255.255", "192.168.1.1"],
                "correct": 1,
                "explanation": "127.0.0.1 är loopback - pekar alltid på den egna datorn.",
            },
            {
                "question": "Vad gör kommandot 'ping'?",
                "options": [
                    "Visar routingtabell",
                    "Testar nätverksanslutning med ICMP",
                    "Konfigurerar IP-adress",
                    "Listar öppna portar",
                ],
                "correct": 1,
                "explanation": "ping skickar ICMP Echo Request och väntar på svar för att testa anslutning.",
            },
            {
                "question": "Hur många hosts finns i ett /30-nät?",
                "options": ["0", "2", "4", "6"],
                "correct": 1,
                "explanation": "/30 = 4 adresser minus nätverks- och broadcast = 2 användbara hosts.",
            },
            {
                "question": "Vad är TCP:s huvudfördel över UDP?",
                "options": [
                    "Snabbare",
                    "Pålitlig leverans med felkontroll",
                    "Mindre overhead",
                    "Stöd för multicast",
                ],
                "correct": 1,
                "explanation": "TCP garanterar leverans med acknowledgements och omsändning vid fel.",
            },
            {
                "question": "Vilken port använder HTTP?",
                "options": ["22", "443", "80", "21"],
                "correct": 2,
                "explanation": "HTTP använder port 80, HTTPS använder port 443.",
            },
            {
                "question": "I vilken oktett skiljer sig 10.0.1.0 och 10.0.2.0?",
                "options": ["Första", "Andra", "Tredje", "Fjärde"],
                "correct": 2,
                "explanation": "Tredje oktetten skiljer sig: 1 vs 2.",
            },
            {
                "question": "Vad betyder CIDR?",
                "options": [
                    "Common Internet Data Router",
                    "Classless Inter-Domain Routing",
                    "Central IP Distribution Registry",
                    "Configurable Internet Domain Range",
                ],
                "correct": 1,
                "explanation": "CIDR = Classless Inter-Domain Routing, ett sätt att ange nätverksstorlek med /prefix.",
            },
            {
                "question": "Vad visar 'ip route'?",
                "options": [
                    "DNS-servrar",
                    "Routingtabellen",
                    "Aktiva anslutningar",
                    "MAC-adresser",
                ],
                "correct": 1,
                "explanation": "'ip route' visar routingtabellen - hur trafik dirigeras till olika nätverk.",
            },
            {
                "question": "Vilken fil innehåller DNS-serverkonfiguration?",
                "options": [
                    "/etc/hosts",
                    "/etc/resolv.conf",
                    "/etc/network",
                    "/etc/dns",
                ],
                "correct": 1,
                "explanation": "/etc/resolv.conf konfigurerar vilka DNS-servrar systemet använder.",
            },
            {
                "question": "Vad är ARP:s funktion?",
                "options": [
                    "Översätta domännamn till IP",
                    "Mappa IP-adresser till MAC-adresser",
                    "Kryptera nätverkstrafik",
                    "Tilldela IP-adresser",
                ],
                "correct": 1,
                "explanation": "ARP (Address Resolution Protocol) mappar IP till MAC på det lokala nätverket.",
            },
            {
                "question": "Hur många bitar är en IPv4-adress?",
                "options": ["8", "16", "32", "64"],
                "correct": 2,
                "explanation": "IPv4 är 32 bitar, uppdelat i 4 oktetter (8 bitar vardera).",
            },
            {
                "question": "Vad är ett VLAN?",
                "options": [
                    "Virtual Local Area Network - logisk nätverksuppdelning",
                    "Very Large Area Network",
                    "Variable Length Address Network",
                    "Virtual Link Area Node",
                ],
                "correct": 0,
                "explanation": "VLAN är virtuell uppdelning av ett fysiskt nätverk för att separera trafik.",
            },
            {
                "question": "Vilken är första användbara adressen i 10.0.0.0/8?",
                "options": ["10.0.0.0", "10.0.0.1", "10.0.0.255", "10.255.255.255"],
                "correct": 1,
                "explanation": "Nätverksadressen (10.0.0.0) + 1 = 10.0.0.1 är första användbara.",
            },
            {
                "question": "Vad betyder TTL i nätverkssammanhang?",
                "options": [
                    "Total Transfer Length",
                    "Time To Live - räknare som minskar vid varje hopp",
                    "Transfer Type Label",
                    "Transport Timeout Limit",
                ],
                "correct": 1,
                "explanation": "TTL minskar med 1 vid varje router-hopp och förhindrar eviga loopar.",
            },
            {
                "question": "Vad gör DHCP?",
                "options": [
                    "Krypterar anslutningar",
                    "Tilldelar IP-adresser automatiskt",
                    "Översätter domännamn",
                    "Blockerar oönskad trafik",
                ],
                "correct": 1,
                "explanation": "DHCP (Dynamic Host Configuration Protocol) tilldelar IP automatiskt till enheter.",
            },
        ],
        # =====================================================================
        # NOD 2: FILSYSTEM & GRUNDKOMMANDON QUIZ (150 frågor) - Del 1 av 3
        # =====================================================================
        "nod2_filsystem": [
            {
                "question": "Vad gör kommandot 'ls -la'?",
                "options": [
                    "Listar bara dolda filer",
                    "Listar alla filer med detaljerad info",
                    "Listar filer sorterade efter storlek",
                    "Tar bort filer",
                ],
                "correct": 1,
                "explanation": "-l = long format (detaljerad), -a = all (inklusive dolda filer).",
            },
            {
                "question": "Vilken katalog innehåller systemloggar?",
                "options": ["/etc/log", "/var/log", "/home/log", "/tmp/log"],
                "correct": 1,
                "explanation": "/var/log innehåller alla systemloggar: syslog, auth.log, etc.",
            },
            {
                "question": "Vad gör 'rm -rf'?",
                "options": [
                    "Tar bort filer med bekräftelse",
                    "Tar bort filer och kataloger rekursivt utan bekräftelse",
                    "Byter namn på filer",
                    "Kopierar filer rekursivt",
                ],
                "correct": 1,
                "explanation": "-r = rekursivt, -f = force (utan fråga). VARNING: Extremt farligt!",
            },
            {
                "question": "Vad är /etc-katalogen för?",
                "options": [
                    "Temporära filer",
                    "Användarnas hemkataloger",
                    "Systemkonfigurationsfiler",
                    "Programbinärer",
                ],
                "correct": 2,
                "explanation": "/etc innehåller konfigurationsfiler för systemet och program.",
            },
            {
                "question": "Vad gör 'cd ..'?",
                "options": [
                    "Går till hemkatalogen",
                    "Går till rotkatalogen",
                    "Går upp en nivå i filsystemet",
                    "Går till föregående katalog",
                ],
                "correct": 2,
                "explanation": ".. betyder föräldrakatalogen, så cd .. går upp en nivå.",
            },
            {
                "question": "Vad är /dev/null?",
                "options": [
                    "Noll-bytes-källa",
                    "Svart hål - allt som skrivs hit försvinner",
                    "Disk-enhet",
                    "Nätverksinterface",
                ],
                "correct": 1,
                "explanation": "/dev/null är ett svart hål - perfekt för att tysta output: command > /dev/null",
            },
            {
                "question": "Hur skapar du en katalog med föräldrakataloger?",
                "options": [
                    "mkdir katalog",
                    "mkdir -p sökväg/till/ny/katalog",
                    "mkdir -r katalog",
                    "mkdir --all katalog",
                ],
                "correct": 1,
                "explanation": "mkdir -p skapar alla föräldrakataloger som saknas.",
            },
            {
                "question": "Vad gör 'tail -f'?",
                "options": [
                    "Visar första raderna",
                    "Visar sista raderna och följer nya tillägg",
                    "Filtrerar rader",
                    "Formaterar output",
                ],
                "correct": 1,
                "explanation": "tail -f följer filen live och visar nya rader direkt. Perfekt för loggar!",
            },
            {
                "question": "Vad gör kommandot 'pwd'?",
                "options": [
                    "Visar lösenord",
                    "Visar aktuell katalog",
                    "Byter katalog",
                    "Skapar katalog",
                ],
                "correct": 1,
                "explanation": "pwd = Print Working Directory - visar absolut sökväg till var du är.",
            },
            {
                "question": "Vad är en symbolisk länk?",
                "options": [
                    "En kopia av filen",
                    "En pekare/genväg till en annan fil",
                    "En komprimerad fil",
                    "En krypterad fil",
                ],
                "correct": 1,
                "explanation": "Symbolisk länk (symlink) är en genväg som pekar på en annan fil eller katalog.",
            },
            {
                "question": "Vilken fil körs vid nya bash-sessioner?",
                "options": [".profile", ".bashrc", ".login", ".terminal"],
                "correct": 1,
                "explanation": ".bashrc körs vid nya interaktiva bash-sessioner (inte login-shells).",
            },
            {
                "question": "Vad gör 'df -h'?",
                "options": [
                    "Visar dolda filer",
                    "Visar diskutrymme i läsbart format",
                    "Visar filhistorik",
                    "Tar bort filer",
                ],
                "correct": 1,
                "explanation": "df = disk free, -h = human readable (GB/MB istället för bytes).",
            },
            {
                "question": "Vad betyder ~ i en sökväg?",
                "options": [
                    "Rotkatalogen",
                    "Aktuell katalog",
                    "Användarens hemkatalog",
                    "Temporär katalog",
                ],
                "correct": 2,
                "explanation": "~ är genväg till din hemkatalog. cd ~ = cd /home/dittnamn.",
            },
            {
                "question": "Vad gör 'cat fil1 fil2'?",
                "options": [
                    "Kopierar fil1 till fil2",
                    "Visar och slår ihop innehållet från båda filerna",
                    "Jämför filerna",
                    "Tar bort filerna",
                ],
                "correct": 1,
                "explanation": "cat (concatenate) visar och kan slå ihop flera filers innehåll.",
            },
            {
                "question": "Hur avslutar du 'man'-sidor?",
                "options": ["Ctrl+C", "Ctrl+D", "q", "Esc"],
                "correct": 2,
                "explanation": "Tryck 'q' (quit) för att avsluta man-sidor och less.",
            },
            {
                "question": "Vad gör 'touch fil.txt'?",
                "options": [
                    "Öppnar filen för redigering",
                    "Skapar tom fil eller uppdaterar tidsstämpel",
                    "Tar bort filen",
                    "Visar filinnehåll",
                ],
                "correct": 1,
                "explanation": "touch skapar en tom fil om den inte finns, annars uppdaterar den tidsstämpeln.",
            },
            {
                "question": "Vad innehåller /proc?",
                "options": [
                    "Program-filer",
                    "Processinformation och kernel-data",
                    "Processer som väntar",
                    "Processorkonfiguration",
                ],
                "correct": 1,
                "explanation": "/proc är ett virtuellt filsystem med information om körande processer och kernel.",
            },
            {
                "question": "Vad gör 'find /home -name \"*.txt\"'?",
                "options": [
                    "Skapar textfiler",
                    "Söker efter alla .txt-filer under /home",
                    "Tar bort textfiler",
                    "Kopierar textfiler",
                ],
                "correct": 1,
                "explanation": "find söker rekursivt efter filer som matchar mönstret.",
            },
            {
                "question": "Vad är skillnaden mellan /root och /?",
                "options": [
                    "Samma sak",
                    "/root = root-användarens hem, / = filsystemets rot",
                    "/ = root-användarens hem, /root = filsystemets rot",
                    "Båda är filsystemets rot",
                ],
                "correct": 1,
                "explanation": "/ är filsystemets rot (toppen), /root är hemkatalog för root-användaren.",
            },
            {
                "question": "Vad gör 'wc -l fil.txt'?",
                "options": [
                    "Räknar ord",
                    "Räknar rader",
                    "Räknar tecken",
                    "Räknar filer",
                ],
                "correct": 1,
                "explanation": "wc = word count, -l = lines. Räknar antal rader i filen.",
            },
            {
                "question": "Vad gör 'cp -r'?",
                "options": [
                    "Kopierar med bekräftelse",
                    "Kopierar rekursivt (hela kataloger)",
                    "Kopierar till remote",
                    "Kopierar snabbt",
                ],
                "correct": 1,
                "explanation": "-r = recursive, kopierar katalog och allt innehåll.",
            },
            {
                "question": "Vad är en inode?",
                "options": [
                    "En typ av disk",
                    "Metadata-struktur för filer",
                    "En katalogtyp",
                    "Ett nätverksprotokoll",
                ],
                "correct": 1,
                "explanation": "Inode lagrar filmetadata: ägare, rättigheter, storlek, plats på disk.",
            },
            {
                "question": "Vad gör 'du -sh katalog'?",
                "options": [
                    "Tar bort katalog",
                    "Visar total storlek på katalog läsbart",
                    "Skapar katalog",
                    "Listar kataloginnehåll",
                ],
                "correct": 1,
                "explanation": "du = disk usage, -s = summarize, -h = human readable.",
            },
            {
                "question": "Vad gör 'history'?",
                "options": [
                    "Visar filhistorik",
                    "Visar kommandohistorik",
                    "Visar systemhistorik",
                    "Visar inloggningshistorik",
                ],
                "correct": 1,
                "explanation": "history visar tidigare körda kommandon. Använd !nummer för att köra igen.",
            },
            {
                "question": "Hur skapar du en symbolisk länk?",
                "options": [
                    "link -s mål länk",
                    "ln -s mål länk",
                    "symlink mål länk",
                    "cp -l mål länk",
                ],
                "correct": 1,
                "explanation": "ln -s skapar symbolisk länk. ln utan -s skapar hård länk.",
            },
        ],
        # =====================================================================
        # NOD 3: BASH SCRIPTING GRUND QUIZ
        # =====================================================================
        "nod3_bash_grund": [
            {
                "question": "Vilken rad ska alltid vara först i ett bash-script?",
                "options": ["#!/bin/bash", "#/bin/bash", "!/bin/bash", "@!/bin/bash"],
                "correct": 0,
                "explanation": "Shebang (#!/bin/bash) talar om för systemet vilken tolk som ska köra scriptet.",
            },
            {
                "question": "Hur gör du ett script körbart?",
                "options": [
                    "chmod +x script.sh",
                    "chmod -x script.sh",
                    "run script.sh",
                    "exec script.sh",
                ],
                "correct": 0,
                "explanation": "chmod +x lägger till execute-rättighet så scriptet kan köras.",
            },
            {
                "question": "Hur skapar du en variabel i bash?",
                "options": [
                    "$namn=värde",
                    "namn = värde",
                    "namn=värde",
                    "set namn=värde",
                ],
                "correct": 2,
                "explanation": "Inga mellanslag runt =! namn=värde är korrekt syntax.",
            },
            {
                "question": "Hur läser du värdet av variabeln 'namn'?",
                "options": ["namn", "$namn", "@namn", "%namn"],
                "correct": 1,
                "explanation": "$ framför variabelnamnet läser dess värde. echo $namn skriver ut värdet.",
            },
            {
                "question": "Vad är $1 i ett bash-script?",
                "options": [
                    "Första raden",
                    "Första argumentet",
                    "Exit-kod 1",
                    "Process ID",
                ],
                "correct": 1,
                "explanation": "$1 är första argumentet till scriptet. $2 är andra, osv.",
            },
            {
                "question": "Vad är $0 i ett bash-script?",
                "options": [
                    "Noll",
                    "Scriptets namn/sökväg",
                    "Antal argument",
                    "Föregående kommando",
                ],
                "correct": 1,
                "explanation": "$0 innehåller scriptets namn eller sökväg som det anropades med.",
            },
            {
                "question": "Vad är $#?",
                "options": [
                    "Senaste exit-kod",
                    "Antal argument",
                    "Alla argument",
                    "Process ID",
                ],
                "correct": 1,
                "explanation": "$# ger antalet argument som skickades till scriptet.",
            },
            {
                "question": "Vad är $@?",
                "options": [
                    "Senaste exit-kod",
                    "Antal argument",
                    "Alla argument som lista",
                    "Process ID",
                ],
                "correct": 2,
                "explanation": "$@ expanderar till alla argument, var och en som separat ord.",
            },
            {
                "question": "Vad är $??",
                "options": [
                    "Senaste kommandots exit-kod",
                    "Antal argument",
                    "Alla argument",
                    "Process ID",
                ],
                "correct": 0,
                "explanation": "$? innehåller exit-koden från senaste kommandot. 0 = lyckat.",
            },
            {
                "question": "Vad betyder exit-kod 0?",
                "options": [
                    "Fel uppstod",
                    "Kommandot lyckades",
                    "Filen finns inte",
                    "Ingen behörighet",
                ],
                "correct": 1,
                "explanation": "Exit-kod 0 betyder framgång. Alla andra värden indikerar någon typ av fel.",
            },
            {
                "question": "Hur skriver man en kommentar i bash?",
                "options": [
                    "// kommentar",
                    "/* kommentar */",
                    "# kommentar",
                    "-- kommentar",
                ],
                "correct": 2,
                "explanation": "# startar en kommentar som sträcker sig till radens slut.",
            },
            {
                "question": "Vilken syntax är korrekt för if-sats?",
                "options": [
                    "if [ villkor ]; then ... fi",
                    "if (villkor) { ... }",
                    "if villkor then ... end",
                    "if [villkor] then ... fi",
                ],
                "correct": 0,
                "explanation": "Korrekt syntax: if [ villkor ]; then kommandon; fi. Notera mellanslagen i [ ]!",
            },
            {
                "question": "Hur jämför man strängar i bash?",
                "options": [
                    "str1 == str2",
                    "str1 -eq str2",
                    "str1 = str2 (i [ ])",
                    "str1.equals(str2)",
                ],
                "correct": 2,
                "explanation": "I [ ] används = för strängjämförelse. == fungerar i [[ ]].",
            },
            {
                "question": "Hur jämför man tal i bash?",
                "options": [
                    "tal1 = tal2",
                    "tal1 -eq tal2",
                    "tal1 == tal2",
                    "tal1 equals tal2",
                ],
                "correct": 1,
                "explanation": "-eq för equal, -ne för not equal, -lt för less than, -gt för greater than.",
            },
            {
                "question": "Vad betyder -f i [ -f fil ]?",
                "options": [
                    "Filen är tom",
                    "Filen finns och är en vanlig fil",
                    "Filen är en katalog",
                    "Filen är körbar",
                ],
                "correct": 1,
                "explanation": "-f testar om filen finns OCH är en vanlig fil (inte katalog/länk).",
            },
            {
                "question": "Vad betyder -d i [ -d katalog ]?",
                "options": [
                    "Katalogen är tom",
                    "Sökvägen finns",
                    "Sökvägen är en katalog",
                    "Katalogen är dold",
                ],
                "correct": 2,
                "explanation": "-d testar om sökvägen finns och är en katalog (directory).",
            },
            {
                "question": "Vad betyder -e i [ -e fil ]?",
                "options": [
                    "Filen är tom",
                    "Filen finns (oavsett typ)",
                    "Filen är körbar",
                    "Filen är redigerbar",
                ],
                "correct": 1,
                "explanation": "-e (exists) testar bara om något finns, oavsett om det är fil, katalog etc.",
            },
            {
                "question": "Hur läser man input från användaren?",
                "options": [
                    "input variabel",
                    "read variabel",
                    "get variabel",
                    "scan variabel",
                ],
                "correct": 1,
                "explanation": "read variabel väntar på input och sparar det i variabeln.",
            },
            {
                "question": "Vad gör 'read -p \"Namn: \" namn'?",
                "options": [
                    "Läser från fil",
                    "Visar prompt och läser input till variabel",
                    "Skriver ut variabel",
                    "Pausar scriptet",
                ],
                "correct": 1,
                "explanation": "-p visar en prompt före input. Svaret sparas i variabeln 'namn'.",
            },
            {
                "question": "Vad gör kommandot 'echo -n'?",
                "options": [
                    "Skriver numrerat",
                    "Skriver utan avslutande radbrytning",
                    "Skriver till /dev/null",
                    "Skriver med färg",
                ],
                "correct": 1,
                "explanation": "-n tar bort den automatiska radbrytningen i slutet av echo.",
            },
            {
                "question": "Hur kör du ett kommando och sparar output i variabel?",
                "options": [
                    "var = kommando",
                    "var=$(kommando)",
                    "var=`kommando`",
                    "Både B och C fungerar",
                ],
                "correct": 3,
                "explanation": "Både $(kommando) och `kommando` fungerar. $(  ) är modernare och lättare att nästla.",
            },
            {
                "question": "Vad är skillnaden mellan ' ' och \" \" i bash?",
                "options": [
                    "Ingen skillnad",
                    "' ' = literal, \" \" = expanderar variabler",
                    "\" \" = literal, ' ' = expanderar variabler",
                    "' ' är för strängar, \" \" för tal",
                ],
                "correct": 1,
                "explanation": "Single quotes bevarar allt bokstavligt. Double quotes expanderar $variabler.",
            },
            {
                "question": "Vad skriver 'echo \"$HOME\"' ut?",
                "options": ["$HOME", "HOME", "Din hemkatalog-sökväg", "Fel"],
                "correct": 2,
                "explanation": 'I " " expanderas $HOME till dess värde, t.ex. /home/användarnamn.',
            },
            {
                "question": "Vad skriver 'echo '$HOME'' ut?",
                "options": ["$HOME bokstavligt", "Din hemkatalog", "HOME", "Fel"],
                "correct": 0,
                "explanation": "I ' ' sker ingen expansion - $HOME skrivs ut som texten $HOME.",
            },
            {
                "question": "Hur kör man ett script i samma shell (utan subshell)?",
                "options": [
                    "./script.sh",
                    "bash script.sh",
                    "source script.sh",
                    "run script.sh",
                ],
                "correct": 2,
                "explanation": "source (eller .) kör scriptet i aktuell shell. Variabler bevaras efteråt.",
            },
        ],
        # =====================================================================
        # NOD 4: BASH SCRIPTING AVANCERAT QUIZ
        # =====================================================================
        "nod4_bash_avancerat": [
            {
                "question": "Hur skriver man en for-loop som loopar 1-10?",
                "options": [
                    "for i in 1-10",
                    "for i in {1..10}",
                    "for (i=1; i<=10; i++)",
                    "for i = 1 to 10",
                ],
                "correct": 1,
                "explanation": "{1..10} är brace expansion som genererar sekvensen 1 2 3 ... 10.",
            },
            {
                "question": "Vilken syntax är korrekt för while-loop?",
                "options": [
                    "while [ villkor ]; do ... done",
                    "while (villkor) { ... }",
                    "while villkor: ...",
                    "while [ villkor ] then ... end",
                ],
                "correct": 0,
                "explanation": "while [ villkor ]; do kommandon; done - notera do/done, inte { }.",
            },
            {
                "question": "Hur definierar man en funktion i bash?",
                "options": [
                    "function namn { ... }",
                    "def namn() { ... }",
                    "func namn { ... }",
                    "namn() { ... }",
                ],
                "correct": 3,
                "explanation": "namn() { ... } är standardsyntax. 'function namn { }' fungerar också.",
            },
            {
                "question": "Hur anropar man en funktion i bash?",
                "options": [
                    "call funktionsnamn",
                    "funktionsnamn()",
                    "funktionsnamn",
                    "run funktionsnamn",
                ],
                "correct": 2,
                "explanation": "Bara skriv funktionsnamnet - inga parenteser vid anrop!",
            },
            {
                "question": "Hur skickar man argument till en funktion?",
                "options": [
                    "funk(arg1, arg2)",
                    "funk arg1 arg2",
                    "funk(arg1 arg2)",
                    "funk --arg1 --arg2",
                ],
                "correct": 1,
                "explanation": "Argument skickas som vid vanliga kommandon: funktionsnamn arg1 arg2.",
            },
            {
                "question": "Hur tar funktionen emot argument?",
                "options": [
                    "Med parametrar i ()",
                    "Med $1, $2, etc",
                    "Med @args",
                    "Med arguments[]",
                ],
                "correct": 1,
                "explanation": "Precis som script använder funktioner $1, $2... för argument.",
            },
            {
                "question": "Vad gör 'return 0' i en funktion?",
                "options": [
                    "Returnerar värdet 0",
                    "Avslutar funktionen med exit-kod 0",
                    "Skriver ut 0",
                    "Sätter variabel till 0",
                ],
                "correct": 1,
                "explanation": "return sätter funktionens exit-kod, inte ett returvärde. Använd echo för att returnera text.",
            },
            {
                "question": "Hur gör man en variabel lokal i en funktion?",
                "options": ["private var", "local var", "var local", "let var"],
                "correct": 1,
                "explanation": "local var=värde gör variabeln synlig bara inuti funktionen.",
            },
            {
                "question": "Vad gör 'set -e' i ett script?",
                "options": [
                    "Aktiverar echo",
                    "Avslutar vid första fel",
                    "Exporterar variabler",
                    "Sätter miljövariabler",
                ],
                "correct": 1,
                "explanation": "set -e (errexit) gör att scriptet avslutas direkt om något kommando misslyckas.",
            },
            {
                "question": "Vad gör 'set -u'?",
                "options": [
                    "Gör variabler uppercase",
                    "Fel vid användning av osatta variabler",
                    "Unika värden bara",
                    "Uppdaterar automatiskt",
                ],
                "correct": 1,
                "explanation": "set -u (nounset) ger fel om du försöker använda en variabel som inte är satt.",
            },
            {
                "question": "Vad gör 'set -x'?",
                "options": [
                    "Avslutar scriptet",
                    "Debugläge - visar varje kommando innan det körs",
                    "Kör i bakgrunden",
                    "Exporterar funktioner",
                ],
                "correct": 1,
                "explanation": "set -x (xtrace) är debug-läge som visar varje kommando med + prefix.",
            },
            {
                "question": "Vad är skillnaden mellan [[ ]] och [ ]?",
                "options": [
                    "Ingen skillnad",
                    "[[ ]] är bash-specifik med fler features",
                    "[ ] är bara för strängar",
                    "[[ ]] är långsammare",
                ],
                "correct": 1,
                "explanation": "[[ ]] är bash-specifik, hanterar && och || direkt, säkrare med variabler.",
            },
            {
                "question": "Hur gör man aritmetik i bash?",
                "options": [
                    "result = 5 + 3",
                    "result=$((5 + 3))",
                    "result=$(5 + 3)",
                    "let result 5 + 3",
                ],
                "correct": 1,
                "explanation": "$(( )) är arithmetic expansion. Även 'let' och 'expr' fungerar.",
            },
            {
                "question": "Vad skriver 'echo $((5 * 3))' ut?",
                "options": ["5 * 3", "15", "$((5 * 3))", "Fel"],
                "correct": 1,
                "explanation": "$(( )) utför beräkningen, så resultatet blir 15.",
            },
            {
                "question": "Vad gör case-satsen i bash?",
                "options": [
                    "Ändrar till versaler",
                    "Pattern matching för flera alternativ",
                    "Kopierar filer",
                    "Komprimerar data",
                ],
                "correct": 1,
                "explanation": "case är som switch - matchar värde mot flera mönster och kör rätt kod.",
            },
            {
                "question": "Hur avslutar man ett case-alternativ?",
                "options": ["break", ";;", "end", "done"],
                "correct": 1,
                "explanation": ";; avslutar varje case-alternativ. esac avslutar hela case-satsen.",
            },
            {
                "question": "Vad gör 'shift' i ett script?",
                "options": [
                    "Ändrar tecken till versaler",
                    "Skiftar argumenten - $2 blir $1, etc",
                    "Indenterar kod",
                    "Väntar en sekund",
                ],
                "correct": 1,
                "explanation": "shift tar bort $1 och flyttar alla argument ett steg. $2→$1, $3→$2...",
            },
            {
                "question": "Vad gör 'trap'?",
                "options": [
                    "Fångar djur",
                    "Fångar signaler och kör kod",
                    "Skapar loopar",
                    "Pausar scriptet",
                ],
                "correct": 1,
                "explanation": "trap 'cleanup' EXIT kör cleanup-funktion när scriptet avslutas.",
            },
            {
                "question": "Hur kör man kommando i bakgrunden?",
                "options": [
                    "kommando &",
                    "kommando bg",
                    "background kommando",
                    "run -b kommando",
                ],
                "correct": 0,
                "explanation": "& i slutet kör kommandot i bakgrunden. fg tar tillbaka det.",
            },
            {
                "question": "Vad är $$?",
                "options": [
                    "Två dollartecken",
                    "Scriptets process-ID (PID)",
                    "Senaste bakgrundsprocess",
                    "Exit-kod",
                ],
                "correct": 1,
                "explanation": "$$ är PID för det aktuella scriptet/shellen.",
            },
            {
                "question": "Vad är $!?",
                "options": [
                    "Senaste exit-kod",
                    "PID för senaste bakgrundsjobb",
                    "Antal bakgrundsjobb",
                    "Negation",
                ],
                "correct": 1,
                "explanation": "$! innehåller PID för senaste kommandot som startades i bakgrunden.",
            },
            {
                "question": "Hur väntar man på att bakgrundsjobb ska bli klara?",
                "options": ["pause", "wait", "hold", "sync"],
                "correct": 1,
                "explanation": "wait väntar på alla bakgrundsjobb. wait $pid väntar på specifikt jobb.",
            },
            {
                "question": "Vad gör 'getopts' i bash?",
                "options": [
                    "Hämtar filinnehåll",
                    "Parsar kommandoradsargument/flaggor",
                    "Sätter systemalternativ",
                    "Optimerar script",
                ],
                "correct": 1,
                "explanation": "getopts parsar flaggor som -a -b. Gör argumenthantering enklare.",
            },
            {
                "question": "Vad betyder '2>&1' i bash?",
                "options": [
                    "Kör kommando 2 gånger",
                    "Omdirigerar stderr till stdout",
                    "Jämför två värden",
                    "Dubblerar output",
                ],
                "correct": 1,
                "explanation": "2>&1 skickar stderr (2) till samma plats som stdout (1).",
            },
            {
                "question": "Vad gör 'exec' i bash?",
                "options": [
                    "Kör kommando",
                    "Ersätter nuvarande process med nytt kommando",
                    "Avslutar script",
                    "Exporterar variabler",
                ],
                "correct": 1,
                "explanation": "exec ersätter helt den aktuella processen - scriptet fortsätter inte efteråt.",
            },
        ],
        # =====================================================================
        # NOD 5: ANVÄNDARE & BEHÖRIGHETER QUIZ
        # =====================================================================
        "nod5_anvandare": [
            {
                "question": "Vem är root-användaren?",
                "options": [
                    "Första användaren",
                    "Systemadministratör med UID 0",
                    "Gästanvändare",
                    "Standardanvändare",
                ],
                "correct": 1,
                "explanation": "root är superuser med UID 0 och har fullständig systemåtkomst.",
            },
            {
                "question": "Vad gör 'sudo'?",
                "options": [
                    "Byter användare",
                    "Kör kommando som root",
                    "Visar användare",
                    "Skapar användare",
                ],
                "correct": 1,
                "explanation": "sudo (Super User DO) kör ett kommando med root-privilegier.",
            },
            {
                "question": "Var lagras användarinformation?",
                "options": ["/etc/passwd", "/etc/users", "/var/users", "/home/users"],
                "correct": 0,
                "explanation": "/etc/passwd innehåller användarnamn, UID, GID, hemkatalog och shell.",
            },
            {
                "question": "Var lagras krypterade lösenord?",
                "options": [
                    "/etc/passwd",
                    "/etc/shadow",
                    "/etc/password",
                    "/etc/secure",
                ],
                "correct": 1,
                "explanation": "/etc/shadow är läsbar endast av root och innehåller krypterade lösenord.",
            },
            {
                "question": "Vad gör 'useradd'?",
                "options": [
                    "Lägger till grupp",
                    "Skapar ny användare",
                    "Ändrar lösenord",
                    "Visar användare",
                ],
                "correct": 1,
                "explanation": "useradd skapar ny användare. Använd -m för att skapa hemkatalog.",
            },
            {
                "question": "Vad gör 'useradd -m anna'?",
                "options": [
                    "Skapar användare utan hemkatalog",
                    "Skapar användare med hemkatalog",
                    "Ändrar hemkatalog",
                    "Tar bort användare",
                ],
                "correct": 1,
                "explanation": "-m (--create-home) skapar hemkatalog /home/anna automatiskt.",
            },
            {
                "question": "Vad gör 'userdel'?",
                "options": [
                    "Inaktiverar användare",
                    "Tar bort användare",
                    "Ändrar användare",
                    "Listar användare",
                ],
                "correct": 1,
                "explanation": "userdel tar bort användare. -r tar även bort hemkatalog.",
            },
            {
                "question": "Vad gör 'passwd'?",
                "options": [
                    "Visar lösenord",
                    "Ändrar lösenord",
                    "Skapar användare",
                    "Tar bort lösenord",
                ],
                "correct": 1,
                "explanation": "passwd ändrar lösenord för aktuell användare, eller annan om root.",
            },
            {
                "question": "Vad gör 'usermod'?",
                "options": [
                    "Modifierar befintlig användare",
                    "Skapar användare",
                    "Tar bort användare",
                    "Visar användare",
                ],
                "correct": 0,
                "explanation": "usermod ändrar befintlig användare. T.ex. usermod -aG sudo anna.",
            },
            {
                "question": "Vad gör 'usermod -aG docker anna'?",
                "options": [
                    "Tar bort anna från docker-grupp",
                    "Lägger till anna i docker-grupp",
                    "Skapar docker-grupp",
                    "Byter annas primära grupp",
                ],
                "correct": 1,
                "explanation": "-a (append) + -G lägger till användare i grupp utan att ta bort från andra.",
            },
            {
                "question": "Var lagras gruppinformation?",
                "options": ["/etc/group", "/etc/groups", "/etc/passwd", "/var/groups"],
                "correct": 0,
                "explanation": "/etc/group innehåller gruppnamn, GID och medlemmar.",
            },
            {
                "question": "Vad gör 'groupadd'?",
                "options": [
                    "Lägger till användare i grupp",
                    "Skapar ny grupp",
                    "Tar bort grupp",
                    "Visar grupper",
                ],
                "correct": 1,
                "explanation": "groupadd skapar en ny grupp. groupadd utvecklare.",
            },
            {
                "question": "Vad gör 'groups'?",
                "options": [
                    "Skapar grupper",
                    "Visar vilka grupper användare tillhör",
                    "Tar bort grupper",
                    "Ändrar grupper",
                ],
                "correct": 1,
                "explanation": "groups visar alla grupper som aktuell (eller angiven) användare tillhör.",
            },
            {
                "question": "Vad gör 'id'?",
                "options": [
                    "Skapar ID",
                    "Visar UID, GID och grupptillhörighet",
                    "Ändrar ID",
                    "Tar bort ID",
                ],
                "correct": 1,
                "explanation": "id visar användarens UID, primär GID och alla grupper.",
            },
            {
                "question": "Vad är UID?",
                "options": ["Unique ID", "User ID", "Universal ID", "Unix ID"],
                "correct": 1,
                "explanation": "User ID - unikt nummer som identifierar användare. root = 0.",
            },
            {
                "question": "Vad är GID?",
                "options": ["General ID", "Group ID", "Global ID", "GNU ID"],
                "correct": 1,
                "explanation": "Group ID - unikt nummer som identifierar en grupp.",
            },
            {
                "question": "Vad gör 'su'?",
                "options": [
                    "Super user",
                    "Byter användare (Switch User)",
                    "Sudo user",
                    "System user",
                ],
                "correct": 1,
                "explanation": "su byter till annan användare. su - anna startar ny login-shell.",
            },
            {
                "question": "Skillnad mellan 'su' och 'su -'?",
                "options": [
                    "Ingen skillnad",
                    "su - laddar målanvändarens miljövariabler",
                    "su laddar målanvändarens miljö",
                    "su - är snabbare",
                ],
                "correct": 1,
                "explanation": "su - (eller su -l) startar login-shell med full miljö som målanvändaren.",
            },
            {
                "question": "Vad är en primär grupp?",
                "options": [
                    "Första gruppen i /etc/group",
                    "Gruppn som används för nya filer",
                    "Admingruppen",
                    "Systemgruppen",
                ],
                "correct": 1,
                "explanation": "Primär grupp är den som tilldelas nya filer som användaren skapar.",
            },
            {
                "question": "Vad representerar 'rwxr-xr--'?",
                "options": [
                    "7-5-4 i oktal",
                    "7-5-4 = 754 i chmod",
                    "Owner: rwx, group: r-x, other: r--",
                    "Både B och C",
                ],
                "correct": 3,
                "explanation": "rwx=7, r-x=5, r--=4. Ägare kan allt, grupp kan läsa/köra, andra bara läsa.",
            },
            {
                "question": "Vad gör 'chmod 755'?",
                "options": ["rwx för alla", "rwxr-xr-x", "rw-r--r--", "rwxrwxrwx"],
                "correct": 1,
                "explanation": "7=rwx för ägare, 5=r-x för grupp och andra. Vanligt för körbara filer.",
            },
            {
                "question": "Vad gör 'chmod 644'?",
                "options": ["rwxr-xr-x", "rw-r--r--", "rwx------", "rw-rw-r--"],
                "correct": 1,
                "explanation": "6=rw- för ägare, 4=r-- för grupp och andra. Vanligt för filer.",
            },
            {
                "question": "Vad gör 'chown anna fil'?",
                "options": [
                    "Ändrar grupp till anna",
                    "Ändrar ägare till anna",
                    "Skapar användare anna",
                    "Kopierar fil till anna",
                ],
                "correct": 1,
                "explanation": "chown (change owner) ändrar filens ägare till anna.",
            },
            {
                "question": "Vad gör 'chown anna:devs fil'?",
                "options": [
                    "Ändrar bara ägare",
                    "Ändrar både ägare och grupp",
                    "Skapar användare och grupp",
                    "Ändrar bara grupp",
                ],
                "correct": 1,
                "explanation": "user:group ändrar både ägare (anna) och grupp (devs) samtidigt.",
            },
            {
                "question": "Vad gör 'chgrp'?",
                "options": [
                    "Ändrar ägare",
                    "Ändrar grupp",
                    "Skapar grupp",
                    "Visar grupp",
                ],
                "correct": 1,
                "explanation": "chgrp (change group) ändrar filens grupptillhörighet.",
            },
        ],
        # =====================================================================
        # NOD 6: SSH & SÄKERHET QUIZ
        # =====================================================================
        "nod6_ssh": [
            {
                "question": "Vad är SSH?",
                "options": [
                    "Secure Shell - krypterad fjärranslutning",
                    "Super Shell - snabb anslutning",
                    "System Shell - lokal terminal",
                    "Simple Shell - grundläggande skal",
                ],
                "correct": 0,
                "explanation": "SSH = Secure Shell - protokoll för krypterad kommunikation, standard port 22.",
            },
            {
                "question": "Standardport för SSH?",
                "options": ["21", "22", "23", "80"],
                "correct": 1,
                "explanation": "SSH använder port 22 som standard. FTP=21, Telnet=23, HTTP=80.",
            },
            {
                "question": "Hur ansluter du via SSH?",
                "options": [
                    "ssh user@host",
                    "connect user@host",
                    "remote user@host",
                    "login user@host",
                ],
                "correct": 0,
                "explanation": "ssh användare@värd - t.ex. ssh admin@192.168.1.100",
            },
            {
                "question": "Hur genererar man SSH-nyckelpar?",
                "options": ["ssh keygen", "ssh-keygen", "ssh --genkey", "keygen ssh"],
                "correct": 1,
                "explanation": "ssh-keygen skapar nyckelpar. -t anger typ (rsa, ed25519).",
            },
            {
                "question": "Var sparas din privata SSH-nyckel?",
                "options": [
                    "~/.ssh/id_rsa.pub",
                    "~/.ssh/id_rsa",
                    "/etc/ssh/keys",
                    "~/.ssh/authorized_keys",
                ],
                "correct": 1,
                "explanation": "~/.ssh/id_rsa är privat nyckel. .pub-filen är publik. Privata ska ALDRIG delas!",
            },
            {
                "question": "Vad är ~/.ssh/authorized_keys?",
                "options": [
                    "Din privata nyckel",
                    "Publika nycklar som får logga in",
                    "SSH-konfiguration",
                    "Kända servrar",
                ],
                "correct": 1,
                "explanation": "authorized_keys innehåller publika nycklar som får SSH:a till denna användare.",
            },
            {
                "question": "Vad gör 'ssh-copy-id user@host'?",
                "options": [
                    "Kopierar SSH-konfiguration",
                    "Kopierar publik nyckel till servern",
                    "Kopierar privat nyckel",
                    "Skapar ny nyckel",
                ],
                "correct": 1,
                "explanation": "ssh-copy-id lägger till din publika nyckel i serverns authorized_keys.",
            },
            {
                "question": "Vad är ~/.ssh/known_hosts?",
                "options": [
                    "Kända användare",
                    "Sparade fingerprints för servrar du anslutit till",
                    "SSH-nycklar",
                    "Tillåtna hosts",
                ],
                "correct": 1,
                "explanation": "known_hosts sparar serverfingerprints för att verifiera identitet nästa gång.",
            },
            {
                "question": "Hur kör du kommando via SSH utan att logga in?",
                "options": [
                    "ssh user@host; kommando",
                    "ssh user@host kommando",
                    "ssh -c kommando user@host",
                    "ssh user@host --exec kommando",
                ],
                "correct": 1,
                "explanation": "ssh user@host kommando - kör kommandot och avslutar direkt.",
            },
            {
                "question": "Vad gör 'scp'?",
                "options": [
                    "Secure connect",
                    "Secure copy - kopierar filer över SSH",
                    "Shell copy",
                    "System copy",
                ],
                "correct": 1,
                "explanation": "scp kopierar filer krypterat. scp fil user@host:/sökväg",
            },
            {
                "question": "Hur kopierar du fil till fjärrserver med scp?",
                "options": [
                    "scp user@host:fil lokal",
                    "scp fil user@host:/sökväg",
                    "scp -r fil host",
                    "scp --remote fil host",
                ],
                "correct": 1,
                "explanation": "scp lokalfil user@host:/destinationssökväg",
            },
            {
                "question": "Hur kopierar du katalog rekursivt med scp?",
                "options": [
                    "scp -d katalog host:/",
                    "scp -r katalog user@host:/",
                    "scp katalog/* user@host:/",
                    "scp --all katalog host:/",
                ],
                "correct": 1,
                "explanation": "-r kopierar rekursivt. scp -r mapp/ user@host:/destination/",
            },
            {
                "question": "Vad är rsync?",
                "options": [
                    "Real-time sync",
                    "Effektiv filsynkronisering - kopierar bara ändringar",
                    "Remote sync",
                    "Roll sync",
                ],
                "correct": 1,
                "explanation": "rsync synkroniserar effektivt genom att bara överföra skillnader.",
            },
            {
                "question": "Vilka flaggor är vanliga med rsync?",
                "options": ["-rpc", "-avz", "-xyz", "-abc"],
                "correct": 1,
                "explanation": "-a (archive), -v (verbose), -z (compress). rsync -avz källa dest.",
            },
            {
                "question": "Vad är SSH-tunnel/port forwarding?",
                "options": [
                    "VPN-ersättning",
                    "Krypterad kanal för trafik genom SSH",
                    "Brandvägg",
                    "Proxy-server",
                ],
                "correct": 1,
                "explanation": "SSH-tunnel skickar annan trafik säkert genom SSH-anslutningen.",
            },
            {
                "question": "Vad gör 'ssh -L 8080:localhost:80 user@host'?",
                "options": [
                    "Loggar in på port 8080",
                    "Skapar lokal tunnel: din 8080 → serverns 80",
                    "Öppnar port 8080 på servern",
                    "Blockerar port 8080",
                ],
                "correct": 1,
                "explanation": "Local forwarding: anslutning till din port 8080 skickas till serverns port 80.",
            },
            {
                "question": "Vilken fil konfigurerar SSH-server?",
                "options": [
                    "~/.ssh/config",
                    "/etc/ssh/ssh_config",
                    "/etc/ssh/sshd_config",
                    "/etc/sshd/config",
                ],
                "correct": 2,
                "explanation": "sshd_config är serverns konfiguration. ssh_config är klientens.",
            },
            {
                "question": "Hur inaktiverar du root-login via SSH?",
                "options": [
                    "PermitRootLogin no",
                    "RootLogin disabled",
                    "AllowRoot no",
                    "NoRootSSH yes",
                ],
                "correct": 0,
                "explanation": "I /etc/ssh/sshd_config: PermitRootLogin no - bästa praxis!",
            },
            {
                "question": "Hur inaktiverar du lösenordsinloggning (bara nycklar)?",
                "options": [
                    "NoPassword yes",
                    "PasswordAuthentication no",
                    "PasswordLogin disabled",
                    "KeyOnly yes",
                ],
                "correct": 1,
                "explanation": "PasswordAuthentication no i sshd_config - kräver nyckel för login.",
            },
            {
                "question": "Vad gör 'ssh-agent'?",
                "options": [
                    "SSH-server",
                    "Lagrar dekrypterade nycklar i minnet",
                    "Genererar nycklar",
                    "Blockerar attacker",
                ],
                "correct": 1,
                "explanation": "ssh-agent håller olåsta privata nycklar så du slipper ange lösenord varje gång.",
            },
            {
                "question": "Vad gör 'ssh-add'?",
                "options": [
                    "Skapar ny nyckel",
                    "Lägger till nyckel till ssh-agent",
                    "Lägger till användare",
                    "Lägger till host",
                ],
                "correct": 1,
                "explanation": "ssh-add ~/.ssh/id_rsa - lägger till nyckel i agenten (frågar om lösenfras).",
            },
            {
                "question": "Rekommenderad nyckeltyp idag?",
                "options": ["RSA 1024", "DSA", "ED25519", "RSA 512"],
                "correct": 2,
                "explanation": "ED25519 rekommenderas - snabbare och säkrare än RSA med kortare nycklar.",
            },
            {
                "question": "Hur skapar du ED25519-nyckel?",
                "options": [
                    "ssh-keygen -t ed25519",
                    "ssh-keygen --ed25519",
                    "ssh-keygen -e ed25519",
                    "keygen ed25519",
                ],
                "correct": 0,
                "explanation": "ssh-keygen -t ed25519 - modern, säker algoritm.",
            },
            {
                "question": "Vad är fail2ban?",
                "options": [
                    "SSH-klient",
                    "Verktyg som blockerar upprepade misslyckade inloggningar",
                    "Brandvägg",
                    "Lösenordshanterare",
                ],
                "correct": 1,
                "explanation": "fail2ban övervakar loggar och blockerar IP:n med för många misslyckade försök.",
            },
            {
                "question": "Vilken rättighet ska ~/.ssh ha?",
                "options": ["777", "755", "700", "644"],
                "correct": 2,
                "explanation": "~/.ssh ska vara 700 (rwx------), endast ägaren får åtkomst.",
            },
        ],
        # =====================================================================
        # NOD 7: FIREWALL & NÄTVERK QUIZ
        # =====================================================================
        "nod7_firewall": [
            {
                "question": "Vad är UFW?",
                "options": [
                    "Universal Firewall",
                    "Uncomplicated Firewall",
                    "Unix Firewall",
                    "User Firewall",
                ],
                "correct": 1,
                "explanation": "UFW = Uncomplicated Firewall - användarvänligt gränssnitt för iptables.",
            },
            {
                "question": "Hur aktiverar du UFW?",
                "options": ["ufw start", "ufw enable", "ufw on", "systemctl start ufw"],
                "correct": 1,
                "explanation": "sudo ufw enable aktiverar brandväggen och startar vid boot.",
            },
            {
                "question": "Hur tillåter du SSH genom UFW?",
                "options": [
                    "ufw allow ssh",
                    "ufw open 22",
                    "ufw add ssh",
                    "ufw permit ssh",
                ],
                "correct": 0,
                "explanation": "ufw allow ssh eller ufw allow 22 - tillåter SSH-trafik.",
            },
            {
                "question": "Hur blockerar du en port med UFW?",
                "options": [
                    "ufw block 80",
                    "ufw deny 80",
                    "ufw reject 80",
                    "ufw close 80",
                ],
                "correct": 1,
                "explanation": "ufw deny 80 blockerar port 80. deny droppar tyst, reject skickar svar.",
            },
            {
                "question": "Vad gör 'ufw status'?",
                "options": [
                    "Startar brandväggen",
                    "Visar aktiva regler",
                    "Återställer regler",
                    "Stänger brandväggen",
                ],
                "correct": 1,
                "explanation": "ufw status visar om brandväggen är aktiv och listar alla regler.",
            },
            {
                "question": "Vad gör 'ufw status verbose'?",
                "options": [
                    "Visar mer detaljer om regler",
                    "Aktiverar loggning",
                    "Visar blockerade paket",
                    "Listar alla portar",
                ],
                "correct": 0,
                "explanation": "verbose visar mer info som default policy och loggningsnivå.",
            },
            {
                "question": "Hur tillåter du specifik IP?",
                "options": [
                    "ufw allow 192.168.1.100",
                    "ufw allow from 192.168.1.100",
                    "ufw permit ip 192.168.1.100",
                    "ufw add 192.168.1.100",
                ],
                "correct": 1,
                "explanation": "ufw allow from 192.168.1.100 - tillåter all trafik från den IP:n.",
            },
            {
                "question": "Hur tar du bort en UFW-regel?",
                "options": [
                    "ufw remove allow 22",
                    "ufw delete allow 22",
                    "ufw drop allow 22",
                    "ufw clear allow 22",
                ],
                "correct": 1,
                "explanation": "ufw delete allow 22 eller ufw delete [regelnummer] tar bort regeln.",
            },
            {
                "question": "Vad är iptables?",
                "options": [
                    "IP-adresstabell",
                    "Linux kärnans brandvägg",
                    "Nätverkskonfiguration",
                    "Routing-tabell",
                ],
                "correct": 1,
                "explanation": "iptables är det klassiska Linux-brandväggsverktyget i kärnan.",
            },
            {
                "question": "Vilka chains finns i iptables?",
                "options": [
                    "IN, OUT, FWD",
                    "INPUT, OUTPUT, FORWARD",
                    "ALLOW, DENY, REJECT",
                    "TCP, UDP, ICMP",
                ],
                "correct": 1,
                "explanation": "INPUT (inkommande), OUTPUT (utgående), FORWARD (vidarebefordra).",
            },
            {
                "question": "Vad gör 'iptables -L'?",
                "options": [
                    "Laddar regler",
                    "Listar alla regler",
                    "Låser brandväggen",
                    "Loggar trafik",
                ],
                "correct": 1,
                "explanation": "iptables -L listar alla regler. -n visar IP:n numeriskt, -v verbose.",
            },
            {
                "question": "Hur blockerar du IP med iptables?",
                "options": [
                    "iptables -A INPUT -s IP -j DROP",
                    "iptables -B INPUT -s IP -j DROP",
                    "iptables -I INPUT -s IP -j BLOCK",
                    "iptables INPUT -s IP DROP",
                ],
                "correct": 0,
                "explanation": "-A lägger till regel, -s source IP, -j DROP droppar paketen.",
            },
            {
                "question": "Vad är nftables?",
                "options": [
                    "Network Filter Tables - ersätter iptables",
                    "NAT Filter Tables",
                    "New Firewall Tables",
                    "Network Forwarding Tables",
                ],
                "correct": 0,
                "explanation": "nftables är den moderna ersättaren för iptables i Linux.",
            },
            {
                "question": "Vad gör kommandot 'ss'?",
                "options": [
                    "Secure Shell",
                    "Visar socket-statistik",
                    "Startar service",
                    "System status",
                ],
                "correct": 1,
                "explanation": "ss visar nätverkssockets. Ersätter äldre netstat.",
            },
            {
                "question": "Hur listar du lyssnande portar?",
                "options": ["ss -l", "ss -a", "ss -t", "ss -p"],
                "correct": 0,
                "explanation": "ss -l visar lyssnande sockets. -t för TCP, -u för UDP, -n för nummer.",
            },
            {
                "question": "Vad gör 'netstat -tulpn'?",
                "options": [
                    "Visar TCP/UDP lyssnande portar med PID",
                    "Testar nätverksuppkoppling",
                    "Uppdaterar nätverksstatistik",
                    "Listar nätverksgränssnitt",
                ],
                "correct": 0,
                "explanation": "t=TCP, u=UDP, l=listening, p=PID/program, n=numeriskt.",
            },
            {
                "question": "Hur sätter du default policy i UFW?",
                "options": [
                    "ufw default deny incoming",
                    "ufw policy deny incoming",
                    "ufw set default deny",
                    "ufw incoming deny",
                ],
                "correct": 0,
                "explanation": "ufw default deny incoming blockerar allt inkommande som standard.",
            },
            {
                "question": "Vilken är bra default policy?",
                "options": [
                    "Allow incoming, allow outgoing",
                    "Deny incoming, allow outgoing",
                    "Deny incoming, deny outgoing",
                    "Allow all",
                ],
                "correct": 1,
                "explanation": "Deny inkommande (säkert default) men tillåt utgående (funktionalitet).",
            },
            {
                "question": "Hur tillåter du port-range med UFW?",
                "options": [
                    "ufw allow 6000-6007",
                    "ufw allow 6000:6007/tcp",
                    "ufw allow ports 6000-6007",
                    "ufw allow range 6000 6007",
                ],
                "correct": 1,
                "explanation": "ufw allow 6000:6007/tcp - notera kolon och protokoll.",
            },
            {
                "question": "Vad gör firewalld?",
                "options": [
                    "Brandväggsdemon - vanlig på RHEL/CentOS",
                    "Brandväggsloggar",
                    "Brandväggstester",
                    "Brandväggsdesigner",
                ],
                "correct": 0,
                "explanation": "firewalld är standardbrandväggen på RHEL/CentOS/Fedora.",
            },
            {
                "question": "Vad är en firewall zone i firewalld?",
                "options": [
                    "Geografisk zon",
                    "Förkonfigurerad säkerhetsprofil",
                    "Nätverkssubnät",
                    "Tidsbaserad regel",
                ],
                "correct": 1,
                "explanation": "Zones är profiler som public, home, internal med olika trustnivåer.",
            },
            {
                "question": "Hur öppnar du port permanent i firewalld?",
                "options": [
                    "firewall-cmd --add-port=80/tcp",
                    "firewall-cmd --permanent --add-port=80/tcp",
                    "firewall-cmd --port 80 open",
                    "firewall-cmd enable 80/tcp",
                ],
                "correct": 1,
                "explanation": "--permanent sparar regeln. Sedan firewall-cmd --reload.",
            },
            {
                "question": "Vad gör ping?",
                "options": [
                    "Skickar HTTP-förfrågan",
                    "Testar nätverksanslutning med ICMP",
                    "Kollar DNS",
                    "Mäter bandbredd",
                ],
                "correct": 1,
                "explanation": "ping skickar ICMP echo request för att testa om värd svarar.",
            },
            {
                "question": "Vad gör traceroute?",
                "options": [
                    "Visar DNS-poster",
                    "Visar vägen paket tar till mål",
                    "Testar portar",
                    "Skannar nätverk",
                ],
                "correct": 1,
                "explanation": "traceroute visar varje hopp (router) på vägen till destination.",
            },
            {
                "question": "Vad gör nmap?",
                "options": [
                    "Nätverksmonitor",
                    "Nätverksskanner - hittar öppna portar",
                    "Nätverksmanager",
                    "Nätverkskarta",
                ],
                "correct": 1,
                "explanation": "nmap skannar nätverk och värdar för öppna portar och tjänster.",
            },
        ],
        # =====================================================================
        # NOD 8: DOCKER BASICS QUIZ
        # =====================================================================
        "nod8_docker_basics": [
            {
                "question": "Vad är Docker?",
                "options": [
                    "Virtuell maskin",
                    "Containerplattform för att paketera applikationer",
                    "Operativsystem",
                    "Programmeringsspråk",
                ],
                "correct": 1,
                "explanation": "Docker paketerar applikationer med alla beroenden i isolerade containers.",
            },
            {
                "question": "Skillnad container vs VM?",
                "options": [
                    "Ingen skillnad",
                    "Container delar OS-kärna, VM har egen kärna",
                    "VM är snabbare",
                    "Container kräver mer RAM",
                ],
                "correct": 1,
                "explanation": "Containers delar värd-OS kärnan och är därför lättare och snabbare.",
            },
            {
                "question": "Vad är en Docker image?",
                "options": [
                    "En körande process",
                    "En mall/blueprint för containers",
                    "En virtuell disk",
                    "Ett script",
                ],
                "correct": 1,
                "explanation": "Image är en skrivskyddad mall. Container är en körande instans av image.",
            },
            {
                "question": "Vad är en container?",
                "options": [
                    "En statisk fil",
                    "En körande instans av en image",
                    "En backup",
                    "Ett nätverk",
                ],
                "correct": 1,
                "explanation": "Container är en isolerad process skapad från en image.",
            },
            {
                "question": "Hur listar du körande containers?",
                "options": [
                    "docker containers",
                    "docker ps",
                    "docker list",
                    "docker show",
                ],
                "correct": 1,
                "explanation": "docker ps visar körande containers. -a visar även stoppade.",
            },
            {
                "question": "Hur listar du alla containers (även stoppade)?",
                "options": [
                    "docker ps all",
                    "docker ps -a",
                    "docker list -all",
                    "docker show all",
                ],
                "correct": 1,
                "explanation": "docker ps -a (--all) visar alla containers oavsett status.",
            },
            {
                "question": "Hur listar du images?",
                "options": [
                    "docker image list",
                    "docker images",
                    "docker img ls",
                    "Båda A och B",
                ],
                "correct": 3,
                "explanation": "Både docker images och docker image list fungerar.",
            },
            {
                "question": "Hur hämtar du en image från Docker Hub?",
                "options": [
                    "docker download nginx",
                    "docker pull nginx",
                    "docker get nginx",
                    "docker fetch nginx",
                ],
                "correct": 1,
                "explanation": "docker pull nginx hämtar nginx-imagen från Docker Hub.",
            },
            {
                "question": "Hur kör du en container?",
                "options": [
                    "docker start nginx",
                    "docker run nginx",
                    "docker exec nginx",
                    "docker create nginx",
                ],
                "correct": 1,
                "explanation": "docker run skapar och startar en ny container från image.",
            },
            {
                "question": "Vad gör -d i 'docker run -d nginx'?",
                "options": [
                    "Debug-läge",
                    "Detached - kör i bakgrunden",
                    "Delete efter stopp",
                    "Download först",
                ],
                "correct": 1,
                "explanation": "-d kör containern i bakgrunden (detached mode).",
            },
            {
                "question": "Vad gör -p 8080:80?",
                "options": [
                    "Pausar på port 80",
                    "Mappar värdport 8080 till containerport 80",
                    "Öppnar port 8080",
                    "Protokoll port 80",
                ],
                "correct": 1,
                "explanation": "-p host:container - trafik till värd 8080 skickas till container 80.",
            },
            {
                "question": "Vad gör --name myapp?",
                "options": [
                    "Döper imagen",
                    "Ger containern ett namn",
                    "Skapar nätverk",
                    "Sätter hostname",
                ],
                "correct": 1,
                "explanation": "--name ger containern ett läsbart namn istället för slumpmässigt.",
            },
            {
                "question": "Hur stoppar du en container?",
                "options": [
                    "docker kill myapp",
                    "docker stop myapp",
                    "docker end myapp",
                    "docker halt myapp",
                ],
                "correct": 1,
                "explanation": "docker stop skickar SIGTERM och väntar innan SIGKILL. kill är direkt.",
            },
            {
                "question": "Hur tar du bort en container?",
                "options": [
                    "docker delete myapp",
                    "docker rm myapp",
                    "docker remove myapp",
                    "docker drop myapp",
                ],
                "correct": 1,
                "explanation": "docker rm tar bort stoppad container. -f tvingar bort körande.",
            },
            {
                "question": "Hur tar du bort en image?",
                "options": [
                    "docker rm nginx",
                    "docker rmi nginx",
                    "docker delete nginx",
                    "docker remove image nginx",
                ],
                "correct": 1,
                "explanation": "docker rmi (remove image) tar bort en image.",
            },
            {
                "question": "Vad gör --rm i docker run?",
                "options": [
                    "Read-only mode",
                    "Tar bort containern automatiskt när den stoppas",
                    "Restartläge",
                    "Remove volumes",
                ],
                "correct": 1,
                "explanation": "--rm städar upp containern automatiskt efter avslut.",
            },
            {
                "question": "Hur går du in i en körande container?",
                "options": [
                    "docker enter myapp bash",
                    "docker exec -it myapp bash",
                    "docker run -it myapp bash",
                    "docker shell myapp",
                ],
                "correct": 1,
                "explanation": "docker exec -it (interactive terminal) kör kommando i körande container.",
            },
            {
                "question": "Vad betyder -it?",
                "options": [
                    "Iteration",
                    "Interactive + TTY (terminal)",
                    "Init",
                    "Internal",
                ],
                "correct": 1,
                "explanation": "-i (interactive) + -t (tty/terminal) ger interaktiv session.",
            },
            {
                "question": "Hur ser du loggar från container?",
                "options": [
                    "docker log myapp",
                    "docker logs myapp",
                    "docker output myapp",
                    "docker print myapp",
                ],
                "correct": 1,
                "explanation": "docker logs visar stdout/stderr. -f följer i realtid.",
            },
            {
                "question": "Vad gör 'docker logs -f'?",
                "options": [
                    "Formaterar loggar",
                    "Följer loggar i realtid (follow)",
                    "Filtrerar loggar",
                    "Första 10 rader",
                ],
                "correct": 1,
                "explanation": "-f (follow) streamer nya loggrader kontinuerligt.",
            },
            {
                "question": "Hur inspekterar du container-detaljer?",
                "options": [
                    "docker info myapp",
                    "docker inspect myapp",
                    "docker details myapp",
                    "docker show myapp",
                ],
                "correct": 1,
                "explanation": "docker inspect visar all metadata om container i JSON.",
            },
            {
                "question": "Vad är Docker Hub?",
                "options": [
                    "Docker IDE",
                    "Publikt registry för Docker images",
                    "Docker dokumentation",
                    "Docker support",
                ],
                "correct": 1,
                "explanation": "Docker Hub är det officiella publika registret för images.",
            },
            {
                "question": "Vad är en Docker volume?",
                "options": [
                    "Ljud i container",
                    "Persistent lagring för containerdata",
                    "Nätverksvolym",
                    "Backup-fil",
                ],
                "correct": 1,
                "explanation": "Volumes är persistent lagring som överlever container-restart/borttagning.",
            },
            {
                "question": "Hur skapar du en volume?",
                "options": [
                    "docker create volume mydata",
                    "docker volume create mydata",
                    "docker vol mydata",
                    "docker storage mydata",
                ],
                "correct": 1,
                "explanation": "docker volume create mydata skapar en namngiven volume.",
            },
            {
                "question": "Hur monterar du volume i container?",
                "options": [
                    "-v mydata:/app/data",
                    "--mount mydata /app/data",
                    "-vol mydata:/app/data",
                    "--volume attach mydata",
                ],
                "correct": 0,
                "explanation": "-v volume:container_path monterar volymen i containern.",
            },
        ],
        # =====================================================================
        # NOD 9: DOCKER COMPOSE QUIZ
        # =====================================================================
        "nod9_docker_compose": [
            {
                "question": "Vad är Docker Compose?",
                "options": [
                    "Docker IDE",
                    "Verktyg för att definiera multi-container applikationer",
                    "Docker registry",
                    "Docker image builder",
                ],
                "correct": 1,
                "explanation": "Docker Compose definierar och kör multi-container apps med YAML-fil.",
            },
            {
                "question": "Vilken fil använder Docker Compose som standard?",
                "options": [
                    "docker-compose.yml",
                    "compose.yaml",
                    "docker.yml",
                    "Både A och B",
                ],
                "correct": 3,
                "explanation": "Både docker-compose.yml och compose.yaml fungerar som standard.",
            },
            {
                "question": "Hur startar du alla tjänster i compose-fil?",
                "options": [
                    "docker-compose start",
                    "docker-compose up",
                    "docker-compose run",
                    "docker-compose begin",
                ],
                "correct": 1,
                "explanation": "docker-compose up startar alla definierade tjänster.",
            },
            {
                "question": "Vad gör 'docker-compose up -d'?",
                "options": [
                    "Debug-läge",
                    "Startar i bakgrunden (detached)",
                    "Kör dry-run",
                    "Laddar ner images",
                ],
                "correct": 1,
                "explanation": "-d kör containers i bakgrunden, returnerar direkt till terminal.",
            },
            {
                "question": "Hur stoppar du alla compose-tjänster?",
                "options": [
                    "docker-compose stop",
                    "docker-compose down",
                    "docker-compose halt",
                    "Både A och B",
                ],
                "correct": 3,
                "explanation": "stop stoppar containers, down stoppar OCH tar bort containers/nätverk.",
            },
            {
                "question": "Skillnad mellan stop och down?",
                "options": [
                    "Ingen skillnad",
                    "down tar även bort containers och nätverk",
                    "stop tar bort volumes",
                    "down är snabbare",
                ],
                "correct": 1,
                "explanation": "stop pausar bara, down städar upp containers, nätverk (ej volumes).",
            },
            {
                "question": "Hur ser du loggar för alla tjänster?",
                "options": [
                    "docker-compose log",
                    "docker-compose logs",
                    "docker-compose output",
                    "docker-compose print",
                ],
                "correct": 1,
                "explanation": "docker-compose logs visar loggar. -f för att följa i realtid.",
            },
            {
                "question": "Hur kör du kommando i en specifik tjänst?",
                "options": [
                    "docker-compose run web bash",
                    "docker-compose exec web bash",
                    "Båda fungerar olika",
                    "docker-compose shell web",
                ],
                "correct": 2,
                "explanation": "run skapar ny container, exec kör i befintlig körande container.",
            },
            {
                "question": "Vad gör 'docker-compose build'?",
                "options": [
                    "Bygger alla images med Dockerfile",
                    "Startar containers",
                    "Laddar ner images",
                    "Skapar volumes",
                ],
                "correct": 0,
                "explanation": "build bygger images definierade med 'build:' i compose-filen.",
            },
            {
                "question": "Hur listar du körande compose-containers?",
                "options": [
                    "docker-compose list",
                    "docker-compose ps",
                    "docker-compose containers",
                    "docker-compose show",
                ],
                "correct": 1,
                "explanation": "docker-compose ps visar containers för aktuellt compose-projekt.",
            },
            {
                "question": "Vad definierar 'services:' i compose?",
                "options": [
                    "Nätverk",
                    "Containers/tjänster som ska köras",
                    "Volumes",
                    "Secrets",
                ],
                "correct": 1,
                "explanation": "services: definierar varje container/tjänst i applikationen.",
            },
            {
                "question": "Vad gör 'depends_on:'?",
                "options": [
                    "Laddar ner beroenden",
                    "Definierar startordning",
                    "Installerar paket",
                    "Skapar nätverk",
                ],
                "correct": 1,
                "explanation": "depends_on bestämmer ordning - tjänster startar efter beroenden.",
            },
            {
                "question": "Vad definierar 'volumes:' i compose?",
                "options": [
                    "CPU-begränsningar",
                    "Persistent lagring",
                    "Nätverksinställningar",
                    "Miljövariabler",
                ],
                "correct": 1,
                "explanation": "volumes: definierar persistent lagring för data.",
            },
            {
                "question": "Vad definierar 'networks:'?",
                "options": [
                    "Internet-inställningar",
                    "Anpassade nätverk för containers",
                    "Port-mappning",
                    "DNS-servrar",
                ],
                "correct": 1,
                "explanation": "networks: skapar och konfigurerar nätverk för container-kommunikation.",
            },
            {
                "question": "Hur definierar du miljövariabler i compose?",
                "options": ["vars:", "environment:", "env:", "variables:"],
                "correct": 1,
                "explanation": "environment: sätter miljövariabler i containern.",
            },
            {
                "question": "Hur använder du .env-fil i compose?",
                "options": [
                    "env_file: .env",
                    "file: .env",
                    "load: .env",
                    "include: .env",
                ],
                "correct": 0,
                "explanation": "env_file: .env laddar miljövariabler från extern fil.",
            },
            {
                "question": "Hur exponerar du portar i compose?",
                "options": ["expose:", "ports:", "publish:", "forward:"],
                "correct": 1,
                "explanation": "ports: mappar värdportar till containerportar. '8080:80'.",
            },
            {
                "question": "Skillnad 'ports:' och 'expose:'?",
                "options": [
                    "Ingen skillnad",
                    "ports mappar till värd, expose bara internt",
                    "expose mappar till värd",
                    "ports är för UDP",
                ],
                "correct": 1,
                "explanation": "ports öppnar externt, expose gör port tillgänglig bara för andra containers.",
            },
            {
                "question": "Hur definierar du build context i compose?",
                "options": ["dockerfile:", "build: ./path", "context:", "Både B och C"],
                "correct": 3,
                "explanation": "build: kan vara sökväg eller objekt med context och dockerfile.",
            },
            {
                "question": "Vad gör 'restart: always'?",
                "options": [
                    "Bygger om vid start",
                    "Startar alltid om container vid krasch/reboot",
                    "Uppdaterar image",
                    "Kör health check",
                ],
                "correct": 1,
                "explanation": "restart: always startar om containern automatiskt vid fel eller systemstart.",
            },
            {
                "question": "Hur skalar du en tjänst?",
                "options": [
                    "docker-compose scale web=3",
                    "docker-compose up --scale web=3",
                    "Båda fungerar",
                    "docker-compose replicas web=3",
                ],
                "correct": 1,
                "explanation": "docker-compose up --scale web=3 startar 3 instanser av web.",
            },
            {
                "question": "Vad gör 'docker-compose pull'?",
                "options": [
                    "Hämtar senaste version av images",
                    "Drar ner loggar",
                    "Kopierar filer",
                    "Hämtar compose-fil",
                ],
                "correct": 0,
                "explanation": "pull hämtar senaste version av alla images i compose-filen.",
            },
            {
                "question": "Hur anger du compose-fil explicit?",
                "options": [
                    "-f docker-compose.prod.yml",
                    "--file docker-compose.prod.yml",
                    "Båda fungerar",
                    "-c docker-compose.prod.yml",
                ],
                "correct": 2,
                "explanation": "Både -f och --file anger vilken compose-fil som ska användas.",
            },
            {
                "question": "Vad är docker compose v2?",
                "options": [
                    "Ny version av YAML-syntax",
                    "Integrerat i docker CLI (docker compose)",
                    "Docker Swarm",
                    "Kubernetes-integration",
                ],
                "correct": 1,
                "explanation": "v2 är integrerat i docker CLI: 'docker compose' istället för 'docker-compose'.",
            },
            {
                "question": "Hur definierar du healthcheck i compose?",
                "options": ["health:", "healthcheck:", "check:", "monitor:"],
                "correct": 1,
                "explanation": "healthcheck: definierar hur Docker kollar om containern är frisk.",
            },
        ],
        # =====================================================================
        # NOD 10: SYSTEMD QUIZ
        # =====================================================================
        "nod10_systemd": [
            {
                "question": "Vad är systemd?",
                "options": [
                    "Textredigerare",
                    "Init-system och service manager",
                    "Pakethanterare",
                    "Filsystem",
                ],
                "correct": 1,
                "explanation": "systemd är Linux init-system som startar/hanterar tjänster.",
            },
            {
                "question": "Vad är en unit i systemd?",
                "options": [
                    "Minnesblock",
                    "Resurs som systemd hanterar",
                    "CPU-kärna",
                    "Partition",
                ],
                "correct": 1,
                "explanation": "Unit är en resurs: service, mount, socket, timer, etc.",
            },
            {
                "question": "Hur startar du en tjänst?",
                "options": [
                    "systemctl run nginx",
                    "systemctl start nginx",
                    "systemctl begin nginx",
                    "systemctl launch nginx",
                ],
                "correct": 1,
                "explanation": "systemctl start nginx startar nginx-tjänsten.",
            },
            {
                "question": "Hur stoppar du en tjänst?",
                "options": [
                    "systemctl halt nginx",
                    "systemctl stop nginx",
                    "systemctl kill nginx",
                    "systemctl end nginx",
                ],
                "correct": 1,
                "explanation": "systemctl stop nginx stoppar tjänsten gracefully.",
            },
            {
                "question": "Hur startar du om en tjänst?",
                "options": [
                    "systemctl rerun nginx",
                    "systemctl restart nginx",
                    "systemctl reload nginx",
                    "systemctl reset nginx",
                ],
                "correct": 1,
                "explanation": "restart stoppar och startar tjänsten. reload laddar om config utan stopp.",
            },
            {
                "question": "Skillnad restart och reload?",
                "options": [
                    "Ingen skillnad",
                    "reload laddar om config utan att stoppa tjänsten",
                    "restart laddar om config",
                    "reload är snabbare",
                ],
                "correct": 1,
                "explanation": "reload läser om konfiguration utan avbrott, restart stoppar helt.",
            },
            {
                "question": "Hur aktiverar du tjänst vid boot?",
                "options": [
                    "systemctl boot nginx",
                    "systemctl enable nginx",
                    "systemctl auto nginx",
                    "systemctl persist nginx",
                ],
                "correct": 1,
                "explanation": "enable skapar symlinks så tjänsten startar automatiskt vid boot.",
            },
            {
                "question": "Hur inaktiverar du tjänst vid boot?",
                "options": [
                    "systemctl noboot nginx",
                    "systemctl disable nginx",
                    "systemctl manual nginx",
                    "systemctl remove nginx",
                ],
                "correct": 1,
                "explanation": "disable tar bort autostart vid boot.",
            },
            {
                "question": "Hur ser du status för en tjänst?",
                "options": [
                    "systemctl info nginx",
                    "systemctl status nginx",
                    "systemctl show nginx",
                    "systemctl check nginx",
                ],
                "correct": 1,
                "explanation": "status visar körande/stoppad, loggrader, PID etc.",
            },
            {
                "question": "Hur listar du alla aktiva tjänster?",
                "options": [
                    "systemctl list-units",
                    "systemctl list-services",
                    "systemctl all",
                    "systemctl show-all",
                ],
                "correct": 0,
                "explanation": "list-units visar alla aktiva units. --type=service för bara tjänster.",
            },
            {
                "question": "Var ligger unit-filer?",
                "options": [
                    "/etc/services/",
                    "/etc/systemd/system/",
                    "/var/systemd/",
                    "/usr/services/",
                ],
                "correct": 1,
                "explanation": "/etc/systemd/system/ för admin-skapade. /lib/systemd/system/ för paket.",
            },
            {
                "question": "Vad gör 'systemctl daemon-reload'?",
                "options": [
                    "Startar om alla tjänster",
                    "Läser om unit-filer efter ändringar",
                    "Startar om systemd",
                    "Rensar cache",
                ],
                "correct": 1,
                "explanation": "daemon-reload måste köras efter att du ändrat/lagt till unit-filer.",
            },
            {
                "question": "Vad gör journalctl?",
                "options": [
                    "Redigerar journal",
                    "Visar systemloggar från journald",
                    "Skapar loggar",
                    "Tar bort loggar",
                ],
                "correct": 1,
                "explanation": "journalctl läser loggar från systemd journal - ersätter traditionella logfiler.",
            },
            {
                "question": "Hur ser du loggar för specifik tjänst?",
                "options": [
                    "journalctl nginx",
                    "journalctl -u nginx",
                    "journalctl --service nginx",
                    "journalctl -s nginx",
                ],
                "correct": 1,
                "explanation": "-u (--unit) filtrerar loggar för specifik tjänst.",
            },
            {
                "question": "Hur följer du loggar i realtid?",
                "options": [
                    "journalctl -r",
                    "journalctl -f",
                    "journalctl -l",
                    "journalctl -t",
                ],
                "correct": 1,
                "explanation": "-f (--follow) streamer nya loggposter kontinuerligt.",
            },
            {
                "question": "Hur ser du loggar sedan senaste boot?",
                "options": [
                    "journalctl -b",
                    "journalctl --boot",
                    "Båda",
                    "journalctl -r",
                ],
                "correct": 2,
                "explanation": "-b visar loggar från aktuell boot. -b -1 för föregående boot.",
            },
            {
                "question": "Vilken sektion definierar hur tjänst körs?",
                "options": ["[Unit]", "[Service]", "[Install]", "[Run]"],
                "correct": 1,
                "explanation": "[Service] definierar ExecStart, Type, User, etc - hur tjänsten körs.",
            },
            {
                "question": "Vad är [Unit]-sektionen för?",
                "options": [
                    "Körningsinställningar",
                    "Metadata och beroenden",
                    "Installationsinställningar",
                    "Loggning",
                ],
                "correct": 1,
                "explanation": "[Unit] innehåller Description, After, Requires - allmän info.",
            },
            {
                "question": "Vad är [Install]-sektionen för?",
                "options": [
                    "Paketinstallation",
                    "Hur tjänsten aktiveras vid boot",
                    "Var tjänsten installeras",
                    "Beroenden",
                ],
                "correct": 1,
                "explanation": "[Install] definierar WantedBy - vilken target som startar tjänsten.",
            },
            {
                "question": "Vad gör 'WantedBy=multi-user.target'?",
                "options": [
                    "Kräver multi-user",
                    "Startar tjänsten i multi-user (standard boot) läge",
                    "Begränsar användare",
                    "Skapar användare",
                ],
                "correct": 1,
                "explanation": "WantedBy=multi-user.target aktiverar tjänsten vid normal boot.",
            },
            {
                "question": "Vad gör 'After=network.target'?",
                "options": [
                    "Stänger nätverk efter",
                    "Startar tjänsten efter att nätverk är uppe",
                    "Kräver nätverk",
                    "Blockerar nätverk",
                ],
                "correct": 1,
                "explanation": "After definierar ordning - vänta tills network.target är redo.",
            },
            {
                "question": "Skillnad After och Requires?",
                "options": [
                    "Samma sak",
                    "After = ordning, Requires = hårt beroende",
                    "Requires = ordning, After = beroende",
                    "After är starkare",
                ],
                "correct": 1,
                "explanation": "After bestämmer bara ordning. Requires = tjänst MÅSTE vara igång.",
            },
            {
                "question": "Vad är ExecStart?",
                "options": [
                    "Kommando för att starta tjänsten",
                    "Användare som startar",
                    "Startordning",
                    "Starttid",
                ],
                "correct": 0,
                "explanation": "ExecStart=/path/to/command är kommandot som körs för att starta tjänsten.",
            },
            {
                "question": "Vad gör Restart=always?",
                "options": [
                    "Startar om systemd",
                    "Startar alltid om tjänsten vid krasch",
                    "Tvingar omstart",
                    "Stoppar tjänsten",
                ],
                "correct": 1,
                "explanation": "Restart=always startar automatiskt om tjänsten vid exit/krasch.",
            },
            {
                "question": "Vad är systemd target?",
                "options": [
                    "Mål-mapp",
                    "Grupp av units för ett systemläge",
                    "Destination för loggar",
                    "CPU-mål",
                ],
                "correct": 1,
                "explanation": "Target är grupp av units som representerar ett systemtillstånd (runlevel).",
            },
        ],
    },
}
