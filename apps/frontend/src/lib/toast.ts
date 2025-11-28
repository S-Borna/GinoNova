/**
 * ============================================================================
 * TOAST UTILITIES — Notification Helper Functions
 * ============================================================================
 *
 * Wrapper around sonner toast for consistent notifications.
 *
 * Usage:
 * import { showToast } from '@/lib/toast';
 * showToast.success('Task completed!');
 * showToast.error('Something went wrong');
 *
 * @phase A.7 - Polish & Animations
 */

import { toast } from 'sonner';

/* ============================================================================
   TYPES
   ============================================================================ */

interface ToastOptions {
  description?: string;
  duration?: number;
  action?: {
    label: string;
    onClick: () => void;
  };
}

/* ============================================================================
   TOAST FUNCTIONS
   ============================================================================ */

export const showToast = {
  /**
   * Success notification
   */
  success: (message: string, options?: ToastOptions) => {
    toast.success(message, {
      description: options?.description,
      duration: options?.duration ?? 4000,
      action: options?.action,
    });
  },

  /**
   * Error notification
   */
  error: (message: string, options?: ToastOptions) => {
    toast.error(message, {
      description: options?.description,
      duration: options?.duration ?? 5000,
      action: options?.action,
    });
  },

  /**
   * Info notification
   */
  info: (message: string, options?: ToastOptions) => {
    toast.info(message, {
      description: options?.description,
      duration: options?.duration ?? 4000,
      action: options?.action,
    });
  },

  /**
   * Warning notification
   */
  warning: (message: string, options?: ToastOptions) => {
    toast.warning(message, {
      description: options?.description,
      duration: options?.duration ?? 4000,
      action: options?.action,
    });
  },

  /**
   * Loading notification (returns dismiss function)
   */
  loading: (message: string) => {
    return toast.loading(message);
  },

  /**
   * Dismiss a specific toast or all toasts
   */
  dismiss: (toastId?: string | number) => {
    toast.dismiss(toastId);
  },

  /**
   * Promise toast (shows loading, then success/error)
   */
  promise: <T>(
    promise: Promise<T>,
    messages: {
      loading: string;
      success: string | ((data: T) => string);
      error: string | ((error: unknown) => string);
    }
  ) => {
    return toast.promise(promise, messages);
  },

  /**
   * Custom toast with any content
   */
  custom: (message: string, options?: ToastOptions & { icon?: React.ReactNode }) => {
    toast(message, {
      description: options?.description,
      duration: options?.duration ?? 4000,
      action: options?.action,
    });
  },
};

/* ============================================================================
   CONVENIENCE FUNCTIONS
   ============================================================================ */

/**
 * Show success toast for task completion
 */
export function toastTaskComplete(taskTitle?: string, xpEarned?: number) {
  showToast.success(
    'Task completed!',
    {
      description: taskTitle 
        ? `${taskTitle}${xpEarned ? ` • +${xpEarned} XP` : ''}`
        : xpEarned 
          ? `+${xpEarned} XP earned`
          : undefined,
    }
  );
}

/**
 * Show error toast for API failures
 */
export function toastApiError(error?: string) {
  showToast.error(
    'Something went wrong',
    {
      description: error || 'Please try again later.',
      action: {
        label: 'Retry',
        onClick: () => window.location.reload(),
      },
    }
  );
}

/**
 * Show success toast for settings saved
 */
export function toastSettingsSaved() {
  showToast.success('Settings saved');
}

/**
 * Show info toast for copy to clipboard
 */
export function toastCopied(item = 'Content') {
  showToast.info(`${item} copied to clipboard`);
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default showToast;
