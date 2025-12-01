'use client';

/**
 * BookmarkSidebar — PROMPT 4: Sidebar Bookmark System
 * 
 * Displays user's bookmarked tasks grouped by module.
 * Features:
 * - Collapsible module groups
 * - Quick navigation to tasks
 * - Clear all button
 * - Empty state
 * - Loading skeleton
 */

import { useState } from 'react';
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
} from 'lucide-react';

interface BookmarkSidebarProps {
  className?: string;
  collapsed?: boolean;
}

export function BookmarkSidebar({ className, collapsed = false }: BookmarkSidebarProps) {
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

  // Collapsed state - just show icon with count
  if (collapsed) {
    return (
      <div className={cn('flex flex-col items-center py-4', className)}>
        <button
          className="relative p-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
          title={`${count} bookmarked tasks`}
        >
          <Star className="w-5 h-5 text-amber-500 fill-amber-400" />
          {count > 0 && (
            <span className="absolute -top-1 -right-1 w-4 h-4 text-[10px] font-bold bg-amber-500 text-white rounded-full flex items-center justify-center">
              {count > 9 ? '9+' : count}
            </span>
          )}
        </button>
      </div>
    );
  }

  // Loading state
  if (loading) {
    return (
      <div className={cn('p-4', className)}>
        <div className="flex items-center gap-2 mb-4">
          <Star className="w-4 h-4 text-amber-500" />
          <span className="text-sm font-medium text-neutral-700 dark:text-neutral-300">
            Bookmarks
          </span>
        </div>
        <div className="space-y-3">
          {[1, 2, 3].map(i => (
            <div key={i} className="animate-pulse">
              <div className="h-4 bg-neutral-200 dark:bg-neutral-700 rounded w-3/4 mb-2" />
              <div className="h-3 bg-neutral-100 dark:bg-neutral-800 rounded w-1/2" />
            </div>
          ))}
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div className={cn('p-4', className)}>
        <div className="text-sm text-red-500 dark:text-red-400">
          Failed to load bookmarks
          <button
            onClick={refresh}
            className="ml-2 text-blue-500 hover:underline"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  const moduleGroups = Object.values(groupedByModule);

  return (
    <div className={cn('flex flex-col', className)}>
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-neutral-100 dark:border-neutral-800">
        <div className="flex items-center gap-2">
          <Star className="w-4 h-4 text-amber-500 fill-amber-400" />
          <span className="text-sm font-semibold text-neutral-800 dark:text-neutral-200">
            Bookmarks
          </span>
          {count > 0 && (
            <span className="px-1.5 py-0.5 text-[10px] font-bold bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-300 rounded-full">
              {count}
            </span>
          )}
        </div>
        
        {count > 0 && (
          <button
            onClick={handleClearAll}
            disabled={clearing}
            className="p-1.5 rounded-md text-neutral-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 transition-colors"
            title="Clear all bookmarks"
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
      <div className="flex-1 overflow-y-auto">
        {count === 0 ? (
          // Empty state
          <div className="flex flex-col items-center justify-center py-8 px-4 text-center">
            <BookmarkX className="w-10 h-10 text-neutral-300 dark:text-neutral-600 mb-3" />
            <p className="text-sm font-medium text-neutral-500 dark:text-neutral-400">
              No bookmarks yet
            </p>
            <p className="text-xs text-neutral-400 dark:text-neutral-500 mt-1">
              Star tasks to save them here for quick access
            </p>
          </div>
        ) : (
          // Bookmarks grouped by module
          <div className="py-2">
            {moduleGroups.map(group => {
              const isExpanded = expandedModules.has(group.module_slug);
              
              return (
                <div key={group.module_slug} className="mb-1">
                  {/* Module Header */}
                  <button
                    onClick={() => toggleModule(group.module_slug)}
                    className={cn(
                      'w-full flex items-center gap-2 px-4 py-2',
                      'text-left text-sm font-medium',
                      'text-neutral-700 dark:text-neutral-300',
                      'hover:bg-neutral-50 dark:hover:bg-neutral-800/50',
                      'transition-colors'
                    )}
                  >
                    {isExpanded ? (
                      <ChevronDown className="w-3.5 h-3.5 text-neutral-400" />
                    ) : (
                      <ChevronRight className="w-3.5 h-3.5 text-neutral-400" />
                    )}
                    <span className="flex-1 truncate">{group.module_name}</span>
                    <span className="text-xs text-neutral-400 dark:text-neutral-500">
                      {group.tasks.length}
                    </span>
                  </button>

                  {/* Tasks */}
                  {isExpanded && (
                    <div className="ml-6 border-l border-neutral-100 dark:border-neutral-800">
                      {group.tasks.map(bookmark => (
                        <Link
                          key={bookmark.id}
                          href={`/modules/${bookmark.module_slug}/${bookmark.task_id}`}
                          className={cn(
                            'group flex items-center gap-2 px-3 py-2',
                            'text-sm text-neutral-600 dark:text-neutral-400',
                            'hover:bg-neutral-50 dark:hover:bg-neutral-800/50',
                            'hover:text-neutral-900 dark:hover:text-neutral-100',
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
    </div>
  );
}

export default BookmarkSidebar;
