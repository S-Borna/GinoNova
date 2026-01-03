"use client"

/**
 * Client-side Providers wrapper
 * Consolidates all client-side providers to prevent SSR issues during static generation.
 * Phase OAuth: Added NextAuthProvider for social login support
 */

import type { ReactNode } from "react"
import { ThemeProvider } from "next-themes"
import { AuthProvider, NextAuthProvider } from "@/components/auth"
import { QueryProvider } from "@/providers/QueryProvider"
import { ExamModeProvider } from "@/contexts/ExamModeContext"
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
            <NextAuthProvider>
                <QueryProvider>
                    <AuthProvider>
                        <ExamModeProvider>
                            {children}
                        </ExamModeProvider>
                    </AuthProvider>
                </QueryProvider>
            </NextAuthProvider>
            <Toaster position="top-right" richColors closeButton />
        </ThemeProvider>
    )
}

export default Providers
