#!/usr/bin/env python3
"""
V3 Premium Content Upgrade Script
Upgrades ALL module tasks to premium V3 pedagogical standard
"""

import os
import re
import sys

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

V3_PEDAGOGICAL_TEMPLATES = {
    "terraform": {
        "intro": """
## Varför {concept} är Kritiskt

> **"{quote}"**

{explanation}

```
{ascii_diagram}
```

### Vad du kommer lära dig

Efter denna uppgift kommer du kunna:
{learning_objectives}

---

""",
    },
    "generic": {
        "intro": """
## Varför detta är viktigt

> **"{quote}"**

{explanation}

```
{ascii_diagram}
```

### Vad du kommer lära dig

{learning_objectives}

---

""",
    }
}

# V3 enhancement patterns for different topics
TOPIC_ENHANCEMENTS = {
    "provider": {
        "concept": "Providers",
        "quote": "Providers är bron mellan Terraform och alla molntjänster – utan rätt provider kan du ingenting.",
        "explanation": """Providers i Terraform är plugins som kommunicerar med APIs. Varje molntjänst (AWS, Azure, GCP),
SaaS-plattform (GitHub, Datadog), eller infrastrukturtjänst (Kubernetes, Helm) har sin egen provider.""",
        "ascii": """
+---------------------------------------------------------------------+
|                    TERRAFORM PROVIDER ARCHITECTURE                   |
+---------------------------------------------------------------------+
|                                                                      |
|   +--------------+                                                   |
|   |  Terraform   |                                                   |
|   |    Core      |                                                   |
|   +------+-------+                                                   |
|          |                                                           |
|          ▼                                                           |
|   +----------------------------------------------------------+      |
|   |                  Provider Plugins                         |      |
|   +-------------+-------------+-------------+---------------+      |
|   |   AWS       |   Azure     |   GCP       |   Kubernetes  |      |
|   |   Provider  |   Provider  |   Provider  |   Provider    |      |
|   +------+------+------+------+------+------+-------+-------+      |
|          |             |             |              |               |
|          ▼             ▼             ▼              ▼               |
|   +----------+  +----------+  +----------+  +------------+         |
|   | AWS API  |  |Azure API |  | GCP API  |  | K8s API    |         |
|   +----------+  +----------+  +----------+  +------------+         |
|                                                                      |
+---------------------------------------------------------------------+
""",
        "objectives": [
            "Konfigurera providers för AWS, Azure och GCP",
            "Använda multiple provider instances",
            "Hantera provider versioning säkert",
            "Förstå provider authentication patterns"
        ]
    },
    "state": {
        "concept": "State Management",
        "quote": "Terraform state är ditt systems minne – utan det vet Terraform ingenting om vad som redan finns.",
        "explanation": """State-filen är Terraforms databas över din infrastruktur. Den mappar HCL-resurser till verkliga molnresurser
och sparar attribut som IDs, ARNs, och IP-adresser. Rätt state management är skillnaden mellan kaos och kontroll.""",
        "ascii": """
+---------------------------------------------------------------------+
|                    STATE MANAGEMENT FLOW                             |
+---------------------------------------------------------------------+
|                                                                      |
|   terraform plan                                                     |
|        |                                                             |
|        ▼                                                             |
|   +-----------------+    +-----------------+                        |
|   |  Configuration  |    |   State File    |                        |
|   |    (.tf files)  |    | (terraform.tfstate)                      |
|   +--------+--------+    +--------+--------+                        |
|            |                      |                                  |
|            +----------+-----------+                                  |
|                       |                                              |
|                       ▼                                              |
|              +-----------------+                                     |
|              |   DIFF ENGINE   |                                     |
|              |  Compare Config |                                     |
|              |   vs Reality    |                                     |
|              +--------+--------+                                     |
|                       |                                              |
|            +----------+----------+                                   |
|            ▼          ▼          ▼                                   |
|       +--------+ +--------+ +--------+                              |
|       | CREATE | | UPDATE | | DELETE |                              |
|       +--------+ +--------+ +--------+                              |
|                                                                      |
+---------------------------------------------------------------------+
""",
        "objectives": [
            "Konfigurera remote state backends (S3, Azure Blob, GCS)",
            "Implementera state locking med DynamoDB",
            "Använda terraform state commands professionellt",
            "Importera existerande infrastruktur",
            "Hantera Terraform workspaces"
        ]
    },
    "variables": {
        "concept": "Variables & Outputs",
        "quote": "Variabler gör din Terraform-kod återanvändbar. Outputs gör den kommunikativ.",
        "explanation": """Input variables är nyckeln till DRY (Don't Repeat Yourself) Terraform-kod.
Outputs låter dig exponera värden för andra system, moduler, eller automatisering.""",
        "ascii": """
+---------------------------------------------------------------------+
|                    TERRAFORM DATA FLOW                               |
+---------------------------------------------------------------------+
|                                                                      |
|   INPUTS                        CORE                      OUTPUTS   |
|   ══════                        ════                      ═══════   |
|                                                                      |
|   +-------------+         +-------------+         +-------------+   |
|   |  Variables  |         |             |         |   Outputs   |   |
|   |  (.tfvars)  |--------▶|   Terraform |--------▶|   (values)  |   |
|   +-------------+         |   Config    |         +-------------+   |
|                           |             |                           |
|   +-------------+         |   +-----+   |                           |
|   | Environment |--------▶|   |Local|   |                           |
|   |  TF_VAR_*   |         |   |vars |   |                           |
|   +-------------+         |   +-----+   |                           |
|                           |             |                           |
|   +-------------+         +-------------+                           |
|   |  CLI Flags  |--------▶                                          |
|   |  -var=...   |                                                   |
|   +-------------+                                                   |
|                                                                      |
+---------------------------------------------------------------------+
""",
        "objectives": [
            "Definiera input variables med validering",
            "Använda complex types (objects, maps, lists)",
            "Skapa locals för computed values",
            "Exponera outputs för cross-module communication",
            "Hantera sensitive values säkert"
        ]
    },
    "data": {
        "concept": "Data Sources",
        "quote": "Data sources låter dig läsa verkligheten – inte bara skapa den.",
        "explanation": """Data sources i Terraform hämtar information om existerande resurser eller extern data.
Detta är kritiskt för att referera till infrastruktur som inte hanteras av din Terraform-konfiguration.""",
        "ascii": """
+---------------------------------------------------------------------+
|                    DATA SOURCE TYPES                                 |
+---------------------------------------------------------------------+
|                                                                      |
|   +-------------------------------------------------------------+   |
|   |                    DATA SOURCES                              |   |
|   +-----------------+-----------------+-------------------------+   |
|   |   Provider      |   Remote        |   External              |   |
|   |   Data          |   State         |   Data                  |   |
|   +-----------------+-----------------+-------------------------+   |
|   | aws_ami         | terraform_      | http                    |   |
|   | aws_vpc         | remote_state    | external (scripts)      |   |
|   | aws_caller_id   |                 | template_file           |   |
|   | aws_region      |                 | local_file              |   |
|   +-----------------+-----------------+-------------------------+   |
|                                                                      |
|   Användning:                                                        |
|   • Hitta senaste AMI automatiskt                                   |
|   • Referera till VPC skapad av annat team                         |
|   • Hämta secrets från Vault                                        |
|   • Läsa outputs från andra Terraform projects                     |
|                                                                      |
+---------------------------------------------------------------------+
""",
        "objectives": [
            "Använda AWS data sources (ami, vpc, subnets)",
            "Referera till remote state från andra projekt",
            "Använda http och external data sources",
            "Kombinera data sources med resources"
        ]
    },
    "modules": {
        "concept": "Terraform Modules",
        "quote": "Moduler är återanvändbar infrastruktur – bygg en gång, använd överallt.",
        "explanation": """Terraform modules är containers för relaterade resurser. De låter dig skapa abstraktioner,
dela kod mellan projekt, och bygga en intern module registry för ditt team.""",
        "ascii": """
+---------------------------------------------------------------------+
|                    MODULE ARCHITECTURE                               |
+---------------------------------------------------------------------+
|                                                                      |
|   Root Module (main.tf)                                             |
|   +-------------------------------------------------------------+   |
|   |                                                              |   |
|   |  module "vpc" {                                              |   |
|   |    source = "./modules/vpc"                                  |   |
|   |    ...                                                       |   |
|   |  }                                                           |   |
|   |               |                                              |   |
|   |               ▼                                              |   |
|   |  +----------------------------------------+                 |   |
|   |  |  Child Module (modules/vpc/)           |                 |   |
|   |  |  +-- main.tf                           |                 |   |
|   |  |  +-- variables.tf                      |                 |   |
|   |  |  +-- outputs.tf                        |                 |   |
|   |  |  +-- versions.tf                       |                 |   |
|   |  |                                        |                 |   |
|   |  |  Creates: VPC, Subnets, IGW, NAT      |                 |   |
|   |  |  Outputs: vpc_id, subnet_ids          |                 |   |
|   |  +----------------------------------------+                 |   |
|   |                                                              |   |
|   +-------------------------------------------------------------+   |
|                                                                      |
+---------------------------------------------------------------------+
""",
        "objectives": [
            "Skapa egna modules med best practices",
            "Använda modules från Terraform Registry",
            "Implementera module versioning",
            "Designa module interfaces (inputs/outputs)"
        ]
    }
}

