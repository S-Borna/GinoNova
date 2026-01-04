/**
 * Hands-On Lab MEGA Quiz - 150 frågor per task = 1050 totalt
 * 
 * Struktur per task:
 * - 50 beginner (nybörjare)
 * - 50 intermediate (medel) 
 * - 50 advanced (avancerad)
 * 
 * Alla frågor speglar exakt innehållet i respektive task!
 */

export type QuizDifficulty = 'beginner' | 'intermediate' | 'advanced';

export interface MegaQuizQuestion {
    id: string;
    question: string;
    options: [string, string, string, string];
    correctIndex: number;
    explanation: string;
    difficulty: QuizDifficulty;
    category: string;
}

export interface MegaQuizTaskSet {
    taskId: string;
    taskTitle: string;
    questions: MegaQuizQuestion[];
}

// ============================================================================
// TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER (150 frågor)
// ============================================================================

const TASK1_ONBOARDING_QUIZ: MegaQuizQuestion[] = [
    // ==================== BEGINNER (50) ====================
    { id: "ho1-b1", question: "Vilket kommando visar din nuvarande katalog?", options: ["cd", "pwd", "ls", "dir"], correctIndex: 1, explanation: "pwd (print working directory) visar full sökväg till nuvarande katalog.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b2", question: "Vad gör kommandot 'cd'?", options: ["Visar filer", "Byter katalog", "Skapar mapp", "Tar bort fil"], correctIndex: 1, explanation: "cd (change directory) byter till en annan katalog.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b3", question: "Hur går du till din hemmapp?", options: ["cd /home", "cd ~", "cd home", "cd root"], correctIndex: 1, explanation: "~ är en genväg till din hemmapp, t.ex. /home/username.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b4", question: "Vad gör 'cd ..'?", options: ["Går till root", "Går upp en nivå", "Går till hemma", "Går till förra katalogen"], correctIndex: 1, explanation: ".. refererar till parent-katalogen, alltså en nivå upp.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b5", question: "Vilket kommando listar filer?", options: ["list", "ls", "dir", "show"], correctIndex: 1, explanation: "ls listar innehållet i en katalog.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b6", question: "Vad visar 'ls -l'?", options: ["Endast filnamn", "Detaljerad lista", "Dolda filer", "Storlek"], correctIndex: 1, explanation: "-l visar lång (long) format med behörigheter, ägare, storlek och datum.", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b7", question: "Hur visar du dolda filer med ls?", options: ["ls -h", "ls -a", "ls -d", "ls -s"], correctIndex: 1, explanation: "-a (all) visar alla filer inklusive dolda (som börjar med .).", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b8", question: "Vad börjar dolda filer med i Linux?", options: ["_", ".", "-", "~"], correctIndex: 1, explanation: "Dolda filer och mappar börjar med punkt (.).", difficulty: "beginner", category: "Navigation" },
    { id: "ho1-b9", question: "Hur skapar du en tom fil?", options: ["create fil", "new fil", "touch fil", "make fil"], correctIndex: 2, explanation: "touch skapar en tom fil eller uppdaterar tidsstämpeln på en befintlig.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b10", question: "Hur skapar du en ny katalog?", options: ["md mapp", "mkdir mapp", "newdir mapp", "create mapp"], correctIndex: 1, explanation: "mkdir (make directory) skapar en ny katalog.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b11", question: "Vad gör 'rm fil.txt'?", options: ["Byter namn", "Flyttar", "Tar bort", "Kopierar"], correctIndex: 2, explanation: "rm (remove) tar bort filer.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b12", question: "Hur tar du bort en katalog med innehåll?", options: ["rm mapp", "rmdir mapp", "rm -r mapp", "del mapp"], correctIndex: 2, explanation: "-r (recursive) tar bort katalogen och allt innehåll.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b13", question: "Vad gör 'cp'?", options: ["Klipper", "Kopierar", "Klistrar", "Komprimerar"], correctIndex: 1, explanation: "cp (copy) kopierar filer eller kataloger.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b14", question: "Vad gör 'mv'?", options: ["Modifierar", "Flyttar/byter namn", "Monterar", "Moddar"], correctIndex: 1, explanation: "mv (move) flyttar filer eller byter namn.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b15", question: "Hur visar du innehållet i en fil?", options: ["show fil", "read fil", "cat fil", "print fil"], correctIndex: 2, explanation: "cat visar hela filens innehåll i terminalen.", difficulty: "beginner", category: "Filvisning" },
    { id: "ho1-b16", question: "Vilken pager är modernare: less eller more?", options: ["more", "less", "Samma", "cat"], correctIndex: 1, explanation: "less är nyare med fler funktioner som bakåtnavigering.", difficulty: "beginner", category: "Filvisning" },
    { id: "ho1-b17", question: "Hur avslutar du less?", options: ["Ctrl+C", "Esc", "q", "x"], correctIndex: 2, explanation: "q (quit) avslutar less.", difficulty: "beginner", category: "Filvisning" },
    { id: "ho1-b18", question: "Vad visar 'head fil.txt'?", options: ["Första 10 raderna", "Sista 10 raderna", "Hela filen", "Filinfo"], correctIndex: 0, explanation: "head visar de första 10 raderna som standard.", difficulty: "beginner", category: "Filvisning" },
    { id: "ho1-b19", question: "Vad visar 'tail fil.txt'?", options: ["Första raderna", "Sista 10 raderna", "Mitten", "Random rader"], correctIndex: 1, explanation: "tail visar de sista 10 raderna som standard.", difficulty: "beginner", category: "Filvisning" },
    { id: "ho1-b20", question: "Hur söker du efter text i en fil?", options: ["find text fil", "search text fil", "grep text fil", "locate text fil"], correctIndex: 2, explanation: "grep söker efter mönster i filer.", difficulty: "beginner", category: "Sökning" },
    { id: "ho1-b21", question: "Vad gör flaggan '-i' med grep?", options: ["Inverterar", "Ignorerar case", "Interaktiv", "Inkluderar radnummer"], correctIndex: 1, explanation: "-i gör sökningen case-insensitive (stor/liten bokstav spelar ingen roll).", difficulty: "beginner", category: "Sökning" },
    { id: "ho1-b22", question: "Hur startar du Nano-editorn?", options: ["nano", "edit", "vi", "vim"], correctIndex: 0, explanation: "nano är en enkel texteditor för nybörjare.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b23", question: "Hur sparar du i Nano?", options: ["Ctrl+S", "Ctrl+O", ":w", "F2"], correctIndex: 1, explanation: "Ctrl+O (WriteOut) sparar filen i Nano.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b24", question: "Hur avslutar du Nano?", options: ["Ctrl+Q", "Ctrl+X", "Esc", ":q"], correctIndex: 1, explanation: "Ctrl+X avslutar Nano.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b25", question: "Vilken editor startas med 'vim'?", options: ["Visual editor", "Vi Improved", "Virtual machine", "Video manager"], correctIndex: 1, explanation: "Vim = Vi Improved, en kraftfull texteditor.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b26", question: "I vilket läge startar Vim?", options: ["Insert mode", "Normal mode", "Visual mode", "Command mode"], correctIndex: 1, explanation: "Vim startar i Normal mode där du kan navigera men inte skriva text.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b27", question: "Hur går du till Insert mode i Vim?", options: ["Tryck Enter", "Tryck i", "Skriv :insert", "Tryck Tab"], correctIndex: 1, explanation: "i sätter Vim i Insert mode så du kan skriva.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b28", question: "Hur går du från Insert till Normal mode i Vim?", options: ["Ctrl+C", "Esc", "Enter", "Tab"], correctIndex: 1, explanation: "Esc tar dig tillbaka till Normal mode.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b29", question: "Hur sparar och avslutar du i Vim?", options: [":wq", ":sq", "Ctrl+S", ":exit"], correctIndex: 0, explanation: ":wq (write quit) sparar och avslutar Vim.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b30", question: "Hur avslutar du Vim UTAN att spara?", options: [":q", ":q!", ":exit", "Ctrl+Q"], correctIndex: 1, explanation: ":q! tvingar avslut utan att spara ändringar.", difficulty: "beginner", category: "Editorer" },
    { id: "ho1-b31", question: "Vad kallas /home/username?", options: ["Root", "Hemmapp", "Base", "User dir"], correctIndex: 1, explanation: "Det är användarens personliga hemmapp.", difficulty: "beginner", category: "Paths" },
    { id: "ho1-b32", question: "Var finns systemkonfigurationsfiler?", options: ["/bin", "/etc", "/home", "/var"], correctIndex: 1, explanation: "/etc innehåller systemkonfigurationsfiler.", difficulty: "beginner", category: "Paths" },
    { id: "ho1-b33", question: "Var finns loggfiler?", options: ["/log", "/var/log", "/etc/log", "/home/log"], correctIndex: 1, explanation: "/var/log är standard för loggfiler.", difficulty: "beginner", category: "Paths" },
    { id: "ho1-b34", question: "Vad är / i Linux?", options: ["Home", "Root", "Empty", "Null"], correctIndex: 1, explanation: "/ är root, toppen av filsystemet.", difficulty: "beginner", category: "Paths" },
    { id: "ho1-b35", question: "Vad gör '>' i 'echo text > fil.txt'?", options: ["Appendar", "Skriver över", "Läser", "Jämför"], correctIndex: 1, explanation: "> omdirigerar output och skriver över filen.", difficulty: "beginner", category: "Redirect" },
    { id: "ho1-b36", question: "Vad gör '>>' i shell?", options: ["Skriver över", "Lägger till i slutet", "Läser", "Skapar"], correctIndex: 1, explanation: ">> appendar (lägger till) i slutet av filen.", difficulty: "beginner", category: "Redirect" },
    { id: "ho1-b37", question: "Vad kallas första raden '#!/bin/bash' i ett script?", options: ["Header", "Shebang", "Comment", "Directive"], correctIndex: 1, explanation: "#! kallas shebang och anger vilken tolk som ska köra scriptet.", difficulty: "beginner", category: "Scripting" },
    { id: "ho1-b38", question: "Hur gör du ett script körbart?", options: ["run script", "exec script", "chmod +x script", "enable script"], correctIndex: 2, explanation: "chmod +x lägger till execute-permission.", difficulty: "beginner", category: "Scripting" },
    { id: "ho1-b39", question: "Hur kör du ett script i nuvarande katalog?", options: ["script.sh", "./script.sh", "run script.sh", "exec script.sh"], correctIndex: 1, explanation: "./ anger att scriptet finns i nuvarande katalog.", difficulty: "beginner", category: "Scripting" },
    { id: "ho1-b40", question: "Vad gör 'man ls'?", options: ["Kör ls", "Visar manual för ls", "Installerar ls", "Tar bort ls"], correctIndex: 1, explanation: "man visar manualsidan för ett kommando.", difficulty: "beginner", category: "Dokumentation" },
    { id: "ho1-b41", question: "Hur söker du i man-sidor?", options: ["/sökterm", "?sökterm", "s sökterm", "Ctrl+F"], correctIndex: 0, explanation: "/ startar sökning framåt i man/less.", difficulty: "beginner", category: "Dokumentation" },
    { id: "ho1-b42", question: "Vad gör kommandot 'clear'?", options: ["Tar bort filer", "Rensar skärmen", "Loggar ut", "Stänger terminal"], correctIndex: 1, explanation: "clear rensar terminalfönstret.", difficulty: "beginner", category: "Terminal" },
    { id: "ho1-b43", question: "Vilket tangentbordskommando rensar skärmen?", options: ["Ctrl+C", "Ctrl+L", "Ctrl+D", "Ctrl+Z"], correctIndex: 1, explanation: "Ctrl+L rensar skärmen, samma som clear.", difficulty: "beginner", category: "Terminal" },
    { id: "ho1-b44", question: "Vad gör Ctrl+C i terminalen?", options: ["Kopierar", "Avbryter körande kommando", "Rensar", "Avslutar"], correctIndex: 1, explanation: "Ctrl+C skickar SIGINT och avbryter det körande kommandot.", difficulty: "beginner", category: "Terminal" },
    { id: "ho1-b45", question: "Hur visar du historik av körda kommandon?", options: ["log", "history", "past", "commands"], correctIndex: 1, explanation: "history visar tidigare körda kommandon.", difficulty: "beginner", category: "Terminal" },
    { id: "ho1-b46", question: "Vad refererar . till i sökvägar?", options: ["Root", "Home", "Nuvarande katalog", "Parent"], correctIndex: 2, explanation: ". refererar till nuvarande katalog.", difficulty: "beginner", category: "Paths" },
    { id: "ho1-b47", question: "Hur kopierar du en mapp med innehåll?", options: ["cp mapp ny", "cp -r mapp ny", "copy mapp ny", "mv mapp ny"], correctIndex: 1, explanation: "cp -r kopierar rekursivt (hela mappstrukturen).", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b48", question: "Vad händer om du kör 'mv fil.txt /tmp/'?", options: ["Kopieras", "Flyttas till /tmp", "Tas bort", "Byter namn"], correctIndex: 1, explanation: "Filen flyttas till /tmp/-katalogen.", difficulty: "beginner", category: "Filhantering" },
    { id: "ho1-b49", question: "Vad gör 'echo Hello'?", options: ["Skapar fil", "Skriver ut Hello", "Söker Hello", "Sparar Hello"], correctIndex: 1, explanation: "echo skriver ut text till terminalen.", difficulty: "beginner", category: "Terminal" },
    { id: "ho1-b50", question: "Hur visar du 20 första raderna i en fil?", options: ["head fil", "head -20 fil", "top 20 fil", "first 20 fil"], correctIndex: 1, explanation: "head -n 20 eller head -20 visar första 20 raderna.", difficulty: "beginner", category: "Filvisning" },
    
    // ==================== INTERMEDIATE (50) ====================
    { id: "ho1-i1", question: "Vad är skillnaden mellan absolut och relativ sökväg?", options: ["Ingen skillnad", "Absolut börjar med /, relativ från nuvarande", "Relativ börjar med /", "Absolut är kortare"], correctIndex: 1, explanation: "Absolut path börjar från root (/), relativ från nuvarande position.", difficulty: "intermediate", category: "Navigation" },
    { id: "ho1-i2", question: "Vad gör 'ls -lah'?", options: ["Listar bara mappar", "Listar allt med storlek i human-readable format", "Listar hidden files", "Sorterar efter datum"], correctIndex: 1, explanation: "-l (long), -a (all), -h (human readable) kombinerat.", difficulty: "intermediate", category: "Navigation" },
    { id: "ho1-i3", question: "Hur skapar du /a/b/c om /a inte finns?", options: ["mkdir /a/b/c", "mkdir -p /a/b/c", "mkdir -r /a/b/c", "mkdir --create /a/b/c"], correctIndex: 1, explanation: "-p (parents) skapar alla saknade parent-kataloger.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i4", question: "Vad gör 'rm -rf /tmp/test'?", options: ["Frågar innan borttagning", "Tar bort utan fråga, rekursivt", "Endast tomma mappar", "Flyttar till papperskorg"], correctIndex: 1, explanation: "-r (recursive) -f (force) tar bort allt utan bekräftelse.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i5", question: "Hur följer du en loggfil i realtid?", options: ["cat -f log", "tail log", "tail -f log", "watch log"], correctIndex: 2, explanation: "tail -f (follow) visar nya rader när de läggs till.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i6", question: "Vad gör 'grep -r error /var/log'?", options: ["Söker i en fil", "Söker rekursivt i alla filer", "Visar radnummer", "Case-insensitive"], correctIndex: 1, explanation: "-r söker rekursivt i alla filer under angiven katalog.", difficulty: "intermediate", category: "Sökning" },
    { id: "ho1-i7", question: "Hur hittar du alla .txt-filer med find?", options: ["find . -name txt", "find . -name '*.txt'", "find . -type txt", "find . txt"], correctIndex: 1, explanation: "-name med wildcards hittar filer baserat på namn.", difficulty: "intermediate", category: "Sökning" },
    { id: "ho1-i8", question: "Vad gör 'cat fil1 fil2 > kombinerad'?", options: ["Jämför filer", "Slår ihop filer", "Kopierar filer", "Tar bort filer"], correctIndex: 1, explanation: "cat kan slå ihop flera filer till en.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i9", question: "Hur räknar du rader i en fil?", options: ["count fil", "wc fil", "wc -l fil", "lines fil"], correctIndex: 2, explanation: "wc -l (word count, lines) räknar rader.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i10", question: "Vad gör pipen '|' i 'ls | grep txt'?", options: ["Skriver till fil", "Skickar output som input till nästa", "Kör parallellt", "Jämför"], correctIndex: 1, explanation: "Pipe skickar stdout från ett kommando som stdin till nästa.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i11", question: "Hur söker du case-insensitive med grep?", options: ["grep -c", "grep -i", "grep -I", "grep -n"], correctIndex: 1, explanation: "-i ignorerar skillnad mellan stora och små bokstäver.", difficulty: "intermediate", category: "Sökning" },
    { id: "ho1-i12", question: "Vad visar 'ls -lt'?", options: ["Storlek och tid", "Sorterat efter tid", "Endast filer", "Tree-vy"], correctIndex: 1, explanation: "-t sorterar efter modifieringstid (nyast först).", difficulty: "intermediate", category: "Navigation" },
    { id: "ho1-i13", question: "I Vim, hur tar du bort en hel rad?", options: ["d", "dd", "x", "del"], correctIndex: 1, explanation: "dd tar bort hela raden i Normal mode.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i14", question: "I Vim, hur kopierar du en rad?", options: ["c", "cc", "yy", "copy"], correctIndex: 2, explanation: "yy (yank) kopierar hela raden.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i15", question: "I Vim, hur klistrar du in?", options: ["p", "paste", "Ctrl+V", "insert"], correctIndex: 0, explanation: "p (put) klistrar in efter markören.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i16", question: "Hur ångrar du i Vim?", options: [":undo", "u", "Ctrl+Z", "z"], correctIndex: 1, explanation: "u (undo) ångrar senaste ändringen.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i17", question: "Vad gör '2>&1' i redirect?", options: ["Skickar fil 2 till 1", "Skickar stderr till stdout", "Skriver till fil 2", "Läser från fil 1"], correctIndex: 1, explanation: "2>&1 omdirigerar stderr (2) till samma plats som stdout (1).", difficulty: "intermediate", category: "Redirect" },
    { id: "ho1-i18", question: "Hur ignorerar du felmeddelanden i output?", options: ["kommando 2>/dev/null", "kommando --quiet", "kommando -s", "kommando | null"], correctIndex: 0, explanation: "2>/dev/null skickar stderr till /dev/null (svart hål).", difficulty: "intermediate", category: "Redirect" },
    { id: "ho1-i19", question: "Vad gör 'cd -'?", options: ["Går till root", "Går till förra katalogen", "Går till hemma", "Går upp en nivå"], correctIndex: 1, explanation: "cd - växlar tillbaka till föregående katalog.", difficulty: "intermediate", category: "Navigation" },
    { id: "ho1-i20", question: "Hur visar du de 5 sista raderna i en fil?", options: ["tail fil", "tail -5 fil", "last 5 fil", "end 5 fil"], correctIndex: 1, explanation: "tail -n 5 eller tail -5 visar sista 5 raderna.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i21", question: "Vad gör 'grep -v pattern fil'?", options: ["Verbose output", "Visar INTE matchande rader", "Visar version", "Visar radnummer"], correctIndex: 1, explanation: "-v (invert) visar rader som INTE matchar mönstret.", difficulty: "intermediate", category: "Sökning" },
    { id: "ho1-i22", question: "Hur visar du radnummer med grep?", options: ["grep -l", "grep -n", "grep -c", "grep -r"], correctIndex: 1, explanation: "-n visar radnummer för varje matchning.", difficulty: "intermediate", category: "Sökning" },
    { id: "ho1-i23", question: "Vad gör 'sort fil.txt'?", options: ["Sorterar filen på plats", "Visar sorterad", "Sorterar och sparar", "Sorterar omvänt"], correctIndex: 1, explanation: "sort visar sorterad output men ändrar inte filen.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i24", question: "Hur tar du bort dubbletter i sorterad output?", options: ["sort -d", "sort | unique", "sort | uniq", "sort -u"], correctIndex: 2, explanation: "uniq tar bort intilliggande dubbletter (kräver sorterad input).", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i25", question: "I Vim, hur går du till rad 50?", options: ["goto 50", ":50", "line 50", "50G"], correctIndex: 3, explanation: "50G eller :50 går till rad 50.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i26", question: "Hur söker du i Vim?", options: ["Ctrl+F", "/sökord", ":search", "?search"], correctIndex: 1, explanation: "/sökord söker framåt i dokumentet.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i27", question: "I Vim, hur ersätter du alla 'foo' med 'bar'?", options: ["s/foo/bar", ":s/foo/bar/g", ":%s/foo/bar/g", "replace foo bar"], correctIndex: 2, explanation: ":%s/foo/bar/g ersätter alla förekomster i hela filen.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i28", question: "Var finns användarnas hemkataloger?", options: ["/users", "/home", "/usr", "/root"], correctIndex: 1, explanation: "/home innehåller vanliga användares hemkataloger.", difficulty: "intermediate", category: "Paths" },
    { id: "ho1-i29", question: "Vad är /root?", options: ["Root-filsystemet", "Roots hemmapp", "Toppen av fs", "En tom mapp"], correctIndex: 1, explanation: "/root är root-användarens (admin) hemmapp.", difficulty: "intermediate", category: "Paths" },
    { id: "ho1-i30", question: "Var finns körbara systemprogram?", options: ["/bin och /usr/bin", "/etc", "/home", "/var"], correctIndex: 0, explanation: "/bin och /usr/bin innehåller körbara program.", difficulty: "intermediate", category: "Paths" },
    { id: "ho1-i31", question: "Vad gör 'which ls'?", options: ["Visar hjälp för ls", "Visar var ls finns", "Kör ls", "Visar ls alias"], correctIndex: 1, explanation: "which visar den fullständiga sökvägen till ett kommando.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i32", question: "Hur kör du förra kommandot igen?", options: ["repeat", "!!", "again", "last"], correctIndex: 1, explanation: "!! kör det senaste kommandot igen.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i33", question: "Vad gör '!grep'?", options: ["Negerar grep", "Kör senaste grep-kommandot", "Visar grep-hjälp", "Installerar grep"], correctIndex: 1, explanation: "!kommando kör det senaste kommandot som började med det ordet.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i34", question: "Hur ser du alias i din shell?", options: ["show alias", "alias", "list alias", "aliases"], correctIndex: 1, explanation: "Kommandot 'alias' utan argument visar alla definierade alias.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i35", question: "Vad gör 'ln -s target link'?", options: ["Hårdlänk", "Symbolisk länk", "Kopiera", "Flytta"], correctIndex: 1, explanation: "ln -s skapar en symbolisk (mjuk) länk.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i36", question: "Vad visar 'file myfile'?", options: ["Filstorlek", "Filtyp", "Filinnehåll", "Filbehörigheter"], correctIndex: 1, explanation: "file-kommandot identifierar filtypen baserat på innehållet.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i37", question: "Hur visar du diskutrymme för en katalog?", options: ["df katalog", "du katalog", "disk katalog", "space katalog"], correctIndex: 1, explanation: "du (disk usage) visar hur mycket utrymme en katalog använder.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i38", question: "Vad gör 'du -sh /home'?", options: ["Visar alla filer", "Visar total storlek human-readable", "Visar struktur", "Sorterar"], correctIndex: 1, explanation: "-s (summary) -h (human) visar total storlek i läsbart format.", difficulty: "intermediate", category: "Filhantering" },
    { id: "ho1-i39", question: "Hur klipper du i Nano?", options: ["Ctrl+X", "Ctrl+K", "Ctrl+C", "Ctrl+W"], correctIndex: 1, explanation: "Ctrl+K klipper (cut) raden i Nano.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i40", question: "Hur söker du i Nano?", options: ["Ctrl+F", "Ctrl+W", "Ctrl+S", "/"], correctIndex: 1, explanation: "Ctrl+W (Where is) startar sökning i Nano.", difficulty: "intermediate", category: "Editorer" },
    { id: "ho1-i41", question: "Vad gör 'head -n -5 fil'?", options: ["Första 5 raderna", "Allt utom sista 5", "Sista 5 raderna", "Error"], correctIndex: 1, explanation: "Negativt tal visar allt UTOM de sista n raderna.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i42", question: "Hur visar du unika rader med antal?", options: ["uniq", "uniq -c", "sort -c", "count -u"], correctIndex: 1, explanation: "uniq -c räknar och visar antal av varje unik rad.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i43", question: "Vad gör 'cut -d: -f1 /etc/passwd'?", options: ["Tar bort rad 1", "Visar första fältet med : som delimiter", "Klipper filen", "Visar användarnamn"], correctIndex: 1, explanation: "cut extraherar fält; -d: sätter delimiter, -f1 tar första fältet.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i44", question: "Hur visar du filer sorterade efter storlek?", options: ["ls -lS", "ls -ls", "ls -size", "ls --sort=size"], correctIndex: 0, explanation: "-S sorterar efter storlek (störst först).", difficulty: "intermediate", category: "Navigation" },
    { id: "ho1-i45", question: "Vad gör 'tee'?", options: ["Läser input", "Skriver till fil OCH stdout", "Skapar T-junction", "Testar kommandon"], correctIndex: 1, explanation: "tee skriver till fil samtidigt som det skickar till stdout.", difficulty: "intermediate", category: "Redirect" },
    { id: "ho1-i46", question: "Hur sparar du command output till fil OCH ser det?", options: ["cmd > fil && cat fil", "cmd | tee fil", "cmd >> fil", "cmd &> fil"], correctIndex: 1, explanation: "cmd | tee fil visar output och sparar det samtidigt.", difficulty: "intermediate", category: "Redirect" },
    { id: "ho1-i47", question: "Vad gör 'diff fil1 fil2'?", options: ["Slår ihop filer", "Visar skillnader", "Kopierar skillnader", "Tar bort skillnader"], correctIndex: 1, explanation: "diff visar skillnader mellan två filer.", difficulty: "intermediate", category: "Filvisning" },
    { id: "ho1-i48", question: "Hur ser du i vilken shell du kör?", options: ["shell", "echo $SHELL", "which shell", "ps shell"], correctIndex: 1, explanation: "$SHELL-variabeln innehåller din default shell.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i49", question: "Vad är skillnaden mellan bash och sh?", options: ["Ingen", "bash har fler features", "sh är nyare", "bash är snabbare"], correctIndex: 1, explanation: "bash är en utökad version av sh med fler funktioner.", difficulty: "intermediate", category: "Terminal" },
    { id: "ho1-i50", question: "Hur gör du ett kommando till bakgrundsjobb?", options: ["bg kommando", "kommando &", "nohup kommando", "kommando --bg"], correctIndex: 1, explanation: "& i slutet kör kommandot i bakgrunden.", difficulty: "intermediate", category: "Terminal" },
    
    // ==================== ADVANCED (50) ====================
    { id: "ho1-a1", question: "Vad är skillnaden mellan 'cp -a' och 'cp -r'?", options: ["Ingen skillnad", "-a bevarar attribut och länkar", "-r är snabbare", "-a är för arkiv"], correctIndex: 1, explanation: "-a (archive) bevarar permissions, timestamps, länkar etc. -r bara kopierar rekursivt.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a2", question: "Hur hittar du filer större än 100MB?", options: ["find . -size 100M", "find . -size +100M", "find . -bigger 100M", "ls -size +100M"], correctIndex: 1, explanation: "+100M hittar filer STÖRRE än 100MB. Utan + = exakt storlek.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a3", question: "Vad gör 'find . -type f -name '*.log' -mtime +30 -delete'?", options: ["Hittar loggfiler", "Tar bort loggfiler äldre än 30 dagar", "Flyttar loggfiler", "Arkiverar loggfiler"], correctIndex: 1, explanation: "-mtime +30 = äldre än 30 dagar, -delete tar bort dem.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a4", question: "Hur hittar du filer med specifika permissions?", options: ["find . -perm", "find . -mode", "find . -access", "ls -perm"], correctIndex: 0, explanation: "find -perm hittar filer med specifika behörigheter.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a5", question: "Vad gör 'xargs' i en pipeline?", options: ["Kör i parallell", "Bygger argument från stdin", "Extraherar argument", "Validerar argument"], correctIndex: 1, explanation: "xargs tar stdin och bygger kommandoradsargument.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a6", question: "Hur kör du 'rm' på alla filer find hittar?", options: ["find . -exec rm", "find . | rm", "find . -exec rm {} \\;", "find . | xargs rm"], correctIndex: 2, explanation: "-exec rm {} \\; kör rm på varje fil. {} ersätts med filnamnet.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a7", question: "Vad är fördelen med 'find -exec + ' vs '-exec \\;'?", options: ["Ingen skillnad", "+ kör kommandot en gång med alla filer", "\\; är snabbare", "+ fungerar på fler system"], correctIndex: 1, explanation: "+ samlar filer och kör kommandot en gång, \\; kör per fil.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a8", question: "Hur skapar du en hardlink?", options: ["ln -s target link", "ln target link", "link target link", "hardlink target link"], correctIndex: 1, explanation: "ln utan -s skapar hardlink (delar samma inode).", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a9", question: "Vad händer om originalet tas bort för en hardlink?", options: ["Länken bryts", "Data finns kvar", "Båda tas bort", "Error"], correctIndex: 1, explanation: "Hardlinks delar inode - data finns tills ALLA länkar är borta.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a10", question: "Vad händer om originalet tas bort för en symlink?", options: ["Länken fungerar", "Länken blir bruten", "Båda tas bort", "Data flyttas"], correctIndex: 1, explanation: "Symlinks pekar på filnamnet - om filen tas bort bryts länken.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a11", question: "Hur ser du inodes för filer?", options: ["ls -l", "ls -i", "stat", "ls -i och stat"], correctIndex: 3, explanation: "ls -i visar inode-nummer, stat visar detaljerad info.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a12", question: "Vad är /dev/null?", options: ["Tom enhet", "Svart hål för data", "Null-disk", "Error device"], correctIndex: 1, explanation: "/dev/null tar emot och kastar bort all data (bit bucket).", difficulty: "advanced", category: "Redirect" },
    { id: "ho1-a13", question: "Vad är /dev/zero?", options: ["Skriver nollor", "Producerar oändliga nollor", "Nollställer disk", "Tom fil"], correctIndex: 1, explanation: "/dev/zero producerar oändligt med null-bytes vid läsning.", difficulty: "advanced", category: "Redirect" },
    { id: "ho1-a14", question: "Hur skapar du en 1GB fil fylld med nollor?", options: ["touch 1G", "dd if=/dev/zero of=fil bs=1G count=1", "fallocate -l 1G fil", "Både dd och fallocate"], correctIndex: 3, explanation: "Både dd och fallocate fungerar för att skapa stora filer.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a15", question: "Vad gör 'grep -E'?", options: ["Exakt matchning", "Extended regex", "Error output", "Exclude"], correctIndex: 1, explanation: "-E aktiverar utökade regular expressions (ERE).", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a16", question: "Hur matchar du 'error' eller 'warning' med grep?", options: ["grep error|warning", "grep 'error|warning'", "grep -E 'error|warning'", "grep error warning"], correctIndex: 2, explanation: "| för alternation kräver -E (extended) eller egrep.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a17", question: "Vad gör 'awk '{print $1}' fil'?", options: ["Skriver ut rad 1", "Skriver ut kolumn 1", "Skriver ut tecken 1", "Skriver ut ord 1"], correctIndex: 1, explanation: "awk $1 refererar till första fältet (kolumnen).", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a18", question: "Hur räknar du ord i en fil?", options: ["wc fil", "wc -w fil", "count fil", "words fil"], correctIndex: 1, explanation: "wc -w räknar ord (words).", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a19", question: "Vad gör 'sed 's/foo/bar/' fil'?", options: ["Tar bort foo", "Ersätter första foo med bar", "Ersätter alla foo", "Lägger till bar efter foo"], correctIndex: 1, explanation: "s/foo/bar/ ersätter första förekomsten per rad. Lägg till /g för alla.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a20", question: "Hur ersätter du alla förekomster med sed?", options: ["sed 's/foo/bar/'", "sed 's/foo/bar/g'", "sed 'g/foo/bar/'", "sed -a 's/foo/bar/'"], correctIndex: 1, explanation: "/g (global) ersätter alla förekomster på raden.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a21", question: "Hur redigerar du en fil på plats med sed?", options: ["sed 's/a/b/' fil", "sed -i 's/a/b/' fil", "sed --inplace 's/a/b/' fil", "sed -e 's/a/b/' fil"], correctIndex: 1, explanation: "-i (in-place) modifierar filen direkt.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a22", question: "Vad gör 'tar -czvf arkiv.tar.gz mapp/'?", options: ["Extraherar", "Komprimerar med gzip", "Listar innehåll", "Verifierar arkiv"], correctIndex: 1, explanation: "c=create, z=gzip, v=verbose, f=file. Skapar gzippat tar-arkiv.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a23", question: "Hur extraherar du ett .tar.gz-arkiv?", options: ["tar -czvf", "tar -xzvf", "tar -tzvf", "untar"], correctIndex: 1, explanation: "x=extract extraherar arkivet.", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a24", question: "I Vim, hur öppnar du en fil i delad vy?", options: [":sp fil", ":vs fil", "Båda fungerar", ":split fil"], correctIndex: 2, explanation: ":sp (horizontal split) och :vs (vertical split) båda fungerar.", difficulty: "advanced", category: "Editorer" },
    { id: "ho1-a25", question: "I Vim, hur navigerar du mellan splittade fönster?", options: ["Tab", "Ctrl+W följt av piltangent", "Alt+pil", "F6"], correctIndex: 1, explanation: "Ctrl+W och sedan piltangent eller hjkl för att byta fönster.", difficulty: "advanced", category: "Editorer" },
    { id: "ho1-a26", question: "Vad gör 'vim -d fil1 fil2'?", options: ["Öppnar båda", "Diff-läge", "Dubbelvy", "Debug-läge"], correctIndex: 1, explanation: "-d öppnar Vim i diff-läge för att jämföra filer.", difficulty: "advanced", category: "Editorer" },
    { id: "ho1-a27", question: "Vad är en process substitution i bash?", options: ["$(...)", "<(...)", "{...}", "[...]"], correctIndex: 1, explanation: "<(cmd) och >(cmd) är process substitution.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a28", question: "Hur jämför du output från två kommandon?", options: ["diff cmd1 cmd2", "diff <(cmd1) <(cmd2)", "cmd1 | diff cmd2", "diff $(cmd1) $(cmd2)"], correctIndex: 1, explanation: "Process substitution låter diff jämföra output från två kommandon.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a29", question: "Vad gör 'command1 && command2'?", options: ["Kör båda", "Kör cmd2 bara om cmd1 lyckas", "Kör cmd2 bara om cmd1 misslyckas", "Kör parallellt"], correctIndex: 1, explanation: "&& kör nästa kommando endast om föregående hade exit code 0.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a30", question: "Vad gör 'command1 || command2'?", options: ["Kör båda", "Kör cmd2 bara om cmd1 lyckas", "Kör cmd2 bara om cmd1 misslyckas", "Logisk ELLER"], correctIndex: 2, explanation: "|| kör nästa kommando endast om föregående misslyckades.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a31", question: "Hur kollar du exit-koden för senaste kommando?", options: ["exit", "$?", "exitcode", "echo error"], correctIndex: 1, explanation: "$? innehåller exit-koden från senaste kommandot.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a32", question: "Vad betyder exit code 0?", options: ["Error", "Success", "Warning", "Not found"], correctIndex: 1, explanation: "Exit code 0 betyder att kommandot lyckades.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a33", question: "Hur kör du ett kommando med timeout?", options: ["timeout 5 cmd", "cmd --timeout 5", "time 5 cmd", "limit 5 cmd"], correctIndex: 0, explanation: "timeout kör ett kommando och dödar det efter angiven tid.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a34", question: "Vad gör 'nohup command &'?", options: ["Tystar output", "Kör även efter logout", "Kör med högre prioritet", "Kör som root"], correctIndex: 1, explanation: "nohup gör att kommandot fortsätter köra även om du loggar ut.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a35", question: "Hur ser du bakgrundsjobb i din shell?", options: ["ps", "jobs", "bg", "tasks"], correctIndex: 1, explanation: "jobs visar bakgrundsjobb startade i aktuell shell.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a36", question: "Hur tar du ett bakgrundsjobb till förgrunden?", options: ["foreground", "fg", "front %1", "bring %1"], correctIndex: 1, explanation: "fg tar bakgrundsjobb till förgrunden.", difficulty: "advanced", category: "Terminal" },
    { id: "ho1-a37", question: "Vad gör 'less +F fil'?", options: ["Öppnar från slutet", "Följer filen som tail -f", "Öppnar snabbare", "Force-öppnar"], correctIndex: 1, explanation: "+F startar less i follow-mode, som tail -f.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a38", question: "Hur söker du bakåt i less?", options: ["/sökord", "?sökord", "b sökord", "r sökord"], correctIndex: 1, explanation: "? söker bakåt i filen, / söker framåt.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a39", question: "Vad gör 'tr' kommandot?", options: ["Transfer", "Translate/delete characters", "Tree", "Trace"], correctIndex: 1, explanation: "tr översätter eller tar bort tecken.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a40", question: "Hur konverterar du till versaler?", options: ["upper fil", "tr a-z A-Z", "tr [:lower:] [:upper:]", "Båda tr-metoderna"], correctIndex: 3, explanation: "Båda syntaxerna fungerar för att konvertera till versaler.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a41", question: "Vad gör 'find . -empty'?", options: ["Hittar tomma filer/mappar", "Hittar fulla diskar", "Skapar tomma filer", "Tar bort tomma"], correctIndex: 0, explanation: "-empty hittar tomma filer och kataloger.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a42", question: "Hur hittar du endast kataloger med find?", options: ["find . -dir", "find . -type d", "find . -d", "find . -folder"], correctIndex: 1, explanation: "-type d hittar endast kataloger (directories).", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a43", question: "Hur hittar du endast vanliga filer?", options: ["find . -type f", "find . -files", "find . -regular", "find . -f"], correctIndex: 0, explanation: "-type f hittar endast vanliga filer (files).", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a44", question: "Vad gör 'locate'?", options: ["Hittar filer i databas", "Hittar nuvarande position", "Söker i PATH", "Hittar kommandon"], correctIndex: 0, explanation: "locate söker i en förbyggd databas (snabbare än find).", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a45", question: "Hur uppdaterar du locate-databasen?", options: ["locate --update", "updatedb", "refresh locate", "locate -u"], correctIndex: 1, explanation: "updatedb uppdaterar databasen som locate använder.", difficulty: "advanced", category: "Sökning" },
    { id: "ho1-a46", question: "Vad gör 'stat fil'?", options: ["Visar status", "Visar detaljerad fil-metadata", "Startar fil", "Statistik om fil"], correctIndex: 1, explanation: "stat visar detaljerad information om en fil (inode, storlek, tider, etc).", difficulty: "advanced", category: "Filhantering" },
    { id: "ho1-a47", question: "I Vim, vad gör makron?", options: ["Spelar in och spelar upp tangentsekvenser", "Skapar genvägar", "Definierar variabler", "Kör externa kommandon"], correctIndex: 0, explanation: "qa startar inspelning till register a, q stoppar, @a spelar upp.", difficulty: "advanced", category: "Editorer" },
    { id: "ho1-a48", question: "I Vim, hur startar du makroinspelning till register a?", options: ["macro a", "qa", ":record a", "@a"], correctIndex: 1, explanation: "qa börjar spela in till register a.", difficulty: "advanced", category: "Editorer" },
    { id: "ho1-a49", question: "Vad gör 'column -t'?", options: ["Skapar kolumner", "Formaterar som tabell", "Tar bort kolumner", "Räknar kolumner"], correctIndex: 1, explanation: "column -t formaterar input som en snygg tabell.", difficulty: "advanced", category: "Filvisning" },
    { id: "ho1-a50", question: "Hur visar du filsystemhierarkin som träd?", options: ["ls -R", "tree", "find . -tree", "dir /s"], correctIndex: 1, explanation: "tree-kommandot visar en grafisk trädvy av filsystemet.", difficulty: "advanced", category: "Navigation" },
];

// ============================================================================
// EXPORT HELPERS
// ============================================================================

export const HANDSON_MEGA_QUIZ: MegaQuizTaskSet[] = [
    {
        taskId: "handson-1-onboarding",
        taskTitle: "Onboarding - Filsystem & Texteditorer",
        questions: TASK1_ONBOARDING_QUIZ
    },
    // More tasks will be added below...
];

// Helper to get questions by difficulty
export function getQuestionsByDifficulty(taskId: string, difficulty: QuizDifficulty): MegaQuizQuestion[] {
    const taskSet = HANDSON_MEGA_QUIZ.find(t => t.taskId === taskId);
    if (!taskSet) return [];
    return taskSet.questions.filter(q => q.difficulty === difficulty);
}

// Helper to get all questions for a task
export function getAllQuestionsForTask(taskId: string): MegaQuizQuestion[] {
    const taskSet = HANDSON_MEGA_QUIZ.find(t => t.taskId === taskId);
    return taskSet?.questions || [];
}

// Helper to get shuffled questions
export function getShuffledQuestions(taskId: string, difficulty?: QuizDifficulty, count?: number): MegaQuizQuestion[] {
    let questions = difficulty 
        ? getQuestionsByDifficulty(taskId, difficulty)
        : getAllQuestionsForTask(taskId);
    
    // Fisher-Yates shuffle
    const shuffled = [...questions];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    
    return count ? shuffled.slice(0, count) : shuffled;
}

// Get total count
export function getTotalQuestionCount(): number {
    return HANDSON_MEGA_QUIZ.reduce((sum, task) => sum + task.questions.length, 0);
}

