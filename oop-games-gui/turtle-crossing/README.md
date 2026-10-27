# Turtle Crossing

A road-crossing game with moving cars and progressively faster traffic.

## Features

- Keyboard movement
- Random car generation
- Collision detection
- Level progression

## Technologies

Python, Turtle, time, random.

## Installation

```powershell
cd oop-games-gui/turtle-crossing
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Press W to move forward. Reach the top to advance a level; hitting a car ends the game. Click the window after game over to close it.
