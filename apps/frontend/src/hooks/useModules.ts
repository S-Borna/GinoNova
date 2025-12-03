/**
 * ============================================================================
 * USE MODULES — Module Data Hooks
 * ============================================================================
 *
 * React Query hooks for fetching module data.
 *
 * @phase A.4 - Data Fetching & State
 */

import { useQuery } from "@tanstack/react-query"
import { queryKeys } from "@/lib/queryClient"
import { api } from "@/lib/api/client"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface Module {
    id: string
    slug: string
    name: string
    description?: string
    order: number
    track_id?: string
    is_active: boolean
    created_at: string
    updated_at?: string
}

export interface ModuleWithProgress extends Module {
    progress: number
    tasks_completed: number
    total_tasks: number
    labs_completed: number
    total_labs: number
    is_locked: boolean
    estimated_hours: number
}

export interface ModuleDetail extends ModuleWithProgress {
    tasks: Task[]
    labs: Lab[]
    project?: Project
}

export interface Task {
    id: string
    title: string
    description?: string
    order: number
    xp_reward: number
    estimated_minutes: number
    is_completed: boolean
    is_locked: boolean
}

export interface Lab {
    id: string
    title: string
    description?: string
    order: number
    xp_reward: number
    estimated_minutes: number
    difficulty: "beginner" | "intermediate" | "advanced"
    is_completed: boolean
    is_locked: boolean
}

export interface Project {
    id: string
    title: string
    description?: string
    xp_reward: number
    is_completed: boolean
    is_locked: boolean
}

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_MODULES: ModuleWithProgress[] = [
    {
        id: "1",
        slug: "terminal-basics",
        name: "Terminal Basics",
        description: "Navigate the command line with confidence",
        order: 1,
        is_active: true,
        created_at: new Date().toISOString(),
        progress: 100,
        tasks_completed: 8,
        total_tasks: 8,
        labs_completed: 2,
        total_labs: 2,
        is_locked: false,
        estimated_hours: 3,
    },
    {
        id: "2",
        slug: "file-system",
        name: "File System",
        description: "Understand the Linux file hierarchy",
        order: 2,
        is_active: true,
        created_at: new Date().toISOString(),
        progress: 100,
        tasks_completed: 10,
        total_tasks: 10,
        labs_completed: 3,
        total_labs: 3,
        is_locked: false,
        estimated_hours: 4,
    },
    {
        id: "3",
        slug: "user-permissions",
        name: "User & Permissions",
        description: "Manage users, groups, and file permissions",
        order: 3,
        is_active: true,
        created_at: new Date().toISOString(),
        progress: 40,
        tasks_completed: 4,
        total_tasks: 10,
        labs_completed: 1,
        total_labs: 3,
        is_locked: false,
        estimated_hours: 5,
    },
    {
        id: "4",
        slug: "process-management",
        name: "Process Management",
        description: "Control and monitor system processes",
        order: 4,
        is_active: true,
        created_at: new Date().toISOString(),
        progress: 0,
        tasks_completed: 0,
        total_tasks: 8,
        labs_completed: 0,
        total_labs: 2,
        is_locked: true,
        estimated_hours: 3,
    },
]

/* ============================================================================
   HOOKS
   ============================================================================ */

/**
 * Fetch all modules
 */
export function useModules() {
    return useQuery({
        queryKey: queryKeys.modules,
        queryFn: async () => {
            try {
                // Direct fetch to backend - CORRECT URL without /v1/
                const response = await fetch("http://localhost:8000/api/modules/")
                if (!response.ok) {
                    console.warn("Modules API unavailable, using mock data")
                    return MOCK_MODULES
                }
                const data = await response.json()
                // Transform backend data to match expected interface
                return data.map((mod: Record<string, unknown>) => ({
                    id: mod.id,
                    slug: mod.slug,
                    name: mod.name,
                    description: mod.description || "",
                    order: mod.order || 0,
                    is_active: mod.is_active !== false,
                    created_at: mod.created_at || new Date().toISOString(),
                    progress: mod.progress || 0,
                    tasks_completed: mod.tasks_completed || 0,
                    total_tasks: mod.total_tasks || mod.task_count || 0,
                    labs_completed: 0,
                    total_labs: 0,
                    is_locked: false,
                    estimated_hours: mod.estimated_hours || 2,
                })) as ModuleWithProgress[]
            } catch (error) {
                console.warn("Modules API error, using mock data:", error)
                return MOCK_MODULES
            }
        },
        staleTime: 1000 * 60 * 5, // 5 minutes
        retry: false,
    })
}

/**
 * Fetch modules by track
 */
export function useModulesByTrack(trackSlug: string) {
    return useQuery({
        queryKey: queryKeys.modulesByTrack(trackSlug),
        queryFn: async () => {
            const result = await api.get<ModuleWithProgress[]>(
                `/api/v1/tracks/${trackSlug}/modules`
            )
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    console.warn("Using mock modules data")
                    return MOCK_MODULES
                }
                throw new Error(result.message)
            }
            return result.data
        },
        enabled: !!trackSlug,
        staleTime: 1000 * 60 * 5, // 5 minutes
    })
}

/**
 * Fetch single module with tasks and labs
 */
export function useModule(moduleId: string) {
    return useQuery({
        queryKey: queryKeys.module(moduleId),
        queryFn: async () => {
            const result = await api.get<ModuleDetail>(`/api/v1/modules/${moduleId}`)
            if (!result.ok) {
                if (process.env.NODE_ENV === "development") {
                    console.warn("Using mock module detail data")
                    const mockModule = MOCK_MODULES.find(
                        (m) => m.id === moduleId || m.slug === moduleId
                    )
                    if (!mockModule) {
                        throw new Error("Module not found")
                    }
                    return {
                        ...mockModule,
                        tasks: [
                            {
                                id: "t1",
                                title: "Understanding the Basics",
                                description: "Learn the fundamentals",
                                order: 1,
                                xp_reward: 25,
                                estimated_minutes: 15,
                                is_completed: true,
                                is_locked: false,
                            },
                            {
                                id: "t2",
                                title: "Hands-on Practice",
                                description: "Apply what you learned",
                                order: 2,
                                xp_reward: 30,
                                estimated_minutes: 20,
                                is_completed: false,
                                is_locked: false,
                            },
                        ],
                        labs: [
                            {
                                id: "l1",
                                title: "Lab: Practical Exercise",
                                description: "Complete the lab exercise",
                                order: 1,
                                xp_reward: 50,
                                estimated_minutes: 30,
                                difficulty: "beginner" as const,
                                is_completed: false,
                                is_locked: false,
                            },
                        ],
                    } as ModuleDetail
                }
                throw new Error(result.message)
            }
            return result.data
        },
        enabled: !!moduleId,
        staleTime: 1000 * 60 * 2, // 2 minutes
    })
}
