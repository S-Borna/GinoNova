"use client"

/**
 * ============================================================================
 * PROGRESS PAGE — Premium Polish Edition ✨
 * ============================================================================
 *
 * Design Philosophy:
 * - GLOW and ENERGY - "LET'S GO" feeling
 * - Chill Mint (#22D3AC) for success/progress
 * - Focus Purple (#8B5CF6) for primary accent
 * - XP Gold (#F59E0B) for achievements
 * - Fire Orange (#F97316) for streaks
 * - Celebration animations and micro-interactions
 *
 * @phase A.3 - App Shell & Routing
 * @design Premium Polish Phase 2
 */

import { useState, useEffect } from "react"
import { cn } from "@/lib/utils"
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
    Sparkles,
    Star,
    Rocket,
} from "lucide-react"

/* ============================================================================
   DEFAULT DATA
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

const generateHeatmapData = () => {
    const data: { date: string; count: number }[] = []
    const today = new Date()
    for (let i = 83; i >= 0; i--) {
        const date = new Date(today)
        date.setDate(date.getDate() - i)
        data.push({
            date: date.toISOString().split("T")[0],
            count: 0,
        })
    }
    return data
}

/* ============================================================================
   HERO HEADER - Premium with Glow
   ============================================================================ */

function ProgressHero({ level, userName }: { level: number; userName: string }) {
    return (
        <div className={cn(
            "relative overflow-hidden rounded-2xl",
            "bg-gradient-to-br from-zinc-900 via-purple-950/30 to-zinc-900",
            "border border-purple-500/20",
            "p-8 md:p-10"
        )}>
            {/* Background glow effects */}
            <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />
            <div className="absolute bottom-0 left-1/4 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl translate-y-1/2" />

            {/* Animated sparkles */}
            <div className="absolute top-8 right-16 text-purple-400/50 animate-pulse">
                <Sparkles className="w-6 h-6" />
            </div>
            <div className="absolute bottom-8 right-32 text-emerald-400/40 animate-pulse" style={{ animationDelay: "500ms" }}>
                <Star className="w-4 h-4" />
            </div>

            <div className="relative flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                <div>
                    <div className="flex items-center gap-3 mb-2">
                        <Rocket className="w-6 h-6 text-purple-400" />
                        <span className="text-purple-400 font-medium text-sm uppercase tracking-wider">
                            Your Journey
                        </span>
                    </div>
                    <h1 className={cn(
                        "text-3xl md:text-4xl font-bold mb-3",
                        "bg-gradient-to-r from-zinc-100 via-purple-200 to-zinc-100 bg-clip-text text-transparent"
                    )}>
                        Keep Going, {userName}! 🔥
                    </h1>
                    <p className="text-zinc-400 text-lg">
                        Track your DevOps learning journey and celebrate every win
                    </p>
                </div>

                {/* Level Badge with Glow */}
                <div className={cn(
                    "flex items-center gap-4 px-6 py-4 rounded-2xl",
                    "bg-gradient-to-r from-purple-600/20 to-purple-500/10",
                    "border border-purple-500/30",
                    "shadow-[0_0_30px_rgba(139,92,246,0.2)]"
                )}>
                    <div className={cn(
                        "w-14 h-14 rounded-xl",
                        "bg-gradient-to-br from-purple-500 to-purple-700",
                        "flex items-center justify-center",
                        "shadow-[0_0_25px_rgba(139,92,246,0.5)]",
                        "animate-pulse"
                    )}>
                        <Zap className="w-7 h-7 text-white" />
                    </div>
                    <div>
                        <p className="text-zinc-400 text-sm">Current Level</p>
                        <p className="text-2xl font-bold text-purple-400">Level {level}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   STAT CARD - Premium with Glow
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    color: "gold" | "fire" | "blue" | "mint"
    glow?: boolean
}

const colorStyles = {
    gold: {
        border: "border-amber-500/30",
        text: "text-amber-400",
        glow: "shadow-[0_0_20px_rgba(245,158,11,0.3)]",
        iconBg: "bg-amber-500/20",
    },
    fire: {
        border: "border-orange-500/30",
        text: "text-orange-400",
        glow: "shadow-[0_0_20px_rgba(249,115,22,0.3)]",
        iconBg: "bg-orange-500/20",
    },
    blue: {
        border: "border-blue-500/30",
        text: "text-blue-400",
        glow: "shadow-[0_0_20px_rgba(59,130,246,0.3)]",
        iconBg: "bg-blue-500/20",
    },
    mint: {
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        glow: "shadow-[0_0_20px_rgba(34,211,172,0.3)]",
        iconBg: "bg-emerald-500/20",
    },
}

function StatCard({ icon, label, value, color, glow = false }: StatCardProps) {
    const styles = colorStyles[color]

    return (
        <div className={cn(
            "relative rounded-2xl p-5",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border", styles.border,
            "transition-all duration-300",
            "hover:scale-[1.02]",
            glow && styles.glow,
            "group"
        )}>
            {/* Hover glow effect */}
            <div className={cn(
                "absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300",
                styles.glow
            )} />

            <div className="relative flex items-center gap-4">
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center",
                    styles.iconBg
                )}>
                    {icon}
                </div>
                <div>
                    <p className="text-zinc-500 text-sm font-medium">{label}</p>
                    <p className={cn("text-2xl font-bold", styles.text)}>{value}</p>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   OVERALL PROGRESS - Premium Ring
   ============================================================================ */

function OverallProgressRing({ progress, userName }: { progress: number; userName: string }) {
    const circumference = 2 * Math.PI * 60
    const offset = circumference - (progress / 100) * circumference

    return (
        <div className={cn(
            "rounded-2xl p-6",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            <div className="flex items-center gap-2 mb-6">
                <Target className="w-5 h-5 text-purple-400" />
                <h3 className="text-lg font-semibold text-zinc-100">Overall Progress</h3>
            </div>

            <div className="flex flex-col items-center">
                {/* Animated Ring */}
                <div className="relative w-40 h-40 mb-6">
                    {/* Glow effect */}
                    <div className={cn(
                        "absolute inset-4 rounded-full blur-xl",
                        progress > 50 ? "bg-emerald-500/30" : "bg-purple-500/30"
                    )} />

                    <svg className="w-full h-full -rotate-90 relative" viewBox="0 0 128 128">
                        {/* Background track */}
                        <circle
                            cx="64"
                            cy="64"
                            r="60"
                            fill="none"
                            stroke="rgba(63, 63, 70, 0.5)"
                            strokeWidth="8"
                        />
                        {/* Progress arc */}
                        <circle
                            cx="64"
                            cy="64"
                            r="60"
                            fill="none"
                            stroke="url(#progressGradientPremium)"
                            strokeWidth="8"
                            strokeLinecap="round"
                            strokeDasharray={circumference}
                            strokeDashoffset={offset}
                            className="transition-all duration-1000 ease-out"
                            style={{
                                filter: "drop-shadow(0 0 8px rgba(34, 211, 172, 0.5))"
                            }}
                        />
                        <defs>
                            <linearGradient id="progressGradientPremium" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stopColor="#8B5CF6" />
                                <stop offset="50%" stopColor="#22D3AC" />
                                <stop offset="100%" stopColor="#8B5CF6" />
                            </linearGradient>
                        </defs>
                    </svg>

                    {/* Center content */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center">
                        <span className={cn(
                            "text-4xl font-bold",
                            "bg-gradient-to-r from-purple-400 to-emerald-400 bg-clip-text text-transparent"
                        )}>
                            {progress}%
                        </span>
                        <span className="text-zinc-500 text-sm font-medium">Complete</span>
                    </div>
                </div>

                {/* Motivation message */}
                <div className={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-xl",
                    "bg-emerald-500/10 border border-emerald-500/20"
                )}>
                    <TrendingUp className="w-4 h-4 text-emerald-400" />
                    <span className="text-emerald-400 text-sm font-medium">
                        {progress === 0
                            ? `Start your journey, ${userName}!`
                            : progress < 25
                                ? "Great start! Keep going! 🚀"
                                : progress < 50
                                    ? "You're doing amazing! 💪"
                                    : progress < 75
                                        ? "Over halfway there! 🔥"
                                        : "Almost there! Finish strong! 🏆"
                        }
                    </span>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   TRACK PROGRESS CARD - Premium
   ============================================================================ */

function TrackProgressCard({ track }: { track: TrackSummary }) {
    return (
        <div className={cn(
            "flex items-center gap-4 p-4 rounded-xl",
            "bg-zinc-800/40 border border-zinc-700/30",
            "hover:border-purple-500/30 hover:bg-zinc-800/60",
            "transition-all duration-300",
            "group"
        )}>
            {/* Icon with glow */}
            <div
                className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center shrink-0",
                    "transition-all duration-300",
                    "group-hover:shadow-[0_0_15px_rgba(139,92,246,0.3)]"
                )}
                style={{ backgroundColor: `${track.color}20` }}
            >
                <BookOpen className="w-6 h-6" style={{ color: track.color }} />
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0">
                <h4 className="font-semibold text-zinc-100 mb-1 group-hover:text-purple-300 transition-colors">
                    {track.title}
                </h4>
                <div className="flex items-center gap-3 mb-2">
                    <span className="text-sm text-zinc-500">
                        {track.completedModules}/{track.totalModules} modules
                    </span>
                </div>
                {/* Progress Bar with glow */}
                <div className="h-2 bg-zinc-700/50 rounded-full overflow-hidden">
                    <div
                        className={cn(
                            "h-full rounded-full transition-all duration-700 ease-out",
                            track.progress > 0 && "shadow-[0_0_10px_rgba(34,211,172,0.4)]"
                        )}
                        style={{
                            width: `${track.progress}%`,
                            background: `linear-gradient(90deg, ${track.color}, ${track.color}cc)`
                        }}
                    />
                </div>
            </div>

            {/* Progress percentage */}
            <div
                className="text-lg font-bold shrink-0 transition-all duration-300"
                style={{ color: track.color }}
            >
                {track.progress}%
            </div>
        </div>
    )
}

/* ============================================================================
   ACTIVITY HEATMAP - Premium
   ============================================================================ */

function ActivityHeatmap({ data }: { data: { date: string; count: number }[] }) {
    const getColor = (count: number) => {
        if (count === 0) return "bg-zinc-800/50"
        if (count === 1) return "bg-purple-900/60"
        if (count === 2) return "bg-purple-700/70"
        if (count === 3) return "bg-purple-500/80"
        return "bg-emerald-500/90 shadow-[0_0_6px_rgba(34,211,172,0.5)]"
    }

    const weeks: { date: string; count: number }[][] = []
    for (let i = 0; i < data.length; i += 7) {
        weeks.push(data.slice(i, i + 7))
    }

    return (
        <div className={cn(
            "rounded-2xl p-6",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            <div className="flex items-center gap-2 mb-4">
                <Calendar className="w-5 h-5 text-purple-400" />
                <h3 className="text-lg font-semibold text-zinc-100">Activity</h3>
            </div>
            <div className="flex gap-1">
                {weeks.map((week, weekIndex) => (
                    <div key={weekIndex} className="flex flex-col gap-1">
                        {week.map((day, dayIndex) => (
                            <div
                                key={dayIndex}
                                className={cn(
                                    "w-3 h-3 rounded-sm transition-all duration-200",
                                    "hover:scale-125",
                                    getColor(day.count)
                                )}
                                title={`${day.date}: ${day.count} activities`}
                            />
                        ))}
                    </div>
                ))}
            </div>
            <div className="flex items-center justify-end gap-2 mt-4 text-xs text-zinc-500">
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
   ACHIEVEMENTS - Premium with Unlock Animation
   ============================================================================ */

function Achievements({ achievements }: { achievements: typeof ACHIEVEMENTS }) {
    return (
        <div className={cn(
            "rounded-2xl p-6",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            <div className="flex items-center gap-2 mb-4">
                <Trophy className="w-5 h-5 text-amber-400" />
                <h3 className="text-lg font-semibold text-zinc-100">Achievements</h3>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {achievements.map((achievement) => (
                    <div
                        key={achievement.id}
                        className={cn(
                            "relative flex flex-col items-center p-4 rounded-xl text-center",
                            "transition-all duration-300",
                            achievement.unlocked
                                ? [
                                    "bg-gradient-to-br from-amber-500/20 to-amber-600/10",
                                    "border border-amber-500/30",
                                    "shadow-[0_0_20px_rgba(245,158,11,0.2)]",
                                    "hover:shadow-[0_0_30px_rgba(245,158,11,0.3)]",
                                ]
                                : [
                                    "bg-zinc-800/40 border border-zinc-700/30",
                                    "opacity-60 grayscale",
                                    "hover:opacity-80 hover:grayscale-0",
                                ]
                        )}
                    >
                        {/* Unlock glow */}
                        {achievement.unlocked && (
                            <div className="absolute inset-0 rounded-xl bg-amber-500/5 animate-pulse" />
                        )}

                        <span className={cn(
                            "text-3xl mb-2 transition-transform duration-300",
                            achievement.unlocked && "animate-bounce"
                        )}>
                            {achievement.icon}
                        </span>
                        <span className={cn(
                            "text-sm font-medium mb-1",
                            achievement.unlocked ? "text-amber-300" : "text-zinc-400"
                        )}>
                            {achievement.name}
                        </span>
                        <span className="text-xs text-zinc-500">
                            {achievement.description}
                        </span>
                    </div>
                ))}
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PROGRESS PAGE
   ============================================================================ */

export default function ProgressPage() {
    const { user } = useAuth()
    const [tracks, setTracks] = useState<TrackSummary[]>([])
    const [heatmapData, setHeatmapData] = useState<{ date: string; count: number }[]>([])

    useEffect(() => {
        setTracks(getMockTracks())
        setHeatmapData(generateHeatmapData())
    }, [])

    const overallProgress = tracks.length > 0
        ? Math.round(tracks.reduce((sum, t) => sum + t.progress, 0) / tracks.length)
        : 0

    const userName = user?.full_name?.split(" ")[0] || "Learner"

    return (
        <div className="min-h-screen bg-zinc-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
                {/* Hero Header */}
                <ProgressHero level={DEFAULT_STATS.level} userName={userName} />

                {/* Stats Grid */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <StatCard
                        icon={<Trophy className="w-6 h-6 text-amber-400" />}
                        label="Total XP"
                        value={DEFAULT_STATS.totalXP.toLocaleString()}
                        color="gold"
                        glow={DEFAULT_STATS.totalXP > 0}
                    />
                    <StatCard
                        icon={<Flame className="w-6 h-6 text-orange-400" />}
                        label="Day Streak"
                        value={DEFAULT_STATS.streak}
                        color="fire"
                        glow={DEFAULT_STATS.streak > 0}
                    />
                    <StatCard
                        icon={<Clock className="w-6 h-6 text-blue-400" />}
                        label="Hours Learned"
                        value={DEFAULT_STATS.totalHours}
                        color="blue"
                    />
                    <StatCard
                        icon={<CheckCircle2 className="w-6 h-6 text-emerald-400" />}
                        label="Tasks Done"
                        value={DEFAULT_STATS.tasksCompleted}
                        color="mint"
                        glow={DEFAULT_STATS.tasksCompleted > 0}
                    />
                </div>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Left Column */}
                    <div className="lg:col-span-2 space-y-6">
                        {/* Overall Progress Ring */}
                        <OverallProgressRing progress={overallProgress} userName={userName} />

                        {/* Track Progress */}
                        <div className={cn(
                            "rounded-2xl p-6",
                            "bg-zinc-900/80 backdrop-blur-sm",
                            "border border-zinc-800/60"
                        )}>
                            <div className="flex items-center gap-2 mb-4">
                                <BookOpen className="w-5 h-5 text-purple-400" />
                                <h3 className="text-lg font-semibold text-zinc-100">Track Progress</h3>
                            </div>
                            <div className="space-y-3">
                                {tracks.map((track) => (
                                    <TrackProgressCard key={track.id} track={track} />
                                ))}
                            </div>
                        </div>

                        {/* Activity Heatmap */}
                        <ActivityHeatmap data={heatmapData} />
                    </div>

                    {/* Right Column */}
                    <div>
                        <Achievements achievements={ACHIEVEMENTS} />
                    </div>
                </div>
            </div>
        </div>
    )
}
