"""
Tentaplugg Linux - Study Data (Version 3.0)
=============================================
25 noder × 30 flashcards × 20 quiz = 1,250 studieobjekt

Struktur per nod:
- 10 easy + 10 medium + 10 hard flashcards
- 7 easy + 7 medium + 6 hard quiz (4 valsalternativ)

INNEHÅLLET SPEGLAR EXAKT materialets noder!
"""

# =============================================================================
# NOD 1: SUBNETTING & NÄTVERK
# Källa: doe25_tentaplugg.py SUBNETTING_NODE
# Koncept: Lådmetoden, 46.84.126.147/28 exemplet, Network ID, Broadcast
# =============================================================================

NOD_01_FLASHCARDS = {
    "easy": [
        # Från "Varför behöver du kunna detta?"
        {"front": "IP-adress som postadress - vad är 'gatan'?", "back": "Nätverksdelen (Network)"},
        {"front": "IP-adress som postadress - vad är 'husnumret'?", "back": "Hostdelen"},
        {"front": "Vad säger /24 om en IP-adress?", "back": "24 bitar är nätverk, 8 bitar är host"},
        # Lådmetoden
        {"front": "Lådmetodens 8 värden (memorera)?", "back": "128, 64, 32, 16, 8, 4, 2, 1"},
        {"front": "Varför är 32 magiskt i subnetting?", "back": "IPv4 har alltid 32 bitar totalt"},
        {"front": "Formel för host-bitar?", "back": "32 - prefix (ex: 32-28=4)"},
        # Grundbegrepp
        {"front": "Vad är Network ID?", "back": "Alla host-bitar nollade - identifierar nätverket"},
        {"front": "Vad är Broadcast?", "back": "Alla host-bitar ettställda - sista adressen"},
        {"front": "First Host formel?", "back": "Network ID + 1"},
        {"front": "Last Host formel?", "back": "Broadcast - 1"},
    ],
    "medium": [
        # 46.84.126.147/28 exemplet från materialet
        {"front": "46.84.126.147/28 - hur många host-bitar?", "back": "4 bitar (32-28=4)"},
        {"front": "Konvertera 147 med lådmetoden?", "back": "128+16+2+1 = 147 ✓"},
        {"front": "46.84.126.147/28 - Network ID?", "back": "46.84.126.144 (host-bitar nollade)"},
        {"front": "46.84.126.147/28 - Broadcast?", "back": "46.84.126.159 (host-bitar ettställda)"},
        {"front": "46.84.126.147/28 - First Host?", "back": "46.84.126.145 (Network+1)"},
        {"front": "46.84.126.147/28 - Last Host?", "back": "46.84.126.158 (Broadcast-1)"},
        {"front": "46.84.126.147/28 - Next Subnet?", "back": "46.84.126.160 (Broadcast+1)"},
        {"front": "46.84.126.147/28 - Antal hosts?", "back": "14 (2^4 - 2)"},
        # Tabell från materialet
        {"front": "Varför -2 i host-formeln?", "back": "Network och Broadcast kan inte användas av enheter"},
        {"front": "N och H i lådmetoden betyder?", "back": "N=Nätverksdel (låst), H=Hostdel (varierar)"},
    ],
    "hard": [
        # Prefix-tabellen från materialet
        {"front": "/24: host-bitar, adresser, hosts?", "back": "8 bitar, 256 adresser, 254 hosts"},
        {"front": "/25: host-bitar, adresser, hosts?", "back": "7 bitar, 128 adresser, 126 hosts"},
        {"front": "/26: host-bitar, adresser, hosts?", "back": "6 bitar, 64 adresser, 62 hosts"},
        {"front": "/27: host-bitar, adresser, hosts?", "back": "5 bitar, 32 adresser, 30 hosts"},
        {"front": "/28: host-bitar, adresser, hosts?", "back": "4 bitar, 16 adresser, 14 hosts"},
        {"front": "/29: host-bitar, adresser, hosts?", "back": "3 bitar, 8 adresser, 6 hosts"},
        {"front": "/30: host-bitar, adresser, hosts?", "back": "2 bitar, 4 adresser, 2 hosts"},
        {"front": "När används /30?", "back": "Punkt-till-punkt-länkar mellan routrar"},
        # DevOps-scenariot från materialet
        {"front": "Chef ger 10.0.0.0/24, dela i 4 segment?", "back": "Använd /26: 0, 64, 128, 192"},
        {"front": "Varför behövs router mellan subnät?", "back": "Olika 'gator' - behöver 'buss' för kommunikation"},
    ],
}

NOD_01_QUIZ = {
    "easy": [
        {"question": "Enligt materialet - IP-adress är som en postadress. Vad motsvarar 'gatan'?", "options": ["Hostdelen", "Nätverksdelen", "Subnätmasken", "Broadcast"], "correct": 1, "explanation": "Från materialet: 'En del säger vilken gata (nätverket)'"},
        {"question": "Vilka är lådmetodens 8 värden enligt materialet?", "options": ["1,2,4,8,16,32,64,128", "128,64,32,16,8,4,2,1", "256,128,64,32,16,8,4,2", "255,127,63,31,15,7,3,1"], "correct": 1, "explanation": "Materialet: 'Memorera dessa värden - 128,64,32,16,8,4,2,1'"},
        {"question": "Hur beräknas host-bitar enligt snabbreferensen?", "options": ["prefix - 32", "32 - prefix", "prefix × 2", "32 / prefix"], "correct": 1, "explanation": "Snabbreferens steg 1: 'Host-bitar = 32 - prefix'"},
        {"question": "Vad gör man för att hitta Network ID enligt lådmetoden?", "options": ["Sätt alla bitar till 1", "Sätt alla host-bitar till 0", "Lägg till 1", "Dra bort 1"], "correct": 1, "explanation": "Steg 4: 'Network ID = sätt alla host-bitar till 0'"},
        {"question": "Vad gör man för att hitta Broadcast enligt lådmetoden?", "options": ["Sätt alla bitar till 0", "Sätt alla host-bitar till 1", "Lägg till 1 till Network", "Ta bort 2 från max"], "correct": 1, "explanation": "Steg 5: 'Broadcast = sätt alla host-bitar till 1'"},
        {"question": "Enligt materialet - varför kan Network och Broadcast inte användas?", "options": ["De är reserverade för DNS", "Network identifierar nätverket, Broadcast går till alla", "De är för routrar", "De är krypterade"], "correct": 1, "explanation": "Materialet: 'Network ID identifierar nätverket, Broadcast skickar till alla'"},
        {"question": "Hur räknas First Host ut enligt formeln?", "options": ["Broadcast + 1", "Network ID + 1", "Network ID - 1", "Prefix + 1"], "correct": 1, "explanation": "Tabell: 'First Host = Network + 1'"},
    ],
    "medium": [
        {"question": "I exemplet 46.84.126.147/28 - hur många host-bitar?", "options": ["28", "4", "8", "32"], "correct": 1, "explanation": "Steg 1 i exemplet: '32 - 28 = 4 bitar till host'"},
        {"question": "Hur konverteras 147 i exemplet?", "options": ["64+32+16+8+4+2+1", "128+16+2+1", "128+8+4+2+1+4", "100+40+7"], "correct": 1, "explanation": "Steg 3: '147 = 128 + 16 + 2 + 1'"},
        {"question": "Network ID för 46.84.126.147/28?", "options": ["46.84.126.128", "46.84.126.144", "46.84.126.147", "46.84.126.160"], "correct": 1, "explanation": "Exemplet: 'Network ID = 46.84.126.144'"},
        {"question": "Broadcast för 46.84.126.147/28?", "options": ["46.84.126.145", "46.84.126.158", "46.84.126.159", "46.84.126.255"], "correct": 2, "explanation": "Exemplet: 'Broadcast = 46.84.126.159'"},
        {"question": "Hur många hosts i /28 enligt tabellen?", "options": ["16", "14", "15", "12"], "correct": 1, "explanation": "Prefix-tabellen: '/28 = 14 hosts (2^4-2)'"},
        {"question": "Next Subnet för 46.84.126.147/28?", "options": ["46.84.126.158", "46.84.126.159", "46.84.126.160", "46.84.127.0"], "correct": 2, "explanation": "Steg 6: 'Next Subnet = Broadcast + 1 = 159 + 1 = 160'"},
        {"question": "Vad beräknas som 128 + 16 + 8 + 4 + 2 + 1 i exemplet?", "options": ["144 (Network)", "147 (IP)", "159 (Broadcast)", "160 (Next)"], "correct": 2, "explanation": "Steg 5: Broadcast med alla host-bitar = 1"},
    ],
    "hard": [
        {"question": "DevOps-scenariot: 10.0.0.0/24 delas i 4 segment. Vilket prefix?", "options": ["/25", "/26", "/27", "/28"], "correct": 1, "explanation": "Materialet: 'Dela i 4 = /26 (62 adresser var)'"},
        {"question": "Enligt prefix-tabellen: /30 ger hur många hosts?", "options": ["4", "6", "2", "1"], "correct": 2, "explanation": "Tabellen: '/30 = 2 hosts'"},
        {"question": "Varför används /30 enligt materialet?", "options": ["Stora nätverk", "Punkt-till-punkt-länkar", "Multicast", "DNS-servrar"], "correct": 1, "explanation": "Tips: '/30 med bara 2 hosts används för punkt-till-punkt-länkar mellan routrar'"},
        {"question": "Snabbreferensen steg 8 - formel för hosts?", "options": ["2^host-bitar", "2^host-bitar + 2", "2^host-bitar - 2", "host-bitar × 2"], "correct": 2, "explanation": "Snabbreferens: 'Hosts = 2^(host-bitar) - 2'"},
        {"question": "I lådmetoden - vad betyder N vs H?", "options": ["Network/Host - N är låst, H varierar", "Null/High - inget/maxvärde", "Negativ/Halv - minus/dela", "Name/Hash - namn/krypto"], "correct": 0, "explanation": "Materialet: 'N = Nätverksdelen (låst), H = Hostdelen (varierar)'"},
        {"question": "Enligt exemplet: Last Host för 46.84.126.147/28?", "options": ["46.84.126.157", "46.84.126.158", "46.84.126.159", "46.84.126.144"], "correct": 1, "explanation": "Tabell: 'Last Host = Broadcast - 1 = 159 - 1 = 158'"},
    ],
}

# =============================================================================
# HUVUDEXPORT (byggs ut med alla 25 noder)
# =============================================================================

# =============================================================================
# NOD 2: FILSYSTEM & GRUNDKOMMANDON
# Källa: doe25_tentaplugg.py FILSYSTEM_NODE
# Koncept: /etc, /var, /home, ls, cp, find, grep, tar, pipes
# =============================================================================

NOD_02_FLASHCARDS = {
    "easy": [
        # Från "Mental modell: Filsystemet är ett träd"
        {"front": "Linux filsystem - vad är roten?", "back": "/ (slash) - allt börjar här"},
        {"front": "Vad ligger i /etc?", "back": "Konfigurationsfiler"},
        {"front": "Vad ligger i /var/log?", "back": "Loggfiler"},
        {"front": "Vad ligger i /home?", "back": "Användarnas hemkataloger"},
        {"front": "Vad är /tmp?", "back": "Tillfälliga filer - rensas vid omstart!"},
        # Navigering från materialet
        {"front": "Kommando: Var är jag?", "back": "pwd"},
        {"front": "Kommando: Gå hem?", "back": "cd ~ eller bara cd"},
        {"front": "Kommando: Upp en nivå?", "back": "cd .."},
        {"front": "Kommando: Tillbaka till förra katalogen?", "back": "cd -"},
        {"front": "ls -l visar?", "back": "Long format - alla detaljer"},
    ],
    "medium": [
        # Specifika filer från materialet
        {"front": "/etc/passwd innehåller?", "back": "Alla användare (INTE lösenord!)"},
        {"front": "/etc/shadow innehåller?", "back": "Krypterade lösenord (bara root)"},
        {"front": "/etc/ssh/sshd_config är?", "back": "SSH-serverns konfiguration"},
        {"front": "/var/log/syslog är?", "back": "Systemloggen"},
        {"front": "/var/log/auth.log visar?", "back": "Inloggningsförsök"},
        # Kommandon från materialet
        {"front": "ls -a visar?", "back": "Dolda filer (börjar med .)"},
        {"front": "ls -lh betyder?", "back": "Long + Human readable (KB, MB)"},
        {"front": "mkdir -p a/b/c gör?", "back": "Skapar hela katalogkedjan"},
        {"front": "cp -r krävs för?", "back": "Kopiera kataloger (rekursivt)"},
        {"front": "rm -r gör?", "back": "Tar bort katalog med allt innehåll"},
    ],
    "hard": [
        # find och grep från materialet
        {"front": "Hitta alla .log-filer i /var/log?", "back": "find /var/log -name \"*.log\""},
        {"front": "Hitta kataloger som heter config?", "back": "find /home -type d -name \"config\""},
        {"front": "Hitta filer större än 100MB?", "back": "find /tmp -size +100M"},
        {"front": "Sök rekursivt efter 'password' i /etc?", "back": "grep -r \"password\" /etc/"},
        {"front": "grep -i betyder?", "back": "Case-insensitive sökning"},
        {"front": "grep -n visar?", "back": "Radnummer i output"},
        {"front": "grep -v gör?", "back": "Visa allt UTOM matchningen (invert)"},
        # tar och pipes
        {"front": "Skapa gzippad backup?", "back": "tar -czvf backup.tar.gz katalog/"},
        {"front": "Extrahera tar.gz?", "back": "tar -xzvf backup.tar.gz"},
        {"front": "Följ loggfil live?", "back": "tail -f /var/log/syslog"},
    ],
}

NOD_02_QUIZ = {
    "easy": [
        {"question": "Enligt materialet - vad innehåller /etc?", "options": ["Loggfiler", "Konfigurationsfiler", "Användardata", "Temporära filer"], "correct": 1, "explanation": "Materialet: '/etc - Configuration Central'"},
        {"question": "Var finns systemloggen enligt materialet?", "options": ["/etc/syslog", "/var/log/syslog", "/home/log", "/tmp/syslog"], "correct": 1, "explanation": "Materialet: '/var/log/syslog - Systemloggen'"},
        {"question": "Vad gör pwd enligt materialet?", "options": ["Byter lösenord", "Visar var du är", "Skapar katalog", "Tar bort fil"], "correct": 1, "explanation": "Navigering: 'pwd - Var är jag?'"},
        {"question": "Hur går du hem enligt materialet?", "options": ["cd /", "cd home", "cd ~", "cd root"], "correct": 2, "explanation": "Navigering: 'cd ~ - Hem'"},
        {"question": "ls -l visar enligt materialet?", "options": ["Bara namn", "Dolda filer", "Long - alla detaljer", "Storlek i MB"], "correct": 2, "explanation": "Lista filer: 'ls -l - Long - alla detaljer'"},
        {"question": "Vad händer med /tmp vid omstart?", "options": ["Ingenting", "Rensas", "Backas upp", "Krypteras"], "correct": 1, "explanation": "Materialet: '/tmp - Rensas vid omstart!'"},
        {"question": "ls -a visar?", "options": ["Alla detaljer", "Dolda filer", "Arkiverade", "Admin-filer"], "correct": 1, "explanation": "Materialet: 'ls -a - Visa dolda (börjar med .)'"},
    ],
    "medium": [
        {"question": "Enligt materialet - var finns SSH-config?", "options": ["/etc/ssh/config", "/etc/sshd_config", "/etc/ssh/sshd_config", "/var/ssh/config"], "correct": 2, "explanation": "Materialet: '/etc/ssh/sshd_config - SSH-serverns config'"},
        {"question": "Vad gör mkdir -p a/b/c?", "options": ["Skapar bara a", "Skapar hela kedjan", "Ger fel om a finns", "Tar bort befintliga"], "correct": 1, "explanation": "Materialet: 'mkdir -p a/b/c - Skapa hela kedjan'"},
        {"question": "Varför behövs -r vid cp av katalog?", "options": ["Read-only", "Rekursivt (inkludera innehåll)", "Root-access", "Remote"], "correct": 1, "explanation": "Materialet: 'cp -r katalog/ backup/ - Kopiera katalog (MÅSTE ha -r!)'"},
        {"question": "tail -f gör enligt materialet?", "options": ["Visar första rader", "FÖLJ filen live", "Filtrerar", "Formaterar"], "correct": 1, "explanation": "Materialet: 'tail -f /var/log/syslog - FÖLJ filen live'"},
        {"question": "Hur skapar du gzippad backup enligt materialet?", "options": ["tar -xvf", "tar -tvf", "tar -czvf", "tar -cvf"], "correct": 2, "explanation": "Materialet: 'tar -czvf backup.tar.gz katalog/ - Med gzip'"},
        {"question": "/etc/passwd innehåller lösenord?", "options": ["Ja, krypterade", "Ja, i klartext", "Nej, INTE lösenord", "Bara admin-lösenord"], "correct": 2, "explanation": "Materialet: '/etc/passwd - Alla användare (INTE lösenord!)'"},
        {"question": "df -h visar?", "options": ["Dolda filer", "Diskutrymme human readable", "Fil-detaljer", "Directory first"], "correct": 1, "explanation": "Materialet: 'df -h - Visa partitioner'"},
    ],
    "hard": [
        {"question": "Hitta alla .log-filer i /var/log enligt materialet?", "options": ["grep .log /var/log", "find /var/log -name \"*.log\"", "ls /var/log/*.log", "search /var/log .log"], "correct": 1, "explanation": "Materialet: 'find /var/log -name \"*.log\"'"},
        {"question": "Sök rekursivt i /etc enligt materialet?", "options": ["grep \"text\" /etc/*", "grep -r \"text\" /etc/", "find /etc -grep text", "search -r /etc text"], "correct": 1, "explanation": "Materialet: 'grep -r \"password\" /etc/ - Sök rekursivt'"},
        {"question": "grep -v gör enligt materialet?", "options": ["Verbose output", "Visa allt UTOM matchningen", "Verifiera syntax", "Version info"], "correct": 1, "explanation": "Materialet: 'grep -v \"debug\" fil.txt - Visa allt UTOM \"debug\"'"},
        {"question": "Pipe-exemplet från materialet?", "options": ["cat fil && grep error", "cat fil > grep error", "cat fil | grep \"error\" | head -20", "grep error < cat fil"], "correct": 2, "explanation": "Materialet: 'cat fil | grep \"error\" | head -20 - Kedja kommandon'"},
        {"question": "Skillnad > vs >> enligt materialet?", "options": ["Ingen skillnad", "> skriver över, >> lägger till", "> läser, >> skriver", "> pipe, >> redirect"], "correct": 1, "explanation": "Materialet: '> - SKRIVER ÖVER!, >> - Lägg till'"},
        {"question": "Kolla storlek på mapp enligt materialet?", "options": ["ls -s /var/log", "du -sh /var/log", "df /var/log", "size /var/log"], "correct": 1, "explanation": "Materialet: 'du -sh /var/log - Hur stor är mappen?'"},
    ],
}

# =============================================================================
# NOD 5: REGEX (REGULJÄRA UTTRYCK)
# Källa: nod_regex.py
# Koncept: Metacharacters, [brackets], POSIX, BRE vs ERE, grep -E
# =============================================================================

NOD_05_FLASHCARDS = {
    "easy": [
        {"front": "Regex - vad betyder . (punkt)?", "back": "Matchar ETT valfritt tecken"},
        {"front": "Regex - vad betyder * (asterisk)?", "back": "Noll eller fler av föregående"},
        {"front": "Regex - vad betyder ^ (caret)?", "back": "Radens BÖRJAN"},
        {"front": "Regex - vad betyder $ (dollar)?", "back": "Radens SLUT"},
        {"front": "[abc] matchar?", "back": "Exakt ETT tecken: a, b eller c"},
        {"front": "[^abc] matchar?", "back": "ETT tecken som INTE är a, b eller c"},
        {"front": "[a-z] matchar?", "back": "En liten bokstav (range)"},
        {"front": "[0-9] matchar?", "back": "En siffra (range)"},
        {"front": "grep -E aktiverar?", "back": "Extended Regular Expressions (ERE)"},
        {"front": "grep -i gör?", "back": "Case-insensitive sökning"},
    ],
    "medium": [
        {"front": "+ i regex betyder?", "back": "En eller fler av föregående (ERE)"},
        {"front": "? i regex betyder?", "back": "Noll eller en av föregående (ERE)"},
        {"front": "Skillnad BRE vs ERE?", "back": "ERE: +?|() fungerar direkt. BRE: kräver backslash"},
        {"front": "[[:alpha:]] matchar?", "back": "Alla bokstäver (POSIX-klass)"},
        {"front": "[[:digit:]] matchar?", "back": "Alla siffror 0-9 (POSIX-klass)"},
        {"front": "[[:alnum:]] matchar?", "back": "Bokstäver OCH siffror"},
        {"front": "[[:space:]] matchar?", "back": "Mellanslag, tab, newline"},
        {"front": "grep -v gör?", "back": "Visar rader som INTE matchar (invert)"},
        {"front": "grep -c gör?", "back": "Räknar matchande rader"},
        {"front": "grep -n gör?", "back": "Visar radnummer"},
    ],
    "hard": [
        {"front": "Matcha siffra med BRE?", "back": "[0-9] eller [[:digit:]]"},
        {"front": "Matcha email-struktur med ERE?", "back": "[a-z]+@[a-z]+\\.[a-z]+"},
        {"front": "grep -E vs egrep?", "back": "Samma sak - båda ERE"},
        {"front": "Regex i bash: [[ $var =~ ^[0-9]+$ ]] testar?", "back": "Om var BARA innehåller siffror"},
        {"front": "Escape punkt bokstavligt i regex?", "back": "\\. (backslash punkt)"},
        {"front": "grep -r gör?", "back": "Söker rekursivt i kataloger"},
        {"front": "grep -w gör?", "back": "Matchar hela ord"},
        {"front": "grep -l gör?", "back": "Visar bara filnamn"},
        {"front": "^$ matchar?", "back": "Tom rad"},
        {"front": ".* matchar?", "back": "Vad som helst (noll eller fler av vad som helst)"},
    ],
}

