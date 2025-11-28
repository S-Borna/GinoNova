'use client';

import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Trophy, 
  Clock, 
  CheckCircle2, 
  Star, 
  Flame, 
  TrendingUp,
  Share2,
  RotateCcw,
  Home,
  ArrowRight
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { SessionContext } from '@/lib/studyflow/sessionMachine';
import { cn } from '@/lib/utils';
import confetti from 'canvas-confetti';

interface SessionSummaryProps {
  session: SessionContext;
  onStartNewSession?: () => void;
  onGoHome?: () => void;
  onShare?: () => void;
  streak?: number;
  dailyGoal?: number;
  dailyProgress?: number;
}

interface StatCardProps {
  icon: React.ReactNode;
  label: string;
  value: string | number;
  subValue?: string;
  delay: number;
}

function StatCard({ icon, label, value, subValue, delay }: StatCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.5 }}
    >
      <Card className="bg-card/50 backdrop-blur-sm border-border/50">
        <CardContent className="p-4 flex items-center gap-4">
          <div className="p-3 rounded-full bg-primary/10 text-primary">
            {icon}
          </div>
          <div>
            <p className="text-sm text-muted-foreground">{label}</p>
            <p className="text-2xl font-bold">{value}</p>
            {subValue && (
              <p className="text-xs text-muted-foreground">{subValue}</p>
            )}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}

function formatDuration(seconds: number): string {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  
  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  return `${minutes}m`;
}

