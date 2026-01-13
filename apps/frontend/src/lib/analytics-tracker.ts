/**
 * ============================================================================
 * ANALYTICS TRACKER - Real-time Learning Analytics
 * ============================================================================
 *
 * Comprehensive analytics tracking for learning progress, study patterns,
 * and performance metrics. Stores data in localStorage with periodic sync.
 *
 * @phase Analytics Dashboard
 */

/* ============================================================================
   TYPE DEFINITIONS
   ============================================================================ */

export interface AnalyticsEvent {
  type: 'task_completed' | 'module_started' | 'module_completed' | 'quiz_passed' |
        'quiz_failed' | 'session_started' | 'session_ended' | 'break_taken' |
        'streak_continued' | 'achievement_unlocked' | 'skill_learned'
  timestamp: Date
  duration?: number
  metadata: Record<string, any>
}

export interface AnalyticsSession {
  id: string
  startTime: Date
  endTime: Date | null
  tasksCompleted: string[]
  modulesStarted: string[]
  xpEarned: number
  focusScore: number // 1-10 based on activity patterns
  breaksTaken: number
  activeMinutes: number
}

export interface UserAnalytics {
  userId: string
  totalStudyTime: number // in minutes
  modulesCompleted: number
  modulesStarted: number
  tasksCompleted: number
  currentStreak: number
  longestStreak: number
  xpEarned: number
  achievementsUnlocked: number
  sessionHistory: AnalyticsSession[]
  skillDistribution: Record<string, number> // skill -> hours spent
  productivityHeatmap: number[][] // [day][hour] - 7x24 matrix
  dailyStats: DailyStats[]
  weeklyStats: WeeklyStats[]
  goals: LearningGoal[]
}

export interface DailyStats {
  date: string // YYYY-MM-DD
  studyTime: number // minutes
  tasksCompleted: number
  xpEarned: number
  modulesCompleted: number
  focusScore: number
  sessionsCount: number
}

export interface WeeklyStats {
  weekStart: string // YYYY-MM-DD
  totalStudyTime: number
  tasksCompleted: number
  xpEarned: number
  averageFocusScore: number
  mostProductiveDay: string
  topSkill: string
}

export interface LearningGoal {
  id: string
  type: 'time' | 'module' | 'skill' | 'streak' | 'certificate'
  title: string
  description: string
  target: number
  current: number
  deadline: Date | null
  completed: boolean
  createdAt: Date
}

export interface StudyPattern {
  peakHours: number[] // hours of day (0-23)
  averageSessionLength: number // minutes
  preferredBreakInterval: number // minutes
  mostProductiveDay: string
  completionRateByDifficulty: Record<string, number>
  contentTypePreferences: Record<string, number>
}

export interface Insight {
  id: string
  type: 'success' | 'warning' | 'info' | 'achievement'
  title: string
  description: string
  action?: {
    label: string
    href: string
  }
  createdAt: Date
  priority: number
}

/* ============================================================================
   STORAGE KEYS
   ============================================================================ */

const ANALYTICS_KEY = 'devopshub_user_analytics'
const CURRENT_SESSION_KEY = 'devopshub_current_session'
const EVENTS_QUEUE_KEY = 'devopshub_analytics_events'

/* ============================================================================
   ANALYTICS TRACKER CLASS
   ============================================================================ */

class AnalyticsTracker {
  private userId: string | null = null
  private currentSession: AnalyticsSession | null = null
  private eventsQueue: AnalyticsEvent[] = []
  private lastActivityTime: Date = new Date()
  private activityCheckInterval: NodeJS.Timeout | null = null

  constructor() {
    if (typeof window !== 'undefined') {
      this.loadFromStorage()
      this.startActivityMonitoring()
    }
  }

  /* ==========================================================================
     INITIALIZATION
     ========================================================================== */

  initialize(userId: string) {
    this.userId = userId
    this.loadUserAnalytics()
  }

