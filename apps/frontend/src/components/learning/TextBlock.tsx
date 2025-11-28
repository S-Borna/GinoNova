"use client"

/**
 * ============================================================================
 * TEXT BLOCK COMPONENT - Markdown Content Renderer
 * ============================================================================
 *
 * Renders markdown content with:
 * - Headings, paragraphs, lists
 * - Tables with GFM support
 * - Links and images
 * - Proper dark theme styling
 *
 * @phase ILE Phase 3 - Content Blocks
 */

import * as React from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TextBlockProps {
    content: string
    className?: string
}

/* ============================================================================
   MARKDOWN COMPONENTS
   ============================================================================ */

const markdownComponents = {
    h1: ({ children }: any) => (
        <h1 className="text-3xl font-bold text-white mt-8 mb-4 first:mt-0">
            {children}
        </h1>
    ),
    h2: ({ children }: any) => (
        <h2 className="text-2xl font-semibold text-white mt-6 mb-3 border-b border-neutral-800 pb-2">
            {children}
        </h2>
    ),
    h3: ({ children }: any) => (
        <h3 className="text-xl font-semibold text-white mt-5 mb-2">
            {children}
        </h3>
    ),
    h4: ({ children }: any) => (
        <h4 className="text-lg font-medium text-white mt-4 mb-2">
            {children}
        </h4>
    ),
    p: ({ children }: any) => (
        <p className="text-neutral-300 leading-relaxed mb-4">
            {children}
        </p>
    ),
    ul: ({ children }: any) => (
        <ul className="list-disc list-inside text-neutral-300 mb-4 space-y-1 ml-4">
            {children}
        </ul>
    ),
    ol: ({ children }: any) => (
        <ol className="list-decimal list-inside text-neutral-300 mb-4 space-y-1 ml-4">
            {children}
        </ol>
    ),
    li: ({ children }: any) => (
        <li className="text-neutral-300">
            {children}
        </li>
    ),
    strong: ({ children }: any) => (
        <strong className="font-semibold text-white">
            {children}
        </strong>
    ),
    em: ({ children }: any) => (
        <em className="italic text-neutral-200">
            {children}
        </em>
    ),
    code: ({ inline, children }: any) => {
        if (inline) {
            return (
                <code className="px-1.5 py-0.5 rounded bg-neutral-800 text-primary-400 font-mono text-sm">
                    {children}
                </code>
            )
        }
        return (
            <code className="block bg-neutral-900 rounded-lg p-4 font-mono text-sm text-neutral-300 overflow-x-auto">
                {children}
            </code>
        )
    },
    pre: ({ children }: any) => (
        <pre className="bg-neutral-900 rounded-lg p-4 overflow-x-auto mb-4">
            {children}
        </pre>
    ),
    blockquote: ({ children }: any) => (
        <blockquote className="border-l-4 border-primary-500 pl-4 py-2 my-4 bg-neutral-900/50 rounded-r-lg">
            {children}
        </blockquote>
    ),
    a: ({ href, children }: any) => (
        <a
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            className="text-primary-400 hover:text-primary-300 underline underline-offset-2"
        >
            {children}
        </a>
    ),
    table: ({ children }: any) => (
        <div className="overflow-x-auto mb-4">
            <table className="min-w-full border border-neutral-800 rounded-lg overflow-hidden">
                {children}
            </table>
        </div>
    ),
    thead: ({ children }: any) => (
        <thead className="bg-neutral-800">
            {children}
        </thead>
    ),
    tbody: ({ children }: any) => (
        <tbody className="divide-y divide-neutral-800">
            {children}
        </tbody>
    ),
    tr: ({ children }: any) => (
        <tr className="hover:bg-neutral-900/50">
            {children}
        </tr>
    ),
    th: ({ children }: any) => (
        <th className="px-4 py-2 text-left text-sm font-semibold text-white">
            {children}
        </th>
    ),
    td: ({ children }: any) => (
        <td className="px-4 py-2 text-sm text-neutral-300">
            {children}
        </td>
    ),
    hr: () => (
        <hr className="border-neutral-800 my-6" />
    ),
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function TextBlock({ content, className }: TextBlockProps) {
    return (
        <div className={cn("prose prose-invert max-w-none", className)}>
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={markdownComponents}
            >
                {content}
            </ReactMarkdown>
        </div>
    )
}

export default TextBlock
