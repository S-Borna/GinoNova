"use client"

/**
 * ============================================================================
 * DASHBOARD PAGE — PREMIUM DELUXE EDITION ✨
 * ============================================================================
 *
 * The MOTHERSHIP - Command Center for DevOps Learning
 *
 * Design Philosophy:
 * - Premium glow effects matching Progress/Studyflow
 * - Chill Mint (#22D3AC) for success/progress
 * - Focus Purple (#8B5CF6) for primary accent
 * - XP Gold (#F59E0B) for achievements
 * - Fire Orange (#F97316) for streaks
 * - Glassmorphism cards with hover effects
 *
 * @phase PREMIUM-DELUXE-POLISH
 */

import { useEffect, useState, useCallback } from "react"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { getDashboardSummary, DashboardSummary } from "@/lib/dashboard"
import { motion } from "framer-motion"
import Link from "next/link"

// 🛡️ SECURITY: Disable prefetching on all links
const SecureLink = ({ href, children, className }: { href: string; children: React.ReactNode; className?: string }) => (
    <Link href={href} prefetch={false} className={className}>{children}</Link>
)

// @saas/ui Design System
import { PageLayout, Section } from "@saas/ui"

// UI Components
import { Button } from "@/components/ui/button"
import {
    RefreshCw,
    Zap,
    Flame,
    BookOpen,
    Target,
    Trophy,
    Sparkles,
    Star,
    Rocket,
    ArrowRight,
    Play,
    Clock,
    TrendingUp,
    ChevronRight,
} from "lucide-react"

/* ============================================================================
   HELPERS
   ============================================================================ */

function calculateLevel(xp: number): { level: number; currentXP: number; xpToNextLevel: number } {
    let level = 1
    let totalXPForLevel = 100
    let remainingXP = xp

    while (remainingXP >= totalXPForLevel) {
        remainingXP -= totalXPForLevel
        level++
        totalXPForLevel = Math.floor(100 * Math.pow(1.5, level - 1))
    }

    return {
        level,
        currentXP: remainingXP,
        xpToNextLevel: totalXPForLevel,
    }
}

/* ============================================================================
   PREMIUM HERO - Command Center Header
   ============================================================================ */

function PremiumHero({ userName, level, streak }: { userName: string; level: number; streak: number }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-zinc-900 via-purple-950/40 to-zinc-900",
                "border border-purple-500/20",
                "p-8 md:p-10"
            )}
        >
            {/* Ambient glow effects */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-500/15 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-emerald-500/10 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />
            <div className="absolute top-1/2 left-1/2 w-[300px] h-[300px] bg-blue-500/5 rounded-full blur-[80px] -translate-x-1/2 -translate-y-1/2" />

            {/* Animated sparkles */}
            <motion.div
                className="absolute top-8 right-20 text-purple-400/60"
                animate={{ rotate: 360, scale: [1, 1.2, 1] }}
                transition={{ duration: 4, repeat: Infinity }}
            >
                <Sparkles className="w-6 h-6" />
            </motion.div>
            <motion.div
                className="absolute bottom-12 right-40 text-emerald-400/40"
                animate={{ rotate: -360, scale: [1, 1.3, 1] }}
                transition={{ duration: 5, repeat: Infinity, delay: 1 }}
            >
                <Star className="w-5 h-5" />
            </motion.div>
            <motion.div
                className="absolute top-1/2 right-16 text-amber-400/30"
                animate={{ y: [0, -10, 0] }}
                transition={{ duration: 3, repeat: Infinity }}
            >
                <Zap className="w-4 h-4" />
            </motion.div>

            <div className="relative flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                <div>
                    <motion.div
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.2 }}
                        className="flex items-center gap-3 mb-3"
                    >
                        <div className={cn(
                            "p-2 rounded-xl",
                            "bg-gradient-to-br from-purple-500/20 to-purple-600/10",
                            "border border-purple-500/30"
                        )}>
                            <Rocket className="w-5 h-5 text-purple-400" />
                        </div>
                        <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                            Command Center
                        </span>
                    </motion.div>

                    <motion.h1
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.3 }}
                        className={cn(
                            "text-3xl md:text-4xl lg:text-5xl font-black mb-3",
                            "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                        )}
                    >
                        Welcome back, {userName}! 🚀
                    </motion.h1>

                    <motion.p
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.4 }}
                        className="text-zinc-400 text-lg max-w-xl"
                    >
                        Your DevOps journey awaits. Let&apos;s crush some goals today!
                    </motion.p>
                </div>

                {/* Stats badges */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.5 }}
                    className="flex gap-4"
                >
                    {/* Level Badge */}
                    <div className={cn(
                        "flex items-center gap-3 px-5 py-4 rounded-2xl",
                        "bg-gradient-to-br from-purple-600/20 to-purple-500/10",
                        "border border-purple-500/30",
                        "shadow-[0_0_40px_rgba(139,92,246,0.25)]"
                    )}>
                        <div className={cn(
                            "w-12 h-12 rounded-xl",
                            "bg-gradient-to-br from-purple-500 to-purple-700",
                            "flex items-center justify-center",
                            "shadow-[0_0_25px_rgba(139,92,246,0.6)]"
                        )}>
                            <Zap className="w-6 h-6 text-white" />
                        </div>
                        <div>
                            <p className="text-zinc-500 text-xs uppercase tracking-wider">Level</p>
                            <p className="text-2xl font-bold text-purple-400">{level}</p>
                        </div>
                    </div>

                    {/* Streak Badge */}
                    <div className={cn(
                        "flex items-center gap-3 px-5 py-4 rounded-2xl",
                        "bg-gradient-to-br from-orange-600/20 to-orange-500/10",
                        "border border-orange-500/30",
                        "shadow-[0_0_40px_rgba(249,115,22,0.2)]"
                    )}>
                        <div className={cn(
                            "w-12 h-12 rounded-xl",
                            "bg-gradient-to-br from-orange-500 to-red-600",
                            "flex items-center justify-center",
                            "shadow-[0_0_25px_rgba(249,115,22,0.5)]"
                        )}>
                            <Flame className="w-6 h-6 text-white" />
                        </div>
                        <div>
                            <p className="text-zinc-500 text-xs uppercase tracking-wider">Streak</p>
                            <p className="text-2xl font-bold text-orange-400">{streak} days</p>
                        </div>
                    </div>
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   PREMIUM STAT CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    subtext?: string
    color: "purple" | "emerald" | "amber" | "orange" | "blue"
    delay?: number
}

