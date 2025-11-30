"""
Bootcamp v3.0 Seed Data - 15 Modules in 4 Tracks
Phase C.1: Seed Bootcamp v3.0 Content (Redo)

Source: docs/bootcamp/bootcamp_v3.0.md

Structure:
- 4 Tracks
- 15 Modules (~200-300 hours total)
- 60+ Labs
- 15+ Projects
"""
from typing import Literal, Optional

DifficultyLevel = Literal["beginner", "intermediate", "advanced", "expert"]


# =============================================================================
# TRACK DEFINITIONS
# =============================================================================

BOOTCAMP_TRACKS: list[dict] = [
    {
        "name": "Foundation",
        "slug": "foundation",
        "description": "Build your core DevOps skills with Linux, scripting, Git, and Python",
        "color": "#6366f1",  # Indigo
        "icon": "🏗️",
        "order_index": 1,
    },
    {
        "name": "Cloud & Infrastructure",
        "slug": "cloud-infrastructure",
        "description": "Master AWS services, Terraform, serverless architecture, and security",
        "color": "#8b5cf6",  # Purple
        "icon": "☁️",
        "order_index": 2,
    },
    {
        "name": "Containers & Orchestration",
        "slug": "containers-orchestration",
        "description": "Learn Docker containerization and Kubernetes orchestration",
        "color": "#06b6d4",  # Cyan
        "icon": "🐳",
        "order_index": 3,
    },
    {
        "name": "Platform Engineering",
        "slug": "platform-engineering",
        "description": "Advanced Kubernetes, GitOps, observability, and SRE practices",
        "color": "#f97316",  # Orange
        "icon": "🚀",
        "order_index": 4,
    },
]


# =============================================================================
# MODULE DEFINITIONS
# =============================================================================

