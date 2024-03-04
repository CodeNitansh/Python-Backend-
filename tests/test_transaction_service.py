import unittest
from domain.account import Account
from service.transaction_service import TransactionService
from service.statement_service import StatementService  # Import StatementService

class TestTransactionService(unittest.TestCase):
    def test_make_transaction(self):
        transaction_service = TransactionService()
        statement_service = StatementService()  # Create an instance of StatementService
        account = Account(1, 1, "123456789")
        
        # Initial balance is 0.0, so the initial statement should mention no transactions.
        statement = statement_service.generate_account_statement(account)
        self.assertIn("No transactions found for this account.", statement)

        transaction_service.make_transaction(account, 100.0, 'deposit')
        statement = statement_service.generate_account_statement(account)
        
        self.assertIn("Account Statement", statement)
        self.assertIn("Balance", statement)
        self.assertIn("Deposit", statement)
        self.assertIn("100.00", statement)
        self.assertNotIn("No transactions found for this account.", statement)