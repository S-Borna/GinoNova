"use client"

/**
 * ============================================================================
 * SKILLPATH BOARD - Personal Analytics Dashboard
 * ============================================================================
 *
 * A clean, insightful view of your DevOps learning journey.
 * 
 * Features:
 * - XP Progress over time
 * - Activity heatmap (GitHub-style)
 * - Module completion breakdown
 * - Current streak & milestones
 * - Time invested stats
 *
 * @phase ENTERPRISE-LEVEL-5
 */

import { useMemo } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    TrendingUp,
    Flame,
    Target,
    Clock,
    Award,
    BookOpen,
    Zap,
    Calendar,
    ChevronRight,
    Trophy
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface DayActivity {
    date: string
    xp: number
    tasks: number
}

interface ModuleProgress {
    name: string
    slug: string
    progress: number
    tasksCompleted: number
    totalTasks: number
    color: string
}

interface SkillpathData {
    totalXP: number
    currentLevel: number
    xpToNextLevel: number
    currentStreak: number
    longestStreak: number
    totalTimeMinutes: number
    modulesStarted: number
    modulesCompleted: number
    tasksCompleted: number
    activityHistory: DayActivity[]
    moduleProgress: ModuleProgress[]
}

/* ============================================================================
   MOCK DATA (Replace with API call)
   ============================================================================ */

const MOCK_DATA: SkillpathData = {
    totalXP: 2450,
    currentLevel: 5,
    xpToNextLevel: 550,
    currentStreak: 3,
    longestStreak: 12,
    totalTimeMinutes: 840, // 14 hours
    modulesStarted: 4,
    modulesCompleted: 1,
    tasksCompleted: 28,
    activityHistory: generateMockActivity(),
    moduleProgress: [
        { name: "Linux Fundamentals", slug: "linux", progress: 100, tasksCompleted: 12, totalTasks: 12, color: "#22c55e" },
        { name: "Docker Basics", slug: "docker", progress: 65, tasksCompleted: 8, totalTasks: 12, color: "#3b82f6" },
        { name: "Kubernetes", slug: "kubernetes", progress: 25, tasksCompleted: 3, totalTasks: 12, color: "#8b5cf6" },
        { name: "CI/CD Pipelines", slug: "cicd", progress: 10, tasksCompleted: 1, totalTasks: 10, color: "#f59e0b" },
    ]
}

function generateMockActivity(): DayActivity[] {
    const days: DayActivity[] = []
    const now = new Date()
    
    for (let i = 83; i >= 0; i--) {
        const date = new Date(now)
        date.setDate(date.getDate() - i)
        
        // Random activity (some days more active than others)
        const isActive = Math.random() > 0.4
        const xp = isActive ? Math.floor(Math.random() * 150) + 25 : 0
        const tasks = isActive ? Math.floor(Math.random() * 4) + 1 : 0
        
        days.push({
            date: date.toISOString().split('T')[0],
            xp,
            tasks
        })
    }
    return days
}

/* ============================================================================
   STAT CARD COMPONENT
   ============================================================================ */

function StatCard({ 
    icon: Icon, 
    label, 
    value, 
    subtext,
    color = "blue"
}: { 
    icon: React.ElementType
    label: string
    value: string | number
    subtext?: string
    color?: "blue" | "green" | "orange" | "purple" | "red"
}) {
    const colorClasses = {
        blue: "from-blue-500/20 to-blue-600/10 text-blue-400",
        green: "from-green-500/20 to-green-600/10 text-green-400",
        orange: "from-orange-500/20 to-orange-600/10 text-orange-400",
        purple: "from-purple-500/20 to-purple-600/10 text-purple-400",
        red: "from-red-500/20 to-red-600/10 text-red-400",
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-2xl",
                "bg-gradient-to-br",
                colorClasses[color],
                "border border-neutral-800",
                "p-5"
            )}
        >
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm text-neutral-400 mb-1">{label}</p>
                    <p className="text-3xl font-bold text-white">{value}</p>
                    {subtext && (
                        <p className="text-xs text-neutral-500 mt-1">{subtext}</p>
                    )}
                </div>
                <div className={cn(
                    "p-3 rounded-xl",
                    "bg-neutral-800/50"
                )}>
                    <Icon className="w-6 h-6" />
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   ACTIVITY HEATMAP (GitHub-style)
   ============================================================================ */

