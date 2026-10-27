# Dot Painting

Draws two randomly colored dots from a fixed RGB palette.

## Features

- RGB color tuples
- Random palette selection
- Turtle drawing

## Technologies

Python, Turtle, random; colorgram.py is imported.

## Installation

```powershell
cd oop-games-gui/hirst-painting
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Run the script and click the drawing window to close it.

## Current limitations

The current implementation draws two dots, not a full painting grid. Image color extraction is not active. The unused local source photograph is excluded.

## Dependency reference

The `colorgram` import is supplied by [colorgram.py](https://pypi.org/project/colorgram.py/).
