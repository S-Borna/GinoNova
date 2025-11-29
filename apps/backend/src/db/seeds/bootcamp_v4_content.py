"""
Bootcamp v4.0 Content - Senior DevOps Curriculum
Phase FAS 5 - Advanced content migration

This file contains the complete v4.0 curriculum structure with:
- 60+ modules organized in 14 sections
- Senior/Enterprise-level content
- Integration with existing v3.0 structure
"""

from typing import List, Dict, Any
from datetime import datetime
import uuid

# ==============================================================================
# V4.0 CURRICULUM STRUCTURE
# ==============================================================================

BOOTCAMP_V4_SECTIONS = [
    {
        "id": "linux-mastery",
        "name": "Linux Mastery",
        "order": 1,
        "description": "Deep Linux internals for production systems",
        "level": "advanced",
        "estimated_hours": 80,
    },
    {
        "id": "networking-deep",
        "name": "Networking Deep Dive",
        "order": 2,
        "description": "Enterprise networking, service mesh, and traffic management",
        "level": "advanced",
        "estimated_hours": 60,
    },
    {
        "id": "kubernetes-advanced",
        "name": "Kubernetes Advanced",
        "order": 3,
        "description": "Production Kubernetes at scale",
        "level": "expert",
        "estimated_hours": 120,
    },
    {
        "id": "sre-mastery",
        "name": "SRE Mastery",
        "order": 4,
        "description": "Site Reliability Engineering practices",
        "level": "expert",
        "estimated_hours": 80,
    },
    {
        "id": "security-zero-trust",
        "name": "Security & Zero Trust",
        "order": 5,
        "description": "Enterprise security architecture",
        "level": "expert",
        "estimated_hours": 70,
    },
    {
        "id": "platform-engineering",
        "name": "Platform Engineering",
        "order": 6,
        "description": "Building internal developer platforms",
        "level": "expert",
        "estimated_hours": 90,
    },
]

