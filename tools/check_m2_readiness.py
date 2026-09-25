"""Check repository-side M2 classroom-quality readiness."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "teacher-guide/PACING.md",
    "printable/README.md",
    "printable/no/01-04-oppdag.md",
    "printable/no/05-08-velg.md",
    "printable/no/09-12-bygg.md",
    "printable/no/13-16-skap.md",
    "docs/ACCESSIBILITY.md",
    "docs/OFFLINE.md",
    "tools/build_offline.py",
    "tests/test_offline_bundle.py",
    "index.md",
    "_config.yml",
    ".github/workflows/pages.yml",
    "docs/TURTLE-QUALIFICATION.md",
)


def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        print("M2 repository readiness: FAIL")
        for name in missing:
            print(f"missing: {name}")
        return 1

    print("M2 repository readiness: PASS")
    print("External gates remain: GitHub Pages deployment and hands-on Turtle/Tk testing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
