"use client"

/**
 * DashboardHeader Component
 * Phase 6.2: User info header with level badge and XP progress
 */

import { Badge } from "@/components/ui/badge"
import { ProgressBar } from "@/components/ui/progress-bar"
import type { DashboardUser } from "@/lib/dashboard"

// ============================================================================
// TYPES
// ============================================================================

interface DashboardHeaderProps {
    user: DashboardUser | null
    level?: number
    currentXP?: number
    xpToNextLevel?: number
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function calculateLevel(xp: number): number {
    // Simple level calculation: every 1000 XP = 1 level
    return Math.floor(xp / 1000) + 1
}

function getXPProgress(xp: number): { current: number; toNext: number; percentage: number } {
    const xpPerLevel = 1000
    const current = xp % xpPerLevel
    const toNext = xpPerLevel
    const percentage = (current / toNext) * 100
    return { current, toNext, percentage }
}

function getLevelBadgeColor(level: number): string {
    if (level >= 10) return "bg-gradient-to-r from-purple-500 to-pink-500 text-white"
    if (level >= 5) return "bg-gradient-to-r from-blue-500 to-cyan-500 text-white"
    if (level >= 3) return "bg-gradient-to-r from-emerald-500 to-teal-500 text-white"
    return "bg-gradient-to-r from-gray-400 to-gray-500 text-white"
}

// ============================================================================
// COMPONENT
// ============================================================================

export function DashboardHeader({
    user,
    level: propLevel,
    currentXP = 0,
    xpToNextLevel,
}: DashboardHeaderProps) {
    const level = propLevel ?? calculateLevel(currentXP)
    const xpProgress = getXPProgress(currentXP)
    const toNext = xpToNextLevel ?? xpProgress.toNext

    const displayName = user?.full_name || user?.email?.split("@")[0] || "Learner"
    const levelBadgeColor = getLevelBadgeColor(level)

    return (
        <div className="rounded-2xl bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-6 text-white shadow-lg">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                {/* User Info */}
                <div className="flex items-center gap-4">
                    {/* Avatar */}
                    <div className="w-14 h-14 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center text-2xl font-bold shadow-inner">
                        {displayName.charAt(0).toUpperCase()}
                    </div>

                    {/* Name & Email */}
                    <div>
                        <h2 className="text-xl font-bold tracking-tight">
                            Welcome back, {displayName}!
                        </h2>
                        {user?.email && (
                            <p className="text-sm text-white/70">{user.email}</p>
                        )}
                    </div>
                </div>

                {/* Level & XP */}
                <div className="flex items-center gap-4">
                    {/* Level Badge */}
                    <Badge className={`${levelBadgeColor} px-4 py-1.5 text-sm font-bold shadow-md`}>
                        Level {level}
                    </Badge>

                    {/* XP Progress */}
                    <div className="min-w-[160px]">
                        <div className="flex items-center justify-between text-xs text-white/80 mb-1">
                            <span>XP Progress</span>
                            <span className="font-medium">
                                {xpProgress.current} / {toNext}
                            </span>
                        </div>
                        <div className="h-2 bg-white/20 rounded-full overflow-hidden">
                            <div
                                className="h-full bg-white rounded-full transition-all duration-500 ease-out"
                                style={{ width: `${xpProgress.percentage}%` }}
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Quick Stats Row */}
            <div className="mt-6 pt-4 border-t border-white/20 grid grid-cols-3 gap-4 text-center">
                <div>
                    <p className="text-2xl font-bold">{currentXP}</p>
                    <p className="text-xs text-white/70">Total XP</p>
                </div>
                <div>
                    <p className="text-2xl font-bold">{level}</p>
                    <p className="text-xs text-white/70">Current Level</p>
                </div>
                <div>
                    <p className="text-2xl font-bold">{toNext - xpProgress.current}</p>
                    <p className="text-xs text-white/70">XP to Next</p>
                </div>
            </div>
        </div>
    )
}
