"use client"

/**
 * ============================================================================
 * ADMIN DASHBOARD — User Management & Analytics
 * ============================================================================
 *
 * Features:
 * - Stats overview cards
 * - User list with detailed progress
 * - Activity indicators
 * - Only visible to admin
 *
 * @phase Admin
 */

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import {
    Users,
    Trophy,
    Flame,
    CheckCircle,
    Calendar,
    Shield,
    Loader2,
    TrendingUp,
    Activity,
    BookOpen,
    Target,
    Clock,
    UserPlus,
    Zap,
    BarChart3,
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

interface AdminUser {
    id: string
    full_name: string | null
    email: string
    created_at: string
    updated_at: string
    total_xp: number
    level: number
    tasks_completed: number
    modules_started: number
    modules_completed: number
    last_active: string | null
    is_active: boolean
}

interface AdminStats {
    total_users: number
    users_today: number
    users_this_week: number
    total_tasks_completed: number
    total_xp_earned: number
    active_users_today: number
    avg_tasks_per_user: number
    avg_xp_per_user: number
    total_modules: number
    total_tasks: number
}

interface AdminUsersResponse {
    users: AdminUser[]
    total: number
    stats: AdminStats
}

// Stat Card Component
function StatCard({
    icon: Icon,
    label,
    value,
    subValue,
    color,
}: {
    icon: React.ElementType
    label: string
    value: string | number
    subValue?: string
    color: string
}) {
    return (
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-5">
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm font-medium text-gray-500 dark:text-gray-400">
                        {label}
                    </p>
                    <p className="mt-1 text-2xl font-bold text-gray-900 dark:text-white">
                        {typeof value === "number" ? value.toLocaleString() : value}
                    </p>
                    {subValue && (
                        <p className="mt-1 text-xs text-gray-500">{subValue}</p>
                    )}
                </div>
                <div className={`p-3 rounded-xl ${color}`}>
                    <Icon className="w-5 h-5 text-white" />
                </div>
            </div>
        </div>
    )
}

// Time ago helper
function timeAgo(dateString: string | null): string {
    if (!dateString) return "Never"
    
    const date = new Date(dateString)
    const now = new Date()
    const seconds = Math.floor((now.getTime() - date.getTime()) / 1000)
    
    if (seconds < 60) return "Just now"
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`
    if (seconds < 604800) return `${Math.floor(seconds / 86400)}d ago`
    
    return date.toLocaleDateString("en-US", { month: "short", day: "numeric" })
}

// Activity indicator
function ActivityIndicator({ lastActive }: { lastActive: string | null }) {
    if (!lastActive) {
        return (
            <span className="inline-flex items-center gap-1.5 text-gray-400">
                <span className="w-2 h-2 rounded-full bg-gray-300" />
                Never
            </span>
        )
    }
    
    const date = new Date(lastActive)
    const now = new Date()
    const hoursSinceActive = (now.getTime() - date.getTime()) / (1000 * 60 * 60)
    
    if (hoursSinceActive < 1) {
        return (
            <span className="inline-flex items-center gap-1.5 text-green-600">
                <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                Online
            </span>
        )
    }
    
    if (hoursSinceActive < 24) {
        return (
            <span className="inline-flex items-center gap-1.5 text-amber-600">
                <span className="w-2 h-2 rounded-full bg-amber-500" />
                {timeAgo(lastActive)}
            </span>
        )
    }
    
    return (
        <span className="inline-flex items-center gap-1.5 text-gray-500">
            <span className="w-2 h-2 rounded-full bg-gray-400" />
            {timeAgo(lastActive)}
        </span>
    )
}

export default function AdminUsersPage() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()
    const [data, setData] = useState<AdminUsersResponse | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    useEffect(() => {
        if (authLoading) return

        if (!user || !isAdmin) {
            router.push("/dashboard")
            return
        }

        const fetchUsers = async () => {
            try {
                const token = getToken()
                const res = await fetch(`${API_BASE_URL}/api/admin/users`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                })

                if (!res.ok) {
                    if (res.status === 403) {
                        router.push("/dashboard")
                        return
                    }
                    throw new Error("Failed to fetch users")
                }

                const responseData: AdminUsersResponse = await res.json()
                setData(responseData)
            } catch (err) {
                setError(err instanceof Error ? err.message : "An error occurred")
            } finally {
                setLoading(false)
            }
        }

        fetchUsers()
        
        // Auto-refresh every 30 seconds
        const interval = setInterval(fetchUsers, 30000)
        return () => clearInterval(interval)
    }, [user, authLoading, isAdmin, router])

    const formatDate = (dateString: string) => {
        return new Date(dateString).toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit",
        })
    }

    if (authLoading || loading) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="flex flex-col items-center gap-4">
                    <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
                    <p className="text-gray-500">Loading admin dashboard...</p>
                </div>
            </div>
        )
    }

    if (!isAdmin) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                        Access Denied
                    </h1>
                    <p className="text-gray-500">
                        You don&apos;t have permission to view this page.
                    </p>
                </div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="text-center">
                    <p className="text-red-500">{error}</p>
                </div>
            </div>
        )
    }

    const stats = data?.stats
    const users = data?.users || []

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Header */}
            <div className="mb-8">
                <div className="flex items-center gap-3 mb-2">
                    <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                        <Shield className="w-6 h-6 text-white" />
                    </div>
                    <div>
                        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Admin Dashboard
                        </h1>
                        <p className="text-sm text-gray-500">
                            User analytics & platform overview
                        </p>
                    </div>
                </div>
            </div>

            {/* Stats Grid */}
            {stats && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                    <StatCard
                        icon={Users}
                        label="Total Users"
                        value={stats.total_users}
                        subValue={`+${stats.users_this_week} this week`}
                        color="bg-indigo-500"
                    />
                    <StatCard
                        icon={Activity}
                        label="Active Today"
                        value={stats.active_users_today}
                        subValue={`${stats.users_today} new today`}
                        color="bg-green-500"
                    />
                    <StatCard
                        icon={CheckCircle}
                        label="Tasks Completed"
                        value={stats.total_tasks_completed}
                        subValue={`${stats.avg_tasks_per_user} avg/user`}
                        color="bg-amber-500"
                    />
                    <StatCard
                        icon={Zap}
                        label="Total XP Earned"
                        value={stats.total_xp_earned}
                        subValue={`${stats.avg_xp_per_user} avg/user`}
                        color="bg-purple-500"
                    />
                </div>
            )}

            {/* Content Stats */}
            {stats && (
                <div className="grid grid-cols-2 gap-4 mb-8">
                    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-5">
                        <div className="flex items-center gap-3">
                            <div className="p-2 rounded-lg bg-blue-100 dark:bg-blue-900/30">
                                <BookOpen className="w-5 h-5 text-blue-600" />
                            </div>
                            <div>
                                <p className="text-2xl font-bold text-gray-900 dark:text-white">
                                    {stats.total_modules}
                                </p>
                                <p className="text-sm text-gray-500">Modules Available</p>
                            </div>
                        </div>
                    </div>
                    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-5">
                        <div className="flex items-center gap-3">
                            <div className="p-2 rounded-lg bg-orange-100 dark:bg-orange-900/30">
                                <Target className="w-5 h-5 text-orange-600" />
                            </div>
                            <div>
                                <p className="text-2xl font-bold text-gray-900 dark:text-white">
                                    {stats.total_tasks}
                                </p>
                                <p className="text-sm text-gray-500">Tasks in System</p>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Users Table */}
            <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
                    <h2 className="text-lg font-semibold text-gray-900 dark:text-white flex items-center gap-2">
                        <Users className="w-5 h-5" />
                        Registered Users ({users.length})
                    </h2>
                </div>
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead>
                            <tr className="bg-gray-50 dark:bg-gray-900/50 border-b border-gray-200 dark:border-gray-700">
                                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    User
                                </th>
                                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center gap-1">
                                        <Clock className="w-3.5 h-3.5" />
                                        Status
                                    </div>
                                </th>
                                <th className="px-6 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-1">
                                        <Trophy className="w-3.5 h-3.5" />
                                        Level
                                    </div>
                                </th>
                                <th className="px-6 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-1">
                                        <Zap className="w-3.5 h-3.5" />
                                        XP
                                    </div>
                                </th>
                                <th className="px-6 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-1">
                                        <BookOpen className="w-3.5 h-3.5" />
                                        Modules
                                    </div>
                                </th>
                                <th className="px-6 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-1">
                                        <CheckCircle className="w-3.5 h-3.5" />
                                        Tasks
                                    </div>
                                </th>
                                <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center gap-1">
                                        <Calendar className="w-3.5 h-3.5" />
                                        Joined
                                    </div>
                                </th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
                            {users.map((u) => (
                                <tr
                                    key={u.id}
                                    className="hover:bg-gray-50 dark:hover:bg-gray-900/30 transition-colors"
                                >
                                    <td className="px-6 py-4">
                                        <div className="flex items-center gap-3">
                                            <div className="relative">
                                                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white font-bold text-sm">
                                                    {u.full_name?.[0]?.toUpperCase() ||
                                                        u.email[0].toUpperCase()}
                                                </div>
                                                {u.email === ADMIN_EMAIL && (
                                                    <div className="absolute -top-1 -right-1 w-4 h-4 bg-amber-500 rounded-full flex items-center justify-center">
                                                        <Shield className="w-2.5 h-2.5 text-white" />
                                                    </div>
                                                )}
                                            </div>
                                            <div>
                                                <p className="font-medium text-gray-900 dark:text-white text-sm">
                                                    {u.full_name || "No name"}
                                                </p>
                                                <p className="text-xs text-gray-500">
                                                    {u.email}
                                                </p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="px-6 py-4">
                                        <ActivityIndicator lastActive={u.last_active} />
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400">
                                            Lvl {u.level}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400">
                                            {u.total_xp.toLocaleString()}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="text-sm text-gray-700 dark:text-gray-300">
                                            {u.modules_completed}/{u.modules_started}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400">
                                            {u.tasks_completed}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-xs text-gray-500">
                                        {formatDate(u.created_at)}
                                    </td>
                                </tr>
                            ))}

                            {users.length === 0 && (
                                <tr>
                                    <td
                                        colSpan={7}
                                        className="px-6 py-12 text-center text-gray-500"
                                    >
                                        <UserPlus className="w-12 h-12 mx-auto mb-3 text-gray-300" />
                                        <p>No users have registered yet</p>
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
            
            {/* Auto-refresh indicator */}
            <p className="mt-4 text-xs text-center text-gray-400">
                Auto-refreshes every 30 seconds
            </p>
        </div>
    )
}
