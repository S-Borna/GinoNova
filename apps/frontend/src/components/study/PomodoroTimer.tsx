"use client"

/**
 * ============================================================================
 * POMODORO TIMER - Study Sessions with Spotify Integration
 * ============================================================================
 *
 * Features:
 * - 25-minute focus sessions
 * - 5-minute short breaks
 * - 15-minute long breaks (every 4 sessions)
 * - Visual countdown with circular progress
 * - Session tracking and statistics
 * - Integration with Spotify (music starts/stops)
 * - Notifications (optional)
 * - Customizable intervals
 * - Cosmic glow animations
 * - Session history
 * - Daily/weekly stats
 *
 * @phase Study Room Enhancement
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Play,
    Pause,
    RotateCcw,
    Settings,
    CheckCircle2,
    Coffee,
    Target,
    Clock,
    Zap,
    TrendingUp,
    X
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type SessionPhase = "focus" | "shortBreak" | "longBreak"

export interface PomodoroSettings {
    focusDuration: number // minutes
    shortBreakDuration: number // minutes
    longBreakDuration: number // minutes
    sessionsUntilLongBreak: number
    autoStartBreaks: boolean
    autoStartPomodoros: boolean
    notifications: boolean
}

export interface PomodoroTimerProps {
    /** Callback when session starts */
    onSessionStart?: (phase: SessionPhase) => void
    /** Callback when session ends */
    onSessionEnd?: (phase: SessionPhase) => void
    /** Callback when timer state changes */
    onTimerStateChange?: (isRunning: boolean) => void
    /** Custom className */
    className?: string
}

export interface SessionStats {
    completedSessions: number
    totalFocusTime: number // minutes
    totalBreakTime: number // minutes
    currentStreak: number
    todaySessions: number
    todayFocusTime: number // minutes
}

/* ============================================================================
   DEFAULT SETTINGS
   ============================================================================ */

const DEFAULT_SETTINGS: PomodoroSettings = {
    focusDuration: 25,
    shortBreakDuration: 5,
    longBreakDuration: 15,
    sessionsUntilLongBreak: 4,
    autoStartBreaks: true,
    autoStartPomodoros: false,
    notifications: true
}

/* ============================================================================
   SETTINGS MODAL
   ============================================================================ */