NOD_05_QUIZ = {
    "easy": [
        {"question": "Vad matchar . (punkt) i regex?", "options": ["Bokstavlig punkt", "ETT valfritt tecken", "Noll tecken", "Radens slut"], "correct": 1, "explanation": "Materialet: '. = Matchar ETT valfritt tecken'"},
        {"question": "Vad betyder ^ i regex?", "options": ["Exponent", "Radens början", "Negation", "Specialtecken"], "correct": 1, "explanation": "Materialet: '^ = Radens BÖRJAN'"},
        {"question": "Vad betyder $ i regex?", "options": ["Variabel", "Radens slut", "Dollar", "Kommentar"], "correct": 1, "explanation": "Materialet: '$ = Radens SLUT'"},
        {"question": "[abc] matchar?", "options": ["abc", "a eller b eller c", "aaa", "Alla tre"], "correct": 1, "explanation": "Materialet: '[abc] = ETT tecken: a, b eller c'"},
        {"question": "grep -i gör?", "options": ["Invers", "Case-insensitive", "Interactive", "Include"], "correct": 1, "explanation": "Flaggtabellen: '-i = Case-insensitive'"},
        {"question": "[^abc] matchar?", "options": ["abc", "Tecken som INTE är a,b,c", "Början med abc", "Slutar med abc"], "correct": 1, "explanation": "Materialet: '[^abc] = ETT tecken som INTE är a, b eller c'"},
        {"question": "Vilken flagga aktiverar ERE?", "options": ["-e", "-E", "-r", "-x"], "correct": 1, "explanation": "Materialet: 'grep -E = Extended Regular Expressions'"},
    ],
    "medium": [
        {"question": "+ i ERE betyder?", "options": ["Noll eller fler", "En eller fler", "Exakt en", "Addition"], "correct": 1, "explanation": "Materialet: '+ = En eller fler av föregående'"},
        {"question": "Skillnad BRE vs ERE enligt materialet?", "options": ["Ingen skillnad", "ERE: +?|() direkt, BRE: backslash", "BRE är bättre", "ERE är långsammare"], "correct": 1, "explanation": "Materialet: 'ERE: +, ?, |, () fungerar direkt utan escape'"},
        {"question": "[[:alpha:]] matchar?", "options": ["Bara a", "Alla bokstäver", "Alfabetisk ordning", "Alpha-tecken"], "correct": 1, "explanation": "POSIX-tabell: '[[:alpha:]] = Alla bokstäver'"},
        {"question": "grep -c gör?", "options": ["Case-sensitive", "Räknar matchande rader", "Skapar fil", "Concatenate"], "correct": 1, "explanation": "Flaggtabellen: '-c = Räkna matchande rader'"},
        {"question": "grep -v gör?", "options": ["Verbose", "Visar ICKE-matchande rader", "Version", "Validate"], "correct": 1, "explanation": "Flaggtabellen: '-v = Visa rader som INTE matchar'"},
        {"question": "[[:digit:]] är samma som?", "options": ["[a-z]", "[0-9]", "[A-Z]", "[[:alpha:]]"], "correct": 1, "explanation": "POSIX-tabell: '[[:digit:]] = Siffror (0-9)'"},
        {"question": "grep -n visar?", "options": ["Antal matchningar", "Radnummer", "Filnamn", "Negation"], "correct": 1, "explanation": "Flaggtabellen: '-n = Visa radnummer'"},
    ],
    "hard": [
        {"question": "[[ $var =~ ^[0-9]+$ ]] testar?", "options": ["Om var börjar med siffra", "Om var BARA innehåller siffror", "Om var är tom", "Om var är definierad"], "correct": 1, "explanation": "Materialet: 'Testar om variabel matchar regex'"},
        {"question": "Hur escape:ar du punkt bokstavligt?", "options": ["[.]", "\\.", "$$.", "&."], "correct": 1, "explanation": "Materialet: '\\. = Bokstavlig punkt'"},
        {"question": "Vad matchar ^$?", "options": ["Allt", "Tom rad", "Början och slut", "Ingenting"], "correct": 1, "explanation": "^ = början, $ = slut, inget mellan = tom rad"},
        {"question": "grep -r gör?", "options": ["Reverse", "Söker rekursivt", "Raw output", "Replace"], "correct": 1, "explanation": "Flaggtabellen: '-r = Sök rekursivt i kataloger'"},
        {"question": ".* matchar?", "options": ["Punkt-asterisk", "Vad som helst", "Inget", "Bara punkter"], "correct": 1, "explanation": ". = ett tecken, * = noll eller fler → vad som helst"},
        {"question": "grep -w gör?", "options": ["Wide output", "Matchar hela ord", "Write mode", "Warning"], "correct": 1, "explanation": "Flaggtabellen: '-w = Matcha hela ord'"},
    ],
}

# =============================================================================
# NOD 6: SED (STREAM EDITOR)
# Källa: nod_sed.py
# Koncept: s/old/new/g, -i flaggan, address patterns, delete
# =============================================================================

NOD_06_FLASHCARDS = {
    "easy": [
        {"front": "sed står för?", "back": "Stream Editor"},
        {"front": "Grundkommando för ersättning?", "back": "sed 's/old/new/' fil"},
        {"front": "g i s/old/new/g betyder?", "back": "Global - ersätt ALLA på raden (inte bara första)"},
        {"front": "Utan g - vad händer?", "back": "Bara FÖRSTA matchningen per rad ersätts"},
        {"front": "-i flaggan gör?", "back": "Ändrar filen DIREKT (in-place)"},
        {"front": "Varför -i.bak rekommenderas?", "back": "Skapar backup innan ändring"},
        {"front": "sed 'd' kommandot gör?", "back": "Delete - tar bort rader"},
        {"front": "Hur tar du bort rad 5?", "back": "sed '5d' fil"},
        {"front": "Hur tar du bort rad 2-4?", "back": "sed '2,4d' fil"},
        {"front": "Hur tar du bort tomma rader?", "back": "sed '/^$/d' fil"},
    ],
    "medium": [
        {"front": "i efter s/ gör?", "back": "Case-insensitive ersättning"},
        {"front": "sed med regex-mönster?", "back": "sed '/pattern/s/old/new/g' fil"},
        {"front": "Ersätt bara på rad 3?", "back": "sed '3s/old/new/g' fil"},
        {"front": "Ersätt rad 1-5?", "back": "sed '1,5s/old/new/g' fil"},
        {"front": "Ersätt från rad 3 till slutet?", "back": "sed '3,$s/old/new/g' fil"},
        {"front": "Ta bort rader som matchar pattern?", "back": "sed '/pattern/d' fil"},
        {"front": "Alternativ delimiter istället för /?", "back": "Kan använda | # @ etc: sed 's|old|new|g'"},
        {"front": "Varför alternativ delimiter?", "back": "Slipper escape:a / i paths"},
        {"front": "Ersätt /usr/local med /opt?", "back": "sed 's|/usr/local|/opt|g' fil"},
        {"front": "sed -n 'p' gör?", "back": "Skriver bara ut matchande rader"},
    ],
    "hard": [
        {"front": "Ersätt ENDAST om raden innehåller 'error'?", "back": "sed '/error/s/old/new/g' fil"},
        {"front": "Ta bort kommentarsrader (börjar med #)?", "back": "sed '/^#/d' fil"},
        {"front": "Ta bort tomma och comment-rader?", "back": "sed '/^$/d; /^#/d' fil"},
        {"front": "& i replacement betyder?", "back": "Hela matchningen återanvänds"},
        {"front": "sed 's/word/[&]/g' med 'hello'?", "back": "[hello] - & ersätts av matchningen"},
        {"front": "Capture groups i sed?", "back": "\\( \\) för att fånga, \\1 för att referera"},
        {"front": "Byt ordning på två ord?", "back": "sed 's/\\(word1\\) \\(word2\\)/\\2 \\1/'"},
        {"front": "sed -e används för?", "back": "Flera sed-kommandon i följd"},
        {"front": "Lägg till text före varje rad?", "back": "sed 's/^/PREFIX: /' fil"},
        {"front": "Lägg till text efter varje rad?", "back": "sed 's/$/ SUFFIX/' fil"},
    ],
}

NOD_06_QUIZ = {
    "easy": [
        {"question": "Vad står sed för?", "options": ["Search Editor", "Stream Editor", "String Editor", "System Editor"], "correct": 1, "explanation": "Materialet: 'sed = Stream EDitor'"},
        {"question": "g i s/old/new/g betyder?", "options": ["Get", "Global - alla matchningar", "Group", "Grep"], "correct": 1, "explanation": "Materialet: 'g = Global (ALLA på raden)'"},
        {"question": "Vad händer utan g i s/old/new/?", "options": ["Ingenting ersätts", "Bara första på raden", "Alla ersätts", "Fel"], "correct": 1, "explanation": "Materialet: 'Utan g: Bara FÖRSTA matchningen'"},
        {"question": "sed -i gör?", "options": ["Interactive", "Ändrar filen direkt", "Input mode", "Ignore"], "correct": 1, "explanation": "Materialet: '-i = Ändra filen DIREKT'"},
        {"question": "Varför sed -i.bak?", "options": ["Snabbare", "Skapar backup", "Backspace", "Binary"], "correct": 1, "explanation": "Materialet: '-i.bak = Backup FÖRST'"},
        {"question": "sed 'd' gör?", "options": ["Download", "Delete rad", "Duplicate", "Debug"], "correct": 1, "explanation": "Materialet: 'd = Delete (ta bort rad)'"},
        {"question": "Hur tar du bort rad 5?", "options": ["sed 'del 5'", "sed '5d'", "sed -d 5", "sed rm 5"], "correct": 1, "explanation": "Materialet: 'sed '5d' fil.txt'"},
    ],
    "medium": [
        {"question": "i efter s/ gör?", "options": ["Insert", "Case-insensitive", "In-place", "Invert"], "correct": 1, "explanation": "Materialet: 'i = Case-insensitive'"},
        {"question": "sed '3s/old/new/' gör?", "options": ["Ersätter 3 gånger", "Ersätter bara rad 3", "Ersätter rad 1-3", "Syntaxfel"], "correct": 1, "explanation": "Materialet: '3s/old/new/g = Bara på rad 3'"},
        {"question": "Alternativ delimiter - varför?", "options": ["Snabbare", "Slipper escape:a /", "Säkrare", "Standard"], "correct": 1, "explanation": "Materialet: 'Använd annan delimiter: s|/path|/new|g'"},
        {"question": "Ta bort rader som matchar 'debug'?", "options": ["sed 'debug d'", "sed '/debug/d'", "sed -d debug", "sed rm debug"], "correct": 1, "explanation": "Materialet: 'sed '/debug/d' fil.txt'"},
        {"question": "sed '/^$/d' tar bort?", "options": ["Alla rader", "Tomma rader", "Kommentarer", "Mellanslag"], "correct": 1, "explanation": "Materialet: '/^$/d = Ta bort tomma rader'"},
        {"question": "$ i sed adress betyder?", "options": ["Dollar", "Sista raden", "Variabel", "Regex slut"], "correct": 1, "explanation": "Materialet: '$ = Sista raden'"},
        {"question": "sed '1,5d' gör?", "options": ["Tar bort rad 1 och 5", "Tar bort rad 1-5", "Behåller 1-5", "Syntaxfel"], "correct": 1, "explanation": "Materialet: '1,5d = Ta bort rad 1-5'"},
    ],
    "hard": [
        {"question": "& i replacement betyder?", "options": ["And", "Ampersand bokstavligt", "Hela matchningen", "Append"], "correct": 2, "explanation": "Materialet: '& = Hela matchningen'"},
        {"question": "sed 's/word/[&]/g' på 'test word here'?", "options": ["test [word] here", "[test word here]", "test [&] here", "Fel"], "correct": 0, "explanation": "& ersätts av matchningen 'word' → [word]"},
        {"question": "Capture groups i sed syntax?", "options": ["() och $1", "(group) och \\1", "\\( \\) och \\1", "{} och &"], "correct": 2, "explanation": "Materialet: 'BRE kräver \\( \\) för grupper'"},
        {"question": "Ta bort kommentarsrader (#)?", "options": ["sed '/#/d'", "sed '/^#/d'", "sed 'd#'", "sed -c '#'"], "correct": 1, "explanation": "Materialet: '/^#/d = Rader som BÖRJAR med #'"},
        {"question": "Lägg till PREFIX före varje rad?", "options": ["sed 'PREFIX'", "sed 's/$/PREFIX/'", "sed 's/^/PREFIX/'", "sed '^PREFIX'"], "correct": 2, "explanation": "^ = radens början, ersätter med PREFIX"},
        {"question": "sed -n 'p' gör?", "options": ["Skriver ut allt", "Skriver bara matchande", "Print mode", "Ingenting"], "correct": 1, "explanation": "Materialet: '-n med p = Skriv bara matchande'"},
    ],
}

# =============================================================================
# NOD 7: AWK
# Källa: nod_awk.py
# Koncept: $1-$NF, NR/NF, -F separator, BEGIN/END, pattern matching
# =============================================================================

NOD_07_FLASHCARDS = {
    "easy": [
        {"front": "awk - vad är $0?", "back": "Hela raden"},
        {"front": "awk - vad är $1?", "back": "Första fältet"},
        {"front": "awk - vad är $NF?", "back": "Sista fältet"},
        {"front": "NF i awk betyder?", "back": "Number of Fields - antal fält på raden"},
        {"front": "NR i awk betyder?", "back": "Number of Records - radnummer"},
        {"front": "-F: i awk gör?", "back": "Sätter : som fältseparator"},
        {"front": "Standard fältseparator i awk?", "back": "Mellanslag/tab"},
        {"front": "awk '{print $1}' gör?", "back": "Skriver ut första fältet på varje rad"},
        {"front": "awk '/pattern/' gör?", "back": "Skriver rader som matchar pattern"},
        {"front": "awk 'NR==3' gör?", "back": "Skriver bara rad 3"},
    ],
    "medium": [
        {"front": "Skriv ut rad 2-4?", "back": "awk 'NR>=2 && NR<=4'"},
        {"front": "Skriv ut om fält 3 > 100?", "back": "awk '$3 > 100'"},
        {"front": "Summera kolumn 2?", "back": "awk '{sum+=$2} END{print sum}'"},
        {"front": "BEGIN block körs?", "back": "En gång INNAN filbearbetning"},
        {"front": "END block körs?", "back": "En gång EFTER filbearbetning"},
        {"front": "printf i awk för?", "back": "Formaterad output (som C)"},
        {"front": "awk printf '%-10s' betyder?", "back": "Vänsterjusterad sträng, 10 tecken bred"},
        {"front": "awk '/error|warning/' gör?", "back": "Matchar rader med error ELLER warning"},
        {"front": "$NF-1 ger?", "back": "Näst sista fältet"},
        {"front": "awk -F, för CSV?", "back": "Komma som separator"},
    ],
    "hard": [
        {"front": "Skriv username från /etc/passwd?", "back": "awk -F: '{print $1}' /etc/passwd"},
        {"front": "Räkna rader?", "back": "awk 'END{print NR}' fil"},
        {"front": "Genomsnitt av kolumn 3?", "back": "awk '{sum+=$3; n++} END{print sum/n}'"},
        {"front": "Villkor: print om $1=='admin'?", "back": "awk '$1==\"admin\" {print}'"},
        {"front": "~ operator i awk?", "back": "Regex-matchning: $1 ~ /pattern/"},
        {"front": "!~ operator i awk?", "back": "Regex INTE-matchning"},
        {"front": "Omdirigera awk output?", "back": "awk '{print > \"fil.txt\"}'"},
        {"front": "awk -v var=value?", "back": "Skicka shell-variabel till awk"},
        {"front": "Längd på fält?", "back": "length($1)"},
        {"front": "OFS i awk?", "back": "Output Field Separator"},
    ],
}

NOD_07_QUIZ = {
    "easy": [
        {"question": "$0 i awk är?", "options": ["Första fältet", "Sista fältet", "Hela raden", "Radnummer"], "correct": 2, "explanation": "Materialet: '$0 = Hela raden'"},
        {"question": "$NF i awk är?", "options": ["Number Field", "Sista fältet", "Antal fält", "Ny fil"], "correct": 1, "explanation": "Materialet: '$NF = Sista fältet'"},
        {"question": "NR i awk betyder?", "options": ["New Record", "Number of Records (radnummer)", "Next Row", "No Result"], "correct": 1, "explanation": "Materialet: 'NR = Radnummer'"},
        {"question": "NF i awk betyder?", "options": ["New Field", "Number of Fields", "Next File", "No Filter"], "correct": 1, "explanation": "Materialet: 'NF = Antal fält på raden'"},
        {"question": "awk -F: sätter?", "options": ["Filnamn", ": som fältseparator", "Format", "Filter"], "correct": 1, "explanation": "Materialet: '-F: = Sätt : som separator'"},
        {"question": "Standard fältseparator i awk?", "options": ["Komma", "Tab", "Mellanslag/tab", "Semikolon"], "correct": 2, "explanation": "Materialet: 'Default: mellanslag och tab'"},
        {"question": "awk '{print $1}' gör?", "options": ["Skriver rad 1", "Skriver första fältet", "Skriver allt", "Skriver $1 bokstavligt"], "correct": 1, "explanation": "Materialet: '{print $1} = Skriv första fältet'"},
    ],
    "medium": [
        {"question": "BEGIN block körs?", "options": ["Varje rad", "Innan filbearbetning", "Efter filbearbetning", "Vid matchning"], "correct": 1, "explanation": "Materialet: 'BEGIN körs EN GÅNG innan filbearbetning'"},
        {"question": "END block körs?", "options": ["Varje rad", "Innan filbearbetning", "Efter filbearbetning", "Aldrig"], "correct": 2, "explanation": "Materialet: 'END körs EN GÅNG efter filbearbetning'"},
        {"question": "awk '$3 > 100' gör?", "options": ["Skriver rad 3", "Skriver om fält 3 > 100", "Adderar 100", "Fel"], "correct": 1, "explanation": "Materialet: 'Villkor: skriv rad om fält 3 > 100'"},
        {"question": "Summera kolumn 2 med awk?", "options": ["awk 'sum $2'", "awk '{sum+=$2} END{print sum}'", "awk '$2++'", "awk 'total $2'"], "correct": 1, "explanation": "Materialet: 'awk '{sum+=$2} END{print sum}''"},
        {"question": "awk printf '%-10s' betyder?", "options": ["Höger 10", "Vänsterjusterad 10 tecken", "10 mellanslag", "Minus 10"], "correct": 1, "explanation": "Materialet: '- = Vänsterjustera'"},
        {"question": "Skriv bara rad 5?", "options": ["awk '5'", "awk 'NR==5'", "awk '$5'", "awk 'row 5'"], "correct": 1, "explanation": "Materialet: 'NR==5 = Endast rad 5'"},
        {"question": "$NF-1 ger?", "options": ["Sista -1", "Näst sista fältet", "Fel", "Antal -1"], "correct": 1, "explanation": "Materialet: '$(NF-1) = Näst sista fältet'"},
    ],
    "hard": [
        {"question": "Username från /etc/passwd?", "options": ["awk '{print $1}' /etc/passwd", "awk -F: '{print $1}' /etc/passwd", "awk '$1' /etc/passwd", "grep user /etc/passwd"], "correct": 1, "explanation": "passwd är :-separerad, $1 är username"},
        {"question": "Räkna totalt antal rader?", "options": ["awk 'NR'", "awk 'END{print NR}'", "awk 'count++'", "awk '$NR'"], "correct": 1, "explanation": "Materialet: 'END{print NR} = Totalt antal rader'"},
        {"question": "~ operator i awk gör?", "options": ["Hem-katalog", "Regex-matchning", "Negation", "Tilde"], "correct": 1, "explanation": "Materialet: '~ = Matchar regex'"},
        {"question": "awk -v var=5 skickar?", "options": ["Version 5", "Shell-variabel till awk", "Verbose", "Validate"], "correct": 1, "explanation": "Materialet: '-v = Skicka variabel till awk'"},
        {"question": "OFS i awk är?", "options": ["Output File", "Output Field Separator", "Open File", "Original FS"], "correct": 1, "explanation": "OFS = Output Field Separator"},
        {"question": "length($1) returnerar?", "options": ["Antal fält", "Längd på första fältet", "Radlängd", "Fillängd"], "correct": 1, "explanation": "length() returnerar stränglängd"},
    ],
}

# =============================================================================
# NOD 8: VILLKOR (IF/ELIF/ELSE/CASE)
# Källa: nod_villkor.py
# Koncept: [ ] vs [[ ]], strängjämförelser, nummerjämförelser, filtester, case
# =============================================================================

NOD_08_FLASHCARDS = {
    "easy": [
        {"front": "if-sats grundsyntax?", "back": "if [ villkor ]; then ... fi"},
        {"front": "KRITISKT: mellanslag i if-sats?", "back": "MÅSTE ha mellanslag efter [ och före ]"},
        {"front": "[ ] vs [[ ]] - vilken rekommenderas?", "back": "[[ ]] - kraftfullare och säkrare"},
        {"front": "== i villkor testar?", "back": "Stränglikhet"},
        {"front": "-eq i villkor testar?", "back": "Nummerlikhet (equal)"},
        {"front": "-ne i villkor betyder?", "back": "Not equal (nummer)"},
        {"front": "-lt i villkor betyder?", "back": "Less than (nummer)"},
        {"front": "-gt i villkor betyder?", "back": "Greater than (nummer)"},
        {"front": "-z \"$var\" testar?", "back": "Om variabeln är TOM (zero)"},
        {"front": "-n \"$var\" testar?", "back": "Om variabeln INTE är tom (non-zero)"},
    ],
    "medium": [
        {"front": "-f fil testar?", "back": "Är vanlig fil (file)"},
        {"front": "-d katalog testar?", "back": "Är katalog (directory)"},
        {"front": "-e fil testar?", "back": "Finns (exists)"},
        {"front": "-r fil testar?", "back": "Är läsbar (readable)"},
        {"front": "-w fil testar?", "back": "Är skrivbar (writable)"},
        {"front": "-x fil testar?", "back": "Är körbar (executable)"},
        {"front": "&& inom [[ ]] betyder?", "back": "OCH (båda sanna)"},
        {"front": "|| inom [[ ]] betyder?", "back": "ELLER (minst en sann)"},
        {"front": "! framför villkor?", "back": "Negerar (INTE)"},
        {"front": "Testa om root? (EUID)", "back": "[[ $EUID -eq 0 ]]"},
    ],
    "hard": [
        {"front": "case-sats grundsyntax?", "back": "case $var in mönster) cmd ;; esac"},
        {"front": "|  i case-mönster?", "back": "OR: ja|Ja|JA) matchar alla tre"},
        {"front": "*) i case?", "back": "Default - fångar allt annat"},
        {"front": "*.txt) i case?", "back": "Wildcard - alla .txt-filer"},
        {"front": ";; i case?", "back": "Avslutar varje mönster-block"},
        {"front": "esac?", "back": "case baklänges - avslutar case-satsen"},
        {"front": "-s fil testar?", "back": "Har innehåll (size > 0)"},
        {"front": "-L fil testar?", "back": "Är symbolisk länk"},
        {"front": "[[ =~ ]] gör?", "back": "Regex-matchning i villkor"},
        {"front": "-le och -ge?", "back": "Less/Greater or Equal"},
    ],
}

NOD_08_QUIZ = {
    "easy": [
        {"question": "Korrekt if-syntax enligt materialet?", "options": ["if [villkor]", "if [ villkor ]; then", "if (villkor)", "if villkor then"], "correct": 1, "explanation": "Materialet: 'if [ villkor ]; then ... fi'"},
        {"question": "Mellanslag i [ $x -eq 5 ] - varför viktigt?", "options": ["Ser snyggare ut", "MÅSTE finnas efter [ och före ]", "Spelar ingen roll", "Bara för läsbarhet"], "correct": 1, "explanation": "Materialet: 'KRITISKT: Mellanslag!'"},
        {"question": "-eq testar?", "options": ["Strängar", "Nummer", "Filer", "Kataloger"], "correct": 1, "explanation": "Materialet: '-eq = Equal (nummer)'"},
        {"question": "== i [[ ]] testar?", "options": ["Nummer", "Strängar", "Regex", "Filer"], "correct": 1, "explanation": "Materialet: '== = Lika med (strängar)'"},
        {"question": "-z testar om variabel är?", "options": ["Noll", "Tom", "Definierad", "Nummer"], "correct": 1, "explanation": "Materialet: '-z = Tom sträng (zero)'"},
        {"question": "-f testar om?", "options": ["Fil finns", "Är vanlig fil", "Är folder", "Är tom"], "correct": 1, "explanation": "Materialet: '-f = Är vanlig fil (file)'"},
        {"question": "Avslutar if-sats?", "options": ["end", "fi", "endif", "done"], "correct": 1, "explanation": "Materialet: 'fi - avslutar if-satsen'"},
    ],
    "medium": [
        {"question": "-d testar?", "options": ["Delete", "Är katalog", "Är disk", "Datum"], "correct": 1, "explanation": "Materialet: '-d = Är katalog (directory)'"},
        {"question": "-r testar?", "options": ["Recursive", "Läsbar", "Running", "Root"], "correct": 1, "explanation": "Materialet: '-r = Läsbar (readable)'"},
        {"question": "&& inom [[ ]]?", "options": ["Pipe", "OCH", "Append", "Background"], "correct": 1, "explanation": "Materialet: '&& = Båda sanna'"},
        {"question": "|| inom [[ ]]?", "options": ["Pipe", "ELLER", "Absolut", "Or not"], "correct": 1, "explanation": "Materialet: '|| = Minst en sann'"},
        {"question": "Kolla om root enligt materialet?", "options": ["$USER == root", "$EUID -eq 0", "$UID == 0", "whoami == root"], "correct": 1, "explanation": "Materialet: '[[ \"$EUID\" -ne 0 ]]'"},
        {"question": "-x testar?", "options": ["Exists", "Executable", "Extended", "External"], "correct": 1, "explanation": "Materialet: '-x = Körbar (executable)'"},
        {"question": "! framför villkor gör?", "options": ["Utropstecken", "Negerar", "Force", "Fel"], "correct": 1, "explanation": "Materialet: '! = Negera'"},
    ],
    "hard": [
        {"question": "case-sats avslutas med?", "options": ["endcase", "esac", "done", "fi"], "correct": 1, "explanation": "Materialet: 'esac - avslutar case'"},
        {"question": ";; i case gör?", "options": ["Kommentar", "Avslutar block", "Fortsätter", "Syntax"], "correct": 1, "explanation": "Materialet: ';;  - avslutar varje fall'"},
        {"question": "*) i case?", "options": ["Multiplication", "Default case", "All files", "Comment"], "correct": 1, "explanation": "Materialet: '*) = default-kommando'"},
        {"question": "ja|Ja|JA) i case matchar?", "options": ["Bara ja", "ja Ja JA", "Alla varianter", "Pipe"], "correct": 2, "explanation": "Materialet: 'ja|Ja|JA = Matchar alla tre'"},
        {"question": "[[ =~ ]] gör?", "options": ["Tilde match", "Regex match", "Approximate", "Not equal"], "correct": 1, "explanation": "Materialet: '[[ =~ ]] = Regex i Bash'"},
        {"question": "-s testar?", "options": ["String", "Fil har innehåll", "Symbolic", "Shell"], "correct": 1, "explanation": "Materialet: '-s = Har innehåll (size > 0)'"},
    ],
}

