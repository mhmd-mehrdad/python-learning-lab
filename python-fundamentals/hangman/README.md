# Hangman

A terminal word-guessing game with staged ASCII illustrations.

## Features

- Letter guesses
- Persistent revealed-letter display
- ASCII life stages

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/hangman
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter one lowercase letter at a time.

## Current limitations

The selected word is printed. Exhausted lives do not stop the loop, which can eventually raise an indexing error.
