# Bash Power Tools

Fokus: Redirection, pipes och textverktyg

## Redirection: >, >>, 2>, &>

Redirection styr var output hamnar.

### Standard streams

```bash
# stdin  (0) - Standard input (tangentbord)
# stdout (1) - Standard output (skärm)
# stderr (2) - Standard error (skärm, men separat kanal)
```

### Output redirection

```bash
# > skriver till fil (överskriver)
echo "hello" > file.txt

# >> appendra till fil
echo "world" >> file.txt

# Skapa tom fil
> file.txt
```

### Stderr redirection

```bash
# 2> skickar stderr till fil
ls /nonexistent 2> errors.txt

# 2>> appendra stderr
ls /nonexistent 2>> errors.txt

# Ignorera stderr
ls /nonexistent 2> /dev/null
```

### Kombinera stdout och stderr

```bash
# &> eller >& skickar BÅDE stdout och stderr till fil
command &> output.txt

# Samma sak, mer explicit
command > output.txt 2>&1
# Förklaring: > output.txt sätter stdout till fil
#            2>&1 sätter stderr till samma som stdout

# Separera stdout och stderr till olika filer
command > stdout.txt 2> stderr.txt

# Appendra båda
command >> output.txt 2>&1
```

### Input redirection

```bash
# < läser från fil
sort < unsorted.txt

# << here document
cat << EOF
Line 1
Line 2
EOF

# <<< here string
grep "hello" <<< "hello world"
```

### Praktiska exempel

```bash
# Logga allt (inkl. fel) till fil
./script.sh &> script.log

# Visa output men logga också
./script.sh 2>&1 | tee script.log

# Ignorera all output
./script.sh &> /dev/null

# Skicka stderr till stdout (för att pipa)
ls /nonexistent 2>&1 | grep "No such"
```

## Pipes: Koppla ihop kommandon

Pipes (`|`) skickar stdout från ett kommando till stdin för nästa.

```bash
# Grundläggande pipe
cat file.txt | grep "pattern"

# Kedja flera kommandon
cat file.txt | grep "pattern" | sort | uniq

# Praktiska exempel
ps aux | grep nginx           # Hitta nginx-processer
history | grep "git"          # Hitta git-kommandon
ls -la | wc -l                # Räkna filer
cat log.txt | tail -100       # Sista 100 raderna
```

### Pipelines och exit codes

```bash
# Utan pipefail: exit code = sista kommandots exit code
false | true
echo $?  # 0 (true lyckades)

# Med set -o pipefail: första felet avgör
set -o pipefail
false | true
echo $?  # 1 (false misslyckades)
```

### Pipe till flera kommandon med tee

```bash
# tee skriver till fil OCH stdout
command | tee output.txt | next_command

# Flera filer
command | tee file1.txt file2.txt

# Appendra
command | tee -a log.txt
```

### Process substitution

```bash
# <() skapar en temporär fil med output
diff <(ls dir1) <(ls dir2)

# Jämför output från två kommandon
diff <(sort file1.txt) <(sort file2.txt)

# Läs output som fil
while read line; do
    echo "$line"
done < <(ls -la)
```

## grep: Sökning efter mönster

grep söker efter textmönster i filer eller input.

### Grundläggande grep

```bash
# Sök i fil
grep "pattern" file.txt

# Sök i flera filer
grep "pattern" *.txt

# Rekursiv sökning
grep -r "pattern" /path/to/dir

# Case-insensitive
grep -i "pattern" file.txt
```

### Vanliga grep-flaggor

```bash
-i    # Case-insensitive
-v    # Invertera (visa rader som INTE matchar)
-n    # Visa radnummer
-c    # Räkna matchande rader
-l    # Visa bara filnamn (som innehåller match)
-L    # Visa filnamn som INTE matchar
-r    # Rekursiv sökning
-w    # Matcha hela ord
-x    # Matcha hela raden
-A N  # Visa N rader efter match
-B N  # Visa N rader före match
-C N  # Visa N rader före och efter (context)
-E    # Extended regex (egrep)
-o    # Visa bara matchande del
-q    # Quiet (exit 0 om match, exit 1 annars)
```

### Praktiska grep-exempel

