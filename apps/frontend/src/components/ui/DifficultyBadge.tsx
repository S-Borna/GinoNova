/**
 * ============================================================================
 * DIFFICULTY BADGE COMPONENT
 * ============================================================================
 *
 * Beautiful badge displaying module difficulty with:
 * - Glow effect matching color tier
 * - Hover animation
 * - Tooltip with description
 * - Size variants (small, medium, large)
 */

"use client"

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { DifficultyLevel, getDifficultyConfig, normalizeDifficulty } from "@/lib/difficulty-config"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

export interface DifficultyBadgeProps {
  difficulty: DifficultyLevel | string
  size?: 'small' | 'medium' | 'large'
  showLabel?: boolean
  showIcon?: boolean
  showTooltip?: boolean
  className?: string
  animated?: boolean
}

const sizeClasses = {
  small: {
    container: 'px-2.5 py-1 text-xs gap-1.5',
    icon: 'text-sm',
    label: 'text-xs font-semibold',
  },
  medium: {
    container: 'px-3 py-1.5 text-sm gap-2',
    icon: 'text-base',
    label: 'text-sm font-bold',
  },
  large: {
    container: 'px-4 py-2 text-base gap-2.5',
    icon: 'text-xl',
    label: 'text-base font-bold',
  },
}

export function DifficultyBadge({
  difficulty,
  size = 'medium',
  showLabel = true,
  showIcon = true,
  showTooltip = true,
  className,
  animated = true,
}: DifficultyBadgeProps) {
  const normalizedLevel = normalizeDifficulty(typeof difficulty === 'string' ? difficulty : difficulty)
  const config = getDifficultyConfig(normalizedLevel)
  const sizeClass = sizeClasses[size]

  const badge = (
    <motion.div
      className={cn(
        "inline-flex items-center rounded-full font-medium transition-all duration-300",
        "border backdrop-blur-sm",
        sizeClass.container,
        className
      )}
      style={{
        backgroundColor: config.color.bg,
        borderColor: config.color.border,
        color: config.color.text,
      }}
      whileHover={animated ? {
        scale: 1.05,
        boxShadow: `0 0 20px ${config.color.glow}`,
      } : undefined}
      whileTap={animated ? { scale: 0.95 } : undefined}
      transition={{ type: "spring", stiffness: 400, damping: 17 }}
    >
      {showIcon && (
        <span className={sizeClass.icon} role="img" aria-label={config.label}>
          {config.icon}
        </span>
      )}
      {showLabel && (
        <span className={sizeClass.label}>
          {config.label}
        </span>
      )}
    </motion.div>
  )

  if (!showTooltip) {
    return badge
  }

  return (
    <TooltipProvider>
      <Tooltip delayDuration={300}>
        <TooltipTrigger asChild>
          {badge}
        </TooltipTrigger>
        <TooltipContent
          side="top"
          className="bg-zinc-900 border-zinc-700 max-w-xs"
        >
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-xl">{config.icon}</span>
              <span className="font-bold text-white">{config.label} Level</span>
            </div>
            <p className="text-sm text-zinc-300">{config.description}</p>
            <div className="pt-2 border-t border-zinc-700 space-y-1">
              <p className="text-xs text-zinc-400">
                <span className="font-semibold text-zinc-300">Prerequisites:</span>{' '}
                {config.prerequisites}
              </p>
              <p className="text-xs text-zinc-400">
                <span className="font-semibold text-zinc-300">Duration:</span>{' '}
                ~{config.estimatedMonths} months
              </p>
              <p className="text-xs text-zinc-400">
                <span className="font-semibold text-zinc-300">Career:</span>{' '}
                {config.careerLevel}
              </p>
            </div>
          </div>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  )
}

/**
 * Compact variant - just icon with tooltip
 */
export function DifficultyIcon({
  difficulty,
  size = 'medium',
  showTooltip = true,
}: Pick<DifficultyBadgeProps, 'difficulty' | 'size' | 'showTooltip'>) {
  return (
    <DifficultyBadge
      difficulty={difficulty}
      size={size}
      showLabel={false}
      showIcon={true}
      showTooltip={showTooltip}
    />
  )
}

/**
 * List of all difficulty badges (for filters)
 */
export function DifficultyList({
  selected,
  onSelect,
  size = 'medium',
}: {
  selected?: DifficultyLevel
  onSelect?: (level: DifficultyLevel) => void
  size?: 'small' | 'medium' | 'large'
}) {
  const levels: DifficultyLevel[] = ['rookie', 'junior', 'senior']

  return (
    <div className="flex flex-wrap gap-2">
      {levels.map((level) => {
        const config = getDifficultyConfig(level)
        const isSelected = selected === level

        return (
          <motion.button
            key={level}
            onClick={() => onSelect?.(level)}
            className={cn(
              "inline-flex items-center rounded-full font-medium transition-all duration-300",
              "border backdrop-blur-sm cursor-pointer",
              sizeClasses[size].container,
              isSelected && "ring-2 ring-offset-2 ring-offset-zinc-950"
            )}
            style={{
              backgroundColor: isSelected ? config.color.bg : 'rgba(0, 0, 0, 0.2)',
              borderColor: isSelected ? config.color.border : 'rgba(255, 255, 255, 0.1)',
              color: isSelected ? config.color.text : '#71717a',
              ringColor: config.color.glow,
            }}
            whileHover={{
              scale: 1.05,
              backgroundColor: config.color.bg,
              borderColor: config.color.border,
              color: config.color.text,
            }}
            whileTap={{ scale: 0.95 }}
          >
            <span className={sizeClasses[size].icon}>{config.icon}</span>
            <span className={sizeClasses[size].label}>{config.label}</span>
          </motion.button>
        )
      })}
    </div>
  )
}
