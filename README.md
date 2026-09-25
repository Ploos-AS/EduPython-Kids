# EduPython Kids

[![CI](https://github.com/Ploos-AS/EduPython-Kids/actions/workflows/ci.yml/badge.svg)](https://github.com/Ploos-AS/EduPython-Kids/actions/workflows/ci.yml)
[![Pages](https://github.com/Ploos-AS/EduPython-Kids/actions/workflows/pages.yml/badge.svg)](https://github.com/Ploos-AS/EduPython-Kids/actions/workflows/pages.yml)
[![Course material: CC BY 4.0](https://img.shields.io/badge/course-CC%20BY%204.0-blue.svg)](LICENSE.md)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE.md)

**Learn programming by making things.**

EduPython Kids is a beginner-friendly Python course for children around 9–12 years old, with 10 years as the primary target age.

The course starts with immediate, playful results and introduces programming concepts gradually through experiments, small challenges, graphics, and games.

## Teaching principles

- zero programming prerequisites
- Norwegian is the primary authoring language; Norwegian and English are equally supported course editions
- short lessons with visible results
- learn by changing and experimenting with working programs
- debugging is a normal and useful part of programming
- no proprietary learning platform required
- usable offline on Linux, Windows, macOS, and Raspberry Pi
- open educational material and open source examples

## Teaching model

Each lesson follows the same basic rhythm:

1. **Oppdrag** – something concrete to make
2. **Kode** – a small working program
3. **Kjør** – run it and see what happens
4. **Endre** – change something
5. **Tenk** – predict and explain what changed
6. **Utfordring** – extend the program yourself

The guiding principle is:

> Make something fun first. Explain why it works afterwards.

## Course 1 — Python Explorer

Python Explorer contains 16 lessons in both Norwegian and English:

1. Hello, Python! — `print()`
2. My program remembers — variables
3. Talk to the computer — `input()`
4. Numbers and a mini calculator
5. Make choices — `if`
6. Randomness — dice and chance
7. Repeat a known number of times — `for`
8. First guessing game
9. Keep going — `while`
10. Guessing game with multiple attempts
11. Make your own commands — functions
12. Project — Monster Battle
13. Collections — lists
14. Draw with Turtle
15. Turtle project — Robot Monster
16. Final independent project

Start with the [Norwegian course index](course/no/README.md) or the [English course index](course/en/README.md). Norwegian is the primary authoring language, while both Norwegian and English are first-class supported editions. See [language parity policy](docs/LANGUAGE-PARITY.md).

Future courses are planned around game creation, physical computing, debugging/data exploration, and independent projects.

## Repository layout

```text
course/
  no/                    Norwegian student lessons
  en/                    English edition (in progress)
exercises/
  no/                    Norwegian practice and challenges
examples/                runnable Python examples
teacher-guide/           notes for teachers and parents
  solutions/             lesson-specific adult guidance
printable/               print-friendly classroom companions
docs/                    installation, progression, accessibility and qualification
tools/                   repository validation and offline tools
tests/                   automated checks
.github/workflows/       CI and Pages deployment
```

## Quick start

Python 3.11 or newer is recommended.

```bash
python examples/hello.py
python examples/talk.py
python examples/dice.py
```

See [installation guidance](docs/INSTALL.md) for classroom setup. Turtle examples require a Python installation with Tk support.

## Status

**M0 — Foundation: PASS**

**M1 — Python Explorer complete: PASS**

**M2 — Classroom Quality: pending hands-on Turtle/Tk qualification**

M2 repository work, CI and GitHub Pages deployment are complete. The milestone deliberately remains open until the documented Q1–Q6 Turtle/Tk workflow has passed on a real graphical desktop environment.

See [MILESTONES.md](MILESTONES.md), the [M2 readiness report](docs/M2-READINESS.md), and the [M2 qualification report](docs/M2-QUALIFICATION.md).

## Licensing

- Course material and documentation: **CC BY 4.0**
- Source code and examples: **MIT License**

See [LICENSE.md](LICENSE.md) for applicability details.

## Project

EduPython Kids is part of the Ploos AS educational project family.
