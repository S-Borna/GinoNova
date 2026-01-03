"use client"

/**
 * ============================================================================
 * HANDS-ON LAB MODULE PAGE — Uses Frontend Data (handson-module.ts)
 * ============================================================================
 *
 * Data source: /data/handson-module.ts (7 praktiska labbar)
 * NOT from backend API - all content is in frontend
 *
 * @phase HANDS-ON-LAB
 */

import { useState, useEffect } from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import {
    ArrowLeft,
    CheckCircle2,
    Circle,
    Clock,
    Zap,
    Trophy,
    ChevronRight,
    Play,
    Terminal,
    Server,
    Container,
    Network,
    Shield,
    HardDrive,
    Users,
} from "lucide-react"

// Frontend data source
import { HANDSON_MODULE, HandsOnTask } from "@/data/handson-module"

// ============================================================================
// TASK ICONS
// ============================================================================

const taskIcons: Record<string, React.ReactNode> = {
    "handson-1-onboarding": <Terminal className="w-5 h-5" />,
    "handson-2-pakethantering": <Server className="w-5 h-5" />,
    "handson-3-ssh-brandvagg": <Shield className="w-5 h-5" />,
    "handson-4-anvandarhantering": <Users className="w-5 h-5" />,
    "handson-5-subnetting": <Network className="w-5 h-5" />,
    "handson-6-docker": <Container className="w-5 h-5" />,
    "handson-7-storage": <HardDrive className="w-5 h-5" />,
}

// ============================================================================
// TASK CARD COMPONENT
// ============================================================================

function TaskCard({
    task,
    index,
    isCompleted,
}: {
    task: HandsOnTask
    index: number
    isCompleted: boolean
}) {
    return (
        <Link href={`/modules/hands-on-lab/tasks/${task.id}`}>
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.05 }}
                className={cn(
                    "group relative overflow-hidden rounded-2xl p-5",
                    "bg-[#0d0d12] border",
                    isCompleted
                        ? "border-emerald-500/30"
                        : "border-white/10 hover:border-emerald-500/30",
                    "transition-all duration-300 cursor-pointer"
                )}
            >
                {/* Hover glow */}
                <div className={cn(
                    "absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500",
                    "bg-gradient-to-br from-emerald-500/5 to-transparent"
                )} />

                <div className="relative flex items-start gap-4">
                    {/* Icon */}
                    <div className={cn(
                        "w-12 h-12 rounded-xl flex items-center justify-center shrink-0",
                        isCompleted
                            ? "bg-emerald-500/20 text-emerald-400"
                            : "bg-white/5 text-zinc-400 group-hover:text-emerald-400 group-hover:bg-emerald-500/10"
                    )}>
                        {isCompleted ? (
                            <CheckCircle2 className="w-6 h-6" />
                        ) : (
                            taskIcons[task.id] || <Play className="w-5 h-5" />
                        )}
                    </div>

                    {/* Content */}
                    <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2 mb-1">
                            <span className="text-xs text-emerald-400/60 font-medium">
                                Labb {index + 1}
                            </span>
                            {isCompleted && (
                                <span className="text-xs bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded-full">
                                    Klar
                                </span>
                            )}
                        </div>
                        <h3 className="font-semibold text-white group-hover:text-emerald-300 transition-colors truncate">
                            {task.title}
                        </h3>
                        <p className="text-sm text-zinc-500 mt-1 line-clamp-2">
                            {task.description}
                        </p>

                        {/* Meta */}
                        <div className="flex items-center gap-4 mt-3">
                            <span className="flex items-center gap-1.5 text-xs text-zinc-500">
                                <Clock className="w-3.5 h-3.5" />
                                {task.estimated_minutes} min
                            </span>
                            <span className="flex items-center gap-1.5 text-xs text-amber-400">
                                <Zap className="w-3.5 h-3.5" />
                                +100 XP
                            </span>
                        </div>
                    </div>

                    {/* Arrow */}
                    <ChevronRight className={cn(
                        "w-5 h-5 text-zinc-600 group-hover:text-emerald-400 transition-all",
                        "group-hover:translate-x-1"
                    )} />
                </div>
            </motion.div>
        </Link>
    )
}

// ============================================================================
// MAIN PAGE
// ============================================================================

