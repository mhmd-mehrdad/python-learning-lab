# Habit Tracker Configuration

Builds account, graph, and daily-entry request payloads for Pixela.

## Features

- Graph configuration
- Daily quantity payload
- Token-header construction

## Technologies

Python, Requests, datetime.

## Installation

```powershell
cd apis-automation/habit-tracker
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:PIXELA_USERNAME = 'replace-with-your-value'
$env:PIXELA_TOKEN = 'replace-with-your-value'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Set account values and run the script to construct request configuration. No request is sent and no output is printed.

## Current limitations

This is configuration-only code. Account creation, graph creation, entry submission, update, and deletion are not active.
