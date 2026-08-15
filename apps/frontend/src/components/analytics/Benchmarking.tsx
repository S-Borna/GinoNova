"use client"

/**
 * ============================================================================
 * BENCHMARKING - Compare Performance with Peer Learners
 * ============================================================================
 *
 * Anonymous benchmarking against cohort with percentile rankings,
 * comparisons of study time, tasks completed, streak, and motivational insights.
 */

import { motion } from "framer-motion"
import { UserAnalytics } from "@/lib/analytics-tracker"
import { cn } from "@/lib/utils"
import {
  Users,
  TrendingUp,
  Award,
  Zap,
  Clock,
  Target,
  Trophy,
  Medal,
  ChevronUp,
  ChevronDown
} from "lucide-react"

interface BenchmarkingProps {
  analytics: UserAnalytics
}

interface BenchmarkMetric {
  label: string
  icon: React.ReactNode
  userValue: number
  avgValue: number
  topValue: number
  percentile: number
  unit: string
  color: string
}

export function Benchmarking({ analytics }: BenchmarkingProps) {
  const benchmarks = calculateBenchmarks(analytics)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-[#0a0a0f] via-purple-950/10 to-[#0a0a0f]",
        "border border-purple-500/20 backdrop-blur-sm"
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
            <Users className="w-6 h-6 text-purple-400" />
          </motion.div>
          <div>
            <h2 className="text-xl font-bold text-white">Benchmarking</h2>
            <p className="text-xs text-zinc-500">Compare with other learners</p>
          </div>
        </div>
        <motion.div
          whileHover={{ scale: 1.05, rotate: 5 }}
          className={cn(
            "px-4 py-2 rounded-xl",
            "bg-gradient-to-r from-purple-500/20 to-cyan-500/20",
            "border border-purple-500/30"
          )}
        >
          <p className="text-xs text-zinc-400">Your Rank</p>
          <p className="text-lg font-bold text-purple-400">
            Top {100 - benchmarks.overallPercentile}%
          </p>
        </motion.div>
      </div>

      {/* Performance Badge */}
      <PerformanceBadge percentile={benchmarks.overallPercentile} />

      {/* Metrics Grid */}
      <div className="grid md:grid-cols-2 gap-4 mt-6">
        {benchmarks.metrics.map((metric, index) => (
          <BenchmarkCard key={metric.label} metric={metric} delay={index * 0.1} />
        ))}
      </div>

      {/* Motivational Message */}
      <MotivationalMessage percentile={benchmarks.overallPercentile} analytics={analytics} />
    </motion.div>
  )
}

interface BenchmarkCardProps {
  metric: BenchmarkMetric
  delay: number
}

function BenchmarkCard({ metric, delay }: BenchmarkCardProps) {
  const percentageOfTop = metric.topValue > 0
    ? (metric.userValue / metric.topValue) * 100
    : 0

  const isAboveAverage = metric.userValue > metric.avgValue

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
      whileHover={{ scale: 1.02, y: -2 }}
      className={cn(
        "relative p-5 rounded-xl",
        "bg-gradient-to-br from-zinc-900/50 to-zinc-900/20",
        "border border-zinc-800",
        "backdrop-blur-sm transition-all duration-300"
      )}
    >
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <div className={cn(
            "w-10 h-10 rounded-lg flex items-center justify-center",
            `bg-${metric.color}-500/10 border border-${metric.color}-500/30`
          )}
            style={{
              backgroundColor: `${metric.color}15`,
              borderColor: `${metric.color}40`
            }}
          >
            <div style={{ color: metric.color }}>
              {metric.icon}
            </div>
          </div>
          <span className="text-sm font-medium text-zinc-300">{metric.label}</span>
        </div>
        <div className={cn(
          "flex items-center gap-1 text-xs font-semibold",
          isAboveAverage ? "text-emerald-400" : "text-amber-400"
        )}>
          {isAboveAverage ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
          <span>{metric.percentile}%</span>
        </div>
      </div>

      {/* Your Value */}
      <div className="mb-4">
        <p className="text-2xl font-bold text-white">
          {metric.userValue.toLocaleString()}{metric.unit}
        </p>
        <p className="text-xs text-zinc-500">Your performance</p>
      </div>

      {/* Comparison Bars */}
      <div className="space-y-3">
        <div>
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-zinc-500">Average</span>
            <span className="text-xs text-zinc-400">{metric.avgValue}{metric.unit}</span>
          </div>
          <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-zinc-600 rounded-full"
              initial={{ width: 0 }}
              animate={{ width: '100%' }}
              transition={{ duration: 1, delay: delay + 0.2 }}
            />
          </div>
        </div>

        <div>
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-zinc-500">You</span>
            <span className="text-xs font-semibold" style={{ color: metric.color }}>
              {metric.userValue}{metric.unit}
            </span>
          </div>
          <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
            <motion.div
              className="h-full rounded-full"
              style={{ backgroundColor: metric.color }}
              initial={{ width: 0 }}
              animate={{ width: `${Math.min(percentageOfTop, 100)}%` }}
              transition={{ duration: 1, delay: delay + 0.3 }}
            />
          </div>
        </div>

        <div>
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-zinc-500">Top 10%</span>
            <span className="text-xs text-amber-400">{metric.topValue}{metric.unit}</span>
          </div>
          <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full"
              initial={{ width: 0 }}
              animate={{ width: '100%' }}
              transition={{ duration: 1, delay: delay + 0.4 }}
            />
          </div>
        </div>
      </div>
    </motion.div>
  )
}

