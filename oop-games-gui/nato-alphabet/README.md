# NATO Alphabet

Converts entered letters into NATO phonetic alphabet words using CSV data.

## Features

- CSV lookup table
- Dictionary comprehension
- Case-normalized lookup

## Technologies

Python, Pandas.

## Installation

```powershell
cd oop-games-gui/nato-alphabet
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter a name containing alphabetic characters.

## Current limitations

Spaces, punctuation, and characters not in the CSV raise KeyError.
