"use client"

/**
 * ============================================================================
 * SKILLSMAP CARD — Premium Glassmorphism Design
 * ============================================================================
 *
 * Beautiful SkillsMap card matching the premium design system:
 * - Glassmorphism with gradient borders on hover
 * - Animated progress indicators
 * - Glowing effects and micro-interactions
 * - Consistent with ModuleCard and PlatformSelector styling
 *
 * @phase SKILLSMAPS-INTEGRATION
 */

import { useState } from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    ChevronRight,
    Sparkles,
    Clock,
    Zap,
    BookOpen,
    CheckCircle2,
    PlayCircle,
    Circle,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type SkillsMapStatus = "not_started" | "in_progress" | "complete"

export interface SkillsMapCardProps {
    id: string
    slug: string
    title: string
    description: string
    icon: string // emoji
    color: string // hex color for accent
    totalNodes: number
    completedNodes: number
    totalXP: number
    estimatedHours: number
    status: SkillsMapStatus
    difficulty: "beginner" | "intermediate" | "advanced" | "expert"
    tags?: string[]
    className?: string
}

/* ============================================================================
   STATUS CONFIG
   ============================================================================ */

const statusConfig: Record<SkillsMapStatus, {
    label: string
    icon: React.ComponentType<{ className?: string }>
    badgeClass: string
    buttonText: string
}> = {
    not_started: {
        label: "Ej påbörjad",
        icon: Circle,
        badgeClass: "bg-zinc-700/50 text-zinc-400 border-zinc-600/50",
        buttonText: "Börja",
    },
    in_progress: {
        label: "Pågående",
        icon: PlayCircle,
        badgeClass: "bg-purple-500/20 text-purple-300 border-purple-500/30",
        buttonText: "Fortsätt",
    },
    complete: {
        label: "Klar",
        icon: CheckCircle2,
        badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
        buttonText: "Granska",
    },
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
   SKILLSMAP CARD COMPONENT
   ============================================================================ */

export function SkillsMapCard({
    id,
    slug,
    title,
    description,
    icon,
    color,
    totalNodes,
    completedNodes,
    totalXP,
    estimatedHours,
    status,
    difficulty,
    tags = [],
    className,
}: SkillsMapCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const config = statusConfig[status]
    const diffConfig = difficultyConfig[difficulty]
    const StatusIcon = config.icon

    const progress = totalNodes > 0 ? Math.round((completedNodes / totalNodes) * 100) : 0
    const isComplete = status === "complete"

    return (
        <Link href={`/skillsmaps/${slug}`} className="block">
            <motion.div
                className={cn(
                    "group relative overflow-hidden",
                    "rounded-2xl",
                    "bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90",
                    "border border-white/[0.08]",
                    "backdrop-blur-xl",
                    "transition-all duration-500",
                    className
                )}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                whileHover={{
                    scale: 1.02,
                    transition: { duration: 0.3 }
                }}
            >
                {/* Gradient border on hover */}
                <motion.div
                    className="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                    style={{
                        background: `linear-gradient(135deg, ${color}40, transparent 50%, ${color}20)`,
                    }}
                />

                {/* Glow effect */}
                <motion.div
                    className="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-xl"
                    style={{
                        background: `radial-gradient(circle at center, ${color}30, transparent 70%)`,
                    }}
                />

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
                                boxShadow: isHovered
                                    ? `0 0 30px ${color}40, inset 0 0 20px ${color}20`
                                    : undefined
                            }}
                            animate={isHovered ? { scale: 1.1 } : { scale: 1 }}
                            transition={{ duration: 0.3 }}
                        >
                            <span className="text-3xl">{icon}</span>
                        </motion.div>

                        {/* Status badge */}
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
                        "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent"
                    )}>
                        {title}
                    </h3>

                    {/* Description */}
                    <p className="text-sm text-zinc-400 line-clamp-2 mb-4">
                        {description}
                    </p>

                    {/* Tags */}
                    {tags.length > 0 && (
                        <div className="flex flex-wrap gap-2 mb-4">
                            {tags.slice(0, 3).map((tag) => (
                                <span
                                    key={tag}
                                    className="px-2 py-0.5 text-xs rounded-md bg-white/5 text-zinc-400 border border-white/5"
                                >
                                    {tag}
                                </span>
                            ))}
                        </div>
                    )}

                    {/* Progress bar */}
                    <div className="mb-4">
                        <div className="flex items-center justify-between text-xs mb-2">
                            <span className="text-zinc-500">
                                {completedNodes} / {totalNodes} noder
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
                                        : `linear-gradient(90deg, ${color}, ${color}cc)`,
                                    boxShadow: `0 0 15px ${isComplete ? "#10b981" : color}50`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 0.8, ease: "easeOut" }}
                            />
                        </div>
                    </div>

                    {/* Meta row */}
                    <div className="flex items-center gap-4 mb-4 text-xs text-zinc-500">
                        <div className="flex items-center gap-1.5">
                            <BookOpen className="w-3.5 h-3.5" />
                            <span>{totalNodes} noder</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <Clock className="w-3.5 h-3.5" />
                            <span>~{estimatedHours}h</span>
                        </div>
                        <div className="flex items-center gap-1.5 text-amber-400">
                            <Zap className="w-3.5 h-3.5" />
                            <span className="font-medium">{totalXP} XP</span>
                        </div>
                        <span className={cn("ml-auto font-medium", diffConfig.color)}>
                            {diffConfig.label}
                        </span>
                    </div>

                    {/* Action button */}
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
        </Link>
    )
}

export default SkillsMapCard
