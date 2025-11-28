/**
 * ============================================================================
 * USE USER — Current User Data Hook
 * ============================================================================
 *
 * React Query hook for fetching and managing current user data.
 *
 * @phase A.4 - Data Fetching & State
 */

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { queryKeys } from "@/lib/queryClient"
import { api } from "@/lib/api/client"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface User {
    id: string
    email: string
    full_name?: string
    avatar_url?: string
    role: "user" | "admin"
    is_active: boolean
    created_at: string
    updated_at?: string
    // Progress stats
    level?: number
    total_xp?: number
    streak?: number
}

export interface UpdateUserData {
    full_name?: string
    avatar_url?: string
}

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Fetch current user data
 */
export function useUser() {
    return useQuery({
        queryKey: queryKeys.user,
        queryFn: async () => {
            const result = await api.get<User>("/api/v1/users/me")
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        // User data should be fresh
        staleTime: 1000 * 60 * 2, // 2 minutes
        // Don't retry on 401 (unauthorized)
        retry: (failureCount, error) => {
            if (error instanceof Error && error.message.includes("401")) {
                return false
            }
            return failureCount < 2
        },
    })
}

/**
 * Fetch user by ID
 */
export function useUserById(userId: string) {
    return useQuery({
        queryKey: queryKeys.userById(userId),
        queryFn: async () => {
            const result = await api.get<User>(`/api/v1/users/${userId}`)
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        enabled: !!userId,
    })
}

/**
 * Update current user profile
 */
export function useUpdateUser() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: async (data: UpdateUserData) => {
            const result = await api.patch<User>("/api/v1/users/me", data)
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        onSuccess: (data) => {
            // Update user cache
            queryClient.setQueryData(queryKeys.user, data)
        },
    })
}

/**
 * Get user stats (level, XP, streak)
 */
export function useUserStats() {
    return useQuery({
        queryKey: [...queryKeys.user, "stats"],
        queryFn: async () => {
            const result = await api.get<{
                level: number
                total_xp: number
                xp_to_next_level: number
                streak: number
                tasks_completed: number
                modules_completed: number
            }>("/api/v1/users/me/stats")
            if (!result.ok) {
                throw new Error(result.message)
            }
            return result.data
        },
        staleTime: 1000 * 60, // 1 minute
    })
}
