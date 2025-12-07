/** @type {import('next').NextConfig} */
module.exports = {
    reactStrictMode: true,
    // Output configuration for Netlify
    output: 'standalone',

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
            // AGGRESSIVE: Bundle everything into minimal chunks
            config.optimization.splitChunks = {
                chunks: 'all',
                minSize: 0,
                maxInitialRequests: 3,
                maxAsyncRequests: 3,
                cacheGroups: {
                    default: false,
                    vendors: false,
                    defaultVendors: false,
                    vendor: {
                        name: 'vendor',
                        test: /[\\/]node_modules[\\/]/,
                        chunks: 'all',
                        priority: 20,
                        enforce: true,
                    },
                    app: {
                        name: 'app',
                        test: /[\\/]src[\\/]/,
                        chunks: 'all',
                        priority: 10,
                        enforce: true,
                        minChunks: 1,
                    },
                },
            };
            config.optimization.runtimeChunk = false;
            
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