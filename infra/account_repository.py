import sqlite3
from domain.account import Account

class AccountRepository:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                account_number TEXT,
                balance REAL
            )
        ''')
        self.conn.commit()

    def save_account(self, account):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO accounts (customer_id, account_number, balance)
            VALUES (?, ?, ?)
        ''', (account.customer_id, account.account_number, account.get_balance()))
        self.conn.commit()

    def find_account_by_id(self, account_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE account_id = ?', (account_id,))
        result = cursor.fetchone()
        if result:
            account = Account(result[0], result[1], result[2])
            account.balance = result[3]
            return account
        return None

    def find_accounts_by_customer_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE customer_id = ?', (customer_id,))
        results = cursor.fetchall()
        accounts = [Account(result[0], result[1], result[2]) for result in results]
        for account, result in zip(accounts, results):
            account.balance = result[3]
        return accounts

