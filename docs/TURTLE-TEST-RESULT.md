# Turtle/Tk test result

Use this file to record one real graphical qualification run.

Do not mark it PASS from CI or from source inspection.

## Environment

Record the exact environment. Do not use a CI runner as the environment for this evidence.

- Date:
- Machine:
- Operating system:
- Desktop/session:
- Python version:
- Tk version:
- Editor/terminal:
- Tested commit:
- Offline bundle used: yes / no

## Results

Run all six checks on the same environment unless a separate environment is explicitly recorded.

| Check | Result | Notes |
| --- | --- | --- |
| Q1 — Tk availability | | |
| Q2 — `examples/turtle_square.py` | | |
| Q3 — Lesson 14 workflow | | |
| Q4 — Lesson 15 workflow | | |
| Q5 — Classroom usability | | |
| Q6 — Error recovery | | |

## Smoke-test helper

The repository includes:

```bash
python tools/turtle_smoke.py
```

or:

```bash
python3 tools/turtle_smoke.py
```

This reports Python/Tk versions and opens a small graphical Turtle test. The user must visually confirm the window and drawing; a zero exit code alone is not sufficient for hands-on qualification.

## Overall result

- [ ] PASS
- [ ] FAIL

Failure category, if applicable:

- [ ] COURSE
- [ ] PYTHON
- [ ] EDITOR
- [ ] OS
- [ ] ACCESSIBILITY
- [ ] UNKNOWN

Notes:

____________________________________________________________

Tester:

____________________________________________________________
