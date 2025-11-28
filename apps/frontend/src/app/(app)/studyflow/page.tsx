"use client"

/**
 * ============================================================================
 * STUDYFLOW PAGE — Focused Study Mode Experience
 * ============================================================================
 *
 * Features:
 * - Pre-session setup (mode, task, goals)
 * - Active session with timer and controls
 * - Session complete celebration
 * - Session history
 * - Calming, focused design
 *
 * @phase A.3 - App Shell & Routing
 * @design D.5 - Studyflow UI
 */

import * as React from "react"
import { useRouter, useSearchParams } from "next/navigation"
import {
    SessionSetup,
    ActiveSession,
    SessionComplete,
    SessionHistory,
    StreakDisplay,
    type SessionConfig,
    type SessionSummary,
    type SessionRecord,
} from "@/components/studyflow"

/* ============================================================================
   TYPES
   ============================================================================ */

type SessionState = "setup" | "active" | "complete"

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_SESSIONS: SessionRecord[] = [
    {
        id: "1",
        date: new Date(),
        durationMinutes: 25,
        tasksCompleted: 1,
        xpEarned: 75,
        mode: "pomodoro",
    },
    {
        id: "2",
        date: new Date(Date.now() - 86400000), // Yesterday
        durationMinutes: 50,
        tasksCompleted: 2,
        xpEarned: 150,
        mode: "deep-focus",
    },
    {
        id: "3",
        date: new Date(Date.now() - 86400000 * 2), // 2 days ago
        durationMinutes: 30,
        tasksCompleted: 1,
        xpEarned: 80,
        mode: "custom",
    },
]

const MOCK_TASKS = [
    {
        id: "1",
        title: "Install Docker",
        moduleId: "m9",
        moduleTitle: "Module 09 · Containers",
        isRecommended: true,
    },
    {
        id: "2",
        title: "Write Dockerfile",
        moduleId: "m9",
        moduleTitle: "Module 09 · Containers",
    },
    {
        id: "3",
        title: "Docker Compose Basics",
        moduleId: "m9",
        moduleTitle: "Module 09 · Containers",
    },
    {
        id: "4",
        title: "Linux File Permissions",
        moduleId: "m3",
        moduleTitle: "Module 03 · Linux Basics",
    },
]

/* ============================================================================
   STUDYFLOW PAGE
   ============================================================================ */

export default function StudyflowPage() {
    const router = useRouter()
    const searchParams = useSearchParams()

    // Check for module/task from URL params (from module detail page)
    const moduleSlug = searchParams.get("module")
    const taskId = searchParams.get("task")

    // Session state
    const [sessionState, setSessionState] = React.useState<SessionState>("setup")
    const [sessionConfig, setSessionConfig] = React.useState<SessionConfig | null>(null)
    const [sessionSummary, setSessionSummary] = React.useState<SessionSummary | null>(null)
    const [sessions, setSessions] = React.useState<SessionRecord[]>(MOCK_SESSIONS)
    const [tasksCompletedInSession, setTasksCompletedInSession] = React.useState(0)

    // Handle start session
    const handleStartSession = (config: SessionConfig) => {
        setSessionConfig(config)
        setTasksCompletedInSession(0)
        setSessionState("active")
    }

    // Handle end session
    const handleEndSession = () => {
        // Create summary
        const summary: SessionSummary = {
            totalFocusMinutes: sessionConfig?.workMinutes || 25,
            tasksCompleted: tasksCompletedInSession,
            xpEarned: tasksCompletedInSession * 50 + 25, // Base 25 XP + 50 per task
            streakDays: 7,
            isNewRecord: false,
        }
        setSessionSummary(summary)
        setSessionState("complete")

        // Add to history
        if (sessionConfig) {
            const newSession: SessionRecord = {
                id: Date.now().toString(),
                date: new Date(),
                durationMinutes: sessionConfig.workMinutes,
                tasksCompleted: tasksCompletedInSession,
                xpEarned: summary.xpEarned,
                mode: sessionConfig.mode,
            }
            setSessions((prev) => [newSession, ...prev])
        }
    }

    // Handle task completion
    const handleCompleteTask = () => {
        setTasksCompletedInSession((prev) => prev + 1)
    }

    // Handle start another session
    const handleStartAnother = () => {
        setSessionConfig(null)
        setSessionSummary(null)
        setSessionState("setup")
    }

    // Handle view progress
    const handleViewProgress = () => {
        router.push("/progress")
    }

    // Handle close complete modal
    const handleCloseComplete = () => {
        setSessionConfig(null)
        setSessionSummary(null)
        setSessionState("setup")
    }

    // Log URL params for future integration
    React.useEffect(() => {
        if (moduleSlug && taskId) {
            console.log("Starting studyflow for:", { moduleSlug, taskId })
        }
    }, [moduleSlug, taskId])

    return (
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Pre-Session Setup */}
            {sessionState === "setup" && (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    {/* Main Setup Area */}
                    <div className="lg:col-span-2">
                        <SessionSetup
                            onStartSession={handleStartSession}
                            availableTasks={MOCK_TASKS}
                        />
                    </div>

                    {/* Sidebar */}
                    <div className="space-y-6">
                        {/* Streak Display */}
                        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                                Your Streak
                            </h3>
                            <StreakDisplay streak={7} />
                        </div>

                        {/* Recent Sessions */}
                        <SessionHistory sessions={sessions} maxDisplay={5} />
                    </div>
                </div>
            )}

            {/* Active Session */}
            {sessionState === "active" && sessionConfig && (
                <ActiveSession
                    config={sessionConfig}
                    onEndSession={handleEndSession}
                    onCompleteTask={handleCompleteTask}
                />
            )}

            {/* Session Complete Modal */}
            {sessionSummary && (
                <SessionComplete
                    isOpen={sessionState === "complete"}
                    summary={sessionSummary}
                    onStartAnother={handleStartAnother}
                    onViewProgress={handleViewProgress}
                    onClose={handleCloseComplete}
                />
            )}
        </div>
    )
}
