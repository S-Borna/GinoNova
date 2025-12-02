'use client';

/**
 * ============================================================================
 * RIGHT SIDEBAR — Premium Quick Access Panel
 * ============================================================================
 *
 * Premium Polish Phase 2 — UPDATED
 *
 * Features:
 * - ⭐ Bookmarks displayed as GOLD-MARKED CARDS with task number & module
 * - ⏰ Task Reminders for skipped tasks
 * - Combined "My Tasks" view (bookmarks + reminders in same card style)
 * - Premium glow effects
 * - Visible in Studyflow too
 *
 * @phase Premium Upgrade Phase 2
 */

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { cn } from '@/lib/utils';
import { useBookmarks } from '@/hooks/useBookmarks';
import {
    Star,
    ChevronDown,
    ChevronRight,
    Trash2,
    ExternalLink,
    Loader2,
    BookmarkX,
    Clock,
    AlertCircle,
    Bell,
    CheckCircle2,
    Sparkles,
    Zap,
    Hash,
} from 'lucide-react';

/* ============================================================================
   TYPES
   ============================================================================ */

interface TaskReminder {
    id: string;
    task_id: string;
    task_title: string;
    task_order?: number;
    module_id: string;
    module_slug: string;
    module_name: string;
    skipped_at: string;
    days_ago: number;
}

interface RightSidebarProps {
    className?: string;
    collapsed?: boolean;
}

/* ============================================================================
   MOCK REMINDERS (Replace with API call later)
   ============================================================================ */

const getMockReminders = (): TaskReminder[] => {
    return [];
};

/* ============================================================================
   SECTION HEADER
   ============================================================================ */

interface SectionHeaderProps {
    icon: React.ReactNode;
    title: string;
    count: number;
    expanded: boolean;
    onToggle: () => void;
    iconColor: string;
    badgeColor: string;
}

function SectionHeader({
    icon,
    title,
    count,
    expanded,
    onToggle,
    iconColor,
    badgeColor,
}: SectionHeaderProps) {
    return (
        <button
            onClick={onToggle}
            className={cn(
                "w-full flex items-center justify-between px-4 py-3",
                "border-b border-zinc-800/60",
                "hover:bg-zinc-800/30 transition-colors",
                "group"
            )}
        >
            <div className="flex items-center gap-2">
                <div className={iconColor}>{icon}</div>
                <span className="text-sm font-semibold text-zinc-200">
                    {title}
                </span>
                {count > 0 && (
                    <span className={cn(
                        "px-1.5 py-0.5 text-[10px] font-bold rounded-full",
                        badgeColor
                    )}>
                        {count}
                    </span>
                )}
            </div>
            <div className="text-zinc-500 group-hover:text-zinc-300 transition-colors">
                {expanded ? (
                    <ChevronDown className="w-4 h-4" />
                ) : (
                    <ChevronRight className="w-4 h-4" />
                )}
            </div>
        </button>
    );
}

/* ============================================================================
   GOLD TASK CARD — Premium Bookmark Card Display
   ============================================================================ */

interface GoldTaskCardProps {
    taskId: string;
    taskTitle: string;
    taskOrder?: number;
    moduleSlug: string;
    moduleName: string;
    type: 'bookmark' | 'reminder';
    daysAgo?: number;
}

function GoldTaskCard({
    taskId,
    taskTitle,
    taskOrder,
    moduleSlug,
    moduleName,
    type,
    daysAgo,
}: GoldTaskCardProps) {
    const isBookmark = type === 'bookmark';

    return (
        <Link
            href={`/modules/${moduleSlug}/tasks/${taskId}`}
            className={cn(
                "group block px-3 py-3 mx-2 mb-2 rounded-xl",
                "transition-all duration-300",
                // Gold styling for bookmarks
                isBookmark && [
                    "bg-gradient-to-br from-amber-500/10 to-amber-600/5",
                    "border border-amber-500/30",
                    "hover:border-amber-400/50",
                    "hover:shadow-[0_0_20px_rgba(251,191,36,0.15)]",
                ],
                // Orange styling for reminders
                !isBookmark && [
                    "bg-gradient-to-br from-orange-500/10 to-orange-600/5",
                    "border border-orange-500/30",
                    "hover:border-orange-400/50",
                    "hover:shadow-[0_0_20px_rgba(249,115,22,0.15)]",
                ]
            )}
        >
            {/* Top row: Task number badge + Star/Bell icon */}
            <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                    {/* Task number with gold styling */}
                    {taskOrder && (
                        <span className={cn(
                            "flex items-center gap-0.5 px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider",
                            isBookmark
                                ? "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                                : "bg-orange-500/20 text-orange-300 border border-orange-500/30"
                        )}>
                            <Hash className="w-2.5 h-2.5" />
                            Task {taskOrder}
                        </span>
                    )}
                </div>

                {/* Icon indicator */}
                {isBookmark ? (
                    <Star className="w-4 h-4 text-amber-400 fill-amber-400 drop-shadow-[0_0_4px_rgba(251,191,36,0.5)]" />
                ) : (
                    <Bell className="w-4 h-4 text-orange-400" />
                )}
            </div>

            {/* Task title - Gold highlighted */}
            <p className={cn(
                "text-sm font-semibold truncate mb-1",
                "group-hover:text-white transition-colors",
                isBookmark ? "text-amber-200" : "text-orange-200"
            )}>
                {taskTitle}
            </p>

            {/* Module name */}
            <p className="text-xs text-zinc-400 truncate flex items-center gap-1">
                <Zap className="w-3 h-3" />
                {moduleName}
                {daysAgo !== undefined && (
                    <span className="ml-auto text-orange-400/70">
                        {daysAgo}d ago
                    </span>
                )}
            </p>

            {/* Hover indicator */}
            <div className={cn(
                "absolute right-3 top-1/2 -translate-y-1/2",
                "opacity-0 group-hover:opacity-100 transition-opacity"
            )}>
                <ExternalLink className="w-4 h-4 text-zinc-400" />
            </div>
        </Link>
    );
}

