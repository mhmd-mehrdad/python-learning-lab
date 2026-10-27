# Cookie Clicker Bot

Clicks cookies and periodically attempts to purchase an affordable product.

## Features

- Browser startup and language selection
- Repeated cookie clicks
- Periodic product inspection

## Technologies

Python, Selenium, time; Google Chrome.

## Installation

```powershell
cd web-scraping-selenium/cookie-clicker-bot
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Install Chrome before running. The script opens the game and loops until interrupted with Ctrl+C; close the detached browser separately.

## Current limitations

If no product is selected, best_item.click() can fail. Price parsing assumes integer text and may fail on formatted large values. Selectors depend on the game UI.