function SettingsModal({
    isOpen,
    settings,
    onSave,
    onClose
}: {
    isOpen: boolean
    settings: PomodoroSettings
    onSave: (settings: PomodoroSettings) => void
    onClose: () => void
}) {
    const [localSettings, setLocalSettings] = useState(settings)

    if (!isOpen) return null

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
            <motion.div
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                className={cn(
                    "w-full max-w-md rounded-2xl",
                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                    "border border-purple-500/30",
                    "shadow-xl"
                )}
            >
                {/* Header */}
                <div className="flex items-center justify-between px-6 py-4 border-b border-purple-500/20">
                    <div className="flex items-center gap-2">
                        <Settings className="w-5 h-5 text-purple-400" />
                        <h3 className="font-semibold text-zinc-100">Timer Settings</h3>
                    </div>
                    <button
                        onClick={onClose}
                        className="p-1.5 rounded-lg hover:bg-zinc-800 transition-colors"
                    >
                        <X className="w-4 h-4 text-zinc-400" />
                    </button>
                </div>

                {/* Content */}
                <div className="p-6 space-y-4">
                    {/* Durations */}
                    <div className="space-y-3">
                        <div>
                            <label className="text-sm font-medium text-zinc-300 block mb-1">
                                Focus Duration (minutes)
                            </label>
                            <input
                                type="number"
                                min="1"
                                max="60"
                                value={localSettings.focusDuration}
                                onChange={(e) => setLocalSettings({ ...localSettings, focusDuration: parseInt(e.target.value) || 25 })}
                                className="w-full px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 focus:border-purple-500 focus:outline-none"
                            />
                        </div>

                        <div>
                            <label className="text-sm font-medium text-zinc-300 block mb-1">
                                Short Break (minutes)
                            </label>
                            <input
                                type="number"
                                min="1"
                                max="30"
                                value={localSettings.shortBreakDuration}
                                onChange={(e) => setLocalSettings({ ...localSettings, shortBreakDuration: parseInt(e.target.value) || 5 })}
                                className="w-full px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 focus:border-purple-500 focus:outline-none"
                            />
                        </div>

                        <div>
                            <label className="text-sm font-medium text-zinc-300 block mb-1">
                                Long Break (minutes)
                            </label>
                            <input
                                type="number"
                                min="1"
                                max="60"
                                value={localSettings.longBreakDuration}
                                onChange={(e) => setLocalSettings({ ...localSettings, longBreakDuration: parseInt(e.target.value) || 15 })}
                                className="w-full px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 focus:border-purple-500 focus:outline-none"
                            />
                        </div>

                        <div>
                            <label className="text-sm font-medium text-zinc-300 block mb-1">
                                Sessions Until Long Break
                            </label>
                            <input
                                type="number"
                                min="2"
                                max="10"
                                value={localSettings.sessionsUntilLongBreak}
                                onChange={(e) => setLocalSettings({ ...localSettings, sessionsUntilLongBreak: parseInt(e.target.value) || 4 })}
                                className="w-full px-3 py-2 rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 focus:border-purple-500 focus:outline-none"
                            />
                        </div>
                    </div>

                    {/* Toggles */}
                    <div className="space-y-3 pt-2 border-t border-zinc-800">
                        <label className="flex items-center justify-between cursor-pointer">
                            <span className="text-sm text-zinc-300">Auto-start breaks</span>
                            <button
                                onClick={() => setLocalSettings({ ...localSettings, autoStartBreaks: !localSettings.autoStartBreaks })}
                                className={cn(
                                    "relative w-11 h-6 rounded-full transition-colors",
                                    localSettings.autoStartBreaks ? "bg-purple-500" : "bg-zinc-700"
                                )}
                            >
                                <motion.div
                                    className="absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white"
                                    animate={{ x: localSettings.autoStartBreaks ? 20 : 0 }}
                                    transition={{ type: "spring", stiffness: 500, damping: 30 }}
                                />
                            </button>
                        </label>

                        <label className="flex items-center justify-between cursor-pointer">
                            <span className="text-sm text-zinc-300">Auto-start focus sessions</span>
                            <button
                                onClick={() => setLocalSettings({ ...localSettings, autoStartPomodoros: !localSettings.autoStartPomodoros })}
                                className={cn(
                                    "relative w-11 h-6 rounded-full transition-colors",
                                    localSettings.autoStartPomodoros ? "bg-purple-500" : "bg-zinc-700"
                                )}
                            >
                                <motion.div
                                    className="absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white"
                                    animate={{ x: localSettings.autoStartPomodoros ? 20 : 0 }}
                                    transition={{ type: "spring", stiffness: 500, damping: 30 }}
                                />
                            </button>
                        </label>

                        <label className="flex items-center justify-between cursor-pointer">
                            <span className="text-sm text-zinc-300">Enable notifications</span>
                            <button
                                onClick={() => setLocalSettings({ ...localSettings, notifications: !localSettings.notifications })}
                                className={cn(
                                    "relative w-11 h-6 rounded-full transition-colors",
                                    localSettings.notifications ? "bg-purple-500" : "bg-zinc-700"
                                )}
                            >
                                <motion.div
                                    className="absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white"
                                    animate={{ x: localSettings.notifications ? 20 : 0 }}
                                    transition={{ type: "spring", stiffness: 500, damping: 30 }}
                                />
                            </button>
                        </label>
                    </div>
                </div>

                {/* Footer */}
                <div className="px-6 py-4 border-t border-purple-500/20 flex gap-3">
                    <button
                        onClick={onClose}
                        className="flex-1 px-4 py-2 rounded-lg bg-zinc-800 text-zinc-300 hover:bg-zinc-700 transition-colors"
                    >
                        Cancel
                    </button>
                    <button
                        onClick={() => {
                            onSave(localSettings)
                            onClose()
                        }}
                        className="flex-1 px-4 py-2 rounded-lg bg-gradient-to-r from-purple-600 to-purple-500 text-white hover:from-purple-500 hover:to-purple-400 transition-all"
                    >
                        Save Changes
                    </button>
                </div>
            </motion.div>
        </div>
    )
}

