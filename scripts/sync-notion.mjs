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
    console.log('📤 Pushing to Notion...');

    try {
        const fs = await import('fs/promises');
        const path = await import('path');
        const inputPath = path.join(process.cwd(), OUTPUT_FILE);

        // Read the markdown file
        const markdown = await fs.readFile(inputPath, 'utf8');

        // Remove the auto-generated header comment
        const content = markdown.replace(/<!--[\s\S]*?-->\n*/, '').trim();

        // Parse markdown to Notion blocks
        const blocks = markdownToNotionBlocks(content);

        console.log(`   📄 Parsed ${blocks.length} blocks from markdown`);

        // First, get existing blocks and delete them
        console.log('   🗑️  Clearing existing page content...');
        const existingBlocks = await fetchAllBlocks(PAGE_ID);
        console.log(`   Found ${existingBlocks.length} existing blocks to delete`);

        // Delete in batches with rate limiting
        for (let i = 0; i < existingBlocks.length; i++) {
            const block = existingBlocks[i];
            try {
                await fetch(`https://api.notion.com/v1/blocks/${block.id}`, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Bearer ${NOTION_API_KEY}`,
                        'Notion-Version': '2022-06-28'
                    }
                });
                // Rate limiting - wait 100ms between deletes
                if (i % 10 === 0) {
                    await new Promise(r => setTimeout(r, 100));
                }
            } catch (e) {
                console.log(`   ⚠️  Failed to delete block ${i}: ${e.message}`);
            }
        }
        console.log('   ✓ Cleared existing content');

        // Wait a moment before uploading
        await new Promise(r => setTimeout(r, 500));

        // Append new blocks in smaller chunks (50 instead of 100 for stability)
        console.log('   📝 Uploading new content...');
        const chunkSize = 50;
        let successfulBlocks = 0;

        for (let i = 0; i < blocks.length; i += chunkSize) {
            const chunk = blocks.slice(i, i + chunkSize);

            try {
                const response = await fetch(`https://api.notion.com/v1/blocks/${PAGE_ID}/children`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${NOTION_API_KEY}`,
                        'Notion-Version': '2022-06-28',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ children: chunk })
                });

                if (!response.ok) {
                    const error = await response.json();
                    console.error(`   ❌ Error uploading blocks ${i + 1}-${Math.min(i + chunkSize, blocks.length)}:`);
                    console.error(`      Status: ${response.status}`);
                    console.error(`      Message: ${JSON.stringify(error).substring(0, 200)}`);
                    
                    // Try to continue with remaining blocks
                    continue;
                }

                successfulBlocks += chunk.length;
                console.log(`   ✓ Uploaded blocks ${i + 1}-${Math.min(i + chunkSize, blocks.length)} (${successfulBlocks}/${blocks.length})`);

                // Rate limiting - wait 300ms between uploads
                await new Promise(r => setTimeout(r, 300));

            } catch (error) {
                console.error(`   ❌ Network error at blocks ${i + 1}-${Math.min(i + chunkSize, blocks.length)}: ${error.message}`);
            }
        }

        console.log(`\n✅ Push complete!`);
        console.log(`   Successfully uploaded: ${successfulBlocks}/${blocks.length} blocks`);
        console.log(`   Page: https://notion.so/${PAGE_ID.replace(/-/g, '')}`);

    } catch (error) {
        console.error('❌ Error:', error.message);
        process.exit(1);
    }
}

function markdownToNotionBlocks(markdown) {
    const blocks = [];
    const lines = markdown.split('\n');
    let i = 0;

    while (i < lines.length) {
        const line = lines[i];

        // Skip empty lines
        if (!line.trim()) {
            i++;
            continue;
        }

        // Headings
        if (line.startsWith('# ')) {
            blocks.push(createHeading1(line.substring(2).trim()));
            i++;
            continue;
        }
        if (line.startsWith('## ')) {
            blocks.push(createHeading2(line.substring(3).trim()));
            i++;
            continue;
        }
        if (line.startsWith('### ')) {
            blocks.push(createHeading3(line.substring(4).trim()));
            i++;
            continue;
        }

        // Horizontal rule
        if (line.trim() === '---') {
            blocks.push({ type: 'divider', divider: {} });
            i++;
            continue;
        }

        // Code blocks
        if (line.startsWith('```')) {
            const lang = line.substring(3).trim() || 'plain text';
            let code = '';
            i++;
            while (i < lines.length && !lines[i].startsWith('```')) {
                code += (code ? '\n' : '') + lines[i];
                i++;
            }
            blocks.push(createCodeBlock(code, lang));
            i++; // Skip closing ```
            continue;
        }

        // Tables
        if (line.includes('|') && line.trim().startsWith('|')) {
            const tableRows = [];
            while (i < lines.length && lines[i].includes('|')) {
                const row = lines[i].trim();
                // Skip separator row (| --- | --- |)
                if (!row.match(/^\|[\s-:|]+\|$/)) {
                    const cells = row.split('|').filter(c => c.trim()).map(c => c.trim());
                    tableRows.push(cells);
                }
                i++;
            }
            if (tableRows.length > 0) {
                blocks.push(createTable(tableRows));
            }
            continue;
        }

        // Bullet list
        if (line.match(/^[-*]\s/)) {
            blocks.push(createBulletItem(line.replace(/^[-*]\s/, '').trim()));
            i++;
            continue;
        }

        // Numbered list
        if (line.match(/^\d+\.\s/)) {
            blocks.push(createNumberedItem(line.replace(/^\d+\.\s/, '').trim()));
            i++;
            continue;
        }

        // Checkbox / todo
        if (line.match(/^-\s*\[[ x]\]/i)) {
            const checked = line.match(/\[x\]/i) !== null;
            const text = line.replace(/^-\s*\[[ x]\]\s*/i, '').trim();
            blocks.push(createTodo(text, checked));
            i++;
            continue;
        }

        // Quote
        if (line.startsWith('> ')) {
            blocks.push(createQuote(line.substring(2).trim()));
            i++;
            continue;
        }

        // Regular paragraph
        blocks.push(createParagraph(line.trim()));
        i++;
    }

    return blocks;
}

