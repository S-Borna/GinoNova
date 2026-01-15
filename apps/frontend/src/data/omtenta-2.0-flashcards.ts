/**
 * OMTENTA 2.0 - Komplett flashcard-bank från alla 10 NOD-moduler
 *
 * INNEHÅLL:
 * - Nod 1: Linux Filsystem & Grunder (50 flashcards)
 * - Nod 2: Rättigheter & Säkerhet (50 flashcards)
 * - Nod 3: Processhantering (50 flashcards)
 * - Nod 4: Nätverk & Server (50 flashcards)
 * - Nod 5: SSH & Kommunikation (50 flashcards)
 * - Nod 6: Bash Skriptprogrammering (50 flashcards)
 * - Nod 7: Bash Verktyg (50 flashcards)
 * - Nod 8: Docker Isolering & Images (50 flashcards)
 * - Nod 9: Docker Nätverk & Lagring (50 flashcards)
 * - Nod 10: Docker Compose & IaC (50 flashcards)
 *
 * TOTAL: 500 flashcards
 */

import type { Omtenta2Topic } from './omtenta-2.0-quiz'

// Import alla 10 NOD flashcards
import { EXAM_NOD1_FLASHCARDS } from './exam-flashcards-nod1'
import { EXAM_NOD2_FLASHCARDS } from './exam-flashcards-nod2'
import { EXAM_NOD3_FLASHCARDS } from './exam-flashcards-nod3'
import { EXAM_NOD4_FLASHCARDS } from './exam-flashcards-nod4'
import { EXAM_NOD5_FLASHCARDS } from './exam-flashcards-nod5'
import { EXAM_NOD6_FLASHCARDS } from './exam-flashcards-nod6'
import { EXAM_NOD7_FLASHCARDS } from './exam-flashcards-nod7'
import { EXAM_NOD8_FLASHCARDS } from './exam-flashcards-nod8'
import { EXAM_NOD9_FLASHCARDS } from './exam-flashcards-nod9'
import { EXAM_NOD10_FLASHCARDS } from './exam-flashcards-nod10'

export interface Omtenta2Flashcard {
    id: number
    topic: Omtenta2Topic
    category: string
    question: string
    answer: string
}

// Re-exportera med gamla namn för bakåtkompatibilitet
export const NOD1_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD1_FLASHCARDS
export const NOD2_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD2_FLASHCARDS
export const NOD3_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD3_FLASHCARDS
export const NOD4_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD4_FLASHCARDS
export const NOD5_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD5_FLASHCARDS
export const NOD6_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD6_FLASHCARDS
export const NOD7_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD7_FLASHCARDS
export const NOD8_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD8_FLASHCARDS
export const NOD9_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD9_FLASHCARDS
export const NOD10_FLASHCARDS: Omtenta2Flashcard[] = EXAM_NOD10_FLASHCARDS

// ===== AGGREGERAD EXPORT =====
export const ALL_OMTENTA_2_FLASHCARDS: Omtenta2Flashcard[] = [
    ...EXAM_NOD1_FLASHCARDS,
    ...EXAM_NOD2_FLASHCARDS,
    ...EXAM_NOD3_FLASHCARDS,
    ...EXAM_NOD4_FLASHCARDS,
    ...EXAM_NOD5_FLASHCARDS,
    ...EXAM_NOD6_FLASHCARDS,
    ...EXAM_NOD7_FLASHCARDS,
    ...EXAM_NOD8_FLASHCARDS,
    ...EXAM_NOD9_FLASHCARDS,
    ...EXAM_NOD10_FLASHCARDS
]

// ===== HJÄLPFUNKTIONER =====
export function shuffleFlashcards(cards: Omtenta2Flashcard[]): Omtenta2Flashcard[] {
    const shuffled = [...cards]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

export function getFlashcardsByTopics(topics: Omtenta2Topic[]): Omtenta2Flashcard[] {
    if (topics.length === 0) return ALL_OMTENTA_2_FLASHCARDS
    return ALL_OMTENTA_2_FLASHCARDS.filter(f => topics.includes(f.topic))
}

export function getRandomFlashcards(count: number, topics?: Omtenta2Topic[]): Omtenta2Flashcard[] {
    const pool = topics && topics.length > 0
        ? getFlashcardsByTopics(topics)
        : ALL_OMTENTA_2_FLASHCARDS

    const shuffled = shuffleFlashcards(pool)
    return shuffled.slice(0, Math.min(count, shuffled.length))
}

export function getFlashcardsByCategory(category: string): Omtenta2Flashcard[] {
    return ALL_OMTENTA_2_FLASHCARDS.filter(f => f.category.toLowerCase().includes(category.toLowerCase()))
}

// Statistik
export const FLASHCARD_STATS = {
    totalFlashcards: ALL_OMTENTA_2_FLASHCARDS.length,
    flashcardsPerNod: 50,
    totalNods: 10
}