# =============================================================================
# NOD 9: INTERAKTIVA SKRIPT (READ, VALIDERING)
# Källa: nod_interaktiva_skript.py
# Koncept: read-flaggor, validering, loops för input, select-menyer
# =============================================================================

NOD_09_FLASHCARDS = {
    "easy": [
        {"front": "read-kommandot gör?", "back": "Läser input från användaren"},
        {"front": "read -p \"Prompt: \" var?", "back": "Visar prompt och sparar i var"},
        {"front": "read -s gör?", "back": "Silent - döljer input (lösenord)"},
        {"front": "read -n 1 gör?", "back": "Läser bara 1 tecken"},
        {"front": "read -t 5 gör?", "back": "Timeout efter 5 sekunder"},
        {"front": "read -r gör?", "back": "Raw - ingen backslash-tolkning"},
        {"front": "Varför alltid read -r?", "back": "Bevarar input exakt som den skrivs"},
        {"front": "read -a arr gör?", "back": "Läser till array"},
        {"front": "Validera tom input?", "back": "[[ -z \"$var\" ]]"},
        {"front": "Validera att input är nummer?", "back": "[[ $var =~ ^[0-9]+$ ]]"},
    ],
    "medium": [
        {"front": "Läs flera variabler?", "back": "read -p \"För Efter: \" förnamn efternamn"},
        {"front": "Loop tills giltig input - mönster?", "back": "while true; do read; validate; break/continue; done"},
        {"front": "continue i loop gör?", "back": "Hoppar till nästa iteration"},
        {"front": "break i loop gör?", "back": "Avbryter loopen helt"},
        {"front": "select-kommandot gör?", "back": "Skapar numrerad meny automatiskt"},
        {"front": "PS3-variabeln?", "back": "Prompten för select-menyer"},
        {"front": "$REPLY i select?", "back": "Numret användaren skrev"},
        {"front": "Validera ja/nej-svar?", "back": "case med ja|Ja|j|J) mönster"},
        {"front": "Validera mot lista?", "back": "[[ $färg =~ ^(röd|grön|blå)$ ]]"},
        {"front": "Max antal försök - variabel?", "back": "attempt++ med (( attempt < MAX ))"},
    ],
    "hard": [
        {"front": "Funktion för validerad input?", "back": "get_number() { while read; validate; echo; return; done }"},
        {"front": ">&2 i validering?", "back": "Skriver felmeddelande till stderr"},
        {"front": "select-loop avsluta?", "back": "[[ $opt == \"Quit\" ]] && break"},
        {"front": "Kolla om användare finns?", "back": "id \"$user\" &>/dev/null"},
        {"front": "Visa shells från /etc/shells?", "back": "grep -v '^#' /etc/shells"},
        {"front": "Default-värde vid tom input?", "back": "${var:-default}"},
        {"front": "Validera shell mot /etc/shells?", "back": "grep -q \"^$shell$\" /etc/shells"},
        {"front": "echo efter read -s?", "back": "Ny rad behövs (silent ger ingen)"},
        {"front": "Visa antal tecken i lösenord?", "back": "${#password}"},
        {"front": "read returnerar false vid?", "back": "EOF eller timeout"},
    ],
}

NOD_09_QUIZ = {
    "easy": [
        {"question": "read -p gör?", "options": ["Print", "Visar prompt", "Password", "Pause"], "correct": 1, "explanation": "Materialet: '-p = Visa prompt'"},
        {"question": "read -s gör?", "options": ["String", "Silent (dölj input)", "Save", "Stop"], "correct": 1, "explanation": "Materialet: '-s = Silent (dölj input)'"},
        {"question": "read -n 1 gör?", "options": ["Nästa rad", "Läser 1 tecken", "Nummer 1", "Negera"], "correct": 1, "explanation": "Materialet: '-n N = Läs endast N tecken'"},
        {"question": "read -t 5 gör?", "options": ["Tab 5", "Timeout 5 sekunder", "Type 5", "Test 5"], "correct": 1, "explanation": "Materialet: '-t N = Timeout efter N sekunder'"},
        {"question": "Varför read -r rekommenderas?", "options": ["Snabbare", "Raw - bevarar input", "Required", "Recursive"], "correct": 1, "explanation": "Materialet: '-r = Raw (ingen backslash-tolkning)'"},
        {"question": "Kolla om input är tom?", "options": ["[ -e $var ]", "[[ -z \"$var\" ]]", "[ $var == \"\" ]", "test empty"], "correct": 1, "explanation": "Materialet: '[[ -z \"$var\" ]] = tom'"},
        {"question": "read -a gör?", "options": ["Append", "Läser till array", "All", "Add"], "correct": 1, "explanation": "Materialet: '-a = Läs till array'"},
    ],
    "medium": [
        {"question": "Validera att input är nummer?", "options": ["[[ -n $var ]]", "[[ $var =~ ^[0-9]+$ ]]", "[[ $var -eq 0 ]]", "isnum $var"], "correct": 1, "explanation": "Materialet: '[[ \"$var\" =~ ^[0-9]+$ ]]'"},
        {"question": "continue i loop gör?", "options": ["Avslutar", "Hoppar till nästa iteration", "Fortsätter", "Pausar"], "correct": 1, "explanation": "Materialet: 'continue = Hoppa till nästa'"},
        {"question": "break i loop gör?", "options": ["Pausar", "Nästa iteration", "Avbryter loopen", "Fel"], "correct": 2, "explanation": "Materialet: 'break = Avbryt loopen'"},
        {"question": "select skapar?", "options": ["Selectbox", "Numrerad meny", "Dropdown", "Checkbox"], "correct": 1, "explanation": "Materialet: 'select skapar automatiskt numrerade menyer'"},
        {"question": "PS3 variabeln är?", "options": ["Process 3", "Select-prompten", "Path 3", "Shell 3"], "correct": 1, "explanation": "Materialet: 'PS3 = Prompten för select'"},
        {"question": "$REPLY i select innehåller?", "options": ["Valt alternativ", "Numret som skrevs", "Svar", "Reply"], "correct": 1, "explanation": "Materialet: '$REPLY = numret användaren skrev'"},
        {"question": "Felmeddelande till stderr?", "options": [">&1", ">&2", "2>&1", "> stderr"], "correct": 1, "explanation": "Materialet: 'echo \"Fel\" >&2'"},
    ],
    "hard": [
        {"question": "Kolla om användare finns?", "options": ["user exists", "id \"$user\" &>/dev/null", "getent user", "test -u"], "correct": 1, "explanation": "Materialet: 'id \"$username\" &>/dev/null'"},
        {"question": "${#password} returnerar?", "options": ["Hash", "Antal tecken", "Password", "Error"], "correct": 1, "explanation": "Materialet: '${#password} tecken'"},
        {"question": "Validera shell mot /etc/shells?", "options": ["shell in /etc/shells", "grep -q \"^$shell$\" /etc/shells", "test shell", "which $shell"], "correct": 1, "explanation": "Materialet: 'grep -q \"^$user_shell$\" /etc/shells'"},
        {"question": "Echo efter read -s behövs för?", "options": ["Felsökning", "Ny rad", "Säkerhet", "Output"], "correct": 1, "explanation": "Materialet: 'echo # Ny rad efter silent input'"},
        {"question": "read returnerar false vid?", "options": ["Tom input", "EOF eller timeout", "Nummer", "Lång input"], "correct": 1, "explanation": "if read -t 5 returnerar false vid timeout"},
        {"question": "Default vid tom input?", "options": ["${var:=def}", "${var:-default}", "${var:?err}", "${var:+val}"], "correct": 1, "explanation": "Materialet: '${var:-default}'"},
    ],
}

# =============================================================================
# NOD 10: LOOPAR (FOR/WHILE/UNTIL)
# Källa: nod_loopar.py
# Koncept: for-lista, for C-style, while, until, read fil, break/continue
# =============================================================================

NOD_10_FLASHCARDS = {
    "easy": [
        {"front": "for-loop grundsyntax?", "back": "for var in lista; do ... done"},
        {"front": "Loopa över a b c?", "back": "for x in a b c; do echo $x; done"},
        {"front": "Loopa 1-5 med brace?", "back": "for i in {1..5}; do"},
        {"front": "while-loop grundsyntax?", "back": "while [ villkor ]; do ... done"},
        {"front": "while-loop kör när?", "back": "Så länge villkoret är SANT"},
        {"front": "until-loop kör när?", "back": "Tills villkoret blir SANT"},
        {"front": "Oändlig while-loop?", "back": "while true; do ... done"},
        {"front": "break gör?", "back": "Avbryter loopen helt"},
        {"front": "continue gör?", "back": "Hoppar till nästa iteration"},
        {"front": "Loopa alla .txt-filer?", "back": "for f in *.txt; do"},
    ],
    "medium": [
        {"front": "C-style for-loop?", "back": "for ((i=0; i<10; i++)); do"},
        {"front": "Loopa med steg {1..10..2}?", "back": "1, 3, 5, 7, 9 (steg 2)"},
        {"front": "Loopa alla argument?", "back": "for arg in \"$@\"; do"},
        {"front": "Räkna ned i while?", "back": "while [[ $count -gt 0 ]]; do ((count--))"},
        {"front": "Läs fil rad för rad?", "back": "while IFS= read -r rad; do ... done < fil"},
        {"front": "IFS= i read-loop?", "back": "Behåll leading/trailing whitespace"},
        {"front": "read -r i loop?", "back": "Tolka inte backslash som escape"},
        {"front": "break 2 gör?", "back": "Bryter ur TVÅ nästlade loopar"},
        {"front": "Vänta på fil med until?", "back": "until [[ -f fil ]]; do sleep 1; done"},
        {"front": "seq 1 5 genererar?", "back": "1 2 3 4 5 (en per rad)"},
    ],
    "hard": [
        {"front": "Varför \"$@\" med citattecken?", "back": "Bevarar argument med mellanslag korrekt"},
        {"front": "Skillnad $@ vs $*?", "back": "$@ = separata ord, $* = ett ord"},
        {"front": "Processa kommando-output?", "back": "cmd | while read -r line; do"},
        {"front": "Byt filändelse .txt till .bak?", "back": "for f in *.txt; do mv \"$f\" \"${f%.txt}.bak\"; done"},
        {"front": "Räkna errors i loggar?", "back": "errors=$(grep -c \"ERROR\" fil)"},
        {"front": "Testa fil innan loop?", "back": "[[ -f \"$fil\" ]] && process"},
        {"front": "Skippa fil om inte finns?", "back": "[[ ! -f \"$f\" ]] && continue"},
        {"front": "Parallella loopar i och j?", "back": "for ((i=0,j=10; i<j; i++,j--))"},
        {"front": "Until ping lyckas?", "back": "until ping -c 1 host &>/dev/null; do"},
        {"front": "done < fil.txt läser från?", "back": "Fil som input till hela loopen"},
    ],
}

NOD_10_QUIZ = {
    "easy": [
        {"question": "for-loop avslutas med?", "options": ["fi", "done", "end", "esac"], "correct": 1, "explanation": "Materialet: 'for ... do ... done'"},
        {"question": "for i in {1..5} genererar?", "options": ["{1..5}", "1 2 3 4 5", "15", "1-5"], "correct": 1, "explanation": "Materialet: '{1..5} → 1,2,3,4,5'"},
        {"question": "while-loop kör?", "options": ["En gång", "Tills sant", "Medan sant", "Aldrig"], "correct": 2, "explanation": "Materialet: 'while kör så länge villkoret är sant'"},
        {"question": "until-loop kör?", "options": ["Medan sant", "Tills sant", "Aldrig", "En gång"], "correct": 1, "explanation": "Materialet: 'until kör tills villkoret blir sant'"},
        {"question": "break gör?", "options": ["Pausar", "Nästa iteration", "Avbryter loopen", "Fortsätter"], "correct": 2, "explanation": "Materialet: 'break = avbryt loopen helt'"},
        {"question": "continue gör?", "options": ["Avbryter", "Hoppar till nästa iteration", "Pausar", "Avslutar"], "correct": 1, "explanation": "Materialet: 'continue = hoppa till nästa'"},
        {"question": "Oändlig loop?", "options": ["while 1", "while true", "loop forever", "infinite"], "correct": 1, "explanation": "Materialet: 'while true; do'"},
    ],
    "medium": [
        {"question": "C-style for-loop syntax?", "options": ["for i=0 to 10", "for ((i=0; i<10; i++))", "for (i:10)", "for i in range"], "correct": 1, "explanation": "Materialet: 'for ((i=0; i<10; i++))'"},
        {"question": "{0..10..2} genererar?", "options": ["0-10", "0 2 4 6 8 10", "2 4 6 8 10", "0 10 2"], "correct": 1, "explanation": "Materialet: 'steg = 2'"},
        {"question": "Loopa argument korrekt?", "options": ["for arg in $@", "for arg in \"$@\"", "for arg in $*", "for arg in args"], "correct": 1, "explanation": "Materialet: '\"$@\" = alla argument som separata ord'"},
        {"question": "Läs fil rad för rad?", "options": ["for line in file", "while read line < file", "while IFS= read -r rad; do ... done < fil", "read file lines"], "correct": 2, "explanation": "Materialet: 'while IFS= read -r rad; do'"},
        {"question": "IFS= behövs för?", "options": ["Input Field", "Behålla whitespace", "Ignore", "Format"], "correct": 1, "explanation": "Materialet: 'IFS= = Behåll whitespace'"},
        {"question": "break 2 gör?", "options": ["Bryter 2 gånger", "Bryter ur 2 loopar", "Väntar 2 sek", "Fel"], "correct": 1, "explanation": "Materialet: 'break 2 = Bryt ur BÅDA looparna'"},
        {"question": "for f in *.txt itererar?", "options": ["Sträng '*.txt'", "Alla .txt-filer", "Fil *.txt", "Fel"], "correct": 1, "explanation": "Materialet: 'Alla .txt-filer i aktuell katalog'"},
    ],
    "hard": [
        {"question": "Skillnad $@ vs $* enligt materialet?", "options": ["Samma", "$@ separata, $* ett ord", "$* separata", "Bara $@ fungerar"], "correct": 1, "explanation": "Materialet: '$@ = separata ord, $* = ett ord'"},
        {"question": "${f%.txt}.bak gör?", "options": ["Lägger till .txt", "Byter .txt mot .bak", "Tar bort .bak", "Fel"], "correct": 1, "explanation": "Materialet: '${fil%.txt}.bak = byt ändelse'"},
        {"question": "Processa output från kommando?", "options": ["for line in cmd", "cmd | while read", "read cmd", "cmd > while"], "correct": 1, "explanation": "Materialet: 'cmd | while read -r'"},
        {"question": "until ping lyckas?", "options": ["until ping fails", "until ping -c 1 host &>/dev/null", "while ping fails", "ping until success"], "correct": 1, "explanation": "Materialet: 'until ping -c 1 server'"},
        {"question": "done < fil.txt gör?", "options": ["Output till fil", "Input från fil", "Append", "Överskriver"], "correct": 1, "explanation": "Materialet: '< fil.txt = Input-redirection'"},
        {"question": "Continue vid saknad fil?", "options": ["[[ -f ]] && continue", "[[ ! -f ]] && continue", "if not file continue", "skip if missing"], "correct": 1, "explanation": "[[ ! -f \"$f\" ]] && continue"},
    ],
}

# =============================================================================
# NOD 3: BASH-GRUNDER & SHEBANG
# Källa: nod_bash_grunder.py
# Koncept: Shebang, chmod +x, exit codes, set -e/-u/-x, Terminal vs Shell
# =============================================================================

NOD_03_FLASHCARDS = {
    "easy": [
        # Terminal vs Shell vs Bash från materialet
        {"front": "Terminal vs Shell - vad är skillnaden?", "back": "Terminal = fönstret, Shell = tolken (programmet)"},
        {"front": "Vad är Bash?", "back": "En typ av shell - tolkar dina kommandon"},
        {"front": "Vad är shebang?", "back": "Första raden: #!/bin/bash - talar om vilken tolk"},
        {"front": "Varför behövs shebang?", "back": "Systemet vet annars inte HUR det ska köra filen"},
        {"front": "Vilket shebang är mest portabelt?", "back": "#!/usr/bin/env bash"},
        # Köra skript
        {"front": "Gör skript körbart?", "back": "chmod +x skript.sh"},
        {"front": "Kör skript i aktuell katalog?", "back": "./skript.sh"},
        {"front": "Vad betyder exit code 0?", "back": "Kommandot lyckades ✅"},
        {"front": "Vad betyder exit code 1-255?", "back": "Något gick fel ❌"},
        {"front": "Variabel för senaste exit code?", "back": "$?"},
    ],
    "medium": [
        # Exit codes från materialet
        {"front": "Exit code 2 betyder?", "back": "Felaktig användning (t.ex. fil saknas)"},
        {"front": "Exit code 126 betyder?", "back": "Kan inte köra (permission denied)"},
        {"front": "Exit code 127 betyder?", "back": "Kommandot finns inte"},
        {"front": "Exit code 130 betyder?", "back": "Avbrutet med Ctrl+C"},
        # Set-flaggor
        {"front": "set -e gör?", "back": "Avbryt skript vid fel"},
        {"front": "set -u gör?", "back": "Fel vid odefinierad variabel"},
        {"front": "set -x gör?", "back": "Debug-läge - visar varje kommando med +"},
        {"front": "Kombinera alla robusta flaggor?", "back": "set -euo pipefail"},
        {"front": "Vad gör pipefail?", "back": "Fånga fel i pipes (inte bara sista kommandot)"},
        {"front": "Varför ./skript.sh istället för skript.sh?", "back": "Bash letar i PATH, inte aktuell katalog"},
    ],
    "hard": [
        # Vanliga misstag från materialet
        {"front": "Varför namn = 'test' är FEL?", "back": "Inga mellanslag runt = i variabler!"},
        {"front": "Rätt sätt att sätta variabel?", "back": "namn='test' (inga mellanslag)"},
        {"front": "Vad visar $(whoami)?", "back": "Aktuell användare (command substitution)"},
        {"front": "Vad visar $(date)?", "back": "Aktuellt datum och tid"},
        {"front": "Vad visar $(pwd)?", "back": "Aktuell katalog"},
        {"front": "I nano - spara och avsluta?", "back": "Ctrl+O (spara), Enter, Ctrl+X (avsluta)"},
        {"front": "Vad gör # i skript?", "back": "Kommentar - ignoreras av bash"},
        {"front": "Utan set -e, vad händer vid fel?", "back": "Skriptet fortsätter ändå!"},
        {"front": "Utan set -u, odefinierad variabel?", "back": "Blir tomt värde, inget fel"},
        {"front": "Output från set -x börjar med?", "back": "+ (plus) före varje kommando"},
    ],
}

NOD_03_QUIZ = {
    "easy": [
        {"question": "Enligt materialet - Terminal vs Shell?", "options": ["Samma sak", "Terminal = fönstret, Shell = tolken", "Shell = fönstret, Terminal = tolken", "Båda är Bash"], "correct": 1, "explanation": "Tabellen: 'Terminal = fönstret, Shell = tolken'"},
        {"question": "Vad är shebang enligt materialet?", "options": ["En variabel", "Första raden som anger tolk", "Ett kommando", "En funktion"], "correct": 1, "explanation": "Materialet: 'Första raden MÅSTE vara först - anger vilken tolk'"},
        {"question": "Vilken shebang rekommenderas?", "options": ["#!/bash", "#!/bin/bash", "#!/usr/bin/env bash", "#!bash"], "correct": 2, "explanation": "Materialet: '#!/usr/bin/env bash - REKOMMENDERAS - mer portabelt'"},
        {"question": "Vad gör chmod +x?", "options": ["Tar bort fil", "Lägger till execute-rättighet", "Kör skriptet", "Skapar fil"], "correct": 1, "explanation": "Materialet: 'chmod +x = lägg till execute-rättighet'"},
        {"question": "Exit code 0 betyder?", "options": ["Fel", "Fil saknas", "Allt gick bra", "Avbrutet"], "correct": 2, "explanation": "Tabellen: '0 = Allt gick bra! ✅'"},
        {"question": "Variabel för senaste exit code?", "options": ["$!", "$0", "$?", "$#"], "correct": 2, "explanation": "Materialet: '$? innehåller ALLTID exit code från senaste kommandot'"},
        {"question": "Hur kör man ./skript.sh?", "options": ["Direkt utan något", "Måste först chmod +x", "Bara i /bin", "Kräver root"], "correct": 1, "explanation": "Materialet: 'Utan chmod +x kan du INTE köra skriptet med ./'"},
    ],
    "medium": [
        {"question": "Exit code 127 enligt materialet?", "options": ["Lyckades", "Permission denied", "Kommandot finns inte", "Fil saknas"], "correct": 2, "explanation": "Tabellen: '127 = Kommandot finns inte'"},
        {"question": "Exit code 130 enligt materialet?", "options": ["Syntaxfel", "Timeout", "Avbrutet med Ctrl+C", "Minne slut"], "correct": 2, "explanation": "Tabellen: '130 = Avbrutet med Ctrl+C'"},
        {"question": "Vad gör set -e?", "options": ["Echo mode", "Avbryt vid fel", "Export variabler", "Edit mode"], "correct": 1, "explanation": "Materialet: 'set -e = Avbryt vid fel'"},
        {"question": "Vad gör set -u?", "options": ["Uppercase", "Fel vid odefinierad variabel", "Update", "Undo"], "correct": 1, "explanation": "Materialet: 'set -u = Fel vid odefinierade variabler'"},
        {"question": "Vad gör set -x?", "options": ["Exit", "Debug-läge", "XML output", "Extra info"], "correct": 1, "explanation": "Materialet: 'set -x = Debug-läge (visa varje kommando)'"},
        {"question": "Kombinera robusta flaggor?", "options": ["set -abc", "set -euo pipefail", "set --robust", "set -safe"], "correct": 1, "explanation": "Materialet: 'set -euo pipefail'"},
        {"question": "Vad gör pipefail?", "options": ["Snabbare pipes", "Fånga fel i pipes", "Parallella pipes", "Pipe till fil"], "correct": 1, "explanation": "Materialet: 'pipefail = fånga fel i pipes också'"},
    ],
    "hard": [
        {"question": "Vanligt misstag: namn = 'test' - varför fel?", "options": ["Fel quotes", "Mellanslag runt =", "Saknar export", "Fel variabelnamn"], "correct": 1, "explanation": "Vanliga misstag: 'Mellanslag runt = i variabler är FEL'"},
        {"question": "Output från set -x börjar med?", "options": ["#", ">", "+", "$"], "correct": 2, "explanation": "Materialet: 'Varje rad visas med + innan den körs'"},
        {"question": "Utan set -e vid fel?", "options": ["Skriptet kraschar", "Skriptet fortsätter", "Startar om", "Frågar användaren"], "correct": 1, "explanation": "Materialet: 'Utan set -e fortsätter skriptet ändå!'"},
        {"question": "Utan set -u, odefinierad $NAMN?", "options": ["Kraschar", "Tomt värde, inget fel", "Visar 'undefined'", "Använder default"], "correct": 1, "explanation": "Materialet: 'Utan set -u: Skriver ut \"Hej \" (tomt, inget fel)'"},
        {"question": "$(whoami) kallas för?", "options": ["Variable expansion", "Command substitution", "String interpolation", "Shell globbing"], "correct": 1, "explanation": "$(kommando) = command substitution"},
        {"question": "Varför ./skript.sh istället för skript.sh?", "options": ["Snabbare", "Bash letar i PATH, inte aktuell katalog", "Säkrare", "Kräver root annars"], "correct": 1, "explanation": "Vanliga misstag: 'Bash letar i PATH, inte aktuell katalog'"},
    ],
}

