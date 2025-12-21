# =============================================================================
# BASH MASTERY V3 - BLOCK 1 PART 2: GLOBBING & QUOTING
# Noder 3-4 av 20 | Premium Bootcamp-kvalitet
# =============================================================================

NODE_3 = {
    "id": "bash_node_3",
    "title": "Globbing & Pattern Matching",
    "slug": "globbing-pattern-matching",
    "order_index": 3,
    "estimated_minutes": 45,
    "xp_reward": 100,
    "difficulty": "easy",
    "content": r'''# Globbing & Pattern Matching

------------------------------------------------------------

Globbing ar Bashs satt att matcha filnamn med mönster. Att beharska wildcards och pattern matching gor dig snabbare och mer precis i terminalen.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Globbing ar viktigt |
|----------|---------------------------|
| **Batch-operationer** | Hantera hundratals filer med ett kommando |
| **Logghantering** | Filtrera loggar baserat pa datum/typ |
| **Deployment** | Kopiera specifika filer till servrar |
| **Cleanup** | Ta bort temporara filer sakert |
| **Backup** | Inkludera/exkludera filer baserat pa monster |

Du maste forsta:

- **Wildcards expanderas av shellen** - Inte av kommandot
- **Ingen match = literal string** - Om inget matchar, behalles monstret
- **Dolda filer** - Kraver explicit hantering

------------------------------------------------------------

## Grundlaggande Wildcards

```
+-------------------------------------------------------------------------+
|                      WILDCARDS SNABBREFERENS                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  WILDCARD | MATCHAR                    | EXEMPEL                        |
|  ---------+----------------------------+--------------------------------|
|  *        | Noll eller flera tecken    | *.txt -> alla .txt-filer       |
|  ?        | Exakt ett tecken           | file?.txt -> file1.txt         |
|  [...]    | Ett tecken fran set        | file[123].txt -> file1.txt     |
|  [!...]   | Ett tecken INTE i set      | file[!0-9].txt -> filea.txt    |
|  [a-z]    | Range av tecken            | [a-z]*.sh -> alla .sh a-z      |
|  {a,b,c}  | Alternativ (brace exp)     | file.{txt,log} -> bada filer   |
|                                                                          |
|  EXEMPEL:                                                                |
|  ls *.log                    # Alla .log-filer                          |
|  rm file?.txt                # file1.txt, file2.txt, etc               |
|  cp config.[ch] backup/      # config.c och config.h                    |
|  mv report_{jan,feb,mar}.pdf archive/  # Tre specifika filer           |
|                                                                          |
+-------------------------------------------------------------------------+
```

| Wildcard | Beskrivning | Matchar | Matchar inte |
|----------|-------------|---------|--------------|
| `*` | Allt | `file.txt`, `a`, `` | (matchar allt) |
| `?` | Ett tecken | `a`, `1`, `.` | `ab`, `` |
| `[abc]` | a, b eller c | `a`, `b`, `c` | `d`, `ab` |
| `[a-z]` | a till z | `a`, `m`, `z` | `A`, `1` |
| `[!abc]` | Inte a, b, c | `d`, `1`, `z` | `a`, `b`, `c` |
| `[^abc]` | Samma som [!abc] | `d`, `1` | `a`, `b` |

```bash
# Praktiska exempel
ls *.txt                         # Alla textfiler
ls file[0-9].log                 # file0.log till file9.log
ls log[!0-9]*                    # Loggar som EJ borjar med siffra
rm *.{tmp,bak,swp}               # Ta bort temp, backup, swap
cp *.{jpg,png,gif} images/       # Kopiera alla bilder

# Rekursiv matching med **
shopt -s globstar                # Aktivera globstar
ls **/*.py                       # Alla Python-filer rekursivt
```

------------------------------------------------------------

## Brace Expansion

```
+-------------------------------------------------------------------------+
|                      BRACE EXPANSION                                     |
+-------------------------------------------------------------------------+
|                                                                          |
|  Brace expansion sker FORE glob expansion!                              |
|  Skapar multipla strings fran ett monster.                              |
|                                                                          |
|  SYNTAX          | RESULTAT                                             |
|  ----------------+----------------------------------------------------- |
|  {a,b,c}         | a b c                                                |
|  {1..5}          | 1 2 3 4 5                                            |
|  {a..z}          | a b c ... z                                          |
|  {01..10}        | 01 02 03 ... 10 (med padding)                        |
|  {1..10..2}      | 1 3 5 7 9 (steg 2)                                   |
|  pre{a,b}post    | preapost prebpost                                    |
|                                                                          |
+-------------------------------------------------------------------------+
```

```bash
# Skapa multipla kataloger
mkdir -p project/{src,bin,lib,doc,test}

# Skapa numrerade filer
touch file{1..10}.txt            # file1.txt till file10.txt
touch log_{01..12}.txt           # Med nollpadding

# Backup med tidstampel
cp config.yml{,.backup}          # config.yml och config.yml.backup
# Motsvarar: cp config.yml config.yml.backup

# Kombinera med range
echo {A..Z}{0..9}                 # A0 A1 ... Z9 (260 kombinationer)

# Praktisk DevOps-anvandning
mkdir -p /var/log/app/{error,access,debug}/{2024..2025}/{01..12}

# Skapa testmiljoer
for env in {dev,staging,prod}; do
    mkdir -p config/$env
    touch config/$env/{app,db,cache}.conf
done
```

------------------------------------------------------------

## Extended Globbing

```bash
# Aktivera extended globbing
shopt -s extglob

# Extended glob patterns
# ?(pattern)  - Matchar noll eller en gang
# *(pattern)  - Matchar noll eller flera ganger
# +(pattern)  - Matchar en eller flera ganger
# @(pattern)  - Matchar exakt en gang
# !(pattern)  - Matchar allt UTOM

# Exempel
ls *.!(bak|tmp)                  # Alla utom .bak och .tmp
rm !(important)*.txt             # Alla .txt utom important*.txt
ls @(*.jpg|*.png|*.gif)          # Bilder med specifika format

# Ta bort allt utom vissa filer
rm !(keep_this|and_this).txt

# Matcha filer med viss struktur
ls +([0-9]).log                  # Filer som 123.log, 1.log
```

------------------------------------------------------------

## Dolda Filer (Dotfiles)

```bash
# Standard glob INKLUDERAR INTE dolda filer
ls *                             # Visar EJ .bashrc, .git, etc

# Visa dolda filer explicit
ls .*                            # Alla dolda filer
ls .??*                          # Dolda filer (undvik . och ..)
ls -d .[!.]*                     # Battre satt (exkluderar . och ..)

# Inkludera dolda filer i glob
shopt -s dotglob                 # Nu matchar * aven dolda filer
ls *                             # Inkluderar nu .bashrc etc
shopt -u dotglob                 # Stang av

# Praktiskt: Kopiera alla inklusive dolda
cp -r source/. destination/      # Allt inklusive dolda
# Eller
shopt -s dotglob
cp -r source/* destination/
shopt -u dotglob
```

------------------------------------------------------------

## Nullglob och Failglob

```bash
# Problem: Om glob inte matchar
ls *.xyz                         # Om inga .xyz finns
# Output: ls: cannot access '*.xyz': No such file or directory

# Losning 1: nullglob - returnera tom lista
shopt -s nullglob
files=(*.xyz)                    # Tom array om ingen match
echo "${#files[@]} files found"  # 0 files found
shopt -u nullglob

# Losning 2: failglob - ge felmeddelande
shopt -s failglob
ls *.xyz                         # Bash-fel om ingen match
# bash: no match: *.xyz
shopt -u failglob

# Praktisk anvandning i skript
shopt -s nullglob
for file in *.log; do
    [ -f "$file" ] || continue   # Extra sakerhet
    process "$file"
done
shopt -u nullglob
```

------------------------------------------------------------

## Snabbreferens

| Pattern | Beskrivning |
|---------|-------------|
| `*` | Noll eller flera tecken |
| `?` | Exakt ett tecken |
| `[abc]` | Ett av tecknen a, b, c |
| `[a-z]` | Range a till z |
| `[!abc]` | Inte a, b, c |
| `{a,b}` | Expansion till a och b |
| `**` | Rekursiv (med globstar) |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `No such file` | Glob matchade inget | Anvand nullglob |
| Dolda filer missas | * matchar ej dotfiles | Anvand dotglob eller .* |
| Ovaentad expansion | Spaces i filnamn | Quoting (se nasta nod) |
| Pattern literal | Ingen match | Kontrollera shopt-installningar |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Shellen expanderar** | Glob hanteras av bash, ej kommandot |
| **Brace fore glob** | {a,b} expanderas innan * |
| **Dolda filer speciella** | Kraver dotglob eller explicit .* |
| **extglob** | Avancerade monster med shopt |
| **nullglob** | Returnera tom lista vid ingen match |

**Kom ihag:**

- Testa glob med echo forst: `echo *.txt`
- Anvand nullglob i skript for sakerhet
- Brace expansion ar for att skapa strings, ej matcha filer
- Extended glob ger regex-liknande kraft
''',
}

