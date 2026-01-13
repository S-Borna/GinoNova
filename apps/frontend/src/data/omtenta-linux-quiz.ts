/**
 * INFÖR OMTENTA LINUX - Huvudfil
 * Samlar alla 350 quiz-frågor för omtenta-förberedelse
 *
 * Struktur:
 * - omtenta-ssh-brandvagg.ts: 50 frågor (SSH & Brandvägg)
 * - omtenta-storage-docker.ts: 100 frågor (Block Storage + Docker)
 * - omtenta-user-filsystem.ts: 100 frågor (Användarhantering + Filsystem)
 * - omtenta-paket-subnetting.ts: 100 frågor (Pakethantering + Subnetting)
 *
 * Total: 350 frågor
 *
 * Skapad: 2026-01-12
 */

import { SSH_BRANDVAGG_QUESTIONS, type OmtentaQuestion } from './omtenta-ssh-brandvagg'
import { STORAGE_QUESTIONS, DOCKER_QUESTIONS } from './omtenta-storage-docker'
import { ANVANDARHANTERING_QUESTIONS, FILSYSTEM_QUESTIONS } from './omtenta-user-filsystem'
import { PAKETHANTERING_QUESTIONS, SUBNETTING_QUESTIONS } from './omtenta-paket-subnetting'

// Re-export type
export type { OmtentaQuestion }

// Combine all questions
export const ALL_OMTENTA_QUESTIONS: OmtentaQuestion[] = [
    ...SSH_BRANDVAGG_QUESTIONS,
    ...STORAGE_QUESTIONS,
    ...DOCKER_QUESTIONS,
    ...ANVANDARHANTERING_QUESTIONS,
    ...FILSYSTEM_QUESTIONS,
    ...PAKETHANTERING_QUESTIONS,
    ...SUBNETTING_QUESTIONS
]

// Stats
export const OMTENTA_STATS = {
    totalQuestions: ALL_OMTENTA_QUESTIONS.length,
    gQuestions: ALL_OMTENTA_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: ALL_OMTENTA_QUESTIONS.filter(q => q.difficulty === 'VG').length,
    categories: [...new Set(ALL_OMTENTA_QUESTIONS.map(q => q.category))],
    byCategory: {
        sshBrandvagg: SSH_BRANDVAGG_QUESTIONS.length,
        storage: STORAGE_QUESTIONS.length,
        docker: DOCKER_QUESTIONS.length,
        anvandarhantering: ANVANDARHANTERING_QUESTIONS.length,
        filsystem: FILSYSTEM_QUESTIONS.length,
        pakethantering: PAKETHANTERING_QUESTIONS.length,
        subnetting: SUBNETTING_QUESTIONS.length
    }
}
