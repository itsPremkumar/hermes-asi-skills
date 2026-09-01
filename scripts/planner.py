"""Planner script — creates hierarchical plans from goals."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional


class GoalType(Enum):
    IMPLEMENTATION = "implementation"
    RESEARCH = "research"
    DEBUGGING = "debugging"
    EVALUATION = "evaluation"
    GENERAL = "general"


class Complexity(Enum):
    SIMPLE = "simple"
    MEDIUM = "medium"
    COMPLEX = "complex"


@dataclass
class TaskPlan:
    id: str
    description: str
    tool: str
    args: dict = field(default_factory=dict)
    expected_output: str = ""


@dataclass
class SubgoalPlan:
    id: str
    description: str
    dependencies: list[str] = field(default_factory=list)
    tasks: list[TaskPlan] = field(default_factory=list)


@dataclass
class Plan:
    goal: str
    goal_type: GoalType
    complexity: Complexity
    subgoals: list[SubgoalPlan] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)


def classify_goal(description: str) -> tuple[GoalType, Complexity]:
    """Classify goal type and complexity."""
    words = description.split()
    word_count = len(words)
    
    # Complexity
    if word_count < 5:
        complexity = Complexity.SIMPLE
    elif word_count < 15:
        complexity = Complexity.MEDIUM
    else:
        complexity = Complexity.COMPLEX
    
    # Type
    desc_lower = description.lower()
    if any(w in desc_lower for w in ["build", "create", "implement", "code"]):
        goal_type = GoalType.IMPLEMENTATION
    elif any(w in desc_lower for w in ["research", "find", "search", "analyze"]):
        goal_type = GoalType.RESEARCH
    elif any(w in desc_lower for w in ["fix", "debug", "error", "bug"]):
        goal_type = GoalType.DEBUGGING
    elif any(w in desc_lower for w in ["evaluate", "compare", "recommend"]):
        goal_type = GoalType.EVALUATION
    else:
        goal_type = GoalType.GENERAL
    
    return goal_type, complexity


def create_plan(goal_description: str) -> Plan:
    """Create a plan from a goal description."""
    goal_type, complexity = classify_goal(goal_description)
    plan = Plan(goal=goal_description, goal_type=goal_type, complexity=complexity)
    
    if goal_type == GoalType.IMPLEMENTATION:
        plan.subgoals = _plan_implementation(goal_description)
    elif goal_type == GoalType.RESEARCH:
        plan.subgoals = _plan_research(goal_description)
    elif goal_type == GoalType.DEBUGGING:
        plan.subgoals = _plan_debugging(goal_description)
    elif goal_type == GoalType.EVALUATION:
        plan.subgoals = _plan_evaluation(goal_description)
    else:
        plan.subgoals = _plan_general(goal_description)
    
    return plan


def _plan_implementation(goal: str) -> list[SubgoalPlan]:
    return [
        SubgoalPlan(
            id="sg1",
            description=f"Research: {goal}",
            tasks=[
                TaskPlan(id="t1", description="Search for relevant documentation", tool="web_search"),
                TaskPlan(id="t2", description="Read existing code if applicable", tool="read_file"),
            ],
        ),
        SubgoalPlan(
            id="sg2",
            description=f"Design: {goal}",
            dependencies=["sg1"],
            tasks=[
                TaskPlan(id="t3", description="Create implementation plan", tool="write_file"),
            ],
        ),
        SubgoalPlan(
            id="sg3",
            description=f"Implement: {goal}",
            dependencies=["sg2"],
            tasks=[
                TaskPlan(id="t4", description="Write the code", tool="write_file"),
                TaskPlan(id="t5", description="Test the implementation", tool="terminal"),
            ],
        ),
        SubgoalPlan(
            id="sg4",
            description=f"Verify: {goal}",
            dependencies=["sg3"],
            tasks=[
                TaskPlan(id="t6", description="Run tests", tool="terminal"),
                TaskPlan(id="t7", description="Verify output", tool="read_file"),
            ],
        ),
    ]


def _plan_research(goal: str) -> list[SubgoalPlan]:
    return [
        SubgoalPlan(
            id="sg1",
            description=f"Search: {goal}",
            tasks=[
                TaskPlan(id="t1", description="Web search", tool="web_search"),
                TaskPlan(id="t2", description="Extract relevant content", tool="web_extract"),
            ],
        ),
        SubgoalPlan(
            id="sg2",
            description=f"Synthesize: {goal}",
            dependencies=["sg1"],
            tasks=[
                TaskPlan(id="t3", description="Summarize findings", tool="write_file"),
            ],
        ),
    ]


def _plan_debugging(goal: str) -> list[SubgoalPlan]:
    return [
        SubgoalPlan(
            id="sg1",
            description=f"Reproduce: {goal}",
            tasks=[
                TaskPlan(id="t1", description="Reproduce the issue", tool="terminal"),
            ],
        ),
        SubgoalPlan(
            id="sg2",
            description=f"Diagnose: {goal}",
            dependencies=["sg1"],
            tasks=[
                TaskPlan(id="t2", description="Isolate root cause", tool="terminal"),
            ],
        ),
        SubgoalPlan(
            id="sg3",
            description=f"Fix: {goal}",
            dependencies=["sg2"],
            tasks=[
                TaskPlan(id="t3", description="Apply fix", tool="write_file"),
                TaskPlan(id="t4", description="Verify fix", tool="terminal"),
            ],
        ),
    ]


def _plan_evaluation(goal: str) -> list[SubgoalPlan]:
    return [
        SubgoalPlan(
            id="sg1",
            description=f"Define criteria: {goal}",
            tasks=[
                TaskPlan(id="t1", description="Define evaluation criteria", tool="write_file"),
            ],
        ),
        SubgoalPlan(
            id="sg2",
            description=f"Gather data: {goal}",
            dependencies=["sg1"],
            tasks=[
                TaskPlan(id="t2", description="Research options", tool="web_search"),
            ],
        ),
        SubgoalPlan(
            id="sg3",
            description=f"Evaluate: {goal}",
            dependencies=["sg2"],
            tasks=[
                TaskPlan(id="t3", description="Score options", tool="write_file"),
                TaskPlan(id="t4", description="Recommend best option", tool="write_file"),
            ],
        ),
    ]


def _plan_general(goal: str) -> list[SubgoalPlan]:
    return [
        SubgoalPlan(
            id="sg1",
            description=f"Analyze: {goal}",
            tasks=[
                TaskPlan(id="t1", description="Understand requirements", tool="web_search"),
            ],
        ),
        SubgoalPlan(
            id="sg2",
            description=f"Execute: {goal}",
            dependencies=["sg1"],
            tasks=[
                TaskPlan(id="t2", description="Execute the task", tool="terminal"),
            ],
        ),
        SubgoalPlan(
            id="sg3",
            description=f"Verify: {goal}",
            dependencies=["sg2"],
            tasks=[
                TaskPlan(id="t3", description="Verify completion", tool="read_file"),
            ],
        ),
    ]


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python planner.py <goal description>")
        sys.exit(1)
    
    goal = " ".join(sys.argv[1:])
    plan = create_plan(goal)
    
    output = {
        "goal": plan.goal,
        "type": plan.goal_type.value,
        "complexity": plan.complexity.value,
        "subgoals": [
            {
                "id": sg.id,
                "description": sg.description,
                "dependencies": sg.dependencies,
                "tasks": [
                    {"id": t.id, "description": t.description, "tool": t.tool}
                    for t in sg.tasks
                ],
            }
            for sg in plan.subgoals
        ],
    }
    
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
