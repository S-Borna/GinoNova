"use client"

/**
 * Omtenta V2 Quiz - Linux Exam Prep
 *
 * Features:
 * - 770 frågor (7 ämnen × 110 frågor)
 * - Topic selector (välj vilka ämnen)
 * - Question count: 100, 200, 300, 400, 500, 600, 700, ALLA
 * - Multi-select support för frågor med flera rätta svar
 * - Timer och poängräkning
 */

import * as React from "react"
import { useState, useEffect, useMemo, useCallback } from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    ArrowLeft, ArrowRight, Clock, CheckCircle, XCircle,
    Trophy, Brain, RotateCcw, Play, Target, BookOpen,
    CheckSquare, Square
} from "lucide-react"

// Import V2 quiz data
import {
    OmtentaV2Question,
    OmtentaV2Topic,
    OMTENTA_V2_TOPICS,
    QUESTION_COUNT_OPTIONS,
    QuestionCountOption,
    getQuizQuestions,
    isMultiSelectQuestion,
    checkAnswer,
    shuffleArray
} from "@/data/omtenta-v2-quiz"

type QuizPhase = 'setup' | 'quiz' | 'results'

interface QuizResult {
    questionId: string
    correct: boolean
    selectedIndices: number[]
    correctIndices: number[]
    timeSpent: number
}

