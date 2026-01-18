"use client"

/**
 * Admin Live Activity - Real-time user activity monitoring
 * Shows what users are doing right now on the platform
 * + Admin heartbeat to show online status to users
 * + User messages inbox
 */

import { useEffect, useState, useCallback } from "react"
import Link from "next/link"
import Image from "next/image"
import {
    Activity,
    Users,
    RefreshCw,
    Eye,
    Clock,
    Globe,
    BookOpen,
    GraduationCap,
    Bot,
    MessageSquare,
    Home,
    Inbox,
    Check,
    Trash2,
    Mail,
    MailOpen
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface LiveUser {
    id: string
    email: string
    full_name: string | null
    avatar_url: string | null
    status: "online" | "away"
    last_activity_at: string
    seconds_ago: number
    current_action: string
    current_page: string | null
}

interface LiveActivityResponse {
    users: LiveUser[]
    total: number
    timestamp: string
}

interface UserMessage {
    id: string
    user_id: string
    user_email: string
    user_name: string | null
    subject: string
    message: string
    timestamp: string
    read: boolean
}

function getActionIcon(action: string) {
    switch (action?.toLowerCase()) {
        case "login": return <Globe className="w-4 h-4" />
        case "study": return <BookOpen className="w-4 h-4" />
        case "quiz": return <GraduationCap className="w-4 h-4" />
        case "ai_quiz": return <Bot className="w-4 h-4" />
        case "community": return <MessageSquare className="w-4 h-4" />
        default: return <Home className="w-4 h-4" />
    }
}

function getActionLabel(action: string, page: string | null) {
    if (page) return page

    switch (action?.toLowerCase()) {
        case "login": return "Just logged in"
        case "study": return "Studying modules"
        case "quiz": return "Taking a quiz"
        case "ai_quiz": return "Using AI Quiz"
        case "community": return "In community"
        case "browsing": return "Browsing"
        default: return "Active on site"
    }
}

function formatTimeAgo(seconds: number) {
    if (seconds < 60) return "just now"
    if (seconds < 120) return "1 min ago"
    if (seconds < 3600) return `${Math.floor(seconds / 60)} min ago`
    return `${Math.floor(seconds / 3600)}h ago`
}

function UserAvatar({ user }: { user: LiveUser }) {
    const initials = user.full_name
        ? user.full_name.split(" ").map(n => n?.[0] || "").join("").toUpperCase().slice(0, 2)
        : user.email.slice(0, 2).toUpperCase()

    return (
        <div className="relative">
            {user.avatar_url ? (
                <Image
                    src={user.avatar_url}
                    alt={user.full_name || user.email}
                    width={48}
                    height={48}
                    className="w-12 h-12 rounded-xl object-cover"
                />
            ) : (
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center font-bold text-white">
                    {initials}
                </div>
            )}
            {/* Live indicator */}
            <div className={cn(
                "absolute -bottom-1 -right-1 w-4 h-4 rounded-full border-2 border-zinc-900",
                user.status === "online" ? "bg-green-500 animate-pulse" : "bg-yellow-500"
            )} />
        </div>
    )
}

function LiveUserCard({ user }: { user: LiveUser }) {
    return (
        <div className={cn(
            "p-4 rounded-xl border transition-all",
            user.status === "online"
                ? "bg-green-500/5 border-green-500/20"
                : "bg-yellow-500/5 border-yellow-500/20"
        )}>
            <div className="flex items-start gap-4">
                <UserAvatar user={user} />

                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-1">
                        <h3 className="font-medium text-white truncate">
                            {user.full_name || user.email.split("@")[0]}
                        </h3>
                        <span className={cn(
                            "text-xs px-2 py-0.5 rounded-full",
                            user.status === "online"
                                ? "bg-green-500/20 text-green-400"
                                : "bg-yellow-500/20 text-yellow-400"
                        )}>
                            {user.status === "online" ? "Active" : "Away"}
                        </span>
                    </div>
                    <p className="text-sm text-zinc-500 truncate">{user.email}</p>

                    {/* Current activity */}
                    <div className="mt-3 flex items-center gap-2 text-sm">
                        <div className={cn(
                            "p-1.5 rounded-lg",
                            user.status === "online" ? "bg-green-500/10 text-green-400" : "bg-yellow-500/10 text-yellow-400"
                        )}>
                            {getActionIcon(user.current_action)}
                        </div>
                        <span className="text-zinc-300">
                            {getActionLabel(user.current_action, user.current_page)}
                        </span>
                    </div>
                </div>

                {/* Time ago */}
                <div className="text-right shrink-0">
                    <div className="flex items-center gap-1 text-xs text-zinc-500">
                        <Clock className="w-3 h-3" />
                        {formatTimeAgo(user.seconds_ago)}
                    </div>
                    <Link
                        href={`/admin/users/${user.id}`}
                        className="mt-2 inline-flex items-center gap-1 text-xs text-purple-400 hover:text-purple-300"
                    >
                        <Eye className="w-3 h-3" />
                        View
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default function LiveActivityPage() {
    const [users, setUsers] = useState<LiveUser[]>([])
    const [loading, setLoading] = useState(true)
    const [lastUpdate, setLastUpdate] = useState<Date | null>(null)
    const [autoRefresh, setAutoRefresh] = useState(true)
    const [messages, setMessages] = useState<UserMessage[]>([])
    const [showMessages, setShowMessages] = useState(false)
    const [unreadCount, setUnreadCount] = useState(0)

    // Send admin heartbeat to indicate online status
    const sendHeartbeat = useCallback(async () => {
        const token = getToken()
        if (!token) return

        try {
            await fetch(`${API_BASE_URL}/api/admin/v2/status/heartbeat`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` }
            })
        } catch {
            // Silent fail
        }
    }, [])

    // Fetch user messages
    const fetchMessages = useCallback(async () => {
        const token = getToken()
        if (!token) return

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const data = await res.json()
                setMessages(data.messages || [])
                setUnreadCount(data.unread || 0)
            }
        } catch {
            // Silent fail
        }
    }, [])

    // Mark message as read
    const markAsRead = async (messageId: string) => {
        const token = getToken()
        if (!token) return

        try {
            await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages/${messageId}/read`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` }
            })
            fetchMessages()
        } catch {
            // Silent fail
        }
    }

    // Delete message
    const deleteMessage = async (messageId: string) => {
        const token = getToken()
        if (!token) return

        try {
            await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages/${messageId}`, {
                method: "DELETE",
                headers: { Authorization: `Bearer ${token}` }
            })
            fetchMessages()
        } catch {
            // Silent fail
        }
    }

    const fetchLiveActivity = useCallback(async () => {
        const token = getToken()
        if (!token) return

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/users/live-activity`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const data: LiveActivityResponse = await res.json()
                setUsers(data.users)
                setLastUpdate(new Date(data.timestamp))
            }
        } catch (err) {
            console.error("Failed to fetch live activity:", err)
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchLiveActivity()
        fetchMessages()
        sendHeartbeat()
    }, [fetchLiveActivity, fetchMessages, sendHeartbeat])

    // Auto-refresh every 5 seconds when enabled
    useEffect(() => {
        if (!autoRefresh) return
        const interval = setInterval(fetchLiveActivity, 5000)
        return () => clearInterval(interval)
    }, [autoRefresh, fetchLiveActivity])

    // Send heartbeat every 30 seconds and refresh messages
    useEffect(() => {
        const heartbeatInterval = setInterval(() => {
            sendHeartbeat()
            fetchMessages()
        }, 30000)
        return () => clearInterval(heartbeatInterval)
    }, [sendHeartbeat, fetchMessages])

    const onlineUsers = users.filter(u => u.status === "online")
    const awayUsers = users.filter(u => u.status === "away")

    return (
        <div className="p-6">
            {/* Header */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
                <div>
                    <div className="flex items-center gap-3">
                        <div className="p-2 rounded-xl bg-green-500/10">
                            <Activity className="w-6 h-6 text-green-400" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold">Live Activity</h1>
                            <p className="text-sm text-zinc-400">
                                {users.length} active users right now
                            </p>
                        </div>
                    </div>
                </div>

                <div className="flex items-center gap-3">
                    {/* Messages inbox button */}
                    <button
                        onClick={() => setShowMessages(!showMessages)}
                        className={cn(
                            "relative flex items-center gap-2 px-3 py-2 rounded-lg transition text-sm",
                            showMessages
                                ? "bg-purple-500/20 text-purple-400"
                                : "bg-zinc-800 hover:bg-zinc-700 text-zinc-300"
                        )}
                    >
                        <Inbox className="w-4 h-4" />
                        Messages
                        {unreadCount > 0 && (
                            <span className="absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-white text-xs flex items-center justify-center font-medium">
                                {unreadCount}
                            </span>
                        )}
                    </button>

                    {/* Auto-refresh toggle */}
                    <label className="flex items-center gap-2 text-sm text-zinc-400">
                        <input
                            type="checkbox"
                            checked={autoRefresh}
                            onChange={(e) => setAutoRefresh(e.target.checked)}
                            className="rounded border-zinc-600 bg-zinc-800 text-purple-500 focus:ring-purple-500"
                        />
                        Auto-refresh
                    </label>

                    {/* Manual refresh */}
                    <button
                        onClick={fetchLiveActivity}
                        disabled={loading}
                        className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Refresh
                    </button>
                </div>
            </div>

            {/* Last update */}
            {lastUpdate && (
                <p className="text-xs text-zinc-500 mb-4">
                    Last updated: {lastUpdate.toLocaleTimeString()}
                </p>
            )}

            {/* Messages Inbox Panel */}
            {showMessages && (
                <div className="mb-6 p-4 bg-zinc-900/50 border border-purple-500/20 rounded-xl">
                    <div className="flex items-center justify-between mb-4">
                        <h2 className="text-lg font-semibold flex items-center gap-2">
                            <Inbox className="w-5 h-5 text-purple-400" />
                            User Messages
                            {unreadCount > 0 && (
                                <span className="px-2 py-0.5 text-xs bg-red-500/20 text-red-400 rounded-full">
                                    {unreadCount} unread
                                </span>
                            )}
                        </h2>
                        <button
                            onClick={() => setShowMessages(false)}
                            className="text-zinc-500 hover:text-white"
                        >
                            ✕
                        </button>
                    </div>

                    {messages.length === 0 ? (
                        <div className="text-center py-8 text-zinc-500">
                            <Mail className="w-10 h-10 mx-auto mb-2 opacity-50" />
                            <p>No messages yet</p>
                        </div>
                    ) : (
                        <div className="space-y-3 max-h-96 overflow-y-auto">
                            {messages.map((msg) => (
                                <div
                                    key={msg.id}
                                    className={cn(
                                        "p-3 rounded-lg border transition-all",
                                        msg.read
                                            ? "bg-zinc-800/50 border-zinc-700"
                                            : "bg-purple-500/10 border-purple-500/30"
                                    )}
                                >
                                    <div className="flex items-start justify-between gap-3">
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2 mb-1">
                                                {msg.read ? (
                                                    <MailOpen className="w-4 h-4 text-zinc-500" />
                                                ) : (
                                                    <Mail className="w-4 h-4 text-purple-400" />
                                                )}
                                                <span className="font-medium text-sm text-white">
                                                    {msg.user_name || msg.user_email.split("@")[0]}
                                                </span>
                                                <span className="text-xs px-2 py-0.5 bg-zinc-700 rounded text-zinc-300">
                                                    {msg.subject}
                                                </span>
                                            </div>
                                            <p className="text-xs text-zinc-500 mb-2">{msg.user_email}</p>
                                            <p className="text-sm text-zinc-300">{msg.message}</p>
                                            <p className="text-xs text-zinc-600 mt-2">
                                                {new Date(msg.timestamp).toLocaleString()}
                                            </p>
                                        </div>
                                        <div className="flex items-center gap-1 shrink-0">
                                            {!msg.read && (
                                                <button
                                                    onClick={() => markAsRead(msg.id)}
                                                    className="p-1.5 rounded hover:bg-green-500/20 text-green-400 transition"
                                                    title="Mark as read"
                                                >
                                                    <Check className="w-4 h-4" />
                                                </button>
                                            )}
                                            <button
                                                onClick={() => deleteMessage(msg.id)}
                                                className="p-1.5 rounded hover:bg-red-500/20 text-red-400 transition"
                                                title="Delete"
                                            >
                                                <Trash2 className="w-4 h-4" />
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}

            {/* Stats cards */}
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 mb-6">
                <div className="p-4 bg-zinc-900/50 border border-zinc-800 rounded-xl">
                    <div className="flex items-center gap-2 text-green-400 mb-1">
                        <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                        <span className="text-sm font-medium">Online Now</span>
                    </div>
                    <p className="text-3xl font-bold text-white">{onlineUsers.length}</p>
                </div>

                <div className="p-4 bg-zinc-900/50 border border-zinc-800 rounded-xl">
                    <div className="flex items-center gap-2 text-yellow-400 mb-1">
                        <div className="w-2 h-2 rounded-full bg-yellow-500" />
                        <span className="text-sm font-medium">Away</span>
                    </div>
                    <p className="text-3xl font-bold text-white">{awayUsers.length}</p>
                </div>

                <div className="p-4 bg-zinc-900/50 border border-zinc-800 rounded-xl col-span-2 sm:col-span-1">
                    <div className="flex items-center gap-2 text-purple-400 mb-1">
                        <Users className="w-4 h-4" />
                        <span className="text-sm font-medium">Total Active</span>
                    </div>
                    <p className="text-3xl font-bold text-white">{users.length}</p>
                </div>
            </div>

            {/* User list */}
            {loading && users.length === 0 ? (
                <div className="space-y-4">
                    {[...Array(3)].map((_, i) => (
                        <div key={i} className="p-4 rounded-xl border border-zinc-800 animate-pulse">
                            <div className="flex items-start gap-4">
                                <div className="w-12 h-12 rounded-xl bg-zinc-800" />
                                <div className="flex-1 space-y-2">
                                    <div className="h-4 w-32 bg-zinc-800 rounded" />
                                    <div className="h-3 w-48 bg-zinc-800 rounded" />
                                    <div className="h-6 w-24 bg-zinc-800 rounded mt-2" />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            ) : users.length === 0 ? (
                <div className="text-center py-12">
                    <Users className="w-12 h-12 text-zinc-600 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-zinc-400 mb-2">No active users</h3>
                    <p className="text-sm text-zinc-500">
                        No users have been active in the last 10 minutes
                    </p>
                </div>
            ) : (
                <div className="space-y-4">
                    {/* Online users */}
                    {onlineUsers.length > 0 && (
                        <div>
                            <h2 className="text-sm font-medium text-green-400 mb-3 flex items-center gap-2">
                                <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                                Online Now ({onlineUsers.length})
                            </h2>
                            <div className="space-y-3">
                                {onlineUsers.map(user => (
                                    <LiveUserCard key={user.id} user={user} />
                                ))}
                            </div>
                        </div>
                    )}

                    {/* Away users */}
                    {awayUsers.length > 0 && (
                        <div className="mt-6">
                            <h2 className="text-sm font-medium text-yellow-400 mb-3 flex items-center gap-2">
                                <div className="w-2 h-2 rounded-full bg-yellow-500" />
                                Recently Active ({awayUsers.length})
                            </h2>
                            <div className="space-y-3">
                                {awayUsers.map(user => (
                                    <LiveUserCard key={user.id} user={user} />
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            )}

            {/* Back to users */}
            <div className="mt-8 pt-6 border-t border-zinc-800">
                <Link
                    href="/admin/users"
                    className="text-sm text-zinc-400 hover:text-white transition"
                >
                    ← Back to all users
                </Link>
            </div>
        </div>
    )
}
