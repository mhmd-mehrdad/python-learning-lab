# Password Generator

Builds a password candidate by placing random characters into a list.

## Features

- Letter, number, and symbol pools
- User-specified character counts

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/password-generator
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter the requested character counts and inspect the printed list.

## Current limitations

This prototype can reuse occupied slots and leave empty positions. It prints debugging details and a list rather than a finished string. It uses random, not a cryptographic generator; do not use its output for real credentials.
