"use client"

/**
 * ============================================================================
 * ADMIN COMMAND CENTER — Full Control Dashboard
 * ============================================================================
 *
 * The ultimate admin dashboard with:
 * - Real-time user statistics
 * - User management (view, edit, track)
 * - Activity monitoring
 * - System health
 *
 * @phase Admin
 * @access Admin only (said.ebadi@hotmail.com)
 */

import { useEffect, useState, useCallback } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
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
    Eye,
    Edit,
    Search,
    RefreshCw,
    ChevronRight,
    AlertCircle,
    Server,
    Database,
    Globe,
    MousePointer,
    LogIn,
    LogOut,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import Link from "next/link"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface AdminUser {
    id: string
    full_name: string | null
    email: string
    avatar_url?: string | null
    bio?: string | null
    is_active: boolean
    is_admin: boolean
    is_verified?: boolean
    created_at: string
    updated_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    current_streak?: number
    longest_streak?: number
    tasks_completed: number
    modules_started?: number
    modules_completed: number
    labs_completed?: number
    projects_completed?: number
    total_study_time?: number
}

interface SystemStats {
    total_users: number
    active_users: number
    admin_users: number
    users_today: number
    users_this_week: number
    total_tracks: number
    total_modules: number
    total_tasks: number
    total_labs: number
    total_projects: number
    total_tasks_completed: number
    total_xp_earned: number
    total_study_minutes: number
    active_sessions: number
    avg_tasks_per_user: number
    avg_xp_per_user: number
    avg_session_minutes: number
    database_status: string
    cache_status: string
    api_version: string
}

interface AdminUsersResponse {
    users: AdminUser[]
    total: number
    page: number
    per_page: number
    total_pages: number
}

/* ============================================================================
   COMPONENTS
   ============================================================================ */

function StatCard({
    icon: Icon,
    label,
    value,
    subValue,
    color,
    trend,
}: {
    icon: React.ElementType
    label: string
    value: string | number
    subValue?: string
    color: string
    trend?: "up" | "down" | "neutral"
}) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative overflow-hidden rounded-2xl",
                "bg-zinc-900/80 border border-zinc-800",
                "p-5 transition-all duration-300",
                "hover:border-zinc-700 hover:shadow-lg"
            )}
        >
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm font-medium text-zinc-400">{label}</p>
                    <p className="mt-1 text-3xl font-bold text-white">
                        {typeof value === "number" ? value.toLocaleString() : value}
                    </p>
                    {subValue && (
                        <p className="mt-1 text-xs text-zinc-500 flex items-center gap-1">
                            {trend === "up" && <TrendingUp className="w-3 h-3 text-emerald-400" />}
                            {subValue}
                        </p>
                    )}
                </div>
                <div className={cn("p-3 rounded-xl", color)}>
                    <Icon className="w-5 h-5 text-white" />
                </div>
            </div>
        </motion.div>
    )
}

function ActivityIndicator({ lastActive }: { lastActive: string | null }) {
    if (!lastActive) {
        return (
            <span className="inline-flex items-center gap-1.5 text-zinc-500 text-xs">
                <span className="w-2 h-2 rounded-full bg-zinc-600" />
                Aldrig
            </span>
        )
    }

    const date = new Date(lastActive)
    const now = new Date()
    const hoursSinceActive = (now.getTime() - date.getTime()) / (1000 * 60 * 60)

    if (hoursSinceActive < 0.5) {
        return (
            <span className="inline-flex items-center gap-1.5 text-emerald-400 text-xs">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                Online nu
            </span>
        )
    }

    if (hoursSinceActive < 24) {
        const hours = Math.floor(hoursSinceActive)
        return (
            <span className="inline-flex items-center gap-1.5 text-amber-400 text-xs">
                <span className="w-2 h-2 rounded-full bg-amber-500" />
                {hours}h sedan
            </span>
        )
    }

    const days = Math.floor(hoursSinceActive / 24)
    return (
        <span className="inline-flex items-center gap-1.5 text-zinc-400 text-xs">
            <span className="w-2 h-2 rounded-full bg-zinc-500" />
            {days}d sedan
        </span>
    )
}

