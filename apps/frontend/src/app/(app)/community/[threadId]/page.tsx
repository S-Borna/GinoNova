"use client"

/**
 * ============================================================================
 * THREAD VIEW PAGE — Single Thread Discussion
 * ============================================================================
 *
 * View thread with nested replies, voting, and best answer
 */

import { CATEGORIES, type Reply } from "@/lib/community-types"
import { DiscussionThread } from "@/components/community"

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_THREAD = {
    id: "1",
    title: "How to optimize Docker image size for production?",
    content: `I'm working on a Node.js application and my Docker image is currently 1.2GB, which seems way too large for production.

I'm using the official \`node:18\` base image and installing dependencies with npm. Here's my current Dockerfile:

\`\`\`dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
\`\`\`

What are the best practices for reducing Docker image size? Should I use Alpine? What about multi-stage builds?

Any help would be appreciated!`,
    authorId: "user1",
    author: {
        id: "user1",
        name: "Sarah Chen",
        avatar: "SC",
        reputation: 1250,
    },
    categoryId: "docker",
    category: CATEGORIES.find((c) => c.id === "docker")!,
    tags: ["docker", "optimization", "production"],
    views: 342,
    replyCount: 15,
    upvotes: 24,
    downvotes: 2,
    isPinned: true,
    isLocked: false,
    hasAcceptedAnswer: true,
    createdAt: new Date("2025-01-12T10:30:00"),
    updatedAt: new Date("2025-01-13T15:20:00"),
    lastActivityAt: new Date("2025-01-13T15:20:00"),
}

const MOCK_REPLIES: Reply[] = [
    {
        id: "r1",
        threadId: "1",
        content: `Great question! Here are my top recommendations:

1. **Use Alpine-based images**: Switch from \`node:18\` to \`node:18-alpine\` to reduce base image size from ~900MB to ~170MB

2. **Multi-stage builds**: Separate build and runtime stages

3. **Layer optimization**: Order your Dockerfile commands from least to most frequently changing

Here's an optimized Dockerfile:

\`\`\`dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
EXPOSE 3000
CMD ["node", "dist/index.js"]
\`\`\`

This should get you down to ~200MB or less!`,
        authorId: "user2",
        author: {
            id: "user2",
            name: "Alex Rodriguez",
            avatar: "AR",
            reputation: 2156,
        },
        upvotes: 42,
        downvotes: 1,
        isAccepted: true,
        createdAt: new Date("2025-01-12T11:15:00"),
        updatedAt: new Date("2025-01-12T11:15:00"),
        replies: [
            {
                id: "r1-1",
                threadId: "1",
                content:
                    "This is exactly what I needed! Thank you so much. Just implemented it and my image is now 185MB. Huge improvement! 🎉",
                authorId: "user1",
                author: {
                    id: "user1",
                    name: "Sarah Chen",
                    avatar: "SC",
                    reputation: 1250,
                },
                parentReplyId: "r1",
                upvotes: 8,
                downvotes: 0,
                isAccepted: false,
                createdAt: new Date("2025-01-12T14:30:00"),
                updatedAt: new Date("2025-01-12T14:30:00"),
            },
        ],
    },
    {
        id: "r2",
        threadId: "1",
        content: `Also consider using \`.dockerignore\` file to exclude unnecessary files from your build context:

\`\`\`
node_modules
npm-debug.log
.git
.env
*.md
.vscode
\`\`\`

This can significantly speed up your build process and reduce context size!`,
        authorId: "user3",
        author: {
            id: "user3",
            name: "Mike Johnson",
            avatar: "MJ",
            reputation: 856,
        },
        upvotes: 18,
        downvotes: 0,
        isAccepted: false,
        createdAt: new Date("2025-01-12T12:00:00"),
        updatedAt: new Date("2025-01-12T12:00:00"),
    },
    {
        id: "r3",
        threadId: "1",
        content: `One more tip: Use \`npm ci\` instead of \`npm install\` for cleaner and faster installs in CI/CD pipelines. It uses package-lock.json and ensures reproducible builds.`,
        authorId: "user4",
        author: {
            id: "user4",
            name: "Emma Wilson",
            avatar: "EW",
            reputation: 423,
        },
        upvotes: 12,
        downvotes: 0,
        isAccepted: false,
        createdAt: new Date("2025-01-13T09:15:00"),
        updatedAt: new Date("2025-01-13T09:15:00"),
    },
]

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function ThreadPage({ params }: { params: { threadId: string } }) {
    const thread = MOCK_THREAD
    const replies = MOCK_REPLIES

    const handleReply = (replyId: string, content: string) => {
    }

    const handleVote = (
        targetType: "thread" | "reply",
        targetId: string,
        voteType: "up" | "down"
    ) => {
    }

    const handleAcceptAnswer = (replyId: string) => {
    }

    const handleDelete = (targetType: "thread" | "reply", targetId: string) => {
    }

    return (
        <DiscussionThread
            thread={thread}
            replies={replies}
            currentUserId="user1"
            onReply={handleReply}
            onVote={handleVote}
            onAcceptAnswer={handleAcceptAnswer}
            onDelete={handleDelete}
        />
    )
}
