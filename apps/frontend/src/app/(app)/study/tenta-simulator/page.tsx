"use client"

/**
 * Tenta-Simulator - Exam Prep Mode
 * 
 * Combines quizzes and flashcards in a timed exam-like environment
 * Features:
 * - Timed sessions (60, 75, 90, 120 min)
 * - Random questions from all tasks
 * - Mix of G and VG difficulty
 * - Live grading OR grading at end
 * - Progress tracking and scoring
 * - Review mode at the end
 */

import * as React from "react"
import { useState, useEffect, useMemo, useCallback } from "react"
import { useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import { 
    ArrowLeft, ArrowRight, Clock, CheckCircle, XCircle, 
    Trophy, Brain, RotateCcw, Play, Pause, Target, 
    Zap, Award, BookOpen, AlertTriangle
} from "lucide-react"

// Import quiz data
import { DOE25_TASK_QUIZ, type TaskQuizQuestion } from "@/data/doe25-task-quiz"

interface SimulatorSettings {
    duration: number // minutes
    questionCount: number
    includeG: boolean
    includeVG: boolean
    showTimer: boolean
    gradingMode: 'live' | 'end' // NEW: live = immediate feedback, end = feedback after completion
}

interface QuizResult {
    questionId: string
    correct: boolean
    selectedIndex: number
    correctIndex: number
    timeSpent: number
}

type SimulatorPhase = 'setup' | 'quiz' | 'review' | 'results'

const DEFAULT_SETTINGS: SimulatorSettings = {
    duration: 90,
    questionCount: 200,
    includeG: true,
    includeVG: true,
    showTimer: true,
    gradingMode: 'live'
}

// Shuffle array helper
function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

export default function TentaSimulatorPage() {
    // URL params
    const searchParams = useSearchParams()
    
    // State
    const [phase, setPhase] = useState<SimulatorPhase>('setup')
    const [settings, setSettings] = useState<SimulatorSettings>(DEFAULT_SETTINGS)
    const [questions, setQuestions] = useState<TaskQuizQuestion[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [results, setResults] = useState<QuizResult[]>([])
    const [timeRemaining, setTimeRemaining] = useState(0)
    const [questionStartTime, setQuestionStartTime] = useState(0)
    const [isPaused, setIsPaused] = useState(false)
    const [showLiveFeedback, setShowLiveFeedback] = useState(false)
    const [hasAutoStarted, setHasAutoStarted] = useState(false)

    // Get all questions from DOE25
    const allQuestions = useMemo(() => {
        return DOE25_TASK_QUIZ.flatMap(set => set.questions)
    }, [])

    // Parse URL params and auto-start if params provided
    useEffect(() => {
        if (hasAutoStarted) return
        
        const timeParam = searchParams?.get('time')
        const countParam = searchParams?.get('count')
        const gradingParam = searchParams?.get('grading')
        
        if (timeParam || countParam || gradingParam) {
            const newSettings: SimulatorSettings = {
                ...DEFAULT_SETTINGS,
                duration: timeParam ? parseInt(timeParam) : DEFAULT_SETTINGS.duration,
                questionCount: countParam ? (parseInt(countParam) === 999 ? 9999 : parseInt(countParam)) : DEFAULT_SETTINGS.questionCount,
                gradingMode: (gradingParam === 'end' ? 'end' : 'live') as 'live' | 'end'
            }
            setSettings(newSettings)
            setHasAutoStarted(true)
            
            // Auto-start the quiz
            setTimeout(() => {
                let filtered = allQuestions.filter(q => {
                    if (newSettings.includeG && q.difficulty === 'G') return true
                    if (newSettings.includeVG && q.difficulty === 'VG') return true
                    return false
                })
                const shuffled = shuffleArray(filtered)
                const prepared = shuffled.slice(0, newSettings.questionCount)
                
                setQuestions(prepared)
                setCurrentIndex(0)
                setSelectedAnswer(null)
                setResults([])
                setTimeRemaining(newSettings.duration * 60)
                setQuestionStartTime(Date.now())
                setPhase('quiz')
            }, 100)
        }
    }, [searchParams, hasAutoStarted, allQuestions])

    // Filter and prepare questions based on settings
    const prepareQuestions = useCallback(() => {
        let filtered = allQuestions.filter(q => {
            if (settings.includeG && q.difficulty === 'G') return true
            if (settings.includeVG && q.difficulty === 'VG') return true
            return false
        })

        // Shuffle and take requested count
        const shuffled = shuffleArray(filtered)
        return shuffled.slice(0, settings.questionCount)
    }, [allQuestions, settings])

    // Timer effect
    useEffect(() => {
        if (phase !== 'quiz' || isPaused || timeRemaining <= 0) return

        const timer = setInterval(() => {
            setTimeRemaining(prev => {
                if (prev <= 1) {
                    // Time's up - go to results
                    setPhase('results')
                    return 0
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(timer)
    }, [phase, isPaused, timeRemaining])

    // Format time
    const formatTime = (seconds: number) => {
        const mins = Math.floor(seconds / 60)
        const secs = seconds % 60
        return `${mins}:${secs.toString().padStart(2, '0')}`
    }

    // Start simulator
    const startSimulator = () => {
        const prepared = prepareQuestions()
        setQuestions(prepared)
        setCurrentIndex(0)
        setSelectedAnswer(null)
        setResults([])
        setTimeRemaining(settings.duration * 60)
        setQuestionStartTime(Date.now())
        setPhase('quiz')
    }

    // Submit answer
    const submitAnswer = () => {
        if (selectedAnswer === null) return

        const currentQuestion = questions[currentIndex]
        const timeSpent = Math.floor((Date.now() - questionStartTime) / 1000)
        
        const result: QuizResult = {
            questionId: currentQuestion.id,
            correct: selectedAnswer === currentQuestion.correctIndex,
            selectedIndex: selectedAnswer,
            correctIndex: currentQuestion.correctIndex,
            timeSpent
        }

        setResults(prev => [...prev, result])

        // If live grading, show feedback before moving to next
        if (settings.gradingMode === 'live') {
            setShowLiveFeedback(true)
        } else {
            // End grading - move to next question immediately
            moveToNextQuestion()
        }
    }

    // Move to next question (called after live feedback or directly in end mode)
    const moveToNextQuestion = () => {
        setShowLiveFeedback(false)
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswer(null)
            setQuestionStartTime(Date.now())
        } else {
            setPhase('results')
        }
    }

    // Calculate results
    const score = useMemo(() => {
        const correct = results.filter(r => r.correct).length
        const total = results.length
        const percentage = total > 0 ? Math.round((correct / total) * 100) : 0
        return { correct, total, percentage }
    }, [results])

    // Get grade based on percentage
    const getGrade = (percentage: number) => {
        if (percentage >= 90) return { grade: 'VG', color: 'text-emerald-400', message: 'Utmärkt! Du är redo för tentan! 🏆' }
        if (percentage >= 75) return { grade: 'G+', color: 'text-green-400', message: 'Bra jobbat! Du har goda chanser.' }
        if (percentage >= 60) return { grade: 'G', color: 'text-yellow-400', message: 'Godkänt! Men öva lite mer.' }
        if (percentage >= 50) return { grade: 'G-', color: 'text-orange-400', message: 'På gränsen. Repetera svaga områden.' }
        return { grade: 'U', color: 'text-red-400', message: 'Mer övning behövs. Du klarar det!' }
    }

    // Render setup phase
    const renderSetup = () => (
        <div className="max-w-2xl mx-auto">
            <div className="text-center mb-12">
                <div className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-purple-500/20 mb-6">
                    <Target className="w-10 h-10 text-purple-400" />
                </div>
                <h1 className="text-3xl font-bold text-white mb-3">Tenta-Simulator</h1>
                <p className="text-zinc-400">Simulera tentaförhållanden med tidspressad quiz</p>
            </div>

            {/* Settings */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-6 mb-8">
                <h2 className="text-lg font-semibold text-white mb-6 flex items-center gap-2">
                    <Zap className="w-5 h-5 text-yellow-400" />
                    Inställningar
                </h2>

                {/* Duration */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-3">Tidsgräns</label>
                    <div className="flex gap-3">
                        {[15, 30, 45, 60].map(mins => (
                            <button
                                key={mins}
                                onClick={() => setSettings(s => ({ ...s, duration: mins }))}
                                className={cn(
                                    "flex-1 py-3 px-4 rounded-xl border transition-all",
                                    settings.duration === mins
                                        ? "bg-purple-500/20 border-purple-500 text-purple-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-400 hover:border-zinc-600"
                                )}
                            >
                                {mins} min
                            </button>
                        ))}
                    </div>
                </div>

                {/* Question count */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-3">Antal frågor</label>
                    <div className="flex gap-3">
                        {[10, 25, 50, 100].map(count => (
                            <button
                                key={count}
                                onClick={() => setSettings(s => ({ ...s, questionCount: count }))}
                                className={cn(
                                    "flex-1 py-3 px-4 rounded-xl border transition-all",
                                    settings.questionCount === count
                                        ? "bg-purple-500/20 border-purple-500 text-purple-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-400 hover:border-zinc-600"
                                )}
                            >
                                {count}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Difficulty */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-3">Svårighetsgrad</label>
                    <div className="flex gap-3">
                        <button
                            onClick={() => setSettings(s => ({ ...s, includeG: !s.includeG }))}
                            className={cn(
                                "flex-1 py-3 px-4 rounded-xl border transition-all",
                                settings.includeG
                                    ? "bg-green-500/20 border-green-500 text-green-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500"
                            )}
                        >
                            G-nivå
                        </button>
                        <button
                            onClick={() => setSettings(s => ({ ...s, includeVG: !s.includeVG }))}
                            className={cn(
                                "flex-1 py-3 px-4 rounded-xl border transition-all",
                                settings.includeVG
                                    ? "bg-purple-500/20 border-purple-500 text-purple-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500"
                            )}
                        >
                            VG-nivå
                        </button>
                    </div>
                </div>

                {/* Timer toggle */}
                <div className="flex items-center justify-between py-3">
                    <span className="text-zinc-400">Visa timer</span>
                    <button
                        onClick={() => setSettings(s => ({ ...s, showTimer: !s.showTimer }))}
                        className={cn(
                            "w-12 h-6 rounded-full transition-all",
                            settings.showTimer ? "bg-purple-500" : "bg-zinc-700"
                        )}
                    >
                        <div className={cn(
                            "w-5 h-5 rounded-full bg-white transition-transform",
                            settings.showTimer ? "translate-x-6" : "translate-x-0.5"
                        )} />
                    </button>
                </div>
            </div>

            {/* Stats preview */}
            <div className="bg-zinc-900/30 border border-zinc-800 rounded-xl p-4 mb-8">
                <div className="flex items-center justify-between text-sm">
                    <span className="text-zinc-500">Tillgängliga frågor:</span>
                    <span className="text-zinc-300">{allQuestions.length} st</span>
                </div>
            </div>

            {/* Start button */}
            <button
                onClick={startSimulator}
                disabled={!settings.includeG && !settings.includeVG}
                className={cn(
                    "w-full py-4 rounded-xl font-semibold text-lg flex items-center justify-center gap-3 transition-all",
                    settings.includeG || settings.includeVG
                        ? "bg-gradient-to-r from-purple-500 to-pink-500 text-white hover:opacity-90"
                        : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                )}
            >
                <Play className="w-5 h-5" />
                Starta Tenta-Simulator
            </button>
        </div>
    )

    // Render quiz phase
    const renderQuiz = () => {
        const currentQuestion = questions[currentIndex]
        const progress = ((currentIndex + 1) / questions.length) * 100
        const lastResult = results[results.length - 1]
        const isCorrect = lastResult?.correct

        return (
            <div className="max-w-3xl mx-auto">
                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <div className="flex items-center gap-4">
                        <span className="text-zinc-400">
                            Fråga {currentIndex + 1} / {questions.length}
                        </span>
                        <span className={cn(
                            "px-2 py-1 rounded text-xs font-medium",
                            currentQuestion.difficulty === 'VG' 
                                ? "bg-purple-500/20 text-purple-300"
                                : "bg-green-500/20 text-green-300"
                        )}>
                            {currentQuestion.difficulty}
                        </span>
                        {/* Grading mode indicator */}
                        <span className={cn(
                            "px-2 py-1 rounded text-xs font-medium",
                            settings.gradingMode === 'live'
                                ? "bg-emerald-500/20 text-emerald-300"
                                : "bg-orange-500/20 text-orange-300"
                        )}>
                            {settings.gradingMode === 'live' ? '⚡ Live' : '📝 Efteråt'}
                        </span>
                    </div>

                    {settings.showTimer && (
                        <div className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-xl",
                            timeRemaining < 60 ? "bg-red-500/20 text-red-400" :
                            timeRemaining < 300 ? "bg-yellow-500/20 text-yellow-400" :
                            "bg-zinc-800 text-zinc-300"
                        )}>
                            <Clock className="w-4 h-4" />
                            <span className="font-mono font-semibold">{formatTime(timeRemaining)}</span>
                            <button
                                onClick={() => setIsPaused(!isPaused)}
                                className="ml-2 hover:opacity-70"
                            >
                                {isPaused ? <Play className="w-4 h-4" /> : <Pause className="w-4 h-4" />}
                            </button>
                        </div>
                    )}
                </div>

                {/* Progress bar */}
                <div className="h-1 bg-zinc-800 rounded-full mb-8 overflow-hidden">
                    <div 
                        className="h-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-300"
                        style={{ width: `${progress}%` }}
                    />
                </div>

                {/* Question */}
                <div className={cn(
                    "bg-zinc-900/50 border rounded-2xl p-8 mb-6 transition-all",
                    showLiveFeedback && isCorrect && "border-green-500/50 bg-green-500/5",
                    showLiveFeedback && !isCorrect && "border-red-500/50 bg-red-500/5",
                    !showLiveFeedback && "border-zinc-800"
                )}>
                    {currentQuestion.scenario && (
                        <div className="flex items-start gap-3 mb-4 p-4 bg-blue-500/10 border border-blue-500/20 rounded-xl">
                            <Brain className="w-5 h-5 text-blue-400 mt-0.5" />
                            <p className="text-blue-300 text-sm">{currentQuestion.scenario}</p>
                        </div>
                    )}
                    
                    <h2 className="text-xl font-semibold text-white leading-relaxed">
                        {currentQuestion.question}
                    </h2>
                </div>

                {/* Options */}
                <div className="space-y-3 mb-6">
                    {currentQuestion.options.map((option, idx) => {
                        const isSelected = selectedAnswer === idx
                        const isCorrectOption = idx === currentQuestion.correctIndex
                        const showAsCorrect = showLiveFeedback && isCorrectOption
                        const showAsWrong = showLiveFeedback && isSelected && !isCorrectOption

                        return (
                            <motion.button
                                key={idx}
                                onClick={() => !showLiveFeedback && setSelectedAnswer(idx)}
                                disabled={showLiveFeedback}
                                animate={showAsCorrect ? { scale: [1, 1.02, 1] } : showAsWrong ? { x: [0, -5, 5, 0] } : {}}
                                transition={{ duration: 0.3 }}
                                className={cn(
                                    "w-full text-left p-5 rounded-xl border transition-all",
                                    showAsCorrect && "bg-green-500/20 border-green-500 text-green-100",
                                    showAsWrong && "bg-red-500/20 border-red-500 text-red-100",
                                    !showLiveFeedback && isSelected && "bg-purple-500/20 border-purple-500 text-white",
                                    !showLiveFeedback && !isSelected && "bg-zinc-900/50 border-zinc-800 text-zinc-300 hover:border-zinc-700",
                                    showLiveFeedback && !showAsCorrect && !showAsWrong && "bg-zinc-900/50 border-zinc-800 text-zinc-500"
                                )}
                            >
                                <div className="flex items-center gap-4">
                                    <span className={cn(
                                        "w-8 h-8 rounded-full flex items-center justify-center font-semibold text-sm",
                                        showAsCorrect && "bg-green-500 text-white",
                                        showAsWrong && "bg-red-500 text-white",
                                        !showLiveFeedback && isSelected && "bg-purple-500 text-white",
                                        !showLiveFeedback && !isSelected && "bg-zinc-800 text-zinc-400",
                                        showLiveFeedback && !showAsCorrect && !showAsWrong && "bg-zinc-800 text-zinc-500"
                                    )}>
                                        {showAsCorrect ? <CheckCircle className="w-5 h-5" /> : 
                                         showAsWrong ? <XCircle className="w-5 h-5" /> : 
                                         String.fromCharCode(65 + idx)}
                                    </span>
                                    <span>{option}</span>
                                </div>
                            </motion.button>
                        )
                    })}
                </div>

                {/* Live feedback explanation */}
                <AnimatePresence>
                    {showLiveFeedback && (
                        <motion.div
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -10 }}
                            className={cn(
                                "mb-6 p-5 rounded-xl border",
                                isCorrect 
                                    ? "bg-green-500/10 border-green-500/30" 
                                    : "bg-red-500/10 border-red-500/30"
                            )}
                        >
                            <div className="flex items-start gap-3">
                                {isCorrect ? (
                                    <CheckCircle className="w-6 h-6 text-green-400 shrink-0" />
                                ) : (
                                    <XCircle className="w-6 h-6 text-red-400 shrink-0" />
                                )}
                                <div>
                                    <p className={cn(
                                        "font-bold mb-2",
                                        isCorrect ? "text-green-400" : "text-red-400"
                                    )}>
                                        {isCorrect ? "Rätt svar! 🎉" : "Fel svar"}
                                    </p>
                                    <p className="text-zinc-300 text-sm">
                                        {currentQuestion.explanation}
                                    </p>
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Submit / Next button */}
                {!showLiveFeedback ? (
                    <button
                        onClick={submitAnswer}
                        disabled={selectedAnswer === null}
                        className={cn(
                            "w-full py-4 rounded-xl font-semibold flex items-center justify-center gap-2 transition-all",
                            selectedAnswer !== null
                                ? "bg-gradient-to-r from-purple-500 to-pink-500 text-white hover:opacity-90"
                                : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                        )}
                    >
                        {settings.gradingMode === 'end' ? (
                            currentIndex < questions.length - 1 ? (
                                <>Nästa fråga <ArrowRight className="w-5 h-5" /></>
                            ) : (
                                <>Avsluta & visa resultat <CheckCircle className="w-5 h-5" /></>
                            )
                        ) : (
                            <>Svara <Zap className="w-5 h-5" /></>
                        )}
                    </button>
                ) : (
                    <motion.button
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        onClick={moveToNextQuestion}
                        className={cn(
                            "w-full py-4 rounded-xl font-semibold flex items-center justify-center gap-2",
                            isCorrect 
                                ? "bg-gradient-to-r from-green-500 to-emerald-500 text-white"
                                : "bg-gradient-to-r from-orange-500 to-red-500 text-white"
                        )}
                    >
                        {currentIndex < questions.length - 1 ? (
                            <>Nästa fråga <ArrowRight className="w-5 h-5" /></>
                        ) : (
                            <>Avsluta & visa resultat <Trophy className="w-5 h-5" /></>
                        )}
                    </motion.button>
                )}
            </div>
        )
    }

    // Render results phase
    const renderResults = () => {
        const gradeInfo = getGrade(score.percentage)
        
        // Group results by category
        const categoryStats = results.reduce((acc, result) => {
            const question = questions.find(q => q.id === result.questionId)
            if (!question) return acc
            
            const category = question.category || 'Övrigt'
            if (!acc[category]) {
                acc[category] = { correct: 0, total: 0 }
            }
            acc[category].total++
            if (result.correct) acc[category].correct++
            return acc
        }, {} as Record<string, { correct: number; total: number }>)

        return (
            <div className="max-w-3xl mx-auto">
                {/* Score card */}
                <div className="text-center mb-12">
                    <div className={cn(
                        "inline-flex items-center justify-center w-32 h-32 rounded-full mb-6",
                        score.percentage >= 60 ? "bg-green-500/20" : "bg-red-500/20"
                    )}>
                        <span className={cn("text-5xl font-bold", gradeInfo.color)}>
                            {gradeInfo.grade}
                        </span>
                    </div>
                    
                    <h1 className="text-3xl font-bold text-white mb-2">
                        {score.correct} av {score.total} rätt
                    </h1>
                    <p className="text-2xl text-zinc-400 mb-4">{score.percentage}%</p>
                    <p className={cn("text-lg", gradeInfo.color)}>{gradeInfo.message}</p>
                </div>

                {/* Stats */}
                <div className="grid grid-cols-3 gap-4 mb-8">
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4 text-center">
                        <CheckCircle className="w-6 h-6 text-green-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-green-400">{score.correct}</div>
                        <div className="text-sm text-zinc-500">Rätt</div>
                    </div>
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4 text-center">
                        <XCircle className="w-6 h-6 text-red-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-red-400">{score.total - score.correct}</div>
                        <div className="text-sm text-zinc-500">Fel</div>
                    </div>
                    <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4 text-center">
                        <Clock className="w-6 h-6 text-blue-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-blue-400">
                            {Math.round(results.reduce((a, r) => a + r.timeSpent, 0) / results.length)}s
                        </div>
                        <div className="text-sm text-zinc-500">Snitt/fråga</div>
                    </div>
                </div>

                {/* Category breakdown */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-6 mb-8">
                    <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                        <BookOpen className="w-5 h-5 text-purple-400" />
                        Resultat per kategori
                    </h2>
                    <div className="space-y-3">
                        {Object.entries(categoryStats)
                            .sort((a, b) => (a[1].correct / a[1].total) - (b[1].correct / b[1].total))
                            .map(([category, stats]) => {
                                const pct = Math.round((stats.correct / stats.total) * 100)
                                return (
                                    <div key={category} className="flex items-center gap-4">
                                        <span className="text-zinc-400 w-40 truncate">{category}</span>
                                        <div className="flex-1 h-2 bg-zinc-800 rounded-full overflow-hidden">
                                            <div 
                                                className={cn(
                                                    "h-full transition-all",
                                                    pct >= 75 ? "bg-green-500" :
                                                    pct >= 50 ? "bg-yellow-500" : "bg-red-500"
                                                )}
                                                style={{ width: `${pct}%` }}
                                            />
                                        </div>
                                        <span className="text-zinc-400 w-16 text-right">
                                            {stats.correct}/{stats.total}
                                        </span>
                                    </div>
                                )
                            })}
                    </div>
                </div>

                {/* Weak areas warning */}
                {Object.entries(categoryStats)
                    .filter(([, s]) => (s.correct / s.total) < 0.5)
                    .length > 0 && (
                    <div className="bg-orange-500/10 border border-orange-500/30 rounded-xl p-4 mb-8">
                        <div className="flex items-start gap-3">
                            <AlertTriangle className="w-5 h-5 text-orange-400 mt-0.5" />
                            <div>
                                <h3 className="font-semibold text-orange-300 mb-1">Fokusområden</h3>
                                <p className="text-orange-200/70 text-sm">
                                    Repetera: {Object.entries(categoryStats)
                                        .filter(([, s]) => (s.correct / s.total) < 0.5)
                                        .map(([cat]) => cat)
                                        .join(', ')}
                                </p>
                            </div>
                        </div>
                    </div>
                )}

                {/* Actions */}
                <div className="flex gap-4">
                    <button
                        onClick={() => setPhase('review')}
                        className="flex-1 py-4 rounded-xl border border-zinc-700 text-zinc-300 hover:border-zinc-600 flex items-center justify-center gap-2"
                    >
                        <BookOpen className="w-5 h-5" />
                        Granska svar
                    </button>
                    <button
                        onClick={() => setPhase('setup')}
                        className="flex-1 py-4 rounded-xl bg-gradient-to-r from-purple-500 to-pink-500 text-white flex items-center justify-center gap-2"
                    >
                        <RotateCcw className="w-5 h-5" />
                        Kör igen
                    </button>
                </div>
            </div>
        )
    }

    // Render review phase
    const renderReview = () => (
        <div className="max-w-3xl mx-auto">
            <div className="flex items-center justify-between mb-8">
                <h1 className="text-2xl font-bold text-white">Granska svar</h1>
                <button
                    onClick={() => setPhase('results')}
                    className="text-zinc-400 hover:text-white flex items-center gap-2"
                >
                    <ArrowLeft className="w-4 h-4" /> Tillbaka
                </button>
            </div>

            <div className="space-y-6">
                {results.map((result, idx) => {
                    const question = questions.find(q => q.id === result.questionId)
                    if (!question) return null

                    return (
                        <div 
                            key={result.questionId}
                            className={cn(
                                "bg-zinc-900/50 border rounded-xl p-6",
                                result.correct ? "border-green-500/30" : "border-red-500/30"
                            )}
                        >
                            <div className="flex items-start justify-between mb-4">
                                <span className="text-zinc-500">Fråga {idx + 1}</span>
                                {result.correct ? (
                                    <CheckCircle className="w-5 h-5 text-green-400" />
                                ) : (
                                    <XCircle className="w-5 h-5 text-red-400" />
                                )}
                            </div>

                            <p className="text-white font-medium mb-4">{question.question}</p>

                            <div className="space-y-2 mb-4">
                                {question.options.map((opt, optIdx) => (
                                    <div
                                        key={optIdx}
                                        className={cn(
                                            "p-3 rounded-lg text-sm",
                                            optIdx === question.correctIndex 
                                                ? "bg-green-500/20 text-green-300 border border-green-500/30"
                                                : optIdx === result.selectedIndex && !result.correct
                                                ? "bg-red-500/20 text-red-300 border border-red-500/30"
                                                : "bg-zinc-800/50 text-zinc-400"
                                        )}
                                    >
                                        <span className="font-semibold mr-2">{String.fromCharCode(65 + optIdx)}.</span>
                                        {opt}
                                        {optIdx === question.correctIndex && " ✓"}
                                    </div>
                                ))}
                            </div>

                            <div className="bg-zinc-800/50 rounded-lg p-3">
                                <p className="text-zinc-400 text-sm">{question.explanation}</p>
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            {/* Back link */}
            <div className="max-w-3xl mx-auto mb-8">
                <Link 
                    href="/study"
                    className="inline-flex items-center gap-2 text-zinc-400 hover:text-white transition-colors"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till Studyroom
                </Link>
            </div>

            {/* Render current phase */}
            {phase === 'setup' && renderSetup()}
            {phase === 'quiz' && renderQuiz()}
            {phase === 'results' && renderResults()}
            {phase === 'review' && renderReview()}
        </div>
    )
}

