# Installation and classroom setup

EduPython Kids is offline-first and does not require an account or cloud service.

## Recommended beginner setup

Use a current Python 3 installation and a simple Python editor. A child should have an obvious **Run** button or an equally simple way to start a program.

The course itself has no third-party Python dependencies.

## Windows

1. Install Python 3 from the official Python distribution or use a trusted school-managed installation.
2. Open the chosen beginner editor.
3. Create a folder named `EduPython`.
4. Save each exercise as a `.py` file.
5. Test with `print("Hei!")`.

## macOS

Install a current Python 3 environment suitable for learning, then use the same course files. Avoid relying on an old system Python installation.

## Linux

Most distributions provide Python 3 through their package manager. Turtle also needs Tk support, which some distributions package separately.

Verify:

```bash
python3 --version
python3 -c "print('Hei!')"
```

## Raspberry Pi

Raspberry Pi OS with Python 3 is a good fit for the course. Course 1 does not require GPIO or other hardware.

## Turtle check

Run:

```bash
python3 -m turtle
```

If a graphics window appears, Turtle is ready. If it does not, check that Python Tk/Tkinter support is installed.

## Offline use

Clone or download the repository once. All Markdown lessons and Python examples can then be used without Internet access.

## Classroom recommendation

Prepare and test the machines before the first lesson. The first student session should begin with programming, not account creation or software troubleshooting.
