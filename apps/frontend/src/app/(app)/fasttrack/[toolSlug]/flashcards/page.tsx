"use client"

/**
 * FastTrack Flashcards Page
 * Study flashcards for a specific tool
 */

import * as React from "react"
import { useState, useEffect, Suspense } from "react"
import { useParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle, Star, X } from "lucide-react"
import { TOOLS_DATA } from "../../page"
import { FASTTRACK_FLASHCARDS } from "@/data/fasttrack-flashcards"

function FlashcardsContent() {
    const params = useParams()
    const toolSlug = params?.toolSlug as string

    const tool = TOOLS_DATA.find(t => t.slug === toolSlug)
    const flashcards = FASTTRACK_FLASHCARDS[toolSlug] || []

    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)

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

    if (!tool || flashcards.length === 0) {
        return (
            <div className="min-h-screen bg-zinc-950 text-white p-8">
                <div className="max-w-2xl mx-auto text-center py-20">
                    <p className="text-zinc-400 mb-4">
                        Inga flashcards tillgängliga för detta verktyg ännu
                    </p>
                    <Link href="/fasttrack" className="text-amber-400 hover:text-amber-300">
                        ← Tillbaka till FastTrack
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
                        href={`/fasttrack/${toolSlug}`}
                        className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4"
                    >
                        ← Tillbaka till {tool.name}
                    </Link>
                    <div className="flex items-center justify-between">
                        <div>
                            <h1 className="text-2xl font-bold flex items-center gap-2">
                                <span>{tool.icon}</span>
                                {tool.name} Flashcards
                            </h1>
                            <p className="text-zinc-400">
                                Kort {currentIndex + 1} av {flashcards.length}
                            </p>
                        </div>
                    </div>
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
                    className="relative w-full aspect-[4/3] cursor-pointer mb-8"
                >
                    <div
                        className={cn(
                            "absolute inset-0 rounded-2xl p-8",
                            "bg-gradient-to-br from-purple-600/30 to-purple-900/30",
                            "border border-purple-500/30",
                            "flex flex-col items-center justify-center",
                            "transition-all duration-500",
                            isFlipped && "opacity-0 pointer-events-none"
                        )}
                    >
                        <p className="text-sm text-purple-400 mb-4">Fråga</p>
                        <p className="text-xl text-center font-medium">{currentCard.front}</p>
                        <p className="text-sm text-zinc-500 mt-6">Klicka för att vända kortet</p>
                    </div>

                    <div
                        className={cn(
                            "absolute inset-0 rounded-2xl p-8",
                            "bg-gradient-to-br from-emerald-600/30 to-emerald-900/30",
                            "border border-emerald-500/30",
                            "flex flex-col items-center justify-center",
                            "transition-all duration-500",
                            !isFlipped && "opacity-0 pointer-events-none"
                        )}
                    >
                        <p className="text-sm text-emerald-400 mb-4">Svar</p>
                        <p className="text-lg text-center">{currentCard.back}</p>
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
                            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 transition-colors"
                        >
                            Nästa
                            <ArrowRight className="w-4 h-4" />
                        </button>
                    ) : (
                        <Link
                            href={`/fasttrack/${toolSlug}`}
                            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 transition-colors"
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

export default function FastTrackFlashcardsPage() {
    return (
        <Suspense fallback={
            <div className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-purple-500" />
            </div>
        }>
            <FlashcardsContent />
        </Suspense>
    )
}
