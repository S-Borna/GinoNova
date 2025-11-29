"use client"

/**
 * ============================================================================
 * SESSION HISTORY — Recent Study Sessions Display
 * ============================================================================
 * 
 * Features:
 * - Balanced compact layout
 * - Session mode badges
 * - XP and task counters
 * - Real dates (not hardcoded)
 * 
 * @phase FAS 1.3 - Fix Recent Sessions balancing
 */

import * as React from "react"
import { Calendar, Clock, Zap, Target } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StudySession {
  id: string
  date: Date | string
  mode: 'pomodoro' | 'deep_focus' | 'custom'
  duration_minutes: number
  tasks_completed: number
  xp_earned: number
}

interface SessionHistoryProps {
  sessions: StudySession[]
  className?: string
}

/* ============================================================================
   HELPERS
   ============================================================================ */

function formatDate(date: Date | string): { day: string; time: string } {
  const d = typeof date === 'string' ? new Date(date) : date
  const now = new Date()
  const diffDays = Math.floor((now.getTime() - d.getTime()) / (1000 * 60 * 60 * 24))
  
  let day: string
  if (diffDays === 0) {
    day = 'Today'
  } else if (diffDays === 1) {
    day = 'Yesterday'
  } else if (diffDays < 7) {
    day = d.toLocaleDateString('en-US', { weekday: 'long' })
  } else {
    day = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
  }
  
  const time = d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' })
  
  return { day, time }
}

function getModeConfig(mode: string): { label: string; bgColor: string; textColor: string } {
  switch (mode.toLowerCase().replace('_', ' ')) {
    case 'pomodoro':
      return { label: 'Pomodoro', bgColor: 'bg-purple-500/20', textColor: 'text-purple-400' }
    case 'deep focus':
    case 'deep_focus':
      return { label: 'Deep Focus', bgColor: 'bg-green-500/20', textColor: 'text-green-400' }
    case 'custom':
      return { label: 'Custom', bgColor: 'bg-orange-500/20', textColor: 'text-orange-400' }
    default:
      return { label: mode, bgColor: 'bg-gray-500/20', textColor: 'text-gray-400' }
  }
}

function formatDuration(minutes: number): string {
  if (minutes < 60) return `${minutes}m`
  const hours = Math.floor(minutes / 60)
  const mins = minutes % 60
  return mins > 0 ? `${hours}h ${mins}m` : `${hours}h`
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function SessionHistory({ sessions, className = "" }: SessionHistoryProps) {
  // Calculate totals
  const totalMinutes = sessions.reduce((sum, s) => sum + s.duration_minutes, 0)
  const totalTasks = sessions.reduce((sum, s) => sum + s.tasks_completed, 0)
  const totalXP = sessions.reduce((sum, s) => sum + s.xp_earned, 0)
  const totalHours = Math.round(totalMinutes / 60 * 10) / 10

  return (
    <div className={`bg-gray-900/50 backdrop-blur-sm rounded-2xl border border-gray-800 overflow-hidden ${className}`}>
      {/* Header */}
      <div className="flex items-center gap-3 px-5 py-4 border-b border-gray-800">
        <div className="p-2 rounded-lg bg-indigo-500/10">
          <Calendar className="w-5 h-5 text-indigo-400" />
        </div>
        <h3 className="text-lg font-semibold text-white">Recent Sessions</h3>
      </div>

      {/* Stats Row */}
      <div className="grid grid-cols-3 divide-x divide-gray-800 border-b border-gray-800">
        <div className="py-4 text-center">
          <div className="text-2xl font-bold text-white">{totalHours}h</div>
          <div className="text-xs text-gray-500 mt-0.5">Total Time</div>
        </div>
        <div className="py-4 text-center">
          <div className="text-2xl font-bold text-white">{totalTasks}</div>
          <div className="text-xs text-gray-500 mt-0.5">Tasks Done</div>
        </div>
        <div className="py-4 text-center">
          <div className="text-2xl font-bold text-yellow-400">{totalXP}</div>
          <div className="text-xs text-gray-500 mt-0.5">XP Earned</div>
        </div>
      </div>

      {/* Session List */}
      <div className="divide-y divide-gray-800/50">
        {sessions.length === 0 ? (
          <div className="px-5 py-8 text-center text-gray-500">
            <Clock className="w-8 h-8 mx-auto mb-2 opacity-50" />
            <p>No sessions yet</p>
            <p className="text-sm mt-1">Start studying to see your history</p>
          </div>
        ) : (
          sessions.slice(0, 5).map((session) => {
            const { day, time } = formatDate(session.date)
            const modeConfig = getModeConfig(session.mode)

            return (
              <div
                key={session.id}
                className="flex items-center justify-between px-5 py-3 hover:bg-gray-800/30 transition-colors"
              >
                {/* Date */}
                <div className="min-w-[80px]">
                  <div className="text-sm font-medium text-white">{day}</div>
                  <div className="text-xs text-gray-500">{time}</div>
                </div>

                {/* Mode Badge */}
                <div className={`px-2.5 py-1 rounded-full text-xs font-medium ${modeConfig.bgColor} ${modeConfig.textColor}`}>
                  {modeConfig.label}
                </div>

                {/* Stats */}
                <div className="flex items-center gap-4 text-sm">
                  <span className="flex items-center gap-1.5 text-gray-400">
                    <Clock className="w-3.5 h-3.5" />
                    {formatDuration(session.duration_minutes)}
                  </span>
                  <span className="flex items-center gap-1.5 text-gray-400">
                    <Target className="w-3.5 h-3.5" />
                    {session.tasks_completed}
                  </span>
                  <span className="flex items-center gap-1.5 text-yellow-400 font-medium min-w-[60px] justify-end">
                    <Zap className="w-3.5 h-3.5" />
                    +{session.xp_earned}
                  </span>
                </div>
              </div>
            )
          })
        )}
      </div>

      {/* View All Link */}
      {sessions.length > 5 && (
        <div className="px-5 py-3 border-t border-gray-800 text-center">
          <button className="text-sm text-indigo-400 hover:text-indigo-300 transition-colors">
            View all {sessions.length} sessions →
          </button>
        </div>
      )}
    </div>
  )
}

export default SessionHistory
