"use client"

/**
 * TutorialCard Component
 * ======================
 * Visar en YouTube-tutorial i ett snyggt kort.
 * Används på Tutorials-sidan, i moduler, studyroom, etc.
 */

import { motion } from "framer-motion"
import { Play, Clock, ExternalLink, Youtube } from "lucide-react"
import { cn } from "@/lib/utils"
import type { Tutorial } from "@/data/tutorials"
import { getYouTubeThumbnail, getYouTubeWatchUrl } from "@/data/tutorials"

interface TutorialCardProps {
    tutorial: Tutorial
    variant?: 'default' | 'compact' | 'horizontal'
    className?: string
}

export function TutorialCard({ tutorial, variant = 'default', className }: TutorialCardProps) {
    const thumbnailUrl = getYouTubeThumbnail(tutorial.youtubeId, 'medium')
    const watchUrl = getYouTubeWatchUrl(tutorial.youtubeId)

    const difficultyColors = {
        beginner: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30',
        intermediate: 'bg-amber-500/20 text-amber-400 border-amber-500/30',
        advanced: 'bg-red-500/20 text-red-400 border-red-500/30'
    }

    const difficultyLabels = {
        beginner: 'Nybörjare',
        intermediate: 'Mellannivå',
        advanced: 'Avancerad'
    }

    if (variant === 'compact') {
        return (
            <motion.a
                href={watchUrl}
                target="_blank"
                rel="noopener noreferrer"
                className={cn(
                    "group flex items-center gap-3 p-3 rounded-xl",
                    "bg-white/[0.02] hover:bg-white/[0.05] border border-white/[0.06]",
                    "transition-all duration-300",
                    className
                )}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                <div className="relative w-16 h-12 rounded-lg overflow-hidden flex-shrink-0">
                    <img
                        src={thumbnailUrl}
                        alt={tutorial.title}
                        className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-black/40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                        <Play className="w-4 h-4 text-white" fill="white" />
                    </div>
                </div>
                <div className="flex-1 min-w-0">
                    <p className="text-sm text-white/90 font-medium truncate">{tutorial.title}</p>
                    <p className="text-xs text-white/50">{tutorial.creator} • {tutorial.duration}</p>
                </div>
                <ExternalLink className="w-4 h-4 text-white/30 group-hover:text-white/60 transition-colors flex-shrink-0" />
            </motion.a>
        )
    }

    if (variant === 'horizontal') {
        return (
            <motion.a
                href={watchUrl}
                target="_blank"
                rel="noopener noreferrer"
                className={cn(
                    "group flex gap-4 p-4 rounded-2xl",
                    "bg-white/[0.02] hover:bg-white/[0.05] border border-white/[0.06]",
                    "transition-all duration-300",
                    className
                )}
                whileHover={{ y: -2 }}
            >
                <div className="relative w-40 h-24 rounded-xl overflow-hidden flex-shrink-0">
                    <img
                        src={thumbnailUrl}
                        alt={tutorial.title}
                        className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
                    <div className="absolute bottom-2 right-2 px-1.5 py-0.5 bg-black/80 rounded text-[10px] text-white font-medium">
                        {tutorial.duration}
                    </div>
                    <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                        <div className="w-10 h-10 rounded-full bg-red-600 flex items-center justify-center">
                            <Play className="w-5 h-5 text-white ml-0.5" fill="white" />
                        </div>
                    </div>
                </div>

                <div className="flex-1 flex flex-col justify-between py-1">
                    <div>
                        <h3 className="text-white/90 font-medium line-clamp-2 group-hover:text-white transition-colors">
                            {tutorial.title}
                        </h3>
                        <p className="text-sm text-white/50 mt-1">{tutorial.creator}</p>
                    </div>
                    <div className="flex items-center gap-2">
                        <span className={cn(
                            "text-xs px-2 py-0.5 rounded-full border",
                            difficultyColors[tutorial.difficulty]
                        )}>
                            {difficultyLabels[tutorial.difficulty]}
                        </span>
                    </div>
                </div>
            </motion.a>
        )
    }

    // Default variant - full card
    return (
        <motion.a
            href={watchUrl}
            target="_blank"
            rel="noopener noreferrer"
            className={cn(
                "group block rounded-2xl overflow-hidden",
                "bg-white/[0.02] hover:bg-white/[0.05] border border-white/[0.06]",
                "transition-all duration-300",
                className
            )}
            whileHover={{ y: -4 }}
        >
            {/* Thumbnail */}
            <div className="relative aspect-video overflow-hidden">
                <img
                    src={thumbnailUrl}
                    alt={tutorial.title}
                    className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent" />

                {/* Duration badge */}
                <div className="absolute bottom-3 right-3 px-2 py-1 bg-black/80 rounded-md text-xs text-white font-medium flex items-center gap-1">
                    <Clock className="w-3 h-3" />
                    {tutorial.duration}
                </div>

                {/* Play button overlay */}
                <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div className="w-16 h-16 rounded-full bg-red-600 flex items-center justify-center shadow-lg shadow-red-600/30">
                        <Play className="w-7 h-7 text-white ml-1" fill="white" />
                    </div>
                </div>

                {/* YouTube badge */}
                <div className="absolute top-3 left-3">
                    <Youtube className="w-6 h-6 text-red-500" />
                </div>
            </div>

            {/* Content */}
            <div className="p-4">
                <h3 className="text-white/90 font-semibold line-clamp-2 group-hover:text-white transition-colors">
                    {tutorial.title}
                </h3>

                <div className="flex items-center gap-2 mt-2 text-sm text-white/50">
                    <span>{tutorial.creator}</span>
                </div>

                <div className="flex items-center gap-2 mt-3">
                    <span className={cn(
                        "text-xs px-2.5 py-1 rounded-full border",
                        difficultyColors[tutorial.difficulty]
                    )}>
                        {difficultyLabels[tutorial.difficulty]}
                    </span>
                    {tutorial.language === 'sv' && (
                        <span className="text-xs px-2 py-1 rounded-full bg-blue-500/20 text-blue-400 border border-blue-500/30">
                            Svenska
                        </span>
                    )}
                </div>

                <p className="text-xs text-white/40 mt-3 line-clamp-2">
                    {tutorial.description}
                </p>
            </div>
        </motion.a>
    )
}