function parseRichText(text) {
    const richText = [];
    // Simple parser - handle bold, italic, code, links
    const regex = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\)|[^*`\[]+)/g;
    let match;

    while ((match = regex.exec(text)) !== null) {
        let segment = match[1];
        let annotations = { bold: false, italic: false, code: false };
        let href = null;

        // Bold
        if (segment.startsWith('**') && segment.endsWith('**')) {
            segment = segment.slice(2, -2);
            annotations.bold = true;
        }
        // Italic
        else if (segment.startsWith('*') && segment.endsWith('*')) {
            segment = segment.slice(1, -1);
            annotations.italic = true;
        }
        // Code
        else if (segment.startsWith('`') && segment.endsWith('`')) {
            segment = segment.slice(1, -1);
            annotations.code = true;
        }
        // Link
        else if (segment.match(/^\[([^\]]+)\]\(([^)]+)\)$/)) {
            const linkMatch = segment.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
            segment = linkMatch[1];
            href = linkMatch[2];
        }

        if (segment) {
            const textObj = {
                type: 'text',
                text: { content: segment }
            };
            if (href) {
                textObj.text.link = { url: href };
            }
            if (annotations.bold || annotations.italic || annotations.code) {
                textObj.annotations = annotations;
            }
            richText.push(textObj);
        }
    }

    // Fallback if regex didn't match anything
    if (richText.length === 0 && text) {
        richText.push({ type: 'text', text: { content: text } });
    }

    return richText;
}

function createHeading1(text) {
    return {
        type: 'heading_1',
        heading_1: { rich_text: parseRichText(text) }
    };
}

function createHeading2(text) {
    return {
        type: 'heading_2',
        heading_2: { rich_text: parseRichText(text) }
    };
}

function createHeading3(text) {
    return {
        type: 'heading_3',
        heading_3: { rich_text: parseRichText(text) }
    };
}

function createParagraph(text) {
    return {
        type: 'paragraph',
        paragraph: { rich_text: parseRichText(text) }
    };
}

function createBulletItem(text) {
    return {
        type: 'bulleted_list_item',
        bulleted_list_item: { rich_text: parseRichText(text) }
    };
}

function createNumberedItem(text) {
    return {
        type: 'numbered_list_item',
        numbered_list_item: { rich_text: parseRichText(text) }
    };
}

function createTodo(text, checked) {
    return {
        type: 'to_do',
        to_do: { rich_text: parseRichText(text), checked }
    };
}

function createQuote(text) {
    return {
        type: 'quote',
        quote: { rich_text: parseRichText(text) }
    };
}

function createCodeBlock(code, language) {
    // Map common language names to Notion's supported languages
    const langMap = {
        'js': 'javascript',
        'ts': 'typescript',
        'py': 'python',
        'sh': 'bash',
        'shell': 'bash',
        'yml': 'yaml',
        'md': 'markdown',
        'json': 'json',
        'text': 'plain text',
        'txt': 'plain text',
        'plain': 'plain text',
        '': 'plain text'
    };
    
    // Notion's valid language list
    const validLangs = [
        'abap', 'agda', 'arduino', 'assembly', 'bash', 'basic', 'bnf', 'c', 'c#', 'c++',
        'clojure', 'coffeescript', 'coq', 'css', 'dart', 'dhall', 'diff', 'docker',
        'ebnf', 'elixir', 'elm', 'erlang', 'f#', 'flow', 'fortran', 'gherkin', 'glsl',
        'go', 'graphql', 'groovy', 'haskell', 'html', 'idris', 'java', 'javascript',
        'json', 'julia', 'kotlin', 'latex', 'less', 'lisp', 'livescript', 'llvm ir',
        'lua', 'makefile', 'markdown', 'markup', 'matlab', 'mathematica', 'mermaid',
        'nix', 'objective-c', 'ocaml', 'pascal', 'perl', 'php', 'plain text',
        'powershell', 'prolog', 'protobuf', 'python', 'r', 'reason', 'ruby', 'rust',
        'sass', 'scala', 'scheme', 'scss', 'shell', 'solidity', 'sql', 'swift',
        'toml', 'typescript', 'vb.net', 'verilog', 'vhdl', 'visual basic', 'webassembly',
        'xml', 'yaml', 'java/c/c++/c#'
    ];
    
    let notionLang = langMap[language.toLowerCase()] || language.toLowerCase() || 'plain text';
    
    // If language isn't valid, default to plain text
    if (!validLangs.includes(notionLang)) {
        notionLang = 'plain text';
    }

    return {
        type: 'code',
        code: {
            rich_text: [{ type: 'text', text: { content: code } }],
            language: notionLang
        }
    };
}

function createTable(rows) {
    const tableWidth = rows[0]?.length || 1;

    return {
        type: 'table',
        table: {
            table_width: tableWidth,
            has_column_header: true,
            has_row_header: false,
            children: rows.map(row => ({
                type: 'table_row',
                table_row: {
                    cells: row.map(cell => parseRichText(cell))
                }
            }))
        }
    };
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
