---
name: asi-planning
description: "ASI-level hierarchical planning and goal decomposition."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, planning, goal-decomposition, hierarchical, replanning]
    related_skills: [hermes-agent, asi-master]
    requires_toolsets: [web, memory, skills]
---

# ASI PLANNING: Hierarchical Planning System

Advanced planning system for ASI-level goal achievement.

## Planning Hierarchy

```
LEVEL 1: MISSION (Ultimate Objective)
  └── LEVEL 2: GOALS (Major Milestones)
       └── LEVEL 3: SUBGOALS (Specific Achievements)
            └── LEVEL 4: TASKS (Concrete Actions)
                 └── LEVEL 5: OPERATIONS (Tool Calls)
```

## Planning Protocol

1. DEFINE: What is the mission?
2. DECOMPOSE: Break into goals, subgoals, tasks
3. PRIORITIZE: What order? What dependencies?
4. ALLOCATE: Resources, time, tools
5. EXECUTE: Follow plan
6. MONITOR: Track progress
7. REPLAN: Adapt when blocked

## Dynamic Replanning

```
IF blocked:
  IDENTIFY blocker
  GENERATE alternatives
  EVALUATE options
  SELECT best alternative
  UPDATE plan
  CONTINUE execution
```

## When to Use
- Long-horizon tasks
- Multi-step projects
- Complex goals
- Resource allocation