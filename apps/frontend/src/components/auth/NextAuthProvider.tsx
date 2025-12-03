"use client"

/**
 * ============================================================================
 * NEXTAUTH SESSION PROVIDER — OAuth Session Wrapper
 * ============================================================================
 *
 * Wraps the application with NextAuth SessionProvider for OAuth support.
 *
 * @phase OAuth Integration
 */

import { SessionProvider } from "next-auth/react"

interface NextAuthProviderProps {
    children: React.ReactNode
}

export function NextAuthProvider({ children }: NextAuthProviderProps) {
    return <SessionProvider>{children}</SessionProvider>
}
