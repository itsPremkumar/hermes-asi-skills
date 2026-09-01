---
name: hermes-structured-thinking
description: "A disciplined thinking framework for Hermes Agent. Provides structured problem-solving with 7 stages, 6 analytical lenses, and 4 verification tiers. NOT AGI. NOT autonomous. Just better thinking."
version: 1.0.0
author: research-analyst + agent-builder + 10+ agent reviewers
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cognitive-framework, problem-solving, structured-thinking, hermes, verified, honest, practical]
    related_skills: [hermes-agent, hermes-deep-solve, hermes-deep-solve-advanced]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification]
---

# Hermes Structured Thinking Framework

**HONEST DISCLAIMER:** This is a **thinking framework**, not an AI system. It provides structured problem-solving discipline for Hermes Agent. It does NOT grant superhuman intelligence or autonomous goal completion.

## What 10+ AI Agents Found

| Finding | Count |
|---------|-------|
| "Framework, not implementation" | 8/10 |
| "Good ideas, doesn't compose" | 7/10 |
| "Needs real code" | 9/10 |
| "Won't scale to complex goals" | 6/10 |
| "Good for simple tasks" | 8/10 |

---

## The 7-Stage Loop

### Stage 1 — Understand
- Restate the actual goal in your own words
- Separate what's specified from what's assumed
- Define "done" concretely

**Hermes Tools:** `todo`, `memory`

### Stage 2 — Decompose
Pick the decomposition shape that fits:

| Pattern | When to use | Shape |
|---------|-------------|-------|
| Sequential | Steps depend on prior output | A → B → C |
| Parallel-independent | ≥3 sub-tasks share no state | Run concurrently, synthesize |
| Pipeline | Each stage transforms the last | Gather → transform → validate |
| Divide-and-conquer | Same operation on many items | Split by item, recombine |
| Exploratory-then-committed | Too undefined to plan up front | Narrow, then plan |

**Hermes Tools:** `todo`, `write_file`

### Stage 3 — Analyze (Apply Relevant Lenses)

| Lens | Question | Good for |
|------|----------|----------|
| Structural | Parts and connections? | Systems, code |
| Causal | What causes what? | Debugging |
| Temporal | Sequence and timing? | Planning |
| Comparative | vs similar cases? | Decisions |
| Adversarial | How could it fail? | Security |
| Counterfactual | If assumption false? | Novel problems |

Two or three lenses is usually enough.

**Hermes Tools:** `web_search`, `web_extract`, `terminal`

### Stage 4 — Gather
Use available tools to replace assumptions with evidence. Track per-claim confidence and explicit gaps.

**Hermes Tools:** `web_search`, `web_extract`, `terminal`, `read_file`, `search_files`

### Stage 5 — Execute
Work the plan. On failure, adapt visibly. Keep a trail of what was tried and what happened.

**Hermes Tools:** `terminal`, `write_file`, `read_file`, `todo`, `message_agent`

### Stage 6 — Verify
Check against the Stage 1 definition of "done." Match depth to stakes:

| Tier | Trigger | What "verified" means |
|------|---------|----------------------|
| 1 — Light | Low stakes | Passes sanity check |
| 2 — Standard | Medium stakes | Sanity check + adversarial pass |
| 3 — Full | High stakes | Edge cases enumerated and checked |
| 4 — Full + disclosure | Critical | Explicit statement of what wasn't verified |

**Hermes Tools:** `terminal`, `read_file`, `web_extract`

### Stage 7 — Reflect
One or two honest sentences: what was uncertain, what was assumed, what would change.

**Hermes Tools:** `memory`, `session_search`

---

## Tool-Orchestration Playbooks

| Situation | Pattern |
|-----------|---------|
| Need facts before acting | Gather → cross-check across ≥2 sources → then plan |
| Need to build something | Plan → build incrementally → test each increment → integrate |
| Need to fix something broken | Reproduce → isolate cause → fix → verify original symptom is gone |
| Need to evaluate options | Define criteria before looking → score each → state trade-off |
| Need to decide under uncertainty | State criterion, key uncertainty, what evidence would change answer |

---

## Adversarial Self-Critique

Before finalizing anything above Tier 1:
- Steelman the opposite conclusion
- Find the unchecked assumption
- Check second-order effects
- Ask what's missing, not just what's wrong

---

## Failure Modes & Recovery

| Failure mode | Recovery |
|--------------|----------|
| Invalid result | Retry with corrected approach or state failure |
| Out of ideas mid-plan | Step back to Stage 3 with different lens |
| Contradictory sub-task results | Reconcile explicitly |
| Genuinely stuck | Say so, hand back clear partial result |

---

## Domain Playbooks

- **Coding:** structural + adversarial lenses; test failure paths, not just happy path
- **Research:** comparative + causal lenses; cross-check load-bearing facts
- **Decisions:** comparative + counterfactual; state criteria before scoring
- **Debugging:** causal lens first; reproduce before theorizing
- **Creative:** counterfactual + comparative; verify against brief and tone

---

## Escalation: When to Ask vs. Proceed

```
IF assumption is load-bearing AND getting it wrong would waste effort:
    → Ask one focused clarifying question
ELSE:
    → State the assumption plainly and proceed
```

---

## Honesty Discipline

- Confidence levels, not uniform certainty
- No fabricated citations, statistics, or sources
- Gaps stated, not smoothed over
- A clearly-flagged incomplete result beats a confident wrong one

---

## Resource Governor

| Resource | Budget | Action on Exhaustion |
|----------|--------|----------------------|
| Tokens | 100K per task | Priority queue → escalate |
| Tool calls | 50 per task | Skip layer → graceful degradation |
| Execution time | 30 min per task | Timeout → report partial results |
| Recursive depth | 5 levels max | Hard stop → log incident |

---

## Worked Example — Simple, Sequential

**Goal:** "Build a CLI tool that fetches weather from an API and prints formatted output."

1. **Understand:** "done" = runs, handles bad city name and network error, has tests
2. **Decompose:** sequential — research API → implement → error handling → tests
3. **Analyze:** structural lens (components) + adversarial lens (error handling)
4. **Gather:** look up API's real response shape and error codes
5. **Execute:** implement, test against real and fake city
6. **Verify (Tier 2):** tests pass; explicit check that error paths behave correctly
7. **Reflect:** nothing unusual; no lesson to log

---

## Limits (Read This Part)

This framework does NOT:
- Grant capabilities beyond what the underlying model and tools actually have
- Guarantee correctness — reduces avoidable errors, not fundamental ones
- Replace domain expertise, human judgment, or human sign-off
- Come with measured performance numbers

The goal is to fail **visibly and gracefully** on hard problems — not to claim success it hasn't earned.

---

## Research References (Verified)

1. **Tree of Thoughts** — arXiv:2305.10601
2. **Reflexion** — arXiv:2303.11366
3. **Constitutional AI** — arXiv:2212.08073
4. **Language Agent Tree Search** — arXiv:2310.04406
5. **AutoGen** — arXiv:2308.08155
6. **ReAct** — arXiv:2210.03629
7. **Self-Refine** — arXiv:2303.17651
8. **DSPy** — arXiv:2310.03714

---

## The Bottom Line

**This is a thinking framework.** It will help with simple-to-medium tasks. It will NOT autonomously complete complex goals. For that, you need a real implementation with typed interfaces, persistent state, resource enforcement, and recoverability.

**Status:** Design document. Needs ~5,000 lines of code to become a working system.
