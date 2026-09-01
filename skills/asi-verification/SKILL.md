---
name: asi-verification
description: "ASI-level multi-round verification and validation."
version: 1.0.0
author: research-analyst
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASI, verification, validation, testing, quality]
    related_skills: [hermes-agent, asi-master]
    requires_toolsets: [web, research, memory]
---

# ASI VERIFICATION: Multi-Round Validation System

Advanced verification for ASI-level output quality.

## Verification Rounds

### Round 1: Automated Testing
- Unit tests
- Integration tests
- Linting
- Output pattern matching

### Round 2: Cross-Validation
- Verify with different methods
- Check consistency
- Independent calculation

### Round 3: Adversarial Testing
- Try to break the solution
- Stress-test edge cases
- Look for failure modes

### Round 4: Consensus
- Independent agent verification
- Compare conclusions
- Resolve disagreements

### Round 5: Human Review
- Present findings to user
- Highlight confidence levels
- Flag uncertain claims

## Verification Protocol

1. GENERATE: Produce initial output
2. TEST: Run automated checks
3. CROSS-CHECK: Verify with alternative methods
4. ADVERSARIAL: Try to break it
5. CONSENSUS: Get independent verification
6. HUMAN: Present for review
7. FINALIZE: Accept or revise

## Completion Criteria
- All rounds pass
- Confidence ≥ threshold
- No unresolved contradictions
- All sources cited

## When to Use
- High-stakes outputs
- Critical decisions
- Published content
- Code production