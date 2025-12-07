"use client"

/**
 * Completed Exercises Hook
 * ========================
 *
 * Spårar antalet avklarade flashcards och quiz.
 * Sparas i localStorage.
 */

import { useState, useEffect, useCallback } from "react"

interface CompletedData {
    total: number
    flashcards: number
    quiz: number
    lastUpdated: string
}

interface UseCompletedExercisesReturn {
    total: number
    flashcards: number
    quiz: number
    incrementFlashcards: (count?: number) => void
    incrementQuiz: (count?: number) => void
}

const STORAGE_KEY = "devopshub_completed_exercises"

export function useCompletedExercises(): UseCompletedExercisesReturn {
    const [data, setData] = useState<CompletedData>({
        total: 0,
        flashcards: 0,
        quiz: 0,
        lastUpdated: new Date().toISOString()
    })

    // Load from localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem(STORAGE_KEY)
            if (saved) {
                setData(JSON.parse(saved))
            }
        } catch {
            // Ignore errors
        }
    }, [])

    // Save to localStorage
    const saveData = useCallback((newData: CompletedData) => {
        setData(newData)
        localStorage.setItem(STORAGE_KEY, JSON.stringify(newData))
    }, [])

    const incrementFlashcards = useCallback((count: number = 1) => {
        saveData({
            ...data,
            total: data.total + count,
            flashcards: data.flashcards + count,
            lastUpdated: new Date().toISOString()
        })
    }, [data, saveData])

    const incrementQuiz = useCallback((count: number = 1) => {
        saveData({
            ...data,
            total: data.total + count,
            quiz: data.quiz + count,
            lastUpdated: new Date().toISOString()
        })
    }, [data, saveData])

    return {
        total: data.total,
        flashcards: data.flashcards,
        quiz: data.quiz,
        incrementFlashcards,
        incrementQuiz
    }
}
