'use client';

/**
 * ============================================================================
 * EMPTY STATE — Beautiful Empty State Components
 * ============================================================================
 *
 * Displays attractive empty states for various scenarios:
 * - No tasks completed
 * - No sessions today
 * - Module not started
 * - No data available
 *
 * @phase A.7 - Polish & Animations
 */

import { motion } from 'framer-motion';
import {
  Inbox,
  Clock,
  BookOpen,
  Target,
  Zap,
  Coffee,
  Search,
  FileQuestion,
  type LucideIcon,
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

/* ============================================================================
   TYPES
   ============================================================================ */

export type EmptyStateVariant =
  | 'no-tasks'
  | 'no-sessions'
  | 'not-started'
  | 'no-data'
  | 'no-results'
  | 'coming-soon'
  | 'custom';

export interface EmptyStateProps {
  variant?: EmptyStateVariant;
  title?: string;
  description?: string;
  icon?: LucideIcon;
  actionLabel?: string;
  onAction?: () => void;
  secondaryActionLabel?: string;
  onSecondaryAction?: () => void;
  className?: string;
  compact?: boolean;
}

/* ============================================================================
   PRESET CONFIGURATIONS
   ============================================================================ */

const presets: Record<
  Exclude<EmptyStateVariant, 'custom'>,
  {
    icon: LucideIcon;
    title: string;
    description: string;
    actionLabel?: string;
  }
> = {
  'no-tasks': {
    icon: Target,
    title: 'No tasks completed yet',
    description: 'Start learning to complete your first task and earn XP!',
    actionLabel: 'Start Learning',
  },
  'no-sessions': {
    icon: Clock,
    title: 'No study sessions today',
    description: 'Start a Studyflow session to track your focus time.',
    actionLabel: 'Start Session',
  },
  'not-started': {
    icon: BookOpen,
    title: 'Module not started',
    description: 'Begin this module to unlock the content and start learning.',
    actionLabel: 'Start Module',
  },
  'no-data': {
    icon: Inbox,
    title: 'No data available',
    description: 'There is nothing to display here yet.',
  },
  'no-results': {
    icon: Search,
    title: 'No results found',
    description: 'Try adjusting your search or filters.',
    actionLabel: 'Clear Filters',
  },
  'coming-soon': {
    icon: Zap,
    title: 'Coming Soon',
    description: "We're working on this feature. Stay tuned!",
  },
};

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function EmptyState({
  variant = 'no-data',
  title,
  description,
  icon,
  actionLabel,
  onAction,
  secondaryActionLabel,
  onSecondaryAction,
  className,
  compact = false,
}: EmptyStateProps) {
  // Get preset config or use custom
  const preset = variant !== 'custom' ? presets[variant] : null;
  const Icon = icon || preset?.icon || FileQuestion;
  const displayTitle = title || preset?.title || 'No data';
  const displayDescription = description || preset?.description || '';
  const displayActionLabel = actionLabel || preset?.actionLabel;

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: [0.25, 0.46, 0.45, 0.94] }}
      className={cn(
        'flex flex-col items-center justify-center text-center',
        compact ? 'py-8 px-4' : 'py-16 px-6',
        className
      )}
    >
      {/* Animated Icon Container */}
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
        {/* Background glow */}
        <div
          className={cn(
            'absolute inset-0 rounded-full',
            'bg-gradient-to-br from-primary/20 to-primary/5',
            'blur-xl'
          )}
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
              'text-muted-foreground',
              compact ? 'w-6 h-6' : 'w-10 h-10'
            )}
          />
        </div>
      </motion.div>

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

      {/* Description */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className={cn(
          'text-muted-foreground max-w-sm',
          compact ? 'text-sm' : 'text-base'
        )}
      >
        {displayDescription}
      </motion.p>

      {/* Actions */}
      {(displayActionLabel || secondaryActionLabel) && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="flex items-center gap-3 mt-6"
        >
          {displayActionLabel && onAction && (
            <Button onClick={onAction} size={compact ? 'sm' : 'default'}>
              {displayActionLabel}
            </Button>
          )}
          {secondaryActionLabel && onSecondaryAction && (
            <Button
              onClick={onSecondaryAction}
              variant="outline"
              size={compact ? 'sm' : 'default'}
            >
              {secondaryActionLabel}
            </Button>
          )}
        </motion.div>
      )}
    </motion.div>
  );
}

/* ============================================================================
   SPECIALIZED EMPTY STATES
   ============================================================================ */

export function EmptyTaskList({ onStartLearning }: { onStartLearning?: () => void }) {
  return (
    <EmptyState
      variant="no-tasks"
      onAction={onStartLearning}
      className="min-h-[200px]"
    />
  );
}

export function EmptySessionHistory({ onStartSession }: { onStartSession?: () => void }) {
  return (
    <EmptyState
      variant="no-sessions"
      onAction={onStartSession}
      className="min-h-[200px]"
    />
  );
}

export function ModuleNotStarted({ onStartModule }: { onStartModule?: () => void }) {
  return (
    <EmptyState
      variant="not-started"
      onAction={onStartModule}
      className="min-h-[300px]"
    />
  );
}

export function NoSearchResults({ onClear }: { onClear?: () => void }) {
  return (
    <EmptyState
      variant="no-results"
      onAction={onClear}
      compact
    />
  );
}

export function ComingSoon({ feature }: { feature?: string }) {
  return (
    <EmptyState
      variant="coming-soon"
      title={feature ? `${feature} Coming Soon` : 'Coming Soon'}
      className="min-h-[200px]"
    />
  );
}

/* ============================================================================
   COFFEE BREAK EMPTY STATE
   ============================================================================ */

export function CoffeeBreakState() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex flex-col items-center justify-center py-12 px-6 text-center"
    >
      <motion.div
        animate={{
          y: [0, -5, 0],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
        className="mb-6"
      >
        <div className="relative">
          <Coffee className="w-16 h-16 text-amber-500" />
          {/* Steam effect */}
          <motion.div
            className="absolute -top-2 left-1/2 w-1 h-4 bg-gradient-to-t from-amber-300/50 to-transparent rounded-full"
            animate={{
              opacity: [0.3, 0.7, 0.3],
              y: [0, -4, 0],
            }}
            transition={{
              duration: 1.5,
              repeat: Infinity,
            }}
          />
          <motion.div
            className="absolute -top-1 left-1/2 translate-x-2 w-1 h-3 bg-gradient-to-t from-amber-300/30 to-transparent rounded-full"
            animate={{
              opacity: [0.2, 0.5, 0.2],
              y: [0, -3, 0],
            }}
            transition={{
              duration: 1.8,
              repeat: Infinity,
              delay: 0.3,
            }}
          />
        </div>
      </motion.div>
      <h3 className="text-lg font-semibold text-foreground mb-2">
        Take a break!
      </h3>
      <p className="text-muted-foreground text-sm max-w-xs">
        All caught up! Enjoy some rest before your next learning session.
      </p>
    </motion.div>
  );
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default EmptyState;
