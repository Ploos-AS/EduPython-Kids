# Offline bundle

EduPython Kids is designed to be usable without student accounts, cloud services or a permanent internet connection.

## Build

From the repository root:

```bash
python tools/build_offline.py
```

This creates:

```text
dist/
├── EduPython-Kids-offline/
└── EduPython-Kids-offline.zip
```

The archive contains:

- complete Norwegian Python Explorer lessons
- complete English Python Explorer lessons
- Norwegian and English exercises
- runnable examples
- Norwegian and English teacher/parent material
- Norwegian and English printable worksheets
- installation and supporting documentation
- licensing and contribution information
- a plain-text `START-HERE.txt`

CI, repository tests, Git metadata and development-only tooling are intentionally not required inside the learner bundle.

## Classroom use

Build the archive on a connected machine, copy it to classroom machines using approved local storage, extract it and open `START-HERE.txt`.

Python must already be installed. See [INSTALL.md](INSTALL.md).

Turtle lessons additionally require local Tk/Turtle graphical support.

## Offline does not mean installation-free

The bundle removes the need to browse GitHub during a lesson. It does not bundle a Python interpreter.

A future zero-install/browser path may complement this, but Python Explorer's real-Python path remains fully usable offline once Python is installed.

## Privacy

No account, analytics service or network request is required by the course materials or standard Python examples.

Teachers should still follow their organisation's normal rules for handling student files and removable media.
