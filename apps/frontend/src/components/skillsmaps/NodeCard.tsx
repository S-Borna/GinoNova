"use client"

/**
 * ============================================================================
 * NODE CARD — Premium Task-Style Card for SkillsMap Nodes
 * ============================================================================
 *
 * Matches TaskCard design with:
 * - Material 3 + Tesla + Apple hybrid styling
 * - 16px border radius
 * - Big emoji icon
 * - XP, time, difficulty indicators
 * - Bookmark support
 * - Premium hover effects
 *
 * @phase SKILLSMAPS-INTEGRATION
 */

import { useState } from "react"
import { cn } from "@/lib/utils"
import { motion } from "framer-motion"
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
   TYPE CONFIG
   ============================================================================ */

const typeConfig: Record<NodeType, {
    label: string
    icon: React.ElementType
    emoji: string
    colorClass: string
    bgClass: string
}> = {
    concept: {
        label: "Koncept",
        icon: BookOpen,
        emoji: "📚",
        colorClass: "text-blue-400",
        bgClass: "bg-blue-500/20",
    },
    practice: {
        label: "Praktik",
        icon: Code2,
        emoji: "💻",
        colorClass: "text-emerald-400",
        bgClass: "bg-emerald-500/20",
    },
    deep_dive: {
        label: "Fördjupning",
        icon: Layers,
        emoji: "🔍",
        colorClass: "text-violet-400",
        bgClass: "bg-violet-500/20",
    },
    project: {
        label: "Projekt",
        icon: Rocket,
        emoji: "🚀",
        colorClass: "text-orange-400",
        bgClass: "bg-orange-500/20",
    },
    challenge: {
        label: "Utmaning",
        icon: Trophy,
        emoji: "🏆",
        colorClass: "text-rose-400",
        bgClass: "bg-rose-500/20",
    },
    quiz: {
        label: "Quiz",
        icon: HelpCircle,
        emoji: "❓",
        colorClass: "text-cyan-400",
        bgClass: "bg-cyan-500/20",
    },
}

/* ============================================================================
   DIFFICULTY CONFIG
   ============================================================================ */

const difficultyConfig: Record<string, { level: number; label: string; color: string }> = {
    easy: { level: 1, label: "Lätt", color: "bg-green-400" },
    medium: { level: 2, label: "Medium", color: "bg-yellow-400" },
    hard: { level: 3, label: "Svår", color: "bg-orange-400" },
    expert: { level: 4, label: "Expert", color: "bg-red-400" },
}

/* ============================================================================
   DIFFICULTY DOTS
   ============================================================================ */

function DifficultyDots({ difficulty }: { difficulty: string }) {
    const config = difficultyConfig[difficulty] || difficultyConfig.medium
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 4 }).map((_, i) => (
                    <div
                        key={i}
                        className={cn(
                            "w-1.5 h-1.5 rounded-full transition-all",
                            i < config.level
                                ? config.color
                                : "bg-zinc-700"
                        )}
                    />
                ))}
            </div>
            <span className="text-xs text-zinc-500">
                {config.label}
            </span>
        </div>
    )
}

/* ============================================================================
   BOOKMARK BUTTON
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
                "p-1.5 rounded-lg transition-all duration-200",
                isBookmarked
                    ? "text-amber-400 bg-amber-500/20"
                    : "text-zinc-500 hover:text-amber-400 hover:bg-amber-500/10"
            )}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            disabled={isLoading}
        >
            {isLoading ? (
                <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
                <Star
                    className={cn("w-4 h-4", isBookmarked && "fill-current")}
                />
            )}
        </motion.button>
    )
}

/* ============================================================================
   NODE CARD COMPONENT
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
        <motion.div
            className={cn(
                "group relative",
                "rounded-2xl",
                "bg-zinc-900/80 backdrop-blur-sm",
                "border border-zinc-800/80",
                "transition-all duration-300",
                isHovered && "border-zinc-700/80 shadow-[0_4px_20px_rgba(0,0,0,0.3)]",
                isComplete && "opacity-80",
                onClick && "cursor-pointer",
                className
            )}
            onClick={handleClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            whileHover={{ y: -2 }}
            transition={{ duration: 0.2 }}
        >
            <div className="p-5">
                {/* Top Row: Icon + Type Badge + Bookmark */}
                <div className="flex items-start justify-between mb-4">
                    {/* Icon container */}
                    <motion.div
                        className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            config.bgClass,
                            "border border-white/5"
                        )}
                        animate={isHovered ? { scale: 1.05 } : { scale: 1 }}
                        transition={{ duration: 0.2 }}
                    >
                        <span className="text-2xl">{config.emoji}</span>
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
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-500/20">
                                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                                <span className="text-xs font-medium text-emerald-300">Klar</span>
                            </div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-purple-500/20">
                                <Loader2 className="w-3.5 h-3.5 text-purple-400 animate-spin" />
                                <span className="text-xs font-medium text-purple-300">Pågår</span>
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

                {/* Node number */}
                <span className="text-xs font-medium text-zinc-600 uppercase tracking-wide">
                    Nod {orderIndex}
                </span>

                {/* Title */}
                <h3 className={cn(
                    "mt-1 text-lg font-semibold leading-tight",
                    "text-white",
                    isComplete && "text-zinc-400"
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
                <div className="flex items-center gap-4 mt-4 pt-4 border-t border-zinc-800">
                    {/* Time */}
                    <div className="flex items-center gap-1.5 text-zinc-500">
                        <Clock className="w-3.5 h-3.5" />
                        <span className="text-xs font-medium">{estimatedMinutes} min</span>
                    </div>

                    {/* XP */}
                    <div className="flex items-center gap-1.5 text-amber-400">
                        <Zap className="w-3.5 h-3.5" />
                        <span className="text-xs font-bold">{xpReward} XP</span>
                    </div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={difficulty} />

                    {/* Action button */}
                    {!isComplete && (
                        <motion.button
                            onClick={(e) => {
                                e.stopPropagation()
                                handleClick()
                            }}
                            disabled={isLoading}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-white text-zinc-900",
                                "hover:bg-zinc-100",
                                isLoading && "opacity-50 cursor-wait"
                            )}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            {isLoading ? (
                                <Loader2 className="w-4 h-4 animate-spin" />
                            ) : isInProgress ? (
                                <>
                                    <span>Fortsätt</span>
                                    <ChevronRight className="w-4 h-4" />
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
        </motion.div>
    )
}

export default NodeCard