```bash
# Hitta alla IP-adresser
grep -E "\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b" file.txt

# Visa rader utan kommentarer
grep -v "^#" config.file

# Hitta filer som innehåller "TODO"
grep -r -l "TODO" src/

# Räkna fel i logg
grep -c "ERROR" /var/log/syslog

# Sök med context
grep -C 3 "error" log.txt

# Test om mönster finns (i script)
if grep -q "pattern" file.txt; then
    echo "Found!"
fi
```

### egrep (extended regex)

```bash
# egrep = grep -E
egrep "pattern1|pattern2" file.txt    # OR
egrep "word+" file.txt                # + utan escape
egrep "(group){2,}" file.txt          # Gruppering
```

## cut: Klipp ut kolumner

cut extraherar delar av varje rad.

### Delimiter och fields

```bash
# -d delimiter (default: tab)
# -f field(s)

# Klipp ut första fältet (kolon-separerat)
cut -d: -f1 /etc/passwd

# Flera fält
cut -d: -f1,3 /etc/passwd        # Fält 1 och 3
cut -d: -f1-3 /etc/passwd        # Fält 1 till 3
cut -d, -f2- file.csv            # Fält 2 till slutet

# Med space som delimiter
cut -d' ' -f2 file.txt
```

### Character positions

```bash
# -c character position(s)
cut -c1-10 file.txt              # Första 10 tecknen
cut -c5- file.txt                # Tecken 5 till slutet
cut -c-5 file.txt                # Första 5 tecknen
```

### Praktiska cut-exempel

```bash
# Användare från passwd
cut -d: -f1 /etc/passwd

# UID från passwd
cut -d: -f3 /etc/passwd

# Kombinera med pipes
cat /etc/passwd | cut -d: -f1,6 | head -5
```

## sed: Stream Editor

sed är en kraftfull stream editor för texttransformationer.

### Grundläggande substitution

```bash
# s/old/new/ - ersätt första förekomsten per rad
sed 's/old/new/' file.txt

# s/old/new/g - ersätt ALLA förekomster per rad
sed 's/old/new/g' file.txt

# Case-insensitive
sed 's/old/new/gi' file.txt
```

### In-place editing

```bash
# -i redigerar filen direkt
sed -i 's/old/new/g' file.txt

# Med backup (rekommenderat!)
sed -i.bak 's/old/new/g' file.txt
# Skapar file.txt.bak innan ändring
```

### Adressering

```bash
# Specifik rad
sed '5s/old/new/' file.txt       # Endast rad 5

# Radintervall
sed '1,10s/old/new/g' file.txt   # Rad 1-10

# Från mönster till mönster
sed '/start/,/end/s/old/new/g' file.txt
```

### Vanliga sed-operationer

```bash
# Ta bort rader
sed '/pattern/d' file.txt        # Rader med pattern
sed '5d' file.txt                # Rad 5
sed '1,10d' file.txt             # Rad 1-10
sed '/^#/d' file.txt             # Rader som börjar med #
sed '/^$/d' file.txt             # Tomma rader

# Infoga text
sed '3i\New line' file.txt       # Infoga före rad 3
sed '3a\New line' file.txt       # Infoga efter rad 3

# Visa specifika rader
sed -n '5p' file.txt             # Endast rad 5
sed -n '1,10p' file.txt          # Rad 1-10
sed -n '/pattern/p' file.txt    # Rader med pattern
```

### Praktiska sed-exempel

```bash
# Ta bort trailing whitespace
sed 's/[[:space:]]*$//' file.txt

# Ersätt Windows line endings
sed 's/\r$//' file.txt

# Omge mönster med quotes
sed 's/[^ ]*/\"&\"/' file.txt

# Flera operationer
sed -e 's/foo/bar/g' -e 's/baz/qux/g' file.txt
```

## awk: Pattern scanning och processing

awk är ett komplett programmeringsspråk för textbearbetning.

### Grundläggande awk

```bash
# Syntax: awk 'pattern { action }' file

# Visa specifika kolumner (default: space/tab-separerat)
awk '{print $1}' file.txt        # Första kolumnen
awk '{print $1, $3}' file.txt    # Kolumn 1 och 3
awk '{print $NF}' file.txt       # Sista kolumnen
awk '{print NR, $0}' file.txt    # Radnummer + hela raden
```

