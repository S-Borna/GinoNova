"use client"

/**
 * ============================================================================
 * TUTORIALS PAGE — Curated DevOps Video Tutorials
 * ============================================================================
 *
 * Samlad sida med alla kvalitets-tutorials från betrodda creators:
 * - NetworkChuck
 * - TechWorld with Nana  
 * - Learn Linux TV
 * - freeCodeCamp
 * - Fireship
 * - tutoriaLinux
 *
 * @phase YOUTUBE-INTEGRATION
 */

import { useState, useMemo } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
  Youtube, 
  Search, 
  Filter,
  BookOpen,
  Terminal,
  Container,
  Network,
  GitBranch,
  Server,
  Shield,
  Clock,
  Sparkles,
  X
} from "lucide-react"
import { CosmicAurora } from "@/components/ui/cosmic-aurora"
import { TutorialCard } from "@/components/tutorials/TutorialCard"
import { TUTORIALS, TRUSTED_CREATORS, type Tutorial } from "@/data/tutorials"

// ============================================================================
// TOPIC FILTERS
// ============================================================================

const TOPIC_FILTERS = [
  { id: 'all', label: 'Alla', icon: Sparkles, color: 'purple' },
  { id: 'linux', label: 'Linux', icon: Terminal, color: 'amber' },
  { id: 'docker', label: 'Docker', icon: Container, color: 'blue' },
  { id: 'kubernetes', label: 'Kubernetes', icon: Server, color: 'cyan' },
  { id: 'git', label: 'Git', icon: GitBranch, color: 'orange' },
  { id: 'networking', label: 'Nätverk', icon: Network, color: 'emerald' },
  { id: 'bash', label: 'Bash', icon: Terminal, color: 'green' },
  { id: 'ssh', label: 'SSH', icon: Shield, color: 'red' },
  { id: 'cicd', label: 'CI/CD', icon: Server, color: 'pink' },
] as const

const DIFFICULTY_FILTERS = [
  { id: 'all', label: 'Alla nivåer' },
  { id: 'beginner', label: 'Nybörjare' },
  { id: 'intermediate', label: 'Mellannivå' },
  { id: 'advanced', label: 'Avancerad' },
] as const

// ============================================================================
// MAIN PAGE
// ============================================================================

