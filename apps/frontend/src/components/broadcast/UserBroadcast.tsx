"use client"

/**
 * User Broadcast Message - Displays admin broadcast messages to all users
 * Shows in TopBar, must be manually dismissed by user
 */

import React, { useState, useEffect, useCallback } from "react"
import { X, Info, AlertTriangle, CheckCircle, AlertCircle, Megaphone } from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface BroadcastMessage {
    id: string
    message: string
    type: "info" | "warning" | "success" | "error"
    created_at: string
}

interface UserBroadcastProps {
    className?: string
}

// Get dismissed message IDs from localStorage
const getDismissedIds = (): Set<string> => {
    if (typeof window === "undefined") return new Set()
    try {
        const stored = localStorage.getItem("dismissed_broadcasts")
        if (stored) {
            const parsed = JSON.parse(stored)
            // Clean up old entries (older than 24 hours)
            const now = Date.now()
            const valid = Object.entries(parsed)
                .filter(([_, timestamp]) => now - (timestamp as number) < 24 * 60 * 60 * 1000)
            localStorage.setItem("dismissed_broadcasts", JSON.stringify(Object.fromEntries(valid)))
            return new Set(valid.map(([id]) => id))
        }
    } catch { }
    return new Set()
}

// Save dismissed message ID to localStorage
const saveDismissedId = (id: string) => {
    if (typeof window === "undefined") return
    try {
        const stored = localStorage.getItem("dismissed_broadcasts")
        const parsed = stored ? JSON.parse(stored) : {}
        parsed[id] = Date.now()
        localStorage.setItem("dismissed_broadcasts", JSON.stringify(parsed))
    } catch { }
}

export function UserBroadcast({ className }: UserBroadcastProps) {
    const { user } = useAuth()
    const [messages, setMessages] = useState<BroadcastMessage[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const fetchingRef = React.useRef(false)
    const dismissedIdsRef = React.useRef<Set<string>>(getDismissedIds())

    // Fetch messages - with deduplication to prevent "glapping"
    const fetchMessages = useCallback(async () => {
        if (!user) return
        if (fetchingRef.current) return // Prevent concurrent fetches

        fetchingRef.current = true

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/user/messages`, {
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })

            if (response.ok) {
                const data = await response.json()
                const allMessages = data.messages || []

                // Filter out locally dismissed messages
                const newMessages = allMessages.filter(
                    (m: BroadcastMessage) => !dismissedIdsRef.current.has(m.id)
                )

                // Only update if message IDs changed (prevents flashing)
                setMessages(prev => {
                    const prevIds = prev.map(m => m.id).sort().join(",")
                    const newIds = newMessages.map((m: BroadcastMessage) => m.id).sort().join(",")
                    if (prevIds === newIds) return prev
                    return newMessages
                })
            }
        } catch (error) {
            // Silent fail
        } finally {
            fetchingRef.current = false
        }
    }, [user])

    // Poll for messages every 30 seconds
    useEffect(() => {
        if (!user) return

        fetchMessages()
        const interval = setInterval(fetchMessages, 3000)
        return () => clearInterval(interval)
    }, [user, fetchMessages])

    // Dismiss a message - persist locally AND to backend
    const dismissMessage = async (messageId: string) => {
        // Immediately save to localStorage so it won't come back
        saveDismissedId(messageId)
        dismissedIdsRef.current.add(messageId)

        // Remove from local state immediately
        setMessages(prev => prev.filter(m => m.id !== messageId))

        // Reset index if needed
        if (currentIndex >= messages.length - 1) {
            setCurrentIndex(Math.max(0, messages.length - 2))
        }

        // Also notify backend (fire and forget)
        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            await fetch(`${API_BASE_URL}/api/admin/v2/user/messages/${messageId}/dismiss`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })
        } catch (error) {
            // Already saved locally, so ignore backend errors
        }
    }

    // Don't render if no messages
    if (messages.length === 0) return null

    const currentMessage = messages[currentIndex]
    if (!currentMessage) return null

    const getIcon = () => {
        switch (currentMessage.type) {
            case "info": return <Info className="w-4 h-4 shrink-0" />
            case "warning": return <AlertTriangle className="w-4 h-4 shrink-0" />
            case "success": return <CheckCircle className="w-4 h-4 shrink-0" />
            case "error": return <AlertCircle className="w-4 h-4 shrink-0" />
            default: return <Megaphone className="w-4 h-4 shrink-0" />
        }
    }

    const getColors = () => {
        switch (currentMessage.type) {
            case "info":
                return "from-blue-500/20 to-cyan-500/10 border-blue-500/30 text-blue-400"
            case "warning":
                return "from-yellow-500/20 to-amber-500/10 border-yellow-500/30 text-yellow-400"
            case "success":
                return "from-green-500/20 to-emerald-500/10 border-green-500/30 text-green-400"
            case "error":
                return "from-red-500/20 to-rose-500/10 border-red-500/30 text-red-400"
            default:
                return "from-purple-500/20 to-pink-500/10 border-purple-500/30 text-purple-400"
        }
    }

    return (
        <div
            className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-xl",
                "bg-gradient-to-r border backdrop-blur-sm",
                "animate-in fade-in slide-in-from-top-2 duration-300",
                "max-w-xs sm:max-w-sm md:max-w-md",
                getColors(),
                className
            )}
        >
            {/* Icon */}
            <div className="shrink-0">
                {getIcon()}
            </div>

            {/* Message */}
            <span className="text-xs sm:text-sm font-medium line-clamp-2 flex-1">
                {currentMessage.message}
            </span>

            {/* Message counter (if multiple) */}
            {messages.length > 1 && (
                <div className="shrink-0 flex items-center gap-1">
                    <button
                        onClick={() => setCurrentIndex(i => Math.max(0, i - 1))}
                        disabled={currentIndex === 0}
                        className="p-0.5 rounded hover:bg-white/10 disabled:opacity-30"
                    >
                        ‹
                    </button>
                    <span className="text-[10px] opacity-60">
                        {currentIndex + 1}/{messages.length}
                    </span>
                    <button
                        onClick={() => setCurrentIndex(i => Math.min(messages.length - 1, i + 1))}
                        disabled={currentIndex === messages.length - 1}
                        className="p-0.5 rounded hover:bg-white/10 disabled:opacity-30"
                    >
                        ›
                    </button>
                </div>
            )}

            {/* Dismiss button */}
            <button
                onClick={() => dismissMessage(currentMessage.id)}
                className="p-1 rounded-full hover:bg-white/10 transition-colors shrink-0"
                aria-label="Dismiss message"
            >
                <X className="w-3.5 h-3.5" />
            </button>
        </div>
    )
}

export default UserBroadcast
