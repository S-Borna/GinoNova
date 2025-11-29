"use client"

/**
 * ============================================================================
 * BLOCK — Design System v1.0
 * ============================================================================
 *
 * Used inside Section for grouping content before code, tables, etc.
 * Applies 24px margin-bottom (block-gap token).
 *
 * @example
 * <Block>
 *   <Subtext>Run the following command:</Subtext>
 *   <CodeBlock>npm install</CodeBlock>
 * </Block>
 */

import * as React from 'react'
import { cn } from './utils'

export interface BlockProps {
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
    /** Spacing variant */
    spacing?: 'none' | 'sm' | 'md' | 'lg'
    /** HTML element to render as */
    as?: 'div' | 'article' | 'aside'
}

const spacingMap = {
    none: '',
    sm: 'mb-4',      // 16px
    md: 'mb-6',      // 24px (default - block-gap token)
    lg: 'mb-8',      // 32px
}

export function Block({
    children,
    className,
    spacing = 'md',
    as: Component = 'div',
}: BlockProps) {
    return (
        <Component
            className={cn(
                // Base spacing
                spacingMap[spacing],
                // Last child removes margin
                'last:mb-0',
                className
            )}
        >
            {children}
        </Component>
    )
}

export default Block