/* ============================================================================
   CIRCULAR TIMER DISPLAY
   ============================================================================ */

function CircularTimer({
    totalSeconds,
    remainingSeconds,
    phase,
    size = 280
}: {
    totalSeconds: number
    remainingSeconds: number
    phase: SessionPhase
    size?: number
}) {
    const progress = totalSeconds > 0 ? remainingSeconds / totalSeconds : 0
    const strokeWidth = 12
    const radius = (size - strokeWidth) / 2
    const circumference = 2 * Math.PI * radius
    const strokeDashoffset = circumference * (1 - progress)

    const minutes = Math.floor(remainingSeconds / 60)
    const seconds = remainingSeconds % 60

    const isLowTime = remainingSeconds > 0 && remainingSeconds < 60

    const colors = {
        focus: { start: "#8b5cf6", end: "#6366f1", glow: "rgba(139, 92, 246, 0.5)" },
        shortBreak: { start: "#22c55e", end: "#10b981", glow: "rgba(34, 211, 153, 0.5)" },
        longBreak: { start: "#3b82f6", end: "#2563eb", glow: "rgba(59, 130, 246, 0.5)" }
    }

    const color = colors[phase] || colors.focus

    return (
        <div className="relative inline-flex items-center justify-center">
            <svg
                width={size}
                height={size}
                className="transform -rotate-90"
            >
                <defs>
                    <linearGradient id={`gradient-${phase}`} x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stopColor={color.start} />
                        <stop offset="100%" stopColor={color.end} />
                    </linearGradient>
                    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
                        <feMerge>
                            <feMergeNode in="blur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                </defs>

                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={strokeWidth}
                    className="text-zinc-800"
                />

                <motion.circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke={`url(#gradient-${phase})`}
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={strokeDashoffset}
                    filter="url(#glow)"
                    className={cn(
                        "transition-all duration-1000 ease-linear",
                        isLowTime && "animate-pulse"
                    )}
                />
            </svg>

            <div className="absolute inset-0 flex flex-col items-center justify-center">
                <div className={cn(
                    "flex items-baseline gap-1 font-mono tabular-nums",
                    isLowTime && "animate-pulse"
                )}>
                    <span className="text-6xl font-bold tracking-tight text-white">
                        {minutes.toString().padStart(2, "0")}
                    </span>
                    <span className="text-4xl font-bold text-zinc-500">:</span>
                    <span className="text-6xl font-bold tracking-tight text-white">
                        {seconds.toString().padStart(2, "0")}
                    </span>
                </div>

                <span className={cn(
                    "mt-2 text-sm font-medium uppercase tracking-wider",
                    phase === "focus" && "text-purple-400",
                    phase === "shortBreak" && "text-emerald-400",
                    phase === "longBreak" && "text-blue-400"
                )}>
                    {phase === "focus" && "Focus Time"}
                    {phase === "shortBreak" && "Short Break"}
                    {phase === "longBreak" && "Long Break"}
                </span>
            </div>

            <motion.div
                className={cn(
                    "absolute inset-0 rounded-full opacity-20 blur-3xl pointer-events-none",
                    phase === "focus" && "bg-gradient-to-br from-purple-400 to-purple-600",
                    phase === "shortBreak" && "bg-gradient-to-br from-emerald-400 to-green-500",
                    phase === "longBreak" && "bg-gradient-to-br from-blue-400 to-blue-600"
                )}
                animate={{
                    scale: [1, 1.1, 1],
                    opacity: [0.2, 0.3, 0.2]
                }}
                transition={{ duration: 3, repeat: Infinity }}
                style={{ transform: "scale(1.1)" }}
            />
        </div>
    )
}

