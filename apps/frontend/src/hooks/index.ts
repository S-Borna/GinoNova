/**
 * ============================================================================
 * HOOKS — Centralized Exports
 * ============================================================================
 *
 * Re-exports all custom hooks from a single location.
 *
 * @phase A.4 - Data Fetching & State, A.5 - Progress & Completion Logic
 */

// Auth hooks (from AuthProvider)
export { useAuth } from "@/components/auth/AuthProvider"

// Session timer and favorites
export { useSessionTimer } from "./useSessionTimer"
export { useFavorites, type FavoriteItem } from "./useFavorites"

// User hooks
export {
    useUser,
    useUserById,
    useUpdateUser,
    useUserStats,
    type User,
    type UpdateUserData,
} from "./useUser"

// Track hooks
export {
    useTracks,
    useTrack,
    useTrackProgress,
} from "./useTracks"

// Module hooks
export {
    useModules,
    useModulesByTrack,
    useModule,
    type Module,
    type ModuleWithProgress,
    type ModuleDetail,
    type Task,
    type Lab,
    type Project,
} from "./useModules"

// Progress hooks
export {
    useProgress,
    useModuleProgress,
    useCompleteTask,
    useUpdateProgress,
    type UserProgress,
    type TrackProgress,
    type ProgressRecord,
    type TaskCompletionResponse,
} from "./useProgress"

// Studyflow hooks
export {
    useStudyflowSession,
    useStudyflowStats,
    useStudyflowSettings,
    useStartSession,
    usePauseSession,
    useResumeSession,
    useCompleteSession,
    useSkipBreak,
    useUpdateSettings,
    useResetSession,
    type StudyflowSession,
    type StudyflowStats,
    type StudyflowSettings,
} from "./useStudyflow"

// Progress sync hooks (A.5)
export {
    useProgressSync,
    useStreakChecker,
    useLevelUpDetector,
} from "./useProgressSync"

// Studyflow session management hooks (A.6)
export { useTimer, type UseTimerOptions, type UseTimerReturn } from "./useTimer"
export { useStudyflowSession as useStudyflowSessionManager } from "./useStudyflowSession"
export { useStudyflowShortcuts, type KeyboardShortcut } from "./useStudyflowShortcuts"
export { useNotifications } from "./useNotifications"

// Platform/OS hooks (FAS-3.1)
export {
    useOperatingSystem,
    usePlatform,
    OS_OPTIONS,
    LINUX_DISTROS,
    filterContentByPlatform,
    getInstallCommand,
    type OperatingSystem,
    type LinuxDistro,
    type PlatformConfig,
} from "./useOperatingSystem"

// Bookmark hooks (PROMPT 4)
export { useBookmarks } from "./useBookmarks"
