"use client"

/**
 * Continue Learning Component
 * Shows user's most recent learning activity with quick resume
 */

import { useEffect, useState } from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Play,
    BookOpen,
    Clock,
    TrendingUp,
    ArrowRight,
    Sparkles,
} from "lucide-react"
import { Button } from "@/components/ui/button"

// ============================================================================
// TYPES
// ============================================================================

interface LastActivity {
    moduleSlug: string
    moduleName: string
    taskTitle?: string
    progress: number
    totalTasks: number
    completedTasks: number
    estimatedMinutes?: number
    lastAccessedAt: Date
    icon?: string
}

interface ContinueLearningProps {
    className?: string
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

/**
 * Get user's last accessed module from localStorage
 */
function getLastActivity(): LastActivity | null {
    if (typeof window === "undefined") return null

    try {
        const stored = localStorage.getItem("last-learning-activity")
        if (!stored) return null

        const activity = JSON.parse(stored)
        return {
            ...activity,
            lastAccessedAt: new Date(activity.lastAccessedAt),
        }
    } catch {
        return null
    }
}

/**
 * Save current learning activity to localStorage
 */
export function saveLastActivity(activity: Omit<LastActivity, "lastAccessedAt">) {
    if (typeof window === "undefined") return

    try {
        localStorage.setItem(
            "last-learning-activity",
            JSON.stringify({
                ...activity,
                lastAccessedAt: new Date().toISOString(),
            })
        )
    } catch (error) {
        console.error("Failed to save last activity:", error)
    }
}

/**
 * Format time ago (e.g., "2 hours ago", "3 days ago")
 */
function formatTimeAgo(date: Date): string {
    const now = new Date()
    const diff = now.getTime() - date.getTime()
    const seconds = Math.floor(diff / 1000)
    const minutes = Math.floor(seconds / 60)
    const hours = Math.floor(minutes / 60)
    const days = Math.floor(hours / 24)

    if (days > 0) return `${days} day${days > 1 ? "s" : ""} ago`
    if (hours > 0) return `${hours} hour${hours > 1 ? "s" : ""} ago`
    if (minutes > 0) return `${minutes} minute${minutes > 1 ? "s" : ""} ago`
    return "Just now"
}

// ============================================================================
// MAIN COMPONENT
// ============================================================================

export function ContinueLearning({ className }: ContinueLearningProps) {
    const [lastActivity, setLastActivity] = useState<LastActivity | null>(null)
    const [mounted, setMounted] = useState(false)

    useEffect(() => {
        setMounted(true)
        setLastActivity(getLastActivity())
    }, [])

    // Don't render on server (avoid hydration mismatch)
    if (!mounted || !lastActivity) {
        return null
    }

    const progressPercent = Math.round(
        (lastActivity.completedTasks / lastActivity.totalTasks) * 100
    )
    const timeAgo = formatTimeAgo(lastActivity.lastAccessedAt)

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4 }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-purple-900/20 via-purple-800/10 to-pink-900/20",
                "border border-purple-500/20",
                "backdrop-blur-sm",
                className
            )}
        >
            {/* Ambient glow */}
            <div className="absolute top-0 right-0 w-64 h-64 bg-purple-500/10 rounded-full blur-3xl" />
            <div className="absolute bottom-0 left-0 w-48 h-48 bg-pink-500/10 rounded-full blur-3xl" />

            {/* Floating sparkle animation */}
            <motion.div
                className="absolute top-6 right-6 text-purple-400/50"
                animate={{
                    rotate: 360,
                    scale: [1, 1.2, 1],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "linear",
                }}
            >
                <Sparkles className="w-5 h-5" />
            </motion.div>

            <div className="relative p-6 md:p-8">
                {/* Header */}
                <div className="flex items-start justify-between mb-6">
                    <div>
                        <div className="flex items-center gap-2 mb-2">
                            <div className="p-2 rounded-xl bg-purple-500/20 border border-purple-500/30">
                                <Play className="w-4 h-4 text-purple-400" />
                            </div>
                            <span className="text-sm font-semibold text-purple-400 uppercase tracking-wider">
                                Continue Learning
                            </span>
                        </div>
                        <h2 className="text-2xl md:text-3xl font-black text-white mb-1">
                            Pick Up Where You Left Off
                        </h2>
                        <p className="text-sm text-zinc-400">
                            Last active {timeAgo}
                        </p>
                    </div>
                </div>

                {/* Module Info Card */}
                <div className={cn(
                    "relative p-5 rounded-2xl mb-6",
                    "bg-gradient-to-br from-zinc-900/80 to-zinc-900/40",
                    "border border-zinc-700/50",
                    "backdrop-blur-sm"
                )}>
                    <div className="flex items-start gap-4">
                        {/* Icon */}
                        {lastActivity.icon && (
                            <div className="text-4xl">{lastActivity.icon}</div>
                        )}
                        {!lastActivity.icon && (
                            <div className={cn(
                                "w-14 h-14 rounded-xl flex items-center justify-center",
                                "bg-gradient-to-br from-purple-500/20 to-pink-500/20",
                                "border border-purple-500/30"
                            )}>
                                <BookOpen className="w-6 h-6 text-purple-400" />
                            </div>
                        )}

                        {/* Content */}
                        <div className="flex-1 min-w-0">
                            <h3 className="text-lg font-bold text-white mb-1 truncate">
                                {lastActivity.moduleName}
                            </h3>
                            {lastActivity.taskTitle && (
                                <p className="text-sm text-zinc-400 mb-3 truncate">
                                    Current: {lastActivity.taskTitle}
                                </p>
                            )}

                            {/* Progress Bar */}
                            <div className="mb-3">
                                <div className="flex items-center justify-between text-xs mb-2">
                                    <span className="text-zinc-400 font-medium">Progress</span>
                                    <span className="font-bold text-purple-400">{progressPercent}%</span>
                                </div>
                                <div className="relative w-full h-2 bg-zinc-800 rounded-full overflow-hidden">
                                    <motion.div
                                        initial={{ width: 0 }}
                                        animate={{ width: `${progressPercent}%` }}
                                        transition={{ duration: 1, ease: "easeOut" }}
                                        className={cn(
                                            "h-full rounded-full",
                                            "bg-gradient-to-r from-purple-600 to-pink-500",
                                            "shadow-[0_0_10px_rgba(168,85,247,0.5)]"
                                        )}
                                    />
                                </div>
                            </div>

                            {/* Meta Info */}
                            <div className="flex items-center gap-4 text-xs text-zinc-500">
                                <span className="flex items-center gap-1">
                                    <BookOpen className="w-3 h-3" />
                                    {lastActivity.completedTasks}/{lastActivity.totalTasks} tasks
                                </span>
                                {lastActivity.estimatedMinutes && (
                                    <span className="flex items-center gap-1">
                                        <Clock className="w-3 h-3" />
                                        {lastActivity.estimatedMinutes} min remaining
                                    </span>
                                )}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Action Buttons */}
                <div className="flex flex-col sm:flex-row gap-3">
                    <Link
                        href={`/study/${lastActivity.moduleSlug}`}
                        className="flex-1"
                    >
                        <Button
                            size="lg"
                            className={cn(
                                "w-full h-12 rounded-xl font-semibold",
                                "bg-gradient-to-r from-purple-600 to-pink-600",
                                "hover:from-purple-500 hover:to-pink-500",
                                "border border-purple-400/20",
                                "shadow-[0_0_20px_rgba(168,85,247,0.3)]",
                                "hover:shadow-[0_0_30px_rgba(168,85,247,0.5)]",
                                "transition-all duration-300",
                                "group"
                            )}
                        >
                            <Play className="w-4 h-4 mr-2 group-hover:scale-110 transition-transform" />
                            Continue Learning
                            <ArrowRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" />
                        </Button>
                    </Link>

                    <Link href="/modules">
                        <Button
                            variant="ghost"
                            size="lg"
                            className={cn(
                                "h-12 rounded-xl",
                                "border border-zinc-700/50",
                                "hover:bg-zinc-800/50 hover:border-zinc-600",
                                "text-zinc-300 hover:text-white",
                                "transition-all duration-200"
                            )}
                        >
                            Browse All Modules
                        </Button>
                    </Link>
                </div>

                {/* Streak Indicator (if applicable) */}
                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3, duration: 0.4 }}
                    className="mt-6 flex items-center gap-2 text-sm"
                >
                    <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-amber-500/10 border border-amber-500/20">
                        <TrendingUp className="w-4 h-4 text-amber-400" />
                        <span className="text-amber-400 font-medium">
                            Keep your learning streak alive!
                        </span>
                    </div>
                </motion.div>
            </div>
        </motion.div>
    )
}

// Helper component to track and save activity (use in module pages)
export function useContinueLearningTracker() {
    const trackActivity = (activity: Omit<LastActivity, "lastAccessedAt">) => {
        saveLastActivity(activity)
    }

    return { trackActivity }
}