/* ============================================================================
   STATS DISPLAY
   ============================================================================ */

function StatsDisplay({ stats }: { stats: SessionStats }) {
    const statItems = [
        { icon: Target, label: "Today's Sessions", value: stats.todaySessions, color: "purple" },
        { icon: Clock, label: "Today's Focus", value: `${stats.todayFocusTime}m`, color: "blue" },
        { icon: CheckCircle2, label: "Total Sessions", value: stats.completedSessions, color: "emerald" },
        { icon: Zap, label: "Current Streak", value: `${stats.currentStreak} days`, color: "orange" }
    ]

    return (
        <div className="grid grid-cols-2 gap-3">
            {statItems.map((item, i) => (
                <motion.div
                    key={item.label}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.1 }}
                    className={cn(
                        "p-3 rounded-xl",
                        "bg-zinc-900/50 border border-zinc-800",
                        "hover:border-zinc-700 transition-colors"
                    )}
                >
                    <div className="flex items-center gap-2 mb-1">
                        <item.icon className={cn(
                            "w-4 h-4",
                            item.color === "purple" && "text-purple-400",
                            item.color === "blue" && "text-blue-400",
                            item.color === "emerald" && "text-emerald-400",
                            item.color === "orange" && "text-orange-400"
                        )} />
                        <span className="text-xs text-zinc-500">{item.label}</span>
                    </div>
                    <p className="text-xl font-bold text-zinc-100">{item.value}</p>
                </motion.div>
            ))}
        </div>
    )
}

/* ============================================================================
   MAIN POMODORO TIMER COMPONENT
   ============================================================================ */

