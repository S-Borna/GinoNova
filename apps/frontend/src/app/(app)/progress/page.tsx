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
 * @design PHASE 2 — Design System Application Layer
 */

import { useState, useEffect } from "react"
import { PageLayout, Section, Block, Headline, Subtext, InfoBanner, SuccessBanner, cn } from "@saas/ui"
import { useAuth } from "@/components/auth"
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
   DEFAULT DATA - Shows real values (0 for new users)
   ============================================================================ */

const DEFAULT_STATS = {
    totalXP: 0,
    level: 1,
    streak: 0,
    totalHours: 0,
    tasksCompleted: 0,
    modulesCompleted: 0,
    achievementsUnlocked: 0,
}

const ACHIEVEMENTS = [
    { id: "1", name: "First Steps", description: "Complete your first task", icon: "🚀", unlocked: false },
    { id: "2", name: "Week Warrior", description: "7-day study streak", icon: "🔥", unlocked: false },
    { id: "3", name: "Linux Basics", description: "Complete Linux fundamentals", icon: "🐧", unlocked: false },
    { id: "4", name: "Docker Pro", description: "Master containerization", icon: "🐳", unlocked: false },
    { id: "5", name: "Month Master", description: "30-day study streak", icon: "👑", unlocked: false },
    { id: "6", name: "K8s Captain", description: "Complete Kubernetes track", icon: "⚙️", unlocked: false },
]

