"use client"

/**
 * ============================================================================
 * INSIGHTS ENGINE - AI-Powered Learning Insights
 * ============================================================================
 *
 * Analyzes learning patterns and provides personalized recommendations,
 * identifies strengths and weaknesses, and suggests optimal study times.
 */

import { motion } from "framer-motion"
import { UserAnalytics } from "@/lib/analytics-tracker"
import { cn } from "@/lib/utils"
import {
  Brain,
  Sparkles,
  TrendingUp,
  AlertCircle,
  Target,
  Clock,
  Zap,
  Award,
  Lightbulb,
  CheckCircle2
} from "lucide-react"

interface InsightsEngineProps {
  analytics: UserAnalytics
}

interface Insight {
  id: string
  type: 'success' | 'warning' | 'info' | 'recommendation'
  icon: React.ReactNode
  title: string
  description: string
  action?: string
  priority: number
}

export function InsightsEngine({ analytics }: InsightsEngineProps) {
  const insights = generateInsights(analytics)

  if (insights.length === 0) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className={cn(
          "relative p-6 rounded-2xl",
          "bg-gradient-to-br from-purple-600/10 via-purple-500/5 to-cyan-500/5",
          "border border-purple-500/20 backdrop-blur-sm"
        )}
      >
        <div className="flex items-center gap-3 mb-4">
          <motion.div
            animate={{
              rotate: [0, 360],
              scale: [1, 1.2, 1]
            }}
            transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
          >
            <Brain className="w-6 h-6 text-purple-400" />
          </motion.div>
          <h2 className="text-xl font-bold text-white">AI Insights Engine</h2>
        </div>
        <p className="text-zinc-400 text-center py-8">
          Keep learning to unlock AI-powered insights and recommendations!
        </p>
      </motion.div>
    )
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-purple-600/10 via-purple-500/5 to-cyan-500/5",
        "border border-purple-500/20 backdrop-blur-sm"
      )}
    >
      {/* Header */}
      <div className="flex items-center gap-3 mb-6">
        <motion.div
          animate={{
            rotate: [0, 360],
            scale: [1, 1.2, 1]
          }}
          transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
        >
          <Brain className="w-6 h-6 text-purple-400" />
        </motion.div>
        <h2 className="text-xl font-bold text-white">AI Insights Engine</h2>
        <motion.div
          animate={{
            opacity: [0.5, 1, 0.5]
          }}
          transition={{ duration: 2, repeat: Infinity }}
          className="ml-auto"
        >
          <Sparkles className="w-5 h-5 text-cyan-400" />
        </motion.div>
      </div>

      {/* Insights Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {insights.map((insight, index) => (
          <InsightCard key={insight.id} insight={insight} delay={index * 0.1} />
        ))}
      </div>
    </motion.div>
  )
}

interface InsightCardProps {
  insight: Insight
  delay: number
}

function InsightCard({ insight, delay }: InsightCardProps) {
  const typeStyles = {
    success: {
      bg: "from-emerald-600/20 to-emerald-500/5",
      border: "border-emerald-500/40",
      iconBg: "bg-emerald-500/20",
      iconColor: "text-emerald-400"
    },
    warning: {
      bg: "from-amber-600/20 to-amber-500/5",
      border: "border-amber-500/40",
      iconBg: "bg-amber-500/20",
      iconColor: "text-amber-400"
    },
    info: {
      bg: "from-cyan-600/20 to-cyan-500/5",
      border: "border-cyan-500/40",
      iconBg: "bg-cyan-500/20",
      iconColor: "text-cyan-400"
    },
    recommendation: {
      bg: "from-purple-600/20 to-purple-500/5",
      border: "border-purple-500/40",
      iconBg: "bg-purple-500/20",
      iconColor: "text-purple-400"
    }
  }

  const style = typeStyles[insight.type]

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
      whileHover={{ scale: 1.02, y: -2 }}
      className={cn(
        "relative p-4 rounded-xl",
        "bg-gradient-to-br",
        style.bg,
        "border",
        style.border,
        "backdrop-blur-sm transition-all duration-300"
      )}
    >
      <div className="flex items-start gap-3">
        <div className={cn(
          "w-10 h-10 rounded-lg flex items-center justify-center shrink-0",
          style.iconBg
        )}>
          <div className={style.iconColor}>
            {insight.icon}
          </div>
        </div>
        <div className="flex-1 min-w-0">
          <h3 className="text-sm font-semibold text-white mb-1">
            {insight.title}
          </h3>
          <p className="text-xs text-zinc-400 leading-relaxed">
            {insight.description}
          </p>
          {insight.action && (
            <p className="text-xs text-purple-400 mt-2 font-medium">
              {insight.action}
            </p>
          )}
        </div>
      </div>
    </motion.div>
  )
}

function generateInsights(analytics: UserAnalytics): Insight[] {
  const insights: Insight[] = []

  // Calculate recent activity (last 7 days)
  const last7Days = analytics.dailyStats.slice(-7)
  const totalStudyTime7Days = last7Days.reduce((sum, day) => sum + day.studyTime, 0)
  const avgStudyTimePerDay = totalStudyTime7Days / Math.max(last7Days.length, 1)

  // Streak insights
  if (analytics.currentStreak >= 7) {
    insights.push({
      id: 'streak_strong',
      type: 'success',
      icon: <Award className="w-5 h-5" />,
      title: `${analytics.currentStreak}-day streak!`,
      description: `You're in the top 15% of learners. Keep the momentum going!`,
      priority: 10
    })
  } else if (analytics.currentStreak > 0) {
    insights.push({
      id: 'streak_growing',
      type: 'info',
      icon: <TrendingUp className="w-5 h-5" />,
      title: `${analytics.currentStreak}-day streak`,
      description: `Reach 7 days to join the top performers!`,
      action: 'Keep going!',
      priority: 8
    })
  } else if (analytics.longestStreak > 0) {
    insights.push({
      id: 'streak_lost',
      type: 'warning',
      icon: <AlertCircle className="w-5 h-5" />,
      title: 'Streak broken',
      description: `Your record was ${analytics.longestStreak} days. Start a new streak today!`,
      action: 'Get back on track',
      priority: 9
    })
  }

  // Peak productivity times
  const hourlyActivity = Array(24).fill(0)
  analytics.productivityHeatmap.forEach(day => {
    day.forEach((minutes, hour) => {
      hourlyActivity[hour] += minutes
    })
  })
  const peakHour = hourlyActivity.indexOf(Math.max(...hourlyActivity))
  if (peakHour >= 0 && hourlyActivity[peakHour] > 0) {
    const timeRange = `${peakHour}:00-${(peakHour + 1) % 24}:00`
    insights.push({
      id: 'peak_time',
      type: 'recommendation',
      icon: <Clock className="w-5 h-5" />,
      title: `Peak focus: ${timeRange}`,
      description: 'Schedule challenging tasks during your most productive hours.',
      priority: 7
    })
  }

  // Study consistency
  if (avgStudyTimePerDay >= 30) {
    insights.push({
      id: 'consistency_high',
      type: 'success',
      icon: <CheckCircle2 className="w-5 h-5" />,
      title: 'Excellent consistency',
      description: `Averaging ${Math.round(avgStudyTimePerDay)} min/day this week!`,
      priority: 8
    })
  } else if (avgStudyTimePerDay >= 15) {
    insights.push({
      id: 'consistency_good',
      type: 'info',
      icon: <Target className="w-5 h-5" />,
      title: 'Good progress',
      description: `Try to reach 30 minutes daily for optimal learning.`,
      action: 'Increase study time',
      priority: 6
    })
  } else if (last7Days.length > 0) {
    insights.push({
      id: 'consistency_low',
      type: 'warning',
      icon: <AlertCircle className="w-5 h-5" />,
      title: 'Increase consistency',
      description: 'Aim for at least 15-20 minutes of daily practice.',
      action: 'Set a daily goal',
      priority: 9
    })
  }

  // Learning velocity
  const recentTasks = last7Days.reduce((sum, day) => sum + day.tasksCompleted, 0)
  if (recentTasks >= 10) {
    insights.push({
      id: 'velocity_high',
      type: 'success',
      icon: <Zap className="w-5 h-5" />,
      title: 'High velocity',
      description: `${recentTasks} tasks completed this week. You're crushing it!`,
      priority: 7
    })
  }

  // Skill diversity
  const skillCount = Object.keys(analytics.skillDistribution).length
  if (skillCount >= 5) {
    insights.push({
      id: 'skill_diversity',
      type: 'success',
      icon: <Sparkles className="w-5 h-5" />,
      title: 'Diverse skill set',
      description: `Learning ${skillCount} different skills. Great for career growth!`,
      priority: 6
    })
  } else if (skillCount >= 1 && skillCount < 3) {
    insights.push({
      id: 'skill_expand',
      type: 'recommendation',
      icon: <Lightbulb className="w-5 h-5" />,
      title: 'Broaden your skills',
      description: 'Try exploring related technologies to become more versatile.',
      action: 'Explore new modules',
      priority: 5
    })
  }

  // Completion rate
  const completionRate = analytics.modulesStarted > 0
    ? (analytics.modulesCompleted / analytics.modulesStarted) * 100
    : 0

  if (completionRate >= 80 && analytics.modulesCompleted > 0) {
    insights.push({
      id: 'completion_high',
      type: 'success',
      icon: <Award className="w-5 h-5" />,
      title: 'High completion rate',
      description: `${Math.round(completionRate)}% of started modules completed. Excellent!`,
      priority: 7
    })
  } else if (completionRate < 50 && analytics.modulesStarted >= 3) {
    insights.push({
      id: 'completion_low',
      type: 'warning',
      icon: <Target className="w-5 h-5" />,
      title: 'Focus on completion',
      description: `Many modules started but not finished. Try completing one before starting another.`,
      action: 'Finish in-progress modules',
      priority: 8
    })
  }

  // Sort by priority and limit to top 6
  return insights.sort((a, b) => b.priority - a.priority).slice(0, 6)
}
