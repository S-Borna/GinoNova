/**
 * ============================================================================
 * API INDEX — Centralized API Exports
 * ============================================================================
 *
 * Re-exports all API modules for clean imports.
 *
 * @phase A.3 - App Shell & Routing
 */

// Core client
export { api, apiRequest, API_BASE_URL } from "./client"
export type { ApiResult, ApiSuccess, ApiFailure } from "./client"

// Domain APIs
export * from "./tracks"
