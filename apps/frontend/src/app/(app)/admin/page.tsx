"use client"

/**
 * ============================================================================
 * ADMIN PANEL — Deluxe User Management v2.0
 * ============================================================================
 *
 * Clean, professional admin interface for user management.
 *
 * Features:
 * - User list with search, filter, sort
 * - Online status tracking (green = online, gray = last seen)
 * - User actions: edit, toggle admin, ban, force logout, delete
 * - Stats overview
 *
 * @version 2.0 - Complete rebuild
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { useRouter } from "next/navigation"
import Image from "next/image"
import { motion, AnimatePresence } from "framer-motion"
import {
    Users, Shield, Search, RefreshCw,
    MoreVertical, UserCheck, UserX, LogOut,
    Ban, Trash2, ShieldCheck, ShieldOff,
    ChevronLeft, ChevronRight,
    Clock, Calendar,
    AlertCircle, CheckCircle
} from "lucide-react"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

// Fallback admin check by email
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

// =============================================================================
// TYPES
// =============================================================================

interface User {
    id: string
    email: string
    full_name: string | null
    avatar_url: string | null
    is_active: boolean
    is_admin: boolean
    is_verified: boolean
    total_xp: number
    level: number
    current_streak: number
    tasks_completed: number
    modules_completed: number
    created_at: string
    updated_at: string
    last_activity_at: string | null
}

interface Stats {
    total_users: number
    active_users: number
    admin_users: number
    online_now: number
    active_today: number
    users_this_week: number
}

type SortField = "last_activity_at" | "created_at" | "email" | "total_xp"
type SortOrder = "asc" | "desc"
type FilterStatus = "all" | "active" | "inactive" | "admin" | "online"

// =============================================================================
// CONSTANTS
// =============================================================================

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || ""
const ONLINE_THRESHOLD_MS = 5 * 60 * 1000 // 5 minutes

// =============================================================================
// UTILITIES
// =============================================================================

function parseDate(date: string | null): Date | null {
    if (!date) return null
    const d = new Date(date.endsWith('Z') ? date : date + 'Z')
    return isNaN(d.getTime()) ? null : d
}

function isOnline(date: string | null): boolean {
    const d = parseDate(date)
    if (!d) return false
    return Date.now() - d.getTime() < ONLINE_THRESHOLD_MS
}

function formatLastSeen(date: string | null): string {
    const d = parseDate(date)
    if (!d) return "Aldrig"

    const diff = Date.now() - d.getTime()
    if (diff < 0) return "Just nu"

    const mins = Math.floor(diff / 60000)
    const hours = Math.floor(diff / 3600000)
    const days = Math.floor(diff / 86400000)

    if (mins < 1) return "Just nu"
    if (mins < 60) return `${mins}m sedan`
    if (hours < 24) return `${hours}h sedan`
    if (days < 7) return `${days}d sedan`
    if (days < 30) return `${Math.floor(days / 7)}v sedan`
    return d.toLocaleDateString("sv-SE")
}

function formatDate(date: string): string {
    return new Date(date).toLocaleDateString("sv-SE", {
        year: "numeric",
        month: "short",
        day: "numeric"
    })
}

function getInitials(name: string | null, email: string): string {
    if (name) {
        return name.split(" ").map(n => n[0]).join("").toUpperCase().slice(0, 2)
    }
    return email.slice(0, 2).toUpperCase()
}

// =============================================================================
// COMPONENTS
// =============================================================================

// Stats Card
function StatsCard({ icon: Icon, value, label, color }: {
    icon: React.ElementType
    value: number | string
    label: string
    color: "blue" | "green" | "purple" | "yellow" | "red"
}) {
    const colors = {
        blue: "text-blue-400 bg-blue-500/10 border-blue-500/20",
        green: "text-green-400 bg-green-500/10 border-green-500/20",
        purple: "text-purple-400 bg-purple-500/10 border-purple-500/20",
        yellow: "text-yellow-400 bg-yellow-500/10 border-yellow-500/20",
        red: "text-red-400 bg-red-500/10 border-red-500/20",
    }

    return (
        <div className={cn("p-4 rounded-xl border", colors[color])}>
            <div className="flex items-center gap-3">
                <Icon className="w-5 h-5" />
                <div>
                    <div className="text-2xl font-bold text-white">{value}</div>
                    <div className="text-xs opacity-70">{label}</div>
                </div>
            </div>
        </div>
    )
}

// Online Status Badge
function OnlineBadge({ lastActivity }: { lastActivity: string | null }) {
    const online = isOnline(lastActivity)
    const lastSeen = formatLastSeen(lastActivity)
    const d = parseDate(lastActivity)
    const tooltip = d ? `Senast sedd: ${d.toLocaleString("sv-SE")}` : "Aldrig aktiv"

    if (online) {
        return (
            <div className="flex items-center gap-1.5" title={tooltip}>
                <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                <span className="text-xs text-green-400 font-medium">Online</span>
            </div>
        )
    }

    return (
        <div className="flex items-center gap-1.5" title={tooltip}>
            <div className="w-2 h-2 rounded-full bg-zinc-600" />
            <span className="text-xs text-zinc-500">{lastSeen}</span>
        </div>
    )
}

// User Avatar
function UserAvatar({ user, size = "md" }: { user: User, size?: "sm" | "md" | "lg" }) {
    const sizes = { sm: "w-8 h-8 text-xs", md: "w-10 h-10 text-sm", lg: "w-12 h-12 text-base" }
    const online = isOnline(user.last_activity_at)

    return (
        <div className="relative">
            {user.avatar_url ? (
                <Image
                    src={user.avatar_url}
                    alt={user.full_name || user.email}
                    width={size === "lg" ? 48 : size === "md" ? 40 : 32}
                    height={size === "lg" ? 48 : size === "md" ? 40 : 32}
                    className={cn(sizes[size], "rounded-xl object-cover")}
                />
            ) : (
                <div className={cn(
                    sizes[size],
                    "rounded-xl flex items-center justify-center font-bold",
                    user.is_admin
                        ? "bg-gradient-to-br from-purple-500 to-pink-500 text-white"
                        : "bg-zinc-800 text-zinc-400"
                )}>
                    {getInitials(user.full_name, user.email)}
                </div>
            )}
            {/* Online indicator dot */}
            <div className={cn(
                "absolute -bottom-0.5 -right-0.5 w-3 h-3 rounded-full border-2 border-zinc-900",
                online ? "bg-green-500" : "bg-zinc-600"
            )} />
        </div>
    )
}

