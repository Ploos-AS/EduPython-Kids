# Accessibility review

**Review scope:** Python Explorer M2 classroom materials  
**Review date:** 2026-09-25

EduPython Kids should be usable by as many learners as practical without requiring one specific way to read, type, see, hear or complete an exercise.

Accessibility is an ongoing design constraint, not a one-time certification.

## Review principles

### 1. Do not depend on colour

Course meaning must not depend on colour alone.

The lesson icons such as 🎯, 💻, 🔧 and 🐞 are helpful visual landmarks, but the text labels beside them carry the meaning. A learner who does not see the icon still receives the instruction.

Printable material is designed to work in monochrome.

**Status: PASS**

### 2. Do not depend on emoji

Emoji may render differently or be unavailable in some environments.

Every emoji heading therefore includes a text label such as “Oppdrag”, “Kode”, “Endre”, “Tenk” or “Bug-jakt”. Emoji are decoration and navigation aids, not required information.

**Status: PASS**

### 3. Keep language concrete

For the primary audience, instructions should:

- use short sentences
- introduce terminology after or beside a concrete example
- avoid unnecessary jargon
- explain one or two major new ideas at a time
- prefer direct verbs such as “kjør”, “endre”, “test” and “skriv”
- explain errors as information rather than failure

The vocabulary guide defines consistent beginner terminology.

**Status: PASS**

### 4. Reduce memory load

Learners should not need to memorise syntax before they can experiment.

Lessons provide working examples first. Learners are encouraged to change, predict and run code. The final project explicitly values explaining code over memorising syntax.

Adults may remind learners of earlier syntax and let them copy a working pattern.

**Status: PASS**

### 5. Support different reading speeds

Pacing plans are guides rather than deadlines. Optional challenges may be skipped or continued later.

A learner should not be judged by how quickly they finish a lesson.

**Status: PASS**

### 6. Support typing and motor differences

Typing speed is not the learning objective.

Adults may:

- provide starter files
- type dictated code when appropriate
- allow copy/paste from canonical examples
- use a larger keyboard or alternative input device
- give extra time
- split a project across sessions

The learner should still make meaningful choices about the program even when someone else assists with physical input.

**Status: PASS with classroom accommodation**

### 7. Keyboard-first operation

The core text-programming lessons can be completed from a keyboard in a suitable editor and terminal.

Turtle introduces a graphical window, but the learning task does not require precise mouse drawing; the learner controls the drawing through code.

Editor-specific keyboard accessibility is outside the repository's direct control and should be checked on classroom machines.

**Status: PASS for course design; environment check required**

### 8. Screen readers and text structure

Markdown uses semantic headings, lists, code blocks and ordinary links. Instructions should not refer only to visual position such as “the green box on the right”.

ASCII punctuation and text labels carry the instructional meaning.

Code itself may still be demanding with a screen reader because punctuation and indentation are meaningful in Python. A learner may need editor configuration or adult support.

**Status: REVIEW IN CLASSROOM ENVIRONMENT**

### 9. Font size and zoom

The repository does not require a fixed font size. Markdown and future web/PDF presentations should remain readable when enlarged.

Future GitHub Pages styling must avoid fixed layouts that break at high zoom.

Printable/PDF work should use a readable body size and leave generous writing space.

**Status: REQUIREMENT RECORDED**

### 10. Do not rely on sound

No current Python Explorer lesson requires audio to understand instructions or complete an exercise.

**Status: PASS**

### 11. Do not rely on time pressure

There are no timed programming tasks. Randomness is used for games, not for measuring learner speed.

**Status: PASS**

### 12. Error handling and emotional load

Errors are treated as normal program feedback.

Teacher guidance should avoid language that labels a learner as “good”, “bad”, “slow” or “weak”. The project rubric describes the current work, not the child.

When a learner is stuck, prefer:

1. read the error
2. find the referenced line
3. test one small part
4. change one thing
5. run again

**Status: PASS**

### 13. Privacy and safe examples

Exercises do not require real names, addresses, schools, passwords or other unnecessary personal information.

Fictional characters, nicknames and invented data are preferred.

**Status: PASS**

## Known accessibility risks

The main remaining risks are environmental rather than conceptual:

- editor and terminal screen-reader behaviour
- Python indentation with assistive technology
- Turtle/Tk behaviour on classroom machines
- future PDF page layout and font sizing
- future GitHub Pages keyboard, zoom and contrast behaviour

These should be included in hands-on M2 qualification rather than assumed from source review.

## Classroom accessibility checklist

Before teaching, check:

- [ ] learner can comfortably read or access the lesson text
- [ ] editor text can be enlarged
- [ ] keyboard or alternative input method works
- [ ] terminal output is readable
- [ ] required assistive technology works with the chosen editor
- [ ] learner can access punctuation needed for Python
- [ ] starter files are available if typing is a barrier
- [ ] no activity depends on colour or sound alone
- [ ] enough time is available without speed pressure
- [ ] Turtle/Tk is tested before graphical lessons

## Future web and PDF requirements

When GitHub Pages and generated PDFs are introduced:

- preserve semantic heading order
- provide meaningful link text
- maintain visible keyboard focus
- avoid colour-only status indicators
- provide sufficient text/background contrast
- support browser zoom and narrow viewports
- avoid essential information embedded only in images
- add alternative text to meaningful images
- keep decorative images out of the reading flow where possible
- verify generated PDFs for reading order and usable text extraction

## Result

**M2 source-level accessibility review: PASS**

This PASS means the current course content and teaching design do not contain an identified source-level accessibility blocker.

It does **not** claim formal WCAG conformance or qualification of every editor, operating system, browser, PDF reader or assistive-technology combination. Those require testing of the actual delivery environment.
