# Stock and News Prototype

Queries daily stock prices and calculates a percentage change for fixed dates.

## Features

- Stock API request
- Daily close comparison
- News endpoint request

## Technologies

Python, Requests.

## Installation

```powershell
cd apis-automation/stock-news-alert
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:STOCK_API_KEY = 'replace-with-your-value'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Set the stock API key before running. Inspect terminal output; the code currently uses fixed historical dates.

## Current limitations

Fixed historical dates may be unavailable in the response. The news request has no API key or search parameters. No notification delivery is implemented.
