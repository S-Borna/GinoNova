"use client"

/**
 * ============================================================================
 * EXAM MODE TASK FEATURES — Confidence & Spaced Repetition för Tasks
 * ============================================================================
 * 
 * Komponenter som läggs till på tasksidan:
 * - Confidence meter
 * - Quick quiz för confidence check
 * - Spaced repetition indicator
 * - "Add to Review" knapp
 */

import { useState, useEffect } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { useExamMode } from "@/contexts/ExamModeContext"
import { DOE25_TASK_QUIZ, TaskQuizQuestion } from "@/data/doe25-task-quiz"
import {
    Target,
    TrendingUp,
    TrendingDown,
    CheckCircle2,
    XCircle,
    RotateCcw,
    Zap,
    Brain
} from "lucide-react"
import { Button } from "@/components/ui/button"

/* ============================================================================
   CONFIDENCE METER
   ============================================================================ */

interface ConfidenceMeterProps {
    taskId: string
}

export function ConfidenceMeter({ taskId }: ConfidenceMeterProps) {
    const { getConfidenceForTask, updateConfidence } = useExamMode()
    const confidence = getConfidenceForTask(taskId)

    const getColor = (conf: number) => {
        if (conf >= 80) return "emerald"
        if (conf >= 50) return "amber"
        return "red"
    }

    const color = getColor(confidence)
    const colorClasses = {
        emerald: "from-emerald-500 to-emerald-600",
        amber: "from-amber-500 to-amber-600",
        red: "from-red-500 to-red-600"
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-xl overflow-hidden",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border border-zinc-700/50",
                "p-4"
            )}
        >
            <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                    <Target className="w-4 h-4 text-zinc-400" />
                    <span className="text-sm font-medium text-zinc-300">Confidence</span>
                </div>
                <span className={cn(
                    "text-lg font-bold",
                    color === "emerald" && "text-emerald-400",
                    color === "amber" && "text-amber-400",
                    color === "red" && "text-red-400"
                )}>
                    {Math.round(confidence)}%
                </span>
            </div>

            <div className="h-2 rounded-full bg-zinc-800 overflow-hidden">
                <motion.div
                    className={cn("h-full bg-gradient-to-r", colorClasses[color])}
                    initial={{ width: 0 }}
                    animate={{ width: `${confidence}%` }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                />
            </div>

            {confidence < 70 && (
                <p className="text-xs text-zinc-500 mt-2">
                    💡 Fokusera på detta område för att öka din confidence
                </p>
            )}
        </motion.div>
    )
}

/* ============================================================================
   QUICK CONFIDENCE CHECK
   ============================================================================ */

interface QuickConfidenceCheckProps {
    taskId: string
}

