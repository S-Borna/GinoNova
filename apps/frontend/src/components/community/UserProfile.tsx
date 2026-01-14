"use client"

/**
 * ============================================================================
 * USER PROFILE CARD — Community Member Profile
 * ============================================================================
 *
 * Displays user profile with stats, badges, and recent activity
 */

import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { type UserProfile } from "@/lib/community-types"
import { getReputationLevel, BADGES } from "@/lib/reputation"
import { ReputationBadge } from "./ReputationBadge"
import {
    Calendar,
    MessageSquare,
    ThumbsUp,
    CheckCircle,
    Award,
    Github,
    Linkedin,
    Twitter,
    Globe,
    TrendingUp,
    Flame,
} from "lucide-react"
import Link from "next/link"
import { Button } from "@/components/ui/button"

interface UserProfileProps {
    profile: UserProfile
    variant?: "card" | "full"
    className?: string
}

export function UserProfile({
    profile,
    variant = "card",
    className,
}: UserProfileProps) {
    const level = getReputationLevel(profile.reputation)

    if (variant === "card") {
        return (
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "p-6 rounded-2xl",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border border-zinc-800/80",
                    "hover:border-purple-500/30 transition-all duration-300",
                    className
                )}
                style={{
                    boxShadow: "0 0 30px rgba(0, 0, 0, 0.5)",
                }}
            >
                {/* Profile Header */}
                <div className="flex items-start gap-4 mb-4">
                    <div
                        className={cn(
                            "w-16 h-16 rounded-2xl shrink-0",
                            "bg-gradient-to-br",
                            level.gradient,
                            "flex items-center justify-center",
                            "text-2xl font-bold text-white",
                            "border-2 border-white/10"
                        )}
                        style={{
                            boxShadow: `0 0 30px ${level.glowColor}`,
                        }}
                    >
                        {profile.avatar || profile.name.substring(0, 2).toUpperCase()}
                    </div>

                    <div className="flex-1 min-w-0">
                        <h3 className="text-xl font-bold text-white mb-1 truncate">
                            {profile.name}
                        </h3>
                        <p className="text-sm text-zinc-500 mb-2">@{profile.username}</p>
                        <ReputationBadge reputation={profile.reputation} size="sm" />
                    </div>
                </div>

                {/* Bio */}
                {profile.bio && (
                    <p className="text-sm text-zinc-400 mb-4 line-clamp-2">
                        {profile.bio}
                    </p>
                )}

                {/* Stats */}
                <div className="grid grid-cols-2 gap-3 mb-4">
                    <StatItem
                        icon={MessageSquare}
                        label="Posts"
                        value={profile.stats.postsCreated}
                    />
                    <StatItem
                        icon={ThumbsUp}
                        label="Upvotes"
                        value={profile.stats.upvotesReceived}
                    />
                    <StatItem
                        icon={CheckCircle}
                        label="Best Answers"
                        value={profile.stats.bestAnswers}
                    />
                    <StatItem
                        icon={Flame}
                        label="Day Streak"
                        value={profile.stats.learningStreak}
                    />
                </div>

                {/* Badges */}
                {profile.badges.length > 0 && (
                    <div>
                        <p className="text-xs text-zinc-500 mb-2 flex items-center gap-1">
                            <Award className="w-3 h-3" />
                            Badges ({profile.badges.length})
                        </p>
                        <div className="flex flex-wrap gap-2">
                            {profile.badges.slice(0, 6).map((badgeId) => {
                                const badge = BADGES.find((b) => b.id === badgeId)
                                if (!badge) return null
                                return (
                                    <motion.div
                                        key={badgeId}
                                        whileHover={{ scale: 1.1 }}
                                        className={cn(
                                            "w-8 h-8 rounded-lg",
                                            "flex items-center justify-center text-lg",
                                            "bg-zinc-800/50 border border-zinc-700/50",
                                            "hover:border-purple-500/50 transition-colors"
                                        )}
                                        title={badge.name}
                                    >
                                        {badge.icon}
                                    </motion.div>
                                )
                            })}
                        </div>
                    </div>
                )}
            </motion.div>
        )
    }

    // Full profile view
    return (
        <div className={cn("space-y-6", className)}>
            {/* Banner */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "relative h-48 rounded-3xl overflow-hidden",
                    "bg-gradient-to-br",
                    level.gradient
                )}
                style={{
                    boxShadow: `0 0 60px ${level.glowColor}`,
                }}
            >
                <div className="absolute inset-0 bg-black/20" />
                <div className="absolute bottom-6 left-6">
                    <div
                        className={cn(
                            "w-24 h-24 rounded-2xl",
                            "bg-gradient-to-br",
                            level.gradient,
                            "flex items-center justify-center",
                            "text-3xl font-bold text-white",
                            "border-4 border-white/20"
                        )}
                    >
                        {profile.avatar || profile.name.substring(0, 2).toUpperCase()}
                    </div>
                </div>
            </motion.div>

            {/* Profile Info */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
                className={cn(
                    "p-8 rounded-3xl",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border border-zinc-800/80"
                )}
            >
                <div className="flex flex-col md:flex-row md:items-start justify-between gap-6 mb-6">
                    <div className="flex-1">
                        <h1 className="text-3xl font-black text-white mb-2">
                            {profile.name}
                        </h1>
                        <p className="text-zinc-500 mb-3">@{profile.username}</p>
                        <ReputationBadge
                            reputation={profile.reputation}
                            size="lg"
                            showProgress
                        />
                    </div>

                    <div className="flex gap-2">
                        <Button variant="outline" className="rounded-xl">
                            <MessageSquare className="w-4 h-4 mr-2" />
                            Message
                        </Button>
                        <Button className="rounded-xl bg-purple-600 hover:bg-purple-500">
                            Follow
                        </Button>
                    </div>
                </div>

                {profile.bio && (
                    <p className="text-zinc-300 mb-6">{profile.bio}</p>
                )}

                {/* Social Links */}
                {profile.socialLinks && (
                    <div className="flex gap-2 mb-6">
                        {profile.socialLinks.github && (
                            <Link
                                href={profile.socialLinks.github}
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    className="rounded-lg"
                                >
                                    <Github className="w-4 h-4" />
                                </Button>
                            </Link>
                        )}
                        {profile.socialLinks.linkedin && (
                            <Link
                                href={profile.socialLinks.linkedin}
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    className="rounded-lg"
                                >
                                    <Linkedin className="w-4 h-4" />
                                </Button>
                            </Link>
                        )}
                        {profile.socialLinks.twitter && (
                            <Link
                                href={profile.socialLinks.twitter}
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    className="rounded-lg"
                                >
                                    <Twitter className="w-4 h-4" />
                                </Button>
                            </Link>
                        )}
                        {profile.socialLinks.website && (
                            <Link
                                href={profile.socialLinks.website}
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    className="rounded-lg"
                                >
                                    <Globe className="w-4 h-4" />
                                </Button>
                            </Link>
                        )}
                    </div>
                )}

                {/* Stats Grid */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    <StatCard
                        icon={MessageSquare}
                        label="Posts Created"
                        value={profile.stats.postsCreated}
                        gradient="from-blue-500 to-cyan-600"
                    />
                    <StatCard
                        icon={ThumbsUp}
                        label="Upvotes Received"
                        value={profile.stats.upvotesReceived}
                        gradient="from-emerald-500 to-teal-600"
                    />
                    <StatCard
                        icon={CheckCircle}
                        label="Best Answers"
                        value={profile.stats.bestAnswers}
                        gradient="from-purple-500 to-violet-600"
                    />
                    <StatCard
                        icon={Flame}
                        label="Learning Streak"
                        value={`${profile.stats.learningStreak} days`}
                        gradient="from-orange-500 to-red-600"
                    />
                </div>

                {/* Member Info */}
                <div className="flex flex-wrap gap-4 text-sm text-zinc-500 pt-6 border-t border-zinc-800">
                    <span className="flex items-center gap-1">
                        <Calendar className="w-4 h-4" />
                        Joined {new Date(profile.joinDate).toLocaleDateString()}
                    </span>
                    <span className="flex items-center gap-1">
                        <TrendingUp className="w-4 h-4" />
                        {profile.reputation} reputation
                    </span>
                </div>
            </motion.div>

            {/* Badges */}
            {profile.badges.length > 0 && (
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.2 }}
                    className={cn(
                        "p-8 rounded-3xl",
                        "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                        "border border-zinc-800/80"
                    )}
                >
                    <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-2">
                        <Award className="w-5 h-5 text-amber-400" />
                        Badges & Achievements
                    </h2>
                    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                        {profile.badges.map((badgeId) => {
                            const badge = BADGES.find((b) => b.id === badgeId)
                            if (!badge) return null
                            return (
                                <motion.div
                                    key={badgeId}
                                    whileHover={{ scale: 1.05, y: -4 }}
                                    className={cn(
                                        "p-4 rounded-xl",
                                        "bg-zinc-900/50 border border-zinc-800",
                                        "hover:border-purple-500/50 transition-all duration-300",
                                        "text-center"
                                    )}
                                >
                                    <div className="text-4xl mb-2">{badge.icon}</div>
                                    <h3
                                        className={cn(
                                            "font-semibold mb-1",
                                            badge.color
                                        )}
                                    >
                                        {badge.name}
                                    </h3>
                                    <p className="text-xs text-zinc-500">
                                        {badge.description}
                                    </p>
                                </motion.div>
                            )
                        })}
                    </div>
                </motion.div>
            )}
        </div>
    )
}

function StatItem({
    icon: Icon,
    label,
    value,
}: {
    icon: any
    label: string
    value: number
}) {
    return (
        <div className="flex items-center gap-2">
            <Icon className="w-4 h-4 text-purple-400 shrink-0" />
            <div className="flex-1 min-w-0">
                <p className="text-lg font-bold text-white">{value}</p>
                <p className="text-xs text-zinc-500 truncate">{label}</p>
            </div>
        </div>
    )
}

function StatCard({
    icon: Icon,
    label,
    value,
    gradient,
}: {
    icon: any
    label: string
    value: number | string
    gradient: string
}) {
    return (
        <div
            className={cn(
                "p-4 rounded-xl",
                "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                "border border-zinc-800/80"
            )}
        >
            <div
                className={cn(
                    "w-10 h-10 rounded-lg mb-3",
                    "bg-gradient-to-br",
                    gradient,
                    "flex items-center justify-center"
                )}
            >
                <Icon className="w-5 h-5 text-white" />
            </div>
            <p className="text-2xl font-bold text-white mb-1">{value}</p>
            <p className="text-xs text-zinc-500">{label}</p>
        </div>
    )
}
