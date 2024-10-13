# accounting.py

class AccountingTool:
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def add_income(self, amount):
        self.transactions.append({'type': 'income', 'amount': amount})
        self.balance += amount

    def add_expense(self, amount):
        self.transactions.append({'type': 'expense', 'amount': amount})
        self.balance -= amount

    def show_balance(self):
        return f'Current balance: ${self.balance}'

    def show_transactions(self):
        for transaction in self.transactions:
            print(f'Transaction: {transaction["type"]}, Amount: ${transaction["amount"]}')
