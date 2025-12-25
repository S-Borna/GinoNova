"use client"

/**
 * ============================================================================
 * SKILLSMAP CARD — MILESTONE 2.0 EDITION
 * ============================================================================
 *
 * 🎬 Disney Magic + Netflix Fräckhet + Google Smart
 *
 * Features:
 * - Luxurious glassmorphism with gradient borders
 * - Netflix-smooth hover animations with lift effect
 * - Animated progress with glow effects
 * - Shimmer highlights on interaction
 * - Micro-interactions that spark joy
 *
 * @phase MILESTONE-2.0
 */

import { useState, useCallback } from "react"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
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
    Star,
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
   STATUS CONFIG — With Netflix-style colors
   ============================================================================ */

const statusConfig: Record<SkillsMapStatus, {
    label: string
    icon: React.ComponentType<{ className?: string }>
    badgeClass: string
    buttonClass: string
    buttonText: string
    glowColor: string
}> = {
    not_started: {
        label: "Ej påbörjad",
        icon: Circle,
        badgeClass: "bg-zinc-800/80 text-zinc-400 border-zinc-700/50",
        buttonClass: "bg-gradient-to-r from-zinc-700/90 to-zinc-600/90 text-white hover:from-zinc-600 hover:to-zinc-500",
        buttonText: "Börja Lära",
        glowColor: "rgba(113, 113, 122, 0.3)",
    },
    in_progress: {
        label: "Pågående",
        icon: PlayCircle,
        badgeClass: "bg-purple-500/20 text-purple-300 border-purple-500/40",
        buttonClass: "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600 text-white shadow-[0_0_30px_rgba(139,92,246,0.4)]",
        buttonText: "Fortsätt",
        glowColor: "rgba(168, 85, 247, 0.5)",
    },
    complete: {
        label: "Avklarad!",
        icon: CheckCircle2,
        badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/40",
        buttonClass: "bg-gradient-to-r from-emerald-600/90 to-teal-600/90 text-white",
        buttonText: "Granska",
        glowColor: "rgba(34, 197, 94, 0.5)",
    },
}

/* ============================================================================
   DIFFICULTY CONFIG — Refined colors
   ============================================================================ */

const difficultyConfig: Record<string, { label: string; color: string; bgColor: string }> = {
    beginner: { label: "Nybörjare", color: "text-emerald-400", bgColor: "bg-emerald-500/10" },
    intermediate: { label: "Mellan", color: "text-cyan-400", bgColor: "bg-cyan-500/10" },
    advanced: { label: "Avancerad", color: "text-orange-400", bgColor: "bg-orange-500/10" },
    expert: { label: "Expert", color: "text-rose-400", bgColor: "bg-rose-500/10" },
}

