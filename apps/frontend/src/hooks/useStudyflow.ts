/**
 * ============================================================================
 * USE STUDYFLOW — Studyflow Session Hooks
 * ============================================================================
 *
 * React Query hooks for managing studyflow sessions (pomodoro-style study
 * sessions with Spotify integration).
 *
 * @phase A.4 - Data Fetching & State
 */

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { queryKeys, invalidateQueries } from "@/lib/queryClient"
import { api } from "@/lib/api/client"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface StudyflowSession {
    id: string
    user_id: string
    module_id?: string
    task_id?: string
    status: "idle" | "focus" | "break" | "long_break" | "completed"
    focus_duration: number // minutes
    break_duration: number // minutes
    long_break_duration: number // minutes
    sessions_until_long_break: number
    current_session: number
    total_focus_time: number // seconds
    started_at?: string
    paused_at?: string
    completed_at?: string
    spotify_playlist_id?: string
}

export interface StudyflowStats {
    today_focus_time: number // minutes
    weekly_focus_time: number // minutes
    total_sessions: number
    total_focus_time: number // minutes
    average_session_length: number
    longest_streak: number
    favorite_time_of_day: string
}

export interface StudyflowSettings {
    focus_duration: number
    break_duration: number
    long_break_duration: number
    sessions_until_long_break: number
    auto_start_breaks: boolean
    auto_start_focus: boolean
    sound_enabled: boolean
    spotify_enabled: boolean
    default_playlist_id?: string
}

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_SESSION: StudyflowSession = {
    id: "mock-session",
    user_id: "demo",
    status: "idle",
    focus_duration: 25,
    break_duration: 5,
    long_break_duration: 15,
    sessions_until_long_break: 4,
    current_session: 0,
    total_focus_time: 0,
}

const MOCK_STATS: StudyflowStats = {
    today_focus_time: 75,
    weekly_focus_time: 420,
    total_sessions: 156,
    total_focus_time: 3900,
    average_session_length: 25,
    longest_streak: 8,
    favorite_time_of_day: "morning",
}

const MOCK_SETTINGS: StudyflowSettings = {
    focus_duration: 25,
    break_duration: 5,
    long_break_duration: 15,
    sessions_until_long_break: 4,
    auto_start_breaks: false,
    auto_start_focus: false,
    sound_enabled: true,
    spotify_enabled: false,
}

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Get current active session or default
 */
export function useStudyflowSession() {
    return useQuery({
        queryKey: queryKeys.studyflow,
        queryFn: async () => {
            const result = await api.get<StudyflowSession>("/api/v1/studyflow/session")
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    console.warn("Using mock studyflow session")
                    return MOCK_SESSION
                }
                throw new Error(result.message)
            }
            return result.data
        },
        staleTime: 0, // Always refetch (session state is critical)
        refetchOnWindowFocus: true,
    })
}

/**
 * Get studyflow statistics
 */
export function useStudyflowStats() {
    return useQuery({
        queryKey: [...queryKeys.studyflow, "stats"],
        queryFn: async () => {
            const result = await api.get<StudyflowStats>("/api/v1/studyflow/stats")
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    return MOCK_STATS
                }
                throw new Error(result.message)
            }
            return result.data
        },
        staleTime: 1000 * 60 * 5, // 5 minutes
    })
}

/**
 * Get studyflow settings
 */
export function useStudyflowSettings() {
    return useQuery({
        queryKey: [...queryKeys.studyflow, "settings"],
        queryFn: async () => {
            const result = await api.get<StudyflowSettings>(
                "/api/v1/studyflow/settings"
            )
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    return MOCK_SETTINGS
                }
                throw new Error(result.message)
            }
            return result.data
        },
        staleTime: 1000 * 60 * 10, // 10 minutes
    })
}

/**
 * Start a new focus session
 */
export function useStartSession() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async (data?: { module_id?: string; task_id?: string }) => {
            const result = await api.post<StudyflowSession>(
                "/api/v1/studyflow/start",
                data
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: () => {
            invalidateQueries.studyflow()
        },
    })
}

/**
 * Pause current session
 */
export function usePauseSession() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async () => {
            const result = await api.post<StudyflowSession>(
                "/api/v1/studyflow/pause"
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onMutate: async () => {
            await queryClient.cancelQueries({ queryKey: queryKeys.studyflow })
            const previous = queryClient.getQueryData<StudyflowSession>(
                queryKeys.studyflow
            )

            if (previous) {
                queryClient.setQueryData<StudyflowSession>(queryKeys.studyflow, {
                    ...previous,
                    paused_at: new Date().toISOString(),
                })
            }

            return { previous }
        },
        onError: (_err, _vars, context) => {
            if (context?.previous) {
                queryClient.setQueryData(queryKeys.studyflow, context.previous)
            }
        },
        onSettled: () => {
            invalidateQueries.studyflow()
        },
    })
}

/**
 * Resume paused session
 */
export function useResumeSession() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async () => {
            const result = await api.post<StudyflowSession>(
                "/api/v1/studyflow/resume"
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onMutate: async () => {
            await queryClient.cancelQueries({ queryKey: queryKeys.studyflow })
            const previous = queryClient.getQueryData<StudyflowSession>(
                queryKeys.studyflow
            )

            if (previous) {
                queryClient.setQueryData<StudyflowSession>(queryKeys.studyflow, {
                    ...previous,
                    paused_at: undefined,
                })
            }

            return { previous }
        },
        onError: (_err, _vars, context) => {
            if (context?.previous) {
                queryClient.setQueryData(queryKeys.studyflow, context.previous)
            }
        },
        onSettled: () => {
            invalidateQueries.studyflow()
        },
    })
}

/**
 * Complete current focus/break session
 */
export function useCompleteSession() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async () => {
            const result = await api.post<StudyflowSession>(
                "/api/v1/studyflow/complete"
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: () => {
            invalidateQueries.studyflow()
            invalidateQueries.progress() // Progress may update after completing a session
        },
    })
}

/**
 * Skip current break session
 */
export function useSkipBreak() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async () => {
            const result = await api.post<StudyflowSession>("/api/v1/studyflow/skip")
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: () => {
            invalidateQueries.studyflow()
        },
    })
}

/**
 * Update studyflow settings
 */
export function useUpdateSettings() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async (settings: Partial<StudyflowSettings>) => {
            const result = await api.put<StudyflowSettings>(
                "/api/v1/studyflow/settings",
                settings
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: (data) => {
            queryClient.setQueryData([...queryKeys.studyflow, "settings"], data)
        },
    })
}

/**
 * Reset/abandon current session
 */
export function useResetSession() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async () => {
            const result = await api.post<StudyflowSession>("/api/v1/studyflow/reset")
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: () => {
            invalidateQueries.studyflow()
        },
    })
}
