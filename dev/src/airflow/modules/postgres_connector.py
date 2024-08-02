from psycopg2 import connect
from psycopg2 import DatabaseError

"""
This module provides functions to deal with postgres connections.

Includes functions to establish a connection, execute a statement
and query a table.
"""


class PostgreSQLConnector:

    def __init__(
            self, host: str = "localhost",
            database: str = "postgres",
            user: str = "postgres",
            password: str = "postgres",
            port=5432) -> None:

        try:
            self.conn = connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port)

            self.cur = self.conn.cursor()

        except DatabaseError as d:
            print(f"{type(d).__name__:} {d}")

    def execute_statement(self, query: str) -> bool:

        try:
            self.cur.execute(query)

            self.conn.commit()

            return True

        except Exception as d:
            print(f"{type(d).__name__:} {d}")

            return False

    def query_database(self, query: str):
        try:
            self.cur.execute(query)

            return self.cur.fetchall()

        except Exception as e:
            print(f"{type(e).__name__:} {e}")

    def close_connection(self):
        self.cur.close()
        self.conn.close()


def main():
    connector = PostgreSQLConnector(
        database="crypto_ethereum",
        user="root",
        password="password"
    )

    query1 = """
        CREATE TABLE IF NOT EXISTS tokens(
        address TEXT NOT NULL,
        symbol TEXT,
        name TEXT,
        decimals TEXT,
        total_supply TEXT,
        block_timestamp TIMESTAMP NOT NULL,
        block_number INTEGER NOT NULL,
        block_hash TEXT NOT NULL);
    """

    query2 = """
        INSERT INTO tokens
        VALUES (
            '0x142362602f1b1ce711a9ea72a8089f49ef6e3021',
            'ETH',
            'ETH...',
            '18',
            '100000000000000000000000000',
            '2024-01-18 22:17:47.000000 UTC',
            '19036676',
            '0x8f28059bebf9a4b55b80307ab34eeda2737a68fd38030c53ea376ee549c70cc0'
        )
    """

    query3 = """
        SELECT * FROM tokens
        LIMIT 2
    """
    connector.execute_statement(query1)
    connector.execute_statement(query2)
    print(connector.query_database(query3))


if __name__ == "__main__":
    main()
