/**
 * ============================================================================
 * STUDYFLOW LIB — Barrel Exports
 * ============================================================================
 * @phase A.6 - Studyflow Integration
 */

export {
    // Types
    type SessionState,
    type SessionEvent,
    type SessionMode,
    type SessionSettings,
    type SessionContext,
    type SessionTransition,
    // Constants
    DEFAULT_SETTINGS,
    PRESET_MODES,
    // Functions
    createInitialContext,
    transition,
    canTransition,
    getNextState,
    isLongBreak,
    getCurrentBreakDuration,
    formatTime,
    formatDuration,
    calculateProgress,
} from "./sessionMachine"
