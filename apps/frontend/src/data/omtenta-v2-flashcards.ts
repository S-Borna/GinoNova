// Omtenta V2 Flashcards - Aggregator
// Kombinerar alla 7 ämnesområden (770 flashcards totalt)

import { OmtentaV2Flashcard } from './omtenta-v2-flashcards-ssh-brandvagg'
import { SSH_BRANDVAGG_FLASHCARDS } from './omtenta-v2-flashcards-ssh-brandvagg'
import { PAKETHANTERING_BASH_FLASHCARDS } from './omtenta-v2-flashcards-pakethantering-bash'
import { DOCKER_CONTAINERS_FLASHCARDS } from './omtenta-v2-flashcards-docker-containers'
import { BLOCKSTORAGE_KRYPTERING_FLASHCARDS } from './omtenta-v2-flashcards-blockstorage-kryptering'
import { SUBNETTING_NATVERK_FLASHCARDS } from './omtenta-v2-flashcards-subnetting-natverk'
import { ANVANDARHANTERING_FLASHCARDS } from './omtenta-v2-flashcards-anvandarhantering'
import { FILSYSTEM_FLASHCARDS } from './omtenta-v2-flashcards-filsystem'

// Re-export type
export type { OmtentaV2Flashcard }

// Flashcard topic type
export type FlashcardTopic =
    | 'ssh-brandvagg'
    | 'pakethantering-bash'
    | 'docker-containers'
    | 'blockstorage-kryptering'
    | 'subnetting-natverk'
    | 'anvandarhantering'
    | 'filsystem'

// Topic metadata for flashcards
export const FLASHCARD_TOPICS: { id: FlashcardTopic; name: string; count: number }[] = [
    { id: 'ssh-brandvagg', name: 'SSH & Brandvägg', count: 110 },
    { id: 'pakethantering-bash', name: 'Pakethantering & Bash', count: 110 },
    { id: 'docker-containers', name: 'Docker & Containers', count: 110 },
    { id: 'blockstorage-kryptering', name: 'Block Storage & Kryptering', count: 110 },
    { id: 'subnetting-natverk', name: 'Subnetting & Nätverk', count: 110 },
    { id: 'anvandarhantering', name: 'Användarhantering', count: 110 },
    { id: 'filsystem', name: 'Filsystem & Navigation', count: 110 },
]

// Flashcard count options
export const FLASHCARD_COUNT_OPTIONS = [100, 200, 300, 400, 500, 600, 700, 'ALLA'] as const
export type FlashcardCountOption = typeof FLASHCARD_COUNT_OPTIONS[number]

// All flashcards by topic
export const FLASHCARDS_BY_TOPIC: Record<FlashcardTopic, OmtentaV2Flashcard[]> = {
    'ssh-brandvagg': SSH_BRANDVAGG_FLASHCARDS,
    'pakethantering-bash': PAKETHANTERING_BASH_FLASHCARDS,
    'docker-containers': DOCKER_CONTAINERS_FLASHCARDS,
    'blockstorage-kryptering': BLOCKSTORAGE_KRYPTERING_FLASHCARDS,
    'subnetting-natverk': SUBNETTING_NATVERK_FLASHCARDS,
    'anvandarhantering': ANVANDARHANTERING_FLASHCARDS,
    'filsystem': FILSYSTEM_FLASHCARDS,
}

// All flashcards combined (770 total)
export const ALL_FLASHCARDS: OmtentaV2Flashcard[] = [
    ...SSH_BRANDVAGG_FLASHCARDS,
    ...PAKETHANTERING_BASH_FLASHCARDS,
    ...DOCKER_CONTAINERS_FLASHCARDS,
    ...BLOCKSTORAGE_KRYPTERING_FLASHCARDS,
    ...SUBNETTING_NATVERK_FLASHCARDS,
    ...ANVANDARHANTERING_FLASHCARDS,
    ...FILSYSTEM_FLASHCARDS,
]

// Helper function to get flashcards by selected topics
export function getFlashcardsByTopics(topics: FlashcardTopic[]): OmtentaV2Flashcard[] {
    if (topics.length === 0) return ALL_FLASHCARDS
    return topics.flatMap(topic => FLASHCARDS_BY_TOPIC[topic])
}

// Helper function to shuffle array
export function shuffleFlashcards<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

// Helper function to get flashcards with options
export function getFlashcards(
    topics: FlashcardTopic[],
    count: FlashcardCountOption
): OmtentaV2Flashcard[] {
    const flashcards = getFlashcardsByTopics(topics)
    const shuffled = shuffleFlashcards(flashcards)

    if (count === 'ALLA') {
        return shuffled
    }

    return shuffled.slice(0, Math.min(count, shuffled.length))
}
