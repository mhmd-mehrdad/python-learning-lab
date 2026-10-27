# Rain Alert

A weather-response prototype that checks condition codes and prints an umbrella reminder.

## Features

- Weather API request
- Condition-code comparison

## Technologies

Python, Requests.

## Installation

```powershell
cd apis-automation/rain-alert
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:WEATHER_API_KEY = 'replace-with-your-value'
$env:WEATHER_LATITUDE = '0'
$env:WEATHER_LONGITUDE = '0'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Set weather configuration, then run the script. It prints a reminder if the processed conditions match.

## Current limitations

The current-weather endpoint does not match the forecast-style list expected by this implementation. It can raise KeyError and is not a working forecast alert. No text/email notification is implemented.
