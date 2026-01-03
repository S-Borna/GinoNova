"use client"

/**
 * Flashcards Study Mode
 *
 * Simple flip-card interface for memorization
 * With star/favorite functionality
 * Now uses local data instead of API
 */

import * as React from "react"
import { useState, useEffect, Suspense, useMemo } from "react"
import { useParams, useSearchParams } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle, Star, X, Shuffle } from "lucide-react"
import { useFavorites } from "@/hooks/useFavorites"

// Import local flashcard data
import { DOE25_TASK_FLASHCARDS, getAllDOE25Flashcards, type TaskFlashcard } from "@/data/doe25-task-flashcards"
import { LINUX247_TASK_FLASHCARDS, getAllFlashcards as getAllLinux247Flashcards } from "@/data/linux247-task-flashcards"

interface Flashcard {
    id: string
    front: string
    back: string
    module_slug: string
    lesson_title: string
    category?: string
    difficulty?: string
}

// Module configuration - slugs match URL paths
const MODULE_CONFIG: Record<string, { title: string; data: typeof DOE25_TASK_FLASHCARDS }> = {
    'doe25-tenta': { title: 'DOE25 Tentaplugg', data: DOE25_TASK_FLASHCARDS },
    'linux-247': { title: 'Linux 24/7', data: LINUX247_TASK_FLASHCARDS },
}

function FlashcardsContent() {
    const params = useParams()
    const searchParams = useSearchParams()
    const moduleSlug = params?.moduleSlug as string || ""

    const [flashcards, setFlashcards] = useState<Flashcard[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [moduleTitle, setModuleTitle] = useState("")
    const [isShuffled, setIsShuffled] = useState(false)

    // Star modal
    const [showStarModal, setShowStarModal] = useState(false)
    const [starName, setStarName] = useState("")

    // Favorites hook
    const { addFavorite, removeFavorite, isFavorite, getFavoriteId } = useFavorites()

    // Load flashcards from local data
    useEffect(() => {
        loadLocalFlashcards()
    }, [moduleSlug])

    function loadLocalFlashcards() {
        try {
            setLoading(true)
            setError(null)

            // Get shuffle preference from URL
            const shouldShuffle = searchParams?.get("shuffle") === "true"
            const tasksFilter = searchParams?.get("tasks") || "" // Comma-separated task IDs
            setIsShuffled(shouldShuffle)

            // Get module config
            const config = MODULE_CONFIG[moduleSlug]
            if (!config) {
                setError(`Modul "${moduleSlug}" hittades inte`)
                setLoading(false)
                return
            }

            setModuleTitle(config.title)

            // Collect flashcards - either all or filtered by tasks
            let allFlashcards: Flashcard[] = []
            const selectedTaskIds = tasksFilter ? tasksFilter.split(',') : []

            if (selectedTaskIds.length > 0) {
                // Get flashcards for selected tasks only
                config.data.forEach(taskSet => {
                    if (selectedTaskIds.includes(taskSet.taskId)) {
                        taskSet.flashcards.forEach(fc => {
                            allFlashcards.push({
                                id: fc.id,
                                front: fc.front,
                                back: fc.back,
                                module_slug: moduleSlug,
                                lesson_title: taskSet.taskTitle,
                                category: fc.category,
                                difficulty: fc.difficulty
                            })
                        })
                    }
                })
            } else {
                // Get all flashcards for module
                config.data.forEach(taskSet => {
                    taskSet.flashcards.forEach(fc => {
                        allFlashcards.push({
                            id: fc.id,
                            front: fc.front,
                            back: fc.back,
                            module_slug: moduleSlug,
                            lesson_title: taskSet.taskTitle,
                            category: fc.category,
                            difficulty: fc.difficulty
                        })
                    })
                })
            }

            // Shuffle if requested
            if (shouldShuffle) {
                allFlashcards = shuffleArray([...allFlashcards])
            }

            setFlashcards(allFlashcards)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Error loading flashcards")
        } finally {
            setLoading(false)
        }
    }

    function shuffleArray<T>(array: T[]): T[] {
        const shuffled = [...array]
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
        }
        return shuffled
    }

    function handleShuffle() {
        setFlashcards(prev => shuffleArray([...prev]))
        setCurrentIndex(0)
        setIsFlipped(false)
        setIsShuffled(true)
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
                        ← Tillbaka till Studyroom
                    </Link>
                </div>
            </div>
        )
    }

    const currentCard = flashcards[currentIndex]
    const progress = ((currentIndex + 1) / flashcards.length) * 100
    const isCurrentFavorite = currentCard ? isFavorite(moduleSlug, currentCard.front, "flashcard") : false

    function handleStarClick() {
        if (isCurrentFavorite) {
            const favId = getFavoriteId(moduleSlug, currentCard.front, "flashcard")
            if (favId) removeFavorite(favId)
        } else {
            setShowStarModal(true)
            setStarName("")
        }
    }

    function handleSaveStar() {
        if (!starName.trim()) return
        addFavorite({
            type: "flashcard",
            customName: starName.slice(0, 6),
            moduleSlug,
            moduleTitle,
            originalQuestion: currentCard.front
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
                        <div>
                            <h1 className="text-2xl font-bold">{moduleTitle}</h1>
                            <p className="text-zinc-400">
                                Flashcard {currentIndex + 1} av {flashcards.length}
                            </p>
                        </div>
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

                    <div className="flex items-center gap-2">
                        <button
                            onClick={handleShuffle}
                            className={cn(
                                "p-2 rounded-lg transition-colors",
                                isShuffled
                                    ? "bg-purple-600/30 text-purple-400"
                                    : "bg-zinc-800 hover:bg-zinc-700"
                            )}
                            title="Blanda kort"
                        >
                            <Shuffle className="w-5 h-5" />
                        </button>
                        <button
                            onClick={resetCards}
                            className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 transition-colors"
                            title="Börja om"
                        >
                            <RotateCcw className="w-5 h-5" />
                        </button>
                    </div>

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
                            placeholder="Ex: K8sPod"
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

export default function FlashcardsPage() {
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
