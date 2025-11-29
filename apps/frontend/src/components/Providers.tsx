"use client"

/**
 * Minimal Providers for testing
 */

import type { ReactNode } from "react"

interface ProvidersProps {
    children: ReactNode
}

export function Providers({ children }: ProvidersProps) {
    return <>{children}</>
}

export default Providers