BOOTCAMP_MODULES: list[dict] = [
    # =========================================================================
    # TRACK 1: FOUNDATION (Modules 01-05)
    # =========================================================================
    {
        "track_slug": "foundation",
        "order_index": 1,
        "name": "Environment & Tooling Setup",
        "slug": "environment-tooling-setup",
        "description": "Establish a professional development environment identical to enterprise standards. Build the foundation for the entire bootcamp.",
        "difficulty": "beginner",
        "estimated_hours": 10.0,
        "prerequisites": [],
        "tasks": [
            {
                "title": "macOS vs Linux for DevOps work",
                "difficulty": "easy",
                "estimated_minutes": 15,
                "xp_reward": 25,
                "content": """# macOS vs Linux for DevOps Work

## Introduction
As a DevOps engineer, you'll work with Linux systems daily. Understanding the differences between macOS and Linux helps you choose the right environment for development.

## macOS Advantages
- **Unix-based**: macOS is built on Darwin (BSD), making it familiar for Linux users
- **Hardware quality**: Great for development laptops
- **Docker Desktop**: Works well for local container development
- **GUI + Terminal**: Best of both worlds

## Linux Advantages
- **Production environment**: Most servers run Linux
- **Native containers**: Docker runs natively without virtualization
- **Resource efficiency**: Uses less RAM/CPU than macOS Docker
- **Free and open source**: No licensing costs

## Recommendation
For this bootcamp:
1. **Local development**: macOS or Linux both work great
2. **Production**: Always Linux (Ubuntu, Amazon Linux, etc.)
3. **Learning**: Consider running a Linux VM for hands-on practice

## Key Commands Work Similarly
```bash
# These work on both macOS and Linux
ls -la
cd /path/to/directory
grep "pattern" file.txt
curl https://api.example.com
```

## What's Different
| Task | macOS | Linux |
|------|-------|-------|
| Package manager | Homebrew | apt, yum, dnf |
| File paths | /Users/name | /home/name |
| Service management | launchctl | systemd |
| File system | APFS | ext4, xfs |

## Next Steps
In the next lesson, we'll set up your terminal emulator for maximum productivity.
"""
            },
            {
                "title": "Terminal emulators (iTerm2, Alacritty)",
                "difficulty": "easy",
                "estimated_minutes": 20,
                "xp_reward": 30,
                "content": """# Terminal Emulators: iTerm2 & Alacritty

## Why Terminal Choice Matters
Your terminal is where you'll spend 60-80% of your DevOps time. A good terminal emulator improves productivity significantly.

## iTerm2 (macOS Recommended)

### Installation
```bash
brew install --cask iterm2
```

### Key Features
- **Split panes**: Cmd+D (vertical), Cmd+Shift+D (horizontal)
- **Hotkey window**: Instant terminal with a keypress
- **Search**: Cmd+F to find text in output
- **Profiles**: Different settings for different tasks

### Recommended Settings
1. Go to Preferences → Profiles → Colors
2. Choose a dark theme (Solarized Dark or One Dark)
3. Enable "Unlimited scrollback" in Terminal tab

## Alacritty (Cross-platform, GPU-accelerated)

### Installation
```bash
# macOS
brew install --cask alacritty

# Ubuntu
sudo apt install alacritty
```

### Configuration (~/.config/alacritty/alacritty.yml)
```yaml
window:
  padding:
    x: 10
    y: 10
  opacity: 0.95

font:
  normal:
    family: "JetBrains Mono"
  size: 14.0

colors:
  primary:
    background: '#1e1e2e'
    foreground: '#cdd6f4'
```

### Why Alacritty?
- **Fastest terminal** due to GPU rendering
- **Cross-platform**: Same config on Mac and Linux
- **Simple**: No tabs/panes built-in (use tmux instead)

## Exercise
1. Install iTerm2 or Alacritty
2. Change the color scheme
3. Try creating split panes (iTerm2) or install tmux (Alacritty)

## Pro Tip
Many DevOps engineers use **tmux** for terminal multiplexing, regardless of which terminal emulator they use. We'll cover tmux later!
"""
            },
            {
                "title": "Shell selection (zsh, bash) and configuration",
                "difficulty": "easy",
                "estimated_minutes": 25,
                "xp_reward": 35,
                "content": """# Shell Selection: Zsh vs Bash

## What is a Shell?
The shell is the command interpreter - it reads your commands and executes them. The two most popular shells for DevOps are **bash** and **zsh**.

## Bash (Bourne Again Shell)
- **Default on most Linux servers**
- **POSIX compliant**: Scripts are portable
- **Stable and predictable**

## Zsh (Z Shell)
- **Default on macOS** (since Catalina)
- **Better autocompletion**
- **Themes and plugins** via Oh My Zsh
- **Bash compatible** (mostly)

## Our Recommendation: Zsh for Local, Bash for Scripts

### Install Oh My Zsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Useful Zsh Plugins
Edit `~/.zshrc`:
```bash
plugins=(
  git
  docker
  kubectl
  aws
  terraform
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```

### Install additional plugins:
```bash
# Autosuggestions (gray text completion)
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Syntax highlighting (colors commands)
git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## Shell Configuration Files

| Shell | Login Config | Interactive Config |
|-------|-------------|-------------------|
| Bash | ~/.bash_profile | ~/.bashrc |
| Zsh | ~/.zprofile | ~/.zshrc |

## Important for Scripts
Always use bash for scripts to ensure portability:
```bash
#!/bin/bash
# Your script here
```

## Exercise
1. Check your current shell: `echo $SHELL`
2. Install Oh My Zsh if using zsh
3. Add the git and docker plugins
4. Run `source ~/.zshrc` to reload

## Next Steps
Now that your shell is configured, let's set up package managers to install tools efficiently.
"""
            },
            {
                "title": "Package managers (Homebrew, apt, yum)",
                "difficulty": "easy",
                "estimated_minutes": 20,
                "xp_reward": 30,
                "content": """# Package Managers: Your Tool Installation Hub

## What is a Package Manager?
A package manager automates installing, updating, and removing software. It handles dependencies and keeps everything organized.

## Homebrew (macOS & Linux)

### Installation
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Common Commands
```bash
# Search for a package
brew search docker

# Install a package
brew install git

# Install a GUI app (cask)
brew install --cask visual-studio-code

# Update all packages
brew update && brew upgrade

# List installed packages
brew list

# Remove a package
brew uninstall wget
```

## APT (Ubuntu/Debian)

### Common Commands
```bash
# Update package list
sudo apt update

# Upgrade all packages
sudo apt upgrade -y

# Install a package
sudo apt install nginx

# Search for packages
apt search docker

# Remove a package
sudo apt remove nginx

# Remove package + config
sudo apt purge nginx
```

## YUM/DNF (RHEL/CentOS/Fedora)

```bash
# Install a package
sudo yum install nginx
# or on newer versions
sudo dnf install nginx

# Update all packages
sudo yum update -y

# Search for packages
yum search docker

# List installed packages
yum list installed
```

## Package Manager Comparison

| Feature | Homebrew | APT | YUM/DNF |
|---------|----------|-----|---------|
| OS | macOS, Linux | Debian/Ubuntu | RHEL/CentOS |
| Config location | /usr/local | /etc/apt | /etc/yum.repos.d |
| GUI apps | ✅ (casks) | ❌ (use snap) | ❌ (use flatpak) |

## Pro Tips
1. **Always update first**: `brew update` or `apt update`
2. **Check what's installed**: Avoid duplicate tools
3. **Use version managers** for languages (pyenv, nvm)

## Exercise
1. Update your package manager
2. Install `tree` command: `brew install tree` or `apt install tree`
3. Run `tree -L 2` in your home directory
"""
            },
            {
                "title": "VS Code with DevOps extensions",
                "difficulty": "easy",
                "estimated_minutes": 20,
                "xp_reward": 30,
                "content": """# VS Code: The DevOps IDE

## Why VS Code?
Visual Studio Code is the most popular editor for DevOps because:
- **Free and open source**
- **Excellent extension ecosystem**
- **Integrated terminal**
- **Remote development** (SSH, Containers, WSL)

## Installation
```bash
# macOS
brew install --cask visual-studio-code

# Ubuntu
sudo snap install code --classic
```

## Essential DevOps Extensions

### Install via Command Line
```bash
# Core extensions
code --install-extension ms-azuretools.vscode-docker
code --install-extension hashicorp.terraform
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
code --install-extension redhat.vscode-yaml
code --install-extension ms-vscode-remote.remote-ssh

# Python (for scripts)
code --install-extension ms-python.python

# Git
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph
```

### Extension Categories

**Infrastructure as Code:**
- Terraform (HashiCorp)
- AWS Toolkit
- Azure Tools

**Containers & Kubernetes:**
- Docker (Microsoft)
- Kubernetes (Microsoft)
- YAML (Red Hat)

**Remote Development:**
- Remote - SSH
- Remote - Containers
- Remote - WSL

## Key Settings for DevOps

Open settings.json (Cmd+Shift+P → "Open Settings JSON"):
```json
{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "files.trimTrailingWhitespace": true,
  "terminal.integrated.defaultProfile.osx": "zsh",
  "[terraform]": {
    "editor.formatOnSave": true
  },
  "[yaml]": {
    "editor.tabSize": 2
  }
}
```

## Keyboard Shortcuts to Learn

| Action | Mac | Purpose |
|--------|-----|---------|
| Command Palette | Cmd+Shift+P | Access all commands |
| Terminal | Ctrl+` | Open/close terminal |
| Go to File | Cmd+P | Quick file navigation |
| Search All | Cmd+Shift+F | Search entire project |
| Split Editor | Cmd+\\ | Side-by-side editing |

## Exercise
1. Install VS Code
2. Install the Docker and Terraform extensions
3. Open the integrated terminal (Ctrl+`)
4. Try the Command Palette (Cmd+Shift+P)
"""
            },
            {
                "title": "Docker Desktop installation",
                "difficulty": "easy",
                "estimated_minutes": 15,
                "xp_reward": 25,
                "content": """# Docker Desktop Installation

## What is Docker?
Docker lets you run applications in **containers** - lightweight, isolated environments that include everything needed to run the app.

## Why Containers Matter for DevOps
- **Consistency**: "Works on my machine" → "Works everywhere"
- **Isolation**: Each app has its own dependencies
- **Efficiency**: Share the OS kernel, unlike VMs
- **Portability**: Same container runs locally and in production

## Installation

### macOS
```bash
brew install --cask docker
```
Then open Docker Desktop from Applications.

### Ubuntu
```bash
# Add Docker's official GPG key
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add yourself to docker group (logout/login required)
sudo usermod -aG docker $USER
```

## Verify Installation
```bash
# Check Docker version
docker --version

# Run test container
docker run hello-world

# Check running containers
docker ps
```

## Docker Desktop Settings (macOS)
1. Open Docker Desktop → Settings
2. **Resources**: Allocate at least 4GB RAM, 2 CPUs
3. **Kubernetes**: Enable if you want local K8s
4. **File Sharing**: Ensure your project directories are shared

## Basic Docker Commands
```bash
# Pull an image
docker pull nginx

# Run a container
docker run -d -p 8080:80 nginx

# List containers
docker ps

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>
```

## Exercise
1. Install Docker Desktop
2. Run `docker run hello-world`
3. Run nginx: `docker run -d -p 8080:80 nginx`
4. Open http://localhost:8080 in your browser
5. Stop and remove the container
"""
            },
            {
                "title": "Git and GitHub CLI setup",
                "difficulty": "easy",
                "estimated_minutes": 20,
                "xp_reward": 30,
                "content": """# Git and GitHub CLI Setup

## Git: The Foundation of DevOps
Git is essential for version control of:
- Application code
- Infrastructure as Code (Terraform, Kubernetes)
- Configuration files
- Documentation

## Install Git
```bash
# macOS
brew install git

# Ubuntu
sudo apt install git
```

## Configure Git
```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set VS Code as editor
git config --global core.editor "code --wait"

# Enable colored output
git config --global color.ui auto

# Set pull strategy
git config --global pull.rebase false
```

## GitHub CLI (gh)

The GitHub CLI lets you interact with GitHub from the terminal.

### Installation
```bash
# macOS
brew install gh

# Ubuntu
sudo apt install gh
```

### Authentication
```bash
gh auth login
# Follow the prompts to authenticate via browser
```

### Useful Commands
```bash
# Clone a repo
gh repo clone owner/repo

# Create a new repo
gh repo create my-project --public

# Create a pull request
gh pr create --title "Add feature" --body "Description"

# View pull requests
gh pr list

# Check out a PR locally
gh pr checkout 123

# View issues
gh issue list
```

## Essential Git Aliases

Add to `~/.gitconfig`:
```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate
    last = log -1 HEAD
    unstage = reset HEAD --
```

## Verify Setup
```bash
# Check Git version
git --version

# Check config
git config --list

# Check GitHub auth
gh auth status
```

## Exercise
1. Install Git and configure your identity
2. Install GitHub CLI and authenticate
3. Create a test repository: `gh repo create test-repo --public`
4. Clone it: `gh repo clone <your-username>/test-repo`
5. Make a commit and push
"""
            },
            {
                "title": "AWS CLI v2 installation",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# AWS CLI v2 Installation

## Varför detta är viktigt
AWS CLI är det primära verktyget för att interagera med Amazon Web Services från terminalen. Som DevOps-ingenjör kommer du använda det dagligen för att hantera EC2-instanser, S3-buckets, IAM-användare och hundratals andra AWS-tjänster.

## Vad du kommer lära dig
- Installera AWS CLI v2 på ditt operativsystem
- Konfigurera credentials och profiler
- Verifiera installationen med ett enkelt API-anrop

## Förutsättningar
- Terminal/shell konfigurerad
- Ett AWS-konto (free tier räcker)
- Access Key ID och Secret Access Key från AWS Console

## Steg-för-steg

### Steg 1: Installera AWS CLI v2

<!-- OS:macos -->
**macOS (med Homebrew - rekommenderat):**
```bash
brew install awscli
```

**Alternativ: Officiell installer:**
```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
rm AWSCLIV2.pkg
```

**Förväntat resultat:**
```
aws --version
aws-cli/2.15.0 Python/3.11.6 Darwin/23.0.0 source/arm64
```
<!-- /OS:macos -->

<!-- OS:windows -->
**Windows (via winget - rekommenderat):**
```powershell
winget install Amazon.AWSCLI
```

**Alternativ: MSI Installer:**
1. Ladda ner från: https://awscli.amazonaws.com/AWSCLIV2.msi
2. Kör MSI-filen och följ installationsguiden
3. Starta om terminalen efter installation

**WSL2 (Ubuntu i Windows):**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```

**Förväntat resultat (PowerShell):**
```
aws --version
aws-cli/2.15.0 Python/3.11.6 Windows/10 exe/AMD64
```
<!-- /OS:windows -->

<!-- OS:linux -->
<!-- DISTRO:ubuntu -->
**Ubuntu/Debian:**
```bash
# Ladda ner och installera
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install -y unzip
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```
<!-- /DISTRO:ubuntu -->

<!-- DISTRO:debian -->
**Debian:**
```bash
# Ladda ner och installera
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install -y unzip
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```
<!-- /DISTRO:debian -->

<!-- DISTRO:fedora -->
**Fedora:**
```bash
# Ladda ner och installera
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo dnf install -y unzip
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```
<!-- /DISTRO:fedora -->

<!-- DISTRO:arch -->
**Arch Linux:**
```bash
# Via AUR (yay)
yay -S aws-cli-v2-bin

# Eller manuellt
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```
<!-- /DISTRO:arch -->

<!-- DISTRO:centos -->
**CentOS/RHEL:**
```bash
# Ladda ner och installera
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo yum install -y unzip
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip
```
<!-- /DISTRO:centos -->

**Förväntat resultat:**
```
aws --version
aws-cli/2.15.0 Python/3.11.6 Linux/6.5.0 source/x86_64
```
<!-- /OS:linux -->

### Steg 2: Skapa AWS Access Keys

1. Logga in på AWS Console → IAM → Users
2. Välj din användare → Security credentials
3. Klicka "Create access key"
4. Välj "Command Line Interface (CLI)"
5. Spara Access Key ID och Secret Access Key säkert!

### Steg 3: Konfigurera AWS CLI

```bash
aws configure
```

**Input som krävs:**
```
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: eu-north-1
Default output format [None]: json
```

### Steg 4: Konfigurera flera profiler (valfritt)

För att hantera flera AWS-konton:

```bash
aws configure --profile work
aws configure --profile personal
```

Använd profil:
```bash
aws s3 ls --profile work
# eller
export AWS_PROFILE=work
aws s3 ls
```

<!-- OS:windows -->
**PowerShell:**
```powershell
$env:AWS_PROFILE = "work"
aws s3 ls
```
<!-- /OS:windows -->

## Vanliga problem

### Problem: "Unable to locate credentials"
**Lösning:** Kör `aws configure` igen eller kontrollera att `~/.aws/credentials` finns.

<!-- OS:windows -->
**Windows:** Kontrollera att filen finns på `C:\\Users\\DITTNAMN\\.aws\\credentials`
<!-- /OS:windows -->

### Problem: "An error occurred (InvalidClientTokenId)"
**Lösning:** Dina access keys är felaktiga eller inaktiverade. Skapa nya i AWS Console.

### Problem: "An error occurred (ExpiredToken)"
**Lösning:** Om du använder MFA/temporary credentials, förnya din session.

<!-- OS:windows -->
### Problem: "aws is not recognized as an internal or external command"
**Lösning:** Starta om PowerShell/CMD efter installation. Om det fortfarande inte fungerar, lägg till AWS CLI till PATH manuellt.
<!-- /OS:windows -->

## Verifiera att det fungerar

```bash
# Lista S3 buckets (kräver s3:ListAllMyBuckets permission)
aws s3 ls

# Visa din AWS-identitet
aws sts get-caller-identity
```

**Förväntat resultat:**
```json
{
    "UserId": "AIDAEXAMPLEUSERID",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/dittnamn"
}
```

## Sammanfattning
Du har nu AWS CLI v2 installerat och konfigurerat. Du kan interagera med alla AWS-tjänster direkt från terminalen. I kommande moduler kommer vi använda AWS CLI för att skapa VPC:er, EC2-instanser, och mycket mer.

## Nästa steg
- Lär dig grundläggande S3-kommandon: `aws s3 cp`, `aws s3 sync`
- Utforska `aws ec2 describe-instances`
- Sätt upp MFA för extra säkerhet
"""
            },
            {
                "title": "Terraform installation",
                "difficulty": "medium",
                "estimated_minutes": 15,
                "xp_reward": 35,
                "content": """# Terraform Installation

## Varför detta är viktigt
Terraform är industristandarden för Infrastructure as Code (IaC). Det låter dig definiera din infrastruktur i kod och versionera den med Git. Istället för att klicka i AWS Console skapar du reproducerbara, granskningsbara infrastruktur-definitioner.

## Vad du kommer lära dig
- Installera Terraform via tfenv (version manager)
- Verifiera installationen
- Förstå Terraform-versioner och varför de är viktiga

## Förutsättningar
- Terminal konfigurerad
- Git installerat

## Steg-för-steg

### Steg 1: Installera tfenv (Terraform version manager)

Vi använder tfenv istället för att installera Terraform direkt. Detta låter oss enkelt växla mellan versioner.

**macOS:**
```bash
brew install tfenv
```

**Linux:**
```bash
git clone https://github.com/tfutils/tfenv.git ~/.tfenv
echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Steg 2: Installera Terraform

```bash
# Lista tillgängliga versioner
tfenv list-remote | head -10

# Installera senaste stabila version
tfenv install latest

# Eller installera specifik version (rekommenderat för team)
tfenv install 1.7.0
tfenv use 1.7.0
```

**Förväntat resultat:**
```
Installing Terraform v1.7.0
Terraform v1.7.0 is successfully installed
```

### Steg 3: Verifiera installation

```bash
terraform version
```

**Förväntat resultat:**
```
Terraform v1.7.0
on darwin_arm64
```

### Steg 4: Sätt upp .terraform-version fil

I varje projekt, skapa en fil som specificerar vilken Terraform-version som ska användas:

```bash
echo "1.7.0" > .terraform-version
```

När du `cd` in i projektet kommer tfenv automatiskt använda rätt version.

## Alternativ: Direkt installation (utan tfenv)

Om du föredrar att inte använda version manager:

**macOS:**
```bash
brew install terraform
```

**Linux:**
```bash
wget https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip
unzip terraform_1.7.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
rm terraform_1.7.0_linux_amd64.zip
```

## Vanliga problem

### Problem: "command not found: terraform"
**Lösning:** Se till att ~/.tfenv/bin finns i din PATH. Kör `source ~/.zshrc`.

### Problem: Versionskonflikt i team
**Lösning:** Använd .terraform-version fil i alla projekt.

## Verifiera att det fungerar

Skapa en minimal Terraform-fil för att testa:

```bash
mkdir ~/terraform-test && cd ~/terraform-test

cat > main.tf << 'EOF'
terraform {
  required_version = ">= 1.0"
}

output "hello" {
  value = "Terraform fungerar!"
}
EOF

terraform init
terraform apply -auto-approve
```

**Förväntat resultat:**
```
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

hello = "Terraform fungerar!"
```

## Sammanfattning
Du har nu Terraform installerat med tfenv för enkel versionshantering. I modul 07 kommer vi dyka djupt in i Terraform och bygga riktig AWS-infrastruktur.

## Nästa steg
- Läs Terraform-dokumentationen på terraform.io
- Titta på Terraform Registry för färdiga moduler
- Installera VS Code extension: HashiCorp Terraform
"""
            },
            {
                "title": "kubectl installation",
                "difficulty": "medium",
                "estimated_minutes": 15,
                "xp_reward": 35,
                "content": """# kubectl Installation

## Varför detta är viktigt
kubectl är kommandorads-verktyget för att interagera med Kubernetes-kluster. Som DevOps-ingenjör kommer du använda kubectl dagligen för att deploya applikationer, felsöka pods, och hantera kluster-resurser.

## Vad du kommer lära dig
- Installera kubectl
- Konfigurera kubectl för att ansluta till ett kluster
- Grundläggande kubectl-kommandon

## Förutsättningar
- Terminal konfigurerad
- (Valfritt) Docker Desktop installerat för lokal Kubernetes

## Steg-för-steg

### Steg 1: Installera kubectl

**macOS:**
```bash
brew install kubectl
```

**Linux (Ubuntu/Debian):**
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Förväntat resultat:**
```bash
kubectl version --client
# Client Version: v1.29.0
```

### Steg 2: Installera kubectx och kubens (rekommenderat)

Dessa verktyg gör det enkelt att växla mellan kluster och namespaces:

```bash
# macOS
brew install kubectx

# Linux
sudo git clone https://github.com/ahmetb/kubectx /opt/kubectx
sudo ln -s /opt/kubectx/kubectx /usr/local/bin/kubectx
sudo ln -s /opt/kubectx/kubens /usr/local/bin/kubens
```

### Steg 3: Aktivera kubectl autocompletion

```bash
# Zsh
echo 'source <(kubectl completion zsh)' >> ~/.zshrc
echo 'alias k=kubectl' >> ~/.zshrc
echo 'complete -F __start_kubectl k' >> ~/.zshrc
source ~/.zshrc

# Bash
echo 'source <(kubectl completion bash)' >> ~/.bashrc
source ~/.bashrc
```

### Steg 4: Konfigurera ett lokalt kluster (valfritt)

**Med Docker Desktop:**
1. Öppna Docker Desktop → Settings → Kubernetes
2. Bocka i "Enable Kubernetes"
3. Klicka "Apply & Restart"

**Med kind (Kubernetes in Docker):**
```bash
brew install kind  # eller: go install sigs.k8s.io/kind@latest
kind create cluster --name devops-lab
```

**Med minikube:**
```bash
brew install minikube
minikube start
```

## Vanliga problem

### Problem: "The connection to the server localhost:8080 was refused"
**Lösning:** Inget kluster är konfigurerat. Starta Docker Desktop Kubernetes eller skapa ett kind-kluster.

### Problem: "error: You must be logged in to the server"
**Lösning:** Dina credentials har gått ut. För EKS, kör `aws eks update-kubeconfig --name CLUSTER_NAME`.

## Verifiera att det fungerar

```bash
# Visa kluster-info
kubectl cluster-info

# Lista nodes
kubectl get nodes

# Lista alla pods i alla namespaces
kubectl get pods -A
```

**Förväntat resultat (Docker Desktop):**
```
NAME             STATUS   ROLES           AGE   VERSION
docker-desktop   Ready    control-plane   10m   v1.29.0
```

## Användbara kubectl-kommandon

```bash
# Kortkommandon (lägg till i .zshrc)
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgn='kubectl get nodes'
alias kaf='kubectl apply -f'
alias kdel='kubectl delete'
alias klog='kubectl logs'
alias kex='kubectl exec -it'
```

## Sammanfattning
Du har nu kubectl installerat och redo att interagera med Kubernetes-kluster. I modul 12 kommer vi dyka djupt in i Kubernetes och bygga riktiga applikationer.

## Nästa steg
- Experimentera med `kubectl run nginx --image=nginx`
- Lär dig `kubectl describe` för felsökning
- Utforska `kubectl explain` för API-dokumentation
"""
            },
            {
                "title": "Python 3.11+ setup",
                "difficulty": "easy",
                "estimated_minutes": 15,
                "xp_reward": 25,
                "content": """# Python 3.11+ Setup

## Varför detta är viktigt
Python är det dominerande språket för DevOps-automation. Du kommer använda det för att skriva scripts, interagera med AWS via boto3, bygga CLI-verktyg, och automatisera allt möjligt. Version 3.11+ ger bättre prestanda och nya features.

## Vad du kommer lära dig
- Installera Python via pyenv (version manager)
- Konfigurera virtuella miljöer
- Sätta upp en professionell Python-utvecklingsmiljö

## Förutsättningar
- Terminal konfigurerad
- Homebrew (macOS) eller build-tools (Linux)

## Steg-för-steg

### Steg 1: Installera pyenv

Vi använder pyenv för att hantera Python-versioner. Detta undviker konflikter med system-Python.

**macOS:**
```bash
brew install pyenv pyenv-virtualenv

# Lägg till i ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc
```

**Linux (Ubuntu/Debian):**
```bash
# Installera dependencies först
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \\
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \\
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \\
  libffi-dev liblzma-dev

# Installera pyenv
curl https://pyenv.run | bash

# Lägg till i ~/.bashrc eller ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Steg 2: Installera Python 3.12

```bash
# Lista tillgängliga versioner
pyenv install --list | grep "^  3.12"

# Installera senaste 3.12.x
pyenv install 3.12.1

# Sätt som global default
pyenv global 3.12.1
```

**Förväntat resultat:**
```bash
python --version
# Python 3.12.1
```

### Steg 3: Skapa virtuella miljöer

```bash
# Skapa en virtuell miljö för ett projekt
pyenv virtualenv 3.12.1 devops-tools

# Aktivera i ett projekt-directory
cd ~/projects/my-devops-project
pyenv local devops-tools
# Nu aktiveras miljön automatiskt när du cd:ar hit
```

### Steg 4: Installera grundläggande paket

```bash
# Uppgradera pip
pip install --upgrade pip

# Installera DevOps-essentials
pip install boto3 requests pyyaml python-dotenv click rich
```

## Vanliga problem

### Problem: "pyenv: no such command 'virtualenv'"
**Lösning:** Installera pyenv-virtualenv: `brew install pyenv-virtualenv`

### Problem: "BUILD FAILED" vid Python-installation
**Lösning:** Du saknar build dependencies. På Linux, kör apt install-kommandot från Steg 1.

### Problem: "pip: command not found"
**Lösning:** Se till att din pyenv-shims är i PATH. Kör `pyenv rehash`.

## Verifiera att det fungerar

```bash
# Kontrollera Python-version
python --version

# Kontrollera pip
pip --version

# Testa ett enkelt script
python -c "import sys; print(f'Python {sys.version}')"

# Testa boto3
pip install boto3
python -c "import boto3; print('boto3 fungerar!')"
```

**Förväntat resultat:**
```
Python 3.12.1
pip 24.0 from /Users/.../.pyenv/versions/3.12.1/lib/python3.12/site-packages/pip
boto3 fungerar!
```

## Sammanfattning
Du har nu en professionell Python-setup med pyenv för versionshantering och virtuella miljöer. Detta ger dig flexibilitet att arbeta med olika projekt som kräver olika Python-versioner.

## Nästa steg
- Installera VS Code Python extension
- Läs om Python best practices i modul 05
- Skapa ditt första boto3-script
"""
            },
            {
                "title": "SSH key generation and management",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# SSH Key Generation and Management

## Varför detta är viktigt
SSH-nycklar är fundamentet för säker autentisering i DevOps. Du använder dem för att logga in på servrar, pusha kod till GitHub, och ansluta till AWS EC2-instanser. Lösenord är inte acceptabelt i produktionsmiljöer.

## Vad du kommer lära dig
- Generera Ed25519 SSH-nycklar (moderna och säkra)
- Konfigurera SSH config för enkel användning
- Lägga till nycklar på GitHub och servrar
- Använda ssh-agent för nyckelhantering

## Förutsättningar
- Terminal konfigurerad
- GitHub-konto

## Steg-för-steg

### Steg 1: Generera SSH-nyckel

Vi använder Ed25519-algoritmen som är modernare och säkrare än RSA:

```bash
ssh-keygen -t ed25519 -C "din.email@example.com"
```

**När du blir frågad:**
```
Enter file in which to save the key: [tryck Enter för default]
Enter passphrase: [valfritt men rekommenderat]
```

**Förväntat resultat:**
```
Your identification has been saved in /Users/dittnamn/.ssh/id_ed25519
Your public key has been saved in /Users/dittnamn/.ssh/id_ed25519.pub
```

### Steg 2: Sätt korrekta filrättigheter

SSH är extremt strikt med filrättigheter:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### Steg 3: Starta ssh-agent och lägg till nyckel

```bash
# Starta ssh-agent
eval "$(ssh-agent -s)"

# Lägg till nyckel (macOS sparar i Keychain)
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

# Linux:
ssh-add ~/.ssh/id_ed25519
```

### Steg 4: Konfigurera SSH config

Skapa/redigera `~/.ssh/config`:

```bash
cat >> ~/.ssh/config << 'EOF'
# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    AddKeysToAgent yes

# Exempel: AWS EC2-server
Host my-server
    HostName ec2-XX-XX-XX-XX.eu-north-1.compute.amazonaws.com
    User ubuntu
    IdentityFile ~/.ssh/aws-key.pem

# Wildcard för alla AWS-servrar
Host *.amazonaws.com
    User ubuntu
    IdentityFile ~/.ssh/aws-key.pem
    StrictHostKeyChecking no
EOF
```

### Steg 5: Lägg till nyckel på GitHub

```bash
# Kopiera public key till clipboard
# macOS:
pbcopy < ~/.ssh/id_ed25519.pub

# Linux:
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
```

Sedan på GitHub:
1. Settings → SSH and GPG keys
2. New SSH key
3. Klistra in nyckeln
4. Give it a descriptive name

## Vanliga problem

### Problem: "Permission denied (publickey)"
**Lösning:** Kontrollera att din public key finns på servern/GitHub. Kör `ssh-add -l` för att se laddade nycklar.

### Problem: "WARNING: UNPROTECTED PRIVATE KEY FILE!"
**Lösning:** Kör `chmod 600 ~/.ssh/id_ed25519`

### Problem: "Agent admitted failure to sign"
**Lösning:** Starta ssh-agent och lägg till nyckeln igen.

## Verifiera att det fungerar

```bash
# Testa GitHub-anslutning
ssh -T git@github.com
```

**Förväntat resultat:**
```
Hi dittnamn! You've successfully authenticated, but GitHub does not provide shell access.
```

## Flera nycklar för olika ändamål

```bash
# Separat nyckel för arbete
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_work -C "work@company.com"

# Uppdatera ~/.ssh/config
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
```

## Sammanfattning
Du har nu säkra SSH-nycklar konfigurerade för GitHub och är redo att ansluta till servrar. Använd alltid Ed25519 för nya nycklar och skydda dina privata nycklar med passphrase.

## Nästa steg
- Lägg till GPG-signering för commits
- Konfigurera SSH för AWS EC2
- Utforska SSH tunneling
"""
            },
            {
                "title": "GPG signing for commits",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# GPG Signing for Commits

## Varför detta är viktigt
GPG-signering bevisar att commits verkligen kommer från dig och inte någon som förfalskar ditt namn. GitHub visar "Verified" på signerade commits. Många företag kräver signerade commits i production-repos.

## Vad du kommer lära dig
- Generera en GPG-nyckel
- Konfigurera Git för automatisk signering
- Lägga till GPG-nyckeln på GitHub

## Förutsättningar
- Git konfigurerat med din email
- GitHub-konto

## Steg-för-steg

### Steg 1: Installera GPG

**macOS:**
```bash
brew install gnupg pinentry-mac
```

**Linux:**
```bash
sudo apt install gnupg
```

### Steg 2: Generera GPG-nyckel

```bash
gpg --full-generate-key
```

**När du blir frågad:**
1. Typ: `1` (RSA and RSA)
2. Keysize: `4096`
3. Giltighet: `0` (aldrig)
4. Real name: Ditt namn
5. Email: **Samma email som i Git config!**
6. Passphrase: Välj en stark passphrase

### Steg 3: Hitta ditt key ID

```bash
gpg --list-secret-keys --keyid-format=long
```

**Output:**
```
sec   rsa4096/3AA5C34371567BD2 2024-01-15
      ABCDEF1234567890ABCDEF1234567890ABCDEF12
uid           [ultimate] Ditt Namn <din.email@example.com>
```

Key ID är `3AA5C34371567BD2` (efter `rsa4096/`).

### Steg 4: Konfigurera Git

```bash
# Sätt din signing key
git config --global user.signingkey 3AA5C34371567BD2

# Aktivera signering för alla commits
git config --global commit.gpgsign true

# Aktivera signering för alla tags
git config --global tag.gpgsign true

# Konfigurera GPG program
git config --global gpg.program gpg
```

### Steg 5: Konfigurera GPG Agent (macOS)

```bash
# Skapa ~/.gnupg/gpg-agent.conf
mkdir -p ~/.gnupg
echo "pinentry-program /opt/homebrew/bin/pinentry-mac" >> ~/.gnupg/gpg-agent.conf
echo "default-cache-ttl 3600" >> ~/.gnupg/gpg-agent.conf
echo "max-cache-ttl 86400" >> ~/.gnupg/gpg-agent.conf

# Lägg till i ~/.zshrc
echo 'export GPG_TTY=$(tty)' >> ~/.zshrc
source ~/.zshrc

# Starta om agent
gpgconf --kill gpg-agent
```

### Steg 6: Lägg till GPG-nyckel på GitHub

```bash
# Exportera public key
gpg --armor --export 3AA5C34371567BD2 | pbcopy
```

På GitHub:
1. Settings → SSH and GPG keys
2. New GPG key
3. Klistra in nyckeln

## Vanliga problem

### Problem: "error: gpg failed to sign the data"
**Lösning:**
```bash
export GPG_TTY=$(tty)
gpgconf --kill gpg-agent
```

### Problem: Pinentry öppnas inte
**Lösning (macOS):** Installera pinentry-mac: `brew install pinentry-mac`

### Problem: "secret key not available"
**Lösning:** Kontrollera att key ID är korrekt: `gpg --list-secret-keys`

## Verifiera att det fungerar

```bash
# Skapa en test-commit
cd /tmp && mkdir gpg-test && cd gpg-test
git init
echo "test" > test.txt
git add . && git commit -m "Test signed commit"

# Verifiera signaturen
git log --show-signature -1
```

**Förväntat resultat:**
```
commit abc123... (HEAD -> main)
gpg: Signature made Mon Jan 15 10:00:00 2024 CET
gpg: Good signature from "Ditt Namn <din.email@example.com>"
```

## Sammanfattning
Dina Git commits är nu signerade och kan verifieras. GitHub kommer visa en grön "Verified" badge på alla dina signerade commits, vilket ökar förtroendet för din kod.

## Nästa steg
- Aktivera "Vigilant mode" på GitHub för att flagga osignerade commits
- Säkerhetskopiera dina GPG-nycklar
- Överväg att använda en hårdvarunyckel (YubiKey)
"""
            },
            {
                "title": "MFA setup for all services",
                "difficulty": "medium",
                "estimated_minutes": 15,
                "xp_reward": 35,
                "content": """# MFA Setup for All Services

## Varför detta är viktigt
Multi-Factor Authentication (MFA) är det enklaste sättet att dramatiskt öka säkerheten för dina konton. Om någon får tag på ditt lösenord behöver de fortfarande din telefon. AWS, GitHub, och alla kritiska tjänster MÅSTE ha MFA aktiverat.

## Vad du kommer lära dig
- Sätta upp MFA på GitHub, AWS, och andra tjänster
- Använda authenticator-appar
- Hantera backup-koder säkert

## Förutsättningar
- Smartphone med authenticator-app
- Konton på GitHub och AWS

## Steg-för-steg

### Steg 1: Installera en authenticator-app

Rekommenderade appar (välj EN):

**1Password** (Bäst om du redan använder det)
- Integrerad lösenordshanterare + TOTP

**Authy** (Rekommenderad för de flesta)
- Cloud backup av TOTP-koder
- Fungerar på flera enheter
- https://authy.com

**Google Authenticator**
- Simpel, ingen cloud backup
- Förlorar du telefonen, förlorar du koderna

### Steg 2: Aktivera MFA på GitHub

1. GitHub → Settings → Password and authentication
2. Klicka "Enable two-factor authentication"
3. Välj "Set up using an app"
4. Skanna QR-koden med din authenticator
5. **VIKTIGT:** Spara recovery codes på säker plats!

```bash
# Exempel: Spara recovery codes krypterat
echo "github-recovery-codes:
XXXXX-XXXXX
XXXXX-XXXXX
..." | gpg -c > ~/recovery-codes/github.gpg
```

### Steg 3: Aktivera MFA på AWS

1. AWS Console → IAM → Users → Ditt användarnamn
2. Security credentials → Assigned MFA device → Assign MFA device
3. Välj "Authenticator app"
4. Skanna QR-koden
5. Ange två på varandra följande koder

**Eller via CLI:**
```bash
# Skapa virtuell MFA-enhet
aws iam create-virtual-mfa-device \\
    --virtual-mfa-device-name my-mfa \\
    --outfile ~/mfa-qr.png \\
    --bootstrap-method QRCodePNG

# Aktivera MFA (behöver två koder)
aws iam enable-mfa-device \\
    --user-name dittnamn \\
    --serial-number arn:aws:iam::123456789012:mfa/my-mfa \\
    --authentication-code1 123456 \\
    --authentication-code2 789012
```

### Steg 4: Aktivera MFA på andra tjänster

**GitLab:**
Settings → Account → Two-Factor Authentication

**Docker Hub:**
Account Settings → Security → Two-Factor Authentication

**Cloudflare:**
My Profile → Authentication → Two-Factor Authentication

### Steg 5: Hantera backup-koder

```bash
# Skapa en säker plats för recovery codes
mkdir -p ~/.recovery-codes
chmod 700 ~/.recovery-codes

# Kryptera med GPG
echo "AWS: XXXXX, XXXXX
GitHub: XXXXX, XXXXX" | gpg -c > ~/.recovery-codes/all-codes.gpg

# Dekryptera när du behöver dem
gpg -d ~/.recovery-codes/all-codes.gpg
```

## Vanliga problem

### Problem: Förlorad telefon
**Lösning:** Använd recovery codes. Därför är det KRITISKT att spara dem!

### Problem: MFA-koder fungerar inte
**Lösning:** Kontrollera att telefonens tid är korrekt. TOTP är tidsbaserat.

### Problem: Låst ute från AWS root account
**Lösning:** Kontakta AWS Support med kontobevis.

## Verifiera att det fungerar

```bash
# Testa GitHub (logga ut och in igen)
gh auth logout
gh auth login
# Du ska bli ombedd om MFA-kod

# Testa AWS (om CLI är konfigurerat med MFA)
aws sts get-caller-identity
```

## AWS CLI med MFA

Om ditt AWS-konto kräver MFA för CLI-åtkomst:

```bash
# Skapa en script för att förnya credentials
cat > ~/bin/aws-mfa << 'EOF'
#!/bin/bash
MFA_ARN="arn:aws:iam::123456789012:mfa/dittnamn"
read -p "MFA Code: " MFA_CODE
CREDS=$(aws sts get-session-token --serial-number $MFA_ARN --token-code $MFA_CODE)
export AWS_ACCESS_KEY_ID=$(echo $CREDS | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $CREDS | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $CREDS | jq -r '.Credentials.SessionToken')
echo "AWS credentials updated!"
EOF
chmod +x ~/bin/aws-mfa
```

## Sammanfattning
Du har nu MFA aktiverat på dina kritiska konton. Detta är en av de viktigaste säkerhetsåtgärderna du kan ta. Förlora aldrig dina recovery codes!

## Nästa steg
- Överväg hårdvarunycklar (YubiKey) för extra säkerhet
- Sätt upp MFA på alla nya tjänster du registrerar dig på
- Utforska AWS Organizations för centraliserad MFA-policy
"""
            },
            {
                "title": "Create personal dotfiles repository",
                "difficulty": "medium",
                "estimated_minutes": 25,
                "xp_reward": 45,
                "content": """# Skapa ett personligt dotfiles-repository

## Varför detta är viktigt
Som DevOps-ingenjör kommer du arbeta på många olika maskiner — din laptop, produktionsservrar, CI/CD-runners. Ett dotfiles-repository låter dig ha samma konfiguration överallt och återställa din miljö på sekunder istället för timmar.

## Vad du kommer lära dig
- Skapa ett Git-repository för dina konfigurationsfiler
- Organisera dotfiles på ett underhållbart sätt
- Skapa ett installationsscript för automatisk setup

## Förutsättningar
- Git installerat (`git --version` ska fungera)
- GitHub-konto och GitHub CLI konfigurerat
- Grundläggande terminalkunskap

## Steg-för-steg

### Steg 1: Skapa repository-struktur

Först skapar vi en organiserad mappstruktur:

```bash
mkdir -p ~/dotfiles/{shell,git,vim,scripts,config}
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
cp ~/.bashrc ~/dotfiles/shell/bashrc 2>/dev/null || true

# Git-konfiguration
cp ~/.gitconfig ~/dotfiles/git/gitconfig

# Skapa en grundläggande zshrc om den inte finns
cat > ~/dotfiles/shell/zshrc << 'EOF'
# DevOps Zsh Configuration

# Path
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"

# Editor
export EDITOR="code --wait"

# Aliases
alias ll="ls -la"
alias k="kubectl"
alias tf="terraform"
alias g="git"
alias dc="docker compose"

# Git aliases
alias gs="git status"
alias gp="git pull"
alias gc="git commit"
alias gco="git checkout"

# AWS
alias awswho="aws sts get-caller-identity"

# Kubernetes
alias kgp="kubectl get pods"
alias kgs="kubectl get svc"
alias kgn="kubectl get nodes"

# Load local config if exists
[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
EOF
```

### Steg 3: Skapa installationsscript

Skapa `~/dotfiles/install.sh`:

```bash
cat > ~/dotfiles/install.sh << 'SCRIPT'
#!/bin/bash
set -e

DOTFILES_DIR="$HOME/dotfiles"
BACKUP_DIR="$HOME/.dotfiles-backup-$(date +%Y%m%d)"

echo "🚀 Installing dotfiles..."

# Skapa backup av befintliga filer
backup_file() {
    if [[ -f "$1" ]] && [[ ! -L "$1" ]]; then
        mkdir -p "$BACKUP_DIR"
        mv "$1" "$BACKUP_DIR/"
        echo "  📦 Backed up $1"
    fi
}

# Skapa symbolisk länk
link_file() {
    local src="$1"
    local dest="$2"
    backup_file "$dest"
    ln -sf "$src" "$dest"
    echo "  ✅ Linked $dest -> $src"
}

# Shell
link_file "$DOTFILES_DIR/shell/zshrc" "$HOME/.zshrc"
link_file "$DOTFILES_DIR/shell/bashrc" "$HOME/.bashrc" 2>/dev/null || true

# Git
link_file "$DOTFILES_DIR/git/gitconfig" "$HOME/.gitconfig"

# Skapa bin-directory
mkdir -p "$HOME/bin"

echo ""
echo "✅ Dotfiles installed successfully!"
echo "💡 Run 'source ~/.zshrc' to reload your shell config"
[[ -d "$BACKUP_DIR" ]] && echo "📦 Old files backed up to: $BACKUP_DIR"
SCRIPT

chmod +x ~/dotfiles/install.sh
```

### Steg 4: Skapa gitconfig

```bash
cat > ~/dotfiles/git/gitconfig << 'EOF'
[user]
    name = Ditt Namn
    email = din.email@example.com

[core]
    editor = code --wait
    autocrlf = input

[init]
    defaultBranch = main

[pull]
    rebase = false

[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate -20
    last = log -1 HEAD
    unstage = reset HEAD --

[color]
    ui = auto
EOF
```

### Steg 5: Pusha till GitHub

```bash
cd ~/dotfiles
git add .
git commit -m "Initial dotfiles setup"
gh repo create dotfiles --public --source=. --push
```

## Vanliga problem

### Problem: "ln: failed to create symbolic link: File exists"
**Lösning:** Install-scriptet hanterar detta genom backup. Kör `./install.sh` igen.

### Problem: Ändringar i dotfiles syns inte
**Lösning:** Kör `source ~/.zshrc` för att ladda om konfigurationen.

## Verifiera att det fungerar

```bash
# Kontrollera att länkarna finns
ls -la ~/.zshrc
# Output: .zshrc -> /Users/dittnamn/dotfiles/shell/zshrc

# Testa på en "ny maskin" (i en container):
docker run -it ubuntu:22.04 bash
apt update && apt install -y git curl
git clone https://github.com/DITTNAMN/dotfiles.git ~/dotfiles
cd ~/dotfiles && ./install.sh
```

## Sammanfattning
Du har nu ett versionshanterat repository med dina konfigurationsfiler. Du kan klona det på vilken maskin som helst och köra install.sh för att få exakt samma miljö.

## Nästa steg
- Lägg till tmux-konfiguration
- Skapa en README.md som dokumenterar dina dotfiles
- Utforska andras dotfiles för inspiration: github.com/mathiasbynens/dotfiles
"""
            },
            {
                "title": "Shell aliases and functions",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# Shell Aliases and Functions

## Varför detta är viktigt
Shell aliases och functions är dina personliga genvägar. De sparar tid, minskar skrivfel, och gör komplexa kommandon enkla att köra. Erfarna DevOps-ingenjörer har hundratals anpassade aliases.

## Vad du kommer lära dig
- Skapa och organisera aliases
- Skriva shell-funktioner för komplexa operationer
- Bygga ett DevOps-specifikt alias-bibliotek

## Förutsättningar
- Zsh eller Bash konfigurerat
- Grundläggande shell-kunskap

## Steg-för-steg

### Steg 1: Förstå aliases vs functions

**Aliases** - Enkla kommando-ersättningar:
```bash
alias ll="ls -la"
```

**Functions** - När du behöver argument eller logik:
```bash
mkcd() {
    mkdir -p "$1" && cd "$1"
}
```

### Steg 2: Skapa alias-fil

Organisera aliases i en separat fil:

```bash
cat > ~/dotfiles/shell/aliases.sh << 'EOF'
# =============================================================================
# DevOps Shell Aliases
# =============================================================================

# -----------------------------------------------------------------------------
# Navigation
# -----------------------------------------------------------------------------
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias ~="cd ~"
alias -- -="cd -"

# -----------------------------------------------------------------------------
# Listing
# -----------------------------------------------------------------------------
alias ll="ls -la"
alias la="ls -A"
alias l="ls -CF"
alias lt="ls -ltr"  # Sort by time, newest last

# -----------------------------------------------------------------------------
# Safety
# -----------------------------------------------------------------------------
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"

# -----------------------------------------------------------------------------
# Git
# -----------------------------------------------------------------------------
alias g="git"
alias gs="git status"
alias gp="git pull"
alias gps="git push"
alias gc="git commit"
alias gca="git commit -a"
alias gcm="git commit -m"
alias gco="git checkout"
alias gb="git branch"
alias gba="git branch -a"
alias gd="git diff"
alias gds="git diff --staged"
alias gl="git log --oneline -20"
alias glg="git log --oneline --graph --decorate"
alias gst="git stash"
alias gstp="git stash pop"

# -----------------------------------------------------------------------------
# Docker
# -----------------------------------------------------------------------------
alias d="docker"
alias dc="docker compose"
alias dps="docker ps"
alias dpsa="docker ps -a"
alias di="docker images"
alias drm="docker rm"
alias drmi="docker rmi"
alias dex="docker exec -it"
alias dlogs="docker logs -f"
alias dprune="docker system prune -af"

# -----------------------------------------------------------------------------
# Kubernetes
# -----------------------------------------------------------------------------
alias k="kubectl"
alias kgp="kubectl get pods"
alias kgs="kubectl get svc"
alias kgn="kubectl get nodes"
alias kgd="kubectl get deployments"
alias kgi="kubectl get ingress"
alias kga="kubectl get all"
alias kaf="kubectl apply -f"
alias kdel="kubectl delete"
alias klog="kubectl logs -f"
alias kex="kubectl exec -it"
alias kctx="kubectx"
alias kns="kubens"

# -----------------------------------------------------------------------------
# Terraform
# -----------------------------------------------------------------------------
alias tf="terraform"
alias tfi="terraform init"
alias tfp="terraform plan"
alias tfa="terraform apply"
alias tfd="terraform destroy"
alias tfv="terraform validate"
alias tff="terraform fmt"
alias tfs="terraform state"

# -----------------------------------------------------------------------------
# AWS
# -----------------------------------------------------------------------------
alias awswho="aws sts get-caller-identity"
alias s3ls="aws s3 ls"
alias ec2ls="aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name,Tags[?Key==\`Name\`].Value|[0]]' --output table"

# -----------------------------------------------------------------------------
# Network
# -----------------------------------------------------------------------------
alias myip="curl -s ifconfig.me"
alias ports="netstat -tulanp"
alias listening="lsof -i -P -n | grep LISTEN"

# -----------------------------------------------------------------------------
# System
# -----------------------------------------------------------------------------
alias df="df -h"
alias du="du -h"
alias free="free -h"
alias top="htop"
alias reload="source ~/.zshrc"
alias path='echo $PATH | tr ":" "\\n"'
EOF
```

### Steg 3: Skapa functions-fil

```bash
cat > ~/dotfiles/shell/functions.sh << 'EOF'
# =============================================================================
# DevOps Shell Functions
# =============================================================================

# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------

# Create directory and cd into it
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Extract any archive
extract() {
    if [[ -f "$1" ]]; then
        case "$1" in
            *.tar.bz2) tar xjf "$1" ;;
            *.tar.gz)  tar xzf "$1" ;;
            *.tar.xz)  tar xJf "$1" ;;
            *.bz2)     bunzip2 "$1" ;;
            *.gz)      gunzip "$1" ;;
            *.tar)     tar xf "$1" ;;
            *.tbz2)    tar xjf "$1" ;;
            *.tgz)     tar xzf "$1" ;;
            *.zip)     unzip "$1" ;;
            *.Z)       uncompress "$1" ;;
            *)         echo "'$1' cannot be extracted" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

