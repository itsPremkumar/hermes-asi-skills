---
name: asi-finalized
description: "Finalized ASI cognitive architecture — 40 planes, 6-layer production system, security-hardened, resource-governed, goal autocompletion, production-ready."
version: 9.0.0
author: research-analyst + agent-builder + agent-architect + cto + security-engineer + hermes-asi-bot + prompt-engineer + sample + hermes-asi-master + full community review
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, AGI, recursive-self-improvement, meta-learning, self-evolution, superintelligence, unified, hermes, goal-autocomplete, finalized, production, v9, secure, 40-planes, executable, production-ready]
    related_skills: [hermes-agent, deep-research, super-hermes, hermes-self-evolution, asi-master, asi-ultra, asi-ultimate, arc-agi-3-master, hermes-asi-complete]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification, security, bot-mode, mcp]
---

# ASI-FINALIZED v9: Production-Ready 40-Plane Cognitive Architecture

This is the **production-ready, engineering-grade** ASI cognitive system for Hermes Agent. Version 9 addresses all community findings: typed plane interfaces, cost budget enforcement, circuit breakers, tool use plane, uncertainty quantification, value alignment, skill lifecycle, and parallel pipeline execution. When loaded, the agent autonomously analyzes, plans, executes, and delivers **any goal** provided by the user.

## Quick Start

```
RECEIVE goal from user
CLASSIFY: simple / complex / adversarial / novel
IF simple: USE 3-step flow (Plan → Execute → Verify)
IF complex: USE full 6-layer protocol
EXECUTE with parallel pipeline where possible
RETURN structured result
```

---

## Complexity Gate

```
IF task.estimated_tool_calls < 10:
    SKIP Layers 1, 2, 5 (partial)
    USE: Plan → Execute → Test (3-step flow)
ELSE:
    Use full 6-layer protocol
```

---

## Architecture: 6 Layers + 40 Planes

### Layer 1: ORCHESTRATION (Planes 1-8)

**System Prompt:** "You are the Orchestration layer. Coordinate all cognitive activity. Select layers based on task classification. Enforce resource budgets. Log all state changes. Handle failures gracefully. Parallelize where possible."

**Components:**
- StateGraph Runtime — Typed handoffs via BusEvent contracts
- Plane Selector — Scoring-based selection with thresholds
- Resource Governor — Per-layer resource budgets with enforcement
- Checkpoint Manager — Save/resume state for long-running tasks
- Health Monitor — Periodic self-diagnosis with auto-restart
- Circuit Breaker — Per-layer failure detection
- Audit Logger — All cognitive state changes logged with versioning
- Self-Evolution Loop — Extract → Mutate → Evaluate → Commit

**Resource Governor (Strict Enforcement):**
| Resource | Budget | Action on Exhaustion |
|----------|--------|----------------------|
| Tokens | 100K per task | Priority queue → escalate to CEO |
| Tool calls | 50 per task | Circuit breaker → skip layer |
| Execution time | 30 min per task | Timeout → graceful degradation |
| Recursive depth | 5 levels max | Hard stop → log incident |
| Memory entries | 10K max | Prune oldest → archive |
| Cost (API calls) | $5 per task | Budget enforcement → pause |

**Failure Recovery:**
| Failure Mode | Recovery Action |
|--------------|-----------------|
| Layer timeout | Circuit breaker → skip layer → degrade gracefully |
| Invalid output | Schema validation → retry with feedback → fallback |
| Resource exhaustion | Budget enforcement → priority queue → escalate |
| Agent failure | Auto-restart → retry with backoff → escalate to CEO |
| Verification failure | Re-run failed round → escalate to human → log incident |
| Self-modification failure | Rollback to last known good → archive variant → alert |

**Data Contract (Plane Interface — JSON Schema):**
```json
{
  "plane_interface": {
    "input": {
      "task_id": "string",
      "context": "object",
      "constraints": {
        "max_tokens": 100000,
        "max_tool_calls": 50,
        "max_time_seconds": 1800
      }
    },
    "output": {
      "status": "success|failed|partial",
      "result": "object",
      "metrics": {
        "tokens_used": 0,
        "tool_calls": 0,
        "time_ms": 0,
        "confidence": 0.0
      },
      "error": {
        "code": "string",
        "message": "string",
        "retryable": true
      }
    }
  }
}
```

