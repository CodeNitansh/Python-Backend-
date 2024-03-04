from datetime import datetime

class StatementService:
    def generate_account_statement(self, account):
        transaction_history = account.get_transaction_history()

        if not transaction_history:
            return "No transactions found for this account."

        statement = f"Account Statement for Account ID: {account.account_id}\n"
        statement += f"Customer ID: {account.customer_id}\n"
        statement += f"Balance: {account.get_balance()}\n\n"

        for transaction in transaction_history:
            statement += self._format_transaction_details(transaction) + "\n"

        return statement

    def _format_transaction_details(self, transaction):
        timestamp = transaction['timestamp']
        amount = transaction['amount']
        transaction_type = transaction['transaction_type']

        formatted_timestamp = datetime.strftime(timestamp, "%Y-%m-%d %H:%M:%S")
        formatted_amount = "{:.2f}".format(amount)  # Format amount with 2 decimal places

        return f"{formatted_timestamp} - {transaction_type.capitalize()}: {formatted_amount}"
