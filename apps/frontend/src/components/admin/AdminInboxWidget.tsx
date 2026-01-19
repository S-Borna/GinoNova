"use client"

/**
 * Admin Inbox Widget - Shows unread user messages in TopBar
 * Only visible to admin users
 */

import { useState, useEffect, useCallback, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import {
    Inbox,
    X,
    Check,
    Trash2,
    Mail,
    MailOpen,
    MessageSquare,
    ChevronDown
} from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

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

interface AdminInboxWidgetProps {
    className?: string
}

export function AdminInboxWidget({ className }: AdminInboxWidgetProps) {
    const { user } = useAuth()
    const [messages, setMessages] = useState<UserMessage[]>([])
    const [unreadCount, setUnreadCount] = useState(0)
    const [showDropdown, setShowDropdown] = useState(false)
    const [loading, setLoading] = useState(false)
    const fetchingRef = useRef(false)
    const prevUnreadCountRef = useRef(0)

    // Only show for admin
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"

    // 🔔 Play notification sound when new message arrives
    const playNotificationSound = useCallback(() => {
        try {
            // Create audio context and play a pleasant notification tone
            const audioContext = new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)()
            const oscillator = audioContext.createOscillator()
            const gainNode = audioContext.createGain()

            oscillator.connect(gainNode)
            gainNode.connect(audioContext.destination)

            // Two-tone notification (ding-dong effect)
            oscillator.frequency.setValueAtTime(880, audioContext.currentTime) // A5
            oscillator.frequency.setValueAtTime(659, audioContext.currentTime + 0.15) // E5

            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime)
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3)

            oscillator.start(audioContext.currentTime)
            oscillator.stop(audioContext.currentTime + 0.3)
        } catch {
            // Audio not available
        }
    }, [])

    // Fetch messages - with deduplication to prevent flashing
    const fetchMessages = useCallback(async () => {
        if (!isAdmin) return
        if (fetchingRef.current) return // Prevent concurrent fetches

        fetchingRef.current = true

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages`, {
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })

            if (response.ok) {
                const data = await response.json()
                const newMessages = data.messages || []
                const newUnread = data.unread || 0

                // 🔔 Play sound if unread count increased (new message!)
                if (newUnread > prevUnreadCountRef.current && prevUnreadCountRef.current !== 0) {
                    playNotificationSound()
                }
                prevUnreadCountRef.current = newUnread

                // Only update messages if IDs changed (prevents flashing)
                setMessages(prev => {
                    const prevIds = prev.map(m => m.id).sort().join(",")
                    const newIds = newMessages.map((m: UserMessage) => m.id).sort().join(",")
                    if (prevIds === newIds) return prev
                    return newMessages
                })
                setUnreadCount(newUnread)
            }
        } catch {
            // Silent fail
        } finally {
            fetchingRef.current = false
        }
    }, [isAdmin, playNotificationSound])

    // Mark as read
    const markAsRead = async (messageId: string) => {
        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages/${messageId}/read`, {
                method: "POST",
                headers: { "Authorization": `Bearer ${token}` }
            })
            fetchMessages()
        } catch {
            // Silent fail
        }
    }

    // Delete message
    const deleteMessage = async (messageId: string) => {
        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            await fetch(`${API_BASE_URL}/api/admin/v2/contact/messages/${messageId}`, {
                method: "DELETE",
                headers: { "Authorization": `Bearer ${token}` }
            })
            fetchMessages()
        } catch {
            // Silent fail
        }
    }

    // Send heartbeat to indicate admin is online
    const sendHeartbeat = useCallback(async () => {
        if (!isAdmin) return

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            await fetch(`${API_BASE_URL}/api/admin/v2/status/heartbeat`, {
                method: "POST",
                headers: { "Authorization": `Bearer ${token}` }
            })
        } catch {
            // Silent fail
        }
    }, [isAdmin])

    // Poll for new messages every 10 seconds + send heartbeat
    useEffect(() => {
        if (!isAdmin) return

        fetchMessages()
        sendHeartbeat()

        const interval = setInterval(() => {
            fetchMessages()
            sendHeartbeat()
        }, 3000)

        return () => clearInterval(interval)
    }, [isAdmin, fetchMessages, sendHeartbeat])

    // Don't render for non-admin
    if (!isAdmin) return null

    return (
        <div className="relative">
            {/* Inbox Button */}
            <motion.button
                onClick={() => setShowDropdown(!showDropdown)}
                className={cn(
                    "hidden md:flex items-center gap-2 px-3 py-1.5 rounded-xl",
                    "border backdrop-blur-sm transition-all duration-300",
                    unreadCount > 0
                        ? "bg-gradient-to-r from-amber-500/15 to-yellow-500/10 border-amber-500/30"
                        : "bg-neutral-500/10 border-neutral-500/20",
                    className
                )}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                <div className="relative">
                    <Inbox className={cn(
                        "w-4 h-4",
                        unreadCount > 0 ? "text-amber-400" : "text-neutral-400"
                    )} />
                    {unreadCount > 0 && (
                        <span className="absolute -top-1.5 -right-1.5 w-4 h-4 rounded-full bg-amber-500 text-[10px] font-bold text-black flex items-center justify-center animate-pulse">
                            {unreadCount > 9 ? "9+" : unreadCount}
                        </span>
                    )}
                </div>
                <span className={cn(
                    "text-xs font-medium",
                    unreadCount > 0 ? "text-amber-300" : "text-neutral-500"
                )}>
                    Inbox
                </span>
                <ChevronDown className={cn(
                    "w-3 h-3 transition-transform",
                    showDropdown && "rotate-180",
                    unreadCount > 0 ? "text-amber-400" : "text-neutral-500"
                )} />
            </motion.button>

            {/* Dropdown */}
            <AnimatePresence>
                {showDropdown && (
                    <>
                        {/* Backdrop */}
                        <div
                            className="fixed inset-0 z-40"
                            onClick={() => setShowDropdown(false)}
                        />

                        {/* Panel */}
                        <motion.div
                            initial={{ opacity: 0, y: 10, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            exit={{ opacity: 0, y: 10, scale: 0.95 }}
                            className={cn(
                                "absolute top-full right-0 mt-2 z-50",
                                "w-80 max-h-96 overflow-hidden",
                                "bg-[#1a1a2e] border border-amber-500/20 rounded-xl",
                                "shadow-2xl shadow-amber-500/10"
                            )}
                        >
                            {/* Header */}
                            <div className="flex items-center justify-between p-3 border-b border-white/5">
                                <div className="flex items-center gap-2">
                                    <MessageSquare className="w-4 h-4 text-amber-400" />
                                    <span className="font-medium text-sm">User Messages</span>
                                    {unreadCount > 0 && (
                                        <span className="px-1.5 py-0.5 text-[10px] bg-amber-500/20 text-amber-400 rounded">
                                            {unreadCount} new
                                        </span>
                                    )}
                                </div>
                                <button
                                    onClick={() => setShowDropdown(false)}
                                    className="p-1 rounded hover:bg-white/5"
                                >
                                    <X className="w-4 h-4 text-neutral-400" />
                                </button>
                            </div>

                            {/* Messages */}
                            <div className="overflow-y-auto max-h-72">
                                {messages.length === 0 ? (
                                    <div className="py-8 text-center text-neutral-500">
                                        <Mail className="w-8 h-8 mx-auto mb-2 opacity-50" />
                                        <p className="text-sm">No messages yet</p>
                                    </div>
                                ) : (
                                    <div className="divide-y divide-white/5">
                                        {messages.slice(0, 5).map((msg) => (
                                            <div
                                                key={msg.id}
                                                className={cn(
                                                    "p-3 transition-colors",
                                                    msg.read ? "bg-transparent" : "bg-amber-500/5"
                                                )}
                                            >
                                                <div className="flex items-start gap-2">
                                                    <div className={cn(
                                                        "mt-0.5 p-1 rounded",
                                                        msg.read ? "bg-neutral-700" : "bg-amber-500/20"
                                                    )}>
                                                        {msg.read ? (
                                                            <MailOpen className="w-3 h-3 text-neutral-400" />
                                                        ) : (
                                                            <Mail className="w-3 h-3 text-amber-400" />
                                                        )}
                                                    </div>
                                                    <div className="flex-1 min-w-0">
                                                        <div className="flex items-center gap-2 mb-0.5">
                                                            <span className="text-xs font-medium text-white truncate">
                                                                {msg.user_name || msg.user_email.split("@")[0]}
                                                            </span>
                                                            <span className="text-[10px] px-1.5 py-0.5 bg-zinc-700 rounded text-zinc-400">
                                                                {msg.subject}
                                                            </span>
                                                        </div>
                                                        <p className="text-xs text-neutral-400 line-clamp-2">
                                                            {msg.message}
                                                        </p>
                                                        <p className="text-[10px] text-neutral-600 mt-1">
                                                            {new Date(msg.timestamp).toLocaleString()}
                                                        </p>
                                                    </div>
                                                    <div className="flex items-center gap-1">
                                                        {!msg.read && (
                                                            <button
                                                                onClick={() => markAsRead(msg.id)}
                                                                className="p-1 rounded hover:bg-green-500/20 text-green-400"
                                                                title="Mark as read"
                                                            >
                                                                <Check className="w-3 h-3" />
                                                            </button>
                                                        )}
                                                        <button
                                                            onClick={() => deleteMessage(msg.id)}
                                                            className="p-1 rounded hover:bg-red-500/20 text-red-400"
                                                            title="Delete"
                                                        >
                                                            <Trash2 className="w-3 h-3" />
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>

                            {/* Footer */}
                            {messages.length > 5 && (
                                <div className="p-2 border-t border-white/5 text-center">
                                    <a
                                        href="/admin/users/live"
                                        className="text-xs text-amber-400 hover:text-amber-300"
                                    >
                                        View all {messages.length} messages →
                                    </a>
                                </div>
                            )}
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </div>
    )
}

export default AdminInboxWidget