# =============================================================================
# NOD 4: VARIABLER, QUOTING & EXPANSIONS
# Källa: nod_variabler_quoting.py
# Koncept: $0,$1,$#,$@,$?, "dubbla"/'enkla', $(cmd), ${var:-default}, {a,b,c}
# =============================================================================

NOD_04_FLASHCARDS = {
    "easy": [
        # Skapa variabler från materialet
        {"front": "Skapa variabel korrekt?", "back": "namn=\"värde\" (INGA mellanslag runt =)"},
        {"front": "Varför namn = \"test\" är FEL?", "back": "Bash tror namn är ett kommando pga mellanslag"},
        {"front": "Använda variabel?", "back": "$namn eller ${namn}"},
        {"front": "När MÅSTE du använda ${klamrar}?", "back": "När text kommer direkt efter: ${namn}sson"},
        {"front": "$0 innehåller?", "back": "Skriptets namn"},
        # Speciella variabler
        {"front": "$1, $2, $3 innehåller?", "back": "Positionsargument 1, 2, 3"},
        {"front": "$# innehåller?", "back": "Antal argument"},
        {"front": "$@ innehåller?", "back": "Alla argument (separata ord)"},
        {"front": "$? innehåller?", "back": "Exit code från senaste kommando"},
        {"front": "$$ innehåller?", "back": "Skriptets process-ID (PID)"},
    ],
    "medium": [
        # Miljövariabler från materialet
        {"front": "$USER innehåller?", "back": "Inloggad användare"},
        {"front": "$HOME innehåller?", "back": "Hemkatalog (/home/student)"},
        {"front": "$PWD innehåller?", "back": "Aktuell katalog"},
        {"front": "$PATH innehåller?", "back": "Sökvägar för kommandon"},
        {"front": "Göra variabel global för subprocesser?", "back": "export MIN_VAR=\"värde\""},
        # Quoting
        {"front": "\"dubbla\" citattecken - expanderas variabler?", "back": "JA - $namn blir värdet"},
        {"front": "'enkla' citattecken - expanderas variabler?", "back": "NEJ - $namn blir bokstavligt $namn"},
        {"front": "echo \"Hej $namn\" med namn=Lisa?", "back": "Hej Lisa"},
        {"front": "echo 'Hej $namn' med namn=Lisa?", "back": "Hej $namn (bokstavligt!)"},
        {"front": "Varför ALLTID \"$variabel\" med citattecken?", "back": "Skyddar mot problem med mellanslag"},
    ],
    "hard": [
        # Command substitution
        {"front": "Fånga kommandoresultat i variabel?", "back": "datum=$(date)"},
        {"front": "Modern syntax vs gammal för cmd substitution?", "back": "$(cmd) modern, `cmd` gammal - använd $()"},
        {"front": "Backup-filnamn med datum?", "back": "backup_$(date +%Y-%m-%d).tar.gz"},
        # Parameter expansion
        {"front": "${var:-default} gör?", "back": "Använder default om var är tom"},
        {"front": "${var:=default} gör?", "back": "Sätter OCH använder default om tom"},
        {"front": "${#var} returnerar?", "back": "Längden på variabelns värde"},
        {"front": "${var^^} gör?", "back": "Konverterar till VERSALER"},
        {"front": "${var,,} gör?", "back": "Konverterar till gemener"},
        # Brace expansion
        {"front": "echo {a,b,c} genererar?", "back": "a b c"},
        {"front": "echo {1..5} genererar?", "back": "1 2 3 4 5"},
    ],
}

NOD_04_QUIZ = {
    "easy": [
        {"question": "Korrekt sätt att skapa variabel enligt materialet?", "options": ["namn = \"Lisa\"", "namn=\"Lisa\"", "$namn=\"Lisa\"", "set namn=\"Lisa\""], "correct": 1, "explanation": "Materialet: 'namn=\"värde\" (INGEN mellanslag runt =)'"},
        {"question": "Vad innehåller $# i ett skript?", "options": ["Skriptets namn", "Senaste exit code", "Antal argument", "Process-ID"], "correct": 2, "explanation": "Tabellen: '$# = Antal argument'"},
        {"question": "Vad innehåller $0?", "options": ["Första argumentet", "Skriptets namn", "Antal argument", "Exit code"], "correct": 1, "explanation": "Tabellen: '$0 = Skriptets namn'"},
        {"question": "echo 'Hej $USER' skriver ut? (USER=student)", "options": ["Hej student", "Hej $USER", "Hej", "Fel"], "correct": 1, "explanation": "Enkla citattecken: INGENTING expanderas - bokstavligt!"},
        {"question": "echo \"Hej $USER\" skriver ut? (USER=student)", "options": ["Hej student", "Hej $USER", "Hej", "Fel"], "correct": 0, "explanation": "Dubbla citattecken: variabler expanderas"},
        {"question": "Vad innehåller $?", "options": ["Skriptnamn", "Argument", "Exit code senaste kommando", "PID"], "correct": 2, "explanation": "Tabellen: '$? = Exit code från senaste kommando'"},
        {"question": "Vad gör export MIN_VAR=\"test\"?", "options": ["Skapar lokal variabel", "Tar bort variabel", "Gör variabel tillgänglig för subprocesser", "Skriver ut"], "correct": 2, "explanation": "Materialet: 'MILJÖVARIABEL (tillgänglig för subprocesser)'"},
    ],
    "medium": [
        {"question": "Fånga resultatet av date i variabel?", "options": ["datum=date", "datum=$(date)", "datum=$date", "$datum=date"], "correct": 1, "explanation": "Materialet: 'datum=$(date) - Fånga dagens datum'"},
        {"question": "Vad genererar echo {a,b,c}.txt?", "options": ["abc.txt", "{a,b,c}.txt", "a.txt b.txt c.txt", "Fel"], "correct": 2, "explanation": "Brace Expansion: 'echo fil{1,2,3}.txt → fil1.txt fil2.txt fil3.txt'"},
        {"question": "${namn:-Gäst} om $namn är tom?", "options": ["Tom sträng", "Gäst", "namn", "Fel"], "correct": 1, "explanation": "Materialet: '${var:-default} = Om var tom, använd default'"},
        {"question": "Varför $(cmd) istället för `cmd`?", "options": ["Snabbare", "Lättare att nästa", "Samma sak", "Äldre syntax"], "correct": 1, "explanation": "Materialet: 'Med backticks - OMÖJLIGT att nästa... använd $() '"},
        {"question": "När MÅSTE ${klamrar} användas?", "options": ["Alltid", "När text kommer direkt efter", "Aldrig", "Bara i funktioner"], "correct": 1, "explanation": "Tabellen: 'Text direkt efter - ${namn}sson - Klamrar krävs!'"},
        {"question": "Vad innehåller $PATH?", "options": ["Nuvarande katalog", "Sökvägar för kommandon", "Hemkatalog", "Tempfiler"], "correct": 1, "explanation": "Tabellen: '$PATH = Sökvägar för kommandon'"},
        {"question": "Skillnad lokal vs export variabel?", "options": ["Ingen", "Export syns i subprocesser", "Lokal är snabbare", "Export sparas permanent"], "correct": 1, "explanation": "Materialet: 'Subprocessen ser inte lokal... Global: jag är global'"},
    ],
    "hard": [
        {"question": "${#var} returnerar enligt materialet?", "options": ["Variabelns värde", "Längden på värdet", "Hashkod", "Antal variabler"], "correct": 1, "explanation": "Tabellen: '${#var} = Längden på variabelns värde'"},
        {"question": "${var^^} gör enligt materialet?", "options": ["Dubblerar värdet", "VERSALER", "Tar bort", "Lägger till"], "correct": 1, "explanation": "Tabellen: '${var^^} = VERSALER'"},
        {"question": "echo {1..5} genererar?", "options": ["{1..5}", "1 2 3 4 5", "12345", "1,2,3,4,5"], "correct": 1, "explanation": "Brace Expansion: 'echo {1..5} → 1 2 3 4 5'"},
        {"question": "Backup-namn med datum enligt materialet?", "options": ["backup_date.tar.gz", "backup_$date.tar.gz", "backup_$(date +%Y-%m-%d).tar.gz", "backup-date.tar.gz"], "correct": 2, "explanation": "Materialet: 'backup_$(date +%Y-%m-%d).tar.gz'"},
        {"question": "Vanligt misstag från tabellen - rm $filnamn utan citattecken?", "options": ["Fungerar", "Bash ser TVÅ filer vid mellanslag", "Kräver sudo", "Snabbare"], "correct": 1, "explanation": "Materialet: 'rm $filnamn → Bash ser: rm min fil.txt (TVÅ filer!)'"},
        {"question": "Skillnad $@ vs $*?", "options": ["Samma", "$@ separata ord, $* ett ord", "$* separata, $@ ett", "Bara $@ fungerar"], "correct": 1, "explanation": "Tabellen: '$@ = Alla argument (separata ord), $* = ett ord'"},
    ],
}

# =============================================================================
# NOD 11: PARAMETRAR & ARRAYS
# Källa: nod_parametrar_arrays.py
# Koncept: shift, parameter expansion, ${var:-default}, arrays
# =============================================================================

NOD_11_FLASHCARDS = {
    "easy": [
        {"front": "$1 innehåller?", "back": "Första argumentet till skriptet"},
        {"front": "$# innehåller?", "back": "Antal argument"},
        {"front": "$@ innehåller?", "back": "Alla argument (separata)"},
        {"front": "shift gör?", "back": "Tar bort $1 och skiftar alla andra"},
        {"front": "shift 2 gör?", "back": "Tar bort $1 och $2"},
        {"front": "Array-syntax?", "back": "arr=(a b c)"},
        {"front": "${arr[0]} returnerar?", "back": "Första elementet"},
        {"front": "${arr[@]} returnerar?", "back": "Alla element"},
        {"front": "${#arr[@]} returnerar?", "back": "Antal element"},
        {"front": "Lägg till i array?", "back": "arr+=(nytt)"},
    ],
    "medium": [
        {"front": "${var:-default} gör?", "back": "Använd default om var är tom"},
        {"front": "${var:=default} gör?", "back": "Sätt OCH använd default om tom"},
        {"front": "${var:?error} gör?", "back": "Visa error och avbryt om tom"},
        {"front": "${#var} returnerar?", "back": "Längden på variabelns värde"},
        {"front": "${var^^} gör?", "back": "Konverterar till VERSALER"},
        {"front": "${var,,} gör?", "back": "Konverterar till gemener"},
        {"front": "${fil%.txt} gör?", "back": "Tar bort .txt från slutet"},
        {"front": "${fil##*/} gör?", "back": "Tar bort path, behåller filnamn"},
        {"front": "${fil%/*} gör?", "back": "Tar bort filnamn, behåller path"},
        {"front": "declare -A skapar?", "back": "Associativ array (key-value)"},
    ],
    "hard": [
        {"front": "# vs % i parameter expansion?", "back": "# = från början, % = från slutet"},
        {"front": "## vs # skillnad?", "back": "## = längsta match, # = kortaste"},
        {"front": "${var:0:5} gör?", "back": "Substring: 5 tecken från position 0"},
        {"front": "${!arr[@]} returnerar?", "back": "Alla INDEX (inte värden)"},
        {"front": "Loopa över array med index?", "back": "for i in \"${!arr[@]}\"; do"},
        {"front": "Array slicing ${arr[@]:2:3}?", "back": "3 element från index 2"},
        {"front": "Associativ array syntax?", "back": "declare -A arr; arr[key]=\"val\""},
        {"front": "unset arr[2] gör?", "back": "Tar bort element på index 2"},
        {"front": "Processa flaggor med while case?", "back": "while [[ $# -gt 0 ]]; case $1 in"},
        {"front": "${var:+value} gör?", "back": "Använd value om var INTE är tom"},
    ],
}

NOD_11_QUIZ = {
    "easy": [
        {"question": "$1 innehåller?", "options": ["Skriptnamn", "Första argumentet", "Antal argument", "Exit code"], "correct": 1, "explanation": "Materialet: '$1-$9 = Argument 1-9'"},
        {"question": "shift gör?", "options": ["Flyttar filer", "Tar bort $1, skiftar resten", "Skapar variabel", "Sorterar"], "correct": 1, "explanation": "Materialet: 'shift tar bort $1 och skiftar'"},
        {"question": "Array skapas med?", "options": ["array a b c", "arr=(a b c)", "[a,b,c]", "new array"], "correct": 1, "explanation": "Materialet: 'arr=(a b c)'"},
        {"question": "${arr[0]} returnerar?", "options": ["Hela arrayen", "Första elementet", "Antal element", "Index"], "correct": 1, "explanation": "Materialet: '${arr[0]} = första elementet'"},
        {"question": "${#arr[@]} returnerar?", "options": ["Första elementet", "Antal element", "Alla element", "Hash"], "correct": 1, "explanation": "Materialet: '${#arr[@]} = antal element'"},
        {"question": "Lägg till element i array?", "options": ["arr.push(x)", "arr+=(x)", "add arr x", "arr[] = x"], "correct": 1, "explanation": "Materialet: 'arr+=(d e)'"},
        {"question": "$# visar?", "options": ["Skriptnamn", "Antal argument", "Process ID", "Exit code"], "correct": 1, "explanation": "Materialet: '$# = Antal argument'"},
    ],
    "medium": [
        {"question": "${var:-default} gör?", "options": ["Sätter default", "Använder default om tom", "Tar bort default", "Definierar"], "correct": 1, "explanation": "Materialet: 'Om var tom, använd default'"},
        {"question": "${#var} returnerar?", "options": ["Hash", "Längden", "Värdet", "Index"], "correct": 1, "explanation": "Materialet: '${#var} = Längden'"},
        {"question": "${var^^} gör?", "options": ["Dubblerar", "VERSALER", "Tar bort", "Kommentar"], "correct": 1, "explanation": "Materialet: '${var^^} = VERSALER'"},
        {"question": "${fil%.txt} gör?", "options": ["Lägger till .txt", "Tar bort .txt från slutet", "Kontrollerar .txt", "Byter namn"], "correct": 1, "explanation": "Materialet: '${fil%.txt} = ta bort ändelse'"},
        {"question": "declare -A skapar?", "options": ["Vanlig array", "Associativ array", "Alias", "Funktion"], "correct": 1, "explanation": "Materialet: 'declare -A = associativ array'"},
        {"question": "${var:=default} skiljer sig från :-?", "options": ["Ingen skillnad", "Sätter OCH använder", "Bara sätter", "Bara använder"], "correct": 1, "explanation": "Materialet: ':= sätter OCH använder'"},
        {"question": "${!arr[@]} returnerar?", "options": ["Värden", "Index", "Längd", "Typ"], "correct": 1, "explanation": "Materialet: '${!arr[@]} = alla index'"},
    ],
    "hard": [
        {"question": "# vs % i expansion?", "options": ["Samma", "# = början, % = slut", "% = början", "Matematiska"], "correct": 1, "explanation": "Materialet: '# = början, % = slut'"},
        {"question": "## vs # skillnad?", "options": ["Ingen", "## längsta, # kortaste", "# längsta", "Kommentar"], "correct": 1, "explanation": "Materialet: '## = längsta match'"},
        {"question": "${var:0:5} gör?", "options": ["5 tecken", "Från index 0, 5 tecken", "Position 5", "Deltal 5"], "correct": 1, "explanation": "Materialet: '${var:0:5} = start:längd'"},
        {"question": "${var:?error} gör vid tom var?", "options": ["Ignorerar", "Visar error, avbryter", "Sätter error", "Fortsätter"], "correct": 1, "explanation": "Materialet: 'Visa error och avbryt om tom'"},
        {"question": "Array slicing ${arr[@]:2:3}?", "options": ["Index 2-3", "3 element från index 2", "Element 2 och 3", "Slice 2,3"], "correct": 1, "explanation": "Materialet: 'från index 2, 3 element'"},
        {"question": "${var:+value} gör om var HAR värde?", "options": ["Ignorerar value", "Använder value", "Tar bort", "Error"], "correct": 1, "explanation": "Materialet: 'Använd value om var INTE är tom'"},
    ],
}

# =============================================================================
# NOD 12: FUNKTIONER
# Källa: nod_funktioner.py
# Koncept: syntax, argument, return, local variabler
# =============================================================================

NOD_12_FLASHCARDS = {
    "easy": [
        {"front": "Funktionssyntax?", "back": "func_name() { kommandon; }"},
        {"front": "$1 i funktion?", "back": "Första argumentet till funktionen"},
        {"front": "$@ i funktion?", "back": "Alla argument till funktionen"},
        {"front": "return gör?", "back": "Avslutar funktionen med exit status (0-255)"},
        {"front": "return 0 betyder?", "back": "Funktionen lyckades"},
        {"front": "return 1 betyder?", "back": "Funktionen misslyckades"},
        {"front": "local gör?", "back": "Skapar lokal variabel (bara i funktionen)"},
        {"front": "Varför local?", "back": "Undviker att ändra globala variabler"},
        {"front": "Anropa funktion?", "back": "func_name arg1 arg2"},
        {"front": "Måste funktion definieras först?", "back": "JA, innan den anropas"},
    ],
    "medium": [
        {"front": "return vs exit?", "back": "return = avslutar funktion, exit = avslutar skriptet"},
        {"front": "return max värde?", "back": "255 (0-255)"},
        {"front": "Returnera data (inte status)?", "back": "Använd echo och fånga med $()"},
        {"front": "Fånga funktionresultat?", "back": "result=$(my_func)"},
        {"front": "Skicka stderr från funktion?", "back": "echo \"fel\" >&2"},
        {"front": "Validera argument i funktion?", "back": "local arg=\"${1:?Argument krävs}\""},
        {"front": "Kolla exit status från funktion?", "back": "if my_func; then"},
        {"front": "Rekursiv funktion?", "back": "Funktion som anropar sig själv"},
        {"front": "Best practice: local?", "back": "ALLTID local för funktionens variabler"},
        {"front": "function keyword?", "back": "Valfritt: function name { } eller name() { }"},
    ],
    "hard": [
        {"front": "Kombinera return och echo?", "back": "echo \"$data\"; return $status"},
        {"front": "Funktion returnerar array?", "back": "echo \"${arr[@]}\" och read -ra"},
        {"front": "Skicka funktion som argument?", "back": "\"$func\" \"$arg\" där func=funktionsnamn"},
        {"front": "Nested functions?", "back": "Funktion definierad inuti annan funktion"},
        {"front": "is_number() validerar?", "back": "[[ \"$1\" =~ ^[0-9]+$ ]]"},
        {"front": "log_error() pattern?", "back": "echo \"[ERROR] $*\" >&2"},
        {"front": "retry() funktion gör?", "back": "Kör kommando med flera försök"},
        {"front": "$FUNCNAME innehåller?", "back": "Aktuell funktions namn"},
        {"front": "Local -a skapar?", "back": "Lokal array"},
        {"front": "Varför >&2 för fel?", "back": "Stderr separerar fel från data"},
    ],
}

NOD_12_QUIZ = {
    "easy": [
        {"question": "Funktionssyntax i Bash?", "options": ["def func():", "func() { }", "function: func", "create func"], "correct": 1, "explanation": "Materialet: 'funktionsnamn() { kommandon }'"},
        {"question": "$1 i funktion är?", "options": ["Skriptets första arg", "Funktionens första arg", "Skriptnamn", "Exit code"], "correct": 1, "explanation": "Materialet: 'Funktioner använder samma parametersystem'"},
        {"question": "return 0 betyder?", "options": ["Fel", "Success", "Noll värde", "Avsluta skript"], "correct": 1, "explanation": "Materialet: 'return 0 = Sant / success'"},
        {"question": "local gör?", "options": ["Loggar", "Lokal variabel", "Låser", "Laddar"], "correct": 1, "explanation": "Materialet: 'local = variabeln finns bara i funktionen'"},
        {"question": "Måste funktion definieras före anrop?", "options": ["Nej", "Ja", "Spelar ingen roll", "Bara med function"], "correct": 1, "explanation": "Materialet: 'Definiera INNAN anrop!'"},
        {"question": "Anropa funktion med argument?", "options": ["func(arg1)", "func arg1 arg2", "call func arg", "func.call(arg)"], "correct": 1, "explanation": "Materialet: 'hälsa \"Lisa\"'"},
        {"question": "return max värde?", "options": ["100", "255", "999", "Obegränsat"], "correct": 1, "explanation": "Materialet: 'return kan bara returnera 0-255'"},
    ],
    "medium": [
        {"question": "return vs exit skillnad?", "options": ["Samma", "return=funktion, exit=skript", "exit=funktion", "return=data"], "correct": 1, "explanation": "Materialet: 'return = Avslutar funktionen, exit = Avslutar HELA skriptet'"},
        {"question": "Returnera data (inte status)?", "options": ["return data", "echo data", "output data", "send data"], "correct": 1, "explanation": "Materialet: 'Använd echo för att returnera värden'"},
        {"question": "Fånga funktion-output?", "options": ["result=func", "result=$(func)", "$result=func", "func > result"], "correct": 1, "explanation": "Materialet: 'resultat=$(addera 10 20)'"},
        {"question": "Fel till stderr i funktion?", "options": ["echo err >&1", "echo err >&2", "error err", "stderr err"], "correct": 1, "explanation": "Materialet: 'echo \"Fel\" >&2'"},
        {"question": "Best practice för variabler i funktion?", "options": ["Globala", "ALLTID local", "export", "readonly"], "correct": 1, "explanation": "Materialet: 'ALLTID använd local!'"},
        {"question": "Kolla om funktion lyckades?", "options": ["if func == 0", "if func; then", "if $(func)", "check func"], "correct": 1, "explanation": "if func; then kollar exit status"},
        {"question": "Rekursiv funktion?", "options": ["Loop", "Anropar sig själv", "Parallell", "Nested"], "correct": 1, "explanation": "Materialet visar factorial som rekursiv"},
    ],
    "hard": [
        {"question": "Kombinera return och echo?", "options": ["Går ej", "echo data; return status", "return echo", "echo return"], "correct": 1, "explanation": "Materialet: 'echo $(( $1 / $2 )); return 0'"},
        {"question": "is_number() validerar med?", "options": ["[[ -n ]]", "[[ =~ ^[0-9]+$ ]]", "test number", "isnumeric"], "correct": 1, "explanation": "Materialet: '[[ \"$1\" =~ ^[0-9]+$ ]]'"},
        {"question": "log_error() skriver till?", "options": ["stdout", "stderr (>&2)", "fil", "syslog"], "correct": 1, "explanation": "Materialet: 'echo \"[ERROR]\" >&2'"},
        {"question": "$FUNCNAME innehåller?", "options": ["Skriptnamn", "Funktionens namn", "Argument", "Status"], "correct": 1, "explanation": "$FUNCNAME = aktuell funktions namn"},
        {"question": "Local -a skapar?", "options": ["Alias", "Lokal array", "Argument", "Attribute"], "correct": 1, "explanation": "local -a = lokal array"},
        {"question": "Skicka funktion som argument?", "options": ["Går ej", "\"$func\" \"$arg\"", "call $func", "&func"], "correct": 1, "explanation": "Materialet: '\"$func\" \"$item\"'"},
    ],
}

# =============================================================================
# NOD 13: SIGNALS, TRAPS & JOB CONTROL
# Källa: nod_signals_traps.py
# Koncept: SIGINT/TERM/KILL, trap, cleanup, bg/fg/jobs
# =============================================================================

