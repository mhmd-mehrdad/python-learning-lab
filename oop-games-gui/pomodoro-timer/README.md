# Pomodoro Timer

Alternates timed work sessions with short and long breaks.

## Features

- 25-minute work intervals
- 5-minute short breaks
- 20-minute long breaks
- Tkinter countdown display

## Technologies

Python, Tkinter, math.

## Installation

```powershell
cd oop-games-gui/pomodoro-timer
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Click START once to begin. Close the window to stop the timer.

## Current limitations

RESET has no callback. Repeated START clicks can create overlapping countdowns. Session labels/checkmarks are not updated.