/* ============================================================================
   BOOKMARKS SECTION — Now with Gold Cards
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
    const [sectionExpanded, setSectionExpanded] = useState(true);

    const handleClearAll = async () => {
        if (!confirm('Ta bort alla bokmärken? Detta kan inte ångras.')) return;
        setClearing(true);
        try {
            await clearAll();
        } finally {
            setClearing(false);
        }
    };

    // Collapsed state
    if (collapsed) {
        return (
            <div className="flex flex-col items-center py-4">
                <button
                    className={cn(
                        "relative p-2 rounded-xl transition-all duration-300",
                        "hover:bg-amber-500/10",
                        count > 0 && "shadow-[0_0_15px_rgba(245,158,11,0.3)]"
                    )}
                    title={`${count} sparade tasks`}
                >
                    <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
                    {count > 0 && (
                        <span className="absolute -top-1 -right-1 w-4 h-4 text-[10px] font-bold bg-amber-500 text-white rounded-full flex items-center justify-center animate-pulse">
                            {count > 9 ? '9+' : count}
                        </span>
                    )}
                </button>
            </div>
        );
    }

    return (
        <div>
            <SectionHeader
                icon={<Star className="w-4 h-4 fill-amber-400" />}
                title="Bookmarks"
                count={count}
                expanded={sectionExpanded}
                onToggle={() => setSectionExpanded(!sectionExpanded)}
                iconColor="text-amber-400"
                badgeColor="bg-amber-500/20 text-amber-300"
            />

            {sectionExpanded && (
                <div className="max-h-80 overflow-y-auto py-2">
                    {loading ? (
                        <div className="p-4 space-y-3">
                            {[1, 2, 3].map(i => (
                                <div key={i} className="animate-pulse mx-2 p-3 rounded-xl bg-zinc-800/30">
                                    <div className="h-4 bg-zinc-700 rounded w-1/3 mb-2" />
                                    <div className="h-5 bg-zinc-700 rounded w-3/4 mb-1" />
                                    <div className="h-3 bg-zinc-800 rounded w-1/2" />
                                </div>
                            ))}
                        </div>
                    ) : error ? (
                        <div className="p-4 text-sm text-red-400">
                            Kunde inte ladda bokmärken
                            <button onClick={refresh} className="ml-2 text-purple-400 hover:underline">
                                Försök igen
                            </button>
                        </div>
                    ) : count === 0 ? (
                        <div className="flex flex-col items-center justify-center py-8 px-4 text-center">
                            <div className={cn(
                                "w-14 h-14 rounded-xl flex items-center justify-center mb-3",
                                "bg-zinc-800/50 border border-zinc-700/50"
                            )}>
                                <BookmarkX className="w-7 h-7 text-zinc-500" />
                            </div>
                            <p className="text-sm font-medium text-zinc-400">
                                Inga bokmärken än
                            </p>
                            <p className="text-xs text-zinc-500 mt-1">
                                Stjärnmarkera tasks för snabb åtkomst
                            </p>
                        </div>
                    ) : (
                        <>
                            {/* Clear All Button */}
                            <div className="px-4 pb-2 flex justify-end">
                                <button
                                    onClick={handleClearAll}
                                    disabled={clearing}
                                    className={cn(
                                        "flex items-center gap-1 text-xs",
                                        "text-zinc-500 hover:text-red-400 transition-colors"
                                    )}
                                >
                                    {clearing ? (
                                        <Loader2 className="w-3 h-3 animate-spin" />
                                    ) : (
                                        <Trash2 className="w-3 h-3" />
                                    )}
                                    Rensa alla
                                </button>
                            </div>

                            {/* Gold Task Cards - flat list for immediate visibility */}
                            {bookmarks.map((bookmark, index) => (
                                <GoldTaskCard
                                    key={bookmark.id}
                                    taskId={bookmark.task_id}
                                    taskTitle={bookmark.task_title}
                                    taskOrder={index + 1} // Will be replaced with actual order when available
                                    moduleSlug={bookmark.module_slug}
                                    moduleName={bookmark.module_name}
                                    type="bookmark"
                                />
                            ))}
                        </>
                    )}
                </div>
            )}
        </div>
    );
}

