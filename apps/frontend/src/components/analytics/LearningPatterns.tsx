"use client"

/**
 * ============================================================================
 * LEARNING PATTERNS - Pattern Analysis & Visualization
 * ============================================================================
 *
 * Analyzes and visualizes study patterns with heatmaps, consistency scores,
 * best performance times, and learning style analysis.
 */

import { motion } from "framer-motion"
import { UserAnalytics } from "@/lib/analytics-tracker"
import { cn } from "@/lib/utils"
import {
  Activity,
  Calendar,
  Clock,
  TrendingUp,
  Award,
  Target,
  Sun,
  Moon,
  Sunrise,
  Sunset
} from "lucide-react"

interface LearningPatternsProps {
  analytics: UserAnalytics
}

export function LearningPatterns({ analytics }: LearningPatternsProps) {
  const patterns = analyzePatterns(analytics)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-[#0a0a0f] via-cyan-950/10 to-[#0a0a0f]",
        "border border-cyan-500/20 backdrop-blur-sm"
      )}
    >
      {/* Header */}
      <div className="flex items-center gap-3 mb-6">
        <motion.div
          animate={{
            scale: [1, 1.1, 1],
            opacity: [0.7, 1, 0.7]
          }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        >
          <Activity className="w-6 h-6 text-cyan-400" />
        </motion.div>
        <h2 className="text-xl font-bold text-white">Learning Patterns</h2>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <StatCard
          icon={<Target className="w-5 h-5" />}
          label="Consistency Score"
          value={`${patterns.consistencyScore}%`}
          color="cyan"
        />
        <StatCard
          icon={<Calendar className="w-5 h-5" />}
          label="Best Day"
          value={patterns.bestDay}
          color="purple"
        />
        <StatCard
          icon={<Clock className="w-5 h-5" />}
          label="Avg Session"
          value={`${patterns.avgSessionLength}m`}
          color="emerald"
        />
        <StatCard
          icon={<TrendingUp className="w-5 h-5" />}
          label="Study Style"
          value={patterns.learningStyle}
          color="amber"
        />
      </div>

      {/* Heatmap */}
      <div className="space-y-4">
        <h3 className="text-sm font-semibold text-zinc-400 flex items-center gap-2">
          <Calendar className="w-4 h-4" />
          Study Time Heatmap (by Day & Hour)
        </h3>
        <ProductivityHeatmap heatmap={analytics.productivityHeatmap} />
      </div>

      {/* Peak Times */}
      <div className="mt-6 grid md:grid-cols-2 gap-4">
        <PeakTimesCard patterns={patterns} />
        <LearningStyleCard patterns={patterns} analytics={analytics} />
      </div>
    </motion.div>
  )
}

interface StatCardProps {
  icon: React.ReactNode
  label: string
  value: string
  color: "cyan" | "purple" | "emerald" | "amber"
}

function StatCard({ icon, label, value, color }: StatCardProps) {
  const colorMap = {
    cyan: "text-cyan-400 bg-cyan-500/10 border-cyan-500/30",
    purple: "text-purple-400 bg-purple-500/10 border-purple-500/30",
    emerald: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
    amber: "text-amber-400 bg-amber-500/10 border-amber-500/30"
  }

  return (
    <motion.div
      whileHover={{ scale: 1.02, y: -2 }}
      className={cn(
        "p-4 rounded-xl border backdrop-blur-sm",
        "bg-gradient-to-br from-zinc-900/50 to-zinc-900/20",
        colorMap[color] || colorMap.purple
      )}
    >
      <div className="flex items-center gap-2 mb-2">
        {icon}
        <span className="text-xs text-zinc-500">{label}</span>
      </div>
      <p className="text-2xl font-bold text-white">{value}</p>
    </motion.div>
  )
}

interface HeatmapProps {
  heatmap: number[][]
}

