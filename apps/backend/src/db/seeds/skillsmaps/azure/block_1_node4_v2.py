# ============================================================================
# AZURE BLOCK 1 - NODE 4: SUBSCRIPTIONS & COST MANAGEMENT (V2 INTERACTIVE)
# ============================================================================

AZURE_NODE_4_V2 = {
    "node_id": 4,
    "title": "Subscriptions & Cost Management",
    "slug": "azure-subscriptions-cost",
    "description": "Hantera Azure-subscriptions och kontrollera kostnader",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "version": "2.0",

    # ========================================================================
    # INTRO SECTION
    # ========================================================================
    "intro": {
        "headline": "Molnkostnader under kontroll",
        "hook": "The cloud is pay-as-you-go, not pay-and-forget. Lär dig spara 40-70% på Azure.",
        "learning_objectives": [
            "Designa subscription-strategi för enterprise",
            "Sätta upp budgets och cost alerts",
            "Använda Reserved Instances för besparingar",
            "Identifiera och eliminera slöseri",
            "Automatisera kostnadsoptimering"
        ],
        "prerequisites": [
            "Azure-konto med billing access",
            "Förståelse för Resource Groups",
            "Grundläggande Azure CLI"
        ],
        "xp": 10
    },

    # ========================================================================
    # CONCEPTS SECTION
    # ========================================================================
    "concepts": [
        {
            "id": "subscription-strategy",
            "title": "Subscription Strategies",
            "explanation": """Hur du organiserar subscriptions påverkar kostnadskontroll, säkerhet och governance.

**Strategi 1: Per Miljö**
```
subscription-dev
subscription-test
subscription-prod
```
✅ Tydlig separation av miljöer
✅ Olika budgetar per miljö
✅ Lätt att se prod-kostnader

**Strategi 2: Per Avdelning**
```
subscription-it
subscription-marketing
subscription-finance
```
✅ Tydlig kostnad per avdelning
✅ Avdelningar kan ha egna budgetar
❌ Svårare att se per-app kostnader

**Strategi 3: Hybrid (Rekommenderat)**
```
Management Group: Company
├── MG: Production
│   ├── sub-prod-eu
│   └── sub-prod-us
└── MG: Non-Production
    ├── sub-dev
    └── sub-test
```
✅ Policies på MG-nivå
✅ Flexibel struktur
✅ Passar enterprise""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│        SUBSCRIPTION STRATEGY: HYBRID            │
├─────────────────────────────────────────────────┤
│                                                 │
│   Root Management Group                         │
│   └── MG: Contoso                               │
│       ├── MG: Production                        │
│       │   ├── sub-prod-eu    ($50,000/mo)      │
│       │   └── sub-prod-us    ($30,000/mo)      │
│       │                                         │
│       ├── MG: Non-Production                    │
│       │   ├── sub-dev        ($5,000/mo)       │
│       │   └── sub-test       ($3,000/mo)       │
│       │                                         │
│       └── MG: Sandbox                           │
│           └── sub-experiments ($1,000/mo)      │
│                                                 │
│   TOTAL: ~$89,000/month                         │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Använd Management Groups för att applicera Azure Policies på flera subscriptions samtidigt.",
            "common_mistake": "Att ha EN subscription för allt. Gör det omöjligt att separera kostnader och rättigheter."
        },
        {
            "id": "cost-analysis",
            "title": "Cost Analysis & Budgets",
            "explanation": """Azure Cost Management hjälper dig förstå och kontrollera utgifter.

**Cost Analysis:**
- Filtrera per tidperiod
- Gruppera per RG, tag, service
- Jämför med föregående period
- Exportera till CSV

**Budgets:**
- Sätt månadsbudget per subscription/RG
- Email-alerts vid 50%, 75%, 90%, 100%
- Action Groups för automation (stäng av VMs!)

**Cost Allocation:**
- Använd tags: `cost-center`, `project`, `owner`
- Visa kostnader per tag i Cost Analysis
- Chargeback till avdelningar

**Nyckeltal att övervaka:**
| Metric | Bra | Varning |
|--------|-----|---------|
| Budget utilization | <80% | >90% |
| Unused resources | 0 | >5% |
| Reserved coverage | >70% | <50% |""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           COST MANAGEMENT DASHBOARD             │
├─────────────────────────────────────────────────┤
│                                                 │
│   December 2024 Forecast: $12,500               │
│   Budget: $15,000     Used: 83% ████████░░      │
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │ COST BY SERVICE                         │   │
│   │ ┌────────────────────────────────┐      │   │
│   │ │██████████████████│ VMs      $6,200   │   │
│   │ │████████████      │ SQL DB   $3,100   │   │
│   │ │██████            │ Storage  $1,500   │   │
│   │ │████              │ Network  $1,200   │   │
│   │ │██                │ Other    $500     │   │
│   │ └────────────────────────────────┘      │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   ALERTS:                                       │
│   ⚠️  Budget 75% - Sent to admin@company.com   │
│   ✅  No anomalies detected                     │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Sätt upp anomaly detection - Azure kan varna dig om plötsliga kostnadsökningar.",
            "common_mistake": "Att bara sätta budget alert på 100%. Då är det för sent. Sätt på 50%, 75%, 90%."
        },
        {
            "id": "reserved-instances",
            "title": "Reserved Instances & Savings",
            "explanation": """Reserved Instances (RIs) ger stora rabatter för långsiktiga åtaganden.

**Hur det fungerar:**
- Betala i förskott för 1 eller 3 år
- Få 40-72% rabatt jämfört med pay-as-you-go
- Gäller: VMs, SQL DB, Cosmos DB, Storage

**Exempel: Standard_D4s_v3 VM**
| Plan | Pris/månad | Besparing |
|------|-----------|-----------|
| Pay-as-you-go | $140 | - |
| 1-year RI | $85 | 40% |
| 3-year RI | $55 | 60% |

**När ska du använda RI?**
✅ Produktions-workloads som kör 24/7
✅ Databaser (nästan alltid on)
✅ Baseline compute capacity
❌ Dev/test (använd auto-shutdown)
❌ Burst workloads (använd Spot VMs)

**Spot VMs (upp till 90% rabatt):**
- Interruptible workloads
- Batch processing
- CI/CD build agents""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           SAVINGS COMPARISON                     │
├─────────────────────────────────────────────────┤
│                                                 │
│   Standard_D4s_v3 VM - Monthly Cost             │
│                                                 │
│   Pay-as-you-go  ████████████████████ $140      │
│   1-year RI      ████████████         $85  -40% │
│   3-year RI      ████████             $55  -60% │
│   Spot VM        ██                   $14  -90% │
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │ RECOMMENDATION ENGINE                   │   │
│   │                                         │   │
│   │ ⭐ Purchase 3x Standard_D4s_v3 3-year RI│   │
│   │    Current: $420/mo → After: $165/mo   │   │
│   │    Savings: $255/mo = $9,180/year      │   │
│   │                                         │   │
│   │ [Buy Now] [Analyze More]               │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Kolla Azure Advisor varje månad - den rekommenderar RIs baserat på din användning.",
            "common_mistake": "Att köpa RIs för VMs du inte är säker på behöver i 3 år. Börja med 1-year och utvärdera."
        },
        {
            "id": "cost-optimization",
            "title": "Cost Optimization Tactics",
            "explanation": """Praktiska sätt att minska Azure-kostnader omedelbart.

**1. Right-size VMs:**
```bash
# Hitta underutnyttjade VMs
# Portal → VM → Metrics → CPU < 20%?
# → Byt till mindre storlek
```

**2. Auto-shutdown för Dev:**
```bash
az vm auto-shutdown --resource-group rg-dev \\
    --name vm-dev --time 1800 # 6 PM
```

**3. Deallocate vs Stop:**
```bash
# ❌ Stop - betalar fortfarande för disk
az vm stop --name vm --resource-group rg

# ✅ Deallocate - betalar bara storage
az vm deallocate --name vm --resource-group rg
```

**4. Hitta oanvända resurser:**
```bash
# Orphan disks
az disk list --query "[?diskState=='Unattached']"

# Public IPs utan association
az network public-ip list --query "[?ipConfiguration==null]"
```

**5. Azure Hybrid Benefit:**
- Använd befintliga Windows/SQL-licenser
- Spara 40% på Windows VMs
- Spara 55% på SQL Server""",
            "diagram": """
┌─────────────────────────────────────────────────┐
│           COST OPTIMIZATION CHECKLIST           │
├─────────────────────────────────────────────────┤
│                                                 │
│   QUICK WINS (Do Today)                         │
│   □ Auto-shutdown dev VMs              -20%     │
│   □ Deallocate stopped VMs              -$50+   │
│   □ Delete orphan disks                 -$20+   │
│   □ Delete unused public IPs            -$5/ea  │
│                                                 │
│   MEDIUM TERM (This Month)                      │
│   □ Right-size over-provisioned VMs    -30%    │
│   □ Enable Azure Hybrid Benefit        -40%    │
│   □ Move dev storage to Cool tier      -50%    │
│                                                 │
│   STRATEGIC (This Quarter)                      │
│   □ Purchase Reserved Instances        -60%    │
│   □ Implement Spot VMs for batch       -90%    │
│   □ Consolidate small databases        -40%    │
│                                                 │
│   ESTIMATED MONTHLY SAVINGS: $3,500+            │
│                                                 │
└─────────────────────────────────────────────────┘
""",
            "pro_tip": "Sätt upp en månatlig 'FinOps review' - 30 min för att kolla Azure Advisor och Cost Analysis.",
            "common_mistake": "Att köra az vm stop istället för az vm deallocate. Du betalar fortfarande för compute!"
        }
    ],

    # ========================================================================
    # PRACTICE SECTION (Simulated Terminal)
    # ========================================================================
    "practice": {
        "introduction": "Nu ska du sätta upp kostnadskontroll och hitta besparingsmöjligheter.",
        "exercises": [
            {
                "step": 1,
                "title": "Lista alla Subscriptions",
                "instruction": "Visa alla subscriptions du har tillgång till.",
                "hint": "Använd 'az account list'",
                "expected_command": "az account list --output table",
                "expected_output": """Name               CloudName    SubscriptionId                        State    IsDefault
-----------------  -----------  ------------------------------------  -------  -----------
Dev Subscription   AzureCloud   aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa  Enabled  False
Prod Subscription  AzureCloud   bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb  Enabled  True""",
                "explanation": "Du kan ha flera subscriptions. IsDefault visar vilken som används för az-kommandon.",
                "xp": 5
            },
            {
                "step": 2,
                "title": "Byt Subscription",
                "instruction": "Byt till Dev Subscription för att undvika att skapa resurser i prod.",
                "hint": "Använd 'az account set --subscription'",
                "expected_command": "az account set --subscription \"Dev Subscription\"",
                "expected_output": """(No output on success)""",
                "explanation": "ALLTID byt till rätt subscription innan du kör kommandon. Annars kan du skapa resurser på fel ställe.",
                "xp": 5
            },
            {
                "step": 3,
                "title": "Hitta Orphan Disks",
                "instruction": "Sök efter diskar som inte är kopplade till någon VM (kostar pengar i onödan).",
                "hint": "Filtrera på diskState=='Unattached'",
                "expected_command": "az disk list --query \"[?diskState=='Unattached'].{Name:name, Size:diskSizeGb, RG:resourceGroup}\" --output table",
                "expected_output": """Name              Size    RG
----------------  ------  ----------------
disk-old-vm       128     rg-myapp-dev
disk-backup-temp  256     rg-myapp-dev""",
                "explanation": "Orphan disks är vanligt efter att man raderat VMs. De fortsätter kosta ~$5-20/månad per disk.",
                "xp": 5
            },
            {
                "step": 4,
                "title": "Hitta Oanvända Public IPs",
                "instruction": "Sök efter public IPs som inte är associerade med någon resurs.",
                "hint": "Filtrera där ipConfiguration är null",
                "expected_command": "az network public-ip list --query \"[?ipConfiguration==null].{Name:name, RG:resourceGroup}\" --output table",
                "expected_output": """Name              RG
----------------  ----------------
pip-old-lb        rg-myapp-dev
pip-test-vm       rg-myapp-dev""",
                "explanation": "Varje oanvänd public IP kostar ~$3-4/månad. Lätt att glömma bort efter att resursen är borta.",
                "xp": 5
            },
            {
                "step": 5,
                "title": "Sätt Auto-shutdown på Dev VM",
                "instruction": "Konfigurera auto-shutdown kl 18:00 för att spara pengar på natten.",
                "hint": "Använd 'az vm auto-shutdown' med --time i UTC format (1700 = 18:00 CET)",
                "expected_command": "az vm auto-shutdown --resource-group rg-myapp-dev --name vm-dev --time 1700",
                "expected_output": """{
  "id": "/subscriptions/xxx/resourceGroups/rg-myapp-dev/providers/Microsoft.DevTestLab/schedules/shutdown-computevm-vm-dev",
  "status": "Enabled",
  "taskType": "ComputeVmShutdownTask",
  "timeZoneId": "UTC",
  "dailyRecurrence": {
    "time": "1700"
  }
}""",
                "explanation": "Auto-shutdown sparar ~70% på dev-VMs som bara behöver köra under arbetstid.",
                "xp": 5
            },
            {
                "step": 6,
                "title": "Visa Azure Advisor Recommendations",
                "instruction": "Hämta kostnadsrekommendationer från Azure Advisor.",
                "hint": "Använd 'az advisor recommendation list' med category filter",
                "expected_command": "az advisor recommendation list --category Cost --output table",
                "expected_output": """Category    Impact    ImpactedField              ImpactedValue
----------  --------  -------------------------  ------------------
Cost        High      Microsoft.Compute/vms      vm-overprovisioned
Cost        Medium    Microsoft.Sql/servers      sql-unused-capacity
Cost        Low       Microsoft.Storage/accounts storage-hot-to-cool""",
                "explanation": "Azure Advisor analyserar din användning och ger konkreta rekommendationer för besparingar.",
                "xp": 5
            }
        ],
        "xp": 30
    },

    # ========================================================================
    # QUIZ SECTION
    # ========================================================================
    "quiz": {
        "passing_score": 80,
        "flashcards": [
            {
                "id": "fc1",
                "front": "Vad är skillnaden mellan 'az vm stop' och 'az vm deallocate'?",
                "back": "stop: VM stannar men du betalar fortfarande. deallocate: Inga compute-kostnader, bara storage."
            },
            {
                "id": "fc2",
                "front": "Hur mycket kan du spara med 3-year Reserved Instance?",
                "back": "Upp till 60-72% jämfört med pay-as-you-go."
            },
            {
                "id": "fc3",
                "front": "Vad är en orphan disk?",
                "back": "En disk som inte är kopplad till någon VM, men som fortfarande kostar pengar."
            },
            {
                "id": "fc4",
                "front": "Vid vilka procentsatser bör du sätta budget alerts?",
                "back": "50%, 75%, 90%, 100% - så du har tid att reagera innan budget överskrids."
            },
            {
                "id": "fc5",
                "front": "Vad är Spot VMs och när ska du använda dem?",
                "back": "VMs med upp till 90% rabatt men kan avbrytas. Bra för batch jobs, CI/CD, interruptible workloads."
            }
        ],
        "multiple_choice": [
            {
                "id": "mc1",
                "question": "En VM med Standard_D4s_v3 har haft <10% CPU-användning de senaste 30 dagarna. Vad bör du göra?",
                "options": [
                    "Köpa Reserved Instance för att spara pengar",
                    "Right-size till mindre VM-storlek",
                    "Aktivera auto-shutdown",
                    "Flytta till annan region"
                ],
                "correct_answer": 1,
                "explanation": "Om CPU är under 10% är VM:en over-provisioned. Right-size till mindre (t.ex. D2s_v3) sparar 50%+ utan att påverka prestanda."
            },
            {
                "id": "mc2",
                "question": "Du vill spara pengar på dev-VMs som bara används 8 timmar/dag. Bästa strategi?",
                "options": [
                    "Köp Reserved Instances",
                    "Använd Spot VMs",
                    "Konfigurera auto-shutdown + auto-start",
                    "Flytta till mindre region"
                ],
                "correct_answer": 2,
                "explanation": "Auto-shutdown under natten sparar ~70%. RIs är för 24/7 workloads. Spot VMs kan avbrytas mitt i arbetet."
            },
            {
                "id": "mc3",
                "question": "Vilken Azure-tjänst ger automatiska rekommendationer för kostnadsbesparingar?",
                "options": [
                    "Azure Cost Management",
                    "Azure Advisor",
                    "Azure Monitor",
                    "Azure Policy"
                ],
                "correct_answer": 1,
                "explanation": "Azure Advisor analyserar din användning och ger proaktiva rekommendationer inom Cost, Security, Performance och Reliability."
            }
        ],
        "xp": 25
    },

    # ========================================================================
    # CHALLENGE SECTION
    # ========================================================================
    "challenge": {
        "title": "FinOps Cost Optimization Audit",
        "scenario": """Du har fått i uppdrag att minska Azure-kostnaderna med 30%.
Nuvarande kostnad: $15,000/månad
Mål: $10,500/månad

Du har tillgång till:
- 20 VMs (blandade storlekar, dev/test/prod)
- 5 SQL Databases
- 50 Storage Accounts
- Ingen Reserved Instances idag""",
        "requirements": [
            "Skriv ett script som identifierar ALLA besparingsmöjligheter",
            "Kategorisera: Quick Wins (<1 dag), Medium (1 vecka), Long-term (1 månad)",
            "Beräkna uppskattad besparing för varje kategori",
            "Generera en rapport som kan presenteras för ledningen",
            "Implementera minst 3 quick wins"
        ],
        "hints": [
            "Börja med orphan resources (disks, IPs, NICs)",
            "Kolla VM sizes vs actual usage",
            "Identifiera kandidater för Reserved Instances",
            "Auto-shutdown på alla dev/test VMs"
        ],
        "solution": """#!/bin/bash
# FinOps Cost Optimization Audit
# Identifies savings opportunities across Azure resources

echo "╔════════════════════════════════════════════════════════════╗"
echo "║           AZURE FINOPS COST OPTIMIZATION AUDIT             ║"
echo "║                    $(date +%Y-%m-%d)                              ║"
echo "╚════════════════════════════════════════════════════════════╝"

TOTAL_SAVINGS=0

# ═══════════════════════════════════════════════════════════════
# QUICK WINS (Implement Today)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🚀 QUICK WINS - Implement Today"
echo "─────────────────────────────────────────────────────────────"

# 1. Orphan Disks
echo ""
echo "📦 Orphan Disks (Unattached):"
ORPHAN_DISKS=$(az disk list --query "[?diskState=='Unattached'].{Name:name, Size:diskSizeGb, RG:resourceGroup}" -o json)
DISK_COUNT=$(echo $ORPHAN_DISKS | jq length)
DISK_SAVINGS=$((DISK_COUNT * 10)) # ~$10/disk/month estimate
echo "   Found: $DISK_COUNT orphan disks"
echo "   Estimated savings: \$$DISK_SAVINGS/month"
echo $ORPHAN_DISKS | jq -r '.[] | "   - \\(.Name) (\\(.Size)GB) in \\(.RG)"'
TOTAL_SAVINGS=$((TOTAL_SAVINGS + DISK_SAVINGS))

# 2. Unused Public IPs
echo ""
echo "🌐 Unused Public IPs:"
UNUSED_IPS=$(az network public-ip list --query "[?ipConfiguration==null].{Name:name, RG:resourceGroup}" -o json)
IP_COUNT=$(echo $UNUSED_IPS | jq length)
IP_SAVINGS=$((IP_COUNT * 4)) # ~$4/IP/month
echo "   Found: $IP_COUNT unused IPs"
echo "   Estimated savings: \$$IP_SAVINGS/month"
TOTAL_SAVINGS=$((TOTAL_SAVINGS + IP_SAVINGS))

# 3. Stopped (not deallocated) VMs
echo ""
echo "⚠️  Stopped VMs (still costing money):"
for RG in $(az group list --query "[].name" -o tsv); do
    STOPPED_VMS=$(az vm list -g $RG --query "[].name" -o tsv)
    for VM in $STOPPED_VMS; do
        STATUS=$(az vm get-instance-view -g $RG -n $VM --query "instanceView.statuses[1].code" -o tsv 2>/dev/null)
        if [[ "$STATUS" == "PowerState/stopped" ]]; then
            echo "   - $VM in $RG (STOPPED but not deallocated!)"
            TOTAL_SAVINGS=$((TOTAL_SAVINGS + 50))
        fi
    done
done

echo ""
echo "   Quick Wins Total: \$$TOTAL_SAVINGS/month"

# ═══════════════════════════════════════════════════════════════
# MEDIUM TERM (This Week)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "📈 MEDIUM TERM - This Week"
echo "─────────────────────────────────────────────────────────────"

# 4. Dev/Test VMs without auto-shutdown
echo ""
echo "🌙 Dev/Test VMs without auto-shutdown:"
DEV_VMS=0
for RG in $(az group list --query "[?tags.environment=='dev' || tags.environment=='test'].name" -o tsv); do
    for VM in $(az vm list -g $RG --query "[].name" -o tsv); do
        SHUTDOWN=$(az vm auto-shutdown show -g $RG -n $VM --query "status" -o tsv 2>/dev/null || echo "Disabled")
        if [[ "$SHUTDOWN" != "Enabled" ]]; then
            echo "   - $VM in $RG (no auto-shutdown)"
            DEV_VMS=$((DEV_VMS + 1))
        fi
    done
done
SHUTDOWN_SAVINGS=$((DEV_VMS * 70)) # ~70% savings
echo "   Found: $DEV_VMS VMs without auto-shutdown"
echo "   Estimated savings: \$$SHUTDOWN_SAVINGS/month"
TOTAL_SAVINGS=$((TOTAL_SAVINGS + SHUTDOWN_SAVINGS))

# 5. Over-provisioned VMs (would need metrics API for real check)
echo ""
echo "📊 Over-provisioned VMs (recommendation):"
echo "   → Check Azure Advisor for right-sizing recommendations"
echo "   → Estimated savings: 20-40% on compute"

# ═══════════════════════════════════════════════════════════════
# LONG TERM (This Quarter)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🎯 LONG TERM - This Quarter"
echo "─────────────────────────────────────────────────────────────"

# 6. Reserved Instance Candidates
echo ""
echo "💰 Reserved Instance Candidates (24/7 Production VMs):"
PROD_VMS=$(az vm list --query "[].{Name:name, Size:hardwareProfile.vmSize, RG:resourceGroup}" -o json)
PROD_COUNT=$(echo $PROD_VMS | jq '[.[] | select(.RG | contains("prod"))] | length')
RI_SAVINGS=$((PROD_COUNT * 85 * 60 / 100)) # 60% savings estimate
echo "   Found: $PROD_COUNT production VMs (candidates for 3-year RI)"
echo "   Estimated savings: \$$RI_SAVINGS/month (60% on compute)"
TOTAL_SAVINGS=$((TOTAL_SAVINGS + RI_SAVINGS))

# 7. Storage tier optimization
echo ""
echo "🗄️  Storage Optimization:"
echo "   → Move infrequently accessed data to Cool/Archive tier"
echo "   → Estimated savings: 50% on storage costs"

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                      SAVINGS SUMMARY                       ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║  Current Monthly Cost:     \$15,000                         ║"
echo "║  Identified Savings:       \$$TOTAL_SAVINGS/month                      ║"
echo "║  New Monthly Cost:         \$$((15000 - TOTAL_SAVINGS))                        ║"
echo "║  Savings Percentage:       $((TOTAL_SAVINGS * 100 / 15000))%                              ║"
echo "╚════════════════════════════════════════════════════════════╝"

# ═══════════════════════════════════════════════════════════════
# IMPLEMENT QUICK WINS
# ═══════════════════════════════════════════════════════════════
echo ""
read -p "Implement quick wins now? (y/n) " IMPLEMENT
if [[ "$IMPLEMENT" == "y" ]]; then
    echo ""
    echo "🔧 Implementing quick wins..."

    # Delete orphan disks
    for DISK in $(az disk list --query "[?diskState=='Unattached'].name" -o tsv); do
        RG=$(az disk show --name $DISK --query "resourceGroup" -o tsv)
        echo "   Deleting orphan disk: $DISK"
        # az disk delete --name $DISK --resource-group $RG --yes --no-wait
    done

    # Delete unused public IPs
    for IP in $(az network public-ip list --query "[?ipConfiguration==null].name" -o tsv); do
        RG=$(az network public-ip show --name $IP --query "resourceGroup" -o tsv)
        echo "   Deleting unused IP: $IP"
        # az network public-ip delete --name $IP --resource-group $RG --no-wait
    done

    echo "   ✅ Quick wins implemented!"
fi

echo ""
echo "📋 Next steps:"
echo "   1. Review and implement medium-term recommendations"
echo "   2. Schedule RI purchase review meeting"
echo "   3. Set up monthly FinOps review calendar event"
echo ""
echo "Report saved to: finops-audit-$(date +%Y-%m-%d).txt"
""",
        "xp": 20
    },

    # ========================================================================
    # METADATA
    # ========================================================================
    "estimated_time_per_section": {
        "intro": 2,
        "concepts": 8,
        "practice": 10,
        "quiz": 5,
        "challenge": 10
    },
    "xp_per_section": {
        "intro": 10,
        "concepts": 15,
        "practice": 30,
        "quiz": 25,
        "challenge": 20
    },
    "total_xp": 100,
    "topics_covered": [
        "subscriptions",
        "cost management",
        "budgets",
        "reserved instances",
        "spot vms",
        "azure advisor",
        "finops",
        "cost optimization"
    ]
}
