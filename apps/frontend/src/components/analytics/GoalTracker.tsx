"use client"

/**
 * ============================================================================
 * GOAL TRACKER - Goal Setting & Progress Tracking
 * ============================================================================
 *
 * Set and track weekly/monthly goals (study hours, modules, XP),
 * with progress bars, completion celebrations, and AI-suggested goals.
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { UserAnalytics, LearningGoal } from "@/lib/analytics-tracker"
import analyticsTracker from "@/lib/analytics-tracker"
import { cn } from "@/lib/utils"
import {
  Target,
  Plus,
  Clock,
  BookOpen,
  Zap,
  Award,
  Calendar,
  TrendingUp,
  CheckCircle2,
  X,
  Sparkles
} from "lucide-react"
import confetti from "canvas-confetti"

interface GoalTrackerProps {
  analytics: UserAnalytics
}

export function GoalTracker({ analytics }: GoalTrackerProps) {
  const [showAddGoal, setShowAddGoal] = useState(false)
  const [goals, setGoals] = useState<LearningGoal[]>(analytics.goals || [])

  const activeGoals = goals.filter(g => !g.completed)
  const completedGoals = goals.filter(g => g.completed)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-[#0a0a0f] via-emerald-950/10 to-[#0a0a0f]",
        "border border-emerald-500/20 backdrop-blur-sm"
      )}
    >
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <motion.div
            animate={{
              scale: [1, 1.1, 1],
              opacity: [0.7, 1, 0.7]
            }}
            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
          >
            <Target className="w-6 h-6 text-emerald-400" />
          </motion.div>
          <div>
            <h2 className="text-xl font-bold text-white">Goal Tracker</h2>
            <p className="text-xs text-zinc-500">
              {activeGoals.length} active, {completedGoals.length} completed
            </p>
          </div>
        </div>
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={() => setShowAddGoal(true)}
          className={cn(
            "px-4 py-2 rounded-xl",
            "bg-gradient-to-r from-emerald-600 to-emerald-700",
            "text-white text-sm font-semibold",
            "flex items-center gap-2",
            "hover:from-emerald-500 hover:to-emerald-600",
            "transition-all duration-300"
          )}
        >
          <Plus className="w-4 h-4" />
          New Goal
        </motion.button>
      </div>

      {/* Suggested Goals */}
      {activeGoals.length === 0 && (
        <SuggestedGoals analytics={analytics} onSelect={setShowAddGoal} />
      )}

      {/* Active Goals */}
      {activeGoals.length > 0 && (
        <div className="space-y-4 mb-6">
          <h3 className="text-sm font-semibold text-zinc-400">Active Goals</h3>
          {activeGoals.map((goal, index) => (
            <GoalCard
              key={goal.id}
              goal={goal}
              delay={index * 0.1}
              onComplete={() => {
                // Celebration animation
                confetti({
                  particleCount: 100,
                  spread: 70,
                  origin: { y: 0.6 }
                })
                // Update goals list
                setGoals(analyticsTracker.getGoals())
              }}
            />
          ))}
        </div>
      )}

      {/* Completed Goals */}
      {completedGoals.length > 0 && (
        <div className="space-y-4 mt-6">
          <h3 className="text-sm font-semibold text-zinc-400 flex items-center gap-2">
            <Award className="w-4 h-4 text-amber-400" />
            Completed Goals
          </h3>
          <div className="grid gap-3 md:grid-cols-2">
            {completedGoals.slice(-4).map((goal, index) => (
              <CompletedGoalCard key={goal.id} goal={goal} delay={index * 0.05} />
            ))}
          </div>
        </div>
      )}

      {/* Add Goal Modal */}
      <AnimatePresence>
        {showAddGoal && (
          <AddGoalModal
            analytics={analytics}
            onClose={() => setShowAddGoal(false)}
            onAdd={() => {
              setGoals(analyticsTracker.getGoals())
              setShowAddGoal(false)
            }}
          />
        )}
      </AnimatePresence>
    </motion.div>
  )
}

interface GoalCardProps {
  goal: LearningGoal
  delay: number
  onComplete: () => void
}

