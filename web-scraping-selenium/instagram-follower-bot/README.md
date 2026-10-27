# Follower Interface Automation

Signs into a demo social interface, opens an account follower list, and clicks follow buttons.

## Features

- Class-based Selenium workflow
- Account search
- Scrollable follower-list processing
- Processed-account tracking

## Technologies

Python, Selenium, time; Google Chrome.

## Installation

```powershell
cd web-scraping-selenium/instagram-follower-bot
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Configuration

`.env.example` documents the required settings. This script reads the process environment and does not automatically load `.env` files. Set the variables in the same terminal before starting:

```powershell
$env:FOLLOWER_USERNAME = 'replace-with-your-value'
$env:FOLLOWER_PASSWORD = 'replace-with-your-value'
$env:SIMILAR_ACCOUNT = 'replace-with-your-value'
$env:FOLLOWER_BASE_URL = 'replace-with-your-value'
```

Use your own configuration and keep credentials outside version control.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Configure a compatible demo endpoint, account, and target handle, then run. This performs follow actions in the configured interface.

## Current limitations

Selectors target a demo social interface, not the production Instagram website. The scroll termination check and short waits can miss content or fail on slow responses.
