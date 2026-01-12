/**
 * INFÖR OMTENTA LINUX - Del 3A: Användarhantering & Filsystem
 * 100 quiz-frågor
 * 
 * Skapad: 2026-01-12
 */

import { OmtentaQuestion } from './omtenta-ssh-brandvagg'

// ============================================================================
// ANVÄNDARHANTERING (50 frågor)
// ============================================================================

export const ANVANDARHANTERING_QUESTIONS: OmtentaQuestion[] = [
    {
        id: 'omtenta-user-1',
        question: 'Kommandot för att skapa en ny användare är...',
        options: ['newuser', 'adduser', 'createuser', 'useradd'],
        correctIndex: 3,
        explanation: 'useradd är standardkommandot. adduser är en interaktiv wrapper.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-2',
        question: 'För att lägga till en användare i en grupp UTAN att ta bort från andra grupper använder du...',
        options: ['usermod -G', 'groupadd -a', 'addgroup', 'usermod -aG'],
        correctIndex: 3,
        explanation: '-a = append, -G = supplementary groups. Utan -a raderas andra grupper!',
        difficulty: 'VG',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-3',
        question: 'Vilken fil innehåller information om alla användare?',
        options: ['/etc/users', '/etc/accounts', '/var/users', '/etc/passwd'],
        correctIndex: 3,
        explanation: '/etc/passwd innehåller användarinfo (men inte lösenord längre).',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 'omtenta-user-4',
        question: 'Kommandot för att byta lösenord är...',
        options: ['password', 'chpass', 'setpass', 'passwd'],
        correctIndex: 3,
        explanation: 'passwd ändrar lösenord för nuvarande eller angiven användare.',
        difficulty: 'G',
        category: 'Lösenord'
    },
    {
        id: 'omtenta-user-5',
        question: 'SGID-biten gör att filer i en mapp...',
        options: ['Körs som root', 'Blir osynliga', 'Inte kan raderas', 'Ärver gruppägande från mappen'],
        correctIndex: 3,
        explanation: 'SGID på mapp = nya filer får mappens grupp, inte skaparens.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-6',
        question: 'Vad gör kommandot chmod 770?',
        options: ['Bara läsbehörighet', 'Full tillgång för alla', 'Ingen tillgång för någon', 'Full tillgång för ägare och grupp, ingen för andra'],
        correctIndex: 3,
        explanation: '7=rwx, 7=rwx, 0=--- → ägare+grupp får allt, andra inget.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-7',
        question: 'Vilken permission representeras av siffran 7?',
        options: ['read', 'write', 'execute', 'rwx (alla tre)'],
        correctIndex: 3,
        explanation: '4(r) + 2(w) + 1(x) = 7 = alla permissions.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-8',
        question: 'Kommandot för att ändra grupptillhörighet på en fil är...',
        options: ['groupmod', 'setgroup', 'chmod', 'chgrp'],
        correctIndex: 3,
        explanation: 'chgrp grupp fil ändrar gruppägare.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-9',
        question: 'Hur sätter du SGID på en mapp?',
        options: ['chmod +s', 'chmod u+s', 'chmod o+s', 'chmod g+s'],
        correctIndex: 3,
        explanation: 'g+s = group SGID. u+s = user SUID.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-10',
        question: 'Kommandot för att visa vilka grupper en användare tillhör är...',
        options: ['usergroups', 'getgroups', 'listgroups', 'groups'],
        correctIndex: 3,
        explanation: 'groups username visar alla grupper för användaren.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-11',
        question: 'För att sätta utgångsdatum på ett konto använder du...',
        options: ['passwd --expire', 'setexpire', 'account -e', 'usermod --expiredate'],
        correctIndex: 3,
        explanation: 'usermod --expiredate YYYY-MM-DD user sätter utgångsdatum.',
        difficulty: 'VG',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-12',
        question: 'Kommandot chage används för att...',
        options: ['Byta användarnamn', 'Ändra grupp', 'Skapa användare', 'Hantera lösenordspolicy'],
        correctIndex: 3,
        explanation: 'chage hanterar lösenords ålder, utgång, varningar.',
        difficulty: 'G',
        category: 'Lösenord'
    },
    {
        id: 'omtenta-user-13',
        question: 'Vilken permission representeras av siffran 4?',
        options: ['write', 'execute', 'none', 'read'],
        correctIndex: 3,
        explanation: '4 = read (r). 2 = write (w). 1 = execute (x).',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-14',
        question: 'Kommandot för att ta bort en användare är...',
        options: ['deluser', 'removeuser', 'rmuser', 'userdel'],
        correctIndex: 3,
        explanation: 'userdel tar bort användare. -r tar även bort hemkatalogen.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-15',
        question: 'Vad visar kommandot id?',
        options: ['Bara användarnamn', 'Bara lösenordsstatus', 'Filsysteminfo', 'UID, GID och grupptillhörigheter'],
        correctIndex: 3,
        explanation: 'id visar uid, gid och alla grupper för användaren.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-16',
        question: 'Vilken flagga behövs för att tvinga lösenordsbyte vid nästa login?',
        options: ['passwd -f', 'passwd -n', 'passwd -c', 'passwd --expire'],
        correctIndex: 3,
        explanation: 'passwd --expire user gör att lösenordet måste bytas.',
        difficulty: 'G',
        category: 'Lösenord'
    },
    {
        id: 'omtenta-user-17',
        question: 'Kommandot getent passwd används för att...',
        options: ['Skapa användare', 'Byta lösenord', 'Radera användare', 'Lista användare från systemdatabaser'],
        correctIndex: 3,
        explanation: 'getent hämtar från alla källor (lokalt + LDAP, etc.).',
        difficulty: 'VG',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-18',
        question: 'Vad gör chmod 2770?',
        options: ['Bara SUID', 'Sticky bit', 'Alla special permissions', 'SGID + rwx för ägare och grupp'],
        correctIndex: 3,
        explanation: '2 = SGID, 770 = rwx för ägare och grupp.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-19',
        question: 'Vilken fil innehåller gruppdefinitioner?',
        options: ['/etc/passwd', '/etc/users', '/etc/groups', '/etc/group'],
        correctIndex: 3,
        explanation: '/etc/group listar alla grupper och deras medlemmar.',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 'omtenta-user-20',
        question: 'Permission 0 betyder...',
        options: ['Read only', 'Execute only', 'Full tillgång', 'Ingen tillgång'],
        correctIndex: 3,
        explanation: '0 = --- = inga rättigheter.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-21',
        question: 'Kommandot för att skapa en ny grupp är...',
        options: ['newgroup', 'addgroup', 'creategroup', 'groupadd'],
        correctIndex: 3,
        explanation: 'groupadd skapar en ny grupp.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-22',
        question: 'Vad representerar "x" i permissions?',
        options: ['Extra', 'Exclude', 'Export', 'Execute (köra)'],
        correctIndex: 3,
        explanation: 'x = execute, möjlighet att köra filer eller gå in i mappar.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-23',
        question: 'Kommandot chown ändrar...',
        options: ['Bara grupp', 'Permissions', 'Filnamn', 'Ägare (och eventuellt grupp)'],
        correctIndex: 3,
        explanation: 'chown user:group fil ändrar ägare och grupp.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-24',
        question: 'Vilken permission representeras av siffran 2?',
        options: ['read', 'execute', 'none', 'write'],
        correctIndex: 3,
        explanation: '2 = write (w).',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-25',
        question: 'För att lista detaljer om en mapps permissions använder du...',
        options: ['ls -a', 'ls -r', 'ls -p', 'ls -ld'],
        correctIndex: 3,
        explanation: '-l = long format, -d = directory itself (inte innehållet).',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-26',
        question: 'Vad innebär sticky bit på en mapp?',
        options: ['Filer kan inte skapas', 'Alla kan radera allt', 'Mappen kan inte raderas', 'Bara ägaren kan radera sina filer'],
        correctIndex: 3,
        explanation: 'Sticky bit på /tmp förhindrar att användare raderar andras filer.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-27',
        question: 'SUID-biten (4000) gör att ett program...',
        options: ['Körs som gruppen', 'Inte kan köras', 'Körs dubbelt', 'Körs som filens ägare'],
        correctIndex: 3,
        explanation: 'SUID = programmet körs med ägarens rättigheter (t.ex. passwd).',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-28',
        question: 'Vilken flagga tar usermod för att ändra primär grupp?',
        options: ['-a', '-G', '-p', '-g'],
        correctIndex: 3,
        explanation: '-g = primary group. -G = supplementary groups.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-29',
        question: 'Datumet 2026-01-01 i Linux är i format...',
        options: ['DD-MM-YYYY', 'MM-DD-YYYY', 'DD/MM/YYYY', 'YYYY-MM-DD'],
        correctIndex: 3,
        explanation: 'ISO 8601 format: YYYY-MM-DD.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'omtenta-user-30',
        question: 'Vilken permission representeras av siffran 1?',
        options: ['read', 'write', 'none', 'execute'],
        correctIndex: 3,
        explanation: '1 = execute (x).',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-31',
        question: 'Kommandot gpasswd används för att...',
        options: ['Byta lösenord', 'Skapa användare', 'Ändra permissions', 'Administrera grupper'],
        correctIndex: 3,
        explanation: 'gpasswd -a user group lägger till användare i grupp.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-32',
        question: 'I ls -l output, vad betyder "d" först?',
        options: ['Dold fil', 'Disk', 'Device', 'Directory (mapp)'],
        correctIndex: 3,
        explanation: 'd = directory. - = vanlig fil. l = symlink.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-33',
        question: 'Vad visar "s" istället för "x" i permissions?',
        options: ['Sticky bit', 'Secret file', 'System file', 'SUID eller SGID är satt'],
        correctIndex: 3,
        explanation: 's = SUID/SGID med execute. S = utan execute.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-34',
        question: 'För att kontrollera lösenordspolicy på en användare använder du...',
        options: ['passwd -l', 'usermod -l', 'policy -l', 'chage -l'],
        correctIndex: 3,
        explanation: 'chage -l user visar lösenordspolicy.',
        difficulty: 'G',
        category: 'Lösenord'
    },
    {
        id: 'omtenta-user-35',
        question: 'Vad gör chmod 755?',
        options: ['Bara läsbar', 'Endast körbar', 'Ingen tillgång', 'rwx för ägare, rx för grupp och andra'],
        correctIndex: 3,
        explanation: '7=rwx, 5=r-x, 5=r-x. Typiskt för scripts.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-36',
        question: 'Kommandot whoami visar...',
        options: ['Alla inloggade användare', 'Systeminfo', 'Root-lösenord', 'Nuvarande användarnamn'],
        correctIndex: 3,
        explanation: 'whoami visar vem du är inloggad som.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-37',
        question: 'Vilken specialpermission har numeriskt värde 1000?',
        options: ['SUID', 'SGID', 'None', 'Sticky bit'],
        correctIndex: 3,
        explanation: '1000 = sticky bit. 2000 = SGID. 4000 = SUID.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-38',
        question: 'För att se inloggade användare använder du...',
        options: ['logged', 'online', 'sessions', 'who, w, eller users'],
        correctIndex: 3,
        explanation: 'who, w och users visar alla inloggade användare.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-39',
        question: 'Vad gör chmod 644?',
        options: ['Full tillgång för alla', 'Ingen tillgång', 'Endast execute', 'rw för ägare, r för grupp och andra'],
        correctIndex: 3,
        explanation: '6=rw-, 4=r--, 4=r--. Typiskt för vanliga filer.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-40',
        question: 'Vilken fil innehåller krypterade lösenord?',
        options: ['/etc/passwd', '/etc/passwords', '/etc/secure', '/etc/shadow'],
        correctIndex: 3,
        explanation: '/etc/shadow innehåller hashade lösenord, endast läsbar av root.',
        difficulty: 'G',
        category: 'Filer'
    },
    {
        id: 'omtenta-user-41',
        question: 'Kommandot newgrp används för att...',
        options: ['Skapa ny grupp', 'Radera grupp', 'Lista grupper', 'Byta primär grupp temporärt'],
        correctIndex: 3,
        explanation: 'newgrp grupp startar ny shell med annan primär grupp.',
        difficulty: 'VG',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-42',
        question: 'Vad betyder -R flaggan i chmod -R?',
        options: ['Read only', 'Reverse', 'Root', 'Rekursivt (alla undermappar)'],
        correctIndex: 3,
        explanation: '-R applicerar ändringen på mapp och allt innehåll.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-43',
        question: 'Permission 6 betyder...',
        options: ['rwx', 'r-x', '-wx', 'rw- (read + write)'],
        correctIndex: 3,
        explanation: '4(r) + 2(w) = 6 = rw-.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-44',
        question: 'Kommandot vipw används för att...',
        options: ['Starta Vim', 'Byta lösenord', 'Visa användare', 'Redigera passwd-filen säkert'],
        correctIndex: 3,
        explanation: 'vipw låser filen så den inte blir korrupt.',
        difficulty: 'VG',
        category: 'Filer'
    },
    {
        id: 'omtenta-user-45',
        question: 'Varför ska man använda -aG och inte bara -G med usermod?',
        options: ['Det går snabbare', 'Ingen skillnad', '-aG är säkrare', '-G tar bort användaren från andra grupper'],
        correctIndex: 3,
        explanation: 'Utan -a ersätts supplementary groups helt!',
        difficulty: 'VG',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-46',
        question: 'Vilken UID har root-användaren?',
        options: ['1', '1000', '100', '0'],
        correctIndex: 3,
        explanation: 'root har alltid UID 0. Vanliga användare börjar från 1000.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-47',
        question: 'Vad gör kommandot groups utan argument?',
        options: ['Listar alla grupper', 'Skapar grupp', 'Fel', 'Visar grupper för nuvarande användare'],
        correctIndex: 3,
        explanation: 'groups utan argument visar dina egna grupper.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'omtenta-user-48',
        question: 'Permission 5 betyder...',
        options: ['rw-', '-wx', 'rwx', 'r-x (read + execute)'],
        correctIndex: 3,
        explanation: '4(r) + 1(x) = 5 = r-x.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'omtenta-user-49',
        question: 'Vilken flagga i useradd skapar hemmapp?',
        options: ['-h', '-d', '-H', '-m'],
        correctIndex: 3,
        explanation: '-m = make home directory.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'omtenta-user-50',
        question: 'Kommandot vigr används för att...',
        options: ['Visa grupper', 'Skapa grupper', 'Verifiera grupper', 'Redigera group-filen säkert'],
        correctIndex: 3,
        explanation: 'vigr är vipw-motsvarigheten för /etc/group.',
        difficulty: 'VG',
        category: 'Filer'
    }
]

