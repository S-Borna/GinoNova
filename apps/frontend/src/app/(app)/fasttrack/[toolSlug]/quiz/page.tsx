"use client"

/**
 * FastTrack Quiz Page
 * Quiz for a specific tool
 */

import * as React from "react"
import { useState, Suspense } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowRight, CheckCircle, XCircle, RotateCcw, Lightbulb } from "lucide-react"
import { TOOLS_DATA } from "@/data/fasttrack-tools"
import { FASTTRACK_QUIZ } from "@/data/fasttrack-quiz"

function QuizContent() {
    const params = useParams()
    const toolSlug = params?.toolSlug as string

    const tool = TOOLS_DATA.find(t => t.slug === toolSlug)
    const questions = FASTTRACK_QUIZ[toolSlug] || []

    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [score, setScore] = useState(0)

    function selectAnswer(index: number) {
        if (showResult) return
        setSelectedAnswer(index)
    }

    function confirmAnswer() {
        if (selectedAnswer === null) return
        const isCorrect = selectedAnswer === questions[currentIndex].correct
        if (isCorrect) setScore(prev => prev + 1)
        setShowResult(true)
    }

    function nextQuestion() {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswer(null)
            setShowResult(false)
        }
    }

    function resetQuiz() {
        setCurrentIndex(0)
        setSelectedAnswer(null)
        setShowResult(false)
        setScore(0)
    }

    if (!tool || questions.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center py-20">
                    <p className="text-zinc-400 mb-4">Inga quiz-frågor tillgängliga för detta verktyg ännu</p>
                    <Link href="/fasttrack" className="text-amber-400 hover:text-amber-300">
                        ← Tillbaka till FastTrack
                    </Link>
                </div>
            </div>
        )
    }

    // Quiz Complete
    if (currentIndex >= questions.length - 1 && showResult) {
        const isCorrect = selectedAnswer === questions[currentIndex].correct
        const finalScore = score
        const finalPercentage = Math.round((finalScore / questions.length) * 100)

        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto">
                    <div className="mb-8">
                        <div className={cn(
                            "p-6 rounded-xl mb-4",
                            isCorrect ? "bg-emerald-500/10 border border-emerald-500/30" : "bg-red-500/10 border border-red-500/30"
                        )}>
                            <div className="flex items-center gap-2 mb-2">
                                {isCorrect ? <CheckCircle className="w-5 h-5 text-emerald-400" /> : <XCircle className="w-5 h-5 text-red-400" />}
                                <span className={isCorrect ? "text-emerald-400" : "text-red-400"}>{isCorrect ? "Rätt!" : "Fel"}</span>
                            </div>
                            {questions[currentIndex].explanation && (
                                <p className="text-sm text-zinc-400">{questions[currentIndex].explanation}</p>
                            )}
                        </div>
                    </div>

                    <div className="text-center py-12">
                        <h1 className="text-3xl font-bold mb-4">Quiz Klart!</h1>
                        <div className={cn(
                            "w-32 h-32 rounded-full mx-auto mb-6 flex items-center justify-center text-4xl font-bold",
                            finalPercentage >= 80 ? "bg-emerald-500/20 text-emerald-400 border-2 border-emerald-500/30"
                                : finalPercentage >= 60 ? "bg-yellow-500/20 text-yellow-400 border-2 border-yellow-500/30"
                                    : "bg-red-500/20 text-red-400 border-2 border-red-500/30"
                        )}>
                            {finalPercentage}%
                        </div>
                        <p className="text-xl text-zinc-300 mb-2">{finalScore} av {questions.length} rätt</p>
                        <p className="text-zinc-500 mb-8">
                            {finalPercentage >= 80 ? "Utmärkt! 🎉" : finalPercentage >= 60 ? "Bra jobbat!" : "Fortsätt öva! 💪"}
                        </p>
                        <div className="flex gap-4 justify-center">
                            <button onClick={resetQuiz} className="flex items-center gap-2 px-6 py-3 rounded-lg bg-zinc-800 hover:bg-zinc-700">
                                <RotateCcw className="w-4 h-4" />Försök igen
                            </button>
                            <Link href={`/fasttrack/${toolSlug}`} className="flex items-center gap-2 px-6 py-3 rounded-lg bg-blue-600 hover:bg-blue-500">
                                Tillbaka
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    const currentQuestion = questions[currentIndex]
    const progress = ((currentIndex + 1) / questions.length) * 100

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-2xl mx-auto">
                <div className="mb-6">
                    <Link href={`/fasttrack/${toolSlug}`} className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4">
                        ← Tillbaka till {tool.name}
                    </Link>
                    <h1 className="text-2xl font-bold flex items-center gap-2">
                        <span>{tool.icon}</span>{tool.name} Quiz
                    </h1>
                    <p className="text-zinc-400">Fråga {currentIndex + 1} av {questions.length}</p>
                </div>

                <div className="w-full h-1 bg-zinc-800 rounded-full mb-8">
                    <div className="h-full bg-blue-500 rounded-full transition-all" style={{ width: `${progress}%` }} />
                </div>

                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <p className="text-lg font-medium mb-6">{currentQuestion.question}</p>
                    <div className="space-y-3">
                        {currentQuestion.options.map((option, i) => (
                            <button
                                key={i}
                                onClick={() => selectAnswer(i)}
                                disabled={showResult}
                                className={cn(
                                    "w-full p-4 rounded-xl text-left transition-all border",
                                    showResult && i === currentQuestion.correct && "bg-emerald-500/20 border-emerald-500/50",
                                    showResult && selectedAnswer === i && i !== currentQuestion.correct && "bg-red-500/20 border-red-500/50",
                                    !showResult && selectedAnswer === i && "bg-blue-500/20 border-blue-500/50",
                                    !showResult && selectedAnswer !== i && "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                                )}
                            >
                                <div className="flex items-center gap-3">
                                    <span className="w-8 h-8 rounded-lg bg-zinc-700 flex items-center justify-center text-sm font-medium">
                                        {String.fromCharCode(65 + i)}
                                    </span>
                                    <span>{option}</span>
                                </div>
                            </button>
                        ))}
                    </div>
                </div>

                {showResult && currentQuestion.explanation && (
                    <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4 mb-6">
                        <div className="flex items-start gap-2">
                            <Lightbulb className="w-5 h-5 text-blue-400 mt-0.5" />
                            <p className="text-sm text-zinc-300">{currentQuestion.explanation}</p>
                        </div>
                    </div>
                )}

                <div className="flex justify-end">
                    {!showResult ? (
                        <button
                            onClick={confirmAnswer}
                            disabled={selectedAnswer === null}
                            className={cn(
                                "px-6 py-3 rounded-xl font-medium transition-all",
                                selectedAnswer !== null ? "bg-blue-600 hover:bg-blue-500" : "bg-zinc-800 opacity-50 cursor-not-allowed"
                            )}
                        >
                            Bekräfta svar
                        </button>
                    ) : (
                        <button onClick={nextQuestion} className="flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500">
                            Nästa <ArrowRight className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}

export default function FastTrackQuizPage() {
    return (
        <Suspense fallback={
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-blue-500" />
            </div>
        }>
            <QuizContent />
        </Suspense>
    )
}
