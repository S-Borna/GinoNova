"use client"

/**
 * ============================================================================
 * TASK CARD — Material 3 + Tesla + Apple Hybrid Design v2.0
 * ============================================================================
 *
 * Redesigned card with:
 * - 16px border radius (Material 3)
 * - Tesla-style minimal borders and hover shadows
 * - Apple grid spacing and typography
 * - Big icon/emoji at top-left
 * - Prominent 20px medium weight title
 * - Clean meta-row with time, XP, difficulty
 * - Primary accent Start button
 * - Bookmark/Star button (PROMPT 4)
 *
 * @phase D.4 - Modules UI (Redesigned)
 */

import { useState } from "react"
import { cn } from "@/lib/utils"
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
    HelpCircle
} from "lucide-react"
import designTokens from "@/lib/design-tokens"
import { BookmarkButton } from "./BookmarkButton"

/* ============================================================================
   TYPES
   ============================================================================ */

export type TaskType =
    | "foundation"
    | "practice"
    | "deepening"
    | "project"
    | "challenge"
    | "quiz"

export type TaskCardStatus = "not_started" | "in_progress" | "complete"

export interface TaskCardProps {
    id: string
    orderIndex: number
    title: string
    description?: string
    type: TaskType
    difficulty: number // 1-5
    xpReward: number
    estimatedMinutes?: number
    status: TaskCardStatus
    onToggleComplete?: (id: string) => void
    onClick?: (id: string) => void
    isLoading?: boolean
    className?: string
    // Bookmark props (PROMPT 4)
    isBookmarked?: boolean
    onToggleBookmark?: (taskId: string) => Promise<boolean>
}

/* ============================================================================
   TYPE CONFIG — Material 3 Color System
   ============================================================================ */

const typeConfig: Record<TaskType, {
    label: string
    icon: React.ElementType
    emoji: string
    colorClass: string
    bgClass: string
    borderClass: string
}> = {
    foundation: {
        label: "Foundation",
        icon: BookOpen,
        emoji: "📚",
        colorClass: "text-blue-600 dark:text-blue-400",
        bgClass: "bg-blue-50 dark:bg-blue-950/40",
        borderClass: "border-blue-100 dark:border-blue-900/50"
    },
    practice: {
        label: "Practice",
        icon: Code2,
        emoji: "💻",
        colorClass: "text-emerald-600 dark:text-emerald-400",
        bgClass: "bg-emerald-50 dark:bg-emerald-950/40",
        borderClass: "border-emerald-100 dark:border-emerald-900/50"
    },
    deepening: {
        label: "Deep Dive",
        icon: Layers,
        emoji: "🔍",
        colorClass: "text-violet-600 dark:text-violet-400",
        bgClass: "bg-violet-50 dark:bg-violet-950/40",
        borderClass: "border-violet-100 dark:border-violet-900/50"
    },
    project: {
        label: "Project",
        icon: Rocket,
        emoji: "🚀",
        colorClass: "text-orange-600 dark:text-orange-400",
        bgClass: "bg-orange-50 dark:bg-orange-950/40",
        borderClass: "border-orange-100 dark:border-orange-900/50"
    },
    challenge: {
        label: "Challenge",
        icon: Trophy,
        emoji: "🏆",
        colorClass: "text-rose-600 dark:text-rose-400",
        bgClass: "bg-rose-50 dark:bg-rose-950/40",
        borderClass: "border-rose-100 dark:border-rose-900/50"
    },
    quiz: {
        label: "Quiz",
        icon: HelpCircle,
        emoji: "❓",
        colorClass: "text-cyan-600 dark:text-cyan-400",
        bgClass: "bg-cyan-50 dark:bg-cyan-950/40",
        borderClass: "border-cyan-100 dark:border-cyan-900/50"
    }
}

/* ============================================================================
   DIFFICULTY DOTS — Tesla Minimal Style
   ============================================================================ */

function DifficultyDots({ difficulty }: { difficulty: number }) {
    const labels = ["Beginner", "Easy", "Medium", "Hard", "Expert"]
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div
                        key={i}
                        className={cn(
                            "w-1.5 h-1.5 rounded-full transition-all",
                            i < difficulty
                                ? "bg-neutral-800 dark:bg-neutral-200"
                                : "bg-neutral-200 dark:bg-neutral-700"
                        )}
                    />
                ))}
            </div>
            <span className="text-xs text-neutral-500 dark:text-neutral-400">
                {labels[Math.min(difficulty - 1, 4)] || "Beginner"}
            </span>
        </div>
    )
}

/* ============================================================================
   TASK CARD COMPONENT — Material 3 + Tesla + Apple Hybrid
   ============================================================================ */

