"use client"

/**
 * Dashboard Page
 * Phase 6.0: Full Dashboard with Backend Integration
 */

import { useEffect, useState } from "react"
import Link from "next/link"
import { Protected, useAuth } from "@/components/auth"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { ProgressBar } from "@/components/ui/progress-bar"
import {
    getDashboardSummary,
    DashboardSummary,
    DashboardModule,
    DashboardTask,
    DashboardStudyflow,
    DashboardProgress,
} from "@/lib/dashboard"

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
                    <p className="text-sm text-muted-foreground">No modules yet</p>
                ) : (
                    <ul className="space-y-2">
                        {modules.slice(0, 5).map((m) => (
                            <li key={m.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50">
                                <Link href={`/modules/${m.id}`} className="text-sm font-medium hover:underline">
                                    {m.name}
                                </Link>
                                <Badge variant={m.is_active ? "success" : "inactive"}>
                                    {m.is_active ? "Active" : "Inactive"}
                                </Badge>
                            </li>
                        ))}
                        {modules.length > 5 && (
                            <li className="text-xs text-muted-foreground text-center pt-2">
                                +{modules.length - 5} more modules
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

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
                    <p className="text-sm text-muted-foreground">No tasks yet</p>
                ) : (
                    <ul className="space-y-2">
                        {tasks.slice(0, 5).map((t) => (
                            <li key={t.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50">
                                <Link href={`/tasks/${t.id}`} className="text-sm font-medium hover:underline">
                                    {t.title}
                                </Link>
                                <span className={`text-xs px-2 py-0.5 rounded-full ${difficultyColor(t.difficulty)}`}>
                                    {t.difficulty}
                                </span>
                            </li>
                        ))}
                        {tasks.length > 5 && (
                            <li className="text-xs text-muted-foreground text-center pt-2">
                                +{tasks.length - 5} more tasks
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

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
                    <p className="text-sm text-muted-foreground">No studyflows yet</p>
                ) : (
                    <ul className="space-y-2">
                        {studyflows.slice(0, 5).map((sf) => (
                            <li key={sf.id} className="flex items-center justify-between p-2 rounded-lg bg-muted/50">
                                <Link href={`/studyflow/${sf.id}`} className="text-sm font-medium hover:underline">
                                    {sf.title}
                                </Link>
                                <span className="text-xs text-muted-foreground">
                                    Step {sf.order}
                                </span>
                            </li>
                        ))}
                        {studyflows.length > 5 && (
                            <li className="text-xs text-muted-foreground text-center pt-2">
                                +{studyflows.length - 5} more studyflows
                            </li>
                        )}
                    </ul>
                )}
            </CardContent>
        </Card>
    )
}

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
                    <p className="text-sm text-muted-foreground">No progress records yet. Start learning!</p>
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
                            <li className="text-xs text-muted-foreground text-center pt-2">
                                <Link href="/progress" className="hover:underline">
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

function DashboardContent() {
    const { user, logout } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        async function fetchDashboard() {
            setLoading(true)
            const result = await getDashboardSummary(user?.id)
            if (result.ok) {
                setDashboard(result.data)
                setError(null)
            } else {
                setError(result.message)
            }
            setLoading(false)
        }
        fetchDashboard()
    }, [user?.id])

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Navigation */}
            <nav className="bg-white shadow">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex items-center space-x-8">
                            <h1 className="text-xl font-bold text-gray-900">DevOpsHub</h1>
                            <div className="hidden md:flex space-x-4">
                                <Link href="/modules" className="text-sm text-gray-600 hover:text-gray-900">Modules</Link>
                                <Link href="/tasks" className="text-sm text-gray-600 hover:text-gray-900">Tasks</Link>
                                <Link href="/studyflow" className="text-sm text-gray-600 hover:text-gray-900">Studyflow</Link>
                                <Link href="/progress" className="text-sm text-gray-600 hover:text-gray-900">Progress</Link>
                            </div>
                        </div>
                        <div className="flex items-center space-x-4">
                            <span className="text-sm text-gray-600">{user?.email}</span>
                            {user?.is_admin && (
                                <Badge variant="secondary">Admin</Badge>
                            )}
                            <button
                                onClick={logout}
                                className="text-sm text-red-600 hover:text-red-500"
                            >
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            {/* Main Content */}
            <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                {/* Welcome Header */}
                <div className="mb-8">
                    <h2 className="text-2xl font-bold text-gray-900">
                        Welcome back, {user?.full_name || user?.email?.split("@")[0]}!
                    </h2>
                    <p className="text-gray-600 mt-1">Here&apos;s your learning dashboard overview.</p>
                </div>

                {loading ? (
                    <div className="flex items-center justify-center py-12">
                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
                        <span className="ml-3 text-gray-600">Loading dashboard...</span>
                    </div>
                ) : error ? (
                    <Card className="border-red-200 bg-red-50">
                        <CardContent className="pt-6">
                            <p className="text-red-600">Error loading dashboard: {error}</p>
                        </CardContent>
                    </Card>
                ) : dashboard ? (
                    <>
                        {/* Stats Grid */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
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

                        {/* Main Panels Grid */}
                        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                            <ModulesPanel modules={dashboard.modules} />
                            <TasksPanel tasks={dashboard.tasks} />
                            <StudyflowPanel studyflows={dashboard.studyflow} />
                        </div>

                        {/* Bottom Section */}
                        <div className="grid md:grid-cols-2 gap-6">
                            <ProgressPanel progress={dashboard.progress} />
                            <SystemInfoPanel system={dashboard.system} version={dashboard.version} />
                        </div>
                    </>
                ) : null}
            </main>
        </div>
    )
}

export default function DashboardPage() {
    return (
        <Protected>
            <DashboardContent />
        </Protected>
    )
}
