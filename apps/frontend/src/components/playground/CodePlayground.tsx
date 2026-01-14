"use client"

/**
 * ============================================================================
 * CODE PLAYGROUND COMPONENT
 * ============================================================================
 *
 * Interactive code playground for DevOps practice:
 * - Multiple environments (Bash, Python, Docker, Kubernetes, Terraform)
 * - Monaco Editor integration (VS Code editor)
 * - Split view: Editor + Terminal output
 * - Syntax highlighting & validation
 * - Save/Load from localStorage
 * - Share functionality
 * - Sample snippets library
 *
 * @phase PLAYGROUND
 */

import { useState, useEffect, useRef, useCallback } from 'react'
import { cn } from '@/lib/utils'
import { motion, AnimatePresence } from 'framer-motion'
import dynamic from 'next/dynamic'
import {
    Play,
    RotateCcw,
    Save,
    Share2,
    Code2,
    Terminal as TerminalIcon,
    Loader2,
    Check,
    X,
    ChevronDown,
    BookOpen,
    Zap,
    Settings,
    Download,
    Copy,
    FileCode,
    Sparkles,
} from 'lucide-react'
import {
    executeCode,
    validateKubernetesYAML,
    validateTerraformHCL,
    sampleSnippets,
    type EnvironmentType,
    type SimulationResult,
} from '@/lib/playground/simulators'
import { Button } from '@/components/ui/button'

// Dynamically import Monaco Editor to avoid SSR issues
const Editor = dynamic(() => import('@monaco-editor/react'), {
    ssr: false,
    loading: () => (
        <div className="flex items-center justify-center h-full bg-[#1e1e1e]">
            <Loader2 className="w-8 h-8 animate-spin text-purple-500" />
        </div>
    ),
})

/* ============================================================================
   TYPES
   ============================================================================ */

export interface CodePlaygroundProps {
    defaultEnvironment?: EnvironmentType
    defaultCode?: string
    initialCode?: string
    showEnvironmentSelector?: boolean
    showSnippets?: boolean
    showSaveLoad?: boolean
    showShare?: boolean
    height?: string
    onRun?: (code: string, result: SimulationResult) => void
    onComplete?: () => void
    readOnly?: boolean
    hiddenControls?: string[]
}

interface OutputEntry {
    type: 'stdout' | 'stderr' | 'info' | 'success' | 'error'
    content: string
    timestamp: number
}

/* ============================================================================
   ENVIRONMENT CONFIGURATIONS
   ============================================================================ */