NOD_13_FLASHCARDS = {
    "easy": [
        {"front": "Signal är?", "back": "Meddelande till process"},
        {"front": "SIGINT (2)?", "back": "Interrupt - Ctrl+C"},
        {"front": "SIGTERM (15)?", "back": "Terminate - snäll avslutning"},
        {"front": "SIGKILL (9)?", "back": "Kill - tvingad, kan EJ fångas"},
        {"front": "kill PID gör?", "back": "Skickar SIGTERM (default)"},
        {"front": "kill -9 PID gör?", "back": "Skickar SIGKILL (tvångsavslut)"},
        {"front": "trap gör?", "back": "Fångar signaler och kör egen kod"},
        {"front": "trap 'cmd' EXIT?", "back": "Kör cmd när skriptet avslutas"},
        {"front": "Ctrl+Z gör?", "back": "Pausar process (SIGSTOP)"},
        {"front": "bg gör?", "back": "Fortsätter pausad process i bakgrunden"},
    ],
    "medium": [
        {"front": "SIGHUP (1)?", "back": "Hangup - terminal stängs"},
        {"front": "SIGSTOP (19)?", "back": "Stop/pausa - kan EJ fångas"},
        {"front": "SIGCONT (18)?", "back": "Continue - återuppta pausad"},
        {"front": "SIGUSR1/USR2?", "back": "User-defined signaler"},
        {"front": "pkill namn?", "back": "Skickar signal till processer med namn"},
        {"front": "killall namn?", "back": "Avslutar alla med det namnet"},
        {"front": "trap - SIGINT?", "back": "Ta bort trap för SIGINT"},
        {"front": "trap cleanup EXIT SIGINT SIGTERM?", "back": "Samma cleanup för alla tre"},
        {"front": "fg gör?", "back": "Tar tillbaka process till förgrunden"},
        {"front": "jobs visar?", "back": "Lista bakgrundsjobb"},
    ],
    "hard": [
        {"front": "Cleanup-mönster med trap?", "back": "trap 'rm -f $TMPFILE' EXIT"},
        {"front": "Lås-fil mönster?", "back": "echo $$ > lockfile; trap 'rm lockfile' EXIT"},
        {"front": "Graceful shutdown-mönster?", "back": "RUNNING=true; trap 'RUNNING=false' SIGTERM"},
        {"front": "& i slutet av kommando?", "back": "Kör i bakgrunden"},
        {"front": "$! innehåller?", "back": "PID för senaste bakgrundsprocess"},
        {"front": "wait PID gör?", "back": "Väntar på att process avslutas"},
        {"front": "nohup gör?", "back": "Process överlever logout (ignorerar SIGHUP)"},
        {"front": "disown gör?", "back": "Kopplar loss process från shell"},
        {"front": "trap ERR fångar?", "back": "Körs när kommando misslyckas"},
        {"front": "$LINENO i trap?", "back": "Radnummer där fel uppstod"},
    ],
}

NOD_13_QUIZ = {
    "easy": [
        {"question": "Ctrl+C skickar vilken signal?", "options": ["SIGKILL", "SIGTERM", "SIGINT", "SIGHUP"], "correct": 2, "explanation": "Materialet: 'SIGINT (2) = Ctrl+C'"},
        {"question": "SIGKILL kan fångas?", "options": ["Ja", "Nej", "Ibland", "Med sudo"], "correct": 1, "explanation": "Materialet: 'SIGKILL (9) - Kan INTE fångas!'"},
        {"question": "kill utan flagga skickar?", "options": ["SIGKILL", "SIGTERM", "SIGINT", "SIGHUP"], "correct": 1, "explanation": "Materialet: 'kill PID = SIGTERM (default)'"},
        {"question": "trap gör?", "options": ["Fälla", "Fångar signaler", "Terminerar", "Testar"], "correct": 1, "explanation": "Materialet: 'trap fångar signaler'"},
        {"question": "Ctrl+Z gör?", "options": ["Avslutar", "Pausar", "Bakgrund", "Zoom"], "correct": 1, "explanation": "Materialet: 'Ctrl+Z = pausa (SIGSTOP)'"},
        {"question": "bg gör?", "options": ["Backup", "Fortsätter i bakgrund", "Begin", "Blockerar"], "correct": 1, "explanation": "Materialet: 'bg = fortsätt i bakgrunden'"},
        {"question": "fg gör?", "options": ["Filgrupp", "Tar till förgrund", "Flagga", "Finish"], "correct": 1, "explanation": "Materialet: 'fg = ta tillbaka till förgrunden'"},
    ],
    "medium": [
        {"question": "kill -9 är?", "options": ["SIGTERM", "SIGINT", "SIGKILL", "SIGHUP"], "correct": 2, "explanation": "Materialet: 'kill -9 = SIGKILL'"},
        {"question": "trap 'cleanup' EXIT körs?", "options": ["Direkt", "Vid start", "När skriptet avslutas", "Aldrig"], "correct": 2, "explanation": "Materialet: 'EXIT körs ALLTID när skriptet avslutas'"},
        {"question": "pkill gör?", "options": ["Process kill med namn", "Print kill", "Partial kill", "Ping kill"], "correct": 0, "explanation": "Materialet: 'pkill firefox'"},
        {"question": "SIGHUP skickas när?", "options": ["Ctrl+C", "Terminal stängs", "kill -9", "Timeout"], "correct": 1, "explanation": "Materialet: 'SIGHUP = Hangup (terminal stängs)'"},
        {"question": "trap - SIGINT gör?", "options": ["Lägger till trap", "Tar bort trap", "Testar", "Trappar -"], "correct": 1, "explanation": "Materialet: 'trap - SIGINT = Ta bort trap'"},
        {"question": "jobs visar?", "options": ["Alla processer", "Bakgrundsjobb", "CPU-användning", "Jobbköer"], "correct": 1, "explanation": "Materialet: 'jobs - Lista bakgrundsjobb'"},
        {"question": "nohup gör?", "options": ["No help", "Ignorerar SIGHUP", "Stoppar", "Nummer hop"], "correct": 1, "explanation": "Materialet: 'nohup ignorerar SIGHUP'"},
    ],
    "hard": [
        {"question": "Tempfil-cleanup mönster?", "options": ["rm -f temp", "trap 'rm -f $TMPFILE' EXIT", "cleanup temp", "exit clean"], "correct": 1, "explanation": "Materialet: 'trap 'rm -f \"$TMPFILE\"' EXIT'"},
        {"question": "$! innehåller?", "options": ["Exit code", "PID bakgrundsprocess", "Senaste kommando", "Error"], "correct": 1, "explanation": "Materialet: 'PID=$!'"},
        {"question": "wait gör?", "options": ["Pausar", "Väntar på bakgrundsprocess", "Watcher", "Warning"], "correct": 1, "explanation": "Materialet: 'wait $pid1 $pid2 $pid3'"},
        {"question": "disown gör?", "options": ["Disables owner", "Kopplar loss från shell", "Delete own", "Dis-ownership"], "correct": 1, "explanation": "Materialet: 'disown - kopplar loss'"},
        {"question": "Graceful shutdown: trap sätter?", "options": ["exit 0", "RUNNING=false", "kill self", "restart"], "correct": 1, "explanation": "Materialet: 'RUNNING=false'"},
        {"question": "trap ERR fångar?", "options": ["Errors i syntax", "När kommando misslyckas", "Exit request", "Environment"], "correct": 1, "explanation": "Materialet: 'ERR - När kommando misslyckas'"},
    ],
}

# =============================================================================
# NOD 14: USERS & GROUPS
# Källa: nod_users_groups.py
# Koncept: useradd, usermod -aG, passwd, /etc/passwd, /etc/shadow
# =============================================================================

NOD_14_FLASHCARDS = {
    "easy": [
        {"front": "useradd -m gör?", "back": "Skapar användare MED hemkatalog"},
        {"front": "useradd -s /bin/bash?", "back": "Sätter login shell"},
        {"front": "usermod -aG grupp user?", "back": "Lägger TILL i grupp (append)"},
        {"front": "KRITISKT: varför -a i usermod -aG?", "back": "Utan -a ERSÄTTS alla grupper!"},
        {"front": "passwd user gör?", "back": "Sätter lösenord för user"},
        {"front": "/etc/passwd innehåller?", "back": "Användarinfo (INTE lösenord)"},
        {"front": "/etc/shadow innehåller?", "back": "Krypterade lösenord"},
        {"front": "/etc/group innehåller?", "back": "Gruppinformation"},
        {"front": "groupadd namn?", "back": "Skapar ny grupp"},
        {"front": "groups user visar?", "back": "Användarens grupptillhörigheter"},
    ],
    "medium": [
        {"front": "userdel -r gör?", "back": "Tar bort user OCH hemkatalog"},
        {"front": "id user visar?", "back": "UID, GID och alla grupper"},
        {"front": "chage -l user visar?", "back": "Lösenordspolicy och utgångsdatum"},
        {"front": "passwd --expire user?", "back": "Tvingar lösenordsbyte vid nästa login"},
        {"front": "usermod -L user?", "back": "Låser kontot"},
        {"front": "usermod -U user?", "back": "Låser upp kontot"},
        {"front": "usermod -e 2025-12-31 user?", "back": "Sätter kontots utgångsdatum"},
        {"front": "/etc/skel är?", "back": "Mall för nya hemkataloger"},
        {"front": "useradd -G sudo,docker user?", "back": "Lägg till i extra grupper direkt"},
        {"front": "Fälten i /etc/passwd?", "back": "user:x:UID:GID:kommentar:hem:shell"},
    ],
    "hard": [
        {"front": "Loop: skapa flera användare?", "back": "for user in A B C; do useradd -m $user; done"},
        {"front": "chage -d 0 user gör?", "back": "Tvingar lösenordsbyte"},
        {"front": "chage -M 90 user gör?", "back": "Max 90 dagar mellan lösenordsbyten"},
        {"front": "chage -E 2025-12-31 gör?", "back": "Sätter KONTOTS utgångsdatum"},
        {"front": "Skillnad passwd -l vs usermod -L?", "back": "Samma effekt - låser kontot"},
        {"front": "chpasswd används för?", "back": "Batch-sätta lösenord: echo 'user:pass' | chpasswd"},
        {"front": "getent passwd user?", "back": "Hämtar user från alla källor (LDAP etc)"},
        {"front": "Kolla om user finns i skript?", "back": "id \"$user\" &>/dev/null"},
        {"front": "Kontraktanställd-script?", "back": "usermod --expiredate 2025-12-31 $user"},
        {"front": "adduser vs useradd?", "back": "adduser = interaktiv (Debian), useradd = lågnivå"},
    ],
}

NOD_14_QUIZ = {
    "easy": [
        {"question": "useradd -m gör?", "options": ["Flyttar user", "Skapar MED hemkatalog", "Modifierar", "Mail"], "correct": 1, "explanation": "Materialet: '-m = Med hemkatalog'"},
        {"question": "KRITISKT: usermod utan -a?", "options": ["Lägger till", "ERSÄTTER alla grupper", "Fel", "Ignorerar"], "correct": 1, "explanation": "Materialet: 'Utan -a ERSÄTTS alla grupper!'"},
        {"question": "/etc/passwd innehåller lösenord?", "options": ["Ja", "Nej, de är i /etc/shadow", "Krypterade", "Bara root"], "correct": 1, "explanation": "Materialet: 'INTE lösenord!'"},
        {"question": "groups user visar?", "options": ["Bara primär", "Alla grupptillhörigheter", "Grupp-ID", "Gruppnamn"], "correct": 1, "explanation": "Materialet: 'groups alice'"},
        {"question": "passwd user gör?", "options": ["Visar lösenord", "Sätter lösenord", "Tar bort", "Krypterar"], "correct": 1, "explanation": "Materialet: 'passwd alice = Sätt lösenord'"},
        {"question": "groupadd gör?", "options": ["Lägger till i grupp", "Skapar ny grupp", "Tar bort grupp", "Grupperar"], "correct": 1, "explanation": "Materialet: 'groupadd developers'"},
        {"question": "userdel -r gör?", "options": ["Tar bort user", "Tar bort user + hem", "Recursive list", "Restore"], "correct": 1, "explanation": "Materialet: '-r = Ta bort hemkatalog också'"},
    ],
    "medium": [
        {"question": "id user visar?", "options": ["Bara UID", "UID, GID och grupper", "Identitet", "ID-kort"], "correct": 1, "explanation": "Materialet: 'id alice = UID, GID och alla grupper'"},
        {"question": "chage -l visar?", "options": ["Lista users", "Lösenordspolicy", "Last login", "Lock status"], "correct": 1, "explanation": "Materialet: 'chage -l alice'"},
        {"question": "passwd --expire gör?", "options": ["Tar bort lösenord", "Tvingar byte nästa login", "Förlänger", "Exporterar"], "correct": 1, "explanation": "Materialet: 'Tvinga byte vid nästa inloggning'"},
        {"question": "usermod -L gör?", "options": ["Lista", "Låser konto", "Login", "Link"], "correct": 1, "explanation": "Materialet: '-L = Lås konto'"},
        {"question": "/etc/skel används för?", "options": ["Skelett", "Mall för hemkataloger", "Security", "Shell"], "correct": 1, "explanation": "Materialet: 'Mall för nya hemkataloger'"},
        {"question": "usermod -e datum sätter?", "options": ["Email", "Kontots utgångsdatum", "Editor", "Expire password"], "correct": 1, "explanation": "Materialet: '-e = Sätt utgångsdatum'"},
        {"question": "Fält i /etc/passwd?", "options": ["5 fält", "7 fält", "3 fält", "10 fält"], "correct": 1, "explanation": "user:x:UID:GID:comment:home:shell = 7"},
    ],
    "hard": [
        {"question": "chage -d 0 gör?", "options": ["Tar bort", "Tvingar lösenordsbyte", "Datum 0", "Delete"], "correct": 1, "explanation": "Materialet: 'chage -d 0 = Tvinga byte'"},
        {"question": "chpasswd används för?", "options": ["Change password interaktivt", "Batch-sätta lösenord", "Check password", "Chain password"], "correct": 1, "explanation": "Materialet: 'echo \"user:pass\" | chpasswd'"},
        {"question": "Kolla om user finns i skript?", "options": ["test user", "id \"$user\" &>/dev/null", "user exists", "check user"], "correct": 1, "explanation": "Materialet: 'id \"$user\" &>/dev/null'"},
        {"question": "adduser vs useradd?", "options": ["Samma", "adduser=interaktiv, useradd=lågnivå", "useradd=interaktiv", "adduser=äldre"], "correct": 1, "explanation": "Materialet: 'adduser - Interaktiv (Debian)'"},
        {"question": "chage -M 90 sätter?", "options": ["Minimum", "Maximum dagar för lösenord", "Månad", "Minutes"], "correct": 1, "explanation": "Materialet: 'Sätt max dagar för lösenord'"},
        {"question": "getent passwd user gör?", "options": ["Get entity", "Hämtar från alla källor", "Generate", "Get entry"], "correct": 1, "explanation": "getent hämtar från passwd, LDAP, etc"},
    ],
}

# =============================================================================
# NOD 15: PERMISSIONS (CHMOD/CHOWN/SGID)
# Källa: nod_permissions.py
# Koncept: rwx, oktal, SUID/SGID/Sticky, chmod/chown
# =============================================================================

NOD_15_FLASHCARDS = {
    "easy": [
        {"front": "r i permissions?", "back": "Read = 4"},
        {"front": "w i permissions?", "back": "Write = 2"},
        {"front": "x i permissions?", "back": "Execute = 1"},
        {"front": "chmod 755 ger?", "back": "rwxr-xr-x"},
        {"front": "chmod 644 ger?", "back": "rw-r--r--"},
        {"front": "chmod +x fil?", "back": "Gör filen körbar för alla"},
        {"front": "chown user:grupp fil?", "back": "Ändrar ägare OCH grupp"},
        {"front": "chown :grupp fil?", "back": "Ändrar ENDAST grupp"},
        {"front": "rwx i oktal?", "back": "4+2+1 = 7"},
        {"front": "r-- i oktal?", "back": "4"},
    ],
    "medium": [
        {"front": "SGID på katalog gör?", "back": "Nya filer ärver gruppägandet"},
        {"front": "chmod 2775 katalog?", "back": "SGID + rwxrwxr-x"},
        {"front": "Sticky bit på katalog?", "back": "Endast ägare kan ta bort sina filer"},
        {"front": "chmod 1777 katalog?", "back": "Sticky bit + rwxrwxrwx"},
        {"front": "s på group-position?", "back": "SGID är aktivt"},
        {"front": "t på others-position?", "back": "Sticky bit är aktivt"},
        {"front": "SUID (4xxx) gör?", "back": "Fil körs med ÄGARENS rättigheter"},
        {"front": "/tmp har vilken special?", "back": "Sticky bit"},
        {"front": "chmod -R 755 katalog?", "back": "Rekursivt (alla filer/mappar)"},
        {"front": "Korrekt SSH permissions för ~/.ssh?", "back": "700"},
    ],
    "hard": [
        {"front": "Delad mapp: rätt permissions?", "back": "chmod 2770 + chown root:grupp"},
        {"front": "Varför 2770 för delad mapp?", "back": "SGID(2) + rwxrwx---(770)"},
        {"front": "chmod 4755 på fil?", "back": "SUID aktiv - kör som ägare"},
        {"front": "Permissions för privat nyckel?", "back": "600 (rw-------)"},
        {"front": "/usr/bin/passwd har?", "back": "SUID (rwsr-xr-x)"},
        {"front": "chmod u+s gör?", "back": "Sätter SUID"},
        {"front": "chmod g+s gör?", "back": "Sätter SGID"},
        {"front": "chmod +t gör?", "back": "Sätter Sticky bit"},
        {"front": "Beräkna rwxrwxr-x?", "back": "775"},
        {"front": "Speciella permissions oktal?", "back": "4=SUID, 2=SGID, 1=Sticky"},
    ],
}

NOD_15_QUIZ = {
    "easy": [
        {"question": "chmod 755 ger?", "options": ["rwxrwxrwx", "rwxr-xr-x", "rw-r--r--", "rwx------"], "correct": 1, "explanation": "Materialet: '755 = rwxr-xr-x'"},
        {"question": "r+w+x i oktal?", "options": ["5", "6", "7", "3"], "correct": 2, "explanation": "Materialet: '4+2+1 = 7'"},
        {"question": "chmod +x gör?", "options": ["Tar bort x", "Lägger till x", "Extended", "Exit"], "correct": 1, "explanation": "Materialet: '+x = Gör körbar'"},
        {"question": "chown user:grupp gör?", "options": ["Bara user", "Bara grupp", "User OCH grupp", "Ingenting"], "correct": 2, "explanation": "Materialet: 'chown user:grupp = ändrar båda'"},
        {"question": "644 i rwx?", "options": ["rwxrwxrwx", "rw-r--r--", "rwx------", "r--r--r--"], "correct": 1, "explanation": "Materialet: '644 = rw-r--r--'"},
        {"question": "Vad betyder r?", "options": ["Run", "Read", "Root", "Right"], "correct": 1, "explanation": "Materialet: 'r = Läsa'"},
        {"question": "chown :grupp ändrar?", "options": ["User", "Endast grupp", "Båda", "Permissions"], "correct": 1, "explanation": "Materialet: 'Ändra endast grupp'"},
    ],
    "medium": [
        {"question": "SGID på katalog gör?", "options": ["Kör som grupp", "Nya filer ärver grupp", "Super group", "Set group"], "correct": 1, "explanation": "Materialet: 'NYA FILER ÄRVER GRUPPÄGANDET'"},
        {"question": "chmod 2775 - vad är 2?", "options": ["SUID", "SGID", "Sticky", "Special"], "correct": 1, "explanation": "Materialet: '2xxx = SGID'"},
        {"question": "Sticky bit gör?", "options": ["Klistrar filer", "Endast ägare kan ta bort", "Snabbare", "Sticky notes"], "correct": 1, "explanation": "Materialet: 'Endast ägare kan ta bort sina filer'"},
        {"question": "s på grupp-position?", "options": ["SUID", "SGID aktiv", "Super", "Sticky"], "correct": 1, "explanation": "Materialet: 's på group = SGID'"},
        {"question": "t på others?", "options": ["SUID", "SGID", "Sticky bit", "Test"], "correct": 2, "explanation": "Materialet: 't = Sticky bit'"},
        {"question": "/tmp har?", "options": ["SUID", "SGID", "Sticky bit", "Ingen special"], "correct": 2, "explanation": "Materialet: '/tmp har sticky bit'"},
        {"question": "~/.ssh permissions?", "options": ["777", "755", "700", "644"], "correct": 2, "explanation": "Materialet: 'chmod 700 ~/.ssh'"},
    ],
    "hard": [
        {"question": "Delad mapp: chmod 2770 - varför 2?", "options": ["SUID", "SGID - filer ärver grupp", "Sticky", "2 användare"], "correct": 1, "explanation": "Materialet: 'SGID + permissions'"},
        {"question": "/usr/bin/passwd har?", "options": ["SGID", "SUID (rwsr-xr-x)", "Sticky", "Ingen"], "correct": 1, "explanation": "Materialet: '/usr/bin/passwd har SUID'"},
        {"question": "chmod u+s sätter?", "options": ["SGID", "SUID", "Sticky", "Special"], "correct": 1, "explanation": "Materialet: 'chmod u+s = SUID'"},
        {"question": "chmod g+s sätter?", "options": ["SUID", "SGID", "Sticky", "Group"], "correct": 1, "explanation": "Materialet: 'chmod g+s = SGID'"},
        {"question": "Speciella permissions oktal: SUID?", "options": ["1", "2", "4", "8"], "correct": 2, "explanation": "4=SUID, 2=SGID, 1=Sticky"},
        {"question": "Privat SSH-nyckel permissions?", "options": ["644", "600", "700", "400"], "correct": 1, "explanation": "Materialet: '600 = rw------- (privat)"},
    ],
}

# =============================================================================
# NOD 16: SSH-NYCKLAR & HÄRDNING
# Källa: nod_ssh_hardening.py
# Koncept: ssh-keygen, ssh-copy-id, PasswordAuthentication no, PermitRootLogin no
# =============================================================================

NOD_16_FLASHCARDS = {
    "easy": [
        {"front": "SSH default port?", "back": "22"},
        {"front": "ssh-keygen -t ed25519?", "back": "Genererar ed25519-nyckel (rekommenderas)"},
        {"front": "ssh-copy-id gör?", "back": "Kopierar publik nyckel till server"},
        {"front": "~/.ssh/id_ed25519?", "back": "Privat nyckel - DELA ALDRIG"},
        {"front": "~/.ssh/id_ed25519.pub?", "back": "Publik nyckel - kan delas"},
        {"front": "~/.ssh/authorized_keys?", "back": "Publika nycklar som får logga in (SERVER)"},
        {"front": "PasswordAuthentication no?", "back": "Stänger av lösenordsinloggning"},
        {"front": "PermitRootLogin no?", "back": "Root får inte logga in via SSH"},
        {"front": "ssh -p 6622 user@server?", "back": "Ansluter via port 6622"},
        {"front": "systemctl restart ssh?", "back": "Startar om SSH-tjänsten"},
    ],
    "medium": [
        {"front": "KRITISK ordning vid härdning?", "back": "Kopiera nyckel → Testa → SEDAN stäng lösenord"},
        {"front": "AllowUsers said alice bob?", "back": "Endast dessa får SSH:a"},
        {"front": "Vilken nyckeltyp rekommenderas?", "back": "ed25519"},
        {"front": "~/.ssh permissions?", "back": "700"},
        {"front": "authorized_keys permissions?", "back": "600"},
        {"front": "/etc/ssh/sshd_config.d/?", "back": "Katalog för SSH-konfiguration"},
        {"front": "Varför aldrig stänga lösenord först?", "back": "Du låser ut dig utan fungerande nyckel!"},
        {"front": "ssh -v user@server?", "back": "Verbose/debug-läge"},
        {"front": "~/.ssh/config används för?", "back": "SSH-alias och host-inställningar"},
        {"front": "journalctl -u ssh?", "back": "Visa SSH-loggar"},
    ],
    "hard": [
        {"front": "Härdningsfil plats?", "back": "/etc/ssh/sshd_config.d/01-hardening.conf"},
        {"front": "ss -tulpn | grep ssh?", "back": "Visar vilken port SSH lyssnar på"},
        {"front": "SSH-config alias syntax?", "back": "Host namn\\n  HostName ip\\n  User user"},
        {"front": "Kopiera nyckel manuellt?", "back": "Klistra pub-nyckel i ~/.ssh/authorized_keys"},
        {"front": "PubkeyAuthentication yes?", "back": "Tillåt nyckelautentisering"},
        {"front": "ChallengeResponseAuthentication no?", "back": "Stäng av challenge-response"},
        {"front": "X11Forwarding no?", "back": "Stäng av X11-forwarding"},
        {"front": "ssh-keygen -C 'email'?", "back": "Lägger till kommentar i nyckeln"},
        {"front": "Testa nyckel innan lösenord stängs?", "back": "Ny terminal: ssh user@server"},
        {"front": "Öppna port i ufw före byte?", "back": "ufw allow 6622/tcp"},
    ],
}