export default function OmtentaV2Page() {
    // Setup state
    const [selectedTopics, setSelectedTopics] = useState<OmtentaV2Topic[]>([])
    const [questionCount, setQuestionCount] = useState<QuestionCountOption>(100)
    const [timedMode, setTimedMode] = useState(true)
    const [duration, setDuration] = useState(60) // minutes

    // Quiz state
    const [phase, setPhase] = useState<QuizPhase>('setup')
    const [questions, setQuestions] = useState<OmtentaV2Question[]>([])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [selectedAnswers, setSelectedAnswers] = useState<number[]>([])
    const [results, setResults] = useState<QuizResult[]>([])
    const [timeRemaining, setTimeRemaining] = useState(0)
    const [questionStartTime, setQuestionStartTime] = useState(0)
    const [showFeedback, setShowFeedback] = useState(false)
    const [hasAnswered, setHasAnswered] = useState(false)

    // Current question
    const currentQuestion = questions[currentIndex]
    const isMultiSelect = currentQuestion ? isMultiSelectQuestion(currentQuestion) : false
    const correctCount = results.filter(r => r.correct).length
    const totalAnswered = results.length

    // Timer effect
    useEffect(() => {
        if (phase !== 'quiz' || !timedMode || timeRemaining <= 0) return

        const timer = setInterval(() => {
            setTimeRemaining(prev => {
                if (prev <= 1) {
                    // Time's up - end quiz
                    setPhase('results')
                    return 0
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(timer)
    }, [phase, timedMode, timeRemaining])

    // Start quiz
    const startQuiz = useCallback(() => {
        const quizQuestions = getQuizQuestions(selectedTopics, questionCount)

        // Shuffle options within each question
        const preparedQuestions = quizQuestions.map(q => {
            const optionsWithIndex = q.options.map((opt, idx) => ({
                option: opt,
                originalIndex: idx
            }))
            const shuffled = shuffleArray(optionsWithIndex)

            // Map old indices to new indices for correctIndices
            const indexMap = new Map<number, number>()
            shuffled.forEach((item, newIdx) => {
                indexMap.set(item.originalIndex, newIdx)
            })

            return {
                ...q,
                options: shuffled.map(item => item.option),
                correctIndices: q.correctIndices.map(oldIdx => indexMap.get(oldIdx)!)
            }
        })

        setQuestions(preparedQuestions)
        setCurrentIndex(0)
        setSelectedAnswers([])
        setResults([])
        setTimeRemaining(timedMode ? duration * 60 : 0)
        setQuestionStartTime(Date.now())
        setShowFeedback(false)
        setHasAnswered(false)
        setPhase('quiz')
    }, [selectedTopics, questionCount, timedMode, duration])

    // Toggle topic selection
    const toggleTopic = (topicId: OmtentaV2Topic) => {
        setSelectedTopics(prev =>
            prev.includes(topicId)
                ? prev.filter(t => t !== topicId)
                : [...prev, topicId]
        )
    }

    // Select all topics
    const selectAllTopics = () => {
        setSelectedTopics(OMTENTA_V2_TOPICS.map(t => t.id))
    }

    // Clear all topics
    const clearAllTopics = () => {
        setSelectedTopics([])
    }

    // Toggle answer selection (for multi-select)
    const toggleAnswer = (index: number) => {
        if (hasAnswered) return

        if (isMultiSelect) {
            setSelectedAnswers(prev =>
                prev.includes(index)
                    ? prev.filter(i => i !== index)
                    : [...prev, index]
            )
        } else {
            setSelectedAnswers([index])
        }
    }

    // Submit answer
    const submitAnswer = () => {
        if (selectedAnswers.length === 0 || hasAnswered) return

        const timeSpent = Date.now() - questionStartTime
        const isCorrect = checkAnswer(currentQuestion, selectedAnswers)

        setResults(prev => [...prev, {
            questionId: currentQuestion.id,
            correct: isCorrect,
            selectedIndices: [...selectedAnswers],
            correctIndices: currentQuestion.correctIndices,
            timeSpent
        }])

        setShowFeedback(true)
        setHasAnswered(true)
    }

    // Next question
    const nextQuestion = () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1)
            setSelectedAnswers([])
            setShowFeedback(false)
            setHasAnswered(false)
            setQuestionStartTime(Date.now())
        } else {
            setPhase('results')
        }
    }

    // Restart quiz
    const restartQuiz = () => {
        setPhase('setup')
        setQuestions([])
        setCurrentIndex(0)
        setSelectedAnswers([])
        setResults([])
    }

    // Format time
    const formatTime = (seconds: number) => {
        const mins = Math.floor(seconds / 60)
        const secs = seconds % 60
        return `${mins}:${secs.toString().padStart(2, '0')}`
    }

    // Calculate available questions based on selection
    const availableQuestions = useMemo(() => {
        if (selectedTopics.length === 0) return 770
        return selectedTopics.reduce((sum, topicId) => {
            const topic = OMTENTA_V2_TOPICS.find(t => t.id === topicId)
            return sum + (topic?.count || 0)
        }, 0)
    }, [selectedTopics])

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
                            🎯 Omtenta V2 - Linux Quiz
                        </h1>
                        <p className="text-slate-400">
                            770 frågor • 7 ämnesområden • Multi-select support
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
                            {OMTENTA_V2_TOPICS.map(topic => (
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
                                        <div className="text-sm text-slate-400">{topic.count} frågor</div>
                                    </div>
                                </button>
                            ))}
                        </div>

                        <div className="mt-4 text-sm text-slate-400">
                            {selectedTopics.length === 0 ? (
                                <span>Alla ämnen valda (770 frågor)</span>
                            ) : (
                                <span>{selectedTopics.length} ämne(n) valt • {availableQuestions} frågor tillgängliga</span>
                            )}
                        </div>
                    </div>

                    {/* Question Count */}
                    <div className="bg-slate-800/50 rounded-2xl border border-slate-700 p-6 mb-6">
                        <h2 className="text-xl font-semibold text-white flex items-center gap-2 mb-4">
                            <Target className="w-5 h-5 text-green-400" />
                            Antal Frågor
                        </h2>

                        <div className="flex flex-wrap gap-2">
                            {QUESTION_COUNT_OPTIONS.map(count => (
                                <button
                                    key={count}
                                    onClick={() => setQuestionCount(count)}
                                    disabled={count !== 'ALLA' && count > availableQuestions}
                                    className={cn(
                                        "px-4 py-2 rounded-xl font-medium transition-all",
                                        questionCount === count
                                            ? "bg-green-500 text-white"
                                            : count !== 'ALLA' && count > availableQuestions
                                                ? "bg-slate-700/30 text-slate-500 cursor-not-allowed"
                                                : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                                    )}
                                >
                                    {count === 'ALLA' ? 'ALLA' : count}
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Timer Settings */}
                    <div className="bg-slate-800/50 rounded-2xl border border-slate-700 p-6 mb-6">
                        <h2 className="text-xl font-semibold text-white flex items-center gap-2 mb-4">
                            <Clock className="w-5 h-5 text-yellow-400" />
                            Timer
                        </h2>

                        <div className="flex items-center gap-4 mb-4">
                            <button
                                onClick={() => setTimedMode(true)}
                                className={cn(
                                    "px-4 py-2 rounded-xl font-medium transition-all",
                                    timedMode
                                        ? "bg-yellow-500 text-black"
                                        : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                                )}
                            >
                                Med timer
                            </button>
                            <button
                                onClick={() => setTimedMode(false)}
                                className={cn(
                                    "px-4 py-2 rounded-xl font-medium transition-all",
                                    !timedMode
                                        ? "bg-yellow-500 text-black"
                                        : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                                )}
                            >
                                Utan timer
                            </button>
                        </div>

                        {timedMode && (
                            <div className="flex flex-wrap gap-2">
                                {[30, 45, 60, 90, 120].map(mins => (
                                    <button
                                        key={mins}
                                        onClick={() => setDuration(mins)}
                                        className={cn(
                                            "px-4 py-2 rounded-xl font-medium transition-all",
                                            duration === mins
                                                ? "bg-yellow-500/30 text-yellow-400 border border-yellow-500"
                                                : "bg-slate-700 text-slate-300 hover:bg-slate-600"
                                        )}
                                    >
                                        {mins} min
                                    </button>
                                ))}
                            </div>
                        )}
                    </div>

                    {/* Start Button */}
                    <button
                        onClick={startQuiz}
                        className="w-full py-4 bg-gradient-to-r from-blue-500 to-purple-500 text-white font-bold text-xl rounded-2xl hover:from-blue-600 hover:to-purple-600 transition-all flex items-center justify-center gap-3"
                    >
                        <Play className="w-6 h-6" />
                        Starta Quiz
                    </button>
                </div>
            </div>
        )
    }

    // QUIZ PHASE
    if (phase === 'quiz' && currentQuestion) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4 md:p-8">
                <div className="max-w-3xl mx-auto">
                    {/* Top Bar */}
                    <div className="flex items-center justify-between mb-6">
                        <div className="flex items-center gap-4">
                            <span className="text-slate-400">
                                Fråga {currentIndex + 1} / {questions.length}
                            </span>
                            <span className="px-3 py-1 bg-slate-700 rounded-lg text-sm text-slate-300">
                                {OMTENTA_V2_TOPICS.find(t => t.id === currentQuestion.topic)?.name || currentQuestion.topic}
                            </span>
                        </div>
                        <div className="flex items-center gap-4">
                            <span className="text-green-400 font-medium">
                                {correctCount} rätt
                            </span>
                            {timedMode && (
                                <div className={cn(
                                    "flex items-center gap-2 px-3 py-1 rounded-lg",
                                    timeRemaining < 300 ? "bg-red-500/20 text-red-400" : "bg-slate-700 text-slate-300"
                                )}>
                                    <Clock className="w-4 h-4" />
                                    {formatTime(timeRemaining)}
                                </div>
                            )}
                        </div>
                    </div>

                    {/* Progress Bar */}
                    <div className="h-2 bg-slate-700 rounded-full mb-6 overflow-hidden">
                        <div
                            className="h-full bg-gradient-to-r from-blue-500 to-purple-500 transition-all duration-300"
                            style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
                        />
                    </div>

                    {/* Question Card */}
                    <div className="bg-slate-800/70 rounded-2xl border border-slate-700 p-6 mb-6">
                        {/* Multi-select indicator */}
                        {isMultiSelect && (
                            <div className="flex items-center gap-2 mb-4 px-3 py-2 bg-purple-500/20 border border-purple-500/30 rounded-lg">
                                <CheckSquare className="w-4 h-4 text-purple-400" />
                                <span className="text-sm text-purple-300">
                                    Välj {currentQuestion.correctIndices.length} rätta svar
                                </span>
                            </div>
                        )}

                        <h2 className="text-xl md:text-2xl font-semibold text-white mb-6">
                            {currentQuestion.question}
                        </h2>

                        {/* Options */}
                        <div className="space-y-3">
                            {currentQuestion.options.map((option, idx) => {
                                const isSelected = selectedAnswers.includes(idx)
                                const isCorrect = currentQuestion.correctIndices.includes(idx)
                                const showResult = showFeedback

                                return (
                                    <button
                                        key={idx}
                                        onClick={() => toggleAnswer(idx)}
                                        disabled={hasAnswered}
                                        className={cn(
                                            "w-full p-4 rounded-xl border-2 text-left transition-all flex items-center gap-3",
                                            !showResult && isSelected && "bg-blue-500/20 border-blue-500",
                                            !showResult && !isSelected && "bg-slate-700/50 border-slate-600 hover:border-slate-500",
                                            showResult && isCorrect && "bg-green-500/20 border-green-500",
                                            showResult && isSelected && !isCorrect && "bg-red-500/20 border-red-500",
                                            showResult && !isSelected && !isCorrect && "bg-slate-700/30 border-slate-600 opacity-50",
                                            hasAnswered && "cursor-default"
                                        )}
                                    >
                                        {isMultiSelect ? (
                                            isSelected ? (
                                                <CheckSquare className={cn(
                                                    "w-5 h-5 flex-shrink-0",
                                                    showResult && isCorrect && "text-green-400",
                                                    showResult && !isCorrect && "text-red-400",
                                                    !showResult && "text-blue-400"
                                                )} />
                                            ) : (
                                                <Square className={cn(
                                                    "w-5 h-5 flex-shrink-0",
                                                    showResult && isCorrect && "text-green-400",
                                                    !showResult && "text-slate-500"
                                                )} />
                                            )
                                        ) : (
                                            <div className={cn(
                                                "w-5 h-5 rounded-full border-2 flex-shrink-0 flex items-center justify-center",
                                                isSelected ? "border-blue-500 bg-blue-500" : "border-slate-500"
                                            )}>
                                                {isSelected && <div className="w-2 h-2 bg-white rounded-full" />}
                                            </div>
                                        )}
                                        <span className={cn(
                                            "flex-1",
                                            showResult && isCorrect && "text-green-300",
                                            showResult && isSelected && !isCorrect && "text-red-300",
                                            !showResult && "text-slate-200"
                                        )}>
                                            {option}
                                        </span>
                                        {showResult && isCorrect && (
                                            <CheckCircle className="w-5 h-5 text-green-400" />
                                        )}
                                        {showResult && isSelected && !isCorrect && (
                                            <XCircle className="w-5 h-5 text-red-400" />
                                        )}
                                    </button>
                                )
                            })}
                        </div>

                        {/* Explanation */}
                        {showFeedback && currentQuestion.explanation && (
                            <div className="mt-6 p-4 bg-slate-700/50 rounded-xl border border-slate-600">
                                <div className="flex items-center gap-2 mb-2">
                                    <Brain className="w-4 h-4 text-blue-400" />
                                    <span className="font-medium text-blue-400">Förklaring</span>
                                </div>
                                <p className="text-slate-300">{currentQuestion.explanation}</p>
                            </div>
                        )}
                    </div>

                    {/* Action Buttons */}
                    <div className="flex gap-4">
                        {!hasAnswered ? (
                            <button
                                onClick={submitAnswer}
                                disabled={selectedAnswers.length === 0}
                                className={cn(
                                    "flex-1 py-4 font-bold text-lg rounded-xl transition-all flex items-center justify-center gap-2",
                                    selectedAnswers.length > 0
                                        ? "bg-blue-500 hover:bg-blue-600 text-white"
                                        : "bg-slate-700 text-slate-500 cursor-not-allowed"
                                )}
                            >
                                <CheckCircle className="w-5 h-5" />
                                Svara
                            </button>
                        ) : (
                            <button
                                onClick={nextQuestion}
                                className="flex-1 py-4 bg-green-500 hover:bg-green-600 text-white font-bold text-lg rounded-xl transition-all flex items-center justify-center gap-2"
                            >
                                {currentIndex < questions.length - 1 ? (
                                    <>
                                        Nästa fråga
                                        <ArrowRight className="w-5 h-5" />
                                    </>
                                ) : (
                                    <>
                                        Visa resultat
                                        <Trophy className="w-5 h-5" />
                                    </>
                                )}
                            </button>
                        )}
                    </div>
                </div>
            </div>
        )
    }

    // RESULTS PHASE
    if (phase === 'results') {
        const percentage = Math.round((correctCount / results.length) * 100) || 0
        const passed = percentage >= 70

        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4 md:p-8">
                <div className="max-w-2xl mx-auto">
                    {/* Result Card */}
                    <div className="bg-slate-800/70 rounded-2xl border border-slate-700 p-8 text-center mb-6">
                        <div className={cn(
                            "w-24 h-24 rounded-full mx-auto mb-6 flex items-center justify-center",
                            passed ? "bg-green-500/20" : "bg-red-500/20"
                        )}>
                            <Trophy className={cn(
                                "w-12 h-12",
                                passed ? "text-green-400" : "text-red-400"
                            )} />
                        </div>

                        <h1 className="text-3xl font-bold text-white mb-2">
                            {passed ? "🎉 Bra jobbat!" : "📚 Fortsätt öva!"}
                        </h1>

                        <p className="text-slate-400 mb-6">
                            {passed
                                ? "Du klarade quizzen!"
                                : "Du behöver minst 70% för att klara quizzen."
                            }
                        </p>

                        {/* Score Display */}
                        <div className="flex justify-center gap-8 mb-8">
                            <div className="text-center">
                                <div className="text-4xl font-bold text-white">{correctCount}</div>
                                <div className="text-sm text-slate-400">Rätt</div>
                            </div>
                            <div className="text-center">
                                <div className="text-4xl font-bold text-slate-400">{results.length - correctCount}</div>
                                <div className="text-sm text-slate-400">Fel</div>
                            </div>
                            <div className="text-center">
                                <div className={cn(
                                    "text-4xl font-bold",
                                    passed ? "text-green-400" : "text-red-400"
                                )}>
                                    {percentage}%
                                </div>
                                <div className="text-sm text-slate-400">Resultat</div>
                            </div>
                        </div>

                        {/* Progress Bar */}
                        <div className="h-4 bg-slate-700 rounded-full overflow-hidden mb-8">
                            <div
                                className={cn(
                                    "h-full transition-all duration-1000",
                                    passed
                                        ? "bg-gradient-to-r from-green-500 to-emerald-500"
                                        : "bg-gradient-to-r from-red-500 to-orange-500"
                                )}
                                style={{ width: `${percentage}%` }}
                            />
                        </div>

                        {/* Action Buttons */}
                        <div className="flex flex-col sm:flex-row gap-4">
                            <button
                                onClick={restartQuiz}
                                className="flex-1 py-3 bg-slate-700 hover:bg-slate-600 text-white font-medium rounded-xl transition-all flex items-center justify-center gap-2"
                            >
                                <RotateCcw className="w-5 h-5" />
                                Ny Quiz
                            </button>
                            <Link
                                href="/study"
                                className="flex-1 py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-xl transition-all flex items-center justify-center gap-2"
                            >
                                <ArrowLeft className="w-5 h-5" />
                                Tillbaka
                            </Link>
                        </div>
                    </div>

                    {/* Per Topic Breakdown */}
                    <div className="bg-slate-800/50 rounded-2xl border border-slate-700 p-6">
                        <h2 className="text-lg font-semibold text-white mb-4">Resultat per ämne</h2>
                        <div className="space-y-3">
                            {OMTENTA_V2_TOPICS.map(topic => {
                                const topicResults = results.filter(r => {
                                    const q = questions.find(q => q.id === r.questionId)
                                    return q?.topic === topic.id
                                })
                                if (topicResults.length === 0) return null

                                const topicCorrect = topicResults.filter(r => r.correct).length
                                const topicPercentage = Math.round((topicCorrect / topicResults.length) * 100)

                                return (
                                    <div key={topic.id} className="flex items-center gap-4">
                                        <div className="flex-1">
                                            <div className="flex justify-between text-sm mb-1">
                                                <span className="text-slate-300">{topic.name}</span>
                                                <span className="text-slate-400">
                                                    {topicCorrect}/{topicResults.length} ({topicPercentage}%)
                                                </span>
                                            </div>
                                            <div className="h-2 bg-slate-700 rounded-full overflow-hidden">
                                                <div
                                                    className={cn(
                                                        "h-full",
                                                        topicPercentage >= 70 ? "bg-green-500" : "bg-red-500"
                                                    )}
                                                    style={{ width: `${topicPercentage}%` }}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                )
                            })}
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    return null
}
