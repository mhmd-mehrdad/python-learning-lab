# Flask Routes

A small Flask application serving two text routes.

## Features

- Root greeting route
- Goodbye route

## Technologies

Python, Flask.

## Installation

```powershell
cd flask-web-apps/flask-introduction
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Visit http://127.0.0.1:5000/ and /bye. Stop the local server with Ctrl+C.

## Current limitations

Uses Flask's local development server; deployment configuration is not included.
