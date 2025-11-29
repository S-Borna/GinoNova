/**
 * ============================================================================
 * BORDER RADIUS TOKENS — Design System v1.0
 * ============================================================================
 *
 * Consistent rounded corners matching Material 3 / Apple aesthetic.
 */

export const radii = {
    // Base values
    none: '0',
    sm: '4px',
    md: '6px',
    DEFAULT: '8px',
    lg: '10px',
    xl: '12px',
    '2xl': '16px',
    '3xl': '20px',
    '4xl': '24px',
    full: '9999px',

    // Semantic radii
    soft: '8px',           // Buttons, inputs
    card: '16px',          // Cards, panels
    code: '12px',          // Code blocks
    badge: '6px',          // Badges, tags
    avatar: '9999px',      // Avatars, circles
    modal: '20px',         // Modals, dialogs
    tooltip: '8px',        // Tooltips
    button: '10px',        // Buttons
    input: '8px',          // Form inputs

    // Component-specific
    taskCard: '16px',
    codeBlock: '12px',
    moduleCard: '16px',
    dashboard: '20px',
} as const

// Tailwind class mappings
export const radiiClasses = {
    soft: 'rounded-lg',        // 8px
    card: 'rounded-2xl',       // 16px
    code: 'rounded-xl',        // 12px
    badge: 'rounded-md',       // 6px
    avatar: 'rounded-full',
    modal: 'rounded-[20px]',
    button: 'rounded-[10px]',
    input: 'rounded-lg',
} as const

export type RadiiToken = keyof typeof radii
