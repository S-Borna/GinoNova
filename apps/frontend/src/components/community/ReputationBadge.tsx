"use client"

/**
 * ============================================================================
 * REPUTATION BADGE — Display User Reputation
 * ============================================================================
 *
 * Shows reputation score with visual badge and level
 */

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { getReputationLevel, getProgressToNextLevel } from "@/lib/reputation"
import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger,
} from "@/components/ui/tooltip"
import { TrendingUp } from "lucide-react"

interface ReputationBadgeProps {
    reputation: number
    showProgress?: boolean
    size?: "sm" | "md" | "lg"
    className?: string
}

export function ReputationBadge({
    reputation,
    showProgress = false,
    size = "md",
    className,
}: ReputationBadgeProps) {
    const level = getReputationLevel(reputation)
    const progress = getProgressToNextLevel(reputation)

    const sizeClasses = {
        sm: "text-xs px-2 py-1",
        md: "text-sm px-3 py-1.5",
        lg: "text-base px-4 py-2",
    }

    const iconSizes = {
        sm: "text-xs",
        md: "text-sm",
        lg: "text-base",
    }

    return (
        <TooltipProvider>
            <Tooltip>
                <TooltipTrigger asChild>
                    <motion.div
                        whileHover={{ scale: 1.05 }}
                        className={cn(
                            "inline-flex items-center gap-1.5 rounded-xl font-semibold",
                            "bg-gradient-to-r",
                            level.gradient,
                            "bg-opacity-20 border border-current/30",
                            sizeClasses[size],
                            level.color,
                            className
                        )}
                        style={{
                            boxShadow: `0 0 20px ${level.glowColor}`,
                        }}
                    >
                        <span className={iconSizes[size]}>{level.icon}</span>
                        <span className="font-bold">{reputation}</span>
                    </motion.div>
                </TooltipTrigger>
                <TooltipContent
                    side="bottom"
                    className="bg-zinc-900 border-zinc-800 p-4 max-w-xs"
                >
                    <div className="space-y-3">
                        <div>
                            <div className="flex items-center justify-between mb-1">
                                <span className="text-sm font-semibold text-white">
                                    {level.level}
                                </span>
                                <span className="text-xs text-zinc-400">
                                    {reputation} points
                                </span>
                            </div>
                            {progress.nextLevel && (
                                <>
                                    <div className="w-full h-2 bg-zinc-800 rounded-full overflow-hidden">
                                        <motion.div
                                            initial={{ width: 0 }}
                                            animate={{ width: `${progress.progress}%` }}
                                            transition={{ duration: 0.5, ease: "easeOut" }}
                                            className={cn(
                                                "h-full bg-gradient-to-r",
                                                level.gradient
                                            )}
                                        />
                                    </div>
                                    <div className="flex items-center justify-between mt-1">
                                        <span className="text-xs text-zinc-500">
                                            Next: {progress.nextLevel.level}{" "}
                                            {progress.nextLevel.icon}
                                        </span>
                                        <span className="text-xs text-zinc-500">
                                            {progress.pointsToNext} points to go
                                        </span>
                                    </div>
                                </>
                            )}
                            {!progress.nextLevel && (
                                <p className="text-xs text-zinc-500 mt-1">
                                    Maximum level reached!
                                </p>
                            )}
                        </div>

                        <div className="border-t border-zinc-800 pt-3">
                            <p className="text-xs text-zinc-400 mb-2">
                                How to earn reputation:
                            </p>
                            <div className="space-y-1 text-xs text-zinc-500">
                                <div className="flex justify-between">
                                    <span>Post a question</span>
                                    <span className="text-emerald-400">+5</span>
                                </div>
                                <div className="flex justify-between">
                                    <span>Reply to question</span>
                                    <span className="text-emerald-400">+10</span>
                                </div>
                                <div className="flex justify-between">
                                    <span>Receive upvote</span>
                                    <span className="text-emerald-400">+2</span>
                                </div>
                                <div className="flex justify-between">
                                    <span>Best answer accepted</span>
                                    <span className="text-emerald-400">+25</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </TooltipContent>
            </Tooltip>
        </TooltipProvider>
    )
}
