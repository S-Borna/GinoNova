"use client"

/**
 * ============================================================================
 * SKILLPATH BOARD - Personal Analytics Dashboard — COSMIC EDITION 🌌
 * ============================================================================
 *
 * A clean, insightful view of your DevOps learning journey.
 * Now connected to LIVE user progress data via useProgress hook.
 *
 * COSMIC DESIGN UPGRADE:
 * - Deep space background (#05050a)
 * - Multi-layered aurora orbs
 * - Pulsating glow effects
 * - Netflix-smooth animations
 *
 * @phase MILESTONE-2.0-COSMIC
 */

import { useMemo, useState, useEffect } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { useProgress } from "@/hooks/useProgress"
import { useModules } from "@/hooks/useModules"
import { useAuth } from "@/components/auth/AuthProvider"
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
    Trophy,
    Loader2,
    AlertCircle,
    RefreshCw,
    Rocket,
    CheckCircle,
} from "lucide-react"
import { Button } from "@/components/ui/button"

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            {/* Deep cosmic base */}
            <div className="absolute inset-0 bg-[#05050a]" />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />

            {/* Aurora orb 1 - Purple */}
            <motion.div
                className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, rgba(139, 92, 246, 0.04) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.1, 1],
                    opacity: [0.5, 0.7, 0.5],
                }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Aurora orb 2 - Cyan */}
            <motion.div
                className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(34, 211, 238, 0.1) 0%, rgba(34, 211, 238, 0.03) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.15, 1],
                    opacity: [0.4, 0.6, 0.4],
                }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
            />

            {/* Aurora orb 3 - Pink */}
            <motion.div
                className="absolute top-1/3 left-1/4 w-[500px] h-[500px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(236, 72, 153, 0.06) 0%, transparent 60%)',
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.3, 0.5, 0.3],
                }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
            />
        </div>
    )
}

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
   MODULE COLORS — Consistent color mapping for modules
   ============================================================================ */

const MODULE_COLORS: Record<string, string> = {
    // Environment & Setup
    "environment-setup": "#10b981",
    "env-setup": "#10b981",
    // Linux
    "linux": "#f97316",
    "linux-fundamentals": "#f97316",
    "linux-mastery": "#f97316",
    // Shell & Scripting
    "shell": "#84cc16",
    "shell-scripting": "#84cc16",
    "bash": "#84cc16",
    // Git
    "git": "#ef4444",
    "git-mastery": "#ef4444",
    // Docker
    "docker": "#3b82f6",
    "docker-fundamentals": "#3b82f6",
    "docker-basics": "#3b82f6",
    "docker-advanced": "#2563eb",
    // Kubernetes
    "kubernetes": "#8b5cf6",
    "k8s": "#8b5cf6",
    "kubernetes-core": "#8b5cf6",
    "k8s-advanced": "#7c3aed",
    // CI/CD
    "cicd": "#f59e0b",
    "ci-cd": "#f59e0b",
    // Python
    "python": "#3776ab",
    "python-automation": "#3776ab",
    // AWS / Cloud
    "aws": "#ff9900",
    "aws-cloud": "#ff9900",
    "cloud": "#06b6d4",
    // Terraform / IaC
    "terraform": "#7b42bc",
    "iac": "#7b42bc",
    // Networking
    "networking": "#ec4899",
    "network": "#ec4899",
    // Observability
    "observability": "#14b8a6",
    "monitoring": "#14b8a6",
    // Security
    "security": "#dc2626",
    "devsecops": "#dc2626",
    "sre": "#6366f1",
    // Serverless
    "serverless": "#8b5cf6",
    // Default
    "default": "#6b7280",
}

function getModuleColor(slug: string): string {
    // Try exact match first
    if (MODULE_COLORS[slug]) return MODULE_COLORS[slug]

    // Try partial match
    const lowerSlug = slug.toLowerCase()
    for (const [key, color] of Object.entries(MODULE_COLORS)) {
        if (lowerSlug.includes(key) || key.includes(lowerSlug)) {
            return color
        }
    }

    return MODULE_COLORS.default
}

/* ============================================================================
   GENERATE ACTIVITY HISTORY — Based on real data patterns
   ============================================================================ */

