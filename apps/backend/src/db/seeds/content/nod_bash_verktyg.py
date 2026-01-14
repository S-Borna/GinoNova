"""
NOD: Kraftfulla kommandoradsverktyg i Bash
==========================================
Bemästra omdirigering, pipes och avancerade textbearbetningsverktyg för effektiv Linux-administration
"""

BASH_VERKTYG_NODE = {
    "title": "Kraftfulla kommandoradsverktyg i Bash",
    "slug": "bash-verktyg",
    "description": "Bemästra omdirigering, pipes och avancerade textbearbetningsverktyg för effektiv Linux-administration",
    "difficulty": "medium",
    "estimated_minutes": 75,
    "xp_reward": 150,
    "order_index": 7,
    "content": r"""# Kraftfulla kommandoradsverktyg i Bash

Tematiskt fokus: Omdirigering, pipes och textmanipulering

## Omdirigering: >, >>, 2>, &>

Omdirigering kontrollerar vart output skickas.

### Standardströmmar

```bash
# stdin  (0) - Standardingång (tangentbord)
# stdout (1) - Standardutgång (skärm)
# stderr (2) - Standardfel (skärm, men separat kanal)
```

### Utdata-omdirigering

```bash
# > skriver över filens innehåll
echo "hello" > file.txt

# >> lägger till i slutet av filen
echo "world" >> file.txt

# Skapa tom fil
> file.txt
```

### Felmeddelanden-omdirigering

```bash
# 2> dirigerar felmeddelanden till fil
ls /nonexistent 2> errors.txt

# 2>> lägger till felmeddelanden
ls /nonexistent 2>> errors.txt

# Kasta bort felmeddelanden
ls /nonexistent 2> /dev/null
```

### Kombinera utdata och felmeddelanden

```bash
# &> eller >& dirigerar BÅDE utdata och fel till fil
command &> output.txt

# Alternativ, mer tydlig syntax
command > output.txt 2>&1
# Tolkning: > output.txt dirigerar stdout till fil
#            2>&1 dirigerar stderr till samma destination som stdout

# Separera stdout och stderr till olika filer
command > stdout.txt 2> stderr.txt

# Lägg till båda
command >> output.txt 2>&1
```

### Indata-omdirigering

```bash
# < hämtar innehåll från fil
sort < unsorted.txt

# << here document
cat << EOF
Line 1
Line 2
EOF

# <<< here string
grep "hello" <<< "hello world"
```

### Praktiska tillämpningar

```bash
# Spara allt (inkl. fel) till fil
./script.sh &> script.log

# Visa output men logga också
./script.sh 2>&1 | tee script.log

# Dölj all output
./script.sh &> /dev/null

# Dirigera stderr till stdout (för att pipa)
ls /nonexistent 2>&1 | grep "No such"
```

## Pipes: Kedja samman kommandon

Pipes (`|`) dirigerar stdout från ett kommando till stdin för nästa.

```bash
# Grundläggande pipe
cat file.txt | grep "pattern"

# Kedja ihop flera kommandon
cat file.txt | grep "pattern" | sort | uniq

# Praktiska tillämpningar
ps aux | grep nginx           # Lokalisera nginx-processer
history | grep "git"          # Lokalisera git-kommandon
ls -la | wc -l                # Räkna filer
cat log.txt | tail -100       # Sista 100 raderna
```

### Pipelines och statuskoder

```bash
# Utan pipefail: statuskod = sista kommandots statuskod
false | true
echo $?  # 0 (true lyckades)

# Med set -o pipefail: första misslyckandet avgör
set -o pipefail
false | true
echo $?  # 1 (false misslyckades)
```

### Pipe till flera destinationer med tee

```bash
# tee skriver till fil OCH stdout
command | tee output.txt | next_command

# Flera destinationer
command | tee file1.txt file2.txt

# Lägg till istället för överskriva
command | tee -a log.txt
```

### Process substitution

```bash
# <() genererar en temporär fil med output
diff <(ls dir1) <(ls dir2)

# Jämför output från två kommandon
diff <(sort file1.txt) <(sort file2.txt)

# Använd output som fil
while read line; do
    echo "$line"
done < <(ls -la)
```

## grep: Mönstermatchning i text

grep söker efter textmönster i filer eller input.

### Grundläggande grep

```bash
# Sök i fil
grep "pattern" file.txt

# Sök i flera filer
grep "pattern" *.txt

# Rekursiv sökning
grep -r "pattern" /path/to/dir

# Skiftlägesokänslig sökning
grep -i "pattern" file.txt
```

### Vanliga grep-alternativ

```bash
-i    # Skiftlägesokänslig
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
-C N  # Visa N rader före och efter (kontext)
-E    # Utökad regex (egrep)
-o    # Visa bara matchande del
-q    # Tyst läge (exit 0 om match, exit 1 annars)
```

### Praktiska grep-tillämpningar

```bash
# Lokalisera alla IP-adresser
grep -E "\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b" file.txt

# Visa rader utan kommentarer
grep -v "^#" config.file

# Lokalisera filer som innehåller "TODO"
grep -r -l "TODO" src/

# Räkna fel i logg
grep -c "ERROR" /var/log/syslog

# Sök med kontext
grep -C 3 "error" log.txt

# Test om mönster finns (i script)
if grep -q "pattern" file.txt; then
    echo "Found!"
fi
```

### egrep (utökad regex)

```bash
# egrep = grep -E
egrep "pattern1|pattern2" file.txt    # OR
egrep "word+" file.txt                # + utan escape
egrep "(group){2,}" file.txt          # Gruppering
```

## cut: Extrahera kolumner

cut extraherar delar av varje rad.

### Avgränsare och fält

```bash
# -d avgränsare (default: tab)
# -f fält

# Extrahera första fältet (kolon-separerat)
cut -d: -f1 /etc/passwd

# Flera fält
cut -d: -f1,3 /etc/passwd        # Fält 1 och 3
cut -d: -f1-3 /etc/passwd        # Fält 1 till 3
cut -d, -f2- file.csv            # Fält 2 till slutet

# Med mellanslag som avgränsare
cut -d' ' -f2 file.txt
```

### Teckenpositioner

```bash
# -c teckenposition(er)
cut -c1-10 file.txt              # Första 10 tecknen
cut -c5- file.txt                # Tecken 5 till slutet
cut -c-5 file.txt                # Första 5 tecknen
```

### Praktiska cut-tillämpningar

```bash
# Användare från passwd
cut -d: -f1 /etc/passwd

# UID från passwd
cut -d: -f3 /etc/passwd

# Kombinera med pipes
cat /etc/passwd | cut -d: -f1,6 | head -5
```

## sed: Strömredigerare

sed är en kraftfull strömredigerare för texttransformationer.

### Grundläggande ersättning

```bash
# s/old/new/ - ersätt första förekomsten per rad
sed 's/old/new/' file.txt

# s/old/new/g - ersätt ALLA förekomster per rad
sed 's/old/new/g' file.txt

# Skiftlägesokänslig
sed 's/old/new/gi' file.txt
```

### Redigera filen direkt

```bash
# -i redigerar filen på plats
sed -i 's/old/new/g' file.txt

# Med säkerhetskopia (rekommenderat!)
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
# Radera rader
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

### Praktiska sed-tillämpningar

```bash
# Radera trailing whitespace
sed 's/[[:space:]]*$//' file.txt

# Ersätt Windows line endings
sed 's/\r$//' file.txt

# Omge mönster med citationstecken
sed 's/[^ ]*/\"&\"/' file.txt

# Flera operationer
sed -e 's/foo/bar/g' -e 's/baz/qux/g' file.txt
```

## awk: Mönsterigenkänning och bearbetning

awk är ett komplett programmeringsspråk för textbearbetning.

### Grundläggande awk

```bash
# Syntax: awk 'pattern { action }' file

# Visa specifika kolumner (default: mellanslag/tab-separerat)
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
FS    # Fältavgränsare (default: whitespace)
OFS   # Utmatningsfältavgränsare
RS    # Postavgränsare (default: newline)
```

### Fältavgränsare

```bash
# -F sätter avgränsare
awk -F: '{print $1}' /etc/passwd         # Kolon
awk -F',' '{print $2}' file.csv          # Komma
awk -F'\t' '{print $1}' file.tsv         # Tab

# Inom awk
awk 'BEGIN{FS=":"} {print $1}' /etc/passwd
```

### Mönstermatchning

```bash
# Villkor
awk '/pattern/ {print}' file.txt         # Rader med pattern
awk '$3 > 100 {print $1, $3}' file.txt   # Kolumn 3 > 100
awk 'NR > 1 {print}' file.txt            # Hoppa över header
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

### Praktiska awk-tillämpningar

```bash
# Summera diskutrymme
df -h | awk 'NR>1 {print $5, $6}'

# Lokalisera stora processer
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

# Skiftlägesokänslig
sort -f file.txt

# Humanläsbar storlek (1K, 2M, 3G)
sort -h sizes.txt
```

### Kombinera med uniq

```bash
# uniq kräver sorterad input
sort file.txt | uniq             # Radera dubletter
sort file.txt | uniq -c          # Räkna förekomster
sort file.txt | uniq -d          # Visa endast dubletter
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

## tr: Översätt/radera tecken

```bash
# Översätt tecken
echo "hello" | tr 'a-z' 'A-Z'    # Versaler: HELLO
echo "HELLO" | tr 'A-Z' 'a-z'    # Gemener: hello

# Radera tecken
echo "hello123" | tr -d '0-9'    # hello

# Komprimera repeterade tecken
echo "heeello" | tr -s 'e'       # helo

# Komplement (allt UTOM)
echo "hello123" | tr -cd '0-9'   # 123

# Ersätt radbrytningar med mellanslag
cat file.txt | tr '\n' ' '

# Radera carriage returns (Windows → Unix)
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

# Följ (live loggövervakning)
tail -f /var/log/syslog
tail -F /var/log/syslog          # Följ även om fil roteras
```

## Regex Basics: Reguljära uttryck

### Grundläggande mönster

```bash
.        # Valfritt tecken
*        # 0 eller fler av föregående
+        # 1 eller fler (utökad regex)
?        # 0 eller 1 av föregående (utökad)
^        # Start av rad
$        # Slut av rad
[]       # Teckenklass
[^]      # Negerad teckenklass
\        # Escape specialtecken
```

### Teckenklasser

```bash
[abc]    # a, b eller c
[a-z]    # a till z
[0-9]    # Siffror
[^0-9]   # Allt UTOM siffror
[A-Za-z] # Alla bokstäver
```

### POSIX-teckenklasser

```bash
[[:alpha:]]  # Bokstäver
[[:digit:]]  # Siffror (0-9)
[[:alnum:]]  # Bokstäver och siffror
[[:space:]]  # Whitespace
[[:lower:]]  # Gemener
[[:upper:]]  # Versaler
```

### Utökad regex (ERE)

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

### Praktiska regex-tillämpningar

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

### Logganalys

```bash
# Räkna unika IP-adresser
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Lokalisera 404-fel
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

# Radera tomma rader
grep -v '^$' file.txt
# eller
sed '/^$/d' file.txt

# Extrahera unika ord
cat file.txt | tr -s ' ' '\n' | sort | uniq
```

## xargs: Konstruera och kör kommandon från stdin

xargs hämtar input från stdin och använder det som argument till ett kommando.

### Grundläggande xargs

```bash
# Enkel användning
echo "file1.txt file2.txt file3.txt" | xargs rm
# rm file1.txt file2.txt file3.txt

# Lista filer och radera dem
find /tmp -name "*.log" | xargs rm

# Med bekräftelse (-p)
find /tmp -name "*.log" | xargs -p rm
# Frågar innan varje kommando körs
```

### xargs med -I (ersättningssträng)

```bash
# -I {} ersätter {} med input
find . -name "*.txt" | xargs -I {} cp {} /backup/
# Kopierar varje .txt-fil till /backup/

# Flera operationer på samma input
cat files.txt | xargs -I {} sh -c 'echo "Processing {}"; cp {} /backup/'

# Skapa kataloger från lista
cat dirlist.txt | xargs -I {} mkdir -p /data/{}
```

### xargs med -n (antal argument per kommando)

```bash
# -n 1: Kör kommando för varje input (en åt gången)
echo "a b c d" | xargs -n 1 echo
# echo a
# echo b
# echo c
# echo d

# -n 2: Två argument åt gången
echo "a b c d" | xargs -n 2 echo
# echo a b
# echo c d
```

### xargs med -P (parallell exekvering)

```bash
# -P 4: Kör 4 processer parallellt
find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png

# Snabbare komprimering av många filer
find /data -name "*.log" | xargs -P 8 gzip
```

### xargs med -0 (null-terminerad)

Används med find -print0 för att hantera filer med mellanslag i namnet.

```bash
# PROBLEM: Filer med mellanslag bryts
find . -name "*.txt" | xargs rm
# Fungerar INTE om filnamn innehåller mellanslag

# LÖSNING: Använd -print0 och -0
find . -name "*.txt" -print0 | xargs -0 rm
# -print0: null-separerade filnamn
# -0: läs null-separerad input
```

### xargs med -t (utförlig/spårning)

```bash
# Visa kommandot innan det körs
echo "file1 file2" | xargs -t rm
# rm file1 file2
# (kör sedan kommandot)
```

### Praktiska xargs-tillämpningar

```bash
# Radera gamla filer (äldre än 30 dagar)
find /tmp -type f -mtime +30 -print0 | xargs -0 rm

# Ändra rättigheter på alla scripts
find /usr/local/bin -name "*.sh" -print0 | xargs -0 chmod +x

# Sök i flera filer parallellt
find . -name "*.log" -print0 | xargs -0 -P 4 grep -H "ERROR"

# Konvertera alla bilder (parallellt)
ls *.jpg | xargs -P 8 -I {} convert {} -resize 800x600 small-{}

# Backup av filer med rsync
find /data -name "*.db" -print0 | xargs -0 -I {} rsync -avz {} backup:/backups/

# Räkna rader i alla filer
find . -name "*.py" | xargs wc -l

# Konstruera kommandon med flera argument
cat users.txt | xargs -I {} useradd -m {}
```

### xargs vs while read loop

```bash
# xargs: Snabbare, men svårare med komplexa operationer
find . -name "*.txt" | xargs rm

# while read: Mer kontroll, enklare för komplexa script
find . -name "*.txt" | while read file; do
    echo "Processing $file"
    rm "$file"
done
```

**När använda xargs**:
- Enkla operationer på många filer
- När parallellisering är önskvärt (-P)
- När prestanda är kritiskt

**När använda while read**:
- Komplexa operationer per fil
- Behöver flera kommandon per input
- Behöver variabler och if-satser

## Viktiga lärdomar

- **Omdirigering**: > (överskriver), >> (lägger till), 2> (stderr), &> (båda)
- **Pipe**: | kopplar stdout → stdin
- **grep**: Sök mönster; -i (skiftläge), -r (rekursiv), -v (invertera)
- **cut**: Extrahera kolumner; -d (avgränsare), -f (fält)
- **sed**: Strömredigerare; s/old/new/g, -i (på plats)
- **awk**: Mönsterbearbetning; $1-$n (fält), NF (antal), NR (radnr)
- **sort**: Sortera; -n (numerisk), -r (omvänd), -k (kolumn)
- **uniq**: Unika rader; -c (räkna), -d (dubletter)
- **wc**: Räkna; -l (rader), -w (ord), -c (bytes)
- **tr**: Översätt; 'a-z' 'A-Z', -d (radera), -s (komprimera)
- **head/tail**: Visa del av fil; tail -f (följ)
- **tee**: Skriv till fil OCH stdout
- **xargs**: Konstruera kommandon från stdin; -I {} (ersättning), -n (antal), -P (parallellt), -0 (null-terminerad)
- **Regex**: ^ (start), $ (slut), . (valfri), * (0+), [] (klass)
- **Pipeline-kraft**: Kombinera verktyg för komplexa uppgifter

"""
}
