# PROMPT 3: Content Rewrite Template

## KONTEXT

Du ska skriva om DevOpsHub tasks från generiskt placeholder-innehåll till pedagogiskt värdefullt material.

Målgrupp: Personer som vill bli DevOps-ingenjörer
Nivå: Från nybörjare till avancerad (beroende på modul)
Språk: Svenska för UI-text, engelska för kod/kommandon

## CONTENT STRUKTUR (OBLIGATORISK)

Varje task MÅSTE följa denna struktur:

```markdown
# {Task Title}

## Varför detta är viktigt
{2-3 meningar som förklarar VARFÖR denna kunskap behövs i verkliga DevOps-arbetet}

## Vad du kommer lära dig
- {Konkret färdighet 1}
- {Konkret färdighet 2}
- {Konkret färdighet 3}

## Förutsättningar
- {Vad användaren behöver ha gjort innan}
- {Verktyg som måste vara installerade}

## Steg-för-steg

### Steg 1: {Beskrivande rubrik}
{Förklaring av vad vi ska göra och varför}

```bash
{Faktiskt kommando som fungerar}
```

**Förväntat resultat:**
```
{Vad användaren ska se}
```

### Steg 2: {Beskrivande rubrik}
{Fortsättning...}

## Vanliga problem

### Problem: {Beskrivning}
**Lösning:** {Hur man fixar det}

## Verifiera att det fungerar

```bash
{Kommando för att verifiera}
```

Du ska se: {Beskrivning av förväntat resultat}

## Sammanfattning
{2-3 meningar som sammanfattar vad användaren lärt sig}

## Nästa steg
{Länk/referens till relaterade tasks}
```

## EXEMPEL: Task "Create personal dotfiles repository"

```markdown
# Skapa ett personligt dotfiles-repository

## Varför detta är viktigt
Som DevOps-ingenjör kommer du arbeta på många olika maskiner — din laptop, produktionsservrar, CI/CD-runners. Ett dotfiles-repository låter dig ha samma konfiguration överallt och återställa din miljö på sekunder istället för timmar.

## Vad du kommer lära dig
- Skapa ett Git-repository för dina konfigurationsfiler
- Organisera dotfiles på ett underhållbart sätt
- Skapa ett installationsscript för automatisk setup

## Förutsättningar
- Git installerat (`git --version` ska fungera)
- GitHub-konto
- Grundläggande terminalkunskap

## Steg-för-steg

### Steg 1: Skapa repository-struktur

Först skapar vi en organiserad mappstruktur:

```bash
mkdir -p ~/dotfiles/{shell,git,vim,scripts}
cd ~/dotfiles
git init
```

**Förväntat resultat:**
```
Initialized empty Git repository in /Users/dittnamn/dotfiles/.git/
```

### Steg 2: Flytta dina befintliga dotfiles

Kopiera dina nuvarande konfigurationsfiler:

```bash
# Shell-konfiguration
cp ~/.zshrc ~/dotfiles/shell/zshrc
cp ~/.bashrc ~/dotfiles/shell/bashrc 2>/dev/null || echo "Ingen .bashrc"

# Git-konfiguration
cp ~/.gitconfig ~/dotfiles/git/gitconfig

# Vim (om du använder det)
cp ~/.vimrc ~/dotfiles/vim/vimrc 2>/dev/null || echo "Ingen .vimrc"
```

### Steg 3: Skapa installationsscript

Skapa `~/dotfiles/install.sh`:

```bash
#!/bin/bash
# Dotfiles installer

DOTFILES_DIR="$HOME/dotfiles"

# Skapa symboliska länkar
ln -sf "$DOTFILES_DIR/shell/zshrc" "$HOME/.zshrc"
ln -sf "$DOTFILES_DIR/git/gitconfig" "$HOME/.gitconfig"

echo "✅ Dotfiles installerade!"
```

Gör scriptet körbart:

```bash
chmod +x ~/dotfiles/install.sh
```

### Steg 4: Pusha till GitHub

```bash
cd ~/dotfiles
git add .
git commit -m "Initial dotfiles setup"
gh repo create dotfiles --public --source=. --push
```

## Vanliga problem

### Problem: "ln: failed to create symbolic link: File exists"
**Lösning:** Filen finns redan. Använd `-f` flaggan för att tvinga överskrivning, eller ta bort filen först med `rm ~/.zshrc`.

### Problem: Ändringar i dotfiles syns inte
**Lösning:** Symboliska länkar pekar på filen, så ändringar i `~/dotfiles/shell/zshrc` påverkar direkt `~/.zshrc`. Kör `source ~/.zshrc` för att ladda om.

## Verifiera att det fungerar

```bash
# Kontrollera att länkarna finns
ls -la ~/.zshrc
# Ska visa: .zshrc -> /Users/dittnamn/dotfiles/shell/zshrc

# Testa på en ny maskin (eller i en container):
git clone https://github.com/DITTNAMN/dotfiles.git ~/dotfiles
cd ~/dotfiles && ./install.sh
```

Du ska se: Alla dina konfigurationsfiler länkade och fungerar direkt.

## Sammanfattning
Du har nu ett versionshanterat repository med dina konfigurationsfiler. Du kan klona det på vilken maskin som helst och köra install.sh för att få exakt samma miljö. Kom ihåg att commita ändringar när du uppdaterar dina dotfiles!

## Nästa steg
- Lägg till fler konfigurationer (tmux, alacritty, starship)
- Skapa en README.md som dokumenterar dina dotfiles
- Utforska andras dotfiles för inspiration: github.com/mathiasbynens/dotfiles
```

## REGLER FÖR INNEHÅLL

### ✅ GÖR
- Skriv steg som faktiskt fungerar (testa dem!)
- Förklara VARFÖR, inte bara HUR
- Inkludera vanliga fel och lösningar
- Visa förväntat resultat efter varje steg
- Använd verkliga exempel

### ❌ GÖR INTE
- Generiska fraser ("this will teach you the basics")
- Placeholder-text ("Concept 1: Understanding...")
- Kod som inte fungerar
- Anta att användaren vet saker du inte förklarat
- Hoppa över verifiering

## BATCH-PROCESS

För att skriva om tasks effektivt:

1. **Välj en modul** (t.ex. "Environment Setup")
2. **Lista alla tasks** i modulen
3. **Skriv om varje task** enligt template ovan
4. **Testa varje kod-exempel** i en ren miljö
5. **Commita modulen** när alla tasks är klara

## COMMIT MESSAGE PER MODUL

```
content(module-01): complete rewrite of Environment Setup tasks

- Rewrote 17 tasks with pedagogical content
- Added working code examples (tested on Ubuntu 24.04)
- Included troubleshooting sections
- Added verification steps

Tasks updated:
- Task 1: macOS vs Linux setup
- Task 2: Terminal emulators
- ...
```

## NÄSTA STEG

Efter content rewrite, fortsätt med PROMPT_4_sidebar_bookmark.md för UX-förbättringar.
