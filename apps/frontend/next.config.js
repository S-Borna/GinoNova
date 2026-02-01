/** @type {import('next').NextConfig} */
module.exports = {
    reactStrictMode: true,
    
    // Cloudflare Pages deployment (requires @cloudflare/next-on-pages with Next.js 15)
    // output: 'export', // Disabled - we need API routes for NextAuth

    // Next.js 16: Explicit webpack mode (Turbopack is default in 16)
    // Keep webpack for production builds with custom optimization
    turbopack: {},

    // 🛡️ SECURITY: Disable source maps in production
    productionBrowserSourceMaps: false,

    // 🛡️ SECURITY: Minimize exposure - hide all internal structure
    poweredByHeader: false,

    // 🛡️ SECURITY: Remove ALL console output in production
    compiler: {
        removeConsole: process.env.NODE_ENV === 'production',
    },

    // 🛡️ SECURITY: Disable prefetching - stops DevTools from revealing routes
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

            // 🛡️ SECURITY: Mangle/obfuscate function and variable names
            if (config.optimization.minimizer) {
                config.optimization.minimizer.forEach((minimizer) => {
                    if (minimizer.constructor.name === 'TerserPlugin') {
                        minimizer.options.terserOptions = {
                            ...minimizer.options.terserOptions,
                            mangle: true,
                            compress: {
                                drop_console: true,
                                drop_debugger: true,
                            },
                        };
                    }
                });
            }
        }
        return config;
    },
}