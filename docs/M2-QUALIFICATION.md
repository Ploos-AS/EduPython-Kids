# M2 — Classroom Quality qualification

**Status:** PENDING ONE EXTERNAL GATE  
**Date:** 2026-09-25

M2 improves Python Explorer for real classroom use. Repository-side work and GitHub Pages deployment are qualified. The milestone must remain open until a real graphical Turtle/Tk session has passed the documented hands-on procedure.

## Qualified scope

- printable companion sheets covering lessons 1–16
- teacher pacing plans for 30, 45 and 60 minute sessions
- accessibility review and classroom accommodations
- offline classroom bundle and automated bundle verification
- student progress checklist
- GitHub Pages source, build and deployment
- M2 repository-readiness enforcement in CI
- Turtle/Tk qualification procedure, result form and graphical smoke-test helper

## Automated evidence

The repository CI validates Python source, internal Markdown links, tests and required M2 repository artifacts on Python 3.11, 3.12 and 3.13.

CI run `36182445563` for commit `cc12322d982e14ec5f3ea2556711d3dfe6632c90` completed successfully.

## GitHub Pages evidence

Pages run `36182445418` for commit `cc12322d982e14ec5f3ea2556711d3dfe6632c90` completed successfully.

Both the build and deployment workflow are therefore operational.

## Remaining gate — Turtle/Tk

**Status: PENDING HANDS-ON TEST**

Follow [TURTLE-QUALIFICATION.md](TURTLE-QUALIFICATION.md) and record the actual environment in [TURTLE-TEST-RESULT.md](TURTLE-TEST-RESULT.md).

The helper `tools/turtle_smoke.py` may be used for the graphical pre-check, but automated or headless execution is not accepted as evidence for this gate.

## PASS rule

Change this report to **PASS** only after:

1. Q1–Q6 in the Turtle/Tk qualification procedure have passed on a real graphical desktop environment.
2. The tested OS, Python version, Tk version, editor/terminal and commit have been recorded.
3. Any discovered course defects have been fixed and retested.
4. CI and Pages remain green for the final qualified commit.

Until then, M2 is deliberately not marked PASS.
