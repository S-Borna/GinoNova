"use client"

/**
 * Tenta-Simulator - Quiz Engine (INTE HUVUDSIDAN!)
 *
 * ⚠️ VIKTIGT: Detta är QUIZ-MOTORN, inte setup-sidan!
 * → Huvudsidan för val av inställningar är: /study/page.tsx (Studyroom)
 *
 * 🔴 NYA FRÅGEKÄLLOR? GÅ TILL /study/page.tsx FÖRST! 🔴
 * 1. Lägg först till källa i study/page.tsx (setup-sidan där användaren väljer)
 * 2. Därefter uppdatera denna fil för quiz-logiken:
 *    - Importera quiz-data
 *    - Lägg till converter-funktion
 *    - Lägg till i useMemo för questions
 *    - Lägg till i allQuestions baserat på selectedSources
 *    - Lägg till knapp i backup setup-vy (om den används)
 *
 * Denna sida:
 * - Tar emot inställningar via URL-params från Studyroom
 * - Kör själva quizzen med timer, frågor, resultat
 * - Har en backup setup-vy om man går hit direkt (utan params)
 *
 * FLÖDE: /study (välj källa) → Starta → /study/tenta-simulator (denna fil - quiz körs)
 *
 * Features:
 * - Timed sessions (60, 75, 90, 120 min)
 * - Random questions from Omtenta 2.0 + Hands-On + Linux Commands + Linux Tenta + Manpage Tenta
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
    Zap, Award, BookOpen, AlertTriangle, Sparkles, ChevronRight
} from "lucide-react"
import { getToken } from "@/lib/auth"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Import quiz data
import { HANDSON_MEGA_QUIZ, type MegaQuizQuestion } from "@/data/handson-mega-quiz"
import { ALL_LINUX_COMMAND_QUESTIONS, type LinuxCommandQuestion } from "@/data/linux-commands-quiz"
import { ALL_LINUX_TENTA_QUESTIONS, type LinuxTentaQuestion } from "@/data/linux-tenta-quiz"
import { ALL_MANPAGE_TENTA_QUESTIONS, type ManpageTentaQuestion } from "@/data/manpage-tenta-quiz"
// OMTENTA 2.0 - Nya frågor från Nod-filer
import { ALL_OMTENTA_2_QUESTIONS, type Omtenta2Question, type Omtenta2Topic, OMTENTA2_TOPICS } from "@/data/omtenta-2.0-quiz"
// FLÖDEN - Scenario & Flow questions
import { ALL_TENTA_FLODEN_QUESTIONS, type TentaFlodenQuestion } from "@/data/tenta-floden-quiz"
import { ALL_MANPAGE_FLODEN_QUESTIONS, type ManpageFlodenQuestion } from "@/data/manpage-floden-quiz"
// Linux Exam 510 - G-nivå frågor för tentaförberedelse
import { ALL_LINUX_EXAM_510_QUESTIONS, type LinuxExam510Question, type LinuxExam510Topic, LINUX_EXAM_510_TOPICS } from "@/data/linux-exam-510-quiz"

// Unified question type for simulator (always has G/VG difficulty)
interface SimulatorQuestion {
    id: string
    question: string
    options: string[]
    correctIndex?: 0 | 1 | 2 | 3  // For single-select (legacy)
    correctIndices: number[]       // For multi-select support
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    source: 'handson' | 'linux-commands' | 'linux-tenta' | 'omtenta-2' | 'tenta-floden' | 'manpage-floden'
    scenario?: string // Optional scenario context
    isMultiSelect: boolean
    nodeTopic?: Omtenta2Topic // For Omtenta 2.0 node filtering
    exam510Topic?: LinuxExam510Topic // For Linux Exam 510 topic filtering
    questionType?: 'scenario' | 'flow' | 'standard' // For Flöden questions
}

interface SimulatorSettings {
    duration: number // minutes
    questionCount: number
    includeG: boolean
    includeVG: boolean
    showTimer: boolean
    gradingMode: 'live' | 'end' // live = immediate feedback, end = feedback after completion
    selectedSources: ('handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta' | 'omtenta-2' | 'tenta-floden' | 'manpage-floden' | 'linux-exam-510')[] // Multi-select question sources
    selectedNodes: Omtenta2Topic[] // For Omtenta 2.0 node filtering
    selectedExam510Topics: LinuxExam510Topic[] // For Linux Exam 510 topic filtering
}

interface QuizResult {
    questionId: string
    correct: boolean
    selectedIndex?: number         // Legacy single-select
    selectedIndices: number[]      // Multi-select support
    correctIndex?: number          // Legacy single-select
    correctIndices: number[]       // Multi-select support
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
    selectedSources: ['omtenta-2'], // Default to Omtenta 2.0
    selectedNodes: OMTENTA2_TOPICS, // All nodes by default
    selectedExam510Topics: LINUX_EXAM_510_TOPICS // All topics by default
}

// Shuffle array helper
function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    // Fisher-Yates shuffle with crypto random for better randomness
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

// Shuffle options within a question and update correctIndices
function shuffleQuestionOptions(question: SimulatorQuestion): SimulatorQuestion {
    // Create array of option objects with their original index
    const optionsWithIndex = question.options.map((option, index) => ({
        option,
        wasCorrect: question.correctIndices.includes(index)
    }))

    // Shuffle the options
    const shuffledOptions = shuffleArray(optionsWithIndex)

    // Find new correct indices
    const newCorrectIndices = shuffledOptions
        .map((o, idx) => o.wasCorrect ? idx : -1)
        .filter(idx => idx !== -1)

    return {
        ...question,
        options: shuffledOptions.map(o => o.option),
        correctIndices: newCorrectIndices,
        correctIndex: newCorrectIndices[0] as 0 | 1 | 2 | 3 | undefined
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
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty,
        category: q.category,
        source: 'handson',
        isMultiSelect: false
    }
}

// Convert Linux Commands question to SimulatorQuestion (map difficulty)
function convertLinuxCommandQuestion(q: LinuxCommandQuestion): SimulatorQuestion {
    // Map: beginner/intermediate → G, advanced → VG
    const difficulty: 'G' | 'VG' = q.difficulty === 'advanced' ? 'VG' : 'G'

    return {
        id: q.id,
        question: q.question,
        options: q.options as string[],
        correctIndex: q.correctIndex as 0 | 1 | 2 | 3,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty,
        category: q.category,
        source: 'linux-commands',
        isMultiSelect: false
    }
}

// Convert Linux Tenta question to SimulatorQuestion
function convertLinuxTentaQuestion(q: LinuxTentaQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'linux-tenta',
        scenario: q.scenario,
        isMultiSelect: false
    }
}

// Convert Manpage Tenta question to SimulatorQuestion
function convertManpageTentaQuestion(q: ManpageTentaQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'linux-tenta', // Same source as linux-tenta for compatibility
        isMultiSelect: false
    }
}

// Convert Omtenta 2.0 question to SimulatorQuestion (FULL multi-select support)
function convertOmtenta2Question(q: Omtenta2Question): SimulatorQuestion {
    const isMulti = q.correctIndices.length > 1
    return {
        id: q.id,
        question: isMulti ? `${q.question} (Välj ${q.correctIndices.length} svar)` : q.question,
        options: q.options,
        correctIndex: isMulti ? undefined : q.correctIndices[0] as 0 | 1 | 2 | 3,
        correctIndices: q.correctIndices,
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'omtenta-2',
        isMultiSelect: isMulti,
        nodeTopic: q.topic
    }
}

// Convert Tenta Flöden question to SimulatorQuestion
function convertTentaFlodenQuestion(q: TentaFlodenQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'tenta-floden',
        isMultiSelect: false,
        questionType: q.type
    }
}

// Convert Manpage Flöden question to SimulatorQuestion
function convertManpageFlodenQuestion(q: ManpageFlodenQuestion): SimulatorQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category,
        source: 'manpage-floden',
        isMultiSelect: false,
        questionType: q.type
    }
}

// Convert Linux Exam 510 question to SimulatorQuestion
function convertLinuxExam510Question(q: LinuxExam510Question): SimulatorQuestion {
    // All 510 questions are G-level (VG filtered out during creation)
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndex as 0 | 1 | 2 | 3,
        correctIndices: [q.correctIndex],
        explanation: q.explanation,
        difficulty: 'G', // All are G-level
        category: q.category,
        source: 'linux-tenta', // Compatible source for UI
        isMultiSelect: false,
        exam510Topic: q.topic // For topic filtering
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
    const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]) // Multi-select support
    const [results, setResults] = useState<QuizResult[]>([])
    const [timeRemaining, setTimeRemaining] = useState(0)
    const [questionStartTime, setQuestionStartTime] = useState(0)
    const [isPaused, setIsPaused] = useState(false)
    const [showLiveFeedback, setShowLiveFeedback] = useState(false)
    const [hasAutoStarted, setHasAutoStarted] = useState(false)
    const [showAbortModal, setShowAbortModal] = useState(false)
    const [examStartTime, setExamStartTime] = useState<Date | null>(null)
    const hasSubmittedResult = useRef(false)

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

    // Get Linux Tenta questions (original exam)
    const linuxTentaQuestions = useMemo(() => {
        return ALL_LINUX_TENTA_QUESTIONS.map(convertLinuxTentaQuestion)
    }, [])

    // Get Manpage Tenta questions (298 comprehensive Linux command questions)
    const manpageTentaQuestions = useMemo(() => {
        return ALL_MANPAGE_TENTA_QUESTIONS.map(convertManpageTentaQuestion)
    }, [])

    // Get Omtenta 2.0 questions (800+ questions from 10 Nod-modules, WITH multi-select support)
    const omtenta2Questions = useMemo(() => {
        return ALL_OMTENTA_2_QUESTIONS.map(convertOmtenta2Question)
    }, [])

    // Get Tenta Flöden questions (40 scenario/flow questions based on Linux Tenta)
    const tentaFlodenQuestions = useMemo(() => {
        return ALL_TENTA_FLODEN_QUESTIONS.map(convertTentaFlodenQuestion)
    }, [])

    // Get Manpage Flöden questions (150 scenario/flow questions based on Manpage Tenta)
    const manpageFlodenQuestions = useMemo(() => {
        return ALL_MANPAGE_FLODEN_QUESTIONS.map(convertManpageFlodenQuestion)
    }, [])

    // Get Linux Exam 510 questions (~430 G-level questions covering all Mål 1-20)
    const linuxExam510Questions = useMemo(() => {
        return ALL_LINUX_EXAM_510_QUESTIONS.map(convertLinuxExam510Question)
    }, [])

    // Get filtered questions based on selected sources and nodes
    const allQuestions = useMemo(() => {
        const questions: SimulatorQuestion[] = []
        if (settings.selectedSources.includes('handson')) {
            questions.push(...handsonQuestions)
        }
        if (settings.selectedSources.includes('linux-commands')) {
            questions.push(...linuxCommandsQuestions)
        }
        if (settings.selectedSources.includes('linux-tenta')) {
            questions.push(...linuxTentaQuestions)
        }
        if (settings.selectedSources.includes('manpage-tenta')) {
            questions.push(...manpageTentaQuestions)
        }
        if (settings.selectedSources.includes('omtenta-2')) {
            // Filter by selected nodes
            const filtered = omtenta2Questions.filter(q =>
                !q.nodeTopic || settings.selectedNodes.includes(q.nodeTopic)
            )
            questions.push(...filtered)
        }
        if (settings.selectedSources.includes('tenta-floden')) {
            questions.push(...tentaFlodenQuestions)
        }
        if (settings.selectedSources.includes('manpage-floden')) {
            questions.push(...manpageFlodenQuestions)
        }
        if (settings.selectedSources.includes('linux-exam-510')) {
            // Filter by selected topics
            const filtered = linuxExam510Questions.filter(q =>
                !q.exam510Topic || settings.selectedExam510Topics.includes(q.exam510Topic)
            )
            questions.push(...filtered)
        }
        return questions
    }, [handsonQuestions, linuxCommandsQuestions, linuxTentaQuestions, manpageTentaQuestions, omtenta2Questions, tentaFlodenQuestions, manpageFlodenQuestions, linuxExam510Questions, settings.selectedSources, settings.selectedNodes, settings.selectedExam510Topics])

    // Parse URL params and auto-start if params provided
    useEffect(() => {
        if (hasAutoStarted) return

        const timeParam = searchParams?.get('time')
        const countParam = searchParams?.get('count')
        const gradingParam = searchParams?.get('grading')
        const difficultyParam = searchParams?.get('difficulty')
        const sourceParam = searchParams?.get('source')
        const nodesParam = searchParams?.get('nodes')
        const exam510TopicsParam = searchParams?.get('exam510topics')

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

            // Parse source param
            let selectedSources: ('handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta' | 'omtenta-2' | 'tenta-floden' | 'manpage-floden' | 'linux-exam-510')[] = ['omtenta-2']
            if (sourceParam) {
                const sources = sourceParam.split(',') as ('handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta' | 'omtenta-2' | 'tenta-floden' | 'manpage-floden' | 'linux-exam-510')[]
                selectedSources = sources.filter(s => ['handson', 'linux-commands', 'linux-tenta', 'manpage-tenta', 'omtenta-2', 'tenta-floden', 'manpage-floden', 'linux-exam-510'].includes(s))
                if (selectedSources.length === 0) selectedSources = ['omtenta-2']
            }

            // Parse nodes param for Omtenta 2.0
            let selectedNodes: Omtenta2Topic[] = OMTENTA2_TOPICS
            if (nodesParam) {
                const nodes = nodesParam.split(',') as Omtenta2Topic[]
                selectedNodes = nodes.filter(n => OMTENTA2_TOPICS.includes(n))
                if (selectedNodes.length === 0) selectedNodes = OMTENTA2_TOPICS
            }

            // Parse topics param for Linux Exam 510
            let selectedExam510Topics: LinuxExam510Topic[] = LINUX_EXAM_510_TOPICS
            if (exam510TopicsParam) {
                const topics = exam510TopicsParam.split(',') as LinuxExam510Topic[]
                selectedExam510Topics = topics.filter(t => LINUX_EXAM_510_TOPICS.includes(t))
                if (selectedExam510Topics.length === 0) selectedExam510Topics = LINUX_EXAM_510_TOPICS
            }

            const newSettings: SimulatorSettings = {
                ...DEFAULT_SETTINGS,
                duration: timeParam ? parseInt(timeParam) : DEFAULT_SETTINGS.duration,
                questionCount: countParam ? (parseInt(countParam) === 999 ? 9999 : parseInt(countParam)) : DEFAULT_SETTINGS.questionCount,
                gradingMode: (gradingParam === 'end' ? 'end' : 'live') as 'live' | 'end',
                includeG,
                includeVG,
                selectedSources,
                selectedNodes,
                selectedExam510Topics
            }
            setSettings(newSettings)
            setHasAutoStarted(true)

            // Get questions based on selected sources
            let sourceQuestions: SimulatorQuestion[] = []
            if (selectedSources.includes('handson')) sourceQuestions.push(...handsonQuestions)
            if (selectedSources.includes('linux-commands')) sourceQuestions.push(...linuxCommandsQuestions)
            if (selectedSources.includes('linux-tenta')) sourceQuestions.push(...linuxTentaQuestions)
            if (selectedSources.includes('manpage-tenta')) sourceQuestions.push(...manpageTentaQuestions)
            if (selectedSources.includes('omtenta-2')) {
                // Filter by selected nodes
                const filtered = omtenta2Questions.filter(q =>
                    !q.nodeTopic || selectedNodes.includes(q.nodeTopic)
                )
                sourceQuestions.push(...filtered)
            }
            if (selectedSources.includes('tenta-floden')) sourceQuestions.push(...tentaFlodenQuestions)
            if (selectedSources.includes('manpage-floden')) sourceQuestions.push(...manpageFlodenQuestions)
            if (selectedSources.includes('linux-exam-510')) {
                // Filter by selected topics
                const filtered = linuxExam510Questions.filter(q =>
                    !q.exam510Topic || selectedExam510Topics.includes(q.exam510Topic)
                )
                sourceQuestions.push(...filtered)
            }

            // Auto-start the quiz
            setTimeout(() => {
                let filtered = sourceQuestions.filter(q => {
                    if (newSettings.includeG && q.difficulty === 'G') return true
                    if (newSettings.includeVG && q.difficulty === 'VG') return true
                    return false
                })
                const shuffled = shuffleArray(filtered)
                console.log('🎲 Shuffled questions:', shuffled.length, 'First 5 IDs:', shuffled.slice(0, 5).map(q => q.id))
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
    }, [searchParams, hasAutoStarted, handsonQuestions, linuxCommandsQuestions, linuxTentaQuestions, omtenta2Questions, tentaFlodenQuestions, manpageFlodenQuestions, linuxExam510Questions])

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
        setSelectedAnswers([])
        setResults([])
        setTimeRemaining(settings.duration * 60)
        setQuestionStartTime(Date.now())
        setExamStartTime(new Date())
        hasSubmittedResult.current = false
        setPhase('quiz')
    }

    // Toggle answer for multi-select
    const toggleAnswer = (idx: number) => {
        const currentQuestion = questions[currentIndex]
        if (currentQuestion.isMultiSelect) {
            setSelectedAnswers(prev =>
                prev.includes(idx)
                    ? prev.filter(i => i !== idx)
                    : [...prev, idx]
            )
        } else {
            setSelectedAnswer(idx)
        }
    }

    // Check if multi-select answer is correct
    const checkMultiSelectAnswer = (selected: number[], correct: number[]): boolean => {
        if (selected.length !== correct.length) return false
        const sortedSelected = [...selected].sort((a, b) => a - b)
        const sortedCorrect = [...correct].sort((a, b) => a - b)
        return sortedSelected.every((val, idx) => val === sortedCorrect[idx])
    }

    // Submit answer
    const submitAnswer = () => {
        const currentQuestion = questions[currentIndex]
        const isMulti = currentQuestion.isMultiSelect

        // Check if answer is selected
        if (isMulti && selectedAnswers.length === 0) return
        if (!isMulti && selectedAnswer === null) return

        const timeSpent = Math.floor((Date.now() - questionStartTime) / 1000)

        const result: QuizResult = {
            questionId: currentQuestion.id,
            correct: isMulti
                ? checkMultiSelectAnswer(selectedAnswers, currentQuestion.correctIndices)
                : selectedAnswer === currentQuestion.correctIndices[0],
            selectedIndex: isMulti ? undefined : selectedAnswer!,
            selectedIndices: isMulti ? selectedAnswers : [selectedAnswer!],
            correctIndex: isMulti ? undefined : currentQuestion.correctIndices[0],
            correctIndices: currentQuestion.correctIndices,
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
            setSelectedAnswers([])
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
        <div className="max-w-4xl mx-auto">
            {/* Hero Header with Glassmorphism */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center mb-8"
            >
                <motion.div
                    className="inline-flex items-center justify-center w-24 h-24 rounded-3xl bg-gradient-to-br from-purple-500/30 to-pink-500/30 backdrop-blur-xl border border-purple-500/20 mb-6 relative overflow-hidden"
                    whileHover={{ scale: 1.05, rotate: 5 }}
                    transition={{ type: "spring", stiffness: 300 }}
                >
                    {/* Animated background glow */}
                    <motion.div
                        className="absolute inset-0 bg-gradient-to-br from-purple-500/20 to-pink-500/20"
                        animate={{
                            scale: [1, 1.2, 1],
                            opacity: [0.5, 0.8, 0.5]
                        }}
                        transition={{ duration: 3, repeat: Infinity }}
                    />
                    <Target className="w-12 h-12 text-purple-300 relative z-10" />
                </motion.div>
                <h1 className="text-4xl font-bold bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent mb-3">
                    Tenta-Simulator
                </h1>
                <p className="text-zinc-400 text-lg">Simulera riktiga tentaförhållanden • Test your skills under pressure</p>
            </motion.div>

            {/* Main Settings Card with Glassmorphism */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
                className="relative bg-gradient-to-br from-zinc-900/80 via-zinc-900/50 to-zinc-900/80 backdrop-blur-xl border border-zinc-800/50 rounded-3xl p-8 mb-6 overflow-hidden"
            >
                {/* Subtle glow effect */}
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl" />

                <div className="relative z-10">
                    <div className="flex items-center gap-3 mb-8">
                        <div className="p-2.5 rounded-xl bg-gradient-to-br from-yellow-500/20 to-orange-500/20 border border-yellow-500/20">
                            <Zap className="w-5 h-5 text-yellow-400" />
                        </div>
                        <h2 className="text-xl font-bold text-white">Konfigurera din tentasimulering</h2>
                    </div>

                    {/* Grid layout for better organization */}
                    <div className="grid md:grid-cols-2 gap-6 mb-6">
                        {/* Duration */}
                        <div>
                            <label className="flex items-center gap-2 text-sm font-medium text-zinc-300 mb-3">
                                <Clock className="w-4 h-4 text-purple-400" />
                                Tidsgräns
                            </label>
                            <div className="grid grid-cols-2 gap-2">
                                {[15, 30, 45, 60].map(mins => (
                                    <motion.button
                                        key={mins}
                                        onClick={() => setSettings(s => ({ ...s, duration: mins }))}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-3 px-4 rounded-xl border transition-all font-medium relative overflow-hidden",
                                            settings.duration === mins
                                                ? "bg-gradient-to-br from-purple-500/30 to-pink-500/30 border-purple-400/50 text-purple-200 shadow-lg shadow-purple-500/20"
                                                : "bg-zinc-800/30 border-zinc-700/50 text-zinc-400 hover:border-zinc-600 hover:bg-zinc-800/50"
                                        )}
                                    >
                                        {settings.duration === mins && (
                                            <motion.div
                                                layoutId="duration-active"
                                                className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-pink-500/10"
                                                transition={{ type: "spring", stiffness: 300, damping: 30 }}
                                            />
                                        )}
                                        <span className="relative z-10">{mins} min</span>
                                    </motion.button>
                                ))}
                            </div>
                        </div>

                        {/* Question count */}
                        <div>
                            <label className="flex items-center gap-2 text-sm font-medium text-zinc-300 mb-3">
                                <Target className="w-4 h-4 text-blue-400" />
                                Antal frågor
                            </label>
                            <div className="grid grid-cols-4 gap-2">
                                {[25, 50, 75, 100, 150, 200, 250, 'Alla'].map(count => (
                                    <motion.button
                                        key={count}
                                        onClick={() => setSettings(s => ({ ...s, questionCount: count === 'Alla' ? 9999 : count as number }))}
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                        className={cn(
                                            "py-2 px-2 rounded-xl border transition-all font-medium relative overflow-hidden text-sm",
                                            (count === 'Alla' ? settings.questionCount === 9999 : settings.questionCount === count)
                                                ? "bg-gradient-to-br from-blue-500/30 to-cyan-500/30 border-blue-400/50 text-blue-200 shadow-lg shadow-blue-500/20"
                                                : "bg-zinc-800/30 border-zinc-700/50 text-zinc-400 hover:border-zinc-600 hover:bg-zinc-800/50"
                                        )}
                                    >
                                        {(count === 'Alla' ? settings.questionCount === 9999 : settings.questionCount === count) && (
                                            <motion.div
                                                layoutId="count-active"
                                                className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-cyan-500/10"
                                                transition={{ type: "spring", stiffness: 300, damping: 30 }}
                                            />
                                        )}
                                        <span className="relative z-10">{count}</span>
                                    </motion.button>
                                ))}
                            </div>
                        </div>
                    </div>

                    {/* Difficulty - G/VG Selection */}
                    <div className="mb-6">
                        <label className="flex items-center gap-2 text-sm font-medium text-zinc-300 mb-3">
                            <Award className="w-4 h-4 text-yellow-400" />
                            Betygsnivå
                        </label>
                        <div className="grid grid-cols-3 gap-3">
                            <motion.button
                                onClick={() => setSettings(s => ({ ...s, includeG: true, includeVG: false }))}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                className={cn(
                                    "py-4 px-4 rounded-xl border transition-all flex flex-col items-center gap-2 relative overflow-hidden",
                                    settings.includeG && !settings.includeVG
                                        ? "bg-gradient-to-br from-green-500/30 to-emerald-500/30 border-green-400/50 text-green-200 shadow-lg shadow-green-500/20"
                                        : "bg-zinc-800/30 border-zinc-700/50 text-zinc-500 hover:border-zinc-600 hover:bg-zinc-800/50"
                                )}
                            >
                                {settings.includeG && !settings.includeVG && (
                                    <motion.div
                                        layoutId="difficulty-active"
                                        className="absolute inset-0 bg-gradient-to-br from-green-500/10 to-emerald-500/10"
                                        transition={{ type: "spring", stiffness: 300, damping: 30 }}
                                    />
                                )}
                                <span className="text-2xl font-bold relative z-10">G</span>
                                <span className="text-xs opacity-80 relative z-10">Godkänt</span>
                            </motion.button>
                            <motion.button
                                onClick={() => setSettings(s => ({ ...s, includeG: false, includeVG: true }))}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                className={cn(
                                    "py-4 px-4 rounded-xl border transition-all flex flex-col items-center gap-2 relative overflow-hidden",
                                    !settings.includeG && settings.includeVG
                                        ? "bg-gradient-to-br from-purple-500/30 to-violet-500/30 border-purple-400/50 text-purple-200 shadow-lg shadow-purple-500/20"
                                        : "bg-zinc-800/30 border-zinc-700/50 text-zinc-500 hover:border-zinc-600 hover:bg-zinc-800/50"
                                )}
                            >
                                {!settings.includeG && settings.includeVG && (
                                    <motion.div
                                        layoutId="difficulty-active"
                                        className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-violet-500/10"
                                        transition={{ type: "spring", stiffness: 300, damping: 30 }}
                                    />
                                )}
                                <span className="text-2xl font-bold relative z-10">VG</span>
                                <span className="text-xs opacity-80 relative z-10">Väl Godkänt</span>
                            </motion.button>
                            <motion.button
                                onClick={() => setSettings(s => ({ ...s, includeG: true, includeVG: true }))}
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                className={cn(
                                    "py-4 px-4 rounded-xl border transition-all flex flex-col items-center gap-2 relative overflow-hidden",
                                    settings.includeG && settings.includeVG
                                        ? "bg-gradient-to-br from-yellow-500/30 via-orange-500/30 to-pink-500/30 border-yellow-400/50 text-yellow-200 shadow-lg shadow-yellow-500/20"
                                        : "bg-zinc-800/30 border-zinc-700/50 text-zinc-500 hover:border-zinc-600 hover:bg-zinc-800/50"
                                )}
                            >
                                {settings.includeG && settings.includeVG && (
                                    <motion.div
                                        layoutId="difficulty-active"
                                        className="absolute inset-0 bg-gradient-to-br from-yellow-500/10 via-orange-500/10 to-pink-500/10"
                                        transition={{ type: "spring", stiffness: 300, damping: 30 }}
                                    />
                                )}
                                <span className="text-2xl font-bold relative z-10">Mixad</span>
                                <span className="text-xs opacity-80 relative z-10">G + VG</span>
                            </motion.button>
                        </div>
                        <motion.p
                            key={`${settings.includeG}-${settings.includeVG}`}
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className="text-xs text-zinc-400 mt-3 flex items-center gap-2 bg-zinc-800/30 rounded-lg p-2"
                        >
                            <Brain className="w-3.5 h-3.5 flex-shrink-0" />
                            {settings.includeG && !settings.includeVG && "Fokus på grundläggande förståelse för G-nivå"}
                            {!settings.includeG && settings.includeVG && "Avancerade frågor för högre betyg"}
                            {settings.includeG && settings.includeVG && "Blandade frågor för fullständig tentaförberedelse"}
                        </motion.p>
                    </div>

                    {/* Question Source Selection - Multi-select */}
                    <div className="mb-6">
                        <label className="flex items-center gap-2 text-sm font-medium text-zinc-300 mb-3">
                            <BookOpen className="w-4 h-4 text-teal-400" />
                            Frågekällor <span className="text-zinc-500 text-xs ml-1">(välj en eller flera)</span>
                        </label>
                        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
                            <button
                                onClick={() => setSettings(s => {
                                    const sources = s.selectedSources.includes('omtenta-2')
                                        ? s.selectedSources.filter(src => src !== 'omtenta-2')
                                        : [...s.selectedSources, 'omtenta-2'] as ('omtenta-2' | 'handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta')[]
                                    return { ...s, selectedSources: sources.length > 0 ? sources : ['omtenta-2'] }
                                })}
                                className={cn(
                                    "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                    settings.selectedSources.includes('omtenta-2')
                                        ? "bg-teal-500/20 border-teal-500 text-teal-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                                )}
                            >
                                {settings.selectedSources.includes('omtenta-2') && (
                                    <div className="absolute top-2 right-2 w-4 h-4 bg-teal-500 rounded-full flex items-center justify-center">
                                        <CheckCircle className="w-3 h-3 text-white" />
                                    </div>
                                )}
                                <span className="text-lg">🎯</span>
                                <span className="text-sm font-medium">Omtenta 2.0</span>
                                <span className="text-xs opacity-70">{omtenta2Questions.length} frågor</span>
                            </button>
                            <button
                                onClick={() => setSettings(s => {
                                    const sources = s.selectedSources.includes('handson')
                                        ? s.selectedSources.filter(src => src !== 'handson')
                                        : [...s.selectedSources, 'handson'] as ('omtenta-2' | 'handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta')[]
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
                                        : [...s.selectedSources, 'linux-commands'] as ('omtenta-2' | 'handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta')[]
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
                                    const sources = s.selectedSources.includes('linux-tenta')
                                        ? s.selectedSources.filter(src => src !== 'linux-tenta')
                                        : [...s.selectedSources, 'linux-tenta'] as ('omtenta-2' | 'handson' | 'linux-commands' | 'linux-tenta')[]
                                    return { ...s, selectedSources: sources.length > 0 ? sources : ['linux-tenta'] }
                                })}
                                className={cn(
                                    "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                    settings.selectedSources.includes('linux-tenta')
                                        ? "bg-red-500/20 border-red-500 text-red-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                                )}
                            >
                                {settings.selectedSources.includes('linux-tenta') && (
                                    <div className="absolute top-2 right-2 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center">
                                        <CheckCircle className="w-3 h-3 text-white" />
                                    </div>
                                )}
                                <span className="text-lg">📝</span>
                                <span className="text-sm font-medium">Linux Tentan</span>
                                <span className="text-xs opacity-70">{linuxTentaQuestions.length} frågor</span>
                            </button>
                            <button
                                onClick={() => setSettings(s => {
                                    const sources = s.selectedSources.includes('manpage-tenta')
                                        ? s.selectedSources.filter(src => src !== 'manpage-tenta')
                                        : [...s.selectedSources, 'manpage-tenta'] as ('omtenta-2' | 'handson' | 'linux-commands' | 'linux-tenta' | 'manpage-tenta')[]
                                    return { ...s, selectedSources: sources.length > 0 ? sources : ['manpage-tenta'] }
                                })}
                                className={cn(
                                    "py-3 px-4 rounded-xl border transition-all flex flex-col items-center gap-1 relative",
                                    settings.selectedSources.includes('manpage-tenta')
                                        ? "bg-cyan-500/20 border-cyan-500 text-cyan-300"
                                        : "bg-zinc-800/50 border-zinc-700 text-zinc-500 hover:border-zinc-600"
                                )}
                            >
                                {settings.selectedSources.includes('manpage-tenta') && (
                                    <div className="absolute top-2 right-2 w-4 h-4 bg-cyan-500 rounded-full flex items-center justify-center">
                                        <CheckCircle className="w-3 h-3 text-white" />
                                    </div>
                                )}
                                <span className="text-lg">📚</span>
                                <span className="text-sm font-medium">Manpage Tenta</span>
                                <span className="text-xs opacity-70">{manpageTentaQuestions.length} frågor</span>
                            </button>
                        </div>
                        <p className="text-xs text-zinc-500 mt-2">
                            {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'omtenta-2' && "🎯 Rekommenderat - 10 Nod-moduler med quiz & scenarios"}
                            {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'handson' && "🔧 Praktiska frågor från Hands-On modulen"}
                            {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'linux-commands' && "💻 Terminal-kommandon: cd, ls, grep, docker, LVM & mer"}
                            {settings.selectedSources.length === 1 && settings.selectedSources[0] === 'linux-tenta' && "📝 Original Linux-tentafrågor"}
                            {settings.selectedSources.length > 1 && `Kombinerat: ${settings.selectedSources.length} källor valda (${allQuestions.length} frågor)`}
                        </p>
                    </div>

                    {/* Timer toggle with better design */}
                    <div className="flex items-center justify-between p-4 bg-zinc-800/20 rounded-xl border border-zinc-700/30">
                        <div className="flex items-center gap-2">
                            <Clock className="w-4 h-4 text-zinc-400" />
                            <span className="text-sm font-medium text-zinc-300">Visa timer</span>
                        </div>
                        <button
                            onClick={() => setSettings(s => ({ ...s, showTimer: !s.showTimer }))}
                            className={cn(
                                "relative w-14 h-7 rounded-full transition-all duration-300",
                                settings.showTimer
                                    ? "bg-gradient-to-r from-purple-500 to-pink-500 shadow-lg shadow-purple-500/30"
                                    : "bg-zinc-700"
                            )}
                        >
                            <motion.div
                                className="absolute top-0.5 left-0.5 w-6 h-6 rounded-full bg-white shadow-lg flex items-center justify-center"
                                animate={{ x: settings.showTimer ? 26 : 0 }}
                                transition={{ type: "spring", stiffness: 500, damping: 30 }}
                            >
                                {settings.showTimer && <Clock className="w-3 h-3 text-purple-600" />}
                            </motion.div>
                        </button>
                    </div>
                </div>
            </motion.div>

            {/* Stats preview with glassmorphism */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="bg-gradient-to-br from-zinc-900/60 to-zinc-900/40 backdrop-blur-xl border border-zinc-800/50 rounded-2xl p-5 mb-6"
            >
                <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-2">
                        <div className="p-2 rounded-lg bg-teal-500/20 border border-teal-500/20">
                            <Sparkles className="w-4 h-4 text-teal-400" />
                        </div>
                        <span className="text-sm font-medium text-zinc-300">Tillgängliga frågor</span>
                    </div>
                    <span className="text-2xl font-bold bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">
                        {allQuestions.filter(q =>
                            (settings.includeG && q.difficulty === 'G') ||
                            (settings.includeVG && q.difficulty === 'VG')
                        ).length}
                    </span>
                </div>
                <div className="flex items-center gap-3 text-sm">
                    <div className="flex items-center gap-2 px-3 py-2 bg-green-500/10 border border-green-500/20 rounded-lg">
                        <span className="text-green-400 font-semibold">G:</span>
                        <span className="text-green-300">{allQuestions.filter(q => q.difficulty === 'G').length}</span>
                    </div>
                    <div className="flex items-center gap-2 px-3 py-2 bg-purple-500/10 border border-purple-500/20 rounded-lg">
                        <span className="text-purple-400 font-semibold">VG:</span>
                        <span className="text-purple-300">{allQuestions.filter(q => q.difficulty === 'VG').length}</span>
                    </div>
                    <div className="flex items-center gap-1.5 ml-auto px-3 py-2 bg-zinc-800/30 rounded-lg">
                        <span className="text-xs text-zinc-500">Källor:</span>
                        <span className="text-base">
                            {settings.selectedSources.map(s => s === 'omtenta-2' ? '🎯' : s === 'handson' ? '🔧' : s === 'linux-tenta' ? '📝' : '💻').join(' ')}
                        </span>
                    </div>
                </div>
            </motion.div>

            {/* Start button with epic design */}
            <motion.button
                onClick={startSimulator}
                disabled={!settings.includeG && !settings.includeVG}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
                whileHover={settings.includeG || settings.includeVG ? { scale: 1.02, y: -2 } : {}}
                whileTap={settings.includeG || settings.includeVG ? { scale: 0.98 } : {}}
                className={cn(
                    "w-full py-5 rounded-2xl font-bold text-lg flex items-center justify-center gap-3 transition-all relative overflow-hidden group",
                    settings.includeG || settings.includeVG
                        ? "bg-gradient-to-r from-purple-600 via-pink-600 to-purple-600 text-white shadow-2xl shadow-purple-500/40 hover:shadow-purple-500/60"
                        : "bg-zinc-800/50 border border-zinc-700 text-zinc-500 cursor-not-allowed"
                )}
            >
                {settings.includeG || settings.includeVG && (
                    <>
                        <motion.div
                            className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent"
                            animate={{ x: ['-200%', '200%'] }}
                            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                        />
                        <motion.div
                            className="absolute inset-0 bg-gradient-to-r from-purple-400/0 via-pink-400/20 to-purple-400/0"
                            animate={{ scale: [1, 1.5, 1], opacity: [0.3, 0.6, 0.3] }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />
                    </>
                )}
                <Play className="w-6 h-6 relative z-10" fill="currentColor" />
                <span className="relative z-10">Starta Tenta-Simulator</span>
                <motion.div
                    className="absolute right-4 opacity-0 group-hover:opacity-100 transition-opacity"
                    animate={{ x: [0, 5, 0] }}
                    transition={{ duration: 1, repeat: Infinity }}
                >
                    <ChevronRight className="w-5 h-5" />
                </motion.div>
            </motion.button>
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
                        const isMulti = currentQuestion.isMultiSelect
                        const isSelected = isMulti ? selectedAnswers.includes(idx) : selectedAnswer === idx
                        const isCorrectOption = currentQuestion.correctIndices.includes(idx)
                        const showAsCorrect = showLiveFeedback && isCorrectOption
                        const showAsWrong = showLiveFeedback && isSelected && !isCorrectOption

                        return (
                            <motion.button
                                key={idx}
                                onClick={() => !showLiveFeedback && toggleAnswer(idx)}
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
                                        "w-8 h-8 flex items-center justify-center font-semibold text-sm",
                                        isMulti ? "rounded-md" : "rounded-full",
                                        showAsCorrect && "bg-green-500 text-white",
                                        showAsWrong && "bg-red-500 text-white",
                                        !showLiveFeedback && isSelected && "bg-purple-500 text-white",
                                        !showLiveFeedback && !isSelected && "bg-zinc-800 text-zinc-400",
                                        showLiveFeedback && !showAsCorrect && !showAsWrong && "bg-zinc-800 text-zinc-500"
                                    )}>
                                        {showAsCorrect ? <CheckCircle className="w-5 h-5" /> :
                                            showAsWrong ? <XCircle className="w-5 h-5" /> :
                                                isMulti && isSelected ? <CheckCircle className="w-5 h-5" /> :
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
                        disabled={currentQuestion.isMultiSelect ? selectedAnswers.length === 0 : selectedAnswer === null}
                        className={cn(
                            "w-full py-4 rounded-xl font-semibold flex items-center justify-center gap-2 transition-all",
                            (currentQuestion.isMultiSelect ? selectedAnswers.length > 0 : selectedAnswer !== null)
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
                                                Ditt svar: {result.selectedIndices.map(i => question.options[i]).join(', ')}
                                            </p>
                                            {!result.correct && (
                                                <p className="text-red-400 text-sm mt-1">
                                                    Rätt svar: {result.correctIndices.map(i => question.options[i]).join(', ')}
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

