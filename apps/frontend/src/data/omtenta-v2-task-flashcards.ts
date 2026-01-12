/**
 * OMTENTA V2 TASK FLASHCARDS ADAPTER
 * Konverterar V2-flashcards (770 st) till TaskFlashcardSet-format
 * för kompatibilitet med flashcard-modulen
 */

import { 
    ALL_FLASHCARDS, 
    FLASHCARDS_BY_TOPIC, 
    FLASHCARD_TOPICS,
    type OmtentaV2Flashcard,
    type FlashcardTopic 
} from './omtenta-v2-flashcards'

// Re-use TaskFlashcard interface from existing module
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

// Konvertera OmtentaV2Flashcard till TaskFlashcard
function v2ToTaskFlashcard(fc: OmtentaV2Flashcard, topicId: string): TaskFlashcard {
    return {
        id: `omtenta-v2-${topicId}-${fc.id}`,
        front: fc.question,
        back: fc.answer,
        category: fc.topic,
        difficulty: 'G' // Default to G since V2 flashcards don't have difficulty
    }
}

// Skapa TaskFlashcardSet för varje topic
export const OMTENTA_V2_TASK_FLASHCARDS: TaskFlashcardSet[] = FLASHCARD_TOPICS.map(topic => ({
    taskId: topic.id,
    taskTitle: topic.name,
    flashcards: FLASHCARDS_BY_TOPIC[topic.id as FlashcardTopic].map(fc => v2ToTaskFlashcard(fc, topic.id))
}))

// All flashcards combined
export const ALL_OMTENTA_V2_FLASHCARDS: TaskFlashcard[] = OMTENTA_V2_TASK_FLASHCARDS.flatMap(t => t.flashcards)

// Stats
export const OMTENTA_V2_FLASHCARD_STATS = {
    totalFlashcards: ALL_OMTENTA_V2_FLASHCARDS.length,
    byTask: OMTENTA_V2_TASK_FLASHCARDS.map(t => ({
        taskId: t.taskId,
        count: t.flashcards.length
    }))
}
