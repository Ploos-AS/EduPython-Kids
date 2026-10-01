# M3 — Python Game Maker

## Goal

**I made my own game!**

M3 is for the same primary learner as EduPython Kids: a 10-year-old who has completed Python Explorer. It is not an adult game-programming course with simplified wording.

The learner should see something fun happen quickly, then discover the Python idea that made it happen.

## Teaching rules

Every lesson follows the familiar rhythm:

**Mission → Code → Run → Change → Think → Challenge**

- visible result early
- one main new idea at a time
- short working starter programs rather than large blank files
- real Python throughout
- explain technical vocabulary only when the learner needs it
- prefer experiments and predictions to long explanations
- bugs are expected and useful
- no game-engine architecture, classes, vectors or formal collision theory as prerequisites
- Norwegian is authored first; English remains an equal supported edition

## Course path

1. **Move!** — open a game window and move a character with the arrow keys.
2. **Stay on screen!** — discover positions and screen edges by experimenting.
3. **Catch the star!** — place and collect an object.
4. **Score!** — make the game remember and show points.
5. **Watch out!** — add a moving monster and a simple hit test.
6. **Three lives** — change what happens after a hit and restart safely.
7. **Make it yours** — change shapes, speed, background and game rules.
8. **Sound and celebration** — optional simple feedback where the platform supports it.
9. **Build a mini-game** — combine movement, collecting, danger and score.
10. **My game** — capstone: choose a theme, change rules, test it with another person, and explain one part of the code.

## Runtime choice

M3 core uses Python's standard `turtle` module on Tk. This continues directly from Python Explorer lessons 14–15, works offline, and avoids adding a package-install step before a child can make something move.

Headless CI may compile and inspect the Python source, but it does **not** qualify the graphical experience. Real Turtle/Tk desktop testing remains required. Sound is optional; visual feedback is the portable baseline.

## Scope guard

M3 introduces coordinates and collision through things the child can see:

- “Where is my character?”
- “Did I touch the star?”
- “Did the monster catch me?”

Formal terminology can be added after the behaviour is familiar.

Sprites do not require an asset pipeline. Early lessons may use simple built-in shapes so that installation and file management do not get in the way of programming.

Sound must be optional or have a silent fallback so the core course remains portable and usable offline.

## M3.0 exit criteria

M3.0 is complete when:

- [x] the 10-year-old-first teaching rules are documented
- [x] the 10-lesson progression is agreed
- [x] the Turtle/Tk runtime choice is documented
- [x] all 10 lessons exist in Norwegian and English
- [x] lesson 1 has a runnable minimal prototype
- [x] the complete shared mini-game reference is included
- [x] CI validates runnable Python snippets and intentional bug-hunt snippets
- [x] CI compiles runnable examples on the supported Python matrix without pretending that headless CI qualifies the graphical experience
- [x] CI builds the offline ZIP and verifies all 20 M3 lesson files, the reference game and start links
- [ ] Turtle/Tk Q1–Q9 passes on a real graphical desktop environment
- [ ] the tested commit and environment are recorded in `M3-TEST-RESULT.md`

The hands-on procedure is defined in [M3-QUALIFICATION.md](M3-QUALIFICATION.md). Until those final two checks pass, M3 remains **content complete; qualification pending**.
