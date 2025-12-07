"use client"

/**
 * Studyflow Quiz Page
 * Multiple choice quiz med scoring
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { useParams, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowRight, CheckCircle, XCircle, RotateCcw, Lightbulb, ArrowLeft } from "lucide-react"

const API_BASE_URL = "https://saas-project-production-9de8.up.railway.app"

interface QuizQuestion {
    id: string
    question: string
    options: string[]
    correct: number
    explanation?: string
    topic_id: string
    topic_title: string
}

export default function QuizPage() {
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

    const fetchQuiz = useCallback(async () => {
        try {
            setLoading(true)

            const topics = searchParams?.get("topics") || ""
            const shuffle = searchParams?.get("shuffle") === "true"

            const url = new URL(`${API_BASE_URL}/api/studyflow/modules/${moduleSlug}/quiz`)
            if (topics) url.searchParams.set("topics", topics)
            if (shuffle) url.searchParams.set("shuffle", "true")

            const res = await fetch(url.toString())
            if (!res.ok) throw new Error("Failed to fetch quiz")

            const data = await res.json()
            setQuestions(data.questions)
            setModuleTitle(data.module_title)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading quiz")
        } finally {
            setLoading(false)
        }
    }, [moduleSlug, searchParams])

    useEffect(() => {
        if (moduleSlug) {
            fetchQuiz()
        }
    }, [moduleSlug, fetchQuiz])

    function selectAnswer(index: number) {
        if (showResult) return
        setSelectedAnswer(index)
    }

    function confirmAnswer() {
        if (selectedAnswer === null) return
        setShowResult(true)
        if (selectedAnswer === questions[currentIndex].correct) {
            setScore(score + 1)
        }
    }

    function nextQuestion() {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(currentIndex + 1)
            setSelectedAnswer(null)
            setShowResult(false)
            setShowHint(false)
        }
    }

    function restart() {
        setCurrentIndex(0)
        setSelectedAnswer(null)
        setShowResult(false)
        setScore(0)
        setShowHint(false)
    }

    if (loading) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
            </div>
        )
    }

    if (error || questions.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center">
                    <p className="text-red-400 mb-4">{error || "Inga quiz-frågor hittades"}</p>
                    <Link href="/studyflow/practice" className="text-purple-400 hover:text-purple-300">
                        ← Tillbaka
                    </Link>
                </div>
            </div>
        )
    }

    const currentQuestion = questions[currentIndex]
    const progress = ((currentIndex + 1) / questions.length) * 100
    const isComplete = currentIndex === questions.length - 1 && showResult
    const finalScore = Math.round((score / questions.length) * 100)

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-2xl mx-auto">
                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <Link
                        href="/studyflow/practice"
                        className="flex items-center gap-2 text-zinc-400 hover:text-white transition-colors"
                    >
                        <ArrowLeft className="w-4 h-4" />
                        Tillbaka
                    </Link>
                    <div className="flex items-center gap-4">
                        <span className="text-green-400">{score} rätt</span>
                        <span className="text-zinc-400">
                            {currentIndex + 1} / {questions.length}
                        </span>
                    </div>
                </div>

                {/* Title */}
                <h1 className="text-2xl font-bold mb-2 text-center">{moduleTitle}</h1>
                <p className="text-zinc-500 text-center mb-6">{currentQuestion.topic_title}</p>

                {/* Progress Bar */}
                <div className="h-1 bg-zinc-800 rounded-full mb-8 overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-green-500 to-emerald-500 transition-all duration-300"
                        style={{ width: `${progress}%` }}
                    />
                </div>

                {/* Question */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6 mb-6">
                    <p className="text-lg mb-6">{currentQuestion.question}</p>

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
                                        "w-full p-4 rounded-lg border text-left transition-all flex items-center gap-3",
                                        !showResult && isSelected && "border-purple-500 bg-purple-500/10",
                                        !showResult && !isSelected && "border-zinc-700 hover:border-zinc-600 hover:bg-zinc-800/50",
                                        showCorrect && "border-green-500 bg-green-500/10",
                                        showWrong && "border-red-500 bg-red-500/10",
                                        showResult && !isSelected && !isCorrect && "opacity-50"
                                    )}
                                >
                                    <span
                                        className={cn(
                                            "w-8 h-8 rounded-full border flex items-center justify-center text-sm font-medium flex-shrink-0",
                                            !showResult && isSelected && "border-purple-500 text-purple-400",
                                            !showResult && !isSelected && "border-zinc-600 text-zinc-400",
                                            showCorrect && "border-green-500 bg-green-500 text-white",
                                            showWrong && "border-red-500 bg-red-500 text-white"
                                        )}
                                    >
                                        {showCorrect ? (
                                            <CheckCircle className="w-5 h-5" />
                                        ) : showWrong ? (
                                            <XCircle className="w-5 h-5" />
                                        ) : (
                                            String.fromCharCode(65 + index)
                                        )}
                                    </span>
                                    <span className="flex-1">{option}</span>
                                </button>
                            )
                        })}
                    </div>
                </div>

                {/* Explanation */}
                {showResult && currentQuestion.explanation && (
                    <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4 mb-6">
                        <div className="flex items-start gap-3">
                            <Lightbulb className="w-5 h-5 text-blue-400 flex-shrink-0 mt-0.5" />
                            <p className="text-zinc-300">{currentQuestion.explanation}</p>
                        </div>
                    </div>
                )}

                {/* Hint Button */}
                {!showResult && !showHint && currentQuestion.explanation && (
                    <button
                        onClick={() => setShowHint(true)}
                        className="flex items-center gap-2 text-zinc-500 hover:text-zinc-400 mb-6 transition-colors"
                    >
                        <Lightbulb className="w-4 h-4" />
                        Visa ledtråd
                    </button>
                )}

                {showHint && !showResult && (
                    <div className="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4 mb-6">
                        <p className="text-zinc-400 text-sm">{currentQuestion.explanation}</p>
                    </div>
                )}

                {/* Actions */}
                <div className="flex items-center justify-center gap-4">
                    {!showResult ? (
                        <button
                            onClick={confirmAnswer}
                            disabled={selectedAnswer === null}
                            className={cn(
                                "px-8 py-3 rounded-lg font-medium transition-all",
                                selectedAnswer !== null
                                    ? "bg-purple-500 hover:bg-purple-600 text-white"
                                    : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                            )}
                        >
                            Bekräfta svar
                        </button>
                    ) : isComplete ? (
                        <div className="w-full">
                            <div
                                className={cn(
                                    "p-6 rounded-xl text-center mb-4",
                                    finalScore >= 80
                                        ? "bg-green-500/10 border border-green-500/30"
                                        : finalScore >= 50
                                            ? "bg-yellow-500/10 border border-yellow-500/30"
                                            : "bg-red-500/10 border border-red-500/30"
                                )}
                            >
                                <div className="text-4xl font-bold mb-2">
                                    {finalScore}%
                                </div>
                                <p className="text-zinc-400">
                                    Du fick {score} av {questions.length} rätt
                                </p>
                                <p className="text-lg mt-2">
                                    {finalScore >= 80
                                        ? "🎉 Utmärkt!"
                                        : finalScore >= 50
                                            ? "👍 Bra jobbat!"
                                            : "💪 Fortsätt öva!"}
                                </p>
                            </div>
                            <button
                                onClick={restart}
                                className="w-full px-8 py-3 bg-purple-500 hover:bg-purple-600 rounded-lg font-medium transition-colors flex items-center justify-center gap-2"
                            >
                                <RotateCcw className="w-4 h-4" />
                                Försök igen
                            </button>
                        </div>
                    ) : (
                        <button
                            onClick={nextQuestion}
                            className="px-8 py-3 bg-purple-500 hover:bg-purple-600 rounded-lg font-medium transition-colors flex items-center gap-2"
                        >
                            Nästa fråga
                            <ArrowRight className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}
