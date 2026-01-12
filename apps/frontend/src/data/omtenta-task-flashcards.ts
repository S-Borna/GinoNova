/**
 * OMTENTA TASK FLASHCARDS
 * 350 flashcards (50 per område, 7 områden)
 * Konverterade från quiz-format till flashcard-format
 */

import { SSH_BRANDVAGG_QUESTIONS } from './omtenta-ssh-brandvagg'
import { STORAGE_QUESTIONS, DOCKER_QUESTIONS } from './omtenta-storage-docker'
import { ANVANDARHANTERING_QUESTIONS, FILSYSTEM_QUESTIONS } from './omtenta-user-filsystem'
import { PAKETHANTERING_QUESTIONS, SUBNETTING_QUESTIONS } from './omtenta-paket-subnetting'

export interface TaskFlashcard {
    id: string
    front: string
    back: string
    category: string
    difficulty: 'G' | 'VG'
}

export interface TaskFlashcardSet {
    taskId: string
    taskTitle: string
    flashcards: TaskFlashcard[]
}

// Konvertera quiz-frågor till flashcards
function quizToFlashcard(q: { id: string; question: string; options: string[]; correctIndex: number; explanation: string; difficulty: 'G' | 'VG'; category: string }): TaskFlashcard {
    return {
        id: q.id,
        front: q.question,
        back: `${q.options[q.correctIndex]}\n\n${q.explanation}`,
        category: q.category,
        difficulty: q.difficulty
    }
}

// SSH & Brandvägg flashcards
const SSH_BRANDVAGG_FLASHCARDS: TaskFlashcard[] = SSH_BRANDVAGG_QUESTIONS.map(quizToFlashcard)

// Block Storage flashcards
const STORAGE_FLASHCARDS: TaskFlashcard[] = STORAGE_QUESTIONS.map(quizToFlashcard)

// Docker flashcards
const DOCKER_FLASHCARDS: TaskFlashcard[] = DOCKER_QUESTIONS.map(quizToFlashcard)

// Användarhantering flashcards
const ANVANDARHANTERING_FLASHCARDS: TaskFlashcard[] = ANVANDARHANTERING_QUESTIONS.map(quizToFlashcard)

// Filsystem flashcards
const FILSYSTEM_FLASHCARDS: TaskFlashcard[] = FILSYSTEM_QUESTIONS.map(quizToFlashcard)

// Pakethantering flashcards
const PAKETHANTERING_FLASHCARDS: TaskFlashcard[] = PAKETHANTERING_QUESTIONS.map(quizToFlashcard)

// Subnetting flashcards
const SUBNETTING_FLASHCARDS: TaskFlashcard[] = SUBNETTING_QUESTIONS.map(quizToFlashcard)

// Export task flashcard sets
export const OMTENTA_TASK_FLASHCARDS: TaskFlashcardSet[] = [
    {
        taskId: 'ssh-brandvagg',
        taskTitle: 'SSH & Brandvägg',
        flashcards: SSH_BRANDVAGG_FLASHCARDS
    },
    {
        taskId: 'block-storage',
        taskTitle: 'Block Storage & Kryptering',
        flashcards: STORAGE_FLASHCARDS
    },
    {
        taskId: 'docker',
        taskTitle: 'Docker & Kontainrar',
        flashcards: DOCKER_FLASHCARDS
    },
    {
        taskId: 'anvandarhantering',
        taskTitle: 'Användarhantering',
        flashcards: ANVANDARHANTERING_FLASHCARDS
    },
    {
        taskId: 'filsystem',
        taskTitle: 'Filsystem & Navigation',
        flashcards: FILSYSTEM_FLASHCARDS
    },
    {
        taskId: 'pakethantering',
        taskTitle: 'Pakethantering & SSH-nycklar',
        flashcards: PAKETHANTERING_FLASHCARDS
    },
    {
        taskId: 'subnetting',
        taskTitle: 'Subnetting & Nätverk',
        flashcards: SUBNETTING_FLASHCARDS
    }
]

// All flashcards combined
export const ALL_OMTENTA_FLASHCARDS: TaskFlashcard[] = OMTENTA_TASK_FLASHCARDS.flatMap(t => t.flashcards)

// Stats
export const OMTENTA_FLASHCARD_STATS = {
    totalFlashcards: ALL_OMTENTA_FLASHCARDS.length,
    byTask: OMTENTA_TASK_FLASHCARDS.map(t => ({
        taskId: t.taskId,
        count: t.flashcards.length
    }))
}
