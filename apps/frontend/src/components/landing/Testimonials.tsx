"use client"

/**
 * ============================================================================
 * TESTIMONIALS SECTION — Social Proof
 * ============================================================================
 *
 * Design: Elegant carousel with gradient cards and floating avatars.
 * Ready for future testimonial data integration.
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Quote, Star } from "lucide-react"

/* ============================================================================
   TESTIMONIAL DATA (Placeholder for future real testimonials)
   ============================================================================ */

const TESTIMONIALS = [
    {
        id: "t1",
        name: "Alex Chen",
        role: "Junior DevOps Engineer",
        company: "TechStartup Inc.",
        avatar: null, // Will use initials
        content: "DevOpsHub transformed my career. The structured curriculum took me from knowing nothing about CI/CD to deploying production Kubernetes clusters in 4 months.",
        rating: 5,
        highlight: "From zero to production in 4 months",
    },
    {
        id: "t2",
        name: "Sarah Mitchell",
        role: "Cloud Engineer",
        company: "Enterprise Solutions",
        avatar: null,
        content: "The hands-on labs are what set this apart. Every concept is backed by real infrastructure you can actually build. My Terraform skills went from beginner to advanced.",
        rating: 5,
        highlight: "Best hands-on labs I've experienced",
    },
    {
        id: "t3",
        name: "Marcus Johnson",
        role: "SRE Lead",
        company: "ScaleUp Corp",
        avatar: null,
        content: "I recommend DevOpsHub to everyone on my team. The SRE module alone covers observability practices that took me years to learn in production.",
        rating: 5,
        highlight: "Team training resource of choice",
    },
]

/* ============================================================================
   TESTIMONIAL CARD COMPONENT
   ============================================================================ */

interface TestimonialCardProps {
    testimonial: typeof TESTIMONIALS[0]
    index: number
}

function TestimonialCard({ testimonial, index }: TestimonialCardProps) {
    const initials = testimonial.name
        .split(" ")
        .map((n) => n[0])
        .join("")

    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{ duration: 0.6, delay: index * 0.15 }}
            className="group relative"
        >
            <div
                className={cn(
                    "relative p-6 rounded-2xl h-full",
                    "bg-gradient-to-br from-white/[0.05] to-white/[0.02]",
                    "border border-white/[0.08]",
                    "hover:border-white/[0.15] hover:from-white/[0.08] hover:to-white/[0.03]",
                    "transition-all duration-500"
                )}
            >
                {/* Quote icon */}
                <div className="absolute top-4 right-4 opacity-20">
                    <Quote className="w-8 h-8 text-primary-400" />
                </div>

                {/* Content */}
                <div className="relative z-10">
                    {/* Rating */}
                    <div className="flex gap-1 mb-4">
                        {Array.from({ length: testimonial.rating }).map((_, i) => (
                            <Star
                                key={i}
                                className="w-4 h-4 fill-yellow-500 text-yellow-500"
                            />
                        ))}
                    </div>

                    {/* Highlight */}
                    <div className="inline-block px-3 py-1 mb-4 text-xs font-medium text-primary-400 bg-primary-500/10 rounded-full">
                        &ldquo;{testimonial.highlight}&rdquo;
                    </div>

                    {/* Quote */}
                    <blockquote className="text-neutral-300 leading-relaxed mb-6">
                        &ldquo;{testimonial.content}&rdquo;
                    </blockquote>

                    {/* Author */}
                    <div className="flex items-center gap-3 pt-4 border-t border-white/[0.08]">
                        {/* Avatar */}
                        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-primary-500 to-purple-600 flex items-center justify-center text-white text-sm font-semibold">
                            {initials}
                        </div>

                        <div>
                            <div className="text-white font-medium">
                                {testimonial.name}
                            </div>
                            <div className="text-sm text-neutral-500">
                                {testimonial.role} · {testimonial.company}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function Testimonials() {
    return (
        <section className="relative py-24 bg-neutral-950 overflow-hidden">
            {/* Background elements */}
            <div className="absolute inset-0">
                {/* Gradient orbs */}
                <div className="absolute top-1/4 left-1/4 w-[400px] h-[400px] bg-primary-500/5 rounded-full blur-[120px]" />
                <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-purple-500/5 rounded-full blur-[120px]" />
            </div>

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-16"
                >
                    <span className="inline-block px-4 py-1.5 mb-4 text-xs font-semibold tracking-wider uppercase text-primary-400 bg-primary-500/10 rounded-full">
                        Success Stories
                    </span>
                    <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
                        Join Thousands of{" "}
                        <span className="bg-gradient-to-r from-yellow-400 to-orange-400 bg-clip-text text-transparent">
                            DevOps Engineers
                        </span>
                    </h2>
                    <p className="text-lg text-neutral-400 max-w-2xl mx-auto">
                        Engineers around the world have accelerated their careers with DevOpsHub.
                        Here&apos;s what they have to say.
                    </p>
                </motion.div>

                {/* Testimonial cards */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    {TESTIMONIALS.map((testimonial, index) => (
                        <TestimonialCard
                            key={testimonial.id}
                            testimonial={testimonial}
                            index={index}
                        />
                    ))}
                </div>

                {/* Trust indicators */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="mt-16 flex flex-col items-center"
                >
                    <div className="flex items-center gap-2 mb-4">
                        {Array.from({ length: 5 }).map((_, i) => (
                            <Star
                                key={i}
                                className="w-5 h-5 fill-yellow-500 text-yellow-500"
                            />
                        ))}
                        <span className="text-white font-semibold ml-2">5.0</span>
                    </div>
                    <p className="text-neutral-400 text-sm">
                        Trusted by <span className="text-white">2,000+</span> engineers worldwide
                    </p>
                </motion.div>
            </div>
        </section>
    )
}

export default Testimonials
