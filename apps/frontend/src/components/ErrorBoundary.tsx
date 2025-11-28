/**
 * ============================================================================
 * ERROR BOUNDARY — React Error Handling
 * ============================================================================
 *
 * Error boundary component to catch and display errors gracefully.
 *
 * @phase A.4 - Data Fetching & State
 */

"use client"

import { Component, type ReactNode } from "react"
import { AlertTriangle, RefreshCw, Home } from "lucide-react"
import { Button } from "@/components/ui/button"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ErrorBoundaryProps {
    children: ReactNode
    fallback?: ReactNode
    onError?: (error: Error, errorInfo: React.ErrorInfo) => void
    resetKeys?: unknown[]
}

interface ErrorBoundaryState {
    hasError: boolean
    error: Error | null
}

/* ============================================================================
   ERROR BOUNDARY CLASS COMPONENT
   ============================================================================ */

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
    constructor(props: ErrorBoundaryProps) {
        super(props)
        this.state = { hasError: false, error: null }
    }

    static getDerivedStateFromError(error: Error): ErrorBoundaryState {
        return { hasError: true, error }
    }

    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
        // Log error to console in development
        if (process.env.NODE_ENV === "development") {
            console.error("ErrorBoundary caught an error:", error, errorInfo)
        }

        // Call custom error handler if provided
        this.props.onError?.(error, errorInfo)
    }

    componentDidUpdate(prevProps: ErrorBoundaryProps) {
        // Reset error state if resetKeys change
        if (this.state.hasError && this.props.resetKeys) {
            const hasResetKeyChanged = this.props.resetKeys.some(
                (key, index) => key !== prevProps.resetKeys?.[index]
            )
            if (hasResetKeyChanged) {
                this.reset()
            }
        }
    }

    reset = () => {
        this.setState({ hasError: false, error: null })
    }

    render() {
        if (this.state.hasError) {
            if (this.props.fallback) {
                return this.props.fallback
            }

            return (
                <DefaultErrorFallback
                    error={this.state.error}
                    onReset={this.reset}
                />
            )
        }

        return this.props.children
    }
}

/* ============================================================================
   DEFAULT FALLBACK UI
   ============================================================================ */

interface DefaultErrorFallbackProps {
    error: Error | null
    onReset: () => void
}

function DefaultErrorFallback({ error, onReset }: DefaultErrorFallbackProps) {
    return (
        <div className="flex min-h-[400px] flex-col items-center justify-center p-8 text-center">
            <div className="mb-6 rounded-full bg-destructive/10 p-4">
                <AlertTriangle className="h-12 w-12 text-destructive" />
            </div>

            <h2 className="mb-2 text-2xl font-bold">Something went wrong</h2>

            <p className="mb-6 max-w-md text-muted-foreground">
                {error?.message || "An unexpected error occurred. Please try again."}
            </p>

            <div className="flex gap-4">
                <Button onClick={onReset} variant="outline">
                    <RefreshCw className="mr-2 h-4 w-4" />
                    Try Again
                </Button>
                <Button onClick={() => (window.location.href = "/dashboard")} variant="default">
                    <Home className="mr-2 h-4 w-4" />
                    Go to Dashboard
                </Button>
            </div>

            {process.env.NODE_ENV === "development" && error && (
                <details className="mt-8 max-w-lg text-left">
                    <summary className="cursor-pointer text-sm text-muted-foreground">
                        Error Details (Development Only)
                    </summary>
                    <pre className="mt-2 overflow-auto rounded-md bg-muted p-4 text-xs">
                        {error.stack}
                    </pre>
                </details>
            )}
        </div>
    )
}

/* ============================================================================
   QUERY ERROR FALLBACK
   ============================================================================ */

interface QueryErrorFallbackProps {
    error: Error
    onRetry: () => void
}

export function QueryErrorFallback({ error, onRetry }: QueryErrorFallbackProps) {
    return (
        <div className="flex flex-col items-center justify-center p-8 text-center">
            <AlertTriangle className="mb-4 h-8 w-8 text-destructive" />
            <h3 className="mb-2 font-semibold">Failed to load data</h3>
            <p className="mb-4 text-sm text-muted-foreground">{error.message}</p>
            <Button onClick={onRetry} size="sm" variant="outline">
                <RefreshCw className="mr-2 h-4 w-4" />
                Retry
            </Button>
        </div>
    )
}

