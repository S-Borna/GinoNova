"use client"

/**
 * ============================================================================
 * DOE25 TENTA MODULE PAGE — Premium Overview
 * ============================================================================
 *
 * Features:
 * - Beautiful task grid with progress
 * - Countdown to exam date
 * - Module statistics
 * - Quick access to all tasks
 *
 * @phase DOE25-REDESIGN
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { TentaCountdown } from "@/components/ui/tenta-countdown"
import {
    ArrowLeft,
    CheckCircle2,
    Circle,
    Clock,
    BookOpen,
    Zap,
    Trophy,
    Target,
    ChevronRight,
    Play,
    Lock,
    Terminal,
    Server,
    Container,
    Network,
    Sparkles
} from "lucide-react"

import { DOE25_MODULE } from "@/data/doe25-module"

/* ============================================================================
   TASK GROUPS CONFIG
   ============================================================================ */

const taskGroups = [
    {
        id: "modul-0",
        title: "Modul 0: Linux Grunder",
        subtitle: "Nätverk & Filsystem",
        icon: <Network className="w-6 h-6" />,
        color: "from-cyan-500 to-blue-500",
        bgGlow: "rgba(6, 182, 212, 0.2)",
        taskIds: ["doe25-0-1-subnetting", "doe25-0-2-filsystem"]
    },
    {
        id: "modul-1",
        title: "Modul 1: Bash Scripting",
        subtitle: "Automatisering med Shell",
        icon: <Terminal className="w-6 h-6" />,
        color: "from-green-500 to-emerald-500",
        bgGlow: "rgba(16, 185, 129, 0.2)",
        taskIds: [
            "doe25-1-1-bash-grunder",
            "doe25-1-2-variabler",
            "doe25-1-3-regex",
            "doe25-1-4-sed",
            "doe25-1-5-awk",
            "doe25-1-6-villkor",
            "doe25-1-7-interaktiva",
            "doe25-1-8-loopar",
            "doe25-1-9-parametrar",
            "doe25-1-10-funktioner",
            "doe25-1-11-signals"
        ]
    },
    {
        id: "modul-2",
        title: "Modul 2: System Administration",
        subtitle: "Användare, Säkerhet & Tjänster",
        icon: <Server className="w-6 h-6" />,
        color: "from-orange-500 to-amber-500",
        bgGlow: "rgba(245, 158, 11, 0.2)",
        taskIds: [
            "doe25-2-1-users",
            "doe25-2-2-permissions",
            "doe25-2-3-ssh",
            "doe25-2-4-ufw",
            "doe25-2-5-firewalld",
            "doe25-2-6-lagring",
            "doe25-2-7-backup",
            "doe25-2-8-systemd"
        ]
    },
    {
        id: "modul-3",
        title: "Modul 3: DevOps",
        subtitle: "Docker & Git",
        icon: <Container className="w-6 h-6" />,
        color: "from-purple-500 to-violet-500",
        bgGlow: "rgba(139, 92, 246, 0.2)",
        taskIds: [
            "doe25-3-1-docker-grunder",
            "doe25-3-2-docker-images",
            "doe25-3-3-docker-compose",
            "doe25-3-4-git"
        ]
    }
]

/* ============================================================================
   STATS CARD
   ============================================================================ */

