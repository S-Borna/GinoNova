/**
 * GlassCard Component
 * Phase D.1: Apple-Inspired Glassmorphism Card
 * 
 * Premium glass effect with subtle blur, soft borders,
 * and elegant shadows for a sophisticated look.
 */

import * as React from 'react';
import { cn } from '@/lib/utils';
import { cva, type VariantProps } from 'class-variance-authority';

/* ============================================================================
   GLASS CARD VARIANTS
   ============================================================================ */

const glassCardVariants = cva(
    // Base styles: glassmorphism foundation
    [
        'relative',
        'overflow-hidden',
        'rounded-xl',
        'border',
        'backdrop-blur-xl',
        'transition-all',
        'duration-300',
    ],
    {
        variants: {
            /**
             * Visual intensity variants
             */
            variant: {
                // Default: Subtle glass effect
                default: [
                    'bg-white/80',
                    'border-white/20',
                    'shadow-soft',
                    'dark:bg-neutral-900/80',
                    'dark:border-white/10',
                ],
                // Light: More transparent
                light: [
                    'bg-white/60',
                    'border-white/15',
                    'shadow-sm',
                    'dark:bg-neutral-900/60',
                    'dark:border-white/5',
                ],
                // Solid: Less transparency, more presence
                solid: [
                    'bg-white/95',
                    'border-neutral-200/50',
                    'shadow-md',
                    'dark:bg-neutral-900/95',
                    'dark:border-neutral-700/50',
                ],
                // Primary: Gradient-tinted glass
                primary: [
                    'bg-gradient-to-br',
                    'from-primary-500/10',
                    'to-primary-600/5',
                    'border-primary-200/30',
                    'shadow-soft',
                    'dark:from-primary-500/15',
                    'dark:to-primary-600/10',
                    'dark:border-primary-400/20',
                ],
                // Success: Green-tinted glass
                success: [
                    'bg-gradient-to-br',
                    'from-accent-success/10',
                    'to-accent-success/5',
                    'border-accent-success/20',
                    'shadow-soft',
                ],
                // Warning: Amber-tinted glass
                warning: [
                    'bg-gradient-to-br',
                    'from-accent-warning/10',
                    'to-accent-warning/5',
                    'border-accent-warning/20',
                    'shadow-soft',
                ],
                // Dark: Inverted glass for light backgrounds
                dark: [
                    'bg-neutral-900/80',
                    'border-neutral-700/30',
                    'shadow-xl',
                    'text-white',
                    'dark:bg-white/10',
                    'dark:border-white/20',
                ],
            },

            /**
             * Padding sizes
             */
            padding: {
                none: 'p-0',
                sm: 'p-4',
                md: 'p-6',
                lg: 'p-8',
                xl: 'p-10',
            },

            /**
             * Border radius options
             */
            radius: {
                sm: 'rounded-lg',
                md: 'rounded-xl',
                lg: 'rounded-2xl',
                xl: 'rounded-3xl',
                full: 'rounded-full',
            },

            /**
             * Interactive states
             */
            interactive: {
                true: [
                    'cursor-pointer',
                    'hover:shadow-lg',
                    'hover:border-primary-300/40',
                    'hover:-translate-y-0.5',
                    'active:translate-y-0',
                    'active:shadow-md',
                    'dark:hover:border-primary-400/30',
                ],
                false: '',
            },

            /**
             * Glow effect
             */
            glow: {
                none: '',
                primary: 'shadow-glow-primary',
                success: 'shadow-glow-success',
                warning: 'shadow-glow-warning',
                info: 'shadow-glow-info',
            },
        },
        defaultVariants: {
            variant: 'default',
            padding: 'md',
            radius: 'md',
            interactive: false,
            glow: 'none',
        },
    }
);

/* ============================================================================
   GLASS CARD COMPONENT
   ============================================================================ */

export interface GlassCardProps
    extends React.HTMLAttributes<HTMLDivElement>,
        VariantProps<typeof glassCardVariants> {
    /**
     * Optional shine effect overlay
     */
    shine?: boolean;
    /**
     * Optional gradient border effect
     */
    gradientBorder?: boolean;
    /**
     * Render as a different element (e.g., 'article', 'section')
     */
    as?: React.ElementType;
}

