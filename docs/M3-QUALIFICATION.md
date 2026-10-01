# M3 — Turtle/Tk desktop qualification

## Status

**READY FOR HANDS-ON TESTING**

M3 uses Turtle/Tk for its graphical game lessons. Headless CI checks source syntax and repository structure, but cannot prove that keyboard input, windows, timers and visual game behaviour work correctly on a real desktop.

M3 is not qualified until the checks below have been completed on at least one real graphical desktop environment.

## Before testing

Record:

- date
- machine
- operating system and desktop/session
- Python version
- Tk version if known
- editor or terminal used
- course edition tested: Norwegian or English
- exact Git commit tested

Use the repository at that commit without uncommitted course fixes.

Before the hands-on run, confirm CI is green for the tested commit and that the offline bundle builds and passes `tools/check_offline_bundle.py`. These are preflight checks only; they do not replace Q1–Q9.

## Q1 — Turtle/Tk opens

Run:

```text
python -m turtle
```

PASS when a Turtle window opens without an import or display error and can be closed normally.

## Q2 — Keyboard movement

Open M3 lesson 1 and run its movement program.

Check:

- Turtle window opens
- Right and Left work
- Up and Down work after completing the lesson challenge
- focus/click behaviour is understandable
- repeated key presses do not make the program unusable

PASS when a learner can control the character with the arrow keys.

## Q3 — Coordinates and screen edges

Run the lesson 2 result.

Check:

- all four directions work
- the player stays inside the intended play area
- displayed/printed coordinates change as expected
- changing STEP produces a visible and understandable result

PASS when movement and boundaries behave consistently.

## Q4 — Target, collision and score

Run the lesson 3–4 result or equivalent completed learner program.

Check:

- target is visible
- touching/catching the target is detected reliably
- target moves to a new valid position
- score increases once per catch
- score display refreshes cleanly

PASS when several catches in a row work without confusing behaviour.

## Q5 — Monster and timer

Run the lesson 5 result.

Check:

- monster starts moving
- monster continues moving without key presses
- it follows the player
- changing monster speed has a visible effect
- the window remains responsive

PASS when `ontimer()` behaviour is stable during normal play.

## Q6 — Lives and game over

Run the lesson 6 result.

Check:

- a monster hit removes one life
- player/monster reset prevents an obvious immediate chain of accidental hits
- life display updates
- zero lives produces GAME OVER
- active gameplay stops after GAME OVER

PASS when the complete lose-state is understandable and stable.

## Q7 — Complete reference mini-game

Run:

```text
python examples/m3-mini-game.py
```

Play long enough to:

1. move in all four directions
2. hit every screen edge
3. collect at least five targets
4. observe score updates
5. be caught by the monster
6. lose all lives
7. reach GAME OVER
8. close the window normally

Also check that visual feedback works. Sound is optional and must not be required for PASS.

PASS when the complete game remains responsive and all core rules work.

## Q8 — Child-facing usability

Using the course instructions rather than knowledge of the source code, check:

- lesson 1 gets to visible movement quickly
- instructions for clicking/focusing the Turtle window are sufficient
- error messages remain accessible when switching between editor/terminal and Turtle
- text is readable at a practical classroom display size
- no internet connection is needed for the core game
- no extra Python package installation is needed beyond a Python/Tk installation
- optional sound failure does not break the game

PASS when the environment is practical for the intended learner rather than merely technically functional.

## Q9 — Recovery test

Introduce one simple error, for example misspell a Turtle method.

Check that the learner workflow remains possible:

1. run
2. see the error
3. return to the source
4. fix it
5. run again
6. continue playing

PASS when a normal beginner mistake is recoverable without restarting the environment or losing the project.

## Result

M3 desktop qualification is PASS only when Q1–Q9 pass.

If something fails, classify it as:

- COURSE
- PYTHON
- TK
- EDITOR
- OS
- ACCESSIBILITY
- UNKNOWN

Fix course-owned problems before qualification. Environment-specific limitations may be documented when the core supported environment still passes.

## Evidence

Record the result in `docs/M3-TEST-RESULT.md`.

The qualification record must name the exact tested commit. Do not mark M3 PASS from CI alone.
