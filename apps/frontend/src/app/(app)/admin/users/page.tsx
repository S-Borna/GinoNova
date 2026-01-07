"use client"

/**
 * Admin v2 Users - Complete user management with filters, actions, pagination
 */

import { useEffect, useState, useCallback, useMemo } from "react"
import Link from "next/link"
import Image from "next/image"
import {
    Search,
    RefreshCw,
    MoreVertical,
    UserCheck,
    UserX,
    LogOut,
    Ban,
    Trash2,
    ShieldCheck,
    ShieldOff,
    Eye,
    ChevronLeft,
    ChevronRight,
    Filter,
    X,
    CheckCircle,
    AlertCircle
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types
interface User {
    id: string
    email: string
    full_name: string | null
    avatar_url: string | null
    is_admin: boolean
    is_banned: boolean
    is_active: boolean
    is_verified: boolean
    oauth_provider: string | null
    created_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    current_streak: number
    permissions: {
        ai_quiz_access: boolean
        premium_modules_access: boolean
        study_room_access: boolean
        skillpath_access: boolean
    }
    stats: {
        modules_completed: number
        tasks_completed: number
        study_sessions: number
        ai_requests: number
    }
    status: "online" | "away" | "offline"
}

interface UsersResponse {
    users: User[]
    total: number
    page: number
    page_size: number
    total_pages: number
}

type SortField = "last_activity" | "created" | "email" | "xp"
type SortOrder = "asc" | "desc"
type StatusFilter = "all" | "online" | "away" | "offline" | "banned"
type RoleFilter = "all" | "admin" | "user"

// Components
function StatusBadge({ status, isBanned }: { status?: string, isBanned?: boolean }) {
    if (isBanned) {
        return (
            <span className="inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium bg-red-500/10 text-red-400">
                <span className="w-2 h-2 rounded-full bg-red-500" />
                Banned
            </span>
        )
    }

    // Default to offline if status is undefined
    const safeStatus = status || "offline"

    const styles = {
        online: "bg-green-500/10 text-green-400",
        away: "bg-yellow-500/10 text-yellow-400",
        offline: "bg-zinc-500/10 text-zinc-400"
    }

    const dotStyles = {
        online: "bg-green-500 animate-pulse",
        away: "bg-yellow-500",
        offline: "bg-zinc-500"
    }

    const displayStatus = safeStatus.charAt(0).toUpperCase() + safeStatus.slice(1)

    return (
        <span className={cn(
            "inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium",
            styles[safeStatus as keyof typeof styles] || styles.offline
        )}>
            <span className={cn("w-2 h-2 rounded-full", dotStyles[safeStatus as keyof typeof dotStyles] || dotStyles.offline)} />
            {displayStatus}
        </span>
    )
}

function UserAvatar({ user }: { user: User }) {
    const initials = user?.full_name
        ? user.full_name.split(" ").map(n => n?.[0] || "").join("").toUpperCase().slice(0, 2)
        : (user?.email || "??").slice(0, 2).toUpperCase()

    return (
        <div className="relative">
            {user.avatar_url ? (
                <Image
                    src={user.avatar_url}
                    alt={user.full_name || user.email}
                    width={40}
                    height={40}
                    className="w-10 h-10 rounded-lg object-cover"
                />
            ) : (
                <div className={cn(
                    "w-10 h-10 rounded-lg flex items-center justify-center font-bold text-sm",
                    user.is_admin
                        ? "bg-gradient-to-br from-purple-500 to-pink-500 text-white"
                        : "bg-zinc-800 text-zinc-400"
                )}>
                    {initials}
                </div>
            )}
            {/* Status dot */}
            <div className={cn(
                "absolute -bottom-0.5 -right-0.5 w-3 h-3 rounded-full border-2 border-zinc-900",
                user.status === "online" && "bg-green-500",
                user.status === "away" && "bg-yellow-500",
                user.status === "offline" && "bg-zinc-600",
                user.is_banned && "bg-red-500"
            )} />
        </div>
    )
}

function ActionMenu({ user, onAction, isOpen, onClose }: {
    user: User
    onAction: (action: string) => void
    isOpen: boolean
    onClose: () => void
}) {
    if (!isOpen) return null

    const actions = [
        { id: "view", icon: Eye, label: "View Details", color: "text-zinc-300" },
        { id: "divider1" },
        {
            id: "toggle-admin", icon: user.is_admin ? ShieldOff : ShieldCheck,
            label: user.is_admin ? "Remove Admin" : "Make Admin",
            color: user.is_admin ? "text-zinc-400" : "text-purple-400"
        },
        {
            id: "toggle-active", icon: user.is_active ? UserX : UserCheck,
            label: user.is_active ? "Deactivate" : "Activate",
            color: user.is_active ? "text-yellow-400" : "text-green-400"
        },
        { id: "divider2" },
        { id: "force-logout", icon: LogOut, label: "Force Logout", color: "text-orange-400" },
        {
            id: "ban", icon: Ban, label: user.is_banned ? "Unban User" : "Ban User",
            color: user.is_banned ? "text-green-400" : "text-red-400"
        },
        { id: "delete", icon: Trash2, label: "Delete User", color: "text-red-500" },
    ]

    return (
        <>
            <div className="fixed inset-0 z-40" onClick={onClose} />
            <div className="absolute right-0 top-full mt-1 w-48 py-1 bg-zinc-900 border border-zinc-700 rounded-xl shadow-xl z-50">
                {actions.map((action) => {
                    if (action.id.startsWith("divider")) {
                        return <div key={action.id} className="my-1 border-t border-zinc-800" />
                    }
                    return (
                        <button
                            key={action.id}
                            onClick={() => { onAction(action.id); onClose() }}
                            className={cn(
                                "w-full px-3 py-2 text-left text-sm flex items-center gap-2",
                                "hover:bg-zinc-800 transition-colors",
                                action.color
                            )}
                        >
                            {action.icon && <action.icon className="w-4 h-4" />}
                            {action.label}
                        </button>
                    )
                })}
            </div>
        </>
    )
}

function ConfirmDialog({
    isOpen,
    onClose,
    onConfirm,
    title,
    description,
    confirmLabel = "Confirm",
    confirmColor = "red",
    loading = false
}: {
    isOpen: boolean
    onClose: () => void
    onConfirm: () => void
    title: string
    description: string
    confirmLabel?: string
    confirmColor?: "red" | "green" | "purple"
    loading?: boolean
}) {
    if (!isOpen) return null

    const colors = {
        red: "bg-red-600 hover:bg-red-700",
        green: "bg-green-600 hover:bg-green-700",
        purple: "bg-purple-600 hover:bg-purple-700"
    }

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
            <div className="bg-zinc-900 border border-zinc-700 rounded-xl p-6 max-w-md w-full mx-4 shadow-2xl">
                <h3 className="text-lg font-semibold mb-2">{title}</h3>
                <p className="text-sm text-zinc-400 mb-6 whitespace-pre-wrap">{description}</p>
                <div className="flex gap-3 justify-end">
                    <button
                        onClick={onClose}
                        disabled={loading}
                        className="px-4 py-2 text-sm bg-zinc-800 hover:bg-zinc-700 rounded-lg transition"
                    >
                        Cancel
                    </button>
                    <button
                        onClick={onConfirm}
                        disabled={loading}
                        className={cn(
                            "px-4 py-2 text-sm rounded-lg transition flex items-center gap-2",
                            colors[confirmColor]
                        )}
                    >
                        {loading && <RefreshCw className="w-4 h-4 animate-spin" />}
                        {confirmLabel}
                    </button>
                </div>
            </div>
        </div>
    )
}

