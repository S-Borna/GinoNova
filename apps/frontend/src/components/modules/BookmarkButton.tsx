'use client';

/**
 * BookmarkButton — PROMPT 4: Sidebar Bookmark System
 *
 * Star button that toggles bookmark state for a task.
 * Features:
 * - Visual star icon (filled when bookmarked)
 * - Optimistic update with animation
 * - Accessible tooltip
 * - Loading state
 * - CRITICAL: Does NOT affect parent card appearance
 */

import { useState, useCallback } from 'react';
import { cn } from '@/lib/utils';
import { Star, Loader2 } from 'lucide-react';

interface BookmarkButtonProps {
  taskId: string;
  isBookmarked: boolean;
  onToggle: (taskId: string) => Promise<boolean>;
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

const sizeClasses = {
  sm: 'w-4 h-4',
  md: 'w-5 h-5',
  lg: 'w-6 h-6',
};

const buttonSizeClasses = {
  sm: 'p-1.5',
  md: 'p-2',
  lg: 'p-2.5',
};

export function BookmarkButton({
  taskId,
  isBookmarked,
  onToggle,
  size = 'md',
  className,
}: BookmarkButtonProps) {
  const [loading, setLoading] = useState(false);
  const [optimisticState, setOptimisticState] = useState<boolean | null>(null);

  const displayBookmarked = optimisticState !== null ? optimisticState : isBookmarked;

  const handleClick = useCallback(async (e: React.MouseEvent) => {
    // CRITICAL: Stop event from bubbling to card
    e.preventDefault();
    e.stopPropagation();
    e.nativeEvent.stopImmediatePropagation();

    if (loading) return;

    // Optimistic update
    const newState = !displayBookmarked;
    setOptimisticState(newState);
    setLoading(true);

    try {
      const result = await onToggle(taskId);
      // Sync with actual result
      setOptimisticState(result);
    } catch (error) {
      // Revert on error
      setOptimisticState(null);
      console.error('Failed to toggle bookmark:', error);
    } finally {
      setLoading(false);
      // Clear optimistic state after animation
      setTimeout(() => setOptimisticState(null), 300);
    }
  }, [loading, displayBookmarked, onToggle, taskId]);

  // Prevent mousedown from triggering card interactions
  const handleMouseDown = useCallback((e: React.MouseEvent) => {
    e.stopPropagation();
  }, []);

  return (
    <button
      type="button"
      onClick={handleClick}
      onMouseDown={handleMouseDown}
      disabled={loading}
      aria-label={displayBookmarked ? 'Ta bort bokmärke' : 'Lägg till bokmärke'}
      aria-pressed={displayBookmarked}
      title={displayBookmarked ? 'Ta bort från Quick Access' : 'Lägg till i Quick Access'}
      className={cn(
        'relative rounded-lg transition-all duration-200 z-10',
        'hover:bg-amber-500/10 dark:hover:bg-amber-500/20',
        'focus:outline-none focus:ring-2 focus:ring-amber-500/50',
        'active:scale-95',
        buttonSizeClasses[size],
        loading && 'cursor-wait',
        // Gold glow when bookmarked
        displayBookmarked && 'shadow-[0_0_10px_rgba(251,191,36,0.3)]',
        className
      )}
    >
      {loading ? (
        <Loader2
          className={cn(
            sizeClasses[size],
            'animate-spin text-amber-500'
          )}
        />
      ) : (
        <Star
          className={cn(
            sizeClasses[size],
            'transition-all duration-200',
            displayBookmarked
              ? 'fill-amber-400 text-amber-400 scale-110 drop-shadow-[0_0_4px_rgba(251,191,36,0.5)]'
              : 'fill-transparent text-neutral-400 hover:text-amber-400',
            // Pop animation when bookmarking
            optimisticState === true && 'animate-[pop_0.3s_ease-out]'
          )}
        />
      )}

      {/* Pop animation keyframes via inline style */}
      <style jsx>{`
        @keyframes pop {
          0% { transform: scale(1); }
          50% { transform: scale(1.3); }
          100% { transform: scale(1.1); }
        }
      `}</style>
    </button>
  );
}

export default BookmarkButton;
