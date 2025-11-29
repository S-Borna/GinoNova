"use client"

/**
 * ============================================================================
 * PAGE LAYOUT — Design System v1.0
 * ============================================================================
 *
 * Main page wrapper that:
 * - Centers content with max-width 840px
 * - Applies consistent vertical padding (32px)
 * - Uses white background
 * - Responsive horizontal padding
 *
 * @example
 * <PageLayout>
 *   <Section>...</Section>
 * </PageLayout>
 */

import * as React from 'react'
import { cn } from './utils'

export interface PageLayoutProps {
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
    /** Maximum width variant */
    maxWidth?: 'narrow' | 'content' | 'standard' | 'wide' | 'full'
    /** Background color */
    background?: 'white' | 'gray' | 'transparent' | 'subtle' | 'gradient'
    /** Remove default padding */
    noPadding?: boolean
    /** HTML element to render as */
    as?: 'div' | 'main' | 'article' | 'section'
}

const maxWidthMap = {
    narrow: 'max-w-[640px]',
    content: 'max-w-[840px]',
    standard: 'max-w-4xl', // ~896px, matches typical prose width
    wide: 'max-w-[1200px]',
    full: 'max-w-full',
}

const backgroundMap = {
    white: 'bg-white dark:bg-neutral-900',
    gray: 'bg-gray-50 dark:bg-neutral-950',
    transparent: 'bg-transparent',
    subtle: 'bg-neutral-50/50 dark:bg-neutral-950/50',
    gradient: 'bg-gradient-to-br from-white via-neutral-50 to-indigo-50/30 dark:from-neutral-900 dark:via-neutral-950 dark:to-indigo-950/20',
}

export function PageLayout({
    children,
    className,
    maxWidth = 'content',
    background = 'white',
    noPadding = false,
    as: Component = 'main',
}: PageLayoutProps) {
    return (
        <Component
            className={cn(
                // Base layout
                'w-full min-h-screen',
                backgroundMap[background],
                className
            )}
        >
            <div
                className={cn(
                    // Centering
                    'mx-auto w-full',
                    maxWidthMap[maxWidth],
                    // Padding
                    !noPadding && [
                        'px-4 sm:px-6 lg:px-8',  // Responsive horizontal
                        'py-8',                    // 32px vertical
                    ]
                )}
            >
                {children}
            </div>
        </Component>
    )
}

export default PageLayout
