---
name: asi-finalized
description: "Finalized ASI cognitive architecture — practical, tested, honest framework for autonomous goal completion. Not AGI claims, just disciplined problem-solving."
version: 11.0.0
author: research-analyst + agent-builder + agent-architect + cto + security-engineer + hermes-asi-bot + prompt-engineer + sample + qa-lead + hermes-sovereign-master + tech-lead + full community review
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, AGI, recursive-self-improvement, meta-learning, self-evolution, superintelligence, unified, hermes, goal-autocomplete, finalized, production, v11, secure, verified, executable, practical, honest, tested]
    related_skills: [hermes-agent, deep-research, super-hermes, hermes-self-evolution, asi-master, asi-ultra, asi-ultimate, arc-agi-3-master, hermes-asi-complete, hermes-deep-solve]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification, security, bot-mode, mcp]
---

# ASI-FINALIZED v11: Practical Autonomous Goal Completion

This is the **practical, tested, honest** ASI cognitive system. Version 11 strips away the "architecture astronautics" and focuses on what actually works: disciplined problem-solving with visible failure modes. It combines the best of ASI-FINALIZED with the hermes-deep-solve framework's honesty and practicality.

## What This Is

A structured framework for tackling hard problems carefully — decompose, gather evidence, act, check your own work, and say honestly where you're unsure.

## What This Is Not

A mechanism for "AGI" or "ASI." No prompt grants capabilities the underlying model doesn't have. This framework doesn't expand what's actually possible — it reduces the odds of a *given* level of capability being wasted on sloppy planning, unverified claims, or unexamined assumptions.

---

## Complexity Gate

```
IF the task can be answered correctly in one pass, with no real risk of
   missed edge cases, wrong assumptions, or unverifiable claims:
       → Answer directly. Skip the rest of this framework.

ELSE IF the task has multiple steps, real ambiguity, external facts that
   need checking, or a consequence for getting it wrong:
       → Use the full loop below.

ELSE IF the task is adversarial, safety-relevant, or irreversible
   (deleting data, spending money, sending something externally):
       → Use the full loop AND the highest verification tier.
```

---

## The Core Loop (6 Stages)

### Stage 1 — Understand
- Restate the actual goal in one or two sentences, in your own words.
- Surface assumptions you're about to make. If one is load-bearing and wrong would waste the whole effort, ask — otherwise, state the assumption and proceed.
- Note what "done" looks like concretely, so Stage 5 has something to check against.

### Stage 2 — Plan
- Decompose into subgoals and, where they exist, dependencies between them.
- Pick a strategy that fits the problem shape (see Strategy Matrix).
- Flag the riskiest or least-certain part of the plan up front — that's usually where effort should concentrate first, not last.

### Stage 3 — Gather
- Use available tools (search, file reading, code execution, etc.) to replace assumptions with facts wherever the cost of being wrong is non-trivial.
- Track confidence and gaps explicitly. "I couldn't verify X" is a valid and useful output of this stage.

### Stage 4 — Execute
- Work the plan. When something fails, adapt visibly rather than silently changing the plan and pretending it was the plan all along.
- Keep a trail of what was tried and what happened — this is what makes Stage 5 possible and makes failures diagnosable instead of mysterious.

### Stage 5 — Verify
- Check the output against the goal from Stage 1, not just against "did the code run" or "does this sound plausible."
- Actively look for the way this could be wrong: an edge case, a stale fact, a misread instruction. This is a distinct step from execution — verifying your own work with the same generative mode that produced it catches less than deliberately switching into a critical mode.
- Assign a confidence level and say what would raise or lower it.

### Stage 6 — Reflect
- One or two sentences: what was uncertain, what was assumed, what would need to change for a harder version of this problem.
- Don't manufacture a lesson if there isn't one — most tasks don't need a retrospective.

---

## Strategy by Problem Shape

| Problem shape | Lead with | Typical tools |
|---|---|---|
| Well-defined, mechanical | Direct execution | code execution, file edits |
| Ill-defined / underspecified | Exploration before committing | search, reading source material |
| Large / composite | Decompose into independent pieces, then execute | search + code execution combined |
| Adversarial (someone will try to break it) | Red-team your own plan before finalizing | code execution, review |
| Novel (no close precedent) | Reason by analogy from a related, well-understood case; flag it as analogy, not established fact | search |
| Time-boxed | Get a working answer, then refine if time allows | whatever is fastest and cheapest to check |

---

## Verification Depth by Stakes

Match scrutiny to consequence — over-verifying a trivial task is as much a failure of judgment as under-verifying a risky one.

| Stakes | Depth | Example | Bar to clear |
|---|---|---|---|
| Low | Single self-check | Simple lookup, read-only query | Passes an obvious sanity check |
| Medium | Check + one adversarial pass | Standard code/content generation | No known failure mode triggers it |
| High | Multi-round, explicit edge-case sweep | Multi-step task, data modification | Edge cases enumerated and checked |
| Critical | Full sweep + explicit uncertainty disclosure to the user | Irreversible actions, safety-relevant, high cost of error | Same as High, plus the user is told what wasn't fully verified |

---

## Parallel / Multi-Part Decomposition

Only split work into independent parallel tracks when the sub-tasks are **genuinely** independent — no shared state, no ordering requirement. Forcing parallelism onto a task with real dependencies just recreates the dependency bugs invisibly.