function PremiumStatCard({ icon, label, value, subtext, color, delay = 0 }: StatCardProps) {
    const colorMap = {
        purple: {
            bg: "from-purple-600/20 to-purple-500/5",
            border: "border-purple-500/30",
            glow: "shadow-[0_0_30px_rgba(139,92,246,0.15)]",
            text: "text-purple-400",
            iconBg: "from-purple-500 to-purple-700",
        },
        emerald: {
            bg: "from-emerald-600/20 to-emerald-500/5",
            border: "border-emerald-500/30",
            glow: "shadow-[0_0_30px_rgba(16,185,129,0.15)]",
            text: "text-emerald-400",
            iconBg: "from-emerald-500 to-teal-600",
        },
        amber: {
            bg: "from-amber-600/20 to-amber-500/5",
            border: "border-amber-500/30",
            glow: "shadow-[0_0_30px_rgba(245,158,11,0.15)]",
            text: "text-amber-400",
            iconBg: "from-amber-500 to-orange-600",
        },
        orange: {
            bg: "from-orange-600/20 to-orange-500/5",
            border: "border-orange-500/30",
            glow: "shadow-[0_0_30px_rgba(249,115,22,0.15)]",
            text: "text-orange-400",
            iconBg: "from-orange-500 to-red-600",
        },
        blue: {
            bg: "from-blue-600/20 to-blue-500/5",
            border: "border-blue-500/30",
            glow: "shadow-[0_0_30px_rgba(59,130,246,0.15)]",
            text: "text-blue-400",
            iconBg: "from-blue-500 to-indigo-600",
        },
    }

    const styles = colorMap[color]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay }}
            whileHover={{ scale: 1.02, y: -4 }}
            className={cn(
                "relative p-5 rounded-2xl",
                "bg-gradient-to-br",
                styles.bg,
                "border",
                styles.border,
                styles.glow,
                "transition-all duration-300"
            )}
        >
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-zinc-500 text-sm font-medium mb-1">{label}</p>
                    <p className={cn("text-3xl font-bold", styles.text)}>{value}</p>
                    {subtext && <p className="text-zinc-600 text-xs mt-1">{subtext}</p>}
                </div>
                <div className={cn(
                    "w-11 h-11 rounded-xl",
                    "bg-gradient-to-br",
                    styles.iconBg,
                    "flex items-center justify-center",
                    "shadow-lg"
                )}>
                    {icon}
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   QUICK ACTION CARD
   ============================================================================ */

interface QuickActionProps {
    icon: React.ReactNode
    title: string
    description: string
    href: string
    color: "purple" | "emerald" | "amber"
    delay?: number
}