// Action Menu
function ActionMenu({ user, onAction, isOpen, onClose }: {
    user: User
    onAction: (action: string) => void
    isOpen: boolean
    onClose: () => void
}) {
    if (!isOpen) return null

    const actions = [
        {
            id: "toggle-admin", icon: user.is_admin ? ShieldOff : ShieldCheck,
            label: user.is_admin ? "Ta bort admin" : "Gör till admin",
            color: user.is_admin ? "text-zinc-400" : "text-purple-400"
        },
        {
            id: "toggle-active", icon: user.is_active ? UserX : UserCheck,
            label: user.is_active ? "Inaktivera" : "Aktivera",
            color: user.is_active ? "text-yellow-400" : "text-green-400"
        },
        { id: "force-logout", icon: LogOut, label: "Tvångsutlogga", color: "text-orange-400" },
        { id: "ban", icon: Ban, label: "Spärra konto", color: "text-red-400" },
        { id: "delete", icon: Trash2, label: "Radera permanent", color: "text-red-500" },
    ]

    return (
        <>
            <div className="fixed inset-0 z-40" onClick={onClose} />
            <motion.div
                initial={{ opacity: 0, scale: 0.95, y: -10 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.95, y: -10 }}
                className="absolute right-0 top-full mt-1 w-48 py-1 bg-zinc-900 border border-zinc-700 rounded-xl shadow-xl z-50"
            >
                {actions.map((action, i) => (
                    <React.Fragment key={action.id}>
                        {i === 3 && <div className="my-1 border-t border-zinc-800" />}
                        <button
                            onClick={() => { onAction(action.id); onClose() }}
                            className={cn(
                                "w-full px-3 py-2 text-left text-sm flex items-center gap-2",
                                "hover:bg-zinc-800 transition-colors",
                                action.color
                            )}
                        >
                            <action.icon className="w-4 h-4" />
                            {action.label}
                        </button>
                    </React.Fragment>
                ))}
            </motion.div>
        </>
    )
}

