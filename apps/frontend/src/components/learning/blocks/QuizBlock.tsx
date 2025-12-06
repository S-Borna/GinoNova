"use client"

/**
 * ============================================================================
 * QUIZ BLOCK - Flashcards + Multiple Choice Questions
 * ============================================================================
 * 
 * Features:
 * - Flashcard deck with flip animation
 * - Multiple choice questions
 * - Score tracking
 * - Pass/fail based on percentage
 */

import { useState, useMemo } from "react"
import { cn } from "@saas/ui"
import { 
    HelpCircle,
    CheckCircle2, 
    XCircle,
    RotateCcw,
    ChevronLeft,
    ChevronRight,
    Lightbulb,
    Trophy
} from "lucide-react"
import { Button } from "@/components/ui/button"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Flashcard {
    term: string
    definition: string
}

interface MultipleChoiceQuestion {
    question: string
    options: string[]
    correctAnswer: number
    explanation: string
}

interface QuizBlockProps {
    flashcards?: Flashcard[]
    questions: MultipleChoiceQuestion[]
    passingScore?: number // Percentage required to pass (default 80)
    onComplete?: (passed: boolean, score: number) => void
}

/* ============================================================================
   FLASHCARD COMPONENT
   ============================================================================ */

function FlashcardDeck({ cards }: { cards: Flashcard[] }) {
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)
    const [knownCards, setKnownCards] = useState<Set<number>>(new Set())

    const shuffledCards = useMemo(() => {
        return [...cards].sort(() => Math.random() - 0.5)
    }, [cards])

    const currentCard = shuffledCards[currentIndex]
    const progress = (knownCards.size / cards.length) * 100

    const handleNext = () => {
        setIsFlipped(false)
        setTimeout(() => {
            setCurrentIndex((prev) => (prev + 1) % shuffledCards.length)
        }, 150)
    }

    const handlePrev = () => {
        setIsFlipped(false)
        setTimeout(() => {
            setCurrentIndex((prev) => (prev - 1 + shuffledCards.length) % shuffledCards.length)
        }, 150)
    }

    const handleMarkKnown = () => {
        setKnownCards(prev => new Set([...prev, currentIndex]))
        handleNext()
    }

    const handleReset = () => {
        setCurrentIndex(0)
        setIsFlipped(false)
        setKnownCards(new Set())
    }

    return (
        <div className="space-y-4">
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                    <Lightbulb className="w-5 h-5 text-amber-400" />
                    <h4 className="font-semibold text-white">Flashcards</h4>
                </div>
                <span className="text-sm text-zinc-400">
                    {knownCards.size} av {cards.length} lärda
                </span>
            </div>

            {/* Progress bar */}
            <div className="h-2 bg-zinc-700 rounded-full overflow-hidden">
                <div 
                    className="h-full bg-amber-500 transition-all duration-300"
                    style={{ width: `${progress}%` }}
                />
            </div>

            {/* Card */}
            <div 
                onClick={() => setIsFlipped(!isFlipped)}
                className={cn(
                    "relative h-48 cursor-pointer perspective-1000",
                    "transition-transform duration-500 transform-style-preserve-3d",
                    isFlipped && "rotate-y-180"
                )}
                style={{
                    perspective: "1000px",
                    transformStyle: "preserve-3d",
                    transform: isFlipped ? "rotateY(180deg)" : "rotateY(0deg)"
                }}
            >
                {/* Front */}
                <div 
                    className={cn(
                        "absolute inset-0 backface-hidden",
                        "bg-gradient-to-br from-amber-900/30 to-amber-800/20",
                        "border border-amber-500/30 rounded-xl",
                        "flex items-center justify-center p-6",
                        "text-center"
                    )}
                    style={{ backfaceVisibility: "hidden" }}
                >
                    <div>
                        <span className="text-xs text-amber-400 mb-2 block">TERM</span>
                        <p className="text-xl font-semibold text-white">
                            {currentCard?.term}
                        </p>
                        <span className="text-xs text-zinc-500 mt-4 block">
                            Klicka för att vända
                        </span>
                    </div>
                </div>

                {/* Back */}
                <div 
                    className={cn(
                        "absolute inset-0 backface-hidden",
                        "bg-gradient-to-br from-emerald-900/30 to-emerald-800/20",
                        "border border-emerald-500/30 rounded-xl",
                        "flex items-center justify-center p-6",
                        "text-center"
                    )}
                    style={{ 
                        backfaceVisibility: "hidden",
                        transform: "rotateY(180deg)"
                    }}
                >
                    <div>
                        <span className="text-xs text-emerald-400 mb-2 block">DEFINITION</span>
                        <p className="text-white">
                            {currentCard?.definition}
                        </p>
                    </div>
                </div>
            </div>

            {/* Navigation */}
            <div className="flex items-center justify-between">
                <Button
                    variant="ghost"
                    size="sm"
                    onClick={handlePrev}
                    disabled={shuffledCards.length <= 1}
                >
                    <ChevronLeft className="w-4 h-4 mr-1" />
                    Föregående
                </Button>
                
                <span className="text-sm text-zinc-400">
                    {currentIndex + 1} / {shuffledCards.length}
                </span>

                <Button
                    variant="ghost"
                    size="sm"
                    onClick={handleNext}
                    disabled={shuffledCards.length <= 1}
                >
                    Nästa
                    <ChevronRight className="w-4 h-4 ml-1" />
                </Button>
            </div>

            {/* Actions */}
            <div className="flex gap-3 justify-center">
                <Button
                    variant="outline"
                    size="sm"
                    onClick={handleMarkKnown}
                    className="text-emerald-400 border-emerald-500/30"
                >
                    <CheckCircle2 className="w-4 h-4 mr-2" />
                    Kan detta
                </Button>
                <Button
                    variant="outline"
                    size="sm"
                    onClick={handleReset}
                    className="text-zinc-400"
                >
                    <RotateCcw className="w-4 h-4 mr-2" />
                    Börja om
                </Button>
            </div>
        </div>
    )
}

