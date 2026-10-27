# Calculator

An interactive arithmetic calculator that can reuse the previous result.

## Features

- Addition, subtraction, multiplication, division
- Chained calculations

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/calculator
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter operands and an operator. Type y to reuse the result or n to start again; press Ctrl+C to exit.

## Current limitations

Division by zero and invalid numeric input are not handled.
