# Name Card Website

Serves a responsive profile card through Flask and a third-party HTML/CSS template.

## Features

- Flask template rendering
- Responsive card layout
- Bundled stylesheet and font assets

## Technologies

Python, Flask, HTML, CSS; HTML5 UP Identity template and Font Awesome.

## Installation

```powershell
cd flask-web-apps/name-card-website
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Open http://127.0.0.1:5000/ after starting the server. The displayed name, role, and avatar are neutral placeholders for customization.

## Current limitations

Social links are placeholders. Uses Flask debug mode for local development.

## Attribution

Design: [Identity by HTML5 UP](https://html5up.net), credited in the template and assets. The bundled template license is retained in `templates/LICENSE.txt`. Font Awesome and supporting scripts retain their own copyright/license notices. This project integrates and customizes an existing design; it does not claim authorship of that design.