/* ============================================================================
   MULTIPLE CHOICE COMPONENT
   ============================================================================ */

function MultipleChoice({ 
    questions, 
    passingScore = 80,
    onComplete 
}: { 
    questions: MultipleChoiceQuestion[]
    passingScore: number
    onComplete?: (passed: boolean, score: number) => void
}) {
    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedOption, setSelectedOption] = useState<number | null>(null)
    const [showResult, setShowResult] = useState(false)
    const [answers, setAnswers] = useState<{ selected: number; correct: boolean }[]>([])
    const [quizComplete, setQuizComplete] = useState(false)

    const currentQuestion = questions[currentIndex]
    const score = answers.filter(a => a.correct).length
    const scorePercent = Math.round((score / questions.length) * 100)
    const passed = scorePercent >= passingScore

    const handleSelect = (optionIndex: number) => {
        if (showResult) return
        setSelectedOption(optionIndex)
    }

    const handleSubmit = () => {
        if (selectedOption === null) return
        
        const isCorrect = selectedOption === currentQuestion.correctAnswer
        setAnswers([...answers, { selected: selectedOption, correct: isCorrect }])
        setShowResult(true)
    }

    const handleNext = () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(currentIndex + 1)
            setSelectedOption(null)
            setShowResult(false)
        } else {
            setQuizComplete(true)
            onComplete?.(passed, scorePercent)
        }
    }

    const handleRetry = () => {
        setCurrentIndex(0)
        setSelectedOption(null)
        setShowResult(false)
        setAnswers([])
        setQuizComplete(false)
    }

    if (quizComplete) {
        return (
            <div className={cn(
                "rounded-xl p-8 text-center",
                passed 
                    ? "bg-emerald-900/20 border border-emerald-500/30"
                    : "bg-red-900/20 border border-red-500/30"
            )}>
                <div className={cn(
                    "w-20 h-20 rounded-full mx-auto mb-4",
                    "flex items-center justify-center",
                    passed ? "bg-emerald-500/20" : "bg-red-500/20"
                )}>
                    {passed ? (
                        <Trophy className="w-10 h-10 text-emerald-400" />
                    ) : (
                        <XCircle className="w-10 h-10 text-red-400" />
                    )}
                </div>
                
                <h4 className="text-2xl font-bold text-white mb-2">
                    {passed ? "Bra jobbat!" : "Försök igen"}
                </h4>
                
                <p className="text-3xl font-bold mb-2">
                    <span className={passed ? "text-emerald-400" : "text-red-400"}>
                        {scorePercent}%
                    </span>
                </p>
                
                <p className="text-zinc-400 mb-6">
                    {score} av {questions.length} rätt
                    {!passed && ` (${passingScore}% krävs för att klara)`}
                </p>

                {!passed && (
                    <Button onClick={handleRetry} className="bg-purple-600 hover:bg-purple-700">
                        <RotateCcw className="w-4 h-4 mr-2" />
                        Försök igen
                    </Button>
                )}
            </div>
        )
    }

    return (
        <div className="space-y-6">
            {/* Progress */}
            <div className="flex items-center justify-between mb-2">
                <span className="text-sm text-zinc-400">
                    Fråga {currentIndex + 1} av {questions.length}
                </span>
                <span className="text-sm text-zinc-400">
                    {score} rätt hittills
                </span>
            </div>
            
            <div className="flex gap-1">
                {questions.map((_, index) => (
                    <div
                        key={index}
                        className={cn(
                            "h-1.5 flex-1 rounded-full",
                            index < answers.length
                                ? answers[index]?.correct
                                    ? "bg-emerald-500"
                                    : "bg-red-500"
                                : index === currentIndex
                                    ? "bg-purple-500"
                                    : "bg-zinc-700"
                        )}
                    />
                ))}
            </div>

            {/* Question */}
            <div className={cn(
                "bg-zinc-800/50 border border-zinc-700/50",
                "rounded-xl p-6"
            )}>
                <div className="flex items-start gap-3 mb-6">
                    <HelpCircle className="w-6 h-6 text-purple-400 flex-shrink-0" />
                    <p className="text-lg text-white">{currentQuestion.question}</p>
                </div>

                {/* Options */}
                <div className="space-y-3">
                    {currentQuestion.options.map((option, index) => {
                        const isSelected = selectedOption === index
                        const isCorrect = index === currentQuestion.correctAnswer
                        
                        let optionStyle = "bg-zinc-700/50 border-zinc-600 hover:border-purple-500"
                        
                        if (showResult) {
                            if (isCorrect) {
                                optionStyle = "bg-emerald-900/30 border-emerald-500"
                            } else if (isSelected && !isCorrect) {
                                optionStyle = "bg-red-900/30 border-red-500"
                            }
                        } else if (isSelected) {
                            optionStyle = "bg-purple-900/30 border-purple-500"
                        }

                        return (
                            <button
                                key={index}
                                onClick={() => handleSelect(index)}
                                disabled={showResult}
                                className={cn(
                                    "w-full p-4 rounded-lg border text-left",
                                    "transition-all duration-200",
                                    optionStyle
                                )}
                            >
                                <div className="flex items-center gap-3">
                                    <span className={cn(
                                        "w-8 h-8 rounded-full flex items-center justify-center",
                                        "text-sm font-medium",
                                        showResult && isCorrect
                                            ? "bg-emerald-500 text-white"
                                            : showResult && isSelected && !isCorrect
                                                ? "bg-red-500 text-white"
                                                : isSelected
                                                    ? "bg-purple-500 text-white"
                                                    : "bg-zinc-600 text-zinc-300"
                                    )}>
                                        {String.fromCharCode(65 + index)}
                                    </span>
                                    <span className="text-zinc-200">{option}</span>
                                    {showResult && isCorrect && (
                                        <CheckCircle2 className="w-5 h-5 text-emerald-400 ml-auto" />
                                    )}
                                    {showResult && isSelected && !isCorrect && (
                                        <XCircle className="w-5 h-5 text-red-400 ml-auto" />
                                    )}
                                </div>
                            </button>
                        )
                    })}
                </div>

                {/* Explanation */}
                {showResult && (
                    <div className={cn(
                        "mt-6 p-4 rounded-lg",
                        "bg-purple-900/20 border border-purple-500/30"
                    )}>
                        <div className="flex items-start gap-2">
                            <Lightbulb className="w-5 h-5 text-purple-400 flex-shrink-0 mt-0.5" />
                            <p className="text-sm text-zinc-300">
                                {currentQuestion.explanation}
                            </p>
                        </div>
                    </div>
                )}
            </div>

            {/* Actions */}
            <div className="flex justify-end">
                {!showResult ? (
                    <Button
                        onClick={handleSubmit}
                        disabled={selectedOption === null}
                        className="bg-purple-600 hover:bg-purple-700"
                    >
                        Svara
                    </Button>
                ) : (
                    <Button
                        onClick={handleNext}
                        className="bg-purple-600 hover:bg-purple-700"
                    >
                        {currentIndex < questions.length - 1 ? "Nästa fråga" : "Se resultat"}
                        <ChevronRight className="w-4 h-4 ml-2" />
                    </Button>
                )}
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN QUIZ BLOCK
   ============================================================================ */

export function QuizBlock({
    flashcards,
    questions,
    passingScore = 80,
    onComplete
}: QuizBlockProps) {
    const [activeTab, setActiveTab] = useState<"flashcards" | "quiz">(
        flashcards && flashcards.length > 0 ? "flashcards" : "quiz"
    )

    return (
        <div className="space-y-6">
            {/* Header */}
            <div className="flex items-center gap-2">
                <HelpCircle className="w-5 h-5 text-purple-400" />
                <h3 className="text-lg font-semibold text-white">
                    Quiz - Testa din kunskap
                </h3>
            </div>

            {/* Tabs */}
            {flashcards && flashcards.length > 0 && (
                <div className="flex gap-2 border-b border-zinc-700 pb-2">
                    <button
                        onClick={() => setActiveTab("flashcards")}
                        className={cn(
                            "px-4 py-2 rounded-t-lg text-sm font-medium transition-colors",
                            activeTab === "flashcards"
                                ? "bg-amber-900/30 text-amber-400 border-b-2 border-amber-400"
                                : "text-zinc-400 hover:text-white"
                        )}
                    >
                        📇 Flashcards ({flashcards.length})
                    </button>
                    <button
                        onClick={() => setActiveTab("quiz")}
                        className={cn(
                            "px-4 py-2 rounded-t-lg text-sm font-medium transition-colors",
                            activeTab === "quiz"
                                ? "bg-purple-900/30 text-purple-400 border-b-2 border-purple-400"
                                : "text-zinc-400 hover:text-white"
                        )}
                    >
                        ❓ Flervalsfrågor ({questions.length})
                    </button>
                </div>
            )}

            {/* Content */}
            {activeTab === "flashcards" && flashcards && flashcards.length > 0 ? (
                <FlashcardDeck cards={flashcards} />
            ) : (
                <MultipleChoice 
                    questions={questions}
                    passingScore={passingScore}
                    onComplete={onComplete}
                />
            )}
        </div>
    )
}

export default QuizBlock
