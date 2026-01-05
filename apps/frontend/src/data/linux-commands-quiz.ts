/**
 * Linux Commands Quiz - Praktiska terminalkommandon
 * Speglar Linux 24/7 modulen och alla Hands-On tasks
 *
 * Kategorier:
 * 1. Navigation & Filsystem
 * 2. Textbearbetning & Sökning
 * 3. Process Management
 * 4. System Information
 * 5. Logghantering
 * 6. SSH & Nätverk
 * 7. Användarhantering
 * 8. Docker
 * 9. Block Storage & LVM
 * 10. Brandvägg
 */

export interface LinuxCommandQuestion {
    id: string;
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
    difficulty: 'beginner' | 'intermediate' | 'advanced';
    category: string;
}

// ============================================================================
// KATEGORI 1: NAVIGATION & FILSYSTEM (50 frågor)
// ============================================================================

export const NAVIGATION_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Navigation
    { id: "cmd-nav-b1", question: "Vilket kommando visar din nuvarande katalog?", options: ["cd", "pwd", "ls", "dir"], correctIndex: 1, explanation: "pwd (print working directory) visar den fullständiga sökvägen till katalogen du står i.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b2", question: "Hur går du till din hemkatalog?", options: ["cd home", "cd /home", "cd ~", "cd .."], correctIndex: 2, explanation: "~ är en genväg till din hemkatalog, t.ex. /home/username.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b3", question: "Vad gör 'cd ..'?", options: ["Går till root", "Går upp en nivå", "Går till hemkatalogen", "Visar nuvarande katalog"], correctIndex: 1, explanation: ".. refererar till parent-katalogen, alltså en nivå upp i filträdet.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b4", question: "Vilket kommando listar filer i en katalog?", options: ["list", "ls", "dir", "show"], correctIndex: 1, explanation: "ls (list) visar innehållet i en katalog.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b5", question: "Vad visar 'ls -l'?", options: ["Dolda filer", "Detaljerad lista med behörigheter", "Endast kataloger", "Filstorlekar"], correctIndex: 1, explanation: "-l (long) visar detaljerad information: behörigheter, ägare, storlek och datum.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b6", question: "Hur visar du dolda filer med ls?", options: ["ls -h", "ls -a", "ls -d", "ls --hidden"], correctIndex: 1, explanation: "-a (all) visar alla filer inklusive dolda som börjar med punkt.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b7", question: "Vad börjar dolda filer med i Linux?", options: ["_", ".", "-", "~"], correctIndex: 1, explanation: "Dolda filer och kataloger börjar med punkt (.) i Linux.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b8", question: "Hur skapar du en ny katalog?", options: ["md nymap", "mkdir nymap", "create nymap", "new nymap"], correctIndex: 1, explanation: "mkdir (make directory) skapar en ny katalog.", difficulty: "beginner", category: "Filsystem" },
    { id: "cmd-nav-b9", question: "Hur skapar du en tom fil?", options: ["create fil", "new fil", "touch fil", "make fil"], correctIndex: 2, explanation: "touch skapar en tom fil eller uppdaterar tidsstämpeln på befintlig fil.", difficulty: "beginner", category: "Filsystem" },
    { id: "cmd-nav-b10", question: "Vad gör 'rm fil.txt'?", options: ["Byter namn", "Flyttar filen", "Tar bort filen", "Kopierar filen"], correctIndex: 2, explanation: "rm (remove) tar bort filer permanent.", difficulty: "beginner", category: "Filsystem" },
    { id: "cmd-nav-b11", question: "Hur kopierar du en fil?", options: ["copy fil kopia", "cp fil kopia", "mv fil kopia", "duplicate fil"], correctIndex: 1, explanation: "cp (copy) kopierar filer.", difficulty: "beginner", category: "Filsystem" },
    { id: "cmd-nav-b12", question: "Hur flyttar eller byter namn på en fil?", options: ["move fil ny", "mv fil ny", "rename fil ny", "rn fil ny"], correctIndex: 1, explanation: "mv (move) flyttar filer eller byter namn.", difficulty: "beginner", category: "Filsystem" },
    { id: "cmd-nav-b13", question: "Vad är / i Linux filsystemet?", options: ["Hemkatalogen", "Root (toppen)", "Temp-katalog", "Användarkatalog"], correctIndex: 1, explanation: "/ är root, toppen av hela filsystemet.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b14", question: "Var finns systemkonfigurationsfiler?", options: ["/bin", "/etc", "/home", "/var"], correctIndex: 1, explanation: "/etc innehåller systemkonfigurationsfiler.", difficulty: "beginner", category: "Navigation" },
    { id: "cmd-nav-b15", question: "Var finns loggfiler i Linux?", options: ["/log", "/var/log", "/etc/log", "/sys/log"], correctIndex: 1, explanation: "/var/log är standardplatsen för systemloggar.", difficulty: "beginner", category: "Navigation" },

    // INTERMEDIATE - Navigation
    { id: "cmd-nav-i1", question: "Vad gör 'ls -lah'?", options: ["Listar endast kataloger", "Detaljerad lista med dolda filer och human-readable storlekar", "Sorterar efter tid", "Visar endast stora filer"], correctIndex: 1, explanation: "-l (long) + -a (all/hidden) + -h (human-readable) = komplett detaljerad lista.", difficulty: "intermediate", category: "Navigation" },
    { id: "cmd-nav-i2", question: "Vad gör 'cd -'?", options: ["Går till root", "Går till hemkatalogen", "Växlar till förra katalogen", "Visar nuvarande katalog"], correctIndex: 2, explanation: "cd - växlar tillbaka till den katalog du var i tidigare.", difficulty: "intermediate", category: "Navigation" },
    { id: "cmd-nav-i3", question: "Hur skapar du /a/b/c om /a inte finns?", options: ["mkdir /a/b/c", "mkdir -p /a/b/c", "mkdir -r /a/b/c", "mkdir --all /a/b/c"], correctIndex: 1, explanation: "-p (parents) skapar alla saknade parent-kataloger.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i4", question: "Hur kopierar du en hel katalog med innehåll?", options: ["cp katalog ny", "cp -r katalog ny", "copy katalog ny", "mv katalog ny"], correctIndex: 1, explanation: "-r (recursive) kopierar katalogen och allt innehåll.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i5", question: "Vad gör 'rm -rf katalog/'?", options: ["Tar bort filen rf", "Frågar innan borttagning", "Tar bort rekursivt utan bekräftelse", "Flyttar till papperskorgen"], correctIndex: 2, explanation: "-r (recursive) + -f (force) tar bort allt utan att fråga. FARLIGT!", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i6", question: "Hur hittar du alla .log-filer i /var/log?", options: ["search /var/log *.log", "find /var/log -name '*.log'", "grep -r .log /var/log", "locate .log /var/log"], correctIndex: 1, explanation: "find med -name och wildcard hittar filer baserat på namn.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i7", question: "Vad visar 'ls -lt'?", options: ["Endast textfiler", "Sorterat efter tid (nyast först)", "Stora filer först", "Tree-vy"], correctIndex: 1, explanation: "-t sorterar efter modifieringstid, nyast först.", difficulty: "intermediate", category: "Navigation" },
    { id: "cmd-nav-i8", question: "Vad gör 'ls -lS'?", options: ["Visar dolda filer", "Sorterar efter storlek (störst först)", "Visar endast kataloger", "Visar symboliska länkar"], correctIndex: 1, explanation: "-S sorterar efter storlek med största filen först.", difficulty: "intermediate", category: "Navigation" },
    { id: "cmd-nav-i9", question: "Hur skapar du en symbolisk länk?", options: ["ln target link", "ln -s target link", "link target link", "symlink target link"], correctIndex: 1, explanation: "ln -s skapar en symbolisk (mjuk) länk som pekar på målet.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i10", question: "Vad visar 'file myfile'?", options: ["Filstorlek", "Filtyp baserat på innehåll", "Filbehörigheter", "Senaste ändring"], correctIndex: 1, explanation: "file-kommandot identifierar filtypen genom att analysera innehållet.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i11", question: "Hur visar du diskutrymme för en katalog?", options: ["df katalog", "du katalog", "disk katalog", "space katalog"], correctIndex: 1, explanation: "du (disk usage) visar hur mycket utrymme en katalog använder.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i12", question: "Vad gör 'du -sh /home'?", options: ["Visar alla filer", "Visar total storlek i human-readable format", "Sorterar filer", "Visar dolda filer"], correctIndex: 1, explanation: "-s (summary) + -h (human-readable) visar total storlek.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i13", question: "Hur hittar du filer större än 100MB?", options: ["find . -size 100M", "find . -size +100M", "find . -bigger 100M", "ls -size +100M"], correctIndex: 1, explanation: "+100M hittar filer STÖRRE än 100MB. Utan + = exakt.", difficulty: "intermediate", category: "Filsystem" },
    { id: "cmd-nav-i14", question: "Vad gör 'which ls'?", options: ["Visar hjälp för ls", "Visar var ls-kommandot finns", "Kör ls", "Visar alias för ls"], correctIndex: 1, explanation: "which visar den fullständiga sökvägen till ett kommando.", difficulty: "intermediate", category: "Navigation" },
    { id: "cmd-nav-i15", question: "Vad refererar . till i sökvägar?", options: ["Root", "Hemkatalogen", "Nuvarande katalog", "Parent-katalogen"], correctIndex: 2, explanation: ". (punkt) refererar alltid till nuvarande katalog.", difficulty: "intermediate", category: "Navigation" },

    // ADVANCED - Navigation
    { id: "cmd-nav-a1", question: "Vad gör 'find . -type f -name '*.log' -mtime +30 -delete'?", options: ["Hittar loggfiler", "Tar bort loggfiler äldre än 30 dagar", "Arkiverar loggfiler", "Komprimerar loggfiler"], correctIndex: 1, explanation: "-mtime +30 = äldre än 30 dagar, -delete tar bort dem.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a2", question: "Hur kör du rm på alla filer som find hittar?", options: ["find . | rm", "find . -exec rm {} \\;", "find . -delete", "find . | xargs rm"], correctIndex: 1, explanation: "-exec rm {} \\; kör rm på varje fil. {} ersätts med filnamnet.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a3", question: "Vad är skillnaden mellan 'cp -a' och 'cp -r'?", options: ["Ingen skillnad", "-a bevarar alla attribut och länkar", "-r är snabbare", "-a komprimerar"], correctIndex: 1, explanation: "-a (archive) bevarar permissions, timestamps, symboliska länkar etc.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a4", question: "Vad händer med en symlink om originalet tas bort?", options: ["Länken fungerar fortfarande", "Länken blir bruten", "Data flyttas till länken", "Länken tas bort automatiskt"], correctIndex: 1, explanation: "Symboliska länkar pekar på filnamnet - tas filen bort blir länken bruten.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a5", question: "Hur hittar du endast kataloger med find?", options: ["find . -dir", "find . -type d", "find . -d", "find . -folder"], correctIndex: 1, explanation: "-type d hittar endast directories (kataloger).", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a6", question: "Vad är fördelen med 'find -exec + ' vs '-exec \\;'?", options: ["Ingen skillnad", "+ kör kommandot en gång med alla filer", "\\; är snabbare", "+ fungerar på fler system"], correctIndex: 1, explanation: "+ samlar filer och kör kommandot EN gång, \\; kör per fil.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a7", question: "Hur uppdaterar du locate-databasen?", options: ["locate --update", "updatedb", "refresh locate", "locate -u"], correctIndex: 1, explanation: "updatedb uppdaterar databasen som locate använder för snabb sökning.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a8", question: "Vad visar 'stat fil'?", options: ["Filstatus", "Detaljerad metadata (inode, storlek, tider)", "Statistik över användning", "Systemstatus"], correctIndex: 1, explanation: "stat visar detaljerad information om en fil: inode, storlek, timestamps, etc.", difficulty: "advanced", category: "Filsystem" },
    { id: "cmd-nav-a9", question: "Vad är /dev/null?", options: ["Tom enhet", "Svart hål för data", "Null-disk", "Temp-fil"], correctIndex: 1, explanation: "/dev/null tar emot och kastar bort all data - ett 'svart hål'.", difficulty: "advanced", category: "Navigation" },
    { id: "cmd-nav-a10", question: "Hur ser du inode-nummer för filer?", options: ["ls -l", "ls -i", "ls -n", "stat -i"], correctIndex: 1, explanation: "ls -i visar inode-nummer för varje fil.", difficulty: "advanced", category: "Filsystem" },
];

// ============================================================================
// KATEGORI 2: TEXTBEARBETNING & SÖKNING (50 frågor)
// ============================================================================

export const TEXT_PROCESSING_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Textbearbetning
    { id: "cmd-txt-b1", question: "Vilket kommando visar hela innehållet i en fil?", options: ["show fil", "read fil", "cat fil", "print fil"], correctIndex: 2, explanation: "cat (concatenate) visar hela filens innehåll i terminalen.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b2", question: "Hur visar du de första 10 raderna i en fil?", options: ["first fil", "head fil", "top fil", "start fil"], correctIndex: 1, explanation: "head visar de första 10 raderna som standard.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b3", question: "Hur visar du de sista 10 raderna i en fil?", options: ["last fil", "end fil", "tail fil", "bottom fil"], correctIndex: 2, explanation: "tail visar de sista 10 raderna som standard.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b4", question: "Hur söker du efter 'error' i en fil?", options: ["find error fil", "search error fil", "grep error fil", "look error fil"], correctIndex: 2, explanation: "grep söker efter mönster i filer och visar matchande rader.", difficulty: "beginner", category: "Sökning" },
    { id: "cmd-txt-b5", question: "Vad gör 'less fil.txt'?", options: ["Visar mindre av filen", "Sidvis visning med scroll", "Tar bort rader", "Komprimerar filen"], correctIndex: 1, explanation: "less låter dig bläddra genom filen med sidnavigering.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b6", question: "Hur avslutar du less?", options: ["Ctrl+C", "Esc", "q", "x"], correctIndex: 2, explanation: "q (quit) avslutar less.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b7", question: "Vad gör pipen | i 'ls | grep txt'?", options: ["Skriver till fil", "Skickar output som input till nästa", "Kör parallellt", "Jämför"], correctIndex: 1, explanation: "Pipe skickar stdout från ett kommando som stdin till nästa.", difficulty: "beginner", category: "Pipes" },
    { id: "cmd-txt-b8", question: "Hur räknar du rader i en fil?", options: ["count fil", "lines fil", "wc -l fil", "num fil"], correctIndex: 2, explanation: "wc -l (word count, lines) räknar antalet rader.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b9", question: "Vad gör '>' i 'echo text > fil'?", options: ["Appendar", "Skriver över filen", "Läser från filen", "Jämför"], correctIndex: 1, explanation: "> omdirigerar output och skriver över befintligt innehåll.", difficulty: "beginner", category: "Redirect" },
    { id: "cmd-txt-b10", question: "Vad gör '>>' i shell?", options: ["Skriver över", "Lägger till i slutet", "Läser", "Skapar"], correctIndex: 1, explanation: ">> appendar (lägger till) i slutet av filen utan att skriva över.", difficulty: "beginner", category: "Redirect" },
    { id: "cmd-txt-b11", question: "Hur söker du case-insensitive med grep?", options: ["grep -c", "grep -i", "grep -I", "grep -n"], correctIndex: 1, explanation: "-i ignorerar skillnad mellan stora och små bokstäver.", difficulty: "beginner", category: "Sökning" },
    { id: "cmd-txt-b12", question: "Vad gör 'echo Hello'?", options: ["Skapar fil Hello", "Skriver ut Hello", "Söker efter Hello", "Sparar Hello"], correctIndex: 1, explanation: "echo skriver ut text till terminalen (stdout).", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b13", question: "Hur visar du första 20 raderna i en fil?", options: ["head fil", "head -20 fil", "top 20 fil", "first 20 fil"], correctIndex: 1, explanation: "head -n 20 eller head -20 visar första 20 raderna.", difficulty: "beginner", category: "Textbearbetning" },
    { id: "cmd-txt-b14", question: "Hur söker du i man-sidor?", options: ["/sökterm", "?sökterm", "s sökterm", "Ctrl+F"], correctIndex: 0, explanation: "/ startar sökning framåt i man/less.", difficulty: "beginner", category: "Dokumentation" },
    { id: "cmd-txt-b15", question: "Vad gör 'man ls'?", options: ["Kör ls", "Visar manual för ls", "Installerar ls", "Tar bort ls"], correctIndex: 1, explanation: "man visar manualsidan för ett kommando.", difficulty: "beginner", category: "Dokumentation" },

    // INTERMEDIATE - Textbearbetning
    { id: "cmd-txt-i1", question: "Vad gör 'tail -f /var/log/syslog'?", options: ["Visar sista raden", "Följer filen i realtid", "Filtrerar loggen", "Formaterar output"], correctIndex: 1, explanation: "-f (follow) visar nya rader när de läggs till - perfekt för loggar!", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i2", question: "Hur söker du rekursivt i alla filer?", options: ["grep error *", "grep -r error .", "grep -R error *", "grep -r error . eller grep -R"], correctIndex: 3, explanation: "-r eller -R söker rekursivt i alla filer under katalogen.", difficulty: "intermediate", category: "Sökning" },
    { id: "cmd-txt-i3", question: "Vad gör 'grep -v pattern fil'?", options: ["Verbose output", "Visar rader som INTE matchar", "Visar version", "Validerar mönster"], correctIndex: 1, explanation: "-v (invert) visar rader som INTE matchar mönstret.", difficulty: "intermediate", category: "Sökning" },
    { id: "cmd-txt-i4", question: "Hur visar du radnummer med grep?", options: ["grep -l", "grep -n", "grep -c", "grep -r"], correctIndex: 1, explanation: "-n visar radnummer för varje matchning.", difficulty: "intermediate", category: "Sökning" },
    { id: "cmd-txt-i5", question: "Vad gör 'sort fil.txt'?", options: ["Sorterar och sparar", "Visar sorterad output", "Sorterar omvänt", "Sorterar numeriskt"], correctIndex: 1, explanation: "sort visar sorterad output men ändrar INTE originalfilen.", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i6", question: "Hur tar du bort dubbletter från sorterad output?", options: ["sort -d", "sort | unique", "sort | uniq", "sort -u"], correctIndex: 2, explanation: "uniq tar bort intilliggande dubbletter (kräver sorterad input).", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i7", question: "Vad gör 'cut -d: -f1 /etc/passwd'?", options: ["Tar bort rad 1", "Visar första fältet med : som delimiter", "Klipper filen", "Visar användarnamn"], correctIndex: 1, explanation: "cut extraherar fält. -d: sätter delimiter, -f1 tar första fältet.", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i8", question: "Vad gör 'diff fil1 fil2'?", options: ["Slår ihop filer", "Visar skillnader", "Kopierar skillnader", "Skapar diff-fil"], correctIndex: 1, explanation: "diff visar skillnader mellan två filer rad för rad.", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i9", question: "Hur ignorerar du stderr i output?", options: ["cmd 2>/dev/null", "cmd --quiet", "cmd -s", "cmd | null"], correctIndex: 0, explanation: "2>/dev/null skickar stderr (fd 2) till /dev/null.", difficulty: "intermediate", category: "Redirect" },
    { id: "cmd-txt-i10", question: "Vad gör '2>&1'?", options: ["Skickar fil 2 till 1", "Skickar stderr till stdout", "Skriver till fil 2", "Läser från fil 1"], correctIndex: 1, explanation: "2>&1 omdirigerar stderr (2) till samma plats som stdout (1).", difficulty: "intermediate", category: "Redirect" },
    { id: "cmd-txt-i11", question: "Hur visar du unika rader med antal?", options: ["uniq", "uniq -c", "sort -c", "count -u"], correctIndex: 1, explanation: "uniq -c räknar och visar antal av varje unik rad.", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i12", question: "Vad gör 'tee'?", options: ["Läser input", "Skriver till fil OCH stdout", "Skapar T-junction", "Testar kommandon"], correctIndex: 1, explanation: "tee skriver till fil samtidigt som det skickar till stdout.", difficulty: "intermediate", category: "Redirect" },
    { id: "cmd-txt-i13", question: "Hur sparar du output till fil OCH ser det?", options: ["cmd > fil && cat fil", "cmd | tee fil", "cmd >> fil", "cmd &> fil"], correctIndex: 1, explanation: "cmd | tee fil visar output och sparar det samtidigt.", difficulty: "intermediate", category: "Redirect" },
    { id: "cmd-txt-i14", question: "Vad gör 'head -n -5 fil'?", options: ["Första 5 raderna", "Allt utom sista 5", "Sista 5 raderna", "Error"], correctIndex: 1, explanation: "Negativt tal visar allt UTOM de sista n raderna.", difficulty: "intermediate", category: "Textbearbetning" },
    { id: "cmd-txt-i15", question: "Vad gör 'cat fil1 fil2 > kombinerad'?", options: ["Jämför filer", "Slår ihop filer till en", "Kopierar filer", "Tar bort filer"], correctIndex: 1, explanation: "cat kan slå ihop flera filer till en.", difficulty: "intermediate", category: "Textbearbetning" },

    // ADVANCED - Textbearbetning
    { id: "cmd-txt-a1", question: "Vad gör 'awk '{print $1}' fil'?", options: ["Skriver ut rad 1", "Skriver ut kolumn/fält 1", "Skriver ut tecken 1", "Skriver ut ord 1"], correctIndex: 1, explanation: "awk $1 refererar till första fältet (kolumnen) i varje rad.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a2", question: "Vad gör 'sed 's/foo/bar/' fil'?", options: ["Tar bort foo", "Ersätter första foo med bar per rad", "Ersätter alla foo", "Lägger till bar"], correctIndex: 1, explanation: "s/foo/bar/ ersätter första förekomsten per rad. Lägg till /g för alla.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a3", question: "Hur ersätter du ALLA förekomster med sed?", options: ["sed 's/foo/bar/'", "sed 's/foo/bar/g'", "sed 'g/foo/bar/'", "sed -a 's/foo/bar/'"], correctIndex: 1, explanation: "/g (global) ersätter alla förekomster på varje rad.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a4", question: "Hur redigerar du en fil på plats med sed?", options: ["sed 's/a/b/' fil", "sed -i 's/a/b/' fil", "sed --inplace 's/a/b/' fil", "sed -e 's/a/b/' > fil"], correctIndex: 1, explanation: "-i (in-place) modifierar filen direkt istället för att visa output.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a5", question: "Vad gör 'grep -E 'error|warning' fil'?", options: ["Söker exakt 'error|warning'", "Söker efter error ELLER warning", "Extended error search", "Exclude warning"], correctIndex: 1, explanation: "-E aktiverar extended regex där | betyder ELLER.", difficulty: "advanced", category: "Sökning" },
    { id: "cmd-txt-a6", question: "Vad gör 'xargs' i en pipeline?", options: ["Kör parallellt", "Bygger argument från stdin", "Extraherar argument", "Validerar argument"], correctIndex: 1, explanation: "xargs tar stdin och bygger kommandoradsargument för nästa kommando.", difficulty: "advanced", category: "Pipes" },
    { id: "cmd-txt-a7", question: "Hur räknar du ord i en fil?", options: ["wc fil", "wc -w fil", "count fil", "words fil"], correctIndex: 1, explanation: "wc -w räknar ord (words).", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a8", question: "Vad gör 'tr a-z A-Z'?", options: ["Översätter filer", "Konverterar till versaler", "Tar bort små bokstäver", "Translates text"], correctIndex: 1, explanation: "tr översätter tecken - här från gemener till versaler.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a9", question: "Hur söker du bakåt i less?", options: ["/sökord", "?sökord", "b sökord", "r sökord"], correctIndex: 1, explanation: "? söker bakåt i filen, / söker framåt.", difficulty: "advanced", category: "Textbearbetning" },
    { id: "cmd-txt-a10", question: "Vad gör 'less +F fil'?", options: ["Öppnar från slutet", "Följer filen som tail -f", "Öppnar snabbare", "Force-öppnar"], correctIndex: 1, explanation: "+F startar less i follow-mode, precis som tail -f men med fler funktioner.", difficulty: "advanced", category: "Textbearbetning" },
];

// ============================================================================
// KATEGORI 3: PROCESS MANAGEMENT (40 frågor)
// ============================================================================

export const PROCESS_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Process
    { id: "cmd-proc-b1", question: "Vilket kommando listar körande processer?", options: ["proc", "ps", "list", "top"], correctIndex: 1, explanation: "ps (process status) listar processer.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b2", question: "Vad gör 'ps aux'?", options: ["Visar endast dina processer", "Visar ALLA processer med detaljer", "Hjälptext", "Auxiliary mode"], correctIndex: 1, explanation: "aux visar alla processer (a), för alla användare (u), med extra info (x).", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b3", question: "Vilket kommando visar processer i realtid?", options: ["ps", "top", "proc", "live"], correctIndex: 1, explanation: "top visar processer och resursanvändning i realtid.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b4", question: "Hur avslutar du top?", options: ["Ctrl+C", "Esc", "q", "exit"], correctIndex: 2, explanation: "q (quit) avslutar top.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b5", question: "Hur dödar du en process med PID 1234?", options: ["stop 1234", "kill 1234", "end 1234", "terminate 1234"], correctIndex: 1, explanation: "kill skickar signal till en process för att avsluta den.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b6", question: "Vad gör Ctrl+C i terminalen?", options: ["Kopierar", "Avbryter körande kommando", "Rensar", "Avslutar"], correctIndex: 1, explanation: "Ctrl+C skickar SIGINT och avbryter det körande kommandot.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b7", question: "Vad gör Ctrl+Z?", options: ["Ångrar", "Pausar process (bakgrund)", "Avslutar", "Zoomar"], correctIndex: 1, explanation: "Ctrl+Z pausar processen och lägger den i bakgrunden.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b8", question: "Vilket kommando är en förbättrad version av top?", options: ["mtop", "htop", "btop", "ktop"], correctIndex: 1, explanation: "htop är en interaktiv processvisare med bättre UI.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b9", question: "Hur kör du ett kommando i bakgrunden?", options: ["bg kommando", "kommando &", "kommando --bg", "background kommando"], correctIndex: 1, explanation: "& i slutet kör kommandot i bakgrunden.", difficulty: "beginner", category: "Processer" },
    { id: "cmd-proc-b10", question: "Vad visar 'jobs'?", options: ["Schemalagda jobb", "Bakgrundsjobb i aktuell shell", "Alla processer", "Cron-jobb"], correctIndex: 1, explanation: "jobs visar bakgrundsjobb startade i nuvarande terminal.", difficulty: "beginner", category: "Processer" },

    // INTERMEDIATE - Process
    { id: "cmd-proc-i1", question: "Vad är skillnaden mellan kill och kill -9?", options: ["Ingen skillnad", "kill ber snällt, kill -9 tvingar", "kill -9 är säkrare", "kill -9 är långsammare"], correctIndex: 1, explanation: "kill (SIGTERM) ger processen chans att städa upp. kill -9 (SIGKILL) tvingar omedelbart.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i2", question: "Hur dödar du alla processer med namn 'nginx'?", options: ["kill nginx", "killall nginx", "pkill nginx", "pkill eller killall"], correctIndex: 3, explanation: "pkill och killall dödar processer baserat på namn.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i3", question: "Vad gör 'fg'?", options: ["Foreground - tar bakgrundsjobb framåt", "Find grep", "File get", "Force go"], correctIndex: 0, explanation: "fg tar ett bakgrundsjobb till förgrunden.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i4", question: "Vad gör 'bg'?", options: ["Bakgrund - startar om pausat jobb", "Big", "Background new", "Backup"], correctIndex: 0, explanation: "bg startar om ett pausat jobb i bakgrunden.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i5", question: "Hur hittar du PID för en process med namn?", options: ["pid nginx", "pgrep nginx", "findpid nginx", "ps nginx"], correctIndex: 1, explanation: "pgrep hittar process-ID baserat på namn.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i6", question: "Vad gör 'nohup command &'?", options: ["Tystar output", "Kör även efter logout", "Kör med högre prioritet", "Kör som root"], correctIndex: 1, explanation: "nohup (no hang up) gör att kommandot fortsätter även om du loggar ut.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i7", question: "Hur ser du vad en process gör just nu?", options: ["strace -p PID", "watch PID", "trace PID", "follow PID"], correctIndex: 0, explanation: "strace visar systemanrop som en process gör i realtid.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i8", question: "Vad visar 'ps aux | grep nginx'?", options: ["Alla nginx-processer", "Nginx-konfiguration", "Nginx-loggar", "Nginx-portar"], correctIndex: 0, explanation: "ps aux listar alla, grep filtrerar på nginx.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i9", question: "Hur sorterar du top efter minnesanvändning?", options: ["Tryck M", "Tryck m", "Tryck R", "Tryck P"], correctIndex: 0, explanation: "M (shift+m) sorterar efter minne, P efter CPU.", difficulty: "intermediate", category: "Processer" },
    { id: "cmd-proc-i10", question: "Vad betyder 'zombie' process?", options: ["Farlig process", "Avslutad men ej rensad av förälder", "Pausad process", "Hög CPU-användning"], correctIndex: 1, explanation: "Zombie är en avslutad process som väntar på att föräldern ska läsa exit-status.", difficulty: "intermediate", category: "Processer" },

    // ADVANCED - Process
    { id: "cmd-proc-a1", question: "Vad gör 'nice -n 10 command'?", options: ["Snyggar output", "Kör med lägre prioritet", "Kör 10 gånger", "Väntar 10 sekunder"], correctIndex: 1, explanation: "nice sätter prioritet. Högre värde = lägre prioritet.", difficulty: "advanced", category: "Processer" },
    { id: "cmd-proc-a2", question: "Hur ändrar du prioritet på körande process?", options: ["nice PID", "renice -n 10 -p PID", "priority PID 10", "setpri PID 10"], correctIndex: 1, explanation: "renice ändrar prioritet på existerande process.", difficulty: "advanced", category: "Processer" },
    { id: "cmd-proc-a3", question: "Vad är skillnaden mellan SIGTERM och SIGKILL?", options: ["Ingen skillnad", "SIGTERM kan fångas, SIGKILL inte", "SIGKILL är snällare", "SIGTERM är signal 9"], correctIndex: 1, explanation: "SIGTERM (15) kan processen hantera och städa. SIGKILL (9) går inte att fånga.", difficulty: "advanced", category: "Processer" },
    { id: "cmd-proc-a4", question: "Hur kör du kommando med timeout?", options: ["timeout 5 cmd", "cmd --timeout 5", "time 5 cmd", "limit 5 cmd"], correctIndex: 0, explanation: "timeout kör kommando och dödar det efter angiven tid.", difficulty: "advanced", category: "Processer" },
    { id: "cmd-proc-a5", question: "Vad visar /proc/PID/cmdline?", options: ["Process-loggar", "Kommandoraden som startade processen", "CPU-användning", "Minneskarta"], correctIndex: 1, explanation: "/proc/PID/cmdline innehåller kommandot som startade processen.", difficulty: "advanced", category: "Processer" },
];

// ============================================================================
// KATEGORI 4: SYSTEM INFORMATION (40 frågor)
// ============================================================================

export const SYSTEM_INFO_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - System
    { id: "cmd-sys-b1", question: "Hur ser du ledigt diskutrymme?", options: ["disk", "df", "free", "space"], correctIndex: 1, explanation: "df (disk free) visar diskutrymme per filsystem.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b2", question: "Vad gör 'df -h'?", options: ["Visar hjälp", "Human-readable storlekar", "Visar hidden", "Header info"], correctIndex: 1, explanation: "-h visar storlekar i KB, MB, GB istället för bytes.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b3", question: "Hur ser du minnesanvändning?", options: ["mem", "memory", "free", "ram"], correctIndex: 2, explanation: "free visar RAM och swap-användning.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b4", question: "Vad visar 'free -h'?", options: ["Hjälptext", "Human-readable minnesinfo", "Header", "History"], correctIndex: 1, explanation: "-h visar minne i MB/GB istället för bytes.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b5", question: "Hur ser du systemets uptime?", options: ["time", "uptime", "runtime", "started"], correctIndex: 1, explanation: "uptime visar hur länge systemet har kört.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b6", question: "Vad visar 'uname -a'?", options: ["Användarnamn", "All systeminformation", "Architecture", "Admin info"], correctIndex: 1, explanation: "-a visar all systeminformation: kernel, hostname, arkitektur.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b7", question: "Hur ser du hostname?", options: ["host", "hostname", "name", "system"], correctIndex: 1, explanation: "hostname visar eller sätter systemets namn.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b8", question: "Vad visar 'whoami'?", options: ["Alla användare", "Nuvarande användarnamn", "Hemkatalog", "UID"], correctIndex: 1, explanation: "whoami visar vilken användare du är inloggad som.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b9", question: "Hur ser du kernel-version?", options: ["uname -r", "kernel -v", "version", "linux --version"], correctIndex: 0, explanation: "uname -r visar endast kernel release/version.", difficulty: "beginner", category: "System" },
    { id: "cmd-sys-b10", question: "Vad visar 'date'?", options: ["Kalendern", "Aktuellt datum och tid", "Uptime", "Timezone"], correctIndex: 1, explanation: "date visar systemets datum och tid.", difficulty: "beginner", category: "System" },

    // INTERMEDIATE - System
    { id: "cmd-sys-i1", question: "Vad visar 'lsblk'?", options: ["Block storage enheter", "Lista block", "Länkar", "Libraries"], correctIndex: 0, explanation: "lsblk listar alla block devices (diskar, partitioner).", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i2", question: "Hur ser du CPU-information?", options: ["cpu", "lscpu", "cpuinfo", "proc cpu"], correctIndex: 1, explanation: "lscpu visar detaljerad CPU-information.", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i3", question: "Vad visar 'cat /etc/os-release'?", options: ["Kernel-version", "OS-information", "Release notes", "Uppdateringshistorik"], correctIndex: 1, explanation: "os-release innehåller information om operativsystemet.", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i4", question: "Hur ser du vilka diskar som är monterade?", options: ["disks", "mount", "mounts", "mounted"], correctIndex: 1, explanation: "mount utan argument visar alla monterade filsystem.", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i5", question: "Vad gör 'ip a'?", options: ["Visar IP-adress", "Visar alla nätverksinterface med IP", "IP analytics", "IP address lookup"], correctIndex: 1, explanation: "ip a (address) visar alla nätverksinterface och deras IP-adresser.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-sys-i6", question: "Hur ser du öppna portar och lyssnande tjänster?", options: ["ports", "netstat -tulpn", "ss -tulpn", "netstat eller ss med -tulpn"], correctIndex: 3, explanation: "-t tcp, -u udp, -l listening, -p program, -n numeric.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-sys-i7", question: "Vad gör 'du -sh *'?", options: ["Visar storlek för alla", "Storlekssammanfattning per item", "Disk usage summary", "Delete unused"], correctIndex: 1, explanation: "du -sh * visar storlek för varje fil/katalog i nuvarande katalog.", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i8", question: "Hur ser du USB-enheter?", options: ["usb", "lsusb", "usblist", "devices usb"], correctIndex: 1, explanation: "lsusb listar alla USB-enheter.", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i9", question: "Vad visar 'lspci'?", options: ["PCI-enheter", "Process-info", "Port-info", "Package-info"], correctIndex: 0, explanation: "lspci listar alla PCI-enheter (grafikkort, nätverkskort, etc.).", difficulty: "intermediate", category: "System" },
    { id: "cmd-sys-i10", question: "Hur ser du load average?", options: ["load", "uptime", "top", "uptime eller top"], correctIndex: 3, explanation: "Load average visas av både uptime och top.", difficulty: "intermediate", category: "System" },

    // ADVANCED - System
    { id: "cmd-sys-a1", question: "Vad visar 'vmstat 1'?", options: ["VM-statistik", "System performance var sekund", "Virtuellt minne", "Volume stats"], correctIndex: 1, explanation: "vmstat 1 visar CPU, minne, I/O statistik varje sekund.", difficulty: "advanced", category: "System" },
    { id: "cmd-sys-a2", question: "Vad gör 'iostat'?", options: ["I/O-statistik för diskar", "IO status", "Input/output list", "Index stats"], correctIndex: 0, explanation: "iostat visar CPU och disk I/O-statistik.", difficulty: "advanced", category: "System" },
    { id: "cmd-sys-a3", question: "Hur ser du detaljerad minnesinformation?", options: ["free -d", "cat /proc/meminfo", "memstat", "memory --detail"], correctIndex: 1, explanation: "/proc/meminfo innehåller detaljerad minnesinformation.", difficulty: "advanced", category: "System" },
    { id: "cmd-sys-a4", question: "Vad visar 'dmesg'?", options: ["Disk messages", "Kernel ring buffer (systemmeddelanden)", "Debug messages", "Driver messages"], correctIndex: 1, explanation: "dmesg visar kernel-meddelanden, bra för felsökning av hårdvara.", difficulty: "advanced", category: "System" },
    { id: "cmd-sys-a5", question: "Hur ser du systemd service status?", options: ["service status", "systemctl status", "status service", "systemd status"], correctIndex: 1, explanation: "systemctl status visar status för systemd-tjänster.", difficulty: "advanced", category: "System" },
];

// ============================================================================
// KATEGORI 5: LOGGHANTERING (30 frågor)
// ============================================================================

export const LOG_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Loggar
    { id: "cmd-log-b1", question: "Var finns de flesta systemloggar?", options: ["/log", "/var/log", "/etc/log", "/sys/log"], correctIndex: 1, explanation: "/var/log är standardplatsen för systemloggar.", difficulty: "beginner", category: "Loggar" },
    { id: "cmd-log-b2", question: "Hur följer du en loggfil i realtid?", options: ["cat -f log", "tail log", "tail -f log", "watch log"], correctIndex: 2, explanation: "tail -f följer filen och visar nya rader direkt.", difficulty: "beginner", category: "Loggar" },
    { id: "cmd-log-b3", question: "Vilken loggfil innehåller autentiseringsinfo?", options: ["/var/log/messages", "/var/log/auth.log", "/var/log/login", "/var/log/users"], correctIndex: 1, explanation: "auth.log (Debian/Ubuntu) eller secure (RHEL) innehåller login-info.", difficulty: "beginner", category: "Loggar" },
    { id: "cmd-log-b4", question: "Vad gör 'journalctl'?", options: ["Skapar journal", "Visar systemd-loggar", "Redigerar loggar", "Journal config"], correctIndex: 1, explanation: "journalctl visar loggar från systemd journal.", difficulty: "beginner", category: "Loggar" },
    { id: "cmd-log-b5", question: "Hur ser du de senaste 50 raderna i en logg?", options: ["tail log", "tail -50 log", "tail -n 50 log", "last 50 log"], correctIndex: 2, explanation: "tail -n 50 eller tail -50 visar sista 50 raderna.", difficulty: "beginner", category: "Loggar" },

    // INTERMEDIATE - Loggar
    { id: "cmd-log-i1", question: "Vad gör 'journalctl -u nginx'?", options: ["Startar nginx", "Visar loggar för nginx-tjänsten", "Uppdaterar nginx", "Unit-test nginx"], correctIndex: 1, explanation: "-u filtrerar loggar för en specifik systemd-tjänst.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i2", question: "Hur ser du loggar sedan senaste boot?", options: ["journalctl -b", "journalctl --boot", "journalctl -b eller --boot", "journalctl -r"], correctIndex: 2, explanation: "-b visar loggar från nuvarande boot.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i3", question: "Hur följer du journalctl i realtid?", options: ["journalctl -r", "journalctl -f", "journalctl --live", "journalctl -w"], correctIndex: 1, explanation: "-f (follow) visar nya loggrader i realtid.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i4", question: "Hur ser du loggar från specifik tid?", options: ["journalctl --time", "journalctl --since '1 hour ago'", "journalctl -t 1h", "journalctl --from"], correctIndex: 1, explanation: "--since och --until filtrerar på tid.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i5", question: "Vad visar 'last'?", options: ["Senaste kommandot", "Senaste inloggningar", "Sista filen", "Last modified"], correctIndex: 1, explanation: "last visar historik över inloggningar.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i6", question: "Hur söker du efter fel i loggar?", options: ["grep -i error /var/log/syslog", "find error log", "search error log", "log --errors"], correctIndex: 0, explanation: "grep -i error söker case-insensitive efter 'error'.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i7", question: "Vad gör 'dmesg | tail'?", options: ["Visar senaste kernel-meddelanden", "Disk messages", "Debug messages", "Driver messages"], correctIndex: 0, explanation: "dmesg visar kernel-meddelanden, tail begränsar till senaste.", difficulty: "intermediate", category: "Loggar" },
    { id: "cmd-log-i8", question: "Hur ser du endast errors i journalctl?", options: ["journalctl -e", "journalctl -p err", "journalctl --errors", "journalctl -E"], correctIndex: 1, explanation: "-p err filtrerar på prioritet error och högre.", difficulty: "intermediate", category: "Loggar" },

    // ADVANCED - Loggar
    { id: "cmd-log-a1", question: "Vad gör logrotate?", options: ["Roterar skärm", "Roterar och komprimerar loggar automatiskt", "Log analytics", "Rotera användare"], correctIndex: 1, explanation: "logrotate hanterar automatisk rotation och komprimering av loggar.", difficulty: "advanced", category: "Loggar" },
    { id: "cmd-log-a2", question: "Hur ser du disk-användning för /var/log?", options: ["log size", "du -sh /var/log", "df /var/log", "size /var/log"], correctIndex: 1, explanation: "du -sh visar total storlek för katalogen.", difficulty: "advanced", category: "Loggar" },
    { id: "cmd-log-a3", question: "Vad visar 'journalctl --disk-usage'?", options: ["Disk-status", "Hur mycket plats journal tar", "Log rotation status", "Disk errors"], correctIndex: 1, explanation: "--disk-usage visar hur mycket diskutrymme journalen använder.", difficulty: "advanced", category: "Loggar" },
    { id: "cmd-log-a4", question: "Hur rensar du gamla journalctl-loggar?", options: ["journalctl --clean", "journalctl --vacuum-time=7d", "journalctl --delete", "journalctl --purge"], correctIndex: 1, explanation: "--vacuum-time tar bort loggar äldre än angiven tid.", difficulty: "advanced", category: "Loggar" },
    { id: "cmd-log-a5", question: "Vad visar 'who'?", options: ["Vem du är", "Inloggade användare just nu", "User history", "System owner"], correctIndex: 1, explanation: "who visar vilka användare som är inloggade just nu.", difficulty: "advanced", category: "Loggar" },
];

// Export alla frågor hittills
export const LINUX_COMMANDS_QUIZ_PART1 = [
    ...NAVIGATION_QUESTIONS,
    ...TEXT_PROCESSING_QUESTIONS,
    ...PROCESS_QUESTIONS,
    ...SYSTEM_INFO_QUESTIONS,
    ...LOG_QUESTIONS,
];

// ============================================================================
// KATEGORI 6: SSH & NÄTVERK (40 frågor)
// ============================================================================

export const SSH_NETWORK_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - SSH & Nätverk
    { id: "cmd-ssh-b1", question: "Hur ansluter du till en server via SSH?", options: ["ssh server", "ssh user@server", "connect server", "remote server"], correctIndex: 1, explanation: "ssh user@server ansluter till server som angiven användare.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b2", question: "Vilken port använder SSH som standard?", options: ["21", "22", "80", "443"], correctIndex: 1, explanation: "SSH använder port 22 som standard.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b3", question: "Hur genererar du SSH-nycklar?", options: ["ssh-key", "ssh-keygen", "keygen", "ssh-create"], correctIndex: 1, explanation: "ssh-keygen skapar nya SSH-nyckelpar.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b4", question: "Vilken algoritm rekommenderas för SSH-nycklar?", options: ["RSA", "DSA", "ed25519", "MD5"], correctIndex: 2, explanation: "ed25519 är modernast, snabbast och säkrast.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b5", question: "Hur kopierar du din publika nyckel till servern?", options: ["ssh-copy", "ssh-copy-id user@server", "scp key server", "ssh-key-copy"], correctIndex: 1, explanation: "ssh-copy-id kopierar din publika nyckel till serverns authorized_keys.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b6", question: "Var sparas SSH-nycklar som standard?", options: ["/etc/ssh/", "~/.ssh/", "/home/ssh/", "/var/ssh/"], correctIndex: 1, explanation: "SSH-nycklar sparas i användarens ~/.ssh/-katalog.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b7", question: "Vilka rättigheter ska privata nyckeln ha?", options: ["644", "600", "700", "755"], correctIndex: 1, explanation: "600 (rw-------) - endast ägaren får läsa/skriva.", difficulty: "beginner", category: "SSH" },
    { id: "cmd-ssh-b8", question: "Hur testar du nätverksanslutning till en server?", options: ["test server", "ping server", "check server", "connect server"], correctIndex: 1, explanation: "ping testar om servern svarar på nätverket.", difficulty: "beginner", category: "Nätverk" },
    { id: "cmd-ssh-b9", question: "Hur ser du din IP-adress?", options: ["myip", "ip a", "ipconfig", "show ip"], correctIndex: 1, explanation: "ip a (address) visar alla nätverksinterface och IP-adresser.", difficulty: "beginner", category: "Nätverk" },
    { id: "cmd-ssh-b10", question: "Hur kopierar du fil till server via SSH?", options: ["cp fil server:", "scp fil user@server:", "ssh cp fil server", "copy fil server"], correctIndex: 1, explanation: "scp (secure copy) kopierar filer säkert via SSH.", difficulty: "beginner", category: "SSH" },

    // INTERMEDIATE - SSH & Nätverk
    { id: "cmd-ssh-i1", question: "Hur genererar du ed25519-nyckel?", options: ["ssh-keygen -ed25519", "ssh-keygen -t ed25519", "keygen -t ed25519", "ssh-key ed25519"], correctIndex: 1, explanation: "-t anger typen av nyckel som ska skapas.", difficulty: "intermediate", category: "SSH" },
    { id: "cmd-ssh-i2", question: "Vad gör 'ssh -v user@server'?", options: ["Version", "Verbose mode för debugging", "Verify connection", "Virtual terminal"], correctIndex: 1, explanation: "-v aktiverar verbose mode som visar anslutningsdetaljer.", difficulty: "intermediate", category: "SSH" },
    { id: "cmd-ssh-i3", question: "Hur använder du specifik nyckel vid SSH?", options: ["ssh -k key user@server", "ssh -i key user@server", "ssh --key key server", "ssh -f key server"], correctIndex: 1, explanation: "-i anger vilken identitetsfil (nyckel) som ska användas.", difficulty: "intermediate", category: "SSH" },
    { id: "cmd-ssh-i4", question: "Hur ansluter du till SSH på annan port?", options: ["ssh user@server port", "ssh -p 2222 user@server", "ssh user@server:2222", "ssh --port 2222 server"], correctIndex: 1, explanation: "-p anger porten att ansluta till.", difficulty: "intermediate", category: "SSH" },
    { id: "cmd-ssh-i5", question: "Vad gör 'ss -tulpn'?", options: ["System status", "Visar lyssnande portar och tjänster", "Socket statistics", "Service status"], correctIndex: 1, explanation: "-t tcp, -u udp, -l listening, -p program, -n numeric.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-ssh-i6", question: "Hur ser du routing-tabell?", options: ["route", "ip route", "netstat -r", "Alla fungerar"], correctIndex: 3, explanation: "Alla tre visar routing-information.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-ssh-i7", question: "Vad gör 'traceroute server'?", options: ["Spårar servern", "Visar nätvägen till servern", "Trace logs", "Track server"], correctIndex: 1, explanation: "traceroute visar alla hopp på vägen till destinationen.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-ssh-i8", question: "Hur gör du DNS-uppslag?", options: ["dns server", "dig server", "nslookup server", "dig eller nslookup"], correctIndex: 3, explanation: "Både dig och nslookup gör DNS-uppslag.", difficulty: "intermediate", category: "Nätverk" },
    { id: "cmd-ssh-i9", question: "Vad gör 'ssh-add'?", options: ["Lägger till SSH-server", "Lägger till nyckel i ssh-agent", "Lägger till användare", "Lägger till config"], correctIndex: 1, explanation: "ssh-add lägger till nyckel i körande ssh-agent.", difficulty: "intermediate", category: "SSH" },
    { id: "cmd-ssh-i10", question: "Hur synkar du kataloger med rsync?", options: ["rsync src dest", "rsync -avz src user@server:dest", "sync src dest", "copy -r src dest"], correctIndex: 1, explanation: "rsync -avz synkar effektivt. -a archive, -v verbose, -z compress.", difficulty: "intermediate", category: "SSH" },

    // ADVANCED - SSH & Nätverk
    { id: "cmd-ssh-a1", question: "Hur skapar du SSH-tunnel för port forwarding?", options: ["ssh -L 8080:localhost:80 server", "ssh -tunnel 8080:80 server", "ssh -forward 8080:80 server", "ssh -T 8080:80 server"], correctIndex: 0, explanation: "-L skapar local port forwarding: lokal-port:remote-host:remote-port.", difficulty: "advanced", category: "SSH" },
    { id: "cmd-ssh-a2", question: "Vad gör ProxyJump i SSH?", options: ["Proxy-konfiguration", "Hoppa via mellanserver (jump host)", "Port forwarding", "SOCKS proxy"], correctIndex: 1, explanation: "ProxyJump (-J) låter dig ansluta via en jump/bastion host.", difficulty: "advanced", category: "SSH" },
    { id: "cmd-ssh-a3", question: "Hur ansluter du via jump host?", options: ["ssh -j jump server", "ssh -J jump@jumphost target", "ssh jump && ssh target", "ssh --via jump target"], correctIndex: 1, explanation: "-J anger jump host att ansluta genom.", difficulty: "advanced", category: "SSH" },
    { id: "cmd-ssh-a4", question: "Vad gör ControlMaster i SSH?", options: ["Master-nyckel", "Multiplexar anslutningar (delar connection)", "Kontrollerar servrar", "Master-server"], correctIndex: 1, explanation: "ControlMaster delar en SSH-anslutning för flera sessioner.", difficulty: "advanced", category: "SSH" },
    { id: "cmd-ssh-a5", question: "Hur avbryter du en hängd SSH-session?", options: ["Ctrl+C", "Enter sedan ~.", "Ctrl+D", "kill -9"], correctIndex: 1, explanation: "Enter följt av ~. är escape sequence för att avbryta.", difficulty: "advanced", category: "SSH" },
    { id: "cmd-ssh-a6", question: "Vad visar 'netstat -an | grep LISTEN'?", options: ["Aktiva anslutningar", "Alla lyssnande portar", "Network statistics", "Listen-config"], correctIndex: 1, explanation: "Visar alla portar som lyssnar efter anslutningar.", difficulty: "advanced", category: "Nätverk" },
    { id: "cmd-ssh-a7", question: "Hur testar du om en port är öppen?", options: ["ping server:port", "nc -zv server port", "telnet server port", "nc eller telnet"], correctIndex: 3, explanation: "Både nc (netcat) och telnet kan testa portar.", difficulty: "advanced", category: "Nätverk" },
    { id: "cmd-ssh-a8", question: "Vad gör 'ssh-keygen -R server'?", options: ["Remove host from known_hosts", "Regenerate key", "Reset connection", "Revoke key"], correctIndex: 0, explanation: "-R tar bort en host från known_hosts-filen.", difficulty: "advanced", category: "SSH" },
];

// ============================================================================
// KATEGORI 7: ANVÄNDARHANTERING & PERMISSIONS (40 frågor)
// ============================================================================

export const USER_PERMISSIONS_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Användare & Permissions
    { id: "cmd-usr-b1", question: "Hur skapar du en ny användare?", options: ["newuser namn", "useradd namn", "adduser namn", "useradd eller adduser"], correctIndex: 3, explanation: "useradd är lågnivå, adduser är interaktiv (Debian). Båda fungerar.", difficulty: "beginner", category: "Användare" },
    { id: "cmd-usr-b2", question: "Hur sätter du lösenord för användare?", options: ["password user", "passwd user", "setpass user", "userpass user"], correctIndex: 1, explanation: "passwd sätter eller ändrar lösenord.", difficulty: "beginner", category: "Användare" },
    { id: "cmd-usr-b3", question: "Hur byter du till annan användare?", options: ["switch user", "su user", "change user", "login user"], correctIndex: 1, explanation: "su (switch user) byter till annan användare.", difficulty: "beginner", category: "Användare" },
    { id: "cmd-usr-b4", question: "Vad gör 'sudo'?", options: ["Super user do - kör som root", "Switch user do", "System user do", "Secure do"], correctIndex: 0, explanation: "sudo kör kommandot med administratörsrättigheter.", difficulty: "beginner", category: "Användare" },
    { id: "cmd-usr-b5", question: "Hur ser du vilka grupper du tillhör?", options: ["mygroups", "groups", "whoami -g", "id groups"], correctIndex: 1, explanation: "groups visar alla grupper användaren tillhör.", difficulty: "beginner", category: "Användare" },
    { id: "cmd-usr-b6", question: "Vad gör 'chmod 755 fil'?", options: ["Ändrar ägare", "Sätter permissions rwxr-xr-x", "Ändrar grupp", "Komprimerar fil"], correctIndex: 1, explanation: "755 = rwx (ägare) + r-x (grupp) + r-x (andra).", difficulty: "beginner", category: "Permissions" },
    { id: "cmd-usr-b7", question: "Vad betyder 'r' i filrättigheter?", options: ["Run", "Read (läsa)", "Remove", "Root"], correctIndex: 1, explanation: "r = read, rätt att läsa filen.", difficulty: "beginner", category: "Permissions" },
    { id: "cmd-usr-b8", question: "Vad betyder 'w' i filrättigheter?", options: ["Wait", "Write (skriva)", "Watch", "World"], correctIndex: 1, explanation: "w = write, rätt att ändra filen.", difficulty: "beginner", category: "Permissions" },
    { id: "cmd-usr-b9", question: "Vad betyder 'x' i filrättigheter?", options: ["Exit", "Execute (köra)", "Extract", "Extend"], correctIndex: 1, explanation: "x = execute, rätt att köra filen/gå in i katalog.", difficulty: "beginner", category: "Permissions" },
    { id: "cmd-usr-b10", question: "Hur ändrar du ägare på en fil?", options: ["owner fil user", "chown user fil", "setowner user fil", "chmod owner user"], correctIndex: 1, explanation: "chown (change owner) ändrar ägare.", difficulty: "beginner", category: "Permissions" },

    // INTERMEDIATE - Användare & Permissions
    { id: "cmd-usr-i1", question: "Vad gör 'chmod +x script.sh'?", options: ["Tar bort execute", "Lägger till execute för alla", "Execute only for owner", "Exclude execute"], correctIndex: 1, explanation: "+x lägger till execute-permission för alla (user, group, other).", difficulty: "intermediate", category: "Permissions" },
    { id: "cmd-usr-i2", question: "Hur lägger du till användare i en grupp?", options: ["groupadd user group", "usermod -aG group user", "addgroup user group", "useradd -g group user"], correctIndex: 1, explanation: "usermod -aG lägger till användare i grupp utan att ta bort andra.", difficulty: "intermediate", category: "Användare" },
    { id: "cmd-usr-i3", question: "Vad gör 'chown user:group fil'?", options: ["Ändrar endast ägare", "Ändrar ägare OCH grupp", "Ändrar endast grupp", "Error"], correctIndex: 1, explanation: "user:group ändrar både ägare och grupp samtidigt.", difficulty: "intermediate", category: "Permissions" },
    { id: "cmd-usr-i4", question: "Hur ändrar du grupp på en fil?", options: ["groupmod fil group", "chgrp group fil", "setgroup group fil", "chmod group fil"], correctIndex: 1, explanation: "chgrp (change group) ändrar gruppen.", difficulty: "intermediate", category: "Permissions" },
    { id: "cmd-usr-i5", question: "Vad gör 'chmod -R 755 katalog/'?", options: ["Ändrar endast katalogen", "Ändrar rekursivt alla filer", "Remove permissions", "Reset permissions"], correctIndex: 1, explanation: "-R gör ändringen rekursivt för alla filer och underkataloger.", difficulty: "intermediate", category: "Permissions" },
    { id: "cmd-usr-i6", question: "Vad visar 'id user'?", options: ["User info", "UID, GID och grupper för användare", "Identity", "ID-nummer"], correctIndex: 1, explanation: "id visar användarens UID, primära GID och alla grupper.", difficulty: "intermediate", category: "Användare" },
    { id: "cmd-usr-i7", question: "Var finns användarlistan?", options: ["/etc/users", "/etc/passwd", "/var/users", "/home/users"], correctIndex: 1, explanation: "/etc/passwd innehåller alla användarekonton.", difficulty: "intermediate", category: "Användare" },
    { id: "cmd-usr-i8", question: "Var finns grupplistan?", options: ["/etc/groups", "/etc/group", "/var/groups", "/home/groups"], correctIndex: 1, explanation: "/etc/group innehåller alla grupper.", difficulty: "intermediate", category: "Användare" },
    { id: "cmd-usr-i9", question: "Vad gör 'chmod 600 fil'?", options: ["Alla kan läsa", "Endast ägaren kan läsa/skriva", "Readonly för alla", "Full access"], correctIndex: 1, explanation: "600 = rw------- endast ägaren har läs/skriv-rättigheter.", difficulty: "intermediate", category: "Permissions" },
    { id: "cmd-usr-i10", question: "Hur tar du bort en användare?", options: ["deluser user", "userdel user", "removeuser user", "userdel eller deluser"], correctIndex: 3, explanation: "userdel är standard, deluser finns på Debian.", difficulty: "intermediate", category: "Användare" },

    // ADVANCED - Användare & Permissions
    { id: "cmd-usr-a1", question: "Vad är SUID-bit?", options: ["Super UID", "Kör som filägare istället för köraren", "Secure UID", "System UID"], correctIndex: 1, explanation: "SUID (Set UID) kör programmet med filägarens rättigheter.", difficulty: "advanced", category: "Permissions" },
    { id: "cmd-usr-a2", question: "Hur sätter du SUID-bit?", options: ["chmod s+u fil", "chmod u+s fil", "chmod +suid fil", "chmod 4755 fil"], correctIndex: 3, explanation: "chmod u+s eller chmod 4755 sätter SUID.", difficulty: "advanced", category: "Permissions" },
    { id: "cmd-usr-a3", question: "Vad är sticky bit på katalog?", options: ["Klibbig", "Endast ägare kan ta bort sina filer", "Sticky sessions", "Stay in memory"], correctIndex: 1, explanation: "Sticky bit på katalog gör att endast filägare kan ta bort sina filer.", difficulty: "advanced", category: "Permissions" },
    { id: "cmd-usr-a4", question: "Hur sätter du sticky bit?", options: ["chmod +t katalog", "chmod 1777 katalog", "Båda fungerar", "chmod sticky katalog"], correctIndex: 2, explanation: "+t eller 1777 sätter sticky bit.", difficulty: "advanced", category: "Permissions" },
    { id: "cmd-usr-a5", question: "Var konfigureras sudo-rättigheter?", options: ["/etc/sudo", "/etc/sudoers", "/etc/admin", "/etc/root"], correctIndex: 1, explanation: "/etc/sudoers eller filer i /etc/sudoers.d/ konfigurerar sudo.", difficulty: "advanced", category: "Användare" },
    { id: "cmd-usr-a6", question: "Hur redigerar du sudoers säkert?", options: ["vim /etc/sudoers", "visudo", "nano /etc/sudoers", "sudoedit /etc/sudoers"], correctIndex: 1, explanation: "visudo validerar syntax innan sparning för att undvika fel.", difficulty: "advanced", category: "Användare" },
    { id: "cmd-usr-a7", question: "Vad gör 'getfacl fil'?", options: ["Get file access control list", "Get facts", "Get file", "Get ACL permissions"], correctIndex: 0, explanation: "getfacl visar extended ACL-rättigheter på filen.", difficulty: "advanced", category: "Permissions" },
    { id: "cmd-usr-a8", question: "Hur sätter du ACL för specifik användare?", options: ["acl set user", "setfacl -m u:user:rwx fil", "chmod acl user", "facl -u user fil"], correctIndex: 1, explanation: "setfacl -m modifierar ACL. u:user:permissions.", difficulty: "advanced", category: "Permissions" },
];

