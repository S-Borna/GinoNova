"use client"

/**
 * ============================================================================
 * DOE25 TASK SIDEBAR - Quick Navigation Between Tasks
 * ============================================================================
 *
 * Features:
 * - Collapsible sidebar with all 25 tasks grouped by module
 * - Current task highlighted
 * - Progress indicators
 * - Smooth animations
 * - Mobile-friendly drawer
 *
 * @phase DOE25-REDESIGN
 */

import * as React from "react"
import { useState, useEffect } from "react"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
    ChevronLeft, 
    ChevronRight, 
    CheckCircle2, 
    Circle, 
    Play,
    BookOpen,
    Terminal,
    Server,
    Container,
    Network,
    FileCode,
    X
} from "lucide-react"
import { DOE25_MODULE, DOE25Task } from "@/data/doe25-module"

/* ============================================================================
   TYPES
   ============================================================================ */

interface DOE25TaskSidebarProps {
    currentTaskId: string
    completedTasks?: string[]
    className?: string
}

/* ============================================================================
   TASK GROUPS CONFIG
   ============================================================================ */

const taskGroups = [
    {
        id: "modul-0",
        title: "Modul 0: Linux Grunder",
        icon: <Network className="w-4 h-4" />,
        color: "from-cyan-500 to-blue-500",
        taskIds: ["doe25-0-1-subnetting", "doe25-0-2-filsystem"]
    },
    {
        id: "modul-1",
        title: "Modul 1: Bash Scripting",
        icon: <Terminal className="w-4 h-4" />,
        color: "from-green-500 to-emerald-500",
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
        title: "Modul 2: System Admin",
        icon: <Server className="w-4 h-4" />,
        color: "from-orange-500 to-amber-500",
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
        icon: <Container className="w-4 h-4" />,
        color: "from-purple-500 to-violet-500",
        taskIds: [
            "doe25-3-1-docker-grunder",
            "doe25-3-2-docker-images",
            "doe25-3-3-docker-compose",
            "doe25-3-4-git"
        ]
    }
]

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function DOE25TaskSidebar({ 
    currentTaskId, 
    completedTasks = [],
    className 
}: DOE25TaskSidebarProps) {
    const [isOpen, setIsOpen] = useState(true)
    const [isMobile, setIsMobile] = useState(false)
    const [expandedGroups, setExpandedGroups] = useState<string[]>(
        // Auto-expand group containing current task
        taskGroups.filter(g => g.taskIds.includes(currentTaskId)).map(g => g.id)
    )

    // Detect mobile
    useEffect(() => {
        const checkMobile = () => setIsMobile(window.innerWidth < 1024)
        checkMobile()
        window.addEventListener("resize", checkMobile)
        return () => window.removeEventListener("resize", checkMobile)
    }, [])

    // On mobile, start closed
    useEffect(() => {
        if (isMobile) setIsOpen(false)
    }, [isMobile])

    const toggleGroup = (groupId: string) => {
        setExpandedGroups(prev => 
            prev.includes(groupId) 
                ? prev.filter(id => id !== groupId)
                : [...prev, groupId]
        )
    }

    const getTaskStatus = (taskId: string) => {
        if (taskId === currentTaskId) return "current"
        if (completedTasks.includes(taskId)) return "completed"
        return "pending"
    }

    const getTask = (taskId: string) => 
        DOE25_MODULE.tasks.find(t => t.id === taskId)

    // Calculate progress
    const totalTasks = DOE25_MODULE.tasks.length
    const completedCount = completedTasks.length
    const progressPercent = Math.round((completedCount / totalTasks) * 100)

    return (
        <>
            {/* Mobile Toggle Button */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={cn(
                    "fixed left-4 top-24 z-50 lg:hidden",
                    "w-12 h-12 rounded-xl",
                    "bg-purple-600 hover:bg-purple-500",
                    "flex items-center justify-center",
                    "shadow-lg shadow-purple-500/30",
                    "transition-all duration-300",
                    isOpen && "opacity-0 pointer-events-none"
                )}
            >
                <BookOpen className="w-5 h-5 text-white" />
            </button>

            {/* Backdrop for mobile */}
            <AnimatePresence>
                {isOpen && isMobile && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        onClick={() => setIsOpen(false)}
                        className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
                    />
                )}
            </AnimatePresence>

            {/* Sidebar */}
            <AnimatePresence mode="wait">
                {isOpen && (
                    <motion.aside
                        initial={{ x: -300, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        exit={{ x: -300, opacity: 0 }}
                        transition={{ type: "spring", damping: 25, stiffness: 300 }}
                        className={cn(
                            "fixed lg:sticky top-0 left-0 h-screen",
                            "w-80 max-w-[85vw]",
                            "bg-[#0a0a0f]/95 backdrop-blur-xl",
                            "border-r border-purple-500/20",
                            "z-50 lg:z-30",
                            "flex flex-col",
                            "overflow-hidden",
                            className
                        )}
                    >
                        {/* Header */}
                        <div className="p-4 border-b border-purple-500/20">
                            <div className="flex items-center justify-between mb-4">
                                <h2 className="text-lg font-bold text-white flex items-center gap-2">
                                    <span className="text-2xl">📝</span>
                                    DOE25 Tenta
                                </h2>
                                <button
                                    onClick={() => setIsOpen(false)}
                                    className="p-2 rounded-lg hover:bg-white/10 transition-colors lg:hidden"
                                >
                                    <X className="w-5 h-5 text-zinc-400" />
                                </button>
                            </div>

                            {/* Progress Bar */}
                            <div className="space-y-2">
                                <div className="flex justify-between text-xs">
                                    <span className="text-zinc-400">Progress</span>
                                    <span className="text-purple-400 font-medium">
                                        {completedCount}/{totalTasks} tasks
                                    </span>
                                </div>
                                <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                    <motion.div
                                        initial={{ width: 0 }}
                                        animate={{ width: `${progressPercent}%` }}
                                        className="h-full bg-gradient-to-r from-purple-500 to-cyan-500 rounded-full"
                                    />
                                </div>
                            </div>
                        </div>

                        {/* Task Groups */}
                        <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-2">
                            {taskGroups.map((group) => {
                                const isExpanded = expandedGroups.includes(group.id)
                                const groupTasks = group.taskIds.map(id => getTask(id)).filter(Boolean) as DOE25Task[]
                                const groupCompleted = group.taskIds.filter(id => completedTasks.includes(id)).length
                                const hasCurrentTask = group.taskIds.includes(currentTaskId)

                                return (
                                    <div key={group.id} className="space-y-1">
                                        {/* Group Header */}
                                        <button
                                            onClick={() => toggleGroup(group.id)}
                                            className={cn(
                                                "w-full flex items-center gap-3 p-3 rounded-xl",
                                                "text-left transition-all duration-200",
                                                hasCurrentTask 
                                                    ? "bg-purple-500/20 border border-purple-500/30"
                                                    : "hover:bg-white/5 border border-transparent"
                                            )}
                                        >
                                            <div className={cn(
                                                "w-8 h-8 rounded-lg flex items-center justify-center",
                                                `bg-gradient-to-br ${group.color}`
                                            )}>
                                                {group.icon}
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <div className="text-sm font-medium text-white truncate">
                                                    {group.title}
                                                </div>
                                                <div className="text-xs text-zinc-500">
                                                    {groupCompleted}/{group.taskIds.length} klara
                                                </div>
                                            </div>
                                            <motion.div
                                                animate={{ rotate: isExpanded ? 90 : 0 }}
                                                transition={{ duration: 0.2 }}
                                            >
                                                <ChevronRight className="w-4 h-4 text-zinc-500" />
                                            </motion.div>
                                        </button>

                                        {/* Tasks */}
                                        <AnimatePresence>
                                            {isExpanded && (
                                                <motion.div
                                                    initial={{ height: 0, opacity: 0 }}
                                                    animate={{ height: "auto", opacity: 1 }}
                                                    exit={{ height: 0, opacity: 0 }}
                                                    transition={{ duration: 0.2 }}
                                                    className="overflow-hidden"
                                                >
                                                    <div className="pl-4 space-y-1 py-1">
                                                        {groupTasks.map((task) => {
                                                            const status = getTaskStatus(task.id)
                                                            
                                                            return (
                                                                <Link
                                                                    key={task.id}
                                                                    href={`/modules/doe25-tenta/tasks/${task.id}`}
                                                                    onClick={() => isMobile && setIsOpen(false)}
                                                                    className={cn(
                                                                        "flex items-center gap-3 p-2.5 rounded-lg",
                                                                        "transition-all duration-200 group",
                                                                        status === "current" 
                                                                            ? "bg-gradient-to-r from-purple-500/30 to-cyan-500/20 border border-purple-500/40"
                                                                            : "hover:bg-white/5 border border-transparent"
                                                                    )}
                                                                >
                                                                    {/* Status Icon */}
                                                                    <div className={cn(
                                                                        "w-6 h-6 rounded-full flex items-center justify-center shrink-0",
                                                                        status === "completed" && "bg-emerald-500/20",
                                                                        status === "current" && "bg-purple-500/30",
                                                                        status === "pending" && "bg-zinc-800"
                                                                    )}>
                                                                        {status === "completed" && (
                                                                            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                                                        )}
                                                                        {status === "current" && (
                                                                            <motion.div
                                                                                animate={{ scale: [1, 1.2, 1] }}
                                                                                transition={{ duration: 1.5, repeat: Infinity }}
                                                                            >
                                                                                <Play className="w-3 h-3 text-purple-400 fill-purple-400" />
                                                                            </motion.div>
                                                                        )}
                                                                        {status === "pending" && (
                                                                            <Circle className="w-3 h-3 text-zinc-600" />
                                                                        )}
                                                                    </div>

                                                                    {/* Task Info */}
                                                                    <div className="flex-1 min-w-0">
                                                                        <div className={cn(
                                                                            "text-sm truncate",
                                                                            status === "current" 
                                                                                ? "text-white font-medium"
                                                                                : status === "completed"
                                                                                    ? "text-zinc-400"
                                                                                    : "text-zinc-300 group-hover:text-white"
                                                                        )}>
                                                                            {task.title}
                                                                        </div>
                                                                    </div>

                                                                    {/* Time */}
                                                                    <span className="text-xs text-zinc-600">
                                                                        {task.estimated_minutes}m
                                                                    </span>
                                                                </Link>
                                                            )
                                                        })}
                                                    </div>
                                                </motion.div>
                                            )}
                                        </AnimatePresence>
                                    </div>
                                )
                            })}
                        </div>

                        {/* Footer - Quick Jump */}
                        <div className="p-4 border-t border-purple-500/20 bg-[#0a0a0f]">
                            <Link
                                href="/modules/doe25-tenta"
                                className={cn(
                                    "flex items-center justify-center gap-2 w-full",
                                    "py-2.5 px-4 rounded-xl",
                                    "bg-white/5 hover:bg-white/10",
                                    "border border-white/10",
                                    "text-sm text-zinc-300 hover:text-white",
                                    "transition-all duration-200"
                                )}
                            >
                                <BookOpen className="w-4 h-4" />
                                Modulöversikt
                            </Link>
                        </div>
                    </motion.aside>
                )}
            </AnimatePresence>

            {/* Desktop Toggle - when closed */}
            {!isOpen && !isMobile && (
                <motion.button
                    initial={{ x: -20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    onClick={() => setIsOpen(true)}
                    className={cn(
                        "fixed left-0 top-1/2 -translate-y-1/2 z-40",
                        "w-8 h-24 rounded-r-xl",
                        "bg-purple-600 hover:bg-purple-500",
                        "flex items-center justify-center",
                        "shadow-lg shadow-purple-500/30",
                        "transition-all duration-300"
                    )}
                >
                    <ChevronRight className="w-5 h-5 text-white" />
                </motion.button>
            )}

            {/* Custom Scrollbar Styles */}
            <style jsx global>{`
                .custom-scrollbar::-webkit-scrollbar {
                    width: 6px;
                }
                .custom-scrollbar::-webkit-scrollbar-track {
                    background: transparent;
                }
                .custom-scrollbar::-webkit-scrollbar-thumb {
                    background: rgba(168, 85, 247, 0.3);
                    border-radius: 3px;
                }
                .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                    background: rgba(168, 85, 247, 0.5);
                }
            `}</style>
        </>
    )
}

export default DOE25TaskSidebar
