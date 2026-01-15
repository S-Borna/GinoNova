/**
 * OMTENTA 2.0 - Komplett frågebank från alla 10 NOD-moduler
 *
 * INNEHÅLL:
 * - Nod 1: Linux Filsystem & Grunder (50 frågor)
 * - Nod 2: Rättigheter & Säkerhet (50 frågor)
 * - Nod 3: Processhantering (50 frågor)
 * - Nod 4: Nätverk & Server (50 frågor)
 * - Nod 5: SSH & Kommunikation (50 frågor)
 * - Nod 6: Bash Skriptprogrammering (50 frågor)
 * - Nod 7: Bash Verktyg (50 frågor)
 * - Nod 8: Docker Isolering & Images (50 frågor)
 * - Nod 9: Docker Nätverk & Lagring (50 frågor)
 * - Nod 10: Docker Compose & IaC (50 frågor)
 *
 * TOTAL: 500 exam-style frågor
 */

// Import alla 10 NOD exam frågor
import { EXAM_NOD1_QUESTIONS } from './exam-nod1-questions'
import { EXAM_NOD2_QUESTIONS } from './exam-nod2-questions'
import { EXAM_NOD3_QUESTIONS } from './exam-nod3-questions'
import { EXAM_NOD4_QUESTIONS } from './exam-nod4-questions'
import { EXAM_NOD5_QUESTIONS } from './exam-nod5-questions'
import { EXAM_NOD6_QUESTIONS } from './exam-nod6-questions'
import { EXAM_NOD7_QUESTIONS } from './exam-nod7-questions'
import { EXAM_NOD8_QUESTIONS } from './exam-nod8-questions'
import { EXAM_NOD9_QUESTIONS } from './exam-nod9-questions'
import { EXAM_NOD10_QUESTIONS } from './exam-nod10-questions'

export type Omtenta2Topic =
    | 'nod1-filsystem'
    | 'nod2-rattigheter'
    | 'nod3-processhantering'
    | 'nod4-natverk'
    | 'nod5-ssh'
    | 'nod6-bash-skript'
    | 'nod7-bash-verktyg'
    | 'nod8-docker-isolering'
    | 'nod9-docker-natverk'
    | 'nod10-docker-compose'

export interface Omtenta2Question {
    id: string
    question: string
    options: string[]
    correctIndices: number[]
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    topic: Omtenta2Topic
    type: 'quiz' | 'scenario'
}

export const OMTENTA2_TOPIC_INFO: Record<Omtenta2Topic, { name: string; description: string }> = {
    'nod1-filsystem': { name: 'Nod 1: Filsystem & Grunder', description: 'FHS, kataloger, inodes, länkar, mount points' },
    'nod2-rattigheter': { name: 'Nod 2: Rättigheter & Säkerhet', description: 'chmod, chown, sudo, umask, ACL, SUID/SGID' },
    'nod3-processhantering': { name: 'Nod 3: Processhantering', description: 'Processer, signaler, jobs, nice, load average' },
    'nod4-natverk': { name: 'Nod 4: Nätverk & Server', description: 'IP, subnetting, TCP/UDP, DNS, portar, OSI' },
    'nod5-ssh': { name: 'Nod 5: SSH & Kommunikation', description: 'SSH-nycklar, agent, tunnlar, scp, rsync' },
    'nod6-bash-skript': { name: 'Nod 6: Bash Skript', description: 'Variabler, loopar, villkor, funktioner, tester' },
    'nod7-bash-verktyg': { name: 'Nod 7: Bash Verktyg', description: 'grep, sed, awk, find, sort, pipes' },
    'nod8-docker-isolering': { name: 'Nod 8: Docker & Isolering', description: 'Containers, images, Dockerfile, registry' },
    'nod9-docker-natverk': { name: 'Nod 9: Docker Nätverk & Lagring', description: 'Volumes, bind mounts, networks, DNS' },
    'nod10-docker-compose': { name: 'Nod 10: Docker Compose & IaC', description: 'docker-compose.yml, services, IaC koncept' }
}

