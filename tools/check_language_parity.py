"""Structural language-parity checks for EduPython Kids."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NO = ROOT / "course" / "no"
EN = ROOT / "course" / "en"

NO_FILES = {
    1: "01-hei-python.md", 2: "02-programmet-husker.md", 3: "03-input.md",
    4: "04-tall-og-kalkulator.md", 5: "05-if.md", 6: "06-tilfeldighet.md",
    7: "07-for-lokker.md", 8: "08-gjett-tallet.md", 9: "09-while.md",
    10: "10-gjett-flere-forsok.md", 11: "11-funksjoner.md", 12: "12-monsterkamp.md",
    13: "13-lister.md", 14: "14-turtle.md", 15: "15-turtle-monstre.md",
    16: "16-sluttprosjekt.md",
}
EN_FILES = {
    1: "01-hello-python.md", 2: "02-variables.md", 3: "03-input.md",
    4: "04-numbers-calculator.md", 5: "05-if.md", 6: "06-randomness.md",
    7: "07-for-loops.md", 8: "08-guess-number.md", 9: "09-while.md",
    10: "10-guess-again.md", 11: "11-functions.md", 12: "12-monster-battle.md",
    13: "13-lists.md", 14: "14-turtle.md", 15: "15-turtle-monster.md",
    16: "16-final-project.md",
}

def headings(text: str) -> int:
    return len(re.findall(r"^## ", text, flags=re.MULTILINE))

def main() -> int:
    errors = []
    for number in range(1, 17):
        no_path, en_path = NO / NO_FILES[number], EN / EN_FILES[number]
        if not no_path.is_file(): errors.append(f"missing Norwegian lesson {number}: {no_path.name}")
        if not en_path.is_file(): errors.append(f"missing English lesson {number}: {en_path.name}")
        if not no_path.is_file() or not en_path.is_file(): continue
        no_text, en_text = no_path.read_text(encoding="utf-8"), en_path.read_text(encoding="utf-8")
        if headings(en_text) < 5:
            errors.append(f"English lesson {number} looks incomplete: only {headings(en_text)} level-2 sections")
        if len(en_text.split()) < 80:
            errors.append(f"English lesson {number} looks incomplete: too little teaching text")
    if errors:
        print("Language parity: FAIL")
        for error in errors: print(error)
        return 1
    exercise_no = list((ROOT / "exercises" / "no").glob("[0-9][0-9]-*.md"))
    exercise_en = list((ROOT / "exercises" / "en").glob("[0-9][0-9]-*.md"))
    if len(exercise_no) != 16 or len(exercise_en) != 16:
        print(f"Language parity: FAIL — exercises NO={len(exercise_no)} EN={len(exercise_en)}")
        return 1
    printable_no = list((ROOT / "printable" / "no").glob("*.md"))
    printable_en = list((ROOT / "printable" / "en").glob("*.md"))
    if len(printable_no) != 4 or len(printable_en) != 4:
        print(f"Language parity: FAIL — printable sheets NO={len(printable_no)} EN={len(printable_en)}")
        return 1
    if not (EN / "STUDENT-CHECKLIST.md").is_file() or not (NO / "ELEV-SJEKKLISTE.md").is_file():
        print("Language parity: FAIL — student checklist missing in one language")
        return 1
    docs_required = (
        "docs/INSTALL.md", "docs/no/INSTALL.md",
        "docs/PROGRESSION.md", "docs/no/PROGRESSION.md",
        "docs/OFFLINE.md", "docs/no/OFFLINE.md",
        "docs/ACCESSIBILITY.md", "docs/en/ACCESSIBILITY.md", "docs/no/ACCESSIBILITY.md",
        "docs/VOCABULARY.md", "docs/en/VOCABULARY.md",
    )
    for name in docs_required:
        if not (ROOT / name).is_file():
            print(f"Language parity: FAIL — missing bilingual learner/support document: {name}")
            return 1
    teacher_en = ROOT / "teacher-guide" / "en"
    for name in ("README.md", "CHECKLIST.md", "PACING.md", "PROJECT-RUBRIC.md", "solutions/README.md"):
        if not (teacher_en / name).is_file():
            print(f"Language parity: FAIL — missing English teacher resource: {name}")
            return 1
    solution_no = list((ROOT / "teacher-guide" / "solutions").glob("[0-9][0-9]-[0-9][0-9].md"))
    solution_en = list((teacher_en / "solutions").glob("[0-9][0-9]-[0-9][0-9].md"))
    if len(solution_no) != 4 or len(solution_en) != 4:
        print(f"Language parity: FAIL — solution groups NO={len(solution_no)} EN={len(solution_en)}")
        return 1
    print("Language parity structure: PASS — core student and teacher resources exist in both Norwegian and English, including 4+4 solution groups.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
