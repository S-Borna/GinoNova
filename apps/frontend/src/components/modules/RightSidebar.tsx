'use client';

/**
 * ============================================================================
 * RIGHT SIDEBAR — Quick Access Panel
 * ============================================================================
 *
 * SIMPLIFIED:
 * - ⭐ Bookmarks = Stjärnmarkerade tasks visas här
 * - 📚 Bookmarks section = Böcker för sparade tasks
 * - ⏰ Task Reminders = Samma som bookmarks (stjärnmarkerade)
 * - Allt i ETT kort-format med guld-styling
 *
 * @phase Premium Upgrade Phase 2
 */

import { useState } from 'react';
import Link from 'next/link';
import { cn } from '@/lib/utils';
import { useBookmarks } from '@/hooks/useBookmarks';
import {
    Star,
    Trash2,
    Loader2,
    BookOpen,
    Sparkles,
    Zap,
    ChevronRight,
} from 'lucide-react';

/* ============================================================================
   TYPES
   ============================================================================ */

interface RightSidebarProps {
    className?: string;
    collapsed?: boolean;
}

/* ============================================================================
   STARRED TASK ITEM — Gold styled card for bookmarked tasks
   ============================================================================ */

interface StarredTaskItemProps {
    taskId: string;
    taskTitle: string;
    moduleSlug: string;
    moduleName: string;
}

function StarredTaskItem({
    taskId,
    taskTitle,
    moduleSlug,
    moduleName,
}: StarredTaskItemProps) {
    return (
        <Link
            href={`/modules/${moduleSlug}/tasks/${taskId}`}
            className={cn(
                "group flex items-center gap-3 px-3 py-2.5 mx-2 mb-1.5 rounded-xl",
                "bg-gradient-to-r from-amber-500/10 to-transparent",
                "border border-amber-500/20",
                "hover:border-amber-400/40 hover:bg-amber-500/15",
                "transition-all duration-200"
            )}
        >
            {/* Star icon */}
            <Star className="w-4 h-4 text-amber-400 fill-amber-400 shrink-0" />

            {/* Content */}
            <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-zinc-200 truncate group-hover:text-amber-200">
                    {taskTitle}
                </p>
                <p className="text-xs text-zinc-500 truncate">
                    {moduleName}
                </p>
            </div>

            {/* Arrow */}
            <ChevronRight className="w-4 h-4 text-zinc-600 group-hover:text-amber-400 shrink-0 transition-colors" />
        </Link>
    );
}

/* ============================================================================
   BOOKMARKS SECTION — Shows all starred tasks
   ============================================================================ */

function BookmarksSection({ collapsed }: { collapsed?: boolean }) {
    const {
        bookmarks,
        loading,
        error,
        clearAll,
        count,
        refresh
    } = useBookmarks();

    const [clearing, setClearing] = useState(false);

    const handleClearAll = async () => {
        if (!confirm('Ta bort alla sparade tasks?')) return;
        setClearing(true);
        try {
            await clearAll();
        } finally {
            setClearing(false);
        }
    };

    // Collapsed state - just show icon with count
    if (collapsed) {
        return (
            <div className="flex flex-col items-center py-4">
                <div
                    className={cn(
                        "relative p-2 rounded-xl",
                        count > 0 && "bg-amber-500/10"
                    )}
                    title={`${count} sparade tasks`}
                >
                    <Star className={cn(
                        "w-5 h-5",
                        count > 0 ? "text-amber-400 fill-amber-400" : "text-zinc-600"
                    )} />
                    {count > 0 && (
                        <span className="absolute -top-1 -right-1 w-4 h-4 text-[10px] font-bold bg-amber-500 text-white rounded-full flex items-center justify-center">
                            {count > 9 ? '9+' : count}
                        </span>
                    )}
                </div>
            </div>
        );
    }

    return (
        <div className="flex-1 flex flex-col">
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-zinc-800/60">
                <div className="flex items-center gap-2">
                    <BookOpen className="w-4 h-4 text-amber-400" />
                    <span className="text-sm font-semibold text-zinc-200">Bookmarks</span>
                    {count > 0 && (
                        <span className="px-1.5 py-0.5 text-[10px] font-bold rounded-full bg-amber-500/20 text-amber-300">
                            {count}
                        </span>
                    )}
                </div>
                {count > 0 && (
                    <button
                        onClick={handleClearAll}
                        disabled={clearing}
                        className="text-xs text-zinc-500 hover:text-red-400 transition-colors"
                        title="Rensa alla"
                    >
                        {clearing ? (
                            <Loader2 className="w-3.5 h-3.5 animate-spin" />
                        ) : (
                            <Trash2 className="w-3.5 h-3.5" />
                        )}
                    </button>
                )}
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto py-2">
                {loading ? (
                    <div className="px-4 py-8 text-center">
                        <Loader2 className="w-6 h-6 text-zinc-600 animate-spin mx-auto" />
                        <p className="text-xs text-zinc-500 mt-2">Laddar...</p>
                    </div>
                ) : error ? (
                    <div className="px-4 py-4 text-center">
                        <p className="text-sm text-red-400">Kunde inte ladda</p>
                        <button
                            onClick={refresh}
                            className="text-xs text-purple-400 hover:underline mt-1"
                        >
                            Försök igen
                        </button>
                    </div>
                ) : count === 0 ? (
                    <div className="px-4 py-8 text-center">
                        <div className="w-12 h-12 mx-auto mb-3 rounded-xl bg-zinc-800/50 flex items-center justify-center">
                            <Star className="w-6 h-6 text-zinc-600" />
                        </div>
                        <p className="text-sm font-medium text-zinc-400">Inga sparade tasks</p>
                        <p className="text-xs text-zinc-500 mt-1">
                            Klicka på ⭐ för att spara
                        </p>
                    </div>
                ) : (
                    <div>
                        {bookmarks.map(bookmark => (
                            <StarredTaskItem
                                key={bookmark.id}
                                taskId={bookmark.task_id}
                                taskTitle={bookmark.task_title}
                                moduleSlug={bookmark.module_slug}
                                moduleName={bookmark.module_name}
                            />
                        ))}
                    </div>
                )}
            </div>

            {/* Task Reminders hint - same as bookmarks */}
            {count > 0 && (
                <div className="px-4 py-2 border-t border-zinc-800/60">
                    <div className="flex items-center gap-2 text-xs text-zinc-500">
                        <Zap className="w-3 h-3 text-amber-500" />
                        <span>{count} task{count > 1 ? 's' : ''} att återkomma till</span>
                    </div>
                </div>
            )}
        </div>
    );
}

/* ============================================================================
   MAIN RIGHT SIDEBAR
   ============================================================================ */

export function RightSidebar({ className, collapsed = false }: RightSidebarProps) {
    if (collapsed) {
        return (
            <div className={cn('flex flex-col items-center py-4', className)}>
                <BookmarksSection collapsed />
            </div>
        );
    }

    return (
        <div className={cn(
            'flex flex-col h-full',
            'bg-zinc-900/95 backdrop-blur-sm',
            className
        )}>
            {/* Header */}
            <div className="flex items-center gap-2 px-4 py-4 border-b border-zinc-800/60">
                <Sparkles className="w-4 h-4 text-purple-400" />
                <span className="text-sm font-semibold text-zinc-100">Quick Access</span>
            </div>

            {/* Bookmarks (only section now) */}
            <BookmarksSection />
        </div>
    );
}

export default RightSidebar;
