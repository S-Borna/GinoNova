"use client"

/**
 * ============================================================================
 * REPORT GENERATOR - Progress Reports & Export
 * ============================================================================
 *
 * Generate weekly/monthly summaries with charts and statistics,
 * PDF export functionality, and shareable progress cards for LinkedIn.
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { UserAnalytics } from "@/lib/analytics-tracker"
import { cn } from "@/lib/utils"
import {
  FileText,
  Download,
  Share2,
  Calendar,
  TrendingUp,
  Award,
  Clock,
  Target,
  BookOpen,
  Zap,
  CheckCircle2,
  Copy,
  X,
  Sparkles
} from "lucide-react"

interface ReportGeneratorProps {
  analytics: UserAnalytics
}

type ReportPeriod = 'week' | 'month' | 'all-time'

export function ReportGenerator({ analytics }: ReportGeneratorProps) {
  const [period, setPeriod] = useState<ReportPeriod>('week')
  const [showShareModal, setShowShareModal] = useState(false)

  const report = generateReport(analytics, period)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "relative p-6 rounded-2xl",
        "bg-gradient-to-br from-[#0a0a0f] via-amber-950/10 to-[#0a0a0f]",
        "border border-amber-500/20 backdrop-blur-sm"
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
            <FileText className="w-6 h-6 text-amber-400" />
          </motion.div>
          <div>
            <h2 className="text-xl font-bold text-white">Progress Reports</h2>
            <p className="text-xs text-zinc-500">Export and share your achievements</p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setShowShareModal(true)}
            className={cn(
              "px-4 py-2 rounded-xl",
              "bg-gradient-to-r from-purple-600/20 to-purple-700/20",
              "border border-purple-500/30",
              "text-purple-400 text-sm font-semibold",
              "flex items-center gap-2",
              "hover:border-purple-500/50",
              "transition-all duration-300"
            )}
          >
            <Share2 className="w-4 h-4" />
            Share
          </motion.button>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => downloadReport(report)}
            className={cn(
              "px-4 py-2 rounded-xl",
              "bg-gradient-to-r from-amber-600 to-amber-700",
              "text-white text-sm font-semibold",
              "flex items-center gap-2",
              "hover:from-amber-500 hover:to-amber-600",
              "transition-all duration-300"
            )}
          >
            <Download className="w-4 h-4" />
            Export PDF
          </motion.button>
        </div>
      </div>

      {/* Period Selector */}
      <div className="flex gap-2 mb-6">
        {(['week', 'month', 'all-time'] as ReportPeriod[]).map((p) => (
          <button
            key={p}
            onClick={() => setPeriod(p)}
            className={cn(
              "px-4 py-2 rounded-lg text-sm font-medium transition-all",
              period === p
                ? "bg-amber-500/20 border border-amber-500/50 text-amber-400"
                : "bg-zinc-800/50 border border-zinc-700 text-zinc-400 hover:border-zinc-600"
            )}
          >
            {p === 'all-time' ? 'All Time' : `Last ${p.charAt(0).toUpperCase() + p.slice(1)}`}
          </button>
        ))}
      </div>

      {/* Report Summary */}
      <ReportSummary report={report} />

      {/* Key Achievements */}
      <KeyAchievements report={report} />

      {/* Share Modal */}
      <AnimatePresence>
        {showShareModal && (
          <ShareModal
            report={report}
            analytics={analytics}
            onClose={() => setShowShareModal(false)}
          />
        )}
      </AnimatePresence>
    </motion.div>
  )
}

interface Report {
  period: string
  studyTime: number
  tasksCompleted: number
  modulesCompleted: number
  xpEarned: number
  currentStreak: number
  averageSessionLength: number
  topSkill: string
  improvements: string[]
  highlights: string[]
}

function ReportSummary({ report }: { report: Report }) {
  const stats = [
    {
      icon: <Clock className="w-5 h-5" />,
      label: 'Study Time',
      value: `${Math.floor(report.studyTime / 60)}h ${report.studyTime % 60}m`,
      color: 'purple'
    },
    {
      icon: <Target className="w-5 h-5" />,
      label: 'Tasks Completed',
      value: report.tasksCompleted,
      color: 'cyan'
    },
    {
      icon: <BookOpen className="w-5 h-5" />,
      label: 'Modules Done',
      value: report.modulesCompleted,
      color: 'emerald'
    },
    {
      icon: <Zap className="w-5 h-5" />,
      label: 'XP Earned',
      value: report.xpEarned,
      color: 'amber'
    }
  ]

  const colorMap = {
    purple: 'bg-purple-500/10 border-purple-500/30 text-purple-400',
    cyan: 'bg-cyan-500/10 border-cyan-500/30 text-cyan-400',
    emerald: 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400',
    amber: 'bg-amber-500/10 border-amber-500/30 text-amber-400'
  }

  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      {stats.map((stat, index) => (
        <motion.div
          key={stat.label}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.05 }}
          whileHover={{ scale: 1.02, y: -2 }}
          className={cn(
            "p-4 rounded-xl border backdrop-blur-sm",
            "bg-gradient-to-br from-zinc-900/50 to-zinc-900/20",
            colorMap[stat.color as keyof typeof colorMap]
          )}
        >
          <div className="flex items-center gap-2 mb-2">
            {stat.icon}
            <span className="text-xs text-zinc-500">{stat.label}</span>
          </div>
          <p className="text-2xl font-bold text-white">
            {typeof stat.value === 'number' ? stat.value.toLocaleString() : stat.value}
          </p>
        </motion.div>
      ))}
    </div>
  )
}

