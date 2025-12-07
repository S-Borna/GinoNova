"use client"

/**
 * Studyflow Flashcards Page
 * Flip-card interface för memorering
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { useParams, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle } from "lucide-react"

const API_BASE_URL = "https://saas-project-production-9de8.up.railway.app"

interface Flashcard {
    id: string
    front: string
    back: string
    topic_id: string
    topic_title: string
}

export default function FlashcardsPage() {
    const params = useParams()
    const searchParams = useSearchParams()
    const moduleSlug = params?.moduleSlug as string || ""

    const [flashcards, setFlashcards] = useState<Flashcard[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [moduleTitle, setModuleTitle] = useState("")

    const fetchFlashcards = useCallback(async () => {
        try {
            setLoading(true)

            const topics = searchParams?.get("topics") || ""
            const shuffle = searchParams?.get("shuffle") === "true"

            const url = new URL(`${API_BASE_URL}/api/studyflow/modules/${moduleSlug}/flashcards`)
            if (topics) url.searchParams.set("topics", topics)
            if (shuffle) url.searchParams.set("shuffle", "true")

            const res = await fetch(url.toString())
            if (!res.ok) throw new Error("Failed to fetch flashcards")

            const data = await res.json()
            setFlashcards(data.flashcards)
            setModuleTitle(data.module_title)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading flashcards")
        } finally {
            setLoading(false)
        }
    }, [moduleSlug, searchParams])

    useEffect(() => {
        if (moduleSlug) {
            fetchFlashcards()
        }
    }, [moduleSlug, fetchFlashcards])

    function flip() {
        setIsFlipped(!isFlipped)
    }

    function next() {
        if (currentIndex < flashcards.length - 1) {
            setCurrentIndex(currentIndex + 1)
            setIsFlipped(false)
        }
    }

    function prev() {
        if (currentIndex > 0) {
            setCurrentIndex(currentIndex - 1)
            setIsFlipped(false)
        }
    }

    function restart() {
        setCurrentIndex(0)
        setIsFlipped(false)
    }

    // Keyboard navigation
    useEffect(() => {
        function handleKeyDown(e: KeyboardEvent) {
            if (e.key === " " || e.key === "Enter") {
                e.preventDefault()
                flip()
            } else if (e.key === "ArrowRight") {
                next()
            } else if (e.key === "ArrowLeft") {
                prev()
            }
        }
        window.addEventListener("keydown", handleKeyDown)
        return () => window.removeEventListener("keydown", handleKeyDown)
    })

    if (loading) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
            </div>
        )
    }

    if (error || flashcards.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center">
                    <p className="text-red-400 mb-4">{error || "Inga flashcards hittades"}</p>
                    <Link href="/studyflow/practice" className="text-purple-400 hover:text-purple-300">
                        ← Tillbaka
                    </Link>
                </div>
            </div>
        )
    }

    const currentCard = flashcards[currentIndex]
    const progress = ((currentIndex + 1) / flashcards.length) * 100

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
                    <div className="text-zinc-400">
                        {currentIndex + 1} / {flashcards.length}
                    </div>
                </div>

                {/* Title */}
                <h1 className="text-2xl font-bold mb-2 text-center">{moduleTitle}</h1>
                <p className="text-zinc-500 text-center mb-6">{currentCard.topic_title}</p>

                {/* Progress Bar */}
                <div className="h-1 bg-zinc-800 rounded-full mb-8 overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-purple-500 to-blue-500 transition-all duration-300"
                        style={{ width: `${progress}%` }}
                    />
                </div>

                {/* Flashcard */}
                <div className="perspective-1000 mb-8">
                    <button
                        onClick={flip}
                        className={cn(
                            "w-full min-h-[300px] relative transition-transform duration-500 transform-style-3d cursor-pointer",
                            isFlipped && "rotate-y-180"
                        )}
                        style={{
                            transformStyle: "preserve-3d",
                            transform: isFlipped ? "rotateY(180deg)" : "rotateY(0deg)",
                        }}
                    >
                        {/* Front */}
                        <div
                            className="absolute inset-0 bg-gradient-to-br from-zinc-900 to-zinc-800 border border-zinc-700 rounded-2xl p-8 flex flex-col items-center justify-center backface-hidden"
                            style={{ backfaceVisibility: "hidden" }}
                        >
                            <span className="text-xs text-purple-400 mb-4">FRÅGA</span>
                            <p className="text-xl text-center">{currentCard.front}</p>
                            <span className="text-xs text-zinc-500 mt-6">Klicka för att vända</span>
                        </div>

                        {/* Back */}
                        <div
                            className="absolute inset-0 bg-gradient-to-br from-purple-900/30 to-blue-900/30 border border-purple-500/30 rounded-2xl p-8 flex flex-col items-center justify-center rotate-y-180"
                            style={{
                                backfaceVisibility: "hidden",
                                transform: "rotateY(180deg)",
                            }}
                        >
                            <span className="text-xs text-green-400 mb-4">SVAR</span>
                            <p className="text-xl text-center">{currentCard.back}</p>
                        </div>
                    </button>
                </div>

                {/* Navigation */}
                <div className="flex items-center justify-center gap-4">
                    <button
                        onClick={prev}
                        disabled={currentIndex === 0}
                        className={cn(
                            "p-3 rounded-lg border transition-colors",
                            currentIndex === 0
                                ? "border-zinc-800 text-zinc-600 cursor-not-allowed"
                                : "border-zinc-700 hover:border-zinc-600 hover:bg-zinc-800"
                        )}
                    >
                        <ArrowLeft className="w-5 h-5" />
                    </button>

                    <button
                        onClick={restart}
                        className="p-3 rounded-lg border border-zinc-700 hover:border-zinc-600 hover:bg-zinc-800 transition-colors"
                        title="Börja om"
                    >
                        <RotateCcw className="w-5 h-5" />
                    </button>

                    <button
                        onClick={next}
                        disabled={currentIndex === flashcards.length - 1}
                        className={cn(
                            "p-3 rounded-lg border transition-colors",
                            currentIndex === flashcards.length - 1
                                ? "border-zinc-800 text-zinc-600 cursor-not-allowed"
                                : "border-zinc-700 hover:border-zinc-600 hover:bg-zinc-800"
                        )}
                    >
                        <ArrowRight className="w-5 h-5" />
                    </button>
                </div>

                {/* Completion */}
                {currentIndex === flashcards.length - 1 && isFlipped && (
                    <div className="mt-8 p-6 bg-green-500/10 border border-green-500/30 rounded-xl text-center">
                        <CheckCircle className="w-12 h-12 text-green-400 mx-auto mb-3" />
                        <p className="text-lg font-semibold text-green-400">Bra jobbat!</p>
                        <p className="text-zinc-400 text-sm">Du har gått igenom alla {flashcards.length} flashcards</p>
                        <button
                            onClick={restart}
                            className="mt-4 px-6 py-2 bg-green-500/20 hover:bg-green-500/30 border border-green-500/30 rounded-lg transition-colors"
                        >
                            Öva igen
                        </button>
                    </div>
                )}

                {/* Keyboard hint */}
                <p className="text-center text-zinc-600 text-xs mt-6">
                    Tips: Använd tangentbord - Space/Enter för att vända, ← → för navigering
                </p>
            </div>
        </div>
    )
}
