import unittest
from domain.customer import Customer
from service.account_service import AccountService

class TestAccountService(unittest.TestCase):
    def test_create_account(self):
        account_service = AccountService()
        customer = Customer(1, "John Doe", "john@example.com", "123-456-7890")
        
        account = account_service.create_account(customer.customer_id, customer.name, customer.email, customer.phone_number)

        self.assertEqual(account.customer_id, customer.customer_id)
        self.assertEqual(account.get_balance(), 0.0)
        self.assertEqual(len(account.get_transaction_history()), 0)
        self.assertIsNotNone(account.account_id)
        self.assertIsNotNone(account.account_number)
        