export default function HandsOnLabPage() {
    const [completedTasks, setCompletedTasks] = useState<string[]>([])

    // Load progress from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem("handson-completed-tasks")
            if (saved) {
                setCompletedTasks(JSON.parse(saved))
            }
        } catch (e) {
            console.log("Could not load progress")
        }
    }, [])

    const tasks = HANDSON_MODULE.tasks
    const totalXP = tasks.length * 100
    const earnedXP = completedTasks.length * 100
    const progress = (completedTasks.length / tasks.length) * 100

    return (
        <div className="min-h-screen bg-[#05050a] relative">
            <CosmicAurora />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Back button */}
                <Link
                    href="/modules"
                    className={cn(
                        "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
                        "text-zinc-400 hover:text-white",
                        "bg-white/5 hover:bg-white/10 border border-white/10",
                        "transition-all duration-300"
                    )}
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till Camp DevOps
                </Link>

                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "relative overflow-hidden rounded-3xl mb-8",
                        "bg-[#0a0a0f] border border-emerald-500/20",
                        "p-8"
                    )}
                    style={{
                        boxShadow: "0 0 80px rgba(16,185,129,0.15)",
                    }}
                >
                    {/* Glow */}
                    <div
                        className="absolute -top-20 -right-20 w-[400px] h-[400px] rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(16,185,129,0.3) 0%, transparent 70%)",
                            filter: "blur(60px)",
                        }}
                    />

                    <div className="relative">
                        {/* Badge */}
                        <div className="flex items-center gap-2 mb-4">
                            <span className="text-3xl">🔬</span>
                            <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider">
                                Praktiska Labbar
                            </span>
                        </div>

                        {/* Title */}
                        <h1 className={cn(
                            "text-3xl md:text-5xl font-black mb-4",
                            "bg-gradient-to-r from-white via-emerald-200 to-cyan-200 bg-clip-text text-transparent"
                        )}>
                            {HANDSON_MODULE.name}
                        </h1>

                        {/* Description */}
                        <p className="text-zinc-300 text-lg mb-6 max-w-2xl">
                            {HANDSON_MODULE.description}
                        </p>

                        {/* Stats */}
                        <div className="flex flex-wrap items-center gap-4">
                            <div className="flex items-center gap-2 bg-white/5 px-4 py-2 rounded-xl border border-white/10">
                                <Terminal className="w-4 h-4 text-emerald-400" />
                                <span className="text-white font-medium">{tasks.length} labbar</span>
                            </div>
                            <div className="flex items-center gap-2 bg-white/5 px-4 py-2 rounded-xl border border-white/10">
                                <Clock className="w-4 h-4 text-emerald-400" />
                                <span className="text-white font-medium">~{HANDSON_MODULE.estimated_hours} timmar</span>
                            </div>
                            <div className="flex items-center gap-2 bg-amber-500/10 px-4 py-2 rounded-xl border border-amber-500/30">
                                <Zap className="w-4 h-4 text-amber-400" />
                                <span className="text-amber-400 font-black">{totalXP} XP</span>
                            </div>
                        </div>

                        {/* Progress */}
                        <div className="mt-6">
                            <div className="flex items-center justify-between text-sm mb-2">
                                <span className="text-zinc-400">Progress</span>
                                <span className="text-emerald-400 font-medium">
                                    {completedTasks.length}/{tasks.length} klara
                                </span>
                            </div>
                            <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                                <motion.div
                                    initial={{ width: 0 }}
                                    animate={{ width: `${progress}%` }}
                                    transition={{ duration: 0.5, ease: "easeOut" }}
                                    className="h-full bg-gradient-to-r from-emerald-500 to-cyan-400"
                                />
                            </div>
                        </div>
                    </div>
                </motion.div>

                {/* Tasks Grid */}
                <div className="space-y-4">
                    <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
                        <Play className="w-5 h-5 text-emerald-400" />
                        Alla Labbar
                    </h2>

                    {tasks.map((task, index) => (
                        <TaskCard
                            key={task.id}
                            task={task}
                            index={index}
                            isCompleted={completedTasks.includes(task.id)}
                        />
                    ))}
                </div>

                {/* Completion message */}
                {completedTasks.length === tasks.length && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className={cn(
                            "mt-8 p-6 rounded-2xl text-center",
                            "bg-gradient-to-br from-emerald-500/20 to-cyan-500/10",
                            "border border-emerald-500/30"
                        )}
                    >
                        <Trophy className="w-12 h-12 text-amber-400 mx-auto mb-4" />
                        <h3 className="text-xl font-bold text-white mb-2">
                            🎉 Grattis! Alla labbar klara!
                        </h3>
                        <p className="text-zinc-400">
                            Du har tjänat {earnedXP} XP och slutfört alla praktiska övningar.
                        </p>
                    </motion.div>
                )}
            </div>
        </div>
    )
}
