---
name: code-engineering
description: Use when inspecting, implementing, debugging, refactoring, testing, reviewing, building, or delivering code in a repository.
---

# Code Engineering

## Required Process Skills

**REQUIRED SUB-SKILL:** Use `superpowers:test-driven-development` for features, bug fixes, refactors, and behavior changes.

**REQUIRED SUB-SKILL:** Use `superpowers:systematic-debugging` when behavior is unexpected, tests fail, or the root cause is not established.

**REQUIRED SUB-SKILL:** Use `superpowers:verification-before-completion` before claiming the task is complete.

## Repository Pass

1. Read repository instructions and identify the project root.
2. Inspect status, relevant files, entry points, tests, scripts, dependencies, and recent context.
3. Preserve unrelated uncommitted changes.
4. Trace the existing behavior before choosing an edit point.
5. Define behavior, non-goals, compatibility constraints, and verification commands.

## Change Rules

- Edit the smallest coherent surface.
- Follow existing naming, architecture, error handling, and formatting conventions.
- Reuse existing utilities before adding abstractions.
- Do not add speculative options, generalized frameworks, or unrelated refactors.
- Remove only imports, variables, or references made unused by the change.
- Keep secrets out of source, fixtures, logs, test snapshots, comments, and command output.

## TDD Gate

For behavior changes: write a focused test, run it, confirm it fails for the intended missing behavior, implement the minimum, run it again, then run the project suite. A test that passes immediately does not prove the new behavior.

## Review Gate

Check requirement coverage, regression risk, type/lint/build status, security boundaries, test honesty, performance impact, public interface compatibility, and scope creep.

## Report

State changed files, behavioral effect, tests/checks run, pre-existing failures, remaining risks, and exact next action if incomplete.
