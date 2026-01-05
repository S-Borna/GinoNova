"use client"

/**
 * Admin v2 AI Usage - Platform AI consumption and costs
 */

import { useEffect, useState, useCallback } from "react"
import {
    RefreshCw,
    Brain,
    DollarSign,
    Zap,
    AlertTriangle,
    TrendingUp,
    TrendingDown,
    Users,
    Activity,
    Clock,
    ChevronDown,
    ChevronUp
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || ""

// Types
interface AIUsageData {
    summary: {
        total_requests: number
        total_tokens: number
        estimated_cost: number
        avg_response_time: number
        success_rate: number
        unique_users: number
        requests_today: number
        requests_change: number
    }
    by_feature: Array<{
        name: string
        requests: number
        tokens: number
        cost: number
        avg_time: number
    }>
    by_model: Array<{
        model: string
        requests: number
        tokens: number
        cost: number
    }>
    by_day: Array<{
        date: string
        requests: number
        tokens: number
        cost: number
    }>
    top_users: Array<{
        user_id: string
        email: string
        requests: number
        tokens: number
    }>
    errors: Array<{
        type: string
        count: number
        last_occurred: string
    }>
}

type TimeRange = "7d" | "30d" | "90d"

// Components
function MetricCard({
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
    color?: "purple" | "blue" | "green" | "orange" | "red"
}) {
    const colors = {
        purple: "text-purple-400",
        blue: "text-blue-400",
        green: "text-green-400",
        orange: "text-orange-400",
        red: "text-red-400"
    }

    return (
        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
            <div className="flex items-start justify-between mb-3">
                <Icon className={cn("w-6 h-6", colors[color])} />
                {trend !== undefined && (
                    <span className={cn(
                        "flex items-center gap-1 text-xs font-medium",
                        trend >= 0 ? "text-green-400" : "text-red-400"
                    )}>
                        {trend >= 0 ? <TrendingUp className="w-3 h-3" /> : <TrendingDown className="w-3 h-3" />}
                        {Math.abs(trend).toFixed(1)}%
                    </span>
                )}
            </div>
            <div className="text-2xl font-bold mb-1">{value}</div>
            <div className="text-sm text-zinc-400">{title}</div>
            {subtitle && <div className="text-xs text-zinc-500 mt-1">{subtitle}</div>}
        </div>
    )
}

function UsageChart({ data }: { data: Array<{ date: string; requests: number; cost: number }> }) {
    const maxRequests = Math.max(...data.map(d => d.requests), 1)

    return (
        <div>
            <div className="flex items-end gap-1 h-48">
                {data.map((item, i) => {
                    const height = (item.requests / maxRequests) * 100
                    const date = new Date(item.date)
                    return (
                        <div key={i} className="flex-1 flex flex-col items-center gap-1 group">
                            <div className="relative w-full">
                                <div
                                    className="w-full bg-gradient-to-t from-purple-600 to-pink-500 rounded-t opacity-80 group-hover:opacity-100 transition cursor-pointer"
                                    style={{ height: `${height}%`, minHeight: item.requests > 0 ? 4 : 0 }}
                                />
                                <div className="absolute -top-16 left-1/2 -translate-x-1/2 bg-zinc-800 px-3 py-2 rounded-lg text-xs opacity-0 group-hover:opacity-100 transition whitespace-nowrap z-10 border border-zinc-700">
                                    <div className="font-medium">{item.requests.toLocaleString()} requests</div>
                                    <div className="text-zinc-400">${item.cost.toFixed(2)}</div>
                                </div>
                            </div>
                            <span className="text-[10px] text-zinc-500">
                                {date.toLocaleDateString("sv-SE", { day: "numeric", month: "short" })}
                            </span>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

function FeatureTable({ data }: { data: AIUsageData["by_feature"] }) {
    const [sortField, setSortField] = useState<"requests" | "tokens" | "cost">("requests")
    const [sortAsc, setSortAsc] = useState(false)

    const sorted = [...data].sort((a, b) => {
        const diff = a[sortField] - b[sortField]
        return sortAsc ? diff : -diff
    })

    const toggleSort = (field: "requests" | "tokens" | "cost") => {
        if (sortField === field) {
            setSortAsc(!sortAsc)
        } else {
            setSortField(field)
            setSortAsc(false)
        }
    }

    const SortIcon = ({ field }: { field: string }) => {
        if (sortField !== field) return null
        return sortAsc ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />
    }

    return (
        <div className="overflow-x-auto">
            <table className="w-full">
                <thead>
                    <tr className="text-left text-xs text-zinc-400 border-b border-zinc-800">
                        <th className="py-3 px-4 font-medium">Feature</th>
                        <th 
                            className="py-3 px-4 font-medium cursor-pointer hover:text-white transition"
                            onClick={() => toggleSort("requests")}
                        >
                            <span className="flex items-center gap-1">
                                Requests <SortIcon field="requests" />
                            </span>
                        </th>
                        <th 
                            className="py-3 px-4 font-medium cursor-pointer hover:text-white transition"
                            onClick={() => toggleSort("tokens")}
                        >
                            <span className="flex items-center gap-1">
                                Tokens <SortIcon field="tokens" />
                            </span>
                        </th>
                        <th 
                            className="py-3 px-4 font-medium cursor-pointer hover:text-white transition"
                            onClick={() => toggleSort("cost")}
                        >
                            <span className="flex items-center gap-1">
                                Cost <SortIcon field="cost" />
                            </span>
                        </th>
                        <th className="py-3 px-4 font-medium">Avg Time</th>
                    </tr>
                </thead>
                <tbody>
                    {sorted.map((feature, i) => (
                        <tr key={i} className="border-b border-zinc-800/50 hover:bg-zinc-800/30 transition">
                            <td className="py-3 px-4">
                                <span className="font-medium">{feature.name}</span>
                            </td>
                            <td className="py-3 px-4 text-sm">{feature.requests.toLocaleString()}</td>
                            <td className="py-3 px-4 text-sm">{feature.tokens.toLocaleString()}</td>
                            <td className="py-3 px-4 text-sm text-green-400">${feature.cost.toFixed(2)}</td>
                            <td className="py-3 px-4 text-sm text-zinc-400">{feature.avg_time}ms</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

function ModelBreakdown({ data }: { data: AIUsageData["by_model"] }) {
    const total = data.reduce((sum, d) => sum + d.requests, 0) || 1
    
    const modelColors: Record<string, string> = {
        "gpt-4": "from-purple-500 to-purple-600",
        "gpt-4-turbo": "from-blue-500 to-blue-600",
        "gpt-3.5-turbo": "from-green-500 to-green-600",
        "claude-3-opus": "from-orange-500 to-orange-600",
        "claude-3-sonnet": "from-pink-500 to-pink-600",
        "default": "from-zinc-500 to-zinc-600"
    }

    return (
        <div className="space-y-4">
            {data.map((model, i) => {
                const percentage = (model.requests / total) * 100
                const colorClass = modelColors[model.model] || modelColors.default
                
                return (
                    <div key={i}>
                        <div className="flex items-center justify-between mb-2">
                            <span className="font-medium text-sm">{model.model}</span>
                            <span className="text-xs text-zinc-400">
                                {model.requests.toLocaleString()} ({percentage.toFixed(1)}%)
                            </span>
                        </div>
                        <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                            <div 
                                className={cn("h-full rounded-full bg-gradient-to-r", colorClass)}
                                style={{ width: `${percentage}%` }}
                            />
                        </div>
                        <div className="flex justify-between mt-1 text-xs text-zinc-500">
                            <span>{model.tokens.toLocaleString()} tokens</span>
                            <span>${model.cost.toFixed(2)}</span>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

function TopUsersTable({ data }: { data: AIUsageData["top_users"] }) {
    return (
        <div className="space-y-3">
            {data.slice(0, 10).map((user, i) => (
                <div 
                    key={user.user_id}
                    className="flex items-center justify-between p-3 bg-zinc-800/30 rounded-lg hover:bg-zinc-800/50 transition"
                >
                    <div className="flex items-center gap-3">
                        <span className="w-6 h-6 rounded-full bg-zinc-700 flex items-center justify-center text-xs font-bold">
                            {i + 1}
                        </span>
                        <div>
                            <div className="text-sm font-medium truncate max-w-[200px]">{user.email}</div>
                            <div className="text-xs text-zinc-500">{user.tokens.toLocaleString()} tokens</div>
                        </div>
                    </div>
                    <div className="text-right">
                        <div className="text-sm font-bold text-purple-400">{user.requests.toLocaleString()}</div>
                        <div className="text-xs text-zinc-500">requests</div>
                    </div>
                </div>
            ))}
        </div>
    )
}

function ErrorsSection({ data }: { data: AIUsageData["errors"] }) {
    if (data.length === 0) {
        return (
            <div className="flex items-center gap-3 p-4 bg-green-500/10 border border-green-500/20 rounded-xl">
                <div className="w-10 h-10 rounded-full bg-green-500/20 flex items-center justify-center">
                    <Zap className="w-5 h-5 text-green-400" />
                </div>
                <div>
                    <div className="font-medium text-green-400">All Systems Nominal</div>
                    <div className="text-sm text-zinc-400">No AI errors in selected period</div>
                </div>
            </div>
        )
    }

    return (
        <div className="space-y-3">
            {data.map((error, i) => (
                <div 
                    key={i}
                    className="flex items-center justify-between p-4 bg-red-500/10 border border-red-500/20 rounded-xl"
                >
                    <div className="flex items-center gap-3">
                        <AlertTriangle className="w-5 h-5 text-red-400" />
                        <div>
                            <div className="font-medium">{error.type}</div>
                            <div className="text-xs text-zinc-400">
                                Last: {new Date(error.last_occurred).toLocaleString("sv-SE")}
                            </div>
                        </div>
                    </div>
                    <div className="text-2xl font-bold text-red-400">{error.count}</div>
                </div>
            ))}
        </div>
    )
}

// Main Component
export default function AdminV2AIUsage() {
    const [data, setData] = useState<AIUsageData | null>(null)
    const [loading, setLoading] = useState(true)
    const [timeRange, setTimeRange] = useState<TimeRange>("30d")

    const fetchData = useCallback(async () => {
        const token = getToken()
        if (!token) return

        setLoading(true)

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/ai-usage?range=${timeRange}`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                setData(await res.json())
            }
        } finally {
            setLoading(false)
        }
    }, [timeRange])

    useEffect(() => {
        fetchData()
    }, [fetchData])

    // Auto-refresh every 2 minutes
    useEffect(() => {
        const interval = setInterval(fetchData, 2 * 60 * 1000)
        return () => clearInterval(interval)
    }, [fetchData])

    const formatCost = (cost: number) => {
        if (cost >= 1000) return `$${(cost / 1000).toFixed(1)}k`
        return `$${cost.toFixed(2)}`
    }

    return (
        <div className="p-6">
            {/* Header */}
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h1 className="text-2xl font-bold">AI Usage</h1>
                    <p className="text-sm text-zinc-400">Monitor AI consumption and costs</p>
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
                        onClick={fetchData}
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
            ) : data ? (
                <>
                    {/* Summary Cards */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                        <MetricCard
                            title="Total Requests"
                            value={data.summary.total_requests.toLocaleString()}
                            icon={Brain}
                            trend={data.summary.requests_change}
                            color="purple"
                        />
                        <MetricCard
                            title="Total Tokens"
                            value={data.summary.total_tokens.toLocaleString()}
                            icon={Activity}
                            color="blue"
                        />
                        <MetricCard
                            title="Estimated Cost"
                            value={formatCost(data.summary.estimated_cost)}
                            subtitle={`${timeRange} period`}
                            icon={DollarSign}
                            color="green"
                        />
                        <MetricCard
                            title="Success Rate"
                            value={`${data.summary.success_rate.toFixed(1)}%`}
                            icon={Zap}
                            color={data.summary.success_rate >= 99 ? "green" : "orange"}
                        />
                    </div>

                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                        <MetricCard
                            title="Avg Response"
                            value={`${data.summary.avg_response_time}ms`}
                            icon={Clock}
                            color="orange"
                        />
                        <MetricCard
                            title="Unique Users"
                            value={data.summary.unique_users.toLocaleString()}
                            icon={Users}
                            color="blue"
                        />
                        <MetricCard
                            title="Today's Requests"
                            value={data.summary.requests_today.toLocaleString()}
                            subtitle="so far"
                            icon={TrendingUp}
                            color="purple"
                        />
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
                            <div className="text-xs text-zinc-400 mb-2">Cost per Request</div>
                            <div className="text-2xl font-bold text-green-400">
                                ${(data.summary.estimated_cost / Math.max(data.summary.total_requests, 1)).toFixed(4)}
                            </div>
                            <div className="text-xs text-zinc-500 mt-1">average</div>
                        </div>
                    </div>

                    {/* Usage Chart */}
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                        <h3 className="font-semibold mb-4 flex items-center gap-2">
                            <Activity className="w-5 h-5 text-purple-400" />
                            Daily Usage
                        </h3>
                        <UsageChart data={data.by_day} />
                    </div>

                    {/* Two Column Layout */}
                    <div className="grid md:grid-cols-2 gap-6 mb-6">
                        {/* Model Breakdown */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <Brain className="w-5 h-5 text-blue-400" />
                                By Model
                            </h3>
                            <ModelBreakdown data={data.by_model} />
                        </div>

                        {/* Top Users */}
                        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                            <h3 className="font-semibold mb-4 flex items-center gap-2">
                                <Users className="w-5 h-5 text-green-400" />
                                Top Users
                            </h3>
                            <TopUsersTable data={data.top_users} />
                        </div>
                    </div>

                    {/* Feature Table */}
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                        <h3 className="font-semibold mb-4 flex items-center gap-2">
                            <Zap className="w-5 h-5 text-orange-400" />
                            By Feature
                        </h3>
                        <FeatureTable data={data.by_feature} />
                    </div>

                    {/* Errors */}
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                        <h3 className="font-semibold mb-4 flex items-center gap-2">
                            <AlertTriangle className="w-5 h-5 text-red-400" />
                            Errors & Issues
                        </h3>
                        <ErrorsSection data={data.errors} />
                    </div>
                </>
            ) : (
                <div className="text-center py-12 text-zinc-500">
                    Failed to load AI usage data
                </div>
            )}
        </div>
    )
}
