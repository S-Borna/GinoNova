"use client"

/**
 * ============================================================================
 * MOCK EXAM SIMULATOR — Fullständig Tentasimulering
 * ============================================================================
 * 
 * Simulerar en riktig tenta med:
 * - Timer (3 timmar)
 * - Fullscreen-läge
 * - Ingen hints eller förklaringar under tentan
 * - Resultat och feedback efteråt
 */

import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { useExamMode } from "@/contexts/ExamModeContext"
import { DOE25_TASK_QUIZ, TaskQuizQuestion } from "@/data/doe25-task-quiz"
import { DOE25_MODULE } from "@/data/doe25-module"
import {
    Clock,
    CheckCircle2,
    XCircle,
    AlertTriangle,
    Play,
    Pause,
    RotateCcw,
    Trophy,
    BarChart3
} from "lucide-react"
import { Button } from "@/components/ui/button"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ExamState {
    questions: TaskQuizQuestion[]
    currentIndex: number
    answers: Record<number, number | null>
    startTime: Date | null
    endTime: Date | null
    isPaused: boolean
    timeRemaining: number // seconds
}

const EXAM_DURATION = 3 * 60 * 60 // 3 hours in seconds

/* ============================================================================
   TIMER COMPONENT
   ============================================================================ */

function ExamTimer({ timeRemaining, isPaused, onPause, onResume }: {
    timeRemaining: number
    isPaused: boolean
    onPause: () => void
    onResume: () => void
}) {
    const hours = Math.floor(timeRemaining / 3600)
    const minutes = Math.floor((timeRemaining % 3600) / 60)
    const seconds = timeRemaining % 60

    const isLowTime = timeRemaining < 30 * 60 // Less than 30 minutes

    return (
        <div className={cn(
            "flex items-center gap-3 px-4 py-2 rounded-xl",
            isLowTime ? "bg-red-500/20 border border-red-500/50" : "bg-zinc-900/50 border border-zinc-700/50"
        )}>
            <Clock className={cn("w-5 h-5", isLowTime ? "text-red-400" : "text-zinc-400")} />
            <span className={cn(
                "text-lg font-mono font-bold",
                isLowTime ? "text-red-400" : "text-white"
            )}>
                {String(hours).padStart(2, "0")}:
                {String(minutes).padStart(2, "0")}:
                {String(seconds).padStart(2, "0")}
            </span>
            {isPaused ? (
                <Button
                    onClick={onResume}
                    size="sm"
                    className="bg-emerald-600 hover:bg-emerald-500"
                >
                    <Play className="w-4 h-4 mr-1" />
                    Fortsätt
                </Button>
            ) : (
                <Button
                    onClick={onPause}
                    size="sm"
                    variant="outline"
                >
                    <Pause className="w-4 h-4 mr-1" />
                    Pausa
                </Button>
            )}
        </div>
    )
}

/* ============================================================================
   EXAM INTERFACE
   ============================================================================ */

