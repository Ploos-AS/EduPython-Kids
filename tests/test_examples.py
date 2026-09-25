import ast
from pathlib import Path


def test_all_examples_parse_as_python():
    examples = Path(__file__).parents[1] / "examples"
    files = sorted(examples.glob("*.py"))
    assert files, "No Python examples found"

    for path in files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_noninteractive_examples_run():
    import subprocess
    import sys

    root = Path(__file__).parents[1]
    for name in ("hello.py", "dice.py"):
        result = subprocess.run(
            [sys.executable, str(root / "examples" / name)],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
        assert result.returncode == 0, result.stderr
