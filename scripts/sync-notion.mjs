#!/usr/bin/env node
/**
 * Notion ↔ Repo Sync Script
 *
 * Usage:
 *   npm run notion:pull    # Pull from Notion → command_center.md
 *   npm run notion:push    # Push command_center.md → Notion (future)
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY || '***REDACTED-NOTION-TOKEN***';
const PAGE_ID = '2b13f977a4d08067b6ddd6c2a80b4da5';
const OUTPUT_FILE = 'docs/command_center.md';

async function fetchAllBlocks(blockId) {
    let allBlocks = [];
    let cursor = undefined;
    let pageNum = 1;

    do {
        const url = cursor
            ? `https://api.notion.com/v1/blocks/${blockId}/children?page_size=100&start_cursor=${cursor}`
            : `https://api.notion.com/v1/blocks/${blockId}/children?page_size=100`;

        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${NOTION_API_KEY}`,
                'Notion-Version': '2022-06-28',
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Notion API error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        allBlocks = allBlocks.concat(data.results || []);
        cursor = data.has_more ? data.next_cursor : undefined;

        if (cursor) {
            console.log(`   📄 Page ${pageNum} fetched (${allBlocks.length} blocks so far)...`);
            pageNum++;
        }
    } while (cursor);

    return allBlocks;
}

async function fetchNotionPage() {
    return { results: await fetchAllBlocks(PAGE_ID) };
}

async function fetchTableRows(blockId) {
    let allRows = [];
    let cursor = undefined;

    do {
        const url = cursor
            ? `https://api.notion.com/v1/blocks/${blockId}/children?start_cursor=${cursor}`
            : `https://api.notion.com/v1/blocks/${blockId}/children`;

        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${NOTION_API_KEY}`,
                'Notion-Version': '2022-06-28'
            }
        });

        if (!response.ok) return allRows;
        const data = await response.json();
        allRows = allRows.concat(data.results || []);
        cursor = data.has_more ? data.next_cursor : undefined;
    } while (cursor);

    return allRows;
}

function extractText(richTextArray) {
    if (!richTextArray) return '';
    return richTextArray.map(t => {
        let text = t.plain_text || '';
        // Apply formatting
        if (t.annotations?.bold) text = `**${text}**`;
        if (t.annotations?.italic) text = `*${text}*`;
        if (t.annotations?.code) text = `\`${text}\``;
        if (t.href) text = `[${text}](${t.href})`;
        return text;
    }).join('');
}

async function blockToMarkdown(block, indent = '') {
    const type = block.type;
    let result = '';

    switch (type) {
        case 'heading_1':
            result = `# ${extractText(block.heading_1.rich_text || block.heading_1.text)}\n`;
            break;
        case 'heading_2':
            result = `## ${extractText(block.heading_2.rich_text || block.heading_2.text)}\n`;
            break;
        case 'heading_3':
            result = `### ${extractText(block.heading_3.rich_text || block.heading_3.text)}\n`;
            break;
        case 'paragraph':
            const text = extractText(block.paragraph.rich_text || block.paragraph.text);
            result = text ? `${indent}${text}\n` : '\n';
            break;
        case 'bulleted_list_item':
            result = `${indent}- ${extractText(block.bulleted_list_item.rich_text || block.bulleted_list_item.text)}\n`;
            break;
        case 'numbered_list_item':
            result = `${indent}1. ${extractText(block.numbered_list_item.rich_text || block.numbered_list_item.text)}\n`;
            break;
        case 'to_do':
            const checked = block.to_do.checked ? 'x' : ' ';
            result = `${indent}- [${checked}] ${extractText(block.to_do.rich_text || block.to_do.text)}\n`;
            break;
        case 'code':
            const lang = block.code.language || '';
            const code = extractText(block.code.rich_text || block.code.text);
            result = `\`\`\`${lang}\n${code}\n\`\`\`\n`;
            break;
        case 'divider':
            result = '\n---\n';
            break;
        case 'table':
            // Fetch table rows
            const rows = await fetchTableRows(block.id);
            if (rows.length === 0) return '';

            let tableStr = '\n';
            rows.forEach((row, idx) => {
                const cells = row.table_row?.cells || [];
                const cellTexts = cells.map(cell => extractText(cell) || ' ');
                tableStr += `| ${cellTexts.join(' | ')} |\n`;

                // Add header separator after first row
                if (idx === 0) {
                    tableStr += `| ${cellTexts.map(() => '---').join(' | ')} |\n`;
                }
            });
            result = tableStr + '\n';
            break;
        case 'toggle':
            result = `<details>\n<summary>${extractText(block.toggle.rich_text || block.toggle.text)}</summary>\n`;
            // Fetch toggle children
            if (block.has_children) {
                const children = await fetchAllBlocks(block.id);
                for (const child of children) {
                    result += await blockToMarkdown(child, '  ');
                }
            }
            result += `</details>\n`;
            break;
        case 'quote':
            result = `> ${extractText(block.quote.rich_text || block.quote.text)}\n`;
            break;
        case 'callout':
            const emoji = block.callout.icon?.emoji || '💡';
            result = `> ${emoji} ${extractText(block.callout.rich_text || block.callout.text)}\n`;
            break;
        case 'bookmark':
            const url = block.bookmark?.url || '';
            const caption = extractText(block.bookmark?.caption) || url;
            result = `🔗 [${caption}](${url})\n`;
            break;
        case 'image':
            const imgUrl = block.image?.file?.url || block.image?.external?.url || '';
            const imgCaption = extractText(block.image?.caption) || 'Image';
            result = `![${imgCaption}](${imgUrl})\n`;
            break;
        case 'embed':
            result = `📎 Embed: ${block.embed?.url || ''}\n`;
            break;
        case 'link_preview':
            result = `🔗 ${block.link_preview?.url || ''}\n`;
            break;
        case 'column_list':
            // Fetch columns
            if (block.has_children) {
                const columns = await fetchAllBlocks(block.id);
                for (const col of columns) {
                    if (col.has_children) {
                        const colChildren = await fetchAllBlocks(col.id);
                        for (const child of colChildren) {
                            result += await blockToMarkdown(child, indent);
                        }
                    }
                }
            }
            break;
        default:
            result = '';
    }

    // Handle nested children for blocks that support them
    if (block.has_children && !['toggle', 'table', 'column_list'].includes(type)) {
        const children = await fetchAllBlocks(block.id);
        for (const child of children) {
            result += await blockToMarkdown(child, indent + '  ');
        }
    }

    return result;
}

async function pullFromNotion() {
    console.log('📥 Pulling from Notion...');

    try {
        const data = await fetchNotionPage();
        const blocks = data.results || [];

        let markdown = `<!--
  AUTO-GENERATED from Notion
  Page ID: ${PAGE_ID}
  Last sync: ${new Date().toISOString()}

  Run: npm run notion:pull to refresh
-->\n\n`;

        for (const block of blocks) {
            const md = await blockToMarkdown(block);
            markdown += md;
        }

        // Write to file
        const fs = await import('fs/promises');
        const path = await import('path');
        const outputPath = path.join(process.cwd(), OUTPUT_FILE);

        await fs.writeFile(outputPath, markdown, 'utf8');
        console.log(`✅ Written to ${OUTPUT_FILE}`);
        console.log(`   ${blocks.length} blocks converted`);

    } catch (error) {
        console.error('❌ Error:', error.message);
        process.exit(1);
    }
}

async function pushToNotion() {
    console.log('📤 Push to Notion is not yet implemented');
    console.log('   For now, edit directly in Notion and pull');
    process.exit(0);
}

// Main
const command = process.argv[2] || 'pull';

if (command === 'pull') {
    pullFromNotion();
} else if (command === 'push') {
    pushToNotion();
} else {
    console.log(`
Notion Sync Script

Usage:
  node scripts/sync-notion.mjs pull    # Pull Notion → command_center.md
  node scripts/sync-notion.mjs push    # Push changes to Notion

Or via npm:
  npm run notion:pull
  npm run notion:push
`);
}
