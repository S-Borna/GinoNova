/**
 * ============================================================================
 * SPACING TOKENS — Design System v1.0
 * ============================================================================
 *
 * Tesla-level precision spacing system.
 * Based on 8px grid with specific task page requirements.
 */

export const spacing = {
    // Base unit (8px grid)
    px: '1px',
    0: '0',
    0.5: '2px',
    1: '4px',
    1.5: '6px',
    2: '8px',
    2.5: '10px',
    3: '12px',
    3.5: '14px',
    4: '16px',
    5: '20px',
    6: '24px',
    7: '28px',
    8: '32px',
    9: '36px',
    10: '40px',
    11: '44px',
    12: '48px',
    14: '56px',
    16: '64px',
    20: '80px',
    24: '96px',
    28: '112px',
    32: '128px',

    // Semantic spacing tokens
    section: '32px',           // Section vertical padding
    blockGap: '24px',          // Gap between blocks
    textAboveCode: '28px',     // Space between text and code block
    textBelowCode: '16px',     // Space after code block
    cardPadding: '20px',       // Internal card padding
    cardGap: '16px',           // Gap between cards
    inlinePadding: '16px',     // Horizontal padding for inline elements

    // Layout constraints
    maxWidth: {
        content: '840px',        // Main content max-width
        narrow: '640px',         // Narrow content (forms, etc.)
        wide: '1200px',          // Wide layouts
        full: '100%',
    },

    // Responsive breakpoint-aware spacing
    responsive: {
        section: {
            mobile: '24px',
            tablet: '32px',
            desktop: '32px',
        },
        blockGap: {
            mobile: '16px',
            tablet: '20px',
            desktop: '24px',
        },
    },
} as const

// Tailwind class mappings
export const spacingClasses = {
    section: 'py-8',           // 32px
    sectionX: 'px-4 md:px-6',  // Horizontal padding
    blockGap: 'mb-6',          // 24px
    textAboveCode: 'mb-7',     // 28px
    textBelowCode: 'mt-4',     // 16px
    cardPadding: 'p-5',        // 20px
    contentMax: 'max-w-[840px]',
    narrowMax: 'max-w-[640px]',
    wideMax: 'max-w-[1200px]',
} as const

export type SpacingToken = keyof typeof spacing
