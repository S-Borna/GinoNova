/**
 * ============================================================================
 * STUDYFLOW COMPONENTS BARREL EXPORT
 * ============================================================================
 * 
 * Export all studyflow-related components for easy imports:
 * import { Timer, SessionSetup, ActiveSession, ... } from "@/components/studyflow"
 * 
 * @phase D.5 - Studyflow UI, A.6 - Studyflow Integration
 */

// Timer Component
export { Timer, MiniTimer } from "./Timer"
export type { TimerProps, MiniTimerProps } from "./Timer"

// Session Setup Component
export { SessionSetup } from "./SessionSetup"
export type { SessionSetupProps, SessionConfig, SessionMode, TaskOption } from "./SessionSetup"

// Active Session Component
export { ActiveSession } from "./ActiveSession"
export type { ActiveSessionProps } from "./ActiveSession"

// Session Complete Modal
export { SessionComplete } from "./SessionComplete"
export type { SessionCompleteProps, SessionSummary } from "./SessionComplete"

// Streak Display Component
export { StreakDisplay } from "./StreakDisplay"
export type { StreakDisplayProps } from "./StreakDisplay"

// Session History Component
export { SessionHistory } from "./SessionHistory"
export type { SessionHistoryProps, SessionRecord } from "./SessionHistory"

// A.6 — Studyflow Integration Components
// Task Panel for focus sessions
export { TaskPanel } from "./TaskPanel"

// Break Screen with activities
export { BreakScreen } from "./BreakScreen"

// Session Summary at end
export { SessionSummary as SessionSummaryView } from "./SessionSummary"

// Keyboard Shortcuts Help
export { KeyboardShortcutsHelp } from "./KeyboardShortcutsHelp"