/* ============================================================================
   SKILLSMAP CARD COMPONENT — The Magic ✨
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
    const isInProgress = status === "in_progress"

    return (
        <Link prefetch={false} href={`/skillsmaps/${slug}`} className="block group">
            <motion.article
                className={cn(
                    "relative overflow-hidden",
                    "rounded-2xl",
                    "backdrop-blur-xl",
                    "transition-colors duration-500",
                    className
                )}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                whileHover={{
                    y: -8,
                    scale: 1.02,
                    transition: { duration: 0.3, ease: [0.165, 0.84, 0.44, 1] }
                }}
                whileTap={{ scale: 0.98 }}
            >
                {/* Background layers */}
                <div className="absolute inset-0 bg-gradient-to-br from-[#0e0e18] via-[#0e0e18] to-[#12121e]" />

                {/* Gradient border effect */}
                <motion.div
                    className="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100"
                    style={{
                        background: `linear-gradient(135deg, ${color}50, transparent 40%, ${color}30)`,
                    }}
                    initial={{ opacity: 0 }}
                    animate={{ opacity: isHovered ? 1 : 0 }}
                    transition={{ duration: 0.4 }}
                />

                {/* Border */}
                <div
                    className={cn(
                        "absolute inset-0 rounded-2xl border transition-all duration-500",
                        isHovered
                            ? "border-white/15"
                            : "border-white/[0.06]"
                    )}
                    style={{
                        borderColor: isHovered ? `${color}40` : undefined,
                    }}
                />

                {/* Glow effect on hover */}
                <motion.div
                    className="absolute -inset-2 rounded-3xl opacity-0 blur-2xl transition-opacity duration-500"
                    style={{
                        background: `radial-gradient(circle at 50% 50%, ${config.glowColor}, transparent 70%)`,
                    }}
                    animate={{ opacity: isHovered ? 0.6 : 0 }}
                />

                {/* Shimmer effect on hover */}
                <motion.div
                    className="absolute inset-0 opacity-0 group-hover:opacity-100"
                    initial={{ x: "-100%" }}
                    animate={{ x: isHovered ? "100%" : "-100%" }}
                    transition={{ duration: 0.8, ease: "easeInOut" }}
                    style={{
                        background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent)",
                    }}
                />

                {/* Card content */}
                <div className="relative p-6">
                    {/* Top row: Icon + Status + Difficulty */}
                    <div className="flex items-start justify-between mb-5">
                        {/* Icon container with premium glow */}
                        <motion.div
                            className={cn(
                                "w-16 h-16 rounded-2xl flex items-center justify-center",
                                "bg-gradient-to-br from-white/10 to-white/[0.02]",
                                "border border-white/10",
                                "shadow-xl"
                            )}
                            style={{
                                boxShadow: isHovered
                                    ? `0 0 40px ${color}40, 0 0 80px ${color}20, inset 0 0 30px ${color}15`
                                    : `0 8px 32px rgba(0,0,0,0.4)`
                            }}
                            animate={{
                                scale: isHovered ? 1.1 : 1,
                                rotate: isHovered ? [0, -5, 5, 0] : 0
                            }}
                            transition={{ duration: 0.4, ease: [0.165, 0.84, 0.44, 1] }}
                        >
                            <span className="text-4xl">{icon}</span>
                        </motion.div>

                        <div className="flex flex-col items-end gap-2">
                            {/* Status badge */}
                            <motion.div
                                className={cn(
                                    "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                                    "border text-xs font-semibold tracking-wide",
                                    "backdrop-blur-sm",
                                    config.badgeClass
                                )}
                                animate={{ scale: isHovered ? 1.05 : 1 }}
                            >
                                <StatusIcon className="w-3.5 h-3.5" />
                                <span>{config.label}</span>
                            </motion.div>

                            {/* Difficulty badge */}
                            <div className={cn(
                                "px-2.5 py-1 rounded-full text-xs font-medium",
                                diffConfig.color,
                                diffConfig.bgColor
                            )}>
                                {diffConfig.label}
                            </div>
                        </div>
                    </div>

                    {/* Title with gradient on hover */}
                    <motion.h3
                        className={cn(
                            "text-xl font-bold mb-2 transition-all duration-300",
                            isHovered
                                ? "bg-gradient-to-r from-white via-white to-white/80 bg-clip-text text-transparent"
                                : "text-white"
                        )}
                    >
                        {title}
                    </motion.h3>

                    {/* Description */}
                    <p className="text-sm text-zinc-400 line-clamp-2 mb-5 leading-relaxed">
                        {description}
                    </p>

                    {/* Tags */}
                    {tags.length > 0 && (
                        <div className="flex flex-wrap gap-2 mb-5">
                            {tags.slice(0, 3).map((tag) => (
                                <span
                                    key={tag}
                                    className={cn(
                                        "px-2.5 py-1 text-xs rounded-lg",
                                        "bg-white/[0.04] text-zinc-400",
                                        "border border-white/[0.06]",
                                        "transition-colors duration-300",
                                        "group-hover:bg-white/[0.06] group-hover:border-white/10"
                                    )}
                                >
                                    {tag}
                                </span>
                            ))}
                        </div>
                    )}

                    {/* Progress section */}
                    <div className="mb-5">
                        <div className="flex items-center justify-between text-xs mb-2.5">
                            <span className="text-zinc-500 font-medium">
                                {completedNodes} av {totalNodes} avsnitt
                            </span>
                            <motion.span
                                className={cn(
                                    "font-bold text-sm",
                                    isComplete ? "text-emerald-400" : "text-purple-400"
                                )}
                                animate={{
                                    scale: isHovered ? [1, 1.15, 1] : 1,
                                }}
                                transition={{ duration: 0.4 }}
                            >
                                {progress}%
                            </motion.span>
                        </div>

                        {/* Progress bar with glow */}
                        <div className="relative h-2.5 bg-zinc-800/80 rounded-full overflow-hidden">
                            {/* Track glow */}
                            <div
                                className="absolute inset-0 opacity-30"
                                style={{
                                    background: `linear-gradient(90deg, ${isComplete ? "#10b981" : color}20, transparent)`,
                                }}
                            />

                            {/* Progress fill */}
                            <motion.div
                                className="absolute inset-y-0 left-0 rounded-full"
                                style={{
                                    background: isComplete
                                        ? "linear-gradient(90deg, #10b981, #14b8a6, #22d3ee)"
                                        : `linear-gradient(90deg, ${color}, ${color}dd, ${color}bb)`,
                                    boxShadow: `0 0 20px ${isComplete ? "#10b981" : color}60`,
                                }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: [0.165, 0.84, 0.44, 1], delay: 0.2 }}
                            />

                            {/* Shimmer on progress bar */}
                            {isInProgress && (
                                <motion.div
                                    className="absolute inset-y-0 w-20"
                                    style={{
                                        background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent)",
                                        left: `${Math.max(0, progress - 10)}%`,
                                    }}
                                    animate={{ x: [-20, 100] }}
                                    transition={{ duration: 1.5, repeat: Infinity, repeatDelay: 1 }}
                                />
                            )}
                        </div>
                    </div>

                    {/* Meta row */}
                    <div className="flex items-center gap-4 mb-5 text-xs text-zinc-500">
                        <div className="flex items-center gap-1.5">
                            <BookOpen className="w-4 h-4 text-zinc-600" />
                            <span>{totalNodes} avsnitt</span>
                        </div>
                        <div className="flex items-center gap-1.5">
                            <Clock className="w-4 h-4 text-zinc-600" />
                            <span>~{estimatedHours}h</span>
                        </div>
                        <motion.div
                            className="flex items-center gap-1.5 text-amber-400"
                            animate={{
                                scale: isHovered ? [1, 1.1, 1] : 1,
                            }}
                            transition={{ duration: 0.4 }}
                        >
                            <Zap className="w-4 h-4" />
                            <span className="font-semibold">{totalXP.toLocaleString()} XP</span>
                        </motion.div>
                    </div>

                    {/* Action button - The star of the show ⭐ */}
                    <motion.div
                        className={cn(
                            "w-full flex items-center justify-center gap-2.5",
                            "py-3.5 px-5 rounded-xl",
                            "font-semibold text-sm",
                            "transition-all duration-300",
                            config.buttonClass
                        )}
                        whileHover={{
                            scale: 1.02,
                            boxShadow: isInProgress
                                ? "0 0 40px rgba(139,92,246,0.5)"
                                : undefined
                        }}
                        whileTap={{ scale: 0.98 }}
                    >
                        {isInProgress && (
                            <motion.div
                                animate={{ rotate: 360 }}
                                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                            >
                                <Sparkles className="w-4 h-4" />
                            </motion.div>
                        )}
                        {isComplete && <Star className="w-4 h-4" />}
                        <span>{config.buttonText}</span>
                        <motion.div
                            animate={{ x: isHovered ? 4 : 0 }}
                            transition={{ duration: 0.2 }}
                        >
                            <ChevronRight className="w-4 h-4" />
                        </motion.div>
                    </motion.div>
                </div>

                {/* Completion celebration effect */}
                <AnimatePresence>
                    {isComplete && isHovered && (
                        <motion.div
                            className="absolute top-4 right-4"
                            initial={{ scale: 0, rotate: -180 }}
                            animate={{ scale: 1, rotate: 0 }}
                            exit={{ scale: 0, rotate: 180 }}
                            transition={{ duration: 0.4, ease: [0.34, 1.56, 0.64, 1] }}
                        >
                            <motion.div
                                animate={{ rotate: 360 }}
                                transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
                            >
                                <Sparkles className="w-6 h-6 text-emerald-400" />
                            </motion.div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </motion.article>
        </Link>
    )
}

export default SkillsMapCard
