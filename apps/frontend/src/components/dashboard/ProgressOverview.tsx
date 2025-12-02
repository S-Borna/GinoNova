"use client"

/**
 * ============================================================================
 * PROGRESS OVERVIEW - Premium Polish Edition ✨
 * ============================================================================
 *
 * Bootcamp progress visualization with:
 * - Animated progress ring with Chill Mint glow
 * - Satisfying milestone celebrations
 * - Premium dark card styling
 *
 * @phase 6.2: Bootcamp progress visualization
 * @polish Premium Polish v1.0
 */

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { cn } from "@/lib/utils"
import type { DashboardStats } from "@/lib/dashboard"

// ============================================================================
// TYPES
// ============================================================================

interface ProgressOverviewProps {
    stats: DashboardStats
    completedModules?: number
    completedTasks?: number
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getProgressColor(percentage: number): { bg: string; glow: string } {
    if (percentage >= 80) return {
        bg: "bg-gradient-to-r from-emerald-500 to-emerald-400",
        glow: "shadow-[0_0_12px_rgba(34,211,172,0.5)]"
    }
    if (percentage >= 50) return {
        bg: "bg-gradient-to-r from-purple-500 to-purple-400",
        glow: "shadow-[0_0_12px_rgba(139,92,246,0.4)]"
    }
    if (percentage >= 25) return {
        bg: "bg-gradient-to-r from-amber-500 to-amber-400",
        glow: "shadow-[0_0_12px_rgba(245,158,11,0.4)]"
    }
    return {
        bg: "bg-zinc-600",
        glow: ""
    }
}

function getProgressLabel(percentage: number): { text: string; emoji: string; color: string } {
    if (percentage >= 100) return { text: "Complete!", emoji: "🎉", color: "text-emerald-400 bg-emerald-500/10 border-emerald-500/20" }
    if (percentage >= 80) return { text: "Almost there!", emoji: "🔥", color: "text-emerald-400 bg-emerald-500/10 border-emerald-500/20" }
    if (percentage >= 50) return { text: "Great progress!", emoji: "⚡", color: "text-purple-400 bg-purple-500/10 border-purple-500/20" }
    if (percentage >= 25) return { text: "Keep going!", emoji: "💪", color: "text-amber-400 bg-amber-500/10 border-amber-500/20" }
    return { text: "Just started", emoji: "🚀", color: "text-zinc-400 bg-zinc-500/10 border-zinc-500/20" }
}

// ============================================================================
// COMPONENT
// ============================================================================

export function ProgressOverview({
    stats,
    completedModules = 0,
    completedTasks = 0,
}: ProgressOverviewProps) {
    const moduleProgress = stats.total_modules > 0
        ? Math.round((completedModules / stats.total_modules) * 100)
        : 0

    const taskProgress = stats.total_tasks > 0
        ? Math.round((completedTasks / stats.total_tasks) * 100)
        : 0

    const overallProgress = Math.round((moduleProgress + taskProgress) / 2)
    const statusLabel = getProgressLabel(overallProgress)

    return (
        <Card className={cn(
            "rounded-2xl border border-zinc-800/60",
            "bg-gradient-to-br from-zinc-900 to-zinc-950",
            "shadow-xl shadow-black/20"
        )}>
            <CardHeader className="pb-2">
                <CardTitle className="text-base font-semibold text-zinc-100 flex items-center gap-2">
                    <span className="text-lg">📊</span>
                    Bootcamp Progress
                </CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
                {/* Overall Progress Circle - Premium Edition */}
                <div className="flex items-center justify-center py-4">
                    <div className="relative w-32 h-32">
                        {/* Glow effect */}
                        <div className={cn(
                            "absolute inset-0 rounded-full blur-xl opacity-30",
                            overallProgress >= 50 ? "bg-emerald-500" : "bg-purple-500"
                        )} />

                        {/* Background circle */}
                        <svg className="w-full h-full -rotate-90 relative" viewBox="0 0 36 36">
                            {/* Track */}
                            <path
                                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                fill="none"
                                stroke="rgba(63, 63, 70, 0.5)"
                                strokeWidth="2.5"
                            />
                            {/* Progress with gradient */}
                            <path
                                d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                fill="none"
                                stroke="url(#premiumProgressGradient)"
                                strokeWidth="2.5"
                                strokeDasharray={`${overallProgress}, 100`}
                                strokeLinecap="round"
                                className="transition-all duration-700 ease-out"
                                style={{
                                    filter: "drop-shadow(0 0 6px rgba(34, 211, 172, 0.5))"
                                }}
                            />
                            <defs>
                                <linearGradient id="premiumProgressGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" stopColor="#22D3AC" />
                                    <stop offset="50%" stopColor="#8B5CF6" />
                                    <stop offset="100%" stopColor="#22D3AC" />
                                </linearGradient>
                            </defs>
                        </svg>

                        {/* Center text */}
                        <div className="absolute inset-0 flex flex-col items-center justify-center">
                            <span className={cn(
                                "text-3xl font-bold",
                                "bg-gradient-to-r from-zinc-100 to-zinc-300 bg-clip-text text-transparent"
                            )}>
                                {overallProgress}%
                            </span>
                            <span className="text-[10px] text-zinc-500 font-medium uppercase tracking-wider">
                                Overall
                            </span>
                        </div>
                    </div>
                </div>

                {/* Status Label - Premium Badge */}
                <div className="text-center">
                    <span className={cn(
                        "inline-flex items-center gap-1.5 px-4 py-1.5",
                        "rounded-full text-xs font-semibold",
                        "border transition-all duration-300",
                        statusLabel.color
                    )}>
                        <span>{statusLabel.emoji}</span>
                        {statusLabel.text}
                    </span>
                </div>

                {/* Detailed Progress Bars - Premium Style */}
                <div className="space-y-4 pt-2">
                    {/* Modules Progress */}
                    <div>
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-400 font-medium">Modules</span>
                            <span className="text-zinc-200 font-semibold">
                                {completedModules} / {stats.total_modules}
                            </span>
                        </div>
                        <div className="h-2.5 bg-zinc-800 rounded-full overflow-hidden">
                            <div
                                className={cn(
                                    "h-full rounded-full transition-all duration-700 ease-out",
                                    getProgressColor(moduleProgress).bg,
                                    getProgressColor(moduleProgress).glow
                                )}
                                style={{ width: `${moduleProgress}%` }}
                            />
                        </div>
                    </div>

                    {/* Tasks Progress */}
                    <div>
                        <div className="flex items-center justify-between text-sm mb-2">
                            <span className="text-zinc-400 font-medium">Tasks</span>
                            <span className="text-zinc-200 font-semibold">
                                {completedTasks} / {stats.total_tasks}
                            </span>
                        </div>
                        <div className="h-2.5 bg-zinc-800 rounded-full overflow-hidden">
                            <div
                                className={cn(
                                    "h-full rounded-full transition-all duration-700 ease-out",
                                    getProgressColor(taskProgress).bg,
                                    getProgressColor(taskProgress).glow
                                )}
                                style={{ width: `${taskProgress}%` }}
                            />
                        </div>
                    </div>
                </div>

                {/* Stats Summary - Premium Cards */}
                <div className="grid grid-cols-2 gap-3 pt-3 border-t border-zinc-800/60">
                    <div className={cn(
                        "text-center p-3 rounded-xl",
                        "bg-zinc-800/40 border border-zinc-700/30",
                        "hover:bg-zinc-800/60 transition-colors duration-200"
                    )}>
                        <p className="text-xl font-bold text-emerald-400">{stats.active_modules}</p>
                        <p className="text-[10px] text-zinc-500 uppercase tracking-wider font-medium">
                            Active Modules
                        </p>
                    </div>
                    <div className={cn(
                        "text-center p-3 rounded-xl",
                        "bg-zinc-800/40 border border-zinc-700/30",
                        "hover:bg-zinc-800/60 transition-colors duration-200"
                    )}>
                        <p className="text-xl font-bold text-purple-400">{stats.active_tasks}</p>
                        <p className="text-[10px] text-zinc-500 uppercase tracking-wider font-medium">
                            Active Tasks
                        </p>
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}
