# Higher Lower Game

Compares follower counts from a local profile dataset.

## Features

- Random profile pairs
- Score tracking across correct comparisons

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/higher-lower-game
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Choose A or B to identify the profile with more followers.

## Current limitations

Counts are a static dataset and are not live social-media statistics. Unrecognized choices are treated as B.
