"use client"

/**
 * ============================================================================
 * NODE CARD — MILESTONE 2.0 EDITION
 * ============================================================================
 *
 * 🎬 Disney Magic + Netflix Fräckhet + Google Smart
 *
 * Features:
 * - Material 3 + Tesla + Apple hybrid styling
 * - Netflix-smooth lift animations
 * - Pulsing gradient borders
 * - XP with celebratory micro-interactions
 * - Bookmark with delight animations
 * - Premium hover states with shimmer
 *
 * @phase MILESTONE-2.0
 */

import { useState } from "react"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    CheckCircle2,
    Loader2,
    Clock,
    Zap,
    Play,
    ChevronRight,
    BookOpen,
    Code2,
    Layers,
    Rocket,
    Trophy,
    HelpCircle,
    Star,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type NodeType =
    | "concept"      // 📚 Theory/concept explanation
    | "practice"     // 💻 Hands-on practice
    | "deep_dive"    // 🔍 Advanced deep dive
    | "project"      // 🚀 Mini project
    | "challenge"    // 🏆 Challenge/exercise
    | "quiz"         // ❓ Knowledge check

export type NodeStatus = "not_started" | "in_progress" | "complete"

export interface NodeCardProps {
    id: string
    orderIndex: number
    title: string
    description?: string
    type: NodeType
    difficulty: "easy" | "medium" | "hard" | "expert"
    xpReward: number
    estimatedMinutes: number
    status: NodeStatus
    prerequisites?: string[]
    onClick?: (id: string) => void
    isLoading?: boolean
    className?: string
    // Bookmark props
    isBookmarked?: boolean
    onToggleBookmark?: (nodeId: string) => Promise<boolean>
}

/* ============================================================================
   TYPE CONFIG — Enhanced with more magic ✨
   ============================================================================ */

const typeConfig: Record<NodeType, {
    label: string
    icon: React.ElementType
    emoji: string
    colorClass: string
    bgClass: string
    gradient: string
    glowColor: string
    borderGlow: string
    accentColor: string
}> = {
    concept: {
        label: "Koncept",
        icon: BookOpen,
        emoji: "📚",
        colorClass: "text-violet-300",
        bgClass: "bg-gradient-to-br from-violet-500/20 via-purple-500/15 to-indigo-500/20",
        gradient: "from-violet-500 via-purple-500 to-indigo-500",
        glowColor: "shadow-violet-500/40",
        borderGlow: "hover:border-violet-500/50",
        accentColor: "#a855f7",
    },
    practice: {
        label: "Praktik",
        icon: Code2,
        emoji: "💻",
        colorClass: "text-cyan-300",
        bgClass: "bg-gradient-to-br from-cyan-500/20 via-teal-500/15 to-emerald-500/20",
        gradient: "from-cyan-500 via-teal-500 to-emerald-500",
        glowColor: "shadow-cyan-500/40",
        borderGlow: "hover:border-cyan-500/50",
        accentColor: "#06b6d4",
    },
    deep_dive: {
        label: "Fördjupning",
        icon: Layers,
        emoji: "🔍",
        colorClass: "text-indigo-300",
        bgClass: "bg-gradient-to-br from-indigo-500/20 via-blue-500/15 to-violet-500/20",
        gradient: "from-indigo-500 via-blue-500 to-violet-500",
        glowColor: "shadow-indigo-500/40",
        borderGlow: "hover:border-indigo-500/50",
        accentColor: "#6366f1",
    },
    project: {
        label: "Projekt",
        icon: Rocket,
        emoji: "🚀",
        colorClass: "text-emerald-300",
        bgClass: "bg-gradient-to-br from-emerald-500/20 via-green-500/15 to-teal-500/20",
        gradient: "from-emerald-500 via-green-500 to-teal-500",
        glowColor: "shadow-emerald-500/40",
        borderGlow: "hover:border-emerald-500/50",
        accentColor: "#22c55e",
    },
    challenge: {
        label: "Utmaning",
        icon: Trophy,
        emoji: "🏆",
        colorClass: "text-orange-300",
        bgClass: "bg-gradient-to-br from-orange-500/20 via-amber-500/15 to-yellow-500/20",
        gradient: "from-orange-500 via-amber-500 to-yellow-500",
        glowColor: "shadow-orange-500/40",
        borderGlow: "hover:border-orange-500/50",
        accentColor: "#f97316",
    },
    quiz: {
        label: "Quiz",
        icon: HelpCircle,
        emoji: "❓",
        colorClass: "text-fuchsia-300",
        bgClass: "bg-gradient-to-br from-fuchsia-500/20 via-pink-500/15 to-rose-500/20",
        gradient: "from-fuchsia-500 via-pink-500 to-rose-500",
        glowColor: "shadow-fuchsia-500/40",
        borderGlow: "hover:border-fuchsia-500/50",
        accentColor: "#d946ef",
    },
}