// ============================================================================
// KATEGORI 8: DOCKER KOMMANDON (50 frågor)
// ============================================================================

export const DOCKER_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Docker
    { id: "cmd-doc-b1", question: "Hur startar du en container från en image?", options: ["docker start image", "docker run image", "docker create image", "docker begin image"], correctIndex: 1, explanation: "docker run skapar och startar en container från angiven image.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b2", question: "Hur listar du körande containers?", options: ["docker list", "docker ps", "docker containers", "docker show"], correctIndex: 1, explanation: "docker ps visar körande containers.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b3", question: "Hur listar du ALLA containers (även stoppade)?", options: ["docker ps", "docker ps -a", "docker all", "docker list all"], correctIndex: 1, explanation: "-a visar alla, inklusive stoppade containers.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b4", question: "Hur stoppar du en container?", options: ["docker stop ID", "docker end ID", "docker kill ID", "docker halt ID"], correctIndex: 0, explanation: "docker stop stoppar containern gracefully.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b5", question: "Hur tar du bort en container?", options: ["docker delete ID", "docker rm ID", "docker remove ID", "docker del ID"], correctIndex: 1, explanation: "docker rm tar bort en stoppad container.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b6", question: "Hur listar du Docker images?", options: ["docker images", "docker image ls", "docker list images", "docker images eller image ls"], correctIndex: 3, explanation: "Både docker images och docker image ls fungerar.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b7", question: "Hur laddar du ner en image?", options: ["docker download", "docker pull", "docker get", "docker fetch"], correctIndex: 1, explanation: "docker pull hämtar image från registry.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b8", question: "Hur kör du container i bakgrunden?", options: ["docker run -b", "docker run -d", "docker run --bg", "docker run &"], correctIndex: 1, explanation: "-d (detached) kör containern i bakgrunden.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b9", question: "Hur ser du loggar från en container?", options: ["docker log ID", "docker logs ID", "docker output ID", "docker console ID"], correctIndex: 1, explanation: "docker logs visar output från containern.", difficulty: "beginner", category: "Docker" },
    { id: "cmd-doc-b10", question: "Hur tar du bort en image?", options: ["docker delete image", "docker rmi image", "docker remove image", "docker rm image"], correctIndex: 1, explanation: "docker rmi (remove image) tar bort images.", difficulty: "beginner", category: "Docker" },

    // INTERMEDIATE - Docker
    { id: "cmd-doc-i1", question: "Hur kör du kommando i körande container?", options: ["docker run -it ID cmd", "docker exec -it ID cmd", "docker command ID cmd", "docker shell ID cmd"], correctIndex: 1, explanation: "docker exec kör kommando i körande container. -it för interaktiv terminal.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i2", question: "Vad gör 'docker run -it ubuntu bash'?", options: ["Startar Ubuntu-server", "Interaktiv terminal i Ubuntu-container", "Installerar Ubuntu", "Bygger Ubuntu-image"], correctIndex: 1, explanation: "-i (interactive) + -t (tty) ger interaktiv terminal.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i3", question: "Hur publicerar du port 80 i containern till port 8080 på host?", options: ["docker run -p 80:8080", "docker run -p 8080:80", "docker run --port 80:8080", "docker run -P 8080"], correctIndex: 1, explanation: "-p host:container, så 8080:80 mappar host 8080 till container 80.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i4", question: "Hur monterar du volym i container?", options: ["-v /host:/container", "-m /host:/container", "--volume /host", "-d /host:/container"], correctIndex: 0, explanation: "-v host-path:container-path monterar katalog.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i5", question: "Hur bygger du image från Dockerfile?", options: ["docker create .", "docker build .", "docker make .", "docker compile ."], correctIndex: 1, explanation: "docker build . bygger image från Dockerfile i nuvarande katalog.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i6", question: "Hur taggar du en image?", options: ["docker tag source:tag target:tag", "docker rename", "docker label", "docker mark"], correctIndex: 0, explanation: "docker tag skapar ny tag för existerande image.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i7", question: "Vad gör 'docker-compose up'?", options: ["Startar containers definierade i compose-fil", "Uppgraderar Docker", "Laddar upp image", "Skapar compose-fil"], correctIndex: 0, explanation: "docker-compose up startar alla tjänster definierade i docker-compose.yml.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i8", question: "Hur startar du compose i bakgrunden?", options: ["docker-compose up -b", "docker-compose up -d", "docker-compose up &", "docker-compose start"], correctIndex: 1, explanation: "-d (detached) kör i bakgrunden.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i9", question: "Hur stoppar du compose-tjänster?", options: ["docker-compose stop", "docker-compose down", "docker-compose end", "stop eller down"], correctIndex: 3, explanation: "stop pausar, down stoppar och tar bort containers.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i10", question: "Hur ser du resursanvändning för containers?", options: ["docker usage", "docker stats", "docker resources", "docker top"], correctIndex: 1, explanation: "docker stats visar CPU, minne etc i realtid.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i11", question: "Vad gör '--rm' flaggan?", options: ["Remove mode", "Ta bort container efter stopp", "Remove image", "Reset memory"], correctIndex: 1, explanation: "--rm tar automatiskt bort containern när den stoppas.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i12", question: "Hur skapar du named volume?", options: ["docker volume new", "docker volume create namn", "docker create volume", "docker vol make"], correctIndex: 1, explanation: "docker volume create skapar namngiven volym.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i13", question: "Hur listar du Docker-nätverk?", options: ["docker networks", "docker network ls", "docker net list", "docker show networks"], correctIndex: 1, explanation: "docker network ls visar alla nätverk.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i14", question: "Hur skapar du ett custom nätverk?", options: ["docker network add", "docker network create namn", "docker create network", "docker net new"], correctIndex: 1, explanation: "docker network create skapar nytt nätverk.", difficulty: "intermediate", category: "Docker" },
    { id: "cmd-doc-i15", question: "Vad gör 'docker inspect'?", options: ["Inspekterar Dockerfile", "Visar detaljerad info om container/image", "Inspekterar nätverk", "Debug mode"], correctIndex: 1, explanation: "docker inspect visar detaljerad JSON-metadata.", difficulty: "intermediate", category: "Docker" },

    // ADVANCED - Docker
    { id: "cmd-doc-a1", question: "Hur rensar du ALLA oanvända resurser?", options: ["docker clean", "docker prune", "docker system prune", "docker remove unused"], correctIndex: 2, explanation: "docker system prune rensar oanvända containers, images, nätverk.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a2", question: "Hur kopierar du fil från container till host?", options: ["docker cp container:/path /host", "docker copy", "docker get", "docker export"], correctIndex: 0, explanation: "docker cp kopierar filer mellan container och host.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a3", question: "Vad gör 'docker commit'?", options: ["Commit till git", "Skapar image från container", "Sparar ändringar", "Commit config"], correctIndex: 1, explanation: "docker commit skapar ny image från container-state.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a4", question: "Hur begränsar du container-minne?", options: ["-m 512m", "--memory 512m", "--mem-limit 512m", "-m eller --memory"], correctIndex: 3, explanation: "-m eller --memory begränsar minnesanvändning.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a5", question: "Hur begränsar du CPU?", options: ["--cpus 0.5", "--cpu-limit 0.5", "--cpu 0.5", "--processor 0.5"], correctIndex: 0, explanation: "--cpus begränsar till antal CPU-cores.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a6", question: "Vad gör 'docker save'?", options: ["Sparar container", "Exporterar image till tar", "Sparar logs", "Backup config"], correctIndex: 1, explanation: "docker save exporterar image till tar-fil för transport.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a7", question: "Hur laddar du sparad image?", options: ["docker import", "docker load", "docker restore", "docker open"], correctIndex: 1, explanation: "docker load laddar image sparad med docker save.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a8", question: "Vad är skillnaden mellan docker save och export?", options: ["Samma", "save=image med layers, export=container filesystem", "export är snabbare", "save inkluderar volumes"], correctIndex: 1, explanation: "save exporterar image med alla layers, export exporterar container-filesystem.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a9", question: "Hur visar du image layers?", options: ["docker layers", "docker history image", "docker show layers", "docker image layers"], correctIndex: 1, explanation: "docker history visar alla layers och kommandon i imagen.", difficulty: "advanced", category: "Docker" },
    { id: "cmd-doc-a10", question: "Hur bygger du med specifik Dockerfile?", options: ["docker build Dockerfile", "docker build -f Dockerfile.prod .", "docker build --file prod", "docker build -d Dockerfile"], correctIndex: 1, explanation: "-f anger vilken Dockerfile som ska användas.", difficulty: "advanced", category: "Docker" },
];