# Pro Tips to add to content
PRO_TIPS = {
    "terraform": [
        """
> 💡 **Pro Tip: Formatering**
> Kör alltid `terraform fmt -recursive` innan du commitar.
> Konsekvent formatering = lättare code reviews.
""",
        """
> 💡 **Pro Tip: Validate Early**
> Kör `terraform validate` efter varje ändring.
> Det fångar syntaxfel utan att kontakta provider APIs.
""",
        """
> 💡 **Pro Tip: Plan Output**
> Spara din plan: `terraform plan -out=tfplan`
> Sedan apply: `terraform apply tfplan`
> Detta garanterar att du applicerar exakt det du granskade.
""",
        """
> 💡 **Pro Tip: State Backup**
> Aktivera ALLTID versioning på din S3 state bucket.
> Det har räddat många från katastrofala misstag.
"""
    ],
    "generic": [
        """
> 💡 **Pro Tip:** Använd version control för all infrastrukturkod.
""",
        """
> 💡 **Pro Tip:** Testa alltid i en dev-miljö först.
""",
        """
> 💡 **Pro Tip:** Dokumentera dina beslut i kod-kommentarer.
"""
    ]
}

HANDS_ON_EXERCISE_TEMPLATE = """
---

## 🎯 Hands-on Övning

### Scenario
{scenario}

### Uppgift
{task_description}

### Steg-för-steg

{steps}

### Förväntad Output
```
{expected_output}
```

### Verifiering
{verification}
"""


