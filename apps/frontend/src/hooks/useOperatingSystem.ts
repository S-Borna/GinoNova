"use client"

/**
 * ============================================================================
 * USE OPERATING SYSTEM HOOK
 * ============================================================================
 *
 * Manages user's operating system and Linux distro preference for DevOps content.
 * Stored in localStorage for persistence across sessions.
 *
 * Supports:
 * - macOS (Homebrew-based instructions)
 * - Windows (WSL2 + PowerShell/winget/choco instructions)
 * - Linux with distro selection:
 *   - Ubuntu (RECOMMENDED - most compatible with all tasks)
 *   - Debian
 *   - Fedora
 *   - Arch
 *   - CentOS/RHEL
 *
 * @phase FAS-3.1 - OS-Adaptive Content System
 */

import { useState, useEffect, useCallback } from "react"

// Operating System types
export type OperatingSystem = "macos" | "windows" | "linux" | null

// Linux distribution types
export type LinuxDistro = 
    | "ubuntu"      // RECOMMENDED - Best for beginners, most tutorials
    | "debian"      // Stable, similar to Ubuntu
    | "fedora"      // Cutting edge, Red Hat family
    | "arch"        // Advanced users, rolling release
    | "centos"      // Enterprise, RHEL-compatible
    | null

// Combined platform configuration
export interface PlatformConfig {
    os: OperatingSystem
    distro: LinuxDistro
}

// Storage keys
const OS_STORAGE_KEY = "devopshub-os-preference"
const DISTRO_STORAGE_KEY = "devopshub-distro-preference"

// Distro metadata for UI
export const LINUX_DISTROS = {
    ubuntu: {
        name: "Ubuntu",
        version: "24.04 LTS",
        icon: "🟠",
        packageManager: "apt",
        recommended: true,
        description: "Mest populär och bäst dokumenterad. Rekommenderas för alla.",
    },
    debian: {
        name: "Debian",
        version: "12 Bookworm",
        icon: "🔴",
        packageManager: "apt",
        recommended: false,
        description: "Stabil och pålitlig. Liknande Ubuntu men konservativare.",
    },
    fedora: {
        name: "Fedora",
        version: "40",
        icon: "🔵",
        packageManager: "dnf",
        recommended: false,
        description: "Senaste teknologin. Bra för Red Hat/RHEL-karriär.",
    },
    arch: {
        name: "Arch Linux",
        version: "Rolling",
        icon: "🟢",
        packageManager: "pacman",
        recommended: false,
        description: "För avancerade användare. DIY-approach.",
    },
    centos: {
        name: "CentOS Stream / RHEL",
        version: "9",
        icon: "🟣",
        packageManager: "dnf",
        recommended: false,
        description: "Enterprise-fokuserat. Vanligt i produktion.",
    },
} as const

// OS metadata for UI
export const OS_OPTIONS = {
    macos: {
        name: "macOS",
        icon: "🍎",
        description: "Apple Silicon (M1/M2/M3) eller Intel Mac",
        packageManager: "Homebrew",
    },
    windows: {
        name: "Windows",
        icon: "🪟",
        description: "Windows 10/11 med WSL2",
        packageManager: "winget / Chocolatey",
    },
    linux: {
        name: "Linux",
        icon: "🐧",
        description: "Välj din distribution i nästa steg",
        packageManager: "Varies",
    },
} as const

interface UsePlatformReturn {
    os: OperatingSystem
    distro: LinuxDistro
    platform: PlatformConfig
    setOS: (os: OperatingSystem) => void
    setDistro: (distro: LinuxDistro) => void
    setPlatform: (config: PlatformConfig) => void
    hasSelected: boolean
    needsDistro: boolean
    isLoading: boolean
    clearSelection: () => void
    getPackageManager: () => string
    platformLabel: string
}