export function TaskCard({
    id,
    orderIndex,
    title,
    description,
    type,
    difficulty,
    xpReward,
    estimatedMinutes = 15,
    status,
    onToggleComplete,
    onClick,
    isLoading = false,
    className,
    isBookmarked = false,
    onToggleBookmark
}: TaskCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const config = typeConfig[type]
    const isComplete = status === "complete"
    const isInProgress = status === "in_progress"
    const IconComponent = config.icon

    const handleCardClick = () => {
        if (onClick) {
            onClick(id)
        }
    }

    const handleStartClick = (e: React.MouseEvent) => {
        e.stopPropagation()
        if (onClick) {
            onClick(id)
        }
    }

    return (
        <div
            className={cn(
                "group relative transition-all duration-300 ease-out",
                "rounded-2xl", // 16px radius — Material 3
                "bg-white dark:bg-neutral-900",
                "border border-[rgba(0,0,0,0.05)] dark:border-[rgba(255,255,255,0.08)]",
                // Tesla-style hover shadow
                isHovered && "shadow-[0_4px_12px_rgba(0,0,0,0.06)] dark:shadow-[0_4px_12px_rgba(0,0,0,0.3)]",
                // Complete state
                isComplete && "bg-neutral-50 dark:bg-neutral-900/50",
                onClick && "cursor-pointer",
                className
            )}
            onClick={handleCardClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            {/* Card Content */}
            <div className="p-5">
                {/* Top Row: Icon + Type Badge */}
                <div className="flex items-start justify-between mb-4">
                    {/* Big Icon Container */}
                    <div className={cn(
                        "w-12 h-12 rounded-xl flex items-center justify-center",
                        "transition-transform duration-200",
                        config.bgClass,
                        isHovered && "scale-105"
                    )}>
                        <span className="text-2xl" role="img" aria-label={config.label}>
                            {config.emoji}
                        </span>
                    </div>

                    {/* Status / Type Badge + Bookmark */}
                    <div className="flex items-center gap-2">
                        {/* Bookmark Button */}
                        {onToggleBookmark && (
                            <BookmarkButton
                                taskId={id}
                                isBookmarked={isBookmarked}
                                onToggle={onToggleBookmark}
                                size="sm"
                            />
                        )}
                        
                        {isComplete && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/40">
                                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                                <span className="text-xs font-medium text-emerald-700 dark:text-emerald-300">Done</span>
                            </div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-100 dark:bg-blue-900/40">
                                <Loader2 className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400 animate-spin" />
                                <span className="text-xs font-medium text-blue-700 dark:text-blue-300">In Progress</span>
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

                {/* Task Number */}
                <span className="text-xs font-medium text-neutral-400 dark:text-neutral-500 tracking-wide uppercase">
                    Task {orderIndex}
                </span>

                {/* Title — 20px Medium Weight */}
                <h3 className={cn(
                    "mt-1 text-xl font-medium leading-tight tracking-tight", // 20px
                    "text-neutral-900 dark:text-white",
                    isComplete && "text-neutral-500 dark:text-neutral-400"
                )}>
                    {title}
                </h3>

                {/* Description */}
                {description && (
                    <p className={cn(
                        "mt-2 text-sm leading-relaxed",
                        "text-neutral-600 dark:text-neutral-400",
                        "line-clamp-2"
                    )}>
                        {description}
                    </p>
                )}

                {/* Meta Row — Clean minimal style */}
                <div className="flex items-center gap-4 mt-4 pt-4 border-t border-neutral-100 dark:border-neutral-800">
                    {/* Time */}
                    <div className="flex items-center gap-1.5 text-neutral-500 dark:text-neutral-400">
                        <Clock className="w-3.5 h-3.5" />
                        <span className="text-xs font-medium">{estimatedMinutes} min</span>
                    </div>

                    {/* XP */}
                    <div className="flex items-center gap-1.5 text-amber-600 dark:text-amber-400">
                        <Zap className="w-3.5 h-3.5" />
                        <span className="text-xs font-bold">{xpReward} XP</span>
                    </div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={difficulty} />

                    {/* Start Button — Pushed to right */}
                    {!isComplete && (
                        <button
                            onClick={handleStartClick}
                            disabled={isLoading}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-neutral-900 dark:bg-white",
                                "text-white dark:text-neutral-900",
                                "hover:bg-neutral-800 dark:hover:bg-neutral-100",
                                "active:scale-[0.98]",
                                isLoading && "opacity-50 cursor-wait"
                            )}
                        >
                            {isLoading ? (
                                <Loader2 className="w-4 h-4 animate-spin" />
                            ) : isInProgress ? (
                                <>
                                    <span>Continue</span>
                                    <ChevronRight className="w-4 h-4" />
                                </>
                            ) : (
                                <>
                                    <Play className="w-3.5 h-3.5" />
                                    <span>Start</span>
                                </>
                            )}
                        </button>
                    )}

                    {/* Completed state — View button */}
                    {isComplete && (
                        <button
                            onClick={handleStartClick}
                            className={cn(
                                "ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl",
                                "text-sm font-medium transition-all duration-200",
                                "bg-neutral-100 dark:bg-neutral-800",
                                "text-neutral-600 dark:text-neutral-300",
                                "hover:bg-neutral-200 dark:hover:bg-neutral-700"
                            )}
                        >
                            <span>Review</span>
                            <ChevronRight className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>

            {/* Progress indicator for in-progress tasks */}
            {isInProgress && (
                <div className="absolute bottom-0 left-0 right-0 h-1 bg-neutral-100 dark:bg-neutral-800 rounded-b-2xl overflow-hidden">
                    <div className="h-full w-1/3 bg-blue-500 dark:bg-blue-400 animate-pulse" />
                </div>
            )}
        </div>
    )
}

export default TaskCard
