'use client';

/**
 * ============================================================================
 * RIGHT SIDEBAR — Premium Combined Bookmarks & Task Reminders
 * ============================================================================
 *
 * Premium Polish Phase 2
 *
 * Features:
 * - ⭐ Bookmarks section (existing functionality)
 * - ⏰ Task Reminders section (skipped tasks bubble up)
 * - Premium glow effects and animations
 * - Collapsible sections
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
} from 'lucide-react';

/* ============================================================================
   TYPES
   ============================================================================ */

interface TaskReminder {
    id: string;
    task_id: string;
    task_title: string;
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
    // Empty for now - reminders will come from API when tasks are skipped
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
   BOOKMARKS SECTION
   ============================================================================ */

function BookmarksSection({ collapsed }: { collapsed?: boolean }) {
    const {
        bookmarks,
        groupedByModule,
        loading,
        error,
        clearAll,
        count,
        refresh
    } = useBookmarks();

    const [expandedModules, setExpandedModules] = useState<Set<string>>(new Set());
    const [clearing, setClearing] = useState(false);
    const [sectionExpanded, setSectionExpanded] = useState(true);

    const toggleModule = (moduleSlug: string) => {
        setExpandedModules(prev => {
            const newSet = new Set(prev);
            if (newSet.has(moduleSlug)) {
                newSet.delete(moduleSlug);
            } else {
                newSet.add(moduleSlug);
            }
            return newSet;
        });
    };

    const handleClearAll = async () => {
        if (!confirm('Remove all bookmarks? This cannot be undone.')) return;
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
                        count > 0 && "shadow-[0_0_15px_rgba(245,158,11,0.2)]"
                    )}
                    title={`${count} bookmarked tasks`}
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