def enhance_task_content(content: str, task_title: str, module_name: str) -> str:
    """Add V3 pedagogical elements to task content if missing"""

    enhanced = content

    # Check if already has V3 elements
    has_varfor = any(marker in content for marker in ["## Varför", "## Why This", "Varför detta"])
    has_ascii = any(marker in content for marker in ["+", "|", "+", "+"])
    has_pro_tip = any(marker in content for marker in ["Pro Tip", "💡"])

    # If already premium, return as-is
    if has_varfor and has_ascii and has_pro_tip:
        return content

    # Determine topic for enhancement
    topic = None
    title_lower = task_title.lower()
    if "provider" in title_lower:
        topic = "provider"
    elif "state" in title_lower:
        topic = "state"
    elif "variable" in title_lower or "output" in title_lower:
        topic = "variables"
    elif "data source" in title_lower or "lookup" in title_lower:
        topic = "data"
    elif "module" in title_lower:
        topic = "modules"

    # Add V3 intro if missing
    if not has_varfor:
        if topic and topic in TOPIC_ENHANCEMENTS:
            te = TOPIC_ENHANCEMENTS[topic]
            intro = f"""
## Varför {te['concept']} är Kritiskt

> **"{te['quote']}"**

{te['explanation']}

```
{te['ascii']}
```

### Vad du kommer lära dig

Efter denna uppgift kommer du kunna:
"""
            for obj in te['objectives']:
                intro += f"- ✅ {obj}\n"
            intro += "\n---\n\n"

            # Insert after first heading
            first_heading = re.search(r'^#[^#].*$', content, re.MULTILINE)
            if first_heading:
                pos = first_heading.end()
                enhanced = content[:pos] + "\n" + intro + content[pos:]
            else:
                enhanced = intro + content
        else:
            # Generic intro
            intro = f"""
## Varför detta är viktigt

> **"Kunskap utan praktisk tillämpning är bara information."**

Denna uppgift bygger fundamental förståelse som du kommer använda dagligen som DevOps-ingenjör.

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten bakom {task_title}
- ✅ Tillämpa kunskapen i verkliga scenarion
- ✅ Undvika vanliga fallgropar

---

"""
            first_heading = re.search(r'^#[^#].*$', content, re.MULTILINE)
            if first_heading:
                pos = first_heading.end()
                enhanced = content[:pos] + "\n" + intro + content[pos:]

    # Add Pro Tip if missing
    if not has_pro_tip:
        tips = PRO_TIPS.get("terraform" if "terraform" in module_name.lower() else "generic", PRO_TIPS["generic"])
        import random
        tip = random.choice(tips)
        enhanced += "\n" + tip

    return enhanced


def process_module_file(filepath: str) -> tuple[int, int]:
    """Process a single module file and enhance tasks"""

    with open(filepath, 'r') as f:
        content = f.read()

    # Count tasks needing upgrade
    tasks_found = 0
    tasks_upgraded = 0

    # This is a simple detection - we'd need AST parsing for real implementation
    # For now, just report what would be done

    return tasks_found, tasks_upgraded


def main():
    print("=" * 80)
    print("V3 PREMIUM CONTENT UPGRADE SCRIPT")
    print("=" * 80)
    print()

    modules_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "src", "db", "seeds", "modules_v3"
    )

    print(f"Scanning: {modules_dir}")
    print()

    # This script provides templates and shows what enhancements are needed
    # The actual file modifications will be done via direct edits

    print("V3 PEDAGOGICAL REQUIREMENTS:")
    print("-" * 40)
    print("1. 'Varför' section explaining importance")
    print("2. ASCII diagrams for visualization")
    print("3. 'Vad du kommer lära dig' objectives")
    print("4. Pro Tips with 💡")
    print("5. Hands-on exercises")
    print("6. Code examples with explanations")
    print()

    print("TOPIC-SPECIFIC ENHANCEMENTS AVAILABLE:")
    print("-" * 40)
    for topic, data in TOPIC_ENHANCEMENTS.items():
        print(f"• {topic}: {data['concept']}")
    print()

    print("To apply V3 Premium to all modules:")
    print("1. Run the audit script to identify low-scoring tasks")
    print("2. Apply the appropriate TOPIC_ENHANCEMENTS template")
    print("3. Add Pro Tips and Hands-on exercises")
    print("4. Re-run audit to verify score >= 70")


if __name__ == "__main__":
    main()
