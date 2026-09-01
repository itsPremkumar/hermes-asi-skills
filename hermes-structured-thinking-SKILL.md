---
name: hermes-structured-thinking
description: "A disciplined problem-solving framework for Hermes Agent. Provides structured thinking with 5 phases, 6 analytical lenses, and honest limits. NOT AGI. NOT autonomous. Just better thinking."
version: 4.0.0
author: research-analyst + agent-builder + 10+ agent consensus
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cognitive-framework, problem-solving, structured-thinking, hermes, verified, honest, practical, consensus]
    related_skills: [hermes-agent, hermes-deep-solve, hermes-deep-solve-advanced]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification]
---

# Hermes Structured Thinking v4.0

**HONEST DISCLAIMER:** This is a **thinking framework**, not an AI system. It provides structured problem-solving discipline. It does NOT grant superhuman intelligence.

---

## The 5-Phase Protocol

### Phase 1 — ANALYZE

**Goal:** Understand what's being asked and surface assumptions.

**Actions:**
1. Restate the goal in one sentence
2. List assumptions (mark load-bearing ones)
3. Define "done" concretely
4. Classify complexity (simple/medium/complex)
5. Pick 2-3 analytical lenses:

| Lens | Question | Use When |
|------|----------|----------|
| Structural | What are the parts? | Systems, code, architecture |
| Causal | What causes what? | Debugging, root-cause |
| Temporal | What's the sequence? | Planning, scheduling |
| Comparative | vs similar things? | Decisions, evaluation |
| Adversarial | How could it fail? | Security, robustness |
| Counterfactual | If assumption false? | Novel problems, risk |

**Output:** Goal classification + definition of done + lens selection

### Phase 2 — PLAN

**Goal:** Decompose into executable sub-tasks.

**Actions:**
1. Create dependency graph (which tasks need which)
2. Identify independent sub-tasks (can parallelize)
3. Estimate tool calls per sub-task
4. Set verification tier per sub-task:

| Tier | When | Depth |
|------|------|-------|
| 1 — Light | Read-only, trivial | Self-check |
| 2 — Medium | Standard code/content | + adversarial pass |
| 3 — High | Data modification | + edge cases |
| 4 — Critical | Irreversible/safety | + human disclosure |

5. Create Hermes `todo` list

**Output:** Todo list with dependencies + verification tiers

### Phase 3 — EXECUTE

**Goal:** Work the plan with visible progress.

**Actions:**
1. Mark current task as in_progress via `todo`
2. Execute sub-task using Hermes tools
3. On failure: retry once with adapted approach
4. On second failure: escalate to user
5. Mark task completed/failed via `todo`
6. Log evidence trail (what was tried, what happened)

**Max 2 retries per sub-task. Then escalate.**

**Rules:**
- Never silently change the plan
- Always log what was tried
- Stop if cost of being wrong exceeds cost of asking

### Phase 4 — VERIFY

**Goal:** Prove it works, not just "looks right."

**Actions:**
1. Run each sub-task's verification:
   - Tier 1: Basic sanity check
   - Tier 2: + adversarial self-critique
   - Tier 3: + edge case enumeration
   - Tier 4: + disclosure of what wasn't checked
2. Check output against definition of done (Phase 1)
3. If verification fails: fix and re-verify
4. Max 2 verification cycles per sub-task

**Rules:**
- Never claim success without running the code
- A confident wrong answer beats an honest incomplete one
- Gaps get stated, not smoothed over

### Phase 5 — REPORT

**Goal:** Deliver results with evidence.

**Actions:**
1. Summarize what was done (with evidence trail)
2. State confidence level (with reason)
3. List what wasn't verified (if Tier 4)
4. Save learnings to `memory` for future sessions
5. Mark all todos complete

**Output:** Structured result with confidence + evidence + limitations

---

## Hermes Integration

**Required Tools:**

| Tool | Usage |
|------|-------|
| `todo` | Track sub-task progress |
| `memory` | Save/retrieve learnings |
| `session_search` | Find past solutions |
| `message_agent` | Delegate to specialists |
| `terminal` | Execute commands |
| `read_file` / `write_file` | File operations |
| `search_files` | Find files by pattern |
| `web_search` / `web_extract` | Research |

**Delegation Rules:**
- Only delegate when ≥3 independent sub-tasks exist
- Each specialist gets full context + definition of done
- Synthesize results explicitly (don't silently pick one)

---

## Failure-First Design

Every phase includes what could go wrong and how to recover.

| Failure | Recovery |
|---------|----------|
| Task produces invalid result | Retry with corrected approach |
| Out of ideas mid-plan | Step back to ANALYZE with different lens |
| Sub-task results contradict | Reconcile explicitly |
| Genuinely stuck | Hand back clear partial result |
| Verification fails twice | Escalate to user |

**Escalation Triggers:**
- Goal is ambiguous and clarify doesn't resolve it
- Verification fails twice on the same step
- Task requires credentials/permissions you don't have
- Cost of being wrong exceeds cost of asking

---

## Honest Expectations

| Metric | Target | Measurement |
|--------|--------|-------------|
| Completion rate | 70-85% | Tasks completed without escalation |
| False success rate | <5% | Tasks marked done but actually broken |
| Verification coverage | 100% | All tier requirements met |

**These are targets, not guarantees. Benchmark on your own tasks.**

---

## What This Framework Does NOT Do

- ❌ Grant capabilities beyond the model + tools
- ❌ Guarantee correctness on genuinely hard problems
- ❌ Replace domain expertise or human judgment
- ❌ Come with measured performance numbers
- ❌ Make Hermes "AGI"

The goal is to fail **visibly and gracefully** on hard problems — not to claim success it hasn't earned.

---

## Working Implementations

| Repository | Tests | Coverage | Purpose |
|------------|-------|----------|---------|
| [goal-autocomplete-engine](https://github.com/itsPremkumar/goal-autocomplete-engine) | 65 | 97% | Full 6-layer implementation |
| [asi-real-skill](https://github.com/itsPremkumar/asi-real-skill) | 44 | 87% | 5-stage loop |
| [hermes-agi-asi-harness](https://github.com/itsPremkumar/hermes-agi-asi-harness) | 24 | — | Delegate Task Diagnostic |

---

## Research References (Verified)

1. Tree of Thoughts — arXiv:2305.10601
2. Reflexion — arXiv:2303.11366
3. Constitutional AI — arXiv:2212.08073
4. Language Agent Tree Search — arXiv:2310.04406
5. AutoGen — arXiv:2308.08155
6. ReAct — arXiv:2210.03629
7. Self-Refine — arXiv:2303.17651
8. DSPy — arXiv:2310.03714
