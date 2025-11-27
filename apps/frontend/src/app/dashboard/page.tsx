"use client"

/**
 * Dashboard Page
 * Phase 6.2: Enhanced Dashboard with Skeletons, Empty States, Soft-fail, Refresh
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

// ============================================================================
// SKELETON COMPONENTS
// ============================================================================

function Skeleton({ className = "" }: { className?: string }) {
    return <div className={`animate-pulse bg-gray-200 rounded ${className}`} />
}

function StatCardSkeleton() {
    return (
        <Card>
            <CardHeader className="pb-2">
                <Skeleton className="h-4 w-24 mb-2" />
                <Skeleton className="h-8 w-16" />
            </CardHeader>
            <CardContent>
                <Skeleton className="h-3 w-20" />
            </CardContent>
        </Card>
    )
}

function PanelSkeleton({ lines = 3 }: { lines?: number }) {
    return (
        <Card>
            <CardHeader>
                <div className="flex items-center justify-between">
                    <Skeleton className="h-5 w-24" />
                    <Skeleton className="h-5 w-8 rounded-full" />
                </div>
                <Skeleton className="h-4 w-40 mt-1" />
            </CardHeader>
            <CardContent>
                <div className="space-y-3">
                    {Array.from({ length: lines }).map((_, i) => (
                        <div key={i} className="flex items-center justify-between p-2 rounded-lg bg-muted/50">
                            <Skeleton className="h-4 w-32" />
                            <Skeleton className="h-5 w-16 rounded-full" />
                        </div>
                    ))}
                </div>
            </CardContent>
        </Card>
    )
}

function ProgressPanelSkeleton() {
    return (
        <Card>
            <CardHeader>
                <div className="flex items-center justify-between">
                    <Skeleton className="h-5 w-28" />
                    <Skeleton className="h-5 w-8 rounded-full" />
                </div>
                <Skeleton className="h-4 w-44 mt-1" />
            </CardHeader>
            <CardContent>
                <div className="space-y-3">
                    {Array.from({ length: 3 }).map((_, i) => (
                        <div key={i} className="p-3 rounded-lg bg-muted/50">
                            <div className="flex items-center justify-between mb-2">
                                <Skeleton className="h-4 w-20" />
                                <Skeleton className="h-5 w-20 rounded-full" />
                            </div>
                            <Skeleton className="h-2.5 w-full rounded-full" />
                        </div>
                    ))}
                </div>
            </CardContent>
        </Card>
    )
}

function SystemPanelSkeleton() {
    return (
        <Card>
            <CardHeader>
                <Skeleton className="h-5 w-24" />
                <Skeleton className="h-4 w-36 mt-1" />
            </CardHeader>
            <CardContent>
                <div className="grid grid-cols-2 gap-4">
                    {Array.from({ length: 4 }).map((_, i) => (
                        <div key={i}>
                            <Skeleton className="h-3 w-16 mb-1" />
                            <Skeleton className="h-4 w-24" />
                        </div>
                    ))}
                </div>
            </CardContent>
        </Card>
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
        <div className="flex flex-col items-center justify-center py-8 text-center">
            <span className="text-4xl mb-3">{icon}</span>
            <p className="text-sm font-medium text-gray-900 mb-1">{title}</p>
            <p className="text-xs text-muted-foreground mb-3">{description}</p>
            {action && (
                <Link href={action.href}>
                    <Button variant="outline" size="sm">{action.label}</Button>
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
        <Card className="border-red-200">
            <CardContent className="py-8">
                <div className="flex flex-col items-center justify-center text-center">
                    <span className="text-3xl mb-2">⚠️</span>
                    <p className="text-sm font-medium text-red-600 mb-1">Failed to load {title}</p>
                    <p className="text-xs text-muted-foreground mb-3">Something went wrong. Try refreshing.</p>
                    {onRetry && (
                        <Button variant="outline" size="sm" onClick={onRetry}>
                            Retry
                        </Button>
                    )}
                </div>
            </CardContent>
        </Card>
    )
}

// ============================================================================
// STAT CARD
// ============================================================================

function StatCard({ title, value, subtitle }: { title: string; value: number | string; subtitle?: string }) {
    return (
        <Card>
            <CardHeader className="pb-2">
                <CardDescription>{title}</CardDescription>
                <CardTitle className="text-3xl">{value}</CardTitle>
            </CardHeader>
            {subtitle && (
                <CardContent>
                    <p className="text-xs text-muted-foreground">{subtitle}</p>
                </CardContent>
            )}
        </Card>
    )
}

// ============================================================================
// MODULES PANEL
// ============================================================================

function ModulesPanel({ modules }: { modules: DashboardModule[] }) {
    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center justify-between">
                    <span>Modules</span>
                    <Badge variant="secondary">{modules.length}</Badge>
                </CardTitle>
                <CardDescription>Learning modules overview</CardDescription>
            </CardHeader>
            <CardContent>
                {modules.length === 0 ? (
                    <EmptyState
                        icon="📚"
                        title="No modules yet"
                        description="Create your first learning module to get started."
                        action={{ label: "Create Module", href: "/modules/new" }}
                    />
                ) : (
                    <ul className="space-y-2">
                        {modules.slice(0, 5).map((m) => (
                            <li key={m.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50 hover:bg-muted transition-colors">
                                <Link href={`/modules/${m.id}`} className="text-sm font-medium hover:underline">
                                    {m.name}
                                </Link>
                                <Badge variant={m.is_active ? "success" : "inactive"}>
                                    {m.is_active ? "Active" : "Inactive"}
                                </Badge>
                            </li>
                        ))}
                        {modules.length > 5 && (
                            <li className="text-center pt-2">
                                <Link href="/modules" className="text-xs text-muted-foreground hover:underline">
                                    View all {modules.length} modules →
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

// ============================================================================
// TASKS PANEL
// ============================================================================

function TasksPanel({ tasks }: { tasks: DashboardTask[] }) {
    const difficultyColor = (d: string) => {
        switch (d.toLowerCase()) {
            case "easy": return "bg-green-100 text-green-800"
            case "medium": return "bg-yellow-100 text-yellow-800"
            case "hard": return "bg-red-100 text-red-800"
            default: return "bg-gray-100 text-gray-800"
        }
    }

    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center justify-between">
                    <span>Tasks</span>
                    <Badge variant="secondary">{tasks.length}</Badge>
                </CardTitle>
                <CardDescription>Practice tasks overview</CardDescription>
            </CardHeader>
            <CardContent>
                {tasks.length === 0 ? (
                    <EmptyState
                        icon="✅"
                        title="No tasks yet"
                        description="Tasks will appear here once modules are created."
                        action={{ label: "Browse Modules", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-2">
                        {tasks.slice(0, 5).map((t) => (
                            <li key={t.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50 hover:bg-muted transition-colors">
                                <Link href={`/tasks/${t.id}`} className="text-sm font-medium hover:underline">
                                    {t.title}
                                </Link>
                                <span className={`text-xs px-2 py-0.5 rounded-full ${difficultyColor(t.difficulty)}`}>
                                    {t.difficulty}
                                </span>
                            </li>
                        ))}
                        {tasks.length > 5 && (
                            <li className="text-center pt-2">
                                <Link href="/tasks" className="text-xs text-muted-foreground hover:underline">
                                    View all {tasks.length} tasks →
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

// ============================================================================
// STUDYFLOW PANEL
// ============================================================================

function StudyflowPanel({ studyflows }: { studyflows: DashboardStudyflow[] }) {
    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center justify-between">
                    <span>Studyflows</span>
                    <Badge variant="secondary">{studyflows.length}</Badge>
                </CardTitle>
                <CardDescription>Learning paths overview</CardDescription>
            </CardHeader>
            <CardContent>
                {studyflows.length === 0 ? (
                    <EmptyState
                        icon="🎯"
                        title="No studyflow steps"
                        description="Studyflows guide your learning path through modules."
                        action={{ label: "Browse Modules", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-2">
                        {studyflows.slice(0, 5).map((sf) => (
                            <li key={sf.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50 hover:bg-muted transition-colors">
                                <Link href={`/studyflow/${sf.id}`} className="text-sm font-medium hover:underline">
                                    {sf.title}
                                </Link>
                                <span className="text-xs text-muted-foreground">
                                    Step {sf.order}
                                </span>
                            </li>
                        ))}
                        {studyflows.length > 5 && (
                            <li className="text-center pt-2">
                                <Link href="/studyflow" className="text-xs text-muted-foreground hover:underline">
                                    View all {studyflows.length} studyflows →
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

// ============================================================================
// PROGRESS PANEL
// ============================================================================

function ProgressPanel({ progress }: { progress: DashboardProgress[] }) {
    const statusColor = (s: string) => {
        switch (s) {
            case "completed": return "bg-green-100 text-green-800"
            case "in_progress": return "bg-yellow-100 text-yellow-800"
            default: return "bg-gray-100 text-gray-800"
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
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center justify-between">
                    <span>Your Progress</span>
                    <Badge variant="secondary">{progress.length}</Badge>
                </CardTitle>
                <CardDescription>Track your learning journey</CardDescription>
            </CardHeader>
            <CardContent>
                {progress.length === 0 ? (
                    <EmptyState
                        icon="📈"
                        title="No progress data"
                        description="Start learning to track your progress here!"
                        action={{ label: "Get Started", href: "/modules" }}
                    />
                ) : (
                    <ul className="space-y-3">
                        {progress.slice(0, 5).map((p) => (
                            <li key={p.id} className="p-3 rounded-lg bg-muted/50">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-medium">
                                        {p.module_id ? "Module" : p.task_id ? "Task" : "Studyflow"}
                                    </span>
                                    <span className={`text-xs px-2 py-0.5 rounded-full ${statusColor(p.status)}`}>
                                        {statusLabel(p.status)}
                                    </span>
                                </div>
                                <ProgressBar value={p.progress} />
                            </li>
                        ))}
                        {progress.length > 5 && (
                            <li className="text-center pt-2">
                                <Link href="/progress" className="text-xs text-muted-foreground hover:underline">
                                    View all {progress.length} progress records →
                                </Link>
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

// ============================================================================
// SYSTEM INFO PANEL
// ============================================================================

function SystemInfoPanel({ system, version }: { system: DashboardSummary["system"]; version: DashboardSummary["version"] }) {
    return (
        <Card>
            <CardHeader>
                <CardTitle>System Info</CardTitle>
                <CardDescription>Backend service status</CardDescription>
            </CardHeader>
            <CardContent>
                <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                        <p className="text-muted-foreground">Service</p>
                        <p className="font-medium">{system.service}</p>
                    </div>
                    <div>
                        <p className="text-muted-foreground">Version</p>
                        <p className="font-medium">{system.version}</p>
                    </div>
                    <div>
                        <p className="text-muted-foreground">Environment</p>
                        <p className="font-medium capitalize">{system.environment}</p>
                    </div>
                    <div>
                        <p className="text-muted-foreground">Phase</p>
                        <p className="font-medium">{version.phase}</p>
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}

// ============================================================================
// REFRESH BUTTON
// ============================================================================

function RefreshButton({ onClick, loading }: { onClick: () => void; loading: boolean }) {
    return (
        <Button
            variant="outline"
            size="sm"
            onClick={onClick}
            disabled={loading}
            className="gap-2"
        >
            <svg
                className={`h-4 w-4 ${loading ? "animate-spin" : ""}`}
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
    )
}

// ============================================================================
// DASHBOARD CONTENT
// ============================================================================

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

    const handleRefresh = () => {
        fetchDashboard(true)
    }

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Navigation */}
            <nav className="bg-white shadow sticky top-0 z-10">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex items-center space-x-8">
                            <h1 className="text-xl font-bold text-gray-900">DevOpsHub</h1>
                            <div className="hidden md:flex space-x-4">
                                <Link href="/modules" className="text-sm text-gray-600 hover:text-gray-900 transition-colors">Modules</Link>
                                <Link href="/tasks" className="text-sm text-gray-600 hover:text-gray-900 transition-colors">Tasks</Link>
                                <Link href="/studyflow" className="text-sm text-gray-600 hover:text-gray-900 transition-colors">Studyflow</Link>
                                <Link href="/progress" className="text-sm text-gray-600 hover:text-gray-900 transition-colors">Progress</Link>
                            </div>
                        </div>
                        <div className="flex items-center space-x-4">
                            <span className="text-sm text-gray-600">{user?.email}</span>
                            {user?.is_admin && (
                                <Badge variant="secondary">Admin</Badge>
                            )}
                            <button
                                onClick={logout}
                                className="text-sm text-red-600 hover:text-red-500 transition-colors"
                            >
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            {/* Main Content */}
            <main className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
                {/* Welcome Header with Refresh */}
                <div className="flex items-start justify-between mb-8">
                    <div>
                        <h2 className="text-2xl font-bold text-gray-900">
                            Welcome back, {user?.full_name || user?.email?.split("@")[0]}!
                        </h2>
                        <p className="text-gray-600 mt-1">Here&apos;s your learning dashboard overview.</p>
                    </div>
                    <RefreshButton onClick={handleRefresh} loading={refreshing} />
                </div>

                {/* Loading State: Skeletons */}
                {loading ? (
                    <>
                        {/* Stats Skeleton */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                            {Array.from({ length: 4 }).map((_, i) => (
                                <StatCardSkeleton key={i} />
                            ))}
                        </div>

                        {/* Main Panels Skeleton */}
                        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                            <PanelSkeleton lines={4} />
                            <PanelSkeleton lines={4} />
                            <PanelSkeleton lines={4} />
                        </div>

                        {/* Bottom Section Skeleton */}
                        <div className="grid md:grid-cols-2 gap-6">
                            <ProgressPanelSkeleton />
                            <SystemPanelSkeleton />
                        </div>
                    </>
                ) : error && !dashboard ? (
                    /* Full error state (only when no data at all) */
                    <Card className="border-red-200 bg-red-50">
                        <CardContent className="py-12">
                            <div className="flex flex-col items-center justify-center text-center">
                                <span className="text-5xl mb-4">😔</span>
                                <p className="text-lg font-medium text-red-600 mb-2">Unable to load dashboard</p>
                                <p className="text-sm text-muted-foreground mb-4">{error}</p>
                                <Button onClick={handleRefresh} disabled={refreshing}>
                                    {refreshing ? "Retrying..." : "Try Again"}
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                ) : dashboard ? (
                    <>
                        {/* Stats Grid */}
                        <section className="mb-8">
                            <h3 className="text-sm font-medium text-gray-500 uppercase tracking-wider mb-4">Overview</h3>
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                                <StatCard
                                    title="Total Modules"
                                    value={dashboard.stats.total_modules}
                                    subtitle={`${dashboard.stats.active_modules} active`}
                                />
                                <StatCard
                                    title="Total Tasks"
                                    value={dashboard.stats.total_tasks}
                                    subtitle={`${dashboard.stats.active_tasks} active`}
                                />
                                <StatCard
                                    title="Studyflows"
                                    value={dashboard.stats.total_studyflows}
                                />
                                <StatCard
                                    title="Progress Records"
                                    value={dashboard.stats.total_progress_records}
                                />
                            </div>
                        </section>

                        {/* Main Panels Grid */}
                        <section className="mb-8">
                            <h3 className="text-sm font-medium text-gray-500 uppercase tracking-wider mb-4">Content</h3>
                            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                                <ModulesPanel modules={dashboard.modules} />
                                <TasksPanel tasks={dashboard.tasks} />
                                <StudyflowPanel studyflows={dashboard.studyflow} />
                            </div>
                        </section>

                        {/* Bottom Section */}
                        <section>
                            <h3 className="text-sm font-medium text-gray-500 uppercase tracking-wider mb-4">Status</h3>
                            <div className="grid md:grid-cols-2 gap-6">
                                <ProgressPanel progress={dashboard.progress} />
                                <SystemInfoPanel system={dashboard.system} version={dashboard.version} />
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