function GoalCard({ goal, delay, onComplete }: GoalCardProps) {
  const progress = Math.min(100, (goal.current / goal.target) * 100)
  const isNearlyComplete = progress >= 80 && progress < 100

  const typeConfig = {
    time: { icon: <Clock className="w-5 h-5" />, color: '#8B5CF6' },
    module: { icon: <BookOpen className="w-5 h-5" />, color: '#22D3EE' },
    skill: { icon: <Sparkles className="w-5 h-5" />, color: '#F59E0B' },
    streak: { icon: <Zap className="w-5 h-5" />, color: '#EF4444' },
    certificate: { icon: <Award className="w-5 h-5" />, color: '#10B981' }
  }

  const config = typeConfig[goal.type] || typeConfig.module

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
      whileHover={{ scale: 1.01, y: -2 }}
      className={cn(
        "relative p-5 rounded-xl",
        "bg-gradient-to-br from-zinc-900/50 to-zinc-900/20",
        "border border-zinc-800",
        "backdrop-blur-sm transition-all duration-300"
      )}
    >
      {/* Header */}
      <div className="flex items-start gap-3 mb-4">
        <div
          className="w-10 h-10 rounded-lg flex items-center justify-center shrink-0"
          style={{
            backgroundColor: `${config.color}15`,
            borderWidth: '1px',
            borderStyle: 'solid',
            borderColor: `${config.color}40`
          }}
        >
          <div style={{ color: config.color }}>
            {config.icon}
          </div>
        </div>
        <div className="flex-1 min-w-0">
          <h3 className="text-sm font-semibold text-white mb-1">{goal.title}</h3>
          <p className="text-xs text-zinc-500">{goal.description}</p>
        </div>
      </div>

      {/* Progress */}
      <div className="space-y-2">
        <div className="flex items-center justify-between text-sm">
          <span className="text-zinc-400">
            {goal.current} / {goal.target}
          </span>
          <span className="font-semibold" style={{ color: config.color }}>
            {Math.round(progress)}%
          </span>
        </div>
        <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
          <motion.div
            className="h-full rounded-full"
            style={{ backgroundColor: config.color }}
            initial={{ width: 0 }}
            animate={{ width: `${progress}%` }}
            transition={{ duration: 1, ease: "easeOut" }}
          />
        </div>
        {goal.deadline && (
          <div className="flex items-center gap-2 text-xs text-zinc-500">
            <Calendar className="w-3 h-3" />
            Deadline: {new Date(goal.deadline).toLocaleDateString()}
          </div>
        )}
      </div>

      {/* Near completion badge */}
      {isNearlyComplete && (
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          className={cn(
            "mt-3 px-3 py-2 rounded-lg",
            "bg-amber-500/10 border border-amber-500/30",
            "text-xs text-amber-400 font-medium",
            "flex items-center gap-2"
          )}
        >
          <TrendingUp className="w-4 h-4" />
          Almost there! Keep pushing!
        </motion.div>
      )}
    </motion.div>
  )
}

function CompletedGoalCard({ goal, delay }: { goal: LearningGoal; delay: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay }}
      className={cn(
        "p-4 rounded-xl",
        "bg-gradient-to-br from-emerald-600/10 to-emerald-500/5",
        "border border-emerald-500/30"
      )}
    >
      <div className="flex items-center gap-3">
        <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
        <div className="flex-1 min-w-0">
          <p className="text-sm font-medium text-white truncate">{goal.title}</p>
          <p className="text-xs text-zinc-500">
            Completed {new Date(goal.createdAt).toLocaleDateString()}
          </p>
        </div>
      </div>
    </motion.div>
  )
}

function SuggestedGoals({
  analytics,
  onSelect
}: {
  analytics: UserAnalytics
  onSelect: (show: boolean) => void
}) {
  const suggestions = generateSuggestedGoals(analytics)

  return (
    <div className="mb-6">
      <div className="flex items-center gap-2 mb-4">
        <Sparkles className="w-4 h-4 text-purple-400" />
        <h3 className="text-sm font-semibold text-zinc-400">Suggested Goals</h3>
      </div>
      <div className="grid gap-3 md:grid-cols-2">
        {suggestions.map((suggestion, index) => (
          <motion.button
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02, y: -2 }}
            onClick={() => onSelect(true)}
            className={cn(
              "p-4 rounded-xl text-left",
              "bg-gradient-to-br from-purple-600/10 to-purple-500/5",
              "border border-purple-500/30",
              "hover:border-purple-500/50",
              "transition-all duration-300"
            )}
          >
            <div className="flex items-center gap-2 mb-2">
              <Target className="w-4 h-4 text-purple-400" />
              <span className="text-sm font-semibold text-white">{suggestion.title}</span>
            </div>
            <p className="text-xs text-zinc-400">{suggestion.description}</p>
          </motion.button>
        ))}
      </div>
    </div>
  )
}