# -----------------------------------------------------------------------------
# Git Functions
# -----------------------------------------------------------------------------

# Git commit with message
gcmsg() {
    git commit -m "$*"
}

# Git add all and commit
gacp() {
    git add -A && git commit -m "$*" && git push
}

# Show git branch in all subdirectories
gitbranches() {
    for d in */; do
        if [[ -d "$d/.git" ]]; then
            echo -n "$d: "
            git -C "$d" branch --show-current
        fi
    done
}

# -----------------------------------------------------------------------------
# Docker Functions
# -----------------------------------------------------------------------------

# Execute bash in a running container
dsh() {
    docker exec -it "$1" /bin/bash || docker exec -it "$1" /bin/sh
}

# Remove all stopped containers
drmall() {
    docker rm $(docker ps -aq)
}

# Remove all unused images
drmiall() {
    docker rmi $(docker images -q --filter "dangling=true")
}

# -----------------------------------------------------------------------------
# Kubernetes Functions
# -----------------------------------------------------------------------------

# Get shell in a pod
ksh() {
    kubectl exec -it "$1" -- /bin/bash || kubectl exec -it "$1" -- /bin/sh
}

# Watch pods
kwatch() {
    watch -n 1 kubectl get pods "$@"
}

# Port forward
kpf() {
    kubectl port-forward "$1" "$2:$2"
}

