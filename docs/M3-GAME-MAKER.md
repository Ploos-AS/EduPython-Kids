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

## Proposed course path

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

- the 10-year-old-first teaching rules are documented
- the 10-lesson progression is agreed
- the graphical library/runtime choice is documented and tested on supported desktop environments
- lesson 1 has a runnable minimal prototype
- CI can test non-graphical logic without pretending that headless CI qualifies the graphical experience
