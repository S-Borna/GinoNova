"use client"

/**
 * ============================================================================
 * QUIZ BLOCK COMPONENT - Interactive Multiple Choice Questions
 * ============================================================================
 *
 * Features:
 * - Radio buttons for options
 * - Submit button
 * - Correct/incorrect feedback with EPIC confetti celebration
 * - 1 retry on wrong answer
 * - Dallas wizard step-in on 2nd failure
 * - Explanation after answering
 * - XP bonus display
 * - Disabled state after answering
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { HelpCircle, CheckCircle2, XCircle, Sparkles, RotateCcw, BookOpen, Wand2 } from "lucide-react"

/* ============================================================================
   CONFETTI SYSTEM - Epic celebration particles
   ============================================================================ */

interface ConfettiPiece {
    id: number
    x: number
    y: number
    rotation: number
    scale: number
    color: string
    velocityX: number
    velocityY: number
    spin: number
    shape: 'square' | 'circle' | 'star' | 'triangle'
}

const CONFETTI_COLORS = [
    '#FFD700', // Gold
    '#FF6B6B', // Coral
    '#4ECDC4', // Teal
    '#45B7D1', // Sky
    '#96CEB4', // Sage
    '#FFEAA7', // Cream
    '#DDA0DD', // Plum
    '#98D8C8', // Mint
    '#F7DC6F', // Yellow
    '#BB8FCE', // Purple
]

function ConfettiExplosion({ onComplete }: { onComplete: () => void }) {
    const [pieces, setPieces] = useState<ConfettiPiece[]>([])

    useEffect(() => {
        // Create 80 confetti pieces for dramatic effect
        const newPieces: ConfettiPiece[] = []
        for (let i = 0; i < 80; i++) {
            const angle = (Math.PI * 2 * i) / 80 + Math.random() * 0.5
            const velocity = 8 + Math.random() * 15
            newPieces.push({
                id: i,
                x: 50, // Start from center
                y: 40,
                rotation: Math.random() * 360,
                scale: 0.5 + Math.random() * 0.8,
                color: CONFETTI_COLORS[Math.floor(Math.random() * CONFETTI_COLORS.length)],
                velocityX: Math.cos(angle) * velocity,
                velocityY: Math.sin(angle) * velocity - 5,
                spin: (Math.random() - 0.5) * 20,
                shape: ['square', 'circle', 'star', 'triangle'][Math.floor(Math.random() * 4)] as ConfettiPiece['shape'],
            })
        }
        setPieces(newPieces)

        // Cleanup after animation
        const timer = setTimeout(onComplete, 3000)
        return () => clearTimeout(timer)
    }, [onComplete])

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none z-50">
            {pieces.map((piece) => (
                <motion.div
                    key={piece.id}
                    initial={{
                        x: `${piece.x}%`,
                        y: `${piece.y}%`,
                        rotate: piece.rotation,
                        scale: 0,
                        opacity: 1,
                    }}
                    animate={{
                        x: `${piece.x + piece.velocityX * 8}%`,
                        y: `${piece.y + piece.velocityY * 8 + 60}%`,
                        rotate: piece.rotation + piece.spin * 20,
                        scale: piece.scale,
                        opacity: 0,
                    }}
                    transition={{
                        duration: 2.5,
                        ease: [0.25, 0.46, 0.45, 0.94],
                    }}
                    className="absolute"
                    style={{
                        width: piece.shape === 'star' ? 16 : 10,
                        height: piece.shape === 'star' ? 16 : 10,
                        backgroundColor: piece.shape !== 'star' ? piece.color : 'transparent',
                        borderRadius: piece.shape === 'circle' ? '50%' : piece.shape === 'triangle' ? '0' : '2px',
                        clipPath: piece.shape === 'triangle'
                            ? 'polygon(50% 0%, 0% 100%, 100% 100%)'
                            : piece.shape === 'star'
                                ? 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)'
                                : 'none',
                        background: piece.shape === 'star' ? piece.color : undefined,
                    }}
                />
            ))}
            {/* Central burst glow */}
            <motion.div
                initial={{ scale: 0, opacity: 0.8 }}
                animate={{ scale: 3, opacity: 0 }}
                transition={{ duration: 0.8, ease: "easeOut" }}
                className="absolute left-1/2 top-1/3 -translate-x-1/2 -translate-y-1/2 w-32 h-32 rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(255,215,0,0.6) 0%, rgba(255,215,0,0) 70%)',
                }}
            />
        </div>
    )
}

