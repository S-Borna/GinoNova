"use client"

/**
 * ============================================================================
 * ADMIN COMMAND CENTER v2.0 — Full Control Dashboard
 * ============================================================================
 *
 * Complete admin dashboard with:
 * - Real-time user monitoring
 * - User management (view, edit, delete)
 * - AI Usage tracking
 * - Activity monitoring
 * - System controls
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
    Trash2,
    UserX,
    UserCheck,
    Brain,
    Sparkles,
    DollarSign,
    MessageSquare,
    Settings,
    ChevronDown,
    ChevronUp,
    X,
    Check,
    MoreVertical,
    Mail,
    Crown,
    Ban,
    Wifi,
    WifiOff,
} from "lucide-react"
import { Button } from "@/components/ui/button"

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
    is_active: boolean
    is_admin: boolean
    is_verified?: boolean
    created_at: string
    updated_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    current_streak?: number
    tasks_completed: number
    modules_completed: number
}

interface SystemStats {
    total_users: number
    active_users: number
    admin_users: number
    users_today: number
    users_this_week: number
    online_now: number
    active_today: number
    total_modules: number
    total_tasks: number
    database_status: string
}

interface AIUsageData {
    user_id: string
    email: string
    total_calls: number
    total_tokens: number
    total_cost_usd: number
}

interface ActivityEvent {
    type: string
    email: string
    name: string | null
    timestamp: string
    details: string
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function timeAgo(dateString: string | null): string {
    if (!dateString) return "Aldrig"
    const date = new Date(dateString)
    const now = new Date()
    const diffMs = now.getTime() - date.getTime()
    const diffMins = Math.floor(diffMs / 60000)
    const diffHours = Math.floor(diffMs / 3600000)
    const diffDays = Math.floor(diffMs / 86400000)

    if (diffMins < 1) return "Just nu"
    if (diffMins < 60) return `${diffMins} min sedan`
    if (diffHours < 24) return `${diffHours}h sedan`
    if (diffDays < 7) return `${diffDays}d sedan`
    return date.toLocaleDateString("sv-SE")
}

function formatDate(dateString: string): string {
    return new Date(dateString).toLocaleDateString("sv-SE", {
        year: "numeric",
        month: "short",
        day: "numeric",
    })
}

function isOnline(lastActivity: string | null): boolean {
    if (!lastActivity) return false
    const lastActive = new Date(lastActivity)
    const diffMs = Date.now() - lastActive.getTime()
    return diffMs < 30 * 60 * 1000 // 30 minutes
}

function isActiveToday(lastActivity: string | null): boolean {
    if (!lastActivity) return false
    const lastActive = new Date(lastActivity)
    const today = new Date()
    return lastActive.toDateString() === today.toDateString()
}

/* ============================================================================
   STAT CARD COMPONENT
   ============================================================================ */

function StatCard({ 
    icon: Icon, 
    label, 
    value, 
    subValue, 
    color,
    trend
}: { 
    icon: any
    label: string
    value: number | string
    subValue?: string
    color: string
    trend?: "up" | "down" | "neutral"
}) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative p-5 rounded-2xl overflow-hidden",
                "bg-zinc-900/50 border border-zinc-800/50",
                "hover:border-zinc-700/50 transition-all duration-300"
            )}
        >
            <div className={cn(
                "absolute top-0 right-0 w-32 h-32 rounded-full blur-3xl opacity-20",
                color
            )} />
            <div className="relative">
                <div className={cn(
                    "w-10 h-10 rounded-xl flex items-center justify-center mb-3",
                    color.replace("bg-", "bg-") + "/20"
                )}>
                    <Icon className={cn("w-5 h-5", color.replace("bg-", "text-"))} />
                </div>
                <p className="text-zinc-400 text-sm mb-1">{label}</p>
                <p className="text-2xl font-bold text-white">{value}</p>
                {subValue && (
                    <p className="text-xs text-zinc-500 mt-1">{subValue}</p>
                )}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   USER ROW COMPONENT
   ============================================================================ */

