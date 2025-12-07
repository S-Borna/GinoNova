"use client"

/**
 * Favorites Hook
 * ==============
 *
 * Hanterar stjärnmarkerade flashcards och quiz.
 * Användaren döper favoriten (max 6 tecken) vid stjärntillfället.
 */

import { useState, useEffect, useCallback } from "react"

export interface FavoriteItem {
    id: string
    type: "flashcard" | "quiz"
    customName: string      // Användarens namn (max 6 tecken)
    moduleSlug: string
    moduleTitle: string
    originalQuestion: string
    createdAt: string
}

interface UseFavoritesReturn {
    favorites: FavoriteItem[]
    addFavorite: (item: Omit<FavoriteItem, "id" | "createdAt">) => void
    removeFavorite: (id: string) => void
    isFavorite: (moduleSlug: string, question: string, type: "flashcard" | "quiz") => boolean
    getFavoriteId: (moduleSlug: string, question: string, type: "flashcard" | "quiz") => string | null
}

const STORAGE_KEY = "devopshub_favorites"

export function useFavorites(): UseFavoritesReturn {
    const [favorites, setFavorites] = useState<FavoriteItem[]>([])

    // Ladda från localStorage
    useEffect(() => {
        try {
            const saved = localStorage.getItem(STORAGE_KEY)
            if (saved) {
                setFavorites(JSON.parse(saved))
            }
        } catch {
            // Ignorera fel
        }
    }, [])

    // Spara till localStorage vid ändringar
    useEffect(() => {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites))
    }, [favorites])

    const addFavorite = useCallback((item: Omit<FavoriteItem, "id" | "createdAt">) => {
        const newItem: FavoriteItem = {
            ...item,
            id: `${item.type}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
            customName: item.customName.slice(0, 6), // Max 6 tecken
            createdAt: new Date().toISOString()
        }
        setFavorites(prev => [newItem, ...prev])
    }, [])

    const removeFavorite = useCallback((id: string) => {
        setFavorites(prev => prev.filter(f => f.id !== id))
    }, [])

    const isFavorite = useCallback((moduleSlug: string, question: string, type: "flashcard" | "quiz"): boolean => {
        return favorites.some(f =>
            f.moduleSlug === moduleSlug &&
            f.originalQuestion === question &&
            f.type === type
        )
    }, [favorites])

    const getFavoriteId = useCallback((moduleSlug: string, question: string, type: "flashcard" | "quiz"): string | null => {
        const found = favorites.find(f =>
            f.moduleSlug === moduleSlug &&
            f.originalQuestion === question &&
            f.type === type
        )
        return found?.id || null
    }, [favorites])

    return {
        favorites,
        addFavorite,
        removeFavorite,
        isFavorite,
        getFavoriteId
    }
}