function ActivityHeatmap({ data }: { data: DayActivity[] }) {
    // Group by weeks (12 weeks = 84 days)
    const weeks = useMemo(() => {
        const result: DayActivity[][] = []
        for (let i = 0; i < data.length; i += 7) {
            result.push(data.slice(i, i + 7))
        }
        return result
    }, [data])

    const getIntensity = (xp: number): string => {
        if (xp === 0) return "bg-neutral-800"
        if (xp < 50) return "bg-green-900/60"
        if (xp < 100) return "bg-green-700/70"
        if (xp < 150) return "bg-green-500/80"
        return "bg-green-400"
    }

    const dayLabels = ["", "Mon", "", "Wed", "", "Fri", ""]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className={cn(
                "rounded-2xl",
                "bg-neutral-900/50 border border-neutral-800",
                "p-6"
            )}
        >
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <Calendar className="w-5 h-5 text-green-400" />
                    <h3 className="text-lg font-semibold text-white">Activity</h3>
                </div>
                <span className="text-sm text-neutral-400">Last 12 weeks</span>
            </div>

            <div className="flex gap-1">
                {/* Day labels */}
                <div className="flex flex-col gap-1 mr-2 text-[10px] text-neutral-500">
                    {dayLabels.map((day, i) => (
                        <div key={i} className="h-3 flex items-center">{day}</div>
                    ))}
                </div>

                {/* Heatmap grid */}
                <div className="flex gap-1 flex-1 overflow-x-auto">
                    {weeks.map((week, weekIdx) => (
                        <div key={weekIdx} className="flex flex-col gap-1">
                            {week.map((day, dayIdx) => (
                                <div
                                    key={dayIdx}
                                    className={cn(
                                        "w-3 h-3 rounded-sm",
                                        getIntensity(day.xp),
                                        "transition-colors cursor-pointer",
                                        "hover:ring-1 hover:ring-white/30"
                                    )}
                                    title={`${day.date}: ${day.xp} XP, ${day.tasks} tasks`}
                                />
                            ))}
                        </div>
                    ))}
                </div>
            </div>

            {/* Legend */}
            <div className="flex items-center justify-end gap-2 mt-4 text-xs text-neutral-500">
                <span>Less</span>
                <div className="flex gap-0.5">
                    <div className="w-3 h-3 rounded-sm bg-neutral-800" />
                    <div className="w-3 h-3 rounded-sm bg-green-900/60" />
                    <div className="w-3 h-3 rounded-sm bg-green-700/70" />
                    <div className="w-3 h-3 rounded-sm bg-green-500/80" />
                    <div className="w-3 h-3 rounded-sm bg-green-400" />
                </div>
                <span>More</span>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MODULE PROGRESS LIST
   ============================================================================ */

function ModuleProgressList({ modules }: { modules: ModuleProgress[] }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className={cn(
                "rounded-2xl",
                "bg-neutral-900/50 border border-neutral-800",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-4">
                <BookOpen className="w-5 h-5 text-blue-400" />
                <h3 className="text-lg font-semibold text-white">Module Progress</h3>
            </div>

            <div className="space-y-4">
                {modules.map((module, idx) => (
                    <motion.div
                        key={module.slug}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.1 * idx }}
                        className="group"
                    >
                        <div className="flex items-center justify-between mb-2">
                            <div className="flex items-center gap-2">
                                <div 
                                    className="w-2 h-2 rounded-full"
                                    style={{ backgroundColor: module.color }}
                                />
                                <span className="text-sm font-medium text-neutral-200">
                                    {module.name}
                                </span>
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="text-xs text-neutral-500">
                                    {module.tasksCompleted}/{module.totalTasks} tasks
                                </span>
                                <span className="text-sm font-semibold text-white">
                                    {module.progress}%
                                </span>
                            </div>
                        </div>
                        
                        {/* Progress bar */}
                        <div className="h-2 bg-neutral-800 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${module.progress}%` }}
                                transition={{ duration: 1, delay: 0.2 + idx * 0.1 }}
                                className="h-full rounded-full"
                                style={{ backgroundColor: module.color }}
                            />
                        </div>
                    </motion.div>
                ))}
            </div>

            {modules.length === 0 && (
                <div className="text-center py-8 text-neutral-500">
                    <BookOpen className="w-10 h-10 mx-auto mb-2 opacity-50" />
                    <p>No modules started yet</p>
                </div>
            )}
        </motion.div>
    )
}

/* ============================================================================
   XP LEVEL PROGRESS
   ============================================================================ */

