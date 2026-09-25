# Turtle/Tk hands-on qualification

This checklist covers the graphical part of Python Explorer that cannot be fully qualified by headless CI.

**Status:** READY FOR HANDS-ON TESTING

Automated CI can compile the Turtle source, but it cannot prove that a classroom machine can open, display and close a Tk window correctly.

## Test environments

Record each real environment tested.

| Date | OS | Python | Editor/terminal | Tk/Turtle | Result | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Recommended coverage before M2 PASS:

- at least one Windows classroom-style installation
- at least one macOS installation when macOS is part of the intended classroom
- at least one Linux desktop installation
- Raspberry Pi OS when Raspberry Pi is part of the intended classroom

M2 does not require every operating system above if it is not available, but the qualification report must state exactly what was physically tested.

## Q1 — Tk availability

Run:

```bash
python -m turtle
```

or, where required:

```bash
python3 -m turtle
```

PASS when a Turtle/Tk window opens without an import or display error.

- [ ] PASS
- [ ] FAIL

Notes:

____________________________________________________________

## Q2 — Repository example

From the repository or offline bundle, run:

```bash
python examples/turtle_square.py
```

PASS when the window opens and the expected drawing is visible.

- [ ] PASS
- [ ] FAIL

Notes:

____________________________________________________________

## Q3 — Lesson 14 workflow

Follow the core activity in `course/no/14-turtle.md`.

Check that the learner can:

- [ ] open the example
- [ ] run it
- [ ] see the drawing
- [ ] change a length
- [ ] change an angle
- [ ] run the changed program again
- [ ] close/reopen the graphical window without confusion

**Q3 result:**

- [ ] PASS
- [ ] FAIL

## Q4 — Lesson 15 workflow

Follow the core activity in `course/no/15-turtle-monstre.md`.

Check that:

- [ ] several drawing functions can be used together
- [ ] a function can be tested separately
- [ ] parameters visibly change the drawing
- [ ] repeated runs do not leave the learner in an unclear window state
- [ ] errors remain visible/readable in the chosen editor or terminal

**Q4 result:**

- [ ] PASS
- [ ] FAIL

## Q5 — Classroom usability

Test the actual learner workflow rather than only Python itself.

- [ ] editor text can be enlarged
- [ ] learner can switch between editor and Turtle window
- [ ] window is not hidden behind the editor after every run
- [ ] keyboard-only operation is practical where needed
- [ ] error output remains accessible
- [ ] no internet connection is required
- [ ] offline-bundle copy works when used for the test

**Q5 result:**

- [ ] PASS
- [ ] FAIL

## Q6 — Recovery

Intentionally create one simple error, for example a misspelled Turtle method.

PASS when the learner/adult can:

1. see the error
2. return to the source
3. correct it
4. run the program successfully again

- [ ] PASS
- [ ] FAIL

## Qualification rule

An environment is Turtle/Tk qualified when Q1–Q6 pass.

A failure should be recorded as one of:

- **COURSE** — lesson/example needs correction
- **PYTHON** — Python/Tk installation issue
- **EDITOR** — editor behaviour creates the problem
- **OS** — graphical/session integration issue
- **ACCESSIBILITY** — workflow is not usable with the required accommodation
- **UNKNOWN** — needs investigation

Do not change course material merely to hide an environment-specific installation problem. Document the environment and fix the correct layer.

## Evidence for M2

When hands-on testing is complete, record:

- machine/OS
- Python version
- editor or terminal
- Q1–Q6 results
- any fixes made
- final commit tested

Then update the M2 qualification report.

Until real graphical testing has been recorded, this document remains **READY FOR HANDS-ON TESTING**, not PASS.
