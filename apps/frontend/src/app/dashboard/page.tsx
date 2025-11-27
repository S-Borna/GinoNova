"use client"

/**
 * Dashboard Page
 * Phase 1.3: Protected dashboard page
 */

import { Protected, useAuth } from "@/components/auth"

function DashboardContent() {
    const { user, logout } = useAuth()

    return (
        <div className="min-h-screen bg-gray-50">
            <nav className="bg-white shadow">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex items-center">
                            <h1 className="text-xl font-bold text-gray-900">DevOpsHub</h1>
                        </div>
                        <div className="flex items-center space-x-4">
                            <span className="text-sm text-gray-600">
                                {user?.email}
                            </span>
                            <button
                                onClick={logout}
                                className="text-sm text-red-600 hover:text-red-500"
                            >
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                <div className="px-4 py-6 sm:px-0">
                    <div className="border-4 border-dashed border-gray-200 rounded-lg p-8">
                        <h2 className="text-2xl font-bold text-gray-900 mb-4">
                            Dashboard Online
                        </h2>
                        <p className="text-gray-600">
                            Welcome, {user?.full_name || user?.email}!
                        </p>
                        {user?.is_admin && (
                            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800 mt-2">
                                Admin
                            </span>
                        )}
                    </div>
                </div>
            </main>
        </div>
    )
}

export default function DashboardPage() {
    return (
        <Protected>
            <DashboardContent />
        </Protected>
    )
}