NOD_16_QUIZ = {
    "easy": [
        {"question": "SSH default port?", "options": ["21", "22", "80", "443"], "correct": 1, "explanation": "Materialet: 'Default port: 22'"},
        {"question": "ssh-keygen -t ed25519 skapar?", "options": ["RSA-nyckel", "ed25519-nyckel", "Lösenord", "Config"], "correct": 1, "explanation": "Materialet: '-t ed25519'"},
        {"question": "ssh-copy-id gör?", "options": ["Kopierar config", "Kopierar publik nyckel", "Kopierar privat nyckel", "Kopierar lösenord"], "correct": 1, "explanation": "Materialet: 'Kopierar publik nyckel till authorized_keys'"},
        {"question": "Privat nyckel ska?", "options": ["Delas", "Aldrig delas", "Kopieras", "Publiceras"], "correct": 1, "explanation": "Materialet: 'PRIVAT - DELA ALDRIG!'"},
        {"question": "authorized_keys finns på?", "options": ["Klienten", "Servern", "Båda", "Ingen"], "correct": 1, "explanation": "Materialet: 'Fil på SERVERN'"},
        {"question": "PasswordAuthentication no gör?", "options": ["Stänger SSH", "Endast nycklar tillåts", "Stänger root", "Timeout"], "correct": 1, "explanation": "Materialet: 'Endast nyckelautentisering'"},
        {"question": "ssh -p 6622 anger?", "options": ["Password", "Port", "Path", "Protocol"], "correct": 1, "explanation": "Materialet: '-p = port'"},
    ],
    "medium": [
        {"question": "Rätt ordning vid härdning?", "options": ["Stäng lösenord → kopiera nyckel", "Kopiera nyckel → testa → stäng lösenord", "Byt port → stäng allt", "Spelar ingen roll"], "correct": 1, "explanation": "Materialet: 'TESTA att nyckelinloggning fungerar FÖRST'"},
        {"question": "Vilken nyckeltyp rekommenderas?", "options": ["rsa", "dsa", "ed25519", "ecdsa"], "correct": 2, "explanation": "Materialet: 'ed25519 - Bäst'"},
        {"question": "~/.ssh permissions?", "options": ["777", "755", "700", "644"], "correct": 2, "explanation": "Materialet: '700 = rwx------'"},
        {"question": "AllowUsers gör?", "options": ["Tillåter alla", "Begränsar vem som får SSH:a", "Lägger till users", "Allow list"], "correct": 1, "explanation": "Materialet: 'AllowUsers said alice bob'"},
        {"question": "Stänga lösenord utan nyckel?", "options": ["OK", "Du låser ut dig", "SSH fixar det", "Backup finns"], "correct": 1, "explanation": "Materialet: 'LÅSER DU UT DIG SJÄLV!'"},
        {"question": "PermitRootLogin no?", "options": ["Root måste logga in", "Root får inte SSH:a", "Root permit", "Root allowed"], "correct": 1, "explanation": "Materialet: 'Root får INTE logga in'"},
        {"question": "ssh -v gör?", "options": ["Version", "Verbose/debug", "Verify", "Virtual"], "correct": 1, "explanation": "Materialet: '-v = Verbose läge'"},
    ],
    "hard": [
        {"question": "SSH-härdningsfil plats?", "options": ["/etc/ssh/config", "/etc/ssh/sshd_config.d/", "~/.ssh/config", "/ssh/harden"], "correct": 1, "explanation": "Materialet: '/etc/ssh/sshd_config.d/01-hardening.conf'"},
        {"question": "ss -tulpn | grep ssh visar?", "options": ["SSH-version", "Vilken port SSH lyssnar", "SSH-nycklar", "SSH-loggar"], "correct": 1, "explanation": "Materialet: 'Verifiera vilken port'"},
        {"question": "X11Forwarding no?", "options": ["Stänger X11", "Stänger SSH", "Forwarding on", "X11 required"], "correct": 0, "explanation": "Materialet: 'X11Forwarding no'"},
        {"question": "ssh-keygen -C gör?", "options": ["Create", "Lägger till kommentar", "Copy", "Check"], "correct": 1, "explanation": "Materialet: '-C = kommentar'"},
        {"question": "Öppna port i ufw före SSH-byte?", "options": ["ufw allow ssh", "ufw allow 6622/tcp", "ufw enable", "Behövs ej"], "correct": 1, "explanation": "Materialet: 'ufw allow 6622/tcp'"},
        {"question": "PubkeyAuthentication yes?", "options": ["Stänger nycklar", "Tillåter nyckelauth", "Public key off", "Required"], "correct": 1, "explanation": "Materialet: 'PubkeyAuthentication yes'"},
    ],
}

# =============================================================================
# NOD 17: UFW (UNCOMPLICATED FIREWALL)
# Källa: nod_ufw.py
# Koncept: ufw allow ssh FÖRST, ufw enable, status numbered, delete
# =============================================================================

NOD_17_FLASHCARDS = {
    "easy": [
        {"front": "UFW står för?", "back": "Uncomplicated Firewall"},
        {"front": "ufw enable gör?", "back": "Aktiverar brandväggen"},
        {"front": "ufw disable gör?", "back": "Inaktiverar brandväggen"},
        {"front": "ufw status visar?", "back": "Aktiva regler"},
        {"front": "ufw allow ssh gör?", "back": "Öppnar port 22"},
        {"front": "ufw allow 80 gör?", "back": "Öppnar port 80"},
        {"front": "ufw deny 23 gör?", "back": "Blockerar port 23"},
        {"front": "KRITISKT före enable?", "back": "ALLTID ufw allow ssh först!"},
        {"front": "ufw default deny incoming?", "back": "Blockerar all inkommande som default"},
        {"front": "ufw default allow outgoing?", "back": "Tillåter all utgående som default"},
    ],
    "medium": [
        {"front": "ufw status numbered visar?", "back": "Regler med nummer (för delete)"},
        {"front": "ufw delete 3 gör?", "back": "Tar bort regel nummer 3"},
        {"front": "ufw allow 6622/tcp?", "back": "Öppnar specifik port med protokoll"},
        {"front": "ufw allow from 10.0.0.0/24?", "back": "Tillåter från specifikt nätverk"},
        {"front": "ufw allow from IP to any port 22?", "back": "Tillåter SSH från specifik IP"},
        {"front": "ufw --force enable?", "back": "Aktiverar utan bekräftelse"},
        {"front": "ufw reset gör?", "back": "Återställer alla regler till default"},
        {"front": "ufw limit ssh gör?", "back": "Rate-limiting mot brute force"},
        {"front": "Varför SSH först?", "back": "Utan SSH-regel låser du ut dig!"},
        {"front": "ufw app list visar?", "back": "Fördefinierade applikationsprofiler"},
    ],
    "hard": [
        {"front": "ufw allow proto tcp from IP?", "back": "Tillåter TCP från specifik IP"},
        {"front": "ufw logging on gör?", "back": "Aktiverar loggning"},
        {"front": "ufw show added visar?", "back": "Regler som ska läggas till"},
        {"front": "Anpassa SSH-port: ordning?", "back": "1) allow ny port 2) ändra sshd 3) reload 4) ta bort 22"},
        {"front": "/etc/ufw/user.rules?", "back": "Användardefinierade IPv4-regler"},
        {"front": "/etc/ufw/user6.rules?", "back": "Användardefinierade IPv6-regler"},
        {"front": "ufw route allow?", "back": "Tillåter forwarding mellan interfaces"},
        {"front": "ufw deny from IP?", "back": "Blockerar allt från specifik IP"},
        {"front": "UFW bakom NAT?", "back": "Fungerar - brandväggen ser intern trafik"},
        {"front": "ufw allow in on eth0?", "back": "Tillåter på specifik interface"},
    ],
}

NOD_17_QUIZ = {
    "easy": [
        {"question": "UFW står för?", "options": ["Ubuntu Firewall", "Uncomplicated Firewall", "Unix Firewall", "Ultimate Firewall"], "correct": 1, "explanation": "Materialet: 'Uncomplicated Firewall'"},
        {"question": "ufw enable gör?", "options": ["Inaktiverar", "Aktiverar brandväggen", "Enabler", "Lägger regel"], "correct": 1, "explanation": "Materialet: 'ufw enable'"},
        {"question": "KRITISKT före enable?", "options": ["Spara config", "ufw allow ssh", "Stänga portar", "Backup"], "correct": 1, "explanation": "Materialet: 'KRITISKT! Tillåt SSH INNAN!'"},
        {"question": "ufw allow 80 gör?", "options": ["Blockerar 80", "Öppnar port 80", "Tar bort 80", "Allow all"], "correct": 1, "explanation": "Materialet: 'ufw allow 80'"},
        {"question": "ufw deny 23?", "options": ["Öppnar 23", "Blockerar port 23", "Denies access", "Delete 23"], "correct": 1, "explanation": "Materialet: 'ufw deny 23'"},
        {"question": "ufw status visar?", "options": ["Status text", "Aktiva regler", "All info", "Stats"], "correct": 1, "explanation": "Materialet: 'ufw status'"},
        {"question": "ufw disable gör?", "options": ["Aktiverar", "Inaktiverar brandväggen", "Disable regler", "Delete"], "correct": 1, "explanation": "Materialet: 'ufw disable'"},
    ],
    "medium": [
        {"question": "ufw status numbered används för?", "options": ["Numrerar portar", "Visa nummer för delete", "Status number", "Count rules"], "correct": 1, "explanation": "Materialet: 'status numbered - visar regler med nummer'"},
        {"question": "ufw delete 3?", "options": ["Port 3", "Tar bort regel 3", "Delete 3 rules", "Tredje port"], "correct": 1, "explanation": "Materialet: 'ufw delete 3'"},
        {"question": "ufw allow 6622/tcp?", "options": ["Alla portar", "Port 6622 TCP", "Allow TCP", "6622 deny"], "correct": 1, "explanation": "Materialet: 'ufw allow 6622/tcp'"},
        {"question": "ufw limit ssh?", "options": ["Begränsar SSH", "Rate-limiting", "SSH limit", "Max SSH"], "correct": 1, "explanation": "Materialet: 'ufw limit ssh - rate-limiting'"},
        {"question": "Utan SSH-regel före enable?", "options": ["OK", "Du låser ut dig", "SSH fungerar", "Default tillåter"], "correct": 1, "explanation": "Materialet: 'UTAN SSH-REGEL LÅSER DU UT DIG!'"},
        {"question": "ufw app list visar?", "options": ["Applications", "Fördefinierade profiler", "App store", "Alla appar"], "correct": 1, "explanation": "Materialet: 'ufw app list'"},
        {"question": "ufw reset?", "options": ["Restartar", "Återställer alla regler", "Reset counter", "Reload"], "correct": 1, "explanation": "Materialet: 'ufw reset'"},
    ],
    "hard": [
        {"question": "ufw allow from 10.0.0.0/24?", "options": ["Port 10", "Tillåter från nätverk", "Allow 24 ports", "10 connections"], "correct": 1, "explanation": "Materialet: 'ufw allow from 10.0.0.0/24'"},
        {"question": "Byta SSH-port ordning?", "options": ["Byt port → enable", "Allow ny → ändra sshd → reload → ta bort 22", "Direct change", "Spelar ingen roll"], "correct": 1, "explanation": "Materialet: '4-stegs process'"},
        {"question": "ufw logging on?", "options": ["Loggar ut", "Aktiverar loggning", "Login", "Log off"], "correct": 1, "explanation": "Materialet: 'ufw logging on'"},
        {"question": "ufw route allow?", "options": ["Route add", "Tillåter forwarding", "Router config", "Routing table"], "correct": 1, "explanation": "Materialet: 'route = forwarding'"},
        {"question": "ufw deny from IP?", "options": ["Deny by IP", "Blockerar allt från IP", "IP deny list", "Deny IP range"], "correct": 1, "explanation": "Materialet: 'ufw deny from [IP]'"},
        {"question": "ufw allow in on eth0?", "options": ["Ethernet", "Tillåter på specifik interface", "Eth0 allow", "In out eth0"], "correct": 1, "explanation": "Materialet: 'allow in on [interface]'"},
    ],
}

# =============================================================================
# NOD 18: FIREWALLD & SELINUX
# Källa: nod_firewalld.py
# Koncept: --permanent, --reload, zoner, SELinux, semanage port
# =============================================================================

NOD_18_FLASHCARDS = {
    "easy": [
        {"front": "firewalld används i?", "back": "RHEL/CentOS/Rocky/Alma"},
        {"front": "firewall-cmd --state?", "back": "Visar om brandväggen är aktiv"},
        {"front": "--permanent gör?", "back": "Sparar regeln permanent"},
        {"front": "--reload gör?", "back": "Laddar om permanent config"},
        {"front": "KRITISKT: utan --permanent?", "back": "Regeln försvinner vid omstart!"},
        {"front": "KRITISKT: utan --reload?", "back": "Permanenta regler aktiveras inte!"},
        {"front": "Default zon?", "back": "public"},
        {"front": "firewall-cmd --list-all?", "back": "Visar alla regler i aktiv zon"},
        {"front": "firewall-cmd --add-service=http?", "back": "Öppnar HTTP (port 80)"},
        {"front": "firewall-cmd --add-port=8080/tcp?", "back": "Öppnar port 8080 TCP"},
    ],
    "medium": [
        {"front": "Korrekt ordning för permanent regel?", "back": "--permanent → --reload"},
        {"front": "firewall-cmd --get-active-zones?", "back": "Visar aktiva zoner"},
        {"front": "Zone 'drop' gör?", "back": "Blockerar allt utan svar"},
        {"front": "Zone 'trusted' gör?", "back": "Tillåter allt"},
        {"front": "Zone 'internal' för?", "back": "Intern nätverkstrafik"},
        {"front": "firewall-cmd --remove-service?", "back": "Tar bort service-regel"},
        {"front": "firewall-cmd --runtime-to-permanent?", "back": "Sparar runtime-regler permanent"},
        {"front": "SELinux 'enforcing' betyder?", "back": "Aktiv och blockerar"},
        {"front": "SELinux 'permissive' betyder?", "back": "Loggar men blockerar inte"},
        {"front": "getenforce visar?", "back": "SELinux-läge"},
    ],
    "hard": [
        {"front": "SELinux blockerar SSH på ny port?", "back": "semanage port -a -t ssh_port_t -p tcp 6622"},
        {"front": "semanage port -l | grep ssh?", "back": "Lista SSH-relaterade portar"},
        {"front": "Tillfälligt disable SELinux?", "back": "setenforce 0"},
        {"front": "Permanent SELinux config?", "back": "/etc/selinux/config"},
        {"front": "firewall-cmd --add-rich-rule?", "back": "Avancerade regler"},
        {"front": "Rich rule: tillåt IP?", "back": "rule family=ipv4 source address=X accept"},
        {"front": "firewall-cmd --panic-on?", "back": "Blockerar ALL trafik (nödläge)"},
        {"front": "firewall-cmd --zone=home --change-interface=eth0?", "back": "Flyttar interface till zon"},
        {"front": "ss -tulpn | grep :6622?", "back": "Kontrollera att tjänst lyssnar"},
        {"front": "journalctl -t setroubleshoot?", "back": "SELinux-problemloggar"},
    ],
}

NOD_18_QUIZ = {
    "easy": [
        {"question": "firewalld används i?", "options": ["Ubuntu", "RHEL/CentOS/Rocky", "Alla", "macOS"], "correct": 1, "explanation": "Materialet: 'RHEL/Rocky/CentOS'"},
        {"question": "--permanent gör?", "options": ["Tillfällig", "Sparar permanent", "Permanent block", "Auto"], "correct": 1, "explanation": "Materialet: '--permanent sparar regeln'"},
        {"question": "Utan --reload?", "options": ["Fungerar direkt", "Permanenta aktiveras inte", "Reload auto", "Error"], "correct": 1, "explanation": "Materialet: '--reload KRÄVS'"},
        {"question": "Default zon?", "options": ["home", "public", "work", "trusted"], "correct": 1, "explanation": "Materialet: 'Default: public'"},
        {"question": "--list-all visar?", "options": ["Alla zoner", "Alla regler i zon", "All config", "List"], "correct": 1, "explanation": "Materialet: 'firewall-cmd --list-all'"},
        {"question": "--add-service=http öppnar?", "options": ["SSH", "HTTP (80)", "HTTPS", "FTP"], "correct": 1, "explanation": "Materialet: '--add-service=http'"},
        {"question": "--state visar?", "options": ["State info", "Om brandväggen är aktiv", "Status text", "States"], "correct": 1, "explanation": "Materialet: '--state'"},
    ],
    "medium": [
        {"question": "Korrekt ordning?", "options": ["--reload → --permanent", "--permanent → --reload", "Spelar ingen roll", "--add → --permanent"], "correct": 1, "explanation": "Materialet: '--permanent → --reload'"},
        {"question": "Zon 'drop' gör?", "options": ["Droppar paket", "Blockerar utan svar", "Drop zone", "Tar bort"], "correct": 1, "explanation": "Materialet: 'drop = Blockera allt utan svar'"},
        {"question": "Zon 'trusted' gör?", "options": ["Verifierar", "Tillåter allt", "Trust check", "Litar på"], "correct": 1, "explanation": "Materialet: 'trusted = Tillåt allt'"},
        {"question": "--runtime-to-permanent?", "options": ["Runtime mode", "Sparar runtime permanent", "Permanent runtime", "Convert"], "correct": 1, "explanation": "Materialet: '--runtime-to-permanent'"},
        {"question": "getenforce visar?", "options": ["Enforce rules", "SELinux-läge", "Get info", "Force mode"], "correct": 1, "explanation": "Materialet: 'getenforce'"},
        {"question": "SELinux 'enforcing'?", "options": ["Av", "Aktiv och blockerar", "Loggar bara", "Enforce"], "correct": 1, "explanation": "Materialet: 'enforcing = aktiv'"},
        {"question": "--get-active-zones?", "options": ["Lista alla", "Visar aktiva zoner", "Get zones", "Zone info"], "correct": 1, "explanation": "Materialet: '--get-active-zones'"},
    ],
    "hard": [
        {"question": "SSH på ny port + SELinux?", "options": ["Bara firewall", "semanage port -a -t ssh_port_t", "SELinux off", "Auto"], "correct": 1, "explanation": "Materialet: 'semanage port -a -t ssh_port_t -p tcp 6622'"},
        {"question": "Tillfälligt disable SELinux?", "options": ["selinux off", "setenforce 0", "disable selinux", "echo 0"], "correct": 1, "explanation": "Materialet: 'setenforce 0'"},
        {"question": "SELinux permanent config?", "options": ["/etc/selinux.conf", "/etc/selinux/config", "~/.selinux", "/selinux"], "correct": 1, "explanation": "Materialet: '/etc/selinux/config'"},
        {"question": "--panic-on gör?", "options": ["Panik meddelande", "Blockerar ALL trafik", "Panic mode", "Emergency"], "correct": 1, "explanation": "Materialet: '--panic-on = blockera allt'"},
        {"question": "Rich rule syntax?", "options": ["--rich", "rule family=ipv4...", "--add-rich", "rich-rule add"], "correct": 1, "explanation": "Materialet: 'rule family=ipv4 source address=X accept'"},
        {"question": "SELinux-problemloggar?", "options": ["syslog", "journalctl -t setroubleshoot", "/var/log/selinux", "audit.log"], "correct": 1, "explanation": "Materialet: 'setroubleshoot'"},
    ],
}

# =============================================================================
# NOD 19: LAGRING (FDISK, LUKS, MKFS, MOUNT)
# Källa: nod_lagring.py
# Koncept: fdisk, LUKS-kryptering, mkfs.ext4, mount, /etc/fstab
# =============================================================================

NOD_19_FLASHCARDS = {
    "easy": [
        {"front": "lsblk visar?", "back": "Blockenheter och deras struktur"},
        {"front": "fdisk -l visar?", "back": "Alla diskar och partitioner"},
        {"front": "fdisk /dev/sdb öppnar?", "back": "Partitioneringsverktyg för disk"},
        {"front": "fdisk: n gör?", "back": "Skapar ny partition"},
        {"front": "fdisk: w gör?", "back": "Skriver och sparar ändringar"},
        {"front": "mkfs.ext4 /dev/sdb1?", "back": "Skapar ext4-filsystem"},
        {"front": "mount /dev/sdb1 /mnt?", "back": "Monterar partition till /mnt"},
        {"front": "umount /mnt?", "back": "Avmonterar /mnt"},
        {"front": "/etc/fstab är?", "back": "Automatisk montering vid boot"},
        {"front": "df -h visar?", "back": "Diskutrymme för monterade FS"},
    ],
    "medium": [
        {"front": "LUKS används för?", "back": "Diskkryptering"},
        {"front": "cryptsetup luksFormat /dev/sdb1?", "back": "Krypterar partitionen"},
        {"front": "cryptsetup luksOpen gör?", "back": "Öppnar krypterad disk"},
        {"front": "/dev/mapper/namn?", "back": "Dekrypterad disk för mount"},
        {"front": "UUID i fstab: varför?", "back": "Unik - ändras inte om diskar byter ordning"},
        {"front": "blkid visar?", "back": "UUID och typ för blockenheter"},
        {"front": "mount -a gör?", "back": "Monterar allt i fstab"},
        {"front": "fstab-fält?", "back": "enhet mountpoint typ options dump pass"},
        {"front": "nofail i fstab?", "back": "Boot fortsätter även om mount misslyckas"},
        {"front": "0 0 i fstab (dump/pass)?", "back": "Ingen backup/check vid boot"},
    ],
    "hard": [
        {"front": "fstab: UUID=xxx /data ext4 defaults,nofail 0 2?", "back": "Monterar UUID till /data med fsck check"},
        {"front": "LUKS + auto-mount: crypttab?", "back": "Konfigurerar krypto-mount vid boot"},
        {"front": "/etc/crypttab syntax?", "back": "namn UUID=xxx keyfile luks"},
        {"front": "mkfs.xfs vs ext4?", "back": "XFS = stora filer, ext4 = generellt"},
        {"front": "resize2fs gör?", "back": "Ändrar storlek på ext4"},
        {"front": "fdisk: p visar?", "back": "Print/visar partitionstabellen"},
        {"front": "fdisk: d tar bort?", "back": "Partition"},
        {"front": "parted vs fdisk?", "back": "parted = GPT-diskar, fdisk = MBR/GPT"},
        {"front": "luksAddKey gör?", "back": "Lägger till extra LUKS-nyckel"},
        {"front": "Testa fstab utan reboot?", "back": "mount -a"},
    ],
}

