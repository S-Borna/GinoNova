/**
 * Dashboard API Client
 * Phase 6.0: Dashboard Foundation
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types matching backend response
export interface DashboardUser {
    id: string
    email: string
    full_name: string | null
    is_active: boolean
    is_admin: boolean
    created_at: string | null
}

export interface DashboardModule {
    id: string
    name: string
    description: string | null
    is_active: boolean
}

export interface DashboardTask {
    id: string
    module_id: string
    title: string
    difficulty: string
    is_active: boolean
}

export interface DashboardStudyflow {
    id: string
    module_id: string
    title: string
    order: number
    is_active: boolean
}

export interface DashboardProgress {
    id: string
    user_id: string
    module_id: string | null
    task_id: string | null
    studyflow_id: string | null
    status: string
    progress: number
}

export interface DashboardSystem {
    service: string
    version: string
    environment: string
}

export interface DashboardVersion {
    api_version: string
    phase: string
}

export interface DashboardStats {
    total_modules: number
    total_tasks: number
    total_studyflows: number
    total_progress_records: number
    active_modules: number
    active_tasks: number
}

export interface DashboardSummary {
    user: DashboardUser | null
    modules: DashboardModule[]
    tasks: DashboardTask[]
    studyflow: DashboardStudyflow[]
    progress: DashboardProgress[]
    system: DashboardSystem
    version: DashboardVersion
    stats: DashboardStats
}

// Standardized API response types
export interface ApiSuccess<T> {
    ok: true
    data: T
}

export interface ApiFailure {
    ok: false
    status: number
    message: string
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure

/**
 * Get dashboard summary (aggregated data)
 */
export async function getDashboardSummary(userId?: string): Promise<ApiResult<DashboardSummary>> {
    try {
        const url = userId
            ? `${API_BASE_URL}/api/dashboard/summary?user_id=${userId}`
            : `${API_BASE_URL}/api/dashboard/summary`

        const res = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch dashboard" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch dashboard" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get dashboard status
 */
export async function getDashboardStatus(): Promise<ApiResult<{ phase: string; feature: string; status: string }>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/dashboard/status`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch status" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch status" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}
