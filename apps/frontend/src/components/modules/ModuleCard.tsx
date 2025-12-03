"use client"

/**
 * ============================================================================
 * MODULE CARD — Premium SkillsMaps-Style Design
 * ============================================================================
 *
 * Features:
 * - Glassmorphism card with colored glow
 * - Framer Motion hover animations
 * - Progress bar with glow effect
 * - XP indicators in amber
 * - Matches SkillsMaps NodeCard design
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
}

/* ============================================================================
   MODULE COLORS
   ============================================================================ */

const moduleColors: Record<string, string> = {
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
   STATUS CONFIG
   ============================================================================ */

const statusConfig: Record<ModuleStatus, {
    icon: React.ComponentType<{ className?: string }>
    label: string
    color: string
    bgColor: string
    buttonText: string
}> = {
    locked: {
        icon: Lock,
        label: "Locked",
        color: "text-neutral-400",
        bgColor: "bg-neutral-100 dark:bg-neutral-800",
        buttonText: "Locked"
    },
    not_started: {
        icon: Circle,
        label: "Not Started",
        color: "text-neutral-500",
        bgColor: "bg-neutral-100 dark:bg-neutral-800",
        buttonText: "Start"
    },
    in_progress: {
        icon: PlayCircle,
        label: "In Progress",
        color: "text-primary-500",
        bgColor: "bg-primary-100 dark:bg-primary-900/30",
        buttonText: "Continue"
    },
    complete: {
        icon: CheckCircle2,
        label: "Complete",
        color: "text-success-500",
        bgColor: "bg-success-100 dark:bg-success-900/30",
        buttonText: "Review"
    }
}

/* ============================================================================
   MODULE CARD COMPONENT
   ============================================================================ */

export function ModuleCard({
    id,
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
}: ModuleCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const config = statusConfig[status]
    const StatusIcon = config.icon
    const isLocked = status === "locked"
    const isComplete = status === "complete"

    // Get module color based on title or use provided color
    const moduleColor = color || Object.entries(moduleColors).find(([key]) => 
        title.toLowerCase().includes(key.split("-")[0])
    )?.[1] || "#6366f1"

    const cardContent = (
        <motion.div
            className={cn(
                "group relative",
                "rounded-2xl",
                "bg-zinc-900/80 backdrop-blur-sm",
                "border border-zinc-800/80",
                "transition-all duration-300",
                isHovered && !isLocked && "border-zinc-700/80 shadow-[0_4px_20px_rgba(0,0,0,0.3)]",
                isLocked && "opacity-60 cursor-not-allowed",
                !isLocked && "cursor-pointer",
                className
            )}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            whileHover={!isLocked ? { y: -4 } : {}}
            transition={{ duration: 0.2 }}
        >
            {/* Colored glow on hover */}
            {!isLocked && (
                <div
                    className={cn(
                        "absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-300",
                        isHovered && "opacity-100"
                    )}
                    style={{
                        boxShadow: `0 0 40px ${moduleColor}20`,
                    }}
                />
            )}

            {/* Complete sparkle */}
            {isComplete && (
                <motion.div
                    className="absolute top-4 right-4 text-emerald-400"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                >
                    <Sparkles className="w-5 h-5" />
                </motion.div>
            )}

            <div className="relative p-6">
                {/* Top row: Icon + Module number + Status */}
                <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center gap-3">
                        {/* Module icon container */}
                        <motion.div
                            className={cn(
                                "w-14 h-14 rounded-xl flex items-center justify-center",
                                "bg-gradient-to-br from-white/10 to-white/5",
                                "border border-white/10"
                            )}
                            style={{ boxShadow: isHovered && !isLocked ? `0 0 30px ${moduleColor}30` : undefined }}
                            animate={isHovered && !isLocked ? { scale: 1.05 } : { scale: 1 }}
                            transition={{ duration: 0.2 }}
                        >
                            <span className="text-3xl">{isLocked ? "🔒" : icon}</span>
                        </motion.div>
                        <div>
                            <span className="text-xs font-medium text-zinc-500 uppercase tracking-wide">
                                Modul {orderIndex}
                            </span>
                            <h3 className={cn(
                                "font-bold text-lg leading-tight",
                                isLocked ? "text-zinc-500" : "text-white"
                            )}>
                                {title}
                            </h3>
                        </div>
                    </div>

                    {/* Status badge */}
                    <span className={cn(
                        "px-2.5 py-1 text-xs font-medium rounded-full",
                        status === "complete" && "bg-emerald-500/20 text-emerald-300",
                        status === "in_progress" && "bg-purple-500/20 text-purple-300",
                        status === "not_started" && "bg-zinc-700 text-zinc-400",
                        status === "locked" && "bg-zinc-800 text-zinc-500"
                    )}>
                        {status === "complete" ? "Klar" : 
                         status === "in_progress" ? "Pågår" :
                         status === "locked" ? "Låst" : "Starta"}
                    </span>
                </div>

                {/* Description */}
                {description && (
                    <p className={cn(
                        "text-sm line-clamp-2 mb-4",
                        isLocked ? "text-zinc-600" : "text-zinc-400"
                    )}>
                        {description}
                    </p>
                )}

                {/* Meta row */}
                <div className="flex items-center gap-4 mb-4 text-sm">
                    <span className="flex items-center gap-1.5 text-zinc-500">
                        <BookOpen className="w-4 h-4" />
                        {totalTasks} tasks
                    </span>
                    {estimatedHours && (
                        <span className="flex items-center gap-1.5 text-zinc-500">
                            <Clock className="w-4 h-4" />
                            ~{estimatedHours}h
                        </span>
                    )}
                    <span className={cn(
                        "flex items-center gap-1.5 font-medium",
                        isComplete ? "text-emerald-400" : "text-purple-400"
                    )}>
                        <CheckCircle2 className="w-4 h-4" />
                        {tasksCompleted}/{totalTasks}
                    </span>
                </div>

                {/* Progress bar with glow */}
                <div className="mb-4">
                    <div className="flex items-center justify-between text-xs mb-2">
                        <span className="text-zinc-500">Progress</span>
                        <span className={cn(
                            "font-bold",
                            isComplete ? "text-emerald-400" : "text-purple-400"
                        )}>
                            {progress}%
                        </span>
                    </div>
                    <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            className="h-full rounded-full"
                            style={{
                                background: isComplete
                                    ? "linear-gradient(90deg, #10b981, #14b8a6)"
                                    : `linear-gradient(90deg, ${moduleColor}, ${moduleColor}cc)`,
                                boxShadow: isComplete
                                    ? "0 0 10px rgba(16, 185, 129, 0.5)"
                                    : `0 0 10px ${moduleColor}50`,
                            }}
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 0.8, ease: "easeOut" }}
                        />
                    </div>
                </div>

                {/* Action button / Locked message */}
                {isLocked ? (
                    <div className="flex items-center justify-center gap-2 py-3 px-4 rounded-xl bg-zinc-800/50 text-zinc-500 text-sm border border-zinc-700/50">
                        <Lock className="w-4 h-4" />
                        <span>Slutför {prerequisiteModule || "föregående"} först</span>
                    </div>
                ) : (
                    <motion.button
                        className={cn(
                            "w-full flex items-center justify-center gap-2 py-3 px-4 rounded-xl font-medium transition-all duration-200",
                            isComplete
                                ? "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                                : status === "in_progress"
                                    ? "bg-white text-zinc-900 hover:bg-zinc-100"
                                    : "bg-white text-zinc-900 hover:bg-zinc-100"
                        )}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                    >
                        <span>{isComplete ? "Granska" : status === "in_progress" ? "Fortsätt" : "Börja"}</span>
                        <ChevronRight className="w-4 h-4" />
                    </motion.button>
                )}
            </div>
        </motion.div>
    )

    // Wrap in link if not locked
    if (isLocked) {
        return cardContent
    }

    return (
        <Link href={`/modules/${id}`} className="block">
            {cardContent}
        </Link>
    )
}

export default ModuleCard
