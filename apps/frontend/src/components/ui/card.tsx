import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & {
    variant?: "default" | "glass" | "bordered" | "elevated"
    hover?: boolean
  }
>(({ className, variant = "default", hover = false, ...props }, ref) => {
  const variantClasses = {
    default: "bg-card border shadow-sm",
    glass: "bg-white/80 dark:bg-gray-900/80 backdrop-blur-md border border-white/20 dark:border-gray-700/50",
    bordered: "bg-card border-2",
    elevated: "bg-card shadow-lg border-0",
  }

  return (
    <div
      ref={ref}
      className={cn(
        "rounded-xl text-card-foreground transition-all duration-200",
        variantClasses[variant],
        hover && "hover:shadow-md hover:-translate-y-0.5 cursor-pointer",
        className
      )}
      {...props}
    />
  )
})
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & {
    as?: "h1" | "h2" | "h3" | "h4" | "h5" | "h6" | "div"
  }
>(({ className, as: Component = "div", ...props }, ref) => (
  <Component
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
