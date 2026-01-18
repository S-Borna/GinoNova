"use client"

/**
 * Admin Activity Flash - Real-time notifications for user login/logout/activity
 * Only visible to admins in the TopBar
 */

import { useState, useEffect, useCallback } from "react"
import { LogIn, LogOut, Clock, X, User } from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface ActivityEvent {
    id: string
    type: "login" | "logout" | "inactive"
    user_email: string
    user_name: string | null
    timestamp: Date
}

interface AdminActivityFlashProps {
    className?: string
}

export function AdminActivityFlash({ className }: AdminActivityFlashProps) {
    const { user } = useAuth()
    const [events, setEvents] = useState<ActivityEvent[]>([])
    const [visible, setVisible] = useState<string | null>(null)
    const [lastChecked, setLastChecked] = useState<Date>(new Date())

    // Only show for admin
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"

    // Check for new activity events
    const checkActivity = useCallback(async () => {
        if (!isAdmin) return

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/activity-flash?since=${lastChecked.toISOString()}`, {
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })

            if (response.ok) {
                const data = await response.json()
                if (data.events && data.events.length > 0) {
                    // Add new events
                    const newEvents = data.events.map((e: any) => ({
                        ...e,
                        timestamp: new Date(e.timestamp)
                    }))
                    
                    setEvents(prev => [...newEvents, ...prev].slice(0, 10))
                    
                    // Show the latest event
                    if (newEvents.length > 0) {
                        setVisible(newEvents[0].id)
                        // Auto-hide after 3 seconds
                        setTimeout(() => setVisible(null), 3000)
                    }
                }
                setLastChecked(new Date())
            }
        } catch (error) {
            // Silent fail - don't spam console
        }
    }, [isAdmin, lastChecked])

    // Poll for activity every 10 seconds
    useEffect(() => {
        if (!isAdmin) return

        // Initial check
        checkActivity()

        const interval = setInterval(checkActivity, 10000)
        return () => clearInterval(interval)
    }, [isAdmin, checkActivity])

    // Don't render anything if not admin
    if (!isAdmin) return null

    const currentEvent = events.find(e => e.id === visible)

    if (!currentEvent) return null

    const getIcon = () => {
        switch (currentEvent.type) {
            case "login": return <LogIn className="w-4 h-4" />
            case "logout": return <LogOut className="w-4 h-4" />
            case "inactive": return <Clock className="w-4 h-4" />
        }
    }

    const getMessage = () => {
        const name = currentEvent.user_name || currentEvent.user_email.split("@")[0]
        switch (currentEvent.type) {
            case "login": return `${name} logged in`
            case "logout": return `${name} logged out`
            case "inactive": return `${name} went inactive`
        }
    }

    const getColors = () => {
        switch (currentEvent.type) {
            case "login": return "from-green-500/20 to-emerald-500/10 border-green-500/30 text-green-400"
            case "logout": return "from-orange-500/20 to-amber-500/10 border-orange-500/30 text-orange-400"
            case "inactive": return "from-yellow-500/20 to-amber-500/10 border-yellow-500/30 text-yellow-400"
        }
    }

    return (
        <div
            className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-full",
                "bg-gradient-to-r border backdrop-blur-sm",
                "animate-in fade-in slide-in-from-top-2 duration-300",
                getColors(),
                className
            )}
        >
            <div className="flex items-center gap-2">
                {getIcon()}
                <span className="text-xs font-medium whitespace-nowrap">
                    {getMessage()}
                </span>
            </div>
            <button
                onClick={() => setVisible(null)}
                className="p-0.5 rounded-full hover:bg-white/10 transition-colors"
                aria-label="Dismiss"
            >
                <X className="w-3 h-3" />
            </button>
        </div>
    )
}

export default AdminActivityFlash
