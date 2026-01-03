"use client"

/**
 * ============================================================================
 * EXAM MODE DASHBOARD — Overview för Tentaplugg
 * ============================================================================
 * 
 * Visar:
 * - Countdown till tentadatum
 * - Confidence scores per task
 * - Weak areas
 * - Study plan
 * - Progress tracking
 */

import { useState } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { useExamMode, StudySession } from "@/contexts/ExamModeContext"
import { DOE25_MODULE, DOE25Task } from "@/data/doe25-module"
import {
    Calendar,
    Target,
    TrendingDown,
    TrendingUp,
    Clock,
    BookOpen,
    AlertTriangle,
    CheckCircle2,
    Zap,
    Flame,
    Play
} from "lucide-react"
import Link from "next/link"
import { MockExamSimulator } from "./MockExamSimulator"

/* ============================================================================
   COUNTDOWN CARD
   ============================================================================ */

function CountdownCard() {
    const { state } = useExamMode()
    const examDate = new Date(DOE25_MODULE.exam_date)
    const now = new Date()
    const diff = examDate.getTime() - now.getTime()
    const days = Math.ceil(diff / (1000 * 60 * 60 * 24))
    const hours = Math.ceil((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-amber-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-amber-500/30",
                "shadow-[0_0_40px_rgba(249,115,22,0.1)]",
                "p-6"
            )}
        >
            <div className="flex items-center gap-3 mb-4">
                <div className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center",
                    "bg-gradient-to-br from-amber-500 to-orange-600",
                    "shadow-[0_0_25px_rgba(249,115,22,0.5)]"
                )}>
                    <Calendar className="w-6 h-6 text-white" />
                </div>
                <div>
                    <h3 className="text-lg font-bold text-white">DOE25 Tenta</h3>
                    <p className="text-sm text-amber-300/60">
                        {examDate.toLocaleDateString("sv-SE", {
                            weekday: "long",
                            year: "numeric",
                            month: "long",
                            day: "numeric",
                            hour: "2-digit",
                            minute: "2-digit"
                        })}
                    </p>
                </div>
            </div>

            {days > 0 ? (
                <div className="space-y-2">
                    <div className="flex items-baseline gap-2">
                        <motion.span
                            className="text-4xl font-black text-amber-400"
                            animate={{ scale: [1, 1.05, 1] }}
                            transition={{ duration: 2, repeat: Infinity }}
                        >
                            {days}
                        </motion.span>
                        <span className="text-lg text-amber-300/60">dagar</span>
                        <span className="text-sm text-amber-300/40">{hours} timmar</span>
                    </div>
                    <p className="text-sm text-amber-300/60">
                        {days === 1 ? "Sista dagen! 🎯" : `${days} dagar kvar att plugga`}
                    </p>
                </div>
            ) : (
                <div className="text-center py-4">
                    <p className="text-2xl font-bold text-red-400">Tentan är idag! 🎓</p>
                    <p className="text-sm text-zinc-400 mt-2">Lycka till!</p>
                </div>
            )}
        </motion.div>
    )
}

/* ============================================================================
   CONFIDENCE OVERVIEW
   ============================================================================ */

