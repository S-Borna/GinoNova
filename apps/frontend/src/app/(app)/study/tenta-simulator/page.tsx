"use client"

/**
 * Tenta-Simulator - Quiz Engine (INTE HUVUDSIDAN!)
 *
 * ⚠️ VIKTIGT: Detta är QUIZ-MOTORN, inte setup-sidan!
 * → Huvudsidan för val av inställningar är: /study/page.tsx (Studyroom)
 * → Vid ändringar av frågekällor: UPPDATERA study/page.tsx FÖRST!
 *
 * Denna sida:
 * - Tar emot inställningar via URL-params från Studyroom
 * - Kör själva quizzen med timer, frågor, resultat
 * - Har en backup setup-vy om man går hit direkt (utan params)
 *
 * Features:
 * - Timed sessions (60, 75, 90, 120 min)
 * - Random questions from DOE25 + Hands-On + Linux Commands + Tentaish
 * - Multi-select question sources
 * - Mix of G and VG difficulty
 * - Live grading OR grading at end
 * - Progress tracking and scoring
 * - Review mode at the end
 */

import * as React from "react"
import { useState, useEffect, useMemo, useCallback, useRef } from "react"
import { useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    ArrowLeft, ArrowRight, Clock, CheckCircle, XCircle,
    Trophy, Brain, RotateCcw, Play, Pause, Target,
    Zap, Award, BookOpen, AlertTriangle
} from "lucide-react"
import { getToken } from "@/lib/auth"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Import quiz data
import { DOE25_TASK_QUIZ, type TaskQuizQuestion } from "@/data/doe25-task-quiz"
import { HANDSON_MEGA_QUIZ, type MegaQuizQuestion } from "@/data/handson-mega-quiz"
import { ALL_LINUX_COMMAND_QUESTIONS, type LinuxCommandQuestion } from "@/data/linux-commands-quiz"
import { ALL_TENTAISH_QUESTIONS, type TentaishQuestion } from "@/data/tentaish-quiz"

// Unified question type for simulator (always has G/VG difficulty)
interface SimulatorQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    source: 'doe25' | 'handson' | 'linux-commands' | 'tentaish'
    scenario?: string // Optional scenario context
}

interface SimulatorSettings {
    duration: number // minutes
    questionCount: number
    includeG: boolean
    includeVG: boolean
    showTimer: boolean
    gradingMode: 'live' | 'end' // live = immediate feedback, end = feedback after completion
    selectedSources: ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[] // Multi-select question sources
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
    gradingMode: 'live',
    selectedSources: ['doe25'] // Default to DOE25 only for best exam prep
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

// Shuffle options within a question and update correctIndex
function shuffleQuestionOptions(question: SimulatorQuestion): SimulatorQuestion {
    // Create array of option objects with their original index
    const optionsWithIndex = question.options.map((option, index) => ({
        option,
        wasCorrect: index === question.correctIndex
    }))

    // Shuffle the options
    const shuffledOptions = shuffleArray(optionsWithIndex)

    // Find new correct index
    const newCorrectIndex = shuffledOptions.findIndex(o => o.wasCorrect) as 0 | 1 | 2 | 3

    return {
        ...question,
        options: shuffledOptions.map(o => o.option) as [string, string, string, string],
        correctIndex: newCorrectIndex
    }
}

// Convert DOE25 question to SimulatorQuestion
function convertDOE25Question(q: TaskQuizQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        explanation: q.explanation,
        difficulty: q.difficulty, // Already 'G' | 'VG'
        category: q.category,
        source: 'doe25',
        scenario: q.scenario // Include if present
    }
}

// Convert Hands-On question to SimulatorQuestion (map difficulty)
function convertHandsOnQuestion(q: MegaQuizQuestion): SimulatorQuestion {
    // Map: beginner/intermediate → G, advanced → VG
    const difficulty: 'G' | 'VG' = q.difficulty === 'advanced' ? 'VG' : 'G'

    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex as 0 | 1 | 2 | 3,
        explanation: q.explanation,
        difficulty,
        category: q.category,
        source: 'handson'
    }
}

