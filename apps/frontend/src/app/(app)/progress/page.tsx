"use client"

/**
 * ============================================================================
 * PROGRESS PAGE — Learning Progress Overview
 * ============================================================================
 *
 * Features:
 * - Overall progress visualization
 * - Track-by-track breakdown
 * - Stats and achievements
 * - Activity heatmap
 *
 * @phase A.3 - App Shell & Routing
 */

import { useState, useEffect } from "react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import { GlassCard } from "@/components/ui/glass-card"
import { ProgressBar } from "@/components/ui/progress-bar"
import { getMockTracks, type TrackSummary } from "@/lib/api/tracks"
import {
    Trophy,
    Target,
    Flame,
    Clock,
    CheckCircle2,
    TrendingUp,
    Calendar,
    BookOpen,
    Zap,
} from "lucide-react"

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_STATS = {
    totalXP: 2450,
    level: 7,
    streak: 14,
    totalHours: 42,
    tasksCompleted: 78,
    modulesCompleted: 6,
    achievementsUnlocked: 12,
}

const MOCK_ACHIEVEMENTS = [
    { id: "1", name: "First Steps", description: "Complete your first task", icon: "🚀", unlocked: true },
    { id: "2", name: "Week Warrior", description: "7-day study streak", icon: "🔥", unlocked: true },
    { id: "3", name: "Linux Basics", description: "Complete Linux fundamentals", icon: "🐧", unlocked: true },
    { id: "4", name: "Docker Pro", description: "Master containerization", icon: "🐳", unlocked: false },
    { id: "5", name: "Month Master", description: "30-day study streak", icon: "👑", unlocked: false },
    { id: "6", name: "K8s Captain", description: "Complete Kubernetes track", icon: "⚙️", unlocked: false },
]

// Generate mock heatmap data for last 12 weeks
const generateHeatmapData = () => {
    const data: { date: string; count: number }[] = []
    const today = new Date()
    for (let i = 83; i >= 0; i--) {
        const date = new Date(today)
        date.setDate(date.getDate() - i)
        // Random activity level, more recent = higher probability
        const probability = Math.max(0.3, 1 - i / 100)
        const count = Math.random() < probability ? Math.floor(Math.random() * 5) : 0
        data.push({
            date: date.toISOString().split("T")[0],
            count,
        })
    }
    return data
}

/* ============================================================================
   STAT CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
}

function StatCard({ icon, label, value, color }: StatCardProps) {
    return (
        <GlassCard variant="default" padding="md" radius="xl">
            <div className="flex items-center gap-3">
                <div
                    className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center",
                        color
                    )}
                >
                    {icon}
                </div>
                <div>
                    <p className="text-sm text-neutral-500 dark:text-neutral-400">{label}</p>
                    <p className="text-xl font-bold text-neutral-900 dark:text-white">{value}</p>
                </div>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   ACTIVITY HEATMAP
   ============================================================================ */

