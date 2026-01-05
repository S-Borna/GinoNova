"use client"

/**
 * Admin v2 Analytics - Platform-wide analytics dashboard
 */

import { useEffect, useState, useCallback } from "react"
import {
    RefreshCw,
    Users,
    TrendingUp,
    TrendingDown,
    Calendar,
    Clock,
    BookOpen,
    CheckCircle,
    Target,
    Zap,
    BarChart3
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types
interface AnalyticsData {
    overview: {
        total_users: number
        active_users_7d: number
        active_users_30d: number
        new_users_7d: number
        new_users_30d: number
        growth_rate: number
    }
    engagement: {
        avg_session_duration: number
        sessions_per_user: number
        modules_completed_total: number
        tasks_completed_total: number
        avg_modules_per_user: number
        avg_tasks_per_user: number
    }
    retention: {
        day1: number
        day7: number
        day30: number
    }
    activity_by_hour: Array<{ hour: number; count: number }>
    activity_by_day: Array<{ date: string; users: number; sessions: number }>
    top_modules: Array<{ name: string; completions: number; avg_time: number }>
    user_levels: Array<{ level: number; count: number }>
}

type TimeRange = "7d" | "30d" | "90d"

// Components
function StatCard({
    title,
    value,
    subtitle,
    icon: Icon,
    trend,
    color = "purple"
}: {
    title: string
    value: string | number
    subtitle?: string
    icon: React.ElementType
    trend?: number
    color?: "purple" | "blue" | "green" | "orange" | "pink"
}) {
    const colors = {
        purple: "from-purple-500/20 to-purple-600/20 text-purple-400",
        blue: "from-blue-500/20 to-blue-600/20 text-blue-400",
        green: "from-green-500/20 to-green-600/20 text-green-400",
        orange: "from-orange-500/20 to-orange-600/20 text-orange-400",
        pink: "from-pink-500/20 to-pink-600/20 text-pink-400"
    }

    return (
        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
            <div className={cn(
                "w-10 h-10 rounded-lg flex items-center justify-center mb-3 bg-gradient-to-br",
                colors[color]
            )}>
                <Icon className="w-5 h-5" />
            </div>
            <div className="text-2xl font-bold mb-1">{value}</div>
            <div className="text-sm text-zinc-400">{title}</div>
            {(trend !== undefined || subtitle) && (
                <div className="flex items-center gap-2 mt-2 text-xs">
                    {trend !== undefined && (
                        <span className={cn(
                            "flex items-center gap-1",
                            trend >= 0 ? "text-green-400" : "text-red-400"
                        )}>
                            {trend >= 0 ? <TrendingUp className="w-3 h-3" /> : <TrendingDown className="w-3 h-3" />}
                            {Math.abs(trend).toFixed(1)}%
                        </span>
                    )}
                    {subtitle && <span className="text-zinc-500">{subtitle}</span>}
                </div>
            )}
        </div>
    )
}

function BarChart({ data, xKey, yKey, label }: {
    data: Array<Record<string, unknown>>
    xKey: string
    yKey: string
    label: string
}) {
    const maxValue = Math.max(...data.map(d => Number(d[yKey]) || 0), 1)
    
    // Show only every nth label based on data length
    const showEveryN = data.length > 10 ? Math.ceil(data.length / 5) : 1

    return (
        <div>
            <div className="flex items-end gap-1 h-48">
                {data.map((item, i) => {
                    const value = Number(item[yKey]) || 0
                    const height = (value / maxValue) * 100
                    const dateStr = String(item[xKey])
                    // Format date nicely: "2026-01-05" -> "5 jan"
                    const formattedDate = (() => {
                        try {
                            const d = new Date(dateStr)
                            return d.toLocaleDateString('sv-SE', { day: 'numeric', month: 'short' })
                        } catch {
                            return dateStr.slice(-5) // fallback: "01-05"
                        }
                    })()
                    const showLabel = i % showEveryN === 0 || i === data.length - 1
                    
                    return (
                        <div key={i} className="flex-1 flex flex-col items-center gap-1">
                            <div
                                className="w-full bg-purple-500 rounded-t opacity-80 hover:opacity-100 transition cursor-pointer relative group"
                                style={{ height: `${height}%`, minHeight: value > 0 ? 4 : 0 }}
                            >
                                <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-zinc-800 px-2 py-1 rounded text-xs opacity-0 group-hover:opacity-100 transition whitespace-nowrap z-10">
                                    {formattedDate}: {value.toLocaleString()}
                                </div>
                            </div>
                            {showLabel ? (
                                <span className="text-[10px] text-zinc-500 whitespace-nowrap">
                                    {formattedDate}
                                </span>
                            ) : (
                                <span className="text-[10px] text-transparent">.</span>
                            )}
                        </div>
                    )
                })}
            </div>
            <div className="text-center text-xs text-zinc-500 mt-2">{label}</div>
        </div>
    )
}

function HourlyChart({ data }: { data: Array<{ hour: number; count: number }> }) {
    const maxValue = Math.max(...data.map(d => d.count), 1)

    // Fill in missing hours
    const fullData = Array.from({ length: 24 }, (_, i) => {
        const found = data.find(d => d.hour === i)
        return { hour: i, count: found?.count || 0 }
    })

    return (
        <div>
            <div className="flex items-end gap-0.5 h-32">
                {fullData.map((item, i) => {
                    const height = (item.count / maxValue) * 100
                    return (
                        <div key={i} className="flex-1 flex flex-col items-center">
                            <div
                                className="w-full bg-blue-500 rounded-t opacity-70 hover:opacity-100 transition cursor-pointer relative group"
                                style={{ height: `${height}%`, minHeight: item.count > 0 ? 2 : 0 }}
                            >
                                <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-zinc-800 px-2 py-1 rounded text-xs opacity-0 group-hover:opacity-100 transition whitespace-nowrap z-10">
                                    {item.hour}:00 - {item.count}
                                </div>
                            </div>
                        </div>
                    )
                })}
            </div>
            <div className="flex justify-between text-[10px] text-zinc-500 mt-1">
                <span>00:00</span>
                <span>06:00</span>
                <span>12:00</span>
                <span>18:00</span>
                <span>23:00</span>
            </div>
        </div>
    )
}

function RetentionCard({ label, value }: { label: string, value: number }) {
    const getColor = (v: number) => {
        if (v >= 70) return "text-green-400 bg-green-500/20"
        if (v >= 40) return "text-yellow-400 bg-yellow-500/20"
        return "text-red-400 bg-red-500/20"
    }

    return (
        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4 text-center">
            <div className={cn("text-3xl font-bold mb-1", getColor(value).split(" ")[0])}>
                {value}%
            </div>
            <div className="text-xs text-zinc-400">{label}</div>
        </div>
    )
}

function LevelDistribution({ data }: { data: Array<{ level: number; count: number }> }) {
    const total = data.reduce((sum, d) => sum + d.count, 0) || 1

    return (
        <div className="space-y-2">
            {data.slice(0, 10).map((item) => {
                const percentage = (item.count / total) * 100
                return (
                    <div key={item.level} className="flex items-center gap-3">
                        <span className="text-xs text-zinc-400 w-12">Lv.{item.level}</span>
                        <div className="flex-1 h-6 bg-zinc-800 rounded-full overflow-hidden">
                            <div
                                className="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-end pr-2"
                                style={{ width: `${Math.max(percentage, 5)}%` }}
                            >
                                <span className="text-[10px] font-medium">{item.count}</span>
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

// Main Component
export default function AdminV2Analytics() {
    const [data, setData] = useState<AnalyticsData | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [timeRange, setTimeRange] = useState<TimeRange>("30d")

    const fetchAnalytics = useCallback(async () => {
        const token = getToken()
        if (!token) {
            setError("Not authenticated - please log in")
            setLoading(false)
            return
        }

        setLoading(true)
        setError(null)

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/analytics?range=${timeRange}`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const json = await res.json()
                setData(json)
            } else {
                const errorText = await res.text()
                console.error("Analytics API error:", res.status, errorText)
                setError(`API error: ${res.status} - ${errorText}`)
            }
        } catch (err) {
            console.error("Analytics fetch error:", err)
            setError(`Network error: ${err instanceof Error ? err.message : String(err)}`)
        } finally {
            setLoading(false)
        }
    }, [timeRange])

    useEffect(() => {
        fetchAnalytics()
    }, [fetchAnalytics])

    // Auto-refresh every 5 minutes
    useEffect(() => {
        const interval = setInterval(fetchAnalytics, 5 * 60 * 1000)
        return () => clearInterval(interval)
    }, [fetchAnalytics])

    const formatDuration = (seconds: number) => {
        if (seconds < 60) return `${seconds}s`
        if (seconds < 3600) return `${Math.floor(seconds / 60)}m`
        return `${(seconds / 3600).toFixed(1)}h`
    }

    return (
        <div className="p-6">
            {/* Header */}
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h1 className="text-2xl font-bold">Analytics</h1>
                    <p className="text-sm text-zinc-400">Platform performance metrics</p>
                </div>
                <div className="flex items-center gap-3">
                    {/* Time Range */}
                    <div className="flex gap-1 p-1 bg-zinc-900 rounded-lg">
                        {(["7d", "30d", "90d"] as TimeRange[]).map(range => (
                            <button
                                key={range}
                                onClick={() => setTimeRange(range)}
                                className={cn(
                                    "px-3 py-1.5 rounded text-sm font-medium transition",
                                    timeRange === range
                                        ? "bg-zinc-800 text-white"
                                        : "text-zinc-400 hover:text-white"
                                )}
                            >
                                {range}
                            </button>
                        ))}
                    </div>

                    <button
                        onClick={fetchAnalytics}
                        disabled={loading}
                        className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Refresh
                    </button>
                </div>
            </div>

            {loading && !data ? (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    {[...Array(8)].map((_, i) => (
                        <div key={i} className="h-32 bg-zinc-800 rounded-xl animate-pulse" />
                    ))}
                </div>
            ) : data?.overview ? (
                <>
                    {/* Overview Stats */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                        <StatCard
                            title="Total Users"
                            value={(data.overview.total_users || 0).toLocaleString()}
                            icon={Users}
                            trend={data.overview.growth_rate || 0}
                            color="purple"
                        />
                        <StatCard
                            title={`Active (${timeRange})`}
                            value={timeRange === "7d"
                                ? (data.overview.active_users_7d || 0).toLocaleString()
                                : (data.overview.active_users_30d || 0).toLocaleString()
                            }
                            subtitle="unique users"
                            icon={Zap}
                            color="green"
                        />
                        <StatCard
                            title="New Users"
                            value={timeRange === "7d"
                                ? (data.overview.new_users_7d || 0).toLocaleString()
                                : (data.overview.new_users_30d || 0).toLocaleString()
                            }
                            subtitle={`last ${timeRange}`}
                            icon={TrendingUp}
                            color="blue"
                        />
                        <StatCard
                            title="Avg Session"
                            value={formatDuration(data.engagement?.avg_session_duration || 0)}
                            icon={Clock}
                            color="orange"
                        />
                    </div>

                    {/* Engagement Stats */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                        <StatCard
                            title="Modules Completed"
                            value={(data.engagement?.modules_completed_total || 0).toLocaleString()}
                            subtitle={`${(data.engagement?.avg_modules_per_user || 0).toFixed(1)} per user`}
                            icon={BookOpen}
                            color="green"
                        />
                        <StatCard
                            title="Tasks Completed"
                            value={(data.engagement?.tasks_completed_total || 0).toLocaleString()}
                            subtitle={`${(data.engagement?.avg_tasks_per_user || 0).toFixed(1)} per user`}
                            icon={CheckCircle}
                            color="blue"
                        />
                        <StatCard
                            title="Sessions/User"
                            value={(data.engagement?.sessions_per_user || 0).toFixed(1)}
                            subtitle="average"
                            icon={Target}
                            color="pink"
                        />
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4">
                            <h3 className="text-sm font-medium text-zinc-400 mb-3">Retention</h3>
                            <div className="grid grid-cols-3 gap-2">
                                <RetentionCard label="Day 1" value={data.retention?.day1 || 0} />
                                <RetentionCard label="Day 7" value={data.retention?.day7 || 0} />
                                <RetentionCard label="Day 30" value={data.retention?.day30 || 0} />
                            </div>
                        </div>
                    </div>

                    {/* Charts Row */}
                    <div className="grid md:grid-cols-2 gap-6 mb-6">
                        {/* Activity by Day */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <Calendar className="w-5 h-5 text-purple-400" />
                                Daily Activity
                            </h3>
                            <BarChart
                                data={data.activity_by_day || []}
                                xKey="date"
                                yKey="users"
                                label="Active Users per Day"
                            />
                        </div>

                        {/* Activity by Hour */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <Clock className="w-5 h-5 text-blue-400" />
                                Peak Hours
                            </h3>
                            <HourlyChart data={data.activity_by_hour || []} />
                        </div>
                    </div>

                    {/* Bottom Row */}
                    <div className="grid md:grid-cols-2 gap-6">
                        {/* Top Modules */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <BookOpen className="w-5 h-5 text-green-400" />
                                Top Modules
                            </h3>
                            {(data.top_modules || []).length === 0 ? (
                                <p className="text-zinc-500 text-sm">No data yet</p>
                            ) : (
                                <div className="space-y-3">
                                    {(data.top_modules || []).slice(0, 5).map((module, i) => (
                                        <div key={i} className="flex items-center justify-between py-2 border-b border-zinc-800 last:border-0">
                                            <div>
                                                <div className="font-medium text-sm">{module.name}</div>
                                                <div className="text-xs text-zinc-500">
                                                    Avg time: {formatDuration(module.avg_time || 0)}
                                                </div>
                                            </div>
                                            <div className="text-right">
                                                <div className="text-lg font-bold text-green-400">{module.completions || 0}</div>
                                                <div className="text-xs text-zinc-500">completions</div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>

                        {/* User Level Distribution */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <BarChart3 className="w-5 h-5 text-purple-400" />
                                Level Distribution
                            </h3>
                            {(data.user_levels || []).length === 0 ? (
                                <p className="text-zinc-500 text-sm">No data yet</p>
                            ) : (
                                <LevelDistribution data={data.user_levels || []} />
                            )}
                        </div>
                    </div>
                </>
            ) : (
                <div className="text-center py-12">
                    <p className="text-zinc-500 mb-2">Failed to load analytics data</p>
                    {error && <p className="text-red-400 text-sm">{error}</p>}
                </div>
            )}
        </div>
    )
}
