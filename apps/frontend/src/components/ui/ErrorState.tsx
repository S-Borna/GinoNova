'use client';

/**
 * ============================================================================
 * ERROR STATE — API & Network Error Display Components
 * ============================================================================
 *
 * Beautiful error states for various scenarios:
 * - API errors
 * - Network offline
 * - Generic errors
 *
 * @phase A.7 - Polish & Animations
 */

import { motion } from 'framer-motion';
import {
  AlertTriangle,
  RefreshCw,
  WifiOff,
  ServerCrash,
  Bug,
  Home,
  type LucideIcon,
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';
import Link from 'next/link';

/* ============================================================================
   TYPES
   ============================================================================ */

export type ErrorVariant = 'api' | 'network' | 'server' | 'generic' | 'custom';

export interface ErrorStateProps {
  variant?: ErrorVariant;
  title?: string;
  message?: string;
  errorCode?: string | number;
  icon?: LucideIcon;
  onRetry?: () => void;
  showHomeButton?: boolean;
  className?: string;
  compact?: boolean;
}

/* ============================================================================
   PRESET CONFIGURATIONS
   ============================================================================ */

const presets: Record<
  Exclude<ErrorVariant, 'custom'>,
  {
    icon: LucideIcon;
    title: string;
    message: string;
    color: string;
  }
> = {
  api: {
    icon: AlertTriangle,
    title: 'Something went wrong',
    message: 'We couldn\'t complete your request. Please try again.',
    color: 'text-yellow-500',
  },
  network: {
    icon: WifiOff,
    title: 'No internet connection',
    message: 'Please check your connection and try again.',
    color: 'text-red-500',
  },
  server: {
    icon: ServerCrash,
    title: 'Server error',
    message: 'Our servers are having issues. Please try again later.',
    color: 'text-orange-500',
  },
  generic: {
    icon: Bug,
    title: 'Oops! An error occurred',
    message: 'Something unexpected happened. Please try again.',
    color: 'text-red-500',
  },
};

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function ErrorState({
  variant = 'generic',
  title,
  message,
  errorCode,
  icon,
  onRetry,
  showHomeButton = false,
  className,
  compact = false,
}: ErrorStateProps) {
  const preset = variant !== 'custom' ? presets[variant] : null;
  const Icon = icon || preset?.icon || AlertTriangle;
  const displayTitle = title || preset?.title || 'Error';
  const displayMessage = message || preset?.message || 'An error occurred.';
  const iconColor = preset?.color || 'text-red-500';

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className={cn(
        'flex flex-col items-center justify-center text-center',
        compact ? 'py-8 px-4' : 'py-16 px-6',
        className
      )}
    >
      {/* Animated Icon */}
      <motion.div
        initial={{ scale: 0.8 }}
        animate={{ scale: 1 }}
        transition={{
          type: 'spring',
          stiffness: 200,
          damping: 15,
          delay: 0.1,
        }}
        className={cn(
          'relative mb-6 flex items-center justify-center',
          compact ? 'w-16 h-16' : 'w-24 h-24'
        )}
      >
        {/* Background pulse */}
        <motion.div
          className={cn(
            'absolute inset-0 rounded-full bg-red-500/10',
          )}
          animate={{
            scale: [1, 1.2, 1],
            opacity: [0.5, 0.2, 0.5],
          }}
          transition={{
            duration: 2,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
        />
        {/* Icon circle */}
        <div
          className={cn(
            'relative flex items-center justify-center rounded-full',
            'bg-gradient-to-br from-muted to-muted/50',
            'border border-border/50',
            compact ? 'w-14 h-14' : 'w-20 h-20'
          )}
        >
          <Icon
            className={cn(
              iconColor,
              compact ? 'w-6 h-6' : 'w-10 h-10'
            )}
          />
        </div>
      </motion.div>

      {/* Error Code Badge */}
      {errorCode && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.15 }}
          className="mb-3"
        >
          <span className="px-2 py-1 text-xs font-mono rounded bg-muted text-muted-foreground">
            Error {errorCode}
          </span>
        </motion.div>
      )}

      {/* Title */}
      <motion.h3
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className={cn(
          'font-semibold text-foreground mb-2',
          compact ? 'text-base' : 'text-lg'
        )}
      >
        {displayTitle}
      </motion.h3>

      {/* Message */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className={cn(
          'text-muted-foreground max-w-sm',
          compact ? 'text-sm' : 'text-base'
        )}
      >
        {displayMessage}
      </motion.p>

      {/* Actions */}
      {(onRetry || showHomeButton) && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="flex items-center gap-3 mt-6"
        >
          {onRetry && (
            <Button onClick={onRetry} size={compact ? 'sm' : 'default'}>
              <RefreshCw className="mr-2 h-4 w-4" />
              Try Again
            </Button>
          )}
          {showHomeButton && (
            <Button
              asChild
              variant="outline"
              size={compact ? 'sm' : 'default'}
            >
              <Link prefetch={false} href="/">
                <Home className="mr-2 h-4 w-4" />
                Go Home
              </Link>
            </Button>
          )}
        </motion.div>
      )}
    </motion.div>
  );
}

/* ============================================================================
   INLINE ERROR MESSAGE
   ============================================================================ */

export function InlineError({
  message,
  onRetry,
  className,
}: {
  message: string;
  onRetry?: () => void;
  className?: string;
}) {
  return (
    <div
      className={cn(
        'flex items-center gap-2 p-3 rounded-lg',
        'bg-red-500/10 border border-red-500/20',
        className
      )}
    >
      <AlertTriangle className="h-4 w-4 text-red-500 shrink-0" />
      <span className="text-sm text-red-600 dark:text-red-400 flex-1">
        {message}
      </span>
      {onRetry && (
        <Button
          variant="ghost"
          size="sm"
          onClick={onRetry}
          className="h-6 px-2 text-xs"
        >
          Retry
        </Button>
      )}
    </div>
  );
}

/* ============================================================================
   NETWORK OFFLINE BANNER
   ============================================================================ */

export function OfflineBanner({ onRetry }: { onRetry?: () => void }) {
  return (
    <motion.div
      initial={{ y: -50, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      exit={{ y: -50, opacity: 0 }}
      className="fixed top-0 left-0 right-0 z-50 px-4 py-2 bg-yellow-500 text-yellow-950"
    >
      <div className="flex items-center justify-center gap-2 text-sm font-medium">
        <WifiOff className="h-4 w-4" />
        <span>You&apos;re offline. Some features may not work.</span>
        {onRetry && (
          <Button
            variant="ghost"
            size="sm"
            onClick={onRetry}
            className="h-6 px-2 text-xs text-yellow-950 hover:bg-yellow-400"
          >
            Retry
          </Button>
        )}
      </div>
    </motion.div>
  );
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default ErrorState;
