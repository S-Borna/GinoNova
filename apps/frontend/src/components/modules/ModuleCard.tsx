"use client"

/**
 * ============================================================================
 * MODULE CARD — Premium SkillsMaps-Style Design
 * ============================================================================
 *
 * Matches SkillsMapCard design exactly:
 * - Glassmorphism with gradient borders
 * - Status badges (Ej påbörjad/Pågående/Klar)
 * - Tags support
 * - XP in meta row
 * - Difficulty level
 *
 * @phase DESIGN-UNIFICATION
 */

import { useState } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import Link from "next/link"
import {
    Lock,
    Circle,
    PlayCircle,
    CheckCircle2,
    ChevronRight,
    Clock,
    BookOpen,
    Zap,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type ModuleStatus = "locked" | "not_started" | "in_progress" | "complete"

export interface ModuleCardProps {
    id: string
    slug: string // Used for URL navigation - ALWAYS use slug, not id
    orderIndex: number
    title: string
    description: string
    icon?: string // emoji
    progress: number // 0-100
    tasksCompleted: number
    totalTasks: number
    status: ModuleStatus
    estimatedHours?: number
    prerequisiteModule?: string // Name of prerequisite if locked
    className?: string
    color?: string // Module color for glow effect
    tags?: string[] // Tags like "CLI", "System Admin", etc.
    xp?: number // XP reward
    difficulty?: "beginner" | "intermediate" | "advanced" | "expert"
}

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, string> = {
    // DOE25 Tenta - Prioriterad tentaplugg!
    "doe25-tenta": "#EF4444",
    // Linux 24/7 - Vår första modul!
    "linux-247": "#FCC624",
    "environment-tooling-setup": "#6366f1",
    "linux-mastery": "#FCC624",
    "shell-scripting-automation": "#4EAA25",
    "git-collaborative-workflows": "#F05032",
    "python-for-devops": "#3776AB",
    "aws-core-services": "#FF9900",
    "infrastructure-as-code-terraform": "#7B42BC",
    "serverless-architecture": "#FF6B35",
    "networking-security": "#00D4AA",
    "docker-fundamentals": "#2496ED",
    "docker-advanced-production": "#066DA5",
    "kubernetes-core": "#326CE5",
    "kubernetes-advanced-gitops": "#1D4ED8",
    "observability-monitoring": "#E6522C",
    "sre-devsecops-capstone": "#10B981",
}

/* ============================================================================
   STATUS CONFIG — Matches SkillsMapCard exactly
   ============================================================================ */

const statusConfig: Record<ModuleStatus, {
    icon: React.ComponentType<{ className?: string }>
    label: string
    badgeClass: string
    buttonText: string
}> = {
    locked: {
        icon: Lock,
        label: "Låst",
        badgeClass: "bg-zinc-800/50 text-zinc-500 border-zinc-700/50",
        buttonText: "Låst"
    },
    not_started: {
        icon: Circle,
        label: "Ej påbörjad",
        badgeClass: "bg-zinc-700/50 text-zinc-400 border-zinc-600/50",
        buttonText: "Börja"
    },
    in_progress: {
        icon: PlayCircle,
        label: "Pågående",
        badgeClass: "bg-purple-500/20 text-purple-300 border-purple-500/30",
        buttonText: "Fortsätt"
    },
    complete: {
        icon: CheckCircle2,
        label: "Klar",
        badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
        buttonText: "Granska"
    }
}

/* ============================================================================
   DIFFICULTY CONFIG
   ============================================================================ */

const difficultyConfig: Record<string, { label: string; color: string }> = {
    beginner: { label: "Nybörjare", color: "text-green-400" },
    intermediate: { label: "Mellan", color: "text-blue-400" },
    advanced: { label: "Avancerad", color: "text-orange-400" },
    expert: { label: "Expert", color: "text-red-400" },
}

/* ============================================================================
   MODULE CARD COMPONENT — Matches SkillsMapCard Design
   ============================================================================ */

export function ModuleCard({
    id,
    slug,
    orderIndex,
    title,
    description,
    icon = "📚",
    progress,
    tasksCompleted,
    totalTasks,
    status,
    estimatedHours,
    prerequisiteModule,
    className,
    color,
    tags = [],
    xp = 0,
    difficulty = "beginner",
}: ModuleCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const config = statusConfig[status] || statusConfig.locked
    const diffConfig = difficultyConfig[difficulty] || difficultyConfig.beginner
    const StatusIcon = config.icon
    const isLocked = status === "locked"
    const isComplete = status === "complete"

    // Get module color based on title or use provided color
    const moduleColor = color || Object.entries(moduleColors).find(([key]) =>
        title.toLowerCase().includes(key.split("-")[0])
    )?.[1] || "#6366f1"

    // Auto-generate tags if not provided
    const displayTags = tags.length > 0 ? tags : generateTagsFromTitle(title)

    // Calculate XP if not provided (estimatedHours * 100)
    const displayXP = xp || (estimatedHours ? estimatedHours * 100 : totalTasks * 50)

    const cardContent = (
        <motion.div
            className={cn(
                "group relative overflow-hidden",
                "rounded-2xl",
                "bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90",
                "border border-white/[0.08]",
                "backdrop-blur-xl",
                "transition-all duration-500",
                isLocked && "opacity-60",
                className
            )}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            whileHover={!isLocked ? {
                scale: 1.02,
                transition: { duration: 0.3 }
            } : {}}
        >
            {/* Gradient border on hover */}
            {!isLocked && (
                <motion.div
                    className="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                    style={{
                        background: `linear-gradient(135deg, ${moduleColor}40, transparent 50%, ${moduleColor}20)`,
                    }}
                />
            )}

            {/* Glow effect */}
            {!isLocked && (
                <motion.div
                    className="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-xl"
                    style={{
                        background: `radial-gradient(circle at center, ${moduleColor}30, transparent 70%)`,
                    }}
                />
            )}

            {/* Card content */}
            <div className="relative p-6">
                {/* Top row: Icon + Status */}
                <div className="flex items-start justify-between mb-4">
                    {/* Icon container with glow */}
                    <motion.div
                        className={cn(
                            "w-14 h-14 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-br from-white/10 to-white/5",
                            "border border-white/10",
                            "shadow-lg"
                        )}
                        style={{
                            boxShadow: isHovered && !isLocked
                                ? `0 0 30px ${moduleColor}40, inset 0 0 20px ${moduleColor}20`
                                : undefined
                        }}
                        animate={isHovered && !isLocked ? { scale: 1.1 } : { scale: 1 }}
                        transition={{ duration: 0.3 }}
                    >
                        <span className="text-3xl">{isLocked ? "🔒" : icon}</span>
                    </motion.div>

                    {/* Status badge — Matches SkillsMapCard */}
                    <div className={cn(
                        "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                        "border text-xs font-medium",
                        config.badgeClass
                    )}>
                        <StatusIcon className="w-3.5 h-3.5" />
                        <span>{config.label}</span>
                    </div>
                </div>

                {/* Title */}
                <h3 className={cn(
                    "text-xl font-bold mb-2",
                    isLocked
                        ? "text-zinc-500"
                        : "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                )}>
                    {title}
                </h3>

                {/* Description */}
                <p className={cn(
                    "text-sm line-clamp-2 mb-4",
                    isLocked ? "text-zinc-600" : "text-zinc-400"
                )}>
                    {description}
                </p>

                {/* Tags — Matches SkillsMapCard */}
                {displayTags.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-4">
                        {displayTags.slice(0, 3).map((tag) => (
                            <span
                                key={tag}
                                className="px-2 py-0.5 text-xs rounded-md bg-white/5 text-zinc-400 border border-white/5"
                            >
                                {tag}
                            </span>
                        ))}
                    </div>
                )}

                {/* Progress bar — Matches SkillsMapCard */}
                <div className="mb-4">
                    <div className="flex items-center justify-between text-xs mb-2">
                        <span className="text-zinc-500">
                            {tasksCompleted} / {totalTasks} tasks
                        </span>
                        <span className={cn(
                            "font-bold",
                            isComplete ? "text-emerald-400" : "text-purple-400"
                        )}>
                            {progress}%
                        </span>
                    </div>
                    <div className="relative h-2 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            className="absolute inset-y-0 left-0 rounded-full"
                            style={{
                                background: isComplete
                                    ? "linear-gradient(90deg, #10b981, #14b8a6)"
                                    : `linear-gradient(90deg, ${moduleColor}, ${moduleColor}cc)`,
                                boxShadow: `0 0 15px ${isComplete ? "#10b981" : moduleColor}50`,
                            }}
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 0.8, ease: "easeOut" }}
                        />
                    </div>
                </div>

                {/* Meta row — Matches SkillsMapCard exactly */}
                <div className="flex items-center gap-4 mb-4 text-xs text-zinc-500">
                    <div className="flex items-center gap-1.5">
                        <BookOpen className="w-3.5 h-3.5" />
                        <span>{totalTasks} noder</span>
                    </div>
                    {estimatedHours && (
                        <div className="flex items-center gap-1.5">
                            <Clock className="w-3.5 h-3.5" />
                            <span>~{estimatedHours}h</span>
                        </div>
                    )}
                    <div className="flex items-center gap-1.5 text-amber-400">
                        <Zap className="w-3.5 h-3.5" />
                        <span className="font-medium">{displayXP} XP</span>
                    </div>
                    <span className={cn("ml-auto font-medium", diffConfig.color)}>
                        {diffConfig.label}
                    </span>
                </div>

                {/* Action button / Locked message — Matches SkillsMapCard */}
                {isLocked ? (
                    <div className="flex items-center justify-center gap-2 py-3 px-4 rounded-xl bg-zinc-800/50 text-zinc-500 text-sm border border-zinc-700/50">
                        <Lock className="w-4 h-4" />
                        <span>Slutför {prerequisiteModule || "föregående"} först</span>
                    </div>
                ) : (
                    <motion.button
                        className={cn(
                            "w-full flex items-center justify-center gap-2",
                            "py-3 px-4 rounded-xl",
                            "font-semibold text-sm",
                            "transition-all duration-300",
                            isComplete
                                ? "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                                : status === "in_progress"
                                    ? "bg-gradient-to-r from-purple-600 to-indigo-600 text-white shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                                    : "bg-gradient-to-r from-zinc-700 to-zinc-600 text-white hover:from-zinc-600 hover:to-zinc-500"
                        )}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                    >
                        {status === "in_progress" && (
                            <Sparkles className="w-4 h-4" />
                        )}
                        <span>{config.buttonText}</span>
                        <ChevronRight className="w-4 h-4" />
                    </motion.button>
                )}
            </div>

            {/* Animated sparkle for complete */}
            {isComplete && isHovered && (
                <motion.div
                    className="absolute top-4 right-4 text-emerald-400"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                >
                    <Sparkles className="w-5 h-5" />
                </motion.div>
            )}
        </motion.div>
    )

    // Wrap in link if not locked
    if (isLocked) {
        return cardContent
    }

    return (
        <Link prefetch={false} href={`/modules/${slug}`} className="block">
            {cardContent}
        </Link>
    )
}

