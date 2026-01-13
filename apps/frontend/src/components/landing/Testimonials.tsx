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
        name: "Erik Andersson",
        role: "Junior DevOps Engineer",
        company: "Spotify",
        avatar: null, // Will use initials
        content: "DevOpsHub förändrade min karriär. Det strukturerade läroplanen tog mig från noll kunskap om CI/CD till att deploya Kubernetes-kluster i produktion på 4 månader. Dallas AI-assistenten var ovärderlig!",
        rating: 5,
        highlight: "Från noll till produktion på 4 månader",
    },
    {
        id: "t2",
        name: "Lisa Bergström",
        role: "Cloud Engineer",
        company: "Klarna",
        avatar: null,
        content: "Hands-on labs är det som skiljer denna plattform från andra. Varje koncept backas upp av riktig infrastruktur du faktiskt bygger. Mina Terraform-kunskaper gick från nybörjare till avancerad nivå.",
        rating: 5,
        highlight: "Bästa hands-on labs jag upplevt",
    },
    {
        id: "t3",
        name: "Johan Svensson",
        role: "SRE Lead",
        company: "King",
        avatar: null,
        content: "Jag rekommenderar DevOpsHub till alla i mitt team. SRE-modulen täcker observability-praktiker som tog mig år att lära mig i produktion. Och det är helt gratis — otroligt!",
        rating: 5,
        highlight: "Teamets första val för utbildning",
    },
    {
        id: "t4",
        name: "Sofia Karlsson",
        role: "DevOps Consultant",
        company: "TietoEVRY",
        avatar: null,
        content: "Jag har provat Udemy, Coursera och Pluralsight. DevOpsHub slår dem alla — och det är gratis! AI-personaliseringen och Dallas-assistenten är spelförändrare.",
        rating: 5,
        highlight: "Bättre än betalda alternativ",
    },
    {
        id: "t5",
        name: "Marcus Lindqvist",
        role: "Platform Engineer",
        company: "Ericsson",
        avatar: null,
        content: "Kubernetes-modulen är fenomenal. Gick från att inte veta vad en pod är till att hantera multi-cluster deployments. Portföljprojekten hjälpte mig få mitt drömjobb!",
        rating: 5,
        highlight: "Fick drömjobbet tack vare kursen",
    },
    {
        id: "t6",
        name: "Anna Johansson",
        role: "Site Reliability Engineer",
        company: "iZettle",
        avatar: null,
        content: "Att lära sig DevOps har aldrig varit enklare. Lärstigarna är perfekt strukturerade, och communityn är fantastisk. Gick från junior till senior på 18 månader.",
        rating: 5,
        highlight: "Junior till Senior på 18 månader",
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
                    "bg-gradient-to-br from-[#0d0d14]/90 to-[#0a0a0f]/90",
                    "border border-white/[0.08]",
                    "hover:border-pink-500/30 hover:from-[#0d0d14] hover:to-[#0a0a0f]",
                    "transition-all duration-500"
                )}
            >
                {/* Quote icon */}
                <div className="absolute top-4 right-4 opacity-10">
                    <Quote className="w-10 h-10 text-pink-400" />
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
                    <div className="inline-block px-3 py-1.5 mb-4 text-xs font-semibold text-pink-300 bg-pink-500/15 rounded-full border border-pink-500/30">
                        {testimonial.highlight}
                    </div>

                    {/* Quote */}
                    <blockquote className="text-zinc-300 leading-relaxed mb-6 text-sm">
                        &ldquo;{testimonial.content}&rdquo;
                    </blockquote>

                    {/* Author */}
                    <div className="flex items-center gap-3 pt-4 border-t border-white/[0.08]">
                        {/* Avatar */}
                        <div className="w-12 h-12 rounded-full bg-gradient-to-br from-pink-500 to-purple-600 flex items-center justify-center text-white text-sm font-bold shadow-lg shadow-pink-500/30">
                            {initials}
                        </div>

                        <div>
                            <div className="text-white font-semibold">
                                {testimonial.name}
                            </div>
                            <div className="text-xs text-zinc-500">
                                {testimonial.role}
                            </div>
                            <div className="text-xs text-zinc-600">
                                {testimonial.company}
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
        <section className="relative py-32 bg-[#05050a] overflow-hidden">
            {/* Background elements */}
            <div className="absolute inset-0">
                {/* Base gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#0a0a12] to-[#05050a]" />

                {/* Gradient orbs */}
                <div className="absolute top-1/4 left-1/4 w-[600px] h-[400px]" style={{ background: "radial-gradient(ellipse, rgba(139,92,246,0.06) 0%, transparent 60%)", filter: "blur(80px)" }} />
                <div className="absolute bottom-1/4 right-1/4 w-[600px] h-[400px]" style={{ background: "radial-gradient(ellipse, rgba(236,72,153,0.06) 0%, transparent 60%)", filter: "blur(80px)" }} />

                {/* Grid pattern */}
                <div className="absolute inset-0 opacity-[0.015]" style={{ backgroundImage: "linear-gradient(rgba(255,255,255,0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.3) 1px, transparent 1px)", backgroundSize: "60px 60px" }} />

                {/* Top separator */}
                <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-pink-500/30 to-transparent" />
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
                    <span className="inline-flex items-center gap-2 px-5 py-2 mb-6 text-sm font-semibold tracking-wide uppercase text-pink-300 bg-pink-500/15 rounded-full border border-pink-500/30">
                        <Star className="w-4 h-4 fill-pink-400 text-pink-400" />
                        Framgångshistorier
                    </span>
                    <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6">
                        Gå med Tusentals{" "}
                        <span className="bg-gradient-to-r from-yellow-400 via-orange-400 to-pink-400 bg-clip-text text-transparent" style={{ filter: "drop-shadow(0 0 25px rgba(251,191,36,0.4))" }}>
                            Nöjda DevOps-Ingenjörer
                        </span>
                    </h2>
                    <p className="text-lg sm:text-xl text-zinc-400 max-w-3xl mx-auto leading-relaxed">
                        Ingenjörer över hela Sverige har accelererat sina karriärer med DevOpsHub.{" "}
                        <span className="text-white font-medium">Här är vad de säger.</span>
                    </p>
                </motion.div>

                {/* Testimonial cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
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
                                className="w-6 h-6 fill-yellow-500 text-yellow-500"
                            />
                        ))}
                        <span className="text-2xl font-black text-white ml-3">5.0</span>
                    </div>
                    <p className="text-zinc-400 text-base">
                        Betrodd av <span className="text-white font-bold">10,000+</span> ingenjörer i Sverige
                    </p>
                </motion.div>
            </div>
        </section>
    )
}

export default Testimonials
