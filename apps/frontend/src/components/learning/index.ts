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
 * - LessonContent: Enhanced markdown lesson view
 *
 * @phase ILE Phase 3 - Content Blocks
 * @phase 4.1 - Enhanced Learning Experience
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

export { LessonContent } from "./LessonContent"

// V2 Interactive Learning Components
export { InteractiveNodeV2 } from "./InteractiveNodeV2"
export * from "./blocks"
