# Flash Card App

Displays French vocabulary cards, reveals translations, and records remaining words.

## Features

- Timed French-to-English card flip
- Known-word removal
- CSV progress persistence

## Technologies

Python, Tkinter, Pandas, random.

## Installation

```powershell
cd oop-games-gui/flash-card-app
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Use the green button to mark a word as known and the red button for another card. Delete the generated words_to_learn.csv to reset progress.

## Current limitations

Completing the final word leaves an empty pool and is not handled by the next-card routine.
