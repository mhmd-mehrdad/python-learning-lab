# Tip Calculator

Calculates a per-person share of a bill including a percentage tip.

## Features

- Percentage arithmetic
- Rounded per-person result

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/tip-calculator
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter the bill, tip percentage, and number of people.

## Current limitations

Input is assumed to be numeric and the group size must be positive.
