# Video Title Search and Sort API

This project implements two Flask applications that demonstrate searching and sorting functionality for a collection of video titles.

## Features

- Binary Search API (app.py)
- Merge Sort API (app2.py)
- Pre-defined collection of educational video titles
- RESTful endpoints for searching and sorting

## Applications

### Search API (app.py)
- Implements binary search algorithm
- Endpoint: `/search?query=<video_title>`
- Returns exact matches for video titles

### Sort API (app2.py)
- Implements merge sort algorithm
- Endpoint: `/sort`
- Returns alphabetically sorted list of all video titles

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install flask
