import logging
from datetime import datetime

class TransactionService:
    def __init__(self):
        self.transaction_history = []

    def make_transaction(self, account, amount, transaction_type):
        try:
            if transaction_type == 'deposit':
                account.deposit(amount)
            elif transaction_type == 'withdraw':
                account.withdraw(amount)
            else:
                raise ValueError("Invalid transaction type")

            # Record the transaction in history
            self._record_transaction(account, amount, transaction_type)

            # Log the transaction
            self._log_transaction(account, amount, transaction_type)

        except ValueError as e:
            # Handle insufficient funds or other errors
            logging.error(f"Transaction failed: {str(e)}")

    def _record_transaction(self, account, amount, transaction_type):
        timestamp = datetime.now()
        transaction_details = {
            'timestamp': timestamp,
            'account_id': account.account_id,
            'amount': amount,
            'transaction_type': transaction_type
        }
        self.transaction_history.append(transaction_details)

    def _log_transaction(self, account, amount, transaction_type):
        log_message = f"{transaction_type.capitalize()} of {amount} on account {account.account_id}. "
        log_message += f"Current balance: {account.get_balance()}"
        logging.info(log_message)
