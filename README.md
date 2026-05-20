# API to Excel with Python

A simple Python project that fetches user data from a public API and saves it into an Excel file.

---

## Features

- Fetch data from a REST API
- Convert JSON response into Python objects
- Export data to an Excel file
- Beginner-friendly Python project
- Simple Git & GitHub workflow

---

## Technologies Used

- Python
- Requests
- OpenPyXL
- Git
- GitHub

---

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
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/najafi81/api-to-excel.git
```

Go to project directory:

```bash
cd api-to-excel
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the project:

```bash
python main.py
```

The program will:

1. Send a request to a public API
2. Receive JSON data
3. Process the response
4. Generate an Excel file

Output file:

```text
data/users.xlsx
```

---

## API Used

This project uses the free public API:

```text
https://jsonplaceholder.typicode.com/users
```

JSONPlaceholder is commonly used for testing and learning API integration.

---

## Example Output

The generated Excel file contains:

| ID | Name | Username | Email | City | Company |
|----|------|-----------|--------|------|----------|

---

## Future Improvements

- Add error handling
- Add logging
- Save timestamped Excel files
- Export CSV files
- Add command-line arguments
- Use environment variables
- Create a GUI version

---

## Author

Meisam Najafi

GitHub:
https://github.com/najafi81
