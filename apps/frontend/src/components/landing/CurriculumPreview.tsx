"use client"

/**
 * ============================================================================
 * CURRICULUM PREVIEW — Expandable Module List
 * ============================================================================
 *
 * Design: Elegant accordion-style list showing all 15 modules,
 * with track grouping and expandable task previews.
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    ChevronDown,
    Terminal,
    Cloud,
    Container,
    Rocket,
    Clock,
    FileText,
    Beaker,
    CheckCircle2,
} from "lucide-react"

/* ============================================================================
   CURRICULUM DATA
   ============================================================================ */

type TrackType = "foundation" | "cloud" | "containers" | "platform"

interface ModuleData {
    id: string
    number: number
    title: string
    track: TrackType
    hours: number
    tasks: number
    labs: number
    topics: string[]
}

const TRACK_CONFIG: Record<TrackType, { icon: React.ElementType; color: string; label: string }> = {
    foundation: { icon: Terminal, color: "#6366f1", label: "Foundation" },
    cloud: { icon: Cloud, color: "#8b5cf6", label: "Cloud & Infrastructure" },
    containers: { icon: Container, color: "#06b6d4", label: "Containers & Orchestration" },
    platform: { icon: Rocket, color: "#f97316", label: "Platform Engineering" },
}

const MODULES: ModuleData[] = [
    { id: "m1", number: 1, title: "Linux Fundamentals", track: "foundation", hours: 20, tasks: 12, labs: 6, topics: ["Command Line", "File System", "Users & Permissions", "Process Management"] },
    { id: "m2", number: 2, title: "Shell Scripting", track: "foundation", hours: 16, tasks: 10, labs: 5, topics: ["Bash Basics", "Variables", "Control Flow", "Functions", "Automation"] },
    { id: "m3", number: 3, title: "Version Control with Git", track: "foundation", hours: 14, tasks: 10, labs: 4, topics: ["Git Fundamentals", "Branching", "GitHub Workflows", "Collaboration"] },
    { id: "m4", number: 4, title: "Python for DevOps", track: "foundation", hours: 18, tasks: 12, labs: 5, topics: ["Python Basics", "Scripting", "APIs", "Automation"] },
    { id: "m5", number: 5, title: "Networking Essentials", track: "foundation", hours: 12, tasks: 8, labs: 4, topics: ["TCP/IP", "DNS", "HTTP", "Firewalls", "VPNs"] },
    { id: "m6", number: 6, title: "AWS Core Services", track: "cloud", hours: 22, tasks: 14, labs: 7, topics: ["EC2", "S3", "VPC", "IAM", "RDS"] },
    { id: "m7", number: 7, title: "Infrastructure as Code", track: "cloud", hours: 20, tasks: 12, labs: 6, topics: ["Terraform Basics", "State Management", "Modules", "Best Practices"] },
    { id: "m8", number: 8, title: "Serverless & Lambda", track: "cloud", hours: 14, tasks: 8, labs: 4, topics: ["Lambda Functions", "API Gateway", "DynamoDB", "Step Functions"] },
    { id: "m9", number: 9, title: "CI/CD Pipelines", track: "cloud", hours: 14, tasks: 10, labs: 5, topics: ["GitHub Actions", "Jenkins", "Pipeline Design", "Deployment Strategies"] },
    { id: "m10", number: 10, title: "Docker Deep Dive", track: "containers", hours: 20, tasks: 14, labs: 6, topics: ["Images", "Containers", "Networking", "Volumes", "Compose"] },
    { id: "m11", number: 11, title: "Kubernetes Fundamentals", track: "containers", hours: 24, tasks: 16, labs: 8, topics: ["Pods", "Deployments", "Services", "ConfigMaps", "Secrets"] },
    { id: "m12", number: 12, title: "Kubernetes Advanced", track: "containers", hours: 16, tasks: 10, labs: 5, topics: ["Helm", "Ingress", "RBAC", "Operators", "Service Mesh"] },
    { id: "m13", number: 13, title: "GitOps & ArgoCD", track: "platform", hours: 16, tasks: 10, labs: 5, topics: ["GitOps Principles", "ArgoCD Setup", "App of Apps", "Sync Strategies"] },
    { id: "m14", number: 14, title: "Observability Stack", track: "platform", hours: 22, tasks: 14, labs: 7, topics: ["Prometheus", "Grafana", "Loki", "Alerting", "Dashboards"] },
    { id: "m15", number: 15, title: "SRE & Production Ops", track: "platform", hours: 22, tasks: 14, labs: 6, topics: ["SLOs/SLIs", "Incident Response", "Chaos Engineering", "Runbooks"] },
]

/* ============================================================================
   MODULE CARD COMPONENT
   ============================================================================ */

interface ModuleCardProps {
    module: ModuleData
    index: number
}