export function usePlatform(): UsePlatformReturn {
    const [os, setOSState] = useState<OperatingSystem>(null)
    const [distro, setDistroState] = useState<LinuxDistro>(null)
    const [isLoading, setIsLoading] = useState(true)

    // Load from localStorage on mount
    useEffect(() => {
        try {
            const storedOS = localStorage.getItem(OS_STORAGE_KEY)
            const storedDistro = localStorage.getItem(DISTRO_STORAGE_KEY)
            
            if (storedOS === "macos" || storedOS === "windows" || storedOS === "linux") {
                setOSState(storedOS)
            }
            
            if (storedDistro && ["ubuntu", "debian", "fedora", "arch", "centos"].includes(storedDistro)) {
                setDistroState(storedDistro as LinuxDistro)
            }
        } catch (error) {
            console.error("Failed to load platform preference:", error)
        } finally {
            setIsLoading(false)
        }
    }, [])

    const setOS = useCallback((newOS: OperatingSystem) => {
        try {
            if (newOS) {
                localStorage.setItem(OS_STORAGE_KEY, newOS)
                // Clear distro if not Linux
                if (newOS !== "linux") {
                    localStorage.removeItem(DISTRO_STORAGE_KEY)
                    setDistroState(null)
                }
            } else {
                localStorage.removeItem(OS_STORAGE_KEY)
                localStorage.removeItem(DISTRO_STORAGE_KEY)
                setDistroState(null)
            }
            setOSState(newOS)
        } catch (error) {
            console.error("Failed to save OS preference:", error)
        }
    }, [])

    const setDistro = useCallback((newDistro: LinuxDistro) => {
        try {
            if (newDistro) {
                localStorage.setItem(DISTRO_STORAGE_KEY, newDistro)
            } else {
                localStorage.removeItem(DISTRO_STORAGE_KEY)
            }
            setDistroState(newDistro)
        } catch (error) {
            console.error("Failed to save distro preference:", error)
        }
    }, [])

    const setPlatform = useCallback((config: PlatformConfig) => {
        setOS(config.os)
        if (config.os === "linux" && config.distro) {
            setDistro(config.distro)
        }
    }, [setOS, setDistro])

    const clearSelection = useCallback(() => {
        try {
            localStorage.removeItem(OS_STORAGE_KEY)
            localStorage.removeItem(DISTRO_STORAGE_KEY)
            setOSState(null)
            setDistroState(null)
        } catch (error) {
            console.error("Failed to clear platform preference:", error)
        }
    }, [])

    const getPackageManager = useCallback(() => {
        if (os === "macos") return "brew"
        if (os === "windows") return "winget"
        if (os === "linux" && distro) {
            return LINUX_DISTROS[distro].packageManager
        }
        return "apt" // Default
    }, [os, distro])

    // Generate human-readable platform label
    const platformLabel = (() => {
        if (!os) return "Ej vald"
        if (os === "macos") return "macOS"
        if (os === "windows") return "Windows (WSL2)"
        if (os === "linux" && distro) {
            return `Linux (${LINUX_DISTROS[distro].name})`
        }
        return "Linux"
    })()

    return {
        os,
        distro,
        platform: { os, distro },
        setOS,
        setDistro,
        setPlatform,
        hasSelected: os !== null && (os !== "linux" || distro !== null),
        needsDistro: os === "linux" && distro === null,
        isLoading,
        clearSelection,
        getPackageManager,
        platformLabel,
    }
}

// Legacy hook for backwards compatibility
export function useOperatingSystem() {
    const platform = usePlatform()
    return {
        os: platform.os,
        setOS: platform.setOS,
        hasSelected: platform.hasSelected,
        isLoading: platform.isLoading,
        clearSelection: platform.clearSelection,
    }
}

/**
 * ============================================================================
 * CONTENT FILTERING HELPERS
 * ============================================================================
 */

