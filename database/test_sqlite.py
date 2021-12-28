
from database.implementations.sqlite import AccountDatabaseSqlite


class TestSqlite:

    def test_connection(self) -> None:
        conn = 'db.sqlite3'
        db = AccountDatabaseSqlite(conn=conn)
        db.close_conn()