function ModuleCard({ module, index }: ModuleCardProps) {
    const [isExpanded, setIsExpanded] = React.useState(false)
    const trackConfig = TRACK_CONFIG[module.track]
    const TrackIcon = trackConfig.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-20px" }}
            transition={{ duration: 0.4, delay: index * 0.03 }}
        >
            <div
                className={cn(
                    "relative rounded-xl overflow-hidden",
                    "bg-white/[0.02] border border-white/[0.06]",
                    "hover:bg-white/[0.04] hover:border-white/[0.1]",
                    "transition-all duration-300",
                    isExpanded && "bg-white/[0.04]"
                )}
            >
                {/* Main row */}
                <button
                    onClick={() => setIsExpanded(!isExpanded)}
                    className="w-full p-4 flex items-center gap-4 text-left"
                >
                    {/* Module number badge */}
                    <div
                        className="flex-shrink-0 w-10 h-10 rounded-lg flex items-center justify-center text-sm font-bold text-white"
                        style={{ backgroundColor: `${trackConfig.color}30` }}
                    >
                        {module.number.toString().padStart(2, "0")}
                    </div>

                    {/* Title & track */}
                    <div className="flex-1 min-w-0">
                        <h4 className="text-white font-medium truncate">
                            {module.title}
                        </h4>
                        <div className="flex items-center gap-2 mt-0.5">
                            <TrackIcon
                                className="w-3.5 h-3.5"
                                style={{ color: trackConfig.color }}
                            />
                            <span className="text-xs text-neutral-500">
                                {trackConfig.label}
                            </span>
                        </div>
                    </div>

                    {/* Stats (hidden on mobile) */}
                    <div className="hidden sm:flex items-center gap-6 text-neutral-400">
                        <div className="flex items-center gap-1.5">
                            <Clock className="w-4 h-4" />
                            <span className="text-sm">{module.hours}h</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <FileText className="w-4 h-4" />
                            <span className="text-sm">{module.tasks}</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <Beaker className="w-4 h-4" />
                            <span className="text-sm">{module.labs}</span>
                        </div>
                    </div>

                    {/* Expand chevron */}
                    <ChevronDown
                        className={cn(
                            "w-5 h-5 text-neutral-500 transition-transform duration-300",
                            isExpanded && "rotate-180"
                        )}
                    />
                </button>

                {/* Expanded content */}
                <AnimatePresence>
                    {isExpanded && (
                        <motion.div
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: "auto", opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.3 }}
                            className="overflow-hidden"
                        >
                            <div className="px-4 pb-4 pt-0">
                                <div className="p-4 rounded-lg bg-black/20 border border-white/[0.05]">
                                    {/* Stats on mobile */}
                                    <div className="flex sm:hidden items-center gap-4 mb-4 text-neutral-400">
                                        <div className="flex items-center gap-1.5">
                                            <Clock className="w-4 h-4" />
                                            <span className="text-sm">{module.hours}h</span>
                                        </div>
                                        <div className="flex items-center gap-1.5">
                                            <FileText className="w-4 h-4" />
                                            <span className="text-sm">{module.tasks} tasks</span>
                                        </div>
                                        <div className="flex items-center gap-1.5">
                                            <Beaker className="w-4 h-4" />
                                            <span className="text-sm">{module.labs} labs</span>
                                        </div>
                                    </div>

                                    {/* Topics */}
                                    <div className="text-xs uppercase tracking-wider text-neutral-500 mb-2">
                                        Topics Covered
                                    </div>
                                    <div className="flex flex-wrap gap-2">
                                        {module.topics.map((topic) => (
                                            <div
                                                key={topic}
                                                className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/[0.05] text-neutral-300 text-sm"
                                            >
                                                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500" />
                                                {topic}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Track color accent line */}
                <div
                    className="absolute left-0 top-0 bottom-0 w-0.5"
                    style={{ backgroundColor: trackConfig.color }}
                />
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function CurriculumPreview() {
    return (
        <section className="relative py-24 bg-neutral-950 overflow-hidden">
            {/* Background */}
            <div className="absolute inset-0">
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
                <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
            </div>

            <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-12"
                >
                    <span className="inline-block px-4 py-1.5 mb-4 text-xs font-semibold tracking-wider uppercase text-primary-400 bg-primary-500/10 rounded-full">
                        Full Curriculum
                    </span>
                    <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
                        36 Modules of{" "}
                        <span className="bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">
                            Deep Learning
                        </span>
                    </h2>
                    <p className="text-lg text-neutral-400 max-w-2xl mx-auto">
                        Click on any module to explore topics covered.
                        Each module includes hands-on labs and real-world projects.
                    </p>
                </motion.div>

                {/* Module list */}
                <div className="space-y-3">
                    {MODULES.map((module, index) => (
                        <ModuleCard key={module.id} module={module} index={index} />
                    ))}
                </div>

                {/* Summary stats */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                    className="mt-12 p-6 rounded-2xl bg-gradient-to-r from-primary-500/10 via-purple-500/10 to-cyan-500/10 border border-white/10"
                >
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                        <div>
                            <div className="text-3xl font-bold text-white">36</div>
                            <div className="text-sm text-neutral-400">Modules</div>
                        </div>
                        <div>
                            <div className="text-3xl font-bold text-white">310h</div>
                            <div className="text-sm text-neutral-400">Content</div>
                        </div>
                        <div>
                            <div className="text-3xl font-bold text-white">384</div>
                            <div className="text-sm text-neutral-400">Tasks</div>
                        </div>
                        <div>
                            <div className="text-3xl font-bold text-white">83</div>
                            <div className="text-sm text-neutral-400">Labs</div>
                        </div>
                    </div>
                </motion.div>
            </div>
        </section>
    )
}

export default CurriculumPreview
