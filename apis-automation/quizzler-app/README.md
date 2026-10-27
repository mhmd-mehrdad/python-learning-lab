# Quizzler

Fetches true/false trivia questions and presents them in a desktop quiz.

## Features

- Open Trivia DB requests
- HTML entity decoding
- Answer feedback and scoring

## Technologies

Python, Requests, Tkinter; separate question, quiz, and UI classes.

## Installation

```powershell
cd apis-automation/quizzler-app
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`. A desktop session and Python with Tk support are required; Tkinter and Turtle are included with Tk-enabled Python installations.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Click the check or cross button to answer each question. An internet connection is required.

## Current limitations

Network/API failures are not retried. The on-screen final score label can lag the last answer.
