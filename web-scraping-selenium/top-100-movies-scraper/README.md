# Top Movies Scraper

Extracts ranked movie headings from an archived film article and writes them to a text file.

## Features

- HTTP page retrieval
- BeautifulSoup heading extraction
- Reversed ranking output

## Technologies

Python, Requests, BeautifulSoup.

## Installation

```powershell
cd web-scraping-selenium/top-100-movies-scraper
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Run with internet access. Results are printed and saved to notes.txt.

## Current limitations

Depends on an archived page and its h3.title markup. Empty or changed responses are not detected. The number of extracted results depends on the returned page.
