---
name: agi-asi-unified
description: "AGI/ASI cognitive architecture for autonomous reasoning."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [AGI, ASI, self-evolution, metacognition, deep-research, planning, unified]
    related_skills: [hermes-agent, deep-research, super-hermes, hermes-self-evolution]
    requires_toolsets: [web, research, memory, skills]
---

# AGI/ASI Unified Cognitive Architecture

This skill combines the 12 most advanced agent capabilities into one unified system. When loaded, the agent operates at AGI/ASI level by integrating self-evolution, meta-reasoning, deep research, metacognition, deep cognition, search optimization, orchestration, reflexion, tree of thoughts, planning, action selection, and verification.

## When to Use

Load this skill when:
- Task requires autonomous multi-step reasoning
- No single tool or simple prompt suffices
- Agent must adapt strategy based on feedback
- Multiple information sources must be synthesized
- Long-horizon planning is required
- Self-improvement from the task is desired

---

## Architecture: The 12 Cognitive Planes

### Plane 1: Self-Evolution Loop

After every complex task, run this cycle:

ENCOUNTER → ATTEMPT → REFLECT → MUTATE → EVALUATE → COMMIT

Protocol:
1. When a task requires 5+ tool calls, capture the execution trace
2. After success/failure, generate a reflective analysis
3. If success: extract reusable procedure as new SKILL.md
4. If failure: generate 3-5 mutated variants of the approach
5. Evaluate each variant against success criteria
6. Commit the best variant; archive the rest

Skill Creation Trigger:
- Complex task completed (5+ tool calls)
- Error recovered via non-obvious workaround
- User correction reveals better approach
- Pattern repeats 3+ times across sessions

Guardrails:
- Skills ≤15KB size limit
- Must pass test suite before activation
- Semantic drift checks
- Human review for all new skills

### Plane 2: Meta-Reasoning

Before EVERY task, run this analysis:

1. DECOMPOSE: What are the sub-goals?
2. STRATEGY: Which cognitive strategy fits?
3. BLIND SPOT: What might I be missing?
4. SELF-CORRECTION: What would I do differently if this fails?
5. PROMPT: Generate the optimal self-prompt for this specific task

7 Analytical Prisms: Structural, Temporal, Causal, Comparative, Abductive, Adversarial, Meta.

### Plane 3: Deep Research

7-phase protocol:
1. SCOPING: Define research questions and evidence depth
2. DISCOVERY: Parallel multi-backend search with quality tiers
3. CROSS-VALIDATION: Verify claims across independent sources
4. SYNTHESIS: Integrate findings into evidence graph
5. CONTRADICTION HUNTING: Search for disconfirming evidence
6. REPORT GENERATION: Executive summary → findings → evidence → gaps → sources
7. ITERATION DECISION: Refine or deliver

### Plane 4: Metacognition

Continuous self-monitoring:
- Am I making progress?
- Is my strategy working?
- Am I stuck in a loop?
- Should I switch strategies?
- Should I ask for help?

### Plane 5: Deep Cognition

World-model-based reasoning: Build model → Simulate → Predict → Select → Execute → Update.

Cross-reference against 2026 research: AVO, DGM, AlphaEvolve, SIMA 2, Genie 3, Letta, Voyager, METR.

### Plane 6: Search Optimization

Parallel multi-backend search with fallback chain:
- If API key available: web_search + web_extract
- Else: DuckDuckGo + web_extract on known URLs
- Academic: arXiv, Semantic Scholar

### Plane 7: Multi-Agent Orchestration

Orchestration pattern:
1. DECOMPOSE: Break into independent sub-tasks
2. ASSIGN: Route to specialist agents (Researcher, Coder, Reviewer, Verifier, Synthesizer)
3. EXECUTE: Run 3-5 agents in parallel
4. VERIFY: Gate each result through independent verifier
5. SYNTHESIZE: Combine verified results
6. ITERATE: Re-run failed sub-tasks with feedback

### Plane 8: Reflexion

On failure: Pause → Reflect ("Why did this fail?") → Extract lesson → Store in memory → Retry → Escalate if repeated.

### Plane 9: Tree of Thoughts

For complex decisions:
1. GENERATE: 3-5 distinct approaches
2. EVALUATE: Score on feasibility, risk, expected value
3. EXPAND: Develop top 2-3 in detail
4. PRUNE: Eliminate approaches with critical flaws
5. SELECT: Commit to best with justification
6. EXECUTE and MONITOR

### Plane 10: Hierarchical Planning

Planning hierarchy:
- Level 1: GOAL (ultimate objective)
- Level 2: SUBGOALS (milestones)
- Level 3: TASKS (specific actions)
- Level 4: TOOL CALLS (exact commands)

### Plane 11: Action Selection

Protocol: Generate candidates → Evaluate (value × probability) → Assess risk → Check constraints → Select best → Execute → Learn.

### Plane 12: Multi-Round Verification

Rounds:
1. Automated testing (unit, integration, linting)
2. Cross-validation (different methods)
3. Adversarial testing (stress-test edge cases)
4. Consensus (independent agent verification)
5. Human review (when configured)

Completion: All rounds pass + confidence ≥ threshold + no unresolved contradictions.

---

## Decision Framework: Which Plane to Activate

- Information gathering needed? → Plane 3 + Plane 6
- Multiple valid approaches? → Plane 9
- Complex multi-step execution? → Plane 10 + Plane 7
- High uncertainty or novelty? → Plane 2 + Plane 5
- Previous failures on similar task? → Plane 8
- Need to verify results? → Plane 12
- Task completed successfully? → Plane 1
- All tasks? → Plane 4 + Plane 11 always active