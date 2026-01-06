"use client"

/**
 * ============================================================================
 * SEARCH BAR — Global Search Component
 * ============================================================================
 *
 * Features:
 * - Debounced search (300ms)
 * - Keyboard shortcuts (Cmd/Ctrl + K)
 * - Type-ahead suggestions
 * - Result categorization (modules, tasks, labs)
 * - Keyboard navigation
 *
 * @phase FAS 1.5 - Implement search functionality
 */

import * as React from "react"
import { useState, useEffect, useRef, useCallback } from "react"
import { useRouter } from "next/navigation"
import {
  Search,
  X,
  Loader2,
  BookOpen,
  FileText,
  FlaskConical,
  ArrowRight,
  Command
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface SearchResult {
  type: 'module' | 'task' | 'lab'
  id: string
  title: string
  description?: string
  url: string
  module_slug?: string
}

interface SearchResponse {
  query: string
  results: SearchResult[]
  total: number
  has_more: boolean
}

/* ============================================================================
   HOOKS
   ============================================================================ */

function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value)
    }, delay)

    return () => {
      clearTimeout(handler)
    }
  }, [value, delay])

  return debouncedValue
}

function useSearch(query: string) {
  const [results, setResults] = useState<SearchResult[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [total, setTotal] = useState(0)

  const debouncedQuery = useDebounce(query, 300)

  useEffect(() => {
    if (debouncedQuery.length < 2) {
      setResults([])
      setTotal(0)
      return
    }

    const searchContent = async () => {
      setIsLoading(true)
      setError(null)

      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://api.ginonova.com'
        const res = await fetch(
          `${apiUrl}/api/search?q=${encodeURIComponent(debouncedQuery)}&limit=10`
        )

        if (!res.ok) {
          throw new Error('Search failed')
        }

        const data: SearchResponse = await res.json()
        setResults(data.results)
        setTotal(data.total)
      } catch (e) {
        console.error('Search error:', e)
        setError('Search failed')
        setResults([])
      } finally {
        setIsLoading(false)
      }
    }

    searchContent()
  }, [debouncedQuery])

  return { results, isLoading, error, total }
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function SearchBar({ className = "" }: { className?: string }) {
  const router = useRouter()
  const [query, setQuery] = useState("")
  const [isOpen, setIsOpen] = useState(false)
  const [selectedIndex, setSelectedIndex] = useState(-1)

  const inputRef = useRef<HTMLInputElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)

  const { results, isLoading, total } = useSearch(query)

  // Close on click outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener("mousedown", handleClickOutside)
    return () => document.removeEventListener("mousedown", handleClickOutside)
  }, [])

  // Keyboard shortcuts
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      // Cmd/Ctrl + K to focus
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault()
        inputRef.current?.focus()
        setIsOpen(true)
      }

      // Escape to close
      if (e.key === "Escape") {
        setIsOpen(false)
        inputRef.current?.blur()
      }
    }
    document.addEventListener("keydown", handleKeyDown)
    return () => document.removeEventListener("keydown", handleKeyDown)
  }, [])

  const handleSelect = useCallback((url: string) => {
    router.push(url)
    setQuery("")
    setIsOpen(false)
    inputRef.current?.blur()
  }, [router])

  // Keyboard navigation in results
  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (!isOpen || results.length === 0) return

    switch (e.key) {
      case "ArrowDown":
        e.preventDefault()
        setSelectedIndex(prev =>
          prev < results.length - 1 ? prev + 1 : prev
        )
        break
      case "ArrowUp":
        e.preventDefault()
        setSelectedIndex(prev => prev > 0 ? prev - 1 : -1)
        break
      case "Enter":
        e.preventDefault()
        if (selectedIndex >= 0 && results[selectedIndex]) {
          handleSelect(results[selectedIndex].url)
        }
        break
    }
  }, [isOpen, results, selectedIndex, handleSelect])

  // Reset selection when results change
  useEffect(() => {
    setSelectedIndex(-1)
  }, [results])

  const getIcon = (type: string) => {
    switch (type) {
      case "module":
        return <BookOpen className="w-4 h-4 text-indigo-400" />
      case "task":
        return <FileText className="w-4 h-4 text-green-400" />
      case "lab":
        return <FlaskConical className="w-4 h-4 text-orange-400" />
      default:
        return <FileText className="w-4 h-4 text-gray-400" />
    }
  }

  const getTypeBadgeColor = (type: string) => {
    switch (type) {
      case "module":
        return "bg-indigo-500/10 text-indigo-400"
      case "task":
        return "bg-green-500/10 text-green-400"
      case "lab":
        return "bg-orange-500/10 text-orange-400"
      default:
        return "bg-gray-500/10 text-gray-400"
    }
  }

  return (
    <div ref={containerRef} className={`relative w-full max-w-md ${className}`}>
      {/* Input */}
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />

        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value)
            setIsOpen(true)
          }}
          onFocus={() => setIsOpen(true)}
          onKeyDown={handleKeyDown}
          placeholder="Search modules, tasks..."
          className="w-full pl-10 pr-20 py-2.5 bg-gray-800/50 border border-gray-700 rounded-xl text-sm text-white placeholder:text-gray-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors"
        />

        {/* Right side: Loading, Clear, or Shortcut */}
        <div className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-2">
          {isLoading ? (
            <Loader2 className="w-4 h-4 text-gray-500 animate-spin" />
          ) : query ? (
            <button
              onClick={() => {
                setQuery("")
                setIsOpen(false)
              }}
              className="p-0.5 rounded hover:bg-gray-700 transition-colors"
            >
              <X className="w-4 h-4 text-gray-500 hover:text-white" />
            </button>
          ) : (
            <div className="flex items-center gap-0.5 px-1.5 py-0.5 rounded bg-gray-700/50 text-gray-500">
              <Command className="w-3 h-3" />
              <span className="text-xs">K</span>
            </div>
          )}
        </div>
      </div>

      {/* Results Dropdown */}
      {isOpen && query.length >= 2 && (
        <div className="absolute top-full left-0 right-0 mt-2 bg-gray-900 border border-gray-700 rounded-xl shadow-2xl overflow-hidden z-50">
          {results.length > 0 ? (
            <>
              <ul className="max-h-[400px] overflow-y-auto">
                {results.map((result, index) => (
                  <li key={`${result.type}-${result.id}`}>
                    <button
                      onClick={() => handleSelect(result.url)}
                      onMouseEnter={() => setSelectedIndex(index)}
                      className={`w-full flex items-center gap-3 px-4 py-3 text-left transition-colors ${selectedIndex === index
                          ? "bg-indigo-500/10 border-l-2 border-indigo-500"
                          : "hover:bg-gray-800/50 border-l-2 border-transparent"
                        }`}
                    >
                      {/* Icon */}
                      <div className="flex-shrink-0">
                        {getIcon(result.type)}
                      </div>

                      {/* Content */}
                      <div className="flex-1 min-w-0">
                        <div className="text-sm font-medium text-white truncate">
                          {result.title}
                        </div>
                        {result.description && (
                          <div className="text-xs text-gray-500 truncate mt-0.5">
                            {result.description}
                          </div>
                        )}
                      </div>

                      {/* Type Badge */}
                      <span className={`flex-shrink-0 px-2 py-0.5 rounded text-xs capitalize ${getTypeBadgeColor(result.type)}`}>
                        {result.type}
                      </span>

                      {/* Arrow */}
                      {selectedIndex === index && (
                        <ArrowRight className="w-4 h-4 text-indigo-400 flex-shrink-0" />
                      )}
                    </button>
                  </li>
                ))}
              </ul>

              {/* Footer */}
              {total > results.length && (
                <div className="px-4 py-2 bg-gray-800/50 border-t border-gray-800 text-center">
                  <span className="text-xs text-gray-500">
                    Showing {results.length} of {total} results
                  </span>
                </div>
              )}
            </>
          ) : !isLoading ? (
            <div className="px-4 py-8 text-center">
              <Search className="w-8 h-8 mx-auto text-gray-600 mb-2" />
              <p className="text-gray-500">No results for &ldquo;{query}&rdquo;</p>
              <p className="text-xs text-gray-600 mt-1">
                Try searching for module names or topics
              </p>
            </div>
          ) : null}
        </div>
      )}
    </div>
  )
}

export default SearchBar
