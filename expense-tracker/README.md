# Python Expense Tracker

## About the Project

A menu-driven command-line Expense Tracker built using Python. It helps users record expenses, view saved expenses, and calculate totals by category.

## Features

- Add an expense with amount, category, and date.
- View all recorded expenses.
- Calculate totals for each category.
- Display the grand total of all expenses.
- Validate amount, category, date, and menu input.
- Save expenses in a JSON file so data persists between runs.

## Requirements

- Python 3
- Visual Studio Code or another Python editor

No external Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal in the repository's root folder.
4. Run:

   ```bash
   python expense-tracker/main.py
   ```

5. Select a menu option:
   - `1` — Add Expense
   - `2` — View All Expenses
   - `3` — Total by Category
   - `4` — Exit

## Data Storage

Expenses are stored in `expenses.json`. The program loads saved expenses when it starts and saves new expenses when they are added.

## Sample Data

The `expenses.json` file contains sample expense records that can be used to test the program.

## Concepts Practised

- Python functions
- Lists and dictionaries
- Loops and conditional statements
- Input validation and exception handling
- JSON file handling
- Date validation

