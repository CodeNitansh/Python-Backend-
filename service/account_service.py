from domain.account import Account
import uuid

class AccountService:
    def create_account(self, customer_id, name, email, phone_number):
        account_id = str(uuid.uuid4()) 
        account_number = self.generate_unique_account_number()

        return Account(account_id, customer_id, account_number)

    @staticmethod
    def generate_unique_account_number():
        return str(uuid.uuid4().int)  # For simplicity, using the integer representation of UUID