function ExamInterface({ state, onAnswer, onSubmit }: {
    state: ExamState
    onAnswer: (questionIndex: number, answerIndex: number) => void
    onSubmit: () => void
}) {
    const question = state.questions[state.currentIndex]
    const selectedAnswer = state.answers[state.currentIndex]
    const answeredCount = Object.values(state.answers).filter(a => a !== null).length
    const totalQuestions = state.questions.length

    return (
        <div className="max-w-4xl mx-auto space-y-6">
            {/* Progress Bar */}
            <div className="space-y-2">
                <div className="flex items-center justify-between text-sm">
                    <span className="text-zinc-400">
                        Fråga {state.currentIndex + 1} av {totalQuestions}
                    </span>
                    <span className="text-zinc-400">
                        {answeredCount} / {totalQuestions} besvarade
                    </span>
                </div>
                <div className="h-2 rounded-full bg-zinc-800 overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-purple-500 to-purple-600 transition-all"
                        style={{ width: `${((state.currentIndex + 1) / totalQuestions) * 100}%` }}
                    />
                </div>
            </div>

            {/* Question */}
            <div className="bg-zinc-900/50 rounded-xl p-6 border border-zinc-700/50">
                <div className="flex items-center gap-2 mb-4">
                    <span className={cn(
                        "px-2 py-1 rounded text-xs font-bold",
                        question.difficulty === "G" ? "bg-emerald-500/20 text-emerald-400" : "bg-purple-500/20 text-purple-400"
                    )}>
                        {question.difficulty}
                    </span>
                    <span className="text-xs text-zinc-500">{question.category}</span>
                </div>
                <h2 className="text-xl font-bold text-white mb-6">
                    {question.question}
                </h2>

                {/* Options */}
                <div className="space-y-3">
                    {question.options.map((option, index) => {
                        const isSelected = selectedAnswer === index
                        return (
                            <button
                                key={index}
                                onClick={() => onAnswer(state.currentIndex, index)}
                                className={cn(
                                    "w-full text-left p-4 rounded-lg border transition-all",
                                    isSelected
                                        ? "bg-purple-500/20 border-purple-500/50 text-purple-300"
                                        : "bg-zinc-800/50 border-zinc-700/50 text-zinc-300 hover:border-purple-500/30"
                                )}
                            >
                                <div className="flex items-center gap-3">
                                    <div className={cn(
                                        "w-8 h-8 rounded-lg flex items-center justify-center font-bold",
                                        isSelected
                                            ? "bg-purple-500 text-white"
                                            : "bg-zinc-700 text-zinc-400"
                                    )}>
                                        {String.fromCharCode(65 + index)}
                                    </div>
                                    <span>{option}</span>
                                </div>
                            </button>
                        )
                    })}
                </div>
            </div>

            {/* Navigation */}
            <div className="flex items-center justify-between">
                <Button
                    onClick={() => {
                        if (state.currentIndex > 0) {
                            onAnswer(state.currentIndex - 1, state.answers[state.currentIndex - 1] || 0)
                        }
                    }}
                    disabled={state.currentIndex === 0}
                    variant="outline"
                >
                    ← Föregående
                </Button>

                <div className="flex gap-2">
                    {state.currentIndex < totalQuestions - 1 ? (
                        <Button
                            onClick={() => {
                                if (state.currentIndex < totalQuestions - 1) {
                                    onAnswer(state.currentIndex + 1, state.answers[state.currentIndex + 1] || 0)
                                }
                            }}
                            className="bg-purple-600 hover:bg-purple-500"
                        >
                            Nästa →
                        </Button>
                    ) : (
                        <Button
                            onClick={onSubmit}
                            className="bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400"
                        >
                            <Trophy className="w-4 h-4 mr-2" />
                            Lämna in tentan
                        </Button>
                    )}
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   RESULTS VIEW
   ============================================================================ */

function ResultsView({ state, onRestart }: {
    state: ExamState
    onRestart: () => void
}) {
    const correctAnswers = state.questions.reduce((count, q, index) => {
        return count + (state.answers[index] === q.correctIndex ? 1 : 0)
    }, 0)
    const totalQuestions = state.questions.length
    const percentage = Math.round((correctAnswers / totalQuestions) * 100)
    const passed = percentage >= 60 // 60% to pass

    const timeSpent = state.startTime && state.endTime
        ? Math.round((state.endTime.getTime() - state.startTime.getTime()) / 1000 / 60)
        : 0

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="max-w-4xl mx-auto space-y-6"
        >
            {/* Result Header */}
            <div className={cn(
                "text-center p-8 rounded-2xl",
                passed
                    ? "bg-gradient-to-br from-emerald-900/20 to-emerald-800/10 border border-emerald-500/30"
                    : "bg-gradient-to-br from-red-900/20 to-red-800/10 border border-red-500/30"
            )}>
                {passed ? (
                    <Trophy className="w-16 h-16 text-emerald-400 mx-auto mb-4" />
                ) : (
                    <AlertTriangle className="w-16 h-16 text-red-400 mx-auto mb-4" />
                )}
                <h2 className="text-3xl font-bold text-white mb-2">
                    {passed ? "Grattis! Du klarade tentan! 🎉" : "Du klarade inte tentan"}
                </h2>
                <div className="text-5xl font-black mb-2" style={{
                    background: passed
                        ? "linear-gradient(to right, #10b981, #34d399)"
                        : "linear-gradient(to right, #ef4444, #f87171)",
                    WebkitBackgroundClip: "text",
                    WebkitTextFillColor: "transparent"
                }}>
                    {percentage}%
                </div>
                <p className="text-zinc-400">
                    {correctAnswers} av {totalQuestions} rätt
                </p>
                <p className="text-sm text-zinc-500 mt-2">
                    Tid: {timeSpent} minuter
                </p>
            </div>

            {/* Detailed Results */}
            <div className="bg-zinc-900/50 rounded-xl p-6 border border-zinc-700/50">
                <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                    <BarChart3 className="w-5 h-5" />
                    Detaljerade Resultat
                </h3>
                <div className="space-y-3">
                    {state.questions.map((question, index) => {
                        const userAnswer = state.answers[index]
                        const isCorrect = userAnswer === question.correctIndex

                        return (
                            <div
                                key={index}
                                className={cn(
                                    "p-4 rounded-lg border",
                                    isCorrect
                                        ? "bg-emerald-500/10 border-emerald-500/30"
                                        : "bg-red-500/10 border-red-500/30"
                                )}
                            >
                                <div className="flex items-start gap-3 mb-2">
                                    {isCorrect ? (
                                        <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                                    ) : (
                                        <XCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
                                    )}
                                    <div className="flex-1">
                                        <p className="text-sm font-medium text-white mb-2">
                                            {question.question}
                                        </p>
                                        <div className="space-y-1">
                                            <p className="text-xs text-zinc-400">
                                                Ditt svar: {userAnswer !== null ? question.options[userAnswer] : "Inget svar"}
                                            </p>
                                            {!isCorrect && (
                                                <p className="text-xs text-emerald-300">
                                                    Rätt svar: {question.options[question.correctIndex]}
                                                </p>
                                            )}
                                            <p className="text-xs text-zinc-500 mt-2">
                                                {question.explanation}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>

            {/* Actions */}
            <div className="flex gap-3 justify-center">
                <Button
                    onClick={onRestart}
                    className="bg-purple-600 hover:bg-purple-500"
                >
                    <RotateCcw className="w-4 h-4 mr-2" />
                    Gör om tentan
                </Button>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function MockExamSimulator() {
    const { addStudySession } = useExamMode()
    const [examState, setExamState] = useState<ExamState | null>(null)
    const [isFullscreen, setIsFullscreen] = useState(false)
    const timerRef = useRef<NodeJS.Timeout | null>(null)

    // Load questions from all tasks
    const loadQuestions = () => {
        const allQuestions: TaskQuizQuestion[] = []
        DOE25_TASK_QUIZ.forEach(quizSet => {
            // Take 2-3 random questions from each task
            const shuffled = [...quizSet.questions].sort(() => Math.random() - 0.5)
            allQuestions.push(...shuffled.slice(0, Math.floor(Math.random() * 2) + 2))
        })
        // Shuffle all questions
        const finalQuestions = allQuestions.sort(() => Math.random() - 0.5).slice(0, 30) // 30 questions total

        return finalQuestions
    }

    const startExam = () => {
        const questions = loadQuestions()
        setExamState({
            questions,
            currentIndex: 0,
            answers: {},
            startTime: new Date(),
            endTime: null,
            isPaused: false,
            timeRemaining: EXAM_DURATION
        })
        setIsFullscreen(true)
        startTimer()
    }

    const startTimer = () => {
        if (timerRef.current) clearInterval(timerRef.current)
        timerRef.current = setInterval(() => {
            setExamState(prev => {
                if (!prev || prev.isPaused || prev.endTime) return prev
                if (prev.timeRemaining <= 0) {
                    submitExam()
                    return prev
                }
                return {
                    ...prev,
                    timeRemaining: prev.timeRemaining - 1
                }
            })
        }, 1000)
    }

    const submitExam = () => {
        if (!examState) return

        const correctAnswers = examState.questions.reduce((count, q, index) => {
            return count + (examState.answers[index] === q.correctIndex ? 1 : 0)
        }, 0)
        const percentage = (correctAnswers / examState.questions.length) * 100

        setExamState(prev => prev ? {
            ...prev,
            endTime: new Date(),
            isPaused: true
        } : null)

        if (timerRef.current) {
            clearInterval(timerRef.current)
        }

        // Save session
        addStudySession({
            taskIds: Array.from(new Set(examState.questions.map(q => {
                const quizSet = DOE25_TASK_QUIZ.find(qs => qs.questions.includes(q))
                return quizSet?.taskId || ""
            }))),
            duration: examState.startTime
                ? Math.round((new Date().getTime() - examState.startTime.getTime()) / 1000 / 60)
                : 0,
            mode: "mock-exam",
            score: percentage
        })
    }

    const handleAnswer = (questionIndex: number, answerIndex: number) => {
        setExamState(prev => prev ? {
            ...prev,
            answers: {
                ...prev.answers,
                [questionIndex]: answerIndex
            }
        } : null)
    }

    const handleNavigate = (newIndex: number) => {
        setExamState(prev => prev ? {
            ...prev,
            currentIndex: newIndex
        } : null)
    }

    if (!examState) {
        return (
            <div className="max-w-2xl mx-auto text-center p-8 rounded-2xl bg-zinc-900/50 border border-zinc-700/50">
                <Trophy className="w-16 h-16 text-purple-400 mx-auto mb-4" />
                <h2 className="text-2xl font-bold text-white mb-4">Mock Exam Simulator</h2>
                <p className="text-zinc-400 mb-6">
                    Simulera en riktig tenta med 30 frågor och 3 timmars tid.
                    Inga hints eller förklaringar under tentan.
                </p>
                <div className="space-y-4 mb-6 text-left">
                    <div className="flex items-center gap-3 p-3 rounded-lg bg-zinc-800/50">
                        <Clock className="w-5 h-5 text-purple-400" />
                        <div>
                            <p className="text-sm font-medium text-white">3 timmar på dig</p>
                            <p className="text-xs text-zinc-400">Timer räknar nedåt</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3 p-3 rounded-lg bg-zinc-800/50">
                        <AlertTriangle className="w-5 h-5 text-amber-400" />
                        <div>
                            <p className="text-sm font-medium text-white">Inga hints</p>
                            <p className="text-xs text-zinc-400">Inga förklaringar under tentan</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3 p-3 rounded-lg bg-zinc-800/50">
                        <BarChart3 className="w-5 h-5 text-emerald-400" />
                        <div>
                            <p className="text-sm font-medium text-white">Detaljerad feedback</p>
                            <p className="text-xs text-zinc-400">Efter tentan får du se alla svar</p>
                        </div>
                    </div>
                </div>
                <Button
                    onClick={startExam}
                    size="lg"
                    className="bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
                >
                    <Play className="w-5 h-5 mr-2" />
                    Starta Mock Exam
                </Button>
            </div>
        )
    }

    if (examState.endTime) {
        return (
            <div className={isFullscreen ? "fixed inset-0 bg-[#05050a] z-50 overflow-y-auto p-8" : ""}>
                <ResultsView
                    state={examState}
                    onRestart={() => {
                        setExamState(null)
                        setIsFullscreen(false)
                    }}
                />
            </div>
        )
    }

    return (
        <div className={cn(
            isFullscreen && "fixed inset-0 bg-[#05050a] z-50 overflow-y-auto"
        )}>
            <div className="max-w-7xl mx-auto p-8">
                {/* Timer Bar */}
                <div className="mb-6 flex items-center justify-between">
                    <ExamTimer
                        timeRemaining={examState.timeRemaining}
                        isPaused={examState.isPaused}
                        onPause={() => {
                            setExamState(prev => prev ? { ...prev, isPaused: true } : null)
                            if (timerRef.current) clearInterval(timerRef.current)
                        }}
                        onResume={() => {
                            setExamState(prev => prev ? { ...prev, isPaused: false } : null)
                            startTimer()
                        }}
                    />
                    {examState.timeRemaining < 60 && (
                        <div className="flex items-center gap-2 text-red-400">
                            <AlertTriangle className="w-5 h-5" />
                            <span className="text-sm font-medium">Lite tid kvar!</span>
                        </div>
                    )}
                </div>

                {/* Exam Interface */}
                <ExamInterface
                    state={examState}
                    onAnswer={handleAnswer}
                    onSubmit={submitExam}
                />
            </div>
        </div>
    )
}

