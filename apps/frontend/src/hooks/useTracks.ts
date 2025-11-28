/**
 * ============================================================================
 * USE TRACKS — Track Data Hooks
 * ============================================================================
 *
 * React Query hooks for fetching track data.
 *
 * @phase A.4 - Data Fetching & State
 */

import { useQuery } from "@tanstack/react-query"
import { queryKeys } from "@/lib/queryClient"
import { api } from "@/lib/api/client"
import {
    getTracks,
    getTrack,
    getTrackProgress,
    getMockTracks,
    getMockTrack,
    type Track,
    type TrackSummary,
} from "@/lib/api/tracks"

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Fetch all tracks
 */
export function useTracks() {
    return useQuery({
        queryKey: queryKeys.tracks,
        queryFn: async () => {
            const result = await getTracks()
            if (!result.ok) {
                // Fall back to mock data in development
                if (process.env.NODE_ENV === "development") {
                    console.warn("Using mock tracks data")
                    return getMockTracks()
                }
                throw new Error(result.message)
            }
            return result.data
        },
        // Tracks rarely change, cache for longer
        staleTime: 1000 * 60 * 10, // 10 minutes
    })
}

/**
 * Fetch a single track with its modules
 */
export function useTrack(slug: string) {
    return useQuery({
        queryKey: queryKeys.track(slug),
        queryFn: async () => {
            const result = await getTrack(slug)
            if (!result.ok) {
                // Fall back to mock data in development
                if (process.env.NODE_ENV === "development") {
                    console.warn("Using mock track data")
                    const mockTrack = getMockTrack(slug)
                    if (!mockTrack) {
                        throw new Error("Track not found")
                    }
                    return mockTrack
                }
                throw new Error(result.message)
            }
            return result.data
        },
        enabled: !!slug,
        staleTime: 1000 * 60 * 10, // 10 minutes
    })
}

/**
 * Fetch user's track progress
 */
export function useTrackProgress() {
    return useQuery({
        queryKey: queryKeys.trackProgress,
        queryFn: async () => {
            const result = await getTrackProgress()
            if (!result.ok) {
                // Return mock progress in development
                if (process.env.NODE_ENV === "development") {
                    return {
                        currentTrack: "linux-fundamentals",
                        currentModule: "user-permissions",
                        overallProgress: 25,
                        tracks: getMockTracks(),
                    }
                }
                throw new Error(result.message)
            }
            return result.data
        },
        // Progress should be relatively fresh
        staleTime: 1000 * 60 * 2, // 2 minutes
        // Refetch when window regains focus
        refetchOnWindowFocus: true,
    })
}
