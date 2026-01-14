"use client"

/**
 * ============================================================================
 * PATH CARD — Career path card component
 * ============================================================================
 *
 * Displays a learning path with stats, modules, salary info, and progress.
 * Used in the path selection view.
 *
 * @phase SKILLPATH-VISUALIZATION
 */

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    TrendingUp,
    Clock,
    BookOpen,
    DollarSign,
    Zap,
    Target,
    CheckCircle2,
    ArrowRight,
    Users,
    Award
} from "lucide-react"
import { LearningPath } from "@/lib/learning-paths"
import { Button } from "@/components/ui/button"

export interface PathCardProps {
    path: LearningPath
    progress: number // 0-100
    completedModules: number
    totalModules: number
    onStart: () => void
    className?: string
}

/**
 * PathCard Component
 */
export function PathCard({
    path,
    progress,
    completedModules,
    totalModules,
    onStart,
    className
}: PathCardProps) {
    const isStarted = progress > 0
    const isCompleted = progress === 100

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ scale: 1.02, y: -4 }}
            transition={{ ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "border-2 backdrop-blur-sm",
                "transition-all duration-300",
                "group cursor-pointer",
                className
            )}
            style={{
                borderColor: path.color,
                background: `linear-gradient(135deg, ${path.color}15, ${path.color}05)`,
                boxShadow: `0 0 40px ${path.color}20`
            }}
            onClick={onStart}
        >
            {/* Background glow effect */}
            <motion.div
                className="absolute inset-0 opacity-0 group-hover:opacity-20 transition-opacity duration-300"
                style={{
                    background: `radial-gradient(circle at 50% 50%, ${path.color}, transparent 70%)`
                }}
            />

            {/* Shimmer effect on hover */}
            <motion.div
                className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent opacity-0 group-hover:opacity-100"
                initial={{ x: "-100%" }}
                whileHover={{ x: "100%" }}
                transition={{ duration: 0.8 }}
            />

            {/* Content */}
            <div className="relative p-6 z-10">
                {/* Header */}
                <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center gap-3">
                        {/* Icon */}
                        <motion.div
                            className="text-5xl"
                            animate={{
                                scale: [1, 1.1, 1],
                                rotate: [0, 5, -5, 0]
                            }}
                            transition={{
                                duration: 3,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        >
                            {path.icon}
                        </motion.div>

                        <div>
                            <h3 className="text-xl font-bold text-white mb-1">
                                {path.name}
                            </h3>
                            <p className="text-sm text-gray-400">
                                {path.description}
                            </p>
                        </div>
                    </div>

                    {/* Completion Badge */}
                    {isCompleted && (
                        <motion.div
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ type: "spring", stiffness: 200, damping: 10 }}
                            className="flex items-center gap-1 px-2 py-1 rounded-full bg-green-500/20 border border-green-500/30"
                        >
                            <CheckCircle2 className="w-4 h-4 text-green-400" />
                            <span className="text-xs font-medium text-green-400">Klar</span>
                        </motion.div>
                    )}
                </div>

                {/* Stats Grid */}
                <div className="grid grid-cols-2 gap-3 mb-4">
                    {/* Timeline */}
                    <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-neutral-800/50">
                        <Clock className="w-4 h-4 text-cyan-400" />
                        <div>
                            <p className="text-xs text-gray-400">Tid</p>
                            <p className="text-sm font-semibold text-white">
                                {path.estimatedMonths} månader
                            </p>
                        </div>
                    </div>

                    {/* Modules */}
                    <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-neutral-800/50">
                        <BookOpen className="w-4 h-4 text-purple-400" />
                        <div>
                            <p className="text-xs text-gray-400">Moduler</p>
                            <p className="text-sm font-semibold text-white">
                                {totalModules} st
                            </p>
                        </div>
                    </div>

                    {/* Job Demand */}
                    <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-neutral-800/50">
                        <TrendingUp className="w-4 h-4 text-green-400" />
                        <div>
                            <p className="text-xs text-gray-400">Efterfrågan</p>
                            <p className="text-sm font-semibold text-white">
                                {path.jobDemand}%
                            </p>
                        </div>
                    </div>

                    {/* Salary */}
                    <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-neutral-800/50">
                        <DollarSign className="w-4 h-4 text-amber-400" />
                        <div>
                            <p className="text-xs text-gray-400">Junior lön</p>
                            <p className="text-sm font-semibold text-white">
                                {path.avgSalary.junior}
                            </p>
                        </div>
                    </div>
                </div>

                {/* Salary Range */}
                <div className="mb-4 p-3 rounded-lg bg-neutral-800/30 border border-neutral-700/50">
                    <p className="text-xs text-gray-400 mb-2">Löneintervall:</p>
                    <div className="flex items-center justify-between text-xs">
                        <div>
                            <p className="text-gray-400">Junior</p>
                            <p className="font-semibold text-white">{path.avgSalary.junior}</p>
                        </div>
                        <div className="text-center">
                            <p className="text-gray-400">Mid-level</p>
                            <p className="font-semibold text-white">{path.avgSalary.mid}</p>
                        </div>
                        <div className="text-right">
                            <p className="text-gray-400">Senior</p>
                            <p className="font-semibold text-white">{path.avgSalary.senior}</p>
                        </div>
                    </div>
                </div>

                {/* Skills Tags */}
                <div className="mb-4">
                    <p className="text-xs text-gray-400 mb-2">Viktiga färdigheter:</p>
                    <div className="flex flex-wrap gap-2">
                        {path.skills.slice(0, 6).map((skill, idx) => (
                            <span
                                key={idx}
                                className="px-2 py-1 text-xs font-medium rounded-md bg-neutral-800/50 text-gray-300 border border-neutral-700/50"
                            >
                                {skill}
                            </span>
                        ))}
                        {path.skills.length > 6 && (
                            <span className="px-2 py-1 text-xs font-medium rounded-md bg-neutral-800/50 text-gray-400">
                                +{path.skills.length - 6} mer
                            </span>
                        )}
                    </div>
                </div>

                {/* Progress Bar */}
                {isStarted && (
                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <span className="text-xs text-gray-400">
                                {completedModules}/{totalModules} moduler klara
                            </span>
                            <span className="text-xs font-semibold text-white">
                                {progress}%
                            </span>
                        </div>
                        <div className="h-2 bg-neutral-800 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full rounded-full relative overflow-hidden"
                                style={{ backgroundColor: path.color }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
                            >
                                {/* Shimmer effect */}
                                <motion.div
                                    className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent"
                                    animate={{ x: ['-100%', '100%'] }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                                />
                            </motion.div>
                        </div>
                    </div>
                )}

                {/* Action Button */}
                <Button
                    onClick={(e) => {
                        e.stopPropagation()
                        onStart()
                    }}
                    className={cn(
                        "w-full font-semibold group/btn transition-all duration-300",
                        isStarted
                            ? "bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500"
                            : "bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500"
                    )}
                >
                    <span className="flex items-center justify-center gap-2">
                        {isStarted ? (
                            <>
                                <Target className="w-4 h-4" />
                                <span>Fortsätt bana</span>
                            </>
                        ) : (
                            <>
                                <Zap className="w-4 h-4" />
                                <span>Starta bana</span>
                            </>
                        )}
                        <ArrowRight className="w-4 h-4 transition-transform group-hover/btn:translate-x-1" />
                    </span>
                </Button>
            </div>

            {/* Glow effect on completion */}
            {isCompleted && (
                <motion.div
                    className="absolute inset-0 rounded-2xl pointer-events-none"
                    style={{
                        boxShadow: `inset 0 0 60px ${path.color}60`,
                        border: `2px solid ${path.color}`
                    }}
                    animate={{
                        opacity: [0.3, 0.7, 0.3]
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                />
            )}
        </motion.div>
    )
}

/**
 * Compact Path Card for smaller displays
 */
export function PathCardCompact({
    path,
    progress,
    onStart
}: Pick<PathCardProps, "path" | "progress" | "onStart">) {
    return (
        <motion.div
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            onClick={onStart}
            className="flex items-center gap-3 p-4 rounded-xl border-2 backdrop-blur-sm cursor-pointer transition-all duration-300"
            style={{
                borderColor: path.color,
                background: `linear-gradient(90deg, ${path.color}15, ${path.color}05)`,
                boxShadow: `0 0 20px ${path.color}15`
            }}
        >
            <span className="text-3xl">{path.icon}</span>
            <div className="flex-1">
                <h4 className="text-sm font-bold text-white mb-1">{path.name}</h4>
                {progress > 0 && (
                    <div className="flex items-center gap-2">
                        <div className="flex-1 h-1 bg-neutral-800 rounded-full overflow-hidden">
                            <motion.div
                                className="h-full rounded-full"
                                style={{ backgroundColor: path.color }}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 0.5 }}
                            />
                        </div>
                        <span className="text-xs text-gray-400">{progress}%</span>
                    </div>
                )}
                {progress === 0 && (
                    <p className="text-xs text-gray-400">{path.estimatedMonths} mån • {path.modules.length} moduler</p>
                )}
            </div>
            <ArrowRight className="w-4 h-4 text-gray-400" />
        </motion.div>
    )
}
