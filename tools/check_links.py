"""Check relative Markdown links inside the repository."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
errors = []

for document in ROOT.rglob("*.md"):
    text = document.read_text(encoding="utf-8")
    for target in LINK.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        path = (document.parent / target).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{document.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not path.exists():
            errors.append(f"{document.relative_to(ROOT)}: missing link target: {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Markdown links OK")
