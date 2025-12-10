"""
Azure Block 4 Node 16: Azure Pipelines - V2 Interactive Format
"""

AZURE_NODE_16_PIPELINES_V2 = {
    "node_id": 16,
    "title": "Azure Pipelines",
    "slug": "azure-pipelines",
    "description": "CI/CD automation med Azure Pipelines",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Azure Pipelines",
            "content": {
                "headline": "Automate your build, test, and deployment",
                "hook": "Azure Pipelines är multi-platform CI/CD som stöder alla språk och frameworks med YAML-baserad pipeline as code.",
                "learning_objectives": [
                    "Skapa YAML-baserade CI/CD pipelines",
                    "Förstå stages, jobs och steps",
                    "Konfigurera environments med approvals",
                    "Använda templates för återanvändbara pipelines"
                ],
                "prerequisites": ["Azure DevOps basics", "Git"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Pipeline Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Pipeline Struktur",
                        "explanation": "Pipeline -> Stages -> Jobs -> Steps. Stages (Build, Deploy-Dev, Deploy-Prod) innehåller Jobs som kör på agents. Steps är enskilda tasks.",
                        "diagram": """
+---------------------------------------------+
| Pipeline                                    |
| +-- Stage: Build                            |
| |   +-- Job: BuildApp                       |
| |       +-- Step: Checkout                  |
| |       +-- Step: npm install               |
| |       +-- Step: npm build                 |
| +-- Stage: Deploy-Dev                       |
| |   +-- Job: DeployDev                      |
| +-- Stage: Deploy-Prod (with approval)      |
|     +-- Job: DeployProd                     |
+---------------------------------------------+""",
                        "pro_tip": "Använd dependsOn för stage-ordning och conditions för conditional execution.",
                        "common_mistake": "Att köra allt i ett stage - separera build, test och deploy."
                    },
                    {
                        "title": "Triggers & Environments",
                        "explanation": "Triggers startar pipeline (push, PR, schedule). Environments representerar deploy targets med approvals och checks.",
                        "diagram": """
+---------------------------------------------+
| TRIGGERS                                    |
+---------------------------------------------+
| trigger: [main]         # Push to main      |
| pr: [main, develop]     # PR to branches    |
| schedules: cron         # Scheduled runs    |
+---------------------------------------------+
| ENVIRONMENTS                                |
+---------------------------------------------+
| dev      | Auto-deploy                      |
| staging  | Auto-deploy                      |
| prod     | Manual approval required         |
+---------------------------------------------+""",
                        "pro_tip": "Kräv alltid approval för produktion - ingen auto-deploy!",
                        "common_mistake": "Att inte använda environments - deployment history går förlorad."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Pipelines",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa basic YAML pipeline",
                        "instruction": "Skapa azure-pipelines.yml med trigger på main och npm build",
                        "expected_command": """# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0
    inputs:
      versionSpec: '18.x'
  - script: npm ci
  - script: npm run build""",
                        "hint": "trigger definierar vilka branches som startar pipeline"
                    },
                    {
                        "task": "Lägg till stages",
                        "instruction": "Separera Build och Deploy i olika stages",
                        "expected_command": """stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - script: npm ci && npm build
  - stage: Deploy
    dependsOn: Build
    jobs:
      - deployment: DeployWeb
        environment: 'dev'""",
                        "hint": "dependsOn säkerställer att Build körs först"
                    },
                    {
                        "task": "Lista pipelines",
                        "instruction": "Visa alla pipelines i projektet via CLI",
                        "expected_command": "az pipelines list --output table",
                        "hint": "Kräver azure-devops extension och konfigurerade defaults"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Vad är skillnaden mellan job och deployment?", "back": "Deployment är för environments med approvals/checks, job är för vanliga tasks"},
                        {"front": "Hur kräver man approval i pipeline?", "back": "Konfigurera Environment i Azure DevOps med Approval check"},
                        {"front": "Vad gör dependsOn?", "back": "Definierar ordning mellan stages/jobs - väntar på att beroende är klart"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken pool kör på Linux?",
                            "options": ["windows-latest", "ubuntu-latest", "macos-latest", "linux-latest"],
                            "correct": 1,
                            "explanation": "ubuntu-latest är standard Linux pool image"
                        },
                        {
                            "question": "Hur triggar man pipeline på PR till main?",
                            "options": ["trigger: pr", "pr: [main]", "pullrequest: main", "on: pull_request"],
                            "correct": 1,
                            "explanation": "pr: [branches] definierar PR triggers"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "Pipeline Challenge",
            "content": {
                "scenario": "Bygg en komplett CI/CD pipeline för en Node.js app till Azure App Service.",
                "requirements": [
                    "Trigger på push till main och PR",
                    "Build stage med npm test",
                    "Deploy stage till dev (auto) och prod (approval)",
                    "Använd Azure Web App deployment task"
                ],
                "hints": [
                    "AzureWebApp@1 task för deployment",
                    "Skapa environments: dev och prod",
                    "condition: succeeded() för att köra efter success"
                ],
                "solution": """# azure-pipelines.yml
trigger:
  - main
pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Build
    jobs:
      - job: BuildAndTest
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '18.x'
          - script: npm ci
          - script: npm test
          - script: npm run build
          - publish: $(System.DefaultWorkingDirectory)/dist
            artifact: webapp

  - stage: DeployDev
    dependsOn: Build
    jobs:
      - deployment: DeployDev
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'MyAzureConnection'
                    appName: 'myapp-dev'
                    package: '$(Pipeline.Workspace)/webapp'

  - stage: DeployProd
    dependsOn: DeployDev
    jobs:
      - deployment: DeployProd
        environment: 'prod'  # Approval configured here
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'MyAzureConnection'
                    appName: 'myapp-prod'
                    package: '$(Pipeline.Workspace)/webapp'""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
