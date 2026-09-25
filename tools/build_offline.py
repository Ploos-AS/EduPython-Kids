"""Build a self-contained EduPython Kids offline bundle."""

from __future__ import annotations

from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STAGE = DIST / "EduPython-Kids-offline"

INCLUDE_DIRS = (
    "course",
    "exercises",
    "examples",
    "teacher-guide",
    "printable",
    "docs",
    "tools",
)

INCLUDE_FILES = (
    "README.md",
    "MILESTONES.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
)


def copy_tree(name: str) -> None:
    source = ROOT / name
    if not source.exists():
        raise FileNotFoundError(source)
    shutil.copytree(source, STAGE / name)


def build() -> Path:
    if DIST.exists():
        shutil.rmtree(DIST)

    STAGE.mkdir(parents=True)

    for name in INCLUDE_DIRS:
        copy_tree(name)

    for name in INCLUDE_FILES:
        source = ROOT / name
        if not source.exists():
            raise FileNotFoundError(source)
        shutil.copy2(source, STAGE / name)

    (STAGE / "START-HERE.txt").write_text(
        """EduPython Kids — Offline Bundle

Start here:
  Course (Norwegian):  course/no/README.md
  Course (English):    course/en/README.md
  Exercises (NO):      exercises/no/README.md
  Exercises (EN):      exercises/en/README.md
  Teacher/parent (NO): teacher-guide/README.md
  Teacher/parent (EN): teacher-guide/en/README.md
  Printable sheets:    printable/README.md
  Installation (NO):   docs/no/INSTALL.md
  Installation (EN):   docs/INSTALL.md

Python Explorer is designed to work without accounts or cloud services.
Python itself must already be installed on the computer.

For Turtle lessons, the local Python installation also needs graphical
Tk/Turtle support.

Have fun changing the code!
""",
        encoding="utf-8",
    )

    archive = DIST / "EduPython-Kids-offline.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(STAGE.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(DIST))

    return archive


if __name__ == "__main__":
    archive = build()
    print(f"Built {archive.relative_to(ROOT)}")