function AddGoalModal({
  analytics,
  onClose,
  onAdd
}: {
  analytics: UserAnalytics
  onClose: () => void
  onAdd: () => void
}) {
  const [goalType, setGoalType] = useState<LearningGoal['type']>('time')
  const [title, setTitle] = useState('')
  const [target, setTarget] = useState(0)
  const [deadline, setDeadline] = useState('')

  const goalTypes = [
    { value: 'time', label: 'Study Hours', icon: <Clock className="w-4 h-4" /> },
    { value: 'module', label: 'Modules', icon: <BookOpen className="w-4 h-4" /> },
    { value: 'skill', label: 'Skills', icon: <Sparkles className="w-4 h-4" /> },
    { value: 'streak', label: 'Streak Days', icon: <Zap className="w-4 h-4" /> }
  ]

  const handleSubmit = () => {
    if (!title || target <= 0) return

    analyticsTracker.addGoal({
      type: goalType,
      title,
      description: `Reach ${target} ${goalType === 'time' ? 'hours' : goalType}`,
      target,
      current: 0,
      deadline: deadline ? new Date(deadline) : null,
      completed: false
    })

    onAdd()
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4"
      onClick={onClose}
    >
      <motion.div
        initial={{ scale: 0.9, y: 20 }}
        animate={{ scale: 1, y: 0 }}
        exit={{ scale: 0.9, y: 20 }}
        onClick={(e) => e.stopPropagation()}
        className={cn(
          "w-full max-w-md p-6 rounded-2xl",
          "bg-gradient-to-br from-zinc-900 via-zinc-900 to-zinc-800",
          "border border-emerald-500/30"
        )}
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold text-white">Create New Goal</h2>
          <button
            onClick={onClose}
            className="text-zinc-400 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-4">
          {/* Goal Type */}
          <div>
            <label className="text-sm font-medium text-zinc-400 mb-2 block">
              Goal Type
            </label>
            <div className="grid grid-cols-2 gap-2">
              {goalTypes.map((type) => (
                <button
                  key={type.value}
                  onClick={() => setGoalType(type.value as LearningGoal['type'])}
                  className={cn(
                    "p-3 rounded-lg border transition-all",
                    goalType === type.value
                      ? "bg-emerald-500/20 border-emerald-500/50 text-emerald-400"
                      : "bg-zinc-800/50 border-zinc-700 text-zinc-400 hover:border-zinc-600"
                  )}
                >
                  <div className="flex items-center gap-2">
                    {type.icon}
                    <span className="text-sm font-medium">{type.label}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Title */}
          <div>
            <label className="text-sm font-medium text-zinc-400 mb-2 block">
              Goal Title
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g., Study 20 hours this month"
              className={cn(
                "w-full px-4 py-3 rounded-lg",
                "bg-zinc-800 border border-zinc-700",
                "text-white placeholder-zinc-500",
                "focus:outline-none focus:border-emerald-500/50",
                "transition-colors"
              )}
            />
          </div>

          {/* Target */}
          <div>
            <label className="text-sm font-medium text-zinc-400 mb-2 block">
              Target Value
            </label>
            <input
              type="number"
              value={target || ''}
              onChange={(e) => setTarget(Number(e.target.value))}
              placeholder="e.g., 20"
              min="1"
              className={cn(
                "w-full px-4 py-3 rounded-lg",
                "bg-zinc-800 border border-zinc-700",
                "text-white placeholder-zinc-500",
                "focus:outline-none focus:border-emerald-500/50",
                "transition-colors"
              )}
            />
          </div>

          {/* Deadline (Optional) */}
          <div>
            <label className="text-sm font-medium text-zinc-400 mb-2 block">
              Deadline (Optional)
            </label>
            <input
              type="date"
              value={deadline}
              onChange={(e) => setDeadline(e.target.value)}
              className={cn(
                "w-full px-4 py-3 rounded-lg",
                "bg-zinc-800 border border-zinc-700",
                "text-white",
                "focus:outline-none focus:border-emerald-500/50",
                "transition-colors"
              )}
            />
          </div>

          {/* Actions */}
          <div className="flex gap-3 pt-4">
            <button
              onClick={onClose}
              className={cn(
                "flex-1 px-4 py-3 rounded-lg",
                "bg-zinc-800 border border-zinc-700",
                "text-zinc-400 font-medium",
                "hover:bg-zinc-700",
                "transition-colors"
              )}
            >
              Cancel
            </button>
            <button
              onClick={handleSubmit}
              disabled={!title || target <= 0}
              className={cn(
                "flex-1 px-4 py-3 rounded-lg",
                "bg-gradient-to-r from-emerald-600 to-emerald-700",
                "text-white font-semibold",
                "hover:from-emerald-500 hover:to-emerald-600",
                "disabled:opacity-50 disabled:cursor-not-allowed",
                "transition-all"
              )}
            >
              Create Goal
            </button>
          </div>
        </div>
      </motion.div>
    </motion.div>
  )
}

function generateSuggestedGoals(analytics: UserAnalytics) {
  const avgDailyTime = analytics.dailyStats.length > 0
    ? analytics.dailyStats.reduce((sum, d) => sum + d.studyTime, 0) / analytics.dailyStats.length
    : 0

  const suggestions = [
    {
      title: 'Study 10 hours this month',
      description: 'Build a consistent study habit'
    },
    {
      title: 'Complete 3 modules',
      description: 'Expand your knowledge base'
    },
    {
      title: '7-day learning streak',
      description: 'Develop daily learning routine'
    },
    {
      title: 'Master 2 new skills',
      description: 'Diversify your skill set'
    }
  ]

  return suggestions.slice(0, 4)
}
