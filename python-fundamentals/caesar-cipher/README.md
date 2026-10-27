# Caesar Cipher

Shifts alphabetic characters using modular arithmetic.

## Features

- Encode and decode prompts
- Alphabet wraparound

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/caesar-cipher
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Choose encode or decode, then enter lowercase letters and a numeric shift.

## Current limitations

Only letters a-z are supported. Decode toggles the shift sign inside the loop, so multi-character decoding is incorrect. This cipher provides no meaningful security.
