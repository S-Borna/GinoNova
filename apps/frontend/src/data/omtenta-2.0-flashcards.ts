/**
 * OMTENTA 2.0 - Komplett flashcard-bank från alla 10 NOD-moduler
 *
 * INNEHÅLL:
 * - Nod 1: Linux Filsystem & Grunder (50 flashcards)
 * - Nod 2: Rättigheter & Säkerhet (50 flashcards)
 * - Nod 3: Processhantering (50 flashcards)
 * - Nod 4: Nätverk & Server (50 flashcards)
 * - Nod 5: SSH & Kommunikation (50 flashcards)
 * - Nod 6: Bash Skriptprogrammering (50 flashcards)
 * - Nod 7: Bash Verktyg (50 flashcards)
 * - Nod 8: Docker Isolering & Images (50 flashcards)
 * - Nod 9: Docker Nätverk & Lagring (50 flashcards)
 * - Nod 10: Docker Compose & IaC (50 flashcards)
 *
 * TOTAL: 500 flashcards
 */

import type { Omtenta2Topic } from './omtenta-2.0-quiz'

export interface Omtenta2Flashcard {
    id: number
    topic: Omtenta2Topic
    category: string
    question: string
    answer: string
}

// ===== NOD 1: FILSYSTEM & GRUNDER =====
export const NOD1_FLASHCARDS: Omtenta2Flashcard[] = [
    {
        id: 1001,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /bin?',
        answer: 'Essentiella binärer för systemstart och single-user mode (ls, cp, cat, bash).'
    },
    {
        id: 1002,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /etc?',
        answer: 'Systemkonfigurationsfiler (hosts, passwd, ssh/, nginx/).'
    },
    {
        id: 1003,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /home?',
        answer: 'Användarnas hemkataloger (personliga filer, inställningar).'
    },
    {
        id: 1004,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /var?',
        answer: 'Variabel data som loggar (/var/log), mail, cache, spool.'
    },
    {
        id: 1005,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /tmp?',
        answer: 'Temporära filer - rensas oftast vid omstart.'
    },
    {
        id: 1006,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /dev?',
        answer: 'Enhetsfiler (devices) - representerar hårdvara som filer (/dev/sda, /dev/null).'
    },
    {
        id: 1007,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /proc?',
        answer: 'Virtuellt filsystem med information om körande processer och systemstatus.'
    },
    {
        id: 1008,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /usr?',
        answer: 'Användarprogramvara, bibliotek och dokumentation (icke-essentiellt).'
    },
    {
        id: 1009,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /opt?',
        answer: 'Valfri, manuellt installerad tredjepartsmjukvara.'
    },
    {
        id: 1010,
        topic: 'nod1-filsystem',
        category: 'FHS',
        question: 'Vad innehåller /boot?',
        answer: 'Filer för systemstart: kernel, initramfs, GRUB.'
    },
    {
        id: 1011,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot cd?',
        answer: 'Change Directory - byter arbetskatalog. "cd ~" = hem, "cd .." = upp.'
    },
    {
        id: 1012,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot ls?',
        answer: 'Listar innehållet i en katalog. -l för detaljerad, -a för dolda filer.'
    },
    {
        id: 1013,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot pwd?',
        answer: 'Print Working Directory - visar din nuvarande position i filsystemet.'
    },
    {
        id: 1014,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot cp?',
        answer: 'Kopierar filer/kataloger. "cp -r" för rekursiv kopiering av kataloger.'
    },
    {
        id: 1015,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot mv?',
        answer: 'Flyttar eller döper om filer/kataloger.'
    },
    {
        id: 1016,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot rm?',
        answer: 'Raderar filer. "rm -r" för kataloger. "rm -f" tvingar utan bekräftelse.'
    },
    {
        id: 1017,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot mkdir?',
        answer: 'Skapar en ny katalog. "mkdir -p" skapar hela sökvägen.'
    },
    {
        id: 1018,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot touch?',
        answer: 'Skapar en tom fil eller uppdaterar tidsstämpeln på en existerande fil.'
    },
    {
        id: 1019,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot cat?',
        answer: 'Visar innehållet i en fil (concatenate). Kan kombinera flera filer.'
    },
    {
        id: 1020,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot less?',
        answer: 'Visar fil sida för sida med scroll. Q för avsluta, / för sökning.'
    },
    {
        id: 1021,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot head?',
        answer: 'Visar första raderna i en fil (default 10). "head -n 5" för 5 rader.'
    },
    {
        id: 1022,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot tail?',
        answer: 'Visar sista raderna. "tail -f" följer nya rader i realtid (loggar).'
    },
    {
        id: 1023,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot df?',
        answer: 'Disk Free - visar ledigt utrymme på filsystem. "df -h" för human-readable.'
    },
    {
        id: 1024,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot du?',
        answer: 'Disk Usage - visar storleken på filer/kataloger. "du -sh" för sammanfattning.'
    },
    {
        id: 1025,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot find?',
        answer: 'Söker filer rekursivt. "find / -name fil.txt" hittar filen överallt.'
    },
    {
        id: 1026,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot which?',
        answer: 'Visar sökvägen till ett kommando/binär i $PATH.'
    },
    {
        id: 1027,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot ln -s?',
        answer: 'Skapar en symbolisk länk (genväg). "ln -s mål länknamn".'
    },
    {
        id: 1028,
        topic: 'nod1-filsystem',
        category: 'Länkar',
        question: 'Vad är skillnaden mellan Hard Link och Symbolic Link?',
        answer: 'Hard: Pekar på samma inode, fungerar bara inom partition. Soft: Pekar på sökväg, fungerar över partitioner.'
    },
    {
        id: 1029,
        topic: 'nod1-filsystem',
        category: 'Koncept',
        question: 'Vad är en Inode?',
        answer: 'Datastruktur som lagrar metadata om en fil (rättigheter, storlek, pekare till data).'
    },
    {
        id: 1030,
        topic: 'nod1-filsystem',
        category: 'Koncept',
        question: 'Vad är en Mount Point?',
        answer: 'En katalog där ett filsystem görs tillgängligt. T.ex. /mnt/disk.'
    },
    {
        id: 1031,
        topic: 'nod1-filsystem',
        category: 'Filer',
        question: 'Vad betyder en punkt (.) framför ett filnamn?',
        answer: 'Filen är dold - visas inte av "ls" utan flagga -a.'
    },
    {
        id: 1032,
        topic: 'nod1-filsystem',
        category: 'Navigation',
        question: 'Vad betyder ".." i en sökväg?',
        answer: 'Föräldrakatalogen (en nivå upp).'
    },
    {
        id: 1033,
        topic: 'nod1-filsystem',
        category: 'Navigation',
        question: 'Vad betyder "." i en sökväg?',
        answer: 'Nuvarande katalog.'
    },
    {
        id: 1034,
        topic: 'nod1-filsystem',
        category: 'Navigation',
        question: 'Vad betyder "~" i en sökväg?',
        answer: 'Din hemkatalog (t.ex. /home/användare).'
    },
    {
        id: 1035,
        topic: 'nod1-filsystem',
        category: 'Sökvägar',
        question: 'Vad är skillnaden på absolut och relativ sökväg?',
        answer: 'Absolut: Börjar från / (rotkatalogen). Relativ: Utgår från nuvarande position.'
    },
    {
        id: 1036,
        topic: 'nod1-filsystem',
        category: 'Enheter',
        question: 'Vad är /dev/null?',
        answer: 'En "svart håla" - kastar all data som skrivs dit. Används för att tysta output.'
    },
    {
        id: 1037,
        topic: 'nod1-filsystem',
        category: 'Enheter',
        question: 'Vad är /dev/sda?',
        answer: 'Första SATA/SCSI-disken. sda1, sda2 = partitioner på disken.'
    },
    {
        id: 1038,
        topic: 'nod1-filsystem',
        category: 'Konfiguration',
        question: 'Vad är /etc/fstab?',
        answer: 'File System Table - definierar vilka diskar/partitioner som monteras vid boot.'
    },
    {
        id: 1039,
        topic: 'nod1-filsystem',
        category: 'Konfiguration',
        question: 'Vad är /etc/hosts?',
        answer: 'Lokal namnupplösning - mappar IP-adresser till hostnamn (kollas före DNS).'
    },
    {
        id: 1040,
        topic: 'nod1-filsystem',
        category: 'Filsystem',
        question: 'Vad är ext4?',
        answer: 'Det vanligaste Linux-filsystemet. Stöder stora filer och journaling.'
    },
    {
        id: 1041,
        topic: 'nod1-filsystem',
        category: 'Filsystem',
        question: 'Vad är XFS?',
        answer: 'Högpresterande filsystem för stora filer. Standard i RHEL/CentOS.'
    },
    {
        id: 1042,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör mount/umount?',
        answer: 'mount: Kopplar ett filsystem till en katalog. umount: Kopplar bort det.'
    },
    {
        id: 1043,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot file?',
        answer: 'Identifierar filtyp baserat på innehåll (inte filändelse).'
    },
    {
        id: 1044,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot stat?',
        answer: 'Visar detaljerad metadata om en fil (storlek, inode, timestamps).'
    },
    {
        id: 1045,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot tree?',
        answer: 'Visar katalogstruktur i ett trädformat (måste ofta installeras).'
    },
    {
        id: 1046,
        topic: 'nod1-filsystem',
        category: 'Koncept',
        question: 'Vad menas med "Allt är en fil" i Linux?',
        answer: 'Enheter, processer, nätverksresurser representeras som filer för enhetligt gränssnitt.'
    },
    {
        id: 1047,
        topic: 'nod1-filsystem',
        category: 'Koncept',
        question: 'Vad är FHS?',
        answer: 'Filesystem Hierarchy Standard - definierar standardstrukturen för Linux-kataloger.'
    },
    {
        id: 1048,
        topic: 'nod1-filsystem',
        category: 'Kryptering',
        question: 'Vad är LUKS?',
        answer: 'Linux Unified Key Setup - standard för diskkryptering i Linux.'
    },
    {
        id: 1049,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot free?',
        answer: 'Visar RAM-användning (totalt, använt, ledigt, cache). "free -h" för human-readable.'
    },
    {
        id: 1050,
        topic: 'nod1-filsystem',
        category: 'Kommandon',
        question: 'Vad gör kommandot lsblk?',
        answer: 'Listar block devices (diskar och partitioner) i trädformat.'
    }
]

