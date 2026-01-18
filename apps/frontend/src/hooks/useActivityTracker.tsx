"use client"

/**
 * Activity Tracker Hook - Tracks user's current page and action
 * Sends activity to backend for Live Activity monitoring
 */

import { useEffect, useCallback, useRef } from "react"
import { usePathname } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Map pathnames to human-readable page names
function getPageName(pathname: string): string {
    if (!pathname) return "Unknown"
    
    // Admin pages
    if (pathname.startsWith("/admin")) {
        if (pathname === "/admin") return "Admin Dashboard"
        if (pathname.includes("/users/live")) return "Live Activity Monitor"
        if (pathname.includes("/users")) return "User Management"
        if (pathname.includes("/broadcast")) return "Broadcast Center"
        if (pathname.includes("/analytics")) return "Analytics"
        if (pathname.includes("/ai-usage")) return "AI Usage"
        if (pathname.includes("/settings")) return "Admin Settings"
        return "Admin Panel"
    }
    
    // Main pages
    if (pathname === "/" || pathname === "/dashboard") return "Dashboard"
    if (pathname.startsWith("/skillpath")) return "Skillpath"
    if (pathname.startsWith("/skillsmaps")) return "SkillsMaps"
    if (pathname.startsWith("/studyroom") || pathname.startsWith("/study")) {
        if (pathname.includes("/quiz")) return "Taking Quiz"
        if (pathname.includes("/flashcards")) return "Reviewing Flashcards"
        if (pathname.includes("/tenta-simulator")) return "Tenta Simulator"
        if (pathname.includes("/omtenta")) return "Omtenta Practice"
        return "Studyroom"
    }
    if (pathname.startsWith("/ai-quiz")) return "AI Quiz"
    if (pathname.startsWith("/camp-devops")) return "Camp DevOps"
    if (pathname.startsWith("/fasttrack")) return "FastTrack"
    if (pathname.startsWith("/tutorials")) return "Tutorials"
    if (pathname.startsWith("/community")) return "Community"
    if (pathname.startsWith("/code-playground")) return "Code Playground"
    if (pathname.startsWith("/profile")) return "Profile"
    if (pathname.startsWith("/settings")) return "Settings"
    if (pathname.startsWith("/leaderboard")) return "Leaderboard"
    
    // Extract module name from study paths
    const moduleMatch = pathname.match(/\/study\/([^\/]+)/)
    if (moduleMatch) {
        return `Studying: ${moduleMatch[1].replace(/-/g, " ")}`
    }
    
    return pathname
}

// Determine action based on pathname
function getAction(pathname: string): string {
    if (!pathname) return "browsing"
    
    if (pathname.includes("/quiz")) return "taking_quiz"
    if (pathname.includes("/flashcards")) return "reviewing_flashcards"
    if (pathname.includes("/tenta")) return "exam_practice"
    if (pathname.includes("/ai-quiz")) return "ai_quiz"
    if (pathname.startsWith("/study/")) return "studying"
    if (pathname.startsWith("/admin")) return "admin"
    if (pathname.startsWith("/community")) return "community"
    if (pathname === "/" || pathname === "/dashboard") return "dashboard"
    
    return "browsing"
}

export function useActivityTracker() {
    const pathname = usePathname()
    const { user } = useAuth()
    const lastSentRef = useRef<string>("")
    const intervalRef = useRef<NodeJS.Timeout | null>(null)
    const sendingRef = useRef(false)

    const sendActivity = useCallback(async (currentPath: string, force: boolean = false) => {
        if (!user) return
        if (sendingRef.current) return // Prevent concurrent requests
        
        // Don't send if same as last sent (unless force heartbeat)
        const activityKey = `${currentPath}`
        if (!force && activityKey === lastSentRef.current) return
        
        sendingRef.current = true
        
        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/users/activity`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    current_page: getPageName(currentPath),
                    current_action: getAction(currentPath),
                    pathname: currentPath
                })
            })
            
            // Only update lastSent if successful
            if (response.ok) {
                lastSentRef.current = activityKey
            }
        } catch {
            // Silent fail - don't interrupt user experience
        } finally {
            sendingRef.current = false
        }
    }, [user])

    // Send activity on page change
    useEffect(() => {
        if (!pathname || !user) return
        
        // Send immediately on page change
        sendActivity(pathname)
        
        // Also send heartbeat every 30 seconds to keep "online" status
        intervalRef.current = setInterval(() => {
            sendActivity(pathname, true) // Force send for heartbeat
        }, 10000)
        
        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current)
            }
        }
    }, [pathname, user, sendActivity])

    return { pathname, pageName: getPageName(pathname || "") }
}

export default useActivityTracker