/* ============================================================================
   DIFFICULTY CONFIG — Refined with more punch
   ============================================================================ */

const difficultyConfig: Record<string, { level: number; label: string; color: string; gradient: string; glowColor: string }> = {
    easy: { level: 1, label: "Lätt", color: "bg-gradient-to-r from-emerald-400 to-green-400", gradient: "from-emerald-500 to-green-500", glowColor: "shadow-emerald-500/50" },
    medium: { level: 2, label: "Medium", color: "bg-gradient-to-r from-amber-400 to-yellow-400", gradient: "from-amber-500 to-yellow-500", glowColor: "shadow-amber-500/50" },
    hard: { level: 3, label: "Svår", color: "bg-gradient-to-r from-orange-400 to-red-400", gradient: "from-orange-500 to-red-500", glowColor: "shadow-orange-500/50" },
    expert: { level: 4, label: "Expert", color: "bg-gradient-to-r from-rose-400 to-fuchsia-400", gradient: "from-rose-500 to-fuchsia-500", glowColor: "shadow-rose-500/50" },
}

/* ============================================================================
   DIFFICULTY DOTS — Animated version
   ============================================================================ */

function DifficultyDots({ difficulty, isHovered }: { difficulty: string; isHovered?: boolean }) {
    const config = difficultyConfig[difficulty] || difficultyConfig.medium
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 4 }).map((_, i) => (
                    <motion.div
                        key={i}
                        className={cn(
                            "w-1.5 h-1.5 rounded-full transition-all",
                            i < config.level
                                ? config.color
                                : "bg-zinc-700"
                        )}
                        animate={{
                            scale: isHovered && i < config.level ? [1, 1.3, 1] : 1
                        }}
                        transition={{ duration: 0.3, delay: i * 0.05 }}
                    />
                ))}
            </div>
            <span className="text-xs text-zinc-500 font-medium">
                {config.label}
            </span>
        </div>
    )
}

/* ============================================================================
   BOOKMARK BUTTON — With delight animation ⭐
   ============================================================================ */

