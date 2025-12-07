/** @type {import('next').NextConfig} */
module.exports = {
    reactStrictMode: true,
    // Output configuration for Netlify
    output: 'standalone',

    // 🛡️ SECURITY: Disable source maps in production
    productionBrowserSourceMaps: false,

    // 🛡️ SECURITY: Minimize exposure
    poweredByHeader: false,

    // 🛡️ SECURITY: Remove ALL console output in production
    compiler: {
        removeConsole: process.env.NODE_ENV === 'production',
    },

    // 📦 AGGRESSIVE OPTIMIZATION: Maximum bundling for minimal network requests
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
                maxInitialRequests: 3, // Only 3 JS files max!
                maxAsyncRequests: 3,
                cacheGroups: {
                    default: false,
                    vendors: false,
                    defaultVendors: false,
                    // ONE file for all vendor code
                    vendor: {
                        name: 'vendor',
                        test: /[\\/]node_modules[\\/]/,
                        chunks: 'all',
                        priority: 20,
                        enforce: true,
                    },
                    // ONE file for all app code
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
            
            // Disable runtime chunk splitting
            config.optimization.runtimeChunk = false;
        }
        return config;
    },
}