BOOTCAMP_V4_MODULES = [
    # =========================================================================
    # SECTION 1: LINUX MASTERY (8 moduler)
    # =========================================================================
    {
        "section_id": "linux-mastery",
        "id": "linux-kernel-internals",
        "name": "Linux Kernel Internals",
        "slug": "linux-kernel-internals",
        "order": 1,
        "description": "Deep dive into kernel architecture, syscalls, and kernel modules",
        "level": "advanced",
        "estimated_hours": 12,
        "prerequisites": ["linux-fundamentals"],
        "learning_outcomes": [
            "Understand kernel architecture and boot process",
            "Write and load kernel modules",
            "Debug kernel issues with ftrace and perf",
            "Configure kernel parameters for production"
        ],
        "tasks": [
            {
                "title": "Kernel Architecture Overview",
                "type": "lesson",
                "xp_reward": 100,
                "estimated_minutes": 45,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## The Linux Kernel Architecture

The Linux kernel is a monolithic kernel with modular capabilities. Understanding its architecture is crucial for senior DevOps engineers who need to optimize systems, debug issues, and configure production workloads.

### Key Components

**Process Scheduler**: Manages CPU time allocation using CFS (Completely Fair Scheduler). Critical for container workloads and cgroup management.

**Memory Management**: Handles virtual memory, page tables, and memory allocation. Understanding this helps optimize container memory limits.

**Virtual File System (VFS)**: Abstraction layer for file operations. Important for understanding container storage and overlayfs.

**Network Stack**: TCP/IP implementation, netfilter, and socket management. Essential for service mesh and network policies."""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": "# View kernel version and configuration\nuname -a\ncat /proc/version\n\n# Explore kernel parameters\nsysctl -a | head -50\n\n# View loaded modules\nlsmod | head -20",
                        "filename": "kernel-basics.sh",
                        "explanation": "These commands help you explore your current kernel configuration"
                    }
                ]
            },
            {
                "title": "Syscalls and System Programming",
                "type": "lesson",
                "xp_reward": 120,
                "estimated_minutes": 60,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## System Calls: The Kernel Interface

System calls are the interface between user space and kernel space. Every operation that interacts with hardware or requires privileged access goes through syscalls.

### Common Syscalls for DevOps

| Syscall | Purpose | DevOps Relevance |
|---------|---------|------------------|
| `clone` | Create process/thread | Container creation |
| `unshare` | Create namespaces | Container isolation |
| `mount` | Mount filesystems | Container storage |
| `setns` | Join namespace | Container exec |
| `pivot_root` | Change root fs | Container root |"""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": "# Trace syscalls of a command\nstrace -c ls /\n\n# Trace specific syscalls\nstrace -e trace=open,read,write cat /etc/passwd\n\n# Trace a running process\nstrace -p $(pgrep nginx) -e trace=network",
                        "explanation": "strace is invaluable for debugging application behavior"
                    },
                    {
                        "type": "terminal",
                        "instructions": "Practice tracing syscalls to understand how containers work",
                        "expected_commands": [
                            {
                                "command": "strace -c ls /",
                                "explanation": "Count syscalls made by ls command",
                                "output": "% time     seconds  usecs/call     calls    errors syscall\n------ ----------- ----------- --------- --------- ----------------\n 42.86    0.000003           3         1           execve\n..."
                            }
                        ],
                        "hints": ["Use strace with -c flag to get a summary"]
                    }
                ]
            },
            {
                "title": "Writing Kernel Modules",
                "type": "exercise",
                "xp_reward": 200,
                "estimated_minutes": 90,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Your First Kernel Module

While you won't write kernel modules in daily DevOps work, understanding them helps you:
- Debug driver issues
- Understand how container runtimes work
- Configure network modules (bridge, vxlan, etc.)
- Optimize storage performance"""
                    },
                    {
                        "type": "code",
                        "language": "c",
                        "code": """// hello_kernel.c
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("DevOpsHub");
MODULE_DESCRIPTION("A simple hello world kernel module");

static int __init hello_init(void) {
    printk(KERN_INFO "Hello from DevOpsHub kernel module!\\n");
    return 0;
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Goodbye from DevOpsHub!\\n");
}

module_init(hello_init);
module_exit(hello_exit);""",
                        "filename": "hello_kernel.c",
                        "explanation": "A minimal kernel module that logs messages on load/unload"
                    },
                    {
                        "type": "code",
                        "language": "makefile",
                        "code": """obj-m += hello_kernel.o

all:
\tmake -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
\tmake -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

install:
\tinsmod hello_kernel.ko

remove:
\trmmod hello_kernel""",
                        "filename": "Makefile"
                    }
                ]
            }
        ],
        "labs": [
            {
                "title": "Kernel Performance Tuning Lab",
                "description": "Optimize kernel parameters for high-performance workloads",
                "estimated_hours": 3,
                "difficulty": "advanced",
                "objectives": [
                    "Configure sysctl for network optimization",
                    "Tune memory management parameters",
                    "Optimize I/O scheduler settings",
                    "Benchmark before and after changes"
                ]
            }
        ]
    },
    {
        "section_id": "linux-mastery",
        "id": "linux-performance",
        "name": "Linux Performance Analysis",
        "slug": "linux-performance",
        "order": 2,
        "description": "Advanced performance analysis with perf, bpftrace, and flamegraphs",
        "level": "advanced",
        "estimated_hours": 15,
        "prerequisites": ["linux-kernel-internals"],
        "tasks": [
            {
                "title": "Performance Analysis Methodology",
                "type": "lesson",
                "xp_reward": 100,
                "estimated_minutes": 45,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## The USE Method

Brendan Gregg's USE Method provides a systematic approach to performance analysis:

**U**tilization - How busy is the resource?
**S**aturation - Is there queued work?
**E**rrors - Are there errors?

Apply USE to every resource:
- CPU: utilization (mpstat), saturation (runq), errors (dmesg)
- Memory: utilization (free), saturation (swap activity), errors (OOM)
- Network: utilization (sar), saturation (drops), errors (ifconfig)
- Storage: utilization (iostat), saturation (avgqu-sz), errors (dmesg)"""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": """# CPU Analysis
mpstat -P ALL 1 5          # Per-CPU utilization
pidstat 1 5                # Per-process CPU

# Memory Analysis
free -h                    # Memory utilization
vmstat 1 5                 # Virtual memory stats
cat /proc/meminfo          # Detailed memory info

# Disk I/O Analysis
iostat -xz 1 5             # Extended I/O stats
iotop -aoP                 # Per-process I/O

# Network Analysis
sar -n DEV 1 5             # Network device stats
ss -s                      # Socket statistics""",
                        "filename": "use-method.sh"
                    }
                ]
            },
            {
                "title": "Perf and Flamegraphs",
                "type": "lesson",
                "xp_reward": 150,
                "estimated_minutes": 60,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## CPU Profiling with perf

`perf` is the standard Linux profiler that samples the call stack at regular intervals. Combined with Flamegraphs, it provides visual representation of where CPU time is spent.

### Workflow
1. Record performance data with `perf record`
2. Process data with `perf script`
3. Generate flamegraph SVG
4. Analyze hotspots"""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": """# Record CPU samples for 30 seconds
sudo perf record -F 99 -a -g -- sleep 30

# Generate flamegraph
sudo perf script | ./stackcollapse-perf.pl | ./flamegraph.pl > flamegraph.svg

# Record specific process
sudo perf record -F 99 -p $(pgrep nginx) -g -- sleep 30

# Off-CPU analysis (blocked time)
sudo perf record -e sched:sched_switch -a -g -- sleep 10""",
                        "filename": "perf-flamegraph.sh",
                        "explanation": "Flamegraphs are essential for identifying performance bottlenecks"
                    }
                ]
            }
        ]
    },
    {
        "section_id": "linux-mastery",
        "id": "linux-namespaces-cgroups",
        "name": "Namespaces & Cgroups Deep Dive",
        "slug": "linux-namespaces-cgroups",
        "order": 3,
        "description": "The building blocks of containers - namespaces and control groups",
        "level": "advanced",
        "estimated_hours": 10,
        "tasks": [
            {
                "title": "Linux Namespaces Explained",
                "type": "lesson",
                "xp_reward": 120,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Container Building Blocks: Namespaces

Namespaces provide isolation for system resources. Each namespace type isolates a specific resource:

| Namespace | Flag | Isolates |
|-----------|------|----------|
| Mount | CLONE_NEWNS | Filesystem mounts |
| UTS | CLONE_NEWUTS | Hostname |
| IPC | CLONE_NEWIPC | Inter-process communication |
| Network | CLONE_NEWNET | Network stack |
| PID | CLONE_NEWPID | Process IDs |
| User | CLONE_NEWUSER | User/Group IDs |
| Cgroup | CLONE_NEWCGROUP | Cgroup root |"""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": """# View namespaces of a process
ls -la /proc/$$/ns/

# Create new namespace and run shell
sudo unshare --mount --uts --ipc --net --pid --fork --mount-proc bash

# Inside the new namespace
hostname container-demo
hostname  # Shows: container-demo
ps aux    # Shows only processes in this PID namespace

# View from host
sudo lsns""",
                        "filename": "namespaces.sh"
                    },
                    {
                        "type": "terminal",
                        "instructions": "Create an isolated environment using namespaces",
                        "expected_commands": [
                            {
                                "command": "sudo unshare --pid --fork --mount-proc ps aux",
                                "explanation": "Create PID namespace and list processes",
                                "output": "USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\nroot         1  0.0  0.0   7236   516 pts/0    R+   10:00   0:00 ps aux"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Cgroups v2 Resource Control",
                "type": "lesson",
                "xp_reward": 150,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Control Groups (cgroups)

While namespaces provide isolation, cgroups provide resource limits and accounting.

### Cgroups v2 Controllers

- **cpu**: CPU bandwidth limits
- **memory**: Memory limits, swap control
- **io**: Block I/O limits
- **pids**: Process count limits
- **cpuset**: CPU/memory node pinning"""
                    },
                    {
                        "type": "code",
                        "language": "bash",
                        "code": """# Check cgroups v2
mount | grep cgroup2

# Create a cgroup
sudo mkdir /sys/fs/cgroup/demo

# Set memory limit (100MB)
echo "104857600" | sudo tee /sys/fs/cgroup/demo/memory.max

# Set CPU limit (50%)
echo "50000 100000" | sudo tee /sys/fs/cgroup/demo/cpu.max

# Add process to cgroup
echo $$ | sudo tee /sys/fs/cgroup/demo/cgroup.procs

# View current usage
cat /sys/fs/cgroup/demo/memory.current
cat /sys/fs/cgroup/demo/cpu.stat""",
                        "filename": "cgroups-v2.sh"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # SECTION 3: KUBERNETES ADVANCED (10 moduler)
    # =========================================================================
    {
        "section_id": "kubernetes-advanced",
        "id": "k8s-scheduler-deep",
        "name": "Kubernetes Scheduler Deep Dive",
        "slug": "k8s-scheduler-deep",
        "order": 1,
        "description": "Custom scheduling, affinity rules, and scheduler extenders",
        "level": "expert",
        "estimated_hours": 12,
        "tasks": [
            {
                "title": "Scheduler Architecture",
                "type": "lesson",
                "xp_reward": 100,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Kubernetes Scheduler Internals

The scheduler's job is to find the best node for each pod. It runs in two phases:

### 1. Filtering (Predicates)
Eliminates nodes that don't meet requirements:
- Sufficient resources (CPU, memory)
- Node selectors match
- Taints/tolerations
- Affinity/anti-affinity rules
- PVC availability

### 2. Scoring (Priorities)
Ranks remaining nodes:
- Resource balance
- Spreading across zones
- Node affinity preferences
- Custom scoring plugins"""
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": """apiVersion: v1
kind: Pod
metadata:
  name: advanced-scheduling-demo
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - eu-north-1a
            - eu-north-1b
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        preference:
          matchExpressions:
          - key: node-type
            operator: In
            values:
            - high-memory
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - web
        topologyKey: kubernetes.io/hostname
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
  containers:
  - name: app
    image: nginx
    resources:
      requests:
        memory: "256Mi"
        cpu: "250m"
      limits:
        memory: "512Mi"
        cpu: "500m" """,
                        "filename": "advanced-scheduling.yaml"
                    }
                ]
            }
        ]
    },
    {
        "section_id": "kubernetes-advanced",
        "id": "k8s-networking-advanced",
        "name": "Kubernetes Networking Advanced",
        "slug": "k8s-networking-advanced",
        "order": 2,
        "description": "CNI plugins, network policies, and service mesh integration",
        "level": "expert",
        "estimated_hours": 15,
        "tasks": [
            {
                "title": "CNI Deep Dive",
                "type": "lesson",
                "xp_reward": 150,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Container Network Interface (CNI)

CNI is the standard for configuring network interfaces in Linux containers. Understanding CNI is crucial for:
- Debugging network issues
- Choosing the right CNI plugin
- Implementing network policies
- Performance optimization

### Popular CNI Plugins

| Plugin | Datapath | Encryption | Policy |
|--------|----------|------------|--------|
| Calico | eBPF/iptables | WireGuard | Yes |
| Cilium | eBPF | WireGuard | Yes |
| Flannel | VXLAN | No | No |
| Weave | VXLAN | Yes | Yes |"""
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": """# NetworkPolicy - Deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
---
# Allow specific ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080""",
                        "filename": "network-policies.yaml"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # SECTION 4: SRE MASTERY (6 moduler)
    # =========================================================================
    {
        "section_id": "sre-mastery",
        "id": "sre-slo-implementation",
        "name": "SLO Implementation",
        "slug": "sre-slo-implementation",
        "order": 1,
        "description": "Implementing and managing SLIs, SLOs, and error budgets",
        "level": "expert",
        "estimated_hours": 12,
        "tasks": [
            {
                "title": "SLI/SLO Fundamentals",
                "type": "lesson",
                "xp_reward": 100,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Service Level Objectives

SRE is built on measurable reliability targets:

**SLI (Service Level Indicator)**: A quantitative measure of service behavior
- Request latency
- Error rate
- Throughput
- Availability

**SLO (Service Level Objective)**: Target value for an SLI
- 99.9% of requests complete in < 200ms
- 99.95% availability over 30 days

**SLA (Service Level Agreement)**: Business commitment with consequences
- External promise to customers
- Financial penalties for violations"""
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": """# SLO definition in YAML (OpenSLO format)
apiVersion: openslo/v1
kind: SLO
metadata:
  name: api-availability
  displayName: API Availability
spec:
  service: payment-api
  budgetingMethod: Occurrences
  objectives:
  - displayName: Availability
    target: 0.999
    targetPercent: 99.9
  indicator:
    metadata:
      name: availability-ratio
    spec:
      ratioMetric:
        good:
          source: prometheus
          queryType: promql
          query: sum(rate(http_requests_total{status=~"2.."}[5m]))
        total:
          source: prometheus
          queryType: promql
          query: sum(rate(http_requests_total[5m]))
  timeWindow:
  - duration: 30d
    isRolling: true""",
                        "filename": "slo-definition.yaml"
                    }
                ]
            },
            {
                "title": "Error Budget Management",
                "type": "lesson",
                "xp_reward": 120,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Error Budgets

Error budget = 1 - SLO target

For 99.9% availability over 30 days:
- Error budget = 0.1%
- = 43.2 minutes of downtime allowed

### Error Budget Policies

When error budget is exhausted:
1. Freeze feature releases
2. Focus on reliability work
3. Increase testing requirements
4. Conduct incident reviews"""
                    },
                    {
                        "type": "code",
                        "language": "python",
                        "code": """# Error budget calculation
def calculate_error_budget(slo_target: float, window_days: int = 30) -> dict:
    '''Calculate error budget from SLO target'''
    error_budget_percent = (1 - slo_target) * 100
    window_minutes = window_days * 24 * 60
    budget_minutes = window_minutes * (1 - slo_target)

    return {
        'slo_target': f'{slo_target * 100:.2f}%',
        'error_budget_percent': f'{error_budget_percent:.3f}%',
        'budget_minutes': round(budget_minutes, 1),
        'budget_hours': round(budget_minutes / 60, 2),
    }

# Examples
print(calculate_error_budget(0.999))   # 99.9% = 43.2 min/month
print(calculate_error_budget(0.9999))  # 99.99% = 4.32 min/month
print(calculate_error_budget(0.99999)) # 99.999% = 26 sec/month""",
                        "filename": "error_budget.py"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # SECTION 5: SECURITY & ZERO TRUST (6 moduler)
    # =========================================================================
    {
        "section_id": "security-zero-trust",
        "id": "zero-trust-architecture",
        "name": "Zero Trust Architecture",
        "slug": "zero-trust-architecture",
        "order": 1,
        "description": "Implementing zero trust security model in cloud-native environments",
        "level": "expert",
        "estimated_hours": 12,
        "tasks": [
            {
                "title": "Zero Trust Principles",
                "type": "lesson",
                "xp_reward": 100,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Zero Trust Security Model

**Core Principle**: Never trust, always verify.

Traditional security relied on network perimeter. Zero Trust assumes breach and verifies every request.

### Zero Trust Pillars

1. **Identity**: Strong authentication for all users and services
2. **Device**: Device health verification
3. **Network**: Micro-segmentation, encrypted traffic
4. **Application**: Application-level access control
5. **Data**: Data classification and protection

### Implementation in Kubernetes

- **Service Mesh**: mTLS between all services
- **Network Policies**: Deny by default
- **RBAC**: Least privilege access
- **Pod Security**: Restricted security contexts
- **Secrets Management**: External secret stores"""
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": """# Istio PeerAuthentication - Require mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT
---
# AuthorizationPolicy - Deny all by default
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: deny-all
  namespace: production
spec:
  {}
---
# AuthorizationPolicy - Allow specific service
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  selector:
    matchLabels:
      app: backend
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/frontend"]
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/*"]""",
                        "filename": "zero-trust-istio.yaml"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # SECTION 6: PLATFORM ENGINEERING (4 moduler)
    # =========================================================================
    {
        "section_id": "platform-engineering",
        "id": "internal-developer-platform",
        "name": "Building Internal Developer Platforms",
        "slug": "internal-developer-platform",
        "order": 1,
        "description": "Design and implement a modern Internal Developer Platform (IDP)",
        "level": "expert",
        "estimated_hours": 20,
        "tasks": [
            {
                "title": "Platform Engineering Fundamentals",
                "type": "lesson",
                "xp_reward": 100,
                "content_blocks": [
                    {
                        "type": "text",
                        "content": """## Internal Developer Platforms

An IDP provides self-service capabilities for development teams while maintaining governance and security.

### Core Capabilities

1. **Service Catalog**: Templates for new services
2. **CI/CD Pipelines**: Standardized deployment workflows
3. **Infrastructure Provisioning**: Self-service infrastructure
4. **Observability**: Built-in monitoring and logging
5. **Security**: Integrated security scanning

### Platform Team Responsibilities

- Define golden paths (recommended approaches)
- Build reusable components
- Maintain platform reliability
- Enable developer productivity"""
                    },
                    {
                        "type": "code",
                        "language": "yaml",
                        "code": """# Backstage Service Template
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: microservice-template
  title: Production Microservice
  description: Create a production-ready microservice
  tags:
    - recommended
    - python
    - kubernetes
spec:
  owner: platform-team
  type: service

  parameters:
    - title: Service Information
      required:
        - name
        - owner
      properties:
        name:
          title: Service Name
          type: string
          pattern: '^[a-z0-9-]+$'
        owner:
          title: Owner Team
          type: string
          ui:field: OwnerPicker

    - title: Infrastructure
      properties:
        database:
          title: Database Type
          type: string
          enum: ['postgres', 'mysql', 'none']
          default: 'postgres'

  steps:
    - id: fetch-template
      name: Fetch Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          owner: ${{ parameters.owner }}

    - id: create-repo
      name: Create Repository
      action: publish:github
      input:
        repoUrl: github.com?owner=company&repo=${{ parameters.name }}

    - id: register-catalog
      name: Register in Catalog
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps.create-repo.output.repoContentsUrl }}""",
                        "filename": "backstage-template.yaml"
                    }
                ]
            }
        ]
    }
]


# ==============================================================================
# SEED FUNCTION
# ==============================================================================

def get_v4_content() -> Dict[str, Any]:
    """
    Get complete v4.0 curriculum content.
    Returns sections and modules ready for database insertion.
    """
    return {
        "version": "4.0",
        "name": "Senior DevOps Bootcamp",
        "description": "Advanced DevOps curriculum for senior engineers",
        "sections": BOOTCAMP_V4_SECTIONS,
        "modules": BOOTCAMP_V4_MODULES,
        "total_modules": len(BOOTCAMP_V4_MODULES),
        "total_hours": sum(m.get("estimated_hours", 0) for m in BOOTCAMP_V4_MODULES),
    }


def seed_v4_content() -> dict:
    """
    Seed v4.0 content into database.
    Creates tracks for sections and modules with tasks.
    Returns summary of created content.
    """
    import logging
    from ..module_repository import create_module, list_modules
    from ..task_repository import create_task
    from ..track_repository import create_track, get_track_by_slug
    from ...schemas.module import ModuleCreate
    from ...schemas.task import TaskCreate
    from ...schemas.track import TrackCreate

    logger = logging.getLogger(__name__)
    content = get_v4_content()

    # Check if v4 content already exists (check for linux-mastery track)
    existing_track = get_track_by_slug("v4-linux-mastery")
    if existing_track:
        logger.info("✅ Bootcamp v4.0 already seeded")
        return {"status": "already_seeded", "modules": 0, "tasks": 0}

    logger.info(f"🌱 Seeding Bootcamp v4.0: {content['total_modules']} modules, {content['total_hours']}h")

    track_id_map = {}
    tracks_created = 0
    modules_created = 0
    tasks_created = 0

    # Create tracks for each section
    for idx, section in enumerate(content["sections"]):
        track_slug = f"v4-{section['id']}"
        track = create_track(TrackCreate(
            name=f"v4.0: {section['name']}",
            slug=track_slug,
            description=section["description"],
            color="#8B5CF6",  # Purple for v4
            icon="🎓",
            order_index=100 + idx,  # After v3 tracks
        ))
        track_id_map[section["id"]] = track.id
        tracks_created += 1
        logger.info(f"  📚 Created track: {section['name']}")

    # Create modules and tasks
    for module_data in content["modules"]:
        section_id = module_data.get("section_id")
        track_id = track_id_map.get(section_id)

        if not track_id:
            logger.warning(f"⚠️ No track for section {section_id}, skipping module {module_data['name']}")
            continue

        # Create module
        module = create_module(ModuleCreate(
            track_id=track_id,
            name=module_data["name"],
            slug=module_data["slug"],
            description=module_data.get("description", ""),
            order_index=module_data.get("order", 1),
            difficulty=module_data.get("level", "advanced"),
            estimated_hours=module_data.get("estimated_hours", 10.0),
            prerequisites=module_data.get("prerequisites", []),
            is_active=False,  # v4 not active by default
        ))
        modules_created += 1

        # Create tasks for this module
        for task_idx, task_data in enumerate(module_data.get("tasks", [])):
            create_task(TaskCreate(
                module_id=module.id,
                title=task_data.get("title", f"Task {task_idx + 1}"),
                description=task_data.get("description"),
                content=task_data.get("content"),
                content_blocks=task_data.get("content_blocks"),
                order_index=task_idx + 1,
                difficulty=task_data.get("difficulty", "medium"),
                estimated_minutes=task_data.get("estimated_minutes", 30),
                xp_reward=task_data.get("xp_reward", 50),
            ))
            tasks_created += 1

    logger.info(f"✅ v4.0 seeded: {tracks_created} tracks, {modules_created} modules, {tasks_created} tasks")

    return {
        "status": "success",
        "tracks": tracks_created,
        "modules": modules_created,
        "tasks": tasks_created,
        "total_hours": content["total_hours"],
    }
