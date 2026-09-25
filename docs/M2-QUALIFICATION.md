# M2 — Classroom Quality qualification

**Status:** PENDING ONE EXTERNAL GATE  
**Date:** 2026-09-25

M2 improves Python Explorer for real classroom use. Repository-side work, bilingual Course 1 material, language parity and GitHub Pages deployment are qualified. The milestone remains open until a real graphical Turtle/Tk session passes Q1–Q6.

## Qualified scope

- Norwegian and English first-class Course 1 editions
- bilingual exercises, student checklists and printable companions
- bilingual teacher/parent guidance, pacing, project rubric and solution notes
- Course 1 language parity: PASS WITH CONTINUOUS REVIEW
- accessibility guidance and classroom accommodations
- offline classroom bundle with automated bilingual-content verification
- GitHub Pages build and deployment
- M2 repository-readiness and language-parity enforcement in CI
- Turtle/Tk qualification procedure, result form and graphical smoke-test helper

## Automated evidence

CI run `36186696660` for commit `5010d31f06b759d135918eb2957d804654f968ee` completed successfully on the current M2 repository architecture.

CI validates Python source, Markdown links, structural language parity, M2 repository readiness, offline-bundle contents and tests across Python 3.11, 3.12 and 3.13.

## GitHub Pages evidence

Pages run `36186696779` for commit `5010d31f06b759d135918eb2957d804654f968ee` completed successfully.

## Language parity evidence

See [LANGUAGE-PARITY-QUALIFICATION.md](LANGUAGE-PARITY-QUALIFICATION.md).

Course 1 language parity is qualified separately from M2's graphical gate. Norwegian remains the primary authoring language while both Norwegian and English are first-class supported editions.

## Remaining gate — Turtle/Tk

**Status: PENDING HANDS-ON TEST**

Follow [TURTLE-QUALIFICATION.md](TURTLE-QUALIFICATION.md) and record the actual environment in [TURTLE-TEST-RESULT.md](TURTLE-TEST-RESULT.md).

The helper `tools/turtle_smoke.py` is included in the offline bundle. It provides a graphical pre-check, but a zero exit code or headless source check is not accepted as hands-on evidence.

## PASS rule

Change this report to **PASS** only after:

1. Q1–Q6 pass on a real graphical desktop environment.
2. OS, Python version, Tk version, editor/terminal and tested commit are recorded.
3. Any discovered course defects are fixed and retested.
4. CI and Pages remain green for the final qualified commit.

Until then, M2 is deliberately not marked PASS.
