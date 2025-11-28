/**
 * ============================================================================
 * QUERY CLIENT — React Query Configuration
 * ============================================================================
 *
 * Centralized query client with caching and retry strategies.
 *
 * @phase A.4 - Data Fetching & State
 */

import { QueryClient } from "@tanstack/react-query"

export const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            // Stale time: how long data is considered fresh
            staleTime: 1000 * 60 * 5, // 5 minutes

            // Cache time: how long to keep unused data in cache
            gcTime: 1000 * 60 * 30, // 30 minutes (formerly cacheTime)

            // Retry failed requests
            retry: 2,
            retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),

            // Refetch on window focus for fresh data
            refetchOnWindowFocus: true,

            // Don't refetch on mount if data is fresh
            refetchOnMount: true,

            // Network mode
            networkMode: "online",
        },
        mutations: {
            // Retry mutations once
            retry: 1,

            // Network mode
            networkMode: "online",
        },
    },
})

/* ============================================================================
   QUERY KEYS
   ============================================================================ */

export const queryKeys = {
    // User
    user: ["user"] as const,
    userById: (id: string) => ["user", id] as const,

    // Tracks
    tracks: ["tracks"] as const,
    track: (slug: string) => ["tracks", slug] as const,
    trackProgress: ["tracks", "progress"] as const,

    // Modules
    modules: ["modules"] as const,
    modulesByTrack: (trackSlug: string) => ["modules", "track", trackSlug] as const,
    module: (id: string) => ["modules", id] as const,

    // Tasks
    tasks: ["tasks"] as const,
    tasksByModule: (moduleId: string) => ["tasks", "module", moduleId] as const,
    task: (id: string) => ["tasks", id] as const,

    // Progress
    progress: ["progress"] as const,
    progressByUser: (userId: string) => ["progress", "user", userId] as const,
    progressByModule: (moduleId: string) => ["progress", "module", moduleId] as const,

    // Studyflow / Sessions
    studyflow: ["studyflow"] as const,
    studyflowStats: ["studyflow", "stats"] as const,
    studyflowSettings: ["studyflow", "settings"] as const,
    sessions: ["sessions"] as const,
    activeSession: ["sessions", "active"] as const,
    sessionHistory: ["sessions", "history"] as const,

    // Dashboard
    dashboard: ["dashboard"] as const,
    dashboardSummary: (userId?: string) => ["dashboard", "summary", userId] as const,
} as const

/* ============================================================================
   CACHE INVALIDATION HELPERS
   ============================================================================ */

export const invalidateQueries = {
    /**
     * Invalidate all progress-related queries
     */
    progress: () => {
        queryClient.invalidateQueries({ queryKey: queryKeys.progress })
        queryClient.invalidateQueries({ queryKey: queryKeys.dashboard })
    },

    /**
     * Invalidate task completion related queries
     */
    taskComplete: (moduleId: string) => {
        queryClient.invalidateQueries({ queryKey: queryKeys.progress })
        queryClient.invalidateQueries({ queryKey: queryKeys.tasksByModule(moduleId) })
        queryClient.invalidateQueries({ queryKey: queryKeys.module(moduleId) })
        queryClient.invalidateQueries({ queryKey: queryKeys.dashboard })
        queryClient.invalidateQueries({ queryKey: queryKeys.trackProgress })
    },

    /**
     * Invalidate user data
     */
    user: () => {
        queryClient.invalidateQueries({ queryKey: queryKeys.user })
    },

    /**
     * Invalidate all session data
     */
    sessions: () => {
        queryClient.invalidateQueries({ queryKey: queryKeys.sessions })
    },

    /**
     * Invalidate studyflow data
     */
    studyflow: () => {
        queryClient.invalidateQueries({ queryKey: queryKeys.studyflow })
    },
}