NOD_19_QUIZ = {
    "easy": [
        {"question": "lsblk visar?", "options": ["Loggar", "Blockenheter", "Links", "Libraries"], "correct": 1, "explanation": "Materialet: 'lsblk = blockenheter'"},
        {"question": "fdisk: n gör?", "options": ["Nothing", "Ny partition", "Name", "Next"], "correct": 1, "explanation": "Materialet: 'n = Ny partition'"},
        {"question": "fdisk: w gör?", "options": ["Wait", "Skriver ändringar", "Warning", "Width"], "correct": 1, "explanation": "Materialet: 'w = Write/spara'"},
        {"question": "mkfs.ext4 gör?", "options": ["Mount", "Skapar ext4 filsystem", "Make file", "Move"], "correct": 1, "explanation": "Materialet: 'mkfs.ext4 = skapa filsystem'"},
        {"question": "mount /dev/sdb1 /mnt?", "options": ["Move", "Monterar till /mnt", "Make mount", "Multiple"], "correct": 1, "explanation": "Materialet: 'mount = montera'"},
        {"question": "/etc/fstab för?", "options": ["Fast tab", "Auto-mount vid boot", "File system", "Fstab config"], "correct": 1, "explanation": "Materialet: 'fstab = automatisk montering'"},
        {"question": "df -h visar?", "options": ["Disk files", "Diskutrymme", "Directory", "Data free"], "correct": 1, "explanation": "Materialet: 'df -h = diskutrymme'"},
    ],
    "medium": [
        {"question": "LUKS används för?", "options": ["Linux Users", "Diskkryptering", "Lock", "Linux Unified"], "correct": 1, "explanation": "Materialet: 'LUKS = Linux Unified Key Setup'"},
        {"question": "cryptsetup luksOpen?", "options": ["Öppnar krypterad disk", "Skapar krypto", "Close", "Lock"], "correct": 0, "explanation": "Materialet: 'luksOpen öppnar'"},
        {"question": "/dev/mapper/namn?", "options": ["Mapper config", "Dekrypterad disk", "Map file", "Device map"], "correct": 1, "explanation": "Materialet: 'Öppnad disk visas i /dev/mapper/'"},
        {"question": "UUID i fstab: varför?", "options": ["Unique", "Ändras inte om diskar byter", "Universal", "User ID"], "correct": 1, "explanation": "Materialet: 'UUID = stabil referens'"},
        {"question": "blkid visar?", "options": ["Block ID", "UUID och typ", "Blockerar", "BLK"], "correct": 1, "explanation": "Materialet: 'blkid = visa UUID'"},
        {"question": "mount -a gör?", "options": ["Mount all", "Monterar allt i fstab", "All mounts", "Append"], "correct": 1, "explanation": "Materialet: 'mount -a'"},
        {"question": "nofail i fstab?", "options": ["No failures", "Boot fortsätter vid fel", "Fail mode", "No file"], "correct": 1, "explanation": "Materialet: 'nofail = boot fortsätter'"},
    ],
    "hard": [
        {"question": "LUKS + auto-mount config?", "options": ["/etc/luks", "/etc/crypttab", "~/.luks", "/luks.conf"], "correct": 1, "explanation": "Materialet: '/etc/crypttab'"},
        {"question": "resize2fs gör?", "options": ["Resize file", "Ändrar storlek på ext4", "Reformat", "Reset"], "correct": 1, "explanation": "resize2fs = resize ext2/3/4"},
        {"question": "parted vs fdisk?", "options": ["Samma", "parted = GPT, fdisk = MBR/GPT", "fdisk bättre", "parted äldre"], "correct": 1, "explanation": "Materialet: 'parted för GPT'"},
        {"question": "Testa fstab utan reboot?", "options": ["systemctl mount", "mount -a", "fstab test", "boot test"], "correct": 1, "explanation": "Materialet: 'mount -a'"},
        {"question": "luksAddKey gör?", "options": ["Lägger till", "Ny LUKS-nyckel", "Add to LUKS", "Key generation"], "correct": 1, "explanation": "Materialet: 'luksAddKey'"},
        {"question": "fstab: 0 2 betyder?", "options": ["0 backup, 2 check", "0 dump, 2 fsck-pass", "Order", "Priority 2"], "correct": 1, "explanation": "Materialet: 'dump=0, pass=2 (fsck check)'"},
    ],
}

# =============================================================================
# NOD 20: BACKUP MED TAR
# Källa: nod_backup_tar.py
# Koncept: tar -czvf, -xzvf, -tzvf, inkrementell backup med -g
# =============================================================================

NOD_20_FLASHCARDS = {
    "easy": [
        {"front": "tar står för?", "back": "Tape Archive"},
        {"front": "tar -c gör?", "back": "Create/skapa arkiv"},
        {"front": "tar -x gör?", "back": "Extract/packa upp"},
        {"front": "tar -t gör?", "back": "List/visa innehåll"},
        {"front": "tar -z gör?", "back": "Komprimera med gzip"},
        {"front": "tar -v gör?", "back": "Verbose/visa filer"},
        {"front": "tar -f gör?", "back": "Ange filnamn"},
        {"front": "tar -czvf backup.tar.gz katalog?", "back": "Skapa komprimerad backup"},
        {"front": "tar -xzvf backup.tar.gz?", "back": "Packa upp backup"},
        {"front": "tar -tzvf backup.tar.gz?", "back": "Lista innehåll utan att packa upp"},
    ],
    "medium": [
        {"front": "Minnesregel CZVF?", "back": "Create Zippad Verbose File"},
        {"front": "tar --exclude='*.log'?", "back": "Exkluderar .log-filer"},
        {"front": "tar -C /path?", "back": "Change directory före extract"},
        {"front": ".tar.gz vs .tgz?", "back": "Samma sak"},
        {"front": "tar -j gör?", "back": "Komprimera med bzip2"},
        {"front": ".tar.bz2 komprimering?", "back": "bzip2 (bättre komprimering)"},
        {"front": "tar -xzvf arkiv -C /dest?", "back": "Extrahera till specifik katalog"},
        {"front": "Inkrementell backup?", "back": "Bara ändrade filer sedan förra"},
        {"front": "tar -g snapshot?", "back": "Använder snapshot-fil för inkrementell"},
        {"front": "Full + inkrementell strategi?", "back": "Full varje vecka, inkr dagligen"},
    ],
    "hard": [
        {"front": "tar -g snapshot -czvf full.tar.gz dir?", "back": "Full backup, skapar snapshot"},
        {"front": "Samma -g kommando igen?", "back": "Inkrementell (bara ändringar)"},
        {"front": "--listed-incremental?", "back": "Samma som -g"},
        {"front": "Restore inkrementell?", "back": "Packa upp full FÖRST, sedan inkr i ordning"},
        {"front": "tar --verify?", "back": "Verifierar arkiv efter skapande"},
        {"front": "tar -uf arkiv.tar fil?", "back": "Update/lägg till fil om nyare"},
        {"front": "tar --newer-mtime='datum'?", "back": "Bara filer ändrade efter datum"},
        {"front": "tar -r gör?", "back": "Append/lägg till filer i arkiv"},
        {"front": "Varför inte komprimera med -u?", "back": "-u fungerar inte på komprimerade arkiv"},
        {"front": "tar -xvf - < stream?", "back": "Läser från stdin"},
    ],
}

NOD_20_QUIZ = {
    "easy": [
        {"question": "tar -c gör?", "options": ["Copy", "Create arkiv", "Change", "Check"], "correct": 1, "explanation": "Materialet: '-c = Create'"},
        {"question": "tar -x gör?", "options": ["Exit", "Extract", "Execute", "Extend"], "correct": 1, "explanation": "Materialet: '-x = eXtract'"},
        {"question": "tar -z använder?", "options": ["zip", "gzip", "bzip2", "xz"], "correct": 1, "explanation": "Materialet: '-z = gZip'"},
        {"question": "tar -v gör?", "options": ["Verify", "Verbose", "Version", "View"], "correct": 1, "explanation": "Materialet: '-v = Verbose'"},
        {"question": "-czvf minnesregel?", "options": ["Copy Zip Verify File", "Create Zippad Verbose File", "Check Zip Var File", "Create Z Version"], "correct": 1, "explanation": "Materialet: 'Create Zippad Verbose File'"},
        {"question": "tar -tzvf?", "options": ["Test", "Listar innehåll", "Tar test", "Type"], "correct": 1, "explanation": "Materialet: '-t = lista'"},
        {"question": "tar -f anger?", "options": ["Force", "Filnamn", "Format", "Flag"], "correct": 1, "explanation": "Materialet: '-f = File'"},
    ],
    "medium": [
        {"question": "--exclude='*.log' gör?", "options": ["Inkluderar logs", "Exkluderar .log", "Exclude all", "Exception"], "correct": 1, "explanation": "Materialet: '--exclude exkluderar'"},
        {"question": "tar -C /path?", "options": ["Create path", "Change directory", "Copy path", "Check"], "correct": 1, "explanation": "Materialet: '-C = byt katalog före extract'"},
        {"question": ".tar.gz vs .tgz?", "options": ["Olika format", "Samma sak", "tgz bättre", "gz nyare"], "correct": 1, "explanation": "Materialet: 'Samma sak'"},
        {"question": "tar -j komprimerar med?", "options": ["gzip", "bzip2", "xz", "zip"], "correct": 1, "explanation": "Materialet: '-j = bzip2'"},
        {"question": "tar -g används för?", "options": ["Grep", "Inkrementell backup", "Group", "Generate"], "correct": 1, "explanation": "Materialet: '-g = snapshot för inkrementell'"},
        {"question": "Inkrementell backup innebär?", "options": ["Allt varje gång", "Bara ändrade filer", "Increment counter", "Backup inkrement"], "correct": 1, "explanation": "Materialet: 'Bara ändrade filer'"},
        {"question": "-xzvf arkiv -C /dest?", "options": ["Check dest", "Extract till dest", "Create dest", "Copy dest"], "correct": 1, "explanation": "Materialet: '-C anger destination'"},
    ],
    "hard": [
        {"question": "Inkrementell restore ordning?", "options": ["Senaste först", "Full först, sedan inkr i ordning", "Spelar ingen roll", "Bara senaste"], "correct": 1, "explanation": "Materialet: 'Full FÖRST, sedan inkrementella i ordning'"},
        {"question": "--listed-incremental?", "options": ["Lista inkr", "Samma som -g", "List increments", "Increment list"], "correct": 1, "explanation": "Materialet: '--listed-incremental = -g'"},
        {"question": "tar --verify?", "options": ["Verifierar syntax", "Verifierar arkiv efter skapande", "Verify tar", "Check archive"], "correct": 1, "explanation": "Materialet: '--verify'"},
        {"question": "tar -u på .tar.gz?", "options": ["Fungerar", "Fungerar INTE", "Auto decompress", "Update works"], "correct": 1, "explanation": "Materialet: '-u fungerar inte på komprimerade'"},
        {"question": "tar -r gör?", "options": ["Read", "Append filer till arkiv", "Recursive", "Remove"], "correct": 1, "explanation": "Materialet: '-r = append'"},
        {"question": "tar --newer-mtime?", "options": ["Newer tar", "Filer ändrade efter datum", "New files", "Modify time"], "correct": 1, "explanation": "Materialet: '--newer-mtime'"},
    ],
}

# =============================================================================
# NOD 21: SYSTEMD
# Källa: nod_systemd.py
# Koncept: systemctl, enable --now, daemon-reload, journalctl
# =============================================================================

NOD_21_FLASHCARDS = {
    "easy": [
        {"front": "systemd är?", "back": "Init-system och service manager"},
        {"front": "systemctl start nginx?", "back": "Startar nginx nu"},
        {"front": "systemctl stop nginx?", "back": "Stoppar nginx"},
        {"front": "systemctl restart nginx?", "back": "Startar om nginx"},
        {"front": "systemctl status nginx?", "back": "Visar status för nginx"},
        {"front": "systemctl enable nginx?", "back": "Startar automatiskt vid boot"},
        {"front": "systemctl disable nginx?", "back": "Tar bort autostart"},
        {"front": "systemctl enable --now nginx?", "back": "Enable OCH start direkt"},
        {"front": "journalctl -u nginx?", "back": "Visar loggar för nginx"},
        {"front": "journalctl -f?", "back": "Follow/realtidsloggar"},
    ],
    "medium": [
        {"front": "systemctl daemon-reload?", "back": "Laddar om unit-filer efter ändring"},
        {"front": "När krävs daemon-reload?", "back": "Efter ändring av .service-fil"},
        {"front": "/etc/systemd/system/ är?", "back": "Plats för egna unit-filer"},
        {"front": "/usr/lib/systemd/system/ är?", "back": "System-unit-filer (paket)"},
        {"front": "Unit-fil suffix?", "back": ".service, .timer, .socket"},
        {"front": "systemctl list-units?", "back": "Visar aktiva units"},
        {"front": "systemctl list-unit-files?", "back": "Visar alla unit-filer"},
        {"front": "systemctl is-enabled nginx?", "back": "Kollar om enabled"},
        {"front": "systemctl is-active nginx?", "back": "Kollar om aktiv"},
        {"front": "journalctl -u nginx -n 50?", "back": "Senaste 50 raderna"},
    ],
    "hard": [
        {"front": "Minimal .service-fil sektioner?", "back": "[Unit], [Service], [Install]"},
        {"front": "[Service] ExecStart=?", "back": "Kommando som startar tjänsten"},
        {"front": "[Service] Restart=always?", "back": "Startar om vid krasch"},
        {"front": "[Install] WantedBy=multi-user.target?", "back": "Startar i normal runlevel"},
        {"front": "Type=simple vs forking?", "back": "simple = main process, forking = dämon-stil"},
        {"front": "WorkingDirectory=?", "back": "Sätter arbetskatalog"},
        {"front": "User=appuser?", "back": "Kör som specifik användare"},
        {"front": "Environment=VAR=val?", "back": "Sätter miljövariabel"},
        {"front": "EnvironmentFile=/path?", "back": "Laddar variabler från fil"},
        {"front": "journalctl --since 'today'?", "back": "Loggar sedan midnatt"},
    ],
}

NOD_21_QUIZ = {
    "easy": [
        {"question": "systemctl start nginx?", "options": ["Startar vid boot", "Startar nu", "System start", "Start all"], "correct": 1, "explanation": "Materialet: 'start = starta nu'"},
        {"question": "systemctl enable nginx?", "options": ["Startar nu", "Autostart vid boot", "Enable all", "Enable now"], "correct": 1, "explanation": "Materialet: 'enable = starta vid boot'"},
        {"question": "enable --now gör?", "options": ["Enable only", "Enable OCH start", "Now enable", "Enable now only"], "correct": 1, "explanation": "Materialet: 'enable --now = båda'"},
        {"question": "journalctl -u nginx?", "options": ["User nginx", "Loggar för nginx", "Unit nginx", "Update"], "correct": 1, "explanation": "Materialet: '-u = unit loggar'"},
        {"question": "journalctl -f?", "options": ["File", "Follow/realtid", "Find", "Filter"], "correct": 1, "explanation": "Materialet: '-f = follow'"},
        {"question": "systemctl status visar?", "options": ["Start status", "Tjänstens status", "System status", "Stats"], "correct": 1, "explanation": "Materialet: 'status'"},
        {"question": "systemctl restart?", "options": ["Reset", "Startar om tjänst", "Restart system", "Reset config"], "correct": 1, "explanation": "Materialet: 'restart'"},
    ],
    "medium": [
        {"question": "daemon-reload krävs när?", "options": ["Alltid", "Efter ändring av .service", "Efter restart", "Dagligen"], "correct": 1, "explanation": "Materialet: 'daemon-reload efter ändringar'"},
        {"question": "Egna unit-filer placeras i?", "options": ["/usr/lib/systemd/", "/etc/systemd/system/", "~/.systemd", "/systemd/"], "correct": 1, "explanation": "Materialet: '/etc/systemd/system/'"},
        {"question": "systemctl list-units?", "options": ["Alla units", "Aktiva units", "Unit files", "List all"], "correct": 1, "explanation": "Materialet: 'list-units = aktiva'"},
        {"question": "is-enabled kollar?", "options": ["Om aktiv", "Om enabled vid boot", "Is enable", "Enable check"], "correct": 1, "explanation": "Materialet: 'is-enabled'"},
        {"question": "journalctl -n 50?", "options": ["Next 50", "Senaste 50 rader", "Number 50", "50 units"], "correct": 1, "explanation": "Materialet: '-n = antal rader'"},
        {"question": "Unit-fil suffix för timer?", "options": [".service", ".timer", ".cron", ".schedule"], "correct": 1, "explanation": "Materialet: '.timer'"},
        {"question": "is-active kollar?", "options": ["Om enabled", "Om aktiv/running", "Active check", "Activity"], "correct": 1, "explanation": "Materialet: 'is-active'"},
    ],
    "hard": [
        {"question": ".service sektioner?", "options": ["[Service] bara", "[Unit], [Service], [Install]", "[Config], [Run]", "[Start], [Stop]"], "correct": 1, "explanation": "Materialet: 'Tre huvudsektioner'"},
        {"question": "ExecStart=?", "options": ["Start script", "Kommando som startar tjänst", "Execute start", "Startup"], "correct": 1, "explanation": "Materialet: 'ExecStart = startkommando'"},
        {"question": "Restart=always?", "options": ["Restart always", "Startar om vid krasch", "Always restart", "Restart loop"], "correct": 1, "explanation": "Materialet: 'Restart=always'"},
        {"question": "WantedBy=multi-user.target?", "options": ["Multi user", "Normal runlevel", "Multi target", "Wanted"], "correct": 1, "explanation": "Materialet: 'multi-user.target = normal boot'"},
        {"question": "Type=forking för?", "options": ["Fork process", "Dämon-stil (forks)", "Forking type", "Fork run"], "correct": 1, "explanation": "Materialet: 'forking = dämon'"},
        {"question": "EnvironmentFile=?", "options": ["Env file", "Laddar variabler från fil", "Environment", "File env"], "correct": 1, "explanation": "Materialet: 'EnvironmentFile=/path'"},
    ],
}

# =============================================================================
# NOD 22: DOCKER GRUNDER
# Källa: nod_docker_grunder.py
# Koncept: containers share kernel, docker run -d/-it/--rm, docker ps
# =============================================================================

NOD_22_FLASHCARDS = {
    "easy": [
        {"front": "Docker container vs VM?", "back": "Container delar kernel, VM har egen"},
        {"front": "docker run nginx?", "back": "Kör nginx-container"},
        {"front": "docker run -d?", "back": "Detached/bakgrund"},
        {"front": "docker run -it?", "back": "Interactive terminal"},
        {"front": "docker run --rm?", "back": "Ta bort container när den stoppas"},
        {"front": "docker ps?", "back": "Visar körande containers"},
        {"front": "docker ps -a?", "back": "Visar ALLA containers (även stoppade)"},
        {"front": "docker stop ID?", "back": "Stoppar container"},
        {"front": "docker start ID?", "back": "Startar stoppad container"},
        {"front": "docker rm ID?", "back": "Tar bort container"},
    ],
    "medium": [
        {"front": "docker run -p 8080:80?", "back": "Host:Container port-mapping"},
        {"front": "docker run -v /host:/container?", "back": "Volym-mapping"},
        {"front": "docker run -e VAR=val?", "back": "Sätter miljövariabel"},
        {"front": "docker run --name myapp?", "back": "Ger containern ett namn"},
        {"front": "docker exec -it ID bash?", "back": "Kör bash i körande container"},
        {"front": "docker logs ID?", "back": "Visar container-loggar"},
        {"front": "docker logs -f ID?", "back": "Follow/realtidsloggar"},
        {"front": "docker inspect ID?", "back": "Detaljerad container-info"},
        {"front": "docker images?", "back": "Listar lokala images"},
        {"front": "docker pull nginx?", "back": "Laddar ner nginx-image"},
    ],
    "hard": [
        {"front": "docker system prune?", "back": "Tar bort oanvända resurser"},
        {"front": "docker system prune -a?", "back": "Tar bort ALLT oanvänt (inkl images)"},
        {"front": "docker network create mynet?", "back": "Skapar eget nätverk"},
        {"front": "--network mynet?", "back": "Ansluter container till nätverk"},
        {"front": "docker volume create myvol?", "back": "Skapar namngiven volym"},
        {"front": "-v myvol:/data?", "back": "Monterar namngiven volym"},
        {"front": "docker cp fil ID:/path?", "back": "Kopierar fil till container"},
        {"front": "docker stats?", "back": "Realtidsresursanvändning"},
        {"front": "docker top ID?", "back": "Processer i container"},
        {"front": "CONTAINER_ID i skript?", "back": "$(docker run -d nginx)"},
    ],
}

NOD_22_QUIZ = {
    "easy": [
        {"question": "Container vs VM: kernel?", "options": ["Egen kernel båda", "Container delar kernel", "VM delar kernel", "Ingen kernel"], "correct": 1, "explanation": "Materialet: 'Containers delar kernel med host'"},
        {"question": "docker run -d?", "options": ["Delete", "Detached/bakgrund", "Debug", "Direct"], "correct": 1, "explanation": "Materialet: '-d = detached'"},
        {"question": "docker run -it?", "options": ["Install terminal", "Interactive terminal", "IT run", "In terminal"], "correct": 1, "explanation": "Materialet: '-it = interaktiv terminal'"},
        {"question": "docker ps -a visar?", "options": ["Bara körande", "ALLA containers", "All images", "All processes"], "correct": 1, "explanation": "Materialet: '-a = alla'"},
        {"question": "docker stop gör?", "options": ["Tar bort", "Stoppar container", "Stop all", "System stop"], "correct": 1, "explanation": "Materialet: 'stop = stoppa'"},
        {"question": "docker rm gör?", "options": ["Remove image", "Tar bort container", "Remove all", "Reset"], "correct": 1, "explanation": "Materialet: 'rm = ta bort'"},
        {"question": "--rm flagga?", "options": ["Remove image", "Auto-remove vid stopp", "Remove manual", "RM forced"], "correct": 1, "explanation": "Materialet: '--rm = auto-remove'"},
    ],
    "medium": [
        {"question": "-p 8080:80 betyder?", "options": ["Port 8080", "Host 8080 → Container 80", "8080 and 80", "Port mapping 80"], "correct": 1, "explanation": "Materialet: 'host:container'"},
        {"question": "-v /host:/container?", "options": ["Volume", "Volym-mapping", "Version", "Variable"], "correct": 1, "explanation": "Materialet: '-v = volym'"},
        {"question": "-e VAR=val?", "options": ["Execute", "Miljövariabel", "Environment", "Error"], "correct": 1, "explanation": "Materialet: '-e = environment'"},
        {"question": "docker exec -it ID bash?", "options": ["Execute bash", "Bash i körande container", "Exec bash", "External bash"], "correct": 1, "explanation": "Materialet: 'exec = kör i container'"},
        {"question": "docker logs -f?", "options": ["File logs", "Follow/realtid", "Full logs", "Filter"], "correct": 1, "explanation": "Materialet: '-f = follow'"},
        {"question": "docker images?", "options": ["Image info", "Listar lokala images", "Images all", "Image list"], "correct": 1, "explanation": "Materialet: 'images = lista'"},
        {"question": "--name myapp?", "options": ["Name file", "Ger container namn", "Named app", "Name run"], "correct": 1, "explanation": "Materialet: '--name = sätt namn'"},
    ],
    "hard": [
        {"question": "docker system prune -a?", "options": ["Prune all", "Tar bort allt oanvänt", "Prune active", "All prune"], "correct": 1, "explanation": "Materialet: 'prune -a = allt oanvänt'"},
        {"question": "docker network create?", "options": ["Network config", "Skapar eget nätverk", "Network add", "Create net"], "correct": 1, "explanation": "Materialet: 'network create'"},
        {"question": "docker volume create?", "options": ["Volume add", "Skapar namngiven volym", "Create vol", "Volume new"], "correct": 1, "explanation": "Materialet: 'volume create'"},
        {"question": "docker cp?", "options": ["Copy process", "Kopierar fil till/från container", "Container process", "Copy"], "correct": 1, "explanation": "Materialet: 'cp = kopiera'"},
        {"question": "docker stats?", "options": ["Statistics", "Realtidsresursanvändning", "Status", "Static"], "correct": 1, "explanation": "Materialet: 'stats = realtid'"},
        {"question": "docker top ID?", "options": ["Top command", "Processer i container", "Top container", "Top ID"], "correct": 1, "explanation": "Materialet: 'top = processer'"},
    ],
}

# =============================================================================
# NOD 23: DOCKER IMAGES & DOCKERFILE
# Källa: nod_docker_images.py
# Koncept: Image vs Container, Dockerfile, layers, caching, multi-stage
# =============================================================================

