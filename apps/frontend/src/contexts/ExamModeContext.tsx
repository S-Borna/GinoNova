"use client"

/**
 * ============================================================================
 * EXAM MODE CONTEXT — State Management för Tentaplugg
 * ============================================================================
 * 
 * Hanterar:
 * - Exam date & countdown
 * - Confidence scores per task
 * - Spaced repetition data
 * - Study sessions & progress
 * - Weak areas identification
 */

import React, { createContext, useContext, useState, useEffect, useCallback } from "react"
import { DOE25_MODULE, DOE25Task } from "@/data/doe25-module"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ConfidenceScore {
    taskId: string
    score: number // 0-100
    lastUpdated: Date
    attempts: number
    correctAnswers: number
    totalQuestions: number
}

export interface SpacedRepetitionCard {
    cardId: string // flashcard ID eller question ID
    taskId: string
    type: "flashcard" | "quiz"
    lastReviewed: Date | null
    nextReview: Date | null
    easeFactor: number // 2.5 = standard
    interval: number // dagar till nästa review
    difficulty: "again" | "hard" | "good" | "easy"
    reviewCount: number
}

export interface StudySession {
    id: string
    date: Date
    taskIds: string[]
    duration: number // minuter
    mode: "flashcards" | "quiz" | "review" | "mock-exam"
    score?: number
}

export interface ExamModeState {
    isActive: boolean
    examDate: Date
    daysRemaining: number
    confidenceScores: Record<string, ConfidenceScore>
    spacedRepetition: Record<string, SpacedRepetitionCard>
    studySessions: StudySession[]
    weakAreas: string[] // taskIds med låg confidence
    studyPlan: {
        dailyTasks: string[]
        focusAreas: string[]
    }
}

interface ExamModeContextType {
    state: ExamModeState
    activateExamMode: (examDate: Date) => void
    deactivateExamMode: () => void
    updateConfidence: (taskId: string, score: number, correct: number, total: number) => void
    updateSpacedRepetition: (cardId: string, difficulty: "again" | "hard" | "good" | "easy") => void
    addStudySession: (session: Omit<StudySession, "id" | "date">) => void
    getCardsForReview: () => SpacedRepetitionCard[]
    getConfidenceForTask: (taskId: string) => number
    getWeakAreas: () => string[]
    calculateStudyPlan: () => void
}

/* ============================================================================
   CONTEXT
   ============================================================================ */

const ExamModeContext = createContext<ExamModeContextType | undefined>(undefined)

/* ============================================================================
   SPACED REPETITION ALGORITHM (SM-2 Algorithm)
   ============================================================================ */

function calculateNextReview(
    currentInterval: number,
    easeFactor: number,
    difficulty: "again" | "hard" | "good" | "easy"
): { interval: number; easeFactor: number } {
    let newEaseFactor = easeFactor
    let newInterval = currentInterval

    switch (difficulty) {
        case "again":
            newInterval = 1 // 1 dag
            newEaseFactor = Math.max(1.3, easeFactor - 0.2)
            break
        case "hard":
            newInterval = Math.max(1, Math.round(currentInterval * 1.2))
            newEaseFactor = Math.max(1.3, easeFactor - 0.15)
            break
        case "good":
            if (currentInterval === 0) {
                newInterval = 1
            } else {
                newInterval = Math.round(currentInterval * easeFactor)
            }
            // easeFactor stays the same
            break
        case "easy":
            newInterval = Math.round(currentInterval * easeFactor * 1.3)
            newEaseFactor = easeFactor + 0.15
            break
    }

    return { interval: newInterval, easeFactor: newEaseFactor }
}

/* ============================================================================
   PROVIDER
   ============================================================================ */

