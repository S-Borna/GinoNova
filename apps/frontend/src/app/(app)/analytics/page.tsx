"use client"

/**
 * ============================================================================
 * ANALYTICS DASHBOARD PAGE
 * ============================================================================
 *
 * Comprehensive analytics and insights dashboard for tracking learning progress
 * and optimizing study habits with beautiful data visualizations.
 *
 * Features:
 * - Overview cards with key metrics
 * - Study time analysis (bar charts, heatmaps)
 * - Learning velocity tracking
 * - Skill distribution visualization
 * - Module progress tracking
 * - AI-powered insights
 * - Goal tracking
 * - Benchmarking
 *
 * @phase Analytics Dashboard
 */

import { useEffect, useState } from "react"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { motion } from "framer-motion"
import analyticsTracker, { UserAnalytics } from "@/lib/analytics-tracker"
import { PageLayout } from "@saas/ui"
import {
  BarChart,
  Bar,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell,
  AreaChart,
  Area,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from 'recharts'
import {
  Zap,
  BookOpen,
  Target,
  Flame,
  Clock,
  TrendingUp,
  Award,
  Calendar,
  BarChart3,
  Activity,
  Brain,
  Trophy,
  Sparkles,
  ArrowUp,
  ArrowDown,
  Minus
} from "lucide-react"

// Import sub-components
import { InsightsEngine } from "@/components/analytics/InsightsEngine"
import { LearningPatterns } from "@/components/analytics/LearningPatterns"
import { Benchmarking } from "@/components/analytics/Benchmarking"
import { GoalTracker } from "@/components/analytics/GoalTracker"
import { ReportGenerator } from "@/components/analytics/ReportGenerator"

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden">
      <div className="absolute inset-0 bg-[#05050a]" />

      <div
        className="absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage: `
            linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
            linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
          `,
          backgroundSize: '60px 60px'
        }}
      />

      <motion.div
        className="absolute -top-40 -right-40 w-[800px] h-[800px] rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, rgba(139, 92, 246, 0.05) 40%, transparent 70%)',
        }}
        animate={{
          scale: [1, 1.1, 1],
          opacity: [0.6, 0.8, 0.6],
        }}
        transition={{
          duration: 8,
          repeat: Infinity,
          ease: "easeInOut"
        }}
      />

      <motion.div
        className="absolute -bottom-60 -left-60 w-[700px] h-[700px] rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(34, 211, 238, 0.12) 0%, rgba(34, 211, 238, 0.04) 40%, transparent 70%)',
        }}
        animate={{
          scale: [1, 1.15, 1],
          opacity: [0.5, 0.7, 0.5],
        }}
        transition={{
          duration: 10,
          repeat: Infinity,
          ease: "easeInOut",
          delay: 2
        }}
      />
    </div>
  )
}

/* ============================================================================
   OVERVIEW STAT CARD
   ============================================================================ */

interface StatCardProps {
  icon: React.ReactNode
  label: string
  value: string | number
  subtext?: string
  trend?: 'up' | 'down' | 'neutral'
  trendValue?: string
  color: "purple" | "emerald" | "amber" | "orange" | "blue" | "cyan"
  delay?: number
}

function OverviewStatCard({ icon, label, value, subtext, trend, trendValue, color, delay = 0 }: StatCardProps) {
  const colorMap = {
    purple: {
      bg: "from-purple-600/25 to-purple-500/5",
      border: "border-purple-500/40",
      text: "text-purple-400",
      iconBg: "from-purple-500 to-purple-700",
    },
    emerald: {
      bg: "from-emerald-600/25 to-emerald-500/5",
      border: "border-emerald-500/40",
      text: "text-emerald-400",
      iconBg: "from-emerald-500 to-teal-600",
    },
    cyan: {
      bg: "from-cyan-600/25 to-cyan-500/5",
      border: "border-cyan-500/40",
      text: "text-cyan-400",
      iconBg: "from-cyan-500 to-cyan-600",
    },
    amber: {
      bg: "from-amber-600/25 to-amber-500/5",
      border: "border-amber-500/40",
      text: "text-amber-400",
      iconBg: "from-amber-500 to-orange-600",
    },
    orange: {
      bg: "from-orange-600/25 to-orange-500/5",
      border: "border-orange-500/40",
      text: "text-orange-400",
      iconBg: "from-orange-500 to-red-600",
    },
    blue: {
      bg: "from-blue-600/25 to-blue-500/5",
      border: "border-blue-500/40",
      text: "text-blue-400",
      iconBg: "from-blue-500 to-indigo-600",
    },
  }

  const styles = colorMap[color] || colorMap.purple

  const TrendIcon = trend === 'up' ? ArrowUp : trend === 'down' ? ArrowDown : Minus
  const trendColor = trend === 'up' ? 'text-emerald-400' : trend === 'down' ? 'text-red-400' : 'text-zinc-500'

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
      whileHover={{ scale: 1.02, y: -3 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br",
        styles.bg,
        "border",
        styles.border,
        "backdrop-blur-sm",
        "transition-all duration-300"
      )}
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <p className="text-zinc-500 text-sm font-medium mb-2">{label}</p>
          <p className={cn("text-3xl font-bold", styles.text)}>{value}</p>
          {subtext && <p className="text-zinc-600 text-xs mt-1">{subtext}</p>}

          {trend && trendValue && (
            <div className={cn("flex items-center gap-1 mt-2 text-xs font-medium", trendColor)}>
              <TrendIcon className="w-3 h-3" />
              <span>{trendValue}</span>
            </div>
          )}
        </div>

        <motion.div
          className={cn(
            "w-12 h-12 rounded-xl shrink-0",
            "bg-gradient-to-br",
            styles.iconBg,
            "flex items-center justify-center"
          )}
          animate={{
            boxShadow: [
              '0 0 10px rgba(139, 92, 246, 0.3)',
              '0 0 25px rgba(139, 92, 246, 0.5)',
              '0 0 10px rgba(139, 92, 246, 0.3)',
            ]
          }}
          transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
        >
          {icon}
        </motion.div>
      </div>
    </motion.div>
  )
}

/* ============================================================================
   CHART CONTAINER
   ============================================================================ */

interface ChartContainerProps {
  title: string
  icon: React.ReactNode
  children: React.ReactNode
  className?: string
}

function ChartContainer({ title, icon, children, className }: ChartContainerProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ ease: [0.16, 1, 0.3, 1] }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-[#0a0a0f] via-purple-950/10 to-[#0a0a0f]",
        "border border-purple-500/20",
        "backdrop-blur-sm",
        className
      )}
    >
      <div className="flex items-center gap-2 mb-6">
        <motion.div
          className="text-purple-400"
          animate={{
            scale: [1, 1.1, 1],
            opacity: [0.7, 1, 0.7]
          }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        >
          {icon}
        </motion.div>
        <h3 className="text-lg font-bold text-white">{title}</h3>
      </div>
      {children}
    </motion.div>
  )
}

/* ============================================================================
   MAIN ANALYTICS PAGE
   ============================================================================ */

export default function AnalyticsPage() {
  const { user } = useAuth()
  const [analytics, setAnalytics] = useState<UserAnalytics | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (user?.id) {
      analyticsTracker.initialize(user.id)
      const data = analyticsTracker.getAnalytics()
      setAnalytics(data)
      setLoading(false)
    }
  }, [user?.id])

  if (loading) {
    return (
      <PageLayout maxWidth="wide" background="cosmic">
        <CosmicAurora />
        <div className="relative z-10">
          <div className="animate-pulse space-y-6">
            <div className="h-32 bg-zinc-800/50 rounded-2xl" />
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              {[...Array(4)].map((_, i) => (
                <div key={i} className="h-32 bg-zinc-800/50 rounded-2xl" />
              ))}
            </div>
            <div className="h-96 bg-zinc-800/50 rounded-2xl" />
          </div>
        </div>
      </PageLayout>
    )
  }

  if (!analytics) {
    return (
      <PageLayout maxWidth="wide" background="cosmic">
        <CosmicAurora />
        <div className="relative z-10 text-center py-20">
          <Brain className="w-16 h-16 text-purple-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-white mb-2">No Analytics Data Yet</h2>
          <p className="text-zinc-400">Start learning to see your analytics!</p>
        </div>
      </PageLayout>
    )
  }

  // Prepare chart data
  const last30Days = analytics.dailyStats.slice(-30)
  const studyTimeData = last30Days.map(stat => ({
    date: new Date(stat.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
    minutes: stat.studyTime,
    tasks: stat.tasksCompleted
  }))

  const weeklyData = [
    { day: 'Sun', time: analytics.productivityHeatmap[0].reduce((a, b) => a + b, 0) },
    { day: 'Mon', time: analytics.productivityHeatmap[1].reduce((a, b) => a + b, 0) },
    { day: 'Tue', time: analytics.productivityHeatmap[2].reduce((a, b) => a + b, 0) },
    { day: 'Wed', time: analytics.productivityHeatmap[3].reduce((a, b) => a + b, 0) },
    { day: 'Thu', time: analytics.productivityHeatmap[4].reduce((a, b) => a + b, 0) },
    { day: 'Fri', time: analytics.productivityHeatmap[5].reduce((a, b) => a + b, 0) },
    { day: 'Sat', time: analytics.productivityHeatmap[6].reduce((a, b) => a + b, 0) },
  ]

  const skillData = Object.entries(analytics.skillDistribution).map(([skill, hours]) => ({
    name: skill,
    value: hours,
    hours: hours.toFixed(1)
  }))

  const COLORS = ['#8B5CF6', '#22D3EE', '#F59E0B', '#10B981', '#EF4444', '#EC4899']

  const velocityData = last30Days.map(stat => ({
    date: new Date(stat.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
    tasks: stat.tasksCompleted,
    xp: stat.xpEarned
  }))

  // Calculate trends
  const last7Days = analytics.dailyStats.slice(-7)
  const previous7Days = analytics.dailyStats.slice(-14, -7)

  const last7DaysTime = last7Days.reduce((sum, s) => sum + s.studyTime, 0)
  const previous7DaysTime = previous7Days.reduce((sum, s) => sum + s.studyTime, 0)
  const timeTrend = previous7DaysTime > 0
    ? ((last7DaysTime - previous7DaysTime) / previous7DaysTime * 100).toFixed(0)
    : '0'

  const last7DaysTasks = last7Days.reduce((sum, s) => sum + s.tasksCompleted, 0)
  const previous7DaysTasks = previous7Days.reduce((sum, s) => sum + s.tasksCompleted, 0)
  const tasksTrend = previous7DaysTasks > 0
    ? ((last7DaysTasks - previous7DaysTasks) / previous7DaysTasks * 100).toFixed(0)
    : '0'

  return (
    <PageLayout maxWidth="wide" background="cosmic">
      <CosmicAurora />

      <div className="relative z-10 space-y-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-8"
        >
          <div className="flex items-center justify-center gap-3 mb-3">
            <motion.div
              animate={{
                rotate: 360,
                scale: [1, 1.2, 1],
              }}
              transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
            >
              <BarChart3 className="w-8 h-8 text-purple-400" />
            </motion.div>
            <h1 className="text-4xl md:text-5xl font-black bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent">
              Analytics Dashboard
            </h1>
          </div>
          <p className="text-zinc-400 text-lg">
            Track your progress, optimize your study habits, and achieve your goals
          </p>
        </motion.div>

        {/* AI-Powered Insights */}
        <InsightsEngine analytics={analytics} />

        {/* Overview Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <OverviewStatCard
            icon={<Clock className="w-6 h-6 text-white" />}
            label="Total Study Time"
            value={`${Math.floor(analytics.totalStudyTime / 60)}h ${analytics.totalStudyTime % 60}m`}
            subtext="All time"
            trend={Number(timeTrend) > 0 ? 'up' : Number(timeTrend) < 0 ? 'down' : 'neutral'}
            trendValue={`${timeTrend}% vs last week`}
            color="purple"
            delay={0.1}
          />

          <OverviewStatCard
            icon={<BookOpen className="w-6 h-6 text-white" />}
            label="Modules Completed"
            value={analytics.modulesCompleted}
            subtext={`${analytics.modulesStarted} started`}
            color="cyan"
            delay={0.2}
          />

          <OverviewStatCard
            icon={<Flame className="w-6 h-6 text-white" />}
            label="Current Streak"
            value={`${analytics.currentStreak} days`}
            subtext={`Record: ${analytics.longestStreak} days`}
            trend={analytics.currentStreak > 0 ? 'up' : 'neutral'}
            trendValue="Keep it going!"
            color="orange"
            delay={0.3}
          />

          <OverviewStatCard
            icon={<Zap className="w-6 h-6 text-white" />}
            label="XP This Week"
            value={last7Days.reduce((sum, s) => sum + s.xpEarned, 0)}
            subtext={`${analytics.xpEarned} total XP`}
            trend={Number(tasksTrend) > 0 ? 'up' : Number(tasksTrend) < 0 ? 'down' : 'neutral'}
            trendValue={`${tasksTrend}% vs last week`}
            color="amber"
            delay={0.4}
          />
        </div>

        {/* Study Time Analysis */}
        <div className="grid lg:grid-cols-2 gap-6">
          <ChartContainer title="Study Time (Last 30 Days)" icon={<BarChart3 className="w-5 h-5" />}>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={studyTimeData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#27272a" />
                <XAxis
                  dataKey="date"
                  stroke="#71717a"
                  fontSize={12}
                  tickLine={false}
                />
                <YAxis
                  stroke="#71717a"
                  fontSize={12}
                  tickLine={false}
                  label={{ value: 'Minutes', angle: -90, position: 'insideLeft', fill: '#71717a' }}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#18181b',
                    border: '1px solid #8B5CF6',
                    borderRadius: '8px',
                    color: '#fff'
                  }}
                />
                <Bar dataKey="minutes" fill="#8B5CF6" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </ChartContainer>

          <ChartContainer title="Study Time by Day of Week" icon={<Calendar className="w-5 h-5" />}>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={weeklyData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#27272a" />
                <XAxis
                  dataKey="day"
                  stroke="#71717a"
                  fontSize={12}
                  tickLine={false}
                />
                <YAxis
                  stroke="#71717a"
                  fontSize={12}
                  tickLine={false}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#18181b',
                    border: '1px solid #22D3EE',
                    borderRadius: '8px',
                    color: '#fff'
                  }}
                />
                <Bar dataKey="time" fill="#22D3EE" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </ChartContainer>
        </div>

        {/* Learning Velocity */}
        <ChartContainer title="Learning Velocity (Tasks & XP)" icon={<TrendingUp className="w-5 h-5" />}>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={velocityData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#27272a" />
              <XAxis
                dataKey="date"
                stroke="#71717a"
                fontSize={12}
                tickLine={false}
              />
              <YAxis
                yAxisId="left"
                stroke="#71717a"
                fontSize={12}
                tickLine={false}
              />
              <YAxis
                yAxisId="right"
                orientation="right"
                stroke="#71717a"
                fontSize={12}
                tickLine={false}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: '#18181b',
                  border: '1px solid #8B5CF6',
                  borderRadius: '8px',
                  color: '#fff'
                }}
              />
              <Legend />
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="tasks"
                stroke="#8B5CF6"
                strokeWidth={3}
                dot={{ fill: '#8B5CF6', r: 4 }}
                name="Tasks Completed"
              />
              <Line
                yAxisId="right"
                type="monotone"
                dataKey="xp"
                stroke="#F59E0B"
                strokeWidth={3}
                dot={{ fill: '#F59E0B', r: 4 }}
                name="XP Earned"
              />
            </LineChart>
          </ResponsiveContainer>
        </ChartContainer>

        {/* Skill Distribution */}
        {skillData.length > 0 && (
          <div className="grid lg:grid-cols-2 gap-6">
            <ChartContainer title="Skill Distribution" icon={<Target className="w-5 h-5" />}>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={skillData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name} ${((percent ?? 0) * 100).toFixed(0)}%`}
                    outerRadius={100}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {skillData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#18181b',
                      border: '1px solid #8B5CF6',
                      borderRadius: '8px',
                      color: '#fff'
                    }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </ChartContainer>

            <ChartContainer title="Skill Progress Overview" icon={<Activity className="w-5 h-5" />}>
              <div className="space-y-4">
                {skillData.slice(0, 5).map((skill, index) => {
                  const percentage = (skill.value / Math.max(...skillData.map(s => s.value))) * 100
                  return (
                    <div key={skill.name}>
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-sm font-medium text-zinc-300">{skill.name}</span>
                        <span className="text-sm text-zinc-500">{skill.hours}h</span>
                      </div>
                      <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                        <motion.div
                          className="h-full rounded-full"
                          style={{ backgroundColor: COLORS[index % COLORS.length] }}
                          initial={{ width: 0 }}
                          animate={{ width: `${percentage}%` }}
                          transition={{ duration: 1, delay: index * 0.1 }}
                        />
                      </div>
                    </div>
                  )
                })}
              </div>
            </ChartContainer>
          </div>
        )}

        {/* Learning Patterns Analysis */}
        <LearningPatterns analytics={analytics} />

        {/* Benchmarking */}
        <Benchmarking analytics={analytics} />

        {/* Goal Tracker */}
        <GoalTracker analytics={analytics} />

        {/* Report Generator */}
        <ReportGenerator analytics={analytics} />
      </div>
    </PageLayout>
  )
}