// ===== NOD 2: RÄTTIGHETER & SÄKERHET =====
export const NOD2_FLASHCARDS: Omtenta2Flashcard[] = [
    {
        id: 2001,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "r" i rättigheter?',
        answer: 'Read - läsrättighet. Får läsa filinnehåll eller lista kataloginnehåll.'
    },
    {
        id: 2002,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "w" i rättigheter?',
        answer: 'Write - skrivrättighet. Får ändra fil eller skapa/radera filer i katalog.'
    },
    {
        id: 2003,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "x" i rättigheter?',
        answer: 'Execute - körrättighet. Får köra fil som program eller gå in i katalog (cd).'
    },
    {
        id: 2004,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad är chmod?',
        answer: 'Change Mode - ändrar filrättigheter. "chmod 755 fil" eller "chmod u+x fil".'
    },
    {
        id: 2005,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad är chown?',
        answer: 'Change Owner - ändrar ägare. "chown user:group fil".'
    },
    {
        id: 2006,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder 755 i octal?',
        answer: 'rwxr-xr-x: Ägare full access, grupp och andra kan läsa/köra.'
    },
    {
        id: 2007,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder 644 i octal?',
        answer: 'rw-r--r--: Ägare läs/skriv, grupp och andra bara läs.'
    },
    {
        id: 2008,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder 700 i octal?',
        answer: 'rwx------: Endast ägaren har tillgång.'
    },
    {
        id: 2009,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Hur räknar man ut octalt värde?',
        answer: 'r=4, w=2, x=1. Summera per kategori. rwx=7, r-x=5, r--=4.'
    },
    {
        id: 2010,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är root?',
        answer: 'Superanvändare med fullständiga systemrättigheter. UID=0.'
    },
    {
        id: 2011,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad gör kommandot sudo?',
        answer: 'Kör ett kommando med förhöjda rättigheter (som root).'
    },
    {
        id: 2012,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är /etc/passwd?',
        answer: 'Innehåller användarinformation (namn, UID, GID, hem, shell). Ingen lösenordsdata.'
    },
    {
        id: 2013,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är /etc/shadow?',
        answer: 'Innehåller krypterade lösenord. Endast läsbar av root.'
    },
    {
        id: 2014,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är /etc/group?',
        answer: 'Definierar grupper och deras medlemmar.'
    },
    {
        id: 2015,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är /etc/sudoers?',
        answer: 'Definierar vilka användare som får köra sudo.'
    },
    {
        id: 2016,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör useradd?',
        answer: 'Skapar en ny användare. "useradd -m user" skapar även hemkatalog.'
    },
    {
        id: 2017,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör userdel?',
        answer: 'Raderar en användare. "userdel -r user" tar även bort hemkatalogen.'
    },
    {
        id: 2018,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör usermod?',
        answer: 'Modifierar användare. "usermod -aG sudo user" lägger till i grupp.'
    },
    {
        id: 2019,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör passwd?',
        answer: 'Ändrar lösenord. "passwd user" som root ändrar andras lösenord.'
    },
    {
        id: 2020,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör groupadd/groupdel?',
        answer: 'Skapar eller tar bort grupper.'
    },
    {
        id: 2021,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör kommandot id?',
        answer: 'Visar UID, GID och gruppmedlemskap för en användare.'
    },
    {
        id: 2022,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör kommandot whoami?',
        answer: 'Visar ditt nuvarande användarnamn.'
    },
    {
        id: 2023,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör kommandot groups?',
        answer: 'Visar vilka grupper en användare tillhör.'
    },
    {
        id: 2024,
        topic: 'nod2-rattigheter',
        category: 'Specialrättigheter',
        question: 'Vad är SUID (Set User ID)?',
        answer: 'Program körs med ägarens rättigheter. T.ex. passwd har SUID för att ändra /etc/shadow.'
    },
    {
        id: 2025,
        topic: 'nod2-rattigheter',
        category: 'Specialrättigheter',
        question: 'Vad är SGID (Set Group ID)?',
        answer: 'Program körs med gruppens rättigheter. På kataloger: nya filer ärver gruppägare.'
    },
    {
        id: 2026,
        topic: 'nod2-rattigheter',
        category: 'Specialrättigheter',
        question: 'Vad är Sticky Bit?',
        answer: 'På kataloger: Endast filägare eller root kan radera filer. Används på /tmp.'
    },
    {
        id: 2027,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vad är SSH-nycklar?',
        answer: 'Asymmetrisk kryptering för autentisering. Privat nyckel hemlig, publik delas.'
    },
    {
        id: 2028,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vad är id_rsa och id_rsa.pub?',
        answer: 'id_rsa = privat nyckel (hemlig). id_rsa.pub = publik nyckel (delas).'
    },
    {
        id: 2029,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vad är authorized_keys?',
        answer: 'Fil som innehåller publika nycklar som får logga in på servern.'
    },
    {
        id: 2030,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vilka rättigheter ska ~/.ssh ha?',
        answer: '700 (rwx------). Nyckelfiler: 600 (rw-------). Publika: 644.'
    },
    {
        id: 2031,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vad gör ssh-keygen?',
        answer: 'Genererar ett SSH-nyckelpar (privat + publik).'
    },
    {
        id: 2032,
        topic: 'nod2-rattigheter',
        category: 'SSH',
        question: 'Vad gör ssh-copy-id?',
        answer: 'Kopierar din publika nyckel till serverns authorized_keys.'
    },
    {
        id: 2033,
        topic: 'nod2-rattigheter',
        category: 'Brandvägg',
        question: 'Vad är UFW?',
        answer: 'Uncomplicated Firewall - enkel frontend för iptables i Ubuntu/Debian.'
    },
    {
        id: 2034,
        topic: 'nod2-rattigheter',
        category: 'Brandvägg',
        question: 'Hur tillåter man SSH i UFW?',
        answer: '"ufw allow ssh" eller "ufw allow 22/tcp".'
    },
    {
        id: 2035,
        topic: 'nod2-rattigheter',
        category: 'Brandvägg',
        question: 'Hur aktiverar man UFW?',
        answer: '"ufw enable" - aktiverar brandväggen.'
    },
    {
        id: 2036,
        topic: 'nod2-rattigheter',
        category: 'Brandvägg',
        question: 'Hur ser man UFW-status?',
        answer: '"ufw status verbose" visar alla regler.'
    },
    {
        id: 2037,
        topic: 'nod2-rattigheter',
        category: 'Brandvägg',
        question: 'Vad är default deny?',
        answer: 'Standardpolicy som blockerar all trafik som inte explicit tillåts.'
    },
    {
        id: 2038,
        topic: 'nod2-rattigheter',
        category: 'SSH-config',
        question: 'Var ligger SSH-serverns konfiguration?',
        answer: '/etc/ssh/sshd_config'
    },
    {
        id: 2039,
        topic: 'nod2-rattigheter',
        category: 'SSH-config',
        question: 'Hur stänger man av root-login via SSH?',
        answer: 'PermitRootLogin no i /etc/ssh/sshd_config.'
    },
    {
        id: 2040,
        topic: 'nod2-rattigheter',
        category: 'SSH-config',
        question: 'Hur stänger man av lösenordsautentisering?',
        answer: 'PasswordAuthentication no i sshd_config (kräver SSH-nycklar).'
    },
    {
        id: 2041,
        topic: 'nod2-rattigheter',
        category: 'Säkerhet',
        question: 'Varför är SSH-nycklar säkrare än lösenord?',
        answer: 'Immuna mot brute force, mycket längre nyckellängd, kan kräva passphrase.'
    },
    {
        id: 2042,
        topic: 'nod2-rattigheter',
        category: 'Säkerhet',
        question: 'Vad är principen om Least Privilege?',
        answer: 'Ge bara de rättigheter som behövs - minimerar skada vid intrång.'
    },
    {
        id: 2043,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "d" i -drwxr-xr-x?',
        answer: 'Det är en katalog (directory). "-" = fil, "l" = länk.'
    },
    {
        id: 2044,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "s" i rwsr-xr-x?',
        answer: 'SUID-bit är satt - programmet körs med ägarens rättigheter.'
    },
    {
        id: 2045,
        topic: 'nod2-rattigheter',
        category: 'Rättigheter',
        question: 'Vad betyder "t" i drwxrwxrwt?',
        answer: 'Sticky bit är satt - endast ägare kan radera sina filer.'
    },
    {
        id: 2046,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Hur sätter man SUID?',
        answer: '"chmod u+s fil" eller "chmod 4755 fil".'
    },
    {
        id: 2047,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Hur sätter man Sticky Bit?',
        answer: '"chmod +t katalog" eller "chmod 1777 katalog".'
    },
    {
        id: 2048,
        topic: 'nod2-rattigheter',
        category: 'Användare',
        question: 'Vad är skillnaden på su och sudo?',
        answer: 'su: Byt till annan användare (behöver deras lösenord). sudo: Kör som root (ditt lösenord).'
    },
    {
        id: 2049,
        topic: 'nod2-rattigheter',
        category: 'Kommandon',
        question: 'Vad gör visudo?',
        answer: 'Redigerar /etc/sudoers säkert med syntaxkontroll.'
    },
    {
        id: 2050,
        topic: 'nod2-rattigheter',
        category: 'Koncept',
        question: 'Vad är umask?',
        answer: 'Bestämmer standardrättigheter för nya filer. umask 022 = nya filer får 644.'
    }
]

