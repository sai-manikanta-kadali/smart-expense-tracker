# Smart Expense Tracker

A command-line Python application for modelling income and expense transactions with object-oriented programming. It calculates totals, maintains an in-memory transaction history, and prints a financial summary.

## Features

- Create income and expense transactions.
- Validate positive transaction amounts and non-empty descriptions.
- Add and display wallet transactions.
- Calculate total income, total expenses, and current balance.
- Print a simple financial summary.
- Demonstrate Python special methods such as `__len__`, `__getitem__`, `__contains__`, and `__str__`.

## OOP concepts

- Abstract base class and inheritance
- Encapsulation through a validated amount property
- Method overriding and polymorphism
- Composition (Wallet contains transactions)
- Static and class methods
- Dunder methods

## Project structure

```text
smart-expense-tracker/
├── main.py
├── transaction.py
├── wallet.py
├── reports.py
└── README.md
```

## Run locally

```bash
git clone https://github.com/sai-manikanta-kadali/smart-expense-tracker.git
cd smart-expense-tracker
python3 main.py
```

No external dependencies are required.

## Current scope

Transactions are stored in memory and reset when the program exits. This project does not yet include a database, recurring transactions, authentication, or a graphical interface. It is an OOP learning project rather than a financial product.

---

Built to practise Python classes, validation, composition, and maintainable program structure.