// ============================================================================
// FILSYSTEM & ONBOARDING (50 frågor)
// ============================================================================

export const FILSYSTEM_QUESTIONS: OmtentaQuestion[] = [
    {
        id: 'omtenta-fs-1',
        question: 'Kommandot pwd står för...',
        options: ['Print Work Done', 'Path Working Directory', 'Print Where Directory', 'Print Working Directory'],
        correctIndex: 3,
        explanation: 'pwd visar vilken katalog du befinner dig i.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-2',
        question: 'För att gå till din hemmapp kan du använda...',
        options: ['cd home', 'cd /', 'cd root', 'cd ~'],
        correctIndex: 3,
        explanation: '~ är en genväg till din hemmapp. cd utan argument fungerar också.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-3',
        question: 'Vilken flagga visar dolda filer med ls?',
        options: ['-h', '-l', '-d', '-a'],
        correctIndex: 3,
        explanation: '-a = all, visar filer som börjar med punkt.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-4',
        question: 'Vad representerar .. i Linux filsystem?',
        options: ['Nuvarande mapp', 'Root-mappen', 'Hemmappen', 'Mappen en nivå upp'],
        correctIndex: 3,
        explanation: '.. = föräldrakatalogen, . = nuvarande katalog.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-5',
        question: 'Vilken path börjar INTE med /?',
        options: ['Absolut path', 'Root path', 'System path', 'Relativ path'],
        correctIndex: 3,
        explanation: 'Relativ path utgår från nuvarande position, t.ex. ./folder.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-6',
        question: 'Kommandot touch används för att...',
        options: ['Radera filer', 'Kopiera filer', 'Flytta filer', 'Skapa tomma filer'],
        correctIndex: 3,
        explanation: 'touch skapar tom fil eller uppdaterar tidsstämpel.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-7',
        question: 'För att skapa en mapp med alla föräldramappar använder du...',
        options: ['mkdir -r', 'mkdir -a', 'mkdir -f', 'mkdir -p'],
        correctIndex: 3,
        explanation: '-p = parents, skapar hela sökvägen.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-8',
        question: 'Kommandot rm -r används för att...',
        options: ['Radera bara tomma mappar', 'Radera skrivskyddade filer', 'Visa vad som ska raderas', 'Radera mappar rekursivt'],
        correctIndex: 3,
        explanation: '-r = recursive, tar bort mapp och allt innehåll.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-9',
        question: 'Vad gör kommandot mv?',
        options: ['Bara flyttar filer', 'Bara byter namn på filer', 'Kopierar filer', 'Både flyttar och byter namn'],
        correctIndex: 3,
        explanation: 'mv flyttar filer/mappar OCH kan byta namn.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-10',
        question: 'Vilken pager rekommenderas istället för more?',
        options: ['cat', 'view', 'page', 'less'],
        correctIndex: 3,
        explanation: 'less kan scrolla båda riktningar, mer funktioner.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-11',
        question: 'I less, hur söker du efter text?',
        options: ['s', 'f', '?', '/'],
        correctIndex: 3,
        explanation: '/ startar sökning framåt. ? söker bakåt.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-12',
        question: 'För att avsluta less eller man, trycker du...',
        options: ['x', 'e', 'ESC', 'q'],
        correctIndex: 3,
        explanation: 'q = quit, avslutar de flesta pagers.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-13',
        question: 'Kommandot find -type f söker efter...',
        options: ['Mappar', 'Länkar', 'Enheter', 'Filer'],
        correctIndex: 3,
        explanation: '-type f = files. -type d = directories.',
        difficulty: 'G',
        category: 'Sökning'
    },
    {
        id: 'omtenta-fs-14',
        question: 'Vilken sektion i man pages innehåller vanliga kommandon?',
        options: ['Sektion 3', 'Sektion 5', 'Sektion 8', 'Sektion 1'],
        correctIndex: 3,
        explanation: 'Sektion 1 = user commands. 5 = file formats. 8 = admin.',
        difficulty: 'G',
        category: 'Man Pages'
    },
    {
        id: 'omtenta-fs-15',
        question: 'I Vim, för att börja skriva text går du till...',
        options: ['Command mode', 'Normal mode', 'Visual mode', 'Insert mode'],
        correctIndex: 3,
        explanation: 'i, a, o etc. tar dig till Insert mode.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-16',
        question: 'För att spara och avsluta i Vim skriver du...',
        options: [':q', ':w', ':x!', ':wq'],
        correctIndex: 3,
        explanation: ':wq = write and quit. :x gör samma sak.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-17',
        question: 'Hur avslutar du Vim utan att spara ändringar?',
        options: [':q', ':wq', 'ESC', ':q!'],
        correctIndex: 3,
        explanation: ':q! = quit utan att spara (force).',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-18',
        question: 'I Vim, vilken tangent tar dig tillbaka till Normal mode?',
        options: ['Enter', 'Tab', 'Ctrl+C', 'ESC'],
        correctIndex: 3,
        explanation: 'ESC tar dig alltid tillbaka till Normal mode.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-19',
        question: 'Kommandot cat används för att...',
        options: ['Skapa filer', 'Redigera filer', 'Söka i filer', 'Visa hela filinnehåll'],
        correctIndex: 3,
        explanation: 'cat skriver ut hela filen. Bra för korta filer.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-20',
        question: 'Vilken mapp innehåller konfigurationsfiler i Linux?',
        options: ['/bin', '/home', '/var', '/etc'],
        correctIndex: 3,
        explanation: '/etc = etcetera, systemkonfiguration.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'omtenta-fs-21',
        question: 'Vad representerar . (en punkt) i filsystemet?',
        options: ['Rotmappen', 'Föräldramappen', 'Hemmappen', 'Nuvarande mapp'],
        correctIndex: 3,
        explanation: '. = current directory.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-22',
        question: 'Tab completion i terminalen hjälper dig att...',
        options: ['Tabulera text', 'Byta flik', 'Skapa tabeller', 'Autocomplete kommandon och filnamn'],
        correctIndex: 3,
        explanation: 'Tab fyller i resten automatiskt eller visar alternativ.',
        difficulty: 'G',
        category: 'Tips'
    },
    {
        id: 'omtenta-fs-23',
        question: 'Filer som börjar med . (punkt) är...',
        options: ['Systemfiler', 'Körbara filer', 'Temporära filer', 'Dolda filer'],
        correctIndex: 3,
        explanation: 'Punktfiler visas inte av ls utan -a flaggan.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'omtenta-fs-24',
        question: 'Kommandot ls -l visar...',
        options: ['Bara filnamn', 'Bara mappar', 'Dolda filer', 'Detaljerad information'],
        correctIndex: 3,
        explanation: '-l = long format med permissions, ägare, storlek, datum.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-25',
        question: 'Vilken flagga sorterar ls efter tid?',
        options: ['-s', '-r', '-d', '-t'],
        correctIndex: 3,
        explanation: '-t = sort by time. -r = reverse.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-26',
        question: 'Kommandot cp -r används för att...',
        options: ['Kopiera bara filer', 'Kopiera med bekräftelse', 'Kopiera bakåt', 'Kopiera mappar rekursivt'],
        correctIndex: 3,
        explanation: '-r = recursive, behövs för att kopiera mappar.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-27',
        question: 'Vad händer om du kör mv fil1.txt fil2.txt och fil2.txt redan finns?',
        options: ['Felmeddelande', 'fil1.txt kopieras', 'Inget händer', 'fil2.txt skrivs över'],
        correctIndex: 3,
        explanation: 'mv skriver över utan varning! Använd -i för prompt.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-28',
        question: 'Kommandot cd - tar dig till...',
        options: ['Hemmappen', 'Rotmappen', 'Föräldramappen', 'Föregående katalog'],
        correctIndex: 3,
        explanation: 'cd - växlar mellan nuvarande och föregående katalog.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-29',
        question: 'I Vim, dd raderar...',
        options: ['Ett tecken', 'Ett ord', 'Till slutet av raden', 'En hel rad'],
        correctIndex: 3,
        explanation: 'dd = delete line. d$ = delete to end of line.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-30',
        question: 'Kommandot u i Vim gör...',
        options: ['Uppåt en rad', 'Uppdatera', 'Går upp till första raden', 'Ångra (undo)'],
        correctIndex: 3,
        explanation: 'u = undo. Ctrl+R = redo.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-31',
        question: 'Vilken mapp innehåller loggar i Linux?',
        options: ['/etc', '/home', '/bin', '/var'],
        correctIndex: 3,
        explanation: '/var/log innehåller systemloggar.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'omtenta-fs-32',
        question: 'Kommandot find -name "*.txt" söker efter...',
        options: ['Filer som heter txt', 'Filer som börjar med txt', 'Filer som innehåller txt', 'Filer som slutar på .txt'],
        correctIndex: 3,
        explanation: '*.txt = alla filer med extension .txt.',
        difficulty: 'G',
        category: 'Sökning'
    },
    {
        id: 'omtenta-fs-33',
        question: 'För att visa hjälp i less trycker du...',
        options: ['?', 'help', '/help', 'h'],
        correctIndex: 3,
        explanation: 'h visar hjälp i less.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-34',
        question: 'Vilken fil skapas av Vim som backup?',
        options: ['.bak fil', '.backup fil', '.tmp fil', 'swap fil (.swp)'],
        correctIndex: 3,
        explanation: 'Vim skapar .swp-filer för crash recovery.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-35',
        question: 'Kommandot rmdir tar bort...',
        options: ['Alla mappar', 'Mappar med innehåll', 'Bara filer', 'Bara tomma mappar'],
        correctIndex: 3,
        explanation: 'rmdir tar endast bort tomma mappar. Använd rm -r annars.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-36',
        question: 'Vad betyder flaggan -f i rm -f?',
        options: ['File', 'Full', 'Fast', 'Force (ingen prompt)'],
        correctIndex: 3,
        explanation: '-f = force, frågar inte om bekräftelse.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-37',
        question: 'Vilka tangenter navigerar i Vims Normal mode?',
        options: ['wasd', 'pfeiltangenter bara', 'ijkl', 'h j k l'],
        correctIndex: 3,
        explanation: 'h=vänster, j=ner, k=upp, l=höger.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-38',
        question: 'Vad är /tmp mappen för?',
        options: ['Säkerhetskopiering', 'Konfiguration', 'Användarfiler', 'Temporära filer'],
        correctIndex: 3,
        explanation: '/tmp rensas ofta vid omstart.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'omtenta-fs-39',
        question: 'Kommandot man man visar...',
        options: ['Fel', 'Alla manualer', 'Inget', 'Manual för man-kommandot'],
        correctIndex: 3,
        explanation: 'man man visar hur man använder man-systemet.',
        difficulty: 'G',
        category: 'Man Pages'
    },
    {
        id: 'omtenta-fs-40',
        question: 'I less, Space-tangenten gör...',
        options: ['Söker', 'Avslutar', 'Går till början', 'Går ner en sida'],
        correctIndex: 3,
        explanation: 'Space = page down. b = page up.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-41',
        question: 'Vilken kommando öppnar interaktiv Vim-tutorial?',
        options: ['vim help', 'vim --tutorial', 'vim -t', 'vimtutor'],
        correctIndex: 3,
        explanation: 'vimtutor är en 30-minuters interaktiv tutorial.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-42',
        question: 'Kommandot ls -R visar...',
        options: ['Omvänd ordning', 'Endast root', 'Raw output', 'Rekursivt (undermappar)'],
        correctIndex: 3,
        explanation: '-R = recursive, visar alla undermappar.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-43',
        question: 'För att gå till nästa sökmatch i less/man trycker du...',
        options: ['s', 'next', 'f', 'n'],
        correctIndex: 3,
        explanation: 'n = next match. N = previous match.',
        difficulty: 'G',
        category: 'Verktyg'
    },
    {
        id: 'omtenta-fs-44',
        question: 'Vad gör Ctrl+L i bash?',
        options: ['Loggar ut', 'Listar filer', 'Låser terminalen', 'Rensar skärmen'],
        correctIndex: 3,
        explanation: 'Ctrl+L = clear, rensar terminalfönstret.',
        difficulty: 'G',
        category: 'Tips'
    },
    {
        id: 'omtenta-fs-45',
        question: 'Kommandot :w i Vim betyder...',
        options: ['Word', 'Window', 'Wrap', 'Write (spara)'],
        correctIndex: 3,
        explanation: ':w sparar filen utan att avsluta.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-46',
        question: 'Vilken flagga gör ls-storlekar läsbara för människor?',
        options: ['-r', '-l', '-s', '-h'],
        correctIndex: 3,
        explanation: '-h = human-readable (KB, MB, GB).',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'omtenta-fs-47',
        question: 'I en absolut path, vad betyder det första /?',
        options: ['Hemmappen', 'Nuvarande mapp', 'Användarens mapp', 'Rotmappen'],
        correctIndex: 3,
        explanation: '/ i början = root, toppen av filsystemet.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'omtenta-fs-48',
        question: 'Kommandot x i Vims Normal mode raderar...',
        options: ['En rad', 'Ett ord', 'Allt', 'Ett tecken'],
        correctIndex: 3,
        explanation: 'x raderar tecknet under markören.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'omtenta-fs-49',
        question: 'Vilken mapp innehåller viktiga program/kommandon?',
        options: ['/etc', '/var', '/home', '/bin'],
        correctIndex: 3,
        explanation: '/bin = binaries, grundläggande kommandon.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'omtenta-fs-50',
        question: 'I less, N (stor) går till...',
        options: ['Nästa sida', 'Nästa match', 'Ny sökning', 'Föregående sökmatch'],
        correctIndex: 3,
        explanation: 'N = previous match (bakåt).',
        difficulty: 'G',
        category: 'Verktyg'
    }
]

export const USER_FS_STATS = {
    userQuestions: ANVANDARHANTERING_QUESTIONS.length,
    fsQuestions: FILSYSTEM_QUESTIONS.length,
    totalQuestions: ANVANDARHANTERING_QUESTIONS.length + FILSYSTEM_QUESTIONS.length,
    gQuestions: [...ANVANDARHANTERING_QUESTIONS, ...FILSYSTEM_QUESTIONS].filter(q => q.difficulty === 'G').length,
    vgQuestions: [...ANVANDARHANTERING_QUESTIONS, ...FILSYSTEM_QUESTIONS].filter(q => q.difficulty === 'VG').length
}
