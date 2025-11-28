/**
 * ============================================================================
 * BREAK SCREEN — Break Period Activities & Display
 * ============================================================================
 *
 * Displayed during break periods with:
 * - Stretch suggestions
 * - Hydration reminder
 * - Quick stats from session
 * - Skip break option
 *
 * @phase A.6 - Studyflow Integration
 */

"use client"

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import {
    Coffee,
    Droplets,
    PersonStanding,
    Eye,
    Wind,
    ArrowRight,
    Timer,
    CheckCircle2,
    Zap,
    Flame,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { formatTime, formatDuration } from "@/lib/studyflow/sessionMachine"

/* ============================================================================
   TYPES
   ============================================================================ */

interface BreakActivity {
    id: string
    title: string
    description: string
    icon: React.ReactNode
    duration?: string
    category: "stretch" | "hydration" | "eyes" | "breathing"
}

interface BreakScreenProps {
    timeRemaining: number
    progress: number
    isLongBreak: boolean
    currentSession: number
    totalFocusTime: number
    tasksCompleted: number
    xpEarned: number
    onSkipBreak: () => void
    onEndSession: () => void
    className?: string
}

/* ============================================================================
   BREAK ACTIVITIES DATA
   ============================================================================ */

const STRETCH_ACTIVITIES: BreakActivity[] = [
    {
        id: "neck-roll",
        title: "Neck Rolls",
        description: "Slowly roll your head in circles, 5 times each direction",
        icon: <PersonStanding className="w-5 h-5" />,
        duration: "30s",
        category: "stretch",
    },
    {
        id: "shoulder-shrug",
        title: "Shoulder Shrugs",
        description: "Raise shoulders to ears, hold 5s, release. Repeat 10 times",
        icon: <PersonStanding className="w-5 h-5" />,
        duration: "1m",
        category: "stretch",
    },
    {
        id: "wrist-stretch",
        title: "Wrist Stretches",
        description: "Extend arm, pull fingers back gently. 15s each hand",
        icon: <PersonStanding className="w-5 h-5" />,
        duration: "30s",
        category: "stretch",
    },
    {
        id: "stand-stretch",
        title: "Standing Stretch",
        description: "Stand up, reach for the ceiling, then touch your toes",
        icon: <PersonStanding className="w-5 h-5" />,
        duration: "1m",
        category: "stretch",
    },
]

const EYE_ACTIVITIES: BreakActivity[] = [
    {
        id: "20-20-20",
        title: "20-20-20 Rule",
        description: "Look at something 20 feet away for 20 seconds",
        icon: <Eye className="w-5 h-5" />,
        duration: "20s",
        category: "eyes",
    },
    {
        id: "eye-circles",
        title: "Eye Circles",
        description: "Roll your eyes in circles, 5 times each direction",
        icon: <Eye className="w-5 h-5" />,
        duration: "30s",
        category: "eyes",
    },
    {
        id: "palming",
        title: "Palm Your Eyes",
        description: "Cup your palms over closed eyes, relax for 30 seconds",
        icon: <Eye className="w-5 h-5" />,
        duration: "30s",
        category: "eyes",
    },
]

const BREATHING_ACTIVITIES: BreakActivity[] = [
    {
        id: "deep-breath",
        title: "Deep Breathing",
        description: "Breathe in for 4s, hold 4s, out for 4s. Repeat 5 times",
        icon: <Wind className="w-5 h-5" />,
        duration: "1m",
        category: "breathing",
    },
    {
        id: "box-breathing",
        title: "Box Breathing",
        description: "4s inhale, 4s hold, 4s exhale, 4s hold. Repeat 4 times",
        icon: <Wind className="w-5 h-5" />,
        duration: "1m",
        category: "breathing",
    },
]

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function BreakScreen({
    timeRemaining,
    progress,
    isLongBreak,
    currentSession,
    totalFocusTime,
    tasksCompleted,
    xpEarned,
    onSkipBreak,
    onEndSession,
    className,
}: BreakScreenProps) {
    const [currentActivity, setCurrentActivity] = useState<BreakActivity | null>(null)
    const [completedActivities, setCompletedActivities] = useState<string[]>([])

    // Randomly select an activity on mount
    useEffect(() => {
        const allActivities = [
            ...STRETCH_ACTIVITIES,
            ...EYE_ACTIVITIES,
            ...BREATHING_ACTIVITIES,
        ]
        const randomIndex = Math.floor(Math.random() * allActivities.length)
        setCurrentActivity(allActivities[randomIndex])
    }, [])

    const markActivityComplete = (activityId: string) => {
        setCompletedActivities((prev) => [...prev, activityId])
        // Pick a new activity
        const allActivities = [
            ...STRETCH_ACTIVITIES,
            ...EYE_ACTIVITIES,
            ...BREATHING_ACTIVITIES,
        ].filter((a) => !completedActivities.includes(a.id) && a.id !== activityId)
        
        if (allActivities.length > 0) {
            const randomIndex = Math.floor(Math.random() * allActivities.length)
            setCurrentActivity(allActivities[randomIndex])
        }
    }

    const getCategoryColor = (category: BreakActivity["category"]) => {
        switch (category) {
            case "stretch":
                return "from-purple-500 to-pink-500"
            case "hydration":
                return "from-blue-500 to-cyan-500"
            case "eyes":
                return "from-green-500 to-emerald-500"
            case "breathing":
                return "from-indigo-500 to-purple-500"
            default:
                return "from-gray-500 to-gray-600"
        }
    }

    return (
        <div
            className={cn(
                "min-h-[400px] flex flex-col items-center justify-center p-8",
                className
            )}
        >
            {/* Break header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center mb-8"
            >
                <div className="flex items-center justify-center gap-2 mb-2">
                    <Coffee className="w-6 h-6 text-amber-400" />
                    <h2 className="text-2xl font-bold text-white">
                        {isLongBreak ? "Long Break" : "Break Time"}
                    </h2>
                </div>
                <p className="text-muted-foreground">
                    Take a moment to rest and recharge
                </p>
            </motion.div>

            {/* Timer display */}
            <motion.div
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ delay: 0.1 }}
                className="mb-8"
            >
                <div className="relative w-48 h-48">
                    {/* Background circle */}
                    <svg className="w-full h-full transform -rotate-90">
                        <circle
                            cx="96"
                            cy="96"
                            r="88"
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="8"
                            className="text-white/10"
                        />
                        <circle
                            cx="96"
                            cy="96"
                            r="88"
                            fill="none"
                            stroke="url(#breakGradient)"
                            strokeWidth="8"
                            strokeLinecap="round"
                            strokeDasharray={2 * Math.PI * 88}
                            strokeDashoffset={2 * Math.PI * 88 * (1 - progress / 100)}
                            className="transition-all duration-1000"
                        />
                        <defs>
                            <linearGradient
                                id="breakGradient"
                                x1="0%"
                                y1="0%"
                                x2="100%"
                                y2="0%"
                            >
                                <stop offset="0%" stopColor="#f59e0b" />
                                <stop offset="100%" stopColor="#f97316" />
                            </linearGradient>
                        </defs>
                    </svg>
                    {/* Time display */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center">
                        <span className="text-4xl font-bold text-white tabular-nums">
                            {formatTime(timeRemaining)}
                        </span>
                        <span className="text-sm text-muted-foreground">remaining</span>
                    </div>
                </div>
            </motion.div>

            {/* Hydration reminder */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className={cn(
                    "w-full max-w-md p-4 rounded-xl mb-6",
                    "bg-gradient-to-r from-blue-500/20 to-cyan-500/20",
                    "border border-blue-500/30"
                )}
            >
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-blue-500/20 flex items-center justify-center">
                        <Droplets className="w-5 h-5 text-blue-400" />
                    </div>
                    <div>
                        <p className="font-medium text-white">Stay Hydrated!</p>
                        <p className="text-sm text-muted-foreground">
                            Take a sip of water to keep your focus sharp
                        </p>
                    </div>
                </div>
            </motion.div>

            {/* Activity suggestion */}
            <AnimatePresence mode="wait">
                {currentActivity && (
                    <motion.div
                        key={currentActivity.id}
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: -20 }}
                        className={cn(
                            "w-full max-w-md p-4 rounded-xl mb-6",
                            `bg-gradient-to-r ${getCategoryColor(currentActivity.category)}`,
                            "bg-opacity-20"
                        )}
                        style={{
                            background: `linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1))`,
                        }}
                    >
                        <div className="flex items-start gap-3">
                            <div className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center shrink-0">
                                {currentActivity.icon}
                            </div>
                            <div className="flex-1">
                                <div className="flex items-center justify-between mb-1">
                                    <p className="font-medium text-white">
                                        {currentActivity.title}
                                    </p>
                                    {currentActivity.duration && (
                                        <span className="text-xs text-muted-foreground">
                                            {currentActivity.duration}
                                        </span>
                                    )}
                                </div>
                                <p className="text-sm text-white/70">
                                    {currentActivity.description}
                                </p>
                            </div>
                        </div>
                        <Button
                            onClick={() => markActivityComplete(currentActivity.id)}
                            variant="ghost"
                            size="sm"
                            className="w-full mt-3 bg-white/10 hover:bg-white/20"
                        >
                            <CheckCircle2 className="w-4 h-4 mr-2" />
                            Done, show another
                        </Button>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Session stats */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
                className="w-full max-w-md grid grid-cols-3 gap-3 mb-6"
            >
                <StatCard
                    icon={<Timer className="w-4 h-4" />}
                    label="Focus Time"
                    value={formatDuration(totalFocusTime)}
                    color="text-indigo-400"
                />
                <StatCard
                    icon={<CheckCircle2 className="w-4 h-4" />}
                    label="Tasks"
                    value={tasksCompleted.toString()}
                    color="text-green-400"
                />
                <StatCard
                    icon={<Zap className="w-4 h-4" />}
                    label="XP Earned"
                    value={`+${xpEarned}`}
                    color="text-orange-400"
                />
            </motion.div>

            {/* Actions */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.4 }}
                className="flex items-center gap-3"
            >
                <Button
                    onClick={onSkipBreak}
                    className="bg-gradient-to-r from-indigo-500 to-purple-500"
                >
                    Skip Break
                    <ArrowRight className="ml-2 w-4 h-4" />
                </Button>
                <Button onClick={onEndSession} variant="outline">
                    End Session
                </Button>
            </motion.div>

            {/* Session counter */}
            <motion.p
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
                className="mt-4 text-sm text-muted-foreground flex items-center gap-2"
            >
                <Flame className="w-4 h-4 text-orange-400" />
                Session {currentSession} complete
            </motion.p>
        </div>
    )
}

/* ============================================================================
   STAT CARD COMPONENT
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string
    color: string
}

function StatCard({ icon, label, value, color }: StatCardProps) {
    return (
        <div className="p-3 rounded-lg bg-white/5 border border-white/10 text-center">
            <div className={cn("flex justify-center mb-1", color)}>{icon}</div>
            <p className="text-lg font-bold text-white">{value}</p>
            <p className="text-xs text-muted-foreground">{label}</p>
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default BreakScreen
