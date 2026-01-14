"use client"

/**
 * ============================================================================
 * MODULE NODE — Interactive skill tree node component
 * ============================================================================
 *
 * Displays a single module as a node in the learning path visualization.
 * Supports different states: locked, unlocked, in-progress, completed.
 *
 * @phase SKILLPATH-VISUALIZATION
 */

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Lock,
    CheckCircle2,
    PlayCircle,
    Clock,
    TrendingUp,
    Zap
} from "lucide-react"

export type ModuleNodeStatus = "locked" | "unlocked" | "in-progress" | "completed"
export type ModuleNodeDifficulty = "beginner" | "intermediate" | "advanced" | "expert"

export interface ModuleNodeProps {
    id: string
    slug: string
    title: string
    icon: string
    duration: number // hours
    difficulty: ModuleNodeDifficulty
    status: ModuleNodeStatus
    color: string
    progress?: number // 0-100
    onClick?: () => void
    className?: string
    size?: "small" | "medium" | "large"
}

/**
 * Get difficulty badge color
 */
function getDifficultyColor(difficulty: ModuleNodeDifficulty): string {
    switch (difficulty) {
        case "beginner":
            return "bg-green-500/20 text-green-400 border-green-500/30"
        case "intermediate":
            return "bg-amber-500/20 text-amber-400 border-amber-500/30"
        case "advanced":
            return "bg-red-500/20 text-red-400 border-red-500/30"
        case "expert":
            return "bg-purple-500/20 text-purple-400 border-purple-500/30"
        default:
            return "bg-gray-500/20 text-gray-400 border-gray-500/30"
    }
}

/**
 * Get difficulty label
 */
function getDifficultyLabel(difficulty: ModuleNodeDifficulty): string {
    switch (difficulty) {
        case "beginner":
            return "Nybörjare"
        case "intermediate":
            return "Medel"
        case "advanced":
            return "Avancerad"
        case "expert":
            return "Expert"
        default:
            return "Okänd"
    }
}

/**
 * ModuleNode Component
 */
