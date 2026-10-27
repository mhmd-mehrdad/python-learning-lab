# Workout Tracker

Parses natural-language exercise input through an API and writes workout rows to a spreadsheet endpoint.

## Features

- Exercise description input
- API response processing
- Timestamped workout rows
- Authenticated spreadsheet requests

## Technologies

Python, Requests, datetime, environment variables.

## Installation

```powershell
cd apis-automation/workout-tracker
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:API_KEY = 'replace-with-your-value'
$env:APP_ID = 'replace-with-your-value'
$env:EXERCISE_API_ENDPOINT = 'replace-with-your-value'
$env:SHEET_ENDPOINT = 'replace-with-your-value'
$env:SHEET_USERNAME = 'replace-with-your-value'
$env:SHEET_PASSWORD = 'replace-with-your-value'
$env:PROFILE_GENDER = 'replace-with-your-value'
$env:PROFILE_WEIGHT_KG = 'replace-with-your-value'
$env:PROFILE_HEIGHT_CM = 'replace-with-your-value'
$env:PROFILE_AGE = 'replace-with-your-value'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Configure your API and spreadsheet service, then describe an activity at the prompt. Running the script sends data and creates spreadsheet rows.

## Current limitations

The exercise endpoint must accept x-app-id/x-app-key headers and return an exercises list with name, duration_min, and nf_calories. The spreadsheet endpoint must accept a workout object. There is no retry/error-recovery logic.
