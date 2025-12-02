"use client"

/**
 * ============================================================================
 * XP POPUP - Premium Gamification Component ✨
 * ============================================================================
 *
 * Satisfying XP popup with:
 * - XP Gold (#F59E0B) glow effect
 * - Smooth slide-in animation
 * - Auto-dismiss after delay
 * - Stack multiple notifications
 *
 * @phase Premium Polish v1.0
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { cn } from "@/lib/utils"
import { Zap, Trophy, Star, Flame, Target } from "lucide-react"

// ============================================================================
// TYPES
// ============================================================================

export interface XPNotification {
    id: string
    amount: number
    reason: string
    type?: "xp" | "achievement" | "streak" | "milestone" | "bonus"
    timestamp?: number
}

interface XPPopupProps {
    notifications: XPNotification[]
    onDismiss?: (id: string) => void
    position?: "top-right" | "top-center" | "bottom-right" | "bottom-center"
    autoHideDuration?: number
}

// ============================================================================
// ICON MAPPING
// ============================================================================

const typeIcons = {
    xp: Zap,
    achievement: Trophy,
    streak: Flame,
    milestone: Target,
    bonus: Star,
}

const typeColors = {
    xp: {
        bg: "from-amber-500/20 to-yellow-500/10",
        border: "border-amber-500/30",
        text: "text-amber-400",
        glow: "shadow-[0_0_25px_rgba(245,158,11,0.4)]",
        iconBg: "bg-amber-500/20",
    },
    achievement: {
        bg: "from-purple-500/20 to-indigo-500/10",
        border: "border-purple-500/30",
        text: "text-purple-400",
        glow: "shadow-[0_0_25px_rgba(139,92,246,0.4)]",
        iconBg: "bg-purple-500/20",
    },
    streak: {
        bg: "from-orange-500/20 to-red-500/10",
        border: "border-orange-500/30",
        text: "text-orange-400",
        glow: "shadow-[0_0_25px_rgba(249,115,22,0.4)]",
        iconBg: "bg-orange-500/20",
    },
    milestone: {
        bg: "from-emerald-500/20 to-teal-500/10",
        border: "border-emerald-500/30",
        text: "text-emerald-400",
        glow: "shadow-[0_0_25px_rgba(34,211,172,0.4)]",
        iconBg: "bg-emerald-500/20",
    },
    bonus: {
        bg: "from-pink-500/20 to-rose-500/10",
        border: "border-pink-500/30",
        text: "text-pink-400",
        glow: "shadow-[0_0_25px_rgba(236,72,153,0.4)]",
        iconBg: "bg-pink-500/20",
    },
}

// ============================================================================
// SINGLE POPUP COMPONENT
// ============================================================================

interface SinglePopupProps {
    notification: XPNotification
    onDismiss: () => void
    autoHideDuration: number
    index: number
}

function SinglePopup({ notification, onDismiss, autoHideDuration, index }: SinglePopupProps) {
    const [isVisible, setIsVisible] = useState(false)
    const [isLeaving, setIsLeaving] = useState(false)

    const type = notification.type || "xp"
    const Icon = typeIcons[type]
    const colors = typeColors[type]

    useEffect(() => {
        // Animate in
        const showTimer = setTimeout(() => setIsVisible(true), 50 + index * 100)

        // Auto-hide
        const hideTimer = setTimeout(() => {
            setIsLeaving(true)
            setTimeout(onDismiss, 300)
        }, autoHideDuration)

        return () => {
            clearTimeout(showTimer)
            clearTimeout(hideTimer)
        }
    }, [autoHideDuration, onDismiss, index])

    return (
        <div
            className={cn(
                "relative flex items-center gap-3 p-4 rounded-xl",
                "bg-gradient-to-r", colors.bg,
                "border", colors.border,
                "backdrop-blur-xl",
                colors.glow,
                // Animation
                "transform transition-all duration-300 ease-out",
                isVisible && !isLeaving
                    ? "translate-x-0 opacity-100 scale-100"
                    : "translate-x-8 opacity-0 scale-95"
            )}
            style={{
                marginTop: index > 0 ? "8px" : "0",
            }}
        >
            {/* Icon */}
            <div className={cn(
                "flex-shrink-0 w-10 h-10 rounded-lg",
                "flex items-center justify-center",
                colors.iconBg
            )}>
                <Icon className={cn("w-5 h-5", colors.text)} />
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2">
                    <span className={cn(
                        "text-lg font-bold",
                        colors.text
                    )}>
                        +{notification.amount} XP
                    </span>
                    {type === "bonus" && (
                        <span className="text-xs px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-400 font-medium">
                            BONUS
                        </span>
                    )}
                </div>
                <p className="text-sm text-zinc-400 truncate">
                    {notification.reason}
                </p>
            </div>

            {/* Animated sparkles for XP */}
            {type === "xp" && (
                <>
                    <div className="absolute top-2 right-2 w-1 h-1 rounded-full bg-amber-400 animate-ping" />
                    <div className="absolute bottom-3 right-8 w-1 h-1 rounded-full bg-yellow-400 animate-ping" style={{ animationDelay: "150ms" }} />
                </>
            )}

            {/* Close on click */}
            <button
                onClick={() => {
                    setIsLeaving(true)
                    setTimeout(onDismiss, 300)
                }}
                className="absolute top-1 right-1 p-1 rounded-full text-zinc-500 hover:text-zinc-300 transition-colors"
            >
                <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
    )
}

// ============================================================================
// MAIN XP POPUP CONTAINER
// ============================================================================

export function XPPopup({
    notifications,
    onDismiss,
    position = "top-right",
    autoHideDuration = 4000,
}: XPPopupProps) {
    const handleDismiss = useCallback((id: string) => {
        onDismiss?.(id)
    }, [onDismiss])

    const positionClasses = {
        "top-right": "top-4 right-4",
        "top-center": "top-4 left-1/2 -translate-x-1/2",
        "bottom-right": "bottom-4 right-4",
        "bottom-center": "bottom-4 left-1/2 -translate-x-1/2",
    }

    if (notifications.length === 0) return null

    return (
        <div
            className={cn(
                "fixed z-[100] flex flex-col w-80",
                positionClasses[position]
            )}
        >
            {notifications.slice(0, 5).map((notification, index) => (
                <SinglePopup
                    key={notification.id}
                    notification={notification}
                    onDismiss={() => handleDismiss(notification.id)}
                    autoHideDuration={autoHideDuration}
                    index={index}
                />
            ))}
        </div>
    )
}

// ============================================================================
// HOOK FOR MANAGING XP NOTIFICATIONS
// ============================================================================

export function useXPNotifications() {
    const [notifications, setNotifications] = useState<XPNotification[]>([])

    const addNotification = useCallback((notification: Omit<XPNotification, "id" | "timestamp">) => {
        const newNotification: XPNotification = {
            ...notification,
            id: `xp-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
            timestamp: Date.now(),
        }
        setNotifications(prev => [...prev, newNotification])
    }, [])

    const dismissNotification = useCallback((id: string) => {
        setNotifications(prev => prev.filter(n => n.id !== id))
    }, [])

    const clearAll = useCallback(() => {
        setNotifications([])
    }, [])

    return {
        notifications,
        addNotification,
        dismissNotification,
        clearAll,
    }
}

export default XPPopup
