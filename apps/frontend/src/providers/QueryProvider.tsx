"use client"

/**
 * ============================================================================
 * QUERY PROVIDER — React Query Provider Wrapper
 * ============================================================================
 *
 * Wraps the app with React Query context for data fetching.
 *
 * @phase A.4 - Data Fetching & State
 */

import { QueryClientProvider } from "@tanstack/react-query"
import dynamic from "next/dynamic"
import { queryClient } from "@/lib/queryClient"

// Dynamically import devtools only in development (client-side)
const ReactQueryDevtools = dynamic(
    () =>
        import("@tanstack/react-query-devtools").then(
            (mod) => mod.ReactQueryDevtools
        ),
    { ssr: false }
)

interface QueryProviderProps {
    children: React.ReactNode
}

export function QueryProvider({ children }: QueryProviderProps) {
    return (
        <QueryClientProvider client={queryClient}>
            {children}
            {process.env.NODE_ENV === "development" && (
                <ReactQueryDevtools initialIsOpen={false} position="bottom" />
            )}
        </QueryClientProvider>
    )
}
