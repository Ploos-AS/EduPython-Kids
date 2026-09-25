# Contributing to EduPython Kids

Thanks for helping children learn programming.

## Audience first

Course 1 is primarily written for children around age 10. Contributions should prefer clear language, small steps and experimentation over dense technical explanations.

## Lesson pattern

Student lessons should normally contain:

1. **Oppdrag**
2. **Kode**
3. **Kjør / Endre**
4. **Tenk**
5. **Utfordring**
6. **Bug-jakt** where appropriate

Introduce no more than one or two major new concepts at a time and reuse earlier concepts frequently.

## Code

Course 1 examples should use the Python standard library only. Keep programs short enough for a beginner to inspect. Examples must compile on supported Python versions; non-interactive examples should be testable where practical.

## Safety and privacy

Core lessons must not require student accounts, personal information, cloud services, tracking or proprietary teaching platforms. Use fictional/example data rather than asking children to publish personal details.

## Languages

Norwegian is the initial complete course language. English material should preserve the same lesson goals and code behavior rather than becoming a separate curriculum.

## Licensing

By contributing, you agree that documentation/course material is provided under the documentation license described in `LICENSE.md`, and source code/examples under the software license described there.

## Before submitting

Run:

```bash
python -m compileall -q examples tools
python tools/check_links.py
pytest -q
```

Turtle programs may require a graphical environment to execute; CI should at minimum validate their syntax.
