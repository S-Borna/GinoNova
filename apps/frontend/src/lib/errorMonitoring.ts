/**
 * ============================================================================
 * ERROR MONITORING UTILITIES
 * ============================================================================
 *
 * Basic error tracking and logging for production.
 * Can be extended with services like Sentry, LogRocket, etc.
 *
 * @phase A.8 - Testing & Launch Prep
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ErrorLogEntry {
  id: string;
  timestamp: string;
  type: 'error' | 'warning' | 'info';
  message: string;
  stack?: string;
  context?: Record<string, unknown>;
  url?: string;
  userAgent?: string;
  userId?: string;
}

export interface APIErrorLog extends ErrorLogEntry {
  endpoint: string;
  method: string;
  statusCode?: number;
  requestBody?: unknown;
  responseBody?: unknown;
}

/* ============================================================================
   ERROR STORAGE
   ============================================================================ */

const MAX_STORED_ERRORS = 50;
const ERROR_STORAGE_KEY = 'ginonova_error_log';

function getStoredErrors(): ErrorLogEntry[] {
  if (typeof window === 'undefined') return [];
  try {
    const stored = localStorage.getItem(ERROR_STORAGE_KEY);
    return stored ? JSON.parse(stored) : [];
  } catch {
    return [];
  }
}

function storeError(error: ErrorLogEntry): void {
  if (typeof window === 'undefined') return;
  try {
    const errors = getStoredErrors();
    errors.unshift(error);
    // Keep only last N errors
    const trimmed = errors.slice(0, MAX_STORED_ERRORS);
    localStorage.setItem(ERROR_STORAGE_KEY, JSON.stringify(trimmed));
  } catch {
    // Storage full or unavailable
  }
}

/* ============================================================================
   ERROR LOGGING FUNCTIONS
   ============================================================================ */

/**
 * Generate unique error ID
 */
function generateErrorId(): string {
  return `err_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
}

/**
 * Log a general error
 */
export function logError(
  error: Error | string,
  context?: Record<string, unknown>
): ErrorLogEntry {
  const errorObj = typeof error === 'string' ? new Error(error) : error;

  const entry: ErrorLogEntry = {
    id: generateErrorId(),
    timestamp: new Date().toISOString(),
    type: 'error',
    message: errorObj.message,
    stack: errorObj.stack,
    context,
    url: typeof window !== 'undefined' ? window.location.href : undefined,
    userAgent: typeof navigator !== 'undefined' ? navigator.userAgent : undefined,
  };

  // Store locally
  storeError(entry);

  // Log to console in development
  if (process.env.NODE_ENV === 'development') {
    console.error('[Error Monitor]', entry);
  }

  // In production, could send to external service
  // sendToExternalService(entry);

  return entry;
}

/**
 * Log an API error
 */
export function logAPIError(
  endpoint: string,
  method: string,
  error: Error | string,
  options?: {
    statusCode?: number;
    requestBody?: unknown;
    responseBody?: unknown;
    context?: Record<string, unknown>;
  }
): APIErrorLog {
  const errorObj = typeof error === 'string' ? new Error(error) : error;

  const entry: APIErrorLog = {
    id: generateErrorId(),
    timestamp: new Date().toISOString(),
    type: 'error',
    message: errorObj.message,
    stack: errorObj.stack,
    endpoint,
    method,
    statusCode: options?.statusCode,
    requestBody: options?.requestBody,
    responseBody: options?.responseBody,
    context: options?.context,
    url: typeof window !== 'undefined' ? window.location.href : undefined,
    userAgent: typeof navigator !== 'undefined' ? navigator.userAgent : undefined,
  };

  // Store locally
  storeError(entry);

  // Log to console in development
  if (process.env.NODE_ENV === 'development') {
    console.error('[API Error]', entry);
  }

  return entry;
}

/**
 * Log a warning (non-critical issue)
 */
export function logWarning(
  message: string,
  context?: Record<string, unknown>
): ErrorLogEntry {
  const entry: ErrorLogEntry = {
    id: generateErrorId(),
    timestamp: new Date().toISOString(),
    type: 'warning',
    message,
    context,
    url: typeof window !== 'undefined' ? window.location.href : undefined,
  };

  storeError(entry);

  if (process.env.NODE_ENV === 'development') {
    console.warn('[Warning Monitor]', entry);
  }

  return entry;
}

/* ============================================================================
   GLOBAL ERROR HANDLERS
   ============================================================================ */

/**
 * Initialize global error handlers
 * Call this once at app startup
 */
export function initializeErrorMonitoring(): void {
  if (typeof window === 'undefined') return;

  // Catch unhandled errors
  window.onerror = (message, source, lineno, colno, error) => {
    logError(error || String(message), {
      source,
      lineno,
      colno,
      type: 'uncaught',
    });
    return false; // Let default handler also run
  };

  // Catch unhandled promise rejections
  window.onunhandledrejection = (event) => {
    logError(
      event.reason instanceof Error
        ? event.reason
        : String(event.reason || 'Unhandled Promise Rejection'),
      { type: 'unhandledRejection' }
    );
  };

  // Log console errors (optional - can be noisy)
  const originalConsoleError = console.error;
  console.error = (...args) => {
    // Don't log our own error monitor logs
    if (args[0]?.includes?.('[Error Monitor]') || args[0]?.includes?.('[API Error]')) {
      originalConsoleError.apply(console, args);
      return;
    }

    const message = args.map((arg) =>
      typeof arg === 'object' ? JSON.stringify(arg) : String(arg)
    ).join(' ');

    logError(message, { type: 'console.error' });
    originalConsoleError.apply(console, args);
  };

  console.log('[Error Monitor] Initialized');
}

/* ============================================================================
   UTILITY FUNCTIONS
   ============================================================================ */

/**
 * Get all stored errors
 */
export function getErrorLog(): ErrorLogEntry[] {
  return getStoredErrors();
}

/**
 * Clear stored errors
 */
export function clearErrorLog(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(ERROR_STORAGE_KEY);
}

/**
 * Get error summary
 */
export function getErrorSummary(): {
  total: number;
  errors: number;
  warnings: number;
  lastError?: ErrorLogEntry;
} {
  const errors = getStoredErrors();
  return {
    total: errors.length,
    errors: errors.filter((e) => e.type === 'error').length,
    warnings: errors.filter((e) => e.type === 'warning').length,
    lastError: errors[0],
  };
}

/* ============================================================================
   EXPORT
   ============================================================================ */

const errorMonitoring = {
  logError,
  logAPIError,
  logWarning,
  initializeErrorMonitoring,
  getErrorLog,
  clearErrorLog,
  getErrorSummary,
};

export default errorMonitoring;
