/**
 * ============================================================================
 * LEARNING COMPONENTS - Barrel Export
 * ============================================================================
 *
 * Interactive Learning Engine components:
 * - TextBlock: Markdown content
 * - LearningCodeBlock: Syntax-highlighted code
 * - QuizBlock: Multiple choice questions
 * - CheckpointBlock: Progress milestones
 * - ContentBlockRenderer: Renders all block types
 *
 * @phase ILE Phase 3 - Content Blocks
 */

export { TextBlock } from "./TextBlock"
export type { TextBlockProps } from "./TextBlock"

export { LearningCodeBlock } from "./CodeBlock"
export type { LearningCodeBlockProps } from "./CodeBlock"

export { QuizBlock } from "./QuizBlock"
export type { QuizBlockProps, QuizOption } from "./QuizBlock"

export { CheckpointBlock } from "./CheckpointBlock"
export type { CheckpointBlockProps } from "./CheckpointBlock"

export { ContentBlockRenderer } from "./ContentBlockRenderer"
export type { ContentBlockRendererProps } from "./ContentBlockRenderer"
