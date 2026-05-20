# API to Excel with Python

A simple Python project that fetches user data from a public API and saves it into an Excel file.

## Features

- Fetch data from a REST API
- Convert JSON response to Python objects
- Export selected fields to Excel
- Simple and beginner-friendly structure

## Technologies

- Python
- Requests
- OpenPyXL
- Git & GitHub

## Project Structure

```text
api-to-excel/
├── data/
│   └── users.xlsx
├── screenshots/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Installation
Bash
git clone https://github.com/najafi81/api-to-excel.git
cd api-to-excel
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Usage
Bash
python main.py

The output Excel file will be created as:
Plain text
data/users.xlsx

API Used
This project uses the JSONPlaceholder public API:
Plain text
https://jsonplaceholder.typicode.com/users

Future Improvements
Add error handling
Add timestamped Excel filenames
Add command-line arguments
Use environment variables
Add logging