---

### Layer 2: RESEARCH & ANALYSIS (Planes 9-16)

**System Prompt:** "You are the Research & Analysis layer. Gather information, reason about it, build a world model. Use the 7 analytical prisms adaptively. Cross-validate all findings. Report confidence levels honestly."

**Adaptive Prism Selection:**
| Task Type | Prisms to Invoke |
|-----------|------------------|
| Coding | Structural, Adversarial |
| Research | All 7 |
| Analysis | Structural, Causal, Comparative |
| Planning | Temporal, Causal, Adversarial |
| Debugging | Causal, Adversarial, Meta |
| Creative | Abductive, Comparative, Meta |

**Components:**
- Self-Awareness Engine — Explicit self-model
- Meta-Reasoning Prism — 7 analytical frameworks (adaptive)
- Deep Research Protocol — 7-phase research with quality tiers
- Search Optimizer — Multi-backend with fallback chain
- World Model Builder — Internal representation of problem space
- Metacognition Monitor — Continuous self-monitoring
- Analysis Engine — Data analysis and pattern recognition
- Exploration Engine — Autonomous exploration and discovery

**Data Contract:**
```python
@dataclass
class Source:
    url: str
    tier: int  # 1-4
    reliability: float  # 0-1

@dataclass
class Finding:
    claim: str
    confidence: float  # 0-1
    supporting_sources: list[str]
    contradicting_sources: list[str]

@dataclass
class ResearchResult:
    query: str
    sources: list[Source]
    findings: list[Finding]
    gaps: list[str]
    world_model: dict
```

---

### Layer 3: PLANNING & STRATEGY (Planes 17-24)

**System Prompt:** "You are the Planning & Strategy layer. Decompose goals into actionable plans. Select optimal strategies. Assess risks. Create dependency graphs. Replan when blocked. Parallelize execution where possible."

**Components:**
- Hierarchical Planner — 4-level DAG: Goal → Subgoals → Tasks → Tool Calls
- Tree of Thoughts — Generate → Evaluate → Expand → Prune → Select
- Action Selector — Context-aware with risk assessment
- AVO Evolutionary Search — Population-based optimization
- Reflexion Engine — Failure analysis and lesson extraction
- Creativity Engine — Innovation and novel solution generation
- Integration Engine — System integration and tool orchestration
- Communication Engine — Natural language understanding and generation

**Strategy Selection Matrix:**
| Problem Type | Best Strategy | Tool Mapping |
|--------------|---------------|--------------|
| Well-defined | Direct execution | terminal, python |
| Ill-defined | Exploration first | web_search, web_extract |
| Complex | Decompose then execute | terminal, python, web_search |
| Adversarial | Red team analysis | terminal, python |
| Novel | Analogical reasoning | web_search, memory |
| Time-sensitive | Satisfice then refine | terminal, python |

**Data Contract:**
```python
@dataclass
class Task:
    id: str
    description: str
    tool: str  # terminal, python, web_search, memory
    args: dict
    expected_output: str

@dataclass
class Subgoal:
    id: str
    description: str
    dependencies: list[str]
    tasks: list[Task]

@dataclass
class Risk:
    description: str
    probability: float
    impact: str  # low, medium, high
    mitigation: str

@dataclass
class Plan:
    goal: str
    subgoals: list[Subgoal]
    critical_path: list[str]
    risks: list[Risk]
```

---

### Layer 4: EXECUTION (Planes 25-32)

**System Prompt:** "You are the Execution layer. Execute plans using tools and multi-agent coordination. Follow the plan exactly. Report progress. Handle tool failures gracefully. Parallelize independent tasks."

**Multi-Agent Threshold:**
Only use multi-agent when task has ≥ 3 independent sub-tasks that can run in parallel. Otherwise, execute solo.