function Toast({ message, type, onClose }: { message: string, type: "success" | "error", onClose: () => void }) {
    useEffect(() => {
        const timer = setTimeout(onClose, 4000)
        return () => clearTimeout(timer)
    }, [onClose])

    return (
        <div className={cn(
            "fixed bottom-4 right-4 z-50 flex items-center gap-3 px-4 py-3 rounded-lg shadow-lg",
            type === "success" ? "bg-green-600" : "bg-red-600"
        )}>
            {type === "success" ? <CheckCircle className="w-5 h-5" /> : <AlertCircle className="w-5 h-5" />}
            <span className="text-sm">{message}</span>
            <button onClick={onClose} className="ml-2 hover:opacity-70">
                <X className="w-4 h-4" />
            </button>
        </div>
    )
}

function UserRow({ user, onAction }: { user: User, onAction: (action: string, user: User) => void }) {
    const [menuOpen, setMenuOpen] = useState(false)

    const lastActive = user.last_activity_at
        ? new Date(user.last_activity_at).toLocaleString("sv-SE")
        : "Never"

    const createdAt = new Date(user.created_at).toLocaleDateString("sv-SE", {
        year: "numeric",
        month: "short",
        day: "numeric"
    })

    return (
        <tr className={cn(
            "border-b border-zinc-800 hover:bg-zinc-900/50 transition",
            !user.is_active && "opacity-60"
        )}>
            <td className="py-3 px-4">
                <StatusBadge status={user.status} isBanned={user.is_banned || !user.is_active} />
            </td>
            <td className="py-3 px-4">
                <div className="flex items-center gap-3">
                    <UserAvatar user={user} />
                    <div>
                        <div className="font-medium flex items-center gap-2">
                            {user.full_name || "No name"}
                            {user.is_admin && (
                                <span className="px-1.5 py-0.5 text-[10px] font-bold rounded bg-purple-500/20 text-purple-400">
                                    ADMIN
                                </span>
                            )}
                        </div>
                        <div className="text-sm text-zinc-500">{user.email}</div>
                    </div>
                </div>
            </td>
            <td className="py-3 px-4 text-sm text-zinc-400">
                {createdAt}
            </td>
            <td className="py-3 px-4 text-sm text-zinc-400">
                {user.status === "online" ? (
                    <span className="text-green-400">Active now</span>
                ) : (
                    lastActive
                )}
            </td>
            <td className="py-3 px-4">
                <div className="flex items-center gap-4 text-sm">
                    <div className="text-center">
                        <div className="font-medium text-white">{user.total_xp.toLocaleString()}</div>
                        <div className="text-xs text-zinc-500">XP</div>
                    </div>
                    <div className="text-center">
                        <div className="font-medium text-white">Lv.{user.level}</div>
                        <div className="text-xs text-zinc-500">Level</div>
                    </div>
                </div>
            </td>
            <td className="py-3 px-4">
                <div className="relative">
                    <button
                        onClick={() => setMenuOpen(!menuOpen)}
                        className="p-2 rounded-lg hover:bg-zinc-800 transition"
                    >
                        <MoreVertical className="w-4 h-4 text-zinc-500" />
                    </button>
                    <ActionMenu
                        user={user}
                        isOpen={menuOpen}
                        onClose={() => setMenuOpen(false)}
                        onAction={(action) => onAction(action, user)}
                    />
                </div>
            </td>
        </tr>
    )
}

