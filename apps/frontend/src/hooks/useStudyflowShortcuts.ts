'use client';

import { useEffect, useCallback, useRef } from 'react';

export interface KeyboardShortcut {
  key: string;
  ctrl?: boolean;
  shift?: boolean;
  alt?: boolean;
  meta?: boolean;
  action: () => void;
  description: string;
  enabled?: boolean;
}

interface UseStudyflowShortcutsOptions {
  onPauseResume?: () => void;
  onSkipBreak?: () => void;
  onEndSession?: () => void;
  onToggleSound?: () => void;
  isRunning?: boolean;
  isBreak?: boolean;
  isPaused?: boolean;
  enabled?: boolean;
}

export function useStudyflowShortcuts({
  onPauseResume,
  onSkipBreak,
  onEndSession,
  onToggleSound,
  isRunning = false,
  isBreak = false,
  isPaused = false,
  enabled = true,
}: UseStudyflowShortcutsOptions) {
  const shortcutsRef = useRef<KeyboardShortcut[]>([]);

  // Define shortcuts
  useEffect(() => {
    shortcutsRef.current = [
      {
        key: ' ', // Space
        action: () => onPauseResume?.(),
        description: isPaused ? 'Resume session' : 'Pause session',
        enabled: isRunning || isPaused,
      },
      {
        key: 'Enter',
        action: () => onSkipBreak?.(),
        description: 'Skip break',
        enabled: isBreak,
      },
      {
        key: 'Escape',
        action: () => onEndSession?.(),
        description: 'End session',
        enabled: isRunning || isPaused || isBreak,
      },
      {
        key: 'm',
        action: () => onToggleSound?.(),
        description: 'Toggle sound',
        enabled: true,
      },
    ];
  }, [
    onPauseResume,
    onSkipBreak,
    onEndSession,
    onToggleSound,
    isRunning,
    isBreak,
    isPaused,
  ]);

  // Handle key press
  const handleKeyDown = useCallback(
    (event: KeyboardEvent) => {
      if (!enabled) return;

      // Don't trigger shortcuts when typing in inputs
      const target = event.target as HTMLElement;
      if (
        target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA' ||
        target.isContentEditable
      ) {
        return;
      }

      const shortcut = shortcutsRef.current.find((s) => {
        if (s.key !== event.key) return false;
        if (s.ctrl && !event.ctrlKey) return false;
        if (s.shift && !event.shiftKey) return false;
        if (s.alt && !event.altKey) return false;
        if (s.meta && !event.metaKey) return false;
        return true;
      });

      if (shortcut && shortcut.enabled !== false) {
        event.preventDefault();
        shortcut.action();
      }
    },
    [enabled]
  );

  // Register event listener
  useEffect(() => {
    if (!enabled) return;

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [enabled, handleKeyDown]);

  // Return active shortcuts for display
  const getActiveShortcuts = useCallback(() => {
    return shortcutsRef.current.filter((s) => s.enabled !== false);
  }, []);

  return { getActiveShortcuts };
}

export default useStudyflowShortcuts;