/* ============================================================================
   TASK REMINDERS SECTION — Now with Orange Cards
   ============================================================================ */

function TaskRemindersSection({ collapsed }: { collapsed?: boolean }) {
    const [reminders, setReminders] = useState<TaskReminder[]>([]);
    const [loading, setLoading] = useState(true);
    const [sectionExpanded, setSectionExpanded] = useState(true);

    useEffect(() => {
        setTimeout(() => {
            setReminders(getMockReminders());
            setLoading(false);
        }, 500);
    }, []);

    const count = reminders.length;

    // Collapsed state
    if (collapsed) {
        return (
            <div className="flex flex-col items-center py-4">
                <button
                    className={cn(
                        "relative p-2 rounded-xl transition-all duration-300",
                        "hover:bg-orange-500/10",
                        count > 0 && "shadow-[0_0_15px_rgba(249,115,22,0.3)]"
                    )}
                    title={`${count} påminnelser`}
                >
                    <Clock className="w-5 h-5 text-orange-400" />
                    {count > 0 && (
                        <span className="absolute -top-1 -right-1 w-4 h-4 text-[10px] font-bold bg-orange-500 text-white rounded-full flex items-center justify-center animate-pulse">
                            {count > 9 ? '9+' : count}
                        </span>
                    )}
                </button>
            </div>
        );
    }

    return (
        <div>
            <SectionHeader
                icon={<Clock className="w-4 h-4" />}
                title="Task Reminders"
                count={count}
                expanded={sectionExpanded}
                onToggle={() => setSectionExpanded(!sectionExpanded)}
                iconColor="text-orange-400"
                badgeColor="bg-orange-500/20 text-orange-300"
            />

            {sectionExpanded && (
                <div className="max-h-64 overflow-y-auto py-2">
                    {loading ? (
                        <div className="p-4 space-y-3">
                            {[1, 2].map(i => (
                                <div key={i} className="animate-pulse mx-2 p-3 rounded-xl bg-zinc-800/30">
                                    <div className="h-4 bg-zinc-700 rounded w-1/3 mb-2" />
                                    <div className="h-5 bg-zinc-700 rounded w-3/4" />
                                </div>
                            ))}
                        </div>
                    ) : count === 0 ? (
                        <div className="flex flex-col items-center justify-center py-8 px-4 text-center">
                            <div className={cn(
                                "w-14 h-14 rounded-xl flex items-center justify-center mb-3",
                                "bg-emerald-500/10 border border-emerald-500/20"
                            )}>
                                <CheckCircle2 className="w-7 h-7 text-emerald-400" />
                            </div>
                            <p className="text-sm font-medium text-zinc-400">
                                Allt klart! 🎉
                            </p>
                            <p className="text-xs text-zinc-500 mt-1">
                                Överhoppade tasks visas här
                            </p>
                        </div>
                    ) : (
                        <>
                            {reminders.slice(0, 5).map(reminder => (
                                <GoldTaskCard
                                    key={reminder.id}
                                    taskId={reminder.task_id}
                                    taskTitle={reminder.task_title}
                                    taskOrder={reminder.task_order}
                                    moduleSlug={reminder.module_slug}
                                    moduleName={reminder.module_name}
                                    type="reminder"
                                    daysAgo={reminder.days_ago}
                                />
                            ))}

                            {count > 5 && (
                                <p className="text-xs text-zinc-500 text-center py-2">
                                    +{count - 5} fler påminnelser
                                </p>
                            )}
                        </>
                    )}
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
            <div className={cn('flex flex-col items-center py-4 gap-4', className)}>
                <BookmarksSection collapsed />
                <div className="w-8 h-px bg-zinc-800" />
                <TaskRemindersSection collapsed />
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
            <div className={cn(
                "flex items-center gap-2 px-4 py-4",
                "border-b border-zinc-800/60"
            )}>
                <Sparkles className="w-4 h-4 text-purple-400" />
                <span className="text-sm font-semibold text-zinc-100">Quick Access</span>
            </div>

            {/* Sections */}
            <div className="flex-1 overflow-y-auto">
                <BookmarksSection />
                <TaskRemindersSection />
            </div>

            {/* Footer tip */}
            <div className={cn(
                "px-4 py-3",
                "border-t border-zinc-800/60",
                "text-xs text-zinc-500 text-center"
            )}>
                💡 Stjärnmarkera tasks & slutför alla för en ren lista
            </div>
        </div>
    );
}

export default RightSidebar;
