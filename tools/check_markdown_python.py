"""Check Python fenced code blocks in course Markdown for syntax errors."""

from pathlib import Path
import ast
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
PYTHON_BLOCK = re.compile(r"```python\s*\n(.*?)```", re.DOTALL)


def main() -> int:
    errors = []
    checked = 0
    for path in sorted(COURSE.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for number, match in enumerate(PYTHON_BLOCK.finditer(text), start=1):
            code = match.group(1)
            checked += 1
            try:
                ast.parse(code, filename=f"{path} python block {number}")
            except SyntaxError as exc:
                line = exc.lineno or "?"
                errors.append(f"{path.relative_to(ROOT)}: Python block {number}, line {line}: {exc.msg}")
    if errors:
        print("Markdown Python syntax: FAIL")
        for error in errors:
            print(error)
        return 1
    print(f"Markdown Python syntax: PASS — {checked} Python blocks parsed.")
    print("Note: snippets are parsed, not executed; GUI behaviour still needs desktop qualification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