### Inbyggda variabler

```bash
$0    # Hela raden
$1-$n # Fält (kolumner)
NF    # Antal fält på raden
NR    # Radnummer
FS    # Field separator (default: whitespace)
OFS   # Output field separator
RS    # Record separator (default: newline)
```

### Field separator

```bash
# -F sätter delimiter
awk -F: '{print $1}' /etc/passwd         # Kolon
awk -F',' '{print $2}' file.csv          # Komma
awk -F'\t' '{print $1}' file.tsv         # Tab

# Inom awk
awk 'BEGIN{FS=":"} {print $1}' /etc/passwd
```

### Pattern matching

```bash
# Villkor
awk '/pattern/ {print}' file.txt         # Rader med pattern
awk '$3 > 100 {print $1, $3}' file.txt   # Kolumn 3 > 100
awk 'NR > 1 {print}' file.txt            # Skippa header
awk 'NF > 0 {print}' file.txt            # Icke-tomma rader
```

### Beräkningar

```bash
# Summera kolumn
awk '{sum += $1} END {print sum}' numbers.txt

# Genomsnitt
awk '{sum += $1; count++} END {print sum/count}' numbers.txt

# Max/min
awk 'NR==1 || $1 > max {max=$1} END {print max}' numbers.txt
```

### Praktiska awk-exempel

```bash
# Summera diskutrymme
df -h | awk 'NR>1 {print $5, $6}'

# Hitta stora processer
ps aux | awk '$3 > 1.0 {print $1, $3, $11}'

# Formaterad output
awk '{printf "%-10s %5d\n", $1, $2}' file.txt

# Räkna unika värden
awk '{count[$1]++} END {for (val in count) print val, count[val]}' file.txt
```

### BEGIN och END

```bash
awk '
BEGIN {
    print "=== START ==="
    FS=","
}
{
    print $1, $2
}
END {
    print "=== END ==="
    print "Total lines:", NR
}
' file.csv
```

## sort: Sortera rader

```bash
# Alfabetisk sortering
sort file.txt

# Numerisk sortering
sort -n numbers.txt

# Omvänd ordning
sort -r file.txt

# Sortera på specifik kolumn
sort -k2 file.txt                # Kolumn 2
sort -k2,2 file.txt              # Endast kolumn 2
sort -t: -k3 -n /etc/passwd      # Sortera på UID

# Unik sortering
sort -u file.txt

# Case-insensitive
sort -f file.txt

# Human-readable (1K, 2M, 3G)
sort -h sizes.txt
```

### Kombinera med uniq

```bash
# uniq kräver sorterad input
sort file.txt | uniq             # Ta bort duplicates
sort file.txt | uniq -c          # Räkna förekomster
sort file.txt | uniq -d          # Visa endast duplicates
```

## wc: Räkna ord/rader/tecken

```bash
wc file.txt                      # Rader, ord, bytes
wc -l file.txt                   # Endast rader
wc -w file.txt                   # Endast ord
wc -c file.txt                   # Endast bytes
wc -m file.txt                   # Endast tecken

# Räkna filer
ls | wc -l

# Räkna matchningar
grep -c "pattern" file.txt
grep "pattern" file.txt | wc -l
```

## tr: Translate/delete tecken

```bash
# Översätt tecken
echo "hello" | tr 'a-z' 'A-Z'    # Versaler: HELLO
echo "HELLO" | tr 'A-Z' 'a-z'    # Gemener: hello

# Ta bort tecken
echo "hello123" | tr -d '0-9'    # hello

# Squeeze repeterade tecken
echo "heeello" | tr -s 'e'       # helo

# Complement (allt UTOM)
echo "hello123" | tr -cd '0-9'   # 123

# Ersätt newlines med space
cat file.txt | tr '\n' ' '

# Ta bort carriage returns (Windows → Unix)
tr -d '\r' < windows.txt > unix.txt
```

## head/tail: Visa delar av fil