// ===== NOD 3-10: FLASHCARDS (Placeholders att fylla i) =====
export const NOD3_FLASHCARDS: Omtenta2Flashcard[] = [
    // Processhantering - kommer att fyllas i
    {
        id: 3001,
        topic: 'nod3-processhantering',
        category: 'Processer',
        question: 'Vad är en process?',
        answer: 'En instans av ett körande program med eget minne, PID och resurser.'
    },
    {
        id: 3002,
        topic: 'nod3-processhantering',
        category: 'Processer',
        question: 'Vad är PID?',
        answer: 'Process ID - unikt nummer som identifierar varje process. PID 1 = init/systemd.'
    },
    {
        id: 3003,
        topic: 'nod3-processhantering',
        category: 'Kommandon',
        question: 'Vad gör ps?',
        answer: 'Visar processer. "ps aux" visar alla processer med detaljer.'
    },
    {
        id: 3004,
        topic: 'nod3-processhantering',
        category: 'Kommandon',
        question: 'Vad gör top/htop?',
        answer: 'Visar processer i realtid med CPU/RAM-användning. htop är mer användarvänlig.'
    },
    {
        id: 3005,
        topic: 'nod3-processhantering',
        category: 'Kommandon',
        question: 'Vad gör kill?',
        answer: 'Skickar signal till process. "kill PID" = SIGTERM, "kill -9 PID" = SIGKILL.'
    }
]