function ProductivityHeatmap({ heatmap }: HeatmapProps) {
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  const hours = Array.from({ length: 24 }, (_, i) => i)

  // Calculate max value for normalization
  const maxValue = Math.max(...heatmap.flat(), 1)

  // Group hours into 4-hour blocks for better visualization
  const hourBlocks = [
    { label: '0-4', start: 0, end: 4 },
    { label: '4-8', start: 4, end: 8 },
    { label: '8-12', start: 8, end: 12 },
    { label: '12-16', start: 12, end: 16 },
    { label: '16-20', start: 16, end: 20 },
    { label: '20-24', start: 20, end: 24 }
  ]

  return (
    <div className="space-y-2">
      {/* Hour labels */}
      <div className="flex gap-1 ml-12">
        {hourBlocks.map(block => (
          <div
            key={block.label}
            className="flex-1 text-xs text-zinc-600 text-center"
          >
            {block.label}
          </div>
        ))}
      </div>

      {/* Heatmap grid */}
      {days.map((day, dayIndex) => (
        <div key={day} className="flex items-center gap-2">
          <div className="w-10 text-xs text-zinc-500 font-medium">
            {day}
          </div>
          <div className="flex-1 flex gap-1">
            {hourBlocks.map(block => {
              // Sum up activity in this block
              const blockActivity = heatmap[dayIndex]
                .slice(block.start, block.end)
                .reduce((sum, val) => sum + val, 0)

              const intensity = blockActivity / maxValue

              return (
                <motion.div
                  key={block.label}
                  className="flex-1 h-8 rounded"
                  style={{
                    backgroundColor: intensity > 0
                      ? `rgba(34, 211, 238, ${0.1 + intensity * 0.7})`
                      : 'rgba(39, 39, 42, 0.3)'
                  }}
                  initial={{ opacity: 0, scale: 0.8 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: dayIndex * 0.05 }}
                  whileHover={{ scale: 1.1, zIndex: 10 }}
                  title={`${day} ${block.label}: ${Math.round(blockActivity)} min`}
                />
              )
            })}
          </div>
        </div>
      ))}

      {/* Legend */}
      <div className="flex items-center justify-end gap-2 mt-4 text-xs text-zinc-500">
        <span>Less</span>
        <div className="flex gap-1">
          {[0.2, 0.4, 0.6, 0.8, 1.0].map((intensity, i) => (
            <div
              key={i}
              className="w-4 h-4 rounded"
              style={{
                backgroundColor: `rgba(34, 211, 238, ${0.1 + intensity * 0.7})`
              }}
            />
          ))}
        </div>
        <span>More</span>
      </div>
    </div>
  )
}

function PeakTimesCard({ patterns }: { patterns: ReturnType<typeof analyzePatterns> }) {
  const timeOfDayIcon = (hour: number) => {
    if (hour >= 6 && hour < 12) return <Sunrise className="w-5 h-5" />
    if (hour >= 12 && hour < 18) return <Sun className="w-5 h-5" />
    if (hour >= 18 && hour < 21) return <Sunset className="w-5 h-5" />
    return <Moon className="w-5 h-5" />
  }

  const timeOfDayLabel = (hour: number) => {
    if (hour >= 6 && hour < 12) return "Morning"
    if (hour >= 12 && hour < 18) return "Afternoon"
    if (hour >= 18 && hour < 21) return "Evening"
    return "Night"
  }

  return (
    <div className={cn(
      "p-5 rounded-xl",
      "bg-gradient-to-br from-purple-600/10 to-purple-500/5",
      "border border-purple-500/20"
    )}>
      <h3 className="text-sm font-semibold text-white mb-4 flex items-center gap-2">
        <Award className="w-4 h-4 text-purple-400" />
        Peak Performance Times
      </h3>
      <div className="space-y-3">
        {patterns.peakHours.slice(0, 3).map((hour, index) => {
          const timeStr = `${hour}:00 - ${(hour + 1) % 24}:00`
          return (
            <motion.div
              key={hour}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="flex items-center gap-3"
            >
              <div className={cn(
                "w-10 h-10 rounded-lg flex items-center justify-center",
                "bg-purple-500/10 border border-purple-500/30",
                "text-purple-400"
              )}>
                {timeOfDayIcon(hour)}
              </div>
              <div className="flex-1">
                <p className="text-sm font-medium text-white">{timeStr}</p>
                <p className="text-xs text-zinc-500">{timeOfDayLabel(hour)} peak</p>
              </div>
              <div className="text-xs font-semibold text-purple-400">
                #{index + 1}
              </div>
            </motion.div>
          )
        })}
      </div>
    </div>
  )
}

