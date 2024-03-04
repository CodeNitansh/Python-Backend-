from domain.customer import Customer
from service.account_service import AccountService
from service.transaction_service import TransactionService
from service.statement_service import StatementService
from infra.account_repository import AccountRepository

def main():
    # Creating customers
    customer1 = Customer(1, "Nitansh V", "nitansh.v@banking.com", "123-456-7890")
    customer2 = Customer(2, "John Doe", "john.d@banking.com", "987-654-3210")

    # Creating accounts for customers
    account_service = AccountService()
    account1 = account_service.create_account(customer1.customer_id, customer1.name, customer1.email, customer1.phone_number)
    account2 = account_service.create_account(customer2.customer_id, customer2.name, customer2.email, customer2.phone_number)

    # Making transactions
    transaction_service = TransactionService()
    transaction_service.make_transaction(account1, 100.0, 'deposit')
    transaction_service.make_transaction(account1, 50.0, 'withdraw')
    transaction_service.make_transaction(account2, 200.0, 'deposit')

    # Generating account statements
    statement_service = StatementService()
    statement1 = statement_service.generate_account_statement(account1)
    statement2 = statement_service.generate_account_statement(account2)

    # Printing results
    print("Customer 1:", customer1.name)
    print("Account 1 ID:", account1.account_id)
    print("Balance 1:", account1.get_balance())
    print("Account 1 Statement:")
    print(statement1)

    print("\nCustomer 2:", customer2.name)
    print("Account 2 ID:", account2.account_id)
    print("Balance 2:", account2.get_balance())
    print("Account 2 Statement:")
    print(statement2)

if __name__ == "__main__":
    main()
