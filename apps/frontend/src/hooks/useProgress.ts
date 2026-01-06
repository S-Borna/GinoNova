/**
 * ============================================================================
 * USE PROGRESS — Progress Data Hooks
 * ============================================================================
 *
 * React Query hooks for fetching and updating user progress.
 *
 * @phase A.4 - Data Fetching & State
 */

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { queryKeys, invalidateQueries } from "@/lib/queryClient"
import { api } from "@/lib/api/client"

// FIXED: Use consistent API URL
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ProgressRecord {
    id: string
    user_id: string
    module_id?: string
    task_id?: string
    studyflow_id?: string
    progress: number
    status: "not_started" | "in_progress" | "completed"
    created_at: string
    updated_at?: string
}

export interface UserProgress {
    overall_progress: number
    total_xp: number
    level: number
    xp_to_next_level: number
    tasks_completed: number
    modules_completed: number
    streak: number
    tracks: TrackProgress[]
}

export interface TrackProgress {
    track_id: string
    track_name: string
    progress: number
    modules_completed: number
    total_modules: number
}

export interface TaskCompletionResponse {
    success: boolean
    xp_earned: number
    total_xp: number
    level_up?: {
        new_level: number
        previous_level: number
    }
    streak?: {
        current: number
        is_new_record: boolean
    }
    next_task?: {
        id: string
        title: string
        module_id: string
    }
}

/* ============================================================================
   EMPTY DEFAULT DATA — No more fake mock data!
   ============================================================================ */

const EMPTY_USER_PROGRESS: UserProgress = {
    overall_progress: 0,
    total_xp: 0,
    level: 1,
    xp_to_next_level: 1000,
    tasks_completed: 0,
    modules_completed: 0,
    streak: 0,
    tracks: [],
}

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Fetch user's overall progress
 */
export function useProgress() {
    return useQuery({
        queryKey: queryKeys.progress,
        queryFn: async () => {
            try {
                // FIXED: Use consistent API URL
                const response = await fetch(`${API_BASE_URL}/api/progress/me`)
                if (!response.ok) {
                    // API unavailable - return empty progress (NOT mock data!)
                    console.warn("Progress API unavailable, showing empty progress")
                    return EMPTY_USER_PROGRESS
                }
                const data = await response.json()
                // Transform to match expected interface
                return {
                    overall_progress: data.overall_progress || 0,
                    total_xp: data.total_xp || 0,
                    level: data.level || 1,
                    xp_to_next_level: data.xp_to_next_level || 1000,
                    tasks_completed: data.tasks_completed || 0,
                    modules_completed: data.modules_completed || 0,
                    streak: data.streak || 0,
                    tracks: data.tracks || [],
                } as UserProgress
            } catch (error) {
                // Network error or API not available - show empty state
                console.warn("Progress API error, showing empty progress:", error)
                return EMPTY_USER_PROGRESS
            }
        },
        staleTime: 1000 * 60, // 1 minute
        refetchOnWindowFocus: true,
        retry: false, // Don't retry - just use empty data
    })
}

/**
 * Fetch progress for a specific module
 */
export function useModuleProgress(moduleId: string) {
    return useQuery({
        queryKey: queryKeys.progressByModule(moduleId),
        queryFn: async () => {
            const result = await api.get<ProgressRecord>(
                `/api/v1/progress/module/${moduleId}`
            )
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    return {
                        id: "mock",
                        user_id: "demo",
                        module_id: moduleId,
                        progress: 40,
                        status: "in_progress" as const,
                        created_at: new Date().toISOString(),
                    }
                }
                throw new Error(result.message)
            }
            return result.data
        },
        enabled: !!moduleId,
        staleTime: 1000 * 60, // 1 minute
    })
}

/**
 * Mark a task as complete with optimistic updates
 */
export function useCompleteTask() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async (taskId: string) => {
            const result = await api.post<TaskCompletionResponse>(
                `/api/v1/tasks/${taskId}/complete`
            )
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },

        // Optimistic update: immediately mark task as complete
        onMutate: async (taskId) => {
            // Cancel outgoing refetches
            await queryClient.cancelQueries({ queryKey: queryKeys.progress })

            // Snapshot previous value
            const previousProgress = queryClient.getQueryData<UserProgress>(
                queryKeys.progress
            )

            // Optimistically update
            if (previousProgress) {
                queryClient.setQueryData<UserProgress>(queryKeys.progress, {
                    ...previousProgress,
                    tasks_completed: previousProgress.tasks_completed + 1,
                    total_xp: previousProgress.total_xp + 25, // Assume 25 XP
                })
            }

            return { previousProgress }
        },

        // Rollback on error
        onError: (_err, _taskId, context) => {
            if (context?.previousProgress) {
                queryClient.setQueryData(queryKeys.progress, context.previousProgress)
            }
        },

        // Refetch after success
        onSuccess: (data, taskId) => {
            // Find the module ID for this task and invalidate
            invalidateQueries.progress()
        },

        onSettled: () => {
            // Always refetch after mutation settles
            queryClient.invalidateQueries({ queryKey: queryKeys.progress })
        },
    })
}

/**
 * Update progress for a module
 */
export function useUpdateProgress() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async (data: {
            module_id: string
            progress: number
        }) => {
            const result = await api.post<ProgressRecord>("/api/v1/progress", data)
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: () => {
            invalidateQueries.progress()
        },
    })
}