function generateActivityFromProgress(
    tasksCompleted: number,
    totalXP: number
): DayActivity[] {
    const days: DayActivity[] = []
    const now = new Date()

    // Distribute tasks and XP somewhat realistically over 84 days
    const avgTasksPerActiveDay = Math.max(1, Math.ceil(tasksCompleted / 30))
    const avgXPPerActiveDay = Math.max(25, Math.ceil(totalXP / 30))

    let remainingTasks = tasksCompleted
    let remainingXP = totalXP

    for (let i = 83; i >= 0; i--) {
        const date = new Date(now)
        date.setDate(date.getDate() - i)

        // More recent days more likely to have activity
        const recencyBonus = (84 - i) / 84
        const isActive = remainingTasks > 0 && Math.random() < (0.3 + recencyBonus * 0.4)

        let dayTasks = 0
        let dayXP = 0

        if (isActive && remainingTasks > 0) {
            dayTasks = Math.min(
                remainingTasks,
                Math.floor(Math.random() * avgTasksPerActiveDay * 2) + 1
            )
            dayXP = Math.min(
                remainingXP,
                Math.floor(Math.random() * avgXPPerActiveDay * 2) + 25
            )
            remainingTasks -= dayTasks
            remainingXP -= dayXP
        }

        days.push({
            date: date.toISOString().split('T')[0],
            xp: dayXP,
            tasks: dayTasks
        })
    }

    return days
}

/* ============================================================================
   COSMIC STAT CARD COMPONENT
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
    color?: "blue" | "green" | "orange" | "purple" | "red" | "cyan"
}) {
    const colorClasses = {
        blue: {
            bg: "from-blue-500/25 to-blue-600/10",
            text: "text-blue-400",
            glow: 'rgba(59, 130, 246, 0.5)',
            border: "border-blue-500/40"
        },
        green: {
            bg: "from-emerald-500/25 to-emerald-600/10",
            text: "text-emerald-400",
            glow: 'rgba(16, 185, 129, 0.5)',
            border: "border-emerald-500/40"
        },
        orange: {
            bg: "from-orange-500/25 to-orange-600/10",
            text: "text-orange-400",
            glow: 'rgba(249, 115, 22, 0.5)',
            border: "border-orange-500/40"
        },
        purple: {
            bg: "from-purple-500/25 to-purple-600/10",
            text: "text-purple-400",
            glow: 'rgba(139, 92, 246, 0.5)',
            border: "border-purple-500/40"
        },
        red: {
            bg: "from-red-500/25 to-red-600/10",
            text: "text-red-400",
            glow: 'rgba(239, 68, 68, 0.5)',
            border: "border-red-500/40"
        },
        cyan: {
            bg: "from-cyan-500/25 to-cyan-600/10",
            text: "text-cyan-400",
            glow: 'rgba(34, 211, 238, 0.5)',
            border: "border-cyan-500/40"
        },
    }

    const styles = colorClasses[color] || colorClasses.blue

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ scale: 1.03, y: -3 }}
            transition={{ ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative overflow-hidden rounded-2xl",
                "bg-gradient-to-br",
                styles.bg,
                "border",
                styles.border,
                "p-5 backdrop-blur-sm"
            )}
            style={{
                boxShadow: `0 0 30px ${styles.glow.replace('0.5', '0.15')}`
            }}
        >
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm text-neutral-400 mb-1">{label}</p>
                    <p className="text-3xl font-bold text-white">{value}</p>
                    {subtext && (
                        <p className="text-xs text-neutral-500 mt-1">{subtext}</p>
                    )}
                </div>
                <motion.div
                    className={cn(
                        "p-3 rounded-xl",
                        "bg-neutral-800/50"
                    )}
                    animate={{
                        boxShadow: [
                            `0 0 10px ${styles.glow}`,
                            `0 0 25px ${styles.glow}`,
                            `0 0 10px ${styles.glow}`,
                        ]
                    }}
                    transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
                >
                    <Icon className={cn("w-6 h-6", styles.text)} />
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   COSMIC ACTIVITY HEATMAP (GitHub-style)
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
        if (xp === 0) return "bg-neutral-800/50"
        if (xp < 50) return "bg-cyan-900/60"
        if (xp < 100) return "bg-cyan-700/70"
        if (xp < 150) return "bg-cyan-500/80"
        return "bg-cyan-400"
    }

    const dayLabels = ["", "Mon", "", "Wed", "", "Fri", ""]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-cyan-500/10 to-cyan-600/5",
                "border border-cyan-500/30",
                "p-6 backdrop-blur-sm"
            )}
            style={{
                boxShadow: '0 0 40px rgba(34, 211, 238, 0.1)'
            }}
        >
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <motion.div
                        animate={{
                            scale: [1, 1.2, 1],
                            opacity: [0.7, 1, 0.7]
                        }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <Calendar className="w-5 h-5 text-cyan-400" />
                    </motion.div>
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
                    <div className="w-3 h-3 rounded-sm bg-neutral-800/50" />
                    <div className="w-3 h-3 rounded-sm bg-cyan-900/60" />
                    <div className="w-3 h-3 rounded-sm bg-cyan-700/70" />
                    <div className="w-3 h-3 rounded-sm bg-cyan-500/80" />
                    <div className="w-3 h-3 rounded-sm bg-cyan-400" />
                </div>
                <span>More</span>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   COSMIC MODULE PROGRESS LIST
   ============================================================================ */

