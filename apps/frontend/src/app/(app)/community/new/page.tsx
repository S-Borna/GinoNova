"use client"

/**
 * ============================================================================
 * CREATE THREAD PAGE — New Discussion
 * ============================================================================
 *
 * Page for creating new community threads
 */

import { useRouter } from "next/navigation"
import Link from "next/link"
import { ArrowLeft } from "lucide-react"
import { Button } from "@/components/ui/button"
import { CreateThreadForm } from "@/components/community"

export default function NewThreadPage() {
    const router = useRouter()

    const handleSubmit = (data: {
        title: string
        content: string
        categoryId: string
        tags: string[]
    }) => {
        console.log("Creating thread:", data)
        // In a real app, this would make an API call to create the thread
        // For now, we'll just redirect back to the community page
        // router.push("/community")

        // Simulate API call
        setTimeout(() => {
            alert(
                `Thread created successfully!\n\nTitle: ${data.title}\nCategory: ${data.categoryId}\nTags: ${data.tags.join(", ")}`
            )
            router.push("/community")
        }, 500)
    }

    const handleCancel = () => {
        router.push("/community")
    }

    return (
        <div className="min-h-screen">
            {/* Back Button */}
            <Link href="/community" prefetch={false}>
                <Button variant="ghost" className="mb-6 rounded-xl">
                    <ArrowLeft className="w-4 h-4 mr-2" />
                    Back to Community
                </Button>
            </Link>

            {/* Form */}
            <CreateThreadForm onSubmit={handleSubmit} onCancel={handleCancel} />
        </div>
    )
}
