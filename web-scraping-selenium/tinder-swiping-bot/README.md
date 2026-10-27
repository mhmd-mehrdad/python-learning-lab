# Dating Interface Automation

Automates a demo dating interface login flow and performs a single like action.

## Features

- Login popup window switching
- Consent dialog interaction
- Single like-button click

## Technologies

Python, Selenium, time; Google Chrome.

## Installation

```powershell
cd web-scraping-selenium/tinder-swiping-bot
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:ACCOUNT_EMAIL = 'replace-with-your-value'
$env:ACCOUNT_PASSWORD = 'replace-with-your-value'
$env:DATING_APP_URL = 'replace-with-your-value'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Configure the compatible demo endpoint and account, install Chrome, then run. This performs a like action in the configured demo.

## Current limitations

The selectors target a specific demo interface, not the production Tinder website. There is no continuous swipe loop. A compatible endpoint is required; changing the URL alone does not make other sites compatible.
