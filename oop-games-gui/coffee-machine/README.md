# Coffee Machine

Models drink recipes, ingredient availability, and coin payments in a terminal interface.

## Features

- Recipe dictionary
- Resource checks
- Coin-value calculation

## Technologies

Python standard library; dictionaries and functions.

## Installation

```powershell
cd oop-games-gui/coffee-machine
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter espresso, latte, cappuccino, or report. Press Ctrl+C to exit.

## Current limitations

The money accumulator is referenced without initialization, so report/payment paths currently raise NameError. Exit and payment-accounting behavior are unfinished. The original implementation is retained for review.
