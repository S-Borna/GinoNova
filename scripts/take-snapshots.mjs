#!/usr/bin/env node
/**
 * Screenshot Documentation Script
 * Takes snapshots of key pages for documentation purposes
 *
 * Usage: node scripts/take-snapshots.mjs
 * Requires: npx playwright install chromium (first time only)
 */

import { chromium } from 'playwright';
import { mkdir } from 'fs/promises';
import { join } from 'path';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';
const OUTPUT_DIR = process.env.OUTPUT_DIR || `docs/snapshots/${new Date().toISOString().split('T')[0]}`;

// Pages to capture
const pages = [
    { name: '01-landing', path: '/', description: 'Landing page' },
    { name: '02-landing-dark', path: '/', dark: true, description: 'Landing page (dark mode)' },
    { name: '03-dashboard', path: '/dashboard', description: 'Dashboard' },
    { name: '04-dashboard-dark', path: '/dashboard', dark: true, description: 'Dashboard (dark mode)' },
    { name: '05-modules', path: '/modules', description: 'Modules list' },
    { name: '06-modules-dark', path: '/modules', dark: true, description: 'Modules list (dark mode)' },
    { name: '07-profile', path: '/profile', description: 'User profile' },
    { name: '08-settings', path: '/settings', description: 'Settings page' },
];

async function takeSnapshots() {
    console.log('📸 Starting snapshot capture...\n');
    console.log(`   Base URL: ${BASE_URL}`);
    console.log(`   Output: ${OUTPUT_DIR}\n`);

    // Create output directory
    await mkdir(OUTPUT_DIR, { recursive: true });

    const browser = await chromium.launch();
    const context = await browser.newContext({
        viewport: { width: 1440, height: 900 },
    });

    const page = await context.newPage();

    for (const config of pages) {
        try {
            const url = `${BASE_URL}${config.path}`;
            console.log(`   Capturing: ${config.name} - ${config.description}`);

            await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });

            // Toggle dark mode if needed
            if (config.dark) {
                await page.evaluate(() => {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('theme', 'dark');
                });
                await page.waitForTimeout(500); // Wait for theme transition
            } else {
                await page.evaluate(() => {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('theme', 'light');
                });
                await page.waitForTimeout(500);
            }

            // Take screenshot
            const filename = `${config.name}.png`;
            await page.screenshot({
                path: join(OUTPUT_DIR, filename),
                fullPage: false,
            });

            console.log(`   ✅ Saved: ${filename}`);
        } catch (error) {
            console.log(`   ❌ Failed: ${config.name} - ${error.message}`);
        }
    }

    await browser.close();

    console.log('\n✨ Snapshot capture complete!');
    console.log(`   Files saved to: ${OUTPUT_DIR}`);
}

// Run
takeSnapshots().catch(console.error);