function UserRow({ user, onViewDetails }: { user: AdminUser; onViewDetails: (user: AdminUser) => void }) {
    return (
        <motion.tr
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="border-b border-zinc-800/50 hover:bg-zinc-800/30 transition-colors"
        >
            <td className="px-4 py-3">
                <div className="flex items-center gap-3">
                    <div className="relative">
                        <div className={cn(
                            "w-10 h-10 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-br from-purple-500 to-indigo-600",
                            "text-white font-bold text-sm"
                        )}>
                            {user.full_name?.[0]?.toUpperCase() || user.email[0].toUpperCase()}
                        </div>
                        {user.is_admin && (
                            <div className="absolute -top-1 -right-1 w-4 h-4 bg-amber-500 rounded-full flex items-center justify-center">
                                <Shield className="w-2.5 h-2.5 text-white" />
                            </div>
                        )}
                    </div>
                    <div>
                        <p className="font-medium text-white text-sm">
                            {user.full_name || "Inget namn"}
                        </p>
                        <p className="text-xs text-zinc-500">{user.email}</p>
                    </div>
                </div>
            </td>
            <td className="px-4 py-3">
                <ActivityIndicator lastActive={user.last_activity_at} />
            </td>
            <td className="px-4 py-3 text-center">
                <span className={cn(
                    "inline-flex items-center px-2 py-1 rounded-lg text-xs font-semibold",
                    "bg-amber-500/20 text-amber-400"
                )}>
                    Lvl {user.level}
                </span>
            </td>
            <td className="px-4 py-3 text-center">
                <span className={cn(
                    "inline-flex items-center gap-1 px-2 py-1 rounded-lg text-xs font-semibold",
                    "bg-purple-500/20 text-purple-400"
                )}>
                    <Zap className="w-3 h-3" />
                    {user.total_xp.toLocaleString()}
                </span>
            </td>
            <td className="px-4 py-3 text-center">
                <span className="text-sm text-zinc-300">
                    {user.modules_completed}/{user.modules_started || 0}
                </span>
            </td>
            <td className="px-4 py-3 text-center">
                <span className={cn(
                    "inline-flex items-center px-2 py-1 rounded-lg text-xs font-semibold",
                    "bg-emerald-500/20 text-emerald-400"
                )}>
                    {user.tasks_completed}
                </span>
            </td>
            <td className="px-4 py-3 text-xs text-zinc-500">
                {new Date(user.created_at).toLocaleDateString("sv-SE")}
            </td>
            <td className="px-4 py-3">
                <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => onViewDetails(user)}
                    className="text-zinc-400 hover:text-white"
                >
                    <Eye className="w-4 h-4" />
                </Button>
            </td>
        </motion.tr>
    )
}