function ConfidenceOverview() {
    const { state, getConfidenceForTask } = useExamMode()
    const allTasks = DOE25_MODULE.tasks

    // Group tasks by confidence level
    const highConfidence = allTasks.filter(t => getConfidenceForTask(t.id) >= 80)
    const mediumConfidence = allTasks.filter(t => {
        const conf = getConfidenceForTask(t.id)
        return conf >= 50 && conf < 80
    })
    const lowConfidence = allTasks.filter(t => getConfidenceForTask(t.id) < 50)

    const avgConfidence = allTasks.length > 0
        ? allTasks.reduce((sum, t) => sum + getConfidenceForTask(t.id), 0) / allTasks.length
        : 0

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border border-purple-500/20",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-6">
                <Target className="w-5 h-5 text-purple-400" />
                <h3 className="text-lg font-bold text-white">Confidence Overview</h3>
            </div>

            {/* Average Confidence */}
            <div className="mb-6">
                <div className="flex items-center justify-between mb-2">
                    <span className="text-sm text-zinc-400">Genomsnittlig Confidence</span>
                    <span className="text-lg font-bold text-purple-400">
                        {Math.round(avgConfidence)}%
                    </span>
                </div>
                <div className="h-3 rounded-full bg-zinc-800 overflow-hidden">
                    <motion.div
                        className="h-full bg-gradient-to-r from-purple-500 to-purple-600"
                        initial={{ width: 0 }}
                        animate={{ width: `${avgConfidence}%` }}
                        transition={{ duration: 1, ease: "easeOut" }}
                    />
                </div>
            </div>

            {/* Breakdown */}
            <div className="grid grid-cols-3 gap-4">
                <div className="text-center p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/30">
                    <div className="text-2xl font-bold text-emerald-400">{highConfidence.length}</div>
                    <div className="text-xs text-emerald-300/60 mt-1">Hög (80%+)</div>
                </div>
                <div className="text-center p-3 rounded-xl bg-amber-500/10 border border-amber-500/30">
                    <div className="text-2xl font-bold text-amber-400">{mediumConfidence.length}</div>
                    <div className="text-xs text-amber-300/60 mt-1">Medel (50-79%)</div>
                </div>
                <div className="text-center p-3 rounded-xl bg-red-500/10 border border-red-500/30">
                    <div className="text-2xl font-bold text-red-400">{lowConfidence.length}</div>
                    <div className="text-xs text-red-300/60 mt-1">Låg (&lt;50%)</div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   WEAK AREAS
   ============================================================================ */

function WeakAreasCard() {
    const { state, getConfidenceForTask } = useExamMode()
    const weakAreas = state.weakAreas.slice(0, 5)
    const allTasks = DOE25_MODULE.tasks

    if (weakAreas.length === 0) {
        return (
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className={cn(
                    "rounded-2xl overflow-hidden",
                    "bg-gradient-to-br from-emerald-900/20 via-[#0d0d14] to-[#0a0a0f]",
                    "border border-emerald-500/30",
                    "p-6 text-center"
                )}
            >
                <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
                <h3 className="text-lg font-bold text-white mb-2">Inga svaga områden! 🎉</h3>
                <p className="text-sm text-zinc-400">
                    Du har minst 70% confidence på alla tasks. Fortsätt så!
                </p>
            </motion.div>
        )
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-red-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-red-500/30",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-4">
                <AlertTriangle className="w-5 h-5 text-red-400" />
                <h3 className="text-lg font-bold text-white">Svaga Områden</h3>
                <span className="text-xs text-red-300/60">({weakAreas.length} tasks)</span>
            </div>

            <div className="space-y-3">
                {weakAreas.map((taskId, index) => {
                    const task = allTasks.find(t => t.id === taskId)
                    const confidence = getConfidenceForTask(taskId)
                    if (!task) return null

                    return (
                        <Link
                            key={taskId}
                            href={`/modules/doe25-tenta/tasks/${taskId}`}
                            className={cn(
                                "block p-3 rounded-xl",
                                "bg-zinc-900/50 border border-red-500/20",
                                "hover:border-red-400/40 hover:bg-zinc-800/50",
                                "transition-all duration-300"
                            )}
                        >
                            <div className="flex items-center justify-between">
                                <div className="flex-1 min-w-0">
                                    <p className="text-sm font-medium text-white truncate">
                                        {task.title}
                                    </p>
                                    <div className="flex items-center gap-2 mt-1">
                                        <div className="h-1.5 flex-1 rounded-full bg-zinc-800 overflow-hidden max-w-[100px]">
                                            <div
                                                className="h-full bg-gradient-to-r from-red-500 to-red-600"
                                                style={{ width: `${confidence}%` }}
                                            />
                                        </div>
                                        <span className="text-xs text-red-400 font-medium">
                                            {Math.round(confidence)}%
                                        </span>
                                    </div>
                                </div>
                                <TrendingDown className="w-4 h-4 text-red-400 ml-2 shrink-0" />
                            </div>
                        </Link>
                    )
                })}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   STUDY PLAN
   ============================================================================ */

function StudyPlanCard() {
    const { state } = useExamMode()
    const allTasks = DOE25_MODULE.tasks

    if (state.daysRemaining <= 0) {
        return null
    }

    const todayTasks = state.studyPlan.dailyTasks.slice(0, 3) // Show first 3 tasks for today

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-blue-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-blue-500/30",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-4">
                <BookOpen className="w-5 h-5 text-blue-400" />
                <h3 className="text-lg font-bold text-white">Dagens Studieplan</h3>
            </div>

            {todayTasks.length > 0 ? (
                <div className="space-y-2">
                    {todayTasks.map((taskId, index) => {
                        const task = allTasks.find(t => t.id === taskId)
                        if (!task) return null

                        return (
                            <Link
                                key={taskId}
                                href={`/modules/doe25-tenta/tasks/${taskId}`}
                                className={cn(
                                    "flex items-center gap-3 p-3 rounded-xl",
                                    "bg-zinc-900/50 border border-blue-500/20",
                                    "hover:border-blue-400/40 hover:bg-zinc-800/50",
                                    "transition-all duration-300"
                                )}
                            >
                                <div className={cn(
                                    "w-8 h-8 rounded-lg flex items-center justify-center shrink-0",
                                    "bg-blue-500/20 text-blue-400 border border-blue-500/30"
                                )}>
                                    {index + 1}
                                </div>
                                <div className="flex-1 min-w-0">
                                    <p className="text-sm font-medium text-white truncate">
                                        {task.title}
                                    </p>
                                    <p className="text-xs text-zinc-400">
                                        {task.estimated_minutes} min
                                    </p>
                                </div>
                                <Zap className="w-4 h-4 text-blue-400 shrink-0" />
                            </Link>
                        )
                    })}
                </div>
            ) : (
                <p className="text-sm text-zinc-400 text-center py-4">
                    Inga tasks planerade för idag. Alla tasks är klara! 🎉
                </p>
            )}
        </motion.div>
    )
}

/* ============================================================================
   STUDY STATS
   ============================================================================ */

function StudyStatsCard() {
    const { state } = useExamMode()
    const totalSessions = state.studySessions.length
    const totalMinutes = state.studySessions.reduce((sum, s) => sum + s.duration, 0)
    const totalHours = Math.round(totalMinutes / 60)
    const streak = calculateStreak(state.studySessions)

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-purple-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-purple-500/30",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-4">
                <Flame className="w-5 h-5 text-orange-400" />
                <h3 className="text-lg font-bold text-white">Study Stats</h3>
            </div>

            <div className="grid grid-cols-3 gap-4">
                <div className="text-center">
                    <div className="text-2xl font-bold text-orange-400">{streak}</div>
                    <div className="text-xs text-zinc-400 mt-1">Dagars Streak</div>
                </div>
                <div className="text-center">
                    <div className="text-2xl font-bold text-purple-400">{totalSessions}</div>
                    <div className="text-xs text-zinc-400 mt-1">Sessions</div>
                </div>
                <div className="text-center">
                    <div className="text-2xl font-bold text-blue-400">{totalHours}h</div>
                    <div className="text-xs text-zinc-400 mt-1">Totalt Studerat</div>
                </div>
            </div>
        </motion.div>
    )
}

function calculateStreak(sessions: StudySession[]): number {
    if (sessions.length === 0) return 0

    const sorted = [...sessions].sort((a, b) => b.date.getTime() - a.date.getTime())
    let streak = 0
    const today = new Date()
    today.setHours(0, 0, 0, 0)

    for (let i = 0; i < sorted.length; i++) {
        const sessionDate = new Date(sorted[i].date)
        sessionDate.setHours(0, 0, 0, 0)
        const diffDays = Math.floor((today.getTime() - sessionDate.getTime()) / (1000 * 60 * 60 * 24))

        if (diffDays === i) {
            streak++
        } else {
            break
        }
    }

    return streak
}

/* ============================================================================
   MOCK EXAM CARD
   ============================================================================ */

function MockExamCard() {
    const [showSimulator, setShowSimulator] = useState(false)

    if (showSimulator) {
        return <MockExamSimulator />
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-purple-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-purple-500/30",
                "p-6"
            )}
        >
            <div className="flex items-center gap-2 mb-4">
                <Play className="w-5 h-5 text-purple-400" />
                <h3 className="text-lg font-bold text-white">Mock Exam</h3>
            </div>
            <p className="text-sm text-zinc-400 mb-4">
                Simulera en riktig tenta med timer och inga hints. Perfekt för att testa din kunskap!
            </p>
            <button
                onClick={() => setShowSimulator(true)}
                className={cn(
                    "w-full px-4 py-3 rounded-xl",
                    "bg-gradient-to-r from-purple-600 to-purple-500",
                    "hover:from-purple-500 hover:to-purple-400",
                    "text-white font-medium",
                    "transition-all duration-300"
                )}
            >
                <Play className="w-4 h-4 mr-2 inline" />
                Starta Mock Exam
            </button>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function ExamModeDashboard() {
    return (
        <div className="space-y-6">
            {/* Countdown */}
            <CountdownCard />

            {/* Grid */}
            <div className="grid lg:grid-cols-2 gap-6">
                <ConfidenceOverview />
                <WeakAreasCard />
            </div>

            <div className="grid lg:grid-cols-2 gap-6">
                <StudyPlanCard />
                <StudyStatsCard />
            </div>

            {/* Mock Exam */}
            <MockExamCard />
        </div>
    )
}

