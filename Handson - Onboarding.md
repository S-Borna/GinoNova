# Linux Hands-On: Filsystem & Texteditorer

## Sammanfattning för Tenta

---

## 📋 Innehållsförteckning

1. [Navigering i Filsystemet](#navigering-i-filsystemet)
2. [Filhantering](#filhantering)
3. [Läsa & Söka](#läsa--söka)
4. [Dokumentation](#dokumentation)
5. [Texteditorer](#texteditorer)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Cheat Sheet](#cheat-sheet)

---

## 🗂️ Navigering i Filsystemet

### Grundkommandon

**`pwd`** - Print Working Directory

- Visar din nuvarande position i filsystemet
- Exempel: `/home/username`

**`cd`** - Change Directory

```bash
cd /home/username    # Absolut path (börjar med /)
cd Documents         # Relativ path (från nuvarande position)
cd ..               # Upp en nivå
cd ~                # Till hemmamapp (samma som cd utan argument)
cd                  # Till hemmamapp
cd -                # Till föregående directory
```

**`ls`** - List directory contents

```bash
ls                  # Lista filer i nuvarande mapp
ls /home           # Lista filer i specifik mapp
ls -l              # Long listing format (detaljerad info)
ls -a              # Visa dolda filer (börjar med .)
ls -t              # Sortera efter tid (nyast först)
ls -la             # Kombination av flaggor
ls -lta            # Alla flaggor tillsammans
```

### 🎯 Viktiga Paths

| Path | Beskrivning |
|------|-------------|
| `/` | Root (roten av filsystemet) |
| `/home` | Användares hemmamappar |
| `/etc` | Konfigurationsfiler |
| `/var` | Loggar och varierande data |
| `/bin` | Viktiga program/kommandon |
| `/tmp` | Temporära filer |
| `~` | Din hemmamapp (shortcut) |
| `.` | Nuvarande mapp |
| `..` | Mapp en nivå upp |

---

## 📁 Filhantering

### Skapa & Ta Bort

**`touch`** - Skapa tom fil

```bash
touch myfile.txt
touch file1 file2 file3    # Skapa flera filer
```

**`mkdir`** - Make Directory

```bash
mkdir myfolder
mkdir -p parent/child/grandchild    # Skapa hela strukturer
```

**`rm`** - Remove (radera filer)

```bash
rm myfile.txt
rm -r myfolder              # Recursive (hela mappar)
rm -f myfile.txt            # Force (ingen prompt)
rm -rf myfolder             # Kombinera flaggor
```

⚠️ **VARNING**: `rm` har ingen ångra-funktion och ingen papperskorg!

**`rmdir`** - Remove Directory (endast tomma mappar)

```bash
rmdir emptyfolder
```

### Kopiera & Flytta

**`cp`** - Copy

```bash
cp source.txt destination.txt
cp file.txt backup.txt
cp -r folder1 folder2        # Kopiera mappar
```

**`mv`** - Move (även för att byta namn)

```bash
mv oldname.txt newname.txt   # Byt namn
mv file.txt /home/user/      # Flytta fil
mv folder1 folder2           # Flytta/byt namn på mapp
```

⚠️ **OBS**: `mv` överskriver filer utan varning!

---

## 🔍 Läsa & Söka

### Visa Filinnehåll

**`cat`** - Concatenate (visa hela filen)

```bash
cat myfile.txt
cat file1.txt file2.txt      # Visa flera filer
```

### Pagers (sidvy)

**`less`** - Moderna pager (rekommenderad)

```bash
less myfile.txt
ps aux | less                # Pipe output till less
```

Navigering i `less`:

- `j` / `↓` - Ner en rad
- `k` / `↑` - Upp en rad
- `Space` / `Page Down` - Ner en sida
- `Page Up` - Upp en sida
- `/sökterm` - Sök
- `n` - Nästa sökmatch
- `N` - Föregående sökmatch
- `q` - Avsluta

**`more`** - Äldre pager (begränsad)

- Kan bara scrolla nedåt
- `Space` eller `Enter` för nästa sida

> 💡 **Tips**: "Less does more than more" - använd `less`!

### Söka i Filsystemet

**`find`** - Sök efter filer och mappar

```bash
find                         # Lista allt i nuvarande mapp
find /home                   # Lista allt under /home
find -type f                 # Bara filer
find -type d                 # Bara mappar
find -name "*bash*"          # Sök efter namn med "bash"
```

---

## 📚 Dokumentation

### Man Pages (Manual Pages)

**`man`** - Visa manualsidor

```bash
man ls                       # Manual för ls
man rm                       # Manual för rm
man man                      # Manual för man (viktigt!)
```

#### Man Page Sektioner

| Sektion | Innehåll |
|---------|----------|
| 1 | Kommandon och program |
| 2 | System calls (C-funktioner) |
| 3 | Bibliotek |
| 5 | Filformat |
| 8 | Systemadministration |

Navigering i man pages:

- Samma som i `less` (j/k, space, /, n, q)
- `h` - Hjälp
- `q` - Avsluta

### Info Pages

**`info`** - Alternativ dokumentation

```bash
info info                    # Lär dig info-systemet
info ls                      # Info om ls
```

- Mer strukturerad än man pages
- Länkar mellan sektioner
- `Tab` - Nästa länk
- `Enter` - Följ länk
- `q` - Avsluta

---

## ✏️ Texteditorer

### Vim

**Starta Vim**

```bash
vim myfile.txt
vimtutor                     # Interaktiv tutorial (VIKTIGT!)
```

#### Vim Basics (från vimtutor)

**Lägen:**

- Normal mode (default) - för navigation och kommandon
- Insert mode - för att skriva text
- Command mode - för kommandon som spara/avsluta

**Grundläggande kommandon:**

```vim
i          # Insert mode (börja skriva)
Esc        # Tillbaka till Normal mode
:w         # Spara (write)
:q         # Avsluta (quit)
:wq        # Spara och avsluta
:q!        # Avsluta utan att spara
h j k l    # Vänster, ner, upp, höger (i Normal mode)
x          # Radera tecken
dd         # Radera rad
u          # Ångra (undo)
/sökterm   # Sök
n          # Nästa sökmatch
```

> 🎯 **Kom ihåg**: "How do I exit vim?" → `:q` eller `:q!`

**Vim Swap Files**

- Vim skapar `.swp` filer som backup
- Tas bort automatiskt när du avslutar korrekt
- Kvarstår om Vim kraschar

### Emacs (Frivilligt)

**Installation:**

```bash
# Ubuntu
sudo apt install emacs-nox

# Fedora
sudo dnf install emacs-nox
```

**Starta:**

```bash
emacs
```

Följ den inbyggda tutorialen (Emacs Tutorial) när du startar.

**Viktiga kortkommandon i Bash (Emacs-stil):**

- `Ctrl-A` - Början av rad
- `Ctrl-E` - Slutet av rad
- `Ctrl-K` - Radera resten av raden
- `Ctrl-L` - Rensa skärmen (samma som `clear`)

---

## 💡 Viktiga Koncept

### Absoluta vs Relativa Paths

**Absolut path** - Börjar med `/`

```bash
cd /home/username/Documents  # Fungerar var du än är
ls /etc
```

**Relativ path** - Börjar INTE med `/`

```bash
cd Documents                 # Från nuvarande position
ls ../other-folder          # Relativ till nuvarande
```

### Hidden Files

- Filer som börjar med `.` är "dolda"
- Visas inte med vanligt `ls`
- Använd `ls -a` för att se dem
- Exempel: `.bashrc`, `.viminfo`, `.bash_history`

### Tab Completion

- Tryck `Tab` för att autocomplete kommandon och filnamn
- Dubbel-`Tab` visar alla möjliga alternativ
- Sparar tid och minskar felstavningar!

```bash
cd Doc[TAB]      # Kompletterar till Documents/
ls myf[TAB]      # Kompletterar till myfile om unikt
```

### File Permissions & Ownership

När du kör `ls -l`:

```
drwxr-xr-x 2 username groupname 4096 Nov 13 10:30 Documents
-rw-r--r-- 1 username groupname   29 Nov 13 11:45 myfile.txt
```

- Första kolumnen: Permissions (d=directory, -=file)
- Tredje kolumnen: Ägare
- Femte kolumnen: Storlek (bytes)
- Sista kolumnerna: Datum och filnamn

### Farliga Kommandon ⚠️

```bash
rm -rf /                     # RADERA ALLT (kräver --no-preserve-root)
rm -rf /*                    # RADERA ALLT
rm -rf ~                     # RADERA HELA HEMMAMAP
mv file.txt existing.txt     # Överskriver utan varning
```

**Gyllene regel**: **Think before you type!**

---

## 📋 Cheat Sheet

### Snabbkommando

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `pwd` | Visa nuvarande mapp | `pwd` |
| `cd` | Byt mapp | `cd /home` |
| `ls` | Lista filer | `ls -la` |
| `touch` | Skapa tom fil | `touch file.txt` |
| `mkdir` | Skapa mapp | `mkdir folder` |
| `rm` | Ta bort | `rm file.txt` |
| `cp` | Kopiera | `cp a.txt b.txt` |
| `mv` | Flytta/byt namn | `mv old.txt new.txt` |
| `cat` | Visa fil | `cat file.txt` |
| `less` | Bläddra fil | `less file.txt` |
| `find` | Sök filer | `find -name "*.txt"` |
| `man` | Manual | `man ls` |
| `vim` | Öppna Vim | `vim file.txt` |

### Vim Snabbkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `i` | Insert mode |
| `Esc` | Normal mode |
| `:w` | Spara |
| `:q` | Avsluta |
| `:wq` | Spara och avsluta |
| `:q!` | Avsluta utan spara |
| `h j k l` | Vänster, ner, upp, höger |
| `dd` | Radera rad |
| `u` | Ångra |
| `/text` | Sök efter "text" |

### ls Flaggor

| Flagga | Beskrivning |
|--------|-------------|
| `-l` | Long format (detaljer) |
| `-a` | Visa dolda filer (all) |
| `-t` | Sortera efter tid (time) |
| `-r` | Omvänd ordning (reverse) |
| `-h` | Human readable storlekar |
| `-R` | Recursive (visa undermappar) |

---

## 📖 Studietips för Tentan

### Måste Kunna

1. **Navigering**: `pwd`, `cd`, `ls` med flaggor
2. **Filhantering**: `touch`, `mkdir`, `rm`, `cp`, `mv`
3. **Läsa filer**: `cat`, `less`
4. **Man pages**: Hitta och läsa dokumentation
5. **Vim basics**: Öppna, editera, spara, avsluta

### Viktigt att Förstå

- Skillnad mellan absoluta och relativa paths
- Hur Tab completion fungerar
- Varför man ska tänka innan man kör `rm`
- Hur man navigerar i man pages och less
- Skillnad mellan `.` (nuvarande) och `..` (upp en nivå)

### Praktisk Övning

1. Gör **vimtutor** (minst en gång!)
2. Läs man pages för alla kommandon ovan
3. Öva navigering i filsystemet
4. Skapa, editera och ta bort filer
5. Använd Vim för anteckningar dagligen

### Vanliga Fel att Undvika

- ❌ Glömma att man är i Insert mode i Vim
- ❌ Använda `rm -rf` utan att dubbelkolla
- ❌ Förväxla absoluta och relativa paths
- ❌ Inte läsa man pages när osäker
- ❌ Försöka scrolla i raw TTY (använd `less` istället)

---

## 🎓 Sammanfattning

### Tre Viktiga Lärdomar

1. **RTFM** - Read The Fine Manual
   - Använd `man` och `info` för dokumentation
   - Sök med `/` i man pages

2. **Think Before You Type**
   - Ingen ångra-funktion för `rm`
   - Dubbelkolla innan du kör destruktiva kommandon

3. **Practice Makes Perfect**
   - Använd Linux dagligen
   - Anteckna i Vim
   - Läs man pages regelbundet

---

## 📚 Referenser

- `man man` - Manual för manual pages
- `man ls`, `man cd`, `man rm`, etc. - Specifik dokumentation
- `vimtutor` - Interaktiv Vim tutorial
- `info info` - Info page dokumentation

---
