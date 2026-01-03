"use client"

import * as React from "react"
import { cn } from "@/lib/utils"

interface TabsContextValue {
    value: string
    onValueChange: (value: string) => void
}

const TabsContext = React.createContext<TabsContextValue | undefined>(undefined)

interface TabsProps {
    value: string
    onValueChange: (value: string) => void
    children: React.ReactNode
    className?: string
}

export function Tabs({ value, onValueChange, children, className }: TabsProps) {
    return (
        <TabsContext.Provider value={{ value, onValueChange }}>
            <div className={className}>{children}</div>
        </TabsContext.Provider>
    )
}

function useTabsContext() {
    const context = React.useContext(TabsContext)
    if (!context) {
        throw new Error("Tabs components must be used within Tabs")
    }
    return context
}

export function TabsList({ children, className }: { children: React.ReactNode; className?: string }) {
    return (
        <div className={cn("inline-flex items-center justify-center rounded-lg bg-zinc-900/50 p-1", className)}>
            {children}
        </div>
    )
}

export function TabsTrigger({
    value,
    children,
    className
}: {
    value: string
    children: React.ReactNode
    className?: string
}) {
    const { value: selectedValue, onValueChange } = useTabsContext()
    const isSelected = selectedValue === value

    return (
        <button
            onClick={() => onValueChange(value)}
            className={cn(
                "inline-flex items-center justify-center whitespace-nowrap rounded-md px-3 py-1.5 text-sm font-medium transition-all",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-purple-500",
                isSelected
                    ? "bg-purple-600 text-white shadow-sm"
                    : "text-zinc-400 hover:text-white hover:bg-zinc-800/50",
                className
            )}
        >
            {children}
        </button>
    )
}

export function TabsContent({
    value,
    children,
    className
}: {
    value: string
    children: React.ReactNode
    className?: string
}) {
    const { value: selectedValue } = useTabsContext()
    if (selectedValue !== value) return null

    return <div className={cn("mt-2", className)}>{children}</div>
}