function LearningStyleCard({
  patterns,
  analytics
}: {
  patterns: ReturnType<typeof analyzePatterns>
  analytics: UserAnalytics
}) {
  const styleInfo = {
    'Sprint Learner': {
      description: 'Short, intense study sessions',
      tip: 'Perfect for quick reviews and practice',
      color: 'text-amber-400'
    },
    'Marathon Learner': {
      description: 'Long, deep-focus sessions',
      tip: 'Ideal for complex topics and projects',
      color: 'text-emerald-400'
    },
    'Consistent Learner': {
      description: 'Regular, balanced sessions',
      tip: 'Great for steady progress',
      color: 'text-cyan-400'
    },
    'Weekend Warrior': {
      description: 'Focused weekend learning',
      tip: 'Maximize weekend productivity',
      color: 'text-purple-400'
    },
    'Getting Started': {
      description: 'Building your routine',
      tip: 'Keep learning to unlock insights',
      color: 'text-zinc-400'
    }
  }

  const info = styleInfo[patterns.learningStyle as keyof typeof styleInfo] || styleInfo['Getting Started']

  return (
    <div className={cn(
      "p-5 rounded-xl",
      "bg-gradient-to-br from-emerald-600/10 to-emerald-500/5",
      "border border-emerald-500/20"
    )}>
      <h3 className="text-sm font-semibold text-white mb-4 flex items-center gap-2">
        <TrendingUp className="w-4 h-4 text-emerald-400" />
        Your Learning Style
      </h3>
      <div className="space-y-3">
        <div>
          <p className={cn("text-lg font-bold", info.color)}>
            {patterns.learningStyle}
          </p>
          <p className="text-sm text-zinc-400 mt-1">
            {info.description}
          </p>
        </div>
        <div className={cn(
          "p-3 rounded-lg",
          "bg-emerald-500/5 border border-emerald-500/20"
        )}>
          <p className="text-xs text-emerald-400 font-medium mb-1">
            Pro Tip:
          </p>
          <p className="text-xs text-zinc-400">
            {info.tip}
          </p>
        </div>
        {analytics.sessionHistory.length > 0 && (
          <div className="text-xs text-zinc-500">
            Based on {analytics.sessionHistory.length} study sessions
          </div>
        )}
      </div>
    </div>
  )
}

function analyzePatterns(analytics: UserAnalytics) {
  // Calculate consistency score
  const last30Days = analytics.dailyStats.slice(-30)
  const daysWithActivity = last30Days.filter(day => day.studyTime > 0).length
  const consistencyScore = Math.round((daysWithActivity / Math.max(last30Days.length, 1)) * 100)

  // Find best day
  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  const dayTotals = analytics.productivityHeatmap.map((hours, day) => ({
    day,
    total: hours.reduce((sum, min) => sum + min, 0)
  }))
  const bestDayIndex = dayTotals.reduce((max, current) =>
    current.total > max.total ? current : max
  ).day
  const bestDay = dayTotals[bestDayIndex].total > 0 ? dayNames[bestDayIndex] : 'N/A'

  // Calculate average session length
  const completedSessions = analytics.sessionHistory.filter(s => s.endTime)
  const avgSessionLength = completedSessions.length > 0
    ? Math.round(completedSessions.reduce((sum, s) => {
      const duration = Math.floor((s.endTime!.getTime() - s.startTime.getTime()) / 1000 / 60)
      return sum + duration
    }, 0) / completedSessions.length)
    : 0

  // Determine learning style
  let learningStyle = 'Getting Started'
  if (completedSessions.length >= 5) {
    if (avgSessionLength < 20) {
      learningStyle = 'Sprint Learner'
    } else if (avgSessionLength > 45) {
      learningStyle = 'Marathon Learner'
    } else if (consistencyScore >= 70) {
      learningStyle = 'Consistent Learner'
    } else {
      // Check if most activity is on weekends
      const weekendActivity = dayTotals[0].total + dayTotals[6].total
      const totalActivity = dayTotals.reduce((sum, d) => sum + d.total, 0)
      if (totalActivity > 0 && weekendActivity / totalActivity > 0.5) {
        learningStyle = 'Weekend Warrior'
      }
    }
  }

  // Find peak hours
  const hourlyActivity = Array(24).fill(0)
  analytics.productivityHeatmap.forEach(day => {
    day.forEach((minutes, hour) => {
      hourlyActivity[hour] += minutes
    })
  })
  const peakHours = hourlyActivity
    .map((minutes, hour) => ({ hour, minutes }))
    .filter(h => h.minutes > 0)
    .sort((a, b) => b.minutes - a.minutes)
    .slice(0, 3)
    .map(h => h.hour)

  return {
    consistencyScore,
    bestDay,
    avgSessionLength,
    learningStyle,
    peakHours
  }
}
