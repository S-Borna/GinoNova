"use client"

/**
 * Admin Panel v2 - Clean Rebuild
 * Real-time user monitoring with activity tracking
 */

import { useEffect, useState, useCallback } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Users,
    Shield,
    Loader2,
    Search,
    RefreshCw,
    AlertCircle,
    Trash2,
    UserX,
    UserCheck,
    MoreHorizontal,
    Clock,
    Calendar,
    Zap,
    Activity,
    Eye,
    Mail,
    CheckCircle,
    XCircle,
    CircleDot,
} from "lucide-react"
import { Button } from "@/components/ui/button"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || ""
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

// Types
interface User {
    id: string
    email: string
    full_name: string | null
    is_active: boolean
    is_admin: boolean
    is_verified: boolean
    total_xp: number
    tasks_completed: number
    created_at: string
    updated_at: string
    last_activity_at: string | null
}

interface Stats {
    total_users: number
    active_users: number
    online_now: number
    active_today: number
    users_this_week: number
}

// Helper functions
function formatTimeAgo(date: string | null): string {
    if (!date) return "Aldrig"
    
    const now = Date.now()
    const then = new Date(date).getTime()
    const diff = now - then
    
    const mins = Math.floor(diff / 60000)
    const hours = Math.floor(diff / 3600000)
    const days = Math.floor(diff / 86400000)
    
    if (mins < 1) return "Just nu"
    if (mins < 60) return `${mins} min sedan`
    if (hours < 24) return `${hours}h sedan`
    if (days < 7) return `${days}d sedan`
    if (days < 30) return `${Math.floor(days / 7)}v sedan`
    return new Date(date).toLocaleDateString("sv-SE")
}

function formatDate(date: string): string {
    return new Date(date).toLocaleDateString("sv-SE", {
        year: "numeric",
        month: "short",
        day: "numeric"
    })
}

function isOnline(date: string | null): boolean {
    if (!date) return false
    // Online if active within last 10 minutes
    return (Date.now() - new Date(date).getTime()) < 10 * 60 * 1000
}

function isActiveToday(date: string | null): boolean {
    if (!date) return false
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    return new Date(date).getTime() >= today.getTime()
}

// Online Status Indicator
function OnlineStatus({ lastActivity }: { lastActivity: string | null }) {
    const online = isOnline(lastActivity)
    const activeToday = isActiveToday(lastActivity)
    
    if (online) {
        return (
            <div className="flex items-center gap-1.5">
                <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                <span className="text-xs text-green-400">Online</span>
            </div>
        )
    }
    
    if (activeToday) {
        return (
            <div className="flex items-center gap-1.5">
                <div className="w-2 h-2 rounded-full bg-yellow-500" />
                <span className="text-xs text-yellow-400">Aktiv idag</span>
            </div>
        )
    }
    
    return (
        <div className="flex items-center gap-1.5">
            <div className="w-2 h-2 rounded-full bg-zinc-600" />
            <span className="text-xs text-zinc-500">Offline</span>
        </div>
    )
}

// Stat Card Component
function StatCard({ 
    icon: Icon, 
    value, 
    label, 
    color = "blue" 
}: { 
    icon: React.ElementType
    value: number | string
    label: string
    color?: "blue" | "green" | "yellow" | "purple"
}) {
    const colors = {
        blue: "text-blue-400 bg-blue-500/10",
        green: "text-green-400 bg-green-500/10",
        yellow: "text-yellow-400 bg-yellow-500/10",
        purple: "text-purple-400 bg-purple-500/10",
    }
    
    return (
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800">
            <div className="flex items-center gap-3">
                <div className={cn("w-10 h-10 rounded-lg flex items-center justify-center", colors[color])}>
                    <Icon className="w-5 h-5" />
                </div>
                <div>
                    <p className="text-2xl font-bold text-white">{value}</p>
                    <p className="text-xs text-zinc-500">{label}</p>
                </div>
            </div>
        </div>
    )
}