// ============================================================================
// KATEGORI 9: BLOCK STORAGE & LVM (40 frågor)
// ============================================================================

export const STORAGE_LVM_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - Storage
    { id: "cmd-sto-b1", question: "Hur listar du block devices (diskar)?", options: ["ls /dev", "lsblk", "fdisk -l", "lsblk eller fdisk -l"], correctIndex: 3, explanation: "Både lsblk och fdisk -l visar diskar och partitioner.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b2", question: "Vad är /dev/sda?", options: ["Systemfil", "Första SATA/SCSI-disk", "Partition", "Mount point"], correctIndex: 1, explanation: "/dev/sda är första SATA/SCSI-disken.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b3", question: "Vad är /dev/sda1?", options: ["Disk 1", "Första partition på sda", "SATA-port 1", "Första disk"], correctIndex: 1, explanation: "/dev/sda1 är första partitionen på disk sda.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b4", question: "Vilket verktyg partitionerar diskar?", options: ["partition", "fdisk", "diskpart", "mkdisk"], correctIndex: 1, explanation: "fdisk är standard för disk-partitionering.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b5", question: "Hur skapar du ext4-filsystem?", options: ["mkfs ext4", "mkfs.ext4 /dev/X", "format ext4", "create ext4"], correctIndex: 1, explanation: "mkfs.ext4 eller mkfs -t ext4 skapar ext4-filsystem.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b6", question: "Hur monterar du en partition?", options: ["connect /dev/X /mnt", "mount /dev/X /mnt", "attach /dev/X /mnt", "link /dev/X /mnt"], correctIndex: 1, explanation: "mount kopplar filsystem till en katalog (mount point).", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b7", question: "Hur avmonterar du?", options: ["unmount /mnt", "umount /mnt", "disconnect /mnt", "detach /mnt"], correctIndex: 1, explanation: "umount (utan n!) avmonterar filsystemet.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b8", question: "Var konfigureras automatisk mount vid boot?", options: ["/etc/mount", "/etc/fstab", "/etc/disks", "/etc/mounts"], correctIndex: 1, explanation: "/etc/fstab konfigurerar automatisk mount vid boot.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b9", question: "Hur hittar du UUID för partition?", options: ["uuid /dev/X", "blkid", "lsblk -f", "blkid eller lsblk -f"], correctIndex: 3, explanation: "Både blkid och lsblk -f visar UUID.", difficulty: "beginner", category: "Storage" },
    { id: "cmd-sto-b10", question: "Vad är LVM?", options: ["Linux Volume Manager", "Logical Volume Manager", "Local Volume Manager", "Logical Volume Manager"], correctIndex: 3, explanation: "LVM = Logical Volume Manager för flexibel volymhantering.", difficulty: "beginner", category: "LVM" },

    // INTERMEDIATE - Storage & LVM
    { id: "cmd-sto-i1", question: "LVM-hierarki: Vilken ordning?", options: ["LV > VG > PV", "PV > VG > LV", "VG > PV > LV", "PV > LV > VG"], correctIndex: 1, explanation: "PV (fysisk disk) → VG (volymgrupp) → LV (logisk volym).", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i2", question: "Hur skapar du Physical Volume?", options: ["pvcreate /dev/X", "lvm pv create", "pvmake", "create-pv"], correctIndex: 0, explanation: "pvcreate initierar en disk/partition för LVM.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i3", question: "Hur skapar du Volume Group?", options: ["vgcreate vgname /dev/X", "lvm vg create", "vgmake", "create-vg"], correctIndex: 0, explanation: "vgcreate skapar volume group med angivna PVs.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i4", question: "Hur skapar du Logical Volume?", options: ["lvcreate -L 10G vgname", "lvcreate -n namn -L 10G vgname", "lvmake", "create-lv"], correctIndex: 1, explanation: "lvcreate -n namn -L storlek vgname skapar LV.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i5", question: "Hur utökar du en LV?", options: ["lvgrow", "lvextend -L +5G /dev/vg/lv", "lv-expand", "lvresize +5G"], correctIndex: 1, explanation: "lvextend utökar logical volume.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i6", question: "Efter lvextend, vad måste du göra?", options: ["Inget", "Utöka filsystemet", "Reboot", "Remount"], correctIndex: 1, explanation: "resize2fs (ext4) eller xfs_growfs (xfs) krävs efteråt.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i7", question: "Hur visar du PVs?", options: ["pvdisplay", "pvs", "pv-list", "pvdisplay eller pvs"], correctIndex: 3, explanation: "pvs är kort, pvdisplay är detaljerad.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i8", question: "Hur visar du VGs?", options: ["vgdisplay", "vgs", "vg-list", "vgdisplay eller vgs"], correctIndex: 3, explanation: "vgs är kort, vgdisplay är detaljerad.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i9", question: "Hur visar du LVs?", options: ["lvdisplay", "lvs", "lv-list", "lvdisplay eller lvs"], correctIndex: 3, explanation: "lvs är kort, lvdisplay är detaljerad.", difficulty: "intermediate", category: "LVM" },
    { id: "cmd-sto-i10", question: "Hur lägger du till disk i existerande VG?", options: ["vgadd", "vgextend vgname /dev/X", "vg add disk", "pvextend"], correctIndex: 1, explanation: "vgextend lägger till ny PV i existerande VG.", difficulty: "intermediate", category: "LVM" },

    // ADVANCED - Storage & LVM
    { id: "cmd-sto-a1", question: "Hur krypterar du partition med LUKS?", options: ["luks-encrypt", "cryptsetup luksFormat /dev/X", "encrypt-disk", "mkluks"], correctIndex: 1, explanation: "cryptsetup luksFormat initierar LUKS-kryptering.", difficulty: "advanced", category: "Kryptering" },
    { id: "cmd-sto-a2", question: "Hur öppnar du LUKS-krypterad enhet?", options: ["luks-open", "cryptsetup open /dev/X namn", "decrypt", "mount"], correctIndex: 1, explanation: "cryptsetup open dekrypterar och öppnar enheten.", difficulty: "advanced", category: "Kryptering" },
    { id: "cmd-sto-a3", question: "Var hamnar öppnad LUKS-enhet?", options: ["/dev/luks/", "/dev/mapper/namn", "/mnt/luks/", "/etc/luks/"], correctIndex: 1, explanation: "Öppnade LUKS-enheter finns under /dev/mapper/.", difficulty: "advanced", category: "Kryptering" },
    { id: "cmd-sto-a4", question: "Hur skapar du LVM snapshot?", options: ["lvcreate --snapshot", "lvcreate -s -L 1G -n snap /dev/vg/lv", "lvsnapshot", "snapshot create"], correctIndex: 1, explanation: "lvcreate -s skapar snapshot av angiven LV.", difficulty: "advanced", category: "LVM" },
    { id: "cmd-sto-a5", question: "Hur kontrollerar du ext4-filsystem?", options: ["checkfs", "fsck.ext4 /dev/X", "verify", "scan"], correctIndex: 1, explanation: "fsck.ext4 kontrollerar och reparerar ext4-filsystem.", difficulty: "advanced", category: "Storage" },
    { id: "cmd-sto-a6", question: "Måste disk vara omonterad för fsck?", options: ["Nej", "Ja, vanligtvis", "Beror på fs", "Aldrig"], correctIndex: 1, explanation: "fsck ska köras på omonterad disk för säkerhet.", difficulty: "advanced", category: "Storage" },
    { id: "cmd-sto-a7", question: "Hur läser du SMART-data från disk?", options: ["smart-info", "smartctl -a /dev/X", "diskhealth", "smart --read"], correctIndex: 1, explanation: "smartctl (från smartmontools) läser SMART-data.", difficulty: "advanced", category: "Storage" },
    { id: "cmd-sto-a8", question: "Hur kör du fstrim för SSD?", options: ["ssd-trim", "fstrim /", "trim-disk", "discard"], correctIndex: 1, explanation: "fstrim skickar TRIM-kommandon till SSD.", difficulty: "advanced", category: "Storage" },
];

// ============================================================================
// KATEGORI 10: BRANDVÄGG & SÄKERHET (30 frågor)
// ============================================================================

export const FIREWALL_QUESTIONS: LinuxCommandQuestion[] = [
    // BEGINNER - UFW
    { id: "cmd-fw-b1", question: "Hur aktiverar du UFW-brandvägg?", options: ["ufw start", "ufw enable", "ufw on", "systemctl start ufw"], correctIndex: 1, explanation: "ufw enable aktiverar brandväggen.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b2", question: "Hur inaktiverar du UFW?", options: ["ufw stop", "ufw disable", "ufw off", "ufw down"], correctIndex: 1, explanation: "ufw disable inaktiverar brandväggen.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b3", question: "Hur ser du UFW-status?", options: ["ufw show", "ufw status", "ufw list", "ufw rules"], correctIndex: 1, explanation: "ufw status visar aktiva regler.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b4", question: "Hur tillåter du SSH (port 22)?", options: ["ufw allow ssh", "ufw open 22", "ufw permit ssh", "ufw enable ssh"], correctIndex: 0, explanation: "ufw allow ssh eller ufw allow 22 tillåter SSH.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b5", question: "Hur tillåter du specifik port?", options: ["ufw open 80", "ufw allow 80", "ufw permit 80", "ufw add 80"], correctIndex: 1, explanation: "ufw allow PORT tillåter trafik på porten.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b6", question: "Hur blockerar du port 23?", options: ["ufw block 23", "ufw deny 23", "ufw reject 23", "ufw close 23"], correctIndex: 1, explanation: "ufw deny PORT blockerar porten.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b7", question: "Hur tar du bort UFW-regel?", options: ["ufw remove allow 22", "ufw delete allow 22", "ufw rm 22", "remove eller delete"], correctIndex: 3, explanation: "Både ufw delete och ufw remove fungerar.", difficulty: "beginner", category: "Firewall" },
    { id: "cmd-fw-b8", question: "Hur sätter du default policy till deny?", options: ["ufw default block", "ufw default deny incoming", "ufw policy deny", "ufw set deny"], correctIndex: 1, explanation: "ufw default deny incoming blockerar allt inkommande som default.", difficulty: "beginner", category: "Firewall" },

    // INTERMEDIATE - UFW & firewall-cmd
    { id: "cmd-fw-i1", question: "Hur tillåter du endast från specifik IP?", options: ["ufw allow from IP", "ufw allow IP", "ufw permit IP", "ufw whitelist IP"], correctIndex: 0, explanation: "ufw allow from IP tillåter all trafik från den IP:n.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i2", question: "Hur tillåter du port 80 endast från specifik IP?", options: ["ufw allow from IP port 80", "ufw allow from IP to any port 80", "ufw allow IP:80", "ufw allow --from IP --port 80"], correctIndex: 1, explanation: "ufw allow from IP to any port 80 är korrekt syntax.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i3", question: "Vad visar 'ufw status verbose'?", options: ["Bara portar", "Detaljerad info inkl. default policy", "Loggade attacker", "Aktiva connections"], correctIndex: 1, explanation: "verbose visar mer detaljer inklusive default policies.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i4", question: "Hur aktiverar du UFW-loggning?", options: ["ufw log on", "ufw logging on", "ufw enable-log", "ufw --log"], correctIndex: 1, explanation: "ufw logging on aktiverar loggning.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i5", question: "Hur listar du regler med nummer?", options: ["ufw status list", "ufw status numbered", "ufw list --numbers", "ufw show numbers"], correctIndex: 1, explanation: "ufw status numbered visar regler med nummer.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i6", question: "Hur tar du bort regel nummer 3?", options: ["ufw delete rule 3", "ufw delete 3", "ufw remove 3", "ufw rm 3"], correctIndex: 1, explanation: "ufw delete NUMBER tar bort regeln med det numret.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i7", question: "Vilket brandväggsverktyg används på RHEL/CentOS?", options: ["ufw", "firewall-cmd", "iptables only", "firewalld"], correctIndex: 1, explanation: "firewall-cmd är CLI för firewalld på RHEL/CentOS.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i8", question: "Hur ser du firewalld-status?", options: ["firewall-cmd --status", "firewall-cmd --state", "firewalld status", "systemctl firewalld"], correctIndex: 1, explanation: "firewall-cmd --state visar om firewalld körs.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i9", question: "Hur öppnar du port permanent i firewalld?", options: ["firewall-cmd --add-port=80/tcp", "firewall-cmd --add-port=80/tcp --permanent", "firewall-cmd --open 80", "firewall-cmd --allow 80"], correctIndex: 1, explanation: "--permanent gör regeln bestående efter reboot.", difficulty: "intermediate", category: "Firewall" },
    { id: "cmd-fw-i10", question: "Vad krävs efter --permanent i firewalld?", options: ["Inget", "firewall-cmd --reload", "Reboot", "systemctl restart"], correctIndex: 1, explanation: "--reload aktiverar permanenta ändringar.", difficulty: "intermediate", category: "Firewall" },

    // ADVANCED - Firewall
    { id: "cmd-fw-a1", question: "Hur skapar du rate limiting med UFW?", options: ["ufw limit ssh", "ufw ratelimit 22", "ufw throttle ssh", "ufw --rate ssh"], correctIndex: 0, explanation: "ufw limit ssh begränsar antal anslutningar.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a2", question: "Var finns UFW-regler lagrade?", options: ["/etc/ufw/rules", "/etc/ufw/user.rules", "/var/ufw/", "/etc/firewall/"], correctIndex: 1, explanation: "Regler finns i /etc/ufw/user.rules och user6.rules.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a3", question: "Hur resettar du UFW till default?", options: ["ufw default", "ufw reset", "ufw clear", "ufw factory"], correctIndex: 1, explanation: "ufw reset tar bort alla regler.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a4", question: "Hur tillåter du portrange?", options: ["ufw allow 8000-8100", "ufw allow 8000:8100/tcp", "ufw allow range 8000 8100", "ufw allow 8000..8100"], correctIndex: 1, explanation: "port:port/protocol för range.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a5", question: "Hur lägger du till regel före andra?", options: ["ufw prepend", "ufw insert 1 allow", "ufw first allow", "ufw --first"], correctIndex: 1, explanation: "ufw insert NUMBER lägger till på specifik position.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a6", question: "Vad är en firewalld 'zone'?", options: ["Geografisk region", "Säkerhetsnivå för nätverksgränssnitt", "Time zone", "DMZ only"], correctIndex: 1, explanation: "Zones definierar olika trust-nivåer för nätverk.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a7", question: "Hur listar du firewalld-zoner?", options: ["firewall-cmd --list-zones", "firewall-cmd --get-zones", "firewall-cmd zones", "firewalld --zones"], correctIndex: 1, explanation: "--get-zones listar alla tillgängliga zoner.", difficulty: "advanced", category: "Firewall" },
    { id: "cmd-fw-a8", question: "Hur ser du aktiv zone?", options: ["firewall-cmd --get-active", "firewall-cmd --get-active-zones", "firewall-cmd --active", "firewall-cmd --zone"], correctIndex: 1, explanation: "--get-active-zones visar zoner och gränssnitt.", difficulty: "advanced", category: "Firewall" },
];

// ============================================================================
// KOMBINERAD EXPORT & UTILITIES
// ============================================================================

export const ALL_LINUX_COMMAND_QUESTIONS: LinuxCommandQuestion[] = [
    ...NAVIGATION_QUESTIONS,
    ...TEXT_PROCESSING_QUESTIONS,
    ...PROCESS_QUESTIONS,
    ...SYSTEM_INFO_QUESTIONS,
    ...LOG_QUESTIONS,
    ...SSH_NETWORK_QUESTIONS,
    ...USER_PERMISSIONS_QUESTIONS,
    ...DOCKER_QUESTIONS,
    ...STORAGE_LVM_QUESTIONS,
    ...FIREWALL_QUESTIONS,
];

export const LINUX_COMMAND_CATEGORIES = [
    { id: "navigation", name: "Navigation & Filsystem", questions: NAVIGATION_QUESTIONS },
    { id: "text-processing", name: "Textbearbetning & Sökning", questions: TEXT_PROCESSING_QUESTIONS },
    { id: "process", name: "Processhantering", questions: PROCESS_QUESTIONS },
    { id: "system-info", name: "Systeminformation", questions: SYSTEM_INFO_QUESTIONS },
    { id: "logs", name: "Logghantering", questions: LOG_QUESTIONS },
    { id: "ssh-network", name: "SSH & Nätverk", questions: SSH_NETWORK_QUESTIONS },
    { id: "user-permissions", name: "Användare & Behörigheter", questions: USER_PERMISSIONS_QUESTIONS },
    { id: "docker", name: "Docker & Containers", questions: DOCKER_QUESTIONS },
    { id: "storage-lvm", name: "Block Storage & LVM", questions: STORAGE_LVM_QUESTIONS },
    { id: "firewall", name: "Brandvägg & Säkerhet", questions: FIREWALL_QUESTIONS },
] as const;

// Utility functions
export function getQuestionsByDifficulty(difficulty: LinuxCommandQuestion["difficulty"]): LinuxCommandQuestion[] {
    return ALL_LINUX_COMMAND_QUESTIONS.filter(q => q.difficulty === difficulty);
}

export function getQuestionsByCategory(categoryId: string): LinuxCommandQuestion[] {
    const category = LINUX_COMMAND_CATEGORIES.find(c => c.id === categoryId);
    return category ? category.questions : [];
}

export function getRandomQuestions(count: number, options?: {
    difficulty?: LinuxCommandQuestion["difficulty"];
    categoryId?: string;
}): LinuxCommandQuestion[] {
    let questions = [...ALL_LINUX_COMMAND_QUESTIONS];

    if (options?.difficulty) {
        questions = questions.filter(q => q.difficulty === options.difficulty);
    }

    if (options?.categoryId) {
        const categoryQuestions = getQuestionsByCategory(options.categoryId);
        questions = questions.filter(q => categoryQuestions.includes(q));
    }

    // Fisher-Yates shuffle
    for (let i = questions.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [questions[i], questions[j]] = [questions[j], questions[i]];
    }

    return questions.slice(0, count);
}

// Stats
export const LINUX_COMMANDS_STATS = {
    totalQuestions: ALL_LINUX_COMMAND_QUESTIONS.length,
    byDifficulty: {
        beginner: ALL_LINUX_COMMAND_QUESTIONS.filter(q => q.difficulty === "beginner").length,
        intermediate: ALL_LINUX_COMMAND_QUESTIONS.filter(q => q.difficulty === "intermediate").length,
        advanced: ALL_LINUX_COMMAND_QUESTIONS.filter(q => q.difficulty === "advanced").length,
    },
    categories: LINUX_COMMAND_CATEGORIES.map(c => ({
        id: c.id,
        name: c.name,
        count: c.questions.length,
    })),
};
