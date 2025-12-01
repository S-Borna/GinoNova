/**
 * ============================================================================
 * LANDING PAGE — Public Home Page
 * ============================================================================
 *
 * The main entry point for DevOpsHub. A premium, high-conversion landing page
 * with smooth animations, beautiful gradients, and compelling copy.
 *
 * Sections:
 * 1. Hero — Bold headline, stats, CTAs
 * 2. Tracks Preview — Four learning tracks
 * 3. Features — Platform capabilities
 * 4. Curriculum Preview — All 15 modules
 * 5. CTA Section — Final conversion push
 * 6. Footer — Navigation and branding
 *
 * @phase A.1 - Landing Page
 */

import {
    Hero,
    TracksPreview,
    Features,
    CurriculumPreview,
    CTASection,
    Footer,
    Navbar,
} from "@/components/landing"

export default function LandingPage() {
    return (
        <div className="relative min-h-screen bg-neutral-950 text-white overflow-x-hidden">
            {/* Navigation */}
            <Navbar />

            {/* Main Content */}
            <main>
                {/* Hero Section */}
                <Hero />

                {/* Learning Tracks */}
                <TracksPreview />

                {/* Platform Features */}
                <Features />

                {/* Full Curriculum */}
                <CurriculumPreview />

                {/* Final CTA */}
                <CTASection />
            </main>

            {/* Footer */}
            <Footer />
        </div>
    )
}