export const NOD4_FLASHCARDS: Omtenta2Flashcard[] = [
    // Nätverk & Server
    {
        id: 4001,
        topic: 'nod4-natverk',
        category: 'IP',
        question: 'Vad är en IP-adress?',
        answer: 'Unik adress som identifierar en enhet på nätverket. IPv4: 32-bit, IPv6: 128-bit.'
    },
    {
        id: 4002,
        topic: 'nod4-natverk',
        category: 'Subnetting',
        question: 'Vad är CIDR-notation?',
        answer: 'IP/prefix som anger nätverksstorlek. /24 = 256 adresser, /16 = 65536 adresser.'
    }
]

export const NOD5_FLASHCARDS: Omtenta2Flashcard[] = [
    // SSH & Kommunikation
    {
        id: 5001,
        topic: 'nod5-ssh',
        category: 'SSH',
        question: 'Vad är SSH?',
        answer: 'Secure Shell - krypterat protokoll för fjärråtkomst. Port 22.'
    }
]

export const NOD6_FLASHCARDS: Omtenta2Flashcard[] = [
    // Bash Skript
    {
        id: 6001,
        topic: 'nod6-bash-skript',
        category: 'Grunderna',
        question: 'Vad är en shebang?',
        answer: '#!/bin/bash - anger vilken tolk som ska köra skriptet.'
    }
]