// Re-exportera med gamla namn för bakåtkompatibilitet
export const NOD1_QUESTIONS: Omtenta2Question[] = EXAM_NOD1_QUESTIONS
export const NOD2_QUESTIONS: Omtenta2Question[] = EXAM_NOD2_QUESTIONS
export const NOD3_QUESTIONS: Omtenta2Question[] = EXAM_NOD3_QUESTIONS
export const NOD4_QUESTIONS: Omtenta2Question[] = EXAM_NOD4_QUESTIONS
export const NOD5_QUESTIONS: Omtenta2Question[] = EXAM_NOD5_QUESTIONS
export const NOD6_QUESTIONS: Omtenta2Question[] = EXAM_NOD6_QUESTIONS
export const NOD7_QUESTIONS: Omtenta2Question[] = EXAM_NOD7_QUESTIONS
export const NOD8_QUESTIONS: Omtenta2Question[] = EXAM_NOD8_QUESTIONS
export const NOD9_QUESTIONS: Omtenta2Question[] = EXAM_NOD9_QUESTIONS
export const NOD10_QUESTIONS: Omtenta2Question[] = EXAM_NOD10_QUESTIONS

// ===== AGGREGERAD EXPORT =====
export const ALL_OMTENTA_2_QUESTIONS: Omtenta2Question[] = [
    ...EXAM_NOD1_QUESTIONS,
    ...EXAM_NOD2_QUESTIONS,
    ...EXAM_NOD3_QUESTIONS,
    ...EXAM_NOD4_QUESTIONS,
    ...EXAM_NOD5_QUESTIONS,
    ...EXAM_NOD6_QUESTIONS,
    ...EXAM_NOD7_QUESTIONS,
    ...EXAM_NOD8_QUESTIONS,
    ...EXAM_NOD9_QUESTIONS,
    ...EXAM_NOD10_QUESTIONS
]

export const OMTENTA2_TOPICS: Omtenta2Topic[] = [
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

// ===== HJÄLPFUNKTIONER =====
export function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

export function getQuestionsByTopics(topics: Omtenta2Topic[]): Omtenta2Question[] {
    if (topics.length === 0) return ALL_OMTENTA_2_QUESTIONS
    return ALL_OMTENTA_2_QUESTIONS.filter(q => topics.includes(q.topic))
}

export function getQuizQuestions(count: number, topics?: Omtenta2Topic[]): Omtenta2Question[] {
    const pool = topics && topics.length > 0
        ? getQuestionsByTopics(topics)
        : ALL_OMTENTA_2_QUESTIONS

    const shuffled = shuffleArray(pool)
    return shuffled.slice(0, Math.min(count, shuffled.length))
}

export function getQuestionsByType(type: 'quiz' | 'scenario', topics?: Omtenta2Topic[]): Omtenta2Question[] {
    let pool = topics && topics.length > 0
        ? getQuestionsByTopics(topics)
        : ALL_OMTENTA_2_QUESTIONS

    return pool.filter(q => q.type === type)
}

export function getQuestionsByDifficulty(difficulty: 'G' | 'VG', topics?: Omtenta2Topic[]): Omtenta2Question[] {
    let pool = topics && topics.length > 0
        ? getQuestionsByTopics(topics)
        : ALL_OMTENTA_2_QUESTIONS

    return pool.filter(q => q.difficulty === difficulty)
}

// Statistik
export const QUIZ_STATS = {
    totalQuestions: ALL_OMTENTA_2_QUESTIONS.length,
    questionsPerNod: 50,
    totalNods: 10,
    gLevel: ALL_OMTENTA_2_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgLevel: ALL_OMTENTA_2_QUESTIONS.filter(q => q.difficulty === 'VG').length
}
