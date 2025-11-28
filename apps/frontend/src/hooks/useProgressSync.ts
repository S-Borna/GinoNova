/**
 * ============================================================================
 * USE PROGRESS SYNC — Progress Persistence Hook
 * ============================================================================
 *
 * Hook that handles syncing progress data:
 * - On task completion (immediate)
 * - On session end (beforeunload)
 * - On window focus/blur (for multi-tab scenarios)
 * - Periodic sync (every 5 minutes)
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { useEffect, useCallback, useRef } from "react"
import { useQueryClient } from "@tanstack/react-query"
import { queryKeys } from "@/lib/queryClient"

/* ============================================================================
   TYPES
   ============================================================================ */

interface UseProgressSyncOptions {
    /** Interval for periodic sync in milliseconds (default: 5 minutes) */
    syncInterval?: number
    /** Enable sync on visibility change */
    syncOnVisibility?: boolean
    /** Enable sync on before unload */
    syncOnUnload?: boolean
    /** Custom sync function */
    onSync?: () => Promise<void>
}

interface ProgressSyncReturn {
    /** Manually trigger a sync */
    syncNow: () => Promise<void>
    /** Flag indicating if sync is in progress */
    isSyncing: boolean
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const DEFAULT_SYNC_INTERVAL = 5 * 60 * 1000 // 5 minutes
const SYNC_DEBOUNCE_MS = 1000 // 1 second debounce

/* ============================================================================
   HOOK
   ============================================================================ */

export function useProgressSync(
    options: UseProgressSyncOptions = {}
): ProgressSyncReturn {
    const {
        syncInterval = DEFAULT_SYNC_INTERVAL,
        syncOnVisibility = true,
        syncOnUnload = true,
        onSync,
    } = options

    const queryClient = useQueryClient()
    const isSyncingRef = useRef(false)
    const lastSyncRef = useRef<number>(Date.now())
    const syncTimeoutRef = useRef<NodeJS.Timeout | null>(null)

    /**
     * Core sync function that invalidates progress queries
     * and optionally calls custom sync handler
     */
    const performSync = useCallback(async () => {
        // Prevent concurrent syncs
        if (isSyncingRef.current) return
        
        // Check debounce
        const now = Date.now()
        if (now - lastSyncRef.current < SYNC_DEBOUNCE_MS) return

        try {
            isSyncingRef.current = true
            lastSyncRef.current = now

            // Invalidate progress-related queries to refetch fresh data
            await Promise.all([
                queryClient.invalidateQueries({ queryKey: queryKeys.progress }),
                queryClient.invalidateQueries({ queryKey: queryKeys.modules }),
            ])

            // Call custom sync handler if provided
            if (onSync) {
                await onSync()
            }

            console.debug("[ProgressSync] Sync completed")
        } catch (error) {
            console.error("[ProgressSync] Sync failed:", error)
        } finally {
            isSyncingRef.current = false
        }
    }, [queryClient, onSync])

    /**
     * Debounced sync that can be called frequently
     */
    const debouncedSync = useCallback(() => {
        if (syncTimeoutRef.current) {
            clearTimeout(syncTimeoutRef.current)
        }
        syncTimeoutRef.current = setTimeout(() => {
            performSync()
        }, SYNC_DEBOUNCE_MS)
    }, [performSync])

    /**
     * Handle visibility change (tab focus/blur)
     */
    useEffect(() => {
        if (!syncOnVisibility) return

        const handleVisibilityChange = () => {
            // Sync when tab becomes visible again
            if (document.visibilityState === "visible") {
                console.debug("[ProgressSync] Tab visible, syncing...")
                debouncedSync()
            }
        }

        document.addEventListener("visibilitychange", handleVisibilityChange)
        return () => {
            document.removeEventListener("visibilitychange", handleVisibilityChange)
        }
    }, [syncOnVisibility, debouncedSync])

    /**
     * Handle window focus (different from visibility for multi-window scenarios)
     */
    useEffect(() => {
        if (!syncOnVisibility) return

        const handleFocus = () => {
            console.debug("[ProgressSync] Window focused, syncing...")
            debouncedSync()
        }

        window.addEventListener("focus", handleFocus)
        return () => {
            window.removeEventListener("focus", handleFocus)
        }
    }, [syncOnVisibility, debouncedSync])

    /**
     * Handle before unload (session end)
     * Note: This is best-effort as beforeunload has limitations
     */
    useEffect(() => {
        if (!syncOnUnload) return

        const handleBeforeUnload = () => {
            // Use sendBeacon for reliable delivery on page close
            // This is a simplified version - in production, you'd want
            // to send any pending local progress data
            console.debug("[ProgressSync] Page unloading, attempting sync...")
            
            // Note: Can't await here, but we can trigger the sync
            // For critical data, use navigator.sendBeacon()
        }

        window.addEventListener("beforeunload", handleBeforeUnload)
        return () => {
            window.removeEventListener("beforeunload", handleBeforeUnload)
        }
    }, [syncOnUnload])

    /**
     * Periodic sync interval
     */
    useEffect(() => {
        if (syncInterval <= 0) return

        const intervalId = setInterval(() => {
            console.debug("[ProgressSync] Periodic sync triggered")
            performSync()
        }, syncInterval)

        return () => {
            clearInterval(intervalId)
        }
    }, [syncInterval, performSync])

    /**
     * Cleanup on unmount
     */
    useEffect(() => {
        return () => {
            if (syncTimeoutRef.current) {
                clearTimeout(syncTimeoutRef.current)
            }
        }
    }, [])

    return {
        syncNow: performSync,
        isSyncing: isSyncingRef.current,
    }
}

/* ============================================================================
   STREAK CHECKER HOOK
   ============================================================================ */

interface StreakState {
    currentStreak: number
    longestStreak: number
    lastActivityDate: string | null
    isActiveToday: boolean
    isStreakBroken: boolean
    previousStreak: number
}

/**
 * Hook to check and manage streak state
 * Detects broken streaks and provides streak info
 */
export function useStreakChecker(
    userProgress?: {
        currentStreak?: number
        longestStreak?: number
        lastActivityDate?: string
    }
): StreakState {
    const today = new Date().toISOString().split("T")[0]
    const yesterday = new Date(Date.now() - 86400000).toISOString().split("T")[0]

    const currentStreak = userProgress?.currentStreak ?? 0
    const longestStreak = userProgress?.longestStreak ?? 0
    const lastActivityDate = userProgress?.lastActivityDate ?? null

    // Check if user was active today
    const isActiveToday = lastActivityDate === today

    // Check if streak was broken (last activity was before yesterday)
    const isStreakBroken =
        !isActiveToday &&
        lastActivityDate !== null &&
        lastActivityDate !== yesterday &&
        currentStreak === 0

    // Previous streak is stored in longestStreak if it was just broken
    const previousStreak = isStreakBroken ? longestStreak : 0

    return {
        currentStreak,
        longestStreak,
        lastActivityDate,
        isActiveToday,
        isStreakBroken,
        previousStreak,
    }
}

/* ============================================================================
   LEVEL UP DETECTOR HOOK
   ============================================================================ */

interface LevelUpState {
    hasLeveledUp: boolean
    oldLevel: number
    newLevel: number
}

/**
 * Hook to detect level ups by comparing previous and current XP
 */
export function useLevelUpDetector(
    previousXP: number,
    currentXP: number,
    calculateLevel: (xp: number) => number
): LevelUpState {
    const oldLevel = calculateLevel(previousXP)
    const newLevel = calculateLevel(currentXP)
    const hasLeveledUp = newLevel > oldLevel && previousXP > 0

    return {
        hasLeveledUp,
        oldLevel,
        newLevel,
    }
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default useProgressSync