function KeyAchievements({ report }: { report: Report }) {
  return (
    <div className="space-y-4">
      {/* Highlights */}
      {report.highlights.length > 0 && (
        <div>
          <h3 className="text-sm font-semibold text-zinc-400 mb-3 flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-amber-400" />
            Highlights
          </h3>
          <div className="space-y-2">
            {report.highlights.map((highlight, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className={cn(
                  "p-4 rounded-xl",
                  "bg-gradient-to-r from-amber-600/10 to-amber-500/5",
                  "border border-amber-500/20"
                )}
              >
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                  <p className="text-sm text-zinc-300">{highlight}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      )}

      {/* Areas for Improvement */}
      {report.improvements.length > 0 && (
        <div className="mt-6">
          <h3 className="text-sm font-semibold text-zinc-400 mb-3 flex items-center gap-2">
            <TrendingUp className="w-4 h-4 text-cyan-400" />
            Growth Opportunities
          </h3>
          <div className="space-y-2">
            {report.improvements.map((improvement, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.2 + index * 0.1 }}
                className={cn(
                  "p-4 rounded-xl",
                  "bg-gradient-to-r from-cyan-600/10 to-cyan-500/5",
                  "border border-cyan-500/20"
                )}
              >
                <div className="flex items-start gap-3">
                  <Target className="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" />
                  <p className="text-sm text-zinc-300">{improvement}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function ShareModal({
  report,
  analytics,
  onClose
}: {
  report: Report
  analytics: UserAnalytics
  onClose: () => void
}) {
  const [copied, setCopied] = useState(false)

  const shareText = `🚀 My DevOps Learning Progress (${report.period})

📚 Study Time: ${Math.floor(report.studyTime / 60)}h ${report.studyTime % 60}m
✅ Tasks Completed: ${report.tasksCompleted}
🎯 Modules Finished: ${report.modulesCompleted}
⚡ XP Earned: ${report.xpEarned}
🔥 Current Streak: ${report.currentStreak} days

Keep learning, keep growing! 💪

#DevOps #Learning #TechSkills #ContinuousLearning`

  const handleCopy = () => {
    navigator.clipboard.writeText(shareText)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
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
          "w-full max-w-lg p-6 rounded-2xl",
          "bg-gradient-to-br from-zinc-900 via-zinc-900 to-zinc-800",
          "border border-amber-500/30"
        )}
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <Share2 className="w-5 h-5 text-amber-400" />
            Share Your Progress
          </h2>
          <button
            onClick={onClose}
            className="text-zinc-400 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Progress Card Preview */}
        <div
          className={cn(
            "mb-6 p-6 rounded-xl",
            "bg-gradient-to-br from-purple-600/20 via-cyan-600/10 to-amber-600/20",
            "border border-purple-500/30"
          )}
        >
          <div className="flex items-center gap-3 mb-4">
            <Award className="w-8 h-8 text-amber-400" />
            <div>
              <h3 className="text-lg font-bold text-white">Learning Progress</h3>
              <p className="text-xs text-zinc-400">{report.period}</p>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div className="text-center p-3 rounded-lg bg-black/20">
              <p className="text-2xl font-bold text-purple-400">
                {Math.floor(report.studyTime / 60)}h
              </p>
              <p className="text-xs text-zinc-500">Study Time</p>
            </div>
            <div className="text-center p-3 rounded-lg bg-black/20">
              <p className="text-2xl font-bold text-cyan-400">{report.tasksCompleted}</p>
              <p className="text-xs text-zinc-500">Tasks Done</p>
            </div>
            <div className="text-center p-3 rounded-lg bg-black/20">
              <p className="text-2xl font-bold text-emerald-400">{report.modulesCompleted}</p>
              <p className="text-xs text-zinc-500">Modules</p>
            </div>
            <div className="text-center p-3 rounded-lg bg-black/20">
              <p className="text-2xl font-bold text-amber-400">{report.currentStreak}</p>
              <p className="text-xs text-zinc-500">Day Streak</p>
            </div>
          </div>
        </div>

        {/* Share Text */}
        <div className="mb-4">
          <label className="text-sm font-medium text-zinc-400 mb-2 block">
            Copy for LinkedIn/Twitter
          </label>
          <div className={cn(
            "p-4 rounded-lg",
            "bg-zinc-800 border border-zinc-700",
            "text-sm text-zinc-300 whitespace-pre-line"
          )}>
            {shareText}
          </div>
        </div>

        {/* Actions */}
        <div className="flex gap-3">
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
            Close
          </button>
          <button
            onClick={handleCopy}
            className={cn(
              "flex-1 px-4 py-3 rounded-lg",
              "bg-gradient-to-r from-amber-600 to-amber-700",
              "text-white font-semibold",
              "hover:from-amber-500 hover:to-amber-600",
              "flex items-center justify-center gap-2",
              "transition-all"
            )}
          >
            {copied ? (
              <>
                <CheckCircle2 className="w-4 h-4" />
                Copied!
              </>
            ) : (
              <>
                <Copy className="w-4 h-4" />
                Copy Text
              </>
            )}
          </button>
        </div>
      </motion.div>
    </motion.div>
  )
}

function generateReport(analytics: UserAnalytics, period: ReportPeriod): Report {
  let periodData = analytics.dailyStats
  let periodLabel = 'All Time'

  if (period === 'week') {
    periodData = analytics.dailyStats.slice(-7)
    periodLabel = 'Last 7 Days'
  } else if (period === 'month') {
    periodData = analytics.dailyStats.slice(-30)
    periodLabel = 'Last 30 Days'
  }

  const studyTime = periodData.reduce((sum, day) => sum + day.studyTime, 0)
  const tasksCompleted = periodData.reduce((sum, day) => sum + day.tasksCompleted, 0)
  const modulesCompleted = periodData.reduce((sum, day) => sum + day.modulesCompleted, 0)
  const xpEarned = periodData.reduce((sum, day) => sum + day.xpEarned, 0)

  // Calculate average session length
  const sessions = analytics.sessionHistory.filter(s => s.endTime)
  const avgSessionLength = sessions.length > 0
    ? Math.round(sessions.reduce((sum, s) => {
        const duration = Math.floor((s.endTime!.getTime() - s.startTime.getTime()) / 1000 / 60)
        return sum + duration
      }, 0) / sessions.length)
    : 0

  // Find top skill
  const topSkill = Object.entries(analytics.skillDistribution)
    .sort((a, b) => b[1] - a[1])[0]?.[0] || 'N/A'

  // Generate highlights
  const highlights: string[] = []
  if (analytics.currentStreak >= 7) {
    highlights.push(`Maintained a ${analytics.currentStreak}-day learning streak!`)
  }
  if (studyTime >= 300) {
    highlights.push(`Dedicated ${Math.floor(studyTime / 60)} hours to learning this period.`)
  }
  if (modulesCompleted >= 2) {
    highlights.push(`Completed ${modulesCompleted} modules successfully.`)
  }
  if (tasksCompleted >= 20) {
    highlights.push(`Crushed ${tasksCompleted} tasks with excellent momentum.`)
  }
  if (highlights.length === 0) {
    highlights.push('Started your learning journey. Keep building momentum!')
  }

  // Generate improvements
  const improvements: string[] = []
  const avgDailyTime = periodData.length > 0 ? studyTime / periodData.length : 0
  if (avgDailyTime < 15) {
    improvements.push('Try to increase daily study time to 15-20 minutes for optimal learning.')
  }
  if (analytics.currentStreak < 3) {
    improvements.push('Build consistency by studying at least once daily.')
  }
  if (Object.keys(analytics.skillDistribution).length < 3) {
    improvements.push('Explore diverse topics to broaden your skill set.')
  }
  const completionRate = analytics.modulesStarted > 0
    ? (analytics.modulesCompleted / analytics.modulesStarted) * 100
    : 0
  if (completionRate < 50 && analytics.modulesStarted >= 3) {
    improvements.push('Focus on completing started modules before beginning new ones.')
  }

  return {
    period: periodLabel,
    studyTime,
    tasksCompleted,
    modulesCompleted,
    xpEarned,
    currentStreak: analytics.currentStreak,
    averageSessionLength: avgSessionLength,
    topSkill,
    improvements,
    highlights
  }
}

function downloadReport(report: Report) {
  // Generate a simple text-based report
  const reportText = `
===================================================
          DEVOPS LEARNING PROGRESS REPORT
===================================================

Period: ${report.period}
Generated: ${new Date().toLocaleDateString()}

===================================================
                 SUMMARY STATISTICS
===================================================

Study Time:           ${Math.floor(report.studyTime / 60)}h ${report.studyTime % 60}m
Tasks Completed:      ${report.tasksCompleted}
Modules Completed:    ${report.modulesCompleted}
XP Earned:            ${report.xpEarned}
Current Streak:       ${report.currentStreak} days
Avg Session Length:   ${report.averageSessionLength} minutes
Top Skill:            ${report.topSkill}

===================================================
                    HIGHLIGHTS
===================================================

${report.highlights.map((h, i) => `${i + 1}. ${h}`).join('\n')}

===================================================
              GROWTH OPPORTUNITIES
===================================================

${report.improvements.map((i, idx) => `${idx + 1}. ${i}`).join('\n')}

===================================================
           Keep learning, keep growing!
===================================================
`

  // Create and download the file
  const blob = new Blob([reportText], { type: 'text/plain' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `learning-report-${new Date().toISOString().split('T')[0]}.txt`
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}
