/**
 * ============================================================================
 * ANALYTICS UTILITIES
 * ============================================================================
 *
 * Basic analytics tracking for DevOpsHub.
 * Privacy-respecting, lightweight tracking for key metrics.
 *
 * Can be extended with GA4, Mixpanel, Posthog, etc.
 *
 * @phase A.8 - Testing & Launch Prep
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export interface AnalyticsEvent {
  name: string;
  properties?: Record<string, unknown>;
  timestamp: string;
  sessionId: string;
  userId?: string;
  url: string;
  referrer?: string;
}

export interface PageView extends AnalyticsEvent {
  name: 'page_view';
  properties: {
    path: string;
    title: string;
    duration?: number;
  };
}

export interface UserAction extends AnalyticsEvent {
  name: string;
  properties: {
    action: string;
    category: string;
    label?: string;
    value?: number;
    [key: string]: unknown;
  };
}

/* ============================================================================
   SESSION MANAGEMENT
   ============================================================================ */

const SESSION_KEY = 'ginonova_analytics_session';
const SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes

interface Session {
  id: string;
  startedAt: string;
  lastActiveAt: string;
  pageViews: number;
}

function generateSessionId(): string {
  return `sess_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
}

function getSession(): Session {
  if (typeof window === 'undefined') {
    return {
      id: 'server',
      startedAt: new Date().toISOString(),
      lastActiveAt: new Date().toISOString(),
      pageViews: 0,
    };
  }

  try {
    const stored = sessionStorage.getItem(SESSION_KEY);
    if (stored) {
      const session = JSON.parse(stored) as Session;
      const lastActive = new Date(session.lastActiveAt).getTime();
      const now = Date.now();

      // Check if session is still valid
      if (now - lastActive < SESSION_TIMEOUT) {
        session.lastActiveAt = new Date().toISOString();
        sessionStorage.setItem(SESSION_KEY, JSON.stringify(session));
        return session;
      }
    }
  } catch {
    // Session storage unavailable
  }

  // Create new session
  const newSession: Session = {
    id: generateSessionId(),
    startedAt: new Date().toISOString(),
    lastActiveAt: new Date().toISOString(),
    pageViews: 0,
  };

  try {
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(newSession));
  } catch {
    // Storage unavailable
  }

  return newSession;
}

function updateSession(updates: Partial<Session>): void {
  if (typeof window === 'undefined') return;

  try {
    const session = getSession();
    const updated = { ...session, ...updates, lastActiveAt: new Date().toISOString() };
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(updated));
  } catch {
    // Storage unavailable
  }
}

/* ============================================================================
   EVENT QUEUE
   ============================================================================ */

const EVENT_QUEUE_KEY = 'ginonova_analytics_queue';
const MAX_QUEUE_SIZE = 100;

let eventQueue: AnalyticsEvent[] = [];

function queueEvent(event: AnalyticsEvent): void {
  eventQueue.push(event);

  // Persist to localStorage for offline support
  if (typeof window !== 'undefined') {
    try {
      const trimmed = eventQueue.slice(-MAX_QUEUE_SIZE);
      localStorage.setItem(EVENT_QUEUE_KEY, JSON.stringify(trimmed));
    } catch {
      // Storage full
    }
  }

  // Log in development
  if (process.env.NODE_ENV === 'development') {
    console.log('[Analytics]', event.name, event.properties);
  }
}

function loadQueuedEvents(): void {
  if (typeof window === 'undefined') return;

  try {
    const stored = localStorage.getItem(EVENT_QUEUE_KEY);
    if (stored) {
      eventQueue = JSON.parse(stored);
    }
  } catch {
    eventQueue = [];
  }
}

/* ============================================================================
   TRACKING FUNCTIONS
   ============================================================================ */

let currentUserId: string | undefined;

/**
 * Set the current user ID for tracking
 */
export function identifyUser(userId: string): void {
  currentUserId = userId;

  queueEvent({
    name: 'user_identified',
    properties: { userId },
    timestamp: new Date().toISOString(),
    sessionId: getSession().id,
    userId,
    url: typeof window !== 'undefined' ? window.location.href : '',
  });
}

/**
 * Clear user identification (on logout)
 */
export function clearUser(): void {
  currentUserId = undefined;
}

/**
 * Track a page view
 */
export function trackPageView(path?: string, title?: string): void {
  const session = getSession();
  updateSession({ pageViews: session.pageViews + 1 });

  const event: PageView = {
    name: 'page_view',
    properties: {
      path: path || (typeof window !== 'undefined' ? window.location.pathname : ''),
      title: title || (typeof document !== 'undefined' ? document.title : ''),
    },
    timestamp: new Date().toISOString(),
    sessionId: session.id,
    userId: currentUserId,
    url: typeof window !== 'undefined' ? window.location.href : '',
    referrer: typeof document !== 'undefined' ? document.referrer : undefined,
  };

  queueEvent(event);
}

/**
 * Track a user action
 */
export function trackAction(
  action: string,
  category: string,
  properties?: Record<string, unknown>
): void {
  const session = getSession();

  const event: UserAction = {
    name: 'user_action',
    properties: {
      action,
      category,
      ...properties,
    },
    timestamp: new Date().toISOString(),
    sessionId: session.id,
    userId: currentUserId,
    url: typeof window !== 'undefined' ? window.location.href : '',
  };

  queueEvent(event);
}

/**
 * Track a custom event
 */
export function trackEvent(
  name: string,
  properties?: Record<string, unknown>
): void {
  const session = getSession();

  const event: AnalyticsEvent = {
    name,
    properties,
    timestamp: new Date().toISOString(),
    sessionId: session.id,
    userId: currentUserId,
    url: typeof window !== 'undefined' ? window.location.href : '',
  };

  queueEvent(event);
}

/* ============================================================================
   PREDEFINED EVENTS
   ============================================================================ */

// Auth events
export const trackSignUp = () => trackAction('sign_up', 'auth');
export const trackLogin = () => trackAction('login', 'auth');
export const trackLogout = () => trackAction('logout', 'auth');

// Module events
export const trackModuleStart = (moduleId: string, moduleName: string) =>
  trackAction('module_start', 'learning', { moduleId, moduleName });

export const trackModuleComplete = (moduleId: string, moduleName: string, xpEarned: number) =>
  trackAction('module_complete', 'learning', { moduleId, moduleName, xpEarned });

// Task events
export const trackTaskComplete = (taskId: string, taskType: string, xpEarned: number) =>
  trackAction('task_complete', 'learning', { taskId, taskType, xpEarned });

// Studyflow events
export const trackStudyflowStart = (mode: string, duration: number) =>
  trackAction('studyflow_start', 'studyflow', { mode, duration });

export const trackStudyflowComplete = (
  mode: string,
  focusTime: number,
  tasksCompleted: number,
  xpEarned: number
) =>
  trackAction('studyflow_complete', 'studyflow', {
    mode,
    focusTime,
    tasksCompleted,
    xpEarned,
  });

// Achievement events
export const trackLevelUp = (newLevel: number, totalXp: number) =>
  trackAction('level_up', 'achievement', { newLevel, totalXp });

export const trackStreakMilestone = (streakDays: number) =>
  trackAction('streak_milestone', 'achievement', { streakDays });

/* ============================================================================
   INITIALIZATION
   ============================================================================ */

let isInitialized = false;

/**
 * Initialize analytics
 * Call once at app startup
 */
export function initializeAnalytics(): void {
  if (isInitialized || typeof window === 'undefined') return;

  loadQueuedEvents();

  // Track initial page view
  trackPageView();

  // Track page views on navigation (for SPAs)
  if (typeof window !== 'undefined') {
    // For Next.js App Router, you may want to use a different approach
    // This is a basic implementation that listens for popstate
    window.addEventListener('popstate', () => {
      trackPageView();
    });
  }

  isInitialized = true;
  console.log('[Analytics] Initialized');
}

/* ============================================================================
   UTILITY FUNCTIONS
   ============================================================================ */

/**
 * Get all queued events (for debugging or export)
 */
export function getQueuedEvents(): AnalyticsEvent[] {
  return [...eventQueue];
}

/**
 * Clear event queue
 */
export function clearEventQueue(): void {
  eventQueue = [];
  if (typeof window !== 'undefined') {
    localStorage.removeItem(EVENT_QUEUE_KEY);
  }
}

/**
 * Get session info
 */
export function getSessionInfo(): Session {
  return getSession();
}

/**
 * Get analytics summary
 */
export function getAnalyticsSummary(): {
  sessionId: string;
  pageViews: number;
  eventCount: number;
  sessionDuration: number;
} {
  const session = getSession();
  const startTime = new Date(session.startedAt).getTime();
  const now = Date.now();

  return {
    sessionId: session.id,
    pageViews: session.pageViews,
    eventCount: eventQueue.length,
    sessionDuration: Math.floor((now - startTime) / 1000),
  };
}

/* ============================================================================
   EXPORT
   ============================================================================ */

const analytics = {
  initializeAnalytics,
  identifyUser,
  clearUser,
  trackPageView,
  trackAction,
  trackEvent,
  // Predefined events
  trackSignUp,
  trackLogin,
  trackLogout,
  trackModuleStart,
  trackModuleComplete,
  trackTaskComplete,
  trackStudyflowStart,
  trackStudyflowComplete,
  trackLevelUp,
  trackStreakMilestone,
  // Utilities
  getQueuedEvents,
  clearEventQueue,
  getSessionInfo,
  getAnalyticsSummary,
};

export default analytics;
