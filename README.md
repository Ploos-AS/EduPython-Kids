# EduPython Kids

**Learn programming by making things.**

EduPython Kids is a beginner-friendly Python course for children around 9–12 years old, with 10 years as the primary target age.

The course starts with immediate, playful results and introduces programming concepts gradually through experiments, small challenges, graphics, and games.

## Teaching principles

- zero programming prerequisites
- Norwegian-first, with English material planned
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

Python Explorer currently contains 16 Norwegian lessons:

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

Start with the [Norwegian course index](course/no/README.md). Extra practice is indexed in [Norwegian exercises](exercises/no/README.md).

Future courses are planned around game creation, physical computing, debugging/data exploration, and independent projects.

## Repository layout

```text
course/
  no/                    Norwegian student lessons
exercises/
  no/                    Norwegian practice and challenges
examples/                runnable Python examples
teacher-guide/           notes for teachers and parents
  solutions/             lesson-specific adult guidance
docs/                    installation, progression and terminology
tools/                   repository validation tools
tests/                   automated checks
.github/workflows/       CI
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

Course 1 is now in M1, focused on completeness, consistency, adult guidance and the English course skeleton.

See [MILESTONES.md](MILESTONES.md) for the roadmap and [M0 qualification](docs/M0-QUALIFICATION.md) for the foundation qualification record.

## Licensing

- Course material and documentation: **CC BY 4.0**
- Source code and examples: **MIT License**

See [LICENSE.md](LICENSE.md) for applicability details.

## Project

EduPython Kids is part of the Ploos AS educational project family.