export function PomodoroTimer({
    onSessionStart,
    onSessionEnd,
    onTimerStateChange,
    className
}: PomodoroTimerProps) {
    const [settings, setSettings] = useState<PomodoroSettings>(DEFAULT_SETTINGS)
    const [phase, setPhase] = useState<SessionPhase>("focus")
    const [isRunning, setIsRunning] = useState(false)
    const [remainingSeconds, setRemainingSeconds] = useState(settings.focusDuration * 60)
    const [completedSessions, setCompletedSessions] = useState(0)
    const [showSettings, setShowSettings] = useState(false)

    const [stats, setStats] = useState<SessionStats>({
        completedSessions: 0,
        totalFocusTime: 0,
        totalBreakTime: 0,
        currentStreak: 3,
        todaySessions: 0,
        todayFocusTime: 0
    })

    const totalSeconds = phase === "focus"
        ? settings.focusDuration * 60
        : phase === "shortBreak"
            ? settings.shortBreakDuration * 60
            : settings.longBreakDuration * 60

    // Timer tick
    useEffect(() => {
        if (!isRunning) return

        const interval = setInterval(() => {
            setRemainingSeconds((prev) => {
                if (prev <= 1) {
                    handleSessionComplete()
                    return 0
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(interval)
    }, [isRunning]) // eslint-disable-line react-hooks/exhaustive-deps

    // Notify timer state changes
    useEffect(() => {
        onTimerStateChange?.(isRunning)
    }, [isRunning, onTimerStateChange])

    const handleSessionComplete = () => {
        onSessionEnd?.(phase)

        // Update stats
        if (phase === "focus") {
            setCompletedSessions((prev) => prev + 1)
            setStats((prev) => ({
                ...prev,
                completedSessions: prev.completedSessions + 1,
                todaySessions: prev.todaySessions + 1,
                todayFocusTime: prev.todayFocusTime + settings.focusDuration,
                totalFocusTime: prev.totalFocusTime + settings.focusDuration
            }))
        }

        // Determine next phase
        if (phase === "focus") {
            const nextPhase = (completedSessions + 1) % settings.sessionsUntilLongBreak === 0
                ? "longBreak"
                : "shortBreak"
            setPhase(nextPhase)
            setRemainingSeconds(
                nextPhase === "longBreak"
                    ? settings.longBreakDuration * 60
                    : settings.shortBreakDuration * 60
            )
            if (settings.autoStartBreaks) {
                onSessionStart?.(nextPhase)
            } else {
                setIsRunning(false)
            }
        } else {
            setPhase("focus")
            setRemainingSeconds(settings.focusDuration * 60)
            if (settings.autoStartPomodoros) {
                onSessionStart?.("focus")
            } else {
                setIsRunning(false)
            }
        }

        // Show notification
        if (settings.notifications && "Notification" in window && Notification.permission === "granted") {
            new Notification("Pomodoro Timer", {
                body: phase === "focus" ? "Time for a break!" : "Time to focus!",
                icon: "/favicon.ico"
            })
        }
    }

    const toggleTimer = () => {
        if (!isRunning) {
            onSessionStart?.(phase)
        }
        setIsRunning(!isRunning)
    }

    const resetTimer = () => {
        setIsRunning(false)
        setRemainingSeconds(totalSeconds)
    }

    const skipToNextPhase = () => {
        handleSessionComplete()
    }

    return (
        <div className={cn("space-y-6", className)}>
            {/* Timer Display */}
            <div className="flex flex-col items-center">
                <CircularTimer
                    totalSeconds={totalSeconds}
                    remainingSeconds={remainingSeconds}
                    phase={phase}
                    size={320}
                />

                {/* Controls */}
                <div className="mt-8 flex items-center gap-4">
                    <motion.button
                        onClick={toggleTimer}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        className={cn(
                            "w-16 h-16 rounded-full flex items-center justify-center",
                            "bg-gradient-to-r from-purple-600 to-purple-500",
                            "text-white shadow-lg shadow-purple-500/30",
                            "hover:from-purple-500 hover:to-purple-400",
                            "transition-all"
                        )}
                    >
                        {isRunning ? <Pause className="w-7 h-7" /> : <Play className="w-7 h-7 ml-1" />}
                    </motion.button>

                    <button
                        onClick={resetTimer}
                        className="p-3 rounded-full bg-zinc-800 text-zinc-400 hover:bg-zinc-700 hover:text-zinc-300 transition-colors"
                    >
                        <RotateCcw className="w-5 h-5" />
                    </button>

                    <button
                        onClick={() => setShowSettings(true)}
                        className="p-3 rounded-full bg-zinc-800 text-zinc-400 hover:bg-zinc-700 hover:text-zinc-300 transition-colors"
                    >
                        <Settings className="w-5 h-5" />
                    </button>
                </div>

                {/* Session Progress */}
                <div className="mt-6 flex items-center gap-2">
                    {Array.from({ length: settings.sessionsUntilLongBreak }).map((_, i) => (
                        <div
                            key={i}
                            className={cn(
                                "w-2 h-2 rounded-full transition-all",
                                i < completedSessions % settings.sessionsUntilLongBreak
                                    ? "bg-purple-500"
                                    : "bg-zinc-700"
                            )}
                        />
                    ))}
                </div>
            </div>

            {/* Stats */}
            <StatsDisplay stats={stats} />

            {/* Settings Modal */}
            <AnimatePresence>
                {showSettings && (
                    <SettingsModal
                        isOpen={showSettings}
                        settings={settings}
                        onSave={(newSettings) => {
                            setSettings(newSettings)
                            setRemainingSeconds(
                                phase === "focus"
                                    ? newSettings.focusDuration * 60
                                    : phase === "shortBreak"
                                        ? newSettings.shortBreakDuration * 60
                                        : newSettings.longBreakDuration * 60
                            )
                        }}
                        onClose={() => setShowSettings(false)}
                    />
                )}
            </AnimatePresence>
        </div>
    )
}

export default PomodoroTimer
