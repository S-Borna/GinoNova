/**
 * ============================================================================
 * @saas/ui — Design System v1.0
 * ============================================================================
 *
 * Professional design system for SaaS applications.
 * Provides tokens, components, and utilities for building consistent UIs.
 *
 * @example
 * // Import tokens
 * import { tokens, colors, spacing } from '@saas/ui'
 *
 * // Import components
 * import { PageLayout, TaskCard, CodeBlock } from '@saas/ui'
 *
 * // Use in your app
 * <PageLayout>
 *   <TaskCard title="Install Docker" type="foundation" ... />
 * </PageLayout>
 */

// ============================================================================
// TOKENS
// ============================================================================

export {
    // Unified tokens
    tokens,
    cssVars,
    classes,
    tailwindExtend,
    DESIGN_SYSTEM_VERSION,
    // Individual token modules
    colors,
    colorCssVars,
    type ColorToken,
    typography,
    typographyClasses,
    type TypographyToken,
    spacing,
    spacingClasses,
    type SpacingToken,
    shadows,
    shadowClasses,
    type ShadowToken,
    radii,
    radiiClasses,
    type RadiiToken,
} from './design-tokens'

// ============================================================================
// COMPONENTS
// ============================================================================

export {
    // Layout
    PageLayout,
    type PageLayoutProps,
    Section,
    type SectionProps,
    Block,
    type BlockProps,
    // Typography
    Headline,
    type HeadlineProps,
    Subtext,
    type SubtextProps,
    // Content
    CodeBlock,
    type CodeBlockProps,
    // Cards
    TaskCard,
    type TaskCardProps,
    type TaskType,
    type TaskStatus,
    // Pages
    TaskPage,
    type TaskPageProps,
    // Interactive (PHASE 3)
    HandsOn,
    type HandsOnProps,
    ExerciseBlock,
    type ExerciseBlockProps,
    LabBlock,
    type LabBlockProps,
    StepBox,
    type StepBoxProps,
    StepSequence,
    type StepSequenceProps,
    TerminalBlock,
    type TerminalBlockProps,
    CheckWork,
    type CheckWorkProps,
    TaskFooter,
    type TaskFooterProps,
    InfoBanner,
    type InfoBannerProps,
    WarningBanner,
    type WarningBannerProps,
    SuccessBanner,
    type SuccessBannerProps,
    // Utilities
    cn,
} from './components'
