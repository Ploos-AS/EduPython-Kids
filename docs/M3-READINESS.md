# M3 — Release readiness

## Status

**READY FOR HANDS-ON DESKTOP QUALIFICATION**

Candidate commit:

`fba303d7f524f4924f528a385aaf285928f77183`

This is a qualification candidate, not an M3 PASS record.

## Automated evidence

For the candidate commit:

- CI run #304: PASS
- Pages run #186: PASS
- Norwegian and English M3 lesson structure is checked in CI
- runnable Python examples compile on Python 3.11, 3.12 and 3.13
- course `python` snippets must parse successfully
- intentional `python-bug` snippets must contain a syntax error
- the offline ZIP is built and inspected in CI
- all 10 Norwegian and all 10 English M3 lessons are required in the ZIP
- `examples/m3-mini-game.py` and the offline start links are required in the ZIP

## What is deliberately not qualified by CI

Automated checks do not prove:

- that a Turtle/Tk window opens correctly on a real desktop
- keyboard focus and arrow-key behaviour
- timer responsiveness during play
- visual readability at a practical classroom display size
- child-facing editor/Turtle error-recovery workflow
- complete play-through behaviour

These are covered by Q1–Q9 in [M3-QUALIFICATION.md](M3-QUALIFICATION.md).

## Qualification procedure

1. Check out the candidate commit exactly.
2. Record the machine, OS, desktop/session, Python, Tk, editor/terminal and course edition.
3. Run Q1–Q9 from [M3-QUALIFICATION.md](M3-QUALIFICATION.md).
4. Record the evidence in [M3-TEST-RESULT.md](M3-TEST-RESULT.md).
5. If a course-owned defect is found, fix it and create a new candidate commit.
6. Mark M3 PASS only after all Q1–Q9 pass against the recorded commit.

Until then, M3 remains **content complete; qualification pending**.
