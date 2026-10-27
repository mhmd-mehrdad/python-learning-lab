# Rock Paper Scissors

Plays a terminal round against a randomly selected computer move.

## Features

- ASCII move illustrations
- Win, loss, and draw comparisons

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/rock-paper-scissors
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Choose 0 for rock, 1 for paper, or 2 for scissors.

## Current limitations

Unsupported or nonnumeric choices are not safely validated.
