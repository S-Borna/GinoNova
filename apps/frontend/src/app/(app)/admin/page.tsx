"use client"

/**
 * Admin v2 Dashboard - Overview page with real-time stats
 */

import { useEffect, useState, useCallback } from "react"
import Link from "next/link"
import {
    Users,
    UserPlus,
    Activity,
    TrendingUp,
    TrendingDown,
    Clock,
    Zap,
    Bot,
    Database,
    Server,
    RefreshCw,
    ArrowRight,
    CheckCircle,
    AlertTriangle,
    Trophy,
    Bell,
    LogIn,
    UserCheck,
    FileCheck
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types
interface OverviewStats {
    online_users: number
    online_trend: number
    total_users: number
    total_users_trend: number
    new_users_today: number
    new_users_trend: number
    active_users_24h: number
    active_users_week: number
    total_study_sessions: number
    avg_session_duration_minutes: number
    total_tasks_completed: number
    total_ai_requests: number
    ai_cost_total: number
    ai_cost_today: number
}

interface ActivityData {
    date: string
    active_users: number
    new_users: number
    study_sessions: number
}

interface SystemHealth {
    database: { status: string; latency_ms: number }
    api: { status: string; latency_ms: number }
    openai: { status: string; rate_limit_percent: number }
}

interface ActivityLogEntry {
    id: string
    timestamp: string
    type: "login" | "registration" | "exam_completed"
    user_email: string
    user_name: string | null
    user_id: string
    details: string | null
    oauth_provider: string | null
}

// Components
function StatCard({
    icon: Icon,
    value,
    label,
    trend,
    trendLabel,
    color = "blue",
    loading = false
}: {
    icon: React.ElementType
    value: number | string
    label: string
    trend?: number
    trendLabel?: string
    color?: "blue" | "green" | "purple" | "yellow" | "red"
    loading?: boolean
}) {
    const colors = {
        blue: "from-blue-500/20 to-blue-600/10 border-blue-500/30 text-blue-400",
        green: "from-green-500/20 to-green-600/10 border-green-500/30 text-green-400",
        purple: "from-purple-500/20 to-purple-600/10 border-purple-500/30 text-purple-400",
        yellow: "from-yellow-500/20 to-yellow-600/10 border-yellow-500/30 text-yellow-400",
        red: "from-red-500/20 to-red-600/10 border-red-500/30 text-red-400",
    }

    return (
        <div className={cn(
            "p-5 rounded-xl border bg-gradient-to-br",
            colors[color] || colors.purple
        )}>
            {loading ? (
                <div className="animate-pulse">
                    <div className="h-10 w-10 bg-zinc-700 rounded-lg mb-3" />
                    <div className="h-8 w-20 bg-zinc-700 rounded mb-2" />
                    <div className="h-4 w-24 bg-zinc-700 rounded" />
                </div>
            ) : (
                <>
                    <Icon className="w-10 h-10 mb-3 opacity-80" />
                    <div className="text-3xl font-bold text-white">{value.toLocaleString()}</div>
                    <div className="text-sm opacity-70 mb-2">{label}</div>
                    {trend !== undefined && (
                        <div className={cn(
                            "text-xs flex items-center gap-1",
                            trend > 0 ? "text-green-400" : trend < 0 ? "text-red-400" : "text-zinc-400"
                        )}>
                            {trend > 0 ? <TrendingUp className="w-3 h-3" /> :
                                trend < 0 ? <TrendingDown className="w-3 h-3" /> : null}
                            {trend > 0 ? "+" : ""}{trend} {trendLabel || ""}
                        </div>
                    )}
                </>
            )}
        </div>
    )
}

function HealthIndicator({
    label,
    status,
    detail
}: {
    label: string
    status: "ok" | "warning" | "error"
    detail: string
}) {
    return (
        <div className="flex items-center justify-between py-2">
            <div className="flex items-center gap-2">
                {status === "ok" && <CheckCircle className="w-4 h-4 text-green-500" />}
                {status === "warning" && <AlertTriangle className="w-4 h-4 text-yellow-500" />}
                {status === "error" && <AlertTriangle className="w-4 h-4 text-red-500" />}
                <span className="text-sm">{label}</span>
            </div>
            <span className="text-xs text-zinc-400">{detail}</span>
        </div>
    )
}

function ActivityChart({ data, loading }: { data: ActivityData[], loading: boolean }) {
    if (loading) {
        return (
            <div className="h-48 flex items-center justify-center">
                <RefreshCw className="w-8 h-8 animate-spin text-purple-500" />
            </div>
        )
    }

    if (!data.length) {
        return (
            <div className="h-48 flex items-center justify-center text-zinc-500">
                No data available
            </div>
        )
    }

    const maxValue = Math.max(...data.map(d => d.active_users), 1)

    return (
        <div className="h-48 flex items-end gap-1">
            {data.map((d, i) => {
                const height = (d.active_users / maxValue) * 100
                return (
                    <div
                        key={d.date}
                        className="flex-1 flex flex-col items-center gap-1 group"
                    >
                        <div className="relative w-full">
                            <div
                                className="w-full bg-purple-500/30 rounded-t transition-all hover:bg-purple-500/50"
                                style={{ height: `${Math.max(height, 4)}%`, minHeight: '4px' }}
                            />
                            {/* Tooltip */}
                            <div className="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-zinc-800 px-2 py-1 rounded text-xs whitespace-nowrap z-10">
                                {d.active_users} active • {d.new_users} new
                            </div>
                        </div>
                        <span className="text-[10px] text-zinc-500 rotate-45 origin-left">
                            {new Date(d.date).toLocaleDateString('sv-SE', { day: 'numeric', month: 'short' })}
                        </span>
                    </div>
                )
            })}
        </div>
    )
}

function ActivityFeed({ activities, loading }: { activities: ActivityLogEntry[], loading: boolean }) {
    const getIcon = (type: string) => {
        switch (type) {
            case "login":
                return <LogIn className="w-4 h-4 text-green-400" />
            case "registration":
                return <UserCheck className="w-4 h-4 text-blue-400" />
            case "exam_completed":
                return <FileCheck className="w-4 h-4 text-yellow-400" />
            default:
                return <Activity className="w-4 h-4 text-zinc-400" />
        }
    }

    const getTypeLabel = (type: string) => {
        switch (type) {
            case "login":
                return "logged in"
            case "registration":
                return "registered"
            case "exam_completed":
                return "completed exam"
            default:
                return type
        }
    }

    const formatTime = (timestamp: string) => {
        const date = new Date(timestamp)
        const now = new Date()
        const diffMs = now.getTime() - date.getTime()
        const diffMins = Math.floor(diffMs / 60000)
        const diffHours = Math.floor(diffMs / 3600000)

        if (diffMins < 1) return "just now"
        if (diffMins < 60) return `${diffMins}m ago`
        if (diffHours < 24) return `${diffHours}h ago`
        return date.toLocaleDateString('sv-SE', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })
    }

    if (loading) {
        return (
            <div className="space-y-3">
                {[1, 2, 3, 4, 5].map(i => (
                    <div key={i} className="animate-pulse flex items-center gap-3">
                        <div className="w-8 h-8 bg-zinc-700 rounded-full" />
                        <div className="flex-1">
                            <div className="h-4 w-32 bg-zinc-700 rounded mb-1" />
                            <div className="h-3 w-24 bg-zinc-700 rounded" />
                        </div>
                    </div>
                ))}
            </div>
        )
    }

    if (!activities.length) {
        return (
            <div className="text-center py-8 text-zinc-500">
                <Bell className="w-8 h-8 mx-auto mb-2 opacity-50" />
                <p>No recent activity</p>
            </div>
        )
    }

    return (
        <div className="space-y-3 max-h-80 overflow-y-auto">
            {activities.map((entry) => (
                <div key={entry.id} className="flex items-start gap-3 p-2 rounded-lg hover:bg-zinc-800/50 transition">
                    <div className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center flex-shrink-0">
                        {getIcon(entry.type)}
                    </div>
                    <div className="flex-1 min-w-0">
                        <p className="text-sm">
                            <span className="font-medium text-white">
                                {entry.user_name || entry.user_email.split('@')[0]}
                            </span>
                            <span className="text-zinc-400"> {getTypeLabel(entry.type)}</span>
                        </p>
                        <div className="flex items-center gap-2 text-xs text-zinc-500">
                            <span>{formatTime(entry.timestamp)}</span>
                            {entry.oauth_provider && entry.oauth_provider !== "refresh" && (
                                <span className="px-1.5 py-0.5 bg-zinc-800 rounded text-zinc-400">
                                    {entry.oauth_provider}
                                </span>
                            )}
                        </div>
                        {entry.details && entry.type === "exam_completed" && (
                            <p className="text-xs text-zinc-500 mt-1 truncate">{entry.details}</p>
                        )}
                    </div>
                </div>
            ))}
        </div>
    )
}

