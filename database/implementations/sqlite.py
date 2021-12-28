
import sqlite3 as sq
from decimal import Decimal
from typing import List

from accounts.account import Account


class AccountDatabaseSqlite:
    def __init__(self, conn: str):
        self.connection = sq.connect(conn, check_same_thread=False)
        cursor = self.connection.execute("""
        CREATE TABLE IF NOT EXISTS kaspi_accounts (
            id varchar primary key ,
            currency varchar ,
            balance decimal 
        );
        """)
        cursor.close()
        print("Table created successfully")
        self.connection.commit()

    def new_acc(self, account: Account) -> None:
        cursor = self.connection.execute("""
                INSERT OR REPLACE INTO kaspi_accounts (id, currency, balance) VALUES (?, ?, ?);
                """, (str(account.id_), account.currency, account.balance))
        self.connection.commit()

    def get_accounts(self) -> List[Account]:
        cursor = self.connection.execute("SELECT id, currency, balance FROM kaspi_accounts")
        data = cursor.fetchall()
        return data

    def max_balance_kzt(self):
        cursor = self.connection.execute("SELECT MAX(balance) FROM kaspi_accounts WHERE currency = 'KZT'")
        for row in cursor:
            return row[0]

    def max_balance_usd(self):
        cursor = self.connection.execute("SELECT MAX(balance) FROM kaspi_accounts WHERE currency = 'USD'")
        for row in cursor:
            return row[0]

    def max_balance_eur(self):
        cursor = self.connection.execute("SELECT MAX(balance) FROM kaspi_accounts WHERE currency = 'EUR'")
        for row in cursor:
            return row[0]

    def delete_accounts(self):
        cursor = self.connection.execute("DELETE from kaspi_accounts;")
        self.connection.commit()
        cursor.close()

    def add_balance(self, id_: str, ball: Decimal):
        cursor = self.connection.cursor()
        sql_update_query = """Update kaspi_accounts set balance = balance + ? where id = ?"""
        data = (ball, id_)
        cursor.execute(sql_update_query, data)
        self.connection.commit()
        print("Balance updated successfully")
        cursor.close()

    def send_balance(self, from_id: str, to_id: str, ball: Decimal):
        cursor = self.connection.cursor()
        sql_update_fromId = """Update kaspi_accounts set balance = balance - ? where id = ?"""
        data_from = (ball, from_id)
        cursor.execute(sql_update_fromId, data_from)
        sql_update_toId = """Update kaspi_accounts set balance = balance + ? where id = ?"""
        data_to = (ball, to_id)
        cursor.execute(sql_update_toId, data_to)
        self.connection.commit()
        print("Balance sended successfully")
        cursor.close()

    def close_conn(self):
        self.connection.close()