function QuickActionCard({ icon, title, description, href, color, delay = 0 }: QuickActionProps) {
    const colorMap = {
        purple: {
            bg: "hover:from-purple-600/20 hover:to-purple-500/10",
            border: "hover:border-purple-500/40",
            glow: "hover:shadow-[0_0_40px_rgba(139,92,246,0.2)]",
            iconBg: "from-purple-500 to-purple-700",
        },
        emerald: {
            bg: "hover:from-emerald-600/20 hover:to-emerald-500/10",
            border: "hover:border-emerald-500/40",
            glow: "hover:shadow-[0_0_40px_rgba(16,185,129,0.2)]",
            iconBg: "from-emerald-500 to-teal-600",
        },
        amber: {
            bg: "hover:from-amber-600/20 hover:to-amber-500/10",
            border: "hover:border-amber-500/40",
            glow: "hover:shadow-[0_0_40px_rgba(245,158,11,0.2)]",
            iconBg: "from-amber-500 to-orange-600",
        },
    }

    const styles = colorMap[color]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay }}
        >
            <Link href={href} prefetch={false}>
                <div className={cn(
                    "group relative p-6 rounded-2xl",
                    "bg-gradient-to-br from-zinc-900/80 to-zinc-800/50",
                    "border border-zinc-800",
                    styles.bg,
                    styles.border,
                    styles.glow,
                    "transition-all duration-300 cursor-pointer"
                )}>
                    <div className="flex items-start gap-4">
                        <div className={cn(
                            "w-12 h-12 rounded-xl shrink-0",
                            "bg-gradient-to-br",
                            styles.iconBg,
                            "flex items-center justify-center",
                            "shadow-lg group-hover:scale-110 transition-transform duration-300"
                        )}>
                            {icon}
                        </div>
                        <div className="flex-1">
                            <h3 className="text-lg font-semibold text-white mb-1 group-hover:text-purple-300 transition-colors">
                                {title}
                            </h3>
                            <p className="text-zinc-500 text-sm">{description}</p>
                        </div>
                        <ChevronRight className="w-5 h-5 text-zinc-600 group-hover:text-purple-400 group-hover:translate-x-1 transition-all" />
                    </div>
                </div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   XP PROGRESS RING
   ============================================================================ */

function XPProgressRing({ currentXP, xpToNextLevel, level }: { currentXP: number; xpToNextLevel: number; level: number }) {
    const progress = (currentXP / xpToNextLevel) * 100
    const circumference = 2 * Math.PI * 45

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.6 }}
            className={cn(
                "relative p-6 rounded-2xl",
                "bg-gradient-to-br from-amber-600/15 to-amber-500/5",
                "border border-amber-500/30",
                "shadow-[0_0_40px_rgba(245,158,11,0.15)]"
            )}
        >
            <h3 className="text-zinc-400 font-medium mb-4 flex items-center gap-2">
                <Trophy className="w-4 h-4 text-amber-400" />
                XP Progress
            </h3>

            <div className="flex items-center justify-center">
                <div className="relative">
                    <svg width="120" height="120" className="transform -rotate-90">
                        {/* Background circle */}
                        <circle
                            cx="60"
                            cy="60"
                            r="45"
                            stroke="currentColor"
                            strokeWidth="8"
                            fill="none"
                            className="text-zinc-800"
                        />
                        {/* Progress circle */}
                        <circle
                            cx="60"
                            cy="60"
                            r="45"
                            stroke="url(#xpGradient)"
                            strokeWidth="8"
                            fill="none"
                            strokeLinecap="round"
                            strokeDasharray={circumference}
                            strokeDashoffset={circumference - (progress / 100) * circumference}
                            className="transition-all duration-1000"
                        />
                        <defs>
                            <linearGradient id="xpGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stopColor="#F59E0B" />
                                <stop offset="100%" stopColor="#EF4444" />
                            </linearGradient>
                        </defs>
                    </svg>

                    {/* Center content */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center">
                        <span className="text-2xl font-bold text-amber-400">{currentXP}</span>
                        <span className="text-xs text-zinc-500">/ {xpToNextLevel} XP</span>
                    </div>
                </div>
            </div>

            <p className="text-center text-zinc-500 text-sm mt-4">
                {xpToNextLevel - currentXP} XP to Level {level + 1}
            </p>
        </motion.div>
    )
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function DashboardSkeleton() {
    return (
        <div className="space-y-8 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {Array.from({ length: 4 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-zinc-800/50" />
                ))}
            </div>
            <div className="grid lg:grid-cols-3 gap-6">
                <div className="lg:col-span-2 h-64 rounded-2xl bg-zinc-800/50" />
                <div className="h-64 rounded-2xl bg-zinc-800/50" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function DashboardError({ onRetry, error }: { onRetry: () => void; error: string }) {
    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className={cn(
                "max-w-md mx-auto text-center p-8 rounded-2xl",
                "bg-gradient-to-br from-red-600/10 to-red-500/5",
                "border border-red-500/30"
            )}
        >
            <div className="w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-red-500 to-red-700 flex items-center justify-center">
                <span className="text-4xl">😔</span>
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Unable to load dashboard</h3>
            <p className="text-zinc-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl bg-red-600 hover:bg-red-700">
                <RefreshCw className="h-4 w-4 mr-2" />
                Try Again
            </Button>
        </motion.div>
    )
}

