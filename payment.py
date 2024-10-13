# payment.py

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f'Processed credit card payment of ${amount}'

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f'Processed PayPal payment of ${amount}'
