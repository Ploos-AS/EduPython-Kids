from pathlib import Path
import subprocess
import sys
import zipfile


ROOT = Path(__file__).parents[1]


def test_offline_bundle_builds_and_contains_core_material():
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_offline.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr

    archive = ROOT / "dist" / "EduPython-Kids-offline.zip"
    assert archive.exists()

    with zipfile.ZipFile(archive) as zf:
        names = set(zf.namelist())

    required = {
        "EduPython-Kids-offline/START-HERE.txt",
        "EduPython-Kids-offline/course/no/README.md",
        "EduPython-Kids-offline/course/no/01-hei-python.md",
        "EduPython-Kids-offline/course/no/16-sluttprosjekt.md",
        "EduPython-Kids-offline/course/en/README.md",
        "EduPython-Kids-offline/course/en/16-final-project.md",
        "EduPython-Kids-offline/exercises/no/README.md",
        "EduPython-Kids-offline/exercises/en/README.md",
        "EduPython-Kids-offline/teacher-guide/README.md",
        "EduPython-Kids-offline/teacher-guide/en/README.md",
        "EduPython-Kids-offline/teacher-guide/en/solutions/13-16.md",
        "EduPython-Kids-offline/printable/README.md",
        "EduPython-Kids-offline/examples/hello.py",
        "EduPython-Kids-offline/docs/INSTALL.md",
        "EduPython-Kids-offline/docs/no/INSTALL.md",
        "EduPython-Kids-offline/docs/en/ACCESSIBILITY.md",
        "EduPython-Kids-offline/LICENSE.md",
    }
    assert required <= names
