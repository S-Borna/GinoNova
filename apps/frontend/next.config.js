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
}