    const moduleGroups = Object.values(groupedByModule);

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
                <div className="max-h-64 overflow-y-auto">
                    {loading ? (
                        <div className="p-4 space-y-3">
                            {[1, 2, 3].map(i => (
                                <div key={i} className="animate-pulse">
                                    <div className="h-4 bg-zinc-800 rounded w-3/4 mb-2" />
                                    <div className="h-3 bg-zinc-800/50 rounded w-1/2" />
                                </div>
                            ))}
                        </div>
                    ) : error ? (
                        <div className="p-4 text-sm text-red-400">
                            Failed to load bookmarks
                            <button onClick={refresh} className="ml-2 text-purple-400 hover:underline">
                                Retry
                            </button>
                        </div>
                    ) : count === 0 ? (
                        <div className="flex flex-col items-center justify-center py-6 px-4 text-center">
                            <div className={cn(
                                "w-12 h-12 rounded-xl flex items-center justify-center mb-3",
                                "bg-zinc-800/50 border border-zinc-700/50"
                            )}>
                                <BookmarkX className="w-6 h-6 text-zinc-500" />
                            </div>
                            <p className="text-sm font-medium text-zinc-400">
                                No bookmarks yet
                            </p>
                            <p className="text-xs text-zinc-500 mt-1">
                                Star tasks for quick access
                            </p>
                        </div>
                    ) : (
                        <div className="py-2">
                            {/* Clear All Button */}
                            <div className="px-4 pb-2">
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
                                    Clear all
                                </button>
                            </div>

                            {moduleGroups.map(group => {
                                const isExpanded = expandedModules.has(group.module_slug);

                                return (
                                    <div key={group.module_slug} className="mb-1">
                                        <button
                                            onClick={() => toggleModule(group.module_slug)}
                                            className={cn(
                                                'w-full flex items-center gap-2 px-4 py-2',
                                                'text-left text-sm font-medium',
                                                'text-zinc-300',
                                                'hover:bg-zinc-800/50',
                                                'transition-colors'
                                            )}
                                        >
                                            {isExpanded ? (
                                                <ChevronDown className="w-3.5 h-3.5 text-zinc-500" />
                                            ) : (
                                                <ChevronRight className="w-3.5 h-3.5 text-zinc-500" />
                                            )}
                                            <span className="flex-1 truncate">{group.module_name}</span>
                                            <span className="text-xs text-zinc-500">
                                                {group.tasks.length}
                                            </span>
                                        </button>

                                        {isExpanded && (
                                            <div className="ml-6 border-l border-zinc-800">
                                                {group.tasks.map(bookmark => (
                                                    <Link
                                                        key={bookmark.id}
                                                        href={`/modules/${bookmark.module_slug}/${bookmark.task_id}`}
                                                        className={cn(
                                                            'group flex items-center gap-2 px-3 py-2',
                                                            'text-sm text-zinc-400',
                                                            'hover:bg-zinc-800/50 hover:text-zinc-200',
                                                            'transition-colors'
                                                        )}
                                                    >
                                                        <Star className="w-3 h-3 text-amber-400 fill-amber-400 flex-shrink-0" />
                                                        <span className="flex-1 truncate">{bookmark.task_title}</span>
                                                        <ExternalLink className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                                                    </Link>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

/* ============================================================================
   TASK REMINDERS SECTION
   ============================================================================ */

function TaskRemindersSection({ collapsed }: { collapsed?: boolean }) {
    const [reminders, setReminders] = useState<TaskReminder[]>([]);
    const [loading, setLoading] = useState(true);
    const [sectionExpanded, setSectionExpanded] = useState(true);

    useEffect(() => {
        // Simulate loading
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
                        count > 0 && "shadow-[0_0_15px_rgba(249,115,22,0.2)]"
                    )}
                    title={`${count} task reminders`}
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
                <div className="max-h-64 overflow-y-auto">
                    {loading ? (
                        <div className="p-4 space-y-3">
                            {[1, 2].map(i => (
                                <div key={i} className="animate-pulse">
                                    <div className="h-4 bg-zinc-800 rounded w-3/4 mb-2" />
                                    <div className="h-3 bg-zinc-800/50 rounded w-1/2" />
                                </div>
                            ))}
                        </div>
                    ) : count === 0 ? (
                        <div className="flex flex-col items-center justify-center py-6 px-4 text-center">
                            <div className={cn(
                                "w-12 h-12 rounded-xl flex items-center justify-center mb-3",
                                "bg-emerald-500/10 border border-emerald-500/20"
                            )}>
                                <CheckCircle2 className="w-6 h-6 text-emerald-400" />
                            </div>
                            <p className="text-sm font-medium text-zinc-400">
                                All caught up! 🎉
                            </p>
                            <p className="text-xs text-zinc-500 mt-1">
                                Skipped tasks will appear here
                            </p>
                        </div>
                    ) : (
                        <div className="py-2 space-y-1">
                            {reminders.slice(0, 5).map(reminder => (
                                <Link
                                    key={reminder.id}
                                    href={`/modules/${reminder.module_slug}/${reminder.task_id}`}
                                    className={cn(
                                        "group flex items-start gap-3 px-4 py-3 mx-2 rounded-xl",
                                        "bg-zinc-800/30 border border-zinc-700/30",
                                        "hover:bg-orange-500/10 hover:border-orange-500/20",
                                        "transition-all duration-300"
                                    )}
                                >
                                    <div className={cn(
                                        "w-8 h-8 rounded-lg flex items-center justify-center shrink-0",
                                        "bg-orange-500/20"
                                    )}>
                                        <AlertCircle className="w-4 h-4 text-orange-400" />
                                    </div>
                                    <div className="flex-1 min-w-0">
                                        <p className="text-sm font-medium text-zinc-200 truncate group-hover:text-orange-300">
                                            {reminder.task_title}
                                        </p>
                                        <p className="text-xs text-zinc-500 mt-0.5">
                                            {reminder.module_name} • Skipped {reminder.days_ago}d ago
                                        </p>
                                    </div>
                                    <Bell className="w-4 h-4 text-zinc-600 group-hover:text-orange-400 shrink-0 mt-0.5" />
                                </Link>
                            ))}

                            {count > 5 && (
                                <p className="text-xs text-zinc-500 text-center py-2">
                                    +{count - 5} more reminders
                                </p>
                            )}
                        </div>
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
                💡 Star tasks & complete all to keep this clean
            </div>
        </div>
    );
}

export default RightSidebar;
