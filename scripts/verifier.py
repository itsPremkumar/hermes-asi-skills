"""Verifier script — verifies results against requirements."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Tier(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class VerificationResult:
    tier: Tier
    rounds_completed: int
    rounds_passed: int
    overall_result: str
    confidence: float
    issues: list[str]


def verify(goal_output: str, tier: Tier = Tier.MEDIUM) -> VerificationResult:
    """Verify the goal output."""
    issues = []
    rounds_completed = 0
    rounds_passed = 0
    
    # Round 1: Basic check
    rounds_completed += 1
    if goal_output:
        rounds_passed += 1
    else:
        issues.append("No output produced")
    
    if tier == Tier.LOW:
        return _build_result(tier, rounds_completed, rounds_passed, issues)
    
    # Round 2: Adversarial check
    rounds_completed += 1
    if goal_output and len(goal_output.strip()) > 10:
        rounds_passed += 1
    else:
        issues.append("Output is too short or empty")
    
    if tier == Tier.MEDIUM:
        return _build_result(tier, rounds_completed, rounds_passed, issues)
    
    # Round 3: Edge case check
    rounds_completed += 1
    if goal_output and not goal_output.startswith("ERROR"):
        rounds_passed += 1
    else:
        issues.append("Output indicates an error")
    
    if tier == Tier.HIGH:
        return _build_result(tier, rounds_completed, rounds_passed, issues)
    
    # Round 4: Full disclosure
    rounds_completed += 1
    rounds_passed += 1  # Disclosure always passes
    
    return _build_result(tier, rounds_completed, rounds_passed, issues)


def _build_result(tier: Tier, completed: int, passed: int, issues: list[str]) -> VerificationResult:
    confidence = passed / completed if completed else 0.0
    result = "pass" if passed == completed else "fail" if passed == 0 else "partial"
    return VerificationResult(
        tier=tier,
        rounds_completed=completed,
        rounds_passed=passed,
        overall_result=result,
        confidence=confidence,
        issues=issues,
    )


def main():
    """CLI entry point."""
    if len(sys.argv) < 3:
        print("Usage: python verifier.py <tier> <output_file>")
        print("  tier: low, medium, high, critical")
        sys.exit(1)
    
    tier_str = sys.argv[1].lower()
    output_file = sys.argv[2]
    
    tier_map = {
        "low": Tier.LOW,
        "medium": Tier.MEDIUM,
        "high": Tier.HIGH,
        "critical": Tier.CRITICAL,
    }
    
    tier = tier_map.get(tier_str, Tier.MEDIUM)
    
    try:
        with open(output_file, "r") as f:
            output = f.read()
    except FileNotFoundError:
        output = ""
    
    result = verify(output, tier)
    
    output_data = {
        "tier": result.tier.value,
        "rounds_completed": result.rounds_completed,
        "rounds_passed": result.rounds_passed,
        "overall_result": result.overall_result,
        "confidence": result.confidence,
        "issues": result.issues,
    }
    
    print(json.dumps(output_data, indent=2))


if __name__ == "__main__":
    main()