function UserRow({ 
    user, 
    aiUsage,
    onEdit, 
    onToggleActive,
    onDelete,
    isExpanded,
    onToggleExpand
}: { 
    user: AdminUser
    aiUsage?: AIUsageData
    onEdit: (user: AdminUser) => void
    onToggleActive: (user: AdminUser) => void
    onDelete: (user: AdminUser) => void
    isExpanded: boolean
    onToggleExpand: () => void
}) {
    const online = isOnline(user.last_activity_at)
    const activeToday = isActiveToday(user.last_activity_at)
    const initials = (user.full_name || user.email)
        .split(" ")
        .map(n => n[0])
        .join("")
        .substring(0, 2)
        .toUpperCase()

    return (
        <>
            <motion.tr 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className={cn(
                    "border-b border-zinc-800/50 hover:bg-zinc-800/30 transition-colors cursor-pointer",
                    isExpanded && "bg-zinc-800/30"
                )}
                onClick={onToggleExpand}
            >
                {/* User Info */}
                <td className="px-4 py-3">
                    <div className="flex items-center gap-3">
                        <div className="relative">
                            <div className={cn(
                                "w-10 h-10 rounded-full flex items-center justify-center text-sm font-medium",
                                user.is_admin 
                                    ? "bg-gradient-to-br from-amber-500 to-orange-600 text-white"
                                    : "bg-zinc-700 text-zinc-300"
                            )}>
                                {initials}
                            </div>
                            {/* Online indicator */}
                            <span className={cn(
                                "absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full border-2 border-zinc-900",
                                online ? "bg-emerald-500" : activeToday ? "bg-amber-500" : "bg-zinc-600"
                            )} />
                        </div>
                        <div>
                            <div className="flex items-center gap-2">
                                <span className="font-medium text-white">
                                    {user.full_name || "Unnamed"}
                                </span>
                                {user.is_admin && (
                                    <Crown className="w-4 h-4 text-amber-500" />
                                )}
                                {!user.is_active && (
                                    <Ban className="w-4 h-4 text-red-500" />
                                )}
                            </div>
                            <span className="text-sm text-zinc-500">{user.email}</span>
                        </div>
                    </div>
                </td>

                {/* Status */}
                <td className="px-4 py-3">
                    <div className="flex items-center gap-2">
                        {online ? (
                            <span className="flex items-center gap-1.5 px-2 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs">
                                <Wifi className="w-3 h-3" />
                                Online
                            </span>
                        ) : (
                            <span className="flex items-center gap-1.5 px-2 py-1 rounded-full bg-zinc-700/50 text-zinc-400 text-xs">
                                <WifiOff className="w-3 h-3" />
                                Offline
                            </span>
                        )}
                    </div>
                </td>

                {/* Last Activity */}
                <td className="px-4 py-3">
                    <span className={cn(
                        "text-sm",
                        online ? "text-emerald-400" : activeToday ? "text-amber-400" : "text-zinc-400"
                    )}>
                        {timeAgo(user.last_activity_at)}
                    </span>
                </td>

                {/* AI Usage */}
                <td className="px-4 py-3">
                    {aiUsage ? (
                        <div className="flex items-center gap-2">
                            <Brain className="w-4 h-4 text-purple-400" />
                            <span className="text-sm text-zinc-300">{aiUsage.total_calls}</span>
                            <span className="text-xs text-zinc-500">
                                (${aiUsage.total_cost_usd.toFixed(3)})
                            </span>
                        </div>
                    ) : (
                        <span className="text-sm text-zinc-600">—</span>
                    )}
                </td>

                {/* XP & Level */}
                <td className="px-4 py-3">
                    <div className="flex items-center gap-2">
                        <Zap className="w-4 h-4 text-amber-500" />
                        <span className="text-sm text-zinc-300">{user.total_xp} XP</span>
                        <span className="text-xs text-zinc-500">Lvl {user.level}</span>
                    </div>
                </td>

                {/* Registered */}
                <td className="px-4 py-3">
                    <span className="text-sm text-zinc-400">
                        {formatDate(user.created_at)}
                    </span>
                </td>

                {/* Actions */}
                <td className="px-4 py-3">
                    <div className="flex items-center gap-1">
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={(e) => { e.stopPropagation(); onEdit(user) }}
                            className="h-8 w-8 p-0 text-zinc-400 hover:text-white"
                        >
                            <Edit className="w-4 h-4" />
                        </Button>
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={(e) => { e.stopPropagation(); onToggleActive(user) }}
                            className={cn(
                                "h-8 w-8 p-0",
                                user.is_active 
                                    ? "text-amber-400 hover:text-amber-300" 
                                    : "text-emerald-400 hover:text-emerald-300"
                            )}
                        >
                            {user.is_active ? <UserX className="w-4 h-4" /> : <UserCheck className="w-4 h-4" />}
                        </Button>
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={(e) => { e.stopPropagation(); onDelete(user) }}
                            className="h-8 w-8 p-0 text-red-400 hover:text-red-300"
                        >
                            <Trash2 className="w-4 h-4" />
                        </Button>
                        <ChevronDown className={cn(
                            "w-4 h-4 text-zinc-500 transition-transform",
                            isExpanded && "rotate-180"
                        )} />
                    </div>
                </td>
            </motion.tr>

            {/* Expanded Details */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.tr
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                    >
                        <td colSpan={7} className="px-4 py-4 bg-zinc-800/20">
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                                <div className="p-3 rounded-lg bg-zinc-800/50">
                                    <p className="text-xs text-zinc-500 mb-1">Tasks Completed</p>
                                    <p className="text-lg font-semibold text-white">{user.tasks_completed}</p>
                                </div>
                                <div className="p-3 rounded-lg bg-zinc-800/50">
                                    <p className="text-xs text-zinc-500 mb-1">Modules Completed</p>
                                    <p className="text-lg font-semibold text-white">{user.modules_completed}</p>
                                </div>
                                <div className="p-3 rounded-lg bg-zinc-800/50">
                                    <p className="text-xs text-zinc-500 mb-1">Current Streak</p>
                                    <p className="text-lg font-semibold text-white">{user.current_streak || 0} 🔥</p>
                                </div>
                                <div className="p-3 rounded-lg bg-zinc-800/50">
                                    <p className="text-xs text-zinc-500 mb-1">AI Quiz Tokens</p>
                                    <p className="text-lg font-semibold text-white">
                                        {aiUsage?.total_tokens?.toLocaleString() || 0}
                                    </p>
                                </div>
                            </div>
                            <div className="mt-3 flex gap-2">
                                <Button size="sm" variant="outline" className="text-xs">
                                    <Mail className="w-3 h-3 mr-1" />
                                    Skicka mail
                                </Button>
                                <Button size="sm" variant="outline" className="text-xs">
                                    <Eye className="w-3 h-3 mr-1" />
                                    Visa profil
                                </Button>
                                <Button size="sm" variant="outline" className="text-xs">
                                    <BarChart3 className="w-3 h-3 mr-1" />
                                    Aktivitetslogg
                                </Button>
                            </div>
                        </td>
                    </motion.tr>
                )}
            </AnimatePresence>
        </>
    )
}

