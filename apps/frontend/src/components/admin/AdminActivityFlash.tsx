"use client"

/**
 * Admin Activity Flash - Real-time notifications for user login/logout/activity
 * Only visible to admins in the TopBar
 */

import { useState, useEffect, useCallback, useRef } from "react"
import { LogIn, LogOut, Clock, X, User, GraduationCap, Brain, UserPlus } from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface ActivityEvent {
    id: string
    type: "login" | "logout" | "inactive" | "registration" | "exam_completed" | "ai_quiz"
    user_email: string
    user_name: string | null
    timestamp: Date
    details?: string
}

interface AdminActivityFlashProps {
    className?: string
}

export function AdminActivityFlash({ className }: AdminActivityFlashProps) {
    const { user } = useAuth()
    const [events, setEvents] = useState<ActivityEvent[]>([])
    const [visible, setVisible] = useState<string | null>(null)
    const lastCheckedRef = useRef<Date>(new Date())
    const seenEventsRef = useRef<Set<string>>(new Set())

    // Only show for admin
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"

    // Check for new activity events
    const checkActivity = useCallback(async () => {
        if (!isAdmin) return

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            // Use a timestamp from 30 seconds ago to catch any recent events
            const sinceTime = new Date(Date.now() - 30000)
            
            const response = await fetch(`${API_BASE_URL}/api/admin/v2/activity-flash?since=${sinceTime.toISOString()}`, {
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })

            if (response.ok) {
                const data = await response.json()
                if (data.events && data.events.length > 0) {
                    // Filter out events we've already seen
                    const newEvents = data.events
                        .map((e: any) => ({
                            ...e,
                            timestamp: new Date(e.timestamp)
                        }))
                        .filter((e: ActivityEvent) => !seenEventsRef.current.has(e.id))

                    if (newEvents.length > 0) {
                        // Mark these events as seen
                        newEvents.forEach((e: ActivityEvent) => seenEventsRef.current.add(e.id))
                        
                        // Keep only last 100 seen events to prevent memory leak
                        if (seenEventsRef.current.size > 100) {
                            const arr = Array.from(seenEventsRef.current)
                            seenEventsRef.current = new Set(arr.slice(-50))
                        }

                        setEvents(prev => [...newEvents, ...prev].slice(0, 10))

                        // Show the latest event
                        setVisible(newEvents[0].id)
                        // Auto-hide after 4 seconds
                        setTimeout(() => setVisible(null), 4000)
                    }
                }
                lastCheckedRef.current = new Date()
            }
        } catch (error) {
            console.debug("[AdminActivityFlash] Poll error:", error)
        }
    }, [isAdmin])

    // Poll for activity every 5 seconds
    useEffect(() => {
        if (!isAdmin) return

        // Initial check after short delay
        const initialTimeout = setTimeout(checkActivity, 1000)

        const interval = setInterval(checkActivity, 5000)
        return () => {
            clearTimeout(initialTimeout)
            clearInterval(interval)
        }
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
            case "registration": return <UserPlus className="w-4 h-4" />
            case "exam_completed": return <GraduationCap className="w-4 h-4" />
            case "ai_quiz": return <Brain className="w-4 h-4" />
            default: return <User className="w-4 h-4" />
        }
    }

    const getMessage = () => {
        const name = currentEvent.user_name || currentEvent.user_email.split("@")[0]
        switch (currentEvent.type) {
            case "login": return `${name} logged in`
            case "logout": return `${name} logged out`
            case "inactive": return `${name} went inactive`
            case "registration": return `${name} registered`
            case "exam_completed": return currentEvent.details || `${name} completed an exam`
            case "ai_quiz": return currentEvent.details || `${name} completed AI Quiz`
            default: return `${name} activity`
        }
    }

    const getColors = () => {
        switch (currentEvent.type) {
            case "login": return "from-green-500/20 to-emerald-500/10 border-green-500/30 text-green-400"
            case "logout": return "from-orange-500/20 to-amber-500/10 border-orange-500/30 text-orange-400"
            case "inactive": return "from-yellow-500/20 to-amber-500/10 border-yellow-500/30 text-yellow-400"
            case "registration": return "from-pink-500/20 to-rose-500/10 border-pink-500/30 text-pink-400"
            case "exam_completed": return "from-purple-500/20 to-violet-500/10 border-purple-500/30 text-purple-400"
            case "ai_quiz": return "from-blue-500/20 to-cyan-500/10 border-blue-500/30 text-blue-400"
            default: return "from-zinc-500/20 to-zinc-500/10 border-zinc-500/30 text-zinc-400"
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
