/** @type {import('next').NextConfig} */
module.exports = {
    reactStrictMode: true,

    // Cloudflare Pages deployment (requires @cloudflare/next-on-pages with Next.js 15)
    // output: 'export', // Disabled - we need API routes for NextAuth

    // Next.js 16: Explicit webpack mode (Turbopack is default in 16)
    // Keep webpack for production builds with custom optimization
    turbopack: {},

    experimental: {
        optimizePackageImports: [
            'lucide-react',
            '@radix-ui/react-icons',
            'framer-motion',
            'date-fns',
            '@hookform/resolvers',
            'react-hook-form',
            'zod',
            'clsx',
            'tailwind-merge',
        ],
    },

    webpack: (config, { isServer }) => {
        if (!isServer) {
            // OPTIMIZED: Better chunking strategy for performance
            config.optimization.splitChunks = {
                chunks: 'all',
                minSize: 20000, // 20KB minimum (prevents tiny chunks)
                maxSize: 244000, // 244KB maximum (optimal for HTTP/2)
                maxInitialRequests: 6, // Increased from 3 for better parallel loading
                maxAsyncRequests: 6,   // Increased for better code splitting
                cacheGroups: {
                    // Framework chunks (React, Next.js)
                    framework: {
                        name: 'framework',
                        test: /[\\/]node_modules[\\/](react|react-dom|scheduler|next)[\\/]/,
                        chunks: 'all',
                        priority: 40,
                        enforce: true,
                    },
                    // UI libraries
                    ui: {
                        name: 'ui',
                        test: /[\\/]node_modules[\\/](framer-motion|lucide-react|@radix-ui)[\\/]/,
                        chunks: 'all',
                        priority: 30,
                        enforce: true,
                        reuseExistingChunk: true,
                    },
                    // Other vendor code
                    vendor: {
                        name: 'vendor',
                        test: /[\\/]node_modules[\\/]/,
                        chunks: 'all',
                        priority: 20,
                        reuseExistingChunk: true,
                    },
                    // Common app code (used in 2+ places)
                    common: {
                        name: 'common',
                        minChunks: 2,
                        priority: 10,
                        reuseExistingChunk: true,
                    },
                },
            };
            // Enable runtime chunk for better caching
            config.optimization.runtimeChunk = {
                name: 'runtime'
            };


        }
        return config;
    },
}// Sun Feb  1 23:19:02 CET 2026
// triggered