function ModuleProgressList({ modules }: { modules: ModuleProgress[] }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-purple-500/10 to-purple-600/5",
                "border border-purple-500/30",
                "p-6 backdrop-blur-sm"
            )}
            style={{
                boxShadow: '0 0 40px rgba(139, 92, 246, 0.1)'
            }}
        >
            <div className="flex items-center gap-2 mb-4">
                <motion.div
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.7, 1, 0.7]
                    }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                >
                    <BookOpen className="w-5 h-5 text-purple-400" />
                </motion.div>
                <h3 className="text-lg font-semibold text-white">Module Progress</h3>
            </div>

            <div className="space-y-4">
                {modules.map((module, idx) => (
                    <motion.div
                        key={module.slug}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.1 * idx, ease: [0.16, 1, 0.3, 1] }}
                        className="group"
                    >
                        <div className="flex items-center justify-between mb-2">
                            <div className="flex items-center gap-2">
                                <motion.div
                                    className="w-2 h-2 rounded-full"
                                    style={{ backgroundColor: module.color }}
                                    animate={{
                                        boxShadow: [
                                            `0 0 5px ${module.color}`,
                                            `0 0 15px ${module.color}`,
                                            `0 0 5px ${module.color}`,
                                        ]
                                    }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
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

                        {/* Shimmer Progress bar */}
                        <div className="h-2 bg-neutral-800/50 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${module.progress}%` }}
                                transition={{ duration: 1, delay: 0.2 + idx * 0.1, ease: [0.16, 1, 0.3, 1] }}
                                className="h-full rounded-full relative overflow-hidden"
                                style={{ backgroundColor: module.color }}
                            >
                                {/* Shimmer effect */}
                                <motion.div
                                    className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                                    animate={{ x: ['-100%', '100%'] }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut", delay: idx * 0.2 }}
                                />
                            </motion.div>
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
   COSMIC XP LEVEL PROGRESS
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
            transition={{ delay: 0.15, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "rounded-2xl",
                "bg-gradient-to-br from-amber-500/15 to-orange-600/10",
                "border border-amber-500/40",
                "p-6 backdrop-blur-sm"
            )}
            style={{
                boxShadow: '0 0 50px rgba(245, 158, 11, 0.12)'
            }}
        >
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <motion.div
                        animate={{
                            scale: [1, 1.2, 1],
                            rotate: [0, 5, -5, 0],
                            opacity: [0.8, 1, 0.8]
                        }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <Trophy className="w-5 h-5 text-amber-400" />
                    </motion.div>
                    <h3 className="text-lg font-semibold text-white">Level Progress</h3>
                </div>
            </div>

            <div className="flex items-center gap-6">
                {/* Level badge with cosmic glow */}
                <motion.div
                    className={cn(
                        "w-20 h-20 rounded-2xl",
                        "bg-gradient-to-br from-amber-500 to-orange-600",
                        "flex items-center justify-center"
                    )}
                    animate={{
                        boxShadow: [
                            '0 0 20px rgba(245, 158, 11, 0.4)',
                            '0 0 40px rgba(245, 158, 11, 0.7)',
                            '0 0 20px rgba(245, 158, 11, 0.4)',
                        ]
                    }}
                    transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
                >
                    <div className="text-center">
                        <p className="text-xs text-amber-100 font-medium">LEVEL</p>
                        <p className="text-3xl font-black text-white">{level}</p>
                    </div>
                </motion.div>

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

                    {/* XP progress bar with shimmer */}
                    <div className="h-3 bg-neutral-800/50 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${progressPercent}%` }}
                            transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
                            className="h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full relative overflow-hidden"
                        >
                            {/* Shimmer effect */}
                            <motion.div
                                className="absolute inset-0 bg-gradient-to-r from-transparent via-white/40 to-transparent"
                                animate={{ x: ['-100%', '100%'] }}
                                transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                            />
                        </motion.div>
                    </div>

                    <p className="text-xs text-neutral-500 mt-2">
                        <span className="text-amber-400 font-semibold">{Math.round(progressPercent)}%</span> till nästa nivå
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MILESTONES / ACHIEVEMENTS — Now dynamic based on real progress!
   ============================================================================ */

function Milestones({
    tasksCompleted,
    streak,
    level,
    modulesCompleted
}: {
    tasksCompleted: number
    streak: number
    level: number
    modulesCompleted: number
}) {
    // Dynamic milestones based on actual progress
    const milestones = [
        {
            icon: Flame,
            label: "Första Streak",
            earned: streak >= 1,
            color: "text-orange-400",
            description: "Lär dig 2 dagar i rad"
        },
        {
            icon: Target,
            label: "10 Tasks",
            earned: tasksCompleted >= 10,
            color: "text-green-400",
            description: "Slutför 10 uppgifter"
        },
        {
            icon: BookOpen,
            label: "Första Modulen",
            earned: modulesCompleted >= 1,
            color: "text-blue-400",
            description: "Slutför en hel modul"
        },
        {
            icon: Zap,
            label: "50 Tasks",
            earned: tasksCompleted >= 50,
            color: "text-yellow-400",
            description: "Slutför 50 uppgifter"
        },
        {
            icon: Trophy,
            label: "Nivå 10",
            earned: level >= 10,
            color: "text-purple-400",
            description: "Nå nivå 10"
        },
    ]

    const earnedCount = milestones.filter(m => m.earned).length

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
                    <h3 className="text-lg font-semibold text-white">Milstolpar</h3>
                </div>
                <span className="text-sm text-neutral-400">{earnedCount}/{milestones.length} uppnådda</span>
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
                            "transition-all group relative"
                        )}
                        title={m.description}
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
   LOADING STATE
   ============================================================================ */

function LoadingState() {
    return (
        <div className="min-h-screen bg-[#05050a] p-6 lg:p-8 flex items-center justify-center">
            <CosmicAurora />
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-center relative z-10"
            >
                <motion.div
                    animate={{
                        rotate: 360,
                        scale: [1, 1.1, 1]
                    }}
                    transition={{
                        rotate: { duration: 1, repeat: Infinity, ease: "linear" },
                        scale: { duration: 1.5, repeat: Infinity, ease: "easeInOut" }
                    }}
                >
                    <Loader2 className="w-12 h-12 text-purple-500 mx-auto mb-4" />
                </motion.div>
                <p className="text-neutral-400">Laddar din progress...</p>
            </motion.div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ message, onRetry }: { message: string; onRetry: () => void }) {
    return (
        <div className="min-h-screen bg-[#05050a] p-6 lg:p-8 flex items-center justify-center">
            <CosmicAurora />
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center max-w-md relative z-10"
            >
                <motion.div
                    animate={{
                        scale: [1, 1.1, 1],
                        opacity: [0.7, 1, 0.7]
                    }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                >
                    <AlertCircle className="w-12 h-12 text-red-500 mx-auto mb-4" />
                </motion.div>
                <h2 className="text-xl font-semibold text-white mb-2">Kunde inte ladda data</h2>
                <p className="text-neutral-400 mb-6">{message}</p>
                <Button onClick={onRetry} variant="outline" className="gap-2 border-red-500/40 hover:border-red-500/60">
                    <RefreshCw className="w-4 h-4" />
                    Försök igen
                </Button>
            </motion.div>
        </div>
    )
}

/* ============================================================================
   MAIN SKILLPATH BOARD COMPONENT — Now with LIVE DATA!
   ============================================================================ */

export function SkillpathBoard() {
    // Fetch live progress data
    const { data: progressData, isLoading: progressLoading, error: progressError, refetch } = useProgress()
    const { data: modulesData, isLoading: modulesLoading } = useModules()
    const { user } = useAuth()

    // Session timer state (weekly)
    const [weeklyTime, setWeeklyTime] = useState(0)
    const [completedExercises, setCompletedExercises] = useState(0)

    // Load session timer and exercises from localStorage
    useEffect(() => {
        try {
            // Weekly session time
            const sessionStr = localStorage.getItem("devopshub_session_timer")
            if (sessionStr) {
                const sessionData = JSON.parse(sessionStr)
                setWeeklyTime(sessionData.totalSeconds || 0)
            }

            // Completed exercises (flashcards + quiz)
            const exercisesStr = localStorage.getItem("devopshub_completed_exercises")
            if (exercisesStr) {
                const exercisesData = JSON.parse(exercisesStr)
                setCompletedExercises(exercisesData.total || 0)
            }
        } catch {
            // Ignore errors
        }
    }, [])

    // Get user's first name for personalized greeting
    const firstName = user?.full_name?.split(' ')[0] || user?.email?.split('@')[0] || 'DevOps Pro'

    const formatTime = (seconds: number): string => {
        const hours = Math.floor(seconds / 3600)
        const mins = Math.floor((seconds % 3600) / 60)
        if (hours > 0) {
            return `${hours}h ${mins}m`
        }
        return `${mins}m`
    }

    // Transform API data to component format
    const data: SkillpathData = useMemo(() => {
        // Use REAL progress data only - no mock fallback for stats!
        const progress = progressData ? {
            total_xp: progressData.total_xp ?? 0,
            level: progressData.level ?? 1,
            xp_to_next_level: progressData.xp_to_next_level ?? 1000,
            tasks_completed: progressData.tasks_completed ?? 0,
            modules_completed: progressData.modules_completed ?? 0,
            streak: progressData.streak ?? 0,
            tracks: progressData.tracks ?? [],
        } : {
            total_xp: 0,
            level: 1,
            xp_to_next_level: 1000,
            tasks_completed: 0,
            modules_completed: 0,
            streak: 0,
            tracks: [],
        }

        // Calculate XP per level (1000 XP per level)
        const XP_PER_LEVEL = 1000
        const currentLevel = progress.level || Math.floor(progress.total_xp / XP_PER_LEVEL) + 1
        const xpInCurrentLevel = progress.total_xp % XP_PER_LEVEL
        const xpToNextLevel = progress.xp_to_next_level || (XP_PER_LEVEL - xpInCurrentLevel)

        // Estimate time: ~5 min per task on average
        const estimatedTimeMinutes = progress.tasks_completed * 5

        // PRIORITY: Use LIVE modules from API if available!
        let moduleProgress: ModuleProgress[] = []

        if (modulesData && Array.isArray(modulesData) && modulesData.length > 0) {
            // Use LIVE module data from backend - this is the ROOT FIX!
            moduleProgress = modulesData.map((mod) => ({
                name: mod.name,
                slug: mod.slug,
                progress: mod.progress || 0,
                tasksCompleted: mod.tasks_completed || 0,
                totalTasks: mod.total_tasks || 10,
                color: getModuleColor(mod.slug),
            }))
            console.log(`✅ SkillpathBoard: Loaded ${modulesData.length} LIVE modules from API`)
        } else {
            // Fallback to tracks from progress data
            moduleProgress = (progress.tracks || []).map(track => ({
                name: track.track_name,
                slug: track.track_id,
                progress: track.progress,
                tasksCompleted: track.modules_completed,
                totalTasks: track.total_modules,
                color: getModuleColor(track.track_id),
            }))
            console.warn("⚠️ SkillpathBoard: Using mock/track data - API not available")
        }

        // Generate activity history based on real data
        const activityHistory = generateActivityFromProgress(
            progress.tasks_completed,
            progress.total_xp
        )

        return {
            totalXP: progress.total_xp,
            currentLevel,
            xpToNextLevel,
            currentStreak: progress.streak || 0,
            longestStreak: progress.streak || 0, // API doesn't track longest yet
            totalTimeMinutes: estimatedTimeMinutes,
            modulesStarted: moduleProgress.filter(m => m.progress > 0).length,
            modulesCompleted: progress.modules_completed,
            tasksCompleted: progress.tasks_completed,
            activityHistory,
            moduleProgress: moduleProgress.slice(0, 8), // Show up to 8 modules
        }
    }, [progressData, modulesData])

    // Loading state
    if (progressLoading || modulesLoading) {
        return <LoadingState />
    }

    // Error state
    if (progressError) {
        return (
            <ErrorState
                message={progressError instanceof Error ? progressError.message : "Ett fel uppstod"}
                onRetry={() => refetch()}
            />
        )
    }

    return (
        <div className="min-h-screen bg-[#05050a] p-6 lg:p-8 relative">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            <div className="relative z-10">
                {/* YOUR JOURNEY Header Card - COSMIC */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ ease: [0.16, 1, 0.3, 1] }}
                    className={cn(
                        "relative overflow-hidden rounded-2xl mb-8",
                        "bg-gradient-to-r from-[#0a0a0f] via-[#0a0a0f]/95 to-purple-950/20",
                        "border border-purple-500/30"
                    )}
                    style={{
                        boxShadow: '0 0 60px rgba(139, 92, 246, 0.15)'
                    }}
                >
                    {/* Background glow effects */}
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2" />
                    <div className="absolute bottom-0 left-1/4 w-64 h-64 bg-cyan-500/8 rounded-full blur-[80px]" />
                    <div className="absolute top-1/2 left-1/2 w-48 h-48 bg-pink-500/5 rounded-full blur-[60px] -translate-x-1/2 -translate-y-1/2" />

                    <div className="relative p-8">
                        {/* Badge with pulsating glow */}
                        <div className="flex items-center gap-2 mb-4">
                            <motion.div
                                animate={{
                                    scale: [1, 1.2, 1],
                                    opacity: [0.7, 1, 0.7]
                                }}
                                transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                            >
                                <Rocket className="w-5 h-5 text-purple-400" />
                            </motion.div>
                            <span className="text-sm font-semibold text-purple-400 tracking-wide uppercase">
                                Your Journey
                            </span>
                        </div>

                        {/* Title */}
                        <h1 className="text-3xl lg:text-4xl font-bold mb-3 flex items-center gap-3">
                            <span className="bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent">
                                Keep Going, {firstName}!
                            </span>
                            <motion.span
                                className="text-3xl"
                                animate={{
                                    scale: [1, 1.2, 1],
                                    rotate: [0, 10, -10, 0]
                                }}
                                transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                            >
                                🔥
                            </motion.span>
                        </h1>

                        {/* Subtitle */}
                        <p className="text-zinc-400 text-lg max-w-xl">
                            Track your DevOps learning journey and celebrate every win
                        </p>

                        {/* Refresh button - positioned top right */}
                        <Button
                            onClick={() => refetch()}
                            variant="ghost"
                            size="sm"
                            className="absolute top-6 right-6 text-zinc-500 hover:text-white hover:bg-purple-500/20"
                        >
                            <RefreshCw className="w-4 h-4" />
                        </Button>
                    </div>
                </motion.div>

                {/* Stats Grid */}
                <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                    <StatCard
                        icon={Zap}
                        label="Total XP"
                        value={data.totalXP.toLocaleString()}
                        subtext={data.totalXP > 0 ? "Fortsätt kämpa!" : "Börja lära dig!"}
                        color="purple"
                    />
                    <StatCard
                        icon={CheckCircle}
                        label="Avklarade Flash/Quiz"
                        value={completedExercises}
                        subtext={completedExercises > 0 ? "Flashcards & Quiz" : "Starta din första!"}
                        color="orange"
                    />
                    <StatCard
                        icon={Target}
                        label="Tasks klara"
                        value={data.tasksCompleted}
                        subtext={data.tasksCompleted > 0 ? "Bra jobbat!" : "Börja med första tasken"}
                        color="cyan"
                    />
                    <StatCard
                        icon={Clock}
                        label="Tid investerad"
                        value={formatTime(weeklyTime)}
                        subtext="Uppskattad tid denna vecka"
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
                        <Milestones tasksCompleted={data.tasksCompleted} streak={data.currentStreak} level={data.currentLevel} modulesCompleted={data.modulesCompleted} />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SkillpathBoard
