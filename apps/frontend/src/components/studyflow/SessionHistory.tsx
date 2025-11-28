"use client"

/**
 * ============================================================================
 * SESSION HISTORY COMPONENT - Recent Sessions List
 * ============================================================================
 *
 * Features:
 * - Recent sessions list
 * - Date/time
 * - Duration
 * - Tasks completed
 * - XP earned
 *
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { Clock, Target, Zap, Calendar } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface SessionRecord {
    id: string
    date: Date
    durationMinutes: number
    tasksCompleted: number
    xpEarned: number
    mode: "pomodoro" | "deep-focus" | "custom"
}

export interface SessionHistoryProps {
    sessions: SessionRecord[]
    maxDisplay?: number
    className?: string
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function formatDate(date: Date): string {
    const now = new Date()
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
    const yesterday = new Date(today.getTime() - 86400000)
    const sessionDate = new Date(date.getFullYear(), date.getMonth(), date.getDate())

    if (sessionDate.getTime() === today.getTime()) {
        return "Today"
    }
    if (sessionDate.getTime() === yesterday.getTime()) {
        return "Yesterday"
    }
    return date.toLocaleDateString("en-US", { month: "short", day: "numeric" })
}

function formatTime(date: Date): string {
    return date.toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit" })
}

function getModeLabel(mode: string): string {
    switch (mode) {
        case "pomodoro":
            return "Pomodoro"
        case "deep-focus":
            return "Deep Focus"
        default:
            return "Custom"
    }
}

function getModeColor(mode: string): string {
    switch (mode) {
        case "pomodoro":
            return "bg-indigo-100 text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-400"
        case "deep-focus":
            return "bg-cyan-100 text-cyan-700 dark:bg-cyan-900/30 dark:text-cyan-400"
        default:
            return "bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400"
    }
}

/* ============================================================================
   SESSION ITEM
   ============================================================================ */

interface SessionItemProps {
    session: SessionRecord
}

function SessionItem({ session }: SessionItemProps) {
    return (
        <div className="flex items-center gap-4 py-3 border-b border-gray-100 dark:border-gray-700 last:border-0">
            {/* Date/Time */}
            <div className="w-20 flex-shrink-0">
                <p className="text-sm font-medium text-gray-900 dark:text-white">
                    {formatDate(session.date)}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                    {formatTime(session.date)}
                </p>
            </div>

            {/* Mode Badge */}
            <span className={cn(
                "px-2 py-0.5 rounded-full text-xs font-medium flex-shrink-0",
                getModeColor(session.mode)
            )}>
                {getModeLabel(session.mode)}
            </span>

            {/* Stats */}
            <div className="flex-1 flex items-center gap-4 justify-end">
                {/* Duration */}
                <div className="flex items-center gap-1 text-gray-600 dark:text-gray-400">
                    <Clock className="h-3.5 w-3.5" />
                    <span className="text-sm">{session.durationMinutes}m</span>
                </div>

                {/* Tasks */}
                <div className="flex items-center gap-1 text-gray-600 dark:text-gray-400">
                    <Target className="h-3.5 w-3.5" />
                    <span className="text-sm">{session.tasksCompleted}</span>
                </div>

                {/* XP */}
                <div className="flex items-center gap-1 text-amber-600 dark:text-amber-400 font-medium">
                    <Zap className="h-3.5 w-3.5" />
                    <span className="text-sm">+{session.xpEarned}</span>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState() {
    return (
        <div className="text-center py-8">
            <div className="mx-auto w-12 h-12 rounded-full bg-gray-100 dark:bg-gray-700 flex items-center justify-center mb-3">
                <Calendar className="h-6 w-6 text-gray-400" />
            </div>
            <p className="text-gray-600 dark:text-gray-400 font-medium">
                No sessions yet
            </p>
            <p className="text-sm text-gray-500 dark:text-gray-500 mt-1">
                Start your first study session!
            </p>
        </div>
    )
}

/* ============================================================================
   STATS SUMMARY
   ============================================================================ */

interface StatsSummaryProps {
    sessions: SessionRecord[]
}

function StatsSummary({ sessions }: StatsSummaryProps) {
    const totalMinutes = sessions.reduce((sum, s) => sum + s.durationMinutes, 0)
    const totalTasks = sessions.reduce((sum, s) => sum + s.tasksCompleted, 0)
    const totalXP = sessions.reduce((sum, s) => sum + s.xpEarned, 0)

    return (
        <div className="grid grid-cols-3 gap-4 mb-4 pb-4 border-b border-gray-200 dark:border-gray-700">
            <div className="text-center">
                <p className="text-2xl font-bold text-gray-900 dark:text-white">
                    {Math.round(totalMinutes / 60)}h
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                    Total Time
                </p>
            </div>
            <div className="text-center">
                <p className="text-2xl font-bold text-gray-900 dark:text-white">
                    {totalTasks}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                    Tasks Done
                </p>
            </div>
            <div className="text-center">
                <p className="text-2xl font-bold text-amber-600 dark:text-amber-400">
                    {totalXP}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                    XP Earned
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN SESSION HISTORY COMPONENT
   ============================================================================ */

export function SessionHistory({
    sessions,
    maxDisplay = 10,
    className,
}: SessionHistoryProps) {
    const displaySessions = sessions.slice(0, maxDisplay)

    return (
        <div className={cn("bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6", className)}>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
                <Calendar className="h-5 w-5 text-indigo-500" />
                Recent Sessions
            </h3>

            {sessions.length === 0 ? (
                <EmptyState />
            ) : (
                <>
                    <StatsSummary sessions={sessions} />
                    <div className="space-y-0">
                        {displaySessions.map(session => (
                            <SessionItem key={session.id} session={session} />
                        ))}
                    </div>

                    {sessions.length > maxDisplay && (
                        <button className="w-full mt-4 text-sm text-indigo-600 dark:text-indigo-400 hover:underline">
                            View all {sessions.length} sessions
                        </button>
                    )}
                </>
            )}
        </div>
    )
}

export default SessionHistory
