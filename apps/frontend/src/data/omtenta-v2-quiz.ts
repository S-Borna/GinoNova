// Omtenta V2 Quiz - Aggregator
// Kombinerar alla 7 ämnesområden (770 frågor totalt)

import { OmtentaV2Question, OmtentaV2Topic } from './omtenta-v2-ssh-brandvagg'
import { SSH_BRANDVAGG_V2_QUESTIONS } from './omtenta-v2-ssh-brandvagg'
import { PAKETHANTERING_BASH_V2_QUESTIONS } from './omtenta-v2-pakethantering-bash'
import { DOCKER_CONTAINERS_V2_QUESTIONS } from './omtenta-v2-docker-containers'
import { BLOCKSTORAGE_KRYPTERING_V2_QUESTIONS } from './omtenta-v2-blockstorage-kryptering'
import { SUBNETTING_NATVERK_V2_QUESTIONS } from './omtenta-v2-subnetting-natverk'
import { ANVANDARHANTERING_V2_QUESTIONS } from './omtenta-v2-anvandarhantering'
import { FILSYSTEM_V2_QUESTIONS } from './omtenta-v2-filsystem'

// Re-export types
export type { OmtentaV2Question, OmtentaV2Topic }

// Topic metadata
export const OMTENTA_V2_TOPICS: { id: OmtentaV2Topic; name: string; count: number }[] = [
    { id: 'ssh-brandvagg', name: 'SSH & Brandvägg', count: 110 },
    { id: 'pakethantering-bash', name: 'Pakethantering & Bash', count: 110 },
    { id: 'docker-containers', name: 'Docker & Containers', count: 110 },
    { id: 'blockstorage-kryptering', name: 'Block Storage & Kryptering', count: 110 },
    { id: 'subnetting-natverk', name: 'Subnetting & Nätverk', count: 110 },
    { id: 'anvandarhantering', name: 'Användarhantering', count: 110 },
    { id: 'filsystem', name: 'Filsystem & Navigation', count: 110 },
]

// Question count options
export const QUESTION_COUNT_OPTIONS = [100, 200, 300, 400, 500, 600, 700, 'ALLA'] as const
export type QuestionCountOption = typeof QUESTION_COUNT_OPTIONS[number]

// All questions by topic
export const OMTENTA_V2_QUESTIONS_BY_TOPIC: Record<OmtentaV2Topic, OmtentaV2Question[]> = {
    'ssh-brandvagg': SSH_BRANDVAGG_V2_QUESTIONS,
    'pakethantering-bash': PAKETHANTERING_BASH_V2_QUESTIONS,
    'docker-containers': DOCKER_CONTAINERS_V2_QUESTIONS,
    'blockstorage-kryptering': BLOCKSTORAGE_KRYPTERING_V2_QUESTIONS,
    'subnetting-natverk': SUBNETTING_NATVERK_V2_QUESTIONS,
    'anvandarhantering': ANVANDARHANTERING_V2_QUESTIONS,
    'filsystem': FILSYSTEM_V2_QUESTIONS,
}

// All questions combined (770 total)
export const ALL_OMTENTA_V2_QUESTIONS: OmtentaV2Question[] = [
    ...SSH_BRANDVAGG_V2_QUESTIONS,
    ...PAKETHANTERING_BASH_V2_QUESTIONS,
    ...DOCKER_CONTAINERS_V2_QUESTIONS,
    ...BLOCKSTORAGE_KRYPTERING_V2_QUESTIONS,
    ...SUBNETTING_NATVERK_V2_QUESTIONS,
    ...ANVANDARHANTERING_V2_QUESTIONS,
    ...FILSYSTEM_V2_QUESTIONS,
]

// Helper function to get questions by selected topics
export function getQuestionsByTopics(topics: OmtentaV2Topic[]): OmtentaV2Question[] {
    if (topics.length === 0) return ALL_OMTENTA_V2_QUESTIONS
    return topics.flatMap(topic => OMTENTA_V2_QUESTIONS_BY_TOPIC[topic])
}

// Helper function to shuffle array
export function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

// Helper function to get quiz questions with options
export function getQuizQuestions(
    topics: OmtentaV2Topic[],
    count: QuestionCountOption
): OmtentaV2Question[] {
    const questions = getQuestionsByTopics(topics)
    const shuffled = shuffleArray(questions)

    if (count === 'ALLA') {
        return shuffled
    }

    return shuffled.slice(0, Math.min(count, shuffled.length))
}

// Check if question is multi-select
export function isMultiSelectQuestion(question: OmtentaV2Question): boolean {
    return question.correctIndices.length > 1
}

// Check answer for single or multi-select
export function checkAnswer(
    question: OmtentaV2Question,
    selectedIndices: number[]
): boolean {
    if (selectedIndices.length !== question.correctIndices.length) {
        return false
    }
    const sortedSelected = [...selectedIndices].sort((a, b) => a - b)
    const sortedCorrect = [...question.correctIndices].sort((a, b) => a - b)
    return sortedSelected.every((val, idx) => val === sortedCorrect[idx])
}
