import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

export const BLOCKSTORAGE_KRYPTERING_V2_QUESTIONS: OmtentaV2Question[] = [
  {
    id: 'omtenta-v2-storage-1',
    question: 'The command to check disk space is...',
    options: ['space', 'disk', 'df', 'du'],
    correctIndices: [2],
    explanation: 'df (disk free) visar hur mycket diskutrymme som används och finns tillgängligt på monterade filsystem.',
    difficulty: 'G',
    category: 'Disk Management',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-2',
    question: 'The command to check file/directory sizes is...',
    options: ['df', 'size', 'du', 'space'],
    correctIndices: [2],
    explanation: 'du (disk usage) visar storleken på filer och kataloger.',
    difficulty: 'G',
    category: 'Disk Management',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-3',
    question: 'The command to list block devices is...',
    options: ['blocks', 'disks', 'lsblk', 'listblk'],
    correctIndices: [2],
    explanation: 'lsblk (list block devices) visar information om alla blockenheter i systemet.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-4',
    question: 'In Linux, everything is...',
    options: ['A process', 'A command', 'A file', 'A directory'],
    correctIndices: [2],
    explanation: 'I Linux behandlas allt som filer - enheter, processer, nätverksanslutningar etc.',
    difficulty: 'G',
    category: 'Linux Fundamentals',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-5',
    question: 'Correct order for encrypted filesystem on new storage?',
    options: [
      'Filesystem → LUKS → Partition',
      'LUKS → Filesystem → Partition',
      'Partition → LUKS → Filesystem',
      'Filesystem → Partition → LUKS'
    ],
    correctIndices: [2],
    explanation: 'Rätt ordning är: Skapa partition först, sedan kryptera med LUKS, och sist skapa filsystem på den krypterade volymen.',
    difficulty: 'VG',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-6',
    question: 'LUKS stands for...',
    options: [
      'Linux User Key System',
      'Linux Unified Key Setup',
      'Logical Unix Key Setup',
      'Linux Utility Key Service'
    ],
    correctIndices: [1],
    explanation: 'LUKS = Linux Unified Key Setup, standardkryptering för Linux-diskar.',
    difficulty: 'G',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-7',
    question: 'The command to create partition is...',
    options: ['mkpart', 'partition', 'fdisk', 'newpart'],
    correctIndices: [2],
    explanation: 'fdisk är det klassiska verktyget för att skapa och hantera partitioner.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-8',
    question: 'Another partition tool is...',
    options: ['mkdisk', 'diskpart', 'parted', 'partmaker'],
    correctIndices: [2],
    explanation: 'parted är ett annat partitionsverktyg som stöder både MBR och GPT.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-9',
    question: 'The command to create filesystem is...',
    options: ['newfs', 'createfs', 'mkfs', 'makefs'],
    correctIndices: [2],
    explanation: 'mkfs (make filesystem) används för att skapa filsystem på partitioner.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-10',
    question: 'To create ext4 filesystem, use...',
    options: ['mkfs -ext4', 'mkfs.ext4', 'mkext4', 'ext4fs'],
    correctIndices: [1],
    explanation: 'mkfs.ext4 skapar ett ext4-filsystem på en partition.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-11',
    question: 'The command to mount filesystem is...',
    options: ['attach', 'connect', 'mount', 'link'],
    correctIndices: [2],
    explanation: 'mount kopplar ett filsystem till en plats i katalogträdet.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-12',
    question: 'The command to unmount is...',
    options: ['unmount', 'umount', 'dismount', 'detach'],
    correctIndices: [1],
    explanation: 'umount (utan n) är kommandot för att avmontera filsystem.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-13',
    question: 'Mount configuration file is...',
    options: ['/etc/mount.conf', '/etc/mounts', '/etc/fstab', '/etc/filesystems'],
    correctIndices: [2],
    explanation: '/etc/fstab innehåller konfiguration för vilka filsystem som ska monteras vid uppstart.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-14',
    question: 'The df flag -h shows...',
    options: ['Help', 'Human readable', 'Hidden', 'Header'],
    correctIndices: [1],
    explanation: '-h gör att df visar storlekar i läsbart format (KB, MB, GB).',
    difficulty: 'G',
    category: 'Disk Management',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-15',
    question: 'The du flag -s shows...',
    options: ['Size', 'Summary', 'Sort', 'System'],
    correctIndices: [1],
    explanation: '-s (summary) visar endast totalsumman istället för varje fil.',
    difficulty: 'G',
    category: 'Disk Management',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-16',
    question: 'The du flag -h shows...',
    options: ['Help', 'Human readable', 'Hidden', 'Header'],
    correctIndices: [1],
    explanation: '-h gör att du visar storlekar i läsbart format.',
    difficulty: 'G',
    category: 'Disk Management',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-17',
    question: 'To show UUID of devices, use...',
    options: ['uuid', 'showid', 'blkid', 'lsid'],
    correctIndices: [2],
    explanation: 'blkid visar UUID och annan information om blockenheter.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-18',
    question: 'UUID stands for...',
    options: [
      'Unique User ID',
      'Universally Unique Identifier',
      'Unix Unique ID',
      'Uniform User ID'
    ],
    correctIndices: [1],
    explanation: 'UUID = Universally Unique Identifier, en unik identifierare för enheter.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-19',
    question: 'Why use UUID in fstab?',
    options: [
      "It's shorter",
      "It's faster",
      'Device names can change',
      "It's required"
    ],
    correctIndices: [2],
    explanation: 'Enhetsnamn som /dev/sda kan ändras mellan omstarter, UUID är alltid samma.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-20',
    question: 'Select all that are filesystems (choose 4):',
    options: [
      'ext4',
      'fdisk',
      'XFS',
      'lvm',
      'btrfs',
      'raid',
      'NTFS',
      'mount',
      'fstab',
      'partition'
    ],
    correctIndices: [0, 2, 4, 6],
    explanation: 'ext4, XFS, btrfs och NTFS är filsystem. fdisk och parted är partitionsverktyg, LVM är volymhantering, RAID är diskredundans.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-21',
    question: 'ext4 stands for...',
    options: [
      'External 4',
      'Extended Filesystem 4',
      'Extra Filesystem 4',
      'Extension 4'
    ],
    correctIndices: [1],
    explanation: 'ext4 = Extended Filesystem 4, fjärde generationens extended filesystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-22',
    question: 'Default filesystem on RHEL is...',
    options: ['ext4', 'XFS', 'btrfs', 'NTFS'],
    correctIndices: [1],
    explanation: 'XFS är standardfilsystemet på Red Hat Enterprise Linux.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-23',
    question: 'Default filesystem on Ubuntu is...',
    options: ['XFS', 'ext4', 'btrfs', 'NTFS'],
    correctIndices: [1],
    explanation: 'ext4 är standardfilsystemet på Ubuntu.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-24',
    question: 'The command to check filesystem is...',
    options: ['checkfs', 'diskcheck', 'fsck', 'verify'],
    correctIndices: [2],
    explanation: 'fsck (filesystem check) kontrollerar och reparerar filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-25',
    question: 'fsck should be run when filesystem is...',
    options: ['Mounted', 'Unmounted', 'In use', 'Full'],
    correctIndices: [1],
    explanation: 'fsck ska köras på avmonterade filsystem för att undvika korruption.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-26',
    question: 'Journaling in filesystem means...',
    options: [
      'Logging user actions',
      'Recording changes for recovery',
      'Keeping file history',
      'Backup automation'
    ],
    correctIndices: [1],
    explanation: 'Journaling loggar ändringar innan de skrivs för att möjliggöra återhämtning vid krasch.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-27',
    question: 'An inode contains...',
    options: ['File content', 'File metadata', 'Directory list', 'User list'],
    correctIndices: [1],
    explanation: 'En inode innehåller metadata om filen: rättigheter, ägare, tidsstämplar, pekare till data.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-28',
    question: 'Inode does NOT contain...',
    options: ['Permissions', 'Timestamps', 'Filename', 'Owner'],
    correctIndices: [2],
    explanation: 'Filnamnet lagras i katalogen, inte i inoden. Inoden innehåller allt annat metadata.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-29',
    question: 'LVM stands for...',
    options: [
      'Linux Virtual Memory',
      'Logical Volume Manager',
      'Logical Virtual Machine',
      'Linux Volume Mount'
    ],
    correctIndices: [1],
    explanation: 'LVM = Logical Volume Manager, för flexibel volymhantering.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-30',
    question: 'LVM hierarchy is PV → VG → ...',
    options: ['LV', 'PE', 'FS', 'DISK'],
    correctIndices: [0],
    explanation: 'LVM-hierarkin är: Physical Volume → Volume Group → Logical Volume.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-31',
    question: 'PV stands for...',
    options: [
      'Primary Volume',
      'Physical Volume',
      'Partition Volume',
      'Private Volume'
    ],
    correctIndices: [1],
    explanation: 'PV = Physical Volume, den fysiska disken eller partitionen i LVM.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-32',
    question: 'VG stands for...',
    options: [
      'Virtual Group',
      'Volume Group',
      'Verified Group',
      'Variable Group'
    ],
    correctIndices: [1],
    explanation: 'VG = Volume Group, en pool av lagringsutrymme från en eller flera PV.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-33',
    question: 'LV stands for...',
    options: [
      'Linux Volume',
      'Logical Volume',
      'Local Volume',
      'Large Volume'
    ],
    correctIndices: [1],
    explanation: 'LV = Logical Volume, den volym som skapas från en VG och kan formateras.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-34',
    question: 'To create Physical Volume, use...',
    options: ['pvnew', 'pvmake', 'pvcreate', 'newpv'],
    correctIndices: [2],
    explanation: 'pvcreate initialiserar en disk eller partition som Physical Volume.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-35',
    question: 'To create Volume Group, use...',
    options: ['vgnew', 'vgmake', 'vgcreate', 'newvg'],
    correctIndices: [2],
    explanation: 'vgcreate skapar en Volume Group från en eller flera PV.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-36',
    question: 'To create Logical Volume, use...',
    options: ['lvnew', 'lvmake', 'lvcreate', 'newlv'],
    correctIndices: [2],
    explanation: 'lvcreate skapar en Logical Volume från en VG.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-37',
    question: 'To show Physical Volumes, use...',
    options: ['pvshow', 'pvdisplay', 'pvlist', 'listpv'],
    correctIndices: [1],
    explanation: 'pvdisplay visar detaljerad information om Physical Volumes.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-38',
    question: 'To show Volume Groups, use...',
    options: ['vgshow', 'vgdisplay', 'vglist', 'listvg'],
    correctIndices: [1],
    explanation: 'vgdisplay visar detaljerad information om Volume Groups.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-39',
    question: 'To show Logical Volumes, use...',
    options: ['lvshow', 'lvdisplay', 'lvlist', 'listlv'],
    correctIndices: [1],
    explanation: 'lvdisplay visar detaljerad information om Logical Volumes.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-40',
    question: 'Select all LVM commands (choose 5):',
    options: [
      'pvcreate',
      'pvmake',
      'vgcreate',
      'vgmake',
      'lvcreate',
      'lvmake',
      'pvdisplay',
      'pvshow',
      'lvextend',
      'lvgrow'
    ],
    correctIndices: [0, 2, 4, 6, 8],
    explanation: 'pvcreate, vgcreate, lvcreate, pvdisplay och lvextend är alla giltiga LVM-kommandon.',
    difficulty: 'VG',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-41',
    question: 'To extend Logical Volume, use...',
    options: ['lvgrow', 'lvadd', 'lvextend', 'lvincrease'],
    correctIndices: [2],
    explanation: 'lvextend ökar storleken på en Logical Volume.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-42',
    question: 'To reduce Logical Volume, use...',
    options: ['lvshrink', 'lvremove', 'lvreduce', 'lvdecrease'],
    correctIndices: [2],
    explanation: 'lvreduce minskar storleken på en Logical Volume.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-43',
    question: 'After lvextend, you must also...',
    options: ['Reboot', 'Remount', 'Resize filesystem', 'Nothing'],
    correctIndices: [2],
    explanation: 'Efter lvextend måste filsystemet också utökas med resize2fs eller xfs_growfs.',
    difficulty: 'VG',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-44',
    question: 'To extend filesystem, use...',
    options: ['fsextend', 'growfs', 'resize2fs', 'extendfs'],
    correctIndices: [2],
    explanation: 'resize2fs utökar ext-filsystem efter att volymen har utökats.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-45',
    question: 'LV path format is...',
    options: ['/lvm/vg/lv', '/dev/vg/lv', '/dev/lvm/vg/lv', '/lv/vg/dev'],
    correctIndices: [1],
    explanation: 'Logical Volumes finns på /dev/vgnamn/lvnamn.',
    difficulty: 'G',
    category: 'LVM',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-46',
    question: 'MBR stands for...',
    options: [
      'Main Boot Record',
      'Master Boot Record',
      'Multiple Boot Region',
      'Memory Boot Record'
    ],
    correctIndices: [1],
    explanation: 'MBR = Master Boot Record, äldre partitionstabellformat.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-47',
    question: 'GPT stands for...',
    options: [
      'General Partition Table',
      'GUID Partition Table',
      'Global Partition Type',
      'Generic Partition Tool'
    ],
    correctIndices: [1],
    explanation: 'GPT = GUID Partition Table, modernt partitionstabellformat.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-48',
    question: 'MBR supports max disk size of...',
    options: ['1 TB', '2 TB', '4 TB', '8 TB'],
    correctIndices: [1],
    explanation: 'MBR stöder max 2 TB diskstorlek.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-49',
    question: 'MBR supports max partitions of...',
    options: ['2', '4 primary', '8', '16'],
    correctIndices: [1],
    explanation: 'MBR stöder max 4 primära partitioner (eller 3 primära + 1 extended).',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-50',
    question: 'GPT supports max partitions of...',
    options: ['4', '16', '64', '128'],
    correctIndices: [3],
    explanation: 'GPT stöder upp till 128 partitioner som standard.',
    difficulty: 'G',
    category: 'Partitioning',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-51',
    question: 'The command to initialize LUKS is...',
    options: [
      'luks format',
      'cryptsetup luksFormat',
      'luks create',
      'cryptsetup create'
    ],
    correctIndices: [1],
    explanation: 'cryptsetup luksFormat initialiserar LUKS-kryptering på en partition.',
    difficulty: 'G',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-52',
    question: 'The command to open LUKS is...',
    options: ['luks open', 'cryptsetup open', 'luks mount', 'cryptsetup mount'],
    correctIndices: [1],
    explanation: 'cryptsetup open öppnar en krypterad LUKS-volym.',
    difficulty: 'G',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-53',
    question: 'The command to close LUKS is...',
    options: [
      'luks close',
      'cryptsetup close',
      'luks unmount',
      'cryptsetup unmount'
    ],
    correctIndices: [1],
    explanation: 'cryptsetup close stänger en öppen LUKS-volym.',
    difficulty: 'G',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-54',
    question: 'Opened LUKS device appears in...',
    options: ['/dev/luks/', '/dev/mapper/', '/dev/crypt/', '/luks/'],
    correctIndices: [1],
    explanation: 'Öppnade LUKS-volymer visas i /dev/mapper/.',
    difficulty: 'G',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-55',
    question: 'LUKS header backup is important because...',
    options: [
      'It speeds up access',
      'Header damage = data loss',
      "It's required",
      'It enables sharing'
    ],
    correctIndices: [1],
    explanation: 'Om LUKS-headern skadas går all data förlorad, därför är backup kritiskt.',
    difficulty: 'VG',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-56',
    question: 'To backup LUKS header, use...',
    options: [
      'cryptsetup backup',
      'cryptsetup luksHeaderBackup',
      'luks backup',
      'cryptsetup save'
    ],
    correctIndices: [1],
    explanation: 'cryptsetup luksHeaderBackup skapar en backup av LUKS-headern.',
    difficulty: 'VG',
    category: 'LUKS Encryption',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-57',
    question: '3-2-1 backup rule: 3 means...',
    options: [
      '3 different locations',
      '3 different media',
      '3 copies of data',
      '3 encryption keys'
    ],
    correctIndices: [2],
    explanation: '3-2-1: 3 kopior av data, 2 olika mediatyper, 1 off-site.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-58',
    question: '3-2-1 backup rule: 2 means...',
    options: [
      '2 copies of data',
      '2 different media types',
      '2 different locations',
      '2 encryption keys'
    ],
    correctIndices: [1],
    explanation: '3-2-1: 3 kopior av data, 2 olika mediatyper, 1 off-site.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-59',
    question: '3-2-1 backup rule: 1 means...',
    options: [
      '1 copy of data',
      '1 media type',
      '1 off-site backup',
      '1 encryption key'
    ],
    correctIndices: [2],
    explanation: '3-2-1: 3 kopior av data, 2 olika mediatyper, 1 off-site backup.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-60',
    question: 'Select all valid backup strategies (choose 3):',
    options: [
      'Full backup',
      'Empty backup',
      'Incremental backup',
      'Partial backup',
      'Differential backup',
      'Fractional backup',
      'Complete backup',
      'Total backup',
      'Segment backup',
      'Section backup'
    ],
    correctIndices: [0, 2, 4],
    explanation: 'Full, Incremental och Differential är de tre huvudsakliga backup-strategierna.',
    difficulty: 'VG',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-61',
    question: 'Incremental backup saves...',
    options: [
      'All data',
      'Changes since last backup',
      'Half the data',
      'Random data'
    ],
    correctIndices: [1],
    explanation: 'Incremental backup sparar endast ändringar sedan senaste backup (full eller incremental).',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-62',
    question: 'Differential backup saves...',
    options: [
      'All data',
      'Changes since last full backup',
      'Changes since last differential',
      'Random data'
    ],
    correctIndices: [1],
    explanation: 'Differential backup sparar alla ändringar sedan senaste fulla backup.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-63',
    question: 'Full backup saves...',
    options: ['Only changes', 'Only new files', 'All data', 'Selected data'],
    correctIndices: [2],
    explanation: 'Full backup sparar all data oavsett om den ändrats eller inte.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-64',
    question: 'To copy disk block-by-block, use...',
    options: ['cp', 'copy', 'dd', 'clone'],
    correctIndices: [2],
    explanation: 'dd kopierar data block för block, perfekt för diskkloning.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-65',
    question: 'dd stands for...',
    options: [
      'Disk Dump',
      'Data Duplicator (or disk dump)',
      'Direct Data',
      'Drive Duplicate'
    ],
    correctIndices: [1],
    explanation: 'dd kallas ofta "data duplicator" eller "disk dump".',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-66',
    question: 'To sync files/directories, use...',
    options: ['sync', 'copy', 'rsync', 'filesync'],
    correctIndices: [2],
    explanation: 'rsync synkroniserar filer och kataloger effektivt.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-67',
    question: 'rsync flag -a means...',
    options: ['All files', 'Archive mode', 'Add files', 'Auto mode'],
    correctIndices: [1],
    explanation: '-a (archive) bevarar rättigheter, ägare, tidsstämplar och kopierar rekursivt.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-68',
    question: 'rsync flag -v means...',
    options: ['Verify', 'Verbose', 'Version', 'Virtual'],
    correctIndices: [1],
    explanation: '-v (verbose) visar detaljerad information under körning.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-69',
    question: 'rsync flag -z means...',
    options: ['Zero files', 'Compress', 'Zone', 'Zip'],
    correctIndices: [1],
    explanation: '-z komprimerar data under överföring.',
    difficulty: 'G',
    category: 'Backup',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-70',
    question: 'fstab has how many columns?',
    options: ['4', '5', '6', '7'],
    correctIndices: [2],
    explanation: 'fstab har 6 kolumner: device, mount point, type, options, dump, pass.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-71',
    question: 'fstab column 1 is...',
    options: ['Mount point', 'Device/UUID', 'Filesystem type', 'Options'],
    correctIndices: [1],
    explanation: 'Kolumn 1 i fstab är enheten eller UUID.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-72',
    question: 'fstab column 2 is...',
    options: ['Device', 'Mount point', 'Filesystem type', 'Options'],
    correctIndices: [1],
    explanation: 'Kolumn 2 i fstab är monteringspunkten.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-73',
    question: 'fstab column 3 is...',
    options: ['Device', 'Mount point', 'Filesystem type', 'Options'],
    correctIndices: [2],
    explanation: 'Kolumn 3 i fstab är filsystemstypen.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-74',
    question: 'fstab column 4 is...',
    options: ['Device', 'Mount point', 'Filesystem type', 'Options'],
    correctIndices: [3],
    explanation: 'Kolumn 4 i fstab är monteringsalternativ.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-75',
    question: 'fstab option "defaults" includes...',
    options: [
      'ro, noexec',
      'rw, suid, dev, exec, auto, nouser, async',
      'rw only',
      'Nothing special'
    ],
    correctIndices: [1],
    explanation: '"defaults" inkluderar: rw, suid, dev, exec, auto, nouser, async.',
    difficulty: 'VG',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-76',
    question: 'fstab option "noauto" means...',
    options: [
      'No automatic backup',
      "Don't mount at boot",
      'No automatic unmount',
      'No auto-resize'
    ],
    correctIndices: [1],
    explanation: '"noauto" betyder att filsystemet inte monteras automatiskt vid uppstart.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-77',
    question: 'fstab option "ro" means...',
    options: ['Root only', 'Read only', 'Remote only', 'Required option'],
    correctIndices: [1],
    explanation: '"ro" betyder read-only, filsystemet kan bara läsas.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-78',
    question: 'To test fstab without reboot, use...',
    options: ['fstab test', 'test mount', 'mount -a', 'mount test'],
    correctIndices: [2],
    explanation: 'mount -a monterar alla filsystem i fstab som inte redan är monterade.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-79',
    question: 'Select valid fstab options (choose 4):',
    options: [
      'defaults',
      'standard',
      'noauto',
      'noBoot',
      'ro',
      'readonly',
      'rw',
      'readwrite',
      'normal',
      'basic'
    ],
    correctIndices: [0, 2, 4, 6],
    explanation: 'defaults, noauto, ro och rw är giltiga fstab-alternativ.',
    difficulty: 'VG',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-80',
    question: 'Swap space is used when...',
    options: ['Disk is full', 'RAM is full', 'CPU is full', 'Network is full'],
    correctIndices: [1],
    explanation: 'Swap används när RAM är fullt för att tillfälligt flytta data från minnet.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-81',
    question: 'To create swap, use...',
    options: ['swapnew', 'createswap', 'mkswap', 'newswap'],
    correctIndices: [2],
    explanation: 'mkswap skapar ett swap-område på en partition eller fil.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-82',
    question: 'To enable swap, use...',
    options: ['swapenable', 'startswap', 'swapon', 'enableswap'],
    correctIndices: [2],
    explanation: 'swapon aktiverar ett swap-område.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-83',
    question: 'To disable swap, use...',
    options: ['swapdisable', 'stopswap', 'swapoff', 'disableswap'],
    correctIndices: [2],
    explanation: 'swapoff inaktiverar ett swap-område.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-84',
    question: 'To show swap usage, use...',
    options: ['swap', 'showswap', 'swapon -s or free', 'swapinfo'],
    correctIndices: [2],
    explanation: 'swapon -s eller free visar swap-användning.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-85',
    question: 'Recommended swap size is...',
    options: ['Same as disk', '1-2x RAM', '10x RAM', 'Fixed 8GB'],
    correctIndices: [1],
    explanation: 'Rekommenderad swap-storlek är 1-2 gånger mängden RAM.',
    difficulty: 'G',
    category: 'Swap',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-86',
    question: 'To show memory usage, use...',
    options: ['mem', 'memory', 'free', 'ram'],
    correctIndices: [2],
    explanation: 'free visar RAM- och swap-användning.',
    difficulty: 'G',
    category: 'Memory',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-87',
    question: 'free flag -h shows...',
    options: ['Help', 'Human readable', 'Headers', 'History'],
    correctIndices: [1],
    explanation: '-h visar minnesstorlekar i läsbart format.',
    difficulty: 'G',
    category: 'Memory',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-88',
    question: '/dev/sda refers to...',
    options: [
      'First partition',
      'First SATA/SCSI disk',
      'System disk always',
      'Swap disk'
    ],
    correctIndices: [1],
    explanation: '/dev/sda är den första SATA/SCSI-disken i systemet.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-89',
    question: '/dev/sda1 refers to...',
    options: [
      'First disk',
      'First partition on first disk',
      'First logical volume',
      'First mount point'
    ],
    correctIndices: [1],
    explanation: '/dev/sda1 är första partitionen på första disken.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-90',
    question: '/dev/nvme0n1 refers to...',
    options: ['Network volume', 'First NVMe disk', 'Virtual disk', 'Swap space'],
    correctIndices: [1],
    explanation: '/dev/nvme0n1 är den första NVMe SSD:n.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-91',
    question: 'Select all block device names (choose 4):',
    options: [
      '/dev/sda',
      '/dev/disk',
      '/dev/nvme0n1',
      '/dev/drive',
      '/dev/vda',
      '/dev/virtual',
      '/dev/xvda',
      '/dev/cloud',
      '/dev/storage',
      '/dev/block'
    ],
    correctIndices: [0, 2, 4, 6],
    explanation: '/dev/sda, /dev/nvme0n1, /dev/vda och /dev/xvda är giltiga blockenhetsnamn.',
    difficulty: 'VG',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-92',
    question: '/dev/vda is typically...',
    options: ['Physical disk', 'Virtual disk (KVM)', 'Network disk', 'USB disk'],
    correctIndices: [1],
    explanation: '/dev/vda är typiskt en virtuell disk i KVM/QEMU.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-93',
    question: '/dev/xvda is typically...',
    options: ['Physical disk', 'Xen virtual disk', 'Network disk', 'External disk'],
    correctIndices: [1],
    explanation: '/dev/xvda är typiskt en virtuell disk i Xen-virtualisering.',
    difficulty: 'G',
    category: 'Block Devices',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-94',
    question: 'To show mounted filesystems, use...',
    options: ['showmount', 'mount or findmnt', 'listmount', 'mounts'],
    correctIndices: [1],
    explanation: 'mount eller findmnt visar monterade filsystem.',
    difficulty: 'G',
    category: 'Mounting',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-95',
    question: 'To show filesystem type, use...',
    options: ['fstype', 'df -T', 'type fs', 'mount -t'],
    correctIndices: [1],
    explanation: 'df -T visar filsystemstyp för monterade filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-96',
    question: 'tmpfs is...',
    options: [
      'Temporary disk',
      'RAM-based filesystem',
      'Temp partition',
      'Cache filesystem'
    ],
    correctIndices: [1],
    explanation: 'tmpfs är ett RAM-baserat filsystem för temporär lagring.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-97',
    question: '/tmp is usually...',
    options: [
      'Permanent storage',
      'Temporary storage',
      'System storage',
      'User storage'
    ],
    correctIndices: [1],
    explanation: '/tmp är för temporära filer som kan raderas vid omstart.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-98',
    question: 'RAID stands for...',
    options: [
      'Random Array of Inexpensive Disks',
      'Redundant Array of Independent Disks',
      'Rapid Array of Internal Disks',
      'Reliable Array of Identical Disks'
    ],
    correctIndices: [1],
    explanation: 'RAID = Redundant Array of Independent Disks.',
    difficulty: 'G',
    category: 'RAID',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-99',
    question: 'RAID 0 provides...',
    options: [
      'Redundancy only',
      'Striping only (no redundancy)',
      'Mirroring only',
      'Both striping and mirroring'
    ],
    correctIndices: [1],
    explanation: 'RAID 0 ger endast striping (prestanda) utan redundans.',
    difficulty: 'G',
    category: 'RAID',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-100',
    question: 'RAID 1 provides...',
    options: [
      'Striping only',
      'Mirroring (redundancy)',
      'Parity only',
      'No benefit'
    ],
    correctIndices: [1],
    explanation: 'RAID 1 ger spegling/mirroring för redundans.',
    difficulty: 'G',
    category: 'RAID',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-101',
    question: 'tune2fs is used for...',
    options: [
      'Tuning system',
      'Adjusting ext filesystem',
      'Tuning performance',
      'Tuning network'
    ],
    correctIndices: [1],
    explanation: 'tune2fs justerar parametrar för ext-filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-102',
    question: 'e2label sets...',
    options: [
      'Disk label',
      'ext filesystem label',
      'Partition label',
      'Volume label'
    ],
    correctIndices: [1],
    explanation: 'e2label sätter etikett på ext-filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-103',
    question: 'xfs_repair is for...',
    options: [
      'ext4 filesystems',
      'XFS filesystems',
      'All filesystems',
      'btrfs filesystems'
    ],
    correctIndices: [1],
    explanation: 'xfs_repair reparerar XFS-filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-104',
    question: 'To resize XFS, use...',
    options: ['resize2fs', 'xfs_growfs', 'xfs_resize', 'growxfs'],
    correctIndices: [1],
    explanation: 'xfs_growfs utökar XFS-filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-105',
    question: 'XFS can only be...',
    options: [
      'Shrunk',
      'Grown (not shrunk)',
      'Both grown and shrunk',
      'Neither'
    ],
    correctIndices: [1],
    explanation: 'XFS kan endast utökas, inte krympas.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-106',
    question: 'Select all filesystem check commands (choose 3):',
    options: [
      'fsck',
      'diskcheck',
      'e2fsck',
      'checkdisk',
      'xfs_repair',
      'repairfs',
      'fixdisk',
      'healfs',
      'verify',
      'validate'
    ],
    correctIndices: [0, 2, 4],
    explanation: 'fsck, e2fsck och xfs_repair är kommandon för att kontrollera/reparera filsystem.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-107',
    question: 'To show inode usage, use...',
    options: ['inodes', 'df -i', 'ls -i', 'inode -l'],
    correctIndices: [1],
    explanation: 'df -i visar inode-användning för filsystem.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-108',
    question: 'Disk full but df shows space? Check...',
    options: ['RAM', 'Inodes (df -i)', 'CPU', 'Network'],
    correctIndices: [1],
    explanation: 'Om disken verkar full men df visar utrymme kan inoderna vara slut.',
    difficulty: 'VG',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-109',
    question: 'stat command shows...',
    options: [
      'Statistics',
      'Status',
      'File information including inode',
      'System state'
    ],
    correctIndices: [2],
    explanation: 'stat visar detaljerad filinformation inklusive inode.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  },
  {
    id: 'omtenta-v2-storage-110',
    question: 'ln command creates...',
    options: [
      'Soft links only',
      'Hard links (default)',
      'Both equally',
      'Neither'
    ],
    correctIndices: [1],
    explanation: 'ln skapar hard links som standard. Använd -s för soft links.',
    difficulty: 'G',
    category: 'Filesystems',
    topic: 'blockstorage-kryptering'
  }
]
