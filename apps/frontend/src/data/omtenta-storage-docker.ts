/**
 * INFÖR OMTENTA LINUX - Del 2: Block Storage, Kryptering & Docker
 * 100 quiz-frågor
 * 
 * Skapad: 2026-01-12
 */

import { OmtentaQuestion } from './omtenta-ssh-brandvagg'

// ============================================================================
// BLOCK STORAGE & KRYPTERING (50 frågor)
// ============================================================================

export const STORAGE_QUESTIONS: OmtentaQuestion[] = [
    {
        id: 'omtenta-storage-1',
        question: 'I vilken ordning skapar du ett krypterat filsystem på ny lagring?',
        options: ['Filesystem -> LUKS -> Partition', 'LUKS -> Block device -> Filesystem', 'Block device -> Partition -> LUKS -> Filesystem', 'Partition -> Filesystem -> LUKS'],
        correctIndex: 2,
        explanation: 'Rätt ordning: Block device finns → skapa partition → LUKS-kryptera → skapa filesystem.',
        difficulty: 'VG',
        category: 'LUKS'
    },
    {
        id: 'omtenta-storage-2',
        question: 'Vad är LUKS?',
        options: ['En filsystemtyp', 'En partitionstyp', 'Linux Unified Key Setup (diskkryptering)', 'En backup-metod'],
        correctIndex: 2,
        explanation: 'LUKS = Linux Unified Key Setup, standard för diskkryptering i Linux.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'omtenta-storage-3',
        question: 'Kommandot för att visa diskutrymme är...',
        options: ['df', 'space', 'disk', 'ls -s'],
        correctIndex: 0,
        explanation: 'df = disk free, visar ledigt/använt utrymme på monterade filsystem.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-4',
        question: 'Kommandot för att visa filstorlekar är...',
        options: ['df', 'size', 'du', 'ls -l'],
        correctIndex: 2,
        explanation: 'du = disk usage, visar storlek på filer och mappar.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-5',
        question: 'Vad gör kommandot lsblk?',
        options: ['Listar filer', 'Listar användare', 'Listar block devices', 'Listar processer'],
        correctIndex: 2,
        explanation: 'lsblk listar alla block devices (diskar, partitioner, etc.).',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-6',
        question: 'Kommandot fdisk används för att...',
        options: ['Formatera disk', 'Kryptera disk', 'Skapa och hantera partitioner', 'Montera disk'],
        correctIndex: 2,
        explanation: 'fdisk är ett verktyg för att skapa, ta bort och hantera partitioner.',
        difficulty: 'G',
        category: 'Partitioner'
    },
    {
        id: 'omtenta-storage-7',
        question: 'Vad är ett block device?',
        options: ['En fil', 'Ett nätverk', 'Lagringsenheter som disk/partition', 'En process'],
        correctIndex: 2,
        explanation: 'Block devices är lagringsenheter som läses/skrivs i block (diskar, USB, etc.).',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'omtenta-storage-8',
        question: 'Kommandot mkfs används för att...',
        options: ['Skapa mapp', 'Skapa partition', 'Montera disk', 'Skapa filsystem'],
        correctIndex: 3,
        explanation: 'mkfs = make filesystem, t.ex. mkfs.ext4 /dev/sda1.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-9',
        question: 'Vad gör kommandot mount?',
        options: ['Skapar filsystem', 'Krypterar disk', 'Monterar filsystem till en katalog', 'Formaterar disk'],
        correctIndex: 2,
        explanation: 'mount gör ett filsystem tillgängligt på en mount point (katalog).',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-10',
        question: 'Vilken fil innehåller permanent mount-konfiguration?',
        options: ['/etc/mount', '/etc/disks', '/etc/filesystems', '/etc/fstab'],
        correctIndex: 3,
        explanation: '/etc/fstab definierar vilka filsystem som monteras automatiskt vid boot.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-11',
        question: 'Kommandot umount används för att...',
        options: ['Montera disk', 'Radera partition', 'Avmontera filsystem', 'Formatera disk'],
        correctIndex: 2,
        explanation: 'umount avmonterar ett filsystem från sin mount point.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-12',
        question: 'Vad betyder ext4?',
        options: ['Extra 4 partitioner', 'Extended partition 4', 'Fourth Extended Filesystem', 'External disk 4'],
        correctIndex: 2,
        explanation: 'ext4 = Fourth Extended Filesystem, standard Linux-filsystem.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-13',
        question: 'Kommandot cryptsetup används för att...',
        options: ['Skapa användare', 'Sätta lösenord', 'Skapa partitioner', 'Hantera LUKS-kryptering'],
        correctIndex: 3,
        explanation: 'cryptsetup hanterar LUKS-volymer: luksFormat, luksOpen, luksClose.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'omtenta-storage-14',
        question: 'Vad gör df -h?',
        options: ['Visar dolda diskar', 'Visar hjälp', 'Visar diskutrymme i human-readable format', 'Visar historik'],
        correctIndex: 2,
        explanation: '-h = human-readable, visar GB/MB istället för bytes.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-15',
        question: 'Var monteras filsystem vanligen?',
        options: ['/home', '/etc', '/var', '/mnt eller /media'],
        correctIndex: 3,
        explanation: '/mnt för manuella mounts, /media för automatiska (USB, etc.).',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-16',
        question: 'Kommandot parted är ett alternativ till...',
        options: ['mount', 'mkfs', 'df', 'fdisk'],
        correctIndex: 3,
        explanation: 'parted är ett modernare partitionsverktyg, stöder GPT.',
        difficulty: 'G',
        category: 'Partitioner'
    },
    {
        id: 'omtenta-storage-17',
        question: 'Vad är en swap partition?',
        options: ['Temporär lagring', 'Backup-partition', 'Virtuellt minne på disk', 'Boot-partition'],
        correctIndex: 2,
        explanation: 'Swap används som virtuellt minne när RAM är fullt.',
        difficulty: 'G',
        category: 'Swap'
    },
    {
        id: 'omtenta-storage-18',
        question: 'Kommandot blkid visar...',
        options: ['Block size', 'Blockerade användare', 'Block device identifierare (UUID)', 'Blockerad trafik'],
        correctIndex: 2,
        explanation: 'blkid visar UUID, filsystemtyp och label för block devices.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-19',
        question: 'Vad är UUID?',
        options: ['User Unique ID', 'Unix User ID', 'Universally Unique Identifier', 'Unified Unit ID'],
        correctIndex: 2,
        explanation: 'UUID är en unik identifierare för partitioner, ändras inte vid omstart.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'omtenta-storage-20',
        question: 'I fstab, vad anger mount point?',
        options: ['Första kolumnen', 'Tredje kolumnen', 'Andra kolumnen', 'Fjärde kolumnen'],
        correctIndex: 2,
        explanation: 'Format: device mount-point fs-type options dump pass',
        difficulty: 'VG',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-21',
        question: 'Kommandot tune2fs används för att...',
        options: ['Spela musik', 'Tuning av CPU', 'Testa nätverk', 'Justera ext-filsystem parametrar'],
        correctIndex: 3,
        explanation: 'tune2fs kan ändra filsystem-label, reserverat utrymme, etc.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-22',
        question: 'Vad gör flaggan -a med mount?',
        options: ['Monterar alla användare', 'Avmonterar allt', 'Visar alla diskar', 'Monterar allt i fstab'],
        correctIndex: 3,
        explanation: 'mount -a monterar alla filsystem definierade i /etc/fstab.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-23',
        question: 'LVM står för...',
        options: ['Linux Virtual Memory', 'Linux Volume Mount', 'Logical Volume Manager', 'Local Virtual Machine'],
        correctIndex: 2,
        explanation: 'LVM gör det möjligt att hantera lagring flexibelt med volymer.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'omtenta-storage-24',
        question: 'Kommandot resize2fs används för att...',
        options: ['Ändra storlek på filer', 'Ändra storlek på partitioner', 'Ändra storlek på images', 'Ändra storlek på ext-filsystem'],
        correctIndex: 3,
        explanation: 'resize2fs ändrar storlek på ext2/ext3/ext4-filsystem.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-25',
        question: 'Vad är 3-2-1 regeln för backup?',
        options: ['3 användare, 2 lösenord, 1 server', '3 diskar, 2 partitioner, 1 filsystem', '3 kopior, 2 mediatyper, 1 off-site', '3 dagar, 2 timmar, 1 minut'],
        correctIndex: 2,
        explanation: '3 kopior av data, lagrat på 2 olika mediatyper, 1 kopia off-site.',
        difficulty: 'G',
        category: 'Backup'
    },
    {
        id: 'omtenta-storage-26',
        question: 'Kommandot fsck används för att...',
        options: ['Formatera disk', 'Skapa filsystem', 'Montera filsystem', 'Kontrollera och reparera filsystem'],
        correctIndex: 3,
        explanation: 'fsck = filesystem check, reparerar korrupta filsystem.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-27',
        question: 'Vad gör dd kommandot?',
        options: ['Tar bort data', 'Visar diskinfo', 'Defragmenterar disk', 'Kopierar och konverterar data på låg nivå'],
        correctIndex: 3,
        explanation: 'dd kan klona diskar, skapa images, konvertera data.',
        difficulty: 'VG',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-28',
        question: 'Vilken flagga i du visar totalen?',
        options: ['-t', '-a', '-c', '-s'],
        correctIndex: 3,
        explanation: 'du -s visar bara summan, inte varje fil/mapp.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-29',
        question: 'Vad är RAID?',
        options: ['Rapid Access ID', 'Random Access Internal Drive', 'Read And Install Data', 'Redundant Array of Independent Disks'],
        correctIndex: 3,
        explanation: 'RAID kombinerar flera diskar för redundans och/eller prestanda.',
        difficulty: 'VG',
        category: 'RAID'
    },
    {
        id: 'omtenta-storage-30',
        question: 'Kommandot mkswap skapar...',
        options: ['Ny mapp', 'Ny användare', 'Ny disk', 'Swap-partition'],
        correctIndex: 3,
        explanation: 'mkswap formaterar en partition för swap.',
        difficulty: 'G',
        category: 'Swap'
    },
    {
        id: 'omtenta-storage-31',
        question: 'Vad gör swapon?',
        options: ['Stänger av swap', 'Skapar swap', 'Visar swap', 'Aktiverar swap'],
        correctIndex: 3,
        explanation: 'swapon aktiverar swap. swapoff stänger av den.',
        difficulty: 'G',
        category: 'Swap'
    },
    {
        id: 'omtenta-storage-32',
        question: 'I fstab, vad anger filsystemtyp?',
        options: ['Första kolumnen', 'Andra kolumnen', 'Fjärde kolumnen', 'Tredje kolumnen'],
        correctIndex: 3,
        explanation: 'Kolumn 3 anger typ: ext4, xfs, swap, nfs, etc.',
        difficulty: 'VG',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-33',
        question: 'Kommandot findmnt visar...',
        options: ['Hittade filer', 'Sökvägar', 'Användare', 'Monterade filsystem'],
        correctIndex: 3,
        explanation: 'findmnt visar monterade filsystem i trädformat.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-34',
        question: 'Vad gör option "noauto" i fstab?',
        options: ['Ingen automatisk formatering', 'Ingen åtkomst', 'Ingen loggning', 'Monteras inte automatiskt vid boot'],
        correctIndex: 3,
        explanation: 'noauto betyder att du måste montera manuellt.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-35',
        question: 'Kommandot lvcreate används med...',
        options: ['LUKS', 'RAID', 'ext4', 'LVM'],
        correctIndex: 3,
        explanation: 'lvcreate skapar logical volumes i LVM.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'omtenta-storage-36',
        question: 'Vad är en physical volume (PV)?',
        options: ['Virtuell disk', 'Nätverksdisk', 'RAM-disk', 'Underliggande disk/partition i LVM'],
        correctIndex: 3,
        explanation: 'PV är basen i LVM - en disk eller partition som används av LVM.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'omtenta-storage-37',
        question: 'Kommandot vgcreate skapar...',
        options: ['Virtual Guest', 'Virtual Graphics', 'Volume Generator', 'Volume Group'],
        correctIndex: 3,
        explanation: 'vgcreate skapar en volume group från physical volumes.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'omtenta-storage-38',
        question: 'Vad är mount point?',
        options: ['Diskens fysiska plats', 'Partitionens början', 'Filsystemets rot', 'Katalog där filsystem blir tillgängligt'],
        correctIndex: 3,
        explanation: 'Mount point är katalogen där filsystemet "kopplas in".',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-39',
        question: 'Flaggan -T i df visar...',
        options: ['Total', 'Tid', 'Temperatur', 'Filsystemtyp'],
        correctIndex: 3,
        explanation: 'df -T visar vilken typ varje filsystem har.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-40',
        question: 'Vad gör option "defaults" i fstab?',
        options: ['Inga options', 'Bara default användare', 'Default filsystem', 'Standard mount options (rw, suid, dev, exec, auto, nouser, async)'],
        correctIndex: 3,
        explanation: 'defaults = rw,suid,dev,exec,auto,nouser,async.',
        difficulty: 'VG',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-41',
        question: 'Kommandot e2label sätter...',
        options: ['Email', 'Error label', 'Extended label', 'Label på ext-filsystem'],
        correctIndex: 3,
        explanation: 'e2label /dev/sda1 MYDATA sätter label på ext-partition.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-42',
        question: 'Vad är inode?',
        options: ['Internet node', 'Input node', 'Internal node', 'Index node (metadata om fil)'],
        correctIndex: 3,
        explanation: 'Inode innehåller metadata: permissions, ägare, timestamps, etc.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-43',
        question: 'Kommandot stat visar...',
        options: ['Statistik om system', 'Status på nätverk', 'Startinfo', 'Detaljerad filinformation inkl inode'],
        correctIndex: 3,
        explanation: 'stat visar inode, storlek, timestamps, permissions, etc.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    },
    {
        id: 'omtenta-storage-44',
        question: 'Vad gör option "ro" i fstab?',
        options: ['Root only', 'Remote only', 'Run once', 'Read only'],
        correctIndex: 3,
        explanation: 'ro = read only, förhindrar skrivning.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'omtenta-storage-45',
        question: 'Kommandot pvdisplay visar...',
        options: ['Process view', 'Partition view', 'Permission view', 'Physical volume info (LVM)'],
        correctIndex: 3,
        explanation: 'pvdisplay visar detaljer om physical volumes i LVM.',
        difficulty: 'VG',
        category: 'LVM'
    },
    {
        id: 'omtenta-storage-46',
        question: 'Vad gör xfs_repair?',
        options: ['Reparerar ext4', 'Reparerar nätverk', 'Reparerar LUKS', 'Reparerar XFS-filsystem'],
        correctIndex: 3,
        explanation: 'xfs_repair är fsck-motsvarigheten för XFS.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-47',
        question: 'Vad är journaling i ett filsystem?',
        options: ['Loggning av användare', 'Dagbok-funktion', 'Backup-funktion', 'Loggning av ändringar för recovery'],
        correctIndex: 3,
        explanation: 'Journal loggar ändringar så filsystemet kan återställas vid krasch.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'omtenta-storage-48',
        question: 'Kommandot cryptsetup luksFormat...',
        options: ['Visar LUKS-format', 'Formaterar vanligt', 'Listar format', 'Initierar LUKS-kryptering på partition'],
        correctIndex: 3,
        explanation: 'luksFormat skapar LUKS-header och sätter lösenord.',
        difficulty: 'VG',
        category: 'LUKS'
    },
    {
        id: 'omtenta-storage-49',
        question: 'Vad gör cryptsetup luksOpen?',
        options: ['Öppnar fil', 'Öppnar terminal', 'Skapar lösenord', 'Öppnar/dekrypterar LUKS-volym'],
        correctIndex: 3,
        explanation: 'luksOpen dekrypterar och gör volymen tillgänglig under /dev/mapper/.',
        difficulty: 'VG',
        category: 'LUKS'
    },
    {
        id: 'omtenta-storage-50',
        question: 'Vilken flagga i du exkluderar mönster från räkning?',
        options: ['--exkluderar användare', '--exkluderar errors', '--exkluderar dolda', '--exclude'],
        correctIndex: 3,
        explanation: 'du --exclude="*.log" exkluderar loggfiler från räkningen.',
        difficulty: 'G',
        category: 'Disk Kommandon'
    }
]

// ============================================================================
// DOCKER & CONTAINERS (50 frågor)
// ============================================================================

export const DOCKER_QUESTIONS: OmtentaQuestion[] = [
    {
        id: 'omtenta-docker-1',
        question: 'En Docker container är...',
        options: ['En virtuell maskin', 'Ett skript', 'En databas', 'En isolerad process'],
        correctIndex: 3,
        explanation: 'En container är en isolerad process, INTE en VM.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'omtenta-docker-2',
        question: 'Vilka två typer av volymer finns i Docker?',
        options: ['Local och remote volumes', 'Private och public volumes', 'File och folder volumes', 'Bind volumes och named volumes'],
        correctIndex: 3,
        explanation: 'Bind mounts mappar host-katalog, named volumes hanteras av Docker.',
        difficulty: 'G',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-3',
        question: 'Kan hosten komma åt en containers localhost?',
        options: ['Nej (False)', 'Bara med root', 'Bara på Linux', 'Ja (True)'],
        correctIndex: 3,
        explanation: 'Hosten kan komma åt containerns nätverk via port mapping.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'omtenta-docker-4',
        question: 'Kan en container komma åt hostens localhost?',
        options: ['Ja (True)', 'Bara med root', 'Bara på Linux', 'Nej (False)'],
        correctIndex: 3,
        explanation: 'Containern har sitt eget nätverk och kan inte nå hostens localhost direkt.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'omtenta-docker-5',
        question: 'Kommandot för att lista körande containers är...',
        options: ['docker list', 'docker show', 'docker running', 'docker ps'],
        correctIndex: 3,
        explanation: 'docker ps listar körande containers. docker ps -a visar alla.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-6',
        question: 'Vad gör docker pull?',
        options: ['Stoppar en container', 'Skapar en container', 'Tar bort en container', 'Laddar ner en image'],
        correctIndex: 3,
        explanation: 'docker pull hämtar en image från Docker Hub eller annat registry.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-7',
        question: 'En Docker image är...',
        options: ['En körande process', 'Ett nätverk', 'En volym', 'En mall för att skapa containers'],
        correctIndex: 3,
        explanation: 'Image är read-only mall. Container är körande instans av image.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-8',
        question: 'Kommandot för att starta en container är...',
        options: ['docker start', 'docker begin', 'docker launch', 'docker run'],
        correctIndex: 3,
        explanation: 'docker run skapar och startar en ny container från en image.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-9',
        question: 'Vad gör flaggan -d i docker run?',
        options: ['Debug mode', 'Delete efter stop', 'Default settings', 'Detached (kör i bakgrunden)'],
        correctIndex: 3,
        explanation: '-d = detached mode, containern körs i bakgrunden.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-10',
        question: 'Vilken flagga mappar portar i docker run?',
        options: ['-m', '-port', '-n', '-p'],
        correctIndex: 3,
        explanation: '-p 8080:80 mappar host-port 8080 till container-port 80.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'omtenta-docker-11',
        question: 'Vad gör docker stop?',
        options: ['Raderar containern', 'Pausar containern', 'Startar om', 'Stoppar en körande container'],
        correctIndex: 3,
        explanation: 'docker stop skickar SIGTERM, väntar, sedan SIGKILL.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-12',
        question: 'Kommandot för att ta bort en container är...',
        options: ['docker delete', 'docker remove', 'docker destroy', 'docker rm'],
        correctIndex: 3,
        explanation: 'docker rm tar bort en stoppad container.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-13',
        question: 'Vad gör docker exec?',
        options: ['Startar ny container', 'Avslutar container', 'Exporterar container', 'Kör kommando i körande container'],
        correctIndex: 3,
        explanation: 'docker exec -it container bash ger dig ett shell inuti containern.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-14',
        question: 'Vilken fil definierar hur en image byggs?',
        options: ['docker.conf', 'container.yaml', 'image.json', 'Dockerfile'],
        correctIndex: 3,
        explanation: 'Dockerfile innehåller instruktioner för att bygga en image.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-15',
        question: 'Vad gör docker build?',
        options: ['Startar container', 'Installerar Docker', 'Konfigurerar nätverk', 'Bygger en image från Dockerfile'],
        correctIndex: 3,
        explanation: 'docker build -t myimage . bygger image från Dockerfile i nuvarande mapp.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-16',
        question: 'Kommandot för att lista alla images är...',
        options: ['docker images list', 'docker list images', 'docker show images', 'docker images'],
        correctIndex: 3,
        explanation: 'docker images visar alla lokala images.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-17',
        question: 'Vad gör docker logs?',
        options: ['Installerar loggning', 'Skapar loggfil', 'Aktiverar debug', 'Visar container-loggar'],
        correctIndex: 3,
        explanation: 'docker logs container visar stdout/stderr från containern.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-18',
        question: 'Vilken flagga gör att containern tas bort efter stopp?',
        options: ['-d', '-p', '-v', '--rm'],
        correctIndex: 3,
        explanation: '--rm rensar upp containern automatiskt när den stoppas.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-19',
        question: 'Vad är Docker Hub?',
        options: ['Lokal fillagring', 'Container-orkestrerare', 'Loggsystem', 'Registrering för Docker images'],
        correctIndex: 3,
        explanation: 'Docker Hub är det officiella public registry för images.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-20',
        question: 'Kommandot för att visa alla containers (även stoppade) är...',
        options: ['docker ps', 'docker ps -s', 'docker ps --stopped', 'docker ps -a'],
        correctIndex: 3,
        explanation: '-a = all, visar även stoppade containers.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-21',
        question: 'Vad gör docker push?',
        options: ['Startar container', 'Kopierar filer', 'Tar bort image', 'Laddar upp image till registry'],
        correctIndex: 3,
        explanation: 'docker push myrepo/myimage:tag laddar upp till registry.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-22',
        question: 'Vilken flagga ger containern ett namn?',
        options: ['-n', '-l', '-id', '--name'],
        correctIndex: 3,
        explanation: '--name mycontainer ger containern ett läsbart namn.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-23',
        question: 'Vad är skillnaden mellan container och image?',
        options: ['Ingen skillnad', 'Container är mall, image är instans', 'Image är större', 'Image är mall, container är körande instans'],
        correctIndex: 3,
        explanation: 'Image är statisk mall, container är live process baserad på image.',
        difficulty: 'G',
        category: 'Docker Grundläggande'
    },
    {
        id: 'omtenta-docker-24',
        question: 'Kommandot för att gå in i en körande container är ofta...',
        options: ['docker enter', 'docker login', 'docker connect', 'docker exec -it container /bin/bash'],
        correctIndex: 3,
        explanation: '-i = interactive, -t = tty (terminal).',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-25',
        question: 'Vad gör flaggan -v i docker run?',
        options: ['Verbose mode', 'Version', 'Virtualisering', 'Monterar volym'],
        correctIndex: 3,
        explanation: '-v /host/path:/container/path monterar en volym.',
        difficulty: 'G',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-26',
        question: 'Vilken flagga kör container interaktivt med terminal?',
        options: ['-d', '-p', '-r', '-it'],
        correctIndex: 3,
        explanation: '-i = interactive (stdin open), -t = pseudo-tty.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-27',
        question: 'Kommandot för att ta bort en image är...',
        options: ['docker rm', 'docker delete image', 'docker remove image', 'docker rmi'],
        correctIndex: 3,
        explanation: 'docker rmi = remove image.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-28',
        question: 'Vad gör docker inspect?',
        options: ['Skapar container', 'Testar container', 'Reparerar container', 'Visar detaljerad info om container/image'],
        correctIndex: 3,
        explanation: 'docker inspect ger JSON med all metadata.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-29',
        question: 'En bind mount mappar...',
        options: ['Containers till varandra', 'Nätverk till container', 'Images till containers', 'Host-katalog till container'],
        correctIndex: 3,
        explanation: 'Bind mount länkar en specifik katalog från hosten in i containern.',
        difficulty: 'G',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-30',
        question: 'Vad gör docker network ls?',
        options: ['Skapar nätverk', 'Ansluter nätverk', 'Tar bort nätverk', 'Listar Docker-nätverk'],
        correctIndex: 3,
        explanation: 'docker network ls visar alla Docker-nätverk.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'omtenta-docker-31',
        question: 'Kommandot för att starta en stoppad container är...',
        options: ['docker run', 'docker resume', 'docker continue', 'docker start'],
        correctIndex: 3,
        explanation: 'docker start startar en existerande stoppad container.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-32',
        question: 'Vad händer med data i container som saknar volym vid restart?',
        options: ['Data sparas', 'Data kopieras till host', 'Data komprimeras', 'Data förloras'],
        correctIndex: 3,
        explanation: 'Container-filsystemet är ephemeral - data försvinner utan volymer.',
        difficulty: 'G',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-33',
        question: 'Vilken port exponerar Docker som standard för HTTP?',
        options: ['22', '443', '8080', '80'],
        correctIndex: 3,
        explanation: 'HTTP använder port 80, HTTPS port 443.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'omtenta-docker-34',
        question: 'Vad gör docker-compose up?',
        options: ['Uppdaterar Docker', 'Uppgraderar image', 'Laddar upp logs', 'Startar tjänster definierade i compose-fil'],
        correctIndex: 3,
        explanation: 'docker-compose up startar alla services i docker-compose.yml.',
        difficulty: 'G',
        category: 'Docker Compose'
    },
    {
        id: 'omtenta-docker-35',
        question: 'Vilken fil används av docker-compose?',
        options: ['compose.conf', 'docker.yaml', 'compose.json', 'docker-compose.yml'],
        correctIndex: 3,
        explanation: 'docker-compose.yml (eller docker-compose.yaml) definierar multi-container apps.',
        difficulty: 'G',
        category: 'Docker Compose'
    },
    {
        id: 'omtenta-docker-36',
        question: 'Kommandot för att se resuranvändning av containers är...',
        options: ['docker usage', 'docker resources', 'docker top', 'docker stats'],
        correctIndex: 3,
        explanation: 'docker stats visar CPU, minne, nätverk i realtid.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-37',
        question: 'Vad gör docker tag?',
        options: ['Märker container', 'Skapar tagg-fil', 'Sorterar images', 'Ger image ett nytt namn/tag'],
        correctIndex: 3,
        explanation: 'docker tag oldname:tag newname:newtag skapar en ny referens.',
        difficulty: 'G',
        category: 'Docker Images'
    },
    {
        id: 'omtenta-docker-38',
        question: 'En named volume lagras var?',
        options: ['I containern', 'I host-hemkatalogen', 'I /tmp', 'Hanteras av Docker i /var/lib/docker'],
        correctIndex: 3,
        explanation: 'Named volumes lagras i /var/lib/docker/volumes/.',
        difficulty: 'VG',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-39',
        question: 'Vad gör EXPOSE i Dockerfile?',
        options: ['Öppnar port på host', 'Kräver lösenord', 'Tar bort port', 'Dokumenterar vilken port containern lyssnar på'],
        correctIndex: 3,
        explanation: 'EXPOSE är dokumentation, öppnar inte port på host.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-40',
        question: 'Kommandot docker cp används för att...',
        options: ['Kopiera containers', 'Kopiera images', 'Kopiera nätverk', 'Kopiera filer mellan host och container'],
        correctIndex: 3,
        explanation: 'docker cp fil container:/path kopierar fil till container.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-41',
        question: 'Vad gör CMD i Dockerfile?',
        options: ['Kommenterar', 'Skapar mapp', 'Installerar paket', 'Anger standardkommando vid container-start'],
        correctIndex: 3,
        explanation: 'CMD körs när containern startar (kan överskrivas).',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-42',
        question: 'Vilken instruktion i Dockerfile anger basimage?',
        options: ['BASE', 'IMAGE', 'SOURCE', 'FROM'],
        correctIndex: 3,
        explanation: 'FROM ubuntu:22.04 anger basimage för bygget.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-43',
        question: 'Vad gör RUN i Dockerfile?',
        options: ['Startar container', 'Kör container', 'Testar image', 'Kör kommando vid image-byggning'],
        correctIndex: 3,
        explanation: 'RUN apt-get install -y nginx körs under docker build.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-44',
        question: 'Kommandot för att se processerna i en container är...',
        options: ['docker ps', 'docker processes', 'docker proc', 'docker top'],
        correctIndex: 3,
        explanation: 'docker top container visar processer inuti containern.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-45',
        question: 'Vad gör docker pause?',
        options: ['Stoppar container permanent', 'Väntar på input', 'Tar backup', 'Pausar containerns processer'],
        correctIndex: 3,
        explanation: 'docker pause fryser processerna, docker unpause återupptar.',
        difficulty: 'G',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-46',
        question: 'WORKDIR i Dockerfile sätter...',
        options: ['Volym-sökväg', 'Host-katalog', 'Logg-katalog', 'Arbetskatalog i containern'],
        correctIndex: 3,
        explanation: 'WORKDIR /app gör att efterföljande kommandon körs i /app.',
        difficulty: 'VG',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-47',
        question: 'Vad gör docker volume create?',
        options: ['Skapar bind mount', 'Skapar container', 'Skapar network', 'Skapar named volume'],
        correctIndex: 3,
        explanation: 'docker volume create myvolume skapar en named volume.',
        difficulty: 'G',
        category: 'Docker Volymer'
    },
    {
        id: 'omtenta-docker-48',
        question: 'Skillnaden mellan docker stop och docker kill är...',
        options: ['Ingen skillnad', 'stop tar bort, kill pausar', 'kill är säkrare', 'stop är graceful, kill är omedelbart'],
        correctIndex: 3,
        explanation: 'stop skickar SIGTERM och väntar, kill skickar SIGKILL direkt.',
        difficulty: 'VG',
        category: 'Docker Kommandon'
    },
    {
        id: 'omtenta-docker-49',
        question: 'Vad gör COPY i Dockerfile?',
        options: ['Kopierar containers', 'Kopierar nätverk', 'Kopierar volymer', 'Kopierar filer från host till image'],
        correctIndex: 3,
        explanation: 'COPY ./app /app kopierar från build context till image.',
        difficulty: 'G',
        category: 'Dockerfile'
    },
    {
        id: 'omtenta-docker-50',
        question: 'Kommandot för att visa volym-information är...',
        options: ['docker volume show', 'docker volume info', 'docker volume ls -l', 'docker volume inspect'],
        correctIndex: 3,
        explanation: 'docker volume inspect myvolume visar detaljer om volymen.',
        difficulty: 'G',
        category: 'Docker Volymer'
    }
]

export const STORAGE_DOCKER_STATS = {
    storageQuestions: STORAGE_QUESTIONS.length,
    dockerQuestions: DOCKER_QUESTIONS.length,
    totalQuestions: STORAGE_QUESTIONS.length + DOCKER_QUESTIONS.length,
    gQuestions: [...STORAGE_QUESTIONS, ...DOCKER_QUESTIONS].filter(q => q.difficulty === 'G').length,
    vgQuestions: [...STORAGE_QUESTIONS, ...DOCKER_QUESTIONS].filter(q => q.difficulty === 'VG').length
}
