"use client"

/**
 * FastTrack Session Page
 * Combined flashcards/quiz from multiple tools
 */

import * as React from "react"
import { useState, useEffect, useMemo, Suspense } from "react"
import { useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle, XCircle, BookOpen, Brain, Lightbulb } from "lucide-react"
import { TOOLS_DATA } from "../page"
import { FASTTRACK_FLASHCARDS } from "@/data/fasttrack-flashcards"
import { FASTTRACK_QUIZ } from "@/data/fasttrack-quiz"

function SessionContent() {
    const searchParams = useSearchParams()
    const toolSlugs = searchParams?.get("tools")?.split(",") || []
    const mode = searchParams?.get("mode") || "flashcards"

    const selectedTools = TOOLS_DATA.filter(t => toolSlugs.includes(t.slug))

    // Combine and shuffle content
    const content = useMemo(() => {
        if (mode === "flashcards") {
            const allCards = toolSlugs.flatMap(slug =>
                (FASTTRACK_FLASHCARDS[slug] || []).map(card => ({ ...card, toolSlug: slug }))
            )
            return allCards.sort(() => Math.random() - 0.5)
        } else {
            const allQuestions = toolSlugs.flatMap(slug =>
                (FASTTRACK_QUIZ[slug] || []).map(q => ({ ...q, toolSlug: slug }))
            )
            return allQuestions.sort(() => Math.random() - 0.5)
        }
    }, [toolSlugs, mode])

    // Flashcard state
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)

    // Quiz state
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [score, setScore] = useState(0)

    if (content.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center py-20">
                    <p className="text-zinc-400 mb-4">Inget innehåll tillgängligt för valda verktyg</p>
                    <Link href="/fasttrack" className="text-amber-400 hover:text-amber-300">
                        ← Tillbaka till FastTrack
                    </Link>
                </div>
            </div>
        )
    }

    const progress = ((currentIndex + 1) / content.length) * 100
    const currentTool = TOOLS_DATA.find(t => t.slug === (content[currentIndex] as any).toolSlug)

    // FLASHCARDS MODE
    if (mode === "flashcards") {
        const currentCard = content[currentIndex] as { front: string; back: string; toolSlug: string }

        function nextCard() {
            if (currentIndex < content.length - 1) {
                setCurrentIndex(prev => prev + 1)
                setIsFlipped(false)
            }
        }

        function prevCard() {
            if (currentIndex > 0) {
                setCurrentIndex(prev => prev - 1)
                setIsFlipped(false)
            }
        }

        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto">
                    <div className="mb-6">
                        <Link href="/fasttrack" className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4">
                            ← Tillbaka till FastTrack
                        </Link>
                        <div className="flex items-center gap-2 mb-2">
                            <BookOpen className="w-5 h-5 text-purple-400" />
                            <h1 className="text-2xl font-bold">Kombinerade Flashcards</h1>
                        </div>
                        <p className="text-zinc-400">
                            {selectedTools.map(t => t.name).join(", ")} • Kort {currentIndex + 1} av {content.length}
                        </p>
                    </div>

                    <div className="w-full h-1 bg-zinc-800 rounded-full mb-4">
                        <div className="h-full bg-purple-500 rounded-full transition-all" style={{ width: `${progress}%` }} />
                    </div>

                    {/* Current Tool Badge */}
                    <div className="flex justify-center mb-4">
                        <span className="px-3 py-1 rounded-full bg-zinc-800 text-sm">
                            {currentTool?.icon} {currentTool?.name}
                        </span>
                    </div>

                    {/* Flashcard */}
                    <div onClick={() => setIsFlipped(!isFlipped)} className="relative w-full aspect-[4/3] cursor-pointer mb-8">
                        <div className={cn(
                            "absolute inset-0 rounded-2xl p-8 bg-gradient-to-br from-purple-600/30 to-purple-900/30 border border-purple-500/30 flex flex-col items-center justify-center transition-all duration-500",
                            isFlipped && "opacity-0 pointer-events-none"
                        )}>
                            <p className="text-sm text-purple-400 mb-4">Fråga</p>
                            <p className="text-xl text-center font-medium">{currentCard.front}</p>
                            <p className="text-sm text-zinc-500 mt-6">Klicka för att vända</p>
                        </div>
                        <div className={cn(
                            "absolute inset-0 rounded-2xl p-8 bg-gradient-to-br from-emerald-600/30 to-emerald-900/30 border border-emerald-500/30 flex flex-col items-center justify-center transition-all duration-500",
                            !isFlipped && "opacity-0 pointer-events-none"
                        )}>
                            <p className="text-sm text-emerald-400 mb-4">Svar</p>
                            <p className="text-lg text-center">{currentCard.back}</p>
                        </div>
                    </div>

                    <div className="flex items-center justify-between">
                        <button onClick={prevCard} disabled={currentIndex === 0} className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-lg bg-zinc-800 hover:bg-zinc-700",
                            currentIndex === 0 && "opacity-50 cursor-not-allowed"
                        )}>
                            <ArrowLeft className="w-4 h-4" />Föregående
                        </button>
                        <button onClick={() => { setCurrentIndex(0); setIsFlipped(false) }} className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700">
                            <RotateCcw className="w-5 h-5" />
                        </button>
                        {currentIndex < content.length - 1 ? (
                            <button onClick={nextCard} className="flex items-center gap-2 px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500">
                                Nästa<ArrowRight className="w-4 h-4" />
                            </button>
                        ) : (
                            <Link href="/fasttrack" className="flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500">
                                <CheckCircle className="w-4 h-4" />Klar!
                            </Link>
                        )}
                    </div>
                </div>
            </div>
        )
    }

    // QUIZ MODE
    const currentQuestion = content[currentIndex] as { question: string; options: string[]; correct: number; explanation?: string; toolSlug: string }

    function selectAnswer(index: number) {
        if (showResult) return
        setSelectedAnswer(index)
    }

    function confirmAnswer() {
        if (selectedAnswer === null) return
        if (selectedAnswer === currentQuestion.correct) setScore(prev => prev + 1)
        setShowResult(true)
    }

    function nextQuestion() {
        if (currentIndex < content.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswer(null)
            setShowResult(false)
        }
    }

    // Quiz Complete
    if (currentIndex >= content.length - 1 && showResult) {
        const finalPercentage = Math.round((score / content.length) * 100)
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center py-12">
                    <h1 className="text-3xl font-bold mb-4">Quiz Klart!</h1>
                    <div className={cn(
                        "w-32 h-32 rounded-full mx-auto mb-6 flex items-center justify-center text-4xl font-bold",
                        finalPercentage >= 80 ? "bg-emerald-500/20 text-emerald-400 border-2 border-emerald-500/30"
                            : finalPercentage >= 60 ? "bg-yellow-500/20 text-yellow-400 border-2 border-yellow-500/30"
                                : "bg-red-500/20 text-red-400 border-2 border-red-500/30"
                    )}>
                        {finalPercentage}%
                    </div>
                    <p className="text-xl text-zinc-300 mb-2">{score} av {content.length} rätt</p>
                    <p className="text-zinc-500 mb-8">
                        {finalPercentage >= 80 ? "Utmärkt! 🎉" : finalPercentage >= 60 ? "Bra jobbat!" : "Fortsätt öva! 💪"}
                    </p>
                    <Link href="/fasttrack" className="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-amber-600 hover:bg-amber-500">
                        Tillbaka till FastTrack
                    </Link>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-2xl mx-auto">
                <div className="mb-6">
                    <Link href="/fasttrack" className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4">
                        ← Tillbaka
                    </Link>
                    <div className="flex items-center gap-2 mb-2">
                        <Brain className="w-5 h-5 text-blue-400" />
                        <h1 className="text-2xl font-bold">Kombinerat Quiz</h1>
                    </div>
                    <p className="text-zinc-400">Fråga {currentIndex + 1} av {content.length}</p>
                </div>

                <div className="w-full h-1 bg-zinc-800 rounded-full mb-4">
                    <div className="h-full bg-blue-500 rounded-full transition-all" style={{ width: `${progress}%` }} />
                </div>

                <div className="flex justify-center mb-4">
                    <span className="px-3 py-1 rounded-full bg-zinc-800 text-sm">
                        {currentTool?.icon} {currentTool?.name}
                    </span>
                </div>

                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 mb-6">
                    <p className="text-lg font-medium mb-6">{currentQuestion.question}</p>
                    <div className="space-y-3">
                        {currentQuestion.options.map((option, i) => (
                            <button key={i} onClick={() => selectAnswer(i)} disabled={showResult} className={cn(
                                "w-full p-4 rounded-xl text-left transition-all border",
                                showResult && i === currentQuestion.correct && "bg-emerald-500/20 border-emerald-500/50",
                                showResult && selectedAnswer === i && i !== currentQuestion.correct && "bg-red-500/20 border-red-500/50",
                                !showResult && selectedAnswer === i && "bg-blue-500/20 border-blue-500/50",
                                !showResult && selectedAnswer !== i && "bg-zinc-800/50 border-zinc-700 hover:border-zinc-600"
                            )}>
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
                        <button onClick={confirmAnswer} disabled={selectedAnswer === null} className={cn(
                            "px-6 py-3 rounded-xl font-medium",
                            selectedAnswer !== null ? "bg-blue-600 hover:bg-blue-500" : "bg-zinc-800 opacity-50 cursor-not-allowed"
                        )}>
                            Bekräfta svar
                        </button>
                    ) : (
                        <button onClick={nextQuestion} className="flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500">
                            Nästa<ArrowRight className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}

export default function FastTrackSessionPage() {
    return (
        <Suspense fallback={
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-amber-500" />
            </div>
        }>
            <SessionContent />
        </Suspense>
    )
}