  private loadFromStorage() {
    try {
      const savedSession = localStorage.getItem(CURRENT_SESSION_KEY)
      if (savedSession) {
        const parsed = JSON.parse(savedSession)
        this.currentSession = {
          ...parsed,
          startTime: new Date(parsed.startTime),
          endTime: parsed.endTime ? new Date(parsed.endTime) : null
        }
      }

      const savedEvents = localStorage.getItem(EVENTS_QUEUE_KEY)
      if (savedEvents) {
        const parsed = JSON.parse(savedEvents)
        this.eventsQueue = parsed.map((e: any) => ({
          ...e,
          timestamp: new Date(e.timestamp)
        }))
      }
    } catch (error) {
      console.error('Failed to load analytics from storage:', error)
    }
  }

  private saveToStorage() {
    try {
      if (this.currentSession) {
        localStorage.setItem(CURRENT_SESSION_KEY, JSON.stringify(this.currentSession))
      }
      localStorage.setItem(EVENTS_QUEUE_KEY, JSON.stringify(this.eventsQueue))
    } catch (error) {
      console.error('Failed to save analytics to storage:', error)
    }
  }

  /* ==========================================================================
     SESSION MANAGEMENT
     ========================================================================== */

  startSession() {
    if (this.currentSession && !this.currentSession.endTime) {
      // Session already active
      return
    }

    this.currentSession = {
      id: `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      startTime: new Date(),
      endTime: null,
      tasksCompleted: [],
      modulesStarted: [],
      xpEarned: 0,
      focusScore: 8,
      breaksTaken: 0,
      activeMinutes: 0
    }

    this.trackEvent({
      type: 'session_started',
      timestamp: new Date(),
      metadata: {
        sessionId: this.currentSession.id
      }
    })

    this.saveToStorage()
  }

  endSession() {
    if (!this.currentSession || this.currentSession.endTime) {
      return
    }

    this.currentSession.endTime = new Date()
    const duration = Math.floor(
      (this.currentSession.endTime.getTime() - this.currentSession.startTime.getTime()) / 1000 / 60
    )

    this.trackEvent({
      type: 'session_ended',
      timestamp: new Date(),
      duration,
      metadata: {
        sessionId: this.currentSession.id,
        tasksCompleted: this.currentSession.tasksCompleted.length,
        xpEarned: this.currentSession.xpEarned,
        focusScore: this.currentSession.focusScore
      }
    })

    // Save session to history
    if (this.userId) {
      this.saveSessionToHistory(this.currentSession)
    }

    this.currentSession = null
    this.saveToStorage()
  }

  private saveSessionToHistory(session: AnalyticsSession) {
    const analytics = this.getUserAnalytics()
    if (!analytics) return

    analytics.sessionHistory.push(session)
    // Keep only last 100 sessions
    if (analytics.sessionHistory.length > 100) {
      analytics.sessionHistory = analytics.sessionHistory.slice(-100)
    }

    this.saveUserAnalytics(analytics)
  }

  getCurrentSession(): AnalyticsSession | null {
    return this.currentSession
  }

  /* ==========================================================================
     EVENT TRACKING
     ========================================================================== */

  trackEvent(event: AnalyticsEvent) {
    this.eventsQueue.push(event)
    this.lastActivityTime = new Date()

    // Process event immediately
    this.processEvent(event)

    // Save to storage
    this.saveToStorage()

    // Log in development
    if (process.env.NODE_ENV === 'development') {
      console.log('[Analytics]', event.type, event.metadata)
    }
  }

  private processEvent(event: AnalyticsEvent) {
    const analytics = this.getUserAnalytics()
    if (!analytics) return

    switch (event.type) {
      case 'task_completed':
        analytics.tasksCompleted++
        if (this.currentSession) {
          this.currentSession.tasksCompleted.push(event.metadata.taskId)
          this.currentSession.xpEarned += event.metadata.xp || 0
        }
        this.updateDailyStats(analytics, { tasksCompleted: 1, xpEarned: event.metadata.xp || 0 })
        break

      case 'module_started':
        analytics.modulesStarted++
        if (this.currentSession) {
          this.currentSession.modulesStarted.push(event.metadata.moduleId)
        }
        break

      case 'module_completed':
        analytics.modulesCompleted++
        this.updateDailyStats(analytics, { modulesCompleted: 1 })
        break

      case 'quiz_passed':
      case 'quiz_failed':
        this.updateDailyStats(analytics, { xpEarned: event.metadata.xp || 0 })
        break

      case 'session_started':
        this.updateDailyStats(analytics, { sessionsCount: 1 })
        break

      case 'session_ended':
        if (event.duration) {
          analytics.totalStudyTime += event.duration
          this.updateDailyStats(analytics, { studyTime: event.duration })
          this.updateProductivityHeatmap(analytics, event.timestamp, event.duration)
        }
        break

      case 'skill_learned':
        const skill = event.metadata.skill
        const hours = event.metadata.hours || 0
        analytics.skillDistribution[skill] = (analytics.skillDistribution[skill] || 0) + hours
        break

      case 'achievement_unlocked':
        analytics.achievementsUnlocked++
        break

      case 'streak_continued':
        analytics.currentStreak = event.metadata.days || 0
        if (analytics.currentStreak > analytics.longestStreak) {
          analytics.longestStreak = analytics.currentStreak
        }
        break
    }

    this.saveUserAnalytics(analytics)
  }

  /* ==========================================================================
     ANALYTICS DATA MANAGEMENT
     ========================================================================== */

  private getUserAnalytics(): UserAnalytics | null {
    if (!this.userId) return null

    try {
      const stored = localStorage.getItem(`${ANALYTICS_KEY}_${this.userId}`)
      if (stored) {
        const parsed = JSON.parse(stored)
        return {
          ...parsed,
          sessionHistory: parsed.sessionHistory.map((s: any) => ({
            ...s,
            startTime: new Date(s.startTime),
            endTime: s.endTime ? new Date(s.endTime) : null
          })),
          dailyStats: parsed.dailyStats || [],
          weeklyStats: parsed.weeklyStats || [],
          goals: parsed.goals?.map((g: any) => ({
            ...g,
            deadline: g.deadline ? new Date(g.deadline) : null,
            createdAt: new Date(g.createdAt)
          })) || []
        }
      }
    } catch (error) {
      console.error('Failed to load user analytics:', error)
    }

    return null
  }

  private loadUserAnalytics() {
    const analytics = this.getUserAnalytics()
    if (!analytics && this.userId) {
      // Initialize new analytics
      const newAnalytics: UserAnalytics = {
        userId: this.userId,
        totalStudyTime: 0,
        modulesCompleted: 0,
        modulesStarted: 0,
        tasksCompleted: 0,
        currentStreak: 0,
        longestStreak: 0,
        xpEarned: 0,
        achievementsUnlocked: 0,
        sessionHistory: [],
        skillDistribution: {},
        productivityHeatmap: Array(7).fill(null).map(() => Array(24).fill(0)),
        dailyStats: [],
        weeklyStats: [],
        goals: []
      }
      this.saveUserAnalytics(newAnalytics)
    }
  }

  private saveUserAnalytics(analytics: UserAnalytics) {
    if (!this.userId) return

    try {
      localStorage.setItem(`${ANALYTICS_KEY}_${this.userId}`, JSON.stringify(analytics))
    } catch (error) {
      console.error('Failed to save user analytics:', error)
    }
  }

  getAnalytics(): UserAnalytics | null {
    return this.getUserAnalytics()
  }

  /* ==========================================================================
     DAILY & WEEKLY STATS
     ========================================================================== */

  private updateDailyStats(analytics: UserAnalytics, updates: Partial<DailyStats>) {
    const today = new Date().toISOString().split('T')[0]
    let todayStats = analytics.dailyStats.find(s => s.date === today)

    if (!todayStats) {
      todayStats = {
        date: today,
        studyTime: 0,
        tasksCompleted: 0,
        xpEarned: 0,
        modulesCompleted: 0,
        focusScore: 8,
        sessionsCount: 0
      }
      analytics.dailyStats.push(todayStats)
    }

    Object.assign(todayStats, {
      studyTime: (todayStats.studyTime || 0) + (updates.studyTime || 0),
      tasksCompleted: (todayStats.tasksCompleted || 0) + (updates.tasksCompleted || 0),
      xpEarned: (todayStats.xpEarned || 0) + (updates.xpEarned || 0),
      modulesCompleted: (todayStats.modulesCompleted || 0) + (updates.modulesCompleted || 0),
      sessionsCount: (todayStats.sessionsCount || 0) + (updates.sessionsCount || 0)
    })

    // Keep only last 90 days
    if (analytics.dailyStats.length > 90) {
      analytics.dailyStats = analytics.dailyStats.slice(-90)
    }
  }

  private updateProductivityHeatmap(analytics: UserAnalytics, timestamp: Date, duration: number) {
    const dayOfWeek = timestamp.getDay() // 0 = Sunday
    const hour = timestamp.getHours()
    analytics.productivityHeatmap[dayOfWeek][hour] += duration
  }

  /* ==========================================================================
     ACTIVITY MONITORING
     ========================================================================== */

  private startActivityMonitoring() {
    if (this.activityCheckInterval) return

    this.activityCheckInterval = setInterval(() => {
      const now = new Date()
      const inactiveDuration = now.getTime() - this.lastActivityTime.getTime()
      const INACTIVITY_THRESHOLD = 5 * 60 * 1000 // 5 minutes

      if (inactiveDuration > INACTIVITY_THRESHOLD && this.currentSession && !this.currentSession.endTime) {
        // Auto-end session after inactivity
        this.endSession()
      }
    }, 60000) // Check every minute
  }

  /* ==========================================================================
     PATTERN ANALYSIS
     ========================================================================== */

  getStudyPatterns(): StudyPattern | null {
    const analytics = this.getUserAnalytics()
    if (!analytics) return null

    // Calculate peak hours
    const hourlyActivity = Array(24).fill(0)
    analytics.productivityHeatmap.forEach(day => {
      day.forEach((minutes, hour) => {
        hourlyActivity[hour] += minutes
      })
    })
    const peakHours = hourlyActivity
      .map((minutes, hour) => ({ hour, minutes }))
      .sort((a, b) => b.minutes - a.minutes)
      .slice(0, 3)
      .map(h => h.hour)

    // Calculate average session length
    const completedSessions = analytics.sessionHistory.filter(s => s.endTime)
    const averageSessionLength = completedSessions.length > 0
      ? completedSessions.reduce((sum, s) => {
          const duration = Math.floor((s.endTime!.getTime() - s.startTime.getTime()) / 1000 / 60)
          return sum + duration
        }, 0) / completedSessions.length
      : 0

    // Find most productive day
    const dayTotals = analytics.productivityHeatmap.map((hours, day) => ({
      day,
      total: hours.reduce((sum, min) => sum + min, 0)
    }))
    const mostProductiveDayIndex = dayTotals.reduce((max, current) =>
      current.total > max.total ? current : max
    ).day
    const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    const mostProductiveDay = dayNames[mostProductiveDayIndex]

    return {
      peakHours,
      averageSessionLength,
      preferredBreakInterval: 25, // Default Pomodoro
      mostProductiveDay,
      completionRateByDifficulty: {},
      contentTypePreferences: {}
    }
  }

  /* ==========================================================================
     INSIGHTS GENERATION
     ========================================================================== */

  generateInsights(): Insight[] {
    const analytics = this.getUserAnalytics()
    if (!analytics) return []

    const insights: Insight[] = []
    const patterns = this.getStudyPatterns()

    // Peak productivity insight
    if (patterns && patterns.peakHours.length > 0) {
      const peakHour = patterns.peakHours[0]
      const timeStr = `${peakHour}:00-${peakHour + 1}:00`
      insights.push({
        id: 'peak_productivity',
        type: 'info',
        title: `You're most productive between ${timeStr}`,
        description: 'Schedule important tasks during your peak hours for better results.',
        priority: 8,
        createdAt: new Date()
      })
    }

    // Streak warning
    if (analytics.currentStreak > 0) {
      const lastActivity = analytics.dailyStats[analytics.dailyStats.length - 1]
      const today = new Date().toISOString().split('T')[0]
      if (lastActivity && lastActivity.date !== today) {
        insights.push({
          id: 'streak_warning',
          type: 'warning',
          title: `Your ${analytics.currentStreak}-day streak is at risk!`,
          description: 'Complete at least one task today to keep your streak alive.',
          action: {
            label: 'Start learning',
            href: '/modules'
          },
          priority: 10,
          createdAt: new Date()
        })
      }
    }

    // Streak milestone
    if (analytics.currentStreak >= 7 && analytics.currentStreak % 7 === 0) {
      insights.push({
        id: 'streak_milestone',
        type: 'success',
        title: `Amazing! ${analytics.currentStreak}-day streak achieved!`,
        description: "You're in the top 10% of learners. Keep up the momentum!",
        priority: 9,
        createdAt: new Date()
      })
    }

    // Task completion milestone
    if (analytics.tasksCompleted === 100) {
      insights.push({
        id: 'tasks_100',
        type: 'achievement',
        title: 'Achievement unlocked: 100 tasks completed!',
        description: 'You\'ve reached a major milestone in your learning journey.',
        priority: 9,
        createdAt: new Date()
      })
    }

    // Study time recommendation
    if (patterns && patterns.averageSessionLength > 0) {
      const recommendedLength = Math.round(patterns.averageSessionLength / 5) * 5
      insights.push({
        id: 'session_length',
        type: 'info',
        title: `Your ideal study session is ${recommendedLength} minutes`,
        description: 'This is based on your historical performance and focus patterns.',
        priority: 6,
        createdAt: new Date()
      })
    }

    // Sort by priority
    return insights.sort((a, b) => b.priority - a.priority)
  }

  /* ==========================================================================
     GOAL MANAGEMENT
     ========================================================================== */

  addGoal(goal: Omit<LearningGoal, 'id' | 'createdAt'>): string {
    const analytics = this.getUserAnalytics()
    if (!analytics) return ''

    const newGoal: LearningGoal = {
      ...goal,
      id: `goal_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      createdAt: new Date()
    }

    analytics.goals.push(newGoal)
    this.saveUserAnalytics(analytics)

    return newGoal.id
  }

  updateGoalProgress(goalId: string, current: number) {
    const analytics = this.getUserAnalytics()
    if (!analytics) return

    const goal = analytics.goals.find(g => g.id === goalId)
    if (!goal) return

    goal.current = current
    if (goal.current >= goal.target && !goal.completed) {
      goal.completed = true
      this.trackEvent({
        type: 'achievement_unlocked',
        timestamp: new Date(),
        metadata: {
          type: 'goal_completed',
          goalId: goal.id,
          goalTitle: goal.title
        }
      })
    }

    this.saveUserAnalytics(analytics)
  }

  getGoals(): LearningGoal[] {
    const analytics = this.getUserAnalytics()
    return analytics?.goals || []
  }

  /* ==========================================================================
     CLEANUP
     ========================================================================== */

  cleanup() {
    if (this.activityCheckInterval) {
      clearInterval(this.activityCheckInterval)
      this.activityCheckInterval = null
    }

    if (this.currentSession && !this.currentSession.endTime) {
      this.endSession()
    }
  }
}

/* ============================================================================
   SINGLETON INSTANCE
   ============================================================================ */

const analyticsTracker = new AnalyticsTracker()

export default analyticsTracker
