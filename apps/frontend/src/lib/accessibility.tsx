/**
 * ============================================================================
 * ACCESSIBILITY UTILITIES
 * ============================================================================
 *
 * Utility components and hooks for accessibility.
 *
 * Features:
 * - Skip to content link
 * - Focus trap
 * - Screen reader only text
 * - Keyboard navigation helpers
 *
 * @phase A.7 - Polish & Animations
 */

'use client';

import { useEffect, useRef, useCallback, ReactNode } from 'react';
import { cn } from '@/lib/utils';

/* ============================================================================
   SKIP TO CONTENT LINK
   ============================================================================ */

export function SkipToContent({
  contentId = 'main-content',
  children = 'Skip to content',
}: {
  contentId?: string;
  children?: ReactNode;
}) {
  return (
    <a
      href={`#${contentId}`}
      className={cn(
        'sr-only focus:not-sr-only',
        'focus:fixed focus:top-4 focus:left-4 focus:z-[100]',
        'focus:px-4 focus:py-2 focus:rounded-md',
        'focus:bg-primary focus:text-primary-foreground',
        'focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2'
      )}
    >
      {children}
    </a>
  );
}

/* ============================================================================
   SCREEN READER ONLY TEXT
   ============================================================================ */

export function VisuallyHidden({ children }: { children: ReactNode }) {
  return <span className="sr-only">{children}</span>;
}

/* ============================================================================
   LIVE REGION (For dynamic announcements)
   ============================================================================ */

export function LiveRegion({
  message,
  politeness = 'polite',
}: {
  message: string;
  politeness?: 'polite' | 'assertive';
}) {
  return (
    <div
      role="status"
      aria-live={politeness}
      aria-atomic="true"
      className="sr-only"
    >
      {message}
    </div>
  );
}

/* ============================================================================
   FOCUS TRAP HOOK
   ============================================================================ */

export function useFocusTrap(isActive: boolean) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isActive || !containerRef.current) return;

    const container = containerRef.current;
    const focusableElements = container.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0] as HTMLElement;
    const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstElement) {
          e.preventDefault();
          lastElement?.focus();
        }
      } else {
        if (document.activeElement === lastElement) {
          e.preventDefault();
          firstElement?.focus();
        }
      }
    };

    // Focus first element when trap activates
    firstElement?.focus();

    container.addEventListener('keydown', handleKeyDown);
    return () => container.removeEventListener('keydown', handleKeyDown);
  }, [isActive]);

  return containerRef;
}

/* ============================================================================
   KEYBOARD NAVIGATION HOOK
   ============================================================================ */

export function useKeyboardNavigation<T extends HTMLElement>(
  itemCount: number,
  options?: {
    orientation?: 'horizontal' | 'vertical' | 'both';
    loop?: boolean;
    onSelect?: (index: number) => void;
  }
) {
  const { orientation = 'vertical', loop = true, onSelect } = options || {};
  const currentIndex = useRef(0);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent<T>) => {
      const isVertical = orientation === 'vertical' || orientation === 'both';
      const isHorizontal = orientation === 'horizontal' || orientation === 'both';

      let newIndex = currentIndex.current;
      let handled = false;

      if ((e.key === 'ArrowDown' && isVertical) || (e.key === 'ArrowRight' && isHorizontal)) {
        newIndex = currentIndex.current + 1;
        handled = true;
      } else if ((e.key === 'ArrowUp' && isVertical) || (e.key === 'ArrowLeft' && isHorizontal)) {
        newIndex = currentIndex.current - 1;
        handled = true;
      } else if (e.key === 'Home') {
        newIndex = 0;
        handled = true;
      } else if (e.key === 'End') {
        newIndex = itemCount - 1;
        handled = true;
      } else if (e.key === 'Enter' || e.key === ' ') {
        onSelect?.(currentIndex.current);
        e.preventDefault();
        return;
      }

      if (handled) {
        e.preventDefault();
        
        if (loop) {
          newIndex = ((newIndex % itemCount) + itemCount) % itemCount;
        } else {
          newIndex = Math.max(0, Math.min(itemCount - 1, newIndex));
        }

        currentIndex.current = newIndex;
      }
    },
    [itemCount, orientation, loop, onSelect]
  );

  const setIndex = useCallback((index: number) => {
    currentIndex.current = index;
  }, []);

  return { handleKeyDown, setIndex, currentIndexRef: currentIndex };
}

/* ============================================================================
   FOCUS RING COMPONENT
   ============================================================================ */

export function FocusRing({
  children,
  className,
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={cn(
        'focus-within:ring-2 focus-within:ring-primary focus-within:ring-offset-2',
        'focus-within:ring-offset-background rounded-md',
        className
      )}
    >
      {children}
    </div>
  );
}

/* ============================================================================
   REDUCE MOTION HOOK
   ============================================================================ */

export function useReducedMotion(): boolean {
  if (typeof window === 'undefined') return false;
  
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/* ============================================================================
   LANDMARK COMPONENT
   ============================================================================ */

export function Landmark({
  as: Component = 'div',
  label,
  children,
  className,
  ...props
}: {
  as?: 'main' | 'nav' | 'aside' | 'section' | 'article' | 'header' | 'footer' | 'div';
  label?: string;
  children: ReactNode;
  className?: string;
  [key: string]: unknown;
}) {
  return (
    <Component
      aria-label={label}
      className={className}
      {...props}
    >
      {children}
    </Component>
  );
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

const accessibilityUtils = {
  SkipToContent,
  VisuallyHidden,
  LiveRegion,
  useFocusTrap,
  useKeyboardNavigation,
  FocusRing,
  useReducedMotion,
  Landmark,
};

export default accessibilityUtils;
