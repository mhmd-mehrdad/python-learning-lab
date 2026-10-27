# Snake Game

An object-oriented Snake game with food, growth, collision resets, and a saved high score.

## Features

- Arrow-key movement
- Food collection and growth
- Wall and self-collision resets
- High-score persistence

## Technologies

Python, Turtle, time, random.

## Installation

```powershell
cd oop-games-gui/snake-game
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Use the arrow keys to steer. Collisions reset the snake and score. Close the window to stop.

## Saved score

`data.txt` starts at zero and stores the local high score. The initial file is included because the program reads it on startup. Runtime changes need not be committed.
