"use client"

/**
 * ============================================================================
 * DASHBOARD PAGE — Design System v2.0
 * ============================================================================
 *
 * Updated with @saas/ui design system components:
 * - PageLayout for consistent centering and spacing
 * - Headline for typography
 * - Section/Block for content organization
 *
 * @phase DS.2 - Design System Application Layer
 */

import { useEffect, useState, useCallback } from "react"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { getDashboardSummary, DashboardSummary } from "@/lib/dashboard"

// @saas/ui Design System
import { PageLayout, Section, Block, Headline, Subtext } from "@saas/ui"

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
import { RefreshCw } from "lucide-react"

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
        xpToNextLevel: totalXPForLevel,
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
            <div
                className={cn(
                    "w-20 h-20 mx-auto mb-6 rounded-3xl flex items-center justify-center",
                    "bg-gradient-to-br from-red-100 to-red-50",
                    "dark:from-red-900/30 dark:to-red-800/20"
                )}
            >
                <span className="text-4xl">😔</span>
            </div>
            <h3 className="text-xl font-semibold text-neutral-900 dark:text-white mb-2">
                Unable to load dashboard
            </h3>
            <p className="text-neutral-500 dark:text-neutral-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl">
                <RefreshCw className="h-4 w-4 mr-2" />
                Try Again
            </Button>
        </GlassCard>
    )
}

/* ============================================================================
   DASHBOARD CONTENT
   ============================================================================ */

export default function DashboardPage() {
    const { user } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const fetchDashboard = useCallback(
        async (isRefresh = false) => {
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
        },
        [user?.id]
    )

    useEffect(() => {
        fetchDashboard()
    }, [fetchDashboard])

    const handleRefresh = () => fetchDashboard(true)

    // Calculate user stats from dashboard data
    const totalXP = dashboard?.stats?.total_progress_records ?? 0
    const levelInfo = calculateLevel(totalXP * 25) // Multiply for demo purposes
    const completedModules =
        dashboard?.progress?.filter((p) => p.module_id && p.status === "completed").length ?? 0
    const totalModules = dashboard?.stats?.total_modules ?? 0
    const streak = 0 // Will be fetched from user progress later

    // Transform modules for ModulesOverview
    const modulesWithProgress =
        dashboard?.modules?.map((m) => ({
            id: m.id,
            name: m.name,
            description: m.description ?? undefined,
            tasksCompleted:
                dashboard?.progress?.filter((p) => p.module_id === m.id && p.status === "completed")
                    .length ?? 0,
            totalTasks: 5, // Default tasks per module
            status: m.is_active ? ("in_progress" as const) : ("not_started" as const),
        })) ?? []

    // Real activities from backend (empty for new users)
    const recentActivities: Activity[] = []

    return (
        <PageLayout maxWidth="wide" background="gray">
            {loading ? (
                <DashboardSkeleton />
            ) : error && !dashboard ? (
                <DashboardError error={error} onRetry={handleRefresh} />
            ) : (
                <div className="space-y-8">
                    {/* Hero Section */}
                    <Section spacing="none">
                        <DashboardHero
                            userName={user?.full_name?.split(" ")[0] || user?.email?.split("@")[0]}
                            streak={streak}
                            level={levelInfo.level}
                            modulesCompleted={completedModules}
                            totalModules={totalModules}
                        />
                    </Section>

                    {/* Stats Row */}
                    <Section spacing="none">
                        <StatsRow
                            level={levelInfo.level}
                            currentXP={levelInfo.currentXP}
                            xpToNextLevel={levelInfo.xpToNextLevel}
                            streak={streak}
                            modulesCompleted={completedModules}
                            totalModules={totalModules}
                            totalXP={levelInfo.level * 100 + levelInfo.currentXP}
                        />
                    </Section>

                    {/* Quick Actions */}
                    <Section spacing="none">
                        <QuickActions
                            hasActiveStudyflow={false}
                            currentModule={
                                modulesWithProgress.find((m) => m.status === "in_progress")
                                    ? {
                                        id: modulesWithProgress[0]?.id ?? "",
                                        name: modulesWithProgress[0]?.name ?? "",
                                        progress: Math.round(
                                            ((modulesWithProgress[0]?.tasksCompleted ?? 0) /
                                                (modulesWithProgress[0]?.totalTasks ?? 1)) *
                                            100
                                        ),
                                    }
                                    : undefined
                            }
                        />
                    </Section>

                    {/* Main Content Grid */}
                    <Section spacing="none">
                        <div className="grid lg:grid-cols-3 gap-6">
                            {/* Modules Overview - 2 columns */}
                            <div className="lg:col-span-2">
                                <ModulesOverview modules={modulesWithProgress} />
                            </div>

                            {/* Right Sidebar - 1 column */}
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
                    </Section>
                </div>
            )}
        </PageLayout>
    )
}
