'use client';

interface KeyboardShortcutsHelpProps {
  isRunning?: boolean;
  isBreak?: boolean;
  isPaused?: boolean;
}

export function KeyboardShortcutsHelp({
  isRunning,
  isBreak,
  isPaused,
}: KeyboardShortcutsHelpProps) {
  const shortcuts = [
    { key: 'Space', description: isPaused ? 'Resume' : 'Pause', enabled: isRunning || isPaused },
    { key: 'Enter', description: 'Skip break', enabled: isBreak },
    { key: 'Escape', description: 'End session', enabled: isRunning || isPaused || isBreak },
    { key: 'M', description: 'Toggle sound', enabled: true },
  ].filter((s) => s.enabled);

  if (shortcuts.length === 0) return null;

  return (
    <div className="flex flex-wrap items-center justify-center gap-3 text-xs text-muted-foreground">
      {shortcuts.map((shortcut) => (
        <div key={shortcut.key} className="flex items-center gap-1">
          <kbd className="px-1.5 py-0.5 rounded bg-muted font-mono text-[10px]">
            {shortcut.key}
          </kbd>
          <span>{shortcut.description}</span>
        </div>
      ))}
    </div>
  );
}

export default KeyboardShortcutsHelp;