/* ============================================================================
   ACTIVITY FEED COMPONENT
   ============================================================================ */

function ActivityFeed({ events }: { events: ActivityEvent[] }) {
    const getEventIcon = (type: string) => {
        switch (type) {
            case "registration": return <UserPlus className="w-4 h-4 text-emerald-400" />
            case "login": return <Wifi className="w-4 h-4 text-blue-400" />
            case "progress": return <CheckCircle className="w-4 h-4 text-purple-400" />
            default: return <Activity className="w-4 h-4 text-zinc-400" />
        }
    }

    const getEventColor = (type: string) => {
        switch (type) {
            case "registration": return "border-l-emerald-500"
            case "login": return "border-l-blue-500"
            case "progress": return "border-l-purple-500"
            default: return "border-l-zinc-500"
        }
    }

    return (
        <div className="space-y-2 max-h-96 overflow-y-auto">
            {events.slice(0, 20).map((event, i) => (
                <motion.div
                    key={i}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: i * 0.05 }}
                    className={cn(
                        "p-3 rounded-lg bg-zinc-800/30 border-l-2",
                        getEventColor(event.type)
                    )}
                >
                    <div className="flex items-start gap-3">
                        <div className="mt-0.5">{getEventIcon(event.type)}</div>
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2">
                                <span className="font-medium text-white text-sm truncate">
                                    {event.name || event.email}
                                </span>
                                <span className="text-xs text-zinc-500">
                                    {timeAgo(event.timestamp)}
                                </span>
                            </div>
                            <p className="text-xs text-zinc-400 truncate">{event.details}</p>
                        </div>
                    </div>
                </motion.div>
            ))}
        </div>
    )
}

