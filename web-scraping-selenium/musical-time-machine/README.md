# Musical Time Machine

Scrapes chart song titles for a date and builds a YouTube Music playlist.

## Features

- Date-based chart retrieval
- Song search
- Playlist creation and population

## Technologies

Python, Requests, BeautifulSoup, ytmusicapi.

## Installation

```powershell
cd web-scraping-selenium/musical-time-machine
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Set `$env:CHART_URL_TEMPLATE` to a compatible chart-page URL containing `{date}` where the entered date belongs. `.env.example` documents the variable; this script reads the process environment and does not automatically load `.env` files. The page must expose song headings as `h3.chart-entry__title`. The URL is configurable because the scraper is tied to a specific page structure.

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Create a local browser.json using the authentication setup supported by your ytmusicapi installation. Enter the chart date when prompted. Running this script creates a playlist in the authenticated account.

## Current limitations

Chart HTML and authentication formats may change. Song matching takes the first search result. Failed/empty responses are not handled.

## Local authentication

`browser.json` is required at runtime and deliberately excluded from version control. It contains sensitive browser headers/cookies. Create your own file locally; never paste its contents into issues, logs, or commits.
