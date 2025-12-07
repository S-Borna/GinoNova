"use client"

/**
 * Flashcards Study Mode
 *
 * Simple flip-card interface for memorization
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useParams, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle } from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

interface Flashcard {
    id: string
    front: string
    back: string
    module_slug: string
    lesson_title: string
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

    useEffect(() => {
        fetchFlashcards()
    }, [moduleSlug])

    async function fetchFlashcards() {
        try {
            setLoading(true)

            // Get lessons and shuffle params
            const lessons = searchParams?.get("lessons") || ""
            const shuffle = searchParams?.get("shuffle") === "true"

            const url = new URL(`${API_BASE_URL}/api/study/modules/${moduleSlug}/flashcards`)
            if (lessons) url.searchParams.set("lessons", lessons)
            if (shuffle) url.searchParams.set("shuffle", "true")

            const res = await fetch(url.toString())
            if (!res.ok) throw new Error("Failed to fetch flashcards")

            const data = await res.json()
            setFlashcards(data.flashcards)

            // Get module title
            const moduleRes = await fetch(`${API_BASE_URL}/api/study/modules/${moduleSlug}`)
            if (moduleRes.ok) {
                const moduleData = await moduleRes.json()
                setModuleTitle(moduleData.title)
            }
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading flashcards")
        } finally {
            setLoading(false)
        }
    }

    function nextCard() {
        if (currentIndex < flashcards.length - 1) {
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

    function resetCards() {
        setCurrentIndex(0)
        setIsFlipped(false)
    }

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
                <div className="max-w-2xl mx-auto text-center py-20">
                    <p className="text-zinc-400 mb-4">
                        {error || "Inga flashcards tillgängliga för denna modul"}
                    </p>
                    <Link
                        href="/study"
                        className="text-purple-400 hover:text-purple-300"
                    >
                        ← Tillbaka till Study
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
                <div className="mb-6">
                    <Link
                        href="/study"
                        prefetch={false}
                        className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4"
                    >
                        ← Tillbaka
                    </Link>
                    <h1 className="text-2xl font-bold">{moduleTitle}</h1>
                    <p className="text-zinc-400">
                        Flashcard {currentIndex + 1} av {flashcards.length}
                    </p>
                </div>

                {/* Progress Bar */}
                <div className="w-full h-1 bg-zinc-800 rounded-full mb-8">
                    <div
                        className="h-full bg-purple-500 rounded-full transition-all duration-300"
                        style={{ width: `${progress}%` }}
                    />
                </div>

                {/* Flashcard */}
                <div
                    onClick={() => setIsFlipped(!isFlipped)}
                    className={cn(
                        "relative w-full aspect-[4/3] cursor-pointer perspective-1000",
                        "mb-8"
                    )}
                >
                    <div
                        className={cn(
                            "absolute inset-0 rounded-2xl p-8",
                            "bg-gradient-to-br from-purple-600/30 to-purple-900/30",
                            "border border-purple-500/30",
                            "flex flex-col items-center justify-center",
                            "transition-all duration-500 transform-style-3d",
                            isFlipped && "rotate-y-180 opacity-0"
                        )}
                    >
                        <p className="text-sm text-purple-400 mb-4">Fråga</p>
                        <p className="text-xl text-center font-medium">
                            {currentCard.front}
                        </p>
                        <p className="text-sm text-zinc-500 mt-6">
                            Klicka för att vända kortet
                        </p>
                    </div>

                    <div
                        className={cn(
                            "absolute inset-0 rounded-2xl p-8",
                            "bg-gradient-to-br from-emerald-600/30 to-emerald-900/30",
                            "border border-emerald-500/30",
                            "flex flex-col items-center justify-center",
                            "transition-all duration-500 transform-style-3d",
                            !isFlipped && "rotate-y-180 opacity-0"
                        )}
                    >
                        <p className="text-sm text-emerald-400 mb-4">Svar</p>
                        <p className="text-lg text-center">
                            {currentCard.back}
                        </p>
                        <p className="text-xs text-zinc-500 mt-6">
                            {currentCard.lesson_title}
                        </p>
                    </div>
                </div>

                {/* Navigation */}
                <div className="flex items-center justify-between">
                    <button
                        onClick={prevCard}
                        disabled={currentIndex === 0}
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-lg",
                            "bg-zinc-800 hover:bg-zinc-700 transition-colors",
                            currentIndex === 0 && "opacity-50 cursor-not-allowed"
                        )}
                    >
                        <ArrowLeft className="w-4 h-4" />
                        Föregående
                    </button>

                    <button
                        onClick={resetCards}
                        className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 transition-colors"
                        title="Börja om"
                    >
                        <RotateCcw className="w-5 h-5" />
                    </button>

                    {currentIndex < flashcards.length - 1 ? (
                        <button
                            onClick={nextCard}
                            className={cn(
                                "flex items-center gap-2 px-4 py-2 rounded-lg",
                                "bg-purple-600 hover:bg-purple-500 transition-colors"
                            )}
                        >
                            Nästa
                            <ArrowRight className="w-4 h-4" />
                        </button>
                    ) : (
                        <Link
                            href="/study"
                            prefetch={false}
                            className={cn(
                                "flex items-center gap-2 px-4 py-2 rounded-lg",
                                "bg-emerald-600 hover:bg-emerald-500 transition-colors"
                            )}
                        >
                            <CheckCircle className="w-4 h-4" />
                            Klar!
                        </Link>
                    )}
                </div>
            </div>
        </div>
    )
}
