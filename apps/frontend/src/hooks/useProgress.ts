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
   MOCK DATA
   ============================================================================ */

const MOCK_USER_PROGRESS: UserProgress = {
    overall_progress: 28,
    total_xp: 2450,
    level: 7,
    xp_to_next_level: 350,
    tasks_completed: 78,
    modules_completed: 6,
    streak: 14,
    tracks: [
        {
            track_id: "linux",
            track_name: "Linux Fundamentals",
            progress: 65,
            modules_completed: 4,
            total_modules: 6,
        },
        {
            track_id: "docker",
            track_name: "Docker & Containers",
            progress: 20,
            modules_completed: 1,
            total_modules: 5,
        },
        {
            track_id: "kubernetes",
            track_name: "Kubernetes",
            progress: 0,
            modules_completed: 0,
            total_modules: 6,
        },
        {
            track_id: "cicd",
            track_name: "CI/CD Pipelines",
            progress: 0,
            modules_completed: 0,
            total_modules: 5,
        },
    ],
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
                const result = await api.get<UserProgress>("/api/v1/progress")
                if (!result.ok) {
                    // In development, use mock data silently
                    console.warn("Progress API unavailable, using mock data")
                    return MOCK_USER_PROGRESS
                }
                return result.data
            } catch (error) {
                // Network error or API not available - use mock data
                console.warn("Progress API error, using mock data:", error)
                return MOCK_USER_PROGRESS
            }
        },
        staleTime: 1000 * 60, // 1 minute
        refetchOnWindowFocus: true,
        retry: false, // Don't retry - just use mock data
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