// Main Component
export default function AdminV2Users() {
    const [users, setUsers] = useState<User[]>([])
    const [total, setTotal] = useState(0)
    const [page, setPage] = useState(1)
    const [totalPages, setTotalPages] = useState(1)
    const [loading, setLoading] = useState(true)

    // Filters
    const [search, setSearch] = useState("")
    const [statusFilter, setStatusFilter] = useState<StatusFilter>("all")
    const [roleFilter, setRoleFilter] = useState<RoleFilter>("all")
    const [sortField, setSortField] = useState<SortField>("last_activity")
    const [sortOrder, setSortOrder] = useState<SortOrder>("desc")

    // Action state
    const [actionLoading, setActionLoading] = useState(false)
    const [confirmDialog, setConfirmDialog] = useState<{
        isOpen: boolean
        title: string
        description: string
        action: () => void
        confirmLabel: string
        confirmColor: "red" | "green" | "purple"
    } | null>(null)
    const [toast, setToast] = useState<{ message: string, type: "success" | "error" } | null>(null)

    const fetchUsers = useCallback(async () => {
        const token = getToken()
        if (!token) return

        setLoading(true)

        try {
            const params = new URLSearchParams({
                page: page.toString(),
                page_size: "50",
                sort: sortField,
                order: sortOrder
            })

            if (search) params.set("search", search)
            if (statusFilter !== "all") params.set("status", statusFilter)
            if (roleFilter !== "all") params.set("role", roleFilter)

            const res = await fetch(`${API_BASE_URL}/api/admin/users?${params}`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const data: UsersResponse = await res.json()
                setUsers(data.users)
                setTotal(data.total)
                setTotalPages(data.total_pages)
            }
        } catch (err) {
            console.error("Users fetch error:", err)
            setToast({ message: "Failed to load users", type: "error" })
        } finally {
            setLoading(false)
        }
    }, [page, search, statusFilter, roleFilter, sortField, sortOrder])

    useEffect(() => {
        const timer = setTimeout(() => {
            fetchUsers()
        }, search ? 300 : 0) // Debounce search

        return () => clearTimeout(timer)
    }, [fetchUsers])

    // Auto-refresh every minute
    useEffect(() => {
        const interval = setInterval(fetchUsers, 60000)
        return () => clearInterval(interval)
    }, [fetchUsers])

    const executeAction = async (action: string, endpoint: string, method = "POST", body?: object) => {
        const token = getToken()
        if (!token) {
            setToast({ message: "Not authenticated", type: "error" })
            return
        }

        setActionLoading(true)

        try {
            console.log(`[Admin] Executing ${method} ${API_BASE_URL}${endpoint}`, body)

            const res = await fetch(`${API_BASE_URL}${endpoint}`, {
                method,
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(body || {})
            })

            console.log(`[Admin] Response status: ${res.status}`)

            if (!res.ok) {
                const data = await res.json().catch(() => null)
                console.error(`[Admin] Error response:`, data)
                const errorMsg = data?.detail || data?.message || `HTTP ${res.status}`
                throw new Error(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg))
            }

            const result = await res.json().catch(() => ({}))
            console.log(`[Admin] Success:`, result)
            setToast({ message: result.message || `Action completed successfully`, type: "success" })
            fetchUsers() // Refresh
        } catch (err) {
            console.error(`[Admin] Action failed:`, err)
            const errorMessage = err instanceof Error ? err.message : String(err)
            setToast({ message: `Failed: ${errorMessage}`, type: "error" })
        } finally {
            setActionLoading(false)
            setConfirmDialog(null)
        }
    }

    const handleAction = (action: string, user: User) => {
        switch (action) {
            case "view":
                window.location.href = `/admin/users/${user.id}`
                break

            case "toggle-admin":
                setConfirmDialog({
                    isOpen: true,
                    title: user.is_admin ? "Remove Admin Rights" : "Grant Admin Rights",
                    description: user.is_admin
                        ? `Remove admin privileges from ${user.email}?`
                        : `Grant admin privileges to ${user.email}?`,
                    action: () => executeAction(action, `/api/admin/users/${user.id}/toggle-admin`),
                    confirmLabel: user.is_admin ? "Remove Admin" : "Make Admin",
                    confirmColor: user.is_admin ? "red" : "purple"
                })
                break

            case "toggle-active":
                setConfirmDialog({
                    isOpen: true,
                    title: user.is_active ? "Deactivate User" : "Activate User",
                    description: user.is_active
                        ? `Deactivate ${user.email}? They will not be able to access the platform.`
                        : `Activate ${user.email}? They will regain access to the platform.`,
                    action: () => executeAction(action, `/api/admin/users/${user.id}`, "PUT", { is_active: !user.is_active }),
                    confirmLabel: user.is_active ? "Deactivate" : "Activate",
                    confirmColor: user.is_active ? "red" : "green"
                })
                break

            case "force-logout":
                setConfirmDialog({
                    isOpen: true,
                    title: "Force Logout",
                    description: `Force logout ${user.email}?\n\nThey will need to log in again.`,
                    action: () => executeAction(action, `/api/admin/users/${user.id}/force-logout`),
                    confirmLabel: "Force Logout",
                    confirmColor: "red"
                })
                break

            case "ban":
                if (user.is_banned) {
                    setConfirmDialog({
                        isOpen: true,
                        title: "Unban User",
                        description: `Unban ${user.email}? They will be able to access the platform again.`,
                        action: () => executeAction(action, `/api/admin/users/${user.id}/unban`, "POST", {}),
                        confirmLabel: "Unban User",
                        confirmColor: "green"
                    })
                } else {
                    setConfirmDialog({
                        isOpen: true,
                        title: "🚫 Ban User",
                        description: `Ban ${user.email}?\n\nThis will immediately log them out and prevent future logins.`,
                        action: () => executeAction(action, `/api/admin/users/${user.id}/ban`, "POST", {}),
                        confirmLabel: "Ban User",
                        confirmColor: "red"
                    })
                }
                break

            case "delete":
                setConfirmDialog({
                    isOpen: true,
                    title: "⚠️ Delete User Permanently",
                    description: `DELETE ${user.email} PERMANENTLY?\n\nThis action cannot be undone. All user data will be lost.`,
                    action: () => executeAction(action, `/api/admin/users/${user.id}`, "DELETE", {}),
                    confirmLabel: "Delete Forever",
                    confirmColor: "red"
                })
                break
        }
    }

    const onlineCount = users.filter(u => u.status === "online").length

    return (
        <div className="p-6">
            {/* Header */}
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h1 className="text-2xl font-bold">Users</h1>
                    <p className="text-sm text-zinc-400">
                        {total.toLocaleString()} total users • {onlineCount} online
                    </p>
                </div>
                <button
                    onClick={fetchUsers}
                    disabled={loading}
                    className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                >
                    <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                    Refresh
                </button>
            </div>

            {/* Filters */}
            <div className="flex flex-col md:flex-row gap-3 mb-6">
                {/* Search */}
                <div className="relative flex-1">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                    <input
                        type="text"
                        placeholder="Search by email or name..."
                        value={search}
                        onChange={(e) => { setSearch(e.target.value); setPage(1) }}
                        className="w-full pl-10 pr-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-lg text-white placeholder-zinc-500 focus:outline-none focus:border-purple-500 transition"
                    />
                </div>

                {/* Status Filter */}
                <select
                    value={statusFilter}
                    onChange={(e) => { setStatusFilter(e.target.value as StatusFilter); setPage(1) }}
                    className="px-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-lg text-white focus:outline-none focus:border-purple-500"
                >
                    <option value="all">All Status</option>
                    <option value="online">Online</option>
                    <option value="away">Away</option>
                    <option value="offline">Offline</option>
                    <option value="banned">Banned</option>
                </select>

                {/* Role Filter */}
                <select
                    value={roleFilter}
                    onChange={(e) => { setRoleFilter(e.target.value as RoleFilter); setPage(1) }}
                    className="px-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-lg text-white focus:outline-none focus:border-purple-500"
                >
                    <option value="all">All Roles</option>
                    <option value="admin">Admins</option>
                    <option value="user">Users</option>
                </select>

                {/* Sort */}
                <select
                    value={`${sortField}-${sortOrder}`}
                    onChange={(e) => {
                        const [field, order] = e.target.value.split("-") as [SortField, SortOrder]
                        setSortField(field)
                        setSortOrder(order)
                    }}
                    className="px-4 py-2.5 bg-zinc-900 border border-zinc-800 rounded-lg text-white focus:outline-none focus:border-purple-500"
                >
                    <option value="last_activity-desc">Last Active</option>
                    <option value="created-desc">Newest First</option>
                    <option value="created-asc">Oldest First</option>
                    <option value="email-asc">Email A-Z</option>
                    <option value="xp-desc">Highest XP</option>
                </select>
            </div>

            {/* Table */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl overflow-hidden">
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead className="bg-zinc-800/50">
                            <tr className="text-left text-xs text-zinc-400 uppercase tracking-wider">
                                <th className="py-3 px-4 font-medium">Status</th>
                                <th className="py-3 px-4 font-medium">User</th>
                                <th className="py-3 px-4 font-medium">Created</th>
                                <th className="py-3 px-4 font-medium">Last Active</th>
                                <th className="py-3 px-4 font-medium">Progress</th>
                                <th className="py-3 px-4 font-medium w-16">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {loading && users.length === 0 ? (
                                [...Array(10)].map((_, i) => (
                                    <tr key={i} className="border-b border-zinc-800 animate-pulse">
                                        <td className="py-3 px-4"><div className="h-6 w-20 bg-zinc-800 rounded" /></td>
                                        <td className="py-3 px-4">
                                            <div className="flex items-center gap-3">
                                                <div className="w-10 h-10 bg-zinc-800 rounded-lg" />
                                                <div className="space-y-2">
                                                    <div className="h-4 w-32 bg-zinc-800 rounded" />
                                                    <div className="h-3 w-40 bg-zinc-800 rounded" />
                                                </div>
                                            </div>
                                        </td>
                                        <td className="py-3 px-4"><div className="h-4 w-24 bg-zinc-800 rounded" /></td>
                                        <td className="py-3 px-4"><div className="h-4 w-32 bg-zinc-800 rounded" /></td>
                                        <td className="py-3 px-4"><div className="h-4 w-20 bg-zinc-800 rounded" /></td>
                                        <td className="py-3 px-4"><div className="h-8 w-8 bg-zinc-800 rounded" /></td>
                                    </tr>
                                ))
                            ) : users.length === 0 ? (
                                <tr>
                                    <td colSpan={6} className="py-12 text-center text-zinc-500">
                                        {search ? "No users match your search" : "No users found"}
                                    </td>
                                </tr>
                            ) : (
                                users.map(user => (
                                    <UserRow
                                        key={user.id}
                                        user={user}
                                        onAction={handleAction}
                                    />
                                ))
                            )}
                        </tbody>
                    </table>
                </div>

                {/* Pagination */}
                {totalPages > 1 && (
                    <div className="flex items-center justify-between px-4 py-3 border-t border-zinc-800">
                        <div className="text-sm text-zinc-400">
                            Page {page} of {totalPages}
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => setPage(p => Math.max(1, p - 1))}
                                disabled={page === 1}
                                className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                                <ChevronLeft className="w-5 h-5" />
                            </button>
                            <button
                                onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                                disabled={page === totalPages}
                                className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                                <ChevronRight className="w-5 h-5" />
                            </button>
                        </div>
                    </div>
                )}
            </div>

            {/* Confirm Dialog */}
            {confirmDialog && (
                <ConfirmDialog
                    isOpen={confirmDialog.isOpen}
                    onClose={() => setConfirmDialog(null)}
                    onConfirm={confirmDialog.action}
                    title={confirmDialog.title}
                    description={confirmDialog.description}
                    confirmLabel={confirmDialog.confirmLabel}
                    confirmColor={confirmDialog.confirmColor}
                    loading={actionLoading}
                />
            )}

            {/* Toast */}
            {toast && (
                <Toast
                    message={toast.message}
                    type={toast.type}
                    onClose={() => setToast(null)}
                />
            )}
        </div>
    )
}
