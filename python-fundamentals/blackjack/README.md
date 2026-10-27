# Blackjack

A simplified terminal card-total game against a computer dealer.

## Features

- Random card values
- Player draw prompts
- Dealer total comparison

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/blackjack
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Use y/n at the play and draw prompts.

## Current limitations

This implementation uses uniformly random values from 1 to 11, does not model a real deck or standard ace rules, and has incomplete handling when a player passes immediately.
