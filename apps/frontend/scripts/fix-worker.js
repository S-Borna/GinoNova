/**
 * Post-build script to fix worker.js for Cloudflare Pages
 * - Removes durable objects exports that aren't needed for Pages
 * - Fixes absolute paths in handler.mjs for @vercel/og assets
 * - Copies @vercel/og assets to where wrangler expects them
 */

const fs = require('fs');
const path = require('path');

// Fix worker.js - remove durable objects
const workerPath = path.join(__dirname, '../.open-next/worker.js');

if (fs.existsSync(workerPath)) {
    let content = fs.readFileSync(workerPath, 'utf-8');

    // Remove durable objects exports
    content = content
        .replace(/.*DOQueueHandler.*\n/g, '')
        .replace(/.*DOShardedTagCache.*\n/g, '')
        .replace(/.*BucketCachePurge.*\n/g, '');

    fs.writeFileSync(workerPath, content);
    console.log('✅ Fixed worker.js - removed durable objects exports');
} else {
    console.log('⚠️ worker.js not found at', workerPath);
}

// Fix handler.mjs - convert absolute paths to relative
const handlerPath = path.join(__dirname, '../.open-next/server-functions/default/apps/frontend/handler.mjs');

if (fs.existsSync(handlerPath)) {
    let content = fs.readFileSync(handlerPath, 'utf-8');

    // Get the monorepo root path that's embedded
    const monoRepoRoot = '/Users/mrebadi/Desktop/DevOps/SaaS-Project/saas-project';
    const frontendPath = `${monoRepoRoot}/apps/frontend`;
    const openNextPath = `${frontendPath}/.open-next/server-functions/default`;

    // Replace absolute @vercel/og asset paths with relative ones
    // These imports need to point to node_modules within the bundle
    content = content
        // Fix .wasm imports - make them relative to current directory
        .replace(
            new RegExp(`from"${openNextPath}/node_modules/next/dist/compiled/@vercel/og/resvg\\.wasm\\?module"`, 'g'),
            'from"./node_modules/next/dist/compiled/@vercel/og/resvg.wasm?module"'
        )
        .replace(
            new RegExp(`from"${openNextPath}/node_modules/next/dist/compiled/@vercel/og/yoga\\.wasm\\?module"`, 'g'),
            'from"./node_modules/next/dist/compiled/@vercel/og/yoga.wasm?module"'
        )
        // Fix dynamic imports for the same
        .replace(
            new RegExp(`import\\("${openNextPath}/node_modules/next/dist/compiled/@vercel/og/resvg\\.wasm\\?module"\\)`, 'g'),
            'import("./node_modules/next/dist/compiled/@vercel/og/resvg.wasm?module")'
        )
        .replace(
            new RegExp(`import\\("${openNextPath}/node_modules/next/dist/compiled/@vercel/og/yoga\\.wasm\\?module"\\)`, 'g'),
            'import("./node_modules/next/dist/compiled/@vercel/og/yoga.wasm?module")'
        )
        .replace(
            new RegExp(`import\\("${openNextPath}/node_modules/next/dist/compiled/@vercel/og/noto-sans-v27-latin-regular\\.ttf\\.bin"\\)`, 'g'),
            'import("./node_modules/next/dist/compiled/@vercel/og/noto-sans-v27-latin-regular.ttf.bin")'
        );

    fs.writeFileSync(handlerPath, content);
    console.log('✅ Fixed handler.mjs - converted absolute paths to relative');

    // Copy @vercel/og assets to where wrangler expects them (relative to handler.mjs)
    const sourceDir = path.join(__dirname, '../.open-next/server-functions/default/node_modules/next/dist/compiled/@vercel/og');
    const targetDir = path.join(__dirname, '../.open-next/server-functions/default/apps/frontend/node_modules/next/dist/compiled/@vercel/og');

    const filesToCopy = [
        'resvg.wasm',
        'yoga.wasm',
        'noto-sans-v27-latin-regular.ttf.bin'
    ];

    // Create target directory recursively
    fs.mkdirSync(targetDir, { recursive: true });

    let copiedCount = 0;
    for (const file of filesToCopy) {
        const srcPath = path.join(sourceDir, file);
        const destPath = path.join(targetDir, file);
        if (fs.existsSync(srcPath)) {
            fs.copyFileSync(srcPath, destPath);
            copiedCount++;
        }
    }
    console.log(`✅ Copied ${copiedCount}/${filesToCopy.length} @vercel/og assets to handler directory`);
} else {
    console.log('⚠️ handler.mjs not found at', handlerPath);
}