export default function TutorialsPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [activeTopic, setActiveTopic] = useState('all')
  const [activeDifficulty, setActiveDifficulty] = useState('all')

  // Filter tutorials
  const filteredTutorials = useMemo(() => {
    return TUTORIALS.filter(tutorial => {
      // Search filter
      if (searchQuery) {
        const query = searchQuery.toLowerCase()
        const matchesSearch = 
          tutorial.title.toLowerCase().includes(query) ||
          tutorial.creator.toLowerCase().includes(query) ||
          tutorial.topics.some(t => t.includes(query)) ||
          tutorial.description.toLowerCase().includes(query)
        if (!matchesSearch) return false
      }

      // Topic filter
      if (activeTopic !== 'all') {
        const matchesTopic = tutorial.topics.some(t => 
          t.includes(activeTopic) || activeTopic.includes(t)
        )
        if (!matchesTopic) return false
      }

      // Difficulty filter
      if (activeDifficulty !== 'all') {
        if (tutorial.difficulty !== activeDifficulty) return false
      }

      return true
    })
  }, [searchQuery, activeTopic, activeDifficulty])

  // Group by topic for display
  const quickVideos = filteredTutorials.filter(t => {
    const duration = t.duration.split(':')
    const minutes = duration.length === 3 ? parseInt(duration[0]) * 60 + parseInt(duration[1]) : parseInt(duration[0])
    return minutes <= 10
  })

  const fullCourses = filteredTutorials.filter(t => {
    const duration = t.duration.split(':')
    const minutes = duration.length === 3 ? parseInt(duration[0]) * 60 + parseInt(duration[1]) : parseInt(duration[0])
    return minutes > 60
  })

  return (
    <div className="relative min-h-screen bg-[#05050a]">
      <CosmicAurora />
      
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <div className="flex items-center gap-4 mb-4">
            <div className="w-14 h-14 rounded-2xl bg-red-500/20 flex items-center justify-center">
              <Youtube className="w-7 h-7 text-red-500" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-white">Video Tutorials</h1>
              <p className="text-white/60">Curerade tutorials från betrodda DevOps-creators</p>
            </div>
          </div>

          {/* Trusted Creators */}
          <div className="flex flex-wrap items-center gap-2 mt-4">
            <span className="text-xs text-white/40">Betrodda sources:</span>
            {TRUSTED_CREATORS.slice(0, 5).map((creator) => (
              <span 
                key={creator.name}
                className="text-xs px-2 py-1 rounded-full bg-white/[0.05] text-white/60 border border-white/[0.08]"
              >
                {creator.name}
              </span>
            ))}
          </div>
        </motion.div>

        {/* Search & Filters */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="mb-8 space-y-4"
        >
          {/* Search */}
          <div className="relative">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-white/40" />
            <input
              type="text"
              placeholder="Sök tutorials..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className={cn(
                "w-full pl-12 pr-4 py-3 rounded-xl",
                "bg-white/[0.03] border border-white/[0.08]",
                "text-white placeholder-white/40",
                "focus:outline-none focus:border-purple-500/50 focus:bg-white/[0.05]",
                "transition-all duration-200"
              )}
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-4 top-1/2 -translate-y-1/2 text-white/40 hover:text-white/60"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Topic Filters */}
          <div className="flex flex-wrap gap-2">
            {TOPIC_FILTERS.map((topic) => {
              const Icon = topic.icon
              const isActive = activeTopic === topic.id
              return (
                <button
                  key={topic.id}
                  onClick={() => setActiveTopic(topic.id)}
                  className={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium",
                    "border transition-all duration-200",
                    isActive
                      ? "bg-purple-500/20 border-purple-500/50 text-purple-400"
                      : "bg-white/[0.02] border-white/[0.08] text-white/60 hover:bg-white/[0.05] hover:text-white/80"
                  )}
                >
                  <Icon className="w-4 h-4" />
                  {topic.label}
                </button>
              )
            })}
          </div>

          {/* Difficulty Filters */}
          <div className="flex gap-2">
            {DIFFICULTY_FILTERS.map((diff) => {
              const isActive = activeDifficulty === diff.id
              return (
                <button
                  key={diff.id}
                  onClick={() => setActiveDifficulty(diff.id)}
                  className={cn(
                    "px-3 py-1.5 rounded-lg text-xs font-medium",
                    "border transition-all duration-200",
                    isActive
                      ? "bg-white/10 border-white/20 text-white"
                      : "bg-white/[0.02] border-white/[0.06] text-white/50 hover:text-white/70"
                  )}
                >
                  {diff.label}
                </button>
              )
            })}
          </div>
        </motion.div>

        {/* Results Count */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mb-6"
        >
          <p className="text-sm text-white/50">
            {filteredTutorials.length} {filteredTutorials.length === 1 ? 'tutorial' : 'tutorials'} hittade
          </p>
        </motion.div>

        {/* Quick Videos Section */}
        {quickVideos.length > 0 && (activeTopic === 'all' || !searchQuery) && (
          <motion.section
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="mb-12"
          >
            <div className="flex items-center gap-3 mb-4">
              <Clock className="w-5 h-5 text-emerald-400" />
              <h2 className="text-xl font-semibold text-white">Snabba videos (under 10 min)</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {quickVideos.slice(0, 8).map((tutorial, index) => (
                <motion.div
                  key={tutorial.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 + index * 0.05 }}
                >
                  <TutorialCard tutorial={tutorial} />
                </motion.div>
              ))}
            </div>
          </motion.section>
        )}

        {/* Full Courses Section */}
        {fullCourses.length > 0 && (activeTopic === 'all' || !searchQuery) && (
          <motion.section
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mb-12"
          >
            <div className="flex items-center gap-3 mb-4">
              <BookOpen className="w-5 h-5 text-purple-400" />
              <h2 className="text-xl font-semibold text-white">Kompletta kurser (1h+)</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {fullCourses.map((tutorial, index) => (
                <motion.div
                  key={tutorial.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 + index * 0.05 }}
                >
                  <TutorialCard tutorial={tutorial} />
                </motion.div>
              ))}
            </div>
          </motion.section>
        )}

        {/* All Tutorials (when filtered) */}
        {(searchQuery || activeTopic !== 'all') && (
          <motion.section
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {filteredTutorials.map((tutorial, index) => (
                <motion.div
                  key={tutorial.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                >
                  <TutorialCard tutorial={tutorial} />
                </motion.div>
              ))}
            </div>
          </motion.section>
        )}

        {/* Empty State */}
        {filteredTutorials.length === 0 && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="flex flex-col items-center justify-center py-20"
          >
            <div className="w-20 h-20 rounded-full bg-white/[0.03] flex items-center justify-center mb-4">
              <Search className="w-8 h-8 text-white/30" />
            </div>
            <h3 className="text-xl font-semibold text-white/70 mb-2">Inga tutorials hittades</h3>
            <p className="text-white/50 text-center max-w-md">
              Prova att ändra dina filter eller sök efter något annat.
            </p>
            <button
              onClick={() => {
                setSearchQuery('')
                setActiveTopic('all')
                setActiveDifficulty('all')
              }}
              className="mt-4 px-4 py-2 rounded-lg bg-purple-500/20 text-purple-400 hover:bg-purple-500/30 transition-colors"
            >
              Återställ filter
            </button>
          </motion.div>
        )}
      </div>
    </div>
  )
}
