import unittest
from domain.account import Account
from service.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):
    def test_make_transaction(self):
        transaction_service = TransactionService()
        account = Account(1, 1, "123456789")
        
        transaction_service.make_transaction(account, 100.0, 'deposit')

        self.assertEqual(account.get_balance(), 100.0)
        self.assertEqual(len(account.get_transaction_history()), 1)

        transaction_service.make_transaction(account, 50.0, 'withdraw')

        self.assertEqual(account.get_balance(), 50.0)
        self.assertEqual(len(account.get_transaction_history()), 2)
        