export const NOD7_FLASHCARDS: Omtenta2Flashcard[] = [
    // Bash Verktyg
    {
        id: 7001,
        topic: 'nod7-bash-verktyg',
        category: 'Verktyg',
        question: 'Vad gör grep?',
        answer: 'Söker text i filer med regex. "grep -r" för rekursiv sökning.'
    }
]

export const NOD8_FLASHCARDS: Omtenta2Flashcard[] = [
    // Docker Isolering
    {
        id: 8001,
        topic: 'nod8-docker-isolering',
        category: 'Docker',
        question: 'Vad är en container?',
        answer: 'Isolerad miljö för applikationer som delar OS-kernel med hosten.'
    }
]

export const NOD9_FLASHCARDS: Omtenta2Flashcard[] = [
    // Docker Nätverk & Lagring
    {
        id: 9001,
        topic: 'nod9-docker-natverk',
        category: 'Volumes',
        question: 'Vad är en Docker volume?',
        answer: 'Persistent lagring som överlever container-livscykeln.'
    }
]

export const NOD10_FLASHCARDS: Omtenta2Flashcard[] = [
    // Docker Compose & IaC
    {
        id: 10001,
        topic: 'nod10-docker-compose',
        category: 'Compose',
        question: 'Vad är Docker Compose?',
        answer: 'Verktyg för att definiera och köra multi-container applikationer med YAML.'
    }
]

