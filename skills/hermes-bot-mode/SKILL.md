---
name: hermes-bot-mode
description: "Complete Bot Mode mastery for Hermes v0.21.0 Pantheon."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [bot-mode, pantheon, v0.21, multi-agent, orchestration]
    related_skills: [hermes-agent, hermes-asi-complete]
    requires_toolsets: [web, memory, skills]
---

# HERMES BOT MODE: Complete v0.21.0 Mastery

Full Bot Mode mastery for Hermes Agent v0.21.0 Pantheon release.

## Bot Roster Management

### Create Bot
```
1. NAME: Unique identifier (kebab-case)
2. TITLE: Role description
3. SOUL.md: Personality and behavior
4. MODEL: Pinned provider/model
5. SKILLS: Enabled skill set
6. TOOLS: Enabled toolsets
7. SCHEDULE: Cron jobs
8. AVATAR: Generated or uploaded
9. GROUP: Assignment to groups
```

### Bot Configuration
- Clone from existing profile
- Skip bundled skills (slim bots)
- Per-skill and per-toolset enablement
- Custom SOUL.md for personality
- Model pinning per bot

### Bot Lifecycle
- Create: name, title, description
- Edit: right-click → Edit Profile
- Hide: right-click → Hide Bot
- Delete: right-click → Delete Profile
- Presence: Active-now strip

## Group Chat Orchestration

### Rules (v0.21.0)
- 2-6 bots per group
- Up to 3 serial rounds
- 10 messages per turn max
- @mentioned bots respond
- @user for escalation
- Room settles when silent round

### Protocol
1. User sends message to group
2. Mentioned bots respond in order
3. Each bot replies briefly or passes
4. Bots pull each other with @name
5. Escalate to user with @user
6. Max 3 rounds, then settle

## Bot-to-Bot Communication

### Message Format
"Message from 🤖 researcher (@researcher): [content]"

### Protocol
1. Each bot has persistent Bot Chat session
2. SOUL.md teaches communication protocol
3. Bots message each other with attribution
4. @name pulls bots into conversation
5. @user escalates to human
6. Context survives like any conversation

## Memory-Backed Cron Jobs

### Configuration
- Standard cron expressions
- Memory-aware scheduling
- Per-bot routines
- Delivery to any platform
- Cost caps and retry

### Protocol
1. DEFINE: What task to run?
2. SCHEDULE: When to run?
3. CONTEXT: What memory/skills to use?
4. DELIVER: Where to send results?
5. MONITOR: Track success/failure
6. OPTIMIZE: Adjust based on results

## Live Subagent Steering

### Capabilities (v0.21.0)
- Monitor subagent progress in real-time
- View live transcripts
- Redirect mid-execution
- Send follow-up messages
- Cancel if needed

### Protocol
1. SPAWN: Launch subagent with task
2. MONITOR: Watch progress via transcript
3. EVALUATE: Is it on track?
4. STEER: Send corrections if needed
5. COLLECT: Gather results when done
6. INTEGRATE: Combine with main work

## Sources
- Hermes Agent v0.21.0 Pantheon Release (August 31, 2026)
- NousResearch/Hermes-Bot-Mode GitHub
- hermes-agent.nousresearch.com/docs/user-guide/bot-mode