"""
Linux Mastery - Study Data
==========================

90 Flashcards (30 easy, 30 medium, 30 hard)
60 Quiz Questions (20 easy, 20 medium, 20 hard)
"""

LINUX_STUDY_DATA = {
    "module_slug": "linux-mastery",
    "module_title": "Linux",
    "module_description": "Komplett Linux-administration på svenska",
    "icon": "Terminal",

    # =========================================================================
    # FLASHCARDS - 90 st totalt (30 per svårighetsgrad)
    # =========================================================================
    "flashcards": {
        "easy": [
            {"front": "Vad gör kommandot 'ls'?", "back": "Listar innehållet i en katalog. Med flaggan -la visas dolda filer och detaljerad info."},
            {"front": "Vad är syftet med /etc-katalogen?", "back": "Innehåller systemkonfigurationsfiler. Alla inställningar för program och tjänster sparas här."},
            {"front": "Hur visar du de sista 10 raderna i en fil?", "back": "tail filnamn - visar sista 10 raderna. tail -n 20 visar sista 20 raderna."},
            {"front": "Vad gör kommandot 'cd'?", "back": "Change Directory - byter aktuell katalog. cd .. går upp en nivå, cd ~ går till hemkatalogen."},
            {"front": "Hur skapar du en ny katalog?", "back": "mkdir katalognamn - skapar en katalog. mkdir -p skapar även föräldrakataloger om de saknas."},
            {"front": "Vad är /home-katalogen?", "back": "Innehåller användarnas hemkataloger. Varje användare har sin egen mapp under /home/användarnamn."},
            {"front": "Hur kopierar du en fil?", "back": "cp källa mål - kopierar en fil. cp -r kopierar kataloger rekursivt."},
            {"front": "Vad gör kommandot 'pwd'?", "back": "Print Working Directory - visar sökvägen till din nuvarande katalog."},
            {"front": "Hur tar du bort en fil?", "back": "rm filnamn - tar bort filen. rm -r tar bort kataloger rekursivt. VARNING: Finns ingen papperskorg!"},
            {"front": "Vad är /var/log?", "back": "Katalog för systemloggar. Här hittar du syslog, auth.log, och applikationsloggar."},
            {"front": "Hur flyttar/byter namn på en fil?", "back": "mv källa mål - flyttar eller byter namn. mv fil.txt nyttnamn.txt byter namn."},
            {"front": "Vad gör 'cat'?", "back": "Concatenate - visar innehållet i en fil. cat fil1 fil2 slår ihop filer."},
            {"front": "Hur söker du efter en fil?", "back": "find /sökväg -name 'filnamn' - söker efter filer. find / -name '*.log' hittar alla .log-filer."},
            {"front": "Vad är en absolut sökväg?", "back": "En sökväg som börjar från roten (/). T.ex. /home/user/dokument/fil.txt"},
            {"front": "Vad är en relativ sökväg?", "back": "En sökväg relativt till nuvarande katalog. T.ex. ./dokument/fil.txt eller ../annan-katalog/"},
            {"front": "Hur visar du första raderna i en fil?", "back": "head filnamn - visar första 10 raderna. head -n 5 visar första 5 raderna."},
            {"front": "Vad gör 'touch'?", "back": "Skapar en tom fil eller uppdaterar en fils tidsstämpel om den redan finns."},
            {"front": "Vad är /tmp-katalogen?", "back": "Katalog för temporära filer. Rensas vid omstart. Spara aldrig viktig data här!"},
            {"front": "Hur visar du diskutrymme?", "back": "df -h - visar diskutrymme för alla monterade filsystem. -h gör det läsbart (GB/MB)."},
            {"front": "Vad gör 'echo'?", "back": "Skriver ut text till terminalen. echo 'Hej' skriver Hej. Används ofta i scripts."},
            {"front": "Hur ser du katalogstorlek?", "back": "du -sh katalog - visar total storlek. -s summerar, -h gör det läsbart."},
            {"front": "Vad är ~-tecknet?", "back": "Genväg till din hemkatalog. cd ~ = cd /home/dittnamn"},
            {"front": "Hur skapar du en symbolisk länk?", "back": "ln -s mål länknamn - skapar en genväg. Motsvarar genvägar i Windows."},
            {"front": "Vad gör 'clear'?", "back": "Rensar terminalskärmen. Ctrl+L gör samma sak."},
            {"front": "Hur avslutar du en process med Ctrl?", "back": "Ctrl+C - avbryter/avslutar den körande processen. Ctrl+Z pausar den."},
            {"front": "Vad är /usr/bin?", "back": "Katalog för användarprogram. De flesta program som installeras med apt/yum hamnar här."},
            {"front": "Hur visar du vilken katalog du är i?", "back": "pwd - Print Working Directory. Visar den fullständiga sökvägen."},
            {"front": "Vad gör kommandot 'man'?", "back": "Visar manualen för ett kommando. man ls visar all info om ls-kommandot."},
            {"front": "Hur avslutar du man-sidor?", "back": "Tryck 'q' för att avsluta. Använd pilar eller Page Up/Down för att scrolla."},
            {"front": "Vad är /bin-katalogen?", "back": "Grundläggande systemkommandon. Här ligger ls, cp, mv - kommandon som alltid måste fungera."},
        ],
        "medium": [
            {"front": "Hur ändrar du filrättigheter?", "back": "chmod - ändrar permissions. chmod 755 fil ger rwxr-xr-x. chmod u+x lägger till execute för ägaren."},
            {"front": "Vad betyder rwxr-xr--?", "back": "Ägare: read+write+execute (7), Grupp: read+execute (5), Andra: read (4). Numeriskt: 754."},
            {"front": "Hur byter du ägare på en fil?", "back": "chown användare:grupp fil - byter ägare. chown -R för rekursivt i kataloger."},
            {"front": "Vad gör kommandot 'grep'?", "back": "Söker efter text/mönster i filer. grep 'error' logfil.txt hittar rader med 'error'."},
            {"front": "Hur kombinerar du kommandon med pipe?", "back": "| (pipe) - skickar output från ett kommando som input till nästa. ls | grep txt"},
            {"front": "Vad gör 'ps aux'?", "back": "Visar alla körande processer. a=alla användare, u=detaljerad info, x=utan terminal."},
            {"front": "Hur dödar du en process?", "back": "kill PID - skickar SIGTERM. kill -9 PID tvingar avslut med SIGKILL."},
            {"front": "Vad är en daemon?", "back": "En bakgrundsprocess som körs kontinuerligt. Exempel: sshd, nginx, mysqld."},
            {"front": "Hur startar du om en tjänst?", "back": "systemctl restart tjänstnamn - startar om tjänsten. start/stop/status finns också."},
            {"front": "Vad gör 'systemctl enable'?", "back": "Aktiverar tjänsten vid systemstart. enable --now startar den direkt också."},
            {"front": "Hur visar du nätverkskonfiguration?", "back": "ip addr eller ip a - visar IP-adresser och nätverksinterface. Ersätter gamla ifconfig."},
            {"front": "Vad gör 'netstat -tulpn'?", "back": "Visar öppna portar och lyssnande tjänster. t=TCP, u=UDP, l=listening, p=process, n=numeriskt."},
            {"front": "Hur testar du nätverksanslutning?", "back": "ping värd - skickar ICMP-paket. ping -c 4 google.com skickar 4 paket."},
            {"front": "Vad gör 'curl'?", "back": "Hämtar data från URL:er. curl https://api.example.com hämtar svar. -o sparar till fil."},
            {"front": "Hur visar du routingtabellen?", "back": "ip route eller route -n - visar nätverksroutes. Default gateway är din router."},
            {"front": "Vad är /etc/hosts?", "back": "Lokal DNS-fil. Mappar IP-adresser till värdnamn. Läses före DNS-server."},
            {"front": "Hur monterar du ett filsystem?", "back": "mount /dev/sdb1 /mnt/disk - monterar partition till katalog. umount avmonterar."},
            {"front": "Vad är /etc/fstab?", "back": "Konfigurerar automatisk montering vid systemstart. Definerar vilka diskar som monteras var."},
            {"front": "Hur komprimerar du filer med tar?", "back": "tar -czvf arkiv.tar.gz katalog - c=create, z=gzip, v=verbose, f=filename."},
            {"front": "Hur extraherar du tar.gz?", "back": "tar -xzvf arkiv.tar.gz - x=extract. -C /path extraherar till specifik katalog."},
            {"front": "Vad gör 'sudo'?", "back": "Kör kommando som root/superuser. sudo apt update kör apt med root-rättigheter."},
            {"front": "Hur skapar du en ny användare?", "back": "useradd användarnamn - skapar användare. useradd -m skapar hemkatalog också."},
            {"front": "Hur sätter du lösenord?", "back": "passwd användarnamn - sätter eller ändrar lösenord. Utan argument ändrar ditt eget."},
            {"front": "Vad är /etc/passwd?", "back": "Innehåller info om alla användare. Användarnamn, UID, GID, hemkatalog, shell."},
            {"front": "Vad är /etc/shadow?", "back": "Innehåller krypterade lösenord. Endast root kan läsa denna fil av säkerhetsskäl."},
            {"front": "Hur lägger du till användare i grupp?", "back": "usermod -aG gruppnamn användare - lägger till i grupp. -a behåller befintliga grupper."},
            {"front": "Vad gör 'crontab -e'?", "back": "Redigerar schemalagda jobb för nuvarande användare. Cron kör kommandon automatiskt."},
            {"front": "Hur ser cron-syntaxen ut?", "back": "min tim dag mån veckodag kommando. * betyder 'alla'. 0 5 * * * = 05:00 varje dag."},
            {"front": "Hur omdirigerar du output till fil?", "back": "> skriver (överskriver), >> appendar. ls > fil.txt sparar output. 2> för stderr."},
            {"front": "Vad är stdin, stdout, stderr?", "back": "Standard streams. stdin=input (0), stdout=output (1), stderr=fel (2). 2>&1 slår ihop."},
        ],
        "hard": [
            {"front": "Hur konfigurerar du iptables för att blocka port 80?", "back": "iptables -A INPUT -p tcp --dport 80 -j DROP. -A appendar regel, -p protokoll, --dport destination port."},
            {"front": "Vad är skillnaden mellan iptables och nftables?", "back": "nftables är modernare ersättare med bättre syntax och prestanda. iptables-nft finns som kompatibilitetslager."},
            {"front": "Hur sätter du upp port forwarding med iptables?", "back": "iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080. Kräver FORWARD-regel också."},
            {"front": "Vad gör 'sysctl'?", "back": "Konfigurerar kernel-parametrar. sysctl -w net.ipv4.ip_forward=1 aktiverar IP forwarding."},
            {"front": "Hur gör du kernel-ändringar permanenta?", "back": "Lägg till i /etc/sysctl.conf eller skapa fil i /etc/sysctl.d/. sysctl -p laddar om."},
            {"front": "Vad är SELinux?", "back": "Security-Enhanced Linux - tvingande åtkomstkontroll. Lägen: enforcing, permissive, disabled."},
            {"front": "Hur kontrollerar du SELinux-status?", "back": "getenforce eller sestatus. setenforce 0 sätter permissive tillfälligt."},
            {"front": "Vad gör 'strace'?", "back": "Spårar systemanrop. strace -p PID visar vad en process gör. Användbart för debugging."},
            {"front": "Hur felsöker du långsam disk I/O?", "back": "iostat -x, iotop, dstat. Kolla await (väntetid) och %util (användning). iowait i top visar CPU-väntan."},
            {"front": "Vad visar 'vmstat'?", "back": "Virtual memory statistics. procs, memory, swap, io, system, cpu. vmstat 1 uppdaterar varje sekund."},
            {"front": "Hur analyserar du minnesanvändning?", "back": "free -h, /proc/meminfo, top/htop. Cached minne kan frigöras. OOM killer dödar vid minnesbrist."},
            {"front": "Vad är swap och när används det?", "back": "Diskutrymme som extra RAM. Används när RAM är fullt. Långsammare än RAM. swappiness styr aggressivitet."},
            {"front": "Hur skapar du en swap-fil?", "back": "dd if=/dev/zero of=/swapfile bs=1G count=4, chmod 600, mkswap, swapon. Lägg i fstab för permanent."},
            {"front": "Vad gör 'lsof'?", "back": "List Open Files - visar vilka filer processer har öppna. lsof -i :80 visar vad som lyssnar på port 80."},
            {"front": "Hur hittar du vilken process använder en fil?", "back": "fuser -v fil eller lsof fil. fuser -k dödar processer som använder filen."},
            {"front": "Vad är inode?", "back": "Datastruktur som lagrar metadata om filer (permissions, ägare, storlek). Filnamn finns i katalog, pekar på inode."},
            {"front": "Hur kontrollerar du inode-användning?", "back": "df -i visar inode-användning. Kan ta slut även om disk har utrymme (många små filer)."},
            {"front": "Vad gör 'nice' och 'renice'?", "back": "Sätter processprioriteter (-20 till 19). nice -n 10 cmd startar med lägre prio. renice ändrar körande process."},
            {"front": "Hur begränsar du resurser med cgroups?", "back": "Control Groups - begränsar CPU, minne, I/O per processgrupp. Grund för containers. cgcreate, cgset, cgexec."},
            {"front": "Vad är namespaces i Linux?", "back": "Isolerar systemresurser: PID, network, mount, user, UTS. Containers använder namespaces + cgroups."},
            {"front": "Hur debuggar du boot-problem?", "back": "journalctl -b för boot-loggar, dmesg för kernel-meddelanden. Lägg till rd.break i GRUB för rescue mode."},
            {"front": "Vad är systemd-target?", "back": "Ersätter runlevels. multi-user.target = runlevel 3, graphical.target = runlevel 5. systemctl isolate byter."},
            {"front": "Hur analyserar du boot-tid?", "back": "systemd-analyze, systemd-analyze blame, systemd-analyze critical-chain. Visar vad som tar tid vid boot."},
            {"front": "Vad gör 'auditd'?", "back": "System auditing daemon. Loggar säkerhetshändelser. auditctl lägger till regler, ausearch söker loggar."},
            {"front": "Hur konfigurerar du logrotate?", "back": "Roterar loggar baserat på storlek/tid. /etc/logrotate.conf och /etc/logrotate.d/. daily, weekly, size 100M."},
            {"front": "Vad är RAID och vilka nivåer finns?", "back": "Redundant Array of Independent Disks. RAID 0=stripe, 1=mirror, 5=stripe+parity, 10=mirror+stripe."},
            {"front": "Hur skapar du software RAID med mdadm?", "back": "mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1. cat /proc/mdstat visar status."},
            {"front": "Vad är LVM och dess komponenter?", "back": "Logical Volume Manager. PV=Physical Volume, VG=Volume Group, LV=Logical Volume. Flexibel diskhantering."},
            {"front": "Hur utökar du en LVM-volym?", "back": "lvextend -L +10G /dev/vg/lv, sedan resize2fs för ext4 eller xfs_growfs för XFS."},
            {"front": "Hur säkerhetskopierar du med rsync?", "back": "rsync -avz --delete källa mål. -a=arkiv, -v=verbose, -z=komprimera. --delete tar bort extra filer."},
        ],
    },

    # =========================================================================
    # QUIZ - 60 st totalt (20 per svårighetsgrad)
    # =========================================================================
    "quiz": {
        "easy": [
            {
                "question": "Vilket kommando visar innehållet i en katalog?",
                "options": ["ls", "cd", "pwd", "cat"],
                "correct": 0,
                "explanation": "ls (list) visar filer och kataloger. cd byter katalog, pwd visar nuvarande sökväg, cat visar filinnehåll."
            },
            {
                "question": "Var sparas systemkonfigurationsfiler i Linux?",
                "options": ["/home", "/var", "/etc", "/usr"],
                "correct": 2,
                "explanation": "/etc innehåller konfigurationsfiler för systemet och tjänster."
            },
            {
                "question": "Hur skapar du en ny tom fil?",
                "options": ["touch filnamn", "create filnamn", "new filnamn", "make filnamn"],
                "correct": 0,
                "explanation": "touch skapar en tom fil eller uppdaterar tidsstämpeln om filen finns."
            },
            {
                "question": "Vad gör kommandot 'cd ..'?",
                "options": ["Går till hemkatalogen", "Går upp en katalognivå", "Visar nuvarande katalog", "Skapar ny katalog"],
                "correct": 1,
                "explanation": ".. betyder föräldrakatalogen. cd .. går upp en nivå i katalogstrukturen."
            },
            {
                "question": "Vilket kommando visar de sista raderna i en fil?",
                "options": ["head", "tail", "cat", "less"],
                "correct": 1,
                "explanation": "tail visar slutet av en fil (standard 10 rader). head visar början."
            },
            {
                "question": "Var finns användarnas hemkataloger?",
                "options": ["/usr/home", "/etc/users", "/home", "/var/users"],
                "correct": 2,
                "explanation": "/home innehåller en katalog per användare, t.ex. /home/anna."
            },
            {
                "question": "Hur kopierar du en fil?",
                "options": ["cp källa mål", "copy källa mål", "mv källa mål", "clone källa mål"],
                "correct": 0,
                "explanation": "cp (copy) kopierar filer. mv flyttar eller byter namn."
            },
            {
                "question": "Vad betyder ~ i en sökväg?",
                "options": ["Rotkatalogen", "Temporär katalog", "Hemkatalogen", "Nuvarande katalog"],
                "correct": 2,
                "explanation": "~ är en genväg till din hemkatalog, t.ex. /home/dittnamn."
            },
            {
                "question": "Hur tar du bort en fil säkert?",
                "options": ["rm filnamn", "del filnamn", "remove filnamn", "erase filnamn"],
                "correct": 0,
                "explanation": "rm (remove) tar bort filer. VARNING: Det finns ingen papperskorg!"
            },
            {
                "question": "Var lagras systemloggar?",
                "options": ["/etc/logs", "/var/log", "/usr/log", "/home/logs"],
                "correct": 1,
                "explanation": "/var/log innehåller alla systemloggar som syslog, auth.log, etc."
            },
            {
                "question": "Hur skapar du en katalog?",
                "options": ["mkdir namn", "create namn", "newdir namn", "makedir namn"],
                "correct": 0,
                "explanation": "mkdir (make directory) skapar en ny katalog."
            },
            {
                "question": "Vad gör kommandot 'pwd'?",
                "options": ["Ändrar lösenord", "Visar nuvarande katalog", "Stänger terminalen", "Visar processer"],
                "correct": 1,
                "explanation": "pwd (Print Working Directory) visar den fullständiga sökvägen till nuvarande katalog."
            },
            {
                "question": "Hur visar du manualen för ett kommando?",
                "options": ["help kommando", "man kommando", "info kommando", "? kommando"],
                "correct": 1,
                "explanation": "man (manual) visar detaljerad dokumentation för kommandon."
            },
            {
                "question": "Vad är /tmp-katalogen för?",
                "options": ["Systemfiler", "Temporära filer", "Användardata", "Loggfiler"],
                "correct": 1,
                "explanation": "/tmp är för temporära filer och rensas ofta vid omstart."
            },
            {
                "question": "Hur rensar du terminalskärmen?",
                "options": ["clean", "cls", "clear", "wipe"],
                "correct": 2,
                "explanation": "clear rensar skärmen. Ctrl+L gör samma sak."
            },
            {
                "question": "Vilket kommando visar diskutrymme?",
                "options": ["disk -h", "df -h", "space -h", "du -h"],
                "correct": 1,
                "explanation": "df (disk free) visar diskutrymme. du visar katalogers storlek."
            },
            {
                "question": "Hur avbryter du ett körande kommando?",
                "options": ["Ctrl+X", "Ctrl+C", "Ctrl+Z", "Ctrl+Q"],
                "correct": 1,
                "explanation": "Ctrl+C skickar SIGINT och avbryter processen. Ctrl+Z pausar den istället."
            },
            {
                "question": "Vad gör 'cat filnamn'?",
                "options": ["Skapar filen", "Visar filinnehåll", "Tar bort filen", "Kopierar filen"],
                "correct": 1,
                "explanation": "cat (concatenate) visar innehållet i en fil i terminalen."
            },
            {
                "question": "Var installeras de flesta program?",
                "options": ["/bin", "/usr/bin", "/opt/bin", "/home/bin"],
                "correct": 1,
                "explanation": "/usr/bin innehåller de flesta användarprogram installerade med pakethanteraren."
            },
            {
                "question": "Hur listar du dolda filer?",
                "options": ["ls -h", "ls -a", "ls -d", "ls -f"],
                "correct": 1,
                "explanation": "ls -a visar alla filer inklusive dolda (som börjar med punkt)."
            },
        ],
        "medium": [
            {
                "question": "Vad betyder permissions 755?",
                "options": [
                    "Alla har full access",
                    "Ägare: rwx, Grupp: r-x, Andra: r-x",
                    "Ägare: rw-, Grupp: r--, Andra: r--",
                    "Endast ägare har access"
                ],
                "correct": 1,
                "explanation": "7=rwx(4+2+1), 5=r-x(4+0+1). Ägare kan allt, andra kan läsa och köra."
            },
            {
                "question": "Hur söker du efter text i filer?",
                "options": ["find 'text'", "search 'text'", "grep 'text' fil", "locate 'text'"],
                "correct": 2,
                "explanation": "grep söker efter mönster i filer. find söker efter filnamn."
            },
            {
                "question": "Vad gör pipe-symbolen |?",
                "options": [
                    "Skriver till fil",
                    "Skickar output till nästa kommando",
                    "Kör kommandon parallellt",
                    "Skapar bakgrundsprocess"
                ],
                "correct": 1,
                "explanation": "Pipe (|) tar output från ett kommando och skickar som input till nästa."
            },
            {
                "question": "Hur visar du alla körande processer?",
                "options": ["top -a", "ps aux", "proc list", "tasks all"],
                "correct": 1,
                "explanation": "ps aux visar alla processer. top/htop visar dem i realtid."
            },
            {
                "question": "Vad gör 'systemctl restart nginx'?",
                "options": [
                    "Installerar nginx",
                    "Startar om nginx-tjänsten",
                    "Aktiverar nginx vid boot",
                    "Visar nginx-status"
                ],
                "correct": 1,
                "explanation": "restart stoppar och startar tjänsten igen för att ladda ny config."
            },
            {
                "question": "Hur dödar du en process med PID 1234?",
                "options": ["stop 1234", "kill 1234", "end 1234", "close 1234"],
                "correct": 1,
                "explanation": "kill skickar signal till process. kill -9 tvingar avslut."
            },
            {
                "question": "Vad innehåller /etc/passwd?",
                "options": ["Krypterade lösenord", "Användarinformation", "Systemloggar", "Nätverkskonfiguration"],
                "correct": 1,
                "explanation": "/etc/passwd innehåller användarinfo (namn, UID, hemkatalog). Lösenord finns i /etc/shadow."
            },
            {
                "question": "Hur lägger du till användare i en grupp?",
                "options": [
                    "groupadd user group",
                    "usermod -aG grupp användare",
                    "addgroup user group",
                    "useradd -g user group"
                ],
                "correct": 1,
                "explanation": "usermod -aG lägger till användare i grupp. -a behåller befintliga grupper."
            },
            {
                "question": "Vad gör cron?",
                "options": [
                    "Övervakar systemet",
                    "Schemalägger återkommande jobb",
                    "Hanterar användare",
                    "Roterar loggar"
                ],
                "correct": 1,
                "explanation": "cron kör kommandon automatiskt enligt schema. crontab -e redigerar."
            },
            {
                "question": "Hur monterar du en disk?",
                "options": [
                    "attach /dev/sdb1 /mnt",
                    "mount /dev/sdb1 /mnt",
                    "connect /dev/sdb1 /mnt",
                    "link /dev/sdb1 /mnt"
                ],
                "correct": 1,
                "explanation": "mount kopplar ett filsystem till en katalog. umount avmonterar."
            },
            {
                "question": "Vad gör 'tar -xzvf arkiv.tar.gz'?",
                "options": [
                    "Skapar ett arkiv",
                    "Listar arkivinnehåll",
                    "Extraherar arkivet",
                    "Komprimerar filer"
                ],
                "correct": 2,
                "explanation": "x=extract, z=gunzip, v=verbose, f=filename. Extraherar arkivet."
            },
            {
                "question": "Hur visar du öppna portar?",
                "options": [
                    "ports -l",
                    "netstat -tulpn",
                    "show ports",
                    "portlist -a"
                ],
                "correct": 1,
                "explanation": "netstat -tulpn eller ss -tulpn visar lyssnande portar och processer."
            },
            {
                "question": "Vad gör 'sudo'?",
                "options": [
                    "Byter användare permanent",
                    "Kör kommando som root",
                    "Skapar administratör",
                    "Visar root-lösenord"
                ],
                "correct": 1,
                "explanation": "sudo kör ett kommando med root-rättigheter efter lösenordskontroll."
            },
            {
                "question": "Hur omdirigerar du stderr till fil?",
                "options": ["kommando > fil", "kommando >> fil", "kommando 2> fil", "kommando &> fil"],
                "correct": 2,
                "explanation": "2> omdirigerar stderr (fd 2). > omdirigerar stdout (fd 1). &> båda."
            },
            {
                "question": "Vad är syftet med /etc/fstab?",
                "options": [
                    "Lista körande processer",
                    "Definera automatisk montering",
                    "Konfigurera nätverk",
                    "Hantera användare"
                ],
                "correct": 1,
                "explanation": "fstab definierar vilka filsystem som monteras automatiskt vid boot."
            },
            {
                "question": "Hur skapar du en ny användare med hemkatalog?",
                "options": [
                    "useradd namn",
                    "useradd -m namn",
                    "adduser --home namn",
                    "newuser -h namn"
                ],
                "correct": 1,
                "explanation": "useradd -m skapar användare med hemkatalog. Utan -m skapas ingen hemkatalog."
            },
            {
                "question": "Vad visar 'ip addr'?",
                "options": [
                    "Routing-tabell",
                    "Nätverksinterface och IP-adresser",
                    "DNS-konfiguration",
                    "Aktiva anslutningar"
                ],
                "correct": 1,
                "explanation": "ip addr visar alla nätverksinterface med IP-adresser. Ersätter ifconfig."
            },
            {
                "question": "Hur schemalägger du ett jobb varje dag kl 03:00?",
                "options": [
                    "0 3 * * * /script.sh",
                    "3 0 * * * /script.sh",
                    "* 3 * * * /script.sh",
                    "0 * 3 * * /script.sh"
                ],
                "correct": 0,
                "explanation": "Cron-format: minut timme dag månad veckodag. 0 3 = 03:00."
            },
            {
                "question": "Vad gör kommandot 'chmod u+x fil'?",
                "options": [
                    "Tar bort execute för alla",
                    "Lägger till execute för ägaren",
                    "Ändrar ägare",
                    "Lägger till execute för alla"
                ],
                "correct": 1,
                "explanation": "u=user/ägare, +=lägg till, x=execute. Gör filen körbar för ägaren."
            },
            {
                "question": "Hur testar du om en port är öppen på fjärrserver?",
                "options": [
                    "ping server:port",
                    "telnet server port",
                    "check server port",
                    "test server port"
                ],
                "correct": 1,
                "explanation": "telnet/nc (netcat) testar TCP-anslutning. ping testar bara ICMP."
            },
        ],
        "hard": [
            {
                "question": "Vilket iptables-kommando blockerar inkommande trafik på port 22?",
                "options": [
                    "iptables -A OUTPUT -p tcp --dport 22 -j DROP",
                    "iptables -A INPUT -p tcp --dport 22 -j DROP",
                    "iptables -A FORWARD -p tcp --dport 22 -j DROP",
                    "iptables -A INPUT -p tcp --sport 22 -j DROP"
                ],
                "correct": 1,
                "explanation": "INPUT-kedjan hanterar inkommande trafik, --dport är destination port."
            },
            {
                "question": "Vad gör 'echo 1 > /proc/sys/net/ipv4/ip_forward'?",
                "options": [
                    "Stänger av brandväggen",
                    "Aktiverar IP-forwarding/routing",
                    "Aktiverar IPv6",
                    "Blockerar all trafik"
                ],
                "correct": 1,
                "explanation": "ip_forward=1 gör att Linux kan routra paket mellan interface. Krävs för NAT."
            },
            {
                "question": "Vad visar 'strace -p 1234'?",
                "options": [
                    "Nätverkstrafik för processen",
                    "Systemanrop processen gör",
                    "Minnesanvändning",
                    "CPU-användning"
                ],
                "correct": 1,
                "explanation": "strace spårar systemanrop (syscalls). Ovärderligt för debugging."
            },
            {
                "question": "Vilken SELinux-läge loggar överträdelser utan att blockera?",
                "options": ["disabled", "enforcing", "permissive", "logging"],
                "correct": 2,
                "explanation": "permissive loggar men blockerar inte. enforcing blockerar. disabled är av."
            },
            {
                "question": "Hur analyserar du vilken tjänst som fördröjer boot mest?",
                "options": [
                    "dmesg | grep slow",
                    "systemd-analyze blame",
                    "boot --analyze",
                    "journalctl --boot-time"
                ],
                "correct": 1,
                "explanation": "systemd-analyze blame listar tjänster sorterade efter starttid."
            },
            {
                "question": "Vad indikerar hög 'wa' i top-output?",
                "options": [
                    "Hög CPU-användning",
                    "Väntan på disk I/O",
                    "Minnesbrist",
                    "Nätverksproblem"
                ],
                "correct": 1,
                "explanation": "wa (iowait) visar tid CPU:n väntar på disk. Hög wa = disk bottleneck."
            },
            {
                "question": "Hur hittar du vilken process som använder port 80?",
                "options": [
                    "ps aux | grep 80",
                    "netstat -p 80",
                    "lsof -i :80",
                    "find -port 80"
                ],
                "correct": 2,
                "explanation": "lsof -i :80 visar processer som lyssnar eller ansluter på port 80."
            },
            {
                "question": "Vad är skillnaden mellan hard link och symbolic link?",
                "options": [
                    "Hard link kopierar data, symbolic kopierar inte",
                    "Hard link pekar på inode, symbolic pekar på sökväg",
                    "Symbolic link fungerar över filsystem, hard link gör inte",
                    "Både B och C är korrekta"
                ],
                "correct": 3,
                "explanation": "Hard links delar inode (samma data). Symbolic links är sökvägar som kan korsa filsystem."
            },
            {
                "question": "Hur begränsar du en process till max 50% CPU med cgroups?",
                "options": [
                    "cpulimit -p PID -l 50",
                    "nice -n 50 command",
                    "Skapa cgroup med cpu.cfs_quota_us=50000",
                    "renice 50 PID"
                ],
                "correct": 2,
                "explanation": "cgroups använder cpu.cfs_quota_us. 50000 av 100000 (period) = 50%. cpulimit är enklare alternativ."
            },
            {
                "question": "Vilken namespace isolerar nätverksstack?",
                "options": ["pid", "net", "mnt", "uts"],
                "correct": 1,
                "explanation": "net namespace ger isolerad nätverksstack. Varje container har sin egen."
            },
            {
                "question": "Vad gör OOM killer?",
                "options": [
                    "Dödar processer med hög CPU",
                    "Dödar processer när minnet tar slut",
                    "Rensar cache automatiskt",
                    "Roterar loggar"
                ],
                "correct": 1,
                "explanation": "Out Of Memory killer dödar processer för att frigöra RAM och undvika systemkrasch."
            },
            {
                "question": "Hur kontrollerar du inode-användning?",
                "options": ["df -h", "df -i", "du -i", "stat -i"],
                "correct": 1,
                "explanation": "df -i visar inode-användning. Man kan få slut på inodes med många små filer."
            },
            {
                "question": "Vad innebär RAID 5?",
                "options": [
                    "Speglar data på två diskar",
                    "Stripar data utan redundans",
                    "Stripar med distribuerad paritet",
                    "Kombinerar RAID 0 och RAID 1"
                ],
                "correct": 2,
                "explanation": "RAID 5 stripar data och fördelar paritet över alla diskar. Tål en diskfel."
            },
            {
                "question": "Hur utökar du en ext4 LVM-partition online?",
                "options": [
                    "lvextend -L +10G /dev/vg/lv && resize2fs /dev/vg/lv",
                    "lvresize -L +10G /dev/vg/lv",
                    "fdisk /dev/vg/lv && resize2fs",
                    "growpart /dev/vg/lv"
                ],
                "correct": 0,
                "explanation": "lvextend utökar LV, resize2fs utökar filsystemet. Kan göras online för ext4."
            },
            {
                "question": "Vad gör 'rsync --delete'?",
                "options": [
                    "Tar bort källfiler efter kopiering",
                    "Tar bort filer i mål som inte finns i källa",
                    "Tar bort tomma kataloger",
                    "Tar bort gamla backuper"
                ],
                "correct": 1,
                "explanation": "--delete gör målet till exakt kopia - filer som tagits bort från källa tas bort från mål."
            },
            {
                "question": "Vilken kernel-parameter styr swap-aggressivitet?",
                "options": ["vm.swapfree", "vm.swappiness", "vm.swap_ratio", "vm.swapuse"],
                "correct": 1,
                "explanation": "vm.swappiness (0-100) styr hur aggressivt systemet swappar. Lägre = mindre swap."
            },
            {
                "question": "Hur skapar du en RAID 1 med mdadm?",
                "options": [
                    "mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/sdb /dev/sdc",
                    "mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc",
                    "mdadm --build /dev/md0 --level=mirror /dev/sdb /dev/sdc",
                    "mdraid create md0 mirror sdb sdc"
                ],
                "correct": 1,
                "explanation": "--level=1 är mirror (RAID 1). Data skrivs till båda diskar för redundans."
            },
            {
                "question": "Vad loggar auditd?",
                "options": [
                    "Endast inloggningsförsök",
                    "Systemanrop och säkerhetshändelser enligt regler",
                    "Alla filoperationer",
                    "Nätverkstrafik"
                ],
                "correct": 1,
                "explanation": "auditd loggar baserat på auditctl-regler. Kan logga filändringar, syscalls, etc."
            },
            {
                "question": "Hur debuggar du en kraschande process med core dump?",
                "options": [
                    "strace -c corefile",
                    "gdb program corefile",
                    "cat corefile | debug",
                    "coredump analyze program"
                ],
                "correct": 1,
                "explanation": "gdb (GNU Debugger) läser core dumps. bt (backtrace) visar stacken vid krasch."
            },
            {
                "question": "Vad gör 'sync && echo 3 > /proc/sys/vm/drop_caches'?",
                "options": [
                    "Startar om nätverket",
                    "Synkar och tömmer page cache",
                    "Aktiverar swap",
                    "Rensar alla loggar"
                ],
                "correct": 1,
                "explanation": "sync skriver buffrar till disk. drop_caches=3 frigör page cache, dentries och inodes."
            },
        ],
    },

    # =========================================================================
    # NODE MAPPING - Kopplar nodes till flashcards/quiz
    # =========================================================================
    "nodes": [
        {"id": 1, "title": "Filesystem Hierarchy Standard (FHS)", "slug": "filesystem-hierarchy-standard"},
        {"id": 2, "title": "Mount Points och Device Files", "slug": "mount-points-device-files"},
        {"id": 3, "title": "Grundläggande filoperationer", "slug": "basic-file-operations"},
        {"id": 4, "title": "Permissions och ägande", "slug": "permissions-ownership"},
        {"id": 5, "title": "Textprocessering", "slug": "text-processing"},
        {"id": 6, "title": "Vim och texteditorer", "slug": "vim-text-editors"},
        {"id": 7, "title": "Pipes och redirects", "slug": "pipes-redirects"},
        {"id": 8, "title": "Användare och grupper", "slug": "users-groups"},
        {"id": 9, "title": "Pakethantering", "slug": "package-management"},
        {"id": 10, "title": "Systemd och tjänster", "slug": "systemd-services"},
        {"id": 11, "title": "Diskhantering och LVM", "slug": "disk-management-lvm"},
        {"id": 12, "title": "Nätverk: Grunderna", "slug": "networking-basics"},
        {"id": 13, "title": "DNS och namnsökning", "slug": "dns-name-resolution"},
        {"id": 14, "title": "Brandväggar: iptables/nftables", "slug": "firewalls-iptables"},
        {"id": 15, "title": "SSH och fjärradministration", "slug": "ssh-remote-admin"},
        {"id": 16, "title": "Arkivering och backup", "slug": "archiving-backup"},
        {"id": 17, "title": "Cron och schemaläggning", "slug": "cron-scheduling"},
        {"id": 18, "title": "Logghantering", "slug": "log-management"},
        {"id": 19, "title": "Prestandaövervakning", "slug": "performance-monitoring"},
        {"id": 20, "title": "Felsökning och debugging", "slug": "troubleshooting-debugging"},
    ],
}