function ActivityHeatmap({ data }: { data: { date: string; count: number }[] }) {
    const getColor = (count: number) => {
        if (count === 0) return "bg-neutral-100 dark:bg-neutral-800"
        if (count === 1) return "bg-primary-200 dark:bg-primary-900/50"
        if (count === 2) return "bg-primary-300 dark:bg-primary-800"
        if (count === 3) return "bg-primary-400 dark:bg-primary-700"
        return "bg-primary-500 dark:bg-primary-600"
    }

    // Group by weeks (7 days each)
    const weeks: { date: string; count: number }[][] = []
    for (let i = 0; i < data.length; i += 7) {
        weeks.push(data.slice(i, i + 7))
    }

    return (
        <GlassCard variant="default" padding="lg" radius="xl">
            <div className="flex items-center gap-2 mb-4">
                <Calendar className="w-5 h-5 text-primary-500" />
                <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                    Activity
                </h3>
            </div>
            <div className="flex gap-1">
                {weeks.map((week, weekIndex) => (
                    <div key={weekIndex} className="flex flex-col gap-1">
                        {week.map((day, dayIndex) => (
                            <div
                                key={dayIndex}
                                className={cn(
                                    "w-3 h-3 rounded-sm",
                                    getColor(day.count)
                                )}
                                title={`${day.date}: ${day.count} activities`}
                            />
                        ))}
                    </div>
                ))}
            </div>
            <div className="flex items-center justify-end gap-2 mt-3 text-xs text-neutral-500">
                <span>Less</span>
                <div className="flex gap-1">
                    {[0, 1, 2, 3, 4].map((level) => (
                        <div
                            key={level}
                            className={cn("w-3 h-3 rounded-sm", getColor(level))}
                        />
                    ))}
                </div>
                <span>More</span>
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   TRACK PROGRESS CARD
   ============================================================================ */

function TrackProgressCard({ track }: { track: TrackSummary }) {
    return (
        <div
            className={cn(
                "flex items-center gap-4 p-4 rounded-xl",
                "bg-white/50 dark:bg-neutral-800/50",
                "border border-neutral-200/50 dark:border-neutral-700/50"
            )}
        >
            {/* Icon */}
            <div
                className="w-12 h-12 rounded-xl flex items-center justify-center shrink-0"
                style={{ backgroundColor: `${track.color}20` }}
            >
                <BookOpen className="w-6 h-6" style={{ color: track.color }} />
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0">
                <h4 className="font-semibold text-neutral-900 dark:text-white mb-1">
                    {track.title}
                </h4>
                <div className="flex items-center gap-3 mb-2">
                    <span className="text-sm text-neutral-500 dark:text-neutral-400">
                        {track.completedModules}/{track.totalModules} modules
                    </span>
                </div>
                <ProgressBar value={track.progress} className="h-2" />
            </div>

            {/* Progress percentage */}
            <div
                className="text-lg font-bold shrink-0"
                style={{ color: track.color }}
            >
                {track.progress}%
            </div>
        </div>
    )
}

/* ============================================================================
   ACHIEVEMENTS SECTION
   ============================================================================ */

function Achievements({ achievements }: { achievements: typeof MOCK_ACHIEVEMENTS }) {
    return (
        <GlassCard variant="default" padding="lg" radius="xl">
            <div className="flex items-center gap-2 mb-4">
                <Trophy className="w-5 h-5 text-warning-500" />
                <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                    Achievements
                </h3>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {achievements.map((achievement) => (
                    <div
                        key={achievement.id}
                        className={cn(
                            "flex flex-col items-center p-3 rounded-xl text-center transition-all",
                            achievement.unlocked
                                ? "bg-warning-50 dark:bg-warning-900/20"
                                : "bg-neutral-100 dark:bg-neutral-800 opacity-50 grayscale"
                        )}
                    >
                        <span className="text-2xl mb-1">{achievement.icon}</span>
                        <span className="text-sm font-medium text-neutral-900 dark:text-white">
                            {achievement.name}
                        </span>
                        <span className="text-xs text-neutral-500 dark:text-neutral-400">
                            {achievement.description}
                        </span>
                    </div>
                ))}
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   PROGRESS PAGE
   ============================================================================ */

export default function ProgressPage() {
    const { user } = useAuth()
    const [tracks, setTracks] = useState<TrackSummary[]>([])
    const [heatmapData, setHeatmapData] = useState<{ date: string; count: number }[]>([])

    useEffect(() => {
        // Load mock data
        setTracks(getMockTracks())
        setHeatmapData(generateHeatmapData())
    }, [])

    const overallProgress = tracks.length > 0
        ? Math.round(tracks.reduce((sum, t) => sum + t.progress, 0) / tracks.length)
        : 0

    return (
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="space-y-8">
                {/* Header */}
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-2xl font-bold text-neutral-900 dark:text-white">
                            Your Progress
                        </h1>
                        <p className="text-neutral-500 dark:text-neutral-400">
                            Track your DevOps learning journey
                        </p>
                    </div>
                    <div
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-xl",
                            "bg-primary-100 dark:bg-primary-900/30"
                        )}
                    >
                        <Zap className="w-5 h-5 text-primary-500" />
                        <span className="font-semibold text-primary-700 dark:text-primary-400">
                            Level {MOCK_STATS.level}
                        </span>
                    </div>
                </div>

                {/* Stats Grid */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <StatCard
                        icon={<Trophy className="w-5 h-5 text-warning-500" />}
                        label="Total XP"
                        value={MOCK_STATS.totalXP.toLocaleString()}
                        color="bg-warning-100 dark:bg-warning-900/30"
                    />
                    <StatCard
                        icon={<Flame className="w-5 h-5 text-orange-500" />}
                        label="Day Streak"
                        value={MOCK_STATS.streak}
                        color="bg-orange-100 dark:bg-orange-900/30"
                    />
                    <StatCard
                        icon={<Clock className="w-5 h-5 text-blue-500" />}
                        label="Hours Learned"
                        value={MOCK_STATS.totalHours}
                        color="bg-blue-100 dark:bg-blue-900/30"
                    />
                    <StatCard
                        icon={<CheckCircle2 className="w-5 h-5 text-success-500" />}
                        label="Tasks Done"
                        value={MOCK_STATS.tasksCompleted}
                        color="bg-success-100 dark:bg-success-900/30"
                    />
                </div>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Left Column - Tracks & Activity */}
                    <div className="lg:col-span-2 space-y-6">
                        {/* Overall Progress */}
                        <GlassCard variant="default" padding="lg" radius="xl">
                            <div className="flex items-center justify-between mb-4">
                                <div className="flex items-center gap-2">
                                    <Target className="w-5 h-5 text-primary-500" />
                                    <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                                        Overall Progress
                                    </h3>
                                </div>
                                <span className="text-2xl font-bold text-primary-500">
                                    {overallProgress}%
                                </span>
                            </div>
                            <ProgressBar value={overallProgress} className="h-3 mb-4" />
                            <div className="flex items-center gap-2 text-sm text-neutral-500">
                                <TrendingUp className="w-4 h-4 text-success-500" />
                                <span>
                                    You&apos;re making great progress! Keep it up, {user?.full_name?.split(" ")[0] || "learner"}!
                                </span>
                            </div>
                        </GlassCard>

                        {/* Tracks Progress */}
                        <GlassCard variant="default" padding="lg" radius="xl">
                            <div className="flex items-center gap-2 mb-4">
                                <BookOpen className="w-5 h-5 text-primary-500" />
                                <h3 className="text-lg font-semibold text-neutral-900 dark:text-white">
                                    Track Progress
                                </h3>
                            </div>
                            <div className="space-y-3">
                                {tracks.map((track) => (
                                    <TrackProgressCard key={track.id} track={track} />
                                ))}
                            </div>
                        </GlassCard>

                        {/* Activity Heatmap */}
                        <ActivityHeatmap data={heatmapData} />
                    </div>

                    {/* Right Column - Achievements */}
                    <div>
                        <Achievements achievements={MOCK_ACHIEVEMENTS} />
                    </div>
                </div>
            </div>
        </div>
    )
}
