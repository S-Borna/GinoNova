/**
 * Post-build script to fix worker.js for Cloudflare Pages
 * Removes durable objects exports that aren't needed for Pages
 */

const fs = require('fs');
const path = require('path');

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