# -----------------------------------------------------------------------------
# AWS Functions
# -----------------------------------------------------------------------------

# Switch AWS profile
awsp() {
    export AWS_PROFILE="$1"
    aws sts get-caller-identity
}

# List EC2 instances
ec2list() {
    aws ec2 describe-instances \\
        --query 'Reservations[].Instances[].[InstanceId,State.Name,PrivateIpAddress,Tags[?Key==`Name`].Value|[0]]' \\
        --output table
}

# SSH to EC2 by name tag
ec2ssh() {
    local ip=$(aws ec2 describe-instances \\
        --filters "Name=tag:Name,Values=$1" "Name=instance-state-name,Values=running" \\
        --query 'Reservations[0].Instances[0].PublicIpAddress' \\
        --output text)
    ssh ubuntu@"$ip"
}

# -----------------------------------------------------------------------------
# Development Functions
# -----------------------------------------------------------------------------

# Start a simple HTTP server
serve() {
    local port="${1:-8000}"
    python3 -m http.server "$port"
}

# JSON pretty print
jsonpp() {
    if [[ -t 0 ]]; then
        python3 -m json.tool "$@"
    else
        python3 -m json.tool
    fi
}

# Generate random password
genpass() {
    local length="${1:-32}"
    openssl rand -base64 48 | tr -dc 'a-zA-Z0-9!@#$%' | head -c "$length"
    echo
}
EOF
```

### Steg 4: Ladda aliases och functions

Lägg till i `~/.zshrc`:

```bash
cat >> ~/dotfiles/shell/zshrc << 'EOF'

# Load aliases and functions
[[ -f ~/dotfiles/shell/aliases.sh ]] && source ~/dotfiles/shell/aliases.sh
[[ -f ~/dotfiles/shell/functions.sh ]] && source ~/dotfiles/shell/functions.sh
EOF

source ~/.zshrc
```

## Verifiera att det fungerar

```bash
# Testa några aliases
ll
gs  # git status
k get pods  # kubectl get pods

# Testa funktioner
mkcd /tmp/test-directory
pwd  # /tmp/test-directory

genpass 16  # Random password
```

## Sammanfattning
Du har nu ett organiserat system för shell-aliases och functions. Dessa kommer spara dig tusentals tangenttryckningar över tid. Fortsätt bygga på dessa efterhand som du hittar mönster i ditt arbete.

## Nästa steg
- Lägg till projekt-specifika aliases
- Skapa functions för upprepade arbetsflöden
- Dela dina bästa aliases med teamet
"""
            },
            {
                "title": "Environment variables management",
                "difficulty": "medium",
                "estimated_minutes": 15,
                "xp_reward": 35,
                "content": """# Environment Variables Management

## Varför detta är viktigt
Environment variables är det säkra sättet att hantera konfiguration och hemligheter. Du använder dem för API-nycklar, databas-URLs, och feature flags. Att hårdkoda hemligheter i kod är en säkerhetsrisk — environment variables löser detta.

## Vad du kommer lära dig
- Förstå hur environment variables fungerar
- Hantera .env-filer säkert
- Använda direnv för automatisk miljökonfiguration

## Förutsättningar
- Shell konfigurerat
- Grundläggande terminalkunskap

## Steg-för-steg

### Steg 1: Förstå environment variables

```bash
# Visa alla environment variables
env

# Visa specifik variabel
echo $PATH
echo $HOME
echo $USER

# Sätta en variabel (bara i nuvarande shell)
export MY_VAR="hello"
echo $MY_VAR

# Variabeln försvinner när du stänger terminalen
```

### Steg 2: Permanenta variabler i .zshrc

```bash
# Lägg till i ~/.zshrc för permanenta variabler
cat >> ~/.zshrc << 'EOF'

# Custom Environment Variables
export EDITOR="code --wait"
export VISUAL="$EDITOR"

# Default AWS region
export AWS_DEFAULT_REGION="eu-north-1"

# Go
export GOPATH="$HOME/go"
export PATH="$GOPATH/bin:$PATH"

# Local bin
export PATH="$HOME/.local/bin:$HOME/bin:$PATH"
EOF

source ~/.zshrc
```

### Steg 3: Använda .env-filer

Skapa en `.env`-fil för projektspecifika variabler:

```bash
# .env (ALDRIG committa denna fil!)
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
API_KEY=sk-abc123...
DEBUG=true
```

Ladda .env i ditt shell-script:

```bash
# Metod 1: Source direkt (funkar i bash/zsh)
set -a  # Exportera automatiskt
source .env
set +a

# Metod 2: Med ett litet script
while IFS= read -r line; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    export "$line"
done < .env
```

### Steg 4: Installera och konfigurera direnv

direnv laddar automatiskt .envrc-filer när du cd:ar in i en mapp.

**Installation:**
```bash
# macOS
brew install direnv

# Ubuntu
sudo apt install direnv

# Lägg till i ~/.zshrc
eval "$(direnv hook zsh)"
```

**Användning:**
```bash
# Skapa .envrc i ditt projekt
cd ~/projects/my-app
cat > .envrc << 'EOF'
export DATABASE_URL="postgresql://localhost:5432/myapp"
export AWS_PROFILE="work"
export TF_VAR_environment="dev"
EOF

# Tillåt direnv att ladda filen
direnv allow

# Nu laddas variablerna automatiskt när du cd:ar hit
cd ~/projects/my-app
# direnv: loading .envrc
# direnv: export +AWS_PROFILE +DATABASE_URL +TF_VAR_environment
```

### Steg 5: Säker hemlighantering

**Aldrig committa hemligheter!**

```bash
# Lägg till i .gitignore
cat >> .gitignore << 'EOF'
.env
.env.*
!.env.example
.envrc
.direnv/
EOF

# Skapa en .env.example som mall
cat > .env.example << 'EOF'
# Copy this to .env and fill in values
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
API_KEY=your-api-key-here
EOF
```

**Bättre alternativ för produktion:**
- AWS Secrets Manager
- HashiCorp Vault
- 1Password CLI
- Doppler

### Steg 6: Environment variables i Docker

```dockerfile
# Dockerfile - bygg-tid variabler
ARG NODE_ENV=production
ENV NODE_ENV=$NODE_ENV

# docker-compose.yml - runtime variabler
services:
  app:
    environment:
      - DATABASE_URL
      - API_KEY=${API_KEY}
    env_file:
      - .env
```

## Vanliga problem

### Problem: "command not found" efter att ha lagt till i PATH
**Lösning:** Kör `source ~/.zshrc` eller öppna en ny terminal.

### Problem: Variable finns inte i subprocess
**Lösning:** Använd `export` — `VAR=value` utan export är bara lokalt.

### Problem: direnv laddar inte .envrc
**Lösning:** Kör `direnv allow` efter varje ändring i .envrc.

## Verifiera att det fungerar

```bash
# Testa direnv
cd ~/projects/my-app
echo $DATABASE_URL  # Ska visa URL:en

# Testa .env loading
cat > /tmp/test.env << 'EOF'
TEST_VAR=it_works
EOF
set -a && source /tmp/test.env && set +a
echo $TEST_VAR  # it_works
```

## Environment Variables Cheat Sheet

```bash
# Visa alla
env | sort

