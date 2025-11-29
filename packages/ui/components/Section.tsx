"use client"

/**
 * ============================================================================
 * SECTION — Design System v1.0
 * ============================================================================
 *
 * Provides consistent vertical spacing between content segments.
 * Used within PageLayout for logical content grouping.
 *
 * @example
 * <Section>
 *   <Headline>Introduction</Headline>
 *   <Block>...</Block>
 * </Section>
 */

import * as React from 'react'
import { cn } from './utils'

export interface SectionProps {
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
    /** Section padding variant */
    spacing?: 'none' | 'sm' | 'md' | 'lg'
    /** Add border at bottom */
    bordered?: boolean
    /** Background variant */
    background?: 'transparent' | 'surface' | 'muted'
    /** HTML element to render as */
    as?: 'section' | 'div' | 'article'
    /** Section ID for navigation */
    id?: string
}

const spacingMap = {
    none: '',
    sm: 'py-4',      // 16px
    md: 'py-8',      // 32px (default - Tesla-level)
    lg: 'py-12',     // 48px
}

const backgroundMap = {
    transparent: '',
    surface: 'bg-[#F6F8FA] dark:bg-neutral-800/50 rounded-2xl px-6',
    muted: 'bg-gray-50 dark:bg-neutral-900 rounded-xl px-5',
}

export function Section({
    children,
    className,
    spacing = 'md',
    bordered = false,
    background = 'transparent',
    as: Component = 'section',
    id,
}: SectionProps) {
    return (
        <Component
            id={id}
            className={cn(
                // Base
                'w-full',
                // Spacing
                spacingMap[spacing],
                // Background
                backgroundMap[background],
                // Border
                bordered && 'border-b border-[rgba(0,0,0,0.08)] dark:border-neutral-800',
                className
            )}
        >
            {children}
        </Component>
    )
}

export default Section
