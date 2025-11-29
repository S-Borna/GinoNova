"use client"

/**
 * Client-side Providers wrapper
 * Consolidates all client-side providers to prevent SSR issues during static generation.
 */

import type { ReactNode } from "react"
import { ThemeProvider } from "next-themes"
import { AuthProvider } from "@/components/auth"
import { QueryProvider } from "@/providers/QueryProvider"
import { Toaster } from "@/components/ui/sonner"
import { AppInitializer } from "@/components/AppInitializer"

interface ProvidersProps {
    children: ReactNode
}

export function Providers({ children }: ProvidersProps) {
    return (
        <ThemeProvider
            attribute="class"
            defaultTheme="dark"
            enableSystem={false}
            disableTransitionOnChange
        >
            <AppInitializer />
            <QueryProvider>
                <AuthProvider>{children}</AuthProvider>
            </QueryProvider>
            <Toaster position="top-right" richColors closeButton />
        </ThemeProvider>
    )
}

export default Providers
