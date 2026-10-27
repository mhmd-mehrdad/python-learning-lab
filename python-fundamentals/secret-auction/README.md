# Secret Auction

Collects named bids and reports the highest bidder.

## Features

- Dictionary-based bid storage
- Maximum-bid comparison

## Technologies

Python standard library; terminal input/output, functions, collections, and control flow.

## Installation

```powershell
cd python-fundamentals/secret-auction
python -m venv .venv
```

Use Python 3.10 or newer. On macOS/Linux, the environment interpreter is `.venv/bin/python`.

## Usage

Run from this project directory so relative resource paths resolve correctly:

```powershell
.\.venv\Scripts\python.exe main.py
```

Enter a name and bid; type yes to add another bidder.

## Current limitations

Clearing the display uses blank lines; bids are not securely hidden. Positive integer bids are assumed.