export function ModuleNode({
    id,
    slug,
    title,
    icon,
    duration,
    difficulty,
    status,
    color,
    progress = 0,
    onClick,
    className,
    size = "medium"
}: ModuleNodeProps) {
    const isLocked = status === "locked"
    const isCompleted = status === "completed"
    const isInProgress = status === "in-progress"
    const isClickable = !isLocked && onClick

    // Size variants
    const sizeClasses = {
        small: "w-32 h-32",
        medium: "w-40 h-40",
        large: "w-48 h-48"
    }

    const iconSizes = {
        small: "text-2xl",
        medium: "text-3xl",
        large: "text-4xl"
    }

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            whileHover={isClickable ? { scale: 1.05, y: -4 } : {}}
            whileTap={isClickable ? { scale: 0.95 } : {}}
            transition={{ ease: [0.16, 1, 0.3, 1] }}
            onClick={isClickable ? onClick : undefined}
            className={cn(
                "relative rounded-2xl overflow-hidden",
                "border-2 backdrop-blur-sm",
                "transition-all duration-300",
                sizeClasses[size],
                isLocked && "opacity-50 grayscale",
                isClickable && "cursor-pointer",
                !isClickable && "cursor-default",
                className
            )}
            style={{
                borderColor: isLocked ? "#4B5563" : color,
                background: isLocked
                    ? "linear-gradient(135deg, rgba(31, 41, 55, 0.5), rgba(17, 24, 39, 0.5))"
                    : `linear-gradient(135deg, ${color}20, ${color}10)`,
                boxShadow: isLocked
                    ? "0 0 20px rgba(0, 0, 0, 0.3)"
                    : `0 0 30px ${color}40`
            }}
        >
            {/* Background glow effect */}
            {!isLocked && (
                <motion.div
                    className="absolute inset-0 opacity-20"
                    style={{
                        background: `radial-gradient(circle at 50% 50%, ${color}, transparent 70%)`
                    }}
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.2, 0.4, 0.2]
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                />
            )}

            {/* Shimmer effect on hover (unlocked only) */}
            {!isLocked && isClickable && (
                <motion.div
                    className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent"
                    initial={{ x: "-100%" }}
                    whileHover={{ x: "100%" }}
                    transition={{ duration: 0.6 }}
                />
            )}

            {/* Content */}
            <div className="relative h-full flex flex-col items-center justify-center p-4 z-10">
                {/* Status Icon (top-right) */}
                <div className="absolute top-2 right-2">
                    {isCompleted && (
                        <motion.div
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ type: "spring", stiffness: 200, damping: 10 }}
                        >
                            <CheckCircle2 className="w-6 h-6 text-green-400" />
                        </motion.div>
                    )}
                    {isInProgress && (
                        <motion.div
                            animate={{ rotate: 360 }}
                            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                        >
                            <PlayCircle className="w-6 h-6 text-blue-400" />
                        </motion.div>
                    )}
                    {isLocked && (
                        <Lock className="w-5 h-5 text-gray-500" />
                    )}
                </div>

                {/* Module Icon */}
                <motion.div
                    className={cn(
                        "mb-2",
                        iconSizes[size]
                    )}
                    animate={!isLocked ? {
                        scale: [1, 1.1, 1],
                        rotate: [0, 5, -5, 0]
                    } : {}}
                    transition={{
                        duration: 2,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                >
                    {icon}
                </motion.div>

                {/* Module Title */}
                <h3 className={cn(
                    "text-center font-semibold mb-1 line-clamp-2",
                    size === "small" ? "text-xs" : size === "medium" ? "text-sm" : "text-base",
                    isLocked ? "text-gray-400" : "text-white"
                )}>
                    {title}
                </h3>

                {/* Duration */}
                <div className="flex items-center gap-1 text-xs text-gray-400 mb-1">
                    <Clock className="w-3 h-3" />
                    <span>{duration}h</span>
                </div>

                {/* Difficulty Badge */}
                <div
                    className={cn(
                        "px-2 py-0.5 rounded-full text-[10px] font-medium border",
                        getDifficultyColor(difficulty)
                    )}
                >
                    {getDifficultyLabel(difficulty)}
                </div>

                {/* Progress Bar (if in progress) */}
                {isInProgress && progress > 0 && (
                    <div className="absolute bottom-0 left-0 right-0 h-1 bg-gray-800">
                        <motion.div
                            className="h-full"
                            style={{ backgroundColor: color }}
                            initial={{ width: 0 }}
                            animate={{ width: `${progress}%` }}
                            transition={{ duration: 0.5, ease: "easeOut" }}
                        />
                    </div>
                )}

                {/* Completion Glow */}
                {isCompleted && (
                    <motion.div
                        className="absolute inset-0 rounded-2xl"
                        style={{
                            boxShadow: `inset 0 0 30px ${color}60`,
                            border: `2px solid ${color}`
                        }}
                        animate={{
                            opacity: [0.5, 1, 0.5]
                        }}
                        transition={{
                            duration: 2,
                            repeat: Infinity,
                            ease: "easeInOut"
                        }}
                    />
                )}
            </div>

            {/* Unlock Animation Overlay */}
            {isLocked && (
                <div className="absolute inset-0 flex items-center justify-center bg-black/60">
                    <div className="text-center">
                        <Lock className="w-8 h-8 text-gray-500 mx-auto mb-2" />
                        <p className="text-xs text-gray-400">Låst</p>
                    </div>
                </div>
            )}
        </motion.div>
    )
}

/**
 * Small variant for compact displays
 */
export function ModuleNodeCompact({
    title,
    icon,
    status,
    color,
    onClick
}: Pick<ModuleNodeProps, "title" | "icon" | "status" | "color" | "onClick">) {
    const isLocked = status === "locked"
    const isCompleted = status === "completed"

    return (
        <motion.div
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={!isLocked ? onClick : undefined}
            className={cn(
                "flex items-center gap-2 px-3 py-2 rounded-lg",
                "border backdrop-blur-sm",
                "transition-all duration-200",
                isLocked && "opacity-50 grayscale cursor-not-allowed",
                !isLocked && "cursor-pointer"
            )}
            style={{
                borderColor: isLocked ? "#4B5563" : color,
                background: isLocked
                    ? "rgba(31, 41, 55, 0.5)"
                    : `linear-gradient(90deg, ${color}20, ${color}10)`
            }}
        >
            <span className="text-xl">{icon}</span>
            <span className={cn(
                "text-sm font-medium flex-1",
                isLocked ? "text-gray-400" : "text-white"
            )}>
                {title}
            </span>
            {isCompleted && (
                <CheckCircle2 className="w-4 h-4 text-green-400" />
            )}
            {isLocked && (
                <Lock className="w-4 h-4 text-gray-500" />
            )}
        </motion.div>
    )
}
