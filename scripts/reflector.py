"""Reflector script — reflects on what was learned from a task."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from typing import Any


@dataclass
class Reflection:
    task_description: str
    success: bool
    uncertainties: list[str]
    assumptions: list[str]
    lessons: list[str]
    improvements: list[str]


def reflect(
    task_description: str,
    success: bool,
    output: str,
    errors: list[str] | None = None,
) -> Reflection:
    """Reflect on a task and extract learnings."""
    uncertainties = []
    assumptions = []
    lessons = []
    improvements = []
    
    # Identify uncertainties
    if not output:
        uncertainties.append("No output was produced")
    if errors:
        for error in errors:
            uncertainties.append(f"Error: {error}")
    
    # Identify assumptions
    assumptions.append("The task was well-defined")
    assumptions.append("The tools were available")
    
    # Extract lessons
    if success:
        lessons.append("The approach worked")
    else:
        lessons.append("The approach needs adjustment")
    
    # Suggest improvements
    if not success:
        improvements.append("Try a different approach")
        improvements.append("Break the task into smaller steps")
    
    return Reflection(
        task_description=task_description,
        success=success,
        uncertainties=uncertainties,
        assumptions=assumptions,
        lessons=lessons,
        improvements=improvements,
    )


def main():
    """CLI entry point."""
    if len(sys.argv) < 3:
        print("Usage: python reflector.py <task_description> <success: true|false> [output_file]")
        sys.exit(1)
    
    task_description = sys.argv[1]
    success = sys.argv[2].lower() == "true"
    output = ""
    errors = []
    
    if len(sys.argv) > 3:
        try:
            with open(sys.argv[3], "r") as f:
                output = f.read()
        except FileNotFoundError:
            errors.append(f"Output file not found: {sys.argv[3]}")
    
    reflection = reflect(task_description, success, output, errors)
    
    output_data = {
        "task": reflection.task_description,
        "success": reflection.success,
        "uncertainties": reflection.uncertainties,
        "assumptions": reflection.assumptions,
        "lessons": reflection.lessons,
        "improvements": reflection.improvements,
    }
    
    print(json.dumps(output_data, indent=2))


if __name__ == "__main__":
    main()
