"use client"

/**
 * ============================================================================
 * MARKDOWN RENDERER - GitHub-Flavored Markdown Display
 * ============================================================================
 *
 * Features:
 * - GitHub-flavored markdown (GFM)
 * - Syntax highlighting for code blocks
 * - Custom styling matching design system
 * - Code copy button
 * - Responsive images
 * - Tables support
 * - Task lists support
 *
 * @phase C.2 - Task Content Display
 */

import * as React from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import rehypeHighlight from "rehype-highlight"
import { cn } from "@/lib/utils"
import { CodeBlock, InlineCode } from "./CodeBlock"
import { ExternalLink, Link as LinkIcon } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface MarkdownRendererProps {
    content: string
    className?: string
}

/* ============================================================================
   CUSTOM COMPONENTS
   ============================================================================ */

const components = {
    // Headings with anchor links
    h1: ({ children, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
        <h1
            className="text-3xl font-bold text-neutral-900 dark:text-white mt-8 mb-4 first:mt-0"
            {...props}
        >
            {children}
        </h1>
    ),
    h2: ({ children, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
        <h2
            className="text-2xl font-semibold text-neutral-900 dark:text-white mt-8 mb-3 pb-2 border-b border-neutral-200 dark:border-neutral-700"
            {...props}
        >
            {children}
        </h2>
    ),
    h3: ({ children, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
        <h3
            className="text-xl font-semibold text-neutral-900 dark:text-white mt-6 mb-2"
            {...props}
        >
            {children}
        </h3>
    ),
    h4: ({ children, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
        <h4
            className="text-lg font-semibold text-neutral-900 dark:text-white mt-4 mb-2"
            {...props}
        >
            {children}
        </h4>
    ),

    // Paragraphs
    p: ({ children, ...props }: React.HTMLAttributes<HTMLParagraphElement>) => (
        <p
            className="text-neutral-700 dark:text-neutral-300 leading-7 mb-4"
            {...props}
        >
            {children}
        </p>
    ),

    // Lists
    ul: ({ children, ...props }: React.HTMLAttributes<HTMLUListElement>) => (
        <ul
            className="list-disc list-inside space-y-2 mb-4 text-neutral-700 dark:text-neutral-300"
            {...props}
        >
            {children}
        </ul>
    ),
    ol: ({ children, ...props }: React.HTMLAttributes<HTMLOListElement>) => (
        <ol
            className="list-decimal list-inside space-y-2 mb-4 text-neutral-700 dark:text-neutral-300"
            {...props}
        >
            {children}
        </ol>
    ),
    li: ({ children, ...props }: React.HTMLAttributes<HTMLLIElement>) => (
        <li className="leading-7" {...props}>
            {children}
        </li>
    ),

    // Links
    a: ({ href, children, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) => {
        const isExternal = href?.startsWith("http")
        return (
            <a
                href={href}
                target={isExternal ? "_blank" : undefined}
                rel={isExternal ? "noopener noreferrer" : undefined}
                className={cn(
                    "text-primary-600 dark:text-primary-400 hover:underline",
                    "inline-flex items-center gap-1"
                )}
                {...props}
            >
                {children}
                {isExternal && <ExternalLink className="h-3.5 w-3.5" />}
            </a>
        )
    },

    // Code blocks
    pre: ({ children, ...props }: React.HTMLAttributes<HTMLPreElement>) => {
        // Extract code element from children
        const codeElement = React.Children.toArray(children).find(
            (child): child is React.ReactElement<{ className?: string; children?: React.ReactNode }> =>
                React.isValidElement(child) && child.type === "code"
        )

        if (codeElement) {
            const codeClassName = codeElement.props.className || ""
            const match = /language-(\w+)/.exec(codeClassName)
            const language = match ? match[1] : undefined
            const code = String(codeElement.props.children || "").replace(/\n$/, "")

            return <CodeBlock language={language}>{code}</CodeBlock>
        }

        return <pre {...props}>{children}</pre>
    },

    // Inline code
    code: ({ className, children, ...props }: React.HTMLAttributes<HTMLElement>) => {
        // Check if this is a code block (has language class)
        const isCodeBlock = className?.includes("language-")
        if (isCodeBlock) {
            return (
                <code className={className} {...props}>
                    {children}
                </code>
            )
        }
        return <InlineCode>{children}</InlineCode>
    },

    // Blockquotes
    blockquote: ({ children, ...props }: React.HTMLAttributes<HTMLQuoteElement>) => (
        <blockquote
            className={cn(
                "border-l-4 border-primary-500 pl-4 py-2 my-4",
                "bg-primary-50 dark:bg-primary-950/20 rounded-r-lg",
                "text-neutral-700 dark:text-neutral-300 italic"
            )}
            {...props}
        >
            {children}
        </blockquote>
    ),

    // Horizontal rule
    hr: () => (
        <hr className="my-8 border-neutral-200 dark:border-neutral-700" />
    ),

    // Tables
    table: ({ children, ...props }: React.TableHTMLAttributes<HTMLTableElement>) => (
        <div className="overflow-x-auto my-4">
            <table
                className="min-w-full border-collapse border border-neutral-200 dark:border-neutral-700 rounded-lg"
                {...props}
            >
                {children}
            </table>
        </div>
    ),
    thead: ({ children, ...props }: React.HTMLAttributes<HTMLTableSectionElement>) => (
        <thead className="bg-neutral-100 dark:bg-neutral-800" {...props}>
            {children}
        </thead>
    ),
    th: ({ children, ...props }: React.ThHTMLAttributes<HTMLTableCellElement>) => (
        <th
            className="px-4 py-3 text-left text-sm font-semibold text-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-700"
            {...props}
        >
            {children}
        </th>
    ),
    td: ({ children, ...props }: React.TdHTMLAttributes<HTMLTableCellElement>) => (
        <td
            className="px-4 py-3 text-sm text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-700"
            {...props}
        >
            {children}
        </td>
    ),

    // Images
    img: ({ src, alt, ...props }: React.ImgHTMLAttributes<HTMLImageElement>) => (
        // eslint-disable-next-line @next/next/no-img-element
        <img
            src={src}
            alt={alt || ""}
            className="max-w-full h-auto rounded-lg my-4 border border-neutral-200 dark:border-neutral-700"
            loading="lazy"
            {...props}
        />
    ),

    // Strong/Bold
    strong: ({ children, ...props }: React.HTMLAttributes<HTMLElement>) => (
        <strong className="font-semibold text-neutral-900 dark:text-white" {...props}>
            {children}
        </strong>
    ),

    // Emphasis/Italic
    em: ({ children, ...props }: React.HTMLAttributes<HTMLElement>) => (
        <em className="italic" {...props}>
            {children}
        </em>
    ),
}

/* ============================================================================
   MAIN MARKDOWN RENDERER
   ============================================================================ */

export function MarkdownRenderer({ content, className }: MarkdownRendererProps) {
    return (
        <div
            className={cn(
                "prose prose-neutral dark:prose-invert max-w-none",
                "prose-headings:scroll-mt-20",
                className
            )}
        >
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
                components={components}
            >
                {content}
            </ReactMarkdown>
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default MarkdownRenderer
