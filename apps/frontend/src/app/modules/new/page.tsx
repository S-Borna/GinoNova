"use client"

/**
 * Create Module Page
 * Phase 2.1: Module creation form with validation
 */

import { useState, FormEvent } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import {
    createModule,
    validateModuleName,
    validateModuleDescription,
    MODULE_NAME_MIN,
    MODULE_NAME_MAX,
    MODULE_DESC_MAX,
} from "@/lib/modules"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Switch } from "@/components/ui/switch"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export default function CreateModulePage() {
    const router = useRouter()
    const [name, setName] = useState("")
    const [description, setDescription] = useState("")
    const [isActive, setIsActive] = useState(true)
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [nameError, setNameError] = useState<string | null>(null)
    const [descError, setDescError] = useState<string | null>(null)

    const handleNameBlur = () => {
        const result = validateModuleName(name)
        setNameError(result.valid ? null : result.error || null)
    }

    const handleDescBlur = () => {
        const result = validateModuleDescription(description)
        setDescError(result.valid ? null : result.error || null)
    }

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()
        setError(null)
        setNameError(null)
        setDescError(null)

        // Validate
        const nameValidation = validateModuleName(name)
        if (!nameValidation.valid) {
            setNameError(nameValidation.error || "Invalid name")
            return
        }

        const descValidation = validateModuleDescription(description)
        if (!descValidation.valid) {
            setDescError(descValidation.error || "Invalid description")
            return
        }

        setIsLoading(true)

        const result = await createModule({
            name: name.trim(),
            description: description.trim() || null,
            is_active: isActive,
        })

        if (result.ok) {
            router.push("/modules")
        } else {
            // Handle 409 conflict (duplicate name)
            if (result.status === 409) {
                setNameError("A module with this name already exists")
            } else {
                setError(result.message)
            }
            setIsLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-2xl mx-auto px-4">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <Link href="/modules" className="text-blue-600 hover:text-blue-500">
                        Modules
                    </Link>
                    <span className="mx-2 text-gray-400">/</span>
                    <span className="text-gray-600">New</span>
                </nav>

                <Card>
                    <CardHeader>
                        <CardTitle className="text-2xl">Create Module</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-6">
                            {/* Global error */}
                            {error && (
                                <div className="bg-red-50 text-red-600 p-3 rounded-md text-sm">
                                    {error}
                                </div>
                            )}

                            {/* Name field */}
                            <div className="space-y-2">
                                <Label htmlFor="name">
                                    Name <span className="text-red-500">*</span>
                                </Label>
                                <Input
                                    id="name"
                                    type="text"
                                    value={name}
                                    onChange={(e) => {
                                        setName(e.target.value)
                                        if (nameError) setNameError(null)
                                    }}
                                    onBlur={handleNameBlur}
                                    placeholder="Enter module name"
                                    disabled={isLoading}
                                    className={nameError ? "border-red-500" : ""}
                                />
                                <p className="text-xs text-gray-500">
                                    {MODULE_NAME_MIN}-{MODULE_NAME_MAX} characters
                                </p>
                                {nameError && (
                                    <p className="text-sm text-red-500">{nameError}</p>
                                )}
                            </div>

                            {/* Description field */}
                            <div className="space-y-2">
                                <Label htmlFor="description">Description</Label>
                                <Textarea
                                    id="description"
                                    value={description}
                                    onChange={(e) => {
                                        setDescription(e.target.value)
                                        if (descError) setDescError(null)
                                    }}
                                    onBlur={handleDescBlur}
                                    placeholder="Enter module description (optional)"
                                    disabled={isLoading}
                                    rows={4}
                                    className={descError ? "border-red-500" : ""}
                                />
                                <p className="text-xs text-gray-500">
                                    Max {MODULE_DESC_MAX} characters ({description.length}/{MODULE_DESC_MAX})
                                </p>
                                {descError && (
                                    <p className="text-sm text-red-500">{descError}</p>
                                )}
                            </div>

                            {/* Is Active toggle */}
                            <div className="flex items-center justify-between">
                                <div>
                                    <Label htmlFor="is_active">Active</Label>
                                    <p className="text-xs text-gray-500">
                                        Enable this module for users
                                    </p>
                                </div>
                                <Switch
                                    id="is_active"
                                    checked={isActive}
                                    onCheckedChange={setIsActive}
                                    disabled={isLoading}
                                />
                            </div>

                            {/* Actions */}
                            <div className="flex items-center gap-4 pt-4">
                                <Button type="submit" disabled={isLoading}>
                                    {isLoading ? "Creating..." : "Create Module"}
                                </Button>
                                <Link href="/modules">
                                    <Button type="button" variant="secondary" disabled={isLoading}>
                                        Cancel
                                    </Button>
                                </Link>
                            </div>
                        </form>
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}