// Generate empty heatmap for new users
const generateHeatmapData = () => {
    const data: { date: string; count: number }[] = []
    const today = new Date()
    for (let i = 83; i >= 0; i--) {
        const date = new Date(today)
        date.setDate(date.getDate() - i)
        // Start with empty heatmap for new users
        data.push({
            date: date.toISOString().split("T")[0],
            count: 0,
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
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
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
                    <p className="text-sm text-gray-500 dark:text-gray-400">{label}</p>
                    <p className="text-xl font-bold text-gray-900 dark:text-white">{value}</p>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   ACTIVITY HEATMAP
   ============================================================================ */

function ActivityHeatmap({ data }: { data: { date: string; count: number }[] }) {
    const getColor = (count: number) => {
        if (count === 0) return "bg-gray-100 dark:bg-gray-800"
        if (count === 1) return "bg-indigo-200 dark:bg-indigo-900/50"
        if (count === 2) return "bg-indigo-300 dark:bg-indigo-800"
        if (count === 3) return "bg-indigo-400 dark:bg-indigo-700"
        return "bg-indigo-500 dark:bg-indigo-600"
    }

    // Group by weeks (7 days each)
    const weeks: { date: string; count: number }[][] = []
    for (let i = 0; i < data.length; i += 7) {
        weeks.push(data.slice(i, i + 7))
    }

    return (
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
            <div className="flex items-center gap-2 mb-4">
                <Calendar className="w-5 h-5 text-indigo-500" />
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
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
            <div className="flex items-center justify-end gap-2 mt-3 text-xs text-gray-500">
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
        </div>
    )
}

/* ============================================================================
   TRACK PROGRESS CARD
   ============================================================================ */

function TrackProgressCard({ track }: { track: TrackSummary }) {
    return (
        <div className="flex items-center gap-4 p-4 rounded-xl bg-gray-50 dark:bg-gray-700/50 border border-gray-100 dark:border-gray-600">
            {/* Icon */}
            <div
                className="w-12 h-12 rounded-xl flex items-center justify-center shrink-0"
                style={{ backgroundColor: `${track.color}20` }}
            >
                <BookOpen className="w-6 h-6" style={{ color: track.color }} />
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0">
                <h4 className="font-semibold text-gray-900 dark:text-white mb-1">
                    {track.title}
                </h4>
                <div className="flex items-center gap-3 mb-2">
                    <span className="text-sm text-gray-500 dark:text-gray-400">
                        {track.completedModules}/{track.totalModules} modules
                    </span>
                </div>
                {/* Progress Bar */}
                <div className="h-2 bg-gray-200 dark:bg-gray-600 rounded-full overflow-hidden">
                    <div
                        className="h-full rounded-full transition-all duration-500"
                        style={{
                            width: `${track.progress}%`,
                            backgroundColor: track.color
                        }}
                    />
                </div>
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

function Achievements({ achievements }: { achievements: typeof ACHIEVEMENTS }) {
    return (
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
            <div className="flex items-center gap-2 mb-4">
                <Trophy className="w-5 h-5 text-amber-500" />
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
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
                                ? "bg-amber-50 dark:bg-amber-900/20"
                                : "bg-gray-100 dark:bg-gray-700 opacity-50 grayscale"
                        )}
                    >
                        <span className="text-2xl mb-1">{achievement.icon}</span>
                        <span className="text-sm font-medium text-gray-900 dark:text-white">
                            {achievement.name}
                        </span>
                        <span className="text-xs text-gray-500 dark:text-gray-400">
                            {achievement.description}
                        </span>
                    </div>
                ))}
            </div>
        </div>
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
        <PageLayout maxWidth="wide" background="subtle">
            <div className="space-y-8">
                {/* Header */}
                <Section>
                    <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6 md:p-8">
                        <div className="flex items-center justify-between">
                            <div>
                                <Headline level={1}>
                                    Your Progress
                                </Headline>
                                <Subtext>
                                    Track your DevOps learning journey
                                </Subtext>
                            </div>
                            <div className="flex items-center gap-2 px-4 py-2 rounded-xl bg-indigo-100 dark:bg-indigo-900/30">
                                <Zap className="w-5 h-5 text-indigo-500" />
                                <span className="font-semibold text-indigo-700 dark:text-indigo-400">
                                    Level {DEFAULT_STATS.level}
                                </span>
                            </div>
                        </div>
                    </Block>
                </Section>

                {/* Stats Grid */}
                <Section>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <StatCard
                            icon={<Trophy className="w-5 h-5 text-amber-500" />}
                            label="Total XP"
                            value={DEFAULT_STATS.totalXP.toLocaleString()}
                            color="bg-amber-100 dark:bg-amber-900/30"
                        />
                        <StatCard
                            icon={<Flame className="w-5 h-5 text-orange-500" />}
                            label="Day Streak"
                            value={DEFAULT_STATS.streak}
                            color="bg-orange-100 dark:bg-orange-900/30"
                        />
                        <StatCard
                            icon={<Clock className="w-5 h-5 text-blue-500" />}
                            label="Hours Learned"
                            value={DEFAULT_STATS.totalHours}
                            color="bg-blue-100 dark:bg-blue-900/30"
                        />
                        <StatCard
                            icon={<CheckCircle2 className="w-5 h-5 text-emerald-500" />}
                            label="Tasks Done"
                            value={DEFAULT_STATS.tasksCompleted}
                            color="bg-emerald-100 dark:bg-emerald-900/30"
                        />
                    </div>
                </Section>

                {/* Main Grid */}
                <Section>
                    <div className="grid lg:grid-cols-3 gap-6">
                        {/* Left Column - Tracks & Activity */}
                        <div className="lg:col-span-2 space-y-6">
                            {/* Overall Progress */}
                            <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6">
                                <div className="flex items-center justify-between mb-4">
                                    <div className="flex items-center gap-2">
                                        <Target className="w-5 h-5 text-indigo-500" />
                                        <Headline level={3}>
                                            Overall Progress
                                        </Headline>
                                    </div>
                                    <span className="text-2xl font-bold text-indigo-500">
                                        {overallProgress}%
                                    </span>
                                </div>
                                {/* Progress Bar */}
                                <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden mb-4">
                                    <div
                                        className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full transition-all duration-500"
                                        style={{ width: `${overallProgress}%` }}
                                    />
                                </div>
                                <div className="flex items-center gap-2 text-sm text-gray-500">
                                    <TrendingUp className="w-4 h-4 text-emerald-500" />
                                    <span>
                                        You&apos;re making great progress! Keep it up, {user?.full_name?.split(" ")[0] || "learner"}!
                                    </span>
                                </div>
                            </Block>

                            {/* Tracks Progress */}
                            <Block className="bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl rounded-2xl border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg p-6">
                                <div className="flex items-center gap-2 mb-4">
                                    <BookOpen className="w-5 h-5 text-indigo-500" />
                                    <Headline level={3}>
                                        Track Progress
                                    </Headline>
                                </div>
                                <div className="space-y-3">
                                    {tracks.map((track) => (
                                        <TrackProgressCard key={track.id} track={track} />
                                    ))}
                                </div>
                            </Block>

                            {/* Activity Heatmap */}
                            <ActivityHeatmap data={heatmapData} />
                        </div>

                        {/* Right Column - Achievements */}
                        <div>
                            <Achievements achievements={ACHIEVEMENTS} />
                        </div>
                    </div>
                </Section>
            </div>
        </PageLayout>
    )
}
