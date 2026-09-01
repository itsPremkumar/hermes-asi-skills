---
name: asi-multi-agent
description: "ASI-level multi-agent orchestration and bot coordination."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, multi-agent, orchestration, bot-mode, coordination]
    related_skills: [hermes-agent, asi-master]
    requires_toolsets: [web, memory, skills]
---

# ASI MULTI-AGENT: Bot Orchestration System

Advanced multi-agent coordination for ASI-level teamwork.

## Bot Mode Architecture (v0.21.0 Pantheon)

### Bot Types
```
ORCHESTRATOR: Coordinates team, assigns tasks, monitors progress
RESEARCHER: Gathers and synthesizes information
CODER: Writes and tests code
REVIEWER: Checks work for errors and gaps
VERIFIER: Independently validates conclusions
SYNTHESIZER: Combines multiple outputs into coherent whole
```

### Bot Creation (v0.21.0 Features)
```
1. NAME: Unique identifier
2. TITLE: Role description
3. SOUL.md: Personality and behavior
4. MODEL: Pinned provider/model
5. SKILLS: Enabled skill set
6. TOOLS: Enabled toolsets
7. SCHEDULE: Cron jobs and routines
```

### Group Chat Protocol (v0.21.0)
```
1. User sends message to group
2. @mentioned bots respond (or all if none mentioned)
3. Each bot replies briefly or passes
4. Up to 3 serial rounds of turns
5. Hard cap: 10 messages per turn
6. Room settles when full round stays silent
7. Bots can @user for escalation
```

### Bot-to-Bot Messaging
```
Message from 🤖 researcher (@researcher): [content]
- Each bot has persistent Bot Chat session
- SOUL.md teaches communication protocol
- Bots pull each other with @name
- Escalate to user with @user
```

## Orchestration Protocol

1. DECOMPOSE: Break task into independent sub-tasks
2. ASSIGN: Route to specialist bots
3. EXECUTE: Run 3-5 bots in parallel
4. VERIFY: Gate each result through independent verifier
5. SYNTHESIZE: Combine verified results
6. ITERATE: Re-run failed sub-tasks with feedback

## When to Use
- Complex multi-part tasks
- Parallel workstreams
- Independent verification
- Team coordination