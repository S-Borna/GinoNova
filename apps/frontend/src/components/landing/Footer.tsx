"use client"

/**
 * ============================================================================
 * FOOTER — Site Footer with Navigation and Branding
 * ============================================================================
 *
 * Design: Clean, organized footer with logo, nav links, and social.
 * Subtle gradient top border for visual separation.
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    Terminal,
    Github,
    Twitter,
    Linkedin,
    Mail,
    Heart,
} from "lucide-react"

/* ============================================================================
   NAVIGATION DATA
   ============================================================================ */

const NAV_SECTIONS = [
    {
        title: "Learning",
        links: [
            { label: "Modules", href: "/modules" },
            { label: "Learning Tracks", href: "/modules#tracks" },
            { label: "Labs & Projects", href: "/modules#labs" },
            { label: "Studyflow", href: "/studyflow" },
        ],
    },
    {
        title: "Resources",
        links: [
            { label: "Documentation", href: "/docs" },
            { label: "API Reference", href: "/api-docs" },
            { label: "Community", href: "/community" },
            { label: "Blog", href: "/blog" },
        ],
    },
    {
        title: "Platform",
        links: [
            { label: "Dashboard", href: "/dashboard" },
            { label: "Progress", href: "/progress" },
            { label: "Certificates", href: "/certificates" },
            { label: "Settings", href: "/settings" },
        ],
    },
    {
        title: "Company",
        links: [
            { label: "About", href: "/about" },
            { label: "Contact", href: "/contact" },
            { label: "Privacy", href: "/privacy" },
            { label: "Terms", href: "/terms" },
        ],
    },
]

const SOCIAL_LINKS = [
    { icon: Github, href: "https://github.com", label: "GitHub" },
    { icon: Twitter, href: "https://twitter.com", label: "Twitter" },
    { icon: Linkedin, href: "https://linkedin.com", label: "LinkedIn" },
    { icon: Mail, href: "mailto:hello@devopshub.io", label: "Email" },
]

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function Footer() {
    const currentYear = new Date().getFullYear()

    return (
        <footer className="relative bg-neutral-950">
            {/* Gradient top border */}
            <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Main footer content */}
                <div className="py-16 grid grid-cols-2 md:grid-cols-6 gap-8 lg:gap-12">
                    {/* Brand column */}
                    <div className="col-span-2">
                        {/* Logo */}
                        <Link href="/" className="inline-flex items-center gap-2 mb-4">
                            <div className="p-2 rounded-lg bg-gradient-to-br from-primary-500 to-purple-600">
                                <Terminal className="w-5 h-5 text-white" />
                            </div>
                            <span className="text-xl font-bold text-white">
                                My DOE Hub
                            </span>
                        </Link>

                        <p className="text-neutral-400 text-sm leading-relaxed mb-6 max-w-xs">
                            The most comprehensive DevOps learning platform.
                            Master modern infrastructure, from Linux to Kubernetes.
                            A project by Ebadi.
                        </p>

                        {/* Social links */}
                        <div className="flex items-center gap-3">
                            {SOCIAL_LINKS.map((social) => {
                                const Icon = social.icon
                                return (
                                    <a
                                        key={social.label}
                                        href={social.href}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className={cn(
                                            "p-2 rounded-lg",
                                            "bg-white/5 text-neutral-400",
                                            "hover:bg-white/10 hover:text-white",
                                            "transition-all duration-200"
                                        )}
                                        aria-label={social.label}
                                    >
                                        <Icon className="w-4 h-4" />
                                    </a>
                                )
                            })}
                        </div>
                    </div>

                    {/* Navigation columns */}
                    {NAV_SECTIONS.map((section) => (
                        <div key={section.title}>
                            <h4 className="text-sm font-semibold text-white mb-4">
                                {section.title}
                            </h4>
                            <ul className="space-y-3">
                                {section.links.map((link) => (
                                    <li key={link.href}>
                                        <Link
                                            href={link.href}
                                            className="text-sm text-neutral-400 hover:text-white transition-colors duration-200"
                                        >
                                            {link.label}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>

                {/* Bottom bar */}
                <div className="py-6 border-t border-white/[0.06] flex flex-col sm:flex-row items-center justify-between gap-4">
                    <p className="text-sm text-neutral-500">
                        © {currentYear} Ebadi. All rights reserved.
                    </p>

                    <p className="text-sm text-neutral-500 flex items-center gap-1">
                        Built with{" "}
                        <Heart className="w-3.5 h-3.5 text-red-500 fill-red-500" />{" "}
                        for DevOps engineers
                    </p>
                </div>
            </div>
        </footer>
    )
}

export default Footer