# Visa specifik
echo $VAR_NAME
printenv VAR_NAME

# Sätt temporär (bara detta kommando)
VAR=value command

# Sätt för session
export VAR=value

# Ta bort
unset VAR

# Kontrollera om satt
[[ -z "$VAR" ]] && echo "Not set"
[[ -n "$VAR" ]] && echo "Is set"
```

## Sammanfattning
Du förstår nu hur environment variables fungerar och har sätta upp direnv för automatisk miljökonfiguration. Använd alltid environment variables för konfiguration istället för att hårdkoda värden.

## Nästa steg
- Utforska AWS Secrets Manager för produktion
- Lär dig om 12-factor app principles
- Sätt upp secrets i CI/CD pipelines
"""
            },
        ],
        "labs": [
            {"title": "Terminal Power User Setup", "slug": "lab-1-1-terminal-setup", "hours": 2.0},
            {"title": "Complete Tool Chain Installation", "slug": "lab-1-2-tool-chain", "hours": 3.0},
            {"title": "SSH & Security Configuration", "slug": "lab-1-3-ssh-security", "hours": 2.0},
            {"title": "Dotfiles Repository Creation", "slug": "lab-1-4-dotfiles", "hours": 2.0},
        ],
        "project": {
            "title": "Development Environment as Code",
            "slug": "project-dev-environment-as-code",
            "description": "Create an automated setup script that installs your entire development environment on a new machine within 30 minutes.",
            "deliverables": [
                "Dotfiles repository on GitHub",
                "Automated setup script (bootstrap.sh)",
                "Tool verification checklist",
                "Environment documentation",
            ],
            "xp_reward": 500,
            "estimated_hours": 5.0,
        },
    },
    {
        "track_slug": "foundation",
        "order_index": 2,
        "name": "Linux Mastery",
        "slug": "linux-mastery",
        "description": "Deep understanding of Linux as the foundation for all DevOps infrastructure. Learn not just commands — understand why things work.",
        "difficulty": "intermediate",
        "estimated_hours": 20.0,
        "prerequisites": ["environment-tooling-setup"],
        "tasks": [
            {
                "title": "Filesystem Hierarchy Standard (FHS)",
                "difficulty": "medium",
                "estimated_minutes": 25,
                "xp_reward": 40,
                "content": """# Filesystem Hierarchy Standard (FHS)

## What is FHS?
The Filesystem Hierarchy Standard defines the directory structure on Linux systems. Understanding this is crucial for DevOps because you need to know where configuration files, logs, and applications live.

## The Root Directory Structure

```
/
├── bin/      → Essential user binaries (ls, cp, mv)
├── boot/     → Boot loader files, kernel
├── dev/      → Device files
├── etc/      → System configuration files
├── home/     → User home directories
├── lib/      → Essential shared libraries
├── media/    → Mount point for removable media
├── mnt/      → Temporary mount points
├── opt/      → Optional/third-party software
├── proc/     → Virtual filesystem for process info
├── root/     → Root user's home directory
├── run/      → Runtime data (PIDs, sockets)
├── sbin/     → System binaries (systemctl, fdisk)
├── srv/      → Service data
├── sys/      → Virtual filesystem for kernel/hardware
├── tmp/      → Temporary files (cleared on reboot)
├── usr/      → User programs and data
└── var/      → Variable data (logs, databases)
```

## Key Directories for DevOps

### /etc - Configuration Files
```bash
/etc/nginx/nginx.conf      # Nginx config
/etc/ssh/sshd_config       # SSH server config
/etc/hosts                  # Local DNS
/etc/passwd                 # User accounts
/etc/systemd/system/       # Custom service files
```

### /var - Variable Data
```bash
/var/log/                  # System and app logs
/var/lib/docker/           # Docker data
/var/www/                  # Web server files
/var/run/ → /run/          # Runtime data (symlink)
```

### /usr - User Programs
```bash
/usr/local/bin/            # Locally installed binaries
/usr/share/                # Shared data
/usr/lib/                  # Libraries
```

### /opt - Third-party Software
```bash
/opt/prometheus/           # Prometheus installation
/opt/grafana/              # Grafana installation
```

## DevOps Best Practices

1. **Never modify /bin, /sbin, /lib** - These are managed by package manager
2. **Use /opt** for manually installed tools
3. **Use /etc** for configuration (and version control it!)
4. **Check /var/log** first when debugging

## Exercise
1. Run `ls -la /` and identify each directory
2. Find your SSH config: `cat /etc/ssh/sshd_config`
3. Check disk usage: `du -sh /var/log`
4. List running services' PIDs: `ls /run/*.pid`
"""
            },
            {
                "title": "Mount points and device files",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# Mount Points and Device Files

## Understanding Device Files

In Linux, **everything is a file** - including hardware devices!

### Device Files Location: /dev
```bash
/dev/sda      → First SATA/SCSI disk
/dev/sda1     → First partition on sda
/dev/nvme0n1  → First NVMe drive
/dev/null     → Discards all data written to it
/dev/zero     → Returns zeros when read
/dev/random   → Random number generator
```

## Block vs Character Devices

```bash
ls -la /dev/sda /dev/tty
brw-rw---- 1 root disk  8, 0 Nov 27 10:00 /dev/sda    # 'b' = block
crw-rw-rw- 1 root tty   5, 0 Nov 27 10:00 /dev/tty    # 'c' = character
```

- **Block devices (b)**: Read/write in blocks (disks, USB drives)
- **Character devices (c)**: Read/write one character at a time (terminals, keyboards)

## Mount Points

A mount point is a directory where a filesystem is attached.

### View Current Mounts
```bash
# Show all mounts
mount

# Show disk mounts only
df -h

# Show mount points clearly
lsblk
```

### Mounting a Filesystem
```bash
# Mount a USB drive
sudo mount /dev/sdb1 /mnt/usb

# Mount with specific type
sudo mount -t ext4 /dev/sdb1 /mnt/data

# Mount read-only
sudo mount -o ro /dev/sdb1 /mnt/backup

# Unmount
sudo umount /mnt/usb
```

## Persistent Mounts: /etc/fstab

The `/etc/fstab` file defines mounts that happen at boot.

```bash
# /etc/fstab structure:
# <device>        <mount point>  <type>  <options>      <dump> <pass>
UUID=abc123       /              ext4    defaults       0      1
/dev/sdb1         /data          xfs     defaults,noatime 0    2
```

### Find UUID of a Device
```bash
sudo blkid
# or
ls -la /dev/disk/by-uuid/
```

## Common Mount Options
| Option | Description |
|--------|-------------|
| defaults | rw, suid, dev, exec, auto, nouser, async |
| noatime | Don't update access time (performance) |
| ro | Read-only |
| rw | Read-write |
| noexec | Can't execute binaries |

## DevOps Relevance
- **Docker**: Uses mount namespaces for isolation
- **Kubernetes**: PersistentVolumes are mounted into pods
- **AWS EBS**: Attached as /dev/xvd* devices

## Exercise
1. Run `lsblk` to see your disk layout
2. Run `df -h` to see disk usage by mount
3. Check `/etc/fstab` on a Linux system
4. Try `mount | grep -E "^/dev"` to see real device mounts
"""
            },
            {
                "title": "Inodes, hard links, symbolic links",
                "difficulty": "medium",
                "estimated_minutes": 25,
                "xp_reward": 45,
                "content": """# Inodes, Hard Links, and Symbolic Links

## What is an Inode?

An **inode** (index node) is a data structure that stores metadata about a file:
- File size
- Owner/group
- Permissions
- Timestamps
- **Location of data blocks**

The inode does NOT store the filename - that's stored in the directory!

### View Inode Information
```bash
# See inode numbers
ls -li

# Detailed inode info
stat filename.txt

# Count inodes
df -i
```

## Hard Links

A **hard link** is another name for the same file (same inode).

```bash
# Create original file
echo "Hello" > original.txt
ls -li original.txt
# 12345 -rw-r--r-- 1 user user 6 Nov 27 10:00 original.txt
#  ^inode          ^link count

# Create hard link
ln original.txt hardlink.txt
ls -li
# 12345 -rw-r--r-- 2 user user 6 Nov 27 10:00 hardlink.txt
# 12345 -rw-r--r-- 2 user user 6 Nov 27 10:00 original.txt
# Same inode! Link count is now 2
```

### Hard Link Characteristics
- ✅ Same inode number
- ✅ Editing one edits both
- ✅ Deleting original doesn't delete data
- ❌ Cannot cross filesystems
- ❌ Cannot link to directories

## Symbolic Links (Symlinks)

A **symbolic link** is a separate file that points to another path.

```bash
# Create symlink
ln -s /path/to/original.txt symlink.txt

ls -li
# 12345 -rw-r--r-- 1 user user 6 Nov 27 10:00 original.txt
# 67890 lrwxrwxrwx 1 user user 22 Nov 27 10:00 symlink.txt -> /path/to/original.txt
# Different inode! 'l' means link
```

### Symlink Characteristics
- ✅ Can cross filesystems
- ✅ Can link to directories
- ✅ Can see what it points to
- ❌ Breaks if target is deleted (dangling link)
- ❌ Different inode number

## Comparison Table

| Feature | Hard Link | Symbolic Link |
|---------|-----------|---------------|
| Same inode | ✅ Yes | ❌ No |
| Cross filesystem | ❌ No | ✅ Yes |
| Link to directory | ❌ No | ✅ Yes |
| Target deleted | Still works | Breaks |
| `ls -l` shows | File type | l + path |

## DevOps Use Cases

### Symlinks (Common)
```bash
# Current version pointing
ln -s /opt/app-v1.2.3 /opt/app-current

# Log rotation
ln -s /var/log/nginx/access.log /home/user/nginx.log

# Alternative binaries
ln -s /usr/bin/python3 /usr/bin/python
```

### Hard Links (Rare)
```bash
# Backup systems (like rsync with --link-dest)
# Same file stored once, appears in multiple backups
```

## Exercise
1. Create a file and check its inode: `echo "test" > file.txt && ls -li file.txt`
2. Create a hard link: `ln file.txt hardlink.txt && ls -li`
3. Create a symlink: `ln -s file.txt symlink.txt && ls -li`
4. Delete original and test both links
"""
            },
            {"title": "Disk management (fdisk, lvm, df, du)", "difficulty": "hard", "estimated_minutes": 30, "xp_reward": 55},
            {
                "title": "File permissions (chmod, chown, umask, ACLs)",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 50,
                "content": """# File Permissions: chmod, chown, umask, ACLs

## Understanding Linux Permissions

Every file has three permission sets for three user categories:

```bash
ls -la file.txt
-rw-r--r-- 1 owner group 1234 Nov 27 10:00 file.txt
│└┬┘└┬┘└┬┘
│ │  │  └── Others (everyone else)
│ │  └───── Group
│ └──────── Owner/User
└────────── File type (- = file, d = directory, l = link)
```

### Permission Types
- **r** (read) = 4
- **w** (write) = 2
- **x** (execute) = 1

## chmod - Change Mode

### Numeric Method (Octal)
```bash
# rwxr-xr-x = 755
chmod 755 script.sh

# rw-r--r-- = 644
chmod 644 file.txt

# rwx------ = 700
chmod 700 private.sh

# Common values:
# 755 - Scripts, executables
# 644 - Regular files
# 600 - Private files (SSH keys!)
# 777 - NEVER use this! Security risk
```

### Symbolic Method
```bash
# Add execute for owner
chmod u+x script.sh

# Remove write for group and others
chmod go-w file.txt

# Set exact permissions
chmod u=rwx,g=rx,o=r script.sh

# Add execute for all
chmod a+x script.sh
```

## chown - Change Owner

```bash
# Change owner
sudo chown newuser file.txt

# Change owner and group
sudo chown newuser:newgroup file.txt

# Change group only
sudo chown :newgroup file.txt

# Recursive (all files in directory)
sudo chown -R www-data:www-data /var/www/
```

## umask - Default Permissions

The umask **subtracts** from default permissions (666 for files, 777 for directories).

```bash
# Check current umask
umask
# 022 means: 666-022=644 for files, 777-022=755 for dirs

# Set stricter umask
umask 027
# Files: 666-027=640 (rw-r-----)
# Dirs: 777-027=750 (rwxr-x---)

# Set in ~/.bashrc for persistence
echo "umask 027" >> ~/.bashrc
```

## ACLs - Access Control Lists

ACLs provide more granular permissions beyond owner/group/other.

```bash
# Check if ACLs are supported
mount | grep acl

# View ACLs
getfacl file.txt

# Grant user specific access
setfacl -m u:username:rw file.txt

# Grant group specific access
setfacl -m g:devteam:r file.txt

# Remove ACL entry
setfacl -x u:username file.txt

# Remove all ACLs
setfacl -b file.txt
```

## DevOps Permission Scenarios

### Web Server Files
```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
sudo chmod -R 644 /var/www/html/*.html
```

### SSH Keys (CRITICAL!)
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 644 ~/.ssh/authorized_keys
```

### Application Secrets
```bash
chmod 600 .env
chmod 600 config/secrets.yml
```

## Exercise
1. Create a file and check permissions: `touch test.sh && ls -la test.sh`
2. Make it executable: `chmod +x test.sh`
3. Try numeric: `chmod 644 test.sh && ls -la test.sh`
4. Check your umask: `umask`
"""
            },
            {
                "title": "Process lifecycle and states",
                "difficulty": "medium",
                "estimated_minutes": 20,
                "xp_reward": 40,
                "content": """# Process Lifecycle and States

## What is a Process?

A **process** is a running instance of a program. Every process has:
- **PID**: Process ID (unique number)
- **PPID**: Parent Process ID
- **UID**: User who owns it
- **State**: Current status

## Process States

```
RUNNING (R)     ←→   INTERRUPTIBLE SLEEP (S)
     ↓                        ↓
STOPPED (T)     ←→   UNINTERRUPTIBLE SLEEP (D)
     ↓
ZOMBIE (Z)
```

### State Meanings
| State | Symbol | Description |
|-------|--------|-------------|
| Running | R | Currently executing on CPU |
| Sleeping | S | Waiting for event (can be interrupted) |
| Disk Sleep | D | Waiting for I/O (cannot be interrupted) |
| Stopped | T | Paused (e.g., Ctrl+Z) |
| Zombie | Z | Finished but parent hasn't collected exit status |

### View Process States
```bash
ps aux
# USER  PID %CPU %MEM  VSZ  RSS TTY STAT START TIME COMMAND
# root    1  0.0  0.1 1234 5678 ?   Ss   10:00 0:01 /sbin/init
#                                    ^^
#                                    ||__ s = session leader
#                                    |___ S = sleeping
```

## Process Lifecycle

### 1. Creation (fork + exec)
```bash
# When you run a command:
$ ls
# Shell calls fork() → creates child process
# Child calls exec() → replaces itself with 'ls'
```

### 2. Running
Process executes on CPU, scheduled by kernel.

### 3. Waiting
Process waits for I/O, user input, or timer.

### 4. Termination
Process calls exit(), parent collects status with wait().

### 5. Zombie (if parent doesn't collect)
```bash
# Find zombies
ps aux | grep Z

# Zombie processes have 'Z' state
# They consume no resources except a PID table entry
```

## Process Tree

```bash
# View process tree
pstree -p

# Output:
# systemd(1)─┬─sshd(1234)───sshd(5678)───bash(9012)───vim(3456)
#            ├─nginx(2345)─┬─nginx(2346)
#            │             └─nginx(2347)
#            └─docker(3456)───containerd(4567)
```

## Key Process Facts

1. **PID 1 is special**: Always `init` or `systemd`, parent of all processes
2. **Orphan processes**: Adopted by PID 1 when parent dies
3. **Zombie processes**: Dead but waiting for parent to acknowledge

## DevOps Relevance

### Container Init Process
```bash
# In Docker, PID 1 must handle signals properly
# That's why we use tini or dumb-init
CMD ["tini", "--", "python", "app.py"]
```

### Zombie Processes in Containers
```bash
# If container's PID 1 doesn't reap children, zombies accumulate
# Check for zombies:
docker exec container_name ps aux | grep Z
```

## Exercise
1. Run `ps aux` and identify different states
2. Run `pstree -p` to see process hierarchy
3. Open vim, press Ctrl+Z, then run `ps aux | grep vim` (should show T state)
4. Type `fg` to resume vim, then `:q` to exit
"""
            },
            {"title": "Foreground vs background processes", "difficulty": "medium", "estimated_minutes": 15, "xp_reward": 35},
            {"title": "Job control (jobs, fg, bg, nohup)", "difficulty": "medium", "estimated_minutes": 20, "xp_reward": 40},
            {"title": "Signals (SIGTERM, SIGKILL, SIGHUP)", "difficulty": "medium", "estimated_minutes": 20, "xp_reward": 40},
            {"title": "Process monitoring (ps, top, htop, pgrep)", "difficulty": "medium", "estimated_minutes": 20, "xp_reward": 40},
            {"title": "Systemd architecture", "difficulty": "hard", "estimated_minutes": 30, "xp_reward": 55},
            {"title": "Unit files (service, timer, socket)", "difficulty": "hard", "estimated_minutes": 25, "xp_reward": 50},
            {"title": "Service management (systemctl)", "difficulty": "medium"},
            {"title": "Boot process and targets", "difficulty": "hard"},
            {"title": "Journald and logging", "difficulty": "medium"},
            {"title": "User/group management", "difficulty": "medium"},
            {"title": "sudo configuration", "difficulty": "medium"},
            {"title": "PAM modules", "difficulty": "hard"},
            {"title": "SSH hardening", "difficulty": "hard"},
            {"title": "Firewall basics (ufw, iptables)", "difficulty": "hard"},
            {"title": "grep, sed, awk mastery", "difficulty": "hard"},
            {"title": "cut, sort, uniq, tr", "difficulty": "medium"},
            {"title": "xargs and command substitution", "difficulty": "hard"},
            {"title": "Regular expressions", "difficulty": "hard"},
            {"title": "Network interfaces (ip, ifconfig)", "difficulty": "medium"},
            {"title": "DNS resolution (dig, nslookup)", "difficulty": "medium"},
            {"title": "Socket inspection (ss, netstat)", "difficulty": "medium"},
            {"title": "Traffic analysis (tcpdump basics)", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "Filesystem Exploration Challenge", "slug": "lab-2-1-filesystem", "hours": 3.0},
            {"title": "Process Detective", "slug": "lab-2-2-processes", "hours": 2.0},
            {"title": "Systemd Service Creation", "slug": "lab-2-3-systemd", "hours": 3.0},
            {"title": "User Security Hardening", "slug": "lab-2-4-security", "hours": 2.0},
            {"title": "Text Processing Olympics", "slug": "lab-2-5-text-processing", "hours": 4.0},
            {"title": "Network Troubleshooting", "slug": "lab-2-6-networking", "hours": 3.0},
        ],
        "project": {
            "title": "Linux System Administration",
            "slug": "project-linux-sysadmin",
            "description": "Configure a Linux server from scratch with hardened SSH, custom systemd services, log rotation, automated backups, and monitoring scripts.",
            "deliverables": [
                "Server configuration documentation",
                "Security hardening checklist",
                "Custom systemd unit files",
                "System monitoring script",
            ],
            "xp_reward": 750,
            "estimated_hours": 8.0,
        },
    },
    {
        "track_slug": "foundation",
        "order_index": 3,
        "name": "Shell Scripting & Automation",
        "slug": "shell-scripting-automation",
        "description": "Transform manual processes into automated, reliable scripts. Build tools that save hours of work.",
        "difficulty": "intermediate",
        "estimated_hours": 20.0,
        "prerequisites": ["linux-mastery"],
        "tasks": [
            {"title": "Shebang and script execution", "difficulty": "easy"},
            {"title": "Variables (local, global, environment)", "difficulty": "medium"},
            {"title": "Quoting rules (single, double, backticks)", "difficulty": "medium"},
            {"title": "Exit codes and error handling", "difficulty": "medium"},
            {"title": "set options (-e, -u, -x, -o pipefail)", "difficulty": "medium"},
            {"title": "Conditionals (if, case, [[]])", "difficulty": "medium"},
            {"title": "Loops (for, while, until)", "difficulty": "medium"},
            {"title": "Functions and return values", "difficulty": "medium"},
            {"title": "Traps and signal handling", "difficulty": "hard"},
            {"title": "Subshells and command grouping", "difficulty": "hard"},
            {"title": "Here documents and here strings", "difficulty": "medium"},
            {"title": "Process substitution", "difficulty": "hard"},
            {"title": "Arrays (indexed, associative)", "difficulty": "hard"},
            {"title": "String manipulation", "difficulty": "medium"},
            {"title": "Arithmetic operations", "difficulty": "medium"},
            {"title": "Log monitoring and alerting", "difficulty": "hard"},
            {"title": "Backup automation", "difficulty": "hard"},
            {"title": "System health checks", "difficulty": "medium"},
            {"title": "User provisioning scripts", "difficulty": "hard"},
            {"title": "Deployment scripts", "difficulty": "hard"},
            {"title": "ShellCheck for linting", "difficulty": "easy"},
            {"title": "Unit testing with BATS", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "Bash Fundamentals Exercises", "slug": "lab-3-1-bash-fundamentals", "hours": 3.0},
            {"title": "Control Flow Challenges", "slug": "lab-3-2-control-flow", "hours": 3.0},
            {"title": "Log Monitor with Email Alerts", "slug": "lab-3-3-log-monitor", "hours": 4.0},
            {"title": "Automated Backup System", "slug": "lab-3-4-backup-system", "hours": 3.0},
            {"title": "System Health Dashboard", "slug": "lab-3-5-health-dashboard", "hours": 4.0},
        ],
        "project": {
            "title": "DevOps Automation Toolkit",
            "slug": "project-automation-toolkit",
            "description": "Create a complete toolkit with server provisioning, automated backup with rotation, log analyzer with alerting, and deployment script with rollback.",
            "deliverables": [
                "5+ production-ready scripts",
                "Function library",
                "Documentation for each script",
                "Test suite with BATS",
            ],
            "xp_reward": 750,
            "estimated_hours": 8.0,
        },
    },
    {
        "track_slug": "foundation",
        "order_index": 4,
        "name": "Git & Collaborative Workflows",
        "slug": "git-collaborative-workflows",
        "description": "Master version control and collaboration workflows used by professional teams. Git is the foundation for all modern software development and DevOps.",
        "difficulty": "intermediate",
        "estimated_hours": 15.0,
        "prerequisites": ["environment-tooling-setup"],
        "tasks": [
            {"title": "Git object model (blobs, trees, commits)", "difficulty": "hard"},
            {"title": "References and HEAD", "difficulty": "medium"},
            {"title": "Index (staging area)", "difficulty": "medium"},
            {"title": "Packfiles and garbage collection", "difficulty": "hard"},
            {"title": "Feature branches", "difficulty": "easy"},
            {"title": "GitFlow workflow", "difficulty": "medium"},
            {"title": "Trunk-based development", "difficulty": "medium"},
            {"title": "Release branches", "difficulty": "medium"},
            {"title": "Hotfix management", "difficulty": "medium"},
            {"title": "Interactive rebase", "difficulty": "hard"},
            {"title": "Cherry-picking", "difficulty": "medium"},
            {"title": "Bisect for debugging", "difficulty": "hard"},
            {"title": "Reflog and recovery", "difficulty": "hard"},
            {"title": "Submodules and subtrees", "difficulty": "hard"},
            {"title": "Pull requests and code review", "difficulty": "medium"},
            {"title": "Branch protection rules", "difficulty": "medium"},
            {"title": "Merge strategies (merge, squash, rebase)", "difficulty": "medium"},
            {"title": "Conflict resolution", "difficulty": "medium"},
            {"title": "Git hooks", "difficulty": "hard"},
            {"title": "GitHub Issues and Projects", "difficulty": "easy"},
            {"title": "GitHub Actions basics", "difficulty": "medium"},
            {"title": "GitHub CLI", "difficulty": "easy"},
        ],
        "labs": [
            {"title": "Git Internals Exploration", "slug": "lab-4-1-git-internals", "hours": 2.0},
            {"title": "Branching Strategy Simulation", "slug": "lab-4-2-branching", "hours": 3.0},
            {"title": "Conflict Resolution Scenarios", "slug": "lab-4-3-conflicts", "hours": 2.0},
            {"title": "Rebase and History Rewriting", "slug": "lab-4-4-rebase", "hours": 3.0},
            {"title": "Pull Request Workflow", "slug": "lab-4-5-pull-requests", "hours": 3.0},
        ],
        "project": {
            "title": "Team Collaboration Simulation",
            "slug": "project-team-collaboration",
            "description": "Simulate a team project with multiple branches, pull requests with review, conflict resolution, release management, and protected main branch.",
            "deliverables": [
                "Git workflow documentation",
                "Contribution guidelines (CONTRIBUTING.md)",
                "Branch protection configuration",
                "Release process documentation",
            ],
            "xp_reward": 600,
            "estimated_hours": 6.0,
        },
    },
    {
        "track_slug": "foundation",
        "order_index": 5,
        "name": "Python for DevOps",
        "slug": "python-for-devops",
        "description": "Python is the dominant language for DevOps automation. Learn to build tools that interact with cloud APIs, automate infrastructure, and process data.",
        "difficulty": "intermediate",
        "estimated_hours": 25.0,
        "prerequisites": ["shell-scripting-automation"],
        "tasks": [
            {"title": "Data types and structures", "difficulty": "easy"},
            {"title": "Functions and decorators", "difficulty": "medium"},
            {"title": "Classes and OOP basics", "difficulty": "medium"},
            {"title": "Exception handling", "difficulty": "medium"},
            {"title": "Virtual environments", "difficulty": "easy"},
            {"title": "boto3 (AWS SDK)", "difficulty": "hard"},
            {"title": "requests (HTTP client)", "difficulty": "medium"},
            {"title": "paramiko (SSH)", "difficulty": "hard"},
            {"title": "jinja2 (templating)", "difficulty": "medium"},
            {"title": "pyyaml and json", "difficulty": "easy"},
            {"title": "Configuration management patterns", "difficulty": "medium"},
            {"title": "Secret handling", "difficulty": "hard"},
            {"title": "Logging and monitoring", "difficulty": "medium"},
            {"title": "Error handling strategies", "difficulty": "medium"},
            {"title": "Retry logic", "difficulty": "medium"},
            {"title": "argparse fundamentals", "difficulty": "medium"},
            {"title": "Click framework", "difficulty": "medium"},
            {"title": "Rich for beautiful output", "difficulty": "easy"},
            {"title": "REST API consumption", "difficulty": "medium"},
            {"title": "Authentication (API keys, OAuth)", "difficulty": "hard"},
            {"title": "Rate limiting handling", "difficulty": "hard"},
            {"title": "pytest fundamentals", "difficulty": "medium"},
            {"title": "Mocking external services", "difficulty": "hard"},
            {"title": "Type hints and mypy", "difficulty": "medium"},
            {"title": "Black and flake8", "difficulty": "easy"},
        ],
        "labs": [
            {"title": "Python Fundamentals Review", "slug": "lab-5-1-python-fundamentals", "hours": 3.0},
            {"title": "AWS Resource Manager with boto3", "slug": "lab-5-2-boto3", "hours": 4.0},
            {"title": "CLI Tool with Click", "slug": "lab-5-3-cli-click", "hours": 3.0},
            {"title": "REST API Client", "slug": "lab-5-4-rest-api", "hours": 3.0},
            {"title": "Configuration Manager", "slug": "lab-5-5-config-manager", "hours": 3.0},
            {"title": "Testing Your Tools", "slug": "lab-5-6-testing", "hours": 3.0},
        ],
        "project": {
            "title": "AWS Automation Suite",
            "slug": "project-aws-automation-suite",
            "description": "Build a complete automation suite: EC2 instance manager, S3 backup tool, IAM user provisioning, cost reporter, and resource tagger.",
            "deliverables": [
                "Python package with 5+ tools",
                "CLI interface",
                "Unit tests (80%+ coverage)",
                "Documentation",
                "PyPI-ready setup",
            ],
            "xp_reward": 1000,
            "estimated_hours": 10.0,
        },
    },

    # =========================================================================
    # TRACK 2: CLOUD & INFRASTRUCTURE (Modules 06-09)
    # =========================================================================
    {
        "track_slug": "cloud-infrastructure",
        "order_index": 6,
        "name": "AWS Core Services",
        "slug": "aws-core-services",
        "description": "Master AWS fundamental services that form the foundation for all cloud infrastructure. Build real production architecture.",
        "difficulty": "advanced",
        "estimated_hours": 25.0,
        "prerequisites": ["python-for-devops"],
        "tasks": [
            {"title": "Global infrastructure (regions, AZs)", "difficulty": "easy"},
            {"title": "Account setup and Organizations", "difficulty": "medium"},
            {"title": "Cost management and budgets", "difficulty": "medium"},
            {"title": "Well-Architected Framework intro", "difficulty": "medium"},
            {"title": "IAM users, groups, roles", "difficulty": "medium"},
            {"title": "IAM policies (managed, inline, custom)", "difficulty": "hard"},
            {"title": "Policy evaluation logic", "difficulty": "hard"},
            {"title": "Cross-account access", "difficulty": "hard"},
            {"title": "VPC CIDR planning", "difficulty": "medium"},
            {"title": "Subnets (public, private)", "difficulty": "medium"},
            {"title": "Internet Gateway", "difficulty": "medium"},
            {"title": "NAT Gateway/Instance", "difficulty": "medium"},
            {"title": "Route tables", "difficulty": "medium"},
            {"title": "Security Groups vs NACLs", "difficulty": "hard"},
            {"title": "VPC Peering", "difficulty": "hard"},
            {"title": "VPC Endpoints", "difficulty": "hard"},
            {"title": "EC2 instance types and selection", "difficulty": "medium"},
            {"title": "AMIs (Amazon Machine Images)", "difficulty": "medium"},
            {"title": "Key pairs and SSH", "difficulty": "easy"},
            {"title": "User data scripts", "difficulty": "medium"},
            {"title": "EBS volumes", "difficulty": "medium"},
            {"title": "ALB, NLB, CLB differences", "difficulty": "hard"},
            {"title": "Target groups and health checks", "difficulty": "medium"},
            {"title": "Auto Scaling groups", "difficulty": "hard"},
            {"title": "S3 bucket configuration", "difficulty": "medium"},
            {"title": "S3 storage classes", "difficulty": "medium"},
            {"title": "S3 lifecycle policies", "difficulty": "medium"},
            {"title": "S3 versioning and encryption", "difficulty": "medium"},
        ],
        "labs": [
            {"title": "Multi-AZ VPC from Scratch", "slug": "lab-6-1-vpc", "hours": 4.0},
            {"title": "IAM Policy Workshop", "slug": "lab-6-2-iam", "hours": 3.0},
            {"title": "EC2 Fleet Deployment", "slug": "lab-6-3-ec2", "hours": 3.0},
            {"title": "Load Balanced Application", "slug": "lab-6-4-load-balancing", "hours": 4.0},
            {"title": "Auto Scaling Configuration", "slug": "lab-6-5-auto-scaling", "hours": 3.0},
            {"title": "S3 Static Website", "slug": "lab-6-6-s3-website", "hours": 2.0},
        ],
        "project": {
            "title": "Three-Tier Web Architecture",
            "slug": "project-three-tier-architecture",
            "description": "Build a complete three-tier application: VPC with public/private subnets, ALB + Auto Scaling web tier, application tier, RDS database tier, and bastion host.",
            "deliverables": [
                "Architecture diagram",
                "VPC configuration documentation",
                "Security group rules matrix",
                "Cost estimation",
                "Disaster recovery plan",
            ],
            "xp_reward": 1000,
            "estimated_hours": 12.0,
        },
    },
    {
        "track_slug": "cloud-infrastructure",
        "order_index": 7,
        "name": "Infrastructure as Code (Terraform)",
        "slug": "infrastructure-as-code-terraform",
        "description": "Infrastructure as code with Terraform — the industry standard for cloud provisioning. Manage complex infrastructure reproducibly and safely.",
        "difficulty": "advanced",
        "estimated_hours": 25.0,
        "prerequisites": ["aws-core-services"],
        "tasks": [
            {"title": "Declarative vs imperative IaC", "difficulty": "easy"},
            {"title": "Provider architecture", "difficulty": "medium"},
            {"title": "Resources and data sources", "difficulty": "medium"},
            {"title": "Variables and outputs", "difficulty": "medium"},
            {"title": "terraform init, plan, apply, destroy", "difficulty": "easy"},
            {"title": "Expressions and functions", "difficulty": "medium"},
            {"title": "Conditionals and loops (count, for_each)", "difficulty": "hard"},
            {"title": "Dynamic blocks", "difficulty": "hard"},
            {"title": "Local values", "difficulty": "medium"},
            {"title": "Type constraints", "difficulty": "medium"},
            {"title": "Local vs remote state", "difficulty": "medium"},
            {"title": "S3 + DynamoDB backend", "difficulty": "hard"},
            {"title": "State locking", "difficulty": "hard"},
            {"title": "terraform state commands", "difficulty": "hard"},
            {"title": "Importing existing resources", "difficulty": "hard"},
            {"title": "Module structure", "difficulty": "medium"},
            {"title": "Module sources (local, registry, git)", "difficulty": "medium"},
            {"title": "Module versioning", "difficulty": "medium"},
            {"title": "Workspace concept", "difficulty": "medium"},
            {"title": "Environment separation strategies", "difficulty": "hard"},
            {"title": "terraform validate", "difficulty": "easy"},
            {"title": "tflint and tfsec", "difficulty": "medium"},
            {"title": "Terratest basics", "difficulty": "hard"},
            {"title": "GitHub Actions integration", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "First Terraform Project", "slug": "lab-7-1-first-terraform", "hours": 3.0},
            {"title": "Variables and Outputs", "slug": "lab-7-2-variables", "hours": 2.0},
            {"title": "Remote State Setup", "slug": "lab-7-3-remote-state", "hours": 2.0},
            {"title": "Creating Modules", "slug": "lab-7-4-modules", "hours": 4.0},
            {"title": "Multi-Environment Setup", "slug": "lab-7-5-multi-env", "hours": 4.0},
            {"title": "CI/CD Pipeline for Terraform", "slug": "lab-7-6-cicd", "hours": 4.0},
        ],
        "project": {
            "title": "Complete AWS Infrastructure with Terraform",
            "slug": "project-terraform-aws",
            "description": "Build Module 06 architecture with Terraform: reusable VPC module, EC2 module with ASG, ALB module, RDS module, multi-environment (dev, staging, prod), remote state, and GitHub Actions deployment.",
            "deliverables": [
                "Terraform module library",
                "Environment configurations",
                "CI/CD pipeline",
                "Documentation (README per module)",
                "Cost tagging strategy",
            ],
            "xp_reward": 1000,
            "estimated_hours": 12.0,
        },
    },
    {
        "track_slug": "cloud-infrastructure",
        "order_index": 8,
        "name": "Serverless Architecture",
        "slug": "serverless-architecture",
        "description": "Build event-driven, serverless applications with AWS Lambda. Design cost-effective, scalable solutions without server management.",
        "difficulty": "advanced",
        "estimated_hours": 20.0,
        "prerequisites": ["infrastructure-as-code-terraform"],
        "tasks": [
            {"title": "Serverless vs traditional", "difficulty": "easy"},
            {"title": "AWS Lambda architecture", "difficulty": "medium"},
            {"title": "Execution model and cold starts", "difficulty": "medium"},
            {"title": "Lambda pricing model", "difficulty": "easy"},
            {"title": "Function handlers", "difficulty": "medium"},
            {"title": "Event and context objects", "difficulty": "medium"},
            {"title": "Environment variables", "difficulty": "easy"},
            {"title": "Lambda layers", "difficulty": "hard"},
            {"title": "Packaging and dependencies", "difficulty": "medium"},
            {"title": "Local development (SAM, LocalStack)", "difficulty": "hard"},
            {"title": "API Gateway integration", "difficulty": "medium"},
            {"title": "S3 triggers", "difficulty": "medium"},
            {"title": "SQS triggers", "difficulty": "medium"},
            {"title": "SNS triggers", "difficulty": "medium"},
            {"title": "EventBridge rules", "difficulty": "hard"},
            {"title": "DynamoDB Streams", "difficulty": "hard"},
            {"title": "Step Functions orchestration", "difficulty": "hard"},
            {"title": "Fan-out/fan-in patterns", "difficulty": "hard"},
            {"title": "Dead letter queues", "difficulty": "medium"},
            {"title": "Idempotency", "difficulty": "hard"},
            {"title": "IAM execution roles", "difficulty": "medium"},
            {"title": "Secrets Manager integration", "difficulty": "medium"},
            {"title": "CloudWatch Logs and X-Ray", "difficulty": "medium"},
        ],
        "labs": [
            {"title": "First Lambda Function", "slug": "lab-8-1-first-lambda", "hours": 2.0},
            {"title": "API Gateway + Lambda", "slug": "lab-8-2-api-gateway", "hours": 3.0},
            {"title": "S3 Event Processing", "slug": "lab-8-3-s3-events", "hours": 3.0},
            {"title": "Step Functions Workflow", "slug": "lab-8-4-step-functions", "hours": 4.0},
            {"title": "SQS Message Processing", "slug": "lab-8-5-sqs", "hours": 3.0},
            {"title": "Lambda with Terraform", "slug": "lab-8-6-lambda-terraform", "hours": 3.0},
        ],
        "project": {
            "title": "Serverless Data Pipeline",
            "slug": "project-serverless-pipeline",
            "description": "Build a complete data processing pipeline: S3 trigger for file upload, Lambda for transformation, Step Functions for orchestration, DynamoDB for state, SNS for notifications, all with Terraform.",
            "deliverables": [
                "Architecture diagram",
                "Lambda functions",
                "Step Functions definition",
                "Terraform code",
                "Monitoring dashboard",
                "Cost analysis",
            ],
            "xp_reward": 1000,
            "estimated_hours": 10.0,
        },
    },
    {
        "track_slug": "cloud-infrastructure",
        "order_index": 9,
        "name": "Networking & Security",
        "slug": "networking-security",
        "description": "Deep dive into network architecture and security practices critical for enterprise-grade infrastructure.",
        "difficulty": "advanced",
        "estimated_hours": 20.0,
        "prerequisites": ["aws-core-services"],
        "tasks": [
            {"title": "Transit Gateway", "difficulty": "hard"},
            {"title": "PrivateLink", "difficulty": "hard"},
            {"title": "Direct Connect basics", "difficulty": "hard"},
            {"title": "VPN connections", "difficulty": "hard"},
            {"title": "Route 53 DNS", "difficulty": "medium"},
            {"title": "CloudFront CDN", "difficulty": "medium"},
            {"title": "Security groups deep dive", "difficulty": "medium"},
            {"title": "Network ACLs", "difficulty": "medium"},
            {"title": "WAF (Web Application Firewall)", "difficulty": "hard"},
            {"title": "Shield (DDoS protection)", "difficulty": "hard"},
            {"title": "AWS SSO", "difficulty": "hard"},
            {"title": "Federation (SAML, OIDC)", "difficulty": "hard"},
            {"title": "Cognito basics", "difficulty": "medium"},
            {"title": "Service Control Policies", "difficulty": "hard"},
            {"title": "Permission boundaries", "difficulty": "hard"},
            {"title": "KMS (Key Management Service)", "difficulty": "hard"},
            {"title": "Encryption at rest and in transit", "difficulty": "medium"},
            {"title": "Certificate Manager (ACM)", "difficulty": "medium"},
            {"title": "Secrets Manager vs Parameter Store", "difficulty": "medium"},
            {"title": "AWS Config", "difficulty": "medium"},
            {"title": "CloudTrail", "difficulty": "medium"},
            {"title": "Security Hub", "difficulty": "hard"},
            {"title": "GuardDuty", "difficulty": "medium"},
            {"title": "Compliance frameworks (SOC2, HIPAA, PCI)", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "Advanced VPC Design", "slug": "lab-9-1-advanced-vpc", "hours": 3.0},
            {"title": "WAF Configuration", "slug": "lab-9-2-waf", "hours": 3.0},
            {"title": "KMS and Encryption", "slug": "lab-9-3-kms", "hours": 3.0},
            {"title": "CloudTrail and Config", "slug": "lab-9-4-cloudtrail", "hours": 3.0},
            {"title": "Security Hub Setup", "slug": "lab-9-5-security-hub", "hours": 2.0},
            {"title": "Automated Security Response", "slug": "lab-9-6-auto-response", "hours": 3.0},
        ],
        "project": {
            "title": "Secure Reference Architecture",
            "slug": "project-secure-architecture",
            "description": "Implement a secure architecture: multi-account strategy, Transit Gateway connectivity, centralized logging, Security Hub aggregation, automated compliance checks, incident response automation.",
            "deliverables": [
                "Security architecture diagram",
                "Network topology diagram",
                "Security controls documentation",
                "Compliance checklist",
                "Incident response playbook",
            ],
            "xp_reward": 1000,
            "estimated_hours": 10.0,
        },
    },

    # =========================================================================
    # TRACK 3: CONTAINERS & ORCHESTRATION (Modules 10-12)
    # =========================================================================
    {
        "track_slug": "containers-orchestration",
        "order_index": 10,
        "name": "Docker Fundamentals",
        "slug": "docker-fundamentals",
        "description": "Master Docker — the container technology that revolutionized how we build and deploy applications.",
        "difficulty": "intermediate",
        "estimated_hours": 15.0,
        "prerequisites": ["linux-mastery"],
        "tasks": [
            {"title": "Containers vs VMs", "difficulty": "easy"},
            {"title": "Docker architecture", "difficulty": "medium"},
            {"title": "Images and layers", "difficulty": "medium"},
            {"title": "Container lifecycle", "difficulty": "medium"},
            {"title": "Docker CLI basics", "difficulty": "easy"},
            {"title": "Dockerfile instruction reference", "difficulty": "medium"},
            {"title": "Build context", "difficulty": "medium"},
            {"title": "Layer caching", "difficulty": "hard"},
            {"title": "Multi-stage builds", "difficulty": "hard"},
            {"title": "Build arguments", "difficulty": "medium"},
            {"title": "Tagging strategies", "difficulty": "medium"},
            {"title": "Registry basics (Docker Hub, ECR)", "difficulty": "medium"},
            {"title": "Image scanning", "difficulty": "medium"},
            {"title": "Base image selection", "difficulty": "medium"},
            {"title": "Size optimization", "difficulty": "hard"},
            {"title": "Resource limits", "difficulty": "medium"},
            {"title": "Environment variables", "difficulty": "easy"},
            {"title": "Volume management", "difficulty": "medium"},
            {"title": "Network basics", "difficulty": "medium"},
            {"title": "Docker Compose syntax", "difficulty": "medium"},
            {"title": "Compose service definition", "difficulty": "medium"},
            {"title": "Non-root containers", "difficulty": "hard"},
            {"title": "Read-only filesystems", "difficulty": "hard"},
            {"title": "Secrets handling", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "Docker CLI Fundamentals", "slug": "lab-10-1-docker-cli", "hours": 2.0},
            {"title": "Dockerfile Best Practices", "slug": "lab-10-2-dockerfile", "hours": 3.0},
            {"title": "Multi-Stage Builds", "slug": "lab-10-3-multistage", "hours": 2.0},
            {"title": "Docker Compose Application", "slug": "lab-10-4-compose", "hours": 3.0},
            {"title": "Container Security Hardening", "slug": "lab-10-5-security", "hours": 2.0},
        ],
        "project": {
            "title": "Containerized Full-Stack App",
            "slug": "project-containerized-fullstack",
            "description": "Containerize a complete application: Frontend (React/Next.js), Backend API (Python/Node), Database (PostgreSQL), Redis cache, Nginx reverse proxy.",
            "deliverables": [
                "Optimized Dockerfiles",
                "docker-compose.yml (dev + prod)",
                "Documentation",
                "Size comparison report",
                "Security scan results",
            ],
            "xp_reward": 750,
            "estimated_hours": 8.0,
        },
    },
    {
        "track_slug": "containers-orchestration",
        "order_index": 11,
        "name": "Docker Advanced & Production",
        "slug": "docker-advanced-production",
        "description": "Take Docker to production with advanced patterns, monitoring, and enterprise-grade practices.",
        "difficulty": "advanced",
        "estimated_hours": 15.0,
        "prerequisites": ["docker-fundamentals"],
        "tasks": [
            {"title": "BuildKit features", "difficulty": "hard"},
            {"title": "Cache mounts", "difficulty": "hard"},
            {"title": "Secret mounts", "difficulty": "hard"},
            {"title": "Build attestations", "difficulty": "hard"},
            {"title": "SBOM generation", "difficulty": "hard"},
            {"title": "Reproducible builds", "difficulty": "hard"},
            {"title": "ECR setup and policies", "difficulty": "medium"},
            {"title": "Image lifecycle management", "difficulty": "medium"},
            {"title": "Cross-region replication", "difficulty": "hard"},
            {"title": "Image signing (cosign)", "difficulty": "hard"},
            {"title": "Health checks", "difficulty": "medium"},
            {"title": "Graceful shutdown", "difficulty": "hard"},
            {"title": "Signal handling", "difficulty": "hard"},
            {"title": "Init systems (tini, dumb-init)", "difficulty": "medium"},
            {"title": "Sidecar containers", "difficulty": "hard"},
            {"title": "Container metrics", "difficulty": "medium"},
            {"title": "Log aggregation", "difficulty": "medium"},
            {"title": "cAdvisor", "difficulty": "medium"},
            {"title": "Prometheus metrics", "difficulty": "hard"},
            {"title": "ECS task definitions", "difficulty": "hard"},
            {"title": "ECS services", "difficulty": "hard"},
            {"title": "Fargate vs EC2", "difficulty": "medium"},
        ],
        "labs": [
            {"title": "BuildKit Advanced Features", "slug": "lab-11-1-buildkit", "hours": 2.0},
            {"title": "ECR Lifecycle Management", "slug": "lab-11-2-ecr", "hours": 2.0},
            {"title": "Container Monitoring Setup", "slug": "lab-11-3-monitoring", "hours": 3.0},
            {"title": "CI/CD Pipeline for Containers", "slug": "lab-11-4-cicd", "hours": 4.0},
            {"title": "ECS Deployment", "slug": "lab-11-5-ecs", "hours": 4.0},
        ],
        "project": {
            "title": "Production Container Platform",
            "slug": "project-production-containers",
            "description": "Build a complete container platform: multi-stage builds with SBOM, ECR with scanning and signing, GitHub Actions pipeline, ECS deployment, Prometheus monitoring, log aggregation.",
            "deliverables": [
                "Production Dockerfiles",
                "CI/CD pipeline",
                "ECS infrastructure (Terraform)",
                "Monitoring dashboards",
                "Runbook documentation",
            ],
            "xp_reward": 1000,
            "estimated_hours": 10.0,
        },
    },
    {
        "track_slug": "containers-orchestration",
        "order_index": 12,
        "name": "Kubernetes Core",
        "slug": "kubernetes-core",
        "description": "Kubernetes — the container orchestration standard. Deploy, scale, and manage containerized applications in production.",
        "difficulty": "advanced",
        "estimated_hours": 25.0,
        "prerequisites": ["docker-advanced-production"],
        "tasks": [
            {"title": "Control plane components", "difficulty": "medium"},
            {"title": "Worker node components", "difficulty": "medium"},
            {"title": "etcd and cluster state", "difficulty": "hard"},
            {"title": "API server", "difficulty": "medium"},
            {"title": "kubectl basics", "difficulty": "easy"},
            {"title": "Pods", "difficulty": "medium"},
            {"title": "ReplicaSets", "difficulty": "medium"},
            {"title": "Deployments", "difficulty": "medium"},
            {"title": "StatefulSets", "difficulty": "hard"},
            {"title": "DaemonSets", "difficulty": "medium"},
            {"title": "Jobs and CronJobs", "difficulty": "medium"},
            {"title": "Service types (ClusterIP, NodePort, LoadBalancer)", "difficulty": "medium"},
            {"title": "Ingress controllers", "difficulty": "hard"},
            {"title": "DNS (CoreDNS)", "difficulty": "medium"},
            {"title": "Network policies basics", "difficulty": "hard"},
            {"title": "Volumes", "difficulty": "medium"},
            {"title": "PersistentVolumes", "difficulty": "hard"},
            {"title": "PersistentVolumeClaims", "difficulty": "hard"},
            {"title": "Storage classes", "difficulty": "hard"},
            {"title": "ConfigMaps", "difficulty": "medium"},
            {"title": "Secrets", "difficulty": "medium"},
            {"title": "Resource limits", "difficulty": "medium"},
            {"title": "QoS classes", "difficulty": "hard"},
            {"title": "Rolling updates and rollbacks", "difficulty": "medium"},
            {"title": "Health checks (liveness, readiness, startup)", "difficulty": "medium"},
            {"title": "Horizontal Pod Autoscaler", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "Cluster Setup (Minikube/kind)", "slug": "lab-12-1-cluster-setup", "hours": 2.0},
            {"title": "Deploying Applications", "slug": "lab-12-2-deployments", "hours": 3.0},
            {"title": "Services and Ingress", "slug": "lab-12-3-services", "hours": 3.0},
            {"title": "Storage Configuration", "slug": "lab-12-4-storage", "hours": 3.0},
            {"title": "ConfigMaps and Secrets", "slug": "lab-12-5-config", "hours": 2.0},
            {"title": "Scaling and Updates", "slug": "lab-12-6-scaling", "hours": 3.0},
        ],
        "project": {
            "title": "Microservices on Kubernetes",
            "slug": "project-k8s-microservices",
            "description": "Deploy a microservices application: Frontend service, API services (2-3), Database (StatefulSet), Redis cache, Ingress with TLS, ConfigMaps and Secrets, HPA configuration.",
            "deliverables": [
                "Kubernetes manifests",
                "Deployment documentation",
                "Architecture diagram",
                "Troubleshooting guide",
                "Scaling strategy",
            ],
            "xp_reward": 1000,
            "estimated_hours": 12.0,
        },
    },

    # =========================================================================
    # TRACK 4: PLATFORM ENGINEERING (Modules 13-15)
    # =========================================================================
    {
        "track_slug": "platform-engineering",
        "order_index": 13,
        "name": "Kubernetes Advanced & GitOps",
        "slug": "kubernetes-advanced-gitops",
        "description": "Advanced Kubernetes patterns and GitOps for enterprise-grade platform engineering.",
        "difficulty": "expert",
        "estimated_hours": 25.0,
        "prerequisites": ["kubernetes-core"],
        "tasks": [
            {"title": "EKS architecture", "difficulty": "hard"},
            {"title": "Managed node groups", "difficulty": "medium"},
            {"title": "Fargate profiles", "difficulty": "hard"},
            {"title": "EKS add-ons", "difficulty": "medium"},
            {"title": "IAM integration (IRSA)", "difficulty": "hard"},
            {"title": "EKS Terraform modules", "difficulty": "hard"},
            {"title": "Helm chart structure", "difficulty": "medium"},
            {"title": "Helm templates and values", "difficulty": "hard"},
            {"title": "Helm hooks", "difficulty": "hard"},
            {"title": "Chart dependencies", "difficulty": "hard"},
            {"title": "Creating custom charts", "difficulty": "hard"},
            {"title": "Kustomize base and overlays", "difficulty": "medium"},
            {"title": "Kustomize patches", "difficulty": "hard"},
            {"title": "ConfigMap/Secret generators", "difficulty": "medium"},
            {"title": "ArgoCD architecture", "difficulty": "hard"},
            {"title": "Application CRD", "difficulty": "hard"},
            {"title": "Sync policies", "difficulty": "medium"},
            {"title": "ArgoCD rollbacks", "difficulty": "medium"},
            {"title": "ApplicationSets", "difficulty": "hard"},
            {"title": "Multi-cluster management", "difficulty": "hard"},
            {"title": "Pod Security Standards", "difficulty": "hard"},
            {"title": "OPA/Gatekeeper", "difficulty": "hard"},
            {"title": "Admission controllers", "difficulty": "hard"},
            {"title": "Network policies advanced", "difficulty": "hard"},
            {"title": "Service mesh intro (Istio/Linkerd)", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "EKS Cluster with Terraform", "slug": "lab-13-1-eks-terraform", "hours": 4.0},
            {"title": "Helm Chart Development", "slug": "lab-13-2-helm", "hours": 3.0},
            {"title": "Kustomize Overlays", "slug": "lab-13-3-kustomize", "hours": 2.0},
            {"title": "ArgoCD Setup and GitOps", "slug": "lab-13-4-argocd", "hours": 4.0},
            {"title": "Advanced Security Policies", "slug": "lab-13-5-security", "hours": 3.0},
            {"title": "Multi-Environment GitOps", "slug": "lab-13-6-multi-env", "hours": 4.0},
        ],
        "project": {
            "title": "GitOps Platform",
            "slug": "project-gitops-platform",
            "description": "Build a complete GitOps platform: EKS cluster (Terraform), ArgoCD installation, app-of-apps pattern, Helm charts for services, environment promotion (dev→staging→prod), security policies, automated sync.",
            "deliverables": [
                "EKS Terraform modules",
                "Helm chart library",
                "ArgoCD applications",
                "GitOps repository structure",
                "Promotion workflow documentation",
            ],
            "xp_reward": 1250,
            "estimated_hours": 15.0,
        },
    },
    {
        "track_slug": "platform-engineering",
        "order_index": 14,
        "name": "Observability & Monitoring",
        "slug": "observability-monitoring",
        "description": "Implement full observability stack — metrics, logs, and traces — to drive reliable infrastructure.",
        "difficulty": "expert",
        "estimated_hours": 20.0,
        "prerequisites": ["kubernetes-advanced-gitops"],
        "tasks": [
            {"title": "Three pillars (metrics, logs, traces)", "difficulty": "easy"},
            {"title": "SLIs, SLOs, SLAs", "difficulty": "medium"},
            {"title": "Error budgets", "difficulty": "hard"},
            {"title": "Observability vs monitoring", "difficulty": "easy"},
            {"title": "Prometheus architecture", "difficulty": "hard"},
            {"title": "Data model (metrics, labels)", "difficulty": "medium"},
            {"title": "PromQL", "difficulty": "hard"},
            {"title": "Scrape configuration", "difficulty": "medium"},
            {"title": "Service discovery", "difficulty": "hard"},
            {"title": "Recording rules", "difficulty": "hard"},
            {"title": "Alerting rules", "difficulty": "hard"},
            {"title": "Grafana dashboard design", "difficulty": "medium"},
            {"title": "Variables and templating", "difficulty": "medium"},
            {"title": "Grafana alerting", "difficulty": "medium"},
            {"title": "Dashboard provisioning", "difficulty": "hard"},
            {"title": "Loki architecture", "difficulty": "hard"},
            {"title": "Log aggregation patterns", "difficulty": "hard"},
            {"title": "LogQL", "difficulty": "hard"},
            {"title": "Structured logging", "difficulty": "medium"},
            {"title": "Distributed tracing concepts", "difficulty": "hard"},
            {"title": "OpenTelemetry", "difficulty": "hard"},
            {"title": "Tempo/Jaeger", "difficulty": "hard"},
            {"title": "Alert design principles", "difficulty": "hard"},
            {"title": "Severity levels", "difficulty": "medium"},
            {"title": "PagerDuty/OpsGenie integration", "difficulty": "medium"},
        ],
        "labs": [
            {"title": "Prometheus Installation", "slug": "lab-14-1-prometheus", "hours": 3.0},
            {"title": "Grafana Dashboards", "slug": "lab-14-2-grafana", "hours": 3.0},
            {"title": "Loki Log Aggregation", "slug": "lab-14-3-loki", "hours": 3.0},
            {"title": "Application Metrics", "slug": "lab-14-4-app-metrics", "hours": 3.0},
            {"title": "Alerting Configuration", "slug": "lab-14-5-alerting", "hours": 2.0},
            {"title": "Full Stack Observability", "slug": "lab-14-6-full-stack", "hours": 4.0},
        ],
        "project": {
            "title": "Production Observability Stack",
            "slug": "project-observability-stack",
            "description": "Implement complete observability: Prometheus + Alertmanager, Grafana dashboards, Loki for logs, application instrumentation, custom metrics, SLO tracking, incident response integration.",
            "deliverables": [
                "Observability architecture diagram",
                "Prometheus configuration",
                "Grafana dashboards (5+)",
                "Alert definitions",
                "Runbooks",
                "SLO documentation",
            ],
            "xp_reward": 1000,
            "estimated_hours": 12.0,
        },
    },
    {
        "track_slug": "platform-engineering",
        "order_index": 15,
        "name": "SRE, DevSecOps & Capstone",
        "slug": "sre-devsecops-capstone",
        "description": "Final module combining SRE practices, DevSecOps, and a capstone project demonstrating all knowledge.",
        "difficulty": "expert",
        "estimated_hours": 30.0,
        "prerequisites": ["observability-monitoring"],
        "tasks": [
            {"title": "SRE vs DevOps", "difficulty": "easy"},
            {"title": "Service Level Objectives", "difficulty": "hard"},
            {"title": "Error budgets deep dive", "difficulty": "hard"},
            {"title": "Toil reduction", "difficulty": "medium"},
            {"title": "Capacity planning", "difficulty": "hard"},
            {"title": "Reliability engineering", "difficulty": "hard"},
            {"title": "Incident response process", "difficulty": "hard"},
            {"title": "On-call practices", "difficulty": "medium"},
            {"title": "Communication during incidents", "difficulty": "medium"},
            {"title": "Postmortems (blameless)", "difficulty": "medium"},
            {"title": "Root cause analysis", "difficulty": "hard"},
            {"title": "Security shift-left", "difficulty": "medium"},
            {"title": "SAST (Static Analysis)", "difficulty": "hard"},
            {"title": "DAST (Dynamic Analysis)", "difficulty": "hard"},
            {"title": "SCA (Software Composition Analysis)", "difficulty": "hard"},
            {"title": "Container scanning", "difficulty": "medium"},
            {"title": "Infrastructure scanning", "difficulty": "hard"},
            {"title": "Secret scanning", "difficulty": "medium"},
            {"title": "Dependency checks", "difficulty": "medium"},
            {"title": "Compliance as code", "difficulty": "hard"},
            {"title": "Policy enforcement", "difficulty": "hard"},
            {"title": "ChatOps", "difficulty": "medium"},
            {"title": "Self-healing infrastructure", "difficulty": "hard"},
            {"title": "Chaos engineering intro", "difficulty": "hard"},
        ],
        "labs": [
            {"title": "SLO Implementation", "slug": "lab-15-1-slo", "hours": 3.0},
            {"title": "Incident Simulation", "slug": "lab-15-2-incident", "hours": 3.0},
            {"title": "Security Scanning Pipeline", "slug": "lab-15-3-security-scan", "hours": 4.0},
            {"title": "Compliance Automation", "slug": "lab-15-4-compliance", "hours": 3.0},
            {"title": "Chaos Engineering Basics", "slug": "lab-15-5-chaos", "hours": 3.0},
        ],
        "project": {
            "title": "Complete DevOps Platform (Capstone)",
            "slug": "project-capstone-platform",
            "description": "Build a complete, production-ready platform demonstrating all 15 modules' knowledge: EKS infrastructure, microservices application, CI/CD with security scanning, GitOps deployment, full observability stack, security policies, documentation, and runbooks.",
            "deliverables": [
                "Complete GitHub repository",
                "Working deployed application",
                "Infrastructure as Code",
                "CI/CD pipelines",
                "Observability stack",
                "Security documentation",
                "Architecture documentation",
                "Video walkthrough (optional)",
            ],
            "xp_reward": 2000,
            "estimated_hours": 25.0,
        },
    },
]


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_tracks() -> list[dict]:
    """Returns all 4 tracks."""
    return BOOTCAMP_TRACKS


def get_modules() -> list[dict]:
    """Returns all 15 modules."""
    return BOOTCAMP_MODULES


def get_track_count() -> int:
    """Returns the total number of tracks."""
    return len(BOOTCAMP_TRACKS)


def get_module_count() -> int:
    """Returns the total number of modules."""
    return len(BOOTCAMP_MODULES)


def get_task_count() -> int:
    """Returns the total number of tasks across all modules."""
    return sum(len(module["tasks"]) for module in BOOTCAMP_MODULES)


def get_lab_count() -> int:
    """Returns the total number of labs across all modules."""
    return sum(len(module["labs"]) for module in BOOTCAMP_MODULES)


def get_project_count() -> int:
    """Returns the total number of projects."""
    return len([m for m in BOOTCAMP_MODULES if m.get("project")])


def get_total_hours() -> float:
    """Returns the total estimated hours for the bootcamp."""
    return sum(module["estimated_hours"] for module in BOOTCAMP_MODULES)


def get_modules_by_track(track_slug: str) -> list[dict]:
    """Returns all modules for a specific track."""
    return [m for m in BOOTCAMP_MODULES if m["track_slug"] == track_slug]


def get_bootcamp_summary() -> dict:
    """Returns a summary of the bootcamp content."""
    return {
        "tracks": get_track_count(),
        "modules": get_module_count(),
        "tasks": get_task_count(),
        "labs": get_lab_count(),
        "projects": get_project_count(),
        "total_hours": get_total_hours(),
    }
