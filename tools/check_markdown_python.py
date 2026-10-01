"""Validate Python fenced code blocks in course Markdown."""

from pathlib import Path
import ast
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
PYTHON_BLOCK = re.compile(r"```python\s*\n(.*?)```", re.DOTALL)
BUG_BLOCK = re.compile(r"```python-bug\s*\n(.*?)```", re.DOTALL)


def main() -> int:
    errors = []
    valid_checked = 0
    bugs_checked = 0

    for path in sorted(COURSE.rglob("*.md")):
        text = path.read_text(encoding="utf-8")

        for number, match in enumerate(PYTHON_BLOCK.finditer(text), start=1):
            code = match.group(1)
            valid_checked += 1
            try:
                ast.parse(code, filename=f"{path} python block {number}")
            except SyntaxError as exc:
                line = exc.lineno or "?"
                errors.append(
                    f"{path.relative_to(ROOT)}: Python block {number}, "
                    f"line {line}: expected valid Python, got {exc.msg}"
                )

        for number, match in enumerate(BUG_BLOCK.finditer(text), start=1):
            code = match.group(1)
            bugs_checked += 1
            try:
                ast.parse(code, filename=f"{path} python-bug block {number}")
            except SyntaxError:
                continue
            errors.append(
                f"{path.relative_to(ROOT)}: python-bug block {number} is valid Python; "
                "bug-hunt blocks must contain an intentional syntax error"
            )

    if errors:
        print("Markdown Python syntax contract: FAIL")
        for error in errors:
            print(error)
        return 1

    print(
        "Markdown Python syntax contract: PASS — "
        f"{valid_checked} runnable snippets parsed; "
        f"{bugs_checked} intentional syntax bugs confirmed."
    )
    print("GUI behaviour still requires desktop qualification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