export function SessionSummary({
  session,
  onStartNewSession,
  onGoHome,
  onShare,
  streak = 0,
  dailyGoal = 60, // 60 minutes default
  dailyProgress = 0,
}: SessionSummaryProps) {
  const [showConfetti, setShowConfetti] = useState(false);
  const [animatedXP, setAnimatedXP] = useState(0);

  // Calculate session stats
  const focusTimeSeconds = session.totalFocusTime || 0;
  const focusTimeMinutes = Math.floor(focusTimeSeconds / 60);
  const tasksCompleted = session.tasksCompleted?.length || 0;
  const xpEarned = session.xpEarned || 0;
  const completedPhases = session.currentSession || 0;

  // Trigger confetti on mount for good sessions
  useEffect(() => {
    if (tasksCompleted > 0 || focusTimeMinutes >= 25) {
      setShowConfetti(true);
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
      });
    }
  }, [tasksCompleted, focusTimeMinutes]);

  // Animate XP counter
  useEffect(() => {
    const duration = 1500;
    const steps = 30;
    const increment = xpEarned / steps;
    let current = 0;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= xpEarned) {
        setAnimatedXP(xpEarned);
        clearInterval(timer);
      } else {
        setAnimatedXP(Math.floor(current));
      }
    }, duration / steps);

    return () => clearInterval(timer);
  }, [xpEarned]);

  // Calculate daily progress percentage
  const newDailyProgress = dailyProgress + focusTimeMinutes;
  const dailyProgressPercent = Math.min((newDailyProgress / dailyGoal) * 100, 100);
  const reachedDailyGoal = newDailyProgress >= dailyGoal;

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-background to-primary/5 p-6">
      <div className="max-w-2xl mx-auto space-y-8">
        {/* Header */}
        <motion.div
          className="text-center space-y-4"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <motion.div
            className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-gradient-to-br from-primary to-primary/60 text-primary-foreground"
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ delay: 0.2, type: 'spring', stiffness: 200 }}
          >
            <Trophy className="h-10 w-10" />
          </motion.div>
          <h1 className="text-3xl font-bold">Session Complete!</h1>
          <p className="text-muted-foreground">
            Great work! Here&apos;s what you accomplished
          </p>
        </motion.div>

        {/* XP Earned Banner */}
        <motion.div
          className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-yellow-500/20 via-amber-500/20 to-orange-500/20 border border-yellow-500/30 p-6"
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3 }}
        >
          <div className="flex items-center justify-center gap-4">
            <Star className="h-8 w-8 text-yellow-500" />
            <div className="text-center">
              <p className="text-sm text-muted-foreground">XP Earned</p>
              <p className="text-4xl font-bold text-yellow-500">+{animatedXP}</p>
            </div>
            <Star className="h-8 w-8 text-yellow-500" />
          </div>
          
          {/* Sparkle effects */}
          <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {[...Array(5)].map((_, i) => (
              <motion.div
                key={i}
                className="absolute w-1 h-1 bg-yellow-400 rounded-full"
                style={{
                  left: `${20 + i * 15}%`,
                  top: `${20 + (i % 3) * 30}%`,
                }}
                animate={{
                  opacity: [0, 1, 0],
                  scale: [0, 1.5, 0],
                }}
                transition={{
                  duration: 2,
                  repeat: Infinity,
                  delay: i * 0.3,
                }}
              />
            ))}
          </div>
        </motion.div>

        {/* Stats Grid */}
        <div className="grid grid-cols-2 gap-4">
          <StatCard
            icon={<Clock className="h-5 w-5" />}
            label="Focus Time"
            value={formatDuration(focusTimeSeconds)}
            subValue={`${completedPhases} pomodoro${completedPhases !== 1 ? 's' : ''}`}
            delay={0.4}
          />
          <StatCard
            icon={<CheckCircle2 className="h-5 w-5" />}
            label="Tasks Completed"
            value={tasksCompleted}
            subValue={tasksCompleted > 0 ? 'Great progress!' : 'Keep going!'}
            delay={0.5}
          />
          <StatCard
            icon={<Flame className="h-5 w-5" />}
            label="Current Streak"
            value={`${streak} day${streak !== 1 ? 's' : ''}`}
            subValue={streak > 0 ? '🔥 On fire!' : 'Start your streak!'}
            delay={0.6}
          />
          <StatCard
            icon={<TrendingUp className="h-5 w-5" />}
            label="Daily Progress"
            value={`${newDailyProgress}m`}
            subValue={`of ${dailyGoal}m goal`}
            delay={0.7}
          />
        </div>

        {/* Daily Goal Progress */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.8 }}
        >
          <Card className={cn(
            'overflow-hidden transition-all',
            reachedDailyGoal && 'border-green-500/50 bg-green-500/5'
          )}>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm font-medium flex items-center justify-between">
                <span>Daily Goal Progress</span>
                {reachedDailyGoal && (
                  <Badge variant="outline" className="bg-green-500/10 text-green-500 border-green-500/30">
                    Goal Reached! 🎉
                  </Badge>
                )}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                <Progress 
                  value={dailyProgressPercent} 
                  className={cn(
                    'h-3',
                    reachedDailyGoal && '[&>div]:bg-green-500'
                  )}
                />
                <div className="flex justify-between text-xs text-muted-foreground">
                  <span>{newDailyProgress} minutes</span>
                  <span>{Math.round(dailyProgressPercent)}%</span>
                  <span>{dailyGoal} minutes</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        {/* Completed Tasks List */}
        {tasksCompleted > 0 && session.tasksCompleted && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.9 }}
          >
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium">
                  Completed Tasks
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  {session.tasksCompleted.map((taskId, index) => (
                    <motion.li
                      key={taskId}
                      className="flex items-center gap-2 text-sm"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 1 + index * 0.1 }}
                    >
                      <CheckCircle2 className="h-4 w-4 text-green-500" />
                      <span>Task #{taskId}</span>
                    </motion.li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          </motion.div>
        )}

        {/* Motivational Message */}
        <motion.div
          className="text-center p-4 rounded-lg bg-muted/50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.1 }}
        >
          <p className="text-sm text-muted-foreground italic">
            {getMotivationalMessage(focusTimeMinutes, tasksCompleted, streak)}
          </p>
        </motion.div>

        {/* Action Buttons */}
        <motion.div
          className="flex flex-col sm:flex-row gap-3"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.2 }}
        >
          <Button
            variant="default"
            size="lg"
            className="flex-1"
            onClick={onStartNewSession}
          >
            <RotateCcw className="mr-2 h-4 w-4" />
            Start New Session
          </Button>
          <Button
            variant="outline"
            size="lg"
            className="flex-1"
            onClick={onGoHome}
          >
            <Home className="mr-2 h-4 w-4" />
            Go to Dashboard
          </Button>
        </motion.div>

        {/* Share Button */}
        <motion.div
          className="text-center"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.3 }}
        >
          <Button
            variant="ghost"
            size="sm"
            onClick={onShare}
            className="text-muted-foreground hover:text-foreground"
          >
            <Share2 className="mr-2 h-4 w-4" />
            Share your progress
            <ArrowRight className="ml-2 h-4 w-4" />
          </Button>
        </motion.div>
      </div>
    </div>
  );
}

function getMotivationalMessage(minutes: number, tasks: number, streak: number): string {
  if (streak >= 7) {
    return "🏆 A week of consistency! You're building unstoppable momentum!";
  }
  if (tasks >= 5) {
    return "🚀 5+ tasks completed! You're a productivity machine!";
  }
  if (minutes >= 120) {
    return "💪 Over 2 hours of focus! Your dedication is inspiring!";
  }
  if (minutes >= 60) {
    return "⭐ An hour of deep work! That's the path to mastery!";
  }
  if (tasks >= 3) {
    return "✨ Great progress on your tasks! Keep up the momentum!";
  }
  if (minutes >= 25) {
    return "🌟 Solid focus session! Every minute counts!";
  }
  if (streak >= 3) {
    return "🔥 3-day streak! Consistency is the key to success!";
  }
  return "👏 Every session matters! You showed up today!";
}

export default SessionSummary;