/**
 * Get OS-specific content from a task using HTML comment tags
 * 
 * Supported tags:
 * <!-- OS:macos --> ... <!-- /OS:macos -->
 * <!-- OS:windows --> ... <!-- /OS:windows -->
 * <!-- OS:linux --> ... <!-- /OS:linux -->
 * <!-- DISTRO:ubuntu --> ... <!-- /DISTRO:ubuntu -->
 * <!-- DISTRO:fedora --> ... <!-- /DISTRO:fedora -->
 * <!-- DISTRO:arch --> ... <!-- /DISTRO:arch -->
 * <!-- DISTRO:debian --> ... <!-- /DISTRO:debian -->
 * <!-- DISTRO:centos --> ... <!-- /DISTRO:centos -->
 */
export function filterContentByPlatform(
    content: string,
    os: OperatingSystem,
    distro: LinuxDistro
): string {
    if (!content) return content

    let result = content

    // Define all OS and distro regexes
    const osRegexes = {
        macos: /<!-- OS:macos -->([\s\S]*?)<!-- \/OS:macos -->/g,
        windows: /<!-- OS:windows -->([\s\S]*?)<!-- \/OS:windows -->/g,
        linux: /<!-- OS:linux -->([\s\S]*?)<!-- \/OS:linux -->/g,
    }

    const distroRegexes = {
        ubuntu: /<!-- DISTRO:ubuntu -->([\s\S]*?)<!-- \/DISTRO:ubuntu -->/g,
        debian: /<!-- DISTRO:debian -->([\s\S]*?)<!-- \/DISTRO:debian -->/g,
        fedora: /<!-- DISTRO:fedora -->([\s\S]*?)<!-- \/DISTRO:fedora -->/g,
        arch: /<!-- DISTRO:arch -->([\s\S]*?)<!-- \/DISTRO:arch -->/g,
        centos: /<!-- DISTRO:centos -->([\s\S]*?)<!-- \/DISTRO:centos -->/g,
    }

    // Filter OS-specific content
    for (const [osKey, regex] of Object.entries(osRegexes)) {
        if (os === osKey) {
            // Keep this OS content, remove tags
            result = result
                .replace(new RegExp(`<!-- OS:${osKey} -->`, 'g'), '')
                .replace(new RegExp(`<!-- /OS:${osKey} -->`, 'g'), '')
        } else {
            // Remove this OS content entirely
            result = result.replace(regex, '')
        }
    }

    // Filter distro-specific content (only if Linux)
    if (os === "linux") {
        for (const [distroKey, regex] of Object.entries(distroRegexes)) {
            if (distro === distroKey) {
                // Keep this distro content, remove tags
                result = result
                    .replace(new RegExp(`<!-- DISTRO:${distroKey} -->`, 'g'), '')
                    .replace(new RegExp(`<!-- /DISTRO:${distroKey} -->`, 'g'), '')
            } else {
                // Remove this distro content entirely
                result = result.replace(regex, '')
            }
        }
    } else {
        // Not Linux - remove all distro tags
        for (const regex of Object.values(distroRegexes)) {
            result = result.replace(regex, '')
        }
    }

    // Clean up any leftover empty lines
    result = result.replace(/\n{3,}/g, '\n\n')

    return result.trim()
}

/**
 * Get installation command based on platform
 */
export function getInstallCommand(
    packageName: string,
    os: OperatingSystem,
    distro: LinuxDistro
): string {
    if (os === "macos") {
        return `brew install ${packageName}`
    }
    
    if (os === "windows") {
        return `winget install ${packageName}`
    }
    
    if (os === "linux") {
        switch (distro) {
            case "ubuntu":
            case "debian":
                return `sudo apt install -y ${packageName}`
            case "fedora":
            case "centos":
                return `sudo dnf install -y ${packageName}`
            case "arch":
                return `sudo pacman -S ${packageName}`
            default:
                return `sudo apt install -y ${packageName}` // Default to apt
        }
    }
    
    return `# Install ${packageName} using your package manager`
}