const GlassCard = React.forwardRef<HTMLDivElement, GlassCardProps>(
    (
        {
            className,
            variant,
            padding,
            radius,
            interactive,
            glow,
            shine = false,
            gradientBorder = false,
            as: Component = 'div',
            children,
            ...props
        },
        ref
    ) => {
        return (
            <Component
                ref={ref}
                className={cn(
                    glassCardVariants({
                        variant,
                        padding,
                        radius,
                        interactive,
                        glow,
                    }),
                    gradientBorder && [
                        'before:absolute',
                        'before:inset-0',
                        'before:rounded-inherit',
                        'before:p-[1px]',
                        'before:bg-gradient-to-br',
                        'before:from-white/30',
                        'before:to-transparent',
                        'before:pointer-events-none',
                    ],
                    className
                )}
                {...props}
            >
                {/* Shine overlay effect */}
                {shine && (
                    <div
                        className={cn(
                            'absolute',
                            'inset-0',
                            'pointer-events-none',
                            'bg-gradient-to-br',
                            'from-white/20',
                            'via-transparent',
                            'to-transparent',
                            'opacity-50'
                        )}
                        aria-hidden="true"
                    />
                )}

                {/* Content wrapper */}
                <div className="relative z-10">{children}</div>
            </Component>
        );
    }
);

GlassCard.displayName = 'GlassCard';

/* ============================================================================
   GLASS CARD HEADER
   ============================================================================ */

interface GlassCardHeaderProps extends React.HTMLAttributes<HTMLDivElement> {
    /**
     * Header with border bottom
     */
    bordered?: boolean;
}

const GlassCardHeader = React.forwardRef<HTMLDivElement, GlassCardHeaderProps>(
    ({ className, bordered = false, ...props }, ref) => (
        <div
            ref={ref}
            className={cn(
                'flex',
                'flex-col',
                'space-y-1.5',
                bordered && [
                    'pb-4',
                    'mb-4',
                    'border-b',
                    'border-neutral-200/50',
                    'dark:border-neutral-700/50',
                ],
                className
            )}
            {...props}
        />
    )
);

GlassCardHeader.displayName = 'GlassCardHeader';

/* ============================================================================
   GLASS CARD TITLE
   ============================================================================ */

const GlassCardTitle = React.forwardRef<
    HTMLHeadingElement,
    React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
    <h3
        ref={ref}
        className={cn(
            'text-lg',
            'font-semibold',
            'leading-tight',
            'tracking-tight',
            'text-neutral-900',
            'dark:text-neutral-50',
            className
        )}
        {...props}
    />
));

GlassCardTitle.displayName = 'GlassCardTitle';

/* ============================================================================
   GLASS CARD DESCRIPTION
   ============================================================================ */

const GlassCardDescription = React.forwardRef<
    HTMLParagraphElement,
    React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
    <p
        ref={ref}
        className={cn(
            'text-sm',
            'text-neutral-500',
            'dark:text-neutral-400',
            className
        )}
        {...props}
    />
));

GlassCardDescription.displayName = 'GlassCardDescription';

/* ============================================================================
   GLASS CARD CONTENT
   ============================================================================ */

const GlassCardContent = React.forwardRef<
    HTMLDivElement,
    React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
    <div ref={ref} className={cn('', className)} {...props} />
));

GlassCardContent.displayName = 'GlassCardContent';

/* ============================================================================
   GLASS CARD FOOTER
   ============================================================================ */

interface GlassCardFooterProps extends React.HTMLAttributes<HTMLDivElement> {
    /**
     * Footer with border top
     */
    bordered?: boolean;
}

const GlassCardFooter = React.forwardRef<HTMLDivElement, GlassCardFooterProps>(
    ({ className, bordered = false, ...props }, ref) => (
        <div
            ref={ref}
            className={cn(
                'flex',
                'items-center',
                bordered && [
                    'pt-4',
                    'mt-4',
                    'border-t',
                    'border-neutral-200/50',
                    'dark:border-neutral-700/50',
                ],
                className
            )}
            {...props}
        />
    )
);

GlassCardFooter.displayName = 'GlassCardFooter';

/* ============================================================================
   EXPORTS
   ============================================================================ */

export {
    GlassCard,
    GlassCardHeader,
    GlassCardTitle,
    GlassCardDescription,
    GlassCardContent,
    GlassCardFooter,
    glassCardVariants,
};
