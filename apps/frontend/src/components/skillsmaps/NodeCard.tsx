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
                "group relative overflow-hidden",
                "rounded-2xl",
                "bg-[#0e0e18]/95 backdrop-blur-xl",
                "border border-white/[0.06]",
                "transition-all duration-500",
                isHovered && cn(
                    "border-white/10",
                    "shadow-xl",
                ),
                isComplete && "opacity-80",
                onClick && "cursor-pointer",
                className
            )}
            style={{
                boxShadow: isHovered ? `0 20px 50px rgba(0,0,0,0.5), 0 0 30px ${config.accentColor}20` : undefined,
                borderColor: isHovered ? `${config.accentColor}30` : undefined,
            }}
            onClick={handleClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ y: -6, scale: 1.01 }}
            transition={{ duration: 0.35, ease: [0.165, 0.84, 0.44, 1] }}
        >
            {/* Gradient overlay on hover */}
            <motion.div
                className={cn(
                    "absolute inset-0",
                    "bg-gradient-to-br",
                    config.gradient,
                )}
                initial={{ opacity: 0 }}
                animate={{ opacity: isHovered ? 0.04 : 0 }}
                transition={{ duration: 0.4 }}
            />

            {/* Top gradient accent line */}
            <motion.div
                className={cn(
                    "absolute top-0 left-0 right-0 h-1 bg-gradient-to-r",
                    config.gradient,
                )}
                initial={{ scaleX: 0 }}
                animate={{ scaleX: isHovered ? 1 : 0 }}
                transition={{ duration: 0.3 }}
                style={{ transformOrigin: "left" }}
            />

            {/* Shimmer effect */}
            <motion.div
                className="absolute inset-0 opacity-0"
                initial={{ x: "-100%" }}
                animate={{
                    x: isHovered ? "100%" : "-100%",
                    opacity: isHovered ? 1 : 0
                }}
                transition={{ duration: 0.6, ease: "easeInOut" }}
                style={{
                    background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent)",
                }}
            />
            <div className="relative p-5">
                {/* Top Row: Icon + Type Badge + Bookmark */}
                <div className="flex items-start justify-between mb-4">
                    {/* Icon container with gradient and glow */}
                    <motion.div
                        className={cn(
                            "relative w-14 h-14 rounded-xl flex items-center justify-center",
                            config.bgClass,
                            "border border-white/10",
                        )}
                        style={{
                            boxShadow: isHovered
                                ? `0 8px 32px rgba(0,0,0,0.3), 0 0 20px ${config.accentColor}30`
                                : "0 4px 16px rgba(0,0,0,0.2)"
                        }}
                        animate={isHovered ? { scale: 1.1, rotate: 5 } : { scale: 1, rotate: 0 }}
                        transition={{ duration: 0.35, ease: [0.165, 0.84, 0.44, 1] }}
                    >
                        <config.icon className={cn("w-7 h-7", config.colorClass)} />
                        {/* Sparkle effect on hover */}
                        <AnimatePresence>
                            {isHovered && (
                                <motion.div
                                    className="absolute -top-1 -right-1"
                                    initial={{ scale: 0, rotate: -45 }}
                                    animate={{ scale: 1, rotate: 0 }}
                                    exit={{ scale: 0, rotate: 45 }}
                                    transition={{ duration: 0.25 }}
                                >
                                    <Sparkles className={cn("w-4 h-4", config.colorClass)} />
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </motion.div>

                    {/* Right side: Status + Bookmark */}
                    <div className="flex items-center gap-2">
                        {onToggleBookmark && (
                            <BookmarkBtn
                                isBookmarked={isBookmarked}
                                onClick={handleBookmark}
                                isLoading={bookmarkLoading}
                            />
                        )}

                        {isComplete && (
                            <motion.div
                                className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gradient-to-r from-emerald-500/25 to-green-500/25 border border-emerald-500/30"
                                initial={{ scale: 0.8, opacity: 0 }}
                                animate={{ scale: 1, opacity: 1 }}
                            >
                                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                <span className="text-xs font-semibold text-emerald-300">Klar</span>
                            </motion.div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gradient-to-r from-violet-500/25 to-purple-500/25 border border-violet-500/30">
                                <Loader2 className="w-4 h-4 text-violet-400 animate-spin" />
                                <span className="text-xs font-semibold text-violet-300">Pågår</span>
                            </div>
                        )}
                        {!isComplete && !isInProgress && (
                            <span className={cn(
                                "px-2.5 py-1 rounded-full text-xs font-medium",
                                config.bgClass,
                                config.colorClass
                            )}>
                                {config.label}
                            </span>
                        )}
                    </div>
                </div>

                {/* Node number with gradient */}
                <div className="flex items-center gap-2 mb-1">
                    <span className={cn(
                        "text-xs font-bold uppercase tracking-wider bg-gradient-to-r bg-clip-text text-transparent",
                        config.gradient
                    )}>
                        Nod {orderIndex}
                    </span>
                    <div className={cn(
                        "h-px flex-1 bg-gradient-to-r opacity-30",
                        config.gradient
                    )} />
                </div>

                {/* Title with enhanced styling */}
                <h3 className={cn(
                    "text-lg font-bold leading-tight tracking-tight",
                    "text-white",
                    isComplete && "text-zinc-400",
                    "group-hover:text-white transition-colors"
                )}>
                    {title}
                </h3>

                {/* Description */}
                {description && (
                    <p className="mt-2 text-sm text-zinc-500 line-clamp-2">
                        {description}
                    </p>
                )}

                {/* Meta row */}
                <div className="flex items-center gap-4 mt-4 pt-4 border-t border-zinc-800/50">
                    {/* Time with icon */}
                    <div className="flex items-center gap-1.5">
                        <div className="p-1 rounded bg-zinc-800/50">
                            <Clock className="w-3.5 h-3.5 text-zinc-400" />
                        </div>
                        <span className="text-xs font-medium text-zinc-400">{estimatedMinutes} min</span>
                    </div>

                    {/* XP with vibrant gradient and pulse animation */}
                    <motion.div
                        className="flex items-center gap-1.5"
                        animate={{
                            scale: isHovered ? [1, 1.1, 1] : 1
                        }}
                        transition={{ duration: 0.4 }}
                    >
                        <div className="p-1 rounded bg-gradient-to-r from-amber-500/20 to-yellow-500/20">
                            <Zap className="w-3.5 h-3.5 text-amber-400" />
                        </div>
                        <span className="text-xs font-bold bg-gradient-to-r from-amber-400 to-yellow-400 bg-clip-text text-transparent">
                            {xpReward} XP
                        </span>
                    </motion.div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={difficulty} isHovered={isHovered} />

                    {/* Action button - Netflix-style */}
                    {!isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                handleClick()
                            }}
                            disabled={isLoading}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2.5 rounded-xl",
                                "text-sm font-semibold transition-all duration-300",
                                "bg-gradient-to-r",
                                config.gradient,
                                "text-white",
                                isLoading && "opacity-50 cursor-wait"
                            )}
                            style={{
                                boxShadow: `0 4px 20px ${config.accentColor}40`
                            }}
                            whileHover={{
                                scale: 1.05,
                                boxShadow: `0 8px 30px ${config.accentColor}50`
                            }}
                            whileTap={{ scale: 0.95 }}
                        >
                            {isLoading ? (
                                <Loader2 className="w-4 h-4 animate-spin" />
                            ) : isInProgress ? (
                                <>
                                    <span>Fortsätt</span>
                                    <motion.div
                                        animate={{ x: [0, 4, 0] }}
                                        transition={{ duration: 1, repeat: Infinity }}
                                    >
                                        <ChevronRight className="w-4 h-4" />
                                    </motion.div>
                                </>
                            ) : (
                                <>
                                    <Play className="w-3.5 h-3.5" />
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
                                "ml-auto flex items-center gap-1.5 px-4 py-2.5 rounded-xl",
                                "text-sm font-semibold transition-all duration-300",
                                "bg-zinc-800/80 text-zinc-300 border border-zinc-700/50",
                                "hover:bg-zinc-700/80 hover:text-white hover:border-zinc-600/50"
                            )}
                            whileHover={{ scale: 1.03 }}
                            whileTap={{ scale: 0.97 }}
                        >
                            <span>Granska</span>
                            <ChevronRight className="w-4 h-4" />
                        </motion.button>
                    )}
                </div>
            </div>

            {/* Progress indicator for in-progress with shimmer */}
            {isInProgress && (
                <div className="absolute bottom-0 left-0 right-0 h-1.5 bg-zinc-800/50 overflow-hidden">
                    <motion.div
                        className={cn(
                            "h-full bg-gradient-to-r",
                            config.gradient
                        )}
                        initial={{ width: "0%" }}
                        animate={{ width: "45%" }}
                        transition={{ duration: 0.8, ease: [0.165, 0.84, 0.44, 1] }}
                    />
                    {/* Shimmer effect */}
                    <motion.div
                        className="absolute inset-0 bg-gradient-to-r from-transparent via-white/25 to-transparent"
                        animate={{ x: ["-100%", "200%"] }}
                        transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
                    />
                </div>
            )}

            {/* Completion sparkle */}
            <AnimatePresence>
                {isComplete && isHovered && (
                    <motion.div
                        className="absolute top-3 right-3"
                        initial={{ scale: 0, rotate: -180 }}
                        animate={{ scale: 1, rotate: 0 }}
                        exit={{ scale: 0, rotate: 180 }}
                        transition={{ duration: 0.3, ease: [0.34, 1.56, 0.64, 1] }}
                    >
                        <motion.div
                            animate={{ rotate: 360 }}
                            transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                        >
                            <Sparkles className="w-5 h-5 text-emerald-400" />
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.article>
    )
}

export default NodeCard
