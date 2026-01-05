"use client"

/**
 * Admin Page - Simple & Clean
 * Fokus på användarvänlighet och enkelhet
 */

import { useEffect, useState, useCallback } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { motion } from "framer-motion"
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
    Brain,
    Crown,
    MoreHorizontal,
    ChevronRight,
    Clock,
    Calendar,
    Zap,
    CheckCircle,
    XCircle,
} from "lucide-react"
import { Button } from "@/components/ui/button"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface User {
    id: string
    full_name: string | null
    email: string
    is_active: boolean
    is_admin: boolean
    created_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    tasks_completed: number
}

interface Stats {
    total_users: number
    online_now: number
    active_today: number
    users_this_week: number
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function timeAgo(date: string | null): string {
    if (!date) return "Aldrig"
    const now = new Date()
    const then = new Date(date)
    const diff = now.getTime() - then.getTime()
    const mins = Math.floor(diff / 60000)
    const hours = Math.floor(diff / 3600000)
    const days = Math.floor(diff / 86400000)
    
    if (mins < 1) return "Just nu"
    if (mins < 60) return `${mins}m sedan`
    if (hours < 24) return `${hours}h sedan`
    if (days < 7) return `${days}d sedan`
    return then.toLocaleDateString("sv-SE", { day: "numeric", month: "short" })
}

function isOnline(date: string | null): boolean {
    if (!date) return false
    // Online = aktivitet inom 10 minuter (heartbeat skickas var 5:e minut)
    return (Date.now() - new Date(date).getTime()) < 10 * 60 * 1000
}

/* ============================================================================
   USER CARD COMPONENT
   ============================================================================ */

function UserCard({ 
    user, 
    onToggleActive, 
    onDelete,
    onViewDetails 
}: { 
    user: User
    onToggleActive: () => void
    onDelete: () => void
    onViewDetails: () => void
}) {
    const online = isOnline(user.last_activity_at)
    const [showMenu, setShowMenu] = useState(false)
    
    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "p-4 rounded-xl border transition-all",
                "bg-zinc-900/50 hover:bg-zinc-800/50",
                user.is_active ? "border-zinc-800" : "border-red-900/50 bg-red-950/20"
            )}
        >
            <div className="flex items-center gap-4">
                {/* Avatar */}
                <div className="relative">
                    <div className={cn(
                        "w-12 h-12 rounded-full flex items-center justify-center text-lg font-bold",
                        user.is_admin 
                            ? "bg-gradient-to-br from-amber-500 to-orange-600" 
                            : "bg-zinc-700"
                    )}>
                        {(user.full_name || user.email)[0].toUpperCase()}
                    </div>
                    {/* Online indicator */}
                    <div className={cn(
                        "absolute -bottom-0.5 -right-0.5 w-4 h-4 rounded-full border-2 border-zinc-900",
                        online ? "bg-green-500" : "bg-zinc-600"
                    )} />
                </div>

                {/* Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                        <h3 className="font-medium text-white truncate">
                            {user.full_name || "Namnlös"}
                        </h3>
                        {user.is_admin && <Crown className="w-4 h-4 text-amber-500 flex-shrink-0" />}
                        {!user.is_active && (
                            <span className="px-1.5 py-0.5 text-[10px] font-medium bg-red-500/20 text-red-400 rounded">
                                INAKTIV
                            </span>
                        )}
                    </div>
                    <p className="text-sm text-zinc-500 truncate">{user.email}</p>
                </div>

                {/* Quick Stats */}
                <div className="hidden md:flex items-center gap-6 text-sm">
                    <div className="text-center">
                        <p className={cn(
                            "font-medium",
                            online ? "text-green-400" : "text-zinc-400"
                        )}>
                            {timeAgo(user.last_activity_at)}
                        </p>
                        <p className="text-xs text-zinc-600">Senast aktiv</p>
                    </div>
                    <div className="text-center">
                        <p className="font-medium text-white">{user.total_xp}</p>
                        <p className="text-xs text-zinc-600">XP</p>
                    </div>
                    <div className="text-center">
                        <p className="font-medium text-white">{user.tasks_completed}</p>
                        <p className="text-xs text-zinc-600">Tasks</p>
                    </div>
                </div>

                {/* Actions Menu */}
                <div className="relative">
                    <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => setShowMenu(!showMenu)}
                        className="h-9 w-9 p-0"
                    >
                        <MoreHorizontal className="w-5 h-5 text-zinc-400" />
                    </Button>

                    {showMenu && (
                        <>
                            <div 
                                className="fixed inset-0 z-10" 
                                onClick={() => setShowMenu(false)} 
                            />
                            <div className="absolute right-0 top-full mt-1 z-20 w-48 rounded-lg bg-zinc-800 border border-zinc-700 shadow-xl py-1">
                                <button
                                    onClick={() => { onViewDetails(); setShowMenu(false) }}
                                    className="w-full px-4 py-2 text-left text-sm text-zinc-300 hover:bg-zinc-700 flex items-center gap-2"
                                >
                                    <ChevronRight className="w-4 h-4" />
                                    Visa detaljer
                                </button>
                                <button
                                    onClick={() => { onToggleActive(); setShowMenu(false) }}
                                    className={cn(
                                        "w-full px-4 py-2 text-left text-sm flex items-center gap-2",
                                        user.is_active 
                                            ? "text-amber-400 hover:bg-amber-500/10" 
                                            : "text-green-400 hover:bg-green-500/10"
                                    )}
                                >
                                    {user.is_active ? (
                                        <>
                                            <UserX className="w-4 h-4" />
                                            Inaktivera
                                        </>
                                    ) : (
                                        <>
                                            <UserCheck className="w-4 h-4" />
                                            Aktivera
                                        </>
                                    )}
                                </button>
                                <button
                                    onClick={() => { onDelete(); setShowMenu(false) }}
                                    className="w-full px-4 py-2 text-left text-sm text-red-400 hover:bg-red-500/10 flex items-center gap-2"
                                >
                                    <Trash2 className="w-4 h-4" />
                                    Ta bort permanent
                                </button>
                            </div>
                        </>
                    )}
                </div>
            </div>

            {/* Mobile Stats */}
            <div className="md:hidden flex items-center gap-4 mt-3 pt-3 border-t border-zinc-800 text-xs">
                <span className={online ? "text-green-400" : "text-zinc-500"}>
                    {timeAgo(user.last_activity_at)}
                </span>
                <span className="text-zinc-500">{user.total_xp} XP</span>
                <span className="text-zinc-500">{user.tasks_completed} tasks</span>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function AdminPage() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()
    
    const [users, setUsers] = useState<User[]>([])
    const [stats, setStats] = useState<Stats | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [search, setSearch] = useState("")
    const [filter, setFilter] = useState<"all" | "online" | "inactive">("all")

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    const fetchData = useCallback(async () => {
        try {
            const token = getToken()
            if (!token) {
                setError("Inte inloggad")
                setLoading(false)
                return
            }

            const headers = { Authorization: `Bearer ${token}` }

            // Fetch users
            const usersRes = await fetch(`${API_BASE_URL}/api/admin/users?per_page=100`, { headers })
            
            if (usersRes.status === 403) {
                router.push("/dashboard")
                return
            }
            
            if (!usersRes.ok) {
                const errorText = await usersRes.text()
                console.error("Admin users error:", usersRes.status, errorText)
                throw new Error(`API error: ${usersRes.status}`)
            }
            
            const data = await usersRes.json()
            setUsers(data.users || [])

            // Fetch stats (optional, don't fail if this fails)
            try {
                const statsRes = await fetch(`${API_BASE_URL}/api/admin/stats`, { headers })
                if (statsRes.ok) {
                    setStats(await statsRes.json())
                }
            } catch (e) {
                console.warn("Stats fetch failed:", e)
            }

            setError(null)
        } catch (err) {
            console.error("Admin fetch error:", err)
            setError(err instanceof Error ? err.message : "Kunde inte ladda data")
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
        const interval = setInterval(fetchData, 30000)
        return () => clearInterval(interval)
    }, [user, authLoading, isAdmin, router, fetchData])

    // Filter & search
    const filteredUsers = users
        .filter(u => {
            if (filter === "online") return isOnline(u.last_activity_at)
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
            const aTime = a.last_activity_at ? new Date(a.last_activity_at).getTime() : 0
            const bTime = b.last_activity_at ? new Date(b.last_activity_at).getTime() : 0
            return bTime - aTime
        })

    // Actions
    const handleToggleActive = async (targetUser: User) => {
        if (!confirm(`${targetUser.is_active ? "Inaktivera" : "Aktivera"} ${targetUser.email}?`)) return
        try {
            const token = getToken()
            await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}`, {
                method: "PATCH",
                headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
                body: JSON.stringify({ is_active: !targetUser.is_active })
            })
            fetchData()
        } catch (e) {
            console.error(e)
        }
    }

    const handleDelete = async (targetUser: User) => {
        if (!confirm(`Ta bort ${targetUser.email} permanent?`)) return
        if (!confirm("Säker? Detta kan inte ångras!")) return
        try {
            const token = getToken()
            await fetch(`${API_BASE_URL}/api/admin/users/${targetUser.id}?hard_delete=true`, {
                method: "DELETE",
                headers: { Authorization: `Bearer ${token}` }
            })
            fetchData()
        } catch (e) {
            console.error(e)
        }
    }

    // Loading
    if (authLoading || loading) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <Loader2 className="w-8 h-8 text-purple-500 animate-spin" />
            </div>
        )
    }

    // Error
    if (error) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center p-6">
                <div className="text-center">
                    <AlertCircle className="w-12 h-12 text-red-400 mx-auto mb-4" />
                    <p className="text-white mb-4">{error}</p>
                    <Button onClick={() => { setLoading(true); fetchData() }}>
                        Försök igen
                    </Button>
                </div>
            </div>
        )
    }

    const onlineCount = users.filter(u => isOnline(u.last_activity_at)).length

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
            </div>

            <div className="max-w-6xl mx-auto px-4 py-6">
                {/* Stats */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
                    <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800">
                        <div className="flex items-center gap-3">
                            <Users className="w-5 h-5 text-blue-400" />
                            <div>
                                <p className="text-2xl font-bold text-white">{users.length}</p>
                                <p className="text-xs text-zinc-500">Totalt</p>
                            </div>
                        </div>
                    </div>
                    <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800">
                        <div className="flex items-center gap-3">
                            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                            <div>
                                <p className="text-2xl font-bold text-green-400">{onlineCount}</p>
                                <p className="text-xs text-zinc-500">Online nu</p>
                            </div>
                        </div>
                    </div>
                    <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800">
                        <div className="flex items-center gap-3">
                            <Clock className="w-5 h-5 text-amber-400" />
                            <div>
                                <p className="text-2xl font-bold text-white">{stats?.active_today || 0}</p>
                                <p className="text-xs text-zinc-500">Aktiva idag</p>
                            </div>
                        </div>
                    </div>
                    <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800">
                        <div className="flex items-center gap-3">
                            <Calendar className="w-5 h-5 text-purple-400" />
                            <div>
                                <p className="text-2xl font-bold text-white">{stats?.users_this_week || 0}</p>
                                <p className="text-xs text-zinc-500">Nya denna vecka</p>
                            </div>
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
                            { key: "online", label: "Online" },
                            { key: "inactive", label: "Inaktiva" },
                        ].map((f) => (
                            <button
                                key={f.key}
                                onClick={() => setFilter(f.key as any)}
                                className={cn(
                                    "px-4 py-2.5 rounded-xl text-sm font-medium transition-colors",
                                    filter === f.key
                                        ? "bg-purple-600 text-white"
                                        : "bg-zinc-900 text-zinc-400 border border-zinc-800 hover:border-zinc-700"
                                )}
                            >
                                {f.label}
                            </button>
                        ))}
                    </div>
                </div>

                {/* User List */}
                <div className="space-y-2">
                    {filteredUsers.length === 0 ? (
                        <div className="text-center py-12 text-zinc-500">
                            Inga användare hittades
                        </div>
                    ) : (
                        filteredUsers.map((u) => (
                            <UserCard
                                key={u.id}
                                user={u}
                                onToggleActive={() => handleToggleActive(u)}
                                onDelete={() => handleDelete(u)}
                                onViewDetails={() => router.push(`/admin/users/${u.id}`)}
                            />
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}
