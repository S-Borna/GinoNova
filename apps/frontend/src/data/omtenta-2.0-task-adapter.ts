/**
 * OMTENTA 2.0 TASK ADAPTER
 * Konverterar Omtenta 2.0 (10 noder) till TaskFlashcardSet och TaskQuizSet format
 * för kompatibilitet med Studyroom flashcards/quiz
 */

import { ALL_OMTENTA_2_FLASHCARDS, type Omtenta2Flashcard } from './omtenta-2.0-flashcards'
import { ALL_OMTENTA_2_QUESTIONS, OMTENTA2_TOPIC_INFO, type Omtenta2Question, type Omtenta2Topic } from './omtenta-2.0-quiz'

// TaskFlashcard format used by flashcards page
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

// TaskQuiz format used by quiz page
export interface TaskQuizQuestion {
    id: string
    question: string
    options: string[]
    correctIndex: number
    explanation: string
    difficulty?: 'G' | 'VG'
    category?: string
}

export interface TaskQuizSet {
    taskId: string
    taskTitle: string
    questions: TaskQuizQuestion[]
}

// Topic IDs for all 10 nodes
const TOPIC_IDS: Omtenta2Topic[] = [
    'nod1-filsystem',
    'nod2-rattigheter',
    'nod3-processhantering',
    'nod4-natverk',
    'nod5-ssh',
    'nod6-bash-skript',
    'nod7-bash-verktyg',
    'nod8-docker-isolering',
    'nod9-docker-natverk',
    'nod10-docker-compose'
]

// Convert Omtenta2Flashcard to TaskFlashcard
function flashcardToTaskFormat(fc: Omtenta2Flashcard): TaskFlashcard {
    return {
        id: `omtenta2-fc-${fc.id}`,
        front: fc.question,
        back: fc.answer,
        category: fc.category,
        difficulty: 'G' // Default since original doesn't have difficulty
    }
}

// Convert Omtenta2Question to TaskQuizQuestion
function quizToTaskFormat(q: Omtenta2Question): TaskQuizQuestion {
    return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctIndex: q.correctIndices[0], // Use first correct answer
        explanation: q.explanation,
        difficulty: q.difficulty,
        category: q.category
    }
}

// Create TaskFlashcardSet for each topic
export const OMTENTA_2_TASK_FLASHCARDS: TaskFlashcardSet[] = TOPIC_IDS.map(topicId => ({
    taskId: topicId,
    taskTitle: OMTENTA2_TOPIC_INFO[topicId].name,
    flashcards: ALL_OMTENTA_2_FLASHCARDS
        .filter(fc => fc.topic === topicId)
        .map(flashcardToTaskFormat)
}))

// Create TaskQuizSet for each topic
export const OMTENTA_2_TASK_QUIZ: TaskQuizSet[] = TOPIC_IDS.map(topicId => ({
    taskId: topicId,
    taskTitle: OMTENTA2_TOPIC_INFO[topicId].name,
    questions: ALL_OMTENTA_2_QUESTIONS
        .filter(q => q.topic === topicId)
        .map(quizToTaskFormat)
}))

// All flashcards flattened
export const ALL_OMTENTA_2_TASK_FLASHCARDS: TaskFlashcard[] =
    OMTENTA_2_TASK_FLASHCARDS.flatMap(t => t.flashcards)

// All quiz questions flattened
export const ALL_OMTENTA_2_TASK_QUIZ: TaskQuizQuestion[] =
    OMTENTA_2_TASK_QUIZ.flatMap(t => t.questions)

// Helper to get all quiz questions
export function getAllOmtenta2Quiz(): TaskQuizQuestion[] {
    return ALL_OMTENTA_2_TASK_QUIZ
}

// Stats
export const OMTENTA_2_STATS = {
    totalFlashcards: ALL_OMTENTA_2_TASK_FLASHCARDS.length,
    totalQuestions: ALL_OMTENTA_2_TASK_QUIZ.length,
    topics: OMTENTA_2_TASK_FLASHCARDS.map(t => ({
        taskId: t.taskId,
        flashcardCount: t.flashcards.length,
        quizCount: OMTENTA_2_TASK_QUIZ.find(q => q.taskId === t.taskId)?.questions.length || 0
    }))
}
