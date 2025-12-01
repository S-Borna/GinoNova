'use client';

/**
 * useBookmarks Hook - PROMPT 4: Sidebar Bookmark System
 * 
 * Manages user task bookmarks with API integration.
 * Features:
 * - Fetch all bookmarks
 * - Toggle bookmark on/off
 * - Group by module for sidebar display
 * - Clear all bookmarks
 */

import { useState, useEffect, useCallback, useMemo } from 'react';
import { useAuth } from '@/components/auth';
import { getToken } from '@/lib/auth';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Bookmark {
  id: string;
  user_id: string;
  task_id: string;
  created_at: string;
  task_title: string;
  module_slug: string;
  module_name: string;
}

interface BookmarkGroup {
  module_name: string;
  module_slug: string;
  tasks: Bookmark[];
}

export function useBookmarks() {
  const { user } = useAuth();
  const token = getToken();
  const [bookmarks, setBookmarks] = useState<Bookmark[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch all bookmarks for current user
  const fetchBookmarks = useCallback(async () => {
    if (!token) {
      setBookmarks([]);
      setLoading(false);
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await fetch(`${API_BASE}/api/bookmarks`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch bookmarks');
      }

      const data = await response.json();
      setBookmarks(data.bookmarks || []);
    } catch (err) {
      console.error('Failed to fetch bookmarks:', err);
      setError(err instanceof Error ? err.message : 'Unknown error');
      setBookmarks([]);
    } finally {
      setLoading(false);
    }
  }, [token]);

  // Fetch on mount and when token changes
  useEffect(() => {
    fetchBookmarks();
  }, [fetchBookmarks]);

  // Toggle bookmark (add or remove)
  const toggleBookmark = useCallback(async (taskId: string): Promise<boolean> => {
    if (!token) return false;

    const isCurrentlyBookmarked = bookmarks.some(b => b.task_id === taskId);

    try {
      if (isCurrentlyBookmarked) {
        // Remove bookmark
        const response = await fetch(`${API_BASE}/api/bookmarks/${taskId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to remove bookmark');
        }

        setBookmarks(prev => prev.filter(b => b.task_id !== taskId));
        return false; // Not bookmarked anymore
      } else {
        // Add bookmark
        const response = await fetch(`${API_BASE}/api/bookmarks`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ task_id: taskId }),
        });

        if (!response.ok) {
          throw new Error('Failed to add bookmark');
        }

        const newBookmark = await response.json();
        setBookmarks(prev => [newBookmark, ...prev]);
        return true; // Now bookmarked
      }
    } catch (err) {
      console.error('Failed to toggle bookmark:', err);
      return isCurrentlyBookmarked; // Return current state on error
    }
  }, [token, bookmarks]);

  // Check if a task is bookmarked
  const isBookmarked = useCallback((taskId: string): boolean => {
    return bookmarks.some(b => b.task_id === taskId);
  }, [bookmarks]);

  // Clear all bookmarks
  const clearAll = useCallback(async (): Promise<void> => {
    if (!token) return;

    try {
      const response = await fetch(`${API_BASE}/api/bookmarks`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error('Failed to clear bookmarks');
      }

      setBookmarks([]);
    } catch (err) {
      console.error('Failed to clear bookmarks:', err);
    }
  }, [token]);

  // Group bookmarks by module for sidebar display
  const groupedByModule = useMemo((): Record<string, BookmarkGroup> => {
    return bookmarks.reduce((acc, bookmark) => {
      const key = bookmark.module_slug;
      if (!acc[key]) {
        acc[key] = {
          module_name: bookmark.module_name,
          module_slug: bookmark.module_slug,
          tasks: [],
        };
      }
      acc[key].tasks.push(bookmark);
      return acc;
    }, {} as Record<string, BookmarkGroup>);
  }, [bookmarks]);

  return {
    bookmarks,
    groupedByModule,
    loading,
    error,
    toggleBookmark,
    isBookmarked,
    clearAll,
    refresh: fetchBookmarks,
    count: bookmarks.length,
  };
}

export default useBookmarks;
