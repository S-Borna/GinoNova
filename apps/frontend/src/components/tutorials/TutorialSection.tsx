"use client"

/**
 * TutorialSection Component
 * =========================
 * Återanvändbar sektion för att visa tutorials.
 * Kan användas på moduler, studyroom, dashboard, etc.
 */

import { useState } from "react"
import { motion } from "framer-motion"
import { Youtube, ChevronRight, Sparkles } from "lucide-react"
import { cn } from "@/lib/utils"
import Link from "next/link"
import { TutorialCard } from "./TutorialCard"
import type { Tutorial } from "@/data/tutorials"

interface TutorialSectionProps {
  title?: string
  subtitle?: string
  tutorials: Tutorial[]
  variant?: 'default' | 'compact' | 'horizontal'
  maxItems?: number
  showViewAll?: boolean
  viewAllHref?: string
  className?: string
}

export function TutorialSection({
  title = "📺 Rekommenderade Tutorials",
  subtitle,
  tutorials,
  variant = 'default',
  maxItems = 3,
  showViewAll = true,
  viewAllHref = "/tutorials",
  className
}: TutorialSectionProps) {
  const displayedTutorials = tutorials.slice(0, maxItems)

  if (tutorials.length === 0) return null

  return (
    <div className={cn("space-y-4", className)}>
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-red-500/10 flex items-center justify-center">
            <Youtube className="w-5 h-5 text-red-500" />
          </div>
          <div>
            <h3 className="text-lg font-semibold text-white/90">{title}</h3>
            {subtitle && (
              <p className="text-sm text-white/50">{subtitle}</p>
            )}
          </div>
        </div>
        
        {showViewAll && tutorials.length > maxItems && (
          <Link
            href={viewAllHref}
            className="flex items-center gap-1 text-sm text-purple-400 hover:text-purple-300 transition-colors"
          >
            <span>Visa alla</span>
            <ChevronRight className="w-4 h-4" />
          </Link>
        )}
      </div>

      {/* Tutorial Grid/List */}
      <div className={cn(
        variant === 'compact' ? 'space-y-2' :
        variant === 'horizontal' ? 'space-y-3' :
        'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'
      )}>
        {displayedTutorials.map((tutorial, index) => (
          <motion.div
            key={tutorial.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
          >
            <TutorialCard tutorial={tutorial} variant={variant} />
          </motion.div>
        ))}
      </div>

      {/* View all link for compact variant */}
      {showViewAll && variant === 'compact' && tutorials.length > maxItems && (
        <Link
          href={viewAllHref}
          className="flex items-center justify-center gap-2 p-3 rounded-xl bg-white/[0.02] hover:bg-white/[0.05] border border-white/[0.06] text-white/60 hover:text-white/80 transition-all"
        >
          <Sparkles className="w-4 h-4" />
          <span className="text-sm">Se fler tutorials</span>
        </Link>
      )}
    </div>
  )
}

/**
 * Quick Tutorial Widget
 * =====================
 * Minimal widget för sidebar/dashboard
 */
export function TutorialWidget({
  tutorials,
  title = "Lär dig mer",
  className
}: {
  tutorials: Tutorial[]
  title?: string
  className?: string
}) {
  if (tutorials.length === 0) return null

  return (
    <div className={cn(
      "p-4 rounded-2xl bg-white/[0.02] border border-white/[0.06]",
      className
    )}>
      <div className="flex items-center gap-2 mb-3">
        <Youtube className="w-4 h-4 text-red-500" />
        <span className="text-sm font-medium text-white/80">{title}</span>
      </div>
      
      <div className="space-y-2">
        {tutorials.slice(0, 3).map((tutorial) => (
          <TutorialCard 
            key={tutorial.id} 
            tutorial={tutorial} 
            variant="compact" 
          />
        ))}
      </div>
      
      <Link
        href="/tutorials"
        className="flex items-center justify-center gap-1 mt-3 text-xs text-purple-400 hover:text-purple-300 transition-colors"
      >
        <span>Alla tutorials</span>
        <ChevronRight className="w-3 h-3" />
      </Link>
    </div>
  )
}
