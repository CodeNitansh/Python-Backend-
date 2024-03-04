from datetime import datetime

class Account:
    def __init__(self, account_id, customer_id, account_number):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self._record_transaction(amount, 'deposit')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction(amount, 'withdraw')

    def get_balance(self):
        return self.balance

    def _record_transaction(self, amount, transaction_type):
        timestamp = datetime.now()
        transaction_details = {
            'timestamp': timestamp,
            'amount': amount,
            'transaction_type': transaction_type
        }
        self.transaction_history.append(transaction_details)

    def get_transaction_history(self):
        return self.transaction_history