// User Row Component
function UserRow({ 
    user, 
    onToggleActive,
    onDelete,
}: { 
    user: User
    onToggleActive: () => void
    onDelete: () => void
}) {
    const [showMenu, setShowMenu] = useState(false)
    const online = isOnline(user.last_activity_at)
    
    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "p-4 rounded-xl border transition-all",
                "bg-zinc-900/50 border-zinc-800 hover:border-zinc-700",
                !user.is_active && "opacity-50"
            )}
        >
            <div className="flex items-center gap-4">
                {/* Avatar */}
                <div className="relative">
                    <div className={cn(
                        "w-12 h-12 rounded-xl flex items-center justify-center text-lg font-bold",
                        user.is_admin 
                            ? "bg-gradient-to-br from-purple-500 to-pink-500 text-white"
                            : "bg-zinc-800 text-zinc-400"
                    )}>
                        {user.full_name?.[0]?.toUpperCase() || user.email[0].toUpperCase()}
                    </div>
                    {/* Online indicator */}
                    <div className={cn(
                        "absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full border-2 border-zinc-900",
                        online ? "bg-green-500" : "bg-zinc-600"
                    )} />
                </div>
                
                {/* User Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                        <h3 className="font-medium text-white truncate">
                            {user.full_name || "Inget namn"}
                        </h3>
                        {user.is_admin && (
                            <span className="px-1.5 py-0.5 text-[10px] font-bold bg-purple-500/20 text-purple-400 rounded">
                                ADMIN
                            </span>
                        )}
                        {!user.is_active && (
                            <span className="px-1.5 py-0.5 text-[10px] font-bold bg-red-500/20 text-red-400 rounded">
                                INAKTIV
                            </span>
                        )}
                    </div>
                    <p className="text-sm text-zinc-500 truncate">{user.email}</p>
                </div>
                
                {/* Activity Info */}
                <div className="hidden md:flex items-center gap-6 text-sm">
                    {/* Online Status */}
                    <div className="w-24">
                        <OnlineStatus lastActivity={user.last_activity_at} />
                    </div>
                    
                    {/* Last Active */}
                    <div className="w-28 text-right">
                        <p className="text-zinc-400">{formatTimeAgo(user.last_activity_at)}</p>
                        <p className="text-[10px] text-zinc-600">Senast aktiv</p>
                    </div>
                    
                    {/* Created */}
                    <div className="w-28 text-right">
                        <p className="text-zinc-400">{formatDate(user.created_at)}</p>
                        <p className="text-[10px] text-zinc-600">Registrerad</p>
                    </div>
                    
                    {/* Stats */}
                    <div className="w-16 text-right">
                        <p className="text-zinc-400">{user.total_xp}</p>
                        <p className="text-[10px] text-zinc-600">XP</p>
                    </div>
                    
                    <div className="w-16 text-right">
                        <p className="text-zinc-400">{user.tasks_completed}</p>
                        <p className="text-[10px] text-zinc-600">Tasks</p>
                    </div>
                </div>
                
                {/* Actions */}
                <div className="relative">
                    <button 
                        onClick={() => setShowMenu(!showMenu)}
                        className="p-2 rounded-lg hover:bg-zinc-800 text-zinc-400 hover:text-white transition-colors"
                    >
                        <MoreHorizontal className="w-5 h-5" />
                    </button>
                    
                    <AnimatePresence>
                        {showMenu && (
                            <>
                                <div 
                                    className="fixed inset-0 z-10" 
                                    onClick={() => setShowMenu(false)} 
                                />
                                <motion.div
                                    initial={{ opacity: 0, scale: 0.95 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    exit={{ opacity: 0, scale: 0.95 }}
                                    className="absolute right-0 top-full mt-1 w-48 py-1 bg-zinc-900 border border-zinc-800 rounded-xl shadow-xl z-20"
                                >
                                    <button
                                        onClick={() => { onToggleActive(); setShowMenu(false) }}
                                        className="w-full px-4 py-2 text-left text-sm hover:bg-zinc-800 flex items-center gap-2"
                                    >
                                        {user.is_active ? (
                                            <>
                                                <UserX className="w-4 h-4 text-yellow-400" />
                                                <span className="text-yellow-400">Inaktivera</span>
                                            </>
                                        ) : (
                                            <>
                                                <UserCheck className="w-4 h-4 text-green-400" />
                                                <span className="text-green-400">Aktivera</span>
                                            </>
                                        )}
                                    </button>
                                    <button
                                        onClick={() => { onDelete(); setShowMenu(false) }}
                                        className="w-full px-4 py-2 text-left text-sm text-red-400 hover:bg-zinc-800 flex items-center gap-2"
                                    >
                                        <Trash2 className="w-4 h-4" />
                                        Ta bort
                                    </button>
                                </motion.div>
                            </>
                        )}
                    </AnimatePresence>
                </div>
            </div>
            
            {/* Mobile Activity Info */}
            <div className="md:hidden mt-3 pt-3 border-t border-zinc-800 grid grid-cols-2 gap-2 text-xs">
                <div>
                    <OnlineStatus lastActivity={user.last_activity_at} />
                </div>
                <div className="text-right text-zinc-500">
                    Senast: {formatTimeAgo(user.last_activity_at)}
                </div>
                <div className="text-zinc-500">
                    Registrerad: {formatDate(user.created_at)}
                </div>
                <div className="text-right text-zinc-500">
                    {user.total_xp} XP • {user.tasks_completed} tasks
                </div>
            </div>
        </motion.div>
    )
}

