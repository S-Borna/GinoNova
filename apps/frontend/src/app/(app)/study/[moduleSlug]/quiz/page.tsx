"use client"

/**
 * Multiple Choice Quiz Study Mode
 *
 * Test knowledge with questions and answers
 * With star/favorite functionality
 * Uses LOCAL DATA instead of API
 */

import * as React from "react"
import { useState, useEffect, Suspense } from "react"
import { useParams, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowRight, CheckCircle, XCircle, RotateCcw, Lightbulb, Star, X } from "lucide-react"
import { useFavorites } from "@/hooks/useFavorites"

// Import local quiz data
import { DOE25_TASK_QUIZ, getAllDOE25Quiz, TaskQuizQuestion as DOE25QuizQuestion, TaskQuizSet } from "@/data/doe25-task-quiz"
import { LINUX247_TASK_QUIZ, getAllLinux247Quiz, TaskQuizQuestion as Linux247QuizQuestion } from "@/data/linux247-task-quiz"
import { HANDSON_TASK_QUIZ, getAllHandsOnQuiz, TaskQuizQuestion as HandsOnQuizQuestion } from "@/data/handson-task-quiz"
import { HANDSON_MEGA_QUIZ, MegaQuizQuestion, MegaQuizTaskSet } from "@/data/handson-mega-quiz"

// Generic quiz question type for local data
interface LocalQuizQuestion {
    id: string
    question: string
    options: string[]
    correctIndex: number
    explanation: string
    difficulty?: 'G' | 'VG' | 'beginner' | 'intermediate' | 'advanced'
    category?: string
}

// Helper to get all mega quiz questions flattened
function getAllMegaQuiz(): LocalQuizQuestion[] {
    return HANDSON_MEGA_QUIZ.flatMap(task =>
        task.questions.map(q => ({
            ...q,
            options: q.options as string[]
        }))
    )
}

// Module configuration - maps URL slugs to data
const MODULE_CONFIG: Record<string, {
    getData: () => LocalQuizQuestion[]
    getTaskData: () => TaskQuizSet[] | MegaQuizTaskSet[]
    title: string
    useMegaQuiz?: boolean
}> = {
    'doe25-tenta': {
        getData: getAllDOE25Quiz as () => LocalQuizQuestion[],
        getTaskData: () => DOE25_TASK_QUIZ as TaskQuizSet[],
        title: 'DOE25 Tentaplugg'
    },
    'linux-247': {
        getData: getAllLinux247Quiz as () => LocalQuizQuestion[],
        getTaskData: () => LINUX247_TASK_QUIZ as TaskQuizSet[],
        title: 'Linux 24/7'
    },
    'hands-on-lab': {
        getData: getAllMegaQuiz as () => LocalQuizQuestion[],
        getTaskData: () => HANDSON_MEGA_QUIZ as MegaQuizTaskSet[],
        title: 'Hands-On Lab',
        useMegaQuiz: true
    }
}

interface QuizQuestion {
    id: string
    question: string
    options: string[]
    correct: number
    explanation?: string
    module_slug: string
    lesson_title: string
}

