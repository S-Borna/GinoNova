/**
 * ============================================================================
 * CONTENT COMPONENTS - Barrel Export
 * ============================================================================
 *
 * Export all content-related components:
 * - MarkdownRenderer
 * - CodeBlock
 * - TaskNav
 * - OutcomeChecklist (C.3)
 * - Hints (C.3)
 * - TerminalEmulator (ILE Phase 2)
 *
 * @phase C.2 - Task Content Display
 * @phase C.3 - Labs & Projects Display
 * @phase ILE Phase 2 - Interactive Terminal
 */

export { MarkdownRenderer } from "./MarkdownRenderer"
export { CodeBlock, InlineCode } from "./CodeBlock"
export { TaskNav } from "./TaskNav"
export { OutcomeChecklist } from "./OutcomeChecklist"
export type { OutcomeItem } from "./OutcomeChecklist"
export { Hints } from "./Hints"
export type { HintItem } from "./Hints"
export { TerminalEmulator } from "./TerminalEmulator"
export type { TerminalCommand, TerminalEmulatorProps } from "./TerminalEmulator"
