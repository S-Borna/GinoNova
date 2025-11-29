"use client"

/**
 * ============================================================================
 * SUBTEXT — Design System v1.0
 * ============================================================================
 *
 * Light grey text for instructions, captions, and secondary content.
 * Used above code blocks ("Run the command below:").
 *
 * @example
 * <Subtext>Run the following command to install dependencies:</Subtext>
 * <CodeBlock>npm install</CodeBlock>
 */

import * as React from 'react'
import { cn } from './utils'

export interface SubtextProps {
    children: React.ReactNode
    /** Additional CSS classes */
    className?: string
    /** Size variant */
    size?: 'sm' | 'md' | 'lg'
    /** Text color variant */
    variant?: 'secondary' | 'tertiary' | 'muted'
    /** HTML element to render as */
    as?: 'p' | 'span' | 'div'
    /** Apply margin for code block spacing */
    beforeCode?: boolean
}

const sizeMap = {
    sm: 'text-sm leading-5',    // 14px
    md: 'text-base leading-6',  // 16px
    lg: 'text-lg leading-7',    // 18px
}

const variantMap = {
    secondary: 'text-[#6B7280] dark:text-neutral-400',
    tertiary: 'text-[#9CA3AF] dark:text-neutral-500',
    muted: 'text-[#9CA3AF] dark:text-neutral-500 italic',
}

export function Subtext({
    children,
    className,
    size = 'md',
    variant = 'secondary',
    as: Component = 'p',
    beforeCode = false,
}: SubtextProps) {
    return (
        <Component
            className={cn(
                // Typography
                sizeMap[size],
                variantMap[variant],
                // Code block spacing (28px = text-above-code token)
                beforeCode && 'mb-7',
                className
            )}
        >
            {children}
        </Component>
    )
}

export default Subtext