// User Row
function UserRow({ user, onAction }: { user: User, onAction: (action: string, user: User) => void }) {
    const [menuOpen, setMenuOpen] = useState(false)

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "group px-4 py-3 rounded-xl border transition-all",
                "bg-zinc-900/50 border-zinc-800 hover:border-zinc-700",
                !user.is_active && "opacity-60"
            )}
        >
            <div className="flex items-center gap-4">
                {/* Avatar */}
                <UserAvatar user={user} />

                {/* User Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                        <span className="font-medium text-white truncate">
                            {user.full_name || "Inget namn"}
                        </span>
                        {user.is_admin && (
                            <span className="px-1.5 py-0.5 text-[10px] font-bold rounded bg-purple-500/20 text-purple-400">
                                ADMIN
                            </span>
                        )}
                        {!user.is_active && (
                            <span className="px-1.5 py-0.5 text-[10px] font-bold rounded bg-red-500/20 text-red-400">
                                INAKTIV
                            </span>
                        )}
                    </div>
                    <div className="text-sm text-zinc-500 truncate">{user.email}</div>
                </div>

                {/* Online Status */}
                <div className="hidden sm:block">
                    <OnlineBadge lastActivity={user.last_activity_at} />
                </div>

                {/* Stats */}
                <div className="hidden md:flex items-center gap-4 text-xs text-zinc-500">
                    <div className="text-center">
                        <div className="font-medium text-white">{user.total_xp}</div>
                        <div>XP</div>
                    </div>
                    <div className="text-center">
                        <div className="font-medium text-white">{user.tasks_completed}</div>
                        <div>Tasks</div>
                    </div>
                </div>

                {/* Registration Date */}
                <div className="hidden lg:block text-xs text-zinc-500">
                    <div>Registrerad</div>
                    <div className="text-zinc-400">{formatDate(user.created_at)}</div>
                </div>

                {/* Actions */}
                <div className="relative">
                    <button
                        onClick={() => setMenuOpen(!menuOpen)}
                        className="p-2 rounded-lg hover:bg-zinc-800 transition-colors"
                    >
                        <MoreVertical className="w-4 h-4 text-zinc-500" />
                    </button>
                    <AnimatePresence>
                        <ActionMenu
                            user={user}
                            isOpen={menuOpen}
                            onClose={() => setMenuOpen(false)}
                            onAction={(action) => onAction(action, user)}
                        />
                    </AnimatePresence>
                </div>
            </div>

            {/* Mobile: Additional info */}
            <div className="sm:hidden mt-2 pt-2 border-t border-zinc-800 flex items-center justify-between text-xs">
                <OnlineBadge lastActivity={user.last_activity_at} />
                <span className="text-zinc-500">{user.total_xp} XP • {user.tasks_completed} tasks</span>
            </div>
        </motion.div>
    )
}

// =============================================================================
// MAIN COMPONENT
// =============================================================================