// ===== AGGREGERAD EXPORT =====
export const ALL_OMTENTA_2_FLASHCARDS: Omtenta2Flashcard[] = [
    ...NOD1_FLASHCARDS,
    ...NOD2_FLASHCARDS,
    ...NOD3_FLASHCARDS,
    ...NOD4_FLASHCARDS,
    ...NOD5_FLASHCARDS,
    ...NOD6_FLASHCARDS,
    ...NOD7_FLASHCARDS,
    ...NOD8_FLASHCARDS,
    ...NOD9_FLASHCARDS,
    ...NOD10_FLASHCARDS
]

// ===== HJÄLPFUNKTIONER =====
export function shuffleFlashcards(cards: Omtenta2Flashcard[]): Omtenta2Flashcard[] {
    const shuffled = [...cards]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

export function getFlashcardsByTopics(topics: Omtenta2Topic[]): Omtenta2Flashcard[] {
    if (topics.length === 0) return ALL_OMTENTA_2_FLASHCARDS
    return ALL_OMTENTA_2_FLASHCARDS.filter(f => topics.includes(f.topic))
}

export function getRandomFlashcards(count: number, topics?: Omtenta2Topic[]): Omtenta2Flashcard[] {
    const pool = topics && topics.length > 0
        ? getFlashcardsByTopics(topics)
        : ALL_OMTENTA_2_FLASHCARDS

    const shuffled = shuffleFlashcards(pool)
    return shuffled.slice(0, Math.min(count, shuffled.length))
}