// Main Admin Page
export default function AdminPage() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()
    
    const [users, setUsers] = useState<User[]>([])
    const [stats, setStats] = useState<Stats | null>(null)
    const [loading, setLoading] = useState(true)
    const [refreshing, setRefreshing] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [search, setSearch] = useState("")
    const [filter, setFilter] = useState<"all" | "online" | "active-today" | "inactive">("all")
    const [lastRefresh, setLastRefresh] = useState<Date>(new Date())

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    const fetchData = useCallback(async (showRefreshing = false) => {
        if (showRefreshing) setRefreshing(true)
        
        try {
            const token = getToken()
            if (!token) {
                setError("Inte inloggad")
                setLoading(false)
                return
            }

            const headers = { Authorization: `Bearer ${token}` }

            // Fetch users with cache busting
            const usersRes = await fetch(
                `${API_BASE_URL}/api/admin/users?per_page=100&_t=${Date.now()}`, 
                { headers, cache: 'no-store' }
            )
            
            if (usersRes.status === 403) {
                router.push("/dashboard")
                return
            }
            
            if (!usersRes.ok) throw new Error(`API error: ${usersRes.status}`)
            
            const data = await usersRes.json()
            setUsers(data.users || [])

            // Fetch stats
            try {
                const statsRes = await fetch(
                    `${API_BASE_URL}/api/admin/stats?_t=${Date.now()}`, 
                    { headers, cache: 'no-store' }
                )
                if (statsRes.ok) {
                    setStats(await statsRes.json())
                }
            } catch (e) {
                console.warn("Stats fetch failed:", e)
            }

            setError(null)
            setLastRefresh(new Date())
        } catch (err) {
            console.error("Admin fetch error:", err)
            setError(err instanceof Error ? err.message : "Kunde inte ladda data")
        } finally {
            setLoading(false)
            setRefreshing(false)
        }
    }, [router])

    useEffect(() => {
        if (authLoading) return
        if (!user || !isAdmin) {
            router.push("/dashboard")
            return
        }
        fetchData()
        // Auto-refresh every 10 seconds
        const interval = setInterval(() => fetchData(false), 10000)
        return () => clearInterval(interval)
    }, [user, authLoading, isAdmin, router, fetchData])

    // Toggle user active status
    const toggleUserActive = async (targetUser: User) => {
        try {
            const token = getToken()
            await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}`, {
                method: "PUT",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ is_active: !targetUser.is_active }),
            })
            fetchData(true)
        } catch (err) {
            console.error("Toggle active error:", err)
        }
    }

    // Delete user
    const deleteUser = async (targetUser: User) => {
        if (!confirm(`Vill du verkligen ta bort ${targetUser.email}?`)) return
        
        try {
            const token = getToken()
            await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}?hard_delete=true`, {
                method: "DELETE",
                headers: { Authorization: `Bearer ${token}` },
            })
            fetchData(true)
        } catch (err) {
            console.error("Delete user error:", err)
        }
    }

    // Filter users
    const filteredUsers = users
        .filter(u => {
            if (filter === "online") return isOnline(u.last_activity_at)
            if (filter === "active-today") return isActiveToday(u.last_activity_at)
            if (filter === "inactive") return !u.is_active
            return true
        })
        .filter(u => {
            if (!search) return true
            const q = search.toLowerCase()
            return u.email.toLowerCase().includes(q) || 
                   (u.full_name?.toLowerCase().includes(q))
        })
        .sort((a, b) => {
            // Online users first, then by last activity
            const aOnline = isOnline(a.last_activity_at)
            const bOnline = isOnline(b.last_activity_at)
            if (aOnline !== bOnline) return bOnline ? 1 : -1
            
            const aTime = a.last_activity_at ? new Date(a.last_activity_at).getTime() : 0
            const bTime = b.last_activity_at ? new Date(b.last_activity_at).getTime() : 0
            return bTime - aTime
        })

    // Calculate real-time stats from users
    const onlineCount = users.filter(u => isOnline(u.last_activity_at)).length
    const activeTodayCount = users.filter(u => isActiveToday(u.last_activity_at)).length

    // Loading state
    if (loading || authLoading) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <Loader2 className="w-8 h-8 text-purple-500 animate-spin" />
            </div>
        )
    }

    // Error state
    if (error) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center p-6">
                <div className="text-center">
                    <AlertCircle className="w-12 h-12 text-red-400 mx-auto mb-4" />
                    <p className="text-white mb-4">{error}</p>
                    <Button onClick={() => fetchData(true)}>Försök igen</Button>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-zinc-950">
            {/* Header */}
            <div className="border-b border-zinc-800 bg-zinc-900/50">
                <div className="max-w-6xl mx-auto px-4 py-6">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            <div className="w-10 h-10 rounded-xl bg-purple-600 flex items-center justify-center">
                                <Shield className="w-5 h-5 text-white" />
                            </div>
                            <div>
                                <h1 className="text-xl font-bold text-white">Admin</h1>
                                <p className="text-sm text-zinc-500">{users.length} användare</p>
                            </div>
                        </div>
                        <div className="flex items-center gap-3">
                            <span className="text-xs text-zinc-600">
                                Uppdaterad {lastRefresh.toLocaleTimeString("sv-SE")}
                            </span>
                            <Button 
                                variant="outline" 
                                size="sm" 
                                onClick={() => fetchData(true)}
                                disabled={refreshing}
                                className="border-zinc-700"
                            >
                                <RefreshCw className={cn("w-4 h-4 mr-2", refreshing && "animate-spin")} />
                                {refreshing ? "Laddar..." : "Uppdatera"}
                            </Button>
                        </div>
                    </div>
                </div>
            </div>

            <div className="max-w-6xl mx-auto px-4 py-6">
                {/* Stats */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
                    <StatCard 
                        icon={Users} 
                        value={users.length} 
                        label="Totalt" 
                        color="blue" 
                    />
                    <StatCard 
                        icon={CircleDot} 
                        value={onlineCount} 
                        label="Online nu" 
                        color="green" 
                    />
                    <StatCard 
                        icon={Activity} 
                        value={activeTodayCount} 
                        label="Aktiva idag" 
                        color="yellow" 
                    />
                    <StatCard 
                        icon={Calendar} 
                        value={stats?.users_this_week || 0} 
                        label="Nya denna vecka" 
                        color="purple" 
                    />
                </div>

                {/* Future: Email Verification Info */}
                <div className="mb-6 p-4 rounded-xl bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20">
                    <div className="flex items-start gap-3">
                        <Mail className="w-5 h-5 text-blue-400 mt-0.5" />
                        <div>
                            <h3 className="font-medium text-white">Kommande: E-postverifiering</h3>
                            <p className="text-sm text-zinc-400 mt-1">
                                För att minska lösdrivarkonton planeras e-postverifiering där nya användare 
                                måste bekräfta sin e-post innan de får full tillgång. Verifierade användare 
                                visas med <CheckCircle className="w-3.5 h-3.5 inline text-green-400" /> och 
                                overifierade med <XCircle className="w-3.5 h-3.5 inline text-yellow-400" />.
                            </p>
                        </div>
                    </div>
                </div>

                {/* Search & Filter */}
                <div className="flex flex-col sm:flex-row gap-3 mb-6">
                    <div className="relative flex-1">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                        <input
                            type="text"
                            placeholder="Sök användare..."
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-zinc-900 border border-zinc-800 text-white placeholder-zinc-500 focus:outline-none focus:border-purple-500"
                        />
                    </div>
                    <div className="flex gap-2">
                        {[
                            { key: "all", label: "Alla" },
                            { key: "online", label: "Online", count: onlineCount },
                            { key: "active-today", label: "Idag", count: activeTodayCount },
                            { key: "inactive", label: "Inaktiva" },
                        ].map((f) => (
                            <button
                                key={f.key}
                                onClick={() => setFilter(f.key as typeof filter)}
                                className={cn(
                                    "px-4 py-2 rounded-xl text-sm font-medium transition-all",
                                    filter === f.key
                                        ? "bg-purple-600 text-white"
                                        : "bg-zinc-900 text-zinc-400 hover:text-white border border-zinc-800"
                                )}
                            >
                                {f.label}
                                {f.count !== undefined && f.count > 0 && (
                                    <span className="ml-1.5 px-1.5 py-0.5 text-[10px] bg-white/20 rounded">
                                        {f.count}
                                    </span>
                                )}
                            </button>
                        ))}
                    </div>
                </div>

                {/* User List */}
                <div className="space-y-3">
                    {filteredUsers.length === 0 ? (
                        <div className="text-center py-12 text-zinc-500">
                            <Users className="w-12 h-12 mx-auto mb-4 opacity-50" />
                            <p>Inga användare hittades</p>
                        </div>
                    ) : (
                        filteredUsers.map((u) => (
                            <UserRow 
                                key={u.id} 
                                user={u}
                                onToggleActive={() => toggleUserActive(u)}
                                onDelete={() => deleteUser(u)}
                            />
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}
