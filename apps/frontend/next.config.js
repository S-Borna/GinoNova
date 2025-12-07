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

    // 📦 OPTIMIZATION: Reduce number of JS chunks for cleaner network tab
    experimental: {
        // Combine more code into fewer chunks
        optimizePackageImports: [
            'lucide-react',
            '@radix-ui/react-icons',
            'framer-motion',
            'date-fns',
        ],
    },

    // Bundle analyzer (optional - run with ANALYZE=true npm run build)
    webpack: (config, { isServer }) => {
        if (!isServer) {
            // Minimize chunk splitting for cleaner network requests
            config.optimization.splitChunks = {
                chunks: 'all',
                minSize: 50000, // 50kb minimum before splitting
                maxInitialRequests: 10, // Max 10 initial requests
                maxAsyncRequests: 10,
                cacheGroups: {
                    default: false,
                    vendors: false,
                    // Bundle all vendor code together
                    vendor: {
                        name: 'vendor',
                        chunks: 'all',
                        test: /node_modules/,
                        priority: 20,
                    },
                    // Bundle common code
                    common: {
                        name: 'common',
                        minChunks: 2,
                        chunks: 'all',
                        priority: 10,
                        reuseExistingChunk: true,
                        enforce: true,
                    },
                },
            };
        }
        return config;
    },
}