NODE_4 = {
    "id": "bash_node_4",
    "title": "Quoting & Escaping - Protect Your Data",
    "slug": "quoting-escaping-protect-your-data",
    "order_index": 4,
    "estimated_minutes": 45,
    "xp_reward": 100,
    "difficulty": "medium",
    "content": r'''# Quoting & Escaping - Protect Your Data

------------------------------------------------------------

Quoting ar en av de viktigaste och mest missforstadda delarna av Bash. Fel quoting leder till buggar, sakerhetshal och ovaentat beteende. Denna nod gor dig till en quoting-expert.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Quoting ar kritiskt |
|----------|---------------------------|
| **Filnamn med spaces** | `rm My File.txt` tar bort TVA filer! |
| **Sakerhet** | Command injection genom dålig quoting |
| **JSON/YAML** | Hantera specialtecken i konfigurationer |
| **SSH-kommandon** | Variabler maste expanderas ratt |
| **Docker** | ENV-variabler och CMD kräver precision |

Du maste forsta:

- **Quoting ar inte optional** - Det ar kravs for sakerhet
- **Tre typer** - Single, double, och escape har olika beteende
- **Ordning spelar roll** - Shellen processar i specifik ordning

------------------------------------------------------------

## De Tre Quoting-typerna

```
+-------------------------------------------------------------------------+
|                        QUOTING JAMFORELSE                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  TYP             | SYNTAX    | EXPANDERAR        | EXEMPEL              |
|  ----------------+-----------+-------------------+--------------------- |
|  Single quotes   | 'text'    | INGET             | '$HOME' -> $HOME      |
|  Double quotes   | "text"    | $, `, \, !, "     | "$HOME" -> /home/user|
|  Backslash       | \x        | Nastaende tecken  | \$ -> $               |
|  $'...'          | $'text'   | Escape sequences  | $'\n' -> newline      |
|                                                                          |
|  MINNESREGEL:                                                           |
|  'Single' = LITERAL (exakt som skrivet)                                 |
|  "Double" = SMART (variabler expanderas)                                |
|  \Escape  = SKIPPA nasta tecken                                         |
|                                                                          |
+-------------------------------------------------------------------------+
```

------------------------------------------------------------

## Single Quotes - Literal Text

```bash
# Single quotes bevarar ALLT som literal text
echo 'Hello $USER'              # Output: Hello $USER
echo 'Today is $(date)'         # Output: Today is $(date)
echo 'Path: $PATH'              # Output: Path: $PATH
echo 'Backslash: \'             # FEL! Kan ej escapa inom single

# Problem: Kan ej inkludera single quote
echo 'It's a problem'           # SYNTAX ERROR!

# Losning 1: Avsluta, escapa, fortsatt
echo 'It'\''s working'          # Output: It's working

# Losning 2: Anvand $'...' syntax
echo $'It\'s working'           # Output: It's working

# Losning 3: Byt till double quotes
echo "It's working"             # Output: It's working

# Praktisk anvandning
grep 'error.*failed' logfile    # Regex med specialtecken
ssh server 'ps aux | grep nginx' # Kommando ska koras pa server
awk '{print $1}'                 # Awk-skript
```

------------------------------------------------------------

## Double Quotes - Smart Expansion

```bash
# Double quotes expanderar variabler och kommandon
echo "Hello $USER"              # Output: Hello johndoe
echo "Today is $(date +%A)"     # Output: Today is Monday
echo "Home: $HOME"              # Output: Home: /home/johndoe

# Bevarar whitespace
filename="my important file.txt"
cat "$filename"                 # Korrekt! En fil
cat $filename                   # FEL! Tre separata argument

# Specialtecken som expanderas i double quotes:
# $    - Variable expansion
# `    - Command substitution (gammalt satt)
# \    - Escape (bara fore $ ` " \ newline)
# !    - History expansion (interaktivt)

# Escape inom double quotes
echo "Price: \$100"             # Output: Price: $100
echo "Quote: \"text\""          # Output: Quote: "text"
echo "Path: $PATH"              # Expanderas
echo "Literal: \$PATH"          # Output: Literal: $PATH

# Praktisk anvandning
message="Deployment to $ENV completed at $(date)"
echo "$message" >> deploy.log

# JSON med variabler
cat << EOF
{
    "hostname": "$HOSTNAME",
    "user": "$USER",
    "timestamp": "$(date -Iseconds)"
}
EOF
```

------------------------------------------------------------

## $'...' - ANSI-C Quoting

```bash
# $'...' tillater escape sequences
echo $'Line 1\nLine 2'          # Två rader
echo $'Tab:\tHere'              # Tab-tecken
echo $'Alert:\a'                # Bell/alert

# Escape sequences i $'...'
# \n    Newline
# \t    Tab
# \r    Carriage return
# \\    Backslash
# \'    Single quote
# \"    Double quote
# \xHH  Hex value
# \uHHHH Unicode

# Praktiska exempel
PS1=$'\\u@\\h:\\w\\$ '          # Prompt med special-tecken
separator=$'\n---\n'             # Separator med newlines
echo "Data:${separator}More data"

# Skapa fil med special-namn (for testning)
touch $'file\twith\ttabs'
touch $'file\nwith\nnewlines'   # Ja, det gar!
```

------------------------------------------------------------

## Escaping med Backslash

```bash
# Backslash escapar enskilda tecken
echo \$HOME                     # Output: $HOME
echo \"quoted\"                 # Output: "quoted"
echo \\backslash\\              # Output: \backslash\

# Line continuation
echo "This is a very long \
command that spans \
multiple lines"

# Praktisk: Langa kommandon
docker run \
    --name mycontainer \
    --rm \
    -v /host/path:/container/path \
    -e ENV_VAR=value \
    nginx:latest

# Escape i olika kontexter
filename="file with spaces.txt"
ls file\ with\ spaces.txt       # Escapa varje space
ls "file with spaces.txt"       # Battre: anvand quotes
ls "$filename"                  # Bast: variabel med quotes
```

------------------------------------------------------------

## Nestlade Quotes

```
+-------------------------------------------------------------------------+
|                      NESTLADE QUOTES STRATEGIER                          |
+-------------------------------------------------------------------------+
|                                                                          |
|  SCENARIO                    | LOSNING                                  |
|  ----------------------------+---------------------------------------- |
|  Double inom single          | 'say "hello"'    -> say "hello"          |
|  Single inom double          | "it's fine"      -> it's fine            |
|  Double inom double          | "say \"hi\""     -> say "hi"             |
|  Single inom single          | 'it'\''s'        -> it's                 |
|  Command i double            | "date: $(date)"  -> expanderas           |
|  Command i single            | 'date: $(date)'  -> literal              |
|                                                                          |
+-------------------------------------------------------------------------+
```

```bash
# SSH med lokala och remote variabler
# Fel: Bada expanderas lokalt
ssh server "echo $LOCAL_VAR $REMOTE_VAR"

# Ratt: Mixa quoting
ssh server "echo $LOCAL_VAR "'$REMOTE_VAR'
# Eller
ssh server "echo $LOCAL_VAR \$REMOTE_VAR"

# Komplex nestling
alias ll='ls -la'                    # Single quotes, literal
alias greeting="echo 'Hello $USER'"  # Double, expanderar $USER
alias timestamp='echo "Time: $(date)"' # Funkar, $() i single

# JSON med bade quotes
json='{"name": "'"$USER"'", "home": "'"$HOME"'"}'
# Resultat: {"name": "johndoe", "home": "/home/johndoe"}

# Enklare med printf
printf '{"name": "%s", "home": "%s"}\n' "$USER" "$HOME"
```

------------------------------------------------------------

## Praktiska Exempel

```bash
# Hantera filnamn sakert
for file in *; do
    echo "Processing: $file"     # Quotes! Hanterar spaces
done

# Find med exec
find . -name "*.txt" -exec grep "pattern" {} \;

# Xargs med quotes
find . -name "*.log" -print0 | xargs -0 rm

# Docker environment
docker run -e "DATABASE_URL=$DB_URL" myimage

# Curl med JSON
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"user": "'"$USER"'", "action": "deploy"}' \
    https://api.example.com/webhook

# Eval (farligt men ibland nodvandigt)
cmd='echo "Hello World"'
eval "$cmd"                      # Med quotes for sakerhet
```

------------------------------------------------------------

## Snabbreferens

| Typ | Expanderar | Anvandning |
|-----|------------|------------|
| `'...'` | Inget | Literal text, regex, awk |
| `"..."` | $, `, \ | Variabler, kommandon |
| `\` | Nasta tecken | Enskilda specialtecken |
| `$'...'` | Escape seq | \n, \t, unicode |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `unexpected EOF` | Obalanserade quotes | Rakna quotes, anvand editor |
| Word splitting | Okvoterad variabel | Alltid "$var" |
| Glob expansion | Okvoterad * eller ? | Anvand quotes |
| `command not found` | Space i kommando | Kontrollera quoting |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **"$var" alltid** | Skydda mot word splitting och glob |
| **Single = literal** | Ingenting expanderas |
| **Double = smart** | Variabler och kommandon expanderas |
| **$'...'** | For escape sequences |
| **Testa med echo** | `echo "$var"` fore rm/mv/etc |

**Kom ihag:**

- ALLTID quota variabler: "$var", inte $var
- Oquoterade variabler ar #1 orsak till skript-buggar
- Anvand shellcheck for att hitta quoting-problem
- Vid tveksamhet: quotera mer, inte mindre
''',
}

BLOCK_1_PART_2_NODES = [NODE_3, NODE_4]