NOD_23_FLASHCARDS = {
    "easy": [
        {"front": "Image vs Container?", "back": "Image = recept (read-only), Container = körande instans"},
        {"front": "Dockerfile är?", "back": "Instruktionsfil för att bygga image"},
        {"front": "docker build -t namn .?", "back": "Bygger image från Dockerfile"},
        {"front": "FROM i Dockerfile?", "back": "Basimage att bygga på"},
        {"front": "RUN i Dockerfile?", "back": "Kör kommando under bygge"},
        {"front": "COPY i Dockerfile?", "back": "Kopierar filer till image"},
        {"front": "WORKDIR i Dockerfile?", "back": "Sätter arbetskatalog"},
        {"front": "CMD i Dockerfile?", "back": "Standardkommando vid container-start"},
        {"front": "EXPOSE i Dockerfile?", "back": "Dokumenterar vilken port som används"},
        {"front": "docker rmi image?", "back": "Tar bort image"},
    ],
    "medium": [
        {"front": "Varje Dockerfile-instruktion skapar?", "back": "Ett nytt lager (layer)"},
        {"front": "Varför kombinera RUN-kommandon?", "back": "Färre lager, mindre image"},
        {"front": "RUN apt update && apt install -y?", "back": "Kombinerar i ett lager"},
        {"front": "ENTRYPOINT vs CMD?", "back": "ENTRYPOINT = fast kommando, CMD = default args"},
        {"front": "ADD vs COPY?", "back": "ADD kan extrahera .tar, COPY är enklare"},
        {"front": "ARG i Dockerfile?", "back": "Bygg-tid variabel"},
        {"front": "ENV i Dockerfile?", "back": "Miljövariabel i image och container"},
        {"front": ".dockerignore är?", "back": "Filer som ignoreras vid COPY/ADD"},
        {"front": "docker tag image newname?", "back": "Skapar ny tagg för image"},
        {"front": "docker push image?", "back": "Pushar till registry"},
    ],
    "hard": [
        {"front": "Multi-stage build?", "back": "Flera FROM - bygger i en, kopierar till minimal"},
        {"front": "FROM node AS builder?", "back": "Namnger byggsteg"},
        {"front": "COPY --from=builder /app /app?", "back": "Kopierar från tidigare steg"},
        {"front": "Varför multi-stage?", "back": "Mindre final image - ingen build-verktyg"},
        {"front": "Layer-caching ordning?", "back": "Sällan-ändrade först för bättre cache"},
        {"front": "COPY package*.json ./ FÖRE kod?", "back": "Cache:ar npm install om bara kod ändras"},
        {"front": "RUN --mount=type=cache?", "back": "Persistent cache mellan builds"},
        {"front": "HEALTHCHECK i Dockerfile?", "back": "Definierar hälsokontroll"},
        {"front": "USER i Dockerfile?", "back": "Kör som non-root user"},
        {"front": "docker history image?", "back": "Visar alla lager i image"},
    ],
}

NOD_23_QUIZ = {
    "easy": [
        {"question": "Image vs Container?", "options": ["Samma", "Image = körande", "Image = recept, Container = körande", "Container = recept"], "correct": 2, "explanation": "Materialet: 'Image = read-only recept'"},
        {"question": "Dockerfile är?", "options": ["Docker file", "Instruktionsfil för image", "Config", "Log file"], "correct": 1, "explanation": "Materialet: 'Dockerfile = byggfil'"},
        {"question": "docker build -t namn .?", "options": ["Build container", "Bygger image", "Build all", "Tag build"], "correct": 1, "explanation": "Materialet: 'build -t = bygg och tagga'"},
        {"question": "FROM i Dockerfile?", "options": ["From where", "Basimage", "From file", "From config"], "correct": 1, "explanation": "Materialet: 'FROM = basimage'"},
        {"question": "RUN gör?", "options": ["Run container", "Kör kommando under bygge", "Run image", "Run all"], "correct": 1, "explanation": "Materialet: 'RUN = bygg-kommando'"},
        {"question": "COPY gör?", "options": ["Copy container", "Kopierar filer till image", "Copy config", "Copy all"], "correct": 1, "explanation": "Materialet: 'COPY = kopiera'"},
        {"question": "CMD definierar?", "options": ["Command build", "Standardkommando vid start", "CMD run", "Command file"], "correct": 1, "explanation": "Materialet: 'CMD = start-kommando'"},
    ],
    "medium": [
        {"question": "Varje instruktion skapar?", "options": ["Container", "Nytt lager", "Image", "Config"], "correct": 1, "explanation": "Materialet: 'Varje rad = nytt lager'"},
        {"question": "Kombinera RUN för?", "options": ["Snabbare", "Färre lager, mindre image", "Lättare läsa", "Debug"], "correct": 1, "explanation": "Materialet: 'Kombinera för färre lager'"},
        {"question": "ENTRYPOINT vs CMD?", "options": ["Samma", "ENTRYPOINT fast, CMD args", "CMD fast", "Entry = CMD"], "correct": 1, "explanation": "Materialet: 'ENTRYPOINT = fast kommando'"},
        {"question": ".dockerignore gör?", "options": ["Ignorerar Docker", "Ignorerar filer vid COPY", "Docker ignore", "Ignore all"], "correct": 1, "explanation": "Materialet: '.dockerignore'"},
        {"question": "ARG vs ENV?", "options": ["Samma", "ARG = bygg-tid, ENV = runtime", "ENV = bygg", "ARG = runtime"], "correct": 1, "explanation": "Materialet: 'ARG = bygg-tid'"},
        {"question": "docker tag gör?", "options": ["Tag container", "Skapar ny tagg för image", "Tag file", "Tag all"], "correct": 1, "explanation": "Materialet: 'tag = nytt namn'"},
        {"question": "docker push gör?", "options": ["Push container", "Pushar till registry", "Push local", "Push all"], "correct": 1, "explanation": "Materialet: 'push till registry'"},
    ],
    "hard": [
        {"question": "Multi-stage build?", "options": ["Flera builds", "Flera FROM - minimal final", "Multi Docker", "Stage builds"], "correct": 1, "explanation": "Materialet: 'Flera FROM för mindre image'"},
        {"question": "COPY --from=builder?", "options": ["Copy builder", "Kopierar från tidigare steg", "From build", "Copy from"], "correct": 1, "explanation": "Materialet: 'Kopiera från namngivet steg'"},
        {"question": "Layer cache ordning?", "options": ["Spelar ingen roll", "Sällan-ändrade först", "Ofta-ändrade först", "Alfabetisk"], "correct": 1, "explanation": "Materialet: 'Sällan-ändrade först = bättre cache'"},
        {"question": "COPY package*.json före kod?", "options": ["Ordning spelar ingen roll", "Cache:ar npm install", "Copy all first", "Package first"], "correct": 1, "explanation": "Materialet: 'Bättre caching av dependencies'"},
        {"question": "HEALTHCHECK gör?", "options": ["Check health", "Definierar hälsokontroll", "Health check", "Check config"], "correct": 1, "explanation": "Materialet: 'HEALTHCHECK'"},
        {"question": "USER i Dockerfile?", "options": ["User config", "Kör som non-root", "User name", "User all"], "correct": 1, "explanation": "Materialet: 'USER = non-root'"},
    ],
}

# =============================================================================
# NOD 24: DOCKER COMPOSE
# Källa: nod_docker_compose.py
# Koncept: docker-compose.yml, services, volumes, networks, depends_on
# =============================================================================

NOD_24_FLASHCARDS = {
    "easy": [
        {"front": "Docker Compose är?", "back": "Verktyg för multi-container setup"},
        {"front": "docker-compose.yml?", "back": "Konfigurationsfil för compose"},
        {"front": "docker compose up?", "back": "Startar alla services"},
        {"front": "docker compose up -d?", "back": "Startar i bakgrunden"},
        {"front": "docker compose down?", "back": "Stoppar och tar bort containers"},
        {"front": "docker compose ps?", "back": "Visar körande services"},
        {"front": "docker compose logs?", "back": "Visar loggar för alla services"},
        {"front": "services: i yml?", "back": "Definierar containers"},
        {"front": "volumes: i yml?", "back": "Definierar volymer"},
        {"front": "networks: i yml?", "back": "Definierar nätverk"},
    ],
    "medium": [
        {"front": "image: nginx i service?", "back": "Använder nginx-image"},
        {"front": "build: ./ i service?", "back": "Bygger från Dockerfile"},
        {"front": "ports: - '8080:80'?", "back": "Port-mapping"},
        {"front": "volumes: - ./app:/app?", "back": "Bind mount"},
        {"front": "environment: - VAR=val?", "back": "Miljövariabler"},
        {"front": "env_file: - .env?", "back": "Laddar env från fil"},
        {"front": "depends_on: - db?", "back": "Startar db före denna service"},
        {"front": "restart: always?", "back": "Startar om automatiskt"},
        {"front": "docker compose build?", "back": "Bygger alla images"},
        {"front": "docker compose pull?", "back": "Laddar ner alla images"},
    ],
    "hard": [
        {"front": "depends_on: db: condition: service_healthy?", "back": "Väntar tills db är healthy"},
        {"front": "healthcheck i compose?", "back": "test, interval, timeout, retries"},
        {"front": "docker compose --profile dev up?", "back": "Startar med specifik profil"},
        {"front": "profiles: - dev i service?", "back": "Service bara i dev-profil"},
        {"front": "docker compose exec web bash?", "back": "Kör bash i web-service"},
        {"front": "docker compose -f custom.yml up?", "back": "Använder annan compose-fil"},
        {"front": "networks: backend: driver: bridge?", "back": "Skapar bridge-nätverk"},
        {"front": "volumes: dbdata: driver: local?", "back": "Namngiven volym"},
        {"front": "docker compose down -v?", "back": "Tar bort volymer också"},
        {"front": "docker compose config?", "back": "Validerar och visar merged config"},
    ],
}

NOD_24_QUIZ = {
    "easy": [
        {"question": "Docker Compose för?", "options": ["En container", "Multi-container setup", "Compose music", "Docker config"], "correct": 1, "explanation": "Materialet: 'Multi-container'"},
        {"question": "docker compose up?", "options": ["Upload", "Startar alla services", "Update", "Up container"], "correct": 1, "explanation": "Materialet: 'up = starta'"},
        {"question": "docker compose up -d?", "options": ["Delete", "Detached/bakgrund", "Debug", "Down"], "correct": 1, "explanation": "Materialet: '-d = bakgrund'"},
        {"question": "docker compose down?", "options": ["Download", "Stoppar och tar bort", "Down load", "Down config"], "correct": 1, "explanation": "Materialet: 'down = stoppa och ta bort'"},
        {"question": "services: definierar?", "options": ["Services", "Containers", "Servers", "Service config"], "correct": 1, "explanation": "Materialet: 'services = containers'"},
        {"question": "volumes: definierar?", "options": ["Volume up", "Volymer", "Volume config", "Vol"], "correct": 1, "explanation": "Materialet: 'volumes = data'"},
        {"question": "docker compose ps?", "options": ["Process", "Körande services", "PS all", "Process status"], "correct": 1, "explanation": "Materialet: 'ps = status'"},
    ],
    "medium": [
        {"question": "build: ./ gör?", "options": ["Build all", "Bygger från Dockerfile", "Build config", "Build here"], "correct": 1, "explanation": "Materialet: 'build = bygg image'"},
        {"question": "ports: - '8080:80'?", "options": ["8080 ports", "Port-mapping", "Ports config", "80 to 8080"], "correct": 1, "explanation": "Materialet: 'host:container'"},
        {"question": "depends_on: - db?", "options": ["Depends on db", "Startar db först", "DB dependency", "On db"], "correct": 1, "explanation": "Materialet: 'depends_on = startordning'"},
        {"question": "restart: always?", "options": ["Restart config", "Auto-restart", "Always restart", "Restart all"], "correct": 1, "explanation": "Materialet: 'restart = auto'"},
        {"question": "env_file: - .env?", "options": ["Env file config", "Laddar env från fil", "Environment", "File env"], "correct": 1, "explanation": "Materialet: 'env_file'"},
        {"question": "docker compose build?", "options": ["Build compose", "Bygger alla images", "Build up", "Build config"], "correct": 1, "explanation": "Materialet: 'build = bygg images'"},
        {"question": "docker compose pull?", "options": ["Pull config", "Laddar ner images", "Pull all", "Pull compose"], "correct": 1, "explanation": "Materialet: 'pull = ladda ner'"},
    ],
    "hard": [
        {"question": "depends_on: condition: service_healthy?", "options": ["Health depends", "Väntar tills healthy", "Condition health", "Healthy start"], "correct": 1, "explanation": "Materialet: 'condition: service_healthy'"},
        {"question": "profiles: - dev gör?", "options": ["Profile dev", "Service bara i dev-profil", "Dev profile", "Profile config"], "correct": 1, "explanation": "Materialet: 'profiles = villkorlig service'"},
        {"question": "docker compose exec web bash?", "options": ["Execute web", "Bash i web-service", "Exec bash", "Web exec"], "correct": 1, "explanation": "Materialet: 'exec = kör i service'"},
        {"question": "docker compose down -v?", "options": ["Down verbose", "Tar bort volymer också", "Down version", "V down"], "correct": 1, "explanation": "Materialet: '-v = ta bort volymer'"},
        {"question": "docker compose config?", "options": ["Config file", "Validerar och visar config", "Config show", "Show config"], "correct": 1, "explanation": "Materialet: 'config = validera'"},
        {"question": "-f custom.yml?", "options": ["Force", "Använder annan compose-fil", "File custom", "F yml"], "correct": 1, "explanation": "Materialet: '-f = annan fil'"},
    ],
}

# =============================================================================
# NOD 25: GIT GRUNDER
# Källa: nod_git_basics.py
# Koncept: git add/commit/push, branching, merge, .gitignore, PR
# =============================================================================

NOD_25_FLASHCARDS = {
    "easy": [
        {"front": "git init?", "back": "Skapar nytt git-repo"},
        {"front": "git clone url?", "back": "Klonar repo från URL"},
        {"front": "git status?", "back": "Visar status för ändringar"},
        {"front": "git add fil?", "back": "Lägger till fil i staging"},
        {"front": "git add .?", "back": "Lägger till ALLA ändringar"},
        {"front": "git commit -m 'msg'?", "back": "Sparar ändringar med meddelande"},
        {"front": "git push?", "back": "Skickar commits till remote"},
        {"front": "git pull?", "back": "Hämtar och mergar från remote"},
        {"front": "git log?", "back": "Visar commit-historik"},
        {"front": ".gitignore är?", "back": "Filer som git ska ignorera"},
    ],
    "medium": [
        {"front": "git branch namn?", "back": "Skapar ny branch"},
        {"front": "git checkout -b namn?", "back": "Skapar OCH byter till branch"},
        {"front": "git switch namn?", "back": "Byter branch (nyare)"},
        {"front": "git merge feature?", "back": "Mergar feature till aktuell branch"},
        {"front": "git branch -d namn?", "back": "Tar bort lokal branch"},
        {"front": "git fetch?", "back": "Hämtar utan att merga"},
        {"front": "git diff?", "back": "Visar ändringar"},
        {"front": "git stash?", "back": "Sparar undan ändringar tillfälligt"},
        {"front": "git stash pop?", "back": "Återställer stash"},
        {"front": "git remote -v?", "back": "Visar remote URLs"},
    ],
    "hard": [
        {"front": "Pull Request (PR)?", "back": "Förfrågan att merga branch"},
        {"front": "git rebase vs merge?", "back": "rebase = linjär historik, merge = bevarar"},
        {"front": "git reset --hard HEAD~1?", "back": "Tar bort senaste commit helt"},
        {"front": "git reset --soft HEAD~1?", "back": "Flyttar HEAD, behåller ändringar"},
        {"front": "git revert commit?", "back": "Skapar ny commit som ångrar"},
        {"front": "Merge conflict lösning?", "back": "Redigera fil → add → commit"},
        {"front": "<<<<<<< HEAD?", "back": "Början på konflikt (din kod)"},
        {"front": "=======?", "back": "Separator i konflikt"},
        {"front": ">>>>>>> branch?", "back": "Slut på konflikt (deras kod)"},
        {"front": "git cherry-pick commit?", "back": "Plockar specifik commit till branch"},
    ],
}

NOD_25_QUIZ = {
    "easy": [
        {"question": "git init gör?", "options": ["Initialize", "Skapar nytt repo", "Init config", "Initial"], "correct": 1, "explanation": "Materialet: 'init = nytt repo'"},
        {"question": "git add . gör?", "options": ["Add one", "Alla ändringar till staging", "Add all files", "Add config"], "correct": 1, "explanation": "Materialet: 'add . = alla'"},
        {"question": "git commit -m?", "options": ["Commit message", "Sparar med meddelande", "Commit main", "Message commit"], "correct": 1, "explanation": "Materialet: '-m = meddelande'"},
        {"question": "git push gör?", "options": ["Push local", "Skickar till remote", "Push config", "Push all"], "correct": 1, "explanation": "Materialet: 'push = skicka'"},
        {"question": "git pull gör?", "options": ["Pull request", "Hämtar och mergar", "Pull config", "Pull all"], "correct": 1, "explanation": "Materialet: 'pull = hämta och merga'"},
        {"question": ".gitignore för?", "options": ["Ignore git", "Filer att ignorera", "Git ignore", "Ignore all"], "correct": 1, "explanation": "Materialet: '.gitignore'"},
        {"question": "git status visar?", "options": ["Git status", "Status för ändringar", "Status all", "File status"], "correct": 1, "explanation": "Materialet: 'status'"},
    ],
    "medium": [
        {"question": "git checkout -b namn?", "options": ["Checkout branch", "Skapar OCH byter branch", "Branch checkout", "B branch"], "correct": 1, "explanation": "Materialet: '-b = skapa och byt'"},
        {"question": "git merge feature?", "options": ["Merge files", "Mergar feature hit", "Feature merge", "Merge all"], "correct": 1, "explanation": "Materialet: 'merge = kombinera'"},
        {"question": "git fetch?", "options": ["Fetch all", "Hämtar utan merge", "Fetch remote", "Get fetch"], "correct": 1, "explanation": "Materialet: 'fetch = bara hämta'"},
        {"question": "git stash?", "options": ["Stash files", "Sparar undan tillfälligt", "Stash all", "Store stash"], "correct": 1, "explanation": "Materialet: 'stash = spara undan'"},
        {"question": "git branch -d?", "options": ["Delete all", "Tar bort branch", "D branch", "Delete d"], "correct": 1, "explanation": "Materialet: '-d = delete'"},
        {"question": "git diff?", "options": ["Difference", "Visar ändringar", "Diff all", "File diff"], "correct": 1, "explanation": "Materialet: 'diff = skillnader'"},
        {"question": "git switch?", "options": ["Switch files", "Byter branch", "Switch all", "Branch switch"], "correct": 1, "explanation": "Materialet: 'switch = byt branch'"},
    ],
    "hard": [
        {"question": "Pull Request är?", "options": ["Pull files", "Förfrågan att merga", "Request pull", "Pull merge"], "correct": 1, "explanation": "Materialet: 'PR = merge-förfrågan'"},
        {"question": "git reset --hard HEAD~1?", "options": ["Reset soft", "Tar bort senaste commit helt", "Hard reset", "Reset all"], "correct": 1, "explanation": "Materialet: '--hard = ta bort helt'"},
        {"question": "git revert?", "options": ["Revert all", "Skapar ångra-commit", "Revert back", "Delete commit"], "correct": 1, "explanation": "Materialet: 'revert = ångra med ny commit'"},
        {"question": "<<<<<<< HEAD i konflikt?", "options": ["Head marker", "Början på din kod", "HEAD start", "Conflict head"], "correct": 1, "explanation": "Materialet: 'HEAD = din kod'"},
        {"question": "Lösa merge conflict?", "options": ["Automatic", "Redigera → add → commit", "Delete conflict", "Merge fix"], "correct": 1, "explanation": "Materialet: 'Redigera, add, commit'"},
        {"question": "git cherry-pick?", "options": ["Pick all", "Plockar specifik commit", "Cherry commit", "Pick cherry"], "correct": 1, "explanation": "Materialet: 'cherry-pick = plocka commit'"},
    ],
}
# =============================================================================
# HUVUDEXPORT - Alla 25 noder för tentaplugg-linux
# =============================================================================

TENTAPLUGG_LINUX_STUDY = {
    "module_slug": "tentaplugg-linux",
    "module_title": "Tentaplugg Linux",
    "module_description": "Komplett tentaförberedelse för DOE25 Linux - 25 noder",
    "icon": "GraduationCap",
    "nodes": {
        "nod_01_subnetting": {
            "title": "Subnetting & Nätverk",
            "flashcards": NOD_01_FLASHCARDS,
            "quiz": NOD_01_QUIZ,
        },
        "nod_02_filsystem": {
            "title": "Filsystem & Grundkommandon",
            "flashcards": NOD_02_FLASHCARDS,
            "quiz": NOD_02_QUIZ,
        },
        "nod_03_bash_grunder": {
            "title": "Bash-grunder & Shebang",
            "flashcards": NOD_03_FLASHCARDS,
            "quiz": NOD_03_QUIZ,
        },
        "nod_04_variabler": {
            "title": "Variabler, Quoting & Expansions",
            "flashcards": NOD_04_FLASHCARDS,
            "quiz": NOD_04_QUIZ,
        },
        "nod_05_regex": {
            "title": "Reguljära Uttryck (Regex)",
            "flashcards": NOD_05_FLASHCARDS,
            "quiz": NOD_05_QUIZ,
        },
        "nod_06_sed": {
            "title": "Stream Editor (sed)",
            "flashcards": NOD_06_FLASHCARDS,
            "quiz": NOD_06_QUIZ,
        },
        "nod_07_awk": {
            "title": "AWK Textbearbetning",
            "flashcards": NOD_07_FLASHCARDS,
            "quiz": NOD_07_QUIZ,
        },
        "nod_08_villkor": {
            "title": "Villkor & Logik (if/case)",
            "flashcards": NOD_08_FLASHCARDS,
            "quiz": NOD_08_QUIZ,
        },
        "nod_09_interaktiva_skript": {
            "title": "Interaktiva Skript (read/select)",
            "flashcards": NOD_09_FLASHCARDS,
            "quiz": NOD_09_QUIZ,
        },
        "nod_10_loopar": {
            "title": "Loopar (for/while/until)",
            "flashcards": NOD_10_FLASHCARDS,
            "quiz": NOD_10_QUIZ,
        },
        "nod_11_parametrar_arrays": {
            "title": "Parametrar & Arrays",
            "flashcards": NOD_11_FLASHCARDS,
            "quiz": NOD_11_QUIZ,
        },
        "nod_12_funktioner": {
            "title": "Funktioner i Bash",
            "flashcards": NOD_12_FLASHCARDS,
            "quiz": NOD_12_QUIZ,
        },
        "nod_13_signals_traps": {
            "title": "Signals, Traps & Job Control",
            "flashcards": NOD_13_FLASHCARDS,
            "quiz": NOD_13_QUIZ,
        },
        "nod_14_users_groups": {
            "title": "Users & Groups",
            "flashcards": NOD_14_FLASHCARDS,
            "quiz": NOD_14_QUIZ,
        },
        "nod_15_permissions": {
            "title": "Permissions (chmod/SGID)",
            "flashcards": NOD_15_FLASHCARDS,
            "quiz": NOD_15_QUIZ,
        },
        "nod_16_ssh_hardening": {
            "title": "SSH-nycklar & Härdning",
            "flashcards": NOD_16_FLASHCARDS,
            "quiz": NOD_16_QUIZ,
        },
        "nod_17_ufw": {
            "title": "UFW Brandvägg",
            "flashcards": NOD_17_FLASHCARDS,
            "quiz": NOD_17_QUIZ,
        },
        "nod_18_firewalld": {
            "title": "FirewallD & SELinux",
            "flashcards": NOD_18_FLASHCARDS,
            "quiz": NOD_18_QUIZ,
        },
        "nod_19_lagring": {
            "title": "Lagring (fdisk/LUKS/mount)",
            "flashcards": NOD_19_FLASHCARDS,
            "quiz": NOD_19_QUIZ,
        },
        "nod_20_backup_tar": {
            "title": "Backup med tar",
            "flashcards": NOD_20_FLASHCARDS,
            "quiz": NOD_20_QUIZ,
        },
        "nod_21_systemd": {
            "title": "Systemd & Services",
            "flashcards": NOD_21_FLASHCARDS,
            "quiz": NOD_21_QUIZ,
        },
        "nod_22_docker_grunder": {
            "title": "Docker Grunder",
            "flashcards": NOD_22_FLASHCARDS,
            "quiz": NOD_22_QUIZ,
        },
        "nod_23_docker_images": {
            "title": "Docker Images & Dockerfile",
            "flashcards": NOD_23_FLASHCARDS,
            "quiz": NOD_23_QUIZ,
        },
        "nod_24_docker_compose": {
            "title": "Docker Compose",
            "flashcards": NOD_24_FLASHCARDS,
            "quiz": NOD_24_QUIZ,
        },
        "nod_25_git": {
            "title": "Git Grunder",
            "flashcards": NOD_25_FLASHCARDS,
            "quiz": NOD_25_QUIZ,
        },
    },
}

__all__ = ["TENTAPLUGG_LINUX_STUDY"]