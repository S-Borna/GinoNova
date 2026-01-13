"use client"

/**
 * ============================================================================
 * ACHIEVEMENTS SYSTEM — GAMIFICATION EDITION
 * ============================================================================
 *
 * Complete badge and achievement system with:
 * - Multiple achievement categories
 * - Rarity levels (common, rare, epic, legendary)
 * - Progress tracking
 * - Unlock animations
 * - XP rewards
 * - Social sharing
 *
 * @phase GAMIFICATION
 */

import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    UserAchievement,
    getRarityColor,
    getCategoryColor,
    calculateCompletionPercentage,
} from "@/lib/certificates"
import {
    Lock,
    Trophy,
    Sparkles,
    Share2,
    X,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { useState } from "react"

/* ============================================================================
   ACHIEVEMENT CARD
   ============================================================================ */

interface AchievementCardProps {
    achievement: UserAchievement
    onClick?: () => void
    showProgress?: boolean
}

export function AchievementCard({
    achievement,
    onClick,
    showProgress = true,
}: AchievementCardProps) {
    const rarityColors = getRarityColor(achievement.rarity)
    const categoryColors = getCategoryColor(achievement.category)
    const isLocked = achievement.isLocked

    const progress = achievement.progress
        ? calculateCompletionPercentage(achievement.progress.current, achievement.progress.total)
        : 100

    return (
        <motion.div
            whileHover={!isLocked ? { scale: 1.05, y: -5 } : {}}
            onClick={onClick}
            className={cn(
                "relative p-6 rounded-2xl cursor-pointer",
                "bg-gradient-to-br",
                rarityColors.bg,
                "border",
                rarityColors.border,
                "backdrop-blur-sm",
                "transition-all duration-300",
                isLocked && "opacity-50 grayscale"
            )}
            style={{
                boxShadow: !isLocked ? rarityColors.glow : "none",
            }}
        >
            {/* Rarity Badge */}
            <div className="absolute top-3 right-3">
                <span
                    className={cn(
                        "px-2 py-1 rounded-lg text-xs font-bold uppercase",
                        categoryColors.bg,
                        categoryColors.text
                    )}
                >
                    {achievement.rarity}
                </span>
            </div>

            {/* Lock Icon for Locked Achievements */}
            {isLocked && (
                <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                    <Lock className="w-16 h-16 text-zinc-700" />
                </div>
            )}

            <div className="space-y-4">
                {/* Icon & Title */}
                <div className="flex items-start gap-4">
                    <motion.div
                        className={cn(
                            "w-16 h-16 rounded-xl shrink-0",
                            "bg-gradient-to-br from-zinc-800 to-zinc-900",
                            "flex items-center justify-center text-3xl",
                            !isLocked && "shadow-lg"
                        )}
                        animate={
                            !isLocked
                                ? {
                                    boxShadow: [
                                        `0 0 20px ${rarityColors.glow}`,
                                        `0 0 30px ${rarityColors.glow}`,
                                        `0 0 20px ${rarityColors.glow}`,
                                    ],
                                }
                                : {}
                        }
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        {achievement.icon}
                    </motion.div>
                    <div className="flex-1 min-w-0">
                        <h3
                            className={cn(
                                "text-lg font-bold mb-1",
                                isLocked ? "text-zinc-600" : "text-white"
                            )}
                        >
                            {achievement.name}
                        </h3>
                        <p
                            className={cn(
                                "text-sm",
                                isLocked ? "text-zinc-700" : "text-zinc-400"
                            )}
                        >
                            {achievement.description}
                        </p>
                    </div>
                </div>

                {/* Progress Bar */}
                {showProgress && achievement.progress && isLocked && (
                    <div className="space-y-1">
                        <div className="flex justify-between text-xs">
                            <span className="text-zinc-500">Progress</span>
                            <span className="text-zinc-400 font-semibold">
                                {achievement.progress.current} / {achievement.progress.total}
                            </span>
                        </div>
                        <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                            <motion.div
                                className={cn(
                                    "h-full",
                                    "bg-gradient-to-r from-purple-500 to-cyan-500"
                                )}
                                initial={{ width: 0 }}
                                animate={{ width: `${progress}%` }}
                                transition={{ duration: 1, ease: "easeOut" }}
                            />
                        </div>
                    </div>
                )}

                {/* XP Reward & Unlock Date */}
                <div className="flex justify-between items-center pt-3 border-t border-zinc-800">
                    <div className="flex items-center gap-2">
                        <Trophy className={cn("w-4 h-4", rarityColors.text)} />
                        <span className={cn("text-sm font-semibold", rarityColors.text)}>
                            +{achievement.xpReward} XP
                        </span>
                    </div>
                    {achievement.earnedAt && !isLocked && (
                        <span className="text-xs text-zinc-500">
                            Unlocked {new Date(achievement.earnedAt).toLocaleDateString()}
                        </span>
                    )}
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   ACHIEVEMENT CARD WITH FLIP ANIMATION
   ============================================================================ */

interface FlipAchievementCardProps {
    achievement: UserAchievement
}

export function FlipAchievementCard({ achievement }: FlipAchievementCardProps) {
    const [isFlipped, setIsFlipped] = useState(false)
    const rarityColors = getRarityColor(achievement.rarity)
    const categoryColors = getCategoryColor(achievement.category)
    const isLocked = achievement.isLocked

    return (
        <motion.div
            className="relative h-[280px] cursor-pointer perspective-1000"
            onClick={() => !isLocked && setIsFlipped(!isFlipped)}
            whileHover={!isLocked ? { scale: 1.02 } : {}}
        >
            <motion.div
                className="relative w-full h-full"
                animate={{ rotateY: isFlipped ? 180 : 0 }}
                transition={{ duration: 0.6, ease: "easeInOut" }}
                style={{ transformStyle: "preserve-3d" }}
            >
                {/* Front Side */}
                <div
                    className={cn(
                        "absolute inset-0 rounded-2xl p-6",
                        "bg-gradient-to-br",
                        rarityColors.bg,
                        "border",
                        rarityColors.border,
                        "backdrop-blur-sm",
                        isLocked && "opacity-50 grayscale"
                    )}
                    style={{
                        backfaceVisibility: "hidden",
                        boxShadow: !isLocked ? rarityColors.glow : "none",
                    }}
                >
                    {/* Lock overlay */}
                    {isLocked && (
                        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                            <Lock className="w-20 h-20 text-zinc-700" />
                        </div>
                    )}

                    <div className="flex flex-col items-center justify-center h-full space-y-4">
                        <motion.div
                            className="text-6xl"
                            animate={
                                !isLocked
                                    ? {
                                        scale: [1, 1.1, 1],
                                        rotate: [0, 5, -5, 0],
                                    }
                                    : {}
                            }
                            transition={{ duration: 2, repeat: Infinity }}
                        >
                            {achievement.icon}
                        </motion.div>
                        <h3
                            className={cn(
                                "text-xl font-bold text-center",
                                isLocked ? "text-zinc-600" : "text-white"
                            )}
                        >
                            {achievement.name}
                        </h3>
                        <span
                            className={cn(
                                "px-3 py-1 rounded-full text-xs font-bold uppercase",
                                categoryColors.bg,
                                categoryColors.text
                            )}
                        >
                            {achievement.rarity}
                        </span>
                    </div>
                </div>

                {/* Back Side */}
                {!isLocked && (
                    <div
                        className={cn(
                            "absolute inset-0 rounded-2xl p-6",
                            "bg-gradient-to-br",
                            rarityColors.bg,
                            "border",
                            rarityColors.border,
                            "backdrop-blur-sm"
                        )}
                        style={{
                            backfaceVisibility: "hidden",
                            transform: "rotateY(180deg)",
                            boxShadow: rarityColors.glow,
                        }}
                    >
                        <div className="flex flex-col justify-between h-full">
                            <div className="space-y-3">
                                <h3 className="text-lg font-bold text-white">
                                    {achievement.name}
                                </h3>
                                <p className="text-sm text-zinc-400">
                                    {achievement.description}
                                </p>
                                <div className="flex items-center gap-2 pt-2">
                                    <Trophy className={cn("w-5 h-5", rarityColors.text)} />
                                    <span
                                        className={cn("text-lg font-bold", rarityColors.text)}
                                    >
                                        +{achievement.xpReward} XP
                                    </span>
                                </div>
                            </div>
                            {achievement.earnedAt && (
                                <div className="text-center pt-4 border-t border-zinc-800">
                                    <p className="text-xs text-zinc-500 mb-1">Unlocked</p>
                                    <p className="text-sm text-zinc-300 font-semibold">
                                        {new Date(achievement.earnedAt).toLocaleDateString(
                                            "en-US",
                                            {
                                                year: "numeric",
                                                month: "long",
                                                day: "numeric",
                                            }
                                        )}
                                    </p>
                                </div>
                            )}
                        </div>
                    </div>
                )}
            </motion.div>
        </motion.div>
    )
}

/* ============================================================================
   ACHIEVEMENT UNLOCK CELEBRATION
   ============================================================================ */

interface AchievementUnlockProps {
    achievement: UserAchievement
    onClose: () => void
}

export function AchievementUnlockCelebration({
    achievement,
    onClose,
}: AchievementUnlockProps) {
    const rarityColors = getRarityColor(achievement.rarity)

    return (
        <AnimatePresence>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
            >
                {/* Confetti/Sparkles Animation */}
                {[...Array(20)].map((_, i) => (
                    <motion.div
                        key={i}
                        className="absolute text-amber-400"
                        initial={{
                            x: "50vw",
                            y: "50vh",
                            scale: 0,
                            opacity: 1,
                        }}
                        animate={{
                            x: `${50 + (Math.random() - 0.5) * 100}vw`,
                            y: `${50 + (Math.random() - 0.5) * 100}vh`,
                            scale: [0, 1, 0.5],
                            opacity: [1, 1, 0],
                            rotate: Math.random() * 360,
                        }}
                        transition={{
                            duration: 2 + Math.random(),
                            ease: "easeOut",
                        }}
                    >
                        <Sparkles className="w-6 h-6" />
                    </motion.div>
                ))}

                {/* Achievement Card */}
                <motion.div
                    initial={{ scale: 0, rotate: -180 }}
                    animate={{ scale: 1, rotate: 0 }}
                    exit={{ scale: 0, rotate: 180 }}
                    transition={{
                        type: "spring",
                        stiffness: 200,
                        damping: 20,
                    }}
                    className={cn(
                        "relative max-w-md w-full p-8 rounded-3xl",
                        "bg-gradient-to-br",
                        rarityColors.bg,
                        "border-2",
                        rarityColors.border,
                        "backdrop-blur-sm"
                    )}
                    style={{
                        boxShadow: `0 0 100px ${rarityColors.glow}`,
                    }}
                >
                    <Button
                        onClick={onClose}
                        variant="ghost"
                        className="absolute top-4 right-4 rounded-full"
                    >
                        <X className="w-5 h-5" />
                    </Button>

                    <div className="text-center space-y-6">
                        <motion.div
                            animate={{
                                scale: [1, 1.2, 1],
                                rotate: [0, 10, -10, 0],
                            }}
                            transition={{
                                duration: 1,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        >
                            <h2 className="text-3xl font-black bg-gradient-to-r from-amber-400 to-orange-400 bg-clip-text text-transparent">
                                Achievement Unlocked!
                            </h2>
                        </motion.div>

                        <motion.div
                            className="text-8xl"
                            animate={{
                                scale: [1, 1.1, 1],
                                rotate: [0, 5, -5, 0],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        >
                            {achievement.icon}
                        </motion.div>

                        <div>
                            <h3 className={cn("text-2xl font-bold mb-2", rarityColors.text)}>
                                {achievement.name}
                            </h3>
                            <p className="text-zinc-400">{achievement.description}</p>
                        </div>

                        <div className="flex items-center justify-center gap-2 pt-4">
                            <Trophy className={cn("w-6 h-6", rarityColors.text)} />
                            <span className={cn("text-2xl font-bold", rarityColors.text)}>
                                +{achievement.xpReward} XP
                            </span>
                        </div>

                        <Button
                            onClick={() => {
                                // Share functionality
                                alert(
                                    "Share to social media functionality would be implemented here"
                                )
                            }}
                            variant="outline"
                            className={cn(
                                "rounded-xl w-full",
                                "border-purple-500/40",
                                "hover:bg-purple-500/10"
                            )}
                        >
                            <Share2 className="w-4 h-4 mr-2" />
                            Share Achievement
                        </Button>
                    </div>
                </motion.div>
            </motion.div>
        </AnimatePresence>
    )
}

/* ============================================================================
   ACHIEVEMENT PROGRESS WIDGET
   ============================================================================ */

interface AchievementProgressWidgetProps {
    totalAchievements: number
    unlockedAchievements: number
    totalXP: number
    className?: string
}

export function AchievementProgressWidget({
    totalAchievements,
    unlockedAchievements,
    totalXP,
    className,
}: AchievementProgressWidgetProps) {
    const progress = calculateCompletionPercentage(
        unlockedAchievements,
        totalAchievements
    )

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "p-6 rounded-2xl",
                "bg-gradient-to-br from-purple-600/20 to-cyan-600/10",
                "border border-purple-500/30",
                "backdrop-blur-sm",
                className
            )}
        >
            <div className="flex items-center gap-3 mb-4">
                <motion.div
                    className={cn(
                        "w-12 h-12 rounded-xl",
                        "bg-gradient-to-br from-purple-500 to-cyan-500",
                        "flex items-center justify-center"
                    )}
                    animate={{
                        boxShadow: [
                            "0 0 20px rgba(139, 92, 246, 0.4)",
                            "0 0 40px rgba(139, 92, 246, 0.6)",
                            "0 0 20px rgba(139, 92, 246, 0.4)",
                        ],
                    }}
                    transition={{ duration: 2, repeat: Infinity }}
                >
                    <Trophy className="w-6 h-6 text-white" />
                </motion.div>
                <div>
                    <h3 className="text-lg font-bold text-white">Achievement Progress</h3>
                    <p className="text-sm text-zinc-400">
                        {unlockedAchievements} of {totalAchievements} unlocked
                    </p>
                </div>
            </div>

            <div className="space-y-2">
                <div className="flex justify-between text-sm">
                    <span className="text-zinc-500">Progress</span>
                    <span className="text-purple-400 font-semibold">{progress}%</span>
                </div>
                <div className="h-3 bg-zinc-800 rounded-full overflow-hidden">
                    <motion.div
                        className="h-full bg-gradient-to-r from-purple-500 via-cyan-500 to-purple-500"
                        initial={{ width: 0 }}
                        animate={{ width: `${progress}%` }}
                        transition={{ duration: 1.5, ease: "easeOut" }}
                    />
                </div>
            </div>

            <div className="mt-4 pt-4 border-t border-zinc-800 flex justify-between items-center">
                <span className="text-sm text-zinc-500">Total XP Earned</span>
                <span className="text-lg font-bold text-amber-400">{totalXP} XP</span>
            </div>
        </motion.div>
    )
}
