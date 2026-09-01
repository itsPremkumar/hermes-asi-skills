---
name: hermes-structured-thinking
description: "A disciplined thinking framework for Hermes Agent. Provides structured problem-solving with 5 stages, 6 analytical lenses, and 4 verification tiers. NOT AGI. NOT autonomous. Just better thinking."
version: 2.0.0
author: research-analyst + agent-builder + 10+ agent consensus
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cognitive-framework, problem-solving, structured-thinking, hermes, verified, honest, practical, consensus]
    related_skills: [hermes-agent, hermes-deep-solve, hermes-deep-solve-advanced]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification]
---

# Hermes Structured Thinking Framework v2.0

**HONEST DISCLAIMER:** This is a **thinking framework**, not an AI system. It provides structured problem-solving discipline for Hermes Agent. It does NOT grant superhuman intelligence or autonomous goal completion.

## What 10+ AI Agents Agreed On

| Principle | Consensus |
|-----------|-----------|
| Name | hermes-structured-thinking (not asi-finalized) |
| Nature | Framework, not AI system |
| Claims | No AGI/ASI claims |
| Citations | Verified only |
| Implementation | Needs real code |
| Honesty | Confidence levels, not certainty |

---

## Complexity Gate

```
IF task is simple (< 300 lines, single domain):
    → Use Fast Path: Plan → Execute → Test

ELSE IF task is complex (multi-step, ambiguous, high-stakes):
    → Use Full 5-Stage Loop

ELSE IF task is critical (irreversible, safety-relevant):
    → Use Full Loop + Tier 4 Verification + Human Approval
```

### Fast Path (Simple Tasks)

For tasks under ~300 lines or single-domain work:

1. **Plan** — Decompose into tasks
2. **Execute** — Build incrementally
3. **Test** — Verify it works

Skip: Analytical lenses, adversarial critique, extensive documentation.

### Full 5-Stage Loop (Complex Tasks)

#### Stage 1 — Understand
- Restate the actual goal in your own words
- Separate what's specified from what's assumed
- Define "done" concretely

#### Stage 2 — Plan + Analyze
- Decompose into subgoals and tasks
- Pick a decomposition shape (sequential, parallel, pipeline)
- Apply 2-3 analytical lenses:

| Lens | Question | Good for |
|------|----------|----------|
| Structural | Parts and connections? | Systems, code |
| Causal | What causes what? | Debugging |
| Temporal | Sequence and timing? | Planning |
| Comparative | vs similar cases? | Decisions |
| Adversarial | How could it fail? | Security |
| Counterfactual | If assumption false? | Novel problems |

#### Stage 3 — Gather + Execute
- Replace assumptions with evidence
- Work the plan, adapt visibly on failure
- Keep a trail of what was tried

#### Stage 4 — Verify
Match depth to stakes:

| Tier | Trigger | Depth |
|------|---------|-------|
| 1 — Light | Low stakes | Self-check |
| 2 — Standard | Medium stakes | + adversarial pass |
| 3 — Full | High stakes | + edge cases |
| 4 — Critical | Irreversible | + disclosure + human approval |

**Tier Selection Rule:**
- Read-only queries → Tier 1
- Standard code/content → Tier 2
- Data modification → Tier 3
- Irreversible/safety → Tier 4

#### Stage 5 — Reflect
- One or two honest sentences
- What was uncertain, what to learn
- Skip if nothing to say

---

## Adversarial Self-Critique

Run **once** before finalizing. Fix issues found. If none found, say so briefly.

- Steelman the opposite conclusion
- Find unchecked assumptions
- Check second-order effects

---

## Decomposition Patterns

| Pattern | When to use | Shape |
|---------|-------------|-------|
| Sequential | Steps depend on prior output | A → B → C |
| Parallel-independent | ≥3 sub-tasks share no state | Run concurrently |
| Pipeline | Each stage transforms the last | Gather → transform → validate |
| Divide-and-conquer | Same operation on many items | Split by item, recombine |
| Exploratory-then-committed | Too undefined to plan up front | Narrow, then plan |

---

## Failure Modes & Recovery

| Failure mode | Recovery |
|--------------|----------|
| Invalid result | Retry or state failure |
| Out of ideas | Step back with different lens |
| Contradictory results | Reconcile explicitly |
| Genuinely stuck | Hand back clear partial result |

---

## Honesty Discipline

- Confidence levels, not uniform certainty
- No fabricated citations, statistics, or sources
- Gaps stated, not smoothed over
- A clearly-flagged incomplete result beats a confident wrong one
- **"I don't know" is always a valid answer**

---

## Escalation: When to Ask vs. Proceed

```
IF assumption is load-bearing AND getting it wrong would waste effort:
    → Ask one focused clarifying question
ELSE:
    → State the assumption plainly and proceed
```

---

## Domain Playbooks

- **Coding:** structural + adversarial; test failure paths
- **Research:** comparative + causal; cross-check facts
- **Decisions:** comparative + counterfactual; state criteria first
- **Debugging:** causal first; reproduce before theorizing
- **Creative:** counterfactual + comparative; verify against brief

---

## Worked Example — Simple CLI Tool

**Goal:** "Build a CLI that fetches weather from wttr.in"

**Fast Path used** (task < 300 lines):

1. **Plan:** research API → implement → test
2. **Execute:** write code, run it
3. **Test:** pytest + manual check

**Result:** Production-ready tool, 24 tests, 632 lines.

---

## Worked Example — Complex Task

**Goal:** "Evaluate 3 database migration strategies for production"

**Full 5-stage loop:**

1. **Understand:** Recommendation with trade-offs, not just preference
2. **Plan:** Parallel-independent (each strategy analyzed separately)
3. **Analyze:** Comparative + counterfactual + adversarial lenses
4. **Gather:** Find real precedent for each strategy
5. **Execute:** Score against criteria defined before looking at options
6. **Verify (Tier 3):** Enumerate failure modes of recommended strategy
7. **Reflect:** Recommendation conditional on downtime assumption

---

## Limits (Read This Part)

This framework does NOT:
- Grant capabilities beyond what the underlying model and tools actually have
- Guarantee correctness — reduces avoidable errors, not fundamental ones
- Replace domain expertise, human judgment, or human sign-off
- Come with measured performance numbers
- Integrate with Hermes tools automatically

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

**This is a thinking framework.** It will help with simple-to-medium tasks. It will NOT autonomously complete complex goals.

**Status:** Design document. Needs ~5,000 lines of code + Hermes tool integration to become a working system.

**Consensus:** Accepted by 10+ AI agents after iterative review.