/* ============================================================================
   DALLAS HELPER - Steps in after 2nd wrong answer
   ============================================================================ */

const DALLAS_QUOTES = [
    "Mistakes are proof that you're trying. Let's learn together!",
    "Every expert was once a beginner. You've got this!",
    "The only real failure is giving up. Let's break this down.",
]

function DallasHelper({
    explanation,
    correctAnswer,
    onDismiss
}: {
    explanation: string
    correctAnswer: string
    onDismiss: () => void
}) {
    const [quote] = useState(() => DALLAS_QUOTES[Math.floor(Math.random() * DALLAS_QUOTES.length)])

    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -10, scale: 0.95 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className="mt-4 relative overflow-hidden"
        >
            {/* Magical border glow */}
            <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-500/20 via-purple-500/20 to-blue-500/20 blur-xl" />

            <div className="relative rounded-xl border border-blue-500/30 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-5">
                {/* Header with Dallas orb */}
                <div className="flex items-start gap-4">
                    {/* Dallas Orb */}
                    <div className="relative flex-shrink-0">
                        <motion.div
                            animate={{
                                boxShadow: [
                                    '0 0 20px rgba(59, 130, 246, 0.5)',
                                    '0 0 40px rgba(147, 51, 234, 0.5)',
                                    '0 0 20px rgba(59, 130, 246, 0.5)',
                                ],
                            }}
                            transition={{ duration: 3, repeat: Infinity }}
                            className="w-14 h-14 rounded-full bg-gradient-to-br from-gray-200 via-white to-gray-300 flex items-center justify-center"
                        >
                            <Wand2 className="w-7 h-7 text-blue-600" />
                        </motion.div>
                        {/* Floating particles */}
                        {[...Array(3)].map((_, i) => (
                            <motion.div
                                key={i}
                                animate={{
                                    y: [-5, -15, -5],
                                    x: [0, (i - 1) * 8, 0],
                                    opacity: [0.3, 0.8, 0.3],
                                }}
                                transition={{
                                    duration: 2,
                                    delay: i * 0.3,
                                    repeat: Infinity,
                                }}
                                className="absolute w-1.5 h-1.5 rounded-full bg-blue-400"
                                style={{ top: '10%', left: `${30 + i * 20}%` }}
                            />
                        ))}
                    </div>

                    <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2 mb-2">
                            <span className="text-lg font-semibold bg-gradient-to-r from-gray-200 to-white bg-clip-text text-transparent">
                                Dallas
                            </span>
                            <span className="text-xs text-blue-400 font-medium px-2 py-0.5 bg-blue-500/10 rounded-full">
                                Learning Guide
                            </span>
                        </div>

                        <p className="text-sm text-gray-400 italic mb-3">
                            &ldquo;{quote}&rdquo;
                        </p>

                        {/* Learner Card */}
                        <div className="bg-slate-800/80 rounded-lg p-4 border border-slate-700/50">
                            <div className="flex items-center gap-2 mb-2">
                                <BookOpen className="w-4 h-4 text-blue-400" />
                                <span className="text-sm font-medium text-blue-300">Let&apos;s read the learner card together</span>
                            </div>

                            <div className="space-y-3">
                                <div>
                                    <span className="text-xs text-gray-500 uppercase tracking-wide">Correct Answer:</span>
                                    <p className="text-sm text-green-400 font-medium mt-0.5">{correctAnswer}</p>
                                </div>

                                <div>
                                    <span className="text-xs text-gray-500 uppercase tracking-wide">Explanation:</span>
                                    <p className="text-sm text-gray-300 mt-0.5 leading-relaxed">{explanation}</p>
                                </div>
                            </div>
                        </div>

                        <motion.button
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            onClick={onDismiss}
                            className="mt-4 w-full py-2.5 rounded-lg bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-medium text-sm transition-all flex items-center justify-center gap-2"
                        >
                            <Sparkles className="w-4 h-4" />
                            I understand now, continue learning
                        </motion.button>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   TYPES
   ============================================================================ */

export interface QuizOption {
    text: string
    isCorrect: boolean
    feedback?: string
}

export interface QuizBlockProps {
    blockId: string
    question: string
    options: QuizOption[]
    explanation: string
    xpBonus?: number
    answered?: {
        selectedOption: number
        isCorrect: boolean
    }
    onAnswer: (blockId: string, optionIndex: number) => void
    className?: string
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function QuizBlock({
    blockId,
    question,
    options,
    explanation,
    xpBonus = 5,
    answered,
    onAnswer,
    className,
}: QuizBlockProps) {
    const [selectedOption, setSelectedOption] = useState<number | null>(
        answered?.selectedOption ?? null
    )
    const [hasSubmitted, setHasSubmitted] = useState(!!answered)
    const [isCorrect, setIsCorrect] = useState(answered?.isCorrect ?? false)
    const [attemptCount, setAttemptCount] = useState(0)
    const [showConfetti, setShowConfetti] = useState(false)
    const [showDallas, setShowDallas] = useState(false)
    const [canRetry, setCanRetry] = useState(false)
    const [shakeWrong, setShakeWrong] = useState(false)

    const correctOption = options.find(o => o.isCorrect)
    const correctAnswerText = correctOption?.text || ""

    const handleConfettiComplete = useCallback(() => {
        setShowConfetti(false)
    }, [])

    const handleSubmit = () => {
        if (selectedOption === null || (hasSubmitted && !canRetry)) return

        const option = options[selectedOption]
        const correct = option.isCorrect
        const newAttemptCount = attemptCount + 1

        setAttemptCount(newAttemptCount)
        setIsCorrect(correct)

        if (correct) {
            // 🎊 EPIC CONFETTI CELEBRATION!
            setShowConfetti(true)
            setHasSubmitted(true)
            setCanRetry(false)
            onAnswer(blockId, selectedOption)
        } else {
            // Wrong answer
            setShakeWrong(true)
            setTimeout(() => setShakeWrong(false), 500)

            if (newAttemptCount === 1) {
                // First wrong - allow retry
                setCanRetry(true)
                setSelectedOption(null)
            } else {
                // Second wrong - Dallas steps in
                setHasSubmitted(true)
                setCanRetry(false)
                setShowDallas(true)
                onAnswer(blockId, selectedOption)
            }
        }
    }

    const handleRetry = () => {
        setCanRetry(false)
        setSelectedOption(null)
    }

    const handleDallasDismiss = () => {
        setShowDallas(false)
    }

    return (
        <div className={cn(
            "rounded-xl overflow-hidden border my-4 relative",
            hasSubmitted
                ? isCorrect
                    ? "border-green-500/50 bg-green-500/5"
                    : "border-red-500/50 bg-red-500/5"
                : canRetry
                    ? "border-amber-500/50 bg-amber-500/5"
                    : "border-neutral-800 bg-neutral-900/50",
            className
        )}>
            {/* 🎊 EPIC CONFETTI EXPLOSION */}
            <AnimatePresence>
                {showConfetti && <ConfettiExplosion onComplete={handleConfettiComplete} />}
            </AnimatePresence>

            {/* Header */}
            <motion.div
                animate={shakeWrong ? { x: [-10, 10, -10, 10, 0] } : {}}
                transition={{ duration: 0.4 }}
                className={cn(
                    "flex items-center gap-3 px-4 py-3 border-b",
                    hasSubmitted
                        ? isCorrect
                            ? "bg-green-500/10 border-green-500/30"
                            : "bg-red-500/10 border-red-500/30"
                        : canRetry
                            ? "bg-amber-500/10 border-amber-500/30"
                            : "bg-neutral-800/50 border-neutral-800"
                )}>
                <div className={cn(
                    "p-2 rounded-lg",
                    hasSubmitted
                        ? isCorrect
                            ? "bg-green-500/20"
                            : "bg-red-500/20"
                        : canRetry
                            ? "bg-amber-500/20"
                            : "bg-primary-500/20"
                )}>
                    {hasSubmitted ? (
                        isCorrect ? (
                            <motion.div
                                initial={{ scale: 0, rotate: -180 }}
                                animate={{ scale: 1, rotate: 0 }}
                                transition={{ type: "spring", stiffness: 200, damping: 15 }}
                            >
                                <CheckCircle2 className="h-5 w-5 text-green-400" />
                            </motion.div>
                        ) : (
                            <XCircle className="h-5 w-5 text-red-400" />
                        )
                    ) : canRetry ? (
                        <RotateCcw className="h-5 w-5 text-amber-400" />
                    ) : (
                        <HelpCircle className="h-5 w-5 text-primary-400" />
                    )}
                </div>
                <div className="flex-1">
                    <span className="text-xs font-medium text-neutral-400 uppercase tracking-wide">
                        {canRetry ? "Try Again - 1 more chance!" : "Quiz Question"}
                    </span>
                    {xpBonus > 0 && !hasSubmitted && !canRetry && (
                        <span className="ml-2 text-xs text-yellow-400">
                            +{xpBonus} XP
                        </span>
                    )}
                    {canRetry && (
                        <span className="ml-2 text-xs text-amber-400">
                            Hint: Think carefully!
                        </span>
                    )}
                </div>
                {hasSubmitted && isCorrect && xpBonus > 0 && (
                    <motion.div
                        initial={{ scale: 0, y: -20 }}
                        animate={{ scale: 1, y: 0 }}
                        transition={{ type: "spring", delay: 0.3 }}
                        className="flex items-center gap-1 px-3 py-1.5 bg-yellow-500/20 rounded-lg border border-yellow-500/30"
                    >
                        <Sparkles className="h-4 w-4 text-yellow-400" />
                        <span className="text-sm font-bold text-yellow-400">+{xpBonus} XP!</span>
                    </motion.div>
                )}
            </motion.div>

            {/* Question */}
            <div className="px-4 py-4">
                <p className="text-lg font-medium text-white mb-4">
                    {question}
                </p>

                {/* Options */}
                <div className="space-y-2">
                    {options.map((option, index) => {
                        const isSelected = selectedOption === index
                        const showResult = hasSubmitted && !showDallas

                        return (
                            <motion.label
                                key={index}
                                whileHover={!hasSubmitted && !canRetry ? { scale: 1.01 } : {}}
                                whileTap={!hasSubmitted ? { scale: 0.99 } : {}}
                                className={cn(
                                    "flex items-start gap-3 p-3 rounded-lg cursor-pointer transition-all",
                                    hasSubmitted && "cursor-default",
                                    !hasSubmitted && isSelected && "bg-primary-500/20 border border-primary-500/50",
                                    !hasSubmitted && !isSelected && "bg-neutral-800/50 border border-transparent hover:bg-neutral-800",
                                    showResult && option.isCorrect && "bg-green-500/20 border border-green-500/50",
                                    showResult && isSelected && !option.isCorrect && "bg-red-500/20 border border-red-500/50",
                                    showResult && !isSelected && !option.isCorrect && "bg-neutral-800/30 border border-transparent opacity-60"
                                )}
                            >
                                <input
                                    type="radio"
                                    name={`quiz-${blockId}`}
                                    checked={isSelected}
                                    onChange={() => !hasSubmitted && setSelectedOption(index)}
                                    disabled={hasSubmitted}
                                    className="sr-only"
                                />
                                <div className={cn(
                                    "w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5 transition-all",
                                    !hasSubmitted && isSelected && "border-primary-500 bg-primary-500",
                                    !hasSubmitted && !isSelected && "border-neutral-600",
                                    showResult && option.isCorrect && "border-green-500 bg-green-500",
                                    showResult && isSelected && !option.isCorrect && "border-red-500 bg-red-500",
                                    showResult && !isSelected && !option.isCorrect && "border-neutral-700"
                                )}>
                                    {((isSelected && !hasSubmitted) || (showResult && option.isCorrect) || (showResult && isSelected)) && (
                                        <motion.div
                                            initial={{ scale: 0 }}
                                            animate={{ scale: 1 }}
                                            className="w-2 h-2 rounded-full bg-white"
                                        />
                                    )}
                                </div>
                                <div className="flex-1">
                                    <span className={cn(
                                        "text-sm",
                                        showResult && option.isCorrect && "text-green-300 font-medium",
                                        showResult && isSelected && !option.isCorrect && "text-red-300",
                                        !showResult && "text-neutral-200"
                                    )}>
                                        {option.text}
                                    </span>
                                    {showResult && isSelected && option.feedback && (
                                        <p className={cn(
                                            "text-xs mt-1",
                                            option.isCorrect ? "text-green-400" : "text-red-400"
                                        )}>
                                            {option.feedback}
                                        </p>
                                    )}
                                </div>
                                {showResult && option.isCorrect && (
                                    <motion.div
                                        initial={{ scale: 0 }}
                                        animate={{ scale: 1 }}
                                        transition={{ type: "spring", delay: 0.1 }}
                                    >
                                        <CheckCircle2 className="h-5 w-5 text-green-400 flex-shrink-0" />
                                    </motion.div>
                                )}
                                {showResult && isSelected && !option.isCorrect && (
                                    <XCircle className="h-5 w-5 text-red-400 flex-shrink-0" />
                                )}
                            </motion.label>
                        )
                    })}
                </div>

                {/* Submit Button */}
                {!hasSubmitted && (
                    <motion.button
                        whileHover={{ scale: selectedOption !== null ? 1.02 : 1 }}
                        whileTap={{ scale: selectedOption !== null ? 0.98 : 1 }}
                        onClick={handleSubmit}
                        disabled={selectedOption === null}
                        className={cn(
                            "mt-4 w-full py-2.5 rounded-lg font-medium transition-all",
                            selectedOption !== null
                                ? canRetry
                                    ? "bg-amber-600 hover:bg-amber-500 text-white"
                                    : "bg-primary-600 hover:bg-primary-500 text-white"
                                : "bg-neutral-800 text-neutral-500 cursor-not-allowed"
                        )}
                    >
                        {canRetry ? "Try Again" : "Submit Answer"}
                    </motion.button>
                )}

                {/* 🧙‍♂️ Dallas Wizard Helper */}
                <AnimatePresence>
                    {showDallas && (
                        <DallasHelper
                            explanation={explanation}
                            correctAnswer={correctAnswerText}
                            onDismiss={handleDallasDismiss}
                        />
                    )}
                </AnimatePresence>

                {/* Normal Explanation (only show if correct or after Dallas dismissed) */}
                {hasSubmitted && isCorrect && !showDallas && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.5 }}
                        className="mt-4 p-3 rounded-lg bg-green-500/10 border border-green-500/20"
                    >
                        <div className="flex items-center gap-2 mb-1">
                            <Sparkles className="w-4 h-4 text-green-400" />
                            <p className="text-sm font-medium text-green-300">
                                Excellent work!
                            </p>
                        </div>
                        <p className="text-sm text-neutral-400">
                            {explanation}
                        </p>
                    </motion.div>
                )}
            </div>
        </div>
    )
}

export default QuizBlock
