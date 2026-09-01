---
name: asi-hermes-pantheon
description: "ASI-level Hermes v0.21.0 Pantheon release features."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, hermes, pantheon, v0.21, bot-mode, features]
    related_skills: [hermes-agent, asi-master]
    requires_toolsets: [web, memory, skills]
---

# ASI HERMES PANTHEON: v0.21.0 Feature Mastery

Complete feature set from Hermes Agent v0.21.0 Pantheon release.

## Pantheon Release Features

### 1. Bot Mode (Built-in)
- Roster of named bots
- Each bot = full Hermes profile
- Own chat, memory, skills, model
- Bot-to-bot messaging
- Group chats (2-6 bots)
- Active-now presence strip

### 2. Bot-to-Bot Direct Messages
```
Message from 🤖 researcher (@researcher): [content]
- Persistent Bot Chat session per bot
- SOUL.md teaches communication protocol
- @name pulls bots into conversation
- @user escalates to human
```

### 3. Memory-Backed Cron Jobs
- Recurring automated tasks
- Memory-aware scheduling
- Per-bot routines
- Delivery to any platform

### 4. Live Subagent Steering
- Monitor subagent progress in real-time
- Redirect mid-execution
- View live transcripts
- Interactive control

### 5. MCP Command Center
- Expanded MCP server catalog
- Interactive picker
- mTLS for HTTP/SSE servers
- OAuth 2.1 support

### 6. Browser Control In-App
- Built-in browser automation
- No external tools needed
- Integrated with agent loop

### 7. New Providers & Models
- Fireworks AI
- DeepInfra
- Upstage Solar
- Expanded model catalog

### 8. Security Hardening
- Smart approvals (independent LLM reviewer)
- Supply-chain audit (OSV.dev)
- Prompt injection defenses
- Credential redaction

## Bot Mode Configuration

### Create Bot
```
1. NAME: Unique identifier
2. TITLE: Role description
3. SOUL.md: Personality and behavior
4. MODEL: Pinned provider/model
5. SKILLS: Enabled skill set
6. TOOLS: Enabled toolsets
7. SCHEDULE: Cron jobs
```

### Group Chat Rules
```
- 2-6 bots per group
- Up to 3 serial rounds
- 10 messages per turn max
- @mentioned bots respond
- @user for escalation
- Room settles when silent round
```

## When to Use
- Multi-agent workflows
- Automated team coordination
- Complex task delegation
- 24/7 operation