export default function AdminPage() {
    const router = useRouter()
    const { user: currentUser, loading: authLoading } = useAuth()

    // State
    const [users, setUsers] = useState<User[]>([])
    const [stats, setStats] = useState<Stats | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    // Filters & Search
    const [search, setSearch] = useState("")
    const [filter, setFilter] = useState<FilterStatus>("all")
    const [sortField, setSortField] = useState<SortField>("last_activity_at")
    const [sortOrder, setSortOrder] = useState<SortOrder>("desc")

    // Pagination
    const [page, setPage] = useState(1)
    const perPage = 20

    // ==========================================================================
    // DATA FETCHING
    // ==========================================================================

    const fetchData = useCallback(async () => {
        const token = getToken()
        if (!token) return

        setLoading(true)
        setError(null)

        try {
            // Fetch users
            const usersRes = await fetch(`${API_BASE_URL}/api/admin/users?per_page=500`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (!usersRes.ok) {
                if (usersRes.status === 403) {
                    setError("Du har inte behörighet att se denna sida")
                    return
                }
                throw new Error(`Kunde inte hämta användare (HTTP ${usersRes.status})`)
            }

            const usersData = await usersRes.json()
            setUsers(usersData.users || [])

            // Fetch stats (optional - don't fail if this doesn't work)
            try {
                const statsRes = await fetch(`${API_BASE_URL}/api/admin/stats`, {
                    headers: { Authorization: `Bearer ${token}` }
                })

                if (statsRes.ok) {
                    const statsData = await statsRes.json()
                    setStats(statsData)
                }
            } catch (statsErr) {
                console.warn("Stats fetch failed:", statsErr)
                // Don't set error - users loaded successfully
            }
        } catch (err) {
            console.error("Admin fetch error:", err)
            setError(err instanceof Error ? err.message : "Kunde inte hämta data")
        } finally {
            setLoading(false)
        }
    }, [])

    // Admin check with email fallback
    const isAdminUser = currentUser?.is_admin || currentUser?.email?.toLowerCase() === ADMIN_EMAIL
    
    useEffect(() => {
        if (!authLoading && isAdminUser) {
            fetchData()
        }
    }, [authLoading, isAdminUser, fetchData])

    // Auto-refresh every 30 seconds
    useEffect(() => {
        const interval = setInterval(() => {
            if (isAdminUser) fetchData()
        }, 30000)
        return () => clearInterval(interval)
    }, [isAdminUser, fetchData])

    // ==========================================================================
    // ACTIONS
    // ==========================================================================

    const handleAction = async (action: string, targetUser: User) => {
        const token = getToken()
        if (!token) return

        const confirmMessages: Record<string, string> = {
            "toggle-admin": targetUser.is_admin
                ? `Ta bort admin-rättigheter från ${targetUser.email}?`
                : `Ge admin-rättigheter till ${targetUser.email}?`,
            "toggle-active": targetUser.is_active
                ? `Inaktivera ${targetUser.email}?`
                : `Aktivera ${targetUser.email}?`,
            "force-logout": `Tvångsutlogga ${targetUser.email}?\n\nAnvändaren måste logga in igen.`,
            "ban": `🚫 SPÄRRA ${targetUser.email}?\n\nKontot inaktiveras permanent.`,
            "delete": `⚠️ RADERA ${targetUser.email} PERMANENT?\n\nDetta kan inte ångras!`,
        }

        if (!confirm(confirmMessages[action])) return

        try {
            let endpoint = ""
            let method = "POST"
            let body: Record<string, unknown> | null = null

            switch (action) {
                case "toggle-admin":
                    endpoint = `/api/admin/users/${targetUser.id}`
                    method = "PATCH"
                    body = { is_admin: !targetUser.is_admin }
                    break
                case "toggle-active":
                    endpoint = `/api/admin/users/${targetUser.id}`
                    method = "PATCH"
                    body = { is_active: !targetUser.is_active }
                    break
                case "force-logout":
                    endpoint = `/api/admin/users/${targetUser.id}/force-logout`
                    break
                case "ban":
                    endpoint = `/api/admin/users/${targetUser.id}/ban`
                    break
                case "delete":
                    endpoint = `/api/admin/users/${targetUser.id}`
                    method = "DELETE"
                    break
            }

            const res = await fetch(`${API_BASE_URL}${endpoint}`, {
                method,
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: body ? JSON.stringify(body) : undefined
            })

            if (!res.ok) {
                const data = await res.json().catch(() => ({}))
                throw new Error(data.detail || `HTTP ${res.status}`)
            }

            // Refresh data
            await fetchData()

        } catch (err) {
            alert(`❌ Fel: ${err instanceof Error ? err.message : "Okänt fel"}`)
        }
    }

    // ==========================================================================
    // FILTERING & SORTING
    // ==========================================================================

    const filteredUsers = React.useMemo(() => {
        let result = [...users]

        // Search
        if (search) {
            const s = search.toLowerCase()
            result = result.filter(u =>
                u.email.toLowerCase().includes(s) ||
                (u.full_name && u.full_name.toLowerCase().includes(s))
            )
        }

        // Filter
        switch (filter) {
            case "active": result = result.filter(u => u.is_active); break
            case "inactive": result = result.filter(u => !u.is_active); break
            case "admin": result = result.filter(u => u.is_admin); break
            case "online": result = result.filter(u => isOnline(u.last_activity_at)); break
        }

        // Sort
        result.sort((a, b) => {
            let aVal: string | number | null = null
            let bVal: string | number | null = null

            switch (sortField) {
                case "email": aVal = a.email; bVal = b.email; break
                case "total_xp": aVal = a.total_xp; bVal = b.total_xp; break
                case "created_at": aVal = a.created_at; bVal = b.created_at; break
                case "last_activity_at":
                    aVal = a.last_activity_at || "";
                    bVal = b.last_activity_at || "";
                    break
            }

            if (aVal === null || bVal === null) return 0
            if (aVal < bVal) return sortOrder === "asc" ? -1 : 1
            if (aVal > bVal) return sortOrder === "asc" ? 1 : -1
            return 0
        })

        return result
    }, [users, search, filter, sortField, sortOrder])

    // Pagination
    const totalPages = Math.ceil(filteredUsers.length / perPage)
    const paginatedUsers = filteredUsers.slice((page - 1) * perPage, page * perPage)
    const onlineCount = users.filter(u => isOnline(u.last_activity_at)).length

    // ==========================================================================
    // AUTH CHECK
    // ==========================================================================

    if (authLoading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-zinc-950">
                <RefreshCw className="w-8 h-8 animate-spin text-purple-500" />
            </div>
        )
    }

    if (!isAdminUser) {
        return (
            <div className="min-h-screen flex flex-col items-center justify-center bg-zinc-950 text-white p-4">
                <Shield className="w-16 h-16 text-red-500 mb-4" />
                <h1 className="text-2xl font-bold mb-2">Åtkomst nekad</h1>
                <p className="text-zinc-400 mb-6">Du måste vara admin för att se denna sida.</p>
                <button
                    onClick={() => router.push("/dashboard")}
                    className="px-4 py-2 bg-purple-600 rounded-lg hover:bg-purple-700 transition"
                >
                    Tillbaka till Dashboard
                </button>
            </div>
        )
    }

    // ==========================================================================
    // RENDER
    // ==========================================================================

    return (
        <div className="min-h-screen bg-zinc-950 text-white">
            <div className="max-w-7xl mx-auto px-4 py-8">

                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <div>
                        <h1 className="text-3xl font-bold flex items-center gap-3">
                            <Shield className="w-8 h-8 text-purple-500" />
                            Admin Panel
                        </h1>
                        <p className="text-zinc-400 mt-1">Hantera användare och systemet</p>
                    </div>
                    <button
                        onClick={fetchData}
                        disabled={loading}
                        className="flex items-center gap-2 px-4 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition disabled:opacity-50"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Uppdatera
                    </button>
                </div>

                {/* Stats */}
                {stats && (
                    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3 mb-8">
                        <StatsCard icon={Users} value={stats.total_users} label="Totalt" color="blue" />
                        <StatsCard icon={UserCheck} value={stats.active_users} label="Aktiva" color="green" />
                        <StatsCard icon={Shield} value={stats.admin_users} label="Admins" color="purple" />
                        <StatsCard icon={CheckCircle} value={onlineCount} label="Online nu" color="green" />
                        <StatsCard icon={Clock} value={stats.active_today} label="Aktiva idag" color="yellow" />
                        <StatsCard icon={Calendar} value={stats.users_this_week} label="Nya (7d)" color="blue" />
                    </div>
                )}

                {/* Error */}
                {error && (
                    <div className="mb-6 p-4 bg-red-500/10 border border-red-500/20 rounded-xl flex items-center gap-3">
                        <AlertCircle className="w-5 h-5 text-red-500" />
                        <span className="text-red-400">{error}</span>
                    </div>
                )}

                {/* Filters */}
                <div className="flex flex-col sm:flex-row gap-3 mb-6">
                    {/* Search */}
                    <div className="relative flex-1">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                        <input
                            type="text"
                            placeholder="Sök på email eller namn..."
                            value={search}
                            onChange={(e) => { setSearch(e.target.value); setPage(1) }}
                            className="w-full pl-10 pr-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-xl text-white placeholder-zinc-500 focus:outline-none focus:border-purple-500 transition"
                        />
                    </div>

                    {/* Filter */}
                    <select
                        value={filter}
                        onChange={(e) => { setFilter(e.target.value as FilterStatus); setPage(1) }}
                        className="px-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-xl text-white focus:outline-none focus:border-purple-500"
                    >
                        <option value="all">Alla användare</option>
                        <option value="active">Aktiva</option>
                        <option value="inactive">Inaktiva</option>
                        <option value="admin">Admins</option>
                        <option value="online">Online nu</option>
                    </select>

                    {/* Sort */}
                    <select
                        value={`${sortField}-${sortOrder}`}
                        onChange={(e) => {
                            const [field, order] = e.target.value.split("-") as [SortField, SortOrder]
                            setSortField(field)
                            setSortOrder(order)
                        }}
                        className="px-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-xl text-white focus:outline-none focus:border-purple-500"
                    >
                        <option value="last_activity_at-desc">Senast aktiv</option>
                        <option value="created_at-desc">Nyast först</option>
                        <option value="created_at-asc">Äldst först</option>
                        <option value="email-asc">Email A-Ö</option>
                        <option value="total_xp-desc">Mest XP</option>
                    </select>
                </div>

                {/* User Count */}
                <div className="text-sm text-zinc-500 mb-4">
                    Visar {paginatedUsers.length} av {filteredUsers.length} användare
                    {search && ` (sökresultat)`}
                </div>

                {/* User List */}
                <div className="space-y-2">
                    {loading && users.length === 0 ? (
                        <div className="flex items-center justify-center py-20">
                            <RefreshCw className="w-8 h-8 animate-spin text-purple-500" />
                        </div>
                    ) : paginatedUsers.length === 0 ? (
                        <div className="text-center py-20 text-zinc-500">
                            {search ? "Inga användare matchar sökningen" : "Inga användare hittades"}
                        </div>
                    ) : (
                        paginatedUsers.map(user => (
                            <UserRow
                                key={user.id}
                                user={user}
                                onAction={handleAction}
                            />
                        ))
                    )}
                </div>

                {/* Pagination */}
                {totalPages > 1 && (
                    <div className="flex items-center justify-center gap-2 mt-8">
                        <button
                            onClick={() => setPage(p => Math.max(1, p - 1))}
                            disabled={page === 1}
                            className="p-2 rounded-lg bg-zinc-900 hover:bg-zinc-800 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            <ChevronLeft className="w-5 h-5" />
                        </button>

                        <div className="flex items-center gap-1">
                            {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
                                let pageNum: number
                                if (totalPages <= 5) {
                                    pageNum = i + 1
                                } else if (page <= 3) {
                                    pageNum = i + 1
                                } else if (page >= totalPages - 2) {
                                    pageNum = totalPages - 4 + i
                                } else {
                                    pageNum = page - 2 + i
                                }

                                return (
                                    <button
                                        key={pageNum}
                                        onClick={() => setPage(pageNum)}
                                        className={cn(
                                            "w-10 h-10 rounded-lg transition",
                                            page === pageNum
                                                ? "bg-purple-600 text-white"
                                                : "bg-zinc-900 hover:bg-zinc-800"
                                        )}
                                    >
                                        {pageNum}
                                    </button>
                                )
                            })}
                        </div>

                        <button
                            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                            disabled={page === totalPages}
                            className="p-2 rounded-lg bg-zinc-900 hover:bg-zinc-800 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            <ChevronRight className="w-5 h-5" />
                        </button>
                    </div>
                )}

            </div>
        </div>
    )
}