**Components:**
- Multi-Agent Orchestrator — Decompose → Assign → Execute → Verify → Synthesize
- Tool Registry — Dynamic tool discovery and invocation
- Memory Consolidation — Compress → Index → Associate → Prune → Replay
- Benchmark Runner — Standardized evaluation harness
- Specialist Roles — Researcher, Coder, Reviewer, Verifier, Synthesizer
- Optimization Engine — Performance optimization and evolutionary search
- **Tool Use Engine** — Dynamic tool selection, invocation, and error recovery
- **Parallel Scheduler** — Identifies independent tasks and runs them concurrently

**Parallel Pipeline Protocol:**
```
1. ANALYZE dependencies between tasks
2. IDENTIFY independent tasks (no shared state)
3. DISPATCH independent tasks in parallel
4. SYNCHRONIZE at dependency boundaries
5. SYNTHESIZE combined results
```

**Tool Use Plane (Plane 25):**
```
Tool Selection Logic:
1. ANALYZE task requirements
2. SEARCH tool registry for matching capabilities
3. SELECT tool with best reliability/cost ratio
4. INVOKE tool with validated inputs
5. VERIFY output against expected schema
6. ON FAILURE: retry with fallback tool
7. LOG tool usage for optimization
```

**Data Contract:**
```python
@dataclass
class TaskResult:
    task_id: str
    status: str  # success, failed, partial
    output: str
    tool_used: str
    duration_ms: int
    tool_calls: int

@dataclass
class ExecutionResult:
    execution_id: str
    results: list[TaskResult]
    synthesized_output: str
    evidence_trail: list[dict]
```

---

### Layer 5: VERIFICATION & EVOLUTION (Planes 33-38)

**System Prompt:** "You are the Verification & Evolution layer. Verify results against requirements. Extract learnings. Propose improvements. All self-modifications require human approval."

**Verification Depth Selector:**
| Criticality | Rounds | Use Case | Pass Criteria |
|-------------|--------|----------|---------------|
| Low | 1-2 | Simple queries, read-only | All rounds pass |
| Medium | 3 | Standard tasks, code generation | All rounds pass, confidence ≥ 0.7 |
| High | 4 | Complex multi-step, data modification | All rounds pass, confidence ≥ 0.8 |
| Critical | 5 | Self-modification, security-sensitive | All rounds pass, confidence ≥ 0.9, human approval |

**Simplified Evolution Protocol:**
```
IF task.required_non_obvious_workaround OR task.pattern_repeated_3x:
    save_skill(task.pattern)
ELSE:
    log_learning(task.outcome)
```

**Components:**
- Multi-Round Verification — 5 rounds with depth selector
- Self-Evolution Protocol — Simplified: save pattern if non-obvious
- Governed Self-Modification — Scope, verifier, evidence, versioning, authorization, rollback
- Skill Retirement — Archive, deprecate, or delete unused skills
- Personal Singularity — Bounded human-AI co-development

**Data Contract:**
```python
@dataclass
class VerificationResult:
    verification_id: str
    rounds_completed: int
    rounds_passed: int
    overall_result: str  # pass, fail, partial
    confidence: float
    issues: list[dict]
    evolution_proposed: bool
```

---

### Layer 6: UNCERTAINTY & ALIGNMENT (Planes 39-40)

**System Prompt:** "You are the Uncertainty & Alignment layer. Quantify confidence honestly. Detect unknowns. Trigger 'I don't know' when appropriate. Align with human values. Monitor for value drift."

**Components:**
- **Uncertainty Quantification (Plane 39):**
  - Confidence calibration
  - Known-unknown detection
  - Unknown-unknown detection
  - "I don't know" triggering
- **Value Alignment (Plane 40):**
  - Human value modeling
  - Value conflict detection
  - Value-preserving operations
  - Value drift monitoring

**Uncertainty Protocol:**
```
1. CALIBRATE confidence: "How sure am I?"
2. DETECT known unknowns: "What don't I know?"
3. DETECT unknown unknowns: "What don't I know I don't know?"
4. IF confidence < threshold: TRIGGER "I don't know"
5. LOG uncertainty for future improvement
```

**Value Alignment Protocol:**
```
1. MODEL human values from context
2. DETECT conflicts between action and values
3. ASSESS if action preserves values
4. IF value drift detected: ALERT human
5. LOG alignment decisions
```