// Main Component
export default function AdminV2Dashboard() {
    const [stats, setStats] = useState<OverviewStats | null>(null)
    const [activity, setActivity] = useState<ActivityData[]>([])
    const [activityLog, setActivityLog] = useState<ActivityLogEntry[]>([])
    const [health, setHealth] = useState<SystemHealth | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [lastUpdated, setLastUpdated] = useState<Date | null>(null)

    const fetchData = useCallback(async () => {
        const token = getToken()
        if (!token) {
            setError("Not authenticated - please log in")
            setLoading(false)
            return
        }

        setError(null)

        try {
            // Fetch all data in parallel
            const fetchOptions = { headers: { Authorization: `Bearer ${token}` } }

            const [statsRes, activityRes, healthRes, activityLogRes] = await Promise.all([
                fetch(`${API_BASE_URL}/api/admin/stats/overview`, fetchOptions),
                fetch(`${API_BASE_URL}/api/admin/stats/activity?days=7`, fetchOptions),
                fetch(`${API_BASE_URL}/api/admin/stats/system-health`, fetchOptions),
                fetch(`${API_BASE_URL}/api/admin/activity-log?limit=20`, fetchOptions)
            ])

            if (statsRes.ok) {
                const statsData = await statsRes.json()
                setStats(statsData)
            } else {
                console.error("Stats API error:", statsRes.status, await statsRes.text())
            }

            if (activityRes.ok) {
                const activityData = await activityRes.json()
                setActivity(activityData.data || [])
            } else {
                console.error("Activity API error:", activityRes.status, await activityRes.text())
            }

            if (healthRes.ok) {
                const healthData = await healthRes.json()
                setHealth(healthData)
            } else {
                console.error("Health API error:", healthRes.status, await healthRes.text())
            }

            if (activityLogRes.ok) {
                const activityLogData = await activityLogRes.json()
                setActivityLog(activityLogData.activities || [])
            } else {
                console.error("Activity Log API error:", activityLogRes.status)
            }

            setLastUpdated(new Date())
        } catch (err) {
            console.error("Dashboard fetch error:", err)
            setError(`Network error: ${err instanceof Error ? err.message : String(err)}`)
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchData()

        // Poll every 30 seconds
        const interval = setInterval(fetchData, 30000)
        return () => clearInterval(interval)
    }, [fetchData])

    return (
        <div className="p-6 max-w-7xl mx-auto">
            {/* Header */}
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-2xl font-bold">Dashboard</h1>
                    <p className="text-zinc-400 text-sm">
                        Real-time overview of your platform
                    </p>
                </div>
                <div className="flex items-center gap-3">
                    {lastUpdated && (
                        <span className="text-xs text-zinc-500">
                            Updated {lastUpdated.toLocaleTimeString()}
                        </span>
                    )}
                    <button
                        onClick={fetchData}
                        disabled={loading}
                        className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Refresh
                    </button>
                </div>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                <StatCard
                    icon={Activity}
                    value={stats?.online_users || 0}
                    label="Online Now"
                    trend={stats?.online_trend}
                    trendLabel="active last 10m"
                    color="green"
                    loading={loading}
                />
                <StatCard
                    icon={Users}
                    value={stats?.total_users || 0}
                    label="Total Users"
                    trend={stats?.total_users_trend}
                    trendLabel="this week"
                    color="blue"
                    loading={loading}
                />
                <StatCard
                    icon={UserPlus}
                    value={stats?.new_users_today || 0}
                    label="New Today"
                    trend={stats?.new_users_trend}
                    trendLabel="vs yesterday"
                    color="purple"
                    loading={loading}
                />
                <StatCard
                    icon={Clock}
                    value={stats?.active_users_24h || 0}
                    label="Active (24h)"
                    color="yellow"
                    loading={loading}
                />
            </div>

            {/* Charts & Info Row */}
            <div className="grid lg:grid-cols-3 gap-6 mb-8">
                {/* Activity Chart */}
                <div className="lg:col-span-2 bg-zinc-900/50 rounded-xl border border-zinc-800 p-5">
                    <div className="flex items-center justify-between mb-4">
                        <h2 className="font-semibold">User Activity (Last 7 Days)</h2>
                    </div>
                    <ActivityChart data={activity} loading={loading} />
                </div>

                {/* System Health */}
                <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-5">
                    <h2 className="font-semibold mb-4">System Health</h2>
                    <div className="space-y-1">
                        <HealthIndicator
                            label="Database"
                            status={health?.database?.status === "connected" ? "ok" : "error"}
                            detail={`${health?.database?.latency_ms || 0}ms`}
                        />
                        <HealthIndicator
                            label="API"
                            status={health?.api?.status === "healthy" ? "ok" : "warning"}
                            detail={`${health?.api?.latency_ms || 0}ms avg`}
                        />
                        <HealthIndicator
                            label="OpenAI"
                            status={
                                (health?.openai?.rate_limit_percent || 0) > 90 ? "warning" :
                                    health?.openai?.status === "connected" ? "ok" : "error"
                            }
                            detail={`${health?.openai?.rate_limit_percent || 0}% used`}
                        />
                    </div>
                </div>
            </div>

            {/* Activity Feed */}
            <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-5 mb-8">
                <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-2">
                        <Bell className="w-5 h-5 text-purple-400" />
                        <h2 className="font-semibold">Live Activity Feed</h2>
                    </div>
                    <span className="text-xs text-zinc-500">
                        Auto-updates every 30s
                    </span>
                </div>
                <ActivityFeed activities={activityLog} loading={loading} />
            </div>

            {/* Quick Actions */}
            <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-5">
                <h2 className="font-semibold mb-4">Quick Actions</h2>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                    <Link
                        href="/admin/users"
                        className="flex items-center justify-between p-4 bg-zinc-800/50 rounded-lg hover:bg-zinc-800 transition group"
                    >
                        <div className="flex items-center gap-3">
                            <Users className="w-5 h-5 text-blue-400" />
                            <span>View All Users</span>
                        </div>
                        <ArrowRight className="w-4 h-4 text-zinc-500 group-hover:text-white transition" />
                    </Link>
                    <Link
                        href="/admin/analytics"
                        className="flex items-center justify-between p-4 bg-zinc-800/50 rounded-lg hover:bg-zinc-800 transition group"
                    >
                        <div className="flex items-center gap-3">
                            <Zap className="w-5 h-5 text-yellow-400" />
                            <span>Analytics</span>
                        </div>
                        <ArrowRight className="w-4 h-4 text-zinc-500 group-hover:text-white transition" />
                    </Link>
                    <Link
                        href="/admin/ai-usage"
                        className="flex items-center justify-between p-4 bg-zinc-800/50 rounded-lg hover:bg-zinc-800 transition group"
                    >
                        <div className="flex items-center gap-3">
                            <Bot className="w-5 h-5 text-purple-400" />
                            <span>AI Usage</span>
                        </div>
                        <ArrowRight className="w-4 h-4 text-zinc-500 group-hover:text-white transition" />
                    </Link>
                    <Link
                        href="/admin/settings"
                        className="flex items-center justify-between p-4 bg-zinc-800/50 rounded-lg hover:bg-zinc-800 transition group"
                    >
                        <div className="flex items-center gap-3">
                            <Database className="w-5 h-5 text-green-400" />
                            <span>Settings</span>
                        </div>
                        <ArrowRight className="w-4 h-4 text-zinc-500 group-hover:text-white transition" />
                    </Link>
                    <Link
                        href="/admin/exam-stats"
                        className="flex items-center justify-between p-4 bg-zinc-800/50 rounded-lg hover:bg-zinc-800 transition group"
                    >
                        <div className="flex items-center gap-3">
                            <Trophy className="w-5 h-5 text-yellow-400" />
                            <span>Exam Stats</span>
                        </div>
                        <ArrowRight className="w-4 h-4 text-zinc-500 group-hover:text-white transition" />
                    </Link>
                </div>
            </div>

            {/* Additional Stats */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
                <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-4">
                    <div className="text-2xl font-bold">{stats?.active_users_week || 0}</div>
                    <div className="text-sm text-zinc-400">Active this week</div>
                </div>
                <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-4">
                    <div className="text-2xl font-bold">{stats?.total_study_sessions || 0}</div>
                    <div className="text-sm text-zinc-400">Study sessions</div>
                </div>
                <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-4">
                    <div className="text-2xl font-bold">{stats?.total_tasks_completed || 0}</div>
                    <div className="text-sm text-zinc-400">Tasks completed</div>
                </div>
                <div className="bg-zinc-900/50 rounded-xl border border-zinc-800 p-4">
                    <div className="text-2xl font-bold">${stats?.ai_cost_total?.toFixed(2) || "0.00"}</div>
                    <div className="text-sm text-zinc-400">AI cost (total)</div>
                </div>
            </div>
        </div>
    )
}
