# Turtle Race

Animates a race among six turtles with randomized movement.

## Features

- Six colored competitors
- Color prediction prompt
- Console winner output

## Technologies

Python, Turtle, random.

## Installation

```powershell
cd oop-games-gui/turtle-race
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter a turtle color in the dialog, then watch the race. Click the window to close.

## Current limitations

The entered prediction enables the race, but the program only prints the winning color; it does not evaluate the prediction.
