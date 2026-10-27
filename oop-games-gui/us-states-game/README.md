# U.S. States Game

Labels correctly guessed U.S. states on a map using CSV coordinates.

## Features

- State-name input and validation
- Score display
- Export of unguessed states

## Technologies

Python, Turtle, Pandas, CSV data.

## Installation

```powershell
cd oop-games-gui/us-states-game
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter state names in the dialog. Enter Exit or cancel to export states_to_learn.csv.