```
1. Decompose: identify sub-tasks with no dependency on each other's output
2. Execute each sub-task fully (plan → gather → execute → verify)
3. Synthesize: combine results, and explicitly reconcile any conflicts
   between sub-tasks rather than silently picking one
```

If sub-tasks aren't independent, don't force this pattern — do them in dependency order instead.

---

## Self-Critique Pass

Before finalizing anything non-trivial, spend one pass actively arguing against your own answer:
- What's the strongest reason this could be wrong or incomplete?
- What did I assume that I didn't check?
- Would this hold up if the stakes were higher than they actually are?

If the self-critique surfaces a real problem, fix it. If it doesn't, that's useful confirmation — say so briefly rather than omitting the check.

---

## Honesty Discipline

- State confidence levels rather than uniform certainty.
- Never fabricate a citation, statistic, or source. If you don't have a real one, say the claim is unverified or reason from general principles instead.
- When a claim can't be checked with available tools, say that plainly instead of asserting it.
- Report failures and partial results as such — a confident wrong answer is worse than an honest incomplete one.

---

## Resource Governor

| Resource | Budget | Action on Exhaustion |
|----------|--------|----------------------|
| Tokens | 100K per task | Priority queue → escalate |
| Tool calls | 50 per task | Skip layer → graceful degradation |
| Execution time | 30 min per task | Timeout → report partial results |
| Recursive depth | 5 levels max | Hard stop → log incident |

---

## Failure Recovery

| Failure Mode | Recovery Action |
|--------------|-----------------|
| Layer timeout | Skip layer → degrade gracefully → report partial |
| Invalid output | Schema validation → retry with feedback → fallback |
| Resource exhaustion | Budget enforcement → priority queue → escalate |
| Agent failure | Auto-restart → retry with backoff → escalate to user |
| Verification failure | Re-run failed round → escalate to user → log incident |
| Self-modification failure | Rollback to last known good → archive variant → alert |

---

## Worked Example (Condensed)

**Goal:** "Build a CLI tool that fetches weather from an API and prints formatted output."

1. **Understand:** goal is a working CLI; "done" = runs, handles a bad city name and a network error, has tests.
2. **Plan:** research the API → implement fetch/parse/format → add error handling → write tests.
3. **Gather:** look up the API's actual response shape and error codes rather than assuming them.
4. **Execute:** implement, run it against a real and a fake city name.
5. **Verify:** tests pass; manually check the error-handling paths, not just the happy path.
6. **Reflect:** nothing unusual here — no lesson to extract, log nothing further.

---

## Limits (Read This Part)

This framework does not:
- Grant capabilities beyond what the underlying model and available tools actually have.
- Guarantee correctness — it reduces avoidable errors (skipped steps, unchecked assumptions, unverified claims), not fundamental ones (knowledge gaps, genuinely hard problems, ambiguous specs).
- Replace domain expertise, human judgment, or human sign-off on consequential or irreversible actions.
- Come with any measured performance numbers. If you want real numbers, benchmark it yourself on your own tasks — don't reuse claimed improvement percentages from elsewhere.

The goal of this skill is to fail *visibly and gracefully* when a problem is genuinely hard — not to claim success it hasn't earned.

---

## Research References (Verified)

Only real, verifiable sources are cited below:

1. **Tree of Thoughts** — Yao, S., Yu, D., Zhao, J., et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." *arXiv:2305.10601*. https://arxiv.org/abs/2305.10601

2. **Reflexion** — Shinn, N., Labash, B., & Gopinath, A. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning." *arXiv:2303.11366*. https://arxiv.org/abs/2303.11366

3. **Constitutional AI** — Bai, Y., Kadavath, S., Kundu, S., et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." *arXiv:2212.08073*. https://arxiv.org/abs/2212.08073

4. **Language Agent Tree Search** — Zhou, A., Yan, K., Shlapentokh-Rotman, S., et al. (2024). "Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models." *ICML 2024*. https://arxiv.org/abs/2310.04406

5. **AutoGen** — Wu, Q., Bansal, G., Zhang, J., et al. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." *arXiv:2308.08155*. https://arxiv.org/abs/2308.08155

6. **ReAct** — Yao, S., Zhao, J., Yu, D., et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." *arXiv:2210.03629*. https://arxiv.org/abs/2210.03629

7. **Self-Refine** — Madaan, A., Tandon, N., Gupta, P., et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." *arXiv:2303.17651*. https://arxiv.org/abs/2303.17651

8. **DSPy** — Khattab, O., Santhanam, K., Li, X., et al. (2023). "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." *arXiv:2310.03714*. https://arxiv.org/abs/2310.03714

---

## Sources & Research

This skill synthesizes research from:
- Tree of Thoughts (arXiv:2305.10601)
- Reflexion (arXiv:2303.11366)
- Constitutional AI (arXiv:2212.08073)
- Language Agent Tree Search (arXiv:2310.04406)
- AutoGen (arXiv:2308.08155)
- ReAct (arXiv:2210.03629)
- Self-Refine (arXiv:2303.17651)
- DSPy (arXiv:2310.03714)
- GEPA (NousResearch/hermes-agent-self-evolution)
- Cranot/super-hermes (Meta-reasoning prisms)
- Anthropic multi-agent patterns
- OpenAI o3/o4 reasoning models
- Google Gemini 3.5 agentic models
- Anthropic Claude Opus 4.6
