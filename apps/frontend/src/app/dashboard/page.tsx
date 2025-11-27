"use client"

/**
 * Dashboard Page
 * Phase 6.2: Refactored with dedicated components
 */

import { useEffect, useState, useCallback } from "react"
import Link from "next/link"
import { Protected, useAuth } from "@/components/auth"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { ProgressBar } from "@/components/ui/progress-bar"
import {
    getDashboardSummary,
    DashboardSummary,
    DashboardModule,
    DashboardTask,
    DashboardStudyflow,
    DashboardProgress,
} from "@/lib/dashboard"

// Phase 6.2 Components
import {
    DashboardHeader,
    ProgressOverview,
    DailyActivity,
    ModulesPreview,
    RecommendationsPanel,
} from "@/components/dashboard"

// ============================================================================
// DESIGN TOKENS (Consistent styling)
// ============================================================================

const cardStyles = "rounded-xl border border-gray-100 bg-white shadow-sm hover:shadow-md transition-shadow duration-200"
const sectionHeadingStyles = "text-xs font-semibold text-gray-400 uppercase tracking-widest mb-4 flex items-center gap-2"
const listItemStyles = "flex items-center justify-between px-3 py-2.5 rounded-lg bg-gray-50/80 hover:bg-gray-100 transition-all duration-150 cursor-pointer group"
const linkStyles = "text-sm font-medium text-gray-900 group-hover:text-blue-600 transition-colors"

// ============================================================================
// SECTION DIVIDER
// ============================================================================

function SectionDivider() {
    return <div className="h-px bg-gradient-to-r from-transparent via-gray-200 to-transparent my-10" />
}

// ============================================================================
// SKELETON COMPONENTS
// ============================================================================

function Skeleton({ className = "" }: { className?: string }) {
    return <div className={`animate-pulse bg-gray-200/80 rounded ${className}`} />
}

function StatCardSkeleton() {
    return (
        <div className={cardStyles}>
            <div className="p-5">
                <Skeleton className="h-3 w-20 mb-3" />
                <Skeleton className="h-9 w-14 mb-2" />
                <Skeleton className="h-2.5 w-16" />
            </div>
        </div>
    )
}