/* ============================================================================
   MAIN DASHBOARD PAGE
   ============================================================================ */

export default function DashboardPage() {
    const { user } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchDashboard = useCallback(
        async (isRefresh = false) => {
            if (!isRefresh) setLoading(true)
            const result = await getDashboardSummary(user?.id)
            if (result.ok) {
                setDashboard(result.data)
                setError(null)
            } else {
                setError(result.message)
            }
            setLoading(false)
        },
        [user?.id]
    )

    useEffect(() => {
        fetchDashboard()
    }, [fetchDashboard])

    const handleRefresh = () => fetchDashboard(true)

    // Calculate stats
    const totalXP = dashboard?.stats?.total_progress_records ?? 0
    const levelInfo = calculateLevel(totalXP * 25)
    const completedModules = dashboard?.progress?.filter((p) => p.module_id && p.status === "completed").length ?? 0
    const totalModules = dashboard?.stats?.total_modules ?? 0
    const totalTasks = dashboard?.stats?.total_tasks ?? 0
    const completedTasks = dashboard?.progress?.filter((p) => p.status === "completed").length ?? 0
    const streak = 0

    const userName = user?.full_name?.split(" ")[0] || user?.email?.split("@")[0] || "DevOps Pro"

    return (
        <PageLayout maxWidth="wide" background="gray">
            {loading ? (
                <DashboardSkeleton />
            ) : error && !dashboard ? (
                <DashboardError error={error} onRetry={handleRefresh} />
            ) : (
                <div className="space-y-8">
                    {/* Premium Hero */}
                    <PremiumHero
                        userName={userName}
                        level={levelInfo.level}
                        streak={streak}
                    />

                    {/* Stats Grid */}
                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                        <PremiumStatCard
                            icon={<Zap className="w-5 h-5 text-white" />}
                            label="Total XP"
                            value={levelInfo.level * 100 + levelInfo.currentXP}
                            subtext="Keep earning!"
                            color="amber"
                            delay={0.1}
                        />
                        <PremiumStatCard
                            icon={<Target className="w-5 h-5 text-white" />}
                            label="Tasks Done"
                            value={completedTasks}
                            subtext={`of ${totalTasks} tasks`}
                            color="emerald"
                            delay={0.2}
                        />
                        <PremiumStatCard
                            icon={<BookOpen className="w-5 h-5 text-white" />}
                            label="Modules"
                            value={completedModules}
                            subtext={`of ${totalModules} completed`}
                            color="purple"
                            delay={0.3}
                        />
                        <PremiumStatCard
                            icon={<Flame className="w-5 h-5 text-white" />}
                            label="Streak"
                            value={`${streak} days`}
                            subtext="Don't break it!"
                            color="orange"
                            delay={0.4}
                        />
                    </div>

                    {/* Quick Actions + XP Progress */}
                    <div className="grid lg:grid-cols-3 gap-6">
                        {/* Quick Actions */}
                        <div className="lg:col-span-2 space-y-4">
                            <h2 className="text-xl font-bold text-white flex items-center gap-2">
                                <Play className="w-5 h-5 text-purple-400" />
                                Quick Actions
                            </h2>
                            <div className="grid md:grid-cols-2 gap-4">
                                <QuickActionCard
                                    icon={<BookOpen className="w-5 h-5 text-white" />}
                                    title="Continue Learning"
                                    description="Jump back into your modules"
                                    href="/modules"
                                    color="purple"
                                    delay={0.5}
                                />
                                <QuickActionCard
                                    icon={<Clock className="w-5 h-5 text-white" />}
                                    title="Study Session"
                                    description="Start a focused learning session"
                                    href="/studyflow"
                                    color="emerald"
                                    delay={0.6}
                                />
                                <QuickActionCard
                                    icon={<TrendingUp className="w-5 h-5 text-white" />}
                                    title="View Progress"
                                    description="Track your learning journey"
                                    href="/progress"
                                    color="amber"
                                    delay={0.7}
                                />
                                <QuickActionCard
                                    icon={<Target className="w-5 h-5 text-white" />}
                                    title="Skillpath Board"
                                    description="Plan your DevOps career path"
                                    href="/skillpath-board"
                                    color="purple"
                                    delay={0.8}
                                />
                            </div>
                        </div>

                        {/* XP Progress */}
                        <XPProgressRing
                            currentXP={levelInfo.currentXP}
                            xpToNextLevel={levelInfo.xpToNextLevel}
                            level={levelInfo.level}
                        />
                    </div>
                </div>
            )}
        </PageLayout>
    )
}
