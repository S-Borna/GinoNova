"use client"

/**
 * ============================================================================
 * TASK DETAIL PAGE — Enhanced Task View
 * ============================================================================
 * 
 * Features:
 * - Rich content rendering (text, code, terminal, quiz, checkpoint)
 * - Shell toggle for code blocks
 * - Progress tracking
 * - Previous/Next navigation
 * - XP and completion status
 * 
 * @phase FAS 2.2 - Improved task content rendering
 * @location apps/frontend/src/app/(app)/modules/[id]/tasks/[taskId]/page.tsx
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import { 
  ArrowLeft, 
  ArrowRight, 
  CheckCircle2, 
  Clock, 
  Zap,
  BookOpen,
  AlertCircle,
  Loader2
} from "lucide-react"
import { ContentBlockRenderer } from "@/components/learning/ContentBlockRenderer"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ContentBlock {
  type: string
  [key: string]: any
}

interface Task {
  id: string
  module_id: string
  title: string
  description?: string
  type: 'lesson' | 'exercise' | 'quiz'
  order_index: number
  xp_reward: number
  estimated_minutes?: number
  content?: string
  content_blocks?: ContentBlock[]
  is_completed?: boolean
}

interface Module {
  id: string
  name: string
  slug: string
  tasks: Task[]
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export default function TaskDetailPage() {
  const params = useParams()
  const router = useRouter()
  
  const [task, setTask] = useState<Task | null>(null)
  const [module, setModule] = useState<Module | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [isCompleting, setIsCompleting] = useState(false)
  const [completedBlocks, setCompletedBlocks] = useState<number[]>([])

  // Fetch task and module data
  useEffect(() => {
    async function fetchData() {
      if (!params.id || !params.taskId) return
      
      setIsLoading(true)
      setError(null)
      
      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
        
        // Fetch task
        const taskRes = await fetch(`${apiUrl}/api/tasks/${params.taskId}`)
        if (!taskRes.ok) throw new Error('Task not found')
        const taskData = await taskRes.json()
        setTask(taskData)
        
        // Fetch module for navigation
        const moduleRes = await fetch(`${apiUrl}/api/modules/${params.id}`)
        if (moduleRes.ok) {
          const moduleData = await moduleRes.json()
          setModule(moduleData)
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load task')
      } finally {
        setIsLoading(false)
      }
    }

    fetchData()
  }, [params.id, params.taskId])

  // Get previous and next tasks
  const getNavigation = () => {
    if (!module || !task) return { prev: null, next: null }
    
    const tasks = module.tasks.sort((a, b) => a.order_index - b.order_index)
    const currentIndex = tasks.findIndex(t => t.id === task.id)
    
    return {
      prev: currentIndex > 0 ? tasks[currentIndex - 1] : null,
      next: currentIndex < tasks.length - 1 ? tasks[currentIndex + 1] : null
    }
  }

  const { prev, next } = getNavigation()

  // Handle task completion
  const handleComplete = async () => {
    if (!task) return
    
    setIsCompleting(true)
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
      const token = localStorage.getItem('token')
      
      await fetch(`${apiUrl}/api/progress/tasks/${task.id}/complete`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      })
      
      setTask(prev => prev ? { ...prev, is_completed: true } : null)
      
      // Navigate to next task
      if (next) {
        router.push(`/modules/${module?.slug}/tasks/${next.id}`)
      }
    } catch (err) {
      console.error('Failed to complete task:', err)
    } finally {
      setIsCompleting(false)
    }
  }

  // Handle block completion
  const handleBlockComplete = (blockIndex: number) => {
    setCompletedBlocks(prev => [...prev, blockIndex])
  }

  // Loading state
  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <Loader2 className="w-8 h-8 text-indigo-500 animate-spin" />
      </div>
    )
  }

  // Error state
  if (error || !task) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen gap-4">
        <AlertCircle className="w-12 h-12 text-red-400" />
        <p className="text-gray-400">{error || 'Task not found'}</p>
        <Link 
          href={`/modules/${params.id}`}
          className="text-indigo-400 hover:text-indigo-300"
        >
          ← Back to module
        </Link>
      </div>
    )
  }

  // Determine content to render
  const hasContentBlocks = task.content_blocks && task.content_blocks.length > 0
  const contentBlocks = hasContentBlocks 
    ? task.content_blocks 
    : task.content 
      ? [{ type: 'text', content: task.content }]
      : []

  return (
    <div className="min-h-screen bg-gray-950">
      {/* Header */}
      <header className="sticky top-0 z-30 bg-gray-950/80 backdrop-blur-lg border-b border-gray-800">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            {/* Breadcrumb */}
            <div className="flex items-center gap-2 text-sm">
              <Link 
                href={`/modules/${module?.slug || params.id}`}
                className="text-gray-500 hover:text-white transition-colors"
              >
                {module?.name || 'Module'}
              </Link>
              <span className="text-gray-600">/</span>
              <span className="text-white font-medium truncate max-w-[200px]">
                {task.title}
              </span>
            </div>

            {/* Meta */}
            <div className="flex items-center gap-4">
              {task.estimated_minutes && (
                <div className="flex items-center gap-1.5 text-sm text-gray-400">
                  <Clock className="w-4 h-4" />
                  <span>{task.estimated_minutes} min</span>
                </div>
              )}
              <div className="flex items-center gap-1.5 text-sm text-yellow-400">
                <Zap className="w-4 h-4" />
                <span>+{task.xp_reward} XP</span>
              </div>
              {task.is_completed && (
                <div className="flex items-center gap-1.5 text-sm text-green-400">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Completed</span>
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-6 py-8">
        {/* Title Section */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-3">
            <div className="p-2 rounded-lg bg-indigo-500/10">
              <BookOpen className="w-5 h-5 text-indigo-400" />
            </div>
            <span className="px-2 py-0.5 bg-gray-800 rounded text-xs text-gray-400 uppercase">
              {task.type}
            </span>
          </div>
          <h1 className="text-3xl font-bold text-white mb-2">{task.title}</h1>
          {task.description && (
            <p className="text-gray-400 text-lg">{task.description}</p>
          )}
        </div>

        {/* Content Blocks */}
        <div className="mb-12">
          {contentBlocks.length > 0 ? (
            <ContentBlockRenderer
              blocks={contentBlocks as any[]}
              completedBlocks={completedBlocks}
              onBlockComplete={handleBlockComplete}
            />
          ) : (
            <div className="p-8 bg-gray-900/50 rounded-xl border border-gray-800 text-center">
              <AlertCircle className="w-8 h-8 text-gray-600 mx-auto mb-2" />
              <p className="text-gray-500">Content coming soon...</p>
            </div>
          )}
        </div>

        {/* Complete Button */}
        {!task.is_completed && (
          <div className="flex justify-center mb-12">
            <button
              onClick={handleComplete}
              disabled={isCompleting}
              className="flex items-center gap-2 px-8 py-3 bg-gradient-to-r from-indigo-500 to-purple-500 hover:from-indigo-600 hover:to-purple-600 text-white font-semibold rounded-xl shadow-lg shadow-indigo-500/25 transition-all disabled:opacity-50"
            >
              {isCompleting ? (
                <Loader2 className="w-5 h-5 animate-spin" />
              ) : (
                <CheckCircle2 className="w-5 h-5" />
              )}
              <span>Mark as Complete</span>
              <span className="text-indigo-200">+{task.xp_reward} XP</span>
            </button>
          </div>
        )}
      </main>

      {/* Navigation Footer */}
      <footer className="sticky bottom-0 bg-gray-900/80 backdrop-blur-lg border-t border-gray-800">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            {/* Previous */}
            {prev ? (
              <Link
                href={`/modules/${module?.slug}/tasks/${prev.id}`}
                className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-800 text-gray-400 hover:text-white transition-colors"
              >
                <ArrowLeft className="w-4 h-4" />
                <div className="text-left">
                  <div className="text-xs text-gray-500">Previous</div>
                  <div className="text-sm truncate max-w-[150px]">{prev.title}</div>
                </div>
              </Link>
            ) : (
              <div />
            )}

            {/* Progress Indicator */}
            <div className="hidden md:flex items-center gap-1">
              {module?.tasks.map((t, i) => (
                <div
                  key={t.id}
                  className={`w-2 h-2 rounded-full transition-colors ${
                    t.id === task.id
                      ? 'bg-indigo-500'
                      : t.is_completed
                        ? 'bg-green-500'
                        : 'bg-gray-700'
                  }`}
                />
              ))}
            </div>

            {/* Next */}
            {next ? (
              <Link
                href={`/modules/${module?.slug}/tasks/${next.id}`}
                className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-800 text-gray-400 hover:text-white transition-colors"
              >
                <div className="text-right">
                  <div className="text-xs text-gray-500">Next</div>
                  <div className="text-sm truncate max-w-[150px]">{next.title}</div>
                </div>
                <ArrowRight className="w-4 h-4" />
              </Link>
            ) : (
              <Link
                href={`/modules/${module?.slug}`}
                className="flex items-center gap-2 px-4 py-2 rounded-lg bg-green-500/10 text-green-400 hover:bg-green-500/20 transition-colors"
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>Complete Module</span>
              </Link>
            )}
          </div>
        </div>
      </footer>
    </div>
  )
}