export function QuickConfidenceCheck({ taskId }: QuickConfidenceCheckProps) {
    const { updateConfidence } = useExamMode()
    const [showQuiz, setShowQuiz] = useState(false)
    const [currentQuestion, setCurrentQuestion] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [score, setScore] = useState(0)
    const [questions, setQuestions] = useState<TaskQuizQuestion[]>([])

    // Load questions for this task
    useEffect(() => {
        const quizSet = DOE25_TASK_QUIZ.find(q => q.taskId === taskId)
        if (quizSet) {
            // Take 5 random questions
            const shuffled = [...quizSet.questions].sort(() => Math.random() - 0.5)
            setQuestions(shuffled.slice(0, 5))
        }
    }, [taskId])

    const handleStart = () => {
        setShowQuiz(true)
        setCurrentQuestion(0)
        setScore(0)
        setSelectedAnswer(null)
        setShowResult(false)
    }

    const handleAnswer = (index: number) => {
        if (showResult) return
        setSelectedAnswer(index)
    }

    const handleConfirm = () => {
        if (selectedAnswer === null) return

        const question = questions[currentQuestion]
        const isCorrect = selectedAnswer === question.correctIndex

        if (isCorrect) {
            setScore(prev => prev + 1)
        }

        setShowResult(true)
    }

    const handleNext = () => {
        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(prev => prev + 1)
            setSelectedAnswer(null)
            setShowResult(false)
        } else {
            // Finished - update confidence
            const percentage = (score / questions.length) * 100
            updateConfidence(taskId, percentage, score, questions.length)
            setShowQuiz(false)
        }
    }

    if (!showQuiz) {
        return (
            <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "rounded-xl overflow-hidden",
                    "bg-gradient-to-br from-purple-900/20 via-[#0d0d14] to-[#0a0a0f]",
                    "border border-purple-500/30",
                    "p-4"
                )}
            >
                <div className="flex items-center gap-2 mb-3">
                    <Brain className="w-4 h-4 text-purple-400" />
                    <span className="text-sm font-medium text-zinc-300">Quick Confidence Check</span>
                </div>
                <p className="text-xs text-zinc-400 mb-4">
                    Testa din förståelse med 5 snabba frågor
                </p>
                <Button
                    onClick={handleStart}
                    className="w-full bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
                >
                    <Zap className="w-4 h-4 mr-2" />
                    Starta Quiz
                </Button>
            </motion.div>
        )
    }

    if (questions.length === 0) {
        return (
            <div className="rounded-xl bg-zinc-900/50 border border-zinc-700/50 p-4 text-center">
                <p className="text-sm text-zinc-400">Inga frågor tillgängliga för denna task</p>
            </div>
        )
    }

    const question = questions[currentQuestion]
    const isLastQuestion = currentQuestion === questions.length - 1
    const isCorrect = selectedAnswer !== null && selectedAnswer === question.correctIndex

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className={cn(
                "rounded-xl overflow-hidden",
                "bg-gradient-to-br from-purple-900/20 via-[#0d0d14] to-[#0a0a0f]",
                "border border-purple-500/30",
                "p-4"
            )}
        >
            {/* Progress */}
            <div className="flex items-center justify-between mb-4">
                <span className="text-xs text-zinc-400">
                    Fråga {currentQuestion + 1} av {questions.length}
                </span>
                <span className="text-xs text-zinc-400">
                    Poäng: {score}/{currentQuestion + (showResult ? 1 : 0)}
                </span>
            </div>

            {/* Question */}
            <h3 className="text-sm font-medium text-white mb-4">
                {question.question}
            </h3>

            {/* Options */}
            <div className="space-y-2 mb-4">
                {question.options.map((option, index) => {
                    let buttonClass = "w-full text-left p-3 rounded-lg border transition-all"
                    
                    if (showResult) {
                        if (index === question.correctIndex) {
                            buttonClass += " bg-emerald-500/20 border-emerald-500/50 text-emerald-300"
                        } else if (index === selectedAnswer && index !== question.correctIndex) {
                            buttonClass += " bg-red-500/20 border-red-500/50 text-red-300"
                        } else {
                            buttonClass += " bg-zinc-800/50 border-zinc-700/50 text-zinc-400"
                        }
                    } else {
                        buttonClass += selectedAnswer === index
                            ? " bg-purple-500/20 border-purple-500/50 text-purple-300"
                            : " bg-zinc-800/50 border-zinc-700/50 text-zinc-300 hover:border-purple-500/30"
                    }

                    return (
                        <button
                            key={index}
                            onClick={() => handleAnswer(index)}
                            disabled={showResult}
                            className={buttonClass}
                        >
                            <div className="flex items-center gap-2">
                                <span className="font-medium">
                                    {String.fromCharCode(65 + index)})
                                </span>
                                <span>{option}</span>
                                {showResult && index === question.correctIndex && (
                                    <CheckCircle2 className="w-4 h-4 ml-auto text-emerald-400" />
                                )}
                                {showResult && index === selectedAnswer && index !== question.correctIndex && (
                                    <XCircle className="w-4 h-4 ml-auto text-red-400" />
                                )}
                            </div>
                        </button>
                    )
                })}
            </div>

            {/* Explanation */}
            {showResult && (
                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-4 p-3 rounded-lg bg-zinc-800/50 border border-zinc-700/50"
                >
                    <p className="text-xs text-zinc-300">{question.explanation}</p>
                </motion.div>
            )}

            {/* Actions */}
            <div className="flex gap-2">
                {!showResult ? (
                    <Button
                        onClick={handleConfirm}
                        disabled={selectedAnswer === null}
                        className="flex-1 bg-purple-600 hover:bg-purple-500"
                    >
                        Bekräfta
                    </Button>
                ) : (
                    <Button
                        onClick={handleNext}
                        className="flex-1 bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
                    >
                        {isLastQuestion ? "Avsluta" : "Nästa"}
                    </Button>
                )}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   SPACED REPETITION INDICATOR
   ============================================================================ */

interface SpacedRepetitionIndicatorProps {
    taskId: string
    cardId: string
    type: "flashcard" | "quiz"
}

export function SpacedRepetitionIndicator({ taskId, cardId, type }: SpacedRepetitionIndicatorProps) {
    const { state, updateSpacedRepetition } = useExamMode()
    const card = state.spacedRepetition[cardId]

    const handleReview = (difficulty: "again" | "hard" | "good" | "easy") => {
        updateSpacedRepetition(cardId, difficulty)
    }

    if (!card || !card.nextReview) {
        return (
            <div className="text-xs text-zinc-500">
                ⭐ Markera när du repeterar för spaced repetition
            </div>
        )
    }

    const now = new Date()
    const daysUntilReview = Math.ceil((card.nextReview.getTime() - now.getTime()) / (1000 * 60 * 60 * 24))

    if (daysUntilReview <= 0) {
        return (
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="flex items-center gap-2 p-2 rounded-lg bg-amber-500/20 border border-amber-500/30"
            >
                <Zap className="w-4 h-4 text-amber-400" />
                <span className="text-xs text-amber-300">
                    Dags att repetera! ({card.reviewCount} gånger repeterad)
                </span>
            </motion.div>
        )
    }

    return (
        <div className="text-xs text-zinc-500">
            Nästa review om {daysUntilReview} {daysUntilReview === 1 ? "dag" : "dagar"}
        </div>
    )
}