function XPLevelProgress({ 
    level, 
    totalXP, 
    xpToNext 
}: { 
    level: number
    totalXP: number
    xpToNext: number 
}) {
    const xpForCurrentLevel = 1000 // XP needed per level
    const currentLevelXP = totalXP % xpForCurrentLevel
    const progressPercent = (currentLevelXP / xpForCurrentLevel) * 100

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.15 }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-indigo-500/20 to-purple-600/10",
                "border border-neutral-800",
                "p-6"
            )}
        >
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <Trophy className="w-5 h-5 text-yellow-400" />
                    <h3 className="text-lg font-semibold text-white">Level Progress</h3>
                </div>
            </div>

            <div className="flex items-center gap-6">
                {/* Level badge */}
                <div className={cn(
                    "w-20 h-20 rounded-2xl",
                    "bg-gradient-to-br from-yellow-500 to-orange-600",
                    "flex items-center justify-center",
                    "shadow-lg shadow-yellow-500/20"
                )}>
                    <div className="text-center">
                        <p className="text-xs text-yellow-100 font-medium">LEVEL</p>
                        <p className="text-3xl font-black text-white">{level}</p>
                    </div>
                </div>

                {/* Progress info */}
                <div className="flex-1">
                    <div className="flex justify-between text-sm mb-2">
                        <span className="text-neutral-400">
                            {totalXP.toLocaleString()} XP total
                        </span>
                        <span className="text-neutral-300 font-medium">
                            {xpToNext} XP to Level {level + 1}
                        </span>
                    </div>
                    
                    {/* XP progress bar */}
                    <div className="h-3 bg-neutral-800 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${progressPercent}%` }}
                            transition={{ duration: 1.2, ease: "easeOut" }}
                            className="h-full bg-gradient-to-r from-yellow-500 to-orange-500 rounded-full"
                        />
                    </div>
                    
                    <p className="text-xs text-neutral-500 mt-2">
                        {Math.round(progressPercent)}% to next level
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MILESTONES / ACHIEVEMENTS
   ============================================================================ */

function Milestones() {
    const milestones = [
        { icon: Flame, label: "First Streak", earned: true, color: "text-orange-400" },
        { icon: Target, label: "10 Tasks Done", earned: true, color: "text-green-400" },
        { icon: Award, label: "Module Master", earned: true, color: "text-blue-400" },
        { icon: Zap, label: "Speed Learner", earned: false, color: "text-yellow-400" },
        { icon: Trophy, label: "Level 10", earned: false, color: "text-purple-400" },
    ]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.25 }}
            className={cn(
                "rounded-2xl",
                "bg-neutral-900/50 border border-neutral-800",
                "p-6"
            )}
        >
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <Award className="w-5 h-5 text-purple-400" />
                    <h3 className="text-lg font-semibold text-white">Milestones</h3>
                </div>
                <span className="text-sm text-neutral-400">3/5 earned</span>
            </div>

            <div className="flex gap-3 flex-wrap">
                {milestones.map((m, idx) => (
                    <div
                        key={idx}
                        className={cn(
                            "flex items-center gap-2 px-3 py-2 rounded-xl",
                            m.earned 
                                ? "bg-neutral-800" 
                                : "bg-neutral-800/30 opacity-50",
                            "transition-all"
                        )}
                    >
                        <m.icon className={cn("w-4 h-4", m.earned ? m.color : "text-neutral-600")} />
                        <span className={cn(
                            "text-sm",
                            m.earned ? "text-neutral-200" : "text-neutral-500"
                        )}>
                            {m.label}
                        </span>
                    </div>
                ))}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN SKILLPATH BOARD COMPONENT
   ============================================================================ */

export function SkillpathBoard() {
    // TODO: Replace with actual API call
    const data = MOCK_DATA

    const formatTime = (minutes: number): string => {
        const hours = Math.floor(minutes / 60)
        const mins = minutes % 60
        return `${hours}h ${mins}m`
    }

    return (
        <div className="min-h-screen bg-gray-950 p-6 lg:p-8">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <h1 className="text-3xl font-bold text-white mb-2">
                    Skillpath Board
                </h1>
                <p className="text-neutral-400">
                    Your DevOps learning journey at a glance
                </p>
            </motion.div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                <StatCard
                    icon={Zap}
                    label="Total XP"
                    value={data.totalXP.toLocaleString()}
                    subtext="Keep grinding!"
                    color="purple"
                />
                <StatCard
                    icon={Flame}
                    label="Current Streak"
                    value={`${data.currentStreak} days`}
                    subtext={`Best: ${data.longestStreak} days`}
                    color="orange"
                />
                <StatCard
                    icon={Target}
                    label="Tasks Done"
                    value={data.tasksCompleted}
                    subtext="Great progress"
                    color="green"
                />
                <StatCard
                    icon={Clock}
                    label="Time Invested"
                    value={formatTime(data.totalTimeMinutes)}
                    subtext="Time well spent"
                    color="blue"
                />
            </div>

            {/* Main Content Grid */}
            <div className="grid lg:grid-cols-2 gap-6">
                {/* Left Column */}
                <div className="space-y-6">
                    <XPLevelProgress
                        level={data.currentLevel}
                        totalXP={data.totalXP}
                        xpToNext={data.xpToNextLevel}
                    />
                    <ActivityHeatmap data={data.activityHistory} />
                </div>

                {/* Right Column */}
                <div className="space-y-6">
                    <ModuleProgressList modules={data.moduleProgress} />
                    <Milestones />
                </div>
            </div>
        </div>
    )
}

export default SkillpathBoard