export function ExamModeProvider({ children }: { children: React.ReactNode }) {
    const [state, setState] = useState<ExamModeState>(() => {
        // Load from localStorage
        if (typeof window !== "undefined") {
            const saved = localStorage.getItem("exam-mode-state")
            if (saved) {
                try {
                    const parsed = JSON.parse(saved)
                    return {
                        ...parsed,
                        examDate: new Date(parsed.examDate),
                        confidenceScores: Object.fromEntries(
                            Object.entries(parsed.confidenceScores || {}).map(([k, v]: [string, any]) => [
                                k,
                                { ...v, lastUpdated: new Date(v.lastUpdated) }
                            ])
                        ),
                        spacedRepetition: Object.fromEntries(
                            Object.entries(parsed.spacedRepetition || {}).map(([k, v]: [string, any]) => [
                                k,
                                {
                                    ...v,
                                    lastReviewed: v.lastReviewed ? new Date(v.lastReviewed) : null,
                                    nextReview: v.nextReview ? new Date(v.nextReview) : null
                                }
                            ])
                        ),
                        studySessions: (parsed.studySessions || []).map((s: any) => ({
                            ...s,
                            date: new Date(s.date)
                        }))
                    }
                } catch (e) {
                    console.error("Failed to load exam mode state:", e)
                }
            }
        }

        // Default state
        return {
            isActive: false,
            examDate: new Date(DOE25_MODULE.exam_date),
            daysRemaining: 0,
            confidenceScores: {},
            spacedRepetition: {},
            studySessions: [],
            weakAreas: [],
            studyPlan: {
                dailyTasks: [],
                focusAreas: []
            }
        }
    })

    // Save to localStorage on change
    useEffect(() => {
        if (typeof window !== "undefined") {
            localStorage.setItem("exam-mode-state", JSON.stringify(state))
        }
    }, [state])

    // Calculate days remaining
    useEffect(() => {
        if (state.isActive && state.examDate) {
            const now = new Date()
            const diff = state.examDate.getTime() - now.getTime()
            const days = Math.ceil(diff / (1000 * 60 * 60 * 24))
            setState(prev => ({ ...prev, daysRemaining: Math.max(0, days) }))
        }
    }, [state.isActive, state.examDate])

    // Calculate weak areas
    useEffect(() => {
        const weak = Object.entries(state.confidenceScores)
            .filter(([_, score]) => score.score < 70)
            .map(([taskId]) => taskId)
        setState(prev => ({ ...prev, weakAreas: weak }))
    }, [state.confidenceScores])

    const activateExamMode = useCallback((examDate: Date) => {
        setState(prev => ({
            ...prev,
            isActive: true,
            examDate,
            daysRemaining: Math.ceil((examDate.getTime() - Date.now()) / (1000 * 60 * 60 * 24))
        }))
        calculateStudyPlan()
    }, [])

    const deactivateExamMode = useCallback(() => {
        setState(prev => ({
            ...prev,
            isActive: false
        }))
    }, [])

    const updateConfidence = useCallback((
        taskId: string,
        score: number,
        correct: number,
        total: number
    ) => {
        setState(prev => {
            const existing = prev.confidenceScores[taskId]
            const newScore: ConfidenceScore = {
                taskId,
                score: Math.max(0, Math.min(100, score)),
                lastUpdated: new Date(),
                attempts: (existing?.attempts || 0) + 1,
                correctAnswers: (existing?.correctAnswers || 0) + correct,
                totalQuestions: (existing?.totalQuestions || 0) + total
            }
            return {
                ...prev,
                confidenceScores: {
                    ...prev.confidenceScores,
                    [taskId]: newScore
                }
            }
        })
    }, [])

    const updateSpacedRepetition = useCallback((
        cardId: string,
        difficulty: "again" | "hard" | "good" | "easy"
    ) => {
        setState(prev => {
            const existing = prev.spacedRepetition[cardId]
            const currentInterval = existing?.interval || 0
            const currentEaseFactor = existing?.easeFactor || 2.5

            const { interval, easeFactor } = calculateNextReview(currentInterval, currentEaseFactor, difficulty)
            const now = new Date()
            const nextReview = new Date(now.getTime() + interval * 24 * 60 * 60 * 1000)

            const taskId = existing?.taskId || ""
            const type = existing?.type || "flashcard"

            const updated: SpacedRepetitionCard = {
                cardId,
                taskId,
                type,
                lastReviewed: now,
                nextReview,
                easeFactor,
                interval,
                difficulty,
                reviewCount: (existing?.reviewCount || 0) + 1
            }

            return {
                ...prev,
                spacedRepetition: {
                    ...prev.spacedRepetition,
                    [cardId]: updated
                }
            }
        })
    }, [])

    const addStudySession = useCallback((session: Omit<StudySession, "id" | "date">) => {
        const newSession: StudySession = {
            ...session,
            id: `session-${Date.now()}`,
            date: new Date()
        }
        setState(prev => ({
            ...prev,
            studySessions: [...prev.studySessions, newSession]
        }))
    }, [])

    const getCardsForReview = useCallback((): SpacedRepetitionCard[] => {
        const now = new Date()
        return Object.values(state.spacedRepetition).filter(card => {
            if (!card.nextReview) return true // Never reviewed
            return card.nextReview <= now
        })
    }, [state.spacedRepetition])

    const getConfidenceForTask = useCallback((taskId: string): number => {
        return state.confidenceScores[taskId]?.score || 0
    }, [state.confidenceScores])

    const getWeakAreas = useCallback((): string[] => {
        return state.weakAreas
    }, [state.weakAreas])

    const calculateStudyPlan = useCallback(() => {
        if (!state.isActive || state.daysRemaining <= 0) return

        const allTasks = DOE25_MODULE.tasks
        const weakTasks = state.weakAreas.length > 0
            ? state.weakAreas
            : allTasks.map(t => t.id) // If no weak areas, study all

        // Distribute tasks over remaining days
        const tasksPerDay = Math.ceil(weakTasks.length / state.daysRemaining)
        const dailyTasks: string[] = []
        
        for (let i = 0; i < weakTasks.length; i += tasksPerDay) {
            dailyTasks.push(...weakTasks.slice(i, i + tasksPerDay))
        }

        setState(prev => ({
            ...prev,
            studyPlan: {
                dailyTasks: dailyTasks.slice(0, state.daysRemaining),
                focusAreas: weakTasks.slice(0, 5) // Top 5 weak areas
            }
        }))
    }, [state.isActive, state.daysRemaining, state.weakAreas])

    const value: ExamModeContextType = {
        state,
        activateExamMode,
        deactivateExamMode,
        updateConfidence,
        updateSpacedRepetition,
        addStudySession,
        getCardsForReview,
        getConfidenceForTask,
        getWeakAreas,
        calculateStudyPlan
    }

    return (
        <ExamModeContext.Provider value={value}>
            {children}
        </ExamModeContext.Provider>
    )
}

/* ============================================================================
   HOOK
   ============================================================================ */

export function useExamMode() {
    const context = useContext(ExamModeContext)
    if (context === undefined) {
        throw new Error("useExamMode must be used within ExamModeProvider")
    }
    return context
}

