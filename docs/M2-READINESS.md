# M2 Classroom Quality — readiness

**Repository-side status:** READY  
**Overall M2 status:** NOT YET QUALIFIED  
**Updated:** 2026-09-25

This document separates repository-verifiable work from the remaining real graphical qualification.

## Repository-side work

Implemented and CI-protected:

- 16-lesson Norwegian and English first-class course editions
- exercises for all 16 lessons in both languages
- student progress checklists in both languages
- four printable companion groups in both languages
- teacher/parent guidance, pacing, project rubric and four solution-note groups in both languages
- Course 1 language-parity policy and human qualification review
- learner-facing installation, progression, offline and accessibility guidance
- source-level accessibility review
- offline bundle builder with bilingual-content verification
- GitHub Pages source and deployment workflow
- Turtle/Tk qualification procedure, result form and graphical smoke-test helper

The CI helpers verify repository readiness, internal links, Python syntax/tests and structural language parity.

## Language parity

**Status: PASS WITH CONTINUOUS REVIEW**

See [LANGUAGE-PARITY-QUALIFICATION.md](LANGUAGE-PARITY-QUALIFICATION.md).

Norwegian remains the primary authoring language; Norwegian and English are equal first-class Course 1 editions. Automated checks protect structure while human review remains necessary for pedagogical quality.

## External gate A — GitHub Pages

**Status: PASS**

Pages has repeatedly deployed successfully. A later confirmed deployment is Actions run `36186696779` for commit `5010d31f06b759d135918eb2957d804654f968ee`.

## External gate B — Turtle/Tk

**Status: READY FOR HANDS-ON TESTING**

Follow [TURTLE-QUALIFICATION.md](TURTLE-QUALIFICATION.md) and record evidence in [TURTLE-TEST-RESULT.md](TURTLE-TEST-RESULT.md).

At least one actual graphical desktop environment must be recorded. The report must state exactly what was physically tested and must not imply coverage of untested operating systems.

## Latest repository evidence

CI run `36186696660` for commit `5010d31f06b759d135918eb2957d804654f968ee` completed successfully.

That run includes bilingual offline-bundle verification, language-parity checks, M2 readiness checks and the accurately named headless Turtle-helper syntax check.

## M2 qualification rule

M2 can be marked PASS only when repository CI/readiness is green, Pages has a successful deployment, and Turtle/Tk has a recorded Q1–Q6 hands-on PASS.

A headless runner cannot prove that a learner can use a real Tk window. This external gate therefore remains deliberately separate.
