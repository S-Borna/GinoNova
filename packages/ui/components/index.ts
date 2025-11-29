/**
 * ============================================================================
 * COMPONENT EXPORTS — Design System v1.0
 * ============================================================================
 */

// Layout components
export { PageLayout, type PageLayoutProps } from './PageLayout'
export { Section, type SectionProps } from './Section'
export { Block, type BlockProps } from './Block'

// Typography components
export { Headline, type HeadlineProps } from './Headline'
export { Subtext, type SubtextProps } from './Subtext'

// Content components
export { CodeBlock, type CodeBlockProps } from './CodeBlock'

// Card components
export { TaskCard, type TaskCardProps, type TaskType, type TaskStatus } from './TaskCard'

// Page components
export { TaskPage, type TaskPageProps } from './TaskPage'

// Interactive components (PHASE 3)
export {
    // Hands-on learning
    HandsOn,
    type HandsOnProps,
    ExerciseBlock,
    type ExerciseBlockProps,
    LabBlock,
    type LabBlockProps,
    // Step-based guides
    StepBox,
    type StepBoxProps,
    StepSequence,
    type StepSequenceProps,
    // Terminal
    TerminalBlock,
    type TerminalBlockProps,
    // Verification
    CheckWork,
    type CheckWorkProps,
    // Navigation
    TaskFooter,
    type TaskFooterProps,
    // Banners
    InfoBanner,
    type InfoBannerProps,
    WarningBanner,
    type WarningBannerProps,
    SuccessBanner,
    type SuccessBannerProps,
} from './interactive'

// Utilities
export { cn } from './utils'
