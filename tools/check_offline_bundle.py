"""Validate the built offline bundle, including M3 Game Maker."""

from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "dist" / "EduPython-Kids-offline.zip"
PREFIX = "EduPython-Kids-offline/"

NO_M3 = [
    "m3-01-flytt.md", "m3-02-hold-deg-pa-skjermen.md",
    "m3-03-fang-stjernen.md", "m3-04-poeng.md", "m3-05-monsteret.md",
    "m3-06-tre-liv.md", "m3-07-gjor-spillet-ditt.md", "m3-08-lyd-og-jubel.md",
    "m3-09-mini-spill.md", "m3-10-mitt-spill.md",
]
EN_M3 = [
    "m3-01-move.md", "m3-02-stay-on-screen.md", "m3-03-catch-the-star.md",
    "m3-04-score.md", "m3-05-watch-out.md", "m3-06-three-lives.md",
    "m3-07-make-it-yours.md", "m3-08-sound-and-celebration.md",
    "m3-09-mini-game.md", "m3-10-my-game.md",
]


def main() -> int:
    if not ARCHIVE.is_file():
        print(f"Offline bundle: FAIL — missing {ARCHIVE.relative_to(ROOT)}")
        return 1

    required = {
        PREFIX + "START-HERE.txt",
        PREFIX + "course/no/README.md",
        PREFIX + "course/en/README.md",
        PREFIX + "examples/m3-mini-game.py",
        *(PREFIX + "course/no/" + name for name in NO_M3),
        *(PREFIX + "course/en/" + name for name in EN_M3),
    }

    with zipfile.ZipFile(ARCHIVE) as zf:
        names = set(zf.namelist())
        missing = sorted(required - names)
        if missing:
            print("Offline bundle: FAIL — required files missing:")
            for name in missing:
                print(name)
            return 1

        start = zf.read(PREFIX + "START-HERE.txt").decode("utf-8")
        for phrase in ("Python Explorer + Game Maker (NO)", "Python Explorer + Game Maker (EN)", "examples/m3-mini-game.py"):
            if phrase not in start:
                print(f"Offline bundle: FAIL — START-HERE missing {phrase!r}")
                return 1

    print("Offline bundle: PASS — M3 NO/EN lessons, reference game and start links present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