function StatCard({ 
    icon, 
    label, 
    value, 
    color 
}: { 
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
}) {
    return (
        <motion.div
            whileHover={{ scale: 1.02 }}
            className={cn(
                "flex items-center gap-4 p-4 rounded-xl",
                "bg-white/5 border border-white/10",
                "hover:border-white/20 transition-colors"
            )}
        >
            <div className={cn(
                "w-12 h-12 rounded-xl flex items-center justify-center",
                `bg-gradient-to-br ${color}`
            )}>
                {icon}
            </div>
            <div>
                <p className="text-2xl font-bold text-white">{value}</p>
                <p className="text-sm text-zinc-400">{label}</p>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function DOE25ModulePage() {
    const [completedTasks, setCompletedTasks] = useState<string[]>([])

    // Load progress from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem("doe25-completed-tasks")
            if (saved) {
                setCompletedTasks(JSON.parse(saved))
            }
        } catch (e) {
            console.log("Could not load progress")
        }
    }, [])

    const totalTasks = DOE25_MODULE.tasks.length
    const completedCount = completedTasks.length
    const progressPercent = Math.round((completedCount / totalTasks) * 100)
    const totalMinutes = DOE25_MODULE.tasks.reduce((acc, t) => acc + t.estimated_minutes, 0)
    const totalHours = Math.round(totalMinutes / 60)

    const getTask = (taskId: string) => DOE25_MODULE.tasks.find(t => t.id === taskId)
    const isCompleted = (taskId: string) => completedTasks.includes(taskId)

    // Find first incomplete task
    const firstIncompleteTask = DOE25_MODULE.tasks.find(t => !completedTasks.includes(t.id))

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Back */}
                <Link
                    href="/learn"
                    className={cn(
                        "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
                        "text-zinc-400 hover:text-white",
                        "bg-white/5 hover:bg-white/10 border border-white/10",
                        "transition-all duration-300"
                    )}
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till Learning
                </Link>

                {/* Hero Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "relative overflow-hidden rounded-3xl mb-8",
                        "bg-gradient-to-br from-amber-500/10 via-orange-500/10 to-red-500/10",
                        "border border-amber-500/20",
                        "p-8 md:p-12"
                    )}
                >
                    {/* Background Glow */}
                    <div className="absolute top-0 right-0 w-96 h-96 bg-amber-500/20 rounded-full blur-[100px]" />
                    <div className="absolute bottom-0 left-0 w-64 h-64 bg-purple-500/10 rounded-full blur-[80px]" />

                    <div className="relative">
                        <div className="flex flex-col md:flex-row md:items-start gap-6 mb-8">
                            {/* Icon */}
                            <motion.div
                                whileHover={{ scale: 1.05, rotate: 5 }}
                                className={cn(
                                    "w-24 h-24 rounded-3xl flex items-center justify-center shrink-0",
                                    "bg-gradient-to-br from-amber-500/30 to-orange-500/30",
                                    "border border-amber-500/40 shadow-lg shadow-amber-500/20"
                                )}
                            >
                                <span className="text-6xl">📝</span>
                            </motion.div>

                            <div className="flex-1">
                                <div className="flex items-center gap-3 mb-3">
                                    <span className="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-500/30 text-amber-400 text-xs font-bold uppercase tracking-wider">
                                        Tenta
                                    </span>
                                    <span className="px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 text-purple-400 text-xs font-bold">
                                        25 Tasks
                                    </span>
                                </div>

                                <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                                    {DOE25_MODULE.name}
                                </h1>

                                <p className="text-lg text-zinc-300 max-w-2xl mb-6">
                                    {DOE25_MODULE.description}
                                </p>

                                {/* Countdown */}
                                <TentaCountdown 
                                    examDate={DOE25_MODULE.exam_date}
                                    className="mb-6"
                                />

                                {/* CTA */}
                                {firstIncompleteTask && (
                                    <Link href={`/modules/doe25-tenta/tasks/${firstIncompleteTask.id}`}>
                                        <motion.button
                                            whileHover={{ scale: 1.02 }}
                                            whileTap={{ scale: 0.98 }}
                                            className={cn(
                                                "flex items-center gap-3 px-6 py-3 rounded-xl",
                                                "bg-gradient-to-r from-purple-600 to-cyan-600",
                                                "text-white font-semibold",
                                                "shadow-lg shadow-purple-500/30",
                                                "hover:shadow-xl hover:shadow-purple-500/40",
                                                "transition-all duration-300"
                                            )}
                                        >
                                            <Play className="w-5 h-5 fill-white" />
                                            {completedCount > 0 ? "Fortsätt plugga" : "Börja plugga"}
                                            <ChevronRight className="w-5 h-5" />
                                        </motion.button>
                                    </Link>
                                )}
                            </div>
                        </div>

                        {/* Stats Grid */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                            <StatCard
                                icon={<Target className="w-6 h-6 text-white" />}
                                label="Tasks klara"
                                value={`${completedCount}/${totalTasks}`}
                                color="from-emerald-500 to-green-500"
                            />
                            <StatCard
                                icon={<Clock className="w-6 h-6 text-white" />}
                                label="Estimerad tid"
                                value={`${totalHours}h`}
                                color="from-blue-500 to-cyan-500"
                            />
                            <StatCard
                                icon={<Zap className="w-6 h-6 text-white" />}
                                label="XP att tjäna"
                                value={`${(totalTasks - completedCount) * 100}`}
                                color="from-amber-500 to-orange-500"
                            />
                            <StatCard
                                icon={<Trophy className="w-6 h-6 text-white" />}
                                label="Progress"
                                value={`${progressPercent}%`}
                                color="from-purple-500 to-violet-500"
                            />
                        </div>
                    </div>
                </motion.div>

                {/* Progress Bar */}
                <div className="mb-8 p-4 rounded-2xl bg-zinc-900/50 border border-zinc-800">
                    <div className="flex justify-between text-sm mb-2">
                        <span className="text-zinc-400">Total progress</span>
                        <span className="text-purple-400 font-medium">{progressPercent}% klar</span>
                    </div>
                    <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                            initial={{ width: 0 }}
                            animate={{ width: `${progressPercent}%` }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            className="h-full bg-gradient-to-r from-purple-500 via-cyan-500 to-emerald-500 rounded-full"
                        />
                    </div>
                </div>

                {/* Task Groups */}
                <div className="space-y-6">
                    {taskGroups.map((group, groupIndex) => {
                        const groupTasks = group.taskIds.map(id => getTask(id)).filter(Boolean)
                        const groupCompleted = group.taskIds.filter(id => isCompleted(id)).length
                        const groupPercent = Math.round((groupCompleted / group.taskIds.length) * 100)

                        return (
                            <motion.div
                                key={group.id}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: groupIndex * 0.1 }}
                                className={cn(
                                    "rounded-2xl overflow-hidden",
                                    "bg-[#0a0a0f] border border-zinc-800/50",
                                    "hover:border-purple-500/30 transition-colors duration-300"
                                )}
                                style={{
                                    boxShadow: `0 0 60px ${group.bgGlow}`,
                                }}
                            >
                                {/* Group Header */}
                                <div className="p-6 border-b border-zinc-800/50">
                                    <div className="flex items-center gap-4">
                                        <div className={cn(
                                            "w-14 h-14 rounded-xl flex items-center justify-center",
                                            `bg-gradient-to-br ${group.color}`
                                        )}>
                                            {group.icon}
                                        </div>
                                        <div className="flex-1">
                                            <h2 className="text-xl font-bold text-white">{group.title}</h2>
                                            <p className="text-sm text-zinc-400">{group.subtitle}</p>
                                        </div>
                                        <div className="text-right">
                                            <p className="text-2xl font-bold text-white">{groupPercent}%</p>
                                            <p className="text-xs text-zinc-500">{groupCompleted}/{group.taskIds.length} klara</p>
                                        </div>
                                    </div>

                                    {/* Group Progress Bar */}
                                    <div className="mt-4 h-2 bg-zinc-800 rounded-full overflow-hidden">
                                        <motion.div
                                            initial={{ width: 0 }}
                                            animate={{ width: `${groupPercent}%` }}
                                            className={cn("h-full rounded-full", `bg-gradient-to-r ${group.color}`)}
                                        />
                                    </div>
                                </div>

                                {/* Tasks Grid */}
                                <div className="p-4 grid gap-2">
                                    {groupTasks.map((task) => {
                                        if (!task) return null
                                        const completed = isCompleted(task.id)

                                        return (
                                            <Link
                                                key={task.id}
                                                href={`/modules/doe25-tenta/tasks/${task.id}`}
                                            >
                                                <motion.div
                                                    whileHover={{ scale: 1.01, x: 4 }}
                                                    className={cn(
                                                        "flex items-center gap-4 p-4 rounded-xl",
                                                        "transition-all duration-200 group",
                                                        completed
                                                            ? "bg-emerald-500/10 border border-emerald-500/20"
                                                            : "bg-white/5 border border-transparent hover:border-purple-500/30"
                                                    )}
                                                >
                                                    {/* Status */}
                                                    <div className={cn(
                                                        "w-8 h-8 rounded-full flex items-center justify-center shrink-0",
                                                        completed
                                                            ? "bg-emerald-500/20"
                                                            : "bg-zinc-800"
                                                    )}>
                                                        {completed ? (
                                                            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                                                        ) : (
                                                            <Circle className="w-4 h-4 text-zinc-600" />
                                                        )}
                                                    </div>

                                                    {/* Info */}
                                                    <div className="flex-1 min-w-0">
                                                        <h3 className={cn(
                                                            "font-medium truncate",
                                                            completed ? "text-emerald-300" : "text-white group-hover:text-purple-300"
                                                        )}>
                                                            {task.title}
                                                        </h3>
                                                        <p className="text-sm text-zinc-500 truncate">
                                                            {task.description}
                                                        </p>
                                                    </div>

                                                    {/* Meta */}
                                                    <div className="flex items-center gap-3 shrink-0">
                                                        <span className="text-xs text-zinc-500 flex items-center gap-1">
                                                            <Clock className="w-3 h-3" />
                                                            {task.estimated_minutes}m
                                                        </span>
                                                        <ChevronRight className={cn(
                                                            "w-5 h-5 transition-transform",
                                                            completed ? "text-emerald-400" : "text-zinc-600 group-hover:text-purple-400 group-hover:translate-x-1"
                                                        )} />
                                                    </div>
                                                </motion.div>
                                            </Link>
                                        )
                                    })}
                                </div>
                            </motion.div>
                        )
                    })}
                </div>

                {/* Completion Message */}
                {completedCount === totalTasks && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className={cn(
                            "mt-8 p-8 rounded-3xl text-center",
                            "bg-gradient-to-r from-emerald-500/20 via-purple-500/20 to-cyan-500/20",
                            "border border-emerald-500/30"
                        )}
                    >
                        <motion.div
                            animate={{ rotate: [0, 10, -10, 0] }}
                            transition={{ duration: 0.5, repeat: Infinity, repeatDelay: 2 }}
                            className="text-6xl mb-4"
                        >
                            🎉
                        </motion.div>
                        <h2 className="text-2xl font-bold text-white mb-2">
                            Grattis! Du har klarat alla tasks!
                        </h2>
                        <p className="text-zinc-300">
                            Du är redo för tentan. Lycka till! 🍀
                        </p>
                    </motion.div>
                )}
            </div>
        </div>
    )
}