// Convert Linux Commands question to SimulatorQuestion (map difficulty)
function convertLinuxCommandQuestion(q: LinuxCommandQuestion): SimulatorQuestion {
    // Map: beginner/intermediate → G, advanced → VG
    const difficulty: 'G' | 'VG' = q.difficulty === 'advanced' ? 'VG' : 'G'

    return {
        id: q.id,
        question: q.question,
        options: q.options as [string, string, string, string],
        correctIndex: q.correctIndex as 0 | 1 | 2 | 3,
        explanation: q.explanation,
        difficulty,
        category: q.category,
        source: 'linux-commands'
    }
}

// Convert Tentaish question to SimulatorQuestion
function convertTentaishQuestion(q: TentaishQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'tentaish',
        scenario: q.scenario
    }
}

export default function TentaSimulatorPage() {
    // URL params
    const searchParams = useSearchParams()

    // State
    const [phase, setPhase] = useState<SimulatorPhase>('setup')
    const [settings, setSettings] = useState<SimulatorSettings>(DEFAULT_SETTINGS)
    const [questions, setQuestions] = useState<SimulatorQuestion[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [results, setResults] = useState<QuizResult[]>([])
    const [timeRemaining, setTimeRemaining] = useState(0)
    const [questionStartTime, setQuestionStartTime] = useState(0)
    const [isPaused, setIsPaused] = useState(false)
    const [showLiveFeedback, setShowLiveFeedback] = useState(false)
    const [hasAutoStarted, setHasAutoStarted] = useState(false)
    const [showAbortModal, setShowAbortModal] = useState(false)
    const [examStartTime, setExamStartTime] = useState<Date | null>(null)
    const hasSubmittedResult = useRef(false)

    // Get DOE25 questions
    const doe25Questions = useMemo(() => {
        return DOE25_TASK_QUIZ.flatMap(set =>
            set.questions.map(convertDOE25Question)
        )
    }, [])

    // Get Hands-On questions
    const handsonQuestions = useMemo(() => {
        return HANDSON_MEGA_QUIZ.flatMap(set =>
            set.questions.map(convertHandsOnQuestion)
        )
    }, [])

    // Get Linux Commands questions
    const linuxCommandsQuestions = useMemo(() => {
        return ALL_LINUX_COMMAND_QUESTIONS.map(convertLinuxCommandQuestion)
    }, [])

    // Get Tentaish questions
    const tentaishQuestions = useMemo(() => {
        return ALL_TENTAISH_QUESTIONS.map(convertTentaishQuestion)
    }, [])

    // Get filtered questions based on selected sources
    const allQuestions = useMemo(() => {
        const questions: SimulatorQuestion[] = []
        if (settings.selectedSources.includes('doe25')) {
            questions.push(...doe25Questions)
        }
        if (settings.selectedSources.includes('handson')) {
            questions.push(...handsonQuestions)
        }
        if (settings.selectedSources.includes('linux-commands')) {
            questions.push(...linuxCommandsQuestions)
        }
        if (settings.selectedSources.includes('tentaish')) {
            questions.push(...tentaishQuestions)
        }
        return questions
    }, [doe25Questions, handsonQuestions, linuxCommandsQuestions, tentaishQuestions, settings.selectedSources])

    // Parse URL params and auto-start if params provided
    useEffect(() => {
        if (hasAutoStarted) return

        const timeParam = searchParams?.get('time')
        const countParam = searchParams?.get('count')
        const gradingParam = searchParams?.get('grading')
        const difficultyParam = searchParams?.get('difficulty')
        const sourceParam = searchParams?.get('source')

        if (timeParam || countParam || gradingParam || difficultyParam || sourceParam) {
            // Parse difficulty param: 'G', 'VG', or 'both'
            let includeG = true
            let includeVG = true
            if (difficultyParam === 'G') {
                includeG = true
                includeVG = false
            } else if (difficultyParam === 'VG') {
                includeG = false
                includeVG = true
            }

            // Parse source param (comma-separated for multi-select)
            let selectedSources: ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[] = ['doe25']
            if (sourceParam) {
                const sources = sourceParam.split(',') as ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[]
                selectedSources = sources.filter(s => ['doe25', 'handson', 'linux-commands', 'tentaish'].includes(s))
                if (selectedSources.length === 0) selectedSources = ['doe25']
            }

            const newSettings: SimulatorSettings = {
                ...DEFAULT_SETTINGS,
                duration: timeParam ? parseInt(timeParam) : DEFAULT_SETTINGS.duration,
                questionCount: countParam ? (parseInt(countParam) === 999 ? 9999 : parseInt(countParam)) : DEFAULT_SETTINGS.questionCount,
                gradingMode: (gradingParam === 'end' ? 'end' : 'live') as 'live' | 'end',
                includeG,
                includeVG,
                selectedSources
            }
            setSettings(newSettings)
            setHasAutoStarted(true)

            // Get questions based on selected sources
            let sourceQuestions: SimulatorQuestion[] = []
            if (selectedSources.includes('doe25')) sourceQuestions.push(...doe25Questions)
            if (selectedSources.includes('handson')) sourceQuestions.push(...handsonQuestions)
            if (selectedSources.includes('linux-commands')) sourceQuestions.push(...linuxCommandsQuestions)
            if (selectedSources.includes('tentaish')) sourceQuestions.push(...tentaishQuestions)

            // Auto-start the quiz
            setTimeout(() => {
                let filtered = sourceQuestions.filter(q => {
                    if (newSettings.includeG && q.difficulty === 'G') return true
                    if (newSettings.includeVG && q.difficulty === 'VG') return true
                    return false
                })
                const shuffled = shuffleArray(filtered)
                const sliced = shuffled.slice(0, newSettings.questionCount)
                // Shuffle options within each question for randomized answer positions
                const prepared = sliced.map(q => shuffleQuestionOptions(q))

                setQuestions(prepared)
                setCurrentIndex(0)
                setSelectedAnswer(null)
                setResults([])
                setTimeRemaining(newSettings.duration * 60)
                setQuestionStartTime(Date.now())
                setExamStartTime(new Date())
                hasSubmittedResult.current = false
                setPhase('quiz')
            }, 100)
        }
    }, [searchParams, hasAutoStarted, doe25Questions, handsonQuestions, linuxCommandsQuestions, tentaishQuestions])

    // Filter and prepare questions based on settings
    const prepareQuestions = useCallback(() => {
        let filtered = allQuestions.filter(q => {
            if (settings.includeG && q.difficulty === 'G') return true
            if (settings.includeVG && q.difficulty === 'VG') return true
            return false
        })

        // Shuffle questions and take requested count
        const shuffled = shuffleArray(filtered)
        const sliced = shuffled.slice(0, settings.questionCount)
        // Shuffle options within each question for randomized answer positions
        return sliced.map(q => shuffleQuestionOptions(q))
    }, [allQuestions, settings])

    // Save exam result to backend
    const saveExamResult = useCallback(async (
        finalResults: QuizResult[],
        examQuestions: SimulatorQuestion[],
        startTime: Date | null
    ) => {
        // Prevent duplicate submissions
        if (hasSubmittedResult.current) return
        hasSubmittedResult.current = true

        const token = getToken()
        if (!token || finalResults.length === 0) {
            console.warn('[ExamResult] Skipped: no token or no results')
            hasSubmittedResult.current = false // Allow retry if conditions change
            return
        }

        try {
            // Calculate G/VG stats
            const gStats = finalResults.reduce((acc, result) => {
                const question = examQuestions.find(q => q.id === result.questionId)
                if (!question || question.difficulty !== 'G') return acc
                acc.total++
                if (result.correct) acc.correct++
                return acc
            }, { correct: 0, total: 0 })

            const vgStats = finalResults.reduce((acc, result) => {
                const question = examQuestions.find(q => q.id === result.questionId)
                if (!question || question.difficulty !== 'VG') return acc
                acc.total++
                if (result.correct) acc.correct++
                return acc
            }, { correct: 0, total: 0 })

            const correctCount = finalResults.filter(r => r.correct).length
            const totalTime = finalResults.reduce((a, r) => a + r.timeSpent, 0)
            const scorePercent = Math.round((correctCount / finalResults.length) * 100)

            // FIXED: Include ALL required fields for backend
            const payload = {
                duration_minutes: settings.duration,
                question_count: examQuestions.length,
                sources: settings.selectedSources,
                include_g: settings.includeG,
                include_vg: settings.includeVG,
                grading_mode: settings.gradingMode,
                correct_answers: correctCount,
                wrong_answers: finalResults.filter(r => !r.correct).length,
                skipped_answers: examQuestions.length - finalResults.length,
                score_percent: scorePercent,
                g_correct: gStats.correct,
                g_total: gStats.total,
                vg_correct: vgStats.correct,
                vg_total: vgStats.total,
                time_spent_seconds: totalTime,
                started_at: startTime?.toISOString() || new Date().toISOString(),
                completed: true
            }

            console.log('[ExamResult] Submitting result...', { questionCount: payload.question_count, score: payload.score_percent })

            const response = await fetch(`${API_BASE_URL}/api/exam/submit`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })

            // FIXED: Actually check response status!
            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }))
                console.error('[ExamResult] Server error:', response.status, errorData)

                if (response.status === 401) {
                    console.error('[ExamResult] Auth token expired or invalid - result NOT saved!')
                    // Don't reset hasSubmittedResult - token won't magically become valid
                } else {
                    // For other errors, allow retry
                    hasSubmittedResult.current = false
                }
                return
            }

            const result = await response.json()
            console.log('[ExamResult] ✓ Saved successfully! ID:', result.id)
        } catch (err) {
            // Network error - allow retry
            hasSubmittedResult.current = false
            console.error('[ExamResult] Network error - will allow retry:', err)
        }
    }, [settings])

    // Timer effect
    useEffect(() => {
        if (phase !== 'quiz' || isPaused || timeRemaining <= 0) return

        const timer = setInterval(() => {
            setTimeRemaining(prev => {
                if (prev <= 1) {
                    // Time's up - save & go to results
                    saveExamResult(results, questions, examStartTime)
                    setPhase('results')
                    return 0
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(timer)
    }, [phase, isPaused, timeRemaining, results, questions, examStartTime, saveExamResult])

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
        setExamStartTime(new Date())
        hasSubmittedResult.current = false
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

        // Create the new results array INCLUDING current answer
        const newResults = [...results, result]
        setResults(newResults)

        // Check if this is the last question - AUTO-SAVE immediately!
        const isLastQuestion = currentIndex >= questions.length - 1

        if (isLastQuestion) {
            // LAST QUESTION: Auto-save with complete results and go to results phase
            console.log('[AutoSave] Last question answered - saving exam result automatically')
            saveExamResult(newResults, questions, examStartTime)

            // Show feedback briefly for live mode, then go to results
            if (settings.gradingMode === 'live') {
                setShowLiveFeedback(true)
                // Auto-transition to results after showing feedback
                setTimeout(() => {
                    setShowLiveFeedback(false)
                    setPhase('results')
                }, 1500)
            } else {
                setPhase('results')
            }
        } else {
            // Not last question - show feedback or move to next
            if (settings.gradingMode === 'live') {
                setShowLiveFeedback(true)
            } else {
                moveToNextQuestion()
            }
        }
    }

    // Move to next question (called after live feedback)
    const moveToNextQuestion = () => {
        setShowLiveFeedback(false)
        // Only move if not last question (last question handled in submitAnswer)
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswer(null)
            setQuestionStartTime(Date.now())
        }
    }

    // Abort exam and go to results
    const abortExam = () => {
        setShowAbortModal(false)
        setShowLiveFeedback(false)
        saveExamResult(results, questions, examStartTime)
        setPhase('results')
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

                {/* Difficulty - G/VG Selection */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-3">Betygsnivå</label>
                    <div className="grid grid-cols-3 gap-3">
                        <button
                            onClick={() => setSettings(s => ({ ...s, includeG: true, includeVG: false }))}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1",
                                settings.includeG && !settings.includeVG
                                    ? "bg-green-500/20 border-green-500 text-green-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            <span className="text-lg font-bold">G</span>
                            <span className="text-xs opacity-70">Godkänt</span>
                        </button>
                        <button
                            onClick={() => setSettings(s => ({ ...s, includeG: false, includeVG: true }))}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1",
                                !settings.includeG && settings.includeVG
                                    ? "bg-purple-500/20 border-purple-500 text-purple-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            <span className="text-lg font-bold">VG</span>
                            <span className="text-xs opacity-70">Väl Godkänt</span>
                        </button>
                        <button
                            onClick={() => setSettings(s => ({ ...s, includeG: true, includeVG: true }))}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1",
                                settings.includeG && settings.includeVG
                                    ? "bg-gradient-to-r from-green-500/20 to-purple-500/20 border-yellow-500 text-yellow-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            <span className="text-lg font-bold">G+VG</span>
                            <span className="text-xs opacity-70">Mixad</span>
                        </button>
                    </div>
                    <p className="text-xs text-zinc-500 mt-2">
                        {settings.includeG && !settings.includeVG && "Fokus på grundläggande förståelse för G-nivå"}
                        {!settings.includeG && settings.includeVG && "Avancerade frågor för högre betyg"}
                        {settings.includeG && settings.includeVG && "Blandade frågor för fullständig tentaförberedelse"}
                    </p>
                </div>

                {/* Question Source Selection - Multi-select */}
                <div className="mb-6">
                    <label className="block text-sm text-zinc-400 mb-3">Frågekälla (välj en eller flera)</label>
                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <button
                            onClick={() => setSettings(s => {
                                const sources = s.selectedSources.includes('doe25')
                                    ? s.selectedSources.filter(src => src !== 'doe25')
                                    : [...s.selectedSources, 'doe25'] as ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[]
                                return { ...s, selectedSources: sources.length > 0 ? sources : ['doe25'] }
                            })}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                settings.selectedSources.includes('doe25')
                                    ? "bg-purple-500/20 border-purple-500 text-purple-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            {settings.selectedSources.includes('doe25') && (
                                <div className="absolute top-2 right-2 w-4 h-4 bg-purple-500 rounded-full flex items-center justify-center">
                                    <CheckCircle className="w-3 h-3 text-white" />
                                </div>
                            )}
                            <span className="text-lg">🎓</span>
                            <span className="text-sm font-medium">DOE25</span>
                            <span className="text-xs opacity-70">{doe25Questions.length} frågor</span>
                        </button>
                        <button
                            onClick={() => setSettings(s => {
                                const sources = s.selectedSources.includes('handson')
                                    ? s.selectedSources.filter(src => src !== 'handson')
                                    : [...s.selectedSources, 'handson'] as ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[]
                                return { ...s, selectedSources: sources.length > 0 ? sources : ['handson'] }
                            })}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                settings.selectedSources.includes('handson')
                                    ? "bg-emerald-500/20 border-emerald-500 text-emerald-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            {settings.selectedSources.includes('handson') && (
                                <div className="absolute top-2 right-2 w-4 h-4 bg-emerald-500 rounded-full flex items-center justify-center">
                                    <CheckCircle className="w-3 h-3 text-white" />
                                </div>
                            )}
                            <span className="text-lg">🔧</span>
                            <span className="text-sm font-medium">Hands-On</span>
                            <span className="text-xs opacity-70">{handsonQuestions.length} frågor</span>
                        </button>
                        <button
                            onClick={() => setSettings(s => {
                                const sources = s.selectedSources.includes('linux-commands')
                                    ? s.selectedSources.filter(src => src !== 'linux-commands')
                                    : [...s.selectedSources, 'linux-commands'] as ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[]
                                return { ...s, selectedSources: sources.length > 0 ? sources : ['linux-commands'] }
                            })}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                settings.selectedSources.includes('linux-commands')
                                    ? "bg-orange-500/20 border-orange-500 text-orange-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            {settings.selectedSources.includes('linux-commands') && (
                                <div className="absolute top-2 right-2 w-4 h-4 bg-orange-500 rounded-full flex items-center justify-center">
                                    <CheckCircle className="w-3 h-3 text-white" />
                                </div>
                            )}
                            <span className="text-lg">💻</span>
                            <span className="text-sm font-medium">Linux Kommandon</span>
                            <span className="text-xs opacity-70">{linuxCommandsQuestions.length} frågor</span>
                        </button>
                        <button
                            onClick={() => setSettings(s => {
                                const sources = s.selectedSources.includes('tentaish')
                                    ? s.selectedSources.filter(src => src !== 'tentaish')
                                    : [...s.selectedSources, 'tentaish'] as ('doe25' | 'handson' | 'linux-commands' | 'tentaish')[]
                                return { ...s, selectedSources: sources.length > 0 ? sources : ['tentaish'] }
                            })}
                            className={cn(
                                "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                settings.selectedSources.includes('tentaish')
                                    ? "bg-cyan-500/20 border-cyan-500 text-cyan-300"
                                    : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                            )}
                        >
                            {settings.selectedSources.includes('tentaish') && (
                                <div className="absolute top-2 right-2 w-4 h-4 bg-cyan-500 rounded-full flex items-center justify-center">
                                    <CheckCircle className="w-3 h-3 text-white" />
                                </div>
                            )}
                            <span className="text-lg">📝</span>
                            <span className="text-sm font-medium">Tentaish</span>
                            <span className="text-xs opacity-70">{tentaishQuestions.length} frågor</span>
                        </button>
                    </div>
                    <p className="text-xs text-zinc-500 mt-2">
                        {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'doe25' && "✨ Rekommenderat för tentan - fokuserade tentafrågor"}
                        {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'handson' && "Praktiska frågor från Hands-On modulen"}
                        {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'linux-commands' && "🔥 Terminal-kommandon: cd, ls, grep, docker, LVM & mer"}
                        {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'tentaish' && "📝 Tentaish - komplett tentaöversikt: filsystem, användare, SSH, Docker, disk & nätverk"}
                        {settings.selectedSources.length > 1 && `Kombinerat: ${settings.selectedSources.length} källor valda (${allQuestions.length} frågor)`}
                    </p>
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

            {/* Stats preview - Show available questions per level */}
            <div className="bg-zinc-900/30 border border-zinc-800 rounded-xl p-4 mb-8">
                <div className="flex items-center justify-between text-sm mb-2">
                    <span className="text-zinc-500">Tillgängliga frågor:</span>
                    <span className="text-zinc-300">
                        {allQuestions.filter(q =>
                            (settings.includeG && q.difficulty === 'G') ||
                            (settings.includeVG && q.difficulty === 'VG')
                        ).length} st
                    </span>
                </div>
                <div className="flex gap-4 text-xs">
                    <span className="text-green-400">
                        G: {allQuestions.filter(q => q.difficulty === 'G').length}
                    </span>
                    <span className="text-purple-400">
                        VG: {allQuestions.filter(q => q.difficulty === 'VG').length}
                    </span>
                    <span className="text-zinc-500 ml-auto">
                        Källa: {settings.selectedSources.map(s => s === 'doe25' ? '🎓' : s === 'handson' ? '🔧' : s === 'tentaish' ? '📝' : '💻').join(' ')}
                    </span>
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
                {/* Abort confirmation modal */}
                <AnimatePresence>
                    {showAbortModal && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4"
                            onClick={() => setShowAbortModal(false)}
                        >
                            <motion.div
                                initial={{ scale: 0.9, opacity: 0 }}
                                animate={{ scale: 1, opacity: 1 }}
                                exit={{ scale: 0.9, opacity: 0 }}
                                onClick={(e) => e.stopPropagation()}
                                className="bg-zinc-900 border border-zinc-700 rounded-2xl p-6 max-w-md w-full"
                            >
                                <div className="flex items-center gap-3 mb-4">
                                    <div className="w-12 h-12 rounded-full bg-orange-500/20 flex items-center justify-center">
                                        <AlertTriangle className="w-6 h-6 text-orange-400" />
                                    </div>
                                    <div>
                                        <h3 className="text-lg font-bold text-white">Avbryt provet?</h3>
                                        <p className="text-sm text-zinc-400">Du har svarat på {results.length} av {questions.length} frågor</p>
                                    </div>
                                </div>
                                <p className="text-zinc-300 mb-6">
                                    Är du säker på att du vill avbryta? Dina {results.length} besvarade frågor kommer att rättas och du får se ditt resultat.
                                </p>
                                <div className="flex gap-3">
                                    <button
                                        onClick={() => setShowAbortModal(false)}
                                        className="flex-1 py-3 px-4 rounded-xl border border-zinc-700 text-zinc-300 hover:bg-zinc-800 transition-all"
                                    >
                                        Fortsätt provet
                                    </button>
                                    <button
                                        onClick={abortExam}
                                        className="flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold hover:opacity-90 transition-all"
                                    >
                                        Avbryt & rätta
                                    </button>
                                </div>
                            </motion.div>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <div className="flex items-center gap-4">
                        <button
                            onClick={() => setShowAbortModal(true)}
                            className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white transition-all text-sm"
                        >
                            <XCircle className="w-4 h-4" />
                            Avbryt
                        </button>
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

        // Calculate G/VG stats
        const gStats = results.reduce((acc, result) => {
            const question = questions.find(q => q.id === result.questionId)
            if (!question || question.difficulty !== 'G') return acc
            acc.total++
            if (result.correct) acc.correct++
            return acc
        }, { correct: 0, total: 0 })

        const vgStats = results.reduce((acc, result) => {
            const question = questions.find(q => q.id === result.questionId)
            if (!question || question.difficulty !== 'VG') return acc
            acc.total++
            if (result.correct) acc.correct++
            return acc
        }, { correct: 0, total: 0 })

        const gPercentage = gStats.total > 0 ? Math.round((gStats.correct / gStats.total) * 100) : 0
        const vgPercentage = vgStats.total > 0 ? Math.round((vgStats.correct / vgStats.total) * 100) : 0

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

                {/* G/VG Stats - NEW */}
                {(gStats.total > 0 || vgStats.total > 0) && (
                    <div className="grid grid-cols-2 gap-4 mb-8">
                        {gStats.total > 0 && (
                            <div className="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-green-400 font-semibold text-lg">G-nivå</span>
                                    <span className={cn(
                                        "text-2xl font-bold",
                                        gPercentage >= 60 ? "text-green-400" : "text-red-400"
                                    )}>
                                        {gPercentage}%
                                    </span>
                                </div>
                                <div className="h-2 bg-green-900/30 rounded-full overflow-hidden mb-2">
                                    <div
                                        className="h-full bg-green-500 transition-all"
                                        style={{ width: `${gPercentage}%` }}
                                    />
                                </div>
                                <p className="text-green-300/70 text-sm">{gStats.correct}/{gStats.total} rätt</p>
                            </div>
                        )}
                        {vgStats.total > 0 && (
                            <div className="bg-purple-500/10 border border-purple-500/30 rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-purple-400 font-semibold text-lg">VG-nivå</span>
                                    <span className={cn(
                                        "text-2xl font-bold",
                                        vgPercentage >= 60 ? "text-purple-400" : "text-red-400"
                                    )}>
                                        {vgPercentage}%
                                    </span>
                                </div>
                                <div className="h-2 bg-purple-900/30 rounded-full overflow-hidden mb-2">
                                    <div
                                        className="h-full bg-purple-500 transition-all"
                                        style={{ width: `${vgPercentage}%` }}
                                    />
                                </div>
                                <p className="text-purple-300/70 text-sm">{vgStats.correct}/{vgStats.total} rätt</p>
                            </div>
                        )}
                    </div>
                )}

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

                {/* Question-by-question results - NEW */}
                <div className="mb-8">
                    <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                        <CheckCircle className="w-5 h-5 text-green-400" />
                        Dina svar
                    </h2>
                    <div className="space-y-3">
                        {results.map((result, idx) => {
                            const question = questions.find(q => q.id === result.questionId)
                            if (!question) return null

                            return (
                                <div
                                    key={result.questionId}
                                    className={cn(
                                        "rounded-xl p-4",
                                        result.correct
                                            ? "bg-green-500/10 border border-green-500/20"
                                            : "bg-red-500/10 border border-red-500/20"
                                    )}
                                >
                                    <div className="flex items-start gap-3">
                                        <span className={cn(
                                            "flex-shrink-0 mt-0.5",
                                            result.correct ? "text-green-400" : "text-red-400"
                                        )}>
                                            {result.correct ? (
                                                <CheckCircle className="w-5 h-5" />
                                            ) : (
                                                <XCircle className="w-5 h-5" />
                                            )}
                                        </span>
                                        <div className="flex-1 min-w-0">
                                            <p className="text-white font-medium mb-1">
                                                {idx + 1}. {question.question}
                                            </p>
                                            <p className="text-zinc-400 text-sm">
                                                Ditt svar: {question.options[result.selectedIndex]}
                                            </p>
                                            {!result.correct && (
                                                <p className="text-red-400 text-sm mt-1">
                                                    Rätt svar: {question.options[question.correctIndex]}
                                                </p>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            )
                        })}
                    </div>
                </div>

                {/* Actions */}
                <div className="flex gap-4">
                    <button
                        onClick={() => setPhase('review')}
                        className="flex-1 py-4 rounded-xl border border-zinc-700 text-zinc-300 hover:border-zinc-600 flex items-center justify-center gap-2"
                    >
                        <BookOpen className="w-5 h-5" />
                        Detaljerad granskning
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

