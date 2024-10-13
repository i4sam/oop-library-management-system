# OOP Library & Accounting Management System

### A Python application demonstrating core Object-Oriented Programming principles with a modern GUI interface.



## Project Overview

This project is a Python application that shows Object-Oriented Programming (OOP) principles using a graphical user interface (GUI) made with Tkinter. The main goal is to demonstrate **Aggregation**, **Abstraction**, and **Encapsulation** while managing a library system, processing payments, and handling accounting transactions. The GUI has a Dracula theme that gives it a professional, modern look.

## Features
- **Library Management**: Manage a collection of books easily using aggregation.
- **Payment Processing**: Different payment methods, including Credit Card and PayPal.
- **Accounting Tool**: Track income and expenses with a balance calculator.
- **GUI Interface**: An interactive Tkinter interface with a Dracula theme for a better user experience.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://https://github.com/i4sam/oop-library-management-system.git
   cd OOP-Library-Accounting-System
2. **Install Dependencies**:
   ```bash
   Make sure you have Python 3 and Tkinter installed on your system.
3. **Install Dependencies**:
   ```bash
   python gui_app.py
 ## Project Structure
   ```bash
   OOP-Library-Accounting-System/
   ├── gui_app.py              # Main GUI application file
   ├── library.py              # Library and Book class   definitions
   ├── payment.py              # PaymentMethod class and   its subclasses
   ├── accounting.py           # AccountingTool class for   transaction tracking
   ├── README.md               # Project documentation
   └── requirements.txt        # List of dependencies (if   applicable)
   ```

## Code Explanation
   ***Library Management (Aggregation):*** The Library class manages a collection of Book objects, showing how aggregation works.
   ```bash
   # library.py
    class Book:
        def __init__(self, title, author, publication_year):
            self.title = title
            self.author = author
            self.publication_year = publication_year

    class Library:
        def __init__(self):
            self.books = []  # Aggregates Book objects

        def add_book(self, book):
            self.books.append(book)

```
  ***Payment Processing (Abstraction):*** The PaymentMethod abstract class provides a template for different payment methods.
   ```bash
  # payment.py
    from abc import ABC, abstractmethod

    class PaymentMethod(ABC):
        @abstractmethod
        def process_payment(self, amount):
            pass

    class CreditCardPayment(PaymentMethod):
        def process_payment(self, amount):
            return f'Processed credit card payment of ${amount}'


```

 ***Accounting Tool (Encapsulation):*** The AccountingTool class handles financial transactions.
   ```bash
    # accounting.py
    class AccountingTool:
        def __init__(self):
            self.transactions = []
            self.balance = 0

        def add_income(self, amount):
            self.transactions.append({'type': 'income', 'amount': amount})
            self.balance += amount



```
***Graphical User Interface (Dracula Theme):*** The Tkinter GUI makes it easy to use the application.
   ```bash
   # gui_app.py
    import tkinter as tk

    root = tk.Tk()
    root.title("OOP Application - Dracula Theme")
    root.config(bg="#282a36")  # Background color

    add_book_button = tk.Button(root, text="Add Book", command=add_book_function, bg="#6272a4", fg="#f8f8f2")
    add_book_button.pack()

    root.mainloop()




```

 ## Key OOP Principles Used
- **Aggregation**: Library class aggregates Book objects.
- **Abstraction**: The PaymentMethod class serves as a base for payment types.
- **Encapsulation**: The AccountingTool class keeps transactions and balance together.