function PerformanceBadge({ percentile }: { percentile: number }) {
  let badge = {
    title: 'Getting Started',
    description: 'Keep learning to improve your rank',
    icon: <Target className="w-8 h-8" />,
    color: 'from-zinc-600 to-zinc-700',
    borderColor: 'border-zinc-500/40'
  }

  if (percentile >= 90) {
    badge = {
      title: 'Elite Performer',
      description: 'Top 10% of all learners',
      icon: <Trophy className="w-8 h-8" />,
      color: 'from-amber-500 to-orange-600',
      borderColor: 'border-amber-500/40'
    }
  } else if (percentile >= 75) {
    badge = {
      title: 'High Achiever',
      description: 'Top 25% of all learners',
      icon: <Medal className="w-8 h-8" />,
      color: 'from-purple-500 to-purple-700',
      borderColor: 'border-purple-500/40'
    }
  } else if (percentile >= 50) {
    badge = {
      title: 'Rising Star',
      description: 'Above average performance',
      icon: <TrendingUp className="w-8 h-8" />,
      color: 'from-cyan-500 to-blue-600',
      borderColor: 'border-cyan-500/40'
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      whileHover={{ scale: 1.02 }}
      className={cn(
        "p-6 rounded-xl",
        "bg-gradient-to-r",
        badge.color,
        "border",
        badge.borderColor,
        "backdrop-blur-sm"
      )}
    >
      <div className="flex items-center gap-4">
        <motion.div
          animate={{
            rotate: [0, 5, -5, 0],
            scale: [1, 1.1, 1]
          }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
          className="text-white"
        >
          {badge.icon}
        </motion.div>
        <div className="flex-1">
          <h3 className="text-lg font-bold text-white mb-1">{badge.title}</h3>
          <p className="text-sm text-white/80">{badge.description}</p>
        </div>
        <div className="text-3xl font-black text-white/90">
          {percentile}
        </div>
      </div>
    </motion.div>
  )
}

function MotivationalMessage({ percentile, analytics }: { percentile: number; analytics: UserAnalytics }) {
  let message = {
    title: 'Keep Building Momentum',
    text: 'Every study session brings you closer to your goals. Stay consistent!',
    color: 'text-cyan-400'
  }

  if (percentile >= 90) {
    message = {
      title: 'Outstanding Performance!',
      text: "You're setting the standard for excellence. Keep inspiring others!",
      color: 'text-amber-400'
    }
  } else if (percentile >= 75) {
    message = {
      title: 'You\'re Doing Great!',
      text: 'Just a bit more effort to join the elite top 10%. You can do it!',
      color: 'text-purple-400'
    }
  } else if (percentile >= 50) {
    message = {
      title: 'Strong Progress!',
      text: 'You\'re above average and climbing. Keep up the consistency!',
      color: 'text-emerald-400'
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.4 }}
      className={cn(
        "mt-6 p-5 rounded-xl",
        "bg-gradient-to-r from-purple-600/10 via-cyan-600/10 to-purple-600/10",
        "border border-purple-500/20"
      )}
    >
      <div className="flex items-start gap-3">
        <motion.div
          animate={{
            scale: [1, 1.2, 1],
            rotate: [0, 10, -10, 0]
          }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        >
          <Award className={cn("w-6 h-6", message.color)} />
        </motion.div>
        <div className="flex-1">
          <h4 className={cn("font-bold mb-1", message.color)}>{message.title}</h4>
          <p className="text-sm text-zinc-400">{message.text}</p>
        </div>
      </div>
    </motion.div>
  )
}

function calculateBenchmarks(analytics: UserAnalytics): {
  metrics: BenchmarkMetric[]
  overallPercentile: number
} {
  // Simulated benchmark data (in a real app, this would come from the backend)
  // These are realistic averages for a learning platform

  const studyTimeHours = Math.round(analytics.totalStudyTime / 60)
  const last7Days = analytics.dailyStats.slice(-7)
  const weeklyStudyTime = last7Days.reduce((sum, day) => sum + day.studyTime, 0)

  const metrics: BenchmarkMetric[] = [
    {
      label: 'Study Time (Total)',
      icon: <Clock className="w-5 h-5" />,
      userValue: studyTimeHours,
      avgValue: 15,
      topValue: 50,
      percentile: Math.min(95, Math.round((studyTimeHours / 50) * 100)),
      unit: 'h',
      color: '#8B5CF6'
    },
    {
      label: 'Current Streak',
      icon: <Zap className="w-5 h-5" />,
      userValue: analytics.currentStreak,
      avgValue: 3,
      topValue: 30,
      percentile: Math.min(95, Math.round((analytics.currentStreak / 30) * 100)),
      unit: ' days',
      color: '#F59E0B'
    },
    {
      label: 'Tasks Completed',
      icon: <Target className="w-5 h-5" />,
      userValue: analytics.tasksCompleted,
      avgValue: 25,
      topValue: 200,
      percentile: Math.min(95, Math.round((analytics.tasksCompleted / 200) * 100)),
      unit: '',
      color: '#22D3EE'
    },
    {
      label: 'Weekly Study Time',
      icon: <TrendingUp className="w-5 h-5" />,
      userValue: Math.round(weeklyStudyTime),
      avgValue: 120,
      topValue: 600,
      percentile: Math.min(95, Math.round((weeklyStudyTime / 600) * 100)),
      unit: ' min',
      color: '#10B981'
    }
  ]

  // Calculate overall percentile (average of all metrics)
  const overallPercentile = Math.round(
    metrics.reduce((sum, m) => sum + m.percentile, 0) / metrics.length
  )

  return { metrics, overallPercentile }
}
