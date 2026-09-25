# M0 Qualification Report

**Milestone:** M0 — Foundation  
**Status:** PASS  
**Qualified:** 2026-09-25  
**Qualified commit before this report:** `5e6e16f60dd1abd4fc7419f5acf9e081bef7a2ab`

## Scope

M0 establishes a usable foundation for EduPython Kids:

- Norwegian beginner course material
- runnable Python examples
- teacher/parent guidance
- student progress checklist
- installation guidance
- documented learning progression
- automated tests
- Markdown link validation
- contribution guidelines
- documented licensing split

## Automated qualification

GitHub Actions run `36178058602` completed successfully on the qualified commit.

The CI matrix passed on:

- Python 3.11
- Python 3.12
- Python 3.13

Each matrix job successfully completed:

1. repository checkout
2. Python setup
3. test dependency installation
4. compilation of `examples/` and `tools/`
5. internal Markdown link validation
6. pytest test suite

## Defect found during qualification

The new link validator detected a stale course-index link for lesson 02. The index referenced `02-variabler.md`, while the actual lesson is `02-programmet-husker.md`.

The link was corrected before qualification. The final qualification run passed the link check on all three Python matrix jobs.

## Result

**M0 PASS**

The repository is ready to move from foundation work into M1 course-completion and polishing work.

This qualification does not claim that every future classroom or platform configuration has been tested. Turtle still requires a graphical Python/Tk environment and should receive separate hands-on classroom qualification later.