function UserDetailModal({ user, onClose }: { user: AdminUser; onClose: () => void }) {
    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
            onClick={onClose}
        >
            <motion.div
                initial={{ scale: 0.95, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.95, opacity: 0 }}
                onClick={(e) => e.stopPropagation()}
                className={cn(
                    "w-full max-w-2xl max-h-[90vh] overflow-y-auto",
                    "bg-zinc-900 rounded-2xl border border-zinc-800",
                    "shadow-2xl"
                )}
            >
                {/* Header */}
                <div className="p-6 border-b border-zinc-800">
                    <div className="flex items-center gap-4">
                        <div className={cn(
                            "w-16 h-16 rounded-2xl flex items-center justify-center",
                            "bg-gradient-to-br from-purple-500 to-indigo-600",
                            "text-white font-bold text-2xl"
                        )}>
                            {user.full_name?.[0]?.toUpperCase() || user.email[0].toUpperCase()}
                        </div>
                        <div>
                            <h2 className="text-xl font-bold text-white">
                                {user.full_name || "Inget namn"}
                            </h2>
                            <p className="text-zinc-400">{user.email}</p>
                            <div className="flex items-center gap-2 mt-2">
                                {user.is_admin && (
                                    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-amber-500/20 text-amber-400">
                                        <Shield className="w-3 h-3" />
                                        Admin
                                    </span>
                                )}
                                {user.is_active ? (
                                    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-emerald-500/20 text-emerald-400">
                                        Aktiv
                                    </span>
                                ) : (
                                    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-red-500/20 text-red-400">
                                        Inaktiv
                                    </span>
                                )}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Stats */}
                <div className="p-6 grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="text-center p-4 rounded-xl bg-zinc-800/50">
                        <div className="text-2xl font-bold text-amber-400">Lvl {user.level}</div>
                        <div className="text-xs text-zinc-500">Nivå</div>
                    </div>
                    <div className="text-center p-4 rounded-xl bg-zinc-800/50">
                        <div className="text-2xl font-bold text-purple-400">{user.total_xp.toLocaleString()}</div>
                        <div className="text-xs text-zinc-500">Total XP</div>
                    </div>
                    <div className="text-center p-4 rounded-xl bg-zinc-800/50">
                        <div className="text-2xl font-bold text-emerald-400">{user.tasks_completed}</div>
                        <div className="text-xs text-zinc-500">Tasks klara</div>
                    </div>
                    <div className="text-center p-4 rounded-xl bg-zinc-800/50">
                        <div className="text-2xl font-bold text-orange-400">{user.current_streak || 0}</div>
                        <div className="text-xs text-zinc-500">Streak</div>
                    </div>
                </div>

                {/* Details */}
                <div className="p-6 border-t border-zinc-800 space-y-4">
                    <h3 className="font-semibold text-white mb-3">Detaljer</h3>

                    <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                            <span className="text-zinc-500">Registrerad:</span>
                            <span className="ml-2 text-white">
                                {new Date(user.created_at).toLocaleDateString("sv-SE", {
                                    year: "numeric",
                                    month: "long",
                                    day: "numeric",
                                    hour: "2-digit",
                                    minute: "2-digit"
                                })}
                            </span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Senast aktiv:</span>
                            <span className="ml-2 text-white">
                                {user.last_activity_at
                                    ? new Date(user.last_activity_at).toLocaleDateString("sv-SE", {
                                        year: "numeric",
                                        month: "long",
                                        day: "numeric",
                                        hour: "2-digit",
                                        minute: "2-digit"
                                    })
                                    : "Aldrig"
                                }
                            </span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Moduler påbörjade:</span>
                            <span className="ml-2 text-white">{user.modules_started || 0}</span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Moduler klara:</span>
                            <span className="ml-2 text-white">{user.modules_completed}</span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Labs klara:</span>
                            <span className="ml-2 text-white">{user.labs_completed || 0}</span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Projekt klara:</span>
                            <span className="ml-2 text-white">{user.projects_completed || 0}</span>
                        </div>
                        <div>
                            <span className="text-zinc-500">Längsta streak:</span>
                            <span className="ml-2 text-white">{user.longest_streak || 0} dagar</span>
                        </div>
                        <div>
                            <span className="text-zinc-500">User ID:</span>
                            <span className="ml-2 text-zinc-400 font-mono text-xs">{user.id}</span>
                        </div>
                    </div>
                </div>

                {/* Actions */}
                <div className="p-6 border-t border-zinc-800 flex justify-end gap-3">
                    <Button variant="outline" onClick={onClose}>
                        Stäng
                    </Button>
                    <Link prefetch={false} href={`/admin/users/${user.id}`}>
                        <Button className="bg-purple-600 hover:bg-purple-500">
                            <Edit className="w-4 h-4 mr-2" />
                            Redigera profil
                        </Button>
                    </Link>
                </div>
            </motion.div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export default function AdminCommandCenter() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()

    const [users, setUsers] = useState<AdminUser[]>([])
    const [stats, setStats] = useState<SystemStats | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [searchQuery, setSearchQuery] = useState("")
    const [selectedUser, setSelectedUser] = useState<AdminUser | null>(null)
    const [lastRefresh, setLastRefresh] = useState<Date>(new Date())

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    const fetchData = useCallback(async () => {
        try {
            const token = getToken()

            if (!token) {
                setError("Du måste vara inloggad för att se admin-panelen")
                setLoading(false)
                return
            }

            // Fetch users
            const usersRes = await fetch(`${API_BASE_URL}/api/admin/users?per_page=100`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
            })

            if (!usersRes.ok) {
                if (usersRes.status === 401) {
                    setError("Sessionen har gått ut. Vänligen logga in igen.")
                    return
                }
                if (usersRes.status === 403) {
                    router.push("/dashboard")
                    return
                }
                const errorData = await usersRes.json().catch(() => ({}))
                throw new Error(errorData.detail || `API-fel: ${usersRes.status}`)
            }

            const usersData: AdminUsersResponse = await usersRes.json()
            setUsers(usersData.users)

            // Fetch stats
            try {
                const statsRes = await fetch(`${API_BASE_URL}/api/admin/stats`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                        "Content-Type": "application/json"
                    },
                })

                if (statsRes.ok) {
                    const statsData: SystemStats = await statsRes.json()
                    setStats(statsData)
                }
            } catch (statsErr) {
                // Stats endpoint might not exist - silent fail
            }

            setError(null)
            setLastRefresh(new Date())
        } catch (err) {
            const errorMsg = err instanceof Error ? err.message : "Ett fel uppstod vid hämtning av data"
            setError(errorMsg)
        } finally {
            setLoading(false)
        }
    }, [router])

    useEffect(() => {
        if (authLoading) return

        if (!user || !isAdmin) {
            router.push("/dashboard")
            return
        }

        fetchData()

        // Auto-refresh every 30 seconds
        const interval = setInterval(fetchData, 30000)
        return () => clearInterval(interval)
    }, [user, authLoading, isAdmin, router, fetchData])

    // Filter users by search
    const filteredUsers = users.filter(u => {
        if (!searchQuery) return true
        const query = searchQuery.toLowerCase()
        return (
            u.email.toLowerCase().includes(query) ||
            (u.full_name?.toLowerCase().includes(query))
        )
    })

    if (authLoading || loading) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="text-center"
                >
                    <Loader2 className="w-12 h-12 text-purple-500 animate-spin mx-auto mb-4" />
                    <p className="text-zinc-400">Laddar Admin Command Center...</p>
                </motion.div>
            </div>
        )
    }

    if (!isAdmin) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-white mb-2">Åtkomst nekad</h1>
                    <p className="text-zinc-400">Du har inte behörighet att se denna sida.</p>
                </div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center p-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="text-center max-w-md"
                >
                    <AlertCircle className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-white mb-2">Fel</h1>
                    <p className="text-zinc-400 mb-6">{error}</p>

                    <div className="space-y-3">
                        <Button
                            onClick={() => { setError(null); setLoading(true); fetchData(); }}
                            className="w-full bg-purple-600 hover:bg-purple-500"
                        >
                            <RefreshCw className="w-4 h-4 mr-2" />
                            Försök igen
                        </Button>

                        <Button
                            variant="outline"
                            onClick={() => router.push("/dashboard")}
                            className="w-full border-zinc-700"
                        >
                            Tillbaka till Dashboard
                        </Button>
                    </div>

                    <p className="mt-6 text-xs text-zinc-600">
                        API: {API_BASE_URL}
                    </p>
                </motion.div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-zinc-950 p-6 lg:p-8">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <div className={cn(
                            "w-14 h-14 rounded-2xl flex items-center justify-center",
                            "bg-gradient-to-br from-purple-600 to-indigo-600",
                            "shadow-lg shadow-purple-500/25"
                        )}>
                            <Shield className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold text-white">
                                Admin Command Center
                            </h1>
                            <p className="text-zinc-400">
                                Full kontroll över DevOpsHub
                            </p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3">
                        <span className="text-xs text-zinc-500">
                            Uppdaterad: {lastRefresh.toLocaleTimeString("sv-SE")}
                        </span>
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={fetchData}
                            className="border-zinc-700"
                        >
                            <RefreshCw className="w-4 h-4 mr-2" />
                            Uppdatera
                        </Button>
                    </div>
                </div>
            </motion.div>

            {/* Stats Grid */}
            {stats && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                    <StatCard
                        icon={Users}
                        label="Totalt användare"
                        value={stats.total_users}
                        subValue={`+${stats.users_this_week} denna vecka`}
                        color="bg-indigo-500"
                        trend="up"
                    />
                    <StatCard
                        icon={Activity}
                        label="Aktiva idag"
                        value={stats.users_today}
                        subValue={`${stats.active_users} totalt aktiva`}
                        color="bg-emerald-500"
                    />
                    <StatCard
                        icon={CheckCircle}
                        label="Tasks slutförda"
                        value={stats.total_tasks_completed}
                        subValue={`${stats.avg_tasks_per_user} snitt/användare`}
                        color="bg-amber-500"
                    />
                    <StatCard
                        icon={Zap}
                        label="Total XP"
                        value={stats.total_xp_earned}
                        subValue={`${stats.avg_xp_per_user} snitt/användare`}
                        color="bg-purple-500"
                    />
                </div>
            )}

            {/* System Status */}
            {stats && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className={cn(
                            "flex items-center gap-3 p-4 rounded-xl",
                            "bg-zinc-900/80 border border-zinc-800"
                        )}
                    >
                        <Database className={cn(
                            "w-5 h-5",
                            stats.database_status === "postgres" ? "text-emerald-400" : "text-amber-400"
                        )} />
                        <div>
                            <p className="text-xs text-zinc-500">Databas</p>
                            <p className="text-sm font-medium text-white capitalize">
                                {stats.database_status}
                            </p>
                        </div>
                    </motion.div>
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        className={cn(
                            "flex items-center gap-3 p-4 rounded-xl",
                            "bg-zinc-900/80 border border-zinc-800"
                        )}
                    >
                        <BookOpen className="w-5 h-5 text-blue-400" />
                        <div>
                            <p className="text-xs text-zinc-500">Moduler</p>
                            <p className="text-sm font-medium text-white">{stats.total_modules}</p>
                        </div>
                    </motion.div>
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2 }}
                        className={cn(
                            "flex items-center gap-3 p-4 rounded-xl",
                            "bg-zinc-900/80 border border-zinc-800"
                        )}
                    >
                        <Target className="w-5 h-5 text-orange-400" />
                        <div>
                            <p className="text-xs text-zinc-500">Tasks</p>
                            <p className="text-sm font-medium text-white">{stats.total_tasks}</p>
                        </div>
                    </motion.div>
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.3 }}
                        className={cn(
                            "flex items-center gap-3 p-4 rounded-xl",
                            "bg-zinc-900/80 border border-zinc-800"
                        )}
                    >
                        <Server className="w-5 h-5 text-purple-400" />
                        <div>
                            <p className="text-xs text-zinc-500">API Version</p>
                            <p className="text-sm font-medium text-white">{stats.api_version}</p>
                        </div>
                    </motion.div>
                </div>
            )}

            {/* Admin Tools Section */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <div className="flex items-center gap-2 mb-4">
                    <Shield className="w-5 h-5 text-amber-400" />
                    <h2 className="text-lg font-semibold text-white">Admin Verktyg</h2>
                </div>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <Link href="/admin/permissions" prefetch={false}>
                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            className={cn(
                                "p-4 rounded-xl cursor-pointer",
                                "bg-zinc-900/80 border border-zinc-800",
                                "hover:border-purple-500/50 hover:bg-zinc-800/50",
                                "transition-all duration-200"
                            )}
                        >
                            <div className="flex items-center gap-3">
                                <div className="p-2 rounded-lg bg-purple-500/20">
                                    <Shield className="w-5 h-5 text-purple-400" />
                                </div>
                                <div>
                                    <p className="font-medium text-white text-sm">Rättigheter</p>
                                    <p className="text-xs text-zinc-500">Feature access</p>
                                </div>
                            </div>
                        </motion.div>
                    </Link>
                    <Link href="/admin/users" prefetch={false}>
                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            className={cn(
                                "p-4 rounded-xl cursor-pointer",
                                "bg-zinc-900/80 border border-zinc-800",
                                "hover:border-indigo-500/50 hover:bg-zinc-800/50",
                                "transition-all duration-200"
                            )}
                        >
                            <div className="flex items-center gap-3">
                                <div className="p-2 rounded-lg bg-indigo-500/20">
                                    <Users className="w-5 h-5 text-indigo-400" />
                                </div>
                                <div>
                                    <p className="font-medium text-white text-sm">Användare</p>
                                    <p className="text-xs text-zinc-500">Hantera alla</p>
                                </div>
                            </div>
                        </motion.div>
                    </Link>
                    <Link href="/admin/content" prefetch={false}>
                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            className={cn(
                                "p-4 rounded-xl cursor-pointer",
                                "bg-zinc-900/80 border border-zinc-800",
                                "hover:border-emerald-500/50 hover:bg-zinc-800/50",
                                "transition-all duration-200"
                            )}
                        >
                            <div className="flex items-center gap-3">
                                <div className="p-2 rounded-lg bg-emerald-500/20">
                                    <BookOpen className="w-5 h-5 text-emerald-400" />
                                </div>
                                <div>
                                    <p className="font-medium text-white text-sm">Innehåll</p>
                                    <p className="text-xs text-zinc-500">Moduler & kurser</p>
                                </div>
                            </div>
                        </motion.div>
                    </Link>
                    <Link href="/admin/analytics" prefetch={false}>
                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            className={cn(
                                "p-4 rounded-xl cursor-pointer",
                                "bg-zinc-900/80 border border-zinc-800",
                                "hover:border-amber-500/50 hover:bg-zinc-800/50",
                                "transition-all duration-200"
                            )}
                        >
                            <div className="flex items-center gap-3">
                                <div className="p-2 rounded-lg bg-amber-500/20">
                                    <BarChart3 className="w-5 h-5 text-amber-400" />
                                </div>
                                <div>
                                    <p className="font-medium text-white text-sm">Analytics</p>
                                    <p className="text-xs text-zinc-500">Statistik</p>
                                </div>
                            </div>
                        </motion.div>
                    </Link>
                </div>
            </motion.div>

            {/* Users Section */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "rounded-2xl overflow-hidden",
                    "bg-zinc-900/80 border border-zinc-800"
                )}
            >
                {/* Users Header */}
                <div className="p-6 border-b border-zinc-800">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <Users className="w-5 h-5 text-purple-400" />
                            <h2 className="text-lg font-semibold text-white">
                                Användare ({users.length})
                            </h2>
                        </div>
                        <div className="flex items-center gap-3">
                            <div className="relative">
                                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                                <input
                                    type="text"
                                    placeholder="Sök användare..."
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                    className={cn(
                                        "pl-9 pr-4 py-2 rounded-lg",
                                        "bg-zinc-800 border border-zinc-700",
                                        "text-white placeholder-zinc-500",
                                        "focus:outline-none focus:border-purple-500",
                                        "text-sm w-64"
                                    )}
                                />
                            </div>
                            <Link prefetch={false} href="/admin/users">
                                <Button variant="outline" size="sm" className="border-zinc-700">
                                    Se alla
                                    <ChevronRight className="w-4 h-4 ml-1" />
                                </Button>
                            </Link>
                        </div>
                    </div>
                </div>

                {/* Users Table */}
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead>
                            <tr className="bg-zinc-800/50 border-b border-zinc-800">
                                <th className="px-4 py-3 text-left text-xs font-semibold text-zinc-400 uppercase">
                                    Användare
                                </th>
                                <th className="px-4 py-3 text-left text-xs font-semibold text-zinc-400 uppercase">
                                    Status
                                </th>
                                <th className="px-4 py-3 text-center text-xs font-semibold text-zinc-400 uppercase">
                                    Nivå
                                </th>
                                <th className="px-4 py-3 text-center text-xs font-semibold text-zinc-400 uppercase">
                                    XP
                                </th>
                                <th className="px-4 py-3 text-center text-xs font-semibold text-zinc-400 uppercase">
                                    Moduler
                                </th>
                                <th className="px-4 py-3 text-center text-xs font-semibold text-zinc-400 uppercase">
                                    Tasks
                                </th>
                                <th className="px-4 py-3 text-left text-xs font-semibold text-zinc-400 uppercase">
                                    Registrerad
                                </th>
                                <th className="px-4 py-3 text-center text-xs font-semibold text-zinc-400 uppercase">
                                    Åtgärd
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredUsers.map((u) => (
                                <UserRow
                                    key={u.id}
                                    user={u}
                                    onViewDetails={setSelectedUser}
                                />
                            ))}
                            {filteredUsers.length === 0 && (
                                <tr>
                                    <td colSpan={8} className="px-4 py-12 text-center">
                                        <UserPlus className="w-12 h-12 text-zinc-700 mx-auto mb-3" />
                                        <p className="text-zinc-500">
                                            {searchQuery ? "Inga användare matchar sökningen" : "Inga användare registrerade ännu"}
                                        </p>
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </motion.div>

            {/* Auto-refresh indicator */}
            <p className="mt-4 text-xs text-center text-zinc-600">
                Auto-uppdaterar var 30:e sekund
            </p>

            {/* User Detail Modal */}
            <AnimatePresence>
                {selectedUser && (
                    <UserDetailModal
                        user={selectedUser}
                        onClose={() => setSelectedUser(null)}
                    />
                )}
            </AnimatePresence>
        </div>
    )
}
