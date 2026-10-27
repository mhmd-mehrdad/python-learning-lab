# Pong Game

A local two-player Pong game with paddles, scoring, and accelerating rallies.

## Features

- Keyboard-controlled paddles
- Wall and paddle collisions
- Automatic scoring
- Ball acceleration during a rally

## Technologies

Python, Turtle, time, random.

## Installation

```powershell
cd oop-games-gui/pong-game
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Left player: W/S. Right player: Up/Down arrows. Close the window to stop.
