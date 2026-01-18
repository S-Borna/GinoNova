"use client"

/**
 * Admin Activity Flash - Real-time notifications for user login/logout/activity
 * Only visible to admins in the TopBar
 * 
 * Shows beautiful notifications for:
 * - User logins/logouts
 * - New registrations
 * - Completed exams (Tenta Simulator) with score and source
 * - AI Quiz completions with module name
 */

import { useState, useEffect, useCallback, useRef } from "react"
import { LogIn, LogOut, Clock, X, GraduationCap, Brain, UserPlus, Sparkles } from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface ActivityEvent {
    id: string
    type: "login" | "logout" | "inactive" | "registration" | "exam_completed" | "ai_quiz"
    user_email: string
    user_name: string | null
    timestamp: string
    details?: string
}

interface AdminActivityFlashProps {
    className?: string
}

export function AdminActivityFlash({ className }: AdminActivityFlashProps) {
    const { user } = useAuth()
    const [currentEvent, setCurrentEvent] = useState<ActivityEvent | null>(null)
    const seenEventsRef = useRef<Set<string>>(new Set())
    const pollIntervalRef = useRef<NodeJS.Timeout | null>(null)

    // Only show for admin
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"

    // Check for new activity events
    const checkActivity = useCallback(async () => {
        if (!isAdmin) return

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) {
                console.debug("[AdminActivityFlash] No auth token")
                return
            }

            // Get events from last 60 seconds
            const sinceTime = new Date(Date.now() - 60000).toISOString()
            
            const response = await fetch(
                `${API_BASE_URL}/api/admin/v2/activity-flash?since=${sinceTime}`,
                {
                    headers: {
                        "Authorization": `Bearer ${token}`,
                        "Content-Type": "application/json"
                    }
                }
            )

            if (!response.ok) {
                if (response.status === 401) {
                    console.debug("[AdminActivityFlash] Unauthorized - token may be expired")
                }
                return
            }

            const data = await response.json()
            
            if (data.events && data.events.length > 0) {
                // Find first event we haven't seen yet
                for (const event of data.events) {
                    if (!seenEventsRef.current.has(event.id)) {
                        seenEventsRef.current.add(event.id)
                        
                        // Limit seen events set size
                        if (seenEventsRef.current.size > 200) {
                            const arr = Array.from(seenEventsRef.current)
                            seenEventsRef.current = new Set(arr.slice(-100))
                        }
                        
                        // Show this event
                        setCurrentEvent(event)
                        
                        // Auto-hide after 5 seconds
                        setTimeout(() => {
                            setCurrentEvent(prev => prev?.id === event.id ? null : prev)
                        }, 5000)
                        
                        break // Only show one at a time
                    }
                }
            }
        } catch (error) {
            // Silent fail - don't spam console
        }
    }, [isAdmin])

    // Start polling when component mounts
    useEffect(() => {
        if (!isAdmin) return

        // Initial check
        checkActivity()

        // Poll every 5 seconds
        pollIntervalRef.current = setInterval(checkActivity, 5000)

        return () => {
            if (pollIntervalRef.current) {
                clearInterval(pollIntervalRef.current)
            }
        }
    }, [isAdmin, checkActivity])

    // Don't render if not admin or no event
    if (!isAdmin || !currentEvent) return null

    const getIcon = () => {
        switch (currentEvent.type) {
            case "login": return <LogIn className="w-4 h-4" />
            case "logout": return <LogOut className="w-4 h-4" />
            case "inactive": return <Clock className="w-4 h-4" />
            case "registration": return <UserPlus className="w-4 h-4" />
            case "exam_completed": return <GraduationCap className="w-4 h-4" />
            case "ai_quiz": return <Brain className="w-4 h-4" />
            default: return <Sparkles className="w-4 h-4" />
        }
    }

    const getMessage = () => {
        const name = currentEvent.user_name || currentEvent.user_email?.split("@")[0] || "User"
        
        switch (currentEvent.type) {
            case "login": 
                return <><span className="font-semibold">{name}</span> loggade in</>
            case "logout": 
                return <><span className="font-semibold">{name}</span> loggade ut</>
            case "inactive": 
                return <><span className="font-semibold">{name}</span> blev inaktiv</>
            case "registration": 
                return <><span className="font-semibold">{name}</span> registrerade sig 🎉</>
            case "exam_completed":
            case "ai_quiz":
                // Details already contains formatted message
                if (currentEvent.details) {
                    return <span>{currentEvent.details}</span>
                }
                return <><span className="font-semibold">{name}</span> slutförde {currentEvent.type === 'ai_quiz' ? 'AI Quiz' : 'tenta'}</>
            default: 
                return <><span className="font-semibold">{name}</span></>
        }
    }

    const getColors = () => {
        switch (currentEvent.type) {
            case "login": 
                return "from-green-500/20 to-emerald-500/10 border-green-500/40 text-green-300"
            case "logout": 
                return "from-orange-500/20 to-amber-500/10 border-orange-500/40 text-orange-300"
            case "inactive": 
                return "from-yellow-500/20 to-amber-500/10 border-yellow-500/40 text-yellow-300"
            case "registration": 
                return "from-pink-500/20 to-rose-500/10 border-pink-500/40 text-pink-300"
            case "exam_completed": 
                return "from-purple-500/20 to-violet-500/10 border-purple-500/40 text-purple-300"
            case "ai_quiz": 
                return "from-blue-500/20 to-cyan-500/10 border-blue-500/40 text-blue-300"
            default: 
                return "from-zinc-500/20 to-zinc-500/10 border-zinc-500/40 text-zinc-300"
        }
    }

    return (
        <div
            className={cn(
                "flex items-center gap-2.5 px-4 py-2 rounded-full",
                "bg-gradient-to-r border backdrop-blur-md",
                "shadow-lg shadow-black/20",
                "animate-in fade-in slide-in-from-top-2 duration-300",
                getColors(),
                className
            )}
        >
            <div className="flex items-center gap-2">
                <div className="p-1 rounded-full bg-white/10">
                    {getIcon()}
                </div>
                <span className="text-sm whitespace-nowrap">
                    {getMessage()}
                </span>
            </div>
            <button
                onClick={() => setCurrentEvent(null)}
                className="p-1 rounded-full hover:bg-white/10 transition-colors ml-1"
                aria-label="Stäng"
            >
                <X className="w-3.5 h-3.5" />
            </button>
        </div>
    )
}

export default AdminActivityFlash
