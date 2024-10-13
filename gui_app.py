import tkinter as tk
from tkinter import messagebox
from library import Library, Book
from payment import CreditCardPayment, PayPalPayment
from accounting import AccountingTool


# Initialize the main components
library = Library()
accounting = AccountingTool()
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Create the main GUI application window
root = tk.Tk()
root.title("Library & Accounting Tool")
root.geometry("550x600")
root.configure(bg="#282a36")  # Dracula theme background color

# --- Dracula Theme Colors ---
background_color = "#282a36"
foreground_color = "#f8f8f2"
button_color = "#44475a"
button_hover_color = "#6272a4"
highlight_color = "#bd93f9"
input_color = "#44475a"

# Styling function for hover effects
def on_hover(button, color):
    button['background'] = color

def on_leave(button, color):
    button['background'] = color

# --- Header Label ---
title_label = tk.Label(root, text="📚 Library & Accounting Tool 💵", font=("Arial", 16, "bold"),
                       bg=background_color, fg=highlight_color)
title_label.pack(pady=20)

# --- Library Section ---
library_frame = tk.Frame(root, bg=background_color)
library_frame.pack(pady=10)

library_label = tk.Label(library_frame, text="Add a Book to the Library:", font=("Arial", 12), bg=background_color, fg=foreground_color)
library_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

title_entry = tk.Entry(library_frame, width=20, bg=input_color, fg=foreground_color, insertbackground=foreground_color)
title_entry.grid(row=1, column=0, padx=5)
title_entry.insert(0, "Title")

author_entry = tk.Entry(library_frame, width=20, bg=input_color, fg=foreground_color, insertbackground=foreground_color)
author_entry.grid(row=1, column=1, padx=5)
author_entry.insert(0, "Author")

year_entry = tk.Entry(library_frame, width=10, bg=input_color, fg=foreground_color, insertbackground=foreground_color)
year_entry.grid(row=1, column=2, padx=5)
year_entry.insert(0, "Year")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    library.add_book(Book(title, author, int(year)))
    messagebox.showinfo("Success", f"Added '{title}' to the library!")

add_book_button = tk.Button(library_frame, text="Add Book", command=add_book, bg=button_color, fg=foreground_color, relief="flat")
add_book_button.grid(row=1, column=3, padx=5)
add_book_button.bind("<Enter>", lambda e: on_hover(add_book_button, button_hover_color))
add_book_button.bind("<Leave>", lambda e: on_leave(add_book_button, button_color))

def show_books():
    books = "\n".join([book.details() for book in library.books])
    messagebox.showinfo("Library Books", books)

show_books_button = tk.Button(library_frame, text="Show Library Books", command=show_books, bg=button_color, fg=foreground_color, relief="flat")
show_books_button.grid(row=2, column=0, columnspan=4, pady=10)
show_books_button.bind("<Enter>", lambda e: on_hover(show_books_button, button_hover_color))
show_books_button.bind("<Leave>", lambda e: on_leave(show_books_button, button_color))

# --- Payment & Accounting Section ---
accounting_frame = tk.Frame(root, bg=background_color)
accounting_frame.pack(pady=10)

payment_label = tk.Label(accounting_frame, text="Process a Payment:", font=("Arial", 12), bg=background_color, fg=foreground_color)
payment_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

amount_entry = tk.Entry(accounting_frame, width=15, bg=input_color, fg=foreground_color, insertbackground=foreground_color)
amount_entry.grid(row=1, column=0, padx=5)
amount_entry.insert(0, "Amount")

def process_credit_card_payment():
    amount = int(amount_entry.get())
    messagebox.showinfo("Payment Processed", credit_card_payment.process_payment(amount))

def process_paypal_payment():
    amount = int(amount_entry.get())
    messagebox.showinfo("Payment Processed", paypal_payment.process_payment(amount))

credit_card_button = tk.Button(accounting_frame, text="Credit Card", command=process_credit_card_payment, bg=button_color, fg=foreground_color, relief="flat")
credit_card_button.grid(row=1, column=1, padx=5)
credit_card_button.bind("<Enter>", lambda e: on_hover(credit_card_button, button_hover_color))
credit_card_button.bind("<Leave>", lambda e: on_leave(credit_card_button, button_color))

paypal_button = tk.Button(accounting_frame, text="PayPal", command=process_paypal_payment, bg=button_color, fg=foreground_color, relief="flat")
paypal_button.grid(row=1, column=2, padx=5)
paypal_button.bind("<Enter>", lambda e: on_hover(paypal_button, button_hover_color))
paypal_button.bind("<Leave>", lambda e: on_leave(paypal_button, button_color))

# --- Accounting Balance & Transactions ---
def add_income():
    amount = int(amount_entry.get())
    accounting.add_income(amount)
    messagebox.showinfo("Transaction", f"Income of ${amount} added to balance!")

def add_expense():
    amount = int(amount_entry.get())
    accounting.add_expense(amount)
    messagebox.showinfo("Transaction", f"Expense of ${amount} subtracted from balance!")

income_button = tk.Button(accounting_frame, text="Add Income", command=add_income, bg=button_color, fg=foreground_color, relief="flat")
income_button.grid(row=2, column=0, pady=10)
income_button.bind("<Enter>", lambda e: on_hover(income_button, button_hover_color))
income_button.bind("<Leave>", lambda e: on_leave(income_button, button_color))

expense_button = tk.Button(accounting_frame, text="Add Expense", command=add_expense, bg=button_color, fg=foreground_color, relief="flat")
expense_button.grid(row=2, column=1, pady=10)
expense_button.bind("<Enter>", lambda e: on_hover(expense_button, button_hover_color))
expense_button.bind("<Leave>", lambda e: on_leave(expense_button, button_color))

def show_balance():
    balance = accounting.show_balance()
    transactions = "\n".join([f"{trans['type']}: ${trans['amount']}" for trans in accounting.transactions])
    messagebox.showinfo("Account Balance", f"{balance}\n\nTransactions:\n{transactions}")

balance_button = tk.Button(accounting_frame, text="Show Balance", command=show_balance, bg=button_color, fg=foreground_color, relief="flat")
balance_button.grid(row=2, column=2, pady=10)
balance_button.bind("<Enter>", lambda e: on_hover(balance_button, button_hover_color))
balance_button.bind("<Leave>", lambda e: on_leave(balance_button, button_color))

# Run the main application loop
root.mainloop()
