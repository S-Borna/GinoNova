/**
 * ============================================================================
 * API CLIENT — Centralized HTTP Client
 * ============================================================================
 *
 * Base API client with auth token handling, error handling, and typing.
 *
 * @phase A.3 - App Shell & Routing
 * @updated A.4 - Enhanced error handling and auth refresh
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ApiSuccess<T> {
    ok: true
    data: T
}

export interface ApiFailure {
    ok: false
    status: number
    message: string
    code?: string
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure

interface RequestOptions extends RequestInit {
    skipAuth?: boolean
}

/* ============================================================================
   ERROR CODES
   ============================================================================ */

export const ApiErrorCodes = {
    UNAUTHORIZED: "UNAUTHORIZED",
    FORBIDDEN: "FORBIDDEN",
    NOT_FOUND: "NOT_FOUND",
    VALIDATION_ERROR: "VALIDATION_ERROR",
    NETWORK_ERROR: "NETWORK_ERROR",
    SERVER_ERROR: "SERVER_ERROR",
    RATE_LIMITED: "RATE_LIMITED",
} as const

/* ============================================================================
   TOKEN MANAGEMENT
   ============================================================================ */

function getAuthToken(): string | null {
    if (typeof window === "undefined") return null
    return localStorage.getItem("auth_token")
}

function clearAuthToken(): void {
    if (typeof window === "undefined") return
    localStorage.removeItem("auth_token")
    localStorage.removeItem("refresh_token")
}

/* ============================================================================
   AUTH EVENT EMITTER
   ============================================================================ */

type AuthEventListener = (event: "logout" | "session_expired") => void
const authEventListeners: AuthEventListener[] = []

export function onAuthEvent(listener: AuthEventListener): () => void {
    authEventListeners.push(listener)
    return () => {
        const index = authEventListeners.indexOf(listener)
        if (index > -1) authEventListeners.splice(index, 1)
    }
}

function emitAuthEvent(event: "logout" | "session_expired") {
    authEventListeners.forEach((listener) => listener(event))
}

/* ============================================================================
   ERROR CODE MAPPING
   ============================================================================ */

function getErrorCode(status: number): string {
    switch (status) {
        case 401:
            return ApiErrorCodes.UNAUTHORIZED
        case 403:
            return ApiErrorCodes.FORBIDDEN
        case 404:
            return ApiErrorCodes.NOT_FOUND
        case 422:
            return ApiErrorCodes.VALIDATION_ERROR
        case 429:
            return ApiErrorCodes.RATE_LIMITED
        default:
            return status >= 500 ? ApiErrorCodes.SERVER_ERROR : ApiErrorCodes.NETWORK_ERROR
    }
}

/* ============================================================================
   BASE REQUEST FUNCTION
   ============================================================================ */

export async function apiRequest<T>(
    endpoint: string,
    options: RequestOptions = {}
): Promise<ApiResult<T>> {
    const { skipAuth = false, ...fetchOptions } = options

    const headers: HeadersInit = {
        "Content-Type": "application/json",
        ...(fetchOptions.headers || {}),
    }

    // Add auth token if available and not skipped
    if (!skipAuth) {
        const token = getAuthToken()
        if (token) {
            ; (headers as Record<string, string>)["Authorization"] = `Bearer ${token}`
        }
    }

    try {
        const res = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...fetchOptions,
            headers,
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Request failed" }))
            const errorCode = getErrorCode(res.status)

            // Handle unauthorized - emit event for auth providers to handle
            if (res.status === 401) {
                clearAuthToken()
                emitAuthEvent("session_expired")
            }

            return {
                ok: false,
                status: res.status,
                message: error.detail || error.message || "Request failed",
                code: errorCode,
            }
        }

        // Handle no-content responses
        if (res.status === 204) {
            return { ok: true, data: undefined as T }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return {
            ok: false,
            status: 0,
            message: error instanceof Error ? error.message : "Network error",
            code: ApiErrorCodes.NETWORK_ERROR,
        }
    }
}

/* ============================================================================
   CONVENIENCE METHODS
   ============================================================================ */

export const api = {
    get: <T>(endpoint: string, options?: RequestOptions) =>
        apiRequest<T>(endpoint, { method: "GET", ...options }),

    post: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "POST",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    put: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "PUT",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions) =>
        apiRequest<T>(endpoint, {
            method: "PATCH",
            body: body ? JSON.stringify(body) : undefined,
            ...options,
        }),

    delete: <T>(endpoint: string, options?: RequestOptions) =>
        apiRequest<T>(endpoint, { method: "DELETE", ...options }),
}

export { API_BASE_URL }