function QuizContent() {
    const params = useParams()
    const searchParams = useSearchParams()
    const moduleSlug = params?.moduleSlug as string || ""

    const [questions, setQuestions] = useState<QuizQuestion[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [score, setScore] = useState(0)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [moduleTitle, setModuleTitle] = useState("")
    const [showHint, setShowHint] = useState(false)
    
    // Store all answers for results review
    const [answers, setAnswers] = useState<{ questionId: string; selectedIndex: number; correct: boolean }[]>([])

    // Star modal
    const [showStarModal, setShowStarModal] = useState(false)
    const [starName, setStarName] = useState("")

    // Favorites hook
    const { addFavorite, removeFavorite, isFavorite, getFavoriteId } = useFavorites()

    useEffect(() => {
        loadQuiz()
    }, [moduleSlug])

    function loadQuiz() {
        try {
            setLoading(true)
            setError(null)

            // Get module config
            const config = MODULE_CONFIG[moduleSlug]
            if (!config) {
                setError(`Modul '${moduleSlug}' hittades inte. Tillgängliga: ${Object.keys(MODULE_CONFIG).join(', ')}`)
                return
            }

            // Get URL parameters
            const tasksFilter = searchParams?.get("tasks") || ""
            const selectedTaskIds = tasksFilter ? tasksFilter.split(',') : []
            const shuffle = searchParams?.get("shuffle") === "true"
            const difficultyFilter = searchParams?.get("difficulty") || "all"
            const countParam = searchParams?.get("count")
            const maxCount = countParam ? parseInt(countParam) : undefined

            // Get local data - filtered by tasks or all
            let localData: LocalQuizQuestion[] = []

            if (selectedTaskIds.length > 0) {
                // Get quiz for selected tasks only
                const taskData = config.getTaskData()
                taskData.forEach(taskSet => {
                    if (selectedTaskIds.includes(taskSet.taskId)) {
                        localData.push(...(taskSet.questions as LocalQuizQuestion[]))
                    }
                })
            } else {
                // Get all quiz questions
                localData = config.getData()
            }

            if (!localData || localData.length === 0) {
                setError("Inga quiz-frågor tillgängliga för valda tasks")
                return
            }

            // Filter by difficulty if specified
            if (difficultyFilter !== 'all') {
                // Map difficulty filter to question difficulty values
                // G = Grundläggande (beginner), VG = Väl Godkänd (intermediate/advanced)
                // Also support direct difficulty values from mega-quiz
                const difficultyMap: Record<string, string[]> = {
                    'beginner': ['G', 'beginner', 'easy'],
                    'intermediate': ['VG', 'intermediate', 'medium'],
                    'advanced': ['advanced', 'hard', 'expert']
                }
                const validDifficulties = difficultyMap[difficultyFilter] || []
                localData = localData.filter(q => {
                    const qDifficulty = (q.difficulty || 'G').toLowerCase().trim()
                    return validDifficulties.some(d => d.toLowerCase() === qDifficulty)
                })
            }

            if (localData.length === 0) {
                setError("Inga frågor för vald svårighetsgrad")
                return
            }

            // Transform local data to QuizQuestion format
            let transformedQuestions: QuizQuestion[] = localData.map(q => ({
                id: q.id,
                question: q.question,
                options: [...q.options],
                correct: q.correctIndex,
                explanation: q.explanation,
                module_slug: moduleSlug,
                lesson_title: q.category || 'Quiz'
            }))

            // Shuffle (always shuffle for better experience, especially important when limiting count)
            if (shuffle || maxCount) {
                transformedQuestions = transformedQuestions.sort(() => Math.random() - 0.5)
            }

            // Limit to count if specified
            if (maxCount && transformedQuestions.length > maxCount) {
                transformedQuestions = transformedQuestions.slice(0, maxCount)
            }

            setQuestions(transformedQuestions)
            setModuleTitle(config.title)

        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading quiz")
        } finally {
            setLoading(false)
        }
    }

    function selectAnswer(index: number) {
        if (showResult) return
        setSelectedAnswer(index)
    }

    function confirmAnswer() {
        if (selectedAnswer === null) return

        const isCorrect = selectedAnswer === questions[currentIndex].correct
        if (isCorrect) {
            setScore(prev => prev + 1)
        }
        
        // Store answer for results review
        setAnswers(prev => [...prev, {
            questionId: questions[currentIndex].id,
            selectedIndex: selectedAnswer,
            correct: isCorrect
        }])
        
        setShowResult(true)
    }

    function nextQuestion() {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswer(null)
            setShowResult(false)
            setShowHint(false)
        }
    }

    function resetQuiz() {
        setCurrentIndex(0)
        setSelectedAnswer(null)
        setShowResult(false)
        setScore(0)
        setShowHint(false)
        setAnswers([])
    }

    if (loading) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-blue-500" />
            </div>
        )
    }

    if (error || questions.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center py-20">
                    <p className="text-zinc-400 mb-4">
                        {error || "Inga quiz-frågor tillgängliga för denna modul"}
                    </p>
                    <Link
                        href="/study"
                        className="text-blue-400 hover:text-blue-300"
                    >
                        ← Tillbaka till Studyroom
                    </Link>
                </div>
            </div>
        )
    }

    // Quiz Complete
    if (currentIndex >= questions.length - 1 && showResult) {
        const percentage = Math.round((score / questions.length) * 100)
        const isCorrect = selectedAnswer === questions[currentIndex].correct
        const finalScore = isCorrect ? score : score
        const finalPercentage = Math.round((finalScore / questions.length) * 100)

        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto">
                    {/* Final Score */}
                    <div className="text-center py-8">
                        <div className={cn(
                            "text-6xl font-bold mb-2",
                            finalPercentage >= 80
                                ? "text-emerald-400"
                                : finalPercentage >= 60
                                    ? "text-yellow-400"
                                    : "text-red-400"
                        )}>
                            {finalPercentage}%
                        </div>

                        <p className="text-xl text-zinc-300 mb-2">
                            Du fick {finalScore} av {questions.length} rätt
                        </p>

                        <p className="text-zinc-500 mb-6">
                            {finalPercentage >= 80
                                ? "Utmärkt! Du har koll på materialet! 🎉"
                                : finalPercentage >= 60
                                    ? "Bra jobbat! Lite mer övning så sitter det!"
                                    : "Fortsätt öva! Du kommer dit! 💪"
                            }
                        </p>
                    </div>
                    
                    {/* Detailed Results - Question by Question */}
                    <div className="mb-8">
                        <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                            <CheckCircle className="w-5 h-5 text-emerald-400" />
                            Dina svar
                        </h2>
                        <div className="space-y-3">
                            {answers.map((answer, idx) => {
                                const question = questions.find(q => q.id === answer.questionId)
                                if (!question) return null
                                
                                return (
                                    <div
                                        key={answer.questionId}
                                        className={cn(
                                            "rounded-xl p-4",
                                            answer.correct 
                                                ? "bg-emerald-500/10 border border-emerald-500/20" 
                                                : "bg-red-500/10 border border-red-500/20"
                                        )}
                                    >
                                        <div className="flex items-start gap-3">
                                            <span className={cn(
                                                "flex-shrink-0 mt-0.5",
                                                answer.correct ? "text-emerald-400" : "text-red-400"
                                            )}>
                                                {answer.correct ? (
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
                                                    Ditt svar: {question.options[answer.selectedIndex]}
                                                </p>
                                                {!answer.correct && (
                                                    <p className="text-red-400 text-sm mt-1">
                                                        Rätt svar: {question.options[question.correct]}
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
                    <div className="flex gap-4 justify-center">
                        <button
                            onClick={resetQuiz}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-lg",
                                "bg-zinc-800 hover:bg-zinc-700 transition-colors"
                            )}
                        >
                            <RotateCcw className="w-4 h-4" />
                            Försök igen
                        </button>
                        <Link
                            href="/study"
                            prefetch={false}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-lg",
                                "bg-blue-600 hover:bg-blue-500 transition-colors"
                            )}
                        >
                            Tillbaka till Studyroom
                        </Link>
                    </div>
                </div>
            </div>
        )
    }

    const currentQuestion = questions[currentIndex]
    const progress = ((currentIndex + 1) / questions.length) * 100
    const isCurrentFavorite = currentQuestion ? isFavorite(moduleSlug, currentQuestion.question, "quiz") : false

    function handleStarClick() {
        if (isCurrentFavorite) {
            const favId = getFavoriteId(moduleSlug, currentQuestion.question, "quiz")
            if (favId) removeFavorite(favId)
        } else {
            setShowStarModal(true)
            setStarName("")
        }
    }

    function handleSaveStar() {
        if (!starName.trim()) return
        addFavorite({
            type: "quiz",
            customName: starName.slice(0, 6),
            moduleSlug,
            moduleTitle,
            originalQuestion: currentQuestion.question
        })
        setShowStarModal(false)
        setStarName("")
    }

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-2xl mx-auto">
                {/* Header */}
                <div className="mb-6">
                    <Link
                        href="/study"
                        prefetch={false}
                        className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4"
                    >
                        ← Tillbaka
                    </Link>
                    <div className="flex items-center justify-between">
                        <h1 className="text-2xl font-bold">{moduleTitle}</h1>
                        {/* Star button */}
                        <button
                            onClick={handleStarClick}
                            className={cn(
                                "p-3 rounded-xl transition-all",
                                isCurrentFavorite
                                    ? "bg-amber-500/20 text-amber-400"
                                    : "bg-zinc-800 text-zinc-400 hover:text-amber-400 hover:bg-zinc-700"
                            )}
                            title={isCurrentFavorite ? "Ta bort favorit" : "Lägg till favorit"}
                        >
                            <Star className={cn("w-5 h-5", isCurrentFavorite && "fill-amber-400")} />
                        </button>
                    </div>
                    <div className="flex items-center justify-between">
                        <p className="text-zinc-400">
                            Fråga {currentIndex + 1} av {questions.length}
                        </p>
                        <p className="text-sm text-zinc-500">
                            {Math.round(progress)}% klart
                        </p>
                    </div>
                </div>

                {/* Progress Bar */}
                <div className="w-full h-1 bg-zinc-800 rounded-full mb-8">
                    <div
                        className="h-full bg-blue-500 rounded-full transition-all duration-300"
                        style={{ width: `${progress}%` }}
                    />
                </div>

                {/* Question */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <div className="flex items-start justify-between gap-4 mb-4">
                        <p className="text-lg font-medium">{currentQuestion.question}</p>
                        {!showResult && (
                            <button
                                onClick={() => setShowHint(!showHint)}
                                className="text-zinc-500 hover:text-zinc-300 p-2"
                                title="Visa ledtråd"
                            >
                                <Lightbulb className="w-5 h-5" />
                            </button>
                        )}
                    </div>

                    {showHint && currentQuestion.explanation && !showResult && (
                        <div className="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3 mb-4">
                            <p className="text-sm text-yellow-300/80">
                                💡 Ledtråd: {currentQuestion.explanation}
                            </p>
                        </div>
                    )}

                    {/* Options */}
                    <div className="space-y-3">
                        {currentQuestion.options.map((option, index) => {
                            const isSelected = selectedAnswer === index
                            const isCorrect = index === currentQuestion.correct
                            const showCorrect = showResult && isCorrect
                            const showWrong = showResult && isSelected && !isCorrect

                            return (
                                <button
                                    key={index}
                                    onClick={() => selectAnswer(index)}
                                    disabled={showResult}
                                    className={cn(
                                        "w-full text-left p-4 rounded-lg border transition-all duration-200",
                                        !showResult && isSelected && "bg-blue-500/20 border-blue-500/50",
                                        !showResult && !isSelected && "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600",
                                        showCorrect && "bg-emerald-500/20 border-emerald-500/50",
                                        showWrong && "bg-red-500/20 border-red-500/50",
                                        showResult && !showCorrect && !showWrong && "opacity-50"
                                    )}
                                >
                                    <div className="flex items-center gap-3">
                                        <span className={cn(
                                            "w-6 h-6 rounded-full flex items-center justify-center text-sm font-medium",
                                            !showResult && isSelected && "bg-blue-500 text-white",
                                            !showResult && !isSelected && "bg-zinc-700 text-zinc-400",
                                            showCorrect && "bg-emerald-500 text-white",
                                            showWrong && "bg-red-500 text-white"
                                        )}>
                                            {String.fromCharCode(65 + index)}
                                        </span>
                                        <span>{option}</span>
                                        {showCorrect && <CheckCircle className="w-5 h-5 text-emerald-400 ml-auto" />}
                                        {showWrong && <XCircle className="w-5 h-5 text-red-400 ml-auto" />}
                                    </div>
                                </button>
                            )
                        })}
                    </div>
                </div>

                {/* Result Message */}
                {showResult && (
                    <div className={cn(
                        "p-4 rounded-lg mb-6",
                        selectedAnswer === currentQuestion.correct
                            ? "bg-emerald-500/10 border border-emerald-500/30"
                            : "bg-red-500/10 border border-red-500/30"
                    )}>
                        <div className="flex items-center gap-2 mb-2">
                            {selectedAnswer === currentQuestion.correct ? (
                                <>
                                    <CheckCircle className="w-5 h-5 text-emerald-400" />
                                    <span className="text-emerald-400 font-medium">Rätt svar!</span>
                                </>
                            ) : (
                                <>
                                    <XCircle className="w-5 h-5 text-red-400" />
                                    <span className="text-red-400 font-medium">Fel svar</span>
                                </>
                            )}
                        </div>
                        {currentQuestion.explanation && (
                            <p className="text-sm text-zinc-400">{currentQuestion.explanation}</p>
                        )}
                    </div>
                )}

                {/* Actions */}
                <div className="flex justify-end">
                    {!showResult ? (
                        <button
                            onClick={confirmAnswer}
                            disabled={selectedAnswer === null}
                            className={cn(
                                "px-6 py-3 rounded-lg font-medium transition-colors",
                                selectedAnswer !== null
                                    ? "bg-purple-600 hover:bg-purple-500"
                                    : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                            )}
                        >
                            Bekräfta svar
                        </button>
                    ) : (
                        <button
                            onClick={nextQuestion}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-lg",
                                "bg-blue-600 hover:bg-blue-500 transition-colors"
                            )}
                        >
                            Nästa
                            <ArrowRight className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>

            {/* Star Modal */}
            {showStarModal && (
                <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50">
                    <div className="bg-zinc-900 border border-zinc-700 rounded-2xl p-6 w-80">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="text-lg font-semibold">Namnge favorit</h3>
                            <button
                                onClick={() => setShowStarModal(false)}
                                className="p-1 hover:bg-zinc-800 rounded"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </div>
                        <p className="text-sm text-zinc-400 mb-4">Max 6 tecken</p>
                        <input
                            type="text"
                            value={starName}
                            onChange={(e) => setStarName(e.target.value.slice(0, 6))}
                            placeholder="Ex: GitPR"
                            maxLength={6}
                            className="w-full bg-zinc-800 border border-zinc-700 rounded-xl px-4 py-3 mb-4 text-white placeholder:text-zinc-500 focus:outline-none focus:border-amber-500"
                            autoFocus
                            onKeyDown={(e) => e.key === "Enter" && handleSaveStar()}
                        />
                        <div className="flex gap-2">
                            <button
                                onClick={() => setShowStarModal(false)}
                                className="flex-1 px-4 py-2 bg-zinc-800 rounded-xl hover:bg-zinc-700 transition-colors"
                            >
                                Avbryt
                            </button>
                            <button
                                onClick={handleSaveStar}
                                disabled={!starName.trim()}
                                className="flex-1 px-4 py-2 bg-amber-500 text-black font-medium rounded-xl hover:bg-amber-400 transition-colors disabled:opacity-50"
                            >
                                <Star className="w-4 h-4 inline mr-1" />
                                Spara
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   EXPORT WITH SUSPENSE
   ============================================================================ */

export default function QuizPage() {
    return (
        <Suspense fallback={
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
            </div>
        }>
            <QuizContent />
        </Suspense>
    )
}
