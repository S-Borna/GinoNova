# =============================================================================
# BLOCK 5: ENTERPRISE GIT PART 1 (Noder 17-18)
# =============================================================================

NODE_17_GITOPS = {
    "node_id": 17,
    "title": "GitOps & Infrastructure as Code",
    "slug": "gitops-infrastructure",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": ["github-actions-mastery"],
    "content": r'''
# GitOps & Infrastructure as Code

## Varför detta är kritiskt

> "GitOps är principen att Git är den enda sanningskällan för deklarativ infrastruktur och applikationer. Allt i Git, allt automatiserat, allt auditerbart."

---

## GitOps Architecture

```
+-------------------------------------------------------------------------+
|                       GITOPS ARCHITECTURE                               |
+-------------------------------------------------------------------------+
|                                                                         |
|   DEVELOPER                   GIT REPOSITORY          KUBERNETES        |
|   ---------                   --------------          ----------        |
|                                                                         |
|   +---------+   git push     +-------------+         +-------------+   |
|   | Change  | ------------►  | main branch |         |  Cluster    |   |
|   | Code    |                |             |         |             |   |
|   +---------+                | manifests/  |         | +---------+ |   |
|                              | +-- app.yaml|         | |  Pods   | |   |
|   +---------+   PR review    | +-- svc.yaml|  sync   | |Services | |   |
|   | Review  | ◄------------  | +-- ing.yaml| ◄-----► | |Ingress  | |   |
|   | Approve |                |             |         | +---------+ |   |
|   +---------+                +-------------+         +-------------+   |
|                                    |                       ▲           |
|                                    |                       |           |
|                              +-----▼-----+                 |           |
|                              |  GitOps   |                 |           |
|                              | Operator  |-----------------+           |
|                              |(ArgoCD/   |    reconcile                |
|                              | Flux)     |                             |
|                              +-----------+                             |
|                                                                         |
|   PRINCIPLES:                                                           |
|   1. Declarative - Desired state in Git                                 |
|   2. Versioned - Git history = audit trail                              |
|   3. Automated - Operators sync continuously                            |
|   4. Auditable - All changes traceable                                  |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## ArgoCD Setup

### Installation

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# Port forward UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Install CLI
brew install argocd

# Login
argocd login localhost:8080
```

### Application Definition

```yaml
# argocd-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-application
  namespace: argocd
spec:
  project: default

  source:
    repoURL: https://github.com/company/app-manifests.git
    targetRevision: main
    path: environments/production

  destination:
    server: https://kubernetes.default.svc
    namespace: production

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### Multi-Environment Setup

```
+-------------------------------------------------------------------------+
|                    MULTI-ENVIRONMENT GITOPS                             |
+-------------------------------------------------------------------------+
|                                                                         |
|   REPOSITORY STRUCTURE:                                                 |
|                                                                         |
|   app-manifests/                                                        |
|   +-- base/                    # Shared base configs                    |
|   |   +-- deployment.yaml                                               |
|   |   +-- service.yaml                                                  |
|   |   +-- kustomization.yaml                                            |
|   |                                                                     |
|   +-- environments/                                                     |
|       +-- development/         # Dev environment                        |
|       |   +-- kustomization.yaml                                        |
|       |   +-- patches/                                                  |
|       |       +-- replicas.yaml                                         |
|       |                                                                 |
|       +-- staging/             # Staging environment                    |
|       |   +-- kustomization.yaml                                        |
|       |   +-- patches/                                                  |
|       |                                                                 |
|       +-- production/          # Production environment                 |
|           +-- kustomization.yaml                                        |
|           +-- patches/                                                  |
|                                                                         |
|   PROMOTION FLOW:                                                       |
|   development -> staging -> production                                    |
|        |           |           |                                        |
|        ▼           ▼           ▼                                        |
|     auto-sync   PR-review   PR-review                                   |
|                + approval   + 2 approvals                               |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Flux CD

### Installation

```bash
# Install Flux CLI
brew install fluxcd/tap/flux

# Bootstrap Flux with GitHub
flux bootstrap github \
  --owner=company \
  --repository=fleet-infra \
  --branch=main \
  --path=clusters/production \
  --personal
```

### GitRepository Source

```yaml
# flux-source.yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: app-manifests
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/company/app-manifests
  ref:
    branch: main
  secretRef:
    name: github-credentials
```

### Kustomization

```yaml
# flux-kustomization.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: production-apps
  namespace: flux-system
spec:
  interval: 10m
  sourceRef:
    kind: GitRepository
    name: app-manifests
  path: ./environments/production
  prune: true
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: my-app
      namespace: production
```

---

## Repository Strategies

### Monorepo Strategy

```
company-platform/
+-- apps/                    # Application code
|   +-- frontend/
|   +-- backend/
+-- manifests/               # Kubernetes manifests
|   +-- base/
|   +-- environments/
+-- terraform/               # Infrastructure
|   +-- modules/
|   +-- environments/
+-- .github/workflows/       # CI/CD
```

### Polyrepo Strategy

```
REPOSITORIES:
+-- app-frontend/           # Frontend code + Dockerfile
+-- app-backend/            # Backend code + Dockerfile
+-- infrastructure/         # Terraform code
+-- fleet-manifests/        # Kubernetes manifests
    +-- apps/
    |   +-- frontend/
    |   +-- backend/
    +-- infrastructure/
```

---

## Image Automation

### Flux Image Automation

```yaml
# image-repository.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: my-app
  namespace: flux-system
spec:
  image: ghcr.io/company/my-app
  interval: 1m
  secretRef:
    name: ghcr-credentials
---
# image-policy.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: my-app
  namespace: flux-system
spec:
  imageRepositoryRef:
    name: my-app
  policy:
    semver:
      range: ">=1.0.0"
---
# image-update.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageUpdateAutomation
metadata:
  name: flux-system
  namespace: flux-system
spec:
  interval: 10m
  sourceRef:
    kind: GitRepository
    name: fleet-infra
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: flux@company.com
        name: Flux
      messageTemplate: |
        Automated image update

        - {{range .Updated.Images}}{{println .}}{{end}}
    push:
      branch: main
  update:
    path: ./clusters/production
    strategy: Setters
```

---

## Secrets Management

### Sealed Secrets

```bash
# Install controller
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.24.0/controller.yaml

# Install kubeseal CLI
brew install kubeseal

# Create sealed secret
kubectl create secret generic my-secret \
  --from-literal=password=supersecret \
  --dry-run=client -o yaml | \
  kubeseal --format yaml > sealed-secret.yaml

# Commit sealed secret to Git (safe!)
git add sealed-secret.yaml
git commit -m "Add sealed secret"
```

### SOPS + Age

```yaml
# .sops.yaml
creation_rules:
  - path_regex: .*secrets.*\.yaml$
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
```

```bash
# Encrypt secret
sops --encrypt secrets.yaml > secrets.enc.yaml

# Decrypt (Flux does this automatically)
sops --decrypt secrets.enc.yaml
```

---

## GitOps Workflows

### PR-based Deployment

```yaml
# .github/workflows/gitops-pr.yml
name: Create Deployment PR

on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      image_tag:
        description: 'Image tag to deploy'
        required: true

jobs:
  create-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: company/fleet-manifests
          token: ${{ secrets.FLEET_TOKEN }}

      - name: Update image tag
        run: |
          cd environments/${{ inputs.environment }}
          kustomize edit set image my-app=ghcr.io/company/my-app:${{ inputs.image_tag }}

      - name: Create PR
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.FLEET_TOKEN }}
          commit-message: "Deploy ${{ inputs.image_tag }} to ${{ inputs.environment }}"
          title: "Deploy ${{ inputs.image_tag }} to ${{ inputs.environment }}"
          branch: deploy/${{ inputs.environment }}/${{ inputs.image_tag }}
```

---

## Sammanfattning

| Component | Tool | Purpose |
|-----------|------|---------|
| GitOps Operator | ArgoCD/Flux | Sync Git -> Cluster |
| Config Management | Kustomize/Helm | Environment patches |
| Secrets | Sealed Secrets/SOPS | Encrypted secrets in Git |
| Image Updates | Flux Image Automation | Auto-update image tags |
| Promotion | PRs | Environment promotion |

---

## Nästa Steg

GitOps behärskad. Nästa: **Disaster Recovery & Migrations** — backup, recovery, och stora migrationer.
''',
}

