"use client"

/**
 * Omtenta V2 Flashcards - Linux Exam Prep
 * 
 * Features:
 * - 770 flashcards (7 ämnen × 110 kort)
 * - Topic selector (välj vilka ämnen)
 * - Card count: 100, 200, 300, 400, 500, 600, 700, ALLA
 * - Flip animation
 * - Progress tracking
 */

import * as React from "react"
import { useState, useEffect, useMemo, useCallback } from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    ArrowLeft, ArrowRight, RotateCcw, Play, Target, BookOpen,
    CheckSquare, Square, Eye, EyeOff, Shuffle, Trophy
} from "lucide-react"

// Import V2 flashcard data
import {
    OmtentaV2Flashcard,
    FlashcardTopic,
    FLASHCARD_TOPICS,
    FLASHCARD_COUNT_OPTIONS,
    FlashcardCountOption,
    getFlashcards,
    shuffleFlashcards
} from "@/data/omtenta-v2-flashcards"

type FlashcardPhase = 'setup' | 'study' | 'results'

export default function OmtentaV2FlashcardsPage() {
    // Setup state
    const [selectedTopics, setSelectedTopics] = useState<FlashcardTopic[]>([])
    const [cardCount, setCardCount] = useState<FlashcardCountOption>(100)

    // Study state
    const [phase, setPhase] = useState<FlashcardPhase>('setup')
    const [cards, setCards] = useState<OmtentaV2Flashcard[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)
    const [knownCards, setKnownCards] = useState<Set<number>>(new Set())
    const [unknownCards, setUnknownCards] = useState<Set<number>>(new Set())

    // Current card
    const currentCard = cards[currentIndex]
    const totalKnown = knownCards.size
    const totalUnknown = unknownCards.size
    const totalReviewed = totalKnown + totalUnknown

    // Start study session
    const startStudy = useCallback(() => {
        const flashcards = getFlashcards(selectedTopics, cardCount)
        setCards(flashcards)
        setCurrentIndex(0)
        setIsFlipped(false)
        setKnownCards(new Set())
        setUnknownCards(new Set())
        setPhase('study')
    }, [selectedTopics, cardCount])

    // Toggle topic selection
    const toggleTopic = (topicId: FlashcardTopic) => {
        setSelectedTopics(prev => 
            prev.includes(topicId)
                ? prev.filter(t => t !== topicId)
                : [...prev, topicId]
        )
    }

    // Select all topics
    const selectAllTopics = () => {
        setSelectedTopics(FLASHCARD_TOPICS.map(t => t.id))
    }

    // Clear all topics
    const clearAllTopics = () => {
        setSelectedTopics([])
    }

    // Flip card
    const flipCard = () => {
        setIsFlipped(!isFlipped)
    }

    // Mark as known
    const markKnown = () => {
        if (currentCard) {
            setKnownCards(prev => new Set([...prev, currentCard.id]))
            setUnknownCards(prev => {
                const newSet = new Set(prev)
                newSet.delete(currentCard.id)
                return newSet
            })
        }
        goToNext()
    }

    // Mark as unknown
    const markUnknown = () => {
        if (currentCard) {
            setUnknownCards(prev => new Set([...prev, currentCard.id]))
            setKnownCards(prev => {
                const newSet = new Set(prev)
                newSet.delete(currentCard.id)
                return newSet
            })
        }
        goToNext()
    }

    // Navigation
    const goToNext = () => {
        setIsFlipped(false)
        if (currentIndex < cards.length - 1) {
            setCurrentIndex(prev => prev + 1)
        } else {
            setPhase('results')
        }
    }

    const goToPrev = () => {
        setIsFlipped(false)
        if (currentIndex > 0) {
            setCurrentIndex(prev => prev - 1)
        }
    }

    // Restart
    const restartStudy = () => {
        setPhase('setup')
        setCards([])
        setCurrentIndex(0)
        setIsFlipped(false)
        setKnownCards(new Set())
        setUnknownCards(new Set())
    }

    // Study only unknown cards
    const studyUnknownOnly = () => {
        const unknownCardsList = cards.filter(c => unknownCards.has(c.id))
        if (unknownCardsList.length > 0) {
            setCards(shuffleFlashcards(unknownCardsList))
            setCurrentIndex(0)
            setIsFlipped(false)
            setKnownCards(new Set())
            setUnknownCards(new Set())
            setPhase('study')
        }
    }

    // Calculate available cards based on selection
    const availableCards = useMemo(() => {
        if (selectedTopics.length === 0) return 770
        return selectedTopics.reduce((sum, topicId) => {
            const topic = FLASHCARD_TOPICS.find(t => t.id === topicId)
            return sum + (topic?.count || 0)
        }, 0)
    }, [selectedTopics])

    // Keyboard navigation
    useEffect(() => {
        if (phase !== 'study') return

        const handleKeyDown = (e: KeyboardEvent) => {
            switch (e.key) {
                case ' ':
                case 'Enter':
                    e.preventDefault()
                    flipCard()
                    break
                case 'ArrowRight':
                    if (isFlipped) markKnown()
                    break
                case 'ArrowLeft':
                    if (isFlipped) markUnknown()
                    break
                case 'ArrowUp':
                    goToPrev()
                    break
                case 'ArrowDown':
                    goToNext()
                    break
            }
        }

        window.addEventListener('keydown', handleKeyDown)
        return () => window.removeEventListener('keydown', handleKeyDown)
    }, [phase, isFlipped, currentIndex])

    // SETUP PHASE
    if (phase === 'setup') {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4 md:p-8">
                <div className="max-w-4xl mx-auto">
                    {/* Header */}
                    <div className="mb-8">
                        <Link href="/study" className="inline-flex items-center gap-2 text-slate-400 hover:text-white mb-4 transition-colors">
                            <ArrowLeft className="w-4 h-4" />
                            Tillbaka till Study
                        </Link>
                        <h1 className="text-3xl md:text-4xl font-bold text-white mb-2">
                            🃏 Omtenta V2 - Flashcards
                        </h1>
                        <p className="text-slate-400">
                            770 flashcards • 7 ämnesområden • Snabb inlärning
                        </p>
                    </div>

                    {/* Topic Selection */}
                    <div className="bg-slate-800/50 rounded-2xl border border-slate-700 p-6 mb-6">
                        <div className="flex items-center justify-between mb-4">
                            <h2 className="text-xl font-semibold text-white flex items-center gap-2">
                                <BookOpen className="w-5 h-5 text-blue-400" />
                                Välj Ämnesområden
                            </h2>
                            <div className="flex gap-2">
                                <button
                                    onClick={selectAllTopics}
                                    className="px-3 py-1 text-sm bg-blue-500/20 text-blue-400 rounded-lg hover:bg-blue-500/30 transition-colors"
                                >
                                    Välj alla
                                </button>
                                <button
                                    onClick={clearAllTopics}
                                    className="px-3 py-1 text-sm bg-slate-700 text-slate-300 rounded-lg hover:bg-slate-600 transition-colors"
                                >
                                    Rensa
                                </button>
                            </div>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                            {FLASHCARD_TOPICS.map(topic => (
                                <button
                                    key={topic.id}
                                    onClick={() => toggleTopic(topic.id)}
                                    className={cn(
                                        "flex items-center gap-3 p-4 rounded-xl border-2 transition-all text-left",
                                        selectedTopics.includes(topic.id)
                                            ? "bg-blue-500/20 border-blue-500 text-white"
                                            : "bg-slate-700/50 border-slate-600 text-slate-300 hover:border-slate-500"
                                    )}
                                >
                                    {selectedTopics.includes(topic.id) ? (
                                        <CheckSquare className="w-5 h-5 text-blue-400 flex-shrink-0" />
                                    ) : (
                                        <Square className="w-5 h-5 text-slate-500 flex-shrink-0" />
                                    )}
                                    <div>
                                        <div className="font-medium">{topic.name}</div>
                                        <div className="text-sm text-slate-400">{topic.count} kort</div>
                                    </div>
                                </button>
                            ))}
                        </div>

                        <div className="mt-4 text-sm text-slate-400">
                            {selectedTopics.length === 0 ? (
                                <span>Alla ämnen valda (770 kort)</span>
                            ) : (
                                <span>{selectedTopics.length} ämne(n) valt • {availableCards} kort tillgängliga</span>
                            )}
                        </div>
                    </div>

                    {/* Card Count */}
                    <div className="bg-slate-800/50 rounded-2xl border border-slate-700 p-6 mb-6">
                        <h2 className="text-xl font-semibold text-white flex items-center gap-2 mb-4">
                            <Target className="w-5 h-5 text-green-400" />
                            Antal Kort
                        </h2>

                        <div className="flex flex-wrap gap-2">
                            {FLASHCARD_COUNT_OPTIONS.map(count => (
                                <button
                                    key={count}
                                    onClick={() => setCardCount(count)}
                                    disabled={count !== 'ALLA' && count > availableCards}
                                    className={cn(
                                        "px-4 py-2 rounded-xl font-medium transition-all",
                                        cardCount === count
                                            ? "bg-green-500 text-white"
                                            : count !== 'ALLA' && count > availableCards
                                            ? "bg-slate-700/30 text-slate-500 cursor-not-allowed"
                                            : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                                    )}
                                >
                                    {count === 'ALLA' ? 'ALLA' : count}
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Start Button */}
                    <button
                        onClick={startStudy}
                        className="w-full py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold text-xl rounded-2xl hover:from-purple-600 hover:to-pink-600 transition-all flex items-center justify-center gap-3"
                    >
                        <Play className="w-6 h-6" />
                        Börja Studera
                    </button>
                </div>
            </div>
        )
    }

    // STUDY PHASE
    if (phase === 'study' && currentCard) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4 md:p-8">
                <div className="max-w-2xl mx-auto">
                    {/* Top Bar */}
                    <div className="flex items-center justify-between mb-6">
                        <span className="text-slate-400">
                            Kort {currentIndex + 1} / {cards.length}
                        </span>
                        <div className="flex items-center gap-4">
                            <span className="text-green-400 text-sm">✓ {totalKnown}</span>
                            <span className="text-red-400 text-sm">✗ {totalUnknown}</span>
                        </div>
                    </div>

                    {/* Progress Bar */}
                    <div className="h-2 bg-slate-700 rounded-full mb-6 overflow-hidden">
                        <div 
                            className="h-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-300"
                            style={{ width: `${((currentIndex + 1) / cards.length) * 100}%` }}
                        />
                    </div>

                    {/* Topic Badge */}
                    <div className="flex justify-center mb-4">
                        <span className="px-3 py-1 bg-slate-700 rounded-lg text-sm text-slate-300">
                            {FLASHCARD_TOPICS.find(t => t.id === currentCard.topic)?.name || currentCard.topic}
                        </span>
                    </div>

                    {/* Flashcard */}
                    <div 
                        onClick={flipCard}
                        className="relative cursor-pointer perspective-1000 mb-6"
                        style={{ perspective: '1000px' }}
                    >
                        <motion.div
                            className="relative w-full min-h-[300px] md:min-h-[350px]"
                            animate={{ rotateY: isFlipped ? 180 : 0 }}
                            transition={{ duration: 0.5 }}
                            style={{ transformStyle: 'preserve-3d' }}
                        >
                            {/* Front (Question) */}
                            <div 
                                className={cn(
                                    "absolute inset-0 w-full h-full bg-gradient-to-br from-slate-800 to-slate-700 rounded-2xl border border-slate-600 p-8 flex flex-col items-center justify-center text-center",
                                    "backface-hidden"
                                )}
                                style={{ backfaceVisibility: 'hidden' }}
                            >
                                <div className="text-sm text-slate-400 mb-4 flex items-center gap-2">
                                    <Eye className="w-4 h-4" />
                                    Fråga
                                </div>
                                <h2 className="text-xl md:text-2xl font-semibold text-white">
                                    {currentCard.question}
                                </h2>
                                <div className="mt-6 text-slate-400 text-sm">
                                    Klicka eller tryck mellanslag för att vända
                                </div>
                            </div>

                            {/* Back (Answer) */}
                            <div 
                                className={cn(
                                    "absolute inset-0 w-full h-full bg-gradient-to-br from-purple-900/50 to-pink-900/50 rounded-2xl border border-purple-500/30 p-8 flex flex-col items-center justify-center text-center",
                                    "backface-hidden"
                                )}
                                style={{ 
                                    backfaceVisibility: 'hidden',
                                    transform: 'rotateY(180deg)'
                                }}
                            >
                                <div className="text-sm text-purple-300 mb-4 flex items-center gap-2">
                                    <EyeOff className="w-4 h-4" />
                                    Svar
                                </div>
                                <h2 className="text-2xl md:text-3xl font-bold text-white">
                                    {currentCard.answer}
                                </h2>
                            </div>
                        </motion.div>
                    </div>

                    {/* Action Buttons */}
                    {isFlipped && (
                        <div className="flex gap-4 mb-4">
                            <button
                                onClick={markUnknown}
                                className="flex-1 py-4 bg-red-500/20 hover:bg-red-500/30 text-red-400 font-bold rounded-xl transition-all flex items-center justify-center gap-2 border border-red-500/30"
                            >
                                ✗ Kunde inte
                            </button>
                            <button
                                onClick={markKnown}
                                className="flex-1 py-4 bg-green-500/20 hover:bg-green-500/30 text-green-400 font-bold rounded-xl transition-all flex items-center justify-center gap-2 border border-green-500/30"
                            >
                                ✓ Kunde
                            </button>
                        </div>
                    )}

                    {/* Navigation */}
                    <div className="flex justify-center gap-4">
                        <button
                            onClick={goToPrev}
                            disabled={currentIndex === 0}
                            className={cn(
                                "p-3 rounded-xl transition-all",
                                currentIndex === 0 
                                    ? "bg-slate-700/50 text-slate-500 cursor-not-allowed"
                                    : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                            )}
                        >
                            <ArrowLeft className="w-5 h-5" />
                        </button>
                        <button
                            onClick={flipCard}
                            className="px-6 py-3 bg-slate-700 text-slate-300 hover:bg-slate-600 rounded-xl transition-all flex items-center gap-2"
                        >
                            <Shuffle className="w-4 h-4" />
                            Vänd
                        </button>
                        <button
                            onClick={goToNext}
                            className="p-3 bg-slate-700 text-slate-300 hover:bg-slate-600 rounded-xl transition-all"
                        >
                            <ArrowRight className="w-5 h-5" />
                        </button>
                    </div>

                    {/* Keyboard hints */}
                    <div className="mt-6 text-center text-xs text-slate-500">
                        <span className="px-2 py-1 bg-slate-800 rounded">Space</span> Vänd • 
                        <span className="px-2 py-1 bg-slate-800 rounded mx-1">←</span> Kunde inte • 
                        <span className="px-2 py-1 bg-slate-800 rounded">→</span> Kunde
                    </div>
                </div>
            </div>
        )
    }

    // RESULTS PHASE
    if (phase === 'results') {
        const percentage = Math.round((totalKnown / cards.length) * 100) || 0

        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4 md:p-8">
                <div className="max-w-2xl mx-auto">
                    {/* Result Card */}
                    <div className="bg-slate-800/70 rounded-2xl border border-slate-700 p-8 text-center mb-6">
                        <div className="w-24 h-24 rounded-full mx-auto mb-6 flex items-center justify-center bg-purple-500/20">
                            <Trophy className="w-12 h-12 text-purple-400" />
                        </div>

                        <h1 className="text-3xl font-bold text-white mb-2">
                            Session Klar! 🎉
                        </h1>

                        <p className="text-slate-400 mb-6">
                            Du har gått igenom alla {cards.length} flashcards
                        </p>

                        {/* Score Display */}
                        <div className="flex justify-center gap-8 mb-8">
                            <div className="text-center">
                                <div className="text-4xl font-bold text-green-400">{totalKnown}</div>
                                <div className="text-sm text-slate-400">Kunde</div>
                            </div>
                            <div className="text-center">
                                <div className="text-4xl font-bold text-red-400">{totalUnknown}</div>
                                <div className="text-sm text-slate-400">Kunde inte</div>
                            </div>
                            <div className="text-center">
                                <div className="text-4xl font-bold text-purple-400">{percentage}%</div>
                                <div className="text-sm text-slate-400">Behärskning</div>
                            </div>
                        </div>

                        {/* Progress Bar */}
                        <div className="h-4 bg-slate-700 rounded-full overflow-hidden mb-8">
                            <div 
                                className="h-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-1000"
                                style={{ width: `${percentage}%` }}
                            />
                        </div>

                        {/* Action Buttons */}
                        <div className="flex flex-col sm:flex-row gap-4">
                            {totalUnknown > 0 && (
                                <button
                                    onClick={studyUnknownOnly}
                                    className="flex-1 py-3 bg-red-500/20 hover:bg-red-500/30 text-red-400 font-medium rounded-xl transition-all flex items-center justify-center gap-2 border border-red-500/30"
                                >
                                    <RotateCcw className="w-5 h-5" />
                                    Öva {totalUnknown} svåra
                                </button>
                            )}
                            <button
                                onClick={restartStudy}
                                className="flex-1 py-3 bg-slate-700 hover:bg-slate-600 text-white font-medium rounded-xl transition-all flex items-center justify-center gap-2"
                            >
                                <RotateCcw className="w-5 h-5" />
                                Ny Session
                            </button>
                            <Link
                                href="/study"
                                className="flex-1 py-3 bg-purple-500 hover:bg-purple-600 text-white font-medium rounded-xl transition-all flex items-center justify-center gap-2"
                            >
                                <ArrowLeft className="w-5 h-5" />
                                Tillbaka
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    return null
}