/* ============================================================================
   MAIN ADMIN PAGE
   ============================================================================ */

export default function AdminCommandCenter() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()
    
    const [users, setUsers] = useState<AdminUser[]>([])
    const [stats, setStats] = useState<SystemStats | null>(null)
    const [aiUsage, setAiUsage] = useState<AIUsageData[]>([])
    const [activityLog, setActivityLog] = useState<ActivityEvent[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [searchQuery, setSearchQuery] = useState("")
    const [expandedUserId, setExpandedUserId] = useState<string | null>(null)
    const [lastRefresh, setLastRefresh] = useState(new Date())
    const [filter, setFilter] = useState<"all" | "online" | "today" | "inactive">("all")

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    // Fetch all data
    const fetchData = useCallback(async () => {
        try {
            const token = getToken()
            if (!token) {
                setError("Du måste vara inloggad")
                setLoading(false)
                return
            }

            const headers = {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json"
            }

            // Fetch users
            const usersRes = await fetch(`${API_BASE_URL}/api/admin/users?per_page=100`, {
                headers,
                cache: 'no-store',
            })

            if (!usersRes.ok) {
                if (usersRes.status === 403) {
                    router.push("/dashboard")
                    return
                }
                throw new Error(`Kunde inte hämta användare: ${usersRes.status}`)
            }

            const usersData = await usersRes.json()
            setUsers(usersData.users || [])

            // Fetch stats
            try {
                const statsRes = await fetch(`${API_BASE_URL}/api/admin/stats`, { headers })
                if (statsRes.ok) {
                    setStats(await statsRes.json())
                }
            } catch (e) {
                console.error("Stats fetch failed:", e)
            }

            // Fetch AI usage
            try {
                const aiRes = await fetch(`${API_BASE_URL}/api/admin/ai-usage`, { headers })
                if (aiRes.ok) {
                    const aiData = await aiRes.json()
                    setAiUsage(aiData.users || [])
                }
            } catch (e) {
                console.error("AI usage fetch failed:", e)
            }

            // Fetch activity log
            try {
                const activityRes = await fetch(`${API_BASE_URL}/api/admin/activity-log?days=7`, { headers })
                if (activityRes.ok) {
                    const activityData = await activityRes.json()
                    setActivityLog(activityData.events || [])
                }
            } catch (e) {
                console.error("Activity log fetch failed:", e)
            }

            setError(null)
            setLastRefresh(new Date())
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
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

    // Filter users
    const filteredUsers = users.filter(u => {
        // Search filter
        if (searchQuery) {
            const query = searchQuery.toLowerCase()
            if (!u.email.toLowerCase().includes(query) && 
                !(u.full_name?.toLowerCase().includes(query))) {
                return false
            }
        }
        
        // Status filter
        switch (filter) {
            case "online":
                return isOnline(u.last_activity_at)
            case "today":
                return isActiveToday(u.last_activity_at)
            case "inactive":
                return !u.is_active
            default:
                return true
        }
    }).sort((a, b) => {
        const aTime = a.last_activity_at ? new Date(a.last_activity_at).getTime() : 0
        const bTime = b.last_activity_at ? new Date(b.last_activity_at).getTime() : 0
        return bTime - aTime
    })

    // Get AI usage for a user
    const getUserAiUsage = (userId: string) => {
        return aiUsage.find(u => u.user_id === userId)
    }

    // Actions
    const handleEdit = (user: AdminUser) => {
        router.push(`/admin/users/${user.id}`)
    }

    const handleToggleActive = async (targetUser: AdminUser) => {
        if (!confirm(`${targetUser.is_active ? "Inaktivera" : "Aktivera"} ${targetUser.email}?`)) return
        
        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}`, {
                method: "PATCH",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ is_active: !targetUser.is_active })
            })
            
            if (res.ok) {
                fetchData()
            }
        } catch (e) {
            console.error("Toggle active failed:", e)
        }
    }

    const handleDelete = async (targetUser: AdminUser) => {
        if (!confirm(`VARNING: Ta bort ${targetUser.email} permanent?`)) return
        if (!confirm("Är du HELT säker? Detta går inte att ångra!")) return
        
        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}?hard_delete=true`, {
                method: "DELETE",
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            })
            
            if (res.ok) {
                fetchData()
            }
        } catch (e) {
            console.error("Delete failed:", e)
        }
    }

    // Loading state
    if (authLoading || loading) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <div className="text-center">
                    <Loader2 className="w-12 h-12 text-purple-500 animate-spin mx-auto mb-4" />
                    <p className="text-zinc-400">Laddar Admin Command Center...</p>
                </div>
            </div>
        )
    }

    // Error state
    if (error) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center p-6">
                <div className="text-center max-w-md">
                    <AlertCircle className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-white mb-2">Fel</h1>
                    <p className="text-zinc-400 mb-6">{error}</p>
                    <Button onClick={() => { setError(null); setLoading(true); fetchData() }}>
                        <RefreshCw className="w-4 h-4 mr-2" />
                        Försök igen
                    </Button>
                </div>
            </div>
        )
    }

    // Calculate totals
    const totalAICost = aiUsage.reduce((sum, u) => sum + u.total_cost_usd, 0)
    const totalAICalls = aiUsage.reduce((sum, u) => sum + u.total_calls, 0)
    const onlineCount = users.filter(u => isOnline(u.last_activity_at)).length

    return (
        <div className="min-h-screen bg-zinc-950 p-4 md:p-8">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                <div className="flex items-center gap-4">
                    <div className={cn(
                        "w-14 h-14 rounded-2xl flex items-center justify-center",
                        "bg-gradient-to-br from-purple-600 to-indigo-600",
                        "shadow-lg shadow-purple-500/25"
                    )}>
                        <Shield className="w-7 h-7 text-white" />
                    </div>
                    <div>
                        <h1 className="text-2xl font-bold text-white">Admin Command Center</h1>
                        <p className="text-zinc-400">Full kontroll över GinoNova</p>
                    </div>
                </div>
                <div className="flex items-center gap-3">
                    <span className="text-xs text-zinc-500">
                        Uppdaterad: {lastRefresh.toLocaleTimeString("sv-SE")}
                    </span>
                    <Button variant="outline" size="sm" onClick={fetchData} className="border-zinc-700">
                        <RefreshCw className="w-4 h-4 mr-2" />
                        Uppdatera
                    </Button>
                </div>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4 mb-8">
                <StatCard
                    icon={Users}
                    label="Totalt användare"
                    value={stats?.total_users || users.length}
                    subValue={`${stats?.users_this_week || 0} denna vecka`}
                    color="bg-blue-500"
                />
                <StatCard
                    icon={Globe}
                    label="Online nu"
                    value={onlineCount}
                    subValue={`${stats?.active_today || 0} aktiva idag`}
                    color="bg-emerald-500"
                />
                <StatCard
                    icon={UserPlus}
                    label="Nya idag"
                    value={stats?.users_today || 0}
                    color="bg-cyan-500"
                />
                <StatCard
                    icon={Brain}
                    label="AI Quiz Anrop"
                    value={totalAICalls}
                    subValue={`$${totalAICost.toFixed(2)} kostnad`}
                    color="bg-purple-500"
                />
                <StatCard
                    icon={BookOpen}
                    label="Moduler"
                    value={stats?.total_modules || 0}
                    color="bg-amber-500"
                />
                <StatCard
                    icon={Database}
                    label="Databas"
                    value={stats?.database_status === "postgres" ? "Online" : "Memory"}
                    color="bg-green-500"
                />
            </div>

            {/* Main Content Grid */}
            <div className="grid lg:grid-cols-4 gap-6">
                {/* User Table - 3 columns */}
                <div className="lg:col-span-3">
                    <div className="rounded-2xl bg-zinc-900/50 border border-zinc-800/50 overflow-hidden">
                        {/* Table Header */}
                        <div className="p-4 border-b border-zinc-800/50">
                            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                                <div className="flex items-center gap-3">
                                    <Users className="w-5 h-5 text-purple-400" />
                                    <h2 className="text-lg font-semibold text-white">
                                        Användare ({filteredUsers.length})
                                    </h2>
                                </div>
                                <div className="flex items-center gap-3">
                                    {/* Search */}
                                    <div className="relative">
                                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                                        <input
                                            type="text"
                                            placeholder="Sök..."
                                            value={searchQuery}
                                            onChange={(e) => setSearchQuery(e.target.value)}
                                            className="pl-9 pr-4 py-2 rounded-lg bg-zinc-800 border border-zinc-700 text-white text-sm placeholder-zinc-500 focus:outline-none focus:border-purple-500 w-48"
                                        />
                                    </div>
                                    {/* Filter */}
                                    <select
                                        value={filter}
                                        onChange={(e) => setFilter(e.target.value as any)}
                                        className="px-3 py-2 rounded-lg bg-zinc-800 border border-zinc-700 text-white text-sm focus:outline-none focus:border-purple-500"
                                    >
                                        <option value="all">Alla</option>
                                        <option value="online">Online</option>
                                        <option value="today">Aktiva idag</option>
                                        <option value="inactive">Inaktiverade</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        {/* Table */}
                        <div className="overflow-x-auto">
                            <table className="w-full">
                                <thead>
                                    <tr className="border-b border-zinc-800/50 text-left">
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">Användare</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">Status</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">Senast aktiv</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">AI Quiz</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">XP</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">Registrerad</th>
                                        <th className="px-4 py-3 text-xs font-medium text-zinc-500 uppercase">Åtgärder</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {filteredUsers.map((u) => (
                                        <UserRow
                                            key={u.id}
                                            user={u}
                                            aiUsage={getUserAiUsage(u.id)}
                                            onEdit={handleEdit}
                                            onToggleActive={handleToggleActive}
                                            onDelete={handleDelete}
                                            isExpanded={expandedUserId === u.id}
                                            onToggleExpand={() => setExpandedUserId(
                                                expandedUserId === u.id ? null : u.id
                                            )}
                                        />
                                    ))}
                                </tbody>
                            </table>
                        </div>

                        {filteredUsers.length === 0 && (
                            <div className="p-8 text-center text-zinc-500">
                                Inga användare hittades
                            </div>
                        )}
                    </div>
                </div>

                {/* Sidebar - Activity Feed */}
                <div className="lg:col-span-1">
                    <div className="rounded-2xl bg-zinc-900/50 border border-zinc-800/50 p-4">
                        <div className="flex items-center gap-2 mb-4">
                            <Activity className="w-5 h-5 text-purple-400" />
                            <h2 className="text-lg font-semibold text-white">Aktivitet</h2>
                        </div>
                        <ActivityFeed events={activityLog} />
                    </div>

                    {/* Quick Actions */}
                    <div className="mt-6 rounded-2xl bg-zinc-900/50 border border-zinc-800/50 p-4">
                        <h2 className="text-lg font-semibold text-white mb-4">Snabbåtgärder</h2>
                        <div className="space-y-2">
                            <Button 
                                variant="outline" 
                                className="w-full justify-start text-left border-zinc-700"
                                onClick={() => router.push("/admin/analytics")}
                            >
                                <BarChart3 className="w-4 h-4 mr-2 text-purple-400" />
                                AI Analytics
                            </Button>
                            <Button 
                                variant="outline" 
                                className="w-full justify-start text-left border-zinc-700"
                                onClick={() => router.push("/admin/content")}
                            >
                                <BookOpen className="w-4 h-4 mr-2 text-amber-400" />
                                Innehåll
                            </Button>
                            <Button 
                                variant="outline" 
                                className="w-full justify-start text-left border-zinc-700"
                                onClick={() => router.push("/admin/permissions")}
                            >
                                <Shield className="w-4 h-4 mr-2 text-emerald-400" />
                                Rättigheter
                            </Button>
                        </div>
                    </div>

                    {/* AI Usage Summary */}
                    <div className="mt-6 rounded-2xl bg-gradient-to-br from-purple-900/30 to-indigo-900/20 border border-purple-500/20 p-4">
                        <div className="flex items-center gap-2 mb-4">
                            <Brain className="w-5 h-5 text-purple-400" />
                            <h2 className="text-lg font-semibold text-white">AI Quiz Användning</h2>
                        </div>
                        <div className="space-y-3">
                            <div className="flex justify-between">
                                <span className="text-zinc-400">Totala anrop</span>
                                <span className="text-white font-medium">{totalAICalls.toLocaleString()}</span>
                            </div>
                            <div className="flex justify-between">
                                <span className="text-zinc-400">Total kostnad</span>
                                <span className="text-emerald-400 font-medium">${totalAICost.toFixed(2)}</span>
                            </div>
                            <div className="flex justify-between">
                                <span className="text-zinc-400">Användare</span>
                                <span className="text-white font-medium">{aiUsage.length}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
