"use client"

/**
 * ============================================================================
 * DASHBOARD PAGE - Apple-Inspired Design (D.2)
 * ============================================================================
 * 
 * Design Philosophy:
 * - Inspired by Apple Fitness+, Notion, and Linear
 * - Clean, minimal, premium aesthetic
 * - Glassmorphism with subtle depth
 * - Staggered animations for visual delight
 * 
 * Features:
 * - Time-aware hero greeting
 * - Stats row with animated counters
 * - XP progress ring (Apple Watch style)
 * - Modules overview grid
 * - Recent activity timeline
 * - Quick actions panel
 * 
 * @phase D.2 - Dashboard UI Complete
 */

import { useEffect, useState, useCallback } from "react"
import { Protected, useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import {
    getDashboardSummary,
    DashboardSummary,
} from "@/lib/dashboard"

// D.2 Dashboard Components
import { DashboardHero } from "@/components/dashboard/DashboardHero"
import { StatsRow } from "@/components/dashboard/StatsRow"
import { XPProgress } from "@/components/dashboard/XPProgress"
import { ModulesOverview } from "@/components/dashboard/ModulesOverview"
import { RecentActivity, Activity } from "@/components/dashboard/RecentActivity"
import { QuickActions } from "@/components/dashboard/QuickActions"

// UI Components
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { RefreshCw, Settings, Bell, LogOut } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface DashboardUser {
    id: string
    email: string
    full_name?: string
    is_admin?: boolean
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function calculateLevel(xp: number): { level: number; currentXP: number; xpToNextLevel: number } {
    // Simple leveling formula: 100 XP per level, scaling by 1.5x each level
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
        xpToNextLevel: totalXPForLevel
    }
}

/* ============================================================================
   SKELETON COMPONENTS
   ============================================================================ */

function DashboardSkeleton() {
    return (
        <div className="space-y-8 animate-pulse">
            {/* Hero skeleton */}
            <div className="h-32 rounded-3xl bg-neutral-200 dark:bg-neutral-800" />
            
            {/* Stats row skeleton */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {Array.from({ length: 4 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-neutral-200 dark:bg-neutral-800" />
                ))}
            </div>

            {/* Main content skeleton */}
            <div className="grid lg:grid-cols-3 gap-6">
                <div className="lg:col-span-2 h-96 rounded-2xl bg-neutral-200 dark:bg-neutral-800" />
                <div className="h-96 rounded-2xl bg-neutral-200 dark:bg-neutral-800" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function DashboardError({ onRetry, error }: { onRetry: () => void; error: string }) {
    return (
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className="max-w-md mx-auto text-center animate-fade-in"
        >
            <div className={cn(
                "w-20 h-20 mx-auto mb-6 rounded-3xl flex items-center justify-center",
                "bg-gradient-to-br from-red-100 to-red-50",
                "dark:from-red-900/30 dark:to-red-800/20"
            )}>
                <span className="text-4xl">😔</span>
            </div>
            <h3 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Unable to load dashboard
            </h3>
            <p className="text-neutral-500 dark:text-neutral-400 mb-6">
                {error}
            </p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="h-4 w-4 mr-2" />
                Try Again
            </Button>
        </GlassCard>
    )
}

/* ============================================================================
   NAVIGATION BAR
   ============================================================================ */

interface NavBarProps {
    user: DashboardUser | null
    onLogout: () => void
    onRefresh: () => void
    isRefreshing: boolean
}

function NavBar({ user, onLogout, onRefresh, isRefreshing }: NavBarProps) {
    return (
        <nav className={cn(
            "sticky top-0 z-50 backdrop-blur-xl",
            "bg-white/70 dark:bg-neutral-900/70",
            "border-b border-neutral-200/50 dark:border-neutral-800/50"
        )}>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    {/* Logo & Brand */}
                    <div className="flex items-center gap-3">
                        <div className={cn(
                            "w-9 h-9 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-br from-primary-500 to-primary-600",
                            "shadow-lg shadow-primary-500/25"
                        )}>
                            <span className="text-white text-lg font-bold">D</span>
                        </div>
                        <span className="text-lg font-semibold text-neutral-900 dark:text-white">
                            DevOpsHub
                        </span>
                    </div>

                    {/* Right side actions */}
                    <div className="flex items-center gap-2">
                        {/* Refresh button */}
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={onRefresh}
                            disabled={isRefreshing}
                            className="rounded-xl"
                        >
                            <RefreshCw className={cn(
                                "h-4 w-4",
                                isRefreshing && "animate-spin"
                            )} />
                        </Button>

                        {/* Notifications */}
                        <Button variant="ghost" size="sm" className="rounded-xl relative">
                            <Bell className="h-4 w-4" />
                            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full" />
                        </Button>

                        {/* Settings */}
                        <Button variant="ghost" size="sm" className="rounded-xl">
                            <Settings className="h-4 w-4" />
                        </Button>

                        {/* User menu */}
                        <div className="flex items-center gap-2 ml-2 pl-2 border-l border-neutral-200 dark:border-neutral-700">
                            <div className={cn(
                                "w-8 h-8 rounded-full flex items-center justify-center",
                                "bg-gradient-to-br from-primary-400 to-primary-600",
                                "text-white text-sm font-medium"
                            )}>
                                {user?.full_name?.[0] || user?.email?.[0] || "?"}
                            </div>
                            <Button
                                variant="ghost"
                                size="sm"
                                onClick={onLogout}
                                className="rounded-xl text-neutral-500 hover:text-red-600"
                            >
                                <LogOut className="h-4 w-4" />
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
}

/* ============================================================================
   DASHBOARD CONTENT
   ============================================================================ */

function DashboardContent() {
    const { user, logout } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const fetchDashboard = useCallback(async (isRefresh = false) => {
        if (isRefresh) {
            setRefreshing(true)
        } else {
            setLoading(true)
        }

        const result = await getDashboardSummary(user?.id)

        if (result.ok) {
            setDashboard(result.data)
            setError(null)
        } else {
            setError(result.message)
        }

        setLoading(false)
        setRefreshing(false)
    }, [user?.id])

    useEffect(() => {
        fetchDashboard()
    }, [fetchDashboard])

    const handleRefresh = () => fetchDashboard(true)

    // Calculate user stats from dashboard data
    const totalXP = dashboard?.stats?.total_progress_records ?? 0
    const levelInfo = calculateLevel(totalXP * 25) // Multiply for demo purposes
    const completedModules = dashboard?.progress?.filter(p => p.module_id && p.status === "completed").length ?? 0
    const totalModules = dashboard?.stats?.total_modules ?? 0
    const streak = 3 // Demo streak - would come from backend

    // Transform modules for ModulesOverview
    const modulesWithProgress = dashboard?.modules?.map(m => ({
        id: m.id,
        name: m.name,
        description: m.description ?? undefined,
        tasksCompleted: dashboard?.progress?.filter(p => p.module_id === m.id && p.status === "completed").length ?? 0,
        totalTasks: 5, // Default tasks per module
        status: m.is_active ? "in_progress" as const : "not_started" as const
    })) ?? []

    // Demo activities - would come from backend
    const recentActivities: Activity[] = [
        {
            id: "1",
            type: "task_completed",
            title: "Completed 'Install VS Code'",
            description: "Linux Basics Module",
            xp: 25,
            timestamp: new Date(Date.now() - 15 * 60 * 1000)
        },
        {
            id: "2",
            type: "streak_milestone",
            title: "3-day streak achieved! 🔥",
            description: "Keep it up!",
            xp: 50,
            timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000)
        },
        {
            id: "3",
            type: "xp_earned",
            title: "Earned bonus XP",
            description: "First task of the day",
            xp: 15,
            timestamp: new Date(Date.now() - 24 * 60 * 60 * 1000)
        }
    ]

    return (
        <div className={cn(
            "min-h-screen",
            "bg-gradient-to-br from-neutral-50 via-neutral-100 to-neutral-50",
            "dark:from-neutral-900 dark:via-neutral-950 dark:to-neutral-900"
        )}>
            {/* Navigation */}
            <NavBar
                user={user as DashboardUser}
                onLogout={logout}
                onRefresh={handleRefresh}
                isRefreshing={refreshing}
            />

            {/* Main Content */}
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {loading ? (
                    <DashboardSkeleton />
                ) : error && !dashboard ? (
                    <DashboardError error={error} onRetry={handleRefresh} />
                ) : (
                    <div className="space-y-8">
                        {/* Hero Section */}
                        <DashboardHero
                            userName={user?.full_name || user?.email?.split("@")[0]}
                            streak={streak}
                            level={levelInfo.level}
                            modulesCompleted={completedModules}
                            totalModules={totalModules}
                        />

                        {/* Stats Row */}
                        <StatsRow
                            level={levelInfo.level}
                            currentXP={levelInfo.currentXP}
                            xpToNextLevel={levelInfo.xpToNextLevel}
                            streak={streak}
                            modulesCompleted={completedModules}
                            totalModules={totalModules}
                            totalXP={levelInfo.level * 100 + levelInfo.currentXP}
                        />

                        {/* Quick Actions */}
                        <QuickActions
                            hasActiveStudyflow={false}
                            currentModule={modulesWithProgress.find(m => m.status === "in_progress") ? {
                                id: modulesWithProgress[0]?.id ?? "",
                                name: modulesWithProgress[0]?.name ?? "",
                                progress: Math.round((modulesWithProgress[0]?.tasksCompleted ?? 0) / (modulesWithProgress[0]?.totalTasks ?? 1) * 100)
                            } : undefined}
                        />

                        {/* Main Content Grid */}
                        <div className="grid lg:grid-cols-3 gap-6">
                            {/* Modules Overview - 2 columns */}
                            <div className="lg:col-span-2">
                                <ModulesOverview modules={modulesWithProgress} />
                            </div>

                            {/* Sidebar - 1 column */}
                            <div className="space-y-6">
                                {/* XP Progress Ring */}
                                <XPProgress
                                    currentXP={levelInfo.currentXP}
                                    xpToNextLevel={levelInfo.xpToNextLevel}
                                    level={levelInfo.level}
                                />

                                {/* Recent Activity */}
                                <RecentActivity activities={recentActivities} />
                            </div>
                        </div>
                    </div>
                )}
            </main>
        </div>
    )
}

/* ============================================================================
   EXPORT
   ============================================================================ */

export default function DashboardPage() {
    return (
        <Protected>
            <DashboardContent />
        </Protected>
    )
}
