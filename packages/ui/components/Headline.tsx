"use client"

/**
 * ============================================================================
 * HEADLINE — Design System v1.0
 * ============================================================================
 *
 * Semantic heading wrapper with typography tokens applied.
 * Auto-applies proper margin spacing above and below.
 *
 * @example
 * <Headline level={1}>Getting Started</Headline>
 * <Headline level={2}>Installation</Headline>
 */

import * as React from 'react'
import { cn } from './utils'

export interface HeadlineProps {
    children: React.ReactNode
    /** Heading level (1-4) */
    level?: 1 | 2 | 3 | 4
    /** Additional CSS classes */
    className?: string
    /** Custom ID for anchor links */
    id?: string
    /** Visual style override (use level for semantics, as for visuals) */
    as?: 1 | 2 | 3 | 4
    /** Remove default margins */
    noMargin?: boolean
}

// Typography styles from tokens
const headlineStyles = {
    1: 'text-[34px] font-semibold leading-[40px] tracking-tight text-[#111827] dark:text-white',
    2: 'text-[24px] font-medium leading-[32px] tracking-tight text-[#111827] dark:text-white',
    3: 'text-[18px] font-medium leading-[28px] text-[#111827] dark:text-white',
    4: 'text-[16px] font-medium leading-[24px] text-[#111827] dark:text-white',
}

// Margin spacing
const headlineMargins = {
    1: 'mt-0 mb-6',    // H1: no top margin, 24px bottom
    2: 'mt-10 mb-4',   // H2: 40px top, 16px bottom
    3: 'mt-8 mb-3',    // H3: 32px top, 12px bottom
    4: 'mt-6 mb-2',    // H4: 24px top, 8px bottom
}

export function Headline({
    children,
    level = 2,
    className,
    id,
    as,
    noMargin = false,
}: HeadlineProps) {
    const visualLevel = as || level
    const Tag = `h${level}` as 'h1' | 'h2' | 'h3' | 'h4'

    return (
        <Tag
            id={id}
            className={cn(
                // Typography
                headlineStyles[visualLevel],
                // Margins
                !noMargin && headlineMargins[visualLevel],
                // First child removes top margin
                'first:mt-0',
                className
            )}
        >
            {children}
        </Tag>
    )
}

export default Headline
