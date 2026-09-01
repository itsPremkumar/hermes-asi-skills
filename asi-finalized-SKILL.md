---
name: asi-finalized
description: "Finalized ASI cognitive architecture — practical, tested, honest framework for autonomous goal completion using Hermes Agent's actual tools and capabilities."
version: 12.0.0
author: research-analyst + agent-builder + agent-architect + cto + security-engineer + hermes-asi-bot + prompt-engineer + sample + qa-lead + hermes-sovereign-master + tech-lead + full community review
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, AGI, recursive-self-improvement, meta-learning, self-evolution, superintelligence, unified, hermes, goal-autocomplete, finalized, production, v12, secure, verified, executable, practical, honest, tested, hermes-integrated]
    related_skills: [hermes-agent, deep-research, super-hermes, hermes-self-evolution, asi-master, asi-ultra, asi-ultimate, arc-agi-3-master, hermes-asi-complete, hermes-deep-solve]
    requires_toolsets: [web, research, memory, skills, multi-agent, verification, security, bot-mode, mcp]
---

# ASI-FINALIZED v12: Hermes-Integrated Autonomous Goal Completion

This is the **practical, Hermes-integrated, honest** cognitive system. Version 12 uses Hermes Agent's actual tools and capabilities — terminal, file operations, Python execution, memory, skills, profiles, cron, MCP, and security model. No pseudocode. No architecture astronautics. Just real tool calls that work.

## What This Is

A structured framework for tackling hard problems using Hermes Agent's actual capabilities. It reduces avoidable errors and fails visibly when problems are genuinely hard.

## What This Is Not

A mechanism for "AGI" or "ASI." No prompt grants capabilities the underlying model doesn't have.

---

## Hermes Tool Integration

### Core Tools Used

| Tool | Purpose | Example |
|------|---------|---------|
| `terminal` | Execute shell commands | `terminal("pytest test_weather.py")` |
| `read_file` | Read file contents | `read_file("src/weather.py")` |
| `write_file` | Write file contents | `write_file("src/weather.py", code)` |
| `search_files` | Find files by pattern | `search_files("*.py", "src/")` |
| `web_search` | Search the web | `web_search("wttr.in API")` |
| `web_extract` | Extract web content | `web_extract("https://wttr.in")` |
| `skill_view` | Load a skill | `skill_view("hermes-agent")` |
| `skills_list` | List available skills | `skills_list()` |
| `todo` | Track task progress | `todo(todos=[...])` |
| `session_search` | Search memory | `session_search("weather API")` |
| `memory` | Persistent memory | `memory(action="store", key="api", value="...")` |
| `cronjob` | Schedule tasks | `cronjob(action="create", schedule="...")` |
| `message_agent` | Multi-agent communication | `message_agent("researcher", "Find API docs")` |

### Security Model

| Security Feature | Tool | Usage |
|-----------------|------|-------|
| Command allowlist | `terminal` | Only allowed commands execute |
| Tirith security | Built-in | Automatic security review |
| Approval modes | Built-in | Human approval for dangerous actions |
| Secret redaction | Built-in | API keys never exposed |
| Filesystem isolation | Built-in | Workspace-only access |

---

## Complexity Gate

```
IF the task can be answered correctly in one pass:
    → Answer directly. Skip the rest.

ELSE IF the task has multiple steps or real ambiguity:
    → Use the full loop below with Hermes tools.

ELSE IF the task is adversarial or irreversible:
    → Use the full loop AND highest verification tier.
```

---

## The Core Loop (6 Stages) — With Hermes Tools

### Stage 1 — Understand

**Actions:**
```python
# Restate goal in your own words
goal = "Build a Python CLI tool that fetches weather from wttr.in"

# Surface assumptions
assumptions = [
    "wttr.in returns JSON",
    "No API key required",
    "Python requests library available"
]

# Define "done"
done_criteria = [
    "CLI runs with city argument",
    "Handles invalid city gracefully",
    "Handles network errors gracefully",
    "Unit tests pass"
]
```

### Stage 2 — Plan

**Actions:**
```python
# Create task tracking
todo(todos=[
    {"id": "1", "content": "Research wttr.in API", "status": "in_progress"},
    {"id": "2", "content": "Implement weather fetcher", "status": "pending"},
    {"id": "3", "content": "Add error handling", "status": "pending"},
    {"id": "4", "content": "Write unit tests", "status": "pending"},
    {"id": "5", "content": "Verify and deliver", "status": "pending"}
])

# Decompose into subgoals
subgoals = [
    "Research API → web_search + web_extract",
    "Implement → write_file + terminal",
    "Test → terminal(pytest)",
    "Verify → read_file + manual check"
]
```

### Stage 3 — Gather

**Actions:**
```python
# Search for API documentation
web_search("wttr.in API documentation JSON format")

# Extract actual API response
web_extract("https://wttr.in?format=j1")

# Verify assumptions
terminal("curl -s 'https://wttr.in?format=j1' | python3 -m json.tool | head -20")

# Store findings in memory
memory(action="store", key="wttr_api_format", value="JSON with current_condition array")
```

### Stage 4 — Execute

