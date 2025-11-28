"use client"

/**
 * DashboardHero Component
 * Phase D.2: Apple-Inspired Hero Header
 *
 * Features:
 * - Time-aware greeting
 * - Motivational subtext based on streak/progress
 * - Glassmorphism background
 * - Subtle gradient accent
 */

import * as React from "react"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface DashboardHeroProps {
    userName?: string | null
    streak?: number
    level?: number
    modulesCompleted?: number
    totalModules?: number
    className?: string
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function getTimeOfDay(): "morning" | "afternoon" | "evening" | "night" {
    const hour = new Date().getHours()
    if (hour >= 5 && hour < 12) return "morning"
    if (hour >= 12 && hour < 17) return "afternoon"
    if (hour >= 17 && hour < 21) return "evening"
    return "night"
}

function getGreeting(timeOfDay: string): string {
    const greetings = {
        morning: "Good morning",
        afternoon: "Good afternoon",
        evening: "Good evening",
        night: "Good night",
    }
    return greetings[timeOfDay as keyof typeof greetings] || "Welcome"
}

function getTimeEmoji(timeOfDay: string): string {
    const emojis = {
        morning: "☀️",
        afternoon: "🌤️",
        evening: "🌅",
        night: "🌙",
    }
    return emojis[timeOfDay as keyof typeof emojis] || "👋"
}

function getMotivationalText(
    streak: number,
    modulesCompleted: number,
    totalModules: number
): string {
    // Streak-based messages
    if (streak >= 30) {
        return "Incredible! 30+ day streak! You're unstoppable! 🔥"
    }
    if (streak >= 14) {
        return "Two weeks strong! Keep that momentum going! 💪"
    }
    if (streak >= 7) {
        return "One week streak! You're building great habits! ⚡"
    }
    if (streak >= 3) {
        return "Nice streak! Keep showing up every day! 🎯"
    }

    // Progress-based messages
    const progressPercent = totalModules > 0
        ? Math.round((modulesCompleted / totalModules) * 100)
        : 0

    if (progressPercent >= 90) {
        return "Almost there! The finish line is in sight! 🏆"
    }
    if (progressPercent >= 75) {
        return "You've come so far! Keep pushing! 🚀"
    }
    if (progressPercent >= 50) {
        return "Halfway through! You're doing amazing! 💫"
    }
    if (progressPercent >= 25) {
        return "Great progress! Every step counts! 🌟"
    }
    if (modulesCompleted > 0) {
        return "You've started your journey! Keep going! 🎉"
    }

    // Default for new users
    return "Ready to start your DevOps journey? Let's go! 🚀"
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function DashboardHero({
    userName,
    streak = 0,
    level = 1,
    modulesCompleted = 0,
    totalModules = 10,
    className,
}: DashboardHeroProps) {
    const timeOfDay = getTimeOfDay()
    const greeting = getGreeting(timeOfDay)
    const emoji = getTimeEmoji(timeOfDay)
    const displayName = userName || "Learner"
    const motivationalText = getMotivationalText(streak, modulesCompleted, totalModules)

    return (
        <div className={cn("relative", className)}>
            {/* Hero card with gradient background */}
            <div className="bg-gradient-to-r from-indigo-500 via-purple-500 to-purple-600 rounded-2xl p-8 text-white shadow-lg overflow-hidden relative">
                {/* Background decorative elements */}
                <div
                    className="absolute -top-24 -right-24 w-64 h-64 rounded-full bg-white/10 blur-3xl"
                    aria-hidden="true"
                />
                <div
                    className="absolute -bottom-16 -left-16 w-48 h-48 rounded-full bg-white/5 blur-2xl"
                    aria-hidden="true"
                />

                <div className="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                    {/* Greeting Section */}
                    <div className="space-y-2">
                        <div className="flex items-center gap-3">
                            <span className="text-3xl" aria-hidden="true">{emoji}</span>
                            <h1 className="text-2xl md:text-3xl font-bold tracking-tight">
                                {greeting}, {displayName}!
                            </h1>
                        </div>
                        <p className="text-indigo-100 text-base md:text-lg max-w-xl">
                            {motivationalText}
                        </p>
                    </div>

                    {/* Quick Stats Mini Display */}
                    <div className="flex items-center gap-4">
                        {/* Streak Badge */}
                        {streak > 0 && (
                            <div className="flex items-center gap-2 px-4 py-2 rounded-full bg-white/20 backdrop-blur-sm border border-white/30">
                                <span className="text-xl">🔥</span>
                                <span className="font-bold">{streak}</span>
                                <span className="text-sm text-white/80">day streak</span>
                            </div>
                        )}

                        {/* Level Badge */}
                        <div className="flex items-center gap-2 px-4 py-2 rounded-full bg-white/20 backdrop-blur-sm border border-white/30">
                            <span className="text-xl">⭐</span>
                            <span className="font-bold">Level {level}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