```bash
# head - visa början
head file.txt                    # Första 10 rader
head -n 5 file.txt               # Första 5 rader
head -n -5 file.txt              # Alla UTOM sista 5

# tail - visa slutet
tail file.txt                    # Sista 10 rader
tail -n 5 file.txt               # Sista 5 rader
tail -n +5 file.txt              # Från rad 5 till slutet

# Follow (live log monitoring)
tail -f /var/log/syslog
tail -F /var/log/syslog          # Följ även om fil roteras
```

## Regex Basics: Reguljära uttryck

### Grundläggande mönster

```bash
.        # Valfritt tecken
*        # 0 eller fler av föregående
+        # 1 eller fler (extended regex)
?        # 0 eller 1 av föregående (extended)
^        # Start av rad
$        # Slut av rad
[]       # Character class
[^]      # Negerad character class
\        # Escape special character
```

### Character classes

```bash
[abc]    # a, b eller c
[a-z]    # a till z
[0-9]    # Siffror
[^0-9]   # Allt UTOM siffror
[A-Za-z] # Alla bokstäver
```

### POSIX character classes

```bash
[[:alpha:]]  # Bokstäver
[[:digit:]]  # Siffror (0-9)
[[:alnum:]]  # Bokstäver och siffror
[[:space:]]  # Whitespace
[[:lower:]]  # Gemener
[[:upper:]]  # Versaler
```

### Extended regex (ERE)

```bash
# Använd grep -E eller egrep
+        # 1 eller fler
?        # 0 eller 1
{n}      # Exakt n gånger
{n,m}    # n till m gånger
{n,}     # n eller fler
|        # OR
()       # Gruppering

# Exempel
grep -E "colou?r" file.txt       # color eller colour
grep -E "(hello|world)" file.txt # hello eller world
grep -E "[0-9]{3}" file.txt      # 3 siffror
```

### Praktiska regex-exempel

```bash
# Email (förenklat)
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" file.txt

# IP-adress
grep -E "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" file.txt

# Telefonnummer
grep -E "\b[0-9]{3}[-.]?[0-9]{3}[-.]?[0-9]{4}\b" file.txt

# URL
grep -E "https?://[a-zA-Z0-9./?=_-]+" file.txt
```

## Kombinera verktyg: Praktiska pipelines

### Loganalys

```bash
# Räkna unika IP-adresser
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Hitta 404-fel
grep " 404 " access.log | awk '{print $7}' | sort | uniq -c | sort -rn

# Fel per timme
grep "ERROR" app.log | cut -d' ' -f1-2 | cut -d: -f1-2 | uniq -c
```

### Systemadministration

```bash
# Diskutrymme per användare
du -sh /home/* 2>/dev/null | sort -rh | head -10

# Minnesanvändning per process
ps aux | awk '{print $4, $11}' | sort -rn | head -10

# Visa aktiva anslutningar
netstat -an | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn
```

### Textbearbetning

```bash
# CSV till TSV
cat file.csv | tr ',' '\t'

# Ta bort tomma rader
grep -v '^$' file.txt
# eller
sed '/^$/d' file.txt

# Extrahera unika ord
cat file.txt | tr -s ' ' '\n' | sort | uniq
```

## Viktiga takeaways

- **Redirection**: > (överskriver), >> (appendra), 2> (stderr), &> (båda)
- **Pipe**: | kopplar stdout → stdin
- **grep**: Sök mönster; -i (case), -r (rekursiv), -v (invertera)
- **cut**: Extrahera kolumner; -d (delimiter), -f (field)
- **sed**: Stream editor; s/old/new/g, -i (in-place)
- **awk**: Pattern processing; $1-$n (fält), NF (antal), NR (radnr)
- **sort**: Sortera; -n (numerisk), -r (omvänd), -k (kolumn)
- **uniq**: Unika rader; -c (räkna), -d (duplicates)
- **wc**: Räkna; -l (rader), -w (ord), -c (bytes)
- **tr**: Translate; 'a-z' 'A-Z', -d (delete), -s (squeeze)
- **head/tail**: Visa del av fil; tail -f (follow)
- **tee**: Skriv till fil OCH stdout
- **Regex**: ^ (start), $ (slut), . (any), * (0+), [] (class)
- **Pipeline power**: Kombinera verktyg för komplexa uppgifter