const environmentConfig = {
    bash: {
        name: 'Bash Terminal',
        icon: TerminalIcon,
        language: 'shell',
        color: 'emerald',
        description: 'Practice Linux shell commands',
    },
    python: {
        name: 'Python',
        icon: FileCode,
        language: 'python',
        color: 'blue',
        description: 'Execute Python scripts in-browser',
    },
    docker: {
        name: 'Docker',
        icon: Code2,
        language: 'shell',
        color: 'cyan',
        description: 'Simulate Docker commands',
    },
    kubernetes: {
        name: 'Kubernetes',
        icon: Settings,
        language: 'yaml',
        color: 'purple',
        description: 'Validate Kubernetes YAML',
    },
    terraform: {
        name: 'Terraform',
        icon: Sparkles,
        language: 'hcl',
        color: 'violet',
        description: 'Validate Terraform HCL',
    },
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function CodePlayground({
    defaultEnvironment = 'bash',
    defaultCode = '',
    initialCode = '',
    showEnvironmentSelector = true,
    showSnippets = true,
    showSaveLoad = true,
    showShare = true,
    height = '600px',
    onRun,
    onComplete,
    readOnly = false,
    hiddenControls = [],
}: CodePlaygroundProps) {
    const [environment, setEnvironment] = useState<EnvironmentType>(defaultEnvironment)
    const [code, setCode] = useState(initialCode || defaultCode || sampleSnippets[defaultEnvironment]['Hello World'] || '')
    const [output, setOutput] = useState<OutputEntry[]>([])
    const [isRunning, setIsRunning] = useState(false)
    const [pyodideReady, setPyodideReady] = useState(false)
    const [showSnippetsPanel, setShowSnippetsPanel] = useState(false)
    const [showSettingsPanel, setShowSettingsPanel] = useState(false)
    const [fontSize, setFontSize] = useState(14)
    const [splitRatio, setSplitRatio] = useState(50)

    const pyodideRef = useRef<any>(null)
    const editorRef = useRef<any>(null)
    const outputRef = useRef<HTMLDivElement>(null)

    // Load Pyodide for Python execution
    useEffect(() => {
        if (environment === 'python' && !pyodideReady) {
            loadPyodide()
        }
    }, [environment])

    const loadPyodide = async () => {
        try {
            // Load Pyodide script dynamically
            if (!(window as any).loadPyodide) {
                const script = document.createElement('script')
                script.src = 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js'
                script.async = true
                await new Promise((resolve, reject) => {
                    script.onload = resolve
                    script.onerror = reject
                    document.head.appendChild(script)
                })
            }
            
            pyodideRef.current = await (window as any).loadPyodide({
                indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/',
            })
            setPyodideReady(true)
            addOutput({
                type: 'info',
                content: '✓ Python runtime loaded successfully',
                timestamp: Date.now(),
            })
        } catch (error) {
            addOutput({
                type: 'error',
                content: `Failed to load Python runtime: ${error instanceof Error ? error.message : 'Unknown error'}`,
                timestamp: Date.now(),
            })
        }
    }

    const addOutput = (entry: OutputEntry) => {
        setOutput(prev => [...prev, entry])
        // Auto-scroll to bottom
        setTimeout(() => {
            if (outputRef.current) {
                outputRef.current.scrollTop = outputRef.current.scrollHeight
            }
        }, 10)
    }

    // Execute code based on environment
    const handleRun = async () => {
        if (!code.trim()) {
            addOutput({
                type: 'error',
                content: 'No code to execute',
                timestamp: Date.now(),
            })
            return
        }

        setIsRunning(true)
        addOutput({
            type: 'info',
            content: `▶ Executing ${environmentConfig[environment].name}...`,
            timestamp: Date.now(),
        })

        try {
            let result: SimulationResult

            if (environment === 'python') {
                result = await executePython(code)
            } else {
                result = executeCode(code, environment)
            }

            // Handle output
            if (result.output === '__CLEAR__') {
                setOutput([])
            } else {
                if (result.output) {
                    addOutput({
                        type: result.exitCode === 0 ? 'stdout' : 'stderr',
                        content: result.output,
                        timestamp: Date.now(),
                    })
                }

                if (result.error) {
                    addOutput({
                        type: 'error',
                        content: result.error,
                        timestamp: Date.now(),
                    })
                }

                if (result.exitCode === 0 && result.output && !result.error) {
                    addOutput({
                        type: 'success',
                        content: `✓ Execution completed successfully (exit code: ${result.exitCode})`,
                        timestamp: Date.now(),
                    })
                } else if (result.exitCode !== 0) {
                    addOutput({
                        type: 'error',
                        content: `✗ Execution failed (exit code: ${result.exitCode})`,
                        timestamp: Date.now(),
                    })
                }
            }

            onRun?.(code, result)

        } catch (error) {
            addOutput({
                type: 'error',
                content: `Execution error: ${error instanceof Error ? error.message : 'Unknown error'}`,
                timestamp: Date.now(),
            })
        } finally {
            setIsRunning(false)
        }
    }

    // Execute Python code using Pyodide
    const executePython = async (code: string): Promise<SimulationResult> => {
        if (!pyodideReady || !pyodideRef.current) {
            return {
                output: '',
                error: 'Python runtime not loaded yet. Please wait...',
                exitCode: 1,
            }
        }

        try {
            // Capture stdout
            await pyodideRef.current.runPythonAsync(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
            `)

            // Run the code
            await pyodideRef.current.runPythonAsync(code)

            // Get output
            const stdout = await pyodideRef.current.runPythonAsync('sys.stdout.getvalue()')
            const stderr = await pyodideRef.current.runPythonAsync('sys.stderr.getvalue()')

            return {
                output: stdout || '',
                error: stderr || undefined,
                exitCode: stderr ? 1 : 0,
            }
        } catch (error) {
            return {
                output: '',
                error: error instanceof Error ? error.message : 'Python execution error',
                exitCode: 1,
            }
        }
    }

    // Reset playground
    const handleReset = () => {
        setCode(sampleSnippets[environment]['Hello World'] || '')
        setOutput([])
    }

    // Save to localStorage
    const handleSave = () => {
        const data = {
            environment,
            code,
            timestamp: Date.now(),
        }
        localStorage.setItem('devops-playground-save', JSON.stringify(data))
        addOutput({
            type: 'success',
            content: '✓ Code saved to browser storage',
            timestamp: Date.now(),
        })
    }

    // Load from localStorage
    const handleLoad = () => {
        const saved = localStorage.getItem('devops-playground-save')
        if (saved) {
            try {
                const data = JSON.parse(saved)
                setEnvironment(data.environment)
                setCode(data.code)
                addOutput({
                    type: 'success',
                    content: `✓ Code loaded from ${new Date(data.timestamp).toLocaleString()}`,
                    timestamp: Date.now(),
                })
            } catch (error) {
                addOutput({
                    type: 'error',
                    content: 'Failed to load saved code',
                    timestamp: Date.now(),
                })
            }
        } else {
            addOutput({
                type: 'info',
                content: 'No saved code found',
                timestamp: Date.now(),
            })
        }
    }

    // Share code (generate shareable link)
    const handleShare = async () => {
        const shareData = {
            environment,
            code,
        }
        const encoded = btoa(JSON.stringify(shareData))
        const url = `${window.location.origin}/playground?shared=${encoded}`

        try {
            await navigator.clipboard.writeText(url)
            addOutput({
                type: 'success',
                content: '✓ Share link copied to clipboard!',
                timestamp: Date.now(),
            })
        } catch (error) {
            addOutput({
                type: 'info',
                content: `Share link: ${url}`,
                timestamp: Date.now(),
            })
        }
    }

    // Handle environment change
    const handleEnvironmentChange = (newEnv: EnvironmentType) => {
        setEnvironment(newEnv)
        setCode(sampleSnippets[newEnv]['Hello World'] || '')
        setOutput([])
    }

    // Load snippet
    const loadSnippet = (snippetName: string) => {
        const snippet = sampleSnippets[environment][snippetName]
        if (snippet) {
            setCode(snippet)
            setShowSnippetsPanel(false)
            addOutput({
                type: 'info',
                content: `✓ Loaded snippet: ${snippetName}`,
                timestamp: Date.now(),
            })
        }
    }

    // Handle keyboard shortcuts
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
                e.preventDefault()
                handleRun()
            } else if ((e.metaKey || e.ctrlKey) && e.key === 's') {
                e.preventDefault()
                handleSave()
            }
        }

        window.addEventListener('keydown', handleKeyDown)
        return () => window.removeEventListener('keydown', handleKeyDown)
    }, [code, environment])

    // Load shared code from URL
    useEffect(() => {
        const params = new URLSearchParams(window.location.search)
        const shared = params.get('shared')
        if (shared) {
            try {
                const data = JSON.parse(atob(shared))
                setEnvironment(data.environment)
                setCode(data.code)
            } catch (error) {
                console.error('Failed to load shared code:', error)
            }
        }
    }, [])

    const config = environmentConfig[environment]

    return (
        <div className={cn(
            "relative rounded-2xl overflow-hidden",
            "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
            "border border-purple-500/20",
            "shadow-[0_0_80px_rgba(139,92,246,0.15)]"
        )}>
            {/* Cosmic glow effects */}
            <div className="absolute top-0 right-0 w-[300px] h-[300px] bg-purple-500/5 rounded-full blur-[100px] pointer-events-none" />
            <div className="absolute bottom-0 left-0 w-[250px] h-[250px] bg-cyan-500/5 rounded-full blur-[80px] pointer-events-none" />

            {/* Header */}
            <div className="relative z-10 flex flex-wrap items-center justify-between gap-4 p-4 border-b border-purple-500/20 bg-black/20 backdrop-blur-sm">
                {/* Environment Selector */}
                {showEnvironmentSelector && (
                    <div className="flex items-center gap-2">
                        {Object.entries(environmentConfig).map(([key, cfg]) => {
                            const Icon = cfg.icon
                            const isActive = environment === key
                            return (
                                <motion.button
                                    key={key}
                                    onClick={() => handleEnvironmentChange(key as EnvironmentType)}
                                    className={cn(
                                        "flex items-center gap-2 px-3 py-2 rounded-lg",
                                        "transition-all duration-200",
                                        isActive
                                            ? "bg-purple-600/30 border border-purple-500/50 text-white"
                                            : "bg-zinc-800/50 border border-zinc-700/50 text-zinc-400 hover:text-white hover:bg-zinc-700/50"
                                    )}
                                    whileHover={{ scale: 1.05 }}
                                    whileTap={{ scale: 0.95 }}
                                >
                                    <Icon className="w-4 h-4" />
                                    <span className="text-sm font-medium">{cfg.name}</span>
                                </motion.button>
                            )
                        })}
                    </div>
                )}

                {/* Controls */}
                <div className="flex items-center gap-2">
                    {/* Run Button */}
                    {!hiddenControls.includes('run') && (
                        <Button
                            onClick={handleRun}
                            disabled={isRunning || (environment === 'python' && !pyodideReady)}
                            className={cn(
                                "bg-gradient-to-r from-emerald-600 to-emerald-700",
                                "hover:from-emerald-500 hover:to-emerald-600",
                                "text-white font-semibold",
                                "shadow-[0_0_20px_rgba(16,185,129,0.3)]"
                            )}
                        >
                            {isRunning ? (
                                <>
                                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                                    Running...
                                </>
                            ) : (
                                <>
                                    <Play className="w-4 h-4 mr-2" />
                                    Run
                                </>
                            )}
                        </Button>
                    )}

                    {/* Snippets */}
                    {showSnippets && !hiddenControls.includes('snippets') && (
                        <Button
                            onClick={() => setShowSnippetsPanel(!showSnippetsPanel)}
                            variant="outline"
                            className="border-zinc-700"
                        >
                            <BookOpen className="w-4 h-4 mr-2" />
                            Snippets
                        </Button>
                    )}

                    {/* Reset */}
                    {!hiddenControls.includes('reset') && (
                        <Button
                            onClick={handleReset}
                            variant="outline"
                            className="border-zinc-700"
                        >
                            <RotateCcw className="w-4 h-4" />
                        </Button>
                    )}

                    {/* Save */}
                    {showSaveLoad && !hiddenControls.includes('save') && (
                        <>
                            <Button
                                onClick={handleSave}
                                variant="outline"
                                className="border-zinc-700"
                            >
                                <Save className="w-4 h-4" />
                            </Button>
                            <Button
                                onClick={handleLoad}
                                variant="outline"
                                className="border-zinc-700"
                            >
                                <Download className="w-4 h-4" />
                            </Button>
                        </>
                    )}

                    {/* Share */}
                    {showShare && !hiddenControls.includes('share') && (
                        <Button
                            onClick={handleShare}
                            variant="outline"
                            className="border-zinc-700"
                        >
                            <Share2 className="w-4 h-4" />
                        </Button>
                    )}
                </div>
            </div>

            {/* Snippets Panel */}
            <AnimatePresence>
                {showSnippetsPanel && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        className="border-b border-purple-500/20 bg-black/30 backdrop-blur-sm overflow-hidden"
                    >
                        <div className="p-4">
                            <p className="text-sm text-zinc-400 mb-3">Sample Snippets:</p>
                            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
                                {Object.keys(sampleSnippets[environment]).map(snippetName => (
                                    <button
                                        key={snippetName}
                                        onClick={() => loadSnippet(snippetName)}
                                        className={cn(
                                            "px-3 py-2 rounded-lg text-sm",
                                            "bg-zinc-800/50 hover:bg-zinc-700/50",
                                            "border border-zinc-700/50 hover:border-purple-500/50",
                                            "text-zinc-300 hover:text-white",
                                            "transition-all duration-200"
                                        )}
                                    >
                                        {snippetName}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Split View Container */}
            <div
                className="relative flex flex-col lg:flex-row"
                style={{ height }}
            >
                {/* Editor Panel */}
                <div
                    className="relative"
                    style={{
                        width: '100%',
                        height: '50%',
                        ...(window.innerWidth >= 1024 && {
                            width: `${splitRatio}%`,
                            height: '100%',
                        }),
                    }}
                >
                    <div className="absolute top-0 left-0 right-0 h-8 bg-[#1e1e1e] border-b border-zinc-800 flex items-center px-4">
                        <Code2 className="w-3 h-3 text-zinc-500 mr-2" />
                        <span className="text-xs text-zinc-500">editor.{config.language}</span>
                    </div>
                    <div className="pt-8 h-full">
                        <Editor
                            height="100%"
                            language={config.language}
                            value={code}
                            onChange={(value) => setCode(value || '')}
                            theme="vs-dark"
                            options={{
                                minimap: { enabled: false },
                                fontSize,
                                lineNumbers: 'on',
                                scrollBeyondLastLine: false,
                                automaticLayout: true,
                                tabSize: 2,
                                wordWrap: 'on',
                                readOnly,
                            }}
                            onMount={(editor) => {
                                editorRef.current = editor
                            }}
                        />
                    </div>
                </div>

                {/* Output Panel */}
                <div
                    className="relative border-t lg:border-t-0 lg:border-l border-purple-500/20 bg-[#0a0a0f]"
                    style={{
                        width: '100%',
                        height: '50%',
                        ...(window.innerWidth >= 1024 && {
                            width: `${100 - splitRatio}%`,
                            height: '100%',
                        }),
                    }}
                >
                    <div className="absolute top-0 left-0 right-0 h-8 bg-black/30 border-b border-zinc-800 flex items-center px-4">
                        <TerminalIcon className="w-3 h-3 text-emerald-500 mr-2" />
                        <span className="text-xs text-zinc-500">output</span>
                        <div className="ml-auto flex gap-1">
                            <button
                                onClick={() => setOutput([])}
                                className="p-1 rounded hover:bg-zinc-700/50"
                            >
                                <X className="w-3 h-3 text-zinc-500" />
                            </button>
                        </div>
                    </div>
                    <div
                        ref={outputRef}
                        className="pt-8 h-full overflow-y-auto p-4 font-mono text-sm"
                    >
                        {output.length === 0 ? (
                            <div className="flex flex-col items-center justify-center h-full text-zinc-600">
                                <TerminalIcon className="w-12 h-12 mb-3 opacity-30" />
                                <p className="text-sm">Output will appear here</p>
                                <p className="text-xs mt-1">Press Cmd/Ctrl + Enter to run</p>
                            </div>
                        ) : (
                            output.map((entry, idx) => (
                                <div
                                    key={idx}
                                    className={cn(
                                        "mb-2 whitespace-pre-wrap break-words",
                                        entry.type === 'stdout' && "text-zinc-300",
                                        entry.type === 'stderr' && "text-red-400",
                                        entry.type === 'info' && "text-cyan-400",
                                        entry.type === 'success' && "text-emerald-400",
                                        entry.type === 'error' && "text-red-400"
                                    )}
                                >
                                    {entry.content}
                                </div>
                            ))
                        )}
                    </div>
                </div>
            </div>

            {/* Keyboard Shortcuts Info */}
            <div className="relative z-10 px-4 py-2 bg-black/20 backdrop-blur-sm border-t border-purple-500/20">
                <div className="flex items-center justify-between text-xs text-zinc-500">
                    <div className="flex items-center gap-4">
                        <span>Keyboard: <kbd className="px-1.5 py-0.5 rounded bg-zinc-800">Cmd/Ctrl + Enter</kbd> to run</span>
                        <span><kbd className="px-1.5 py-0.5 rounded bg-zinc-800">Cmd/Ctrl + S</kbd> to save</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <Zap className="w-3 h-3 text-yellow-500" />
                        <span>{config.description}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default CodePlayground
