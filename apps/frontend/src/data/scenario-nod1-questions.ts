/**
 * NOD 1: Linux Filesystem & Fundamentals - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD1_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod1-s1',
        question: 'Du SSH:ar in på en ny prod-server och behöver hitta Apache-konfigurationen. Var letar du först?',
        options: ['/bin/apache', '/var/apache', '/etc/apache2', '/home/apache'],
        correctIndices: [2],
        explanation: '/etc innehåller systemkonfiguration. Apache config finns i /etc/apache2 (Debian) eller /etc/httpd (RHEL).',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s2',
        question: 'En utvecklare frågar: "Var hamnar filerna när jag kör apt install nginx?". Var installeras binärfilen nginx?',
        options: ['/home/nginx', '/opt/nginx/bin', '/usr/sbin/nginx', '/var/nginx'],
        correctIndices: [2],
        explanation: 'System-binärer från pakethanteraren hamnar i /usr/sbin (daemon) eller /usr/bin (vanliga program).',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s3',
        question: 'Du kör `ls -la /var/log` och ser att syslog är 2GB. Du tar bort filen men `df -h` visar fortfarande samma diskutrymme. Varför?',
        options: ['Du måste köra sync först', 'Filen används av en process som håller den öppen', 'Papperskorgen är full', 'Filsystemet måste unmountas'],
        correctIndices: [1],
        explanation: 'I Linux frigörs inte diskutrymme förrän ALLA processer som har filen öppen stänger sina file descriptors.',
        difficulty: 'VG',
        category: 'Inodes',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s4',
        question: 'Du kör `ls -li` och ser att två filer har samma inode-nummer. Vad innebär det?',
        options: ['Filerna är korrupta', 'Det är hard links till samma data', 'Det är symboliska länkar', 'En av filerna är en kopia'],
        correctIndices: [1],
        explanation: 'Samma inode = hard links. Båda "filnamnen" pekar på exakt samma data på disk.',
        difficulty: 'VG',
        category: 'Länkar',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s5',
        question: 'Du vill skapa en genväg till /var/log/syslog i din hemkatalog. Vilken typ av länk bör du använda?',
        options: ['Hard link - fungerar alltid', 'Symbolisk länk - pekar på sökvägen', 'Båda fungerar likadant', 'Ingen länk - bara kopiera filen'],
        correctIndices: [1],
        explanation: 'Symbolisk länk är bäst - den pekar på sökvägen och fungerar även om målfilsystemet ändras. Hard link fungerar inte över filsystemgränser.',
        difficulty: 'G',
        category: 'Länkar',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s6',
        question: 'Du kör `ls -la` och ser: `lrwxrwxrwx 1 root root 7 Jan 15 /bin -> usr/bin`. Vad betyder l i början?',
        options: ['Locked file', 'Large file', 'Symbolic link', 'Library file'],
        correctIndices: [2],
        explanation: 'l = symbolic link. Moderna Linux-system har /bin som symlink till /usr/bin för bakåtkompatibilitet.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s7',
        question: 'En kollega kör skriptet `/tmp/backup.sh` och får "Permission denied" trots att hen äger filen. Vad har hen glömt?',
        options: ['Att vara root', 'Att sätta execute-permission (chmod +x)', 'Att installera bash', 'Att reboota servern'],
        correctIndices: [1],
        explanation: 'Filer måste ha execute-permission (x) för att kunna köras. Lösning: chmod +x /tmp/backup.sh',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s8',
        question: 'Du får felmeddelandet "No space left on device" men `df -h` visar 50% ledigt. Vad kan vara problemet?',
        options: ['Disken är trasig', 'RAM-minnet är fullt', 'Inodes är slut', 'Nätverket är nere'],
        correctIndices: [2],
        explanation: 'Varje fil kräver en inode. Många små filer kan ta slut på inodes även om diskutrymme finns. Kolla med df -i.',
        difficulty: 'VG',
        category: 'Inodes',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s9',
        question: 'Du ska montera en USB-sticka på en server utan GUI. Du kör `lsblk` och ser enheten som `sdb1`. Var monterar du den?',
        options: ['/dev/sdb1', '/media/usb eller /mnt', '/home/usb', '/var/usb'],
        correctIndices: [1],
        explanation: '/mnt används för temporära mounts, /media för removable media. /dev innehåller device files, inte mount points.',
        difficulty: 'G',
        category: 'Mount',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s10',
        question: 'Du behöver skapa en katalog och dess föräldrar som inte finns: /var/www/app/public/images. Vilket kommando?',
        options: ['mkdir /var/www/app/public/images', 'mkdir -p /var/www/app/public/images', 'touch -r /var/www/app/public/images', 'create --recursive /var/www/app/public/images'],
        correctIndices: [1],
        explanation: 'mkdir -p skapar parent directories automatiskt. Utan -p failar kommandot om föräldern inte finns.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s11',
        question: 'En process skriver loggar till /var/log/app.log. Du vill följa loggarna i realtid. Vilket kommando?',
        options: ['cat /var/log/app.log', 'tail -f /var/log/app.log', 'head -n 100 /var/log/app.log', 'grep -r /var/log/app.log'],
        correctIndices: [1],
        explanation: 'tail -f "följer" filen och visar nya rader när de skrivs. Perfekt för att övervaka loggar i realtid.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s12',
        question: 'Du tar bort en symlink med `rm /var/www/current`. Vad händer med mappen den pekar på?',
        options: ['Mappen tas också bort', 'Mappen blir korrupt', 'Ingenting - endast länken tas bort', 'Systemet kraschar'],
        correctIndices: [2],
        explanation: 'rm på en symlink tar bara bort länken. Målet (target) påverkas inte. OBS: rm -rf på symlink-katalog kan ta bort innehållet!',
        difficulty: 'VG',
        category: 'Länkar',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s13',
        question: 'Du vill kopiera hela katalogen /etc/nginx till /backup/nginx med alla filer och mappar. Vilket kommando?',
        options: ['cp /etc/nginx /backup/', 'cp -r /etc/nginx /backup/', 'mv /etc/nginx /backup/', 'copy --all /etc/nginx /backup/'],
        correctIndices: [1],
        explanation: 'cp -r (recursive) kopierar kataloger och allt innehåll. Utan -r kopieras bara filer, inte kataloger.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s14',
        question: 'Du kör `file /bin/ls` och ser "ELF 64-bit LSB executable". Vad betyder ELF?',
        options: ['Error Log Format', 'Executable and Linkable Format', 'Extended Linux File', 'Encrypted Linux Format'],
        correctIndices: [1],
        explanation: 'ELF (Executable and Linkable Format) är standardformatet för körbar kod på Linux. Ersatte äldre a.out-formatet.',
        difficulty: 'VG',
        category: 'Filtyper',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s15',
        question: 'Du vill veta hur mycket diskutrymme katalogen /home tar. Vilket kommando ger den totala storleken?',
        options: ['df /home', 'ls -lh /home', 'du -sh /home', 'size /home'],
        correctIndices: [2],
        explanation: 'du -sh: -s = summary (endast total), -h = human-readable. df visar filsystem, inte katalogstorlek.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s16',
        question: 'I /etc/fstab står det: `/dev/sda1 / ext4 defaults 0 1`. Vad betyder siffran 1 i slutet?',
        options: ['Partition nummer', 'Mount prioritet', 'fsck-ordning vid boot', 'Antal mount-försök'],
        correctIndices: [2],
        explanation: 'Sista fältet i fstab är fsck pass nummer. 1 = root först, 2 = andra filsystem, 0 = ingen fsck.',
        difficulty: 'VG',
        category: 'fstab',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s17',
        question: 'Du behöver hitta var programmet nginx är installerat. Vilket kommando visar hela sökvägen?',
        options: ['find nginx', 'which nginx', 'locate nginx', 'search nginx'],
        correctIndices: [1],
        explanation: 'which visar sökvägen till körbara filer i PATH. locate söker i databas, find söker i filsystem.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s18',
        question: 'Du vill att /data/shared alltid mountas vid boot. Var lägger du mount-konfigurationen?',
        options: ['/etc/mounts', '/etc/fstab', '/boot/mount.conf', '/var/mount/auto'],
        correctIndices: [1],
        explanation: '/etc/fstab (filesystem table) läses vid boot och definierar vilka filsystem som ska mountas automatiskt.',
        difficulty: 'G',
        category: 'fstab',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s19',
        question: 'Du kör `stat /etc/passwd` och ser "Links: 1". Vad betyder det?',
        options: ['Filen är en symlink', 'Filen har en hard link (sig själv)', 'Filen är låst', 'Filen är komprimerad'],
        correctIndices: [1],
        explanation: 'Links visar antal hard links. 1 = bara originalet (varje fil är minst 1 hard link till sin inode).',
        difficulty: 'VG',
        category: 'Inodes',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s20',
        question: 'Du vill se dolda filer (som .bashrc) i din hemkatalog. Vilket ls-kommando använder du?',
        options: ['ls -l ~', 'ls -a ~', 'ls -hidden ~', 'ls --all ~'],
        correctIndices: [1],
        explanation: 'ls -a visar alla filer inkl. dolda (som börjar med punkt). -l ger bara lång listning utan dolda.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'scenario'
    }
]
