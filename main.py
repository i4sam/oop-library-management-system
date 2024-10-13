# main.py

from library import Library, Book
from payment import CreditCardPayment, PayPalPayment
from accounting import AccountingTool
import argparse

def main():
    # Create objects
    library = Library()
    accounting = AccountingTool()
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    
    # Add some books to the library
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    
    # Perform some transactions
    accounting.add_income(500)
    accounting.add_expense(150)
    
    # Process a payment
    print(credit_card_payment.process_payment(100))
    print(paypal_payment.process_payment(75))
    
    # Display library books
    print("\nLibrary Books:")
    library.show_books()
    
    # Show balance and transactions
    print("\nAccounting:")
    print(accounting.show_balance())
    accounting.show_transactions()

if __name__ == "__main__":
    main()
