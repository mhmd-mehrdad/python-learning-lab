# Mail Merge

Creates personalized letters by replacing a name placeholder in a text template.

## Features

- Name-list input
- Template substitution
- One output file per recipient

## Technologies

Python standard-library file I/O and string methods.

## Installation

```powershell
cd oop-games-gui/mail-merge
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Edit the fictional names in Input/Names/invited_names.txt and the template in Input/Letters/starting_letter.txt. Generated letters appear under Output/ReadyToSend.

Generated letters are ignored by Git. No email is sent.
