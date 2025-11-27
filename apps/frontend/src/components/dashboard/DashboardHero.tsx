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
import { GlassCard } from "@/components/ui/glass-card"
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
            {/* Background gradient overlay */}
            <div
                className="absolute inset-0 rounded-2xl bg-gradient-to-br from-primary-500/20 via-primary-600/10 to-transparent opacity-50"
                aria-hidden="true"
            />

            <GlassCard
                variant="default"
                padding="lg"
                radius="lg"
                className="relative overflow-hidden"
            >
                {/* Subtle gradient accent on top */}
                <div
                    className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-primary-500 via-primary-400 to-accent-info"
                    aria-hidden="true"
                />

                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                    {/* Greeting Section */}
                    <div className="space-y-2">
                        <div className="flex items-center gap-3">
                            <span className="text-3xl" aria-hidden="true">{emoji}</span>
                            <h1 className="text-2xl md:text-3xl font-bold text-neutral-900 dark:text-white tracking-tight">
                                {greeting}, {displayName}!
                            </h1>
                        </div>
                        <p className="text-neutral-600 dark:text-neutral-300 text-base md:text-lg max-w-xl">
                            {motivationalText}
                        </p>
                    </div>

                    {/* Quick Stats Mini Display */}
                    <div className="flex items-center gap-6">
                        {/* Streak Badge */}
                        {streak > 0 && (
                            <div className="flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-accent-warning/20 to-accent-xp/20 border border-accent-warning/30">
                                <span className="text-xl">🔥</span>
                                <span className="font-bold text-neutral-900 dark:text-white">{streak}</span>
                                <span className="text-sm text-neutral-600 dark:text-neutral-400">day streak</span>
                            </div>
                        )}

                        {/* Level Badge */}
                        <div className="flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-primary-500/20 to-primary-600/20 border border-primary-300/30">
                            <span className="text-xl">⭐</span>
                            <span className="font-bold text-neutral-900 dark:text-white">Level {level}</span>
                        </div>
                    </div>
                </div>

                {/* Decorative elements */}
                <div
                    className="absolute -bottom-20 -right-20 w-64 h-64 rounded-full bg-gradient-to-br from-primary-400/10 to-transparent blur-3xl"
                    aria-hidden="true"
                />
            </GlassCard>
        </div>
    )
}
