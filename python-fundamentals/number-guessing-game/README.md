# Number Guessing Game

Asks the player to identify a random integer using high/low feedback.

## Features

- Random target from 1 to 100
- Attempt counter
- High and low hints

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/number-guessing-game
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Choose easy or hard, then enter integer guesses.

## Current limitations

Both difficulty choices currently allow ten guesses. Unsupported difficulty input is not handled safely.