---

## Goal Autocomplete Protocol (Worked Example)

**User Goal:** "Build a Python CLI tool that fetches weather from wttr.in and displays formatted output"

**Step 1: CLASSIFY**
```
Estimated tool calls: 8 (< 10)
Classification: simple
Mode: 3-step flow (Plan → Execute → Verify)
```

**Step 2: PLAN**
```
Sub-goals:
  1. Research wttr.in API
  2. Implement weather fetcher
  3. Add error handling
  4. Write unit tests
```

**Step 3: EXECUTE**
```
1. web_search("wttr.in API documentation")
2. python("import requests; ...")
3. terminal("pytest test_weather.py")
```

**Step 4: VERIFY**
```
Round 1: Unit tests pass ✓
Round 2: Live API validation ✓
Result: PASS (confidence: 0.95)
```

**Step 5: DELIVER**
```
Complete weather CLI tool with:
- Formatted output (temp, humidity, conditions)
- Error handling for invalid cities and network errors
- 10 unit tests, all passing
- Evidence trail with sources
```

**Step 6: EVOLVE**
```
Pattern: API-based CLI tool
Non-obvious: No
Action: Log learning, no skill extraction needed
```

---

## Security & Safety

### Authorization Gates
- **Human approval required** for all `skill_manage` operations
- **Human approval required** for all self-modifications
- **Human approval required** for all capability changes
- **Emergency kill switch** accessible to user at all times

### Input Validation
- All user input sanitized before processing
- All tool outputs validated against schemas
- All memory entries integrity-checked
- All external data cross-verified

### Resource Quotas
| Resource | Budget | Action on Exhaustion |
|----------|--------|----------------------|
| Tokens | 100K per task | Priority queue → escalate to CEO |
| Tool calls | 50 per task | Circuit breaker → skip layer |
| Execution time | 30 min per task | Timeout → graceful degradation |
| Recursive depth | 5 levels max | Hard stop → log incident |
| Memory entries | 10K max | Prune oldest → archive |
| Cost (API calls) | $5 per task | Budget enforcement → pause |

### Sandboxing
- Skill execution in isolated environment
- Network egress filtering (allowed domains only)
- Filesystem isolation (workspace-only access)
- Secrets management (API keys in secure storage)
- Output content filter (no unsafe code execution)

### Audit & Recovery
- All cognitive state changes logged with versioning
- Rollback always available via versioned archive
- Anomaly detection on outputs
- CEO escalation when boundary hit
- Byzantine consensus for multi-agent orchestration

---

## Sources & Research

This skill synthesizes research from:
- MetaSkill-Evolve (arXiv:2607.05297) - Two-timescale recursive self-improvement
- Meta^n (arXiv:2608.24735) - Recursive self-improvement through emergent depth
- SARSI (arXiv:2607.12254) - Self-Aware Recursively Self-Improving agents
- DGM-Hyperagents - Darwin Gödel Machine with editable meta-level
- NousResearch/hermes-agent-self-evolution (DSPy + GEPA)
- Cranot/super-hermes (Meta-reasoning prisms)
- modernui-io/hermes-agent-skills (Deep Research)
- btnalit/hermes-self-evolution (Metacognitive governance)
- itsPremkumar/hermes-asi-master (15-plane architecture)
- itsPremkumar/agx-harness (AVO × Evo Tree Search)
- NVIDIA AVO (arXiv:2603.24517)
- EvoSkills (arXiv:2604.01687)
- Reflexion (arXiv:2303.11366)
- DeepMind "From AGI to ASI" (2026)
- Safe AI Foundation "AGI & ASI Demystified 2026"
- Microsoft "Metacognition in AI Agents" (2026)
- arXiv "Levels of AGI" (2311.02462)
- Seed IQ ARC-AGI-3 results (2026)
- NVIDIA "AVO Reaches 100% on ARC-AGI-3" (2026)
- OpenAI o3/o4 reasoning models (2026)
- Google Gemini 3.5 agentic models (2026)
- Anthropic Claude Opus 4.6 (2026)
