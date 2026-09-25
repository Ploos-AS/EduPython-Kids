# M1 Qualification Report — Python Explorer

**Status: PASS**

Qualified: 2026-09-25

Qualified commit: `58190cdc4320814dbaaf9d613833c6acb3b998e8`

GitHub Actions run: `36179952931`

## Qualified scope

M1 qualifies the Python Explorer course layer built on the M0 foundation:

- complete 16-lesson Norwegian beginner sequence
- exercises and challenge variants for all 16 lessons
- adult solution/support notes covering lessons 1–16
- Turtle graphics progression
- Monster Battle intermediate project
- independent final-project path
- project conversation rubric
- consistent Norwegian beginner terminology and style guidance
- exercise and teacher-material indexes
- whole-course Norwegian consistency review
- English 16-lesson course skeleton, with initial translated lessons
- repository-local Markdown link validation
- Python example syntax validation and baseline runtime tests
- CI matrix on Python 3.11, 3.12 and 3.13

## Qualification evidence

GitHub Actions run `36179952931` completed successfully for commit `58190cdc4320814dbaaf9d613833c6acb3b998e8`.

The CI workflow checks:

1. Python compilation for `examples/` and `tools/`
2. relative Markdown links across the repository
3. pytest test suite
4. Python 3.11, 3.12 and 3.13

## Defect found during qualification

The first M1.7 qualification candidate failed the Markdown-link check because `course/en/README.md` linked to the planned 16 English lesson files while lessons 5–16 did not yet exist.

This was treated as a real qualification defect rather than ignored. Skeleton files for lessons 5–16 were added, after which the full CI matrix passed.

## Deliberate exclusions

M1 does **not** claim:

- full English translation of all 16 lessons
- hands-on qualification of Turtle/Tk on classroom machines
- printable classroom sheets
- pacing plans
- accessibility qualification
- offline release bundle
- GitHub Pages course site

Those belong to later work, primarily M2.

Turtle source is covered by repository checks, but graphical/Tk behaviour still requires the separate hands-on classroom qualification already tracked in M2.

## Result

M1 — Python Explorer complete: **PASS**

The Norwegian Python Explorer course is structurally complete and internally consistent at the M1 scope. The repository has a complete English course skeleton and a green automated qualification baseline.
