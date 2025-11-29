/**
 * ============================================================================
 * DESIGN TOKENS — Unified Export
 * ============================================================================
 *
 * Single source of truth for all design tokens.
 * Import this file for complete access to the design system.
 *
 * @example
 * import { tokens } from '@saas/ui/tokens'
 * const cardRadius = tokens.radii.card
 */

import { colors, colorCssVars, type ColorToken } from './colors'
import { typography, typographyClasses, type TypographyToken } from './typography'
import { spacing, spacingClasses, type SpacingToken } from './spacing'
import { shadows, shadowClasses, type ShadowToken } from './shadows'
import { radii, radiiClasses, type RadiiToken } from './radii'

// Unified tokens object
export const tokens = {
    colors,
    typography,
    spacing,
    shadows,
    radii,
} as const

// CSS variable mappings
export const cssVars = {
    ...colorCssVars,
} as const

// Tailwind class presets
export const classes = {
    typography: typographyClasses,
    spacing: spacingClasses,
    shadows: shadowClasses,
    radii: radiiClasses,
} as const

// Re-export individual token modules
export { colors, colorCssVars, type ColorToken }
export { typography, typographyClasses, type TypographyToken }
export { spacing, spacingClasses, type SpacingToken }
export { shadows, shadowClasses, type ShadowToken }
export { radii, radiiClasses, type RadiiToken }

// Design system version
export const DESIGN_SYSTEM_VERSION = '1.0.0'

// Theme configuration for Tailwind extend
export const tailwindExtend = {
    colors: {
        primary: colors.primary,
        surface: colors.surface,
        border: colors.border,
    },
    spacing: {
        section: spacing.section,
        'block-gap': spacing.blockGap,
    },
    borderRadius: {
        card: radii.card,
        code: radii.code,
        soft: radii.soft,
    },
    boxShadow: {
        card: shadows.card,
        'card-hover': shadows.cardHover,
        code: shadows.code,
    },
    fontFamily: {
        sans: typography.fontFamily.sans,
        display: typography.fontFamily.display,
        mono: typography.fontFamily.mono,
    },
    maxWidth: {
        content: spacing.maxWidth.content,
        narrow: spacing.maxWidth.narrow,
        wide: spacing.maxWidth.wide,
    },
} as const