**Actions:**
```python
# Mark task as in-progress
todo(todos=[{"id": "2", "content": "Implement weather fetcher", "status": "in_progress"}])

# Write the code
write_file("src/weather.py", '''
import requests
import sys
import json

def get_weather(city):
    """Fetch weather from wttr.in API."""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        return {
            "city": city,
            "temp": current["temp_C"],
            "humidity": current["humidity"],
            "description": current["weatherDesc"][0]["value"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    except (KeyError, IndexError) as e:
        return {"error": f"Invalid response format: {e}"}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    result = get_weather(sys.argv[1])
    print(json.dumps(result, indent=2))
''')

# Test it
terminal("python3 src/weather.py London")
```

### Stage 5 — Verify

**Actions:**
```python
# Run unit tests
terminal("pytest test_weather.py -v")

# Check code quality
terminal("python3 -m py_compile src/weather.py")

# Verify error handling
terminal("python3 src/weather.py InvalidCityName123")

# Manual code review
read_file("src/weather.py")

# Mark complete
todo(todos=[{"id": "2", "content": "Implement weather fetcher", "status": "completed"}])
```

### Stage 6 — Reflect

**Actions:**
```python
# Log learnings
memory(action="store", key="weather_cli_pattern", value="API CLI: requests + argparse + json")

# Update task status
todo(todos=[{"id": "5", "content": "Verify and deliver", "status": "completed"}])
```

---

## Resource Governor

| Resource | Budget | Tool | Action on Exhaustion |
|----------|--------|------|----------------------|
| Tokens | 100K | Built-in | Priority queue → escalate |
| Tool calls | 50 | Built-in | Skip layer → graceful degradation |
| Execution time | 30 min | Built-in | Timeout → report partial results |
| Recursive depth | 5 levels | Built-in | Hard stop → log incident |

---

## Failure Recovery

| Failure Mode | Recovery Action | Tool |
|--------------|-----------------|------|
| Layer timeout | Skip layer → degrade gracefully | Built-in |
| Invalid output | Schema validation → retry with feedback | `read_file` + `terminal` |
| Resource exhaustion | Budget enforcement → priority queue | Built-in |
| Agent failure | Auto-restart → retry with backoff | `terminal` |
| Verification failure | Re-run failed round → escalate to user | `terminal` |
| Self-modification failure | Rollback to last known good | `terminal` + `read_file` |

---

## Multi-Agent Coordination

**Threshold:** Only use multi-agent when task has ≥ 3 independent sub-tasks.

**Protocol:**
```python
# Agent A: Research
message_agent("researcher", "Find wttr.in API documentation and response format")

# Agent B: Implementation
message_agent("coder", "Implement weather.py based on API docs")

# Agent C: Testing
message_agent("tester", "Write comprehensive unit tests for weather.py")

# Synthesize results
# Combine outputs from all agents
```

---

## Skill Integration

**Loading Skills:**
```python
# Load hermes-agent skill for reference
skill_view("hermes-agent")

# List available skills
skills_list()

# Load specific skill
skill_view("deep-research")
```

**Memory Integration:**
```python
# Store findings
memory(action="store", key="api_format", value="JSON")

# Retrieve later
memory(action="retrieve", key="api_format")

# Search memory
session_search("weather API")
```

---

## Worked Example (Complete)

**Goal:** "Build a Python CLI tool that fetches weather from wttr.in"

**Execution:**

```python
# Stage 1: Understand
goal = "Build Python CLI for wttr.in weather"
done = ["CLI runs", "Handles errors", "Tests pass"]

# Stage 2: Plan
todo(todos=[
    {"id": "1", "content": "Research API", "status": "in_progress"},
    {"id": "2", "content": "Implement", "status": "pending"},
    {"id": "3", "content": "Test", "status": "pending"}
])

# Stage 3: Gather
web_search("wttr.in API JSON format")
web_extract("https://wttr.in?format=j1")
terminal("curl -s 'https://wttr.in?format=j1' | head -20")

# Stage 4: Execute
write_file("src/weather.py", WEATHER_CODE)
terminal("python3 src/weather.py London")

# Stage 5: Verify
terminal("pytest test_weather.py -v")
terminal("python3 src/weather.py InvalidCity")

# Stage 6: Reflect
memory(action="store", key="weather_pattern", value="API CLI pattern")
todo(todos=[{"id": "1", "status": "completed"}, {"id": "2", "status": "completed"}, {"id": "3", "status": "completed"}])
```

---

## Limits (Read This Part)

This framework does not:
- Grant capabilities beyond what the underlying model and available tools actually have.
- Guarantee correctness — it reduces avoidable errors, not fundamental ones.
- Replace domain expertise, human judgment, or human sign-off on consequential actions.
- Come with any measured performance numbers.

The goal of this skill is to fail *visibly and gracefully* when a problem is genuinely hard — not to claim success it hasn't earned.

---

## Research References (Verified)

1. **Tree of Thoughts** — arXiv:2305.10601 ✅
2. **Reflexion** — arXiv:2303.11366 ✅
3. **Constitutional AI** — arXiv:2212.08073 ✅
4. **Language Agent Tree Search** — arXiv:2310.04406 ✅
5. **AutoGen** — arXiv:2308.08155 ✅
6. **ReAct** — arXiv:2210.03629 ✅
7. **Self-Refine** — arXiv:2303.17651 ✅
8. **DSPy** — arXiv:2310.03714 ✅

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