/* ============================================================================
   EMPTY STATE COMPONENT
   ============================================================================ */

interface EmptyStateProps {
    icon?: ReactNode
    title: string
    description?: string
    action?: {
        label: string
        onClick: () => void
    }
}

export function EmptyState({ icon, title, description, action }: EmptyStateProps) {
    return (
        <div className="flex flex-col items-center justify-center p-8 text-center">
            {icon && (
                <div className="mb-4 rounded-full bg-muted p-4">
                    {icon}
                </div>
            )}
            <h3 className="mb-2 font-semibold">{title}</h3>
            {description && (
                <p className="mb-4 max-w-sm text-sm text-muted-foreground">
                    {description}
                </p>
            )}
            {action && (
                <Button onClick={action.onClick} size="sm">
                    {action.label}
                </Button>
            )}
        </div>
    )
}

/* ============================================================================
   LOADING SKELETON COMPONENTS
   ============================================================================ */

export function CardSkeleton() {
    return (
        <div className="animate-pulse rounded-lg border bg-card p-6">
            <div className="mb-4 h-4 w-2/3 rounded bg-muted" />
            <div className="space-y-2">
                <div className="h-3 w-full rounded bg-muted" />
                <div className="h-3 w-4/5 rounded bg-muted" />
            </div>
        </div>
    )
}

export function ModuleCardSkeleton() {
    return (
        <div className="animate-pulse rounded-lg border bg-card p-6">
            <div className="flex items-start gap-4">
                <div className="h-12 w-12 rounded-lg bg-muted" />
                <div className="flex-1">
                    <div className="mb-2 h-5 w-1/2 rounded bg-muted" />
                    <div className="mb-4 h-3 w-3/4 rounded bg-muted" />
                    <div className="h-2 w-full rounded bg-muted" />
                </div>
            </div>
        </div>
    )
}

export function DashboardSkeleton() {
    return (
        <div className="space-y-6">
            {/* Stats row */}
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
                {[...Array(4)].map((_, i) => (
                    <div key={i} className="animate-pulse rounded-lg border bg-card p-6">
                        <div className="mb-2 h-4 w-1/3 rounded bg-muted" />
                        <div className="h-8 w-1/2 rounded bg-muted" />
                    </div>
                ))}
            </div>

            {/* Main content */}
            <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
                <div className="lg:col-span-2">
                    <div className="animate-pulse rounded-lg border bg-card p-6">
                        <div className="mb-4 h-6 w-1/4 rounded bg-muted" />
                        <div className="space-y-3">
                            {[...Array(3)].map((_, i) => (
                                <div key={i} className="h-16 rounded bg-muted" />
                            ))}
                        </div>
                    </div>
                </div>
                <div className="animate-pulse rounded-lg border bg-card p-6">
                    <div className="mb-4 h-6 w-1/2 rounded bg-muted" />
                    <div className="h-40 rounded bg-muted" />
                </div>
            </div>
        </div>
    )
}

export function TableSkeleton({ rows = 5 }: { rows?: number }) {
    return (
        <div className="animate-pulse rounded-lg border">
            {/* Header */}
            <div className="flex gap-4 border-b bg-muted/50 p-4">
                <div className="h-4 w-1/4 rounded bg-muted" />
                <div className="h-4 w-1/4 rounded bg-muted" />
                <div className="h-4 w-1/4 rounded bg-muted" />
                <div className="h-4 w-1/4 rounded bg-muted" />
            </div>
            {/* Rows */}
            {[...Array(rows)].map((_, i) => (
                <div key={i} className="flex gap-4 border-b p-4 last:border-0">
                    <div className="h-4 w-1/4 rounded bg-muted" />
                    <div className="h-4 w-1/4 rounded bg-muted" />
                    <div className="h-4 w-1/4 rounded bg-muted" />
                    <div className="h-4 w-1/4 rounded bg-muted" />
                </div>
            ))}
        </div>
    )
}