NODE_18_DISASTER_RECOVERY = {
    "node_id": 18,
    "title": "Disaster Recovery & Migrations",
    "slug": "disaster-recovery-migrations",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": ["gitops-infrastructure"],
    "content": r'''
# Disaster Recovery & Migrations

## Varför detta är kritiskt

> "Det finns två typer av företag: de som har förlorat data, och de som kommer att förlora data. Disaster recovery och migrationsstrategier är inte valfria — de är överlevnad."

---

## Backup Strategies

```
+-------------------------------------------------------------------------+
|                       GIT BACKUP STRATEGIES                             |
+-------------------------------------------------------------------------+
|                                                                         |
|   LEVEL 1: DISTRIBUTED COPIES                                           |
|   -----------------------------                                         |
|   Every clone is a backup!                                              |
|   • Developer machines                                                  |
|   • CI/CD runners                                                       |
|   • Multiple remotes                                                    |
|                                                                         |
|   LEVEL 2: MIRROR REPOSITORIES                                          |
|   -----------------------------                                         |
|   +--------------+    mirror    +--------------+                       |
|   |   GitHub     | ----------►  |   GitLab     |                       |
|   |   (Primary)  |              |   (Backup)   |                       |
|   +--------------+              +--------------+                       |
|                                                                         |
|   LEVEL 3: BARE REPOSITORY BACKUPS                                      |
|   ---------------------------------                                     |
|   +--------------+    backup    +--------------+                       |
|   |   Origin     | ----------►  |   S3/GCS     |                       |
|   |              |    daily     |   Archive    |                       |
|   +--------------+              +--------------+                       |
|                                                                         |
|   LEVEL 4: FULL ORGANIZATION BACKUP                                     |
|   ---------------------------------                                     |
|   • All repositories                                                    |
|   • Issues, PRs, wikis                                                  |
|   • Actions workflows                                                   |
|   • Settings and permissions                                            |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Mirror Setup

### Push Mirror

```bash
# Add mirror remote
git remote add mirror git@gitlab.com:company/repo.git

# Push all branches and tags
git push mirror --all
git push mirror --tags

# Automated mirror script
#!/bin/bash
# mirror-repos.sh

REPOS=(
  "repo1"
  "repo2"
  "repo3"
)

for repo in "${REPOS[@]}"; do
  cd "/backup/$repo"
  git fetch origin --prune
  git push mirror --all --force
  git push mirror --tags --force
done
```

### GitHub Actions Mirror

```yaml
# .github/workflows/mirror.yml
name: Mirror to GitLab

on:
  push:
    branches: ['**']
    tags: ['**']

jobs:
  mirror:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Mirror to GitLab
        env:
          GITLAB_TOKEN: ${{ secrets.GITLAB_TOKEN }}
        run: |
          git remote add mirror https://oauth2:${GITLAB_TOKEN}@gitlab.com/company/repo.git
          git push mirror --all --force
          git push mirror --tags --force
```

---

## Backup Scripts

### Full Repository Backup

```bash
#!/bin/bash
# backup-repos.sh

BACKUP_DIR="/backup/git"
DATE=$(date +%Y-%m-%d)
GITHUB_ORG="company"

# Create backup directory
mkdir -p "$BACKUP_DIR/$DATE"

# Get all repos via GitHub API
repos=$(gh repo list "$GITHUB_ORG" --json name -q '.[].name')

for repo in $repos; do
  echo "Backing up $repo..."

  # Clone as bare repository
  git clone --mirror "https://github.com/$GITHUB_ORG/$repo.git" \
    "$BACKUP_DIR/$DATE/$repo.git"

  # Create tarball
  tar -czf "$BACKUP_DIR/$DATE/$repo.tar.gz" \
    -C "$BACKUP_DIR/$DATE" "$repo.git"

  # Remove bare repo (keep only tarball)
  rm -rf "$BACKUP_DIR/$DATE/$repo.git"
done

# Upload to S3
aws s3 sync "$BACKUP_DIR/$DATE" "s3://company-backups/git/$DATE/"

# Cleanup old local backups (keep 7 days)
find "$BACKUP_DIR" -maxdepth 1 -type d -mtime +7 -exec rm -rf {} \;

echo "Backup complete: $(ls -la $BACKUP_DIR/$DATE | wc -l) repos"
```

### Restore from Backup

```bash
#!/bin/bash
# restore-repo.sh

REPO_NAME=$1
BACKUP_DATE=$2
BACKUP_DIR="/backup/git"

# Download from S3 if needed
aws s3 cp "s3://company-backups/git/$BACKUP_DATE/$REPO_NAME.tar.gz" \
  "$BACKUP_DIR/"

# Extract
tar -xzf "$BACKUP_DIR/$REPO_NAME.tar.gz" -C "$BACKUP_DIR/"

# Push to new remote
cd "$BACKUP_DIR/$REPO_NAME.git"
git remote add restore "https://github.com/company/$REPO_NAME.git"
git push restore --all
git push restore --tags

echo "Restored $REPO_NAME from $BACKUP_DATE"
```

---

## Repository Migrations

### GitHub to GitHub (Different Org)

```bash
# Clone with full history
git clone --mirror https://github.com/old-org/repo.git
cd repo.git

# Update remote
git remote set-url origin https://github.com/new-org/repo.git

# Push everything
git push origin --all
git push origin --tags
```

### GitHub to GitLab (Full Migration)

```bash
# 1. Clone mirror
git clone --mirror https://github.com/company/repo.git
cd repo.git

# 2. Add GitLab remote
git remote add gitlab https://gitlab.com/company/repo.git

# 3. Push all
git push gitlab --all
git push gitlab --tags

# 4. Migrate issues (use tool)
# github-to-gitlab-migrator or manual export/import
```

### Large Repository Migration

```bash
#!/bin/bash
# migrate-large-repo.sh

# For repos with large history

# 1. Shallow clone first
git clone --depth=1 https://github.com/company/huge-repo.git
cd huge-repo

# 2. Fetch rest of history in batches
git fetch --unshallow

# 3. If LFS is used
git lfs fetch --all
git lfs push --all https://gitlab.com/company/huge-repo.git

# 4. Push to new remote
git remote add new https://gitlab.com/company/huge-repo.git
git push new --all
git push new --tags
```

---

## History Rewriting (Migrations)

### Remove Sensitive Data

```bash
# Using git-filter-repo (recommended)
pip install git-filter-repo

# Remove file from all history
git filter-repo --path secrets.json --invert-paths

# Replace text
echo "PASSWORD123==>REDACTED" > replacements.txt
git filter-repo --replace-text replacements.txt

# Remove large files
git filter-repo --strip-blobs-bigger-than 100M
```

### Change Author Information

```bash
# Create mailmap file
cat > .mailmap << EOF
New Name <new@email.com> Old Name <old@email.com>
New Name <new@email.com> <another-old@email.com>
EOF

# Apply mailmap
git filter-repo --mailmap .mailmap
```

### Subdirectory to New Repository

```bash
# Extract subdirectory as new repo
git filter-repo --subdirectory-filter apps/frontend

# This rewrites history so apps/frontend becomes root
# All other files removed from history
```

---

## Recovery Scenarios

### Recover Deleted Branch

```bash
# Find the commit
git reflog show --all | grep "branch-name"

# Or use fsck
git fsck --lost-found

# Recreate branch
git branch recovered-branch abc1234

# If remote was force-pushed
# Check if anyone has old commits locally
git fetch origin
git branch -a | grep -i branch-name
```

### Recover from Bad Rebase

```bash
# Find pre-rebase state
git reflog
# abc1234 HEAD@{5}: rebase -i (start): checkout main

# Reset to before rebase
git reset --hard HEAD@{6}

# Or if you know the commit
git reset --hard abc1234
```

### Recover Lost Commits

```bash
# Find dangling commits
git fsck --lost-found

# Check each commit
git show <commit-hash>

# Cherry-pick needed commits
git cherry-pick <commit-hash>

# Or create branch from it
git branch recovered <commit-hash>
```

---

## Disaster Recovery Plan

```
+-------------------------------------------------------------------------+
|                    DISASTER RECOVERY PLAN                               |
+-------------------------------------------------------------------------+
|                                                                         |
|   SCENARIO 1: Accidental Force Push                                     |
|   ----------------------------------                                    |
|   1. Check reflog on any machine with old state                         |
|   2. git reflog | grep <branch>                                         |
|   3. git push origin <old-commit>:<branch> --force                      |
|   4. Notify team, verify recovery                                       |
|   RTO: Minutes                                                          |
|                                                                         |
|   SCENARIO 2: Repository Deletion                                       |
|   --------------------------------                                      |
|   1. Check GitHub support (30-day retention)                            |
|   2. Restore from mirror/backup                                         |
|   3. Re-create repo settings manually                                   |
|   4. Re-configure branch protection                                     |
|   RTO: Hours                                                            |
|                                                                         |
|   SCENARIO 3: Complete GitHub Outage                                    |
|   ----------------------------------                                    |
|   1. Communicate to team                                                |
|   2. Switch to mirror (GitLab/self-hosted)                              |
|   3. Update CI/CD to use mirror                                         |
|   4. Continue operations                                                |
|   RTO: Hours                                                            |
|                                                                         |
|   SCENARIO 4: Ransomware/Compromise                                     |
|   --------------------------------                                      |
|   1. Isolate affected systems                                           |
|   2. Revoke all access tokens                                           |
|   3. Restore from verified clean backup                                 |
|   4. Forensic analysis                                                  |
|   5. Reset all credentials                                              |
|   RTO: Days                                                             |
|                                                                         |
|   TESTING SCHEDULE:                                                     |
|   • Monthly: Restore test (random repo)                                 |
|   • Quarterly: Full DR drill                                            |
|   • Annually: Complete failover test                                    |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Sammanfattning

| Scenario | Tool | Recovery Time |
|----------|------|---------------|
| Lost commit | git reflog | Minutes |
| Deleted branch | git fsck | Minutes |
| Bad push | git reset | Minutes |
| Repo deletion | Backup restore | Hours |
| Full outage | Mirror failover | Hours |
| Compromise | Clean backup | Days |

---

## Nästa Steg

Disaster Recovery behärskad. Nästa: **Enterprise Workflows** — stora team och enterprise patterns.
''',
}

BLOCK_5_PART_1_NODES = [NODE_17_GITOPS, NODE_18_DISASTER_RECOVERY]