function PanelSkeleton({ lines = 3 }: { lines?: number }) {
    return (
        <div className={cardStyles}>
            <div className="p-5 border-b border-gray-50">
                <div className="flex items-center justify-between mb-1">
                    <Skeleton className="h-5 w-24" />
                    <Skeleton className="h-5 w-8 rounded-full" />
                </div>
                <Skeleton className="h-3.5 w-36" />
            </div>
            <div className="p-5">
                <div className="space-y-2.5">
                    {Array.from({ length: lines }).map((_, i) => (
                        <div key={i} className="flex items-center justify-between px-3 py-2.5 rounded-lg bg-gray-50/80">
                            <Skeleton className="h-4 w-28" />
                            <Skeleton className="h-5 w-14 rounded-full" />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

function ProgressPanelSkeleton() {
    return (
        <div className={cardStyles}>
            <div className="p-5 border-b border-gray-50">
                <div className="flex items-center justify-between mb-1">
                    <Skeleton className="h-5 w-28" />
                    <Skeleton className="h-5 w-8 rounded-full" />
                </div>
                <Skeleton className="h-3.5 w-40" />
            </div>
            <div className="p-5">
                <div className="space-y-3">
                    {Array.from({ length: 3 }).map((_, i) => (
                        <div key={i} className="px-3 py-3 rounded-lg bg-gray-50/80">
                            <div className="flex items-center justify-between mb-2.5">
                                <Skeleton className="h-4 w-16" />
                                <Skeleton className="h-5 w-20 rounded-full" />
                            </div>
                            <Skeleton className="h-2 w-full rounded-full" />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

function SystemPanelSkeleton() {
    return (
        <div className={cardStyles}>
            <div className="p-5 border-b border-gray-50">
                <Skeleton className="h-5 w-24 mb-1" />
                <Skeleton className="h-3.5 w-32" />
            </div>
            <div className="p-5">
                <div className="grid grid-cols-2 gap-5">
                    {Array.from({ length: 4 }).map((_, i) => (
                        <div key={i}>
                            <Skeleton className="h-3 w-14 mb-1.5" />
                            <Skeleton className="h-4 w-20" />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// EMPTY STATE COMPONENTS
// ============================================================================

function EmptyState({ icon, title, description, action }: {
    icon: string
    title: string
    description: string
    action?: { label: string; href: string }
}) {
    return (
        <div className="flex flex-col items-center justify-center py-10 text-center">
            <div className="w-14 h-14 rounded-full bg-gray-100 flex items-center justify-center mb-4">
                <span className="text-2xl">{icon}</span>
            </div>
            <p className="text-sm font-semibold text-gray-900 mb-1">{title}</p>
            <p className="text-xs text-gray-500 mb-4 max-w-[200px]">{description}</p>
            {action && (
                <Link href={action.href}>
                    <Button variant="outline" size="sm" className="text-xs h-8 px-3 rounded-lg">
                        {action.label}
                    </Button>
                </Link>
            )}
        </div>
    )
}

// ============================================================================
// PANEL ERROR COMPONENT (Soft-fail)
// ============================================================================

function PanelError({ title, onRetry }: { title: string; onRetry?: () => void }) {
    return (
        <div className={`${cardStyles} border-red-100`}>
            <div className="py-10 px-5">
                <div className="flex flex-col items-center justify-center text-center">
                    <div className="w-12 h-12 rounded-full bg-red-50 flex items-center justify-center mb-3">
                        <span className="text-xl">⚠️</span>
                    </div>
                    <p className="text-sm font-semibold text-red-600 mb-1">Failed to load {title}</p>
                    <p className="text-xs text-gray-500 mb-4">Something went wrong. Try refreshing.</p>
                    {onRetry && (
                        <Button variant="outline" size="sm" onClick={onRetry} className="text-xs h-8 px-3 rounded-lg">
                            Retry
                        </Button>
                    )}
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// STAT CARD
// ============================================================================

function StatCard({ title, value, subtitle, icon }: { title: string; value: number | string; subtitle?: string; icon?: string }) {
    return (
        <div className={cardStyles}>
            <div className="p-5">
                <div className="flex items-start justify-between">
                    <div>
                        <p className="text-xs font-medium text-gray-500 uppercase tracking-wide mb-1">{title}</p>
                        <p className="text-3xl font-bold text-gray-900 tracking-tight">{value}</p>
                        {subtitle && (
                            <p className="text-xs text-gray-400 mt-1">{subtitle}</p>
                        )}
                    </div>
                    {icon && (
                        <div className="w-10 h-10 rounded-lg bg-gray-50 flex items-center justify-center">
                            <span className="text-lg">{icon}</span>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// MODULES PANEL
// ============================================================================

function ModulesPanel({ modules }: { modules: DashboardModule[] }) {
    return (
        <div className={cardStyles}>
            <div className="px-5 py-4 border-b border-gray-50">
                <div className="flex items-center justify-between">
                    <h4 className="text-base font-semibold text-gray-900">Modules</h4>
                    <Badge variant="secondary" className="text-xs font-medium">{modules.length}</Badge>
                </div>
                <p className="text-xs text-gray-500 mt-0.5">Learning modules overview</p>
            </div>
            <div className="p-4">
                {modules.length === 0 ? (
                    <EmptyState
                        icon="📚"
                        title="No modules yet"
                        description="Create your first learning module to get started."
                        action={{ label: "Create Module", href: "/modules/new" }}
                    />
                ) : (
                    <ul className="space-y-1.5">
                        {modules.slice(0, 5).map((m) => (
                            <li key={m.id}>
                                <Link href={`/modules/${m.id}`} className={listItemStyles}>
                                    <span className={linkStyles}>{m.name}</span>
                                    <Badge variant={m.is_active ? "success" : "inactive"} className="text-[10px] px-2 py-0.5">
                                        {m.is_active ? "Active" : "Inactive"}
                                    </Badge>
                                </Link>
                            </li>
                        ))}
                        {modules.length > 5 && (
                            <li className="pt-2">
                                <Link href="/modules" className="text-xs text-blue-600 hover:text-blue-700 font-medium flex items-center justify-center gap-1">
                                    View all {modules.length} modules
                                    <span>→</span>
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </div>
        </div>
    )
}

// ============================================================================
// TASKS PANEL
// ============================================================================

function TasksPanel({ tasks }: { tasks: DashboardTask[] }) {
    const difficultyStyles = (d: string) => {
        switch (d.toLowerCase()) {
            case "easy": return "bg-emerald-50 text-emerald-700 border-emerald-100"
            case "medium": return "bg-amber-50 text-amber-700 border-amber-100"
            case "hard": return "bg-rose-50 text-rose-700 border-rose-100"
            default: return "bg-gray-50 text-gray-600 border-gray-100"
        }
    }

    return (
        <div className={cardStyles}>
            <div className="px-5 py-4 border-b border-gray-50">
                <div className="flex items-center justify-between">
                    <h4 className="text-base font-semibold text-gray-900">Tasks</h4>
                    <Badge variant="secondary" className="text-xs font-medium">{tasks.length}</Badge>
                </div>
                <p className="text-xs text-gray-500 mt-0.5">Practice tasks overview</p>
            </div>
            <div className="p-4">
                {tasks.length === 0 ? (
                    <EmptyState
                        icon="✅"
                        title="No tasks yet"
                        description="Tasks will appear here once modules are created."
                        action={{ label: "Browse Modules", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-1.5">
                        {tasks.slice(0, 5).map((t) => (
                            <li key={t.id}>
                                <Link href={`/tasks/${t.id}`} className={listItemStyles}>
                                    <span className={linkStyles}>{t.title}</span>
                                    <span className={`text-[10px] font-medium px-2 py-0.5 rounded-full border ${difficultyStyles(t.difficulty)}`}>
                                        {t.difficulty}
                                    </span>
                                </Link>
                            </li>
                        ))}
                        {tasks.length > 5 && (
                            <li className="pt-2">
                                <Link href="/tasks" className="text-xs text-blue-600 hover:text-blue-700 font-medium flex items-center justify-center gap-1">
                                    View all {tasks.length} tasks
                                    <span>→</span>
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </div>
        </div>
    )
}

// ============================================================================
// STUDYFLOW PANEL
// ============================================================================

function StudyflowPanel({ studyflows }: { studyflows: DashboardStudyflow[] }) {
    return (
        <div className={cardStyles}>
            <div className="px-5 py-4 border-b border-gray-50">
                <div className="flex items-center justify-between">
                    <h4 className="text-base font-semibold text-gray-900">Studyflows</h4>
                    <Badge variant="secondary" className="text-xs font-medium">{studyflows.length}</Badge>
                </div>
                <p className="text-xs text-gray-500 mt-0.5">Learning paths overview</p>
            </div>
            <div className="p-4">
                {studyflows.length === 0 ? (
                    <EmptyState
                        icon="🎯"
                        title="No studyflow steps"
                        description="Studyflows guide your learning path through modules."
                        action={{ label: "Browse Modules", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-1.5">
                        {studyflows.slice(0, 5).map((sf) => (
                            <li key={sf.id}>
                                <Link href={`/studyflow/${sf.id}`} className={listItemStyles}>
                                    <span className={linkStyles}>{sf.title}</span>
                                    <span className="text-[10px] font-medium text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
                                        Step {sf.order}
                                    </span>
                                </Link>
                            </li>
                        ))}
                        {studyflows.length > 5 && (
                            <li className="pt-2">
                                <Link href="/studyflow" className="text-xs text-blue-600 hover:text-blue-700 font-medium flex items-center justify-center gap-1">
                                    View all {studyflows.length} studyflows
                                    <span>→</span>
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </div>
        </div>
    )
}

// ============================================================================
// PROGRESS PANEL
// ============================================================================

function ProgressPanel({ progress }: { progress: DashboardProgress[] }) {
    const statusStyles = (s: string) => {
        switch (s) {
            case "completed": return "bg-emerald-50 text-emerald-700 border-emerald-100"
            case "in_progress": return "bg-amber-50 text-amber-700 border-amber-100"
            default: return "bg-gray-50 text-gray-600 border-gray-100"
        }
    }

    const statusLabel = (s: string) => {
        switch (s) {
            case "completed": return "Completed"
            case "in_progress": return "In Progress"
            default: return "Not Started"
        }
    }

    return (
        <div className={cardStyles}>
            <div className="px-5 py-4 border-b border-gray-50">
                <div className="flex items-center justify-between">
                    <h4 className="text-base font-semibold text-gray-900">Your Progress</h4>
                    <Badge variant="secondary" className="text-xs font-medium">{progress.length}</Badge>
                </div>
                <p className="text-xs text-gray-500 mt-0.5">Track your learning journey</p>
            </div>
            <div className="p-4">
                {progress.length === 0 ? (
                    <EmptyState
                        icon="📈"
                        title="No progress data"
                        description="Start learning to track your progress here!"
                        action={{ label: "Get Started", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-2.5">
                        {progress.slice(0, 5).map((p) => (
                            <li key={p.id} className="px-3 py-3 rounded-lg bg-gray-50/80">
                                <div className="flex items-center justify-between mb-2.5">
                                    <span className="text-xs font-semibold text-gray-700">
                                        {p.module_id ? "Module" : p.task_id ? "Task" : "Studyflow"}
                                    </span>
                                    <span className={`text-[10px] font-medium px-2 py-0.5 rounded-full border ${statusStyles(p.status)}`}>
                                        {statusLabel(p.status)}
                                    </span>
                                </div>
                                <ProgressBar value={p.progress} />
                            </li>
                        ))}
                        {progress.length > 5 && (
                            <li className="pt-1">
                                <Link href="/progress" className="text-xs text-blue-600 hover:text-blue-700 font-medium flex items-center justify-center gap-1">
                                    View all {progress.length} progress records
                                    <span>→</span>
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </div>
        </div>
    )
}

// ============================================================================
// SYSTEM INFO PANEL
// ============================================================================

function SystemInfoPanel({ system, version }: { system: DashboardSummary["system"]; version: DashboardSummary["version"] }) {
    return (
        <div className={cardStyles}>
            <div className="px-5 py-4 border-b border-gray-50">
                <h4 className="text-base font-semibold text-gray-900">System Info</h4>
                <p className="text-xs text-gray-500 mt-0.5">Backend service status</p>
            </div>
            <div className="p-5">
                <div className="grid grid-cols-2 gap-5">
                    <div className="space-y-1">
                        <p className="text-[10px] font-medium text-gray-400 uppercase tracking-wider">Service</p>
                        <p className="text-sm font-semibold text-gray-900">{system.service}</p>
                    </div>
                    <div className="space-y-1">
                        <p className="text-[10px] font-medium text-gray-400 uppercase tracking-wider">Version</p>
                        <p className="text-sm font-semibold text-gray-900">{system.version}</p>
                    </div>
                    <div className="space-y-1">
                        <p className="text-[10px] font-medium text-gray-400 uppercase tracking-wider">Environment</p>
                        <p className="text-sm font-semibold text-gray-900 capitalize">{system.environment}</p>
                    </div>
                    <div className="space-y-1">
                        <p className="text-[10px] font-medium text-gray-400 uppercase tracking-wider">Phase</p>
                        <p className="text-sm font-semibold text-gray-900">{version.phase}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

// ============================================================================
// REFRESH CONTROLS
// ============================================================================

function RefreshControls({
    onRefresh,
    loading,
    autoRefreshEnabled,
    onToggleAutoRefresh,
    lastUpdated,
}: {
    onRefresh: () => void
    loading: boolean
    autoRefreshEnabled: boolean
    onToggleAutoRefresh: () => void
    lastUpdated: Date | null
}) {
    const formatLastUpdated = (date: Date | null) => {
        if (!date) return "Never"
        return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })
    }

    return (
        <div className="flex items-center gap-4">
            {/* Last Updated */}
            {lastUpdated && (
                <span className="text-xs text-gray-400">
                    Updated {formatLastUpdated(lastUpdated)}
                </span>
            )}

            {/* Auto-refresh Toggle */}
            <button
                onClick={onToggleAutoRefresh}
                className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${autoRefreshEnabled
                        ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
                        : "bg-gray-50 text-gray-500 border border-gray-200 hover:bg-gray-100"
                    }`}
            >
                <div className={`w-2 h-2 rounded-full ${autoRefreshEnabled ? "bg-emerald-500 animate-pulse" : "bg-gray-400"}`} />
                Auto-refresh {autoRefreshEnabled ? "ON" : "OFF"}
            </button>

            {/* Manual Refresh Button */}
            <Button
                variant="outline"
                size="sm"
                onClick={onRefresh}
                disabled={loading}
                className="gap-2 h-9 px-4 rounded-lg text-xs font-medium shadow-sm hover:shadow transition-shadow"
            >
                <svg
                    className={`h-3.5 w-3.5 ${loading ? "animate-spin" : ""}`}
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                >
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                    />
                </svg>
                {loading ? "Refreshing..." : "Refresh"}
            </Button>
        </div>
    )
}

// ============================================================================
// DASHBOARD CONTENT
// ============================================================================

// Auto-refresh interval (60 seconds)
const AUTO_REFRESH_INTERVAL = 60000

function DashboardContent() {
    const { user, logout } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [autoRefreshEnabled, setAutoRefreshEnabled] = useState(false)
    const [lastUpdated, setLastUpdated] = useState<Date | null>(null)

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
            setLastUpdated(new Date())
        } else {
            setError(result.message)
        }

        setLoading(false)
        setRefreshing(false)
    }, [user?.id])

    // Initial fetch
    useEffect(() => {
        fetchDashboard()
    }, [fetchDashboard])

    // Auto-refresh effect
    useEffect(() => {
        if (!autoRefreshEnabled) return

        const intervalId = setInterval(() => {
            fetchDashboard(true)
        }, AUTO_REFRESH_INTERVAL)

        return () => clearInterval(intervalId)
    }, [autoRefreshEnabled, fetchDashboard])

    const handleRefresh = () => {
        fetchDashboard(true)
    }

    const toggleAutoRefresh = () => {
        setAutoRefreshEnabled(prev => !prev)
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100/50">
            {/* Navigation */}
            <nav className="bg-white/80 backdrop-blur-md border-b border-gray-100 sticky top-0 z-10">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex items-center space-x-8">
                            <h1 className="text-xl font-bold text-gray-900 tracking-tight">DevOpsHub</h1>
                            <div className="hidden md:flex items-center space-x-1">
                                {[
                                    { href: "/modules", label: "Modules" },
                                    { href: "/tasks", label: "Tasks" },
                                    { href: "/studyflow", label: "Studyflow" },
                                    { href: "/progress", label: "Progress" },
                                ].map((link) => (
                                    <Link
                                        key={link.href}
                                        href={link.href}
                                        className="text-sm font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-100 px-3 py-2 rounded-lg transition-all"
                                    >
                                        {link.label}
                                    </Link>
                                ))}
                            </div>
                        </div>
                        <div className="flex items-center space-x-3">
                            <div className="hidden sm:flex items-center space-x-2 px-3 py-1.5 bg-gray-50 rounded-lg">
                                <div className="w-2 h-2 rounded-full bg-emerald-500"></div>
                                <span className="text-xs font-medium text-gray-600">{user?.email}</span>
                            </div>
                            {user?.is_admin && (
                                <Badge variant="secondary" className="text-xs">Admin</Badge>
                            )}
                            <button
                                onClick={logout}
                                className="text-xs font-medium text-gray-500 hover:text-red-600 px-3 py-2 rounded-lg hover:bg-red-50 transition-all"
                            >
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            {/* Main Content */}
            <main className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
                {/* Phase 6.2: Dashboard Header Component */}
                <div className="mb-8">
                    <DashboardHeader
                        user={dashboard?.user ?? user}
                        currentXP={dashboard?.stats?.total_progress_records ?? 0}
                    />
                </div>

                {/* Refresh Controls Row */}
                <div className="flex justify-end mb-6">
                    <RefreshControls
                        onRefresh={handleRefresh}
                        loading={refreshing}
                        autoRefreshEnabled={autoRefreshEnabled}
                        onToggleAutoRefresh={toggleAutoRefresh}
                        lastUpdated={lastUpdated}
                    />
                </div>

                {/* Loading State: Skeletons */}
                {loading ? (
                    <>
                        {/* Stats Skeleton */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-blue-500 rounded-full"></span>
                                Overview
                            </div>
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                                {Array.from({ length: 4 }).map((_, i) => (
                                    <StatCardSkeleton key={i} />
                                ))}
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Main Panels Skeleton */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-purple-500 rounded-full"></span>
                                Content
                            </div>
                            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
                                <PanelSkeleton lines={4} />
                                <PanelSkeleton lines={4} />
                                <PanelSkeleton lines={4} />
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Bottom Section Skeleton */}
                        <section>
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-emerald-500 rounded-full"></span>
                                Status
                            </div>
                            <div className="grid md:grid-cols-2 gap-5">
                                <ProgressPanelSkeleton />
                                <SystemPanelSkeleton />
                            </div>
                        </section>
                    </>
                ) : error && !dashboard ? (
                    /* Full error state (only when no data at all) */
                    <div className={`${cardStyles} border-red-100 bg-red-50/50`}>
                        <div className="py-16 px-5">
                            <div className="flex flex-col items-center justify-center text-center">
                                <div className="w-16 h-16 rounded-full bg-red-100 flex items-center justify-center mb-4">
                                    <span className="text-3xl">😔</span>
                                </div>
                                <p className="text-lg font-semibold text-red-600 mb-2">Unable to load dashboard</p>
                                <p className="text-sm text-gray-500 mb-6 max-w-sm">{error}</p>
                                <Button onClick={handleRefresh} disabled={refreshing} className="rounded-lg">
                                    {refreshing ? "Retrying..." : "Try Again"}
                                </Button>
                            </div>
                        </div>
                    </div>
                ) : dashboard ? (
                    <>
                        {/* Stats Grid */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-blue-500 rounded-full"></span>
                                Overview
                            </div>
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                                <StatCard
                                    title="Total Modules"
                                    value={dashboard.stats.total_modules}
                                    subtitle={`${dashboard.stats.active_modules} active`}
                                    icon="📚"
                                />
                                <StatCard
                                    title="Total Tasks"
                                    value={dashboard.stats.total_tasks}
                                    subtitle={`${dashboard.stats.active_tasks} active`}
                                    icon="✅"
                                />
                                <StatCard
                                    title="Studyflows"
                                    value={dashboard.stats.total_studyflows}
                                    icon="🎯"
                                />
                                <StatCard
                                    title="Progress"
                                    value={dashboard.stats.total_progress_records}
                                    icon="📈"
                                />
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Phase 6.2: Enhanced Panels Grid */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-purple-500 rounded-full"></span>
                                Your Learning Journey
                            </div>
                            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
                                {/* Phase 6.2: ModulesPreview Component */}
                                <ModulesPreview
                                    modules={dashboard.modules}
                                    progress={dashboard.progress}
                                />
                                {/* Phase 6.2: ProgressOverview Component */}
                                <ProgressOverview
                                    stats={dashboard.stats}
                                    completedModules={dashboard.progress.filter(p => p.module_id && p.status === "completed").length}
                                    completedTasks={dashboard.progress.filter(p => p.task_id && p.status === "completed").length}
                                />
                                {/* Phase 6.2: DailyActivity Component */}
                                <DailyActivity
                                    studyflows={dashboard.studyflow}
                                    studyMinutesToday={0}
                                    tasksCompletedToday={0}
                                    currentStreak={0}
                                />
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Phase 6.2: AI Recommendations + System Info */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-indigo-500 rounded-full"></span>
                                Insights & Recommendations
                            </div>
                            <div className="grid md:grid-cols-2 gap-5">
                                {/* Phase 6.2: RecommendationsPanel Component */}
                                <RecommendationsPanel isEnabled={false} />
                                <SystemInfoPanel system={dashboard.system} version={dashboard.version} />
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Legacy Content Panels (keeping for backward compatibility) */}
                        <section className="mb-10">
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-gray-400 rounded-full"></span>
                                Detailed Content
                            </div>
                            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
                                <ModulesPanel modules={dashboard.modules} />
                                <TasksPanel tasks={dashboard.tasks} />
                                <StudyflowPanel studyflows={dashboard.studyflow} />
                            </div>
                        </section>

                        <SectionDivider />

                        {/* Bottom Section */}
                        <section>
                            <div className={sectionHeadingStyles}>
                                <span className="w-1 h-4 bg-emerald-500 rounded-full"></span>
                                Progress Tracking
                            </div>
                            <div className="grid md:grid-cols-2 gap-5">
                                <ProgressPanel progress={dashboard.progress} />
                            </div>
                        </section>
                    </>
                ) : null}
            </main>
        </div>
    )
}

// ============================================================================
// EXPORT
// ============================================================================

export default function DashboardPage() {
    return (
        <Protected>
            <DashboardContent />
        </Protected>
    )
}
