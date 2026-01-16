"use client"

/**
 * DailyActivity Component
 * Phase 6.2: Today's study activity and streaks
 */

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { DashboardStudyflow } from "@/lib/dashboard"

// ============================================================================
// TYPES
// ============================================================================

interface DailyActivityProps {
    studyflows: DashboardStudyflow[]
    studyMinutesToday?: number
    tasksCompletedToday?: number
    currentStreak?: number
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getStreakEmoji(streak: number): string {
    if (streak >= 30) return "🔥"
    if (streak >= 14) return "⚡"
    if (streak >= 7) return "✨"
    if (streak >= 3) return "🌟"
    return "💫"
}

function getStreakMessage(streak: number): string {
    if (streak >= 30) return "Legendary streak!"
    if (streak >= 14) return "On fire!"
    if (streak >= 7) return "Great momentum!"
    if (streak >= 3) return "Building habit!"
    if (streak >= 1) return "Keep it up!"
    return "Start your streak!"
}

function formatMinutes(minutes: number): string {
    if (minutes >= 60) {
        const hours = Math.floor(minutes / 60)
        const mins = minutes % 60
        return mins > 0 ? `${hours}h ${mins}m` : `${hours}h`
    }
    return `${minutes}m`
}

// ============================================================================
// COMPONENT
// ============================================================================

export function DailyActivity({
    studyflows,
    studyMinutesToday = 0,
    tasksCompletedToday = 0,
    currentStreak = 0,
}: DailyActivityProps) {
    const streakEmoji = getStreakEmoji(currentStreak)
    const streakMessage = getStreakMessage(currentStreak)
    const activeStudyflows = studyflows.filter(sf => sf.is_active).length

    return (
        <Card className="rounded-xl border-0 shadow-md bg-white dark:bg-neutral-900/80">
            <CardHeader className="pb-2">
                <CardTitle className="text-base font-semibold text-gray-900 dark:text-white flex items-center gap-2">
                    <span className="text-lg">⚡</span>
                    Today&apos;s Activity
                </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
                {/* Streak Banner */}
                <div className="relative overflow-hidden rounded-xl bg-gradient-to-br from-orange-400 to-pink-500 p-4 text-white">
                    <div className="relative z-10 flex items-center justify-between">
                        <div>
                            <p className="text-3xl font-bold">{currentStreak}</p>
                            <p className="text-sm text-white/80">Day Streak {streakEmoji}</p>
                        </div>
                        <div className="text-right">
                            <p className="text-sm font-medium">{streakMessage}</p>
                            <p className="text-xs text-white/70">Don&apos;t break the chain!</p>
                        </div>
                    </div>
                    {/* Decorative circles */}
                    <div className="absolute -right-4 -top-4 w-20 h-20 rounded-full bg-white/10" />
                    <div className="absolute -right-2 -bottom-6 w-16 h-16 rounded-full bg-white/10" />
                </div>

                {/* Activity Stats Grid */}
                <div className="grid grid-cols-2 gap-3">
                    {/* Study Time */}
                    <div className="p-4 rounded-xl bg-blue-50 dark:bg-blue-500/10 border border-blue-100 dark:border-blue-500/20">
                        <div className="flex items-center gap-2 mb-2">
                            <div className="w-8 h-8 rounded-lg bg-blue-500 flex items-center justify-center">
                                <span className="text-white text-sm">⏱️</span>
                            </div>
                            <span className="text-xs font-medium text-blue-600 dark:text-blue-400 uppercase tracking-wider">Study Time</span>
                        </div>
                        <p className="text-2xl font-bold text-gray-900 dark:text-white">
                            {formatMinutes(studyMinutesToday)}
                        </p>
                        <p className="text-xs text-gray-500 dark:text-zinc-400">Today</p>
                    </div>

                    {/* Tasks Completed */}
                    <div className="p-4 rounded-xl bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-100 dark:border-emerald-500/20">
                        <div className="flex items-center gap-2 mb-2">
                            <div className="w-8 h-8 rounded-lg bg-emerald-500 flex items-center justify-center">
                                <span className="text-white text-sm">✅</span>
                            </div>
                            <span className="text-xs font-medium text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Tasks</span>
                        </div>
                        <p className="text-2xl font-bold text-gray-900 dark:text-white">{tasksCompletedToday}</p>
                        <p className="text-xs text-gray-500 dark:text-zinc-400">Completed</p>
                    </div>
                </div>

                {/* Active Studyflows */}
                <div className="p-4 rounded-xl bg-purple-50 dark:bg-purple-500/10 border border-purple-100 dark:border-purple-500/20">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <div className="w-8 h-8 rounded-lg bg-purple-500 flex items-center justify-center">
                                <span className="text-white text-sm">🎯</span>
                            </div>
                            <div>
                                <p className="text-sm font-medium text-gray-900 dark:text-white">Active Studyflows</p>
                                <p className="text-xs text-gray-500 dark:text-zinc-400">{studyflows.length} total</p>
                            </div>
                        </div>
                        <div className="text-right">
                            <p className="text-2xl font-bold text-purple-600 dark:text-purple-400">{activeStudyflows}</p>
                            <p className="text-xs text-gray-500 dark:text-zinc-400">in progress</p>
                        </div>
                    </div>
                </div>

                {/* Motivation Message */}
                {studyMinutesToday === 0 && tasksCompletedToday === 0 && (
                    <div className="text-center py-3 px-4 rounded-lg bg-gray-50 dark:bg-white/5 border border-dashed border-gray-200 dark:border-white/10">
                        <p className="text-sm text-gray-600 dark:text-zinc-400">
                            🌅 Start your day strong! Complete a task to keep your streak alive.
                        </p>
                    </div>
                )}
            </CardContent>
        </Card>
    )
}