/* ============================================================================
   HELPER: Generate tags from module title
   ============================================================================ */

function generateTagsFromTitle(title: string): string[] {
    const tagMap: Record<string, string[]> = {
        "environment": ["Setup", "Tools", "IDE"],
        "tooling": ["Setup", "Tools", "IDE"],
        "linux": ["CLI", "System Admin", "Shell"],
        "shell": ["Bash", "Scripting", "Automation"],
        "git": ["Version Control", "GitHub", "Collaboration"],
        "python": ["Scripting", "Automation", "API"],
        "aws": ["Cloud", "Infrastructure", "Services"],
        "terraform": ["IaC", "Provisioning", "Cloud"],
        "docker": ["Containers", "DevOps", "Microservices"],
        "kubernetes": ["Orchestration", "K8s", "Containers"],
        "ci/cd": ["Pipelines", "Automation", "Deploy"],
        "networking": ["Security", "VPC", "Protocols"],
        "observability": ["Monitoring", "Logs", "Metrics"],
        "sre": ["Reliability", "DevSecOps", "Production"],
    }

    const lowerTitle = title.toLowerCase()
    for (const [key, tags] of Object.entries(tagMap)) {
        if (lowerTitle.includes(key)) {
            return tags
        }
    }
    return ["DevOps", "Learning"]
}

export default ModuleCard
