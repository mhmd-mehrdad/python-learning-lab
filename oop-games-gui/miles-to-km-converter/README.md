# Miles to Kilometers Converter

Converts an integer distance in miles into kilometers in a desktop window.

## Features

- Tkinter form
- Button-driven conversion
- Result label

## Technologies

Python, Tkinter.

## Installation

```powershell
cd oop-games-gui/miles-to-km-converter
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter a whole number of miles and click CALCULATE.

## Current limitations

Uses the approximation 1 mile = 1.6 km. Decimal and invalid input are not handled.
