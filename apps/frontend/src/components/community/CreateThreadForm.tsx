"use client"

/**
 * ============================================================================
 * CREATE THREAD FORM — New Discussion Thread
 * ============================================================================
 *
 * Form for creating new community threads with rich text editor
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { CATEGORIES } from "@/lib/community-types"
import {
    MessageSquare,
    X,
    Bold,
    Italic,
    Code,
    List,
    Image as ImageIcon,
    Link as LinkIcon,
    Eye,
    Send,
    Sparkles,
} from "lucide-react"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"

interface CreateThreadFormProps {
    onSubmit?: (data: {
        title: string
        content: string
        categoryId: string
        tags: string[]
    }) => void
    onCancel?: () => void
    className?: string
}

export function CreateThreadForm({
    onSubmit,
    onCancel,
    className,
}: CreateThreadFormProps) {
    const [title, setTitle] = useState("")
    const [content, setContent] = useState("")
    const [categoryId, setCategoryId] = useState<string>("")
    const [tags, setTags] = useState<string[]>([])
    const [tagInput, setTagInput] = useState("")
    const [showPreview, setShowPreview] = useState(false)
    const [errors, setErrors] = useState<Record<string, string>>({})

    const validateForm = () => {
        const newErrors: Record<string, string> = {}

        if (!title.trim()) {
            newErrors.title = "Title is required"
        } else if (title.length < 10) {
            newErrors.title = "Title must be at least 10 characters"
        } else if (title.length > 200) {
            newErrors.title = "Title must be less than 200 characters"
        }

        if (!content.trim()) {
            newErrors.content = "Content is required"
        } else if (content.length < 20) {
            newErrors.content = "Content must be at least 20 characters"
        }

        if (!categoryId) {
            newErrors.category = "Please select a category"
        }

        if (tags.length === 0) {
            newErrors.tags = "Add at least one tag"
        } else if (tags.length > 5) {
            newErrors.tags = "Maximum 5 tags allowed"
        }

        setErrors(newErrors)
        return Object.keys(newErrors).length === 0
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()

        if (validateForm() && onSubmit) {
            onSubmit({
                title: title.trim(),
                content: content.trim(),
                categoryId,
                tags,
            })

            // Reset form
            setTitle("")
            setContent("")
            setCategoryId("")
            setTags([])
            setTagInput("")
            setErrors({})
        }
    }

    const handleAddTag = () => {
        const tag = tagInput.trim().toLowerCase()
        if (tag && !tags.includes(tag) && tags.length < 5) {
            setTags([...tags, tag])
            setTagInput("")
            setErrors({ ...errors, tags: "" })
        }
    }

    const handleRemoveTag = (tagToRemove: string) => {
        setTags(tags.filter((tag) => tag !== tagToRemove))
    }

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === "Enter") {
            e.preventDefault()
            handleAddTag()
        }
    }

    const insertMarkdown = (type: string) => {
        const textarea = document.querySelector("textarea") as HTMLTextAreaElement
        if (!textarea) return

        const start = textarea.selectionStart
        const end = textarea.selectionEnd
        const selectedText = content.substring(start, end)
        let newText = content

        switch (type) {
            case "bold":
                newText =
                    content.substring(0, start) +
                    `**${selectedText || "bold text"}**` +
                    content.substring(end)
                break
            case "italic":
                newText =
                    content.substring(0, start) +
                    `*${selectedText || "italic text"}*` +
                    content.substring(end)
                break
            case "code":
                newText =
                    content.substring(0, start) +
                    `\`${selectedText || "code"}\`` +
                    content.substring(end)
                break
            case "codeblock":
                newText =
                    content.substring(0, start) +
                    `\n\`\`\`\n${selectedText || "code block"}\n\`\`\`\n` +
                    content.substring(end)
                break
            case "list":
                newText =
                    content.substring(0, start) +
                    `\n- ${selectedText || "list item"}\n- list item\n` +
                    content.substring(end)
                break
            case "link":
                newText =
                    content.substring(0, start) +
                    `[${selectedText || "link text"}](url)` +
                    content.substring(end)
                break
        }

        setContent(newText)
    }

    const selectedCategory = CATEGORIES.find((c) => c.id === categoryId)

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "p-8 rounded-3xl",
                "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                "border border-zinc-800/80",
                className
            )}
            style={{
                boxShadow: "0 0 40px rgba(0, 0, 0, 0.5)",
            }}
        >
            {/* Header */}
            <div className="mb-8">
                <div className="flex items-center gap-3 mb-3">
                    <motion.div
                        className="p-2.5 rounded-xl bg-gradient-to-br from-purple-500/30 to-purple-600/20 border border-purple-500/40"
                        animate={{
                            boxShadow: [
                                "0 0 20px rgba(139, 92, 246, 0.3)",
                                "0 0 40px rgba(139, 92, 246, 0.5)",
                                "0 0 20px rgba(139, 92, 246, 0.3)",
                            ],
                        }}
                        transition={{
                            duration: 2,
                            repeat: Infinity,
                            ease: "easeInOut",
                        }}
                    >
                        <MessageSquare className="w-5 h-5 text-purple-400" />
                    </motion.div>
                    <h2 className="text-2xl font-black text-white">
                        Create New Discussion
                    </h2>
                </div>
                <p className="text-zinc-400">
                    Share your knowledge, ask questions, or start a discussion with
                    the community
                </p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6">
                {/* Title */}
                <div>
                    <Label htmlFor="title" className="text-white mb-2 block">
                        Title *
                    </Label>
                    <Input
                        id="title"
                        placeholder="Enter a descriptive title for your thread..."
                        value={title}
                        onChange={(e) => {
                            setTitle(e.target.value)
                            setErrors({ ...errors, title: "" })
                        }}
                        className={cn(
                            "h-12 rounded-xl bg-zinc-900/50 border-zinc-800",
                            "focus:border-purple-500",
                            errors.title && "border-red-500"
                        )}
                    />
                    {errors.title && (
                        <p className="text-red-400 text-sm mt-1">{errors.title}</p>
                    )}
                    <p className="text-xs text-zinc-500 mt-1">
                        {title.length}/200 characters
                    </p>
                </div>

                {/* Category */}
                <div>
                    <Label htmlFor="category" className="text-white mb-2 block">
                        Category *
                    </Label>
                    <Select value={categoryId} onValueChange={setCategoryId}>
                        <SelectTrigger
                            className={cn(
                                "h-12 rounded-xl bg-zinc-900/50 border-zinc-800",
                                errors.category && "border-red-500"
                            )}
                        >
                            <SelectValue placeholder="Select a category..." />
                        </SelectTrigger>
                        <SelectContent className="bg-zinc-900 border-zinc-800">
                            {CATEGORIES.map((category) => (
                                <SelectItem
                                    key={category.id}
                                    value={category.id}
                                    className="cursor-pointer hover:bg-zinc-800"
                                >
                                    <div className="flex items-center gap-2">
                                        <span>{category.icon}</span>
                                        <span>{category.name}</span>
                                    </div>
                                </SelectItem>
                            ))}
                        </SelectContent>
                    </Select>
                    {errors.category && (
                        <p className="text-red-400 text-sm mt-1">{errors.category}</p>
                    )}
                    {selectedCategory && (
                        <p className="text-xs text-zinc-500 mt-1">
                            {selectedCategory.description}
                        </p>
                    )}
                </div>

                {/* Tags */}
                <div>
                    <Label htmlFor="tags" className="text-white mb-2 block">
                        Tags *
                    </Label>
                    <div className="flex gap-2 mb-2">
                        <Input
                            id="tags"
                            placeholder="Add tags (press Enter)..."
                            value={tagInput}
                            onChange={(e) => setTagInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            disabled={tags.length >= 5}
                            className={cn(
                                "h-10 rounded-xl bg-zinc-900/50 border-zinc-800",
                                errors.tags && "border-red-500"
                            )}
                        />
                        <Button
                            type="button"
                            onClick={handleAddTag}
                            disabled={!tagInput.trim() || tags.length >= 5}
                            className="rounded-xl bg-purple-600 hover:bg-purple-500"
                        >
                            Add
                        </Button>
                    </div>
                    {errors.tags && (
                        <p className="text-red-400 text-sm mb-2">{errors.tags}</p>
                    )}
                    <div className="flex flex-wrap gap-2">
                        {tags.map((tag) => (
                            <motion.span
                                key={tag}
                                initial={{ opacity: 0, scale: 0.8 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0.8 }}
                                className="px-3 py-1.5 rounded-lg bg-purple-500/20 text-purple-300 text-sm flex items-center gap-2 border border-purple-500/30"
                            >
                                #{tag}
                                <button
                                    type="button"
                                    onClick={() => handleRemoveTag(tag)}
                                    className="hover:text-white transition-colors"
                                >
                                    <X className="w-3 h-3" />
                                </button>
                            </motion.span>
                        ))}
                    </div>
                    <p className="text-xs text-zinc-500 mt-2">
                        {tags.length}/5 tags added
                    </p>
                </div>

                {/* Content */}
                <div>
                    <div className="flex items-center justify-between mb-2">
                        <Label htmlFor="content" className="text-white">
                            Content *
                        </Label>
                        <Button
                            type="button"
                            variant="ghost"
                            size="sm"
                            onClick={() => setShowPreview(!showPreview)}
                            className="rounded-lg text-purple-400"
                        >
                            <Eye className="w-4 h-4 mr-2" />
                            {showPreview ? "Edit" : "Preview"}
                        </Button>
                    </div>

                    {/* Editor Toolbar */}
                    {!showPreview && (
                        <div className="flex flex-wrap gap-2 mb-2 p-2 rounded-xl bg-zinc-900/50 border border-zinc-800">
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("bold")}
                                className="rounded-lg"
                                title="Bold (Ctrl+B)"
                            >
                                <Bold className="w-4 h-4" />
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("italic")}
                                className="rounded-lg"
                                title="Italic (Ctrl+I)"
                            >
                                <Italic className="w-4 h-4" />
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("code")}
                                className="rounded-lg"
                                title="Inline Code"
                            >
                                <Code className="w-4 h-4" />
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("codeblock")}
                                className="rounded-lg"
                                title="Code Block"
                            >
                                <Code className="w-4 h-4 mr-1" />
                                Block
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("list")}
                                className="rounded-lg"
                                title="Bulleted List"
                            >
                                <List className="w-4 h-4" />
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                onClick={() => insertMarkdown("link")}
                                className="rounded-lg"
                                title="Insert Link"
                            >
                                <LinkIcon className="w-4 h-4" />
                            </Button>
                            <Button
                                type="button"
                                variant="ghost"
                                size="sm"
                                className="rounded-lg"
                                title="Upload Image"
                            >
                                <ImageIcon className="w-4 h-4" />
                            </Button>
                        </div>
                    )}

                    <AnimatePresence mode="wait">
                        {showPreview ? (
                            <motion.div
                                key="preview"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                                className={cn(
                                    "min-h-[300px] p-4 rounded-xl",
                                    "bg-zinc-900/50 border border-zinc-800",
                                    "prose prose-invert prose-sm max-w-none"
                                )}
                            >
                                {content ? (
                                    <MarkdownPreview content={content} />
                                ) : (
                                    <p className="text-zinc-500 italic">
                                        Nothing to preview yet...
                                    </p>
                                )}
                            </motion.div>
                        ) : (
                            <motion.div
                                key="editor"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                            >
                                <Textarea
                                    id="content"
                                    placeholder="Write your post here... Markdown is supported!&#10;&#10;Use **bold**, *italic*, `code`, or ```code blocks```"
                                    value={content}
                                    onChange={(e) => {
                                        setContent(e.target.value)
                                        setErrors({ ...errors, content: "" })
                                    }}
                                    className={cn(
                                        "min-h-[300px] rounded-xl bg-zinc-900/50 border-zinc-800",
                                        "focus:border-purple-500 font-mono text-sm",
                                        errors.content && "border-red-500"
                                    )}
                                />
                            </motion.div>
                        )}
                    </AnimatePresence>

                    {errors.content && (
                        <p className="text-red-400 text-sm mt-1">{errors.content}</p>
                    )}
                    <p className="text-xs text-zinc-500 mt-1">
                        {content.length} characters • Markdown supported
                    </p>
                </div>

                {/* Actions */}
                <div className="flex gap-3 pt-6 border-t border-zinc-800">
                    <Button
                        type="submit"
                        className={cn(
                            "flex-1 rounded-xl h-12",
                            "bg-gradient-to-r from-purple-600 to-purple-500",
                            "hover:from-purple-500 hover:to-purple-400",
                            "shadow-[0_0_30px_rgba(139,92,246,0.3)]"
                        )}
                    >
                        <Send className="w-4 h-4 mr-2" />
                        Create Thread
                    </Button>
                    {onCancel && (
                        <Button
                            type="button"
                            variant="outline"
                            onClick={onCancel}
                            className="rounded-xl h-12 px-8"
                        >
                            Cancel
                        </Button>
                    )}
                </div>

                {/* Help Text */}
                <div className="flex items-start gap-3 p-4 rounded-xl bg-purple-500/10 border border-purple-500/30">
                    <Sparkles className="w-5 h-5 text-purple-400 shrink-0 mt-0.5" />
                    <div className="text-sm text-zinc-300">
                        <p className="font-semibold text-purple-300 mb-1">
                            Tips for a great post:
                        </p>
                        <ul className="text-xs text-zinc-400 space-y-1 list-disc list-inside">
                            <li>Write a clear, descriptive title</li>
                            <li>
                                Include code examples using ``` for better readability
                            </li>
                            <li>Add relevant tags to help others find your post</li>
                            <li>Be respectful and follow community guidelines</li>
                        </ul>
                    </div>
                </div>
            </form>
        </motion.div>
    )
}

function MarkdownPreview({ content }: { content: string }) {
    const parts = content.split("```")

    return (
        <div className="text-zinc-300 whitespace-pre-wrap leading-relaxed">
            {parts.map((part, i) =>
                i % 2 === 0 ? (
                    <span key={i}>{part}</span>
                ) : (
                    <pre
                        key={i}
                        className="my-3 p-4 rounded-xl bg-zinc-900/80 border border-zinc-800 overflow-x-auto text-sm"
                    >
                        <code className="text-emerald-400 font-mono">{part}</code>
                    </pre>
                )
            )}
        </div>
    )
}
