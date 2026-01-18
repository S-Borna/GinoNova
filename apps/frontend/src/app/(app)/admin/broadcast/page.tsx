"use client"

/**
 * Admin Broadcast - Send messages to all logged-in users
 */

import { useState, useEffect, useCallback } from "react"
import { 
    Megaphone, 
    Send, 
    Trash2, 
    RefreshCw,
    Info,
    AlertTriangle,
    CheckCircle,
    AlertCircle,
    Clock
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface BroadcastMessage {
    id: string
    message: string
    type: string
    created_at: string
    expires_at: string | null
    created_by: string
}

const messageTypes = [
    { value: "info", label: "Info", icon: Info, color: "text-blue-400 bg-blue-500/10" },
    { value: "success", label: "Success", icon: CheckCircle, color: "text-green-400 bg-green-500/10" },
    { value: "warning", label: "Warning", icon: AlertTriangle, color: "text-yellow-400 bg-yellow-500/10" },
    { value: "error", label: "Alert", icon: AlertCircle, color: "text-red-400 bg-red-500/10" },
]

export default function BroadcastPage() {
    const [message, setMessage] = useState("")
    const [type, setType] = useState("info")
    const [duration, setDuration] = useState(60)
    const [sending, setSending] = useState(false)
    const [broadcasts, setBroadcasts] = useState<BroadcastMessage[]>([])
    const [loading, setLoading] = useState(true)
    const [success, setSuccess] = useState<string | null>(null)
    const [error, setError] = useState<string | null>(null)

    // Fetch active broadcasts
    const fetchBroadcasts = useCallback(async () => {
        const token = getToken()
        if (!token) return

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/broadcast/active`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const data = await res.json()
                setBroadcasts(data.messages || [])
            }
        } catch (err) {
            console.error("Failed to fetch broadcasts:", err)
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchBroadcasts()
    }, [fetchBroadcasts])

    // Send broadcast
    const sendBroadcast = async () => {
        if (!message.trim()) {
            setError("Please enter a message")
            return
        }

        const token = getToken()
        if (!token) return

        setSending(true)
        setError(null)
        setSuccess(null)

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/broadcast`, {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message.trim(),
                    type,
                    duration_minutes: duration
                })
            })

            if (res.ok) {
                setSuccess("Broadcast sent successfully!")
                setMessage("")
                fetchBroadcasts()
                setTimeout(() => setSuccess(null), 3000)
            } else {
                const data = await res.json()
                setError(data.detail || "Failed to send broadcast")
            }
        } catch (err) {
            setError("Failed to send broadcast")
        } finally {
            setSending(false)
        }
    }

    // Delete broadcast
    const deleteBroadcast = async (id: string) => {
        const token = getToken()
        if (!token) return

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/broadcast/${id}`, {
                method: "DELETE",
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                fetchBroadcasts()
            }
        } catch (err) {
            console.error("Failed to delete broadcast:", err)
        }
    }

    const selectedType = messageTypes.find(t => t.value === type)

    return (
        <div className="p-6 max-w-4xl mx-auto">
            {/* Header */}
            <div className="flex items-center gap-3 mb-8">
                <div className="p-3 rounded-xl bg-purple-500/10">
                    <Megaphone className="w-7 h-7 text-purple-400" />
                </div>
                <div>
                    <h1 className="text-2xl font-bold">Broadcast Message</h1>
                    <p className="text-sm text-zinc-400">
                        Send messages to all logged-in users
                    </p>
                </div>
            </div>

            {/* Compose Section */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-8">
                <h2 className="text-lg font-semibold mb-4">Compose Message</h2>

                {/* Message Type */}
                <div className="mb-4">
                    <label className="block text-sm text-zinc-400 mb-2">Message Type</label>
                    <div className="flex flex-wrap gap-2">
                        {messageTypes.map((t) => (
                            <button
                                key={t.value}
                                onClick={() => setType(t.value)}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-lg border transition",
                                    type === t.value
                                        ? `${t.color} border-current`
                                        : "border-zinc-700 text-zinc-400 hover:border-zinc-600"
                                )}
                            >
                                <t.icon className="w-4 h-4" />
                                {t.label}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Message Input */}
                <div className="mb-4">
                    <label className="block text-sm text-zinc-400 mb-2">Message</label>
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder="Enter your message to all users..."
                        className="w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white placeholder-zinc-500 focus:outline-none focus:border-purple-500 resize-none"
                        rows={3}
                        maxLength={500}
                    />
                    <div className="text-xs text-zinc-500 mt-1 text-right">
                        {message.length}/500 characters
                    </div>
                </div>

                {/* Duration */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-2">
                        Duration (how long before message expires)
                    </label>
                    <div className="flex flex-wrap gap-2">
                        {[15, 30, 60, 120, 240, 1440].map((mins) => (
                            <button
                                key={mins}
                                onClick={() => setDuration(mins)}
                                className={cn(
                                    "px-3 py-1.5 rounded-lg text-sm transition",
                                    duration === mins
                                        ? "bg-purple-500 text-white"
                                        : "bg-zinc-800 text-zinc-400 hover:bg-zinc-700"
                                )}
                            >
                                {mins < 60 ? `${mins}m` : mins === 1440 ? "24h" : `${mins / 60}h`}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Preview */}
                {message && (
                    <div className="mb-6">
                        <label className="block text-sm text-zinc-400 mb-2">Preview</label>
                        <div className={cn(
                            "flex items-center gap-2 px-3 py-2 rounded-xl",
                            "bg-gradient-to-r border",
                            type === "info" && "from-blue-500/20 to-cyan-500/10 border-blue-500/30 text-blue-400",
                            type === "success" && "from-green-500/20 to-emerald-500/10 border-green-500/30 text-green-400",
                            type === "warning" && "from-yellow-500/20 to-amber-500/10 border-yellow-500/30 text-yellow-400",
                            type === "error" && "from-red-500/20 to-rose-500/10 border-red-500/30 text-red-400"
                        )}>
                            {selectedType && <selectedType.icon className="w-4 h-4 shrink-0" />}
                            <span className="text-sm">{message}</span>
                        </div>
                    </div>
                )}

                {/* Error/Success messages */}
                {error && (
                    <div className="mb-4 p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm">
                        {error}
                    </div>
                )}
                {success && (
                    <div className="mb-4 p-3 rounded-lg bg-green-500/10 border border-green-500/30 text-green-400 text-sm">
                        {success}
                    </div>
                )}

                {/* Send Button */}
                <button
                    onClick={sendBroadcast}
                    disabled={sending || !message.trim()}
                    className={cn(
                        "flex items-center justify-center gap-2 w-full py-3 rounded-xl font-medium transition",
                        "bg-purple-600 hover:bg-purple-500 text-white",
                        "disabled:opacity-50 disabled:cursor-not-allowed"
                    )}
                >
                    {sending ? (
                        <RefreshCw className="w-5 h-5 animate-spin" />
                    ) : (
                        <Send className="w-5 h-5" />
                    )}
                    {sending ? "Sending..." : "Send Broadcast"}
                </button>
            </div>

            {/* Active Broadcasts */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                <div className="flex items-center justify-between mb-4">
                    <h2 className="text-lg font-semibold">Active Broadcasts</h2>
                    <button
                        onClick={fetchBroadcasts}
                        className="p-2 rounded-lg hover:bg-zinc-800 transition"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                    </button>
                </div>

                {loading ? (
                    <div className="space-y-3">
                        {[...Array(2)].map((_, i) => (
                            <div key={i} className="h-16 bg-zinc-800 rounded-lg animate-pulse" />
                        ))}
                    </div>
                ) : broadcasts.length === 0 ? (
                    <div className="text-center py-8 text-zinc-500">
                        <Megaphone className="w-10 h-10 mx-auto mb-2 opacity-50" />
                        <p>No active broadcasts</p>
                    </div>
                ) : (
                    <div className="space-y-3">
                        {broadcasts.map((b) => {
                            const typeInfo = messageTypes.find(t => t.value === b.type) || messageTypes[0]
                            return (
                                <div
                                    key={b.id}
                                    className="flex items-start gap-3 p-4 bg-zinc-800/50 rounded-lg border border-zinc-700"
                                >
                                    <div className={cn("p-2 rounded-lg", typeInfo.color)}>
                                        <typeInfo.icon className="w-4 h-4" />
                                    </div>
                                    <div className="flex-1 min-w-0">
                                        <p className="text-white">{b.message}</p>
                                        <div className="flex items-center gap-3 mt-2 text-xs text-zinc-500">
                                            <span className="flex items-center gap-1">
                                                <Clock className="w-3 h-3" />
                                                {new Date(b.created_at).toLocaleString("sv-SE")}
                                            </span>
                                            {b.expires_at && (
                                                <span>
                                                    Expires: {new Date(b.expires_at).toLocaleString("sv-SE")}
                                                </span>
                                            )}
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => deleteBroadcast(b.id)}
                                        className="p-2 rounded-lg text-zinc-500 hover:text-red-400 hover:bg-red-500/10 transition"
                                    >
                                        <Trash2 className="w-4 h-4" />
                                    </button>
                                </div>
                            )
                        })}
                    </div>
                )}
            </div>
        </div>
    )
}