function BookmarkBtn({
    isBookmarked,
    onClick,
    isLoading
}: {
    isBookmarked: boolean
    onClick: () => void
    isLoading?: boolean
}) {
    return (
        <motion.button
            onClick={(e) => {
                e.stopPropagation()
                onClick()
            }}
            className={cn(
                "p-2 rounded-xl transition-all duration-300",
                isBookmarked
                    ? "text-amber-400 bg-amber-500/20 shadow-[0_0_15px_rgba(251,191,36,0.3)]"
                    : "text-zinc-500 hover:text-amber-400 hover:bg-amber-500/10"
            )}
            whileHover={{ scale: 1.15, rotate: isBookmarked ? [0, -10, 10, 0] : 0 }}
            whileTap={{ scale: 0.85 }}
            disabled={isLoading}
        >
            <AnimatePresence mode="wait">
                {isLoading ? (
                    <motion.div
                        key="loading"
                        initial={{ opacity: 0, scale: 0.5 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.5 }}
                    >
                        <Loader2 className="w-4 h-4 animate-spin" />
                    </motion.div>
                ) : (
                    <motion.div
                        key="star"
                        initial={{ opacity: 0, scale: 0.5, rotate: -180 }}
                        animate={{ opacity: 1, scale: 1, rotate: 0 }}
                        exit={{ opacity: 0, scale: 0.5, rotate: 180 }}
                    >
                        <Star
                            className={cn("w-4 h-4", isBookmarked && "fill-current")}
                        />
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.button>
    )
}

/* ============================================================================
   NODE CARD COMPONENT — The Magic ✨
   ============================================================================ */

export function NodeCard({
    id,
    orderIndex,
    title,
    description,
    type,
    difficulty,
    xpReward,
    estimatedMinutes,
    status,
    onClick,
    isLoading = false,
    className,
    isBookmarked = false,
    onToggleBookmark,
}: NodeCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const [bookmarkLoading, setBookmarkLoading] = useState(false)

    const config = typeConfig[type]
    const isComplete = status === "complete"
    const isInProgress = status === "in_progress"

    const handleClick = () => {
        if (onClick && !isLoading) {
            onClick(id)
        }
    }

    const handleBookmark = async () => {
        if (onToggleBookmark) {
            setBookmarkLoading(true)
            try {
                await onToggleBookmark(id)
            } finally {
                setBookmarkLoading(false)
            }
        }
    }

    return (
        <motion.article
            className={cn(
                "group relative h-full overflow-hidden",
                "rounded-2xl",
                "bg-[#0d0d12]", // Same as Camp DevOps TaskCard
                "border border-purple-500/10",
                "transition-all duration-500",
                "cursor-pointer",
                isComplete && "opacity-80",
                className
            )}
            style={{
                boxShadow: isHovered
                    ? "0 20px 60px rgba(168,85,247,0.15), 0 0 40px rgba(168,85,247,0.1)"
                    : "0 4px 20px rgba(0,0,0,0.3)",
            }}
            onClick={handleClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ y: -8, scale: 1.02 }}
            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
        >
            {/* Gradient border glow on hover */}
            {isHovered && (
                <motion.div
                    className="absolute inset-0 rounded-2xl pointer-events-none"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    style={{
                        background: "linear-gradient(135deg, rgba(168,85,247,0.2) 0%, rgba(6,182,212,0.1) 50%, rgba(236,72,153,0.15) 100%)",
                    }}
                />
            )}

            <div className="relative p-6 flex flex-col h-full">
                {/* Top Row: Icon + Type Badge + Bookmark */}
                <div className="flex items-start justify-between mb-4">
                    {/* Icon container with glow — Using emoji like Camp DevOps */}
                    <motion.div
                        className={cn(
                            "w-14 h-14 rounded-xl flex items-center justify-center",
                            config.bgClass,
                            "border border-white/10"
                        )}
                        animate={isHovered ? { scale: 1.1, rotate: 5 } : { scale: 1, rotate: 0 }}
                        transition={{ duration: 0.3 }}
                        style={{
                            boxShadow: isHovered ? `0 0 30px ${config.accentColor}40` : "none",
                        }}
                    >
                        <span className="text-3xl">{config.emoji}</span>
                    </motion.div>

                    {/* Right side: Status + Bookmark */}
                    <div className="flex items-center gap-2">
                        {onToggleBookmark && (
                            <motion.button
                                onClick={(e) => {
                                    e.stopPropagation()
                                    handleBookmark()
                                }}
                                className={cn(
                                    "p-2 rounded-xl transition-all duration-200",
                                    isBookmarked
                                        ? "text-amber-400 bg-amber-500/20 border border-amber-500/30"
                                        : "text-zinc-500 hover:text-amber-400 hover:bg-amber-500/10 border border-transparent"
                                )}
                                whileHover={{ scale: 1.15 }}
                                whileTap={{ scale: 0.9 }}
                                disabled={bookmarkLoading}
                            >
                                {bookmarkLoading ? (
                                    <Loader2 className="w-4 h-4 animate-spin" />
                                ) : (
                                    <Star className={cn("w-4 h-4", isBookmarked && "fill-current")} />
                                )}
                            </motion.button>
                        )}

                        {isComplete && (
                            <motion.div
                                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-500/30"
                                animate={{ boxShadow: ["0 0 10px rgba(16,185,129,0.2)", "0 0 20px rgba(16,185,129,0.4)", "0 0 10px rgba(16,185,129,0.2)"] }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                <span className="text-xs font-bold text-emerald-300">Klar</span>
                            </motion.div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-purple-500/20 border border-purple-500/30">
                                <Loader2 className="w-4 h-4 text-purple-400 animate-spin" />
                                <span className="text-xs font-bold text-purple-300">Pågår</span>
                            </div>
                        )}
                        {!isComplete && !isInProgress && (
                            <span className={cn(
                                "px-3 py-1.5 rounded-xl text-xs font-bold border",
                                config.bgClass,
                                config.colorClass,
                                "border-white/10"
                            )}>
                                {config.label}
                            </span>
                        )}
                    </div>
                </div>

                {/* Task number */}
                <span className="text-xs font-bold text-purple-400/60 uppercase tracking-[0.15em]">
                    Task {orderIndex}
                </span>

                {/* Title */}
                <h3 className={cn(
                    "mt-2 text-xl font-bold leading-tight",
                    "bg-gradient-to-r from-white to-white/80 bg-clip-text text-transparent",
                    isComplete && "opacity-60"
                )}>
                    {title}
                </h3>

                {/* Description - flex-grow to push meta to bottom */}
                <div className="flex-grow">
                    {description && (
                        <p className="mt-3 text-sm text-zinc-400 line-clamp-3 leading-relaxed">
                            {description}
                        </p>
                    )}
                </div>

                {/* Meta row - always at bottom */}
                <div className="flex flex-wrap items-center gap-4 mt-5 pt-5 border-t border-purple-500/10">
                    {/* Time */}
                    <div className="flex items-center gap-1.5 text-zinc-400">
                        <Clock className="w-4 h-4" />
                        <span className="text-sm font-medium">{estimatedMinutes} min</span>
                    </div>

                    {/* XP */}
                    <motion.div
                        className="flex items-center gap-1.5"
                        animate={isHovered ? { scale: 1.1 } : { scale: 1 }}
                    >
                        <Zap className="w-4 h-4 text-amber-400" />
                        <span className="text-sm font-black text-amber-400">{xpReward} XP</span>
                    </motion.div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={difficulty} isHovered={isHovered} />

                    {/* Action button */}
                    {!isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                handleClick()
                            }}
                            className={cn(
                                "ml-auto flex items-center gap-2 px-5 py-2.5 rounded-xl",
                                "text-sm font-bold transition-all duration-300",
                                "bg-gradient-to-r from-purple-600 to-pink-600 text-white",
                                "hover:from-purple-500 hover:to-pink-500"
                            )}
                            whileHover={{ scale: 1.05, boxShadow: "0 0 30px rgba(168,85,247,0.4)" }}
                            whileTap={{ scale: 0.95 }}
                        >
                            {isInProgress ? (
                                <>
                                    <span>Fortsätt</span>
                                    <ChevronRight className="w-4 h-4" />
                                </>
                            ) : (
                                <>
                                    <Play className="w-4 h-4" />
                                    <span>Börja</span>
                                </>
                            )}
                        </motion.button>
                    )}

                    {isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                handleClick()
                            }}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-zinc-800 text-zinc-400",
                                "hover:bg-zinc-700 hover:text-zinc-300"
                            )}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <span>Granska</span>
                            <ChevronRight className="w-4 h-4" />
                        </motion.button>
                    )}
                </div>
            </div>

            {/* Progress indicator for in-progress */}
            {isInProgress && (
                <div className="absolute bottom-0 left-0 right-0 h-1 bg-zinc-800 rounded-b-2xl overflow-hidden">
                    <motion.div
                        className="h-full bg-purple-500"
                        initial={{ width: "0%" }}
                        animate={{ width: "33%" }}
                        transition={{ duration: 0.5 }}
                    />
                </div>
            )}
        </motion.article>
    )
}

export default NodeCard
