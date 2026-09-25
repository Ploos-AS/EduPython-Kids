# M2 Classroom Quality — readiness

**Repository-side status:** READY  
**Overall M2 status:** NOT YET QUALIFIED

This document separates work that can be verified in the repository from work that requires a real external environment.

## Repository-side work

The following M2 material is implemented:

- printable companion sheets for all 16 lessons
- teacher pacing for 30, 45 and 60 minute sessions
- source-level accessibility review
- offline bundle builder and automated bundle test
- student progress checklist
- GitHub Pages source and deployment workflow
- Turtle/Tk hands-on qualification procedure

The CI helper `tools/check_m2_readiness.py` verifies that these required repository artifacts remain present.

## External gate A — GitHub Pages

**Status: BLOCKED ON REPOSITORY SETTING**

The Pages source and workflow exist, but GitHub Pages must be enabled for the repository with **GitHub Actions** selected as the deployment source.

After enablement:

1. run or trigger the Pages workflow
2. verify build PASS
3. verify deploy PASS
4. open the published site
5. verify the home page and several lesson links
6. record the deployed URL and workflow run in the M2 qualification report

Do not mark this gate PASS based only on the workflow file existing.

## External gate B — Turtle/Tk

**Status: READY FOR HANDS-ON TESTING**

Follow [TURTLE-QUALIFICATION.md](TURTLE-QUALIFICATION.md).

At least one actual graphical desktop environment must be recorded. The final M2 report must say exactly which environments were tested; it must not imply untested operating systems were qualified.

## M2 qualification rule

M2 can be marked PASS only when:

- repository CI is green
- repository-side readiness check is green
- Pages has a successful real deployment
- Turtle/Tk has a recorded hands-on PASS

Additional platforms can be qualified later without invalidating the initial M2 PASS, provided the report clearly states the tested platform coverage.

## Why the gates are separate

A headless CI runner can validate source files, links, tests and the offline archive. It cannot prove that a learner can use a real Tk graphical window.

Likewise, a correct Pages workflow cannot publish a site when repository-level Pages configuration denies deployment.

Keeping these as explicit external gates prevents the milestone from claiming more than was actually tested.
